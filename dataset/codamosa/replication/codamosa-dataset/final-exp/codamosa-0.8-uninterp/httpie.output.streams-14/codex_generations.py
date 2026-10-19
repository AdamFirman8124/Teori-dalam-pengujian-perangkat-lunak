

# Generated at 2022-06-13 22:12:36.702922
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # create a response
    response = HTTPMessage(headers = { "Content-Type": "text/plain" }, 
                           encoding = "utf-8",
                           body = "response body")
    # create an instance of EncodedStream
    stream = EncodedStream(response)
    # get the body as stream of bytes
    body = stream.iter_body()
    # get the first byte of the body
    body_first_byte = next(body)
    # check if the body is equal to expected body
    assert b'response body' == body_first_byte
    
    # create a response
    binary_body = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09'

# Generated at 2022-06-13 22:12:39.939971
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    data = b'a\r\nb'
    msg = HTTPMessage()
    msg.encoding = 'utf-8'
    msg._body = io.BytesIO(data)
    msg.headers = 'Content-Type: text/plain'

    encoded_stream = EncodedStream(
        msg=msg,
        with_headers=False,
        with_body=False,
    )
    assert b''.join(encoded_stream) == b'a\r\nb'

# Generated at 2022-06-13 22:12:46.662632
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    from httpie.output.processing import Conversion
    from httpie.output.processing import Formatting
    from httpie.output.streams import BufferedPrettyStream
    from httpie.models import HTTPMessage
    conversion = Conversion()
    formatting = Formatting()
    msg = HTTPMessage(b'{"name": "John Smith"}', content_type='application/json')
    stream = BufferedPrettyStream(msg=msg, conversion=conversion, formatting=formatting)

# Generated at 2022-06-13 22:12:51.564212
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    headers={}
    msg=HTTPMessage(headers)
    stream=PrettyStream(msg)
    out=stream.get_headers()
    assert out == b'{}'


# Generated at 2022-06-13 22:13:00.724205
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    class TestHTTPMessage(HTTPMessage):
        def iter_body(self, chunk_size):
            for i in range(10):
                yield str(i).encode('utf-8')

    msg = TestHTTPMessage(headers="\n".join(['a: b', 'c: d']),
                          content_type="text/html; charset=utf-8")
    stream = RawStream(msg, on_body_chunk_downloaded=print)
    for chunks in stream:
        print(chunks)



# Generated at 2022-06-13 22:13:12.199958
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    from httpie import ExitStatus
    from httpie.client import JSON_ACCEPT
    from httpie.compat import urlopen
    from httpie.downloads import (
        parse_content_range, filename_from_content_disposition, filename_from_url, get_unique_filename, ContentRangeError, filename_from_content_type, ContentTypeError, filename_from_url,
    )
    from httpie.output.streams import EncodedStream, PrettyStream
    from httpie.output.streams import BinarySuppressedError
    from httpie.parser import get_parser
    from httpie.plugins import plugin_manager
    from httpie.status import ExitStatus
    from httpie import ExitStatus
    from httpie.models import Request, Response, HTTPHeaders
    from utils import test
    from fixtures import FILE_PATH, FILE_

# Generated at 2022-06-13 22:13:24.814711
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    from httpie.output.streams import RawStream
    from httpie.models import HTTPMessage
    def test(msg_data):
        msg = HTTPMessage()
        msg.headers = msg_data.split("\r\n\r\n")[0]
        msg.body = msg_data.split("\r\n\r\n")[1]
        msg.encoding = "utf8"
        msg.content_type = "test"
        s = RawStream(msg)
        return s.iter_body()
    assert list(test("")) == []
    assert list(test("get")) == [b"get"]
    assert list(test("get\r\n\r\n123")) == [b"get\r\n\r\n1", b"23"]

# Generated at 2022-06-13 22:13:35.011306
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    """Test case for PrettyStream class.

    Test case for method get_headers.

    """
    message = b'Content-Type: application/json\r\nContent-Length: 2\r\n\r\n{}'
    message = HTTPMessage.from_raw(message)
    pretty_stream = PrettyStream(message,
                                 with_headers=True,
                                 with_body=False)
    headers = pretty_stream.get_headers()
    match = b'Content-Type: application/json\nContent-Length: 2\n\n'
    assert headers == match



# Generated at 2022-06-13 22:13:36.062108
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    pass

