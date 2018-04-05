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

    def __init__(self):
        auth = tweepy.OAuthHandler(cipher.consumer_key, cipher.consumer_secret)
        auth.set_access_token(cipher.access_token, cipher.access_token_secret)
        self.api = tweepy.API(auth)

    def start(self, content):
	self.api.update_status('content->' + str(random() * 100)+ content)
	print "it works"

class TheProxy:
    def __init__(self, host, port):
	self.input_list = []
	self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	self.server.bind((host, port))
	self.server.listen(200)
        print('listen to host' + str(host) + ',port' + str(port))

    def main_loop(self):
	self.input_list.append(self.server)
        while 1:
            time.sleep(1)
            content = 'input:' + str(self.input_list)
	    #print(content)
	    self.on_accept(content)

    def on_accept(self,content):
        print(content)
        #twit = twitsend().start(content)

if __name__ == '__main__':
    proxy = TheProxy('127.0.0.1', 9090)
    try:
        proxy.main_loop()
    except KeyboardInterrupt:
	print "Ctrl C - Stopping server"
	sys.exit(1)
