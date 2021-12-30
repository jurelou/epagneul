# -*- coding: utf-8 -*-
from .base import BaseObservable


class IpAddress(BaseObservable):
    address: str

    def unique_key(self):
        return self.address
