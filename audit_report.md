# Laporan Audit & Ringkasan Eksperimen (CodaMOSA vs CoverUp)

**Tanggal Audit:** 6 November 2026  
**Sumber Data Kanonik:** `results/results_combined.csv` (11.683 run utama) & `results/pilot_results.csv` (64 run pilot)  
**Konfigurasi Protokol:** `config/experiment.toml` (`R = 10` run utama, `R = 2` pilot, anggaran 600 detik/run, evaluasi flaky 5×)

---

## 1. Ringkasan Eksekutif untuk Dosen

1. **Status Eksekusi Selesai:**
   - **Pilot (`R = 2`):** 64/64 run berhasil (`100% ok`), total biaya **$8,77** (`results/pilot_results.csv`).
   - **Run Utama (`R = 10`):** Total **11.683 run** tercatat dari 11 kombinasi (`Suite × Tool × Backbone`) pada **203 unit analisis utama** (163 fungsi `MT` + 40 modul sampel bertingkat `CM` dari 16 proyek dan 8 stratum `L0B0`–`L2B2`).
2. **Temuan RQ1 (Efektivitas Tool):**
   - **Suite `MT` (Fungsi Tunggal):** Seluruh generator berbasis LLM mengungguli baseline genetik murni `Pynguin` secara signifikan pada *Mutation Score* (`ms` median: `MuTAP` **100,0%**, `CodaMOSA` **96,0%–100,0%**, `CoverUp` **92,3%–94,4%**, vs `Pynguin` **68,0%**; Wilcoxon berpasangan $p_{\text{holm}} < 10^{-12}$, Vargha–Delaney $A_{12} = 0,77\text{–}0,81$).
   - **Suite `CM` (Modul Kompleks Dunia Nyata):** `CoverUp` mendominasi *Branch Coverage* (`bc` median **95,2%** pada `B1` dan **100,0%** pada `B2`; mean **73,4%** dan **72,1%**), mengungguli `CodaMOSA` (`bc` median **0,0%**, mean **16,7%** dan **15,4%**, $A_{12} = 0,85\text{–}0,88$, $p_{\text{holm}} \le 0,029$) serta `Pynguin` (`bc` median **0,0%**, mean **31,8%**).
3. **Temuan RQ2 (Algoritma vs Backbone LLM):**
   - Berdasarkan *Linear Mixed-Effects Model* (`metric ~ tool * backbone + (1 | unit)`), pada modul kompleks `CM`, **pilihan algoritma/tool (`CoverUp` vs `CodaMOSA`) menyumbang 43,16% dari total varians** ($\beta = +55,276$, $p = 3,66 \times 10^{-138}$), sedangkan pergantian backbone (`B1` vs `B2`) dan interaksinya tidak signifikan ($p > 0,25$, varians $\le 0,01\%$).
   - Pada fungsi sederhana `MT`, baik algoritma maupun backbone hanya menyumbang $< 1\%$ varians (`Tool` 0,14%, `Backbone` 0,63%, `Interaksi` 0,25%) karena efek *ceiling* (seluruh tool LLM mencapai cakupan mendekati 100%).
4. **Temuan RQ3 (Cost-Effectiveness):**
   - Pada `B1` (`gpt-5.6-sol`), `CoverUp` pada suite `CM` **3,3× lebih hemat biaya** dan **2,7× lebih cepat** dibanding `CodaMOSA` (median **$0,567** vs **$1,859** per run; **230,6 dtk** vs **622,0 dtk**; *hit budget* 600 dtk pada `CodaMOSA` mencapai **96,0%** vs `CoverUp` **0,0%**).
   - Penggunaan model ekonomis `B2` (`glm-5.3-flash`, $0,15/M input, $0,50/M output) menurunkan biaya median per run hingga **35–65× lebih murah** dibanding `B1` (`CM CoverUp B2` **$0,0085**/run dengan $\text{CE} = 11.491,04$; `MT CoverUp B2` **$0,00085**/run dengan $\text{CE} = 29.263,72$).

---

