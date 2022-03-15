import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

while True:
    ret, frame=cam.read()

    

    # setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]
  
    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    warna = ''

    if (b_mean > g_mean and b_mean > r_mean):
        warna = 'BIRU'
        cv2.putText(frame, warna, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    elif (g_mean > r_mean and g_mean > b_mean):
        warna = 'HIJAU'
        cv2.putText(frame, warna, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    else:
        warna = 'MERAH'
        cv2.putText(frame, warna, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)


    
    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()