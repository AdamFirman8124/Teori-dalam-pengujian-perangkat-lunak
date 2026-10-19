

# Generated at 2022-06-13 22:12:20.184459
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # Test for constructor of class PrettyStream
    PrettyStream()


# Generated at 2022-06-13 22:12:31.660840
# Unit test for method __iter__ of class BaseStream

# Generated at 2022-06-13 22:12:34.104107
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers = 'http://www.google.com')
    prettifier = PrettyStream(msg)
    print(prettifier.get_headers())


# Generated at 2022-06-13 22:12:38.692306
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = {'a': 'b', 'c': 'd'}
    obj = PrettyStream(HTTPMessage(headers=headers), False, False)
    assert obj.get_headers() == b'a: b\r\nc: d\r\n'

# Generated at 2022-06-13 22:12:46.991976
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():

    import json

    formatting = Formatting()
    conversion = Conversion()
    headers = dict(
        header1='text/html',
        header2='charset=utf-8',
    )
    msg = HTTPMessage(headers=headers, body='{"foo": "bar"}')

    for chunk in msg.iter_body(1):
        try:
            print(formatting.format_body(chunk, msg.headers))
        except:
            print(chunk)

# Generated at 2022-06-13 22:13:01.021044
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.models import HTTPMessage
    from httpie.output.streams import RawStream
    from httpie.output.processing import SimpleFormatting
    import httpie.output.formatters

    env = Environment(stdout_isatty=True, stdout_encoding='utf8')
    env.formatter = httpie.output.formatters.JSONFormatter(env)

    msg = HTTPMessage(env)
    with open('/home/yasoob/Downloads/sample.json') as f:
        msg.data = f.read()
    msg.encoding = 'utf8'

    stream = RawStream(msg=msg, formatting=SimpleFormatting(), env=env)

    for chunk in stream.iter_body():
        print(chunk)

# Test for EncodedStream

# Generated at 2022-06-13 22:13:03.679598
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    with pytest.raises(NotImplementedError):
        stream_obj = BaseStream()
        generator = stream_obj.__iter__()
        assert isinstance(generator, Iterable)



# Generated at 2022-06-13 22:13:17.317705
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Test with all kind of unicode
    test_msg = HTTPMessage(b"HTTP/1.1 200 OK\r\n"
                      b"Content-Length: 10\r\n"
                      b"Content-Type: application/json\r\n"
                      b"\r\n"
                      b"{ \"key1\": \"value1\" }\n"
                                 b"{ \"key2\": \"value2\" }\n"
                                 b"{ \"key3\": \"value3\" }\n")
    # Test with utf8 encoding
    test_msg.encoding = 'utf8'
    test_msg.headers = test_msg.headers
    gen_iter_body = EncodedStream.iter_body(test_msg)
    assert b'{' in next(gen_iter_body)
   

# Generated at 2022-06-13 22:13:23.661827
# Unit test for method iter_body of class EncodedStream

# Generated at 2022-06-13 22:13:27.136671
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    test = BufferedPrettyStream(msg='test message', with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    assert test


# Generated at 2022-06-13 22:13:34.542948
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    str("test")
    assert True


# Generated at 2022-06-13 22:13:36.642055
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    buffer = BufferedPrettyStream(msg=None)
    assert next(buffer.iter_body()) == None

# Generated at 2022-06-13 22:13:43.007401
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.client import JSON_ACCEPT, CONTENT_TYPE_JSON, JSON_SORT_KEYS
    from httpie.core import main
    from httpie.downloads import Downloader
    from httpie.plugins.builtin import HTTPBasicAuth

# Generated at 2022-06-13 22:13:54.181947
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers=(
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/plain\r\n'
        'Connection: keep-alive\r\n'
        'Transfer-Encoding: chunked\r\n'
        '\r\n'
    ))
    expected = b'HTTP/1.1 200 OK\r\n' \
               b'Content-Type: text/plain\r\n' \
               b'Connection: keep-alive\r\n' \
               b'Transfer-Encoding: chunked'
    output_encoding = 'utf8'

# Generated at 2022-06-13 22:14:06.850056
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # prepare a msg object
    msg = HTTPMessage()
    msg.body = b'line1\nline2\nline3\nline4'
    msg.headers = 'Content-Type: text/plain'
    msg.encoding = 'utf-8'

    # make the BufferedPrettyStream class
    fmt = Formatting()
    fmt.localfile = False
    fmt.body_indent = 0
    fmt.body_width = -1
    fmt.default_options = False
    fmt.minimal = False
    fmt.prettify = True
    fmt.style = 'default'
    fmt.style_defs = 'httpie.style'
    fmt.verbose = False
    fmt.headers_style = 'default'
    fmt.format = 'colors'
    fmt.indent = 4


