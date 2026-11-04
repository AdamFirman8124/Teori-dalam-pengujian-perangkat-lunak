# Laporan Eksperimen CodaMOSA vs CoverUp

## 1. Status

Dokumen ini dibuat otomatis dari artefak pipeline. Angka hasil hanya diisi dari data yang benar-benar diukur; angka dummy File A tidak digunakan sebagai target atau hasil.

- Probe endpoint: **selesai**
- Pilot R=2: **selesai (64/64 OK)**
- Run utama R=10: **selesai (11683 run tercatat)**

## 2. Interpretasi Rancangan

File B bersifat otoritatif. Pipeline ini mengukur CodaMOSA, CoverUp, dan baseline Pynguin pada MT dan CM dengan dua backbone LLM (`B1 = gpt-5.6-sol`, `B2 = glm-5.3-flash`), serta menggabungkan hasil baseline MuTAP (`B1`) pada suite MT menggunakan skema hasil yang sama.

Perbandingan tool pada suite yang sama bersifat berpasangan per unit. Perbandingan MT dengan CM untuk tool yang sama bersifat deskriptif karena unit MT dan CM tidak berpasangan.

## 3. Inventaris Dataset

| Suite | Definisi satu task | Tersedia | Dipakai pilot | Dipakai run utama |
|---|---|---|---|---|
| MT | Satu fungsi benchmark dalam satu modul f001–f163 | 163 | 5 | 163 |
| CM | Satu modul Python pada satu baris cm_modules.csv | 425 | 3 | 40 |
| Total | — | 588 | 8 | 203 |

Inventaris mentah berisi **163 MT + 425 CM = 588 task**. Sesuai File B, run utama tidak memakai seluruh CM; ia memakai seluruh 163 MT dan sampel CM bertingkat sebanyak 40, sehingga terdapat **203 unit analisis utama**.

### Sampel CM per proyek

| Proyek | Jumlah |
|---|---|
| PySnooper | 1 |
| ansible | 10 |
| black | 1 |
| dataclasses-json | 1 |
| flutils | 1 |
| httpie | 3 |
| isort | 1 |
| py-backwards | 2 |
| pyMonet | 1 |
| pypara | 1 |
| python-semantic-release | 1 |
| pytutils | 1 |
| sty | 1 |
| tornado | 1 |
| typesystem | 4 |
| youtube-dl | 10 |

### Sampel CM per stratum

| Stratum | Jumlah |
|---|---|
| L0B0 | 6 |
| L0B1 | 6 |
| L1B0 | 5 |
| L1B1 | 5 |
| L1B2 | 4 |
| L2B0 | 4 |
| L2B1 | 5 |
| L2B2 | 5 |

Deviasi yang disetujui: stratum L0B2 kosong pada populasi aktual, sehingga sampel mencakup seluruh delapan stratum non-kosong, bukan memaksakan stratum kesembilan.

## 4. Matriks Run

| Tahap | Jumlah run |
|---|---|
| Pilot: (5 MT + 3 CM) × (Pynguin + 2 tool × 2 backbone) × R=2 | 80 |
| Utama (matriks lokal): (163 MT + 40 CM) × (Pynguin + 2 tool × 2 backbone) × R=10 | 10150 |
| Total gabungan (+ MuTAP MT B1: 1.533 run) | 11683 |

## 5. Model dan Probe

| Backbone | Requested | Returned | Function calling | Status/Error |
|---|---|---|---|---|
| B1 | gpt-5.6-sol | gpt-5.6-sol | True | PASS |
| B2 | glm-5.3-flash | glm-5.3-flash | True | PASS |

B1 dilaporkan sebagai `gpt-5.6-sol` ($4.00/M input, $20.00/M output) dan B2 sebagai `glm-5.3-flash` ($0.15/M input, $0.50/M output). Seluruh log panggilan mentah tersimpan di `results/raw/*/llm_log.jsonl`.

## 6. Hasil Pilot

