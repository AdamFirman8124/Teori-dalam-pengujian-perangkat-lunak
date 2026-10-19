

# Generated at 2022-06-13 22:12:25.217578
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    print(BufferedPrettyStream(conversion = "", formatting = "", msg = "",
                               with_headers = True, with_body = True,
                               on_body_chunk_downloaded = ""))

# Generated at 2022-06-13 22:12:34.855763
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    test_data = [
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
        ["HTTP/1.1 200 OK\r\n\r\nabc\n", "abc\n"],
    ]


# Generated at 2022-06-13 22:12:38.904945
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    bps = BufferedPrettyStream(conversion=Conversion(), formatting=Formatting())
    # Check that BufferedPrettyStream is a subclass of BaseStream
    assert issubclass(BufferedPrettyStream, BaseStream)


# Generated at 2022-06-13 22:12:49.274204
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # test_iter_body_convert_from_text_to_json
    class MockFormatting():
        def format_headers(self, headers):
            pass

        def format_body(self, content, mime):
            pass
    class TextToJsonConverter():
        def convert(self, body):
            pass
    class MockConversion():
        def get_converter(self, mime):
            return TextToJsonConverter()
    class MockHTTPMessage():
        encoding = 'utf8'
        content_type = 'text/html; charset=utf8'
        def iter_lines(self, chunk_size):
            return [('line\n'.encode('utf8'),b'\n'),('line\n'.encode('utf8'),b'\n')]

# Generated at 2022-06-13 22:13:03.746084
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import pytest
    from httpie.models import Response
    from httpie.output.streams import BinarySuppressedError, BufferedPrettyStream, EncodedStream, RawStream

    env = Environment(colors=256)
    msg = Response(headers=[('Content-Type', 'text/plain')], encoding='utf-8', body='ё')

# Generated at 2022-06-13 22:13:07.013807
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class HTTPMessageMock(object):
        def iter_body(self, chunk_size):
            return [(b'Message', b'\n')]
    h = HTTPMessageMock()
    bps = BufferedPrettyStream(env=Environment(), msg=h)

    for chunk in bps.iter_body():
        assert chunk == b'Message\n'

    print('Test for method iter_body of class BufferedPrettyStream is passed')


# Generated at 2022-06-13 22:13:12.508853
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    data_msg = HTTPMessage()
    data_stream = PrettyStream.get_headers()
    # Проверка совпадения обоих ответов
    assert data_stream == data_msg.headers.encode('utf8')

# Generated at 2022-06-13 22:13:25.028516
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    b = bytearray()
    b.extend(b"abc")
    # insert 0x00 after 'b'
    b.insert(1,b'\x00')
    b.extend(b"def")

    # suppress this
    stream = EncodedStream(msg=HTTPMessage(body=b), with_headers=False, with_body=True)
    assert b'\0' in b
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

    # test the iterator works
    stream = EncodedStream(msg=HTTPMessage(body=b.replace(b"\x00", b"")), with_headers=False, with_body=True)
    a = list(stream.iter_body())

# Generated at 2022-06-13 22:13:33.695703
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(b'GET / HTTP/1.1\r\n'
                      b'Content-Type: text/plain\r\n'
                      b'\r\n')
    stream = PrettyStream(msg, True, True, '', '', '', '', '', '', '')
    assert stream.get_headers() == b'GET / HTTP/1.1\n' \
                                   b'Content-Type: text/plain\n' \
                                   b'\n'



