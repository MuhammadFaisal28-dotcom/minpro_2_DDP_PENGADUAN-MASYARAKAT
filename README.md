# minpro_2_DDP_PENGADUAN-MASYARAKAT

### Biodata Mahasiswa
- **Nama** : Muh. Faisal
- **NIM** : 2609116075
- **Kelas** : B
- **Program studi** : dasar-dasar pemrogrmaan
- **tugas** : mini project 2

## 1. Deskripsi Singkat

sistem pelayanan pengaduan masyarakat ini merupakan pemrograman untuk mempermudah masyarakat dalam menyampaikan pengaduan ke pemerintah agar pemerintah dapat menindak lanjuti permasalahan masyarakat secara cepat dan tepat contohnya seperti (masalah jalan berlubang, mati lampu, bencana alam, maling, hingga fasilitas umum dll). secara terstruktur dan efisien.

pada minpro 2 ini merupakan progeram yang di kembangkan dari minpro1, ppada program ini di tambhkan menu user dan admin dann penerapan "dictionery", "function",  validasi input menggunakan *Conditional Statement* dan *Exception Handling*, serta integrasi **Library Python** untuk meningkatkan fungsionalitas dan tampilan antarmuka.


## 2. Screenshot Flowchart

<img width="2800" height="2272" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/0803b3a8-fab7-4c55-8281-74078cfc3cfd" />

gambr diatas merupakan gambar flowchart yang ku buat untuk program minipro 2

### Ringkasan Alur Program:


1. **Tahap Inisialisasi & Halaman Login/Registrasi**:
   - **Start**: Program dimulai dan menampilkan **Menu Login**.
   - **Pengecekan Akun (`Sudah Punya Akun?`)**:
     - **Jika TIDAK**: Pengguna diarahkan ke proses **Daftar Akun** (`Input Username` -> `Input Password` -> `Simpan Akun User`), lalu kembali ke **Menu Login**.
     - **Jika IYA**: Pengguna memilih opsi **Login ke Menu Utama**.
       - Jika memilih tidak login, sistem menanyakan `Keluar dari Menu Login?`. Jika **IYA**, program selesai (**END**); jika **TIDAK**, kembali ke **Menu Login**.
       - Jika memilih login, sistem memverifikasi hak akses/role:
         1. **Login sebagai Admin**: Input `Username Admin` & `Password Admin`. Jika valid, masuk ke **Menu Admin**. Jika salah, kembali ke **Menu Login**.
         2. **Login sebagai User**: Input `Username` & `Password`. Jika valid, masuk ke **Menu User**. Jika salah, kembali ke **Menu Login**.

2. **Alur Menu Admin (1-5 Daftar Menu)**:
   - **Menu 1 (Tambah Pengaduan)**: Input Nama, Kategori (1-7), dan Isi Pengaduan. Data disimpan dan ditampilkan di terminal, lalu kembali ke menu Admin.
   - **Menu 2 (Lihat Pengaduan)**: Mengecek keberadaan data pengaduan. Jika ada, menampilkan seluruh pengaduan warga. Jika tidak ada, menampilkan pesan `"Belum Ada Pengaduan"`.
   - **Menu 3 (Ubah Pengaduan)**: Mengecek data pengaduan. Jika ada, Admin menginput nama data yang ingin diubah, lalu memasukkan Nama Baru, Kategori Baru (1-7), dan Isi Pengaduan Baru.
   - **Menu 4 (Hapus Pengaduan)**: Mengecek data pengaduan. Jika ada, Admin menginput nama data yang mau dihapus, lalu data dihapus dari sistem.
   - **Menu 5 (Keluar)**: Mengakhiri sesi Admin dan keluar ke proses akhir (**END**).

3. **Alur Menu User (1-4 Daftar Menu)**:
   - **Menu 1 (Tambah Pengaduan)**: Input Nama, Kategori (1-7), dan Isi Pengaduan. Data disimpan dan kembali ke menu User.
   - **Menu 2 (Lihat Pengaduan)**: Menampilkan daftar pengaduan warga jika ada, atau pesan `"Belum Ada Pengaduan"` jika kosong.
   - **Menu 3 (Ubah Pengaduan)**: Memasukkan nama data yang ingin diubah, lalu mengupdate Nama Baru, Kategori Baru (1-7), dan Isi Pengaduan Baru.
   - **Menu 4 (Keluar)**: Mengakhiri sesi User dan keluar ke proses akhir (**END**).

