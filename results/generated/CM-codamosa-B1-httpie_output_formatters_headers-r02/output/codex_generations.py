

# Generated at 2026-10-23 18:48:29.733103
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept-Ranges: bytes"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept-Ranges: bytes\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

# Generated at 2026-10-23 18:48:36.503557
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
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

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:48:45.310774
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:48:52.592167
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=1\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=2"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=1\r\n"
        "Set-Cookie: second=2\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:48:59.540501
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "X-Alpha: first\r\n"
        "X-Zebra: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "X-Alpha: first\r\n"
        "X-Zebra: last\r\n"
        "X-Zebra: second"
    )

# Generated at 2026-10-23 18:49:06.925014
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Zebra: last\r\n"
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
        "Zebra: last"
    )

# Generated at 2026-10-23 18:49:14.478145
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Zebra: first\r\n'
        'Content-Type: application/json\r\n'
        'Accept: text/plain\r\n'
        'X-Zebra: second'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: text/plain\r\n'
        'Content-Type: application/json\r\n'
        'X-Zebra: first\r\n'
        'X-Zebra: second'
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:49:22.658445
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Accept: application/json\r\n"
        "X-Custom: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Custom: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:49:31.472840
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Test: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Test: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: first\r\n"
        "X-Test: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:49:38.499317
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Set-Cookie: first=value\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "Z-Header: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:49:47.555512
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Duplicate: first\r\n"
        "Content-Type: text/plain\r\n"
        "X-Duplicate: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Duplicate: first\r\n"
        "X-Duplicate: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:49:57.223034
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:50:05.391550
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

# Generated at 2026-10-23 18:50:13.200078
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
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

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:50:21.261493
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    raw_headers = (
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

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:50:28.426646
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
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

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:50:37.541332
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Test: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: first\r\n"
        "X-Test: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:50:44.998895
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

# Generated at 2026-10-23 18:50:52.442108
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "X-Test: first\r\n"
        "Accept: application/json\r\n"
        "X-Test: second\r\n"
        "Content-Type: text/plain\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Test: first\r\n"
        "X-Test: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:51:01.811405
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # format_headers does not depend on initialization state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "X-Multiple: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Multiple: second\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Multiple: first\r\n"
        "X-Multiple: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:51:08.977982
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Test: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Test: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: first\r\n"
        "X-Test: second"
    )

# Generated at 2026-10-23 18:51:15.725317
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Accept: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: first\r\n"
        "Accept: second\r\n"
        "Content-Type: application/json\r\n"
        "Z-Header: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:51:23.211672
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "Z-Header: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:51:30.678482
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

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:51:40.210712
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because module_0.format_headers() does not use instance state.
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Custom: first\r\n"
        "Content-Type: text/plain\r\n"
        "X-Custom: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:51:49.119744
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # module_0.format_headers() does not depend on state initialized by FormatterPlugin.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Custom: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Custom: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:51:55.997839
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass plugin initialization because module_0.format_headers() uses no instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:52:04.998912
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:52:15.130178
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

# Generated at 2026-10-23 18:52:23.115554
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__; format_headers does not depend on instance state.
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: value\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: value"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:52:31.614688
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because format_headers does not depend on instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:52:46.565676
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(
        format_options={'headers': {'sort': True}}
    )
    input_headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Zeta: first\r\n'
        'Content-Type: application/json\r\n'
        'Accept: */*\r\n'
        'X-Zeta: second'
    )

    result = formatter.format_headers(input_headers)

    assert result == (
        'HTTP/1.1 200 OK\r\n'
        'Accept: */*\r\n'
        'Content-Type: application/json\r\n'
        'X-Zeta: first\r\n'
        'X-Zeta: second'
    )

# Generated at 2026-10-23 18:52:56.907466
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because format_headers does not use instance state.
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:53:04.904081
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:53:12.779567
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Set-Cookie: first=value\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "A-Header: first\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "Z-Header: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:53:20.664435
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
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

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:53:29.471728
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:53:39.917114
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: application/json\r\n"
        "X-Repeat: first\r\n"
        "Cache-Control: no-cache\r\n"
        "X-Repeat: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Cache-Control: no-cache\r\n"
        "X-Repeat: first\r\n"
        "X-Repeat: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:53:49.029407
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass plugin initialization because format_headers has no instance state.
    formatter = object.__new__(HeadersFormatter)

    raw_headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: first\r\n'
        'Accept: application/json\r\n'
        'X-Request-ID: second\r\n'
        'Content-Type: text/plain\r\n'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: application/json\r\n'
        'Content-Type: text/plain\r\n'
        'X-Request-ID: first\r\n'
        'X-Request-ID: second'
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:53:56.710003
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(
        format_options={'headers': {'sort': True}}
    )

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

