# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from unittest.mock import Mock, sentinel

from httpie.output.formatters import colors


def test_format_body_highlights_body_when_lexer_is_available(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.formatter = sentinel.formatter

    get_lexer = Mock(return_value=sentinel.lexer)
    highlight = Mock(return_value="highlighted body")
    monkeypatch.setattr(formatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    result = formatter.format_body('{"key": "value"}', "application/json")

    assert result == "highlighted body"
    get_lexer.assert_called_once_with("application/json", '{"key": "value"}')
    highlight.assert_called_once_with(
        code='{"key": "value"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )


def test_format_body_returns_body_unchanged_when_no_lexer_is_available(
    monkeypatch,
):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.formatter = sentinel.formatter

    get_lexer = Mock(return_value=None)
    highlight = Mock()
    monkeypatch.setattr(formatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    body = "unrecognized content"
    result = formatter.format_body(body, "application/x-unknown")

    assert result == body
    get_lexer.assert_called_once_with("application/x-unknown", body)
    highlight.assert_not_called()
