

# Generated at 2022-06-13 22:12:33.361574
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # Test class EncodedStream
    class TestEncodedStream(EncodedStream):
        CHUNK_SIZE = 1

        def iter_body(self) -> Iterable[bytes]:
            raise NotImplementedError()

    # default args
    http_message = HTTPMessage(b'HTTP/1.0 200 OK\r\n\r\n')
    s = TestEncodedStream(http_message)
    assert s.msg == http_message
    assert s.with_headers == True
    assert s.with_body == True
    assert s.on_body_chunk_downloaded == None
    assert s.output_encoding == 'utf8'
    # non-default args
    s = TestEncodedStream(http_message, with_headers=False, with_body=False)
    assert s.msg == http

# Generated at 2022-06-13 22:12:44.473411
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
  input_bytes = (b'{"text": "\\u3053\\u3093\\u306b\\u3061\\u306f\\u4e16\\u754c"}')
  #print(input_bytes)
  msg = HTTPMessage()
  msg.encoding = 'utf-8'
  msg.content_type = 'application/json;charset=utf-8'
  ps = PrettyStream(msg, conversion=Conversion(),
                    formatting=Formatting())
  output_bytes = bytearray()
  for chunk in ps.iter_body():
    output_bytes.extend(chunk)
  assert(input_bytes == output_bytes)


# Generated at 2022-06-13 22:12:52.178343
# Unit test for method process_body of class PrettyStream

# Generated at 2022-06-13 22:12:57.549295
# Unit test for constructor of class RawStream
def test_RawStream():
    msg = HTTPMessage(b'test_body')
    with_headers = True
    with_body = True
    on_body_chunk_downloaded = None

    rs = RawStream(msg, with_headers, with_body, on_body_chunk_downloaded)
    print(rs)

# Generated at 2022-06-13 22:13:08.605079
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.output.processing import BodyLinesFormatter
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPMessage
    from httpie.status import ExitStatus
    import pytest
    from httpie.cookie import CookieJar
    from httpie.core import main
    from httpie import ExitStatus

    from utils import HTTP_OK, MockEnvironment


# Generated at 2022-06-13 22:13:13.574753
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    #Given
    env = Environment()
    #When
    es = EncodedStream(env=env,msg=HTTPMessage(),with_headers=True,with_body=True,on_body_chunk_downloaded=None)
    #Then
    assert es != None


# Generated at 2022-06-13 22:13:24.351239
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    from httpie.models import HTTPResponse
    from httpie.downloads import StreamingHTTPResponse
    from httpie.output.streams import EncodedStream
    from httpie.compat import StringIO
    response = StreamingHTTPResponse(
            StringIO(
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain; charset=utf8\r\n"
                    "\r\n"
                    "Hello World"
            ),
            URL('http://example.com')
    )
    stream = EncodedStream(HTTPResponse.from_stream(response))
    assert 'Hello World' in stream

# Generated at 2022-06-13 22:13:37.327030
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # given
    msg = HTTPMessage(headers="Vary: Accept-Encoding\n"
                              "Content-Type: application/json\n"
                              "Content-Length: 12\n"
                              "X-Request-Id: f0093c8b-1180-4817-aff0-c3b2a3a3a3a3\n"
                              "Date: Sun, 16 Sep 2018 12:36:48 GMT\n"
                              "Connection: keep-alive",
                      body="{\"key\": \"value\"}\n")

    env = Environment(stdout_isatty=False, stdout_encoding='utf8')
    conversion = Conversion()

# Generated at 2022-06-13 22:13:45.389739
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie import ExitStatus
    from httpie.compat import urlopen
    from httpie.context import Environment
    from httpie.core import main
    from httpie.models import HTTPMessage, HTTPRequest
    from httpie.output.formatters import JSONFormatter
    from httpie.plugins import plugin_manager
    import pytest
    env = Environment()
    formatter = JSONFormatter()
    conversion = plugin_manager.get_converter()
    formatting = JSONFormatter()
    request = HTTPRequest(
        'GET', 'http://httpbin.org/get',
        headers={'Accept': 'application/json'},
        auth='user:pass',
    )
    response = urlopen(request.url)
    msg = HTTPMessage.from_http(response, request=request)
    stream = Buff

