# -*- coding: utf-8 -*-

import pydantic


class BaseModel(pydantic.BaseModel):
    machine_key: str = ""

    def model_name(self):
        return self.schema()["title"]

    class Config:
        extra = "allow"
