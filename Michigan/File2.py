# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:57:40 2018

@author: Twox3
"""

fname = input('Please enter the file name : ')
searchText = input('Please Enter Search Text : ')
try:
    fhand = open(fname)
    totalSpam=0.0
    countSpam=0
    for line in fhand:
        line=line.rstrip()
        if (line.startswith(searchText)):
            startPos = line.find(searchText)+len(searchText)
            endPos = len(line)
            countSpam=countSpam+1
            totalSpam = totalSpam + float(line[startPos:endPos])
            
    print(totalSpam/countSpam)
      
except:
      print('File cannot be opened.')