## 2. Audit Kelengkapan Perulangan (`R = 10`) & Unit Analisis

| Suite | Tool | Backbone | Run Tercatat | Run `ok` (%) | Run `failed` (%) | Unit Total | Unit $\ge 1$ `ok` | Unit $10/10$ `ok` | Unit $0/10$ `ok` | Median `ok`/Unit | Biaya Total (USD) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `CM` | CodaMOSA | `B1` | 400 / 400 | 302 (75,5%) | 98 (24,5%) | 40 | 37 | 8 | 3 | 8,5 | $730,25 |
| `CM` | CodaMOSA | `B2` | 400 / 400 | 74 (18,5%) | 326 (81,5%) | 40 | 28 | 0 | 12 | 2,0 | $1,09 |
| `CM` | CoverUp | `B1` | 400 / 400 | 261 (65,2%) | 139 (34,8%) | 40 | 31 | 10 | 9 | 9,0 | $185,82 |
| `CM` | CoverUp | `B2` | 400 / 400 | 79 (19,8%) | 321 (80,2%) | 40 | 23 | 0 | 17 | 1,0 | $2,64 |
| `CM` | Pynguin | `-` | 400 / 400 | 242 (60,5%) | 158 (39,5%) | 40 | 29 | 9 | 11 | 8,0 | $0,00 |
| `MT` | CodaMOSA | `B1` | 1.630 / 1.630 | 1.444 (88,6%) | 186 (11,4%) | 163 | 162 | 59 | 1 | 9,0 | $284,06 |
| `MT` | CodaMOSA | `B2` | 1.630 / 1.630 | 1.284 (78,8%) | 346 (21,2%) | 163 | 162 | 23 | 1 | 8,0 | $3,06 |
| `MT` | CoverUp | `B1` | 1.630 / 1.630 | 1.605 (98,5%) | 25 (1,5%) | 163 | 163 | 138 | 0 | 10,0 | $75,78 |
| `MT` | CoverUp | `B2` | 1.630 / 1.630 | 1.424 (87,4%) | 206 (12,6%) | 163 | 163 | 49 | 0 | 9,0 | $1,90 |
| `MT` | MuTAP | `B1` | **1.533 / 1.630** | 1.200 (78,3%) | 333 (21,7%) | **154** | 121 | 119 | 33 | 10,0 | $43,71 |
| `MT` | Pynguin | `-` | 1.630 / 1.630 | 1.589 (97,5%) | 41 (2,5%) | 163 | 162 | 156 | 1 | 10,0 | $0,00 |

### Catatan Audit Kelengkapan Matriks:
- **Duplikasi `run_id`:** `0` (seluruh 11.683 baris unik).
- **10 dari 11 konfigurasi** memiliki tepat **100% baris matriks tercatat** (`400/400` pada `CM`, `1.630/1.630` pada `MT`).
- **97 baris belum tercatat pada `MT MuTAP B1`** (`results/mutap_results.csv`): Unit `f154` baru memiliki 3 dari 10 perulangan, dan 9 unit (`f155`–`f163`) belum tersedia dari impor kolaborator.

---

## 3. Audit Identitas Model (`model_requested` vs `model_returned`)

