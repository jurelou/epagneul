# -*- coding: utf-8 -*-
from .base import BaseObservable


class Logon(BaseObservable):
    id: str
    guid: str = ""

    def unique_key(self):
        return self.id