# Generated at 2022-06-13 22:13:52.693095
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    response = """HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf8

Hello
World
"""
    msg = HTTPMessage.from_http(response)
    stream = EncodedStream(msg)
    lines = list(stream.iter_body())
    #print(len(lines))
    #print(lines)
    assert lines[0] == b'Hello\r\n'
    assert lines[1] == b'World\r\n'



# Generated at 2022-06-13 22:14:09.748596
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Use the exact conversion and formatting
    # as in class PrettyStream.
    conversion = Conversion()
    formatting = Formatting(auto_json=True, pretty=True)
    msg = HTTPMessage(headers={}, body={"foo": "bar"})
    msg.content_type = 'application/json'
    msg.encoding = 'utf8'
    stream = PrettyStream(msg=msg, conversion=conversion, formatting=formatting)
    body = [line for line in stream.iter_body()]
    assert body == [b'{\n  "foo": "bar"\n}']

# Generated at 2022-06-13 22:14:20.668539
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    class TestMessage(HTTPMessage):
        encoding = 'utf8'
        headers = """\
X-Test: Foo
Content-Type: text/html; charset=utf8
Content-Length: 18

""".encode('utf8')
        body = '<b>Hello</b>'.encode('utf8')

    stream = EncodedStream(msg=TestMessage())
    assert list(stream.iter_body()) == [
        b'<b>Hello</b>',
    ]
    return True


# Generated at 2022-06-13 22:14:25.404285
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    '''
        Test for EncodedStream
        Test Data: ('some text')
        Expected Output: ('some text')
        '''
    msg = HTTPMessage('some_text')
    message_stream = EncodedStream(msg)
    assert message_stream.iter_body()


# Generated at 2022-06-13 22:14:35.844705
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # expect that the output_encoding attribute is set to 'utf8' because
    # the environment's stdout_isatty attribute is set to False
    test_instance = EncodedStream(env=Environment(stdout_isatty=False), msg=HTTPMessage())
    assert test_instance.output_encoding == 'utf8'

    # expect that the output_encoding attribute is set to 'utf8' because
    # the message's encoding attribute is None
    test_instance = EncodedStream(env=Environment(stdout_isatty=True), msg=HTTPMessage())
    assert test_instance.output_encoding == 'utf8'

    # expect that the output_encoding attribute is set to the environment's stdout_encoding
    # because the environment's stdout_isatty attribute is set to True
    test

# Generated at 2022-06-13 22:14:43.795128
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    conversion = Conversion()
    formatting = Formatting()
    pretty_st = PrettyStream(msg=HTTPMessage(), conversion=conversion,
                             formatting=formatting)
    assert pretty_st.process_body(b'\x7b\x22\x6c\x6f\x63\x61\x74\x69\x6f\x6e\x69\x6e\x6f\x6f\x6e\x22\x3a\x22\x31\x30\x30\x32\x22\x7d') == b'{\n    "locationinoo"\n    "1002"\n}'

# Generated at 2022-06-13 22:14:49.947927
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import httpie
    env = httpie.Environment()
    msg = httpie.models.HTTPMessage(encoding='utf8')
    msg.headers['content-type'] = 'text/plain'
    msg.raw = [b'abc', b'\x8f']
    buf = BufferedPrettyStream(msg, env)
    print(buf.iter_body())

# Generated at 2022-06-13 22:14:51.095254
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    assert BufferedPrettyStream != None


