

# Generated at 2022-06-13 22:01:55.166683
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hf.format_options = {'headers': {'sort': True}}
    headers = """\
HTTP/1.1 200 OK
Vary: Accept
Server: nginx/1.4.4
Content-Type: application/json
Connection: keep-alive
Access-Control-Allow-Origin: *
Date: Mon, 22 Sep 2014 17:50:57 GMT
Content-Length: 2

{}"""
    assert hf.format_headers(headers) == """\
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 2
Content-Type: application/json
Date: Mon, 22 Sep 2014 17:50:57 GMT
Server: nginx/1.4.4
Vary: Accept

{}"""




# Generated at 2022-06-13 22:02:04.541049
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('\r\n'.join([
        'GET / HTTP/1.1',
        'Host: example.org',
        'Accept: */*',
        'Accept-Encoding: gzip, deflate',
        'Connection: keep-alive',
    ])) == '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept: */*',
        'Accept-Encoding: gzip, deflate',
        'Connection: keep-alive',
        'Host: example.org',
    ])


Plugin = HeadersFormatter

# Generated at 2022-06-13 22:02:18.285790
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    obj = HeadersFormatter()
    assert obj.format_headers('one: 1\ntwo: 2\nthree: 3') == 'one: 1\ntwo: 2\nthree: 3'
    assert obj.format_headers('one: 1\ntwo: 2\nthree: 3\nthree: 3b') == 'one: 1\ntwo: 2\nthree: 3\nthree: 3b'
    assert obj.format_headers('one: 1\ntwo: 2\nthree: 3\nthree: 3b\none: 1b') == 'one: 1\none: 1b\ntwo: 2\nthree: 3\nthree: 3b'


# Generated at 2022-06-13 22:02:27.517150
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:02:35.018779
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Content-Length: 7
Content-Type: application/json
Host: example.com
Content-Type: text/html; charset=UTF-8'''
    expected = '''Content-Length: 7
Content-Type: application/json
Content-Type: text/html; charset=UTF-8
Host: example.com'''
    assert HeadersFormatter().format_headers(headers) == expected

# Inherit properties of class FormatterPlugin
HeadersFormatter.allow_in

# Generated at 2022-06-13 22:02:44.521518
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK\r
Content-Type: application/json\r
Cache-Control: no-cache\r
Content-Length: 26\r
Date: Wed, 29 Jun 2016 13:43:08 GMT\r
Server: waitress\r
\r
"""
    expected = """\
HTTP/1.1 200 OK\r
Cache-Control: no-cache\r
Content-Length: 26\r
Content-Type: application/json\r
Date: Wed, 29 Jun 2016 13:43:08 GMT\r
Server: waitress\r
\r
"""
    assert headers_formatter.format_headers(headers) == expected

# Generated at 2022-06-13 22:02:55.038006
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
POST /post HTTP/1.1
Host: httpbin.org
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 11
Content-Type: application/json

abcdefghijk
    """
    formatter = HeadersFormatter(
        format_options={'headers': {'sort': True}}
    )
    formatted_headers = formatter.format_headers(headers)
    assert headers.splitlines()[0] == formatted_headers.splitlines()[0]

# Generated at 2022-06-13 22:03:06.782982
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    line = 'Accept-Encoding: gzip, deflate\r\nAccept-Language: en\r\nUser-Agent: Mozilla/5.0\r\nCache-Control: no-cache\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: httpbin.org\r\nConnection: keep-alive\r\n'
    out = HeadersFormatter().format_headers(line)
    assert out == 'Accept-Encoding: gzip, deflate\r\nAccept-Language: en\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: httpbin.org\r\nUser-Agent: Mozilla/5.0\r\n'

# Generated at 2022-06-13 22:03:14.473009
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    entry_headers = ('GET / HTTP/1.1\r\n'
                     'B: value 1\r\n'
                     'A: value 2\r\n'
                     'B: value 3\r\n')
    exit_headers = ('GET / HTTP/1.1\r\n'
                    'A: value 2\r\n'
                    'B: value 1\r\n'
                    'B: value 3\r\n')
    assert headers_formatter.format_headers(entry_headers) == exit_headers



# Generated at 2022-06-13 22:03:23.725440
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    plugin = HeadersFormatter(format_options={'headers':{'sort': True}})

# Generated at 2022-06-13 22:03:36.411092
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options = {'headers': {'sort': True}})
    headers = '''HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 2
