

# Generated at 2022-06-13 22:01:49.192627
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fp = HeadersFormatter()
    input_data = '''\

Diagnostics: 200 OK
Date: Sun, 16 Aug 2020 22:08:00 GMT
Server: Apache
Vary: Accept-Encoding
Connection: close

^C'''
    expected_data = '''\

Diagnostics: 200 OK
Connection: close
Date: Sun, 16 Aug 2020 22:08:00 GMT
Server: Apache
Vary: Accept-Encoding

^C'''
    output_data = fp.format_headers(input_data)
    assert expected_data == output_data
    # assert True



# Generated at 2022-06-13 22:02:03.406669
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()

# Generated at 2022-06-13 22:02:11.637350
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter(format_options={'headers': {'sort': True}})

# Generated at 2022-06-13 22:02:22.485292
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit tests for method format_headers of class HeadersFormatter.
    """
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})

    unsorted_headers = \
"""HTTP/1.1 200 OK
content-length: 4
Connection: keep-alive
Server: BaseHTTP/0.6 Python/3.8.3
Date: Sun, 27 Sep 2020 09:30:10 GMT
Content-Type: text/html; charset=utf-8
"""
    sorted_headers = \
"""HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 4
Content-Type: text/html; charset=utf-8
Date: Sun, 27 Sep 2020 09:30:10 GMT
Server: BaseHTTP/0.6 Python/3.8.3
"""


# Generated at 2022-06-13 22:02:34.421972
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    given_data = (
        'GET / HTTP/1.1\r\n'
        'User-Agent: httpie\r\n'
        'Accept: */*\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'Content-Length: 3\r\n'
        '\r\n'
    )
    expected_data = (
        'GET / HTTP/1.1\r\n'
        'Accept: */*\r\n'
        'Accept-Encoding: gzip, deflate\r\n'
        'Content-Length: 3\r\n'
        'User-Agent: httpie\r\n'
        '\r\n'
    )
    actual_data = fmt.format_headers

# Generated at 2022-06-13 22:02:45.109739
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie import __version__
    headers_formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\nServer: BaseHTTP/{}\r\nDate: Sat, 14 Sep 2019 12:27:24 GMT\r\nContent-Length: 0\r\nContent-Type: text/plain; charset=utf-8".format(__version__)
    formatted_headers = headers_formatter.format_headers(headers)
    expected_output = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\nContent-Type: text/plain; charset=utf-8\r\nDate: Sat, 14 Sep 2019 12:27:24 GMT\r\nServer: BaseHTTP/{}".format(__version__)

# Generated at 2022-06-13 22:02:47.600442
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    a = HeadersFormatter()
    assert a


# Generated at 2022-06-13 22:02:52.579535
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = FormatterPlugin()
    headers = """GET / HTTP/1.1
User-Agent: HTTPie/2.0.0-dev
Test: B
Test: A
Test: C
"""
    expected_headers = """GET / HTTP/1.1
Test: B
Test: A
Test: C
User-Agent: HTTPie/2.0.0-dev
"""
    assert formatter.format_heade

# Generated at 2022-06-13 22:03:05.962381
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\n" \
              "foo: c\r\n" \
              "X-Bar: b\r\n" \
              "Content-Type: application/json\r\n" \
              "content-type: text/csv\r\n" \
              "foo: a\r\n" \
              "foo: b\r\n"


# Generated at 2022-06-13 22:03:13.217128
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.enabled
    assert formatter.format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'foo: c',
        'bar: a',
        'baz: b',
    ])) == '\r\n'.join([
        'HTTP/1.1 200 OK',
        'bar: a',
        'baz: b',
        'foo: c',
    ])

# Generated at 2022-06-13 22:03:24.299480
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:34.014536
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    actual = hf.format_headers('HTTP/1.1 200 OK\r\nHeader1: value1\r\nHeader2: value2\r\nHeader1: value3\r\n\r\n')
    expected = 'HTTP/1.1 200 OK\r\nHeader1: value1\r\nHeader1: value3\r\nHeader2: value2\r\n\r\n'
    assert actual == expected
 

# Generated at 2022-06-13 22:03:43.855685
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    a = HeadersFormatter()
    assert a.format_headers('Host: 127.0.0.1:5000\r\n'\
        'User-Agent: curl/7.54.0\r\n'\
        'Accept: */*\r\n'\
        'Accept-Encoding: gzip, deflate\r\n'\
        'Connection: keep-alive\r\n') == \
        'Host: 127.0.0.1:5000\r\n'\
        'Accept: */*\r\n'\
        'Accept-Encoding: gzip, deflate\r\n'\
        'Connection: keep-alive\r\n'\
        'User-Agent: curl/7.54.0\r\n'



# Generated at 2022-06-13 22:03:55.349288
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()

    headers = """\
