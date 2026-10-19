

# Generated at 2022-06-13 22:23:03.196137
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class DummyArgument:
        def __init__(self, val):
            pass
    
    def get_stream_type(stream_class, stream_kwargs):
        return (('RawStream', RawStream),
                ('PrettyStream', PrettyStream),
                ('BufferedPrettyStream', BufferedPrettyStream),
                ('EncodedStream', EncodedStream))[stream_class](**stream_kwargs)
    
    # test pretify not set, but stream set
    class DummyEnvironment:
        stdout_isatty = True
        
    cli_args = argparse.Namespace()
    cli_args.prettify = DummyArgument(False)
    cli_args.stream = DummyArgument(True)
    

# Generated at 2022-06-13 22:23:12.627803
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import os
    import requests
    import json
    import shutil
    import io

    path_of_tests = os.path.dirname(os.path.abspath(__file__))
    path_of_test_data = os.path.join(path_of_tests, "../data/")
    json_content = []
    with open(os.path.join(path_of_test_data, "test_data.json"), "r") as json_file:
        json_content = json.load(json_file)

    filename = "test_put"
    filepath = os.path.join(path_of_test_data, filename)
    # We use PUT because it's the only verb that write a body.

# Generated at 2022-06-13 22:23:23.768295
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env.stdout_isatty = False
    args.prettify = None
    env, args =  variables

    env.stdout_isatty = False
    args.prettify = None
    env, args =  variables
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == RawStream

    env.stdout_isatty = True
    args.prettify = None
    env, args =  variables
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == EncodedStream



# Generated at 2022-06-13 22:23:37.082268
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class TestEnvironment(Environment):
        def __init__(self):
            self.is_windows = False
            self.stdout_isatty = False
            self.stdout = ''

    def test(args, stream_class, chunk_size=None):
        env = TestEnvironment()
        stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
        assert stream_class == stream_class
        if chunk_size is not None:
            assert 'chunk_size' in stream_kwargs
            assert stream_kwargs['chunk_size'] == chunk_size
        else:
            assert stream_kwargs == {}

    args = argparse.Namespace()
    args.stream = True

    args.prettify = []
    args.style = None
    args.json = False

# Generated at 2022-06-13 22:23:45.979608
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.compat import is_windows
    env = Environment()
    args = parser.parse_args(argstr='')
    r = requests.Response()
    r.status_code = 200
    r.encoding = 'utf8'
    r.url = 'http://www.example.com/'
    r.headers = {
        'content-type': 'application/json'
    }
    r._content = b'[{"number": 1 }, {"number": 2}]'
    r.reason = 'OK'
    r.request = requests.PreparedRequest()
    r.request.headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

# Generated at 2022-06-13 22:23:59.538159
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie import ExitStatus

    env = Environment(
        stdin_isatty=False,
    )
    parser = get_parser()
    args = parser.parse_args(args=[])
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type is RawStream
    assert stream_kwargs == {'chunk_size': RawStream.CHUNK_SIZE_BY_LINE}

    env = Environment(
        stdout_isatty=True,
    )
    parser = get_parser()
    args = parser.parse_args(args=['--prettify', 'all'])
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type is PrettyStream

# Generated at 2022-06-13 22:24:07.423203
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    Unit test for function write_stream_with_colors_win_py3.
    Checks that writing bytes to the console
    """
    import sys
    import os

    import pytest

    from .test_streams import stream_chunks
    from .test_prettifier import prettify_chunks

    pytest.importorskip('colorama')
    from colorama.initialise import deinit as deinit_colorama


# Generated at 2022-06-13 22:24:08.954662
# Unit test for function write_message
def test_write_message():
    pass


# Generated at 2022-06-13 22:24:17.587093
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Unit test for function write_stream_with_colors_win_py3"""
    from tempfile import TemporaryFile
    from unittest.mock import Mock
    env = Mock()
    env.is_windows = True
    env.stdout = TemporaryFile(mode='w+b')
    outfile = env.stdout
    buf = outfile.buffer
    stream = Mock()
    stream.__iter__ = lambda x: iter([b'\x1b[30mtest\x1b[0mtest'])
    flush = False
    write_stream_with_colors_win_py3(stream, outfile, flush)
    outfile.seek(0)
    buf.seek(0)
    assert outfile.read() == 'test\x1b[0mtest'

