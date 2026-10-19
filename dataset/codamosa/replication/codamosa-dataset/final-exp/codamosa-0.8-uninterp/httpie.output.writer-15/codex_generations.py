

# Generated at 2022-06-13 22:22:56.474018
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """test write_stream_with_colors_win_py3
    """
    outfile = StringIO()
    stream = RawStream(msg=HTTPResponse(requests.Response()))
    write_stream_with_colors_win_py3(stream, outfile, True)

# Generated at 2022-06-13 22:23:08.380656
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class MockEnv(object):
        def __init__(self, stdout_isatty):
            self.stdout_isatty = stdout_isatty
    class MockFoo(object):
        pass

    env = MockEnv(True)
    args = MockFoo()
    args.prettify = True
    args.stream = False
    args.style = "foo"
    args.json = False
    args.format_options = None


# Generated at 2022-06-13 22:23:17.759942
# Unit test for function write_message
def test_write_message():
    message_string = 'Request successfully executed'
    message_bytes = bytes(message_string, 'utf-8')
    message_headers = {
        'accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'httpbin.org',
        'User-Agent': 'HTTPie/0.9.9',
    }
    requests_message = requests.PreparedRequest()
    requests_message.body = message_bytes
    requests_message.headers = message_headers
    requests_message.method = 'get'
    requests_message.url = 'http://httpbin.org'

# Generated at 2022-06-13 22:23:26.782896
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import sys, argparse
    args = argparse.Namespace()
    env = Environment(stdout_isatty=True)
    response = requests.Response()
    response.status_code = 200
    response._content = b'Hello World'
    messages = []
    for chunk in build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=response,
        with_headers=True,
        with_body=True,
    ):
        messages.append(chunk)
    assert b'Hello World' in messages[-2]
    assert b'\n\n' in messages[-1]

# Generated at 2022-06-13 22:23:27.730682
# Unit test for function write_message
def test_write_message():
    pass

# Generated at 2022-06-13 22:23:40.135584
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import pytest
    from httpie.input import ParseError
    from httpie.models import HTTPRequest
    from httpie.output import build_output_stream_for_message
    from httpie.output.streams import RawStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.compat import is_windows
    from httpie.utils import get_binary_stream

    class MockEnv(object):
        stdout = get_binary_stream('wb')
        stdout_isatty = True

    http_request = HTTPRequest(headers={
        'Content-Type': 'text/plain',
        'Content-Length': '4',
        'Accept': 'application/json',
    },
    body=b'bla')

    class MockArgs(object):
        stream = True

# Generated at 2022-06-13 22:23:46.883172
# Unit test for function write_message
def test_write_message():
    # Usage:
    # 1. Run `python write_message.py`
    # 2. Open http://httpbin.org/get
    # 3. Press Ctrl-D

    args
    env
    with_headers=True
    with_body=True

    write_message(
        requests_message=requests.Response(200, "OK"),
        env=env,
        args=args,
        with_headers=with_headers,
        with_body=with_body,
    )

# Generated at 2022-06-13 22:23:57.318838
# Unit test for function write_message
def test_write_message():
    from pytest_mock import mock
    from httpie.cli import Environment, parser

    args = parser.parse_args(['-v'])

    env = Environment()

    with mock.patch.object(env.stdout, 'isatty'):
        env.stdout.isatty.return_value = True

    with mock.patch.object(env.stdout, 'buffer'):
        env.stdout.buffer.write.return_value = ''
        import requests
        requests_message = requests.PreparedRequest()
        write_message(requests_message, env, args, True, True)

# Generated at 2022-06-13 22:24:06.762774
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    parser = argparse.ArgumentParser(
        prog='http',
        usage='%(prog)s',
        description='a curl-like application but for HTTP',
        add_help=False,
        allow_abbrev=False,
    )
    parser.add_argument('--headers', dest='prettify',
                                                    action='store_const',
                                                    const=['headers'],
                                                    default=[],
                                                    help='Prettify headers.')
    parser.add_argument('--pretty', dest='prettify',
                                                    default=[],
                                                    action='store_const',
                                                    const=['all'],
                                                    help='Prettify output'
                                                    ' (shortcode: pp).')