4. **Tahap Akhir (END)**: Program selesai ketika pengguna memilih keluar.

## 3. Penjelasan Kode


### A. Libery

<img width="452" height="140" alt="Cuplikan layar 2026-10-05 225155" src="https://github.com/user-attachments/assets/242460b9-3278-47b4-b039-7f7f7f4b36b4" />

**penjelasan kode**

| Library       | Kegunaan di program                          |
| ------------- | -------------------------------------------- |
| `datetime`    | Mengambil **tanggal otomatis**               |
| `random`      | Membuat **nomor pengaduan acak**             |
| `pwinput`     | **Menyembunyikan password**                  |
| `prettytable` | Menampilkan pengaduan dalam **bentuk tabel** |

### B. menyimpan data akun pengguna

<img width="561" height="226" alt="Cuplikan layar 2026-10-06 001647" src="https://github.com/user-attachments/assets/f69afe7b-af63-44ec-ae22-eea4ba6e4ffa" />

Penjelasannya:

akun → nama dictionary untuk menyimpan data akun.
"admin" → username akun.
"password": "admin123" → password dari username admin.
"role": "admin" → menunjukkan bahwa akun tersebut memiliki hak akses sebagai admin.
Jadi saat login, program bisa mengecek:

if username in akun and akun[username]["password"] == password:

Kalau username dan password benar, program akan tahu bahwa orang tersebut adalah admin.

data_pengaduan = []

fungsinya untuk menyediakan tempat menyimpan semua data pengaduan masyarakat.

[] artinya list kosong. Awalnya belum ada pengaduan, jadi masih kosong

### C.Fungsi daftar()

<img width="677" height="462" alt="Cuplikan layar 2026-10-06 002740" src="https://github.com/user-attachments/assets/b41a6607-fa04-4aa4-a607-44ab12f17bd8" />

### Penjelasan Logika Kode:

1. **Input Data &amp; Keamanan (** **pwinput** **)**
  * Mengambil `username` menggunakan `input()` biasa.
  * Mengambil `password` menggunakan `pwinput.pwinput()`, sehingga karakter password tersensor saat diketik di terminal.
2. **Validasi Berbelapis (** **if - elif - else** **)**
  * **Cek Kosong (** **if username == "" or password == ""** **):** Mencegah pendaftaran akun jika ada bidang input yang belum diisi.
  * **Cek Duplikasi (** **elif username in akun** **):** Memeriksa apakah `username` tersebut sudah terdaftar di dalam dictionary `akun` agar tidak terjadi penumpukan data dengan kunci yang sama.
3. **Penyimpanan pada Nested Dictionary**
  * **akun[username] = {"password": password, "role": "user"}** Menambahkan akun baru ke dalam dictionary `akun` dengan *role* otomatis diset sebagai `"user"`.

contoh dokumntasi output nya

<img width="325" height="131" alt="Cuplikan layar 2026-10-06 003303" src="https://github.com/user-attachments/assets/4cd427b8-dfed-4c19-a43e-61f4bb6e9240" />

### D.fungsi login

<img width="880" height="702" alt="Cuplikan layar 2026-10-06 003510" src="https://github.com/user-attachments/assets/d66af089-b073-4491-be57-231aaa7caaa0" />

### **1\. Penjelasan Fungsi** **daftar()** **(Registrasi Akun)**

Fungsi ini bertugas menangani pendaftaran akun baru untuk pengguna biasa (*role: user*):

* **Input Data:** Meminta pengguna memasukkan `username` dan `password` (menggunakan `pwinput` agar password tersensor saat diketik).
* **Validasi Kosong (** **if username == "" or password == ""** **):** Mencegah pendaftaran jika ada kolom yang tidak diisi.
* **Pengecekan Duplikasi (** **elif username in akun** **):** Memeriksa apakah `username` tersebut sudah terdaftar sebagai *key* di dalam dictionary `akun` agar tidak terjadi penumpukan data.
* **Penyimpanan Data (** **else** **):** Menambahkan akun baru ke dalam dictionary `akun` dengan bentuk **Nested Dictionary**:

