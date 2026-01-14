import cv2
import os
#read image 
image_path = os.path.join('images', 'whiteboard.jpg')
image = cv2.imread(image_path)  

#line

cv2.line(image,(200,150),(300,450),(255,0,0),3)

#rectangle 
cv2.rectangle(image,(200,350),(400,500),(0,255,255),9)


#circle 
cv2.circle(image,(500,500),70,(0,255,0),3)


#putText
cv2.putText(image,'Hello there!',(500,400),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)



cv2.imshow('image',image)
cv2.waitKey(0)