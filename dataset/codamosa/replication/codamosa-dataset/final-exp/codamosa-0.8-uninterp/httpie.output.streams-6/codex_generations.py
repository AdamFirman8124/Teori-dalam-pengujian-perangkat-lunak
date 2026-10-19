

# Generated at 2022-06-13 22:12:34.417563
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():

    def get_bytes():
        return b"line1"\
               b"line2"\
               b"line3"\
               b"line4"\
               b"line5"\
               b"line6"\
               b"line7"\
               b"line8"\
               b"line9"\
               b"line10"

    pretty_stream = PrettyStream(
        HTTPMessage(b"".join(chr(i).encode() for i in range(256)), "image/png"),
        Conversion(),
        Formatting(),
        with_headers=False,
        with_body=True,
        on_body_chunk_downloaded=None
    )

    gen = pretty_stream.iter_body()
    bytes = next(gen)

    assert bytes == get_bytes()

# Generated at 2022-06-13 22:12:47.336755
# Unit test for constructor of class EncodedStream

# Generated at 2022-06-13 22:13:01.294646
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    print('Test PrettyStream constructor:')
    # case 1
    stream1 = PrettyStream(
        msg=HTTPMessage(headers={"Content-Type": 'application/json'}, body=b'{"a":1}\n'),
        conversion=Conversion(),
        formatting=Formatting(),
        with_headers=True,
        with_body=True,
    )
    assert stream1.mime == 'application/json'
    assert stream1.output_encoding == 'utf8'

    # case 2

# Generated at 2022-06-13 22:13:12.637875
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.output.streams import BufferedPrettyStream
    from httpie.models import HTTPResponse

    import json

    data = dict(a=1, b="b\nbb", c=dict(d=3))
    json_str = json.dumps(data)

    response = HTTPResponse(
        url='http://www.baidu.com',
        headers={"content-type": "application/json;charset=UTF-8"},
        body=json_str,
        status_code=200,
        reason="OK")

    stream = BufferedPrettyStream(conversion=Conversion(),
                                  formatting=Formatting(),
                                  msg=response)

    print(json_str)
    print(stream.iter_body())

test_BufferedPrettyStream_iter_body()

# Generated at 2022-06-13 22:13:20.202715
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    msg = HTTPMessage(200, '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Foo: bar',
        'Content-Type: text/xml',
        'Content-Length: 16',
        '',
        '']))
    msg.body = '{"foo": "bar"}'
    for chunk in BufferedPrettyStream(msg):
        print(chunk, end='')



# Generated at 2022-06-13 22:13:27.297827
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from requests import Response
    from httpie.models import Response as HTTPieResponse
    response = Response()
    response.headers = {'Content-Type': 'application/json'}
    response.encoding = 'utf-8'
    response.status_code = 200
    response.raw = BytesIO(b'{"a":"b"}')
    pretty_response = HTTPieResponse.from_httpie_response(response)
    BufferedPrettyStream(pretty_response).iter_body()

# Generated at 2022-06-13 22:13:31.506048
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    from httpie.output.streams import PrettyStream
    from httpie.models import HTTPMessage
    m = HTTPMessage()
    ps = PrettyStream(m)


# Generated at 2022-06-13 22:13:38.511297
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # Example 1: Initialize with default values
    test1 = EncodedStream(msg = HTTPMessage(b'', b'', b''))
    assert test1.output_encoding == 'utf8'

    # Example 2: Initialize with custom values
    test2 = EncodedStream(msg = HTTPMessage(b'', b'', b''), output_encoding = 'ascii')
    assert test2.output_encoding == 'ascii'


# Generated at 2022-06-13 22:13:39.436941
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    print(1)



# Generated at 2022-06-13 22:13:41.631435
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    pass



# Generated at 2022-06-13 22:14:08.040964
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # An HTTP Message
    msg = HTTPMessage(status_line=b'HTTP/1.1 200 OK')
    msg.headers = b'Content-Type: text/html\r\n' \
                  b'Content-Length: 10\r\n'
    msg.body = b'0123456789'
    # The Conversion object
    conversion = Conversion(detect_encoding=True)
    # The Formatting object
    formatting = Formatting()

    # Create PrettyStream using constructor
    ps = PrettyStream(msg, True, True, conversion, formatting)

    # Get the headers
    headers = ps.get_headers()
    # Get the body
    body = ps.iter_body()

    # We can iterate the body and get the body bytes
    for chunk in body:
        print(chunk)

    #

