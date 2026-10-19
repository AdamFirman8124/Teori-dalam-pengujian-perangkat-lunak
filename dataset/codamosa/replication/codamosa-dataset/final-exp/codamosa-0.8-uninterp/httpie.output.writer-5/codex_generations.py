

# Generated at 2022-06-13 22:23:05.798311
# Unit test for function write_message

# Generated at 2022-06-13 22:23:09.692729
# Unit test for function write_message
def test_write_message():
    assert write_message(
        requests_message='',
        env=Environment(),
        args=argparse.Namespace(),
        with_headers=True,
        with_body=True
    ) == (
        '\n'
    )

# Generated at 2022-06-13 22:23:18.530620
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class MockStream(BaseStream):
        def __init__(self, msgs: list):
            self._msgs = msgs

        def __iter__(self):
            for chunk in self._msgs:
                yield chunk.encode()

    class MockOutfile():
        def __init__(self, arr: list):
            self.arr = arr
            self.encoding = 'utf-8'

        def buffer(self):
            return self

        def write(self, chunk: bytes):
            self.arr.append(chunk.decode(self.encoding))

        def flush(self):
            pass

    arr = []
    outfile = MockOutfile(arr)
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify='colors')

    write

# Generated at 2022-06-13 22:23:29.429317
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import json
    from httpie.input import AuthCredentials
    from httpie import __main__ as httpie
    
    class MockEnv:
        def __init__(self, stdout_isatty, stdout):
            self.stdout_isatty = stdout_isatty
            self.stdout = stdout
    
    class MockArgs:
        def __init__(self, stream, debug, traceback, prettify, style, json, format_options):
            self.stream = stream
            self.debug = debug
            self.traceback = traceback
            self.prettify = prettify
            self.style = style
            self.json = json
            self.format_options = format_options


# Generated at 2022-06-13 22:23:34.362104
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    type_and_kwargs = get_stream_type_and_kwargs()
    assert type_and_kwargs.get('type') == 'httpie.output.streams.EncodedStream'
    assert type_and_kwargs.get('kwargs').keys() == ['env']

# Generated at 2022-06-13 22:23:45.032994
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie import __version__

    from httpie.output.streams import (
        BaseStream, EncodedStream, Formatting, PrettyStream
    )

    from httpie.output.streams import write_stream_with_colors_win_py3

    #
    # Setup.
    #

    encoding = 'utf8'
    bytes = b'\x1b[0m\x1b[4mfoo\x1b[0m'
    colorized_chunk, non_colorized_chunk = (bytes[:8], bytes[8:])
    assert len(colorized_chunk) == len(non_colorized_chunk)
    assert colorized_chunk == colorized_chunk.decode(encoding).encode(encoding)
    assert non_colorized_chunk == non_color

# Generated at 2022-06-13 22:23:58.701676
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import PrettyStream
    from httpie.models import HTTPResponse
    from httpie.compat import is_windows, is_py3
    env = Environment()
    env.stdout_isatty = True
    args = argparse.Namespace()
    args.style = 'monokai'
    args.prettify = {'colors'}
    args.format_options = []
    args.stream = False
    response = requests.Response()
    response.request = requests.Request()
    response.request.method = 'GET'
    response.request.url = 'http://example.com/'
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.status_code = 200
    response.content = 'Hello World!'


# Generated at 2022-06-13 22:24:03.611449
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env = Environment(), args = None);
    assert(stream_class == EncodedStream);
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env = Environment(stdout_isatty = False), args = None);
    assert(stream_class == RawStream);
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env = Environment(), args = argparse.Namespace(prettify = []));
    assert(stream_class == BufferedPrettyStream);
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env = Environment(stdout_isatty = False), args = argparse.Namespace(prettify = []));

# Generated at 2022-06-13 22:24:15.285652
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import requests
    from httpie.cli import parser
    env = Environment()
    args = parser.parse_args()

    # Get stream type if stream is false
    stream_type_1,stream_kwargs_1 = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert(stream_type_1 == EncodedStream)
    assert(stream_kwargs_1 == {'env': env})

    # Get stream type if stream is true
    args.stream = True
    stream_type_2,stream_kwargs_2 = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert(stream_type_2 == PrettyStream)

