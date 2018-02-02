# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:19:34 2018

@author: Twox3
"""

import string

line='test!!!!..,'

line = line.translate(line.maketrans('', '', string.punctuation))
print(line)