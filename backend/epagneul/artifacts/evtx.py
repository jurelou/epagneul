# -*- coding: utf-8 -*-
from evtx import PyEvtxParser
from lxml import etree
from loguru import logger
import re
import datetime
from epagneul.common import settings
from epagneul.models.graph import Node, Edge
from typing import Optional, List, Any
from pydantic import BaseModel, Field, validator
import pandas as pd
import numpy as np
import ipaddress
#from hmmlearn import hmm
#import joblib
from epagneul.api.core.changefinder import ChangeFinder

"""
Champs uniques dans le domaine:
    ComputerName
    Sids
    
relations:
    (machine)-(contains)->(user)
        # Event: 4672

    (username)-(member_of)->(domain)
    (machine)-(login)->(username)
        # Event: 4624 An account was successfully logged on
        # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624
        -   IpAddress || Workstation || WorkstationName-(login)->TargetUserSid || TargetSid
        -   TargetUserName-(member_of)->TargetDomainName
        -   TargetUserSid || TargetSid<->TargetUserName
        #  Event: 4625 An account failed to log on
        -   idem
        #  Event: 4768 A Kerberos authentication ticket (TGT) was requested
        -   idem
        #  Event: 4769 A Kerberos service ticket was requested
        -   idem
        #  Event: 4776 The domain controller attempted to validate the credentials for an account
        -   idem

    (username)-(created)->(username)
        # Event: 4720 A user account was created.
        # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720
        -   SubjectUserSid-(created)->(TargetSid)
        -   SubjectUserSid<->SubjectUserName
        -   TargetSid<->TargetUserName
        -   DisplayName / SamAccountName / UserWorkstations / AccountExpires / UserParameters / SidHistory

    (username)-(deleted)->(username)
        # Event: 4726 A user account was deleted.
        # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4726
        -   SubjectUserSid-(deleted)->(TargetSid)
        -   SubjectUserSid<->SubjectUserName
        -   TargetSid<->TargetUserName
        -   PrivilegeList

    (username)-(added_to)->(group)
        # Event: 4728 A member was added to a security-enabled global group
        # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4732
        -   MemberSid-(added_to)->(TargetSid)
        -   MemberSid <-> MemberName
        -   TargetSid <-> TargetUserName
        -   MemberName / TargetUserName / TargetDomainName / SubjectUserName (créateur)
        # Event: 4732 A member was added to a security-enabled local group
            - idem 
        # Event: 4756 A member was added to a security-enabled universal group
            - idem 

    (username)-(removed_from)->(group)
        # Event: 4729 A member was removed from a security-enabled global group
        # https://docs.microsoft.com/fr-fr/windows/security/threat-protection/auditing/event-4733
        -   MemberSid-(removed_from)->(TargetSid)
        -   MemberSid <-> MemberName
        -   TargetSid <-> TargetUserName
        -   MemberName / TargetUserName / TargetDomainName / SubjectUserName (créateur)
        # Event: 4733 A member was removed from a security-enabled local  group
            - idem        
        # Event: 4757 A member was removed from a security-enabled universal  group
            - idem 

    (username)-(uses)->(policy)
        # Event: 4719 System audit policy was changed.
        # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4719
        -   SubjectUserName-(uses)->CategoryId 
        -   SubjectDomainName / SubcategoryId / SubcategoryGuid


"""
class Event(BaseModel):
    event_id: int
    #computer_name: str
    timestamp: datetime.datetime
    data: Any

class NonEmptyValuesModel(BaseModel):
    def __setattr__(self, name, value):
        if value and value != "-":
            super().__setattr__(name, value)

    class Config:
        validate_assignment = True

class Machine(NonEmptyValuesModel):
    identifier : str = ""

    hostname: str = ""

    ip: str = ""
    ips: set = set()

    domain: str = ""

    def add_ip(self, ip: str):
        if not ip or ip in ("::1", "127.0.0.1"):
            return None
        self.ips.add(ip)

    @validator("ip")
    def validate_ip(cls, value):
        if not value or value in ("::1", "127.0.0.1"):
            return ""
        return value


    @validator("hostname", "domain")
    def validate_hostname(cls, value):
        v = value.split("@")[0].strip().lower().strip("$")
        if not v or v == "localhost":
            return ""
        return v