# Generated at 2022-06-13 22:24:17.897970
# Unit test for function write_stream
def test_write_stream():
    '''Testing write_stream function'''
    write_stream('stream', 'outfile', 'flush')

# Generated at 2022-06-13 22:24:34.410084
# Unit test for function write_message
def test_write_message():
    from httpie.cli import parser
    args = parser.parse_args('https://httpbin.org/get'.split())
    env = Environment()
    with requests.Session() as s:
        resp = s.request('GET', args.url, verify=False,
                         headers=args.headers, auth=args.auth,
                         proxies=args.proxies, timeout=args.timeout)
        write_message(resp, env, args, with_headers=True, with_body=True)


if __name__ == '__main__':
    test_write_message()

# Generated at 2022-06-13 22:24:39.637578
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    result = list(build_output_stream_for_message(
        args=argparse.Namespace(),
        env=Environment(),
        requests_message=requests.Response(),
        with_headers=False,
        with_body=False,
    ))
    assert result == []

# Generated at 2022-06-13 22:24:49.883293
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # use argparse.Namespace to simulate argument parser like object
    args = argparse.Namespace(with_body=True, with_headers=True,
    stream=False, prettify=False, debug=False, traceback=False)
    env = Environment(
        stdin=io.BytesIO(b'{"name": "httpie"}'),
        stdin_isatty=True,
        stdout=io.BytesIO(),
        stdout_isatty=True,
        stderr=io.BytesIO(),
        stderr_isatty=True,
    )

    # Test on RawStream
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert(stream_class == RawStream)

# Generated at 2022-06-13 22:25:01.972745
# Unit test for function write_message
def test_write_message():
    # args.prettify=False, args.stream=False, env.stdout_isatty=True, with_headers=True, with_body=True
    # RawStream
    with pytest.raises(IOError):
        write_message(requests.PreparedRequest(), Environment(debug=False, traceback=False), argparse.Namespace(prettify=[], stream=False))

    # args.prettify=['colors'], args.stream=True, env.stdout_isatty=True, with_headers=True, with_body=True
    # PrettyStream

    # args.prettify=['colors'], args.stream=False, env.stdout_isatty=True, with_headers=True, with_body=True
    # BufferedPrettyStream

    # args.prettify=

# Generated at 2022-06-13 22:25:12.700835
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import StringIO
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import EncodedStream
    from httpie.output.streams import RawStream
    import argparse
    from httpie.cli import Environment
    from httpie.models import HTTPRequest
    from httpie.models import HTTPResponse
    import requests

    # Precondition: terminal is not a tty
    args = argparse.Namespace()
    env = Environment()
    env.stdout_isatty = False

    # Precondition: no prettify
    args.prettify = False

    # Precondition: request, not response
    request = requests.PreparedRequest()

# Generated at 2022-06-13 22:25:13.588118
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    pass

# Generated at 2022-06-13 22:25:25.032015
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import io
    import time
    import threading
    from httpie.core import main as httpie

    (out, err) = io.StringIO(), io.StringIO()
    stdin = io.TextIOWrapper(io.BytesIO(b'hello'), encoding='utf-8')
    env = Environment(stdin=stdin, stdout=out, stderr=err)
    args = argparse.Namespace(prettify=['colors'], style='windows', stream=False)

    # mock requests.Response
    class Response:
        pass
    response = Response()
    response.headers = {'content-type': 'application/json'}
    response.raw = io.BytesIO(b'{"message": "Hello World!"}')
    response.status_code = 200

    # build_

# Generated at 2022-06-13 22:25:36.440951
# Unit test for function write_stream
def test_write_stream():
    import io
    class Stream(io.BytesIO):
        def __init__(self, *args, **kwargs):
            io.BytesIO.__init__(self, *args, **kwargs)
        def __iter__(self):
            return self
        def __next__(self):
            return self.read()

    requests_message = requests.Response()
    environment = Environment()
    args = argparse.Namespace(
        prettify=['colors'],
        stream=False
    )