# Generated at 2022-06-13 22:13:42.449191
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import csv
    csvfile = open('data/stocks.csv', 'r')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    msg = '\r\n'.join(['\t'.join(row) for row in spamreader])
    msg = HTTPMessage(
        body=msg,
        encoding='utf8',
        content_type='text/csv',
    )
    pretty_stream = BufferedPrettyStream(
        msg=msg,
        with_headers=False,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting(),
    )
    for line in pretty_stream.iter_body():
        print(line)
# End of unit test

# Generated at 2022-06-13 22:13:59.592104
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    test_message = HTTPMessage()
    test_message.set_headers({'test_key': 'test_value'})
    test_message.encoding = 'utf-8'
    test_message.set_body(b'')
    expected = b'HTTP/1.1 200 OK\r\n' \
               b'Content-Length: 0\r\n' \
               b'test_key: test_value\r\n' \
               b'\r\n'
    stream = RawStream(test_message)
    assert expected == b''.join(stream.iter_body())

# Generated at 2022-06-13 22:14:04.074509
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Test function iter_body() of EncodedStream class.
    #
    # c = EncodedStream(msg)
    # c.iter_body()
    #
    # This test case is intended to verify that the iter_body
    # function of EncodedStream class works correctly. The
    # expected result is the same as the expected value.
    #

    # Create a HTTPMessage object with the given headers and body.
    # If body is given, content_type is automatically set to
    # "httpie/client-form", and if a dict is passed, it will
    # automatically be encoded as form data.
    msg = HTTPMessage(headers={'User-Agent': 'HTTPie-client/0.9.8'},
                      body='Chunk1 Chunk2 Chunk3 Chunk4',
                      encoding='utf8')

# Generated at 2022-06-13 22:14:18.011296
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    # Pair: (uri, expected_mime)
    test_set = [
        ("https://httpbin.org/robots.txt", 'text/plain'),
        ("https://httpbin.org/headers", 'application/json'),
        ("https://httpbin.org/user-agent", 'application/json'),
        ("https://httpbin.org/user-agent", 'application/json'),
    ]
    for (uri, expected_mime) in test_set:
        downloader = HTTPDownloaderContext(cli_args=[uri], env=Environment())
        response = downloader.get_raw_response()
        stream = BufferedPrettyStream(
            msg=response,
            conversion=Conversion(downloader.args),
            formatting=Formatting(downloader.args),
        )
        assert stream.mime == expected

# Generated at 2022-06-13 22:14:28.341175
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(
        b'HTTP/1.1 200 OK\r\n'
        b'Content-Type: application/json\r\n'
        b'Date: Mon, 13 Jan 2020 16:55:48 GMT\r\n'
        b'Server: Apache/2.4.29\r\n'
        b'Vary: Accept-Encoding\r\n'
        b'Transfer-Encoding: chunked\r\n'
        b'\r\n'
        b'{"statement": "SELECT * FROM accounts"}')
    conversion = Conversion.get_default_converter_map(verbose_json=False)
    formatting = Formatting.get_default_formatter_map()
    stream = PrettyStream(msg, conversion=conversion, formatting=formatting)

# Generated at 2022-06-13 22:14:32.535324
# Unit test for constructor of class RawStream
def test_RawStream():
    L = RawStream(msg=HTTPMessage(b'HTTP/1.1 200 OK'))
    assert L.msg == HTTPMessage(b'HTTP/1.1 200 OK')
    assert L.with_headers == True
    assert L.with_body == True



# Generated at 2022-06-13 22:14:42.331016
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(headers=dict(a='1', b='2'), body='abcdef')
    raw_stream = RawStream(msg, with_headers=False, with_body=True)
    body_stream = raw_stream.iter_body()
    assert next(body_stream) == b'abc'
    assert next(body_stream) == b'def'
    assert next(body_stream) == b''

    raw_stream = RawStream(msg, with_headers=True, with_body=True)
    body_stream = raw_stream.iter_body()
    assert next(body_stream) == b'abc'
    assert next(body_stream) == b'def'
    assert next(body_stream) == b''


# Generated at 2022-06-13 22:14:53.608612
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.models import HTTPMessage
    msg = HTTPMessage(body="line1\nline2\n")
    msg.encoding = 'utf8'
    output_encoding = 'gb2312'
    stream = EncodedStream(msg,
                           output_encoding=output_encoding)
    assert list(stream.iter_body()) == [b"line1\r\n", b"line2\r\n"]
    msg.encoding = 'gb2312'
    stream = EncodedStream(msg,
                           output_encoding=output_encoding)
    assert list(stream.iter_body()) == [b"line1\r\n", b"line2\r\n"]
    msg.encoding = 'utf8'
    output_encoding = 'utf8'
    stream

