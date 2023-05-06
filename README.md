# Selfservice-cashier

## Latar belakang
Pada project kali ini saya diposisikan sebagai rekan dari salah satu pemilik supermarket yang ingin membuat supermarketnya lebih efisien dengan adanya sistem kasir yang self-service. Tak hanya hal tersebut, tetapi sang pemilik supermarket meminta kepada saya untuk data-data yang diinput dapat otomatis masuk ke dalam database yang menggunakan RDBMS SQLITE

## Requirement / Objective untuk membuat program
### Alur program
Dalam memahami alur program, sang pemilik supermarket memiliki ekspektasi setidaknya ada 6 poin ketika user nya menjalankan program. Diantaranya:
1. Pengguna akan diminta untuk memasukkan nama dan otomatis akan tergenerate transaction ID
2. Setelah pengguna melakukan poin 1, akan disuguhkan untuk input detail belanjaan seperti nama barang, jumlah, dan harga
3. Setelah pengguna melakukan poin 2, akan diberikan opsi either input detail lagi atau tidak. Ketika pilih iya maka masuk ke poin ke dua dan kalau tidak akan disuguhkan 6 opsi diantarnya: Tambah barang, Update barang, Hapus barang, Tampilkan seluruh barang, Set ulang seluruh barang, Hitung total harga + Checkout
4. Selesai dan seharusnya pengguna bisa langsung hitung total harga + checkout

### Requirement dan penjelasan fungsi
Dalam menjalankan program sesuai alur di atas, maka dibutuhkan requirement atau fungsi apa saja yang perlu dibuat:
1. Tambah barang -> perlu dibuat fungsi yang menghubungkan ke fungsi add_item di file Modules
2. Update barang -> perlu dibuat fungsi yang menghubungkan ke fungsi untuk masing-masing kegunaan. Sebagai contoh untuk ganti nama barang bisa add fungsi ganti_nama di file Modules, dan lakukan hal yang serupa untuk kegunaan update barang lainnya
3. Hapus barang -> perlu dibuat fungsi yang menghubungkan ke fungsi hapus_barang di file Modules 
4. Tampilkan seluruh barang -> perlu dibuat fungsi yang menghubungkan ke fungsi total_belanja di file Modules
5. Set ulang seluruh barang -> perlu dibuat fungsi yang menghubungkan ke fungsi reset di file Modules
6. Hitung total harga + Checkout -> perlu dibuat fungsi yang menghubungkan ke fungsi hitung_total_harga

Jika disimpulkan kita perlu membuat 3 file utama
1. File cashier.py sebagai file py utama untuk menjalankan interface cashier
2. File Modules.py sebagai acuan modul yang ada di poin satu sampai enam pada penjelasan di atas yang fungsi2nya akan dipanggil dari cashier.py
3. db.py yang berfungsi untuk membuat database sehingga data yang diinput oleh pengguna akan otomatis terekap di database kita


## Penjelasan fungsi
### Fungsi "add_item" (menambahkan item)
1. Fungsi ini meminta pengguna untuk memasukkan nama barang, jumlah, dan harga
2. Kemudian, fungsi ini akan menghitung total harga dengan mengalikan jumlah dengan harga
3. Fungsi akan menambahkan item baru ke dalam daftar belanjaan dalam bentuk kamus (dictionary)
4. Fungsi juga akan mencetak pesan bahwa barang telah berhasil ditambahkan ke daftar belanjaan.
### Fungsi "ganti_nama" (mengganti nama barang)
1. Fungsi ini akan menampilkan daftar belanjaan dan meminta pengguna untuk memilih nomor item yang ingin diubah
2. Pengguna akan diminta untuk memasukkan nama item yang baru
3. Fungsi akan mengganti nama item yang dipilih dengan nama yang baru
4. Fungsi akan mencetak pesan bahwa item telah berhasil diperbarui dan menampilkan daftar belanjaan yang terbaru.
### Fungsi "ganti_harga" (mengganti harga barang)
1. Fungsi ini akan menampilkan daftar belanjaan dan meminta pengguna untuk memilih nomor item yang ingin diubah
2. Pengguna akan diminta untuk memasukkan harga baru untuk item yang dipilih
3. Fungsi akan mengganti harga item yang dipilih dengan harga yang baru
4. Fungsi akan mencetak pesan bahwa item telah berhasil diperbarui dan menampilkan daftar belanjaan yang terbaru.
### Fungsi "ganti_jumlah" (mengganti jumlah barang)
1. Fungsi ini akan menampilkan daftar belanjaan dan meminta pengguna untuk memilih nomor item yang ingin diubah
2. Pengguna akan diminta untuk memasukkan jumlah baru untuk item yang dipilih
3. Fungsi akan mengganti jumlah item yang dipilih dengan jumlah yang baru
4. Fungsi akan mencetak pesan bahwa item telah berhasil diperbarui dan menampilkan daftar belanjaan yang terbaru.
### Fungsi "hapus_barang" (menghapus barang dari daftar belanjaan)
1. Fungsi ini akan menampilkan daftar belanjaan dan meminta pengguna untuk memilih nomor item yang ingin dihapus
2. Fungsi akan menghapus item yang dipilih dari daftar belanjaan
3. Fungsi akan mencetak pesan bahwa item telah berhasil dihapus (jika item ditemukan) atau pesan kesalahan (jika item tidak ditemukan atau pengguna memasukkan nomor item yang tidak valid).
### Fungsi "tampilkan_belanjaan" (menampilkan seluruh daftar belanjaan)
1. Fungsi ini akan menampilkan seluruh daftar belanjaan dengan menggunakan modul tabulate dan termcolor.

## Test case
Untuk memudahkan dalam memahami programnya, saya sudah membuat test case yang dapat diakses gambarnya di file test case dengan list perintah di bawah:
1. Customer ingin menambahkan dua item baru menggunakan method add_item()
2. Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method hapus_barang() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi.
3. Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan.
4. Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method tampilkan_belanjaan()
