# Alur Eksperimen: dari Konfigurasi sampai Hasil

Dokumen ini menjelaskan **seluruh alur eksperimen** secara berurutan: apa yang
terjadi di setiap cell, di mana **CoverUp** dan **CodaMOSA** bekerja, di mana
**model LLM benar-benar dipanggil**, dan di mana **token dibelanjakan**.

Semua jalur di dokumen ini relatif terhadap root repositori.

---

## 0. Ringkasan satu paragraf

`config/.env` menentukan model dan budget. Dua notebook dipisah per metode/OS:
`experiments_linux.ipynb` menjalankan CoverUp secara Windows-native dan
`experiments_linux.ipynb` menjalankan CodaMOSA di Ubuntu native (bukan WSL).
Keduanya menjalankan setup, kesiapan device, discovery model, preflight,
**generator + evaluator**, finalize, lalu analisis; notebook CodaMOSA juga membangun
image Docker. Generator memanggil LLM untuk **menghasilkan test** (CoverUp lewat
subprocess Python, CodaMOSA lewat container Docker). Evaluator **tidak** memanggil
LLM sama sekali — ia hanya menjalankan pytest, SlipCover, dan mutant secara lokal.

---

## 1. Diagram alur besar

```text
config/.env
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 1  Setup                                               │
│  • load .env, set alias credential                          │
│  • baca COVERUP_MODELS / CODAMOSA_MODELS                    │
│  • hitung TASK_WORKERS, EVAL_MUTANT_WORKERS                 │
│  • TASKS = 169 HumanEval + 5 Refactory                      │
│  • store.begin()  → runs/<run_id>/                          │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 3  Kesiapan device          [1 HTTP GET, tanpa token]  │
│  CPU / RAM / disk / paket / Docker / clock drift            │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 4  Discovery                [TOKEN: 1 per model]       │
│  GET /models  → daftar model                                │
│  probe max_tokens=1 per model                               │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 6  Preflight                [TOKEN: 1 per model]       │
│  CoverUp  : litellm.completion(max_tokens=1)                │
│  CodaMOSA : requests.post(max_tokens=1)                     │
│  Docker   : daemon + DNS container                          │
│  → ACTIVE_COVERUP_MODELS, ACTIVE_CODAMOSA_MODELS            │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 7  Image Docker CodaMOSA    [tanpa token]              │
│  docker build bila label source-sha tidak cocok             │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
╔═════════════════════════════════════════════════════════════╗
║ CELL 9  GENERATOR + EVALUATOR   [TOKEN: PALING BANYAK]      ║
║                                                             ║
║  ThreadPoolExecutor(TASK_WORKERS=2)                         ║
║  untuk setiap task (dataset, task_id):                      ║
║                                                             ║
║    ┌── CoverUp ────────────────────────────┐                ║
║    │ subprocess: python -m coverup         │  ← TOKEN       ║
║    │  → test_coverup_*.py                  │                ║
║    └───────────────────────────────────────┘                ║
║    ┌── Evaluator CoverUp ──────────────────┐                ║
║    │ pytest + slipcover + mut.py           │  ← tanpa token ║
║    └───────────────────────────────────────┘                ║
║                                                             ║
║    ┌── CodaMOSA ───────────────────────────┐                ║
║    │ docker run pynguin-runner             │  ← TOKEN       ║
║    │  → test_script_*.py                   │                ║
║    └───────────────────────────────────────┘                ║
║    ┌── Evaluator CodaMOSA ─────────────────┐                ║
║    │ pytest + slipcover + mut.py           │  ← tanpa token ║
║    └───────────────────────────────────────┘                ║
║                                                             ║
║    store.checkpoint() → runs/<run_id>/                      ║
╚═════════════════════════════════════════════════════════════╝
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 11 Finalize                 [tanpa token]              │
│  validasi kelengkapan status, konflik mutant, unmeasured     │
│  promote → experiment_results/rows.csv + status.json        │
│  backup snapshot lama → backups/<run_id>/                   │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ CELL 13 Grafik comparison.png           [tanpa token]       │
│ CELL 15 Tabel log LLM per panggilan     [tanpa token]       │
│ CELL 18 Tabel BB / RV / Flaky / LC / BC / MS                │
│ CELL 20 Wilcoxon + Holm + A12                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Tahap per tahap: input, proses, output

### Tahap A — Cell 1: Setup (tanpa token)

| Item | Detail |
|---|---|
| Sumber konfigurasi | `config/.env` (satu-satunya file env) |
| Model aktif | `COVERUP_MODELS=openai/gpt-5.6-luna`, `CODAMOSA_MODELS=gpt-5.6-luna` |
| Dataset | 169 task HumanEval + 5 task Refactory (dari `MuTAP/`) |
| Paralelisme | `TASK_WORKERS=2` (2 task jalan bersamaan) |
| Direktori hasil | `store.begin()` → `experiment_results/runs/<run_id>/` |

Cell ini **hanya menyiapkan variabel**; belum menyentuh provider.

### Tahap B — Cell 3: Kesiapan device (tanpa token)

- Cek CPU, RAM, disk, paket Python, daemon Docker.
- Cek selisih jam via satu HTTP GET `…/v1/models` (membaca header `Date`,
  bukan memanggil model). Tidak ada prompt, tidak ada token.

### Tahap C — Cell 4: Discovery (TOKEN: ~1 per model)

1. `GET …/v1/models` → daftar model yang ditawarkan provider.
2. Untuk tiap model: satu probe `max_tokens=1` lewat
   `src/model_discovery.py` (`discover_and_probe`).

Tujuannya hanya menjawab "model apa yang hidup sekarang".

### Tahap D — Cell 6: Preflight (TOKEN: ~1 per model per metode)

| Pemeriksaan | Kode | Token |
|---|---|---|
| CoverUp | `coverup_preflight()` → `litellm.completion(…, max_tokens=1)` | 1 |
| CodaMOSA | `codamosa_preflight()` → `requests.post(…, max_tokens=1)` | 1 |
| Docker | daemon + DNS dari dalam container | 0 |

Hasilnya `ACTIVE_COVERUP_MODELS` dan `ACTIVE_CODAMOSA_MODELS`. Hanya model yang
lolos yang dipakai di cell 9.

### Tahap E — Cell 7: Image Docker (tanpa token)

`ensure_codamosa_image()` menghitung hash source `codamosa/` dan menjalankan
`docker build` bila label image tidak cocok. Murni lokal.

### Tahap F — Cell 9: Generator + Evaluator (TOKEN PALING BANYAK)

Inti eksperimen. Untuk **setiap task**:

```text
task (mis. HumanEval/42)
 ├──► CoverUp   → test_coverup_*.py   → evaluator → angka metrik
 └──► CodaMOSA  → test_script_*.py    → evaluator → angka metrik
