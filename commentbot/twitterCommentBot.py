import time
import random
from profile import my_email, my_password

import tweepy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys


CONSUMER_KEY = '9oix7X1CGe0qTH5Iy0DHIy9D2'
CONSUMER_SECRET = 'zyXMKSxY1YfyjX2ZSw1ZrJxALARj9Qe4EIEFC9X21EMFul8SY5'
ACCESS_TOKEN = '979820330154889216-FAWxAwGKJgAxAOXN24CPvEhKa86w0o0'
ACCESS_TOKEN_SECRET = '0e9obiLXcsNGpOPpJ8JrHu8YvbgNcvRysbpxI7omkA8Wh'



def login(driver, my_email, my_password):

    #initializing and login to twitter


    driver.get('https://twitter.com/login')
    time.sleep(1)
    email_sign = driver.find_element_by_css_selector("input.js-username-field.email-input.js-initial-focus")
    email_sign.send_keys(my_email)
    pwd_sign = driver.find_element_by_css_selector("input.js-password-field")
    pwd_sign.send_keys(my_password)
    pwd_sign.submit()
    time.sleep(2)

def open():
    driver.get('https://twitter.com')
    time.sleep(1)


def twit(message):
    time.sleep(1)
    message_box = driver.find_element_by_name("tweet")
    message_box.send_keys(message)
    message_box.send_keys(Keys.COMMAND, Keys.RETURN)


def oauth_login(consumer_key, consumer_secret, access_token, access_token_secret):
    """Authenticate with twitter using OAuth"""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    # auth_url = auth.get_authorization_url()

    # verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url)
    # auth.get_access_token(verify_code)

    return tweepy.API(auth)


def batch_delete(api):
    print "You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name
    # print "Does this sound ok? There is no undo! Type yes to carry out this action."
    # do_delete = raw_input("> ")
    # if do_delete.lower() == 'yes':
    count = 0
    for status in tweepy.Cursor(api.user_timeline).items():
        # if count == 5:
        #     break
        # count = count + 1
        try:
            api.destroy_status(status.id)
            print "Deleted:", status.id
        except:
            print "Failed to delete:", status.id



# random = random.randint(1,101)



if __name__ == "__main__":
    #prepare
    api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    batch_delete(api)
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    login(driver, my_email, my_password)
    open()
    count = 0
    while (count < 1000):
        twit("hello this is an test message number: " + str(count))
        count = count + 1
        if count % 5 == 0:
            time.sleep(2)
            print "Authenticated as: %s" % api.me().screen_name
            batch_delete(api)