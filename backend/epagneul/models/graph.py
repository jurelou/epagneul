from typing import Union, Any

from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class EdgeData(BaseModel):
    source: str
    target: str
    label: str
    #tip: str
    timestamp: float
    

class Edge(BaseModel):
    data: EdgeData


class NodeData(BaseModel):
    id: str
    category: str

    label: str = ""

    bg_opacity : float = 1.0
    bg_color: str = "black"
    border_color: str = "black"
    parent: str = None
    shape: str = "circle"
    tip: str = ""
    width: int = 50
    height: int = 50
    algo_pagerank: float = 0.15
    timeline: Any

class Node(BaseModel):
    data: NodeData

