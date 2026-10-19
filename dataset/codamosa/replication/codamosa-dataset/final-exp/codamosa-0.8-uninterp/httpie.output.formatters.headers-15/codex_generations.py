

# Generated at 2022-06-13 22:01:55.199739
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = """
    Accept: application/json
    Connection: keep-alive
    Content-Length: 232
    Content-Type: application/json
    User-Agent: HTTPie/0.9.9
    """
    expected_result = """
    Accept: application/json
    Content-Length: 232
    Content-Type: application/json
    Connection: keep-alive
    User-Agent: HTTPie/0.9.9
    """

    from httpie.plugins.builtin import HeadersColors
    from httpie.plugins import registry

    registry.install_builtin_plugins()

    headers_formatter = HeadersFormatter()
    headers_formatter.format_options = HeadersColors().get_options()
    headers_formatter.format_options['headers']['sort'] = True

    assert headers_form

# Generated at 2022-06-13 22:02:06.785698
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers_str = 'HTTP/1.1 200 OK\r\n' \
                  'Server: nginx\r\n' \
                  'Content-Type: text/html; charset=utf-8\r\n' \
                  'Content-Length: 648\r\n' \
                  'Connection: close\r\n' \
                  'Vary: Accept-Encoding\r\n' \
                  'X-Frame-Options: SAMEORIGIN\r\n' \
                  'X-XSS-Protection: 1; mode=block\r\n' \
                  'Strict-Transport-Security: max-age=31536000'
    assert formatter.format_headers(headers_str) is not None

# Generated at 2022-06-13 22:02:10.872380
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    obj = HeadersFormatter()
    assert obj.enabled == False
    assert obj.format_options == {"headers": {"sort": False}}


# Generated at 2022-06-13 22:02:18.235974
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = "\
Host: www.google.com\r\n\
Content-Type: text\r\n\
Connection: close\r\n\
Content-Length: 26\r\n\
\r\n"
    assert HeadersFormatter().format_headers(headers) == "\
Host: www.google.com\r\n\
Connection: close\r\n\
Content-Length: 26\r\n\
Content-Type: text\r\n\
\r\n"

# Generated at 2022-06-13 22:02:25.207391
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatted_headers = format_headers(headers_str)
    lines_formatted_headers = formatted_headers.splitlines()

# Generated at 2022-06-13 22:02:30.195819
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options={'headers': {'sort': True}})
    assert HeadersFormatter(format_options={'headers': {'sort': False}})


# Generated at 2022-06-13 22:02:39.596005
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    input = '''GET / HTTP/1.1
Host: localhost:8001
Accept: application/json
Accept: text/html
Accept-Encoding: gzip, deflate
Accept-Language: en-us
Authorization: Basic bmlyZWw6cGFzc3dvcmQ=
Cache-Control: no-cache
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 10
Content-Type: application/x-www-form-urlencoded
Cookie: foo=bar
Pragma: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'''

# Generated at 2022-06-13 22:02:49.914914
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    obj = HeadersFormatter()

# Generated at 2022-06-13 22:02:54.510230
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:02.911207
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = ["GET / HTTP/1.1", "Host: example.com", "Accept: */*", "Accept-Encoding: gzip, deflate", "Connection: keep-alive"]
    t = ['Host: example.com', 'Accept: */*', 'Accept-Encoding: gzip, deflate', 'Connection: keep-alive']
    assert HeadersFormatter().format_headers('\r\n'.join(h)) == '\r\n'.join(h[:1]+t)



# Generated at 2022-06-13 22:03:15.296972
# Unit test for method format_headers of class HeadersFormatter

# Generated at 2022-06-13 22:03:23.975144
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    str = """
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 23
Content-Type: application/json
Date: Mon, 24 Oct 2016 01:22:06 GMT
Server: gunicorn/19.6.0
Via: 1.1 vegur

{
    "key1": "value1",
    "key2": "value2"
}
    """

