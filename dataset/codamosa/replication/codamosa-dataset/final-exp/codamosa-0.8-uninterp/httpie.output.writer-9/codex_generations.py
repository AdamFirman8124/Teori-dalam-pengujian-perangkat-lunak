

# Generated at 2022-06-13 22:22:58.324700
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from io import StringIO
    import requests
    import argparse
    from httpie.context import Environment
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    env = Environment()
    args = argparse.Namespace()
    args.format = 'pretty'
    args.stream = True
    args.prettify = 'body'
    args.style = 'parrot'
    args.json = False
    args.format_options = {}
    req = requests.Request('GET', 'http://url.com')
    prepared_req = req.prepare()
    resp = requests.Response()

# Generated at 2022-06-13 22:23:00.062572
# Unit test for function write_stream
def test_write_stream():
    pass


# Generated at 2022-06-13 22:23:10.653468
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # noinspection PyProtectedMember
    from httpie.cli.argtypes import KeyValueArgType
    import requests
    import json

    args = argparse.Namespace()
    args.stream = True
    args.prettify = 'all'
    args.style = 'none'
    args.json = False
    args.debug = False
    args.traceback = False
    args.format_options = KeyValueArgType.from_args([])

    env = Environment()
    env.is_windows = False
    env.stdout_isatty = True
    env.stdout = None
    env.stderr = None
    env.config = None
    env.color = 'auto'

    resp_json = {'a': 1, 'b': 2}
    resp = requests.Response()
    # noins

# Generated at 2022-06-13 22:23:24.548798
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('--method')
    parser.add_argument('--headers')
    parser.add_argument('--body')
    parser.add_argument('--auth')
    parser.add_argument('--body-include')
    parser.add_argument('--output')
    parser.add_argument('--style')
    parser.add_argument('--style-global')
    parser.add_argument('--style-set')
    parser.add_argument('--style-override')
    parser.add_argument('--print')
    parser.add_argument('--debug')
    parser.add_argument('--traceback')
    parser.add_argument('--stream')

# Generated at 2022-06-13 22:23:38.118768
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # requests_response == requests.Response(body)
    # args == Namespace
    # env == Environment
    from httpie.core import main
    from tempfile import NamedTemporaryFile
    # Get a requests.Response object
    requests_response, env, args = main(['github.com'])
    # Build a file-like object to write to
    outfile = NamedTemporaryFile()
    write_stream_with_colors_win_py3(
        stream=build_output_stream_for_message(
            args=args,
            env=env,
            requests_message=requests_response,
            with_body=True,
            with_headers=True
        ),
        outfile=outfile,
        flush=False
    )
    # Reset file position
    outfile.seek(0)
    # Grab

# Generated at 2022-06-13 22:23:46.326853
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import RawStream, Foreground

    stream = RawStream(HTTPRequest(
        requests.PreparedRequest()
    ))

    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=False)
    assert outfile.getvalue() == ''

    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=True)
    assert outfile.getvalue() == ''

    stream = RawStream(HTTPRequest(
        requests.PreparedRequest(),
        prettifier=True,
        colors=Foreground,
        highlight_headers=True
    ))

    outfile = io.StringIO()

# Generated at 2022-06-13 22:23:59.834917
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # basic value
    env = Environment(
        argv=['http'],
        headers={},
        stdin=StringIO(),
        stdout=BytesIO(),
        stderr=StringIO(),
        is_windows=True,
        should_pretty_print=True
    )
    args = argparse.Namespace(
        debug=False,
        headers=[],
        method='GET',
        traceback=False,
        body=True,
        style='paraiso-light',
        prettify='colors',
        format_options={},
        ignore_stdin=False,
        timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
        download=False,
        stream=False
    )
    requests_message = requests.Response()
    with_headers = True
    with_body = True
   

# Generated at 2022-06-13 22:24:05.357501
# Unit test for function write_stream
def test_write_stream():
    # Setup
    ws = write_stream
    ws_wc_wp3 = write_stream_with_colors_win_py3
    global MESSAGE_SEPARATOR, MESSAGE_SEPARATOR_BYTES
    MESSAGE_SEPARATOR = '\n\n'
    MESSAGE_SEPARATOR_BYTES = MESSAGE_SEPARATOR.encode()
    # Unit test for function write_stream


