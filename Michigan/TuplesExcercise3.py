# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:16:22 2018

@author: Twox3
"""
import string

fileName = input('Enter file name :')

fhandler = open(fileName)
words = list()
wordCount = dict()
wordCountList=list()

for line in fhandler:
    line=line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        word=word.lower()
        wordCount[word]=wordCount.get(word,0) + 1

for key,val in wordCount.items():
    wordCountList.append((val,key))

wordCountList.sort(reverse=True)    

for key,val in wordCountList:
    print(val,key)

