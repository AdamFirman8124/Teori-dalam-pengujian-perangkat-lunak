# Pedoman Eksperimen dan Reproduksi

**Studi Komparatif Generator Unit Test Python (Pynguin, CodaMOSA, CoverUp, MuTAP)**  
*Versi 1.2 · 21 Oktober 2026*  
*Mengikuti Methodology v3 dan Keputusan 16, 19, dan 21 Oktober 2026 (`CLAUDE.md`)*

---

> ### 🎯 TUJUAN PEDOMAN
> Menghasilkan dua file data utama, yaitu `results.csv` dan `module_characteristics.csv`, yang lengkap dan benar untuk menjawab **RQ1–RQ3**, dengan waktu dan biaya seminimal mungkin tanpa perlu mengulang eksperimen.
>
> ### ⚠️ TANDA KHUSUS DOKUMEN
> * `[PERLU DICEK]`: Fakta atau perintah yang belum dipastikan dari sumber resmi; wajib diuji di Fase 2 atau Fase 6 sebelum diandalkan.
> * `⛔ GERBANG`: Syarat mutlak yang wajib terpenuhi sebelum diizinkan lanjut ke fase berikutnya.

---

> ### 📝 CATATAN REVISI
>
> **Revisi 19 Oktober 2026 (RQ3 $\rightarrow$ Cost-Effectiveness):**
> 1. Karakteristik modul `cc_mean`, `n_ext_deps`, dan `annot_density` **tidak lagi dihitung**. Fase 4 cukup menghitung `loc`, `sloc`, `n_branches`, dan `project` untuk sampling.
> 2. Keputusan baru **0.9**: Tanggal dan sumber daftar harga resmi berbayar untuk menghitung `cost_usd` (meskipun run menggunakan *free tier*).
> 3. Metrik `tokens_in`, `tokens_out`, `cost_usd`, `gen_time_s`, dan `hit_budget` menjadi **data utama RQ3**.
> 4. *Dry run* Fase 5 wajib menghasilkan TABEL VIII (biaya & *cost-effectiveness*), TABEL IX (uji biaya), dan Gambar 5 (*Pareto plot*).
> 5. Penambahan dua larangan baru (nomor 12 dan 13) di Bagian 14.
>
> **Revisi 21 Oktober 2026 (Aturan Waktu):**
> * Keputusan baru **0.10** menetapkan kapan jam $600\text{ s}$ mulai dan berhenti, perlakuan waktu tunggu *rate limit*, serta jumlah run paralel $P$.

---

## 0. RINGKASAN ALUR

| Fase | Nama | RQ yang Dilayani | Memakai API LLM? | Keluaran Utama |
| :---: | :--- | :---: | :---: | :--- |
| **0** | Keputusan yang tersisa | Semua | Tidak | `docs/protocol.md` terisi sebagian |
| **1** | Lingkungan dan versi tool | Semua | Tidak | Image Docker per tool, `docs/sources.md` |
| **2** | Pengecekan teknis | Semua | Sedikit ($\le 10$ panggilan) | Laporan cek A–E |
| **3** | `llm_proxy` dan logging | RQ1 (*raw validity*), RQ2, RQ3 (token) | Sedikit | Log JSONL per panggilan |
| **4** | Benchmark, ukuran modul, sampling CM | Semua | Tidak | `module_characteristics.csv`, `cm_sample.csv` |
| **5** | *Dry run* analisis | Semua | Tidak | Tabel IV–IX terisi dari data simulasi |
| **6** | Pilot dan estimasi biaya | Semua | Ya (kecil) | `pilot_report.md`, estimasi biaya dan waktu |
| **7** | Pembekuan protokol | Semua | Tidak | Commit bertag `protocol-frozen` |
| **8** | Eksekusi utama | Semua | Ya (besar) | Folder hasil per run |
| **9** | Evaluasi S3–S4 | Semua | Tidak | `results.csv` |
| **10** | Pemeriksaan kewajaran data | Semua | Tidak | `sanity_report.md` |
| **11** | Pengarsipan untuk reproduksi | — | Tidak | Paket replikasi |

*Prinsip Urutan:* Semua langkah gratis/murah dikerjakan lebih dahulu (Fase 0–5). Pilot kecil dilakukan pada Fase 6, lalu protokol dibekukan (Fase 7) sebelum eksekusi utama berbiaya tinggi dilakukan pada Fase 8.

---

## 1. FAKTA TOOL YANG SUDAH DIVERIFIKASI (16 OKTOBER 2026)

