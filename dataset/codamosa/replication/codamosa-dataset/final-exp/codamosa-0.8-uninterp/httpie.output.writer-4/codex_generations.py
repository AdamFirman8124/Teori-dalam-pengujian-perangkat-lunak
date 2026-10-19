

# Generated at 2022-06-13 22:22:56.275482
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass



# Generated at 2022-06-13 22:23:04.887114
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import termcolor
    from httpie.output.streams import write_stream_with_colors_win_py3

    stdout = io.StringIO()
    colors = ['red', 'green', 'blue']
    for color in colors:
        stream = termcolor.colored('test\n', color).encode()
        write_stream_with_colors_win_py3(stream=stream,
                                         outfile=stdout,
                                         flush=True)
        assert stdout.getvalue() == termcolor.colored('test\n', color)

# Generated at 2022-06-13 22:23:14.897346
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.formatters.registry import formatter_registry

    from httpie.compat import is_windows
    args = argparse.Namespace(
        stream=False,
        prettify=formatter_registry.get_by_name('all'),
        style='default',
        json=False,
        stream=False,
        format_options={},
    )
    env = Environment(
        stdin_isatty=True,
        stdout_isatty=True,
        is_windows=is_windows,
    )

    stream_class_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class_kwargs[0].__name__ == 'BufferedPrettyStream'


# Generated at 2022-06-13 22:23:15.667861
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert(False);

# Generated at 2022-06-13 22:23:27.750098
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.compat import bytes
    from httpie.output.streams import StreamType
    from httpie.cli import parser
    parser.parse_args(['--download', '--traceback'])
    response = requests.Response()
    body = 'ok'
    # for function build_output_stream_for_message
    response.headers = {
        'content-type': 'image/jpeg',
        'content-length': '1024'
    }
    response.raw.headers = {
        'content-type': 'application/json',
        'content-length': '1024'
    }
    response.request = requests.PreparedRequest()
    response.request.url = 'http://127.0.0.1:5000/'

# Generated at 2022-06-13 22:23:35.675255
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    buffer = StringIO()
    stream = [b"\x1b[32m", b"abc", b"\x1b[33m", b"de"]
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=buffer,
        flush=False
    )

    output = buffer.getvalue()
    assert output == "\x1b[32mabc\x1b[33mde"

# Generated at 2022-06-13 22:23:45.541841
# Unit test for function write_stream
def test_write_stream():
    from contextlib import redirect_stdout
    from io import BytesIO
    from httpie.output.streams import StreamError

    # Inputs
    args.prettify = False
    args.stream = False
    env.stdout_isatty = False
    env.is_windows = False

    # Expected Outcomes
    expected_return_type = StreamError
    expected_outfile = BytesIO()
    expected_flush = False
    chunk_size = 512

    # Test Conditions
    actual_return_type = write_stream(
        stream=chunk_size,
        outfile=expected_outfile,
        flush=expected_flush
    )

    # Assertions
    assert actual_return_type == expected_return_type

    # Test Conditions

# Generated at 2022-06-13 22:23:47.362709
# Unit test for function write_stream
def test_write_stream():
    write_stream(stream=BaseStream, outfile=IO, flush=False)

# Generated at 2022-06-13 22:24:00.374526
# Unit test for function write_message
def test_write_message():
    """
    测试函数 write_message
    """
    parsed_args = {'format': [''], 'style': '', 'prettify': [''], 'stream': False}
    args = argparse.Namespace(**parsed_args)
    env = Environment()
    requests_message = requests.PreparedRequest()
    with_headers = True
    with_body = False
    write_message(requests_message, env, args, with_headers, with_body)
    parsed_args = {'format': [''], 'style': '', 'prettify': [''], 'stream': False}
    args = argparse.Namespace(**parsed_args)
    env = Environment()
    requests_message = requests.Response()
    with_headers = True

