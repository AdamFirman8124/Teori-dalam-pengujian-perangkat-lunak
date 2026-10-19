

# Generated at 2022-06-13 22:23:01.841593
# Unit test for function write_message
def test_write_message():
    import io
    import sys
    from httpie import ExitStatus
    sys.stderr = io.StringIO()
    env = Environment(
        stdin=io.StringIO(),
        stdout=io.StringIO(),
        stderr=sys.stderr,
        stdout_isatty=False,
        stdin_isatty=False,
        color=True,
    )
    parser = env.argparser
    args = parser.parse_args([], env)
    req = requests.PreparedRequest()
    req.body = 'h1'
    write_message(
        requests_message=req,
        env=env,
        args=args,
        with_headers=True,
        with_body=True,
    )


# Generated at 2022-06-13 22:23:11.853311
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import filecmp
    args = argparse.Namespace()
    env = Environment(stdin=None, stdout=None, stderr=None,
                      is_windows=False)
    from . import utils
    requests_message = utils.get_response()
    with_headers = True
    with_body = True
    stream = build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=requests_message,
        with_headers=with_headers,
        with_body=with_body
    )
    filename = "test_build_output_stream_for_message1.txt"
    f = open(filename, 'wb')
    for chunk in stream:
        f.write(chunk)
    f.close()

# Generated at 2022-06-13 22:23:25.128219
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    args = argparse.Namespace(style='colors')
    env = Environment()
    outfile = StringIO()
    chunk1 = b'abcd\x1b[31m'
    chunk2 = b'efgh'
    chunk3 = b'\x1b[32m'
    chunk4 = b'ijkl'
    chunk5 = b'\x1b[0m'
    chunk6 = b'mn\nop'
    chunk7 = b'\x1b[0m'
    chunk8 = b'q\x1b[0mr'
    stream = [chunk1, chunk2, chunk3, chunk4, chunk5, chunk6, chunk7, chunk8]

# Generated at 2022-06-13 22:23:38.465588
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(
        stdin=None,
        stdin_isatty=False,
        stdout=sys.stdout,
        stdout_isatty=True,
        stderr=sys.stderr,
        stderr_isatty=False,
        colors=256,
        emulator=None,
        is_windows=(os.name == 'nt'),
        raw_mode=False,
    )

# Generated at 2022-06-13 22:23:39.228324
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    return

# Generated at 2022-06-13 22:23:49.940543
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream, PrettyStream, EncodedStream

    from httpie.context import Environment
    from httpie.models import JSONDict
    from httpie.config import Config

    args = JSONDict(prettify="all", style="foo", json=False)
    env = Environment(stdout_isatty=True, config=Config())
    cls, kwargs = get_stream_type_and_kwargs(env=env, args=args)
    assert cls == PrettyStream
    assert kwargs["env"] == env
    assert kwargs["conversion"]
    assert kwargs["formatting"].env == env
    assert kwargs["formatting"].groups == "all"
    assert kwargs["formatting"].color_scheme == "foo"
    assert k

# Generated at 2022-06-13 22:23:57.519714
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from httpie.output.streams import PrettyStream

    outfile = StringIO()
    stream = PrettyStream(
        msg=None,
        with_headers=True,
        with_body=True,
        env=None,
        conversion=None,
        formatting=Formatting(
            env=None,
            groups=('colors',),
            color_scheme='nocolor',
            explicit_json=False,
            format_options={},
        )
    )
    for chunk in stream:
        if '\x1b[' in chunk:
            outfile.write(chunk.decode('utf-8'))
        else:
            outfile.buffer.write(chunk)
        outfile.flush()
    assert outfile.getvalue()

# Generated at 2022-06-13 22:24:06.762282
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    print("test_get_stream_type_and_kwargs")
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(
        prettify=False, stream=False, style='default', json=True,
        format_options=[])))
    print("------------")

    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(
        prettify=True, stream=False, style='default', json=True,
        format_options=[])))
    print("------------")
    print(get_stream_type_and_kwargs(Environment(), argparse.Namespace(
        prettify=True, stream=True, style='default', json=True,
        format_options=[])))
    print("------------")

