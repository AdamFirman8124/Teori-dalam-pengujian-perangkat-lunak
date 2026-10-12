"""Build rows.csv + rq1.md + rq2.md from a run_experiment JSON-lines log.

Useful while a run is still in progress: it reads whatever rows have been
printed so far, so a long baseline run does not have to finish to be readable.

    .venv/bin/python tools/build_report.py /tmp/baselines_full.log results_dir
"""
import csv
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import run_experiment as rx  # noqa: E402

log = Path(sys.argv[1])
outdir = Path(sys.argv[2] if len(sys.argv) > 2 else "results_report")
outdir.mkdir(parents=True, exist_ok=True)

rows = []
seen = set()
for line in log.read_text(errors="ignore").splitlines():
    line = line.strip()
    if not line.startswith("{"):
        continue
    try:
        d = json.loads(line)
    except json.JSONDecodeError:
        continue
    key = (d["dataset"], d["task"], d["method"])
    if key in seen:
        continue
    seen.add(key)
    rows.append(d)

if not rows:
    raise SystemExit("no rows found in " + str(log))

cols = ["dataset", "task", "method", "put", "line_pct", "pass_rate", "mutation_score",
        "killed", "survived", "problematic", "n_mutants", "n_tests", "n_passed",
        "n_test_files", "wall_time_s", "cost_usd", "coverup_ok", "coverup_GFU_R", "error"]
with (outdir / "rows.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# RQ1 groups by METHOD (CoverUp vs baselines); RQ2 groups by BACKBONE/model
# (which LLM/backbone yields the best coverage/pass-rate per unit time & cost).
by_method = {}
for r in rows:
    by_method.setdefault(r["method"], []).append(r)

by_backbone = {}
for r in rows:
    backbone = rx.backbone_name(r.get("model")) or r.get("method") or "unknown"
    by_backbone.setdefault(backbone, []).append(r)

rq1 = rx.table(by_method, "RQ1 - Main performance (Coverage / Pass Rate / Mutation Score)",
               ["line_pct", "pass_rate", "mutation_score"])
rq2 = rx.table(by_backbone, "RQ2 - Backbone (Coverage / Pass Rate / Time / Cost)",
               ["line_pct", "pass_rate", "wall_time_s", "cost_usd"],
               first_col="backbone")

per_dataset = {}
for ds in sorted({r["dataset"] for r in rows}):
    grp = {}
    for r in rows:
        if r["dataset"] == ds:
            grp.setdefault(r["method"], []).append(r)
    per_dataset[ds] = rx.table(grp, ds + " (n=%d tasks)" %
                               len({r["task"] for r in rows if r["dataset"] == ds}),
                               ["line_pct", "pass_rate", "mutation_score"])

(outdir / "rq1.md").write_text(rq1 + "\n" + rq2)
(outdir / "rq2.md").write_text(rq2)
(outdir / "rq_by_dataset.md").write_text("\n\n".join(per_dataset.values()))
print(rq1)
print(rq2)
print("\n".join(per_dataset.values()))
print("wrote", outdir / "rows.csv", "with", len(rows), "rows")