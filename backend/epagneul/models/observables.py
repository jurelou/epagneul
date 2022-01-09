from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any
import datetime

class NonEmptyValuesModel(BaseModel):
    def __setattr__(self, name, value):
        if value and value != "-":
            super().__setattr__(name, value)

    class Config:
        validate_assignment = True

class Observable(NonEmptyValuesModel):
    id : Optional[str]

class ObservableInDB(Observable):
    label: str = ""
    category: str

    bg_opacity: float = 1.0
    bg_color: str = "black"
    border_color: str = "black"
    parent: str = None
    shape: str = "circle"
    tip: str = ""
    width: int = 50
    height: int = 50

    algo_lpa: int = -1
    #algo_pagerank: float = 0.15
    #timeline: List[int] = []
    #algo_change_finder: ??


class Machine(Observable):
    hostname: Optional[str]
    domain: Optional[str]
    ip: Optional[str]
    ips: set = set()

    def add_ip(self, ip: str):
        if not ip or ip in ("::1", "127.0.0.1"):
            return None
        self.ips.add(ip)

    @validator("ip")
    def validate_ip(cls, value):
        if not value or value in ("::1", "127.0.0.1"):
            return ""
        return value


    @validator("hostname", "domain")
    def validate_hostname(cls, value):
        v = value.split("@")[0].strip().lower().strip("$")
        if not v or v in "localhost" :
            return ""
        return v


class User(Observable):
    username: Optional[str]
    sid: Optional[str]
    domain: Optional[str]
    is_admin: bool = False
    role: str = "???"

    @validator("sid")
    def validate_sid(cls, value):
        if value and value in ("S-1-0-0", "S-1-5-7"): # skip Anonymous Logon
            return ""
        return value

    @validator("domain")
    def validate_domain(cls, value):
        return value.split("@")[0].strip().lower() or ""

    @validator("username")
    def validate_username(cls, value):
        v = value.split("@")[0].strip().lower().strip("$")
        v = v[:-1] if v[-1:] == "$" else v
        if not v or v == "anonymous logon":
            return ""
        return v