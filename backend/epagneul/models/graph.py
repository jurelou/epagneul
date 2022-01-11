from epagneul.models.relationships import RelationshipInDB
from epagneul.models.observables import Observable
from pydantic import BaseModel


class Edge(BaseModel):
    data: RelationshipInDB


class Node(BaseModel):
    data: Observable
