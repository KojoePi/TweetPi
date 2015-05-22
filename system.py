#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
from twython import Twython
#A script to make the Orange Pi tweet his Debian Version
CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Set up a variable with a bash command.
cmd2 = 'uname -a'

#Formating the variable
kernel = os.popen(cmd2).readline()

# The actuall tweet with the Debian Version
api.update_status(status=''+kernel+' #orangepi #bot')
