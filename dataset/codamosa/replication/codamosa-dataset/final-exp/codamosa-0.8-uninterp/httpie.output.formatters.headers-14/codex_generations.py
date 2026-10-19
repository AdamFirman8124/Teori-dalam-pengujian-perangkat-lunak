

# Generated at 2022-06-13 22:01:49.978407
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.plugins.builtin import HTTPBasicAuth

    formatter = HeadersFormatter({'headers': {'sort': True}})
    auth = HTTPBasicAuth()
    auth.update_auth(AUTH_HEADERS, {})
    assert formatter.format_headers(auth.get_headers()) == AUTH_HEADERS_SORTED



# Generated at 2022-06-13 22:02:03.451910
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:02:04.860467
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    f = HeadersFormatter()
    assert f != None


# Generated at 2022-06-13 22:02:11.304143
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """HTTP/1.1 200 OK
Content-Length: 15
Content-Type: application/json
Server: TornadoServer/6.0.2
Date: Wed, 01 Jan 2020 08:43:37 GMT

abcdefghijklm0o"""
    headers_sorted = """HTTP/1.1 200 OK
Content-Length: 15
Content-Type: application/json
Date: Wed, 01 Jan 2020 08:43:37 GMT
Server: TornadoServer/6.0.2

abcdefghijklm0o"""
    assert HeadersFormatter().format_headers(headers) == headers_sorted

#---------------------------------------------------


# Generated at 2022-06-13 22:02:14.723338
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options=1, output_file=2).__dict__ == \
    {'format_options': 1, 'output_file': 2}


# Generated at 2022-06-13 22:02:19.692804
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = """POST / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Content-Length: 5
Content-Type: application/x-www-form-urlencoded
X-Test: foo

q=str"""
    assert hf.format_headers(headers) == hf.format_headers(headers)

# Generated at 2022-06-13 22:02:24.238245
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    format_options = {
        'headers': {
            'sort': 'on'
        }
    }
    headers_formatter = HeadersFormatter(format_options=format_options)
    assert headers_formatter.enabled



# Generated at 2022-06-13 22:02:25.333876
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    pass


# Generated at 2022-06-13 22:02:29.303028
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    try:
        formatter = HeadersFormatter()
        assert(True)
    except:
        assert(False)


# Generated at 2022-06-13 22:02:39.139755
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    plugin = HeadersFormatter()
    assert plugin.format_headers("Content-Type: application/json\r\nX-Header: one\r\nX-Header: two") == "Content-Type: application/json\r\nX-Header: one\r\nX-Header: two"
    assert plugin.format_headers("Content-Type: application/json\r\nX-Header: one\r\nX-Header: two\r\nX-Something: 1") == "Content-Type: application/json\r\nX-Header: one\r\nX-Header: two\r\nX-Something: 1"

# Generated at 2022-06-13 22:02:46.439887
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_str = '''Content-Type: text/plain
Content-Length: 8
Set-Cookie: foo=bar
Set-Cookie: baz=qux'''
    headers_str2 = '''Content-Type: text/plain
Content-Length: 8
Set-Cookie: baz=qux
Set-Cookie: foo=bar'''
    result = headers_formatter.format_headers(headers_str)
    assert result == headers_str2



# Generated at 2022-06-13 22:02:53.550009
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    headers = """\
Content-Type: text/html
Date: Wed, 13 Jan 2021 23:12:46 GMT
Set-Cookie: sessionid=123abc; expires=Wed, 20 Jan 2021 23:12:46 GMT
Set-Cookie: csrftoken=456def; expires=Wed, 20 Jan 2021 23:12:46 GMT
Content-Length: 9
Server: Test-Server\
"""

# Generated at 2022-06-13 22:02:56.296904
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(enabled = True)


# Generated at 2022-06-13 22:03:06.652551
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
POST / HTTP/1.1
Host: localhost:9876
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 13
Content-Type: application/json
User-Agent: HTTPie/2.2.0

"""
    expected = """\
POST / HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 13
Content-Type: application/json
Host: localhost:9876
User-Agent: HTTPie/2.2.0

