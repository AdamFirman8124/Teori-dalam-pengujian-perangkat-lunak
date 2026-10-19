

# Generated at 2022-06-13 22:01:52.718707
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    
    hf = HeadersFormatter()

    headers = """
        Host: 127.0.0.1:8080
        Accept: */*
        Content-Type: application/x-www-form-urlencoded
        Accept-Encoding: gzip, deflate
        Transfer-Encoding: chunked
        
        """
    headers = hf.format_headers(headers)

    assert headers == """
        Host: 127.0.0.1:8080
        Accept: */*
        Accept-Encoding: gzip, deflate
        Content-Type: application/x-www-form-urlencoded
        Transfer-Encoding: chunked
        """
    print(headers)

# Generated at 2022-06-13 22:01:59.544369
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers('GET / HTTP/1.1\r\nB: 1\r\nA: 1\r\nC: 1\r\n') == \
        'GET / HTTP/1.1\r\nA: 1\r\nB: 1\r\nC: 1\r\n'

# Generated at 2022-06-13 22:02:09.369968
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h_formatter = HeadersFormatter()
    headers = """\
Content-Length: 225
Content-Type: application/json; charset=utf-8
Server: Werkzeug/0.14.1 Python/3.6.5
Date: Wed, 16 Jan 2019 08:56:10 GMT
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN

"""
    right_headers = """\
Content-Length: 225
Content-Type: application/json; charset=utf-8
Date: Wed, 16 Jan 2019 08:56:10 GMT
Server: Werkzeug/0.14.1 Python/3.6.5
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN

"""
    assert h_formatter.format_

# Generated at 2022-06-13 22:02:11.382292
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter()
    assert headers_formatter is not None


# Generated at 2022-06-13 22:02:22.299897
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter().format_headers(
        'GET / HTTP/1.1\r\n'
        'Host: localhost\r\n'
        'User-Agent: HTTPie/0.9.6\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'Accept: */*\r\n'
        '\r\n'
    )
    assert headers == (
        'GET / HTTP/1.1\r\n'
        'Accept: */*\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'Host: localhost\r\n'
        'User-Agent: HTTPie/0.9.6\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:02:32.829503
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hh1 = '''\
HTTP/1.1 200 OK
Content-type: application/json
X-Xss-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-RESPONSE: {
  "result": "OK"
}
X-Response: {
  "result": "FAILED"
}
'''

    # Sorted

# Generated at 2022-06-13 22:02:43.746573
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = formatter.format_headers(
'''\
HTTP/1.1 200 OK
Date: Thu, 13 Feb 2020 14:28:09 GMT
Server: Apache
Last-Modified: Mon, 10 Feb 2020 10:23:42 GMT
Etag: "59-5a4e4e1f673c0"
Accept-Ranges: bytes
Content-Length: 89
Connection: close
Content-Type: text/html
'''
    )

# Generated at 2022-06-13 22:02:54.449162
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from dataclasses import dataclass
    from httpie.compat import urlparse
    from httpie.context import Environment
    from os import getenv
    from httpie.environment import Environment

    @dataclass
    class TestEnv(Environment):
        stdin: object = None
        stdin_isatty: bool = None
        stdout: object = None
        stdout_isatty: bool = None
        stderr: object = None
        stderr_isatty: bool = None
        is_windows: bool = False
        is_cygwin: bool = False
        config_dir: str = ''
        config_path: str = ''
        colors: int = 256
        stdout_is_redirected: bool = False

    env = TestEnv()

# Generated at 2022-06-13 22:03:05.088135
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    data = ("foo: o\r\n"
            "Bar: Z\r\n"
            "baz: x\r\n"
            "Foo: a\r\n"
            "Baz: b\r\n"
            "Bar: y\r\n")

    expected = ("foo: o\r\n"
                "Bar: Z\r\n"
                "Bar: y\r\n"
                "Baz: b\r\n"
                "baz: x\r\n"
                "Foo: a\r\n")

    assert h.format_headers(data) == expected

# Generated at 2022-06-13 22:03:07.673593
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter()
    assert not h.enabled
    assert h is not None


# Generated at 2022-06-13 22:03:22.405808
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # This test case should pass when correct implementation
    # of method format_headers of class HeadersFormatter
    # is submitted.
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:03:35.732112
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    header_formatter = HeadersFormatter()

    # test with a header containing a capital letter
    headers = """GET / HTTP/1.1
Accept: */*
Accept_EncodiNG: gzip, deflate
Host: httpbin.org
User-Agent: HTTPie/0.9.1
"""
    assert header_formatter.format_headers(headers) == """GET / HTTP/1.1
Accept: */*
Accept_EncodiNG: gzip, deflate
Host: httpbin.org
User-Agent: HTTPie/0.9.1
"""

    # test with a header containing multiple capital letters
    headers = """GET / HTTP/1.1
Accept: application/json
User-Agent: HTTPie/0.9.1
X-API-Key: ABCDX-1234Y-DefgZ
"""


# Generated at 2022-06-13 22:03:44.903183
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    r = requests.Request('GET', 'http://httpbin.org/get',
                         headers=OrderedDict([('Foo', 'one'), ('Bar', 'two'),
                                              ('Foo', 'three')]))

    prepared_request = r.prepare()

    # httpbin returns the headers back as a string in the response
    headers = prepared_request.headers

    formatted_headers = HeadersFormatter().format_headers(headers)


# Generated at 2022-06-13 22:03:56.013327
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Connection: close\r\n'
        'Server: SimpleHTTP/0.6 Python/3.7.3\r\n'
        'Date: Wed, 26 Jul 2017 15:24:36 GMT\r\n'
        'Content-Type: text/html; charset=utf-8\r\n'
        'Content-Length: 215\r\n'
    )