class Domain(NonEmptyValuesModel):
    name: Optional[str]

class User(NonEmptyValuesModel):
    identifier : str = ""

    username: str = ""
    sid: str = ""
    domain: str = ""
    is_admin: bool = False
    role: str = "user?"

    @validator("sid")
    def validate_sid(cls, value):
        if value and value in ("S-1-0-0", "S-1-5-7"): # skip Anonymous Logon
            return ""
        return value

    @validator("domain")
    def validate_domain(cls, value):
        return value.split("@")[0].strip().lower() or ""

    @validator("username")
    def validate_username(cls, value):
        v = value.split("@")[0].strip().lower().strip("$")
        v = v[:-1] if v[-1:] == "$" else v
        if not v or v == "anonymous logon":
            return ""
        return v


class BaseLogonEvent(BaseModel):
    source: str
    target: str
    event_id: int
    logon_type: int = 0
    status: str = ""

class LogonEvent(BaseLogonEvent):
    timestamp: datetime.datetime 

class MergedLogonEvent(BaseLogonEvent):
    timestamps: set = set()


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
                known_machines[machine.identifier] = machine

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
                known_users[user.username] = user



        self.users = known_users
        """
        for v in sorted(self.users.values(), key=lambda x: x.username):
            print("UUU",  v.identifier, v)
        for v in sorted(self.machines.values(), key=lambda x: x.hostname):
            print("MMM",  v.identifier, v)
        """
        for event in self.logon_events.values():
            if event.target not in self.machines:
                for m in self.machines.values():
                    if event.target == m.hostname or event.target in m.ips:
                        event.target = m.identifier
                        break
            if event.source not in self.users:
                for u in self.users.values():
                    if event.source == u.sid or event.source == u.username:
                        event.source = u.identifier
                        break
            for ts in event.timestamps:
                self.add_ml_frame([ts.strftime("%Y-%m-%d %H:%M:%S"), event.event_id, event.source])


    def add_timestamp(self, timestamp):
        if not self.start_time:
            self.start_time = timestamp
        elif self.start_time > timestamp:
            self.start_time = timestamp

        if not self.end_time:
            self.end_time = timestamp
        elif self.end_time < timestamp:
            self.end_time = timestamp

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
        identifier = f"{event.source}-{event.target}-{event.event_id}-{event.logon_type}"
        if identifier in self.logon_events:
            self.logon_events[identifier].timestamps.add(event.timestamp)
        else:
            self.logon_events[identifier] = MergedLogonEvent(**event.dict(exclude={'timestamp'}), timestamps={event.timestamp})

    def add_machine(self, machine: Machine):
        if machine.hostname:
            machine.identifier = machine.hostname
        elif machine.ip:
            machine.identifier = machine.ip
        else:
            return None
        
        if machine.identifier in self.machines:
            self.machines[machine.identifier] = merge_models(self.machines[machine.identifier], machine)
        else:
            self.machines[machine.identifier] = machine
        self.machines[machine.identifier].add_ip(machine.ip)
        return machine.identifier

    def add_user(self, user: User):
        if user.sid:
            # SID
            if user.sid.count("-") != 3:
                user.identifier = user.sid
            else:
                user.identifier = user.username
        elif user.username:
            # username
            user.identifier = user.username
        else:
            return None

        user.is_admin, user.role = get_role_from_sid(user)

        if user.identifier in self.users:
            self.users[user.identifier] = merge_models(self.users[user.identifier], user)
        else:
            self.users[user.identifier] = user
        
        return user.identifier


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
                store.add_logon_event(LogonEvent(
                    timestamp=event.timestamp,
                    event_id=event.event_id,
                    source=user_id,
                    target=machine_id,
                    logon_type=logon_type,
                    status=status
                    )
                )
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

    users = ['scep-service-ex', 'S-1-5-21-1614722772-2063729921-1886836735-1166', 'S-1-5-21-3190859163-3046400631-2231273112-500', 'S-1-5-21-1614722772-2063729921-1886836735-1217', 'S-1-5-21-1614722772-2063729921-1886836735-1453', 'S-1-5-21-1614722772-2063729921-1886836735-1270', 'S-1-5-21-1614722772-2063729921-1886836735-1515', 'S-1-5-21-1614722772-2063729921-1886836735-1862', 'S-1-5-80-1184457765-4068085190-3456807688-2200952327-3769537534', 'local service', 'S-1-5-90-0-1', 'network service', 'system', 'scep-service-rd', 'scep-infra-dc-a', 'S-1-5-21-1614722772-2063729921-1886836735-1105', 'S-1-5-21-1614722772-2063729921-1886836735-1791', '', 'S-1-5-21-1614722772-2063729921-1886836735-1549', 'S-1-5-90-1', 'S-1-5-21-1614722772-2063729921-1886836735-1366', 'S-1-5-21-1614722772-2063729921-1886836735-1001', 'S-1-5-21-1614722772-2063729921-1886836735-1107', 'S-1-5-21-1614722772-2063729921-1886836735-1106', 'S-1-5-21-1614722772-2063729921-1886836735-1898', 'S-1-5-21-1614722772-2063729921-1886836735-1784', 'S-1-5-21-1614722772-2063729921-1886836735-1104', 'S-1-5-21-1614722772-2063729921-1886836735-1897', 'S-1-5-21-1614722772-2063729921-1886836735-1108', 'scep-service-pk', 'iusr', 'S-1-5-21-1614722772-2063729921-1886836735-1165', 'scep-service-fi', 'S-1-5-21-1614722772-2063729921-1886836735-1109', 'S-1-5-21-1614722772-2063729921-1886836735-1110', 'S-1-5-21-1614722772-2063729921-1886836735-1112', 'S-1-5-21-1614722772-2063729921-1886836735-1814', 'S-1-5-21-1614722772-2063729921-1886836735-1113', 'S-1-5-21-1614722772-2063729921-1886836735-1111', 'S-1-5-21-1614722772-2063729921-1886836735-1884', 'S-1-5-21-1614722772-2063729921-1886836735-1115', 'S-1-5-21-1614722772-2063729921-1886836735-1735', 'S-1-5-21-1614722772-2063729921-1886836735-1116', 'S-1-5-21-1614722772-2063729921-1886836735-1118', 'S-1-5-21-1614722772-2063729921-1886836735-1295', 'S-1-5-21-1614722772-2063729921-1886836735-1117', 'S-1-5-21-1614722772-2063729921-1886836735-1114', 'S-1-5-21-1614722772-2063729921-1886836735-1347', 'S-1-5-21-1614722772-2063729921-1886836735-1759', 'S-1-5-21-1614722772-2063729921-1886836735-1851', 'S-1-5-21-1614722772-2063729921-1886836735-1516', 'S-1-5-21-1614722772-2063729921-1886836735-1684', 'S-1-5-21-1614722772-2063729921-1886836735-1121', 'S-1-5-21-1614722772-2063729921-1886836735-1119', 'S-1-5-21-1614722772-2063729921-1886836735-1123', 'S-1-5-21-1614722772-2063729921-1886836735-1120', 'S-1-5-21-1614722772-2063729921-1886836735-1122', 'S-1-5-21-1614722772-2063729921-1886836735-1797', 'S-1-5-21-1614722772-2063729921-1886836735-1849', 'S-1-5-21-1614722772-2063729921-1886836735-1361', 'S-1-5-21-1614722772-2063729921-1886836735-1127', 'S-1-5-21-1614722772-2063729921-1886836735-1467', 'S-1-5-21-1614722772-2063729921-1886836735-1128', 'S-1-5-21-1614722772-2063729921-1886836735-1367', 'S-1-5-21-1614722772-2063729921-1886836735-1125', 'S-1-5-21-1614722772-2063729921-1886836735-1124', 'S-1-5-21-1614722772-2063729921-1886836735-1126', 'S-1-5-21-1614722772-2063729921-1886836735-1129', 'S-1-5-21-1614722772-2063729921-1886836735-1133', 'S-1-5-21-1614722772-2063729921-1886836735-1509', 'S-1-5-21-1614722772-2063729921-1886836735-1130', 'S-1-5-21-1614722772-2063729921-1886836735-1131', 'S-1-5-21-1614722772-2063729921-1886836735-1369', 'S-1-5-21-1614722772-2063729921-1886836735-1132', 'S-1-5-21-1614722772-2063729921-1886836735-1534', 'S-1-5-21-1614722772-2063729921-1886836735-1134', 'scep-admin-wks1', 'scep-admin-wks2', 'scep-wks-02', 'scep-wks-01', 'scep-wks-03', 'scep-wks-06', 'scep-wks-04', 'scep-wks-07', 'scep-wks-05', 'scep-wks-09', 'scep-wks-08', 'scep-wks-12', 'scep-wks-10', 'scep-wks-11', 'scep-wks-13', 'scep-wks-18', 'scep-wks-16', 'scep-wks-17', 'scep-wks-14', 'scep-wks-15', 'scep-wks-23', 'scep-wks-21', 'scep-wks-22', 'scep-wks-19', 'scep-wks-20', 'scep-wks-24', 'S-1-5-21-1614722772-2063729921-1886836735-500', 'S-1-5-90-0-2', 'S-1-5-21-1493626464-1800764222-4210299026-500', 'S-1-5-21-143386994-2064860016-4136263729-500', 'S-1-5-21-2042724577-1801804113-2809386060-500', 'S-1-5-21-2492111565-2571168641-1099202330-500', 'S-1-5-21-1930436988-33830073-716220238-500', 'S-1-5-21-2105026350-389141950-1573985521-500', 'S-1-5-21-995854933-13933936-3220113501-500', 'S-1-5-21-2315413114-2228892671-2054880901-500', 'S-1-5-21-309712095-726237008-3563880964-500', 'S-1-5-21-1950601678-3807048000-3276331250-500', 'S-1-5-21-3816986116-4056927275-583030915-500', 'S-1-5-21-2947775960-2003569467-1206992157-500', 'S-1-5-21-3452268287-1118998018-1709054811-500', 'S-1-5-21-1541107420-194589081-2794743203-500', 'S-1-5-21-1278085612-538607690-602980321-500', 'S-1-5-21-443682548-66122474-1922608812-500', 'S-1-5-21-268263514-3082661447-3156119065-500', 'S-1-5-21-259117265-2066337403-3743540599-500', 'S-1-5-21-214208530-253367804-3631887496-500', 'S-1-5-21-2633843497-1387056221-1230101653-500', 'S-1-5-21-1225465739-1138774916-3069107167-500', 'S-1-5-21-2616939979-2839056425-4098346542-500', 'S-1-5-21-569642405-1079416390-590265888-500', 'S-1-5-21-2009882220-2748953025-2577819363-500', 'S-1-5-21-3450254828-2593496867-3440634386-500', 'S-1-5-21-2696980251-2893310999-3498759677-500', 'S-1-5-21-166234388-3044547414-104967907-500', 'S-1-5-21-2744361779-3909220837-3693416614-500', 'S-1-5-21-1040107654-1627049556-1359509401-500', 'S-1-5-21-1614722772-2063729921-1886836735-2605', 'nevergonnaletyoudown', 'scep.corp\\adm-ybenjamin', 'S-1-5-21-1614722772-2063729921-1886836735-1728', 'S-1-5-90-0-3']
    db = get_database()
    db.bootstrap()
    db.rm()
    
    store = parse_evtx("/data/filtered.evtx")

    store.finalize()

    #a, b, c = store.get_change_finder()

    """
    #start_day = datetime.datetime(*store.start_time.timetuple()[:3]).strftime("%Y-%m-%d")
    start_day = datetime.datetime.strptime("2021-12-09", "%Y-%m-%d") #temp
    learn_hmm(ml_frame, users, start_day)
    predictions = predict_hmm(ml_frame, users, start_day)
    print(predictions)
    """
    db.add_evtx_store(store, folder="a")

    db.make_lpa("a")
    db.make_pagerank("a")

    
    
