

# Generated at 2022-06-13 22:01:47.780256
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    headers_input = '''Content-Length: 0
User-Agent: httpie/1.0.2
Content-Type: application/json
Accept-Encoding: gzip, deflate
'''
    assert fmt.format_headers(headers_input) == '''Content-Length: 0
User-Agent: httpie/1.0.2
Accept-Encoding: gzip, deflate
Content-Type: application/json
'''



# Generated at 2022-06-13 22:01:57.375235
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    head = "HTTP/2 200 \r\n" \
        "date: Fri, 27 Jul 2018 21:58:46 GMT\r\n"\
        "server: Apache/2.4.18 (Ubuntu)\r\n"\
        "last-modified: Sat, 12 May 2018 03:07:35 GMT\r\n"\
        "content-length: 12\r\n"\
        "content-type: text/html\r\n"\
        "keep-alive: timeout=5, max=100\r\n"\
        "connection: Keep-Alive\r\n"\
        "\r\n"\
        "get request\n"

# Generated at 2022-06-13 22:02:02.099005
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    test_object = HeadersFormatter(format_options={"headers" : {"sort" : True}})
    assert test_object.enabled == True

# Unit Test for format_headers method of class HeadersFormatter

# Generated at 2022-06-13 22:02:07.638014
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    expected_value = {
        'headers': {
            'sort': False
        }
    }
    actual_value = formatter.format_options
    assert actual_value == expected_value


# Generated at 2022-06-13 22:02:20.512457
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter({'headers': {'sort': True}})
    headers = '''
    HTTP/1.1 200 OK
    Content-Type: application/json; charset=utf-8
    Server: Werkzeug/0.10.4 Python/3.6.0
    Date: Wed, 04 Jan 2017 06:07:44 GMT
    Content-Length: 71
    Connection: keep-alive
    X-XSS-Protection: 1; mode=block'''

# Generated at 2022-06-13 22:02:31.596547
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    input_str = '''
                HTTP/1.1 200 OK
                Content-Type: text/plain; charset=utf-8
                Content-Length: 13
                Connection: keep-alive
                Date: Thu, 21 May 2015 09:11:51 GMT
                '''
    output_str = '''
                HTTP/1.1 200 OK
                Connection: keep-alive
                Content-Length: 13
                Content-Type: text/plain; charset=utf-8
                Date: Thu, 21 May 2015 09:11:51 GMT
                '''
    assert hf.format_headers(input_str) == output_str

# Generated at 2022-06-13 22:02:40.298140
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter(format_options={'headers': {'sort': True}})

    headers = '''\
HTTP/1.1 200 OK
user-Agent: httpie
Content-Type: text/html
X-Custom-Header: abcd
X-Custom-Header: efgh'''
    assert fmt.format_headers(headers) == \
        '''\
HTTP/1.1 200 OK
Content-Type: text/html
X-Custom-Header: abcd
X-Custom-Header: efgh
user-Agent: httpie'''

# Generated at 2022-06-13 22:02:51.911073
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()

# Generated at 2022-06-13 22:03:00.299033
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    factor = HeadersFormatter()

# Generated at 2022-06-13 22:03:02.852520
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options={'headers':{'sort':True}})
    assert formatter.enabled == True


# Generated at 2022-06-13 22:03:15.765230
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:03:27.056372
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # testing with one header with same name
    headers = HeadersFormatter().format_headers("""Content-Type: application/json
User-Agent: httpie
Content-Type: application/xml
Host: httpbin.com""")
    assert headers == """Content-Type: application/json
Content-Type: application/xml
User-Agent: httpie
Host: httpbin.com"""
    # testing with multiple headers with same name
    headers = HeadersFormatter().format_headers("""Content-Type: application/json
User-Agent: httpie
Content-Type: application/xml
Host: httpbin.com""")
    assert headers == """Content-Type: application/json
Content-Type: application/xml
User-Agent: httpie
Host: httpbin.com"""
    # testing with multiple headers with same name
    headers = HeadersFormatter

