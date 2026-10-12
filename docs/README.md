# Teori dalam Pengujian Perangkat Lunak.

Repositori ini berisi materi dan eksperimen terkait teori pengujian perangkat lunak:
perbandingan generator pengujian otomatis **CoverUp** dan **CodaMOSA** pada dataset
**MuTAP** (HumanEval & Refactory), diukur dari sisi *coverage*, *pass rate*,
*mutation score*, waktu, dan biaya.

## Isi Repositori

| Path | Keterangan |
|---|---|
| `run_experiment.py` | Orkestrasi eksperimen (baseline + CoverUp) |
| `eval_metrics.py` | Perhitungan metrik: coverage, pass rate, mutation score |
| `experiments_codamosa_coverup.ipynb` | Notebook eksperimen CodaMOSA & CoverUp |
| `EXPERIMENT_PROTOCOL.md` | Definisi metrik & perintah menjalankan eksperimen |
| `EXPERIMENT_REPORT.md` | Status eksperimen terkini: perbaikan harness, hasil re-score, dan langkah berikutnya |
| `CODAMOSA_KNOWN_LIMITATIONS.md` | Keterbatasan CodaMOSA, mitigasi retry/guard, dan catatan interpretasi hasil |
| `experiment_results/` | Artefak hasil eksperimen |
| `tools/` | Utilitas pendukung |
| `codamosa/` | Sumber CodaMOSA (checkout terpisah) |
| `coverup/` | Sumber CoverUp (checkout terpisah) |
| `MuTAP/` | Dataset & harness MuTAP (checkout terpisah) |

## Menjalankan Eksperimen

```bash
# 1) Salin template kredensial dan isi dengan kunci Anda sendiri
cp .env.example .env

# 2) Baseline tanpa LLM (MuTAP-Codex, Copilot-FS, Pynguin)
.venv/bin/python run_experiment.py --dataset both --methods baselines --outdir results

# 3) CoverUp (butuh akses LLM yang valid)
.venv/bin/python run_experiment.py --dataset both --methods all --model gpt-4o --outdir results
```

> **Catatan keamanan:** jangan pernah meng-commit file `.env` berisi API key.
> Gunakan `.env.example` sebagai acuan variabel yang dibutuhkan.

