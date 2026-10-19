

# Generated at 2022-06-13 22:01:51.141879
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:02:03.848260
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # --- Input ---
    # A variable that is equal to the output of http_headers.py
    # (re-formatted in a more readable way)
    headers_input = """\
HTTP/1.1 200 OK
Date: Wed, 15 Nov 2017 09:45:17 GMT
Server: Apache
Last-Modified: Tue, 14 Nov 2017 16:35:43 GMT
ETag: "2e9-563893d3cec00"
Accept-Ranges: bytes
Content-Length: 1817
Connection: close
Content-Type: text/html; charset=UTF-8

"""
    # --- Output ---
    # The formated headers outputed by the method format_headers of the
    # class HeadersFormatter

# Generated at 2022-06-13 22:02:11.147156
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    pipe = HeadersFormatter.format_headers(
        '\r\n'.join([
            'HTTP/1.1 201 Created',
            'Content-Type: application/json',
            'Set-Cookie: a=A',
            'Set-Cookie: b=B',
            'X-Foo: Foo',
            'X-Bar: Bar'
        ])
    )
    assert pipe == '\r\n'.join([
        'HTTP/1.1 201 Created',
        'Content-Type: application/json',
        'Set-Cookie: a=A',
        'Set-Cookie: b=B',
        'X-Bar: Bar',
        'X-Foo: Foo'
    ])

# Generated at 2022-06-13 22:02:14.671687
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter().__class__ == HeadersFormatter

if __name__ == "__main__":
    test_HeadersFormatter()

# Generated at 2022-06-13 22:02:19.640544
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    h = '''HTTP/1.1 200 OK\r
Host: httpie.org\r
Connection: keep-alive\r
\r
{}'''
    h1 = hf.format_headers(h)
    h2 = hf.format_headers(h1)
    assert h1 == h2

# Generated at 2022-06-13 22:02:26.338429
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
  formatter = HeadersFormatter()
  headers = '''\r\nContent-Type: application/json\r\nA: B\r\nC: D\r\nA: E'''
  assert formatter.format_headers(headers) == '''\r\nA: B\r\nA: E\r\nC: D\r\nContent-Type: application/json'''

# Generated at 2022-06-13 22:02:32.986130
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    sorted_headers = "Header1: Value1"
    unsorted_headers = "Header2: Value2\nHeader1: Value1"
    headers_formatter = HeadersFormatter()
    assert sorted_headers == headers_formatter.format_headers(sorted_headers)
    assert "Header1: Value1\nHeader2: Value2" == headers_formatter.format_headers(unsorted_headers)

# Generated at 2022-06-13 22:02:34.792493
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter=HeadersFormatter()
    assert formatter.format_options['headers']['sort']


# Generated at 2022-06-13 22:02:45.331880
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = textwrap.dedent('''\
        HTTP/1.1 201 Created
        Connection: keep-alive
        Content-Length: 0
        Content-Type: application/json
        Date: Thu, 17 Aug 2017 19:17:38 GMT
        Server: gunicorn/19.7.1
        Via: 1.1 vegur''')
    result_headers = textwrap.dedent('''\
        HTTP/1.1 201 Created
        Connection: keep-alive
        Content-Length: 0
        Content-Type: application/json
        Date: Thu, 17 Aug 2017 19:17:38 GMT
        Server: gunicorn/19.7.1
        Via: 1.1 vegur''')
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == result_headers




# Generated at 2022-06-13 22:02:49.437991
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers_formatter = HeadersFormatter(headers={
        'sort': True,
        'linesep': '\r\n',
    })
    assert headers_formatter != None



# Generated at 2022-06-13 22:02:59.768508
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        """Connection: keep-alive
        Accept-Language: en-US,en;q=0.8
        Accept: */*
        """
    ) == """Connection: keep-alive
        Accept: */*
        Accept-Language: en-US,en;q=0.8
        """

# Generated at 2022-06-13 22:03:02.391232
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Construct class HeadersFormatter
    assert HeadersFormatter()

# Unit test on date return of function format_headers

