#!/usr/local/bin/python
# coding:utf-8
# import urllib
import pyautogui
from urllib import urlopen
from urllib import urlretrieve
import urllib
import requests
from selenium import webdriver
import BeautifulSoup as BS
import json
import sys
import os
import zipfile
import shutil
import multiprocessing
import time

def dr_login(email,password):

    driver = webdriver.Chrome()
    # print 1111
    # /html/body/div[7]/div/div/div[2]/div/login-form/form/div[2]/div/input
    driver.get('https://www.dramafever.com/login/')
    # find email, send data and submit
    # //*[@id="identifierId"]
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.typewrite(email)
    time.sleep(1)
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.typewrite(password)
    time.sleep(1)
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.press('enter')
    # EMAIL_FIELD = driver.find_element_by_id('identifierId')
    # EMAIL_FIELD.click()
    # EMAIL_FIELD.clear()
    # EMAIL_FIELD.send_keys(email)
    # EMAIL_FIELD.send_keys(Keys.ENTER)
    time.sleep(3)
    
    # print 111111

    # driver.find_element_by_class_name('CeoRYc').click()
    # time.sleep(4)
    # print 22222

    # # find password, send data and submit
    # PASSWD_FIELD = driver.find_element_by_name('password')
    # PASSWD_FIELD.click()
    # PASSWD_FIELD.clear()
    # PASSWD_FIELD.send_keys(password)
    # PASSWD_FIELD.send_keys(Keys.ENTER)
    # time.sleep(3)
    


    time.sleep(3)

    return driver

def crawl(url, driver):
 
    # driver = webdriver.Chrome()
    # driver.find_elements_by_xpath('//*[@id="dsb-problem-content-div0"]/div/table/tbody/tr[2]/td[1]/code')
    # print driver.page_source
    driver.get(url)
    time.sleep(2)
    # path = "//body/div[@class='comments']//div[@class='comment-item']"
    # //*[@id="content-text"]/text()
    # //*[@id="content-text"]/a
    # //*[@id="reviews__list-container"]/ul/li[5]/div[2]/p
    # for i in range(0,10):
    path = '//*[@id="account-tab-container"]/div[2]/div/div[1]/div/div[1]/div[2]/textarea'
    # 
    # driver.execute_script('window.scrollTo(1, 500);')
    # time.sleep(3)
    # driver.execute_script('window.scrollTo(1, 3000);')
# //*[@id="reviews__list-container"]/ul/li[1]/div[2]/p
    a = driver.find_elements_by_xpath(path)
    # comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
    # a = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
    # print driver.page_source
    # print a
    # print a
    # //*[@id="voted-option"]//*[@id="content-text"]
    for k in a:
        print k.get_attribute('data-placeholder')
    # print a.
    driver.quit()
    # //*[@id="dsb-problem-content-div1"]/div/table/tbody/tr[2]/td[1]/code
    # if i == 1:
    #     break

if __name__ == '__main__':
    email = 'sectest777sec@gmail.com'
    password = '1qazxsW@'
    url = 'https://www.dramafever.com/account/profile/#/profile'
    driver = dr_login(email,password)
    crawl(url, driver)

