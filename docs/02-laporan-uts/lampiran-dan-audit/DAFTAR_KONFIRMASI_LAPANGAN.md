# DAFTAR KONFIRMASI LAPANGAN (INSTRUMEN ELISITASI LANJUTAN)
## Panduan Wawancara & Observasi Lapangan Pemilik Toko dan Kasir Sembako & Gas LPG
*Dokumen Kerja Tim Rekayasa Perangkat Lunak — Proyek SmartPOS*

---

## 1. Latar Belakang dan Tujuan Dokumen

Sesuai dengan prinsip integritas akademik dan anti-asumsi pada rekayasa perangkat lunak, **analisis kebutuhan pada laporan UTS SmartPOS disusun berdasarkan inspeksi kode sumber (*reverse engineering*), pengujian sistem yang tersedia, serta analisis dokumen teknis**. Wawancara mendalam dan observasi empiris langsung dengan pemilik toko dan kasir di lapangan **belum dilaksanakan**.

Oleh karena itu, dokumen ini disusun sebagai instrumen elisitasi formal yang memuat butir-butir pertanyaan terstruktur untuk divalidasikan kepada narasumber lapangan pada tahap pengembangan atau evaluasi operasional selanjutnya.

---

## 2. Profil Narasumber yang Dibutuhkan

| Target Narasumber | Peran / Posisi | Tujuan Elisitasi |
| :--- | :--- | :--- |
| **Narasumber 1** | Pemilik Usaha / Pengelola Toko & Pangkalan LPG | Mengonfirmasi alur pasokan barang grosir, kebijakan harga komoditas berfluktuasi, pengelolaan aset tabung gas fisik ke agen Pertamina, serta kebutuhan laporan keuangan riil. |
| **Narasumber 2** | Staf Kasir / Operator Meja Transaksi | Mengonfirmasi kebiasaan transaksi harian pembeli eceran ("Beli Rp"), alur penukaran tabung gas konsumen, tata cara penerimaan pembayaran non-tunai, dan kendala operasional meja kasir. |

---

## 3. Daftar Pertanyaan Terstruktur Berdasarkan Domain Bisnis

### Domain A: Kebiasaan Transaksi Kasir & Fitur "Beli Rp"
1. **Pertanyaan untuk Kasir**: Seberapa sering konsumen membeli komoditas curah (beras/telur) dengan menyebutkan batasan nominal uang rupiah (contoh: *"Beli beras Rp15.000"* atau *"Beli telur Rp8.000"*), dibandingkan dengan menyebutkan bobot kilogram langsung?
2. **Pertanyaan untuk Kasir**: Bagaimana langkah yang saat ini dilakukan kasir ketika pembeli meminta transaksi berbasis nominal uang tersebut? Apakah kasir menghitung pembagian menggunakan kalkulator meja, ponsel, atau langsung menaksir timbangan?
3. **Pertanyaan untuk Kasir & Pemilik**: Terkait pembulatan pecahan desimal hasil konversi nominal uang ke kilogram, berapa angka desimal di belakang koma yang dianggap lazim dan dapat terbaca pada timbangan meja toko (misal 2 desimal atau 3 desimal)?
4. **Pertanyaan untuk Kasir**: Apakah terdapat batas minimal nominal transaksi eceran yang dilayani oleh toko?

### Domain B: Pengelolaan Multi-Satuan & Satuan Kemasan
1. **Pertanyaan untuk Pemilik**: Apa saja satuan kemasan yang digunakan pemasok saat mengirimkan beras ke toko (misal karung 25 kg, 50 kg, atau karung beras bermerk khusus)?
2. **Pertanyaan untuk Pemilik**: Untuk komoditas telur ayam, bagaimana kemasan pengiriman dari peternak/distributor (apakah peti kayu 10 kg, 15 kg, atau rak karton/tray isi 30 butir)?
3. **Pertanyaan untuk Kasir**: Apakah toko juga melayani penjualan beras dalam bentuk karung utuh kepada konsumen akhir atau warung makan sekitar? Jika ya, apakah ada perbedaan harga per kilogram dibanding pembelian eceran?

### Domain C: Sirkulasi Fisik Tabung Gas LPG (Konsumen & Agen)
1. **Pertanyaan untuk Kasir**: Ketika konsumen membeli gas LPG (3 kg, 5.5 kg, atau 12 kg), apakah selalu membawa tabung kosong untuk ditukar?
2. **Pertanyaan untuk Kasir & Pemilik**: Bagaimana prosedur yang diterapkan jika konsumen ingin membeli tabung perdana (membeli isi gas beserta tabungnya tanpa membawa tabung kosong)? Berapa selisih harga atau uang jaminan tabung yang dibebankan?
3. **Pertanyaan untuk Pemilik**: Bagaimana prosedur penukaran tabung kosong pangkalan ke truk agen penyalur resmi Pertamina?
   - Apakah tabung kosong diangkut terlebih dahulu lalu tabung isi diantar kemudian pada hari yang berbeda (siklus 2-tahap)?
   - Ataukah pertukaran tabung kosong dengan tabung isi selalu terjadi bersamaan di lokasi pangkalan?