# Generated at 2022-06-13 22:03:37.900635
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Dict of multiple headers with same name
    test_dict_list = [
        {'Content-Type': 'application/json; charset=UTF-8'},
        {'Accept': 'application/json'},
        {'Accept': 'application/json'},
        {'Access-Control-Request-Method': 'GET'},
        {'Host': 'www.google.com'},
        {'User-Agent': 'httpie'},
        {'Accept-Encoding': 'gzip, deflate'},
        {'Connection': 'keep-alive'}
    ]

    # Expected string

# Generated at 2022-06-13 22:03:43.751835
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    from httpie.plugins import FormatterPluginManager
    from httpie.cli.argtypes import KeyValueArgType

    arg_type = KeyValueArgType()
    arg_type.parse({'headers': ['authorization: Basic token', 'Content-Length: 0']})
    plugin_manager = FormatterPluginManager({}, arg_type)
    plugin_manager.get_enabled_plugins()

    assert isinstance(plugin_manager.get_enabled_plugins()[0], HeadersFormatter)


# Generated at 2022-06-13 22:03:55.349683
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    assert formatter.format_headers(
        '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 5
Host: httpbin.org
User-Agent: HTTPie/1.0.2
X-API-Token: 123456

''') == '''GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 5
Host: httpbin.org
User-Agent: HTTPie/1.0.2
X-API-Token: 123456

'''

# Generated at 2022-06-13 22:04:07.764131
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(width=80, color=False, sort=True)

# Generated at 2022-06-13 22:04:09.134213
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    HeadersFormatter()


# Generated at 2022-06-13 22:04:19.063202
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = '''Access-Control-Allow-Credentials: true
Content-Length: 2
Content-Type: application/json
Date: Mon, 03 Sep 2018 08:15:22 GMT
Server: nginx/1.10.3 (Ubuntu)
Strict-Transport-Security: max-age=63072000
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block'''

# Generated at 2022-06-13 22:04:29.417041
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter_plugin = HeadersFormatter()

    # Case: Headers with relative order of multiple headers
    #       with the same name will be retained

# Generated at 2022-06-13 22:04:37.926715
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter(format_options={
        'headers': {
            'sort': True
        }
    })
    assert headers_formatter.format_headers(
        """\
Content-type: application/json
X-Custom-Header: abc
X-Custom-Header: def
X-Custom-Header: ghi
X-Custom-Header2: abc
X-Custom-Header2: def
X-Custom-Header2: ghi

""") == """\
Content-type: application/json
X-Custom-Header: abc
X-Custom-Header: def
X-Custom-Header: ghi
X-Custom-Header2: abc
X-Custom-Header2: def
X-Custom-Header2: ghi

"""

# Generated at 2022-06-13 22:04:53.268542
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:05:02.869517
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter()
    headers_to_be_tested =\
        ('HTTP/1.1 200 OK\r\n'
         'Content-Length: 123\r\n'
         'Content-Type: application/json\r\n'
         'Some-Header: val1\r\n'
         'Some-Header: val2\r\n'
         'Some-Header: val3')

    formatted_headers = hf.format_headers(headers_to_be_tested)

# Generated at 2022-06-13 22:05:06.064697
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    f = HeadersFormatter()
    assert f.enabled == False
    assert f.format_options['headers']['sort'] == False

# Generated at 2022-06-13 22:05:15.253943
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers1 = 'GET / HTTP/1.1\r\n' \
              'accept: a\r\n' \
              'z: z\r\n' \
              'accept-encoding: gzip, deflate\r\n' \
              'user-agent: HTTPie/0.9.9\r\n' \
              '\r\n'
    headers2 = 'GET / HTTP/1.1\r\n' \
              'accept: a\r\n' \
              'accept-encoding: gzip, deflate\r\n' \
              'user-agent: HTTPie/0.9.9\r\n' \
              'z: z\r\n' \
              '\r\n'

# Generated at 2022-06-13 22:05:27.923674
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import HTTPHeaders
    from httpie.plugins.builtin import PrettyPrint
    from httpie.plugins.builtin import LineEndings

    _plugin_instances = [HTTPHeaders(), PrettyPrint(), LineEndings()]

    instance = HeadersFormatter()


# Generated at 2022-06-13 22:05:35.662114
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()
    headers_formatter.format_options = {
        'headers': {
            'sort': True
        },
    }

    assert headers_formatter.format_headers(headers='Content-Type: text/html\r\nContent-Length: 12') == \
           'Content-Length: 12\r\nContent-Type: text/html'


if __name__ == '__main__':
    test_HeadersFormatter_format_headers()

# Generated at 2022-06-13 22:05:38.281936
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter().format_options == {
        'headers': {'sort': True}
    }


# Generated at 2022-06-13 22:05:49.717729
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:05:58.068434
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

    headers = '''\
HTTP/1.1 200 OK
Content-Type: application/json
Connection: keep-alive
Content-Length: 16
\r
{
"a": "A"
}
'''
    assert formatter.format_headers(headers) == '''\
HTTP/1.1 200 OK
Content-Length: 16
Connection: keep-alive
Content-Type: application/json
\r
{
"a": "A"
}
'''


# Generated at 2022-06-13 22:06:05.355172
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    original_headers = '''\
GET / HTTP/1.1
Accept: application/json
Cache-Control: no-cache
Content-Length: 0
Content-Type: application/json
User-Agent: HTTPie/0.9.8
'''
    sorted_headers = '''\
GET / HTTP/1.1
Accept: application/json
Cache-Control: no-cache
Content-Length: 0
Content-Type: application/json
User-Agent: HTTPie/0.9.8
'''
    # Test sorting enabled
    assert formatter.format_headers(original_headers) == sorted_headers

# Generated at 2022-06-13 22:06:22.702171
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    import os
    import json
    from httpie.client import JSON_ACCEPT
    from httpie.plugins import builtin

    config_dir = os.path.dirname(__file__)
    env = TestEnvironment(config_dir=config_dir)
    config = Config(env=env)
    args = Namespace(headers=[], accept=[JSON_ACCEPT])
    http = HTTPie(config=config, env=env, args=args)
    builtin.plugins = http.plugins

    HeadersFormatter(args=args, format_options=config.format_options)


# Generated at 2022-06-13 22:06:35.817737
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    """
    Test case for method format_headers of class HeadersFormatter
    """

    headers_formatter = HeadersFormatter()
    # headers = '''
    # HTTP/1.1 200 OK
    # Content-Length: 14
    # Connection: keep-alive
    # Access-Control-Allow-Origin: *
    # Access-Control-Allow-Credentials: true
    # Content-Type: application/json
    # Date: Sat, 07 Jul 2018 19:01:25 GMT
    # Vary: Accept-Encoding
    # X-Powered-By: Express
    # '''

    headers = ''

# Generated at 2022-06-13 22:06:42.208258
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers_text = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Length: 42\r\n'
        'Cache-Control: public,max-age=3600\r\n'
        'Content-Type: application/json; charset=utf-8\r\n'
        'Etag: "12345"\r\n'
        'Content-Type: application/json\r\n'
    )

