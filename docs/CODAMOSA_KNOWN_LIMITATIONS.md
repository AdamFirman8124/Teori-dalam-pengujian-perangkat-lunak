# CodaMOSA: Known Limitations dan Mitigasi

Dokumen ini mencatat keterbatasan yang ditemukan saat eksperimen CoverUp + CodaMOSA pada dataset MuTAP, serta mitigasi yang diterapkan di repository ini.

## 1. Output LLM tidak selalu dapat di-deserialize

CodaMOSA meminta model menghasilkan kode test, lalu mengubahnya menjadi objek `TestCase` Pynguin. Model dapat mengembalikan:

- header fungsi tanpa body yang dapat dieksekusi;
- prose atau markdown di sekitar kode;
- placeholder seperti `pass` atau `...`;
- test tanpa assertion;
- kode yang masuk ke file diagnostik `test_script_0_failing.py`, tetapi tidak masuk ke suite utama.

Jika tidak ada `TestCase` yang berhasil dibuat, versi sebelumnya langsung mengembalikan populasi kosong. Akibatnya, tahap evolusi memanggil `randomness.choice([])` dan berhenti dengan `IndexError`.

### Mitigasi yang diterapkan

1. `codamosa/pynguin/analyses/seeding.py` sekarang melakukan retry terbatas ketika tidak ada test case yang berhasil di-parse.
2. Retry menambahkan feedback eksplisit agar model mengembalikan Python executable, tanpa prose, placeholder, atau `try/except` yang menelan kegagalan.
3. Jumlah retry dapat dikonfigurasi dengan:

   ```bash
   export CODAMOSA_LLM_RETRIES=2
   ```

   Nilai `2` berarti maksimal tiga request total: satu request awal dan dua retry. Nilai `0` menonaktifkan retry.
4. `codamosa/pynguin/generation/algorithms/codamosastrategy.py` sekarang memiliki guard untuk populasi seed kosong. Jika semua retry gagal, CodaMOSA melewati targeted evolution dan tidak lagi crash dengan `IndexError`.

### Batas mitigasi

Guard tersebut mencegah crash, tetapi tidak dapat menciptakan test case ketika model tidak menghasilkan kode yang valid. Task yang seluruh seed-nya gagal masih dapat menghasilkan suite kosong atau suite dengan coverage rendah. Status `BLOCKED` akibat empty-population crash seharusnya berkurang, tetapi `INVALID_GENERATED_TEST` tetap mungkin terjadi bila output akhir tidak memenuhi validasi suite.

Retry juga menambah waktu dan biaya pemanggilan model. Karena itu retry dibatasi dan tidak boleh dianggap sebagai jaminan keberhasilan.

## 2. Validasi suite lebih ketat daripada parser CodaMOSA

Pipeline evaluasi menggunakan `src/eval_metrics.py::suite_validity()` untuk menolak suite yang:

- tidak memiliki fungsi `test*`;
- tidak memiliki assertion atau oracle yang dapat dievaluasi;
- menyembunyikan kegagalan dengan broad `except` dan `pass`.

Perbedaan antara parser internal CodaMOSA dan validator evaluasi ini disengaja: test yang hanya terlihat berhasil karena exception ditelan tidak dianggap sebagai test valid untuk metrik eksperimen.

## 3. Mutation score `0.0%` pada suite bergaya import (SUDAH DIPERBAIKI)

Pada run `20261010T164023Z_manual`, mutation score terbaca `0.0%` karena seluruh mutan dicatat sebagai `survived`:

```text
killed: 0
survived: N
mutation score: 0.0%
```

### Root cause

`src/eval_metrics.py::mutation_score_of()` menjalankan mutan pada suite bergaya *import* (CoverUp/Pynguin) dengan cara menaruh mutan di `mut_shadow/`, menambahkan `mut_shadow` ke `PYTHONPATH`, dan menjalankan `pytest` dengan `cwd = workdir`.

Masalahnya, `workdir` juga memuat PUT **asli** (`script_<task>.py`). Pytest menyisipkan direktori rootdir/`cwd` ke `sys.path[0]`, sehingga `import script_<task>` selalu menyelesaikan ke PUT asli dan **bukan** ke mutan di `PYTHONPATH`. Karena suite diuji terhadap kode yang benar, semua mutan tampak `survived`.

Bukti reproduksi pada HumanEval task 0 (suite CoverUp, 6 mutan):

```text
# sebelum: shadow via PYTHONPATH, cwd=workdir (PUT asli menang)
mutation_score = 0.0%   (killed 0 / survived 6)

# setelah: pytest dijalankan dari jobdir terisolasi
mutation_score = 83.33% (killed 5 / survived 6)
```

### Perbaikan

`mutation_score_of()` untuk gaya *import* sekarang menjalankan `pytest` dari `jobdir` per-mutan (bukan `workdir`). `jobdir` memuat `mut_shadow/` berisi mutan **dan** salinan file test, sehingga rootdir yang disisipkan pytest tidak memuat PUT asli dan mutan benar-benar menang saat `import`.

