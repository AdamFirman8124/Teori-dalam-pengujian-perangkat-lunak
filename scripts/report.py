#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def table(headers: list[str], body: list[list[object]]) -> str:
    if not body:
        return "_Belum tersedia._"
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(str(value) for value in record) + " |" for record in body]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "experiment_report.md")
    args = parser.parse_args()

    characteristics = rows(ROOT / "results" / "module_characteristics.csv")
    sample = rows(ROOT / "results" / "cm_sample.csv")
    pilot_matrix = rows(ROOT / "results" / "pilot_matrix.csv")
    full_matrix = rows(ROOT / "results" / "run_matrix.csv")
    pilot_results = rows(ROOT / "results" / "pilot_results.csv")
    final_results = rows(ROOT / "results" / "results.csv")
    probe_path = ROOT / "results" / "endpoint_probe.json"
    probes = json.loads(probe_path.read_text(encoding="utf-8")) if probe_path.exists() else []

    mt_available = 163
    cm_available = len(characteristics)
    cm_pilot = [row for row in sample if row.get("is_pilot") == "1"]
    cm_main = [row for row in sample if row.get("in_sample") == "1"]
    project_counts = Counter(row["project"] for row in cm_main)
    stratum_counts = Counter(row["stratum"] for row in cm_main)

    def result_summary(data: list[dict[str, str]]) -> list[list[object]]:
        grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for row in data:
            grouped.setdefault((row.get("suite", ""), row.get("tool", ""), row.get("backbone", "")), []).append(row)
        body = []
        for key, group in sorted(grouped.items()):
            costs = [float(row.get("cost_usd") or 0) for row in group]
            body.append([*key, len(group), sum(1 for item in group if item.get("status") == "ok"), sum(1 for item in group if item.get("status") == "failed"), f"{sum(costs):.6f}"])
        return body

    sections = [
        "# Laporan Eksperimen CodaMOSA vs CoverUp",
        "",
        "## 1. Status",
        "",
        "Dokumen ini dibuat otomatis dari artefak pipeline. Angka hasil hanya diisi dari data yang benar-benar diukur; angka dummy File A tidak digunakan sebagai target atau hasil.",
        "",
        f"- Probe endpoint: **{'selesai' if probes else 'belum dijalankan'}**",
        f"- Pilot R=2: **{'selesai/sebagian' if pilot_results else 'belum dijalankan'}**",
        f"- Run utama R=10: **{'selesai/sebagian' if final_results else 'belum dijalankan'}**",
        "",
        "## 2. Interpretasi Rancangan",
        "",
        "File B bersifat otoritatif. Pipeline ini mengukur CodaMOSA dan CoverUp pada MT dan CM dengan dua backbone. Hasil Pynguin dan MuTAP akan digabung dari kolaborator menggunakan skema hasil yang sama.",
        "",
        "Perbandingan tool pada suite yang sama bersifat berpasangan per unit. Perbandingan MT dengan CM untuk tool yang sama bersifat deskriptif karena unit MT dan CM tidak berpasangan.",
        "",
        "## 3. Inventaris Dataset",
        "",
        table(
            ["Suite", "Definisi satu task", "Tersedia", "Dipakai pilot", "Dipakai run utama"],
            [
                ["MT", "Satu fungsi benchmark dalam satu modul f001–f163", mt_available, 5, mt_available],
                ["CM", "Satu modul Python pada satu baris cm_modules.csv", cm_available, len(cm_pilot), len(cm_main)],
                ["Total", "—", mt_available + cm_available, 5 + len(cm_pilot), mt_available + len(cm_main)],
            ],
        ),
        "",
        f"Inventaris mentah berisi **{mt_available} MT + {cm_available} CM = {mt_available + cm_available} task**. Sesuai File B, run utama tidak memakai seluruh CM; ia memakai seluruh 163 MT dan sampel CM bertingkat sebanyak {len(cm_main)}, sehingga terdapat **{mt_available + len(cm_main)} unit analisis utama**.",
        "",
        "### Sampel CM per proyek",
        "",
        table(["Proyek", "Jumlah"], [[name, count] for name, count in sorted(project_counts.items())]),
        "",
        "### Sampel CM per stratum",
        "",
        table(["Stratum", "Jumlah"], [[name, count] for name, count in sorted(stratum_counts.items())]),
        "",
        "Deviasi yang disetujui: stratum L0B2 kosong pada populasi aktual, sehingga sampel mencakup seluruh delapan stratum non-kosong, bukan memaksakan stratum kesembilan.",
        "",
        "## 4. Matriks Run",
        "",
        table(
            ["Tahap", "Jumlah run"],
            [["Pilot: 5 MT + 3 CM × 2 tool × 2 backbone × R=2", len(pilot_matrix)], ["Utama: 163 MT + 40 CM × 2 tool × 2 backbone × R=10", len(full_matrix)]],
        ),
        "",
        "## 5. Model dan Probe",
        "",
        table(
            ["Backbone", "Requested", "Returned", "Function calling", "Status/Error"],
            [[item.get("backbone"), item.get("model_requested"), item.get("model_returned"), item.get("function_calling"), "PASS" if item.get("passed") else item.get("error", "FAIL")] for item in probes],
        ),
        "",
        "B1 dilaporkan sebagai `gpt-5.6-sol (seller-claimed; endpoint reports \"auto\")`. Identitas model adalah klaim penjual dan tidak dapat diverifikasi. Field model mentah dari setiap respons harus tetap disimpan untuk audit routing.",
        "",
        "## 6. Hasil Pilot",
        "",
        table(["Suite", "Tool", "Backbone", "Run tercatat", "OK", "Gagal", "Biaya USD"], result_summary(pilot_results)),
        "",
        "## 7. Hasil Utama",
        "",
        table(["Suite", "Tool", "Backbone", "Run tercatat", "OK", "Gagal", "Biaya USD"], result_summary(final_results)),
        "",
        "Analisis akhir menggunakan mean, median, dan standard deviation; Wilcoxon signed-rank berpasangan; koreksi Holm; Vargha–Delaney A12; dan bootstrap CI 95% untuk selisih mean.",
        "",
        "## 8. Task Gagal atau Dikeluarkan",
        "",
        "Daftar rinci tersedia di `results/analysis/excluded_tasks.csv` atau `results/pilot_analysis/excluded_tasks.csv`. Tidak ada task yang boleh dikeluarkan untuk menyesuaikan hasil dengan File A.",
        "",
        "## 9. Deviasi dari File B",
        "",
        "1. File A memuat angka ilustratif bertanda dummy; angka tersebut tidak dipakai sebagai ekspektasi.",
        "2. File B merevisi RQ3 menjadi cost-effectiveness; revisi ini mengalahkan rancangan korelasi karakteristik kode pada File A.",
        "3. Pipeline lokal menjalankan CodaMOSA dan CoverUp; Pynguin dan MuTAP ditangani kolaborator.",
        "4. Populasi CM hanya memiliki delapan stratum tertil non-kosong; penggunaan delapan stratum telah disetujui.",
        "5. B2 sementara menggunakan `auto` yang sama sebagai B1 karena endpoint konfigurasi B2 hanya mengekspos `auto`. Deviasi ini dicatat di docs/protocol.md dan tidak memenuhi dua rambang File B.",
        "",
        "## 10. Keterbatasan",
        "",
        "- Identitas GPT-5.6 Sol pada endpoint `auto` adalah klaim penjual dan tidak diverifikasi.",
        "- Perbandingan lintas dataset tidak berpasangan karena unit MT dan CM berbeda.",
        "- Hasil final tidak boleh disimpulkan sebelum probe B2, pilot, sanity checks, dan run utama selesai.",
        "- Efek kontaminasi data tetap mungkin karena benchmark bersifat publik.",
        "",
        "## 11. Artefak Reproduksi",
        "",
        "- `config/experiment.toml`: protokol mesin-baca (tanpa secrets)",
        "- `experiment_control.ipynb`: kontrol dan observasi proses",
        "- `scripts/setup.sh`: setup tunggal",
        "- `scripts/run_experiment.py`: entry point tunggal dan resumable",
        "- `results/module_characteristics.csv`, `results/cm_sample.csv`, `results/*matrix.csv`",
        "- `results/raw/<run_id>/`: request/response teredaksi",
        "- `results/generated/<run_id>/`: generated tests dan logs",
        "- `results/analysis/`: tabel statistik, failure rate, task exclusion, dan deviations",
    ]
    args.output.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Wrote Markdown report to {args.output}")


if __name__ == "__main__":
    main()