# Generated at 2022-06-13 22:14:19.765726
# Unit test for method iter_body of class PrettyStream

# Generated at 2022-06-13 22:14:23.960919
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    def convert(string):
        return string.swapcase()
    # body = b'abc123'
    body = 'abc123'
    # assert body.decode('utf-8') == 'abc123'
    assert body == 'abc123'
    assert BufferedPrettyStream(body=body, with_body=True, with_headers=False, on_body_chunk_downloaded=convert).iter_body() == ['ABC123']

# Generated at 2022-06-13 22:14:31.176261
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    json_data = b'{"result":"success"}'
    data = json.loads(json_data)
    json_data = json.dumps(data, ensure_ascii=False)
    msg = HTTPMessage(None, None, None, json_data)
    msg_stream = EncodedStream(msg)
    mime, body = msg_stream.conversion.get_converter(msg.content_type.split(';')[0]).convert(json_data)
    print(mime)
    print(body)

test_EncodedStream()

# def main(argv=None):
#     # json_data = b'{"result":"success"}'
#     # data = json.loads(json_data)
#     # json_data = json.dumps(data, ensure_ascii

# Generated at 2022-06-13 22:14:42.295936
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import io
    import os

    # Get the absolute path of the file
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../requests/tests/data/unicode_fixture.txt')
    f = io.open(filename, 'rb')
    stream_body = f.read()
    f.close()

    from httpie.models import Request
    msg = Request()
    msg.body = stream_body

    stream = EncodedStream(msg, with_body=True)

    # read the file again to get its content
    f = io.open(filename, 'rb')
    file_content = f.read()
    f.close()

    print(file_content.decode('utf8'))

    print("------------------------------")

    # print

# Generated at 2022-06-13 22:14:54.547362
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage(
        url='https://httpbin.org/stream/20',
        headers={'Content-Type': 'application/json; charset=utf-8'}
    )

    def mock_iter_body(self, chunk_size) -> Iterable[bytes]:
        body = bytearray(chunk_size)
        for i in range(20):
            body[i] = 48 + i
        yield body

    msg.iter_body = types.MethodType(mock_iter_body, msg)

    prettified_body = BufferedPrettyStream(msg).iter_body().__next__()

    expected_body = "[0123456789abcdefghijklmnopqrstuvwxyz]\n"

    assert expected_body == prettified_body.decode('utf-8')

# Generated at 2022-06-13 22:15:12.353118
# Unit test for method iter_body of class PrettyStream

# Generated at 2022-06-13 22:15:25.416036
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    import os, random, tempfile
    from httpie.models import HTTPRequest

    tmp_path = None
    tmp_file = None

# Generated at 2022-06-13 22:15:31.252405
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    print('Testing method __iter__ of class BaseStream')
    headers = HTTPMessage(headers={'Content-Type': 'application/json'}, encoding='utf8')
    body = '{"test": "test"}'
    headers.set_decoded_body(body)
    stream = EncodedStream(msg=headers)
    assert list(stream) == [b'\n', BINARY_SUPPRESSED_NOTICE]


# Generated at 2022-06-13 22:15:32.494863
# Unit test for constructor of class RawStream
def test_RawStream():
    assert RawStream


# Generated at 2022-06-13 22:15:37.930439
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(
        'HTTP/1.1 200 OK\r\n\r\nBody',
        # Default to utf8 when unsure.
        encoding='utf8',
    )
    print(list(EncodedStream(msg=msg).iter_body()))



# Generated at 2022-06-13 22:15:40.330000
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    assert isinstance(BufferedPrettyStream, PrettyStream)
    assert BufferedPrettyStream.CHUNK_SIZE == 1024 * 10


# Generated at 2022-06-13 22:15:45.775407
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import Response
    from httpie.context import Environment
    s = b'last_\xff_line'
    e = EncodedStream(
        Response(200, [b'Content-Type: text/plain; charset=utf-8'], s),
        env=Environment(),
        with_body=True
    )
    assert [b'last_\ufffd_line'] == list(e.iter_body())

# Generated at 2022-06-13 22:15:55.060985
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    p = PrettyStream(None, None)
    assert p.process_body(b'hello world') == b'hello world\n'
    assert p.process_body(b'hello \xe2\x99\xa5 world') == b'hello \xe2\x99\xa5 world\n'
    assert p.process_body(b'hello \xff world') == b'hello \xff world\n'
    assert p.process_body(b'hello \xb0\xfc\x0f\x00 world') == b'hello \xb0\xfc\x0f\x00 world\n'

