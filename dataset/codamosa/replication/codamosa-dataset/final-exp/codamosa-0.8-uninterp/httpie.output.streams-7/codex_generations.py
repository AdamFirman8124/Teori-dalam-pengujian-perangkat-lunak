

# Generated at 2022-06-13 22:12:30.492363
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage.from_response(
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/plain\r\n\r\n'
        'Message\n'
        'More\n'
    )
    stream = RawStream(msg)
    assert list(stream.iter_body()) == [b'Message\n', b'More\n']


# Generated at 2022-06-13 22:12:39.244896
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # Expected value
    with_headers = True
    with_body = True
    on_body_chunk_downloaded = None
    msg = HTTPMessage()
    env = Environment()
    conversion = Conversion()
    formatting = Formatting()

    # Actual value
    ps = PrettyStream(
        msg, with_headers, with_body, on_body_chunk_downloaded,
        conversion, formatting, env
    )

    # Compare
    assert ps.msg == msg
    assert ps.with_headers == with_headers
    assert ps.with_body == with_body
    assert ps.on_body_chunk_downloaded == on_body_chunk_downloaded
    assert ps.output_encoding == env.stdout_encoding
    assert ps.formatting == formatting
    assert ps.conversion == conversion

# Generated at 2022-06-13 22:12:47.072626
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    try:
        BufferedPrettyStream(
            msg=HTTPMessage(),
            with_headers=True,
            with_body=True,
            on_body_chunk_downloaded=None,
            conversion=None,
            formatting=None,
            env=None)
    except NameError as e:
        assert False, "Conversion does not exist"
    except Exception as e:
        assert False, "Unexpected error"



# Generated at 2022-06-13 22:12:56.446473
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(
        headers=b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n',
        content_type='application/json',
    )
    stream = PrettyStream(msg, False, False)
    headers = stream.get_headers()
    assert headers == b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'


# Generated at 2022-06-13 22:13:07.843464
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # initialize the variables
    # prepared the msg
    # create a new line
    str1 = '<div class="s-item-container">\n'
    str2 = '<div class="s-item-container">\n'
    str3 = '</div>'
    str4 = '<div class="s-item-container">\n'
    str5 = '<div class="s-item-container">\n'
    # for the purpose of test, the whole message is concatenated by the lines
    whole_msg = '<div class="s-item-container">\n</div><div class="s-item-container">\n</div>'

    # initialize the test data
    msg = HTTPMessage(headers=None, body=None, body_path=None, encoding='utf-8')
    msg

# Generated at 2022-06-13 22:13:15.384553
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import pytest
    a = b'\x1b[1;33mHTTP/1.1 200 OK\x1b[0m'
    b = 'HTTP/1.1 200 OK'
    headers = 'HTTP/1.1 200 OK'
    msg = HTTPMessage(headers=headers)
    f = Formatting()
    c = Conversion()
    s = PrettyStream(msg, conversion=c, formatting=f)
    assert s.process_body(b) == a

# Generated at 2022-06-13 22:13:19.324832
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    stream = EncodedStream(msg=HTTPMessage(), with_headers=True, with_body=True)
    #assert stream.output_encoding == 'utf8'
    assert stream.CHUNK_SIZE == 1



# Generated at 2022-06-13 22:13:25.145096
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    def _test():
        msg = HTTPMessage()
        msg.encoding = "gbk"
        msg.set_body("123")
        raw = RawStream(msg)
        for chunk in raw.iter_body():
            print(chunk)
    _test()

if __name__ == '__main__':
    test_RawStream_iter_body()

# Generated at 2022-06-13 22:13:32.821531
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    s = EncodedStream(msg=None)
    body = b'This is line 1.\nThis is line 2.\nThis is line 3.\n'
    lines = []
    for i in s.iter_body():
        lines.append(i)
    assert lines == [
        'This is line 1.\n',
        'This is line 2.\n',
        'This is line 3.\n',
    ]


# Generated at 2022-06-13 22:13:40.535062
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    source_data = b'<html>\n</html>'
    msg = HTTPMessage(
        headers={"Content-Type": "text/html"},
        raw=source_data,
        encoding='utf8'
    )
    stream = PrettyStream(
        msg=msg,
        with_headers=True,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting(None)
    )
    # No conversion
    assert stream.process_body(source_data) == source_data
    # Conversion from bytearray
    assert stream.process_body(bytearray(source_data)) == source_data

