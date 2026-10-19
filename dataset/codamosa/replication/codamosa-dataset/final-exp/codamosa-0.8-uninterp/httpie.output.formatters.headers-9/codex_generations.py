

# Generated at 2022-06-13 22:01:54.841342
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(session=None, format_options=None)

# Generated at 2022-06-13 22:02:06.836383
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    my_headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/plain\r\n'
        'Set-Cookie: a=1\r\n'
        'Set-Cookie: b=2\r\n'
        'Connection: close\r\n'
        'Server: Python/3.7 pytest-5.3.4\r\n'
        'Date: Thu, 26 Mar 2020 17:40:40 GMT\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:02:11.267133
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled == True
    assert formatter.format_options['headers']['sort'] == True


# Generated at 2022-06-13 22:02:22.254314
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Check sorting headers by name:
    format_headers method of class HeadersFormatter
    """
    h = '''
HTTP/1.1 200 OK
DATE: Wed, 02 Oct 2019 17:58:06 GMT
SERVER: Apache/2.4.25 (Debian)
CONTENT-LENGTH: 11
CONTENT-TYPE: text/html; charset=utf-8
CONNECTION: close

Hello world!
    '''
    s = '''
HTTP/1.1 200 OK
CONTENT-LENGTH: 11
CONTENT-TYPE: text/html; charset=utf-8
CONNECTION: close
DATE: Wed, 02 Oct 2019 17:58:06 GMT
SERVER: Apache/2.4.25 (Debian)

Hello world!
    '''

# Generated at 2022-06-13 22:02:28.927251
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """Content-Type: application/json; charset=utf-8
Connection: keep-alive
Server: tornado
Content-Length: 4
"""
    headers_sorted = """Content-Type: application/json; charset=utf-8
Connection: keep-alive
Content-Length: 4
Server: tornado
"""
    assert headers_formatter.format_headers(headers) == headers_sorted

# Generated at 2022-06-13 22:02:37.906065
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test variables
    headers_input = '''Content-Type: application/json
Accept: application/json
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
'''
    headers_output = '''Content-Type: application/json
Accept: application/json
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
'''
    # Test
    headers_result = HeadersFormatter(prog='http').format_headers(headers_input)
    print(headers_result)
    print(headers_output)
    assert headers_result == headers_output



# Generated at 2022-06-13 22:02:48.951217
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = hf.format_headers(
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json; charset=utf-8\r\n'
        'Server: gunicorn/19.9.0\r\n'
        'Date: Sat, 09 Feb 2019 05:55:58 GMT\r\n'
        'Connection: close\r\n'
        'Content-Length: 95'
    )

# Generated at 2022-06-13 22:02:51.911287
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter.__init__
    h = HeadersFormatter()
    assert h.format_options['headers']['sort']


# Generated at 2022-06-13 22:03:00.292451
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    # Test case with headers in random order

# Generated at 2022-06-13 22:03:04.667056
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Check the default attributes and types
    assert HeadersFormatter.__name__ == 'HeadersFormatter'
    assert HeadersFormatter.enabled == 'False'

    # Check that the constructor is correct
    assert HeadersFormatter.enabled == 'False'


# Generated at 2022-06-13 22:03:15.904832
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:27.093969
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json\r\n'
        'Vary: Authorization\r\n'
        'Vary: Cookie\r\n'
        'Vary: Accept-Encoding\r\n'
        'Link: <https://api.github.com/user/9287/repos?page=2>; rel="next", '
        '<https://api.github.com/user/9287/repos?page=7>; rel="last"'
    )

# Generated at 2022-06-13 22:03:32.414254
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    assert HeadersFormatter().format_headers(
        'GET /foo HTTP/1.1\r\nFoo: Bar\r\nContent-Type: application/json\r\nFoo: Baz\r\n\r\n'
    ) == 'GET /foo HTTP/1.1\r\nContent-Type: application/json\r\nFoo: Bar\r\nFoo: Baz\r\n\r\n'



# Generated at 2022-06-13 22:03:40.426850
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Type: application/json; charset=utf-8
Set-Cookie: a=1
Set-Cookie: b=2
X-Custom-Header: value
'''
    assert HeadersFormatter().format_headers(headers) == '''\
Content-Type: application/json; charset=utf-8
Set-Cookie: a=1
Set-Cookie: b=2
X-Custom-Header: value
'''

# Generated at 2022-06-13 22:03:47.925122
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:03:55.669278
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''
HTTP/1.1 200
Cookie: bar
ETag: abc123
Set-Cookie: foo
Cookie: baz

'''
    expected_headers = '''
HTTP/1.1 200
Cookie: bar
Cookie: baz
ETag: abc123
Set-Cookie: foo

'''
    assert HeadersFormatter().format_headers(headers) == expected_headers


# Configuration for Plugin
name = 'headers'
format_options = {
    'headers': {
        'sort': True
    }
}

# Generated at 2022-06-13 22:04:06.184520
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    h = """
Content-Type: image/jpeg
Date: Thu, 26 Apr 2018 04:01:45 GMT
Expires: Fri, 25 May 2018 04:01:45 GMT
Last-Modified: Tue, 06 Feb 2018 09:27:38 GMT
Server: Apache
"""
    output = formatter.format_headers(h)
    assert output == """