# Generated at 2022-06-13 22:16:03.733343
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # Create an object of class BufferedPrettyStream
    msg = BufferedPrettyStream(
        conversion=Conversion(lambda x: ('text/plain', 'Converted')),
        formatting=Formatting(lambda x,y: 'Formatted'),
        msg='Response',
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )
    # Call method iter_body
    msg.iter_body()
    # first chunk of body is binary
    assert body[0] == b'\0'

# Generated at 2022-06-13 22:16:15.347825
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import io
    from httpie.models import Response
    from httpie.core import TESTENV
    msg1 = Response(
        status_line='HTTP/1.1 200 OK',
        headers=[('Content-Type', 'text/plain; charset=utf-8')],
        body=io.BytesIO(b'\x80\xff\xfe\xfd\nA\nB\nC\n'),
    )
    msg2 = Response(
        status_line='HTTP/1.1 200 OK',
        headers=[('Content-Type', 'text/plain; charset=utf-8')],
        body=io.BytesIO(b'A\nB\nC\n'),
    )

# Generated at 2022-06-13 22:16:42.846757
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    class Response:
        def iter_lines(self, chunk_size=1):
            yield b'[\n', b'\n'
            yield b'  {\n', b'\n'
            yield b'    "id": 1,\n', b'\n'
            yield b'    "name": "Leanne Graham",\n', b'\n'
            yield b'    "username": "Bret",\n', b'\n'
            yield b'    "email": "Sincere@april.biz",\n', b'\n'
            yield b'    "address": {\n', b'\n'
            yield b'      "street": "Kulas Light",\n', b'\n'
            yield b'      "suite": "Apt. 556",\n', b'\n'

# Generated at 2022-06-13 22:16:56.411276
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie import ExitStatus
    from httpie.compat import is_py26
    from httpie.downloads import Downloader
    import json
    with JSONStream(ExitStatus.OK, 'UTF-8', False,
                    b'{"a": "foo\\nbar"}', 200, 'OK', {},
                    b'{"a": "foo\\nbar"}') as s:
        p = PrettyStream(s, False, '1.0', False, False,
                         None, Conversion(), Formatting(),
                         None, None, None, None, True)
        assert isinstance(p.process_body(b'{"a": "foo\\nbar"}'), bytes)

# Generated at 2022-06-13 22:17:08.530030
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    class Mock:
        class env:
            stdout_isatty = True
            stdout_encoding = None 
        class msg:
            content_type = 'text/plain'
            encoding = 'utf-8'
            def iter_body(self,chunk_size):
                body = 'test'
                yield body.encode('utf-8')
    class Mock1:
        class conversion:
            class get_converter:
                @staticmethod
                def convert(self,body):
                    return body
        class formatting:
            @staticmethod
            def format_body(content=None,mime=None):
                return content
    Mock.conversion = Mock1.conversion()
    Mock.formatting = Mock1.formatting()
    MockObj = Mock()

# Generated at 2022-06-13 22:17:15.378575
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage("response")
    msg.encoding = "UTF-8"
    msg.content_type = "text/json"
    msg.raw = b''
    msg.body = "hello world"
    msg.headers['Content-Type'] = 'text/html'
    es = EncodedStream(msg)

    expected = [[b"hello world\r\n"]]
    actual = [[b for b in es.iter_body()]]
    print(expected == actual)



# Generated at 2022-06-13 22:17:26.545063
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import unittest
    import json
    from httpie.models import JSONDict
    from httpie.output.streams import BufferedPrettyStream

    class TestBufferedPrettyStream(unittest.TestCase):

        def test_BufferedPrettyStream(self):
            response = HTTPMessage(
                headers=JSONDict(
                    headers={
                        'content-type': 'application/json',
                        'content-length': 20,
                    }
                ),
                body=b'{"a":"b"}'
            )

            pretty_stream = BufferedPrettyStream(
                msg=response,
                with_headers=True,
                with_body=True
            )


# Generated at 2022-06-13 22:17:32.525528
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print('Testing EncodedStream constructor...')
    msg = HTTPMessage()
    msg.encoding= 'utf8'
    msg.headers='headers'
    with_headers= True
    with_body= True
    on_body_chunk_downloaded= None
    est = EncodedStream(msg=msg, with_headers=with_headers, with_body=with_body, on_body_chunk_downloaded=on_body_chunk_downloaded)
    print('EncodedStream constructor test passed.')
    return True