# Generated at 2022-06-13 22:24:16.337847
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import json

    def dict_str_int_recursive(d: dict) -> dict:
        """ Recursively replace all the string in dict with int type and returns a dict
        """
        return {int(k) if k.isdigit() else k: dict_str_int_recursive(v) if isinstance(v, dict) else int(v)
                for k, v in d.items()}

    def dict_str_int_nonrecursive(d: dict) -> dict:
        """ Recursively replace all the string in dict with int type and returns a dict
        """
        for key in d:
            d[key] = int(d[key]) if str(d[key]).isdigit() else d[key]
        return d


# Generated at 2022-06-13 22:24:28.070315
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.input import ParseOptions
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import EncodedStream
    from httpie.cli.argtypes import KeyValueArg
    import httpie
    import argparse
    env = Environment()
    options = ParseOptions(args=[], env=env)
    args = httpie.cli.parser.parse_args(args=[], env=env)
    args.prettify = False
    args.stream = False
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env': env})
    args.prettify = False
    args.stream = True
    assert get_stream_type_and_kwargs(env, args) == (EncodedStream, {'env': env})
    env

# Generated at 2022-06-13 22:24:49.429529
# Unit test for function write_message
def test_write_message():

    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.core import main
    from utils import TestEnvironment, http, HTTP_OK

    env = TestEnvironment(stdin_isatty=True, stdout_isatty=False)
    r = http('GET', HTTP_OK, env=env)
    assert r == http('GET', HTTP_OK, '--pretty=none', env=env)
    assert 0 == r.exit_status

    # $ echo 'GET /' |./http --stream --pretty=none
    r = http(
        'GET', HTTP_OK, '--stream', '--pretty=none',
        env=Environment(stdin_isatty=False, stdout_isatty=False)
    )
    assert r.exit_

# Generated at 2022-06-13 22:24:57.558542
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from httpie.output.streams import ColorizedStream
    env = Environment()
    sio = StringIO()
    sio.encoding = 'utf8'
    args = argparse.Namespace(prettify='colors')
    stream = ColorizedStream('haha', env=env, formatting=Formatting(env, args.prettify, 'Solarized', False, {}))
    write_stream_with_colors_win_py3(stream, sio, False)

# Generated at 2022-06-13 22:25:02.823864
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest()
    env = Environment()
    env.stdout = Mock(spec=IO)
    env.stderr = Mock(spec=IO)
    env.stdout_isatty = Mock(spec=IO)
    env.is_windows = False
    args = argparse.Namespace()
    args.debug = True
    args.traceback = True
    args.stream = True
    with_headers = True
    with_body = True
    assert_not_equal(
        write_message(requests_message, env, args, with_headers, with_body), None)

# Generated at 2022-06-13 22:25:12.253693
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    # pytest.skip()
    from io import StringIO

    stream = StringIO()
    colors = ('bold', 'green', 'red', 'default')
    try:
        write_stream(
            stream=build_output_stream_for_message(
                args=argparse.Namespace(prettify=colors),
                env=Environment(is_windows=True, stdout_isatty=True, colors_256=False),
                requests_message=requests.Response(),
                with_headers=False,
                with_body=False,
            ),
            outfile=StringIO(),
            flush=False,
        )
    except UnicodeDecodeError:
        pytest.xfail('Not fixed yet')

# Generated at 2022-06-13 22:25:23.749217
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class TestEnv():
        def __init__(self, is_stdout_atty):
            self.stdout_isatty = is_stdout_atty
    
    class TestArgs():
        def __init__(self, is_json, is_stream, prettify, style, options):
            self.json = is_json
            self.stream = is_stream
            self.prettify = prettify
            self.style = style
            self.format_options = options

    env = TestEnv(False)
    args = TestArgs(False, False, False, False, False)
    assert get_stream_type_and_kwargs(env, args) == (RawStream, {'chunk_size': 16384})
    
    env = TestEnv(True)

