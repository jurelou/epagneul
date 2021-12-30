from typing import Union

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class EdgeData(BaseModel):
    source: str
    target: str
    label: str
    id: str = Field(default_factory=lambda : uuid4().hex)

class Edge(BaseModel):
    data: EdgeData


class NodeData(BaseModel):
    label: str = ""
    bg_opacity : float = 1.0
    bg_color: str = "black"
    border_color: str = "black"
    parent: str = None
    shape: str = "circle"
    tip: str = ""
    width: int = 50
    height: int = 50
    id: str = Field(default_factory=lambda : uuid4().hex)

class Node(BaseModel):
    data: NodeData

