# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:53:43 2022

@author: IPN_ESIME
"""

import cv2
import numpy as np


Img = cv2.imread("C:\\Intrl(")


a=Img.shape
E=np.zeros((a[0],a[1]), dtype=np.uint8)
I=np.zeros((a[0],a[1]), dtype=np.uint8)
B=np.zeros((a[0],a[1]), dtype=np.uint8)
U=np.zeros((a[0],a[1]), dtype=np.uint8)

R = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)
V = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)
A = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)

for x in range (a[0]):
    for y in range(a[1]):
        E[x,y]=(Img[x,y,0]*0.299+Img[x,y,1]*0.587+Img[x,y,2]*0.114)

for x in range (a[0]):
    for y in range(a[1]):
        I[x,y]=255-E[x,y]
             

for x in range (a[0]):
    for y in range(a[1]):
        if( 10 <= E[x,y] <=50 ):
            U[x,y]=255

for x in range (a[0]):
    for y in range(a[1]):
        if( 10 < E[x,y] <=50 ):
            B[x,y]=255
        
        
#cv2.imshow("asd", I)
#cv2.imshow("original", E)
cv2.imshow("Um", U)
cv2.imshow("Bin", B)

cv2.waitKey(0)
cv2.destroyAllWindows()