"""
    assert HeadersFormatter().format_headers(headers) == expected

# Generated at 2022-06-13 22:03:16.147076
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = 'HTTP/1.0 200 OK\r\nconnection: keep-alive\r\nserver: gunicorn/19.9.0\r\ndate: Mon, 13 May 2019 17:57:48 GMT\r\ncontent-type: application/json\r\ncontent-length: 35\r\naccess-control-allow-origin: *\r\naccess-control-allow-credentials: true\r\nvia: 1.1 vegur'

# Generated at 2022-06-13 22:03:23.351475
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = "HTTP/1.1 200\r\nContent-Type: text/plain\r\nContent-Length: 13\r\nContent-Encoding: utf-8\r\nContent-Encoding: base64\r\n\r\n"
    assert headers_formatter.format_headers(headers) == "HTTP/1.1 200\r\nContent-Encoding: utf-8\r\nContent-Encoding: base64\r\nContent-Length: 13\r\nContent-Type: text/plain\r\n\r\n"

# Generated at 2022-06-13 22:03:34.776329
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers(): # pragma: no cover
    formatter = HeadersFormatter()
    headers = """
        user-agent: httpie/0.7.2
        accept-encoding: gzip, deflate
        accept: */*
        host: api.github.com
        foo: bar
        """
    assert formatter.format_headers(headers) == """
        user-agent: httpie/0.7.2
        accept-encoding: gzip, deflate
        accept: */*
        foo: bar
        host: api.github.com
        """

# Generated at 2022-06-13 22:03:38.561949
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    opts = {'headers': {'sort': True}}
    headers = HeadersFormatter(format_options=opts)
    assert headers.enabled == True
    assert not hasattr(headers, 'format_headers')


# Generated at 2022-06-13 22:03:40.809468
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter()
    assert headers_formatter.enabled == False


# Generated at 2022-06-13 22:03:45.943782
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    h = HeadersFormatter(
        format_options = {
            'headers': {
                'sort': True
            }
        }
    )

    assert isinstance(h, HeadersFormatter)
    assert h.enabled
    assert h.format_options == {
            'headers': {
                'sort': True
            }
        }


# Generated at 2022-06-13 22:03:55.102905
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = """\
GET / HTTP/1.1
Host: example.org
Foo: bar
Baz: qux
""".strip()
    assert formatter.format_headers(headers) == """\
GET / HTTP/1.1
Baz: qux
Foo: bar
Host: example.org
""".strip()



# Generated at 2022-06-13 22:04:03.250132
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    response_headers = """HTTP/1.1 200 OK
Date: Wed, 01 May 2013 21:31:09 GMT
Server: Apache
X-Powered-By: PHP/5.4.13
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/html; charset=UTF-8

"""
    assert formatter.format_headers(response_headers) == """HTTP/1.1 200 OK
Connection: close
Content-Type: text/html; charset=UTF-8
Date: Wed, 01 May 2013 21:31:09 GMT
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Server: Apache
X-Powered-By: PHP/5.4.13
"""

# Generated at 2022-06-13 22:04:09.454800
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter()
    assert hf.exclude == ('b', 'body', 'h', 'headers')
    assert hf.enabled == False
    assert hf.format_options == {
            'headers': {
                'sort': False
            }
        }


# Generated at 2022-06-13 22:04:18.917260
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Length: 100
Accept-Encoding: gzip, deflate
Connection: keep-alive
Accept: */*
Content-Type: application/json
Host: localhost:3000
User-Agent: HTTPie/1.0.0-dev
'''
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == '''\
Content-Length: 100
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Host: localhost:3000
User-Agent: HTTPie/1.0.0-dev
'''

"""
Unit test for class JsonBody
This class is used in format method of class JsonBodyFormatter
"""

# Generated at 2022-06-13 22:04:29.347041
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # There are no headers with the same name, the relative order of headers does not change.
    source = [
        'Content-Disposition: form-data; name="color"',
        'Content-Type: text/plain; charset=utf-8',
        'Content-Length: 5'
    ]
    expected = '\r\n'.join(source)
    actual = HeadersFormatter().format_headers('\r\n'.join(source))
    assert expected == actual

    # The relative order of headers with the same name should be retained.
    source = [
        'Content-Type: text/plain; charset=utf-8',
        'Content-Disposition: form-data; name="color"',
        'Content-Length: 5',
        'Content-Type: audio/mpeg',
    ]

# Generated at 2022-06-13 22:04:37.643221
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    lines = [
        'Content-type: application/json', 'Date: 2020-04-01 14:25:30',
        'Content-type: application/xml', 'Host: http://host.com',
        'Accept: application/json'
    ]
    headers_in = '\r\n'.join(lines)
    lines.sort(key=lambda h: h.split(':')[0])
    headers_out = '\r\n'.join(lines)
    obj = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert obj.format_headers(headers_in + '\r\n\r\n') == headers_out + '\r\n\r\n'

# Generated at 2022-06-13 22:04:48.783137
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

# Generated at 2022-06-13 22:04:53.466006
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = {
        'headers': {},
        'sort': 0,
        'verbose': 0,
    }
    t = HeadersFormatter(format_options=formatter)
    assert t.enabled == 0


# Generated at 2022-06-13 22:05:03.031205
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = "HTTP/1.1 200 OK\r\n" +\
    "Content-Type: text/html; charset=UTF-8\r\n" +\
    "Vary: Accept-Encoding\r\n" +\
    "Date: Sun, 27 Jan 2019 16:03:18 GMT\r\n" +\
    "Server: EasyEngine 3.6.2\r\n\r\n"

# Generated at 2022-06-13 22:05:12.559168
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''
        GET / HTTP/1.1
        User-Agent: HTTPie/0.9.9
        Accept-Encoding: gzip, deflate, compress
        Accept: */*
        Host: localhost:5000
    '''
    expected = '''
        GET / HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate, compress
        Host: localhost:5000
        User-Agent: HTTPie/0.9.9
    '''
    assert headers_formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:05:26.614517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers('abc\r\nxyz:1\r\nxyz:2\r\nxyz:3\r\nxyz:4\r\nxyz:5') == 'abc\r\nxyz:1\r\nxyz:2\r\nxyz:3\r\nxyz:4\r\nxyz:5'

# Generated at 2022-06-13 22:05:36.130653
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options = {'headers': {'sort': True}}
    headers = ('HTTP/1.1 200 OK\r\n'
               'Content-Type: text/html; charset=utf-8\r\n'
               'Content-Length: 35\r\n'
               'Accept-Ranges: bytes\r\n'
               'X-Foo: Bar')
    expected = ('HTTP/1.1 200 OK\r\n'
               'Accept-Ranges: bytes\r\n'
               'Content-Length: 35\r\n'
               'Content-Type: text/html; charset=utf-8\r\n'
               'X-Foo: Bar')

# Generated at 2022-06-13 22:05:42.395824
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.2
"""
    formatted_headers = h.format_headers(headers)
    expected_headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.2
