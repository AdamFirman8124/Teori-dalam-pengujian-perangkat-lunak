

# Generated at 2022-06-13 22:01:50.807293
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter.name == 'headers'
    assert HeadersFormatter.__doc__ == '''\
        Sort headers by name while retaining relative order of multiple headers with the same name.
        ''' 
    assert HeadersFormatter.format_options == {'headers':{'sort':True}}
    assert HeadersFormatter.enabled == True



# Generated at 2022-06-13 22:02:01.237248
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    assert hf.format_headers('\r\n'.join([
        'GET / HTTP/1.1',
        '###: ###: ###',
        'zzz: zzz',
        'aaa: aaa',
        'bbb: bbb',
        'ccc: ccc'])) == '\r\n'.join([
            'GET / HTTP/1.1',
            '###: ###: ###',
            'aaa: aaa',
            'bbb: bbb',
            'ccc: ccc',
            'zzz: zzz'])

# Generated at 2022-06-13 22:02:17.733336
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.plugins import FormatterPluginTest
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.context import Environment
    from io import StringIO
    import os

    env = Environment()
    env.stdin = StringIO('')
    env.stdout = StringIO()
    env.stderr = StringIO()
    env.arguments = ['http']
    env.config = env.config.copy()
    env.config.__dict__.update({
        '__file__': os.devnull,
        '__name__': '',
        '__doc__': None,
        '__package__': None
    })
    env.config.default_options['output-options']['headers'].clear()

# Generated at 2022-06-13 22:02:22.458674
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers("""\
HTTP/1.1 200 OK
B: x
A: y
A: z
""") == """\
HTTP/1.1 200 OK
A: y
A: z
B: x
"""

# Generated at 2022-06-13 22:02:26.336222
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == expected


# Generated at 2022-06-13 22:02:30.406467
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options={"headers":{"sort": True}})
    assert formatter.format_options == {"headers":{"sort": True}}


# Generated at 2022-06-13 22:02:38.750506
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('\r\n'.join((
        'Host: example.com',
        'Content-type: text/plain',
        'Accept: */*',
        'Content-type: text/html',
        'Content-type: text/csv',
        'Accept-encoding: gzip',
    ))) == '\r\n'.join((
        'Host: example.com',
        'Accept: */*',
        'Accept-encoding: gzip',
        'Content-type: text/plain',
        'Content-type: text/html',
        'Content-type: text/csv',
    ))