# Generated at 2022-06-13 22:06:53.539581
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """
        HTTP/1.1 200 OK
        Content-Type: text/html
        Content-Length: 300
        Connection: keep-alive
        Server: meinheld/0.6.1
        Date: Fri, 27 Oct 2017 09:56:13 GMT

        """
    headers_sorted = """
        HTTP/1.1 200 OK
        Connection: keep-alive
        Content-Length: 300
        Content-Type: text/html
        Date: Fri, 27 Oct 2017 09:56:13 GMT
        Server: meinheld/0.6.1

        """
    assert formatter.format_headers(headers) == headers_sorted

# Generated at 2022-06-13 22:07:01.652310
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers_formatter = HeadersFormatter()

# Generated at 2022-06-13 22:07:11.434466
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = '''\
HTTP/1.1 200 OK
Cache-Control: no-cache, private
Connection: close
Content-Type: application/json
Date: Thu, 21 May 2015 08:21:46 GMT
Server: BaseHTTP/0.3 Python/2.7.6
Set-Cookie: session=51e70c9b0b0d22c39f1faa3e7a3c785a
Transfer-Encoding: chunked'''
    # Notice that header Date is moved before header Content-Type

# Generated at 2022-06-13 22:07:22.365970
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={
        'headers': {'sort': True},
    })

    h = '''
header2: 123
HEADER1: 234
Header1: 555
header1: 123
'''.strip()
    assert formatter.format_headers(h) == '''
header2: 123
HEADER1: 234
header1: 123
Header1: 555
'''.strip()

    h = '''
Aaaa: 111
Aaaa: 222
Aaaa: 333
Bbbb: 444
Cccc: 555
'''.strip()
    assert formatter.format_headers(h) == '''
Aaaa: 111
Aaaa: 222
Aaaa: 333
Bbbb: 444
Cccc: 555
'''.strip()



