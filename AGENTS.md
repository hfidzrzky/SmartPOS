# AGENTS.md — Pedoman Penyusunan Laporan SmartPOS

## 1. Identitas dan tujuan dokumen

**Proyek:** SMARTPOS: Sistem Kasir dan Manajemen Usaha (Beras, Telur, dan Gas LPG) Berbasis Desktop *Offline-First*  
**Dokumen:** Analisis Kebutuhan dan Pemodelan Perangkat Lunak  
**Konteks:** Laporan Ujian Tengah Semester (UTS) mata kuliah Rekayasa Perangkat Lunak.

Dokumen ini menjadi instruksi kerja bagi AI agent yang membantu memeriksa, menganalisis, dan menyusun laporan SmartPOS. **Aplikasi SmartPOS telah tersedia/diimplementasikan. Tugas agent adalah mendokumentasikan dan menganalisis sistem yang benar-benar ada, bukan mengarang rancangan ideal, menambahkan fitur, atau mengubah aplikasi agar sesuai dengan narasi laporan.**

Laporan harus menggambarkan hubungan yang dapat ditelusuri antara:

1. proses bisnis dan kondisi operasional yang benar-benar diketahui;
2. masalah yang didukung hasil observasi, wawancara, atau bukti sistem;
3. kebutuhan pengguna dan kebutuhan perangkat lunak;
4. perilaku serta fitur yang benar-benar tersedia pada implementasi SmartPOS;
5. model analisis yang merepresentasikan kebutuhan tersebut; dan
6. hasil pemeriksaan konsistensi antarartefak.

Instruksi ini berlaku untuk seluruh pekerjaan penulisan laporan, revisi narasi, penyusunan tabel, diagram, SRS, RTM, dan evaluasi model.

---

## 2. Prinsip utama: dokumentasikan fakta, jangan mengarang

### 2.1 Sistem yang berjalan adalah objek utama dokumentasi

Perlakukan repository, kode sumber, konfigurasi, skema basis data, migrasi, pengujian, serta perilaku aplikasi sebagai sumber utama untuk mengetahui implementasi SmartPOS. Jangan menjadikan draf laporan sebagai bukti bahwa suatu fitur benar-benar tersedia.

**Jangan pernah:**

- mengklaim fitur sudah berjalan hanya karena disebut dalam judul, latar belakang, diagram, backlog, atau rencana;
- menambahkan fitur ke laporan agar terlihat lengkap padahal tidak ditemukan pada aplikasi atau kode;
- menyatakan aplikasi berjalan sempurna, bebas kesalahan, 100% aman, *zero downtime*, atau 100% offline tanpa bukti pengujian yang relevan;
- menyimpulkan bahwa sebuah proses menyebabkan kerugian, kehilangan barang, antrean, atau kesalahan keuangan tanpa bukti;
- membuat angka, frekuensi kejadian, persentase, nama narasumber, tanggal wawancara, hasil observasi, atau kutipan yang tidak tersedia;
- menganggap diagram, komentar kode, nama fungsi, atau tabel database saja sudah membuktikan seluruh alur berhasil digunakan;
- mengubah ruang lingkup sistem secara diam-diam saat memperbaiki tata bahasa.

### 2.2 Klasifikasi status setiap fitur

Sebelum menulis fitur, klasifikasikan statusnya dengan salah satu kategori berikut:

| Status | Makna | Cara menuliskan dalam laporan |
|---|---|---|
| **Terimplementasi dan terverifikasi** | Fitur ditemukan pada kode dan perilakunya dapat dibuktikan melalui aplikasi, pengujian, atau keduanya. | Dapat dijelaskan sebagai fungsi sistem yang tersedia. Sebutkan batas atau kondisi penggunaannya. |
| **Terimplementasi sebagian** | Sebagian alur tersedia, tetapi ada langkah, kondisi, atau validasi yang belum tersedia. | Jelaskan bagian yang tersedia dan batasannya. Jangan menyebutnya selesai sepenuhnya. |
| **Bergantung konfigurasi/perangkat** | Fitur bekerja hanya jika perangkat, konfigurasi, printer, jaringan, atau layanan tertentu tersedia. | Nyatakan prasyarat dan ketergantungannya. |
| **Direncanakan/belum terimplementasi** | Ada di rancangan, backlog, atau pembahasan, tetapi belum tersedia pada aplikasi. | Masukkan sebagai batasan atau pengembangan lanjutan, bukan kebutuhan yang telah dipenuhi. |
| **Belum dapat diverifikasi** | Bukti yang tersedia tidak cukup untuk memastikan statusnya. | Nyatakan bahwa status belum dapat dipastikan. Jangan membuat kesimpulan. |
| **Di luar ruang lingkup** | Secara eksplisit tidak didukung atau tidak ditangani oleh sistem. | Cantumkan pada batasan sistem jika relevan. |

Jika status suatu fitur tidak jelas, gunakan **belum dapat diverifikasi** sampai bukti ditemukan.

### 2.3 Catatan bukti wajib

Setiap pernyataan penting mengenai implementasi harus dapat ditelusuri. Saat melakukan audit, catat sekurang-kurangnya:

- nama fitur atau proses;
- status implementasi;
- bukti repository: path file, nama modul/fungsi/komponen, skema tabel, migrasi, atau test;
- bukti perilaku: halaman aplikasi, alur penggunaan, hasil pengujian, atau keluaran yang dapat diamati;
- batasan, prasyarat, dan kondisi gagal;
- implikasi terhadap SRS dan diagram.

