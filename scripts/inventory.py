#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from inventory import write_inventory


if __name__ == "__main__":
    mt_count, cm_count = write_inventory(ROOT / "results")
    print(f"MT tasks: {mt_count}")
    print(f"CM tasks: {cm_count}")
    print(f"Total available tasks: {mt_count + cm_count}")
