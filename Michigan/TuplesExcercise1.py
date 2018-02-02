# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:40:00 2018

@author: Twox3
"""

FileName = input('Enter the file name : ')
counts=dict()
countList=list()
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
    
for key,value in counts.items():
    countList.append((value,key))
    
countList.sort(reverse=True)
    
for key,value in countList[:1]:
    print(value,key)
    
print(countList[0])
            