Content-Length: 1
B: 2
A: 3
A: 4
B: 5
Content-Length: 6
X-B: 7
"""
    expected = """\
Content-Length: 1
Content-Length: 6
A: 3
A: 4
B: 2
B: 5
X-B: 7
"""
    assert headersFormatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:04:06.424095
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = \
"""
Header1: value1
Header2: value2
Header3: value3
"""
    expected_headers = \
"""
Header1: value1
Header2: value2
Header3: value3
"""
    assert HeadersFormatter().format_headers(headers) == expected_headers
    # test multiple headers with same name
    headers = \
"""
Header1: value1
Header2: value2
Header3: value3
Header2: value4
"""
    expected_headers = \
"""
Header1: value1
Header2: value2
Header2: value4
Header3: value3
"""
    assert HeadersFormatter().format_headers(headers) == expected_headers

# Generated at 2022-06-13 22:04:07.385589
# Unit test for constructor of class HeadersFormatter

# Generated at 2022-06-13 22:04:14.169835
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Connection: keep-alive
Transfer-Encoding: chunked
Vary: Cookie
Server: gunicorn/19.6.0
Date: Tue, 14 Mar 2017 05:30:22 GMT
Content-Type: text/html; charset=utf-8
X-Powered-By: Werkzeug/0.11.15 Python/3.5.2
"""

# Generated at 2022-06-13 22:04:27.175893
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Integration test for method format_headers of class HeadersFormatter.
    Inputs:
        headers: A string with the exact format of the headers of an HTTP
            response.
    Expected output:
        A string with the same information as the input, but with the headers
        sorted by name.
    """
    # raw headers
    headers = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: application/json; charset=utf-8\r\n'
               'Connection: keep-alive\r\n'
               'Transfer-Encoding: chunked\r\n'
               'Server: gunicorn/19.9.0\r\n'
               'Date: Fri, 05 Jul 2019 16:30:51 GMT\r\n'
               '\r\n')
    formatter

# Generated at 2022-06-13 22:04:39.510062
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:04:49.051506
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt_options = ParseFormatOptions(format_options={'headers': {'sort': True}})
    formatter = HeadersFormatter(format_options=fmt_options)
    headers = ("""HTTP/1.1 200 OK
Server: nginx/1.14.1
Date: Fri, 16 Nov 2018 15:56:01 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: Express

""").strip('\n')

    headers = formatter.format_headers(headers)

# Generated at 2022-06-13 22:05:05.505004
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_str = ('Accept: application/json\n'
                   'Accept-Language: ru;q=0.9,en;q=0.8,es;q=0.7\n'
                   'Accept-Encoding: gzip, deflate\n'
                   'Connection: keep-alive\n'
                   'Host: httpbin.org\n'
                   'User-Agent: HTTPie/1.0.3')

# Generated at 2022-06-13 22:05:12.029981
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.9
"""
    expected_headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.9
"""
    sorted_headers = formatter.format_headers(headers)
    assert sorted_headers == expected_headers

# Generated at 2022-06-13 22:05:17.135368
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        """
        Content-Type: application/json
        X-Auth-Token: abcdef12345

        {
        }
        """
    ) == (
        """
        Content-Type: application/json
        X-Auth-Token: abcdef12345

        {
        }
        """
    )



# Generated at 2022-06-13 22:05:27.275576
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(**{'headers': {'sort': True}})
    assert headers_formatter.format_headers(
        'GET / HTTP/1.1\r\nHost: httpbin.org\r\n'
        'Connection: keep-alive\r\nAccept: */*\r\n\r\n') == \
        'GET / HTTP/1.1\r\n' \
        'Accept: */*\r\n' \
        'Connection: keep-alive\r\n' \
        'Host: httpbin.org\r\n' \
        '\r\n'

# Generated at 2022-06-13 22:05:34.046278
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    m_headers="""GET /hello HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive"""
    e_headers="""GET /hello HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org"""
    assert headers_formatter.format_headers(m_headers) == e_headers    


# Generated at 2022-06-13 22:05:41.333162
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    result = HeadersFormatter()\
        .format_headers("""\
POST / HTTP/1.1
Content-Type: application/json; charset=UTF-8
A: 1
B: 2
B: 21
A: 11
Accept: application/json
C: 3
X-B: 1
X-A: 1
        """)
    assert result == """\
