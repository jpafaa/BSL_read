# -*- coding: utf-8 -*-
"""
Patrick Fairclough
First attempt at BSL file reading
December 2022
"""
import struct as st
import numpy as np
import matplotlib.pyplot as plt

ax=[]
cplot=[]
datal=[]

file="C:\\Users\\ch1paf\\Downloads\\tmp\\saxs\\D02001.129"
with open(file, mode="rb" ) as file:    
    for i in range (0,(64*512*512)) : #0 as it stops one before final number
        data=file.read(4)
        datal +=[st.unpack('>f', data)] #convert to big endian

maxZ=max(datal) 
minZ=min(datal)
print (minZ, maxZ)
frames=np.reshape(datal,(64,512,512))

k=0
# Plot the contour plots in 8x8 array
fig, ax = plt.subplots(8, 8, sharex='col', sharey='row')
for i in range(0,8,1):
    for j in range(0,8,1):   
        cplot=ax[i,j].contourf(frames[k],cmap='plasma')
        k=k+1
         
plt.show()