# Generated at 2022-06-13 22:04:08.585598
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {
            'sort': True
        }
    })
    assert formatter.format_headers('HTTP/1.1 200 OK\r\n'
                                    'Content-Length: 10\r\n'
                                    'ABC: def\r\n'
                                    'Content-Type: qqq\r\n'
                                    'Content-Type: abc\r\n') == 'HTTP/1.1 200 OK\r\n'\
                                                                'ABC: def\r\n'\
                                                                'Content-Length: 10\r\n'\
                                                                'Content-Type: qqq\r\n'\
                                                                'Content-Type: abc\r\n'

# Generated at 2022-06-13 22:04:18.954734
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:04:21.604309
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={'headers': {'sort': True}},
                            color_options={})


# Generated at 2022-06-13 22:04:29.627742
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers("Content-Type: application/json\r\nContent-Length: 9\r\nUnex: b") == \
    "Content-Type: application/json\r\nUnex: b\r\nContent-Length: 9"
    assert HeadersFormatter().format_headers("Content-Type: application/json\r\nContent-Length: 9\r\nUnex: a\r\nUnex: b\r\nContent-Length: 10") == \
    "Content-Type: application/json\r\nUnex: a\r\nUnex: b\r\nContent-Length: 9"


# Generated at 2022-06-13 22:04:33.475405
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test sorting headers with multiple headers with the same name
    headers = '''\
GET /foo HTTP/1.1
User-Agent: httpie
Content-Type: application/json
Content-Type: text/plain
Accept-Encoding: gzip
Accept-Encoding: gzip, deflate
Host: httpbin.org'''
    expected_headers = '''\
GET /foo HTTP/1.1
Accept-Encoding: gzip
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Type: text/plain
Host: httpbin.org
User-Agent: httpie'''
    assert expected_headers == HeadersFormatter().format_headers(headers)


# Generated at 2022-06-13 22:04:43.235527
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:04:58.045851
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = "Cokkie: 111111\n" +\
        "P: 222222\n" +\
        "Cookie: 123456\n" +\
        "Cookie: 7890\n"

    expected_result = "Cokkie: 111111\n" +\
        "Cookie: 123456\n" +\
        "Cookie: 7890\n" +\
        "P: 222222"

    headers_formatter = HeadersFormatter()
    assert headers_formatter.format_headers(headers) == expected_result

