

# Generated at 2022-06-13 22:12:29.388894
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    """Test iter_body of EncodedStream class."""
    import test_client
    import test_client as test_client
    env = Environment()
    response = test_client.HttpBin().get()
    output = EncodedStream(response, env=env)
    returned = []
    for chunk in output.iter_body():
        returned.append(chunk)
    assert returned == [b'{}']
test_EncodedStream_iter_body()

# Generated at 2022-06-13 22:12:38.940244
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import Response
    from httpie.output.processing import Conversion, Formatting
    headers = {'content-type': 'application/json'}
    body = b'{"a": "1", "b": 2, "c": "3"}'
    msg = Response(headers, body)
    expected = (b'{\n    "a": "1", \n    "b": 2, \n    '
                b'"c": "3"\n}')
    stream = BufferedPrettyStream(msg,
        with_headers=False, with_body=True,
        conversion=Conversion(), formatting=Formatting())
    # Using list() to force the reading of the whole body
    output = list(stream)[0]
    assert output == expected
    return 0


# Generated at 2022-06-13 22:12:49.274183
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
  from httpie.output.streams import PrettyStream
  from httpie.models import HTTPMessage
  from httpie.output.processing import Conversion, Formatting

  def callback(chunk) -> None:
      pass
  # Testing a Headers message and processing headers
  test_msg = HTTPMessage('HEADERS', headers='clé: été\r\n',
                         encoding='iso-8859-1')
  test_stream = PrettyStream(test_msg, conversion=Conversion(),
                             formatting=Formatting(), with_body=False,
                             on_body_chunk_downloaded=callback)

  assert test_stream.get_headers() == b'cl\xe9: \xe9t\xe9\r\n'

  # Testing a Text message and processing body
  test_msg = HTTPMessage

# Generated at 2022-06-13 22:13:03.728482
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.core import main as httpie_core
    from httpie import ExitStatus
    from httpie import http


# Generated at 2022-06-13 22:13:11.432175
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage()
    msg.body = "Hello World!"
    stream = RawStream(msg=msg,with_headers=True,with_body=True)
    body = ""
    for chunk in stream.iter_body():
        body += chunk.decode("utf-8")
    # Make sure that the whole body is sent
    assert body == "Hello World!"


# Generated at 2022-06-13 22:13:20.953551
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    msg.url = "http://www.example.com"
    msg.headers = "Content-Type: application/json"
    env = Environment()
    env.stdout_isatty = False
    conversion = Conversion()
    formatting = Formatting()
    s = PrettyStream(
        msg=msg,
        conversion=conversion,
        formatting=formatting,
        env=env,
        with_headers=True,
        with_body=True,
    )

    assert s.get_headers() == b'Content-Type: application/json'

# Generated at 2022-06-13 22:13:30.447304
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    httpResponse = ["Hello world\r\n", "This\r\n", "is\r\n", "a Message\r\n"]
    # body = b'Hello world\r\nThis\r\nis\r\na Message\r\n'
    # encoding = 'utf8'
    # output_encoding = 'utf8'
    # assert EncodedStream(body, encoding, output_encoding).iter_body() == httpResponse

    # body = b'Hello world\r\nThis\r\nis\r\na Message\r\n'
    # encoding = 'utf8'
    # output_encoding = 'ascii'
    # assert EncodedStream(body, encoding, output_encoding).iter_body() == httpResponse



# Generated at 2022-06-13 22:13:40.629785
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    def iter_body():
        yield b'hello'
        yield b'world'

    msg = HTTPMessage(headers=[('h', 'v')], body=iter_body())
    stream = BaseStream(msg=msg, with_headers=True, with_body=True)
    assert list(stream) == [b'h: v\r\n\r\n', b'hello', b'world']
    stream = BaseStream(msg=msg, with_headers=False, with_body=True)
    assert list(stream) == [b'hello', b'world']
    stream = BaseStream(msg=msg, with_headers=True, with_body=False)
    assert list(stream) == [b'h: v\r\n\r\n', b'\r\n\r\n']