POST / HTTP/1.1
Accept: application/json
A: 1
A: 11
B: 2
B: 21
C: 3
Content-Type: application/json; charset=UTF-8
X-A: 1
X-B: 1
        """

# Generated at 2022-06-13 22:05:43.136363
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    x = HeadersFormatter()
    assert x.format_options['headers']['sort'] is True


# Generated at 2022-06-13 22:05:52.740883
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(format_options={
        'headers': {'sort': True}
    })
    headers = (
        'Content-Length: 8\r\n'
        'Content-Type: application/json\r\n'
        'Date: Wed, 21 Oct 2015 07:28:00 GMT\r\n'
        'Server: Google Frontend\r\n'
        'Cache-Control: private, max-age=0\r\n'
        'Accept-Ranges: none\r\n'
    )

# Generated at 2022-06-13 22:05:53.879037
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    pass


# Generated at 2022-06-13 22:06:00.823006
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.enabled
    assert hf.format_headers('GET / HTTP/1.1\r\nb: 2\r\na: 1\r\n') == 'GET / HTTP/1.1\r\na: 1\r\nb: 2\r\n'



"""
COOKIES_FORMATTER
"""

# Generated at 2022-06-13 22:06:16.161436
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    fmt = HeadersFormatter()
    header = [
        'HTTP/1.1 200 OK',
        'Date: Fri, 14 Sep 2018 08:48:12 GMT',
        'Content-Type: text/html;charset=ISO-8859-1',
        'Content-Length: 23',
        'Server: Jetty(9.0.z-SNAPSHOT)',
        'Content-Encoding: deflate',
        'Content-Encoding: gzip',
        'Server: Jetty(9.0.z-SNAPSHOT)',
        '',
        '<html>hallo</html>'
    ]

# Generated at 2022-06-13 22:06:20.470261
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter(format_options={
        "headers":{
            "sort":True
        }
    })
    assert hf.enabled == True


# Generated at 2022-06-13 22:06:28.153658
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:06:32.176086
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
	"""
	Test initialization of HeadersFormatter object
	"""

	headers_formatter = HeadersFormatter({'headers' : {'sort' : True}})

	assert headers_formatter.enabled == True

# Unit tests for format_headers function

# Generated at 2022-06-13 22:06:37.984783
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers_raw = '''
Cookie: foo=bar
HTTP/1.1 200 OK
set-cookie: foo=bar
content-type: text/html
'''

    headers_formatted = formatter.format_headers(headers_raw)
    expected = '''
Cookie: foo=bar
HTTP/1.1 200 OK
content-type: text/html
set-cookie: foo=bar
'''

    assert headers_formatted == expected

# Generated at 2022-06-13 22:06:41.475175
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """Host: api.github.com
authorization: bearer abcd
X-Custom: header
Content-Length: 48
Content-Type: application/json
"""
    assert(headers_formatter.format_headers(headers) == """Host: api.github.com
authorization: bearer abcd
Content-Length: 48
Content-Type: application/json
X-Custom: header
""")

# Generated at 2022-06-13 22:06:50.697906
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Language: en,de
b: a
a: b
a: c
User-Agent: HTTPie/0.9.2
"""
    expected = """\
GET / HTTP/1.1
Accept: */*
Accept-Language: en,de
User-Agent: HTTPie/0.9.2
a: b
a: c
b: a
"""
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == expected


# Generated at 2022-06-13 22:07:00.612374
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    # the following headers should be in the same order in both lists
    unsorted_headers = [
        'User-Agent: httpie',
        'Accept: text/plain',
        'Accept: application/json',
        'Content-Type: application/json',
        'X-Test-1: value-1',
        'X-Test-2: value-2',
        'X-Test-1: value-3',
    ]

# Generated at 2022-06-13 22:07:08.372391
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert hf.format_headers('GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 12\r\nContent-Length: 8\r\n\r\n') == 'GET / HTTP/1.1\r\nContent-Length: 12\r\nContent-Length: 8\r\nHost: example.com\r\n'

# Generated at 2022-06-13 22:07:21.394232
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    # Test 1:
    headers = """
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US
Connection: keep-alive
Host: tree.cemetech.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 20
"""
    expected_output = """
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US
Connection: keep-alive
Host: tree.cemetech.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 20
"""
    assert formatter.format_headers(headers) == expected_output
    # Test 2:

# Generated at 2022-06-13 22:07:46.879937
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = ('HTTP/1.1 200 OK\r\n'
               'Content-Length: 7\r\n'
               'User-Agent: HTTPie/0.9.6\r\n'
               'Content-Type: text/html; charset=utf-8\r\n')
    expected = ('HTTP/1.1 200 OK\r\n'
                'Content-Length: 7\r\n'
                'Content-Type: text/html; charset=utf-8\r\n'
                'User-Agent: HTTPie/0.9.6\r\n')
    formatter = HeadersFormatter(
        style=Style(command='http', options=['--headers', '--sort'])
    )
    assert formatter.format_headers(headers) == expected


# Generated at 2022-06-13 22:07:58.297204
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    header = '\n'.join([
        'GET / HTTP/1.1',
        'Accept-Encoding: gzip, deflate, compress',
        'Accept: */*',
        'Accept-Language: en',
        'User-Agent: HTTPie/0.9.2',
        'Connection: keep-alive',
        ''
    ])
    testee = HeadersFormatter()
    assert testee.format_headers(header) == '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept: */*',
        'Accept-Encoding: gzip, deflate, compress',
        'Accept-Language: en',
        'Connection: keep-alive',
        'User-Agent: HTTPie/0.9.2',
        '',
    ])



# Generated at 2022-06-13 22:08:08.973637
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Accept-Language: en
Accept-Language: ru
Accept-Encoding: gzip, deflate
Accept: */*
Host: oauth.vk.com"""

    result = """\
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en
Accept-Language: ru
Host: oauth.vk.com"""

    assert HeadersFormatter().format_headers(headers) == result



# Generated at 2022-06-13 22:08:19.927422
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:08:31.026651
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Test with multiple headers with the same name.
    source = '''\
HTTP/1.1 200 OK
Cache-Control: no-cache
Cache-Control: no-store
Pragma: no-cache
Date: Sun, 22 Nov 2015 14:59:17 GMT
Content-Type: text/html; charset=utf-8
Last-Modified: Wed, 04 Nov 2015 21:46:29 GMT
'''
    expected = '''\
HTTP/1.1 200 OK
Cache-Control: no-cache
Cache-Control: no-store
Date: Sun, 22 Nov 2015 14:59:17 GMT
Last-Modified: Wed, 04 Nov 2015 21:46:29 GMT
Pragma: no-cache
Content-Type: text/html; charset=utf-8
'''
   

# Generated at 2022-06-13 22:08:42.779968
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = 'Accept: text/html\r\n' \
        'Accept-Encoding: gzip,deflate\r\n' \
        'Content-Type: text/html; charset=utf-8\r\n' \
        'Connection: keep-alive\r\n' \
        'Accept: application/json\r\n'
    assert (HeadersFormatter().format_headers(h) ==
            'Accept: text/html\r\n'
            'Accept: application/json\r\n'
            'Accept-Encoding: gzip,deflate\r\n'
            'Content-Type: text/html; charset=utf-8\r\n'
            'Connection: keep-alive\r\n')



# Generated at 2022-06-13 22:08:50.786549
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        'HTTP/1.1 200 OK\n'
        'Connection: close\n'
        'Content-Type: application/json\n'
        'Content-Length: 631\n'
        'Date: Tue, 11 Apr 2017 15:25:34 GMT\n'
    ) == (
        'HTTP/1.1 200 OK\r\n'
        'Connection: close\r\n'
        'Content-Length: 631\r\n'
        'Content-Type: application/json\r\n'
        'Date: Tue, 11 Apr 2017 15:25:34 GMT\r\n'
    )

# Generated at 2022-06-13 22:09:01.465234
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:09:10.650912
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test case when two headers have the same name
    formatter = HeadersFormatter()
    headers = "Content-Type: application/json\r\nUser-Agent: HTTPie\r\n" + \
              "User-Agent: Awesome-HTTPie-Plugin\r\n"
    assert formatter.format_headers(headers) == headers

    # Test case when multiple headers with different names
    headers = "Content-Type: application/json\r\nUser-Agent: HTTPie\r\n" + \
              "Accept-Language: en-US\r\n"
    expected = "Content-Type: application/json\r\n" + \
               "Accept-Language: en-US\r\nUser-Agent: HTTPie\r\n"
    assert formatter.format_headers(headers) == expected

    # Test

# Generated at 2022-06-13 22:09:20.031421
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hdrs = '''\
POST /post HTTP/1.1
Content-Type: application/x-www-form-urlencoded
B: 2
A: 1
Cookie: a=b
Cookie: c=d
Content-Length: 7
'''
    hdrs_fmt = '''\
POST /post HTTP/1.1
A: 1
B: 2
Cookie: a=b
Cookie: c=d
Content-Type: application/x-www-form-urlencoded
Content-Length: 7
'''
    assert HeadersFormatter.format_headers(hdrs) == hdrs_fmt



# Generated at 2022-06-13 22:09:54.040810
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    resp = ('HTTP/1.1 200 OK\r\n'
            'Connection: keep-alive\r\n'
            'Cache-Control: private, max-age=0, must-revalidate\r\n'
            'Content-Type: text/html; charset=utf-8\r\n'
            'Content-Encoding: gzip\r\n'
            'Content-Length: 14\r\n'
            'Date: Sun, 17 Dec 2017 20:48:24 GMT\r\n'
            'Server: nginx\r\n\r\n')

# Generated at 2022-06-13 22:10:07.258172
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = ("GET / HTTP/1.1\r\n"
               "Accept: */*\r\n"
               "Connection: keep-alive\r\n"
               "Host: httpbin.org\r\n"
               "User-Agent: HTTPie/1.0.2\r\n"
               "Accept-Encoding: gzip, deflate\r\n"
               "Accept-Encoding: gzip\r\n"
               "\r\n")

