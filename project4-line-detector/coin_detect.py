import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# buat trackbar
def empty(a):
    pass

cv2.namedWindow("parameter")
cv2.resizeWindow("parameter",640,240)
cv2.createTrackbar("threshold1","parameter",150,500,empty)
cv2.createTrackbar("threshold2","parameter",255,500,empty)

while True:
    ret, frame=cap.read()

    img = cv2.imread('resources/coin1.jpg')

    img = imutils.resize(img, width=600)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    threshold1=cv2.getTrackbarPos("threshold1","parameter")
    threshold2=cv2.getTrackbarPos("threshold2","parameter")
    canny = cv2.Canny(blur, threshold1, threshold2)

    dilasi = cv2.dilate(canny, (1,1), iterations=0)

    contour, _ = cv2.findContours(dilasi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.drawContours(color, contour, -1, (0, 255, 0), 2)

    cv2.imshow('Hasil',color)

    print("banyak coin adalah ", len(contour))

    if cv2.waitKey(1) == ord("q"):
        break 