# Generated at 2022-06-13 22:24:15.100305
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    args.prettify = None
    args.stream = None
    #for args.prettify == None and args.stream == None
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert stream_class.__name__ == 'BufferedPrettyStream'
    assert stream_kwargs['env'] == env
    assert stream_kwargs['conversion'].__class__.__name__ == "Conversion"
    assert stream_kwargs['formatting'].__class__.__name__ == "Formatting"
    #for args.prettify == 'all' and args.stream == True
    args.prettify = 'all'
    args.stream = True


# Generated at 2022-06-13 22:24:27.813194
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import pytest

    class FakeEnvironment(Environment):
        @property
        def stdout_isatty(self):
            return False

        @property
        def is_windows(self):
            return False

    env = FakeEnvironment()
    args = argparse.Namespace()
    args.stream = False
    args.prettify = False
    args.style = None
    args.json = False
    args.format_options = {}
    args.debug = False
    args.traceback = False

    stream, _ = get_stream_type_and_kwargs(env=env, args=args)
    assert stream == RawStream

    args.stream = True
    stream, _ = get_stream_type_and_kwargs(env=env, args=args)
    assert stream == RawStream

    args.stream = False


# Generated at 2022-06-13 22:24:36.644001
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(prettify=None, stream=False, style='foo')))
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(prettify=['foo'], stream=True, style='foo')))
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(prettify=['foo'], stream=False, style='foo')))
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(prettify=None, stream=True, style='foo')))
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(prettify=['foo'], stream=True, style='foo', json=True)))


# Generated at 2022-06-13 22:24:46.276775
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(colors=256, stdin_isatty=True, stdout_isatty=True)
    args = argparse.Namespace(prettify=['colors'], stream=False, style="paraiso-dark", format_options={})
    assert get_stream_type_and_kwargs(env, args) == (PrettyStream,
                                                     {'env': env, 'conversion': Conversion(),
                                                      'formatting': Formatting(env=env, groups=['colors'],
                                                                               color_scheme="paraiso-dark",
                                                                               explicit_json=False,
                                                                               format_options={})})

# Generated at 2022-06-13 22:24:57.359098
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.core import main
    from httpie.output.streams import PrettyStream
    from httpie.context import Environment
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.plugins.builtin import HTTPBasicAuth
    import requests

    stdin = sys.stdin if sys.stdin.isatty() else open('/dev/null')

# Generated at 2022-06-13 22:25:02.742991
# Unit test for function write_stream
def test_write_stream():
    class Outfile(object):
        def __init__(self):
            self.buffer = []
        def __getattr__(self, attr):
            def func(*args, **kwargs):
                self.buffer.append((attr, args, kwargs))
                return getattr(self, attr)
            return func
    mock_stream = [b'HTTP/1.1 200 OK\r\n', b'content-length: 0\r\n', b'\r\n', b'']
    write_stream(mock_stream, Outfile(), True)
    assert len(mock_stream) == 4

# Generated at 2022-06-13 22:25:13.015314
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import unittest
    import sys
    import argparse
    from httpie.input import ParseArgs
    from httpie import ExitStatus
    from httpie.core import main
    from httpie.core import io as core_io
    from httpie.context import Environment
    from httpie.models import HTTPRequest
    from httpie.downloads import Downloader
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )

    #python -m httpie.core http://httpbin.org/get
    sys.argv = [sys.argv[0], 'http://httpbin.org/get']
    args = ParseArgs()

