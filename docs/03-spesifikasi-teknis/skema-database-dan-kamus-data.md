# Skema Basis Data & Spesifikasi Teknis Relasi
## Dokumentasi Basis Data SQLite Sistem SmartPOS

SmartPOS menggunakan engine basis data **SQLite 3** melalui native C++ binding `better-sqlite3`. Basis data disimpan sebagai berkas lokal mandiri pada path direktori pengguna (`%APPDATA%/SmartPOS/database/app.db`).

---

## 1. Diagram Relasi Entitas (Entity-Relationship Diagram)

```mermaid
erDiagram
    users ||--o{ transactions : "memproses (cashier_name)"
    products ||--o{ transaction_items : "tercatat_di"
    transactions ||--|{ transaction_items : "memiliki"
    products ||--o{ stock_movements : "memiliki_riwayat"
    gas_stock ||--o{ gas_transactions : "memiliki_mutasi"
    gas_stock ||--o| products : "direpresentasikan_di"

    users {
        int id PK
        string username UK
        string password
        string full_name
        string role
        int active
        string created_at
    }

    products {
        int id PK
        string name
        string category
        string unit
        string secondary_unit
        real secondary_conversion
        real purchase_price
        real selling_price
        real no_exchange_price
        real secondary_price
        real stock
        real minimum_stock
        int gas_id FK
        int active
    }

    transactions {
        int id PK
        string invoice_number UK
        string transaction_date
        string cashier_name
        string payment_method
        real total_amount
        real discount
        real final_amount
        real paid_amount
        real change_amount
        string note
        string status
    }

    transaction_items {
        int id PK
        int transaction_id FK
        int product_id FK
        string product_name
        string category
        real quantity
        string unit
        real price
        real subtotal
    }

    gas_stock {
        int id PK
        string gas_name UK
        int filled_stock
        int empty_stock
        int total_cylinders
        real purchase_price
        real selling_price
        real no_exchange_price
        int minimum_stock
    }

    gas_transactions {
        int id PK
        int gas_id FK
        string transaction_type
        int quantity
        int filled_before
        int empty_before
        int filled_after
        int empty_after
        int total_before
        int total_after
        real amount
        string description
        string date
    }

    stock_movements {
        int id PK
        int product_id FK
        string type
        string reason
        real quantity
        string unit
        real purchase_price
        string supplier
        real stock_before
        real stock_after
        string date
    }

    expenses {
        int id PK
        string category
        string description
        real amount
        string date
    }

    income_extra {
        int id PK
        string description
        real amount
        string date
    }

    settings {
        int id PK
        string store_name
        string address
        string phone
        string receipt_note
        string printer_mode
    }
```

---

## 2. Integritas Transaksional (ACID Guarantee)

Untuk menjamin tidak terjadinya inkonsistensi saldo stok jika terjadi gangguan listrik (*power loss*), seluruh mutasi lintas tabel dibungkus di dalam transaksi SQLite atomik:

```javascript
// Contoh transaksi atomik pada database/transactions.js
const checkout = db.transaction((payload) => {
  // 1. Simpan Header Transaksi
  const stmtTx = db.prepare('INSERT INTO transactions (...) VALUES (...)');
  const result = stmtTx.run(...);
  const txId = result.lastInsertRowid;

  // 2. Simpan Item & Potong Stok Produk
  for (const item of payload.items) {
    db.prepare('INSERT INTO transaction_items (...) VALUES (...)').run(txId, ...);
    
    // Potong stok produk sembako / gas isi
    db.prepare('UPDATE products SET stock = stock - ? WHERE id = ?').run(item.quantity, item.productId);
  }

  return { id: txId, invoiceNumber: payload.invoiceNumber };
});
```
Jika terjadi kegagalan sistem di tengah perulangan item, SQLite secara otomatis melakukan *rollback* penuh, sehingga saldo stok tidak akan pernah berkurang separuh jalan.