Content-Type: image/jpeg
Date: Thu, 26 Apr 2018 04:01:45 GMT
Expires: Fri, 25 May 2018 04:01:45 GMT
Last-Modified: Tue, 06 Feb 2018 09:27:38 GMT
Server: Apache
"""


# Generated at 2022-06-13 22:04:07.314403
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter is not None

# Generated at 2022-06-13 22:04:14.157105
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    test_string = """GET /foo HTTP/1.1\r\nUser-Agent: HTTPie/0.9.3\r\nAccept-Encoding: gzip, deflate, compress\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n"""
    assert formatter.format_headers(test_string) == '\r\n'.join([
        'GET /foo HTTP/1.1',
        'Accept: */*',
        'Accept-Encoding: gzip, deflate, compress',
        'Connection: keep-alive',
        'User-Agent: HTTPie/0.9.3',
        ''
    ])

formatter.add_plugin(HeadersFormatter)

# Generated at 2022-06-13 22:04:27.125446
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    forward_headers = ['Accept: application/json',
                       'Content-Type: application/json;charset=UTF-8',
                       'Content-Type: application/json',
                       'Accept-Language: en-US,en;q=0.5']

    reverse_headers = ['Accept-Language: en-US,en;q=0.5',
                       'Content-Type: application/json',
                       'Content-Type: application/json;charset=UTF-8',
                       'Accept: application/json']

    forward_headers_str = '\r\n'.join(forward_headers)
    reverse_headers_str = '\r\n'.join(reverse_headers)

    assert HeadersFormatter.format_headers(forward_headers_str) == reverse_headers_str,\
        "HTTP headers were not formatted properly"

# Generated at 2022-06-13 22:04:40.154076
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Date: Mon, 18 Aug 2020 11:51:05 GMT
Warning: 299 - "Deprecated header"
ETag: "123abc"
ETag: "abc123"
Date: Mon, 17 Aug 2020 11:51:05 GMT
Warning: 299 - "Deprecated header"
ETag: "xyz987"
'''
    headers_sorted = '''\
Date: Mon, 18 Aug 2020 11:51:05 GMT
Warning: 299 - "Deprecated header"
ETag: "123abc"
ETag: "abc123"
Date: Mon, 17 Aug 2020 11:51:05 GMT
Warning: 299 - "Deprecated header"
ETag: "xyz987"
'''
    assert HeadersFormatter().format_headers(headers) == headers_sorted

# Generated at 2022-06-13 22:04:49.349575
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Create an instance of class HeadersFormatter
    my_HeadersFormatter = HeadersFormatter()
    # Create a string
    headers_str = '''HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
Server: WSGIServer/0.2 CPython/3.7.4
X-Powered-By: Werkzeug/0.16.0
Content-Length: 47
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Date: Mon, 21 Oct 2019 02:30:12 GMT

'''
    # Apply formatting
    headers_str = my_HeadersFormatter.format_headers(headers_str)
    # Print the result
    print(headers_str)
    # Verify that the result is what we expected

# Generated at 2022-06-13 22:05:00.458719
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()

    # Test when there is a header with a single line
    sample_headers = "HTTP/1.1 200 OK\r\n\
Date: Fri, 13 Sep 2013 18:03:20 GMT\r\n\
Server: Apache\r\n\
Content-Length: 50\r\n\
Connection: close\r\n\
Content-Type: text/html; charset=UTF-8\r\n"

    result = f.format_headers(sample_headers)

# Generated at 2022-06-13 22:05:02.311056
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter({'headers': {'sort': True}})


# Generated at 2022-06-13 22:05:13.972661
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:05:27.498292
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # format_headers should return 3rd, 1st, and 2nd lines in input
    headers = "test\nAccept:application/json\nUser-Agent:testcase"
    assert HeadersFormatter().format_headers(headers) == "test\nUser-Agent:testcase\nAccept:application/json"
    headers = "test\nUser-Agent:testcase\nAccept:application/json"
    assert HeadersFormatter().format_headers(headers) == "test\nUser-Agent:testcase\nAccept:application/json"
    headers = "test\nAccept:application/json\nUser-Agent:testcase\nAccept:application/xml"
    assert HeadersFormatter().format_headers(headers) == "test\nAccept:application/json\nAccept:application/xml\nUser-Agent:testcase"



# Generated at 2022-06-13 22:05:39.065635
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\nContent-Length: 71\r\nContent-Type: application/json\r\nDate: Tue, 18 Nov 2014 20:30:59 GMT\r\nLast-Modified: Tue, 17 Jun 2014 21:22:48 GMT"
    result = formatter.format_headers(headers)
    expected = "HTTP/1.1 200 OK\r\nContent-Length: 71\r\nContent-Type: application/json\r\nDate: Tue, 18 Nov 2014 20:30:59 GMT\r\nLast-Modified: Tue, 17 Jun 2014 21:22:48 GMT"
    assert result == expected

    # Test sorting of multiple headers with the same name

# Generated at 2022-06-13 22:05:47.518000
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Content-Length: 14
Content-Type: application/json
Date: Fri, 10 Oct 2014 09:41:52 GMT
Server: BaseHTTP/0.6 Python/3.4.3
X-Powered-By: Flask'''
    assert HeadersFormatter.format_headers(headers) == '''Content-Length: 14
Content-Type: application/json
Date: Fri, 10 Oct 2014 09:41:52 GMT
Server: BaseHTTP/0.6 Python/3.4.3
X-Powered-By: Flask'''



# Generated at 2022-06-13 22:05:50.887126
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    h = f.format_headers('A: b\r\nC: d\r\nB: c')
    print(h)
    assert h == 'A: b\r\nB: c\r\nC: d'


# Generated at 2022-06-13 22:06:01.875006
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:13.087638
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Case 1: If header contains ':'
    header = "Content-Type:text/html"
    assert HeadersFormatter.format_headers(header) == \
        "Content-Type:text/html"
    # Case 2: If header contains no ':'
    header = "Content-Type"
    assert HeadersFormatter.format_headers(header) == \
        "Content-Type"



# Generated at 2022-06-13 22:06:23.632148
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {'sort': True}})

# Generated at 2022-06-13 22:06:35.500108
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """Content-Type: application/json
Host: httpbin.org
User-Agent: HTTPie/0.9.9
X-Test-Header-A: a
X-Test-Header-B: b
Content-Length: 16
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
"""
    assert formatter.format_headers(headers) == """Content-Type: application/json
