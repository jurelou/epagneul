from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any
import datetime
from uuid import UUID

class BaseEvent(BaseModel):
    source: str
    target: str
    timestamps: set = set()
    event_type: int

class LogonEvent(BaseEvent):
    logon_type: int = 0
    status: str = ""

class SingleTimestampLogonEvent(LogonEvent):
    timestamp: datetime.datetime

class EventInDB(BaseEvent):
    tip: str
    id: Optional[UUID]
    
    class Config:
        extra: "allow"
