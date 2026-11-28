# 02 — Berkas Laporan Resmi UTS Rekayasa Perangkat Lunak (SmartPOS)

Subfolder ini memuat **berkas naskah resmi yang dikumpulkan mahasiswa kepada dosen pengampu (Dwi Rizki Bramantio, S.T., M.T.) untuk Ujian Tengah Semester (UTS)** mata kuliah Rekayasa Perangkat Lunak, Program Studi S1 Teknik Informatika, Universitas Teknologi Bandung.

Struktur folder ini telah ditata secara modular dan rapi untuk mengeliminasi beban kognitif (*zero cognitive load*). Seluruh isi laporan telah diaudit dan **100% patuh terhadap sistematika resmi soal UTS ([docs/soal-uts/UTS TIF .pdf](../soal-uts/UTS%20TIF%20.pdf))**.

---

## 🧭 Peta Berkas & Direktori

```
docs/02-laporan-uts/
│
├── LAPORAN_UTUH_UTS_SMARTPOS.docx  <-- 🏆 BERKAS UTAMA UNTUK DIKUMPULKAN KE DOSEN (WORD SIAP CETAK/PDF)
├── LAPORAN_UTUH_UTS_SMARTPOS.md    <-- ⭐ BERKAS MASTER MARKDOWN TUNGGAL (SINGLE SOURCE OF TRUTH)
├── README.md                       <-- Peta panduan ini
│
├── bab/                            <-- 📂 NASKAH MODULAR PER BAB (BAB 1 s.d. 4 + DAFTAR PUSTAKA)
│   ├── BAB_1_PENDAHULUAN.md
│   ├── BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md
│   ├── BAB_3_PEMODELAN_ANALISIS_SISTEM.md
│   ├── BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md
│   └── DAFTAR_PUSTAKA.md
│
├── lampiran-dan-audit/             <-- 🔍 ARTEFAK AUDIT IMPLEMENTASI & INSTRUMEN VERIFIKASI
│   ├── AUDIT_BUKTI_DAN_IMPLEMENTASI.md
│   ├── CHECKLIST_KONSISTENSI_LAPORAN.md
│   └── DAFTAR_KONFIRMASI_LAPANGAN.md
│
└── scripts/                        <-- 🛠️ SKRIP OTOMASI PEMBUATAN DOKUMEN
    ├── generate_docx.py
    ├── build_clean_report.py
    └── fix_report_headings_and_narrative.py
```

---

## 🏆 1. Berkas Utama Pengumpulan Ujian

| Berkas | Format | Deskripsi & Kegunaan |
|---|---|---|
| **[LAPORAN UTS KELOMPOK 5 - SMARTPOS SISTEM KASIR DAN MANAJEMEN USAHA BERBASIS DESKTOP OFFLINE-FIRST - SOFTWARE REQUIREMENTS SPECIFICATION (SRS).docx](LAPORAN%20UTS%20KELOMPOK%205%20-%20SMARTPOS%20SISTEM%20KASIR%20DAN%20MANAJEMEN%20USAHA%20BERBASIS%20DESKTOP%20OFFLINE-FIRST%20-%20SOFTWARE%20REQUIREMENTS%20SPECIFICATION%20(SRS).docx)** | Microsoft Word (`.docx`) | **Naskah Word Terintegrasi Penuh (Template Resmi Kelompok 5).** Memuat Halaman Judul lengkap dengan tabel anggota, Kata Pengantar, Daftar Isi, Bab I s.d. Bab IV utuh, 16 tabel rapi, 15 diagram gambar resolusi tinggi, dan Daftar Pustaka berindentasi hanging. |
| **[LAPORAN_UTUH_UTS_SMARTPOS.docx](LAPORAN_UTUH_UTS_SMARTPOS.docx)** | Microsoft Word (`.docx`) | Salinan standar berpenamaan ringkas yang 100% identik dengan naskah Word Kelompok 5. |
| **[LAPORAN_UTUH_UTS_SMARTPOS.md](LAPORAN_UTUH_UTS_SMARTPOS.md)** | Markdown (`.md`) | **Master source naskah utuh.** Memuat seluruh teks laporan dari Cover, Kata Pengantar, Daftar Isi, Bab I s.d. Bab IV, Daftar Pustaka, hingga Lampiran Pengujian Black-Box. |

> **Catatan Pengumpulan**: Jika dosen meminta pengumpulan dalam format PDF, buka `LAPORAN_UTUH_UTS_SMARTPOS.docx` di Microsoft Word, lalu pilih **File $\rightarrow$ Save As / Export $\rightarrow$ PDF (*.pdf)**.

---

## 📂 2. Naskah Modular per Bab (`bab/`)

Digunakan jika dosen meminta penyerahan naskah terpisah per bab atau untuk kemudahan review bab per bab:

1. **[bab/BAB_1_PENDAHULUAN.md](bab/BAB_1_PENDAHULUAN.md)**  
   *Menjawab Soal 1 UTS*: Latar Belakang komoditas pangan & gas, Identifikasi Masalah, Rumusan Masalah, Tujuan Pengembangan, Batasan Masalah, Gambaran Umum Sistem, dan Pemilihan Model Proses SDLC Incremental (perbandingan 6 model proses, justifikasi 4 parameter, roadmap rilis inkremental 1 s.d. 4).
2. **[bab/BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md](bab/BAB_2_SOFTWARE_REQUIREMENTS_SPECIFICATION_SRS.md)**  
   *Menjawab Soal 2 UTS*: Deskripsi Umum Topologi Desktop Offline-First, Identifikasi Stakeholder, Triangulasi Teknik Elisitasi, Aktor & Matriks RBAC, 20 Kebutuhan Fungsional (FR-01 s.d. FR-20), 7 Kebutuhan Nonfungsional (NFR ISO/IEC 25010), 5 User Story, 10 Acceptance Criteria Given-When-Then, Matriks Prioritas 4 Tingkat, dan Requirements Traceability Matrix (RTM 20 baris).
3. **[bab/BAB_3_PEMODELAN_ANALISIS_SISTEM.md](bab/BAB_3_PEMODELAN_ANALISIS_SISTEM.md)**  
   *Menjawab Soal 3 UTS*: Use Case Diagram (UML 2.5.1, 16 use case, `<<include>>`/`<<extend>>`), 3 Skenario Use Case Rinci (Kasir & Beli Rp, Tukar Gas Konsumen, Sirkulasi Gas Agen 2-Tahap), 2 Activity Diagram (Transaksi Kasir & Logistik Masuk), Context Diagram, DFD Level 0 (7 proses & 7 data store), DFD Level 1 (Dekomposisi Transaksi Kasir 3.1–3.4), dan Kamus Data Lengkap.
4. **[bab/BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md](bab/BAB_4_ANALISIS_DAN_EVALUASI_HASIL_PEMODELAN.md)**  
   *Menjawab Soal 4 UTS*: Evaluasi Kesesuaian FR vs Use Case (zero gold plating), Konsistensi Use Case vs Activity Diagram, Konsistensi Context Diagram vs DFD Level 0, Evaluasi Uji Keseimbangan DFD Level 0 vs Level 1 (DFD Balancing 100%), Evaluasi Keterlacakan Kebutuhan (Forward & Backward Traceability), dan Kesimpulan Analisis Sistem.
5. **[bab/DAFTAR_PUSTAKA.md](bab/DAFTAR_PUSTAKA.md)**  
   Daftar Pustaka standar akademik IEEE/APA yang memuat buku teks acuan (Pressman, Sommerville), standar internasional (OMG UML 2.5.1, IEEE Std 830, ISO/IEC 25010), metodologi terstruktur (Gane & Sarson, DeMarco), dan dokumentasi resmi framework (Electron, SQLite).

---

## 🔍 3. Instrumen Audit & Verifikasi (`lampiran-dan-audit/`)

Dokumen pelengkap untuk membuktikan transparansi, integritas akademik, dan keterlacakan antara laporan dengan kode sumber sistem:

- **[lampiran-dan-audit/AUDIT_BUKTI_DAN_IMPLEMENTASI.md](lampiran-dan-audit/AUDIT_BUKTI_DAN_IMPLEMENTASI.md)**: Matriks audit pembuktian setiap klaim fitur terhadap baris kode sumber, IPC handler, skema tabel, dan pengujian aktual.
- **[lampiran-dan-audit/CHECKLIST_KONSISTENSI_LAPORAN.md](lampiran-dan-audit/CHECKLIST_KONSISTENSI_LAPORAN.md)**: Ceklis kepatuhan instruksi soal UTS untuk memastikan setiap butir pertanyaan terjawab tuntas.
- **[lampiran-dan-audit/DAFTAR_KONFIRMASI_LAPANGAN.md](lampiran-dan-audit/DAFTAR_KONFIRMASI_LAPANGAN.md)**: Instrumen pertanyaan konfirmasi lapangan untuk memisahkan fakta kode dari asumsi operasional toko.

---

## 🛠️ 4. Skrip Otomasi Pembuatan Dokumen (`scripts/`)

- **[scripts/generate_docx.py](scripts/generate_docx.py)**: Skrip Python untuk mengonversi `LAPORAN_UTUH_UTS_SMARTPOS.md` menjadi berkas `LAPORAN_UTUH_UTS_SMARTPOS.docx` secara otomatis lengkap dengan styling Times New Roman 12 pt, margin 4-3-3-3 cm, spasi 1.5 baris, tabel terformat rapi, dan 15 diagram beranotasi visual.

Cara menjalankan ulang generator jika terdapat revisi teks:
```powershell
python d:\Projects\SmartPOS\docs\02-laporan-uts\scripts\generate_docx.py
```
