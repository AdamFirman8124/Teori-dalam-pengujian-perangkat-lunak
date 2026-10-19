

# Generated at 2022-06-13 22:01:54.288302
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    >>> # Create headers from string with method format_headers
    >>> from httpie.plugins.headers import HeadersFormatter
    >>> headers = HeadersFormatter()
    >>> headers_string = 'HTTP/1.1 200 OK\\r\\nContent-Length: 3\\r\\nContent-type: text/html\\r\\n\\r\\n<h1>All is well!</h1>'
    >>> headers.format_headers(headers_string)
    'HTTP/1.1 200 OK\\r\\nContent-Length: 3\\r\\nContent-type: text/html\\r\\n\\r\\n<h1>All is well!</h1>'
    """

# Generated at 2022-06-13 22:02:01.892875
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(headers={'sort': True})
    headers = 'HTTP/1.1 200 OK\r\nContent-type: application/json\r\nServer: nginx\r\nX-Powered-By: Python\r\n\r\n'
    print(hf.format_headers(headers))

if __name__ == '__main__':
    test_HeadersFormatter_format_headers()

# Generated at 2022-06-13 22:02:18.365212
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers(): 
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:02:27.559402
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter({})
    headers = "HTTP/1.1 200 OK\r\n" + \
              "Content-Type: application/json\r\n" + \
              "X-Header: foo\r\n" + \
              "X-Header: bar\r\n" + \
              "X-Header2: foo\r\n" + \
              "X-Header2: bar\r\n"

# Generated at 2022-06-13 22:02:38.280603
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hfmt = HeadersFormatter()
    headers = """HTTP/1.1 200 OK\r
Date: Thu, 15 Aug 2019 12:19:35 GMT\r
Expires: -1\r
Cache-Control: private, max-age=0\r
Content-Type: text/html; charset=UTF-8\r
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r
Server: gws\r
X-XSS-Protection: 0\r
X-Frame-Options: SAMEORIGIN\r
\r
Content-Length: 0\r
"""
    formatted_headers = hfmt.format_headers(headers)

# Generated at 2022-06-13 22:02:43.132224
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = """GET /some/resource HTTP/1.1
Host: www.github.com
Content-Type: application/json
Cookie: aaa=1; bbb=2
Cookie: ccc=3; ddd=4
"""
    expected = """GET /some/resource HTTP/1.1
Content-Type: application/json
Cookie: aaa=1; bbb=2
Cookie: ccc=3; ddd=4
Host: www.github.com
"""

    f = HeadersFormatter()
    result = f.format_headers(h)
    assert result == expected

# Generated at 2022-06-13 22:02:52.883238
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
  headers = "HTTP/1.1 200 OK\r\nSet-Cookie: foo\r\nSet-Cookie: bar\r\nContent-Type: application/json; charset=utf-8\r\n\r\n"
  formatter = HeadersFormatter()
  formatted_headers = formatter.format_headers(headers)
  expected_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\nSet-Cookie: foo\r\nSet-Cookie: bar\r\n\r\n"
  assert formatted_headers == expected_headers

# Generated at 2022-06-13 22:03:01.056166
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:10.347071
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter.format_headers
    assert f('GET / HTTP/1.1\r\nUser-Agent: httpie\r\nContent-Type: text/html\r\n\r\n') == \
    ('GET / HTTP/1.1\r\n'
    'Content-Type: text/html\r\n'
    'User-Agent: httpie\r\n\r\n')

# Generated at 2022-06-13 22:03:14.191747
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert 'headers' in formatter.format_options
    assert formatter.format_options['headers']['sort']



# Generated at 2022-06-13 22:03:24.824364
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fh = HeadersFormatter()

# Generated at 2022-06-13 22:03:30.331599
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatterHeaders = HeadersFormatter(raw_output=True)
    assert formatterHeaders.__class__ == HeadersFormatter
    assert formatterHeaders.__module__ == 'httpie.plugins.sort'
    assert formatterHeaders.raw_output


# Generated at 2022-06-13 22:03:35.914430
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Length: 23
Content-Type: application/json
Accept: application/json
'''
    expected_headers = '''\
Content-Length: 23
Accept: application/json
Content-Type: application/json
'''
    assert HeadersFormatter.format_headers(headers) == expected_headers



# Generated at 2022-06-13 22:03:44.972039
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatted = HeadersFormatter().format_headers(
        '''\
HTTP/1.1 200 OK
Server: nginx
Content-Type: text/html; charset=utf-8
Vary: Origin
Vary: X-HTTP-Method-Override
Vary: Accept-Encoding
Content-Length: 145
Connection: keep-alive
Date: Thu, 08 Dec 2016 17:40:03 GMT
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000
Allow: GET, POST, PUT, DELETE, HEAD, OPTIONS
'''.splitlines(True)
    )

# Generated at 2022-06-13 22:03:51.041341
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_fmt = HeadersFormatter()
    assert headers_fmt.format_headers(
        """
        foo: 1
        bar: 2
        baz: 3
        bar: 4
        qux: 5
        """
    ) == """
        foo: 1
        bar: 2
        bar: 4
        baz: 3
        qux: 5
        """

# Generated at 2022-06-13 22:03:54.649858
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Test with no arguments
    instance = HeadersFormatter()
    assert instance.enabled is False

    # Test with arguments
    instance = HeadersFormatter(format_options={'sort' : True})
    assert instance.enabled is True



# Generated at 2022-06-13 22:04:03.293245
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    base_headers = """
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 346
Connection: close
Status: 200 OK
X-Powered-By: Flask
X-Processed-Time: 0.00147080421448
Date: Thu, 30 Mar 2017 20:00:32 GMT