# Generated at 2022-06-13 22:24:13.326443
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.core import main
    from httpie.input import ParseError
    from httpie.downloads import Downloader
    from . import httpbin
    from .utils import MockEnvironment, MockResponse
    env = MockEnvironment(
        stdout_isatty=True,
        stdin_isatty=False,
        stdout=io.BytesIO(),
        stdin=io.BytesIO(b'GET / HTTP/1.1\n\n'),
        colors=256,
    )
    args = main.parser.parse_args(args=[], env=env)
    args.prettify = args.stream = args.traceback = False
    args.download = False
    d = Downloader(env, args)

# Generated at 2022-06-13 22:24:26.789876
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class FakeTextIo:
        def __init__(self):
            self.encoding = 'utf-8'

    class FakeStdout:
        text_io = FakeTextIo()

        def write(self, text):
            assert text == '\033[123\n'

        def flush(self):
            pass

    fake_stdout = FakeStdout()
    env = Environment(
        colors=256,
        is_windows=True,
    )

# Generated at 2022-06-13 22:24:32.214647
# Unit test for function write_stream
def test_write_stream():
    print("Testing write_stream")
    error = open("error", 'w')
    stdout = open("stdout", 'w')
    test = ["1", "2", "3"]
    write_stream(stream=test, outfile=stdout, flush=False)
    write_stream(stream=test, outfile=error, flush=False)
    write_stream(stream=test, outfile=stdout, flush=True)
    write_stream(stream=test, outfile=error, flush=True)
    stdout.close()
    error.close()


# Generated at 2022-06-13 22:24:45.257001
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import httpie
    from httpie.core import main
    from requests.models import PreparedRequest
    from requests.models import Response

    # Build prepared request
    r1 = PreparedRequest()
    r1.method = 'GET'
    r1.url = 'http://www.example.com'
    r1.body = 'test'
    r1.headers['Content-Type'] = 'text/html'
    # Build response
    r2 = Response()
    r2.url = 'http://www.example.com'
    r2.status_code = 200
    r2.encoding = 'utf-8'
    r2.headers['Content-Type'] = 'text/html'
    r2.text = 'test'
    # Build httpie.models.HTTPRequest
    r3 = httpie.models.HTTP

# Generated at 2022-06-13 22:24:57.150829
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import unittest

    class TestBuildOutputStreamForMessage(unittest.TestCase):
        def test_build_output_stream_for_message1(self):
            # Assuming the function is called with
            # requests_message=messages.HTTPRequest(messages.PreparedRequest)
            # and
            # with_headers=True,
            # and
            # with_body=False
            # The function should return
            # stream_class = RawStream
            # and
            # stream_kwargs = {'chunk_size': RawStream.CHUNK_SIZE}

            from httpie.output.streams import RawStream
            from httpie.models import HTTPRequest, HTTPResponse


# Generated at 2022-06-13 22:25:04.005298
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace()
    args.prettify = []
    args.stream = False
    env = Environment()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': env}

    args.prettify = ['colors', 'format']
    args.style = 'default'
    args.json = False
    args.format_options = {'verify': False}
    args.stream = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream
    assert stream_kwargs['formatting'].color_scheme == 'default'

# Generated at 2022-06-13 22:25:16.481017
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams.base import FakeStdout

    kwargs = {
        'stream': [
            b'\x1b[6;30;42m\x1b[Khello\x1b[m\x1b[K\x1b[7m\x1b[Kworld!',
            b'\x1b[m\x1b[K\n',
        ],
        'outfile': FakeStdout(),
        'flush': False,
    }
    write_stream_with_colors_win_py3(**kwargs)

