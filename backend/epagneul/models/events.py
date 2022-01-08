from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any
import datetime

class BaseEvent(BaseModel):
    source: str
    target: str
    timestamps: set = set()

class LogonEvent(BaseEvent):
    event_id: int
    logon_type: int = 0
    status: str = ""

class SingleTimestampLogonEvent(LogonEvent):
    timestamp: datetime.datetime

class EventInDB(BaseEvent):
    id: str
    label: str
    tip: str