# Generated at 2022-06-13 22:15:00.064152
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # If no converter, the body is binary (contains null character '\0')
    body = b'\x7f\x00\x00\x01'
    msg = HTTPMessage(body=body)
    httpstream = BufferedPrettyStream(msg=msg)
    assert body == b''.join(httpstream.iter_body())
    # If there is converter, then body does not contain null character '\0'
    # For example, body containing gzip data will be decompressed by
    # converter (decompress_gzip converter) and no null character '\0'
    # will be found in decompressed data
    body = b'\x7f\x00\x00\x01'
    msg = HTTPMessage(body=body, content_type='application/x-gzip')
    httpstream = Buffered

# Generated at 2022-06-13 22:15:11.666028
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    env = Environment()
    # TODO refactor
    from httpie.output.streams import PrettyStream
    from httpie.output.formatters.colors import get_lexer
    formatting = Formatting(
        get_lexer(None, env),
        True, False, False, False, False, None
    )
    conversion = Conversion()
    msg = HTTPMessage(
        headers=None, body=b'{"k": "v"}\n', headers_str=None,
        encoding='utf8', content_type='application/json'
    )
    chunks = PrettyStream(msg, True, True, conversion, formatting, env).iter_body()
    # If a converter was used, then body is str,
    # otherwise bytes.
    content = next(chunks).decode('utf8')

# Generated at 2022-06-13 22:15:24.971854
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    from httpie.models import HTTPResponse
    from httpie.output import Conversion, Formatting
    from httpie.output.streams import BufferedPrettyStream
    from httpie.utils import Response

    mime = 'text/plain'
    body = b'Not binary data'
    headers = {'Content-Type': mime}
    conversion = Conversion()
    formatting = Formatting()
    response = HTTPResponse(Response(headers=headers, body=body))
    buffered_pretty_stream = BufferedPrettyStream(
        msg=response, with_headers=False, with_body=True,
        conversion=conversion, formatting=formatting)

    assert isinstance(buffered_pretty_stream, BufferedPrettyStream)
    assert isinstance(buffered_pretty_stream, PrettyStream)

# Generated at 2022-06-13 22:15:52.924000
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    class Request(HTTPMessage):
        def __init__(self, data):
            super().__init__('HTTP/1.1 200 OK')
            self.data = data

        def iter_lines(self, chunk_size):
            for line in self.data.splitlines(keepends=True):
                yield line, '\n' if line.endswith('\n') else '\r\n'

    request = Request('key=value')
    stream = PrettyStream(request, conversion=Conversion(),
                                  formatting=Formatting())
    assert list(stream.iter_body()) == [b'key=value\r\n']

# Generated at 2022-06-13 22:15:56.617607
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage()
    env = Environment()
    conversion = Conversion()
    formatting = Formatting()
    output_encoding = 'utf8'
    chunk_size = 1
    with_headers = True
    with_body = True

    assert msg is not None
    assert env is not None
    assert conversion is not None
    assert formatting is not None
    assert output_encoding is not None
    assert with_headers is not None
    assert with_body is not None

# Generated at 2022-06-13 22:16:03.916402
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    message = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'
    msg = HTTPMessage(io.BytesIO(message.encode('utf-8')))
    result = PrettyStream(
        msg=msg,
        with_headers=True,
        with_body=True,
    ).get_headers().decode()
    assert result == 'Content-Type: text/plain; charset=utf-8'



# Generated at 2022-06-13 22:16:14.954424
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import HTTPMessage

    msg = HTTPMessage(
        headers={'Content-Type': 'application/json; charset=utf8'},
        body=b'{"some": "body"}',
    )
    stream = PrettyStream(
        msg=msg,
        with_headers=True,
        with_body=True,
        conversion=None,
        formatting=None,
    )

    iterator = stream.iter_body()

    assert next(iterator) == b'{"some": "body"}'
    assert next(iterator) == b''

    try:
        next(iterator)
    except StopIteration:
        pass
    else:
        assert False, 'The iterator should be exhausted'



