# -*- coding: utf-8 -*-
from .base import BaseObservable


class Account(BaseObservable):
    name: str
    domain: str = ""

    def unique_key(self):
        return self.name
