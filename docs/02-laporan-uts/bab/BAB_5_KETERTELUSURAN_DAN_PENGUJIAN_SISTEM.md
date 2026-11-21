# BAB V: KETERTELUSURAN KEBUTUHAN & PENGUJIAN SISTEM

---

## 5.1 Konsep Ketertelusuran Kebutuhan (Requirements Traceability)
Ketertelusuran Kebutuhan (*Requirements Traceability*) adalah metodologi rekayasa perangkat lunak untuk menjaga mata rantai hubungan dua arah (*bidirectional traceability*) dari kebutuhan pengguna, perancangan model, implementasi kode, hingga verifikasi pengujian:

```
[Requirement ID (FR)]  <──>  [User Story (US)]
          ▲                         ▲
          │                         │
          ▼                         ▼
   [Use Case (UC)]     <──>  [Model Proses (DFD/Activity)]
          ▲                         ▲
          │                         │
          ▼                         ▼
 [Antarmuka UI/Code]   <──>  [Test Case ID (TC)]
```

Implementasi RTM pada SmartPOS membuktikan bahwa:
1. Tidak ada spesifikasi kebutuhan yang tidak memiliki kode implementasi (*no missing requirements*).
2. Tidak ada kode implementasi fungsional yang dibuat tanpa dasar kebutuhan pengguna (*no gold plating*).
3. Seluruh kebutuhan fungsional memiliki instrumen pengujian yang valid dan dapat diuji ulang (*testable*).

---

## 5.2 Matriks Ketertelusuran Kebutuhan (Requirements Traceability Matrix)

| Req ID | User Story ID | Use Case ID | Model Proses (DFD / Activity) | Komponen UI & Kode Implementasi | Test Case ID | Status Pemenuhan |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| **FR-01** | US-05 | UC-01 | DFD 1.0 (Autentikasi) | `pages/login.html`, `database/auth.js` | **TC-01** | Terpenuhi (Verified) |
| **FR-02** | US-05 | UC-15 | DFD 1.0 (Manajemen User) | `pages/settings.html`, `js/settings.js` | **TC-02** | Terpenuhi (Verified) |
| **FR-03** | US-01 | UC-06 | DFD 2.0 (Katalog Produk) | `pages/products.html`, `database/products.js`| **TC-03** | Terpenuhi (Verified) |
| **FR-04** | US-01 | UC-02 | DFD 3.0 & Activity Kasir | `pages/kasir.html`, `database/transactions.js`| **TC-04** | Terpenuhi (Verified) |
| **FR-05** | US-01 | UC-03 | DFD 3.0 & Activity Beli Rp | `js/kasir.js` (`handleBeliRp()`) | **TC-05** | Terpenuhi (Verified) |
| **FR-06** | US-01 | UC-02 | DFD 3.0 (Validasi Bayar) | `js/kasir.js` (`processPayment()`) | **TC-06** | Terpenuhi (Verified) |
| **FR-07** | US-01 | UC-04 | DFD 3.0 (Cetak Struk) | `main.js` (IPC `receipt:print`) | **TC-07** | Terpenuhi (Verified) |
| **FR-08** | US-01 | UC-16 | DFD 3.0 (Void Transaksi) | `pages/reports.html`, `database/transactions.js`| **TC-08** | Terpenuhi (Verified) |
| **FR-09** | US-02 | UC-05 | DFD 4.0 (Dual-Stock Gas) | `database/gas.js`, `database/schema.sql` | **TC-09** | Terpenuhi (Verified) |
| **FR-10** | US-02 | UC-05 | DFD 4.0 (Tukar Konsumen) | `pages/kasir.html`, `pages/gas.html` | **TC-10** | Terpenuhi (Verified) |
| **FR-11** | US-04 | UC-07 | DFD 4.0 (Kirim Agen) | `pages/gas.html`, `js/gas.js` | **TC-11** | Terpenuhi (Verified) |
| **FR-12** | US-04 | UC-07 | DFD 4.0 (Terima Agen) | `pages/gas.html`, `js/gas.js` | **TC-12** | Terpenuhi (Verified) |
| **FR-13** | US-02 | UC-05 | DFD 4.0 (Jual Perdana) | `pages/kasir.html`, `database/gas.js` | **TC-13** | Terpenuhi (Verified) |
| **FR-14** | US-04 | UC-08 | DFD 4.0 (Opname Gas) | `pages/gas.html`, `database/gas.js` | **TC-14** | Terpenuhi (Verified) |
| **FR-15** | US-03 | UC-09 | DFD 5.0 & Activity Masuk | `pages/stock-in.html`, `database/stock.js` | **TC-15** | Terpenuhi (Verified) |
| **FR-16** | US-03 | UC-10 | DFD 5.0 (Barang Keluar) | `pages/stock-out.html`, `database/stock.js` | **TC-16** | Terpenuhi (Verified) |
| **FR-17** | US-05 | UC-11 | DFD 6.0 (Finansial Toko) | `pages/finance.html`, `database/finance.js` | **TC-17** | Terpenuhi (Verified) |
| **FR-18** | US-05 | UC-12 | DFD 6.0 (Dashboard Laba) | `pages/dashboard.html`, `database/dashboard.js`| **TC-18** | Terpenuhi (Verified) |
| **FR-19** | US-05 | UC-13 | DFD 7.0 (Laporan & Ekspor)| `pages/reports.html`, `database/export.js` | **TC-19** | Terpenuhi (Verified) |
| **FR-20** | US-05 | UC-14 | DFD 7.0 (Backup Restore) | `pages/settings.html`, `database/backup.js` | **TC-20** | Terpenuhi (Verified) |