| Tool | Sumber yang Dipakai | Versi / Commit | Python | Catatan Penting |
| :--- | :--- | :---: | :---: | :--- |
| **Pynguin** | PyPI `pynguin` | `0.47.0` | 3.10 | Wajib `PYNGUIN_DANGER_AWARE`. Opsi: `--project-path`, `--module-name`, `--output-path`, `--algorithm DYNAMOSA`, `--maximum-search-time`, `--seed`, `--assertion-generation`, `--coverage-metrics BRANCH LINE`, `--output-variables`. Build Dockerfile sendiri dari repo. |
| **CodaMOSA** | Fork `plasma-umass/codamosa` `@17a4c2a2` | Berbasis Pynguin `0.19.0` | 3.10.2 | Menggunakan Chat API dan menyimpan prompt/completion (`llm_prompts.txt`, `llm_completions.txt`). Konfigurasi resmi menggunakan `--assertion-generation NONE`. |
| **CoverUp** | PyPI `coverup` | `0.6.3` | $\ge 3.10$ | Menggunakan `litellm`. Wajib *function calling* (`get_info`) pada prompt default `gpt-v2`. Tidak ada batas waktu total internal. Mengukur coverage dengan SlipCover. |
| **MuTAP** | Fork `plasma-umass/MuTAP` `@888ab58a` | — | 3.9 | Fork menggunakan Chat API, kunci dari `OPENAI_API_KEY`. Hanya menyimpan respons (`gpt_completions.jsonl`), tidak menyimpan prompt. |
| **coverage.py**| PyPI `coverage` | `7.16.2` | $\ge 3.10$ | `coverage run --branch -m pytest ...` lalu `coverage json`. $\text{LC} = \frac{\text{covered\_lines}}{\text{num\_statements}}$, $\text{BC} = \frac{\text{covered\_branches}}{\text{num\_branches}}$. |
| **Cosmic Ray**| PyPI `cosmic-ray` | `8.7.0` | $\ge 3.9$ | `new-config` $\rightarrow$ `init` $\rightarrow$ `baseline` $\rightarrow$ `exec` $\rightarrow$ `cr-report`. Mutan *timeout* ditandai `"incompetent"`. |
| **mutmut** | PyPI `mutmut` | `3.8.0` | $\ge 3.10$ | Butuh fork (jalan di Linux/WSL). Konfigurasi `[tool.mutmut]` dengan `source_paths`. |
| **radon** | PyPI `radon` | — | — | `radon raw -j` (`LOC`, `SLOC`). |

### Benchmark
* **MT Suite:** `coverup-eval/MuTAP-benchmarks/f001` … `f163` (163 folder).
* **CM Suite:** `codamosa/replication/test-apps/cm_modules.csv` (425 modul dari 24 proyek; 237 modul dari `ansible`, 35 `youtube-dl`, 19 `py-backwards`, 19 `httpie`, sisa $\le 13$ per proyek).
* *Konsekuensi Paper:* Tulis **"425 modules from 24 projects"** (bukan 35 proyek).

---

## FASE 0. KEPUTUSAN YANG TERSISA

| No | Keputusan | Pilihan | Batas Final |
| :---: | :--- | :--- | :--- |
| **0.1** | Backbone B1 (Proprietary) | Snapshot bertanggal dari penyedia | Sebelum Fase 2 |
| **0.2** | Backbone B2 (Open-weight) | Model yang lolos Cek C (*function calling*) di Fase 2 | Setelah Fase 2 |
| **0.3** | Mutation Tool | Cosmic Ray atau mutmut | Sebelum Fase 5 |
| **0.4** | $k$ (Pengulangan deteksi *flaky*) | $k = 5$ (default `--repeat-tests` CoverUp) | Sebelum Fase 5 |
| **0.5** | Temperatur CodaMOSA | `0.8` (konfigurasi asli `0.8-uninterp`) | Sebelum Fase 6 |
| **0.6** | Perlakuan Mutan *Timeout* | Dihitung terbunuh dan dilaporkan terpisah | Sebelum Fase 5 |
| **0.7** | Batas Modul per Proyek (CM Sample) | Maksimal 25% sampel dari satu proyek | Sebelum Fase 4 |
| **0.8** | Anggaran Biaya & Waktu Maksimum | Biaya ($\text{USD}$) dan Waktu (Hari) ditentukan peneliti | Sebelum Fase 6 |
| **0.9** | Daftar Harga `cost_usd` | Harga berbayar per 1 juta token (input & output) dari situs resmi | Sebelum Fase 5 |
| **0.10**| Aturan Waktu per Run | Mengikuti aturan W1–W8 di bawah | Sebelum Fase 6 |

### Aturan Waktu per Run (Keputusan 0.10)
> Satu run = $1\text{ tool} \times 1\text{ backbone} \times 1\text{ unit} \times 1\text{ pengulangan}$.

