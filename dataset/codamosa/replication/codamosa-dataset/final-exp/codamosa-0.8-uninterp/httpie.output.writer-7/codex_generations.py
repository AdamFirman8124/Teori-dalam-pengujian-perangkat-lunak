

# Generated at 2022-06-13 22:23:02.885133
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import json
    from httpie.__main__ import main
    from httpie.cli.parser import parser
    from httpie import ExitStatus

    args = parser.parse_args(args=[
        'https://httpbin.org/get'
    ])


# Generated at 2022-06-13 22:23:11.610814
# Unit test for function write_message
def test_write_message():
    env = {
        "stdout": sys.stdout,
        "stdout_isatty": False,
        "is_windows": True
    }
    args = {
        "prettify": ['all'],
        "stream": False,
        "querystring": [],
        "headers": [],
        "style": [],
        "format_options": [],
        "traceback": False,
        "debug": False
    }

    url = "http://www.example.org"
    r = requests.get(url)
    write_message(r, env, args, with_body=True, with_headers=True)

# Generated at 2022-06-13 22:23:22.982316
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    requests_message = requests.Response()
    requests_message.status_code = 200
    requests_message.raw = b'Test raw content'
    requests_message.url = 'http://test.test'

    env = Environment(colors=256, stdout_isatty=True)
    args = argparse.Namespace(
        stream=False,
        debug=False,
        traceback=False,
        prettify='all',
        style='fancy',
        json=False,
        format_options={}
    )

    write_message(requests_message, env, args, with_headers=True, with_body=True)



# Generated at 2022-06-13 22:23:31.140175
# Unit test for function write_message
def test_write_message():
    from httpie.context import Environment
    from httpie.plugins import builtin
    from httpie.cli import get_parser
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.output.streams import PrettyStream
    import sys
    import tempfile
    from io import StringIO


# Generated at 2022-06-13 22:23:41.110799
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import sys

    sys.stderr = io.TextIOWrapper(
        io.BytesIO(), encoding="utf8", line_buffering=True
    )

    write_stream_with_colors_win_py3(
        stream=PrettyStream(HTTPRequest({}), with_headers=True, with_body=True,
            conversion=Conversion(), formatting=Formatting(groups=['colors'], color_scheme='./colors.yml')),
        outfile=sys.stderr, flush=True
    )



# Generated at 2022-06-13 22:23:51.226817
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # Test colors
    b = b'\x1b'
    c = b'\x1b[0m'