# Generated at 2022-06-13 22:03:35.742923
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Encoding: gzip\r\n'
        'Content-Type: application/json\r\n'
        'Date: Sun, 20 Jan 2019 14:50:46 GMT\r\n'
        'Vary: Origin,Accept-Encoding\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:03:44.859623
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Function to test format_headers method of class HeadersFormatter
    """
    from textwrap import dedent
    headers = dedent("""\
    content-type: application/json
    accept: application/json
    content-length: 100
    accept-encoding: deflate
    foo: bar
    foo: baz
    user-agent: HTTPie/1.0.0-dev""")
    expected_headers = dedent("""\
    content-type: application/json
    accept: application/json
    content-length: 100
    accept-encoding: deflate
    foo: bar
    foo: baz
    user-agent: HTTPie/1.0.0-dev""")
    formatter_obj = HeadersFormatter()
    actual_headers = formatter_obj.format_headers(headers)

# Generated at 2022-06-13 22:03:55.979285
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter()

# Generated at 2022-06-13 22:04:05.057536
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers("""\
GET / HTTP/1.1
Accept: application/json
User-Agent: HTTPie/0.9.6
Connection: keep-alive
Accept-Encoding: gzip, deflate
Host: httpbin.org
Content-Length: 0""") == """\
GET / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 0
Host: httpbin.org
User-Agent: HTTPie/0.9.6"""

# Generated at 2022-06-13 22:04:11.315314
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter()
    assert isinstance(h, HeadersFormatter)
    assert isinstance(h.format_options, dict)
    assert isinstance(h.format_options['headers'], dict)
    sort_headers = h.format_options['headers']['sort']
    assert isinstance(sort_headers, bool)
    assert sort_headers is True


# Generated at 2022-06-13 22:04:21.572560
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = "User-Agent: HTTPie/0.9.2\r\nAccept-Encoding: gzip, deflate, compress\r\nHost: httpbin.org\r\nConnection: keep-alive"
    expected = "User-Agent: HTTPie/0.9.2\r\nHost: httpbin.org\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, compress"
    assert formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:04:29.601569
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''GET / HTTP/1.1
Accept: application/json, */*
User-Agent: HTTPie/0.9.9
Accept-Encoding: gzip, deflate, compress
Accept-Language: en
Connection: keep-alive
Host: localhost:5000
'''
    expected = '''GET / HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate, compress
Accept-Language: en
Connection: keep-alive
Host: localhost:5000
User-Agent: HTTPie/0.9.9
'''
    assert HeadersFormatter().format_headers(headers).strip() == expected

# Generated at 2022-06-13 22:04:37.713596
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import FormatterPluginManager
    from httpie.plugins import PluginConfig
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPHeadersFormat
    header_formatter = HeadersFormatter(format_options=PluginConfig(
        headers=HTTPHeadersFormat(sort=True)), env=Environment())
    assert header_formatter.enabled == True
    assert isinstance(header_formatter, FormatterPlugin)
    assert isinstance(header_formatter.format_options, PluginConfig)
    manager = FormatterPluginManager()
    manager.add_plugin(header_formatter)
    assert manager.plugin_count() > 0


# Generated at 2022-06-13 22:04:48.239231
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    h = """\
    HTTP/1.1 200 OK
    Set-Cookie: a=42
    Set-Cookie: b=hello;path=/
    Set-Cookie: c=world;domain=example.com
    Content-Type: application/json
    """
    assert f.format_headers(h) == """\
    HTTP/1.1 200 OK
    Content-Type: application/json
    Set-Cookie: a=42
    Set-Cookie: b=hello;path=/
    Set-Cookie: c=world;domain=example.com
    """



# Generated at 2022-06-13 22:04:54.097071
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert hf.format_options['headers']['sort'] is False
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert hf.format_options['headers']['sort'] is True
    hf.format_options['headers'] = {}
    assert hf.format_options['headers'] == {}


# Generated at 2022-06-13 22:05:03.670131
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
Content-Type: application/json; charset=utf-8
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 355
Content-Encoding: gzip
Date: Sun, 03 Jun 2018 23:50:55 GMT
Server: gunicorn/19.7.1
Vary: Accept-Encoding
X-Powered-By: Flask
X-Processed-Time: 0.000107216873169
Via: 1.1 vegur
"""

# Generated at 2022-06-13 22:05:11.304181
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h_formatter = HeadersFormatter(url='/get', headers='h1: v1\r\nh2: v2\r\nh1: v3', method='GET')
    assert h_formatter.enabled
    assert h_formatter.url == '/get'
    assert h_formatter.method == 'GET'
    assert h_formatter.headers == 'h1: v1\r\nh2: v2\r\nh1: v3'


