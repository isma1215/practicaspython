# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:08:05 2023

@author: isma
"""

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
hsv = np.zeros((f[0],f[1],f[2]),dtype= np.float32);

capah = np.zeros((f[0],f[1]),dtype= np.float32);
capas = np.zeros((f[0],f[1]),dtype= np.float32);
capav = np.zeros((f[0],f[1]),dtype= np.float32);

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
    if(maximo == 0):
        return 0
    else:
        return 1 - (minimo/maximo)

def tono(maximo,minimo,r,g,b):
    max_min = maximo-minimo
    if (maximo==minimo):
        return 0
    
    elif (maximo == r and g>=b ):
        return  60 * ( (g-b)/max_min )
    
    elif (maximo == r and g<b):
        return (60*( (g-b)/max_min) ) + 360
    
    elif (maximo == g):
        return (60*( (b-r)/max_min) ) +120
    
    elif (maximo == b):
        return (60*( (r-g)/max_min) ) + 240

        
for x in range(f[0]):
    for y in range(f[1]):
        for z in range(f[2]):
            
            v=max(r[x,y],g[x,y],b[x,y])
            minimo= min(r[x,y],g[x,y],b[x,y])
            
            s = saturacion(v,minimo)
            h = tono(v,minimo,r[x,y],g[x,y],b[x,y])
            
            hsv[x,y,0]=capah[x,y]=h 
            hsv[x,y,1]=capas[x,y]=s
            hsv[x,y,2]=capav[x,y]=v

            
cv2.imshow("capa h",capah)
cv2.imshow("capa s",capas)
cv2.imshow("capa i",capav)
cv2.imshow("imagrn hsv",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()