# Generated at 2022-06-13 22:25:22.882192
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import tempfile
    from httpie.context import Environment
    from httpie.output.streams import PrettyStream, RawStream
    from httpie.output.processing import Conversion, Formatting

    # Test RawStream
    args = argparse.Namespace(stream=False)
    env = Environment(stdout_isatty=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert stream_class == RawStream
    assert stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE

    args.stream = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert stream_class == RawStream

# Generated at 2022-06-13 22:25:26.995243
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    stream_class, stream_kwargs = get_stream_type_and_kwargs(Environment(), argparse.Namespace())
    assert stream_class is EncodedStream

test_get_stream_type_and_kwargs()

# Generated at 2022-06-13 22:25:34.935663
# Unit test for function write_message
def test_write_message():
    message = 'Hello World'
    env = Environment()
    env.stdout_isatty = True
    args = argparse.Namespace()
    args.stream = False
    args.prettify = []
    args.style = None
    args.json = False
    args.format_options = {}
    args.debug = False
    args.traceback = False
    with_headers = False
    with_body= True
    write_message(message, env, args, with_headers, with_body)

# Generated at 2022-06-13 22:25:44.401232
# Unit test for function write_message
def test_write_message():
    import io
    import json
    import requests
    from httpie.context import Environment
    from httpie.cli import parser
    from httpie.output import write_stream
    from httpie.output.streams import RawStream, EncodedStream

    args = parser.parse_args([])
    env = Environment()
    outfile = io.BytesIO()
    # Test for request
    prepped_request = requests.Request('GET', 'http://example.com').prepare()
    write_message(prepped_request, env, args, with_headers=True, with_body=True)
    assert len(prepped_request.body) == 0
    stream = RawStream(msg=prepped_request)
    write_stream(stream=stream, outfile=outfile, flush=False)
    assert len(outfile.getvalue())

# Generated at 2022-06-13 22:25:51.666416
# Unit test for function write_message
def test_write_message():
    write_message(requests.PreparedRequest(), Environment(), argparse.Namespace())

# Generated at 2022-06-13 22:26:07.603971
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import sys
    import json

    class Environment(object):
        stdout_isatty = True

    env = Environment()
    args = {'prettify':'all', 'style':'none', 'stream':False, 'json':False, 'traceback':False, 'debug':False}
    content = b'{"a":1}\n{"b":2}\n'
    r = requests.Request(
        method='GET',
        url='httpbin.org',
        headers={'a': 'b'},
        data=content
    )

    prepped = r.prepare()
    response = requests.Response()
    response.status_code = 200
    response.headers = {'c': 'd', 'Content-Type': 'application/json'}
    response.raw = BytesIO(content)


# Generated at 2022-06-13 22:26:18.587562
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import (
        RawStream, BufferedPrettyStream, EncodedStream,
    )
    from httpie.constants import (
        WIN32_ANSI_PREFIX
    )

    class Env:
        is_windows = False
        stdout_isatty = True

    args = argparse.Namespace(
        download=False,
        json=False,
        prettify=None,
        style='default',
        stream=False,
    )
    cls, kwargs = get_stream_type_and_kwargs(
        env=Env,
        args=args)
    assert cls == EncodedStream
    assert 'env' in kwargs


# Generated at 2022-06-13 22:26:29.065048
# Unit test for function write_message
def test_write_message():

    # test write_message with header 
    assert write_message(
        requests_message = requests.Response(),
        env = Environment(),
        args = argparse.Namespace(),
        with_headers = True,
        with_body = False
    ) is None

    # test write_message with body
    assert write_message(
        requests_message = requests.Response(),
        env = Environment(),
        args = argparse.Namespace(),
        with_headers = False,
        with_body = True
    ) is None

    # test write_message without body and headers
    assert write_message(
        requests_message = requests.Response(),
        env = Environment(),
        args = argparse.Namespace(),
        with_headers = False,
        with_body = False
    ) is None



# Generated at 2022-06-13 22:26:41.674893
# Unit test for function write_message
def test_write_message():
    import os
    import builtins
    import tempfile

    # Mock output function
    open_mock = mock.mock_open()
    builtins.open = open_mock
    # Mock stdout_isatty function
    stdout_isatty_mock = mock.MagicMock()
    # Mock request object
    request_mock = mock.MagicMock()
    # Mock output stream
    chunk_mock = mock.MagicMock()

    # --------------------------------------------------------------
    # Set up unexpected os.isatty return value so we will
    # test a stream other than RawStream
    # --------------------------------------------------------------

    # Store the original return value
    os_isatty_return_value = os.isatty(0)
    # Setup unexpected return value
    os.isatty = mock.MagicMock()


# Generated at 2022-06-13 22:26:56.087636
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    Create a mock stream with a bunch of chunks that should be
    colorized and written to console, and a bunch of raw
    bytes that should be written to stdout.buffer.
    This can only be tested on Windows.
    An IOError will be raised if a step
    fails

    """
    from io import StringIO
    from unittest.mock import patch, MagicMock

    stream_out_stringio = StringIO()
    stream_class = MagicMock()
    stream_instance = MagicMock()

# Generated at 2022-06-13 22:27:07.672993
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import io
    import colorama
    colorama.deinit()

    tty = open('/dev/tty', 'r+')
    fd = tty.fileno()

    env = Environment()
    env.stdout = tty
    env.stdout_isatty = True
    args = argparse.Namespace()


    fcntl.ioctl(fd, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0))

    args.stream = True
    args.prettify = False
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env': env})

    args.prettify = ['headers']

# Generated at 2022-06-13 22:27:10.827029
# Unit test for function write_stream
def test_write_stream():
    stream = RawStream()
    stream.write('hello world')
    output = write_stream(stream = stream)
    print(output)

test_write_stream()

# Generated at 2022-06-13 22:27:15.908395
# Unit test for function write_stream
def test_write_stream():
    with tempfile.NamedTemporaryFile(mode='r+') as temp_file:
        print(temp_file.name)
        write_stream(stream=[b'abc\n'], outfile=temp_file, flush=True)
        temp_file.seek(0)
        ch = temp_file.read()
        assert ch == 'abc\n'


# Generated at 2022-06-13 22:27:28.138394
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    Check the content of the stream (redirected to stdout)
    """
    # prepare input
    class Stream:
        """
        A custom stream to test the function.
        """
        def __init__(self, content_list):
            self.content_list = content_list
            self.index = -1

        def __iter__(self):
            return self

        def __next__(self):
            self.index += 1
            if self.index >= len(self.content_list):
                raise StopIteration
            return self.content_list[self.index]

    stream = Stream(['stream1', 'stream2', 'stream3', '\x1b[0m'])

    # write stream to stdout
    class File:
        """
        A custom file to test the function.
        """

# Generated at 2022-06-13 22:27:51.006814
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import pytest
    from httpie.output.streams import BaseStream
    import io
    import sys

    class WindowsColorStreamMock(BaseStream):
        def __init__(self, **kwargs):
            pass

        def __iter__(self):
            yield b'\x1b[1;36mhello\n\x1b[0m'
            yield b'world'

    if sys.version_info[0] > 2:
        assert write_stream_with_colors_win_py3.__module__ == "httpie.output.streams"
    else:
        pytest.skip("Prefix win_py3 is only for Python 3 running on Windows")

    # No exception raised
    outfile = io.TextIOWrapper(io.BytesIO(), 'UTF-8')
    stream = WindowsColor

# Generated at 2022-06-13 22:27:52.203258
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass


# Generated at 2022-06-13 22:27:53.120789
# Unit test for function write_stream
def test_write_stream():
    print("")

# Generated at 2022-06-13 22:28:01.663765
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.compat import is_windows, is_py3
    from io import StringIO
    test_string = "\033[1m\033[31mRed\033[0m"
    if not is_windows or not is_py3:
        return
    output = StringIO()
    write_stream_with_colors_win_py3(stream=test_string, outfile=output, flush=True)
    assert output.getvalue() == test_string

# Generated at 2022-06-13 22:28:13.734471
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.core import main
    from httpie.output.streams import RawStream
    from httpie.compat import is_windows
    from httpie.constants import DEFAULT_CONFIG_DIR

    # The 1st argument is the absolute path to the calling
    # script. We don't need it, so it is removed.
    sys.argv.pop(0)
    parser = main.get_parser()
    args = parser.parse_args([])
    env = Environment(vars(args), DEFAULT_CONFIG_DIR)

    # The following is the equivalent of
    # http httpie.org
    # If the terminal is not a tty and if --prettify is not specified
    # then the stream class should be RawStream
    env.stdout_isatty = False
    stream_class, stream_kw

# Generated at 2022-06-13 22:28:21.299877
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """Test function get_stream_type_and_kwargs"""
    import io
    import sys
    import pytest
    # import io
    # io.TextIOWrapper
    # io.BufferedWriter
    # io.BufferedRandom
    # import sys
    # sys.__stdout__
    # sys.stdout
    # sys.__stdout__.buffer
    # sys.stdout.buffer
    from httpie.context import Environment
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )

    args = pytest.lazy_fixture('args')
    args.prettify = ('colors',)
    args.style = 'default'
    args.stream = False

