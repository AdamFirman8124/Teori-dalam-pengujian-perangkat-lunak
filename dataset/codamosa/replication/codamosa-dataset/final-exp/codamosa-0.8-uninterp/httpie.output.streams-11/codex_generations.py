

# Generated at 2022-06-13 22:12:34.951425
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPMessage
    conversion = Conversion()
    formatting = Formatting()
    pretty_stream = PrettyStream(
        msg = HTTPMessage(),
        with_headers = True,
        with_body = True,
        on_body_chunk_downloaded = None,
        conversion = conversion,
        formatting = formatting,
    )
    print(hasattr(pretty_stream, 'CHUNK_SIZE'))
    print(pretty_stream.CHUNK_SIZE)
    print(hasattr(pretty_stream, '_str__'))
    print(pretty_stream.__str__)
    print(hasattr(pretty_stream, '__repr__'))

# Generated at 2022-06-13 22:12:40.677518
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import json
    import httpie.output.formatters as formatters
    from httpie.models import Response
    prettyStream = PrettyStream(formatting=formatters.Formatter(),
                                        conversion=Conversion(),
                                        msg=Response(),)
    print(prettyStream.process_body(json.dumps({"a": "b"})))

# Generated at 2022-06-13 22:12:49.340003
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Tests that the process_body() method of the PrettyStream class
    # returns the correct data:
    msg = HTTPMessage()
    conversion = Conversion()
    formatting = Formatting()
    assert(BufferedPrettyStream(msg, True, True, conversion, formatting).process_body(b'A') == b'A')
    assert(BufferedPrettyStream(msg, True, True, conversion, formatting).process_body(b'\x10\xA0\x03\xFF') == b'\x10\xA0\x03\xFF')




# Generated at 2022-06-13 22:13:00.969461
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    req_data = b'GET / HTTP/1.1\r\n' \
              b'Accept: */*\r\n' \
              b'Host: www.example.com\r\n' \
              b'\r\n'
    
    req, req_body = req_data.split(b'\r\n\r\n', 1)
    req_headers, req_start_line = req.split(b'\r\n', 1)

    resp_data = b'HTTP/1.1 200 OK\r\n' \
               b'Content-Type: text/html; charset=UTF-8\r\n' \
               b'Content-Length: 14\r\n' \
               b'Connection: keep-alive\r\n' \
               b'\r\n'

# Generated at 2022-06-13 22:13:10.836471
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPResponse
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.processing import Conversion
    from httpie.output.processing import Formatting
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie import ExitStatus
    with HTTPResponse(TestEnv().request('/basic-auth/user/password',
                                        auth=HTTPBasicAuth())) as r:
        it = BufferedPrettyStream(r,
                                  with_headers=True,
                                  with_body=True,
                                  conversion=Conversion(),
                                  formatting=Formatting())
        print(it.CHUNK_SIZE)
    return ExitStatus.OK

# Generated at 2022-06-13 22:13:15.127321
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(
        status_code=200,
        headers={
            'Content-Type': 'application/json; charset=utf-8',
        }
    )
    stream = EncodedStream(msg)
    assert stream.msg == msg


if __name__ == '__main__':
    test_EncodedStream()

# Generated at 2022-06-13 22:13:16.374769
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    a = PrettyStream()



# Generated at 2022-06-13 22:13:23.031313
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Arrange
    text_mime = 'text/plain'
    true_body = 'hello world'
    true_body_pretty = f'{true_body}\n'
    true_body_bytes = true_body.encode()
    msg = HTTPMessage('HTTP', 1.1, 200, 'OK', None, text_mime, true_body_bytes)
    stream = PrettyStream(msg=msg, conversion=None, formatting=None)
    # Act
    stream_iter = stream.iter_body()
    # Assert
    stream_body = b''.join(stream_iter)
    assert stream_body == true_body_pretty.encode(), 'fail'


# Generated at 2022-06-13 22:13:36.530387
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    env = Environment()
    headers = ["Content-Type: application/json", "Access-Control-Allow-Origin: *"]
    body = "{" + "\n" + "    \"firstName\": \"John\"," + "\n" + "    \"lastName\": \"Smith\"," + "\n" + "    \"age\": 25" + "\n" + "}" + "\n"
    msg = HTTPMessage(env=env, headers=headers, body=body, content_type="application/json")
    rawStream = RawStream(msg=msg, with_headers=True, with_body=True)
    result = [i for i in rawStream.iter_body()]
    assert bytes("Content-Type: application/json".encode("utf-8")) in result[0]