Jangan mencantumkan path atau nama fungsi dalam laporan akademik kecuali memang diperlukan. Catatan bukti ini terutama digunakan agent untuk memastikan setiap pernyataan benar.

---

## 3. Urutan sumber kebenaran dan penanganan konflik

Gunakan hierarki berikut. Jika dua sumber bertentangan, jangan memilih salah satunya secara diam-diam. Catat konflik dan lakukan verifikasi.

1. **Perilaku aplikasi yang dapat direproduksi** melalui alur penggunaan dan pengujian yang aman.
2. **Kode sumber, konfigurasi, skema database, migrasi, dan automated test** yang aktif pada versi proyek yang sedang diperiksa.
3. **Catatan observasi, wawancara, dan keputusan pengguna** yang benar-benar tersedia.
4. **Dokumentasi teknis proyek** seperti README, spesifikasi sebelumnya, issue, changelog, dan catatan pengembangan.
5. **Draf laporan SmartPOS** sebagai bahan konteks dan petunjuk pemeriksaan, bukan bukti final implementasi.
6. **Materi soal UTS** sebagai acuan struktur dan kriteria tugas akademik.
7. **Sumber eksternal resmi/ilmiah** untuk mendukung teori, regulasi, standar, dan statistik umum; bukan untuk menggantikan bukti kondisi toko.

### 3.1 Dokumen acuan UTS

Gunakan PDF soal UTS yang diberikan pengguna sebagai acuan utama penyusunan laporan. Jika PDF soal dan draf laporan tidak tersedia di workspace agent, periksa lampiran yang dapat diakses dalam sesi. Jika tidak dapat diakses, minta pengguna menempatkan salinannya pada folder referensi proyek (misalnya `docs/referensi/`) sebelum mengklaim telah mencocokkan laporan dengan soal. Jangan mengarang isi dokumen berdasarkan nama file atau ringkasan sebelumnya.

Struktur wajibnya adalah:

- **BAB I — Pendahuluan:** 1.1 Latar Belakang; 1.2 Identifikasi Masalah; 1.3 Rumusan Masalah; 1.4 Tujuan Pengembangan Sistem; 1.5 Batasan Masalah; 1.6 Gambaran Umum Sistem; 1.7 Pemilihan Model Proses Pengembangan Perangkat Lunak.
- **BAB II — Software Requirements Specification (SRS):** 2.1 Deskripsi Umum Sistem; 2.2 Identifikasi Stakeholder; 2.3 Teknik Elisitasi Kebutuhan; 2.4 Identifikasi Aktor dan Hak Akses; 2.5 Kebutuhan Fungsional; 2.6 Kebutuhan Nonfungsional; 2.7 User Story; 2.8 Acceptance Criteria; 2.9 Prioritas Kebutuhan; 2.10 Requirements Traceability Matrix (RTM).
- **BAB III — Pemodelan Analisis Sistem:** 3.1 Use Case Diagram; 3.2 Deskripsi/Skenario Use Case; 3.3 Activity Diagram; 3.4 Context Diagram; 3.5 DFD Level 0; 3.6 DFD Level 1; 3.7 Kamus Data.
- **BAB IV — Analisis dan Evaluasi Hasil Pemodelan:** 4.1 Kesesuaian Kebutuhan Fungsional dengan Use Case Diagram; 4.2 Konsistensi Use Case dan Activity Diagram; 4.3 Konsistensi Context Diagram dan DFD Level 0; 4.4 Konsistensi DFD Level 0 dan DFD Level 1; 4.5 Evaluasi Keterlacakan Kebutuhan; 4.6 Kesimpulan.

Patuhi pula ketentuan soal tentang notasi UML 2.5.1 untuk Use Case dan Activity Diagram, penggunaan notasi DFD secara konsisten (DFD bukan UML), penamaan dan aliran data yang konsisten, balancing DFD, judul dan penjelasan setiap diagram, serta RTM.

### 3.2 Informasi awal dari draf SmartPOS yang wajib diverifikasi

Draf laporan yang tersedia menyebutkan konteks berikut. Perlakukan semua butir ini sebagai **informasi awal untuk diperiksa**, bukan fakta implementasi otomatis. Bila agent tidak memiliki akses ke draf yang dimaksud, jangan mengklaim telah memeriksanya; minta pengguna menyediakan dokumen tersebut.

- aplikasi desktop berbasis Electron;
- basis data lokal SQLite;
- pendekatan *offline-first* dan penggunaan satu perangkat (*single-device standalone*);
- komoditas beras, telur ayam, LPG 3 kg bersubsidi, LPG 5,5 kg, dan LPG 12 kg;
- transaksi penjualan, konversi nominal rupiah ke kuantitas, dan pengelolaan multi-satuan;
- perhitungan HPP *moving weighted average* untuk komoditas yang ditentukan;
- pencatatan tabung LPG isi, kosong, dan perpindahan tabung ke/dari agen;
- pencatatan biaya operasional dan laporan usaha;
- akun pengguna, hak akses, riwayat aktivitas, serta backup dan pemulihan database;
- pembayaran tunai, transfer bank, dan QRIS statis dengan verifikasi manual;
- printer thermal 80 mm dan input hasil penimbangan secara manual;
- tidak ada integrasi langsung dengan payment gateway, timbangan digital, atau sistem agen LPG; tidak ada sinkronisasi multi-cabang.