# Generated at 2022-06-13 22:05:05.653752
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('\r\n'.join(
        ['head1: value1', 'head2: value2', 'head1: value3']
    )) == '\r\n'.join(
        ['head2: value2', 'head1: value1', 'head1: value3']
    )



# Generated at 2022-06-13 22:05:15.138846
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h1 = HeadersFormatter()
    h2 = HeadersFormatter(format_options={'headers':{'sort':False}})
    for hf in [h1,h2]:
        headers = '''\
GET /foo HTTP/1.1
Host: example.com
Connection: close
Accept-Encoding: compress, gzip
Cache-Control: no-cache
'''
        assert hf.format_headers(headers) == headers
        headers = '''\
GET /foo HTTP/1.1
Host: example.com
Connection: close
Accept-Encoding: compress, gzip
Cache-Control: no-cache
Accept: */*

'''

# Generated at 2022-06-13 22:05:17.582034
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter(None)
    assert headers_formatter is not None


# Generated at 2022-06-13 22:05:29.661298
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:05:40.724357
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # test_case_1
    headers_1 = '''\
POST /post HTTP/1.1
Accept: */*
Host: example.org
X-Custom-Header: Custom header
X-Custom-Header: Custom header (2)
Content-Length: 13
Content-Type: application/x-www-form-urlencoded'''

    # test_case_2
    headers_2 = '''\
POST /post HTTP/1.1
Content-Length: 13
Accept: */*
X-Custom-Header: Custom header
X-Custom-Header: Custom header (2)
Host: example.org
Content-Type: application/x-www-form-urlencoded'''

    # target

# Generated at 2022-06-13 22:05:49.534200
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(options={})
    formatted_data = formatter.format_headers("""\
HTTP/1.1 200 OK
Content-Length: 131
Content-Type: application/json; charset=utf-8
Server: Werkzeug/0.14.1 Python/3.4.4""")
    assert formatted_data == """\
HTTP/1.1 200 OK
Content-Length: 131
Content-Type: application/json; charset=utf-8
Server: Werkzeug/0.14.1 Python/3.4.4"""

# Integration test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:05:55.063610
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert 'Foo: 1\r\nBar: 2\r\nBaz: 3' == HeadersFormatter().format_headers('\r\nFoo: 1\r\nBaz: 3\r\nBar: 2\r\n')

# argparse helper methods

# Generated at 2022-06-13 22:06:05.955247
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = formatter.format_headers("""
HTTP/1.1 200 OK
Content-type: application/json; charset=utf-8
Content-Encoding: gzip
Vary: Accept-Encoding
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: e99aec37-856a-48fb-b557-932d95924957
X-Runtime: 0.127906""")

# Generated at 2022-06-13 22:06:08.565512
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled == formatter.format_options['headers']['sort']


# Generated at 2022-06-13 22:06:28.559287
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    test method format_headers of class HeadersFormatter
    """
    headers_formatter = HeadersFormatter()
    headers = 'HTTP/1.1 200 OK\r\n' \
              'Content-Type: application/json; charset=utf-8\r\n' \
              'Server: WSGIServer/0.2 CPython/3.5.2\r\n' \
              'Date: Sun, 11 Dec 2016 06:22:30 GMT\r\n' \
              'Content-Length: 269\r\n\r\n'

# Generated at 2022-06-13 22:06:38.627691
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hm = HeadersFormatter()
    response_headers = b'''\
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 06 May 2020 12:37:26 GMT
Content-Type: application/json
Content-Length: 1968
Connection: keep-alive
Content-Disposition: attachment; filename="contacts"
X-Powered-By: PHP/7.3.20
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Link: <https://api.byteplant.com/v1/contacts?per_page=100&page=2>; rel="next"
'''

# Generated at 2022-06-13 22:06:47.850687
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers':{'sort': True}})
    headers = """\