# Generated at 2022-06-13 22:13:42.988232
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    class MyEncodedStream(EncodedStream):
        CHUNK_SIZE = 10
        encoding = 'utf8'

    class HTTPMessage(object):
        def iter_body(self, chunk_size):
            return ([
                ('line1\n', b'\n'), ('line2', b''), ('line3', b'\n')
            ], [
                ('line4\n', b'\n'), ('line5', b'\n'), ('line6', b'\n')
            ])[0]


# Generated at 2022-06-13 22:13:59.444936
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    def on_body_chunk_downloaded(chunk):
        print("chunk: " + str(chunk))

    stream = BufferedPrettyStream(msg,
                                  with_headers=True,
                                  with_body=True,
                                  on_body_chunk_downloaded=on_body_chunk_downloaded)

    for chunk in stream.iter_body():
        print("chunk: " + str(chunk))
        assert chunk is not None
    assert True

## Unit test for method process_body of class BufferedPrettyStream

# Generated at 2022-06-13 22:14:05.572090
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(b'abc')
    es = EncodedStream(msg)

    assert es.msg == HTTPMessage(b'abc')
    assert es.with_headers is True
    assert es.with_body is True
    assert es.on_body_chunk_downloaded is None
    assert es.output_encoding is None


# Generated at 2022-06-13 22:14:14.467086
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    a = 'hello world'
    f = BytesIO(a.encode('utf8'))
    headers = CaseInsensitiveDict({'content-type': 'text/html'})
    msg = HTTPMessage(headers, f, None, None, None)
    stream = RawStream(msg, with_headers=True, with_body=True)
    for i in stream:
        assert i == a.encode('utf8')
        break



# Generated at 2022-06-13 22:14:24.404238
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(
        protocol=b'HTTP',
        status_code=200,
        reason=b'OK',
        headers={
            'Content-Type': 'application/json',
            'Content-Encoding': 'utf8'
        },
        body='{\n    "test": "文本信息"\n}\n'
    )

    for stream in (EncodedStream, RawStream, PrettyStream, BufferedPrettyStream):
        print(f'Testing {stream.__name__}')
        stream = stream(
            msg=msg,
            with_headers=True,
            with_body=True,
            env=Environment(stdout_isatty=True)
        )

        for line in stream:
            print(line)

test_EncodedStream()

# Generated at 2022-06-13 22:14:30.464062
# Unit test for constructor of class RawStream
def test_RawStream():
    '''
    Display non-binary response in terminal
    '''
    from httpie.models import HTTPResponse
    from httpie.output.streams import RawStream

    response = HTTPResponse(encoding = 'utf8')
    raw = RawStream(response)
    assert raw.chunk_size == 102400


# Generated at 2022-06-13 22:14:35.858629
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(msg=None, with_headers=False, with_body=False, on_body_chunk_downloaded=None)
    chunk = b'hello world'
    assert 'hello world' == stream.process_body(chunk)

# Generated at 2022-06-13 22:14:38.709611
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    msg.headers = 'header1: value1\nheader2: value2'
    p = PrettyStream(msg)
    assert p.get_headers() == b'header1: value1\nheader2: value2'
    assert p.output_encoding == 'utf8'


# Generated at 2022-06-13 22:14:47.110561
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():

    msg = HTTPMessage(body=b'1\r\n2\r\n')
    stream = PrettyStream(msg, conversion=Conversion(), formatting=Formatting())
    """
    iter_lines returns bytestring, so body must return bytestring.
    In this test, the body has binary content, and each call to iter_body will
    raise an error.
    """
    assert next(stream.iter_body()) == b'1\n2\n'

# Generated at 2022-06-13 22:14:48.613899
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    for chunk in RawStream(msg = HTTPMessage()).iter_body():
        return chunk


