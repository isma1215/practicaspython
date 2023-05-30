# -*- coding: utf-8 -*-
import numpy as np
import cv2


A=cv2.imread("C:\\Intel\\carros.jpg")

#cv2.imshow('imagen', A)

f = A.shape

E=np.zeros((f[0], f[1]), dtype=np.float32)

for x in range (f[0]): 
    for y in range(f[1]):
        E[x,y]= A[x,y,0]*0.299 + A[x,y,1]*0.587 + A[x,y,2]*0.114

Ef = E.astype(np.float32)
px = np.zeros((f[0],f[1]),dtype=np.float32)
py = np.zeros((f[0],f[1]),dtype=np.float32)

for x in range(1,f[0]-1):
    for y in range(1,f[1]-1):
        px[x,y] = (-E[x-1,y-1] + E[x+1,y-1]
                   -E[x-1,y] + E[x+1,y]
                   -E[x-1,y+1]+ E[x+1,y+1]) /6
        
        if px[x,y] < 0:
            px[x,y]=0
            

for x in range(1,f[0]-1):
    for y in range(1,f[1]-1):
        py[x,y] = (-E[x-1,y-1] -E[x,y-1] -E[x+1,y-1]
                   +E[x-1,y+1] +E[x,y+1] +E[x+1,y+1])/6
        
        if py[x,y] < 0:
            py[x,y]=0



E8 = E.astype(np.uint8)           
Prx = px.astype(np.uint8)
Pry = py.astype(np.uint8)
cv2.imshow("original",E8)
cv2.imshow("prewitt x",Prx)
cv2.imshow("prewitt y",Pry)
cv2.waitKey(0)
cv2.destroyAllWindows()