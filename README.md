# Perbandingan CoverUp vs CodaMOSA sebagai Generator Test Otomatis

Repositori ini menjalankan dua metode pembuat test otomatis — **CoverUp** dan
**CodaMOSA** — pada dua dataset (**HumanEval** dan **Refactory** dari paket
MuTAP), lalu mengukur hasilnya untuk menjawab dua pertanyaan riset:

- **RQ1 (Performa utama):** Coverage, Pass Rate, Mutation Score
- **RQ2 (Backbone):** Coverage, Pass Rate, Waktu, dan Biaya

> Panduan teknis tambahan ada di [`docs/README.md`](docs/README.md),
> [`docs/EXPERIMENT_PROTOCOL.md`](docs/EXPERIMENT_PROTOCOL.md), dan
> [`docs/CODAMOSA_KNOWN_LIMITATIONS.md`](docs/CODAMOSA_KNOWN_LIMITATIONS.md).

---

## Bagian 1 — Panduan Cepat (untuk pengguna awam)

### Ini programnya untuk apa?

Ibaratnya: kita punya "program kecil" (fungsi Python), lalu meminta **dua asisten
AI yang berbeda** membuat soal ujian (test) untuk program itu. Setelah soal
jadi, kita koreksi:

- Seberapa banyak baris kode yang sempat diperiksa soalnya? (**coverage**)
- Apakah jawaban yang diperiksa benar semua? (**pass rate**)
- Kalau programnya diubah sedikit (dibuat "mutan" yang salah), apakah soalnya
  bisa mendeteksi kebohongannya? (**mutation score** — semakin tinggi, semakin
  tajam soalnya)
- Berapa lama dan berapa biaya token untuk membuat soal itu? (**waktu & biaya**)

### Yang Anda butuhkan

| Kebutuhan | Keterangan |
|---|---|
| Python 3.14 di folder `.venv` | Sudah tersedia di repo ini |
| Docker | Hanya untuk metode CodaMOSA (CoverUp tidak perlu) |
| API key OctaLabs | Diletakkan di `config/.env` |
| Koneksi internet | Model dipanggil lewat API, bukan dijalankan di PC |

### Langkah menjalankan

1. **Isi kunci API.** Salin `config/.env.example` menjadi `config/.env`, lalu
   isi `OCTA_API_KEY=` dengan kunci Anda. Jangan pernah membagikan file ini.

2. **Daftarkan kernel notebook** (sekali saja):
   ```bash
   .venv/bin/python -m ipykernel install --user --name teori-pengujian \
     --display-name 'Python (.venv Teori Pengujian)'
   ```

3. **Buka** `experiments_codamosa_coverup.ipynb` di VS Code, pilih kernel
   **Python (.venv Teori Pengujian)** di pojok kanan atas.

4. **Jalankan cell dari atas ke bawah** (tombol ▶ atau `Shift+Enter`):

   | Cell | Apa yang dilakukan | Butuh internet? |
   |---|---|---|
   | 1–2 | Cek dependency + konfigurasi | Tidak |
   | 3 | Tanya provider: model apa yang tersedia (hanya `gpt-5.6-sol`) | Ya, 1 request kecil |
   | 5 | Cek tiap model bisa merespons + cek Docker | Ya, beberapa request kecil |
   | 6 | Cek/bangun image Docker CodaMOSA | Tidak (lokal) |
   | 8 | **Inti**: buat test + evaluasi semua task | Ya, banyak request |
   | 10+ | Simpan hasil, grafik, tabel RQ | Tidak |

5. **Lihat hasilnya** di folder `experiment_results/`:

   | File | Isi |
   |---|---|
   | `rows.csv` | Satu baris per (metode × task): semua angka metrik |
   | `status.json` | Status tiap kombinasi: `OK`, `BLOCKED`, `INVALID_GENERATED_TEST` + alasannya |
   | `comparison.png` | Grafik batang perbandingan kedua metode |
   | `runs/<waktu>/rq1.md`, `rq2.md` | Tabel ringkasan RQ1 & RQ2 |
   | `work/` | Berkas mentah (test yang dihasilkan, log) — boleh dihapus |

