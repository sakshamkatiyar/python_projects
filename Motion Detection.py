import numpy as np
import cv2 
cap = cv2.VideoCapture(2)
ret, frame = cap.read()
gray_old = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
while(True):
    ret, frame = cap.read()
    gray_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_diff = cv2.absdiff(gray_new,gray_old)
    cv2.imshow('Result',img_diff)
    if cv2.countNonZero(img_diff) > 2000:
        print ("yo whats up")
    gray_old = gray_new
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows() 