"""
    result = HeadersFormatter(format_options={'headers': {'sort': True}}).format_headers(base_headers)

# Generated at 2022-06-13 22:04:11.130948
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '\r\n'.join([
        '',
        'alpha: abcd',
        'bravo: bcde',
        'alpha: 123',
        'charlie: cdef',
    ])
    expected = '\r\n'.join([
        '',
        'alpha: abcd',
        'alpha: 123',
        'bravo: bcde',
        'charlie: cdef',
    ])
    assert HeadersFormatter.format_headers(headers) == expected

# Generated at 2022-06-13 22:04:16.003247
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    formatter.addon = 'headers'
    assert formatter.enabled
    assert formatter.format_options


# Generated at 2022-06-13 22:04:23.367949
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    s = """\
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8
Connection: keep-alive
Content-Length: 13

"""
    assert f.format_headers(s) == """\
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 13
Content-Type: application/json;charset=utf-8

"""

# Generated at 2022-06-13 22:04:32.197674
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options=default_options)
    assert formatter.enabled == formatter.format_options['headers']['sort']


# Generated at 2022-06-13 22:04:41.479865
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Content-Length: 30
    Cookie: a=1
    Cache-Control: no-cache
    Content-Type: application/json
    Cookie: b=1
    '''
    actual = HeadersFormatter().format_headers(headers)
    expected = '''Content-Length: 30
    Cache-Control: no-cache
    Content-Type: application/json
    Cookie: a=1
    Cookie: b=1
    '''
    print('expected = {}'.format(expected))
    print('actual = {}'.format(actual))
    assert actual == expected

if __name__ == '__main__':
    test_HeadersFormatter_format_headers()

# Generated at 2022-06-13 22:04:53.421961
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Cache-Control: no-cache\r\n'
        'X-Min: 11\r\n'
        'Set-Cookie: a=1\r\n'
        'ETag: "123"\r\n'
        'X-Min: 22\r\n'
        'Content-Type: application/json\r\n'
    )
    headers = formatter.format_headers(headers)

# Generated at 2022-06-13 22:04:56.659094
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter()
    assert hf.format_options['headers']['sort'] == True
    assert hf.enabled == True


# Generated at 2022-06-13 22:05:05.941646
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter(format_options={
        'headers': {
            'sort': True,
        }
    })

# Generated at 2022-06-13 22:05:15.223975
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hdrs = (
            "HTTP/1.1 200 OK\r\n"
            "Date: Mon, 09 Jul 2018 04:51:37 GMT\r\n"
            "Server: Apache/2.4.7 (Ubuntu)\r\n"
            "X-Powered-By: PHP/5.5.9-1ubuntu4.22\r\n"
            "Vary: Accept-Encoding\r\n"
            "Content-Encoding: gzip\r\n"
            "Content-Length: 2312\r\n"
            "Connection: close\r\n"
            "Content-Type: text/html; charset=UTF-8")

# Generated at 2022-06-13 22:05:18.151980
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.format_options['headers']['sort'] == False



# Generated at 2022-06-13 22:05:28.947869
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Method format_headers should sort headers by name while retaining relative order of multiple headers with same name.
    """
    test_case = """\
        POST /foo HTTP/1.1
        Content-Type: application/json
        Cookie: foo=bar
        Cookie: bar=baz
        Accept: application/json
        Content-Length: 17
        """
    expected_output = """\
        POST /foo HTTP/1.1
        Accept: application/json
        Content-Length: 17
        Content-Type: application/json
        Cookie: foo=bar
        Cookie: bar=baz
        """
    formatter = HeadersFormatter()
    assert formatter.format_headers(test_case) == expected_output