# Generated at 2022-06-13 22:14:14.149024
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    test_str = 'test'
    msg = HTTPMessage('test', 'text/html', b'11111')
    stream = PrettyStream(msg, True, True)
    assert stream.process_body(test_str) == b'test'



# Generated at 2022-06-13 22:14:16.500376
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage()
    EncodedStream(msg = msg)


# Generated at 2022-06-13 22:14:27.938163
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    def on_body_chunk_downloaded(chunk):
        print(chunk)

    data = {}

# Generated at 2022-06-13 22:14:33.762373
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    '''
    This method gets an iterator on the message body,
    applies the appropriate converter,
    then formats the output to the terminal.
    '''
    # GIVEN a Stream object
    pretty_stream            = PrettyStream(conversion=True, formatting=True)

    # WHEN calling the method iter_body
    iterator = pretty_stream.iter_body()

    # THEN the returned iterator is correct
    assert isinstance(iterator, Iterable)

# Generated at 2022-06-13 22:14:42.146650
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    input_list = ['foo', 'bar', 'greek: αβγδ', 'exotic: ⓉⒺⒸⓃⒾⓋⒺ', '\xff']
    input_str = '\n'.join(input_list)
    msg = HTTPMessage(content_type='text/plain; charset=ASCII', body=input_str)
    output_list = list(EncodedStream(msg).iter_body())
    output_str = b''.join(output_list).decode()
    expected = '\n'.join(input_list) + '\n'
    assert output_str == expected


# Generated at 2022-06-13 22:14:54.435759
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    http_response = requests.get("http://httpbin.org/get")
    http_response.encoding = 'utf-8'
    msg = HTTPMessage(
        http_response.raw,
        http_response.headers,
        http_response.content,
        http_response.url,
        http_response.status_code,
        http_response.encoding,
        http_response.reason
    )
    stream = BaseStream(
        msg,
        with_headers=False,
        with_body=True,
        on_body_chunk_downloaded=None
    )
    assert msg.url == http_response.url
    assert msg.status_code == http_response.status_code
    assert msg.encoding == http_response.encoding
    assert msg.reason == http_response.reason

# Generated at 2022-06-13 22:15:05.592997
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # missing required arguments
    try:
        PrettyStream()
    except TypeError:
        pass
    except BaseException as e:
        raise e

    # missing optional arguments
    PrettyStream(msg=HTTPMessage(), conversion=Conversion(Environment()),
                 formatting=Formatting(Environment()))

    # missing optional arguments
    PrettyStream(msg=HTTPMessage(), conversion=Conversion(Environment()),
                 formatting=Formatting(Environment()), with_headers=False)

    # missing optional arguments
    PrettyStream(msg=HTTPMessage(), conversion=Conversion(Environment()),
                 formatting=Formatting(Environment()), with_body=False)


# Generated at 2022-06-13 22:15:14.609959
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    import os, json
    import requests
    import httpie.output.formatters
    import httpie.input
    import httpie.cli
    import httpie.context
    import httpie.output.streams
    environment = httpie.context.Environment()
    environment.stdin = httpie.input.DEFAULT_STDIN
    output_options = httpie.cli.OutputOptions()
    output_options.pretty = True
    output_options.stream = False
    output_options.prettify = True
    output_options.print_headers = True
    output_options.follow = False
    output_options.download = False
    output_options.output_dir = None
    output_options.output_file = None
    output_options.formatted = True
    output_options.output_encoding = 'utf8'
   

# Generated at 2022-06-13 22:15:17.866980
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    stream = PrettyStream(msg=None, with_headers=False, with_body=False, conversion=None, formatting=None)
    stream.get_headers()


# Generated at 2022-06-13 22:15:43.340196
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    message = HTTPMessage('\r\n'.join((
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        '',
        'first line\nsecond line'
    )).encode('utf8'))
    buffered = BufferedPrettyStream(
        message,
        conversion=Conversion(),
        formatting=Formatting(),
        with_headers=True,
        with_body=True
    )
    result = []
    for chunk in buffered.iter_body():
        result.append(chunk)
    expected = (b'first line\nsecond line')
    assert b''.join(result) == expected, "bytes.join failed"


# Generated at 2022-06-13 22:15:45.127056
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    # TODO: test_RawStream_iter_body()
    pass