| Backbone | Tool | `model_requested` | `model_returned` | Run `ok` | Run `failed` | Keterangan Audit |
|---|---|---|---|---|---|---|
| `-` | Pynguin | `-` | `-` | 1.831 | 199 | Baseline genetik DYNAMOSA (CPU murni tanpa LLM) |
| `B1` | CodaMOSA | `gpt-5.6-sol` | `gpt-5.6-sol` | 1.640 | 0 | Terverifikasi sesuai permintaan |
| `B1` | CodaMOSA | `gpt-5.6-sol` | `-` (kosong) | **106** | 284 | 106 run `ok` selesai 100% melalui eksplorasi genetik Pynguin/MOSA sebelum CodaMOSA perlu memanggil LLM (`cost_usd = 0`) |
| `B1` | CoverUp | `gpt-5.6-sol` | `gpt-5.6-sol` | 1.866 | 44 | Terverifikasi sesuai permintaan |
| `B1` | CoverUp | `gpt-5.6-sol` | `-` (kosong) | 0 | 120 | Gagal sebelum panggilan LLM (mis. error `env` modul) |
| `B1` | MuTAP | `gpt-5.6-sol` | `gpt-5.6-sol` | 1.200 | 0 | Terverifikasi sesuai permintaan |
| `B1` | MuTAP | `gpt-5.6-sol` | `-` (kosong) | 0 | 333 | Run gagal (`invalid_tests` / `crash`) |
| `B2` | CodaMOSA | `glm-5.3-flash` | `glm-5.3-flash` / `z-ai/*` / `zai-org/*` | **1.015** | 637 | Variasi alias upstream provider untuk model `GLM-5.3-Flash` |
| `B2` | CodaMOSA | `gpt-5.6-luna` | `gpt-5.6-luna` / `-` | **343** | 35 | Sisa checkpoint awal di `results/b2_results.csv` sebelum migrasi penuh `B2` ke `glm-5.3-flash` |
| `B2` | CoverUp | `glm-5.3-flash` | `glm-5.3-flash` / `z-ai/*` / `zai-org/*` | **1.160** | 504 | Variasi alias upstream provider untuk model `GLM-5.3-Flash` |
| `B2` | CoverUp | `gpt-5.6-luna` | `gpt-5.6-luna` / `-` | **343** | 23 | Sisa checkpoint awal di `results/b2_results.csv` sebelum migrasi penuh `B2` ke `glm-5.3-flash` |

---

## 4. Audit Kategori Kegagalan (`status == "failed"`)

| Suite | Tool | Backbone | `timeout` | `api` | `env` | `invalid_tests` | `syntax` | `crash` | Total Gagal | Fail Rate |
|---|---|---|---|---|---|---|---|---|---|---|
| `CM` | CodaMOSA | `B1` | 49 | 30 | 9 | 10 | 0 | 0 | 98 | 24,5% |
| `CM` | CodaMOSA | `B2` | **301** | 18 | 2 | 3 | 0 | 2 | 326 | 81,5% |
| `CM` | CoverUp | `B1` | 46 | 19 | **53** | 0 | 20 | 1 | 139 | 34,8% |
| `CM` | CoverUp | `B2` | **227** | 0 | **73** | 0 | 20 | 1 | 321 | 80,2% |
| `CM` | Pynguin | `-` | **109** | 0 | 5 | 0 | 0 | **44** | 158 | 39,5% |
| `MT` | CodaMOSA | `B1` | 21 | **122** | 3 | 40 | 0 | 0 | 186 | 11,4% |
| `MT` | CodaMOSA | `B2` | **295** | 29 | 2 | 20 | 0 | 0 | 346 | 21,2% |
| `MT` | CoverUp | `B1` | 24 | 1 | 0 | 0 | 0 | 0 | 25 | **1,5%** |
| `MT` | CoverUp | `B2` | **196** | 0 | 8 | 0 | 0 | 2 | 206 | 12,6% |
| `MT` | MuTAP | `B1` | 0 | 0 | 0 | **315** | 0 | 18 | 333 | 21,7% |
| `MT` | Pynguin | `-` | 36 | 0 | 4 | 0 | 0 | 1 | 41 | **2,5%** |

### Akar Penyebab Kegagalan Utama:
1. **Dominasi `timeout` pada `B2` (`CM` 80–81%, `MT` 12–21%):** Antrean *rate-limiter* global 50 RPM (`src/rate_gate.py`) yang dibagi lintas *worker* paralel ditambah latensi generasi token `glm-5.3-flash` membuat eksekusi multi-iterasi pada modul besar melewati batas waktu 600 detik.
2. **Error `env` pada `CM CoverUp` (`B1` 53 run, `B2` 73 run):** Beberapa modul dunia nyata (`flutils.setuputils.cfg`, `dataclasses_json.undefined`, `py_backwards.transformers.string_types`) memiliki ketergantungan lingkungan/paket spesifik saat dieksekusi langsung oleh `CoverUp`.
3. **Error `api` pada `CodaMOSA B1` (`MT` 122 run, `CM` 30 run):** Terjadi pada batch awal sebelum mekanisme *auto-retry* khusus `error_category == "api"` diterapkan di `scripts/run_experiment.py`.
4. **Error `invalid_tests` pada `MuTAP B1` (315 run):** Seluruh kandidat test yang dihasilkan gagal saat verifikasi `pytest` (`n_raw_pass == 0`).

