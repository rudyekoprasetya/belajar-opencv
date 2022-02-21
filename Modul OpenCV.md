# Modul Computer Vision Fundamental
---

Penyusun **Rudy Eko Prasetya, S.Kom** - Blog [https://rudyekoprasetya.wordpress.com](https://rudyekoprasetya.wordpress.com)


![OpenCV](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/1200px-OpenCV_Logo_with_text_svg_version.svg.png)

Modul ini disusun sebagai bahan belajar *Artificial Intellegence (AI)* khususnya *Computer Vision* untuk siswa SMA/K atau Mahasiswa menggunakan library OpenCV untuk membangun suatu aplikasi AI.

Modul ini dibuat berdasarkan dokumentasi resmi dari OpenCV versi 4.x yang dipersingkat agar mudah untuk dipraktekkan dan dipahami serta berbagai literatur penunjang untuk lebih memahami akan konsep. Sehingga jika menginginkan panduan lengkap bisa merujuk ke [https://docs.opencv.org/4.x/](https://docs.opencv.org/4.x/).

Modul ini menggunakan lisensi [Creative Common](https://creativecommons.org/licenses/by-sa/4.0/) dengan atribut NonKomersial-BerbagiRupa dimana Lisensi ini mengizinkan setiap orang untuk menggubah, memperbaiki, dan membuat ciptaan turunan bukan untuk kepentingan komersial, selama mereka mencantumkan kredit dan melisensikan ciptaan turunan dengan syarat yang serupa dengan ciptaan asli.

## Daftar Isi
---

- [Pengantar](#pengantar)
- [Chapter 1 - Konsep Gambar Digital](#konsep-gambar-digital)
- [Chapter 2 - Persiapan dan Installasi](#persiapan-dan-installasi)
- [Chapter 3 - Membaca Gambar, Video dan Camera](#membaca-gambar-dan-video)
- [Chapter 4 - Mengelola Citra Digital Bag 1](#mengelola-citra-digital)
- [Chapter 5 - Mengelola Citra Digital Bag 2](#mengelola-warna-citra)
- Chapter 6
- Chapter 7
- Chapter 8
- Chapter 9
- Chapter 10
- Tentang Penyusun

## Pengantar
---

**Computer Vision** merupakan salah satu studi yang saling berkaitan antara image processing serta Artificial Intelligence. Image processing berfungsi untuk melakukan processing pada gambar yang akan dianalisis sehingga lebih mudah untuk dikenali oleh model yang dikembangkan dengan menggunakan Artificial Intelligence. Dengan kata lain, image processing menyediakan input untuk model *Artificial Intelligence (AI)*.

Menurut buku *Computer Vision : Foundations and Application by Standford University* Computer vision adalah 

 > Computer vision is building algorithms that can understand the content
of images and use it for other applications.

secara sederhana Computer Vision disini menggunakan suatu algoritma agar komputer bisa memahami dan menjelaskan dari tiap gambar yang diproses.

![example CV](https://miro.medium.com/max/800/1*8gmgaAkFdI-9OHY5cA93xQ.png)

Pada dasarnya, beberapa tugas yang dapat diselesaikan menggunakan Computer Vision antara lain:

1. **Object Classification**: Mengklasifikasikan berbagai jenis objek dalam suatu gambar. Misalnya pada gambar Cat vs Dog maka Object Classification berfungsi untuk menandai Anjing dan menandai Kucing. Umumnya, penandaan dilakukan dengan menggunakan round box.
2. **Object Identification:** Melakukan deteksi jenis objek yang diharapkan dalam suatu image. Misalnya : mencari gambar anjing dari sebuah foto Cat vs Dog
3. **Object Verification**: Melakukan pengecekan apakah objek yang dimaksud benar-benar terdapat dalam image. Misalnya memastikan bahwa benar-benar terdapat gambar anjing pada foto Cat vs Dog.
4. **Object Detection**: Melakukan deteksi letak dari objek tertentu pada sebuah image. Untuk menandai letak dari sebuah objek, umumnya menggunakan round box
5. **Object Landmark Detection**: Melakukan deteksi key points dari sebuah object di dalam sebuah image.
6. **Object Segmentation**: Melakukan deteksi pixels dari sebuah image yang memuat objek tertentu
7. **Object Recognition**: Pada dasarnya, object recognition merupakan gabungan dari object detection and object classification.


## Konsep Gambar Digital
---

Pada dasarnya komputer melihat segala sesuatu atau data dalam bentuk numerikal. Baik itu text maupun gambar atau image. Image dalam komputer secara numerik disebut sebagai pixel.

Menurut [Wikipedia](https://id.wikipedia.org/wiki/Piksel) 

 > **Pixels** adalah unsur gambar atau representasi sebuah titik terkecil dalam sebuah gambar grafis yang dihitung per inci. Pixel sendiri berasal dari akronim bahasa Inggris *Picture Element* yang disingkat menjadi Pixel.

Untuk lebih detail perhatikan gambar dibawah ini

![image1](https://i.ibb.co/M167C8F/Selection-005.png)

Gambar diatas disusun berdasarkan nilai pixel yaitu angka 0 dan 1. Dimana gambar diatas tersusun atas 10 pixels panjang dan 10 pixels lebar. Pixels disini adalah jumlah kotak-kotak kecil yang menyusun gambar tersebut atau atau gambar itu disebut image 10x10 pixels. Semakin banyak pixels akan semakin rapat dan bagus gambarnya. Semisal ada suatu gambar yang tersusun atas 640 x 480 atau biasanya disebut kualitas VGA, adapula gambar HD dengan ukuran 1280 x 720 pixels.

![image2](https://i.ibb.co/BKryzKZ/Selection-006.png)

Gambar angka 3 diatas disebut sebagai Binary Image. **Binary Image** adalah gambar yang tersusun hanya warna putih (1) dan hitam (0) atau bisa disebut level 2. Untuk gambar hitam putih tau grayscale merupakan gambar level 16 atau 8 bit. Dimana warna penyusunannya dimulai dari 0(putih) sd 255(hitam). 

![image3](https://i.ibb.co/S5GDGn9/Selection-007.png)

selanjutnya perlu dipahami komputer membaca gambar berwarna *(colored image)* dan gambar hitam putih *(grayscale image)*. Sebuah gambar yang berwarna (colored image) akan memiliki 3 nilai untuk tiap pixelnya. Ketiga nilai tersebut disebut Channel yang melambangkan warna **Red, Green dan Blue (R,G,B)**. Artinya bahwa sebuah pixel pada gambar yang berwarna merupakan perpaduan dari warna Merah (Red), Hijau (Green) dan Biru (Blue). 

![image4](https://i.ibb.co/sVYhXQb/Selection-008.png)

Apabila sebuah colored image memiliki pixels 640 x 480 maka shape dari image tersebut adalah (640,480,3). Terdapat angka 3 karena menandakan konsep RGB (3 channel). Sedangkan apabila sebuah image gray scale dengan width x height = 640 x 480 maka shape dari image tersebut adalah (640,480,1).


## Persiapan dan Installasi
---

Pada pembahasan sebelumnya kita telah bahas mengenai konsep computer vision dan gambar digital. Pada pembahasan kali ini, kita akan melakukan implementasi konsep Computer Vision ke dalam aplikasi dengan bahasa Python. Implementasi tersebut menggunakan library **OpenCV**.

menurut [Wikipedia](https://id.wikipedia.org/wiki/OpenCV) *OpenCV (Open Source Computer Vision Library)* adalah

 > Sebuah pustaka perangkat lunak yang ditujukan untuk pengolahan citra dinamis secara real-time, yang dibuat oleh Intel, dan sekarang didukung oleh Willow Garage dan Itseez. Program ini bebas dan berada dalam naungan sumber terbuka dari lisensi BSD

OpenCV pertama kali diluncurkan secara resmi pada tahun 1999 oleh Inter Research sebagai lanjutan dari bagian proyek bertajuk aplikasi intensif berbasis CPU, r*eal-time ray tracing* dan tembok penampil 3D. 

Sebelum kita lanjut ke installasi OpenCV, Alangkah baiknya Anda belajar terlebih dahulu mengenai bahasa pemrograman Python. Hal ini dikarena OpenCV menggunakan bahasa python dalam operasinya. Silahkan merujuk ke [sini](https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/) untuk memahami dasar pemrograman bahasa python.

Hal-hal yang harus dipersiapkan sebelum belajar adalah

1. Install Python versi 3.x, silahkan download di [https://www.python.org/downloads/](https://www.python.org/downloads/) dan lakukan installasi pada sistem operasi anda
2. Install Code Editor bisa [Sublime-text](https://www.sublimetext.com/download) atau [VS Code](https://code.visualstudio.com/download)
3. Paham perintah dasar console / terminal / cmd. Silahkan merujuk [kesini](https://dev.to/kymiddleton/reference-guide-common-commands-for-terminal-6no)

Setelah itu untuk memulai menggunakan laravel. Buatlah suatu folder kerja, semisal **Documents/Belajar-openCV** dimana nantinya akan kita gunakan sebagai workspace atau letak semua file kita. 

Untuk cek apakah python sudah terinstall anda bisa membuka terminal, kemudian ketikan perintah

untuk windows
```console
py --version
```

untuk MacOS atau linux perintahnya 

```console
$ python --version
```

jika muncul versi python maka installasi sudah berhasil.

Selanjutnya kita akan lakukan install library openCV. Jalankan ini pada terminal

```console
pip install opencv-python
```

Tunggu sampai proses installasi selesai

Jika mengalami kegagalan installasi, atau error dibawah ini

```console
Step 12/24 : RUN pip install opencv-python opencv-contrib-python
 ---> Running in a0f746a23aed
Collecting opencv-python
  Downloading https://files.pythonhosted.org/packages/77/f5/49f034f8d109efcf9b7e98fbc051878b83b2f02a1c73f92bbd37f317288e/opencv-python-4.4.0.42.tar.gz (88.9MB)
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-cciracwm/opencv-python/setup.py", line 9, in <module>
        import skbuild
    ModuleNotFoundError: No module named 'skbuild'
```

biasanya butuh dilakukan upgrade pip. Jika mengalami hal diatas maka jalankan perintah dibawah ini

```console
pip install --upgrade pip
pip install opencv-python
```

Jika proses sudah selesai untuk ujicoba silahkan jalankan perintah dibawah ini untuk cek versi openCV yang terinstall pada terminal

```console
$ python3 -c "import cv2; print(cv2.__version__)"
```

bila di OS windows

```console
py -c "import cv2; print(cv2.__version__)"
```

Jika muncul versi yang diinstall semisal versi 4.5.5 maka kita sudah berhasil melakukan installasi openCV.


## Membaca Gambar dan Video
---

Setelah kita melakukan persiapan dan installasi semua kebutuhan, selanjutnya kita akan memulai praktikum untuk mengetahui bagaimana openCV membaca suatu gambar dan video baik itu file video atau dari camera/webcam.

Pertama kita buat folder kerja untuk menampung semua file project, misalkan di **Documents/BelajarOpenCV**, Kemudian silahkan buat folder **Chapter1** didalam folder kerja anda. Selanjutnya didalamnya kita buat folder **resources** untuk menampung file gambar atau video kita. Berikut struktur foldernya

```console
BelajarOpenCV
|-chapter1
    |-resources
        |-file_image.jpg
        |-file_video.mp4 
```

Anda bisa memasukan file gambar sesuai keinginan. Untuk format bisa JPG, PNG tau BMP. Sedangkan untuk file video usahakan formatnya MP4 dan durasinya jangan terlalu lama, semisal 5 detik itu sudah cukup.

Untuk belajar membaca file image. Pertama silahkan download file lenna.png di [sini](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png). Kemudian Masukan kedalam folder **resources**.

Kemudian buatlah file **read_img.py** didalam folder **chapter1** dengan code sebagai berikut 

```python
#import library openCV
import cv2

#load gambar
img = cv2.imread("resources/lenna.png")

# menampilkan gambar
cv2.imshow("Hasil",img)

#melihat banyak pixel dan channel gambar
print(img.shape)

# tunggu 
cv2.waitKey(0)
```

Kemudian buka terminal atau console, masuk kedalam folder chapter1 dan jalankan file read_img.py dengan perintah 

```console
py read_img.py
```

Amatilah jendela apa yang muncul. 

Code `imread("resources/lenna.png")` digunakan untuk membaca file gambar dari path atau komputer kita. Pastikan path atau jalur ke file tersebut tepat beserta nama filenya, contohnya adalah file gambar lenna.png ada didalam folder resources. Sedangkan code `imshow("Hasil",img)` digunakan untuk menampilkan hasil dalam suatu jendela dengan nama Windows *Hasil*. Untuk code `cv2.waitKey(0)` digunakan untuk menghentikan eksekusi sementara. `cv2.waitKey` menerima satu argumen integer yang berperan sebagai delay (dalam milisenconds) menampilkan frame hingga frame tersebut akan secara otomatis di-close. 

Selain itu di console atau terminal akan munculkan nilai `(512,512,3)` dalam hal ini berarti image tersebut memiliki dimensi 512 x 512 pixel dengan 3 channel.

Selanjutnya kita coba untuk menampilkan file video. Buatlah file **read_vid.py** didalam folder **chapter1**

```python
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
```

Jangan lupa masukan file video didalam folder resources. Coba jalankan file tersebut

```console
py read_video.py
```
Amatilah jendela yang muncul. Untuk menutup jendela video cukup dengan menekan **tombol Q** di keyboard. Ini sesuai dengan code ` if cv2.waitKey(1) == ord("q"):`

Kita juga bisa mengambil gambar dari web cam atau camera yang ada didalam komputer/laptop kita. Untuk ujicoba silahkan buat file baru **read_cam.py** di folder **chapter1**

```python
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
```

Jalankan file diatas dengan perintah

```console
py read_cam.py
```

Amatilah hasilnya. 

Code `cap.set(3,640)` dan `cap.set(4,480)` digunakan untuk merubah resolusi camera yang ditampilkan. kemudian hasilnya ditampilkan dengan code `cv.imshow("camera",frame)`.  Untuk menghapus cache file menggunakan code `cap.release()` dan `cv2.destroyAllWindows()`. Untuk menutup jendela tekan tombol Q.

Untuk mengambil gambar dari camera kita buat file **take_pic.py**

```python
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

    # ambil gambar saat ditekan tombol Y di keyboard 
    if cv2.waitKey(1) == ord("y"):
        #simpan frame yang aktif di folder resources dengan nama pic1.png
        cv2.imwrite('resources/pic1.png',frame)
        break
    
#hapus semua cache
cap.release()
cv2.destroyAllWindows()
```

Coba jalankan code diatas dan amatilah.

pada code `cv2.imwrite('resources/pic1.png',frame)` berfungsi untuk menyimpan frame yang aktif dari camera dan disimpan dalam folder **resources** dengan nama file **pic1.png**.  Itu semua akan dijalankan saat ditekan tombol Y.


## Mengelola Citra Digital
---

Setelah kita bisa memuat gambar dan video, baik dalam bentuk file maupun dari camera. Sekarang kita akan belajar bagaimana mengelolanya dengan openCV.

Silahkan buat folder **chapter2** pada folder kerja kita. Kemudian kita copykan folder resources yang ada pada chapter1 kedalam folder chapter2, sehingga strukturnya seperti dibawah ini

```console
BelajarOpenCV
|-chapter1
|-chapter2
    |-resources
        |-lenna.png
        |-video.mp4 
```

Pertama kita akan praktikum memanipulasi gambar, sebelum itu kita install paket **imutils**. Sedangkan imutils adalah library untuk pemrosesan gambar dasar seperti translasi, rotasi, pengubahan ukuran.

Untuk install jalankan perintah

```console
pip install imutils
```
selanjutnya buatlah file baru dengan nama **img_translate.py** dengan coding dibawah ini

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#tranlasi
x, y = 150, 50 #geser sumbu X sebesar 150 sumbu Y sebesar 50
img_trans = imutils.translate(img, x, y)
cv2.imshow('gambar translasi', img_trans)
cv2.waitKey(0)
```

coba jalankan file tersebut, dan amatilah yang terjadi.

Pada dasarnya translasi digunakan untuk mengeser gambar ke suatu koordinat tertentu, hal ini bisa dilihat pada code `imutils.translate(img, x, y)` nilai X positif akan menggeser image ke kanan sedangkan nilai y positif akan menggeser image ke bawah. Dalam hal ini berlaku untuk kebalikannya.

Coba ubahlah kode diatas menjadi dibawah ini

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#tranlasi
x, y = -150, 50 #geser sumbu X sebesar 150 sumbu Y sebesar 50
img_trans = imutils.translate(img, x, y)
cv2.imshow('gambar translasi', img_trans)
cv2.waitKey(0)
```
Jalankan dan amatilah hasilnya.

Kita akan belajar memutar citra. Silahkan buat file baru **img_rotate.py**

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#rotasi kekiri 90 derajat
angle = 90

img_rotate = imutils.rotate(img, angle)
cv2.imshow('gambar rotasi', img_rotate)
cv2.waitKey(0)
```

Jalankan file tersebut dan amatilah perbedaanya.

fungsi `imutils.rotate(img, angle)` digunakan untuk memutar citra dengan sudut derajat tertentu. untuk nilai positif objek akan diputar berlawanan arah jarum jam. Untuk negatif objek akan diputar searah jarum jam.  

operasi ini bisa pula digunakan untuk camera, coba buatlah file **cam_rotate.py** dengan code berikut

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    #tampilkan camera normal
    cv2.imshow("Camera Asli",frame)
    
    #tampilkan camera rotasi 90 derajat
    angle = 90
    frame_rotate = imutils.rotate(frame,angle)
    cv2.imshow("Camera rotasi",frame_rotate)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```

Jalankan dan cermatilah hasilnya. Untuk keluar tekan tombol Q

Selanjutnya kita akan belajar untuk merubah ukuran atau resize citra. silahkan buat file **img_resize.py**

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#resize ukuran panjang 150 lebar 150
w, h = 150, 150

img_resize = cv2.resize(img, (w,h), interpolation=cv2.INTER_AREA)
cv2.imshow('gambar resize', img_resize)

cv2.waitKey(0)
```

Coba jalankan dan bandingkan hasilnya dengan gambar asli.

kita bisa jua menggunakan imutils agar aspect ratio saat resize sesuai. Coba ubahlah coding diatas menjadi dibawah ini

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#resize ukuran panjang 150 lebar 150
w, h = 150, 150

img_resize = imutils.resize(img, width=w)
cv2.imshow('gambar resize', img_resize)

cv2.waitKey(0)
```
Kita cukup mendefinisikan salah satu ukuran saja baik width atau height saja.

Selanjutnya kita akan mencoba untuk flip atau membalik citra. Silahkan buat file **img_flip.py**

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#flip horisontal
flip_hor = cv2.flip(img, 1)
#flip vertikal
flip_ver = cv2.flip(img, 0)
#flip vertikal dan horisontal
flip_verhor = cv2.flip(img, -1)
cv2.imshow('Flip horisontal', flip_hor)
cv2.imshow('Flip vertikal', flip_ver)
cv2.imshow('Flip vertikal dan horisontal', flip_verhor)

cv2.waitKey(0)
```

Coba jalankan dan bandingkan hasilnya dengan gambar aslinya.

kita coba pula lakukan operasi ini pada camera, semisal kita mau lakukan file vertikal atau buat mirro camera kita. Buatlah file **cam_flip.py**

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    #tampilkan camera normal
    cv2.imshow("Camera Asli",frame)

    #buat mirror
    frame_mirror = cv2.flip(frame, 1)
    cv2.imshow("Camera mirror",frame_mirror)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```
Coba jalankan dan perhatikan hasilnya. tekan tombol Q untuk menutup jendela kamera.

Kemudian buatlah file **img_crop.py** untuk belajar cropping image

```python
import cv2
import imutils 

img = cv2.imread('resources/lenna.png')
cv2.imshow('gambar asli',img)

#cropping image dari pixel 48 s/d 255 dan pixel 90 s/d 240
img_crop = img[48:255, 90:240]

cv2.imshow('gambar crop',img_crop)

cv2.waitKey(0)
```
Coba jalankan dan bandingkan hasilnya dengan gambar aslinya.

Terakhir kita akan coba menggabungkan beberapa citra menjadi satu. disini kita akan menggunakan *library numpy*. 

**NumPy** adalah sebuah library pada Python yang berfungsi untuk melakukan operasi vektor dan matriks dengan mengolah array dan array multidimensi. Biasanya NumPy digunakan untuk kebutuhan dalam menganalisis data. Kita tahu bahwa citra adalah kumpulan array sehingga numpy bisa membantu untuk mengelolanya.

silahkan buat file **img_gabung.py** dengan code berikut

```python
import cv2
import numpy as np

img = cv2.imread('resources/lenna.png')

#flip image
flip_hor = cv2.flip(img, 1)
flip_ver = cv2.flip(img, 0)

#gabungkan gambar horizontal
gabung_hor = np.hstack((img,flip_hor,flip_ver))

#gabungkan gambar vertital
gabung_ver = np.vstack((img,flip_hor,flip_ver))

cv2.imshow('gabung horizontal',gabung_hor)
cv2.imshow('gabung vertikal',gabung_ver)

cv2.waitKey(0)
```

Coba jalankan code diatas dan amati hasilnya.

Kita coba pula dengan camera. Buatlah file **cam_gabung.py**

```python
import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    #buat mirror
    frame_mirror = cv2.flip(frame, 1)

    #gabung camera
    gabung = np.hstack((frame,frame_mirror))
    # cv2.imshow("Camera mirror",frame_mirror)
    cv2.imshow("Camera gabung",gabung)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```

Coba jalankan code diatas dan amati hasilnya.

## Mengelola Warna Citra
---

Pada bab ini kita akan belajar mengolah citra dengan merubah warnanya, atau mengkonversinya serta melakukan operasi-operasi citra dasar seperti morfology.

Silahkan buat folder **chapter3** pada folder kerja kita. Kemudian kita copykan folder *resources* yang ada pada chapter1 kedalam folder chapter2, sehingga strukturnya seperti dibawah ini

```console
BelajarOpenCV
|-chapter1
|-chapter2
|-chapter3
    |-resources
        |-lenna.png
        |-video.mp4 
```



## Referensi
 
 - Computer Vision : Foundation and Application, Standford University
 - [https://id.wikipedia.org/wiki/Piksel](https://id.wikipedia.org/wiki/Piksel)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/)
 - [https://id.wikipedia.org/wiki/OpenCV](https://id.wikipedia.org/wiki/OpenCV)
 - [https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/](https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/)
 - [https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/)
 - [https://iglab.tech/opencv-part-1-meng-load-dan-menampilkan-image/](https://iglab.tech/opencv-part-1-meng-load-dan-menampilkan-image/)
 - [https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv](https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv)