# Generated at 2022-06-13 22:24:28.772596
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from tempfile import TemporaryFile
    outfile = TemporaryFile()
    class fake_args:
        def __init__(self):
            self.style = 'default'
            self.prettify = []
            self.format_options = []
            self.stream = True
            self.json = False
    class fake_env:
        def __init__(self):
            self.stdout_isatty = True
        def is_windows(self):
            return False
        def stdout(self):
            return outfile
    import requests
    class fake_message(requests.Response):
        pass
    with open('/etc/hosts', 'rb') as f:
        fake_message.raw = f
        fake_message.status_code = 200

# Generated at 2022-06-13 22:24:48.368768
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # Dummy httpie.context.Environment
    # TODO: In the future, should make it more realistic.
    env = Environment()
    env.is_windows = False
    env.stdout_isatty = True
    env.stdout = sys.stdout

    # Dummy argparse.Namespace
    args = argparse.Namespace()
    args.stream = False
    #args.prettify = []
    args.prettify = ['colors']
    args.style = ""

    # PreparedRequest
    prepared_request = requests.Request()
    prepared_request.method = 'GET'
    prepared_request.url = 'https://httpie.org'
    prepared_request.headers['Accept-Encoding'] = 'gzip, deflate'
    prepared_request.prepare()

    # Make a http

# Generated at 2022-06-13 22:24:55.360233
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class MockEnv():
        stdout_isatty = True

    class MockArgs():
        prettify = ['colors']
        stream = False
        style = 'solarized'
        json = False
        format_options = {'sort': False}

    env = MockEnv()
    args = MockArgs()

    assert get_stream_type_and_kwargs(env, args)[0] == PrettyStream

# Generated at 2022-06-13 22:24:59.846678
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.core import main

    environ = os.environ.copy()
    environ['REQUESTS_CA_BUNDLE'] = 'foobar'
    env = Environment(argv=['http'], environ=environ)
    args = main.parser.parse_args(['--verbose'])

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    from httpie.output.streams import BufferedPrettyStream
    assert stream_class is BufferedPrettyStream
    assert set(stream_kwargs.keys()) == {'env', 'conversion', 'formatting'}

    args = main.parser.parse_args(['--verbose', '--pretty', 'all'])
    stream_class, stream_kwargs = get_

# Generated at 2022-06-13 22:25:12.179814
# Unit test for function write_stream
def test_write_stream():
    from httpie.output.streams import PrettyStream, EncodedStream, RawStream
    from httpie.compat import is_windows
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie import ExitStatus
    from httpie.models import HTTPRequest, HTTPResponse

    class MockStdOut:
        def __init__(self, isatty = True, lines = None):
            self.isatty = isatty
            self.lines = lines
            self.written_bytes = []

        def write(self, bytes):
            if self.lines:
                self.written_bytes.append(bytes.decode('utf-8'))
            else:
                self.written_bytes.extend(bytes)

        def flush(self):
            pass

    # Create an Environment and an Argument

# Generated at 2022-06-13 22:25:22.180480
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli.constants import DEFAULT_OPTIONS
    from httpie.cli.parser import Parser
    from httpie.context import Environment
    from httpie.output.output import build_output_stream_for_message
    from httpie.output.streams import PrettyStream

    args = Parser().parse_args(
        ['GET', 'example.com'] + DEFAULT_OPTIONS + ['-p'],
        env=Environment(),
    )
    import requests
    s = requests.Session()
    response = s.get('https://example.com')
    g = build_output_stream_for_message(args, Environment(), response, True, True)
    assert isinstance(next(g).stream, PrettyStream)



