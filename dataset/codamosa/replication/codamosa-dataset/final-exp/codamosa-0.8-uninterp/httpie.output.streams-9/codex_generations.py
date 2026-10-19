

# Generated at 2022-06-13 22:12:34.471227
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import json
    # test1: body is binary, will raise exception
    start = True
    def iter_lines_test1():
        nonlocal start
        if start:
            start = False
            yield b"\x9d\xeb\x96\xff", b"\r\n"
            yield b"\x98\x9d\xff\xdd", b"\r\n"
            yield b"\x00\x00\x00\xff", b""
        else:
            raise StopIteration

# Generated at 2022-06-13 22:12:39.488458
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage()

    def iter_body():
        yield b'\0'

    msg.iter_lines = iter_body
    msg_iter = PrettyStream(msg)
    with pytest.raises(BinarySuppressedError):
        for chunk in msg_iter.iter_body():
            pass

# Generated at 2022-06-13 22:12:49.409220
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    """
    Test for the constructor of class BufferedPrettyStream
    """
    resp = HTTPRequestResponse(b'HTTP/1.1 200 OK\r\nContent-Length: 5\r\n\r\nhello')
    bps = BufferedPrettyStream(resp.response, conversion=Conversion(),
                               formatting=Formatting(), with_headers=True, with_body=True)
    assert bps.msg == resp.response
    assert bps.with_headers == True
    assert bps.with_body == True
    assert bps.on_body_chunk_downloaded == None

    # Assert an exception if one of the key word arguments is missing

# Generated at 2022-06-13 22:12:55.773777
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    bps = BufferedPrettyStream("msg", "with_headers", "with_body", "on_body_chunk_downloaded")
    assert(bps.chunk_size == 1024 * 10)
    assert(bps.msg == "msg")
    assert(bps.with_headers == "with_headers")
    assert(bps.with_body == "with_body")
    assert(bps.on_body_chunk_downloaded == "on_body_chunk_downloaded")



# Generated at 2022-06-13 22:13:02.549023
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    CHUNK_SIZE = 1024 * 10
    chunk = b'\u4f60\u597d'
    print(type(chunk))
    chunk = chunk.decode(self.msg.encoding, 'replace')
    chunk = self.formatting.format_body(content=chunk, mime=self.mime)
    return chunk.encode(self.output_encoding, 'replace')

# Generated at 2022-06-13 22:13:13.389401
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import subprocess
    from contextlib import redirect_stdout
    from httpie.output.streams import BufferedPrettyStream
    from httpie import output
    from io import StringIO
    # https://github.com/jakubroztocil/httpie/issues/1101
    URL = 'https://raw.github.com/jakubroztocil/httpie/master/httpie/compat.py'

    session = requests.Session()
    response = session.get(URL)
    env = Environment()
    stream = BufferedPrettyStream(
        response,
        conversion=output.Conversion(),
        formatting=output.Formatting(),
        env=env
    )


# Generated at 2022-06-13 22:13:22.090170
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf8\r\n\r\nfoo')
    env = Environment(stdout_isatty=True, stdout_encoding='utf8')
    fs = PrettyStream(msg, True, True, None, None, Conversion(), Formatting(env), env)
    assert fs.get_headers() == b'Content-Type: text/plain; charset=utf8\n'

# Generated at 2022-06-13 22:13:35.728732
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # Test request with a body
    msg = HTTPMessage(
        headers=b'Content-Type: application/json\r\n',
        body=b'{'
    )
    bufferedPrettyStream = BufferedPrettyStream(
        msg=msg,
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )
    result = [x for x in bufferedPrettyStream.iter_body()]
    assert result == ['{\n']
    # Test request with no body, but header
    msg = HTTPMessage(
        headers=b'Content-Type: application/json\r\n',
        body=b''
    )

