# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from types import SimpleNamespace

from httpie.output.formatters.colors import ColorFormatter


def _make_formatter(explicit_json=False):
    env = SimpleNamespace(colors=16)
    return ColorFormatter(
        env=env,
        explicit_json=explicit_json,
        format_options={},
    )


def test_get_lexer_for_body_delegates_with_kwargs(monkeypatch):
    import httpie.output.formatters.colors as colors_mod
    formatter = _make_formatter(explicit_json=True)
    captured = {}
    sentinel = object()

    def fake_get_lexer(mime, explicit_json=False, body=""):
        captured["mime"] = mime
        captured["explicit_json"] = explicit_json
        captured["body"] = body
        return sentinel

    monkeypatch.setattr(colors_mod, "get_lexer", fake_get_lexer)
    result = formatter.get_lexer_for_body(mime="application/json", body='{"a": 1}')

    assert result is sentinel
    assert captured == {
        "mime": "application/json",
        "explicit_json": True,
        "body": '{"a": 1}',
    }


def test_get_lexer_for_body_json_mime():
    formatter = _make_formatter(explicit_json=False)
    lexer = formatter.get_lexer_for_body(mime="application/json", body='{"a": 1}')
    assert lexer is not None
    assert "json" in getattr(lexer, "aliases", [])


def test_get_lexer_for_body_explicit_json_fallback(monkeypatch):
    formatter = _make_formatter(explicit_json=False)
    monkeypatch.setattr(formatter, "explicit_json", True)
    lexer = formatter.get_lexer_for_body(mime="text/plain", body='{"a": 1}')
    assert lexer is not None
    assert "json" in getattr(lexer, "aliases", [])

    plain_formatter = _make_formatter(explicit_json=False)
    lexer_unknown = plain_formatter.get_lexer_for_body(
        mime="application/x-unknown-foobar123", body=""
    )
    assert lexer_unknown is None