# Generated at 2022-06-13 22:13:40.739263
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    msg = HTTPMessage(
        url='https://127.0.0.1/test?page=2',
        method='GET',
        headers={
            'Set-Cookie': 'foo=bar;'
        },
        body='test'
    )
    obj = BufferedPrettyStream(msg, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    assert obj.msg == msg
    assert obj.with_headers == True
    assert obj.with_body == True
    assert obj.on_body_chunk_downloaded == None


# Generated at 2022-06-13 22:14:09.849554
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.context import Environment
    from httpie.models import HTTPResponse
    from httpie.output.processing import Conversion, Formatting

    msg = HTTPResponse(headers={
        'Content-Type': 'text/whatever; charset=utf8'
    })

    env = Environment()
    conversion = Conversion()
    formatting = Formatting()

    def get_body(chunk):
        stream = BufferedPrettyStream(
            msg=msg,
            conversion=conversion,
            formatting=formatting,
            env=env,
            chunk_size=1
        )
        stream.msg.body = chunk

        return b''.join(stream.iter_body())

    # Use the `iter_body` method which uses `process_body`

# Generated at 2022-06-13 22:14:14.148719
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(b'test')
    buf = RawStream(msg)
    assert list(buf.iter_body()) == [b'test']


# Generated at 2022-06-13 22:14:20.357045
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage()
    msg.set_body(b'0123456789', 'raw')
    stream = RawStream(msg, with_body=True)
    assert list(stream.iter_body()) == [b'01234', b'56789']



# Generated at 2022-06-13 22:14:23.577395
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # Test: without conversion and formatting
    env = Environment()
    msg = HTTPMessage()
    stream = PrettyStream(env, msg)

    # Test: with conversion and formatting
    conversion = Conversion()
    formatting = Formatting()
    env = Environment()
    msg = HTTPMessage()
    stream = PrettyStream(env, msg, conversion, formatting)

# Generated at 2022-06-13 22:14:35.366045
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # when message encoding is not set (defaults to utf8)
    msg = HTTPMessage()
    es = EncodedStream(msg)
    assert es.output_encoding == 'utf8'

    # when stdout is not a tty
    msg = HTTPMessage(encoding='cp437')
    es = EncodedStream(msg, env=Environment(stdout_isatty=False))
    assert es.output_encoding == 'cp437'

    # when stdout is a tty
    msg = HTTPMessage(encoding='cp437')
    es = EncodedStream(msg, env=Environment(stdout_isatty=True, stdout_encoding='utf8'))
    assert es.output_encoding == 'utf8'

    # when stdout is a tty and stdout_enc

# Generated at 2022-06-13 22:14:37.321598
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    assert isinstance(EncodedStream(), HTTPMessage)
    

# Generated at 2022-06-13 22:14:46.047884
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    # 测试httpie.output.streams.RawStream.iter_body函数
    # 初始化 RawStream 对象
    raw_stream = RawStream(HTTPMessage())
    # 判断调用 iter_body 方法，返回的是一个迭代器
    assert isinstance(raw_stream.iter_body(), Iterator)

# Generated at 2022-06-13 22:14:56.765434
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    h = HTTPMessage()
    h.encoding = "utf-8"
    h.headers = '''HTTP/1.1 200 OK\nDate: Tue, 28 Feb 2017 18:37:35 GMT\nContent-Type: text/html; charset=utf-8\nContent-Length: 18\nConnection: keep-alive\nServer: nginx/1.10.1\nX-Powered-By: PHP/5.6.30\n'''
    h.body = '''{"name":"ni","age":11}'''
    p = PrettyStream(h)
    assert next(p.iter_body()) == '{"name":"ni","age":11}\n'

# Generated at 2022-06-13 22:15:09.054080
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage()
    msg.encoding = "utf8"
    msg.content_type = "text/plain;charset=utf8"
    msg.headers = "Content-Type:text/plain"
    msg.body = "1".encode("utf8") * 1000 + b'\0' * 10
    env = Environment()
    env.stdout_isatty = False
    env.stdout_encoding = "utf8"
    formatting = Formatting()
    conv = Conversion()
    stream = PrettyStream(conversion=conv, formatting=formatting, msg=msg, env=env)
    stream.process_body = lambda x: x.decode(msg.encoding)
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

# Generated at 2022-06-13 22:15:16.727509
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie import ExitStatus
    from httpie.client import HTTPError
    from httpie.compat import OrderedDict
    from httpie.output import write_output
    import json
    import pytest

# Generated at 2022-06-13 22:15:46.910682
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.output.streams import PrettyStream

    http_message = {'headers': {
        'Content-Type': 'text/javascript',
        'Content-Encoding': 'utf8'},
        'body': '{"results": [{"name": "a", "value": 1.1}, {"name": "b", "value": 2.2}]}'}
    pretty_stream = PrettyStream(msg=http_message)
    assert(pretty_stream.process_body(http_message['body'])
           == b'{\n    "results": [\n        {\n            "name": "a", \n            "value": 1.1\n        }, \n        {\n            "name": "b", \n            "value": 2.2\n        }\n    ]\n}\n')

# Generated at 2022-06-13 22:15:51.061837
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    f = BufferedPrettyStream(msg=None, conversion=None, formatting=None)
    assert f.msg == None
    assert f.conversion == None
    assert f.formatting == None
    assert f.mime == None

# Generated at 2022-06-13 22:15:54.512101
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    stream = EncodedStream('')
    lines = list(stream.iter_body())
    print(lines)

if __name__ == '__main__':
    test_EncodedStream_iter_body()

# Generated at 2022-06-13 22:16:06.081526
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import HTTPRequest

    def _get_headers_bool(instance: BaseStream, attr_name: str) -> bool:
        vars_local = vars(instance)
        res = vars_local.get(attr_name)
        return res

    request_1 = HTTPRequest(
        method="GET",
        url="https://httpbin.org/get",
        headers={"X-Header": "1"},
        data=b"data data data"
    )

    request_2 = HTTPRequest(
        method="GET",
        url="https://httpbin.org/get",
        headers={"X-Header": "2"},
        data=b"data data data"
    )

    raw_stream = RawStream(msg=request_1, with_headers=True, with_body=True)


# Generated at 2022-06-13 22:16:16.230199
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Added as part of testing https://github.com/jakubroztocil/httpie/issues/773
    msg = HTTPMessage(
        (
            'HTTP/1.0', 200, 'OK\n'
            'Content-Type: application/json\n'
            '\n'
            '{"value": "my text"}'
        )
    )
    converted_msg = HTTPMessage(
        (
            'HTTP/1.0', 200, 'OK\n'
            'Content-Type: application/json\n'
            '\n'
            '{"value": "my text"}'
        )
    )
    conversion = Conversion()
    formatting = Formatting()
    stream = PrettyStream(msg, conversion, formatting)

# Generated at 2022-06-13 22:16:31.700691
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    json_data = {
        'id': 1,
        'name': 'Foo'
    }
    json_encoded = json.dumps(json_data).encode('utf-8')
    response = HTTPMessage(
        None,
        json_encoded,
        content_type='application/json',
        encoding='utf-8'
    )

    stream = EncodedStream(response, with_body=True, with_headers=False)

    assert response.encoding == 'utf-8'
    assert stream.output_encoding == 'utf-8'
    assert json_encoded in stream.iter_body()

# Generated at 2022-06-13 22:16:35.543711
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    b = BaseStream(1)
    assert next(b) == b.get_headers() + b'\r\n\r\n'
    assert next(b) == b''
    assert next(b) == b''


# Generated at 2022-06-13 22:16:50.934479
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    """Test function iter_body of class PrettyStream"""
    # Run this test by running the following command in the terminal
    # (from the top folder of the project)
    # python -m httpie.output.streams test_PrettyStream_iter_body
    import sys
    import re
    import json
    import pygments
    from httpie.utils import JSON_TYPES
    from httpie.output import streams
    from httpie.output.formatters import JSONFormatter

    def _pretty_print(body):
        if isinstance(body, JSON_TYPES):
            return json.dumps(
                body,
                ensure_ascii=False,
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            )
        else:
            return body


# Generated at 2022-06-13 22:17:04.777153
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    print("\n---====--- Testing method process_body of class PrettyStream ---====---")
    # Testing input
    chunk = "<title>HTTPie | CLI HTTP client</title>\r\n"
    mime = "text/html"

    # Stream to be used in test
    pretty_stream = PrettyStream(
        None,
        None
    )

    pretty_stream.mime = mime

    pretty_stream.output_encoding = "utf8"

    pretty_stream.formatting = Formatting(
        format_options={},
        color_options={},
    )

    # Testing
    print("Testing PrettyStream.process_body() with chunk: ", chunk, " and mime: ", mime)
    print("Expected: ", chunk)
    result = pretty_stream.process_body(chunk)
    expected

# Generated at 2022-06-13 22:17:16.304331
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.input import ParseError
    from httpie.models import Response
    from httpie.compat import is_py26
    import time
    import datetime

    #test input data
    response = Response('HTTP/1.0 200 OK\r\n'
                        'Date: ' + time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime()) + ' GMT\r\n'
                        'Content-Type: application/json; charset=UTF-8\r\n'
                        'Content-Length: 17\r\n'
                        'Server: BaseHTTP/0.3 Python/2.7.10\r\n'
                        '\r\n'
                        '{"message": "bye"}'
                        )

    #test class
    stream = EncodedStream

