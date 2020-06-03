#!/bin/python3

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox import firefox_profile

username = input('enter username: ')
password = input('enter password: ')

url = 'https://www.facebook.com/'
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", "en-US")
drive = webdriver.Firefox(firefox_profile=fp)

drive.get(url)
time.sleep(3)
drive.implicitly_wait(8)
drive.find_element_by_id('email').send_keys(username)
time.sleep(2)
drive.find_element_by_id('pass').send_keys(password)
time.sleep(2)
drive.find_element_by_id('loginbutton').click()
