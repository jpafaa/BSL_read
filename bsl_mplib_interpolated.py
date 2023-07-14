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
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

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


fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(frames, interpolation=interp_method, cmap='hsv')
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()