# Generated at 2022-06-13 22:13:56.642339
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    body = b'Yu\xe7ukur\xdcm\xfc\xe7\xfcn' # üçük Kurşunçuçün
    body_iter = EncodedStream(HTTPMessage()).iter_body(body)
    assert next(body_iter).startswith(b'Yu??kur??m???')

# Generated at 2022-06-13 22:14:07.207350
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    import io
    from httpie.core import main
    from httpie.models import Request
    from httpie.output import streams
    env = Environment()
    request_headers = Request(method='GET', headers=['one: two three'])
    message = request_headers
    with io.StringIO() as file:
        stream = streams.EncodedStream(
            message=message,
            with_headers=True,
            with_body=True,
            env=env,
            write=file.write,
        )
        for chunk in stream:
            pass
    assert file.getvalue() == 'one: two three\r\n\r\n\n'


# Generated at 2022-06-13 22:14:16.875570
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Given
    msg = HTTPMessage(url='http://httpbin.org/status/200', method='GET')
    msg.encoding = 'utf-8'
    msg.send()

    # When
    msg.content_encoding = 'identity'
    stream = EncodedStream(msg=msg)
    result = list(stream.iter_body())[0].decode('utf-8')

    # Then
    assert result == '{\n  "status": 200\n}\n'



# Generated at 2022-06-13 22:14:27.982512
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    headers = u'content-type: text/plain\nConnection: close'
    body = 'Some text\nand another one\nand the last one'
    msg = HTTPMessage(headers=headers, body=body)
    stream = RawStream(msg)
    assert b''.join(stream) == \
        b'content-type: text/plain\nConnection: close\r\n\r\nSome text\nand another one\nand the last one'
    stream = EncodedStream(msg, with_headers=False)
    assert b''.join(stream) == \
        b'Some text\nand another one\nand the last one'
    stream = EncodedStream(msg)

# Generated at 2022-06-13 22:14:34.844899
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    sample_msg = HTTPMessage(headers=['Content-Type: application/json', 'X-Foo: 123'])
    encoding = 'utf8'
    # method get_headers of class PrettyStream
    header_stream = PrettyStream(msg=sample_msg, conversion=None, formatting=None, env=Environment())
    pretty_headers = header_stream.get_headers().decode(encoding)
    assert pretty_headers == 'Content-Type: application/json\r\nX-Foo: 123\r\n'


# Generated at 2022-06-13 22:14:43.503578
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    # Create a test message.
    # Create the message.
    msg = HTTPMessage(
        protocol='HTTP/1.1',
        method='GET',
        headers={
            'Content-Type': 'application/javascript',
            'Content-Length': '30',
        },
        body='test-test-test-test-test-test',
    )
    # Create the stream.
    bps = BufferedPrettyStream(
        msg=msg,
        conversion=Conversion(),
        formatting=Formatting(colors=False),
        with_headers=True,
        with_body=True,
    )
    body = ''.join(bps.iter_body())
    # Check the result
    assert body == 'test-test-test-test-test-test'

# Generated at 2022-06-13 22:14:49.236243
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.models import Response
    msg = Response(headers = {'content-type': 'text/html'})
    stream = PrettyStream(msg, conversion='all', formatting='colors')
    output = stream.get_headers().decode('utf-8')
    expected = 'content-type: text/html'
    assert output == expected

# Generated at 2022-06-13 22:14:59.171930
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(headers="Content-Type: text/plain; charset=utf8",
                      encoding="utf8",
                      items=[
                          (b"1", b"\xa5"),
                          (b"2", b"\xe2\x82\xa1"),
                          (b"3", b"\xe2\x82\xac"),
                          (b"4", b"\xe2\x80\xaa\xed\x95\x9c\xed\x98\x84"),
                      ])
    stream = EncodedStream(msg=msg)
    received = [chunk for chunk in stream.iter_body()]

# Generated at 2022-06-13 22:15:04.703206
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(
        headers={"Content-Type":"text/plain"},
        body='1234567890',
        encoding='utf8'
        )
    stream = RawStream(msg)

    stream_iter=stream.iter_body()
    assert next(stream_iter)==b'1234567890'