# Generated at 2022-06-13 22:15:01.667742
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import os
    import re
    path = os.path.dirname(os.path.abspath(__file__))

    import json
    import httpie.output
    def test_iter_body(self):
        """
        Test iter_body method of class PrettyStream using
        chunks of size 1 in order to make the test independent of the size
        of the chunk
        :param self:
        :return:
        """
        # Get the iterator from file
        with open(path+'/test.txt', 'r') as f_in:
            iterator_from_file = f_in.readlines()

        pretty_stream = PrettyStream(None, None, None, False, False)
        pretty_stream.msg = httpie.output.processing.HTTPMessage()
        pretty_stream.output_encoding = 'utf8'

# Generated at 2022-06-13 22:15:10.087764
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    expected_result = []
    http_msg = {'headers': 'header1 : value1\nheader2 : value2'}
    http_msg['body'] = b'body'
    http_msg = HTTPMessage(**http_msg)
    http_msg = RawStream(http_msg, with_headers=True, with_body=True)
    result = [q for q in http_msg.iter_body()]
    expected_result = [b'b', b'o', b'd', b'y']
    assert result == expected_result


# Generated at 2022-06-13 22:15:10.645402
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    pass

# Generated at 2022-06-13 22:15:35.786663
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage(headers='header: value')
    stream = PrettyStream(msg, with_headers=True, with_body=False, conversion=None,
                          formatting=Formatting(colors=False))
    headers = stream.get_headers()
    assert headers == b'header: value'



# Generated at 2022-06-13 22:15:44.488251
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    test_msg = HTTPMessage(
    b'HTTP/1.0 200 OK\r\n'
    b'Content-Type: application/json\r\n'
    b'\r\n'
    b'{"foo": "bar"}'
    )
    prettystream = BufferedPrettyStream(
        msg=test_msg,
        with_headers=True,
        with_body=True,
        conversion=Conversion('auto'),
        formatting=Formatting('pygments')
        )
    body = b''.join(prettystream.iter_body())
    assert body == b'{\n    "foo": "bar"\n}\n'



# Generated at 2022-06-13 22:15:45.556615
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    pass

# Generated at 2022-06-13 22:15:52.695971
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    raw_stream = RawStream(msg=HTTPMessage(), with_headers=True, with_body=True)
    pretty_stream = PrettyStream(msg=HTTPMessage(), with_headers=True, with_body=True)
    buffered_pretty_stream = BufferedPrettyStream(msg=HTTPMessage(), with_headers=True, with_body=True)

    assert raw_stream != pretty_stream != buffered_pretty_stream

# Generated at 2022-06-13 22:15:55.906076
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    conv = Conversion()
    formatting = Formatting()
    ps = PrettyStream(msg=HTTPMessage(), conversion=conv, formatting=formatting)
    
    src = "Hello, 世界!\n"
    dst = ps.process_body(src)
    assert dst == "Hello, 世界!\n".encode("utf-8", "replace")

# Generated at 2022-06-13 22:15:58.931268
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # TODO: create unit test
    pass


# Generated at 2022-06-13 22:16:06.836046
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    _msg = HTTPMessage()
    _msg.encoding = 'utf8'
    _msg.content_type = 'text/plain; charset=utf-8'
    _msg.body = "{'data': 'Some JSON'}"

    def pass_through(data):
        return data

    _env = Environment()
    _conversion = Conversion()
    _formatting = Formatting()
    _stream = BufferedPrettyStream(msg=_msg, conversion=_conversion, formatting=_formatting, env=_env, on_body_chunk_downloaded=pass_through)

    _str = next(_stream.iter_body())
    assert isinstance(_str, str)
    assert _str == "{\n    'data': 'Some JSON'\n}"

# Generated at 2022-06-13 22:16:09.833122
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    stream = EncodedStream(msg = HTTPMessage(encoding='utf-8'), with_headers=False, with_body=True)
    generator = stream.iter_body()
    print(list(generator))

