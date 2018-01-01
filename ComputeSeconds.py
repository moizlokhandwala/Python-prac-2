# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 09:42:18 2018

@author: Twox3
"""

"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.

def ComputeSeconds(hours,minutes,seconds):
    totalSeconds = (hours*60*60)+(minutes*60)+seconds
    return totalSeconds

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.
totalSeconds = ComputeSeconds(7,21,37)
print (totalSeconds)
#26497