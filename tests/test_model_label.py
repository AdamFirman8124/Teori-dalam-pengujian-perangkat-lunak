"""Stored result labels must use the real backbone, not a router alias.

SrByte only exposes the transport id ``auto`` in ``/models`` and in the
response ``model`` field, while the backbone actually served is
``gpt-5.6-sol``.  Requests keep the transport id; every persisted label
(rows.csv, status.json, consolidated logs, tables) must be canonical.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def test_canonical_model_name_maps_alias_to_backbone(monkeypatch):
    import eval_metrics as em

    monkeypatch.setenv("MODEL_ALIASES", "auto=gpt-5.6-sol")
    assert em.canonical_model_name("auto") == "gpt-5.6-sol"
    assert em.canonical_model_name("openai/auto") == "openai/gpt-5.6-sol"
    assert em.canonical_model_name("gpt-5.6-sol") == "gpt-5.6-sol"
    assert em.canonical_model_name("openai/gpt-5.6-sol") == "openai/gpt-5.6-sol"


def test_canonical_model_name_without_mapping_is_identity(monkeypatch):
    import eval_metrics as em

    monkeypatch.delenv("MODEL_ALIASES", raising=False)
    assert em.canonical_model_name("auto") == "auto"
    assert em.canonical_model_name(None) is None