# Generated at 2022-06-13 22:25:25.756441
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    A unit test for function write_stream_with_colors_win_py3()
    """
    from httpie.output.streams import write_stream_with_colors_win_py3
    from httpie.compat import BytesIO
    from httpie.core import main_impl
    from httpie.parse import parse_items

    headers = parse_items([
        'Content-Type: text/html; charset=utf-8',
    ])

# Generated at 2022-06-13 22:25:26.630870
# Unit test for function write_message
def test_write_message():
    pass


# Generated at 2022-06-13 22:25:27.108980
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    pass



# Generated at 2022-06-13 22:25:31.225561
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    env = Environment(argv=[])
    args = argparse.Namespace()
    args.stream = False
    args.prettify = 'all'
    args.style = 'solarized'
    args.json = False
    args.format_options = []
    args.download = False
    args.debug = False
    args.traceback = False
    args.verify = False
    args.verify = False
    args.cert = False
    args.client_cert = False
    args.ascii = False
    args.unicode = False
    args.colors = 'auto'
    args.headers = True
    args.body = True
    args.verbose = True

    requests_message = requests.PreparedRequest()
    requests_message.method = 'HEAD'
    requests_message

# Generated at 2022-06-13 22:25:44.541421
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import RawStream
    from httpie.output.streams import EncodedStream

    from httpie.context import Environment

    from httpie.config import DEFAULT_OPTIONS
    from httpie.models import HTTPRequest
    from httpie.cli import parser


    def set_args(args_str):
        args = parser.parse_args(args_str.split())
        args.__dict__.update(DEFAULT_OPTIONS.__dict__)

# Generated at 2022-06-13 22:25:49.729039
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    mock_terminal = open('mock_terminal.txt', 'w', encoding='utf-8')
    mock_terminal.write('\n\n')
    mock_terminal.close()

# Generated at 2022-06-13 22:25:59.328597
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # set up parameters
    stream = json.dumps({'message': 'hello world'})
    stream = io.StringIO(stream)
    outfile = io.StringIO()
    flush = True

    # run test
    write_stream_with_colors_win_py3(stream=stream, outfile=outfile, flush=flush)

    # check result
    print(outfile.getvalue())
    assert outfile.getvalue() == '{"message": "hello world"}'

# Generated at 2022-06-13 22:26:08.410225
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # test with different arguments and host OS
    res = get_stream_type_and_kwargs(
        env=Environment(stdout_isatty=True, stdout=None, stderr=None, is_windows=False),
        args=argparse.Namespace(prettify=False, stream=False),
    )
    assert res == (EncodedStream, {'env': Environment(stdout_isatty=True, stdout=None, stderr=None, is_windows=False)})

    res = get_stream_type_and_kwargs(
        env=Environment(stdout_isatty=True, stdout=None, stderr=None, is_windows=False),
        args=argparse.Namespace(prettify=True, stream=True),
    )

# Generated at 2022-06-13 22:26:19.229720
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(
        stdin=io.StringIO(u'test'),
        stdout=io.StringIO(),
        stderr=io.StringIO(),
        is_windows=True,
        stdout_isatty=False,
        stdin_isatty=False,
        stdout_bytes_mode=False,
    )
    args = argparse.Namespace(prettify=[], style=None)
    if sys.version_info.major == 2:
        assert get_stream_type_and_kwargs(env=env, args=args) == (RawStream,{'chunk_size': 8092})
    else:
        assert get_stream_type_and_kwargs(env=env, args=args) == (RawStream,{'chunk_size': 8096})
    env

# Generated at 2022-06-13 22:26:19.694807
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    pass

# Generated at 2022-06-13 22:26:24.091304
# Unit test for function write_stream
def test_write_stream():
    s = ""
    class A:
        def buffer(self):
            return self
        def write(self, str):
            nonlocal s
            s = s + str
    a = A()
    write_stream(b"hello", a, False)
    assert s == "hello"

# Generated at 2022-06-13 22:26:34.704312
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import TextIOWrapper, BytesIO
    from sys import stdout
    from unittest.mock import Mock

    class MockStream(PrettyStream):
        def __init__(self, side_effect, **kwargs):
            super().__init__(**kwargs)
            self.side_effect = side_effect

        def __iter__(self):
            for value in self.side_effect:
                yield value

    def encoding_of(file):
        return file.encoding


# Generated at 2022-06-13 22:26:43.458438
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    s = StringIO()
    chunks = [
        b'foo ',
        b'\x1b[31mbar ',
        b'\x1b[32myikes ',
        b'\x1b[31mbaz',
        b'\x1b[0m',
        b' qux',
    ]
    write_stream_with_colors_win_py3(
        stream=chunks,
        outfile=s,
        flush=True,
    )
    assert s.getvalue() == 'foo bar yikes baz qux'

# Generated at 2022-06-13 22:26:48.420327
# Unit test for function write_message
def test_write_message():
    write_message(
        requests_message=None,
        env=None,
        args=None,
        with_headers=False,
        with_body=False,
    )
    
if __name__ == '__main__':
    test_write_message()

# Generated at 2022-06-13 22:27:00.956158
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import io
    infile = io.BytesIO(b'\x1b[1;32mfoo\x1b[0m\n\x1b[1;33mbar\x1b[0m\n')
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(
        stream=infile,
        outfile=outfile,
        flush=False
    )
    output = outfile.getvalue()
    assert output == 'foo\nbar\n', "colorized output is not correct"

# Generated at 2022-06-13 22:27:06.786662
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    stream = [b'foo', b'\x1b[1mbar\x1b[0m', b'baz']
    outfile = io.StringIO()

    write_stream_with_colors_win_py3(stream=stream,
                                     outfile=outfile,
                                     flush=False)

    assert(outfile.getvalue() == 'foo\x1b[1mbar\x1b[0mbaz')

# Generated at 2022-06-13 22:27:18.460749
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    args = argparse.Namespace(stream=False,prettify=[],style=None)
    env = Environment()
    requests_message = requests.PreparedRequest()
    requests_message.url = "http://www.baidu.com"
    requests_message.method = 'POST'
    requests_message.body = '{"json": "data"}'
    with_header = True
    with_body = True
    for chunk in build_output_stream_for_message(args=args, env=env, 
        requests_message=requests_message,with_headers=with_header,with_body=with_body):
        print(chunk.decode('utf-8'))

if __name__ == "__main__":
    test_build_output_stream_for_message()

# Generated at 2022-06-13 22:27:31.346366
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from unittest.mock import patch
    from httpie.context import Environment
    from httpie.output.streams import BaseStream
    args = argparse.Namespace()
    env = Environment(stdout_isatty=True)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    outfile = io.StringIO()

# Generated at 2022-06-13 22:27:31.866215
# Unit test for function write_message
def test_write_message():
    env.headers = []

# Generated at 2022-06-13 22:27:43.496812
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    stream_types = {
        RawStream: {
            'chunk_size': 4096
        },
        PrettyStream: {
            'env': Environment(),
            'conversion': Conversion(),
            'formatting': Formatting(
                env=Environment(),
                groups=[],
                color_scheme=None,
                explicit_json=False,
                format_options=None,
            )
        },
        EncodedStream: {
            'env': Environment()
        }
    }
    parsed_args = argparse.Namespace()
    parsed_args.stream = False
    parsed_args.prettify = []

    env = Environment(stdout_isatty=False)
    request = HTTPRequest(requests.PreparedRequest())
    response = HTTPResponse(requests.Response())


# Generated at 2022-06-13 22:27:51.357576
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.input import ParseRequest
    from httpie.output.streams import PrettyStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPRequest

    request_data = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
    args = ParseRequest().parse_args(['-v', '--stream', '--prettify', 'all', '-H'])
    environment = Environment(True, True, True)

    prepped = requests.Request('GET', 'https://www.google.com').prepare()
    prepped.body = request_data.encode()
    stream = build_output_stream_for_message(args, environment, prepped, with_headers=True, with_body=True)
   

# Generated at 2022-06-13 22:28:04.648221
# Unit test for function build_output_stream_for_message

# Generated at 2022-06-13 22:28:15.942517
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """
    Test `write_stream_with_colors_win_py3`
    """
    # Test data
    test_data = (
        b'\x1b[31mtest\x1b[39m'
        # Test split color sequences
        b'\x1b[3'
        b'1m'
        b'test\x1b[39m'
    )
    # Test stdout
    out = io.BytesIO()
    # Test args
    args = argparse.Namespace(
        stream = True,
        flush = True
    )
    # Test env
    env = Environment(
        is_windows = True,
        stdout = out,
        stdout_isatty = True,
    )
    # Test stream
    stream = test_data
    # Test Expected result

# Generated at 2022-06-13 22:28:28.310631
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Unit test for function write_stream_with_colors_win_py3.

    In order to make this test runnable on Linux and MacOS, we provide a
    mock for the function win_py3_colorized_output_supported, which is
    normally defined in httpie/platform.

    """
    from unittest.mock import patch

    with patch.object(Environment, '__init__') as mock_env_init:
        from httpie.output.streams import win_py3_colorized_output_supported
        mock_env_init.return_value = None

