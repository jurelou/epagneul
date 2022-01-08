# -*- coding: utf-8 -*-
from evtx import PyEvtxParser
from lxml import etree
from loguru import logger
import re
import datetime
from epagneul.common import settings
from typing import Optional, List, Any
from pydantic import BaseModel
import pandas as pd
import numpy as np
import ipaddress

from epagneul.api.core.changefinder import ChangeFinder

from epagneul.models.observables import * 
from epagneul.models.events import * 

class Event(BaseModel):
    event_id: int
    timestamp: datetime.datetime
    data: Any


HCHECK = r"[*\\/|:\"<>?&]"

USEFULL_EVENTS_STR = re.compile(r'<EventID>(4624|4625|4648|4768|4769|4771|4776|4672)', re.MULTILINE)


KNOWN_ADMIN_SIDS = {
    "S-1-5-18": "System (or LocalSystem)",
    "S-1-5-19": "NT Authority (LocalService)",
    "S-1-5-20": "Network Service",
    "S-1-5-32-544": "Administrator",
    "S-1-5-32-547": "Power User",
}

KNOWN_ADMIN_SIDS_ENDINGS = {
    "-500": "Domain local administrator",
    "-502": "krbtgt",
    "-512": "Domain Admin",
    "-517": "Cert Publisher",
    "-518": "Schema Admin",
    "-519": "Enterprise Admin",
    "-520": "Group Policy Creator Owner"
}

def to_lxml(record_xml):
    rep_xml = record_xml.replace("xmlns=\"http://schemas.microsoft.com/win/2004/08/events/event\"", "")
    fin_xml = rep_xml.encode("utf-8")
    parser = etree.XMLParser(resolve_entities=False)
    return etree.fromstring(fin_xml, parser)