# Generated at 2022-06-13 22:05:32.130934
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    try:
        HeadersFormatter()
    except Exception:
        assert True
    else:
        assert False



# Generated at 2022-06-13 22:05:41.502694
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:02.705936
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:05.652158
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    HeadersFormatter()



# Generated at 2022-06-13 22:06:15.136303
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Server: nginx/1.9.10
Date: Tue, 02 Aug 2016 14:23:37 GMT
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-UA-Compatible: IE=Edge,chrome=1
"""

# Generated at 2022-06-13 22:06:26.099452
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """
HTTP/1.1 200 OK
Server: nginx/1.12.1
Date: Fri, 28 Apr 2017 11:42:37 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Keep-Alive: timeout=60
X-Powered-By: Express
ETag: W/"5f-OacYyCH4vxIoTYfzCm1OBF/BZDw"
Content-Encoding: gzip

""".strip()
    result = formatter.format_headers(headers)

# Generated at 2022-06-13 22:06:37.270773
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
get / HTTP/1.1
Content-Length: 45
X-Foo: Baz
X-Bar: Foo
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
User-Agent: HTTPie/0.9.2
"""
    compare_headers = """\
get / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 45
Host: httpbin.org
User-Agent: HTTPie/0.9.2
X-Bar: Foo
X-Foo: Baz
"""
    formatter = HeadersFormatter()
    headers = formatter.format_headers(headers)
    assert headers == compare_headers


# Generated at 2022-06-13 22:06:42.842333
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {'sort': True}
    })
    headers = """\
HTTP/1.1 200 OK
Date: Thu, 08 Feb 2018 14:45:39 GMT
Server: Apache
Location: /new
Content-Length: 234
Connection: close
Content-Type: text/html; charset=iso-8859-1
"""
    expected_formatted_headers = """\
HTTP/1.1 200 OK
Content-Length: 234
Content-Type: text/html; charset=iso-8859-1
Connection: close
Date: Thu, 08 Feb 2018 14:45:39 GMT
Location: /new
Server: Apache
"""
    assert formatter.format_headers(headers) == expected_formatted_headers

# Generated at 2022-06-13 22:06:50.882842
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(headers_raw) == headers_expected
headers_raw = """GET / HTTP/1.1
Host: example.com
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.18.4
"""
headers_expected = """GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Host: example.com
User-Agent: python-requests/2.18.4
"""

# Generated at 2022-06-13 22:06:59.096930
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers("""\
HTTP/1.1 200 OK
Content-Security-Policy: default-src 'none'
Date: Wed, 03 Jun 2015 21:46:59 GMT
Connection: keep-alive
Content-Type: text/html; charset=utf-8

""") == """\
HTTP/1.1 200 OK
Connection: keep-alive
Content-Security-Policy: default-src 'none'
Content-Type: text/html; charset=utf-8
Date: Wed, 03 Jun 2015 21:46:59 GMT

"""



# Generated at 2022-06-13 22:07:07.655104
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = '''Content-Type: applicatio/json
Content-Length: 5
Date: Mon, 05 Oct 2015 08:22:39 GMT
Accept: application/json
'''
    expected_output = '''Content-Type: applicatio/json
Content-Length: 5
Date: Mon, 05 Oct 2015 08:22:39 GMT
Accept: application/json
'''
    assert hf.format_headers(headers) == expected_output

