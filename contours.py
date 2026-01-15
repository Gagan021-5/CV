import cv2
import os


image_path = os.path.join('images', 'marvel.jpg')
image = cv2.imread(image_path)  

image_gry = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#threshold
ret, thresh =  cv2.threshold(image_gry,127,255,cv2.THRESH_BINARY_INV)
contours, hierarchy  = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if(cv2.contourArea(cnt)> 300):
        # cv2.drawContours(image,cnt,-1,(0,255,0),2)

        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image,(x1,y1),(x1 + w,y1 + h),(0,255,0),2)

cv2.imshow('image',image)
cv2.imshow('threshimage',thresh)
cv2.waitKey(0)