# Generated at 2022-06-13 22:13:53.140754
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    url = 'http://www.baidu.com'
    request.url = url
    request.method = 'GET'
    request.headers = {'user-agent': 'curl/7.54.0', 'accept': '*/*'}
    request.body = ''

    response.status_code = 200

# Generated at 2022-06-13 22:14:02.014327
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    '''test function test_PrettyStream_process_body
    to check the test cases pass or not
    '''

# Generated at 2022-06-13 22:14:22.321224
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    with open("EncodedStream_iter_body.txt", mode='w+') as file:
        from httpie import ExitStatus
        from httpie.compat import urllib
        from httpie.downloads import (
            parse_content_range, filename_from_content_disposition,
            filename_from_url, get_unique_filename, ContentRangeError,
        )
        from httpie.input import SEP_CREDENTIALS
        from httpie.plugins import plugin_manager
        from httpie.utils import (
            get_binary_stream, get_response_range, get_response_stream,
            is_file_url, is_windows, parse_version, str_to_python_type,
            super_len,
        )

        # Taken from https://github.com/jkbrzt/httpie/

# Generated at 2022-06-13 22:14:35.249540
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import Response
    from io import BytesIO
    # 下面的内容是原文中的测试用例，在中文环境下运行时会报错
    # msg = Response(http_version='1.1',
    #                status_code=200,
    #                headers=CaseInsensitiveDictNameView(CaseInsensitiveDict({
    #                    'Content-Type': 'text/plain; charset=utf8',
    #                    'Content-Length': '14',
    #                })),
    #                content=BytesIO(b'\u00a1Unicode!\xe9'))
    # 将测试用例

# Generated at 2022-06-13 22:14:43.945308
# Unit test for method process_body of class PrettyStream

# Generated at 2022-06-13 22:14:55.489107
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    msg = HTTPMessage(headers={'content-type': 'application/json'},
                      body='{"name": "a", "full_name": "b"}',
                      encoding='utf-8')
    stream = PrettyStream(msg=msg,
                          with_headers=True,
                          with_body=True,
                          conversion=Conversion(),
                          formatting=Formatting())
    body = stream.process_body('{"name": "a", "full_name": "b"}')

# Generated at 2022-06-13 22:15:08.197745
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    data = [1,2,3,4,5]
    class Msg:
        def __init__(self, msgtype):
            self.msgtype = msgtype # HTTPResponse
            self.content_type = 'application/json'
            self.encoding = 'utf-8'
            self.data = data
            self.headers = 'HTTP/1.1 200 OK'

        def iter_body(self, chunk_size):
            return self.data

    msg = Msg('HTTPResponse')

    # Init BufferedPrettyStream
    stream = BufferedPrettyStream(
        msg = msg,
        with_headers = True,
        with_body = True,
        conversion = Conversion(),
        formatting = Formatting()
    )

    # Return an iterator over the message body.

# Generated at 2022-06-13 22:15:12.709631
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    env = Environment()
    response = BufferedPrettyStream(env, {'Content-Type': 'text/plain', 'Content-Length': 4}, with_headers=False, with_body=True)
    body = next(response.iter_body())
    assert (body == b'abc\n'), 'unit test for iter_body failed'

# Generated at 2022-06-13 22:15:25.683995
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    class HTTPMessage_mock:
        def __init__(self):
            self.encoding = 'utf8'
        def iter_lines(self, size):
            yield b'x\x80x\x80', b'\n'
            yield b'x\x80', b'\n'
            yield b'x\x80x\x80', b'\n'
            yield b'x\x80', b'\n'
            yield b'x\x80x\x80', b'\n'
            yield b'x\x80', b'\n'
            yield b'x\x80x\x80', b'\n'
            yield b'x\x80', b'\n'
    msg = HTTPMessage_mock()
  