# Generated at 2022-06-13 22:25:35.143005
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    from httpie.output.streams import PrettyStream
    from httpie.context import Environment
    from httpie.models import HTTPResponse
    requests_message = HTTPResponse({"status": True})
    env = Environment()
    env.stdout = open("test_output.txt", "w")
    args = parser.parse_args(
        ["http", "is", "here"])
    args.stream, args.prettify, args.style, args.debug, args.traceback = True, [], "default", False, False
    i = 0
    for chunk in build_output_stream_for_message(args=args, env=env, requests_message=requests_message, with_headers=False, with_body=False):
        print(chunk)
       

# Generated at 2022-06-13 22:25:44.515748
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    from . import TestEnvironment

    env = TestEnvironment()
    args = parser.parse_args([])
    response = requests.Response()
    response.url = 'https://httpbin.org/get'
    response.encoding = 'utf-8'
    response.headers['content-type'] = 'application/json'
    response._content_consumed = True
    response._content = b'{"hello":"world"}'
    response.status_code = 200

    stream = build_output_stream_for_message(
        requests_message=response,
        env=env,
        args=args,
        with_headers=True,
        with_body=True,
    )
    # assert stream is not None

    for chunk in stream:
        assert len(chunk) > 0

# Generated at 2022-06-13 22:25:54.555916
# Unit test for function write_stream
def test_write_stream():
    # test without error
    stream = RawStream(msg=HTTPResponse(requests.Response()), chunk_size=1024)
    outfile = StringIO()
    write_stream(stream=stream, outfile=outfile, flush=False)
    assert outfile.getvalue() == ""

    # test broken pipe error
    outfile = UnseekableStringIO()
    with pytest.raises(IOError) as excinfo:
        write_stream(stream=stream, outfile=outfile, flush=False)
    assert excinfo.value.errno == errno.EPIPE


# Generated at 2022-06-13 22:26:08.375605
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from pytest import raises
    from io import StringIO
    from requests import PreparedRequest
    from httpie.core import main
    from httpie import ExitStatus

    class DummyStdout:
        encoding = 'utf-8'

        def write(self, data):
            if isinstance(data, bytes):
                self.buffer.write(data)
            else:
                self._write_text(data)

        def _write_text(self, data):
            self.buffer.write(data.encode('utf-8'))

        def buffer(self):
            return self


    class Env:
        stdout = DummyStdout()
        is_windows = True
        stdout_isatty = True


# Generated at 2022-06-13 22:26:15.825458
# Unit test for function write_message
def test_write_message():
    requests_message = requests.Response()
    requests_message.status_code = 200

    env = Environment()
    env.stdout = 'teststr'
    env.stdout_isatty = True

    args = argparse.Namespace()
    args.traceback = True
    args.debug = True
    args.prettify = 'colors'
    args.stream = False

    write_message(requests_message, env, args, with_headers=True, with_body=True)

# Generated at 2022-06-13 22:26:27.692365
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    args = MagicMock()
    env = MagicMock()
    request = MagicMock()
    request.is_body_upload_chunk = False

    output = build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=request,
        with_body=True,
        with_headers=True
    )

    assert next(output) == bytearray(b'\n')

# Generated at 2022-06-13 22:26:38.523160
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.core import main
    args = main.parser.parse_args()
    args.headers = True
    args.body = True
    env = Environment(
        stdout=sys.stdout,
        stderr=sys.stderr,
        stdin=sys.stdin,
        should_stream=False,
    )

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )

    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': env}

# Generated at 2022-06-13 22:26:52.388319
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class Outfile(object):
        def __init__(self, encoding: str) -> None:
            self.encoding = encoding

        def write(self, data: str) -> None:
            self.result += data

        def buffer(self):
            return self

    class Stream(object):
        def __iter__(self):
            for chunk in [b'a\x1b[1mb\x1b[22mc', b'd\x1b[32me\x1b[39mf']:
                yield chunk

    encoding = 'utf-16'
    outfile = Outfile(encoding)
    outfile.result = ''
    write_stream_with_colors_win_py3(stream=Stream(), outfile=outfile, flush=False)

