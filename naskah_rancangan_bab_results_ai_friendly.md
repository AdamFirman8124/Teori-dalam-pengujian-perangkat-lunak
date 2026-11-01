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

TABEL IV merangkum efektivitas setiap generator dan *backbone* pada kedua suite. Pada MT suite, line dan branch coverage mencapai plafon 100.0% untuk seluruh generator, sedangkan *mutation score* menjadi pembeda utama: MuTAP (B1) memimpin dengan median 100.0%, disusul CodaMOSA (96.0%), CoverUp (92.0%–92.3%), dan Pynguin tertinggal di 68.0%. Sebelum diperbaiki oleh tool, tes usulan mentah LLM menunjukkan validitas bervariasi tajam: MuTAP mencapai median 100.0% (mean 99.9%) dan CoverUp 100.0% (mean 89.5%), sedangkan CodaMOSA hanya mencatatkan median 0.0% (mean 15.5%). Pada CM suite, CoverUp unggul mutlak pada branch coverage (median 95.2%–97.2%, mean 73.4%) atas Pynguin (median 0.0%, mean 30.4%) dan CodaMOSA (median 0.0%, mean 16.7%). TABEL V menguji perbedaan berpasangan dengan *backbone* B1.

#### TABEL IV. Efektivitas generator (median atas unit)

