#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:37:04 2018
"""


#import csv
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser(description='Takes in filters for craigslist search (exclusively for motorcycles and cars)')
parser.add_argument("-mi", "--miles", help="Miles from zip (default: None)", action="store", default=None)
parser.add_argument("-z", "--zip", help="Zipcode (default: None)", action="store", default=None)
parser.add_argument("-minp", "--min_price", help="Minimum price of the item (default: None)", action="store", default=None)
parser.add_argument("-maxp", "--max_price", help="Maximum price of the item (default: None)", action="store", default=None)
parser.add_argument("-ma", "--make", help="Make/Model of the item (default: None)", action="store", default=None)
parser.add_argument("-mo", "--model", help="Make/Model of the item (default: None)", action="store", default=None)
parser.add_argument("-minen", "--min_eng_disp", help="Minimum engine displacement (default: None)", action="store", default=None)
parser.add_argument("-maxen", "--max_eng_disp", help="Maximum engine displacement (default: None)", action="store", default=None)
parser.add_argument("-miny", "--min_year", help="Minimum model year (default: None)", action="store", default=None)
parser.add_argument("-maxy", "--max_year", help="Maximum model year (default: None)", action="store", default=None)
parser.add_argument("-mino", "--min_odo", help="Minimum odometer (default: None)", action="store", default=None)
parser.add_argument("-maxo", "--max_odo", help="Maximum odometer (default: None)", action="store", default=None)
parser.add_argument("-con", "--condition", help="Condition of the item (Options: new, like new, excellent, good, fair, salvage) (default: None)", action="store", default=None)
parser.add_argument("-f", "--fuel", help="Type of fuel for item (Options: gas, diesel, hybrid, electric, other) (default: None)", action="store", default=None)
parser.add_argument("-col", "--color", help="Color of the item (Options: black, blue, brown, green, grey, orange, purple, red, silver, white, yellow, custom, all) (default: None)", action="store", default=None)
parser.add_argument("-ti", "--title", help="Title status (Options: clean, salvage, rebuilt, parts_only, lien, missing) (default: None)", action="store", default=None)
parser.add_argument("-tr", "--trans", help="Transmission (Options: manual, automatic, other) (default: None)", action="store", default=None)
parser.add_argument("-l", "--location", help="Location of the item (default: None)", action="store", default=None)
results = parser.parse_args()


baseUrl = 'https://boston.craigslist.org/search/sss?sort=rel'

#print("results: " + str(results))
#declare variables
miles='';postal='';min_price='';max_price='';make='';model=''
min_eng_disp='';max_eng_disp='';min_year='';max_year=''
min_odo='';max_odo='';condition='';fuel='';color=''
title='';trans='';location='';query='';


if results.make:
    make = str(results.make)
    
if results.model:
    model = str(results.model)
    
#query with make and model
if results.make and results.model:
    baseUrl = baseUrl + '&query=' + make + "+" + model
if results.make and results.model == None:
    #print('1')
    baseUrl = baseUrl + '&query=' + make
if results.make == None and results.model:
    #print('2')
    baseUrl = baseUrl + '&query=' + model

if results.miles:
    miles = "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.zip:
    postal = "&postal=" + str(results.zip)
    baseUrl = baseUrl + postal
    
if results.min_price:
    min_price = "&min_price=" + str(results.min_price)
    baseUrl = baseUrl + min_price
    
if results.max_price:
    max_price = "&max_price=" + str(results.max_price)
    baseUrl = baseUrl + max_price

if results.min_eng_disp:
    min_eng_disp = "&min_engine_displacement_cc=" + str(results.min_eng_disp)
    baseUrl = baseUrl + min_eng_disp
    
if results.max_eng_disp:
    max_eng_disp = "&max_engine_displacement_cc=" + str(results.max_eng_disp)
    baseUrl = baseUrl + max_eng_disp
    
if results.min_year:
    min_year = "&min_auto_year=" + str(results.min_year)
    baseUrl = baseUrl + min_year
    
if results.max_year:
    max_year = "&max_auto_year=" + str(results.max_year)
    baseUrl = baseUrl + max_year
    
if results.min_odo:
    min_odo = "&min_auto_miles=" + str(results.min_odo)
    baseUrl = baseUrl + min_odo
    
if results.max_odo:
    max_odo = "&max_auto_miles=" + str(results.max_odo)
    baseUrl = baseUrl + max_odo
    
if results.condition:
    condition = "&condition=" + str(results.condition)
    baseUrl = baseUrl + condition
    
if results.fuel:
    fuel = "&auto_fuel_type=" + str(results.fuel)
    baseUrl = baseUrl + fuel
    
if results.color:
    color = "&auto_paint=" + str(results.color)
    baseUrl = baseUrl + color
    
if results.title:
    title = "&auto_title_status=" + str(results.title)
    baseUrl = baseUrl + title
    
if results.trans:
    trans = "&auto_transmission=" + str(results.trans)
    baseUrl = baseUrl + trans
    
if results.location:
    location = "&postal=" + str(results.location)
    baseUrl = baseUrl + location


print(baseUrl)        
from urllib.request import urlopen
from bs4 import BeautifulSoup
rec = open("initialRecommendations.csv", 'w')
response = urlopen(baseUrl)
soup = BeautifulSoup(response, "lxml")
for child in soup.find_all("li", {"class" : "result-row"}):
   stri = ""
   title = ""
   link = ""
   date = ""
   title = child.p.a.get_text()
   link = child.p.a.attrs['href']
   date = child.p.time.attrs['datetime']
   stri = date + "," + title + "," + link + "\n"
   try:
       rec.write(stri)
   except:
       stri = date + "," + "Bad encoding!" + "," + link + "\n"
rec.close() 

    
