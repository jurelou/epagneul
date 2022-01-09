from datetime import datetime
from typing import Union
from uuid import UUID, uuid4

from neo4j.time import DateTime
from pydantic import BaseModel, Field


class File(BaseModel):
    name: str
    start_time: int
    end_time: int

    timestamp: Union[datetime, DateTime] = Field(default_factory=datetime.now)
    identifier: UUID = Field(default_factory=lambda: uuid4().hex)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda date: datetime.strftime(date, "%e/%m/%Y %H:%M:%S"),
            DateTime: lambda date: datetime.strftime(
                datetime(
                    date.year,
                    date.month,
                    date.day,
                    date.hour,
                    date.minute,
                    int(date.second),
                    int(date.second * 1000000 % 1000000),
                    tzinfo=date.tzinfo,
                ),
                "%e/%m/%Y %H:%M:%S",
            ),
        }