# Generated at 2022-06-13 22:02:50.517517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    original_headers = """
    HTTP/1.1 200 OK
    Transfer-Encoding: chunked
    Content-Type: application/json
    Content-Encoding: gzip
    Server: nginx
    Date: Thu, 10 Dec 2015 15:00:21 GMT
    Connection: keep-alive
    Cache-Control: max-age=60
    """
    sorted_headers = """
    HTTP/1.1 200 OK
    Cache-Control: max-age=60
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json
    Date: Thu, 10 Dec 2015 15:00:21 GMT
    Server: nginx
    Transfer-Encoding: chunked
    """
    assert headers_formatter.format_headers(original_headers)

# Generated at 2022-06-13 22:02:51.891832
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter()
    assert formatter.enabled



# Generated at 2022-06-13 22:03:00.299826
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options['headers']['sort'] = True
    unsortheaders = '''HTTP/1.1 200 OK
Server: nginx/1.10.3
Date: Fri, 05 Jan 2018 15:01:18 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/7.1.2

'''

# Generated at 2022-06-13 22:03:05.528386
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers('A: 1\nB: 2\nA: 3') == 'A: 1\nA: 3\nB: 2'


# Generated at 2022-06-13 22:03:15.549364
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:26.860164
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    headers_formatter = HeadersFormatter()

    headers_string = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-cache
Connection: keep-alive
Date: Sun, 13 May 2018 18:24:42 GMT
Expires: -1
Pragma: no-cache
Server: Kestrel
Transfer-Encoding: chunked
X-Powered-By: ASP.NET
Content-Encoding: gzip
'''

# Generated at 2022-06-13 22:03:36.976014
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hs = HeadersFormatter(format_options={
        'headers': {'sort': True}
    })
    assert hs.format_headers('Accept: application/json\r\n'
                             'Host: example.org\r\n'
                             'Accept-Encoding: gzip\r\n'
                             'Accept: text/plain') ==\
        'Accept: application/json\r\n' \
        'Accept: text/plain\r\n' \
        'Accept-Encoding: gzip\r\n' \
        'Host: example.org'

# Generated at 2022-06-13 22:03:46.633838
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    string = '''…
Content-Type: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: 127.0.0.1:5000
Content-Length: 18
…'''

    expected = '''…
Content-Length: 18
Content-Type: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: 127.0.0.1:5000
…'''

    assert HeadersFormatter.format_headers(string) == expected

# Generated at 2022-06-13 22:03:58.467944
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    # Test data.
    url = 'https://httpbin.org/post'
    data = {'Name': ('NAME', 'N.A.M.E.'),
            'Gender': ('Male', 'Female')}
    headers = {'User-Agent': 'HTTPie/1.0.2',
               'Accept': '*/*',
               'Content-Type': 'multipart/form-data; boundary=------------------e4a4f4e4f1d4e4c4'}
    formatted_headers = {'User-Agent': 'HTTPie/1.0.2',
                         'Accept': '*/*',
                         'Content-Type': 'multipart/form-data; boundary=------------------e4a4f4e4f1d4e4c4'}

    # Create HeadersFormatter instance.


# Generated at 2022-06-13 22:04:09.833761
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '\r\n'.join(['Content-Type: text/plain',
                           'HTTPie/0.9.2',
                           'Content-Length: 12',
                           'Date: 2015-11-12'])
    expected_headers = '\r\n'.join(['Content-Type: text/plain',
                          'Content-Length: 12',
                          'Date: 2015-11-12',
                          'HTTPie/0.9.2',])
    assert HeadersFormatter(format_options={'headers': {'sort': True}}).format_headers(headers) == expected_headers

# Generated at 2022-06-13 22:04:19.368866
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    #Test 1
    headers_formatter = HeadersFormatter()
    headers_str = """HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\nDate: Sun, 22 Dec 2019 10:10:59 GMT\r\nServer: WSGIServer/0.2 CPython/3.7.3\r\nVary: Accept, Cookie\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n"""

# Generated at 2022-06-13 22:04:29.483341
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter.format_headers('Name: val\r\nName: val2') == 'Name: val\r\nName: val2'
    assert HeadersFormatter.format_headers('Name: val\r\nAnother-Name: val2') == 'Name: val\r\nAnother-Name: val2'
    assert HeadersFormatter.format_headers('Name: val\r\nAnother-Name: val1\r\nAnother-Name: val2') == \
        'Name: val\r\nAnother-Name: val1\r\nAnother-Name: val2'

# Generated at 2022-06-13 22:04:39.913530
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: application/json; charset=utf-8',
        'Transfer-Encoding: chunked',
        'Connection: keep-alive',
        'Vary: Accept-Encoding',
        'X-Powered-By: Express'
    ])) == '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Connection: keep-alive',
        'Content-Type: application/json; charset=utf-8',
        'Transfer-Encoding: chunked',
        'Vary: Accept-Encoding',
        'X-Powered-By: Express'
    ])

# Generated at 2022-06-13 22:04:52.217214
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """
    GET / HTTP/1.1
    Host: test.com
    Cookie: a=1
    Cookie: b=2
    Accept: */*
    Cookie: c=3
    Cookie: d=4
    """
    formatted_headers = """
    GET / HTTP/1.1
    Host: test.com
    Accept: */*
    Cookie: a=1
    Cookie: b=2
    Cookie: c=3
    Cookie: d=4
    """
    assert formatter._format_headers(headers) == formatted_headers

# Generated at 2022-06-13 22:05:02.170821
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    ds = ['Header: value',
          'Accept: text/html',
          'Header2 : value',
          'Header3:   value',
          'Header3: value',
          'Header3:  value',
          'Header: value',
          'Header2: value',
          'Header2: value',
          'Header:  value']
    ds_sorted = ['Header: value',
                 'Header: value',
                 'Header:  value',
                 'Header2: value',
                 'Header2: value',
                 'Header2 : value',
                 'Header3:   value',
                 'Header3:  value',
                 'Header3: value',
                 'Header3: value',
                 'Accept: text/html']
    subject = HeaderFormatter()

# Generated at 2022-06-13 22:05:13.829806
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    def test(before: str, after: str):
        hf = HeadersFormatter()
        hf.enabled = True
        actual = hf.format_headers(before)
        assert actual == after, f"\nExpected:\n{after}\nGot:\n{actual}"

# Generated at 2022-06-13 22:05:27.443575
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {
            'sort': True
        }
    })

# Generated at 2022-06-13 22:05:38.993953
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Server: nginx
Content-Type: text/plain; charset=utf-8
Content-Length: 13
Connection: keep-alive
X-Powered-By: PHP/5.5.9-1ubuntu4.29
Cache-Control: no-cache, private
Date: Tue, 26 Jun 2018 14:15:57 GMT
X-RateLimit-Remaining: 35
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *'''

# Generated at 2022-06-13 22:05:49.898393
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test on headers string with no order
    no_order = """
    User-Agent: httpie/1.0.0
    Content-Type: application/json
    Authorization: Basic dGVzdDp0ZXN0
    Accept: application/json
    """
    sorted_headers = """
    User-Agent: httpie/1.0.0
    Content-Type: application/json
    Accept: application/json
    Authorization: Basic dGVzdDp0ZXN0
    """
    formatter = HeadersFormatter()
    headers_sorted = formatter.format_headers(no_order)
    assert(headers_sorted == sorted_headers)

    # Test on headers string that are already sorted

# Generated at 2022-06-13 22:06:01.374003
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:13.721889
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {
            'sort': True
        }
    })

    headers = '''\
HTTP/1.1 200 OK
Age: 1337
Connection: keep-alive
Cache-Control: max-age=604800
ETag: "1234"
Content-Type: text/plain
Content-Length: 5
Vary: Cookie

Hello'''

    expected_headers = '''\
HTTP/1.1 200 OK
Age: 1337
Cache-Control: max-age=604800
Connection: keep-alive
Content-Length: 5
Content-Type: text/plain
ETag: "1234"
Vary: Cookie

Hello'''

    assert formatter.format_headers(headers) == expected_headers

    formatter.enabled = False

# Generated at 2022-06-13 22:06:23.661806
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
POST / HTTP/1.1
Host: localhost:8000
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
User-Agent: HTTPie/1.0.2

"""
    # Test sorted headers
    assert HeadersFormatter('headers').format_headers(headers) == """
POST / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/1.0.2

"""
    # Test unsorted headers

