#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from twython import Twython

#A script that will tweet the uptime of your orange pi

CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#Setting up a variable 
cmd = 'uptime'
#Formate the variable
uptime = os.popen(cmd).readline()

# Send a Tweet with the result of uptime and some additional text.
api.update_status(status='default@orangepiplus:/# '+uptime+'#orangepi #bot')
