import numpy as np
import cv2

cap = cv2.VideoCapture('bmw.mp4')
#To check if video is there
if cap.isOpened() == False:
    print("Cannot open file or video stream")

#Looping through since videos have frames. It has two return values return
#and frame

while True:
    ret,frame = cap.read()

    if ret == True:
        cv2.imshow('Frame',frame)
#Wait for 25 ms or until escape key is pressed
        if cv2.waitKey(25) & 0xFF == 27:
            break
        else:
            break






cap.release()
cv2.destroyAllWindows()
