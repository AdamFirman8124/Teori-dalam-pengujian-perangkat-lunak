

# Generated at 2022-06-13 22:12:30.831745
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.context import Environment
    from httpie.input import ParseError, KeyValue
    from httpie.models import HTTPMessage
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.plugins import plugin_manager
    plugin_manager.discover()
    env = Environment()
    conversion = Conversion(env=env)
    formatting = Formatting(env=env)
    conversion.get_converter('application/json')
    body = b'{"test": "test"}'
    msg = HTTPMessage(headers=KeyValue([]), body=body)
    msg.encoding = 'utf-8'
    msg.content_type = 'application/json'

# Generated at 2022-06-13 22:12:39.266819
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    # Source : https://gist.github.com/wmayner/3695e5c8437c3f9adaa9
    from collections import deque

    class _IterBodyStream(EncodedStream):
        """ A class that behaves like an encoded stream, but is easily
            unit-testable

        """
        def __init__(self, response, **kwargs):
            self.response = response
            super().__init__(msg=None, on_body_chunk_downloaded=None, **kwargs)

        def iter_body(self):
            for line, lf in self.msg.iter_lines(self.CHUNK_SIZE):
                yield line.decode(self.msg.encoding).encode(self.output_encoding, 'replace') + lf

    # Test the stream without 'chunked

# Generated at 2022-06-13 22:12:41.731152
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    if __name__ == "__main__":

        from httpie.models import Response
        from httpie.output.processing import (
            Conversion,
            Formatting,
        )

        body = '{"a": "b"}'
        msg = Response(200, headers={'Content-Type': 'application/json'}, body=body)
        stream = BufferedPrettyStream(msg, conversion=Conversion(), formatting=Formatting())
        body = stream.iter_body()
        next(body)



# Generated at 2022-06-13 22:12:47.596983
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    stream = BufferedPrettyStream(conversion = None, formatting = None, msg = None, with_headers = True, with_body = True, on_body_chunk_downloaded = None)
    assert stream.msg == None
    assert stream.with_headers == True
    assert stream.with_body == True
    assert stream.on_body_chunk_downloaded == None


# Generated at 2022-06-13 22:12:48.537999
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    pass



# Generated at 2022-06-13 22:12:53.436809
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # test short and long responses
    short_msg = HTTPMessage(b'GET', b'/', b'HTTP/1.0', b'', b'', b'Hello!\r\n\r\n')
    long_msg = HTTPMessage(b'GET', b'/', b'HTTP/1.0', b'', b'', b'Hello!\r\n' * 300000)

    # test short and long lines
    short_line_msg = HTTPMessage(b'GET', b'/', b'HTTP/1.0', b'', b'', b'Hello!\r\n\r\n')

# Generated at 2022-06-13 22:12:55.682819
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = EncodedStream(Environment(), chunk_size=100)
    #print(msg)


# Generated at 2022-06-13 22:13:07.272535
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    from httpie.context import Environment
    from httpie.models import HTTPMessage
    from httpie.output.processing import Conversion, Formatting
    from io import BytesIO
    b = BytesIO()
    b.write(b'''
        {"id":1, "name":"john", "id_float":1.2, "id_boolean":true}
    ''')
    b.write(b'\n')
    b.write(b'''{"id":2, "name":"henry", "id_float":2.2, "id_boolean":false}''')
    b.seek(0)
    msg = HTTPMessage()
    msg.headers[b'content-type'] = "application/json"
    msg.body = b
    conversion = Conversion()
    formatting = Formatting()


# Generated at 2022-06-13 22:13:17.318053
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import io
    import json

    msg = HTTPMessage(
        headers={'content-type': 'application/json'},
        encoding='utf8',
        body=io.BytesIO(json.dumps({'msg': 'hello httpie'}).encode('utf8'))
    )

    stream = PrettyStream(
        msg=msg,
        with_headers=False,
        with_body=True,
        conversion=Conversion(),
        formatting=Formatting()
    )

    assert json.loads(next(iter(stream)).decode('utf8')) == {'msg': 'hello httpie'}

