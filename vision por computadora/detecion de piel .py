# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:26:26 2023

@author: isma
"""

import cv2
import numpy as np

al =cv2.imread("C://Intel//alvina.jpg")
cv2.imshow('Imagen Original', al)

a=al.shape
piel=np.zeros((a[0],a[1]), dtype=np.uint8)
pielcolor=np.zeros((a[0],a[1],a[2]), dtype=np.uint8)

for x in range(a[0]):
    for y in range(a[1]):
        R = al[x,y,2]
        G = al[x,y,1]
        B = al[x,y,0]
        
        if(R>95 and G>40 and B>20 and (max(R,G,B)-min(R,G,B))>15 and abs(R-G)>15
           and R>G and R>B ):
            piel[x,y] = 255
            
            for z in range(a[2]):
                pielcolor[x,y,z] = al[x,y,z]
          
    
cv2.imshow('detecion de piel', piel) 
cv2.imshow('detecion de piel color', pielcolor) 
cv2.waitKey(0)
cv2.destroyAllWindows()