Jika repository atau perilaku aplikasi tidak mendukung salah satu butir di atas, koreksi laporan berdasarkan kondisi aktual dan catat perbedaannya. Jangan mempertahankan klaim hanya karena sudah tercantum pada draf.

---

## 4. Prosedur wajib sebelum menulis atau merevisi laporan

AI agent **tidak boleh langsung menulis ulang laporan** sebelum menyelesaikan pemeriksaan awal berikut.

### Tahap 1 — Pahami repository

1. Periksa struktur direktori proyek dan instruksi `AGENTS.md` lain yang berlaku.
2. Baca README, package manifest, dokumentasi setup, konfigurasi, dan catatan versi.
3. Identifikasi entry point aplikasi, modul utama, routing/navigation, service, database layer, dan komponen UI.
4. Identifikasi skema database, migration, seed, query, serta relasi tabel yang relevan.
5. Identifikasi test, lint, build script, dan cara menjalankan aplikasi yang telah disediakan proyek.
6. Periksa Git status sebelum bekerja. Jangan menghapus, menimpa, atau mengubah pekerjaan pengguna.

### Tahap 2 — Petakan fungsi yang benar-benar tersedia

Periksa setidaknya domain berikut, jika memang ada pada proyek:

- autentikasi, akun, peran, dan hak akses;
- data produk dan kategori;
- transaksi penjualan dan detail transaksi;
- perhitungan harga, kuantitas, diskon, pembayaran, dan kembalian;
- input nominal rupiah dan konversi menjadi kuantitas;
- penerimaan/pembelian barang;
- satuan pembelian dan satuan penjualan;
- pergerakan stok dan penyesuaian stok;
- perhitungan HPP dan histori biaya perolehan;
- status tabung LPG dan transaksi pertukaran;
- pengiriman/penerimaan tabung dari agen;
- biaya operasional dan laporan;
- cetak struk;
- audit log/riwayat aktivitas;
- backup dan restore;
- pengaturan aplikasi dan ketergantungan eksternal.

Jangan menganggap semua domain di atas pasti tersedia. Domain tersebut adalah daftar pemeriksaan.

### Tahap 3 — Verifikasi perilaku sistem

1. Jalankan aplikasi hanya menggunakan prosedur resmi proyek dan lingkungan lokal yang aman.
2. Gunakan data uji atau data dummy. Jangan mengekspos data pribadi, transaksi riil, kredensial, token, atau informasi sensitif.
3. Uji alur utama dan alur alternatif yang relevan jika memungkinkan.
4. Periksa validasi input, kondisi gagal, batas transaksi, perubahan stok, dan konsistensi hasil.
5. Verifikasi klaim *offline-first* dengan cara yang aman dan terkendali. Bedakan fungsi yang tetap berjalan tanpa internet dari fungsi yang tetap memerlukan jaringan.
6. Verifikasi proses cetak, backup, restore, dan integrasi perangkat hanya jika perangkat atau lingkungan pengujiannya tersedia.
7. Jangan menjalankan perintah destruktif, menghapus database, menjalankan migrasi terhadap database produksi, atau mengubah konfigurasi pengguna.

Jika aplikasi tidak dapat dijalankan, jangan menebak perilakunya dari kode saja. Jelaskan bukti statis yang tersedia dan tandai perilaku runtime sebagai belum terverifikasi.

### Tahap 4 — Buat matriks inventaris fitur

Sebelum menyusun narasi, buat tabel kerja seperti berikut:

| ID | Domain/fitur | Bukti implementasi | Bukti perilaku/test | Status | Batasan/catatan |
|---|---|---|---|---|---|
| SYS-01 | Contoh domain | Path/simbol yang ditemukan | Test/alur yang diamati | Terverifikasi/parsial/dll. | Catatan faktual |

Gunakan ID yang stabil untuk memudahkan penelusuran. Jangan mengisi status “terverifikasi” tanpa bukti.

### Tahap 5 — Susun peta konsistensi

Buat hubungan berikut sebelum menulis final:

`Masalah (P) → Kebutuhan (FR/NFR) → User Story → Acceptance Criteria → Use Case → Activity Diagram → DFD/Aliran Data → Test/Evaluasi`

Setiap fitur yang disebut di Bab I harus memiliki status dan ruang lingkup yang konsisten dengan Bab II. Setiap kebutuhan fungsional pada Bab II harus memiliki aktor/proses yang sesuai pada Bab III. Bab IV harus memeriksa artefak yang benar-benar tersedia, bukan menyatakan konsisten tanpa pemeriksaan.

---

## 5. Pedoman penulisan setiap bab

## 5.1 BAB I — Pendahuluan

### 1.1 Latar Belakang

- Awali dengan konteks perdagangan beras, telur, dan LPG sesuai objek SmartPOS.
- Gunakan statistik nasional hanya sebagai konteks, bukan bukti masalah spesifik pada toko.
- Uraikan masalah lokal hanya berdasarkan wawancara, observasi, dokumen, atau bukti lain yang benar-benar tersedia.
- Jelaskan alasan sistem diperlukan dan arah solusi secara ringkas.
- Jangan memakai klaim “lebih dari 85% transaksi” atau statistik sejenis kecuali ditemukan sumber primer yang secara eksplisit mengukur klaim tersebut.
- Jangan menyatakan semua UMKM masih menggunakan pencatatan manual.
- Setiap data eksternal harus memiliki sitasi yang dapat diverifikasi dan entri daftar pustaka.