# Generated at 2022-06-13 22:13:20.831078
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    message = "{\n\t\"user\": \"John\"\n}\n"
    prettyStream = PrettyStream(Conversion(), Formatting())
    message = prettyStream.process_body(message)
    print(message)
    assert message == b'{\n    "user": "John"\n}\n'

# Generated at 2022-06-13 22:13:39.254804
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    ## Test case 1.
    print("Test case 1")
    mime = "image/png"

# Generated at 2022-06-13 22:13:48.122922
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    class MockMsg():
        def iter_body(self, chunk_size):
            yield 'chunk1'
            yield 'chunk2'
            yield 'chunk3'

        @property
        def content_type(self):
            return 'application/json'

    msg = MockMsg()
    stream = BufferedPrettyStream(msg=msg, conversion=None, formatting=None)
    assert next(stream.iter_body()) == 'chunk1chunk2chunk3'

# Generated at 2022-06-13 22:13:53.523251
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(body=b'a\0\nb')
    stream = EncodedStream(msg=msg, with_headers=False)
    assert list(stream.iter_body()) == [b'a\ufffd\nb']
    stream = EncodedStream(msg=msg, with_headers=False,
                           on_body_chunk_downloaded=lambda chunk: None)
    assert list(stream.iter_body()) == [b'a\ufffd\nb']
    # If a chunk contains a null byte, BinarySuppressedError exception
    # is raised.
    msg = HTTPMessage(body=b'\0')
    stream = EncodedStream(msg=msg, with_headers=False)
    with pytest.raises(BinarySuppressedError):
        stream.iter_body()

# Generated at 2022-06-13 22:14:02.089632
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    http_message = HTTPMessage(
        text='HTTP/1.1 200 OK\r\n'
             'content-type:application/json\r\n'
             'Date:Thu, 20 Dec 2018 16:21:06 GMT\r\n'
             'Server:WSGIServer/0.2 CPython/3.6.6\r\n'
             'X-Frame-Options:SAMEORIGIN\r\n'
             'Content-Length:14\r\n'
             'X-XSS-Protection:1; mode=block\r\n'
             '\r\n'
             '{"description":"OK","status":"200"}'
    )

# Generated at 2022-06-13 22:14:06.000578
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # Given
    class TestStream(EncodedStream):
        def __init__(self):
            super().__init__(
                msg=TestMessage(
                    TestHeaders([TestHeader(name="Content-Type", value="text/html;charset=utf-8")]),
                    TestBody("body")
                ),
                with_headers=True,
                with_body=True,
                on_body_chunk_downloaded=None
            )

    stream = TestStream()
    # When
    headers = stream.get_headers()
    # Then
    assert headers == b'Content-Type: text/html;charset=utf-8\r\n\r\n'



# Generated at 2022-06-13 22:14:19.612051
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    # construct a HTTPDmmonse class
    msg: HTTPMessage = HTTPMessage(
        '{'
        '"method": "POST",'
        '"url": "http://httpbin.org/post",'
        '"data": "",'
        '"headers": {'
        '    "Content-Type": "application/json"'
        '}'
        '}',
        'POST http://httpbin.org/post HTTP/1.1\n'
        'Content-Type: application/json\n'
        'Content-Length: 0\n'
        'Content-Type: application/json\n'
        '\n'
    )
    # construct a RawStream class
    stream: BaseStream = RawStream(msg)
    assert type(stream) == RawStream

# Generated at 2022-06-13 22:14:24.077674
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    msg = HTTPMessage(headers = 'Header: value', encoding=None)
    stream = EncodedStream(msg)
    assert stream.CHUNK_SIZE == 1
    assert stream.msg == msg
    assert stream.with_headers == True
    assert stream.with_body == True
    assert stream.on_body_chunk_downloaded == None
    assert stream.env == Environment()
    assert stream.output_encoding == 'utf8'


