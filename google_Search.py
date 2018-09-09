#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:13:01 2018

@author: rohit
"""

from selenium import webdriver
search = input('Please enter the item to search:.\n')
driver = webdriver.Chrome()
url = 'http://www.google.com'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(search)
driver.find_element_by_xpath("//div[@class='jsb']//input[@value='Google Search']").click()