# Generated at 2022-06-13 22:15:07.937708
# Unit test for constructor of class RawStream
def test_RawStream():
    try:
        obj = RawStream(None, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    except Exception:
        assert False

    assert isinstance(obj, RawStream)


# Generated at 2022-06-13 22:15:35.185205
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = {
        'foo': 'bar',
        'baz': 'qux'
    }
    msg = HTTPMessage(headers=headers)
    p = PrettyStream(msg)
    s = p.get_headers().decode()
    assert "FOO: bar" in s and "BAZ: qux" in s

# Generated at 2022-06-13 22:15:45.917488
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import pytest
    bs = PrettyStream(
        HTTPMessage(
            headers={"aaa":"123"},
            content_type="text/html",
            encoding="utf8"
        ),
        with_headers=False,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting()
    )
    # raise BinarySuppressedError()
    # with pytest.raises(BinarySuppressedError) as error:
    #     for line in bs.iter_body():
    #         print(line)
    # print("error: " + error)
    # print("error: " + error.value)
    # print("error: " + error.value.message)

    # raise DataSuppressedError("123")
    # with pytest.raises(BinarySuppressedError) as error

# Generated at 2022-06-13 22:15:57.594736
# Unit test for method iter_body of class PrettyStream

# Generated at 2022-06-13 22:16:06.485565
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httptools import RequestParser
    from .utils import MockEnvironment

    # Test for a stream with a converter
    msg = HTTPMessage(
        RequestParser.stream_class().read_headers(b'GET / HTTP/1.1\r\n')
    )
    msg.headers['Content-Type'] = 'image/jpeg'
    msg.content = b'test data'
    stream = BufferedPrettyStream(msg)
    stream.conversion.add_converter(
        'image/*',
        lambda content: ('text/plain', 'Converted to text')
    )
    stream.formatting.add_formatter(
        'text/plain',
        lambda content, mime: 'Now formatted'
    )
    assert list(stream.iter_body()) == [b'Now formatted']

    # Test for

# Generated at 2022-06-13 22:16:11.955383
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    type_name, base_msg = 'BaseStream', 'HTTP/1.1 200 OK\r\n\r\n'
    try:
        BaseStream.__iter__(type_name)
    except AttributeError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 22:16:17.539699
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers= {'a': '1', 'b': '2'})
    headers = PrettyStream(msg=msg, with_headers=True, with_body=True).get_headers()
    assert (headers == 'a: 1\r\nb: 2\r\n\r\n'.encode('UTF-8'))


# Generated at 2022-06-13 22:16:36.476846
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    http_message = HTTPMessage(
        headers=u'Content-Type: text/html\n\n',
        encoding='utf-8',
        content_type='text/html'
    )
    stream = PrettyStream(
        msg=http_message,
        env=Environment(
            stdout_isatty=True,
            stdout_encoding='utf-8'
        ),
        conversion=Conversion(
            renderers={'text/html': 'html'},
            renderer_options={'html': {}}
        ),
        formatting=Formatting(),
    )
    expect = 'Content-Type: text/html\r\n\r\n'
    assert stream.get_headers().decode('utf8') == expect

# Generated at 2022-06-13 22:16:42.948783
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    #create stream message
    req_msg  = HTTPMessage(headers={
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Host": "eutils.ncbi.nlm.nih.gov:80",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:50.0) Gecko/20100101 Firefox/50.0"})
    #add body
    req_msg.add_body('<?xml version="1.0" encoding="UTF-8"?>')

# Generated at 2022-06-13 22:16:53.232109
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.plugins.builtin import HTTPHeader
    from httpie.output import format_stream
    from httpie.output.streams import PrettyStream
    from httpie.plugins.builtin import http, HTTP_OK
    url = URL("http://localhost:8010/get")
    stream = PrettyStream(
        msg=HTTPHeader(http(url)),
        formatting=Formatting(),
        conversion=Conversion(),
        with_headers=True,
        with_body=True)
    out = format_stream(stream)
    assert out
    assert HTTP_OK in out

# Generated at 2022-06-13 22:17:07.162772
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage('UTF-8', content_type='UTF-8')
    msg._body = (
      b'{'
      b'  "first_name": "Guido",'
      b'  "last_name": "Bartoli",'
      b'  "attributes": {'
      b'    "email": "guido.bartoli@gmail.com",'
      b'    "age": 41,'
      b'    "phones": ['
      b'      "+39-342-6278481",'
      b'      "+39-342-6278481"'
      b'    ]'
      b'  }'
      b'}'
    )
    stream = EncodedStream(msg)

# Generated at 2022-06-13 22:18:01.911171
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    # Test if the iterator "__iter__" method can be called more than once
    import pytest
    from httpie.core import main
    from httpie.client import HTTPieClient
    from httpie.core import read_http_message
    from httpie.utils import is_windows
    from httpie.output.streams import BinarySuppressedError, BaseStream

    p = pytest.ensure_clean_app_cache_dir(httpserver.__file__)

