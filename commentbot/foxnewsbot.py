import time
import random, string
from foxprofile import my_email, my_password

import tweepy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys



def login(driver, my_email, my_password):

    #initializing and login to twitter

    driver.get('http://www.foxnews.com/#')
    time.sleep(3)

    login_button = driver.find_element_by_class_name('login')
    login_button.click()
    time.sleep(1)
    email_sign = driver.find_element_by_id('email_login')
    email_sign.send_keys(my_email)

    pwd_sign = driver.find_element_by_id('password_login')
    pwd_sign.send_keys(my_password)

    submit_button = driver.find_element_by_id('btn-login')
    submit_button.click()
    print('login success!')

    time.sleep(2)

def open_page(driver, url):
    driver.get(url)

#modify the account, need to relogin to check the update??
def modify_account(driver, message):
    first_name = driver.find_element_by_name('first_name')
    first_name.clear()
    first_name.send_keys(message)
    # user_name.clear()
    # user_name.send_key(message)
    update_button = driver.find_element_by_id('save-profile')
    update_button.click()

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

if __name__ == "__main__":
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    login(driver, my_email, my_password)

    open_page(driver, 'https://www.foxnews.com/community/auth/user/profile.html')
    time.sleep(5)
    print 'profile page loaded'

    for i in range(0,300):
        message = randomword(15)
        print(message)
        modify_account(driver, message)
        print 'update success time %d : %s'% (i, message)
        time.sleep(5)