# Generated at 2022-06-13 22:16:32.735152
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    """Encoding of pretty stream is the same as EncodedStream"""
    binary_suppressed_notice_utf8 = BINARY_SUPPRESSED_NOTICE.decode("utf8",'ignore') 
    # test iter_body with and without binary data
    class Stream(PrettyStream): 
        def __init__(self, with_headers=True, with_body=True, on_body_chunk_downloaded=None, binary=False):
            self.binary = binary
            self.msg = HTTPMessage()
            self.msg.encoding = 'utf8'
            self.msg.content_type = 'text/plain'
            self.with_headers = with_headers
            self.with_body = with_body
            self.body = 'hello' if not self.binary else b'\x80'
        
       

# Generated at 2022-06-13 22:16:38.637902
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    """Unit test for method iter_body of class PrettyStream."""
    msg = HTTPMessage(
        status=200, headers={"Content-Type": "text/html"},
        encoding='utf8', body=b'{"a":1, "b":2}'
    )
    ps = PrettyStream(msg, True, True, None, None, None)
    assert ps.iter_body().__next__().decode('utf8') == '{"a":1, "b":2}'

# Generated at 2022-06-13 22:16:43.223489
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    msg = 'hello world'
    msg_bytes = msg.encode("utf-8")

    stream = BufferedPrettyStream(msg, False, True)

    assert(msg_bytes == next(stream.msg.iter_body()))



# Generated at 2022-06-13 22:16:56.549714
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import httpie.compat
    import httpie.output.streams

    headers_str = """HTTP/1.1 200 OK
Content-Length: 3
Content-Type: text/plain; charset=utf-8
Connection: keep-alive\r
\r
"""

    headers = httpie.compat.OrderedDict([
        ('HTTP/1.1', '200 OK'),
        ('Content-Length', '3'),
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Connection', 'keep-alive')
    ])

    msg = httpie.output.streams.HTTPMessage(headers=headers, body=b'abc')
    stream = httpie.output.streams.PrettyStream(msg, with_body=False)
    result = stream.get_headers()

   

# Generated at 2022-06-13 22:17:05.530054
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage(headers={"key1": "value1", "key2": "value2"})
    msg.body = b'{ "name": "Hello World" }'
    msg._encoding='utf-8'
    msg.content_type="application/json"
    msg._stream_len=len(msg.body)
    stream = BufferedPrettyStream(msg=msg, with_headers=True, with_body=True)
    for chunk in stream.iter_body():
        print(chunk)

# Generated at 2022-06-13 22:17:08.585959
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    assert EncodedStream(msg=HTTPMessage()).msg is not None
    assert EncodedStream(msg=HTTPMessage(), with_headers=False).with_headers is False
    assert EncodedStream(msg=HTTPMessage(), with_body=False).with_body is False

# Generated at 2022-06-13 22:17:50.189599
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPRequestMessage, HTTPResponseMessage
    env = Environment()
    request_object = HTTPRequestMessage.from_raw('GET http://example.com/ HTTP/1.1', env)
    response_object = HTTPResponseMessage.from_raw('HTTP/1.1 200 OK\n\n', env)
    for stream_object in [BufferedPrettyStream(request_object, env=env),
                          BufferedPrettyStream(response_object, env=env)]:
        iter(stream_object)
        if stream_object.with_body:
            stream_object.iter_body()

# Generated at 2022-06-13 22:18:02.340942
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    msg = '''HTTP/1.1 200 OK\r
Require: http-utils\r
Carbs: 1.0\r
Content-Length: 94\r
Content-Range: bytes 0-93/94\r
Content-Type: text/html; charset=UTF-8\r
Date: Sun, 08 Sep 2019 17:32:16 GMT\r
Server: Apache/2.4.46 (Unix)\r
\r
<!DOCTYPE html>\n<html lang="en">\n<head>\n<title>HTTPie</title>\n'''
    message = HTTPMessage.from_bytes(msg, url='http://127.0.0.1')
    stream = BufferedPrettyStream(message, True, True)
    for chunk in stream:
        print(chunk)

