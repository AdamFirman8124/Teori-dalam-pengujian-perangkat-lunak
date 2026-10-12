"""Token accounting must survive the round trip to the CoverUp checkpoint.

Provider token counts are the only exact cost signal for the experiment, so
they are accumulated by ``Chatter``, handed to ``State.add_usage``, written to
``coverup.checkpoint`` and read back by ``eval_metrics``.  These tests pin each
hop so a future refactor cannot silently drop the numbers.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "coverup" / "src"))
sys.path.insert(0, str(ROOT / "src"))


def test_state_accumulates_usage():
    from coverup.coverup import State

    state = State({"files": {}})
    assert state._usage["prompt_tokens"] == 0
    state.add_usage(100, 20, 120)
    state.add_usage(50, 10, 60)
    assert state._usage == {
        "prompt_tokens": 150,
        "completion_tokens": 30,
        "total_tokens": 180,
        "calls_with_usage": 2,
    }


def test_checkpoint_round_trip_preserves_usage(tmp_path):
    from coverup.coverup import State

    state = State({"files": {}})
    state.add_usage(1000, 250, 1250)
    ckpt = tmp_path / "coverup.checkpoint"
    state.save_checkpoint(ckpt)

    raw = json.loads(ckpt.read_text())
    assert raw["usage"]["prompt_tokens"] == 1000

    reloaded = State.load_checkpoint(ckpt)
    assert reloaded._usage["prompt_tokens"] == 1000
    assert reloaded._usage["completion_tokens"] == 250
    assert reloaded._usage["total_tokens"] == 1250


def test_checkpoint_missing_usage_key_still_loads(tmp_path):
    """Older checkpoints (no ``usage`` key) must keep working unchanged."""
    from coverup.coverup import State

    ckpt = tmp_path / "old.checkpoint"
    ckpt.write_text(json.dumps({
        "version": 2, "done": {}, "cost": 0.0,
        "counters": {"G": 1, "F": 0, "U": 0, "R": 0},
        "coverage": {"files": {}},
    }))
    state = State.load_checkpoint(ckpt)
    assert state is not None
    assert state._usage["prompt_tokens"] == 0