# Generated at 2022-06-13 22:06:35.856616
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    t = """\
HTTP/1.1 200 OK
Content-Length: 2
Cache-Control: public, max-age=60
Last-Modified: Mon, 23 May 2016 11:11:11 GMT
Accept-Ranges: bytes
Content-Type: text/html
Date: Thu, 19 Jan 2017 12:34:56 GMT
Connection: close

<!DOCTYPE html>
<html>
<body>
Hello World!
</body>
</html>
"""


# Generated at 2022-06-13 22:06:54.218831
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options=[])

# Generated at 2022-06-13 22:07:00.389593
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
HEAD / HTTP/1.1
Host: www.google.com
Foo: bar
Foo: baz
Foo: qux
Bar: 1
Bar: 2
Bar: 3
'''
    expected = '''\
HEAD / HTTP/1.1
Foo: bar
Foo: baz
Foo: qux
Bar: 1
Bar: 2
Bar: 3
Host: www.google.com
'''
    actual = HeadersFormatter().format_headers(headers)
    assert actual == expected



# Generated at 2022-06-13 22:07:05.257525
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    plugin = HeadersFormatter()
    assert plugin.format_headers('Host: example.org\n'
                                 'Connection: keep-alive\n'
                                 'Cache-Control: no-cache\n'
                                 'Accept: application/json\n'
                                 'Accept-Encoding: gzip') == (
                                 'Host: example.org\n'
                                 'Accept: application/json\n'
                                 'Accept-Encoding: gzip\n'
                                 'Cache-Control: no-cache\n'
                                 'Connection: keep-alive')

# Generated at 2022-06-13 22:07:19.570562
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers('HTTP/1.1 200 OK\r\n'
                                      'Content-Type: application/json\r\n'
                                      'Server: nginx\r\n'
                                      'ETag: "5d566db27f0cdf5d217f0dc34b30e52c"\r\n'
                                      'Content-Length: 4\r\n'
                                      'Connection: keep-alive\r\n'
                                      )

# Generated at 2022-06-13 22:07:27.213577
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:07:35.861567
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test_input = '''\
GET / HTTP/1.1
Host: localhost:8080
Accept: application/json, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
DNT: 1
Referer: http://localhost:8080/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36\
'''


# Generated at 2022-06-13 22:07:43.081739
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    HeadersFormatter_instance = HeadersFormatter() 
    assert HeadersFormatter_instance.format_headers("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 17\r\nConnection: close\r\n") == "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: 17\r\nContent-Type: text/plain\r\n"

# Generated at 2022-06-13 22:07:52.285610
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test string:
    #   - contains a mix of 1st name, 2nd name and 3rd name headers
    #   - some are repeated, some are not
    #   - order is intentionally scrambled
    headers = '''
