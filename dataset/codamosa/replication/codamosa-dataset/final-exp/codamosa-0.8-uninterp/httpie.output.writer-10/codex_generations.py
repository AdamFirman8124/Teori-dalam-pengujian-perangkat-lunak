

# Generated at 2022-06-13 22:23:02.805611
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    from httpie.output.streams import BaseStream
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion
    from httpie.output.processing import Formatting
    from httpie import ExitStatus
    from core import main

    class TestPrettyStream(PrettyStream):
        def __init__(self, body, **kwargs):
            self.body = body

# Generated at 2022-06-13 22:23:13.354889
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import PrettyStream, RawStream
    from httpie.context import Environment
    from httpie import ExitStatus
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPRequest, HTTPResponse
    import io
    import argparse
    import os
    import random

    # Prepare environment
    env = Environment(
        colors=256,
        stdout=io.BytesIO(),
    )
    env.stdout.isatty = lambda: True
    env.stdout.encoding = 'utf-8'

    # Prepare args
    args = argparse.Namespace(
        download=False,
        output_dir=None,
        prettify=['all'],
        style='colourful',
        stream=False,
        format_options=[],
    )

# Generated at 2022-06-13 22:23:26.203719
# Unit test for function write_message
def test_write_message():
    import io
    stdout = io.StringIO()
    args = argparse.Namespace()
    env = Environment()
    env.stdout = stdout
    env.stdout.isatty = True
    requests_message = requests.PreparedRequest()
    requests_message.headers = {}
    requests_message.body = b''
    requests_message.url = 'http://www.google.com/'
    requests_message.method = 'GET'
    requests_message.headers['test'] = 'test'
    write_message(requests_message=requests_message, env=env, args=args, with_body=True, with_headers=True)

# Generated at 2022-06-13 22:23:30.293532
# Unit test for function write_message
def test_write_message():
    kwargs = {
        # "requests_message": sResponse,
        # "with_body": True,
        # "with_headers": True,
    }
    return write_message(**kwargs)

# Generated at 2022-06-13 22:23:31.084209
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    write_message()

# Generated at 2022-06-13 22:23:37.320978
# Unit test for function write_stream
def test_write_stream():
    env = Environment(stdout=io.StringIO())
    args = argparse.Namespace()
    stream = EncodedStream(msg="hi", with_headers=True, with_body=False, env=env)
    write_stream(stream=stream, outfile=env.stdout, flush=False)
    assert env.stdout.getvalue() == 'hi\n'

# Generated at 2022-06-13 22:23:48.808254
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from io import BytesIO
    from httpie.context import Environment
    from httpie.compat import is_windows
    from httpie.output.streams import RawStream
    from httpie.models import HTTPRequest
    from httpie.output import streams
    import pytest
    import sys

    env = Environment(stdin=BytesIO(), stdin_isatty=False)
    env.stdout.line_buffering = False
    env.stdout.isatty = False
    args = argparse.Namespace()
    args.stream = False
    args.prettify = []
    args.style = None
    args.json = False
    args.format_options = []
    args.debug = False
    args.traceback = False

    requests_message = HTTPRequest('GET', 'http://test.com/test')

# Generated at 2022-06-13 22:23:56.878762
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class TestBuf:
        s = ''
        encoding = 'utf-8'
        def write(self, txt):
            TestBuf.s += txt
        def __getattr__(self, name):
            raise AttributeError(name)

    class TestEnv:
        class stdout:
            buffer = TestBuf()

        is_windows = False

    class TestArgs:
        def __init__(self):
            self.prettify = None
            self.stream = False

    # Using a buffer interface (Python 3), and no color
    env = TestEnv()
    args = TestArgs()
    write_stream_with_colors_win_py3(
        stream=b'test',
        outfile=env.stdout,
        flush=False
    )
    assert TestBuf.s

