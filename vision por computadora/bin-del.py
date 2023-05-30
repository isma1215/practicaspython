# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:53:43 2022

@author: IPN_ESIME
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

Img = cv2.imread("C:\\Intel\\img1.jpeg")


a=Img.shape
E=np.zeros((a[0],a[1]), dtype=np.uint8)
B=np.zeros((a[0],a[1]), dtype=np.uint8)
U=np.zeros((a[0],a[1]), dtype=np.uint8)
kernel = np.ones(([3,3]),dtype=np.uint8)

c=np.zeros(256)

for x in range (a[0]):
    for y in range(a[1]):
        E[x,y]=(Img[x,y,0]*0.299+Img[x,y,1]*0.587+Img[x,y,2]*0.114)


p1=0
p2=20#negroo

for x in range (a[0]):
    for y in range(a[1]):
        if( E[x,y] < p1 ):
            B[x,y]=255
        elif( E[x,y] >= p2):
            B[x,y] = 255
        elif( E[x,y] >= 129):
                B[x,y] = 0

       
for x in range (a[0]):
    for y in range(a[1]):
        c[E[x,y]]=c[E[x,y]]+1
                   
#Dil=cv2.dilate(U,kernel)
        
                        
plt.plot(c)
plt.xlabel("Niveles de grises")
plt.ylabel("Repeticiones")
plt.title("Grafica")
plt.show()

cv2.imshow("original", E)
cv2.imshow("binaria",B)    
#cv2.imshow("dil",Dil)


cv2.waitKey(0)
cv2.destroyAllWindows()