# Generated at 2022-06-13 22:28:23.187765
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    pass

# Generated at 2022-06-13 22:28:25.703323
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import sys
    out = sys.stdout
    print(out)
    return 0


# Generated at 2022-06-13 22:28:34.808585
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import PrettyStream
    from httpie.output.utils import write_stream_with_colors_win_py3
    from httpie.models import HTTPRequest
    from httpie.context import Environment
    from httpie.output.base import BaseFormat
    from io import StringIO
    from .utils import MockStream, MockArgsNamespace
    environment = Environment(
        stdout=MockStream(isatty=True),
        stdout_isatty=True
    )

# Generated at 2022-06-13 22:28:47.307260
# Unit test for function write_stream
def test_write_stream():
    from . import TestEnvironment
    from httpie.output.streams import RawStream
    env = TestEnvironment()

    args = argparse.Namespace(
        stream=False,
        colors=False,
        pretty=False,
    )

    # write a stream to stdout
    stream = RawStream(
        msg=HTTPResponse(requests.Response()),
        with_headers=True,
        with_body=True,
    )
    write_stream(
        stream,
        env.stdout,
        flush=env.stdout_isatty or args.stream
    )

# Generated at 2022-06-13 22:29:23.370237
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(stdin_isatty=True, stdout_isatty=True)
    str_args = argparse.Namespace(
        prettify=['all'],
        style='none',
        json=False,
        format_options={},
        stream=True
    )
    assert get_stream_type_and_kwargs(env, str_args)[0] == PrettyStream
    str_args.stream = False
    assert get_stream_type_and_kwargs(env, str_args)[0] == BufferedPrettyStream

    env.stdout_isatty = False
    str_args.stream = True
    assert get_stream_type_and_kwargs(env, str_args)[0] == RawStream
    str_args.stream = False
    assert get_stream_type_and_kw

