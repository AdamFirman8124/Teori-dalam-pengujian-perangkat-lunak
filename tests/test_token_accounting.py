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


def test_coverup_per_call_log_records_input_and_output_tokens(tmp_path, monkeypatch):
    """The logger must persist the provider's exact input/output token counts."""
    from coverup import llm

    target = tmp_path / "coverup.jsonl"
    monkeypatch.setenv("COVERUP_LLM_CALLS_LOG", str(target))
    llm._llm_calls_log({
        "model": "openai/auto",
        "requested_model": "openai/auto",
        "returned_model": "auto",
        "prompt_tokens": 310,
        "completion_tokens": 7,
        "total_tokens": 317,
        "status_code": 200,
    })

    entry = json.loads(target.read_text(encoding="utf-8"))
    assert entry["requested_model"] == "openai/auto"
    assert entry["returned_model"] == "auto"
    assert entry["prompt_tokens"] == 310
    assert entry["completion_tokens"] == 7
    assert entry["total_tokens"] == 317


def test_coverup_live_response_accumulates_input_and_output_tokens(tmp_path, monkeypatch):
    """Exercise CoverUp's real chat path against a provider-shaped response."""
    import asyncio
    from types import SimpleNamespace
    from coverup import llm

    target = tmp_path / "coverup-live.jsonl"
    monkeypatch.setenv("COVERUP_LLM_CALLS_LOG", str(target))
    monkeypatch.setenv("OPENAI_API_KEY", "test-only")
    chatter = llm.Chatter("openai/gpt-5.6-luna")
    response = SimpleNamespace(
        model="auto",
        usage=SimpleNamespace(prompt_tokens=310, completion_tokens=7, total_tokens=317),
        choices=[SimpleNamespace(
            finish_reason="stop",
            message=SimpleNamespace(content="OK LUNA", tool_calls=[]),
        )],
        headers={},
        status_code=200,
        json=lambda: {"choices": [{"message": {"content": "OK LUNA"}}]},
    )

    async def fake_send(_request, ctx=None):
        return response

    monkeypatch.setattr(chatter, "_send_request", fake_send)
    monkeypatch.setattr(llm.litellm, "completion_cost", lambda _response: 0.0)
    result = asyncio.run(chatter.chat([{"role": "user", "content": "Balas OK"}]))

    entry = json.loads(target.read_text(encoding="utf-8"))
    assert result["choices"][0]["message"]["content"] == "OK LUNA"
    assert entry["requested_model"] == "openai/gpt-5.6-luna"
    assert entry["returned_model"] == "auto"
    assert chatter.prompt_tokens == entry["prompt_tokens"] == 310
    assert chatter.completion_tokens == entry["completion_tokens"] == 7
    assert chatter.total_tokens == entry["total_tokens"] == 317



def test_codamosa_usage_records_input_and_output_tokens():
    """CodaMOSA must parse and accumulate exact usage from the provider JSON."""
    import ast

    source = (ROOT / "codamosa" / "pynguin" / "languagemodels" / "model.py").read_text(
        encoding="utf-8"
    )
    tree = ast.parse(source)
    class_node = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                      and node.name == "_OpenAILanguageModel")
    method_node = next(node for node in class_node.body if isinstance(node, ast.FunctionDef)
                       and node.name == "_record_usage")
    namespace = {}
    exec(compile(ast.Module(body=[method_node], type_ignores=[]), "_record_usage", "exec"), namespace)

    class Model:
        prompt_tokens = 0
        completion_tokens = 0
        total_tokens = 0
        cache_read_tokens = 0
        cache_write_tokens = 0
        usage_reported = 0

    model = Model()

    class Response:
        @staticmethod
        def json():
            return {
                "usage": {
                    "prompt_tokens": 310,
                    "completion_tokens": 7,
                    "total_tokens": 317,
                    "prompt_tokens_details": {"cached_tokens": 0},
                }
            }

    namespace["_record_usage"](model, Response())
    assert model.prompt_tokens == 310
    assert model.completion_tokens == 7
    assert model.total_tokens == 317
    assert model.usage_reported == 1



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
