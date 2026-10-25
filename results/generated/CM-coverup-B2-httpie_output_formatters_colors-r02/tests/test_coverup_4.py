# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import httpie.output.formatters.colors as colors


def test_format_headers_highlights_and_strips_output(monkeypatch):
    color_formatter = colors.ColorFormatter.__new__(colors.ColorFormatter)
    http_lexer = object()
    pygments_formatter = object()
    color_formatter.http_lexer = http_lexer
    color_formatter.formatter = pygments_formatter
    calls = []

    def fake_highlight(*, code, lexer, formatter):
        calls.append((code, lexer, formatter))
        return "  highlighted headers\n"

    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = color_formatter.format_headers("Content-Type: application/json")

    assert result == "highlighted headers"
    assert calls == [
        ("Content-Type: application/json", http_lexer, pygments_formatter)
    ]