Cache-Control: max-age=604800
Date: Thu, 09 Oct 2014 23:33:54 GMT

{}'''
    assert '''HTTP/1.1 200 OK
Cache-Control: max-age=604800
Content-Length: 2
Content-Type: application/json
Date: Thu, 09 Oct 2014 23:33:54 GMT

{}''' == formatter.format_headers(headers)

# Generated at 2022-06-13 22:03:45.178494
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
ACCEPT: application/json
Content-Type: application/json
AUTHORIZATION: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTE5MDMwMjgsImlkIjoxMDB9.ZWJgRmRgn9i4nCKc4z4eUDi99xJ-nkl50DQN5SZU5Ak
X_REQUEST_ID: 12345678
"""

# Generated at 2022-06-13 22:03:48.607850
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    format_options = {}
    format_options['headers'] = {'indent': 2}
    HeadersFormatter(format_options=format_options)


# Generated at 2022-06-13 22:03:50.170004
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headersformatter = HeadersFormatter()


# Generated at 2022-06-13 22:03:53.379307
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options=dict(
        headers=dict(
            sort=True,
        ),
    ))
    assert formatter.enabled is True


# Generated at 2022-06-13 22:03:55.527174
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.format_options == {'headers': {'sort': False}}


# Generated at 2022-06-13 22:04:06.008850
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    SUT = HeadersFormatter()
    # Test case data
    headers = '''GET / HTTP/1.1
Host: localhost:2020
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
User-Agent: HTTPie/1.0.3
'''
    expected = '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:2020
User-Agent: HTTPie/1.0.3
'''
    # Perform the unit test
    actual = SUT.format_headers(headers)
    assert actual == expected


# Generated at 2022-06-13 22:04:07.921192
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options={'headers': 'sort'})
    assert formatter.enabled

# Generated at 2022-06-13 22:04:18.694784
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = \
        '''Host: example.com
        User-Agent: HTTPie/2.0.0-alpha.1
        Accept-Encoding: gzip, deflate
        Accept: */*
        Connection: keep-alive
        Content-Length: 15
        Content-Type: application/json'''
    output_header = formatter.format_headers(headers)
    expected_output = \
        '''Host: example.com
        Accept: */*
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Content-Length: 15
        Content-Type: application/json
        User-Agent: HTTPie/2.0.0-alpha.1'''

# Generated at 2022-06-13 22:04:25.823387
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from httpie.context import Environment
    from httpie.config import Config

    env = Environment(stdin=six.StringIO(),
                      stdout=six.StringIO(),
                      stderr=six.StringIO())

    config = Config(env=env)

    assert isinstance(FormatterPlugin(config), HeadersFormatter)



# Generated at 2022-06-13 22:04:40.308881
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:04:47.127145
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.formatter import format_headers
    assert format_headers('''\
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: text/plain; charset=utf-8
X-Foo: Bar
X-Foo: Baz
''') == '''\
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: text/plain; charset=utf-8
X-Foo: Bar
X-Foo: Baz
'''


plugin_class = HeadersFormatter

# Generated at 2022-06-13 22:04:59.476802
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(
        format_options=dict(headers=dict(sort=True)))
    assert (formatter.format_headers(
        '''\
HTTP/1.1 200 OK
Cache-Control: private
Content-Length: 47
Content-Type: text/html; charset=utf-8
Date: Wed, 26 Oct 2016 13:48:27 GMT

<html><body><h1>It works!</h1></body></html>''') == '''\
HTTP/1.1 200 OK
Cache-Control: private
Content-Length: 47
Content-Type: text/html; charset=utf-8
Date: Wed, 26 Oct 2016 13:48:27 GMT

<html><body><h1>It works!</h1></body></html>''')

