#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import sys
import explorerhat


def button(channel):
    print("button pressed")
    # os.system("sudo shutdown -h now")


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback = button, bouncetime = 2000)

V = 5.125

threshold = 2.5
delay = 0.25

while True:
    t = time.strftime("%Y-%m-%dT%H:%M:%S")
    V1  = explorerhat.analog.three.read()
    print('{1},{0:5.3f}'.format(round(V1,3),t))
    sys.stdout.flush()
    time.sleep(delay)
