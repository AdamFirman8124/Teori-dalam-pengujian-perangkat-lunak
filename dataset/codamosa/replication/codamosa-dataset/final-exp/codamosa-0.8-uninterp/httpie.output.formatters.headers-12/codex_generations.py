

# Generated at 2022-06-13 22:01:47.586502
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('''\
    content-length: 170
    foo: bar
    content-length: 170
''') == '''\
content-length: 170
content-length: 170
foo: bar
'''

PluginManager.register(HeadersFormatter)

# Generated at 2022-06-13 22:01:57.283897
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Each string contains the following headers in this order:
        # Accept, Accept -Encoding, Content -Type, Content -Length, Host
    unfmt_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Host: www.example.com\r\n"
        "Accept-Encoding: gzip, deflate\r\n"
        "Content-Length: 5\r\n"
        "Accept: text/plain\r\n"
    )

# Generated at 2022-06-13 22:02:01.509471
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter(help_msg=None, version=None)
    assert 'headers' in headers_formatter.format_options


# Generated at 2022-06-13 22:02:17.334747
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Ensure that the method format_headers sorts headers by name while
    # retaining relative order of multiple headers with the same name
    fh = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Length: 0
x-host: host1
Content-Type: application/json; charset=UTF-8
X-Host: host2
X-Host: host3
'''
    expected_headers = '''\
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json; charset=UTF-8
x-host: host1
X-Host: host2
X-Host: host3
'''
    actual_headers = fh.format_headers(headers)
    assert actual_headers == expected_headers



# Generated at 2022-06-13 22:02:20.362486
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    p = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert not p.enabled
    assert p.format_options['headers']['sort'] == False



# Generated at 2022-06-13 22:02:29.703134
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    import io

    headers = '''\
Connection: keep-alive
content-Type: application/json
Cookie: sessionid=123abc
content-length: 24
B: b
A: a
'''
    f = HeadersFormatter(format_options={'headers': {'sort': True}})
    f.start_format(stream=io.StringIO(), color_scheme={})
    headers = f.format_headers(headers)

    assert headers == '''\
Connection: keep-alive
A: a
B: b
Cookie: sessionid=123abc
content-Type: application/json
content-length: 24
'''

# Generated at 2022-06-13 22:02:38.080459
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = dedent("""\
        POST / HTTP/1.1
        Accept: application/json
        X-API-Token: 123
        Content-Type: application/json
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
    """)
    expected_headers = dedent("""\
        POST / HTTP/1.1
        Accept: application/json
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Content-Type: application/json
        X-API-Token: 123
    """)
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == expected_headers

# Generated at 2022-06-13 22:02:44.795332
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers('Authorization :asd\n123: asd\nZX: asd\n') == 'Authorization :asd\n123: asd\nZX: asd\n'

if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 22:02:55.202050
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_before = '''\
HTTP/1.1 200 OK
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8,es;q=0.6
'''

# Generated at 2022-06-13 22:03:06.915815
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    format_headers = formatter.format_headers

# Generated at 2022-06-13 22:03:21.059929
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    # Create instance of HeadersFormatter class
    headers_formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    # Expected result of headers_formatter.format_headers function
    # when invoked with the following input
    input = (
        'Content-Type: application/x-www-form-urlencoded\r\n'
        'User-Agent: httpie/1.0x\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'Accept: */*\r\n'
        'Connection: keep-alive\r\n'
        'Content-Length: 0\r\n'
    )
    # Expected result

# Generated at 2022-06-13 22:03:30.018580
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = '''HTTP/1.1 200 OK
Content-Length: 4
Date: Tue, 20 Sep 2016 03:18:36 GMT
Content-Type: application/json

'''.lstrip()
    correct = '''HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Tue, 20 Sep 2016 03:18:36 GMT

'''
    assert f.format_headers(headers) == correct


# unit test for sort_dict


# Generated at 2022-06-13 22:03:35.303731
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    json_o = dict()
    json_o['headers'] = dict()
    json_o['headers']['sort'] = True
    formatter = HeadersFormatter(format_options=json_o)
    assert formatter.enabled == json_o['headers']['sort']


# Generated at 2022-06-13 22:03:42.686508
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Accept: */*
Accept-Charset: UTF-8
X-Foo: 1
X-Bar: 2
X-Foo: 3
Content-Type: application/x-www-form-urlencoded
'''
    assert (HeadersFormatter.format_headers(headers) == '''\
Accept: */*
Accept-Charset: UTF-8
Content-Type: application/x-www-form-urlencoded
X-Bar: 2
X-Foo: 1
X-Foo: 3
''')