---

## 5. Audit Integritas Metrik pada Run Berhasil (`status == "ok"`)

1. **Line Coverage (`lc`):** `lines_total` terisi **100%** pada seluruh 9.504 run `ok` (0 *missing value*).
2. **Branch Coverage (`bc`):** Terdapat 58 fungsi pada suite `MT` yang bersifat sekuensial murni (tanpa percabangan `branches_total == 0`). Sesuai fungsi `derivatives()` di `scripts/analyze.py`, nilai `bc` pada fungsi tanpa cabang dikodekan sebagai `NaN` agar tidak mendistorsi rata-rata/median percabangan.
3. **Mutation Score (`ms`):** Pada suite `CM` (`B1`), sebanyak 224/302 run `CodaMOSA` dan 226/261 run `CoverUp` memiliki `n_mutants == 0` karena eksekusi mutasi *Cosmic Ray* dibatasi *evaluation timeout* 900 detik pada modul berukuran besar. Oleh karena itu, sesuai protokol File B, evaluasi efektifitas utama pada `CM` menggunakan **Branch Coverage (`bc`)**, sedangkan pada `MT` menggunakan **Mutation Score (`ms`)**.

---

## 6. Distribusi Lengkap Tabel Hasil per Research Question (RQ1, RQ2, RQ3)

Seluruh **3 Research Questions (RQ1, RQ2, RQ3)** telah **terjawab penuh** menggunakan Tabel IV s.d. Tabel IX di `results/analysis/`.

---

### RQ1: Efektivitas Tool & Validitas Test
> **Pertanyaan:** *Seberapa efektif CodaMOSA, CoverUp, MuTAP, dan Pynguin dalam menghasilkan unit test yang valid, mencapai cakupan kode (`lc`, `bc`), dan membunuh mutan (`ms`) pada benchmark fungsi tunggal (`MT`) dan modul dunia nyata (`CM`)?*  
> **Status:** **Terjawab Penuh** (Tabel IV & Tabel V).

#### Tabel IV — Ringkasan Efektivitas & Validitas (`results/analysis/table_iv_summary.csv`)

| Suite | Tool | Backbone | `rv` Mean / Med / SD (%) | `lc` Mean / Med / SD (%) | `bc` Mean / Med / SD (%) | `ms` Mean / Med / SD (%) |
|---|---|---|---|---|---|---|
| `CM` | CodaMOSA | `B1` | 3,49 / 0,00 / 13,35 | 33,46 / 21,25 / 32,92 | 16,75 / 0,00 / 27,33 | 10,26 / 0,00 / 30,54 |
| `CM` | CodaMOSA | `B2` | 5,37 / 0,00 / 14,60 | 33,89 / 26,19 / 31,69 | 15,44 / 0,00 / 26,07 | 14,45 / 0,00 / 34,98 |
| `CM` | CoverUp | `B1` | 32,47 / 20,00 / 35,12 | **77,60 / 99,09** / 31,63 | **73,39 / 95,24** / 37,33 | 0,00 / 0,00 / 0,00 |
| `CM` | CoverUp | `B2` | **83,47 / 100,00** / 27,19 | **76,97 / 100,00** / 33,47 | **72,14 / 100,00** / 38,18 | 0,00 / 0,00 / 0,00 |
| `CM` | Pynguin | `-` | — | 46,01 / 26,19 / 37,40 | 31,81 / 0,00 / 42,02 | 6,20 / 0,00 / 24,16 |
| `MT` | CodaMOSA | `B1` | 15,48 / 0,00 / 33,24 | 97,64 / 100,00 / 10,17 | 95,05 / 100,00 / 16,01 | 87,95 / **96,00** / 20,69 |
| `MT` | CodaMOSA | `B2` | 12,01 / 0,00 / 18,77 | 99,08 / 100,00 / 6,76 | 97,88 / 100,00 / 11,13 | **92,44 / 100,00** / 14,17 |
| `MT` | CoverUp | `B1` | 89,42 / 100,00 / 27,79 | **99,71 / 100,00** / 4,80 | **99,22 / 100,00** / 7,35 | 88,39 / 92,31 / 16,82 |
| `MT` | CoverUp | `B2` | 95,50 / 100,00 / 15,04 | **99,98 / 100,00** / 0,48 | **99,67 / 100,00** / 2,48 | 89,44 / 94,44 / 14,88 |
| `MT` | MuTAP | `B1` | **99,76 / 100,00** / 1,71 | 98,81 / 100,00 / 7,16 | 97,49 / 100,00 / 12,59 | **91,88 / 100,00** / 12,19 |
| `MT` | Pynguin | `-` | — | 98,23 / 100,00 / 8,87 | 94,99 / 100,00 / 17,49 | 57,36 / 68,00 / 36,86 |

