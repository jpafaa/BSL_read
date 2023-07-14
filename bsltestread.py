# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 21:37:23 2022

@author: ch1paf
"""

filein = input('enter header filname, eg D02000.129, case sensitive..: ')
dirin="C:\\Users\\ch1paf\\Downloads\\tmp\\saxs\\"
file=dirin+filein
print(file)
f = open(file, 'r') # 'r' = read
lines = f.readlines()
f.close()
for i in range(6):
    print (i, lines[i])
infile=lines[3]
    

