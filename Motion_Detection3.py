import numpy as np
import cv2
import datetime
import time
import message2

cap=cv2.VideoCapture(0)
time.sleep(2)
fgbg=cv2.createBackgroundSubtractorMOG2()
count=0

while True:
    ret,frame = cap.read()
    text="UNOCCUPIED"
    fgmask= fgbg.apply(frame)
    gray = cv2.GaussianBlur(fgmask, (101, 101), 0)
    ret,thresh= cv2.threshold(gray,25,255,cv2.THRESH_BINARY)
    contours,hierarchy= cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if (len(contours)!=0 and count<20):
        if count>10 and count <20:
            imgname="screen{}.png".format(count-10)
            cv2.imwrite(imgname,frame)
        if count ==19:
            message2.message()
        count=count+1
    for cnt in contours:
        if cv2.contourArea(cnt) < 10000:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        text="OCCUPIED"
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow('Security Feed',frame)
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
