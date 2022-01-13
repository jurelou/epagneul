import datetime
from typing import Optional
from uuid import UUID
from enum import Enum

from pydantic import BaseModel
from epagneul.models.observables import ObservableType

class RelationshipType(str, Enum):
    SUCCESSFULL_LOGON = "Successfull logon"
    FAILED_LOGON = "Failed logon"
    

    TGT_REQUEST = "TGT request"
    TGT_FAILED = "TGT failed"

    TGS_REQUEST = "TGS request"

    NTLM_REQUEST = "NTLM request"

    NETWORK_CONNECTION = "Network connection"
    LOGON_EXPLICIT_CREDS = "Logon w/ explicit credentials"
    GROUP_ADDED = "Group add"    

class BaseRelationship(BaseModel):
    source: str
    target: str
    event_type: RelationshipType
    count: int = 1

    class Config:
        extra = "allow"


class RelationshipInDB(BaseRelationship):
    tip: str
    count: int = 1

    id: Optional[UUID]
    timestamps: set = set()


class TimestampedRelationship(BaseRelationship):
    timestamp: datetime.datetime


class GroupRelationship(BaseRelationship):
    source_type = ObservableType.USER
    target_type = ObservableType.GROUP

    privileges: Optional[str]


class LogonRelationship(TimestampedRelationship):
    source_type = ObservableType.USER
    target_type = ObservableType.MACHINE


class NativeLogonRelationship(LogonRelationship):
    logon_type: int = 0
    status: str = ""


class SysmonLogonRelationship(LogonRelationship):
    initiated: Optional[bool]
    image: Optional[str]
    procotol: Optional[str]
    destination_port: Optional[int]
    source_port: Optional[int]