```
akun[username] = {
    "password": password,
    "role": "user"
}

```

*(Role otomatis diatur sebagai* *"user"* *).*

---

### **2\. Penjelasan Fungsi** **login()** **(Menu Utama &amp; Autentikasi)**

Fungsi ini berfungsi sebagai gerbang utama aplikasi yang menghubungkan proses login dan pendaftaran:

* **Perulangan Menu (** **while True** **):** Menjaga agar tampilan menu login terus muncul sampai pengguna berhasil masuk atau memilih keluar.
* **Opsi 1 — Login Sistem:**
  * Meminta `username` dan `password`.
  * **Verifikasi Data:** Memeriksa keberadaan akun dan kecocokan password dengan sintaks `if username in akun and akun[username]["password"] == password:`.
  * **Return Value:** Jika valid, fungsi mengembalikan nilai `username` dan `role` (`return username, akun[username]["role"]`). Nilai ini akan digunakan oleh program utama untuk menentukan hak akses menu (Admin atau User).
* **Opsi 2 — Memanggil** **daftar()** **:**
  * Mengarahkan pengguna ke fungsi `daftar()` jika belum memiliki akun. Setelah selesai mendaftar, pengguna kembali ke menu login ini.
* **Opsi 3 — Keluar:**
  * Mengembalikan nilai `"keluar", "keluar"` untuk menghentikan perulangan aplikasi.
* **Opsi Else:**
  * Menampilkan pesan eror jika pengguna memasukkan angka di luar pilihan menu (1/2/3).
 
### E.Tambah Pengaduan

<img width="942" height="858" alt="Cuplikan layar 2026-10-06 004223" src="https://github.com/user-attachments/assets/4a41d95f-4b35-4d8f-aa5e-a51b6619959d" />

<img width="745" height="623" alt="Cuplikan layar 2026-10-06 004348" src="https://github.com/user-attachments/assets/564f8d1c-0912-4fdc-89d8-d5dae7bfab29" />

### **1\. Header Fungsi &amp; Parameter (** **def tambah\_pengaduan(username)** **)**

* **username**: Fungsi ini menerima parameter `username` milik akun yang sedang aktif/login, sehingga sistem tahu laporan ini dibuat oleh siapa.

---

### **2\. Validasi Nama Pengadu**

```
nama = input("Nama pengadu: ")
if nama == "":
    print("Nama pengadu tidak boleh kosong!")
    return

```

* Meminta input nama pengadu.
* Jika pengguna mengosongkan input (`nama == ""`), sistem mencetak pesan peringatan dan langsung menghentikan fungsi dengan perintah **return**.

---

### **3\. Pilihan Kategori &amp; Validasi Input (** **try-except** **)**

```
kategori = ["Lampu","Jalan","Sampah","Bencana","Air","Keamanan","Fasilitas"]
try:
    pilih = int(input("Kategori: "))

    if pilih &lt; 1 or pilih &gt; 7:
        print("Kategori tidak tersedia!")
        return
except ValueError:
    print("kategori harus berupa angka!")
    return

kategori = kategori[pilih - 1]

```

* **Menu Kategori**: Menampilkan 7 daftar pilihan kategori.
* **Penanganan Eror (** **try-except ValueError** **)**: Menangkap eror jika pengguna memasukkan karakter huruf/teks pada input kategori.
* **Validasi Range (** **if pilih &lt; 1 or pilih &gt; 7** **)**: Memastikan angka yang dimasukkan berada di rentang 1 sampai 7.
* **Konversi Indeks (** **kategori[pilih - 1]** **)**: Mengubah angka pilihan pengguna menjadi teks nama kategori (misalnya pilihan `1` mengambil indeks `0` yaitu `"Lampu"`).

---

### **4\. Validasi Isi Pengaduan**

```
isi = input("Isi pengaduan: ")
if isi == "":
    print("Data pengaduan tidak boleh kosong!")
    return

```

* Meminta detail penjelasan laporan. Jika dikosongkan, fungsi akan dihentikan via `return`.

