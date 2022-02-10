#import library openCV
import cv2

#load file video
cap = cv2.VideoCapture("resources/video.mp4")

#baca hasil video
while True:
    success, video=cap.read()

    # menampilkan video ke jendela
    cv2.imshow("Video",video)

    # hentikan jika ditekan tombol Q di keyboard 
    if cv2.waitKey(1) == ord("q"):
        break