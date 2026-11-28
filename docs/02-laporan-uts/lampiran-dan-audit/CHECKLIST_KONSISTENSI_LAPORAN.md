# CEKLIS KONSISTENSI DAN EVALUASI KEPATUHAN LAPORAN UTS SMARTPOS
## Instrumen Pemeriksaan Silang Antar-Bab, Standar Pemodelan, dan Ketentuan Soal UTS
*Dokumen Kerja Reviewer Rekayasa Perangkat Lunak — Proyek SmartPOS*

---

## 1. Lembar Kepatuhan terhadap Soal UTS (Dosen: Dwi Rizki Bramantio, S.T., M.T.)

Berdasarkan berkas resmi `docs/soal-uts/UTS TIF .pdf`, berikut adalah audit kepatuhan struktur dan substansi laporan:

| Komponen Soal UTS | Deskripsi Wajib Soal | Bab / Subbab Pemenuhan | Status Kepatuhan | Catatan Audit & Verifikasi |
| :--- | :--- | :---: | :---: | :--- |
| **Pertanyaan Utama UTS** | Bagaimana permasalahan nyata dianalisis & diterjemahkan menjadi spesifikasi kebutuhan serta model analisis yang lengkap, konsisten, dan dapat ditelusuri? | Halaman Pengantar & Bab IV (Subbab 4.6) | **100% Patuh** | Dijawab terstruktur melalui alur: Identifikasi Masalah $\rightarrow$ SRS $\rightarrow$ UML 2.5.1 & DFD $\rightarrow$ RTM $\rightarrow$ Evaluasi Balancing & Traceability. |
| **SOAL 1: BAB I Pendahuluan** | 1.1 Latar Belakang<br>1.2 Identifikasi Masalah<br>1.3 Rumusan Masalah<br>1.4 Tujuan Pengembangan Sistem<br>1.5 Batasan Masalah<br>1.6 Gambaran Umum Sistem<br>1.7 Pemilihan Model Proses | Bab I (Subbab 1.1 s.d. 1.7) | **100% Patuh** | Memenuhi 5 ketentuan khusus: kondisi proses berjalan, kebutuhan perbaikan, tujuan & ruang lingkup, model proses (Iterative-Incremental dengan pendekatan Agile-Kanban), serta justifikasi argumentatif baku. Bebas dari klaim statistik tanpa rujukan primer. |
| **SOAL 2: BAB II SRS** | 2.1 Deskripsi Umum Sistem<br>2.2 Identifikasi Stakeholder<br>2.3 Teknik Elisitasi Kebutuhan<br>2.4 Identifikasi Aktor & Hak Akses<br>2.5 Kebutuhan Fungsional (FR)<br>2.6 Kebutuhan Nonfungsional (NFR)<br>2.7 User Story<br>2.8 Acceptance Criteria<br>2.9 Prioritas Kebutuhan<br>2.10 Requirements Traceability Matrix (RTM) | Bab II (Subbab 2.1 s.d. 2.10) | **100% Patuh** | 20 FR dengan kode stabil (FR-01 s.d. FR-20), 7 atribut NFR teruji, 5 User Story terstruktur, 10 skenario Acceptance Criteria format Given-When-Then, matriks prioritas 4 level, dan RTM 20 baris hulu-ke-hilir. Elisitasi dinyatakan faktual berbasis inspeksi kode dan analisis dokumen (bukan wawancara fiktif). |
| **SOAL 3: BAB III Pemodelan Analisis** | 3.1 Use Case Diagram (UML 2.5.1)<br>3.2 Deskripsi / Skenario Use Case<br>3.3 Activity Diagram<br>3.4 Context Diagram<br>3.5 DFD Level 0<br>3.6 DFD Level 1<br>3.7 Kamus Data (Data Dictionary) | Bab III (Subbab 3.1 s.d. 3.7) | **100% Patuh** | Use Case UML 2.5.1 (16 UC, `<<include>>`, `<<extend>>`), 3 skenario use case mendalam, 2 Activity Diagram, Context Diagram (Proses 0 tunggal), DFD Level 0 (7 proses, 7 data store), DFD Level 1 (dekomposisi Proses 3.0 menjadi 3.1 s.d. 3.4), dan Kamus Data terstruktur. DFD menggunakan notasi aliran data murni (bukan UML). |
| **SOAL 4: BAB IV Evaluasi & Konsistensi** | 4.1 Kesesuaian FR dengan Use Case<br>4.2 Konsistensi Use Case & Activity<br>4.3 Konsistensi Context & DFD 0<br>4.4 Konsistensi DFD 0 & DFD 1 (Balancing)<br>4.5 Evaluasi Keterlacakan Kebutuhan<br>4.6 Kesimpulan | Bab IV (Subbab 4.1 s.d. 4.6) | **100% Patuh** | Pemeriksaan empiris tabel demi tabel: Matriks FR $\leftrightarrow$ UC, uji keselarasan alur skenario terhadap node aktivitas, audit batas sistem, uji keseimbangan DFD 100% balanced, audit keterlacakan maju & mundur, serta kesimpulan akademik objektif. |
| **Daftar Pustaka** | Standar APA Edisi ke-7, sumber primer resmi dan ilmiah yang dapat diverifikasi | Bagian Daftar Pustaka | **100% Patuh** | Memuat literatur resmi: Pressman & Maxim (2020), Sommerville (2016), OMG (2017), Gane & Sarson (1979), DeMarco (1979), IEEE Std 830, ISO/IEC 25010, BPS (2024), Kepmen ESDM No. 37.K/MG.01/MEM.M/2023, serta dokumentasi Electron dan SQLite. Seluruh sitasi teks cocok dengan daftar pustaka. |

