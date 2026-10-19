

# Generated at 2022-06-13 22:01:41.988218
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():

    #TODO: Replace the assertion
    assert True

# Generated at 2022-06-13 22:01:43.999254
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter



# Generated at 2022-06-13 22:01:55.405533
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.plugins import plugin_manager
    from httpie.context import Environment

    formatter = HeadersFormatter()

    def transform_headers(raw_headers:str):
        formatted_headers = RawHTTP(raw_headers)

        key_value_arg_type = KeyValueArgType()
        headers_list = key_value_arg_type.split(formatted_headers)
        headers = key_value_arg_type.transform_values(headers_list)

        formatter._env = Environment(values=headers,
                                     stream=None,
                                     color=True)
        plugin_manager.hook.headers(headers=headers)
        return formatter.format_headers(headers)

    # Tests

# Generated at 2022-06-13 22:02:03.225651
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
	headers = "GET / HTTP/1.1\r\nUser-Agent: aaa\r\nAccept-Language: aaa\r\nAccept-Language: bbb\r\n\r\n"
	assert HeadersFormatter().format_headers(headers) == "GET / HTTP/1.1\r\nAccept-Language: aaa\r\nAccept-Language: bbb\r\nUser-Agent: aaa\r\n\r\n"


# Generated at 2022-06-13 22:02:13.116372
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Test initialisation of the HeadersFormatter class
    headers_formatter = HeadersFormatter()
    # Test the initial values of the class
    print("Type of headers_formatter: " + str(type(headers_formatter)))
    print("Value of __init__.enabled: " + str(headers_formatter.enabled))
    print("Value of __init__.format_options: " + str(headers_formatter.format_options))


# Generated at 2022-06-13 22:02:19.197219
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """Content-Type: application/json
User-Agent: HTTPie/0.9.9
Accept: */*
"""
    expected = """Content-Type: application/json
Accept: */*
User-Agent: HTTPie/0.9.9
"""
    assert formatter.format_headers(headers) == expected
    
    
    
    

# Generated at 2022-06-13 22:02:30.824332
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options=json.loads('{"headers": {"sort": false}}'))
    assert hf.format_headers('Content-Type: application/json\r\nAccept: application/json\r\n') == 'Content-Type: application/json\r\nAccept: application/json\r\n'

    hf.enabled = True
    assert hf.format_headers('Content-Type: application/json\r\nAccept: application/json\r\n') == 'Content-Type: application/json\r\nAccept: application/json\r\n'

# Generated at 2022-06-13 22:02:42.043903
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('\r\n'.join([
        'GET / HTTP/1.1',
        'Host: example.org',
        'User-Agent: httpie-unittest',
        'Accept-Encoding: gzip',
        'Connection: keep-alive',
        'Accept: */*',
        'Cookie: foo=bar',
        '',
        '',
    ])) == '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept: */*',
        'Accept-Encoding: gzip',
        'Connection: keep-alive',
        'Cookie: foo=bar',
        'Host: example.org',
        'User-Agent: httpie-unittest',
        '',
        '',
    ])



# Generated at 2022-06-13 22:02:45.683479
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    try:
        HeadersFormatter()
        assert True
    except:
        assert False

# Unit test of format_headers()
# Proper output as expected and format_headers() returns a string

# Generated at 2022-06-13 22:02:55.625844
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    h = '''HTTP/1.1 200 OK
Date: Sat, 23 Mar 2019 13:42:24 GMT
Server: Apache
Access-Control-Allow-Origin: http://example.com
X-Content-Type-Options: nosniff
Access-Control-Allow-Credentials: true
Vary: Origin
Content-Length: 1311
Connection: close
Content-Type: application/json; charset=UTF-8

{"data":{"test":"test"}}
'''

# Generated at 2022-06-13 22:03:05.854037
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers='''\
GET /test/test/test.txt HTTP/1.1
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.foo.com
User-Agent: HTTPie/1.0.0-dev
'''
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == '''\
GET /test/test/test.txt HTTP/1.1
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.foo.com
User-Agent: HTTPie/1.0.0-dev
'''



# Generated at 2022-06-13 22:03:15.695140
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:21.137035
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive'''

    result = formatter.format_headers(headers)
    assert result == '''Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive'''

# Generated at 2022-06-13 22:03:34.134110
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    actual = headers_formatter.format_headers(\
    '''\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 42
X-Foobar: Baz
Date: Thu, 11 May 2017 13:01:53 GMT
Connection: keep-alive
Cache-Control: private, max-age=0, no-cache

''')

    expected = '''\
HTTP/1.1 200 OK
Cache-Control: private, max-age=0, no-cache
Connection: keep-alive
Content-Length: 42
Content-Type: text/html
Date: Thu, 11 May 2017 13:01:53 GMT
X-Foobar: Baz

'''
    assert actual == expected



# Generated at 2022-06-13 22:03:42.800503
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Set up
    headers = '''GET http://example.org/ HTTP/1.1