# Generated at 2022-06-13 22:24:06.655516
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import json
    import os
    import sys
    import datetime
    import textwrap

    import pytest
    import requests
    import requests.models
    import requests.status_codes
    import requests.structures
    import requests.packages.urllib3.fields
    from httpie.plugins import plugin_manager
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Formatting
    from httpie.output.formatters import Formatter
    from httpie import models

    class TestException(Exception):
        pass

    class MockEnvironment(object):
        def __init__(self):
            self.colors = 0
            self.stdout = sys.stdout
            self.stdout_isatty = True


# Generated at 2022-06-13 22:24:13.919635
# Unit test for function write_stream
def test_write_stream():
    from io import BytesIO
    from httpie.output.streams import WriteStream, DummyWriteStream


    class TestOutfile:
        def __init__(self):
            self.buf = BytesIO()
            self.x = False
        def write(self, b):
            raise Exception()
        def buffer(self):
            return self

    outfile = TestOutfile()


    def f(stream: WriteStream):
        write_stream(stream, outfile, False)

    f(DummyWriteStream())

    # WriteStream is not implemented yet
    # f(WriteStream)

# Generated at 2022-06-13 22:24:26.892527
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from mock import patch
    from httpie.utils import is_windows, get_windows_terminal_encoding
    from httpie.output.streams import BaseStream
    # Get the encoding for a console on Windows
    from locale import getpreferredencoding
    encoding = getpreferredencoding()
    if not is_windows():
        return

# Generated at 2022-06-13 22:24:27.991829
# Unit test for function write_stream
def test_write_stream():
    pass

# Generated at 2022-06-13 22:24:36.691104
# Unit test for function write_stream
def test_write_stream():
    import io
    from httpie.output.streams import RawStream
    from httpie.context import Environment
    class mock(object):
        def __init__(self, tty):
            self.isatty = tty
    class mock_stdout(object):
        def __init__(self, buf=None):
            self.buf = buf
        def __getattr__(self, attr):
            return getattr(self.buf, attr)

    env = Environment()
    env.stdout = mock_stdout(mock(False))
    env.stderr = mock_stdout(mock(True))
    stream_kwargs = {
        'stream': RawStream(msg='123456', chunk_size=1),
        'outfile': env.stdout,
        'flush': False,
    }

# Generated at 2022-06-13 22:24:43.146592
# Unit test for function write_stream
def test_write_stream():
    from io import BytesIO
    from mock import MagicMock
    stream = EncodedStream()
    outfile = BytesIO()
    stream.__iter__ = MagicMock(return_value = bytes("test","utf-8"))
    write_stream(stream,outfile,False)
    assert outfile.getvalue() == bytes("test","utf-8")
    outfile.close()


