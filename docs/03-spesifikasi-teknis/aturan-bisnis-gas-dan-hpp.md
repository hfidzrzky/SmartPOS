# Aturan Bisnis Khusus UMKM: Gas LPG, Konversi Eceran & HPP Tertimbang
## Dokumentasi Algoritma dan Formula Bisnis SmartPOS

Dokumen ini mendokumentasikan spesifikasi formula matematika dan aturan logika bisnis (*business rules*) yang diimplementasikan pada basis kode **SmartPOS**.

---

## 1. Logika Bisnis Sirkulasi Tabung Gas LPG (*Dual-Stock Closed-Loop*)

Inventaris gas LPG memiliki karakteristik unik karena produk memiliki aset fisik wadah (tabung). SmartPOS memisahkan inventaris menjadi 3 metrik stok:
- $S_{\text{isi}}$: Stok tabung berisi gas yang siap dijual (`filled_stock`).
- $S_{\text{kosong}}$: Stok tabung kosong yang menunggu pengisian ulang (`empty_stock`).
- $S_{\text{total}}$: Total aset tabung fisik yang berada di toko (`total_cylinders`), di mana secara fisik:
  $$S_{\text{total}} = S_{\text{isi}} + S_{\text{kosong}}$$

### Matriks Perpindahan Stok Gas:

| Jenis Transaksi | Perubahan $S_{\text{isi}}$ | Perubahan $S_{\text{kosong}}$ | Perubahan $S_{\text{total}}$ Toko | Keterangan Alur Fisik |
| :--- | :---: | :---: | :---: | :--- |
| **1. Tukar Konsumen (*Refill*)** | $-N$ | $+N$ | $0$ (Tetap) | Konsumen menyerahkan tabung kosong dan membawa pulang tabung isi. Total aset tabung toko tidak berubah. |
| **2. Tukar Agen: Kirim Kosong** | $0$ | $-N$ | $-N$ | Truk agen mengangkut tabung kosong keluar dari toko. $N$ tabung berada dalam perjalanan/pengisian di agen. |
| **3. Tukar Agen: Terima Isi** | $+N$ | $0$ | $+N$ | Truk agen mengantar tabung isi ke toko. Total fisik di toko kembali pulih ke jumlah semula. |
| **4. Jual Perdana (Tanpa Tukar)** | $-N$ | $0$ | $-N$ | Konsumen membeli tabung baru beserta isinya. Aset tabung berpindah kepemilikan ke konsumen. |
| **5. Tambah Tabung Baru** | $+N_{\text{isi}}$ | $+N_{\text{kosong}}$ | $+ (N_{\text{isi}} + N_{\text{kosong}})$ | Toko membeli aset wadah tabung tambahan dari distributor. |
| **6. Opname / Penyesuaian** | $\pm \Delta_{\text{isi}}$ | $\pm \Delta_{\text{kosong}}$ | $\pm (\Delta_{\text{isi}} + \Delta_{\text{kosong}})$ | Koreksi selisih hitung fisik saat audit persediaan berkala. |

---

## 2. Algoritma HPP Rata-Rata Tertimbang (*Moving Weighted Average Cost*)

Ketika terjadi pasokan barang masuk baru pada produk beras atau telur dengan harga beli yang berfluktuasi dari pemasok, sistem secara otomatis mereposisi Harga Pokok Penjualan (HPP) per kilogram menggunakan formula:

$$\text{HPP}_{\text{baru}} = \frac{(Q_{\text{lama}} \times \text{HPP}_{\text{lama}}) + (Q_{\text{masuk}} \times P_{\text{beli\_baru}})}{Q_{\text{lama}} + Q_{\text{masuk}}}$$

### Notasi Variabel:
- $Q_{\text{lama}}$: Kuantitas persediaan fisik barang di toko sebelum pasokan tiba (`stock`).
- $\text{HPP}_{\text{lama}}$: Harga pokok pembelian per unit dasar sebelum transaksi baru (`purchase_price`).
- $Q_{\text{masuk}}$: Kuantitas pasokan baru yang diterima dalam unit dasar ($kg$). Jika pasokan dalam kemasan karung ($K$), maka:
  $$Q_{\text{masuk}} = K \times \text{rasio\_konversi}$$
- $P_{\text{beli\_baru}}$: Harga beli per unit dasar pada transaksi pengadaan saat ini.

### Contoh Kasus Riil:
1. Toko memiliki stok awal beras 100 kg dengan HPP Rp 12.000/kg (Nilai aset persediaan = Rp 1.200.000).
2. Toko menerima pasokan 2 karung beras (1 karung = 50 kg, total $Q_{\text{masuk}} = 100\text{ kg}$) dengan harga beli baru Rp 14.000/kg (Total beli baru = Rp 1.400.000).
3. Kalkulasi HPP Baru:
   $$\text{HPP}_{\text{baru}} = \frac{1.200.000 + 1.400.000}{100 + 100} = \frac{2.600.000}{200} = \text{Rp } 13.000/\text{kg}$$
4. Stok fisik toko otomatis menjadi $200\text{ kg}$ dan nilai persediaan tercatat Rp 2.600.000.

---

## 3. Algoritma Konversi Instan "Beli Rp"

Pada komoditas curah yang dijual secara eceran (beras dan telur), konsumen seringkali bertransaksi berdasarkan nilai nominal uang tunai yang mereka bawa:

$$Q_{\text{dihitung}} = \frac{N_{\text{nominal}}}{P_{\text{jual\_kg}}}$$

- $N_{\text{nominal}}$: Nominal rupiah yang diinput kasir pada dialog "Beli Rp" (misal Rp 15.000).
- $P_{\text{jual\_kg}}$: Harga jual produk per kilogram (misal Rp 14.000 / kg).
- $Q_{\text{dihitung}}$: Kuantitas berat kilogram pecahan desimal (misal $\frac{15.000}{14.000} \approx 1.0714\text{ kg}$).

### Penanganan Presisi Mata Uang:
Untuk mencegah selisih hitung uang kembalian akibat pembulatan desimal, sistem menetapkan:
- Subtotal baris item dikunci tepat sebesar $N_{\text{nominal}}$ yang dibayarkan konsumen.
- Kuantitas desimal ditampilkan dengan presisi 2 angka di belakang koma untuk kebutuhan penimbangan fisik kasir.

---

## 4. Agregasi Finansial & Laba Bersih Riil Toko

Sistem menyajikan perhitungan performa keuangan toko dengan memisahkan modal perolehan barang dagangan dari beban operasional toko:

$$\text{Laba Kotor} = \text{Omzet Penjualan} - \sum \text{HPP Barang Terjual}$$
$$\text{Laba Bersih} = \text{Laba Kotor} + \text{Pendapatan Lain} - \text{Beban Operasional Toko}$$

- **Omzet Penjualan**: Agregasi `final_amount` seluruh transaksi kasir yang berstatus 'selesai'.
- **HPP Barang Terjual**: Jumlah akumulasi kuantitas terjual dikalikan HPP modal masing-masing item saat transaksi.
- **Pendapatan Lain**: Pemasukan ekstra di luar kasir (tabel `income_extra`).
- **Beban Operasional Toko**: Seluruh pengeluaran utilitas listrik, gaji pegawai, sewa tempat, dan bensin angkutan toko (tabel `expenses`).
