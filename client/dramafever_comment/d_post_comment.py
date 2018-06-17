#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python bot for comment a list of urls in Dr
import pyautogui
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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

def comment_page(driver,urls,comment):

	# Check if there still urls
	if len( urls ) == 0:
		print 'Dr Comment Bot: Finished!'
		return []
	
	# Pop a URL from the array	
	url = urls.pop()
	
	# Visite the page	
	driver.get(url)
	driver.implicitly_wait(1)

	# Is video avaliable (deleted,private) ?
	if not check_exists_by_xpath(driver,'//*[@id="movie_player"]'):
		return comment_page(driver, urls, random_comment())

	# Scroll, wait for load comment box
	driver.execute_script("window.scrollTo(0, 500);")
	
	# Comments are disabled?
	if check_exists_by_xpath(driver,'//*[@id="comments-disabled-message"]/div/span'):
		return comment_page(driver, urls, random_comment())

	# Lets wait for comment box
	# print 1111111
	# WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "comment-section-renderer")))
	# print 11111111
	# Activate box for comments
	time.sleep(5)
	driver.find_element_by_id('comment-simplebox-renderer-collapsed-content').click()
	#driver.find_element_by_xpath("//div[@id='comment-section-renderer']/div/div[2]/div").click()

	# Send comment and post
	driver.implicitly_wait(5)
	driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(_convert(comment))
	driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(Keys.ENTER + Keys.ENTER)

	# Is post ready to be clicked? comment-simplebox-submit
	
	driver.find_element_by_class_name('comment-simplebox-submit').click()

	# Lets wait a bit
	r = np.random.randint(2,5)
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
		'what up'
	]
	
	r = np.random.randint(0, len(messages))

	return messages[r]
 
def check_exists_by_xpath(driver,xpath):
	
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True
if __name__ == '__main__':

	# Credentials
	email = 'sectest777sec@gmail.com'
	password = '1qazxsW@'


	# List of Urls
	#urls = [
	 # 'https://www.dr.com/watch?v=qbrvM61MUAY',
	#]


	# urls = ['https://www.dr.com/watch?v=qbrvM61MUAY']



	# You can add in a file and import from there
	
	# inp = open ("urls.txt","r")
	# for line in inp.readlines():
	# 		yeni_url = line.split()
	# 		for current_word in yeni_url:
	# 			urls.append(current_word)
  	
	# Login in dr

	driver = dr_login(email, password)
	time.sleep(3)

	driver.get('https://www.dramafever.com/drama/5140/Longing_Heart/')
	# /html/body/div[4]/div/div[2]/div[6]/lazy-load/ng-transclude/reviews/div/div[2]/form/div[3]/textarea
		# Scroll, wait for load comment box
		# /html/body/div[4]/div/div[2]/div[6]/lazy-load/ng-transclude/reviews/div/div[2]/form/div[2]/rating/ul/li[3]
	time.sleep(1)
	driver.execute_script("window.scrollTo(0, 500);")
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, 3000);")
	time.sleep(3)
	comment = "what up"
	# /html/body/div[4]/div/div[2]/div[6]/lazy-load/ng-transclude/reviews/div/div[2]/form/div[3]/textarea
	box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, u"/html/body/div[4]/div/div[2]/div[6]/lazy-load/ng-transclude/reviews/div/div[2]/form/div[2]/rating/ul/li[3]")))
	box.click()
	# pyautogui.typewrite(_convert(comment))
	box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, u"/html/body/div[4]/div/div[2]/div[6]/lazy-load/ng-transclude/reviews/div/div[2]/form/div[3]/textarea")))
	box.click()
	pyautogui.typewrite(_convert(comment))
	# time.sleep(3)
	# pyautogui.typewrite('\t')
	time.sleep(1)
	pyautogui.typewrite('\t')
	time.sleep(1)
	pyautogui.press('enter')

	# driver = webdriver.Firefox()
	# driver.get('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.dr.com%2Fsignin%3Fhl%3Den%26feature%3Dcomment%26app%3Ddesktop%26next%3D%252Fall_comments%253Fv%253DLAr6oAKieHk%26action_handle_signin%3Dtrue&uilel=3&service=dr&passive=true&hl=en')

	# # log in
	# driver.find_element_by_id('Email').send_keys('username')
	# driver.find_element_by_id('Passwd').send_keys('password')
	# driver.find_element_by_id('signIn').click()

	# post a comment



	# time.sleep(3)

	# driver.get('https://www.dr.com/watch?v=wmctXndgmJk')
	# 	# Scroll, wait for load comment box
	# time.sleep(1)
	# driver.execute_script("window.scrollTo(0, 500);")
	# time.sleep(5)
	# comment = "what up"




	# //*[@id="textarea"]
# //*[@id="textarea"]
# //*[@id="mirror"]
	# com = driver.find_element(by=By.CLASS_NAME, value='paper-input-input style-scope ytd-commentbox')
	# com.click()
	# //*[@id="textarea"]/div[2]
	# com.clear()
	# com.send_keys(comment)
	# com.send_keys(Keys.ENTER)
	# time.sleep(3)



	# box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "simplebox-placeholder")))
	# box.click()
	# pyautogui.typewrite(_convert(comment))
	# time.sleep(3)
	# pyautogui.typewrite('\t')
	# time.sleep(1)
	# pyautogui.typewrite('\t')
	# time.sleep(1)
	# pyautogui.press('enter')



	# driver.implicitly_wait(5)
	# driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(_convert(comment))
	# driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(Keys.ENTER + Keys.ENTER)

	# # Is post ready to be clicked? comment-simplebox-submit
	
	# driver.find_element_by_class_name('comment-simplebox-submit').click()
	# driver.find_element_by_class_name('style-scope ytd-button-renderer style-primary').click()

	# //*[@id="button"]
	# driver.find_element_by_name('Comment').click()
	# //*[@id="text"]
	# box.clear()

	# box.send_keys(_convert(comment))
	# driver.implicitly_wait(5)
	# //*[@id="mirror"]
	# driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(_convert(comment))
	# driver.find_element_by_xpath('//*[@id="comment-simplebox"]/div[1]').send_keys(Keys.ENTER + Keys.ENTER)
	# frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="+1"]')))
	# driver.switch_to.frame(frame)

	# driver.find_element_by_xpath('//div[@onclick]').click()

	# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jsname="msEQQc"]/following-sibling::div//div[@g_editable="true"]')))
	# driver.execute_script("arguments[0].innerHTML='%s';" % comment, element)

	# Random comment
	# comment_page(driver,urls,random_comment())
