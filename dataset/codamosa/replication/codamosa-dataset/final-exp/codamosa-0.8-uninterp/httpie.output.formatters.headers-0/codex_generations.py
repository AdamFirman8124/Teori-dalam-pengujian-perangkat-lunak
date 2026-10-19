

# Generated at 2022-06-13 22:01:43.339149
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-cache

""".strip()
    expected = """HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Type: application/json

""".strip()
    actual = formatter.format_headers(headers)
    assert actual == expected



# Generated at 2022-06-13 22:01:46.163187
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(**{'headers': {'sort': True}})
    assert formatter.enabled



# Generated at 2022-06-13 22:01:54.097994
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Input
    headers = '''\
HTTP/1.1 200 OK
ZZZ: val
NNN: val
AAA: val
BBB: val'''
    # Expected response
    expected = '''\
HTTP/1.1 200 OK
AAA: val
BBB: val
NNN: val
ZZZ: val'''

    # Perform the test
    obj = HeadersFormatter()
    actual = obj.format_headers(headers)

    # Validate the result
    assert expected == actual



# Generated at 2022-06-13 22:01:55.666275
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter([], True, {})
    assert h.enabled

# Generated at 2022-06-13 22:02:03.407141
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    method = 'HEADERS'
    headers = 'http://httpbin.org/get'
    #headers = 'Content-Type: application/json'
    print('\n--- test_HeadersFormatter ---')
    print('method:', method)
    print('headers:', headers)
    print('\nheaders sorted:')

    formatter = HeadersFormatter()
    print(formatter.format_headers(headers))
    print()


test_HeadersFormatter()

# Generated at 2022-06-13 22:02:05.373157
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    head_ = HeadersFormatter()
    assert 'headers' in head_.format_options

# Generated at 2022-06-13 22:02:08.660949
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
	assert HeadersFormatter().format_headers('foo\r\nbar\r\n') == 'foo\r\nbar\r\n'

# Generated at 2022-06-13 22:02:16.819382
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    formatted_headers = formatter.format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Cache-Control: no-cache',
        'Connection: keep-alive',
        'Content-Type: text/html; charset=utf-8',
        'Link: <http://localhost/some/resource/>; rel="next"',
        'Link: <http://localhost/some/resource/>; rel="prev"',
        'Set-Cookie: foo=bar; Path=/; Expires=Tue, 07-Nov-2017 20:12:31 GMT',
        'Set-Cookie: bar=baz; Path=/',
    ]))

# Generated at 2022-06-13 22:02:26.234548
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter(format_options={'headers': {'sort': True}})
    unsorted = (
        'GET / HTTP/1.1\r\n'
        'Content-Type: application/json\r\n'
        'Accept: application/json\r\n'
        'Content-Type: application/xml\r\n'
        'Accept: application/xml\r\n'
        'Content-Length: 35\r\n'
    )
    assert headers.format_headers(unsorted) == unsorted

# Generated at 2022-06-13 22:02:34.397001
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    result = hf.format_headers('HTTP/1.1 200 OK\r\nServer: s\r\nContent-Length: 0\r\nAccept: a\r\nContent-Type: c\r\nConnection: close')
    assert result == 'HTTP/1.1 200 OK\r\nAccept: a\r\nContent-Length: 0\r\nContent-Type: c\r\nConnection: close\r\nServer: s'



# Generated at 2022-06-13 22:02:49.990040
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = (
        '''Content-Type: application/json; charset=utf-8\r\nAccept: */*\r\n
        Authorization: Basic Zm9v\r\nContent-Type: application/json; charset=utf-8\r\n
        Content-Type: application/json'''
    )
    expected = (
        '''Content-Type: application/json; charset=utf-8\r\n
        Accept: */*\r\nAuthorization: Basic Zm9v\r\n
        Content-Type: application/json; charset=utf-8\r\n
        Content-Type: application/json'''
    )
    print(HeadersFormatter().format_headers(headers) == expected)


# Generated at 2022-06-13 22:02:53.547854
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # First, get class object
    formatter = HeadersFormatter()
    # Test that object is a instance of class
    assert isinstance(formatter, object)
    # Test that object is a instance of FormatterPlugin
    assert isinstance(formatter, FormatterPlugin)


# Generated at 2022-06-13 22:02:58.543404
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={'headers': {'sort': True}})
    assert HeadersFormatter(format_options={'headers': {'sort': False}})


# Generated at 2022-06-13 22:03:01.683453
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter()
    assert isinstance(headers_formatter, HeadersFormatter)
    assert headers_formatter.enabled == False


# Generated at 2022-06-13 22:03:10.446559
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.enabled = True
    headers = '''\
Content-Length: 11
Pragma: no-cache
Content-Type: application/json; charset=utf-8
Cache-Control: no-cache
Date: Thu, 19 Mar 2020 11:25:47 GMT
Server: nginx/1.10.3 (Ubuntu)
'''
    assert headers_formatter.format_headers(headers) == '''\
Content-Length: 11
Content-Type: application/json; charset=utf-8
Cache-Control: no-cache
Date: Thu, 19 Mar 2020 11:25:47 GMT
Pragma: no-cache
Server: nginx/1.10.3 (Ubuntu)
'''

# Generated at 2022-06-13 22:03:12.516585
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter.__init__ is not object.__init__


# Generated at 2022-06-13 22:03:16.819812
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test_data = '''POST / HTTP/1.1
Content-Type: text/html
X-Header: a b c
X-Header: d e f
Content-Length: 1
Connection: keep-alive
Accept: */*

'''

# Generated at 2022-06-13 22:03:23.508945
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test = '''\
GET / HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate, compress
Accept: */*
User-Agent: HTTPie/0.9.2
\
'''
    expected = '''\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, compress
Host: httpbin.org
User-Agent: HTTPie/0.9.2
\
'''
    formatter = HeadersFormatter()
    assert formatter.format_headers(test) == expected


# Generated at 2022-06-13 22:03:37.810366
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options['headers']['sort'] = True
    headers_formatter.format_options['headers']['truncate'] = None
    headers_formatter.format_options['headers']['all'] = True

    formatter = headers_formatter.get_formatter()


# Generated at 2022-06-13 22:03:44.457132
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
    HTTP/1.1 200 OK
    Cache-Control: private
    Connection: close
    Date: Wed, 07 Oct 2020 23:17:43 GMT
    Server: Apache
    Content-Length: 0
    Content-Type: text/html; charset=UTF-8
    """
    lines = headers.splitlines()
    sorted_headers = sorted(lines[1:], key=lambda h: h.split(':')[0])
    expected = '\r\n'.join(lines[:1] + sorted_headers)
    assert expected == HeadersFormatter.format_headers(headers)