# Generated at 2022-06-13 22:10:16.174844
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Initialization
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options['headers']['sort'] = True

    # No headers in the message
    message = '''HTTP/1.1 200 OK

Some data.'''
    expected_message = '''HTTP/1.1 200 OK

Some data.'''
    assert headers_formatter.format_headers(message) == expected_message

    # Some headers in the message

# Generated at 2022-06-13 22:10:20.976532
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Content-Length: 15
Content-Type: application/json
x-httpie-test: test-value'''

    expected = '''Content-Length: 15
Content-Type: application/json
x-httpie-test: test-value'''

    assert HeadersFormatter().format_headers(headers) == expected

# Generated at 2022-06-13 22:10:34.903655
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\\r\\n
Content-Type: application/json\\r\\n
User-Agent: HTTPie/0.9.9\\r\\n
X-Header: 1\\r\\n
X-Header: 2\\r\\n
Content-Length: 15\\r\\n
X-Header: 3\\r\\n
'''

# Generated at 2022-06-13 22:10:40.965969
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Server: nginx/1.10.1
Date: Fri, 10 Feb 2017 10:10:07 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
"""
    assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
Connection: keep-alive
Content-Type: text/html; charset=UTF-8
Date: Fri, 10 Feb 2017 10:10:07 GMT
Server: nginx/1.10.1
"""

# Generated at 2022-06-13 22:10:50.584805
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Date: Fri, 10 Jul 2020 05:14:12 GMT
Content-Length: 76
Connection: close

<html></html>
"""
    expected = """\
HTTP/1.1 200 OK
Connection: close
Content-Length: 76
Content-Type: text/html; charset=utf-8
Date: Fri, 10 Jul 2020 05:14:12 GMT

<html></html>
"""
    assert formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:10:58.791544
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """HTTP/1.1 200 OK
Server: nginx
Date: Tue, 03 Jul 2018 13:30:36 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
x-cached: MISS
X-Timeline-Version: versionXXX
Content-Encoding: gzip"""

    expected = """HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: application/json
Connection: keep-alive
Date: Tue, 03 Jul 2018 13:30:36 GMT
Server: nginx
Transfer-Encoding: chunked
X-Timeline-Version: versionXXX
x-cached: MISS"""

    formatter = HeadersFormatter(format_options={
        'headers': {'sort': True}
    })
    assert formatter.format_headers(headers)

# Generated at 2022-06-13 22:11:05.667969
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_string = '''\
Connection: close
Content-Length: 14
Content-Type: application/json
'''
    sorted_headers_string = '''\
Connection: close
Content-Length: 14
Content-Type: application/json
'''
    sorted_headers = headers_formatter.format_headers(headers_string)
    assert sorted_headers_string == sorted_headers

# Generated at 2022-06-13 22:11:15.954279
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    line = "Accept: text/html"
    line1 = "Content-Type: text/html"
    line2 = "Content-Type: text/plain"
    line3 = "Cookie: value1=value2"
    line4 = "Set-Cookie: name=value"
    headers = line + "\r\n" + line1 + "\r\n" +  line2 + "\r\n" + line3 + "\r\n" + line4
    result_headers = "Accept: text/html\r\nContent-Type: text/html\r\nContent-Type: text/plain\r\nCookie: value1=value2\r\nSet-Cookie: name=value"
    result = HeadersFormatter().format_headers(headers)
    assert result == result_headers


# Unit testing for method