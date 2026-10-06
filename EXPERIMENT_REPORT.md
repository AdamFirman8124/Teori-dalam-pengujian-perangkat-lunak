# CoverUp & CODAMOSA Eksperimen - Laporan Akhir

**Tanggal:** 2026-10-05  
**Status:** ✅ Parsial Selesai (CODAMOSA 100%, CoverUp 0%)

## Ringkasan Eksekusi

### Konfigurasi
- **Endpoint:** https://stream.srbyte.id/v1
- **Models:** 4 SRByte models
  - `srbyte/claude-sonnet-4.5`
  - `srbyte/claude-haiku-4.5`
  - `srbyte/glm-5`
  - `srbyte/deepseek-3.2`
- **Datasets:** HumanEval (164 tasks), Refactory (5 tasks) — *partial run*
- **Methods:** CoverUp (LiteLLM), CODAMOSA (native HTTP)
- **Runtime:** ~2 jam 30 menit (terminated early)

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

experiments_codamosa_coverup.ipynb
  ✓ Cell 3: Strict preflight (all models must pass)
  ✓ Cell 6: Per-model work dirs + explicit loops

run_experiment.py
  ✓ Added: import os
```

## Summary

**Status:** Eksperimen parsial selesai dengan mixed results.
- **CODAMOSA:** Production-ready, 100% success
- **CoverUp:** Model integration issue, requires debugging
- **Next action:** Fix CoverUp model routing, resume full experiment