# Generated at 2022-06-13 22:28:42.259414
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    env = Environment()
    with requests.Session() as s:
        r = s.get('http://httpbin.org/get')
    write_message(r,env,args,with_body=True)

# Generated at 2022-06-13 22:28:53.841982
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Test 1: stream, prettify, and color (assert raw stream)
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(stream=True, prettify=True, style="equindens")
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == RawStream
    assert stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE_BY_LINE

    # Test 2: prettify and color (assert buffered pretty stream)
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(stream=False, prettify=True, style="equindens")

# Generated at 2022-06-13 22:29:07.397640
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = mock.Mock()
    args.prettify = None
    args.stream = False
    args.style = None
    args.json = False
    args.format_options = None
    env = mock.Mock()
    env.stdout_isatty = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == RawStream
    assert stream_kwargs == {
        'chunk_size': RawStream.CHUNK_SIZE
    }

    args = mock.Mock()
    args.prettify = None
    args.stream = True
    args.style = None
    args.json = False
    args.format_options = None
    env = mock.Mock()

# Generated at 2022-06-13 22:29:22.199118
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert name_stream_class(get_stream_type_and_kwargs(Environment(), argparse.Namespace(
        headers=[],
        method='GET',
        prettify=None,
        stream=False,
        style='default',
        json=False,
        format_options={}
    ))) == 'EncodedStream'
    assert name_stream_class(get_stream_type_and_kwargs(Environment(stdout_isatty=False), argparse.Namespace(
        headers=[],
        method='GET',
        prettify=None,
        stream=False,
        style='default',
        json=False,
        format_options={}
    ))) == 'RawStream'

