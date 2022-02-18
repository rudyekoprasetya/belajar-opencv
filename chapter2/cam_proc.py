import cv2
import imutils
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

while True:
    ret, frame=cam.read()

    #tampilkan camera normal
    # cv2.imshow("Camera",frame)
    
    #tampilkan camera rotasi 90 derajat
    # angle = 90
    # frame_rotate = imutils.rotate(frame,angle)
    # cv2.imshow("Camera rotasi",frame_rotate)

    #buat mirror
    frame_mirror = cv2.flip(frame, 1)

    #gabung camera
    gabung = np.hstack((frame,frame_mirror))
    gabung4 = np.vstack((gabung,gabung))
    # cv2.imshow("Camera mirror",frame_mirror)
    cv2.imshow("Camera gabung",gabung4)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()