# Protokol Eksperimen — CodaMOSA vs CoverUp (File B, versi 1.2)

Status: **draft** — belum difreeze (belum ada tag `protocol-frozen`). File A tidak digunakan lagi; semua angka, tren, dan kesimpulan di File A dianggap dummy/ilhustrasi dan tidak digunakan sebagai target.

## Interpretasi rancangan (dikoreksi sesuai File B hanya)

- File B otoritatif untuk prosedur, skema data, dan aturan waktu.
- Ruang lingkup yang diukur di repositori ini: **CodaMOSA dan CoverUp** saja. Pynguin dan MuTAP dikerjakan oleh kolaboran, dengan skema hasil yang sama agar dapat digabungkan nanti.
- Desain yang diukur: `tool × suite × backbone` (2 tool × 2 suite × 2 backbone), R=10 untuk run utama, pilot R=2 (5 MT + 3 CM).
- File B revisi 19 Oktober 2026 mengubah RQ3 dari "korelasi karakteristik kode" menjadi **cost-effectiveness** (ΔE, cost_usd, CE, plot Pareto). File A (korelasi karakteristik kode) diabaikan.

## Keputusan yang tersisa (Fase 0, poin 0.1–0.10)

| No | Keputusan | Nilai | Keterangan |
|----|-----------|-------|------------|
| 0.1 | Backbone B1 (proprietary) | `entah/auto` pada endpoint `http://localhost:20128/v1` | Endpoint melaporkan `model_returned = auto`; identitas seller (gpt-5.6-sol) tidak terverifikasi |
| 0.2 | Backbone B2 (open-weight) | `entah/auto` pada endpoint yang sama (`LLM_BASE_URL_B2` / `LLM_API_KEY_B2`) | **Deviasi tercatat**: File B mengharapkan B2 terpisah dari B1; saat ini kedua route sama. Harus diganti sebelum simpulan dua backbone diambil |
| 0.3 | Mutation tool | Cosmic Ray 8.7.0 | Himpunan mutan bersama untuk semua tool/run |
| 0.4 | k (pengulangan deteksi flaky) | 5 | `--repeat-tests` pada CoverUp |
| 0.5 | Temperatur CodaMOSA | 0.8 | Konfigurasi asli `0.8-uninterp` |
| 0.6 | Perlakuan mutan timeout | Dihitung terbunuh, dilaporkan terpisah (`n_mutant_timeout`) | Tidak ditandai selesai saat timeout |
| 0.7 | Batas modul per proyek (CM sample) | Maksimal 25% sampel dari satu proyek | Terapkan saat sampling CM |
| 0.8 | Anggaran biaya & waktu maksimum | USD 900, 14 hari | Stop peluncuran pada 80%; henti pada 100% |
| 0.9 | Daftar harga `cost_usd` | USD 4.00/M input, USD 20.00/M output (paid-equivalent, OpenAI GPT-5.6 Sol) | Sumber: https://developers.openai.com/api/docs/models/gpt-5.6-sol.md, diakses 2026-10-22. B2 gunakan estimasi yang sama sementara route sama |
| 0.10 | Aturan waktu per run | W1–W8 (lihat bawah) | Budget 600 s, rate-limit wait ikut dihitung, `gen_time_s = wall − wait` |

### Aturan Waktu per Run (Keputusan 0.10)

- **W1:** 600 s wall-clock per run untuk pembangkitan tes.
- **W2:** Timer dimulai saat proses tool berjalan pada unit (setup container tidak dihitung).
- **W3:** Tool selesai sendiri (`hit_budget=0`), atau mencapai 600 s (SIGINT, tenggang 30 s → SIGKILL, `hit_budget=1`).
- **W4:** CodaMOSA `--maximum-search-time` 600 (turunkan ke 540 s pada pilot jika perlu agar total tetap 600 s).
- **W5:** `ratelimit_wait_s` ikut dihitung dalam 600 s; jika > 60 s, `wait_flag=1` dan ulang 1× di akhir blok.
- **W6:** Evaluasi tes/coverage/mutasi tidak mengurangi jatah 600 s (timeout sendiri).
- **W7:** `gen_time_s = wall-clock − ratelimit_wait_s`.
- **W8:** $P$ (paralelisme) tetap $\le$ jumlah inti CPU fisik. Setiap container bounded CPU/RAM yang sama.

## Aturan Fatal (Bagian 14 File B) yang dipatuhi

1. Run utama **tanpa** `llm_proxy` aktif: dilarang.
2. Raw validity dihitung dari suite akhir: dilarang.
3. `MS = 0` jika `n_mutants = 0`: dilarang (harus `NA`).
4. Himpunan mutan berbeda antar-tool/run: dilarang.
5. Coverage bawaan tool: dilarang (wajib `coverage.py`).
6. CoverUp melebihi 600 s: dilarang.
7. Versi model/tool/image berubah tengah jalan: dilarang.
8. Modul pilot masuk sampel CM atau data pilot digunakan di paper: dilarang.
9. Metode analisis berubah setelah melihat data: dilarang.
10. Jumlah backbone dipotong menjadi 1 demi menghemat biaya: dilarang.
11. API key disimpan di repositori/log/screenshot: dilarang.
12. Biaya dihitung dari tagihan *free tier* ($0 USD) atau dari tanggal daftar harga yang salah: dilarang.
13. Bandingkan total token antar-backbone dengan tokenizer berbeda: dilarang.
14. Waktu setup container/evaluasi masuk jatah 600 s: dilarang.
15. Ubah nilai $P$ tengah eksekusi blok: dilarang.

## Skema output yang diharapkan (Bagian 12–13 File B)

`results.csv` (31 kolom, satu baris per run): `run_id`, `suite`, `unit_id`, `project`, `tool`, `tool_version`, `backbone`, `model_requested`, `model_returned`, `run_idx`, `seed`, `start_time`, `end_time`, `budget_s`, `gen_time_s`, `ratelimit_wait_s`, `hit_budget`, `wait_flag`, `attempt`, `status`, `error_category`, `n_api_calls`, `tokens_in`, `tokens_out`, `cost_usd`, `n_raw_proposals`, `n_raw_pass`, `n_tests_final`, `n_pass_first`, `n_fail`, `n_error`, `n_timeout`, `k_reruns`, `n_flaky`, `n_valid`, `lines_total`, `lines_exec`, `branches_total`, `branches_exec`, `mutation_tool`, `n_mutants`, `n_killed`, `n_survived`, `n_mutant_timeout`, `sim_max_median`.

`module_characteristics.csv`: 425 baris, kolom `unit_id`, `project`, `loc`, `sloc`, `n_branches`, `stratum`, `is_pilot`, `in_sample`.

`cm_sample.csv`: 3 pilot + ≥40 sampel, 25% per proyek cap, seed 20261022.

## Tabel yang harus dihasilkan (Fase 5 dry run dan Fase 10)

- Tabel IV: Efektivitas per tool × backbone (median atas unit).
- Tabel V: Perbandingan berpasangan (Wilcoxon signed-rank, koreksi Holm, A12).
- Tabel VI: Efek backbone per generator.
- Tabel VII: Model mixed-effects.
- Tabel VIII: Cost-effectiveness (ΔE, CE).
- Tabel IX: Uji statistik biaya (13 uji Wilcoxon + Holm).
- Gambar 3: Boxplot coverage/MS.
- Gambar 4: Interaction plot.
- Gambar 5: Pareto plot (biaya vs efektivitas, skala log).
