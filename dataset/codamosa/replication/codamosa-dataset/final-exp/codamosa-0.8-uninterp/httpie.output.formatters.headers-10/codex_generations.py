

# Generated at 2022-06-13 22:01:54.173923
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fake_format_options = {'headers': {'sort': True}}
    formatter = HeadersFormatter(**fake_format_options)
    headers_str_1 = (
        "HTTP/1.1 200 OK\r\n"
        "Accept-Encoding: identity\r\n"
        "Content-Type: application/json\r\n"
        "Server: gunicorn/19.9.0\r\n"
        "Date: Tue, 16 Jul 2019 13:02:10 GMT\r\n"
    )

# Generated at 2022-06-13 22:02:06.391128
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    unformatted = """\
HTTP/1.1 200 OK
Date: Sat, 25 Jul 2020 21:15:02 GMT
Server: Apache/2.4.10 (Debian)
Last-Modified: Fri, 24 Jul 2020 01:01:49 GMT
ETag: "1f9-592f77b56d7c1"
Accept-Ranges: bytes
Content-Length: 503
Content-Type: text/html"""

# Generated at 2022-06-13 22:02:16.227737
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:02:24.390359
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    plugin = HeadersFormatter()
    headers = (
        "HTTP/1.1 301 Moved Permanently\r\n"
        "Server: nginx/1.4.6 (Ubuntu)\r\n"
        "Date: Sun, 13 Jul 2014 15:36:17 GMT\r\n"
        "Content-Type: text/html\r\n"
        "Content-Length: 193\r\n"
        "Connection: keep-alive\r\n"
        "Location: http://httpbin.org/get"
    )

# Generated at 2022-06-13 22:02:33.946831
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''User-Agent: httpie
Content-Type: application/json
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
Host: 10.211.55.3:8090
Content-Length: 2
X-Forwarded-Proto: http
X-Forwarded-Port: 8090
Cache-Control: no-cache
Postman-Token: ee6b7f30-566f-4d8b-a6ce-db633129dca3
X-Forwarded-For: 10.211.55.3
'''

# Generated at 2022-06-13 22:02:38.194204
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    options = {'headers': {'sort': True}}
    headersFormatter = HeadersFormatter(format_options=options)
    assert(headersFormatter.enabled == options['headers']['sort'])
    assert(headersFormatter.format_options == options)


# Generated at 2022-06-13 22:02:48.421261
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test_HeadersFormatter = HeadersFormatter()
    assert test_HeadersFormatter.format_headers(
        'Content-Type: application/json\n'
        'Content-Type: text/plain; charset=utf-8\n'
        'X-Powered-By: Test\r\n'
        'X-Foo: Baz\r\n'
        'X-Bar: Qux\r\n'
        'X-Bar: Fux\r\n'
    ) == '''Content-Type: application/json
Content-Type: text/plain; charset=utf-8
X-Bar: Qux
X-Bar: Fux
X-Foo: Baz
X-Powered-By: Test'''



# Generated at 2022-06-13 22:02:56.620173
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    #if __name__ == '__main__':
    test_input = '''
        HTTP/1.1 200 OK
        Content-Type: application/json
        Date: Mon, 25 Sep 2017 02:10:36 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Vary: Accept-Encoding,User-Agent
        X-Powered-By: PHP/7.1.3
        Allow: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
        Content-Length: 232
        Connection: close
    '''

# Generated at 2022-06-13 22:03:02.449933
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test method format_headers of class HeadersFormatter
    """
    fmt = HeadersFormatter()
    headers = fmt.format_headers("""HTTP/1.1 200 OK\r
Content-Length: 46\r
\r
""")
    assert("Content-Length: 46" in headers)


# Generated at 2022-06-13 22:03:10.441628
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    str_headers = '''\
GET / HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: HTTPie/1.0.0-dev

    '''
    headers_object = HeadersFormatter()
    assert headers_object.format_headers(str_headers) == '''\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Host: httpbin.org
