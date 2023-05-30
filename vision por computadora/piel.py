# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:52:32 2023

@author: isma
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:47:39 2022

@author: moise
"""
import cv2
import numpy as np

imagen =cv2.imread("C://Intel//men.png")
cv2.imshow('Imagen Original', imagen)

a=imagen.shape
uno=np.zeros((a[0],a[1]), dtype=np.uint8)
dos=np.zeros((a[0],a[1],a[2]), dtype=np.uint8)

for x in range(a[0]):
    for y in range(a[1]):
        R = imagen[x,y,2]
        G = imagen[x,y,1]
        B = imagen[x,y,0]
             
        if(R>95 and G>40 and B>20 and (max(R,G,B)-min(R,G,B))>15 and abs(R-G)>15
           and R>G and R>B ):
            uno[x,y] = 255
            

for x in range(a[0]):
    for y in range(a[1]):  
        for z in range(a[2]):
            if(uno[x,y] == 255):
                dos[x,y,z] = imagen[x,y,z]
               
cv2.imshow('piel binario', uno) 
cv2.imshow("color",dos)
cv2.waitKey(0)
cv2.destroyAllWindows()