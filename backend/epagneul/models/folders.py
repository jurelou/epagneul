from typing import List, Union, Optional

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4
from neo4j.time import DateTime

from .files import File
from .graph import Node, Edge

class Folder(BaseModel):
    name: str
    summary: str
    timestamp: Union[datetime, DateTime] = Field(default_factory=datetime.now)
    identifier: str = Field(default_factory=lambda : uuid4().hex)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda date: datetime.strftime(date, "%e/%m/%Y %H:%M:%S"),
            DateTime: lambda date: datetime.strftime(datetime(date.year, date.month, date.day, date.hour, date.minute, int(date.second), int(date.second * 1000000 % 1000000), tzinfo=date.tzinfo), "%e/%m/%Y %H:%M:%S")
        }

class MachineStat(BaseModel):
    identifier: str
    pagerank: float

class UserStat(BaseModel):
    identifier: str
    pagerank: float

class Stats(BaseModel):
    machines_stats: List[MachineStat] = []
    users_stats: List[UserStat] = []

class FolderInDB(BaseModel):
    name: str
    summary: str
    start_time: Optional[Union[datetime, DateTime]]
    end_time: Optional[Union[datetime, DateTime]]

    timestamp: Union[datetime, DateTime] = Field(default_factory=datetime.now)
    identifier: str = Field(default_factory=lambda : uuid4().hex)
    files: List[File] = []
    nodes: List[Node] = []
    edges: List[Edge] = []
    stats: Stats = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda date: datetime.strftime(date, "%Y-%m-%dT%H:%M:%S"),
            DateTime: lambda date: datetime.strftime(datetime(date.year, date.month, date.day, date.hour, date.minute, int(date.second), int(date.second * 1000000 % 1000000), tzinfo=date.tzinfo), "%Y-%m-%dT%H:%M:%S")
        }

