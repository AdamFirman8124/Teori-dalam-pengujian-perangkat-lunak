#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from matrix import generate_matrix

parser = argparse.ArgumentParser()
parser.add_argument("--pilot", action="store_true")
args = parser.parse_args()
name = "pilot_matrix.csv" if args.pilot else "run_matrix.csv"
count = generate_matrix(ROOT / "results" / name, pilot=args.pilot)
print(f"Wrote {count} runs to results/{name}")
