import cv2
import os
#read image 
image_path = os.path.join('images', 'marvel.jpg')
image = cv2.imread(image_path)

#write image 
cv2.imwrite(os.path.join('images', 'marvelnew.jpg'),image)
print(image.shape)

#Basic operations on image
resizedimage = cv2.resize(image,(640,480))
print(resizedimage.shape)


#visualize image 
cv2.imshow('image',image)
cv2.imshow('resizemaged',resizedimage)
cv2.waitKey(0)