User-Agent: HTTPie/0.9.9
Content-Length: 16
Host: httpbin.org
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
X-Test-Header-A: a
X-Test-Header-B: b"""

# Generated at 2022-06-13 22:06:36.579150
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter()


# Generated at 2022-06-13 22:06:45.243932
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:07:00.139041
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:07:10.903543
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter(format_options={'headers': {'sort': True}})
    fmt.enabled = True
    headers = dedent("""\
        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Length: 28
        Content-Type: application/json
        Date: Thu, 30 May 2019 11:26:45 GMT
        Server: TornadoServer/5.1.1
        Via: kong/1.1.4
        X-Kong-Proxy-Latency: 2
        X-Kong-Upstream-Latency: 1
        """)

# Generated at 2022-06-13 22:07:22.391824
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''
Content-Type: application/json; charset=utf-8
Server: nginx/1.14.1
Connection: keep-alive
Date: Sun, 08 Dec 2019 19:07:09 GMT
Content-Length: 2
Cache-Control: max-age=0, private, must-revalidate
X-Request-Id: ead1b6f3-6fdf-41e2-a0ea-406a3b6c3b60
X-Runtime:  0.003862
Content-Encoding: gzip

'''
    formatter_headers = headers_formatter.format_headers(headers)
    print("formatter_headers:", formatter_headers)


# Generated at 2022-06-13 22:07:27.105906
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    t_headersFormatter = HeadersFormatter(format_options = {
        'headers': {
            'sort': True
        }
    })
    assert t_headersFormatter.enabled == True


# Generated at 2022-06-13 22:07:35.813670
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Arrange
    headers = '''\
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Wed, 14 Oct 2015 13:21:10 GMT
Content-Type: text/plain; charset=utf-8
Connection: keep-alive
Content-Length: 7
X-Powered-By: Express
ETag: W/"7-RmZUZjcKcGv40Ujk6IYls3U5BIk"

'''
    # Act
    output = HeadersFormatter().format_headers(headers)
    # Assert

# Generated at 2022-06-13 22:07:58.602006
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate
Connection: close
Date: Wed, 14 Apr 2010 17:40:18 GMT
Etag: ZaaIkB
Server: WEBrick/1.3.1 (Ruby/1.8.7/2009-06-12)
Set-Cookie: _session_id=4b409c4a4d08ca242726ad7f64a87a2f; path=/; HttpOnly
Status: 200 OK
X-Request-Id: cc4d4d4c
X-Runtime: 0.02037
'''
    result = hf.format_headers(headers)

# Generated at 2022-06-13 22:08:10.334738
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
HTTP/1.1 200 OK
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Content-Type: application/json
Vary: Origin
Content-Length: 23
Server: WEBrick/1.3.1 (Ruby/2.0.0/2013-11-22)
Date: Sat, 24 May 2014 17:19:46 GMT
X-Request-Id: bdb3b863-53c1-4a44-9ddf-e6f9b6c31b6b
X-Runtime: 0.005637'''


# Generated at 2022-06-13 22:08:12.451687
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    check_method_for_unit_test(HeadersFormatter, 'format_headers')


# Generated at 2022-06-13 22:08:21.113966
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    assert f.format_headers(
        '''\
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 35
X-Ratelimit-Limit: 5000
X-Ratelimit-Remaining: 4999
Date: Mon, 30 Jul 2018 18:04:08 GMT

'''
    ) == (
        '''\
HTTP/1.1 200 OK
Content-Length: 35
Content-Type: application/json; charset=utf-8
Date: Mon, 30 Jul 2018 18:04:08 GMT
X-Ratelimit-Limit: 5000
X-Ratelimit-Remaining: 4999

'''
    )

# Generated at 2022-06-13 22:08:28.858674
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 3\r\n\r\nabc') == 'HTTP/1.1 200 OK\r\nContent-Length: 3\r\nContent-Type: text/plain\r\n\r\nabc'

# Generated at 2022-06-13 22:08:37.973696
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    formatter = HeadersFormatter()
    headers = '\r\n'.join(['a:b', 'b:a', 'a:a'])
    headers_expected = '\r\n'.join(['a:b', 'a:a', 'b:a'])
    headers_result = formatter.format_headers(headers)

    assert headers_expected == headers_result

# Generated at 2022-06-13 22:08:47.077996
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''
Host: 127.0.0.1:5000
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
'''
    assert hf.format_headers(headers) == '''
Host: 127.0.0.1:5000
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
'''



# Generated at 2022-06-13 22:08:57.811753
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    header_formatter = HeadersFormatter(None)
    headers = 'HTTP/1.1 200 OK\r\n' \
              'Date: Wed, 19 Jun 2019 10:30:00 GMT\r\n' \
              'Server: nginx/1.14.2\r\n' \
              'Content-Type: text/html\r\n' \
              'Transfer-Encoding: chunked\r\n' \
              'Connection: keep-alive\r\n' \
              'Vary: Accept-Encoding\r\n'

# Generated at 2022-06-13 22:08:58.418652
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    pass


# Generated at 2022-06-13 22:09:08.743854
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
HTTP/1.1 200 OK
Server: nginx
Date: Sun, 09 Aug 2015 22:49:10 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2
Connection: keep-alive
Etag: W/"2-1439253348000"

"""
    expected = """
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 2
Content-Type: application/json; charset=utf-8
Date: Sun, 09 Aug 2015 22:49:10 GMT
Etag: W/"2-1439253348000"
Server: nginx

"""
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == expected

