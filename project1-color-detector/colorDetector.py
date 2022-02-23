import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

#membuat window
def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT max", "HSV", 255, 255, empty)
cv2.createTrackbar("VAL min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL max", "HSV", 255, 255, empty)


while True:
    ret, frame=cam.read()

    #load gambar
    image = cv2.imread("color_detection.jpg")
    # convert HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE min","HSV")
    h_max = cv2.getTrackbarPos("HUE max","HSV")
    s_min = cv2.getTrackbarPos("SAT min","HSV")
    s_max = cv2.getTrackbarPos("SAT max","HSV")
    v_min = cv2.getTrackbarPos("VAL min","HSV")
    v_max = cv2.getTrackbarPos("VAL max","HSV")

    # array warna
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    print([lower, upper])
    #masking
    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    

    gabung = np.hstack((image,result))

    cv2.imshow("Color detection", gabung)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()