# Generated at 2022-06-13 22:25:49.956920
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    # example for stream
    stream = [b"\x1b[35mHTTP/1.1 200 OK\x1b[0m", b"asd", MESSAGE_SEPARATOR_BYTES]
    # example for args
    args = argparse.Namespace()
    # example for env
    env = Environment()

    # test 1
    # args.stream = False
    args.stream = False
    # env.stdout_isatty = False
    env.stdout_isatty = False
    # use StringIO to redirect stdout
    stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = stdout

# Generated at 2022-06-13 22:25:51.968181
# Unit test for function write_message
def test_write_message():
    assert write_message('test_write_message', '', '', '') is None

# Generated at 2022-06-13 22:26:05.631977
# Unit test for function write_message
def test_write_message():
    import io
    from httpie.context import Environment

    env = Environment(
        stdin=io.BytesIO(),
        stdout=io.BytesIO(),
        stderr=io.BytesIO()
    )
    args = argparse.Namespace()
    message = 'Hello world!'
    requests_message = type('Message', (object,), {'content': message})()
    write_message(requests_message, env, args)
    assert env.stdout.getvalue() == message

# Generated at 2022-06-13 22:26:14.246676
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # Reset the output
    sys.stdout = sys.__stdout__
    # Prepare a test output stream
    class TestFileIO(io.TextIOWrapper):
        def __init__(self, file):
            self.file = file
            self.encoding = 'utf-8'
            super().__init__(file, self.encoding)
    
        def write(self, str):
            pass
    test_out = TestFileIO(io.BytesIO())
    # The class to be tested
    from httpie.output.streams import write_stream_with_colors_win_py3
    # Test case 1: output with colors
    write_stream_with_colors_win_py3(PrettyStream(content_type='text/plain'), test_out, False)
    # Test case 2: output without

# Generated at 2022-06-13 22:26:18.520280
# Unit test for function write_stream
def test_write_stream():
    import pytest
    from io import StringIO

    f = StringIO()
    write_stream(["put","get"], f, True)

    f.seek(0)
    assert f.read() == "putget"

# Generated at 2022-06-13 22:26:25.789001
# Unit test for function write_message
def test_write_message():
    args = argparse.Namespace()
    env = Environment()
    requests_message = requests.Request()
    requests_message.url = 'http://www.google.com'
    requests_message.method = 'get'
    requests_message.body = '12345'
    requests_message.headers = {'content-type': 'text'}
    with_headers = True
    with_body = True

    write_message(requests_message, env, args, True, True)

# Generated at 2022-06-13 22:26:28.887293
# Unit test for function write_stream
def test_write_stream():
    env = Environment(
        stdout_isatty=True
    )
    args = argparse.Namespace(
        prettify=[],
        colors=[]
    )
    with open('test.txt', 'r+') as f:
        write_stream(
            requests_message=None,
            env=env,
            args=args,
            with_headers=False,
            with_body=False
        )

# Generated at 2022-06-13 22:26:29.693020
# Unit test for function write_message
def test_write_message():
    assert True

# Generated at 2022-06-13 22:26:39.647552
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    print("")
    print("--- Stream type & kwargs test ---")
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=(), stream=True, style='pretty')
    result = get_stream_type_and_kwargs(env, args)
    print("Result")
    print(result)
    assert(result == (PrettyStream, {'env': env, 'conversion': Conversion(), 'formatting': Formatting(env=env, groups=(), color_scheme='pretty', explicit_json=False, format_options={})}))

# Generated at 2022-06-13 22:26:52.984528
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    args = parser.parse_args(['--print=h'])
    from httpie.models import HTTPRequest
    from httpie.output.streams import PrettyStream

