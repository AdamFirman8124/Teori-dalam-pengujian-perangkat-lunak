# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import pygments
from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter


def test_format_headers_returns_stripped_highlighted_output():
    env = Environment(colors=256)
    plugin = ColorFormatter(env=env, format_options={})
    assert hasattr(plugin, "http_lexer")
    assert hasattr(plugin, "formatter")
    headers = "HTTP/1.1 200 OK\nContent-Type: text/plain\n"
    result = plugin.format_headers(headers)
    expected = pygments.highlight(
        code=headers,
        lexer=plugin.http_lexer,
        formatter=plugin.formatter,
    ).strip()
    assert result == expected
    assert result == result.strip()
    assert result != ""
    assert "HTTP/1.1" in result or "HTTP" in result


def test_format_headers_forwards_lexer_and_formatter(monkeypatch):
    env = Environment(colors=8)
    plugin = ColorFormatter(env=env, format_options={})
    captured = {}
    real_highlight = pygments.highlight

    def fake_highlight(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return real_highlight(*args, **kwargs)

    monkeypatch.setattr(pygments, "highlight", fake_highlight)
    headers = "HTTP/1.1 404 Not Found\nContent-Type: text/plain"
    result = plugin.format_headers(headers)
    assert "kwargs" in captured
    assert captured["kwargs"]["code"] == headers
    assert captured["kwargs"]["lexer"] is plugin.http_lexer
    assert captured["kwargs"]["formatter"] is plugin.formatter
    expected = real_highlight(
        code=headers,
        lexer=plugin.http_lexer,
        formatter=plugin.formatter,
    ).strip()
    assert result == expected
    assert result == result.strip()
    assert not result.endswith("\n")
