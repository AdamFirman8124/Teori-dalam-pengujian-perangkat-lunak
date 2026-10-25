# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest

from httpie.output.formatters import colors


@pytest.mark.parametrize("explicit_json", [False, True])
def test_get_lexer_for_body_delegates_to_get_lexer(monkeypatch, explicit_json):
    expected_lexer = object()
    calls = []

    def fake_get_lexer(*, mime, explicit_json, body):
        calls.append(
            {
                "mime": mime,
                "explicit_json": explicit_json,
                "body": body,
            }
        )
        return expected_lexer

    monkeypatch.setattr(colors, "get_lexer", fake_get_lexer)

    formatter = colors.ColorFormatter.__new__(colors.ColorFormatter)
    formatter.explicit_json = explicit_json

    result = formatter.get_lexer_for_body(
        mime="application/example+json",
        body='{"answer": 42}',
    )

    assert result is expected_lexer
    assert calls == [
        {
            "mime": "application/example+json",
            "explicit_json": explicit_json,
            "body": '{"answer": 42}',
        }
    ]