* **W1 (Anggaran):** $600\text{ s}$ *wall-clock time* untuk pembangkitan tes pada keempat tool.
* **W2 (Jam Mulai):** Diukur saat proses tool berjalan pada unit tersebut. (Setup container & dependensi tidak dihitung).
* **W3 (Jam Berhenti):** Tool selesai sendiri ($\text{hit\_budget} = 0$), atau mencapai $600\text{ s}$ ($\text{SIGINT}$, masa tenggang $30\text{ s} \rightarrow \text{SIGKILL}$, $\text{hit\_budget} = 1$). Tes yang tersimpan tetap dievaluasi.
* **W4 (Pynguin & CodaMOSA):** `--maximum-search-time 600`. Jika tahap pembuatan *assertion* terpotong pada pilot, turunkan waktu pencarian internal (misal $540\text{ s}$) agar total tetap $600\text{ s}$.
* **W5 (Waktu Tunggu Rate Limit):** Ikut dihitung dalam $600\text{ s}$. Jika $\text{ratelimit\_wait\_s} > 60\text{ s}$ ($10\%$ anggaran), tandai $\text{wait\_flag} = 1$ dan ulang $1\times$.
* **W6 (Evaluasi):** Evaluasi tes/coverage/mutasi tidak mengurangi jatah $600\text{ s}$ (menggunakan *timeout* tersendiri).
* **W7 (Waktu RQ3):** $\text{gen\_time\_s} = \text{wall-clock time} - \text{ratelimit\_wait\_s}$.
* **W8 (Paralelisme):** Jumlah run paralel $P$ bernilai tetap dan $\le \text{jumlah inti CPU fisik}$. Setiap container dibatasi CPU dan RAM yang sama (`--cpus`, `--memory`).

> `⛔ GERBANG 0`: Poin 0.1, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9, dan 0.10 wajib terisi penuh di `docs/protocol.md`.

---

## FASE 1. LINGKUNGAN DAN VERSI TOOL

1. Clone repository dengan commit terkunci:
   ```bash
   git clone --recurse-submodules https://github.com/plasma-umass/coverup-eval third_party/coverup-eval
   cd third_party/coverup-eval && git checkout f3173196 && git submodule update --init --recursive
   ```
2. Build Docker Image per Tool:
   * `img-pynguin`: `python:3.10` + `pynguin==0.47.0`
   * `img-codamosa`: `python:3.10.2` + fork `plasma-umass/codamosa`
   * `img-coverup`: `python:3.10` + `coverup==0.6.3`
   * `img-mutap`: `python:3.9` + fork `plasma-umass/MuTAP`
   * `img-eval`: `python:3.10` + `pytest`, `coverage==7.16.2`, `cosmic-ray`/`mutmut`, `radon`
3. Catat digest image (`docker images --digests`) ke `docs/sources.md`.

> `⛔ GERBANG 1`: Setiap image dapat menjalankan perintah `--help` tanpa error, dan semua versi tercatat di `docs/sources.md`.

---

## FASE 2. PENGECEKAN TEKNIS

| Cek | Pertanyaan Teknis | Cara Menguji | Penanganan Jika Gagal |
| :---: | :--- | :--- | :--- |
| **A** | Bisakah CodaMOSA membuat *assertion*? | Dijalankan dengan `--algorithm CODAMOSA --uninterpreted_statements ONLY --assertion-generation MUTATION_ANALYSIS`. | Coba `SIMPLE`. Jika gagal, laporkan MS dengan catatan atau keluarkan dari perbandingan MS. |
| **B** | Apakah tes CoverUp aman saat dihentikan di $600\text{ s}$? | Jalankan `timeout -s INT 600 coverup ...`. Periksa `test_coverup_*.py`. | CoverUp menulis tes secara langsung saat diterima. Jika checkpoint gagal, andalkan file tes yang ada. |
| **C** | Apakah backbone B2 mendukung *function calling*? | Jalankan CoverUp dengan B2 pada `f001`. | Ganti B2 ke model open-weight lain yang mendukung *function calling*. Jangan ganti ke `--prompt-family gpt-v2-no-code-context`. |
| **D** | Bisakah semua tool diarahkan ke endpoint custom? | CodaMOSA (`--model-base-url`), CoverUp (`litellm`), MuTAP (`OPENAI_BASE_URL`). | Arahkan via `llm_proxy` (Fase 3) yang meniru endpoint OpenAI API. |
| **E** | Apakah pipeline evaluasi berjalan mulus? | Jalankan pipeline Fase 9 pada output cek A–C (`pytest`, `coverage`, `mutation tool`). | Perbaiki skrip evaluasi. Pastikan mutan $> 0$ dan coverage terbaca. |

> `⛔ GERBANG 2`: Kelima cek (A–E) lolos atau solusi penggantinya tercatat di protokol. Model B2 final telah ditetapkan.

---

## FASE 3. LLM_PROXY DAN LOGGING

