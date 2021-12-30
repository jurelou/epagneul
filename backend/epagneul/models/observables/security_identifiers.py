# -*- coding: utf-8 -*-
from .base import BaseObservable


class SecurityIdentifier(BaseObservable):
    sid: str

    def unique_key(self):
        return self.sid