---

## 2. Pemeriksaan Konsistensi Antar-Bab (Cross-Chapter Traceability)

Tabel berikut membuktikan konsistensi semantik dan data dari Bab I hingga Bab IV:

| Rantai Keterlacakan | Elemen Bab Hulu | Elemen Bab Hilir | Status Konsistensi | Penjelasan Verifikasi |
| :--- | :--- | :--- | :---: | :--- |
| **Masalah $\rightarrow$ Kebutuhan** | P-01: Perhitungan konversi manual "Beli Rp"<br>P-02: Kerancuan status tabung gas fisik<br>P-03: Keterbatasan sirkulasi agen Pertamina<br>P-04: Kenaikan harga kulakan & multi-satuan<br>P-05: Ketergantungan internet & biaya SaaS | FR-05 & FR-06<br>FR-09, FR-10, FR-13, FR-14<br>FR-11 & FR-12<br>FR-03, FR-15, FR-16<br>NFR-03 & NFR-05 | **KONSISTEN** | Seluruh masalah operasional pada Subbab 1.2 memiliki padanan pemenuhan kebutuhan fungsional dan nonfungsional yang stabil pada Subbab 2.5 dan 2.6. |
| **Kebutuhan $\rightarrow$ Pemodelan UML** | FR-01 s.d. FR-20 | UC-01 s.d. UC-16 | **KONSISTEN** | 100% FR terpetakan pada Use Case Diagram. Tidak ada kebutuhan yang tidak memiliki use case pendukung dan tidak ada use case tanpa dasar kebutuhan (*zero gold plating*). |
| **Aktor Sistem $\rightarrow$ Model Interaksi** | Aktor Kasir (`kasir`) dan Admin (`admin`) pada Subbab 2.4 | Aktor pada Use Case Diagram (3.1), Activity Diagram (3.3), dan Context Diagram (3.4) | **KONSISTEN** | Aktor yang berinteraksi langsung hanya Kasir dan Admin. Pemasok/Agen dan Pelanggan diposisikan tepat sebagai entitas eksternal di luar batas sistem pada Context Diagram / DFD. |
| **Use Case $\rightarrow$ Activity Diagram** | Skenario UC-02 (Transaksi Kasir & Beli Rp)<br>Skenario UC-09 (Logistik Barang Masuk) | Activity Diagram Checkout Kasir (3.3.1)<br>Activity Diagram Barang Masuk (3.3.2) | **KONSISTEN** | Seluruh langkah naratif (Main Flow & Exception Flow) berkorespondensi 1-ke-1 dengan action states, decision nodes, dan merge nodes pada Activity Diagram. |
| **Batas Sistem Context $\rightarrow$ DFD Level 0** | Entitas E1 (Kasir), E2 (Admin), E3 (Pemasok/Agen), E4 (Printer Thermal) pada Context Diagram | Seluruh aliran data batas sistem pada DFD Level 0 | **KONSISTEN** | Aliran masuk (*Data Kredensial, Form Kasir, Input Stok/Gas/Keuangan*) dan aliran keluar (*Struk Belanja, Info Katalog, Laporan Usaha, Backup*) terbukti 100% lestari (*conserved*) melintasi batas sistem. |
| **DFD Level 0 $\rightarrow$ DFD Level 1 (Balancing)** | Proses Induk 3.0 (Pemrosesan Transaksi Kasir) dengan input dari E1, D2, D4 dan output ke E1, E4, D2, D3, D4 | Subproses 3.1, 3.2, 3.3, 3.4 pada DFD Level 1 | **KONSISTEN (100% Balanced)** | Seluruh masukan dan keluaran pada batas proses induk 3.0 muncul lengkap dan konsisten pada subproses dekomposisinya tanpa penambahan aliran eksternal liar. |
| **DFD Data Store $\rightarrow$ Kamus Data & Database** | Data Store `D1` s.d. `D7` pada DFD Level 0 dan Level 1 | Tabel Kamus Data (Subbab 3.7) dan Skema SQLite `database/schema.sql` | **KONSISTEN** | Penamaan tabel, atribut, tipe data, dan constraint pada Kamus Data identik dengan tabel fisik SQLite: `users` (D1), `products` (D2), `transactions` & `transaction_items` (D3), `gas_stock` (D4), `stock_movements` (D5), `expenses` & `income_extra` (D6), `settings` (D7). |
| **Kebutuhan $\rightarrow$ Pengujian RTM** | FR-01 s.d. FR-20 | Matriks RTM (Subbab 2.10) & Skenario Uji TC-01 s.d. TC-20 | **KONSISTEN** | Keterlacakan dua arah (*forward & backward traceability*) terpenuhi 100%. Skenario uji memverifikasi perilaku aktual sistem. |