# Generated at 2022-06-13 22:25:35.864837
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    """This test case is to test the function get_stream_type_and_kwargs"""
    args = argparse.Namespace()
    env = 'env'
    args.prettify = []
    args.stream = True
    args.style = 'color'
    args.json = 'json'
    args.format_options = 'format_options'
    # call function
    result_1 = get_stream_type_and_kwargs(env, args)
    assert result_1[0].__name__ == 'PrettyStream'
    assert result_1[1]['env'] == 'env'
    assert result_1[1]['conversion'] == Conversion()
    assert result_1[1]['formatting'].env == 'env'
    assert result_1[1]['formatting'].groups == []

# Generated at 2022-06-13 22:25:49.307115
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.downloads import ResponseProcessor, get_unique_filename
    from httpie.input import SEP_CREDENTIALS
    from httpie.styles import AUTH_CONFIG_KEY, build_style_map
    from httpie.compat import str
    import os
    import tempfile
    import platform
    is_windows = platform.platform().startswith('Windows')

    args = argparse.Namespace()
    auth = ('user', 'password')
    args.auth = SEP_CREDENTIALS.join(auth)
    args.ignore_stdin = True
    args.stream = False
    args.prettify = ['b']
    args.headers = ['Accept: application/json', 'X-Custom: Test']
    args.style = 'parrot'
    args.output = None
    args

# Generated at 2022-06-13 22:25:57.360940
# Unit test for function write_message
def test_write_message():
    import requests
    import json
    # requests.post('http://httpbin.org/post', data = {'key':'value'})
    # r = requests.post('http://httpbin.org/post', data = {'key':'value'})
    args = {}
    env = {'stdout': True, 'is_windows': True, 'stdout_isatty': True}
    # HTTPRequest HTTPResponse
    req = HTTPRequest(requests.post('http://httpbin.org/post', data={'key': 'value'}))
    # stream = PrettyStream(req, with_headers=True, with_body=True, env=env, explicit_json=True, format_options='', formatting='colors', conversion=None)
    # stream = get_stream_type_and_kwargs(env=

# Generated at 2022-06-13 22:26:07.028273
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    url = 'https://httpbin.org/anything/'
    output_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }
    res = requests.get(url+'test')
    response_class = output_class[type(res)]
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=Environment(),
        args=argparse.Namespace(),
    )
    stream = stream_class(
        msg=response_class(res),
        with_headers=True,
        with_body=True,
        **stream_kwargs,
    )

# Generated at 2022-06-13 22:26:14.907669
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout_isatty = True
    args = argparse.Namespace(prettify=None)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': env}

    args = argparse.Namespace(prettify=['headers'], stream=True, style='default', json=False, format_options={})
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream

# Generated at 2022-06-13 22:26:31.636723
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import HTTPOutputStream
    env = Environment(stdout_isatty=False)
    args = argparse.Namespace(
        stream=False,
        prettify=False,
        style=None,
        json=None,
        format_options=[])
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert stream_class == EncodedStream
    assert (stream_kwargs['env'] == env)
    args = argparse.Namespace(
        stream=True,
        prettify=True,
        style=None,
        json=None,
        format_options=[])
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)

# Generated at 2022-06-13 22:26:39.259039
# Unit test for function write_stream
def test_write_stream():
    data = b'hello'
    class dummy:
        def __init__(self):
            self.buf = None
        def write(self, b):
            self.buf = b
        def buffer(self):
            return self
        def read(self):
            return self.buf
    outfile = dummy()
    stream = BaseStream(iter([data]))
    write_stream(stream, outfile, flush=False)
    assert outfile.read() == data

# Generated at 2022-06-13 22:26:52.693838
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class DummyEnvironment:
        def __init__(self):
            self.stdout_isatty = True

    class DummyArgumentParser:
        def __init__(self):
            self.stream = True
            self.prettify = False

    env = DummyEnvironment()
    args = DummyArgumentParser()
    assert get_stream_type_and_kwargs(env, args)[0] == EncodedStream

    args.stream = False
    args.prettify = True
    assert get_stream_type_and_kwargs(env, args)[0] == BufferedPrettyStream
    assert get_stream_type_and_kwargs(env, args)[1]['formatting'].groups == False

    env.stdout_isatty = False
    args.stream = True

