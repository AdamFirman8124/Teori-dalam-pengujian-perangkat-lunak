

# Generated at 2022-06-13 22:12:33.881449
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.cli import Environment
    from httpie.models import HTTPMessage
    from httpie.output.processing import Conversion, Formatting

    env = Environment()
    msg = HTTPMessage(headers = {
        'Content-Type': 'chuncked',
        'Content-Length': 0
    })
    conversion = Conversion()
    formatting = Formatting()

    stream = PrettyStream(msg, conversion, formatting)
    assert stream.mime == 'chuncked'

# Generated at 2022-06-13 22:12:39.830467
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Given
    obj = PrettyStream(None, None, None, None, None)
    chunk = b"\x00\x01\x02"
    # When
    result = obj.process_body(chunk)

    # Then
    assert result == b"\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd"

# Generated at 2022-06-13 22:12:49.564754
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    import pytest
    from httpie.models import HTTPMessage

    def test(headers, body, expected):
        msg = HTTPMessage(headers, body)
        actual = EncodedStream(msg).iter_body()
        expected = ''.join(expected)
        assert actual == expected

    test(
        [
            'Content-Type: text/plain; encoding=utf8',
            'X-Mock: 200'
        ],
        'Hello',
        ['Hello']
    )

    with pytest.raises(BinarySuppressedError):
        test(
            [
                'Content-Type: text/plain; encoding=utf8',
                'X-Mock: 200'
            ],
            b'\0World',
            ['\0World']
        )


# Generated at 2022-06-13 22:13:01.098203
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie import STATUS_CODES
    from httpie.models import HTTPStatus
    from httpie.output.streams import PrettyStream
    from httpie.output.formatters import JSONFormatter
    from httpie.compat import is_py26
    headers = {
        'Content-Type': 'application/json'
    }
    body = [{
        'id': 1,
        'name': 'A',
        'count': 1
    }, {
        'id': 2,
        'name': 'B',
        'count': 2
    }, {
        'id': 3,
        'name': 'C',
        'count': 3
    }]
    status = HTTPStatus(100, 'Continue')
    msg = HTTPMessage(headers=headers, body=[], status=status)
    msg._body

# Generated at 2022-06-13 22:13:08.524327
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    body = "This is a test\n"
    chunk = body.encode("utf8")
    msg = HTTPMessage(headers=None, content=chunk, encoding="utf8")
    conversion = Conversion()
    formatting = Formatting()
    stream = PrettyStream(conversion=conversion, formatting=formatting, msg=msg, with_headers=None, with_body=True)
    result = stream.iter_body()
    for i in range(3):
        assert next(result) == b"This is a test\n"


# Generated at 2022-06-13 22:13:12.667747
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage(b'{"key1": "value1"}')
    stream = BufferedPrettyStream(msg, True, True)
    assert list(stream.iter_body()) == [b'{ "key1" : "value1" }']

