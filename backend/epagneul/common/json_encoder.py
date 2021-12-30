# -*- coding: utf-8 -*-
import json
from uuid import UUID


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        # elif isinstance(obj, datetime):
        #     return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)
