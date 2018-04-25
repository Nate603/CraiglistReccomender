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
parser.add_argument("-mi", "--miles", help="Miles from zip (default: None)", action="store", dest="miles", default=None)
parser.add_argument("-z", "--zip", help="Zipcode (default: None)", action="store", dest="zip", default=None)
parser.add_argument("-minp", "--min_price", help="Minimum price of the item (default: None)", action="store", dest="minp", default=None)
parser.add_argument("-maxp", "--max_price", help="Maximum price of the item (default: None)", action="store", dest="maxp", default=None)
parser.add_argument("-ma", "--make", help="Make/Model of the item (default: None)", action="store", dest="make", default=None)
parser.add_argument("-minen", "--min_eng_disp", help="Minimum engine displacement (default: None)", action="store", dest="minen", default=None)
parser.add_argument("-maxen", "--max_eng_disp", help="Maximum engine displacement (default: None)", action="store", dest="maxen", default=None)
parser.add_argument("-miny", "--min_year", help="Minimum model year (default: None)", action="store", dest="miny", default=None)
parser.add_argument("-maxy", "--max_year", help="Maximum model year (default: None)", action="store", dest="maxy", default=None)
parser.add_argument("-mino", "--min_odo", help="Minimum odometer (default: None)", action="store", dest="mino", default=None)
parser.add_argument("-maxo", "--max_odo", help="Maximum odometer (default: None)", action="store", dest="maxo", default=None)
parser.add_argument("-con", "--condition", help="Condition of the item (Options: new, like new, excellent, good, fair, salvage) (default: None)", action="store", dest="condition", default=None)
parser.add_argument("-f", "--fuel", help="Type of fuel for item (Options: gas, diesel, hybrid, electric, other) (default: None)", action="store", dest="fuel", default=None)
parser.add_argument("-col", "--color", help="Color of the item (Options: black, blue, brown, green, grey, orange, purple, red, silver, white, yellow, custom, all) (default: None)", action="store", dest="color", default=None)
parser.add_argument("-ti", "--title", help="Title status (Options: clean, salvage, rebuilt, parts_only, lien, missing) (default: None)", action="store", dest="title", default=None)
parser.add_argument("-tr", "--trans", help="Transmission (Options: manual, automatic, other) (default: None)", action="store", dest="trans", default=None)
parser.add_argument("-l", "--location", help="Location of the item (default: None)", action="store", dest="location", default=None)
results = parser.parse_args()

baseUrl = 'https://boston.craigslist.org/search/sss?sort=rel'

#print("results: " + str(results))

baseUrl = 'https://boston.craigslist.org/search/sss?sort=rel'

#print("results: " + str(results))
miles=''
postal=''
min_price=''
max_price=''
make=''
model=''
min_eng_disp=''
max_eng_disp=''
min_year=''
max_year=''
min_odo=''
max_odo=''
condition=''
fuel=''
color=''
title=''
trans=''
location=''

if results.miles:
    location= "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + location
    
if results.postal:
    miles= "&postal=" + str(results.postal)
    baseUrl = baseUrl + miles
    
if results.min_price:
    location= "&min_price=" + str(results.min_price)
    baseUrl = baseUrl + location
    
if results.max_price:
    miles= "&max_price=" + str(results.max_miles)
    baseUrl = baseUrl + miles
    
if results.make:
    location= "&auto_make_model=" + str(results.make)
    baseUrl = baseUrl + location
    
if results.model:
    miles= "&postal=" + str(results.model)
    baseUrl = baseUrl + miles
    
if results.min_eng_disp:
    location= "&min_engine_displacement_cc=" + str(results.min_eng_disp)
    baseUrl = baseUrl + location
    
if results.max_eng_disp:
    miles= "&max_engine_displacement_cc=" + str(results.max_eng_disp)
    baseUrl = baseUrl + miles
    
if results.min_year:
    location= "&min_auto_year=" + str(results.min_year)
    baseUrl = baseUrl + location
    
if results.max_year:
    location= "&max_auto_year=" + str(results.max_year)
    baseUrl = baseUrl + location
    
if results.min_odo:
    location= "&min_auto_miles=" + str(results.min_odo)
    baseUrl = baseUrl + location
    
if results.max_odo:
    location= "&max_auto_miles=" + str(results.max_odo)
    baseUrl = baseUrl + location
    
if results.condition:
    location= "&condition=" + str(results.condition)
    baseUrl = baseUrl + location
    
if results.fuel:
    location= "&auto_fuel_type=" + str(results.fuel)
    baseUrl = baseUrl + location
    
if results.color:
    location= "&auto_paint=" + str(results.color)
    baseUrl = baseUrl + location
    
if results.title:
    location= "&auto_title_status=" + str(results.title)
    baseUrl = baseUrl + location
    
if results.trans:
    location= "&auto_transmission=" + str(results.trans)
    baseUrl = baseUrl + location
    
if results.location:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location

  
print(baseUrl)        
  

    
