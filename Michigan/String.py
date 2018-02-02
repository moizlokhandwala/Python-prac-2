# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:41:54 2018

@author: Twox3
"""



strs='X-DSPAM-Confidence:0.8475'
cPos = strs.find(':')
fValue=float(strs[cPos+1:len(strs)])
print(fValue)

a1=23
a2='Hello'
a3='23'
a4=int(a3) +5
a5=8.5
print (a5)
