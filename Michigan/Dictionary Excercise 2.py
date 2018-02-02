# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:45:06 2018

@author: Twox3
"""


FileName = input('Enter the file name : ')
counts=dict()
MaxWord=''
MaxCount=0
try:
    fhandler = open(FileName)
except:
    print('Invalid File !')
    
for line in fhandler:
    line = line.rstrip()
   
    if line.startswith('From') :
        words = line.split()
        if len(words)==7:
            date=words[5].split(':')
            
            counts[date[0]]=counts.get(date[0],0) + 1
        
keys = list(counts.keys())

keys.sort()

for key in keys:
    print(key,counts[key])



            