# Generated at 2022-06-13 22:13:43.983166
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from pprint import pprint
    from httpie.models import Response
    from httpie.output.streams import RawStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.context import Environment
    from httpie import ExitStatus

    from httpie.compat import urlopen
    from httpie.models import HTTPResponse
    from httpie.utils import subtests

    URL = 'https://httpbin.org'

    args = FakeArgs()

    env = Environment()
    env.config['output']['stream'] = True
    env.config['output']['pretty'] = True
    env.config['output']['stream_chunk_size'] = 1024 * 4
    env.config['output']['download_insecure'] = False


# Generated at 2022-06-13 22:13:51.981321
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    #arrange
    body_chunks = [b'C',b'\x8a', b'\r\n\r\n', b'T', b'\0', b'\x8a', b'\r\n\r\n']
    stream = BufferedPrettyStream(None,False,True,None)
    stream.msg = object
    stream.msg.iter_body = lambda: body_chunks
    #act
    actual = list(stream.iter_body())
    #assert
    assert actual == []


# Generated at 2022-06-13 22:14:08.007700
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage()
    stream = RawStream(msg)
    chunks = list(stream.iter_body())



# Generated at 2022-06-13 22:14:20.098401
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import Response
    from httpie.output.streams import PrettyStream
    from httpie.output.formatters.utils import get_response_formatter
    import json


