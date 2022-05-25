import cv2

# load CascadeClassifier
cascade = cv2.CascadeClassifier("xml/frontal_face.xml")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:

    ret, frame=cap.read()

    # ubah ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # deteksi wajah
    face = cascade.detectMultiScale(gray, 1.1, 1)

     # berikan kotak pada tiap objek terdeteksi
    for (x,y,w,h) in face :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)

    #tampilkan video
    cv2.imshow('hasil', frame)   

    #berhenti
    if cv2.waitKey(1) == ord("q"):
        break 

cv2.destroyAllWindows()