User-Agent: HTTPie/1.0.0-dev

    '''

# Generated at 2022-06-13 22:03:22.357891
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-type: text/html;charset=utf-8
Date: Tue, 19 Nov 2019 08:23:20 GMT
Transfer-encoding: chunked
Server: nginx
X-Cache: HIT
Connection: keep-alive
X-Cache: HIT
X-Cache: HIT
"""
    assert headers_formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
Content-type: text/html;charset=utf-8
Date: Tue, 19 Nov 2019 08:23:20 GMT
Transfer-encoding: chunked
Server: nginx
X-Cache: HIT
X-Cache: HIT
X-Cache: HIT
Connection: keep-alive
"""

# Generated at 2022-06-13 22:03:35.672868
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:44.830375
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Connection: keep-alive
Transfer-Encoding: chunked
Content-Type: application/json
Vary: Accept, Cookie
Content-Encoding: gzip
Date: Thu, 27 Jun 2019 06:55:48 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Via: 1.1 varnish
Age: 0
X-Served-By: cache-sin18025-SIN
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1561607348.624773,VS0,VE637
Vary: Accept-Encoding
'''

    headers_formatted = formatter.format_headers(headers)
    headers_form

# Generated at 2022-06-13 22:03:54.293894
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hd = HeadersFormatter(format_options={'headers': {'sort':True}})
    headers = '''\
HTTP/1.1 200 OK
Content-Length: 20
X-Foo: foofoofoo
X-Bar: barbarbar
Connection: Keep-Alive
X-Foo: barbarbar
'''
    expect_headers = '''\
HTTP/1.1 200 OK
Content-Length: 20
X-Bar: barbarbar
X-Foo: foofoofoo
X-Foo: barbarbar
Connection: Keep-Alive
'''
    assert hd.format_headers(headers) == expect_headers



# Generated at 2022-06-13 22:04:02.067032
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    headers The headers in key: value form.
    """
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-Length: 123
Host: example.org
Etag: "a35e2a8"
Accept: text/html, */*
User-Agent: curl/7.65.3
"""
    assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
Accept: text/html, */*
Content-Length: 123
Etag: "a35e2a8"
Host: example.org
User-Agent: curl/7.65.3
"""

# Generated at 2022-06-13 22:04:03.749290
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers = HeadersFormatter()
    assert headers.enabled == False


# Generated at 2022-06-13 22:04:12.143101
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(
        format_options={'headers': {'sort': True}})

    headers = '''
HTTP/1.1 200 OK
Server: Apache
Content-Length: 46297
Connection: close
Content-Type: text/html
Date: Sat, 17 Jun 2017 18:00:34 GMT

'''

    assert headers_formatter.format_headers(headers) == '''
HTTP/1.1 200 OK
Content-Length: 46297
Content-Type: text/html
Connection: close
Date: Sat, 17 Jun 2017 18:00:34 GMT
Server: Apache

'''

# Generated at 2022-06-13 22:04:26.122301
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    s = hf.format_headers("""HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: close
Content-Length: 21
Content-Type: text/plain; charset=utf-8
Date: Xxx, XX Xxx XXXX XX:XX:XX GMT
Last-Modified: Xxx, XX Xxx XXXX XX:XX:XX GMT
Server: TestServer/0.1 Python/3.8.1
X-Test: 1
X-Test: 2
X-Test: 3
""")

# Generated at 2022-06-13 22:04:36.518747
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter()
    headers_str = '''
HTTP/1.0 200 OK
Accept: */*
Content-Length: 65
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Cache-Control: no-cache
'''
    correct_headers_str = '''
