# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:53:43 2022

@author: IPN_ESIME
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

Img = cv2.imread("C:\\Intel\\cross.jpg")


a=Img.shape
E=np.zeros((a[0],a[1]), dtype=np.uint8)
I=np.zeros((a[0],a[1]), dtype=np.uint8)
B=np.zeros((a[0],a[1]), dtype=np.uint8)
U=np.zeros((a[0],a[1]), dtype=np.uint8)

R = np.zeros((a[0],a[1]), dtype=np.uint8)
V = np.zeros((a[0],a[1]), dtype=np.uint8)
A = np.zeros((a[0],a[1]), dtype=np.uint8)
UBI = np.zeros((a[0],a[1]), dtype=np.uint8)
UEG = np.zeros((a[0],a[1]), dtype=np.uint8)
UEGI = np.zeros((a[0],a[1]), dtype=np.uint8)
c=np.zeros(256)

for x in range (a[0]):
    for y in range(a[1]):
        E[x,y]=(Img[x,y,0]*0.299+Img[x,y,1]*0.587+Img[x,y,2]*0.114)

for x in range (a[0]):
    for y in range(a[1]):
        I[x,y]=255-E[x,y]

p1=150
p2=200           

for x in range (a[0]):
    for y in range(a[1]):
        if(E[x,y]<=p1):
            U[x,y]=255
        elif(E[x,y]>=p2):
            U[x,y]=255

for x in range (a[0]):
    for y in range(a[1]):
        if( E[x,y] < p1 ):
            B[x,y]=255
        elif( E[x,y] >= p2 ):
            B[x,y]=255
            
for x in range (a[0]):
    for y in range(a[1]):
        if(p1 < E[x,y] < p2):
            UBI[x,y]=255
            
for x in range (a[0]):
    for y in range(a[1]):
        if(E[x,y] <= p1):
            UEG[x,y] = 255
        elif(E[x,y] >= p2):
            UEG[x,y]=255
        elif(p1<E[x,y]<p2):
            UEG[x,y] = E[x,y]

for x in range (a[0]):
    for y in range(a[1]):
        if(E[x,y] <= p1):
            UEGI[x,y]=255
        elif(E[x,y] >= p2):
            UEGI[x,y]=255
        elif(p1 < E[x,y] < p2):
            UEGI[x,y] = 255 - E[x,y]

for x in range (a[0]):
    for y in range(a[1]):
        c[E[x,y]]=c[E[x,y]]+1
                   
                 
                        
plt.plot(c)
plt.xlabel("Niveles de grises")
plt.ylabel("Repeticiones")
plt.title("Grafica")
plt.show()

cv2.imshow("original", E)        
cv2.imshow("Negativo", I)
cv2.imshow("Umbral", U)
cv2.imshow("Umbral Binario", B)
cv2.imshow("Umbral Binario Invertido", UBI)
cv2.imshow("Umbral de Escala de Grises", UEG)
cv2.imshow("Umbral de Escala de Grises Invertida", UEGI)

cv2.waitKey(0)
cv2.destroyAllWindows()