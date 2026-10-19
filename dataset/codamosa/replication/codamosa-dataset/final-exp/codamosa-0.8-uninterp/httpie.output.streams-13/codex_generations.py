

# Generated at 2022-06-13 22:12:32.299683
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    response = HTTPMessage()
    response.encoding = 'utf-8'
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf-8'
    stream = EncodedStream(env=env,msg=response)
    assert stream.output_encoding == 'utf-8'


# Generated at 2022-06-13 22:12:38.793156
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # create a test message
    msg = HTTPMessage(
        url='http://example.com',
        headers={'some': 'header'},
        body=b'body\n',
        encoding='utf8'
    )

    # create the stream
    stream = EncodedStream(msg=msg)

    # checks the stream
    assert next(stream.iter_body()) == b'body\n'

# Generated at 2022-06-13 22:12:46.482848
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import HTTPResponse
    from httpie.output.streams import BufferedPrettyStream
    response = HTTPResponse(b'\r\n'.join([
        b'HTTP/1.1 200 OK',
        b'Content-Type: application/json; charset=UTF-8',
        b'',
        b'{"test":"test"}']))
    stream = BufferedPrettyStream(response, conversion=None, formatting=None)
    print(stream.iter_body())

# Generated at 2022-06-13 22:12:50.362692
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage()
    msg._encoding = 'utf8'
    msg._raw = [b'a\n', b'b\n']
    msg._body_line_iterator = iter(msg._raw)
    stream = EncodedStream(msg, with_headers=True, with_body=True)
    assert list(stream.iter_body()) == [b'a\n', b'b\n']

# Generated at 2022-06-13 22:12:58.525929
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    body = "blah\nblah\nblah"
    body_lines = body.splitlines(True)
    for line, lf in BufferedPrettyStream(msg=None, with_headers=False, with_body=True).iter_body():
        assert line == body_lines[0]
        body_lines.pop(0)
    assert body_lines == []

# Generated at 2022-06-13 22:13:00.105246
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    assert PrettyStream(None, None, None, None, None, None).get_headers()

# Generated at 2022-06-13 22:13:09.789641
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    http_response = HTTPMessage(
        headers = b'HTTP/1.1 200 OK\r\n'
                  b'Content-Type: text/plain; charset=utf-8\r\n'
                  b'Date: Fri, 21 Oct 2016 00:12:55 GMT\r\n'
                  b'Expires: Fri, 21 Oct 2016 00:12:55 GMT\r\n'
                  b'Content-Length: 15\r\n'
                  b'Server: ECS (mia/42F2)',
        body = b'Hello Worl ...'
    )
    assert EncodedStream(msg=http_response).msg.headers == http_response.headers


# Generated at 2022-06-13 22:13:22.670337
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    from httpie.models import Message
    from .processing import Conversion, Formatting
    from . import PrettyStream

    headers = 'Content-Type: text/plain; charset=utf8\r\n' \
              'Connection: keep-alive\r\n' \
              'Transfer-Encoding: chunked'

    body = '1\r\n' \
           'Foo\r\n' \
           '2\r\n' \
           'Ba' \
           '2\r\n' \
           'r\r\n' \
           '0\r\n'

    msg = Message()
    msg.headers = headers
    msg.encoding = 'utf8'

# Generated at 2022-06-13 22:13:28.142651
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    actual = False
    i = iter_body(b'abc', b'\xc2\xbb')
    for a in i:
        try:
            next(i)
        except StopIteration:
            actual = True
    assert actual == True


# Generated at 2022-06-13 22:13:34.663000
# Unit test for constructor of class RawStream
def test_RawStream():
    rawStream = RawStream("msg", "withheaders", "withBody", "onBodyChunkDownloaded")
    assert rawStream.msg == "msg"
    assert rawStream.with_headers == "withheaders"
    assert rawStream.with_body == "withBody"
    assert rawStream.on_body_chunk_downloaded == "onBodyChunkDownloaded"


# Generated at 2022-06-13 22:13:47.809519
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    stream = PrettyStream(None, None, HTTPMessage(), with_body=True, with_headers=True)
    for i in stream.iter_body():
        pass

