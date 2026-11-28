# SmartPOS — Dokumentasi Rekayasa Perangkat Lunak (Master Index)

Repositori ini memuat seluruh dokumentasi rekayasa perangkat lunak (RPL) untuk sistem **SmartPOS: Sistem Kasir dan Manajemen Usaha (Beras, Telur, dan Gas LPG)**. Seluruh dokumen telah ditata secara terstruktur, bebas ambiguitas, dan menganut prinsip **Single Source of Truth (SSOT)** agar memudahkan pengumpulan tugas akademik serta referensi teknis pengembang tanpa beban kognitif.

---

## 🗺️ Peta Struktur Dokumentasi (`docs/`)

Dokumentasi dipisahkan secara tegas ke dalam 3 zona fungsional:

```
docs/
│
├── 01-panduan-akademik/          <-- ZONA 1: PANDUAN & AUDIT MATERI KULIAH (INTERNAL)
│   ├── README.md
│   ├── audit-dan-panduan-materi-rpl.md
│   └── rubrik-penilaian-sub-cpmk.md
│
├── 02-laporan-uts/               <-- ZONA 2: BERKAS RESMI PENGUMPULAN UTS (DELIVERABLES)
│   ├── README.md                 <-- Panduan navigasi berkas laporan UTS
│   ├── LAPORAN_UTUH_UTS_SMARTPOS.docx  <-- ⭐ DOKUMEN WORD RESMI SIAP KUMPUL / PRINT PDF
│   ├── LAPORAN_UTUH_UTS_SMARTPOS.md    <-- ⭐ DOKUMEN MASTER MARKDOWN (SSOT)
│   │
│   ├── bab/                      <-- Naskah modular per Bab resmi sesuai soal UTS
│   │   ├── BAB_1_PENDAHULUAN.md
│   │   ├── BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md
│   │   ├── BAB_3_PEMODELAN_ANALISIS_SISTEM.md
│   │   ├── BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md
│   │   └── DAFTAR_PUSTAKA.md
│   │
│   ├── lampiran-dan-audit/       <-- Instrumen audit kode & verifikasi implementasi
│   │   ├── AUDIT_BUKTI_DAN_IMPLEMENTASI.md
│   │   ├── CHECKLIST_KONSISTENSI_LAPORAN.md
│   │   └── DAFTAR_KONFIRMASI_LAPANGAN.md
│   │
│   └── scripts/                  <-- Utilitas generator & kompilasi dokumen
│       ├── generate_docx.py
│       ├── build_clean_report.py
│       └── fix_report_headings_and_narrative.py
│
├── 03-spesifikasi-teknis/        <-- ZONA 3: DOKUMENTASI TEKNIS SISTEM & DEVELOPER REFERENCE
│   ├── README.md
│   ├── arsitektur-dan-keamanan-electron.md
│   ├── skema-database-dan-kamus-data.md
│   └── aturan-bisnis-gas-dan-hpp.md
│
└── soal-uts/                     <-- Berkas soal resmi UTS
    └── UTS TIF .pdf
```

---

## 1. Rincian Zona Dokumentasi

### 🎓 Zona 1: Panduan Akademik & Silabus Kuliah (`docs/01-panduan-akademik/`)
*Ditujukan untuk memahami capaian pembelajaran dan persiapan menghadapi evaluasi/sidang:*
- [01-panduan-akademik/audit-dan-panduan-materi-rpl.md](01-panduan-akademik/audit-dan-panduan-materi-rpl.md): Hasil audit materi perkuliahan Pertemuan 1–7 dosen pengampu (Dwi Rizki Bramantio, S.T., M.T. - Universitas Teknologi Bandung) dan pemetaan standar Sub-CPMK 052.2.
- [01-panduan-akademik/rubrik-penilaian-sub-cpmk.md](01-panduan-akademik/rubrik-penilaian-sub-cpmk.md): Instrumen ceklis pemenuhan 10 poin penilaian dosen dan panduan argumentasi untuk sesi tanya jawab/sidang.

---

### 📝 Zona 2: Berkas Laporan Resmi UTS (`docs/02-laporan-uts/`) ⭐
*Berkas deliverables resmi yang dikumpulkan mahasiswa kepada dosen pengampu:*
- **[02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.docx](02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.docx)** ⭐:  
  **Berkas Word (.docx) Resmi Siap Kumpul**: Diformat persis standar akademik (Times New Roman 12pt, spasi 1.5 baris, margin A4 4-3-3-3 cm, tabel bergaris rapi, cover resmi, dan 15 diagram beranotasi lengkap).
