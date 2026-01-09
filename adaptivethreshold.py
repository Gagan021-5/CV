import cv2
import os

image_path = os.path.join('images', 'handwritten.png')
image = cv2.imread(image_path)


grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, simple_thresh = cv2.threshold(grayscaled, 80, 255, cv2.THRESH_BINARY)

adaptive_thresh = cv2.adaptiveThreshold(
    grayscaled,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    21,  
    30
)

cv2.imshow('Original Image', image)
cv2.imshow('Simple Threshold', simple_thresh)
cv2.imshow('Adaptive Threshold', adaptive_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
