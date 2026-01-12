import cv2
import os
import numpy as np
#read image 
image_path = os.path.join('images', 'basketball.jpg')
image = cv2.imread(image_path)  


#edge det
edgeimage = cv2.Canny(image,200,300)

imageedgedil = cv2.dilate(edgeimage,np.ones((5,5),dtype=np.int8))
imageerode = cv2.erode(imageedgedil,np.ones((3,3),dtype=np.int8))





cv2.imshow('img',image)
cv2.imshow('edgedimg',edgeimage)
cv2.imshow('edgedimgdilated',imageedgedil)
cv2.imshow('imageerode',imageerode)
cv2.waitKey(0)