---

### **5\. Otomatisasi Data (Nomor Tiket, Tanggal, &amp; Status)**

```
nomor = random.randint(1000, 9999)
tanggal = datetime.datetime.now().strftime("%d-%m-%Y")
status = "Diproses"

```

* **random.randint(1000, 9999)**: Menggenerasi nomor aduan acak 4 digit menggunakan library `random`.
* **datetime.datetime.now().strftime("%d-%m-%Y")**: Mengambil tanggal dan waktu saat ini secara otomatis dari sistem dalam format `Hari-Bulan-Tahun`.
* **status = "Diproses"**: Mengatur status awal setiap laporan baru.

---

### **6\. Penyimpanan ke Dictionary &amp; List Database**

```
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

```

* Membungkus seluruh informasi laporan ke dalam sebuah **Dictionary** (`data`).
* Menambahkan dictionary tersebut ke dalam list utama `data_pengaduan` menggunakan metode **.append()**.

---

### **7\. Tampilan Output Konfirmasi**



```
print("Pengaduan berhasil ditambahkan!")
print("Nomor pengaduan:", nomor)
print("Tanggal:", tanggal)

```
<img width="367" height="547" alt="Cuplikan layar 2026-10-06 004820" src="https://github.com/user-attachments/assets/c651a97d-615f-4786-a335-658b7e86b895" />

* Menampilkan pesan bahwa laporan berhasil disimpan, serta memperlihatkan nomor aduan dan tanggal pembuatan sebagai bukti bagi pengadu.

  ### F.lihat Pengaduan

  <img width="857" height="572" alt="Cuplikan layar 2026-10-06 005059" src="https://github.com/user-attachments/assets/1e0aa5e1-d786-432c-a0bc-fd96c36359de" />

### **1\. Header Fungsi &amp; Judul (** **def lihat\_pengaduan()** **)**

```
def lihat_pengaduan():
    print("=========================")
    print("     DAFTAR PENGADUAN")

```

* Menandai awal definisi fungsi `lihat_pengaduan()` yang akan mencetak judul halaman di layar terminal.

---

### **2\. Pengecekan Data Kosong (** **if data\_pengaduan == []:** **)**

```
if data_pengaduan == []:
    print("Belum ada pengaduan.")

```

* Memeriksa apakah list `data_pengaduan` masih kosong.
* Jika kosong (`True`), sistem langsung mencetak pesan `"Belum ada pengaduan."` dan tidak menjalankan pembuatan tabel.

---

### **3\. Inisialisasi Tabel (** **tabel = PrettyTable()** **)**

```
else:
    tabel = PrettyTable()
    tabel.field_names = ["Nomor","Nama","Kategori","Isi","Status","Tanggal"]

```

* **PrettyTable()**: Membuat objek tabel baru dari library `prettytable`.
* **tabel.field\_names**: Menentukan judul untuk setiap kolom tabel, yaitu `Nomor`, `Nama`, `Kategori`, `Isi`, `Status`, dan `Tanggal`.

---

### **4\. Perulangan &amp; Memasukkan Baris Data (** **for** **&amp;** **add\_row** **)**

```
for data in data_pengaduan:
    tabel.add_row([
        data["nomor"],
        data["nama"],
        data["kategori"],
        data["isi"],
        data["status"],
        data["tanggal"]
    ])

```

* **for data in data\_pengaduan:**: Melakukan perulangan untuk membaca setiap item laporan (berbentuk *dictionary*) yang ada di dalam list `data_pengaduan`.
* **tabel.add\_row([...])**: Mengambil nilai (*value*) berdasarkan kunci (*key*) dari *dictionary* `data` (`data["nomor"]`, `data["nama"]`, dsb.), lalu memasukkannya sebagai baris baru ke dalam tabel.

---

### **5\. hasil output nya

<img width="705" height="162" alt="Cuplikan layar 2026-10-06 005312" src="https://github.com/user-attachments/assets/4857267c-28a0-4ab8-9531-be84027d0f2a" />

 ### G. Ubah Pengaduan

