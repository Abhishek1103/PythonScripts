import numpy as np
import cv2

#cap=cv2.VideoCapture('output.mp4')
cap=cv2.VideoCapture('output.mp4')

while(cap.isOpened()):

    ret,frame=cap.read()

    #Play video in grayscale
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gray)

    cv2.imshow('frame',frame)   #Play video as it is

    if cv2.waitKey(25) & 0xFF == ord('q'):  #delay of 25 is given so that video could be drawn on the frame
        break


cap.release()
cv2.destroyAllWindows()
