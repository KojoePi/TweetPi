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

#cmd = 'cat /etc/debian_version'
#debian = os.popen(cmd).readline()
cmd2 = 'uname -a'
kernel = os.popen(cmd2).readline()
# Tweet mit Debian Version
api.update_status(status=''+kernel+' #orangepi #bot')