# Generated at 2022-06-13 22:07:16.720864
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = 'Content-Length: 154\r\nContent-Type: application/json\r\nContent-Length: 144\r\nFoo: bar'
    expected = 'Content-Length: 154\r\nContent-Type: application/json\r\nContent-Length: 144\r\nFoo: bar'
    formatter = HeadersFormatter(None, None, None)
    assert formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:07:59.155562
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Checks whether the headers formatter returns
    the same string if it is already sorted by name.

    """
    s = '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept: */*',
        'Accept-Encoding: gzip, deflate',
        'Connection: keep-alive',
        'Content-Type: application/json',
        'Host: httpbin.org',
        'User-Agent: HTTPie/0.9.9',
        'X-Http-Custom: custom'
    ])
    assert HeadersFormatter.format_headers(s) == s


# Generated at 2022-06-13 22:08:10.548956
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # 1) Method format_headers of class HeadersFormatter sorts headers
    # by name while retaining relative order of multiple headers with
    # the same name.
    formatter = HeadersFormatter(stream=None)
    headers = """HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
X-Header-2: value2
X-Header-1: value1
Link: </stylesheets/app.css>; rel="stylesheet"
X-Header-1: value3
Link: </stylesheets/dark.css>; rel="stylesheet"
X-Header-3: value3
"""

# Generated at 2022-06-13 22:08:20.812389
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()
    headers = "GET / HTTP/1.1\r\nUser-Agent: httpie/0.9.9\r\nAccept: */*\r\nContent-Type: application/json\r\nHost: httpbin.org\r\nAccept-Encoding: gzip, deflate\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n"
    formattedHeaders = headersFormatter.format_headers(headers)

# Generated at 2022-06-13 22:08:26.614228
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=0
Vary: Accept, Accept-Encoding
Server: AmazonS3
Via: 1.1 0006b4aa81495ef0be0c4f4ef4c2d5f0.cloudfront.net (CloudFront)
X-Cache: Hit from cloudfront
X-Amz-Cf-Id: gOIu_K3OiJb3Ao7I8dvXkkV7AjYGJFlw7E8DZL-3tq3_tP_DIkhC8g=="""
    formatter_headers = ''.join(headers.splitlines()[1:])
    expected_headers = formatter_headers.splitlines()
    expected_headers.sort

# Generated at 2022-06-13 22:08:31.384737
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
content-type: application/json
Content-Length: 1984
Connection: close
Content-Length: 1984
Content-Type: application/json
'''
    expected = '''\
content-type: application/json
Content-Length: 1984
Connection: close
Content-Length: 1984
Content-Type: application/json
'''
    assert formatter.format_headers(headers) == expected


# Generated at 2022-06-13 22:08:41.308785
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
GET / HTTP/1.1
Host: www.example.org
Content-Type: text/html; charset=utf-8
Content-Length: 29
User-Agent: httpie/0.3.3
'''
    formatted_headers = '''\
GET / HTTP/1.1
Content-Length: 29
Content-Type: text/html; charset=utf-8
Host: www.example.org
User-Agent: httpie/0.3.3
'''
    assert HeadersFormatter().format_headers(headers) == formatted_headers

# Generated at 2022-06-13 22:08:51.191174
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = (
        'POST / HTTP/1.1\r\n'
        'Content-Length: 255\r\n'
        'Cookie: name=value\r\n'
        'Set-Cookie: other=thing\r\n'
        'cOnTeNt-tYpE: bLaH\r\n'
        'Content-type: blah\r\n'
        'Accept: */*\r\n'
    )

# Generated at 2022-06-13 22:08:56.257351
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    assert f.format_headers('Content-Type: text/plain\r\nContent-Length: 0\r\nCache-Control: no-cache\r\nCCC: 302\r\n') == \
        'Content-Type: text/plain\r\nCache-Control: no-cache\r\nCCC: 302\r\nContent-Length: 0\r\n'

# Generated at 2022-06-13 22:09:06.751058
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    def test(headers, expected):
        assert HeadersFormatter().format_headers(headers) == expected

    test('X: 1\r\nB: 2\r\nA: 3\r\n', 'X: 1\r\nA: 3\r\nB: 2\r\n')
    test('A:\r\n\t1\r\n\t2\r\nB:\r\n\t3\r\n\t4\r\n', 'A:\r\n\t1\r\n\t2\r\nB:\r\n\t3\r\n\t4\r\n')

# Generated at 2022-06-13 22:09:15.472202
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    def assert_formatted_headers(expected, original):
        assert HeadersFormatter.format_headers(original) == expected

    assert_formatted_headers(
        '''\
Content-Type: application/json
Cache-Control: no-cache

''',
        '''\
Cache-Control: no-cache
Content-Type: application/json

'''

    )
    assert_formatted_headers(
        '''\
Cache-Control: max-age=60
Content-Type: application/json
Location: /

''',
        '''\
Location: /
Content-Type: application/json
Cache-Control: max-age=60

'''
    )

