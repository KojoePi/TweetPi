from twython import Twython, TwythonError
import datetime

CONSUMER_KEY = 'YOUR STRING'
CONSUMER_SECRET = 'YOUR STRING'
ACCESS_KEY = 'YOUR STRING'
ACCESS_SECRET = 'YOUR STRING'

#This contains your api keys
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Make an empty list named followers
followers = []

#Make a datestamp for the later output file
datestamp = datetime.datetime.now().strftime("%Y-%m-%d")

#Make a variable named username that will wait for the input of a username
username = raw_input("Retrieve Follower list of: ")

#We need this if the result is paginated
next_cursor = -1

#A while loop running until there are no further pages containing users.
#This will insert the username in our followers list.

while(next_cursor):
    get_followers = twitter.get_followers_list(screen_name=username,count=200,cursor=next_cursor)
    for follower in get_followers["users"]:
        followers.append(follower["screen_name"].encode("utf-8"))
        next_cursor = get_followers["next_cursor"]

#Make a new txt file named username+datestam.txt
followers_text = open(username+"-"+datestamp+".txt","a")

#Write the list in the new txt file
followers_text.write(%s has %s followers (%s):\n\n" % (str(username),str(len(followers)),str(datestamp))+"\n".join(followers))

#Close the file
followers_text.close()
