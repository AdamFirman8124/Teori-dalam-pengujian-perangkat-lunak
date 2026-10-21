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

Bagian ini menjawab ketiga pertanyaan penelitian secara berurutan. Kecuali dinyatakan lain, setiap nilai adalah median atas fungsi (MT) atau modul (CM) dari median per unit atas $R = [ISI]$ run sebuah konfigurasi.

> ### 📌 CATATAN: Kenapa "median dari median" (Hapus sebelum submit)
> Setiap fungsi/modul dijalankan $R$ kali per konfigurasi.
> - **Langkah 1:** Ambil median $R$ run untuk setiap unit (satu angka per unit).
> - **Langkah 2:** Ambil median dari semua unit (satu angka per konfigurasi).
> 
> Median dipakai karena tidak terpengaruh oleh satu run yang gagal total. Cara ini mengikuti pelaporan per-modul di [10].

---

### A. RQ1: Efektivitas Tool

TABEL IV merangkum efektivitas setiap generator dan *backbone* pada kedua suite. Pada MT suite, coverage mencapai `[ISI]`, sedangkan *mutation score* berkisar dari `[ISI]` sampai `[ISI]`. Sebelum diperbaiki oleh tool, `[ISI]%` tes yang diusulkan LLM valid. Pada CM suite, `[ISI]`. TABEL V menguji perbedaan berpasangan dengan *backbone* B1, dan Gambar 3 menunjukkan distribusinya pada MT suite.

#### TABEL IV. Efektivitas generator (median atas unit)

