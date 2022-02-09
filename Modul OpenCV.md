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
- [Chapter 3 - Membaca Gambar dan Video](#membaca-gambar-dan-video)
- Chapter 4
- Chapter 5
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

Menurut Wikipedia

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

Selanjutnya kita akan lakukan install library openCV. Untuk OS Windows silahkan download kemudian instal
l openCV [https://sourceforge.net/projects/opencvlibrary/files/4.5.5/opencv-4.5.5-vc14_vc15.exe/download](https://sourceforge.net/projects/opencvlibrary/files/4.5.5/opencv-4.5.5-vc14_vc15.exe/download).

Untuk OS Linux seperti ubuntu dkk silahkan jalankan perintah berikut pada terminal

```console
$ sudo apt install libopencv-dev python3-opencv
```
Tunggu sampai proses installasi selesai

Jika proses sudah selesai untuk ujicoba silahkan jalankan perintah dibawah ini untuk cek versi openCV yang terinstall pada terminal

```console
$ python3 -c "import cv2; print(cv2.__version__)"
```

bila di windows

```console
py -c "import cv2; print(cv2.__version__)"
```

Jika muncul versi yang diinstall semisal versi 4.5.5 maka kita sudah berhasil melakukan installasi openCV.


## Membaca Gambar dan Video
---










## Referensi
 
 - Computer Vision : Foundation and Application, Standford University
 - [https://id.wikipedia.org/wiki/Piksel](https://id.wikipedia.org/wiki/Piksel)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-1/)
 - [https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/](https://iglab.tech/mengenal-konsep-dasar-computer-vision-part-2/)
 - [https://id.wikipedia.org/wiki/OpenCV](https://id.wikipedia.org/wiki/OpenCV)
 - [https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/](https://rudyekoprasetya.wordpress.com/2021/08/14/kenapa-aku-belajar-python/)
 - [https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/)