# Generated at 2022-06-13 22:13:55.058026
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Define the response message
    resp = HTTPMessage(
        headers={'Content-Type': 'application/json'},
        body='{}'
    )

    # Create an instance of PrettyStream
    inst = PrettyStream(
        msg=resp,
        # with_headers=with_headers,
        # with_body=with_body,
        # on_body_chunk_downloaded=on_body_chunk_downloaded
    )

    # The method process_body will be tested here
    chunk = '{}'
    result = inst.process_body(chunk)
    assert (result == '{}\n')

# Generated at 2022-06-13 22:14:07.846622
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    print("Start to test PostStream_iter_body()...")
    # Construct a fake message
    f = open("./test/test_cases/fake_msg.txt", 'w')

# Generated at 2022-06-13 22:14:20.539625
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    print(BINARY_SUPPRESSED_NOTICE)
    print(b'\x80')
    # UnicodeEncodeError: 'latin-1' codec can't encode character '\udc80' in position 0: ordinal not in range(256)
    # print(b'\x80'.decode('utf8'))
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
    print(b'\x80'.decode('utf8', 'replace'))

if __name__ == '__main__':
    test_BufferedPrettyStream_iter_body()

# Generated at 2022-06-13 22:14:21.309671
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    assert True

# Generated at 2022-06-13 22:14:23.770947
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage()
    encodestream = PrettyStream(msg=msg)
    assert(encodestream.msg == msg)

# Generated at 2022-06-13 22:14:35.441013
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.core import main
    from httpie.models import HTTPMessage

    # verify BinarySuppressedError
    msg = HTTPMessage(status_code=200, headers={}, body = b'\x00')
    stream = RawStream(msg, with_headers=False, with_body=True)
    output = b''.join(stream)
    assert output == BINARY_SUPPRESSED_NOTICE # verify with_body is True

    # verify binary file
    msg = HTTPMessage(status_code=200, headers={}, body = b'\x00')
    stream = RawStream(msg, with_headers=True, with_body=True)
    output = b''.join(stream)
    assert output == BINARY_SUPPRESSED_NOTICE # verify with_headers is True

    # verify with_body

# Generated at 2022-06-13 22:14:44.041939
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.downloads import Response
    from httpie.models import HTTPMessage
    from io import BytesIO
    from httpie.output.processing import Conversion, Formatting
    from httpie.context import Environment

    import os
    import copy
    import json

    # HTTP headers
    headers_stream = BytesIO(b'''HTTP/1.1 200 OK
    Content-Type: application/json; charset=utf-8
    Content-Length: 70
    Connection: keep-alive
    Keep-Alive: timeout=10
    Server: gunicorn/20.0.4
    Date: Mon, 17 Feb 2020 09:48:05 GMT''')
    # HTTP body
    body_stream = BytesIO(b'''{
    "test": "data"
    }''')
    # Merge headers and body

# Generated at 2022-06-13 22:14:50.762659
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(b'hello', encoding='utf8')
    assert list(RawStream(msg).iter_body()) == [b'hello']
    msg = HTTPMessage(b'hello', encoding='utf8', content_type='text/plain')
    assert list(RawStream(msg, chunk_size=2).iter_body()) == [b'he', b'll', b'o']


# Generated at 2022-06-13 22:14:55.461182
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage(None, b'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\n{"msg": "hello"}\n')
    assert len(list(msg.iter_body(1))) == 9
    stream = PrettyStream(msg, True, True)
    assert len(list(stream.iter_body())) == 11

# Generated at 2022-06-13 22:15:10.668056
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    response = requests.get('https://www.baidu.com/')
    # msg = models.Response(response)
    msg = response
    for i in RawStream(msg).iter_body():
        print(i)
        break


# Generated at 2022-06-13 22:15:23.397933
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # Setup
    from httpie.output.formatters import JSONFormatter
    from httpie.output.streams import PrettyStream
    import json
    import requests

    env = Environment()
    formatting = JSONFormatter(indent=4, sort_keys=True)
    conversion = Conversion(None, None)
    r = requests.get("http://httpbin.org/get")
    stream = PrettyStream(r, env=env, conversion=conversion,
                          formatting=formatting, with_body=False)

    # Exercise
    headers = stream.get_headers()

    # Verify
    assert headers == json.dumps(r.headers.__dict__["_store"], indent=4, sort_keys=True).encode("utf8")
    # Cleanup - none necessary



