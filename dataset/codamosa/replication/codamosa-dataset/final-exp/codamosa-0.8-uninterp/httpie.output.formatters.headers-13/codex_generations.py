

# Generated at 2022-06-13 22:01:47.771537
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={'headers':{'sort': True}}).enabled
    assert not HeadersFormatter(format_options={'headers':{'sort': True}}).enabled


# Generated at 2022-06-13 22:01:49.611016
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter().enabled == True



# Generated at 2022-06-13 22:01:57.610303
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        '''\
Content-Length: 32
Connection: keep-alive
Content-Type: application/json
Cache-Control: null
Content-Length: 16
Connection: close
        '''
    ) == '''\
Content-Length: 32
Content-Length: 16
Cache-Control: null
Content-Type: application/json
Connection: keep-alive
Connection: close
        '''



# Generated at 2022-06-13 22:02:08.960538
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:02:10.815747
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():    
    headers_formatter = HeadersFormatter()


# Generated at 2022-06-13 22:02:16.607154
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert(HeadersFormatter().format_headers('Content-type: application/json\r\nHost: google.com\r\nConnection: close\r\nContent-Length: 200\r\n')
           == 'Content-type: application/json\r\nContent-Length: 200\r\nConnection: close\r\nHost: google.com\r\n')



# Generated at 2022-06-13 22:02:19.591856
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
  FormatterPlugin_instance = HeadersFormatter()
  FormatterPlugin_instance.format_options['headers']['sort'] = 'True'
  assert FormatterPlugin_instance.enabled == True


# Generated at 2022-06-13 22:02:31.026591
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})

    assert formatter.format_headers('\r\nX-Foo: bar\r\nA-B: 1\r\nA-B: 2\r\nA-B: 3') \
        == '\r\nA-B: 1\r\nA-B: 2\r\nA-B: 3\r\nX-Foo: bar'


# Generated at 2022-06-13 22:02:42.218180
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    s = 'POST http://httpbin.org/post HTTP/1.1\r\n' \
        'User-Agent: HTTPie\r\n' \
        'Content-Type: application/json\r\n' \
        'Accept: application/json\r\n' \
        'Accept-Encoding: gzip, deflate\r\n' \
        'Connection: keep-alive\r\n' \
        'Content-Length: 8\r\n' \
        '\r\n' \
        '{"a":"b"}'


# Generated at 2022-06-13 22:02:50.554468
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Date: Wed, 04 Sep 2019 05:51:58 GMT\r\n'
        'Server: nginx/1.15.12\r\n'
        'Content-Type: text/html; charset=utf-8\r\n'
        'X-Request-Start: 1567502118966\r\n'
        'Content-Length: 1245\r\n'
    )

    assert formatter.format_headers(headers) == headers



# Generated at 2022-06-13 22:02:57.908382
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter.format_headers("""GET /demo HTTP/1.1\r
Host: httpbin.org\r
Accept-Encoding: gzip, deflate\r
Accept: */*\r
User-Agent: HTTPie/0.9.2\r
Connection: keep-alive\r
\r
""") == """GET /demo HTTP/1.1\r
Host: httpbin.org\r
Accept: */*\r
Accept-Encoding: gzip, deflate\r
Connection: keep-alive\r
User-Agent: HTTPie/0.9.2\r
\r
"""


# Generated at 2022-06-13 22:03:08.554720
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    headers = '\r\n'.join((
        'HTTP/1.1 200 OK',
        'Server: gunicorn/19.7.1',
        'Connection: close',
        'Content-Type: text/html; charset=utf-8',
        'Date: Fri, 27 Apr 2018 10:20:29 GMT',
        'Transfer-Encoding: chunked',
        'X-Content-Type-Options: nosniff',
        'X-Frame-Options: DENY',
        'X-XSS-Protection: 1; mode=block'
    ))

# Generated at 2022-06-13 22:03:21.059722
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Create instance of class HeadersFormatter
    headers_formatter = HeadersFormatter()
    
    # Sample headers (multi-line string)
    headers = 'HTTP/1.1 200 OK\r\n' \
              'Set-Cookie: key=value; \r\n' \
              'Cache-Control: no-store\r\n' \
              'Pragma: no-cache\r\n' \
              'Set-Cookie: key2=value2; \r\n' \
              'Set-Cookie: key3=value3; '

    # Expected output (multi-line string)

# Generated at 2022-06-13 22:03:34.567020
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatted = headers_formatter.format_headers('''HTTP/1.0 200 OK
Content-Type: application/json
Date: Fri, 09 Sep 2017 23:27:21 GMT
Server: BaseHTTP/0.6 Python/3.6.3
Transfer-Encoding: chunked
Accept: application/json
Accept-Encoding: gzip, deflate
Authorization: Basic dXNlcjpwYXNzd29yZA==
Connection: keep-alive
Content-Length: 40
Cookie: key1=value1; key2=value2
Host: localhost:8080
User-Agent: HTTPie/1.0.0-dev
X-Request-ID: 1234
''')