# Generated at 2022-06-13 22:07:24.536087
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    fmt = HeadersFormatter()

# Generated at 2022-06-13 22:07:34.682953
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter(
        format_options={'headers': {'sort': True, 'key_case': 'capitalize'}}
    )

# Generated at 2022-06-13 22:07:43.968284
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # echo 'X-Foo: 1\nX-Bar: 2\nX-Bar: 3' | http --print=hB | sort
    h = 'Content-Type: application/json\r\nX-Bar: 2\r\nX-Bar: 3\r\nX-Foo: 1'
    expected_result = 'Content-Type: application/json\r\nX-Bar: 2\r\nX-Bar: 3\r\nX-Foo: 1'
    formatter = HeadersFormatter()
    assert formatter.format_headers(h) == expected_result

# Generated at 2022-06-13 22:08:03.619638
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(format_options = {'headers': {'sort': True}})
    assert formatter.enabled == True
    assert formatter.format_options == {'headers': {'sort': True}}


# Generated at 2022-06-13 22:08:12.090201
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    header_string = u'GET / HTTP/1.1\r\n' \
                    u'foo: X\r\n' \
                    u'A: Y\r\n' \
                    u'a: Z\r\n' \
                    u'B: Y\r\n' \
                    u'b: Z\r\n'
    assert formatter.format_headers(header_string) == u'GET / HTTP/1.1\r\n' \
                                                      u'A: Y\r\n' \
                                                      u'B: Y\r\n' \
                                                      u'a: Z\r\n' \
                                                      u'b: Z\r\n' \
                                                      u'foo: X\r\n'

# Generated at 2022-06-13 22:08:22.802104
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    headers = """\
HTTP/1.1 200 OK
Content-Type: application/json
Date: Mon, 27 Jul 2015 20:01:05 GMT
X-Content-Type-Options: nosniff
Server: TornadoServer/4.2.1"""
    assert formatter.format_headers(headers) == """\
HTTP/1.1 200 OK
Content-Type: application/json
Date: Mon, 27 Jul 2015 20:01:05 GMT
Server: TornadoServer/4.2.1
X-Content-Type-Options: nosniff"""

# Generated at 2022-06-13 22:08:29.525599
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    actual = b'Server: werkzeug/0.14.1\r\nSet-Cookie: name=value\r\n\r\n'
    expected = b'Server: werkzeug/0.14.1\r\nSet-Cookie: name=value\r\n\r\n'
    assert formatter.format_headers(actual) == expected

# Generated at 2022-06-13 22:08:38.551355
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'X-Token': '123-456-789',
        'X-Time': '123456789',
        'X-Location': 'Wroclaw'
    }
    headers_formatter = HeadersFormatter(format_options=headers)
    assert headers_formatter.enabled == False


# Generated at 2022-06-13 22:08:48.705208
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter(format_options = {'headers': {'sort': True}})
    headers = '''Content-Length: 0
Content-Type: application/json
Accept: text/plain, application/json
Content-Type: application/json
Cache-Control: no-cache

'''
    assert formatter.format_headers(headers) == '''Content-Length: 0
Accept: text/plain, application/json
Cache-Control: no-cache
Content-Type: application/json
Content-Type: application/json

'''



# Generated at 2022-06-13 22:09:00.229494
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers('''\
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Etag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Connection: close
Content-Type: text/plain
X-Foo: Bar
X-Foo: Foo''')

# Generated at 2022-06-13 22:09:02.340281
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = httpie.__version__
    result = HeadersFormatter().format_headers(headers)
    assert result == headers