# Generated at 2022-06-13 22:18:13.589295
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.input import ParseError
    from httpie.models import Response
    from httpie.compat import urlopen
    env = Environment()
    url = "http://httpbin.org/image/jpeg"
    response = urlopen(url)
    try:
        msg = Response(
            url.encode(),
            [RC_OK, 'OK'.encode()],
            response.headers.items(),
            response.read()
        )
    except ParseError as e:
        print(e)
        msg = None
    conversion = Conversion(env, msg)
    formatting = Formatting()
    stream = BufferedPrettyStream(conversion, formatting, msg)
    for chunk in stream.iter_body():
        print(chunk)

# Generated at 2022-06-13 22:18:19.599963
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # test use change newline of chunk to '\n'
    format = Formatting()
    format.is_windows = False
    format.is_raw = False
    stream = PrettyStream(Conversion(), format)
    line_with_lf = '{"prop1": "value1"}\r\n'
    chunk = stream.process_body(line_with_lf)
    assert chunk == bytes(line_with_lf, 'utf-8')

    # test use change newline of chunk to '\r\n'
    format = Formatting()
    format.is_windows = True
    stream = PrettyStream(Conversion(), format)
    line_with_lf = '{"prop1": "value1"}\n'
    chunk = stream.process_body(line_with_lf)

# Generated at 2022-06-13 22:18:26.569359
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage()
    msg.headers = '''HTTP/1.1 200 OK
Server: Apache
Accept-Ranges: bytes
Content-Length: 6
Vary: Accept-Encoding
Connection: close
Content-Type: text/html; charset=UTF-8'''
    stream = BufferedPrettyStream(msg,with_headers=True,with_body=True)
    print(stream.iter_body())

# Generated at 2022-06-13 22:18:30.571427
# Unit test for method iter_body of class PrettyStream

# Generated at 2022-06-13 22:18:41.166035
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    ts = PrettyStream(msg=HTTPMessage(body='abc'), with_headers=False,
                      conversion=None, formatting=None)
    assert list(ts.iter_body()) == [b'abc\r\n']
    ts = PrettyStream(msg=HTTPMessage(body='a\0bc'), with_headers=False,
                      conversion=None, formatting=None)
    assert list(ts.iter_body()) == [b'a\0bc\r\n']
    ts = PrettyStream(msg=HTTPMessage(body='abc\r\ndef'), with_headers=False,
                      conversion=None, formatting=None)
    assert list(ts.iter_body()) == [b'abc\r\n', b'def\r\n']

# Generated at 2022-06-13 22:18:45.091399
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    tstr = "hello"
    temp = HTTPMessage(b'200 OK', b'', headers={}, encoding='utf8')
    temp.bytes = bytes(tstr, 'utf-8')

    enc = EncodedStream(temp)
    iter_body = enc.iter_body()
    result = list(iter_body)[0]
    # iter_body returns bytes
    assert result == bytes(tstr, 'utf-8')

# Generated at 2022-06-13 22:18:54.051014
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: application/json;\r\n' + 'X-Request-ID: 123456789\r\n\r\n'
    msg = HTTPMessage()
    msg.encoding = 'utf8'
    msg.headers = headers
    msg.content_type = 'application/json;'
    stream = PrettyStream(msg=msg)
    headers_bytes = stream.get_headers()
    assert headers_bytes == bytes(headers, 'utf-8')



# Generated at 2022-06-13 22:19:04.532867
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    stream = EncodedStream(msg=Mock())
    stream.msg.encoding = 'gbk'
    stream.output_encoding = 'utf8'
    s = [b'abcd\n1234\n']
    stream.msg.iter_lines = lambda chunk_size: s
    stream.msg.encoding = 'gbk'
    stream.output_encoding = 'utf8'
    assert list(stream.iter_body()) == ['abcd\n'.encode('utf8'), '1234\n'.encode('utf8')]
    s.pop()
    s.append(b'abcd\u0000\n')
    try:
        for _ in stream.iter_body():
            assert False
    except BinarySuppressedError as e:
        assert e.message == BINARY_SUPPRESSED_

# Generated at 2022-06-13 22:19:15.314687
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import json
    import re
    from httpie.compat import is_py26
    from httpie.output.streams import BufferedPrettyStream

    msg = HTTPMessage('200 OK', 'Content-Type: application/json', b'{"key": "value"}')

    tmp = BufferedPrettyStream(msg, with_headers=True, with_body=True)
    result = tmp.iter_body()

    if not is_py26:
        next(result)

    exp = re.compile(r'{\n +"key": "value"\n}', re.M)
    assert len(list(filter(exp.match, result))) == 1

