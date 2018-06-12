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
    driver.execute_script('window.scrollTo(1, 3000);')
    time.sleep(5)
    driver.execute_script('window.scrollTo(1, 5000);')
    for i in range(2,10):
        path = '/html/body/div[1]/div[5]/div[1]/div[3]/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[4]/ul/li[' + str(i) + ']/div[2]/div[2]/p/span'
    # 
    #           /html/body/div[1]/div[5]/div[1]/div[3]/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[4]/ul/li[2]/div[2]/div[2]/p/span



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
    url = 'https://www.viki.com/tv/35692c-a-love-so-beautiful?cb=17780a1ddb2a35755aef219a842d24e8&content_lang=en&email_verified=false&fresh_login=registration&last_cta=sign_up_navbar_dropdown&new_registration=true&site_lang=en'
    crawl(url)