# Generated at 2022-06-13 22:16:17.446051
# Unit test for constructor of class RawStream
def test_RawStream():
    response = HTTPMessage()
    response.headers = "HTTP/1.1 200 OK\r\n"
    response.body = b"Hello!"
    response.content_type = "text/html; encoding=utf-8"
    stream = RawStream(response)
    response.headers = "HTTP/1.1 200 OK\r\n"
    response.body = b"Hello!"
    response.content_type = "text/html; encoding=utf-8"
    stream = RawStream(response, chunk_size=2)
    response.headers = "HTTP/1.1 200 OK\r\n"
    response.body = "Hello!"
    response.content_type = "text/html; encoding=utf-8"
    stream = RawStream(response, with_headers=False)

# Generated at 2022-06-13 22:16:36.795976
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    env = Environment()
    msg = HTTPMessage(headers=[('Accept-Encoding', 'utf8')],
                      encoding='utf8')
    # Case 1: stdout_isatty is False, encoding is None
    env.stdout_isatty = False
    msg.encoding = None
    output_encoding = 'utf8'
    stream = EncodedStream(msg, env=env)
    assert stream.output_encoding == output_encoding
    # Case 2: stdout_isatty is False, encoding is utf8
    env.stdout_isatty = False
    msg.encoding = 'utf8'
    stream = EncodedStream(msg, env=env)
    assert stream.output_encoding == output_encoding
    # Case 3: stdout_isatty is True
    env

# Generated at 2022-06-13 22:17:18.911167
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    stream = PrettyStream(
        msg=None,
        with_headers=False,
        with_body=False,
        on_body_chunk_downloaded=None,
        conversion=None,
        formatting=None
        )
    assert stream.process_body("test") == b"test"
    assert stream.process_body("test\n") == b"test\n"

# Generated at 2022-06-13 22:17:26.139691
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage()
    msg.parse_headers_and_body(b'{"Test":{"me":"you"}}')
    formatted_stream = PrettyStream(
        msg, True, True, Environment(), None, None)
    iterator = formatted_stream.iter_body()
    res = b''
    for chunk in iterator:
        res += chunk
    assert res == b'{\n    "Test": {\n        "me": "you"\n    }\n}'


# Generated at 2022-06-13 22:17:33.347764
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    headers = '''HTTP/1.1 200 OK
Server: CERN/3.0 libwww/2.17
Content-Type: text/html
Content-Length: 39210
Date: Fri, 13 Feb 1998 23:24:47 GMT
'''
    from httpie.models import Response
    msg = Response(headers, '')
    stream = EncodedStream(msg, on_body_chunk_downloaded=None)
    # assert type(stream.__iter__()) == GeneratorType
    assert b'Server: CERN/3.0 libwww/2.17' in stream.__iter__()
    assert b'Content-Length: 39210' in stream.__iter__()

# Generated at 2022-06-13 22:17:42.564788
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    try:
        PrettyStream(
        msg=HTTPMessage(b'ABCDEF', 'text/plain', content_type='text/plain'),
        conversion=Conversion(),
        formatting=Formatting(None),
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=Callable[[bytes], None])
    except DataSuppressedError as e:
        print(e)
    except BinarySuppressedError as e:
        print(e)


# Generated at 2022-06-13 22:17:50.992401
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import pprint
    def func(http, text):
        stream = PrettyStream(http, Conversion(), Formatting())
        body = ''.join(stream.iter_body())
        return pprint.pformat(body.splitlines())
    import httpie.plugins.builtin.human
    http = httpie.plugins.builtin.human.HumanHTTPResponse()
    # http = httpie.plugins.builtin.human.HumanHTTPRequest()
    base = "HTTP/1.1 200 OK\r\n" \
           "Content-Type: text/plain\r\n" \
           "Content-Length: 40\r\n" \
           "\r\n"
    #############
    base1 = base

# Generated at 2022-06-13 22:17:55.340729
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage('test')
    msg.headers['test'] = 'test'
    stream = PrettyStream(msg, formatting=Formatting(), conversion=Conversion())
    assert stream.get_headers() == b'test: test\n'

# Generated at 2022-06-13 22:17:59.295551
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    msg = HTTPMessage(1, '1', '1', headers = '1')
    stream = RawStream(msg)
    assert stream.iter_body() == b'\x01'


# Generated at 2022-06-13 22:17:59.859800
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    pass

# Generated at 2022-06-13 22:18:08.834838
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie import ExitStatus
    from httpie.cli import http
    from httpie.compat import bytes, str
    from httpie.output import BINARY_SUPPRESSED_NOTICE

    # PrettyStream.iter_body(self: 'PrettyStream[bytes]', content_type: str) -> Iterable[bytes]
    # Zulip API test
    # query=q&q=neil@example.com&limit=10&anchor=0&narrow=[]
    # curl http://127.0.0.1:9991/api/v1/messages -F "q=neil@example.com" -F "limit=10" -F "anchor=0" -F "narrow=[]"
    # {"anchor": 0,
    #  "found_newest": false,
    #  "

