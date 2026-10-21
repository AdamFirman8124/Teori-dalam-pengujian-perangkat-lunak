# Sumber dan Versi (Fase 1)

Dicatat 21 Oktober 2026. Semua run memakai versi di bawah ini; mengubah versi
di tengah eksekusi dilarang (pedoman 14.7).

## Tool

| Tool | Versi / Commit | Catatan |
|---|---|---|
| CoverUp | `0.6.3` (source di `coverup/`) | memakai LiteLLM; butuh *function calling* |
| CodaMOSA | fork `plasma-umass/codamosa`, basis Pynguin `0.19.0` | dijalankan di container |
| Pynguin | `0.19.0` (di dalam image `pynguin-runner`) | baseline DYNAMOSA |
| MuTAP | tidak dijalankan di mesin ini | data dari kolaborator |

## Image Docker

| Image | ID | Catatan |
|---|---|---|
| `pynguin-runner:latest` | `sha256:5036213d48ac5bacd56556572017332e732cfd7c695e04e479ec00af5374dc32` | dibangun dari `codamosa/docker/Dockerfile` |

Image dibangun ulang setiap kali source `codamosa/` berubah; ID di atas harus
dicocokkan dengan `docker images --digests` sebelum protokol dibekukan.

## Evaluasi

| Paket | Versi |
|---|---|
| `coverage` | 7.16.2 |
| `MutPy` | 0.6.1 |
| `pytest` | 9.1.1 |
| `pytest-timeout` | 2.4.0 |
| `pytest-repeat` | terpasang |
| `radon` | 6.0.1 |
| `slipcover` | 1.1.0 (tidak dipakai untuk metrik; hanya internal CoverUp) |

## Benchmark

| Suite | Sumber | Jumlah |
|---|---|---|
| MT | `dataset/coverup-eval/MuTAP-benchmarks/` | 163 fungsi |
| CM | `dataset/codamosa/replication/test-apps/cm_modules.csv` | 425 modul, 24 proyek |

## Runtime

| Komponen | Versi |
|---|---|
| Python (host) | 3.14 |
| Python (container) | 3.10 |
| Docker Engine | 29.8.2 |
| OS | Ubuntu, kernel Linux (bukan WSL) |
