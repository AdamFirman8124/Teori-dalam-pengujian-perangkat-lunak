# Daftar Harga Saham (Keputusan 0.9) — File B

Diakses: 2026-10-22. Mata uang: USD. Biaya dihitung dari token input/output yang dilaporkan API (tidak termasuk cache). Tidak ada diskon free-tier, cache, batch, atau regional.

| Backbone | Referensi | Input / 1M | Output / 1M | Sumber | Catatan |
|---|---|---:|---:|---|---|
| B1 | OpenAI GPT-5.6 Sol | $4.00 | $20.00 | https://developers.openai.com/api/docs/models/gpt-5.6-sol.md | Estimasi paid-equivalent. Harga promosi dinyatakan tersedia setidaknya hingga 2026-11-21. Endpoint sebenarnya melaporkan `auto`; identitas seller tidak terverifikasi. |
| B2 | `auto` (sama seperti B1, sementara) | $4.00 | $20.00 | https://developers.openai.com/api/docs/models/gpt-5.6-sol.md | **Deviasi File B**: B2 saat ini berbagi endpoint/kunci/kontfigurasi dengan B1. Dasar biaya sama dengan estimasi B1. Ganti ketika backbone B2 asli diverifikasi. |

Aturan perhitungan:
- `cost_usd = (tokens_in × harga_input) + (tokens_out × harga_output) / 1.000.000`
- Jangan memperoleh biaya dari tagihan *free tier* ($0 USD) atau dari tanggal daftar harga yang berbeda (larangan 12).
