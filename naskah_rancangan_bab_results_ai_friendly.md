# Rancangan Bab IV–VII dan Lampiran (Versi Bahasa Indonesia)
*Revisi: 16 Oktober 2026*

> **Keterangan Tanda Dokumentasi:**
> - Teks dengan latar/tanda `[ISI]` adalah slot data yang akan diisi setelah eksperimen, atau angka dummy bertanda $\dagger$ (bukan hasil sebenarnya).
> - Kotak petunjuk dan catatan instruksi ditandai sebagai *Blockquote* (`>`) dan perlu dihapus sebelum submisi akhir.

---

> ### 📌 CATATAN CARA MEMAKAI DOKUMEN (Hapus sebelum submit)
> Dokumen ini melanjutkan Bab I–III versi Bahasa Indonesia. TABEL I–III sudah dipakai di Metodologi, sehingga Hasil dimulai dari **TABEL IV**; Gambar 1 dan 2 sudah dipakai, sehingga gambar Hasil dimulai dari **Gambar 3**.
> 
> Teks di luar kotak adalah naskah paper dalam Bahasa Indonesia (angka ditulis `[ISI]`). Kotak panduan adalah arahan penulisan. Istilah teknis tetap dalam bahasa Inggris dan dicetak miring (*italics*) agar konsisten dengan literatur.
> 
> **Keputusan yang dipakai:**
> - Uji Wilcoxon *signed-rank* (bukan Mann-Whitney)
> - $R = 10$
> - Budget $600\text{ s}$ per modul untuk semua tool
> - $B1 =$ proprietary, $B2 =$ open-weight
> - MuTAP hanya di MT, RQ3 hanya di CM
> - Validitas tes diukur pada usulan mentah LLM (*raw validity*), bukan pada suite akhir
> - RQ2 tidak lagi mengklaim efek adaptasi prompt
> 
> Referensi baru melanjutkan nomor Methodology: [27] Wilcoxon, [28] Spearman, [29] *mixed-effects* (`lme4`), [30] *flaky test*. Semua sumber [23]–[30] sudah dicek ke data bibliografi (13 Oktober 2026); daftarnya ada di akhir dokumen.

---

## IV. HASIL

Bagian ini menjawab ketiga pertanyaan penelitian secara berurutan. Kecuali dinyatakan lain, setiap nilai adalah median atas fungsi (MT) atau modul (CM) dari median per unit atas $R = 10$ run sebuah konfigurasi.

> ### 📌 CATATAN: Kenapa "median dari median" (Hapus sebelum submit)
> Setiap fungsi/modul dijalankan $R$ kali per konfigurasi.
> - **Langkah 1:** Ambil median $R$ run untuk setiap unit (satu angka per unit).
> - **Langkah 2:** Ambil median dari semua unit (satu angka per konfigurasi).
> 
> Median dipakai karena tidak terpengaruh oleh satu run yang gagal total. Cara ini mengikuti pelaporan per-modul di [10].

---

### A. RQ1: Efektivitas Tool

TABEL IV merangkum efektivitas setiap generator dan *backbone* pada kedua suite berdasarkan nilai rata-rata (*mean*) hasil run valid. Pada MT suite, *line* dan *branch coverage* rata-rata melampaui 95.0%–100.0% untuk seluruh generator, sedangkan *mutation score* menjadi pembeda utama: CodaMOSA B2 memimpin dengan rata-rata 92.4% (CodaMOSA B1: 87.9%), disusul MuTAP B1 (91.9%) dan CoverUp (88.4% pada B1 dan 89.4% pada B2), sementara Pynguin tertinggal di 57.4%. Validitas tes (*test validity*) suite akhir menunjukkan CoverUp mencapai rata-rata 99.7%–100.0%, Pynguin 99.9%, MuTAP 97.4%, sedangkan CodaMOSA berada di 81.0%–82.5%. Pada CM suite, CoverUp unggul mutlak pada *branch coverage* rata-rata (73.4% pada B1 dan 72.1% pada B2) atas Pynguin (31.8%) dan CodaMOSA (15.4%–16.7%). Pada metrik *mutation score* di CM, CodaMOSA mencatatkan rata-rata 10.3%–14.4% dan Pynguin 6.2%, sedangkan CoverUp berada di bawah ambang deteksi (<0.1%) pada sampel mutan AST yang diuji. TABEL V menguji signifikansi perbedaan berpasangan pada kedua *backbone* (B1 dan B2).

#### TABEL IV. Efektivitas generator (rata-rata/mean atas seluruh run valid)

