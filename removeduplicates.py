#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:47:53 2018

@author: Nate
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


path = 'initialRecommendations.xls'
xls = pd.ExcelFile(path)
df = pd.read_excel(xls)
#df.duplicated(['price'], keep=False)
dfafter = df.drop_duplicates(subset=['price', 'Make/Model'], keep='first')
print(dfafter)

writer = ExcelWriter('NoDuplicates.xlsx')
dfafter.to_excel(writer)
writer.save()