# Generated at 2022-06-13 22:24:16.874765
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output.streams import PrettyStream
    from httpie.models import HTTPRequest

    args = argparse.Namespace(
        stream=False,
        pretty=True,
        colors=None
    )
    env = Environment()
    env.set_stdout()
    env.set_stderr()
    requests_message = requests.PreparedRequest()
    requests_message.url = "https://www.google.com"
    requests_message.headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0"
    }
    requests_message._body = "hello"
    requests_message.method = "GET"
    with_headers = True
    with_body = True
    stream_kw

# Generated at 2022-06-13 22:24:28.374115
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.config import Config
    args = argparse.Namespace(prettify=None, style=None, stream=None, json=None, format_options={})
    env = Environment(Config())
    assert get_stream_type_and_kwargs(env, args)[0] == RawStream
    args = argparse.Namespace(prettify=None, style=None, stream=True, json=None, format_options={})
    assert get_stream_type_and_kwargs(env, args)[0] == RawStream
    args = argparse.Namespace(prettify=['all'], style=None, stream=None, json=None, format_options={})
    assert get_stream_type_and_kwargs(env, args)[0] == PrettyStream #BufferedPrettyStream
    args = argparse.Names

# Generated at 2022-06-13 22:24:48.555171
# Unit test for function write_message
def test_write_message():
    args = argparse.Namespace()
    req = requests.PreparedRequest()
    req.url = "http://httpbin.org/get"
    req.method = "GET"
    req.headers["Accept"] = "text/plain"
    req.headers["Accept-Encoding"] = "gzip, deflate"
    req.headers["Connection"] = "keep-alive"
    req.headers["Host"] = "httpbin.org"
    req.headers["User-Agent"] = "Python-Requests/2.22.0"

    env = Environment()
    env.stdout = sys.stdout
    env.stdout_isatty = True
    env.stderr = sys.stderr
    args.debug = False
    args.traceback = False
    args.prettify = ['colors']

# Generated at 2022-06-13 22:24:50.875437
# Unit test for function write_stream
def test_write_stream():
    # Neglect the first if statement due to exceptional case
    return 1

# Generated at 2022-06-13 22:25:00.227446
# Unit test for function write_stream
def test_write_stream():
    stream = ['a', 'b', 'c']
    outfile = StringIO()

    # write the stream
    write_stream(stream=stream, outfile=outfile)
    assert outfile.getvalue() == 'abc'

    # write the stream
    outfile = StringIO()
    write_stream(stream=stream + stream, outfile=outfile, flush=True)
    assert outfile.getvalue() == 'ab'

    # write the stream again
    outfile = StringIO()
    write_stream(stream=stream, outfile=outfile, flush=True)
    assert outfile.getvalue() == 'abc'

# Generated at 2022-06-13 22:25:06.727137
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest()
    env = Environment()
    env.stdout = "test"
    args = argparse.Namespace
    with_headers=True
    with_body=False
    write_message(requests_message, env, args, with_headers, with_body)

test_write_message()

# Generated at 2022-06-13 22:25:07.377773
# Unit test for function write_message
def test_write_message():
    pass

# Generated at 2022-06-13 22:25:13.440036
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    stream = [b'foo\x1b[10mbar\x1b[0m']
    outfile = io.StringIO()
    flush = False
    write_stream_with_colors_win_py3(stream, outfile, flush)
    assert outfile.getvalue() == 'foo\x1b[10mbar\x1b[0m'

# Generated at 2022-06-13 22:25:20.659724
# Unit test for function write_message
def test_write_message():
    from httpie.output.streams import Stream
    class TestStream(Stream):
        def __init__(self, msg, with_headers, with_body, **kwargs):
            super(TestStream, self).__init__(msg, with_headers, with_body)
            self.kwargs = kwargs
        def __iter__(self):
            yield "test_write_message"
    print(write_message(None, None, None, None, None))
    pass