# Generated at 2022-06-13 22:17:33.193081
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    pass

# Generated at 2022-06-13 22:17:46.857366
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    http_message = HTTPMessage()

# Generated at 2022-06-13 22:17:55.121161
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.output.streams import PrettyStream
    from httpie.models import HTTPResponse
    from httpie.context import Environment
    from httpie.output.processing import ContentTypeConversion, Formatting
    content = b'\x80\x81\x82\x83'

    conv = ContentTypeConversion()
    env = Environment()
    form = Formatting()

# Generated at 2022-06-13 22:18:04.639083
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    """
    这个测试案例将通过迭代一个空 json 对象, 来观察经过处理后的输出是否正确
    """
    data = "{\n}\n"
    data = data.encode("utf-8")

    msg = HTTPMessage("text/plain", encoding="utf-8", body=data)
    stream = EncodedStream(msg)

    output = ''.join([x.decode("utf-8") for x in stream.iter_body()])
    assert output == data.decode("utf-8")


# Generated at 2022-06-13 22:18:49.186319
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.input import ParseError
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output import get_content_stream

    # Test iter_body of class PrettyStream
    pretty_stream = get_content_stream(
        HTTPResponse(
            headers=b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n',
            body='{"hello": "world"}',
        ),
        # TODO: test also with --style=colorful,
        # once the colorful style is implemented.
        # env=Environment(colors=False),
    )
    assert pretty_stream.iter_body().__next__().decode() == '{\n    "hello": "world"\n}\n'

    # Test iter_body of class PrettyStream when

# Generated at 2022-06-13 22:18:59.040885
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import json
    class FakeMsg:
        encoding = 'utf8'
        def iter_lines(self, size):
            text = b'{"a": 1}\n{"b": 2}\n'
            lines = [line+b'\n' for line in text.splitlines()]
            for line in lines:
                yield line, b'\n'
    s = EncodedStream(msg=FakeMsg())
    result = ''
    for chunk in s.iter_body():
        result += chunk.decode()
    expected = text.decode()
    assert result == expected

# Generated at 2022-06-13 22:19:00.475042
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    assert None!=EncodedStream


# Generated at 2022-06-13 22:19:15.844129
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import io
    import os
    import sys
    import unittest
    from httpie.core import ExitStatus

    from httpie import __version__
    from httpie.core import main
    from httpie.testing import CLITest, http
    from httpie.input import SEP_CREDENTIALS
    from httpie.compat import str


    class TestPrettyResponse(CLITest):

        def test_headers_omitted(self):
            r = http('--pretty=none', '--print=h', 'GET', httpbin.url + '/headers')
            self.assertNotIn('GET /headers', r)
            self.assertIn('Accept: */*', r)


# Generated at 2022-06-13 22:19:26.135271
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    CHUNK_SIZE = 1

    def test_iter_body(self) -> Iterable[bytes]:
        for line, lf in self.msg.iter_lines(CHUNK_SIZE):
            if b'\0' in line:
                raise BinarySuppressedError()
            yield line.decode(self.msg.encoding) \
                      .encode(self.output_encoding, 'replace') + lf
    EncodedStream.iter_body = test_iter_body
    EncodedStream.CHUNK_SIZE = CHUNK_SIZE
    test_msg = HTTPMessage()
    test_msg.encoding = 'utf-8'
    test_msg.body = 'hello world!'
    # CHUNK_SIZE = 1
    stream = EncodedStream(msg=test_msg)

