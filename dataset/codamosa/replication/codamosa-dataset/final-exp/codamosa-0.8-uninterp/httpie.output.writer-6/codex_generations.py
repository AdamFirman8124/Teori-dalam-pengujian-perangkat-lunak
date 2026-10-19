

# Generated at 2022-06-13 22:22:58.175313
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import os

    os.environ['TERM'] = 'xterm-256color'
    stream = PrettyStream([b'a', b'\x1b[1mb', b'\x1b[34mc'])
    outfile = io.StringIO()

    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=outfile,
        flush=True
    )
    assert outfile.getvalue() == 'a\x1b[1mb\x1b[34mc\n\n'

# Generated at 2022-06-13 22:23:09.864124
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from .httpie import main

    args_list = [['--style=monokai', 'http://google.com']]
    if sys.version_info.minor == 2:
        args_list.append(['--style=monokai', '--stream', 'http://google.com'])

    for args in args_list:
        try:
            main(args, env=Environment(stdout=sys.stdout, stdout_isatty=False))
        except IOError as e:
            if e.errno == errno.EPIPE:
                # Ignore broken pipes unless --traceback.
                sys.stderr.write('\n')
            else:
                raise
        sys.stdout.write('\n')
        sys.stderr.write('\n')

# Generated at 2022-06-13 22:23:24.375468
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import platform
    import sys

    class MockOutfile():
        def __init__(self):
            self.text = ''

        def write(self, text):
            self.text += text

        def __str__(self):
            return self.text

    if platform.system() != 'Windows' or sys.version_info[0] != 3:
        return
    else:
        from httpie.output.fallback import WIN_PY3_COLOR_SUPPORTED
        assert WIN_PY3_COLOR_SUPPORTED
        outfile = MockOutfile()
        stream_class, stream_kwargs = get_stream_type_and_kwargs(
            env=None,
            args=None,
        )

# Generated at 2022-06-13 22:23:28.699881
# Unit test for function write_stream
def test_write_stream():
    import io
    test_str = b'test'
    f = io.BytesIO(test_str)
    write_stream(
                f,
                io.StringIO(),
                True
    )

# Generated at 2022-06-13 22:23:41.530157
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    def build_output_stream_for_message(
        args: argparse.Namespace,
        env: Environment,
        requests_message: Union[requests.PreparedRequest, requests.Response],
        with_headers: bool,
        with_body: bool,
    ):
        stream_class, stream_kwargs = get_stream_type_and_kwargs(
            env=env,
            args=args,
        )
        message_class = {
            requests.PreparedRequest: HTTPRequest,
            requests.Response: HTTPResponse,
        }[type(requests_message)]
        yield from stream_class(
            msg=message_class(requests_message),
            with_headers=with_headers,
            with_body=with_body,
            **stream_kwargs,
        )

# Generated at 2022-06-13 22:23:51.505930
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    import platform

    class MockArgs:
        def __init__(self):
            self.prettify = ['colors']
            self.stream = False

    class MockEnv:
        def __init__(self):
            self.stdout = StringIO()
            self.stdout_isatty = True
            self.is_windows = platform.system() == 'Windows'


# Generated at 2022-06-13 22:24:01.482153
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():

    class MockArgs:
        stream = False
        json = False
        prettify = []
        style = ''
        format_options = {}
        debug = False
        traceback = False

    args = MockArgs()

    class MockEnv:
        stdout_isatty = True
        stdout = ''
        is_windows = False

    env = MockEnv()

    class MockResponse:
        is_body_upload_chunk = False

    request = requests.PreparedRequest()
    response = MockResponse()

    with_headers = False
    with_body = False
    test = build_output_stream_for_message(args, env, request, with_headers, with_body)
    assert next(test) == ''

    with_headers = True
    with_body = False
    test = build_output_stream_

