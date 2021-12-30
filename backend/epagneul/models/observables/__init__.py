# -*- coding: utf-8 -*-
from .logon import Logon
from .account import Account
from .process import Process
from .ip_address import IpAddress
from .workstation import Workstation
from .security_identifiers import SecurityIdentifier

ALL_OBSERVABLES = [Process, SecurityIdentifier, Account, Logon, Workstation, IpAddress]

__all__ = [o.schema()["title"] for o in ALL_OBSERVABLES]