HTTP/1.0 200 OK
Accept: */*
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 65
Content-Type: application/json; charset=utf-8
'''
    assert headers.format_headers(headers_str) == correct_headers_str


# Generated at 2022-06-13 22:04:48.604213
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # create HeaderFormatter object
    line1 = 'GET http://httpbin.org/ Response'
    line2 = 'HTTP/1.1 200 OK'
    line3 = 'Connection: keep-alive'
    line4 = 'Content-Encoding: gzip'
    line5 = 'Content-Type: application/json'
    line6 = 'Date: Thu, 22 Aug 2019 11:24:42 GMT'
    line7 = 'Server: gunicorn/19.9.0'
    line8 = 'Transfer-Encoding: chunked'
    line9 = 'Via: 1.1 vegur'
    http_line = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 + '\n' + line

# Generated at 2022-06-13 22:05:00.500579
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """\
Accept: text/html
Accept-Language: en-US,en;q=0.8
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
User-Agent: HTTPie/0.9.2
"""
    assert headers_formatter.format_headers(headers) == """\
Accept: text/html
Accept-Language: en-US,en;q=0.8
Cache-Control: max-age=0
Content-Type: application/x-www-form-urlencoded
User-Agent: HTTPie/0.9.2
"""



# Generated at 2022-06-13 22:05:10.417496
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options = {'headers': {'sort': True}})
    assert(formatter.format_headers("""
GET / HTTP/1.1
Host: httpbin.org
Connection: keep-alive
User-Agent: HTTPie/0.9.3
Accept: */*
Accept-Encoding: gzip, deflate, identity
Content-Type: application/json

    """) == """
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, identity
Content-Type: application/json
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.3
    """)


# Generated at 2022-06-13 22:05:16.990122
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = \
'''

Connection: Keep-Alive\r
Connection: Upgrade\r
Content-Length: 5\r
Content-Length: 5\r
Content-Length: 5\r
Content-Type: application/json\r
\r
'''

    expected_output = \
'''

Connection: Keep-Alive\r
Connection: Upgrade\r
Content-Length: 5\r
Content-Length: 5\r
Content-Length: 5\r
Content-Type: application/json\r
\r
'''

    assert HeadersFormatter().format_headers(headers) == expected_output

# Generated at 2022-06-13 22:05:29.257284
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    string = """\
Content-Type: text/json; charset=utf-8
Content-Length: 83
X-RateLimit-Remaining: 60
X-RateLimit-Reset: 1522219200
X-RateLimit-Limit: 60
X-RateLimit-Reset: 1522219200
ETag: "f2646a7c8d1eaa0eafb943d6fdea6e1a"
Date: Mon, 19 Feb 2018 17:41:57 GMT
X-RateLimit-Limit: 60"""

# Generated at 2022-06-13 22:05:35.072827
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test = HeadersFormatter()
    assert test.format_headers("GET / HTTP/1.1\r\nHost: www.github.com\r\nAccept: */*\r\n") == "GET / HTTP/1.1\r\nAccept: */*\r\nHost: www.github.com\r\n"

# Generated at 2022-06-13 22:05:37.325637
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter()
    assert not hf.enabled


# Generated at 2022-06-13 22:05:48.860312
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.0 200 OK
Server: nginx
Content-Type: application/json
Vary: Accept
Allow: GET, POST, OPTIONS

'''
    assert formatter.format_headers(headers) == '''\
HTTP/1.0 200 OK
Allow: GET, POST, OPTIONS
Content-Type: application/json
Server: nginx
Vary: Accept

'''


# Monkey patch cls.format to replace the first argument (self) with the new
# HeadersFormatter class. Note that the changes here are global and not
# compatible with other plugins that change the format method.
httpie.output.format._cls.format = classmethod(
    lambda cls, **kwargs: HeadersFormatter(**kwargs).format
)

# Generated at 2022-06-13 22:05:56.092926
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
        headers = HeadersFormatter()
        input = '''
        content-length: 12
        date: Sun, 05 Jul 2015 16:38:44 GMT
        server: Example
        '''
        expected = '''
        date: Sun, 05 Jul 2015 16:38:44 GMT
        content-length: 12
        server: Example
        '''
        assert headers.format_headers(input) == expected


# Generated at 2022-06-13 22:05:59.007365
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    header = HeadersFormatter()
    assert header is not None


# Generated at 2022-06-13 22:06:07.820694
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers_string = "GET / HTTP/1.1\n" \
                     "Accept: */*\n" \
                     "Accept-Encoding: gzip, deflate\n" \
                     "Connection: keep-alive\n" \
                     "Host: httpbin.org\n" \
                     "User-Agent: HTTPie/0.9.9\n"

    sorted_headers_string = "GET / HTTP/1.1\n" \
                            "Accept: */*\n" \
                            "Accept-Encoding: gzip, deflate\n" \
                            "Connection: keep-alive\n" \
                            "Host: httpbin.org\n" \
                            "User-Agent: HTTPie/0.9.9\n"


# Generated at 2022-06-13 22:06:16.509609
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    instance = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Length: 35
Content-Type: application/json
Date: Thu, 03 Aug 2017 16:45:24 GMT
Server: TornadoServer/5.0.2
'''
    expected = '''\
HTTP/1.1 200 OK
Content-Length: 35
Content-Type: application/json
Date: Thu, 03 Aug 2017 16:45:24 GMT
Server: TornadoServer/5.0.2
'''
    instance.enabled = True
    actual = instance.format_headers(headers)
    assert actual == expected


# Generated at 2022-06-13 22:06:26.671985
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    The headers of a request/response are sorted by name,
    with multiple headers with the same name still in
    their relative order.

    """
    headers = "GET / HTTP/1.1\r\n" \
              "Host: httpbin.org\r\n" \
              "Accept-Encoding: gzip, deflate\r\n" \
              "Connection: keep-alive\r\n" \
              "Accept: */*\r\n" \
              "User-Agent: HTTPie/1.0.3\r\n" \
              "Content-Length: 0\r\n"


