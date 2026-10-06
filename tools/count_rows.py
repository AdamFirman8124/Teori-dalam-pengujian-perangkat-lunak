"""Summarise a run_experiment JSON-lines log: rows per dataset/method, metric means."""
import collections
import json
import statistics
import sys

path = sys.argv[1]
counts = collections.Counter()
metrics = collections.defaultdict(lambda: collections.defaultdict(list))
for line in open(path):
    line = line.strip()
    if not line.startswith("{"):
        continue
    try:
        d = json.loads(line)
    except json.JSONDecodeError:
        continue
    key = (d["dataset"], d["method"])
    counts[key] += 1
    for m in ("line_pct", "pass_rate", "mutation_score"):
        v = d.get(m)
        if isinstance(v, (int, float)):
            metrics[key][m].append(v)

print(f"{'dataset':<10} {'method':<12} {'rows':>4} "
      f"{'cov%':>7} {'pass%':>7} {'MS%':>7}")
for key in sorted(counts):
    row = [f"{statistics.fmean(metrics[key][m]):.1f}" if metrics[key][m] else "-"
           for m in ("line_pct", "pass_rate", "mutation_score")]
    print(f"{key[0]:<10} {key[1]:<12} {counts[key]:>4} " + " ".join(f"{v:>7}" for v in row))