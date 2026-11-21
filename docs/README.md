# SmartPOS — Dokumentasi Rekayasa Perangkat Lunak (Master Index)

Repositori ini memuat seluruh dokumentasi rekayasa perangkat lunak (RPL) untuk sistem **SmartPOS: Sistem Kasir dan Manajemen Usaha (Beras, Telur, dan Gas LPG)**. Seluruh dokumen telah ditata secara terstruktur, bebas ambiguitas, dan menganut prinsip **Single Source of Truth (SSOT)** agar memudahkan pengumpulan tugas akademik serta referensi teknis pengembang.

---

## Peta Struktur Dokumentasi (`docs/`)

Dokumentasi dipisahkan secara tegas ke dalam 3 zona fungsional:

```
docs/
│
├── 01-panduan-akademik/          <-- ZONA 1: PANDUAN & AUDIT MATERI KULIAH (INTERNAL)
│   ├── README.md
│   ├── audit-dan-panduan-materi-rpl.md
│   └── rubrik-penilaian-sub-cpmk.md
│
├── 02-laporan-uts/               <-- ZONA 2: BERKAS RESMI UNTUK DIKUMPULKAN SAAT UTS (DELIVERABLES)
│   ├── README.md
│   ├── LAPORAN_UTUH_UTS_SMARTPOS.md  <-- ⭐ DOKUMEN MASTER TUNGGAL SIAP CETAK / EXPORT PDF
│   └── bab/                          <-- Naskah modular jika dosen meminta per bab terpisah
│       ├── BAB_1_PENDAHULUAN_DAN_ELISITASI.md
│       ├── BAB_2_METODOLOGI_PENGEMBANGAN_SISTEM.md
│       ├── BAB_3_SPESIFIKASI_KEBUTUHAN_PERANGKAT_LUNAK_SRS.md
│       ├── BAB_4_PEMODELAN_ANALISIS_DAN_PROSES_BISNIS.md
│       └── BAB_5_KETERTELUSURAN_DAN_PENGUJIAN_SISTEM.md
│
└── 03-spesifikasi-teknis/        <-- ZONA 3: DOKUMENTASI TEKNIS SISTEM & DEVELOPER REFERENCE
    ├── README.md
    ├── arsitektur-dan-keamanan-electron.md
    ├── skema-database-dan-kamus-data.md
    └── aturan-bisnis-gas-dan-hpp.md
```

---

## 1. Rincian Zona Dokumentasi

### Zona 1: Panduan Akademik & Audit Silabus Kuliah (`docs/01-panduan-akademik/`)
*Ditujukan untuk memahami capaian pembelajaran dan persiapan menghadapi ujian/sidang:*
- [01-panduan-akademik/audit-dan-panduan-materi-rpl.md](01-panduan-akademik/audit-dan-panduan-materi-rpl.md): Hasil audit materi perkuliahan Pertemuan 1–7 dosen pengampu (Dwi Rizki Bramantio, S.T., M.T. - Universitas Teknologi Bandung) dan pemetaan standar Sub-CPMK 052.2.
- [01-panduan-akademik/rubrik-penilaian-sub-cpmk.md](01-panduan-akademik/rubrik-penilaian-sub-cpmk.md): Instrumen ceklis pemenuhan 10 poin penilaian dosen dan panduan argumentasi untuk sesi tanya jawab/sidang.

---

### Zona 2: Berkas Laporan Resmi UTS (`docs/02-laporan-uts/`) ⭐
*Berkas deliverables resmi yang dikumpulkan mahasiswa ke dosen:*
- **[02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md](02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md)**  
  **Dokumen Master Tunggal Siap Kumpul**: Memuat Halaman Judul/Cover resmi UTS, Kata Pengantar, Daftar Isi, Bab I s.d. Bab VI lengkap dengan seluruh diagram Mermaid dan tabel terstandar.
- **Naskah Modular per Bab (`02-laporan-uts/bab/`)**:
  - [BAB I: Pendahuluan & Elisitasi Kebutuhan](02-laporan-uts/bab/BAB_1_PENDAHULUAN_DAN_ELISITASI.md) (Latar Belakang, Stakeholder, Persona, Problem Statement).
  - [BAB II: Metodologi Pengembangan Sistem](02-laporan-uts/bab/BAB_2_METODOLOGI_PENGEMBANGAN_SISTEM.md) (SDLC, Perbandingan 6 Model Proses, Justifikasi Argumentatif Model Incremental/Agile-Kanban, Delivery Roadmap 4 Tahap).
  - [BAB III: Spesifikasi Kebutuhan Perangkat Lunak (SRS / SKPL)](02-laporan-uts/bab/BAB_3_SPESIFIKASI_KEBUTUHAN_PERANGKAT_LUNAK_SRS.md) (20 Kebutuhan Fungsional baku, 5 User Story & Acceptance Criteria format Given-When-Then, Tabel NFR dengan kolom *Scope/How*, Matriks Prioritas 4 Level).
  - [BAB IV: Pemodelan Analisis Sistem & Proses Bisnis](02-laporan-uts/bab/BAB_4_PEMODELAN_ANALISIS_DAN_PROSES_BISNIS.md) (Use Case Diagram, 3 Skenario Use Case Rinci, Context Diagram, DFD Level 0, 2 Activity Diagram Kritis, Kamus Data lengkap, Verifikasi Konsistensi).
  - [BAB V: Ketertelusuran Kebutuhan & Pengujian Sistem](02-laporan-uts/bab/BAB_5_KETERTELUSURAN_DAN_PENGUJIAN_SISTEM.md) (Requirements Traceability Matrix / RTM 20 baris, 20 Skenario Black-Box Test Cases, Hasil Uji 100% PASS).

---

### Zona 3: Spesifikasi Teknis Sistem (`docs/03-spesifikasi-teknis/`)
*Ditujukan untuk referensi teknis pengembang dan arsitektur kode:*
- [03-spesifikasi-teknis/arsitektur-dan-keamanan-electron.md](03-spesifikasi-teknis/arsitektur-dan-keamanan-electron.md): Arsitektur multi-proses Electron 31, komunikasi IPC asinkron, isolasi `contextBridge`, dan hashing password `scrypt`.
- [03-spesifikasi-teknis/skema-database-dan-kamus-data.md](03-spesifikasi-teknis/skema-database-dan-kamus-data.md): Diagram Relasi Entitas (ERD), skema tabel SQLite, indeks query, dan proteksi transaksi atomik ACID.
- [03-spesifikasi-teknis/aturan-bisnis-gas-dan-hpp.md](03-spesifikasi-teknis/aturan-bisnis-gas-dan-hpp.md): Formula matematika *dual-stock* tabung gas LPG, algoritma *Moving Weighted Average Cost* HPP, dan konversi dinamis nominal "Beli Rp".

---

## 2. Petunjuk Praktis Pengumpulan Tugas UTS

1. Buka berkas master [02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md](02-laporan-uts/LAPORAN_UTUH_UTS_SMARTPOS.md).
2. Isi identitas mahasiswa pada halaman sampul depan (*Cover*):
   - **Nama Mahasiswa**: `[Nama Anda]`
   - **NIM**: `[Nomor Induk Mahasiswa Anda]`
   - **Kelas / Semester**: `[Kelas Anda]`
3. Ekspor ke berkas PDF:
   - Gunakan ekstensi **Markdown PDF** di Visual Studio Code (Klik kanan $\rightarrow$ **Markdown PDF: Export (pdf)**), atau
   - Salin isi dokumen ke Microsoft Word untuk disimpan ke format `.pdf` / `.docx`.