# Generated at 2022-06-13 22:05:07.086093
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """Host: localhost:5000
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 37
Content-Type: application/x-www-form-urlencoded
User-Agent: HTTPie/1.0.2

"""
    headers_formatted = formatter.format_headers(headers)
    lines_formatted = headers_formatted.splitlines()
    assert lines_formatted[1] == 'Accept: */*'
    assert lines_formatted[2] == 'Accept-Encoding: gzip, deflate'
    assert lines_formatted[3] == 'Connection: keep-alive'
    assert lines_formatted[4] == 'Content-Type: application/x-www-form-urlencoded'

# Generated at 2022-06-13 22:05:13.252530
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
  assert HeadersFormatter().format_headers("") == ""
  assert HeadersFormatter().format_headers("Content-Type: text/plain\r\n") == "Content-Type: text/plain\r\n"
  assert HeadersFormatter().format_headers("Content-Type: text/plain\r\nContent-Length: 10\r\n") == "Content-Type: text/plain\r\nContent-Length: 10\r\n"
  assert HeadersFormatter().format_headers("Content-Type: text/plain\r\nContent-Length: 10\r\nContent-Type: text/html") == "Content-Type: text/plain\r\nContent-Type: text/html\r\nContent-Length: 10\r\n"

# Generated at 2022-06-13 22:05:20.651002
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:05:26.336329
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers("GET / HTTP/1.1\r\nCookie: a=1\r\nCookie: b=2") == \
        "GET / HTTP/1.1\r\nCookie: a=1\r\nCookie: b=2"

# Generated at 2022-06-13 22:05:29.612252
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    class Test(HeadersFormatter):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
    t = Test(format_options='some options')
    assert t.format_options == 'some options'


# Generated at 2022-06-13 22:05:37.503946
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers(): 
    assert HeadersFormatter().format_headers('""\r\n"Accept: */*\r\n"A: 1\r\n"B: 1\r\n"A: 2\r\n"\r\n') == '""\r\n"Accept: */*\r\n"A: 1\r\n"A: 2\r\n"B: 1\r\n"\r\n'


# Generated at 2022-06-13 22:05:40.075710
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter(format_options=format_options_default)
    assert headers_formatter is not None


# Generated at 2022-06-13 22:05:45.960057
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headersFormatter = HeadersFormatter({'headers': {'sort': True}})
    assert headersFormatter.enabled == True


# Generated at 2022-06-13 22:05:54.340654
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Unit test for method format_headers of class HeadersFormatter
    """
    hdrs = 'HTTP/1.0 200 OK\r\n'\
        'Header1: aaa\r\n'\
        'Header2: bbb\r\n'\
        'Header1: ccc\r\n'\
        'Header2: ddd\r\n'

    hf = HeadersFormatter()
    nh = hf.format_headers(hdrs)

    assert nh == 'HTTP/1.0 200 OK\r\n'\
        'Header1: aaa\r\n'\
        'Header1: ccc\r\n'\
        'Header2: bbb\r\n'\
        'Header2: ddd\r\n'



# Generated at 2022-06-13 22:06:03.203698
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()

    # Test with an unsorted header with multiple values

# Generated at 2022-06-13 22:06:14.676455
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_input = """
    Date: Mon, 14 May 2018 18:13:29 GMT
    Content-Type: application/json
    Content-Length: 242
    Connection: keep-alive
    X-Powered-By: Express
    X-Request-Id: 5d2fe711-0e9c-487e-8c3b-ba3d07c0ab34
    ETag: W/"f2-aUZ9gUZp6FDBbfiDdA6gClQOARw"
    """

# Generated at 2022-06-13 22:06:24.449420
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Etag: "3f80f-1b6-3e1cb03b"
Accept-Ranges: bytes
Content-Length: 438
Connection: close
Content-Type: text/html; charset=UTF-8
'''.lstrip()
    result = formatter.format_headers(headers)
    assert headers == result

# Generated at 2022-06-13 22:06:36.169174
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    class Formatter:
        def format(self, headers, **kwargs):
            return headers
    formatter = Formatter()
    headers_formatter = HeadersFormatter(formatter, {'headers': {'sort': True}})
    headers = '''
    POST / HTTP/1.1
    Host: httpbin.org
    Content-Length: 40
    Content-Type: application/x-www-form-urlencoded; charset=utf-8

    '''
    headers_expected = '''
    POST / HTTP/1.1
    Content-Length: 40
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Host: httpbin.org

    '''
    assert headers_formatter.format_headers(headers) == headers_expected

# Generated at 2022-06-13 22:06:47.648278
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    request_header = {
        'host': 'httpbin.org',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Length': '19',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'HTTPie/0.11.0'
    }
    settings = {
        'headers' : {
            'sort' : True
        }
    }
    format_options = {
        'headers': {
            'sort': True
        }
    }
    session = Session()
    headers_formatter = HeadersFormatter(session=session, settings=settings, format_options=format_options)
    assert headers_formatter.enabled == True
   

# Generated at 2022-06-13 22:06:55.445919
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
GET /index.html HTTP/1.1
Content-Type: application/json
X-Forwarded-For: 203.0.113.195
Accept: */*
User-Agent: HTTPie/1.0.2
Host: example.org
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18

"""
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:01.604512
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers("") == ""
    assert formatter.format_headers("a: 1\nb: 2\nc: 3\n") == "a: 1\nb: 2\nc: 3\n"
    assert formatter.format_headers("a: 1\nb: 2\nb: 3\n") == "a: 1\nb: 2\nb: 3\n"
    assert formatter.format_headers("a: 1\nb: 2\nb: 3\na: 4\n") == "a: 1\na: 4\nb: 2\nb: 3\n"