# Generated at 2022-06-13 22:25:34.615419
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream, PrettyStream, \
        BufferedPrettyStream, EncodedStream

    env = Environment(stdout_isatty=True)
    args = argparse.Namespace()

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class in [RawStream, PrettyStream, BufferedPrettyStream, EncodedStream]
    assert len(stream_kwargs) > 0

    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=['colors'])

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class in [RawStream, PrettyStream, BufferedPrettyStream, EncodedStream]

# Generated at 2022-06-13 22:25:44.223737
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import sys
    import json
    from httpie.cli import parser
    import httpie.cli.output
    from httpie.output.streams import PrettyStream
    from httpie import httpsession
    from httpie import __version__ as httpie_version

    env = Environment(
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
        version=httpie_version,
        colors=256,
        config_dir=None,
        config_path=None,
        is_windows=(sys.platform == 'win32'),
    )
    args = parser.parse_args(['-p'])


# Generated at 2022-06-13 22:25:50.870537
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.cli import parser
    parser_args = parser.parse_args([])
    args = parser_args
    env = Environment(parser_args=args)
    assert get_stream_type_and_kwargs(env, args)[0].__name__ == 'EncodedStream'
    assert get_stream_type_and_kwargs(env, args)[1] == {'env': env}

# Generated at 2022-06-13 22:26:08.031252
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    parser = argparse.ArgumentParser()
    args = parser.parse_args([])

    # RawStream
    env.stdout_isatty = False
    args.prettify = ''
    args.stream = False

    stream_type, _ = get_stream_type_and_kwargs(env, args)
    assert stream_type is RawStream
    args.stream = True
    stream_type, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_type is RawStream
    assert stream_kwargs['chunk_size'] is RawStream.CHUNK_SIZE_BY_LINE

    # BufferedPrettyStream
    args.stream = False
    args.prettify = 'all'
    env.stdout_isatty = True
   

# Generated at 2022-06-13 22:26:12.624441
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest(
        method='GET',
        url='https://www.google.com',
        headers={}
    )

    #request.headers.get('Host')
    env = Environment()
    args = argparse.Namespace()
    with_headers = False
    with_body = False
    write_message(requests_message, env, args, with_headers, with_body)

# Generated at 2022-06-13 22:26:13.908999
# Unit test for function write_stream
def test_write_stream():
    b'\n\n'

# Generated at 2022-06-13 22:26:24.893268
# Unit test for function write_message
def test_write_message():
    class PreparedRequest:
        pass

    class Response:
        pass

    class Stdout:
        outfile = 'stdout'
        def write(self, data):
            print(data)
        def __getattr__(self, name):
            return None

    class Stderr:
        outfile = 'stderr'
        def write(self, data):
            print(data)
        def __getattr__(self, name):
            return None

    class Env:
        stdout = Stdout()
        def __getattr__(self, name):
            return None

    class Args:
        def __getattr__(self, name):
            return None

    env = Env()
    args = Args()
    requests_message = PreparedRequest()


# Generated at 2022-06-13 22:26:35.466948
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from six import BytesIO

    env = Environment()
    env.stdout = BytesIO()
    env.stdout_isatty = True
    env.is_windows = True
    args = argparse.Namespace(
        stream=False,
        prettify=['colors'],
    )

    # Test 1: check if text is written to stdout (output buffer) directly
    requests_message = requests.PreparedRequest()
    requests_message.body = '{"message": "hello"}'
    write_message(
        requests_message=requests_message,
        env=env,
        args=args,
        with_body=True,
        with_headers=True
    )

