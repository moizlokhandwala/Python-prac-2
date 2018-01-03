# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:22:49 2018

@author: Twox3
"""

"""
Template - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
def smaller_root(coeff_a, coeff_b, coeff_c):
    discriminant = coeff_b**2 - 4*coeff_a*coeff_c
    if(discriminant>0):
        x1 = (-coeff_b + (coeff_b**2 - 4*coeff_a*coeff_c)**0.5)/(2*coeff_a)
        x2 = (-coeff_b - (coeff_b**2 - 4*coeff_a*coeff_c)**0.5)/(2*coeff_a)
        
        if(x1<x2):
             return x1
        else:
             return x2
    elif(discriminant==0):
        x = (-coeff_b + (coeff_b**2 - 4*coeff_a*coeff_c)**0.5)/(2*coeff_a)
        return x
    else:
        return "Error: No real solutions"



###################################################
# Tests
# Student should not change this code.

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
