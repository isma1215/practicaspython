# -*- coding: utf-8 -*-
import numpy as np
import cv2


A=cv2.imread("C:\\Intel\\perico1.jpg")

#cv2.imshow('imagen', A)

f = A.shape

E=np.zeros((f[0], f[1]), dtype=np.uint8)

for x in range (f[0]): 
    for y in range(f[1]):
        E[x,y]= A[x,y,0]*0.299 + A[x,y,1]*0.587 + A[x,y,2]*0.114

Ef = E.astype(np.float32)
Bfx=np.zeros((f[0],f[1]), dtype=np.float32);
B2fx=np.zeros((f[0],f[1]), dtype=np.float32);
Bfy=np.zeros((f[0],f[1]), dtype=np.float32);

for x in range (f[0]-1): 
    for y in range(f[1]):
        Bfx[x,y] = ( (Ef[x+1,y]) - (Ef[x,y]) )
        if Bfx[x,y] < 0:
            Bfx[x,y] = 0
            
for x in range (f[0]-1): 
    for y in range(f[1]):
        B2fx[x,y] = ( E[x-1,y] - (2*E[x,y]) + E[x+1,y] )
        if B2fx[x,y] < 0:
            B2fx[x,y] = 0
                       
for x in range (f[0]): 
    for y in range(f[1]-1):
        Bfy[x,y] = ( (Ef[x,y+1]) - (Ef[x,y]) )
        if Bfy[x,y] < 0:
            Bfy[x,y] = 0
             
        
'''for x in range (f[0]): 
    for y in range(f[1]):
        if Bf[x,y] < 0:
            Bf[x,y]= Bf[x,y]*-1 '''



Bx = Bfx.astype(np.uint8)
B2x = B2fx.astype(np.uint8)
By = Bfy.astype(np.uint8)
#cv2.imshow('Escala', E)
#cv2.imshow("derivada x",Bx)
#cv2.imshow("segunda derivada x",B2x)
#cv2.imshow("derivada y",By)
cv2.waitKey(0)
cv2.destroyAllWindows()