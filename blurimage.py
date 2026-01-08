import cv2
import os
#read image 
image_path = os.path.join('images', 'cow.png')
image = cv2.imread(image_path)  

k_size = 7
blurred= cv2.blur(image,(k_size,k_size))
gaussianblur = cv2.GaussianBlur(image,(k_size,k_size),3)
median_blur = cv2.medianBlur(image,k_size)


cv2.imshow('img',image)
# cv2.imshow('gausblurred',gaussianblur)
# cv2.imshow('blurred',blurred)
cv2.imshow('median_blur',median_blur)
cv2.waitKey(0)
