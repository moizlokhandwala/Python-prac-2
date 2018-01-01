# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 11:04:28 2018

@author: Twox3
"""

"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.
def powerball():
    number1=random.randint(1,60)
    number2=random.randint(1,60)
    number3=random.randint(1,60)
    number4=random.randint(1,60)
    number5=random.randint(1,60)
    powerballnumber = random.randint(1,36)
    print ("Today's numbers are "+ str(number1)+", "+str(number2)+", "+str(number3)+", "+str(number4)+", and "+str(number5)+". The Powerball number is "+str(powerballnumber)+".")


    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
