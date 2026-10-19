

# Generated at 2022-06-13 22:01:54.097207
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options = {"headers": {"sort": True}})
    actual = formatter.format_headers("""GET / HTTP/1.1
Connection: close
X-Header: AAA
Host: example.org
Accept-Encoding: gzip
Connection: keep-alive
X-Header: CCC
Accept: */*
User-Agent: HTTPie
X-Header: BBB
""")
    expected = """GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip
Connection: close
Connection: keep-alive
Host: example.org
User-Agent: HTTPie
X-Header: AAA
X-Header: BBB
X-Header: CCC
"""
    assert actual == expected

# Generated at 2022-06-13 22:02:04.101425
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers1 = [
        'GET / HTTP/1.1',
        'Accept: application/json',
        'Content-Length: 0',
        'X-Auth-Token: 1234',
        'Content-Type: application/json'
    ]
    headers2 = [
        'GET / HTTP/1.1',
        'Accept: application/json',
        'X-Auth-Token: 1234',
        'Content-Length: 0',
        'Content-Type: application/json'
    ]
    assert HeadersFormatter().format_headers('\r\n'.join(headers1)) == '\r\n'.join(headers2)



# Generated at 2022-06-13 22:02:10.769823
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Test default constructor
    formatter = HeadersFormatter()
    assert formatter.enabled is False
    # Test constructor with custom format_options
    fo = {'headers': {'sort': True}}
    formatter = HeadersFormatter(format_options=fo)
    assert formatter.enabled is True


# Generated at 2022-06-13 22:02:21.791841
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert hf.format_headers('''\
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 1
Cache-Control: no-cache

''') == '''\
HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Length: 1
Content-Type: text/plain; charset=utf-8

'''

    hf = HeadersFormatter(format_options={'headers': {'sort': True}})

# Generated at 2022-06-13 22:02:25.972942
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Setup
    s = io.StringIO()
    formatter = HeadersFormatter(output_file=s)

    # Exercise
    formatter.format_headers('Test')

    # Verify
    assert s.getvalue() == 'Test'



# Generated at 2022-06-13 22:02:37.616204
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:02:50.358791
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(**{
        'format_options': {
            'headers': {
                'sort': True,
                'key': 'headers'
            }
        }
    })

# Generated at 2022-06-13 22:03:01.215381
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:03:07.238930
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    actual = HeadersFormatter().format_headers(headers="""\
HTTP/1.1 200 OK\r
Server: nginx\r
Cache-Control: private, max-age=0, no-store\r
Connection: close\r
X-Uid: tz4v4y6x3qzmc1bk\r
Expires: Sun, 13 Dec 2026 01:59:59 GMT\r
Date: Mon, 14 Dec 2015 02:00:04 GMT\r
Content-Type: text/html; charset=utf-8\r
Content-Encoding: gzip\r
Access-Control-Allow-Origin: *\r
X-Random-Header: random-value\r
X-Random-Header: another-random-value\r
\r
""")

# Generated at 2022-06-13 22:03:16.467864
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # create a dummy text file
    with open('dummy.txt', 'w') as file:
        file.write("""\
HTTP/1.1 200 OK\r
Content-Type: text/plain\r
Connection: keep-alive\r
Content-Length: 0\r
""")

    # open the dummy file
    with open('dummy.txt', 'r') as f:
        headers = f.read()

    formatter_plugin = HeadersFormatter()

    formatted_headers = formatter_plugin.format_headers(headers)

    # this variable will be None if test fails
    is_same = formatted_headers == """\
HTTP/1.1 200 OK\r
Connection: keep-alive\r
Content-Length: 0\r
Content-Type: text/plain\r
"""

    # delete the dummy