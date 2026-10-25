# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from unittest.mock import Mock

from httpie.output.formatters import colors


def test_format_body_returns_body_unchanged_without_lexer(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    get_lexer = Mock(return_value=None)
    highlight = Mock()

    monkeypatch.setattr(formatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    body = '{"message": "hello"}'
    result = formatter.format_body(body=body, mime="application/octet-stream")

    assert result == body
    get_lexer.assert_called_once_with("application/octet-stream", body)
    highlight.assert_not_called()


def test_format_body_highlights_body_with_detected_lexer(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    lexer = object()
    pygments_formatter = object()
    get_lexer = Mock(return_value=lexer)
    highlight = Mock(return_value="\x1b[32mhighlighted\x1b[0m")

    formatter.formatter = pygments_formatter
    monkeypatch.setattr(formatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    body = '{"message": "hello"}'
    result = formatter.format_body(body=body, mime="application/json")

    assert result == "\x1b[32mhighlighted\x1b[0m"
    get_lexer.assert_called_once_with("application/json", body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=pygments_formatter,
    )
