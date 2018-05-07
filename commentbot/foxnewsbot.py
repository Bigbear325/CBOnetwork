import time
import random, string
from foxprofile import my_email, my_password
from bs4 import BeautifulSoup

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


def post_comment(driver, message):
    time.sleep(5)
    post_message = driver.find_element_by_class_name('ql-editor ql-blank')
    post_message.send_keys(message)
    time.sleep(10)
    post_message.submit()




# def update_comment(driver, message):

if __name__ == "__main__":
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    login(driver, my_email, my_password)


    open_page(driver, 'http://www.foxnews.com/opinion/2018/04/01/what-is-easter-and-why-do-christians-celebrate-this-holiday.html')
    time.sleep(5)
    print 'news page loaded'

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    page_html = driver.page_source
    time.sleep(5)
    # print source

    # soup = BeautifulSoup(page_html, 'html')
    #
    # mydivs = soup.findAll("div", {"id": "commenting"})

    comment_url = "https://spoxy-shard4.spot.im/v2/spot/sp_ANQXRpqH/post/44cb71eb-b87a-47aa-8156-8fe92bf8054f/?elementId=ba314173ff98020a17b6995ce616f0d4&amp;spot_im_platform=desktop&amp;host_url=http%3A%2F%2Fwww.foxnews.com%2Fopinion%2F2018%2F04%2F01%2Fwhat-is-easter-and-why-do-christians-celebrate-this-holiday.html&amp;host_url_64=aHR0cDovL3d3dy5mb3huZXdzLmNvbS9vcGluaW9uLzIwMTgvMDQvMDEvd2hhdC1pcy1lYXN0ZXItYW5kLXdoeS1kby1jaHJpc3RpYW5zLWNlbGVicmF0ZS10aGlzLWhvbGlkYXkuaHRtbA%3D%3D&amp;spot_im_ph__prerender_deferred=true&amp;prerenderDeferred=true&amp;sort_by=newest&amp;spot_im_ih__livefyre_url=44cb71eb-b87a-47aa-8156-8fe92bf8054f&amp;isStarsRatingEnabled=false&amp;enableMessageShare=true&amp;enableAnonymize=true&amp;isConversationLiveBlog=false&amp;enableSeeMoreButton=true"

    driver.get(comment_url)
    # post_msg = driver.find_element_by_css_selector('.ql-editor.ql-blank')
    post_msg = driver.find_element_by_class_name("ql-editor ql-blank")
    print 'class name finded!'
    time.sleep(5)
    btn = driver.find_element_by_css_selector(
        "#root > div > div.sppre_conversation > div.sppre_rich-editor.sppre_expanded > div.sppre_rich-editor-container > div.sppre_panel > div > div.sppre_actions > button")

    for i in range(0, 20):
        message = randomword(20)
        post_msg.send_keys(message)
        btn.click()




    # message = randomword(15)
    # post_comment(driver, message)








    # open_page(driver, 'https://www.foxnews.com/community/auth/user/profile.html')
    # time.sleep(5)
    # print 'profile page loaded'
    # modify the profile name

    # for i in range(0,300):
    #     message = randomword(15)
    #     print(message)
    #     modify_account(driver, message)
    #     print 'update success time %d : %s'% (i, message)
    #     time.sleep(5)