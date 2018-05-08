#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:47:53 2018

@author: Nate
"""

import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
#import numpy as np
import FormSubmitter as Form
#import time

def removedupe(resultsZipCode):
    path = 'initialRecommendations.csv'
    #xls = pd.ExcelFile(path)
    
    df = pd.read_csv(path,encoding='latin-1')
    
    #df.duplicated(['price'], keep=False)
    dfafter = df.drop_duplicates(subset=['price','year','Make/Model','odometer'], keep='first')
    #dfafter = dfafter.drop(columns=")
    columnsTitles=['date','title','link','price','year','Make/Model','odometer','Color','Fuel Type','VIN','Title Status','Car Type','Transmission','Size','Drive','Cyclinders','Condition']
    dfafter=dfafter.reindex(columns=columnsTitles)
    #print(dfafter)
    
    Makes = []
    Models = []
    
    for index, row in dfafter.iterrows():
        Make = row['Make/Model'].split(' ', 1)[0]
        Model = row['Make/Model'].split(' ', 1)[1]
        Make = Make.title()
        Model = Model.title()
        #special cases
        if Make == 'Bmw':
            Make = 'BMW'
        if Make == 'Gmc':
            Make = 'GMC'
        if Make == 'Infiniti':
            Make = 'INFINITI'
       
        Makes.append(Make)
        Models.append(Model)
        #print(Make,Model)
     
    #print(Makes)
    #print(Models)
    
    dfafter = dfafter.drop('Make/Model',1)
    dfafter['Make']= Makes
    dfafter['Model']= Models
    
    columnsTitles=['date','title','link','price','year','Make','Model','odometer','Color','Fuel Type','VIN','Title Status','Car Type','Transmission','Size','Drive','Cyclinders','Condition']
    dfafter=dfafter.reindex(columns=columnsTitles)
    #print(dfafter)
     
    reccommendedprices = []
    #for each row fill out form and get price for comparison
    for index, row in dfafter.iterrows():
        make = str(row['Make'])
        #model = str(row['Model'])
        model = str(row['Model'].split(' ', 1)[0])
        miles = str(row['odometer'])
        miles = miles.split('.', 1)[0]
        
        #print(miles)
        if miles == "nan":
            miles = ""
        
        
        #price = row['price'].strip('$')
        year = str(row['year'])
        zipcode = resultsZipCode
        #zipcode = row['zipcode]
        #print(make,model,year,zipcode,miles)
        try:
            reccommendedprice = Form.getprice(make,model,year,zipcode,miles)  
            #reccommendedprice = Form.getprice('Nissan','Maxima','2005','03842','50000') 
            #print(reccommendedprice)
        except Exception as e:
            print("Error: " , e )
            reccommendedprice = "Bad Data"
        if reccommendedprice == "":
            reccommendedprice = "Not Enough Pricing Data"
        
        reccommendedprices.append(reccommendedprice.strip())
        #print(reccommendedprice)
            
    #print(reccommendedprices)
    suggestions = []
    priceDiff = []
        
    dfafter['ReccommendedPrice']= reccommendedprices
    for index, row in dfafter.iterrows():
        oldPrice = row["price"]
        newPrice = row["ReccommendedPrice"]
        oldPrice = oldPrice.replace("$" , "")
        oldPrice = oldPrice.replace("," , "")
        newPrice = newPrice.replace("," , "")
        if newPrice == "Not Enough Pricing Data" or newPrice == "Bad Data":
            suggestions.append("Bad Data")
            priceDiff.append("Bad Data")
            exit
        else:
            if int(oldPrice) < int(newPrice):
                diff = int(oldPrice) - int(newPrice)
                priceDiff.append(diff)
                suggestions.append("Good")
            else:
                diff = int(oldPrice) - int(newPrice)
                priceDiff.append(diff)
                suggestions.append("Bad")
        
    dfafter['Recommendation']= suggestions
    dfafter['PriceDifference(Reccomended Price - Craigslist Price)']= priceDiff
    dfafter.to_csv('NoDuplicates.csv',index=False)

#writer = ExcelWriter('NoDuplicates.xlsx')
#dfafter.to_excel(writer)
#writer.save()

