# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:10:40 2023

@author: ruppg
"""

search_year=["2023"]
search_month=['04']

search_json=[]
search_unknowndate=[]
for file_i in json_files:
    file_split=file_i.split('/')
    
    
    
    if len(file_split[-1].split('.json')[0]) == 2:
        search_unknowndate.append(file_i)
        continue
    year=file_split[2]
    month=file_split[3]
    day=file_split[4]
    
    
    
    if (month in search_month) and (year in search_year):
       # print('in Suchfeld')
        search_json.append(file_i)