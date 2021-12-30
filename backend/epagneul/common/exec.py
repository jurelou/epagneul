# -*- coding: utf-8 -*-
from subprocess import PIPE, Popen


def decode(data):
    return data.decode("utf-8", errors="replace")


def run_cmd(*cmd, stdin=None):
    stdin_pipe = None
    if stdin:
        stdin_pipe = PIPE

    proc = Popen(cmd, stdin=stdin_pipe, stdout=PIPE, stderr=PIPE)

    if stdin is not None:
        proc.stdin.write(str.encode(stdin))

    stdout, stderr = (decode(x.strip()) for x in proc.communicate())
    return proc.returncode, stdout, stderr