# Generated at 2022-06-13 22:06:37.670355
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    https://github.com/jakubroztocil/httpie/blob/master/tests/test_plugins.py
    """

    # test sample:
    #  request:
    #      GET / HTTP/1.1
    #      User-Agent: HTTPie/0.9.2
    #      Accept-Encoding: gzip, deflate, compress
    #      Accept: text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8
    #      Foo: bar
    #      Foo: baz
    #      Foo: quux
    #      Content-Type: application/json
    #      Content-Length: 12
    #  response:
    #    HTTP/1.1 200 OK
    #    Server: TornadoServer/4.2.

# Generated at 2022-06-13 22:06:40.008594
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    r1 = HeadersFormatter({'headers':{'sort': True}})
    assert r1.enabled == True
    r2 = HeadersFormatter({'headers':{'sort': False}})
    assert r2.enabled == False


# Generated at 2022-06-13 22:06:50.537118
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers("""HTTP/1.1 200 OK
Date: Sun, 19 Mar 2017 23:52:17 GMT
Server: Apache/2.4.7
Content-Length: 609
Connection: close
Content-Type: text/html; charset=UTF-8

""") == """HTTP/1.1 200 OK
Connection: close
Content-Length: 609
Content-Type: text/html; charset=UTF-8
Date: Sun, 19 Mar 2017 23:52:17 GMT
Server: Apache/2.4.7