# Generated at 2022-06-13 22:18:05.772189
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Case 1: When it is not the first chunk, and if it is of binary type
    msg = HTTPMessage()
    msg.encoding = 'utf8'
    msg.content_type = 'application/json'
    msg.body = "aa\0"
    c = Conversion()
    f = Formatting()
    p = PrettyStream(msg, with_headers=False, with_body=True, conversion=c, formatting=f)
    p.CHUNK_SIZE = 1
    try:
        for line in p.iter_body():
            pass
        assert False  # Fail if it does not raise BinarySuppressedError
    except BinarySuppressedError:
        pass
    # Case 2: When it is the first chunk, and if it is of binary type
    msg = HTTPMessage()

# Generated at 2022-06-13 22:18:11.848664
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    import io
    from httpie.models import Response
    from httpie.context import Environment

    stream = EncodedStream(
        msg = Response.parse(
            'HTTP/1.1 200 OK\r\n'
            'Connection: keep-alive\r\n'
            'Set-Cookie: foo=bar\r\n'
            '\r\n'
            'ok'
        )
    )

    # Default to utf8 when unsure.
    assert stream.output_encoding == 'utf8'
    # stream the body
    assert b''.join(stream.iter_body()) == b'ok'


# Generated at 2022-06-13 22:18:19.320664
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    #mimetype = 'application/x-www-form-urlencoded';
    mimetype = 'application/json';
    #mimetype = 'text/plain';
    #mimetype = 'text/html';
    headers = 'HTTP/1.1 200 OK\r\nContent-Length: 214\r\nContent-Type: ' + mimetype + ';charset=utf-8\r\n\r\n'

    # http://wiki.lazyscripts.org/index.php?title=Tiger_vnc_session
    #body = 'mode=viewonly&password=&user=guest&wait=&autoscale=0&rdp=no&geometry=&fullscreen=0&autopopup=0&listen=&viewmode=2&http=no

