#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import sys
import explorerhat

ads = explorerhat.ads1015

run = True

def button(channel):
    global run
    run = False
    print("button pressed")
    # os.system("sudo shutdown -h now")


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback = button, bouncetime = 2000)

V = 5.125

delay = 0.5
rate = 128 # 250
def finger():
    ir.on()
    time.sleep(0.001)
    v = ads.read_se_adc(channel=0,programmable_gain=ads.PGA_0_512V,samples_per_second=rate)
    ir.off()
    return v

ir = explorerhat.output.one

count = 24

while run:
    t = time.strftime("%Y-%m-%dT%H:%M:%S")
    V1 = sum([finger()/count for x in range(count)])
    #V1 = finger()
    print('{1},{0:1.5f}'.format(V1,t))
    sys.stdout.flush()
    time.sleep(delay)

ir.off()
print("bye")
