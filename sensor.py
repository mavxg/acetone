#!/usr/bin/env python

import time
import sys
import explorerhat


V = 5.125

threshold = 2.5
delay = 0.25

while True:
    t = time.strftime("%Y-%m-%dT%H:%M:%S")
    V1  = explorerhat.analog.three.read()
    print('{1},{0:5.3f}'.format(round(V1,3),t))
    sys.stdout.flush()
    time.sleep(delay)