# Generated at 2022-06-13 22:18:26.048636
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.models import HTTPMessage
    from httpie.output.processing import Conversion, Formatting

    env = Environment()
    msg = HTTPMessage(
        body=(b'peanuts\r\n'),
        headers={
            'Content-Type': 'text/plain; charset=UTF-8',
            'Content-Length': '9'
        },
        encoding='UTF-8'
    )
    conversion = Conversion()
    formatting = Formatting()
    pretty_stream = PrettyStream(msg, conversion=conversion, formatting=formatting,
                                 with_headers=True, with_body=True,
                                 on_body_chunk_downloaded=None)
    assert pretty_stream.CHUNK_SIZE == 1
    assert pretty_stream.msg == msg

# Generated at 2022-06-13 22:18:37.157484
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    messages = []
    messages.append(HTTPMessage(
        headers=b'HTTP/1.1 200 OK\r\n'
                b'Content-Type: text/html\r\n'
                b'Content-Length: 13\r\n'
                b'\r\n'
                b'Hello World!',
        encoding='utf8',
    ))
    messages.append(HTTPMessage(
        headers=b'HTTP/1.1 200 OK\r\n'
                b'Content-Type: text/html; charset=utf-8\r\n'
                b'Content-Length: 13\r\n'
                b'\r\n'
                b'Hello World!',
    ))

# Generated at 2022-06-13 22:18:46.761290
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Unit test for function iter_body of class PrettyStream
    stream = PrettyStream(
        HTTPMessage(headers='key: value'),
        Conversion(),
        Formatting(),
        with_headers=False
    )

    body = {
        # Example of a text
        "text": b'hello world\r\n'
    }

    result = {
        # Expected result of the text
        "text": b'hello world\r\n'
    }

    # iterate the input body
    for key in body:
        # encode the body and compare it with the expected result
        assert result[key] == b''.join(stream.iter_body())

# Generated at 2022-06-13 22:18:54.776644
# Unit test for constructor of class RawStream
def test_RawStream():
    # Case 1: value chunk_size is None -> error
    try:
        rawStream = RawStream(chunk_size=None)
        print('Error: No body')
    except Exception:
        print('No body')

    # Case 2: value chunk_size not None -> success
    msg = HTTPMessage(b'Raw Stream')
    rawStream = RawStream(msg=msg, chunk_size=1024)
    for chunk in rawStream.iter_body():
        print(chunk)



# Generated at 2022-06-13 22:19:05.302824
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    test_data = {
        'json': {
            "body": b'"data"',
            "mime": "application/json",
            "expected": '"data"\n'
        },
        'html': {
            "body": b'<div class="test">data</div>',
            "mime": "text/html",
            "expected": '<div class="test">data</div>\n'
        },
        'xml': {
            "body": b'<test attr="data">content</test>',
            "mime": 'application/xml',
            "expected": '<test attr="data">content</test>\n'
        },
    }
    for type, values in test_data.items():
        body = values['body'].decode('utf8', 'replace')