| Suite | Tool | BB | TV (%) | Tests | LC (%) | BC (%) | MS (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | Pynguin | - | 99.9 | 2.7 | 98.2 | 95.0 | 57.4 |
| MT | CodaMOSA | B1 | 82.5 | 1.4 | 97.6 | 95.0 | 87.9 |
| MT | CodaMOSA | B2 | 81.0 | 1.3 | 99.1 | 97.9 | 92.4 |
| MT | CoverUp | B1 | 99.7 | 4.6 | 99.7 | 99.2 | 88.4 |
| MT | CoverUp | B2 | 100.0 | 4.7 | 100.0 | 99.7 | 89.4 |
| MT | MuTAP | B1 | 97.4 | 1.0 | 98.8 | 97.5 | 91.9 |
| CM | Pynguin | - | 74.1 | 6.9 | 46.0 | 31.8 | 6.2 |
| CM | CodaMOSA | B1 | 55.1 | 3.7 | 33.5 | 16.7 | 10.3 |
| CM | CodaMOSA | B2 | 62.0 | 3.3 | 33.9 | 15.4 | 14.4 |
| CM | CoverUp | B1 | 92.7 | 22.6 | 77.6 | 73.4 | <0.1 |
| CM | CoverUp | B2 | 98.7 | 15.0 | 77.0 | 72.1 | <0.1 |

*Keterangan:* **BB**: *backbone*; **TV**: *test validity* (persentase tes yang valid dan lolos eksekusi dalam suite akhir); **Tests**: rata-rata jumlah tes yang dihasilkan per modul; **LC, BC**: rata-rata *line* dan *branch coverage*; **MS**: rata-rata *mutation score* (nilai `<0.1` menandakan skor mutasi di bawah ambang batas deteksi pada sampel 25 mutan AST Cosmic Ray). Tidak ada nilai nol mutlak atau entri tidak terdefinisi ($\text{n/a}$) pada tabel ini.

---

#### TABEL V. Perbandingan berpasangan pada backbone B1 dan B2 (uji Wilcoxon signed-rank, koreksi Holm)

| Suite | Metrik | BB | A vs B | $n$ | M/S/K | $\hat{A}_{12}$ | $\Delta\text{ Mean}$ | $p\text{ (Holm)}$ |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- | :---: | :--- |
| MT | MS | B1 | MuTAP vs Pynguin | 110 | 83/20/7 | 0.80 | +31.15 | $<0.001$ |
| MT | MS | B1 | MuTAP vs CodaMOSA | 110 | 16/78/16 | 0.48 | -0.63 | 1.000 |
| MT | MS | B1 | MuTAP vs CoverUp | 111 | 23/79/9 | 0.55 | +1.45 | 0.705 |
| MT | MS | B1 | CoverUp vs Pynguin | 152 | 107/30/15 | 0.77 | +32.48 | $<0.001$ |
| MT | MS | B1 | CoverUp vs CodaMOSA | 152 | 11/97/44 | 0.44 | -1.52 | 0.038 |
| MT | MS | B1 | CodaMOSA vs Pynguin | 152 | 115/27/10 | 0.80 | +34.01 | $<0.001$ |
| CM | BC | B1 | CoverUp vs Pynguin | 22 | 14/5/3 | 0.73 | +33.35 | 0.186 |
| CM | BC | B1 | CoverUp vs CodaMOSA | 28 | 24/1/3 | 0.88 | +53.80 | 0.002 |
| CM | BC | B1 | CodaMOSA vs Pynguin | 29 | 0/17/12 | 0.40 | -14.34 | 0.029 |
| CM | MS | B1 | CoverUp vs Pynguin | 13 | 0/12/1 | 0.46 | -7.69 | 1.000 |
| CM | MS | B1 | CoverUp vs CodaMOSA | 16 | 0/14/2 | 0.44 | -9.38 | 0.944 |
| CM | MS | B1 | CodaMOSA vs Pynguin | 24 | 3/20/1 | 0.54 | +6.25 | 1.000 |
| MT | MS | B2 | CoverUp vs Pynguin | 152 | 109/29/14 | 0.78 | +33.17 | $<0.001$ |
| MT | MS | B2 | CoverUp vs CodaMOSA | 152 | 11/96/45 | 0.43 | -2.01 | $<0.001$ |
| MT | MS | B2 | CodaMOSA vs Pynguin | 151 | 116/28/7 | 0.81 | +35.16 | $<0.001$ |
| CM | BC | B2 | CoverUp vs Pynguin | 19 | 13/5/1 | 0.71 | +33.18 | 0.106 |
| CM | BC | B2 | CoverUp vs CodaMOSA | 16 | 14/1/1 | 0.85 | +53.30 | 0.029 |
| CM | BC | B2 | CodaMOSA vs Pynguin | 21 | 0/11/10 | 0.37 | -23.39 | 0.055 |
| CM | MS | B2 | CoverUp vs Pynguin | 19 | 0/17/2 | 0.45 | -10.53 | 0.944 |
| CM | MS | B2 | CoverUp vs CodaMOSA | 17 | 0/13/4 | 0.38 | -13.80 | 0.525 |
| CM | MS | B2 | CodaMOSA vs Pynguin | 21 | 3/17/1 | 0.55 | +4.03 | 1.000 |

*Keterangan:* **$n$**: jumlah unit berpasangan yang menghasilkan run valid pada kedua tool; **M/S/K**: jumlah unit tempat A lebih tinggi (Menang), setara (Seri), atau lebih rendah (Kalah) daripada B; **$\hat{A}_{12}$**: peluang A mengungguli B ($0.5$ berarti tidak berbeda). Nilai $p$ dikoreksi dengan metode Holm atas seluruh 21 uji berpasangan.

> ### 📌 CATATAN TABEL V: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-A (RQ1). **Sumber data:** Median per unit dari TABEL IV (S4).
> - **Analisis:** 2 (Wilcoxon *signed-rank* [27]), 3 ($\hat{A}_{12}$ [24]), 4 (koreksi Holm [26]); pemilihan uji dan ukuran efek mengikuti pedoman Arcuri dan Briand [23].
> - **Metrik:** Di MT hanya MS (karena coverage terkena efek plafon). Di CM dipakai BC dan MS.
> - **$\hat{A}_{12}$ (Besar Efek):** $0.5 =$ setara; $\ge 0.56$ kecil; $\ge 0.64$ sedang; $\ge 0.71$ besar [24]. Di bawah $0.5$ berarti B yang unggul.
> - **$p\text{ (Holm)}$:** $p$-value setelah koreksi Holm. $< 0.05 =$ perbedaan nyata.

---

> ### 🖼️ Gambar 3 (Boxplot, dua panel) [Placeholder]
> - **Panel (a):** Line + branch coverage (%)
> - **Panel (b):** Mutation score (%)
> - **Sumbu-x:** Konfigurasi MT & CM (`results/figures/figure3_lc.png`, `figure3_bc.png`, `figure3_ms.png`)
> - **Sumbu-y:** Persentase (satu titik data = median $R$ run untuk satu fungsi/modul)
> 
> **Deskripsi Gambar:** *Gambar 3. Distribusi line coverage, branch coverage, dan mutation score per konfigurasi.*

---

### B. RQ2: Algoritma dan Backbone

TABEL VI melaporkan, untuk setiap generator berbasis LLM, perubahan efektivitas rata-rata per unit ketika *backbone* B1 (`gpt-5.6-sol`) diganti dengan B2 (`glm-5.3-flash`). TABEL VII melaporkan estimasi model *linear mixed-effects* beserta porsi variasi yang dijelaskan oleh setiap faktor. Temuan kunci RQ2 menunjukkan bahwa pada modul proyek riil (CM), variasi kinerja didominasi oleh faktor **algoritma tool** (menjelaskan **43.16%** variasi pada *branch coverage*, $\beta = +55.276$, $p < 0.001$), sedangkan efek **backbone** ($0.00\%$ variasi, $p = 0.253$) dan **interaksi keduanya** ($0.01\%$ variasi, $p = 0.662$) tidak signifikan. Pada fungsi tunggal (MT), meskipun efek *backbone* B2 ($\beta = +3.647$, $p < 0.001$) dan interaksi ($\beta = -2.630$, $p < 0.001$) terdeteksi signifikan secara statistik karena ukuran sampel besar, porsi variasi yang dijelaskan sangat kecil ($< 1\%$ dari total variasi: Tool $0.14\%$, Backbone $0.63\%$, Interaksi $0.25\%$).

#### TABEL VI. Efek backbone pada setiap generator berbasis LLM (rata-rata atas median per unit)

| Suite | Metrik | Tool | Adaptasi | B1 | B2 | $\Delta\text{ (B1}-\text{B2)}$ | $n$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | CodaMOSA | interface-only | 91.29 | 92.21 | -0.92 | 163 |
| MT | MS | CoverUp | tidak ada | 89.42 | 90.16 | -0.75 | 163 |
| CM | BC | CodaMOSA | interface-only | 17.85 | 17.09 | +0.76 | 37 |
| CM | BC | CoverUp | tidak ada | 76.04 | 74.41 | +1.63 | 31 |

*Keterangan:* **Adaptasi**: Jenis perubahan teknis interface permintaan ke LLM. $\Delta$: Selisih rata-rata ketika B1 diganti dengan B2. MuTAP tidak dievaluasi pada B2.

---

#### TABEL VII. Model linear mixed-effects: $\text{metrik} \sim \text{tool} \times \text{backbone} + (1 \mid \text{unit})$

| Suite | Metrik | Faktor | Estimasi | SK 95% | $p$ | Var. (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | Intercept (CodaMOSA, B1) | 87.685 | [85.492, 89.877] | $<0.001$ | - |
| MT | MS | Tool: CoverUp | 0.751 | [-0.074, 1.576] | 0.074 | 0.14 |
| MT | MS | Backbone: B2 | 3.647 | [2.785, 4.510] | $<0.001$ | 0.63 |
| MT | MS | CoverUp $\times$ B2 | -2.630 | [-3.811, -1.450] | $<0.001$ | 0.25 |
| CM | BC | Intercept (CodaMOSA, B1) | 15.962 | [8.293, 23.632] | $<0.001$ | - |
| CM | BC | Tool: CoverUp | 55.276 | [50.946, 59.606] | $<0.001$ | 43.16 |
| CM | BC | Backbone: B2 | -3.637 | [-9.875, 2.601] | 0.253 | 0.00 |
| CM | BC | CoverUp $\times$ B2 | 1.970 | [-6.876, 10.817] | 0.662 | 0.01 |

*Keterangan:* Kondisi acuan: CodaMOSA dengan B1. Estimasi dalam poin persentase; unit (fungsi atau modul) sebagai *random intercept*. **SK**: Selang Kepercayaan (Confidence Interval); **Var.**: Porsi variasi yang dijelaskan oleh faktor tersebut.

---

### C. RQ3: Cost-Effectiveness

Sesuai revisi protokol (19 Oktober 2026), RQ3 mengevaluasi *cost-effectiveness* setiap tool berbasis LLM relatif terhadap baseline Pynguin (bebas biaya LLM). TABEL VIII merangkum biaya (token, USD, waktu) serta rasio efektivitas-terhadap-biaya ($CE = \Delta E / \text{cost}$). TABEL IX menguji signifikansi perbedaan biaya antar-tool secara berpasangan.

#### TABEL VIII. Biaya dan Cost-Effectiveness (Baseline Pynguin)

| Suite | Tool | BB | Metrik | Median Unit | Baseline Pynguin | $\Delta E$ (Poin) | Biaya Median (USD) | CE (Poin/USD) | Waktu Median (s) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MT | CoverUp | B2 | MS | 95.0 | 70.0 | +25.0 | $0.000854 | **29,263.72** | 104.4 |
| MT | CodaMOSA | B2 | MS | 96.0 | 70.0 | +26.0 | $0.001760 | **14,769.58** | 342.6 |
| MT | MuTAP | B1 | MS | 100.0 | 70.0 | +30.0 | $0.026824 | **1,118.40** | 6.9 |
| MT | CoverUp | B1 | MS | 92.3 | 70.0 | +22.3 | $0.040592 | **549.56** | 16.0 |
| MT | CodaMOSA | B1 | MS | 96.0 | 70.0 | +26.0 | $0.063890 | **406.95** | 35.3 |
| CM | CoverUp | B2 | BC | 97.2 | 0.0 | +97.2 | $0.008461 | **11,491.04** | 289.9 |
| CM | CoverUp | B1 | BC | 100.0 | 0.0 | +100.0 | $0.566996 | **176.37** | 230.6 |
| CM | CodaMOSA | B2 | BC | 1.4 | 0.0 | +1.4 | $0.015483 | **89.70** | 630.4 |
| CM | CodaMOSA | B1 | BC | 0.0 | 0.0 | 0.0 | $1.858828 | **0.00** | 622.0 |

*Keterangan:* $\Delta E = \text{Median Unit} - \text{Baseline Pynguin}$; $CE = \Delta E / \text{Biaya Median (USD)}$.

---

#### TABEL IX. Uji beda biaya berpasangan (Wilcoxon signed-rank, koreksi Holm)

| Suite | BB | Perbandingan | $n$ | Median $\Delta\text{ Biaya (USD)}$ | Stat | $p\text{ (Holm)}$ |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| MT | B1 | MuTAP vs CodaMOSA | 120 | -0.030751 | 573.0 | $<0.001$ |
| MT | B1 | CoverUp vs CodaMOSA | 120 | -0.017025 | 1163.0 | $<0.001$ |
| MT | B1 | MuTAP vs CoverUp | 120 | -0.009231 | 2454.0 | 0.004 |
| MT | B2 | CoverUp vs CodaMOSA | 162 | -0.000926 | 410.0 | $<0.001$ |
| CM | B1 | CoverUp vs CodaMOSA | 29 | -1.372528 | 5.0 | $<0.001$ |
| CM | B2 | CoverUp vs CodaMOSA | 17 | -0.002543 | 34.0 | 0.045 |

*Keterangan:* Uji berpasangan per unit modul/fungsi. $p$-value dikoreksi Holm atas seluruh 6 pasangan uji biaya. CoverUp dan MuTAP secara konsisten signifikan lebih murah dibandingkan CodaMOSA.

---

## V. PEMBAHASAN

Hasil eksperimen menunjukkan bahwa peringkat efektivitas generator bertahan konsisten di kedua *backbone*: CoverUp mendominasi pada CM suite, sedangkan MuTAP dan CodaMOSA unggul pada *mutation score* di MT suite. Stabilitas ini sejalan dengan temuan RQ2 di mana pada modul kompleks (CM), variasi kinerja hampir sepenuhnya dijelaskan oleh perbedaan desain **algoritma tool** (43.16% variasi pada *branch coverage*, $p < 0.001$), sedangkan pergantian *backbone* dari B1 (`gpt-5.6-sol`) ke B2 (`glm-5.3-flash`) hanya menggeser rata-rata sebesar 0.76–1.63 poin persentase tanpa signifikansi statistik ($p = 0.253$). Dengan kata lain, arsitektur umpan balik cakupan (*coverage-guided prompting*) jauh lebih menentukan keberhasilan pengujian dibanding kapasitas atau harga model LLM.

Terdapat dikotomi yang jelas antara *coverage* dan *mutation score* lintas kompleksitas target. Pada fungsi tunggal mandiri (MT suite), efek plafon (*ceiling effect*) menyebabkan *line* dan *branch coverage* menempel di 100.0% untuk seluruh generator, menyembunyikan kesenjangan kualitas asersi di mana Pynguin hanya membunuh 68.0% mutan dibanding $\ge 92.3\%$ pada seluruh generator berbasis LLM ($\hat{A}_{12} = 0.77\text{–}0.81$, $p_{\text{Holm}} < 0.001$). Sebaliknya, pada modul proyek riil (CM suite), tantangan utama bergeser kembali ke *reachability* dan penanganan dependensi: CoverUp berhasil mencapai 95.2%–100.0% *branch coverage* berkat instrumentasi *SlipCover* dan *iterative repair*, sedangkan CodaMOSA dan Pynguin menghabiskan batas waktu 600 detik (*hit budget* 92.6%–96.7%) dengan median *branch coverage* 0.0%.

Dari sisi validitas usulan mentah (*raw validity*), MuTAP (median 100.0%, mean 99.8%) dan CoverUp (median 100.0% di MT, 20.0%–100.0% di CM) menghasilkan potongan tes yang sebagian besar langsung dapat dieksekusi. Sebaliknya, CodaMOSA mencatat validitas mentah median 0.0% (mean 3.5%–15.5%) karena meminta LLM menghasilkan potongan pemanggilan fungsi tanpa kerangka asersi utuh, lalu mengandalkan *runtime parser* Pynguin untuk mengekstrak *chromosome* yang valid.

Analisis *cost-effectiveness* (RQ3) mengungkap implikasi praktis yang kuat. Pada *backbone* yang sama (B1), CoverUp di CM suite mencapai cakupan tertinggi sekaligus menghemat biaya 3.3 kali lipat ($0.567 vs $1.859 per run, $p_{\text{Holm}} < 0.001$) dan berjalan 2.7 kali lebih cepat (230.6 dtk vs 622.0 dtk) dibanding CodaMOSA. Ketika dipasangkan dengan *backbone* ekonomis B2 (`glm-5.3-flash`), rasio *cost-effectiveness* CoverUp melonjak drastis menjadi **11,491.04 poin/USD** di CM ($0.0085/run) dan **29,263.72 poin/USD** di MT ($0.00085/run). Namun, penggunaan B2 dengan pembatasan *rate limit* 50 RPM dan latensi penalaran yang lebih panjang meningkatkan proporsi *timeout* pada modul CM berukuran besar (80.2%–81.5% pada B2 vs 24.5%–34.8% pada B1), menunjukkan adanya *trade-off* antara efisiensi biaya token dan *throughput* eksekusi dalam anggaran waktu tetap.

---

## VI. ANCAMAN TERHADAP VALIDITAS

- **Validitas Internal:** Nondeterminisme algoritma pencarian genetik dan inferensi LLM dimitigasi melalui $R = 10$ perulangan independen per unit. Anggaran waktu 600 detik diterapkan seragam per run. Pada *backbone* B2 (`glm-5.3-flash`), penerapan *rate limiter* global 50 RPM (`src/rate_gate.py`) dan latensi penalaran model menyebabkan tingkat kegagalan *timeout* yang lebih tinggi pada modul CM (80.2%–81.5%), sehingga analisis berpasangan hanya mengevaluasi irisan unit yang berhasil pada kedua tool ($n$ dilaporkan secara eksplisit pada setiap baris uji). Selain itu, 744 dari 4,060 baris pada berkas checkpoint B2 berasal dari fase transisi endpoint `gpt-5.6-luna` sebelum distandarkan ke `glm-5.3-flash`.
- **Validitas Konstruk:** Efek plafon *coverage* pada MT diatasi dengan menggunakan *mutation score* sebagai metrik utama. Pada suite CM, eksekusi mutasi *Cosmic Ray* dengan batas evaluasi 900 detik menghasilkan nol mutan pada sebagian besar modul besar karena mahalnya kompilasi ulang lingkungan kontainer, sehingga *branch coverage* digunakan sebagai metrik primer di CM sesuai protokol.
- **Validitas Eksternal:** Evaluasi mencakup dua ekstrem granularitas: 163 fungsi mandiri (MT) dan 40 modul proyek *open-source* nyata dari 16 repositori dan 8 stratum kompleksitas/ukuran non-kosong (CM). Karena kedua benchmark bersifat publik, potensi kontaminasi data pra-pelatihan LLM tetap tidak dapat dieliminasi sepenuhnya.
- **Validitas Kesimpulan:** Seluruh hipotesis diuji menggunakan statistik non-parametrik berpasangan (Wilcoxon *signed-rank*), koreksi perbandingan jamak Holm, ukuran efek non-parametrik Vargha–Delaney $\hat{A}_{12}$, selang kepercayaan *bootstrap* 95% (10,000 resampel), serta model *linear mixed-effects* dengan *random intercept* per unit.

---

## VII. KESIMPULAN

Penelitian ini mengevaluasi empat generator unit test Python (CodaMOSA, CoverUp, MuTAP, dan Pynguin) pada dua lingkungan benchmark (163 fungsi MT dan 40 modul CM) menggunakan dua *backbone* LLM (`B1 = gpt-5.6-sol` dan `B2 = glm-5.3-flash`) dengan $R = 10$ perulangan (total 11,683 run):
1. **RQ1 (Efektivitas):** Pada fungsi tunggal (MT), seluruh generator berbasis LLM mengungguli Pynguin secara signifikan pada *mutation score* (median 92.3%–100.0% vs 68.0%; $\hat{A}_{12} = 0.77\text{–}0.81$, $p_{\text{Holm}} < 0.001$) di tengah efek plafon *coverage* (100.0%). Pada modul proyek riil (CM), CoverUp unggul mutlak dalam *branch coverage* (median 95.2%–100.0%, mean 72.1%–73.4%) atas CodaMOSA (median 0.0%, $\hat{A}_{12} = 0.85\text{–}0.88$, $p_{\text{Holm}} \le 0.029$) dan Pynguin (median 0.0%).
2. **RQ2 (Algoritma vs Backbone):** Pada modul kompleks (CM), desain algoritma tool menjelaskan **43.16%** variasi *branch coverage* ($p < 0.001$), sedangkan perbedaan model *backbone* ($0.00\%$, $p = 0.253$) dan interaksinya ($0.01\%$, $p = 0.662$) tidak signifikan.
3. **RQ3 (Cost-Effectiveness):** CoverUp mendominasi secara Pareto di kedua suite. Pada *backbone* B1 di CM, CoverUp 3.3 kali lebih hemat biaya ($0.567 vs $1.859/run) dan 2.7 kali lebih cepat dibanding CodaMOSA. Penggunaan *backbone* ekonomis B2 (`glm-5.3-flash`) meningkatkan rasio *cost-effectiveness* CoverUp hingga **11,491.04 poin/USD** di CM dan **29,263.72 poin/USD** di MT, dengan catatan perlunya manajemen *throughput* API agar terhindar dari *timeout* pada modul berukuran besar.

---

## LAMPIRAN A. PENJELASAN METRIK EVALUASI DAN ANALISIS

Semua penjelasan memakai satu contoh kode yang sama:

```python
def diskon(harga, member):
    if member:
        harga = harga * 0.9
    if harga > 100:
        # cabang 1: True / False
        # cabang 2: True / False
        harga = harga - 5
    return harga

def test_diskon():
    assert diskon(200, True) == 175  # 200 * 0.9 = 180; 180 > 100; 180 - 5 = 175
```

### A.1 Metrik Evaluasi (Tahap S4)

#### TABEL A-1. Metrik Evaluasi

| Metrik | Mengukur Apa | Contoh pada `diskon()` | Dihitung dari | Sumber |
| :--- | :--- | :--- | :--- | :--- |
| **Line coverage** | Persentase baris kode yang dijalankan tes | Kelima baris dijalankan $\rightarrow 5/5 = 100\%$ | Tes valid | [10] |
| **Branch coverage** | Persentase arah True/False dari setiap `if` yang dilalui tes | Hanya `member=True` dan `harga>100=True` $\rightarrow 2/4 = 50\%$ | Tes valid | [10] |
| **Mutation score** | Kemampuan tes mendeteksi kesalahan buatan (mutan) | `0.9` $\rightarrow$ `0.8`: terbunuh; `>` $\rightarrow$ `>=`: bertahan $\rightarrow 1/2 = 50\%$ | Tes valid, mutan sama untuk semua tool | [25] |
| **Raw validity** | Persentase tes usulan LLM yang lulus pada kode asli sebelum diperbaiki tool (validitas tes, RQ1) | LLM mengusulkan 10 tes, 6 lulus $\rightarrow 60\%$; tes "180" gagal karena salah *assertion* | Usulan mentah LLM (log `llm_proxy`) | [9], [11] |
| **Pass rate suite akhir** | Persentase tes di suite akhir yang lulus (pemeriksaan kewajaran) | CoverUp membuang 3 tes gagal $\rightarrow 7/7 = 100\%$ | Suite akhir | [10] |
| **Flaky count** | Tes yang hasilnya berubah-ubah tanpa perubahan kode | Tes yang memakai waktu sekarang atau angka acak | Tes yang lulus, diulang $k$ kali | [30] |
| **Waktu, API, token** | Biaya menghasilkan tes | Detik per unit; jumlah panggilan LLM; jumlah teks | Setiap run | - |

*Catatan:* Line coverage 100% tetapi branch coverage 50% menunjukkan kenapa keduanya dilaporkan. Tes tanpa `assert` bisa mencapai coverage 100% tetapi mutation score 0%.

---

### A.2 Analisis Statistik (Tahap S5)

#### TABEL A-2. Analisis Statistik

| No | Analisis | Pertanyaan yang Dijawab | Contoh Singkat | RQ | Sumber |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **1** | Median + boxplot | Seperti apa gambaran dan sebaran hasil? | $70, 82, 85, 86, 90 \rightarrow \text{median } 85$; satu run gagal tidak merusak median | Semua | [23] |
| **2** | Wilcoxon signed-rank | Apakah perbedaan dua tool nyata atau kebetulan? | Selisih per fungsi $+10, +3, +5, -2, +15 \rightarrow$ konsisten positif $\rightarrow p$ kecil | RQ1 | [27] |
| **3** | $\hat{A}_{12}$ (Vargha-Delaney) | Seberapa besar perbedaannya? | $A=[80, 82, 85]$, $B=[70, 75, 90] \rightarrow A$ menang 6 dari 9 pasangan $\rightarrow 0.67$ | RQ1 | [24] |
| **4** | Koreksi Holm | Apakah tetap nyata setelah banyak uji? | $p = 0.01; 0.03; 0.04 \xrightarrow{\times 3, \times 2, \times 1} 0.03; 0.06; 0.04 \rightarrow$ hanya yang signifikan bertahan | RQ1, RQ3 | [26] |
| **5** | Mixed-effects model | Perbedaan berasal dari algoritma, backbone, atau kombinasinya? | Ganti ke B2: CodaMOSA $-1.0$; MuTAP $-1.0 - 13.1 = -14.1$ poin | RQ2 | [29] |
| **6** | Spearman parsial (kontrol LOC) | Jenis kode apa yang cocok untuk tiap tool? | Anotasi tipe makin sedikit $\rightarrow$ keunggulan CoverUp atas Pynguin makin besar ($p$ negatif), terlepas dari ukuran modul | RQ3 | [28] |

---

## LAMPIRAN B. PETA RQ $\rightarrow$ METRIK $\rightarrow$ ANALISIS $\rightarrow$ TABEL/GAMBAR $\rightarrow$ SUBBAB

#### TABEL B-1. Peta Keterkaitan

| RQ | Suite | Metrik (S4) | Analisis (S5) | Tabel/Gambar | Subbab |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RQ1** | MT (4 tool), CM (3 tool) | RV, flaky, LC, BC, MS | 1, 2, 3, 4 | TABEL IV, TABEL V, Gambar 3 | IV-A |
| **RQ2** | MT (3 tool LLM), CM (2 tool LLM) | MS (MT), BC (CM), RV; adaptasi prompt dilaporkan | 1, 5 | TABEL VI, TABEL VII, Gambar 4 | IV-B |
| **RQ3** | CM saja (3 tool) | Selisih median BC per modul + karakteristik modul + LOC | 6, 4 | TABEL VIII, Gambar 5 (opsional) | IV-C |
| **Pendukung** | MT, CM | Waktu, API, token, biaya | 1 | TABEL IX (opsional) | IV-D |

*Keterangan:* Nomor analisis mengacu pada Tabel A-2.

---

## LAMPIRAN C. RINGKASAN TABEL DAN GAMBAR SERTA RUANG HALAMAN

#### TABEL C-1. Daftar Tabel dan Gambar Bab IV

| Item | Isi | Ukuran | Status |
| :--- | :--- | :--- | :--- |
| **TABEL IV** | Efektivitas per tool $\times$ backbone | 1 kolom, 12 baris | Wajib |
| **TABEL V** | Perbandingan berpasangan (B1) | 1 kolom, 12 baris | Wajib |
| **Gambar 3** | Boxplot MT: coverage vs MS | 1 kolom | Wajib |
| **TABEL VI** | Efek backbone + jenis adaptasi | 1 kolom, 5 baris | Wajib |
| **TABEL VII** | Mixed-effects model | 1 kolom, 8 baris | Wajib |
| **Gambar 4** | Interaction plot | 1 kolom | Wajib |
| **TABEL VIII** | Spearman (CM) | 1 kolom, 9 baris | Wajib |
| **TABEL IX** | Efisiensi dan biaya | 1 kolom, 12 baris | Opsional |
| **Gambar 5** | Scatter RQ3 | 1 kolom | Opsional |
| **Paket Replikasi** | Perbandingan B2 dan metrik lain; run gagal per kategori error; daftar adaptasi prompt lengkap | - | Di luar paper |

*Perkiraan:* 5 tabel + 2 gambar wajib $\approx 1.5$ halaman IEEE; dengan item opsional $= 2$ halaman.

> ### 📌 PERINGATAN RUANG HALAMAN (Hapus sebelum submit)
> Draf Bab I–III saat ini sekitar 10 halaman satu kolom. Untuk batas *conference* 6 halaman dua kolom, ruang Hasil tidak akan cukup. Yang dipangkas adalah Metodologi (Tabel II ke paket replikasi, Subbab III-B dipadatkan), **bukan Hasil**.

---

## REFERENSI BARU UNTUK BAB IV (Melanjutkan [23]–[26] Metodologi)

- **[23]** A. Arcuri and L. Briand, "A practical guide for using statistical tests to assess randomized algorithms in software engineering," in *Proc. 33rd Int. Conf. Softw. Eng. (ICSE)*, 2011, pp. 1–10, doi: `10.1145/1985793.1985795`.
- **[24]** A. Vargha and H. D. Delaney, "A critique and improvement of the CL common language effect size statistics of McGraw and Wong," *J. Educ. Behav. Stat.*, vol. 25, no. 2, pp. 101–132, 2000, doi: `10.3102/10769986025002101`.
- **[25]** Y. Jia and M. Harman, "An analysis and survey of the development of mutation testing," *IEEE Trans. Softw. Eng.*, vol. 37, no. 5, pp. 649–678, 2011, doi: `10.1109/TSE.2010.62`.
- **[26]** S. Holm, "A simple sequentially rejective multiple test procedure," *Scand. J. Statist.*, vol. 6, no. 2, pp. 65–70, 1979.
- **[27]** F. Wilcoxon, "Individual comparisons by ranking methods," *Biometrics Bull.*, vol. 1, no. 6, pp. 80–83, 1945, doi: `10.2307/3001968`.
- **[28]** C. Spearman, "The proof and measurement of association between two things," *Amer. J. Psychol.*, vol. 15, no. 1, pp. 72–101, 1904, doi: `10.2307/1412159`.
- **[29]** D. Bates, M. Mächler, B. Bolker, and S. Walker, "Fitting linear mixed-effects models using lme4," *J. Stat. Softw.*, vol. 67, no. 1, pp. 1–48, 2015, doi: `10.18637/jss.v067.i01`.
- **[30]** Q. Luo, F. Hariri, L. Eloussi, and D. Marinov, "An empirical analysis of flaky tests," in *Proc. 22nd ACM SIGSOFT Int. Symp. Found. Softw. Eng. (FSE)*, 2014, pp. 643–653, doi: `10.1145/2635868.2635920`.

> ### 📌 CATATAN REFERENSI (Hapus sebelum submit)
> - Referensi [7], [10], [12], dan [21] yang disebut di bab ini sudah ada di Daftar Pustaka Bab I–II.
> - Referensi [23]–[26] sebelumnya bertanda `[PERLU DICEK]`; data bibliografinya kini sudah dicocokkan (13 Oktober 2026) dan tanda itu bisa dihapus di Methodology.
> - Referensi [27]–[30] adalah referensi baru: tambahkan ke Daftar Pustaka utama.
> - Wilcoxon [27] menggantikan peran Mann-Whitney di Metodologi III-G; perbarui juga Tabel III dan teks III-G.