# End of program

# Generated at 2022-06-13 22:07:11.406403
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:25.418255
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.enabled
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Transfer-Encoding: chunked\r\n'
        'Vary: Cookie\r\n'
        'Content-Type: application/json\r\n'
        'Allow: GET, HEAD, OPTIONS\r\n\r\n'
    )

# Generated at 2022-06-13 22:07:35.006141
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:37.744722
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert HeadersFormatter



# Generated at 2022-06-13 22:07:46.247773
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter.format_headers(
        r'''\
GET / HTTP/1.1
Host: example.org
Connection: close
Cookie: foo=bar
Cookie: bar=baz
''') == r'''\
GET / HTTP/1.1
Cookie: foo=bar
Cookie: bar=baz
Host: example.org
Connection: close
'''


if __name__ == '__main__':
    import sys
    import json
    from pprint import pprint

    try:
        from pygments import highlight
        from pygments.lexers import JsonLexer
        from pygments.formatters import TerminalFormatter
    except ImportError:
        # no pygments, no colors
        def highlight(s, lexer, formatter):
            return s

    json_data = json.load

# Generated at 2022-06-13 22:07:51.545573
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    format_options = {}
    format_options['headers'] = {}
    format_options['headers']['sort'] = True
    headers_formatter = HeadersFormatter(format_options)
    assert headers_formatter.enabled == True


# Generated at 2022-06-13 22:08:00.261361
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h1 = """content-type: text/html; charset="utf-8"
content-length: 8
date: Tue, 16 Apr 2019 17:04:47 GMT
x-xss-protection: 1; mode=block
"""

    h2 = """content-length: 8
date: Tue, 16 Apr 2019 17:04:47 GMT
content-type: text/html; charset="utf-8"
x-xss-protection: 1; mode=block
"""

    h3 = """x-xss-protection: 1; mode=block
date: Tue, 16 Apr 2019 17:04:47 GMT
content-type: text/html; charset="utf-8"
content-length: 8
"""
    assert h2 == HeadersFormatter().format_headers(h1)
    assert h2 == HeadersFormatter().format_headers

