# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:44:50 2023

@author: isma
"""

import cv2
import numpy as np

rgb=cv2.imread("C://Intel//tigre.jpg")
f=rgb.shape
b = np.zeros((f[0],f[1]),dtype= np.uint8)
g = np.zeros((f[0],f[1]),dtype= np.uint8)
r = np.zeros((f[0],f[1]),dtype= np.uint8)

Y = np.zeros((f[0],f[1]),dtype= np.float32)
cb= np.zeros((f[0],f[1]),dtype= np.float32)
cr= np.zeros((f[0],f[1]),dtype= np.float32)
YCbCr = np.zeros((f[0],f[1],f[2]),dtype=np.uint8)

for x in range (f[0]):  
    for y in range (f[1]):
        for z in range(f[2]):
            if(z==0):
                b[x,y]=rgb[x,y,z]
            elif(z==1):
                g[x,y]=rgb[x,y,z]
            elif(z==2):
                r[x,y]=rgb[x,y,z]


for x in range (f[0]):
    for y in range(f[1]):
        Y[x,y]=(0.299*r[x,y]) + (0.587*g[x,y]) + (0.114*b[x,y])
        cb[x,y]=(-0.169*r[x,y]) + (-0.331*g[x,y]) + (0.5*b[x,y])  + 128
        cr[x,y]=(0.5*r[x,y]) + (-0.419*g[x,y]) + (-0.081*b[x,y])  + 128
        
      
y8 = Y.astype(np.uint8)   
cb8= cb.astype(np.uint8)
cr8= cr.astype(np.uint8)

for x in range (f[0]):
    for y in range(f[1]):
        YCbCr[x,y,0] = y8[x,y]
        YCbCr[x,y,1] = cb8[x,y]
        YCbCr[x,y,2] = cr8[x,y]

cv2.imshow("YCbCr",YCbCr)
cv2.imshow("Y",y8)
cv2.imshow("Cb",cb8)
cv2.imshow("Cr",cr8)
cv2.waitKey(0)
cv2.destroyAllWindows()