# Generated at 2022-06-13 22:03:58.801195
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = \
'''HTTP/1.1 200 OK
Date: Wed, 07 Nov 2018 22:25:33 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_wsgi/3.4 Python/2.7.5
Last-Modified: Wed, 07 Nov 2018 21:12:17 GMT
ETag: "14-56b065acc1780"
Accept-Ranges: bytes
Content-Length: 20
Content-Type: text/plain; charset=UTF-8

dummy body for test'''
    obj = HeadersFormatter(format_options={'headers':{'sort': '1'}})

# Generated at 2022-06-13 22:04:02.952153
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter()
    assert headers_formatter.enabled is False
    assert headers_formatter.format_options['headers']['sort'] is False


# Generated at 2022-06-13 22:04:11.225457
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''GET /user HTTP/1.1
Host: example.org
Authorization: Bearer xxx
Content-Type: application/json'''

    assert HeadersFormatter().format_headers(headers) == '''GET /user HTTP/1.1
Authorization: Bearer xxx
Content-Type: application/json
Host: example.org'''


# Generated at 2022-06-13 22:04:12.660257
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter()



# Generated at 2022-06-13 22:04:14.992767
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter is not None


# Generated at 2022-06-13 22:04:18.881879
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter()
    assert isinstance(hf, FormatterPlugin)
    assert isinstance(hf, HeadersFormatter)


# Generated at 2022-06-13 22:04:34.517891
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:04:43.636714
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:04:54.419928
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # no second header
    assert (HeadersFormatter().format_headers("""\
HTTP/1.1 200 OK
foo: bar
""") == """\
HTTP/1.1 200 OK
foo: bar
""")
    # one second header
    assert (HeadersFormatter().format_headers("""\
HTTP/1.1 200 OK
foo: bar
second: 2
""") == """\
HTTP/1.1 200 OK
second: 2
foo: bar
""")
    # two second headers
    assert (HeadersFormatter().format_headers("""\
HTTP/1.1 200 OK
foo: bar
second: 2
baz: qux
second: 3
""") == """\
HTTP/1.1 200 OK
baz: qux
second: 3
second: 2
foo: bar
""")
   

# Generated at 2022-06-13 22:05:04.240905
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    HeadersFormatter().format_headers('\r\n'.join([
        'POST / HTTP/1.1',
        'Accept: */*',
        'Content-Type: application/json',
        'Content-Length: 39',
        'Host: httpbin.org',
        'User-Agent: HTTPie/0.9.2',
        '',
        '{"Hello": "World"}',
    ])) == '\r\n'.join([
        'POST / HTTP/1.1',
        'Content-Length: 39',
        'Content-Type: application/json',
        'Accept: */*',
        'Host: httpbin.org',
        'User-Agent: HTTPie/0.9.2',
        '',
        '{"Hello": "World"}',
    ])

# Generated at 2022-06-13 22:05:25.110913
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    f = HeadersFormatter()
    headers = ['HTTP/1.1 200 OK',
               'Header2: c',
               'Header1: b',
               'Header1: a']
    headers = '\r\n'.join(headers)
    expected_headers = ['HTTP/1.1 200 OK',
                        'Header1: b',
                        'Header1: a',
                        'Header2: c']
    expected_headers = '\r\n'.join(expected_headers)

    assert f.format_headers(headers) == expected_headers

# Generated at 2022-06-13 22:05:30.330853
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json
'''
    assert headers_formatter.format_headers(headers) == '''\
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json
'''

