# Perbandingan CoverUp vs CodaMOSA sebagai Generator Test Otomatis


## Benchmark paper (pipeline aktif)

Pipeline aktif memakai suite paper yang ada di `dataset/`, bukan checkout MuTAP
lama di root:

- **MT:** tepat 163 task `f001`–`f163` dari
  `dataset/coverup-eval/MuTAP-benchmarks` untuk RQ1/RQ2.
- **CM:** tepat 425 modul / 24 package dari manifest
  `dataset/codamosa/replication/test-apps/cm_modules.csv`; checkout CodaMOSA
  tervalidasi pada commit `17a4c2a2ecb40b60e32a7e4a437db03573612f11`.
- **MuTAP generator tidak dijalankan di perangkat ini.** Hasil rekan digabung
  sesudah run melalui `tools/merge_collaborator_results.py`.

Validasi layout sebelum memakai API:

```powershell
.venv\Scripts\python.exe tools\validate_benchmarks.py
```

Urutan run: pilot MT (`TASK_FILTER=MT:f001`), MT penuh, pilot CM
(`TASK_FILTER=CM:flutils.objutils`), lalu CM penuh. Setelah hasil tersedia:

```powershell
.venv\Scripts\python.exe tools\module_characteristics.py experiment_results\module_characteristics.csv
.venv\Scripts\python.exe tools\rq_tables.py experiment_results\rows.csv experiment_results\paper_tables
```


## Struktur repositori

```text
config/                         konfigurasi tunggal: .env / .env.example
experiments_codamosa_coverup.ipynb  satu-satunya notebook eksperimen
src/                            evaluator, storage, discovery, loop helpers
tools/                          post-run, rescore, tabel RQ, provider log
scripts/                        runner alternatif
dataset/                        suite paper: MT (f001-f163) + CM (425 modul)
MuTAP/                          checkout MuTAP lama (arsip, tidak dipakai pipeline)
codamosa/                      source + Docker runner CodaMOSA
coverup/                       source runner CoverUp
docs/                           protokol, batasan, laporan, referensi
experiment_results/             output lokal (tidak di-commit)
```

## Run fresh yang direkomendasikan

1. Isi API key di `config/.env`.
2. Pastikan konfigurasi fresh:

   ```env
   COVERUP_MODELS=openai/gpt-5.6-luna
   CODAMOSA_MODELS=gpt-5.6-luna
   TASK_FILTER=
   TASK_LIMIT=None
   RESUME=0
   FRESH=1
   RUN_LABEL=luna-fresh
   TASK_WORKERS=2
   AUTO_SCALE=0
   ```

3. Restart kernel VS Code, pilih kernel `.venv`.
4. Buka `experiments_codamosa_coverup.ipynb` dan tekan **Run All**.
5. Amati `experiment_results/provider_responses_summary.md` selama run.

Semua hasil lama yang dibutuhkan untuk audit disimpan di luar output aktif atau
arsip manual; `experiment_results/` selalu dianggap disposable dan diabaikan Git.

## Struktur hasil

```text
experiment_results/
  rows.csv                         hasil aktif setelah finalize
  status.json                      status seluruh task
  provider_responses.jsonl         satu log semua respons provider
  provider_responses_summary.md    ringkasan error/token/cache
  runs/<run_id>/                   checkpoint kandidat dan manifest
  work/                            artefak mentah per metode/model/task
  llm_calls/                       log per-panggilan JSONL
  model_discovery/                 laporan discovery provider
  backups/                         backup snapshot yang dipromosikan
```

## Verifikasi tanpa LLM

```powershell
.venv\Scripts\python.exe tools\provider_responses.py
.venv\Scripts\python.exe tools\post_run.py --source experiment_results
.venv\Scripts\python.exe -m pytest tests -q
```

## Catatan validitas

- Sol tidak dijalankan lagi; hanya luna yang menjadi model aktif.
- Error provider dicatat sebagai `BLOCKED`, bukan skor nol.
- `cache_hit` tetap dihitung sebagai token yang digunakan jika provider
  melaporkan token cache.
- Mutation score dari `EVAL_MUTANT_LIMIT=25` tidak setara dengan skor paper;
  gunakan `EVAL_MUTANT_LIMIT=0` untuk hasil final.

Repositori ini menjalankan **CoverUp** dan **CodaMOSA** pada suite paper **MT**
(163 task `f001`–`f163`) dan **CM** (425 modul/24 package). MuTAP generation
akan digabung dari device kolaborator. RQ3 dihitung pada CM saja.

