# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 09:56:12 2018

@author: Twox3
"""

"""
Template - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.
# 2w+2h

def rectangle_perimeter(width,height):
    perimeter = 2*width + 2*height
    return perimeter



###################################################
# Tests
# Student should not change this code.


width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.