"""
    assert formatted_headers == expected_headers

# Generated at 2022-06-13 22:05:51.465195
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = """
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.9
Content-Length: 500
Accept-Language: en-US
"""
    expected = """
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US
Connection: keep-alive
Content-Length: 500
Host: httpbin.org
User-Agent: HTTPie/0.9.9
"""
    actual = formatter.format_headers(headers)
    assert actual == expected

# Generated at 2022-06-13 22:06:01.452248
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Host: httpbin.org',
        'Connection: keep-alive',
        'User-Agent: HTTPie/0.9.2',
        'Accept-Encoding: gzip, deflate',
        'Accept: */*',
        '\r\n',
    ])) == 'HTTP/1.1 200 OK\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nHost: httpbin.org\r\nUser-Agent: HTTPie/0.9.2\r\n\r\n'



# Generated at 2022-06-13 22:06:10.210794
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 98\r\n\r\n'
    ) == (
        'HTTP/1.1 200 OK\r\n'
        'Content-Length: 98\r\n'
        'Content-Type: application/json\r\n'
        '\r\n'
    )

# Generated at 2022-06-13 22:06:16.126124
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
Host: www.google.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: HTTPie/0.9.9
'''
    new_headers = '''\
Host: www.google.com
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
User-Agent: HTTPie/0.9.9
'''
    assert formatter.format_headers(headers) == new_headers

# Generated at 2022-06-13 22:06:24.482570
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hdr = """
        Content-Type: application/json
        Accept: application/json, */*
        Connection: keep-alive
        Content-Type: application/json
    """
    f = HeadersFormatter()
    f.format_options['headers']['sort'] = True
    assert f.format_headers(hdr) == """
        Content-Type: application/json
        Accept: application/json, */*
        Connection: keep-alive
        Content-Type: application/json
    """

# Generated at 2022-06-13 22:06:36.169243
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter()
    headers.format_options = {
        'headers': {
            'sort': 'on'
        }
    }
    assert (
        headers.format_headers(
            """
            HTTP/1.1 200 OK
            Header-Two: one
            Header-One: two
            """
        )
        == """
            HTTP/1.1 200 OK
            Header-One: two
            Header-Two: one
            """
    )

# Generated at 2022-06-13 22:06:47.649765
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    string = '''SET-COOKIE: 	a=1
SET-COOKIE: 	b=2
CONTENT-TYPE: 	application/xhtml+xml
CACHE-CONTROL: 	max-age=604800
CONTENT-TYPE: 	text/html; charset=UTF-8
SET-COOKIE: 	c=3'''
    result = '''SET-COOKIE: 	a=1
SET-COOKIE: 	b=2
SET-COOKIE: 	c=3
CACHE-CONTROL: 	max-age=604800
CONTENT-TYPE: 	application/xhtml+xml
CONTENT-TYPE: 	text/html; charset=UTF-8'''

# Generated at 2022-06-13 22:07:10.343808
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers("""
    Authorization: Basic YWRtaW46cGFzc3dvcmQ=
    X-Custom-Header: IAmACustomHeader
    Cookie: sessionId=123
    X-Custom-Header: IAmAlsoACustomHeader
    Accept: application/json
    Content-Type: application/x-www-form-urlencoded
    """.strip()) == """
    Authorization: Basic YWRtaW46cGFzc3dvcmQ=
    Cookie: sessionId=123
    X-Custom-Header: IAmACustomHeader
    X-Custom-Header: IAmAlsoACustomHeader
    Accept: application/json
    Content-Type: application/x-www-form-urlencoded
    """.strip()



# Generated at 2022-06-13 22:07:22.141838
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    # Create a string that represents headers

# Generated at 2022-06-13 22:07:34.039725
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    h = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'content-length: 1234',
        'Content-Type: application/json',
        'Connection: keep-alive',
        'Content-Type: text/plain',
        'Content-Type: text/html',
        'Content-Type: text/css',
        'Content-Type: text/javascript',
        'Date: Fri, 18 Sep 2020 05:47:06 GMT',
        'Connection: close',
    ])

# Generated at 2022-06-13 22:07:42.479397
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """
Content-Type: text/plain; charset=utf-8
Content-Length: 7
Connection: close
Host: localhost:8080
"""
    expected = """