- **RQ1:** MT memakai mutation score; CM memakai branch/line coverage.
- **RQ2:** efek backbone, waktu, dan biaya.
- **RQ3:** Spearman parsial karakteristik modul vs keunggulan branch coverage CM.

> Panduan teknis tambahan ada di [`docs/EXPERIMENT_FLOW.md`](docs/EXPERIMENT_FLOW.md)
> (alur dari awal sampai akhir, titik pemanggilan model & token),
> [`docs/README.md`](docs/README.md), [`docs/EXPERIMENT_PROTOCOL.md`](docs/EXPERIMENT_PROTOCOL.md), dan
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
| Python 3.12 di folder `.venv` | Sudah tersedia di repo ini |
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
   | 1 | Setup: dependency, konfigurasi, path hasil | Tidak |
   | 2 | **Kesiapan device**: CPU/RAM/disk, WSL, jam, Docker | Ya (cek jam, 1 request kecil) |
   | 3 | Tanya provider: model apa yang tersedia (hanya `gpt-5.6-luna`) | Ya, 1 request kecil |
   | 4 | Cek tiap model bisa merespons | Ya, beberapa request kecil |
   | 5 | Cek/bangun image Docker CodaMOSA | Tidak (lokal) |
   | 6 | **Inti**: buat test + evaluasi semua task | Ya, banyak request |
   | 7 | Simpan hasil (finalize + manifest) | Tidak |
   | 8 | Grafik `comparison.png` + ringkasan | Tidak |
   | 9 | Verifikasi pasca-run + tabel RQ (`tools/post_run.py`) | Tidak |

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
berjalan penuh memakai ~2 core (≈17% dari total). Untuk memakai lebih banyak,
set `AUTO_SCALE=1` — cell kesiapan menaikkan beban otomatis. Jaga
`CPU_RESERVED_THREADS >= 2` bila akses lewat SSH supaya koneksi tidak putus.

---

## Bagian 1b — Pindah ke PC yang menyala 24 jam

Bagian ini untuk memindahkan eksperimen ke PC/mesin yang hidup terus.

### Ringkas: 6 langkah

```bash
# 1) Di PC ini: pastikan semua perubahan sudah terkirim
git status          # harus bersih (tidak ada "M ...")
git push origin main

# 2) Di PC 24 jam: ambil kode
git clone https://github.com/AdamFirman8124/Teori-dalam-pengujian-perangkat-lunak.git
cd Teori-dalam-pengujian-perangkat-lunak

# 3) Buat Python env + daftarkan kernel
python3 -m venv .venv
.venv/bin/pip install -r config/requirements.txt
.venv/bin/python -m ipykernel install --user --name teori-pengujian \
  --display-name 'Python (.venv Teori Pengujian)'

# 4) Isi kredensial (hanya 2 nilai: endpoint + API key)
cp config/.env.example config/.env
nano config/.env        # isi OCTA_API_KEY dan OPENAI_BASE_URL saja

# 5) Siapkan Docker (untuk CodaMOSA)
docker info             # harus menampilkan Server Version

# 6) Jalankan di tmux supaya selamat dari putus koneksi
tmux new -s exp
.venv/bin/python tools/run_notebook.py experiments_codamosa_coverup.ipynb out.ipynb
# tekan Ctrl+B lalu D untuk detach — proses tetap jalan
```

Pantau kapan saja dengan: `tmux attach -t exp`.

### Yang WAJIB ada di PC 24 jam

| Kebutuhan | Cara cek | Kalau belum ada |
|---|---|---|
| Python 3.11+ | `python3 --version` | `sudo apt install python3 python3-venv` |
| Docker Engine | `docker info` | `sudo apt install docker.io` + `sudo usermod -aG docker $USER` |
| Git | `git --version` | `sudo apt install git` |
| Ruang disk ≥ 5 GB | `df -h .` | bersihkan `experiment_results/work/` |
| Internet stabil | `curl -sI https://router.octalabs.id/v1/models` | perbaiki jaringan |
| Jam akurat | cell kesiapan akan memeriksa | `sudo hwclock -s` |

Cell **Kesiapan Device** memeriksa semua ini otomatis sebelum eksperimen mulai,
jadi Anda tidak perlu menebak.

### Isi `config/.env` (hanya 2 baris yang perlu diubah)

```env
OCTA_API_KEY=<token Anda>
OPENAI_BASE_URL=https://router.octalabs.id/v1
```

