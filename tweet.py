#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from twython import Twython

#A Script that lets you send tweets through command line. Just type 'python tweet.py "YOUR STATUS" ' to send a tweet.

CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOUR KEY'
ACCESS_SECRET = 'YOUR SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#The command to make a tweet from command line
api.update_status(status=sys.argv[1])