### 1.2 Identifikasi Masalah

- Daftar masalah yang benar-benar ditemukan, bukan daftar fitur yang ingin dibuat.
- Satu butir membahas satu masalah yang jelas.
- Bedakan fakta, dampak yang teramati, dan risiko yang mungkin terjadi.
- Hindari kata “sering”, “selalu”, “banyak”, “menumpuk”, “hilang”, “merugikan”, atau “tidak akurat” jika tidak ada bukti yang mendukung.
- Jangan menyalin isi latar belakang secara panjang; ringkas masalah operasionalnya.

### 1.3 Rumusan Masalah

- Bentuk sebagai pertanyaan yang dapat dijawab oleh pekerjaan analisis dan pemodelan.
- Pertanyaan harus sejalan dengan masalah pada 1.2.
- Hindari memasukkan fitur yang tidak ditemukan atau tidak masuk ruang lingkup.
- Jangan mengubah seluruh rumusan menjadi pertanyaan implementasi coding apabila keluaran UTS adalah dokumen analisis dan pemodelan.

### 1.4 Tujuan Pengembangan Sistem

- Setiap tujuan harus menjawab rumusan masalah yang relevan.
- Bedakan tujuan penyusunan dokumen (analisis, SRS, diagram, RTM) dan tujuan sistem (fungsi operasional).
- Gunakan kata kerja yang dapat dievaluasi: mengidentifikasi, menganalisis, menyusun, merancang, memodelkan, mengevaluasi.
- Jangan mengklaim keberhasilan/peningkatan yang belum diukur.

### 1.5 Batasan Masalah

- Nyatakan platform dan arsitektur yang benar-benar digunakan.
- Jelaskan komoditas dan variasi produk yang benar-benar didukung.
- Nyatakan fungsi yang termasuk dan tidak termasuk.
- Jelaskan batas single-device, konektivitas, pembayaran, hardware, integrasi, dan laporan jika relevan.
- Jangan menetapkan versi runtime atau library yang tidak lagi sesuai dengan konfigurasi repository aktual.
- Jangan menyebut fitur “tidak tersedia” sebelum memeriksa keseluruhan implementasi dan konfigurasi terkait.

### 1.6 Gambaran Umum Sistem

- Gambarkan sistem sesuai fungsi yang benar-benar ditemukan.
- Pembagian subsistem harus mencerminkan modul atau kelompok fungsi nyata, bukan arsitektur khayalan.
- Jelaskan hubungan antarbagian secara ringkas.
- Diagram dan narasi harus memiliki daftar fitur yang sama.
- Jangan menambahkan fitur seperti diskon, ekspor PDF/Excel, audit log, enkripsi tertentu, opname, atau dashboard jika belum terverifikasi.

### 1.7 Pemilihan Model Proses Pengembangan Perangkat Lunak

Bagian ini wajib memenuhi lima ketentuan soal UTS secara eksplisit:

1. **Kondisi proses berjalan dan permasalahan:** gambarkan proses bisnis sebelum/saat sistem digunakan berdasarkan bukti yang tersedia. Bedakan proses lama (*as-is*) dari proses yang didukung SmartPOS.
2. **Kebutuhan atau peluang perbaikan:** petakan masalah ke kebutuhan sistem. Jangan mengulang masalah tanpa menunjukkan peluang perbaikannya.
3. **Tujuan dan ruang lingkup:** ringkas sasaran dan batas sistem berdasarkan 1.4–1.6. Hindari menambahkan cakupan baru.
4. **Model proses yang digunakan:** jelaskan model yang benar-benar dipilih/digunakan selama proyek. Alternatif seperti Waterfall, Incremental, Prototyping, dan Agile dapat dibandingkan secara proporsional jika relevan.
5. **Alasan pemilihan:** bahas karakteristik proyek, kebutuhan dan perubahan, risiko, serta kemampuan/organisasi tim berdasarkan kondisi nyata.

**Ketentuan metodologis:**

- Bedakan model proses, pendekatan, dan metode pengelolaan kerja. *Iterative-Incremental* dapat dijelaskan sebagai pendekatan/model siklus pengembangan; Agile sebagai pendekatan adaptif; Kanban sebagai metode visualisasi dan pengelolaan alur kerja. Jangan menyebut Kanban sebagai Scrum atau menganggap Kanban mensyaratkan sprint.
- Karena aplikasi sudah tersedia, jelaskan proses pengembangan yang benar-benar dilakukan berdasarkan bukti (misalnya riwayat commit, issue, pembagian tugas, catatan rapat, atau tahapan kerja). Jangan memilih model secara retrospektif hanya karena terdengar cocok.
- Jika model yang digunakan tim tidak terdokumentasi, tulis secara jujur bahwa model merupakan pendekatan yang dipilih/diadopsi untuk proyek, bukan mengklaim seluruh praktiknya telah dijalankan.
- Perbandingan model harus seimbang. Jangan menyebut Waterfall selalu “sekali rilis”, Prototyping tidak dapat mendukung sistem transaksional, Spiral hanya untuk enterprise, Incremental otomatis berisiko rendah, atau DevOps tidak dapat digunakan untuk aplikasi desktop.
- Jangan memberikan nilai risiko tinggi/sedang/rendah tanpa kriteria dan bukti.
- Uraikan kemampuan tim sesuai jumlah anggota, pembagian peran, ketersediaan waktu, dan kompetensi yang benar-benar diketahui. Jangan mengarang kemampuan individu.
- Tahapan increment yang ditulis harus sesuai urutan pengerjaan aktual atau diberi label jelas sebagai rencana, bukan riwayat yang sudah terjadi.
- Hindari pengulangan panjang dari 1.2–1.6. Bagian 1.7 menyatukan informasi tersebut untuk menjelaskan keputusan model.

