# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:42:54 2023

@author: isma
"""
import cv2 
import numpy as np

rgb = cv2.imread("C:\\Intel\\apex.jpg")

f= rgb.shape
b = np.zeros((f[0],f[1]),dtype= np.uint8);
g = np.zeros((f[0],f[1]),dtype= np.uint8);
r = np.zeros((f[0],f[1]),dtype= np.uint8);
cmy = rgb.astype(np.float32)/255

for x in range (f[0]):  
    for y in range (f[1]):
        for z in range(f[2]):
            if(z==0):
                b[x,y]=rgb[x,y,z]
            elif(z==1):
                g[x,y]=rgb[x,y,z]
            elif(z==2):
                r[x,y]=rgb[x,y,z]

for x in range(f[0]):
    for y in range(f[1]):
        k= 1 - max(r[x,y]/255,g[x,y]/255,b[x,y]/255)
        c[x]=( (1-(r[x,y]/255) ) - k) / (1-k)
        [x]=( (1-(g[x,y]/255) ) - k) / (1-k)
        =( (1-(b[x,y]/255) ) - k) / (1-k)

CMYK = (cmy * 255).astype(np.uint8)

cv2.imshow("cmy",cmy)
cv2.waitKey(0)
cv2.destroyAllWindows()