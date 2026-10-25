

# Generated at 2026-10-24 10:09:28.875366
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:09:37.155057
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():import pytest
from httpie.plugins import FormatterPlugin
from your_module import HeadersFormatter  # adjust import to your file


class TestHeadersFormatterConstructor:

    def test_enabled_when_sort_true(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        assert formatter.enabled is True

    def test_disabled_when_sort_false(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
        assert formatter.enabled is False

    def test_missing_format_options_raises_keyerror(self):
        with pytest.raises(KeyError):
            HeadersFormatter()

    def test_missing_headers_section_raises_keyerror(self):
        with pytest.raises(KeyError):
            HeadersFormatter(format_options={})

    def test_is_formatter_plugin(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        assert isinstance(formatter, FormatterPlugin)

# Generated at 2026-10-24 10:09:53.753729
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:10:10.339640
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:10:11.808334
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():import pytest
from httpie.plugins import FormatterPlugin
from your_module import HeadersFormatter  # adjust import to your file


class TestHeadersFormatterConstructor:

    def test_enabled_when_sort_true(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        assert formatter.enabled is True

    def test_disabled_when_sort_false(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
        assert formatter.enabled is False

    def test_missing_format_options_raises_keyerror(self):
        with pytest.raises(KeyError):
            HeadersFormatter()

    def test_missing_headers_section_raises_keyerror(self):
        with pytest.raises(KeyError):
            HeadersFormatter(format_options={})

    def test_is_formatter_plugin(self):
        formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
        assert isinstance(formatter, FormatterPlugin)

# Generated at 2026-10-24 10:10:28.213330
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:10:44.985218
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:11:01.477964
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:11:19.661281
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:11:21.091995
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:11:22.452293
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:11:38.869021
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:11:55.409408
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:12:13.308199
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:12:14.749293
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:12:16.260082
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:12:34.306932
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:12:35.670969
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:12:37.039395
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:12:53.545236
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:13:09.944517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:13:26.453007
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:13:42.950574
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:13:59.510081
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:14:16.298904
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:14:34.298533
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:14:35.653734
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:14:37.066381
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:14:53.776443
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:15:10.548937
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:15:26.993153
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:15:43.748925
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:16:00.256124
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:16:16.831131
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:16:33.834573
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:16:50.309024
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:17:06.862127
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:17:24.816712
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:17:41.361291
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:17:57.894764
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:18:14.314399
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:18:30.976517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:18:47.454772
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only

# Generated at 2026-10-24 10:19:03.918753
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Status line stays first; headers get sorted by name
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
        'Accept: text/plain',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Accept: text/plain',
        'Content-Type: text/html',
        'Date: Mon, 01 Jan 2024 00:00:00 GMT',
    ])
    assert formatter.format_headers(headers) == expected

    # Already sorted input remains unchanged
    sorted_headers = '\r\n'.join([
        'HTTP/1.1 404 Not Found',
        'A: 1',
        'B: 2',
    ])
    assert formatter.format_headers(sorted_headers) == sorted_headers

    # Duplicate header names keep their relative order (stable sort)
    dup_headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'X-Custom: x',
        'Set-Cookie: a=1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Set-Cookie: b=2',
        'Set-Cookie: a=1',
        'X-Custom: x',
    ])
    assert formatter.format_headers(dup_headers) == expected

    # Header with no value is handled (split(':')[0] still works)
    no_value = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    expected = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-Empty:',
        'Z-Last: 1',
    ])
    assert formatter.format_headers(no_value) == expected

    # Only a status line â nothing to sort, returned as-is
    status_only = 'HTTP/1.1 500 Internal Server Error'
    assert formatter.format_headers(status_only) == status_only