import tweepy
import cipher


auth = tweepy.OAuthHandler(cipher.consumer_key, cipher.consumer_secret)
auth.set_access_token(cipher.access_token, cipher.access_token_secret)

api = tweepy.API(auth)

// public_tweets = api.home_timeline()
// for tweet in public_tweets:
//     print(tweet.text)


