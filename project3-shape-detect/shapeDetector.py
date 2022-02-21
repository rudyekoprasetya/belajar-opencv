import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# buat trackbar
def empty(a):
    pass

cv2.namedWindow("parameter")
cv2.resizeWindow("parameter",640,240)
cv2.createTrackbar("threshold1","parameter",150,255,empty)
cv2.createTrackbar("threshold2","parameter",255,255,empty)

while True:
    ret, frame=cap.read()

    # load image dan resize
    image=cv2.imread('shapes-image.jpg')
    img = imutils.resize(image, width=480)
    #jadikan blur
    blur=cv2.GaussianBlur(img,(5,5),1)
    #jadikan grayscale
    gray=cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    #cari contour
    threshold1=cv2.getTrackbarPos("threshold1","parameter")
    threshold2=cv2.getTrackbarPos("threshold2","parameter")
    canny=cv2.Canny(gray,threshold1,threshold2)

    contours,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
    
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        # print(len(approx))

        cv2.drawContours(img, [contour], 0, (255, 0, 0), 5)

        #cari tengah shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

        if len(approx) == 3:
            cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)  
        elif len(approx) == 4:
            cv2.putText(img, 'rectangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)    
        elif len(approx) == 5:
            cv2.putText(img, 'Pentagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)    
        elif len(approx) == 6:
            cv2.putText(img, 'Hexagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)    
        else:
            cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
    

    cv2.imshow("original",img)
    # cv2.imshow("gray",gray)
    cv2.imshow("canny",canny)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()