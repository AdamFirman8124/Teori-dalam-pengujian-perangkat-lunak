# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from pygments.lexer import Lexer

from httpie.output.formatters.colors import ColorFormatter


class _SentinelLexer(Lexer):
    pass


def _make_formatter(explicit_json):
    formatter = object.__new__(ColorFormatter)
    formatter.explicit_json = explicit_json
    return formatter


@pytest.mark.parametrize("explicit_json", [True, False])
def test_get_lexer_for_body_delegates_to_get_lexer(monkeypatch, explicit_json):
    calls = []

    def fake_get_lexer(mime, explicit_json, body):
        calls.append(
            {"mime": mime, "explicit_json": explicit_json, "body": body}
        )
        return _SentinelLexer

    monkeypatch.setattr(
        "httpie.output.formatters.colors.get_lexer",
        fake_get_lexer,
    )

    formatter = _make_formatter(explicit_json=explicit_json)
    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"key": "value"}',
    )

    assert result is _SentinelLexer
    assert calls == [
        {
            "mime": "application/json",
            "explicit_json": explicit_json,
            "body": '{"key": "value"}',
        }
    ]


def test_get_lexer_for_body_via_constructor_delegates(monkeypatch):
    calls = []

    def fake_get_lexer(mime, explicit_json, body):
        calls.append((mime, explicit_json, body))
        return _SentinelLexer

    monkeypatch.setattr(
        "httpie.output.formatters.colors.get_lexer",
        fake_get_lexer,
    )

    env = type("FakeEnv", (), {"colors": 1})()
    formatter = ColorFormatter(
        env=env,
        explicit_json=True,
        format_options={},
    )

    assert formatter.explicit_json is True

    result = formatter.get_lexer_for_body("text/plain", "hello")

    assert result is _SentinelLexer
    assert calls == [("text/plain", True, "hello")]


def test_get_lexer_for_body_real_json_returns_lexer():
    formatter = _make_formatter(explicit_json=False)

    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"key": "value"}',
    )

    assert result is not None
    lexer_class = result if isinstance(result, type) else type(result)
    assert issubclass(lexer_class, Lexer)


def test_get_lexer_for_body_real_explicit_json_returns_lexer():
    formatter = _make_formatter(explicit_json=True)

    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"key": "value"}',
    )

    assert result is not None
    lexer_class = result if isinstance(result, type) else type(result)
    assert issubclass(lexer_class, Lexer)