Host: example.org
Accept: */*
Connection: close
Accept-Encoding: gzip, deflate
User-Agent: HTTPie/0.9.9
Content-Length: 15
'''
    # Exercise
    result = HeadersFormatter().format_headers(headers)
    # Verify
    assert result == '''GET http://example.org/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 15
Host: example.org
User-Agent: HTTPie/0.9.9
'''

# Generated at 2022-06-13 22:03:51.556837
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
content-type: application/json; charset=utf-8
content-length: 15
server: waitress
date: Sun, 25 Oct 2020 01:12:32 GMT

'''
    expected = '''
HTTP/1.1 200 OK
content-length: 15
content-type: application/json; charset=utf-8
date: Sun, 25 Oct 2020 01:12:32 GMT
server: waitress

'''
    assert headersFormatter.format_headers(headers) == expected

# Generated at 2022-06-13 22:04:00.145003
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = "Accept-Charset: iso-8859-5\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: ru\r\nConnection: close\r\nHost: example.com\r\nUser-Agent: Custom"
    assert HeadersFormatter().format_headers(headers) == "Accept-Charset: iso-8859-5\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: ru\r\nConnection: close\r\nHost: example.com\r\nUser-Agent: Custom"



# Generated at 2022-06-13 22:04:02.998276
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    f = HeadersFormatter(format_options={'headers':{'sort':True}})
    assert(f.enabled == True)


# Generated at 2022-06-13 22:04:07.932958
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h1 = 'hello'
    h2 = 'world'
    fmt_cls = HeadersFormatter()
    headers = fmt_cls.format_headers(f'{h1}\n{h2}')
    assert headers == f'{h1}\n{h2}'



# Generated at 2022-06-13 22:04:11.915278
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter()
    assert h.format_options == {'headers': {'sort': True}}
    assert h.enabled == True


# Generated at 2022-06-13 22:04:27.609624
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    ft = HeadersFormatter(format_options={'headers':{'sort': True}})

    # Empty string
    assert ft.format_headers('') == ''

    # One header line
    headers = '''GET / HTTP/1.1
Host: example.com'''
    assert ft.format_headers(headers) == headers

    # Multiple header lines with different names
    headers = '''GET / HTTP/1.1
Cookie: cookie1
Host: example.com
User-Agent: foo/1.0'''
    assert ft.format_headers(headers) == headers

    # Multiple header lines with same name
    headers = '''GET / HTTP/1.1
Host: example.com
Cookie: cookie1
Cookie: cookie2
User-Agent: foo/1.0'''

# Generated at 2022-06-13 22:04:39.252221
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    lines = [
        'Content-Type: application/json',
        'Server: aspen 0.22',
        'X-Foo: bar',
        'X-Foo: baz',
        'Transfer-Encoding: chunked'
    ]
    headers = '\r\n'.join(lines)
    headers = HeadersFormatter().format_headers(headers)
    assert headers.splitlines() == [
        'Content-Type: application/json',
        'Transfer-Encoding: chunked',
        'X-Foo: bar',
        'X-Foo: baz',
        'Server: aspen 0.22'
    ]
    h = HeadersFormatter(format_options={'headers': {'sort': False}})
    headers = h.format_headers(headers)
    assert headers.splitlines

# Generated at 2022-06-13 22:04:45.653623
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers('GET / HTTP/1.1\r\n'
                             'X-Foo: 1\r\n'
                             'foo: Bar\r\n') == 'GET / HTTP/1.1\r\n'\
                                                  'foo: Bar\r\n'\
                                                  'X-Foo: 1\r\n'

# Generated at 2022-06-13 22:04:55.199580
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fp = HeadersFormatter()
    result = fp.format_headers('''\
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Encoding: UTF-8
Server: Python/3.7.1 (LinuxDell5.5.5.5)
X-Powered-By: Servlet/2.5 JSP/2.1
ETag: W/"2933-4dee214c957c0"
Content-Length: 15
Connection: Close\
''')

# Generated at 2022-06-13 22:05:05.333978
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    import netloc

    assert (HeadersFormatter().format_headers("""Content-Length: 9
Content-Type: text/plain
Content-Length: 8
""") == """Content-Length: 9
Content-Type: text/plain
Content-Length: 8
""")
    assert (HeadersFormatter().format_headers("""Content-Length: 9
Content-Type: text/plain
Content-Length: 8
Content-Type: text/plain
""") == """Content-Length: 9
Content-Type: text/plain
Content-Length: 8
Content-Type: text/plain
""")

# Generated at 2022-06-13 22:05:12.740881
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    formatter = HeadersFormatter()
    header_list = requests.structures.CaseInsensitiveDict()
    header_list['a'] = '1'
    header_list['b'] = '2'
    header_list['c'] = '3'
    header_list['d'] = '4'
    header_list['e'] = '5'
    header_list['f'] = '6'
    header_list['g'] = '7'
    header_list['h'] = '8'
    header_list['i'] = '9'
    header_list['j'] = '10'
    headers = str(header_list)


# Generated at 2022-06-13 22:05:20.417271
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    input = """
POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 8
Host: localhost:5000
User-Agent: HTTPie/0.9.2
"""
    output = """
POST / HTTP/1.1
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 8
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: localhost:5000
User-Agent: HTTPie/0.9.2
"""
    assert formatter.format_headers(input) == output


# Generated at 2022-06-13 22:05:29.101268
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Type: application/json
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
Content-Length: 304
User-Agent: HTTPie/0.9.9
'''

    expected = '''\
Content-Type: application/json
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 304
User-Agent: HTTPie/0.9.9
'''

    assert HeadersFormatter().format_headers(headers) == expected



# Generated at 2022-06-13 22:05:39.522488
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers("""\
GET /some/url HTTP/1.1
Cookie: something=else;
User-Agent: httpie
X-My-Header: oops
Accept: application/json
X-My-Header: abc
Accept-Encoding: gzip, deflate
Connection: keep-alive""") == """\
GET /some/url HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: something=else;
User-Agent: httpie
X-My-Header: oops
X-My-Header: abc"""


# Generated at 2022-06-13 22:05:48.316244
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = formatter.format_headers("""
    Accept: application/json
    Accept-Language: en-US,en
    Content-Length: 28
    Content-Type: application/json
    Accept-Encoding: gzip, deflate
    Connection: Keep-Alive
    """)
    assert headers == """
    Accept: application/json
    Accept-Language: en-US,en
    Accept-Encoding: gzip, deflate
    Content-Length: 28
    Content-Type: application/json
    Connection: Keep-Alive
    """, headers


# Generated at 2022-06-13 22:06:03.128993
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:06.865613
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled is True


# Generated at 2022-06-13 22:06:15.035154
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    assert f.format_headers("""HTTP/1.1 200 OK
Server: uvicorn
Content-Type: text/html; charset=UTF-8
Content-Length: 17
X-Powered-By: ASGI
Date: Wed, 25 Mar 2020 09:27:04 GMT
Via: 1.1 vegur""") == """HTTP/1.1 200 OK
Content-Length: 17
Content-Type: text/html; charset=UTF-8
Date: Wed, 25 Mar 2020 09:27:04 GMT
Server: uvicorn
Via: 1.1 vegur
X-Powered-By: ASGI
""", "test_HeadersFormatter_format_headers()"

# Generated at 2022-06-13 22:06:26.013205
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """Test a few permutations of headers in original and sorted orders."""

# Generated at 2022-06-13 22:06:37.195588
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test with no header
    test_header = ""
    formatter = HeadersFormatter(**{'format_options': {'headers': {'sort': False}}})
    test_result = formatter.format_headers(test_header)
    assert test_result == ""
    # Test with one header
    test_header = "HTTP/1.1 200 OK\r\nDate: Thu, 16 Nov 2017 09:22:27 GMT"
    formatter = HeadersFormatter(**{'format_options': {'headers': {'sort': False}}})
    test_result = formatter.format_headers(test_header)
    assert test_result == "HTTP/1.1 200 OK\r\nDate: Thu, 16 Nov 2017 09:22:27 GMT"
    # Test with multiple headers and multiple headers with same name
    test

# Generated at 2022-06-13 22:06:42.787112
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
GET / HTTP/1.1
User-Agent: httpie
Accept-Encoding: gzip, deflate
Accept: */*
Host: httpbin.org
Connection: keep-alive