# Generated at 2022-06-13 22:24:51.821656
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    Unit test for function write_stream_with_colors_win_py3
    """
    from io import StringIO
    from httpie.output.streams import PrettyStream
    from httpie.output.core import write_stream_with_colors_win_py3
    class FakeEnv(object):
        """
        Fake Env class
        """
        def __init__(self):
            self.is_windows = True
            self.stdout = StringIO()
            self.stdout_isatty = True

    env = FakeEnv()
    stream_class = PrettyStream

# Generated at 2022-06-13 22:25:03.016188
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class MockFile:
        def __init__(self):
            self.text_buffer = ''
            self.bytes_buffer = b''
            self.flush_count = 0

        def write(self, text):
            self.text_buffer += text

        def buffer(self):
            return self
        write = buffer

        def write(self, bytes):
            self.bytes_buffer += bytes

        def flush(self):
            self.flush_count += 1

    class Stream:
        def __init__(self, chunks):
            self.chunks = chunks
        def __iter__(self):
            return iter(self.chunks)

    f = MockFile()
    s = b'\x1b[33mHello\x1b[0m\n'
    write_stream_with_colors_win_py3

# Generated at 2022-06-13 22:25:13.131265
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    from httpie.client import get_response_for_prepared_request
    from httpie.compat import is_windows
    from httpie.output.streams import RawStream

    with parser.parse_args([]) as args:
        args.stream = True
        args.prettify = True
        args.style = 'pardkim'
        env = Environment(args=args)

        request = HTTPRequest('http://example.com', 'GET')
        r = get_response_for_prepared_request(request, session=requests.Session())



# Generated at 2022-06-13 22:25:14.001051
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:25:23.364282
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.input.parser import KeyValueArgType
    from httpie.output.streams import PrettyStream
    import pytest
    from requests import PreparedRequest, Response

    args = parser.parse_args(['--prettify', 'colors'])

# Generated at 2022-06-13 22:25:35.691265
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import json

    class MockResponse:

        def __init__(self, response_dict):
            self.__dict__ = response_dict

    class MockEnvironment:

        def __init__(self, is_windows=False, stdout_isatty=True):
            self.is_windows = is_windows
            self.stdout_isatty = stdout_isatty

    env = MockEnvironment()
    args = argparse.Namespace(prettify=['all'], stream=False, style=None, debug=False, traceback=False)
    request = requests.PreparedRequest()
    request.headers = {'user-agent': 'test-user-agent'}
    request.body = 'test-body'
    request.method = 'GET'

# Generated at 2022-06-13 22:25:54.841304
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    env = Environment()
    env.stdout_isatty = False
    args = argparse.Namespace()
    args.stream = False
    args.prettify = False
    args.prettify = False
    args.style = False
    args.json = False
    args.format_options = False

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )

    assert(stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE)
    assert(stream_class == RawStream)

# Generated at 2022-06-13 22:26:08.591428
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli.exceptions import ExitStatus
    from httpie.output.streams import (
        BINARY_SUPPRESSED_NOTICE, RedirectStream
    )
    stdout = io.BytesIO()
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': '18',
        'Transfer-Encoding': 'chunked',
    }
    body = b'{"id": 1, "name": "A green door"}'
    response = requests.Response()
    response.status_code = 200
    response.reason = 'OK'

# Generated at 2022-06-13 22:26:15.719414
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    test_stream = iter([
        b'\033[22;39m[\033[1m\033[22;39m200\033[0m\033[22;39m]\033[22;39m ' +
        b'\033[22;39mGET\033[22;39m http://127.0.0.1:8000/get',
        b'\r\n\r\n',
    ])
    test_outfile = io.StringIO()
    test_outfile.write('test')
    test_outfile.read()
    with mock.patch('httpie.output.streams.write_stream') as write_stream_mock:
        write_stream_with_colors_win_py3(test_stream, test_outfile, False)

# Generated at 2022-06-13 22:26:27.464292
# Unit test for function write_message
def test_write_message():
    import sys
    import os
    import tempfile
    
    # argparse.Namespace
    args = argparse.Namespace()
    args.style = "solarized"
    
    def write_stream(
        stream: BaseStream,
        outfile: Union[IO, TextIO],
        flush: bool
    ):
        pass

    # Environment
    env = Environment(args)
    env.stdout = tempfile.TemporaryFile()
    env.stdout_isatty = True

    # requests.PreparedRequest
    requests_message = requests.PreparedRequest()
    requests_message.headers['Content-Type'] = "application/json"
    requests_message.headers['Content-Length'] = 5
    requests_message.body = "foobar"
   
    requests_message.body = "foobar"


# Generated at 2022-06-13 22:26:28.931215
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:26:41.573183
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment as tEnvironment

    from httpie.output.streams import (
        BaseStream as tBaseStream, BufferedPrettyStream as tBufferedPrettyStream,
        EncodedStream as tEncodedStream, PrettyStream as tPrettyStream,
        RawStream as tRawStream
    )

    from httpie.output.processing import Conversion as tConversion, Formatting as tFormatting

    from httpie.cli.argtypes import KeyValueArg
    from httpie import cli

    args = cli.parser.parse_args(['-pjson,prettify'])
    # args = cli.parser.parse_args(['-pjson'])

    args.format_options = [KeyValueArg(k, v) for k, v in args.format_options or []]

    env = tEnvironment()
    env

# Generated at 2022-06-13 22:26:54.600382
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Test function write_stream_with_colors_win_py3"""
    # prepare test data
    stream = ['\x1b[0;32mdata\x1b[0m', '\x1b[1;31mdata\x1b[0m', 'data']
    outfile = io.StringIO()
    flush = True
    # run test
    write_stream_with_colors_win_py3(stream, outfile, flush)
    # check test result
    expected_result = '\x1b[0;32mdata\x1b[0m\x1b[1;31mdata\x1b[0mdata'
    assert outfile.getvalue() == expected_result