# Generated at 2022-06-13 22:26:45.093951
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import httpie
    class TestArgs:
        colors = 80
        pretty = 'all'
        style = 'solarized'
        stream = False
        debug = False
        traceback = False
        download = False
        output = None
        print_body = False
        json = False
    args = TestArgs()

    message = '{"hello": "world"}'
    url = 'https://httpbin.org/get'
    r = requests.get(url, data=message)
    r.json()

    for i in build_output_stream_for_message(args, httpie.context.Environment(), r, True, True):
        print(i.decode())

if __name__ == "__main__":
    test_build_output_stream_for_message()

# Generated at 2022-06-13 22:26:55.953074
# Unit test for function write_stream
def test_write_stream():
    import io

    data = {'message': 'Hello, world!'}
    in_stream = EncodedStream(HTTPRequest(
        requests.Request('GET', 'http://example.com', data)))
    out_stream = io.StringIO()

    write_stream(in_stream, out_stream, flush=False)


# Generated at 2022-06-13 22:27:07.606048
# Unit test for function write_stream

# Generated at 2022-06-13 22:27:08.409546
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    pass

# Generated at 2022-06-13 22:27:12.842160
# Unit test for function write_message
def test_write_message():
    write_message(requests.PreparedRequest, Environment, argparse.Namespace, with_headers=False, with_body=False)
    write_message(requests.Response, Environment, argparse.Namespace, with_headers=False, with_body=False)

# Generated at 2022-06-13 22:27:27.252695
# Unit test for function write_message
def test_write_message():
    pass