# Generated at 2022-06-13 22:15:28.638049
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # given
    msg = HTTPMessage(
        body=b'1\n2\n3\n4',
        method='GET',
        url='http://example.com',
        headers={"content-type": "application/json"},
        encoding='utf8',
    )

    # when
    for i, (line, _) in enumerate(EncodedStream(msg).iter_body()):
        assert line == f'{i+1}\n'.encode('utf8')

# Generated at 2022-06-13 22:15:42.029745
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import responses
    import httpie
    import json
    import os
    from httpie.models import Request
    from httpie.output.streams import RawStream
    from httpie.input import ParseError
    from httpie.core import main
    from httpie import ExitStatus
    url = 'http://' + os.environ['HTTPIE_TEST_HOST'] + '/'
    # print(url)
    # TestBase
    req = Request(method='GET', url=url, headers={'h2': 'v2'}, data='d2')
    env = Environment()
    env.stdout_isatty = False
    env.print_body_only = True
    env.stdin_isatty = False
    # prepare for query
    env.stdout_isatty = False
    env.print_

# Generated at 2022-06-13 22:15:54.784374
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    #
    # Test when chunk is str
    #
    pretty_stream = PrettyStream(None, None, None, None, None, None)
    pretty_stream.formatting = Mock()
    pretty_stream.mime = 'text/plain'
    chunk_str = 'chunk_str'
    output_encoding = 'utf-8'
    pretty_stream.output_encoding = output_encoding
    body = Mock()
    pretty_stream.formatting.format_body.return_value = body
    expected = body.encode.return_value
    result = pretty_stream.process_body(chunk_str)
    pretty_stream.formatting.format_body.assert_called_once_with(chunk_str, pretty_stream.mime)

# Generated at 2022-06-13 22:16:06.047225
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import httpie.models as models
    # test for headers without 'Content-Type'

# Generated at 2022-06-13 22:16:14.919685
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    r = requests.get("https://api.github.com/users/hongtao520/repos")
    msg = HTTPMessage(
            r.headers,
            r.status_code,
            r.reason,
            r.encoding,
            r.content,
        )

    raw_stream = RawStream(msg)
    print("msg.iter_body")
    for i in raw_stream.iter_body():
        print(repr(i))
    print("msg.iter_body")


if __name__ == '__main__':
    test_RawStream_iter_body()

# Generated at 2022-06-13 22:16:29.383007
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage(headers=None, body=b"foo\nbar\n")
    stream = PrettyStream(msg=msg, with_headers=False, with_body=True)

    assert list(stream.iter_body()) == [b'foo\n', b'bar\n']

# Generated at 2022-06-13 22:16:35.191746
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import HTTPRequest
    from httpie.output.streams import PrettyStream

    http_request = HTTPRequest('GET', 'http://localhost/')
    stream = PrettyStream(http_request, 'headers')

    assert stream.get_headers() == http_request.headers.encode('utf8')


# Generated at 2022-06-13 22:16:50.635022
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage('utf8', [], b'test')
    es = EncodedStream(msg, with_headers=False)
    assert list(es.iter_body()) == [b'test']

    msg = HTTPMessage('utf8', [], b't\xc3\xa9st')
    es = EncodedStream(msg, with_headers=False)
    assert list(es.iter_body()) == [b't\xc3\xa9st']

    msg = HTTPMessage('utf8', [], b't\xe9st')
    es = EncodedStream(msg, with_headers=False)
    assert list(es.iter_body()) == [b't\xc3\xa9st']

    msg = HTTPMessage('utf8', [], b'\0')
    es = EncodedStream

# Generated at 2022-06-13 22:17:20.876821
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import HTTPMessage
    stream = PrettyStream(HTTPMessage(headers={'content-type': 'application/json'}, body=b'{}\n'))
    lines = list(stream.iter_body())
    assert len(lines) == 2
    assert lines[0].endswith(b'\n')
    assert lines[0].decode(stream.output_encoding) == '{\n'
    assert lines[1].endswith(b'\n')
    assert lines[1].decode(stream.output_encoding) == '}\n'