# Generated at 2022-06-13 22:27:06.641402
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(prettify=None, stream=False, style=None, json=False)
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env': env})

    args = argparse.Namespace(prettify=None, stream=True, style=None, json=False)
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': 1})

    args = argparse.Namespace(prettify=None, stream=False, style=None, json=False)
    env = Environment(stdout_isatty=False)

# Generated at 2022-06-13 22:27:16.859622
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import argparse
    from httpie.context import Environment
    from httpie.config import Config
    from httpie.models import HTTPRequest, HTTPResponse
    import io


# Generated at 2022-06-13 22:27:28.373385
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie import input
    from httpie.config import Config
    
    # first 3 function param 
    config = Config(env=Environment(), client__default_options=input.DEFAULT_OPTIONS)
    args = argparse.Namespace()

    # =============================================================
    # Case 1: Raw stream, stdout is not a tty, not meant to be pretty
    # =============================================================

    # case 1.1: stdout is not a tty, not stream, meant to be pretty
    args.prettify = True
    args.stream = False
    env = Environment(is_windows=False,
                      stdout_isatty=False,
                      stdout=None)

# Generated at 2022-06-13 22:27:59.757023
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import os
    from httpie.core import main
    from httpie.downloads import prompts
    class _Args:
        pass
    args = _Args()

    args.verbose = False
    args.quiet = False
    args.stream = False
    args.download = True
    args.prettify = False

    args.output = ''

    args.style = 'parallel'
    args.color = True
    args.traffic = False
    args.force_colors = True
    args.colors = True
    args.format = None
    args.help = False
    args.debug = False
    args.traceback = False
    args.json = False
    args.download_flat = '.'
    args.download_output = None
    args.download_output_dir = None
    args.output_dir

# Generated at 2022-06-13 22:28:12.901810
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.input import ParseRequest
    from httpie.output.processing import Conversion, Formatting
    from httpie.plugins import builtin
    from httpie import __main__
    requests_message = ParseRequest('GET httpbin.org', stdin=open(__main__.__file__))[0].prepare()
    env = Environment(
        stdin=open(__main__.__file__),
        stdout=sys.stdout,
        stderr=sys.stderr,
        color=False,
    )
    args = __main__.parser.parse_args(['GET', 'httpbin.org'])
    args.prettify = ['all']
    args.stream = False
    args.format_options = ['quote=all']

# Generated at 2022-06-13 22:28:18.084675
# Unit test for function write_stream
def test_write_stream():
    mock_outfile=Mock()
    mock_outfile.write=MagicMock()

    mock_stream=Mock()
    mock_stream.__iter__=MagicMock(return_value=["a","b","c"])

    write_stream(
        stream=mock_stream,
        outfile=mock_outfile,
        flush=False
    )

    mock_outfile.write.assert_has_calls([
        call("a"),
        call("b"),
        call("c")
    ])

    mock_stream.__iter__.assert_called_once_with()



# Generated at 2022-06-13 22:28:31.554033
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import sys
    # Default UTF-8 encoding on Unix is enough; on Windows we need to
    # know the OEM codepage of the terminal so we write the right bytes
    # to the pipe.
    encoding = sys.stdout.encoding or 'cp{0}'.format(
        ctypes.windll.kernel32.GetOEMCP())

    buf = io.BytesIO()

    class FakeStream(list):
        def __iter__(self):
            for elem in self:
                yield elem.encode(encoding)

        def __getitem__(self, *args):
            return super().__getitem__(*args)

    stream = FakeStream(['aaa'])
    write_stream_with_colors_win_py3(
        stream, buf, flush=True)

    stream = Fake