# Generated at 2022-06-13 22:27:35.550712
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Simulate a Windows Python 3 colorized terminal output session.

    """
    class Capture(object):
        """Output file-like object capturing (writing) to `self.capture`.

        """
        _buffer = b''

        def __init__(self, initial_contents=b''):
            self.capture = bytearray(initial_contents)

        @property
        def contents(self):
            return bytes(self.capture)

        def write(self, string):
            self._buffer += string.encode()
            while True:
                index = self._buffer.find(MESSAGE_SEPARATOR_BYTES)
                if index == -1:
                    break
                self._buffer = self._buffer[index + len(MESSAGE_SEPARATOR_BYTES):]


# Generated at 2022-06-13 22:27:45.875898
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import argparse
    from httpie.context import Environment
    from httpie.output.streams import PrettyStream
    env = Environment(stdout=io.StringIO(), stdout_isatty=True)
    args = argparse.Namespace(prettify=['colors'],style='default',stream=False)
    msg = HTTPRequest()
    message_stream = build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=msg,
        with_headers=True,
        with_body=True,
    )

    a = next(message_stream)
    assert isinstance(message_stream, PrettyStream)
    assert isinstance(a, bytes)

# Generated at 2022-06-13 22:27:57.707692
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    args.stream = False
    args.prettify = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert isinstance(stream_class, EncodedStream)
    assert stream_kwargs == dict(env=env)
    args.stream = True
    args.prettify = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert isinstance(stream_class, PrettyStream)
    assert stream_kwargs['env'] == env
    assert isinstance(stream_kwargs['conversion'], Conversion)

# Generated at 2022-06-13 22:28:06.947671
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests

    requests_message_req = requests.PreparedRequest()
    requests_message_resp = requests.Response()
    env = Environment()
    args = argparse.Namespace(prettify=['headers'])
    with_headers_true_with_body_true = True
    with_headers_true_with_body_false = False
    with_headers_false_with_body_true = True
    with_headers_false_with_body_false = False

    write_message(requests_message_req, env, args, with_headers_true_with_body_true)
    write_message(requests_message_req, env, args, with_headers_true_with_body_false)

# Generated at 2022-06-13 22:28:19.295336
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    assert(get_stream_type_and_kwargs(env, args) ==
           (EncodedStream, {'env': env}))
    args.prettify = ['all']
    assert(get_stream_type_and_kwargs(env, args) ==
           (BufferedPrettyStream, {
               'env': env,
               'conversion': Conversion(),
               'formatting': Formatting(
                   env=env,
                   groups=args.prettify,
                   color_scheme=args.style,
                   explicit_json=args.json,
                   format_options=args.format_options,
               )
           }
           ))
    args.stream = True

# Generated at 2022-06-13 22:28:32.110669
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    '''Use the function build_output_stream_for_message, then assert the type of
    the stream that was yielded, to see if it was of the right type.
    '''
    # Follows file output.py's test_get_stream_type_and_kwargs()
    from unittest import mock

    mock_args = mock.Mock()
    mock_args.prettify = True
    mock_args.stream = False
    mock_args.json = False
    mock_args.style = None
    mock_args.format_options = None

    mock_env = mock.Mock()
    mock_env.stdout_isatty = True

    mock_response = mock.Mock()
    mock_response.request = mock.Mock()

# Generated at 2022-06-13 22:28:38.272616
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    requests_message = requests.PreparedRequest()
    env = Environment()
    args = argparse.Namespace()
    with_headers = True
    with_body = True
    assert write_message(requests_message, env, args, with_headers, with_body)

# Generated at 2022-06-13 22:28:51.597141
# Unit test for function write_message
def test_write_message():
    from httpie.cli import parser
    from httpie.output.streams import OutBytesIO, OutFileWrapper
    from httpie.compat import urlencode
    import os
    import tempfile
    import requests
    from contextlib import contextmanager

    env = Environment()

    @contextmanager
    def capture(command, env=env, **kwargs):
        """
        Run a command and capture stdout/stderr.

        """
        args = ['http'] + command
        args = parser.parse_args(args)
        args.output_options = {}
        args.output_options.update(kwargs)
        env.stdout = OutBytesIO()
        env.stderr = OutBytesIO()


# Generated at 2022-06-13 22:29:05.794954
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from cStringIO import StringIO
    from httpie.output import COLOR_ENCODING, COLOR_RESET
    from httpie.output.streams import BaseStream

    encoding = COLOR_ENCODING
    stream = BaseStream(
        lambda _: [b'foo', b'\x1b[0m', b'bar', b'\x1b[0m'],
        with_body=True,
    )
    outfile = StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=False)
    outfile.seek(0)
    assert outfile.read() == 'foo{0}bar{0}'.format(COLOR_RESET).encode(encoding)
    outfile.close()

# Generated at 2022-06-13 22:29:26.637948
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from .colors import ColoredEnvironment

    from .config import Config

    args = argparse.Namespace()
    args.prettify = []
    env = ColoredEnvironment('red', 'utf8', "", "", "", "", Config())
    assert get_stream_type_and_kwargs(env=env, args=args)[0] == RawStream

    args.prettify = ['all']
    assert get_stream_type_and_kwargs(env=env, args=args)[0] == PrettyStream

    args.stream = True
    assert get_stream_type_and_kwargs(env=env, args=args)[0] == PrettyStream

# Generated at 2022-06-13 22:29:37.340456
# Unit test for function write_message
def test_write_message():
    import httpie
    from httpie import ExitStatus
    from httpie.core import main
    from httpie.compat import is_windows

    def do_main_with_streaming(*args, **kwargs):
        return main(args, **kwargs)

    def do_main_without_streaming(*args, **kwargs):
        kwargs.update(stream=False)
        return main(args, **kwargs)

    class TestStdoutIsTTY:
        def __init__(self, isatty_value):
            self.buffer = []
            self.isatty_value = isatty_value

        def isatty(self):
            return self.isatty_value

        def write(self, s):
            self.buffer.append(s)


# Generated at 2022-06-13 22:29:49.898244
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import argparse

    arg = argparse.Namespace(prettify='all')
    req = requests.PreparedRequest()
    req.method = 'GET'
    req.url = 'http://127.0.0.1:8080/test/'
    req.headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    req.body = '{"d":2}'

    res = requests.Response()
    res.status_code = 200
    res.headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    res.raw = b'{"d":2}'

    from httpie.context import Environment
    from httpie.output.streams import PrettyStream

    env = Environment(stdout_isatty=True)
   

# Generated at 2022-06-13 22:30:01.654746
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import get_response
    from httpie.core import main
    from httpie.compat import is_windows
    from httpie.output.streams import PrettyStream 
    import sys
    import os
    os.environ['COLUMNS']='120'
    os.environ['LINES']='120'
    sys.argv = ['http', '--json', 
                   '--pretty=all', 'localhost:5000/get/hello']
    fake_stdout = sys.stdout
    fake_stdout.flush()
    fake_stdout.write('{"message": "hello", "metadata": {"timestamp": "2020-06-14 19:46:57.885140"}}\n')
    sys.stdout=fake_stdout
    args = main()

# Generated at 2022-06-13 22:30:12.027010
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import sys
    import io

    # "http" will always contain at least one character, therefore
    # at least one byte. So the only difference is between
    # non-color-containing strings (HTTP status line) and color-containing
    # strings (colorized HTTP header).
    non_color_contatining_string = "http"
    color_containing_string = "http\x1b[0m\x1b[33m"

    stream_chunks = [
        b'\x1b[0m',  # Default color reset
        non_color_contatining_string.encode(),
        b'\x1b[0m',  # Default color reset
        color_containing_string.encode(),
    ]

    # In Python 3.X, sys.stdout is a TextIOBase, so in order to


# Generated at 2022-06-13 22:30:23.543291
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.output.streams import BaseStream
    from unittest.mock import patch
    from io import StringIO

    class Stream(BaseStream):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.data = [b'foo', b'\x1b[1mbar', b'\x1b[7mbaz']
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self) -> bytes:
            try:
                return self.data[self.index]
            finally:
                self.index += 1

    stream = Stream()
    outfile = StringIO()
    stream.reset()

# Generated at 2022-06-13 22:30:36.000385
# Unit test for function write_message
def test_write_message():
    import json
    import requests
    import requests_mock
    import requests_toolbelt
    from httpie.client import RawResponse
    from httpie.input import ParseError
    from httpie.output import streams

    class Args():
        def __init__(self):
            self.download=False
            self.output=None
            self.prettify=['all']
            self.stream=False
            self.headers=True
            self.body=True

    class Environment():
        def __init__(self):
            self.colors=256
            self.prefer_ipv6=False
            self.verify=False

    url='/'
    content="""abc123"""
    resp=requests.Response()
    resp.status_code=200

# Generated at 2022-06-13 22:30:47.053433
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():

    class MockWriter:
        def __init__(self, *args, **kwargs):
            self.written = []
            self.written_as_text = []

        def write(self, chunk):
            self.written_as_text.append(chunk)

        def buffer_write(self, chunk):
            self.written.append(chunk)

        def flush(self):
            pass

    args = argparse.Namespace(prettify=['colors'])
    writer = MockWriter()

# Generated at 2022-06-13 22:30:57.198378
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from tempfile import TemporaryFile
    from httpie.output.streams import BaseStream
    from httpie.output.streams import Colorized
    from httpie.output.streams import EncodedStream
    import platform
    # Save the current value of `platform.python_implementation`
    saved_platform_python_implementation = platform.python_implementation

    # Windows running Python 3
    platform.python_implementation = lambda: "CPython"
    outfile = TemporaryFile(mode='r+')
    outfile.write('Some text')
    outfile.seek(0)
    class MockSubclass(BaseStream):
        def __iter__(self):
            yield b'\x1b['
            yield ' Some'.encode('utf-8')
            yield Colorized.RESET_ALL

# Generated at 2022-06-13 22:31:07.526330
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    def test(
        stdout_isatty: bool,
        prettify_types: list,
        stream: bool,
        expected_stream_class: str,
        expected_stream_kwargs: dict
    ):
        env = Environment(stdout_isatty, 'x', 'x')
        args = argparse.Namespace(
            prettify=prettify_types,
            stream=stream,
            style='x',
            json=True,
            format_options=[],
        )
        stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
        assert isinstance(stream_class, type(eval(expected_stream_class)))
        assert stream_kwargs == expected_stream_kwargs


# Generated at 2022-06-13 22:31:41.591496
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():

    env = Environment(
        stdin_isatty=False,
        stdout_isatty=True,
        stdin=io.BytesIO(),
        stdout=io.BytesIO(),
        stderr=io.BytesIO(),
        colors=256,
        scheme='default',
    )

    class ArgNamespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    args = ArgNamespace(
        prettify='all',
        stream=False,
        style="default",
        json=False,
        format_options="",
    )

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class is BufferedPrettyStream
    assert stream_kwargs['env'] is env


# Generated at 2022-06-13 22:31:46.957876
# Unit test for function write_stream
def test_write_stream():
    stream:BaseStream = get_stream_type_and_kwargs(True, True)
    outfile = 'abc'
    flush = True
    result = write_stream(stream, outfile, flush)
    assert result == None

# Generated at 2022-06-13 22:31:57.445256
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    class Env:
        def __init__(self, isatty):
            self.stdout_isatty = isatty

    class MsgType:
        def __init__(self, msg):
            self.msg = msg

    class Args:
        def __init__(self, prettify=False, stream=False):
            self.prettify = prettify
            self.stream = stream

    class ReqArgs:
        def __init__(self, body='body'):
            self.body = body

    class PrepReq:
        def __init__(self, req_args, headers):
            self.headers = headers
            self.body = req_args.body

    class Resp:
        def __init__(self, headers, status_code):
            self.headers = headers
            self.status_

# Generated at 2022-06-13 22:32:07.074732
# Unit test for function write_message
def test_write_message():
    # 1.
    requests_message = requests.PreparedRequest()
    requests_message.url = 'https://httpbin.org/get'
    requests_message.headers = {'content-type': 'application/json'}
    requests_message.body = textwrap.dedent("""
        {
            "id": "1234",
            "name": [
                "jane",
                "doe"
            ]
        }
    """)
    env = Environment()
    env.stdout = sys.stdout
    env.stdout_isatty = True
    env.is_windows = False
    args = argparse.Namespace(prettify='colors', format='json', style='paraiso-dark')
    with_headers = True
    with_body = True

# Generated at 2022-06-13 22:32:17.721674
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.core import main
    from httpie.output.streams import DefaultStream, PrettyStream

    # class structure for test
    class FakeEnv:
        class FakeStdout:
            isatty = False

        def __init__(self):
            self.stdout = FakeEnv.FakeStdout()

    # class structure for test
    class FakeArgs:
        prettify = None
        stream = False
        style = 'default'
        json = True
        format_options = None

    def get_stream_type_and_kwargs_test(isatty=False, prettify=None, stream=False):
        env = FakeEnv()
        env.stdout.isatty = isatty
        args = FakeArgs()
        args.prettify = prettify
        args.stream = stream


# Generated at 2022-06-13 22:32:33.248840
# Unit test for function write_stream
def test_write_stream():
    import io
    import sys
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.env = Environment()

        def test_write_stream_with_colors_win_py3(self):
            import colorama
            colorama.init()
            self.env.is_windows = True
            stream = EncodedStream(env=self.env)
            outfile = sys.stdout
            flush = False
            write_stream_with_colors_win_py3(stream, outfile, flush)
            colorama.deinit()

        def test_build_output_stream_for_message(self):
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('--json', action='store_true')

# Generated at 2022-06-13 22:32:42.885166
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from .compat import BytesIO, StringIO

    def write_stream_call(**kwargs):
        from .outstreams import write_stream_with_colors_win_py3
        write_stream_with_colors_win_py3(**kwargs)

    out = BytesIO()
    stream = (b'\x1b[0mabc\x1b[34m', b'123\x1b[34m', b'\x1b[0m')
    expected = b'abc123\n'
    write_stream_call(stream=stream, outfile=out, flush=False)
    assert out.getvalue() == expected

    out = StringIO()