# Generated at 2022-06-13 22:14:35.477039
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # test for a body containing a binary data chunk
    msg = HTTPMessage()
    msg.body = b'foo\0bar'
    ps = PrettyStream(msg)
    with pytest.raises(BinarySuppressedError):
        list(ps.iter_body())

    # test for a body containing a binary data chunk and a converter
    msg = HTTPMessage()
    msg.body = b'foo\0bar'
    ps = PrettyStream(msg)
    converter = ps.conversion.get_converter(ps.mime)
    if converter:
        body = bytearray()
        for line, lf in chain([(msg.body, "\r\n")], msg.iter_lines(1)):
            body.extend(line)
            body.extend(lf)
        converted_

# Generated at 2022-06-13 22:14:36.641809
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
	pass

# Generated at 2022-06-13 22:14:44.322907
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    """Unit test for method iter_body of class BufferedPrettyStream"""
    import io
    import json

    msg = HTTPMessage()
    msg.content_type = 'application/json'
    msg.body = io.StringIO('[1, 2, 3]')

    converted_mime, converted_body = 'text/plain', '[1, 2, 3]'

    def convert_JSON(mime, body):
        return converted_mime, converted_body

    class Conversion:
        def get_converter(self, mime):
            if mime == 'application/json':
                return convert_JSON

    formatting = Formatting(colors=False)

    stream = BufferedPrettyStream(msg, conversion, formatting)
    body = b''.join(stream.iter_body())

# Generated at 2022-06-13 22:15:12.814919
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    def mock_get_converter(mime):
        return None

    class MockFoormatting:
        def format_body(self, content, mime):
            return content

    mock_formatting = MockFoormatting()
    ps = PrettyStream(
        msg=None,
        conversion=None,
        formatting=mock_formatting
    )
    assert ps.process_body(b'foo bar') == b'foo bar'

# Generated at 2022-06-13 22:15:25.736668
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    import io
    import json
    import unittest

    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPMessage
    from httpie.output.base import DataSuppressedError

    class TestCase(unittest.TestCase):

        def _run(self, content_type, body):
            f_headers = io.BytesIO()
            f_body = io.BytesIO()

            msg = HTTPMessage()
            msg.headers = self.headers
            msg.content_type = content_type
            msg.encoding = "utf8"
            msg.body_raw = body


# Generated at 2022-06-13 22:15:29.963251
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    doc = '''\
    <plexml>
        <name>Doe</name>
        <firstname>John</firstname>
    </plexml>
    '''
    msg = HTTPMessage(
        method='GET',
        url='https://example.com',
        headers={'content-type': 'application/xml'},
        body=doc
    )
    stream = RawStream(msg, with_headers=False, with_body=True)
    data = ''.join(stream)
    assert data == doc


# Generated at 2022-06-13 22:15:42.720365
# Unit test for method iter_body of class RawStream

# Generated at 2022-06-13 22:15:45.015711
# Unit test for constructor of class BufferedPrettyStream
def test_BufferedPrettyStream():
    stream = BufferedPrettyStream(None, None, None, None) # type: ignore



# Generated at 2022-06-13 22:15:56.993845
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    from httpie.models import Response
    from io import BytesIO
    from httpie.output.formatters.colors import get_lexer
    from httpie.plugins import plugin_manager

    class DummyResponse(Response):
        def __init__(self):
            super().__init__(
                http_version='1.1',
                status_code=200,
                headers={'content-type':'application/json'},
                body=b'{\n  "test": "passed!"\n}'
                )
            self.encoding = 'utf8'

    class DummyEnvironment:
        def __init__(self):
            self.stdout_isatty = True
            self.stdout_encoding = 'utf8'
            self.stdout = BytesIO()

# Generated at 2022-06-13 22:16:03.603786
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # set up arguments for EncodedStream
    msg = HTTPMessage()
    msg.encoding = 'utf8'
    env = Environment()
    env.stdout_isatty = True
    env.stdout_encoding = 'utf8'
    stream = EncodedStream(msg=msg, env=env)
    eq_(stream.msg.encoding, 'utf8')
    eq_(stream.output_encoding, 'utf8')
    eq_(stream.get_headers(), b'')