# Generated at 2022-06-13 22:27:00.666171
# Unit test for function write_message
def test_write_message():
    import io
    temp_stream = io.StringIO()
    import requests
    sample_url = 'https://httpbin.org/'
    r = requests.get(sample_url)
    import httpie.cli
    httpie.cli.parse_args = lambda args: None
    env = Environment()
    args = argparse.Namespace()
    write_message(
        requests_message=r,
        env=env,
        args=args,
        with_headers=False,
        with_body=False,
    )

# Generated at 2022-06-13 22:27:09.943438
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    
    class FakeEnv(object):
        def __init__(self):
            self.stdout = None
            self.stdout_isatty = None

    class FakeArguments(object):
        def __init__(self):
            self.prettify = None
            self.stream = None
            self.debug = None
            self.traceback = None

    class FakeRequests(object):
        def __init__(self):
            self.url = None
            self.method = None
            self.headers = None
            self.body = None

    env = FakeEnv()
    args = FakeArguments()
    rqst = FakeRequests()

    # test for write_message
    assert write_message(rqst, env, args, False, False) == None

    # test for build

# Generated at 2022-06-13 22:27:17.384469
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    import argparse
    env = Environment()
    env.stdout_isatty = True
    env.stderr_isatty = True
    args = argparse.Namespace()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    stream_class.__name__ == 'PrettyStream'
    stream_kwargs['env'].__name__ == 'Environment'


# Generated at 2022-06-13 22:27:23.352329
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import re
    import requests
    from httpie.context import Environment
    from httpie.cli.parser import parse_args
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )

    # # Write a simple request to the stream
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=Environment(),
        args=parse_args('https://www.google.com')
    )
    google_req = requests.get('https://www.google.com')
    google_req_stream = stream_class(msg=HTTPResponse(google_req), **stream_kwargs)

    # # Write a simple request's response to the stream

# Generated at 2022-06-13 22:27:29.777733
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(
        stream=False,
        prettify=False,
        style=False,
        json=False,
        format_options=None,
    )

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert stream_class == EncodedStream

# Generated at 2022-06-13 22:27:33.078192
# Unit test for function write_stream
def test_write_stream():
    import sys
    import io
    data = b'foo\nbar\nbaz\n'
    result = io.BytesIO()
    write_stream(data, result, False)
    assert result.getvalue() == data



# Generated at 2022-06-13 22:27:44.638459
# Unit test for function write_message
def test_write_message():
    print("Testing function write_message")
    import json
    import pprint
    import requests
    import sys
    import pytest
    from httpie.context import Environment
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.context import Environment
    from httpie.output.processing import Conversion, Formatting
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )

# Generated at 2022-06-13 22:28:04.648273
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    from httpie import cli
    args = cli.parser.parse_args()
    env = Environment()
    env.stdout_isatty = True
    args.prettify = ["colors"]
    args.stream = True
    args.json = False
    args.style = ""
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    ls = args.prettify
    fo = args.format_options
    assert stream_class is PrettyStream
    assert stream_kwargs['env'] is env
    assert isinstance(stream_kwargs['conversion'], Conversion)
    assert isinstance(stream_kwargs['formatting'], Formatting)
    assert stream_kwargs['formatting'].env is env

# Generated at 2022-06-13 22:28:06.171227
# Unit test for function write_stream
def test_write_stream():
    out = StringIO()
    write_stream(["b", "a", "r"], out, False)
    assert out.getvalue() == "bar"

# Generated at 2022-06-13 22:28:16.581366
# Unit test for function write_message
def test_write_message():
    import json
    import requests
    # Make sure it prints nothing without a header or body
    args = argparse.Namespace(
        json = False,
        style = None,
    #    output = "",
        output = "https://ptsv2.com/t/pqowz-1586050429/post",
        traceback = False,
        browser = False,
        pretty = None,
        download = False,
        ignore_stdin = False
    )

