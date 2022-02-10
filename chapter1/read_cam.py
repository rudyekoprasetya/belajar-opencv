#import library openCV
import cv2

#load camera utama perangkat
cap = cv2.VideoCapture(0)

#merubah resolusi camera 640 x 480
cap.set(3,640)
cap.set(4,480)

#baca hasil
while True:
    ret, frame=cap.read()

    # menampilkan hasil ke jendela
    cv2.imshow("Camera",frame)

    # hentikan jika ditekan tombol Q di keyboard 
    if cv2.waitKey(1) == ord("q"):
        break

#hapus semua cache
cap.release()
cv2.destroyAllWindows()