# Generated at 2022-06-13 22:18:11.774904
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    msg = HTTPMessage()
    msg.headers = "h1: v1\r\nh2: v2\r\n"
    msg.body = b"hello world!"
    with_headers = True
    with_body = True
    result = []
    stream = BaseStream(msg, with_headers, with_body)
    for chunk in stream:
        result.append(chunk)
    assert result == [b"h1: v1\r\nh2: v2\r\n\r\n\nhello world!"]



# Generated at 2022-06-13 22:18:19.283291
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import json
    import requests
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPResponse

    headers = {'Host': 'httpbin.org', 'User-Agent': 'HTTPie/1.0.2', 'Accept': '*/*'}
    body = requests.get('http://httpbin.org/headers', headers=headers)
    response = HTTPResponse(body.raw)
    # assert body.text == json.loads(response.body)

    conversion = Conversion()
    formatting = Formatting(sorted_headers=False)
    stream = BufferedPrettyStream(
        formatting=formatting,
        conversion=conversion,
        msg=response,
        chunk_size=1024 * 10,
        with_headers=True,
        with_body=True
    )

# Generated at 2022-06-13 22:18:31.429862
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    method = BufferedPrettyStream.iter_body
    
    test = method(_)

    class IterBody:
        def __call__(self, *args, **kwargs):
            return self

        def __iter__(self):
            self.i = 1
            return self

        def __next__(self):
            if self.i == 1:
                self.i += 1
                for result in [b'\n']:
                    yield result
            else:
                raise StopIteration

    class PrettyStream:
        def __init__(self, msg):
            self.msg = msg

        def process_body(self, chunk: Union[str, bytes]) -> bytes:
            if chunk == b'\n':
                return b'\n'
            else:
                return b' '


# Generated at 2022-06-13 22:18:42.297244
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class MockMsg:
        def __init__(self, iter_body_ret, content_type):
            self.iter_body_ret = iter_body_ret
            self.content_type = content_type
        def iter_body(self, chunk_size):
            return self.iter_body_ret

    class MockConversion:
        def get_converter(self, mime):
            if mime == "text/plain":
                class MockConverter:
                    def convert(self, body):
                        return "text/plain", body.decode()
                return MockConverter()
            else:
                return None
    class MockFormatting:
        def format_body(self, content, mime):
            return content

    import io

# Generated at 2022-06-13 22:18:47.571083
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.input.v2 import Request
    from httpie.models import RequestObject
    from httpie.output import BINARY_SUPPRESSED_NOTICE, RawStream
    # 构建请求对象
    r = Request(
        method='POST',
        url='http://httpbin.org/post',
        headers=None,
        data='helloworld',
        files=None,
        json=None,
        auth=None,
        allow_redirects=True
    )
    assert isinstance(r, RequestObject)
    stream = RawStream(msg=r.http_request)
    body = stream.iter_body()
    for i in body:
        assert i == b'helloworld'


# Generated at 2022-06-13 22:18:53.811374
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    m = MIMEText(b'abc\0\r\nabc\r\nabc', _charset='utf-8')
    m['Content-Type'] = 'text/html; charset=utf-8'
    s = EncodedStream(msg=m)
    assert [b'abc\0\r\n'] == [i for i in s.iter_body()]

# Generated at 2022-06-13 22:19:04.440916
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import textwrap
    from httpie.input import ParseRequest

    def test_iter_body_json(json):
        req = ParseRequest().parse('http://127.0.0.1:8081')
        req.body = json
        req.headers['Content-Type'] = 'application/json'
        s = BufferedPrettyStream(msg=req, with_body=True)
        return s.iter_body()

    def test_iter_body_form(form):
        req = ParseRequest().parse('http://127.0.0.1:8081')
        req.body = form
        req.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        s = BufferedPrettyStream(msg=req, with_body=True)
        return s.iter_body()

   

