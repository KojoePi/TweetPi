#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from twython import Twython

CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
cmd = 'cat --squeeze-blank /sys/class/thermal/thermal_zone0/temp'
temp = os.popen(cmd).readline().strip()

# Tweet mit CPU Temperatur
api.update_status(status='Meine CPU ist '+temp+'° C warm. #orangepi #bot')