# Generated at 2022-06-13 22:29:33.175444
# Unit test for function write_message
def test_write_message():
    import io
    import contextlib
    import requests
    import argparse
    import httpie.output.streams
    import httpie.output.processing
    import httpie.context
    import httpie.models

    # mock Env
    class MockEnv:
        def __init__(self):
            self.stdout = io.BytesIO()
            self.stderr = io.BytesIO()
            self.stdout_isatty = False
            self.is_windows = False

    # mock RequestsMessage
    class MockRequestMessage:
        def __init__(self):
            self.headers = {}
            self.url = ''
            self.raw = io.BytesIO()

    # mock RequestsMessage
    class MockResponseMessage(MockRequestMessage):
        def __init__(self):
            super().__

# Generated at 2022-06-13 22:29:43.038829
# Unit test for function write_message
def test_write_message():
    test_requests_message = requests.get("http://www.google.com")
    env = Environment()

# Generated at 2022-06-13 22:29:52.241795
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import sys
    # Testing write_stream_with_colors_win_py3 with colorized terminal output with py3:
    out_fd = io.StringIO()
    assert not hasattr(out_fd, 'buffer')
    expected_out = 'foo bar\n'
    write_stream_with_colors_win_py3(
        stream=io.BytesIO(b'foo bar\n'),
        outfile=out_fd,
        flush=False
    )
    assert out_fd.getvalue() == expected_out
    out_fd.truncate(0)
    out_fd.seek(0)
    # Testing write_stream_with_colors_win_py3 with colorized terminal output with py3, but without colors:
    write_stream_with_colors_win_py

