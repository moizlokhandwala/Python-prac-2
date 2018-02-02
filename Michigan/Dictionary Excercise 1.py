# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:25:35 2018

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
    if line.startswith('From:') :
        words = line.split()
        counts[words[1]]=counts.get(words[1],0) + 1
    
for key in counts:
    if MaxCount < counts[key]:
            
        MaxWord=key
        MaxCount=counts[key]
            
print(MaxWord,MaxCount)  