<img width="587" height="455" alt="Cuplikan layar 2026-10-06 005541" src="https://github.com/user-attachments/assets/420f6b56-440c-4981-98ca-9c86dd6c80df" />

<img width="926" height="872" alt="Cuplikan layar 2026-10-06 005527" src="https://github.com/user-attachments/assets/7ba6676d-723b-4e28-ab76-53eae595060b" />

Fungsi **ubah\_pengaduan()** bertugas untuk memperbarui data laporan pengaduan yang sudah ada berdasarkan **nomor pengaduan**.

1. **Cek Data Kosong:** Memeriksa `data_pengaduan`. Jika belum ada aduan, fungsi langsung berhenti (`return`).
2. **Input Nomor Aduan:** Meminta nomor aduan yang ingin diubah dengan validasi `try-except` agar input harus berupa angka.
3. **Pencarian Data (** **for loop** **):** Mencari laporan di `data_pengaduan` yang `nomor`\-nya cocok dengan input.
4. **Input &amp; Validasi Data Baru:**
  * **Nama:** Diinput ulang (tidak boleh kosong).
  * **Kategori:** Dipilih dari 7 opsi (diuji agar berupa angka 1–7).
  * **Isi Aduan:** Diinput ulang (tidak boleh kosong).
5. **Update Data:** Mengganti nilai `nama`, `kategori`, dan `isi` pada dictionary, serta mereset `status` kembali menjadi **"Diproses"**.
6. **Penanganan Eror/Gagal:** Jika nomor aduan tidak ditemukan di dalam list, sistem mencetak `"Data tidak ditemukan!"`.

**Contoh outputnya**

<img width="431" height="345" alt="Cuplikan layar 2026-10-06 005917" src="https://github.com/user-attachments/assets/5e962bc0-ae7a-4182-8d2c-9b4dfda19546" />


 ### G. Hapus Pengaduan
 
 <img width="802" height="520" alt="Cuplikan layar 2026-10-06 010056" src="https://github.com/user-attachments/assets/943a1bb3-404c-49c7-b162-0b552d46d120" />

Fungsi **hapus\_pengaduan()** bertugas untuk menghapus data laporan pengaduan tertentu dari list database berdasarkan **nomor pengaduan**.

Berikut alur ringkas kodenya:

1. **Cek Data Kosong (** **if data\_pengaduan == []** **):** Memeriksa apakah database pengaduan masih kosong. Jika kosong, fungsi langsung berhenti (`return`).
2. **Input Nomor Aduan &amp; Validasi (** **try-except** **):** Meminta input nomor aduan yang ingin dihapus, sekaligus memvalidasinya agar pengguna harus memasukkan angka (*integer*).
3. **Pencarian Data (** **for loop** **):** Mencari laporan di `data_pengaduan` yang `nomor`\-nya cocok dengan input pengguna.
4. **Eksekusi Hapus Data (** **.remove()** **):** Jika nomor ditemukan, laporan tersebut dihapus dari list menggunakan `data_pengaduan.remove(data)`, mencetak pesan berhasil, dan langsung keluar dari fungsi (`return`).
5. **Penanganan Eror/Gagal:** Jika perulangan selesai dan nomor tidak ditemukan di dalam list, sistem mencetak `"Data tidak ditemukan!"`.

   **contoh hasil outputnya**

<img width="331" height="266" alt="Cuplikan layar 2026-10-06 010245" src="https://github.com/user-attachments/assets/70f967a0-4d9f-4ee6-97f0-8619a2ae496b" />

 ### H. keluar pengaduan dan tammpilan menu pada user

 <img width="885" height="772" alt="Cuplikan layar 2026-10-06 010331" src="https://github.com/user-attachments/assets/d6fcbc8e-6670-4e34-ad25-7be54d18f902" />

alur ringkas kodenya:

1. **Perulangan Utama (** **while True** **Luar):**
  * Memanggil fungsi `login()` untuk mendapatkan nilai `username` dan `role`.
  * **Cek Keluar (** **if role == "keluar"** **):** Jika pengguna memilih keluar dari menu login, program mencetak pesan terima kasih dan berhenti total (`break`).
2. **Pemeriksaan Role (** **if role == "user"** **):**
  * Memastikan bahwa sub-menu pengaduan hanya dapat diakses oleh pengguna dengan status/role `"user"`.