# Generated at 2022-06-13 22:15:50.941674
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers={'a': 'b'})
    stream = PrettyStream(
        msg,
        with_headers=True,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting())
    s = stream.get_headers()
    assert s == b'a: b'


# Generated at 2022-06-13 22:15:56.902162
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(b'\xef\xbb\xbf#!/usr/bin/env bash\n', headers={b'foo': b'bar'}, encoding='utf-8')
    stream = EncodedStream(msg=msg)
    assert b'\xef\xbb\xbf#!/usr/bin/env bash\n' == next(stream.iter_body())



# Generated at 2022-06-13 22:16:02.728701
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage()
    msg.iter_body = lambda chunk_size: iter([b'{"key":', b'"value"}'])
    msg.encoding = 'utf8'
    ps = PrettyStream(msg, with_headers=False, with_body=True)
    res = list(ps.iter_body())
    assert b'{"key": "value"}' in res



# Generated at 2022-06-13 22:16:15.021959
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    print("Test PrettyStream iter_body")
    msg1 = HTTPMessage.from_string(
        raw=b"Content-type: Application/JSON\r\n\r\n"
            b"{\"A\":1, \"B\":2}",
        body_as_raw=True,
        headers_as_raw=True,
    )
    ps = PrettyStream(msg1, True, True)
    assert list(ps.iter_body()) == [b'{\n\t"A": 1,\n\t"B": 2\n}\n']

# Generated at 2022-06-13 22:16:31.883345
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    header = {'Content-Type': 'application/json'}
    text_body = b'{"aaa": "bbb"}\n'
    test_msg = HTTPMessage(
        url='http://python.org',
        method='GET',
        headers=header,
        body=text_body,
        encoding='utf8',
        content_type='application/json'
    )
    formatting = Formatting()
    conversion = Conversion()

    ps = PrettyStream(
        msg=test_msg,
        conversion=conversion,
        formatting=formatting
    )

    for i in ps.iter_body():
        print(i)



# Generated at 2022-06-13 22:16:47.375894
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.output.formatters import JSONFormatter
    from httpie.models import HTTPResponse

    # MIME types for which the formatter will be used.
    FORMATTERS_MIME_TYPES = {
        'application/json',
        'application/hal+json',
    }
    # Expected output for each input

# Generated at 2022-06-13 22:16:53.760654
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie.compat import urlunparse, OrderedDict
    from httpie.context import Environment
    from httpie.models import Address
    from httpie.utils import get_response_headers

    class PrettyStreamNew(PrettyStream):
        def get_headers(self) -> bytes:
            return self.formatting.format_headers(
                self.msg.headers).encode(self.output_encoding)

    env = Environment()
    env.stdout_isatty = True

    scheme, host, port, path, _, _ = urlunparse(('https', 'httpbin.org', '', 'get', '', ''))
    response_headers = OrderedDict([
        ('Content-Type', 'application/json'),
        ('Content-Length', None),
        ('Foo', 'bar')
    ])
   

# Generated at 2022-06-13 22:17:05.350944
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    import io
    from httpie.output.streams import PrettyStream
    from httpie.context import Environment
    from httpie.models import Message

    env = Environment(vars=dict())
    msg = Message(headers=dict(a='a', b='b'))
    stream = PrettyStream(msg=Message(), env=env, with_headers=False)
    assert stream.get_headers() == ''.encode()

    stream = PrettyStream(msg=msg, env=env, with_headers=True)
    assert stream.get_headers() == 'a: a\nb: b\r\n\r\n'.encode()


# Generated at 2022-06-13 22:17:49.670876
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    s = EncodedStream(msg=HTTPMessage('{"status": "OK"}', 'application/json', 
                                                                        ExitStatus.OK), env=Environment())
    assert s.msg.headers == '{"status": "OK"}'
    assert s.with_headers == True
    assert s.with_body == True
    assert s.on_body_chunk_downloaded == None
    assert s.output_encoding == 'utf8'

# Generated at 2022-06-13 22:18:01.894176
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    import StringIO
    s = StringIO.StringIO()
    s.write(u"HTTP/1.1 200 OK\r\n")
    s.write(u"Content-Type: text/plain; charset=utf8\r\n")
    s.write(u"\r\n")
    s.write(u"hello\r\n")
    s.write(u"world\r\n")
    s.write(u"\r\n")
    s.seek(0)
    msg = next(iter(HTTPMessage.parse_stream(s)))
    stream = EncodedStream(msg)
    assert stream.iter_body()