## 5.2 BAB II — Software Requirements Specification (SRS)

### 2.1 Deskripsi Umum Sistem

Jelaskan tujuan, ruang lingkup, konteks penggunaan, karakteristik umum, platform, dan batas sistem berdasarkan implementasi aktual.

### 2.2 Identifikasi Stakeholder

Identifikasi pihak yang benar-benar berkepentingan atau berinteraksi dengan sistem. Jangan membuat stakeholder eksternal seperti bank, agen, distributor, atau pelanggan sebagai aktor sistem jika tidak ada interaksi langsung yang relevan.

### 2.3 Teknik Elisitasi Kebutuhan

- Sebutkan teknik yang benar-benar dilakukan: wawancara, observasi, analisis dokumen, atau teknik lain.
- Cantumkan narasumber, peran, waktu, konteks, dan hasil hanya jika datanya tersedia.
- Pisahkan hasil wawancara dari interpretasi tim.
- Jangan membuat transkrip, kutipan, tanggal, durasi, atau hasil observasi fiktif.
- Jika bukti elisitasi belum tersedia, tandai kekosongan tersebut dan minta pengguna melengkapi bahan; jangan mengarang.

### 2.4 Identifikasi Aktor dan Hak Akses

Aktor adalah peran yang benar-benar berinteraksi dengan sistem. Hak akses harus sesuai dengan implementasi otorisasi. Jangan menyimpulkan adanya RBAC hanya karena terdapat nama peran pada UI.

### 2.5 Kebutuhan Fungsional (FR)

- Beri ID unik dan stabil: FR-001, FR-002, dan seterusnya.
- Satu kebutuhan menyatakan satu kemampuan sistem.
- Gunakan format yang jelas, misalnya: “Sistem harus dapat ...”.
- Nyatakan pemicu, input, proses/aturan, dan hasil bila diperlukan.
- Hindari kata kabur: cepat, mudah, optimal, otomatis sepenuhnya, fleksibel, real-time, dan sejenisnya tanpa definisi.
- Kebutuhan harus berasal dari kebutuhan pengguna atau perilaku sistem aktual, bukan daftar fitur yang dibayangkan agent.
- Bedakan kebutuhan yang sudah diimplementasikan dari kebutuhan yang belum atau hanya sebagian tersedia.

### 2.6 Kebutuhan Nonfungsional (NFR)

- Beri ID unik: NFR-001, NFR-002, dan seterusnya.
- Buat spesifik dan dapat diuji.
- Kelompokkan bila relevan: performa, keamanan, keandalan, kompatibilitas, usability, pemeliharaan, backup, dan offline operation.
- Jangan mencantumkan target waktu respons, jumlah pengguna, ukuran data, RPO/RTO, atau tingkat ketersediaan tanpa dasar atau persetujuan yang jelas.
- Bedakan target yang ditetapkan dari hasil pengujian yang benar-benar diperoleh.

### 2.7 User Story

Gunakan format: “Sebagai [peran], saya ingin [kebutuhan], sehingga [manfaat].” Peran, kebutuhan, dan manfaat harus berasal dari konteks pengguna nyata. Jangan menjadikan developer sebagai pengguna bisnis tanpa alasan.

### 2.8 Acceptance Criteria

- Gunakan kriteria yang objektif dan dapat diverifikasi.
- Jika sesuai, gunakan format Given–When–Then.
- Sertakan kondisi normal, batas input, dan kondisi gagal yang relevan.
- Kriteria penerimaan bukan klaim bahwa fitur telah lulus pengujian. Status hasil uji dicatat terpisah.

### 2.9 Prioritas Kebutuhan

Gunakan metode prioritas yang konsisten (misalnya MoSCoW) dan jelaskan dasar prioritasnya. Jangan memberi label Must Have pada fitur hanya karena agent menilai fitur tersebut menarik.

### 2.10 Requirements Traceability Matrix (RTM)

RTM harus menghubungkan ID masalah, FR/NFR, User Story, Acceptance Criteria, Use Case, diagram terkait, dan test/evaluasi jika tersedia. Gunakan ID yang sama di seluruh bab. Jika suatu relasi belum dibuat atau belum diuji, tandai belum tersedia; jangan mengisi hubungan semu.

## 5.3 BAB III — Pemodelan Analisis Sistem

### 3.1 Use Case Diagram

- Gunakan notasi UML sesuai OMG UML 2.5.1 sebagaimana diminta soal.
- Identifikasi aktor yang berinteraksi langsung dengan sistem.
- Use case harus mewakili kebutuhan fungsional, bukan nama tabel atau aktivitas internal kode.
- Gunakan association, `include`, dan `extend` hanya bila maknanya benar.
- Batas sistem harus jelas.

### 3.2 Deskripsi/Skenario Use Case

Setiap skenario memuat: ID/nama, tujuan, aktor utama, aktor pendukung bila ada, precondition, pemicu, main flow, alternative/exception flow, dan postcondition. Alur harus menggambarkan perilaku aktual atau kebutuhan yang telah disepakati.

### 3.3 Activity Diagram

