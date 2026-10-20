# CoverUp & CodaMOSA - Laporan Status Eksperimen

**Status:** Pipeline siap; data lengkap **belum** tersedia (butuh kuota LLM untuk full run).
**Terakhir diperbarui:** 2026-10-12

> Dokumen ini menggantikan laporan lama yang menyebut endpoint SRByte dan
> CoverUp 0%. Angka lama itu **tidak valid** karena berasal dari harness yang
> belum diperbaiki (lihat `CODAMOSA_KNOWN_LIMITATIONS.md`).

## 1. Lingkungan

- **Endpoint:** OpenAI-compatible OctaLabs (`https://router.octalabs.id/v1`), gaya `chat`.
- **Model:** `claude-sonnet-5`, `gpt-5.5` (CoverUp memakai prefix transport `openai/`).
- **Dataset:** HumanEval (164 task), Refactory (5 task: q1..q5).
- **CodaMOSA:** dijalankan di dalam image Docker `pynguin-runner:latest`.

## 2. Perbaikan harness yang sudah terverifikasi

| Perbaikan | Lokasi | Bukti |
|---|---|---|
| Mutation score tidak lagi `0.0%` (mutan kini benar-benar menaungi PUT) | `src/eval_metrics.py::mutation_score_of` | HumanEval/0 CoverUp: `0.0%` -> `83.33%` |
| `pass_rate` tidak lagi mengoleksi file asing dari parent dir | `src/eval_metrics.py::pass_rate_of` | `n_tests` konsisten dengan suite tervalidasi |
| Klasifikasi killed/survived tidak lagi substring match | `src/eval_metrics.py::pytest_outcome` | 8 unit test |
| Suite kosong/`except: pass` ditolak | `src/eval_metrics.py::suite_validity` | test parametrik |
| CodaMOSA: guard empty archive & empty LLM seeding | `codamosa/.../codamosastrategy.py` | tidak lagi `IndexError` |
| CodaMOSA: retry seeding terbatas | `codamosa/pynguin/analyses/seeding.py` | `CODAMOSA_LLM_RETRIES` |
| CoverUp: transport error (5xx/connection) di-retry, bukan langsung `giving up` | `coverup/src/coverup/llm.py` | `tests/test_coverup_retry.py` |

## 3. Hasil re-score artefak (tanpa LLM)

`tools/rescore_existing.py` mengukur ulang suite yang masih ada di
`experiment_results/work` dengan harness terkini. Hasil
(`experiment_results/rescore_smoke/`):

**RQ1 - per metode**

| method | n_tasks | line_pct | pass_rate | mutation_score |
|---|---|---|---|---|
| CoverUp | 10 | 100.0% | 100.0% | 85.95% |
| CODAMOSA | 4 | 98.18% | 100.0% | 90.0% |

**RQ2 - per backbone**

| backbone | n_tasks | line_pct | pass_rate | wall_time_s | cost_usd |
|---|---|---|---|---|---|
| gpt-5.5 | 10 | 99.24% | 100.0% | 143.1 s total / 11.92 s avg | $0.1723 total |
| claude-sonnet-5 | 9 | 100.0% | 100.0% | 408.91 s total / 37.17 s avg | $0.0 total |

> **Catatan:** angka ini berasal dari suite yang kebetulan masih ada di disk
> (23 baris, 7 di-skip). **Belum** seimbang dan **belum** cukup untuk klaim
> final, tetapi sudah cukup untuk membuktikan pengaruh perbaikan harness.

## 4. Bukti smoke test terbaru (dengan LLM)

1 task, 1 model/metode, `GENERATOR_ATTEMPTS=2`:

- CodaMOSA `claude-sonnet-5` HumanEval/0: suite **valid**, `line_pct=100`,
  `mutation_score=66.67` (killed 2, survived 1).
- CoverUp `claude-sonnet-5` HumanEval/0: **BLOCKED** karena
  `InternalServerError: Connection error` lalu `giving up` — akar masalah sudah
  diperbaiki di `llm.py` dan akan aktif pada image/run berikutnya.

