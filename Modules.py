import tabulate
import sqlite3
from termcolor import colored

# Semua barang belanjaan akan masuk ke list di bawah
list_belanja = []

def add_item():

    nama_barang = input("Mau beli apa nih? ")
    while nama_barang.isnumeric():
        print("Punten, sepertinya salah input")
        nama_barang = input("Beli apa? ")


    jumlah = input("Berapa banyak kak? ")
    while not jumlah.isdigit():
        print("Punten, sepertinya salah input")
        jumlah = input("Berapa banyak bos?")
    jumlah = int(jumlah)


    # Input harganya
    while True:
        try:
            harga = float(input("Harganya berapa? "))
            break
        except ValueError:
            print("Punten, sepertinya salah input")
            
    # generate new item number
    no_id = len(list_belanja) + 1

    # Hitung total haraganya
    total_harga = jumlah * harga

     # create dictionary to represent item and append to the shopping list
    list_belanja.append({
        'no': no_id,
        'name': nama_barang,
        'jumlah': jumlah,
        'harga': harga
    })

    # print a success message
    print(f"\nBarang berhasil ditambahkan.\n")

#2. Update barang

def ganti_nama():
    print(tabulate.tabulate(list_belanja, headers='keys'))
    while True:
        try:
            item_id = int(input("Pilih nomor barang yang ingin diupdate: "))
            break
        except ValueError:
            print(colored("Tolong pilih nomor yang sesuai", "red"))
    new_name = input("\nKetik nama item yang baru: \n")

    for item in list_belanja:
        if item['no'] == item_id:
            item['name'] = new_name
            break

    print(colored("\nMantap bos! sudah berhasil terupdate\n", "green"))
    print(tabulate.tabulate(list_belanja, headers='keys'))

def ganti_harga():
    print(tabulate.tabulate(list_belanja, headers='keys'))
    while True:
        try:
            item_id = int(input("\nPilih nomor barang yang ingin diupdate:"))
            break
        except ValueError:
            print(colored("\nTolong pilih nomor yang sesuai\n", "red"))
    while True:
        try:
            harga_baru = float(input("Ketikkan harga yang baru: "))
            break
        except ValueError:
            print(colored("\nTolong masukkan harga yang valid\n", "red"))

    for item in list_belanja:
        if item['no'] == item_id:
            item['harga'] = harga_baru
            break

    print(colored("\nMantap bos! sudah berhasil terupdate\n", "green"))
    print(tabulate.tabulate(list_belanja, headers='keys'))

def ganti_jumlah():
    print(tabulate.tabulate(list_belanja, headers='keys'))
    while True:
        try:
            item_id = int(input("Pilih nomor barang yang ingin diupdate: "))
            break
        except ValueError:
            print(colored("Tolong pilih nomor yang sesuai", "red"))
    
    while True:
        try:
            jumlah_baru = int(input("Ketikkan jumlah yang baru: "))
            break
        except ValueError:
            print(colored("\nTolong masukkan jumlah yang valid\n", "red"))

    for item in list_belanja:
        if item['no'] == item_id:
            item['jumlah'] = jumlah_baru
            break
        
    print(colored("\nMantap bos! sudah berhasil terupdate\n", "green"))
    print(tabulate.tabulate(list_belanja, headers='keys'))


#3. Hapus barang

import tabulate
from termcolor import colored

# Semua barang belanjaan akan masuk ke list di bawah
list_belanja = []

def hapus_barang():
    if not list_belanja:
        print(colored("Keranjang belanjamu masih kosong","red"))
    else:
        table = tabulate.tabulate(list_belanja, headers='keys', tablefmt='grid')
        print(table)
        inp_statement = input("\nMasukkan nomor item yang ingin dihapus (tekan '0' untuk batal): ")
        if inp_statement == "0":
            print(colored("Batal menghapus barang","green"))
        else:
            try:
                item_id = int(inp_statement)
                item_deleted = False
                for i, item in enumerate(list_belanja):
                    if item['no'] == item_id:
                        list_belanja.pop(i)
                        item_deleted = True
                        break
                if item_deleted:
                    print(colored("\nBarang berhasil dihapus. Berikut list barang terupdate\n","green"))
                    table = tabulate.tabulate(list_belanja, headers='keys', tablefmt='grid')
                    print(table)
                    print("\n")
                else:
                    print(colored("Tidak ada item dengan nomor tersebut","red"))
            except ValueError:
                print(colored("Tolong masukkan nomor item dengan benar","red"))


#4. Menampilkan seluruh list belanjaan

import subprocess

subprocess.check_call(['pip', 'install', 'rich'])


from rich.console import Console
from rich.table import Table

def total_belanja():
    if not list_belanja:
        print(colored("Keranjang belanjamu masih kosong","red"))
    else:
        table = Table(show_header=True, header_style="yellow")
        table.add_column("No.")
        table.add_column("Nama Barang")
        table.add_column("Harga")
        table.add_column("Jumlah")

        for i, item in enumerate(list_belanja):
            table.add_row(str(i+1), item.get("name"), str(item.get("harga")), str(item.get("jumlah")))
        console = Console()
        console.print(table)

# db insert
conn = sqlite3.connect("cashier.db")
cursor = conn.cursor()

sql_insert = f"""
  INSERT INTO transaction (no, Nama_Barang, Harga, Jumlah) VALUES
  (
    "{list_belanja[0]['no']}",
    "{list_belanja[1]['name']}",
    "{list_belanja[2]['harga']}",
    "{list_belanja[3]['jumlah']}"

    )
  """

cursor.execute(sql_insert)

conn.commit()

5. Set ulang seluruh barang

def reset():
    inp_statement = input("Apakah anda yakin untuk reset items? ketik 1 jika yakin, 0 jika membatalkan \n")

    if inp_statement == "1":
        list_belanja.clear()
        print(colored("Seluruh belanjaan anda berhasil terhapus","green"))
    else:
        print(colored("Seluruh belanjaan tidak jadi terhapus","green"))

#6. Hitung total harga

from colorama import Fore, Style
import locale

def hitung_total_harga():
    locale.setlocale(locale.LC_ALL, '') 
    total_harga = 0
    for item in list_belanja:
        total_harga += item['harga'] * item['jumlah']
    
    diskon = 0

    # hitung diskon berdasarkan total harga barang
    diskon = 0.1 if total_harga > 500000 else 0.08 if total_harga > 300000 else 0.05 if total_harga > 200000 else 0

    print(Fore.YELLOW + "YOUR SHOPPING CART\n" + Style.RESET_ALL)
    print(tabulate.tabulate(list_belanja, headers='keys', tablefmt='grid'))
    print("\n")

    jumlah_diskon = total_harga * diskon 
    harga_setelah_diskon = total_harga - jumlah_diskon 
    
    # format angka dengan pemisah ribuan
    total_harga_formatted = locale.currency(total_harga, grouping=True, symbol=False)
    jumlah_diskon_formatted = locale.currency(jumlah_diskon, grouping=True, symbol=False)
    harga_setelah_diskon_formatted = locale.currency(harga_setelah_diskon, grouping=True, symbol=False)

    # Menampilkan total harganya
    print(f"\nTotal harga: {Fore.GREEN}Rp. {total_harga_formatted}{Style.RESET_ALL}")
    print(f"\nDiskon (%): {Fore.RED}{diskon * 100}%{Style.RESET_ALL}")
    print(f"\nJumlah diskon: {Fore.GREEN}Rp. {jumlah_diskon_formatted}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Harga setelah diskon: Rp. {harga_setelah_diskon_formatted}{Style.RESET_ALL}\n")