- Gunakan notasi UML 2.5.1.
- Gunakan initial node, action, decision/merge, fork/join, dan final node sesuai kebutuhan.
- Diagram harus konsisten dengan skenario use case.
- Jangan memasukkan langkah yang tidak dilakukan sistem atau aktor.

### 3.4 Context Diagram

Gambarkan SmartPOS sebagai satu proses sistem dan entitas eksternal yang benar-benar berinteraksi. Tampilkan aliran data masuk/keluar yang relevan. Jangan memasukkan data store atau dekomposisi internal ke context diagram.

### 3.5 DFD Level 0

- Uraikan sistem menjadi proses utama dan data store.
- Gunakan entitas eksternal, proses, data store, dan aliran data secara konsisten.
- Setiap proses memiliki nama berbasis aktivitas dan fungsi yang jelas.
- Aliran data pada batas sistem harus konsisten dengan context diagram.
- Ingat: DFD bukan diagram UML.

### 3.6 DFD Level 1

- Pilih proses Level 0 yang benar-benar perlu didekomposisi.
- Gunakan penomoran konsisten (misalnya proses 2.0 menjadi 2.1, 2.2, 2.3).
- Tampilkan aliran data dan data store relevan.
- Periksa balancing: input dan output pada batas proses induk harus tetap terwakili pada diagram dekomposisi.
- Jangan menambah aliran eksternal baru tanpa alasan dan tanpa memperbarui model terkait.

### 3.7 Kamus Data

Definisikan setiap aliran data dan data store yang muncul di DFD. Jelaskan elemen, struktur, tipe atau format data bila relevan. Penamaan wajib sama persis dengan diagram.

## 5.4 BAB IV — Analisis dan Evaluasi Hasil Pemodelan

BAB IV merupakan pemeriksaan berdasarkan artefak aktual. Jangan menulis bahwa semua diagram konsisten tanpa membandingkan satu per satu.

- **4.1 Kesesuaian FR dengan Use Case:** tunjukkan FR mana direpresentasikan oleh use case tertentu; identifikasi FR yang belum terwakili.
- **4.2 Konsistensi Use Case dan Activity Diagram:** bandingkan aktor, pemicu, alur utama, alternatif, dan hasil.
- **4.3 Konsistensi Context Diagram dan DFD Level 0:** bandingkan entitas eksternal serta aliran data pada batas sistem.
- **4.4 Konsistensi DFD Level 0 dan Level 1:** periksa dekomposisi dan balancing input/output.
- **4.5 Evaluasi Keterlacakan Kebutuhan:** periksa hubungan masalah, kebutuhan, user story, acceptance criteria, use case, diagram, dan pengujian.
- **4.6 Kesimpulan:** simpulkan kelengkapan dan konsistensi yang benar-benar diperiksa. Sebutkan kekurangan atau bagian yang belum dapat diverifikasi.

Gunakan tabel evaluasi dengan status seperti **Sesuai**, **Sebagian sesuai**, **Tidak sesuai**, atau **Belum dapat diverifikasi**, disertai bukti dan tindak lanjut.

---

## 6. Aturan ketepatan teknis SmartPOS

Bagian ini mencegah agent memakai istilah teknis yang tampak meyakinkan tetapi tidak sesuai implementasi.

### 6.1 Offline-first dan aplikasi desktop

- *Offline-first* berarti fungsi yang diklaim tetap dapat berjalan tanpa internet harus benar-benar menggunakan sumber daya lokal dan tidak bergantung pada request jaringan untuk alur tersebut.
- Jangan menyamakan aplikasi desktop dengan aplikasi yang otomatis dapat bekerja offline.
- Identifikasi fitur yang membutuhkan internet, misalnya update, lisensi, sinkronisasi, atau layanan eksternal, jika ada.
- Jelaskan cakupan offline secara spesifik, bukan “seluruh sistem 100% offline” kecuali semua fungsi dan ketergantungannya telah diverifikasi.
- Satu perangkat lokal bukan berarti otomatis aman dari kehilangan data. Backup dan restore harus diperiksa secara terpisah.

### 6.2 SQLite dan ACID

- SQLite mendukung transaksi ACID, tetapi klaim pada SmartPOS harus mengacu pada transaksi dan implementasi database yang benar-benar digunakan.
- Jangan menyatakan seluruh operasi sistem ACID-compliant hanya karena menggunakan SQLite.
- Periksa apakah perubahan transaksi penjualan, detail penjualan, pembayaran, dan stok dilakukan dalam batas transaksi yang tepat.
- Bedakan ACID dari autentikasi, enkripsi, isolasi proses Electron, dan backup; semuanya merupakan topik berbeda.

### 6.3 HPP rata-rata tertimbang bergerak

- Pastikan rumus dan cakupan komoditas cocok dengan implementasi.
- Rumus dasar saat ada penerimaan persediaan baru:

  `Biaya rata-rata baru = (Nilai persediaan sebelum penerimaan + Nilai pembelian baru) / (Kuantitas sebelum penerimaan + Kuantitas pembelian baru)`

- Jangan menyatakan semua transaksi penjualan memperbarui rata-rata biaya. Dalam metode rata-rata bergerak, pembaruan umumnya terjadi saat penerimaan/pembelian persediaan; penjualan menggunakan biaya rata-rata yang berlaku.
- Periksa konversi satuan, biaya tambahan, retur, stok negatif, pembulatan, dan transaksi pembelian yang dibatalkan jika fungsi tersebut ada.
- Jangan mengklaim kesesuaian akuntansi secara luas hanya berdasarkan nama metode. Jelaskan metode dan aturan yang benar-benar diimplementasikan.