# Generated at 2022-06-13 22:24:14.371435
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace()
    args.prettify = {"format": "colors"}
    args.stream = False
    args.style = None
    args.format_options = None
    args.json = False
    env_args = argparse.Namespace()
    env_args.stdout_isatty = True
    env = Environment(env_args)
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert isinstance(stream_type, BufferedPrettyStream)
    args.prettify = None
    args.stream = True
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert isinstance(stream_type, PrettyStream)
    args.pre

# Generated at 2022-06-13 22:24:24.782584
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.client import Client

    # default
    env = Environment(stdout_isatty=True, stderr_isatty=False)

# Generated at 2022-06-13 22:24:36.273057
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class Stream(object):
        def __init__(self, streams):
            self.streams = streams

        def __iter__(self):
            return iter(self.streams)

    class Outfile(object):
        def __init__(self, encoding):
            self.encoding = encoding

        def write(self, *args, **kwargs):
            print('write', args, kwargs)

        def flush(self, *args, **kwargs):
            print('flush', args, kwargs)


# Generated at 2022-06-13 22:24:51.891493
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    """
    Test that the output stream is created correctly in the following cases:

    When the output is a TTY (no stream)
    When the output is not a TTY (stream)
    When the output is pretty (no stream)
    When the output is pretty and streamed
    """
    import io
    import traceback
    from httpie.cli import parser

    from httpie.core import main
    from httpie.context import Environment
    from httpie import ExitStatus
    from requests.models import Response
    from httpie.compat import is_windows

    # Base test cases
    env = Environment()
    stdout_fd = io.StringIO()
    args = parser.parse_args(args=['https://www.google.com'], env=env)
    args.prettify = ['b', 'h']

    # Test:

# Generated at 2022-06-13 22:25:01.208074
# Unit test for function write_message
def test_write_message():
    headers = '''GET / HTTP/1.1
User-Agent: HTTPie/0.9.9
Accept-Encoding: gzip, deflate
Accept: */*
Host: 127.0.0.1:5000


'''
    headers2 = '''GET / HTTP/1.1
User-Agent: HTTPie/0.9.9
Accept-Encoding: gzip, deflate
Accept: */*
Host: 127.0.0.1:5000



'''
    body = '''HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 2
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Sun, 23 Jun 2019 08:59:22 GMT


{"key": "value"}
'''

# Generated at 2022-06-13 22:25:12.289872
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    if sys.version_info >= (3, 0):
        from httpie.output.streams.raw import RawStream
        class MockArgs(object):
            def __init__(self, debug=False, traceback=False):
                self.debug = debug
                self.traceback = traceback
        class MockEnv(object):
            def __init__(self, is_windows):
                self.is_windows = is_windows
                self.stdout = sys.stdout
                self.stdout_isatty = sys.stdout.isatty()
        # This should work just fine
        mock_args = MockArgs(debug=False, traceback=False)
        mock_env = MockEnv(is_windows=True)

# Generated at 2022-06-13 22:25:21.448895
# Unit test for function write_stream
def test_write_stream():
    from unittest.mock import patch
    from tempfile import TemporaryFile

    with patch('httpie.output.streams.write_stream_with_colors_win_py3') as write_stream:
        TEST_STR = "Some example test string"
        with TemporaryFile(mode='w+b') as tempfile:
            stream = EncodedStream(env=Environment(stdout=tempfile))
            write_stream(stream=stream, outfile=tempfile, flush=False)
            tempfile.seek(0)
            assert tempfile.read().rstrip(b'\r\n') == TEST_STR.encode()

# Generated at 2022-06-13 22:25:31.993014
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    Environment.global_config.load(None)

    env = Environment(colors=256)
    args = argparse.Namespace(prettify=['colors'], style='slate', 
    format_options={}, json=False, stream=True)

    assert get_stream_type_and_kwargs(env=env, args=args) == (PrettyStream, {'env': env, 'conversion': Conversion(), 'formatting': Formatting(env=env, groups=['colors'], color_scheme='slate', explicit_json=False, format_options={})})

