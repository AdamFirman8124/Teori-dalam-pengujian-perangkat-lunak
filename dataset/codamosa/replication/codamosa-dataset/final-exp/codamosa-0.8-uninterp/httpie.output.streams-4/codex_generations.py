

# Generated at 2022-06-13 22:12:31.600393
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    class Subclass(BaseStream):
        def __init__(self):
            super().__init__(None, True, True)
            self.msg = HTTPMessage()
        def get_headers(self):
            return self.msg.headers.encode('utf8')
        def iter_body(self):
            return self.msg.iter_body(self.CHUNK_SIZE)

    class TestClass:
        def test_get_headers_method_as_regular_method(self):
            with pytest.raises(AssertionError):
                return Subclass().get_headers()
        def test_headers_as_regular_method(self):
            with pytest.raises(AssertionError):
                return Subclass().headers
        def test_get_headers_method_as_attribute(self):
            Sub

# Generated at 2022-06-13 22:12:32.386083
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    assert 1 == 1

# Generated at 2022-06-13 22:12:45.686059
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import pytest

    from httpie.models import Response

    stream = PrettyStream(
        msg=Response(b'\n'.join([
            b'HTTP/1.1 200 OK',
            b'Content-Type: text/html',
            b'',
            b'<html></html>'
        ])),
        conversion=Conversion(),
        formatting=Formatting(),
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )


# Generated at 2022-06-13 22:12:50.868644
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    env = Environment()
    msg = HTTPMessage()
    with_headers=True
    with_body = True
    on_body_chunk_downloaded = None
    try:
        es = EncodedStream(msg=msg, env=env, with_headers=with_headers,
                           with_body=with_body, on_body_chunk_downloaded=on_body_chunk_downloaded)
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-13 22:13:03.871599
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import httpie
    import json
    # https://github.com/jakubroztocil/httpie/blob/master/tests/sessions/test_headers.py
    packet = httpie.Request(
        method=u'POST',
        url=u'http://httpbin.org/post',
        headers={u'Content-Type': u'application/json'},
        data=json.dumps({u'foo': u'bar'})
    )
    # https://github.com/jakubroztocil/httpie/blob/master/tests/compat/test_pretty.py

# Generated at 2022-06-13 22:13:09.932919
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage('GET / HTTP/1.1\r\nContent-Length: 3\r\n\r\nabc')
    env = Environment()
    assert PrettyStream(msg, env=env).get_headers() == b'Content-Length: 3\r\n'


# Generated at 2022-06-13 22:13:17.824026
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    headers = (
        'Content-Type: text/plain; charset=UTF-8', 
        'Content-Length: 99'
    )
    msg = HTTPMessage(headers=headers, body=b'\0')
    stream = EncodedStream(msg=msg)
    assert next(stream.iter_body()) == ('\x00').encode('utf8')

    headers = (
        'Content-Type: text/plain; charset=ISO-8859-1', 
        'Content-Length: 99'
    )
    msg = HTTPMessage(headers=headers, body=b'\xad')
    stream = EncodedStream(msg=msg)

    # check first character returned by iter_body
    assert next(stream.iter_body()) == ('\ufffd').encode('utf8')

# Generated at 2022-06-13 22:13:26.170889
# Unit test for method iter_body of class EncodedStream

# Generated at 2022-06-13 22:13:38.624587
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg_with_bom = HTTPMessage(headers='''\
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8

''')
    msg_with_bom.body = b'\xef\xbb\xbf' + b'\xc3\xa5\xc3\xb6'
    stream_with_bom = EncodedStream(msg=msg_with_bom, env=Environment(stdout_isatty=True))
    assert [b'\xc3\xa5\xc3\xb6\r\n'] == list(stream_with_bom.iter_body())


# Generated at 2022-06-13 22:13:47.296493
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    body_bytes = '{"test_key": "test_value"}'.encode('utf8')
    msg = HTTPMessage(headers={"Content-Type": "application/json"}, body=body_bytes)
    stream = EncodedStream(msg=msg, with_headers=True, with_body=True)

    body = b''.join(stream.iter_body())
    assert body.decode('utf8') == '{"test_key": "test_value"}'

# Generated at 2022-06-13 22:13:56.573424
# Unit test for constructor of class RawStream
def test_RawStream():
    stream = RawStream(None)
    print("RawStream get_headers()")
    print(stream.get_headers())
    print("RawStream iter_body()")
    print(stream.iter_body())



