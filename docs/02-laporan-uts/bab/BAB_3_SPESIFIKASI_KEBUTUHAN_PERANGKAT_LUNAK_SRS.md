# BAB III: SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS / SKPL)

---

## 3.1 Ruang Lingkup Sistem & Arsitektur Desktop Offline-First
Sistem **SmartPOS** dirancang sebagai aplikasi desktop mandiri (*standalone desktop application*) yang beroperasi di atas lingkungan runtime Electron 31 dan basis data relasional SQLite 3 (`better-sqlite3`). Seluruh proses bisnis berjalan secara lokal tanpa memerlukan ketergantungan koneksi internet (*zero cloud dependency*).

```mermaid
graph TD
    subgraph Mesin Komputer Desktop Kasir
        subgraph Renderer Process (Chromium Sandbox)
            UI["Halaman Antarmuka Kasir & Manajemen (HTML5/CSS3/JS)"]
        end
        subgraph Preload Isolation Layer
            Bridge["contextBridge API ('preload.js')"]
        end
        subgraph Main Process (Node.js 20+ Runtime)
            IPC["IPC Handlers ('main.js')"]
            Logic["Business Logic Modules ('database/*.js')"]
            Engine["SQLite 3 Engine ('better-sqlite3')"]
        end
        DB[("Basis Data Lokal ('app.db')")]
        Printer["Printer Kasir Thermal (80mm)"]
    end

    UI <--> Bridge
    Bridge <--> IPC
    IPC <--> Logic
    Logic <--> Engine
    Engine <--> DB
    IPC -.-> Printer
```

---

## 3.2 Kebutuhan Fungsional (Functional Requirements)
Mengacu pada kaidah perkuliahan Pertemuan 4 (Slide 10 & 11), kebutuhan fungsional dirumuskan secara eksplisit dengan subjek yang jelas, kata kerja spesifik, dan hasil tindakan yang terukur:

| ID Kebutuhan | Modul / Kategori | Rumusan Kebutuhan Fungsional Baku |
| :---: | :--- | :--- |
| **FR-01** | Autentikasi | Sistem memungkinkan pengguna masuk (*login*) menggunakan username dan password valid, serta mengarahkan pengguna ke halaman yang sesuai hak akses perannya (`admin` atau `kasir`). |
| **FR-02** | Manajemen User | Sistem memungkinkan Admin membuat akun pengguna baru, mengatur status keaktifan akun, dan memperbarui kata sandi dengan verifikasi enkripsi salt kriptografi. |
| **FR-03** | Katalog Produk | Sistem memungkinkan Admin menambah, memperbarui, mencari, dan menonaktifkan produk komoditas pangan dengan mengatur unit primer (kg), unit sekunder (karung), rasio konversi, dan batas stok minimum. |
| **FR-04** | Transaksi Kasir | Sistem memungkinkan Kasir memilih produk, mengatur kuantitas desimal, menerapkan diskon, dan memilih metode pembayaran (tunai, transfer, QRIS) untuk menghasilkan nota penjualan. |
| **FR-05** | Konversi "Beli Rp" | Sistem memungkinkan Kasir memasukkan nilai nominal belanja rupiah pada komoditas timbangan, dan secara otomatis mengonversinya menjadi berat pecahan kilogram secara akurat. |
| **FR-06** | Validasi Kembalian | Sistem menghitung selisih nominal uang bayar dengan total tagihan, serta menolak proses checkout jika uang tunai yang diserahkan kurang dari total belanja. |
| **FR-07** | Cetak Struk 80mm | Sistem memungkinkan Kasir mencetak nota belanja kasir berukuran 80 mm ke printer thermal melalui Windows Print Spooler maupun direct socket TCP ESC/POS (port 9100). |
| **FR-08** | Pembatalan Transaksi | Sistem memungkinkan Admin membatalkan (*void*) transaksi kasir yang salah catat, dengan secara otomatis mengembalikan (*rollback*) jumlah stok produk ke kondisi semula. |
| **FR-09** | Dual-Stock Gas | Sistem mengelola kuantitas fisik tabung gas LPG secara terpisah antara stok tabung isi (`filled_stock`), stok tabung kosong (`empty_stock`), dan total aset tabung (`total_cylinders`). |
| **FR-10** | Tukar Gas Konsumen | Sistem memungkinkan Kasir mencatat transaksi tukar tabung konsumen, yang mengurangi stok tabung isi sebesar $N$, menambah stok tabung kosong sebesar $N$, tanpa mengubah total aset tabung di toko. |
| **FR-11** | Tukar Gas Agen: Kirim | Sistem memungkinkan Admin mencatat pengiriman tabung kosong ke agen, yang mengurangi stok tabung kosong dan mengurangi total tabung fisik di toko. |
| **FR-12** | Tukar Gas Agen: Terima | Sistem memungkinkan Admin mencatat penerimaan tabung isi dari agen, yang menambah stok tabung isi dan menambah total tabung fisik di toko, disertai pencatatan biaya pengadaan. |
| **FR-13** | Jual Tabung Perdana | Sistem memungkinkan Kasir memproses penjualan tabung gas baru beserta isinya tanpa tukar, yang mengurangi stok tabung isi dan mengurangi total aset tabung toko. |
| **FR-14** | Opname / Koreksi Gas | Sistem memungkinkan Admin melakukan penyesuaian delta fisik stok isi maupun kosong untuk mencocokkan selisih fisik riil (*stock opname*) disertai catatan alasan. |
| **FR-15** | Logistik Barang Masuk | Sistem memungkinkan Admin mencatat penerimaan pasokan barang dari distributor, dan secara otomatis memperbarui HPP menggunakan formula rata-rata tertimbang (*Moving Weighted Average*). |
| **FR-16** | Logistik Barang Keluar | Sistem memungkinkan Admin mencatat pengurangan stok non-penjualan (rusak, susut, retur, pemakaian pribadi) disertai pencatatan log audit stok sebelum dan sesudah mutasi. |
| **FR-17** | Manajemen Keuangan | Sistem memungkinkan Admin mencatat pos pengeluaran operasional toko dan pos penerimaan kas ekstra di luar transaksi kasir utama. |
| **FR-18** | Dashboard Analitik | Sistem menyajikan visualisasi ringkasan omzet harian, laba kotor, biaya operasional, laba bersih riil, dan grafik penjualan komoditas terlaris menggunakan Chart.js. |
| **FR-19** | Laporan & Ekspor | Sistem mengagregasi 6 kategori laporan (Penjualan, Stok, Keuangan, Sirkulasi Gas, Barang Masuk, Barang Keluar) berdasarkan rentang tanggal, serta mengekspornya ke format file Excel (.xlsx) dan PDF (.pdf). |
| **FR-20** | Backup & Restore Data | Sistem memungkinkan Admin membuat salinan cadangan (*backup archive*) basis data SQLite ke lokasi disk pilihan pengguna, serta memulihkan (*restore*) berkas database saat dibutuhkan. |

