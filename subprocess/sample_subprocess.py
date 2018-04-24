#!/usr/bin/env python3

import os
import subprocess

popen = subprocess.Popen(
    ['env'],
    cwd=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)))),
    env={},
)
popen.wait()
print(popen.returncode)