# Generated at 2022-06-13 22:03:44.807196
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(verbose=False)
    assert formatter.enabled == False


# Generated at 2022-06-13 22:03:57.718116
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    test_str = 'HTTP/1.1 200 OK\r\n' \
        'Content-Length: 18\r\n' \
        'Connection: keep-alive\r\n' \
        'Keep-Alive: timeout=5\r\n'
    assert formatter.format_headers(test_str) == 'HTTP/1.1 200 OK\r\n' \
        'Connection: keep-alive\r\n' \
        'Keep-Alive: timeout=5\r\n' \
        'Content-Length: 18\r\n'



# Generated at 2022-06-13 22:03:59.627443
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter.enabled == False


# Generated at 2022-06-13 22:04:03.273745
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    d = {'headers': {'sort': True}}
    headersFormatterTest = HeadersFormatter(format_options=d)
    assert headersFormatterTest is not None


# Generated at 2022-06-13 22:04:07.310540
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():

    # Arrange
    # Create an instance of the Python class to be tested,
    # passing required values as inputs

    # Act
    # Call the method to be tested

    # Assert
    # Verify that the expected results were returned
    assert True

# Generated at 2022-06-13 22:04:14.157046
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={"headers": {"sort": True}})
    actual = hf.format_headers("""HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json; charset=utf-8
Content-Length: 13
Date: Mon, 13 Apr 2020 03:19:28 GMT
Connection: keep-alive

{ "message": "OK" }
""")
    print(actual)
    expected = """HTTP/1.1 200 OK
Content-Length: 13
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Date: Mon, 13 Apr 2020 03:19:28 GMT
X-Powered-By: Express

{ "message": "OK" }
"""
    assert actual == expected

# Generated at 2022-06-13 22:04:28.137742
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test that method HeadersFormatter.format_headers() sorts HTTP headers in
    the response while retaining the relative order of multiple headers with
    the same name.
    """
    headers = "\r\n".join([
        "HTTP/1.1 200 OK",
        "Server: example",
        "Connection: keep-alive",
        "Date: Thu, 03 Jan 2019 13:00:00 GMT",
        "Content-Type: text/html",
        "Content-Length: 1",
        "Vary: Accept-Encoding",
        "Accept-Ranges: bytes"
    ])

# Generated at 2022-06-13 22:04:30.336050
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter is not None


# Generated at 2022-06-13 22:04:37.684899
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
    HTTP/1.1 200 OK
    X-Server-Name: foo
    X-Server-Name: bar
    HTTP/1.1 200 OK
    """.strip()
    expected_result = """
    HTTP/1.1 200 OK
    HTTP/1.1 200 OK
    X-Server-Name: foo
    X-Server-Name: bar
    """.strip()
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == expected_result