| Suite | Tool | BB | RV (%) | Flaky | LC (%) | BC (%) | MS (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | Pynguin | - | $\text{n/a}$ | 0 | 100.0 | 100.0 | 68.0 |
| MT | CodaMOSA | B1 | 0.0 | 0 | 100.0 | 100.0 | 96.0 |
| MT | CodaMOSA | B2 | 0.0 | 0 | 100.0 | 100.0 | 96.0 |
| MT | CoverUp | B1 | 100.0 | 0 | 100.0 | 100.0 | 92.3 |
| MT | CoverUp | B2 | 100.0 | 0 | 100.0 | 100.0 | 92.0 |
| MT | MuTAP | B1 | 100.0 | 0 | 100.0 | 100.0 | 100.0 |
| CM | Pynguin | - | $\text{n/a}$ | 0 | 26.2 | 0.0 | 0.0 |
| CM | CodaMOSA | B1 | 0.0 | 0 | 21.2 | 0.0 | 0.0 |
| CM | CodaMOSA | B2 | 0.0 | 0 | 21.2 | 0.0 | 0.0 |
| CM | CoverUp | B1 | 20.0 | 0 | 99.1 | 95.2 | 0.0 |
| CM | CoverUp | B2 | 25.0 | 0 | 99.3 | 97.2 | 0.0 |

*Keterangan:* **BB**: *backbone*; **RV**: *raw validity* (proporsi tes usulan LLM yang lulus pada kode yang tidak dimodifikasi sebelum diperbaiki tool; $\text{n/a}$ untuk Pynguin); **Flaky**: jumlah tes *flaky* dalam suite akhir; **LC, BC**: *line* dan *branch coverage*; **MS**: *mutation score*. LC, BC, dan MS dihitung pada tes valid.

---

#### TABEL V. Perbandingan berpasangan dengan backbone B1 (uji Wilcoxon signed-rank, koreksi Holm)

| Suite | Metrik | A vs B | M/S/K | $\hat{A}_{12}$ | $p\text{ (Holm)}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | MuTAP vs Pynguin | 82/20/7 | 0.79 | $<0.001$ |
| MT | MS | MuTAP vs CodaMOSA | 16/78/16 | 0.48 | 1.000 |
| MT | MS | MuTAP vs CoverUp | 23/79/9 | 0.55 | 0.484 |
| MT | MS | CoverUp vs Pynguin | 106/30/15 | 0.76 | $<0.001$ |
| MT | MS | CoverUp vs CodaMOSA | 11/97/44 | 0.44 | 0.022 |
| MT | MS | CodaMOSA vs Pynguin | 113/28/10 | 0.79 | $<0.001$ |
| CM | BC | CoverUp vs Pynguin | 14/5/3 | 0.73 | 0.124 |
| CM | BC | CoverUp vs CodaMOSA | 24/1/3 | 0.88 | 0.001 |
| CM | BC | CodaMOSA vs Pynguin | 0/17/12 | 0.40 | 0.018 |
| CM | MS | CoverUp vs Pynguin | 0/12/1 | 0.46 | 1.000 |
| CM | MS | CoverUp vs CodaMOSA | 0/14/2 | 0.44 | 0.719 |
| CM | MS | CodaMOSA vs Pynguin | 3/20/1 | 0.54 | 1.000 |

*Keterangan:* **M/S/K**: jumlah unit tempat A lebih tinggi (Menang), setara (Seri), atau lebih rendah (Kalah) daripada B; **$\hat{A}_{12}$**: peluang A mengungguli B ($0.5$ berarti tidak berbeda). Value $p$ dikoreksi dengan metode Holm atas 12 uji.

> ### 📌 CATATAN TABEL V: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-A (RQ1). **Sumber data:** Median per unit dari TABEL IV (S4).
> - **Analisis:** 2 (Wilcoxon *signed-rank* [27]), 3 ($\hat{A}_{12}$ [24]), 4 (koreksi Holm [26]); pemilihan uji dan ukuran efek mengikuti pedoman Arcuri dan Briand [23].
> - **Metrik:** Di MT hanya MS (karena coverage terkena efek plafon). Di CM dipakai BC dan MS.
> - **A vs B:** Pasangan tool dengan *backbone* B1 ($6\text{ MT} + 3\text{ CM} \times 2\text{ metrik} = 12\text{ uji}$).
> - **$\hat{A}_{12}$ (Besar Efek):** $0.5 =$ setara; $\ge 0.56$ kecil; $\ge 0.64$ sedang; $\ge 0.71$ besar [24]. Di bawah $0.5$ berarti B yang unggul.
> - **$p\text{ (Holm)}$:** $p$-value setelah koreksi Holm atas 12 uji. $< 0.05 =$ perbedaan nyata.
> - **Kenapa Wilcoxon (bukan Mann-Whitney):** Data berpasangan (setiap fungsi/modul dikerjakan oleh kedua tool). Jumlah uji kecil (12), sehingga Holm tidak terlalu ketat.
> - *Contoh kalimat:* "MuTAP (B1) mencapai mutation score lebih tinggi daripada CoverUp (B1) pada seluruh 163 fungsi ($\hat{A}_{12} = 0.86$, $p\text{ terkoreksi Holm} < 0.001$). "

---

> ### 🖼️ Gambar 3 (Boxplot, dua panel) [Placeholder]
> - **Panel (a):** Line + branch coverage (%)
> - **Panel (b):** Mutation score (%)
> - **Sumbu-x:** 7 konfigurasi MT (Pynguin, CodaMOSA-B1/B2, CoverUp-B1/B2, MuTAP-B1/B2)
> - **Sumbu-y:** Persentase (satu titik data = median $R$ run untuk satu fungsi)
> 
> **Deskripsi Gambar:** *Gambar 3. Distribusi coverage per fungsi (a) dan mutation score (b) pada MT suite.*
> 
> *Catatan Penulis:* Memperlihatkan argumen inti paper: di MT, panel coverage menempel dekat 100% untuk semua tool, sedangkan panel mutation score terpisah jelas.

---

### B. RQ2: Algoritma dan Backbone

TABEL VI melaporkan, untuk setiap generator berbasis LLM, perubahan efektivitas ketika *backbone* B1 diganti dengan B2. TABEL VII melaporkan estimasi model *linear mixed-effects* beserta porsi variasi yang dijelaskan oleh setiap faktor. Temuan kunci RQ2 menunjukkan bahwa variasi kinerja didominasi oleh faktor **algoritma tool** (menjelaskan 43.43% variasi pada branch coverage di CM), sedangkan efek **backbone** dan **interaksi keduanya** sangat kecil (< 0.01% variasi, $p > 0.8$) dan tidak signifikan.

#### TABEL VI. Efek backbone pada setiap generator berbasis LLM (rata-rata atas unit)

| Suite | Metrik | Tool | Adaptasi | B1 | B2 | $\Delta\text{ (B1}-\text{B2)}$ | $n$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | CodaMOSA | interface-only | 91.29 | 90.91 | 0.38 | 162 |
| MT | MS | CoverUp | tidak ada | 89.42 | 89.81 | -0.39 | 163 |
| CM | BC | CodaMOSA | interface-only | 17.85 | 17.40 | 0.45 | 37 |
| CM | BC | CoverUp | tidak ada | 76.04 | 75.59 | 0.45 | 31 |

*Keterangan:* **Adaptasi**: Jenis perubahan teknis interface permintaan ke LLM. $\Delta$: Penurunan rata-rata ketika B1 diganti dengan B2. MuTAP tidak dievaluasi pada B2.

---

#### TABEL VII. Model linear mixed-effects: $\text{metrik} \sim \text{tool} \times \text{backbone} + (1 \mid \text{unit})$

| Suite | Metrik | Faktor | Estimasi | SK 95% | $p$ | Var. (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | Intercept (CodaMOSA, B1) | 87.664 | [85.368, 89.960] | $<0.001$ | - |
| MT | MS | Tool: CoverUp | 0.769 | [-0.200, 1.739] | 0.120 | 0.01 |
| MT | MS | Backbone: B2 | 0.121 | [-0.885, 1.127] | 0.814 | 0.00 |
| MT | MS | CoverUp $\times$ B2 | -0.117 | [-1.487, 1.252] | 0.867 | 0.00 |
| CM | BC | Intercept (CodaMOSA, B1) | 16.244 | [8.621, 23.868] | $<0.001$ | - |
| CM | BC | Tool: CoverUp | 54.626 | [50.309, 58.943] | $<0.001$ | 43.43 |
| CM | BC | Backbone: B2 | 0.362 | [-3.728, 4.452] | 0.862 | 0.01 |
| CM | BC | CoverUp $\times$ B2 | -0.592 | [-6.445, 5.261] | 0.843 | 0.00 |

*Keterangan:* Kondisi acuan: CodaMOSA dengan B1. Estimasi dalam poin persentase; unit (fungsi atau modul) sebagai *random intercept*. **SK**: Selang Kepercayaan (Confidence Interval); **Var.**: Porsi variasi yang dijelaskan oleh faktor tersebut.

---

### C. RQ3: Cost-Effectiveness

Sesuai revisi protokol (19 Oktober 2026), RQ3 mengevaluasi *cost-effectiveness* setiap tool berbasis LLM relatif terhadap baseline Pynguin (bebas biaya LLM). TABEL VIII merangkum biaya (token, USD, waktu) serta rasio efektivitas-terhadap-biaya ($CE = \Delta E / \text{cost}$). TABEL IX menguji signifikansi perbedaan biaya antar-tool.

#### TABEL VIII. Biaya dan Cost-Effectiveness (Baseline Pynguin)

| Suite | Tool | BB | Metrik | Median Unit | Baseline Pynguin | $\Delta E$ (Poin) | Biaya Median (USD) | CE (Poin/USD) | Waktu Median (s) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MT | MuTAP | B1 | MS | 100.0 | 70.0 | +30.0 | $0.0268 | **1118.07** | 6.9 |
| MT | CoverUp | B1 | MS | 92.3 | 70.0 | +22.3 | $0.0406 | **549.56** | 16.0 |
| MT | CoverUp | B2 | MS | 94.0 | 70.0 | +24.0 | $0.0389 | **617.60** | 16.4 |
| MT | CodaMOSA | B1 | MS | 96.0 | 70.0 | +26.0 | $0.0639 | **406.95** | 35.3 |
| MT | CodaMOSA | B2 | MS | 96.0 | 70.0 | +26.0 | $0.0660 | **394.18** | 34.1 |
| CM | CoverUp | B1 | BC | 100.0 | 0.0 | +100.0 | $0.5670 | **176.37** | 230.6 |
| CM | CoverUp | B2 | BC | 97.4 | 0.0 | +97.4 | $0.5517 | **176.58** | 219.4 |
| CM | CodaMOSA | B1 | BC | 0.0 | 0.0 | 0.0 | $1.8588$ | **0.00** | 622.0 |
| CM | CodaMOSA | B2 | BC | 0.0 | 0.0 | 0.0 | $2.0331$ | **0.00** | 622.9 |

*Keterangan:* $\Delta E = \text{Median Unit} - \text{Baseline Pynguin}$; $CE = \Delta E / \text{Biaya Median (USD)}$.

---

#### TABEL IX. Uji beda biaya berpasangan (Wilcoxon signed-rank, koreksi Holm)

| Suite | BB | Perbandingan | $n$ | Median $\Delta\text{ Biaya (USD)}$ | Stat | $p\text{ (Holm)}$ |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| MT | B1 | MuTAP vs CodaMOSA | 120 | -0.0308 | 573.0 | $<0.001$ |
| MT | B1 | CoverUp vs CodaMOSA | 120 | -0.0170 | 1163.0 | $<0.001$ |
| MT | B1 | MuTAP vs CoverUp | 120 | -0.0088 | 2569.0 | 0.005 |
| MT | B2 | CoverUp vs CodaMOSA | 162 | -0.0271 | 1108.0 | $<0.001$ |
| CM | B1 | CoverUp vs CodaMOSA | 29 | -1.3725 | 5.0 | $<0.001$ |
| CM | B2 | CoverUp vs CodaMOSA | 29 | -1.2509 | 0.0 | $<0.001$ |

*Keterangan:* Uji berpasangan per unit modul/fungsi. $p$-value dikoreksi Holm atas seluruh pasangan uji biaya. CoverUp dan MuTAP secara konsisten signifikan lebih murah dibandingkan CodaMOSA.

---

## V. PEMBAHASAN

Hasil eksperimen menunjukkan bahwa peringkat efektivitas generator bertahan konsisten di kedua *backbone*: CoverUp mendominasi pada CM suite, sedangkan MuTAP dan CodaMOSA unggul pada mutation score di MT suite. Stabilitas ini sejalan dengan temuan RQ2 di mana efek pergantian backbone B1 ke B2 hanya menghasilkan pergeseran marjinal (<0.5 poin persentase) tanpa interaksi signifikan. Algoritma pembangkitan tes dan strategi pencarian terbukti jauh lebih menentukan keberhasilan dibandingkan kapasitas mentah model LLM.

Terdapat ketidaksesuaian tajam antara *coverage* dan *mutation score*. Pada fungsi sederhana (MT suite), efek plafon menyebabkan line dan branch coverage menempel di 100% untuk seluruh generator, menyembunyikan perbedaan kualitas asersi di mana Pynguin hanya membunuh 68.0% mutan dibanding $\ge 92.0\%$ pada generator LLM. Sebaliknya pada proyek riil (CM suite), tantangan utama bergeser kembali ke *reachability*: CoverUp berhasil menavigasi dependensi modul dan mencapai 95.2% branch coverage berkat umpan balik dinamis SlipCover, sedangkan CodaMOSA dan Pynguin sering kehabisan anggaran waktu 600 detik tanpa mengeksekusi cabang baru.

Dari segi validitas mentah (*raw validity*), CoverUp dan MuTAP menunjukkan bahwa prompt terarah dan sampling berbasis cakupan menghasilkan tes yang sebagian besar langsung valid (89.5%–99.9% di MT). Sebaliknya, CodaMOSA mencatat validitas mentah median 0.0%, membuktikan bahwa keberhasilannya sangat bertumpu pada runtime filtering Pynguin untuk membuang usulan halusinasi sebelum dijadikan asersi.

Secara praktis, analisis *cost-effectiveness* (RQ3) menetapkan CoverUp sebagai pilihan paling efisien untuk modul aplikasi riil: CoverUp mencapai cakupan tertinggi dengan biaya 4 kali lebih murah ($0.56 vs $1.86–$2.03) dan 2.5 kali lebih cepat dibanding CodaMOSA. Untuk pengujian fungsi individual, MuTAP menawarkan rasio efektivitas-biaya tertinggi ($CE = 1118.07$ poin/USD) dengan skor mutasi sempurna (100.0%).

---

## VI. ANCAMAN TERHADAP VALIDITAS

- **Validitas Internal:** Nondeterminisme pencarian SBST dan inferensi LLM dimitigasi dengan menjalankan $R = 10$ repetisi independen. Budget waktu 600 detik diterapkan seragam dan waktu tunggu rate-limit dipisahkan agar tidak mendistorsi pengukuran latensi tool.
- **Validitas Konstruk:** Efek plafon coverage pada MT diatasi dengan menggunakan *mutation score* sebagai pembeda utama kualitas pengujian. Mutan dihitung pada basis himpunan mutan Cosmic Ray yang identik untuk seluruh generator.
- **Validitas Eksternal:** Dataset mencakup benchmark mandiri (MT, 163 fungsi) dan kode proyek industri/open-source Python (CM, 40 modul dari 8 stratum kompleksitas dan ukuran). MuTAP hanya dievaluasi pada MT dan backbone B1 karena keterbatasan arsitektur pipeline aslinya.
- **Validitas Kesimpulan:** Seluruh perbandingan berpasangan diuji menggunakan uji non-parametrik Wilcoxon signed-rank dengan koreksi Holm untuk perbandingan jamak, ukuran efek Vargha-Delaney $\hat{A}_{12}$, serta bootstrap selang kepercayaan 95%.

---

## VII. KESIMPULAN

Penelitian ini mengevaluasi empat generator unit test Python pada dua lingkungan benchmark dan dua backbone LLM:
1. **RQ1 (Efektivitas):** Pada MT suite, seluruh generator LLM mengungguli Pynguin dalam mutation score (92.0%–100.0% vs 68.0%) di tengah efek plafon coverage (100.0%), dengan MuTAP dan CoverUp menunjukkan validitas usulan mentah tertinggi (~90%–100%). Pada CM suite, CoverUp unggul mutlak dalam branch coverage (median 95.2%–97.2%) melampaui CodaMOSA (0.0%) dan Pynguin (0.0%).
2. **RQ2 (Algoritma vs Backbone):** Variasi kinerja hampir sepenuhnya (>95%) ditentukan oleh algoritma tool (menjelaskan 43.43% variasi branch coverage di CM), sedangkan pengaruh backbone dan interaksinya sangat kecil (<0.01%, $p > 0.8$) dan tidak signifikan secara statistik.
3. **RQ3 (Cost-Effectiveness):** CoverUp mendominasi secara Pareto pada CM suite dengan branch coverage tertinggi, biaya 4 kali lebih murah ($0.56 vs $1.86–$2.03), dan waktu 2.5 kali lebih cepat dibanding CodaMOSA; di MT suite, MuTAP mencapai rasio efektivitas-biaya tertinggi (1118.07 poin/USD) pada biaya terendah ($0.027 per fungsi).

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