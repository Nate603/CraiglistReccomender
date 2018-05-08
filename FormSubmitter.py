#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:57:15 2018

@author: Nate
"""

#import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from urllib.request import Request, urlopen
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


url = 'https://www.cargurus.com/Cars/instantMarketValue.action'
driver = webdriver.Chrome('/Users/zacharygirard/Documents/GitHub/CraigslistRecommender/chromedriver')
driver.get(url)

time.sleep(1)

selectMake = Select(driver.find_element_by_id('carPicker_makerSelect'))
selectModel = Select(driver.find_element_by_id('carPicker_modelSelect'))
selectYear = Select(driver.find_element_by_id('carPicker_year1Select'))
selectTrim = Select(driver.find_element_by_id('carPicker_trimSelect'))
selectZip = driver.find_element_by_id('listingFormZip')
selectMileage = driver.find_element_by_id('mileage')

def getprice(make,model,year,zipcode,miles):
    #select by visible text
    time.sleep(.1)
    selectMake.select_by_visible_text(make)
    selectModel.select_by_visible_text(model)
    selectYear.select_by_visible_text(year)
    time.sleep(.1)
    selectTrim.select_by_index(1)
    selectZip.send_keys(zipcode)
    time.sleep(.1)
    selectMileage.send_keys(miles)
    selectMileage.send_keys(Keys.ENTER)
    time.sleep(.5)
    updatedurl = driver.page_source
    soup = BeautifulSoup(updatedurl, 'html.parser')
    price = soup.find("div", {"id" : "sellMyCarPrice"})
    time.sleep(.1)
    selectZip.clear()
    selectMileage.clear()
    return(price.get_text()[2:])
    
   

##select by visible text
#selectMake.select_by_visible_text('Nissan')
#selectModel.select_by_visible_text('Altima')
#selectYear.select_by_visible_text('2008')
#time.sleep(.1)
#selectTrim.select_by_index(1)
#selectZip.send_keys('03842')
#selectMileage.send_keys('50000')
#selectMileage.send_keys(Keys.ENTER)
#time.sleep(.1)
#updatedurl = driver.page_source
#soup = BeautifulSoup(updatedurl, 'html.parser')
#price = soup.find("div", {"id" : "sellMyCarPrice"})
#print(price.get_text()[2:])
#
#selectZip.clear()
#selectMileage.clear()
#
##select by visible text
#selectMake.select_by_visible_text('Audi')
#selectModel.select_by_visible_text('S5')
#selectYear.select_by_visible_text('2016')
#time.sleep(.1)
#selectTrim.select_by_index(1)
#selectZip.send_keys('03842')
#selectMileage.send_keys('10000')
#selectMileage.send_keys(Keys.ENTER)
#time.sleep(.1)
#updatedurl = driver.page_source
#soup = BeautifulSoup(updatedurl, 'html.parser')
#price = soup.find("div", {"id" : "sellMyCarPrice"})
#print(price.get_text()[2:])

#print(getprice('Nissan','Maxima','2005','03842','50000'))
#print(getprice('Bmw','I3','2014','03842','50000'))