HTTP/0.9 200 OK
Connection: Keep-Alive
Content-Type: text/html
Server: BaseHTTP/0.3 Python/2.7.6
Date: Sat, 02 May 2015 11:51:28 GMT
Connection: close
Date: Sat, 02 May 2015 11:51:28 GMT
Content-Type: text/html
Connection: close
Connection: Keep-Alive
Server: BaseHTTP/0.3 Python/2.7.6
'''
    # The expected resulant string:
    #   - headers of the same name are sorted (by name)
    #   - but within a given name,

# Generated at 2022-06-13 22:08:00.794801
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """GET / HTTP/1.1
Host: httpie.org
Connection: keep-alive
Accept-Encoding: gzip, deflate, sdch
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4
Accept: application/json
User-Agnet: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
"""
    f = HeadersFormatter(format_options={'headers': {'sort': True}})

# Generated at 2022-06-13 22:08:07.941241
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    header = 'Host:www.google.com\r\nUser-Agent:My Agent\r\nReferer:www.google.com\r\n'
    headers = HeadersFormatter.format_headers(header)
    assert headers == 'Host:www.google.com\r\nReferer:www.google.com\r\nUser-Agent:My Agent\r\n'



# Generated at 2022-06-13 22:08:30.665822
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = (
        'Content-Type: text/plain; charset=utf8\r\n'
        'Connection: close\r\n'
        'Content-Length: 12\r\n'
        'Date: Mon, 03 Aug 2020 16:20:16 GMT\r\n'
        'Server: Python/3.8 aiohttp/3.6.2\r\n'
    )
    expected = (
        'Content-Type: text/plain; charset=utf8\r\n'
        'Connection: close\r\n'
        'Content-Length: 12\r\n'
        'Date: Mon, 03 Aug 2020 16:20:16 GMT\r\n'
        'Server: Python/3.8 aiohttp/3.6.2\r\n'
    )

# Generated at 2022-06-13 22:08:31.484902
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    pass

# Generated at 2022-06-13 22:08:41.965493
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Type: application/json
Connection: keep-alive
totally-random-order: is
Content-Length: 78
totally-random-order: this
totally-random-order: valid
'''
    expected = '''\
Content-Type: application/json
Connection: keep-alive
totally-random-order: is
Content-Length: 78
totally-random-order: this
totally-random-order: valid
'''
    actual = HeadersFormatter(format_options=dict(headers=dict(sort=True))).format_headers(headers)
    assert actual == expected



