# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import pygments
from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter


def test_format_headers_with_256_colors():
    env = Environment(colors=256)
    plugin = ColorFormatter(env=env, format_options={})
    headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
    result = plugin.format_headers(headers)
    expected = pygments.highlight(
        code=headers,
        lexer=plugin.http_lexer,
        formatter=plugin.formatter,
    ).strip()
    assert isinstance(result, str)
    assert result == expected
    assert result == result.strip()
    assert "HTTP" in result
    assert "1.1" in result
    assert "200" in result
    assert "OK" in result


def test_format_headers_with_basic_colors():
    env = Environment(colors=8)
    plugin = ColorFormatter(env=env, format_options={})
    headers = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n"
    result = plugin.format_headers(headers)
    expected = pygments.highlight(
        code=headers,
        lexer=plugin.http_lexer,
        formatter=plugin.formatter,
    ).strip()
    assert isinstance(result, str)
    assert result == expected
    assert result == result.strip()
    assert "HTTP" in result
    assert "404" in result