# Generated at 2022-06-13 22:18:23.848345
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    import json
    import xml.etree.ElementTree as ET
    from httpie.output.formatters import get_formatter
    from httpie.compat import is_py26

    # Unit test for xml
    chunk = "<html></html>"
    stream = PrettyStream(
        msg=HTTPMessage(headers={'Content-Type': 'application/xml'}),
        with_headers=False,
        with_body=True,
        formatting=get_formatter(output_options={
            "pretty": True,
            "print_body": True,
            "indent": 2
        }),
        conversion=Conversion()
    )
    result = stream.process_body(chunk).decode()
    assert result == '<html></html>'


# Generated at 2022-06-13 22:19:40.837010
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    raw_stream = RawStream(chunk_size=10)
    try:
        print(raw_stream.iter_body())
    except NotImplementedError as e:
        print(e)


# Generated at 2022-06-13 22:19:49.586798
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():

    class MockMsg:
        def __init__(self):
            self.headers = 'a:b\r\nc:d'
            self.encoding = 'utf-8'
            self.chunks = [b'a', b'b', b'c', b'\r\n']

        def iter_body(self, chunk_size):
            for chunk in self.chunks:
                yield chunk

    msg = MockMsg()

    stream = BaseStream(
        msg=msg,
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )

    # for item in iterable:
    #     yield item

# Generated at 2022-06-13 22:19:54.330429
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    test_message = HTTPMessage(headers={"Content-Type":"application/json"})
    test_stream = PrettyStream(msg=test_message)
    assert all(test_stream.get_headers())


# Generated at 2022-06-13 22:20:06.557883
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import HTTPResponse
    from httpie.output.formatters import JSONPrettyFormatter
    from httpie.output.streams import PrettyStream
    import re

    # the object used in this test
    json_pretty_stream = None

    # http message body used in this test

# Generated at 2022-06-13 22:20:07.589556
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    pass


# Generated at 2022-06-13 22:20:18.524630
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class msg(object):
        def iter_body(self,chunk_size):
            body_chunk1 = b'\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00'
            body_chunk2 = b'\xff\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff'
            yield body_chunk1
            yield body_chunk2
    class conversion(object):
        def get_converter(self,mime):
            converter = mime

# Generated at 2022-06-13 22:20:26.751185
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    import httpie.output.streams
    import httpie.compat

    # Since BufferedPrettyStream is a subclass of EncodedStream
    # Three parameters are required to pass
    s = httpie.output.streams.BufferedPrettyStream(
        httpie.compat.BytesIO(),
        httpie.compat.BytesIO(),
        httpie.compat.BytesIO(),
    )
    assert isinstance(s, httpie.output.streams.BufferedPrettyStream)

# Generated at 2022-06-13 22:20:36.532502
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    import json
    from httpie.input import ParseException
    from httpie.models import HTTPRequest
    msg = HTTPRequest('GET', 'http://www.baidu.com', headers={'Accept': 'application/json'},
                    body='test')
    stream = EncodedStream(msg=msg, with_headers=True, with_body=True)
    print(json.loads(b''.join(stream).decode('utf-8')))
    assert stream.output_encoding == 'utf8'
    assert stream.msg == msg
    assert stream.with_headers
    assert stream.with_body


# Generated at 2022-06-13 22:20:49.071208
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class Dummy:
        def __init__(self):
            self.encoding = 'utf-8'
            self.content_type = 'text/plain'
        def iter_body(self, chunk_size):
            yield b'\xa0\xaa'

    encoding = Formatting(None, None, None, 'utf-8')
    conversion = Conversion(None, None)

    # Test for utf-8
    stream = BufferedPrettyStream(Dummy(), encoding=encoding, conversion=conversion)
    assert next(stream.iter_body()) == b'\xc2\xa0\xc2\xaa'

    class Dummy:
        def __init__(self):
            self.encoding = 'utf-8'
            self.content_type = 'application/json'

# Generated at 2022-06-13 22:20:54.590217
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    msg = 'HTTP/1.1 200 OK\r\nContent-Length: 3\r\n\r\nfoo'
    stream = RawStream(HTTPMessage.from_http(msg))
    assert '200' in b''.join(stream)
    assert b'foo' in b''.join(stream)