# Generated at 2026-10-23 18:54:05.310688
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: */*\r\n"
        "X-Request-ID: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:54:13.196779
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "X-Duplicate: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Duplicate: second\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Duplicate: first\r\n"
        "X-Duplicate: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:54:22.412192
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because format_headers does not depend on instance state.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "X-Header: first value\r\n"
        "Accept: application/json\r\n"
        "X-Header: second value\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Header: first value\r\n"
        "X-Header: second value\r\n"
        "Z-Header: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:54:33.448556
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

# Generated at 2026-10-23 18:54:42.238895
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Custom: first\r\n"
        "Accept: application/json\r\n"
        "X-Custom: second\r\n"
        "Content-Type: text/plain"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:54:51.050696
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: second\r\n"
        "Accept: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: last\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:54:57.986632
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: first\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zebra: second"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Zebra: first\r\n"
        "X-Zebra: second"
    )

# Generated at 2026-10-23 18:55:05.320321
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

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

# Generated at 2026-10-23 18:55:11.468088
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:55:19.346406
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass plugin initialization because module_0.format_headers() has no state dependencies.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "X-Test: first\r\n"
        "Accept: application/json\r\n"
        "X-Test: second\r\n"
        "Host: example.com"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Host: example.com\r\n"
        "X-Test: first\r\n"
        "X-Test: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:55:30.519933
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: 123\r\n'
        'Set-Cookie: first=value\r\n'
        'Content-Type: application/json\r\n'
        'Set-Cookie: second=value\r\n'
        'Accept: */*\r\n'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: */*\r\n'
        'Content-Type: application/json\r\n'
        'Set-Cookie: first=value\r\n'
        'Set-Cookie: second=value\r\n'
        'X-Request-ID: 123'
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:55:39.255548
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

# Generated at 2026-10-23 18:55:48.737034
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
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

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:55:54.368632
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

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:56:03.789912
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

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

# Generated at 2026-10-23 18:56:12.697261
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:56:23.370306
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Request-ID: 123"
    )

# Generated at 2026-10-23 18:56:31.641257
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

# Generated at 2026-10-23 18:56:38.296990
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

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Zeta: first\r\n"
        "X-Zeta: second"
    )

# Generated at 2026-10-23 18:56:46.899506
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Content-Type: application/json\r\n"
        "Accept: text/plain\r\n"
        "X-Zebra: first"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: text/plain\r\n"
        "Content-Type: application/json\r\n"
        "X-Zebra: last\r\n"
        "X-Zebra: first"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:56:53.977740
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

# Generated at 2026-10-23 18:57:02.874099
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

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

# Generated at 2026-10-23 18:57:12.601760
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
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

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:57:23.250608
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(
        format_options={'headers': {'sort': True}}
    )

    raw_headers = (
        'HTTP/1.1 200 OK\r\n'
        'X-Request-ID: 123\r\n'
        'Accept: application/json\r\n'
        'Content-Type: text/plain\r\n'
        'Accept: text/html\r\n'
    )

    expected = (
        'HTTP/1.1 200 OK\r\n'
        'Accept: application/json\r\n'
        'Accept: text/html\r\n'
        'Content-Type: text/plain\r\n'
        'X-Request-ID: 123'
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:57:32.266001
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Avoid FormatterPlugin initialization because format_headers is stateless.
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: application/json"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:57:44.141407
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Bypass __init__ because format_headers does not depend on instance state.
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: value\r\n"
        "X-Example: first\r\n"
        "Accept: application/json\r\n"
        "X-Example: second"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "X-Example: first\r\n"
        "X-Example: second\r\n"
        "X-Zebra: value"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:57:53.266090
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zebra: last\r\n"
        "Accept: application/json\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "Content-Type: text/plain\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: text/plain\r\n"
        "X-Custom: first\r\n"
        "X-Custom: second\r\n"
        "X-Zebra: last"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-23 18:58:01.960297
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: 123\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=1\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=2\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=1\r\n"
        "Set-Cookie: second=2\r\n"
        "X-Request-ID: 123"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-23 18:58:09.170323
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Z-Header: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: second=value"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "Z-Header: last"
    )

# Generated at 2026-10-23 18:58:19.776164
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
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

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-23 18:58:27.288959
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Set-Cookie: first=value\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: second=value\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "Set-Cookie: first=value\r\n"
        "Set-Cookie: second=value\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(input_headers) == expected