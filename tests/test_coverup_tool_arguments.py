"""Malformed tool-call arguments must not abort the whole CoverUp task.

Observed failure:

    json.decoder.JSONDecodeError: Extra data: line 1 column 3 (char 2)
      coverup/src/coverup/llm.py, in _call_function
        args = json.loads(tool_call.function.arguments)

The exception escaped ``asyncio.gather`` and marked the task BLOCKED at 0%.
A bad tool call is a recoverable model mistake: it should be reported back to
the model as a tool error, not crash the run.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "coverup" / "src"))
sys.path.insert(0, str(ROOT / "src"))


class _Fn:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class _Call:
    def __init__(self, name, arguments):
        self.function = _Fn(name, arguments)
        self.id = "call_1"


def _chatter():
    from coverup.llm import Chatter

    c = Chatter.__new__(Chatter)
    c._log_msg = lambda ctx, msg: None
    c._log_json = lambda ctx, j: None
    c._functions = {"get_info": {"function": lambda ctx: "ok"}}
    return c


def test_extra_data_arguments_return_error_not_raise():
    c = _chatter()
    # exactly the shape that crashed: JSON object followed by extra text
    result = c._call_function(object(), _Call("get_info", "{} {}"))
    assert "invalid arguments JSON" in result


def test_garbage_arguments_return_error_not_raise():
    c = _chatter()
    result = c._call_function(object(), _Call("get_info", "not json at all"))
    assert "invalid arguments JSON" in result


def test_empty_arguments_treated_as_no_args():
    c = _chatter()
    result = c._call_function(object(), _Call("get_info", ""))
    assert result == "ok"


def test_unknown_function_returns_error_not_keyerror():
    c = _chatter()
    result = c._call_function(object(), _Call("does_not_exist", "{}"))
    assert "unknown function" in result


def test_valid_arguments_still_work():
    c = _chatter()
    c._functions["echo"] = {"function": lambda ctx, value: value}
    result = c._call_function(object(), _Call("echo", '{"value": "hi"}'))
    assert result == "hi"
