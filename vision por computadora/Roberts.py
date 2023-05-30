"""
Created on Thu Jan 19 18:01:28 2023

@author: IPN_ESIME
"""

import cv2 
import numpy as np

A = cv2.imread("C:\\Intel\\jamie.jpg")
f=A.shape
E = np.zeros((f[0],f[1]),dtype=np.uint8)

for x in range(f[0]):
    for y in range(f[1]):
        E[x,y] = A[x,y,0]*0.299 + A[x,y,1]*0.587 + A[x,y,2]*0.114

rx = np.array([
    [0,1],
    [-1,0],
    ])
ry = np.array([
    [1,0],
    [0,-1],
    ])
ro = rx + ry

robertsx = cv2.filter2D(E,-1, rx)
robertsy = cv2.filter2D(E,-1, ry)
roberts = cv2.filter2D(E,-1, ro)

cv2.imshow("original",E)
cv2.imshow("robers eje x",robertsx)
cv2.imshow("robers eje y",robertsy)
cv2.imshow("robers eje x , y",roberts)
cv2.waitKey(0)
cv2.destroyAllWindows()