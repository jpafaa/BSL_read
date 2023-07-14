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
cmg=['viridis', 'plasma', 'inferno', 'magma', 'cividis',\
     'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',\
     'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',\
    'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper','PiYG',\
    'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',\
     'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',\
    'twilight', 'twilight_shifted', 'hsv','Pastel1', \
    'Pastel2', 'Paired', 'Accent', 'Dark2','Set1',\
    'Set2', 'Set3', 'tab10', 'tab20', 'tab20b','tab20c']

file="C:\\Users\\ch1paf\\Downloads\\tmp\\saxs\\S14001.131"
with open(file, mode="rb" ) as file:    
    for i in range (0,(512*512)) : #0 as it stops one before final number
        data=file.read(4)
        datal +=[st.unpack('>f', data)] #convert to big endian
        
        
lndatal=np.log(datal)
maxZ=max(lndatal) 
minZ=min(lndatal)
print (minZ, maxZ)

frames=np.reshape(lndatal,(512,512))
k=0
# Plot the contour plots in 8x8 array
fig, ax = plt.subplots(8, 8, sharex='col', sharey='row')
for i in range(0,8,1):
    for j in range(0,8,1):   
        ax[i,j].set_title(cmg[k])
        cplot=ax[i,j].contourf(frames,cmap=cmg[k],vmax=9.0)
        k=k+1
         
plt.show()
