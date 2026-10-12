# Prompt yang Digunakan dalam Eksperimen (Penjelasan Awam)

Dokumen ini menjelaskan *apa yang sebenarnya diminta* kepada model AI saat
eksperimen berjalan, dalam bahasa sederhana, agar hasil dataset bisa dipahami
tanpa latar belakang teknis.

## Apa yang dilakukan CoverUp?

CoverUp bekerja seperti ini:

1. Ia mengukur berapa banyak baris kode yang sudah dieksekusi oleh test.
2. Ada baris/cabang yang belum tereksekusi ("kode belum tercakup").
3. Ia mengirim potongan kode itu ke LLM sambil meminta: *"buatkan test yang
   mengeksekusi semua bagian yang belum tercakup."*
4. Test dijalankan. Kalau error atau coverage masih kurang, ia kirim lagi ke
   LLM untuk diperbaiki.
5. Loop berhenti bila coverage penuh, atau model menyerah.

Prompt yang dipakai adalah `gpt-v2` (default CoverUp).

## Prompt 1 - Permintaan awal (per potongan kode)

```text
You are an expert Python test-driven developer.
The code below, extracted from {nama_file}, does not achieve full coverage:
when tested, {daftar_baris_dan_cabang_yang_belum_dieksekusi} not execute.
Create new pytest test functions that execute all missing lines and branches, always making
sure that each test is correct and indeed improves coverage.
Use the get_info tool function as necessary.
Always send entire Python test scripts when proposing a new test or correcting one you
previously proposed.
Be sure to include assertions in the test that verify any applicable postconditions.
Please also make VERY SURE to clean up after the test, so as to avoid state pollution;
use 'monkeypatch' or 'pytest-mock' if appropriate.
Write as little top-level code as possible, and in particular do not include any top-level code
calling into pytest.main or the test itself.
Respond ONLY with the Python code enclosed in backticks, without any explanation.
```python
{isi_kode_yang_diuji}
```
```

Arti bebasnya:

- "Kamu adalah pengembang test Python tingkat ahli."
- "Kode ini belum tercakup penuh; baris/cabang tertentu belum dieksekusi."
- "Buat fungsi test pytest yang mengeksekusi semua bagian yang belum tercakup."
- "Pastikan setiap test benar dan benar-benar menambah coverage."
- "Gunakan tool `get_info` bila perlu."
- "Selalu kirim file test lengkap saat mengusulkan/memperbaiki test."
- "Sertakan assertion untuk memeriksa kondisi hasil."
- "Bersihkan state setelah test (monkeypatch/pytest-mock)."
- "Jangan tulis kode top-level yang memanggil pytest.main."
- "Balas HANYA kode Python di dalam backticks."

## Prompt 2 - Saat test menghasilkan error

```text
Executing the test yields an error, shown below.
Modify or rewrite the test to correct it; respond only with the complete Python code in backticks.
Use the get_info tool function as necessary.

{pesan_error_pytest}
```

Arti bebasnya: "Test ini error seperti berikut; perbaiki dan balas kode Python
lengkap dalam backticks."

## Prompt 3 - Saat coverage masih kurang

```text
The tests still lack coverage: {bagian_yang_belum_dieksekusi} not execute.
Modify it to correct that; respond only with the complete Python code in backticks.
Use the get_info tool function as necessary.
```

Arti bebasnya: "Coverage masih kurang di bagian ini; perbaiki dan balas kode
Python lengkap."

## Tool `get_info`

Model boleh memanggil satu tool bernama `get_info`:

> "Returns information about a symbol." - mengembalikan informasi tentang
> fungsi/kelas/metode (mis. `f` untuk fungsi f, `C.foo` untuk metode foo di
> kelas C).

Tujuannya: agar model bisa "mengintip" definisi simbol sebelum menulis test,
sehingga test lebih akurat.

## Mengapa ini penting untuk membaca hasil

- **BLOCKED** = model tidak berhasil menghasilkan test yang valid/berguna untuk
  task itu, walaupun sudah diberi beberapa kali kesempatan lewat Prompt 2 dan 3.
  Ini bisa karena (a) keterbatasan model, atau (b) kendala teknis harness.
- **Model salah paham spesifikasi** adalah penyebab umum BLOCKED - misalnya model
  mengira fungsi A mengembalikan nilai X, padahal sebenarnya Y, sehingga
  assertion-nya selalu gagal.
- Prompt 2 dan 3 membuat CoverUp "mencoba lagi", tetapi jumlah percobaan terbatas;
  setelah habis, task ditandai BLOCKED.