# Generated at 2022-06-13 22:25:42.257151
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout_isatty = True
    env.is_windows = False
    args = argparse.Namespace()
    args.prettify = ['all']
    args.style = 'parity'
    args.stream = True
    args.json = True
    args.format_options = None
    req = requests.PreparedRequest()

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    yield_stream = stream_class(req, **stream_kwargs)
    results = next(yield_stream)

    assert isinstance(results, bytes) == True
    assert isinstance(results, str) == False



# Generated at 2022-06-13 22:25:53.938580
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import EncodedStream, RawStream, PrettyStream, BufferedPrettyStream

    environment = Environment()
    args = argparse.Namespace(
        styles=False,
        prettify=None,
        style='',
        stream=False,
        download=False,
        out=sys.stdout,
        output_options=None,
    )
    requests_message = requests.Response()
    stream, stream_kwargs = get_stream_type_and_kwargs(args=args, env=environment)
    assert stream_kwargs == {}
    assert stream == EncodedStream
    # Todo: Test http_message


# Generated at 2022-06-13 22:26:07.702597
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(colors=256, stdin_isatty=True, stdout_isatty=True,
                      is_windows=True, is_iterm=False, is_cygwin=False)
    args = argparse.Namespace(prettify=['all'], style=None, stream=False, json=False,
                              format_options=[])
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class.__name__ == 'BufferedPrettyStream'
    assert 'env' in stream_kwargs
    assert 'prettify' in stream_kwargs['formatting'].groups
    args.prettify = ['none']
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)

# Generated at 2022-06-13 22:26:16.990649
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io

    outfile = io.StringIO()
    stream = BaseStream(b'\x1b[34mOK\x1b[0m', with_headers=False, with_body=True)
    write_stream_with_colors_win_py3(stream,outfile, True)
    assert outfile.getvalue() == "OK"

    outfile = io.StringIO()
    stream = BaseStream(b'OK', with_headers=False, with_body=True)
    write_stream_with_colors_win_py3(stream,outfile, True)
    assert outfile.getvalue() == "OK"

# Generated at 2022-06-13 22:26:24.732813
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    env = Environment()
    args = argparse.Namespace()
    requests_message = requests.PreparedRequest()
    with_headers = True
    with_body = False
    try:
        stream = build_output_stream_for_message(
            args=args,
            env=env,
            requests_message=requests_message,
            with_body=with_body,
            with_headers=with_headers)
    except:
        assert False
    
    assert True

# Generated at 2022-06-13 22:26:39.977780
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:26:41.099467
# Unit test for function write_message
def test_write_message():
    return True

# Generated at 2022-06-13 22:26:54.449584
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import BytesIO, TextIOWrapper
    from colorama import Fore
    from httpie.cli import parser

    env = Environment()
    args = parser.parse_args([])
    requests_message = requests.PreparedRequest()
    requests_message.url = 'https://api.github.com/events'
    requests_message.method = 'POST'
    requests_message.headers['Content-Type'] = 'text/xml; charset=utf-8'

# Generated at 2022-06-13 22:27:05.768026
# Unit test for function write_stream
def test_write_stream():
    from tempfile import TemporaryFile

    outfile = TemporaryFile()
    stream_class = BaseStream
    stream_kwargs = {
        'msg': HTTPRequest(
            requests.Request(
                method='GET',
                url='http://example.com',
            ).prepare(),
            with_body=True,
            with_headers=True,
            env=None
        )
    }

    write_stream(
        stream=stream_class(**stream_kwargs),
        outfile=outfile,
        flush=True
    )

    outfile.seek(0)

    out = outfile.read()
    assert b'GET / HTTP/1.1\r' in out



# Generated at 2022-06-13 22:27:18.280856
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import os
    import sys
    # python_version = (sys.version_info.major, sys.version_info.minor)
    # if python_version != (3, 6):
    #     raise NotImplementedError('test for function '
    #                               'get_stream_type_and_kwargs '
    #                               'only works with python 3.6')
    from httpie.context import Environment
    from httpie.output.streams import PrettyStream, BufferedPrettyStream, EncodedStream, RawStream
    from httpie.output.processing import Conversion, Formatting
    from httpie.models import HTTPRequest, HTTPResponse
    env = Environment()
    env.stdout = sys.stdout
    env.stderr = sys.stderr