"""


# Generated at 2022-06-13 22:07:00.506057
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers(): 
    _headers = '''\
HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/19.9.0
Date: Fri, 28 Sep 2018 16:28:33 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 45617
Vary: Cookie
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Via: 1.1 vegur
Alter: Welcome to the 1st HTTPBin!
'''

# Generated at 2022-06-13 22:07:10.744823
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
User-Agent: HTTPie/0.9.2


'''.lstrip()

    headers_sorted = '''\
Host: httpbin.org
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
User-Agent: HTTPie/0.9.2

'''.lstrip()

    f = HeadersFormatter()
    f.format_options['headers']['sort'] = True
    assert f.format_headers(headers) == headers_sorted
    f.format_options['headers']['sort'] = False
    assert f.format_headers(headers) == headers

# Generated at 2022-06-13 22:07:12.103790
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    HeadersFormatter()


# Generated at 2022-06-13 22:07:22.448570
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    input_string = 'HTTP/1.1 200 OK\r\bContent-Type: text/html\r\nContent-Length: 0\r\nX-Id: 1\r\nX-Id: 2\r\nContent-Length: 4\r\n'
    expected_output_string = 'HTTP/1.1 200 OK\r\bContent-Length: 0\r\nContent-Length: 4\r\nContent-Type: text/html\r\nX-Id: 1\r\nX-Id: 2\r\n'
    actual_output_string = headers_formatter.format_headers(input_string)
    assert expected_output_string == actual_output_string

# Generated at 2022-06-13 22:07:34.072567
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    received = "Accept-Encoding: gzip, deflate\r\nConnection: keep-alive\nContent-Length: 0\r\nContent-Type: text/html; charset=utf-8\r\nDate: Sun, 05 Jul 2020 16:55:19 GMT\r\nServer: gunicorn/19.10.0\r\nVia: 1.1 vegur\r\nX-Powered-By: Flask\r\n\r\n"

# Generated at 2022-06-13 22:07:46.056888
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:53.582352
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(auth=None,
                                 format_options={'headers': {'sort': True}},
                                 is_windows=False)
    assert formatter.enabled is True
    assert formatter.auth is None
    assert formatter.format_options == {'headers': {'sort': True}}
    assert formatter.is_windows is False

# Unit tests for formatting headers

# Generated at 2022-06-13 22:08:01.223230
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test case for method format_headers of class HeadersFormatter.

    """
    # Case 1: All uppercase
    headers = "GET / HTTP/1.1\r\nHOST: example.org\r\nCONTENT-TYPE: application/json\r\nCONTENT-LENGTH: 11\r\n\r\nA=1; A=2; A=3"
    headers = HeadersFormatter().format_headers(headers)
    assert headers == "GET / HTTP/1.1\r\nCONTENT-LENGTH: 11\r\nCONTENT-TYPE: application/json\r\nHOST: example.org\r\n\r\nA=1; A=2; A=3"

    # Case 2: All lowercase

# Generated at 2022-06-13 22:08:05.752338
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    #Assert that it isn't enabled and the format options are default
    testObj = HeadersFormatter()

    assert testObj.enabled == False
    assert testObj.format_options == {'headers': {'sort': False}}


# Generated at 2022-06-13 22:08:12.706378
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:08:22.203806
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    print("test_HeadersFormatter_format_headers")
    formatter = HeadersFormatter()
    headers = "\r\n".join([
        'HTTP/1.1 200 OK',
        'Connection: keep-alive',
        'Content-Length: 5',
        'Content-Type: application/json',
        'Date: Mon, 03 Jul 2017 13:25:21 GMT',
        'Server: gunicorn/19.6.0',
        'Via: 1.1 vegur'
    ])
    formatted_headers = formatter.format_headers(headers)

# Generated at 2022-06-13 22:08:32.021083
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method format_headers of class HeadersFormatter

    :return:
    """
    formatter = HeadersFormatter(**{
        "format_options": {
            "headers": {
                "sort": True
            }
        }
    })
    input_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
    expected_output_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
    assert formatter.format_headers(input_headers) == expected_output_headers


# Generated at 2022-06-13 22:08:33.381710
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter()


# Generated at 2022-06-13 22:08:43.934855
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    class MyHeadersFormatter(HeadersFormatter):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.enabled = self.format_options['headers']['sort']

    myformatter = MyHeadersFormatter(format_options={'headers': {'sort': True}})

# Generated at 2022-06-13 22:08:50.315394
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from io import StringIO
    from httpie.plugins.builtin import HeadersFormatter
    formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\nUser-Agent: httpie\r\nContent-Type: application/json\r\n"
    sortedHeaders = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nUser-Agent: httpie\r\n"
    result = formatter.format_headers(headers)
    assert result == sortedHeaders

