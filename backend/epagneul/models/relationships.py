import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BaseRelationship(BaseModel):
    source: str
    target: str
    timestamps: set = set()
    event_type: int
    count: int = 1

    class Config:
        extra = "allow"


    class Config:
        extra = "allow"

class TimestampedRelationship(BaseRelationship):
    timestamp: datetime.datetime

class GroupRelationship(BaseRelationship):
    subject_user: Optional[str]
    subject_sid: Optional[str]
    privileges: Optional[str]


class NativeLogonRelationship(TimestampedRelationship):
    logon_type: int = 0
    status: str = ""


class SysmonLogonRelationship(TimestampedRelationship):
    initiated: Optional[bool]
    image: Optional[str]
    procotol: Optional[str]
    destination_port: Optional[int]
    source_port: Optional[int]


class RelationshipInDB(BaseRelationship):
    tip: str
    count: int = 1
    id: Optional[UUID]