# Generated at 2022-06-13 22:27:19.407167
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass


# Generated at 2022-06-13 22:27:30.941584
# Unit test for function write_message
def test_write_message():
    msg = requests.PreparedRequest()
    msg.body = b'This is a body'
    msg.encoding = "utf-8"
    msg.headers = {'Hello': 'World'}
    msg.url = 'http://www.example.com'
    env = Environment()
    from httpie import cli
    args = cli.parser.parse_args([], env)
    # body without headers
    outfile = io.StringIO()
    env.stdout = outfile
    env.stdout_isatty = False
    write_message(msg, env, args, with_body=True, with_headers=False)
    assert outfile.read() == "This is a body\n"
    assert not env.stderr.getvalue()

# Generated at 2022-06-13 22:27:40.777946
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    env = Environment()
    env.stdout = StringIO()
    args = argparse.Namespace()
    args.prettify = ['colors']
    stream = PrettyStream(
        msg=HTTPResponse(requests.Response()),
        with_headers=True,
        with_body=True,
        env=env,
        conversion=Conversion(),
        formatting=Formatting(
            env=env,
            groups=args.prettify,
            color_scheme=args.style,
            explicit_json=args.json,
            format_options=args.format_options,
        )
    )
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=env.stdout,
        flush=False
    )


# Generated at 2022-06-13 22:27:50.079483
# Unit test for function write_message
def test_write_message():
    from httpie.input import ParseArgs
    class MockRequests(object):
        class PreparedRequest(object):
            def __init__(self, cookie, header, body):
                self.cookies = cookie
                self.headers = header
                self.body = body
            def __str__(self):
                return "<PreparedRequest>"
        class Response(object):
            def __init__(self, cookie, header, body):
                self.cookies = cookie
                self.headers = header
                self.body = body
            def __str__(self):
                return "<requests.Response>"
    class MockEnv(object):
        class Stdout(object):
            def __init__(self, stream):
                self.stream = stream

# Generated at 2022-06-13 22:28:00.976535
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(stdout_isatty=True, colors=256)
    args = argparse.ArgumentParser().parse_args(['--stream'])
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type == PrettyStream
    assert stream_kwargs['chunk_size'] == Stream.CHUNK_SIZE_BY_LINE

    args = argparse.ArgumentParser().parse_args([])
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type == BufferedPrettyStream
    assert stream_kwargs['chunk_size'] == BufferedPrettyStream.CHUNK_SIZE_BY_LINE

    args = argparse.ArgumentParser().parse_args([])

# Generated at 2022-06-13 22:28:28.106189
# Unit test for function write_message
def test_write_message():

    import pytest
    import json
    import requests
    import httpie.output.streams
    import httpie.cli
    import httpie.context
    import httpie.cli
    import httpie.models
    import httpie.output.streams
    import httpie.output.processing
    import httpie.output.formatters.colors
    import httpie.output.formatters.format

    @pytest.fixture
    def env(monkeypatch):

        class StdStream(object):

            def write(self, chunk):
                return 'write'

            def isatty(self):
                return True
        stdout = StdStream()
        stderr = StdStream()
        env = httpie.context.Environment(stdout, stderr)
        return env


# Generated at 2022-06-13 22:28:35.615338
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    requests_message = requests.PreparedRequest()
    requests_message.url = "https://www.baidu.com"
    requests_message.method = "GET"
    env = Environment()
    from argparse import Namespace
    args = Namespace()
    args.json = True
    args.style = "default"
    args.unicode = True
    args.prettify = "all"
    args.headers = True
    args.body = True
    args.format_options = []
    args.stream = True
    args.traceback = True
    args.timeout = 10

    stream = build_output_stream_for_message(args=args, env=env,requests_message=requests_message)

