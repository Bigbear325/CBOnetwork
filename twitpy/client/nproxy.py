import socket
import select
import time
import sys
import tweepy
import cipher
from random import *

class twitsend:
	"""this will be the twitter post method
		
		note:
		option 1. will directly create twit connection. 
		just for posting, will talk about getting(streaming) later

		option 2. creat socket. but I'm not sure
	"""

	def __init__(self, api):
		self.api = api

	def start(self, content):
		api.update_status('content->' + str(random() * 100)+ content);
		print "it works"

class TheProxy:
	"""this is the proxy class"""

	input_list = []
    # not use for now
    #channel = {}
	auth = tweepy.OAuthHandler(cipher.consumer_key, cipher.consumer_secret)
	auth.set_access_token(cipher.access_token, cipher.access_token_secret)
	api = tweepy.API(auth)

	def __init__(self, host, port):
		"""I think this is for connect the browser side"""
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(5)

    def main_loop(self):
    	self.input_list.append(self.server)
    	content = 'input:' + input_list
    	print(content)
    	self.on_accept()

    def on_accept(self):
    	twit = twitsend().start(content)

if __name__ == '__main__':
    proxy = TheProxy('127.0.0.1', 9090)
    proxy.main_loop()