## 5. Yang masih menghalangi klaim final

1. **Full run belum dijalankan** (butuh kuota LLM). `n` masih kecil dan tidak seimbang.
2. **7 sel kosong** pada matriks (suite tidak ada/ tidak valid).
3. **CodaMOSA crash** pada beberapa task masih mungkin; perlu dipantau di run penuh.
4. **CoverUp retry baru teruji unit**, belum diuji end-to-end lewat provider nyata.

## 6. Langkah selanjutnya

```bash
# 1) (wajib) rebuild image setelah patch codamosa & retry
docker build --build-arg CODAMOSA_SOURCE_SHA=$(python3 - <<'PY'
import hashlib
from pathlib import Path
r=Path("codamosa"); d=hashlib.sha256()
for p in sorted(r.rglob("*")):
    if p.is_file() and p.name!=".DS_Store" and "__pycache__" not in p.parts:
        d.update(str(p.relative_to(r)).encode()); d.update(p.read_bytes())
print(d.hexdigest())
PY
) -t pynguin-runner:latest -f codamosa/docker/Dockerfile codamosa

# 2) full run (butuh kuota); Windows lalu Ubuntu native
#    experiments_coverup_windows.ipynb dari atas ke bawah
#    experiments_codamosa_linux.ipynb dari atas ke bawah

# 3) re-score (gratis) setelah run
.venv/bin/python tools/rescore_existing.py \
    --source experiment_results --outdir experiment_results/rescore_full

# 4) regenerasi tabel RQ
.venv/bin/python tools/rq_tables.py experiment_results/rows.csv results_dir
```

## 7. Aturan pelaporan

- Jangan memakai angka dari run `20261010T164023Z_manual` (harness lama, mutation score 0.0%).
- Sertakan `n` efektif setelah filtering status `OK`.
- Simpan distribusi `OK` / `BLOCKED` / `INVALID_GENERATED_TEST` sebagai konteks.
- Mutation score hanya dibandingkan pada himpunan mutan yang sama
  (`mutant_set_id`); `storage.mutant_set_conflicts` memblokir promosi bila berbeda.


### Hasil Eksperimen

| Method | Model | Status | Tasks | Output |
|--------|-------|--------|-------|--------|
| **CODAMOSA** | 4 × claude-sonnet-4.5 | ✅ OK | 4/4 | 32 test files |
| | 4 × claude-haiku-4.5 | ✅ OK | 4/4 | |
| | 4 × glm-5 | ✅ OK | 4/4 | |
| | 4 × deepseek-3.2 | ✅ OK | 4/4 | |
| **CoverUp** | 4 × claude-sonnet-4.5 | ⚠️ INCOMPLETE | 0/5 | 0 test files |
| | 4 × claude-haiku-4.5 | ⚠️ INCOMPLETE | 0/4 | |
| | 4 × glm-5 | ⚠️ INCOMPLETE | 0/4 | |
| | 4 × deepseek-3.2 | ⚠️ INCOMPLETE | 0/4 | |

**Total:** 33 tasks diproses, 16 berhasil (CODAMOSA)

### Output Artifacts

```
/home/masoyi/stacks/PRPL/experiment_results/
├── work/
│   ├── codamosa/
│   │   ├── srbyte_claude-sonnet-4.5/HumanEval/{0,1,2,3}/output/test_script_*.py
│   │   ├── srbyte_claude-haiku-4.5/HumanEval/{0,1,2,3}/output/test_script_*.py
│   │   ├── srbyte_glm-5/HumanEval/{0,1,2,3}/output/test_script_*.py
│   │   └── srbyte_deepseek-3.2/HumanEval/{0,1,2,3}/output/test_script_*.py
│   └── coverup/
│       ├── openai_srbyte_claude-sonnet-4.5/HumanEval/{0-4}/
│       │   ├── coverup.log (API calls logged)
│       │   ├── coverup.checkpoint
│       │   └── (no output/test_script_*.py)
│       └── ... (similar for other models)
├── status.json (33 records)
└── Size: 1.6 MB
```