# Generated at 2022-06-13 22:05:40.785744
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\nHost: httpbin.org\r\nConnection: keep-alive\r\n"
    assert fmt.format_headers(headers) == "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nHost: httpbin.org\r\n"
    headers = "HTTP/1.1 200 OK\r\nHost: httpbin.org\r\nConnection: close\r\n"
    assert fmt.format_headers(headers) == "HTTP/1.1 200 OK\r\nConnection: close\r\nHost: httpbin.org\r\n"
    headers = "HTTP/1.1 200 OK\r\nContent-Encoding: gzip\r\n"

# Generated at 2022-06-13 22:05:50.921538
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
    HTTP/1.1 200 OK
    Set-Cookie: csrftoken=U6d8Ry34R2OvQxppHkJG0o8X5Wq3vBlt; expires=Sat, 07-Nov-2020 11:36:04 GMT; Max-Age=31449600; Path=/
    Content-Type: text/html; charset=utf-8
    Vary: Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 6535
    X-Content-Type-Options: nosniff
    Date: Thu, 07 Nov 2019 11:36:04 GMT
    """
    formatter = HeadersFormatter(format_options={})
    fmt_headers = formatter.format_headers(headers)
    assert fmt_

# Generated at 2022-06-13 22:06:01.875272
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
ETag: "3f80f-1b6-3e1cb03b"
Content-Type: text/html; charset=UTF-8
Content-Length: 131
Accept-Ranges: bytes
Connection: close

'''

# Generated at 2022-06-13 22:06:13.232143
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = f.format_headers("""
HTTP/1.1 200 OK
content-encoding: gzip
Content-Length: 43
content-type: application/json
connection: keep-alive
accept: */*
server: gunicorn/19.9.0
date: Sat, 24 Dec 2016 13:11:44 GMT

""")
    assert headers == """
HTTP/1.1 200 OK
accept: */*
connection: keep-alive
content-encoding: gzip
Content-Length: 43
content-type: application/json
date: Sat, 24 Dec 2016 13:11:44 GMT
server: gunicorn/19.9.0

