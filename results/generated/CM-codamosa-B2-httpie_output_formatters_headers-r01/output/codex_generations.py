

# Generated at 2026-10-23 18:38:16.931605
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

# Generated at 2026-10-23 18:38:25.786925
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Cache-Control: no-cache"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Cache-Control: no-cache\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:38:35.927935
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=1\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=2"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=1\r\n"
        "Set-Cookie: second=2\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:38:57.838426
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():import pytest
from unittest.mock import Mock


@pytest.mark.parametrize("sort_enabled", [True, False])
def test_HeadersFormatter(sort_enabled):
    formatter = HeadersFormatter(
        env=Mock(),
        format_options={
            "headers": {
                "sort": sort_enabled,
            }
        },
    )

    assert formatter.enabled is sort_enabled

# Generated at 2026-10-23 18:39:09.820115
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: second\r\n"
        "Accept: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:39:17.806803
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:39:25.691002
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:39:34.190115
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "X-Duplicate: first\r\n"
        "Accept: application/json\r\n"
        "X-Duplicate: second\r\n"
        "Content-Type: text/plain"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Duplicate: first\r\n"
        "X-Duplicate: second\r\n"
        "X-Zebra: last"
    )

# Generated at 2026-10-23 18:39:42.211588
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: first\r\n"
        "A-Header: value\r\n"
        "Z-Header: second\r\n"
        "M-Header: value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: value\r\n"
        "M-Header: value\r\n"
        "Z-Header: first\r\n"
        "Z-Header: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:39:49.652602
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Test: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: second\r\n"
        "Accept: application/json\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: first\r\n"
        "X-Test: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:39:56.820872
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
        "Accept: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/plain\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:40:04.910468
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:40:13.511490
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:40:22.523319
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Accept: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: first\r\n"
        "Accept: second\r\n"
        "Content-Type: application/json\r\n"
        "Z-Header: last"
    )

# Generated at 2026-10-23 18:40:31.843366
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Zeta: first\r\n"
        "Alpha: value\r\n"
        "Zeta: second\r\n"
        "Beta: value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Alpha: value\r\n"
        "Beta: value\r\n"
        "Zeta: first\r\n"
        "Zeta: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:40:40.136447
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # format_headers does not depend on initialized instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Alpha: first\r\n"
        "Accept: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/plain\r\n"
        "X-Alpha: first\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:40:46.998051
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "Content-Type: text/plain\r\n"
    )

    result = formatter.format_headers(input_headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "X-Zeta: last"
    )

# Generated at 2026-10-23 18:40:54.062798
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zeta: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

# Generated at 2026-10-23 18:41:00.928274
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Accept: text/html"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/html\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:41:09.115649
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Custom: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Custom: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second"
    )

# Generated at 2026-10-23 18:41:16.900684
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because format_headers does not depend on instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Accept: text/html"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/html\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:41:24.680288
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:41:35.332621
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)  # Method does not use instance state

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=1\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=2\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=1\r\n"
        "Set-Cookie: second=2\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:41:43.421579
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Zebra: last\r\n'
        'Content-Type: application/json\r\n'
        'Accept: text/plain\r\n'
        'X-Zebra: second'
    )

    result = formatter.format_headers(headers)

    assert result == (
        'HTTP/1.1 200 OK\r\n'
        'Accept: text/plain\r\n'
        'Content-Type: application/json\r\n'
        'X-Zebra: last\r\n'
        'X-Zebra: second'
    )

# Generated at 2026-10-23 18:41:51.099448
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: text/plain\r\n"
    )

    result = formatter.format_headers(raw_headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

# Generated at 2026-10-23 18:41:59.907700
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: 123\r\n'
        'Set-Cookie: first=value\r\n'
        'Content-Type: application/json\r\n'
        'Set-Cookie: second=value'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json\r\n'
        'Set-Cookie: first=value\r\n'
        'Set-Cookie: second=value\r\n'
        'X-Request-ID: 123'
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:42:08.108353
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: application/json"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

# Generated at 2026-10-23 18:42:17.008000
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:42:26.122026
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    result = formatter.format_headers(raw_headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

# Generated at 2026-10-23 18:42:35.850998
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Custom: first\r\n"
        "Accept: text/plain\r\n"
        "Content-Type: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/plain\r\n"
        "Content-Type: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:42:44.246459
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:42:52.552642
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:43:01.142346
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Zebra: second\r\n"
        "Accept: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zebra: first\r\n"
        "X-Zebra: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:43:09.744055
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: first\r\n"
        "Accept: text/plain\r\n"
        "Z-Header: second\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: text/plain\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Z-Header: first\r\n"
        "Z-Header: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:43:17.115618
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: second\r\n"
        "Accept: */*"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

# Generated at 2026-10-23 18:43:25.819451
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:43:33.705726
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Zeta: last\r\n"
        "Alpha: first\r\n"
        "Middle: value\r\n"
        "Alpha: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Alpha: first\r\n"
        "Alpha: second\r\n"
        "Middle: value\r\n"
        "Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:43:41.599137
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Zeta: second\r\n"
        "Accept: text/plain\r\n"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/plain\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

# Generated at 2026-10-23 18:43:49.884809
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

# Generated at 2026-10-23 18:43:57.564737
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # module_0.format_headers() does not depend on initialization state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: value\r\n"
        "Accept: text/html\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: text/html\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: value"
    )

# Generated at 2026-10-23 18:44:04.932909
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Avoid invoking FormatterPlugin.__init__; format_headers has no instance
    # state dependencies.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Accept: application/json\r\n"
        "X-Zeta: second\r\n"
        "Content-Type: text/plain\r\n"
        "Accept: text/html"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Accept: text/html\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:44:13.027209
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:44:23.061927
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "X-Header: first value\r\n"
        "A-Header: first\r\n"
        "X-Header: second value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: first\r\n"
        "X-Header: first value\r\n"
        "X-Header: second value\r\n"
        "Z-Header: last"
    )