# Generated at 2022-06-13 22:29:34.247515
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(stream=False, prettify=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert isinstance(stream_class(), EncodedStream)
    assert stream_kwargs == {'env': env}

    env = Environment(stdout_isatty=False)
    args = argparse.Namespace(stream=False, prettify=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert isinstance(stream_class(), RawStream)
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE}

    env = Environment(stdout_isatty=True)

# Generated at 2022-06-13 22:29:42.841784
# Unit test for function write_message
def test_write_message():
    message_separator = '\n\n'
    # Testing if the write_message function is working
    req = requests.PreparedRequest()
    req.prepare_method('GET')
    req.prepare_url('http://google.com', {})
    req.prepare_body([], {})
    env = Environment()
    args = argparse.Namespace()
    assert write_message(req, env, args) == None
    assert write_message(req, env, args, True, True) == None
    assert write_message(req, env, args, True, False) == None
    assert write_message(req, env, args, False, True) == None


# Generated at 2022-06-13 22:29:52.153189
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import tempfile
    outfile = tempfile.TemporaryFile('r+b', -1, tempfile.gettempdir(), 'httpie', 'test', 'suffix')
    stream = PrettyStream(msg=HTTPResponse(), env=Environment(), with_headers=True, with_body=True,
                          conversion=Conversion(), formatting=Formatting(env=Environment(), groups=['all'], color_scheme='monokai', explicit_json=True, format_options=None))
    for chunk in stream:
        if b'\x1b[' in chunk:
            outfile.write(chunk.decode('utf-8'))
        else:
            outfile.buffer.write(chunk)
    outfile.seek(0)
    for line in outfile:
        sys.stdout.write

# Generated at 2022-06-13 22:30:04.405514
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    if sys.platform == 'win32' and sys.version_info.major == 3:
        from io import StringIO
        from httpie.output.streams import ColorizedStream
        outfile = StringIO()
        write_stream_with_colors_win_py3(
            stream=ColorizedStream(
                msg=HTTPRequest(
                    requests.PreparedRequest()
                ),
                with_headers=True,
                with_body=False,
                env=Environment(),
                conversion=Conversion(),
                formatting=Formatting(
                    env=Environment(),
                    groups=['colors'],
                    color_scheme=None,
                    explicit_json=False,
                    format_options={},
                )
            ),
            outfile=outfile,
            flush=False,
        )

# Generated at 2022-06-13 22:30:13.253986
# Unit test for function write_message
def test_write_message():
    from original_code.httpie.output import streams

    # Build arguments
    args = argparse.Namespace()

    str_nag = "Not Accessable Group !"
    args.nag = str_nag
    args.prettify = ["colors", "format", "all", "group1", "group2"]
    args.style = "paraiso-dark"
    args.format_options = ""
    args.print_empty_body = True
    args.json = False

    args.stream = True
    args.debug = True
    args.traceback = True
    #args.download_output = "3"
    # args.traceback = True

    # Build environment
    env = Environment()
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env

# Generated at 2022-06-13 22:30:13.814869
# Unit test for function write_stream
def test_write_stream():
    pass


# Generated at 2022-06-13 22:30:24.691040
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=None,
        args=None
    )
    from httpie import ExitStatus
    from httpie.output.streams import BASE_FORMAT_OPTIONS


