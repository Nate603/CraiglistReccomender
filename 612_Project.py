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
location=''
miles=''
make=''
model=''

if results.miles:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.zip:
    miles= "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
if results.min_price:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.max_price:
    miles= "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
if results.make:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.model:
    miles= "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
if results.min_eng_disp:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.max_eng_disp:
    miles= "&search_distance=" + str(results.miles)
    baseUrl = baseUrl + miles
if results.min_year:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.max_year:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.min_odo:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.max_odo:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.condition:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.fuel:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.color:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.title:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.trans:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location
if results.location:
    location= "&postal=" + str(results.location)
    baseUrl = baseUrl + location

  
print(baseUrl)    
    
#mylist = []
#
#html = urlopen("https://nh.craigslist.org/search/mca")
#
#soup = BeautifulSoup(html, "html.parser")
#
#for x in soup.find_all("li", {"class":"result-row"})[1:]:
#    
#    for n in x.find_all("time", {"class":"result-date"}):
#        time = (n['title'])
#        
#    for a in x.find_all('a', {"class":"result-title"}, href=True):
#        href = a['href']
#    a = x.find_all("a")
#    data = time, a[1].text, "https://nh.craigslist.org"+href
#    mylist.append(data)
#    
#for i in mylist:
#    pass
#    #print(i, "\n")
#
#with open('Boston area.csv', 'a') as outcsv:   
#    writer = csv.writer(outcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#    for item in mylist:
#        writer.writerow(item)
#    
