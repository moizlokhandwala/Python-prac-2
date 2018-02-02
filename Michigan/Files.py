# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:41:11 2018

@author: Twox3
"""

"""fhand=open('mob.txt')
inf=fhand.read()
print(inf)"""
"""for cheese in fhand:
    //print(cheese)"""
    
fname = input('Please enter the file name : ')
try:
    fhand = open(fname)
    
    for line in fhand:
        line=line.rstrip()
        print(line.upper())
    
except:
      print('File cannot be opened.')
    
    

        