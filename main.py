import json
import os
from datetime import datetime

saldo = 0
riwayat = []
FILE_SALDO = "saldo.json"

def simpan_saldo():
    with open(FILE_SALDO, "w") as file:
        json.dump({"saldo": saldo, "riwayat": riwayat}, file)

def muat_saldo():
    global saldo, riwayat
    if os.path.exists(FILE_SALDO):
        with open(FILE_SALDO, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
            riwayat = data.get("riwayat", [])

def tambah_pemasukan():
    global saldo
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    riwayat.append({"tipe": "Pemasukan", "jumlah": jumlah, "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M")})
    simpan_saldo()
    print(f"Pemasukan sebesar {jumlah} berhasil ditambahkan!")
    print()

def tambah_pengeluaran():
    global saldo
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print(f"Peringatan! Saldo tidak cukup. Saldo Anda hanya Rp {saldo}")
    else:
        saldo = saldo - jumlah
        riwayat.append({"tipe": "Pengeluaran", "jumlah": jumlah, "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M")})
        simpan_saldo()
        print(f"Pengeluaran sebesar {jumlah} berhasil dikurangi!")
    print()

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo Anda saat ini: Rp {saldo:,}")
    print("=" * 30)
    print()

def lihat_laporan():
    print("=" * 50)
    print("LAPORAN PEMASUKAN DAN PENGELUARAN")
    print("=" * 50)
    
    total_pemasukan = sum([t["jumlah"] for t in riwayat if t["tipe"] == "Pemasukan"])
    total_pengeluaran = sum([t["jumlah"] for t in riwayat if t["tipe"] == "Pengeluaran"])
    
    print(f"Total Pemasukan: Rp {total_pemasukan:,}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:,}")
    print("-" * 50)
    print("\nRiwayat Transaksi:")
    
    if not riwayat:
        print("Belum ada transaksi")
    else:
        for i, t in enumerate(riwayat, 1):
            print(f"{i}. {t['tipe']:15} | Rp {t['jumlah']:>10,} | {t['tanggal']}")
    
    print("\n" + "=" * 50)
    print()

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

muat_saldo()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")