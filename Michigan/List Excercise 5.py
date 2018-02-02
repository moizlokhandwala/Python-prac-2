# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:06:29 2018

@author: Twox3
"""

fname = input('Please enter the file name : ')
fromList = list()
try:
    fhand = open(fname)
    
    for line in fhand:
       line=line.rstrip()
       if line.startswith("From:"):
           lineParts = line.split()
           fromList.append(lineParts[1])
    
    print(fromList)
    print('Total Senders : ',len(fromList))           
       
    
except:
      print('File cannot be opened.')