---

## 3.3 User Story & Acceptance Criteria (Format Given-When-Then)

### US-01: Penjualan Cepat & Konversi Otomatis "Beli Rp" (Kasir)
> **Sebagai** Kasir Toko,  
> **Saya ingin** mengonversi input nominal rupiah langsung menjadi berat kilogram pada keranjang kasir,  
> **Agar** saya dapat melayani transaksi eceran konsumen secara cepat tanpa menghitung kalkulator manual.

- **Acceptance Criteria 1.1: Konversi Pecahan Tepat**
  - **Given** Kasir berada pada antarmuka kasir dan memilih produk "Beras Rojo Lele" seharga Rp 14.000 / kg.
  - **When** Kasir menekan tombol "Beli Rp" dan memasukkan nominal `35000`.
  - **Then** Sistem secara otomatis memasukkan item ke keranjang belanja dengan kuantitas `2.50` kg dan subtotal `Rp 35.000`.
- **Acceptance Criteria 1.2: Validasi Nilai Input**
  - **Given** Kasir berada pada modal dialog "Beli Rp".
  - **When** Kasir menginput nominal belanja `0` atau angka negatif.
  - **Then** Sistem menonaktifkan tombol konfirmasi dan menampilkan notifikasi validasi bahwa nominal harus lebih dari 0.

---

### US-02: Transaksi Tukar Tabung Gas Konsumen (Kasir)
> **Sebagai** Kasir Toko,  
> **Saya ingin** mencatat transaksi penukaran tabung gas LPG konsumen secara instan dari meja kasir,  
> **Agar** stok tabung isi berkurang, stok tabung kosong bertambah, dan pembayaran gas tercatat ke dalam kas penjualan.

- **Acceptance Criteria 2.1: Ketersediaan Tabung Isi Mencukupi**
  - **Given** Gas LPG 3 KG memiliki stok tabung isi 15 dan tabung kosong 5.
  - **When** Kasir memilih transaksi tukar sebanyak 2 tabung dengan total tagihan Rp 44.000 secara tunai.
  - **Then** Sistem menerbitkan nota, mengurangi stok isi menjadi 13 tabung, menambah stok kosong menjadi 7 tabung, dan total aset fisik tabung tetap 20.
- **Acceptance Criteria 2.2: Ketersediaan Tabung Isi Kosong / Habis**
  - **Given** Gas LPG 3 KG memiliki stok tabung isi 0.
  - **When** Kasir mencoba memasukkan transaksi tukar tabung gas ke keranjang belanja.
  - **Then** Sistem menolak aksi tersebut dan memunculkan peringatan bahwa persediaan tabung isi habis.

