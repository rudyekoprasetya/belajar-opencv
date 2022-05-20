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
- [Chapter 4 - Mengelola Citra Digital Bag 1](#mengelola-citra-digital-1)
- [Chapter 5 - Mengelola Citra Digital Bag 2](#mengelola-citra-digital-2)
- [Chapter 6 - Menyisipkan Objek ke Citra](#menyisipkan-objek)
- [Project 1 - Deteksi Warna Citra](#project-1-deteksi-warna-citra)
- [Project 2 - Deteksi Garis Tepi Citra](#project-2-deteksi-garis-tepi)
- [Project 3 - Deteksi Benda](#project-3-deteksi-benda)
- [Project 4 - Deteksi Wajah](#project-4-deteksi-wajah)
- [Tentang Penyusun](#tentang-penyusun)

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

Setelah itu untuk memulai menggunakannya. Buatlah suatu folder kerja, semisal **Documents/Belajar-openCV** dimana nantinya akan kita gunakan sebagai workspace atau letak semua file kita. 

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

Jika muncul versi yang diinstall semisal versi 4.5.x maka kita sudah berhasil melakukan installasi openCV.

Atau jika kita melakukan installasi menggunakan GUI, terlebih dahulu download installer opencv disini [https://sourceforge.net/projects/opencvlibrary/files/4.5.4/opencv-4.5.4-vc14_vc15.exe/download](https://sourceforge.net/projects/opencvlibrary/files/4.5.4/opencv-4.5.4-vc14_vc15.exe/download)

kemudian akan muncul tampilan installer seperti dibawah ini, kemudian klik **next**

![install1](https://learnopencv.com/wp-content/uploads/2020/12/Installer-Welcome-Screen.jpg)

kemudian pilih **I accept the agreement** kemudian pilih **next**

![install2](https://learnopencv.com/wp-content/uploads/2020/12/Installer-License.jpg)

selanjutnya kita diminta untuk menentukan lokasi installasi opencv, semisal kita install di drive C

![install3](https://learnopencv.com/wp-content/uploads/2020/12/Installer-Select-Destination.jpg)

Kemudian klik tombol **Install**

![install4](https://learnopencv.com/wp-content/uploads/2020/12/Installer-Install.jpg)

Tunggu sampai installasi selesai 

![finish](https://learnopencv.com/wp-content/uploads/2020/12/Installer-Installing.jpg)


Jika proses sudah selesai untuk ujicoba silahkan jalankan perintah dibawah ini untuk cek versi openCV yang terinstall pada terminal

```console
$ python3 -c "import cv2; print(cv2.__version__)"
```

bila di OS windows

```console
py -c "import cv2; print(cv2.__version__)"
```


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

Amatilah Maka akan muncul tampilan berikut

![baca image](https://i.ibb.co/wWxvzKh/Selection-009.png)

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

Amatilah hasilnya. Jika benar maka camera internal akan aktif seperti dibawah ini

![read cam](https://i.ibb.co/6NXFW9K/Selection-010.png)

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


## Mengelola Citra Digital 1
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

![translasi](https://i.ibb.co/W3DwzrX/Selection-011.png)

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

![rotasi](https://i.ibb.co/6gHJzq6/Selection-012.png)

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

![resize](https://i.ibb.co/FV4qJkB/Selection-013.png)

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

![crop](https://i.ibb.co/hWD0QRW/Selection-014.png)

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

## Mengelola Citra Digital 2
---

Pada bab ini kita akan belajar mengolah citra dengan merubah warnanya, *filtering*, atau ubah channel serta melakukan operasi-operasi citra dasar seperti *morfology*.

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

Pertama kita buat file baru dengan nama **img_filter.py**

```python
import cv2
import imutils

#load image
image = cv2.imread("resources/lenna.png")

#ubah ke grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#tampilkan hasil
cv2.imshow("original",image)
cv2.imshow("grayscale",grayscale)

cv2.waitKey(0)
```

coba jalankan file diatas dan amatilah hasilnya.

![grayscale](https://i.ibb.co/L1ZSs1y/Selection-015.png)

Code `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` digunakan untuk konversi image dari RGB (dalam hal ini opencv terbalik BGR) menjadi warna grayscale. 

Kemudian kita akan coba membuat gambar menjadi blur dengan Gaussian Filter. Gaussian filter adalah filter dengan nilai pembobotan untuk tiap pixel. Filter ini sangat baik digunakan untuk menghilangkan noise yang bersifat sebaran normal yang biasanya digunakan untuk gambar digital hasil proses kamera.

Silahkan ubah code diatas menjadi dibawah ini

```python
import cv2
import imutils

#load image
image = cv2.imread("resources/lenna.png")

#blur
blur = cv2.GaussianBlur(image,(5,5),1)

#tampilkan hasil
cv2.imshow("original",image)
cv2.imshow("blur",blur)

cv2.waitKey(0)
```

Coba jalankan dan cermati perbedaanya.

![blur](https://i.ibb.co/jfbNwqX/Selection-016.png)

untuk nilai `(5,5)` adalah nilai kernel. **Kernel** adalah matriks kecil yang digunakan untuk menerapkan efek seperti yang mungkin Anda temukan di Photoshop atau Gimp, seperti mengaburkan, mempertajam, menguraikan, atau mengembos sebuah gambar. untuk nilai terakhir yaitu 1 digunakan untuk standar deviasi dari matrik atau pixel.

selanjutnya kita akan mengkonversi gambar tersebut ke biner dengan menggunakan fungsi threshold. silahkan ubah code **img_filter.py** menjadi dibawah ini

```python
import cv2
import imutils

#load image
image = cv2.imread("resources/lenna.png")

#ubah ke grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#ubah ke binary image
_, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

#tampilkan hasil
cv2.imshow("original",image)
cv2.imshow("grayscale",grayscale)
cv2.imshow("binary",binary)

cv2.waitKey(0)
```
coba jalankan file diatas dan bandingkan hasilnya

![binary](https://i.ibb.co/7r5kzBJ/Selection-017.png)

**Thresholding** adalah proses mengubah citra berderajat keabuan menjadi citra biner atau hitam putih sehingga dapat diketahui daerah mana yang termasuk obyek dan background dari citra secara jelas. Citra hasil thresholding biasanya digunakan lebih lanjut untuk proses pengenalan obyek serta ekstraksi fitur.Yang pertama kita lakukan adalah sumber gambar yang akan diubah. **Ini harus gambar grayscale**. Kedua adalah nilai ambang (threshold) yang digunakan untuk mengklasifikasikan nilai-nilai pixel nilainya antara 0 s/d 255. Ketiga adalah maxVal yang mewakili nilai yang akan diberikan jika nilai piksel lebih dari atau kurang dari nilai ambang(0 s/d 255). Coba ubah-ubah parameternya agar sesuai dengan keinginan.

Selain threshold kita bisa menggunakan fungsi **canny** untuk merubah image ke binary dan mendeteksi garis tepinya. berikut adalah contohnya

```python
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
```

Coba jalankan ulang dan cermati perbedaanya.

![canny](https://i.ibb.co/54SfydH/Selection-018.png)

**Morfologi** digunakan untuk mengolah bentuk obyek dari citra biner untuk menghilangkan gangguan atau *noise*  yang tidak termasuk bagian dari obyek. Operasi ini digunakan untuk memperjelas obyek dan menghilangkan celah-celah yang ada dilingkungannya.

![morfology](https://itanurjanah.files.wordpress.com/2019/03/figure.jpg)

Buat file **morphology.py** dan tambahkan code dibawah ini 

```python
import cv2

img = cv2.imread("resources/lenna.png")

erosi = cv2.erode(img,kernel,iterations = 1)
dilasi = cv2.dilate(erosi,kernel,iterations = 1)
opening = cv2.morphologyEx(dilasi, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow("original", img)
cv2.imshow("erosi", erosi)
cv2.imshow("dilasi", dilasi)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

Coba jalankan dan cermati perbedaan masing-masing

operasi dilasi digunakan untuk menambahkan atau mempertebal pixel objek atau memperbesar ukuran objek. sedangkan erosi adalah kebalikannya, digunakan untuk menghapus pixel atau memperkecil ukuran objek. Sedangkan *opening* dan *closing* adalah operasi gabungan antara erosi dan dilasi.

## Menyisipkan Objek
---

Didalam OpenCV kita jua bisa menyisipkan objek lain dalam citra digital seperti garis atau bentuk dasar seperti persegi, lingkaran bahkan text.

Untuk praktikum silahkan buat folder kerja **chapter4** didalamnya buatlah file dengan nama **shape.py** dengan code dibawah ini

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    # menggambar garis diagonal berwarna hijau
    hasil = cv2.line(frame, (0,0), (640,480), (0,255,0), 3)

    #menampilkan hasil
    cv2.imshow("Hasil",hasil)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```
Coba jalankan code diatas dan cermati. 

![line](https://i.ibb.co/r3bPVHf/Selection-019.png)

code `cv2.line(frame, (0,0), (640,480), (0,255,0), 3)` digunakan untuk menggabar garis pada frame camera dimulai dari koordinat 0,0 s/d 640,480 dimana warnanya adalah hijau (0,255,0) dengan ketebalan garis 3.

Selanjutnya kita akan belajar membuat objek kotak. Ubahlah code diatas menjadi dibawah ini

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    # menggambar kotak ditengah gambar
    hasil = cv2.rectangle(frame,(320,240),(240,320),(0,255,0),3)

    #menampilkan hasil
    cv2.imshow("Hasil",hasil)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```
![kotak](https://i.ibb.co/715v0kC/Selection-020.png)

code `cv2.rectangle(frame,(320,240),(240,320),(0,255,0),3)` berfungsi untuk menggambar kotak pada koordinat 320,240 sd 240,320 dengan warna hijau (0,255,0) dengan ketebalan garis 3.

Selanjutnya kita akan belajar menyisipkan objek lingkaran. ubah code menjadi berikut ini

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    # menyisipkan objek lingkaran
    hasil = cv2.circle(frame, (320,240), 100, (0,0,255), 3)

    #menampilkan hasil
    cv2.imshow("Hasil",hasil)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```
Jika dijalankan maka akan muncul objek linkaran berwarna merah (0,0,255) pada koordinar (320,240) dengan radius 100 serta ketebalan garis 3 seperti dibawah ini

![lingkaran](https://i.ibb.co/Q7Vn2wQ/Selection-021.png)

Untuk menyisipkan text pada citra silahkan ubah code menjadi berikut ini

```python
import cv2
import imutils

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame=cam.read()

    #Menempatkan text
    hasil = cv2.putText(frame, 'Rudy Eko Prasetya', (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)

    #menampilkan hasil
    cv2.imshow("Hasil",hasil)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```
![text](https://i.ibb.co/Y2wk3HR/Selection-022.png)

Code `cv2.putText(frame, 'Rudy Eko Prasetya', (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)` digunakan untuk menuliskan text **Rudy Eko Prasetya** pada citra di koordinat (10,300) dengan tipe font *FONT_HERSHEY_SIMPLEX* dengan ukuran 2, warna hijau serta ketebalan tulisan 5. Silahkan ubah parameter diatas sesuai dengan keinginan anda.

selain fungsi sisipkan objek diatas ada beberapa code seperto `cv2.polygon`, `cv2.polyline` dan `cv2.ellipse` silahkan merujuk ke [https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html) untuk keterangan lebih lanjut.


## Project 1 Deteksi Warna Citra
---

Setelah belajar dasar-dasar pengolahan citra digital. Sekarang kita akan belajar beberapa project sederhana untuk opencv seperti aplikasi untuk deteksi warna 

Untuk memulai silahkan buat folder **project1** dengan struktur folder sebagai berikut ini

```console
BelajarOpenCV
|-chapter1
|-chapter2
|-chapter3
|-chapter4
|-project1
    |-resources
        |-color_detection.jpg
```

File gambar bisa anda download [disini](https://i.ibb.co/ZW78Yn8/color-detection.jpg)

Selanjutnya buatlah file baru dengan nama **colorDetection.py**

```python
import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

#membuat window
def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT max", "HSV", 255, 255, empty)
cv2.createTrackbar("VAL min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL max", "HSV", 255, 255, empty)


while True:
    ret, frame=cam.read()

    #load gambar
    image = cv2.imread("resources/color_detection.jpg")
    # convert HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE min","HSV")
    h_max = cv2.getTrackbarPos("HUE max","HSV")
    s_min = cv2.getTrackbarPos("SAT min","HSV")
    s_max = cv2.getTrackbarPos("SAT max","HSV")
    v_min = cv2.getTrackbarPos("VAL min","HSV")
    v_max = cv2.getTrackbarPos("VAL max","HSV")

    # array warna
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    print([lower, upper])
    #masking
    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    gabung = np.hstack((image,result))

    cv2.imshow("Color detection", gabung)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
```

Untuk penjelasan dari masing-masing code adalah sebagai berikut 

```python
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT max", "HSV", 255, 255, empty)
cv2.createTrackbar("VAL min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL max", "HSV", 255, 255, empty)
```

digunakan untuk membuat trackbar dimana fungsinya adalah untuk menentukan nilai HUE, SATURATION dan VALUE (HSV) dari warna yang akan kita filter. 

HSV mendefinisikan warna dalam terminologi Hue, Saturation dan Value. Keuntungan HSV adalah terdapat warna-warna yang sama dengan yang ditangkap oleh indra manusia. Sedangkan warna yang dibentuk model lain seperti RGB merupakan hasil campuran dari warna-warna primer.  

- **Hue** : menyatakan warna sebenarnya, seperti merah, violet, dan kuning dan digunakan menentukan kemerahan (redness), kehijauan (greeness), dsb.  
- **Saturation** : kadang disebut chroma, adalah kemurnian atau kekuatan warna.
- **Value** : kecerahan dari warna. Nilainya berkisar antara 0-100 %. Apabila nilainya 0 maka warnanya akan menjadi hitam, semakin besar nilai maka semakin cerah dan  muncul variasi-variasi baru dari warna tersebut.

Disini saya gunakan fungsi untuk camera agar setiap perubahan yang kita lakukan pada trackbar akan dijalankan secara real time dan kita load gambar **color_detection.jpg**

```python
while True:
    ret, frame=cam.read()

    #load gambar
    image = cv2.imread("resources/color_detection.jpg")
```

Selanjutnya gambar tersebut di konversi ke warna HSV `hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)`. Kemudian masing-masing nilai dari trackbar kita masukan dalam variable dan dimasukan dalam sebuah array untuk batas nilai atas dan bawah suatu warna. kemudia kita cetak hasilnya dalam Terminal. Hal ini bertujuan agar kita mengetahui range nilai suatu warna.


```python
h_min = cv2.getTrackbarPos("HUE min","HSV")
h_max = cv2.getTrackbarPos("HUE max","HSV")
s_min = cv2.getTrackbarPos("SAT min","HSV")
s_max = cv2.getTrackbarPos("SAT max","HSV")
v_min = cv2.getTrackbarPos("VAL min","HSV")
v_max = cv2.getTrackbarPos("VAL max","HSV")

# array warna
lower = np.array([h_min,s_min,v_min])
upper = np.array([h_max,s_max,v_max])
print([lower, upper])
```

Selanjutnya hasil dari array tersebut kita masking dan kita gabungkan dengan gambar untuk mendapatkan warna yang akan di filter

```python
#masking
mask = cv2.inRange(hsv,lower,upper)
result = cv2.bitwise_and(image, image, mask=mask)
```

Yang terakhir adalah memunculkan hasil gambar asli dan hasil filternya

```python
gabung = np.hstack((image,result))

cv2.imshow("Color detection", gabung)
```

Coba jalankan file diatas dan lakukan perubahan pada nilai HSV masing-masing. Lakukan filter sampai yang tersisa hanya warna merah seperti dibawah ini.

![red filter](https://i.ibb.co/tqjnwSz/red.jpg)

Amati hasil dari print arraynya. Bisa disimpulkan bahwa warna merah dari nilai HSVnya dari [0,150,0] sd [10,255,255]. Coba cari pula untuk warna biru

![blue filter](https://i.ibb.co/7SDF449/blue.jpg)

bisa dilihat kita dapati HSVnya adalah [90,150,0] sd [130,255,255]

Anda bisa bereksperimen untuk warna-warna lainnya seperti warna kuning dibawah ini

![yellow filter](https://i.ibb.co/x2LnYNx/yellow.jpg)

catatlah nilai HSV dari masing-masing filter warna yang sudah anda dapat ini.

Selanjutnya kita akan membuat camera yang bisa mendeteksi warna dari objek yang ada didepannya.

Silahkan buat file **color-cam.py** dengan code dibawah ini

```python
import cv2
import numpy as np

#load camera resolusi 640 x 480
cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

while True:
    ret, frame=cam.read()

    # convert HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #array warna merah
    low_red = np.array([0,150,0], np.uint8)
    up_red = np.array([10,255,255], np.uint8)
    #array warna biru
    low_blue = np.array([90,150,0], np.uint8)
    up_blue = np.array([130,255,255], np.uint8)
    #array warna hijau
    low_green = np.array([50,130,0], np.uint8)
    up_green = np.array([90,255,255], np.uint8)

    #masking merah
    mask_red = cv2.inRange(hsv,low_red,up_red)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

    #masking biru
    mask_blue = cv2.inRange(hsv,low_blue,up_blue)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    #masking hijaun
    mask_green = cv2.inRange(hsv,low_green,up_green)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    gabung1 = np.hstack((frame,res_red))
    gabung2 = np.hstack((res_green,res_blue))
    gabung = np.vstack((gabung1,gabung2))

    cv2.imshow("Camera Color Detection", gabung)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
```

Jika dijalankan maka sebagai berikut ini

![color detection](https://i.ibb.co/f9NvLLC/color-detect.jpg)

masing-masing warna akan dimasking sesuai dengan batas nilai array yang sudah ditentukan sehingga bisa ke filter sesuai dengan warna yang diinginkan.

Untuk Contoh project sederhana mengenai color detector dengan menggunakan camera. Silahkan buat file baru dengan nama **rgb_detector.py**

```python
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
```
Coba jalankan dan arahkan beberapa objek yang berwarna merah, biru dan hijaun satu persatu

![colordetect](https://i.ibb.co/QbnnVTN/Selection-025.png)

Maka secara otomatis camera akan mendeteksi dan menuliskan hasil pembacaan warnanya seperti dibawah ini

![colordetect](https://i.ibb.co/71g0kKZ/Selection-023.png)
 
## Project 2 Deteksi Garis Tepi
---

Kali ini kita membuat project untuk mendeteksi garis tepi dari citra. Dimana kita akan menghitung jumlah coin yang ada pada suatu gambar.

```console
BelajarOpenCV
|-chapter1
|-chapter2
|-chapter3
|-chapter4
|-project1
|-project2
    |-resources
        |-coin.jpg
```

File gambar bisa didownload [disini](https://images.unsplash.com/photo-1625806785652-f4427c3fda40?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Y29pbnxlbnwwfHwwfHw%3D&w=1000&q=80). Kemudian simpan dengan nama file **coin.jpg** simpan dalam folder resources.

Kemudian buatlah file **coinDetector.py**

```python
import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# buat trackbar
def empty(a):
    pass

cv2.namedWindow("parameter")
cv2.resizeWindow("parameter",640,240)
cv2.createTrackbar("threshold1","parameter",0,500,empty)
cv2.createTrackbar("threshold2","parameter",255,500,empty)

while True:
    ret, frame=cap.read()

    img = cv2.imread('resources/coin1.jpg')

    img = imutils.resize(img, width=300)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    threshold1=cv2.getTrackbarPos("threshold1","parameter")
    threshold2=cv2.getTrackbarPos("threshold2","parameter")
    canny = cv2.Canny(blur, threshold1, threshold2)

    dilasi = cv2.dilate(canny, (1,1), iterations=0)

    contour, _ = cv2.findContours(dilasi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.drawContours(color, contour, -1, (0, 255, 0), 2)

    cv2.imshow('Hasil',color)

    print("banyak coin adalah ", len(contour))

    if cv2.waitKey(1) == ord("q"):
        break 
```
 Coba Jalankan maka di console atau terminal akan mencul tulisan seperti ini

```console
banyak coin adalah 3
banyak coin adalah 3
banyak coin adalah 3
banyak coin adalah 3
```
dan memunculkan gambar coin dengan garis tepi hijau seperti dibawah ini

![Coin detector](https://i.ibb.co/3B3xgLn/Selection-027.png)

Penjelasan dari masing-masing code adalah sebagai berikut ini

```python
# buat trackbar
def empty(a):
    pass

cv2.namedWindow("parameter")
cv2.resizeWindow("parameter",640,240)
cv2.createTrackbar("threshold1","parameter",0,500,empty)
cv2.createTrackbar("threshold2","parameter",255,500,empty)
```

Code diatas digunakan untuk membuat trackball yang digunakan sebagai parameter untuk mencari garis tepi dari objek. Disini saya gunakan 2 parameter yaitu threshold1 dan threshhold2.

Disini saya gunakan fungsi untuk camera agar setiap perubahan yang kita lakukan pada trackbar akan dijalankan secara real time dan kita load gambar coin.

```python
while True:
    ret, frame=cam.read()

    #load gambar
    image = cv2.imread("resources/coin1.jpg")
```
Selanjutnya kita resize ukurannya, serta di konversi ke abu-abu dan diberikan filter gaussian blur.

```python
img = imutils.resize(img, width=300)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)
```





## Referensi
 
 - Computer Vision : Foundation and Application, Standford University
 - Ahmad, Usman. 2005. *Pengolahan Citra Digital dan Teknik Pemrograman*. Yogyakarta: Graha Ilmu.
 - [https://id.wikipedia.org/wiki/Piksel](https://id.wikipedia.org/wiki/Piksel)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/)
 - [https://id.wikipedia.org/wiki/OpenCV](https://id.wikipedia.org/wiki/OpenCV)
 - [https://learnopencv.com/install-opencv-on-windows/](https://learnopencv.com/install-opencv-on-windows/)
 - [https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/](https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/)
 - [https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/)
 - [https://iglab.tech/opencv-part-1-meng-load-dan-menampilkan-image/](https://iglab.tech/opencv-part-1-meng-load-dan-menampilkan-image/)
 - [https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv](https://stackoverflow.com/questions/4179220/capture-single-picture-with-opencv)
 - [https://itanurjanah.wordpress.com/2019/03/17/operasi-morfologi-menggunakan-opencv-python/](https://itanurjanah.wordpress.com/2019/03/17/operasi-morfologi-menggunakan-opencv-python/)
 - [https://www.ivanjul.com/tutorial-opencv-python-3-7-part-6-membuat-garis-line/](https://www.ivanjul.com/tutorial-opencv-python-3-7-part-6-membuat-garis-line/)
 - [https://www.ivanjul.com/tutorial-opencv-python-3-7-part-7-membuat-kotak-rectangle/](https://www.ivanjul.com/tutorial-opencv-python-3-7-part-7-membuat-kotak-rectangle/)
 - [https://www.ivanjul.com/tutorial-opencv-python-3-7-part-8-membuat-lingkaran-circle/](https://www.ivanjul.com/tutorial-opencv-python-3-7-part-8-membuat-lingkaran-circle/)
 - [https://www.ivanjul.com/tutorial-opencv-python-3-7-part-9-membuat-text/](https://www.ivanjul.com/tutorial-opencv-python-3-7-part-9-membuat-text/)
 - [http://www.kitainformatika.com/2015/01/ruang-warna-hue-saturation-value-hsv.html](http://www.kitainformatika.com/2015/01/ruang-warna-hue-saturation-value-hsv.html)

