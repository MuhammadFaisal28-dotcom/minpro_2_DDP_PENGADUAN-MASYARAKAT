import datetime
import random
import pwinput
from prettytable import PrettyTable

akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

data_pengaduan = []

def daftar():
    print("=========================")
    print("       DAFTAR AKUN")

    username = input("Buat username: ")
    password = pwinput.pwinput("Buat password: ")

    if username == "" or password == "":
        print("Username dan password tidak boleh kosong!")
    elif username in akun:
        print("Username sudah digunakan!")
    else:
        akun[username] = {
            "password": password,
            "role": "user"
        }

        print("Akun berhasil dibuat!")
        print("Silahkan login.")

def login():
    while True:

        print("=========================")
        print("          LOGIN")
        print("1. LOGIN")
        print("2. DAFTAR AKUN")
        print("3. KELUAR")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username = input("Username: ")
            password = pwinput.pwinput("Password: ")
            if username in akun and akun[username]["password"] == password:
                print("Login berhasil!")
                print("Role:", akun[username]["role"])
                return username, akun[username]["role"]
            else:
                print("Username atau password salah!")
                print("Silahkan masukkan kembali.")

        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            return "keluar", "keluar"
        else:
            print("Menu tidak tersedia!")

def tambah_pengaduan(username):

    print("=========================")
    print("  MASUKKAN DATA PENGADUAN")

    nama = input("Nama pengadu: ")
    if nama == "":
        print("Nama pengadu tidak boleh kosong!")
        return

    print("KATEGORI")
    print("1. Lampu")
    print("2. Jalan")
    print("3. Sampah")
    print("4. Bencana")
    print("5. Air")
    print("6. Keamanan")
    print("7. Fasilitas")

    kategori = ["Lampu","Jalan","Sampah","Bencana","Air","Keamanan","Fasilitas"]
    try:
        pilih = int(input("Kategori: "))

        if pilih < 1 or pilih > 7:
            print("Kategori tidak tersedia!")
            return
    except ValueError:
        print("kategori harus berupa angka!")
        return

    kategori = kategori[pilih - 1]

    isi = input("Isi pengaduan: ")

    if isi == "":
        print("Data pengaduan tidak boleh kosong!")
        return

    nomor = random.randint(1000, 9999)
    tanggal = datetime.datetime.now().strftime("%d-%m-%Y")
    status = "Diproses"
    data = {
        "nomor": nomor,
        "nama": nama,
        "kategori": kategori,
        "isi": isi,
        "status": status,
        "tanggal": tanggal,
        "username": username
    }

    data_pengaduan.append(data)
    print("Pengaduan berhasil ditambahkan!")
    print("Nomor pengaduan:", nomor)
    print("Tanggal:", tanggal)

def lihat_pengaduan():

    print("=========================")
    print("     DAFTAR PENGADUAN")

    if data_pengaduan == []:

        print("Belum ada pengaduan.")

    else:
        tabel = PrettyTable()
        tabel.field_names = ["Nomor","Nama","Kategori","Isi","Status","Tanggal"]
        for data in data_pengaduan:
            tabel.add_row([
                data["nomor"],
                data["nama"],
                data["kategori"],
                data["isi"],
                data["status"],
                data["tanggal"]
            ])

        print(tabel)

def ubah_pengaduan():

    print("=========================")
    print("     UBAH PENGADUAN")

    if data_pengaduan == []:

        print("Belum ada pengaduan.")
        return
    try:
        nomor = int(input("Masukkan nomor pengaduan: "))
    except ValueError:
        print("nomor pengaduan harus berupa angka!")

    for data in data_pengaduan:
        if data["nomor"] == nomor:
            nama = input("Nama baru: ")

            if nama == "":
                print("Nama tidak boleh kosong!")
                return

            print("KATEGORI")
            print("1. Lampu")
            print("2. Jalan")
            print("3. Sampah")
            print("4. Bencana")
            print("5. Air")
            print("6. Keamanan")
            print("7. Fasilitas")

            kategori = ["Lampu", "Jalan","Sampah","Bencana","Air","Keamanan","Fasilitas"]
            try:
                pilih = int(input("Kategori: "))

                if pilih < 1 or pilih > 7:
                    print("Kategori tidak tersedia!")
                    return
            except ValueError:
                print("kategori harus berupa angka!")
                return

            kategori = kategori[pilih - 1]
            isi = input("Isi pengaduan baru: ")
            if isi == "":
                print("Isi pengaduan tidak boleh kosong!")
                return

            data["nama"] = nama
            data["kategori"] = kategori
            data["isi"] = isi
            data["status"] = "Diproses"
            print("Data berhasil diubah!")
            return

    print("Data tidak ditemukan!")

def hapus_pengaduan():

    print("=========================")
    print("     HAPUS PENGADUAN")

    if data_pengaduan == []:

        print("Belum ada data yang dapat dihapus.")
        return
    try:
        nomor = int(input("Masukkan nomor pengaduan: "))
    except ValueError:
        print("nomor pengaduan harus berupa angkka!")
        return

    for data in data_pengaduan:
        if data["nomor"] == nomor:
            data_pengaduan.remove(data)
            print("Data berhasil dihapus!")
            return
    print("Data tidak ditemukan!")

while True:
    username, role = login()

    if role == "keluar":
        print("TERIMA KASIH TELAH MENGGUNAKAN LAYANAN INI")
        break

    if role == "user":

        while True:
            print("=========================")
            print("MENU PENGADUAN MASYARAKAT")
            print("=========================")
            print("1. TAMBAH PENGADUAN")
            print("2. LIHAT PENGADUAN")
            print("3. UBAH DATA PENGADUAN")
            print("4. KELUAR")

            pilihan = input("Pilih menu (1/2/3/4): ")

            if pilihan == "1":
                tambah_pengaduan(username)
            elif pilihan == "2":
                lihat_pengaduan()
            elif pilihan == "3":
                ubah_pengaduan()
            elif pilihan == "4":
                print("Berhasil keluar, terima kasih telah menggunakkan layannan ini")
                break
            else:
                print("Menu tidak tersedia!")
                print("Silahkan pilih menu 1-4.")

    elif role == "admin":

        while True:
            print("=================================")
            print(" PENGADUAN MASYARAKAT (MENU ADMIN)")
            print("===================================")
            print("1. TAMBAH PENGADUAN")
            print("2. LIHAT PENGADUAN")
            print("3. UBAH DATA PENGADUAN")
            print("4. HAPUS DATA PENGADUAN")
            print("5. KELUAR")

            pilihan = input("Pilih menu (1/2/3/4/5): ")

            if pilihan == "1":
                tambah_pengaduan(username)
            elif pilihan == "2":
                lihat_pengaduan()
            elif pilihan == "3":
                ubah_pengaduan()
            elif pilihan == "4":
                hapus_pengaduan()
            elif pilihan == "5":
                print("Berhasil keluar terima kasih telah mengguakan layanan ini.")
                break
            else:
                print("Menu tidak tersedia!")
                print("Silahkan pilih menu 1-5.")