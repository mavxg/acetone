#!/usr/bin/env python

import time
import sys
import explorerhat


V = 5.125

threshold = 2.5
delay = 0.25

calibrated = False

while (not calibrated):
    minimum = 1000.0
    maximum = 0.0
    t = time.strftime("%Y-%m-%dT%H:%M:%S")
    for i in range(5):
        time.sleep(1)
        V1  = explorerhat.analog.three.read()
        if (V1 < minimum):
            minimum = V1
        if (V1 > maximum):
            maximum = V1
    print('{2},{0:5.3f},{1:5.3f}'.format(minimum,maximum,t))
    sys.stdout.flush()
    change = maximum - minimum
    if (change < 0.05):
        calibrated = True

