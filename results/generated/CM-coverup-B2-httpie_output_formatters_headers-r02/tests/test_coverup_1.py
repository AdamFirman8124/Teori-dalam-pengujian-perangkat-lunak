# file: project/httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8, 16, 17, 18], "branches": []}
# gained: {"lines": [7, 8, 16, 17, 18], "branches": []}

import pytest

from httpie.output.formatters.headers import HeadersFormatter


def make_formatter(sort: bool) -> HeadersFormatter:
    return HeadersFormatter(format_options={'headers': {'sort': sort}})


def test_init_enabled_true():
    formatter = make_formatter(sort=True)
    assert formatter.enabled is True
    assert formatter.kwargs == {'format_options': {'headers': {'sort': True}}}


def test_init_enabled_false():
    formatter = make_formatter(sort=False)
    assert formatter.enabled is False


def test_format_headers_sorts_headers():
    formatter = make_formatter(sort=True)
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Z-Header: last\r\n'
        'A-Header: first\r\n'
        'M-Header: middle\r\n'
    )
    expected = (
        'HTTP/1.1 200 OK\r\n'
        'A-Header: first\r\n'
        'M-Header: middle\r\n'
        'Z-Header: last'
    )
    assert formatter.format_headers(headers) == expected


def test_format_headers_retains_order_of_same_name():
    formatter = make_formatter(sort=True)
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Set-Cookie: b=2\r\n'
        'A-Header: x\r\n'
        'Set-Cookie: a=1\r\n'
    )
    expected = (
        'HTTP/1.1 200 OK\r\n'
        'A-Header: x\r\n'
        'Set-Cookie: b=2\r\n'
        'Set-Cookie: a=1'
    )
    assert formatter.format_headers(headers) == expected


def test_format_headers_no_headers_to_sort():
    formatter = make_formatter(sort=True)
    headers = 'HTTP/1.1 200 OK'
    assert formatter.format_headers(headers) == 'HTTP/1.1 200 OK'
