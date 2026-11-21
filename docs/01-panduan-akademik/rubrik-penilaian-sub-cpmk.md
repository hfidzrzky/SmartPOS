# Rubrik Penilaian & Ceklis Kesiapan UTS (Sub-CPMK 052.2)
## Panduan Evaluasi Mandiri Dokumen Rekayasa Perangkat Lunak SmartPOS

Berkas ini memuat instrumen audit mandiri (*self-assessment checklist*) untuk memastikan bahwa dokumen yang dikumpulkan pada folder `02-laporan-uts/` memenuhi seluruh indikator capaian penilaian dosen pengampu pada UTS Mata Kuliah Rekayasa Perangkat Lunak.

---

## 1. Ceklis Evaluasi Capaian Pembelajaran (Sub-CPMK 052.2)

| Parameter Evaluasi Dosen | Target / Standar Silabus | Bukti Pemenuhan pada Dokumen Laporan UTS SmartPOS | Status |
| :--- | :--- | :--- | :---: |
| **1. Justifikasi Model Proses SDLC** | Format argumentatif (Slide 22): Menyatakan alasan pemilihan model berdasarkan bukti karakteristik proyek. | Bab II menyajikan analisis 6 model SDLC dan justifikasi formal pemilihan **Iterative-Incremental (Agile-Kanban)** lengkap dengan 4 tahap rilis (*Increments*). | **100% Terpenuhi** |
| **2. Elisitasi & Stakeholder** | Mengidentifikasi stakeholder, menerapkan teknik elisitasi, menyusun Persona, dan merumuskan *Problem Statement*. | Bab I memuat 5 kategori stakeholder, triangulasi teknik (wawancara, observasi, analisis berkas bon), persona Pak Hendra & Rina, serta matriks pemetaan kebutuhan. | **100% Terpenuhi** |
| **3. Formulasi Kebutuhan Fungsional (FR)** | Rumusan kalimat baku: *Subjek + Kata Kerja Spesifik + Hasil Tindakan*. | Bab III memuat **20 Kebutuhan Fungsional** (FR-01 s.d. FR-20) yang dirumuskan secara eksplisit dan tidak ambigu. | **100% Terpenuhi** |
| **4. User Story & Acceptance Criteria** | Minimal 5 User Story dengan format: *Sebagai [peran], saya ingin [fitur], agar [manfaat]* dan kriteria format **Given-When-Then** (min. 2 AC per US). | Bab III menyajikan 5 User Story lengkap dengan 10 skenario Acceptance Criteria berbasis **GIVEN - WHEN - THEN** (mencakup kasus sukses dan penanganan kesalahan). | **100% Terpenuhi** |
| **5. Kebutuhan Nonfungsional (NFR)** | Minimal 5 atribut kualitas dengan format kolom: *Quality Attribute, Requirement Definition, Scope / How*. | Bab III memuat 7 atribut NFR (Security, Process Isolation, Performance, ACID Reliability, Availability, Portability, Usability) dengan mekanisme teknis pemenuhannya. | **100% Terpenuhi** |
| **6. Matriks Skema Prioritas** | Membagi kebutuhan ke dalam 4 kategori prioritas: **High, Medium, Low, No Priority**. | Bab III memuat tabel matriks 4 level prioritas untuk seluruh domain fungsionalitas sistem. | **100% Terpenuhi** |
| **7. Pemodelan Use Case & Skenario** | Use Case Diagram lengkap dan minimal 2 Skenario Use Case detail (Precondition, Main Flow, Alternative Flow, Exception Flow, Postcondition). | Bab IV menyajikan Use Case Diagram Mermaid dan 3 skenario use case mendalam: Transaksi Kasir & Beli Rp (UC-02), Tukar Gas Konsumen (UC-05), dan Sirkulasi Agen 2-Tahap (UC-07). | **100% Terpenuhi** |
| **8. Context Diagram & DFD Level 0** | Menampilkan batasan sistem makro dan DFD Level 0 yang konsisten dengan data store fisik. | Bab IV memuat Context Diagram dengan 4 entitas eksternal dan DFD Level 0 dengan 7 proses bernomor serta 7 Data Store lokal (`D1` s.d. `D7`). | **100% Terpenuhi** |
| **9. Kamus Data (Data Dictionary)** | Mendefinisikan atribut: Nama Data, Deskripsi, Tipe Data, Format/Panjang, Constraint, Sumber Data. | Bab IV memuat tabel Kamus Data lengkap untuk entitas `products`, `transactions`, `transaction_items`, `gas_stock`, `gas_transactions`. | **100% Terpenuhi** |
| **10. Requirements Traceability Matrix (RTM)** | Menghubungkan kebutuhan hulu ke hilir: `FR` $\leftrightarrow$ `US` $\leftrightarrow$ `UC` $\leftrightarrow$ `DFD` $\leftrightarrow$ `UI` $\leftrightarrow$ `Test Case`. | Bab V memuat tabel RTM 20 baris lengkap dan 20 skenario pengujian *Black-Box* dengan tingkat kelulusan 100% PASS. | **100% Terpenuhi** |

---

## 2. Panduan Menghadapi Sesi Tanya Jawab Dosen / Ujian Lisan

Jika dosen penguji menanyakan aspek-aspek kritis dari sistem SmartPOS:

1. **Pertanyaan: *"Mengapa memilih arsitektur desktop offline-first dibanding web/cloud?"***
   - **Jawaban Argumentatif**: Berdasarkan hasil elisitasi langsung pada toko sembako dan pangkalan gas di lapangan (Bab I), konektivitas internet sering tidak stabil dan biaya langganan bulanan SaaS memberatkan UMKM. Arsitektur offline-first menjamin operasional kasir tetap berjalan 100% tanpa risiko offline, dengan jaminan integritas data lokal menggunakan SQLite ACID transaction.
2. **Pertanyaan: *"Bagaimana sistem menjamin stok tabung gas LPG tidak kacau saat transaksi?"***
   - **Jawaban Argumentatif**: SmartPOS menerapkan pemodelan *dual-stock closed-loop* (Bab IV & Bab V). Stok fisik dipisahkan secara eksplisit antara tabung isi (`filled_stock`) dan tabung kosong (`empty_stock`). Transaksi tukar konsumen dieksekusi secara tertutup (isi berkurang $N$, kosong bertambah $N$, total aset tabung di toko tetap). Pengiriman ke agen dicatat dalam 2 tahap terpisah, sehingga tabung yang berada di luar toko terlacak secara transparan.
3. **Pertanyaan: *"Bagaimana sistem menangani pembelian komoditas eceran yang nominal rupiahnya ganjil?"***
   - **Jawaban Argumentatif**: Sistem menyediakan fitur "Beli Rp" (FR-05 & UC-03) yang secara otomatis mengonversi nominal rupiah menjadi kuantitas pecahan kilogram desimal ($kg = \frac{\text{nominal}}{\text{harga\_kg}}$) secara instan, sehingga kasir tidak perlu menghitung kalkulator manual di jam sibuk toko.
