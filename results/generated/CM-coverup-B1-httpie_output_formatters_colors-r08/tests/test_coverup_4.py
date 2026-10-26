# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import pytest

from httpie.output.formatters.colors import ColorFormatter


class FakeEnv:
    """Minimal stand-in for httpie.context.Environment.

    ColorFormatter.__init__ only reads ``env.colors``, so a tiny fake
    avoids any dependency on real TTY state (no state pollution).
    """

    def __init__(self, colors):
        self.colors = colors


@pytest.mark.parametrize('colors', [256, 4])
def test_format_headers_highlights_and_strips(colors):
    formatter = ColorFormatter(FakeEnv(colors=colors), format_options={})
    assert formatter.enabled

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'
    result = formatter.format_headers(headers)

    # Postconditions: something was produced, it is fully stripped
    # (no leading/trailing whitespace), and pygments actually
    # colorized the output (ANSI escape sequences present).
    assert result
    assert result == result.strip()
    assert '\x1b[' in result
