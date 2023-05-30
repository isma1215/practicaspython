# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:19:15 2023

@author: isma
"""

import cv2
import numpy as np
import math 

img = cv2.imread("C:\\Intel\\perro.jpg")
f = img.shape
a= np.zeros((f[0],f[1]), dtype=np.uint8)
bfloat= np.zeros((f[0],f[1]), dtype = np.float32)


for x in range (f[0]):
    for y in range (f[1]):
        a[x,y] = img[x,y,0]*0.299 + img[x,y,1]*0.587 + img[x,y,2]*0.114
        
alfa = 10
for x in range (f[0]):
    for y in range (f[1]):
        bfloat[x,y] = pow((a[x,y]/255),alfa)*255
gama = bfloat.astype(np.uint8)

for x in range (f[0]):
    for y in range (f[1]):
        bfloat[x,y] = (  (255 / ( math.log( (alfa * 255) + 1) ) *  math.log( (alfa * a[x,y]) +1)  )  )
blog = bfloat.astype(np.uint8) 

for x in range (f[0]):
    for y in range(f[1]):
        bfloat[x,y] = ( 255 * ( math.sin( (math.radians(270) * a[x,y])/ (2*255) ) )   )
bsin = bfloat.astype(np.uint8);      
       
for x in range(f[0]):
    for y in range(f[1]):
        bfloat[x,y] = 250 * (1-math.cos((math.radians(270)*a[x,y])/510 ) )
bcos= bfloat.astype(np.uint8)

for x in range (f[0]):
    for y in range (f[1]):
        bfloat[x,y] = (  (255/(1-math.exp(-alfa)) )*(1-math.exp((-alfa * a[x,y])/255))     )
bexp= bfloat.astype(np.uint8)

for x in range (f[0]):
    for y in range (f[1]):
        bfloat[x,y] = ( ( 255/(math.exp(alfa)-1) )*(math.exp((alfa*a[x,y])/255)-1) )
bexpc = bfloat.astype(np.uint8)


cv2.imshow("escala de grises", a)
#cv2.imshow("correccion gama", gama)
#cv2.imshow("logaridmica", blog)
#cv2.imshow("senoidal",bsin)
#cv2.imshow("cosenoidal",bcos)
#cv2.imshow("exponencial",bexp)
cv2.imshow("exponencial creciente",bexpc)



cv2.waitKey(0)
cv2.destroyAllWindows();