POST / HTTP/1.1
Host: example.org
Connection: keep-alive
Content-Length: 112
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept-Language: en-US,en;q=0.8
Accept-Encoding: gzip, deflate
Accept: */*
Referer: http://example.org/login
Cookie: key1=val1; key2=val2
"""

# Generated at 2022-06-13 22:06:59.528386
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hdr = """\r\n
Connection: keep-alive\r\n
Accept-Encoding: gzip, deflate\r\n
Accept: */*\r\n
User-Agent: HTTPie/1.0.0\r\n
Accept-Language: zh-cn\r\n
"""
    hdr_sorted = """\r\n
Accept: */*\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: zh-cn\r\n
Connection: keep-alive\r\n
User-Agent: HTTPie/1.0.0\r\n
"""
    assert hdr_sorted == hf.format_headers(hdr)

# Generated at 2022-06-13 22:07:10.650780
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 9
Content-Type: application/json
X-Powered-By: Express
Date: Thu, 26 Oct 2017 15:48:34 GMT
Server: nginx/1.12.1
Strict-Transport-Security: max-age=15724800; includeSubDomains


"""

# Generated at 2022-06-13 22:07:14.057148
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter is not None
    assert issubclass(HeadersFormatter, FormatterPlugin)
    assert hasattr(HeadersFormatter, '__init__')

# Generated at 2022-06-13 22:07:22.966588
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.0 200 OK
Content-Type: text/html
Cache-Control: max-age=3600
Content-Language: en
Server: BaseHTTP/0.3 Python/3.4.3

<p>Hello, world</p>
'''
    expected_result = '''\
HTTP/1.0 200 OK
Content-Language: en
Content-Type: text/html
Cache-Control: max-age=3600
Server: BaseHTTP/0.3 Python/3.4.3

<p>Hello, world</p>
'''
    assert formatter.format_headers(headers) == expected_result



# Generated at 2022-06-13 22:07:34.106510
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''
    GET / HTTP/1.1
    User-Agent: httpie
    Accept-Encoding: gzip, deflate
    Accept: */*
    Host: localhost
    Content-Type: application/x-www-form-urlencoded
    Connection: keep-alive
    Content-Length: 17
    '''
    expected = '''
    GET / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Length: 17
    Content-Type: application/x-www-form-urlencoded
    Host: localhost
    User-Agent: httpie
    '''

    headers_formatter = HeadersFormatter()
    result = headers_formatter.format_headers(headers)
    assert result == expected



# Generated at 2022-06-13 22:07:42.941901
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = formatter.format_headers('GET / HTTP/1.1\r\n'
                                       'Connection: keep-alive\r\n'
                                       'Accept: text/html\r\n'
                                       'Accept-Encoding: gzip\r\n'
                                       'Accept: application/json\r\n')
    assert headers == ('GET / HTTP/1.1\r\n'
                       'Accept: text/html\r\n'
                       'Accept: application/json\r\n'
                       'Accept-Encoding: gzip\r\n'
                       'Connection: keep-alive\r\n')



# Generated at 2022-06-13 22:07:47.449587
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = """\
POST / HTTP/1.1
Content-Type: application/json
B: bbb
A: aaa
"""
    assert hf.format_headers(headers) == """\
POST / HTTP/1.1
A: aaa
B: bbb
Content-Type: application/json
"""


# Generated at 2022-06-13 22:08:10.931506
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    # input string h with headers in random order 

# Generated at 2022-06-13 22:08:21.052132
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    str_headers = """
    POST /args HTTP/1.1
    Authorization: Basic Zm9vOmJhcg==
    Content-Length: 7
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    User-Agent: HTTPie/0.9.9
    X-Amzn-Trace-Id: Root=1-5f4cf873-7cae4d07b0edf9841fa8d8fa
    """

# Generated at 2022-06-13 22:08:26.691515
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = """\
HTTP/1.1 302 Moved Temporarily
Location: http://httpbin.org/get
Content-Length: 0
"""
    assert f.format_headers(headers) == headers



# Generated at 2022-06-13 22:08:36.387078
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_string = ByteString('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Server: example.com',
        'Foo: 1',
        'Bar: 1',
        'Bar: 2',
        'Foo: 1',
        'Foo: 2',
        'Bar: 1',
        'Foo: 1',
        'Bar: 2',
        'Foo: 1',
        'Foo: 2',
        'Bar: 3',
        'Bar: 1',
        'Bar: 2',
        'Foo: 1',
    ]))


# Generated at 2022-06-13 22:08:43.454071
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
  lines = ['GET / HTTP/1.1', 'Host: example.org', 'User-Agent: httpie', 'Accept: */*', 'Accept-Encoding: gzip, deflate', 'Connection: keep-alive']
  expected = ['Accept: */*', 'Accept-Encoding: gzip, deflate', 'Connection: keep-alive', 'Host: example.org', 'User-Agent: httpie']
  result = HeadersFormatter()
  assert expected == result.format_headers('\r\n'.join(lines)).strip().split('\r\n')


# Generated at 2022-06-13 22:08:52.130151
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    def check(input, output, **kwargs):
        ff = HeadersFormatter(**kwargs)
        assert ff.format_headers(input) == output

    # Test case 1
    input = '''\