"""

# Generated at 2022-06-13 22:06:24.517290
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:27.787698
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    '''
    Test that format_headers returns the same string as it receives.
    '''
    H = HeadersFormatter()
    assert H.format_headers('test') == 'test'

# Generated at 2022-06-13 22:06:37.617573
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    
    # Test case 1: Standard case
    headers = "HTTP/1.1 200 OK\r\n" \
              "Date: Sun, 04 Oct 2020 21:44:44 GMT\r\n" \
              "Server: Apache\r\n" \
              "Vary: Accept-Encoding\r\n" \
              "Content-Encoding: gzip\r\n" \
              "Connection: close\r\n" \
              "Content-Type: text/html\r\n" \
              "\r\n"

# Generated at 2022-06-13 22:06:46.597037
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_test=HeadersFormatter(format_options = {'headers': {'sort': True}})
    headers_test.format_headers("""HTTP/1.1 200 OK
Content-Length: 17
Content-Type: application/json
Server: Werkzeug/0.16.1 Python/3.7.3""")
    assert headers_test.format_headers("""HTTP/1.1 200 OK
Content-Length: 17
Content-Type: application/json
Server: Werkzeug/0.16.1 Python/3.7.3""") == """HTTP/1.1 200 OK
Content-Length: 17
Content-Type: application/json
Server: Werkzeug/0.16.1 Python/3.7.3"""

# Generated at 2022-06-13 22:07:08.371069
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()
    result = headersFormatter.format_headers(
        'HTTP/1.1 200 OK\r\n'
        'X-Foo: Bar\r\n'
        'X-Bar: Foo\r\n'
        'X-Foo: Baz\r\n'
    )
    assert result == (
        'HTTP/1.1 200 OK\r\n'
        'X-Bar: Foo\r\n'
        'X-Foo: Bar\r\n'
        'X-Foo: Baz\r\n'
    )

# Generated at 2022-06-13 22:07:19.568612
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = ("Content-Length: 20\r\n"
               "Content-Type: text/plain; charset=utf-8\r\n"
               "Accept: text/*\r\n"
               "Accept: application/json\r\n")
    headers_formatted = headers_formatter.format_headers(headers)
    headers_expected = ("Content-Length: 20\r\n"
                        "Accept: text/*\r\n"
                        "Accept: application/json\r\n"
                        "Content-Type: text/plain; charset=utf-8\r\n")
    assert headers_expected == headers_formatted

# Generated at 2022-06-13 22:07:24.611714
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    x = HeadersFormatter()
    assert x.format_headers('ACCEPT: application/json\nUSER_AGENT: httpie\nACCEPT: application/xml\nCOOKIE: abc') == 'ACCEPT: application/json\nACCEPT: application/xml\nCOOKIE: abc\nUSER_AGENT: httpie'


# Generated at 2022-06-13 22:07:34.465936
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    import httpie.plugins
    httpie.plugins._loaded = False

    fmt = HeadersFormatter()
    assert fmt.format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Z: 1',
        'X-A: 1',
        'X-B: 2',
        'X-B: 3',
        'X-A: 2',
        ''
    ])) == '\r\n'.join([
        'HTTP/1.1 200 OK',
        'X-A: 1',
        'X-A: 2',
        'X-B: 2',
        'X-B: 3',
        'Z: 1',
        ''
    ])


# Generated at 2022-06-13 22:07:44.876857
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    '''
    Test HeadersFormatter.format_headers.

    '''
    hf = HeadersFormatter()
    
    headers = '''\
GET / HTTP/1.1
Host: httpbin.org
User-Agent: HTTPie/0.7.2
Accept-Encoding: gzip, deflate, compress
Accept: application/json
Connection: keep-alive

    '''
    expected = '''\
GET / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate, compress
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.7.2

    '''
    actual = hf.format_headers(headers)
    assert actual == expected

# Generated at 2022-06-13 22:07:53.223365
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test case #1. Formatting headers with no CRLF or LF at end of headers
    input_headers = "HTTP/1.1 200 OK\r\n" \
                    "Content-Length: 25\r\n" \
                    "Content-Type: text/html\r\n" \
                    "Date: Mon, 06 Apr 2020 01:23:45 GMT\r\n" \
                    "X-Content-Type-Options: nosniff\r\n"

# Generated at 2022-06-13 22:08:01.081584
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Connection: keep-alive
Server: gunicorn/19.7.1
Date: Wed, 11 Apr 2018 01:45:52 GMT
content-length: 2
Cache-Control: max-age=604800
Via: 1.1 vegur\r
'''
    headers_formatter = HeadersFormatter()
    headers_formatted = headers_formatter.format_headers(headers)


# Generated at 2022-06-13 22:08:11.176007
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    from httpie.plugins import FormatterPlugin, Formatter
    from httpie.formatter import format_header

    # Given a FormatterPlugin with only one formatter,
    # and that formatter is a HeadersFormatter
    formatter_plugin = FormatterPlugin()
    formatter = HeadersFormatter()
    formatter_plugin.formatters = [formatter]

    # Given a Formatter with the above FormatterPlugin as
    # its only plugin, and that formatter is enabled
    formatter_ = Formatter(formatter_plugin)
    formatter_.enabled = True

    # Given a HTTP response with a header that is uppercase
    # (The sort function is case insensitive)
    http_response = HTTP_200_OK.copy()
    http_response.headers['Server'] = 'TestServer'

    # When I call the format

# Generated at 2022-06-13 22:08:18.812473
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Create the object
    formatter = HeadersFormatter()

    # Create headers and test formated headers
    headers = "GET / HTTP/1.1\r\nHost: www.example.com\r\nAuthorizatio: 12345\r\n\r\n"
    result = formatter.format_headers(headers)
    assert result == "GET / HTTP/1.1\r\nAuthorizatio: 12345\r\nHost: www.example.com\r\n\r\n"



# Generated at 2022-06-13 22:08:25.421761
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    assert headers_formatter.format_headers(textwrap.dedent("""\
        GET / HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Host: example.com
        User-Agent: HTTPie/X.Y.Z
        X-Custom-Header: 42

        """)) == textwrap.dedent("""\
        GET / HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Host: example.com
        User-Agent: HTTPie/X.Y.Z
        X-Custom-Header: 42

        """)

# Generated at 2022-06-13 22:08:51.698579
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    assert f.format_headers("""
HTTP/1.1 200 OK
Server: SimpleHTTP/0.6 Python/3.5.3
Date: Tue, 15 Aug 2017 06:31:27 GMT
Content-Length: 1
Content-Type: text/plain