# Generated at 2022-06-13 22:19:06.257583
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    BaseStream.__iter__()

# Generated at 2022-06-13 22:20:22.012294
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import io
    import csv
    fp = io.BytesIO(b'key1,key2\r\nvalue1,value2\r\n')
    n = 0
    while True:
        n = n + 1
        line = fp.readline()
        if not line:
            break
        print(line)
    print('n=',n)
    print('type(line)=',type(line))


# Generated at 2022-06-13 22:20:23.242514
# Unit test for constructor of class PrettyStream
def test_PrettyStream():

    assert type(PrettyStream) == type(object)

# Generated at 2022-06-13 22:20:36.483854
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import ResponseInfo
    from httpie.output.formatters import JsonFormatter
    from httpie.output import outputters
    from httpie.output.formatters.colors import get_lexer

    conversion = Conversion()
    formatting = Formatting(
        json_indent=2, headers_max_length=0, max_json_size=2,
        max_body_size=0, force_json=False,
        body_formatter=JsonFormatter(get_lexer(), None)
    )
    response = ResponseInfo(
        headers={'Content-Type': 'text/json'},
        status_code=200,
        encoding='utf-8',
        reason='OK',
        http_version='HTTP/1.1',
        redirect_url=None

    )
    response.raw

# Generated at 2022-06-13 22:20:37.442596
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    e = EncodedStream()

# Generated at 2022-06-13 22:20:39.237923
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = requests.head("https://httpbin.org/get").headers
    h = PrettyStream(headers, with_headers=True, with_body=False)
    print(h.get_headers())


# Generated at 2022-06-13 22:20:45.236593
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    env = Environment(headers=[])
    msg = HTTPMessage()
    msg.content_type = 'text/plain'
    msg.encoding = 'utf8'
    body = "body text"
    msg.body = body
    msg.encoded_body = body.encode('utf8')
    stream = PrettyStream(msg, with_body=True, with_headers=False, env=env)
    assert stream.process_body(body) == msg.encoded_body
    msg.content_type = 'text/html'
    stream = PrettyStream(msg, with_body=True, with_headers=False, env=env)
    assert stream.process_body(body) == msg.encoded_body

    # test for case when chunk is a byte string
    msg.content_type = 'text/plain'
   

# Generated at 2022-06-13 22:20:55.917603
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import json

    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    from httpie.output.processing import Conversion, Formatting
    from httpie.plugins import body_formatter
    from httpie.input import Parser

    body = {'aaa':'bbb','ccc':'ddd'}
    data = json.dumps(body,ensure_ascii=False)
    headers = Parser.parse_headers('Content-Type: application/json; charset=utf-8')
    msg = HTTPMessage(data.encode("utf-8"), headers)

    # if not is_windows:
    #     env = Environment(
    #         stdin=None,
    #         stdout=subprocess.PIPE,


# Generated at 2022-06-13 22:21:01.169057
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(None, None, None, None)
    chunk = b'\x41\x42\x43'
    assert stream.process_body(chunk) == b'ABC\n'

    chunk = b'\x61\x62\x63'
    assert stream.process_body(chunk) == b'abc\n'


# Generated at 2022-06-13 22:21:14.963792
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import json
    import time
    import timeit
    import requests
    if __name__ == '__main__':
        env = Environment()
        url = "https://api.github.com/repos/jakubroztocil/httpie"
        r = requests.get(url)
        assert r.encoding is None, "Encoding should be none for binary data"
        assert r.headers['content-type'] == 'application/json; charset=utf-8'
        #print(r.headers['content-type'].split(';')[0])
        msg = HTTPMessage(r.headers, r.text, encoding=r.encoding)
        #print(msg.raw.read(4096))
        #/usr/local/lib/python3.6/site-packages/httpie/output/__

# Generated at 2022-06-13 22:21:16.353523
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print(EncodedStream)