# Generated at 2022-06-13 22:14:27.314850
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    " iter_body of class EncodedStream"
    response = HTTPMessage(headers={
        'Content-Type': 'text/html; charset=utf-8'
    }, body=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8').encode('utf-8'))
    stream = EncodedStream(response)
    result = next(stream.iter_body())
    expected = b'\xe4\xb8\xad\xe6\x96\x87'
    assert result == expected



# Generated at 2022-06-13 22:14:36.333604
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    test_msg = HTTPMessage()
    test_msg.headers = """GET / HTTP/1.1
Host: www.google.com
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Request Method: GET
Status Code: 200
Remote Address: 172.217.161.67:443
Referrer Policy: no-referrer-when-downgrade
"""
    test_msg.encoding = input()
    output_encoding = 'utf-8'
    es = EncodedStream(test_msg, Environment(), with_headers=True,
        with_body=True, on_body_chunk_downloaded=None)
    assert es.output_encoding == output_encoding


# Generated at 2022-06-13 22:14:44.226657
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    p = PrettyStream(None,None,None)
    assert p.process_body(b'1') == b'1'
    assert p.process_body(b'1\n') == b'1\n'
    assert p.process_body(b'1\r\n') == b'1\r\n'
    assert p.process_body(b'1\r\n\r\n') == b'1\r\n\r\n'
    assert p.process_body(b'1\r\n\r\n1\r\n') == b'1\r\n\r\n1\r\n'

# Generated at 2022-06-13 22:14:46.326164
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    result = EncodedStream()
    assert result is not None


# Generated at 2022-06-13 22:14:56.915203
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    test_msg = {}
    test_msg['headers'] = {"content-type": "application/json", "test-header": "test-value"}
    test_msg['encoding'] = "utf-8"
    test_msg['iter_body'] = lambda chunk_size: iter([b'{"test": "chunk"}\n'])

    test_conversion = Conversion()
    test_conversion.add_converter("application/json", "application/json")

    test_formatting = Formatting()
    test_formatting.add_formatter("application/json", "application/json")

    response = BufferedPrettyStream(Conversion(), Formatting(), msg=test_msg, with_headers=True, with_body=True)


# Generated at 2022-06-13 22:15:07.559329
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    chunck_size = 10
    class Response(object):
        def __init__(self):
            self.body = [b'abc',b'def',b'ghi']
            self.test_body = [b'abcdefghi']
        def iter_body(self,chunk_size):
            for b in self.body:
                yield b
    r = Response()
    msg = HTTPMessage(None,r)
    raw = RawStream(msg,chunk_size = chunck_size)
    body = []
    for chunk in raw.iter_body():
        body.append(chunk)
    assert body == r.test_body


# Generated at 2022-06-13 22:15:13.495753
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    msg = HTTPMessage()
    stream = BaseStream(msg)
    msg.headers = 'Content-Type: application/json'
    msg.body = '{"test": "case"}'
    msg.encoding = 'utf-8'
    body = ''
    for chunk in stream:
        body = body + chunk.decode('utf-8')
    assert body == 'Content-Type: application/json\r\n\r\n{"test": "case"}'



# Generated at 2022-06-13 22:15:26.145125
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():

    class DummyHTTPMessage():
        # Dummy HTTPMessage to satisfy the constructor of PrettyStream
        def __init__(self):
            self.encoding = 'utf-8'
            self.headers = 'headers'
            self.content_type = 'content_type'
        def iter_lines(self, num):
            return iter([])

    class DummyFormatting:
        # Dummy Formatting to satisfy the constructor of PrettyStream
        def format_headers(self, headers):
            return 'headers'
        def format_body(self, content, mime):
            return 'body'

    class DummyConversion:
        # Dummy Conversion to satisfy the constructor of PrettyStream
        def get_converter(self, mime):
            return DummyConverter()


# Generated at 2022-06-13 22:15:38.229266
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    args = [[1, 2, 3]]
    with pytest.raises(NotImplementedError):
        assert list(BaseStream(*args).__iter__())



# Generated at 2022-06-13 22:15:47.789966
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # Tests that the method iter_body of class PrettyStream
    # will always have yield of type bytes
    def make_msg(text):
        msg = HTTPMessage()
        msg.encoding = 'UTF-8'
        msg.content_type = 'application/json'
        msg.raw = text.encode('utf-8')
        msg.headers = msg.headers.as_str()
        return msg

    env = Environment()
    body_chunk_downloaded = False


# Generated at 2022-06-13 22:15:58.446219
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """TEST for iter_body method in BufferedPrettyStream class

    """
    def iter_content(chunk_size):
        body = b'This is a testing string.\n'
        for i in range(0, len(body), chunk_size):
            yield body[i:i+chunk_size]
    class HTTPMessage:
        def __init__(self, content_type="text/plain", encoding="", iter_body=None):
            self.content_type = content_type
            self.encoding = encoding
            self.iter_body = iter_body
    class Conversion:
        def get_converter(self, mime):
            return None
    class Formatting:
        def format_body(self, content, mime):
            return content.replace('\n', '\r\n')

# Generated at 2022-06-13 22:16:05.047284
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage(
        body=b'{"id":12345}',
        headers=[('Content-Type', 'application/json')],
    )
    stream = PrettyStream(
        msg=msg,
        conversion=Conversion(),
        formatting=Formatting(),
    )
    assert list(stream.iter_body()) == [b'{\n    "id": 12345\n}']

# Generated at 2022-06-13 22:16:15.945692
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import HTTPRequest

    req_info = {
        'method': 'GET',
        'url': 'https://api.github.com/events',
        'headers': '',
        'body': '{"hello": "world"}'
    }

    req = HTTPRequest(**req_info)
    req.headers.update({
        'Content-Type': 'application/json',
        'Content-Length': len(req.body),
    })

    req.parse_headers()
    req.parse_content_type()
    req.parse_body()

    stream = EncodedStream(msg=req, with_headers=True, with_body=True)


# Generated at 2022-06-13 22:16:28.601947
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers={"test": "test"})
    headers = PrettyStream(msg).get_headers()

    assert headers == b'test: test\n'


# Generated at 2022-06-13 22:16:40.340520
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import json
    from httpie.compat import bytes, str

    msg = HTTPMessage()

    class MockStream(BaseStream):
        def __init__(self, *_, **kwargs):
            super().__init__(*_, **kwargs)
            # set some non-default values for the API call
            self.with_headers = self.with_body = True

        def get_headers(self):
            return bytes(
                json.dumps(dict(msg.headers)),
                encoding=msg.encoding
            )

        def iter_body(self):
            yield bytes('This is a test message body', encoding=msg.encoding)

    # test iterating over raw output stream
    raw_stream = RawStream(msg)