# Generated at 2022-06-13 22:27:04.865695
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.core import main_impl
    from httpie import ExitStatus
    from pygments import highlight
    from pygments.formatters import TerminalFormatter
    from pygments.lexers import JsonLexer
    import json

    args = main_impl.parser.parse_args([
        '--json',
        '--pretty', 'all',
        '--style', 'paraiso-dark',
        'http://httpbin.org/get',
    ])

    env = main_impl.get_environment(args, 80000)

    body_json = json.loads(env.stdin.read())
    requests_message = main_impl.get_requests_message(
        args,
        env,
        body_json
    )

    chunk = []

# Generated at 2022-06-13 22:27:18.051331
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import sys
    from httpie import __version__
    from httpie.cli import parser
    #sys.stderr = io.StringIO()
    args = parser.parse_args(args=[])

    # sys.version = '3.5.2 (default, Sep 14 2017, 22:51:06) \n[GCC 5.4.0 20160609]'
    # sys.platform = 'win32'
    # sys.stdout = io.StringIO()
    # sys.stdout_isatty = True
    from httpie import Environment
    env = Environment(args, __version__)
    #print(env.stdout.write)
    #print(env.stdout.flush)
    #print(env.stdout_isatty)

    from httpie.utils import get_local_add

# Generated at 2022-06-13 22:27:29.512338
# Unit test for function get_stream_type_and_kwargs

# Generated at 2022-06-13 22:27:40.984788
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie import env
    from httpie.constants import (
        BINARY_SUPPRESSED_NOTICE,
        UNREPRESENTABLE_CONTROL_CHAR_FMT
    )

    old_stdout = env.stdout
    env.stdout = io.StringIO()

    test_args = argparse.Namespace(
        stream=True,
        output_file='/tmp/output.txt',
        verify=True,
        debug=False,
        traceback=False,
        pretty='all',
        style='native',
        json=False,
        format_options=[],
    )

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, test_args)
    # assert stream_class is PrettyStream
    assert stream_kwargs['env'] == env

# Generated at 2022-06-13 22:27:50.167578
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from click.testing import CliRunner
    from httpie import cli

    runner = CliRunner()
    result = runner.invoke(cli.main, ['https://httpbin.org/get'])
    assert result.exit_code == 0
    assert result.stdout == '{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "HTTPie/x.y.z"\n  }, \n  "origin": "xx.xx.xx.xx", \n  "url": "https://httpbin.org/get"\n}\n'

# Generated at 2022-06-13 22:28:04.204933
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.utils import write_stream_with_colors_win_py3
    chunks = [b'abc', b'\x1b[35;1mdef\x1b[0m', b'ghi']
    outfile = io.BytesIO()
    write_stream_with_colors_win_py3(
        args=None,
        env=None,
        stream=chunks,
        outfile=outfile,
        flush=False
    )
    assert chunks == outfile.getvalue().split(b'\n')
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(
        args=None,
        env=None,
        stream=chunks,
        outfile=outfile,
        flush=False
    )

# Generated at 2022-06-13 22:28:08.691518
# Unit test for function write_stream
def test_write_stream():
    requests_message = requests.PreparedRequest()
    env = Environment(True, True)
    args = argparse.Namespace(prettify=None, debug=False, traceback=False, stream=True)
    with_headers = True
    with_body = True