---

## 5.3 Rencana dan Skenario Pengujian Black-Box (Black-Box Test Cases)

Pengujian sistem menggunakan metode *Black-Box Testing* dengan teknik *Equivalence Partitioning* dan *Boundary Value Analysis* untuk memverifikasi fungsionalitas terhadap spesifikasi tanpa mengasumsikan struktur internal baris kode.

### TC-01: Verifikasi Autentikasi Pengguna & Role-Based Access Control
- **Target Kebutuhan**: FR-01, FR-02 (US-05)
- **Tujuan Uji**: Memastikan hanya pengguna aktif dengan kredensial valid yang dapat masuk, dan hak akses antarmuka dibatasi sesuai peran (`admin` vs `kasir`).
- **Prasyarat**: Sistem memiliki akun `admin` (role admin) dan `kasir` (role kasir).

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-01.1** | Masukkan username dan password valid role kasir. | Username: `kasir`<br>Password: `kasir123` | Sistem berhasil login, membuka halaman kasir, dan menyembunyikan menu Admin (Pengaturan & Manajemen User). | **PASS** |
| **TC-01.2** | Masukkan password salah pada username admin. | Username: `admin`<br>Password: `salah123` | Sistem menolak login dan menampilkan pesan *"Username atau password salah"*. | **PASS** |
| **TC-01.3** | Percobaan login dengan akun berstatus dinonaktifkan (`active = 0`). | Akun nonaktif | Sistem menolak login dengan pesan *"Akun dinonaktifkan, hubungi admin"*. | **PASS** |

---

### TC-05: Verifikasi Fitur Konversi Otomatis "Beli Rp" ke Kuantitas Pecahan
- **Target Kebutuhan**: FR-04, FR-05 (US-01)
- **Tujuan Uji**: Menguji akurasi matematis konversi nilai nominal rupiah belanja menjadi berat kilogram desimal pada komoditas sembako.
- **Prasyarat**: Produk "Beras Ramos" aktif dengan harga Rp 14.000 / kg.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-05.1** | Kasir memilih beras Ramos, klik tombol "Beli Rp", dan input nominal pas kelipatan harga. | Nominal: `Rp 28.000` | Sistem memasukkan item ke keranjang dengan kuantitas tepat `2.00` kg dan subtotal `Rp 28.000`. | **PASS** |
| **TC-05.2** | Kasir input nominal rupiah yang menghasilkan angka pecahan desimal berulang. | Nominal: `Rp 10.000`<br>(Harga: Rp 14.000/kg) | Sistem menghitung kuantitas menjadi `0.71` kg dan mengunci subtotal tepat `Rp 10.000` tanpa selisih hitung uang. | **PASS** |
| **TC-05.3** | Kasir menginput nominal 0 atau angka negatif pada modal "Beli Rp". | Nominal: `-5000` atau `0` | Tombol konfirmasi dinonaktifkan / sistem menampilkan pesan *"Nominal harus lebih dari 0"*. | **PASS** |

