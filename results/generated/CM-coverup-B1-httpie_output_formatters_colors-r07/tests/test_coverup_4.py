# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

from unittest.mock import Mock

from httpie.output.formatters import colors


def test_format_headers_highlights_and_strips_output(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.http_lexer = object()
    formatter.formatter = object()

    highlight = Mock(return_value=" \n highlighted headers \n ")
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    result = formatter.format_headers("Content-Type: application/json")

    assert result == "highlighted headers"
    highlight.assert_called_once_with(
        code="Content-Type: application/json",
        lexer=formatter.http_lexer,
        formatter=formatter.formatter,
    )