# Generated at 2022-06-13 22:05:20.533151
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:05:31.206175
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    unsorted_headers = """HTTP/1.1 200 OK
Server: nginx
Date: Tue, 15 Jan 2019 15:54:25 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 251
Connection: keep-alive
Vary: Accept-Encoding, Cookie
X-Powered-By: Express
Etag: W/"fb-Lve95gjOVATpfV8ELRb/w"
Allow: GET, PUT, PATCH, DELETE
Cache-Control: private"""

# Generated at 2022-06-13 22:05:35.202291
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.headers import HeadersFormatter
    obj = HeadersFormatter(format_options={}, raw_stream=None, output_file=None)
    assert isinstance(obj, FormatterPlugin)


# Generated at 2022-06-13 22:05:38.662068
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter1 = HeadersFormatter()

    assert(formatter1.enabled == True)

    formatter2 = HeadersFormatter(sort = False)

    assert(formatter2.enabled == False)



# Generated at 2022-06-13 22:05:39.991002
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter().enabled == 1

# Generated at 2022-06-13 22:05:50.571319
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from io import StringIO
    a = HeadersFormatter()
    A = a.format_headers

# Generated at 2022-06-13 22:06:02.890376
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = 'HTTP/1.1 200 OK\r\n' \
        'Server: Apache\r\n' \
        'Content-Type: text/html\r\n' \
        'Content-Language: en\r\n' \
        'Connection: keep-alive\r\n' \
        '\r\n'
    h_fmt = 'HTTP/1.1 200 OK\r\n' \
        'Connection: keep-alive\r\n' \
        'Content-Language: en\r\n' \
        'Content-Type: text/html\r\n' \
        'Server: Apache\r\n' \
        '\r\n'

# Generated at 2022-06-13 22:06:12.937332
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers("""\
HTTP/1.1 200 OK
Content-Length: 9
Content-Type: application/json; charset=utf-8
Content-Encoding: identity
Date: Thu, 06 Feb 2020 19:37:12 GMT
Server: gunicorn/19.9.0

""") == """\
HTTP/1.1 200 OK
Content-Encoding: identity
Content-Length: 9
Content-Type: application/json; charset=utf-8
Date: Thu, 06 Feb 2020 19:37:12 GMT
Server: gunicorn/19.9.0

"""

# Generated at 2022-06-13 22:06:17.734887
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter(options=None, **{})
    assert type(h) == HeadersFormatter


# Generated at 2022-06-13 22:06:23.375413
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input = """
GET / HTTP/1.1
Host: example.org

"""
    expected = """
GET / HTTP/1.1
Host: example.org

"""
    actual = HeadersFormatter().format_headers(input)
    assert expected == actual, '\n'.join((expected, actual))


# Generated at 2022-06-13 22:06:35.816874
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:38.697446
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert hf.enabled == False

    hf2 = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert hf2.enabled == True

# Generated at 2022-06-13 22:06:47.942504
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={"headers": {"sort": True}})
    formatted_headers = formatter.format_headers('''\
HTTP/1.1 200 OK
Accept: */*
Accept-Encoding: gzip, deflate
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 3
Content-Type: application/json; charset=utf-8
Date: Wed, 01 Jul 2020 22:38:14 GMT
Pragma: no-cache
Server: Werkzeug/1.0.1 Python/3.8.3
X-Powered-By: Flask

''')
    

# Generated at 2022-06-13 22:06:59.528835
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = b"""\
HTTP/1.1 301 Moved Permanently
Date: Thu, 14 Nov 2019 00:06:30 GMT
Server: Apache
Cache-Control: max-age=0, no-cache, no-store, must-revalidate, no-transform
Pragma: no-cache
Vary: Accept-Encoding
Content-Type: text/html; charset=iso-8859-1
Location: https://www.w3.org/People/Berners-Lee/card
Content-Length: 289

"""
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    result = hf.format_headers(headers.decode('ascii'))
    assert result == headers.decode('ascii').strip()

# Generated at 2022-06-13 22:07:07.609438
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(None, None)
    headers = 'HTTP/1.1 200 OK\r\nHost: example.com\r\nX-Greeting: Hello world\r\nX-Fruit: Banana\r\n'
    assert formatter.format_headers(headers) == 'HTTP/1.1 200 OK\r\nHost: example.com\r\nX-Fruit: Banana\r\nX-Greeting: Hello world\r\n'



# Generated at 2022-06-13 22:07:21.070852
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Arrange
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:36.783204
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    # Check for sorting on case insensitive basis