4. **Pertanyaan untuk Pemilik**: Bagaimana pemilik saat ini mengawasi jumlah tabung kosong yang sedang berada di luar toko (sedang dalam proses isi ulang di agen) agar tidak terjadi selisih atau kehilangan aset tabung?
5. **Pertanyaan untuk Pemilik**: Seberapa sering pemilik melakukan pemeriksaan fisik (*stock opname*) terhadap total tabung di pangkalan? Apakah sering ditemukan tabung rusak/bocor (*defect*) saat pengiriman?

### Domain D: Fluktuasi Harga Pasokan & Kebijakan HPP
1. **Pertanyaan untuk Pemilik**: Seberapa sering harga pasokan dari distributor beras dan telur mengalami kenaikan atau penurunan harga?
2. **Pertanyaan untuk Pemilik**: Ketika pasokan baru tiba dengan harga beli yang lebih mahal sementara stok lama masih tersisa di gudang:
   - Apakah pemilik langsung menaikkan harga jual produk saat itu juga?
   - Ataukah pemilik menghitung harga rata-rata tertimbang (*moving weighted average*) dari sisa stok lama dan pasokan baru?
3. **Pertanyaan untuk Pemilik**: Apakah margin keuntungan ditetapkan dalam persentase tetap (markup) atau nominal rupiah per kilogram?

### Domain E: Metode Pembayaran & Verifikasi Non-Tunai
1. **Pertanyaan untuk Kasir**: Metode pembayaran apa saja yang saat ini digunakan oleh konsumen (Tunai, Transfer Bank BCA/BRI/Mandiri, QRIS)?
2. **Pertanyaan untuk Kasir**: Untuk pembayaran QRIS atau transfer, bagaimana kasir memverifikasi bahwa pembayaran telah berhasil masuk ke rekening pemilik toko sebelum menyerahkan barang belanjaan?
3. **Pertanyaan untuk Pemilik**: Apakah pemilik menginginkan pencatatan uang masuk kasir dipisahkan secara tegas antara kas fisik tunai di laci (*cash drawer*) dengan saldo rekening bank?

### Domain F: Pencatatan Keuangan, Beban Operasional, & Laba Rugi
1. **Pertanyaan untuk Pemilik**: Pengeluaran operasional apa saja yang rutin dikeluarkan toko (seperti listrik PLN, sewa tempat, gaji karyawan, bensin armada angkutan, plastik pembungkus)?
2. **Pertanyaan untuk Pemilik**: Apakah pemilik mencampur uang kas toko dengan kebutuhan belanja pribadi rumah tangga? Jika ada kas keluar untuk keperluan pribadi, bagaimana hal itu dicatat saat ini?
3. **Pertanyaan untuk Pemilik**: Bagaimana pemilik saat ini mengetahui laba bersih toko dalam kurun waktu satu bulan?

### Domain G: Perangkat Keras, Printer Kasir, & Konektivitas
1. **Pertanyaan untuk Kasir & Pemilik**: Perangkat komputer apa yang digunakan di meja kasir (PC desktop atau laptop)? Sistem operasi apa yang terpasang (Windows 10 / Windows 11)?
2. **Pertanyaan untuk Pemilik**: Jenis printer apa yang tersedia atau direncanakan untuk mencetak struk belanja (printer thermal 58mm atau 80mm? Koneksi via kabel USB atau jaringan LAN/Wi-Fi)?
3. **Pertanyaan untuk Kasir**: Apakah setiap transaksi wajib dicetak struk fisiknya, ataukah opsi cetak struk hanya diberikan jika diminta oleh pembeli?
4. **Pertanyaan untuk Pemilik**: Bagaimana kondisi kestabilan jaringan internet di lokasi toko? Mengapa pendekatan aplikasi desktop yang dapat berjalan tanpa internet (*offline-first*) dipandang lebih tepat dibanding aplikasi web kasir berbasis langganan bulanan (*cloud SaaS*)?

---

## 4. Lembar Catatan Hasil Konfirmasi (Template)

Ketika sesi wawancara dan observasi lapangan telah dilaksanakan, tim rekayasa wajib mendokumentasikan hasilnya pada format berikut sebelum memperbarui naskah laporan:

- **Hari / Tanggal Pelaksanaan**: ____________________
- **Waktu & Durasi**: ____________________
- **Lokasi Toko / Pangkalan**: ____________________
- **Nama Narasumber**: ____________________
- **Jabatan / Peran**: [ ] Pemilik Toko  [ ] Kasir  [ ] Lainnya: _______
- **Ringkasan Jawaban & Temuan Faktual**:
  1. *Temuan Alur Transaksi & "Beli Rp"*:
  2. *Temuan Sirkulasi Tabung Gas*:
  3. *Temuan Penerimaan Barang & HPP*:
  4. *Temuan Pembayaran & Keuangan*:
  5. *Temuan Perangkat Keras & Infrastruktur*:
- **Dampak Perubahan terhadap Spesifikasi Kebutuhan (SRS)**:
  - Butir Kebutuhan Fungsional yang terkonfirmasi: ____________________
  - Butir Kebutuhan Fungsional yang memerlukan penyesuaian: ____________________
- **Tanda Tangan Pengonfirmasi / Pewawancara**: ____________________
