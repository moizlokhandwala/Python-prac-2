# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:12:20 2018

@author: Twox3
"""

"""
Template - Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(year):
    if(year%4 is not 0):
        return False
    elif(year%100 is not 0):
        return True
    elif (year%400 is not 0):
        return False
    else :
        return True



###################################################
# Tests
# Student should not change this code.

year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
