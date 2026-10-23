# Laporan Eksperimen CodaMOSA vs CoverUp

## 1. Status

Dokumen ini dibuat otomatis dari artefak pipeline. Angka hasil hanya diisi dari data yang benar-benar diukur; angka dummy File A tidak digunakan sebagai target atau hasil.

- Probe endpoint: **selesai**
- Pilot R=2: **selesai/sebagian**
- Run utama R=10: **belum dijalankan**

## 2. Interpretasi Rancangan

File B bersifat otoritatif. Pipeline ini mengukur CodaMOSA dan CoverUp pada MT dan CM dengan dua backbone. Hasil Pynguin dan MuTAP akan digabung dari kolaborator menggunakan skema hasil yang sama.

Perbandingan tool pada suite yang sama bersifat berpasangan per unit. Perbandingan MT dengan CM untuk tool yang sama bersifat deskriptif karena unit MT dan CM tidak berpasangan.

## 3. Inventaris Dataset

| Suite | Definisi satu task | Tersedia | Dipakai pilot | Dipakai run utama |
|---|---|---|---|---|
| MT | Satu fungsi benchmark dalam satu modul f001–f163 | 163 | 5 | 163 |
| CM | Satu modul Python pada satu baris cm_modules.csv | 425 | 3 | 40 |
| Total | — | 588 | 8 | 203 |

Inventaris mentah berisi **163 MT + 425 CM = 588 task**. Sesuai File B, run utama tidak memakai seluruh CM; ia memakai seluruh 163 MT dan sampel CM bertingkat sebanyak 40, sehingga terdapat **203 unit analisis utama**.

### Sampel CM per proyek

| Proyek | Jumlah |
|---|---|
| PySnooper | 1 |
| ansible | 10 |
| black | 1 |
| dataclasses-json | 1 |
| flutils | 1 |
| httpie | 3 |
| isort | 1 |
| py-backwards | 2 |
| pyMonet | 1 |
| pypara | 1 |
| python-semantic-release | 1 |
| pytutils | 1 |
| sty | 1 |
| tornado | 1 |
| typesystem | 4 |
| youtube-dl | 10 |

### Sampel CM per stratum

| Stratum | Jumlah |
|---|---|
| L0B0 | 6 |
| L0B1 | 6 |
| L1B0 | 5 |
| L1B1 | 5 |
| L1B2 | 4 |
| L2B0 | 4 |
| L2B1 | 5 |
| L2B2 | 5 |

Deviasi yang disetujui: stratum L0B2 kosong pada populasi aktual, sehingga sampel mencakup seluruh delapan stratum non-kosong, bukan memaksakan stratum kesembilan.

## 4. Matriks Run

| Tahap | Jumlah run |
|---|---|
| Pilot: 5 MT + 3 CM × 2 tool × 2 backbone × R=2 | 64 |
| Utama: 163 MT + 40 CM × 2 tool × 2 backbone × R=10 | 8120 |

## 5. Model dan Probe

| Backbone | Requested | Returned | Function calling | Status/Error |
|---|---|---|---|---|
| B1 | entah/auto | auto | True | PASS |
| B2 | entah/auto | auto | True | PASS |

B1 dilaporkan sebagai `gpt-5.6-sol (seller-claimed; endpoint reports "auto")`. Identitas model adalah klaim penjual dan tidak dapat diverifikasi. Field model mentah dari setiap respons harus tetap disimpan untuk audit routing.

## 6. Hasil Pilot

| Suite | Tool | Backbone | Run tercatat | OK | Gagal | Biaya USD |
|---|---|---|---|---|---|---|
| MT | CoverUp | B1 | 1 | 0 | 1 | 0.036064 |

## 7. Hasil Utama

_Belum tersedia._

Analisis akhir menggunakan mean, median, dan standard deviation; Wilcoxon signed-rank berpasangan; koreksi Holm; Vargha–Delaney A12; dan bootstrap CI 95% untuk selisih mean.

## 8. Task Gagal atau Dikeluarkan

Daftar rinci tersedia di `results/analysis/excluded_tasks.csv` atau `results/pilot_analysis/excluded_tasks.csv`. Tidak ada task yang boleh dikeluarkan untuk menyesuaikan hasil dengan File A.

## 9. Deviasi dari File B

1. File A memuat angka ilustratif bertanda dummy; angka tersebut tidak dipakai sebagai ekspektasi.
2. File B merevisi RQ3 menjadi cost-effectiveness; revisi ini mengalahkan rancangan korelasi karakteristik kode pada File A.
3. Pipeline lokal menjalankan CodaMOSA dan CoverUp; Pynguin dan MuTAP ditangani kolaborator.
4. Populasi CM hanya memiliki delapan stratum tertil non-kosong; penggunaan delapan stratum telah disetujui.
5. B2 sementara menggunakan `auto` yang sama sebagai B1 karena endpoint konfigurasi B2 hanya mengekspos `auto`. Deviasi ini dicatat di docs/protocol.md dan tidak memenuhi dua rambang File B.

## 10. Keterbatasan

- Identitas GPT-5.6 Sol pada endpoint `auto` adalah klaim penjual dan tidak diverifikasi.
- Perbandingan lintas dataset tidak berpasangan karena unit MT dan CM berbeda.
- Hasil final tidak boleh disimpulkan sebelum probe B2, pilot, sanity checks, dan run utama selesai.
- Efek kontaminasi data tetap mungkin karena benchmark bersifat publik.

## 11. Artefak Reproduksi

- `config/experiment.toml`: protokol mesin-baca (tanpa secrets)
- `experiment_control.ipynb`: kontrol dan observasi proses
- `scripts/setup.sh`: setup tunggal
- `scripts/run_experiment.py`: entry point tunggal dan resumable
- `results/module_characteristics.csv`, `results/cm_sample.csv`, `results/*matrix.csv`
- `results/raw/<run_id>/`: request/response teredaksi
- `results/generated/<run_id>/`: generated tests dan logs
- `results/analysis/`: tabel statistik, failure rate, task exclusion, dan deviations