def convert_logtime(logtime, tzone=1):
    tzless = re.sub('[^0-9-:\s]', ' ', logtime.split(".")[0]).strip()
    try:
        return datetime.datetime.strptime(tzless, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=tzone)
    except:
        return datetime.datetime.strptime(tzless, "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(hours=tzone)

def get_event_from_xml(raw_xml_event):
    xml_event = to_lxml(raw_xml_event)
    return Event(
        event_id=int(xml_event.xpath("/Event/System/EventID")[0].text),
        #computer_name=xml_event.xpath("/Event/System/Computer")[0].text,
        timestamp=convert_logtime(xml_event.xpath("/Event/System/TimeCreated")[0].get("SystemTime")),
        data=xml_event.xpath("/Event/EventData/Data")
    )

def merge_models(a, b):
    for b_field in b.__fields__:
        b_field_value = getattr(b, b_field)
        if not b_field_value:
            continue
        a_field_value = getattr(a, b_field)

        if a_field_value == b_field_value:
            continue
        try:
            if a_field_value in b_field_value:
                # a is a subset of b
                setattr(a, b_field, b_field_value)
            continue
        except TypeError:
            pass
        
        if a_field_value:
            print(f"DOUBLE VALUE ({b_field}) {a_field_value} -- {b_field_value}")
        else:
            setattr(a, b_field, b_field_value)
    return a

def get_role_from_sid(user):
    if not user.sid:
        return False, None
    
    for sid, role in KNOWN_ADMIN_SIDS.items():
        if sid == user.sid:
            return True, role

    for sid, role in KNOWN_ADMIN_SIDS_ENDINGS.items():
        if user.sid.endswith(sid):
            return True, role

    return False, None

class Datastore:
    def __init__(self):
        self.machines = {}
        self.users = {}
        self.logon_events = {}
        #self.ml_frame = pd.DataFrame(index=[], columns=["dates", "eventid", "username"])
        
        self.ml_list = []

        self.start_time = None
        self.end_time = None

    def finalize(self):        
        # Remove duplicate machines
        known_machines = {}
        for k in list(self.machines.keys()):
            if self.machines[k].hostname:
                known_machines[k] = self.machines[k]
                del self.machines[k]

        for machine in self.machines.values():
            if not machine.hostname and not any(machine.ip in km.ips for km in known_machines.values()):
                known_machines[machine.id] = machine

        self.machines = known_machines

        # Remove duplicate users
        known_users = {}
        for k in list(self.users.keys()):
            if self.users[k].sid and self.users[k].username:
                known_users[k] = self.users[k]
                del self.users[k]

        for user in self.users.values():
            if user.username in known_users:
                known_users[user.username] = merge_models(known_users[user.username], user)
            else:
                for k, v in known_users.items():
                    if user.username == v.username and user.domain == v.domain:
                        known_users[k] = merge_models(known_users[k], user)
                        break
                else:
                    known_users[user.username] = user
        self.users = known_users

        for event in self.logon_events.values():
            if event.target not in self.machines:
                for m in self.machines.values():
                    if event.target == m.hostname or event.target in m.ips:
                        event.target = m.id
                        break
            if event.source not in self.users:
                for u in self.users.values():
                    if event.source == u.sid or event.source == u.username:
                        event.source = u.id
                        break
            event.source = f"user-{event.source}"
            event.target = f"machine-{event.target}"
            for ts in event.timestamps:
                self.add_ml_frame([ts.strftime("%Y-%m-%d %H:%M:%S"), event.event_type, event.source])


    def add_timestamp(self, timestamp):
        if not self.start_time:
            self.start_time = timestamp
        elif self.start_time > timestamp:
            self.start_time = timestamp

        if not self.end_time:
            self.end_time = timestamp
        elif self.end_time < timestamp:
            self.end_time = timestamp

    def get_timeline():
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "eventid", "username"])
        count_set["count"] = count_set.groupby(["dates", "eventid", "username"])["dates"].transform("count")
        return count_set.drop_duplicates()

    def get_change_finder(self):
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "eventid", "username"])
        count_set["count"] = count_set.groupby(["dates", "eventid", "username"])["dates"].transform("count")
        count_set = count_set.drop_duplicates()
        tohours = int((self.end_time - self.start_time).total_seconds() / 3600)
        return adetection(count_set, list(self.users.keys()), self.start_time, tohours)

    def add_ml_frame(self, frame):
        self.ml_list.append(frame)
        #self.ml_frame = self.ml_frame.append(series, ignore_index=True)

    def add_logon_event(self, event):
        identifier = f"{event.source}-{event.event_type}-{event.target}"
        if identifier in self.logon_events:
            self.logon_events[identifier].timestamps.add(event.timestamp)
        else:
            self.logon_events[identifier] = LogonEvent(**event.dict(exclude={'timestamp', 'timestamps'}), timestamps={event.timestamp})

    def add_machine(self, machine: Machine):
        if machine.hostname:
            machine.id = machine.hostname
        elif machine.ip:
            machine.id = machine.ip
        else:
            return None
        
        if machine.id in self.machines:
            self.machines[machine.id] = merge_models(self.machines[machine.id], machine)
        else:
            self.machines[machine.id] = machine
        self.machines[machine.id].add_ip(machine.ip)
        return machine.id

    def add_user(self, user: User):
        if user.sid:
            # SID
            if user.sid.count("-") != 3:
                user.id = user.sid
            else:
                user.id = user.username
        elif user.username:
            user.id = user.username
        else:
            return None

        user.is_admin, user.role = get_role_from_sid(user)

        if user.id in self.users:
            self.users[user.id] = merge_models(self.users[user.id], user)
        else:
            self.users[user.id] = user
        
        return user.id