### 6.4 Persediaan LPG dan tabung

- Bedakan **isi gas sebagai barang dagangan** dan **tabung sebagai wadah fisik/aset yang berpindah** apabila model bisnis dan implementasi memang memisahkannya.
- Gunakan status hanya sesuai aturan aplikasi, misalnya tabung isi, tabung kosong, atau tabung dalam pengiriman; jangan mengasumsikan status yang tidak ada.
- Sistem lokal hanya dapat mencatat informasi pengiriman/penerimaan tabung kepada agen. Jangan menyatakan dapat memantau stok fisik di agen secara langsung jika tidak ada integrasi atau konfirmasi eksternal.
- Jangan menyebut “Pertamina” sebagai penerima/pemasok tertentu kecuali hubungan tersebut benar-benar sesuai objek usaha dan data yang tersedia.
- Bedakan mekanisme LPG bersubsidi dan non-subsidi jika terdapat aturan atau alur yang berbeda.

### 6.5 Pembayaran

- Bedakan pencatatan metode pembayaran dengan verifikasi pembayaran otomatis.
- Transfer bank atau QRIS yang dicatat manual tidak boleh disebut integrasi bank/payment gateway.
- Jelaskan apakah satu transaksi mendukung satu metode atau pembayaran campuran hanya jika perilakunya sudah dipastikan.

### 6.6 Laporan keuangan

- Bedakan omzet/penjualan, HPP, laba kotor, biaya operasional, dan laba bersih.
- Jangan menyebut “laba bersih riil” jika pencatatan biaya, pajak, retur, penyusutan, dan komponen relevan lainnya tidak lengkap.
- Gunakan istilah “ringkasan”, “estimasi”, atau “laporan berdasarkan data yang dicatat” bila cakupannya terbatas.

### 6.7 Printer dan timbangan

- Bedakan pencetakan melalui driver/Windows Print Spooler, direct socket, dan metode lain berdasarkan implementasi aktual.
- Input angka hasil timbangan secara manual bukan integrasi timbangan digital.
- Sebutkan ukuran kertas dan model printer hanya jika sesuai konfigurasi/perangkat yang didukung.

---

## 7. Standar bahasa dan penyajian akademik

### 7.1 Gaya bahasa

Gunakan bahasa Indonesia formal, efektif, objektif, dan langsung pada pokok pembahasan.

- Gunakan kalimat yang jelas dan tidak terlalu panjang.
- Satu paragraf membahas satu gagasan utama.
- Hindari bahasa promosi seperti “revolusioner”, “sangat canggih”, “sempurna”, “paling optimal”, “solusi terbaik”, atau “kelas industri”.
- Hindari pengulangan gagasan yang sama antar-subbagian.
- Jangan menggunakan istilah teknis bahasa Inggris jika padanan Indonesia sudah jelas; istilah teknis yang memang lazim dapat ditulis miring pada penyebutan yang sesuai.
- Definisikan singkatan saat pertama kali digunakan, misalnya Harga Pokok Penjualan (HPP), Software Requirements Specification (SRS), dan Requirements Traceability Matrix (RTM).
- Gunakan istilah secara konsisten: “kasir”, “pemilik usaha”, “penerimaan barang”, “persediaan”, “tabung isi”, “tabung kosong”, dan “agen”.
- Hindari kata ganti percakapan “kami”, “kita”, “kamu”, atau “Anda” dalam uraian analisis, kecuali pada kata pengantar.

### 7.2 Istilah dan konsistensi penamaan

- Gunakan nama **SmartPOS** secara konsisten.
- Judul sistem mengikuti judul yang telah ditetapkan dalam dokumen, kecuali pengguna meminta perubahan.
- Gunakan “LPG tabung 3 kg” atau “LPG” secara konsisten sesuai konteks.
- Gunakan “beras dan telur” untuk komoditas yang dikelola berdasarkan satuan berat hanya jika hal tersebut benar-benar sesuai implementasi.
- Gunakan istilah **HPP** secara konsisten setelah definisi pertama.
- Gunakan *moving weighted average* hanya jika implementasi benar-benar menerapkan rata-rata tertimbang bergerak.
- Hindari istilah “dual-stock closed-loop”, “total asset”, atau nama variabel teknis dalam narasi akademik kecuali telah didefinisikan dan sesuai model aktual.
- Nama menu, aktor, proses, data store, aliran data, dan ID kebutuhan harus konsisten pada seluruh bab.

### 7.3 Tata paragraf dan tabel

- Hindari bullet yang terlalu panjang jika dapat dijelaskan dengan paragraf formal.
- Gunakan tabel untuk perbandingan, inventaris kebutuhan, hak akses, dan evaluasi konsistensi.
- Setiap tabel dan gambar harus diberi nomor, judul, serta dirujuk dalam narasi.
- Setiap diagram harus memiliki penjelasan fungsi dan batas pembahasannya.
- Pastikan diagram dapat dibaca ketika diekspor ke PDF; jangan menggunakan gambar kecil atau teks yang terpotong.

---

## 8. Referensi dan sitasi

