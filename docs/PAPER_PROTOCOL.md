# Protokol Eksperimen Final (sesuai rancangan Bab IV–VII)

## Keputusan tetap

- `R = 10` run independen per `(suite, tool, backbone, unit)`.
- Budget generasi = `600 s` per tool per unit.
- B1 = proprietary; B2 = open-weight.
- MuTAP hanya berasal dari kolaborator dan tidak dijalankan di mesin ini.
- Pynguin baseline memakai DynaMOSA tanpa LLM, budget yang sama.
- LC/BC memakai `coverage.py`; MS memakai satu himpunan mutant per unit.
- Raw validity diukur sebelum tool memperbaiki/membuang proposal.
- Flaky = jumlah unit test yang berubah outcome dalam 5 rerun.
- Agregasi: median 10 run per unit, lalu median lintas unit.

## Identitas dan resume

Setiap row/status membawa `run_index=1..10`. Resume key adalah
`(method, model, dataset, task, run_index)`, sehingga restart tidak
mencampur replikasi atau menganggap satu run sudah mewakili sepuluh run.

## Keterbatasan model saat ini

Endpoint SrByte hanya mengembalikan model transport `auto`. B2 belum dapat
dijalankan sampai provider menyediakan ID open-weight kedua. Hasil B1 boleh
dikumpulkan sekarang; tabel RQ2 tetap kosong sampai B2 tersedia. Label hasil
harus merupakan backend yang dapat diverifikasi, bukan tebakan dari alias.

## Data pilot

Run lama dipindahkan ke `experiment_results_pilot_auto_linux/` dan tidak
digabung ke hasil final karena R=1 dan budgetnya 30 s untuk CodaMOSA.
