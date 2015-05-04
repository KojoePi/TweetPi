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

cmd = 'uptime'
uptime = os.popen(cmd).readline()

# Send a Tweet with the result of uptime
api.update_status(status='default@orangepiplus:/# '+uptime+'#orangepi #bot')
