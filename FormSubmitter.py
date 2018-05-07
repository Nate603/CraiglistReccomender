# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:12:43 2018
@program: FormSubmitter.py
@author: aleew
"""

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://www.cargurus.com/Cars/instantMarketValue.action'
driver = webdriver.Chrome('/Users/Nate/anaconda3/selenium/webdriver/chromedriver')
driver.get(url)

selectMake = Select(driver.find_element_by_id('carPicker_makerSelect'))
selectModel = Select(driver.find_element_by_id('carPicker_modelSelect'))
selectYear = Select(driver.find_element_by_id('carPicker_year1Select'))
selectTrim = Select(driver.find_element_by_id('carPicker_trimSelect'))
selectZip = driver.find_element_by_id('listingFormZip')
selectMileage = driver.find_element_by_id('mileage')

# select by visible text
selectMake.select_by_visible_text('Nissan')
selectModel.select_by_visible_text('Maxima')
selectYear.select_by_visible_text('2005')
selectTrim.select_by_index(1)
selectZip.send_keys('03842')
selectMileage.send_keys('50000')

updatedurl = driver.page_source

soup = BeautifulSoup(updatedurl, 'html.parser')