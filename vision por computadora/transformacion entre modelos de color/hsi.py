# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:43:05 2023

@author: isma
"""
import cv2 
import numpy as np

rgb = cv2.imread("C:\\Intel\\tigre.jpg")

f= rgb.shape
b = np.zeros((f[0],f[1]),dtype= np.float32);
g = np.zeros((f[0],f[1]),dtype= np.float32);
r = np.zeros((f[0],f[1]),dtype= np.float32);
hsi = np.zeros((f[0],f[1],f[2]),dtype= np.float32);

capah = np.zeros((f[0],f[1]),dtype= np.float32);
capas = np.zeros((f[0],f[1]),dtype= np.float32);
capai = np.zeros((f[0],f[1]),dtype= np.float32);

for x in range (f[0]):
    for y in range (f[1]):
        for z in range(f[2]):
            if(z==0):
                b[x,y]=rgb[x,y,z]/255
            elif(z==1):
                g[x,y]=rgb[x,y,z]/255
            elif(z==2):
                r[x,y]=rgb[x,y,z]/255
                
                
def saturacion(maximo,minimo):
    l=maximo+minimo/2
    if(maximo==minimo):
        return 0
    elif(l<=.5):
        return (maximo-minimo)/(maximo+minimo)
    elif(l>.5):
        return (maximo-minimo)/(2 - (maximo+minimo))

def tono(maximo,minimo,r,g,b):
    if(maximo==minimo):
        return 0
    
    elif(maximo==r):
        return (60*  ( (g-b)/maximo-minimo)  ) +360
    
    elif(maximo==g):
        return (60*  ( (b-r)/maximo-minimo)  ) +120
    
    elif(maximo==b):
        return (60*  ( (r-g)/maximo-minimo)  ) +240
        
for x in range(f[0]):
    for y in range(f[1]):
        for z in range(f[2]):
            
            maximo= max(r[x,y],g[x,y],b[x,y])
            minimo= min(r[x,y],g[x,y],b[x,y])
            
            i = (maximo + minimo)/2
            s = saturacion(maximo,minimo)
            h = tono(maximo,minimo,r[x,y],g[x,y],b[x,y])
            
            hsi[x,y,0]=capah[x,y]=h 
            hsi[x,y,1]=capas[x,y]=s
            hsi[x,y,2]=capai[x,y]=i

           
cv2.imshow("capa h",capah)
cv2.imshow("capa s",capas)
cv2.imshow("capa i",capai)
cv2.imshow("imagrn hsi",hsi)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
            
            
        