# Generated at 2022-06-13 22:07:45.359774
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
        formatter = HeadersFormatter()
        headers = """\
HTTP/1.1 200 OK\r
Server: Apache\r
Vary: Accept-Encoding\r
Content-Length: 57\r
Content-Type: text/html\r
Date: Sun, 12 May 2019 20:43:14 GMT\r
"""
        assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK\r
Content-Length: 57\r
Content-Type: text/html\r
Date: Sun, 12 May 2019 20:43:14 GMT\r
Server: Apache\r
Vary: Accept-Encoding\r
"""

# Generated at 2022-06-13 22:07:57.590095
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = "HTTP/1.1 200 OK\r\n\
Server: nginx/1.6.0\r\n\
Content-Type: application/json; charset=utf-8\r\n\
Transfer-Encoding: chunked\r\n\
Connection: keep-alive\r\n\r\n"

    assert formatter.format_headers(headers) == "HTTP/1.1 200 OK\r\n\
Connection: keep-alive\r\n\
Content-Type: application/json; charset=utf-8\r\n\
Server: nginx/1.6.0\r\n\
Transfer-Encoding: chunked\r\n\r\n"

# Generated at 2022-06-13 22:08:08.899580
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    test_headers_unsorted = """\
HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: cookie1=value
Set-Cookie: cookie2=value
Set-Cookie: cookie3=value"""
    test_headers_sorted = """\
HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: cookie1=value
Set-Cookie: cookie2=value
Set-Cookie: cookie3=value"""
    assert hf.format_headers(test_headers_unsorted) == test_headers_sorted



# Generated at 2022-06-13 22:08:19.927365
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    # Sort headers case 1
    header = '''
        HTTP/1.1 200 OK
        Content-type: text/plain
        A-header: 1
        A-header: 2
        B-header: 1
        C-header: 1
        C-header: 2
        C-header: 3
    '''
    result = hf.format_headers(header)
    expected = '''
        HTTP/1.1 200 OK
        A-header: 1
        A-header: 2
        B-header: 1
        C-header: 1
        C-header: 2
        C-header: 3
        Content-type: text/plain
    '''
    assert result == expected
    # Sort headers case 2

# Generated at 2022-06-13 22:08:31.160177
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = [':authority', ':method', ':path', ':scheme', 'accept', 'accept-encoding', 'accept-language', 'cache-control', 'cookie', 'dnt', 'origin', 'referer', 'user-agent']
    first_line_headers = ':authority\r\n:method\r\n:path\r\n:scheme'
    text = '\r\n'.join(first_line_headers + '\r\n' + '\r\n'.join(headers))
    assert hf.format_headers(text) == '\n'.join(first_line_headers + '\n' + '\n'.join(sorted(headers)))

# An example usage of HeadersFormatter class
#headers = HeadersFormatter()


# Generated at 2022-06-13 22:08:42.846105
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
Content-Length: 22

'''
    assert HeadersFormatter().format_headers(headers) == '''\
HTTP/1.1 200 OK
Content-Length: 22
Content-Type: application/json
Connection: close

'''

    # multiple headers of the same name
    headers = '''\
HTTP/1.1 200 OK
Connection: Upgrade
Connection: close
Content-Type: application/json
Content-Length: 22

'''

    assert HeadersFormatter().format_headers(headers) == '''\
HTTP/1.1 200 OK
Connection: Upgrade
Connection: close
Content-Length: 22
Content-Type: application/json

'''

# Generated at 2022-06-13 22:08:51.388913
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})    
    text = "POST /post HTTP/1.1\r\nHost: httpbin.org\r\nAccept: application/json\r\nContent-Length: 11\r\nContent-Type: text/plain\r\n\r\n"
    expected = "POST /post HTTP/1.1\r\nAccept: application/json\r\nContent-Length: 11\r\nContent-Type: text/plain\r\nHost: httpbin.org\r\n\r\n"
    actual = formatter.format_headers(text)
    assert actual == expected

test_HeadersFormatter_format_headers()

# Generated at 2022-06-13 22:09:00.292095
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Date: Wed, 13 Feb 2019 09:44:37 GMT
Server: Apache
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 418
Content-Type: text/html; charset=iso-8859-1
'''
    exp = '''
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Length: 418
Content-Type: text/html; charset=iso-8859-1
Date: Wed, 13 Feb 2019 09:44:37 GMT
Server: Apache
Vary: Accept-Encoding
'''
    assert exp == hf.format_headers(headers)


# Generated at 2022-06-13 22:09:12.282039
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter1 = HeadersFormatter()
    headers_str = 'HTTP/1.1 200 OK\r\nDate: Wed, 07 Jul 2010 16:02:41 GMT\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: 486\r\n'
    actual = formatter1.format_headers(headers_str)
    expected = 'HTTP/1.1 200 OK\r\nContent-Length: 486\r\nContent-Type: text/html; charset=utf-8\r\nDate: Wed, 07 Jul 2010 16:02:41 GMT\r\n'
    assert actual == expected

# Generated at 2022-06-13 22:09:32.607624
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    t = HeadersFormatter()

# Generated at 2022-06-13 22:09:41.846444
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method format_headers of class HeadersFormatter.
    """
    # setup
    headers = "HTTP/1.1 200 OK\r\nDate: Mon, 27 Jul 2009 12:28:53 GMT\r\n" \
              "Server: Apache/2.2.14 (Win32)SS\r\n" \
              "Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n" \
              "ETag: \"34aa387-d-1568eb00\"\r\n" \
              "Accept-Ranges: bytes\r\nContent-Length: 51\r\n" \
              "Connection: close\r\nContent-Type: text/html\r\n" \
              "X-Pad: avoid browser bug"
    formatter_plugin = Headers