---

### US-03: Penerimaan Barang Masuk & Rekalkulasi HPP Tertimbang (Admin)
> **Sebagai** Pemilik Usaha (Admin),  
> **Saya ingin** mencatat pasokan barang masuk dalam kemasan karung dengan harga beli grosir terbaru,  
> **Agar** persediaan kilogram bertambah dan Harga Pokok Penjualan (HPP) diperbarui secara rata-rata tertimbang.

- **Acceptance Criteria 3.1: Perhitungan HPP Rata-Rata Tertimbang**
  - **Given** Persediaan beras toko saat ini 100 kg dengan HPP Rp 12.000/kg (total nilai modal = Rp 1.200.000).
  - **When** Admin mencatat pasokan masuk 2 karung (konversi 1 karung = 50 kg, total 100 kg) seharga Rp 14.000/kg (total beli Rp 1.400.000).
  - **Then** Sistem memperbarui stok menjadi 200 kg dan mengkalkulasi HPP baru menjadi tepat Rp 13.000/kg:
    $$\text{HPP Baru} = \frac{1.200.000 + 1.400.000}{100 + 100} = \text{Rp } 13.000/\text{kg}$$
- **Acceptance Criteria 3.2: Penolakan Input Data Negatif**
  - **Given** Admin membuka form penerimaan barang masuk.
  - **When** Admin mengisi harga beli `-1000` atau kuantitas `0`.
  - **Then** Sistem memblokir penyimpanan data dan menandai kolom input dengan indikator kesalahan merah.

---

### US-04: Transaksi Sirkulasi Tabung Gas Agen 2 Tahap (Admin)
> **Sebagai** Pemilik Usaha (Admin),  
> **Saya ingin** mencatat pengiriman tabung kosong ke agen dan penerimaan tabung isi dari agen secara bertahap,  
> **Agar** perputaran tabung di pihak agen penyalur terpantau jelas dan tidak ada tabung yang hilang.

- **Acceptance Criteria 4.1: Tahap 1 - Kirim Tabung Kosong**
  - **Given** Toko memiliki 30 tabung kosong dan total tabung di toko 50.
  - **When** Admin mencatat pengiriman 20 tabung kosong ke agen Pertamina.
  - **Then** Stok kosong toko berkurang menjadi 10, total tabung fisik di toko berkurang menjadi 30, dan riwayat mencatat 20 tabung sedang beredar di agen.
- **Acceptance Criteria 4.2: Tahap 2 - Terima Tabung Isi**
  - **Given** Admin menerima pasokan 20 tabung isi dari agen pengganti tabung kosong yang dikirim sebelumnya.
  - **When** Admin mencatat transaksi terima tabung isi 20 buah beserta biaya pengadaan per tabung.
  - **Then** Stok tabung isi toko bertambah 20, total tabung di toko kembali seimbang menjadi 50, dan beban pembelian tercatat ke tabel pengeluaran toko.

---

### US-05: Laporan Laba Rugi Riil & Ekspor Berkas (Admin)
> **Sebagai** Pemilik Usaha (Admin),  
> **Saya ingin** melihat ringkasan keuangan laba bersih dan mengunduh laporan penjualan dalam format Excel (.xlsx),  
> **Agar** saya memiliki arsip pembukuan resmi bulanan untuk evaluasi kinerja bisnis toko.

- **Acceptance Criteria 5.1: Agregasi Laba Bersih Presisi**
  - **Given** Toko mencatat penjualan omzet Rp 10.000.000, total HPP modal Rp 8.000.000, beban operasional listrik Rp 500.000, dan kas ekstra Rp 200.000.
  - **When** Admin membuka laporan keuangan periode terkait.
  - **Then** Sistem menampilkan Laba Kotor Rp 2.000.000 dan Laba Bersih riil tepat Rp 1.700.000:
    $$\text{Laba Bersih} = (\text{Omzet} - \text{HPP}) + \text{Kas Ekstra} - \text{Beban Operasional}$$
- **Acceptance Criteria 5.2: Ekspor Berkas Excel**
  - **Given** Admin memilih laporan Penjualan periode "Bulan Ini".
  - **When** Admin mengklik tombol "Ekspor Excel".
  - **Then** Sistem memunculkan jendela dialog Windows dan menghasilkan berkas `.xlsx` terstruktur yang valid.

---

## 3.4 Kebutuhan Nonfungsional (Non-Functional Requirements)