# Generated at 2022-06-13 22:23:56.644270
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Write the output stream."""
    import io

    outfile = io.TextIOWrapper(io.BytesIO(), encoding="utf-8")
    outfile.write(b'\x1b[33m123\n')
    
    test_stream = BaseStream()
    for chunk in test_stream:
        if b'\x1b[33m' in chunk:
            outfile.write(chunk.decode('utf-8'))

# Generated at 2022-06-13 22:24:06.538733
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.core import main_test as httpie

    class Args:
        stream = False
        prettify = False
        style = None
        json = False
        format_options = None
        trim_http_traceback = True

    class Env:
        is_windows = False
        stdin_isatty = False
        stdout_isatty = False
        stdout_can_display_colors = True
        stderr_isatty = False

    args = Args()
    args.json = True
    env = Env()
    message_class = {
        False: HTTPRequest,
        True: HTTPResponse,
    }[bool(httpie.__version__)]

# Generated at 2022-06-13 22:24:16.759266
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import PrettyStream
    args = argparse.Namespace(prettify=['colors','format','all'],stream=True)
    env = Environment(stdout=sys.stdout,stdout_isatty=True)
    with requests.Session() as s:
        r = s.get('http://httpbin.org/get')
        stream_type, stream_kwargs = get_stream_type_and_kwargs(env=env,args=args)
        assert stream_type==PrettyStream
        assert stream_kwargs
        message_class = {
            requests.PreparedRequest: HTTPRequest,
            requests.Response: HTTPResponse,
        }[type(r)]

# Generated at 2022-06-13 22:24:28.326213
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output import stream as f
    from httpie.compat import is_windows
    from httpie.output.streams import EncodedStream, RawStream, PrettyStream, BufferedPrettyStream

    args = argparse.Namespace()
    env = Environment()
    env.stdout_isatty = True
    env.is_windows = is_windows

    # prettify=True, stream=True
    args.prettify = True
    args.stream = True
    expected_stream_class = PrettyStream
    expected_stream_kwargs = {
        'env': env,
        'conversion': Conversion(),
        'formatting': Formatting(
            env=env,
            groups='colors',
            color_scheme='',
            explicit_json=False,
            format_options={},
        )
    }

# Generated at 2022-06-13 22:24:46.694016
# Unit test for function write_message
def test_write_message():
    class MockArgs:
        def __init__(self):
            self.stream=True
            self.prettify="group"
            self.format_options=None
            self.style=None
            self.debug=False
            self.traceback=False
    class MockEnv:
        def __init__(self):
            self.stdout=None
            self.stderr=None
            self.stdout_isatty=True
            self.is_windows=False
    class MockPreparedRequest:
        def __init__(self):
            self.body=''
            self.headers=''
    class MockResponse:
        def __init__(self):
            self.status_code=None
            self.elapsed=None
            self.headers=''
            self.history=''

# Generated at 2022-06-13 22:24:57.683165
# Unit test for function write_message
def test_write_message():
    requests_message = requests.Response()
    requests_message.status_code = 200
    requests_message.encoding = "utf-8"
    requests_message.headers = {}
    requests_message.content = b"Hello World !!!"

    message_body = requests_message.content
    header_dict = dict(requests_message.headers)
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--verbose', action='store_true', default=False)
    my_parser.add_argument('--stream', action='store_true', default=False)
    my_parser.add_argument('--prettify', type=str, default='')
    my_parser.add_argument('--style', type=str, default='default')

# Generated at 2022-06-13 22:25:00.364746
# Unit test for function write_message
def test_write_message():
    requests_message = requests.Response()
    with stdoutIO() as s:
        write_message(requests_message, Environment(), {}, False, False)
        out = s.getvalue()
    assert out == ""


# Generated at 2022-06-13 22:25:12.217339
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import unittest
    import requests
    import argparse
    from httpie.context import Environment
    class MockEnvironment(Environment):
        def __init__(self):
            return
    class MockArgs():
        def __init__(self):
            self.format_options = []
            self.stdin_isatty = False
            self.stdout_isatty = False
            self.is_windows = True
            self.debug = True
            self.stream = True
            self.prettify = []
            self.style = ""
            self.json = False
            self.traceback = True
    class MockRequest():
        def __init__(self):
            self.body = "A"
            self.headers = {"A": "A"}
            self.url = "https://www.google.com"
            self

# Generated at 2022-06-13 22:25:22.534203
# Unit test for function write_message
def test_write_message():
    class Test_HTTPRequest():
        def __init__(self, url, headers, body, method):
            self.url = url
            self.headers = headers
            self.body = body
            self.method = method

    class Test_HTTPResponse():
        def __init__(self, status_code, headers, content):
            self.status_code = status_code
            self.headers = headers
            self.content = content
        
    class Test_Environment():
        def __init__(self, isatty, stdout):
            self.stdout_isatty = isatty
            self.stdout = stdout
    
    class Test_Namespace():
        def __init__(self, stream, debug):
            self.stream = stream
            self.debug = debug
    

# Generated at 2022-06-13 22:25:35.235301
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.models import Environment
    environment = Environment()

    from httpie import ExitStatus
    class Namespace(object):
        def __init__(self, arg_dict):
            self.__dict__.update(arg_dict)

    # Test case 1: RawStream with chunk size == RawStream.CHUNK_SIZE
    args = Namespace({'stream': False, 'prettify': False, 'style': 'solarized'})
    outfile = io.BytesIO()
    env = Environment(stdout=outfile, stderr=outfile, stdout_isatty=False)
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type == RawStream

# Generated at 2022-06-13 22:25:43.549248
# Unit test for function write_stream
def test_write_stream():
    import pytest
    import sys
    from httpie.output.streams import BufferedPrettyStream

    sys.stdout.isatty = lambda: True
    args = argparse.Namespace(stream=False, prettify=['colors'])
    env = Environment(stdout_isatty=None)
    stream_kwargs = get_stream_type_and_kwargs(env, args)[1]
    stream = BufferedPrettyStream(
        msg=HTTPResponse(requests.Response()), **stream_kwargs)
    with pytest.raises(Exception):
        write_stream(stream.read, 1, flush=True)



# Generated at 2022-06-13 22:25:48.114731
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # TODO: learn how to mock
    class FakeArgs:
        def __init__(self):
            self.method = 'GET'
            self.headers = [['Content-Type', 'application/json']]
            self.prettify = ['colors']
            self.style = 'solarized'

    class FakeEnv:
        def __init__(self):
            self.stdout_isatty = True
            self.stderr = print
            self.stdout = print

    class FakeResponse:
        def __init__(self):
            self.status_code = 200

    args = FakeArgs()
    env = FakeEnv()
    response = FakeResponse()

# Generated at 2022-06-13 22:25:56.920035
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class FakeStream(BaseStream):
        def __init__(self, *chunks):
            self.chunks = chunks
        def __iter__(self):
            return iter(self.chunks)

    class FakeOutfile:
        def __init__(self, encoding):
            self.buffer = FakeBuffer(encoding)
            self.encoding = encoding
        def write(self, s):
            pass

    class FakeBuffer(object):
        def __init__(self, encoding):
            self.encoding = encoding
        def write(self, chunk):
            self.chunk = chunk

    colors = 'gK'
    outfile = FakeOutfile(encoding="utf-8")

# Generated at 2022-06-13 22:26:09.818381
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(
        stdin_isatty=True, stdout_isatty=True, stdout_bytes_written=0)
    args = argparse.Namespace(
        download=False,
        output_file=None,
        json=False,
        pretty=None,
        stream=False,
        style=None,
        traceback=False,
        verify=True,
        verify_all=False,
        verbose=False
    )

    assert get_stream_type_and_kwargs(env, args) == (RawStream, {
        'chunk_size': RawStream.CHUNK_SIZE})

    args.pretty = True


# Generated at 2022-06-13 22:26:27.792050
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.input import ParseResult
    from httpie.output.streams import PrettyStream, BufferedPrettyStream, RawStream, EncodedStream

    env = Environment(stdout_isatty=True)
    args = ParseResult(prettify='all', stream=True, style='implicit', json=False)

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert stream_class is PrettyStream
    assert stream_kwargs == {
        'env': env,
        'conversion': Conversion(),
        'formatting': Formatting(
            env=env,
            groups='all',
            color_scheme='implicit',
            explicit_json=False,
            format_options=None
        )
    }

    args = ParseResult

# Generated at 2022-06-13 22:26:41.114824
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
  """
  Test function build_output_stream_for_message
  """
  import httpie
  import requests
  import tempfile
  import os
  import json

  # get a response object
  # define test url
  url = 'https://github.com/trending' + '?' + 'since=daily'
  # make a request
  s = requests.Session()
  r = s.get(url,
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                                   'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                                   'Chrome/74.0.3729.131 Safari/537.36'},
          timeout = 1)
  # get the response
  response = r.content

  #

# Generated at 2022-06-13 22:26:55.678464
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """Unit test for function get_stream_type_and_kwargs."""
    from httpie.compat import is_windows, isatty

    env = Environment(
        is_windows=is_windows,
        is_reverse_proxy=False,
        stdin_isatty=True,
        stdout_isatty=isatty(sys.stdout),
        stderr_isatty=isatty(sys.stderr),
    )
    args = argparse.Namespace(
        debug=False,
        download=False,
        form=False,
        json=False,
        pretty=True,
        prettify=['colors', 'headers', 'status'],
        style='default',
        traceback=False,
        stream=True,
    )
    assert get_stream_type_

# Generated at 2022-06-13 22:27:00.078802
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    try:
        write_stream_with_colors_win_py3(b'\x1b[31mred\x1b[0m', None, False)
    except AttributeError:
        pass

# Generated at 2022-06-13 22:27:11.842631
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """This function tests get_stream_type_and_kwargs"""

    env = Environment(stdout_isatty=False)
    args = argparse.Namespace(prettify=False)
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size':1})

    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=False)
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env':env})

    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=True)

# Generated at 2022-06-13 22:27:16.464397
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.core import main
    args = main(args=['--pretty=all', 'GET', 'https://httpbin.org/get'])
    write_message(args.session.request, env=args.env, args=args, with_headers=True, with_body=True)

# Generated at 2022-06-13 22:27:28.314808
# Unit test for function write_message
def test_write_message():
    import requests

    # httpie -v GET http://localhost:8080/{foo}
    requests_message = requests.PreparedRequest()
    requests_message.url = 'http://localhost:8080/{foo}'
    requests_message.body = '{"foo": "bar"}'
    requests_message.method = 'GET'
    requests_message.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    env = Environment()
    args = argparse.Namespace()
    args.prettify = ['all']
    args.stream = False
    args.style = 'paraiso-dark'
    args.format_options = ['pretty', 'unicode']


# Generated at 2022-06-13 22:27:34.949560
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    stream = BaseStream()
    stream.output = [b"\x1b[0m\x1b[31mhello\x1b[0m\x1b[31m", b"\x1b[0mworld\x1b[0m"]
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=True)
    assert outfile.getvalue() == "\x1b[0m\x1b[31mhello\x1b[0m\x1b[31m\x1b[0mworld\x1b[0m"

# Generated at 2022-06-13 22:27:46.120732
# Unit test for function write_message
def test_write_message():
    import os
    import requests
    import json
    import unittest
    class TestWriteMessage(unittest.TestCase):
        def test_write_message(self):
            url = 'http://httpbin.org/get'
            header = {'header': 'value'}
            env = Environment()
            args = argparse.Namespace(
                stream=False,
                headers=True,
                body=True,
                json=False,
                download=False,
                pretty=None,
                style=None,
                colors=True,
                formats=[],
                verbose=True,
                traceback=False,
                output_file=None,
                debug=False,
            )

# Generated at 2022-06-13 22:27:52.640767
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import json
    import httpie.cli
    from httpie.cli import parser
    args = parser.parse_args(["--json", "http://localhost:9200/"])
    env = Environment(stdin=None, stdout=None, stderr=None)
    request = json.loads("""{
    "url": "http://localhost:9200/",
    "method": "GET",
    "headers": {
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "User-Agent": "python-requests/2.18.4"
    },
    "cookies": {},
    "body": ""
}""")
    request = convert(request)
    print("json request = ", request)

# Generated at 2022-06-13 22:28:15.882427
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    >>> from io import StringIO
    >>> outfile = StringIO()
    >>> write_stream_with_colors_win_py3(
    ...     stream = [b'foo', b'\\x1b[1;34m', b'bar', b'\\x1b[0m', b'baz'],
    ...     outfile = StringIO(),
    ...     flush = True,
    ... )
    >>> outfile.getvalue()
    'foo\\x1b[1;34mbar\\x1b[0mbaz'
    >>> outfile.close()
    """