formatter = HeadersFormatter()
formatter.format = formatter.format

# Generated at 2022-06-13 22:09:42.292585
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    b = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Length: 893
Content-Type: text/html; charset=UTF-8
Date: Sun, 24 Mar 2019 05:46:42 GMT
Keep-Alive: timeout=2, max=100
Server: Apache
'''
    assert b.format_headers(headers) == '''\
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Length: 893
Content-Type: text/html; charset=UTF-8
Date: Sun, 24 Mar 2019 05:46:42 GMT
Keep-Alive: timeout=2, max=100
Server: Apache
'''

# Generated at 2022-06-13 22:09:51.009145
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('Connection: keep-alive\r\nVary: Accept-Encoding\r\n\r\n') == 'Connection: keep-alive\r\nVary: Accept-Encoding\r\n\r\n'
    assert HeadersFormatter().format_headers('Connection: keep-alive\r\nVary: Accept-Encoding\r\nAccept-Encoding: gzip, deflate\r\n\r\n') == 'Connection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nVary: Accept-Encoding\r\n\r\n'

# Generated at 2022-06-13 22:10:00.579364
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers("""Content-Type: application/json
Authorization: Basic cnVubmVyOnRlc3RwYXNz
Content-Length: 15
Some-Header: fdafdsafdsa
Another-Header: fdafdsafdsa""")
    assert result == """Content-Type: application/json
Authorization: Basic cnVubmVyOnRlc3RwYXNz
Content-Length: 15
Another-Header: fdafdsafdsa
Some-Header: fdafdsafdsa"""

# Generated at 2022-06-13 22:10:09.389518
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=300
Content-Language: en
Content-Length: 137
Content-Type: application/json; charset=utf-8
Date: Mon, 08 Dec 2014 15:59:38 GMT
Etag: "601513b6fbd5e0ef59b29c5d1adf1183"
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
X-RateLimit-Reset: 1418069369
X-Runtime: 0.015250
"""

    result = headers_formatter.format_headers(headers)
    assert result == headers



# Generated at 2022-06-13 22:10:22.118848
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers =  '''\
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 18 Aug 2018 17:09:16 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 47
Connection: keep-alive
Link: <http://127.0.0.1/app_dev.php/items>; rel="http://127.0.0.1/app_dev.php/rels/items",<http://127.0.0.1/app_dev.php/items>; rel="item"

