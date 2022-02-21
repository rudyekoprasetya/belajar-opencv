import cv2
import numpy as np
import os

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame1=cam.read()
    ret, frame2=cam.read()
    # diff
    diff = cv2.absdiff(frame1,frame2)
    # ubah ke grayscale
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    # blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    # threshold
    _, thres = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # dilasi
    dilated = cv2.dilate(thres, None, iterations=3)
    #batas
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        # gambar persegi
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
       
        

    cv2.imshow("Camera",frame1)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()