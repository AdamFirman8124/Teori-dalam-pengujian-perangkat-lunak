#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ -x ".venv/bin/python" ] && ".venv/bin/python" -c "import pip" 2>/dev/null; then
    PIP=".venv/bin/python -m pip install"
else
    UV="$(command -v uv || true)"
    [ -z "$UV" ] && [ -x "$HOME/.local/bin/uv" ] && UV="$HOME/.local/bin/uv"
    if [ -z "$UV" ]; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        UV="$HOME/.local/bin/uv"
    fi
    if [ ! -x ".venv/bin/python" ]; then
        "$UV" venv .venv
    fi
    PIP="$UV pip install --python .venv/bin/python"
fi

$PIP -r requirements.lock
$PIP ./coverup ipykernel
.venv/bin/python -m ipykernel install --user --name teori-experiment --display-name ".venv (Python 3.14.4)"
.venv/bin/python scripts/inventory.py
.venv/bin/python scripts/build_matrix.py --pilot
.venv/bin/python -m pytest tests -q