# Generated at 2022-06-13 22:08:10.547181
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test method format_headers of class HeadersFormatter.
    """
    headers = '\r\n'.join((
            'GET / HTTP/1.1',
            'Content-Type: application/json',
            'B: a',
            'A: c',
            'A: b',
            'C: b',
            'C: a'
    ))

    assert HeadersFormatter().format_headers(headers) == '\r\n'.join((
            'GET / HTTP/1.1',
            'A: c',
            'A: b',
            'B: a',
            'C: b',
            'C: a',
            'Content-Type: application/json',
    ))



# Generated at 2022-06-13 22:08:20.814200
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """
    Host: httpie.org
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9
    Cookie: _ga=GA1.1.1112209490.1575383737
    """
    headers = formatter.format_headers(headers)

# Generated at 2022-06-13 22:08:34.321092
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    # test sorted result with empty header name
    assert h.format_headers("\r\nFoo: bar\r\n: 1\r\nB: 1") == "\r\n: 1\r\nB: 1\r\nFoo: bar"
    # test sorted result with empty header value
    assert h.format_headers("\r\n1: \r\nFoo: bar\r\nB: 1") == "\r\n1: \r\nB: 1\r\nFoo: bar"
    # test sorted result with empty lines
    assert h.format_headers("\r\n\r\nFoo: bar\r\nB: 1") == "\r\n\r\nB: 1\r\nFoo: bar"

# Unit

# Generated at 2022-06-13 22:08:40.753264
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = "test\r\n1: 1\r\n2: 2\r\n2: 3\r\n"
    assert "test\r\n1: 1\r\n2: 2\r\n2: 3\r\n" == HeadersFormatter().format_headers(headers)


# Generated at 2022-06-13 22:08:57.813966
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    print("Start: test_HeadersFormatter")
    hd = HeadersFormatter(format_options={
                                          'headers': {'sort': True},
                                          'body': {'indent': 2}
                                          },
                          no_colors=True)
    print(hd.format_headers('GET /dummy HTTP/1.1\r\n' +
                            'Host: 127.0.0.1\r\n' +
                            'Accept: */*\r\n' +
                            'Accept-Encoding: gzip, deflate\r\n' +
                            'User-Agent: HTTPie/1.0.2\r\n' +
                            'X-Field: Value1 X-Field: Value2\r\n'))

    # Expected string:
   

# Generated at 2022-06-13 22:08:59.882545
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
  x=HeadersFormatter()
  assert x!=None


# Generated at 2022-06-13 22:09:07.054023
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    hdrsStr = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Thu, 06 Jul 2017 07:20:02 GMT\r\nServer: Apache\r\n\r\n'
    assert hf.format_headers(hdrsStr) == 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Thu, 06 Jul 2017 07:20:02 GMT\r\nServer: Apache'

# Generated at 2022-06-13 22:09:08.951616
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # assert HeadersFormatter() == HeadersFormatter()
    print('HeadersFormatter constructor is ok')


# Generated at 2022-06-13 22:09:15.676575
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = '''\
GET / HTTP/1.1
Connection: close
Content-Length: 0

'''
    hf = HeadersFormatter(format_options={'headers': {}})
    assert hf.format_headers(h) == h

    h = '''\
GET / HTTP/1.1
Connection: close
Content-Length: 0
Connection: keep-alive

'''
    hf = HeadersFormatter(format_options={'headers': {}})
    assert hf.format_headers(h) == '''\
GET / HTTP/1.1
Content-Length: 0
Connection: close
Connection: keep-alive

'''


# Generated at 2022-06-13 22:09:23.407577
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Connection: keep-alive
Date: Tue, 28 Jul 2015 23:43:06 GMT
Server: Apache/2.2.15 (CentOS)
Transfer-Encoding: chunked
Via: 1.0 example.com (MyProxy/1.0)'''

#     expected result
    expected = '''\
Connection: keep-alive
Date: Tue, 28 Jul 2015 23:43:06 GMT
Server: Apache/2.2.15 (CentOS)
Transfer-Encoding: chunked
Via: 1.0 example.com (MyProxy/1.0)'''
    headersFormatter = HeadersFormatter()
    assert headersFormatter.format_headers(headers) == expected

# Generated at 2022-06-13 22:09:32.555567
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    t = HeadersFormatter()
    actual_output = t.format_headers('GET / HTTP/1.1\r\nContent-Length: 100\r\nContent-Type: application/json\r\nA: 1\r\nA: 2\r\nA: 3\r\nA: 4\r\nB: 5\r\nB: 6\r\nB: 7\r\nC: 9\r\nC: 8')

# Generated at 2022-06-13 22:09:40.724897
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''
Content-Type: text/plain; charset=utf-8
Content-length: 37
Content-Disposition: attachment; filename=test
Content-Disposition: attachment; filename=test2
Date: Sun, 25 Aug 2019 20:30:46 GMT
Status: 200
'''
    assert HeadersFormatter().format_headers(headers) == '''
Content-Type: text/plain; charset=utf-8
Content-Disposition: attachment; filename=test
Content-Disposition: attachment; filename=test2
Content-length: 37
Date: Sun, 25 Aug 2019 20:30:46 GMT
Status: 200
'''

# Generated at 2022-06-13 22:09:51.476060
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    format_options = {
        'headers': {'sort': True}
    }
    formatter = HeadersFormatter(None, format_options)


# Generated at 2022-06-13 22:09:57.644693
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
    GET / HTTP/1.1
    Content-Type: foo/bar
    Cookie: a=1
    Cookie: b=2
    """
    h = HeadersFormatter(format_options={'headers': {'sort': False}})
    
    assert h.format_headers(headers) == headers