# Generated at 2022-06-13 22:16:41.517859
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    pass

# Generated at 2022-06-13 22:16:54.967033
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.output.formatters.json import JSONFormatter
    from httpie.output.formatters.headers import HeadersFormatter
    from httpie.plugins import plugin_manager
    from httpie.compat import urlopen
    from httpie.models import Response
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output import get_response_stream
    from httpie.plugins.builtin import HTMLFormatter
    from httpie.plugins import FormatterPlugin
    import json
    import requests

    def test_get_response_stream():
        mime = 'application/json'
        headers = Headers([('Content-Type', mime),
                           ('Content-Length', '14')])
        # body = b'{"success": true}'

# Generated at 2022-06-13 22:17:07.851773
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import json
    import textwrap
    class PrettyStream(PrettyStream):
        def get_headers(self):
            return b''
    with Environment() as env:
        format_body = PrettyStream(None, Formatting(), env=env).formatting.format_body
        # json
        assert format_body(json.dumps({'key': 'value'}), 'application/json') == textwrap.dedent(
            """
            {
                "key": "value"
            }
            """
        )
        # json pretty
        assert format_body(json.dumps({'key': 'value'}, indent=2), 'application/json') == textwrap.dedent(
            """
            {
              "key": "value"
            }
            """
        )
        # xml

# Generated at 2022-06-13 22:17:34.057971
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # text is a string
    test_text = 'this is a test'
    converter = None
    # 'html' here is simply a string, not a mime
    mime = 'html'
    formatting = Formatting()
    conversion = Conversion()
    stream = PrettyStream(
        msg = Mock(),
        env = Mock(),
        conversion = conversion,
        formatting = formatting,
        with_headers = True,
        with_body = True,
    )

    chunk_processed = stream.process_body(test_text)

    # chunk_processed should be equal to 'this is a test'
    #    formatted to HTML
    #    and then encoded to utf8
    assert chunk_processed == 'this is a test'.encode('utf8')

# Generated at 2022-06-13 22:17:35.484816
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    pass


# Generated at 2022-06-13 22:17:42.142092
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    http_response = EncodedStream(msg='HTTP/1.1 200\r\nabc')
    assert 'abc' == http_response.msg.status
    result = ''
    for chunk in http_response.iter_body():
        result = result + chunk.decode()
    assert 'HTTP/1.1 200\r\nabc' == result


# Generated at 2022-06-13 22:17:50.060706
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import httpie
    filename='test_BufferedPrettyStream_iter_body.json'
    content = {'key': 'value'}
    http_response = httpie.Response(filename, 'utf-8', 200)
    http_response.headers.add(httpie.headers.ContentTypeHeader('application/json'))
    http_response.add_body(content, 'utf-8')
    stream = BufferedPrettyStream(
        http_response, conversion=None, formatting=None,
        with_headers=False, with_body=True, on_body_chunk_downloaded=None)
    for chunk in stream.iter_body():
        print(chunk)


# Generated at 2022-06-13 22:17:54.621433
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.output.streams import RawStream

    rs = RawStream(msg=None, with_headers=None, with_body=None)
    assert_equal(list(rs.__iter__()), [])



# Generated at 2022-06-13 22:18:02.454697
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.input import DummyResponse
    msg = DummyResponse(headers=dict(
        Content_Type='application/xml;charset=UTF-8',
        Content_Length=65535,
    ))
    msg.body = b'a'
    msg._encoding = 'UTF-8'
    stream = BufferedPrettyStream(
        msg=msg, with_headers=False, with_body=True,
    )
    body = b"".join(stream.iter_body())
    assert body == b'a'


# Generated at 2022-06-13 22:18:04.841074
# Unit test for constructor of class RawStream
def test_RawStream():
    assert issubclass(RawStream, BaseStream)