# Generated at 2022-06-13 22:28:48.653638
# Unit test for function write_message
def test_write_message():
    from httpie.cli import parse_args
    args = parse_args(['https://httpbin.org/get', '-p'])
    env = Environment(
        args=args,
        stdout=sys.stdout,
        stderr=sys.stderr,
        stdin=sys.stdin,
        color=args.color,
        verify=args.verify,
        trust_env=args.trust_env
    )
    requests_message = requests.PreparedRequest()
    write_message(
        requests_message=requests_message,
        env=env,
        args=args,
        with_headers=False,
        with_body=False
    )
    requests_message = requests.Response()

# Generated at 2022-06-13 22:28:52.451485
# Unit test for function write_stream
def test_write_stream():
    write_stream(
        stream = [b'\x1b[31m'+b'hello'+b'\x1b[0m'],
        outfile = sys.stdout,
        flush = True
    )

# Generated at 2022-06-13 22:29:06.968167
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    """Unit test for function build_output_stream_for_message

    """
    from httpie.plugins import builtin

    builtin.load_plugins()

    from httpie.compat import str

    from httpie.context import Environment
    from httpie.output.streams import (
        RawStream, PrettyStream, EncodedStream
    )
    from httpie.models import (
        HTTPRequest, HTTPResponse
    )

    import requests
    from requests.cookies import RequestsCookieJar
    from requests.structures import CaseInsensitiveDict

    args = argparse.Namespace(
        stream=False,
        prettify=None,
        style=None,
        json=None,
        format_options=[],
    )

# Generated at 2022-06-13 22:29:21.678508
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import PrettyStream
    from httpie.core import main
    import requests
    import sys

    current_platform = sys.platform
    sys.platform = "linux"
    env = Environment()
    args = main.get_parser().parse_args([])
    # Get a prepared request with request body
    with open('../test/test_request', 'rb') as f:
        headers = f.readline()
        body = f.read()
    r = requests.Request('POST', 'http://httpbin.org/headers', headers={'Content-Type': 'application/json'}, data=body)
    prepared_request = r.prepare()
    # 1. Get stream for message with body

# Generated at 2022-06-13 22:29:31.056773
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=Environment(
            stdout_isatty=True,
            debug=True,
        ),
        args=argparse.Namespace(
            stream=False,
            prettify='all',
            style='solarized',
            json=False,
            format_options={},
        )
    )
    assert stream_class == PrettyStream
    assert stream_kwargs['env'].stdout_isatty
    assert stream_kwargs['formatting'].color_scheme == 'solarized'
    assert stream_kwargs['formatting'].explicit_json is False
    assert stream_kwargs['formatting'].groups == 'all'

# Generated at 2022-06-13 22:29:42.972261
# Unit test for function write_message

# Generated at 2022-06-13 22:29:44.467051
# Unit test for function write_stream
def test_write_stream():
    import io
    outfile = io.BytesIO()
    assert write_stream(b'hello world', outfile) == b'hello world'

# Generated at 2022-06-13 22:29:55.147451
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(arguments=['http','--form','localhost:8000/'],
        stdout=StringIO(),
        stdin=StringIO(b'name=yu'),
        stdin_isatty=False,
        stdout_isatty=False,
        color_scheme=None)
    args = argparse.Namespace()
    args.prettify = None
    args.stream = False
    args.style = None
    args.json = False
    args.format_options = {}
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert(stream_class == EncodedStream)
    assert(stream_kwargs == {'env': env})

    args.prettify = 'colors,headers'
    args.stream = False
    args

# Generated at 2022-06-13 22:30:19.794616
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie import input
    from httpie.output.streams import PrettyStream

    class Namespace:
        colors = None
        stream = False
        style = 'auto'
        format = None
        pretty = 'all'
        json = False
        output_options = None
        download = False
        traceback = False
        debug = False
        redirect = True
        verify = True
        insecure = False
        cert = None
        timeout = None
        max_redirects = 10
        output = None
        check_status = False

    args = Namespace()

    class Environment:
        colors = 256
        stdout_isatty = True
        is_windows = False
        stdout = False
        request = None
        # ignore the rest of the vars

    env = Environment()