1. Gunakan sumber primer atau sumber resmi untuk statistik, kebijakan, regulasi, dan standar.
2. Verifikasi judul dokumen, penerbit/penulis, tahun, tanggal, dan URL sebelum memasukkan ke daftar pustaka.
3. Jangan membuat referensi, DOI, nomor regulasi, halaman, atau tautan.
4. Statistik nasional hanya mendukung konteks nasional; jangan menggunakannya untuk membuktikan kondisi operasional objek penelitian.
5. Klaim kondisi usaha harus merujuk pada hasil observasi/wawancara atau bukti internal, bukan artikel umum tentang UMKM.
6. Gunakan format APA edisi ke-7 secara konsisten, kecuali dosen memberikan format khusus.
7. Pastikan setiap sitasi dalam teks memiliki entri daftar pustaka dan sebaliknya.
8. Klaim “lebih dari 85% transaksi perdagangan bahan pokok dilakukan toko sembako dan pangkalan LPG” **tidak boleh digunakan** kecuali agent menemukan sumber primer yang secara eksplisit mendukung angka, definisi transaksi, cakupan komoditas, wilayah, periode, dan metode pengukurannya.
9. Jangan menambahkan sumber eksternal hanya untuk memperbanyak daftar pustaka.

---

## 9. Aturan perubahan dokumen dan repository

- Pekerjaan default adalah **audit dan dokumentasi**, bukan implementasi fitur.
- Jangan mengubah kode aplikasi, skema database, konfigurasi, atau dependency untuk menyesuaikan laporan.
- Jangan menjalankan migrasi, seeder, reset, atau perintah yang dapat mengubah data tanpa instruksi eksplisit dan lingkungan uji yang aman.
- Jangan menghapus diagram, catatan, komentar, atau file pengguna tanpa alasan dan persetujuan yang jelas.
- Pertahankan struktur folder dan gaya dokumen yang sudah ada selama tidak bertentangan dengan soal UTS.
- Bila mengedit laporan, lakukan perubahan terarah dan pertahankan isi yang sudah benar.
- Jangan mengganti fakta yang belum diketahui dengan asumsi. Buat daftar “perlu konfirmasi” yang spesifik.
- Jangan menyatakan pekerjaan selesai jika ada bagian wajib yang belum diperiksa.

---

## 10. Alur kerja dan keluaran yang diharapkan dari AI agent

Setiap kali diminta mengaudit atau menyusun laporan, lakukan urutan berikut:

### Keluaran A — Audit implementasi

Berikan ringkasan repository, daftar modul, fitur terverifikasi, fitur parsial, fitur belum terverifikasi, dan fitur di luar cakupan. Sertakan bukti untuk setiap kesimpulan penting.

### Keluaran B — Matriks kesesuaian soal UTS

Petakan seluruh butir soal UTS ke bagian laporan yang sudah ada. Gunakan status:

- Terpenuhi;
- Terpenuhi sebagian;
- Belum terpenuhi;
- Tidak relevan (dengan alasan).

### Keluaran C — Daftar inkonsistensi

Tunjukkan perbedaan antara laporan, kode, database, perilaku aplikasi, bukti elisitasi, dan diagram. Urutkan berdasarkan dampak akademik dan teknis.

### Keluaran D — Usulan revisi

Berikan teks pengganti yang siap dimasukkan ke laporan. Setiap perubahan harus mempertahankan fakta implementasi dan mengikuti struktur soal UTS. Jelaskan asumsi atau kekosongan bukti secara terpisah, jangan menyisipkannya sebagai fakta.

### Keluaran E — Pemeriksaan akhir

Sebelum menyatakan selesai, periksa:

- seluruh bagian wajib UTS sudah tersedia;
- tidak ada fitur fiktif atau klaim tanpa bukti;
- istilah dan nama fitur konsisten;
- ID FR/NFR, Use Case, diagram, dan RTM selaras;
- aliran data Context Diagram dan DFD Level 0 konsisten;
- DFD Level 1 memenuhi balancing;
- skenario use case dan Activity Diagram konsisten;
- sitasi dan daftar pustaka dapat diverifikasi;
- bahasa formal, ringkas, dan tidak repetitif;
- batasan implementasi dinyatakan secara jujur.

### Format ringkasan akhir agent

Akhiri setiap pekerjaan besar dengan format:

1. **Yang telah diperiksa:** sumber, modul, bagian laporan, atau diagram yang benar-benar ditinjau.
2. **Temuan utama:** fakta, ketidaksesuaian, dan kekurangan bukti.
3. **Perubahan yang dilakukan:** bagian dokumen yang direvisi.
4. **Belum dapat dipastikan:** pertanyaan atau bukti yang masih dibutuhkan.
5. **Status:** selesai, selesai sebagian, atau terblokir.

---

## 11. Prinsip keputusan terakhir

Jika harus memilih antara laporan yang terdengar lengkap dan laporan yang sesuai bukti, **pilih laporan yang sesuai bukti**.

Jika implementasi berbeda dari rancangan lama, dokumentasikan implementasi yang aktual dan jelaskan perbedaannya. Jika fitur belum ada, jangan menuliskannya sebagai fitur tersedia. Jika data lapangan belum tersedia, nyatakan keterbatasan bukti dan jangan mengarang hasil wawancara.

Tujuan akhir laporan SmartPOS bukan membuat sistem terlihat lebih hebat daripada kenyataannya, melainkan menunjukkan bahwa kelompok mampu menganalisis sistem yang benar-benar ada, menyusun kebutuhan secara terukur, memodelkannya dengan notasi yang tepat, dan mengevaluasi konsistensi hasil analisis secara objektif.