# Generated at 2022-06-13 22:19:37.449739
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # test case 1. dct with valid info
    dct = {'Content-Length': '15', 'Content-Type': 'text/html', 'Cookie': 'SID=31d4d96e407aad42', 'Host': 'httpbin.org',
           'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    headers = httpie.models.Headers(dct)
    msg = httpie.models.HTTPMessage(headers=headers, encoding='utf8')
    pretty_stream = PrettyStream(msg, with_headers=True, with_body=True)
    # test case 1.1 with_headers and with_body both True
    with_headers = True
   

# Generated at 2022-06-13 22:19:45.486291
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    env = Environment()
    test_msg = HTTPMessage()
    test_msg.headers['Content-Type'] = 'text/json; charset=utf-8'
    test_msg.headers['Content-Length'] = '10'
    test_msg.headers['Server'] = 'nginx'
    conversion = Conversion()
    formatting = Formatting()
    p = PrettyStream(test_msg, env=env, conversion=conversion, formatting=formatting)
    assert p.get_headers() == b''


# Generated at 2022-06-13 22:19:49.329449
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    try:
        BufferedPrettyStream('','','','','','','','','','','','')
    except TypeError as e:
        if type(e) == TypeError:
            pass
        else:
            raise e


# Generated at 2022-06-13 22:19:54.259903
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    headers = {
        'Content-Type': 'application/json'
    }
    msg = HTTPMessage(200, headers=headers, body=b'\x80')
    stream = BufferedPrettyStream(conversion=Conversion(), formatting=Formatting(), msg=msg)
    assert b'\x80' in next(iter(stream.iter_body()))

# Generated at 2022-06-13 22:20:05.626122
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # Arrange
    msg = HTTPMessage(response=True)
    msg.headers.add('foo', 'bar', False)
    msg.headers.add('foo', 'baz', True)
    msg.headers.add('foo1', 'baz1', True)
    formatting = Formatting(pretty=True)
    conversion = Conversion('utf-8')
    # Act
    stream = PrettyStream(msg=msg, with_headers=True, with_body=True, conversion=conversion, formatting=formatting)
    res = stream.get_headers().decode()
    # Assert
    assert res == 'foo: bar, baz\r\nfoo1: baz1\r\n'


# Generated at 2022-06-13 22:21:17.458983
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    raw_stream = RawStream(msg="./tests/data/common/headers.json")
    assert raw_stream.iter_body() is not None

# Generated at 2022-06-13 22:21:23.678774
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    ms = HTTPMessage(headers=b'Content-Type: application/json', body=b'{"account": {"account_id": "12345", "balance": 0.0, "currency": "GBP"}}')
    pms = PrettyStream(msg=ms, with_body=True)
    body = pms.iter_body()
    assert b'{' in bytes(body.__next__())
    assert b'}' in bytes(body.__next__())

# Generated at 2022-06-13 22:21:27.067359
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.models import HTTPMessage
    raw_stream = RawStream(HTTPMessage())
    result = raw_stream.iter_body()
    assert(next(result) == b'')


# Generated at 2022-06-13 22:21:32.807000
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(headers={"transfer-encoding": "chunked"},
                      encoding="utf8",
                      body=b'\x91H\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xba\x86\x94\n')
    assert (
        bytearray(EncodedStream(msg).iter_body()) ==
        b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xba\x86\n'
    )

# Generated at 2022-06-13 22:21:36.844204
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    request = HTTPMessage()
    request.body = 'test-body'
    request.headers = 'test-headers'
    stream = RawStream(request)
    assert b'test-body' == b''.join(stream.iter_body())



# Generated at 2022-06-13 22:21:41.276557
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.output.streams import PrettyStream
    from httpie.models import Headers
    expectedheaders = 'HTTP/1.0 200 OK\r\nHello: World'
    headers = Headers(expectedheaders)
    expectedoutput = expectedheaders + '\n'
    stream = PrettyStream(
        msg = headers
    )
    assert stream.get_headers() == expectedoutput.encode('utf8')


# Generated at 2022-06-13 22:21:51.109558
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPResponse
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.processing import Formatter, Converter
    from httpie.utils import get_binary_stream
    from httpie.utils import get_binary_stream
    import StringIO
    import sys

    stdout = sys.stdout

    # Unit test for case all is binary data

# Generated at 2022-06-13 22:21:53.459299
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    stream = PrettyStream(msg = HTTPMessage(headers='test_header'),with_headers=True)
    assert stream.get_headers() == b'\nHTTP/1.1 200 OK\nContent-Type: application/json'

# Generated at 2022-06-13 22:22:06.764813
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage('GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    msg.http_version = b'HTTP/1.1'
    msg.headers = 'Host: example.com'
    msg.body = b'{"msg":"hi"}'
    env = Environment()
    conversion = Conversion()
    formatting = Formatting()
    pretty = PrettyStream(msg=msg, env=env, conversion=conversion, formatting=formatting)
    assert pretty.get_headers() == b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
    assert pretty.iter_body() == [b'{\n    "msg": "hi"\n}']
    assert pretty.formatting == formatting
    assert pretty.conversion

# Generated at 2022-06-13 22:22:15.124025
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPResponse
    stream = BufferedPrettyStream(
        msg=HTTPResponse.from_url(
            url='http://google.com',
            content_type='application/json',
            headers={'content-type': 'application/json'},
            json={'foo': 'bar'},
            ),
        conversion=Conversion(),
        formatting=Formatting(),
        )
    assert stream.iter_body() == b'{\n    "foo": "bar"\n}\n'
    # Check that the msg is not modified
    assert stream.msg.json == {'foo': 'bar'}
