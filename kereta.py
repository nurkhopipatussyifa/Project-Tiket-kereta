import os
import platform
import random

########################################################################
#############   SISTEM FUNCTION TIKET : List menu dll.  ################
########################################################################

# Function Membersihkan Terminal
def clearTerminal():
    # Untuk sistem Windows
    if platform.system() == "Windows" or platform.system() == "Win":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')

# Function list menu
def list_menu():
    print("=" * 36)
    print("Aplikasi Pesan Tiket Stasiun Sudirman")
    print("-" * 36)
    print("1. Pilih Kota Tujuan")
    print("2. Batalkan Tiket")
    print("3. Layanan Pelanggan")
    print("4. Keluar Aplikasi")
    print("-" * 36)

# Function List Kota
def list_kota():
    print("=" * 36)
    print("Daftar Tujuan Kota Tersedia")
    print("-" * 36)
    print("1. Bandung")
    print("2. Malang")
    print("3. Garut")

# Function untuk menyimpan data tiket
tiket_terpesan = {}

# Function Pemesanan Tiket
def pemesanan():
    global namaKereta, pilihan_kota, harga_tiket, jam_keberangkatan, tiket_terpesan

    print("-" * 36)
    print("Mengisi Data Pemesanan")
    print("-" * 36)

    # Masukan Jam Keberangkatan
    print("Jam Keberangkatan Tersedia:")
    for i, jam in enumerate(jam_keberangkatan, start=1):
        print(f"{i}. {jam}")
    
    pilihan_jam = int(input("Pilih Jam Keberangkatan (nomor): "))
    jam_terpilih = jam_keberangkatan[pilihan_jam - 1]

    # Masukan Jumlah Tiket
    beli_tiket = int(input("Masukan Jumlah Tiket: "))

    # List atau Array menampung jumlah pemesan Tiket
    list_penumpang = []

    # Masukan nama dan nomor KTP penumpang
    for urutanPemesan in range(beli_tiket):
        namaPemesan = input(f"> Masukan Nama Pemesan ke {urutanPemesan + 1}: ")
        nomor_ktp = input(f"> Masukan Nomor KTP Pemesan ke {urutanPemesan + 1}: ")
        list_penumpang.append({'nama': namaPemesan, 'ktp': nomor_ktp})

    # Bersihkan Terminal
    clearTerminal()

    # Hitung total harga tiket
    total_harga_tiket = beli_tiket * harga_tiket

    # Generate kode pemesanan
    kode_pemesanan = random.randint(1000, 9999)
    
    # Simpan data tiket
    tiket_terpesan[kode_pemesanan] = {
        'kereta': namaKereta,
        'kota': pilihan_kota,
        'jam': jam_terpilih,
        'penumpang': list_penumpang,
        'total_harga': total_harga_tiket
    }

    # Cetak Struk
    print("-" * 46)
    print("   PT. Kereta API Indonesia - Stasiun Sudirman   ")
    print("-" * 46)
    print("Kode Pemesanan Tiket : ", kode_pemesanan)
    print("Nama Kereta Api      : ", namaKereta)
    print("Kota Tujuan          : ", pilihan_kota)
    print("Jam Keberangkatan    : ", jam_terpilih)
    print("Nama dan KTP Pemesan :")
    for penumpang in list_penumpang:
        print(f"- {penumpang['nama']} (KTP: {penumpang['ktp']})")
    print("-" * 46)
    print("Total Harga Tiket adalah", "Rp.", total_harga_tiket)
    print("-" * 46)
    print("")

# Function untuk Membatalkan Tiket
def pembatalan_tiket():
    print("-" * 36)
    print("Pembatalan Tiket")
    print("-" * 36)
    
    kode_batal = int(input("Masukan Kode Pemesanan Tiket: "))
    
    if kode_batal in tiket_terpesan:
        clearTerminal()
        print("Informasi Pemesanan Tiket:")
        print("-" * 46)
        print("Kode Pemesanan  : ", kode_batal)
        print("Nama Kereta Api : ", tiket_terpesan[kode_batal]['kereta'])
        print("Kota Tujuan     : ", tiket_terpesan[kode_batal]['kota'])
        print("Jam Keberangkatan : ", tiket_terpesan[kode_batal]['jam'])
        print("Total Harga     : Rp.", tiket_terpesan[kode_batal]['total_harga'])
        print("-" * 46)
        konfirmasi = input("Apakah Anda yakin ingin membatalkan tiket ini? [Y/T]: ").strip().upper()
        if konfirmasi == 'Y':
            del tiket_terpesan[kode_batal]
            clearTerminal()
            print("Tiket dengan kode", kode_batal, "telah dibatalkan.")
        else:
            print("Pembatalan tiket dibatalkan.")
    else:
        clearTerminal()
        print("Kode pemesanan tidak ditemukan.")

