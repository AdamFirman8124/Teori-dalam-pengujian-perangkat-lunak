import json
from pathlib import Path

from coverup.coverup import State


def test_checkpoint_replace_is_atomic(tmp_path):
    path = tmp_path / "checkpoint.json"
    state = State({"files": {}})
    state.save_checkpoint(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["version"] == 2
    assert not list(tmp_path.glob("tmp*"))