# Generated at 2022-06-13 22:14:58.945436
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import pytest
    from httpie.models import HTTPResponse
    from httpie.status import ExitStatus
    from httpie import ExitStatus
    # HTTP Response 200
    # No body
    with pytest.raises(AssertionError):
        msg = HTTPResponse(
            url='http://httpbin.org/',
            status_code=200,
            headers={},
            content=''
        )
        BaseStream(
            msg=msg,
            with_headers=False,
            with_body=False,
        )
    # No body
    msg = HTTPResponse(
        url='http://httpbin.org/',
        status_code=200,
        headers={},
        content=''
    )

# Generated at 2022-06-13 22:15:12.735920
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    s = BufferedPrettyStream(
        msg='test',
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )
    assert s.msg == 'test'
    assert s.with_headers == True
    assert s.with_body == True
    assert s.on_body_chunk_downloaded == None


# Generated at 2022-06-13 22:15:25.684327
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    class MockStream(PrettyStream):
        pass
    # Initialize the HTTP message
    msg = HTTPMessage(start_line=b'', headers=b'Content-Type: text/plain', body=b'')
    # Initialize the conversion
    c = Conversion()
    # Initialize the formatting
    f = Formatting()
    # Initialize class BufferedPrettyStream
    stream = MockStream(msg=msg, conversion=c, formatting=f, with_headers=False, with_body=True)
    # Test the process_body function, expected output is bytes object
    assert stream.process_body(b"httpie") == b"httpie"
    assert stream.process_body(b"httpie\n") == b"httpie\n"

# Generated at 2022-06-13 22:15:33.427438
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class MockMessage(HTTPMessage):
        def __init__(self, encod, headers, body):
            super().__init__(encod, headers, body)
        def iter_body(self, chunk_size):
            yield self.body

    import httpie.output.streams
    env = Environment()
    conversion = Conversion()
    formatting = Formatting()
    ret_iter_body = []

    headers = {'h': 'H'}
    body = b"Hello World"
    msg = MockMessage('utf8', headers, body)
    def on_body_chunk_downloaded(chunk):
        pass
    stream = BufferedPrettyStream(
        msg,
        env,
        conversion,
        formatting,
        on_body_chunk_downloaded
    )

# Generated at 2022-06-13 22:15:44.456140
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.models import HTTPRequest
    h = HTTPRequest()
    h.body = "a\nb"
    h.headers = h.headers.add('c', 'd')
    assert not h.headers.get('Content-Length')
    assert len(h.body) == 3
    rs = RawStream(h, with_headers=True, with_body=True)
    assert list(rs.iter_body()) == [b'a\nb']
    rs = RawStream(h, with_headers=True, with_body=False)
    assert list(rs.iter_body()) == []
    rs = RawStream(h, with_headers=False, with_body=True)
    assert list(rs.iter_body()) == [b'a\nb']

# Generated at 2022-06-13 22:15:45.956936
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    pass


# Generated at 2022-06-13 22:15:53.237956
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # TODO: right now this is a fully-fledged unit test, please refactor
    #       to a doctest (or similar)
    env = Environment()
    msg = HTTPMessage(headers=[('Content-Type', 'text/plain')],
                      body=b'body',
                      encoding='utf-8')
    # Preserve the message encoding if the output is not a terminal:
    assert EncodedStream(msg, env=env).output_encoding == 'utf-8'
    # Default to utf-8 if the message encoding is not specified:
    assert EncodedStream(msg, encoding=None, env=env).output_encoding == 'utf-8'

    # Use the encoding supported by the terminal:
    old_encoding = env.stdout_encoding

# Generated at 2022-06-13 22:15:54.848894
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    stream = BufferedPrettyStream()
    assert isinstance(stream, BufferedPrettyStream)

# Generated at 2022-06-13 22:16:01.505911
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    pretty_stream = PrettyStream(None, None)
    str_body = "body"
    bytes_body = b"body"
    assert pretty_stream.process_body(str_body) == b"body"
    assert pretty_stream.process_body(bytes_body) == b"body"

# Generated at 2022-06-13 22:16:12.074616
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Create a stream
    body_chunk = b"{\"hello\":\"world\"}"
    stream = PrettyStream(msg=None, with_headers=False, with_body=True)
    # process_body does not change the body chunk
    assert body_chunk == stream.process_body(body_chunk)
    # process_body changes the body chunk, when formatting
    stream.formatting = Formatting({"indent": 0})
    assert b"\n{\"hello\":\"world\"}\n" == stream.process_body(body_chunk)