```

Dua task berjalan paralel (`TASK_WORKERS=2`), lalu checkpoint ditulis ke
`runs/<run_id>/` setiap satu task selesai.

---

## 3. Jalur CoverUp — model dipanggil lewat subprocess Python

```text
cell 9
  → python -m coverup \
       --model openai/gpt-5.6-luna \
       --max-attempts 3 --rate-limit 8000 --model-temperature 0
  → coverup/src/coverup/coverup.py          (iterasi coverage)
  → coverup/src/coverup/llm.py::_send_request
       → litellm.acreate()                  ← PANGGILAN MODEL
```

Model menerima kode PUT, segmen yang belum tercakup, dan test yang sudah ada.
Model mengembalikan usulan test Python. CoverUp menjalankannya dengan pytest;
test yang menaikkan coverage dipertahankan, lalu proses diulang sampai segmen
habis atau `max-attempts` tercapai.

Output mentah per task:

```text
work/coverup/openai_gpt-5.6-luna/<dataset>/<task>/
  tests/test_coverup_*.py      ← suite hasil generasi (dinilai!)
  coverup.checkpoint           ← progres + usage + counter G/F/U/R
  coverup.log                  ← log mentah CoverUp
  pytest_collect.*.log         ← bukti suite lolos collection
llm_calls/CoverUp/<model>/<dataset>/<task>.jsonl   ← 1 baris per panggilan
```


---

## 5. Evaluator lokal — tanpa satu pun token

Setelah suite dihasilkan, `src/eval_metrics.py::evaluate()` mengukur semuanya
**secara lokal** di direktori temporer:

| Metrik | Cara ukur | Token |
|---|---|---:|
| Line coverage | SlipCover | 0 |
| Branch coverage | SlipCover | 0 |
| Pass rate | `python -m pytest`, tiap unit terisolasi | 0 |
| Mutation score | mutant + pytest per mutant | 0 |
| Wall time / cost | stopwatch + checkpoint | 0 |

## 6. Penyimpanan hasil

```text
cell 9  → store.checkpoint()
       → experiment_results/runs/<run_id>/rows.csv + status.json