# Generated at 2022-06-13 22:30:04.405517
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(Environment(stdout_isatty=False), argparse.Namespace(prettify=[])) == (RawStream, {'chunk_size': 1000})
    assert get_stream_type_and_kwargs(Environment(stdout_isatty=False), argparse.Namespace(prettify=[], stream=True)) == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE_BY_LINE})
    assert get_stream_type_and_kwargs(Environment(stdout_isatty=True), argparse.Namespace(prettify=[])) == (EncodedStream, {'env': Environment(stdout_isatty=True)})

# Generated at 2022-06-13 22:30:13.252877
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import TestByteStream
    from httpie.core import main
    from httpie.core import is_windows
    import pytest

    if not is_windows():
        pytest.skip("False positive on non-Windows")

    # This test function is only run on Windows with Python 3 and colorized terminal output.
    # The purpose is to ensure that colorized output is written as text directly to the
    # outfile to ensure it gets processed by colorama (otherwise the color codes get
    # discarded).

    args = main.get_parser().parse_args(['--pretty=colors'])
    env = Environment(args)
    stream = TestByteStream(bytearray(b'\x1b[0m\x1b[1;31m123\x1b[0m'), env)

    #

# Generated at 2022-06-13 22:30:18.282389
# Unit test for function write_message
def test_write_message():
    with_headers = True
    with_body = True
    env = Environment()
    args = argparse.Namespace()

    requests_message = "This is a message"
    write_message(requests_message, env, args, with_headers=with_headers, with_body=with_body)

# Generated at 2022-06-13 22:30:46.205250
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from httpie.output import build_output_stream_for_message, write_stream_with_colors_win_py3
    from httpie.core import main

    start_args = [
        '--pretty=colors',
        '--print=b',
        '--stream',
        'GET',
    ]
    args = main.parser.parse_args(start_args)
    rm = main.get_response(main.get_requests_session(), args)
    main.write_stream_with_colors_win_py3 = write_stream_with_colors_win_py3
    with patch('sys.stdout', new=StringIO()) as out, patch('httpie.core.is_windows', return_value=True):
        main.stdout = out

# Generated at 2022-06-13 22:30:57.416211
# Unit test for function write_message
def test_write_message():
    temp = os.path.join(os.path.dirname(__file__), 'temp')
    args = argparse.Namespace()
    args.json = False
    args.prettify = []
    args.debug = True
    args.stream = False
    args.form = False
    args.traceback = False
    env = Environment(args.json, args.prettify, temp, args.debug)
    env.stdout = temp + '/stdout'
    env.stdout_isatty = False
    env.stderr = temp + '/stderr'
    env.stderr_isatty = False
    env.is_windows = False
    request = requests.PreparedRequest()
    response = requests.Response()
    request.headers['Content-Type'] = 'application/json'
    request

# Generated at 2022-06-13 22:31:07.700386
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    f = io.StringIO()
    color1 = b'\x1b[32m'
    color2 = b'\x1b[35m'
    color3 = b'\x1b[0m'
    color12 = color1 + color2
    color23 = color2 + color3
    stream = [
        b'a', b'b', color1, b'c', b'd', color2, b'e', b'f', b'g', color12, b'h',
        b'i', color3, b'j', b'k', color23, b'l', b'm', color23, b'n'
    ]
    write_stream_with_colors_win_py3(
        stream = stream,
        outfile = f,
        flush = False
    )


