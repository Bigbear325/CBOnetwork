import time
import random
from profile import my_email, my_password

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys



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
    time.sleep(2)
    message_box = driver.find_element_by_name("tweet")
    message_box.send_keys(message)
    message_box.send_keys(Keys.COMMAND, Keys.RETURN)

def del()


# random = random.randint(1,101)
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
login(driver, my_email, my_password)
open()
count = 0
while(count < 1000):
    twit("this is an test message number: " + str(count))
    count = count + 1