#### Tabel V — Uji Statistik Berpasangan Wilcoxon, Koreksi Holm, & Vargha–Delaney $A_{12}$ (`results/analysis/table_v_paired_tests.csv`)

| Suite | Metrik | Backbone | Perbandingan (`A vs B`) | $n$ Unit | W / T / L | $A_{12}$ | $\Delta$ Mean (`A - B`) | 95% Bootstrap CI | Wilcoxon $W$ | $p_{\text{holm}}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| `MT` | `ms` | `B1` | `MuTAP vs Pynguin` | 110 | 83 / 20 / 7 | **0,800** | +31,15 | `[24,71, 37,78]` | 156,0 | **$4,58 \times 10^{-13}$** |
| `MT` | `ms` | `B1` | `MuTAP vs CodaMOSA` | 110 | 16 / 78 / 16 | 0,484 | -0,63 | `[-2,40, 1,20]` | 228,5 | $1,000$ |
| `MT` | `ms` | `B1` | `MuTAP vs CoverUp` | 111 | 23 / 79 / 9 | 0,545 | +1,45 | `[-0,34, 3,45]` | 176,5 | $0,7051$ |
| `MT` | `ms` | `B1` | `CoverUp vs Pynguin` | 152 | 107 / 30 / 15 | **0,771** | +32,48 | `[26,74, 38,46]` | 390,0 | **$1,57 \times 10^{-16}$** |
| `MT` | `ms` | `B1` | `CoverUp vs CodaMOSA` | 152 | 11 / 97 / 44 | 0,440 | -1,52 | `[-3,22, 0,21]` | 418,5 | **$0,0380$** |
| `MT` | `ms` | `B1` | `CodaMOSA vs Pynguin` | 152 | 115 / 27 / 10 | **0,799** | +34,01 | `[28,48, 39,70]` | 251,5 | **$2,11 \times 10^{-18}$** |
| `CM` | `bc` | `B1` | `CoverUp vs Pynguin` | 22 | 14 / 5 / 3 | **0,726** | +33,35 | `[8,84, 56,53]` | 28,0 | $0,1860$ |
| `CM` | `bc` | `B1` | `CoverUp vs CodaMOSA` | 28 | 24 / 1 / 3 | **0,875** | +53,80 | `[35,79, 71,11]` | 30,0 | **$0,0018$** |
| `CM` | `bc` | `B1` | `CodaMOSA vs Pynguin` | 29 | 0 / 17 / 12 | 0,404 | -14,34 | `[-24,97, -5,48]` | 0,0 | **$0,0294$** |
| `CM` | `ms` | `B1` | `CoverUp vs Pynguin` | 13 | 0 / 12 / 1 | 0,462 | -7,69 | `[-23,08, 0,00]` | 0,0 | $1,000$ |
| `CM` | `ms` | `B1` | `CoverUp vs CodaMOSA` | 16 | 0 / 14 / 2 | 0,438 | -9,38 | `[-25,00, 0,00]` | 0,0 | $0,9438$ |
| `CM` | `ms` | `B1` | `CodaMOSA vs Pynguin` | 24 | 3 / 20 / 1 | 0,541 | +6,25 | `[-8,33, 20,83]` | 3,0 | $1,000$ |
| `MT` | `ms` | `B2` | `CoverUp vs Pynguin` | 152 | 109 / 29 / 14 | **0,780** | +33,17 | `[27,53, 39,09]` | 297,5 | **$1,33 \times 10^{-17}$** |
| `MT` | `ms` | `B2` | `CoverUp vs CodaMOSA` | 152 | 11 / 96 / 45 | 0,432 | -2,01 | `[-3,61, -0,38]` | 301,0 | **$0,0008$** |
| `MT` | `ms` | `B2` | `CodaMOSA vs Pynguin` | 151 | 116 / 28 / 7 | **0,814** | +35,16 | `[29,58, 40,78]` | 163,5 | **$6,71 \times 10^{-19}$** |
| `CM` | `bc` | `B2` | `CoverUp vs Pynguin` | 19 | 13 / 5 / 1 | **0,712** | +33,18 | `[10,50, 53,99]` | 12,0 | $0,1062$ |
| `CM` | `bc` | `B2` | `CoverUp vs CodaMOSA` | 16 | 14 / 1 / 1 | **0,854** | +53,30 | `[31,77, 73,39]` | 6,0 | **$0,0294$** |
| `CM` | `bc` | `B2` | `CodaMOSA vs Pynguin` | 21 | 0 / 11 / 10 | 0,374 | -23,39 | `[-36,41, -11,57]` | 0,0 | $0,0554$ |
| `CM` | `ms` | `B2` | `CoverUp vs Pynguin` | 19 | 0 / 17 / 2 | 0,447 | -10,53 | `[-26,32, 0,00]` | 0,0 | $0,9438$ |
| `CM` | `ms` | `B2` | `CoverUp vs CodaMOSA` | 17 | 0 / 13 / 4 | 0,382 | -13,80 | `[-28,51, -2,94]` | 0,0 | $0,5248$ |
| `CM` | `ms` | `B2` | `CodaMOSA vs Pynguin` | 21 | 3 / 17 / 1 | 0,545 | +4,03 | `[-10,08, 18,32]` | 3,5 | $1,000$ |