# Generated at 2022-06-13 22:27:05.070485
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import httpie
    import sys
    import requests
    from httpie.cli import parser
    from httpie.client import Client
    from httpie.context import Environment
    from httpie.output.streams import RawStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import EncodedStream

    env = Environment(
        stdin=getattr(sys.stdin, 'buffer', sys.stdin),
        stdout=getattr(sys.stdout, 'buffer', sys.stdout),
        stderr=getattr(sys.stderr, 'buffer', sys.stderr),
    )
    args = parser.parse_args(args=['--stream'], env=env)

# Generated at 2022-06-13 22:27:17.384686
# Unit test for function write_message
def test_write_message():
    from httpie.cli.parser import parser

    args = parser.parse_args(['--download', '/'])
    env = Environment(colors=256, stdin=sys.stdin,
                      stdout=sys.stdout, stderr=sys.stderr)
    request = requests.Request('GET', 'http://httpbin.org/')
    prep = request.prepare()
    resp = requests.Response()
    resp.status_code = 200
    resp.raw = BytesIO(b'HTTPbin is here')
    write_message(prep, env, args, with_headers=True, with_body=True)
    write_message(resp, env, args, with_headers=True, with_body=True)

# Generated at 2022-06-13 22:27:33.786388
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    args.prettify = 'all'
    args.stream = True
    args.style = 'paraiso-dark'
    args.json = True
    args.format_options = ['']
    args.download = True
    args.output = True
    (stream_class, stream_kwargs) = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert stream_class == PrettyStream
    assert stream_kwargs['env'] == env
    assert stream_kwargs['conversion']
    assert stream_kwargs['formatting'].env == env
    assert stream_kwargs['formatting'].groups == 'all'

# Generated at 2022-06-13 22:27:45.471174
# Unit test for function write_message
def test_write_message():
    from click.testing import CliRunner
    from httpie.cli import main

    args = ['GET', 'http://httpbin.org/get']

    cli = CliRunner()
    result = cli.invoke(main, args)

    assert result.exit_code == ExitStatus.OK

# Generated at 2022-06-13 22:27:52.371487
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """
    testing the function get_stream_type_and_kwargs
    """
    from httpie.context import Environment
    from httpie.cli.argtypes import KeyValueArg
    from httpie.models import KeyValue
    # test for raw stream
    env = Environment(stdout_isatty=False, stdin_isatty=True)
    args = argparse.Namespace(stream=False, prettify=[],
                              style='default', json=False, format_options=[], download=None)
    assert get_stream_type_and_kwargs(
            env=env,
            args=args) == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE})
    # test for pretty stream

# Generated at 2022-06-13 22:28:02.129260
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import DEFAULT_CHUNK_SIZE
    from httpie.output.streams import RawStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import EncodedStream

    # Test for non-tty with no arg --prettify
    env = Environment(stdin=True, stdin_isatty=True,
                      stdout=True, stdout_isatty=False,
                      stderr=True, stderr_isatty=True,
                      is_windows=False,
                      colors=256,
                      encoding='utf8')
    args = argparse.Namespace(prettify=False,
                              stream=False,
                              json=False,
                              style=None,
                              format_options=None)
    stream

# Generated at 2022-06-13 22:28:14.083015
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args_prettify = argparse.Namespace(prettify='all')
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args_prettify)
    assert stream_class is BufferedPrettyStream
    assert len(stream_kwargs) == 3

    args_json = argparse.Namespace(prettify='body', json=True)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args_json)
    assert stream_class is PrettyStream
    assert len(stream_kwargs) == 3

    args_raw = argparse.Namespace(prettify='')
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args_raw)
    assert stream

# Generated at 2022-06-13 22:28:17.480522
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # Python 3
    stream = EncodedStream(
        msg=HTTPRequest(requests.PreparedRequest()),
        with_headers=True,
        with_body=True,
        env=Environment()
    )
    # BytesIO
    outfile = io.BytesIO()
    write_stream_with_colors_win_py3(stream, outfile, False)