# Generated at 2022-06-13 22:18:10.448717
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # Create a HTTPMessage object with headers to test
    headersTest = 'user-agent: Httpie\ncookie: test_cookie'
    msg = HTTPMessage(headers=headersTest)
    # Create a PrettyStream instance
    p = PrettyStream(msg, False, False)
    # Check headers not modified
    assert p.get_headers() == b'user-agent: Httpie\ncookie: test_cookie'


# Generated at 2022-06-13 22:18:16.901462
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(headers = '''HTTP/1.1 200 OK\r\nX-Powered-By: Flask\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: 8\r\n\r\n''', body = '''{"hello": "world"}''', encoding = 'utf-8')
    stream = EncodedStream(msg = msg)
    for chunk in stream.iter_body():
        print(chunk)


# Generated at 2022-06-13 22:18:21.478754
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(
        headers={'content-encoding': 'utf8'},
        body='\u2713'
    )
    stream = EncodedStream(msg, with_headers=False, with_body=True)
    assert b'\xe2\x9c\x93\n' == next(stream.iter_body())



# Generated at 2022-06-13 22:18:32.645041
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(
        'GET', 'http://www.example.com/',
        headers={'Content-Type': 'text/plain'},
        body='this is a test'
    )
    stream = EncodedStream(msg)
    print(type(stream), stream)
    print(type(stream.output_encoding), stream.output_encoding)
    msg = HTTPMessage(
        'GET', 'http://www.example.com/',
        headers={'Content-Type': 'text/plain'},
        body='this is a test',
        encoding='utf8'
    )
    stream = EncodedStream(msg)
    print(type(stream), stream)
    print(type(stream.output_encoding), stream.output_encoding)

# Generated at 2022-06-13 22:18:37.575503
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(headers=b'\r\n')
    assert encoding == 'utf8'
    assert conversion == self.msg.encoding
    assert formatting == self.msg.encoding
    assert chunk_size == 1

# Generated at 2022-06-13 22:18:41.823667
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    msg = HTTPMessage()
    stream = PrettyStream(msg, with_headers=True, with_body=True)
    assert stream.msg == msg
    assert stream.with_headers == True
    assert stream.with_body == True

# Generated at 2022-06-13 22:18:47.527804
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    import io
    import sys
    import unittest

    from httpie.cli import Environment
    from httpie.input import ParseError
    from httpie.client import JSON_ACCEPT
    from httpie.models import HTTPMessage
    from httpie.output.streams import EncodedStream

    class EncodedStreamTest(unittest.TestCase):

        def setUp(self):
            super(EncodedStreamTest, self).setUp()
            self.encoding = 'utf8'
            self.env = Environment(stdin=io.BytesIO(),
                                   stdout=io.BytesIO(),
                                   stderr=io.BytesIO(),
                                   isatty=True,
                                   colors=256)
            self.env.stdout_isatty = True
            self.env.stdout_encoding

# Generated at 2022-06-13 22:18:53.764685
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(
        'GET / HTTP/1.1',
        {'Content-Type': 'application/json'},
        '{"a": "b"}'
    )
    ps = PrettyStream(msg, conversion=Conversion(),
                      formatting=Formatting())
    assert ps.get_headers() == b'Content-Type: application/json'



# Generated at 2022-06-13 22:20:15.407359
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    test = EncodedStream(
        msg = HTTPMessage(body='ñ'.encode('utf-8'))
    )
    assert list(test.iter_body()) == ['\xc3\xb1\n'.encode('utf-8')]
# test_EncodedStream_iter_body()


# Generated at 2022-06-13 22:20:27.367521
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    from httpie.output.streams import BufferedPrettyStream, RawStream
    from httpie.output.processing import Conversion, Formatting

    msg = HTTPMessage(headers=['Content-Type: text/plain'], body='foobar')
    env = Environment()
    conversion = Conversion(env=env)
    formatting = Formatting(env=env)
    stream = BufferedPrettyStream(
        msg=msg, conversion=conversion, formatting=formatting,
        on_body_chunk_downloaded=None,
        #with_headers=True, with_body=True
    )
    res = [b for b in stream]
    assert b'Content-Type: text/plain' in res[0]

# Generated at 2022-06-13 22:20:32.762534
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    bps = BufferedPrettyStream(
        HTTPMessage(
            headers='*'),
        conversion='',
        formatting='')
    returned_values = [
        chunk
        for chunk in bps.iter_body()
    ]
    print(returned_values)

