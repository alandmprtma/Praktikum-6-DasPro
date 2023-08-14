# Praktikum-6-DasPro
Praktikum 6 Dasar Pemrograman Institut Teknologi Bandung yang menggunakan bahasa Python dengan mempelajari mengolah data dengan file eksternal.
## Soal 1
Bu Roro Jonggrang memiliki satu buah file yang memiliki dua baris kata kata. Setiap kata di tiap baris dipisahkan oleh spasi. Ia ingin mengetahui kata apa saja yang muncul di kedua file, beserta jumlahnya di masing - masing file. Apabila tidak terdapat kata - kata yang sama, maka cetak “Tidak ada kata yang sama”. Bantulah Bu Roro Jonggrang untuk menyelesaikan permasalahan ini. Nama file program Anda harus main.py.

Note: Gunakan file tester.py untuk menyelesaikan persoalan ini

Cara penggunaan modul tester adalah sebagai berikut (silahkan di-copy)

import tester
tester.start("input.txt")
file = open("input.txt", "r")
#Tulis program kalian disini
tester.end("input.txt")
Tidak diperkenankan menggunakan dictionary
## Soal 2
Pak Bondowoso memiliki banyak jin dalam pasukannya dan ia ingin mengurutkan jin - jin tersebut berdasarkan namanya secara leksikografis dari kecil ke besar. Artinya huruf a akan berada di atas huruf b. Apabila terdapat “Asep” dan “AsepSamsul”, maka “Asep” akan berada di atas “AsepSamsul”. Bantulah Pak Bondowoso untuk membuat program daftar nama ini. Daftar nama jin berada di sebuah file dan output dari program dituliskan ke file lain (tidak diperlukan newline di akhir file yang ditulis). Nama file program Anda harus main.py.


Note: Gunakan file tester.py untuk menyelesaikan persoalan ini

Cara penggunaan modul tester adalah sebagai berikut (silahkan di-copy)

import tester
tester.start("input.txt")
fileIn = open("input.txt", "r")
fileOut = open("output.txt", "w")
#Tulis program kalian disini
tester.end("output.txt")
Tidak diperkenankan menggunakan .sort(), tetapi boleh menggunakan string comparison ("a" < "b")
## Soal 3
Seorang Jin menemukan skematik bangunan candi dalam bentuk matriks. Akan tetapi, untuk menemukan rumus candi yang tepat, ia memerlukan hasil penjumlahan semua elemen di dalam matriks. Bantulah jin ini untuk mendapatkan rumus candi. Asumsikan bahwa ukuran matriks selalu nxn (baris dan kolom berukuran sama). Nama file program Anda harus main.py.

Note: Gunakan file tester.py untuk menyelesaikan persoalan ini

Cara penggunaan modul tester adalah sebagai berikut (silahkan di-copy)

import tester
tester.start("input.txt")
file = open("input.txt", "r")
#Tulis program kalian disini
tester.end("input.txt")
## Soal 4
Bandung Bondowoso mencatat seluruh candi yang dibuat oleh 10 jin-nya pada file input.txt dengan format csv, yaitu dengan header kolom dan , (koma) sebagai pemisah antar datanya. Jin terajin adalah jin yang membangun candi paling banyak. Bantu bandung bondowoso mencari jumlah candi yang dibangun oleh jin terajin ke-3 dari data tersebut! Nama file program Anda harus main.py.

Note: Gunakan file tester.py untuk menyelesaikan persoalan ini

Cara penggunaan modul tester adalah sebagai berikut (silahkan di-copy)

import tester
tester.start("input.txt")
file = open("input.txt", "r")
#Tulis program kalian disini
tester.end("input.txt")