# Generated at 2022-06-13 22:28:19.141464
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(Environment(), argparse.Namespace()) == (EncodedStream, {'env': Environment()})

# Generated at 2022-06-13 22:28:30.645369
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import tests.httpie.test_output.test_streams
    import sys
    from httpie.context import Environment
    from httpie.output.streams import PrettyStream, BufferedPrettyStream, RawStream, EncodedStream

    sys.argv = ['http', '--json', '--stream', '--prettify', 'colors', '--style', 'solarized']
    args = tests.httpie.test_output.test_streams.get_args()
    env = Environment()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream
    assert stream_kwargs['env'] == env
    assert stream_kwargs['conversion'].__class__ == Conversion
    assert stream_kwargs['formatting'].__class__ == Format

# Generated at 2022-06-13 22:28:40.508288
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    stream=io.BytesIO()
    outfile=io.StringIO()
    stream.write(b"hello\n")
    stream.write(b"\x1b[3290mcolor\x1b[39m\n")
    stream.seek(0)
    write_stream_with_colors_win_py3(stream,outfile,True)
    outfile.seek(0)
    assert outfile.read() == "hello\ncolor\n"

# Generated at 2022-06-13 22:28:52.936275
# Unit test for function write_stream
def test_write_stream():
    # Streaming response, terminal output
    with requests.Session() as session:
        session.get("https://google.com")
        stream_class, stream_kwargs = get_stream_type_and_kwargs(
            env=Environment(),
            args=argparse.Namespace(format_options={"print_only": 1})
        )
        assert type(stream_kwargs['formatting'].complete_output) == bool
        assert stream_kwargs['formatting'].complete_output is False
        assert type(stream_kwargs['formatting'].stdout_is_tty) == bool
        assert stream_kwargs['formatting'].stdout_is_tty is True
        assert stream_class is PrettyStream
        assert type(stream_kwargs['conversion'].stdout_is_pipe) == bool
        assert stream_kw