1. Skema Proxy: Menerima endpoint `/v1/chat/completions`, meneruskan ke penyedia B1/B2, lalu mencatat log JSONL.
2. Structure Log (`results/raw/<run_id>/llm_log.jsonl`):
   * `run_id`, `timestamp`, `backbone`, `model_requested`, `model_returned`, `request`, `response`, `tokens_in`, `tokens_out`, `latency_s`, `http_status`, `ratelimit_wait_s`.
3. `tokens_in` & `tokens_out` diambil langsung dari field `usage` pada respons API. Jika bernilai null (*streaming*), catat `NA`.
4. Nilai `cost_usd` dihitung pada tahap analisis: $\text{tokens} \times \text{harga (Keputusan 0.9)}$.

> `⛔ GERBANG 3`: Pada 1 run uji per tool:
> 1. Jumlah log cocok dengan laporan panggilan internal tool.
> 2. Isi respons selaras dengan `llm_completions.txt` atau `gpt_completions.jsonl`.
> 3. `tokens_in` dan `tokens_out` terisi penuh.

---

## FASE 4. BENCHMARK, UKURAN MODUL, DAN SAMPLING CM

1. **MT Suite:** Gunakan seluruh 163 fungsi dari `MuTAP-benchmarks`.
2. **Karakteristik Modul CM (`module_characteristics.csv`):**
   * Hitung `loc` dan `sloc` (`radon raw -j`).
   * Hitung `n_branches` (Jumlah titik percabangan AST: `if`, `elif`, `for`, `while`, `try/except`, `match`, ekspresi kondisional).
3. **Pilot Modul:** Pilih 3 modul CM kecil dari proyek berbeda ($\text{is\_pilot} = 1$).
4. **Sampling CM (`cm_sample.csv`):**
   * Buat $3 \times 3$ strata: Tertil LOC $\times$ Tertil `n_branches` (9 strata).
   * Ambil sampel acak bertingkat hingga $\ge 40$ modul (gunakan *seed* tetap dan batas per proyek dari Keputusan 0.7).

> `⛔ GERBANG 4`: Tidak ada nilai kosong, modul pilot terpisah dari sampel, pembatasan per proyek dipatuhi, dan seluruh strata terisi.

---

## FASE 5. DRY RUN ANALISIS DENGAN DATA SIMULASI

1. Buat `results_sim.csv` menggunakan data acak rasional ($\text{MT}: 163 \times 7 \times 10$; $\text{CM}: 40 \times 5 \times 10$).
2. Jalankan skrip analisis untuk menghasilkan TABEL IV–IX dan Gambar 3–5:
   * **TABEL VIII:** Token, Biaya, Waktu, `hit_budget`, $\Delta E$, dan $CE$.
   * **TABEL IX:** Uji statistik biaya (13 uji Wilcoxon dengan koreksi Holm).
   * **Gambar 5:** *Pareto plot* (skala log pada sumbu-x biaya, Pynguin sebagai acuan).
3. Uji *edge cases*: Unit dengan $\text{n\_mutants} = 0$ ($\text{MS} = \text{NA}$), run gagal, Pynguin ($\text{RV} = \text{NA}$), $\Delta E \le 0$ ($CE = \text{"dominated"}$), dan `tokens_in` = `NA`.

> `⛔ GERBANG 5`: Seluruh tabel dan grafik tergenerate otomatis tanpa error.

---

## FASE 6. PILOT DAN ESTIMASI BIAYA

1. **Unit Pilot:** 5 fungsi MT + 3 modul CM pilot. Run seluruh konfigurasi dengan $R = 2$, budget $600\text{ s}$.
2. Evaluasi aturan waktu 0.10: Periksa apakah ada pemotongan *assertion* Pynguin/CodaMOSA, cek run dengan $\text{ratelimit\_wait\_s} > 60\text{ s}$, dan validasi nilai $P$.
3. Hitung Rata-rata Waktu ($\bar{t}_c$) dan Biaya ($\bar{b}_c$) per Run:
   $$\text{Estimasi Total Biaya} \approx \sum_c (N_{\text{unit},c} \times R \times \bar{b}_c) \times 1.2$$
   $$\text{Estimasi Total Waktu (jam)} \approx \frac{\sum_c (N_{\text{unit},c} \times R \times \bar{t}_c)}{3600 \times P}$$

### Matrix Rancangan Run Utama
| Blok | Konfigurasi | Unit | $R$ | Total Run | Memakai API? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **MT, Pynguin** | 1 | 163 | 10 | 1.630 | Tidak |
| **MT, Tool LLM** | 6 | 163 | 10 | 9.780 | Ya |
| **CM, Pynguin** | 1 | 40 | 10 | 400 | Tidak |
| **CM, Tool LLM** | 4 | 40 | 10 | 1.600 | Ya |
| **TOTAL** | | | | **13.410** | **11.380 (API)** |