# Generated at 2022-06-13 22:17:32.677377
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    import requests
    import json
    url = "https://jsonplaceholder.typicode.com/posts"
    req = requests.get(url)
    req_msg = HTTPMessage(method="GET", headers=req.headers, encoding='utf8', body=req.text)
    pretty_stream = BaseStream(msg=req_msg, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    pretty_stream_iter = pretty_stream.__iter__()
    req_msg_body = req_msg.body.encode("utf-8")
    req_msg_str = str(req_msg)
    req_msg_str_split = req_msg_str.split("\n")

# Generated at 2022-06-13 22:17:42.366221
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print('test_EncodedStream')
    msg = HTTPMessage(version='1.1', headers='{}', content_type='JSON', encoding='UTF-8')
    env = Environment(stdout_isatty=False, stdout_encoding='GBK')
    stream = EncodedStream(msg=msg, env=env, with_body=True)
    assert(stream.CHUNK_SIZE == 1)
    assert(stream.get_headers() == '{}')
    assert(stream.iter_body() == None)

# Generated at 2022-06-13 22:17:48.565412
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: text/html; charset=utf-8\r\n'
        b'Content-Length: 5\r\n'
        b'\r\n'
        b'hello'
    )
    result = list(EncodedStream(msg).iter_body())
    assert result == [b'hello']

# Generated at 2022-06-13 22:17:59.136358
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    class mock_msg(object):
        msg = b'HTTP/1.1 302 Moved Temporarily\r\n\r\n'
        encoding ='ascii'
        def iter_lines(self, size):
            yield self.msg, b'\r\n'

    stream = EncodedStream(chunk_size=1, msg=mock_msg(), with_headers=False, with_body=True)
    result = b''
    for chunk in stream.iter_body():
        result += chunk
    print(result)
    assert(result==b'HTTP/1.1 302 Moved Temporarily\r\n\r\n')

# Generated at 2022-06-13 22:18:08.437623
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.compat import is_py26
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    env = Environment()
    msg = HTTPMessage()
    msg.headers = '''{'key':'value'}'''
    msg.body = '''{'id':'1'}'''
    msg.encoding = 'utf-8'
    msg.content_type = 'application/json'
    bps = BufferedPrettyStream(msg=msg, env=env)
    result_str = next(bps.iter_body())
    if is_py26:
        assert result_str == "{'id':'1'}".encode('ascii')
    else:
        assert result_str == "{'id':'1'}".encode('utf-8')

# Generated at 2022-06-13 22:18:19.291628
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from io import BytesIO
    
    # Setup
    body = b'abc\xffdef\nghi\0'
    message = HTTPMessage(headers=b'Content-Type: text/plain',
                          body=BytesIO(body),
                          encoding='utf8')

    stream = EncodedStream(message, with_headers=False, with_body=True)

    # Exercise
    expected_output = b'abc\ufffd\nghi\ufffd\n'
    output = b''.join(stream)

    # Verify
    assert output == expected_output

# Generated at 2022-06-13 22:18:25.846976
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'
    msg = HTTPMessage(headers=headers, body=b'{"foo": "bar"}')
    stream = BufferedPrettyStream(conversion=Conversion(), msg=msg,
                                  env=Environment())
    result = str(stream.iter_body())
    assert 'foo' in result

# Generated at 2022-06-13 22:18:34.138260
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import pytest
    from httpie.models import HTTPResponse
    def mock_iter_lines(self, chunk_size=1):
        yield (b'line1', b'\n')
        yield (b'line2', b'\n')
        yield (b'line3\0', b'\n')
    from unittest.mock import patch
    with patch.object(HTTPResponse, 'iter_lines', mock_iter_lines):
        msg = HTTPResponse(headers=b'', encoding='utf8')
        stream = EncodedStream(msg=msg, with_headers=False, with_body=True)
        result = list(stream.iter_body())
    assert result == [b'line1\n', b'line2\n']

# Generated at 2022-06-13 22:18:44.208151
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    stream = PrettyStream(
        HTTPMessage(
            http_version="1.1",
            status_code="200",
            reason_phrase="OK",
            headers={"Content-Type": "application/json",
                     "Content-Length": "12"},
            body="\u0ca0_\u0ca0"),
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None,
        conversion=Conversion(),
        formatting=Formatting(formats={}, colors={})
    )
    assert b"\u0ca0" not in stream.get_headers()

# Generated at 2022-06-13 22:19:37.771316
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    l = []
    stream = EncodedStream(msg=HTTPMessage(headers={'Content-Type': 'text/html'},
                                           body='a\u8513zzz\u2044zzz\u8513z',
                                           encoding='utf-8'))
    for chunk in stream.iter_body():
        l.append(chunk)
    assert l == [
        b'a\xed\xa0\x9c\xed\xb2\x93\xed\xab\xa0zzz\xe2\x81\x84zzz\xed\xa0\x9c\xed\xb2\x93z'
    ]