---

### TC-06: Verifikasi Checkout Pembayaran Tunai & Validasi Kembalian
- **Target Kebutuhan**: FR-04, FR-06 (US-01)
- **Tujuan Uji**: Memverifikasi validasi nominal uang bayar, perhitungan uang kembalian, pemotongan stok otomatis, dan penerbitan nota transaksi.
- **Prasyarat**: Keranjang belanja berisi total tagihan Rp 75.000. Stok produk di database = 50 kg.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-06.1** | Kasir memasukkan uang tunai lebih besar dari total tagihan. | Uang Diterima: `Rp 100.000` | Sistem menghitung kembalian tepat `Rp 25.000`, transaksi berhasil disimpan, stok produk berkurang menjadi 45 kg. | **PASS** |
| **TC-06.2** | Kasir memasukkan uang tunai pas sesuai total tagihan. | Uang Diterima: `Rp 75.000` | Sistem mencatat kembalian `Rp 0`, status transaksi selesai, nomor invoice unik terbit. | **PASS** |
| **TC-06.3** | Kasir memasukkan uang tunai kurang dari total tagihan dan menekan tombol konfirmasi. | Uang Diterima: `Rp 50.000` | Sistem memblokir proses checkout dan menampilkan notifikasi *"Uang pembayaran kurang Rp 25.000"*. | **PASS** |

---

### TC-10: Verifikasi Transaksi Tukar Tabung Gas Konsumen (Dual-Stock Closed Loop)
- **Target Kebutuhan**: FR-09, FR-10 (US-02)
- **Tujuan Uji**: Memastikan mutasi stok tabung isi berkurang, tabung kosong bertambah, dan total aset tabung fisik di toko tetap seimbang secara tertutup.
- **Prasyarat**: Gas LPG 3 KG memiliki saldo awal: `filled_stock = 25`, `empty_stock = 15`, `total_cylinders = 40`.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-10.1** | Kasir memproses transaksi tukar konsumen sebanyak 5 tabung gas 3 kg tunai. | Qty: `5 tabung`<br>Harga: Rp 22.000 | Saldo baru: `filled_stock = 20`, `empty_stock = 20`, `total_cylinders = 40`. Riwayat tercatat di `gas_transactions`. | **PASS** |
| **TC-10.2** | Kasir mencoba memproses tukar gas melebihi jumlah tabung isi yang tersedia. | Qty: `30 tabung`<br>(Stok isi hanya 20) | Sistem menolak transaksi dengan notifikasi *"Stok tabung isi tidak mencukupi"*, tidak ada mutasi stok. | **PASS** |

---

### TC-11 & 12: Verifikasi Sirkulasi Tabung Gas Agen 2-Tahap
- **Target Kebutuhan**: FR-11, FR-12 (US-04)
- **Tujuan Uji**: Menguji alur logistik pengiriman tabung kosong ke agen dan penerimaan kembali tabung isi beserta pencatatan beban modal beli.
- **Prasyarat**: Saldo toko: `filled = 10`, `empty = 30`, `total = 40`.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-11.1** | **Tahap 1: Kirim Kosong**<br>Admin mencatat pengiriman 25 tabung kosong ke agen. | Qty Kirim: `25 tabung` | Saldo toko: `empty = 5`, `total = 15`. Log mencatat 25 tabung berstatus sedang dikirim ke agen. | **PASS** |
| **TC-12.1** | **Tahap 2: Terima Isi**<br>Admin mencatat penerimaan 25 tabung isi dari agen seharga Rp 19.000/tabung. | Qty Terima: `25 tabung`<br>Total Beli: Rp 475.000 | Saldo toko: `filled = 35`, `total = 40`. Tabel `expenses` otomatis mencatat beban pembelian gas Rp 475.000. | **PASS** |

---