# Generated at 2022-06-13 22:30:36.678300
# Unit test for function write_stream
def test_write_stream():
    env = Environment(
        stdout_isatty=True,
        output_options={
            'pretty': 'all',
            'colors': '16m',
            'style': 'paraiso-dark'
        },
        ignore_stdin=True,
        stdin=None,
        output_stream=None,
    )
    args = argparse.Namespace(
        debug=True,
        form=False,
        headers=[],
        idented=True,
        ignore_stdin=[],
        json=False,
        output=None,
        output_dir=None,
        output_file=None,
        prettify=['all'],
        print_body=True,
        stream=True,
    )

# Generated at 2022-06-13 22:30:40.200636
# Unit test for function write_message
def test_write_message():
    http_request = HTTPRequest(requests.PreparedRequest())
    http_response = HTTPResponse(requests.Response())



# Generated at 2022-06-13 22:31:29.399268
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from httpie.documents import Request
    from httpie.output.streams import PrettyStream
    import unittest
    class TestWriteStream(unittest.TestCase):
        def test_write(self):
            stream = PrettyStream(msg=Request(None), with_headers=True, with_body=True, env=None, conversion=None, formatting=None)
            outfile = StringIO()
            outfile.encoding = 'utf-8'
            print(write_stream_with_colors_win_py3(
                stream=stream,
                outfile=outfile,
                flush=True
            ))

    unittest.main()