""") == """
HTTP/1.1 200 OK
Content-Length: 1
Content-Type: text/plain
Date: Tue, 15 Aug 2017 06:31:27 GMT
Server: SimpleHTTP/0.6 Python/3.5.3

"""

# Generated at 2022-06-13 22:08:58.186472
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers_a = '''\
'Host: github.com
Accept: application/json
User-Agent: HTTPie/0.9.4
'''
    headers_b = '''\
User-Agent: HTTPie/0.9.4
Host: github.com
Accept: application/json
'''
    assert formatter.format_headers(headers_a) == formatter.format_headers(headers_b)



# Generated at 2022-06-13 22:09:08.661146
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    input = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Connection: close',
        'Content-Length: 56',
        'Content-Type: application/json; charset=utf-8',
        'Server: ngx_openresty',
        'Date: Mon, 12 Aug 2019 08:37:00 GMT',
        '',
        '{"message":"Hello, world!"}'
    ])
    output = formatter.format_headers(input)
    lines = output.splitlines()
    assert lines[1] == 'Connection: close'
    assert lines[2] == 'Content-Length: 56'
    assert lines[3] == 'Content-Type: application/json; charset=utf-8'

# Generated at 2022-06-13 22:09:12.308360
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''Content-Type: application/json
Accept: application/json
X-Custom-Header: 42
Accept-Encoding: gzip, deflate
Accept-Language: en
X-Custom-Header: 13'''

# Generated at 2022-06-13 22:09:22.716517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    HeadersFormatter_format_headers = HeadersFormatter().format_headers
    headers = '''\
HTTP/1.1 200 OK
Date: Sat, 23 Jun 2018 07:38:12 GMT
Server: Apache
X-Powered-By: PHP/5.2.6-1+lenny3
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 30
Connection: close
Content-Type: text/xml; charset=utf-8

'''

# Generated at 2022-06-13 22:09:31.667404
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''HTTP/1.1 200 OK
Date: Sun, 11 Aug 2019 05:54:43 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Tue, 04 Oct 2016 03:27:11 GMT
ETag: "2d-543969099c3c0"
Accept-Ranges: bytes
Content-Length: 45
Content-Type: text/plain
'''

# Generated at 2022-06-13 22:09:38.885928
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
foo: foo-value-1
bar: bar-value-1
foo: foo-value-2
bar: bar-value-2"""
    assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