# Generated at 2022-06-13 22:29:07.129695
# Unit test for function write_message
def test_write_message():
    '''
        Test for function write_message
    '''
    from httpie.output.streams import PrettyStream
    from httpie.output.formatters.colors import get_style
    from httpie.cli import parser
    from httpie.context import Environment

    args = parser.parse_args(args=[])
    env = Environment()
    style = get_style(color_scheme=args.style,
                      is_windows=env.is_windows,
                      autolocation=True)
    kwargs = {'is_curl':args.curl,
                'styles': style,
                'env': env
                }
    stream = PrettyStream(**kwargs)

# Generated at 2022-06-13 22:29:11.917407
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env='something', args=argparse.Namespace())
    print (f"{stream_class}")
    print (f"{stream_kwargs}")

# Generated at 2022-06-13 22:29:25.411157
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    requests_message = requests.Request("GET", "http://httpbin.org/get")
    requests_message.headers['Accept'] = 'application/json'
    requests_message.headers['User-Agent'] = 'HTTPie'
    requests_message.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    #requests_message.data = 'a=1&b=3'
    print(requests_message.headers)
    print("Requests Message : ", requests_message)
    stream, stream_kwargs = get_stream_type_and_kwargs(None, None)
    print("Stream : ", stream)
    print("Stream Kwargs : ", stream_kwargs)
    #stream_class = {
    #    requests.PreparedRequest: HTTPRequest,
    #    requests.Response:

# Generated at 2022-06-13 22:29:26.112648
# Unit test for function write_message
def test_write_message():
    pass

# Generated at 2022-06-13 22:29:36.809084
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # request_response.request.headers[':method'] = 'GET'
    env = Environment()
    args = argparse.Namespace()
    requests_response = requests.Response()
    requests_response.headers['content-type'] = 'text/html'
    requests_response.url = 'http://www.google.com'
    # requests_response.raw.read = lambda size = None: 'TEXT'
    requests_response._content = b'TEST'
    # requests_response.request.url = 'http://www.google.com'
    # requests_response.request.method = 'GET'
    args.response_writer = 'httpie.output.streams.PrettyStream'

# Generated at 2022-06-13 22:30:12.922663
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    import win_unicode_console
    from httpie.output.streams import write_stream

    outfile = StringIO()
    env = {
        'stdout_isatty': True,
        'is_windows': True,
    }

    def create_stream(msg: str):
        return ('\x1b[33m' + msg.encode() + '\x1b[0m').split(b'')

    write_stream(stream=create_stream('test'), outfile=outfile, flush=False)
    assert outfile.getvalue() == '\x1b[33mtest\x1b[0m'

    outfile = StringIO()

# Generated at 2022-06-13 22:30:13.637544
# Unit test for function write_message
def test_write_message():
    pass

# Generated at 2022-06-13 22:30:24.626217
# Unit test for function write_message
def test_write_message():
    """
    Just run it, it should be OK
    """
    import requests
    import argparse
    from httpie.context import Environment
    from httpie.output.streams import PrettyStream

    class MockOutputStream(PrettyStream):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.write_chunks = []

        def __iter__(self):
            yield b'\n'
            return self

        def write_chunk(self, chunk):
            self.write_chunks.append(chunk)

    class MockEnvironment:
        def __init__(self):
            self.stderr = None
            self.stdout = self.stderr
            self.stdout_isatty = True


# Generated at 2022-06-13 22:30:27.851615
# Unit test for function write_message
def test_write_message():
    """Write message should print message name and version."""
    assert write_message("HTTPie 1.0.2") == "HTTPie 1.0.2"


