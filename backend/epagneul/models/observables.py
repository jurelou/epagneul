from typing import Optional

from enum import Enum

from pydantic import BaseModel, validator, root_validator

class ObservableType(str, Enum):
    GROUP = "Group"
    MACHINE = "Machine"
    USER = "User"
    COMPOUND = "Compound"


class NonEmptyValuesModel(BaseModel):
    def __setattr__(self, name, value):
        if value and value != "-":
            super().__setattr__(name, value)

    class Config:
        validate_assignment = True


class Observable(NonEmptyValuesModel):
    id: Optional[str]

    category: ObservableType

    label: str = ""
    bg_opacity: float = 0.33
    bg_color: str = "grey"
    border_color: str = "grey"
    parent: str = None
    shape: str = "circle"
    tip: str = ""
    width: int = 50
    height: int = 50
    border_width: int = 5
    algo_lpa: int = -1

    class Config:
        use_enum_values = True
    # algo_pagerank: float = 0.15
    # timeline: List[int] = []
    # algo_change_finder: ??

class Group(Observable):
    category = ObservableType.GROUP

    sid: Optional[str]
    name: Optional[str]
    domain: Optional[str]

    shape: str = "hexagon"
    border_color: str = "#e7298a"


    def finalize(self):
        self.id = f"Group-{self.id}"
        self.label = self.name or self.sid
        self.tip = f"Name: {self.name}<br>SID: {self.sid}<br>Domain: {self.domain}"

class Machine(Observable):
    category = ObservableType.MACHINE

    hostname: Optional[str]
    domain: Optional[str]
    ip: Optional[str]
    ips: set = set()

    shape: str = "round-rectangle"
    border_color: str = "#7570b3"

    def finalize(self):
        self.id = f"Machine-{self.id}"
        self.label = self.hostname or self.ip
        self.tip = f"Hostname: {self.hostname}<br>Domain: {self.domain}<br>Ip(s): {', '.join(self.ips)}"


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
        if not value:
            return ""
        v = value.split("@")[0].strip().lower().strip("$")
        if v in "localhost":
            return ""
        return v

class User(Observable):
    category = ObservableType.USER

    username: Optional[str]
    sid: Optional[str]
    domain: Optional[str]
    is_admin: bool = False
    role: str = ""
    border_width: int = 2

    shape: str = "circle"
    border_color: str = "#e6ab02"

    def finalize(self):
        self.id = f"User-{self.id}"
        self.tip = f"Username: {self.username}<br>SID: {self.sid}<br>Domain: {self.domain}<br>Role: {self.role}"
        self.label = self.username

    @validator("sid")
    def validate_sid(cls, value):
        if value and value in ("S-1-0-0", "S-1-5-7"):  # skip Anonymous Logon
            return ""
        return value

    @validator("domain")
    def validate_domain(cls, value):
        if not value:
            return ""
        return value.split("@")[0].strip().lower() or ""

    @validator("username")
    def validate_username(cls, value):
        if not value:
            return ""
        v = value.split("@")[0].strip().lower().strip("$")
        v = v[:-1] if v[-1:] == "$" else v
        if not v or v == "anonymous logon":
            return ""
        return v

class LocalAdminUser(User):
    is_admin: bool = True
    role: str = "admin"

    border_color: str = "#d95f02"
    border_width: int = 4

class DomainAdminUser(User):
    is_admin: bool = True
    role: str = "admin"

    border_width: int = 6
    border_color: str = "#e31a1c"
