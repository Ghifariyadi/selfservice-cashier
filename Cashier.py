"""

Berikut merupakan sekumpulan kode untuk menjalankan self service cashier untuk suatu supermarket besar yang bernama indoapril
Seluruh code di bawah ini mengacu ke satu modul yang bernama Modules.py. Untuk kasus yang lebih kompleks saya sarankan menggunakan
modul terpisah per kategori fungsi



"""

#Import modul
import Modules

# import library warna biar makin cakep kayak mantan
from termcolor import colored

# Print header gaya jamet
print(colored("=" * 100, "green"))
print(colored("{:^100}".format("Indoapril cabang kemang"), "blue"))
print(colored("{:^100}".format("Selamat datang, selamat berbelanja"), "yellow"))
print(colored("=" * 100, "green"))

# Input nama dulu bosku
while True:
    name = input("Siapa namanya? ")
    if name.isalpha():
        break
    else:
        print("Punten sepertinya salah input")

# Buat transaksi ID berdasarkan cabang, tanggal, dan random int biar kalau ada kasus orang dihipnotis gampang trackingnya
from datetime import datetime
import random

import datetime

now = datetime.datetime.now()
date_str = now.strftime("%d%m")
time_str = now.strftime("%H%M")

id_transaksi = f"Indoapril-{date_str}-{time_str}-{random.randint(1000,9999)}"
print(f"\n   Nama         = {name}")
print(f"   ID Transaksi = {id_transaksi}")


# Tambah barang
print(colored("\nTambah barang\n", "green"))
tambah_barang = True
while tambah_barang:
    Modules.add_item()
    if input("\nAda lagi? (Pilih salah satu | ya/tidak): ") == "tidak":
        tambah_barang = False

# Menu
menu = True
while menu:
    print(colored("\nPilih salah satu\n", "green"))
    print("1. Tambah barang",
      "\n2. Update barang",
      "\n3. Hapus barang",
      "\n4. Tampilkan seluruh barang",
      "\n5. Set ulang seluruh barang",
      "\n6. Hitung total harga + Checkout")
    
    try:
        inp_code = int(input("\nInput kode yang diinginkan: "))
    except ValueError:
        print("Tolong input angka kode yang sesuai")
        continue

    if inp_code == 1:
        print(colored("Tambah barang\n","green"))
        tambah_lagi = True
        while tambah_lagi:
            Modules.add_item()
            if input("Ada lagi? (Pilih salah satu | ya/tidak): ") == "tidak":
                tambah_lagi = False

    elif inp_code == 2:
        update_menu = True
        while update_menu:
            print("\n1. Update nama barang")
            print("2. Update harga barang")
            print("3. Update jumlah barang")
            print("4. Kembali ke menu")

            try:
                opsi_update = int(input("\nPilih salah satu: "))
            except ValueError:
                print("\nTolong input yang sesuai\n")
                continue

            # Execute user's update choice
            if opsi_update == 1:
                Modules.ganti_nama()

            elif opsi_update == 2:
                Modules.ganti_harga()

            elif opsi_update == 3:
                Modules.ganti_jumlah()

            elif opsi_update == 4:
                update_menu = False

            else:
                print("Tolong input yang sesuai\n")

    elif inp_code == 3:
        while True:
            delete_choice = input("Apakah kamu yakin ingin menghapus barang? (ya/tidak): ")
            if delete_choice.lower() == 'ya':
                Modules.hapus_barang()
                break
            elif delete_choice.lower() == 'tidak':
                break
            else:
                print("Tolong pilih opsi yang sesuai\n")

    elif inp_code == 4:
        print(colored("\nBerikut seluruh barang yang anda beli\n","green"))
        Modules.total_belanja()

    elif inp_code == 5:
        Modules.reset()

    elif inp_code == 6:
        Modules.check_out()

    else:
        print("Masukkan kode yang benar")
        