### TC-15: Verifikasi Barang Masuk & Algoritma HPP Rata-Rata Tertimbang
- **Target Kebutuhan**: FR-15 (US-03)
- **Tujuan Uji**: Memastikan perhitungan HPP tertimbang diperbarui secara akurat saat terjadi pengadaan barang baru dengan harga beli berbeda.
- **Prasyarat**: Beras Rojo Lele memiliki stok awal 100 kg dengan HPP Rp 12.000/kg (Nilai modal persediaan = Rp 1.200.000).

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-15.1** | Admin mencatat pasokan masuk 1 karung (konversi 1 karung = 50 kg) dengan harga beli baru Rp 15.000/kg (total beli Rp 750.000). | Qty: `1 karung` (50 kg)<br>Harga Beli: `Rp 15.000` | Stok baru menjadi `150 kg`. HPP baru dihitung secara rata-rata tertimbang menjadi tepat `Rp 13.000 / kg`: $$\frac{1.200.000 + 750.000}{100 + 50} = \text{Rp } 13.000$$ | **PASS** |
| **TC-15.2** | Admin input data barang masuk dengan kuantitas 0 atau harga beli negatif. | Qty: `0` atau Harga: `-1000` | Sistem menolak input dan menampilkan pesan validasi error. | **PASS** |

---

### TC-18 & 19: Verifikasi Modul Finansial & Mesin Ekspor Data
- **Target Kebutuhan**: FR-17, FR-18, FR-19 (US-05)
- **Tujuan Uji**: Menguji akurasi agregasi Laba Bersih riil dan pembuatan berkas laporan eksternal (.xlsx dan .pdf).
- **Prasyarat**: Toko memiliki data penjualan omzet Rp 5.000.000, HPP total Rp 4.000.000, dan biaya listrik Rp 300.000.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-18.1** | Admin membuka halaman Ringkasan Finansial Toko. | Filter: Bulan Berjalan | Sistem menampilkan Omzet Rp 5.000.000, Laba Kotor Rp 1.000.000, dan Laba Bersih tepat `Rp 700.000`. | **PASS** |
| **TC-19.1** | Admin menekan tombol "Ekspor Excel" pada laporan Penjualan. | Format: Excel (.xlsx) | Sistem memunculkan jendela Save File dan menghasilkan berkas `.xlsx` valid yang dapat dibuka sempurna di Microsoft Excel. | **PASS** |
| **TC-19.2** | Admin menekan tombol "Ekspor PDF" pada laporan Sirkulasi Gas. | Format: PDF (.pdf) | Berkas `.pdf` berhasil di-generate dengan layout tabel rapi dan header identitas toko yang sesuai. | **PASS** |

---

### TC-20: Verifikasi Backup dan Restore Basis Data SQLite
- **Target Kebutuhan**: FR-20 (US-05)
- **Tujuan Uji**: Memastikan keandalan utilitas pencadangan dan pemulihan data lokal demi mencegah kehilangan data (*disaster recovery*).
- **Prasyarat**: Database operasional terisi data transaksi riil.

| ID Skenario | Langkah Pengujian | Data Uji | Hasil yang Diharapkan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-20.1** | Admin mengklik tombol "Cadangkan Database" di menu Pengaturan. | Lokasi disk lokal | Sistem membuat salinan berkas database dengan format nama `backup-YYYY-MM-DD_HH-mm-ss.db` secara utuh. | **PASS** |
| **TC-20.2** | Admin memilih berkas cadangan `.db` valid untuk melakukan proses pemulihan (*restore*). | File `.db` valid | Sistem meminta konfirmasi peringatan, menutup koneksi database aktif, menimpa file database operasional, dan merestart pembacaan data secara sukses. | **PASS** |
| **TC-20.3** | Pengguna mencoba memulihkan berkas yang bukan database SQLite (misal file teks `.txt`). | File `dokumen.txt` | Sistem mendeteksi berkas tidak valid dan membatalkan proses restore dengan pesan error aman. | **PASS** |

---

## 5.4 Evaluasi Hasil Pengujian & Tingkat Keberhasilan
- Total Kebutuhan Fungsional yang Diuji: **20 Kebutuhan (FR-01 s.d. FR-20)**.
- Jumlah Skenario Pengujian Dieksekusi: **20 Test Cases**.
- Tingkat Keberhasilan Pengujian (*Success Rate*): **100% (20 PASS / 0 FAIL)**.
- **Kesimpulan Kualitas**: Sistem SmartPOS terbukti stabil, memenuhi seluruh parameter spesifikasi fungsional, dan siap digunakan secara operasional.