# Generated at 2022-06-13 22:19:12.860953
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    def test_iter_body(self):
        """Test iter_body"""
        # Test iter_body
        message = HTTPMessage(iter_body=iter(b'test\n'),
                       encoding='ascii')
        stream = RawStream(message, chunk_size=2)
        for data in stream.iter_body():
            assert isinstance(data, bytes)
        assert isinstance(data, bytes)



# Generated at 2022-06-13 22:19:13.631242
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    assert body == b'hello world'

# Generated at 2022-06-13 22:20:37.645969
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage()
    msg.body = b'123456789'
    http = RawStream(msg)
    it = http.iter_body()
    assert next(it) == b'123456789'
    try:
        next(it)
        assert False
    except StopIteration:
        assert True


# Generated at 2022-06-13 22:20:47.599201
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    assert PrettyStream(
        msg=HTTPMessage(
            'HTTP/1.1 201 Created\r\n\r\n',
            headers={'status': 'HTTP/1.1 201 Created'},
            encoding='utf8'
        ),
        with_headers=True,
        with_body=False,
        on_body_chunk_downloaded=None
    ).msg == HTTPMessage(
        'HTTP/1.1 201 Created\r\n\r\n',
        headers={'status': 'HTTP/1.1 201 Created'},
        encoding='utf8'
    )

# Generated at 2022-06-13 22:20:52.798481
# Unit test for constructor of class RawStream
def test_RawStream():
    import sys
    import httpie
    http_msg = httpie.input.HTTPRequest()
    if sys.version_info >= (3, 6):
        assert isinstance(RawStream(msg=http_msg), RawStream)
    else:
        assert isinstance(RawStream(), RawStream)

# Generated at 2022-06-13 22:21:02.046000
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    conversion = Conversion()
    formatting = Formatting()
    test_data = [b'\xef\xbb\xbf<!DOCTYPE html', b'<html>\n<head>\n<title>', b'title</title>\n<body>\n<h', b'1>Hello world</h1>\n</body></html>']
    test_bytes = b'\xef\xbb\xbf<!DOCTYPE html<html>\n<head>\n<title>title</title>\n<body>\n<h1>Hello world</h1>\n</body></html>'

# Generated at 2022-06-13 22:21:15.241957
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import httpie.output.streams as streams
    import httpie.output.formatters.colors as colors
    import httpie.compat
    import httpie.context
    from httpie.models import ContentTypeJsonIsh, HTTPResponse

    httpie.compat.is_py26 = True

    mime = ContentTypeJsonIsh('application/json')
    streaming = True
    headers = [('Content-Type', 'application/json'), ('foo', 'bar'), ('baz', 'buz')]
    body = '{ "a": 1 }'
    encoding = 'utf8'
    status = '200'
    status_line = 'HTTP/1.1 200 OK'
    request_url = 'http://foo.bar'
    env = httpie.context.Environment()

    msg = HTTPR

# Generated at 2022-06-13 22:21:22.582692
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    print("\n\nUnit test for method get_headers of class PrettyStream")
    msg = HTTPMessage()
    msg.headers = "Pair: Value\r\nPair: Value 2\r\n\r\n"
    msg.encoding = "utf8"
    pretty_stream = PrettyStream(msg, True, False)
    assert pretty_stream.get_headers() == "Pair: Value\r\nPair: Value 2\r\n\r\n".encode('utf8')


# Generated at 2022-06-13 22:21:26.072208
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # test constructor with pretty_stream,
    #   assert pretty_stream is not None
    pretty_stream = PrettyStream(None, None, None, None)
    assert pretty_stream is not None

# Generated at 2022-06-13 22:21:36.923875
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import pytest

    env = Environment()
    msg = HTTPMessage()
    msg.headers.add('h1', 'v1')
    msg.headers.add('h2', 'v2')
    msg.headers.add('h3', 'v3')
    msg.headers.add('h3', 'v3-2')

    # h1: v1\nh2: v2\nh3: v3\nh3: v3-2
    headers = msg.headers

    # h1: v1\nh2: v2\nh3\n  v3\n  v3-2
    formatting = Formatting(env)
    expected_headers = formatting.format_headers(headers).encode(env.stdout_encoding)


# Generated at 2022-06-13 22:21:38.196789
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    stream = PrettyStream(Conversion(), Formatting())
    return stream


# Generated at 2022-06-13 22:21:39.655665
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    pass