# Generated at 2022-06-13 22:09:06.256458
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    hf = HeadersFormatter()
    assert isinstance(hf, FormatterPlugin)
    assert hf.format_options == {"headers": {"sort": False}}
    assert hf.enabled == False


# Generated at 2022-06-13 22:09:15.033505
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    f = HeadersFormatter()
    h = f.format_headers('\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: application/json',
        'Connection: keep-alive',
        'Transfer-Encoding: chunked',
        'Vary: Origin',
        'Vary: Accept-Encoding',
        'Server: gunicorn/19.9.0',
        'Date: Mon, 25 Dec 2017 16:39:57 GMT',
        'X-Frame-Options: SAMEORIGIN',
        ''
    ]))

# Generated at 2022-06-13 22:09:48.361185
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    t = HeadersFormatter(**{'format_options': {'headers': {'sort': False}}})
    assert not t.enabled
    t = HeadersFormatter(**{'format_options': {'headers': {'sort': True}}})
    assert t.enabled


# Generated at 2022-06-13 22:09:50.450873
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    obj = HeadersFormatter()
    assert obj.enabled is False


# Generated at 2022-06-13 22:10:02.200857
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    # Headers sorted in natural order
    h = HeadersFormatter()

# Generated at 2022-06-13 22:10:11.870142
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()
    result = formatter.format_headers("""\
HTTP/1.1 200 OK
Content-Length: 1234
Content-Type: application/json
X-Foo: Bar
X-Foo: Baz
""")
    assert result == """\
HTTP/1.1 200 OK
Content-Length: 1234
Content-Type: application/json
X-Foo: Bar
X-Foo: Baz
""", (
        'The method format_headers does not return the expected result')

# Generated at 2022-06-13 22:10:23.064372
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    headers = '''Host: api.github.com
Accept: application/vnd.github.v3+json, application/vnd.github.antiope-preview+json, application/vnd.github.shadow-cat-preview+json
Accept-Encoding: gzip, deflate
Connection: close
User-Agent: HTTPie/2.0.0
'''
    headers_formatted = '''Host: api.github.com
Accept: application/vnd.github.antiope-preview+json, application/vnd.github.shadow-cat-preview+json, application/vnd.github.v3+json
Accept-Encoding: gzip, deflate
Connection: close
User-Agent: HTTPie/2.0.0
'''
    assert HeadersFormatter().format_headers(headers) == headers_formatted

# Generated at 2022-06-13 22:10:35.921786
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    h = HeadersFormatter()
    assert h.format_headers('Accept: appli\r\nAccept-Encoding: deflate\r\nAccept-Language: en_US') == 'Accept: appli\r\nAccept-Encoding: deflate\r\nAccept-Language: en_US'
    assert h.format_headers('Accept-Encoding: deflate\r\nAccept: appli\r\nAccept-Language: en_US') == 'Accept: appli\r\nAccept-Encoding: deflate\r\nAccept-Language: en_US'

# Generated at 2022-06-13 22:10:42.195904
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    formatter = HeadersFormatter(print_body=False)
    if not isinstance(formatter, HeadersFormatter):
        raise RuntimeError("Invalid type for formatter instance")
    if formatter.format_options['headers']['sort'] is not True:
        raise RuntimeError("formatter.format_options['headers']['sort'] is not True")


# Generated at 2022-06-13 22:10:53.387034
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    formatter = HeadersFormatter()

# Generated at 2022-06-13 22:10:54.843949
# Unit test for constructor of class HeadersFormatter
def test_HeadersFormatter():
    assert HeadersFormatter(format_options=options)


# Generated at 2022-06-13 22:11:04.473819
# Unit test for method format_headers of class HeadersFormatter
def test_HeadersFormatter_format_headers():
    hf = HeadersFormatter(format_options={'headers': {'sort': True}})
    headers = '''\
GET / HTTP/1.1
User-Agent: HTTPie/0.9.9
Connection: keep-alive
Host: www.google.com
Accept-Encoding: gzip, deflate
Accept: */*
'''
    expected = '''\
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.google.com
User-Agent: HTTPie/0.9.9
'''
    assert hf.format_headers(headers) == expected