# Generated at 2022-06-13 22:14:02.767828
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(b"HTTP/1.1 200 OK\nContent-Type: application/json\n\nTest")
    stream = PrettyStream(msg, formatting = Formatting())
    assert stream.get_headers() == b"HTTP/1.1 200 OK\nContent-Type: application/json\n\n"


# Generated at 2022-06-13 22:14:10.916379
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.response.headers import Headers
    from httpie.models import HTTP_SUCCESS

    http_message = HTTPMessage(version=(1,1),
                            status=HTTP_SUCCESS,
                            headers=Headers(
                                content_type='text/plain; charset=utf-8',
                                content_length=len(b'Hi!')),
                            body=b'Hi!')
    pretty_stream = PrettyStream(conversion=Conversion(),
                           formatting=Formatting(),
                           msg=http_message)
    expected = 'Hi!'
    actual = pretty_stream.process_body(http_message.body)
    print(type(actual))
    print(type(expected))
    print(actual)
    print(expected)

    # assert actual == expected


# Unit

# Generated at 2022-06-13 22:14:20.415762
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import HTTPRequest
    env = Environment()
    headers = HTTPRequest(method="DELETE", url="/search?q=foo&q=bar").headers
    p = PrettyStream(msg=headers, env=env, with_body=False, with_headers=True)
    assert p.get_headers() == b'DELETE /search?q=foo&q=bar HTTP/1.1\r\n\r\n'



# Generated at 2022-06-13 22:14:25.550695
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    env = Environment()
    formatting = Formatting()
    conversion = Conversion()
    stream = PrettyStream(env=env, conversion=conversion, formatting=formatting)
    assert stream.process_body(b'ab\0cd') == b'ab?cd'
    assert stream.process_body(u'ab\0cd') == b'ab?cd'

# Generated at 2022-06-13 22:14:28.984220
# Unit test for constructor of class BaseStream
def test_BaseStream():
    from httpie.models import Response
    from httpie.output.streams import BaseStream
    BaseStream(Response(), with_headers=True, with_body=True)

# Generated at 2022-06-13 22:14:41.359187
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import os
    import random
    import string
    import logging
    import pytest
    from httpie.context import Environment
    from httpie.models import ContentType
    from httpie.output.processing import Conversion, Formatting
    logging.basicConfig(level=logging.DEBUG)

    import httpie.output.formatters as formatters
    formatters.register()
    cwd = os.path.abspath(os.path.dirname(__file__))
    env = Environment(colors=False)

    def random_string(size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size)).encode()


# Generated at 2022-06-13 22:14:52.451455
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Function to decode unicode error
    def iterable(s):
        for c in s:
            yield c

    # Function to decode unicode error
    def char_iterable(s):
        for c in s:
            for char in c:
                yield char

    def expectedResults(s):
        for c in s:
            for char in c:
                yield char

    ################################################################################
    #   TEST CASE
    ################################################################################
    #   case 1:
    #       Unicode string
    ################################################################################
    string = '1 2 3 áçèñtø'
    # Create a HTTPMessage
    msg = HTTPMessage(iterable(string), 'utf8')
    # Create a EncodedStream
    encoded_stream = EncodedStream(msg)
    #

# Generated at 2022-06-13 22:15:00.936535
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    b1 = RawStream(
        msg=HTTPMessage(
            headers=b'abc',
            body=b'abcdefg',
            encoding='utf8',
            chunk_size=1,
        ),
        with_headers=True,
        with_body=True,
    )
    assert b1.iter_body() == b'abcdefg'
    b2 = RawStream(
        msg=HTTPMessage(
            headers=b'abc',
            body=b'abcdefg',
            encoding='utf8',
            chunk_size=7,
        ),
        with_headers=True,
        with_body=True,
    )
    assert b2.iter_body() == b'abcdefg'

# Generated at 2022-06-13 22:15:05.030551
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    stream = BufferedPrettyStream(
        with_headers=True, with_body=True, msg=HTTPMessage(), conversion=Conversion(), formatting=Formatting()
    )
    assert stream is not None

