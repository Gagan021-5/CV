import cv2
import os

image_path = os.path.join('images', 'marvel.jpg')
image = cv2.imread(image_path)

grayscaled = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(grayscaled,80,255,cv2.THRESH_BINARY)

cv2.imshow('Original Image', grayscaled)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