# Function untuk Layanan Pelanggan (CS)
def layanan_pelanggan():
    clearTerminal()
    print("=" * 36)
    print("Layanan Pelanggan - PT. Kereta API Indonesia")
    print("-" * 36)
    print("Nomor Telepon: 021-12345678")
    print("Email       : cs@kai.id")
    print("Alamat      : Jl. Perintis Kemerdekaan No. 1")
    print("=" * 36)
    print("")

# Perulangan Untuk mengkonfirmasi pemesanan tiket kembali
def konfirmasi_pemesanan_ulang():
    while True:
        pilihan = input("Apakah Anda ingin memesan tiket kembali? [Y/T] ... ").strip().upper()
        if pilihan == "Y":
            clearTerminal()
            list_menu()
            break
        elif pilihan == "T":
            clearTerminal()
            print("Baik, Terima Kasih telah menggunakan aplikasi kami :)")
            exit()
        else:
            print("Input tidak valid. Silakan coba lagi.")

########################################################################
############# SISTEM PEMESANAN TIKET : Percabangan dll. ################
########################################################################

# Menampilkan list menu aplikasi
list_menu()

# Keputusan pemilihan menu aplikasi
pilihan_menu = int(input("Masukan Pilihan Anda: "))
print("-" * 36)

# Percabangan Pemilihan menu aplikasi
if pilihan_menu == 1:
    # Menampilkan List Kota
    clearTerminal()
    list_kota()

    # Keputusan pemilihan kota tujuan
    pilihan_kota = input("Masukan Nama Kota Tujuan Anda: ").strip().capitalize()
    clearTerminal()

    # Percabangan bersarang untuk list kereta api
    print("=" * 55)
    print(f"Daftar Kereta Api yang Tersedia untuk Jurusan {pilihan_kota}")
    print("-" * 55)
    if pilihan_kota == "Bandung":
        # List Kereta Api Bandung
        print("1. Cikuray Eksekutif")
        print("2. Argo Parahyangan")
        # Keputusan pemilihan kereta api
        pilihan_kereta = int(input("Masukan Pilihan Kereta Anda: "))
        if pilihan_kereta == 1:
            harga_tiket = 10000
            namaKereta = "Cikuray Eksekutif"
            jam_keberangkatan = ["06:00", "12:00", "18:00"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Cikuray Eksekutif")
            pemesanan()
            konfirmasi_pemesanan_ulang()
        elif pilihan_kereta == 2:
            harga_tiket = 250000
            namaKereta = "Argo Parahyangan"
            jam_keberangkatan = ["08:00", "14:00", "20:00"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Argo Parahyangan")
            pemesanan()
            konfirmasi_pemesanan_ulang()

    elif pilihan_kota == "Malang":
        # List Kereta Api Malang
        print("1. KA Argo wilis")
        print("2. KA Brawijaya")
        # Keputusan pemilihan kereta api
        pilihan_kereta = int(input("Masukan Pilihan Kereta Anda: "))
        if pilihan_kereta == 1:
            harga_tiket = 300000
            namaKereta = "KA Argo wilis"
            jam_keberangkatan = ["07:00", "13:00", "19:00"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Argo wilis")
            pemesanan()
            konfirmasi_pemesanan_ulang()
        elif pilihan_kereta == 2:
            harga_tiket = 500000
            namaKereta = "KA Brawijaya"
            jam_keberangkatan = ["09:00", "15:00", "21:00"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Brawijaya")
            pemesanan()
            konfirmasi_pemesanan_ulang()
        else:
            print("Pilihan kereta tidak valid.")

    elif pilihan_kota == "Garut":
        # List Kereta Api Garut
        print("1. KA Pangrango")
        print("2. KA Serayu")
        # Keputusan pemilihan kereta api
        pilihan_kereta = int(input("Masukan Pilihan Kereta Anda: "))
        if pilihan_kereta == 1:
            harga_tiket = 150000
            namaKereta = "KA Pangrango"
            jam_keberangkatan = ["06:30", "12:30", "18:30"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Pangrango")
            pemesanan()
            konfirmasi_pemesanan_ulang()
        elif pilihan_kereta == 2:
            harga_tiket = 200000
            namaKereta = "KA Serayu"
            jam_keberangkatan = ["07:30", "13:30", "19:30"]
            clearTerminal()
            print("Kamu memilih Kereta Api KA Serayu")
            pemesanan()
            konfirmasi_pemesanan_ulang()
        else:
            print("Pilihan kereta tidak valid.")
    else:
        print("Kota tujuan tidak valid.")

elif pilihan_menu == 2:
    clearTerminal()
    pembatalan_tiket()

elif pilihan_menu == 3:
    layanan_pelanggan()

elif pilihan_menu == 4:
    clearTerminal()
    print("Terima kasih telah menggunakan aplikasi kami. Selamat tinggal!")

else:
    clearTerminal()
    print("Pilihan tidak valid.")
