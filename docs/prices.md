# Daftar Harga (Keputusan 0.9)

Tanggal daftar harga: **21 Oktober 2026**.
Biaya dihitung dari tarif **berbayar**, bukan dari tagihan *free tier*
(pedoman 14.12).

## Model B1 — `gpt-5.6-sol`

| Komponen | Harga per 1 juta token |
|---|---|
| Input | USD 1,25 |
| Output | USD 10,00 |

Sumber: halaman harga resmi penyedia, diakses 21 Oktober 2026.

> **Catatan verifikasi:** nilai di atas harus dicocokkan ulang dengan halaman
> harga resmi sebelum `protocol-frozen`. Bila penyedia mengubah tarif,
> perbarui file ini dan catat tanggalnya; jangan mencampur tarif dari dua
> tanggal berbeda dalam satu analisis (pedoman 14.12).

## Model B2

Belum ditetapkan (lihat `docs/protocol.md` poin 0.2). Harga B2 wajib
ditambahkan sebelum blok B2 dijalankan.

## Rumus

```
cost_usd = tokens_in/1e6 * harga_in + tokens_out/1e6 * harga_out
```

Diterapkan pada tahap analisis, bukan saat run, agar perubahan harga tidak
memaksa pengulangan eksekusi.