POST / HTTP/1.1
Accept-Encoding: gzip, deflate
X-header: value1, value2
Content-Type: application/json
Connection: close
Host: httpbin.org
Content-Length: 2
X-header: value3
User-Agent: HTTPie/0.9.8
'''

# Generated at 2022-06-13 22:09:00.992928
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    headers_input = '''\
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed'''
    headers_expected = '''\
HTTP/1.1 200 OK
Connection: Closed
Content-Length: 88
Content-Type: text/html
Date: Mon, 27 Jul 2009 12:28:53 GMT
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Server: Apache/2.2.14 (Win32)
'''
    headers_actual = fmt.format_headers(headers_input)
    assert headers_expected == headers_actual

# Generated at 2022-06-13 22:09:07.103774
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter()
    input_str = "HTTP/1.1 200 OK\r\nX-Test: foo\r\nX-Test: bar\r\nX-Test: baz\r\nX-Test: qux"
    expected_output = "HTTP/1.1 200 OK\r\nX-Test: foo\r\nX-Test: bar\r\nX-Test: baz\r\nX-Test: qux"
    assert headers.format_headers(input_str) == expected_output

# Generated at 2022-06-13 22:09:13.880904
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    h1 = 'Content-Length: 0\r\n'
    h2 = 'Date: Mon, 24 Jun 2019 19:34:35 GMT\r\n'
    h3 = 'Content-Type: text/plain\r\n'
    s = '{}{}{}'.format(h1, h2, h3)
    assert formatter.format_headers(s) == '{}{}{}'.format(h2, h3, h1)



# Generated at 2022-06-13 22:09:22.315329
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    On this test will get headers that should be unchanged
    """
    hf = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json\r\n'
        'Connection: close\r\n'
        'Transfer-Encoding: chunked\r\n'
        'Server: gunicorn/19.9.0\r\n'
        'Date: Thu, 05 Dec 2019 00:21:41 GMT\r\n')
    formatted_headers = hf.format_headers(headers)
    assert headers == formatted_headers


# Generated at 2022-06-13 22:09:42.789197
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from httpie.core import parser, formatter
    from httpie.plugins import builtin, manager
    from httpie.plugins.manager import LOGGING_PLUGIN_NAME, FORMATTERS_PLUGIN_NAME, FORMATS_PLUGIN_NAME

    parser_ = parser.Parser().build()
    formatter_ = formatter.Formatter(parser_)
    manager_ = manager.PluginManager(plugin_names=[FORMATS_PLUGIN_NAME, FORMATTERS_PLUGIN_NAME, LOGGING_PLUGIN_NAME])


# Generated at 2022-06-13 22:09:56.796462
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method HeadersFormatter.format_headers()
    """
    test_input = '\r\n'.join(['POST / HTTP/1.1',
                              'User-Agent: httpie.py',
                              'AAA: bbb',
                              'Content-Type: application/json',
                              'Content-Length: 17',
                              'Host: localhost:8080',
                              'Accept-Encoding: gzip, deflate',
                              'Accept: */*',
                              'Connection: keep-alive',
                              ])

# Generated at 2022-06-13 22:10:08.058699
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        textwrap.dedent("""\
        POST /post HTTP/1.1
        User-Agent: HTTPie/0.9.2
        Accept-Encoding: gzip, deflate
        Accept: */*
        Content-Type: application/json
        Content-Length: 10

        b'{"key": "val"}'""")
    ) == textwrap.dedent("""\
        POST /post HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Content-Length: 10
        Content-Type: application/json
        User-Agent: HTTPie/0.9.2

        b'{"key": "val"}'""")

# Generated at 2022-06-13 22:10:12.407452
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    s = HeadersFormatter(format_options={'headers':{'sort':True}})
    assert s.enabled == True
    assert s.format_options['headers']['sort'] == True


# Generated at 2022-06-13 22:10:23.317336
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter(options={}).format_headers('Accept: application/json\r\nUser-Agent: HTTPie/0.9.9') == 'Accept: application/json\r\nUser-Agent: HTTPie/0.9.9'
    assert HeadersFormatter(options={}).format_headers('User-Agent: HTTPie/0.9.9\r\nAccept: application/json') == 'Accept: application/json\r\nUser-Agent: HTTPie/0.9.9'

# Generated at 2022-06-13 22:10:28.751100
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('Content-Type: a\r\nContent-Length: b\r\n') == 'Content-Type: a\r\nContent-Length: b\r\n'

# Generated at 2022-06-13 22:10:39.704636
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Parameters:
    :headers: string of headers
    """
    headers = (
        "GET / HTTP/1.1\r\n"
        "User-Agent: curl/7.64.0\r\n"
        "Host: httpbin.org\r\n"
        "Accept: */*\r\n"
        "Content-Type: application/json\r\n"
    )
    def _test_headers_sort(headers):
        """
        Parameters:
        :headers: string of headers
        """
        formatter = HeadersFormatter()
        actual = formatter.format_headers(headers)

# Generated at 2022-06-13 22:10:41.756585
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled

# Generated at 2022-06-13 22:10:51.036934
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """GET / HTTP/1.1
User-Agent: HTTPie/1.0.2
Accept-Encoding: gzip, deflate
Accept: */*
Host: httpbin.org
Content-Length: 35

"""
    exp_headers = """GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Content-Length: 35
Host: httpbin.org
User-Agent: HTTPie/1.0.2

"""
    assert formatter.format_headers(headers) == exp_headers

# Generated at 2022-06-13 22:11:01.595327
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('Host: host\r\nAccept: child') == 'Host: host\r\nAccept: child'
    assert HeadersFormatter().format_headers('Accept: child\r\nHost: host') == 'Host: host\r\nAccept: child'
    assert HeadersFormatter().format_headers('Accept: child\r\nHost: host\r\nAccept: child') == 'Host: host\r\nAccept: child\r\nAccept: child'
    assert HeadersFormatter().format_headers('Accept: child\r\nHost: host\r\nAccept: child\r\nAccept: child') == 'Host: host\r\nAccept: child\r\nAccept: child\r\nAccept: child'

# Generated at 2022-06-13 22:11:33.129150
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers_unformatted = """\
HTTP/1.1 300 MULTIPLE CHOICES
Date: Fri, 19 Oct 2012 07:54:00 GMT
Server: Apache
Vary: Accept-Encoding
Content-Type: text/html; charset=iso-8859-1
Location: http://www.iana.org/domains/example/
Content-Length: 236"""
    headers_formatted = formatter.format_headers(headers_unformatted)
    lines = headers_formatted.splitlines()
    assert lines[1][:6] == 'Date: '
    assert lines[2][:8] == 'Server: '
    assert lines[3][:6] == 'Vary: '
    assert lines[4][:13] == 'Content-Type: '

# Generated at 2022-06-13 22:11:41.752226
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nCookie: cookie2=qwer\r\nCookie: cookie1=asdf\r\n\r\n'
    result = formatter.format_headers(headers)
    assert result == 'HTTP/1.1 200 OK\r\nCookie: cookie2=qwer\r\nCookie: cookie1=asdf\r\nContent-Type: application/json\r\n\r\n'
