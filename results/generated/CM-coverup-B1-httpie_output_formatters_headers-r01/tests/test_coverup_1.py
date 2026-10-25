# file: project/httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8, 16, 17, 18], "branches": []}
# gained: {"lines": [7, 8, 16, 17, 18], "branches": []}

from httpie.output.formatters.headers import HeadersFormatter


def test_init_enabled_true():
    fmt = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert fmt.enabled is True
    assert fmt.format_options == {'headers': {'sort': True}}
    assert fmt.kwargs == {'format_options': {'headers': {'sort': True}}}


def test_init_enabled_false():
    fmt = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert fmt.enabled is False
    assert fmt.format_options == {'headers': {'sort': False}}


def test_format_headers_sorts_by_name():
    fmt = HeadersFormatter(format_options={'headers': {'sort': True}})
    given = 'HTTP/1.1 200 OK\r\nX-Custom: c\r\nA-Header: a\r\nM-Header: m'
    result = fmt.format_headers(given)
    assert result == 'HTTP/1.1 200 OK\r\nA-Header: a\r\nM-Header: m\r\nX-Custom: c'
    # status line retained first
    assert result.splitlines()[0] == 'HTTP/1.1 200 OK'


def test_format_headers_stable_for_same_name():
    fmt = HeadersFormatter(format_options={'headers': {'sort': True}})
    given = 'HTTP/1.1 200 OK\r\nB: 1\r\nA: 2\r\nB: 3'
    result = fmt.format_headers(given)
    assert result == 'HTTP/1.1 200 OK\r\nA: 2\r\nB: 1\r\nB: 3'
    # relative order of duplicate names retained (stable sort)
    lines = result.splitlines()
    assert lines[0] == 'HTTP/1.1 200 OK'
    assert lines[1:] == sorted(lines[1:], key=lambda h: h.split(':')[0])


def test_format_headers_single_line():
    fmt = HeadersFormatter(format_options={'headers': {'sort': False}})
    given = 'HTTP/1.1 200 OK'
    result = fmt.format_headers(given)
    assert result == 'HTTP/1.1 200 OK'
