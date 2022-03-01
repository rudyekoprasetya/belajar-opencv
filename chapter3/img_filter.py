import cv2
import imutils

#load image
image = cv2.imread("resources/lenna.png")

#ubah ke grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#ubah ke binary image
_, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

#canny
canny = cv2.Canny(grayscale, 127, 255)

#tampilkan hasil
cv2.imshow("original",image)
cv2.imshow("grayscale",grayscale)
cv2.imshow("binary",binary)
cv2.imshow("canny",canny)

cv2.waitKey(0)