# Generated at 2022-06-13 22:15:27.375972
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage()
    # Default arguments
    PrettyStream(msg)
    # Default arguments with conversion
    conversion = Conversion()
    PrettyStream(msg, conversion=conversion)
    # Default arguments with conversion and formatting
    formatting = Formatting()
    PrettyStream(msg, conversion=conversion, formatting=formatting)
    # Default arguments with formatting
    PrettyStream(msg, formatting=formatting)



# Generated at 2022-06-13 22:15:29.496095
# Unit test for constructor of class RawStream
def test_RawStream():
    r = RawStream(None, None, None, None)
    assert r.iter_body() is None

# Generated at 2022-06-13 22:15:42.497194
# Unit test for method get_headers of class PrettyStream

# Generated at 2022-06-13 22:15:48.889097
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    req = HTTPMessage(Method.GET, URL('http://httpbin.org/headers'), Headers([]))
    req.headers = [('key1', 'value1'), ('key2', 'value2')]
    assert PrettyStream(req).get_headers() == b'key1: value1\nkey2: value2\n'


# Generated at 2022-06-13 22:15:56.137399
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.streams import EncodedStream

# Generated at 2022-06-13 22:16:03.262437
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    chunks = [b'\n', b'my line', b'\n', b'1\x00\n']
    for i, chunk in enumerate(EncodedStream(msg=HTTPMessage('', chunks)).iter_body()):
        if i == 1:
            raise DataSuppressedError('Test.')
        print(chunk)
    print('Success.')

if __name__ == '__main__':
    test_EncodedStream_iter_body()

# Generated at 2022-06-13 22:16:15.204793
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import Headers
    from httpie.output.streams import PrettyStream
    from httpie.output.formats.colors import get_lexer
    from pygments.formatters import Terminal256Formatter
    from pygments import highlight
    env = Environment()
    headers = Headers(list({'a': '1', 'b': '2'}.items()))
    pstream = PrettyStream(msg=None, headers=headers, env=env,
                           formatting=Formatting(get_lexer,
                                                 Terminal256Formatter))

    formatted_headers = pstream.get_headers()

    assert 'a'.encode('utf8') in formatted_headers
    assert 'b'.encode('utf8') in formatted_headers
    assert '1'.encode('utf8') in formatted_headers

# Generated at 2022-06-13 22:16:32.719095
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    msg = HTTPMessage()
    msg.headers = 'some headers'
    msg.body = 'some body'

    stream = BaseStream(msg)
    stream.get_headers = lambda: 'some headers'.encode('utf8')
    stream.iter_body = lambda: 'some body'.encode('utf8')
    stream.with_headers = True
    stream.with_body = True
    iterator = stream.__iter__()
    assert isinstance(iterator, Iterable)

    assert next(iterator) == 'some headers'.encode('utf8')
    assert next(iterator) == '\r\n\r\n'.encode('utf8')
    assert next(iterator) == 'some body'.encode('utf8')
    try:
        next(iterator)
    except StopIteration:
        pass

# Generated at 2022-06-13 22:16:35.032698
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    stream = PrettyStream(msg, True, False)
    stream.get_headers()

# Generated at 2022-06-13 22:16:41.644743
# Unit test for constructor of class RawStream
def test_RawStream():
    msg = b"hello world"
    with_headers = True
    with_body = True
    chunk_size = 1024 * 100
    assert RawStream(msg, with_headers=with_headers, with_body=with_body, chunk_size=chunk_size).chunk_size == 102400



# Generated at 2022-06-13 22:17:22.862915
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    message = HTTPMessage()
    headers = message.headers
    headers.set("HTTP/1.1 200 OK")
    headers.set("Content-Type: application/json")
    headers.set("Date: Sun, 17 Jun 2018 15:04:53 GMT")
    headers.set("Expires: -1")
    headers.set("Cache-Control: private, max-age=0")
    headers.set("Content-Encoding: gzip")

    encoded_stream = EncodedStream(msg=message)
    bytes_body = b'{\n  "name": "kevin",\n  "age": 26\n}'

# Generated at 2022-06-13 22:17:31.324934
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import HTTP_200
    msg = HTTP_200(
        body=b'line1\n\nline2\n\nline3\n',
        encoding='utf16'
    )
    expected_body = [
        'line1\r\n\r\n',
        'line2\r\n\r\n',
        'line3\r\n\r\n'
    ]
    stream = EncodedStream(msg, with_headers=False)
    assert list(stream.iter_body()) == list(map(bytes, expected_body))