# Generated at 2022-06-13 22:28:29.043252
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import sys
    import unittest

    import httpie

    class TestOutput(unittest.TestCase):

        def setUp(self):
            self.outfile = io.StringIO()

        def tearDown(self):
            self.outfile.close()

        def test_write_stream_with_colors_win_py3(self):
            from httpie.output.streams import (
                BaseStream, RawStream, UnicodeStream,
                write_stream_with_colors_win_py3,
            )
            # Set up some values to be used in any test.
            stream_kwargs = {'stream': None, 'outfile': self.outfile,
                             'flush': True}

            # Test with RawStream.
            stream_class = RawStream

# Generated at 2022-06-13 22:28:36.086469
# Unit test for function write_message
def test_write_message():
    stdout_isatty: False
    class Environment():
        stdout_isatty = False
        stdout = StringIO()
        stderr = StringIO()
        json = None
        is_windows = False

    class Namespace():
        stream = None
        output_file = None
        debug = None
        traceback = None
        chunked = None
        download = None
        output_dir = None
        download_in = None
        download_out = None
        print_body = None
        verbose = None
        pretty = None
        headers = None
        style = None
        output_options = None
        output_options_overrides = None
        download_resume = None

    class StringIO(IO):
        def __init__(self):
            self.buffer = list()

# Generated at 2022-06-13 22:28:48.151103
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():  # pragma: no cover
    import io
    import sys

    class Stream(bytes):
        def __iter__(self):
            yield self

    stream = Stream(b'\x1b[31mfoo\x1b[0m')
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=outfile,
        flush=False,
    )
    assert outfile.getvalue() == '\x1b[31mfoo\x1b[0m'

    # Write directly to sys.stdout.
    for c in stream:
        sys.stdout.buffer.write(c)

# Generated at 2022-06-13 22:28:57.940955
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    from httpie.output.streams import EncodedStream, PrettyStream, BufferedPrettyStream, RawStream
    env = Environment(stdout_isatty=False, colors=256, stdout_encoding='utf-8')
    args = argparse.Namespace()
    args.prettify = []
    args.stream = False
    args__default = argparse.Namespace()