# Generated at 2022-06-13 22:28:42.139185
# Unit test for function write_stream
def test_write_stream():
    from unittest.mock import MagicMock, patch
    outfile_mock = MagicMock()
    outfile_mock.buffer = outfile_mock
    with patch('httpie.output.streams.EncodedStream') as EncodedStream_mock:
        write_stream(
            stream=EncodedStream_mock(),
            outfile=outfile_mock,
            flush=True,
        )
    outfile_mock.write.assert_called_once()


# Generated at 2022-06-13 22:28:53.771086
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import build_encoded_stream

    def get_stream_for_message(msg, with_headers=True, with_body=True):
        return build_encoded_stream(
            msg=msg,
            with_headers=with_headers,
            with_body=with_body,
            env=Environment(),
        )

    import io
    import sys
    if (sys.platform == 'win32'
            and sys.version_info >= (3, 0)
            and sys.stdout.encoding):

        msg = HTTPRequest()
        stream = get_stream_for_message(msg)
        outfile = io.TextIOWrapper(io.BytesIO(), encoding=sys.stdout.encoding)

# Generated at 2022-06-13 22:29:07.368642
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """Test function get_stream_type_and_kwargs"""
    from httpie.core import main

    class MockStdout(StringIO):
        def __init__(self):
            super().__init__()
            self.isatty = True

        def write(self, data):
            super().write(data)
            raise IOError(errno.EPIPE, 'Broken Pipe')

    class MockArgParseNamespace:
        def __init__(self, **kwargs):
            self.__attributes = kwargs

        def __getitem__(self, key):
            return self.__attributes[key]

        def __setitem__(self, key, value):
            self.__attributes[key] = value

        def __getattr__(self, attr):
            return self.__att

# Generated at 2022-06-13 22:29:11.078146
# Unit test for function write_stream
def test_write_stream():
    with open('./stdout.txt', 'wb') as f:
        stream = b'data'
        write_stream(stream, f, False)


# Generated at 2022-06-13 22:29:25.018313
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.processing import Conversion, Formatting
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.cli.environment import Environment
    from httpie.client.base import Client

    class FakeArgs:
        def __init__(self):
            self.prettify = 'none'
            self.prettify_all = False
            self.stream = False
            self.pretty = False
            self.format = None
            self.format_options = {}
            self.json = False
            self.style = None
            self.stream = False
            self.traceback = False
            self.debug = False

# Generated at 2022-06-13 22:29:35.891499
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import io
    from httpie.output.streams import BaseStream, RawStream

    test_stream_classes = [BaseStream, RawStream]
    for stream_class in test_stream_classes:
        outfile = io.StringIO('')
        buffer_size = 10
        normal_chunk = b'normal' * buffer_size
        color_chunk = b'\x1b[2mcolor\x1b[0m' * buffer_size
        chunks = [normal_chunk, color_chunk]
        stream = stream_class(msg=None, with_headers=False, with_body=True, chunks=chunks)
        write_stream_with_colors_win_py3(
            stream=stream,
            outfile=outfile,
            flush=False
        )

# Generated at 2022-06-13 22:30:06.824585
# Unit test for function write_message
def test_write_message():
    import io
    import sys
    import httpie
    from httpie.models import HTTPRequest
    from httpie.output.streams import BufferedPrettyStream, EncodedStream

    class Environ:
        def __init__(self, stdout, stderr, isatty=False, is_windows=False):
            self.stdout = stdout
            self.stderr = stderr
            self.stdout_isatty = isatty
            self.is_windows = is_windows
            self.debug = False
            self.traceback = False

    class ArgSpace:
        def __init__(self, stream):
            self.stream = stream
            self.prettify = ['colors']
            self.style = 'native'
            self.json = False
            self.format_options = {}


