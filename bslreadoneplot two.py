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
fig,ax=plt.subplots(1,1)

cp = ax.contourf(frames,cmap='hsv',vmin=1.0,vmax=9.0)      
fig.colorbar(cp)
   
plt.show()
k=0
x=[]
y=[]
z=[]
#x=np.linspace(0,512,num=512)
#y=np.linspace(0,512,num=512)
#x_2 = np.linspace(0,512,num=1024)
#y_2 = np.linspace(0,512,num=1024)
z_2=[]
x, y = np.mgrid[0:512, 0:512]
x_2, y_2 = np.mgrid[0:512:1024, 0:512:1024j]
for i in range (0,512):
    for j in range (0,512):
        z[i:j]=lndatal[k]
        k=k+1       
        
print (i,j,((i+1)*(j+1)),k)

grid_z0 = griddata(x,y, z, (x_2, y_2), method='nearest')
grid_z1 = griddata(x,y, z, (x_2, y_2), method='linear')
grid_z2 = griddata(x,y, z, (x_2, y_2), method='cubic')
plt.subplot(221)
ax.set_title('Original')
cp = ax.contourf(z,cmap='hsv',vmin=1.0,vmax=9.0)      
plt.subplot(222)
ax.set_title('closest')
cp = ax.contourf(grid_z0,cmap='hsv',vmin=1.0,vmax=9.0) 
plt.subplot(223)
ax.set_title('linear')
cp = ax.contourf(grid_z1,cmap='hsv',vmin=1.0,vmax=9.0) 
plt.subplot(224)
ax.set_title('cubic')
cp = ax.contourf(grid_z2,cmap='hsv',vmin=1.0,vmax=9.0) 
plt.show()

