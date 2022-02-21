import cv2
import numpy as np
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

# buat trackbar
def empty(a):
    pass
cv2.namedWindow("parameter")
cv2.resizeWindow("parameter",640,240)
cv2.createTrackbar("threshold1","parameter",150,255,empty)
cv2.createTrackbar("threshold2","parameter",0,255,empty)

while True:
    ret, frame=cam.read()

    blur = cv2.GaussianBlur(frame, (7,7),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)
    #cari contour
    threshold1=cv2.getTrackbarPos("threshold1","parameter")
    threshold2=cv2.getTrackbarPos("threshold2","parameter")
    canny=cv2.Canny(gray,threshold1,threshold2)
    # dilasi
    dilated = cv2.dilate(canny, None, iterations=3)

    contours,_ = cv2.findContours(dilated, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        cv2.drawContours(frame, [contour], 0, (255, 0, 0), 4)
        # x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Camera",frame)
    cv2.imshow("Camera dilasi",dilated)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()