> `⛔ GERBANG 6`: Estimasi biaya $\le \text{Anggaran (0.8)}$, estimasi waktu $\le \text{Batas Waktu}$, dan seluruh kolom `results.csv` terisi valid di `docs/pilot_report.md`.

---

## FASE 7. PEMBEKUAN PROTOKOL

1. Lengkapi seluruh parameter di `docs/protocol.md` dan `config/experiment.yaml`.
2. Commit dan berikan tag Git:
   ```bash
   git tag protocol-frozen
   ```

> `⛔ GERBANG 7`: Tag `protocol-frozen` terpasang, tanpa ada variabel placeholder (`[ISI]` atau `null`) tersisa.

---

## FASE 8. EKSEKUSI UTAMA

1. Generate `run_matrix.csv` (Urutan blok: Pynguin MT $\rightarrow$ Pynguin CM $\rightarrow$ LLM MT $\rightarrow$ LLM CM).
2. Acak urutan run di dalam blok LLM menggunakan *seed* tetap untuk menghindari bias temporer dari penyedia API.
3. Jalankan tiap run di container baru dengan batas waktu:
   ```bash
   timeout -s INT -k 30 600 ...
   ```
4. Run dengan `wait_flag = 1` diulang satu kali di akhir blok; percobaan kedua yang dianalisis.

> `⛔ GERBANG 8` *(Pemeriksaan Harian)*: Hentikan eksekusi jika:
> * Tingkat kegagalan konfigurasi $> 10\%$.
> * `model_returned` berubah dari penyedia.
> * Biaya membengkak $> 20\%$ dari proyeksi.
> * Lebih dari $10\%$ run terkena `wait_flag = 1`.

---

## FASE 9. EVALUASI S3–S4 (PENGISIAN `results.csv`)

Jalankan evaluasi pada container `img-eval` terhadap kode asli:
1. **Suite Akhir:** Jalankan tes dengan `pytest` $\rightarrow$ `n_tests_final`, `n_pass_first`, `n_fail`, `n_error`, `n_timeout`.
2. **Flaky:** Ulangi tes yang lulus sebanyak $k$ kali $\rightarrow$ `n_flaky`, `n_valid`.
3. **Coverage:** Ukur `coverage.py` $\rightarrow$ `lines_total`, `lines_exec`, `branches_total`, `branches_exec`.
4. **Mutasi:** Eksekusi tes valid pada mutan bersama $\rightarrow$ `n_mutants`, `n_killed`, `n_survived`, `n_mutant_timeout`.
5. **Raw Validity (LLM):** Ekstrak tes mentah dari log proxy $\rightarrow$ `n_raw_proposals`, `n_raw_pass`.
6. **Kemiripan:** Hitung kemiripan *normalized Levenshtein* maksimum $\rightarrow$ `sim_max_median`.

> `⛔ GERBANG 9`: Baris pada `results.csv` sama persis dengan jumlah baris pada `run_matrix.csv`.

---

## FASE 10. PEMERIKSAAN KEWAJARAN DATA

| No | Pemeriksaan | Hasil yang Diharapkan | Tindakan Jika Menyimpang |
| :---: | :--- | :--- | :--- |
| **1** | Jumlah run per konfigurasi | 10 per unit | Jalankan ulang run yang hilang. |
| **2** | `n_mutants` | $> 0$ untuk seluruh unit | Perbaiki skrip mutasi. |
| **3** | Mutation Score (MS) | Variasi wajar ($0 < \text{MS} < 100$) | Cek path file tes dan mutan. |
| **4** | Raw Validity | $< 100\%$ dan bervariasi | Jika $100\%$, kemungkinan yang teruji adalah suite akhir. |
| **5** | Pass rate suite akhir | Mendekati $100\%$ | Cek isolasi lingkungan uji. |
| **6** | Coverage MT | Mendekati $100\%$ (efek plafon) | Perbaiki path modul coverage. |
| **7** | `hit_budget` | Terlaporkan per tool | Bahas di bab *Threats to Validity*. |
| **8** | `model_returned` | Konsisten per backbone | Tandai dan laporkan run yang berbeda. |
| **9** | Run Gagal | $\le 10\%$ per konfigurasi | Kelompokkan berdasarkan `error_category`. |
| **10**| Match ID Unit | `results.csv` $\leftrightarrow$ `module_characteristics.csv` | Perbaiki penamaan ID modul CM. |
| **11**| Metrik Biaya | `tokens_in`, `tokens_out`, `cost_usd` $> 0$ (Tool LLM) | Cek log proxy & `docs/prices.md`. |

