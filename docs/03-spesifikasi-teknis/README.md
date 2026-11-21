# 03 - Spesifikasi Teknis & Referensi Pengembang

Subfolder ini memuat dokumentasi arsitektur internal, keamanan, basis data, dan aturan bisnis matematis sistem **SmartPOS** yang ditujukan sebagai referensi teknis pengembang (*developer reference*) dan portofolio teknis sistem.

## Daftar Berkas:
1. [arsitektur-dan-keamanan-electron.md](arsitektur-dan-keamanan-electron.md) — Arsitektur multi-proses Electron 31, protokol IPC asinkron, isolasi proses aman via `contextBridge`, dan enkripsi kata sandi `scrypt`.
2. [skema-database-dan-kamus-data.md](skema-database-dan-kamus-data.md) — Diagram Relasi Entitas (ERD), spesifikasi skema SQLite, indeks query, dan penjaminan integritas data ACID melalui transaksi database.
3. [aturan-bisnis-gas-dan-hpp.md](aturan-bisnis-gas-dan-hpp.md) — Penjelasan detail formula matematika sirkulasi tabung gas LPG (*dual-stock closed-loop*), algoritma *Moving Weighted Average Cost* HPP, dan konversi kuantitas pecahan "Beli Rp".
