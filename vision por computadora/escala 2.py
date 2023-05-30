# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:52:04 2022

@author: IPN_ESIME
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

Img = cv2.imread("C:\\Users\\IPN_ESIME\\Desktop\\EscalaGrises\\Spike.jpeg")
#cv2.imshow('imagen uno', Img)

a=Img.shape
E=np.zeros((a[0],a[1]), dtype=np.uint8)
I=np.zeros((a[0],a[1]), dtype=np.uint8)

R = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)
V = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)
A = np.zeros((a[0],a[1],a[2]), dtype=np.uint8)

for x in range (a[0]):
    for y in range(a[1]):
        E[x,y]=(Img[x,y,0]*0.299+Img[x,y,1]*0.587+Img[x,y,2]*0.114)

"""        
for x in range (a[0]):
    for y in range (a[1]):
        for z in range(a[2]):
            if(z==0):
                A[x,y]=Img[x,y,z]
            elif(z==1):
                V[x,y]=Img[x,y,z]
            elif(z==2):
                R[x,y]=Img[x,y,z]

cv2.imshow('Spike Azul',A)
cv2.imshow('Spike Verde',V)
cv2.imshow('Spike Rojo',R)
cv2.imshow('Spike Escala Grises',E) """
 
c=np.zeros(256)

for x in range (a[0]):
    for y in range(a[1]):
            c[E[x,y]]=c[E[x,y]]+1
           
         
                
        
        
plt.plot(c)
plt.xlabel("Niveles de grises")
plt.ylabel("Repeticiones")
plt.title("Grafica")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()