# Testing method get_headers of class BaseStream

# Generated at 2022-06-13 22:16:18.921896
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(
        str.encode("HTTP/1.1 200 OK\r\n"),
        str.encode("Content-Type: text/plain; charset=UTF-8\r\n"),
        str.encode("Content-Length: 20\r\n\r\n"),
        b"hello\n world"
        )
    s = EncodedStream(msg=msg, with_body=True)
    assert [line for line in s.iter_body()] == [b"hello\n world"]

# Generated at 2022-06-13 22:16:49.753635
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage(headers=None, body=None, encoding=None, content_type=None, 
                     downloaded_size=None, download_started=None, num_of_redirects=None, 
                     excluded_headers=None, timeout=None, request=None, response=None)
    msg.headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
    msg.body = '''<html>
    <head>
        <title>test html</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>'''
    # msg.encoding = 'utf-8'
    msg.content_type = "text/html"
    conversion = Conversion('auto')
    formatting

# Generated at 2022-06-13 22:16:56.549917
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import requests
    url_str = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    res = requests.get(url_str)
    bps = BufferedPrettyStream(msg=res, on_body_chunk_downloaded=None, with_headers=True, with_body=True)
    for body_chunk in bps.iter_body():
        print(body_chunk)
    


# Generated at 2022-06-13 22:17:05.348228
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # mock a response
    headers = {'Content-Type':'text/plain; charset=utf8',
               'Content-Length': '21'}
    body = b'\xe2\x85\x94\n\xe2\x85\x95\n\xe2\x85\x96'
    msg = HTTPMessage(200, 'OK', headers, body)
    # test
    stream = EncodedStream(msg)
    for item in stream.__iter__():
        print(item)

# Generated at 2022-06-13 22:17:16.418584
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """If the content is binary, BinarySuppressedError is thrown"""
    # Create an instance of HTTPMessage, which stores the headers and body of an HTTP message.
    # HTTPMessage is the superclass of HTTPResponse and HTTPRequest.
    # This function is called with an object of HTTPResponse or HTTPRequest,
    # but here we use HTTPMessage since it allows us to create headers and body as we like.
    msg = HTTPMessage()
    msg.headers = 'a:b'
    msg.content = b'\0'

    # Create an instance of BufferedPrettyStream
    bps = BufferedPrettyStream(msg)

    # Call the iter_body method and catch the exception

# Generated at 2022-06-13 22:17:19.968991
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    p = PrettyStream(None, None, None, None, None)
    line = 'blah\n'
    rv = p.process_body(line)
    assert rv == line.encode()
    assert isinstance(rv, bytes)



# Generated at 2022-06-13 22:17:31.185105
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import json
    import sys
    import httpie.output.formatters
    import httpie.output.processors

    def parse_formatter_option(option):
        if option is None:
            return httpie.output.formatters.FORMAT_NONE
        else:
            return httpie.output.formatters.get_formatter(option)

    class TestEnvironment:
        stdin_isatty = sys.stdin.isatty()
        stdout_isatty = sys.stdout.isatty()

        stdin_encoding = None
        stdout_encoding = 'utf8'

    class TestResponse:
        def __init__(self, body, encoding=None, mime=None):
            self.headers = []
            self.body = body
            self.encoding = encoding

# Generated at 2022-06-13 22:17:43.338569
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import json
    mock_msg = HTTPMessage(content_type='application/json')
    mock_msg.headers = json.dumps(['a', 'b', 'c'])
    mock_msg.encoding = 'utf8'
    mock_formatting = Formatting(None, None)
    mock_conversion = Coversion()
    s = PrettyStream(mock_msg, conversion=mock_conversion, formatting=mock_formatting)
    s.mime = 'application/json'
    assert list(s.iter_body())[0].decode('utf8') == '[\n  "a",\n  "b",\n  "c"\n]'


# Generated at 2022-06-13 22:17:51.261378
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import pytest
    from httpie import ExitStatus
    from utils import http, HTTP_OK
    from fixtures import (
        UNICODE_LOCALE_HEADERS_RESPONSE,
        BINARY_SUPPRESSED_NOTICE,
        MULTIPART_ENCODED_ITEMS_RESPONSE,
        MULTIPART_BOUNDARY,
    )

    http('--print=B', '--pretty=all', 'GET', httpbin.url + '/get',
         env=ENV_SESSION_TEST, error_exit_ok=True)
    assert not ExitStatus.OK

    r = http('--print=B', '--pretty=all', 'GET', httpbin.url + '/get',
             env=ENV_SESSION_TEST, error_exit_ok=True)

