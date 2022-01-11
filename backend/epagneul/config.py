# -*- coding: utf-8 -*-
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.yaml"],
    environments=True,
)