# Generated at 2022-06-13 22:17:44.953017
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(headers=dict(), encoding="utf8", content_type=None)
    env = Environment()
    env.stdout_encoding = "utf8"
    env.stdout_isatty = True
    e = EncodedStream(msg=msg, env=env, with_headers=True, with_body=True)
    assert e.msg == msg
    assert e.with_headers
    assert e.with_body
    assert not e.on_body_chunk_downloaded
    assert e.output_encoding == "utf8"
    env.stdout_isatty = False
    e = EncodedStream(msg=msg, env=env, with_headers=True, with_body=True)
    assert e.output_encoding == "utf8"

# Generated at 2022-06-13 22:17:52.063063
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    data = 'This is a test.'
    data_bytes = data.encode('utf8')
    data_hex = data_bytes.hex()
    msg = HTTPMessage(data_bytes, headers={'Content-Type': 'text/plain'})
    stream = EncodedStream(msg)
    assert data_bytes == b''.join(stream.iter_body())
    assert data_bytes == b''.join(stream.iter_body())
    assert data_bytes == b''.join(stream.iter_body())
    msg = HTTPMessage(
        data_bytes, headers={'Content-Type': 'text/plain; charset=utf8'})
    stream = EncodedStream(msg)
    assert data_bytes == b''.join(stream.iter_body())

# Generated at 2022-06-13 22:17:58.046478
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    p = PrettyStream(msg=None, conversion=None, formatting=None, with_headers=True)
    p.formatting = Formatting()
    p.msg = HTTPMessage(headers={'Content-Type': 'application/json'})
    assert p.get_headers() == b'Content-Type: application/json\r\n'



# Generated at 2022-06-13 22:18:07.068324
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
  # Test for headers and body
  msg = ('HTTP/1.1 200 OK\r\n'
         'Content-Type: text/plain; charset=utf-8\r\n'
         'Transfer-Encoding: chunked\r\n'
         '\r\n'
         '17\r\n'
         'I am a plain text response\r\n'
         '0\r\n\r\n')
  msg = HTTPMessage.from_http(msg)
  stream = EncodedStream(msg=msg, with_headers=True, with_body=True)
  it = iter(stream)
  assert b''.join(it) == msg
  
  # Test for body only

# Generated at 2022-06-13 22:18:16.494396
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """
    测试 BufferedPrettyStream 的 iter_body 方法
    
    这个方法中没有重写 iter_lines 方法，故只能按照这个方法来测试
    """
    import os
    import io
    import tempfile
    from httpie.context import Environment
    from httpie.core import main
    from httpie.output.streams import BufferedPrettyStream
    from httpie.cli.requestitems import items_from_args
    from httpie.compat import urlopen
    from httpie.models import Response
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth, HTTPBearerTokenAuth

    #

# Generated at 2022-06-13 22:18:24.792098
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    print("\n")
    print("test_BufferedPrettyStream_iter_body")

    import json
    json_obj = {"test":"test_test_test"}

    env = Environment()
    encoding = 'utf8'
    json_obj_json_str = json.dumps(json_obj,ensure_ascii=False)
    json_obj_json_str_bytes = bytes(json_obj_json_str,encoding)
    print("json_obj_json_str_bytes: ", json_obj_json_str_bytes)
    msg = HTTPMessage(
        json_obj_json_str_bytes,
        headers=None,
        encoding=encoding,
        content_type='application/json'
    )

    conversion = Conversion()
    formatting = Formatting()
    stream = BufferedPretty

# Generated at 2022-06-13 22:18:29.606784
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    s = HTTPMessage(b'HTTP/1.1 200 OK\r\n\r\n')
    for chunk in EncodedStream(s,with_headers=False).iter_body():
        print(chunk)

# Generated at 2022-06-13 22:18:31.821432
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    env = Environment()
    # The env.stdout is None by default
    assert EncodedStream(env = env)


# Generated at 2022-06-13 22:19:45.285617
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    msg.headers = '''HTTP/1.1 200 OK
Date: Mon, 24 Sep 2018 03:30:32 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Expires: Mon, 24 Sep 2018 03:30:32 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Content-Encoding: gzip

'''
    stream = PrettyStream(
        conversion='all',
        formatting='all',
        msg=msg,
        with_headers=True,
        with_body=True,
    )