# Generated at 2022-06-13 22:15:33.426616
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.core import main
    from httpie.output.streams import BufferedPrettyStream
    import urllib3
    from httpie.output.processing import ContentTypeAutoMatchConverter

    # testing a simple request that returns an xml as response
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    env = Environment('stream.BufferedPrettyStream', 1024, 1024)
    stream = BufferedPrettyStream(HTTPMessage(), env=env, with_headers=False, with_body=True,
                                  conversion=ContentTypeAutoMatchConverter())
    # method iter_body of class BufferedPrettyStream
    assert stream.iter_body() is not ''

    # testing a request with a bad content_type header
    env = Environment('httpie', 1024, 1024)
    env

# Generated at 2022-06-13 22:15:34.721096
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    assert True


# Generated at 2022-06-13 22:15:38.629029
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers = '{"headers": "headers"}')
    print(PrettyStream(msg, with_headers = True, with_body = False).get_headers())



# Generated at 2022-06-13 22:15:57.380227
# Unit test for method iter_body of class PrettyStream

# Generated at 2022-06-13 22:16:02.524547
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(headers='', body='text')
    msg.encoding = 'utf-8'
    stream = EncodedStream(msg = msg)
    # Write the Stream to a string
    result = ''
    for item in stream.iter_body():
        result += item.decode('utf-8')
    assert result == 'text'



# Generated at 2022-06-13 22:16:08.805351
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import os
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    msg = HTTPMessage(headers)
    env = Environment(os.environ)
    ps = PrettyStream(msg, env, True, True)
    for h in ps.get_headers():
        pass


# Generated at 2022-06-13 22:16:12.187837
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    raw_stream = RawStream()
    encoded_stream = EncodedStream()
    assert(raw_stream.get_headers() == encoded_stream.get_headers())
    

# Generated at 2022-06-13 22:16:18.418795
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import pytest
    from httpie.models import HTTPMessage

    class Stream(BaseStream):
        pass

    class Msg(HTTPMessage):
        @property
        def headers(self):
            return 'headers '

    env = Environment()
    env.stdout_isatty = False
    with pytest.raises(NotImplementedError):
        Stream(msg=Msg(), with_headers=False, with_body=False).__iter__()

# Generated at 2022-06-13 22:16:38.968641
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    from httpie.models import HTTPRequest
    from httpie.context import Environment
    from httpie.output.processing import Conversion, Formatting
    from httpie.output.streams import EncodedStream, PrettyStream, BufferedPrettyStream
    from httpie.output.writers import write_binary_to
    env = Environment()
    r = HTTPRequest('GET', 'https://www.baidu.com', headers={'User-Agent': 'me'})
    s = EncodedStream(r, with_headers=True, with_body=True, env=env)
    s.__iter__()
    write_binary_to(s, env.stdout)
    s = PrettyStream(r, with_headers=True, with_body=True, env=env, conversion=Conversion(env), formatting=Formatting(env))
    s.__

# Generated at 2022-06-13 22:16:45.450616
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage(
        status_line=b'X',
        headers=b'X',
        body=b'a' * 1024 * 10 + b'\0'
    )
    assert next(BufferedPrettyStream(msg).iter_body()) == BINARY_SUPPRESSED_NOTICE



# Generated at 2022-06-13 22:16:57.290196
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    class Message(HTTPMessage):
        def __init__(self, status: str, headers: dict, body: dict):
            self.status = status
            self.headers = headers
            self.body = body

        def iter_body(self, chunk_size):
            output = self.body
            while output:
                yield output[:chunk_size]
                output = output[chunk_size:]

    msg = Message('test', {'test': 'test'}, {'test': 'test'})
    stream = BaseStream(msg, with_headers=True, with_body=True)
    output = []
    for chunk in stream:
        output.append(chunk)
    assert b''.join(output) == b'test: test\r\n\r\n{\'test\': \'test\'}'