# Generated at 2022-06-13 22:31:13.556516
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    response_value = b'\x1b[32m'
    outfile_value = io.StringIO()

    write_stream_with_colors_win_py3(response_value, outfile_value, True)
    assert '\x1b[32m' in outfile_value.getvalue()

# Generated at 2022-06-13 22:31:26.580220
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    '''
    Testing attribue of class and value of arguments
    '''
    args = argparse.Namespace(
        stream=True, prettify=['all'], style='default',
        format_options=[], json=False)
    env = Environment()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    try:
        assert(issubclass(stream_class, PrettyStream))
    except AssertionError:
        raise AssertionError

    try:
        assert(stream_kwargs["conversion"].__class__.__name__ == 'Conversion')
    except AssertionError:
        raise AssertionError

    args.prettify = []
    stream_class, stream_kwargs = get_stream_type_and_

# Generated at 2022-06-13 22:31:40.541102
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import io
    import httpie.output
    # Test simple write
    outfile = io.StringIO("")
    write_stream_with_colors_win_py3(
        stream=[b"Test"],
        outfile=outfile,
        flush=False,
    )
    assert outfile.getvalue() == "Test"

    # Test write with colours
    outfile = io.StringIO("")
    write_stream_with_colors_win_py3(
        stream=[b"\x1b[31mTest\x1b[39m"],
        outfile=outfile,
        flush=False,
    )
    assert outfile.getvalue() == httpie.output.termstyle("Test", [31])

# Generated at 2022-06-13 22:31:54.353630
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # message_class = {
    #     requests.PreparedRequest: HTTPRequest,
    #     requests.Response: HTTPResponse,
    # }[type(requests_message)]
    #
    # yield from stream_class(
    #     msg=message_class(requests_message),
    #     with_headers=with_headers,
    #     with_body=with_body,
    #     **stream_kwargs,
    # )
    # if (env.stdout_isatty and with_body
    #         and not getattr(requests_message, 'is_body_upload_chunk', False)):
    #     # Ensure a blank line after the response body.
    #     # For terminal output only.
    #     yield MESSAGE_SEPARATOR_BYTES

    test

# Generated at 2022-06-13 22:32:04.642850
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # pylint: disable=C0111,protected-access
    class MockEncodedStream(_BaseStream):
        def __init__(self, chunks):
            self.chunks = chunks
            self.closed = False
            self.encoding = 'utf8'

        def __iter__(self):
            return iter(self.chunks)

    def reset():
        ofile.write.called = False
        ofile.write.called_with = None
        ofile.buffer.write.called = False
        ofile.buffer.write.called_with = None

    def ofile_write(*args, **kwargs):
        ofile.write.called = True
        ofile.write.called_with = args[0]
        return len(ofile.write.called_with)


# Generated at 2022-06-13 22:32:15.137616
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class FakeStream:
        def __iter__(self):
            return iter([b'b', b'\x1b[', b'c'])
    class FakeOutFile:
        def __init__(self, encoding):
            self.encoding = encoding
        def buffer(self):
            raise AttributeError
        def write(self, s):
            pass
        def flush(self):
            pass
    class FakeEnv:
        def __init__(self, stdout_isatty, is_windows):
            self.stdout_isatty = stdout_isatty
            self.is_windows = is_windows
            self.stdout = FakeOutFile('utf8')

    def fake_write_stream(stream, outfile, flush):
        for chunk in stream:
            outfile.write(chunk)

# Generated at 2022-06-13 22:32:25.192907
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import os

    f = io.StringIO()
    color = b'\x1b['
    data = (
        b'binary\n'
        b'\x1b[31mwinpy3\x1b[39m\n'
        b'line\n'
    )
    stream = BaseStream.get_chunks(data)
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=f,
        flush=False
    )
    assert f.getvalue() == 'binary\n\x1b[31mwinpy3\x1b[39m\nline\n'

    os.environ['TERM'] = 'xterm-256color'
    f = io.StringIO()