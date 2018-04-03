from tweepy import StreamListener
from tweepy import Stream
import tweepy
import cipher
import json


auth = tweepy.OAuthHandler(cipher.consumer_key, cipher.consumer_secret)
auth.set_access_token(cipher.access_token, cipher.access_token_secret)

api = tweepy.API(auth)

print('connect!')


class StdOutListener(StreamListener):

    def on_data(self, data):

        json_data = json.loads(data)
        print(json_data["text"])


    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=['979820330154889216'])





#     #override tweepy.StreamListener to add logic to on_status
# class MyStreamListener(tweepy.StreamListener):

#     def on_status(self, status):
#         print(status.text)


# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)


# mytwitID = ["1122642456"]

# myStream.filter(follow = mytwitID)


