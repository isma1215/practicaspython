
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:44:50 2023

@author: isma
"""

import cv2
import numpy as np

rgb=cv2.imread("C://Intel//tigre.jpg")
f=rgb.shape
E = np.zeros((f[0],f[1]),dtype= np.float32)




for x in range (f[0]):
    for y in range(f[1]):
        E[x,y]=(0.299*rgb[:,:,2]) + (0.587*rgb[:,:,1]) + (0.114*rgb[:,:,2])
        
      
grises = E.astype(np.uint8)   

 
cv2.imshow("RGB",rgb)
cv2.imshow("Escala de grises",grises)

cv2.waitKey(0)
cv2.destroyAllWindows()