> `⛔ GERBANG 10`: Seluruh poin lolos uji kewajaran di `docs/sanity_report.md` sebelum analisis statistik RQ1–RQ3 dijalankan.

---

## FASE 11. PENGARSIPAN UNTUK REPRODUKSI

Arsipkan dan unggah aset ke repositori publik (misal Zenodo):
* Data utama: `results.csv`, `module_characteristics.csv`, `cm_sample.csv`, `run_matrix.csv`.
* Mentah: Folder `results/raw/<run_id>/` terkompresi.
* Dokumentasi: Seluruh file di folder `docs/`.
* Code & Environment: Dockerfile, digest image, serta notebook/skrip analisis.

---

## 12. SKEMA RESULTS.CSV

| Kolom | Tipe | Definisi | Ditulis di Fase |
| :--- | :---: | :--- | :---: |
| `run_id` | Teks | ID Unik Run | 8 |
| `suite` | MT/CM | Benchmark | 8 |
| `unit_id` | Teks | ID Fungsi (`f001`) atau Modul (`proyek:modul`) | 8 |
| `project` | Teks | Nama Proyek (CM) | 4 |
| `tool` | Teks | Generator Test (Pynguin/CodaMOSA/CoverUp/MuTAP) | 8 |
| `tool_version` | Teks | Versi / Commit Hash Tool | 1 |
| `backbone` | B1/B2/– | Model Backbone | 8 |
| `model_requested`, `model_returned` | Teks | ID Model yang diminta & dikembalikan API | 3 |
| `run_idx`, `seed` | Angka | Pengulangan (1–10) dan Random Seed | 8 |
| `start_time`, `end_time` | Waktu | Timestamp Eksekusi | 8 |
| `budget_s` | Angka | Anggaran Waktu ($600\text{ s}$) | 8 |
| `gen_time_s` | Angka | Waktu Pembangkitan murni ($\text{Wall-clock} - \text{Wait}$) | 8 |
| `ratelimit_wait_s` | Angka | Total Waktu Tunggu Rate Limit | 3 |
| `hit_budget` | 0/1 | $1$ jika terhenti oleh batas waktu ($600\text{ s}$) | 8 |
| `wait_flag`, `attempt` | 0/1, Angka | Flag waktu tunggu $> 60\text{ s}$ & Nomor Percobaan | 8 |
| `status`, `error_category` | Teks | `ok`/`failed`; `crash`/`syntax`/`env`/`timeout` | 8–9 |
| `n_api_calls`, `tokens_in`, `tokens_out` | Angka | Statistik Token dari Usage Proxy | 3 |
| `cost_usd` | Angka | Biaya ($\text{tokens\_in} \times \text{harga\_in} + \text{tokens\_out} \times \text{harga\_out}$) | 9 |
| `n_raw_proposals`, `n_raw_pass` | Angka | Jumlah usulan tes mentah LLM & yang lulus | 9 |
| `n_tests_final`, `n_pass_first`, `n_fail`, `n_error`, `n_timeout` | Angka | Hasil Eksekusi Suite Akhir | 9 |
| `k_reruns`, `n_flaky`, `n_valid` | Angka | Deteksi Tes Flaky | 9 |
| `lines_total`, `lines_exec`, `branches_total`, `branches_exec` | Angka | Statistik Line & Branch Coverage | 9 |
| `mutation_tool`, `n_mutants`, `n_killed`, `n_survived`, `n_mutant_timeout` | Teks/Angka | Hasil Evaluasi Mutasi | 9 |
| `sim_max_median` | Angka | Median Kemiripan Maksimum Levenshtein | 9 |

**Metrik Turunan (Analisis):**
* $\text{RV} = \frac{\text{n\_raw\_pass}}{\text{n\_raw\_proposals}}$
* $\text{LC} = \frac{\text{lines\_exec}}{\text{lines\_total}}$
* $\text{BC} = \frac{\text{branches\_exec}}{\text{branches\_total}}$
* $\text{MS} = \frac{\text{n\_killed}}{\text{n\_mutants}}$
* $\Delta E = \text{Median Efektivitas Tool} - \text{Median Pynguin}$
* $CE = \frac{\Delta E}{\text{Median cost\_usd}}$ (Jika $\Delta E \le 0 \rightarrow CE = \text{"dominated"}$).

---

## 13. SKEMA MODULE_CHARACTERISTICS.CSV

| Kolom | Definisi | Tool / Cara Ukur |
| :--- | :--- | :--- |
| `unit_id`, `project` | Nama modul dan proyek CM | `cm_modules.csv` |
| `loc`, `sloc` | Line of Code total & Source Line of Code | `radon raw -j` |
| `n_branches` | Jumlah titik percabangan AST | Skrip AST Custom |
| `stratum` | Matriks $3 \times 3$ (LOC $\times$ `n_branches`) | Skrip Sampling |
| `is_pilot`, `in_sample` | Flag Modul Pilot ($1/0$) dan Modul Sampel ($1/0$) | Skrip Sampling |

