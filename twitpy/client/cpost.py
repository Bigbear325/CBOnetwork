import tweepy
import cipher
from random import *
import time, sys

auth = tweepy.OAuthHandler(cipher.consumer_key, cipher.consumer_secret)
auth.set_access_token(cipher.access_token, cipher.access_token_secret)

api = tweepy.API(auth)

api.update_status('tweepy + oauth!' + str(random() * 100))

for i in range(0,10):
#    rand = float(random() * 100)
	api.update_status('tweepy + oauth!' + str(random() * 100))
	time.sleep(1)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# user = api.get_user('twitlehighB')
# print user.screen_name
# print user.followers_count

# for friend in user.friends():
#    print friend.screen_name