# Generated at 2022-06-13 22:10:13.695658
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = ('Content-Length: 12\r\n'
               'Content-Type: application/json\r\n'
               'X-Foo: Bar\r\n\r\n')
    expected = ('Content-Length: 12\r\n'
                'Content-Type: application/json\r\n'
                'X-Foo: Bar\r\n\r\n')
    assert HeadersFormatter().format_headers(headers) == expected
    headers = ('Content-Type: application/json\r\n'
               'X-Foo: Bar\r\n\r\n')
    expected = ('Content-Type: application/json\r\n'
                'X-Foo: Bar\r\n\r\n')
    assert HeadersFormatter().format_headers(headers) == expected

# Generated at 2022-06-13 22:10:23.571302
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Server: TestServer
Set-Cookie: c=1
Vary: Accept, Accept-Encoding
Set-Cookie: a=1
Set-Cookie: b=1"""
    result = formatter.format_headers(headers)
    expected = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Server: TestServer
Set-Cookie: c=1
Set-Cookie: a=1
Set-Cookie: b=1
Vary: Accept, Accept-Encoding"""
    assert result == expected


plugin_cls = HeadersFormatter

# Generated at 2022-06-13 22:10:36.555218
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:10:48.151331
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """
        HTTP/1.1 200 OK
        Cache-Control: max-age=0
        Expires: Wed, 20 Jul 2016 06:38:28 GMT
        Last-Modified: Wed, 20 Jul 2016 06:38:28 GMT
    """
    expected = """HTTP/1.1 200 OK
Cache-Control: max-age=0
Expires: Wed, 20 Jul 2016 06:38:28 GMT
Last-Modified: Wed, 20 Jul 2016 06:38:28 GMT"""
    actual = formatter.format_headers(headers)
    assert actual == expected



# Generated at 2022-06-13 22:10:54.906027
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = """HTTP/1.1 200 OK
Content-Type: application/json
Server: Jetty(9.3.6.v20151106)
Foo: a
Foo: b
Foo: c
Foo: d
Foo: e
Foo: f
Foo: g
Foo: h
Date: Thu, 10 Dec 2015 07:42:45 GMT
Content-Length: 6
"""
    headers_formatted = hf.format_headers(headers)

# Generated at 2022-06-13 22:11:05.216129
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Arrange
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:11:13.649626
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Host: example.org
Server: nginx
X-Foo: Bar
Formatter: Foo
Formatter: Bar
Formatter: Baz
Formatter: Qux
'''
    expect = '''\
Host: example.org
Formatter: Foo
Formatter: Bar
Formatter: Baz
Formatter: Qux
Server: nginx
X-Foo: Bar
'''
    actual = HeadersFormatter().format_headers(headers)

    assert actual == expect
    assert actual == expect.replace('\n', '\r\n')
    assert actual == expect.replace('\n', '\r\n')

# Generated at 2022-06-13 22:11:24.466230
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 0
Host: httpbin.org
User-Agent: HTTPie/0.9.2"""
    expected = """GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 0
Host: httpbin.org
User-Agent: HTTPie/0.9.2"""
    http_formatter = HeadersFormatter()
    assert http_formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:11:32.589676
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    header_strings = ["HTTP/1.1 200 OK",
                      "Server: nginx",
                      "Content-Type: application/json; charset=UTF-8",
                      "Content-Length: 183",
                      "Connection: keep-alive",
                      "Vary: Accept-Encoding",
                      "X-Frame-Options: DENY",
                      "Strict-Transport-Security: max-age=15768000",
                      "X-Content-Type-Options: nosniff",
                      "X-XSS-Protection: 1; mode=block",
                      "Date: Sat, 17 Oct 2015 00:04:38 GMT",
                      "",
                      "{'bfgs_result': {'A': [1, 1], 'B': [2, 2]}}",
                      ""]
    headers_formatter = HeadersFormatter()


# Generated at 2022-06-13 22:11:39.742320
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers':
                                                    {'sort': True}})
    assert formatter.format_headers('Content-Type: application/json\r\nAccept: text/html\r\nAccept: application/json') == 'Content-Type: application/json\r\nAccept: application/json\r\nAccept: text/html'