# Generated at 2022-06-13 22:29:19.182466
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Testing write_stream function to write for windows
    with python 3 and colored output"""
    from httpie.output import streams
    import io
    import sys

    out = io.StringIO()

    def get_outfile(out):
        """Return stdout if sys.stdout.isatty is True else out"""
        if sys.stdout.isatty():
            return sys.stdout
        else:
            return out


# Generated at 2022-06-13 22:29:28.014993
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    class TestEnv:
        def __init__(self):
            self.stdout_isatty = True
            self.stderr = sys.stderr
    env = TestEnv()

    args = argparse.Namespace(json=False)
    buf = io.BytesIO()
    req = requests.Request('GET', 'https://httpbin.org/get')
    prepared = req.prepare()
    write_message(
        prepared,
        env,
        args,
        with_headers=True,
        with_body=True,
    )
    response = requests.Response()
    response.status_code = 200
    response.encoding = 'UTF-8'
    response._content = b'{"args":{}}'

# Generated at 2022-06-13 22:29:30.317320
# Unit test for function write_message
def test_write_message():
    assert write_message(requests_message=1, env=1, args=1, with_headers=True, with_body=True) == None

# Generated at 2022-06-13 22:29:38.934173
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class DummyEnv:
        is_windows = True
    class DummyTextIO:
        def __init__(self):
            self.buf = []
        def write(self, text):
            self.buf.append(text)
        def flush(self):
            pass
        def __getattr__(self, name):
            return self
    env = DummyEnv()
    outfile = DummyTextIO()
    flush = True

    write_stream_with_colors_win_py3(
        stream=[b'\x1b[31mred', b'\x1b[0mreset', b'\x1b[1mbold\x1b[0m'],
        outfile=outfile,
        flush=flush
    )


# Generated at 2022-06-13 22:29:48.598064
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from unittest import mock
    from httpie.output.streams import BaseStream
    stream_mock = mock.Mock(spec=BaseStream)
    outfile_mock = mock.MagicMock(encoding="UTF-8")
    outfile_mock.buffer = mock.MagicMock()
    chunk_mock_1 = mock.MagicMock()
    chunk_mock_1.__contains__.return_value = True
    chunk_mock_2 = mock.MagicMock()
    chunk_mock_2.__contains__.return_value = False
    stream_mock.__iter__.return_value = iter([chunk_mock_1, chunk_mock_2])

# Generated at 2022-06-13 22:29:56.950995
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert(get_stream_type_and_kwargs(env=Environment(), args=argparse.Namespace(prettify="all", stream=False, json=False, style="solarized")) == 
           (BufferedPrettyStream, {'env': Environment(), 'conversion': Conversion(), 'formatting': Formatting(env=Environment(), groups='all', 
           color_scheme='solarized', explicit_json=False, format_options={})}))

# Generated at 2022-06-13 22:30:07.194501
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """
    Test the get_stream_type_and_kwargs function on the following scenarios:
    1. pretty output on terminal
    2. pretty output in a file
    3. normal output on terminal
    4. normal output in a file
    """
    
    # Create a fake environment
    env = MagicMock()
    env.stdout_isatty = True

    # Test pretty output on terminal
    args = MagicMock(pretty=['colors'], stream=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert(stream_class == PrettyStream)
    assert(len(stream_kwargs) == 2)
    assert(stream_kwargs["env"] == env)

    # Test pretty output in a file

# Generated at 2022-06-13 22:30:20.489203
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from . import main
    from . import plugins
    from .compat import str, bytes
    from .output.streams import (
        BaseStream, BufferedPrettyStream, RawStream, EncodedStream,
    )
    from .plugins import FormatterPlugin, ConverterPlugin
    from .output.processing import Conversion, Formatting
    from .models import HTTPRequest, HTTPResponse
    from httpie import ExitStatus
    import requests

    class MockPlugin(FormatterPlugin, ConverterPlugin):
        def __init__(self):
            pass

    class MockParser:
        def __init__(self, class_name):
            self.prog = class_name

    class MockEnvironment:

        # Boolean indicating if stdout is a TTY or file.
        # If False, both -p and -r are ignored
        stdout_isat

# Generated at 2022-06-13 22:30:28.122268
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    args = parser.parse_args([])
    from httpie.context import Environment
    env = Environment(stdout_isatty=True, stdin_isatty=False,
                      stdout=sys.stdout, stdin=sys.stdin,
                      stdin_path=None, stdout_path=None,
                      output_options=None, request_data=None,
                      output_file_path=None,
                      session=None,
                      stdout_bytes_written=0,
                      is_windows=False)
    from httpie.output.streams import RawStream, BufferedPrettyStream
    with requests.Session() as session:
        response = session.get('http://httpbin.org/get')
    stream_class, stream_kwargs = get_stream_type_and_

# Generated at 2022-06-13 22:30:40.318263
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace()
    args.stream = False
    args.style = None
    args.style = ''
    args.prettify = ['colors']
    args.format = None
    args.format_options = {}

    env = Environment()
    env.stdout_isatty = True
    env.is_windows = False

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class is BufferedPrettyStream

    env.stdout_isatty = False
    args.stream = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class is RawStream
    assert stream_kwargs.get('chunk_size') == RawStream.CHUNK_

# Generated at 2022-06-13 22:31:04.689968
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest()
    env = Environment()
    args = argparse.Namespace()
    with_headers = False
    with_body = False
    with pytest.warns(None) as record:
        write_message(requests_message, env, args, with_headers, with_body)
    warnings = [r.message for r in record]
    assert warnings == []


# Generated at 2022-06-13 22:31:13.816757
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # Build the test environment
    env = Environment()
    parser = argparse.ArgumentParser(description="httpie")
    parser.add_argument("httpbin_url")
    args = parser.parse_args(["httpbin_url"], env=env)
    
    # Build the test message
    r = requests.get("https://httpbin.org/get?a=b")

    # Build the output

# Generated at 2022-06-13 22:31:22.540030
# Unit test for function write_stream
def test_write_stream():
    # python3
    if sys.version_info >= (3, 0):
        outfile = io.StringIO()
    # python2
    else:
        outfile = io.BytesIO()
    stream = b'b\x1b[1;31m\x1b[K12\x1b[m\x1b[K\n'
    write_stream(stream=stream, outfile=outfile, flush=False)
    assert outfile.getvalue() == b'b\x1b[1;31m\x1b[K12\x1b[m\x1b[K\n'



# Generated at 2022-06-13 22:31:27.906554
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
  env = Environment()
  args = argparse.Namespace(
    prettify = 'all',
    stream = True,
    style = 'colors',
    json = False,
    format_options = {
      'all': None,
      'body': None,
      'headers': None,
    }
  )
  
  print('Test for function get_stream_type_and_kwargs')
  stream_class, stream_kwargs = get_stream_type_and_kwargs(env = env, args = args)
  assert stream_class == PrettyStream, "Something went wrong"

# Generated at 2022-06-13 22:31:39.684684
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    from httpie.argtypes import KeyValueArgType, KeyValueType

    env = Env()
    env.config.update(1, 'output options', {'style': 'default'}, [])
    env.config.update(1, 'prettifiers', {'json': 'python -m json.tool'}, [])
    env.config.update(1, 'output options', {'stream': True}, [])
    env.config.update(1, 'output options', {'pretty': ['all']}, [])
    args = argparse.Namespace()
    args.__setattr__('style', 'default')
    args.__setattr__('prettify', ['all'])
    args.__setattr__('stream', True)
    args.__setattr__('max_redirects', 10)


# Generated at 2022-06-13 22:31:53.411033
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import json
    import platform
    import sys
    import time

    import pytest

    from httpie.compat import is_windows, is_py36
    from httpie.models import Environment, HTTPRequest
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, PrettyStream, RawStream,
    )

    if is_windows:
        pytest.skip("Skipping because platform is Windows")


# Generated at 2022-06-13 22:32:03.668078
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    This test is only relevant for windows and py3.
    """
    # noinspection PyUnresolvedReferences
    import sys
    import os
    import pytest

    is_windows = sys.platform == 'win32'
    is_py3 = sys.version_info[0] == 3

    if not (is_windows and is_py3):
        pytest.skip()

    # noinspection PyUnresolvedReferences
    import msvcrt

    # noinspection PyUnresolvedReferences
    from colorama import Fore, Back, Style
    import six

    from httpie.plugins.builtin import HTTPBasicAuth

    # noinspection PyUnresolvedReferences
    from httpie.output.streams import write_stream_with_colors_win_py3

    auth = HTTPBasicAuth()