# Generated at 2022-06-13 22:04:48.781179
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method format_headers of class HeadersFormatter.
    """
    headers = "HTTP/1.1 200 OK\r\nUser-Agent: httpie/2.2.0\r\n" \
    "Host: api.github.com\r\nConnection: keep-alive\r\n" \
    "Accept-Encoding: gzip, deflate\r\nAccept: */*\r\nContent-Type: application/json\r\nContent-Length: 5\r\n" \
    "Accept-Language: en-US\r\n\r\n"
    hf = HeadersFormatter(format_options={'headers': {'sort': False}})
    formatted_headers = hf.format_headers(headers)
    assert formatted_headers == headers

# Generated at 2022-06-13 22:05:00.169561
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 01 May 2017 18:12:25 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: Express
Strict-Transport-Security: max-age=31536000; includeSubDomains
ETag: W/"17a-TgTIJxybwH1mJ+cKj2gPsIhMFRY"
X-Content-Type-Options: nosniff
'''

# Generated at 2022-06-13 22:05:01.797594
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter()
    assert isinstance(headers_formatter, HeadersFormatter)



# Generated at 2022-06-13 22:05:10.511114
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test sorting of headers
    from httpie.input import ParseError
    from urllib.error import HTTPError
    try:
        http('--format=fmt',
             '--headers-sort',
             'GET',
             'http://httpbin',
             'Content-Type:application/xml',
             'Accept:application/json',
             'Content-Type:application/json',
             'Accept:application/xml')
    except (ParseError, HTTPError) as e:
        assert False, str(e)

# Generated at 2022-06-13 22:05:13.465920
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options={'diff': True, 'headers': {'sort': True}})
    assert formatter.enabled is True



# Generated at 2022-06-13 22:05:19.125397
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    assert h.format_headers(
        "GET / HTTP/1.1\r\n"
        "A-Header: a\r\n"
        "C-Header: c\r\n"
        "B-Header: b\r\n"
    ) == (
        "GET / HTTP/1.1\r\n"
        "A-Header: a\r\n"
        "B-Header: b\r\n"
        "C-Header: c\r\n"
    )

# Generated at 2022-06-13 22:05:28.640773
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK\r
X-My-Header: value\r
Content-Type: application/json\r
X-My-Header: value\r
\r
'''
    formatted_headers = formatter.format_headers(headers)
    assert formatted_headers == '''\
HTTP/1.1 200 OK\r
Content-Type: application/json\r
X-My-Header: value\r
X-My-Header: value\r
\r
'''


# Overrides the render_headers method to format response headers

# Generated at 2022-06-13 22:05:35.581936
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # inputs
    ## headers = {}

    # expect
    ## None

    # actual
    actual = HeadersFormatter(**{'format_options': {'headers': {'sort': True}}})

    # assert
    assert actual



# Generated at 2022-06-13 22:05:42.895934
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input_headers = """
    GET / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Length: 0
    Host: localhost:8080
    User-Agent: HTTPie/1.0.2
    X-Hello: World
    X-Hello: Everyone
    """
    excepted_headers = """
    GET / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Length: 0
    Host: localhost:8080
    User-Agent: HTTPie/1.0.2
    X-Hello: World
    X-Hello: Everyone
    """
    actual_headers = HeadersFormatter().format_headers(input_headers)
   

# Generated at 2022-06-13 22:05:44.639413
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    expected = HeadersFormatter()
    assert expected.enabled == True


# Generated at 2022-06-13 22:05:53.592578
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Tue, 09 Feb 2016 14:00:24 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2
Connection: keep-alive
X-Powered-By: Express
Access-Control-Allow-Origin: *
Etag: W/"2-1447066243000"
Set-Cookie: connect.sid=s%3Ajj0oC5K_52aUeMC6UW3cUfz-; Path=/; HttpOnly
'''.lstrip()

# Generated at 2022-06-13 22:06:02.946355
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test case when an empty string is passed as an argument
    headers_formatter_plugin = HeadersFormatter()
    assert headers_formatter_plugin.format_headers('') == ''

    # Test case when an string of length less than 10 is passed as an argument
    assert headers_formatter_plugin.format_headers('abc') == 'abc'

    # Test case when an string of length greater than 10 is passed as an argument
    assert headers_formatter_plugin.format_headers(
        'Simple is better than complex'
    ) == 'Simple is better than complex'

    # Test case when an string of length greater than 10 but not starting with either
    # 'Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Accept-Ranges',
    # 'Cookie', 'Connection', 'Content-Length', '

# Generated at 2022-06-13 22:06:09.029377
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Default class constructor
    print('Class constructor')
    HeadersFormatter()
    # Testing class constructor with some values
    print('\nClass constructor with some values')
    HeadersFormatter(format_options={'headers': {'sort': True}})



# Generated at 2022-06-13 22:06:13.417292
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\nheader-b: value-b\r\nheader-a: value-a"
    assert formatter.format_headers(headers) == "HTTP/1.1 200 OK\r\nheader-a: value-a\r\nheader-b: value-b"



# Generated at 2022-06-13 22:06:24.816505
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()

# Generated at 2022-06-13 22:06:31.596259
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = '''\r
POST /foo HTTP/1.1
Cookie: foo=bar
Content-Type: application/json\r
'''
    assert hf.format_headers(headers) == '''\r
POST /foo HTTP/1.1
Content-Type: application/json
Cookie: foo=bar\r
'''


# Generated at 2022-06-13 22:06:36.629506
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={'headers': {'sort': True}})
    assert HeadersFormatter(format_options={'headers': {'sort': False}})

# Generated at 2022-06-13 22:06:48.476058
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersformatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:59.823696
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Given
    formatter = HeadersFormatter()
    headers_string = """\
