# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

from httpie.output.formatters import colors


def test_format_headers_highlights_and_strips_output(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.http_lexer = object()
    formatter.formatter = object()
    calls = []

    def fake_highlight(*, code, lexer, formatter):
        calls.append((code, lexer, formatter))
        return "\n  highlighted headers  \t"

    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = formatter.format_headers("Content-Type: application/json")

    assert result == "highlighted headers"
    assert calls == [
        (
            "Content-Type: application/json",
            formatter.http_lexer,
            formatter.formatter,
        )
    ]