---

### RQ2: Kontribusi Algoritma vs Backbone LLM
> **Pertanyaan:** *Seberapa besar variasi efektivitas yang disebabkan oleh perbedaan desain algoritma/tool dibandingkan perbedaan model backbone LLM (`B1 = gpt-5.6-sol` vs `B2 = glm-5.3-flash`)?*  
> **Status:** **Terjawab Penuh** (Tabel VI & Tabel VII).

#### Tabel VI — Efek Pergantian Backbone per Tool (`results/analysis/table_vi_backbone_effect.csv`)

| Suite | Metrik | Tool | Tingkat Adaptasi | Mean `B1` (%) | Mean `B2` (%) | $\Delta$ (`B1 - B2`) | Jumlah Unit ($n$) |
|---|---|---|---|---|---|---|---|
| `MT` | `ms` | CodaMOSA | `interface-only` | 91,29 | 92,21 | -0,92 | 163 |
| `MT` | `ms` | CoverUp | `none` | 89,42 | 90,16 | -0,75 | 163 |
| `CM` | `bc` | CodaMOSA | `interface-only` | 17,85 | 17,09 | +0,76 | 37 |
| `CM` | `bc` | CoverUp | `none` | 76,04 | 74,41 | +1,63 | 31 |

#### Tabel VII — Linear Mixed-Effects Model & Dekomposisi Varians (`results/analysis/table_vii_mixed_effects.csv`)
Model: `metric ~ C(tool) * C(backbone) + (1 | unit_id)` (Referensi: `CodaMOSA`, `B1`).

