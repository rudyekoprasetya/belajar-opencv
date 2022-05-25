import cv2

# load VideoCapture
cap = cv2.VideoCapture("resources/video1.avi")
# load cascade 
car_cascade = cv2.CascadeClassifier("xml/cars.xml")

while True:

    ret, frame=cap.read()
    
    # ubah ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # deteksi mobil
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    awal = 0
    # berikan kotak pada tiap objek terdeteksi
    for (x,y,w,h) in cars :
        awal+=1
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)

    #tampilkan video
    cv2.imshow('hasil', frame)    
    print('banyak kendaraan adalah ', awal)
    #berhenti
    if cv2.waitKey(1) == ord("q"):
        break 

cv2.destroyAllWindows()