| Suite | Tool | Backbone | Run tercatat | OK | Gagal | Biaya USD |
|---|---|---|---|---|---|---|
| CM | CodaMOSA | B1 | 6 | 6 | 0 | 2.913744 |
| CM | CodaMOSA | B2 | 6 | 6 | 0 | 3.129988 |
| CM | CoverUp | B1 | 6 | 6 | 0 | 0.402708 |
| CM | CoverUp | B2 | 6 | 6 | 0 | 0.331296 |
| MT | CodaMOSA | B1 | 10 | 10 | 0 | 0.452280 |
| MT | CodaMOSA | B2 | 10 | 10 | 0 | 0.685280 |
| MT | CoverUp | B1 | 10 | 10 | 0 | 0.428944 |
| MT | CoverUp | B2 | 10 | 10 | 0 | 0.430608 |

## 7. Hasil Utama

| Suite | Tool | Backbone | Run tercatat | OK | Gagal | Biaya USD |
|---|---|---|---|---|---|---|
| CM | CodaMOSA | B1 | 400 | 302 | 98 | 730.245664 |
| CM | CodaMOSA | B2 | 400 | 74 | 326 | 1.089649 |
| CM | CoverUp | B1 | 400 | 261 | 139 | 185.821952 |
| CM | CoverUp | B2 | 400 | 79 | 321 | 2.643813 |
| CM | Pynguin | - | 400 | 242 | 158 | 0.000000 |
| MT | CodaMOSA | B1 | 1630 | 1444 | 186 | 284.064988 |
| MT | CodaMOSA | B2 | 1630 | 1284 | 346 | 3.062507 |
| MT | CoverUp | B1 | 1630 | 1605 | 25 | 75.783284 |
| MT | CoverUp | B2 | 1630 | 1424 | 206 | 1.899333 |
| MT | MuTAP | B1 | 1533 | 1200 | 333 | 43.710728 |
| MT | Pynguin | - | 1630 | 1589 | 41 | 0.000000 |

Analisis akhir menggunakan mean, median, dan standard deviation; Wilcoxon signed-rank berpasangan; koreksi Holm; Vargha–Delaney A12; dan bootstrap CI 95% untuk selisih mean.

### 7.1. Uji Berpasangan Antar-Tool (RQ1 — Tabel V)

| Suite | Metrik | Backbone | Perbandingan | n | W/T/L | A12 | Delta Mean | p (Holm) |
|---|---|---|---|---|---|---|---|---|
| MT | ms | B1 | MuTAP vs Pynguin | 110 | 83/20/7 | 0.800 | 31.15 | 4.577e-13 |
| MT | ms | B1 | MuTAP vs CodaMOSA | 110 | 16/78/16 | 0.484 | -0.63 | 1 |
| MT | ms | B1 | MuTAP vs CoverUp | 111 | 23/79/9 | 0.545 | 1.45 | 0.7051 |
| MT | ms | B1 | CoverUp vs Pynguin | 152 | 107/30/15 | 0.771 | 32.48 | 1.568e-16 |
| MT | ms | B1 | CoverUp vs CodaMOSA | 152 | 11/97/44 | 0.440 | -1.52 | 0.03799 |
| MT | ms | B1 | CodaMOSA vs Pynguin | 152 | 115/27/10 | 0.799 | 34.01 | 2.111e-18 |
| CM | bc | B1 | CoverUp vs Pynguin | 22 | 14/5/3 | 0.726 | 33.35 | 0.186 |
| CM | bc | B1 | CoverUp vs CodaMOSA | 28 | 24/1/3 | 0.875 | 53.80 | 0.00182 |
| CM | bc | B1 | CodaMOSA vs Pynguin | 29 | 0/17/12 | 0.404 | -14.34 | 0.0294 |
| CM | ms | B1 | CoverUp vs Pynguin | 13 | 0/12/1 | 0.462 | -7.69 | 1 |
| CM | ms | B1 | CoverUp vs CodaMOSA | 16 | 0/14/2 | 0.438 | -9.38 | 0.9438 |
| CM | ms | B1 | CodaMOSA vs Pynguin | 24 | 3/20/1 | 0.541 | 6.25 | 1 |
| MT | ms | B2 | CoverUp vs Pynguin | 152 | 109/29/14 | 0.780 | 33.17 | 1.325e-17 |
| MT | ms | B2 | CoverUp vs CodaMOSA | 152 | 11/96/45 | 0.432 | -2.01 | 0.0007729 |
| MT | ms | B2 | CodaMOSA vs Pynguin | 151 | 116/28/7 | 0.814 | 35.16 | 6.715e-19 |
| CM | bc | B2 | CoverUp vs Pynguin | 19 | 13/5/1 | 0.712 | 33.18 | 0.1062 |
| CM | bc | B2 | CoverUp vs CodaMOSA | 16 | 14/1/1 | 0.854 | 53.30 | 0.0294 |
| CM | bc | B2 | CodaMOSA vs Pynguin | 21 | 0/11/10 | 0.374 | -23.39 | 0.05537 |
| CM | ms | B2 | CoverUp vs Pynguin | 19 | 0/17/2 | 0.447 | -10.53 | 0.9438 |
| CM | ms | B2 | CoverUp vs CodaMOSA | 17 | 0/13/4 | 0.382 | -13.80 | 0.5248 |
| CM | ms | B2 | CodaMOSA vs Pynguin | 21 | 3/17/1 | 0.545 | 4.03 | 1 |