# Generated at 2022-06-13 22:08:51.457063
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    # Case 1: no headers
    result = formatter.format_headers('')
    expected = ''
    assert result == expected

    # Case 2: single header
    result = formatter.format_headers('HTTP/1.1 200 OK')
    expected = 'HTTP/1.1 200 OK'
    assert result == expected

    # Case 3: multiple headers with same name
    result = formatter.format_headers('HTTP/1.1 200 OK\r\nContent-Length: 6\r\nConnection: keep-alive\r\nContent-Length: 1')
    expected = 'HTTP/1.1 200 OK\r\nContent-Length: 6\r\nContent-Length: 1\r\nConnection: keep-alive'
    assert result == expected

    # Case 4: multiple

# Generated at 2022-06-13 22:09:00.556007
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    obj = HeadersFormatter()
    result = obj.format_headers(headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nETag: W/"123456"\r\nSet-Cookie: a=b\r\nSet-Cookie: c=d\r\nDate: Sat, 02 Feb 2019 06:05:34 GMT\r\nContent-Length: 0')
    assert result == 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nDate: Sat, 02 Feb 2019 06:05:34 GMT\r\nETag: W/"123456"\r\nSet-Cookie: a=b\r\nSet-Cookie: c=d\r\nContent-Length: 0'

# Generated at 2022-06-13 22:09:09.209194
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Content-Type: text/html;charset="utf-8"
Connection: keep-alive
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
\r\n'''
    assert formatter.format_headers(headers) == '''\
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Type: text/html;charset="utf-8"
Server: nginx/1.4.6 (Ubuntu)
Vary: Accept-Encoding
'''


# Generated at 2022-06-13 22:09:13.482881
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    headers = '\r\n'.join([
        'Wibble: foo',
        'X-Foo: bar',
        'Wibble: baz',
    ])
    assert f.format_headers(headers) == '\r\n'.join([
        'Wibble: foo',
        'Wibble: baz',
        'X-Foo: bar',
    ])



# Generated at 2022-06-13 22:09:21.838274
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        '''GET / HTTP/1.1
Host: example.org
Accept: application/json
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Content-Type: application/json
Accept-Encoding: gzip
''') == '''GET / HTTP/1.1
Accept: application/json
Accept-Encoding: gzip
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Content-Type: application/json
Host: example.org
'''

# Generated at 2022-06-13 22:09:36.671606
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    test_string = """\
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Wed, 18 Apr 2018 11:55:47 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 20
Last-Modified: Sat, 13 Jan 2018 19:24:08 GMT
Connection: keep-alive
ETag: "5a5a4ac8-14"
Accept-Ranges: bytes
Cache-Control: max-age=0
Strict-Transport-Security: max-age=15768000
"""

# Generated at 2022-06-13 22:09:43.221117
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Do not mutate a literal string
    headers = '\r\n'.join(['HTTP/1.1 200 OK',
                           'Content-Type: application/json',
                           'Connection: close',
                           'Content-Length: 16',
                           'Date: Sat, 27 Apr 2019 11:45:17 GMT',
                           'Server: BaseHTTP/0.6 Python/3.6.8'])
    print(headers)
    print('\nresult:\n')
    print(formatter.format_headers(headers))
    assert (headers == formatter.format_headers(headers))

    # Mutate the string

# Generated at 2022-06-13 22:10:15.296933
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    response = """\
HTTP/1.1 200 OK
Content-Length: 2
Content-Type: application/json
Date: Thu, 24 Oct 2019 14:51:24 GMT
ETag: W/"2-L7pfEBtnxql3Psj/N9R5A"
Server: Cowboy
Vary: Origin, Accept-Encoding
Via: 1.1 vegur

[]
"""

# Generated at 2022-06-13 22:10:22.389655
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.8.3
Date: Sun, 21 Jun 2020 11:46:19 GMT
Content-type: text/html; charset=utf-8
Content-Length: 5
Last-Modified: Fri, 08 Dec 2006 17:35:39 GMT
'''
    expected_headers = '''\
HTTP/1.0 200 OK
Content-Length: 5
Content-type: text/html; charset=utf-8
Date: Sun, 21 Jun 2020 11:46:19 GMT
Last-Modified: Fri, 08 Dec 2006 17:35:39 GMT
Server: SimpleHTTP/0.6 Python/3.8.3
'''
    headers_formatter = HeadersFormatter()
    result_headers = headers_formatter.format_headers

# Generated at 2022-06-13 22:10:35.687302
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    # Test case 1 (Test is False)
    assert formatter.format_headers('\r\n'.join([
        'GET / HTTP/1.1',
        'Accept-Encoding: gzip, deflate',
        'Accept: */*',
        'Connection: keep-alive',
        ''
    ])) == '\r\n'.join([
        'GET / HTTP/1.1',
        'Accept-Encoding: gzip, deflate',
        'Accept: */*',
        'Connection: keep-alive',
        ''
    ])

    # Test case 2 (Test is True)

# Generated at 2022-06-13 22:10:48.152517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.headers import HeadersFormatterPlugin
    headers_formatter = HeadersFormatterPlugin()
    headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Content-Length: 35\r\n"
        "Content-Encoding: gzip\r\n"
        "Vary: Accept-Encoding\r\n"
        "Date: Sun, 23 Apr 2017 11:16:35 GMT\r\n"
        "Via: 1.1 vegur\r\n"
        "\r\n")
    formatter = FormatterPlugin()