Suite bergaya *inline* (MuTAP/Codex/Copilot) tidak terpengaruh: kode mutan dan bagian test digabung ke satu file probe, sehingga sudah benar. Contoh setelah perbaikan pada HumanEval task 6: MuTAP-Codex `100%`, Copilot-FS `75%`.

### Batas

Skor mutasi tetap hanya sekuat mutan yang tersedia di dataset. Jika sebuah dataset tidak menyediakan mutan dan `mut.py` (MutPy) tidak terpasang, `generate_mutants()` mengembalikan daftar kosong dan `mutation_score` bernilai `None`, bukan `0.0%`. Pastikan MutPy tersedia bila ingin menghitung mutasi pada PUT tanpa mutan bawaan.

## 4. CoverUp: transport error 5xx/connection tidak boleh langsung menyerah

Saat smoke test, CoverUp `claude-sonnet-5` HumanEval/0 berakhir `BLOCKED` dengan pesan:

```text
Error: <class 'litellm.exceptions.InternalServerError'>
       InternalServerError: OpenAIException - Connection error.
giving up
```

Padahal request sebelumnya sudah mengembalikan completion valid. Artinya gangguan
jaringan sesaat membuat seluruh segment CoverUp menyerah.

### Root cause

`coverup/src/coverup/llm.py::Chatter._send_request()` hanya menangani
`ServiceUnavailableError`, `RateLimitError`, dan `APITimeoutError`.
`litellm.exceptions.InternalServerError` adalah subclass `openai.APIError`
**tetapi bukan** `APIConnectionError`, sehingga jatuh ke handler generik
`openai.APIError` yang langsung `return None` (menyerah).

### Perbaikan

`_send_request()` sekarang menangani `openai.APIConnectionError`,
`litellm.exceptions.InternalServerError`, dan `openai.InternalServerError`
sebagai transport error yang di-retry dengan exponential backoff terbatas.
Batas retry dikonfigurasi lewat:

```bash
export COVERUP_MAX_TRANSPORT_RETRIES=4   # default; 0 mematikan retry transport
```

Kegagalan kuota (`You exceeded your current quota`), `BadRequestError`, dan
`AuthenticationError` tetap fail-fast. Error `openai.APIError` yang tidak dikenal
juga tetap fail-fast agar bug konfigurasi tidak di-retry tanpa henti.

### Regression test

`tests/test_coverup_retry.py` menguji retry pada `InternalServerError`, batas
percobaan, dan bahwa kuota tidak di-retry.

## 5. Interpretasi hasil eksperimen

Jangan menggabungkan task `OK`, `BLOCKED`, dan `INVALID_GENERATED_TEST` tanpa menyimpan statusnya. Untuk pelaporan RQ:

- gunakan hanya baris yang memenuhi aturan inklusi yang ditetapkan di pipeline;
- laporkan jumlah `n` setelah filtering;
- simpan status kegagalan sebagai konteks reproduksibilitas;
- jangan menganggap suite kosong sebagai pass rate `100%`.

Run terakhir disimpan di:

```text
experiment_results/runs/20261010T164023Z_manual/
experiment_results/report_20261010T164023Z/
```

## 6. Kredensial dan endpoint

File `.env` hanya menyediakan `OCTA_API_KEY` pada konfigurasi saat ini. Runner yang memakai library atau adapter OpenAI-compatible tetap membutuhkan `OPENAI_API_KEY` yang diekspor ke environment, misalnya:

```bash
export OPENAI_API_KEY="$OCTA_API_KEY"
```

Kegagalan autentikasi atau endpoint tidak terjangkau berbeda dari kegagalan parsing yang dibahas di atas. Sebelum mendiagnosis CodaMOSA, periksa log request dan response model terlebih dahulu.

## 7. Rekomendasi menjalankan eksperimen berikutnya

1. Jalankan smoke test pada sedikit task dengan `CODAMOSA_LLM_RETRIES=2`.
2. Periksa `codex_generations.py`, `test_script_*.py`, dan log Docker untuk membedakan output kosong, output tidak ter-parse, dan kegagalan runtime.
3. Pastikan status setiap task tersimpan sebelum menghitung RQ1/RQ2.
4. Verifikasi bahwa `mutation_score` tidak lagi seragam `0.0%` sebelum memakai metrik mutasi sebagai kesimpulan komparatif. Gunakan `EVAL_MUTANT_LIMIT` untuk membatasi jumlah mutan saat smoke test.
5. Naikkan `TASK_LIMIT` hanya setelah retry/guard dan mutation harness tervalidasi.

Patch ini meningkatkan ketahanan pipeline, tetapi tidak menghilangkan ketergantungan CodaMOSA pada kualitas, format, dan konsistensi output LLM.