# Generated at 2022-06-13 22:32:10.176116
# Unit test for function write_stream
def test_write_stream():
    ###
    # test if write_stream produces the same result as expected_bytes
    ###
    result_bytes = b'foo\nbar\nbaz\n'

    from io import BytesIO
    from httpie.output.streams import RawStream

    stream = RawStream(
        msg=HTTPRequest(
        ),
        with_headers=False,
        with_body=True,
        chunk_size=1
    )

    outfile = BytesIO()

    write_stream(
        stream=stream,
        outfile=outfile,
        flush=True
    )
    
    assert outfile.getvalue() == result_bytes


# Generated at 2022-06-13 22:32:20.549232
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.output.streams import (
        RawStream,
        PrettyStream,
        BufferedPrettyStream,
        EncodedStream,
    )
    import argparse

    parser = argparse.ArgumentParser()
    env = Environment(parser)
    args = parser.parse_args(['-z'])
    args.prettify = ['all']
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env, args=args)
    assert stream_class == PrettyStream

test_get_stream_type_and_kwargs()

# Generated at 2022-06-13 22:32:27.857764
# Unit test for function write_message
def test_write_message():
    a = """{"message":"Successfully created."}"""
    b = """HTTP/1.1 200 OK
Date: Wed, 12 Feb 2020 04:45:09 GMT
Server: gunicorn/19.9.0
Content-Type: application/json
Content-Length: 38
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Content-Type, Authorization
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{"message":"Successfully created."}"""