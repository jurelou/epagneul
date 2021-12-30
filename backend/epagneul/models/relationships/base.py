# -*- coding: utf-8 -*-
from enum import Enum, auto
from typing import List, Union, Optional
from datetime import datetime

from epagneul.models import BaseModel
from epagneul.models.observables.base import BaseObservable

ONE_OR_MANY_OBSERVABLES = Union[BaseObservable, List[BaseObservable]]


class RelationshipTypes(Enum):
    CREATES = auto()
    USES = auto()
    CONSISTS_OF = auto()
    LOGGED_TO = auto()


class Relationship(BaseModel):
    type: RelationshipTypes
    source: ONE_OR_MANY_OBSERVABLES
    target: ONE_OR_MANY_OBSERVABLES

    key: str
    comment: str
    artifact: str = ""
    sub_artifact: str = ""
    timestamp: Optional[datetime] = None

    class Config:
        extra = "allow"