# Generated at 2022-06-13 22:10:22.430470
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input_headers = '''\
GET /path?foo=bar HTTP/1.1
Host: example.org
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
'''

# Generated at 2022-06-13 22:10:35.718709
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    It tests whether format_headers of HeadersFormatter class
    is functioning properly or not.
    """
    headers = '''GET / HTTP/1.1
Host: localhost:5000
User-Agent: HTTPie/1.1.1
Accept: */*
Content-Type: application/json
Authorization: Basic bWF0dGhld2FsbHBoaQ=='''
    result_headers = '''GET / HTTP/1.1
Accept: */*
Authorization: Basic bWF0dGhld2FsbHBoaQ==
Content-Type: application/json
Host: localhost:5000
User-Agent: HTTPie/1.1.1'''
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.format_headers(headers) == result

# Generated at 2022-06-13 22:10:43.600960
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('''\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
Date: Sun, 11 Oct 2020 20:40:47 GMT

''') == '''\
HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Type: text/html; charset=utf-8
Date: Sun, 11 Oct 2020 20:40:47 GMT

'''

# Generated at 2022-06-13 22:10:55.593746
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/1.0.0-dev
'''
    expected = '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/1.0.0-dev
'''
    assert HeadersFormatter(format_options={'headers': {'sort': True}}).format_headers(headers) == expected



# Generated at 2022-06-13 22:11:06.978736
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = ('Content-Type: application/json\r\n'
               'Authorization: Basic Zm9vOmJhcg==\r\n'
               'X-Foo: bar\r\n'
               'Date: 2018-09-01T14:36:18.221443\r\n'
               'Accept: */*\r\n')

# Generated at 2022-06-13 22:11:07.993029
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()


# Generated at 2022-06-13 22:11:17.650139
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    # Test with one header
    hf.format_options = {'headers': {'sort': True}}
    header = hf.format_headers('HTTP/1.1 200 OK\r\nConnection: close\r\n')
    assert header == 'HTTP/1.1 200 OK\r\nConnection: close\r\n'

    # Test with 5 headers
    hf.format_options = {'headers': {'sort': True}}
    header = hf.format_headers('HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: 18\r\nContent-Type: text/html\r\nX-Test: header\r\nDate: Fri, 26 May 2017 04:39:23 GMT\r\n')

# Generated at 2022-06-13 22:11:24.704647
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('''HTTP/1.1 200 OK
Connection: close
Content-Length: 5
Content-Type: text/html
Date: Mon, 01 Jul 2019 06:52:01 GMT

''') == '''HTTP/1.1 200 OK
Content-Length: 5
Content-Type: text/html
Connection: close
Date: Mon, 01 Jul 2019 06:52:01 GMT

'''


# Generated at 2022-06-13 22:11:32.948274
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    i = h.format_headers('HTTP/1.1 200 OK\r\n'
                         'Content-Length: 12\r\n'
                         'Content-Type: application/json\r\n'
                         'Date: Sun, 01 Jan 1970 01:01:01 GMT\r\n'
                         'ETag: "1234etag"\r\n'
                         'X-Header: 123\r\n'
                         'X-Header: 456\r\n'
                         '\r\n')

# Generated at 2022-06-13 22:11:42.613907
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    header = """HTTP/1.1 200 OK
Host: localhost:8080
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp
Accept-Encoding: gzip,deflate,br
Accept-Language: en-US,en;q=0.8,nb;q=0.6,nn;q=0.4
Cookie: _ga=GA1.1.1379317448.1476805201
"""