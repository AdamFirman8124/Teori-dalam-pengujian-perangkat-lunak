# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

from httpie.output.formatters import colors


def test_get_lexer_for_body_delegates_to_get_lexer(monkeypatch):
    expected_lexer = object()
    calls = []

    def fake_get_lexer(*, mime, explicit_json, body):
        calls.append({
            "mime": mime,
            "explicit_json": explicit_json,
            "body": body,
        })
        return expected_lexer

    monkeypatch.setattr(colors, "get_lexer", fake_get_lexer)

    formatter = colors.ColorFormatter.__new__(colors.ColorFormatter)
    formatter.explicit_json = True

    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"success": true}',
    )

    assert result is expected_lexer
    assert calls == [{
        "mime": "application/json",
        "explicit_json": True,
        "body": '{"success": true}',
    }]