---

## 14. DAFTAR "JANGAN PERNAH" (ATURAN FATAL)

1. ❌ Menjalankan run utama tanpa `llm_proxy` aktif.
2. ❌ Menghitung *raw validity* dari suite akhir.
3. ❌ Menulis $\text{MS} = 0$ jika $\text{n\_mutants} = 0$ (Harus $\text{NA}$).
4. ❌ Membuat set mutan yang berbeda antar-tool atau antar-run.
5. ❌ Menggunakan coverage bawaan tool (Wajib gunakan `coverage.py` untuk semua).
6. ❌ Membiarkan CoverUp berjalan melebihi $600\text{ s}$.
7. ❌ Mengubah versi model, tool, atau image Docker di tengah jalan.
8. ❌ Memasukkan modul pilot ke sampel CM atau menggunakan data pilot di paper.
9. ❌ Mengubah metode analisis statistik setelah melihat hasil data.
10. ❌ Memotong jumlah backbone menjadi 1 demi menghemat biaya.
11. ❌ Menyimpan API key di repositori, file log, atau screenshot.
12. ❌ Menghitung biaya dari tagihan *free tier* ($0\text{ USD}$) atau beda tanggal daftar harga.
13. ❌ Membandingkan jumlah total token antar-backbone yang berbeda *tokenizer*.
14. ❌ Memasukkan waktu setup container/evaluasi ke dalam jatah $600\text{ s}$.
15. ❌ Mengubah nilai $P$ (paralelisme) di tengah eksekusi blok.

---

## 15. PENANGANAN MASALAH

| Masalah | Tanda-Tanda | Tindakan Koreksi |
| :--- | :--- | :--- |
| **Rate Limit** | HTTP 429, `ratelimit_wait_s` tinggi | Kurangi paralelisme $P$. Pisahkan waktu tunggu dari `gen_time_s`. |
| **Saldo Habis** | HTTP 401 / 402 / 403 | Isi ulang saldo API, lalu lanjutkan via `run_matrix.csv`. |
| **Model Berubah** | `model_returned` berbeda | Hentikan run. Tandai data dan putuskan pengulangan di protokol. |
| **Run Crash** | `status = failed` | Simpan log error. Ulangi $1\times$ dengan seed sama. |
| **Container Macet** | Eksekusi $> 600\text{ s} + 30\text{ s}$ | Jalankan `docker kill`. Catat `error_category = env`. |
| **Disk Penuh** | Error penulisan file | Kompres folder `results/raw/` yang sudah dievaluasi. |
| **Pencemaran Lingkungan** | Hasil berubah antar-urutan | Pastikan setiap run menggunakan container Docker baru. |

---

## 16. DAFTAR PERIKSA (CHECKLIST)

### Sebelum Mengeluarkan Biaya API
* [ ] **Fase 0:** Poin 0.1–0.10 lengkap; file `docs/prices.md` memuat bukti halaman harga resmi.
* [ ] **Fase 1:** 5 Image Docker siap dan digest tercatat di `docs/sources.md`.
* [ ] **Fase 2:** Cek A, B, C, D, dan E lolos pengujian.
* [ ] **Fase 3:** `llm_proxy` mencatat $100\%$ panggilan API secara presisi.
* [ ] **Fase 4:** `module_characteristics.csv` terisi (425 baris); sampel CM $\ge 40$ modul.
* [ ] **Fase 5:** *Dry run* berhasil menghasilkan TABEL IV–IX dan Gambar 3–5.

### Pilot dan Pembekuan
* [ ] **Fase 6:** Pilot selesai; estimasi biaya & waktu berada di bawah ambang batas.
* [ ] **Fase 7:** Document `docs/protocol.md` terisi lengkap; tag `protocol-frozen` terpasang.

### Eksekusi dan Evaluasi
* [ ] **Fase 8:** Eksekusi berjalan sesuai urutan blok; pemantauan harian aktif.
* [ ] **Fase 9:** `results.csv` terisi penuh dengan jumlah baris yang sesuai.
* [ ] **Fase 10:** Uji kewajaran data 100% lolos di `docs/sanity_report.md`.
* [ ] **Fase 11:** Paket replikasi lengkap diarsipkan ke Zenodo.

---

## 17. PROMPT SIAP PAKAI UNTUK CLAUDE DI VS CODE

### Fase 1
```text
Baca CLAUDE.md dan docs/pedoman_eksperimen.md (Fase 1). Buat lima Dockerfile (img-pynguin, img-codamosa, img-coverup, img-mutap, img-eval) dengan versi persis seperti Bagian 1. Clone coverup-eval beserta submodule pada commit yang tercatat. Isi docs/sources.md dengan versi, commit, dan digest image. Jangan menjalankan panggilan API. Tunjukkan perintah build, lalu berhenti dan tunggu konfirmasi saya.
```