# Generated at 2022-06-13 22:03:08.757563
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test that format_headers method correctly sorts the headers
    while retaining relative order of multiple headers with the
    same name.
    """

    test_input = """\
  GET / HTTP/1.1
  content-type: application/json
  foo: bar
  foo: baz"""

    assert HeadersFormatter().format_headers(test_input) == """\
  GET / HTTP/1.1
  content-type: application/json
  foo: bar
  foo: baz"""

# Generated at 2022-06-13 22:03:14.909692
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    # Unit test for constructor of class HeadersFormatter

    headers_formatter = HeadersFormatter()

    assert headers_formatter.enabled == headers_formatter.format_options['headers']['sort']
    assert headers_formatter.format_options['headers']['sort'] == False



# Generated at 2022-06-13 22:03:23.865199
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Type: application/json
Date: Fri, 06 Nov 2015 01:04:29 GMT
Connection: keep-alive
Content-Encoding: gzip
Server: nginx/1.4.6 (Ubuntu)
Transfer-Encoding: chunked
Cache-Control: max-age=0, private, must-revalidate
'''
    expected = '''\
Content-Type: application/json
Connection: keep-alive
Content-Encoding: gzip
Cache-Control: max-age=0, private, must-revalidate
Date: Fri, 06 Nov 2015 01:04:29 GMT
Server: nginx/1.4.6 (Ubuntu)
Transfer-Encoding: chunked
'''
    assert HeadersFormatter().format_headers(headers) == expected



# Generated at 2022-06-13 22:03:37.857120
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from io import StringIO
    headers = '''HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 11
Content-Type: text/html; charset=utf-8
Date: Fri, 04 Jan 2019 00:00:00 GMT
Server: gunicorn/19.9.0

'''
    expected_headers = '''HTTP/1.1 200 OK
Content-Length: 11
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Date: Fri, 04 Jan 2019 00:00:00 GMT
Server: gunicorn/19.9.0

'''
    f = StringIO()
    f.write(headers)
    f.seek(0)
    hf = HeadersFormatter()
    assert hf.format_headers(f.read()) == expected

# Generated at 2022-06-13 22:03:43.683343
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
HTTP/1.1 200 OK
Content-Type: application/json
User-Agent: HTTPie/0.9.9
Connection: keep-alive
Content-Length: 19

"""
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 19
Content-Type: application/json
User-Agent: HTTPie/0.9.9