# Generated at 2022-06-13 22:30:20.015169
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    class Namespace:
        def __init__(self, stream, prettify):
            self.stream = stream
            self.prettify = prettify

    class Environment:
        def __init__(self, stdout_isatty):
            self.stdout_isatty = stdout_isatty

    class IO:
        def __init__(self, encoding):
            self.encoding = encoding
          
    class HTTPRequest:
        def __init__(self, requests_message):
            self.requests_message = requests_message

    class HTTPResponse:
        def __init__(self, requests_message):
            self.requests_message = requests_message
    requests_message = requests.PreparedRequest()
    args = Namespace(stream=True, prettify=True)
   

# Generated at 2022-06-13 22:30:26.786005
# Unit test for function write_message
def test_write_message():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    env = Environment(argparse.Namespace(colors=0, pretty='all', style='curl', traceback=False, debug=False, stream=False))
    response = requests.Response()
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    response.encoding = 'utf-8'
    response._content = b'{\n "name": "Abc"\n}\n'
    response.request.method = 'GET'
    write_message(requests_message=response, env=env, args=args, with_headers=True, with_body=True)

# Generated at 2022-06-13 22:30:27.505842
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:30:39.080517
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():

    class MockStream:
        """A mock stream that yields bytes that are colorized with ANSI."""

        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < 2:
                self.i += 1
                return b'hello world'
            elif self.i < 5:
                self.i += 1
                return b'\x1b[34m'
            raise StopIteration

    class MockOutfile:
        """A mock outfile that collects writes to its `buffer`.

        This is to make sure that the bytes are written to the buffer
        and not the `outfile`.

        """

        def __init__(self):
            self.buffer = []


# Generated at 2022-06-13 22:30:48.217553
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    env = Environment(stdout_isatty=False, stdout='file_obj')
    args = argparse.Namespace(stream=True, prettify=None)
    requests_response = requests.Response()
    requests_response._content = b'hello world'
    requests_response.headers = {'Content-Type': 'text/plain'}
    for chunk in build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=requests_response,
        with_body=True,
        with_headers=False,
    ):
        pass



# Generated at 2022-06-13 22:30:58.066632
# Unit test for function write_stream
def test_write_stream():
    """
    Test the write_stream function
    """
    import requests
    import os
    import sys

    import httpie.core
    from httpie.core import main
    from httpie import ExitStatus

    # https://stackoverflow.com/a/5803329/1679946
    r = requests.get('http://jsonplaceholder.typicode.com/posts/1')
    r2 = requests.get('http://jsonplaceholder.typicode.com/posts/2')
    class Args:
        """
        Fake argparse namespace for testing httpie.core:main
        """
        def __init__(self):
            self.download = False
            self.stream = False
            self.debug = False
            self.traceback = False
            self.prettify = ''
            self.style = ''


# Generated at 2022-06-13 22:31:10.627474
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # windows raw
    env = Environment(colors=256, stdout_isatty=False, is_windows=True)
    args = argparse.Namespace(prettify=None, stream=False, style="default", json=False, format_options=[])
    # print(get_stream_type_and_kwargs(env, args))
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': 65536})
    # windows raw
    env = Environment(colors=256, stdout_isatty=False, is_windows=True)
    args = argparse.Namespace(prettify=None, stream=True, style="default", json=False, format_options=[])
    # print(get_stream_type_and_kwargs(env, args

