# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:02:09 2018

@author: Twox3
"""

fname = input('Please enter the file name : ')
nameList = list()
try:
    fhand = open(fname)
    
    for line in fhand:
       lineParts = line.split()
       for parts in lineParts:
           if parts not in nameList:
               nameList.append(parts)
               
    nameList.sort()
    print(nameList)
               
       
    
except:
      print('File cannot be opened.')