# Generated at 2022-06-13 22:30:27.712547
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    result = get_stream_type_and_kwargs(
                    env=Environment(stdout_isatty=True, colors=256),
                    args=argparse.Namespace(prettify=['colors', 'format', 'headers'],
                                            style='solarized',
                                            json=False,
                                            format_options={},
                                            stream=False)
    )
    assert result[0] == BufferedPrettyStream
    assert result[1]['env'].colors == 256
    assert result[1]['formatting'].style.name == 'solarized'
    assert result[1]['formatting'].groups == ['colors', 'format', 'headers']
    assert result[1]['formatting'].color_scheme is None
    assert result[1]['formatting'].expl

# Generated at 2022-06-13 22:30:39.551246
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import EncodedStream
    assert get_stream_type_and_kwargs(
        env=Environment(),
        args=argparse.Namespace(
            stream=False,
            prettify=False,
        )
    ) == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE})


# Generated at 2022-06-13 22:30:43.799331
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Unit test for the function write_stream_with_colors_win_py3().
    """
    import tempfile
    import io
    from httpie.output.streams import BaseStream
    from httpie.core import main

    args = main.parser.parse_args(args=[])
    stdin_bytes = io.BytesIO()
    stdout_text = io.TextIOWrapper(io.BytesIO(), encoding='utf8')

# Generated at 2022-06-13 22:30:50.811078
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():

    import requests
    from httpie.context import Environment
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.processing import Conversion, Formatting
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )

    env = Environment()
    env.stdout = 1
    env.stdout_isatty = 1
    req = requests.Request('GET', 'https://www.google.com')
    preq = req.prepare()
    header = [('User-Agent', 'python-requests/2.22.0'), ('Accept-Encoding', 'gzip, deflate'), ('Accept', '*/*'), ('Connection', 'keep-alive')]
    body = ''

# Generated at 2022-06-13 22:30:59.217794
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import sys
    import io
    import sys
    from contextlib import redirect_stdout

    from loguru import logger
    import requests
    import responses
    import cli

    args = cli.parser.parse_args(args=['-j', '-H', 'Cache-Control: max-age=0', 'http://httpbin.org/get'])
    env = Environment(args)
    requests_message = requests.PreparedRequest()
    requests_message.headers = {'Cache-Control': 'max-age=0'}
    requests_message.url = 'http://httpbin.org/get'
    requests_message.method = 'GET'
    f = io.StringIO()

# Generated at 2022-06-13 22:31:11.412169
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Set up some objects to mock the function call
    class TestEnv():
        stdout_isatty = True
    class TestArgs():
        prettify = None
        stream = False
    env = TestEnv()
    args = TestArgs()
    
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type == EncodedStream
    assert stream_kwargs == {'env': env}

    # Reset args
    args = TestArgs()
    args.prettify = 'colors'
    args.stream = True
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type == PrettyStream

# Generated at 2022-06-13 22:31:19.767348
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    stream = b'\x1b[1m\x1b[31mGET / HTTP/1.1\x1b[39m\x1b[22m'
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, False)
    assert outfile.getvalue() == u'\x1b[1m\x1b[31mGET / HTTP/1.1\x1b[39m\x1b[22m'

# Generated at 2022-06-13 22:31:29.314061
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream
    from httpie.output.streams import EncodedStream
    from httpie.context import Environment
    from httpie.models import Converter

    from tests.it.data import CLI_COMMAND_SIMPLE, CLI_COMMAND_SIMPLE_WITH_STREAM
    from tests.it.data import CLI_COMPARE, CLI_COMPARE_WITH_STREAM
    from tests.it.data import CLI_COOKIES, CLI_COOKIES_WITH_STREAM
    from tests.it.data import CLI_FORM, CLI_FORM_WITH_STREAM
    from tests.it.data import CLI_FORM_JSON, CLI_FORM_JSON_WITH_STREAM
    from tests.it.data import CLI_FORM_MULTIPART, CLI_FORM_

# Generated at 2022-06-13 22:31:31.346017
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import httpie.cli
    args = httpie.cli.parser.parse_args()
    args.prettify = 'colors'
    args.style = 'paraiso-light'
    assert type(get_stream_type_and_kwargs(None, args)[0]) == type(BufferedPrettyStream)

# Generated at 2022-06-13 22:31:55.595916
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import unittest
    import sys
    import io
    import tempfile

    from httpie.core import main as core_cli
    from httpie import ExitStatus

    from httpie.context import Environment
    from httpie.request import RequestOptions
    from httpie.models import Request, Response
    from httpie.output.processing import Conversion, Formatting

    from httpie.compat import is_windows

    def read_file_to_string(filepath):
        with open(filepath) as f:
            return f.read()

    class MockEnv(Environment):
        """
        An environment with a custom stdout buffer (for assertions).
        """
        def __init__(self):
            super(MockEnv, self).__init__()

# Generated at 2022-06-13 22:31:57.099130
# Unit test for function write_message
def test_write_message():
    pass

# Generated at 2022-06-13 22:32:06.945528
# Unit test for function write_message
def test_write_message():
    import os, sys, json
    from httpie.context import Environment
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.core import main
    from httpie.utils import StdinBytesIO
    from httpie.output.streams import RawStream, PrettyStream
    from httpie.output.processing import Formatting
    requests_message = {
        'url':'http://www.baidu.com',
        'body':'{"a":"1"}',
        'headers':{'User-Agent':'httpie','Content-Type':'application/json'},
        'method':'GET',
        'cookies': '1234565'
    }
    env = Environment()
    args = main.parser.parse_args([])
    env.stdout_isatty = True
    env.std

# Generated at 2022-06-13 22:32:13.576893
# Unit test for function write_message
def test_write_message():
    requests_message = requests.Request("GET", "http://httpbin.org/anything")
    requests_message = requests_message.prepare()
    env = Environment()
    args = argparse.Namespace()
    args.prettify = ["colors", "format", "info", "headers", "body"]
    args.style = "storm"
    args.json = True
    args.format_options = {"sort_keys": True}
    print(write_message(requests_message, env, args, with_body=True, with_headers=True))

# Generated at 2022-06-13 22:32:15.555086
# Unit test for function write_message
def test_write_message():
    write_message(
        requests_message=requests.PreparedRequest(),
        env=Environment(),
        args=argparse.Namespace(),
        with_headers=False,
        with_body=False,
    )

# Generated at 2022-06-13 22:32:23.343457
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    class TestStream(BaseStream):
        def __iter__(self):
            yield b'\x1b[1m1\x1b[0m'
            yield b'2'
            yield b'\x1b[1m3\x1b[0m'
        def fileno(self):
            return 0
    class TestOutFile:
        def __init__(self):
            self.buffer = io.BytesIO()
            self.encoding = 'utf-8'
        def write(self, data):
            self.buffer.write(data.encode(self.encoding))
        def flush(self):
            pass
    outfile = TestOutFile()

# Generated at 2022-06-13 22:32:37.591382
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    environment = Environment(
        colors=256,
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
        is_windows=False,
        stdout_isatty=True)
    args = argparse.Namespace(prettify=('all', 'b'))
    # request = HTTPRequest()
    # request.method = 'GET'
    # request.url = 'http://httpbin.org/get'
    # requests_message = HTTPRequest(request)

    # requests_message = HTTPRequest(**kwargs)

    # response = HTTPResponse()
    # response.status_code = 200
    # response.reason = 'OK'
    # response.url = 'http://httpbin.org/get'
    # response.raw =

# Generated at 2022-06-13 22:32:44.992503
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():

    env = Environment()
    args = argparse.Namespace()
    requests_message = ""
    with_headers = True
    with_body = True
    assert build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=requests_message,
        with_body=with_body,
        with_headers=with_headers,
    )