"""


# Generated at 2022-06-13 22:03:45.303015
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter.__name__ == "HeadersFormatter"

# Generated at 2022-06-13 22:03:54.751893
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    current_headers = "GET / HTTP/1.1\r\nAccept: application/json\r\nCache-Control: no-cache\r\nContent-Type: application/json\r\nContent-Type: application/json\r\n"
    new_headers = "GET / HTTP/1.1\r\nAccept: application/json\r\nCache-Control: no-cache\r\nContent-Type: application/json\r\nContent-Type: application/json\r\n"
    formatter = HeadersFormatter()
    formatted_headers = formatter.format_headers(current_headers)
    assert formatted_headers == new_headers

# Generated at 2022-06-13 22:03:56.146929
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    head = HeadersFormatter(options={'headers': {'sort': True}})
    assert head.enabled == True

# Generated at 2022-06-13 22:04:03.691993
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(
        format_options={"headers": {"sort": True}},
        configuration={"default_options": {"headers": {"sort": True}}}
    )
    assert formatter.enabled


# Generated at 2022-06-13 22:04:13.028356
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:04:23.259089
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    header_string = """\
POST / HTTP/1.1
Content-Type: application/json
accept-encoding: gzip, deflate
Connection: keep-alive
Content-Length: 16
Accept: */*"""
    actual = formatter.format_headers(header_string)
    expected = """\
POST / HTTP/1.1
Accept: */*
Connection: keep-alive
Content-Length: 16
Content-Type: application/json
accept-encoding: gzip, deflate"""
    assert expected == actual



# Generated at 2022-06-13 22:04:36.518794
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    results = formatter.format_headers('HTTP/1.1 200 OK\r\nServer: nginx/1.19.2\r\nContent-Type: text/html\r\n'
    'ETag: "5f2b4d32-8f4"\r\nCache-Control: max-age=0\r\nCache-Control: max-age=10\r\nCache-Control: max-age=20\r\n'
    'Set-Cookie: SID=test-sid\r\nSet-Cookie: PASS=test-pass\r\nConnection: keep-alive\r\n')
    assert results == 'HTTP/1.1 200 OK\r\n' \
                      'Cache-Control: max-age=0\r\n'

# Generated at 2022-06-13 22:04:48.604059
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    formatter = HeadersFormatter()
    headers = '''
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 1d9f112c-8a93-48a3-baed-ea89dd279c95
User-Agent: PostmanRuntime/7.15.2
Accept: */*
Host: localhost:5000
accept-encoding: gzip, deflate
Connection: keep-alive
'''
    # Ensure test data starts in unsorted state
    assert headers.splitlines()[1] != 'Accept: */*'

    # Sort the headers and ensure a different string is returned
    assert formatter.format_headers(headers) != headers

    # Ensure the returned string is in sorted order.

# Generated at 2022-06-13 22:05:00.132621
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    x = HeadersFormatter(format_options = {'headers': {'sort': True}})

# Generated at 2022-06-13 22:05:10.879493
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():

    headers_formatter = HeadersFormatter()
    headers: str

    headers = '''
        GET / HTTP/1.1
        B-1: hoge
        A-1: hoge
        B-2: huga
        C-1: piyo
        A-2: huga
        C-2: piyo
        D-1: fuga
    '''
    headers_formatted = headers_formatter.format_headers(headers)

    # -------------------------------------------------------------------------
    #  Content-Type: application/x-www-form-urlencoded
    # -------------------------------------------------------------------------
    #  A-1: hoge
    #  A-2: huga
    #  B-1: hoge
    #  B-2: huga
    #  C-1: piyo
    #  C-2:

# Generated at 2022-06-13 22:05:20.314833
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:05:27.329922
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''
Content-Type: application/json
B: b
A: a
A: b
    '''
    expected_headers = '''
Content-Type: application/json
A: a
A: b
B: b
    '''
    formatter = HeadersFormatter()
    actual_headers = formatter.format_headers(headers)

    assert actual_headers.strip() == expected_headers.strip()


# Generated at 2022-06-13 22:05:29.265289
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    t = HeadersFormatter(format_options = {'headers' : {'sort': 1}})
    assert t.enabled == True


# Generated at 2022-06-13 22:05:41.971486
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.compat import OrderedDict
    from httpie import ExitStatus

    class ValidationExit(Exception):
        def __init__(self, status):
            self.status = status

    class Resources(object):

        def __init__(self, headers):
            self.headers = headers

        def open(self, url, method='GET', headers=None, data=None, params=None,
                 files=None, auth=None, timeout=None, verify=None,
                 stream=None, allow_redirects=None):
            if headers:
                raise AssertionError('Headers must not be passed to open().')


# Generated at 2022-06-13 22:05:50.309566
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = \
    """
    User-Agent: HTTPie/0.9.9
    Accept-Encoding: gzip, deflate
    Accept: */*
    Content-Type: application/json
    Content-Length: 22
    Host: www.google.com
    """
    assert HeadersFormatter().format_headers(headers) == \
    """
    User-Agent: HTTPie/0.9.9
    Accept: */*
    Accept-Encoding: gzip, deflate
    Content-Length: 22
    Content-Type: application/json
    Host: www.google.com
    """


# Generated at 2022-06-13 22:05:59.975840
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    user_headers = {
        'User-Agent': 'httpie/0.9.2',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    headers = "\r\n".join([': '.join([h, v]) for h, v in user_headers.items()])
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == "\r\n".join([
        ': '.join([h, v]) for h, v in sorted(user_headers.items())
    ])


plugin_class = HeadersFormatter

# Generated at 2022-06-13 22:06:04.576687
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    h.format_options = {'headers': {'sort': True}}
    s = '''cache-control: no-cache
User-Agent: {_httpie_version_}
Content-Length: 3
Content-Type: application/json
Accept: application/json
'''
    assert h.format_headers(s) == '''cache-control: no-cache
Accept: application/json
Content-Length: 3
Content-Type: application/json
User-Agent: {_httpie_version_}'''

# Generated at 2022-06-13 22:06:13.331193
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    assert HeadersFormatter().format_headers(
        '''\
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: close
Content-Length: 9
Content-Type: text/html
Date: Mon, 15 Jun 2015 20:53:58 GMT
Server: Python/3.4 http.server

Hello World'''
    ) == '''\
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: close
Content-Length: 9
Content-Type: text/html
Date: Mon, 15 Jun 2015 20:53:58 GMT
Server: Python/3.4 http.server

Hello World'''

# Generated at 2022-06-13 22:06:24.615713
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headersFormatter = HeadersFormatter()
    headersFormatter.format_options['headers']['sort'] = True
    headersFormat = headersFormatter.format_headers("""\
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 31 Dec 2019 18:53:12 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 41
Connection: keep-alive
X-Powered-By: Express
ETag: W/"29-lPRzmBM6OpbU6fHLU6ADFJZQ9DY"\
""")
    lines = headersFormat.splitlines()

    assert lines[0] == "HTTP/1.1 200 OK"
    assert lines[1] == "Connection: keep-alive"
    assert lines

# Generated at 2022-06-13 22:06:34.858792
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = (
        'GET / HTTP/1.1\r\n'
        'Header1: b\r\nHeader2: a\r\nHeader1: c\r\n'
        '\r\n'  # Body
    )
    result = hf.format_headers(headers)
    assert result == (
        'GET / HTTP/1.1\r\n'
        'Header1: b\r\nHeader1: c\r\nHeader2: a\r\n'
        '\r\n'  # Body
    )

# Generated at 2022-06-13 22:06:40.898550
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(format_options={'headers': {'sort': True} })
    headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: keep-alive\r\nContent-Length: 12\r\n\r\n"
    expected_result = "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nContent-Length: 12\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    assert headers_formatter.format_headers(headers) == expected_result


# Generated at 2022-06-13 22:06:54.131379
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:06:59.217546
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    h = '''\
Content-Type: application/json
Accept: application/json, */*
X-Auth-Token: 12345
'''
    transformed_result = hf.format_headers(h)
    assert transformed_result == '''\
Content-Type: application/json
Accept: application/json, */*
X-Auth-Token: 12345
'''

# Generated at 2022-06-13 22:07:21.759590
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    input_headers = """\
Content-Type: application/json; charset=utf-8
Server: Meinheld/0.6.1
X-Powered-By: Werkzeug/0.9.1
Content-Length: 0
Date: Sun, 07 Dec 2014 16:09:21 GMT
"""
    output_headers = formatter.format_headers(input_headers)
    assert output_headers == """\
