# Runs CodaMosa (gpt4) on the "good_modules" benchmark set
# Designed so that various instances can be run in parallel

import csv
from pathlib import Path
from collections import defaultdict
import subprocess
import os

openai_key=Path(os.environ['HOME']) / "openai-key"
modules_csv = Path("test-apps") / "good_modules.csv"
#config = "gpt4"
config = "gpt4o"
codamosa_tests = Path(f"{config}-coda")
runs=1
max_search_secs=600

modules = list()
with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        modules.append(m)

codamosa_tests.mkdir(exist_ok=True)

for run in range(runs):
    for m in modules:
        d = codamosa_tests / f"{m}-{run}"
        d = d.resolve()

        try:
            d.mkdir(exist_ok=False)
        except FileExistsError:
            continue

        cmd = f"scripts/run_one.sh {m} {str(d)} config-args/{config} {max_search_secs} --auth {openai_key}"
        print(f"**** {cmd}")
        subprocess.run(cmd, shell=True, check=False)
