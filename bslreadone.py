# -*- coding: utf-8 -*-
"""
Patrick Fairclough
First attempt at BSL file reading
December 2022
"""
import struct as st
import matplotlib.pyplot as plt
import numpy as np



datal=[]

file="C:\\Users\\ch1paf\\Downloads\\tmp\\saxs\\S14001.131"
with open(file, mode="rb" ) as file:    
    for i in range (0,(512*512)) : #0 as it stops one before final number
        data=file.read(4)
        datal +=[st.unpack('>f', data)] #convert to big endian

maxZ=max(datal) 
minZ=min(datal)
print (minZ, maxZ)
lndatal=np.log(datal)
frames=np.reshape(datal,(512,512))
framln=np.reshape(lndatal,(512,512))
fig,ax=plt.subplots(1,1)
cp = ax.contourf(frames)         
plt.show()
