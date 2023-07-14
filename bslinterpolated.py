# -*- coding: utf-8 -*-
"""
Patrick Fairclough
First attempt at BSL file reading
December 2022
"""
import struct as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata


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
lndatal[lndatal<2]=2
#frames=np.reshape(datal,(512,512))
frames=np.reshape(lndatal,(512,512))


k=0
z=[]
z_2=[]
x= np.mgrid[0:511:512j]
x_2= np.mgrid[0:511:1024]

'''
for i in range (0,512):
    for j in range (0,512):
        z[i:j]=lndatal[k]
        k=k+1 
'''   
   
grid_z0 = griddata(x, frames, x_2, method='nearest')
grid_z1 = griddata(x, frames, x_2, method='linear')
grid_z2 = griddata(x, frames, x_2, method='cubic')

frames0=np.reshape(grid_z0,(1024,1024))
frame1=np.reshape(grid_z1,(1024,1024))
frame2=np.reshape(grid_z2,(1024,1024))

fig,ax=plt.subplots(2,2)
ax[0,0].set_title('Original')
cplot=ax[0,0].contourf(frames,cmap='hsv',vmax=9.0)

ax[0,1].set_title('nearest')
cplot=ax[0,1].contourf(grid_z0,cmap='hsv',vmax=9.0)

ax[1,0].set_title('linear')
cplot=ax[1,0].contourf(grid_z1,cmap='hsv',vmax=9.0)

ax[1,1].set_title('cubic')
cplot=ax[1,1].contourf(grid_z2,cmap='hsv',vmax=9.0)

plt.show()

