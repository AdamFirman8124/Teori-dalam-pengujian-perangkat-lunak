

# Generated at 2026-10-24 10:19:15.244928
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

# Generated at 2026-10-24 10:19:16.561769
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

# Generated at 2026-10-24 10:19:17.868932
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

# Generated at 2026-10-24 10:19:35.890475
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:19:37.323932
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:19:38.756543
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:19:40.078081
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

# Generated at 2026-10-24 10:19:56.524289
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

# Generated at 2026-10-24 10:20:13.008370
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

# Generated at 2026-10-24 10:20:29.561656
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

# Generated at 2026-10-24 10:20:46.042014
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

# Generated at 2026-10-24 10:21:02.828178
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

# Generated at 2026-10-24 10:21:20.859152
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:21:22.388018
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:21:23.923713
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:21:40.627886
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

# Generated at 2026-10-24 10:21:57.081398
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

# Generated at 2026-10-24 10:22:13.687815
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

# Generated at 2026-10-24 10:22:30.482060
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

# Generated at 2026-10-24 10:22:47.327533
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

# Generated at 2026-10-24 10:23:03.969262
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

# Generated at 2026-10-24 10:23:20.763871
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

# Generated at 2026-10-24 10:23:38.988131
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:23:40.403296
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:23:41.855592
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:24:04.494380
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Zebra: last\r\n"
        "Accept: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: second\r\n"
    )

    result = formatter.format_headers(headers)

    assert result == (
        "HTTP/1.1 200 OK\r\n"
        "Accept: first\r\n"
        "Accept: second\r\n"
        "Content-Type: application/json\r\n"
        "Zebra: last"
    )

# Generated at 2026-10-24 10:24:29.494813
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

# Generated at 2026-10-24 10:24:52.837925
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "X-Duplicate: first\r\n"
        "Accept: application/json\r\n"
        "X-Duplicate: second\r\n"
        "Content-Type: text/plain"
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

# Generated at 2026-10-24 10:25:16.851600
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    raw_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Test: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: second\r\n"
        "Accept: */*"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
        "X-Test: first\r\n"
        "X-Test: second"
    )

    assert formatter.format_headers(raw_headers) == expected

# Generated at 2026-10-24 10:25:33.412982
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

# Generated at 2026-10-24 10:25:50.064449
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

# Generated at 2026-10-24 10:26:06.539694
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

# Generated at 2026-10-24 10:26:23.221962
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

# Generated at 2026-10-24 10:26:39.801941
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

# Generated at 2026-10-24 10:27:02.583446
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = object.__new__(HeadersFormatter)

    input_headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "Accept: application/json\r\n"
        "X-Request-ID: second\r\n"
        "Cache-Control: no-cache"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Cache-Control: no-cache\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(input_headers) == expected

# Generated at 2026-10-24 10:27:25.920229
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Zeta: last\r\n"
        "Accept: text/html\r\n"
        "X-Test: first\r\n"
        "Accept: application/json\r\n"
        "Host: example.com\r\n"
        "X-Test: second\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: text/html\r\n"
        "Accept: application/json\r\n"
        "Host: example.com\r\n"
        "X-Test: first\r\n"
        "X-Test: second\r\n"
        "X-Zeta: last"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-24 10:27:42.598582
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

# Generated at 2026-10-24 10:28:05.062794
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter.__new__(HeadersFormatter)

    headers = (
        "HTTP/1.1 200 OK\r\n"
        "X-Request-ID: first\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: second\r\n"
        "Accept: application/json\r\n"
    )

    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Accept: application/json\r\n"
        "Content-Type: application/json\r\n"
        "X-Request-ID: first\r\n"
        "X-Request-ID: second"
    )

    assert formatter.format_headers(headers) == expected

# Generated at 2026-10-24 10:28:21.481123
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

# Generated at 2026-10-24 10:28:38.009966
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

# Generated at 2026-10-24 10:28:56.019630
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:28:57.453816
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:28:58.805481
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:29:16.719920
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2026-10-24 10:29:18.217918
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)

# Generated at 2026-10-24 10:29:19.839800
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():formatter = HeadersFormatter.__new__(HeadersFormatter)