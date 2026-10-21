# Protokol Eksperimen (Fase 0 & 7)

Status: **DRAF — belum `protocol-frozen`**.
Acuan: `pedoman_eksperimen_ai_friendly.md` v1.2 dan
`naskah_rancangan_bab_results_ai_friendly.md` (revisi 16 Oktober 2026).

## 0.1 Backbone B1 (proprietary)

- Transport: alias `auto` pada endpoint SrByte (`https://stream.srbyte.id/v1`).
- Backbone sebenarnya: `gpt-5.6-sol`, dikonfirmasi oleh penyedia.
- Penyedia **tidak** mengekspos ID model asli pada `/models` maupun pada field
  `model` respons. Karena itu:
  - request mengirim `auto`;
  - label hasil memakai `gpt-5.6-sol` (`MODEL_ALIASES=auto=gpt-5.6-sol`);
  - `provider_model=auto` disimpan di setiap baris untuk audit.
- Konsekuensi: `model_returned` tidak dapat diverifikasi otomatis. Ini dicatat
  sebagai ancaman validitas konstruk.

## 0.2 Backbone B2 (open-weight)

**BELUM DITETAPKAN.** Endpoint hanya mengekspos alias `auto`. B2 harus
model open-weight yang mendukung *function calling* (Cek C pada Fase 2).
Sampai B2 tersedia:

- RQ1, RQ3, dan Tabel IV baris B1 dapat dikerjakan;
- Tabel VI, Tabel VII, Gambar 4 tidak dapat diisi;
- pedoman 14.10 melarang memotong backbone secara permanen, jadi B2 harus
  dijalankan sebelum protokol dibekukan.

## 0.3 Mutation tool

MutPy 0.6.1 (in-process `FirstOrderMutator`, satu himpunan mutan per unit yang
dipakai ulang oleh semua tool). Alasan: himpunan mutan identik lintas tool
(pedoman 14.4) dan tidak memerlukan container tambahan.

## 0.4 k (pengulangan flaky)

`k = 5` (`FLAKY_REPEATS=5`), dijalankan dengan `pytest-repeat --count 5`.

## 0.5 Temperatur CodaMOSA

`0.8` (`CODAMOSA_TEMPERATURE=0.8`), sesuai konfigurasi `0.8-uninterp`.

## 0.6 Perlakuan mutan timeout

Mutan yang melewati batas 10 detik dicatat sebagai `n_mutant_timeout` dan
**tidak** dihitung terbunuh. MS = `n_killed / (n_killed + n_survived)`.

## 0.7 Batas modul per proyek (CM)

Maksimum **25%** dari ukuran sampel per proyek (`--max-project-share 0.25`).
Dengan sampel 40 modul, batasnya 10 modul per proyek.

## 0.8 Anggaran biaya dan waktu

- Waktu: target ≤ 3 hari wall-clock pada satu mesin.
- Biaya: tarif berbayar pada `docs/prices.md` (bukan free tier).

## 0.9 Daftar harga

Lihat `docs/prices.md`. Tanggal daftar harga: **21 Oktober 2026**.

## 0.10 Aturan waktu per run

| Aturan | Implementasi |
|---|---|
| W1 anggaran 600 s | `PAPER_BUDGET_SECONDS=600`; `COVERUP_TIMEOUT=600`; `CODAMOSA_SEARCH_SECONDS=600` |
| W2 jam mulai | `_started_ts` dicatat tepat sebelum proses generator berjalan; setup container tidak dihitung |
| W3 jam berhenti | Tool selesai sendiri (`hit_budget=0`) atau mencapai 600 s (`hit_budget=1`); suite yang tersimpan tetap dievaluasi |
| W4 Pynguin/CodaMOSA | `--maximum_search_time 600` |
| W5 waktu tunggu rate limit | `rate_limit_wait_s` dicatat; `wait_flag` diisi bila > 60 s |
| W6 evaluasi | Evaluasi memakai timeout tersendiri (600 s per suite, 60 s per tes) dan tidak mengurangi 600 s |
| W7 waktu RQ3 | `gen_time_s = wall_time_s - rate_limit_wait_s` |
| W8 paralelisme | `P=4` tetap; setiap container `--cpus 2 --memory 700m` |

## Cakupan unit

| Suite | Unit | Sumber |
|---|---|---|
| MT | 163 fungsi (penuh) | `dataset/coverup-eval/MuTAP-benchmarks/f001..f163` |
| CM | 40 modul (sampel bertingkat) | `experiment_results_linux/cm_sample.csv` |

Sampling CM mengikuti Fase 4: tertil LOC × tertil `n_branches`, seed
`20261021`, minimal 40 modul, maksimum 25% per proyek, 3 modul pilot
dikeluarkan dari sampel. Strata `L0B2` kosong secara alami (tidak ada modul
< 94 LOC dengan > 24 cabang) dan dicatat di `docs/sanity_report.md`.

## Tool yang dijalankan

| Tool | Versi | Peran |
|---|---|---|
| CoverUp | 0.6.3 | generator LLM |
| CodaMOSA | 0.19.0 (fork) | generator LLM |
| Pynguin (DYNAMOSA) | 0.19.0 | baseline non-LLM |
| MuTAP | — | tidak dijalankan di mesin ini (data dari kolaborator) |

## Evaluasi

`coverage.py 7.16.2` untuk LC/BC, MutPy 0.6.1 untuk MS, `pytest 9.1.1` untuk
suite akhir dan flaky, `radon 6.0.1` untuk LOC/SLOC.