Sisanya sudah punya nilai bawaan yang benar. `config/.env` **tidak ikut Git**,
jadi harus diisi manual di setiap mesin — jangan pernah dikirim lewat chat.

### Kalau PC 24 jam hanya menyediakan Windows (WSL)

Cell kesiapan mendeteksi WSL otomatis dan menyesuaikan:

- **WSL2** → didukung penuh. Docker harus lewat **Docker Desktop Windows**:
  aktifkan *Settings → Resources → WSL Integration* untuk distro Anda.
- **WSL1** → **diblokir** (tidak punya kernel Linux penuh, Docker tidak jalan).
  Perbaiki: `wsl --set-version <distro> 2` di PowerShell admin.
- **Repo di `/mnt/c/...`** → diberi peringatan: I/O 2–5× lebih lambat.
  Sebaiknya `git clone` ke home WSL (`~/`) untuk run 24 jam.
- **Batas RAM/CPU** mengikuti `.wslconfig` Windows, bukan spek fisik PC.
  Cell membaca file itu dan menampilkan batas efektifnya.
- **Windows sleep** akan membekukan WSL → set *Power → Sleep = Never* saat dicolok.

### Mengatur beban CPU

```env
CPU_RESERVED_THREADS=2   # thread yang disisakan untuk desktop + koneksi remote
AUTO_SCALE=1             # naikkan beban otomatis bila PC kuat
CONFIG_MAX_LOAD=8        # batas keras jumlah worker
TASK_WORKERS=3           # jumlah task paralel
EVAL_MUTANT_WORKERS=2    # subprocess mutasi per task
```

Rumus budget: `cpu_count - CPU_RESERVED_THREADS`, lalu dibagi
`(1 + EVAL_MUTANT_WORKERS)` per pipeline. Dengan `AUTO_SCALE=1`, cell kesiapan
menghitung ulang sendiri. **Selalu sisakan ≥2 thread** bila Anda mengakses PC
lewat SSH/VS Code Remote — kalau tidak, koneksi bisa terputus.

### Menjalankan bertahap (aman untuk 24 jam)

```env
RESUME=1        # lanjutkan task yang sudah OK, jangan ulang
```

Progres disimpan berkala ke `experiment_results/runs/<waktu>/`. Kalau PC mati,
restart, atau Windows update memaksa reboot: jalankan lagi dari cell 1 —
task berstatus `OK` dilewati otomatis.

### Kalau provider rate limit (50 RPM)

```env
RPM_LIMIT=50              # 1 request setiap 1,2 detik
RPM_RETRY_ATTEMPTS=4      # retry saat kena 429
RPM_RETRY_WAIT=5
```

### Cek kesehatan hasil (tanpa biaya)

```bash
.venv/bin/python tools/post_run.py --source experiment_results
```

Akan mencetak verdict **SIAP PAPER / BELUM SIAP PAPER** beserta alasannya.

---

## Bagian 2 — Untuk kebutuhan paper

### Desain eksperimen

- **Metode:** CoverUp (coverage-guided LLM, berjalan native) dan CodaMOSA
  (search-based Pynguin + LLM saat coverage plateau, berjalan di Docker
  `pynguin-runner:latest`, Python 3.10).
- **Dataset:** MT = 163 task CoverUp (`dataset/coverup-eval/MuTAP-benchmarks`,
  PUT + `package.txt`); CM = 425 modul dari
  `dataset/codamosa/replication/test-apps/cm_modules.csv` (paket multi-file).
  Mutation score hanya dihitung pada MT; CM memakai coverage (sesuai protokol).
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
| `TASK_WORKERS` | `2–3` | `3–8` (sesuai CPU) |
| `RESUME` | `1` | `1` |

Kunci kesiapan/lingkungan (bukan bagian RQ, hanya operasional):

| Kunci | Arti |
|---|---|
| `CPU_RESERVED_THREADS` | Thread yang disisakan untuk desktop/remote (default 2) |
| `AUTO_SCALE` | `1` = naikkan beban otomatis bila PC kuat |
| `CONFIG_MAX_LOAD` | Batas keras jumlah worker |
| `CLOCK_WARN_SECONDS` / `CLOCK_BLOCK_SECONDS` | Ambang selisih jam lokal vs provider |
| `AUTO_INSTALL` | `1` = `pip install` otomatis paket yang hilang |
| `RPM_LIMIT` | Kuota request/menit provider (default 50) |

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
berisi 76 test regresi (preflight per-model, rate limiter, discovery filter,
kesiapan device/WSL, clock drift, token accounting, penyimpanan hasil).

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