# Generated at 2022-06-13 22:18:01.965039
# Unit test for constructor of class RawStream
def test_RawStream():
    # Create a RawStream object
    r = RawStream()

    # Test if the object is an instance of RawStream
    assert isinstance(r, RawStream)

    # Test if the object is an instance of BaseStream
    assert isinstance(r, BaseStream)

    # Test if the object is not an instance of EncodedStream
    assert not isinstance(r, EncodedStream)

    # Test if the object is not an instance of PrettyStream
    assert not isinstance(r, PrettyStream)

    # Test if the object is not an instance of BufferedPrettyStream
    assert not isinstance(r, BufferedPrettyStream)



# Generated at 2022-06-13 22:18:08.328788
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    actual = EncodedStream(msg=HTTPMessage(headers="HHH", body="B"), with_headers=True, with_body=True).iter_body()
    expected = ["HHH", "\r\n\r\n", "B"]
    assert actual == expected

# Generated at 2022-06-13 22:19:01.358175
# Unit test for constructor of class EncodedStream
def test_EncodedStream():

    env = Environment(stdout_isatty=False)
    msg = HTTPMessage(headers='', headers_encoding='utf8')
    stream = EncodedStream(msg, env=env)
    assert stream.output_encoding == 'utf8'
    assert hasattr(stream, 'msg')
    assert hasattr(stream, 'on_body_chunk_downloaded')
    assert hasattr(stream, 'with_body')
    assert hasattr(stream, 'with_headers')

    env = Environment(stdout_isatty=True)
    msg = HTTPMessage(headers='', encoding='ascii')
    stream = EncodedStream(msg, env=env)
    assert stream.output_encoding == 'utf8'

# Generated at 2022-06-13 22:19:09.775584
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    print("Testing PrettyStream class")

    msg = HTTPMessage()
    msg.content_type = 'text/html'
    msg.body = '<html><body></body></html>'
    msg.encoding = 'utf-8'

    conversion = Conversion()
    formatting = Formatting(None)
    pretty_stream = PrettyStream(msg, conversion, formatting)

    print("Testing process_body")
    pretty_stream.process_body("<html>\n<body>\n</body>\n</html>")
    print("Successfully tested process_body")

test_PrettyStream_process_body()

# Generated at 2022-06-13 22:19:19.024533
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(None)
    msg.encoding = 'utf-8'
    msg.headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'
    msg.body = bytes('This is a test', msg.encoding)
    stream = RawStream(msg)
    l = list(stream.iter_body())
    right = [bytes('This is a test', 'utf-8')]
    print('l: {0}, right: {1}'.format(l, right))
    assert l == right



# Generated at 2022-06-13 22:19:26.767252
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    print('httpie.output.streams.PrettyStream:')
    print(PrettyStream.__doc__)
    print('msg:')
    msg = HTTPMessage(content_type='text/plain; charset=test', encoding='test')
    print(msg.headers)
    print('msg.body:', msg.body)


# Unit test of method get_headers() of class PrettyStream

# Generated at 2022-06-13 22:19:41.396793
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    msg = HTTPMessage(
        request_line=(b'POST', b'http://httpbin.org/post', b'HTTP/1.1'),
        headers=[(b'Content-Type', b'application/json'), (b'Content-Length', 9)]
    )
    msg.body = '"abc"'
    assert list(msg) == [b'Content-Type: application/json\r\n', b'Content-Length: 9\r\n', b'\r\n', b'"abc"']
    assert list(BaseStream(msg, with_headers=False, with_body=True)) == [b'"abc"']

# Generated at 2022-06-13 22:19:48.076334
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    # Given
    msg = HTTPMessage(b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"name": 1, "age": 2}', 'UTF-8')
    stream = BaseStream(
        msg=msg,
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )

    # When
    for chunk in stream.__iter__():
        print(chunk)

    # Then
    assert True

