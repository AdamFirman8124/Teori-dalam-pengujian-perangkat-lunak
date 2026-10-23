# file: project/httpie/output/formatters/headers.py:4-18
# asked: {"lines": [7, 8, 16, 17, 18], "branches": []}
# gained: {"lines": [7, 8, 16, 17, 18], "branches": []}

import pytest
from httpie.output.formatters.headers import HeadersFormatter

def test_headers_formatter_init_enabled_true():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 assert formatter.enabled is True
 assert formatter.format_options == {'headers': {'sort': True}}

def test_headers_formatter_init_enabled_false():
 formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
 assert formatter.enabled is False
 assert formatter.format_options == {'headers': {'sort': False}}

def test_format_headers_sorts_by_name():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK\r\nZ-Header: last\r\nA-Header: first\r\nM-Header: middle"
 result = formatter.format_headers(headers)
 lines = result.split('\r\n')
 assert lines[0] == "HTTP/1.1 200 OK"
 assert lines[1] == "A-Header: first"
 assert lines[2] == "M-Header: middle"
 assert lines[3] == "Z-Header: last"

def test_format_headers_preserves_relative_order_of_same_name():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK\r\nAccept: text/html\r\nAccept: application/json\r\nAccept: */*"
 result = formatter.format_headers(headers)
 lines = result.split('\r\n')
 assert lines[0] == "HTTP/1.1 200 OK"
 assert lines[1] == "Accept: text/html"
 assert lines[2] == "Accept: application/json"
 assert lines[3] == "Accept: */*"

def test_format_headers_single_header_line():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html"
 result = formatter.format_headers(headers)
 lines = result.split('\r\n')
 assert lines[0] == "HTTP/1.1 200 OK"
 assert lines[1] == "Content-Type: text/html"

def test_format_headers_just_status_line():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK"
 result = formatter.format_headers(headers)
 assert result == "HTTP/1.1 200 OK"

def test_format_headers_status_line_with_trailing_newline():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK\r\n"
 result = formatter.format_headers(headers)
 assert result == "HTTP/1.1 200 OK"

def test_format_headers_empty_after_status_line():
 formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
 headers = "HTTP/1.1 200 OK\r\n\r\n"
 result = formatter.format_headers(headers)
 lines = result.split('\r\n')
 assert lines[0] == "HTTP/1.1 200 OK"
 assert lines[1] == ""