# Generated at 2022-06-13 22:31:16.856245
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    in case we add any new functionality here, we should have a unit test to cover it
    """
    stream = [b'a\x1b[1mb\x1b[0mc', b'd\x1b[1me\x1b[0mf']
    out = StringIO()
    write_stream_with_colors_win_py3(stream, out, flush=False)
    assert out.getvalue() == 'a\x1b[1mb\x1b[0mcdef\x1b[1m\x1b[0m'

# Generated at 2022-06-13 22:31:18.126697
# Unit test for function write_message
def test_write_message():
  pass


# Generated at 2022-06-13 22:31:44.833081
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """
    get_stream_type_and_kwargs test
    """
    import json
    with open('httpie/tests/data/http-response.json') as f:
        http_response = json.load(f)
    assert len(http_response) == 2

    # test args.prettify
    http_response[1]['headers']['User-Agent'] = 'test'
    args = argparse.Namespace()
    args.prettify = []
    args.style = "default"
    args.json = True
    args.format_options = {}
    env = Environment()
    response = HTTPResponse(http_response[1])

    # test terminal output
    env.stdout_isatty = True
    # test args.prettify = []
    stream_class, stream_

# Generated at 2022-06-13 22:31:53.595065
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Monkeypatch the stdout to provide file in write mode
    # Without this check we have crash in get_stream_type_and_kwargs as
    # the attribute 'isatty' is not present in the stdout
    test_stdout_file_obj = open(os.devnull,'wb')
    env = Environment(
        stdin=sys.stdin,
        stdout=test_stdout_file_obj,
        stderr=sys.stderr,
        is_windows=False
    )
    args = argparse.Namespace(
        json=True,
        stream=False,
        prettify=None,
        style=None
    )
    stream_type = get_stream_type_and_kwargs(
        env=env,
        args=args
    )

# Generated at 2022-06-13 22:32:03.865684
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import httpie.output.streams
    import httpie.compat
    stdout = httpie.compat.get_strio(encoding='utf8')
    stdout.isatty = True
    stdout.encoding = 'utf8'
    httpie.compat.is_windows = True
    httpie.compat.json = json
    httpie.output.streams.json = json
    # make sure that stdout.buffer is available
    getattr(stdout, 'buffer')
    # write a simple request

# Generated at 2022-06-13 22:32:09.255845
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    test_env = Environment()
    test_args = argparse.Namespace()
    test_args.prettify, test_args.stream, test_args.json, test_args.style = None,  None,  None,  None
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=test_env,
        args=test_args
    )
    assert stream_class == RawStream

# Generated at 2022-06-13 22:32:15.169051
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """Unit test for function get_stream_type_and_kwargs"""
    env = Environment()
    parser = argparse.ArgumentParser(parents=[])
    args = parser.parse_args()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream

# Generated at 2022-06-13 22:32:19.389432
# Unit test for function write_stream
def test_write_stream():
    outfile = open("temp.txt", "w")
    a = [b'a', b'b', b'c']
    write_stream(a, outfile, False)
    outfile.close()
    f = open("temp.txt", "r")
    out_str = f.read()
    f.close()
    os.remove("temp.txt")
    assert(out_str == "abc")

# Generated at 2022-06-13 22:32:28.076733
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.core import main
    args = main.parse_args(['--prettify', 'colors'])
    env = Environment()
    get_stream_type_and_kwargs(env, args)
    # requests_message = requests.PreparedRequest()
    requests_message = requests.Response()
    requests_message.status_code = 200
    requests_message.request.method = 'GET'
    requests_message.request.url = 'http://127.0.0.1:5000/'
    requests_message.request.headers = {'Content-Type': 'text/plain'}
    requests_message._content = 'hello httpie'.encode()

# Generated at 2022-06-13 22:32:40.041156
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()

    # Error: no prettify, no stdout, no --stream
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    stream_type == RawStream
    'chunk_size' in stream_kwargs
    stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE

    # Ok: no prettify, no stdout, --stream
    args.stream = True
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    stream_type == RawStream
    'chunk_size' in stream_kwargs
    stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE_BY_LINE

    # Ok: no

# Generated at 2022-06-13 22:32:45.667631
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import json
    import requests
    from io import BytesIO
    from io import StringIO

    from httpie.output.streams import BufferedPrettyStream
    from httpie.utils import get_first_bytes_of_response
    from httpie.utils import get_response_headers_as_dict
    from httpie.utils import parse_content_type
