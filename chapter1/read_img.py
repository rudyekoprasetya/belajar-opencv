import cv2

#load gambar
img = cv2.imread("resources/lenna.png")

# menampilkan gambar
cv2.imshow("Hasil",img)

print(img.shape)

# tunggu 
cv2.waitKey(0)