| Suite | Tool | BB | RV (%) | Flaky | LC (%) | BC (%) | MS (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | Pynguin | - | $\text{n/a}$ | 0 | 95.2 | 93.0 | 53.1 |
| MT | CodaMOSA | B1 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | CodaMOSA | B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | CoverUp | B1 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | CoverUp | B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MuTAP | B1 | 61.3 | 2 | 99.0 | 98.5 | 80.6$\dagger$ |
| MT | MuTAP | B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | Pynguin | - | $\text{n/a}$ | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | CodaMOSA | B1 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | CodaMOSA | B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | CoverUp | B1 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | CoverUp | B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |

*Keterangan:* **BB**: *backbone*; **RV**: *raw validity* (proporsi tes usulan LLM yang lulus pada kode yang tidak dimodifikasi sebelum diperbaiki tool; $\text{n/a}$ untuk Pynguin); **Flaky**: jumlah tes *flaky* dalam suite akhir; **LC, BC**: *line* dan *branch coverage*; **MS**: *mutation score*. LC, BC, dan MS dihitung pada tes valid. *Pass rate* suite akhir dilaporkan di paket replikasi.  
$\dagger$ *Nilai dummy, hanya ilustrasi.*

> ### 📌 CATATAN TABEL IV: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-A (RQ1). **Sumber data:** S3 (status tes) dan S4 (perhitungan metrik) pada Gambar 1.
> - **Analisis:** Analisis 1 (median) deskriptif, belum ada uji signifikansi.
> - **Detail Kolom:**
>   - Pynguin bertanda `-` karena tidak memakai LLM. MuTAP hanya ada di baris MT.
>   - **RV (*raw validity*):** % tes yang diusulkan LLM yang lulus pada kode asli SEBELUM tool memperbaiki/membuangnya. Pynguin tidak punya usulan LLM ($\text{n/a}$).
>   - *Pass rate* suite akhir tidak dipakai di tabel karena hampir pasti 100%: CoverUp hanya menyimpan tes yang lulus [10], MuTAP mengganti nilai harapan yang salah [11], Pynguin/CodaMOSA membuat *assertion* dari keluaran nyata. Preseden ukuran output mentah: CodaMOSA [9] dan MuTAP [11].
>   - **Flaky:** Jumlah tes yang hasilnya berubah-ubah saat dijalankan ulang [30]. Idealnya 0.
>   - **LC/BC:** Coverage dari tes valid (`coverage.py`). Di MT diperkirakan mendekati 100% untuk semua tool (efek plafon [10]).
>   - **MS:** *Mutation score* dari tes valid, dengan himpunan mutan yang sama untuk semua tool [25]. Ini pembeda utama di MT.
> - **Cara membaca:** Bandingkan per kolom, bukan per baris. Tool terbaik di LC belum tentu terbaik di MS. RV yang rendah berarti tool sangat bergantung pada perbaikan internalnya. Signifikansi selisih dilihat di TABEL V.
> - *Contoh kalimat:* "Coverage pada MT suite mendekati plafon untuk semua generator, sedangkan MuTAP (B1) mencapai median mutation score tertinggi (80.6%)."

---

#### TABEL V. Perbandingan berpasangan dengan backbone B1 (uji Wilcoxon signed-rank, koreksi Holm)

| Suite | Metrik | A vs B | M/S/K | $\hat{A}_{12}$ | $p\text{ (Holm)}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | MuTAP vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | MuTAP vs CodaMOSA | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | MuTAP vs CoverUp | 163/0/0 | 0.86$\dagger$ | $<0.001\dagger$ |
| MT | MS | CoverUp vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | CoverUp vs CodaMOSA | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | CodaMOSA vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | CoverUp vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | CoverUp vs CodaMOSA | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | CodaMOSA vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | MS | CoverUp vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | MS | CoverUp vs CodaMOSA | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | MS | CodaMOSA vs Pynguin | `[ISI]` | `[ISI]` | `[ISI]` |

*Keterangan:* **M/S/K**: jumlah unit tempat A lebih tinggi (Menang), setara (Seri), atau lebih rendah (Kalah) daripada B; **$\hat{A}_{12}$**: peluang A mengungguli B ($0.5$ berarti tidak berbeda). Value $p$ dikoreksi dengan metode Holm atas 12 uji.  
$\dagger$ *Nilai dummy.*

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

TABEL VI melaporkan, untuk setiap generator berbasis LLM, perubahan efektivitas ketika *backbone* B1 diganti dengan B2; jenis adaptasi prompt yang dibutuhkan setiap generator dicantumkan sebagai informasi. TABEL VII melaporkan model *mixed-effects* beserta porsi variasi yang dijelaskan setiap faktor, dan Gambar 4 memvisualisasikan interaksinya. `[ISI: kalimat temuan utama, mis. generator mana yang paling sensitif terhadap backbone]`.

#### TABEL VI. Efek backbone pada setiap generator berbasis LLM (rata-rata atas unit)

| Suite | Metrik | Tool | Adaptasi | B1 | B2 | $\Delta\text{ (B1}-\text{B2)}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | CodaMOSA | interface-only | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | CoverUp | tidak ada | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | MuTAP | `[ISI]` | 80.3$\dagger$ | 66.2$\dagger$ | 14.1$\dagger$ |
| CM | BC | CodaMOSA | interface-only | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | CoverUp | tidak ada | `[ISI]` | `[ISI]` | `[ISI]` |

*Keterangan:* **Adaptasi**: Jenis perubahan yang diperlukan agar generator dapat dijalankan dengan *backbone* masa kini (Bagian III-C). $\Delta$: Penurunan ketika B1 diganti dengan B2.  
$\dagger$ *Nilai dummy.*

> ### 📌 CATATAN TABEL VI: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-B (RQ2). **Sumber data:** S4 + catatan adaptasi prompt dari S2 (`docs/prompt_adaptations.md`).
> - **Adaptation:** 
>   - *interface-only*: Hanya format permintaan yang diubah (CodaMOSA: payload completions $\rightarrow$ chat).
>   - *none*: Cukup ganti konfigurasi (CoverUp).
>   - *content-changing*: Isi prompt ikut berubah.
>   - Kolom ini bersifat INFORMASI. Adaptasi sama untuk B1 dan B2 dalam satu tool, sehingga efeknya tidak dapat dipisahkan dari efek tool. Hal ini dibahas di Ancaman terhadap Validitas.
> - **B1/B2:** Rata-rata (bukan median) dipakai agar konsisten dengan model di TABEL VII.
> - **$\Delta$:** Penurunan saat *backbone* diganti. $\Delta$ besar = generator sensitif terhadap *backbone*.
> - *Contoh kalimat:* "MuTAP adalah generator yang paling sensitif terhadap backbone: mengganti B1 dengan B2 menurunkan mutation score-nya sebesar 14.1 poin."

---

#### TABEL VII. Model linear mixed-effects: $\text{metrik} \sim \text{tool} \times \text{backbone} + (1 \mid \text{unit})$

| Suite | Metrik | Faktor | Estimasi | SK 95% | $p$ | Var. (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | MS | Tool: CoverUp | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | Tool: MuTAP | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | Backbone: B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | CoverUp $\times$ B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| MT | MS | MuTAP $\times$ B2 | -13.1$\dagger$ | [-14.3, -11.9]$\dagger$ | $<0.001\dagger$ | 4.7$\dagger$ |
| CM | BC | Tool: CoverUp | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | Backbone: B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | BC | CoverUp $\times$ B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |

*Keterangan:* **Kondisi acuan:** CodaMOSA dengan B1. Estimasi dalam poin persentase; unit (fungsi atau modul) sebagai *random intercept*. **SK**: Selang Kepercayaan (Confidence Interval); **Var.**: Porsi variasi yang dijelaskan oleh faktor tersebut.  
$\dagger$ *Nilai dummy.*

> ### 📌 CATATAN TABEL VII: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-B (RQ2). **Sumber data:** Semua run tool LLM dari S4 (bukan median).
> - **Analisis:** 5 (linear *mixed-effects model* [29]; Python: `statsmodels MixedLM`, R: `lme4`).
> - **Faktor:** "Tool" = efek algoritma; "Backbone" = efek model; "$\times\text{ B2}$" = interaksi (apakah efek *backbone* berbeda antar-tool).
> - **Estimasi:** Selisih poin persentase terhadap kondisi acuan (CodaMOSA + B1).
>   - Baris "Backbone: B2" adalah efek ganti *backbone* untuk CodaMOSA saja.
>   - Baris "MuTAP $\times$ B2" adalah penurunan TAMBAHAN yang dialami MuTAP.
> - **SK 95%:** Bila tidak melewati 0, efeknya nyata.
> - **$p$:** Signifikansi. Interaksi signifikan = temuan kunci RQ2.
> - **Var. (%):** Menjawab seberapa besar variasi yang dapat diatribusikan ke faktor tersebut.
> - **$(1 \mid \text{unit})$:** Fungsi/modul sebagai efek acak agar perbedaan tingkat kesulitan kode tidak dikira efek tool.
> - *Contoh kalimat:* "Interaksi tool $\times$ backbone signifikan pada MT suite: dengan B2, MuTAP kehilangan 13.1 poin lebih banyak daripada CodaMOSA (SK 95% [-14.3; -11.9])."

---

> ### 🖼️ Gambar 4 (Interaction plot) [Placeholder]
> - **Sumbu-x:** Backbone (B1, B2)
> - **Sumbu-y:** Mutation score (MT) atau Branch coverage (CM)
> - **Garis:** Satu garis per generator LLM (CodaMOSA, CoverUp, MuTAP); titik rata-rata, garis galat $= 95\%$ CI.
> 
> **Deskripsi Gambar:** *Gambar 4. Rata-rata efektivitas generator berbasis LLM dengan backbone B1 dan B2.*
> 
> *Catatan Penulis:* Garis yang tidak sejajar menunjukkan adanya interaksi *tool* $\times$ *backbone*.

---

### C. RQ3: Karakteristik Kode

TABEL VIII menghubungkan keunggulan per modul setiap generator dengan karakteristik modul CM. `[ISI: temuan utama, mis. karakteristik yang paling kuat berasosiasi]`. Karena MuTAP hanya dijalankan pada MT suite, analisis ini mencakup Pynguin, CodaMOSA, dan CoverUp.

#### TABEL VIII. Korelasi Spearman parsial (kendali LOC) antara karakteristik modul dan keunggulan branch coverage per modul (CM suite, B1)

| Perbandingan | Karakteristik | $\rho\text{ parsial}$ | $p\text{ (Holm)}$ |
| :--- | :--- | :--- | :--- |
| CoverUp vs Pynguin | Cyclomatic complexity | `[ISI]` | `[ISI]` |
| CoverUp vs Pynguin | Dependensi eksternal | `[ISI]` | `[ISI]` |
| CoverUp vs Pynguin | Densitas anotasi tipe | -0.91$\dagger$ | $<0.001\dagger$ |
| CodaMOSA vs Pynguin | Cyclomatic complexity | `[ISI]` | `[ISI]` |
| CodaMOSA vs Pynguin | Dependensi eksternal | `[ISI]` | `[ISI]` |
| CodaMOSA vs Pynguin | Densitas anotasi tipe | `[ISI]` | `[ISI]` |
| CoverUp vs CodaMOSA | Cyclomatic complexity | `[ISI]` | `[ISI]` |
| CoverUp vs CodaMOSA | Dependensi eksternal | `[ISI]` | `[ISI]` |
| CoverUp vs CodaMOSA | Densitas anotasi tipe | `[ISI]` | `[ISI]` |

*Keterangan:* $n = [ISI]$ modul CM (minimal 40). Keunggulan = selisih median *branch coverage* kedua generator pada suatu modul (poin persentase). $\rho\text{ parsial}$ mengendalikan ukuran modul (LOC); $p$-value dikoreksi Holm atas sembilan uji.  
$\dagger$ *Nilai dummy.*

> ### 📌 CATATAN TABEL VIII: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-C (RQ3). **Sumber data:** Selisih median BC per modul (S4) + karakteristik modul (S1).
> - **Analisis:** Korelasi Spearman parsial [28] (dikontrol terhadap LOC) dengan koreksi Holm [26].
> - **Keunggulan:** Selisih median BC (tool 1 minus tool 2). Selisih dipakai (bukan $\hat{A}_{12}$) agar tidak menumpuk di 1.0 dan kehilangan variasi.
> - **Karakteristik:** *Cyclomatic complexity*, jumlah dependensi eksternal, dan densitas anotasi tipe.
> - **$\rho\text{ parsial}$:** $-1$ hingga $+1$. Mengontrol LOC penting karena *cyclomatic complexity* berkorelasi kuat dengan ukuran kode. Nilai negatif = makin tinggi nilai karakteristik, makin kecil keunggulan tool pertama.
> - **Daya uji:** Dengan 40 modul dan 9 uji Holm, $|\rho| \ge 0.43$ dapat terdeteksi.
> - **Batasan:** Korelasi bukan sebab-akibat (tulis "berasosiasi dengan", bukan "menyebabkan").
> - *Contoh kalimat:* "Keunggulan CoverUp atas Pynguin berasosiasi kuat dan negatif dengan densitas anotasi tipe ($\rho = -0.91$), sejalan dengan temuan bahwa ketiadaan informasi tipe menghambat SBST [7]."

---

> ### 🖼️ Gambar 5 (Scatter plot - OPSIONAL) [Placeholder]
> - **Sumbu-x:** Karakteristik dengan $\rho$ terbesar
> - **Sumbu-y:** Selisih median BC per modul (poin)
> - **Visual:** Satu titik = satu modul CM; garis horizontal di 0 (tidak ada keunggulan).
> 
> **Deskripsi Gambar:** *Gambar 5. Keunggulan branch coverage per modul terhadap [ISI: karakteristik] pada CM suite.*

---

### D. Efisiensi dan Biaya

TABEL IX melaporkan biaya pembangkitan per unit. `[ISI: perbandingan biaya, mis. generator termahal dan selisihnya terhadap peningkatan efektivitas]`.

#### TABEL IX. Biaya pembangkitan per unit (median)

| Suite | Tool | BB | Waktu (s) | Panggilan API | Token (ribu) | Biaya (USD) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MT | Pynguin | - | `[ISI]` | 0 | 0 | 0 |
| MT | CoverUp | B1 | 23.5$\dagger$ | 41 | 12.1 | 0.04$\dagger$ |
| MT | CodaMOSA, CoverUp, MuTAP | B1, B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |
| CM | Pynguin, CodaMOSA, CoverUp | -, B1, B2 | `[ISI]` | `[ISI]` | `[ISI]` | `[ISI]` |

*Keterangan:* **Waktu**: *wall-clock time* pembangkitan tanpa waktu tunggu *rate limit*. Biaya menggunakan harga penyedia pada saat run (`[ISI: tanggal]`). Pada tabel akhir, setiap konfigurasi memiliki barisnya sendiri.  
$\dagger$ *Nilai dummy.*

> ### 📌 CATATAN TABEL IX: Arti Kolom dan Cara Membaca (Hapus sebelum submit)
> - **Letak:** Subbab IV-D (pendukung, OPSIONAL). **Sumber data:** Log S2 dan `llm_proxy`.
> - **Analisis:** Deskriptif (tanpa uji statistik).
> - **Waktu:** Waktu pembangkitan per fungsi/modul. Waktu tunggu *rate limit* dipisah agar kuota tidak dikira kelambatan tool.
> - **Biaya:** Bila halaman terbatas, tabel ini dipindah ke paket replikasi dan diringkas dalam 1 kalimat di teks.

---

## V. PEMBAHASAN

`[ISI: 3–4 paragraf.]`

> ### 📌 KERANGKA POIN YANG WAJIB DIBAHAS:
> 1. Apakah peringkat generator pada RQ1 bertahan pada kedua *backbone* atau berubah mengikuti *backbone* (menghubungkan RQ1 dan RQ2).
> 2. Ketidaksesuaian antara *coverage* dan *mutation score*: sebuah generator dapat unggul pada satu metrik tetapi tertinggal pada metrik lainnya.
> 3. Bagaimana hasil ini dibandingkan dengan hasil CoverUp [10] dan TestWeaver [21] dengan *backbone* masing-masing.
> 4. Panduan praktis: generator mana yang dipakai untuk jenis kode apa (dari RQ3) dan dengan biaya berapa (TABEL IX).
> 
> *Catatan Penulis:* Jangan mengulang angka tabel satu per satu. Hubungkan temuan dengan celah di Pendahuluan: (1) satu *backbone* tidak cukup, (2) *coverage* saja tidak cukup, (3) perlu evaluasi independen.

---

## VI. ANCAMAN TERHADAP VALIDITAS

`[ISI: Satu paragraf per jenis ancaman.]`

> ### 📌 KERANGKA POIN ANCAMAN:
> - **Validitas Internal:** Adaptasi prompt untuk CodaMOSA dan MuTAP sama untuk kedua *backbone* sehingga tidak dapat dipisahkan dari efek tool; sifat nondeterministik pencarian dan sampling LLM (dimitigasi dengan $R$ run berulang); CoverUp dihentikan pada anggaran 600 detik walaupun tidak dirancang dengan batas waktu.
> - **Validitas Konstruk:** Efek plafon *coverage* pada MT suite; mutan ekuivalen tidak dikeluarkan; *mutation tool* untuk evaluasi berbeda dari *engine* MutPy yang dipakai MuTAP secara internal.
> - **Validitas Eksternal:** MuTAP hanya dijalankan pada MT suite sehingga tidak tercakup dalam RQ3; CM suite diambil sampelnya (bukan seluruhnya); hanya bahasa Python; dua *backbone*.
> - **Validitas Kesimpulan:** Perbandingan berganda (ditangani dengan metode Holm); daya uji statistik bergantung pada $R$.
> - **Kontaminasi Data:** HumanEval dan proyek CM bersifat publik sehingga mungkin masuk data pelatihan *backbone*; kemiripan tes yang dibangkitkan dengan tes eksisting dilaporkan mengikuti [4], [9].

---

## VII. KESIMPULAN

`[ISI: 1 paragraf, ±120 kata: ringkasan jawaban RQ1–RQ3 dalam satu kalimat masing-masing, kontribusi utama, dan rencana penelitian lanjutan. Jangan memasukkan angka baru yang tidak ada di Hasil.]`

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