def parse_evtx(file_data):
    logger.info(f"Parsing evtx file: {file_data}")
    evtx = PyEvtxParser(file_data)

    store = Datastore()

    for r in evtx.records():
        data = r["data"]
        if not "<Channel>Security" in data:
            continue

        if not re.search(USEFULL_EVENTS_STR, data):
            continue
        event = get_event_from_xml(data)
        store.add_timestamp(event.timestamp)
        

        ###############################################################
        # Admin users:
        #  EventID 4672: Special privileges assigned to new logon
        ###############################################################
        if event.event_id == 4672:
            user = User(is_admin=True, role="")
            for item in event.data:
                if not item.text:
                    continue
                name = item.get("Name")
                if name == "SubjectUserName":
                    user.username = item.text
                elif name == "SubjectUserSid":
                    user.sid = item.text
                elif name == "SubjectDomainName":
                    user.domain = item.text
            store.add_user(user)

        ###############################################################
        # Logon events:
        #  EventID 4624: An account was successfully logged on
        #  EventID 4625: An account failed to log on
        #  EventID 4768: A Kerberos authentication ticket (TGT) was requested
        #  EventID 4769: A Kerberos service ticket was requested
        #  EventID 4776: The domain controller attempted to validate the credentials for an account
        ###############################################################
        else:
            user = User()
            machine = Machine()
            logon_type = 0
            status = ""

            if event.event_id == 4648:
                for item in event.data:
                    if not item.text:
                        continue
                    name = item.get("Name")
                    if name == "SubjectUserSid":
                        user.sid = item.text
                    elif name == "SubjectUserName":
                        user.username = item.text
                    elif name == "SubjectDomainName":
                        user.domain = item.text
                    elif name == "TargetServerName":
                        machine.hostname = item.text
                    elif name == "TargetServerName":
                        machine.hostname = item.text
                    elif name == "TargetDomainName":
                        machine.domain = item.text
            else:
                for item in event.data:
                    if not item.text:
                        continue
                    name = item.get("Name")
                    if name in ("WorkstationName", "Workstation"):
                        machine.hostname = item.text
                    elif name == "IpAddress":
                        value = item.text.replace("::ffff:", "")
                        try:
                            ipaddress.ip_address(value)
                            machine.ip = value
                        except:
                            machine.hostname = value
                    elif name == "TargetUserName":
                        user.username = item.text
                    elif name == "TargetDomainName":
                        user.domain = item.text
                    elif name in ("TargetUserSid", "TargetSid"):
                        user.sid = item.text
                    #elif name == "SubjectDomainName" :
                    #    store.add_domain(Domain(name=item.text))
                    elif name == "LogonType":
                        logon_type = item.text
                    elif name == "Status":
                        status = item.text
                    #elif name == "AuthenticationPackageName":
                    #    relationship_data["AuthenticationPackageName"] = item.text
            user_id = store.add_user(user)
            machine_id = store.add_machine(machine)


            if user_id and machine_id:
                store.add_logon_event(SingleTimestampLogonEvent(
                    source=user_id,
                    target=machine_id,
                    event_type=event.event_id,

                    timestamp=event.timestamp,

                    logon_type=logon_type,
                    status=status
                ))
    return store

def adetection(counts, users, starttime, tohours):
    count_array = np.zeros((6, len(users), tohours + 1))
    count_all_array = []
    result_array = []
    cfdetect = {}
    for _, event in counts.iterrows():
        column = int((datetime.datetime.strptime(event["dates"], "%Y-%m-%d  %H:%M:%S") - starttime).total_seconds() / 3600)
        row = users.index(event["username"])
        # count_array[row, column, 0] = count_array[row, column, 0] + count
        if event["eventid"] == 4624:
            count_array[0, row, column] = event["count"]
        elif event["eventid"] == 4625:
            count_array[1, row, column] = event["count"]
        elif event["eventid"] == 4768:
            count_array[2, row, column] = event["count"]
        elif event["eventid"] == 4769:
            count_array[3, row, column] = event["count"]
        elif event["eventid"] == 4776:
            count_array[4, row, column] = event["count"]
        elif event["eventid"] == 4648:
            count_array[5, row, column] = event["count"]
    count_sum = np.sum(count_array, axis=0)
    count_average = count_sum.mean(axis=0)
    num = 0
    for udata in count_sum:
        cf = ChangeFinder(r=0.04, order=1, smooth=6)
        ret = []
        for i in count_average:
            cf.update(i)

        for i in udata:
            score = cf.update(i)
            ret.append(round(score[1], 2))
        result_array.append(ret)

        cfdetect[users[num]] = max(ret)

        count_all_array.append(udata.tolist())
        for var in range(0, 6):
            con = []
            for i in range(0, tohours + 1):
                con.append(count_array[var, num, i])
            count_all_array.append(con)
        num += 1

    return count_all_array, result_array, cfdetect