"""
if __name__ == "__main__":
    from epagneul.api.core.neo4j import get_database

    users = ['scep-service-ex', 'S-1-5-21-1614722772-2063729921-1886836735-1166', 'S-1-5-21-3190859163-3046400631-2231273112-500', 'S-1-5-21-1614722772-2063729921-1886836735-1217', 'S-1-5-21-1614722772-2063729921-1886836735-1453', 'S-1-5-21-1614722772-2063729921-1886836735-1270', 'S-1-5-21-1614722772-2063729921-1886836735-1515', 'S-1-5-21-1614722772-2063729921-1886836735-1862', 'S-1-5-80-1184457765-4068085190-3456807688-2200952327-3769537534', 'local service', 'S-1-5-90-0-1', 'network service', 'system', 'scep-service-rd', 'scep-infra-dc-a', 'S-1-5-21-1614722772-2063729921-1886836735-1105', 'S-1-5-21-1614722772-2063729921-1886836735-1791', '', 'S-1-5-21-1614722772-2063729921-1886836735-1549', 'S-1-5-90-1', 'S-1-5-21-1614722772-2063729921-1886836735-1366', 'S-1-5-21-1614722772-2063729921-1886836735-1001', 'S-1-5-21-1614722772-2063729921-1886836735-1107', 'S-1-5-21-1614722772-2063729921-1886836735-1106', 'S-1-5-21-1614722772-2063729921-1886836735-1898', 'S-1-5-21-1614722772-2063729921-1886836735-1784', 'S-1-5-21-1614722772-2063729921-1886836735-1104', 'S-1-5-21-1614722772-2063729921-1886836735-1897', 'S-1-5-21-1614722772-2063729921-1886836735-1108', 'scep-service-pk', 'iusr', 'S-1-5-21-1614722772-2063729921-1886836735-1165', 'scep-service-fi', 'S-1-5-21-1614722772-2063729921-1886836735-1109', 'S-1-5-21-1614722772-2063729921-1886836735-1110', 'S-1-5-21-1614722772-2063729921-1886836735-1112', 'S-1-5-21-1614722772-2063729921-1886836735-1814', 'S-1-5-21-1614722772-2063729921-1886836735-1113', 'S-1-5-21-1614722772-2063729921-1886836735-1111', 'S-1-5-21-1614722772-2063729921-1886836735-1884', 'S-1-5-21-1614722772-2063729921-1886836735-1115', 'S-1-5-21-1614722772-2063729921-1886836735-1735', 'S-1-5-21-1614722772-2063729921-1886836735-1116', 'S-1-5-21-1614722772-2063729921-1886836735-1118', 'S-1-5-21-1614722772-2063729921-1886836735-1295', 'S-1-5-21-1614722772-2063729921-1886836735-1117', 'S-1-5-21-1614722772-2063729921-1886836735-1114', 'S-1-5-21-1614722772-2063729921-1886836735-1347', 'S-1-5-21-1614722772-2063729921-1886836735-1759', 'S-1-5-21-1614722772-2063729921-1886836735-1851', 'S-1-5-21-1614722772-2063729921-1886836735-1516', 'S-1-5-21-1614722772-2063729921-1886836735-1684', 'S-1-5-21-1614722772-2063729921-1886836735-1121', 'S-1-5-21-1614722772-2063729921-1886836735-1119', 'S-1-5-21-1614722772-2063729921-1886836735-1123', 'S-1-5-21-1614722772-2063729921-1886836735-1120', 'S-1-5-21-1614722772-2063729921-1886836735-1122', 'S-1-5-21-1614722772-2063729921-1886836735-1797', 'S-1-5-21-1614722772-2063729921-1886836735-1849', 'S-1-5-21-1614722772-2063729921-1886836735-1361', 'S-1-5-21-1614722772-2063729921-1886836735-1127', 'S-1-5-21-1614722772-2063729921-1886836735-1467', 'S-1-5-21-1614722772-2063729921-1886836735-1128', 'S-1-5-21-1614722772-2063729921-1886836735-1367', 'S-1-5-21-1614722772-2063729921-1886836735-1125', 'S-1-5-21-1614722772-2063729921-1886836735-1124', 'S-1-5-21-1614722772-2063729921-1886836735-1126', 'S-1-5-21-1614722772-2063729921-1886836735-1129', 'S-1-5-21-1614722772-2063729921-1886836735-1133', 'S-1-5-21-1614722772-2063729921-1886836735-1509', 'S-1-5-21-1614722772-2063729921-1886836735-1130', 'S-1-5-21-1614722772-2063729921-1886836735-1131', 'S-1-5-21-1614722772-2063729921-1886836735-1369', 'S-1-5-21-1614722772-2063729921-1886836735-1132', 'S-1-5-21-1614722772-2063729921-1886836735-1534', 'S-1-5-21-1614722772-2063729921-1886836735-1134', 'scep-admin-wks1', 'scep-admin-wks2', 'scep-wks-02', 'scep-wks-01', 'scep-wks-03', 'scep-wks-06', 'scep-wks-04', 'scep-wks-07', 'scep-wks-05', 'scep-wks-09', 'scep-wks-08', 'scep-wks-12', 'scep-wks-10', 'scep-wks-11', 'scep-wks-13', 'scep-wks-18', 'scep-wks-16', 'scep-wks-17', 'scep-wks-14', 'scep-wks-15', 'scep-wks-23', 'scep-wks-21', 'scep-wks-22', 'scep-wks-19', 'scep-wks-20', 'scep-wks-24', 'S-1-5-21-1614722772-2063729921-1886836735-500', 'S-1-5-90-0-2', 'S-1-5-21-1493626464-1800764222-4210299026-500', 'S-1-5-21-143386994-2064860016-4136263729-500', 'S-1-5-21-2042724577-1801804113-2809386060-500', 'S-1-5-21-2492111565-2571168641-1099202330-500', 'S-1-5-21-1930436988-33830073-716220238-500', 'S-1-5-21-2105026350-389141950-1573985521-500', 'S-1-5-21-995854933-13933936-3220113501-500', 'S-1-5-21-2315413114-2228892671-2054880901-500', 'S-1-5-21-309712095-726237008-3563880964-500', 'S-1-5-21-1950601678-3807048000-3276331250-500', 'S-1-5-21-3816986116-4056927275-583030915-500', 'S-1-5-21-2947775960-2003569467-1206992157-500', 'S-1-5-21-3452268287-1118998018-1709054811-500', 'S-1-5-21-1541107420-194589081-2794743203-500', 'S-1-5-21-1278085612-538607690-602980321-500', 'S-1-5-21-443682548-66122474-1922608812-500', 'S-1-5-21-268263514-3082661447-3156119065-500', 'S-1-5-21-259117265-2066337403-3743540599-500', 'S-1-5-21-214208530-253367804-3631887496-500', 'S-1-5-21-2633843497-1387056221-1230101653-500', 'S-1-5-21-1225465739-1138774916-3069107167-500', 'S-1-5-21-2616939979-2839056425-4098346542-500', 'S-1-5-21-569642405-1079416390-590265888-500', 'S-1-5-21-2009882220-2748953025-2577819363-500', 'S-1-5-21-3450254828-2593496867-3440634386-500', 'S-1-5-21-2696980251-2893310999-3498759677-500', 'S-1-5-21-166234388-3044547414-104967907-500', 'S-1-5-21-2744361779-3909220837-3693416614-500', 'S-1-5-21-1040107654-1627049556-1359509401-500', 'S-1-5-21-1614722772-2063729921-1886836735-2605', 'nevergonnaletyoudown', 'scep.corp\\adm-ybenjamin', 'S-1-5-21-1614722772-2063729921-1886836735-1728', 'S-1-5-90-0-3']
    db = get_database()
    db.bootstrap()
    db.rm()
    
    store = parse_evtx("/data/filtered2.evtx")
    count_set = pd.DataFrame(store.ml_list, columns =["dates", "eventid", "username"])

    count_set["count"] = count_set.groupby(["dates", "eventid", "username"])["dates"].transform("count")
    count_set = count_set.drop_duplicates()

    #count_set = pd.to_pickle(count_set, "ml_frame.pkl")

    tohours = 37# int((store.end_time - store.start_time).total_seconds() / 3600)

    timelines, detects, detect_cf = adetection(count_set, users, datetime.datetime.strptime("2021-12-09", "%Y-%m-%d"), tohours)
    
    i = 0
    for u in users:
        print(u, detects[i])
        i = i + 1

    s = {k: v for k, v in sorted(detect_cf.items(), key=lambda item: item[1])}
    print(s)

    #start_day = datetime.datetime(*store.start_time.timetuple()[:3]).strftime("%Y-%m-%d")
    start_day = datetime.datetime.strptime("2021-12-09", "%Y-%m-%d") #temp
    learn_hmm(ml_frame, users, start_day)
    predictions = predict_hmm(ml_frame, users, start_day)
    print(predictions)

    #db.add_evtx_store(store, folder="a")
    #db.make_lpa("a")
    #db.make_pagerank("a")
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