# -*- coding: utf-8 -*-
from .base import BaseObservable


class Workstation(BaseObservable):
    name: str

    def unique_key(self):
        return self.name
