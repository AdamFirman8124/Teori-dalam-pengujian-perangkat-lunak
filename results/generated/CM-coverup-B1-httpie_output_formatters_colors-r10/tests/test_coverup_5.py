# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import types

import pytest

import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


def _make_formatter(explicit_json=False):
    env = types.SimpleNamespace(colors=1)
    return ColorFormatter(
        env,
        explicit_json=explicit_json,
        format_options={},
    )


@pytest.mark.parametrize("explicit_json", [True, False])
def test_get_lexer_for_body_delegates_to_get_lexer(monkeypatch, explicit_json):
    sentinel = object()
    calls = {}

    def fake_get_lexer(mime, explicit_json, body):
        calls["mime"] = mime
        calls["explicit_json"] = explicit_json
        calls["body"] = body
        return sentinel

    monkeypatch.setattr(colors_module, "get_lexer", fake_get_lexer)

    formatter = _make_formatter(explicit_json=explicit_json)
    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"key": "value"}',
    )

    assert result is sentinel
    assert calls == {
        "mime": "application/json",
        "explicit_json": explicit_json,
        "body": '{"key": "value"}',
    }
    assert formatter.explicit_json is explicit_json