Content-Type: application/json; charset=utf-8
Content-Length: 0
Server: Meinheld/0.6.1
X-Powered-By: Werkzeug/0.9.1
Date: Sun, 07 Dec 2014 16:09:21 GMT
"""

# Generated at 2022-06-13 22:07:33.831680
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Set-Cookie: foo=bar; path=/; HttpOnly
Set-Cookie: bar=baz; path=/; HttpOnly
Content-Length: 7
Server: Werkzeug/0.15.6 Python/3.6.5
Date: Wed, 03 Oct 2018 16:38:49 GMT'''

# Generated at 2022-06-13 22:07:45.052637
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Initialize Object
    H = HeadersFormatter()
    # Setup input

# Generated at 2022-06-13 22:07:53.342370
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:08:07.777696
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers = '''HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=A04D9D9210B75554224A8506CC6C3BCF; Path=/; HttpOnly
Content-Length: 11
Content-Type: application/json
Date: Mon, 28 Oct 2019 06:01:56 GMT'''

    # Sorts headers by name while retaining relative
    # order of multiple headers with the same name.

# Generated at 2022-06-13 22:08:13.023862
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    s = """\
abc: 1
a: 2
a: b
"""
    s_correct = """\
abc: 1
a: 2
a: b
"""
    hf = HeadersFormatter()
    assert hf.format_headers(s) == s_correct
#

# Generated at 2022-06-13 22:08:22.323991
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    test_headers_formatter = HeadersFormatter()
    test_headers_formatter.format_options = \
        {'headers': {'sort': True}}
    # Test case 1
    test_headers = '''\
GET / HTTP/1.1
Host: example.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: text/html
User-Agent: python-requests/2.21.0
'''
    expected = '''\
GET / HTTP/1.1
Accept: text/html
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: example.com
User-Agent: python-requests/2.21.0
'''
    assert test_headers_formatter.format_headers(test_headers) \
        == expected
    #

# Generated at 2022-06-13 22:08:31.840704
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    HEADERS_TXT = '''\
POST /js HTTP/1.1
Host: jquery.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Connection: keep-alive
X-Custom-Header: custom-header-value
Accept: application/json

'''
    expected = '''\
POST /js HTTP/1.1
Accept: application/json
Content-Length: 11
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive
Host: jquery.com
X-Custom-Header: custom-header-value

'''
    headers_formatter = HeadersFormatter()
    assert headers_formatter.format_headers(HEADERS_TXT) == expected

# Generated at 2022-06-13 22:08:43.148868
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Content-Type: text/plain

Accept: text/html
Accept: */*
Accept-Language: gb
Accept-Language: us
Accept-Charset: iso-8859-1
Accept-Charset: unicode-1-1'''
    headers_sorted = '''Content-Type: text/plain

Accept: text/html
Accept: */*
Accept-Charset: iso-8859-1
Accept-Charset: unicode-1-1
Accept-Language: gb
Accept-Language: us'''
    formatter = HeadersFormatter()
    assert formatter.format_headers(headers) == headers_sorted

if __name__ == '__main__':
    test_HeadersFormatter_format_headers()

# Generated at 2022-06-13 22:08:51.997041
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test Case 1
    headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.9
"""

    sorted_headers = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpbin.org