# Generated at 2022-06-13 22:30:39.545868
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(raw_stdout=False, prettify=False) == (EncodedStream, {'env': Environment()})
    assert get_stream_type_and_kwargs(raw_stdout=True, prettify=False) == (RawStream, {'chunk_size': 8192})
    assert get_stream_type_and_kwargs(raw_stdout=True, prettify=True) == (PrettyStream, {'formatting': Formatting(env=Environment(), groups=None, color_scheme='', explicit_json=False, format_options={}), 'conversion': Conversion(), 'env': Environment()})

# Generated at 2022-06-13 22:30:43.798911
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():

    # RawStream.CHUNK_SIZE_BY_LINE = 1024
    # RawStream.CHUNK_SIZE = 32768
    # PrettyStream.CHUNK_SIZE_BY_LINE = 1024
    # BufferedPrettyStream.CHUNK_SIZE = 32768

    # mock Environment
    env = Environment()
    env.stdout_isatty = True

    # mock Namespace
    args = argparse.Namespace()
    args.prettify = True
    args.stream = True
    args.style = 'random'
    args.json = 'True'
    args.format_options = []

    # RawStream
    env.stdout_isatty = False
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': 1024})
    args.stream

# Generated at 2022-06-13 22:30:54.153683
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.compat import is_windows
    from httpie.output.streams import PrettyStream, RawStream, EncodedStream
    from httpie.output.streams import BufferedPrettyStream

    class Request(object):
        headers = {}

    class Response(object):
        headers = {}

    class Environment(object):
        def __init__(self, stdout_isatty=False, is_windows=False):
            self.stdout_isatty = stdout_isatty
            self.is_windows = is_windows


# Generated at 2022-06-13 22:31:05.478377
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    """
    Test_build_output_stream_for_message to make sure that \r\n is encoded properly
    :return: None
    """

    import sys
    test_args = argparse.Namespace()
    test_args.stream = True
    test_args.prettify = None
    test_args.debug = False
    test_args.traceback = False
    test_args.style = None

    test_env = Environment()
    test_env.stderr = sys.stdout
    test_env.stdout = sys.stdout
    test_env.stdout_isatty = True
    test_env.is_windows = False
    test_env.default_options = {}

    test_response = requests.Response()
    test_response.status_code = 200

# Generated at 2022-06-13 22:31:14.349627
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.compat import is_windows
    from httpie.output import streams
    from httpie.output.streams import (
        BufferedPrettyStream,
        EncodedStream,
        PrettyStream,
        RawStream,
    )
    from httpie.context import Environment
    # Output to file or pipe without --pretty
    env = Environment(stdout_isatty=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=None,
    )
    assert stream_class == RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE}
    env = Environment(stdout_isatty=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs

# Generated at 2022-06-13 22:31:24.800006
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment('test_test_test')
    args = argparse.Namespace()
    args.prettify = ''
    args.stream = ''
    args_prettify_stream = argparse.Namespace()
    args_prettify_stream.prettify = ''
    args_prettify_stream.stream = True
    args_prettify = argparse.Namespace()
    args_prettify.prettify = ''
    args_prettify.stream = False
    args_stream = argparse.Namespace()
    args_stream.stream = True
    args_stream.prettify = ''

# Generated at 2022-06-13 22:32:36.081675
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from requests import Response
    class EnvMock:
        def __init__(self):
            self.stdout_isatty = True
            self.is_windows = False
    class ArgsMock:
        def __init__(self):
            self.prettify = 'headers,colors'
            self.json = 'jq'
            self.style = 'monokai'
            self.stream = True
            self.format_options = {"format": 'auto'}
    class EnvMock2:
        def __init__(self):
            self.stdout_isatty = False
            self.is_windows = False
    env = EnvMock()
    args = ArgsMock()
    env2 = EnvMock2()
    args2 = ArgsMock()
    args2

# Generated at 2022-06-13 22:32:39.978960
# Unit test for function write_stream
def test_write_stream():
    output_stream = [b'hello\r\n', b'world']
    outfile = BytesIO(b'test_content')
    write_stream(output_stream, outfile, True)
    assert outfile.getvalue() == b'hello\r\nworld'

# Generated at 2022-06-13 22:32:44.344263
# Unit test for function write_message
def test_write_message():
    from .http import http
    env = Environment(httpie_version=__version__)
    args = argparse.Namespace(stream=True, prettify={"0":True}, style="")
    write_message(http, env, args, True, True)