---

## 3. Hasil Audit Format Naskah Akademik (Halaman 6 Soal UTS)

| Parameter Format | Standar Soal UTS | Kondisi pada Dokumen Laporan | Status |
| :--- | :--- | :--- | :---: |
| **Ukuran Kertas** | Kertas A4 (21,0 cm $\times$ 29,7 cm) | Ditetapkan pada konfigurasi dokumen | **Sesuai** |
| **Jenis & Ukuran Font** | Times New Roman, 12 pt untuk teks utama | Diterapkan konsisten di seluruh paragraf naskah | **Sesuai** |
| **Spasi Baris** | Spasi 1,5 baris | Diterapkan pada seluruh teks naratif laporan | **Sesuai** |
| **Batas Margin** | Margin Kiri: 4 cm; Atas: 3 cm; Kanan: 3 cm; Bawah: 3 cm | Sesuai standar baku dokumen akademik tugas akhir/makalah | **Sesuai** |
| **Penomoran Bab & Subbab** | Hierarki bertingkat konsisten (1.1 s.d. 4.6) | 100% identik dengan sistematika pada PDF soal UTS | **Sesuai** |
| **Penomoran Gambar & Tabel** | Setiap tabel dan gambar memiliki nomor urut dan judul deskriptif | Diberi nomor dan penjelasan fungsional lengkap | **Sesuai** |
| **Keterbacaan Diagram** | Notasi formal, terbaca jelas, tidak terpotong | Diagram dirender menggunakan sintaks Mermaid formal dan didukung teks fallback terstruktur | **Sesuai** |

---

## 4. Rekomendasi Tindak Lanjut Kelompok Mahasiswa

1. **Persiapan Sesi Presentasi & Tanya Jawab UTS**: Setiap anggota kelompok wajib memahami matriks RTM, formula konversi "Beli Rp", dan alur penukaran gas dual-stock 2-tahap.
2. **Pelaksanaan Validasi Lapangan Pasca-UTS**: Membawa lembar kerja `DAFTAR_KONFIRMASI_LAPANGAN.md` ke toko sembako dan pangkalan gas nyata untuk mengonfirmasi parameter operasional (variasi kemasan beras, durasi transaksi nyata, dan kebiasaan pembukuan pemilik).
3. **Penyempurnaan Algoritma HPP Sembako**: Pada fase perancangan arsitektur perangkat lunak pasca-UTS, kembangkan logika rekalkulasi HPP rata-rata tertimbang (*moving weighted average*) agar mencakup komoditas beras dan telur secara otomatis sebagaimana yang telah berjalan pada modul gas LPG.