# Generated at 2022-06-13 22:28:26.518432
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    outfile = io.BytesIO()
    write_stream_with_colors_win_py3(
        stream=b'foo\x1b[33mbar\x1b[39mbaz',
        outfile=outfile,
        flush=False
    )
    assert outfile.getvalue() == b'foobarbaz'
    write_stream_with_colors_win_py3(
        stream=b'foo\x1b[33mbar\x1b[39mbaz',
        outfile=outfile,
        flush=True
    )
    assert outfile.getvalue() == b'foobarbaz'

# Generated at 2022-06-13 22:28:35.176720
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import unittest
    class TestGetOutputStreamTypeAndKwargs(unittest.TestCase):
        def test_get_stream_type_and_kwargs(self):
            args = argparse.Namespace()
            args.json = ''
            args.prettify = ''
            args.style = 'foo'
            args.stream = ''
            args.format_options = ''
            env = Environment()
            stream_class, stream_kwargs = get_stream_type_and_kwargs(
                env=env,
                args=args,
            )
            self.assertEqual(stream_class, EncodedStream)
            self.assertEqual(stream_kwargs, {'env': env})

            args.prettify = 'bar'
            stream_class, stream_kwargs = get_stream_type

# Generated at 2022-06-13 22:28:49.734829
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    env = Environment(
        stdin=None,
        stdin_isatty=False,
        stdout=None,
        stdout_isatty=False,
        stderr=None,
        stderr_isatty=False,
        color_mode=True,
        color_depth=None,
        is_windows=False,
    )

    args = argparse.Namespace()

    requests_message = requests.PreparedRequest()

    with_headers = True
    with_body = True

    class TestBufferedPrettyStream(BufferedPrettyStream):
        def _write(self, bytes_: bytes) -> None:
            print(bytes_)

    class TestPrettyStream(PrettyStream):
        def _write(self, bytes_: bytes) -> None:
            print(bytes_)