| ID NFR | Quality Attribute | Requirement Definition | Scope / How (Mekanisme Teknis Pemenuhan) |
| :---: | :--- | :--- | :--- |
| **NFR-01** | **Keamanan (Security)** | Password pengguna tidak boleh disimpan dalam teks polos (*plaintext*) dan data sesi harus terlindungi. | Menggunakan algoritma enkripsi satu arah `scrypt` modul crypto Node.js native dengan penambahan *random salt* 16-byte unik per akun. |
| **NFR-02** | **Isolasi Arsitektur** | Antarmuka browser tidak boleh mengakses langsung API OS atau modul native Node.js. | Menetapkan konfigurasi `contextIsolation: true` dan `nodeIntegration: false` pada Electron Browser Window, di mana komunikasi dijembatani melalui `preload.js`. |
| **NFR-03** | **Kinerja (Performance)** | Pencarian produk dan eksekusi transaksi kasir harus responsif demi menghindari penumpukan antrean. | Waktu respons kueri pencarian produk katalog $\le 100\text{ ms}$ melalui indeks SQLite (`idx_products_category`, `idx_transactions_date`). |
| **NFR-04** | **Integritas Data (ACID)** | Saldo stok fisik dan pencatatan kas tidak boleh korup jika komputer mati mendadak saat transaksi berlangsung. | Seluruh pemrosesan mutasi kasir dan mutasi gas dibungkus di dalam transaksi atomik `db.transaction(...)` engine `better-sqlite3`. |
| **NFR-05** | **Ketersediaan (Offline-First)** | Sistem kasir harus beroperasi penuh 100% tanpa jaringan internet. | Menggunakan basis data relasional SQLite lokal berkas tunggal (`app.db`) di direktori sistem pengguna (`userData`). |
| **NFR-06** | **Portabilitas & Deployment** | Aplikasi harus mudah dipasang pada sistem operasi komputer toko standar pengguna awam. | Dikemas menggunakan `electron-builder` menjadi installer tunggal Windows NSIS (`.exe`) mandiri yang mencakup seluruh dependensi native. |
| **NFR-07** | **Kegunaan (Usability)** | Tampilan antarmuka kasir harus ergonomis dan mendukung pengoperasian keyboard minimal. | Menggunakan Custom CSS Design System dengan kontras tinggi, tata letak keypad angka kasir yang ramah sentuh/klik, dan feedback modal yang jelas. |

---

## 3.5 Matriks Kategori Prioritas Kebutuhan Fungsional

Mengacu pada template penugasan perkuliahan (Pertemuan 4 Slide 22–25):

| No | Kebutuhan / User Story | High Priority | Medium Priority | Low Priority | No Priority |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Autentikasi (US-05)** | Login kredensial & hak akses role (`admin`/`kasir`). | Fitur ubah kata sandi pengguna mandiri. | Pengaturan foto profil staf kasir. | Login biometrik / sidik jari dan Single Sign-On (SSO). |
| **2** | **Kasir Ritel (US-01)** | Pencarian produk, keranjang, hitung tunai, dan potong stok. | Fitur "Beli Rp", input kuantitas pecahan, dan multi-metode (QRIS). | Fitur diskon persentase dan diskon nominal per nota. | Rekomendasi belanja cerdas berbasis AI. |
| **3** | **Sirkulasi Gas (US-02, US-04)**| Manajemen *dual-stock* dan transaksi tukar konsumen kasir. | Transaksi tukar agen 2 tahap (kirim/terima) dan jual tabung perdana. | Riwayat riil mutasi log pergeseran tabung dan opname fisik. | Pelacakan tabung berbasis RFID / barcode individual. |
| **4** | **Logistik & HPP (US-03)** | Pencatatan barang masuk dan penambahan stok dasar (kg). | Rekalkulasi HPP rata-rata tertimbang (*Moving Average*) otomatis. | Pencatatan barang keluar non-penjualan (rusak, hilang, retur, pribadi). | Notifikasi otomatis order pasokan via WhatsApp API. |
| **5** | **Keuangan & Laporan (US-05)** | Pencatatan pengeluaran operasional & hitung omzet kasir. | Laporan Laba Bersih riil (Omzet - HPP - Operasional) dan filter periode. | Fitur ekspor berkas ke Excel (.xlsx) dan dokumen cetak PDF (.pdf). | Integrasi pelaporan pajak online ke server Dirjen Pajak. |
| **6** | **Hardware & Cetak (US-01)** | Pratinjau struk kasir di layar monitor. | Cetak struk 80mm via Windows Print Spooler. | Direct raw socket ESC/POS printing via port TCP 9100. | Pengiriman nota digital otomatis via SMS/Email. |
| **7** | **Pemeliharaan Data** | Penyimpanan basis data lokal SQLite terenkripsi ACID. | Fitur backup database manual menjadi file `.db` arsip. | Fitur restore database dengan validasi berkas cadangan. | Sinkronisasi multi-toko otomatis ke database cloud. |