### Fase 2
```text
Kerjakan Fase 2 docs/pedoman_eksperimen.md: cek A–E pada fungsi MT f001 dan satu modul CM kecil yang tidak akan masuk sampel. Batasi panggilan API maksimal 10 per cek. Catat perintah persis, keluaran, dan keputusan di docs/technical_checks.md. Kalau ada cek yang gagal, jangan mengubah algoritma tool; laporkan pilihan yang tersedia dan tunggu keputusan saya.
```

### Fase 3
```text
Kerjakan Fase 3: implementasikan llm_proxy yang meniru endpoint OpenAI /v1/chat/completions, meneruskan ke penyedia B1/B2 dari .env, dan menulis satu baris JSONL per panggilan dengan field di pedoman (tanpa API key). Uji dengan satu run per tool dan bandingkan jumlah panggilan dengan laporan tool. Berhenti dan laporkan hasilnya.
```

### Fase 4
```text
Kerjakan Fase 4: hitung module_characteristics.csv (hanya loc, sloc, n_branches, project) untuk semua 425 modul di cm_modules.csv sesuai definisi Bagian 13; pilih 3 modul pilot; ambil sampel CM bertingkat (tertil LOC × tertil n_branches) minimal 40 modul dengan seed dan batas per proyek dari docs/protocol.md. Tampilkan distribusi per proyek, per stratum, serta ringkasan LOC dan n_branches. Berhenti dan tunggu konfirmasi saya.
```

### Fase 5
```text
Kerjakan Fase 5: buat results_sim.csv dengan skema persis Bagian 12 berisi data simulasi, lalu jalankan skrip analisis RQ1–RQ3 sampai TABLE IV–IX dan Gambar 3–5 terisi; untuk RQ3 hitung cost_usd dari docs/prices.md, ΔE, CE, 13 uji Wilcoxon biaya dengan Holm, dan Pareto plot. Uji kasus n_mutants = 0, run gagal, rv NA untuk Pynguin, ΔE ≤ 0, dan token NA. Laporkan tabel yang gagal terisi dan kolom yang kurang.
```

### Fase 6
```text
Kerjakan Fase 6: jalankan pilot (5 fungsi MT + 3 modul CM pilot, semua konfigurasi, R = 2, budget 600 s), lalu Fase 9–10 pada hasilnya. Hitung t̄ dan b̄ per konfigurasi serta estimasi total dengan rumus di pedoman. Tulis docs/pilot_report.md. Berhenti dan tunggu keputusan saya sebelum membekukan protokol.
```

### Fase 8
```text
Protokol sudah dibekukan (tag protocol-frozen). Kerjakan Fase 8: buat run_matrix.csv, jalankan blok sesuai urutan di pedoman dengan urutan acak di dalam blok LLM, hentikan setiap run pada 600 s dengan SIGINT, dan pastikan eksekusi bisa dilanjutkan. Laporkan kemajuan, tingkat kegagalan, biaya kumulatif, dan model_returned setiap selesai satu blok.
```

### Fase 9–10
```text
Kerjakan Fase 9 dan 10 untuk semua run berstatus done: isi results.csv sesuai skema Bagian 12, lalu jalankan pemeriksaan kewajaran dan tulis docs/sanity_report.md. Jangan menjalankan analisis statistik sebelum saya menyetujui laporan kewajaran.
```

---

## SUMBER REFERENSI TEKNIS

* **Pynguin:** [PyPI](https://pypi.org/project/pynguin/) · [GitHub](https://github.com/se2p/pynguin) · [Docs](https://pynguin.readthedocs.io)
* **CodaMOSA:** [GitHub Original](https://github.com/microsoft/codamosa) · [Fork CoverUp-Eval](https://github.com/plasma-umass/coverup-eval)
* **CoverUp:** [PyPI](https://pypi.org/project/coverup/) · [GitHub Tool](https://github.com/plasma-umass/coverup) · [GitHub Eval](https://github.com/plasma-umass/coverup-eval)
* **MuTAP:** [GitHub Original](https://github.com/ExpertiseModel/MuTAP) · [Fork CoverUp-Eval](https://github.com/plasma-umass/coverup-eval)
* **Coverage & Mutation:** [coverage.py](https://coverage.readthedocs.io) · [Cosmic Ray](https://cosmic-ray.readthedocs.io) · [mutmut](https://github.com/boxed/mutmut) · [radon](https://radon.readthedocs.io)
* **LiteLLM Provider Naming:** [LiteLLM Docs](https://docs.litellm.ai/docs/providers)