# Generated at 2022-06-13 22:19:38.891168
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    print(EncodedStream(msg="test"))

# Generated at 2022-06-13 22:19:44.523171
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # Test instance of PrettyStream with  message
    # with output encoding
    msg = 'message'
    output_encoding = 'output'
    dummy_str = 'dummy'
    conversion, formatted, mime = 'conversion', 'formatted', 'mime'
    pretty_instance = PrettyStream(msg, conversion, formatted, output_encoding, mime)
    # Test with str input
    assert pretty_instance.process_body(msg) == msg.encode()

    # Test with bytes input
    assert pretty_instance.process_body(dummy_str) == dummy_str.encode()

    # Test with str input

    with pytest.raises(AttributeError):
        pretty_instance.process_body(dummy_str)

# Generated at 2022-06-13 22:19:45.492841
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    assert True


# Generated at 2022-06-13 22:19:47.805072
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    stream = PrettyStream({}, {}, None, None, True, True)
    print(stream.get_headers())

# Generated at 2022-06-13 22:19:52.459267
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    res = b''
    def test_func(str):
        res = str

    stream = RawStream(b'HTTP/1.1 200 OK\r\n\r\n', on_body_chunk_downloaded=test_func)
    for str in stream:
        res = str

    assert res == b''


# Generated at 2022-06-13 22:19:59.244520
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.models import Response
    from httpie.output.streams import PrettyStream
    from httpie.context import Environment
    from httpie.output.processing import Conversion
    from httpie.output.formatting import Formatting
    import pprint

    env=Environment()
    conversion=Conversion()
    formatting=Formatting()
    fp=open('test3.txt', 'r')
    response=Response(status_code=200, headers={}, body=fp)

    pretty_line_stream=PrettyStream(msg=response, env=env, conversion=conversion, formatting=formatting)
    pretty_line_stream.msg.headers=pprint.pformat(pretty_line_stream.msg.headers, indent=4).encode('utf8')
    print(pretty_line_stream.msg.headers)

# Generated at 2022-06-13 22:20:06.013897
# Unit test for constructor of class RawStream
def test_RawStream():
    msg = HTTPMessage(headers={'Content-Type':'application/json'}, encoding=None,
                      raw_headers=None, content=b'{"username":"rainy","password":"123456"}')
    raw_stream = RawStream(msg=msg, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    assert raw_stream.chunk_size == 10240



# Generated at 2022-06-13 22:20:09.953251
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(b'Hello World!\n')
    s = RawStream(msg)
    assert list(s.iter_body()) == [b'Hello World!\n']


# Generated at 2022-06-13 22:20:22.694432
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg_str = (
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: text/plain\r\n'
        b'\r\n'
        b'hello, world\r\n'
        b'foo bar\r\n'
    )
    msg = HTTPMessage.parse(msg_str)
    stream = PrettyStream(msg, conversion = None, formatting = None, with_headers = True, with_body = True, on_body_chunk_downloaded = None)
    assert stream.get_headers() == msg_str.decode("utf-8").encode("utf-8")
    assert next(iter(stream)) == msg_str.decode("utf-8").encode("utf-8")

# Generated at 2022-06-13 22:22:05.105585
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    data = (
        b''
        b'HTTP/1.1 200 OK\r\n'
        b'Content-length: 6\r\n'
        b'Content-type: text/plain;charset=utf-8\r\n'
        b'\r\n'
        b'message'
    )
    msg = HTTPMessage()
    msg.parse(data)

    stream = BaseStream(msg=msg)
    result = list(stream)
    assert len(result) == 3
    assert result[0] == data[:29]
    assert result[1] == data[29:31]
    assert result[2] == data[31:38]


# Generated at 2022-06-13 22:22:14.066699
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """
    :return: Success if iter_body returns the expected text
    """
    data = {"name":"Geco","origin":"Montenegro","type":"Python","age":3}
    data_json = json.dumps(data)
    num_iterations = 10
    stream = BufferedPrettyStream(
        msg = HTTPMessage(
            headers=data_json,
            content_type='application/json'),
        with_body=True,
        on_body_chunk_downloaded=None,
        conversion=Conversion(),
        formatting=Formatting()
        )
    for i in range(num_iterations):
        assert next(stream.iter_body()) == data_json, "iter_body is wrong"