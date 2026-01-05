import cv2
import os

image_path = os.path.join('images', 'marvel.jpg')
image = cv2.imread(image_path)
print(image.shape)
#Crop image 

cropped_img = image[100:648,220:940]



cv2.imshow('image',image)
cv2.imshow("croppedimage",cropped_img)
cv2.waitKey(0)
