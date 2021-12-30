# -*- coding: utf-8 -*-
from .base import BaseObservable


class Process(BaseObservable):
    pid: str
    name: str = ""
    command_line: str = ""
    address: str = ""

    def unique_key(self):
        return self.pid