# Generated at 2022-06-13 22:17:08.193487
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    chunks = RawStream.CHUNK_SIZE*b'a' + b'b'*2
    raw = RawStream(None,False,True)
    raw._RawStream__init__(None,False,True)
    raw.msg = TestBody(chunks)
    raw2 = RawStream(None,False,True)
    raw2._RawStream__init__(None,False,True)
    raw2.msg = TestBody(b'\00')
    return (
        list(raw.iter_body()) == [RawStream.CHUNK_SIZE*b'a'] + [b'b'*2],
        list(raw2.iter_body()) == [b'\00']
    )


# Generated at 2022-06-13 22:17:13.399355
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    b = BaseStream(msg=None, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    b.iter_body = lambda: b'ok'
    assert hasattr(b, '__iter__')
    assert list(b) == [b'ok']


# Generated at 2022-06-13 22:17:35.892195
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # 创建消息体
    msg = HTTPMessage()
    msg.headers = ""
    msg.encoding = 'utf8'
    # 创建环境，并设置环境变量
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf8'
    # 创建格式化器
    formatting = Formatting()
    # 创建转换器
    conversion = Conversion()
    # 创建一个PrettyStream流

# Generated at 2022-06-13 22:17:48.266372
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():

    if __name__ == '__main__':

        # Создаём mock объект с телом запроса
        mock_msg_html = mock.Mock(spec=HTTPMessage,
                                  body= '<html>\r\n</html>')
        mock_msg_html.content_type.split.return_value = 'text/html'
        mock_msg_html.status_code = 200

        # Создаём mock объект с телом ответа
        mock_msg_text = mock.Mock(spec=HTTPMessage,
                                  body= 'Hello, world')
        mock_msg_text.content

# Generated at 2022-06-13 22:17:55.775138
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(None, None)
    assert stream.process_body('foo') == b'foo'
    assert stream.process_body('foo\n') == b'foo\n'
    assert stream.process_body(b'foo') == b'foo'
    assert stream.process_body(b'foo\n') == b'foo\n'
    assert stream.process_body('foo') == b'foo'

# Generated at 2022-06-13 22:18:05.679928
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    if sys.version_info < (3, 0):
        return

    import pytest
    from hypothesis import assume, settings, HealthCheck
    from hypothesis.strategies import integers, text, binary
    from httpie.compat import StringIO
    from httpie.models import HTTPResponse
    from httpie.output.streams import RawStream
    
    @settings(suppress_health_check=[HealthCheck.too_slow])
    @given(binary())
    def test_BaseStream___iter__body(body):
        assume(b'\0' not in body)
        response = HTTPResponse(b'HTTP/1.1 200 OK\r\n', body=body)
        assert b''.join(RawStream(response, chunk_size=1)) == body


# Generated at 2022-06-13 22:18:15.667729
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    http_message = HTTPMessage(
        headers={'Content-Type': 'application/json'},
        encoding='utf8',
        body=b"{\"a\": \"b\"}")
    stream = PrettyStream(http_message,
                          env=Environment(),
                          conversion=Conversion(),
                          formatting=Formatting()
                          )
    assert stream.process_body(http_message.body) == b"{\n    \"a\": \"b\"\n}"
    http_message = HTTPMessage(
        headers={'Content-Type': 'application/json'},
        encoding='utf8',
        body=b"{\"a\": \"b\", \"c\": \"d\"}")

# Generated at 2022-06-13 22:18:24.444465
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    """Unit test for method process_body of class PrettyStream"""
    import httpie
    import httpie.output.formatters as formatters
    import httpie.output.streams as streams
    import httpie.output.formatters.colors as colors
    import httpie.output.streams as streams
    import httpie.models as models
    import httpie.output.streams as streams
    import httpie.output.formatters as formatters
    import httpie.output.streams as streams
    import httpie.output.streams.base as base

    headers = httpie.models.Headers()
    headers.add('content-type', 'application/json')
    headers.add('content-location', 'http://example.com')


# Generated at 2022-06-13 22:18:36.255627
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.output.streams import PrettyStream
    from httpie.models import HTTPMessage
    from httpie.output.formats import AutoJSONFormatter
    from httpie.output.formats.base import FormattedResponse
    from httpie.output.converters import JSONConverter
    from httpie.core import main
    from httpie.compat import is_py26

    args = main.parser.parse_args(args=[
        '--print', 'hb',
        '--pretty=all',
        'GET',
        'http://httpbin.org/get'
    ])

    output_options = main.get_output_options(args)
    debug = args.debug
    env = main.get_environ(args)
    output_kwargs = {}
    if debug:
        output_kw

# Generated at 2022-06-13 22:18:45.470197
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    bytes_stream = b"HTTP/1.1 200 OK\r\n" \
                   b"Content-Type: text/plain; charset=utf-8\r\n" \
                   b"Date: Fri, 17 Nov 2017 07:49:04 GMT\r\n\r\n" \
                   b"abc\r\ndef\n\r"
    stream = EncodedStream(HTTPMessage.from_bytes(bytes_stream, 'utf-8'))
    assert b''.join(stream.iter_body()) == b"abc\r\ndef\n\r"


# Generated at 2022-06-13 22:18:57.701365
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    def _test_PrettyStream_iter_body(iter_lines, expected):
        iter_lines = iter_lines.copy()
        msg = Mock()
        msg.iter_lines = Mock(return_value=iter_lines)
        msg.headers = 'foo: bar'
        msg.content_type = 'baz; blah'
        msg.encoding = 'utf8'
        stream = PrettyStream(None, None, msg=msg)
        for line, lf in stream.iter_body():
            assert line == expected[:len(line)]
            expected = expected[len(line):]
        assert not expected

    # No conversions.

# Generated at 2022-06-13 22:19:05.209577
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import HTTPResponse
    import json
    # test with valid json
    response = HTTPResponse(json.dumps({'test':'json'}).encode())
    resp_stream = EncodedStream(response)
    for body in resp_stream.iter_body():
        print(body)
    # test with invalid json
    response = HTTPResponse("{'test':'json'}".encode())
    resp_stream = EncodedStream(response)
    for body in resp_stream.iter_body():
        print(body)
    
if __name__ == "__main__":
    test_EncodedStream_iter_body()

# Generated at 2022-06-13 22:19:56.303046
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    s = PrettyStream(None, None, msg=None)

    # Case 1: input is str type
    sample = '\u03bc\u03b5\u03b9\u03bc\u03ad\u03bb\u03b5\u03c3\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac'
    result = s.process_body(sample)
    expect = b'\xce\xbc\xce\xb5\xce\xb9\xce\xbc\xce\xad\xce\xbb\xce\xb5\xcf\x83\xce\xbc\xce\xb1\xcf\x84\xce\xb9\xce\xba\xce\xac'

# Generated at 2022-06-13 22:19:59.761567
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # Command line arguments
    encoded_stream = EncodedStream(msg = '')
    # Properties
    assert encoded_stream.output_encoding == 'utf8'


# Generated at 2022-06-13 22:20:08.054414
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():

    print("Starting test_PrettyStream_iter_body")

    # First test case: content-type is text/csv, no streaming of lines, no body data
    headers_json = '{"content-type": "text/csv"}'
    body_json = ''
    env = Environment()

# Generated at 2022-06-13 22:20:13.441082
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = {'Content-Type': 'application/json'}
    msg = HTTPMessage.without_body(headers=headers)
    stream = PrettyStream(msg=msg,
            formatting=Formatting(), conversion=Conversion())
    assert stream.get_headers() == b'"Content-Type: application/json\\n"'

test_PrettyStream_get_headers()

# Generated at 2022-06-13 22:20:15.217907
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # test_PrettyStream()
    assert True


# Generated at 2022-06-13 22:20:27.282422
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import httpie.input.v1
    import httpie.output.v1
    args = httpie.input.v1.parse_args(['https://httpbin.org/get'])
    args.pretty = True
    args.prettify = {}
    args.all = True
    args.output_options = {}
    req = httpie.input.v1.HTTPieRequest(args)
    req.method = b'GET'
    req.url = b'https://httpbin.org/get'
    req.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    req.body = b'{"foo": "bar"}'
    req.output_file = None
    req.stdout = io.BytesIO()
    req.env = httpie.Environment()
    req

# Generated at 2022-06-13 22:20:39.364930
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.cli.argtypes import KeyValue, KeyValueArgType
    from httpie.context import Environment
    from httpie.output.streams import EncodedStream
    from httpie.models import HTTPRequest, HTTPResponse

    encoding = 'utf8'
    msg = HTTPResponse(
        content_type='text/plain; charset=' + encoding,
        encoding=encoding,
    )

    form = KeyValueArgType()
    form.add_argument('--timeout', type=int)
    form.add_argument('--bilbob', type=str)


# Generated at 2022-06-13 22:20:49.021803
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # 下面是测试数据，用于测试EncodedStream.iter_body方法
    # 使用了迭代器chain,将三个迭代器组合起来，chain参数为多个迭代器
    test_data = chain(
        'hello',
        [' ', 'world'],
        (c for c in '!\n')
    )

    # 在Python中
    # 字符串是不可变的，所以一个字符一个字符的添加的话会不断的产生

# Generated at 2022-06-13 22:20:54.535369
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(msg='msg', conversion='conversion', formatting='formatting')
    assert stream.process_body(b'123') == b'123'
    assert stream.process_body(b'123\0') == b'123\0'
    assert stream.process_body(b'123\0') == b'123\0'

# Generated at 2022-06-13 22:21:02.421481
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    """
    This test case checks if BufferedPrettyStream() contructor is called
    correctly or not.
    """
    from httpie.output import Conversion, Formatting
    from httpie.models import HTTPMessage
    from httpie.output.streams import BufferedPrettyStream
    from httpie.context import Environment
    from httpie.utils import URL
    from httpie.cli.argtypes import KeyValueArg
    import mock
    env = Environment()

# Generated at 2022-06-13 22:21:53.488900
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Test with MIME Type = text
    msg = HTTPMessage()
    msg.content_type = 'text'
    msg.encoding = 'utf8'
    prettifier = PrettyStream(msg, conversion=Conversion(), formatting=Formatting())
    assert prettifier.process_body('body') == b'body'

    # Test with MIME Type = json
    msg = HTTPMessage()
    msg.content_type = 'application/json'
    msg.encoding = 'utf8'
    prettifier = PrettyStream(msg, conversion=Conversion(), formatting=Formatting())
    assert prettifier.process_body('{"status": "OK"}') == b'{\n    "status": "OK"\n}\n'

    # Test with MIME Type = xml
    msg = HTTPMessage()
    msg.content_

# Generated at 2022-06-13 22:22:03.121859
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    print()
    msg = HTTPMessage()
    msg.headers = "1\r\n2\r\n\r\n"
    msg.body = "body"
    msg.encoding = "utf8"
    msg.content_type = "text/plain"
    baseStream = BaseStream(msg, True, True)
    print(list(baseStream.__iter__()))


# Generated at 2022-06-13 22:22:13.059541
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import Message
    from httpie.output import byte_stream
    from httpie.compat import str

    msg = Message()
    msg.headers = 'foo: bar'
    msg.body = 'abc'
    msg_bytes = b'HTTP/1.1 200 OK\r\nfoo: bar\r\n\r\ndef\r\n'
    assert list(byte_stream(msg)) == [msg_bytes]
    msg.body = str('abc')
    assert list(byte_stream(msg)) == [msg_bytes]
    msg.body = b'def'
    assert list(byte_stream(msg)) == [msg_bytes]