# Generated at 2022-06-13 22:28:58.746452
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Unit tests for function write_stream_with_colors_win_py3"""

    import io
    import subprocess
    import unittest

    # Use a private version of RawStream so that we can write to it
    # for this unit test
    class UnitTestRawStream(RawStream):
        @property
        def _iterable(self):
            pass

        def __init__(self, iterable):
            self._iterable = iterable

        def __iter__(self):
            return iter(self._iterable)

    class TestCase(unittest.TestCase):
        """Test cases for function write_stream_with_colors_win_py3"""

        def test_write_bytes_win_py3(self):
            """test write_bytes_win_py3"""
            output = io.StringIO()


# Generated at 2022-06-13 22:29:02.165661
# Unit test for function write_message
def test_write_message():
    import sys
    args = argparse.Namespace()
    with open('test.txt', 'w') as file:
        write_message(req, args, file)

# Generated at 2022-06-13 22:29:14.681263
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class MyStream(BaseStream):
        def __init__(self, chunks):
            self.chunks = chunks

        def __iter__(self):
            for chunk in self.chunks:
                yield chunk.encode()

    class MyOutfile:
        encoding = 'utf-8'

        def __init__(self, out_value=None):
            self.out_value = out_value or []

        def write(self, value):
            self.out_value.append(value)

        def buffer(self):
            return self

    outfile = MyOutfile()

    args = argparse.Namespace(
        colors='auto'
    )
    env = Environment(
        is_windows=True
    )


# Generated at 2022-06-13 22:29:26.494875
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import pytest
    from httpie.cli import parser
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import EncodedStream
    from httpie.output.streams import BufferedPrettyStream
    args = parser.parse_args([])
    args.debug = True
    args.download = False
    args.prettify = {'colors'}
    requests.Response.is_body_upload_chunk = False

    env = Environment()
    env.stdout_isatty = True
    env.stdout = sys.__stdout__
    env.stderr = sys.__stderr__
    env.is_windows = False


# Generated at 2022-06-13 22:29:49.644903
# Unit test for function get_stream_type_and_kwargs

# Generated at 2022-06-13 22:29:54.894718
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class Args():
        def __init__(self):
            self.prettify = 'colors'
            self.stream = True
            self.style = 'boring'
            self.json = False
            self.format_options = {'style': 'boring'}

    class MockEnv():
        def __init__(self):
            self.stdout_isatty = True

    args = Args()
    env = MockEnv()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env,
                                                             args=args)
    assert stream_class is PrettyStream

# Generated at 2022-06-13 22:30:01.654427
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import sys
    print(get_stream_type_and_kwargs(
        env=Environment(stdout=sys.stdout,
                        stderr=sys.stderr,
                        stdout_isatty=True,
                        is_windows=True),
        args=argparse.Namespace(prettify=[],
                                style={},
                                stream=False)
    ))



# Generated at 2022-06-13 22:30:06.517720
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    message_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }['type(requests_message)']
    x = message_class("requests_message")
    print(x)

# Generated at 2022-06-13 22:30:19.737683
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class args:
        style = 'none'
        prettify = []
        json = False
        stream = False
        format_options = {}

    mock_env = MagicMock()
    mock_env.stdout_isatty = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=mock_env,
        args=args,
    )
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': mock_env}

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=mock_env,
        args=args,
        **{'args.prettify': ['colors']}
    )
    assert stream_class == BufferedPrettyStream

# Generated at 2022-06-13 22:30:25.381877
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout_isatty = False

    args = argparse.Namespace()
    args.stream = False
    args.prettify = ['colors']

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )

    assert stream_class == RawStream
    assert stream_kwargs == {
        'chunk_size': RawStream.CHUNK_SIZE
    }

# Generated at 2022-06-13 22:30:37.446767
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace()
    args.prettify = []
    args.format_options = {}
    args.stream = False
    args.style = None
    args.json = False

    env = Environment(stdout_isatty=True)
    assert get_stream_type_and_kwargs(env, args) == (BufferedPrettyStream, {
        'env': env,
        'conversion': Conversion(),
        'formatting': Formatting(env=env, groups=[], color_scheme=None, explicit_json=False, format_options={})
    })

    env = Environment(stdout_isatty=False)
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE})

# Generated at 2022-06-13 22:30:47.276271
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(prettify=['colors', 'format', 'body'], stream=True)

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert stream_class == PrettyStream
    assert stream_kwargs['env'] == env
    assert stream_kwargs['conversion'] == Conversion()
    assert stream_kwargs['formatting'].groups == ['colors', 'format', 'body']
    assert stream_kwargs['formatting'].color_scheme == 'solarized-dark'
    assert stream_kwargs['formatting'].explicit_json == False
    assert stream_kwargs['formatting'].format_options == {}

# Generated at 2022-06-13 22:30:57.347322
# Unit test for function write_message
def test_write_message():
    import argparse
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.output.streams import BaseStream
    class Stream(BaseStream):
        def __iter__(self):
            yield b"abc"
            return
    import requests
    class Response(requests.models.Response):
        pass
    response = Response()
    response.headers = {"xx":"x"}

    class ArgSpace(argparse.Namespace):
        pass
    args = ArgSpace()
    args.pretty = True
    args.style = "default"
    args.json = True
    args.format_options = {}
    args.stream = True
    args.debug = True
    args.traceback = True

    env = Environment()
    env.stdout = None
    env.stdout_isatty = True

# Generated at 2022-06-13 22:31:06.693336
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():

    args = argparse.Namespace(
        debug=False,
        download=False,
        max_redirects=0,
        max_timeline=0,
        output_dir='',
        output_file='',
        stream=False,
        style='',
        traceback=False,
        upload_file=None,
        verify=False,
    )
    env = Environment()
    requests_message = requests.Response
    with_headers = False
    with_body = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    print(stream_class)


# Generated at 2022-06-13 22:31:29.489301
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.downloads import (
        parse_content_range, parse_content_length
    )
    from httpie.plugins import builtin
    env = Environment(stdout=six.StringIO(), output_options={})
    args = builtin.parser.parse_args(args=[], env=env)
    class Request:
        headers = {
            'Range': 'bytes=0-9',
            'Content-Range': 'bytes 1-10/11',
            'Content-Length': '11'
        }
    request = Request()
    request.headers = {
        h: v for h, v in request.headers.items() if h != 'Range'
    }

# Generated at 2022-06-13 22:31:40.285022
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class dummy_environment:
        stdout_isatty = False
        class stdout:
            name = 'stdout'

    class dummy_args:
        prettify = False
        stream = False
        style = 'solarized-dark'
        json = False
        format_options = ['format_options']

    class dummy_args2:
        prettify = True
        stream = True
        style = 'solarized-dark'
        json = False
        format_options = ['format_options']

    env_obj = dummy_environment()
    args_obj = dummy_args()
    args_obj2 = dummy_args2()

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env_obj,
        args=args_obj
    )

    stream_class2

# Generated at 2022-06-13 22:31:54.056813
# Unit test for function write_message
def test_write_message():
    args = ['-v', '-L', '--all', '--print=H',
            '--pretty=all', '--style=paraiso-dark', '--download',
            'POST', 'http://httpbin.org/post']

# Generated at 2022-06-13 22:32:00.845641
# Unit test for function write_stream
def test_write_stream():
    
    # output should not be None
    output = io.StringIO()
    inputstream = io.BytesIO(b'a' * 32 + b'b' * 32)
    stream_class = EncodedStream
    stream_kwargs = {'env': Environment(stdout_isatty=True)}
    stream = stream_class(msg=inputstream, **stream_kwargs)
    write_stream(stream, output, False)
    assert output.getvalue() != ''
    
    

# Generated at 2022-06-13 22:32:11.696863
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(prettify=None, style=None, stream=None, json=None, format_options=None)
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env': env})

    args = argparse.Namespace(prettify=None, style=None, stream=True, json=None, format_options=None)
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE_BY_LINE})

    args = argparse.Namespace(prettify=None, style=None, stream=False, json=None, format_options=None)

# Generated at 2022-06-13 22:32:23.402052
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli.parser import parser
    from httpie.compat import is_windows, is_py3
    from httpie.output.streams import PrettyStream, BufferedPrettyStream, EncodedStream
    from httpie.output.streams import RawStream
    from httpie.output.processing import Formatting, Conversion
    
    from httpie.output.streams import EncodedStream
    from httpie.output.streams import RawStream
    
    import requests
    
    import httpie
    from httpie.compat import is_py3, is_windows
    # import pytest
    # import os
    import sys
    import time
    
    # Collect args
    args = parser.parse_args(['--prettify', 'all', '--stream'])
    # Create environment

# Generated at 2022-06-13 22:32:37.618236
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import re
    terminal_colors = re.compile(r'\x1b\[.*?m')
    stream = [
        b'HTTP\x1b[32m/1.1\x1b[0m \x1b[33m200\x1b[0m\n',
        b'Hello',
        b'\x1b[32m200\x1b[0m World\n',
    ]
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=True)
    s = outfile.getvalue()
    assert terminal_colors.sub('', s) == 'HTTP/1.1 200\nHello200 World\n'

# Generated at 2022-06-13 22:32:38.981971
# Unit test for function write_message
def test_write_message():
    write_message(None, None, None, True, True)

# Generated at 2022-06-13 22:32:51.218972
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import pytest

    from io import BytesIO
    from httpie.output.streams import ColorizedBytesStream
    from httpie.output.streams import BaseStream

    def _get_write_stream_with_colors_win_py3(
        BytesIO,
        BytesIO_write_bytes,
        BytesIO_decode,
    ):
        from httpie.output.streams import write_stream_with_colors_win_py3

        return write_stream_with_colors_win_py3

    write_stream_with_colors_win_py3 = _get_write_stream_with_colors_win_py3(
        BytesIO,
        BytesIO.write,
        BytesIO.decode,
    )