3. **Perulangan Menu User (** **while True** **Dalam):**
  * Menampilkan 4 pilihan menu utama dan menerima input pilihan pengguna.
  * **Opsi 1:** Memanggil `tambah_pengaduan(username)` dengan membawa parameter *username* aktif.
  * **Opsi 2:** Memanggil `lihat_pengaduan()` untuk menampilkan tabel laporan.
  * **Opsi 3:** Memanggil `ubah_pengaduan()` untuk memperbarui isi laporan.
  * **Opsi 4:** Menghentikan loop menu user (`break`) untuk *logout* dan kembali ke tampilan login utama.
  * **Else:** Menampilkan pesan peringatan jika pengguna memasukkan angka di luar opsi 1–4.

**contoh outputnya**

<img width="655" height="342" alt="Cuplikan layar 2026-10-06 010914" src="https://github.com/user-attachments/assets/b63da07d-0b5f-49bb-a5ab-f243f89ef3a6" />

   ### I. tammpilan menu pada admin

   <img width="910" height="702" alt="Cuplikan layar 2026-10-06 011026" src="https://github.com/user-attachments/assets/735ec7ac-0ac2-4e3d-b782-96ffd493d940" />

alur ringkas kodenya:

1. **Pemeriksaan Role (** **elif role == "admin":** **)**:
  * Memastikan sub-menu ini hanya bisa diakses oleh akun yang memiliki hak akses/role `"admin"`.
2. **Perulangan Menu Admin (** **while True** **)**:
  * Menampilkan 5 pilihan menu utama khusus Admin dan menerima input opsi dari pengguna.
  * **Opsi 1 (Tambah Pengaduan):** Memanggil `tambah_pengaduan(username)` untuk mencatat laporan baru.
  * **Opsi 2 (Lihat Pengaduan):** Memanggil `lihat_pengaduan()` untuk menampilkan seluruh daftar laporan masyarakat.
  * **Opsi 3 (Ubah Data Pengaduan):** Memanggil `ubah_pengaduan()` untuk mengubah isi atau memperbarui status laporan.
  * **Opsi 4 (Hapus Data Pengaduan):** Memanggil `hapus_pengaduan()` untuk menghapus aduan tertentu dari database (hak akses khusus Admin).
  * **Opsi 5 (Keluar):** Menghentikan loop menu Admin (`break`) untuk *logout* dan kembali ke tampilan login utama.
  * **Else:** Menampilkan pesan peringatan jika Admin memasukkan angka di luar opsi 1–5.

    **hasil outputnnya**

<img width="605" height="228" alt="Cuplikan layar 2026-10-06 011141" src="https://github.com/user-attachments/assets/e5b35fdd-c6ca-432c-b5ff-e20c5f3cf65e" />

## Penjelasan Nilai Tambah

### 1. Robustness Melalui Exception Handling (`try-except`)

Penggunaan struktur penanganan eksepsi `try-except` pada fungsi input numerik memberikan jaminan stabilitas (*fault tolerance*). Program tidak akan mengalami *runtime exception* atau *traceback crash* ketika pengguna memasukkan karakter alfabetis atau simbol tak valid. Program secara otomatis meminta input ulang sampai nilai yang sah diberikan.

### 2. PENJELASAN LEBRY YANG DI GUNAKAN
| **Modul / Library** | **Jenis Library** | **Fungsi Utama**           | **Peran dalam Program**                                    |
| ------------------- | ----------------- | -------------------------- | ---------------------------------------------------------- |
| **datetime**        | Built-in (Bawaan) | Mengolah tanggal dan waktu | Mengambil tanggal pembuatan pengaduan secara otomatis.     |
| **random**          | Built-in (Bawaan) | Menghasilkan angka acak    | Membuat nomor pengaduan secara acak dari **1000–9999**.    |
| **pwinput**         | Eksternal         | Mengamankan input password | Menyembunyikan password saat diketik di terminal.          |
| **prettytable**     | Eksternal         | Membuat tampilan tabel     | Menampilkan daftar pengaduan dalam bentuk tabel yang rapi. |
