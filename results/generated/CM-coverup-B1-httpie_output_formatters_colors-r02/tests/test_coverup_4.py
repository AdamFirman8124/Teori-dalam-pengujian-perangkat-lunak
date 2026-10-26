# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import pytest

from httpie.output.formatters.colors import ColorFormatter


class FakeEnv:
    def __init__(self, colors):
        self.colors = colors


@pytest.mark.parametrize('colors', [256, 8])
def test_format_headers_highlights_and_strips(colors):
    formatter = ColorFormatter(FakeEnv(colors=colors), format_options={})
    assert formatter.enabled

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'
    result = formatter.format_headers(headers)

    assert result
    assert result == result.strip()
    assert '\x1b[' in result


def test_format_headers_explicit_style_256_colors():
    formatter = ColorFormatter(
        FakeEnv(colors=256),
        format_options={},
        color_scheme='monokai',
    )
    assert formatter.enabled

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'
    result = formatter.format_headers(headers)

    assert result
    assert result == result.strip()
    assert '\x1b[' in result