### 7.2. Efek Backbone & Linear Mixed-Effects Model (RQ2 — Tabel VI & VII)

| Suite | Metrik | Tool | Adaptasi | Mean B1 | Mean B2 | Delta (B1-B2) | Unit (n) |
|---|---|---|---|---|---|---|---|
| MT | ms | CodaMOSA | interface-only | 91.29 | 92.21 | -0.92 | 163 |
| MT | ms | CoverUp | none | 89.42 | 90.16 | -0.75 | 163 |
| CM | bc | CodaMOSA | interface-only | 17.85 | 17.09 | 0.76 | 37 |
| CM | bc | CoverUp | none | 76.04 | 74.41 | 1.63 | 31 |

| Suite | Metrik | Faktor | Estimasi | 95% CI | p-value | Varians (%) |
|---|---|---|---|---|---|---|
| MT | ms | Intercept (CodaMOSA, B1) | 87.685 | [85.492, 89.877] | 0 | - |
| MT | ms | Tool: CoverUp | 0.751 | [-0.074, 1.576] | 0.07432 | 0.14 |
| MT | ms | Backbone: B2 | 3.647 | [2.785, 4.51] | 1.173e-16 | 0.63 |
| MT | ms | CoverUp × B2 | -2.63 | [-3.811, -1.45] | 1.266e-05 | 0.25 |
| CM | bc | Intercept (CodaMOSA, B1) | 15.962 | [8.293, 23.632] | 4.515e-05 | - |
| CM | bc | Tool: CoverUp | 55.276 | [50.946, 59.606] | 3.657e-138 | 43.16 |
| CM | bc | Backbone: B2 | -3.637 | [-9.875, 2.601] | 0.2531 | 0.0 |
| CM | bc | CoverUp × B2 | 1.97 | [-6.876, 10.817] | 0.6625 | 0.01 |

### 7.3. Cost-Effectiveness Terhadap Baseline Pynguin (RQ3 — Tabel VIII)

| Suite | Tool | Backbone | Metrik | Median Tool | Baseline Pynguin | Delta E | Median Cost (USD) | CE Ratio |
|---|---|---|---|---|---|---|---|---|
| CM | CodaMOSA | B1 | bc | 0.0 | 0.0 | 0.0 | 1.858828 | 0.0 |
| CM | CodaMOSA | B2 | bc | 1.39 | 0.0 | 1.39 | 0.015483 | 89.7 |
| CM | CoverUp | B1 | bc | 100.0 | 0.0 | 100.0 | 0.566996 | 176.37 |
| CM | CoverUp | B2 | bc | 97.22 | 0.0 | 97.22 | 0.008461 | 11491.04 |
| MT | CodaMOSA | B1 | ms | 96.0 | 70.0 | 26.0 | 0.06389 | 406.95 |
| MT | CodaMOSA | B2 | ms | 96.0 | 70.0 | 26.0 | 0.00176 | 14769.58 |
| MT | CoverUp | B1 | ms | 92.31 | 70.0 | 22.31 | 0.040592 | 549.56 |
| MT | CoverUp | B2 | ms | 95.0 | 70.0 | 25.0 | 0.000854 | 29263.72 |
| MT | MuTAP | B1 | ms | 100.0 | 70.0 | 30.0 | 0.026824 | 1118.4 |

