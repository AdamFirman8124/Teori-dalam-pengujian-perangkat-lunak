#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python -m pip install ./coverup
.venv/bin/python -m ipykernel install --user --name teori-experiment --display-name ".venv (Python 3.14.4)"
.venv/bin/python scripts/inventory.py
.venv/bin/python scripts/build_matrix.py --pilot
.venv/bin/python -m pytest tests -q