"""
    formatter.format_headers(headers) == """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: httpie

"""


# Generated at 2022-06-13 22:06:50.433850
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''
    X-HTTPie-Foo: foo
    X-HTTPie-BAR: bar
    '''
    headers_expected = '''
    X-HTTPie-Foo: foo
    X-HTTPie-BAR: bar
    '''
    headers_formatted = HeadersFormatter(format_options={'headers': {'sort': True}}).format_headers(headers)
    assert headers_formatted == headers_expected

# Generated at 2022-06-13 22:06:59.969699
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers(
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: application/json\r\n'
        'Content-Length: 224\r\n'
        'Connection: keep-alive\r\n'
        'X-Powered-By: Express\r\n'
    ) == (
        'HTTP/1.1 200 OK\r\n'
        'Content-Length: 224\r\n'
        'Content-Type: application/json\r\n'
        'Connection: keep-alive\r\n'
        'X-Powered-By: Express\r\n'
    )


# Generated at 2022-06-13 22:07:10.552491
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hf.enabled = True
    headers = """POST /post HTTP/1.1
Connection: close
Host: example.com
Content-Length: 128
Content-Type: application/x-www-form-urlencoded; charset=utf-8
User-Agent: HTTPie/1.0.2

This is the body of the request."""
    headers_formatted = """POST /post HTTP/1.1
Connection: close
Content-Length: 128
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: example.com
User-Agent: HTTPie/1.0.2

This is the body of the request."""
    assert hf.format_headers(headers) == headers_formatted

# Generated at 2022-06-13 22:07:12.879461
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headersFormatter = HeadersFormatter()
    assert headersFormatter.enabled == True 