bar: bar-value-1
bar: bar-value-2
foo: foo-value-1
foo: foo-value-2"""


# Generated at 2022-06-13 22:09:50.236734
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    plugin=HeadersFormatter()

    # Case 1
    headers_in=b'''\
HTTP/1.1 204 No Content
Server: example-server
HeaderA: foo
HeaderB: bar
HeaderA: baz'''
    headers_expected=b'''HTTP/1.1 204 No Content
HeaderA: foo
HeaderB: bar
HeaderA: baz
Server: example-server'''
    headers_out=plugin.format_headers(headers_in)
    assert headers_out==headers_expected

    # Case 2
    headers_in='''\
HTTP/1.1 204 No Content
Server: example-server
HeaderA: foo
HeaderB: bar
HeaderA: baz'''

# Generated at 2022-06-13 22:09:59.943028
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """HTTP/1.1 200 OK\r
Content-Length: 5\r
Content-Type: text/html; charset=UTF-8\r
\r
hello"""

    hf = HeadersFormatter(format_options={'headers': {'structure': 'always-display', 'sort': True}})

    result = hf.format_headers(headers)

    assert result == """HTTP/1.1 200 OK\r
Content-Length: 5\r
Content-Type: text/html; charset=UTF-8\r
\r
hello"""


# Generated at 2022-06-13 22:10:14.749157
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    def test_input_output_pair(input, output):
        """Test input, output pair."""
        headers_formatter = HeadersFormatter()
        assert headers_formatter.format_headers(input) == output

    # Empty string
    test_input_output_pair('', '')

    # Single header
    test_input_output_pair('Header: Value', 'Header: Value\r\n')

    # Multiple headers, no duplicates
    test_input_output_pair(
        'Header1: Value1\r\nHeader2: Value2\r\nHeader3: Value3\r\n',
        'Header1: Value1\r\nHeader2: Value2\r\nHeader3: Value3\r\n'
    )

    # Multiple headers, with duplicates
    test_input_output_

# Generated at 2022-06-13 22:11:08.156072
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    formatter = HeadersFormatter(format_options={'headers':{'sort':True}})

    headers = """
HTTP/1.1 200 OK\r
Content-type: application/json\r
content-length: 1000\r
Server: Microsoft-IIS/8.0\r
Pragma: no-cache\r
Content-Encoding: gzip\r
Date: Tue, 08 Mar 2016 11:50:53 GMT\r
\r
""".strip('\n')


# Generated at 2022-06-13 22:11:17.764142
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input_header = '''POST http://example.com HTTP/1.1
Accept: application/json
User-Agent: HTTPie/1.1.0
Connection: keep-alive
Accept-Encoding: gzip, deflate
Content-Length: 12
Content-Type: application/json; charset=utf-8
Host: example.com

'''
    expected_output = '''POST http://example.com HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 12
Content-Type: application/json; charset=utf-8
Host: example.com
User-Agent: HTTPie/1.1.0

'''
    formatted_header = HeadersFormatter(format_options={'headers': {'sort': True}}).format

# Generated at 2022-06-13 22:11:28.052200
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method format_headers of class HeadersFormatter

    """
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Server: Werkzeug/0.16.0 Python/3.8.0
Date: Wed, 01 Jan 2020 00:00:00 GMT
Content-Length: 5
Connection: close

{}"""
    expected = """\
HTTP/1.1 200 OK
Content-Length: 5
Content-Type: application/json; charset=utf-8
Connection: close
Date: Wed, 01 Jan 2020 00:00:00 GMT
Server: Werkzeug/0.16.0 Python/3.8.0

{}"""

# Generated at 2022-06-13 22:11:39.698988
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter_obj = HeadersFormatter()