- **[02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md](02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md)** ⭐:  
  **Dokumen Master Markdown Tunggal (SSOT)**: Memuat seluruh isi laporan Bab I s.d. Bab IV, Daftar Pustaka, dan Lampiran Uji Black-box.
- **Naskah Modular per Bab (`02-laporan-uts/bab/`)**:
  - [Bab 1: Pendahuluan](02-laporan-uts/bab/BAB_1_PENDAHULUAN.md) (Latar Belakang, Identifikasi Masalah, Rumusan Masalah, Tujuan, Batasan Masalah, Gambaran Umum, Model Proses SDLC Incremental).
  - [Bab 2: Software Requirements Specification / SRS](02-laporan-uts/bab/BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md) (Deskripsi Sistem, Stakeholder, Elisitasi, Aktor & RBAC, 20 FR, 7 NFR, 5 User Story, 10 Acceptance Criteria, Matriks Prioritas, RTM 20 baris).
  - [Bab 3: Pemodelan Analisis Sistem](02-laporan-uts/bab/BAB_3_PEMODELAN_ANALISIS_SISTEM.md) (Use Case Diagram, 3 Skenario UC Kritis, 2 Activity Diagram, Context Diagram, DFD Level 0, DFD Level 1, Kamus Data).
  - [Bab 4: Analisis dan Evaluasi Hasil Pemodelan](02-laporan-uts/bab/BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md) (Kesesuaian FR vs UC, Konsistensi UC vs Activity, Konsistensi Context vs DFD 0, Uji Keseimbangan DFD Level 0 vs Level 1, Evaluasi Traceability, Kesimpulan).
  - [Daftar Pustaka](02-laporan-uts/bab/DAFTAR_PUSTAKA.md) (Standar IEEE/APA terverifikasi).
- **Instrumen Audit & Verifikasi (`02-laporan-uts/lampiran-dan-audit/`)**:
  - [AUDIT_BUKTI_DAN_IMPLEMENTASI.md](02-laporan-uts/lampiran-dan-audit/AUDIT_BUKTI_DAN_IMPLEMENTASI.md): Matriks audit kode sumber aktual vs klaim laporan.
  - [CHECKLIST_KONSISTENSI_LAPORAN.md](02-laporan-uts/lampiran-dan-audit/CHECKLIST_KONSISTENSI_LAPORAN.md): Ceklis kepatuhan instruksi soal UTS.
  - [DAFTAR_KONFIRMASI_LAPANGAN.md](02-laporan-uts/lampiran-dan-audit/DAFTAR_KONFIRMASI_LAPANGAN.md): Daftar verifikasi operasional lapangan.
- **Skrip Utilitas (`02-laporan-uts/scripts/`)**:
  - [generate_docx.py](02-laporan-uts/scripts/generate_docx.py): Skrip otomatis konversi Markdown ke DOCX standar UTS.

---

### ⚙️ Zona 3: Spesifikasi Teknis Sistem (`docs/03-spesifikasi-teknis/`)
*Ditujukan untuk referensi teknis pengembang dan arsitektur kode:*
- [03-spesifikasi-teknis/arsitektur-dan-keamanan-electron.md](03-spesifikasi-teknis/arsitektur-dan-keamanan-electron.md): Arsitektur multi-proses Electron 31, komunikasi IPC asinkron, isolasi `contextBridge`, dan hashing password `scrypt`.
- [03-spesifikasi-teknis/skema-database-dan-kamus-data.md](03-spesifikasi-teknis/skema-database-dan-kamus-data.md): Diagram Relasi Entitas (ERD), skema tabel SQLite, indeks query, dan proteksi transaksi atomik ACID.
- [03-spesifikasi-teknis/aturan-bisnis-gas-dan-hpp.md](03-spesifikasi-teknis/aturan-bisnis-gas-dan-hpp.md): Formula matematika *dual-stock* tabung gas LPG, algoritma *Moving Weighted Average Cost* HPP, dan konversi dinamis nominal "Beli Rp".

---

## 2. Petunjuk Pengumpulan Tugas UTS

1. Berkas utama yang diserahkan ke dosen pengampu adalah **[02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.docx](02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.docx)**.
2. Buka berkas tersebut di Microsoft Word, periksa halaman sampul (*Cover*), dan pastikan data diri (Nama, NIM, Kelas) telah terisi dengan benar.
3. Simpan atau cetak (*Export*) menjadi berkas `.pdf` jika dosen menghendaki pengumpulan dalam format PDF.
