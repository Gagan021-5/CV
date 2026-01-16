import cv2
from browncolor import get_limits
from PIL import Image


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()


    hsvimg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerlimit , upperlimit = get_limits("blue")

    mask = cv2.inRange(hsvimg,lowerlimit,upperlimit)
    masknew = Image.fromarray(mask)
    
    bbox = masknew.getbbox()

    if bbox is not None:
        x1,y1,x2,y2 = bbox

        

    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)    
    cv2.imshow('frame',frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