HTTP/1.1 200 OK
Server: nginx
Date: Wed, 23 Aug 2017 20:14:32 GMT
Content-Type: application/json
Connection: close
Content-Length: 590
Cache-Control: no-cache
Access-Control-Allow-Origin: http://localhost
Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, PATCH, DELETE
Access-Control-Allow-Headers: X-Requested-With,content-type
Access-Control-Allow-Credentials: true
Pragma: no-cache
Expires: -1
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN

"""

# Generated at 2022-06-13 22:07:10.745400
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(
        format_options=dict(headers=dict(sort=True)))
    headers_before = (
        'GET / HTTP/1.1\r\n'
        'Connection: keep-alive\r\n'
        'Accept: image/png\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'User-Agent: HTTPie/0.9.2\r\n'
        'Host: httpbin.org\r\n')

# Generated at 2022-06-13 22:07:23.267019
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('HTTP/1.0 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\nServer: SimpleHTTP/0.6 Python/3.8.3\r\nDate: Sat, 30 May 2020 09:12:11 GMT\r\n\r\n{') == 'HTTP/1.0 200 OK\r\nConnection: close\r\nContent-Type: application/json\r\nDate: Sat, 30 May 2020 09:12:11 GMT\r\nServer: SimpleHTTP/0.6 Python/3.8.3\r\n\r\n{'

# Function test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:07:34.169037
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    output = formatter.format_headers('HTTP/1.1 405 Method Not Allowed\r\n'
                                      'Cache-Control: private\r\n'
                                      'Content-Type: application/json\r\n'
                                      'Date: Wed, 28 Aug 2019 15:11:13 GMT\r\n'
                                      'Server: BaseHTTP/0.6 Python/3.7.4\r\n'
                                      'Content-Length: 208\r\n'
                                      'Connection: close\r\n\r\n')


# Generated at 2022-06-13 22:07:44.484538
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hf.enabled = True
    assert hf.format_headers("""\
Host: localhost:8081
Date: Fri, 13 Nov 2015 12:54:42 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Allow: GET, POST, PUT, OPTIONS

""") == """\
Host: localhost:8081
Date: Fri, 13 Nov 2015 12:54:42 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Allow: GET, POST, PUT, OPTIONS

"""


# Generated at 2022-06-13 22:07:52.012309
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''HTTP/1.1 200 OK
Server: nginx
Date: Wed, 14 Aug 2019 10:49:35 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 9
Connection: keep-alive'''
    expected_headers = '''HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 9
Content-Type: text/html; charset=utf-8
Date: Wed, 14 Aug 2019 10:49:35 GMT
Server: nginx'''
    actual_headers = formatter.format_headers(headers)
    assert actual_headers == expected_headers



# Generated at 2022-06-13 22:07:56.773611
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json

'''
    assert (formatter.format_headers(headers) == '''\
HTTP/1.1 200 OK
Content-Type: application/json
Server: nginx

''')



# Generated at 2022-06-13 22:08:01.699522
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = formatter.format_headers("""\
Content-Length: 5
Accept: */*
Accept-Encoding: gzip, deflate
Host: httpbin.org
User-Agent: HTTPie/0.9.6
""")

    expected_headers = """\
Content-Length: 5
Accept: */*
Accept-Encoding: gzip, deflate
Host: httpbin.org
User-Agent: HTTPie/0.9.6\
"""
    assert headers == expected_headers

headers_formatter = HeadersFormatter()
http.PRE_REQUEST_HOOK_DICT['headers_formatter.format_headers'] = \
    headers_formatter.format_headers

# Generated at 2022-06-13 22:08:11.382921
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/html; charset=utf-8\r\n'
        'Connection: keep-alive\r\n'
        'Transfer-Encoding: chunked\r\n'
        'Server: gunicorn/19.9.0\r\n'
        'Date: Sun, 11 Nov 2018 14:47:59 GMT\r\n')