# Generated at 2022-06-13 22:18:15.475415
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    format_body = MagicMock()
    conversion = MagicMock()
    conversion.get_converter.return_value = None
    formatting = MagicMock()
    formatting.format_headers.return_value = '2'
    formatting.format_body.return_value = '4'
    env = MagicMock()
    env.stdout.encoding = '5'
    msg = MagicMock()
    msg.headers = '1'
    msg.iter_body = MagicMock(return_value = ['3'])
    msg.content_type = '6'
    msg.encoding = '7'
    pStream = PrettyStream(conversion, formatting, msg, with_headers=True, with_body=True)
    assert pStream.with_headers == True
    assert pStream.with_body == True


# Generated at 2022-06-13 22:18:21.274992
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    #Arrange
    msg = HTTPMessage()
    msg.encoding = 'utf-8'
    msg.content_type = 'text/html; charset=utf-8'
    body = b'{"test": "test"}'
    msg.iter_body = lambda x: body
    #Act
    stream = BufferedPrettyStream(msg)
    #Assert
    assert stream.iter_body() == body


# Generated at 2022-06-13 22:18:32.589213
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    env = Environment()
    # Make conversion and formatting objects with different headers
    # for the sake of testing
    env.stdout_isatty = True
    env.stdout_encoding = 'utf8'
    headers = {
        '3D': '3D',
        'true': 'true',
        'false': 'false',
        'name': 'value',
        'name2': 'value2',
        'name3': 'value3',
        'name4': 'value4',
        'name5': 'value5',
        'name6': 'value6',
        'name7': 'value7',
        'name8': 'value8',
        'name9': 'value9',
        'name10': 'value10',
    }

# Generated at 2022-06-13 22:19:19.733548
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # Setup
    conversion = Conversion()
    formatting = Formatting()
    msg = HTTPMessage(
        headers='content-type: application/json',
        body='{ "foo": 1, "bar": "baz" }',
        encoding='utf8')
    pretty_stream = PrettyStream(
        msg=msg,
        conversion=conversion,
        formatting=formatting,
        with_headers=True,
        with_body=True
    )
    # Exercise
    output = ''.join(pretty_stream)
    assert output == 'content-type: application/json\r\n\r\n' \
                     '{\n    "foo": 1,\n    "bar": "baz"\n}\n'

# Generated at 2022-06-13 22:19:27.446012
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # test a binary file
    body_content=b'\0'
    msg = HTTPMessage(encoding='utf8', headers={}, content=body_content)
    stream = PrettyStream(msg, with_headers=False, with_body=True)
    #assert BinarySuppressedError in list(stream.iter_body())
    assert BinarySuppressedError.message in list(stream.iter_body())
    # test a plain text file
    body_content=b'this is plain text'
    msg = HTTPMessage(encoding='utf8', headers={}, content=body_content)
    stream = PrettyStream(msg, with_headers=False, with_body=True)
    assert b'this is plain text' in list(stream.iter_body())

# Generated at 2022-06-13 22:19:38.621053
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    def get_BufferedPrettyStream(*args, **kwargs):
        return BufferedPrettyStream(*args, **kwargs)

    class FakeResponse:
        headers = None
        encoding = None
        content_type = None
        content = None
        iter_body_returns = None

        def __init__(self, **kwargs):
            self.__dict__ = kwargs

        def iter_body(self, chunk_size):
            for data in self.iter_body_returns:
                yield data


# Generated at 2022-06-13 22:19:42.537060
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    msg.add_header('key','value')
    msg.add_header('key','value')
    stream = PrettyStream(msg=msg,with_headers=True,with_body=False)
    result = stream.get_headers()
    assert result.decode() == "\r\nkey: value\r\nkey: value\r\n"

# Generated at 2022-06-13 22:19:50.782049
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.models import Response
    from httpie.context import Environment
    import os

    env = Environment()
    # Create a Response with a file path of a file which contains text
    response = Response(env, './test/test_data/test_RawStream/test_iter_body')
    # Initialize a RawStream with the response
    raw_stream = RawStream(
        msg=response,
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )
    # Get the iterator of the message body
    iterator = raw_stream.iter_body()
    # Get the size of the message body
    body_size = os.stat(response.raw.file.name).st_size

    # The iterator should yield the message body with size 1024 * 100

