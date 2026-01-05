import cv2
import os
#read image 
image_path = os.path.join('images', 'parrot.jpg')
image = cv2.imread(image_path)  

img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
img_bgr= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('image',img_bgr)
cv2.imshow('imrgb',img_rgb)
cv2.imshow('imhsv',img_hsv)
cv2.waitKey(0)