# Generated at 2026-10-23 18:44:30.541479
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Zeta: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:44:40.777271
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: 123\r\n'
        'Set-Cookie: first=1\r\n'
        'Accept: application/json\r\n'
        'Set-Cookie: second=2\r\n'
        'Content-Type: text/plain\r\n'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: application/json\r\n'
        'Content-Type: text/plain\r\n'
        'Set-Cookie: first=1\r\n'
        'Set-Cookie: second=2\r\n'
        'X-Request-ID: 123'
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:44:49.789591
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass plugin initialization because format_headers has no instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:44:57.469431
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first\r\n"
        "Set-Cookie: second\r\n"
        "X-Zeta: last"
    )

    # format_headers does not depend on instance state.
    result = HeadersFormatter.format_headers(None, raw_headers)

    assert result == expected

# Generated at 2026-10-23 18:45:04.851686
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

# Generated at 2026-10-23 18:45:13.840875
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Avoid __init__, since format_headers does not use instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:45:25.833473
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: abc123\r\n"
        "Set-Cookie: session=first\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: preference=dark\r\n"
        "Content-Type: application/json\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: session=first\r\n"
        "Set-Cookie: preference=dark\r\n"
        "X-Request-ID: abc123"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:45:36.381141
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:45:46.006617
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: first\r\n'
        'Content-Type: application/json\r\n'
        'Accept: application/json\r\n'
        'X-Request-ID: second'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: application/json\r\n'
        'Content-Type: application/json\r\n'
        'X-Request-ID: first\r\n'
        'X-Request-ID: second'
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:45:57.490120
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Z-Header: first\r\n'
        'A-Header: value\r\n'
        'Z-Header: second\r\n'
        'M-Header: value'
    )

    result = formatter.format_headers(headers)

    assert result == (
        'HTTP/1.1 200 OK\r\n'
        'A-Header: value\r\n'
        'M-Header: value\r\n'
        'Z-Header: first\r\n'
        'Z-Header: second'
    )

# Generated at 2026-10-23 18:46:07.306519
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Set-Cookie: first=value\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: second=value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "Z-Header: last"
    )

# Generated at 2026-10-23 18:46:13.975765
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: first\r\n"
        "Accept: application/json\r\n"
        "X-Zebra: second\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zebra: first\r\n"
        "X-Zebra: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:46:20.209564
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Zebra: first\r\n'
        'Content-Type: application/json\r\n'
        'X-Zebra: second\r\n'
        'Accept: application/json'
    )

    result = formatter.format_headers(headers)

    assert result == (
        'HTTP/1.1 200 OK\r\n'
        'Accept: application/json\r\n'
        'Content-Type: application/json\r\n'
        'X-Zebra: first\r\n'
        'X-Zebra: second'
    )

# Generated at 2026-10-23 18:46:28.709415
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Test: first\r\n"
        "Accept: application/json\r\n"
        "Zebra: value\r\n"
        "X-Test: second\r\n"
        "Content-Type: text/plain"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Test: first\r\n"
        "X-Test: second\r\n"
        "Zebra: value"
    )

# Generated at 2026-10-23 18:46:39.664726
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\n"
        "X-Trace: first\n"
        "Content-Type: application/json\n"
        "X-Trace: second\n"
        "Accept: application/json"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Trace: first\r\n"
        "X-Trace: second"
    )

# Generated at 2026-10-23 18:46:50.008227
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: application/json"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

# Generated at 2026-10-23 18:47:00.349154
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:47:10.590080
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Accept: application/json\r\n"
        "X-Zeta: second\r\n"
        "Content-Type: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:47:20.522572
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Zeta: first\r\n'
        'Content-Type: application/json\r\n'
        'X-Zeta: second\r\n'
        'Accept: */*'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: */*\r\n'
        'Content-Type: application/json\r\n'
        'X-Zeta: first\r\n'
        'X-Zeta: second'
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:47:29.024311
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Zeta: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:47:39.569433
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=1\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=2\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=1\r\n"
        "Set-Cookie: second=2\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:47:50.769311
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: value\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: value"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:47:58.720524
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: */*"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

# Generated at 2026-10-23 18:48:06.403106
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: text/html\r\n"
        "X-Request-ID: second\r\n"
        "Accept: application/json\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: text/html\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:48:13.056827
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "A-Header: first value\r\n"
        "M-Header: middle\r\n"
        "A-Header: second value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: first value\r\n"
        "A-Header: second value\r\n"
        "M-Header: middle\r\n"
        "Z-Header: last"
    )