### Pertanyaan yang sering muncul

**Output berhenti lama di satu baris `[PROGRESS] ...`, apakah macet?**
Kemungkinan besar tidak. Baris progres baru tercetak setelah **satu task
selesai penuh**, dan satu task bisa memakan waktu lama (pencarian test +
evaluasi mutant). Cek tanda hidup: buka terminal dan jalankan `docker ps` —
jika ada container dengan status `Up`, berarti masih bekerja. Agar tiap langkah
terlihat, set `VERBOSE_TASK_LOG=1` di `config/.env`.

**Kenapa ada yang gagal (`BLOCKED`)?**
Wajar dan sudah dirancang. Penyebab umum: provider sedang gangguan (503),
rate limit (429), model lambat (timeout), atau test yang dihasilkan tidak
valid. Yang gagal hanya kombinasi (metode × model × task) itu — yang lain
tetap berjalan. Semua alasan tercatat di `status.json`.

**Kenapa di dashboard provider muncul banyak "cache hit"?**
Karena prompt yang dikirim mengulang bagian yang sama (kode program +
instruksi) berkali-kali. Cache hit biasanya **lebih murah** dari token biasa;
tetap tercatat di pemakaian.

**Apakah VGA/GPU saya dipakai?**
Tidak. Model AI berjalan di server provider; pekerjaan di PC (pencarian test,
mutasi, coverage) murni CPU. VGA hanya dipakai sistem untuk menampilkan layar.

**Laptop saya crash / saya harus matikan, apa hilang semua?**
Tidak, asalkan `RESUME=1` di `config/.env`. Progres disimpan berkala di
`experiment_results/runs/<waktu>/rows.csv` dan `status.json`; menjalankan
ulang cell 1→8 akan melanjutkan dari yang sudah selesai.

**Kenapa CPU terlihat cuma ~12%?**
Monitor menghitung seluruh 12 thread sebagai 100%. Dua container CodaMOSA yang
berjalan penuh memakai ~2 core (≈17% dari total). Ini disengaja
(`TASK_WORKERS=2`) agar desktop/VS Code tetap responsif dan tidak crash.

---

## Bagian 2 — Untuk kebutuhan paper

### Desain eksperimen

- **Metode:** CoverUp (coverage-guided LLM, berjalan native) dan CodaMOSA
  (search-based Pynguin + LLM saat coverage plateau, berjalan di Docker
  `pynguin-runner:latest`, Python 3.10).
- **Dataset:** HumanEval (164 task) dan Refactory (5 task) dari struktur MuTAP;
  setiap task menyediakan PUT, mutant, dan baseline suite.
- **Model LLM:** satu model tetap `gpt-5.6-sol` (keputusan kelompok), dikirim
  bare oleh CodaMOSA dan dengan prefix transport `openai/` oleh CoverUp melalui
  LiteLLM — ID model yang sampai ke provider identik.
- **Kesetaraan perbandingan:** setiap baris hasil menyimpan `mutant_set_id`;
  evaluator menolak mempromosikan run yang membandingkan metode pada mutant set
  yang berbeda.

### Pemetaan metrik (kolom `rows.csv`)

| RQ | Metrik | Kolom |
|---|---|---|
| RQ1 | Line/Branch coverage | `line_pct`, `branch_pct`, `lines_covered`, `lines_total` |
| RQ1 | Pass rate | `pass_rate`, `n_passed`, `n_tests` |
| RQ1 | Mutation score | `mutation_score`, `killed`, `survived`, `broken`, `timeout`, `n_mutants` |
| RQ2 | Coverage & pass rate | sama dengan RQ1 |
| RQ2 | Waktu | `wall_time_s` |
| RQ2 | Biaya | `cost_usd`, `calls_with_usage`, `prompt_tokens`, `completion_tokens` |

Definisi formal metrik ada di docstring `src/eval_metrics.py` dan
`docs/EXPERIMENT_PROTOCOL.md`. Mutan `broken`/`timeout` dikeluarkan dari
penyebut mutation score (protokol MuTAP).

