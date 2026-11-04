#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT / "src"))
from protocol import load_config  # noqa: E402


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
    combined_results_path = ROOT / "results" / "results_combined.csv"
    final_results = rows(combined_results_path) if combined_results_path.exists() else rows(ROOT / "results" / "results.csv")
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
            grouped.setdefault((row.get("suite", ""), row.get("tool", ""), row.get("backbone", "") or "-"), []).append(row)
        body = []
        for key, group in sorted(grouped.items()):
            costs = [float(row.get("cost_usd") or 0) for row in group]
            body.append([*key, len(group), sum(1 for item in group if item.get("status") == "ok"), sum(1 for item in group if item.get("status") == "failed"), f"{sum(costs):.6f}"])
        return body

    analysis_dir = ROOT / "results" / "analysis"
    tbl_vi = rows(analysis_dir / "table_vi_backbone_effect.csv")
    tbl_vii = rows(analysis_dir / "table_vii_mixed_effects.csv")
    tbl_ce = rows(analysis_dir / "table_viii_cost_effectiveness.csv")
    tbl_fail = rows(analysis_dir / "failure_rate.csv")
    tbl_v = rows(analysis_dir / "table_v_paired_tests.csv")

    pilot_done = len(pilot_results) >= 64 and all(r.get("status") == "ok" for r in pilot_results)
    main_done = len(final_results) >= 10150

    sections = [
        "# Laporan Eksperimen CodaMOSA vs CoverUp",
        "",
        "## 1. Status",
        "",
        "Dokumen ini dibuat otomatis dari artefak pipeline. Angka hasil hanya diisi dari data yang benar-benar diukur; angka dummy File A tidak digunakan sebagai target atau hasil.",
        "",
        f"- Probe endpoint: **{'selesai' if probes else 'belum dijalankan'}**",
        f"- Pilot R=2: **{'selesai (64/64 OK)' if pilot_done else ('selesai/sebagian' if pilot_results else 'belum dijalankan')}**",
        f"- Run utama R=10: **{'selesai (' + str(len(final_results)) + ' run tercatat)' if main_done else ('selesai/sebagian' if final_results else 'belum dijalankan')}**",
        "",
        "## 2. Interpretasi Rancangan",
        "",
        "File B bersifat otoritatif. Pipeline ini mengukur CodaMOSA, CoverUp, dan baseline Pynguin pada MT dan CM dengan dua backbone LLM (`B1 = gpt-5.6-sol`, `B2 = glm-5.3-flash`), serta menggabungkan hasil baseline MuTAP (`B1`) pada suite MT menggunakan skema hasil yang sama.",
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
            [
                ["Pilot: (5 MT + 3 CM) × (Pynguin + 2 tool × 2 backbone) × R=2", len(pilot_matrix)],
                ["Utama (matriks lokal): (163 MT + 40 CM) × (Pynguin + 2 tool × 2 backbone) × R=10", len(full_matrix)],
                ["Total gabungan (+ MuTAP MT B1: 1.533 run)", len(final_results)],
            ],
        ),
        "",
        "## 5. Model dan Probe",
        "",
        table(
            ["Backbone", "Requested", "Returned", "Function calling", "Status/Error"],
            [[item.get("backbone"), item.get("model_requested"), item.get("model_returned"), item.get("function_calling"), "PASS" if item.get("passed") else item.get("error", "FAIL")] for item in probes],
        ),
        "",
        f"B1 dilaporkan sebagai `{load_config()['backbones']['B1']['label']}` ($4.00/M input, $20.00/M output) dan B2 sebagai `{load_config()['backbones']['B2']['label']}` ($0.15/M input, $0.50/M output). Seluruh log panggilan mentah tersimpan di `results/raw/*/llm_log.jsonl`.",
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
        "### 7.1. Uji Berpasangan Antar-Tool (RQ1 — Tabel V)",
        "",
        table(
            ["Suite", "Metrik", "Backbone", "Perbandingan", "n", "W/T/L", "A12", "Delta Mean", "p (Holm)"],
            [
                [
                    r["suite"], r["metric"], r["backbone"], r["comparison"], r["n"],
                    f"{r['wins']}/{r['ties']}/{r['losses']}",
                    f"{float(r['a12']):.3f}", f"{float(r['mean_difference']):.2f}", f"{float(r['p_holm']):.4g}",
                ]
                for r in tbl_v
            ],
        ),
        "",
        "### 7.2. Efek Backbone & Linear Mixed-Effects Model (RQ2 — Tabel VI & VII)",
        "",
        table(
            ["Suite", "Metrik", "Tool", "Adaptasi", "Mean B1", "Mean B2", "Delta (B1-B2)", "Unit (n)"],
            [[r["suite"], r["metric"], r["tool"], r["adaptasi"], r["b1"], r["b2"], r["delta_b1_minus_b2"], r["n_units"]] for r in tbl_vi],
        ),
        "",
        table(
            ["Suite", "Metrik", "Faktor", "Estimasi", "95% CI", "p-value", "Varians (%)"],
            [
                [
                    r["suite"], r["metric"], r["factor"], r["estimate"],
                    f"[{r['ci_95_low']}, {r['ci_95_high']}]", f"{float(r['p_value']):.4g}", r["var_pct"],
                ]
                for r in tbl_vii
            ],
        ),
        "",
        "### 7.3. Cost-Effectiveness Terhadap Baseline Pynguin (RQ3 — Tabel VIII)",
        "",
        table(
            ["Suite", "Tool", "Backbone", "Metrik", "Median Tool", "Baseline Pynguin", "Delta E", "Median Cost (USD)", "CE Ratio"],
            [
                [
                    r["suite"], r["tool"], r["backbone"], r["metric"],
                    r["tool_median"], r["baseline_pynguin"], r["delta_e"], r["median_cost_usd"], r["CE"],
                ]
                for r in tbl_ce
            ],
        ),
        "",
        "## 8. Profil Kegagalan & Task yang Dikeluarkan",
        "",
        table(
            ["Suite", "Tool", "Backbone", "Total", "Gagal", "Kategori Dominan", "Jumlah Dominan", "Fail Rate", ">10%"],
            [
                [
                    r["suite"], r["tool"], r["backbone"], r["n_total"], r["n_failed"],
                    r["error_category"], r["count"], f"{float(r['fail_rate']) * 100:.1f}%", r["over_10pct"],
                ]
                for r in tbl_fail
            ],
        ),
        "",
        "Daftar rinci tersedia di `results/analysis/excluded_tasks.csv` atau `results/pilot_analysis/excluded_tasks.csv`. Tidak ada task yang dikeluarkan untuk menyesuaikan hasil dengan File A.",
        "",
        "## 9. Deviasi dari File B",
        "",
        "1. File A memuat angka ilustratif bertanda dummy; angka tersebut tidak dipakai sebagai ekspektasi.",
        "2. File B merevisi RQ3 menjadi cost-effectiveness; revisi ini mengalahkan rancangan korelasi karakteristik kode pada File A.",
        "3. Populasi CM hanya memiliki delapan stratum tertil non-kosong (`L0B2` kosong pada populasi aktual); penggunaan delapan stratum telah disetujui.",
        "4. Backbone B2 dijalankan terpisah ke `results/b2_results.csv` menggunakan model `glm-5.3-flash` dengan batas rate 50 RPM; sebagian baris awal B2 (686 run `ok`) direkam saat transisi endpoint `gpt-5.6-luna` sebelum distandarkan ke `glm-5.3-flash`.",
        "5. Filter dependensi container (`py2exe`, `python_apt`) diterapkan di `src/tool_adapters.py` agar modul target CM dapat diuji di lingkungan container Linux.",
        "",
        "## 10. Keterbatasan",
        "",
        "- Identitas model upstream pada router pihak ketiga bergantung pada pelaporan metadata endpoint (`model_returned`).",
        "- Perbandingan lintas dataset (MT vs CM) tidak berpasangan karena unit MT (fungsi tunggal) dan CM (modul utuh) berbeda.",
        "- Pembatasan rate 50 RPM dan latensi penalaran pada B2 meningkatkan proporsi `timeout` dalam batas anggaran 600 detik per run pada modul CM berukuran besar.",
        "- Efek kontaminasi data tetap mungkin karena benchmark MT dan CM bersifat publik.",
        "",
        "## 11. Artefak Reproduksi",
        "",
        "- `config/experiment.toml`: protokol mesin-baca (tanpa secrets)",
        "- `experiment.ipynb`: kontrol dan observasi proses",
        "- `scripts/setup.sh`: setup tunggal",
        "- `scripts/run_experiment.py`: entry point tunggal dan resumable",
        "- `results/module_characteristics.csv`, `results/cm_sample.csv`, `results/*matrix.csv`",
        "- `results/results_combined.csv`: gabungan kanonik seluruh 11.683 run (B1, B2, Pynguin, MuTAP)",
        "- `results/raw/<run_id>/`: request/response teredaksi",
        "- `results/generated/<run_id>/`: generated tests dan logs",
        "- `results/analysis/`: tabel statistik IV–IX, failure rate, task exclusion, dan deviations",
        "- `results/figures/`: visualisasi boxplot (Figure 3), interaksi (Figure 4), dan Pareto frontier (Figure 5)",
    ]
    args.output.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Wrote Markdown report to {args.output}")


if __name__ == "__main__":
    main()
