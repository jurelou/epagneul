from epagneul.models.events import EventInDB
from epagneul.models.observables import ObservableInDB
from pydantic import BaseModel


class Edge(BaseModel):
    data: EventInDB


class Node(BaseModel):
    data: ObservableInDB
