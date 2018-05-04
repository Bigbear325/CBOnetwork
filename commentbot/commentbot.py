#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python bot for comment a list of urls in YouTube

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def youtube_login(email, password):
    # Browser
    binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=tr&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26feature%3Dsign_in_button%26app%3Ddesktop%26action_handle_signin%3Dtrue%26next%3D%252F&uilel=3&passive=true&service=youtube#identifier')
    # find email, send data and submit
    EMAIL_FIELD = driver.find_element_by_id('identifierId')
    EMAIL_FIELD.click()
    EMAIL_FIELD.clear()
    EMAIL_FIELD.send_keys(email)
    EMAIL_FIELD.send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element_by_class_name('CeoRYc').click()
    time.sleep(4)

    # find password, send data and submit
    PASSWD_FIELD = driver.find_element_by_name('password')
    PASSWD_FIELD.click()
    PASSWD_FIELD.clear()
    PASSWD_FIELD.send_keys(password)
    PASSWD_FIELD.send_keys(Keys.ENTER)
    time.sleep(3)

    time.sleep(3)

    return driver


def comment_page(driver, urls, comment):
    # Check if there still urls
    if len(urls) == 0:
        print 'Youtube Comment Bot: Finished!'
        return []

    # Pop a URL from the array
    url = urls.pop()

    # Visite the page
    driver.get(url)
    driver.implicitly_wait(1)

    # Is video avaliable (deleted,private) ?
    if not check_exists_by_xpath(driver, '//*[@id="movie_player"]'):
        return comment_page(driver, urls, random_comment())

    # Scroll, wait for load comment box
    driver.execute_script("window.scrollTo(0, 500);")

    # Comments are disabled?
    if check_exists_by_xpath(driver, '//*[@id="comments-disabled-message"]/div/span'):
        return comment_page(driver, urls, random_comment())

    # Lets wait for comment box
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "comment-section-renderer")))

    # Activate box for comments
    driver.find_element_by_class_name('comment-simplebox-renderer-collapsed-content').click()
    # driver.find_element_by_xpath("//div[@id='comment-section-renderer']/div/div[2]/div").click()

    # Send comment and post
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(_convert(comment))
    driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(Keys.ENTER + Keys.ENTER)

    # Is post ready to be clicked? comment-simplebox-submit

    driver.find_element_by_class_name('comment-simplebox-submit').click()

    # Lets wait a bit
    r = np.random.randint(2, 5)
    time.sleep(r)

    # Recursive
    return comment_page(driver, urls, random_comment())


def _convert(param):
    if isinstance(param, str):
        return param.decode('utf-8')
    else:
        return param


def random_comment():
    messages = [
        'Müzik Caddesi Uyguluması müzik indirme ve dinleme programı telefonuza şarkı keyfi yaşatır. Google Play\'den indirebilir veya https://play.google.com/store/apps/details?id=com.muzikcaddesi.muzikcaddesi'
    ]

    r = np.random.randint(0, len(messages))

    return messages[r]


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True


if __name__ == '__main__':

    # Credentials
    email = ''
    password = ''

    # List of Urls
    # urls = [
    # 'https://www.youtube.com/watch?v=qbrvM61MUAY',
    # ]
    urls = ['']
    # You can add in a file and import from there

    inp = open("urls.txt", "r")
    for line in inp.readlines():
        yeni_url = line.split()
        for current_word in yeni_url:
            urls.append(current_word)

    # Login in youtube

    driver = youtube_login(email, password)

    # Random comment
    comment_page(driver, urls, random_comment())