Content-Type: text/plain; charset=utf-8
Connection: close
Content-Length: 7
Host: localhost:8080
"""
    actual = headers_formatter.format_headers(headers)
    assert actual == expected



# Generated at 2022-06-13 22:07:51.810731
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Server: TornadoServer/7.0.2
Content-Length: 93
Set-Cookie: crumb=BbbWTlbg5D5J;Path=/
X-Content-Type-Options: nosniff
Expires: Thu, 01 Jan 1970 00:00:00 GMT
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Date: Tue, 23 May 2017 19:24:53 GMT
Connection: close

'''

# Generated at 2022-06-13 22:08:00.437650
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """POST /post HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: httpbin.org
User-Agent: HTTPie/0.9.2


"""
    headers1 = """POST /post HTTP/1.1
Accept: application/json, */*
Content-Length: 18
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.2


"""
    test = HeadersFormatter()
    assert test.format

# Generated at 2022-06-13 22:08:11.013873
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    string = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 110\r\nDate: Sun, 31 May 2020 12:56:07 GMT\r\nPywb-Request-Timestamp: 2020-05-31T12:56:08.183978\r\nPywb-Request-Origin: pywb\r\n\r\n"
    result = formatter.format_headers(string)

# Generated at 2022-06-13 22:08:18.063467
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = 'Date: Mon, 17 Sep 2018 15:01:00 GMT\r\nContent-Type: application/json\r\n'
    describe_test = 'given an unsorted string of headers, ensures that the headers are sorted'
    assert formatter.format_headers(headers) == 'Date: Mon, 17 Sep 2018 15:01:00 GMT\r\nContent-Type: application/json\r\n', describe_test

# Generated at 2022-06-13 22:08:24.926509
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options = {'headers': {'sort': True}}
    headers = """HTTP/1.1 200 OK
Content-Length: 326
Accept-Ranges: bytes
Connection: keep-alive
Server: gunicorn/19.7.1
Date: Thu, 12 Apr 2018 00:42:41 GMT
Via: 1.1 vegur

"""
    headers_formatted = headers_formatter.format_headers(headers)
    headers_formatted_expected = """HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: keep-alive
Content-Length: 326
Date: Thu, 12 Apr 2018 00:42:41 GMT
Server: gunicorn/19.7.1
Via: 1.1 vegur

"""
    assert headers_form

# Generated at 2022-06-13 22:08:34.134498
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
POST / HTTP/1.1
Content-type: text/html
A: 1
A: 2
B: 3
C: 4
'''
    headers_expected = '''\
POST / HTTP/1.1
A: 1
A: 2
B: 3
C: 4
Content-type: text/html
'''
    headers_formatted = formatter.format_headers(headers)
    assert headers_formatted == headers_expected

# Integration test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:09:04.552774
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    line = 'GET / HTTP/1.1\r\nHost: httpbin.org\r\nAccept: application/json\r\nConnection: keep-alive\r\nUser-Agent: HTTPie/0.9.9\r\n\r\n'
    assert formatter.format_headers(line) == 'GET / HTTP/1.1\r\nAccept: application/json\r\nConnection: keep-alive\r\nHost: httpbin.org\r\nUser-Agent: HTTPie/0.9.9\r\n\r\n'

# Generated at 2022-06-13 22:09:12.624231
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('''\
HTTP/1.1 200 OK
Content-Type: application/json
Foo: Fum
Baz: Bazza
WWW-Authenticate: Basic
Content-Length: 38''') == '''\
HTTP/1.1 200 OK
Baz: Bazza
Content-Length: 38
Content-Type: application/json
Foo: Fum
WWW-Authenticate: Basic'''


# Generated at 2022-06-13 22:09:21.241552
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    hf = HeadersFormatter()
    headers = hf.format_headers("""

Content-Type: text/html; charset=utf-8
Content-Length: 27
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Sat, 28 Apr 2018 13:45:36 GMT

""")
    assert headers == """

Content-Length: 27
Content-Type: text/html; charset=utf-8
Date: Sat, 28 Apr 2018 13:45:36 GMT
Server: Werkzeug/0.14.1 Python/3.6.4

""".lstrip()

# Generated at 2022-06-13 22:09:36.017972
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(None)
    headers = """\
host: localhost:8088
x-amzn-trace-id: Root=1-5cdd2eb2-659e0d4a0b4e4c094af9b955
x-amzn-requestid: 732537b7-fb52-43d5-94bb-b2a02b9fbd26
user-agent: aws-cli/1.16.94 Python/3.7.3 Linux/4.14.77-81.58.amzn2.x86_64 botocore/1.12.84
content-type: application/x-amz-json-1.0
content-length: 1691
x-amz-date: 20190123T182356Z
"""

# Generated at 2022-06-13 22:09:49.119365
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = 'HTTP/1.1 200 OK\r\nContent-Encoding: gzip\r\nContent-Type: application/json\r\nDate: Mon, 20 Apr 2020 12:23:51 GMT\r\nServer: nginx\r\nTransfer-Encoding: chunked'
    response_headers = headers_formatter.format_headers(headers)

    # split headers by lines
    lines = response_headers.splitlines()

    # first line should be the same
    assert lines[0] == 'HTTP/1.1 200 OK'

    # lines with same header name should be kept together
    assert lines.index('Content-Type: application/json') == 2

    # sort remaining headers alphabetically
    assert lines.index('Content-Encoding: gzip') == 1
   

# Generated at 2022-06-13 22:09:58.559080
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input = ("""POST /post?foo=bar&foo=baz&baz=qux&key=value HTTP/1.1
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Content-Length: 34
Host: httpbin.org

foo=bar&foo=baz&baz=qux&key=value""")
    expected = input
    assert HeadersFormatter().format_headers(input) == expected


# Generated at 2022-06-13 22:10:08.879938
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    headers_formatter = HeadersFormatter(format_options={'headers':{'sort': True}})


# Generated at 2022-06-13 22:10:20.351185
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = Formatter()
    formatter.headers = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Server: nginx/1.10.1
Date: Fri, 20 Jan 2017 15:45:52 GMT
Content-Type: application/json
Content-Length: 464
Connection: close
Set-Cookie: _some_cookie=some_value; HttpOnly; Path=/
X-Some-Header: some value

        """

# Generated at 2022-06-13 22:10:34.909712
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:10:42.407057
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        'Content-Type: application/json\r\n'
        'X-Foo: Bar Baz\r\n'
        'X-Foo: Qux\r\n'
    ) == (
        'Content-Type: application/json\r\n'
        'X-Foo: Bar Baz\r\n'
        'X-Foo: Qux\r\n'
    )



# Generated at 2022-06-13 22:11:39.604320
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''GET / HTTP/1.1
Host: httpbin.org
Connection: keep-alive
User-Agent: HTTPie/0.9.8
Accept: application/json
Accept-Encoding: gzip, deflate, compress
Accept-Language: en-US,en;q=0.5
Cookie: _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_month=1
X-Request-Start: 1453123733570
X-Request-Id: 4419fad8-e0e8-4423-9e2f-2d1cbf55b429
X-Forwarded-Port: 443
X-Forwarded-For: 192.168.1.1
Cache-Control: no-cache
'''

# Generated at 2022-06-13 22:11:51.015151
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Server: nginx/1.8.1',
        'Date: Fri, 15 Apr 2016 12:15:18 GMT',
        'Content-Type: application/json',
        'Content-Length: 2',
        'Last-Modified: Tue, 12 Apr 2016 13:11:26 GMT',
        'Connection: keep-alive',
        'ETag: "570c8a66-2"',
        'Accept-Ranges: bytes',
        '',
        ''
    ])