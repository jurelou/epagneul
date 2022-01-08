from pydantic import BaseModel, Field

from epagneul.models.events import EventInDB
from epagneul.models.observables import ObservableInDB


class Edge(BaseModel):
    data: EventInDB

class Node(BaseModel):
    data: ObservableInDB