# Generated at 2022-06-13 22:19:55.899176
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # 1,2. test invalid input
    # 1. test invalid input of the subclass
    try:
        EncodedStream(msg=None)
    except Exception as e:
        assert type(e) == TypeError
    # 2. test invalid input of the parent class
    try:
        EncodedStream(msg=None, with_headers=None)
    except Exception as e:
        assert type(e) == TypeError
    # 3. test empty constructor
    EncodedStream(msg=HTTPMessage())
    # 4. test constructor with valid inputs
    EncodedStream(msg=HTTPMessage(), with_headers=True, with_body=True)



# Generated at 2022-06-13 22:20:01.818291
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    prettystream = PrettyStream(msg = '')
    assert prettystream.process_body(b'blabla') == b'blabla'
    assert prettystream.process_body(b'blabla\x00') == b''
    assert prettystream.process_body(b'\x7f') == b''


# Generated at 2022-06-13 22:20:08.148676
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPResponse
    from httpie.output.streams import BufferedPrettyStream

    msg = HTTPResponse({'Content-Type': 'text/html'}, b'<span>5</span>')

    def test_data(data:bytes):
        assert data == b'<span>5</span>'

    base_stream = BufferedPrettyStream(msg, with_headers=False, with_body=True,
                                       on_body_chunk_downloaded=test_data)

    assert bytes(next(iter(base_stream))) == b'<span>5</span>'

# Generated at 2022-06-13 22:20:19.051592
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import io
    from models import HTTPBinResponse

    content = str(b'\xe4\xb8\xad\xe6\x96\x87', 'utf8')
    msg = HTTPBinResponse(
        'HTTP/1.1 101 Switching Protocols\r\n'
        'Connection: Upgrade\r\n'
        'Upgrade: websocket\r\n'
        'Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r\n\r\n'
        + content
    )

    # Use a converter to convert the content from `gbk` to `utf8`.
    # So the content will be interpreted as `utf8` in function iter_body.

# Generated at 2022-06-13 22:21:50.987931
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    import httpie.core
    import httpie.core.dumpers
    import httpie.core.protocol
    import httpie.core.parser
    import httpie.compat
    import httpie.output.streams
    import httpie.output.processing
    import json

    if httpie.compat.is_py2:
        import urllib
    else:
        import urllib.parse as urllib

    res = httpie.core.protocol.Response(200, 'OK', {"Content-Type" : "text/plain"}, b'{"msg": "Hello World"}')
    conversion = httpie.output.processing.Conversion()
    formatting = httpie.output.processing.Formatting()
    env = httpie.core.Environment()
    env.stdout_isatty = True
    env.stdout

# Generated at 2022-06-13 22:21:54.277872
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import Response
    from httpie.output.processing import Conversion, Formatting
    msg = Response(headers={'Content-Type': 'text/html'}, text='Hello world!\n')
    stream = PrettyStream(msg, conversion=Conversion(), formatting=Formatting())
    lines = list(stream.iter_body())
    assert lines == ['Hello world!', '']

# Generated at 2022-06-13 22:22:07.454993
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Test for normal situation
    class DummyMsg:
        def __init__(self, encoding="utf-8", content_type=None):
            self.content_type = content_type
            self.encoding = encoding
            self._response_chunks = [(b'{"name": "John"}\n'), (b'{"name": "Doe"}\n')]
            self._response_chunk_number = 0
        def iter_body(self, chunk_size):
            for chunk in self._response_chunks:
                self._response_chunk_number = self._response_chunk_number + 1
                yield chunk
        def iter_lines(self, chunk_size):
            for chunk in self._response_chunks:
                yield chunk, b"\n"
    dmsg = DummyMsg()
    es = Enc

# Generated at 2022-06-13 22:22:11.895834
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    pm = PrettyStream(None, None, None, None, None, None, None)
    input = b'a\xe2\x80\xa6b'
    out = pm.process_body(input)
    assert input.decode('utf-8') == out.decode('utf-8')

# Generated at 2022-06-13 22:22:19.638812
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    prettyStream = PrettyStream
    raw_headers = "Content-Type: application/json; charset=UTF-8"
    raw_msg = HTTPMessage()
    raw_msg.headers = raw_headers
    prettyStream.msg = raw_msg
    prettyStream.formatting = Formatting()
    prettyStream.output_encoding = 'utf8'
    print (prettyStream.get_headers())
