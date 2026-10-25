# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import re
import pygments
from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter

_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

def _strip_ansi(value: str) -> str:
    return _ANSI_RE.sub("", value)


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
    assert "HTTP/1.1" in _strip_ansi(result)
    assert "200" in _strip_ansi(result)
    assert "Content-Type" in _strip_ansi(result)


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
    assert "HTTP/1.1" in _strip_ansi(result)
    assert "404" in _strip_ansi(result)
