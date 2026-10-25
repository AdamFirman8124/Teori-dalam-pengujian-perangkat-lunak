# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from unittest.mock import Mock, sentinel

from httpie.output.formatters import colors


def test_format_body_highlights_when_lexer_is_available(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.formatter = sentinel.formatter

    get_lexer = Mock(return_value=sentinel.lexer)
    highlight = Mock(return_value=sentinel.highlighted_body)

    monkeypatch.setattr(colors.ColorFormatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    result = formatter.format_body('{"answer": 42}', "application/json")

    assert result is sentinel.highlighted_body
    get_lexer.assert_called_once_with("application/json", '{"answer": 42}')
    highlight.assert_called_once_with(
        code='{"answer": 42}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )


def test_format_body_returns_original_body_when_no_lexer_is_available(monkeypatch):
    formatter = object.__new__(colors.ColorFormatter)

    get_lexer = Mock(return_value=None)
    highlight = Mock()

    monkeypatch.setattr(colors.ColorFormatter, "get_lexer_for_body", get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", highlight)

    body = "unrecognized content"
    result = formatter.format_body(body, "application/x-unknown")

    assert result == body
    get_lexer.assert_called_once_with("application/x-unknown", body)
    highlight.assert_not_called()