| Suite | Metrik | Faktor | Estimasi ($\beta$) | 95% CI | $p$-value | Kontribusi Varians (%) |
|---|---|---|---|---|---|---|
| `MT` | `ms` | Intercept (`CodaMOSA`, `B1`) | 87,685 | `[85,492, 89,877]` | $< 10^{-16}$ | — |
| `MT` | `ms` | `Tool: CoverUp` | +0,751 | `[-0,074, 1,576]` | $0,0743$ | 0,14% |
| `MT` | `ms` | `Backbone: B2` | +3,647 | `[2,785, 4,510]` | $1,17 \times 10^{-16}$ | 0,63% |
| `MT` | `ms` | `CoverUp × B2` | -2,630 | `[-3,811, -1,450]` | $1,27 \times 10^{-5}$ | 0,25% |
| `CM` | `bc` | Intercept (`CodaMOSA`, `B1`) | 15,962 | `[8,293, 23,632]` | $4,51 \times 10^{-5}$ | — |
| `CM` | `bc` | `Tool: CoverUp` | **+55,276** | `[50,946, 59,606]` | **$3,66 \times 10^{-138}$** | **43,16%** |
| `CM` | `bc` | `Backbone: B2` | -3,637 | `[-9,875, 2,601]` | $0,2531$ | 0,00% |
| `CM` | `bc` | `CoverUp × B2` | +1,970 | `[-6,876, 10,817]` | $0,6625$ | 0,01% |

---

### RQ3: Efisiensi Biaya & Cost-Effectiveness (CE)
> **Pertanyaan:** *Bagaimana perbandingan konsumsi token, waktu generasi, biaya moneter (USD), rasio Cost-Effectiveness ($\Delta E / \text{Cost}$ terhadap baseline Pynguin), dan posisi Pareto frontier antar-tool?*  
> **Status:** **Terjawab Penuh** (Tabel VIII, Tabel VIII-CE, Tabel IX, & Data Figure 5 Pareto).

#### Tabel VIII-A — Konsumsi Token, Waktu, Biaya, & Hit-Budget (`results/analysis/table_viii_cost.csv`)

| Suite | Tool | Backbone | Token In (Mean / Med) | Token Out (Mean / Med) | Biaya USD (Mean / Med / SD) | Waktu `gen_time_s` (Mean / Med) | Hit Budget 600s (%) |
|---|---|---|---|---|---|---|---|
| `CM` | CodaMOSA | `B1` | 144.122 / 107.434 | 92.077 / 68.871 | $2,4180 / $1,8588 / $2,0478 | 613,3 / 622,0 dtk | **96,0%** |
| `CM` | CodaMOSA | `B2` | 30.672 / 18.741 | 20.248 / 18.337 | $0,0147 / $0,0155 / $0,0080 | 629,5 / 630,4 dtk | **96,7%** |
| `CM` | CoverUp | `B1` | 73.039 / 62.114 | 16.040 / 13.687 | $0,6129 / $0,5670 / $0,4108 | **247,7 / 230,6 dtk** | **0,0%** |
| `CM` | CoverUp | `B2` | 21.371 / 17.764 | 12.865 / 10.416 | **$0,0096 / $0,0085** / $0,0083 | 290,8 / 289,9 dtk | **0,0%** |
| `CM` | Pynguin | `-` | — | — | $0,0000 / $0,0000 / $0,0000 | 591,9 / 624,2 dtk | **92,6%** |
| `MT` | CodaMOSA | `B1` | 6.007 / 3.148 | 8.635 / 2.535 | $0,1967 / $0,0639 / $0,5151 | 73,4 / 35,3 dtk | 4,6% |
| `MT` | CodaMOSA | `B2` | 1.314 / 650 | 4.376 / 3.235 | $0,0024 / $0,0018 / $0,0020 | 324,2 / 342,6 dtk | 4,9% |
| `MT` | CoverUp | `B1` | 6.381 / 6.405 | 1.082 / 674 | $0,0472 / $0,0406 / $0,0288 | 32,1 / 16,0 dtk | **0,0%** |
| `MT` | CoverUp | `B2` | 2.095 / 1.590 | 1.809 / 1.231 | **$0,0012 / $0,0009** / $0,0013 | 165,4 / 104,4 dtk | **0,0%** |
| `MT` | MuTAP | `B1` | **519 / 365** | 1.718 / 1.273 | $0,0364 / $0,0268 / $0,0344 | **15,3 / 6,9 dtk** | **0,0%** |
| `MT` | Pynguin | `-` | — | — | $0,0000 / $0,0000 / $0,0000 | 73,5 / 8,0 dtk | 8,3% |