if __name__ == "__main__":
    from epagneul.api.core.neo4j import get_database

    db = get_database()
    db.bootstrap()
    db.rm()
    """
    store = parse_evtx("/data/filtered.evtx")
    store.finalize()
    """

    """
    #a, b, c = store.get_change_finder()
    #start_day = datetime.datetime(*store.start_time.timetuple()[:3]).strftime("%Y-%m-%d")
    start_day = datetime.datetime.strptime("2021-12-09", "%Y-%m-%d") #temp
    learn_hmm(ml_frame, users, start_day)
    predictions = predict_hmm(ml_frame, users, start_day)
    print(predictions)
    db.add_evtx_store(store, folder="a")

    db.make_lpa("a")
    db.make_pagerank("a")
    """


"""
def predict_hmm(frame, users, start_day):
    detections = []
    model = joblib.load("multinomial_hmm.pkl")

    while True:
        start_day_str = start_day.strftime("%Y-%m-%d")
        for user in users:
            hosts = np.unique(frame[(frame["user"] == user)].host.values)
            for host in hosts:
                udata = []

                for _, data in frame[(frame["date"].str.contains(start_day_str)) & (frame["user"] == user) & (frame["host"] == host)].iterrows():
                    id = data["id"]
                    if id == 4776:
                        udata.append(0)
                    elif id == 4768:
                        udata.append(1)
                    elif id == 4769:
                        udata.append(2)
                    elif id == 4624:
                        udata.append(3)
                    elif id == 4625:
                        udata.append(4)
                    elif id == 4648:
                        udata.append(5)

                if len(udata) > 2:
                    data_decode = model.predict(np.array([np.array(udata)], dtype="int").T)
                    unique_data = np.unique(data_decode)
                    if unique_data.shape[0] == 2:
                        if user not in detections:
                            detections.append(user)


        start_day += datetime.timedelta(days=1)
        if frame.loc[(frame["date"].str.contains(start_day_str))].empty:
            break
    return detections


def learn_hmm(frame, users, start_day):
    lengths = []
    data_array = np.array([])
    emission_probability = np.array([[0.09,   0.05,   0.35,   0.51],
                                     [0.0003, 0.0004, 0.0003, 0.999],
                                     [0.0003, 0.0004, 0.0003, 0.999]])

    while True:
        start_day_str = start_day.strftime("%Y-%m-%d")
        for user in users:
            hosts = np.unique(frame[(frame["user"] == user)].host.values)
            for host in hosts:
                udata = np.array([])
                for _, data in frame[(frame["date"].str.contains(start_day_str)) & (frame["user"] == user) & (frame["host"] == host)].iterrows():
                    udata = np.append(udata, data["id"])

                if udata.shape[0] > 2:
                    data_array = np.append(data_array, udata)
                    lengths.append(udata.shape[0])
        start_day += datetime.timedelta(days=1)
        if frame.loc[(frame["date"].str.contains(start_day_str))].empty:
            break

    data_array[data_array == 4776] = 0
    data_array[data_array == 4768] = 1
    data_array[data_array == 4769] = 2
    data_array[data_array == 4624] = 3
    data_array[data_array == 4625] = 4
    data_array[data_array == 4648] = 5

    model = hmm.MultinomialHMM(n_components=3, n_iter=10000)
    #model.emissionprob_ = emission_probability
    model.fit(np.array([data_array], dtype="int").T, lengths)
    joblib.dump(model, "./multinomial_hmm.pkl")
"""