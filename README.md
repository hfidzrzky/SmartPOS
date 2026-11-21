# SmartPOS: Sistem Kasir dan Manajemen Usaha (Beras, Telur, dan Gas LPG)

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-0078D4?style=flat)](https://nodejs.org)
[![Electron](https://img.shields.io/badge/Electron-31.x-47848F?style=flat&logo=electron&logoColor=white)](https://electronjs.org/)
[![Database](https://img.shields.io/badge/Database-SQLite%203%20(better--sqlite3)-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=flat)](LICENSE)

Sistem informasi Point of Sale (POS) dan manajemen inventaris berbasis desktop dengan arsitektur offline-first. Aplikasi ini dirancang khusus untuk memfasilitasi operasional usaha mikro, kecil, dan menengah (UMKM) pada sektor kebutuhan pokok dan pangkalan gas LPG.

Sistem dibangun menggunakan Electron, SQLite (better-sqlite3), dan Vanilla JavaScript tanpa ketergantungan koneksi internet, server pihak ketiga, maupun database cloud.

---

## 1. Latar Belakang dan Permasalahan yang Diselesaikan

Aplikasi POS ritel pada umumnya dirancang untuk komoditas barang jadi berbasis unit bulat dan pemindaian barcode. Pendekatan tersebut tidak memadai untuk proses bisnis toko kebutuhan pokok dan pangkalan gas karena beberapa kendala mendasar:

1. **Pelacakan Aset Tabung Gas (Dual-Stock Management)**  
   Penjualan gas LPG melibatkan pengelolaan aset wadah (tabung). Sistem kasir konvensional kerap menimbulkan selisih hitung karena tidak memisahkan stok tabung isi dan tabung kosong. SmartPOS mengimplementasikan pelacakan sirkulasi tabung secara tertutup: transaksi tukar konsumen, pengiriman tabung kosong ke agen, penerimaan tabung isi dari agen, penjualan tabung baru (tanpa tukar), dan penyesuaian fisik.

2. **Transaksi Eceran Dinamis dan Kuantitas Pecahan**  
   Konsumen komoditas pokok sering melakukan pembelian berdasarkan anggaran nominal uang (contoh: "beli beras Rp 15.000") atau satuan berat fraksional (contoh: 0,25 kg atau 0,5 kg telur). Sistem ini menyediakan fungsi konversi otomatis dari nilai rupiah ke kuantitas desimal, serta mendukung input kuantitas pecahan desimal secara langsung.

3. **Multi-Satuan dan Harga Pokok Penjualan (HPP) Tertimbang**  
   Pengadaan barang sering dilakukan dalam kemasan karung (misalnya 25 kg atau 50 kg), sementara penjualan dilakukan dalam kilogram eceran maupun karungan. Sistem mengelola konversi satuan dasar serta menghitung HPP rata-rata tertimbang (*weighted average cost*) saat terjadi pengadaan baru.

4. **Kemandirian Infrastruktur (Offline-First)**  
   Banyak pangkalan dan toko sembako beroperasi di lingkungan dengan koneksi internet terbatas dan memerlukan sistem yang bebas biaya langganan berkala. Seluruh data transaksi, katalog, dan keuangan disimpan secara lokal di mesin pengguna dalam berkas SQLite terenkripsi pada level integritas ACID.

5. **Pemisahan Arus Kas dan Pencatatan Kerugian Fisik**  
   Sistem memfasilitasi pencatatan barang rusak, susut, retur, atau pemakaian pribadi, serta mencatat pengeluaran operasional di luar pengadaan barang untuk menghasilkan laporan laba-rugi riil.

---

## 2. Fitur Utama Sistem

### Modul Kasir (Point of Sale)
- Antarmuka pencarian cepat dan keranjang transaksi responsif.
- Fitur kalkulasi otomatis "Beli Rp" untuk konversi instan dari nominal uang ke berat kilogram.
- Dukungan kuantitas desimal (pecahan) untuk komoditas timbangan.
- Multi-metode pembayaran: Tunai, Transfer Bank, dan QRIS.
- Perhitungan kembalian dan diskon transaksi.
- Pratinjau dan pencetakan nota kasir berukuran 80 mm.

### Modul Manajemen Gas LPG
- Pemisahan data kuantitas Tabung Isi, Tabung Kosong, dan Total Tabung per varian gas.
- Transaksi Tukar Konsumen: mengurangi stok isi dan menambah stok kosong tanpa mengubah total aset fisik.
- Transaksi Tukar Agen (2 Tahap):
  - Pengiriman tabung kosong ke agen (mengurangi stok kosong dan total tabung di toko).
  - Penerimaan tabung isi dari agen (menambah stok isi dan total tabung di toko).
- Penjualan Tanpa Tukar: penjualan tabung perdana beserta isinya.
- Penambahan Tabung Baru dan Penyesuaian Selisih Fisik.
- Riwayat lengkap mutasi gas per varian tabung.

### Modul Produk dan Inventaris
- Manajemen katalog komoditas beras, telur, dan gas LPG.
- Pengaturan unit primer (kg/tabung) dan unit sekunder (karung) dengan faktor konversi dan harga khusus.
- Batas stok minimum dengan penanda visual otomatis saat persediaan menipis.

### Modul Logistik (Barang Masuk dan Keluar)
- Pencatatan penerimaan stok dari pemasok disertai pembaruan HPP tertimbang.
- Pencatatan barang keluar non-penjualan (rusak, hilang, retur, penggunaan pribadi).
- Audit trail mutasi stok dengan rekam data stok sebelum dan sesudah mutasi.

### Modul Keuangan dan Dashboard
- Agregasi pendapatan dari transaksi kasir dan pos pendapatan lain.
- Pencatatan biaya operasional toko secara rinci.
- Perhitungan Laba Bersih riil (Pendapatan - HPP Barang Terjual - Biaya Operasional).
- Visualisasi grafik analitik harian dan bulanan menggunakan Chart.js.

### Modul Laporan dan Ekspor
- 6 jenis laporan: Penjualan, Persediaan Stok, Laporan Keuangan, Sirkulasi Gas, Barang Masuk, dan Barang Keluar.
- Filter berdasarkan rentang waktu dan preset periode (hari ini, minggu ini, bulan ini, tahun ini).
- Fitur ekspor data ke format spreadsheet Excel (.xlsx) dan dokumen cetak PDF (.pdf).

### Modul Pengaturan, Keamanan, dan Pemeliharaan
- Konfigurasi identitas toko, kontak, dan catatan kaki pada struk.
- Manajemen pengguna dengan sistem Role-Based Access Control (Admin dan Kasir).
- Hashing kata sandi menggunakan algoritma kriptografi scrypt dengan salt acak.
- Utilitas backup dan restore database lokal untuk keamanan cadangan data.

---

## 3. Arsitektur Teknis dan Spesifikasi Perangkat Lunak

### Stack Teknologi
- **Runtime Environment**: Electron 31 (Node.js 20+ & Chromium)
- **Database Engine**: SQLite 3 via `better-sqlite3` v11 (native binding C++)
- **Frontend Layer**: HTML5, Vanilla JavaScript (ES6+), Modern Custom CSS Design System
- **Komponen Ekspor**: `exceljs` v4, `pdfkit` v0.15
- **Visualisasi Data**: `chart.js` v4
- **Build & Packaging**: `electron-builder` v24

### Keamanan Arsitektur Electron
- `contextIsolation: true` dan `nodeIntegration: false` diterapkan pada jendela browser utama. Renderer tidak memiliki akses langsung ke modul Node.js, sistem berkas OS, maupun koneksi database langsung.
- Komunikasi antara renderer dan proses utama diisolasi melalui `preload.js` menggunakan `contextBridge` dan protokol IPC asinkron (`ipcMain.handle` / `ipcRenderer.invoke`).
- Seluruh mutasi kasir dan pergeseran stok gas dieksekusi di dalam transaksi SQLite atomik (`db.transaction`), menjamin konsistensi data (ACID) jika terjadi interupsi proses di tengah transaksi.

---

## 4. Persyaratan Sistem dan Instalasi

### Persyaratan Lingkungan
- Node.js versi 18 LTS atau lebih baru.
- Sistem Operasi: Windows 10/11, macOS 11+, atau distribusi Linux modern.
- Kompiler C++ untuk pembangunan modul native `better-sqlite3`:
  - **Windows**: Visual Studio Build Tools ("Desktop development with C++").
  - **macOS**: Xcode Command Line Tools (`xcode-select --install`).
  - **Linux**: Paket `build-essential` dan `python3`.

### Prosedur Instalasi
1. Kloning atau unduh repositori proyek ke direktori lokal:
   ```bash
   git clone https://github.com/username/SmartPOS.git
   cd SmartPOS
   ```

2. Unduh paket dependensi dan kompilasi modul native:
   ```bash
   npm install
   ```
   *Catatan: Perintah ini secara otomatis menjalankan `electron-rebuild` via skrip `postinstall`.*

---

## 5. Menjalankan Aplikasi

Jalankan perintah berikut pada terminal kerja:

```bash
npm start
```

Untuk menjalankan aplikasi dalam mode pengembang dengan konsol DevTools terbuka:

```bash
npm start -- --dev
```

### Kredensial Bawaan (Default Accounts)

Saat aplikasi dijalankan untuk pertama kali, sistem otomatis menginisialisasi dua akun default:

| Role | Username | Password Default | Hak Akses |
| :--- | :--- | :--- | :--- |
| Admin | `admin` | `admin123` | Akses penuh seluruh modul dan pengaturan |
| Kasir | `kasir` | `kasir123` | Akses terbatas pada kasir dan riwayat transaksi |

*Disarankan untuk segera memperbarui kata sandi melalui menu Pengaturan setelah sesi login pertama.*

---

## 6. Penyimpanan dan Integritas Database

Database SQLite (`app.db`) disimpan secara terpisah dari folder instalasi/kode sumber untuk mencegah tertimpa saat proses pembaruan atau build ulang:

- **Windows**: `%APPDATA%/kasir-usaha-desktop/database/app.db`
- **macOS**: `~/Library/Application Support/kasir-usaha-desktop/database/app.db`
- **Linux**: `~/.config/kasir-usaha-desktop/database/app.db`

Lokasi berkas ini dapat dibuka langsung dari dalam aplikasi melalui menu **Pengaturan > Buka Lokasi File**.

---

## 7. Integrasi Perangkat Cetak (Thermal Printer)

Format nota transaksi dioptimalkan untuk kertas struk thermal standar 80 mm. Sistem mendukung dua mekanisme pencetakan:

1. **Windows Print Spooler (Default)**  
   Mengirim dokumen nota ke driver printer yang telah terpasang di sistem operasi Windows (koneksi USB, Bluetooth, atau LAN).
2. **Direct ESC/POS Raw Socket**  
   Mengirim instruksi perintah cetak ESC/POS mentah secara langsung melalui antarmuka jaringan TCP/IP (Port standar 9100) atau port serial terkonfigurasi.

### Panduan Operasional Pencetakan:
1. Hubungkan printer thermal ke komputer dan pastikan status printer aktif pada daftar perangkat Windows.
2. Buka menu **Pengaturan > Pengaturan Printer** di dalam aplikasi, pilih mode pencetakan yang sesuai, lalu pilih nama printer target.
3. Selesaikan transaksi pada halaman Kasir dan klik **Cetak Struk**.

---

## 8. Struktur Direktori Proyek

```
SmartPOS/
|-- main.js                 # Electron process main, manajemen window, dan handler IPC
|-- preload.js              # Jembatan contextBridge aman antara renderer dan proses utama
|-- package.json            # Konfigurasi dependensi dan skrip build
|-- database/
|   |-- schema.sql          # DDL struktur tabel dan indeks relasional SQLite
|   |-- db.js               # Inisialisasi koneksi basis data dan pembuatan data awal
|   |-- auth.js             # Verifikasi login, hashing scrypt, dan otorisasi pengguna
|   |-- products.js         # Operasi CRUD produk dan sinkronisasi stok kg/karung
|   |-- gas.js              # State machine sirkulasi tabung gas (isi, kosong, total)
|   |-- stock.js            # Logika pencatatan barang masuk dan keluar
|   |-- transactions.js     # Logika checkout kasir dengan transaksi atomik SQLite
|   |-- finance.js          # Pengelolaan pengeluaran dan perhitungan laba bersih
|   |-- dashboard.js        # Kueri statistik KPI dan pembentukan data grafik Chart.js
|   |-- reports.js          # Agregasi data laporan bersyarat periode
|   |-- export.js           # Mesin konversi data ke format Excel dan PDF
|   |-- settings.js         # Pengelolaan konfigurasi profil toko dan perangkat printer
|   |-- backup.js           # Fungsi cadangkan dan pulihkan berkas database SQLite
|   `-- helpers.js          # Utilitas format mata uang, tanggal, dan nomor faktur
|-- renderer/
|   |-- css/app.css         # Lembar gaya antarmuka pengguna
|   |-- js/common.js        # Utilitas antarmuka bersama (modal, notifikasi toast, format)
|   |-- js/*.js             # Berkas pengendali logika masing-masing halaman antarmuka
|   `-- pages/*.html        # Halaman-halaman modular antarmuka aplikasi
`-- assets/                 # Berkas ikon dan aset statis sistem
```

---

## 9. Kompilasi Paket Distribusi (Build Installer)

Untuk mengemas aplikasi menjadi berkas instalasi mandiri yang siap dipasang pada komputer target tanpa membutuhkan instalasi Node.js:

```bash
npm run dist
```

Hasil paket instalasi yang dapat didistribusikan (.exe untuk Windows, .dmg untuk macOS, atau .AppImage untuk Linux) akan digenerasikan pada direktori `dist/`.

---

## 10. Lisensi

Proyek ini dirilis dan didistribusikan di bawah lisensi [MIT](LICENSE).