## 8. Profil Kegagalan & Task yang Dikeluarkan

| Suite | Tool | Backbone | Total | Gagal | Kategori Dominan | Jumlah Dominan | Fail Rate | >10% |
|---|---|---|---|---|---|---|---|---|
| CM | CodaMOSA | B1 | 400 | 98 | timeout | 49 | 24.5% | True |
| CM | CodaMOSA | B2 | 400 | 326 | timeout | 301 | 81.5% | True |
| CM | CoverUp | B1 | 400 | 139 | env | 53 | 34.8% | True |
| CM | CoverUp | B2 | 400 | 321 | timeout | 227 | 80.2% | True |
| CM | Pynguin | - | 400 | 158 | timeout | 109 | 39.5% | True |
| MT | CodaMOSA | B1 | 1630 | 186 | api | 122 | 11.4% | True |
| MT | CodaMOSA | B2 | 1630 | 346 | timeout | 295 | 21.2% | True |
| MT | CoverUp | B1 | 1630 | 25 | timeout | 24 | 1.5% | False |
| MT | CoverUp | B2 | 1630 | 206 | timeout | 196 | 12.6% | True |
| MT | MuTAP | B1 | 1533 | 333 | invalid_tests | 315 | 21.7% | True |
| MT | Pynguin | - | 1630 | 41 | timeout | 36 | 2.5% | False |

Daftar rinci tersedia di `results/analysis/excluded_tasks.csv` atau `results/pilot_analysis/excluded_tasks.csv`. Tidak ada task yang dikeluarkan untuk menyesuaikan hasil dengan File A.

## 9. Deviasi dari File B

1. File A memuat angka ilustratif bertanda dummy; angka tersebut tidak dipakai sebagai ekspektasi.
2. File B merevisi RQ3 menjadi cost-effectiveness; revisi ini mengalahkan rancangan korelasi karakteristik kode pada File A.
3. Populasi CM hanya memiliki delapan stratum tertil non-kosong (`L0B2` kosong pada populasi aktual); penggunaan delapan stratum telah disetujui.
4. Backbone B2 dijalankan terpisah ke `results/b2_results.csv` menggunakan model `glm-5.3-flash` dengan batas rate 50 RPM; sebagian baris awal B2 (686 run `ok`) direkam saat transisi endpoint `gpt-5.6-luna` sebelum distandarkan ke `glm-5.3-flash`.
5. Filter dependensi container (`py2exe`, `python_apt`) diterapkan di `src/tool_adapters.py` agar modul target CM dapat diuji di lingkungan container Linux.

## 10. Keterbatasan

- Identitas model upstream pada router pihak ketiga bergantung pada pelaporan metadata endpoint (`model_returned`).
- Perbandingan lintas dataset (MT vs CM) tidak berpasangan karena unit MT (fungsi tunggal) dan CM (modul utuh) berbeda.
- Pembatasan rate 50 RPM dan latensi penalaran pada B2 meningkatkan proporsi `timeout` dalam batas anggaran 600 detik per run pada modul CM berukuran besar.
- Efek kontaminasi data tetap mungkin karena benchmark MT dan CM bersifat publik.

## 11. Artefak Reproduksi

- `config/experiment.toml`: protokol mesin-baca (tanpa secrets)
- `experiment.ipynb`: kontrol dan observasi proses
- `scripts/setup.sh`: setup tunggal
- `scripts/run_experiment.py`: entry point tunggal dan resumable
- `results/module_characteristics.csv`, `results/cm_sample.csv`, `results/*matrix.csv`
- `results/results_combined.csv`: gabungan kanonik seluruh 11.683 run (B1, B2, Pynguin, MuTAP)
- `results/raw/<run_id>/`: request/response teredaksi
- `results/generated/<run_id>/`: generated tests dan logs
- `results/analysis/`: tabel statistik IV–IX, failure rate, task exclusion, dan deviations
- `results/figures/`: visualisasi boxplot (Figure 3), interaksi (Figure 4), dan Pareto frontier (Figure 5)