# Generated at 2022-06-13 22:16:15.053650
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    env = Environment()
    print(env)
    msg = HTTPMessage(headers='', body='', encoding='utf-8')
    print(msg)
    with_headers = True
    with_body = True
    es = EncodedStream(msg=msg, env=env, with_headers=with_headers, with_body=with_body)
    print(es)
    print('{}\n'.format(es.__dict__))
    print(es.__dict__['msg'].__dict__)
    print(es.__dict__['msg'].__dict__['encoding'])
    print(es.__dict__['msg'].__dict__['body'])
    print(es.__dict__['msg'].__dict__['headers'])

# Generated at 2022-06-13 22:16:32.718685
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import pytest
    from httpie.context import Environment
    from httpie.models import HTTPMessage

    from httpie.output import formats

    env = Environment()
    stream = BufferedPrettyStream(
        HTTPMessage('HTTP/1.1 200 OK',
                    headers={
                        'Content-Type': 'application/json'
                    },
                    body='{"Hello": "World"}'),
        conversion=formats.Conversion(),
        formatting=formats.Formatting(env),
        env=env,
        with_headers=False,
        with_body=True
    )

    body = b''.join(stream.iter_body())


# Generated at 2022-06-13 22:16:38.878662
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # test for isatty
    enc_stream = EncodedStream(
        msg=HTTPMessage(),
        env=Environment(stdout_isatty=True))
    assert enc_stream.output_encoding == 'utf8'
    # test for non-isatty
    enc_stream = EncodedStream(
        msg=HTTPMessage(),
        env=Environment(stdout_isatty=False))
    assert enc_stream.output_encoding == 'utf8'


# Generated at 2022-06-13 22:17:24.551772
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    msg = HTTPMessage(content_type='text/plain')
    msg.encoding = 'utf-8'
    msg.body = 'hello world'.encode(msg.encoding)
    stream = PrettyStream(msg, conversion=None, formatting=Formatting())
    content = b''.join(stream.iter_body())
    assert content == b'hello world'
    msg = HTTPMessage(content_type='text/plain')
    msg.encoding = 'utf-8'
    msg.body = ''
    stream = PrettyStream(msg, conversion=None, formatting=Formatting())
    content = b''.join(stream.iter_body())
    assert content == b''


# Generated at 2022-06-13 22:17:33.621483
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import httpie.cli.main
    import httpie.compat
    import io

    def process_body(self, chunk):
        assert isinstance(chunk, str)
        return chunk.encode(self.output_encoding, 'replace')

    old_process_body = BufferedPrettyStream.process_body
    BufferedPrettyStream.process_body = process_body
    env = Environment()
    env.stdout_isatty = False
    on_body_chunk_downloaded=None
    mime="application/json"
    mime_type={"mime":mime}
    if mime in httpie.cli.main.CONVERTERS_BY_MIME:
        mime_type["mime"]="application/json"

# Generated at 2022-06-13 22:17:47.079890
# Unit test for constructor of class EncodedStream
def test_EncodedStream():
    # test case 1 : when encoding not specified
    # If stdout is not at a terminal, encoding is None
    # stdout_isatty = False
    # stdout_encoding = None
    env = Environment()
    encoding = EncodedStream(env = env, msg = response).output_encoding
    assert encoding == "utf8"

    # If stdout is at terminal, encoding is utf-8 if the terminal encoding
    # is utf-8, otherwise it is the terminal encoding
    # stdout_isatty = True
    # stdout_encoding = "utf8"
    env = Environment()
    env.stdout_encoding = "utf8"
    env.stdout_isatty = True
    encoding = EncodedStream(env = env, msg = response).output_encoding

