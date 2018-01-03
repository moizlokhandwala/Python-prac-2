# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:34:33 2018

@author: Twox3
"""

"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula
# Student should enter function on the next lines.
def name_and_age(name,age):
    if(age>0):
        return name+" is " + str(age) +" years old."
    else :
        return "Error: Invalid age"



###################################################
# Tests
# Student should not change this code.

name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", -46
print(name_and_age(name, age))



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 56 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age
