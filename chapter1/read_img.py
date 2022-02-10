import cv2

#load gambar
img = cv2.imread("resources/Lenna.png")

# menampilkan gambar
cv2.imshow("Hasil",img)

# tunggu 
cv2.waitKey(0)