# Generated at 2022-06-13 22:19:55.978009
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage()
    msg.headers = '''HTTP/1.0 200 OK
Content-Type: text/csv;charset=utf-8
Content-Length: 18

''' + '\r\n\r\n' + '''a,b,c
1,2,3
4,5,6'''

    msg.body = msg.headers.encode("utf-8")
    output_message = "".join(
        BufferedPrettyStream(msg, formatting="json", conversion="header").iter_body()).decode("utf-8")

# Generated at 2022-06-13 22:20:07.152466
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import unittest
    import httpie

    class Test(unittest.TestCase):
        def test(self):
            msg = httpie.models.HTTPMessage(
                url='http://httpbin.org/get',
                headers=[
                    ('hello', 'world')
                ],
                body='1+1=2',
                status_code=200,
                reason_phrase='OK',
                http_version='1.1')
            s = BaseStream(msg)
            self.assertEqual(
                list(s.__iter__()),
                [
                    b'hello: world\r\n\r\n\r\n',
                    b'1+1=2'
                ])

    unittest.main()

if __name__ == '__main__':
    test_BaseStream___iter

# Generated at 2022-06-13 22:20:18.073959
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Test assertion of replacing invalid characters in bytes after decoding
    # to string and before encoding to bytes and returning.
    test_string = str(bytes([233, 243, 245, 232, 233, 243]), 'utf-8')
    test_bytes = bytes([233, 243, 245, 232, 233, 243])

    ps = PrettyStream(mime='text/plain',
                      msg=HTTPMessage(content_type='text/plain'),
                      conversion=Conversion(),
                      formatting=Formatting())

    # Test decoding of bytes to string and encoding of string to bytes
    assert ps.process_body(test_bytes) == test_string.encode('utf-8', 'replace')

    # Test encoding of string to bytes
    assert ps.process_body(test_string) == test_string.encode('utf-8', 'replace')

# Generated at 2022-06-13 22:20:29.507657
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import Response
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.cli import close_http_sessions
    from httpie.input import ParseError
    from httpie.output.formatters import JSONFormatter

# Generated at 2022-06-13 22:20:38.957133
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    """
    Test the iter_body method of PrettyStream class as described in
    https://github.com/jakubroztocil/httpie/issues/1186#issuecomment-557465075
    """

    headers = '''
        HTTP/1.1 200 OK
        Content-Type: image/svg+xml
        Content-Length: 27
        Server: test-server
        Connection: Close

    '''

    body = '''
    <svg
    xmlns="http://www.w3.org/2000/svg"
    width="100" height="100">
    <rect fill="#00ff00" width="100" height="100"/>
    </svg>

    '''

    headers_list = headers.strip().split("\n")

# Generated at 2022-06-13 22:22:06.470572
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import pytest
    from httpie.core import main as httpie
    from httpie.context import Environment

    from httpie.models import Response
    from httpie.output.streams import PrettyStream

    response = Response(
        encoding='utf8',
        headers={'Content-Type': 'application/json'},
        status_code=200,
        url='http://www.example.com',
        http_version='1.1',
        reason='OK',
        body='''{
            "list": [
                {
                    "id": 1,
                    "name": "name1"
                },
                {
                    "id": 2,
                    "name": "name2"
                },
                {
                    "id": 3,
                    "name": "name3"
                }
            ]
        }''')



# Generated at 2022-06-13 22:22:12.522405
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    s = EncodedStream(msg=HTTPMessage(body='abc\0de'), with_headers=False)
    assert list(s.iter_body()) == ['abc\0de'], 'EncodedStream_iter_body() failed'
    s = EncodedStream(msg=HTTPMessage(body='abc\0de'), with_headers=False, with_body=False)
    assert list(s.iter_body()) == [], 'EncodedStream_iter_body() without body failed'