# Generated at 2022-06-13 22:18:00.168899
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
    import json
    import requests
    import httpie.output

    r = requests.get('https://api.github.com')
    assert r.ok
    env = httpie.output.Environment()
    b = BufferedPrettyStream(msg=r, env=env, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    for line in b.iter_body():
        json_line = json.loads(line.decode('utf8'))
        assert len(json_line) == 1
        assert "current_user_url" in json_line[0].keys()
        assert "authorizations_url" in json_line[0].keys()
        assert "code_search_url" in json_line[0].keys()

# Generated at 2022-06-13 22:18:04.049450
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    # JSON prettified should be formatted in one line
    msg = HTTPMessage(200, [], b'{"key":"value"}')
    prettified_json = PrettyStream(msg, with_body=True).iter_body()
    assert sum(1 for _ in prettified_json) == 1

# Generated at 2022-06-13 22:18:14.835322
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # Type: (None) -> None
    """Write a unit test for method get_headers of class PrettyStream"""

    # Create an HTTPMessage to serve as a response entity
    http_response = HTTPMessage()

    # Set a header in the response entity
    http_response.headers = {'X-Something': 'value'}

    # Create a format stream, testing method get_headers of class PrettyStream
    stream = PrettyStream(
        conversion=Conversion(),
        formatting=Formatting(),
        msg=http_response,
        with_headers=True,
        with_body=True,
        on_body_chunk_downloaded=None
    )

    # Create a set of expected and actual headers

# Generated at 2022-06-13 22:18:17.779545
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(content_type='text/plain', encoding='utf-8')
    stream = EncodedStream(msg=msg,with_headers=True, with_body=True)
    i = stream.iter_body()
    assert isinstance(i, Iterable)
    for chunk in i:
        pass


# Generated at 2022-06-13 22:18:25.633140
# Unit test for method iter_body of class RawStream
def test_RawStream_iter_body():
    test_data = "abcd12345"
    test_obj = HTTPMessage()
    test_obj.body = test_data
    stream = RawStream(msg=test_obj)
    try:
        # This is to simulate the iteration.
        while(True):
            print(next(stream.iter_body()))
    except:
        # Exception is thrown when the no element is present in the list.
        pass


# Generated at 2022-06-13 22:18:37.013449
# Unit test for method iter_body of class EncodedStream
def test_EncodedStream_iter_body():
    msg = HTTPMessage(b'''HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello''')
    assert msg.encoding == 'utf8'
    stream = EncodedStream(msg=msg, env=Environment())
    assert b''.join(stream.iter_body()) == b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'

    # msg = HTTPMessage(b''

# Generated at 2022-06-13 22:18:48.540449
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    # randomly selected message
    http_response = HTTPMessage(
        str.encode('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'),
        None,
    )
    # randomly picked environment
    env = Environment()


    # randomly picked conversion
    conversion = Conversion()
    # randomly picked formatting
    formatting = Formatting()

    # randomly picked with headers
    with_headers = True
    # randomly picked with body
    with_body = True
    # randomly picked on body chunk downloaded
    on_body_chunk_downloaded = None

    # test object

# Generated at 2022-06-13 22:20:08.882260
# Unit test for method __iter__ of class BaseStream
def test_BaseStream___iter__():
    # test BaseStream.__iter__()
    import sys
    import os
    import json
    import pytest
    @pytest.mark.parametrize('kwargs,expected', [
        [dict(with_headers=False, with_body=False), b''],
        [dict(with_headers=True, with_body=False), b'\r\n'],
        [dict(with_headers=False, with_body=True), b''],
        [dict(with_headers=True, with_body=True), b'\r\n\r\n'],
    ])
    def test(kwargs, expected):
        args = dict(
            msg=HTTPMessage(),
        )
        args.update(kwargs)
        stream = BaseStream(**args)

# Generated at 2022-06-13 22:20:11.710978
# Unit test for constructor of class RawStream
def test_RawStream():
    # call constructor of class RawStream, test whether raise error or not.
    with pytest.raises(NotImplementedError):
        RawStream().iter_body()

# Generated at 2022-06-13 22:20:15.531015
# Unit test for constructor of class PrettyStream
def test_PrettyStream():
    PrettyStream(msg=None, with_headers=True,
        with_body=True, on_body_chunk_downloaded=None,
        env=None, conversion=None,
        formatting=None)

# Generated at 2022-06-13 22:20:27.421041
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    from httpie.cli import builtin_headers
    from httpie.output.formatters.pretty import HEADER_TEMPLATE
    from httpie.output.formatters.pretty import Formatter, FormatterImpl
    from httpie.output.formatters.json import JSONJSONFormatter, JSONPrettyFormatter
    from httpie.output.formatters.colors import Colors
    from httpie.compat import urlopen, is_windows
    from httpie.output.streams import PrettyStream
    
    if is_windows:
        # https://github.com/psf/requests/issues/3005
        # On Windows, content type will be read as text/html with encoding=utf-8
        # even if the server specified a different charset in the headers.
        # https://bugs.python.org/issue2939
        return
    

# Generated at 2022-06-13 22:20:39.691781
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    """
    测试PrettyStream()类中方法iter_body()

    用于获取流中的内容并返回
    :return:
    """
    from httpie.models import HTTPMessage, Response
    from httpie import ExitStatus
    from httpie.output.streams import PrettyStream
    from httpie.output.formatters.colors import get_lexer
    from httpie.output.formatters.utils import get_binary_stream
    from httpie.plugins.builtin import HTTPHeaders
    from httpie.compat import urlopen
    from httpie.context import Environment

    url = 'https://httpbin.org/bytes/10'

# Generated at 2022-06-13 22:20:45.416522
# Unit test for method iter_body of class BufferedPrettyStream
def test_BufferedPrettyStream_iter_body():
	messages = [
		HTTPMessage(headers='header1: value1\r\nheader2: value2',body=b'test1\r\ntest2')
	]
	for msg in messages:
		for chunk, done in BufferedPrettyStream(msg).iter_body():
			if done:
				break
			print(chunk)

	mimes = ['text/html']
	for msg in messages:
		for chunk in BufferedPrettyStream(msg,mime=mimes).iter_body():
			print(chunk)

	mimes = ['application/json']
	for msg in messages:
		for chunk in BufferedPrettyStream(msg,mime=mimes).iter_body():
			print(chunk)
	

# Generated at 2022-06-13 22:20:51.257024
# Unit test for method get_headers of class PrettyStream
def test_PrettyStream_get_headers():
    msg = HTTPMessage()
    msg.headers = 'test'
    prettyStream = PrettyStream(msg, Environment(), conversion=None, formatting=None, with_headers=True, with_body=True, on_body_chunk_downloaded=None)
    assert prettyStream.get_headers() == b'test'


# Generated at 2022-06-13 22:20:54.028384
# Unit test for method process_body of class PrettyStream
def test_PrettyStream_process_body():
    # When
    prettyStream = PrettyStream(None,None,None,None,None,None)
    # Then
    assert prettyStream.process_body("test")
    assert prettyStream.process_body(b"test")

# Generated at 2022-06-13 22:20:58.898438
# Unit test for constructor of class RawStream
def test_RawStream():
    a = HTTPMessage(version='1.1', status_code=200, reason='OK', headers=None, body=None, encoding='utf-8')
    c = RawStream(msg=a, chunk_size=1024 * 10)
    assert c.CHUNK_SIZE == 1024 * 10


# Generated at 2022-06-13 22:21:11.996940
# Unit test for method iter_body of class PrettyStream
def test_PrettyStream_iter_body():
    test_str_1="<a href=\"https://www.baidu.com/\">111</a>"
    test_str_2="<a href=\"https://www.baidu.com/\">222</a>"
    test_str_3="<a href=\"https://www.baidu.com/\">333</a>"
    test_str_4="<a href=\"https://www.baidu.com/\">444</a>"
    # test_list=list(map(lambda x:"<a href=\"https://www.baidu.com/\">"+str(x)+"</a>",range(100000)))
    test_list=list(map(lambda x:str(x),range(100000)))
    test_list_len=len(test_list)
    # test_str=('\n'.