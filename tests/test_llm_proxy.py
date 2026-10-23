import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_proxy import append_jsonl, usage


def test_usage_openai_and_anthropic_shapes():
    assert usage({"usage": {"prompt_tokens": 2, "completion_tokens": 3}}) == (2, 3)
    assert usage({"usage": {"input_tokens": 4, "output_tokens": 5}}) == (4, 5)
    assert usage({}) == (None, None)


def test_log_never_contains_environment_key(tmp_path, monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "secret-value")
    path = tmp_path / "calls.jsonl"
    append_jsonl(path, {"request": {"model": "auto"}, "response": {"model": "auto"}})
    content = path.read_text(encoding="utf-8")
    assert "secret-value" not in content
    assert json.loads(content)["response"]["model"] == "auto"
