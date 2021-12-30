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
import ipaddress

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
    domain: str = ""

    @validator("ip")
    def validate_ip(cls, value):
        if value in ("::1", "127.0.0.1"):
            return ""
        return value or ""


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
        if value and value == "S-1-5-7": # skip Anonymous Logon	
            return ""
        return value


    @validator("domain")
    def validate_domain(cls, value):
        return value.split("@")[0].strip().lower() or ""

    @validator("username")
    def validate_username(cls, value):
        v = value.split("@")[0].strip().lower().strip("$")
        return (v[:-1] if v[-1:] == "$" else v) or ""


class LogonEvent(BaseModel):
    identifier: Optional[str]

    source: str
    target: str
    event_id: int
    timestamp: datetime.datetime 
    logon_type: int = 0
    status: str = ""

    count: int = 1


HCHECK = r"[*\\/|:\"<>?&]"

USEFULL_EVENTS_STR = re.compile(r'<EventID>(4624|4625|4648|4768|4769|4771|4776|4672)', re.MULTILINE)

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
    t = convert_logtime(xml_event.xpath("/Event/System/TimeCreated")[0].get("SystemTime"))

    return Event(
        event_id=int(xml_event.xpath("/Event/System/EventID")[0].text),
        #computer_name=xml_event.xpath("/Event/System/Computer")[0].text,
        timestamp=t, #datetime.datetime(*t.timetuple()[:4]),
        data=xml_event.xpath("/Event/EventData/Data")
    )

def merge_models(a, b):
    print("->", dir(a))

class Datastore:
    def __init__(self):
        self.machines = {}
        self.users = {}
        self.logon_events = {}

    def add_logon_event(self, event):
        event.identifier = f"{event.event_id}-{event.source}-{event.target}"

        if event.identifier in self.logon_events:
            self.logon_events[event.identifier].count = self.logon_events[event.identifier].count + 1
        else:
            self.logon_events[event.identifier] = event
        return event.identifier

    def add_machine(self, machine: Machine):
        if machine.ip:
            machine.identifier = machine.ip
        elif machine.hostname:
            machine.identifier = f"computer-{machine.hostname}"
        else:
            return None

        if machine.identifier not in self.machines:
            self.machines[machine.identifier] = machine
        elif machine.ip and machine.hostname:
            if not self.machines[machine.ip].hostname:
                self.machines[machine.ip].hostname = machine.hostname            
            elif machine.hostname != self.machines[machine.ip].hostname:
                print(f"/!\ 2 hostnames for {machine.ip}: {machine.hostname} && {self.machines[machine.ip].hostname}")
        return machine.identifier

    def add_user(self, user: User):
        if not user.sid:
            return None

        is_unique_sid = user.sid.count("-") != 3
        user.identifier = user.sid if is_unique_sid else user.username
        if user.identifier not in self.users:
            self.users[user.identifier] = user

        if user.sid == "S-1-5-18":
            self.users[user.identifier].is_admin = True
            self.users[user.identifier].role = "System (or LocalSystem)"
        elif user.sid == "S-1-5-19":
            self.users[user.identifier].is_admin = True
            self.users[user.identifier].role = "NT Authority (LocalService)"
        elif user.sid == "S-1-5-20":
            self.users[user.identifier].is_admin = True
            self.users[user.identifier].role = "Network Service"
        elif user.sid == "S-1-5-32-544":
            self.users[user.identifier].is_admin = True
            self.users[user.identifier].role = "Administrator"
        elif user.sid == "S-1-5-32-547":
            self.users[user.identifier].is_admin = True
            self.users[user.identifier].role = "Power User"

        elif is_unique_sid:
            user_sid_suffix = user.sid[-4:]
            if user_sid_suffix == "-500":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Domain local administrator"
            elif user_sid_suffix == "-502":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "krbtgt"
            elif user_sid_suffix == "-512":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Domain Admin"
            elif user_sid_suffix == "-517":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Cert Publisher"
            elif user_sid_suffix == "-518":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Schema Admin"
            elif user_sid_suffix == "-519":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Enterprise Admin"
            elif user_sid_suffix == "-520":
                self.users[user.identifier].is_admin = True
                self.users[user.identifier].role = "Group Policy Creator Owner"
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
        # https://github.com/JPCERTCC/LogonTracer/blob/master/logontracer.py#L875

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
        elif event.event_id == 4648:
            user = User()
            machine = Machine()
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

            user_id = store.add_user(user)
            machine_id = store.add_machine(machine)

            if user_id and machine_id:

                store.add_logon_event(LogonEvent(
                    timestamp=event.timestamp,
                    event_id=event.event_id,
                    source=user_id,
                    target=machine_id,
                    )
                )
        else:
            user = User()
            machine = Machine()
            logon_type = 0
            status = ""
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

if __name__ == "__main__":
    from epagneul.api.core.neo4j import get_database
    

    db = get_database()
    db.bootstrap()
    #db.rm()
    
    store = parse_evtx("/data/filtered2.evtx")
    #db.add_evtx_store(store, folder="lol")

    #db.make_lpa("lol")
    #db.make_pagerank("lol")

    #a = db.get_graph("lol")
    #db.add_many_machines(store.machines.values(), folder="lol")
    #db.add_many_logon_events(store.logon_events.values(), folder="lol")
    