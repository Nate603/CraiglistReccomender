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
    location= "&search_distance=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.postal:
    miles= "&postal=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.min_price:
    location= "&min_price=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.max_price:
    miles= "&max_price=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.make:
    location= "&auto_make_model=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.model:
    miles= "&postal=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.min_eng_disp:
    location= "&min_engine_displacement_cc=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.max_eng_disp:
    miles= "&max_engine_displacement_cc=" + str(results.miles)
    baseUrl = baseUrl + miles
    
if results.min_year:
    location= "&min_auto_year=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.max_year:
    location= "&max_auto_year=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.min_odo:
    location= "&min_auto_miles=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.max_odo:
    location= "&max_auto_miles=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.condition:
    location= "&condition=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.fuel:
    location= "&auto_fuel_type=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.color:
    location= "&auto_paint=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.title:
    location= "&auto_title_status=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.trans:
    location= "&auto_transmission=" + str(results.location)
    baseUrl = baseUrl + location
    
if results.location:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location

  
print(baseUrl)        
  

    
