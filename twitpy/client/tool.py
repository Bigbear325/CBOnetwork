from twitter import *



consumer_key = 'BZBot1tkXKOkarmq4bWbrHAdW'

consumer_secret = 'tlsO1cRD2qCGPJxQTzA48Nl6ZFIX1QMmGytQPQ20OexZ1DQfvM'

token = '979820330154889216-FAWxAwGKJgAxAOXN24CPvEhKa86w0o0'

token_secret = '0e9obiLXcsNGpOPpJ8JrHu8YvbgNcvRysbpxI7omkA8Wh'


auth=OAuth(token, token_secret, consumer_key, consumer_secret)



twitter_userstream = TwitterStream(auth=auth, domain='twitter.com/twitlehigh')
for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        print msg['direct_message']['text']