{"items":[],"_links":{"self":{"href":"http:\/\/127.0.0.1\/app_dev.php\/items"}}}
'''

# Generated at 2022-06-13 22:10:35.602757
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(None, request=None, response=None, format_options={
        'headers': {
            'sort': True
        }
    })
    data = '''HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json
Date: Wed, 14 Dec 2016 14:04:00 GMT
Connection: keep-alive
Content-Length: 70
Access-Control-Allow-Origin: *

'''
    expected_result = '''HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 70
Content-Type: application/json
Date: Wed, 14 Dec 2016 14:04:00 GMT
Server: nginx

'''
    assert formatter.format_headers(data) == expected_result

# Generated at 2022-06-13 22:10:48.096569
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers, expected = """\
Accept: application/json
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json
Host: httpbin.org
User-Agent: HTTPie/0.9.2
Accept-Encoding: gzip, deflate
X-Xss-Protection: 1; mode=block""", """\
Accept: application/json
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json
Host: httpbin.org
User-Agent: HTTPie/0.9.2
Accept-Encoding: gzip, deflate
X-Xss-Protection: 1; mode=block"""
    assert HeadersFormatter(format_options={
        'headers': {'sort': True}
    }).format_headers(headers) == expected


# Generated at 2022-06-13 22:10:56.913319
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = \
"""POST /post HTTP/1.1
User-Agent: HTTPie/1.0.3
Content-Type: application/json; charset=utf-8
Accept: application/json
Content-Length: 17

{"foo": "bar"}""".strip()
    assert formatter.format_headers(headers) == \
"""POST /post HTTP/1.1
Accept: application/json
Content-Length: 17
Content-Type: application/json; charset=utf-8
User-Agent: HTTPie/1.0.3

{"foo": "bar"}""".strip()

# Generated at 2022-06-13 22:11:06.853585
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_fmt = HeadersFormatter()
    assert headers_fmt.format_headers('\r\n'.join([
        'GET / HTTP/1.1',
        'Host: requestb.in',
        'User-Agent: Custom-User-Agent',
        'Accept-Encoding: gzip, deflate',
        'Accept: text/html'
    ])) == '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept: text/html',
        'Accept-Encoding: gzip, deflate',
        'Host: requestb.in',
        'User-Agent: Custom-User-Agent'])

# Generated at 2022-06-13 22:11:14.643732
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers("""HTTP/1.1 200 OK
Date: Tue, 04 Jul 2017 03:14:29 GMT
Server: WSGIServer/0.2 CPython/3.5.2+
Content-Type: text/html; charset=utf-8
Vary: Cookie

""")
    assert result == """HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Date: Tue, 04 Jul 2017 03:14:29 GMT
Server: WSGIServer/0.2 CPython/3.5.2+
Vary: Cookie

"""