# Generated at 2022-06-13 22:28:25.750439
# Unit test for function write_message
def test_write_message():
    import pytest
    from httpie import ExitStatus
    from httpie.cli import parser
    exit_status, error = pytest.main(['-x', 'httpie'])
    assert exit_status == ExitStatus.OK
    assert not error

    env = Environment(
        colors=256,
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    args = parser.parse_args(args=['--json',''], env=env)
    with pytest.raises(SystemExit):
        write_message(b'', env, args)

    args = parser.parse_args(args=['--pretty=all',''], env=env)

# Generated at 2022-06-13 22:28:34.823946
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.cli import parser
    from httpie.context import Environment
    args = parser.parse_args(['example.com'])
    env = Environment()

    # enable all types of prettify
    args.prettify = 'all'
    args.stream = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream
    assert 'env' in stream_kwargs
    assert isinstance(stream_kwargs['conversion'], Conversion)
    assert isinstance(stream_kwargs['formatting'], Formatting)
    assert 'groups' in stream_kwargs['formatting'].__dict__
    assert stream_kwargs['formatting'].__dict__['groups'] == 'all'


# Generated at 2022-06-13 22:28:49.478348
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(
        config=None,
        colors=True,
        stdin_isatty=False,
        stdout_isatty=True,
        stdin=None,
        stdin_raw=None,
        stdout=None,
        stdout_raw=None,
        stdout_is_redirected=False,
        is_windows=False,
        stdout_encoding=None,
        stdin_encoding=None
    )

# Generated at 2022-06-13 22:28:58.666663
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    output_stream_type, output_stream_kwargs = get_stream_type_and_kwargs(
        env=None, args=None)
    assert output_stream_type == EncodedStream
    assert output_stream_kwargs == {'env': None}

    output_stream_type, output_stream_kwargs = get_stream_type_and_kwargs(
        env=None, args={'prettify': ['colors'], 'stream': True})
    assert output_stream_type == PrettyStream

# Generated at 2022-06-13 22:29:08.764493
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    # b'\x1b[32m\x1b[1mfoo\x1b[22m\x1b[39m', b'bar\n',
    # b'\x1b[32m\x1b[1mbaz\x1b[22m\x1b[39m'
    colored_chunk_red = '\x1b[31m\x1b[1mfoo\x1b[22m\x1b[39m'.encode()
    colored_chunk_green = '\x1b[32m\x1b[1mfoo\x1b[22m\x1b[39m'.encode()

# Generated at 2022-06-13 22:29:09.581150
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:29:18.095768
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io
    import httpie.config
    httpie.config.DEFAULT_CONFIG_DIR = ''

    raw_request = b'GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: curl/7.18.0 (i486-pc-linux-gnu) libcurl/7.18.0 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.1\r\nAccept: */*\r\n\r\n'

# Generated at 2022-06-13 22:29:21.470337
# Unit test for function write_message
def test_write_message():
    import requests

    req_url = "https://www.google.com"
    response = requests.get(req_url)
    env = Environment()

    write_message(response, env, args, with_headers=True, with_body=True)

# Generated at 2022-06-13 22:29:32.498951
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import ColorizingStream
    from httpie.output.formatters.colors import WIN_PYTHON_3_COLOR_PREFIX
    import sys

    class MockOutfile:
        encoding = 'utf-8'
        buffer = sys.stdout

        def write(self, chunk):
            buffer.write(chunk)

        def flush(self):
            sys.stdout.flush()

    # PYTHON_3_COLOR_PREFIX is a byte string, and is the most likely
    # to be written to the stdout.
    output = (WIN_PYTHON_3_COLOR_PREFIX + b'color').decode('utf-8')
    stream = ColorizingStream(output.encode('utf-8'), 'json')
    write_stream_with_col

# Generated at 2022-06-13 22:29:39.536211
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # request object
    http_request = HTTPRequest()
    http_request.headers = {'name':'Vipul'}
    http_request.body = '{"name":"Vipul"}'

    # response object
    http_response = HTTPResponse()
    http_response.headers = {'name': 'Vipul'}
    http_response.body = '{"name":"Vipul"}'

    # env object
    env = Environment()

    # args object
    args = argparse.Namespace()

    with_headers = True
    with_body = True

    class BufferedPrettyStream(PrettyStream):
        """
        Buffered pretty output stream might be used for other purposes as well.
        """


# Generated at 2022-06-13 22:30:03.459501
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.cli.argtypes import KeyValueArg
    import io
    from io import BufferedIOBase
    from httpie.compat import is_py2, is_windows
    from httpie import constants as C
    from httpie.context import Environment
    from httpie.output.streams import (
        RawStream, BufferedPrettyStream, EncodedStream, PrettyStream)
    from httpie.output.processing import Conversion,Formatting

    args = argparse.Namespace()
    args.stream = True
    args.prettify = True
    args.style = 'default'
    args.json=True
    args.format_options = [KeyValueArg('Verbose',True)]

    env = Environment()
    env.is_windows = False
    env.stdout_isatty = True


# Generated at 2022-06-13 22:30:12.723444
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    httpRequest = requests.PreparedRequest()
    httpRequest.url = 'http://www.baidu.com'
    httpRequest.method = 'get'

# Generated at 2022-06-13 22:30:24.053691
# Unit test for function write_stream
def test_write_stream():

    from io import StringIO

    from httpie.core import main

    import json
    data = dict(a=0)

    # note that io.StringIO doesnt accept binary data
    try:
        json.dumps(data).encode('utf-8')
    except TypeError:
        a = data.copy()
        a['a'] = u'0'
        data = a

    env = Environment(
        colors=256,
        stdin=None,
        stdin_isatty=True,
        stdout=(StringIO()),
        stdout_isatty=False,
        stderr=None,
        stderr_isatty=False,
        is_windows=False
    )


# Generated at 2022-06-13 22:30:36.113660
# Unit test for function write_message
def test_write_message():
    from httpie.cli import get_parser
    from httpie.context import Environment
    from . import (
        HTTPBIN_URL, TestEnvironment,
        get_response
    )
    parser = get_parser()
    args = parser.parse_args(['https://httpbin.org/get'])
    env = TestEnvironment(args=args)
    args.check_status = False
    args.download = False
    args.follow = True
    args.timeout = 10.0
    args.json = False
    args.prettify = False
    args.stream = True
    args.traceback = False
    args.max_redirects = 5
    args.verify = True
    args.auth = None
    args.headers = None
    args.extra_headers = None
    args.method = 'GET'


# Generated at 2022-06-13 22:30:40.942992
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO

    stream = PrettyStream(None, None, None, None, None, None)
    outfile = StringIO()
    flush = False
    write_stream_with_colors_win_py3(stream, outfile, flush)

# Generated at 2022-06-13 22:30:51.536377
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    from httpie.args import Parser
    from httpie.models import Request
    from httpie.compat import is_windows
    from httpie import ExitStatus

    args = Parser().parse_args(args=[])
    env = Environment(
        vars={
            'HTTPIE_CONFIG_DIR': '.httpie'
        },
        stdin=None,
        stdout=None,
        stderr=None,
        is_windows=is_windows
    )
    env.stdin.isatty = True
    env.stdout.isatty = False
    env.stderr.isatty = True
    env.stdout_isatty = False


# Generated at 2022-06-13 22:30:59.290232
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.cli import parser
    from httpie.compat import is_windows
    args = parser.parse_args()
    env = Environment(vars={'TERM': ''})
    # Unix, no prettify
    assert get_stream_type_and_kwargs(env, args)[0] == RawStream
    # Unix, prettify
    args.prettify = True
    assert get_stream_type_and_kwargs(env, args)[0] == BufferedPrettyStream
    # Windows, no prettify
    env = Environment(vars={'TERM': 'xterm'})
    assert get_stream_type_and_kwargs(env, args)[0] == EncodedStream
    # Windows, prettify
    args.prettify = True

# Generated at 2022-06-13 22:31:06.596193
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    args = argparse.Namespace()
    env = Environment()
    requests_message = requests.Request(method="GET", url='http://www.baidu.com', headers={}, data=None)
    with_headers = True
    with_body = True
    write_message(requests_message,env,args,with_headers,with_body)

# Generated at 2022-06-13 22:31:15.315062
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class TestStdOutIsATTY:
        def __init__(self, isatty):
            self.isatty = isatty

        def isatty(self):
            return False

    class TestEnv:
        def __init__(self, stdout_isatty, set_headers=None):
            self.stdout_isatty = stdout_isatty
            self.set_headers = set_headers

    class TestArgs:
        def __init__(self, prettify, stream, style, json, format_options):
            self.prettify = prettify
            self.stream = stream
            self.style = style
            self.json = json
            self.format_options = format_options

    # test case 1:
    # stdout.isatty() == False, prettify == True,

# Generated at 2022-06-13 22:31:23.266608
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.compat import is_windows
    from httpie.cli import parser
    env = Environment(stdout_isatty=True, stderr_isatty=True)
    args = parser.parse_args(['--style=solarized-dark'])
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class.__name__ == 'PrettyStream'
    assert stream_kwargs['formatting'].color.__name__ == 'ColorSchemeSolarizedDark'


# Generated at 2022-06-13 22:31:49.815916
# Unit test for function write_stream
def test_write_stream():
    with open('/tmp/test', 'w+') as f:
        write_stream(EncodedStream(HTTPRequest(requests.Request('GET', 'http://example.org'))), f, False)

# Generated at 2022-06-13 22:31:55.642630
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(
        prettify=None,
        stream=False
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert stream_class == EncodedStream
    assert stream_kwargs == {
        'env': env
    }

# Generated at 2022-06-13 22:32:06.662903
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie import ExitStatus
    from httpie.core import main
    from httpie.input import ParseError
    from tests.data import (
        FILE_PATH_ARG_PE,
        FILE_PATH_ARG_PE_OUTPUT,
        FILE_PATH_REQ,
        FILE_PATH_REQ_OUTPUT,
        FILE_PATH_RESP,
        FILE_PATH_RESP_OUTPUT,
        JSON_FILE_PATH_ARG,
        JSON_FILE_PATH_ARG_OUTPUT,
        JSON_FILE_PATH_REQ,
        JSON_FILE_PATH_REQ_OUTPUT,
        JSON_RESP,
        JSON_RESP_SIMPLE_OUTPUT,
    )

    # Test for "http  <file>"

# Generated at 2022-06-13 22:32:11.041586
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import os
    import subprocess
    import sys
    import tempfile
    from httpie.core import main
    from httpie.core import main

    with tempfile.NamedTemporaryFile('wb') as f:
        env = Environment(stdin=f,
                          stdout=f,
                          stderr=f,
                          is_windows=False)
        args = main.parser.parse_args(['--debug'])

        message = 'HTTP/1.1 200 OK' + '\r\n' + 'Content-Type: text/plain' + '\r\n' +\
                  '\r\n' + 'OK'
        request = requests.Request('GET', 'http://httpbin.org/headers')
        request.prepare()
        request.body = message

# Generated at 2022-06-13 22:32:20.009973
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Test the function write_stream_with_colors_win_py3
    """
    buf = io.StringIO()
    buf.encoding = 'utf-8'
    stream = [b'\x1b[1mhaha', b'\x1b[0m']
    # buf.write don't need encoding
    write_stream_with_colors_win_py3(stream, buf, True)
    buf.seek(0)
    assert buf.readlines() == ['\x1b[1mhaha\x1b[0m']

# Generated at 2022-06-13 22:32:27.780653
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # Generate stream
    output = build_output_stream_for_message(None, None, None, None, False)
    # Create an iterable
    output = iter(output)
    # Get the first item of iterable
    output = next(output)
    # Check if the output is an instance of BaseStream
    assert isinstance(output, BaseStream) == True

# Generated at 2022-06-13 22:32:40.008033
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.plugins import plugin_manager
    from httpie.context import Environment
    from httpie import ExitStatus
    from httpie.cli.parser import parser
    from httpie.config import Config
    from httpie.output.streams import (
        BaseStream, BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.models import HTTPRequest, HTTPResponse
    from httpie.output.processing import Conversion, Formatting

    _, args, env_config = parser.parse_args(
        "httpie -v",
        config=Config(stdin_isatty=True, stdout_isatty=True)
    )

# Generated at 2022-06-13 22:32:45.649041
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():

    class test_stream(BaseStream):
        def __init__(self, msg, color, no_color, color_and_no_color):
            self.msg = msg
            self.color = color
            self.no_color = no_color
            self.color_and_no_color = color_and_no_color
            self.counter = 0

        def __iter__(self):
            yield self.color
            yield self.color_and_no_color
            yield self.no_color

        def __next__(self):
            if self.counter < 3:
                res = next(iter(self))
                self.counter += 1
                return res
            else:
                raise StopIteration

    class test_outfile:
        def __init__(self):
            self.written = ''
            self.encoding