# Generated at 2022-06-13 22:13:17.545591
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers={'Content-Type': 'application/json'})
    stream = PrettyStream(msg=msg, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    # Get the headers
    headers = stream.get_headers()
    # Convert headers to string
    headers_str = headers.decode('utf8')

    # Create the expected headers string
    headers_str_expected = 'Content-Type: application/json\n'

    assert headers_str == headers_str_expected


# Generated at 2022-06-13 22:13:23.714118
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.streams import RawStream
    # execute raw stream
    request = HTTPRequest('GET / HTTP/1.1\r\nHost: www.example.com\r\nAccept: */*\r\n\r\n')
    stream = RawStream(request, with_headers=False, with_body=True)
    assert [chunk.decode('utf8') for chunk in stream] == []
    # execute raw stream
    response = HTTPResponse(
        'HTTP/1.1 200 OK\r\nContent-Length: 0\r\nDate: Thu, 1 Jan 1970 00:00:01 GMT\r\n\r\n'
    )

# Generated at 2022-06-13 22:13:26.412858
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import Response

    r = Response(headers=list(b'login:pass'), body=b'', encoding=None)
    stream = RawStream(r)
    assert bytes.join(b'', stream) == \
                       b'login:pass\r\n'

    stream.with_headers = False
    assert bytes.join(b'', stream) == \
                       b''

    stream.with_body = False
    assert bytes.join(b'', stream) == \
                       b''


# Generated at 2022-06-13 22:13:38.699251
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import HTTPRequest
    from httpie.core import main

    rq = HTTPRequest('GET', 'http://httpbin.org/get',
                     headers={'content-type': 'text/plain'},
                     data='hello\nworld\n')

    color_settings = main.DEFAULT_FORMAT_OPTIONS['colors']
    with patch.object(sys, 'stdout', io.StringIO()) as mocked_stdout:
        PrettyStream(rq, Environment(), color_settings,
                     with_headers=False, with_body=True).iter_body()
    assert mocked_stdout.getvalue() == '''hello
world
'''


# Generated at 2022-06-13 22:14:09.957787
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    req = Request(url='http://httpbin.org/get')
    req.headers['User-Agent'] = 'HTTPie Testing'
    req.headers['Accept-Encoding'] = 'identity'
    req.headers['Content-Type'] = 'application/json'
    req.body = json.dumps({'testing': 'ok'})
    content_type = req.headers.get('Content-Type')
    content_type, body = req.body.converter.convert(body=req.body, content_type=content_type)
    res = BufferedPrettyStream(env=Environment(), msg=req, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    assert isinstance(res, BufferedPrettyStream)
    assert res.msg == req

# Generated at 2022-06-13 22:14:20.352253
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    env=Environment()
    env.stdout_isatty=False
    env.stdout_encoding='utf8'
    msg=HTTPMessage()
    msg.headers='Content-Type: text/plain; charset=iso-8859-1'
    msg.encoding='iso-8859-1'
    msg_stream=EncodedStream(msg=msg,env=env)
    with pytest.raises(NotImplementedError):
        msg_stream.iter_body()

# Generated at 2022-06-13 22:14:28.546139
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    #test case
    def transfer(self, chunk):
        return str(self) + str(chunk)

    self = BufferedPrettyStream(transferer=transfer)

    test_body = ['a', 'b', 'c']
    result = [self.iter_body(chunk) for chunk in test_body]
    expected_result = ['<__main__.BufferedPrettyStream object at 0x7f25c6864dd8>a',
                       '<__main__.BufferedPrettyStream object at 0x7f25c6864dd8>ab',
                       '<__main__.BufferedPrettyStream object at 0x7f25c6864dd8>abc']
    assert result == expected_result

# Generated at 2022-06-13 22:14:34.061814
# Unit test for constructor of class RawStream
def test_RawStream():
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
    raw_stream = RawStream(HTTPMessage(b'abc'), False, True, None)
    assert raw_stream is not None
   

# Generated at 2022-06-13 22:14:38.659422
# Unit test for constructor of class RawStream
def test_RawStream():
    result = RawStream('s')
    assert result.msg == 's'
    assert result.with_headers == True
    assert result.with_body == True
    assert result.on_body_chunk_downloaded == None
    assert result.chunk_size == 104857600


# Generated at 2022-06-13 22:14:51.776313
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.context import Environment
    from httpie.compat import is_windows

    from httpie.output.streams import BufferedPrettyStream

    env = Environment(stdout_isatty=False,
                              format='pretty',
                              colors=0,
                              default_options=True,
                              stdin=None,
                              stdin_isatty=False,
                              stdout=None,
                              stdout_isatty=False,
                              stdout_raw=False,
                              style='solarized')

    msg = HTTPResponse(headers=dict(Content_Type='text/html'),
                        encoding='utf8',
                        status_line='200 OK')

    # There is no body (has not been downloaded)

# Generated at 2022-06-13 22:14:59.425657
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import pytest
    from httpie.models import HTTPResponse
    host = 'https://httpbin.org'
    url = host + '/robots.txt'
    resp = HTTPResponse('GET', url, status_code=200, headers={}, body=b'''
User-agent: *
Disallow: /deny
''')
    # resp = httpx.get(url)
    # print(resp.text)
    def _test_BaseStream():
        try:
            for i in BaseStream(resp):
                print(i.decode('utf-8'))
        except Exception as e:
            raise e
    _test_BaseStream()



# Generated at 2022-06-13 22:15:08.195929
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    msg = HTTPMessage()
    msg.headers = '''\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

'''
    msg.content = '''\
<!DOCTYPE html>
<html>
<head>
<title>Some Title</title>
</head>
<body>
Some content.
</body>
</html>
'''
    stream = PrettyStream(msg, 'utf8', None)
    assert stream.process_body(msg.content) == msg.content.encode('utf8')

# Generated at 2022-06-13 22:15:16.414116
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # This is the body of the stream 
    ls = ["[\n", '{"name":"John Midas","age":21}', "\n", '{"name":"George","age":23}', "\n", '{"name":"Elsa","age":22}', "\n", '{"name":"Nora","age":20}', "\n", '{"name":"Kamal","age":18}', "\n", '{"name":"Syd","age":19}', "\n", '{"name":"Betty","age":23}', "\n", "]\n"]

    # This is the array where we should store each chunk for the iter_body()
    ls_to_test = []

    # We create the stream

# Generated at 2022-06-13 22:15:27.579360
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = [
        ('Host', 'httpbin.org'),
        ('User-Agent', 'HTTPie/0.9.9'),
        ('Accept-Encoding', 'gzip, deflate, compress'),
        ('Accept', '*/*'),
        ('Connection', 'keep-alive')
    ]
    headers = CaseInsensitiveDict(headers)

    headers_expect = '\nHost: httpbin.org\nUser-Agent: HTTPie/0.9.9\nAccept-Encoding: gzip, deflate, compress\nAccept: */*\nConnection: keep-alive\n\n'

    stream = PrettyStream(None, None, None, True, True)
    stream.msg.headers = headers
    headers_test = stream.get_headers()

    assert headers_test == headers_expect

# Generated at 2022-06-13 22:16:14.224414
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import HTTPResponse
    from httpie.output.streams import RawStream

    test_message = 'This is a test message'
    test_headers = {'test_header': 'This is a test header'}


# Generated at 2022-06-13 22:16:15.182007
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    pass


# Generated at 2022-06-13 22:16:32.730042
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage()
    msg.headers = 'Content-Type: text/plain; encoding=utf-8'
    msg.body = "abc\n".encode("utf-8") + b"\0" + "def\n".encode("utf-8")
    msg.encoding = 'utf-8'
    output_encoding = "utf-8"

    # This will raise BinarySuppressedError
    try:
        for line in EncodedStream(msg).iter_body():
            print("This will not execute")
    except BinarySuppressedError:
        pass

    # If no binary data, it's output by line
    msg = HTTPMessage()
    msg.headers = 'Content-Type: text/plain; encoding=utf-8'

# Generated at 2022-06-13 22:16:41.071175
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    stream = BufferedPrettyStream(
        msg=HTTPMessage(),
        with_headers=True,
        with_body=True
    )
    stream.msg.encoding = ''
    stream.msg.iter_body = lambda x: []
    stream.process_body = lambda x: x
    stream.conversion.get_converter = lambda x: None
    stream.output_encoding = ''
    stream.formatting.format_body = lambda c, m: c
    assert list(stream.iter_body()) == []
    stream.msg.iter_body = lambda x: [b'binary body']
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
    stream.msg.iter_body = lambda x: [b'body\nwith\nnewlines']
   

# Generated at 2022-06-13 22:16:46.051774
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    """Test constructor of EncodedStream
    """
    from httpie.models import Response
    mock_response = Response()
    msg = EncodedStream(mock_response,with_headers=True,with_body=True)
    assert msg.msg == mock_response
    assert msg.with_headers == True
    assert msg.with_body == True


# Generated at 2022-06-13 22:16:57.381489
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie import input
    from httpie.input import SEP_CREDENTIALS
    from httpie.context import Environment
    from httpie.models import HTTPResponse
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.compat import is_windows
    from httpie.output.formatters.colors import get_lexer
    import os

    env = Environment()
    # env.stdout_isatty = False
    env.stdout = sys.stdout
    env.output_options = input.ParseResult(
        args=['.'],
        json=True,
        pretty=True,
        print_body=True,
        colors=256,
        style='paraiso-dark',
    )
   

# Generated at 2022-06-13 22:17:07.696283
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import MockRequest
    env = Environment()
    conv = Conversion()
    format = Formatting()
    mime = 'text/html'
    line = '<!DOCTYPE html>'
    msg = MockRequest(headers='', content_type=mime, method='GET', url='http://localhost', body=line)
    stream = PrettyStream(msg, conversion=conv, formatting=format, env=env)
    assert '<!DOCTYPE html>' == str(stream.process_body(line))

# Generated at 2022-06-13 22:17:09.781847
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    prettyStream = PrettyStream(None, None, None, None, None)
    assert prettyStream is not None



# Generated at 2022-06-13 22:17:18.261790
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    data = 'This is a plain-text message.\r\n'
    expected = [b'This is a plain-text message.\r\n']

    class FakeResponse(object):
        encoding = 'utf-8'
        def iter_body(self, chunk_size=1):
            yield data.encode('utf-8'), b'\r\n'

    env = Environment()
    stream = EncodedStream(msg=FakeResponse(), env=env, with_headers=False, with_body=True)
    assert list(stream.iter_body()) == expected

# Generated at 2022-06-13 22:17:25.472853
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(
        msg=HTTPMessage(
            method='GET',
            url='http://httpbin.org/get',
            headers={'content-type': 'application/json'},
        ),
        conversion=Conversion(),
        formatting=Formatting(),
        )

    test_chunk = 'test1\ntest2\ntest3\ntest4'
    assert stream.process_body(test_chunk) == b'test1\ntest2\ntest3\ntest4'

# Generated at 2022-06-13 22:18:17.231541
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.output import processing
    import httpie.output.streams
    import json

    # Verify we can format JSON body without error
    # Use a raw message so we don't have to parse
    # JSON body as part of the test (stream.py)
    headers = "Content-Type: application/json"
    body = json.dumps({'state': 'ok'})
    msg = httpie.models.RawRequestMessage(headers=headers, body=body)

    # Initialize with defaults
    formatting = processing.Formatting()
    conversion = processing.Conversion(None)
    stream = httpie.output.streams.PrettyStream(msg, formatting, conversion)

    # Verify we get a list back of the formatted body
    lines = list(stream.iter_body())
    assert lines[0] == msg.body

    #

# Generated at 2022-06-13 22:18:23.696600
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    from httpie.output.streams import EncodedStream

    msg = HTTPMessage()
    msg.headers = 'headers'
    msg.body = 'body'
    msg.chunked = False
    
    with Environment(stdout_isatty=True, stdout_encoding='encoding') as env:
        encoded_stream = EncodedStream(msg=msg, env=env)

    list1 = list(encoded_stream)
    assert list1 == [b'headers\r\n\r\nbody']


# Generated at 2022-06-13 22:18:27.056978
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    assert list(BaseStream(HTTPMessage(b'abc')).__iter__())==[b'abc']

# Generated at 2022-06-13 22:18:37.745181
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    """Test BaseStream __iter__."""
    env = Environment(stdout_isatty=True)
    # Test with_headers and with_body
    raw_stream = RawStream(
        msg=HTTPMessage(
            headers='test:123',
            body=b'\0\0\0\0\0',
            content_type='binary/octet-stream'
        ),
        env=env,
        with_headers=True,
        with_body=True
    )

    assert raw_stream
    assert not raw_stream.with_body and not raw_stream.with_headers
    for _ in raw_stream:
        pass

    # Test with_headers and without body

# Generated at 2022-06-13 22:18:47.288044
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    class HttpMsg():

        def iter_lines(self, _):
            yield (b'{ "name": "Alice", "age": 5 }', b'\n')

        @property
        def content_type(self):
            return "application/json"

        @property
        def encoding(self):
            return "utf-8"

    input_msg = HttpMsg()
    pretty_stream = PrettyStream(
        input_msg, with_headers=False, with_body=True)
    assert b'\n{ "name": "Alice", "age": 5 }' == next(pretty_stream.iter_body)



# Generated at 2022-06-13 22:18:57.544674
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    headers = b'HTTP/1.1 200 OK\r\n'\
              b'content-type: application/json\r\n\r\n'
    chunk_size = 2048
    rawstream = RawStream(msg=HTTPMessage(headers, b'a' * 2048),
                          chunk_size=chunk_size)
    try:
        num_chunks = 0
        for chunk in rawstream.iter_body():
            num_chunks += 1
            assert len(chunk) == chunk_size
    except DataSuppressedError as e:
        print(e)
    # 1 chunks returned
    assert num_chunks == 1



# Generated at 2022-06-13 22:19:05.837387
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import HTTPRequest
    req = HTTPRequest("http://127.0.0.1:8080/cgi-bin/ab?ab=c%20de")
    req._body = b'1234\n2345\n3456\n'

    for chunk in PrettyStream(msg=req, with_headers=False, with_body=False).iter_body():
        print(chunk)
    print()

    req._body = b'1234\n2345\n3456\n'
    for chunk in PrettyStream(msg=req, with_headers=False, with_body=True).iter_body():
        print(chunk)
    print()

    req._body = b'1234\r2345\r3456\r'

# Generated at 2022-06-13 22:19:14.662656
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    binary_data = b'abc\0def\0ghi'
    head, data, tail = binary_data[:3], binary_data[3:6], binary_data[6:]
    msg = HTTPMessage(headers=b'', body=binary_data)
    stream = PrettyStream(msg=msg, conversion=Conversion(), formatting=Formatting())
    it = stream.iter_body()
    assert next(it) == head
    assert next(it) == data
    assert next(it) == tail
    assert next(it, False) == False

# Generated at 2022-06-13 22:19:26.550705
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    fmt = "{\"type\": \"message\"," \
          " \"timestamp\": \"2020-07-20T14:20:59.942Z\", \"message\": \"Started\"}"
    fmt = fmt.encode('utf-8')
    fmt += b'\r\n'

    _msg = HTTPMessage()
    _msg.headers['Content-Type'] = 'application/json'
    _msg.encoding = 'utf-8'

    _bytes = []
    for c in fmt:
        _bytes.append(c)

    def _iter(bytes):
        for c in bytes:
            yield c
        yield b'\r\n'

    _msg.iter_body = lambda chunk=1: _iter(_bytes)


# Generated at 2022-06-13 22:19:29.214982
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """Test if unit of BufferedPrettyStream is functioning."""
    result = BufferedPrettyStream(None, None).iter_body()
    assert result is not None

# Generated at 2022-06-13 22:20:05.473374
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import Headers
    from httpie.output.formatters import RawFormatter
    from httpie.output.processing import Conversion
    from httpie.output.streams import PrettyStream
    p = PrettyStream(RawFormatter(), Conversion(), msg=HTTPMessage(headers=Headers([('content-type', 'application/json; charset=utf-8'),('Content-Length', '0')])))
    assert p.get_headers() == b'\x1b[1mcontent-type:\x1b[0m application/json; charset=utf-8\r\n\x1b[1mContent-Length:\x1b[0m 0\r\n'

# Generated at 2022-06-13 22:20:13.200984
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print('raw = RawStream(msg, with_headers=True, with_body=True)')
    print('encd = EncodedStream(env=Environment(), msg, with_headers=True, with_body=True)')
    print('buffd = BufferedPrettyStream(msg, with_headers=True, with_body=True)')
    print('buffd = PrettyStream(msg, with_headers=True, with_body=True)')

if __name__ == '__main__':
    test_EncodedStream()

# Generated at 2022-06-13 22:20:17.933938
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    h = {'abc': 'def','ghi': 'jkl'}
    headers = HTTPMessage(headers = h)
    c = Conversion()
    f = Formatting()
    m = BufferedPrettyStream(headers, conversion = c, formatting = f)


# Generated at 2022-06-13 22:20:29.308765
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    if __name__ == '__main__':
        from pprint import pprint
        from unittest import TestCase
        import unittest
        from httpie.output.streams import PrettyStream
        from httpie.context import Environment
        from httpie.models import HTTPResponse, JSONDict
        from httpie.compat import str
        from json import loads

        class MockEnvironment(Environment):
            stdout_isatty = False

        class PrettyStreamTest(TestCase):

            def test_get_headers(self):
                args = {'pretty_options': {'colors': False}, 'stream': False}
                env = MockEnvironment(args=args, stdout=None)

# Generated at 2022-06-13 22:20:40.443805
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # This test is added by Mengting Wan
    msg = HTTPMessage()

# Generated at 2022-06-13 22:20:48.313109
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    msg = HTTPMessage()
    msg.encoding = 'utf8'
    msg.headers = ''
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf8'
    conversion = Conversion()
    formatting = Formatting()
    stream = BufferedPrettyStream(msg, with_headers=True, with_body=True, conversion=conversion, env=env, formatting=formatting)
    assert type(stream) == BufferedPrettyStream

# Generated at 2022-06-13 22:20:51.028197
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print('Testing constructor of class EncodedStream')
    import httpie.output
    msgTest = httpie.models.HTTPMessage()
    msgTest.encoding = 'utf8'
    test1 = EncodedStream(msg=msgTest, with_headers=True, with_body=True)
    assert test1.msg == msgTest
    assert test1.with_headers
    assert test1.with_body


# Generated at 2022-06-13 22:20:58.153752
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # Test for initialization of PrettyStream
    # Body of request object is empty
    r_headers = dict()
    r_method = 'GET'
    r_body = ''
    r_url = 'https://httpbin.org/get?course=networking&assignment=1'
    response = HTTPMessage.from_objects(r_headers, r_body, r_method, r_url)
    # Convert response object to stream
    r_stream = BufferedPrettyStream(response, True, True, None)
    assert r_stream.msg.__class__.__name__ == 'HTTPMessage'



# Generated at 2022-06-13 22:21:05.299219
# Unit test for constructor of class RawStream
def test_RawStream():
    """
    This test is for the constructor of RawStream.
    """
    msg = HTTPMessage()
    msg.raw = b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
    rs = RawStream(msg)
    assert isinstance(rs, RawStream), 'Should be RawStream instance'



# Generated at 2022-06-13 22:21:14.192542
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    s = b'abcd\r\nefgh\r\n'
    msg = HTTPMessage(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n', s, encoding='utf8')
    stream = EncodedStream(msg)
    it = iter(stream)
    assert next(it) == b'abcd\r\n'
    assert next(it) == b'efgh\r\n'