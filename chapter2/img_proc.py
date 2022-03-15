import cv2
import imutils 
import numpy as np

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

# tranlasi
# x, y = 150, 50 #geser sumbu X sebesar 150 sumbu Y sebesar 50
# img_trans = imutils.translate(img, x, y)
# cv2.imshow('gambar translasi', img_trans)

#rotasi kekiri 90 derajat
# angle = 90

# img_rotate = imutils.rotate(img, angle)
# cv2.imshow('gambar rotasi', img_rotate)

#resize ukuran panjang 150 lebar 150
# w, h = 150, 150

# # img_resize = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
# img_resize = imutils.resize(img, width=w)
# cv2.imshow('gambar resize', img_resize)

#flip
# flip_hor = cv2.flip(img, 1)
# flip_ver = cv2.flip(img, 0)
# flip_verhor = cv2.flip(img, -1)
# cv2.imshow('Flip horisontal', flip_hor)
# cv2.imshow('Flip vertikal', flip_ver)
# cv2.imshow('Flip vertikal dan horisontal', flip_verhor)

#gabungkan gambar horizontal
# gabung_hor = np.hstack((img,flip_hor,flip_ver))
# gabung_ver = np.vstack((img,flip_hor,flip_ver))
# cv2.imshow('gabung horizontal',gabung_hor)
# cv2.imshow('gabung vertikal',gabung_ver)

#cropping
# img_crop = img[48:255, 90:240]

# cv2.imshow('gambar crop',img_crop)

cv2.waitKey(0)