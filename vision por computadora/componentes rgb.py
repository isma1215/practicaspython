# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:41:28 2023

@author: isma
"""
import cv2
import numpy as np

rgb = cv2.imread("C:\\Intel\\joven.jpg")
cv2.imshow("rgb",rgb)
f = rgb.shape
b = np.zeros((f[0],f[1],f[2]),dtype= np.uint8);
g = np.zeros((f[0],f[1],f[2]),dtype= np.uint8);
r = np.zeros((f[0],f[1],f[2]),dtype= np.uint8);

for x in range (f[0]):
    for y in range (f[1]):
        for z in range(f[2]):
            if(z==0):
                b[x,y,z]=rgb[x,y,z]
            elif(z==1):
                g[x,y,z]=rgb[x,y,z]
            elif(z==2):
                r[x,y,z]=rgb[x,y,z]
    
cv2.imshow("rojo",r)
cv2.imshow("verde",g)
cv2.imshow("azul",b)

cv2.waitKey(0)
cv2.destroyAllWindows()
