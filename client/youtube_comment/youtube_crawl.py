#!/usr/local/bin/python
# coding:utf-8
# import urllib
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


def crawl(url):
 
    driver = webdriver.Chrome()
    # driver.find_elements_by_xpath('//*[@id="dsb-problem-content-div0"]/div/table/tbody/tr[2]/td[1]/code')
    # print driver.page_source
    driver.get(url)
    time.sleep(2)
    # path = "//body/div[@class='comments']//div[@class='comment-item']"
    # //*[@id="content-text"]/text()
    # //*[@id="content-text"]/a
    path = '//*[@id="content-text"]'
    # 
    driver.execute_script('window.scrollTo(1, 500);')
    time.sleep(5)
    driver.execute_script('window.scrollTo(1, 3000);')

    a = driver.find_elements_by_xpath(path)
    # comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
    # a = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
    # print driver.page_source
    # print a
    # //*[@id="voted-option"]//*[@id="content-text"]
    for k in a:
    	print k.text
    driver.quit()
    # //*[@id="dsb-problem-content-div1"]/div/table/tbody/tr[2]/td[1]/code
    # if i == 1:
    #     break

if __name__ == '__main__':
	url = 'https://www.youtube.com/watch?v=wmctXndgmJk'
	crawl(url)