## Analisis

### ✅ CODAMOSA - Sukses

**Mengapa berhasil:**
- Direct HTTP calls ke `/v1/chat/completions`
- Model ID format: `srbyte/...` (bare name)
- Docker-based test execution (pynguin container)
- Checkpoint system berjalan sempurna
- Semua 4 model menghasilkan test cases

**Output:**
- 2 test files per task (test_script_*.py, test_script_*_failing.py)
- Coverage evaluation via Docker
- Consistent hasil di semua model

### ⚠️ CoverUp - Gagal Generating Output

**Observasi:**
1. Checkpoints dibuat ✓
2. API calls tercatat di coverup.log ✓
3. Model responses diterima ✓
4. Tapi: **Tidak ada output/test_script_*.py**

**coverup.log snippet:**
```json
{
  "model": "openai/srbyte/claude-sonnet-4.5",
  "messages": [...],
  "tools": [{"name": "get_info", ...}]
}
```

**Kemungkinan masalah:**
1. Model ID parsing di CoverUp (openai/ prefix handling)
2. Tool response parsing error
3. Test extraction dari model output gagal
4. Format response mismatch antara SRByte dan OpenAI API

## Format Model ID Resolution

Patch yang diterapkan:
- **CODAMOSA:** Direct `srbyte/...` → works ✓
- **CoverUp (LiteLLM):** `openai/srbyte/...` → API OK, output fail ⚠️

```python
# Notebook patch status
✓ Cell 3: Preflight checks (strict per-model)
✓ Cell 6: Per-model work directories + loops
✓ .env: Model ID normalization applied
```

## Environment & Setup

### Perubahan Applied
1. **Notebook patches:**
   - Strict preflight: fail hard if any model invalid
   - Per-model work dirs: `work/{method}/{model_slug}/{dataset}/{task_id}/`
   - Loop structure: iterate all models explicitly

2. **Model ID format:**
   - CODAMOSA_MODELS: bare `srbyte/...`
   - COVERUP_MODELS: `openai/srbyte/...` (LiteLLM transport prefix)

3. **API Key:** Rotated (new key active)

## Rekomendasi Next Steps

### 1. Debug CoverUp (Prioritas Tinggi)
```bash
# Inspect single task
cat /home/masoyi/stacks/PRPL/experiment_results/work/coverup/*/HumanEval/0/coverup.log | tail -100

# Check for model ID issues
grep "model\|error" coverup.log | head -20

# Run single CoverUp task manually with debug
coverup --tests-dir ... --model openai/srbyte/claude-sonnet-4.5 --verbose
```

### 2. Resume Eksperimen
- **CODAMOSA:** Siap lanjut dari task 4+ (checkpoints ada)
- **CoverUp:** Perlu fix format issue dulu

### 3. Full Scale Eksperimen
```bash
TASK_LIMIT=None  # Run all 164 HumanEval + 5 Refactory
# Duration estimate: 8-12 hours (2 methods × 4 models)
```

### 4. Validation
- [ ] Verify CoverUp model ID normalization
- [ ] Test LiteLLM routing untuk SRByte
- [ ] Inspect tool response parsing
- [ ] Run preflight untuk CoverUp only

## Files Modified

```
.env
  ✓ COVERUP_MODELS=openai/srbyte/...
  ✓ CODAMOSA_MODELS=srbyte/...
  ✓ API key rotated

experiments_coverup_windows.ipynb
experiments_codamosa_linux.ipynb
  ✓ Notebook dipisah berdasarkan metode dan OS
  ✓ Model `gpt-5.6-sol` tanpa label backbone buatan
  ✓ Hardware profile i5-11400F / RAM 16 GB

run_experiment.py
  ✓ Added: import os
```

## Summary

**Status:** Eksperimen parsial selesai dengan mixed results.
- **CODAMOSA:** Production-ready, 100% success
- **CoverUp:** Model integration issue, requires debugging
- **Next action:** Fix CoverUp model routing, resume full experiment

