# file: project/httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

from unittest.mock import Mock

import pytest

from httpie.output.formatters.colors import ColorFormatter


@pytest.mark.parametrize('colors', [1, 16, 256])
def test_format_headers_executes_highlight(colors):
    env = Mock(colors=colors)
    formatter = ColorFormatter(env=env, format_options={})
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'

    result = formatter.format_headers(headers)

    assert isinstance(result, str)
    assert result == result.strip()
    assert '200' in result
    assert 'Content-Type' in result
    # The headers must have been passed through pygments highlighting,
    # which tokenizes them rather than returning them verbatim.
    assert result != headers
