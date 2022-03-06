import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

while True:
    ret, frame=cam.read()

    # convert HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #array warna merah
    low_red = np.array([0,150,0], np.uint8)
    up_red = np.array([10,255,255], np.uint8)
    #array warna biru
    low_blue = np.array([90,150,0], np.uint8)
    up_blue = np.array([130,255,255], np.uint8)
    #array warna hijau
    low_green = np.array([50,130,0], np.uint8)
    up_green = np.array([90,255,255], np.uint8)


    #masking merah
    mask_red = cv2.inRange(hsv,low_red,up_red)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    # print(type(res_red))

    #masking biru
    mask_blue = cv2.inRange(hsv,low_blue,up_blue)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    #masking hijaun
    mask_green = cv2.inRange(hsv,low_green,up_green)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    gabung1 = np.hstack((frame,res_red))
    gabung2 = np.hstack((res_green,res_blue))
    gabung = np.vstack((gabung1,gabung2))

    # cv2.imshow("Camera Color Detection", frame)
    cv2.imshow("Camera Color Detection", gabung)
    # cv2.imshow("Camera Blue", res_blue)
    # cv2.imshow("Camera Red", res_red)
    # cv2.imshow("Camera Green", res_green)


    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()