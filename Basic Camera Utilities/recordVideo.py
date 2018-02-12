import numpy as np
import cv2
import time

print("Press Q to exit..!!")
#cap=cv2.VideoCapture('output.mp4')
cap=cv2.VideoCapture(0) #Opens VideoCapture object i.e. opens a stream to camera

#Defining codec and creating VideoWriter Object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Output file name, fourcc parameters, frame per second(fcc), frame size
c = time.ctime()
out = cv2.VideoWriter('Video-'+str(c)+'.avi', fourcc, 30.0, (640,480))

while(cap.isOpened()):

    ret,frame=cap.read()
    if ret == True:
        #frame = cv2.flip(frame,0) #flips the frame vertically
        frame = cv2.flip(frame,90)  #flips the frame horizontly
        out.write(frame)            #writes the current frame to the output file
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):       # Press q to exit
            break
    else:
        break

#release everything when the job is done
cap.release()
out.release()
cv2.destroyAllWindows()