User-Agent: HTTPie/0.9.9
"""

    assert sorted_headers == HeadersFormatter().format_headers(headers)

    # Test Case 2

# Generated at 2022-06-13 22:09:22.813995
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
ETag: '12345'
Date: Mon, 01 Jan 2012 00:00:00 GMT
Cache-Control: private, max-age=0
Vary: Accept-Encoding
'''
    expected_headers = '''\
HTTP/1.1 200 OK
Cache-Control: private, max-age=0
Date: Mon, 01 Jan 2012 00:00:00 GMT
ETag: '12345'
Vary: Accept-Encoding
'''
    assert formatter.format_headers(headers) == expected_headers


 

import sys


# Generated at 2022-06-13 22:09:31.691579
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Test default sort enabled
    headersFormatter1 = HeadersFormatter(format_options={
        "headers": {"sort": True}
    })
    foo_bar_headers1 = ('GET / HTTP/1.1\r\n'
                        'Foo: 1\r\n'
                        'Bar: 1\r\n'
                        'Foo: 2\r\n')
    expected_foo_bar_headers1 = ('GET / HTTP/1.1\r\n'
                                 'Bar: 1\r\n'
                                 'Foo: 1\r\n'
                                 'Foo: 2\r\n')
    assert headersFormatter1.format_headers(foo_bar_headers1) == expected_foo_bar_headers1

    # Test default sort disabled
    headersFormatter2 = HeadersForm

# Generated at 2022-06-13 22:09:41.496729
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
Server: nginx
Date: Sun, 17 May 2020 21:32:47 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 62
Connection: keep-alive
ETag: W/"3e-ngzj8MYFsvVC7DYwYpcoIaCUkjk"
Vary: Origin
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 98
Vary: Access-Control-Request-Headers
Vary: Access-Control-Request-Method
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 86400
X-Frame-Options: SAMEORIGIN

"""

# Generated at 2022-06-13 22:09:51.201093
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """\
GET / HTTP/1.1
User-Agent: httpie
Accept-Encoding: gzip, deflate
Accept: */*
Host: localhost:5000
Connection: keep-alive
X-Custom: 1
X-Custom: 2
X-Custom: 3
"""

    headers_formatted = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:5000
User-Agent: httpie
X-Custom: 1
X-Custom: 2
X-Custom: 3
"""

    assert HeadersFormatter(None, None, None).format_headers(headers) \
        == headers_formatted



# Generated at 2022-06-13 22:10:02.512462
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Date: Tue, 29 May 2018 15:04:21 GMT
Server: WSGIServer/0.1 Python/3.6.4+
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Content-Length: 42
Connection: keep-alive'''

# Generated at 2022-06-13 22:10:11.569321
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

    headers = """\
GET / HTTP/1.1
Cache-Control: no-cache
Content-Type: application/x-www-form-urlencoded
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
"""

    expected = """\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cache-Control: no-cache
Connection: close
Content-Type: application/x-www-form-urlencoded
"""

    assert headers_formatter.format_headers(headers) == expected



# Generated at 2022-06-13 22:10:23.019147
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers('HTTP/1.1 200 OK\r\n'
                                      'Date: Wed, 14 Jan 2015 21:02:35 GMT\r\n'
                                      'Content-Length: 8\r\n'
                                      'Accept-Ranges: bytes\r\n'
                                      'Content-Type: text/plain; charset=utf-8\r\n'
                                      'Content-Encoding: identity\r\n'
                                      'Connection: keep-alive\r\n')

# Generated at 2022-06-13 22:10:35.898186
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:10:45.892088
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''\
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Accept: */*
User-Agent: httpie/2.3.0
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
'''
    assert HeadersFormatter.\
        format_headers(headers) == '''\
Content-Type: application/json
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
User-Agent: httpie/2.3.0
'''

# Generated at 2022-06-13 22:10:56.607249
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'a: 1\r\n'
        'B: 2\r\n'
        'A: 3\r\n'
        'b: 4\r\n'
    )
    expected = (
        'HTTP/1.1 200 OK\r\n'
        'A: 3\r\n'
        'B: 2\r\n'
        'a: 1\r\n'
        'b: 4\r\n'
    )
    assert hf.format_headers(headers) == expected