# Generated at 2022-06-13 22:03:44.228102
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = """HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 26
Content-Type: application/json
Date: Mon, 05 Aug 2019 21:05:06 GMT
Server: Example

{"status": "OK"}
""".strip()
    expected = """HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 26
Content-Type: application/json
Date: Mon, 05 Aug 2019 21:05:06 GMT
Server: Example

{"status": "OK"}
""".strip()
    assert expected == f.format_headers(headers)


if __name__ == "__main__":
    import sys
    import doctest

# Generated at 2022-06-13 22:03:47.468451
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headersFormatter = HeadersFormatter()
    assert isinstance(headersFormatter, HeadersFormatter)

# Unit tests for method format_headers()

# Generated at 2022-06-13 22:03:59.056027
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(stream=None, format_options={'headers': {'sort': True}})
    headers = """
HTTP/1.1 200 OK
Cache-Control: private
Server: Microsoft-IIS/7.5
X-AspNet-Version: 4.0.30319
X-Powered-By: ASP.NET
Content-Length: 29672
Content-Type: text/html; charset=windows-1256
Date: Thu, 24 Dec 2015 03:23:40 GMT

"""

# Generated at 2022-06-13 22:04:11.397311
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hformatter = HeadersFormatter()
    test_string = ('GET / HTTP/1.1\r\n'
                   'Host: localhost:8080\r\n'
                   'User-Agent: HTTPie/0.9.9\r\n'
                   'Accept-Encoding: gzip, deflate\r\n'
                   'Accept: */*\r\n'
                   'Connection: keep-alive\r\n')

# Generated at 2022-06-13 22:04:14.373773
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options=None).__class__ == HeadersFormatter


# Generated at 2022-06-13 22:04:22.315993
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
GET / HTTP/1.1
Header-C: C
Header-B: B
Header-A: A
Header-B: B2'''
    expected = '''\
GET / HTTP/1.1
Header-A: A
Header-B: B
Header-B: B2
Header-C: C'''
    assert HeadersFormatter(None).format_headers(headers) == expected



# Generated at 2022-06-13 22:04:36.721390
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

    # Test case 1

# Generated at 2022-06-13 22:04:48.756569
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fp = HeadersFormatter()

# Generated at 2022-06-13 22:05:00.169280
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
GET / HTTP/1.1
Accept: application/json
Connection: keep-alive
Host: www.example.com
User-Agent: HTTPie/0.9.2
Accept-Encoding: gzip, deflate
"""

    # This should be sorted by headers name
    expected_headers = """\
GET / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.example.com
User-Agent: HTTPie/0.9.2
"""

    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.format_headers(headers) == expected_headers

    # test when headers are already sorted
    assert formatter.format_headers(expected_headers) == expected_

# Generated at 2022-06-13 22:05:01.371503
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    tf = HeadersFormatter()
    assert tf.enabled == False


# Generated at 2022-06-13 22:05:11.513317
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Cache-Control: max-age=0
Accept-Ranges: bytes
Date: Wed, 16 May 2018 19:33:14 GMT
Expires: Wed, 16 May 2018 19:33:14 GMT
Content-Length: 12
Accept-Ranges: bytes
Content-Type: text/plain; charset=UTF-8
    '''
    expected_headers = '''
HTTP/1.1 200 OK
Accept-Ranges: bytes
Accept-Ranges: bytes
Cache-Control: max-age=0
Content-Length: 12
Content-Type: text/plain; charset=UTF-8
Date: Wed, 16 May 2018 19:33:14 GMT
Expires: Wed, 16 May 2018 19:33:14 GMT
    '''
    assert h

# Generated at 2022-06-13 22:05:19.916477
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\n" \
              "Set-Cookie: SESSIONID=123\r\n" \
              "Set-Cookie:lang=en-US\r\n" \
              "Server: example-server\n" \
              "Content-Type: application/xml; charset=utf-8\r\n\r\n"

# Generated at 2022-06-13 22:05:30.362271
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    assert h.format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Foo: 1',
        'A-Header: xxx',
        'Cache-Control: public, max-age=3600',
        'B-Header: 2',
        'A-Header: yyy',
    ])) == '\r\n'.join([
        'HTTP/1.1 200 OK',
        'A-Header: xxx',
        'A-Header: yyy',
        'B-Header: 2',
        'Cache-Control: public, max-age=3600',
        'Foo: 1',
    ])