#### Tabel VIII-B — Rasio Cost-Effectiveness ($\text{CE} = \Delta E / \text{Median Cost}$) (`results/analysis/table_viii_cost_effectiveness.csv`)

| Suite | Tool | Backbone | Metrik Evaluasi | Median Tool (%) | Baseline Pynguin (%) | $\Delta E$ (Poin %) | Median Cost (USD) | Rasio $\text{CE}$ ($\Delta E / \text{USD}$) |
|---|---|---|---|---|---|---|---|---|
| `CM` | CodaMOSA | `B1` | `bc` | 0,00 | 0,00 | 0,00 | $1,858828 | 0,00 |
| `CM` | CodaMOSA | `B2` | `bc` | 1,39 | 0,00 | +1,39 | $0,015483 | 89,70 |
| `CM` | CoverUp | `B1` | `bc` | **100,00** | 0,00 | **+100,00** | $0,566996 | **176,37** |
| `CM` | CoverUp | `B2` | `bc` | **97,22** | 0,00 | **+97,22** | **$0,008461** | **11.491,04** |
| `MT` | CodaMOSA | `B1` | `ms` | 96,00 | 70,00 | +26,00 | $0,063890 | 406,95 |
| `MT` | CodaMOSA | `B2` | `ms` | 96,00 | 70,00 | +26,00 | $0,001760 | 14.769,58 |
| `MT` | CoverUp | `B1` | `ms` | 92,31 | 70,00 | +22,31 | $0,040592 | 549,56 |
| `MT` | CoverUp | `B2` | `ms` | 95,00 | 70,00 | +25,00 | **$0,000854** | **29.263,72** |
| `MT` | MuTAP | `B1` | `ms` | **100,00** | 70,00 | **+30,00** | $0,026824 | **1.118,40** |

#### Tabel IX — Uji Berpasangan Wilcoxon untuk Biaya Moneter (`results/analysis/table_ix_cost_wilcoxon.csv`)

| Backbone | Suite | Perbandingan (`Right vs Left`) | $n$ Unit | Median $\Delta$ Cost (USD) | Wilcoxon $W$ | $p$-value | $p_{\text{holm}}$ |
|---|---|---|---|---|---|---|---|
| `B1` | `CM` | `CoverUp vs CodaMOSA` | 29 | **-$1,372528** | 5,0 | $3,73 \times 10^{-8}$ | **$1,12 \times 10^{-7}$** |
| `B1` | `MT` | `CoverUp vs CodaMOSA` | 120 | **-$0,017025** | 1163,0 | $1,04 \times 10^{-10}$ | **$4,17 \times 10^{-10}$** |
| `B1` | `MT` | `MuTAP vs CodaMOSA` | 120 | **-$0,030751** | 573,0 | $1,19 \times 10^{-15}$ | **$5,93 \times 10^{-15}$** |
| `B1` | `MT` | `MuTAP vs CoverUp` | 120 | **-$0,009231** | 2454,0 | $0,00207$ | **$0,00414$** |
| `B2` | `CM` | `CoverUp vs CodaMOSA` | 17 | **-$0,002543** | 34,0 | $0,04477$ | **$0,04477$** |
| `B2` | `MT` | `CoverUp vs CodaMOSA` | 162 | **-$0,000926** | 410,0 | $4,01 \times 10^{-25}$ | **$2,41 \times 10^{-24}$** |

