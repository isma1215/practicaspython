# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 16:26:21 2023

@author: isma
"""

import cv2
import numpy as np
Img = cv2.imread("C:\\Intel\\z400.jpg")
#Img = cv2.imread("C:\\Intel\\grafiti.png")


a=Img.shape
E=np.zeros((a[0],a[1]), dtype=np.uint8)
"kernels Horizontal y vertical"
PreY = np.array([
    [-1,0,1],
    [-1,0,1],
    [-1,0,1] ])
Prex = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1] ])
sobY = np.array([
    [-1,0,1],
    [-1,0,1],
    [-1,0,1] ])
sobx = np.array([
       [-1,-2,-1],
        [0,0,0],
        [1,2,1] ])
IsoY = np.array([
    [-1,0,1],
    [-(np.sqrt(2)),0,np.sqrt(2)],
    [-1,0,1] ])
Isox = np.array([
    [-1,-(np.sqrt(2)),-1],
    [0,0,0],
    [1,np.sqrt(2),1] ])
Roby = np.array([
    [0,1],
    [-1,0]])
Robx = np.array([
    [1,0],
    [0,-1]])

"kernels Kirsch"
Gra0 = np.array([
    [-3,-3,5],
    [-3,0,5],
    [-3,-3,5] ])
Gra45 = np.array([
    [-3,5,5],
    [-3,0,5],
    [-3,-3,-3] ])
Gra90 = np.array([
    [5,5,5],
    [-3,0,-3],
    [-3,-3,-3] ])
Gra135 = np.array([
    [5,5,-3],
    [5,0,-3],
    [-3,-3,-3] ])
Gra180 = np.array([
    [5,-3,-3],
    [5,0,-3],
    [5,-3,-3] ])
Gra225 = np.array([
    [-3,-3,-3],
    [5,0,-3],
    [5,5,-3] ])
Gra270 = np.array([
    [-3,-3,-3],
    [-3,0,-3],
    [5,5,5] ])
Gra315 = np.array([
    [-3,-3,-3],
    [-3,0,5],
    [-3,5,5] ])

"kernels Robinson"
Rgra0 = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1] ])
Rgra45 = np.array([
    [-0,1,2],
    [-1,0,1],
    [-2,-1,0] ])
Rgra90 = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1] ])
Rgra135 = np.array([
    [2,1,0],
    [1,0,-1],
    [0,-1,-2] ])
Rgra180 = np.array([
    [1,0,-1],
    [2,0,-2],
    [1,0,-1] ])
Rgra225 = np.array([
    [0,-1,-2],
    [1,0,-1],
    [2,1,0] ])
Rgra270 = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1] ])
Rgra315 = np.array([
    [-2,-1,0],
    [-1,0,1],
    [0,1,2] ])

"kernels Frei-Chen"
Freh = np.array([
    [1,np.sqrt(2),1],
    [0,0,0],
    [-1,-np.sqrt(2),-1]
    ]) / (1 / 2*np.sqrt(2))
Frev = np.array([
    [1,0,-1],
    [np.sqrt(2),0,-np.sqrt(2)],
    [-1,0,-1]
    ]) / (1 / 2*np.sqrt(2))
Fred = np.array([
    [0,-1,-np.sqrt(2)],
    [1,0,-1],
    [np.sqrt(2),1,0]
    ]) / (1 / 2*np.sqrt(2))
Fred2 = np.array([
    [np.sqrt(2),-1,0],
    [-1,0,1],
    [0,1,-np.sqrt(2)]
    ]) / (1 / 2*np.sqrt(2))
Fre = np.array([
    [0,1,0],
    [-1,0,-1],
    [0,1,0]
    ]) * .5

"x,y"
XY = np.array([
    [0,1,0],
    [1,-4,1],
    [0,1,0]
    ])

for x in range (a[0]):
    for y in range(a[1]):
        E[x,y]=(Img[x,y,0]*0.299+Img[x,y,1]*0.587+Img[x,y,2]*0.114)

PrewittY = cv2.filter2D(E,-1,PreY)
PrewittX = cv2.filter2D(E,-1,Prex)
SobelX = cv2.filter2D(E,-1,sobx)
SobelY = cv2.filter2D(E,-1,sobY) 
IsotY = cv2.filter2D(E,-1,IsoY) 
Isotx = cv2.filter2D(E,-1,Isox)         
Rox = cv2.filter2D(E,-1,Robx)  
Roy = cv2.filter2D(E,-1,Roby)

Kir0 =cv2.filter2D(E,-1,Gra0)   
Kir45 =cv2.filter2D(E,-1,Gra45)    
Kir90 =cv2.filter2D(E,-1,Gra90)    
Kir135 =cv2.filter2D(E,-1,Gra135)    
Kir180 =cv2.filter2D(E,-1,Gra180)    
Kir225 =cv2.filter2D(E,-1,Gra225)                    
Kir270 =cv2.filter2D(E,-1,Gra270)   
Kir315 =cv2.filter2D(E,-1,Gra315)  

Rob0 =cv2.filter2D(E,-1,Rgra0)      
Rob45 =cv2.filter2D(E,-1,Rgra45)      
Rob90 =cv2.filter2D(E,-1,Rgra90) 
Rob135 =cv2.filter2D(E,-1,Rgra135)           
Rob180 =cv2.filter2D(E,-1,Rgra180)      
Rob225 =cv2.filter2D(E,-1,Rgra225)      
Rob270 =cv2.filter2D(E,-1,Rgra270)      
Rob315 =cv2.filter2D(E,-1,Rgra315)  
    
Frei1 =cv2.filter2D(E,-1,Freh) 
Frei2 =cv2.filter2D(E,-1,Frev) 
Frei3 =cv2.filter2D(E,-1,Fred) 
Frei4 =cv2.filter2D(E,-1,Fred2) 
Frei5 =cv2.filter2D(E,-1,Fre) 

FXY = cv2.filter2D(E,-1,XY)
#cv2.imshow("original", E)
#cv2.imshow("Prewitt Horizontal",PrewittX)
#cv2.imshow("Prewitt  Vertical",PrewittY)   
#cv2.imshow("Sobel  Vertical",SobelY)     
#cv2.imshow("Sobel Horizontal",SobelX)  
#cv2.imshow("Isotropico Horizontal",Isotx)
#cv2.imshow("Isotropico Vertical", IsotY)  
#cv2.imshow("Roberts Horizontal",Rox)
#cv2.imshow("Roberts Vertical",Roy)
#cv2.imshow("Frei 0 grados",Frei0)
#cv2.imshow("kir 0 grados",Kir0)
#cv2.imshow("kir 45 grados",Kir45)
#cv2.imshow("kir 90 grados",Kir90)
#cv2.imshow("kir 135 grados",Kir135)
#cv2.imshow("kir 180 grados",Kir180)
#cv2.imshow("kir 225 grados",Kir225)
#cv2.imshow("kir 270 grados",Kir270)
#cv2.imshow("kir 315 grados",Kir315)

#cv2.imshow("Rob 0 grados",Rob0)
#cv2.imshow("Rob 45 grados",Rob45)
#cv2.imshow("Rob 90 grados",Rob90)
#cv2.imshow("Rob 135 grados",Rob135)
#cv2.imshow("Rob 180 grados",Rob180)
#cv2.imshow("Rob 225 grados",Rob225)
#cv2.imshow("Rob 270 grados",Rob270)
#cv2.imshow("Rob 315 grados",Rob315)

#cv2.imshow("Fre h",Frei1)
#cv2.imshow("Fre v",Frei2)
#cv2.imshow("Fre d",Frei3)
#cv2.imshow("Fre d2",Frei4)
#cv2.imshow("Fre ",Frei5)
cv2.imshow("filtro x , y ",FXY)



cv2.waitKey(0)
cv2.destroyAllWindows()