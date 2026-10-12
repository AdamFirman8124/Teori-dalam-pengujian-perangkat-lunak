"""Execute the experiment notebook headlessly via nbclient.

Usage: .venv/bin/python tools/run_notebook.py <notebook> [out_notebook]

Reads/writes nothing sensitive; the notebook itself loads config/.env and
reads credentials from the kernel environment.
"""
from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

nb_path = Path(sys.argv[1]).resolve()
out_path = Path(sys.argv[2] if len(sys.argv) > 2 else nb_path).resolve()

nb = nbformat.read(nb_path, as_version=4)
client = NotebookClient(
    nb,
    timeout=None,
    kernel_name="teori-pengujian",
    resources={"metadata": {"path": str(nb_path.parent)}},
)
client.execute()
nbformat.write(nb, out_path)
print("NOTEBOOK_EXECUTED", out_path)