### Profil konfigurasi (`config/.env`)

| Kunci | Pilot (cepat) | Final (paper) |
|---|---|---|
| `EVAL_MUTANT_LIMIT` | `25` | `0` (semua mutant) |
| `CODAMOSA_SEARCH_SECONDS` | `30` | `60` |
| `TASK_LIMIT` | kecil, mis. `5` | `None` |
| `TASK_WORKERS` | `2` | `2–3` |
| `RESUME` | `1` | `1` |

**Penting untuk validitas:** kedua metode harus dievaluasi dengan profil yang
sama. Mutation score dari sampel 25 mutant tidak setara dengan skor penuh —
untuk angka paper, jalankan ulang dengan `EVAL_MUTANT_LIMIT=0`.

### Alur data & lokasi artefak

```text
config/.env ──► cell 3 (discovery) ──► cell 5 (preflight per-model)
                                            │
                        ACTIVE_*_MODELS + *_ok
                                            ▼
              cell 8: generator + evaluator (per task, paralel)
                ├── work/<metode>/<model>/<dataset>/<task>/   (artefak mentah)
                └── store.checkpoint → runs/<waktu>/rows.csv + status.json
                                            ▼
              cell simpan: store.finalize → rows.csv + status.json (aktif)
                           manifest.json (valid / promoted / quality)
                                            ▼
              cell grafik (comparison.png) + tools/post_run.py (rq1.md, rq2.md)
```

Selama cell 8 berjalan, hasil sementara ada di
`experiment_results/runs/<waktu>/rows.csv`. File
`experiment_results/rows.csv` baru muncul setelah cell simpan (finalize)
berhasil dan run **dipromosikan** (syarat: jumlah status sesuai ekspektasi,
tidak ada konflik `mutant_set_id`, kualitas tidak lebih buruk dari run aktif
sebelumnya). Snapshot lama otomatis dibackup ke `experiment_results/backups/`.

### Melanjutkan run yang terputus

1. Pastikan pasangan `rows.csv` + `status.json` yang ingin dilanjutkan berada
   di root `experiment_results/`. Jika masih di `runs/<waktu>/`, salin dulu ke
   root — itulah yang dibaca `RESUME`.
2. Set `RESUME=1`, restart kernel, jalankan cell 1→8. Task berstatus `OK`
   dilewati otomatis.

### Verifikasi pasca-run (tanpa panggilan LLM)

```bash
.venv/bin/python tools/post_run.py --source experiment_results
.venv/bin/python -m pytest -q tests
```

`post_run.py` memeriksa kesehatan data (distribusi status, sel kosong, mutation
score nol merata, konflik mutant set), menjalankan re-score, dan mencetak
verdict **SIAP PAPER / BELUM SIAP PAPER** beserta alasannya. Suite `tests/`
berisi 59 test regresi (preflight per-model, rate limiter, discovery filter,
token accounting, penyimpanan hasil).

### Batas dan catatan interpretasi

- CodaMOSA sensitif terhadap format respons model; suite kosong dicatat
  `INVALID_GENERATED_TEST` dan **tidak diberi skor**
  (`docs/CODAMOSA_KNOWN_LIMITATIONS.md`).
- Kegagalan transient provider (429/503/timeout) di-retry `GENERATOR_ATTEMPTS`
  kali; yang tetap gagal menjadi `BLOCKED`, bukan skor 0.
- Rate limit provider dipatuhi lewat `RPM_LIMIT` (default 50 request/menit)
  pada tahap discovery dan preflight.
- Model non-`gpt-5.6-sol` difilter di tahap discovery
  (`MODEL_DISCOVERY_FAMILY_FILTER`), sehingga laporan hanya memuat model yang
  benar-benar dipakai.

### Keamanan

- `config/.env` ada di `.gitignore` — jangan pernah di-commit.
- Fungsi `redact()` di notebook menghapus API key dari semua pesan error.
- Jika kunci pernah tersebar (mis. ditempel ke chat), **rotasi kunci** di
  dashboard provider.


