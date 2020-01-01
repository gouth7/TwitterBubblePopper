import urllib2
import time
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import re

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

#for status in tweepy.Cursor(api.home_timeline).items(200):
#	print(status._json)

def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False

friendship = api.show_friendship(source_screen_name='Gouthasoarus' ,target_id=599722912)
print friendship[0].following
#tweets given user likes
likes = api.favorites(id=974373447165005825)
print type(likes)
for ids in likes.ids():
    print "\n a tweet I like :"
    print(ids)
    print "\n people who also like it:"
    if (ids == 1181034966462930944):
        continue
    newFriends = get_user_ids_of_post_likes(ids)
    for friend in newFriends:
        if (friendship[0].following == False):
            print(friend)
            #try:
            #    res = api.create_friendship(friend)
            #    print(res.screen_name)
            #except:
            #    time.sleep(60)

