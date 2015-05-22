#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from twython import Twython

#This is a script that will tweet the actuall CPU THemperature of the Orange Pi.
CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#Setting up the cmd variable containig a simple bash command.
cmd = 'cat --squeeze-blank /sys/class/thermal/thermal_zone0/temp'
#Formate the variable cmd
temp = os.popen(cmd).readline().strip()

# The actuall tweet
api.update_status(status='My CPU is '+temp+'° C hot. #orangepi #bot')