# Generated at 2022-06-13 22:19:55.407180
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # python -c 'import main; main.test_BufferedPrettyStream_iter_body()'
    from io import BytesIO
    from httpie.core import main
    from httpie.output.streams import PrettyStream

    def assert_body_iter(stream_cls, env=Environment(), **kwargs):
        """
        Return the iter_body method of a `stream_cls` object.
        Then assert that the object is equal to expected_body.
        """
        r = BytesIO()
        args = main.Args(
            headers=[],
            method='GET',
            output_options=main.OutputOptions(env=env),
            redirects=False,
            stream=True,
            **kwargs,
        )
        stream = stream_cls(msg=r, **args.__dict__)
       

# Generated at 2022-06-13 22:20:07.029716
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    env = Environment(stdout_isatty=True)
    message = HTTPMessage(headers={'a': 'b'}, body='c')
    stream = PrettyStream(msg=message, env=env)

    result = list(stream)
    assert b'\n'.join(result) == b'a: b\r\n\r\n{"c": 1}\n\n'
    assert len(result) == 3

    stream = PrettyStream(msg=message, env=env, with_headers=False)
    result = list(stream)
    assert b'\n'.join(result) == b'{"c": 1}\n\n'
    assert len(result) == 2

    stream = PrettyStream(msg=message, env=env, with_body=False)
    result = list(stream)

# Generated at 2022-06-13 22:20:17.960600
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # unit test for init function
    headers = {'key': 'value'}
    data = b"data"
    length = len(data)
    content_type = 'application/json'
    http_version = b"1.1"
    status_code = 200
    reason_phrase = b"OK"

    # create message
    msg = HTTPMessage(headers, data, length, content_type, http_version, status_code, reason_phrase)
    env = Environment()
    # create encoded stream
    stream = EncodedStream(msg=msg, with_headers=True, with_body=True, on_body_chunk_downloaded=None, env=env)

    # test iter function
    with pytest.raises(NotImplementedError):
        stream.__iter__()

    # test iter_body

# Generated at 2022-06-13 22:20:28.810635
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import httpie.output.streams as streams
    #import httpie.input
    import httpie.context
    import httpie.models

    env = httpie.context.Environment()
    msg = httpie.models.HTTPMessage(headers={'Content-Type': 'text/html'})
    msg.encoding = 'utf-8'
    stream_obj = streams.PrettyStream(conversion=None,
                                      formatting=None,
                                      msg=msg,
                                      env=env)
    text = ["line1", "line2", "line3"]
    msg.body = '\n'.join(text)
    for chunk in stream_obj.iter_body():
        print(chunk.decode())


# Generated at 2022-06-13 22:20:35.849658
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(
        headers=Headers(),
        content=b'abcdefgh',
        encoding='utf8'
    )
    stream = RawStream(msg, with_headers=False, with_body=True)
    stream_iter = stream.iter_body()
    assert next(stream_iter) == b'abcdefg'
    assert next(stream_iter) == b'h'



# Generated at 2022-06-13 22:20:43.580802
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # 1. No conversion needed
    stream = BufferedPrettyStream(msg=HTTPMessage(), mime='text/plain')
    for line, lf in stream.msg.iter_lines(1):
        if b'\0' in line:
            raise BinarySuppressedError()
        yield line.decode(stream.msg.encoding) \
                  .encode(stream.output_encoding, 'replace') + lf  # yapf: disable

    # 2. Conversion needed
    converter = str(self.conversion.get_converter(self.mime))
    if converter:
        body = bytearray()
        # noinspection PyAssignmentToLoopOrWithParameter
        for line, lf in chain([(line, lf)], iter_lines):
            body.extend(line)
            body

# Generated at 2022-06-13 22:20:44.713459
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    pass


# Generated at 2022-06-13 22:20:51.040014
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    r = b'''HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n'''
    def get_body(r):
        obj = EncodedStream(msg=r)
        yield from obj.iter_body()
    gen = get_body(r)
    assert next(gen) == ''

# Generated at 2022-06-13 22:20:59.639623
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    class FakeHTTPMessage():
        def __init__(self, encoding, content_type):
            self.encoding = encoding
            self.content_type = content_type
        def iter_lines(self, chunk_size):
            for c in [b'abc',b'def',b'ghi']:
                yield c, b'\n'