# Generated at 2022-06-13 22:20:49.667636
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # mock message
    msg = HTTPMessage(
        url='http://www.google.com',
        body='some_body',
        headers={'header': 'some_value'},
        encoding='utf8',
        status_line='201 Created'
    )

    # mock content processing
    class Foo:
        def get_converter(self, mime):
            return None

    # mock environment
    env = Environment()
    env.stdout_encoding = 'utf8'
    env.stdout_isatty = True

    # set up test
    stream = EncodedStream(msg=msg, env=env)

    # execute test
    assert b'\n' in b''.join([i for i in stream.iter_body()])

    # set up test

# Generated at 2022-06-13 22:20:54.682368
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(method='GET', target='/', version="HTTP/1.1")
    msg.body = b"abc\0def\ng"
    msg.encoding = "utf-8"
    stream = EncodedStream(msg)
    lines = [x for x in stream.iter_body()]
    assert lines == [b'abc?def\ng']


# Generated at 2022-06-13 22:20:57.391776
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    body = 'this is a test'
    stream = PrettyStream(None, None)
    assert stream.process_body(body)

# Generated at 2022-06-13 22:21:00.799979
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.models import Response
    from io import BytesIO
    res = Response(BytesIO(b'hello world'))
    for chunk in RawStream(res, with_headers=False).iter_body():
        assert chunk == b'hello world'

# Generated at 2022-06-13 22:21:14.124027
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # chunk is str
    stream = PrettyStream(conversion=Conversion(),
                          formatting=Formatting())
    chunk = stream.process_body(u"Hello world")
    assert chunk == b'\x1b[32mHello world\x1b[39m'
    chunk = stream.process_body(b"Hello world")
    assert chunk == b'\x1b[32mHello world\x1b[39m'

    # chunk is bytes
    stream = PrettyStream(conversion=Conversion(),
                          formatting=Formatting())
    chunk = stream.process_body(b'Hello world')
    assert chunk == b'\x1b[32mHello world\x1b[39m'

# Generated at 2022-06-13 22:21:24.271903
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    """Test method iter_body of class EncodedStream."""

    # Test with a simple UTF-8 message
    message = b'hello\r\n'
    stream = EncodedStream(HTTPMessage(message))
    assert stream.iter_body() == [b'hello\r\n']

    # Test with a UTF-8 message with an accent
    message = b'h\xc3\xa9llo\r\n'
    stream = EncodedStream(HTTPMessage(message))
    assert stream.iter_body() == [b'h\xc3\xa9llo\r\n']

    # Test with a message using Latin-1 encoding
    message = b'h\xe9llo\r\n'
    stream = EncodedStream(HTTPMessage(message, encoding='latin1'))

# Generated at 2022-06-13 22:21:35.285257
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import csv
    csv_data = [['i', 'j'], ['1', '2'], ['10', '20']]
    csv_str = ','.join(['i', 'j']) + '\n' + ','.join(['1', '2']) + '\n' + ','.join(['10', '20'])
    data = PrettyStream(
        msg=HTTPMessage(headers='''content-type: text/csv''',
                        data=csv_str),
        with_headers=False,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting()
        ).iter_body()
    data_list = []
    for d in data:
        data_list.append(d)
    assert(len(data_list) == 1)

# Generated at 2022-06-13 22:21:43.439020
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.input import ParseError
    from httpie.models import HTTPResponse
    from tempfile import NamedTemporaryFile
    headers = "HTTP /1.1 200 OK\r\nContent-length: 5\r\nContent-Type: text/plain"
    body = "Hello World".encode()
    response = HTTPResponse(fp=BytesIO(headers.encode()+b"\r\n"+body))
    response.parse_headers()
    stream = PrettyStream(response, conversion=Conversion(), formatting=Formatting())
    # The convertion of header
    assert response.headers.encode() == b'HTTP/1.1 200 OK\r\nContent-length: 5\r\nContent-Type: text/plain'

# Generated at 2022-06-13 22:21:48.507032
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # 1. msg is not in (request,response)
    with pytest.raises(AssertionError):
        a = EncodedStream(mime="")
    # 2. msg is in request
    with pytest.raises(AssertionError):
        a = EncodedStream(request="")
    # 3. msg is in response
    a = EncodedStream(response="")

# Generated at 2022-06-13 22:21:51.162926
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    e = EncodedStream(msg)
    assert e.msg == msg
    assert e.with_headers == True
    assert e.with_body == True
    assert e.on_body_chunk_downloaded == None