# Generated at 2022-06-13 22:05:40.785358
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """Test the format_headers method of HeadersFormatter class"""
    test_string = '''\
    HTTP/1.1 200 OK\r\n\
    Server: nginx\r\n\
    Date: Sat, 13 Oct 2018 17:25:22 GMT\r\n\
    Content-Type: text/html; charset=utf-8\r\n\
    Transfer-Encoding: chunked\r\n\
    Connection: keep-alive\r\n\
    X-Frame-Options: SAMEORIGIN\r\n\
    X-XSS-Protection: 1; mode=block\r\n\
    X-Content-Type-Options: nosniff\r\n\
    Content-Encoding: gzip'''

# Generated at 2022-06-13 22:05:43.176963
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled == formatter.format_options['headers']['sort']


# Generated at 2022-06-13 22:05:49.458040
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
Content-Type: application/json
Content-Length: 35
Connection: keep-alive
X-Foo: 42
X-Bar: 42
"""
    expected = """\
Content-Type: application/json
Content-Length: 35
Connection: keep-alive
X-Bar: 42
X-Foo: 42
"""
    got = HeadersFormatter().format_headers(headers)
    assert got == expected


# Generated at 2022-06-13 22:06:02.431405
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """Tests the method HeadersFormatter.format_headers()
    """
    line1 = "HTTP/1.1 200 OK"
    line2 = "Content-Encoding: gzip"
    line3 = "Content-Length: 10"
    line4 = "Content-Type: text/html"
    line5 = "Date: Wed, 22 Apr 1998 05:19:00 GMT"
    line6 = "ETag: \"5c5d5d5e5f5f5f5f5f5f5f5f5f5f5f5f5f5f\""
    line7 = "Last-Modified: Wed, 22 Apr 1998 05:19:00 GMT"
    line8 = "Server: Apache/1.3.3 (Unix)"


# Generated at 2022-06-13 22:06:14.345112
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    snippet = """
    HTTP/1.1 200 OK
    Content-Length: 5931
    Content-Type: application/json
    Content-Encoding: gzip
    Server: Jetty(9.4.z-SNAPSHOT)
    Date: Fri, 11 Jan 2019 00:04:00 GMT
    X-Random-Header: abc
    X-Random-Header: mno
    X-Random-Header: xyz
    """
    headersFormatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:25.461781
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:35.857505
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
Content-Length: 0
Content-Type: application/json
Content-Type: application/x-www-form-urlencoded"""
    assert HeadersFormatter.format_headers(headers) == """\
Content-Length: 0
Content-Type: application/json
Content-Type: application/x-www-form-urlencoded"""

    headers = """\
Content-Length: 0
Content-Type: application/x-www-form-urlencoded
Content-Type: application/json"""
    assert HeadersFormatter.format_headers(headers) == """\
Content-Length: 0
Content-Type: application/x-www-form-urlencoded
Content-Type: application/json"""

# Generated at 2022-06-13 22:06:43.946130
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test case 1
    """
    headers_formatter = HeadersFormatter()
    actual = headers_formatter.format_headers("""Host: example.com\r
User-Agent: curl/7.43.0\r
Accept: */*\r
Content-Length: 13\r
Content-Type: application/x-www-form-urlencoded\r
\r
foo=bar&baz=qux""")
    expected = """Host: example.com\r
Accept: */*\r
Content-Length: 13\r
Content-Type: application/x-www-form-urlencoded\r
User-Agent: curl/7.43.0\r
\r
foo=bar&baz=qux"""
    assert expected == actual

    """
    Test case 2
    """
    headers_

# Generated at 2022-06-13 22:06:52.603680
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
    GET / HTTP/1.1
    Foo: aaa
    Foo: bbb
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: text/html; charset=utf-8
    Foo: ccc'''

    expected_headers = '''\
    GET / HTTP/1.1
    Content-Encoding: gzip
    Content-Type: text/html; charset=utf-8
    Connection: keep-alive
    Foo: aaa
    Foo: bbb
    Foo: ccc'''
    assert HeadersFormatter(format_options={'headers': {'sort': True}}).format_headers(headers) == expected_headers

# Generated at 2022-06-13 22:07:01.160116
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/html; charset=utf-8\r\n'
        'Content-Length: 10\r\n'
        'Set-Cookie: foo=bar\r\n'
        'Set-Cookie: spam=eggs\r\n'
        '\r\n'
        '1234567890'
    )
    formatted_headers = formatter.format_headers(headers)

# Generated at 2022-06-13 22:07:03.052817
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={}) is not None


# Generated at 2022-06-13 22:07:07.245387
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter(**{'format_options': {'headers': {'sort': True}}})
    # verify if the variable format_options is correctly set in the constructor of class HeadersFormatter
    assert headers_formatter.format_options['headers']['sort'] == True


# Generated at 2022-06-13 22:07:22.773136
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 2c2b8020-25a3-49e3-a30a-d948c6f27b8c
X-Rate-Limit-Limit: 10
X-Rate-Limit-Remaining: 8
X-Rate-Limit-Reset: 1516171296
Content-Length: 42

"""