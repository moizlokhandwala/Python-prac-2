# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:11:15 2018

@author: Twox3
"""
numbers=list()
while(True):
    userinput=input(':')
    if userinput == "done":
        break
    numbers.append(userinput)

print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)