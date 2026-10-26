# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import re
import pygments
from types import SimpleNamespace

from httpie.output.formatters.colors import ColorFormatter


def _make_formatter(colors=8):
    env = SimpleNamespace(colors=colors)
    return ColorFormatter(env=env, format_options={})


def _strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def test_format_headers_basic():
    fmt = _make_formatter()
    headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
    result = fmt.format_headers(headers)
    assert isinstance(result, str)
    # lines 75-79 end with .strip()
    assert result == result.strip()
    assert _strip_ansi(result).strip() != ""
    plain = _strip_ansi(result)
    assert "HTTP/1.1" in plain
    assert "Content-Type" in plain


def test_format_headers_strips_surrounding_whitespace():
    fmt = _make_formatter()
    headers = "HTTP/1.1 200 OK"
    result = fmt.format_headers(headers)
    assert isinstance(result, str)
    assert result == result.strip()
    assert not result.endswith("\n")
    assert not result.endswith(" ")
    assert "HTTP/1.1" in _strip_ansi(result)


def test_format_headers_delegates_to_pygments(monkeypatch):
    fmt = _make_formatter()
    captured = {}

    def fake_highlight(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return "  padded result  \n"

    monkeypatch.setattr(pygments, "highlight", fake_highlight)
    out = fmt.format_headers("HTTP/1.1 200 OK")

    assert captured["kwargs"].get("code") == "HTTP/1.1 200 OK"
    assert captured["kwargs"].get("lexer") is fmt.http_lexer
    assert captured["kwargs"].get("formatter") is fmt.formatter
    # verifies .strip() postcondition on lines 75-79
    assert out == "padded result"