# Generated at 2022-06-13 22:20:40.928091
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    # test PrettyStream class
    print("test prettystream begins")
    from httpie.models import Response
    res = Response(status_code='200', url='http://www.baidu.com', headers={'A': 'a'}, content='content')
    ps = PrettyStream(msg=res, conversion=None, formatting=None, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    for i in ps.iter_body():
        print(i)
    print("test prettystream ends")
    pass

if __name__ == '__main__':
    test_PrettyStream()

# Generated at 2022-06-13 22:20:53.270413
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import sys

    from httpie.models import HTTPResponse

    from httpie.output.streams import PrettyStream

    response = HTTPResponse(
        'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{{"abc": 123}}',
        encoding='utf-8',
    )

    stream = PrettyStream(
        msg=response,
        conversion=Conversion(),
        formatting=Formatting(),
        env=Environment(),
        with_body=True
    )
    try:
        stream_iter = stream.iter_body()
    except Exception as e:
        print(e, file=sys.stderr)
        return
    for line in stream_iter:
        print(line.decode())



# Generated at 2022-06-13 22:21:02.257652
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    from httpie.models import Response
    from httpie.output.processing import Conversion, Formatting

    response = Response(
        status_code=200,
        headers={'Content-Type': 'application/json'},
        body='{"age": 33}'
    )

    class FakeConversion:
        def __init__(self):
            pass

        def get_converter(self, mime):
            return None
    
    class FakeFormatting:
        def __init__(self):
            pass

        def format_body(self, content, mime):
            return content

    stream = BufferedPrettyStream(response,
                                  conversion=FakeConversion(),
                                  formatting=FakeFormatting()
                                  )

    for chunk in stream.iter_body():
        assert chunk == b'{"age": 33}'
       

# Generated at 2022-06-13 22:21:15.292813
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    from httpie.models import Response
    from httpie.output.streams import BaseStream, RawStream
    import httpie.cli.argtypes

    # Arrange
    msg = Response(
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{\n"
        "   \"headers\": {\n"
        "       \"Content-Type\": \"application/json\"\n"
        "   }\n"
        "}\n",
        b"{\n   \"headers\": {\n       \"Content-Type\": \"application/json\"\n   }\n}\n"
    )
    stream = BaseStream(
        msg,
        with_headers=True,
        with_body=True
    )

    # Act
   

# Generated at 2022-06-13 22:21:24.667922
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    message = HTTPMessage()
    message.headers = 'Content-type: text/plain'
    message.content = 'foo bar'
    message.content_type = 'text/plain'
    message.encoding = 'utf8'

    # Test if headers and body is written
    output=[]
    stream = RawStream(message, on_body_chunk_downloaded=output.append)
    assert list(stream) == [b'Content-type: text/plain', b'\r\n\r\n', b'foo bar']
    # Check if there was actually one callback to body chunk
    assert output == [b'foo bar']

    # Test if headers only is written
    output=[]
    stream = RawStream(message, with_body=False, on_body_chunk_downloaded=output.append)
   

# Generated at 2022-06-13 22:21:35.510939
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(b'GET / HTTP/1.1\r\n\r\n', encoding='ascii')
    stream = EncodedStream(msg)
    # Iterate the body of msg by line
    for line in stream.iter_body():
        print(line)
    msg = HTTPMessage(b'GET / HTTP/1.1\r\n\r\n', encoding='ascii')
    stream = EncodedStream(msg, with_body=False)
    # Iterate the body of msg by line (no body)
    for line in stream.iter_body():
        print(line)
    msg = HTTPMessage(b'GET / HTTP/1.1\r\n\r\n\0', encoding='ascii')
    stream = EncodedStream(msg)
    #

# Generated at 2022-06-13 22:21:43.606692
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.core import parse_headers
    # Works for regular text
    msg = HTTPMessage(headers=b"Content-Type: text/html\r\n\r\n", body=b"Hello\nWorld\n\n")
    pretty_stream = PrettyStream(msg=msg, conversion=Conversion(), formatting=Formatting({}))
    assert list(pretty_stream.iter_body()) == [b"Hello\n", b"World\n\n"]
    # works for binary text
    msg = HTTPMessage(headers=b"Content-Type: application/x-gzip\r\n\r\n", body=b"Hello\0World\n\n")
    pretty_stream = PrettyStream(msg=msg, conversion=Conversion(), formatting=Formatting({}))