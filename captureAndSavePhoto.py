import numpy as np
import cv2

#cap=cv2.VideoCapture('output.mp4')
print("Press \'q\' to exit and \'s\' to save....!!")
cap=cv2.VideoCapture(0)
c=0
while(cap.isOpened()):

    ret,frame=cap.read()
    frame = cv2.flip(frame,90)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('s'):
        c += 1
        cv2.imwrite('ScreenShot'+str(c)+'.png',frame)

cap.release()
cv2.destroyAllWindows()
