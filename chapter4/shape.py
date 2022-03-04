import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    # hasil = cv2.line(frame, (0,0), (640,480), (0,255,0), 3)

    # hasil = cv2.rectangle(frame,(320,240),(240,320),(0,255,0),3)

    # hasil = cv2.circle(frame, (320,240), 100, (0,0,255), 3)

    #Menempatkan text
    hasil = cv2.putText(frame, 'Rudy Eko Prasetya', (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)

    #menampilkan hasil
    cv2.imshow("hasil",frame)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