# Generated at 2022-06-13 22:09:52.080820
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()

# Generated at 2022-06-13 22:10:04.990049
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    # Unsorted headers
    headers = '''\
Content-Type: application/json; charset=utf-8
x-svc-id: svc-e325d9fe
Connection: keep-alive
Content-Length: 64
Host: example.com
x-correlator: 95749076-5b01-4b15-852d-241daa10e348
x-svc-id: svc-e325d9fe
User-Agent: HTTPie/1.0.0-dev
x-svc-id: svc-e325d9fe
'''
    # Sorted headers

# Generated at 2022-06-13 22:10:14.871259
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:10:24.134262
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {'sort': True}
    })

# Generated at 2022-06-13 22:10:36.291965
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.enabled

    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/plain; charset=utf-8\r\n'
        'Content-Length: 2\r\n'
        'Content-Encoding: gzip\r\n'
        'Content-Encoding: deflate\r\n'
        'Connection: keep-alive\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:10:50.259658
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hs = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n' \
         'Date: Wed, 11 Apr 2018 14:45:43 GMT\r\nServer: Werkzeug/0.12.2\r\n' \
         'X-Frame-Options: SAMEORIGIN\r\nX-Powered-By: Flask\r\n\r\n'
    h1 = sorted(hs.splitlines()[1:], key=lambda h: h.split(':')[0])
    h1 = '\r\n'.join(hs.splitlines()[:1] + h1)
    assert hf.format_headers(hs) == h1



# Generated at 2022-06-13 22:10:58.678476
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = hf.format_headers('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: keep-alive\r\n\r\n')
    assert headers == 'HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nContent-Type: application/json\r\n\r\n'
    headers = hf.format_headers('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Type: application/xml\r\n\r\n')
    assert headers == 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Type: application/xml\r\n\r\n'

# Generated at 2022-06-13 22:11:10.313512
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    # Two headers with the same name, and a header with a name that's
    # a prefix of another header (see https://github.com/jakubroztocil/httpie/issues/720)
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK', 'Content-Type: text/plain',
        'X-Foo: 1', 'X-Foo: 2', 'X-Foo-Bar: 3'
    ])
    assert hf.format_headers(headers) == '\r\n'.join([
        'HTTP/1.1 200 OK', 'X-Foo: 1', 'X-Foo: 2', 'X-Foo-Bar: 3',
        'Content-Type: text/plain'
    ])

# Generated at 2022-06-13 22:11:43.970199
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    input_headers='''\
        User-Agent: HTTPie/0.9.9
        Accept-Encoding: gzip, deflate
        Cookie: session=73c8dbf5a5c5274f1e9f7d84613
        Accept: application/json
    '''
    actual_headers = formatter.format_headers(input_headers)
    expected_headers = '''\
        User-Agent: HTTPie/0.9.9
        Accept: application/json
        Accept-Encoding: gzip, deflate
        Cookie: session=73c8dbf5a5c5274f1e9f7d84613
    '''
    assert actual_headers == expected_headers