# Generated at 2022-06-13 22:10:57.978076
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    actual_result = formatter.format_headers('HTTP/1.0 200 OK\r\n' \
        'Content-Type: application/json\r\n' \
        'Z: z\r\n' \
        'X-A: a\r\n' \
        'Y: y\r\n' \
        'X-B: x\r\n' \
        'X-C: c\r\n' \
        '\r\n')

# Generated at 2022-06-13 22:11:05.218669
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': 'True'}})

    input = """
            HTTP/1.1 200 OK
            foo: 1
            foo: 2
            bar: 3
            """
    output = """
             HTTP/1.1 200 OK
             bar: 3
             foo: 1
             foo: 2
             """
    assert formatter.format_headers(input) == output

# Generated at 2022-06-13 22:11:14.842231
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_raw = "GET / HTTP/1.1\r\n\r\n"
    headers_formatted = 'GET / HTTP/1.1\r\n\r\n'
    headers_formatter = HeadersFormatter()
    headers_formatted_test = headers_formatter.format_headers(headers_raw)
    assert(headers_formatted == headers_formatted_test)

    headers_raw = "GET / HTTP/1.1\r\n\r\nname: value"
    headers_formatted = "GET / HTTP/1.1\r\nname: value\r\n\r\n"
    headers_formatted_test = headers_formatter.format_headers(headers_raw)
    assert(headers_formatted == headers_formatted_test)


# Generated at 2022-06-13 22:11:20.489153
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    import os
    import pytest
    from unittest.mock import Mock
    from httpie import ExitStatus

    # FormatterPlugin
    # def format(self, context, **kwargs):
    #
    #     if context['method'] == 'HEAD' or context['request_headers'].empty():
    #         return
    #
    #     config = context['config']
    #     headers = config.format_options.get('headers')
    #
    #     if headers['sort']:
    #         context['request_headers'] = self.format_headers(context['request_headers'])


# Generated at 2022-06-13 22:11:27.554995
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    t1 = """Accept-Language: zh-CN,zh;q=0.8,en;q=0.6\r\nAllow: GET, HEAD\r\nCache-Control: max-age=0\r\n"""
    assert h.format_headers(t1) == """Accept-Language: zh-CN,zh;q=0.8,en;q=0.6\r\nAllow: GET, HEAD\r\nCache-Control: max-age=0"""


# Generated at 2022-06-13 22:11:39.471702
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = HeadersFormatter()
    headers1 = "Accept-Language: en\r\nContent-Encoding: x-gzip\r\nContent-Type: application/json\r\nfoo: bar\r\nX-Content-Type-Options: nosniff"
    sorted_headers = headers.format_headers(headers1)
    assert sorted_headers == "Accept-Language: en\r\nContent-Encoding: x-gzip\r\nContent-Type: application/json\r\nX-Content-Type-Options: nosniff\r\nfoo: bar"
