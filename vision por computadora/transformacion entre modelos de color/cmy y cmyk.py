# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:42:54 2023

@author: isma
"""
import cv2 
import numpy as np
rgb = cv2.imread("C:\\Intel\\tigre.jpg")

f= rgb.shape
b = np.zeros((f[0],f[1]),dtype= np.float32);
g = np.zeros((f[0],f[1]),dtype= np.float32);
r = np.zeros((f[0],f[1]),dtype= np.float32);
cmy = np.zeros((f[0],f[1],f[2]),dtype= np.float32);
cmyk = np.zeros((f[0],f[1],f[2]+1),dtype= np.float32);

for x in range (f[0]):  
    for y in range (f[1]):
        for z in range(f[2]):
            if(z==0):
                b[x,y]=rgb[x,y,z]/255
            elif(z==1):
                g[x,y]=rgb[x,y,z]/255
            elif(z==2):
                r[x,y]=rgb[x,y,z]/255

for x in range(f[0]):
    for y in range(f[1]):
        cmy[x,y,0] = 1 - r[x,y]
        cmy[x,y,1] = 1 - g[x,y]
        cmy[x,y,2] = 1 - b[x,y]

        cmyk[x,y,3] = k = 1 - max(r[x,y],g[x,y],b[x,y])
        cmyk[x,y,0] = (1-r[x,y]-k)/(1-k)
        cmyk[x,y,1] = (1-g[x,y]-k)/(1-k)
        cmyk[x,y,2] = (1-b[x,y]-k)/(1-k)
        
#cv2.imshow("cmy",cmy)
#cv2.imshow("componente C", cmy[:,:,0])    
#cv2.imshow("componente M", cmy[:,:,1])
#cv2.imshow("componente Y", cmy[:,:,2])     
cv2.imshow("cmyk",cmyk)
cv2.imshow(" cmyk componente C", cmyk[:,:,0])    
cv2.imshow(" cmyk componente M", cmyk[:,:,1])
cv2.imshow(" cmyk componente Y", cmyk[:,:,2]) 
cv2.imshow(" cmyk componente k", cmyk[:,:,3]) 
cv2.waitKey(0)
cv2.destroyAllWindows()