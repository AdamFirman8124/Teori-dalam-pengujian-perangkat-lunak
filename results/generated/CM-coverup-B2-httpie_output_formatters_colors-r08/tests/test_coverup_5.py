# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import types
import pytest
from pygments.lexers.special import TextLexer
import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


def _make_env(colors=8):
    return types.SimpleNamespace(colors=colors)


def _make_formatter(explicit_json=False, colors=8):
    env = _make_env(colors=colors)
    return ColorFormatter(env=env, explicit_json=explicit_json, format_options={})


def test_get_lexer_for_body_json_mime():
    formatter = _make_formatter(explicit_json=False)
    lexer = formatter.get_lexer_for_body(mime="application/json", body='{"a": 1}')
    assert lexer is not None
    assert hasattr(lexer, "get_tokens")
    assert "json" in type(lexer).__name__.lower()


def test_get_lexer_for_body_forwards_explicit_json_body_and_mime(monkeypatch):
    formatter = _make_formatter(explicit_json=True)
    assert formatter.explicit_json is True
    captured = {}

    def fake_get_lexer(mime=None, explicit_json=False, body=""):
        captured["mime"] = mime
        captured["explicit_json"] = explicit_json
        captured["body"] = body
        return "sentinel-lexer"

    monkeypatch.setattr(colors_module, "get_lexer", fake_get_lexer)
    result = formatter.get_lexer_for_body(mime="text/html", body="<html></html>")
    assert result == "sentinel-lexer"
    assert captured == {
        "mime": "text/html",
        "explicit_json": True,
        "body": "<html></html>",
    }


def test_get_lexer_for_body_explicit_json_fallback_to_json():
    formatter = _make_formatter(explicit_json=True)
    lexer = formatter.get_lexer_for_body(
        mime="application/x-unknown-mime", body='{"hello": "world"}'
    )
    assert lexer is not None
    assert not isinstance(lexer, TextLexer)
    assert "json" in type(lexer).__name__.lower()
