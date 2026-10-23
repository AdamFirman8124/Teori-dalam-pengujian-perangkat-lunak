# Provenansi Sumber dan Versi Tool (Fase 1 File B)

Parent repository HEAD: `c9c42f5b59f42c8a7d72db52428711fa6de59d18` (sebelum cleanup; `b683e3d02` setelah cleanup).

| Komponen | Versi yang Diperlukan | Path yang Dipertahankan | Status Provenansi |
|---|---|---|---|
| CodaMOSA | `plasma-umass/codamosa` `17a4c2a2ecb40b60e32a7e4a437db03573612f11` (berbasis Pynguin 0.19.0) | `codamosa/`, `dataset/codamosa/` | Commit diklaim File B/coverup-eval; salinan aktif berisi patch chat-completions, akunting, timeout, dan retry |
| CoverUp | 0.6.3 (commit upstream `c4ad2f13c74c1154761038cf924ae5ece27dffdc`) | `coverup/`, `dataset/coverup/` | Versi terverifikasi di `version.py`; salinan aktif berisi patch endpoint, logging, dan timeout |
| MT Benchmark | coverup-eval `f3173196b90181974b0b684600ffde42ac36672c` | `dataset/coverup-eval/MuTAP-benchmarks/` | 163 direktori tugas ada; metadata commit nested tidak ada |
| CM Benchmark | coverup-eval CodaMOSA replication | `dataset/codamosa/replication/test-apps/` | 425 baris manifest dari 24 proyek ada; metadata commit tidak ada |
| coverage.py | 7.16.2 | Image yang akan dibangun | Tertunda |
| Cosmic Ray | 8.7.0 | Image yang akan dibangun | Tertunda |

Catatan:
- CoverUp submodule pada coverup-eval `f3173196…` tak semula menggunakan CoverUp `130238e…` / 0.6.1, sedangkan paket yang dipisahkan adalah 0.6.3. Kedua fakta dicatat; tidak diperlakukan sebagai satu snapshots yang sama.
- Image historis hanya tersedia sebagai pointer Git LFS (tidak dapat dimuat); image Linux baru diperlukan untuk reproduksi.