# Generated at 2022-06-13 22:31:40.260581
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class args:
        prettify = ['colors', 'format', 'headers', 'json']
        stream = False
    class env:
        stdout_isatty = True
    assert get_stream_type_and_kwargs(env, args) == (BufferedPrettyStream, {'conversion': Conversion(), 'env': env, 'formatting': Formatting(env=env, groups=['colors', 'format', 'headers', 'json'], color_scheme='', explicit_json=False, format_options={})})
    args.stream = True

# Generated at 2022-06-13 22:31:47.241933
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import unittest
    env = Environment()
    env.stdout_isatty = False

    stream, kwargs = get_stream_type_and_kwargs(env=env, args=None)
    assert stream == RawStream
    assert kwargs == {'chunk_size': RawStream.CHUNK_SIZE}

# Generated at 2022-06-13 22:31:57.540631
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():

    import re

    class FakeStdout:

        # Use a list as a buffer, to be able to check that
        # the color pattern is written all at once in one
        # call to stdout.write
        _data = []

        def write(self, dat):
            self._data.append(dat)

        def flush(self):
            pass

        def close(self):
            pass

        @property
        def encoding(self):
            return 'utf8'

    stdout_stream = FakeStdout()
    stream = iter(['row-1\n', 'row-2\n', 'row-3\n'])
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=stdout_stream,
        flush=True
    )

    # We expect the pattern

# Generated at 2022-06-13 22:32:07.098345
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """Unit test for function get_stream_type_and_kwargs"""
    from httpie.cli import parser
    from httpie.output.streams import RawStream, BufferedPrettyStream, EncodedStream
    from httpie.output.streams import PrettyStream

    args = parser.parse_args(
        ['--prettify', 'headers', 'https://httpbin.org/get']
    )
    env = Environment()

    (stream, stream_kwargs) = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert stream == PrettyStream
    assert stream_kwargs['conversion'].__class__.__name__ == 'Conversion'
    assert stream_kwargs['formatting'].__class__.__name__ == 'Formatting'
    assert stream_kwargs

# Generated at 2022-06-13 22:32:08.414690
# Unit test for function write_stream
def test_write_stream():
    write_stream(['a','b'], 'a', flush=True)
    write_stream(['a','b'], 'a', flush=False)


# Generated at 2022-06-13 22:32:09.877813
# Unit test for function write_message
def test_write_message():
    assert 1 == 1


# Generated at 2022-06-13 22:32:21.922367
# Unit test for function write_message
def test_write_message():
    class MockEnv():
        is_windows = False
        stdout_isatty = True
        stdout = None
        stderr = None

    class MockArgs():
        stream = True
        debug = False
        traceback = False
        prettify = 'all'
        style = None
        json = False
        format_options = {}

    args = MockArgs()
    env = MockEnv()
    with_headers = True
    with_body = True

    response = requests.Response()
    response.request = requests.PreparedRequest()
    response.url = 'http://www.google.com'
    response.status_code = 200

# Generated at 2022-06-13 22:32:37.022415
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import argparse
    import mock
    import pytest

    from httpie.context import Environment
    from httpie.output.streams import (
        BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.output.processing import Conversion, Formatting

    # Stream type

# Generated at 2022-06-13 22:32:49.540033
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.context import Environment
    from httpie import ExitStatus
    from httpie.exit import _EXIT_STATUSES_TO_BINARY_EXIT_STATUSES
    from httpie.input import ParseError
    from httpie import __version__ as version
    from httpie.compat import is_windows, is_py3
    from httpie.cli.argparser import parser
    from httpie.output.streams import _get_unicode_stream
    from httpie.output.processing import Conversion
    import httpie.exit
    import argparse
    import requests
    import httpie.cli.argparser as argparser
    import httpie.output.streams as streams
    import httpie.output.processing as processing
    import httpie.cli.argtypes as argtypes
    
    args = argparse.Names