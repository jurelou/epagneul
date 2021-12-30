# -*- coding: utf-8 -*-
from typing import Optional

from epagneul.models import BaseModel


class BaseObservable(BaseModel):

    detection_key: Optional[str] = None

    def unique_key(self):
        raise NotImplementedError(f"{type(self).__name__} does not have a unique key.")