cell 11 → store.finalize()
       → validasi status, mutant set, unmeasured rows
       → promote ke experiment_results/rows.csv + status.json
```

`manifest.json` mencatat validitas dan alasan promosi/penolakan. `rows.csv`
aktif hanya ditulis saat snapshot lengkap berhasil dipromosikan.

## 7. Token dan respons provider

Token dibelanjakan di cell 4, cell 6, dan terutama cell 9. Evaluator serta
analisis cell 11–20 semuanya lokal dan tidak memanggil model.

```text
experiment_results/provider_responses.jsonl
experiment_results/provider_responses_summary.md
```

| `outcome` | Arti |
|---|---|
| `ok` | completion valid dan dipakai untuk test |
| `cache_hit` | provider mengembalikan cache; token cache tetap dihitung |
| `error` | provider gagal; token tetap bisa ditagih, tetapi jumlahnya `unknown` jika usage tidak dikirim |

Field penting: `status_code`, `error_code`, `prompt_tokens`,
`completion_tokens`, `total_tokens`, `cache_read_tokens`, `cache_write_tokens`,
`cost_usd`, `usage_reported`, `billed_unknown`.

Jalankan tanpa API request:

```powershell
.venv\Scripts\python.exe tools\provider_responses.py
```

## 8. Glosarium peran

| Aktor | Kerja | Token | Lokasi |
|---|---|---:|---|
| `gpt-5.6-sol` | menghasilkan test (CoverUp) atau assertion (CodaMOSA) | ya | provider |
| CoverUp | iterasi coverage: prompt → test → validasi | per prompt | `coverup/src/coverup/` |
| CodaMOSA | evolusi test + prompt assertion | per prompt | `codamosa/pynguin/languagemodels/` |
| Evaluator | coverage, pass rate, mutation score | tidak | `src/eval_metrics.py` |
| Storage | checkpoint, finalize, backup | tidak | `src/experiment_storage.py` |
| Notebook | orkestrasi dan analisis | tidak | `experiments_linux.ipynb`, `experiments_linux.ipynb` |

## 9. Verifikasi tanpa LLM

```powershell
.venv\Scripts\python.exe tools\provider_responses.py
.venv\Scripts\python.exe tools\post_run.py --source experiment_results
.venv\Scripts\python.exe -m pytest tests -q
```

*State dokumentasi: backbone aktif `gpt-5.6-sol` (dikirim apa adanya, tanpa label
buatan), satu `.env`, `TASK_WORKERS=2`, dan retry minimal.*

Data nyata run sebelumnya: median 1 panggilan per task (rata-rata 1,6, maks 6),
prompt median 832 token, waktu median ±23 detik per task.

---

## 4. Jalur CodaMOSA — model dipanggil dari dalam container Docker

```text
cell 9
  → docker run --rm --name prpl-codamosa-<model>-main-<dataset>-<task>
       -v <project>:/input:ro -v <output>:/output
       -v <auth>:/run/codamosa-auth:ro
       -v <host-jsonl>:/output/llm_calls.jsonl
       -e CODAMOSA_LLM_CALLS_LOG=/output/llm_calls.jsonl
       pynguin-runner:latest
       --model_name gpt-5.6-luna
       --maximum_search_time 60 --population 5 --temperature 0.8
  → codamosa/pynguin/languagemodels/model.py::complete_model
       → requests.post(/chat/completions)   ← PANGGILAN MODEL
```

CodaMOSA menjalankan pencarian evolusioner (genetic algorithm). Untuk candidate
yang menjanjikan, model diminta menghasilkan **assertion** (oracle).
Suite tanpa assertion ditolak sebagai `INVALID_GENERATED_TEST`.

Output mentah per task:

```text
work/codamosa/gpt-5.6-luna/<dataset>/<task>/
  project/                     ← salinan PUT (read-only di container)
  output/test_script_*.py      ← suite hasil generasi (dinilai!)
  output/statistics.csv        ← LLMCalls, LLMQueryTime, LineCoverage
  docker.stdout.log            ← stdout container
  docker.stderr.log            ← biasanya hanya warning pip
llm_calls/CODAMOSA/<model>/<dataset>/<task>.jsonl
```

Nama container unik per task dan selalu `docker rm -f` saat timeout, sehingga
retry tidak meninggalkan container zombie pemakan CPU.

Data nyata: median **10** panggilan per task (rata-rata 14, maks 54),
waktu median ±43 detik per task.


