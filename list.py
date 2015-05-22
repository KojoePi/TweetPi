#Importing time and random now!
# coding=utf8
from twython import Twython, TwythonError
import time
import random
#This is a script to post a list of tweets in an interval.

#This is imported to make SSL Connections work
import urllib3

#The path to your certificates
ca_certs = "/etc/ssl/certs/ca-certificates.crt"  # Or wherever it lives.

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=ca_certs,         # Path to your certificate bundle.
)

# You're ready to make verified HTTPS requests.
CONSUMER_KEY = 'YOUR STRING'
CONSUMER_SECRET = 'YOUR STRING'
ACCESS_KEY = 'YOUR STRING'
ACCESS_SECRET = 'YOUR STRING'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Small list of Tweets to Tweet
list = [
        "This is a post",
        "This is a post too"]

#This is called a while loop.
#It will be run as long as the lenght of the list is more than 0.
#If there is no entry anymore it will tweet the message you put in under else:
#The loop will be execute every 72 hours. You can change it in time.sleep . You have to write it in seconds!

while True:
    try:
        if len(list) > 0:
            list = tweets[random.randint(0,len(list))-1]
            twitter.update_status(status=toTweet)
            list.remove(toTweet)
            time.sleep(259201)
        else: #This tells what to tweet if there is no entry in your list anymore
#Oops! Our twitter.update_status should all be on one line!
            twitter.update_status(status="I just don't know what i could tell you! =(")
            break
    except TwythonError as e:
        print e
