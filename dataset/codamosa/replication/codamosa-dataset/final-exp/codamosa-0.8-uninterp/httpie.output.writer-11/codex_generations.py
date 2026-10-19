

# Generated at 2022-06-13 22:23:02.764346
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    from httpie.models import HTTPRequest
    env = Environment()
    args = type('MyNamespace', (object,), {
        'prettify': [],
        'stream': False,
        'style': '',
        'json': False,
        'format_options': {},
    })
    request = HTTPRequest(
        requests.Request(None, 'GET', None, None, None, None, None).prepare()
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert stream_class is EncodedStream
    assert list(stream_class(msg=request, **stream_kwargs)) == [b'GET / HTTP/1.1\r\n']

# Generated at 2022-06-13 22:23:05.538450
# Unit test for function write_stream
def test_write_stream():
    outfile = StringIO()
    write_stream(['test'], outfile, True)
    assert outfile.getvalue() == 'test'



# Generated at 2022-06-13 22:23:06.640810
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    return


# Generated at 2022-06-13 22:23:13.731574
# Unit test for function write_stream
def test_write_stream():
    import io
    import io
    output = io.BytesIO()
    args = argparse.ArgumentParser(description='HTTPie argument parser.').parse_args([])
    env = Environment(stderr=io.StringIO(), stdin=io.StringIO(), stdout=io.StringIO())
    expect = b'\x1b[32mOK\x1b[0m'
    write_stream({expect}, output, True)
    output.seek(0)
    res = output.read()
    assert res == expect

# Generated at 2022-06-13 22:23:26.417652
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import os, sys
    import json
    env = Environment(stdout_isatty=False, colors=256)
    args = argparse.Namespace(
        traceback=True,
        print_headers='always',
        download=False,
        stream=True,
        prettify='all',
        style='paraiso-dark',
        json=False,
        format_options={}
    )

# Generated at 2022-06-13 22:23:39.364683
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    class FakeTextIOWrapper(TextIO):
        def __init__(self, data):
            self.buffer = FakeBytesIO(data)
            self.encoding = 'utf-8'

    class FakeBytesIO(BytesIO):
        def __init__(self, data):
            self.data = data
            BytesIO.__init__(self)

        def write(self, data):
            if isinstance(data, str):
                # we should be writing bytes
                raise ValueError
            else:
                self.data += data

    stdout = FakeTextIOWrapper(b"")
    data = (b'foo', b'\x1b[31mabc\x1b[39m', b'bar')
    write_stream_with_colors_win_py3(data, stdout, False)

# Generated at 2022-06-13 22:23:49.982871
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace(
        stream=False,
        prettify=True,
        style='automatic',
        format_options=argparse.Namespace(
            colors=argparse.Namespace(
                status=True,
                header=True,
                request_header=True,
                request_body=True,
                response_body=True,
                error=True
            ),
            indent=2,
            request_fields=None,
            response_fields=None,
            request_headers=None,
            response_headers=None,
        ),
        json=False,
        debug=False,
        traceback=False,
    )
    env = Environment()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )

# Generated at 2022-06-13 22:23:57.543197
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from httpie.core import main

    # Python 3
    from httpie import ExitStatus
    from utils import TestEnvironment, http

    args = ['--pretty=colors']
    env = TestEnvironment(stdin_isatty=True, stdout_isatty=False)
    r = http('--print=HBhb', args, env=env)
    assert r.exit_status == ExitStatus.ERROR
    assert 'Switch from binary' in r.stderr

    # Python 2
    env = TestEnvironment(stdin_isatty=True, stdin=StringIO(''),
                          stdout_isatty=False,
                          stdout=StringIO())
    r = main(args, env=env)
    assert r.exit_status == ExitStatus.OK

# Generated at 2022-06-13 22:24:06.762865
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.context import Environment
    from httpie.output.streams import (
        BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.output.processing import Conversion, Formatting
    env = Environment()
    args = argparse.Namespace()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == BufferedPrettyStream
    assert isinstance(stream_kwargs['conversion'], Conversion)
    assert isinstance(stream_kwargs['formatting'], Formatting)

    args.prettify = ['none']
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == EncodedStream

    env.stdout_isatty

# Generated at 2022-06-13 22:24:12.165031
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    import sys
    stream = EncodedStream(msg=HTTPRequest(requests.Request(method='GET', url='https://foo.com/?key=val')))
    outfile = StringIO()
    write_stream_with_colors_win_py3(stream, outfile, flush=True)
    print(outfile.getvalue())



# Generated at 2022-06-13 22:24:30.187475
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.plugins import plugin_manager
    import os

    plugin_manager.load_installed_plugins()
    args = parser.parse_args(args=['-v', 'POST', 'http://httpbin.org/post', '--json'])
    env = Environment(args,
                      stdin=sys.stdin,
                      stdout=sys.stdout,
                      stderr=sys.stderr)

    return build_output_stream_for_message(args=args,
                                           env=env,
                                           requests_message=None,
                                           with_headers=False,
                                           with_body=False)

# Generated at 2022-06-13 22:24:43.442380
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import sys
    env = Environment()
    env.stdout = sys.stdout

    http_request = requests.Request("GET", "http://127.0.0.1:8000/api/v1")
    http_request = http_request.prepare()
    http_request.headers['Content-Type'] = 'application/json'
    http_request.headers['Authorization'] = 'Token'
    http_request.body = "hello"

# Generated at 2022-06-13 22:24:51.996829
# Unit test for function write_message
def test_write_message():
    """
    Simple unit test
    """
    import httpie.cli
    from httpie.base import main
    from httpie.input import Parser
    from httpie.output import build_output_stream_for_message
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.streams import EncodedStream
    from httpie.output.streams import RawStream

    args = httpie.cli.parser.parse_args(['-j', 'https://httpbin.org/get'])
    parser = Parser()
    env = Environment(vars(args))
    request = parser.parse_request(args.url, args.method, args.items, env)
    requests_message = request.prepare()
    

# Generated at 2022-06-13 22:25:00.299294
# Unit test for function write_message
def test_write_message():
    import sys
    import os
    import requests
    import argparse
    import httpie.context
    import httpie.output.processin
    sys.path.append(".")
    test_requests_message = requests.PreparedRequest()
    test_requests_message.method = "GET"
    test_requests_message.headers = {}
    test_requests_message.body = b''
    env = httpie.context.Environment()
    env.stdout = sys.stdout
    args = argparse.Namespace(traceback = False, debug = False, verbose = False)
    write_message(test_requests_message, env, args)


# Generated at 2022-06-13 22:25:12.216811
# Unit test for function write_stream
def test_write_stream():
    class MockStdout(object):
        def __init__(self):
            self.data = []
        def buffer(self):
            return self
        def write(self, chunk):
            self.data.append(chunk)
        def size(self):
            return len(''.join(self.data))

    stdout = MockStdout()
    class MockRawStream(object):
        def __init__(self, msg, **_):
            self.msg = msg
            self.closed = False
        def __iter__(self):
            if not self.closed:
                self.closed = True
                yield self.msg
                yield b'\n'
        def close(self):
            pass

    # Request message with headers and body

# Generated at 2022-06-13 22:25:20.620618
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest
    env = Environment()
    args = argparse.Namespace(
        stream=True,
        prettify='all',
        style='parrot',
    )
    write_message(
        requests_message=requests_message,
        env=env,
        args=args,
        with_headers=True,
        with_body=True,
    )
    print(MESSAGE_SEPARATOR)
    print(MESSAGE_SEPARATOR_BYTES)

# Generated at 2022-06-13 22:25:34.562601
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import os
    import tempfile
    from httpie.output.streams import PrettyStream
    from httpie import Environment, ExitStatus

    def is_stream_class_equal_to(env: Environment, args:argparse.Namespace,
                                 expected_stream_class: Type[BaseStream]):
        actual_stream_class, _ = get_stream_type_and_kwargs(env=env, args=args)
        assert actual_stream_class == expected_stream_class

    # Test for RawStream

# Generated at 2022-06-13 22:25:38.751386
# Unit test for function write_stream
def test_write_stream():
    outfile=env.stdout
    flush=False

    class BaseStream:
        def __init__(self):
            self.stream = 1
        def __iter__(self):
            return iter([1,2,3])

    stream = BaseStream()

    assert write_stream(stream,outfile,flush)==None

# Generated at 2022-06-13 22:25:41.499683
# Unit test for function write_stream
def test_write_stream():
    stream = []
    outfile = []

    write_stream(
        stream,
        outfile,
        flush=False
    )

# Generated at 2022-06-13 22:25:50.870356
# Unit test for function write_stream
def test_write_stream():
    import sys
    import json
    import tempfile
    t = tempfile.NamedTemporaryFile(mode='w+')
    write_stream(stream=[b'hello_world'],outfile=sys.stdout,flush=True)
    write_stream(stream=[b'hello_world'],outfile=json,flush=True)
    write_stream(stream=[b'hello_world'],outfile=t,flush=True)
    write_stream(stream=[b'hello_world'],outfile=open('test','w'),flush=True)


# Generated at 2022-06-13 22:25:59.234099
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest()
    env = Environment()
    args = argparse.Namespace()
    res = write_message(requests_message, env, args)
    print(res)

# Generated at 2022-06-13 22:26:00.732533
# Unit test for function write_message
def test_write_message():
    assert write_message(1,1,1,1,1) == None

# Generated at 2022-06-13 22:26:07.931057
# Unit test for function write_message
def test_write_message():
    import io
    import sys

    f = io.StringIO()
    sys.stdout = f
    env = Environment()
    args = argparse.Namespace()
    write_message('aaaa', env, args, False, True)
    f.seek(0)
    first_line = f.readline()
    sys.stdout = sys.__stdout__
    f.close()

# Generated at 2022-06-13 22:26:15.388140
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import NoEnv
    env = NoEnv()
    args = parse_args("--verbose", "--headers", "--prettify=all", "--style=monokai",
                      "--json", "--debug", "--stream", "--format=all")
    pre_stream_class, pre_stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert pre_stream_class is PrettyStream
    assert len(pre_stream_kwargs) == 2
    assert pre_stream_kwargs['env'] is env
    assert pre_stream_kwargs['conversion'].__class__.__name__ == 'Conversion'
    assert pre_stream_kwargs['formatting'].__class__.__name__ == 'Formatting'

# Generated at 2022-06-13 22:26:27.296064
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli import parser
    args = parser.parse_args()
    env = Environment()

    data = {'test_data': 'test_data', 'test_data2': [1, 2, 3]}
    headers = {'test_header': 'test_header'}
    body = json.dumps(data).encode('utf8')
    request = requests.Request('POST', 'http://example.org', data=data)
    prepared = request.prepare()
    response = requests.Response()
    response.headers = headers
    response.status_code = 200
    response.raw = six.BytesIO(body)


# Generated at 2022-06-13 22:26:34.858241
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.context import Environment
    from httpie.output.streams import EncodedStream

    environment = Environment()
    # args = parser.parse_args()
    # requests_message = 
    # with_headers = False
    # with_body = False

    assert get_stream_type_and_kwargs(environment, args) == (EncodedStream, {'env': environment})

# Generated at 2022-06-13 22:26:41.029730
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(stream=True, prettify=True, style='default', json=True, format_options={})

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    stream = stream_class(env=env, **stream_kwargs)
    assert isinstance(stream, RawStream)
    assert stream.chunk_size == RawStream.CHUNK_SIZE_BY_LINE

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    stream = stream_class(env=env, **stream_kwargs)
    assert isinstance(stream, RawStream)

    env = Environment(stdout_isatty=True)
    stream_class, stream_kwargs = get_stream_

# Generated at 2022-06-13 22:26:55.623179
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import io

    class FakeStream(BaseStream):
        def __init__(self, chunks):
            self.chunks = chunks

        def __iter__(self):
            yield from self.chunks

    env = Environment(stdout=io.StringIO(), stderr=io.StringIO(), is_windows=True)
    outfile = env.stdout
    outfile.encoding = 'UTF-8'
    chunks = [
        # chunks should be bytes, but easier to read in the test if not.
        b'\x1b[32mfoo\x1b[0m',
        b'bar',
        '\x1b[1mbold\x1b[0m',
    ]
    # whitespace added so the "expected" value will have some whitespace

# Generated at 2022-06-13 22:27:07.393421
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import httpie
    from httpie.cli import parser
    from httpie import utils
    from httpie.output import streams

    from httpie.downloads import Downloader
    from httpie.plugins import plugin_manager
    from httpie.session import Session

    from httpie.input import ParseError
    from httpie.output import (
        build_output_stream_for_message,
        write_stream,
    )
    from httpie.status import ExitStatus

    args = parser.parse_args([])
    config = httpie.Config()
    env = httpie.Environment(args, config, session=Session())
    args.session = Session(exit_status=ExitStatus.SUCCESS)
    args.output_stream_class = streams.EncodedStream
    args.prettify = 'colors'

# Generated at 2022-06-13 22:27:08.287131
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    write_message

# Generated at 2022-06-13 22:27:21.602897
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.compat import isatty
    from httpie.output.streams import PrettyStream
    from httpie.output.streams import EncodedStream
    from httpie.output.streams import RawStream
    from httpie.output.streams import BufferedPrettyStream
    from httpie.context import Environment

    pretty_stream_type = {
        True: PrettyStream,
        False: BufferedPrettyStream
    }
    for is_tty in [True, False]:
        for is_stream in [True, False]:
            for is_prettify in [True, False]:
                env = Environment(isatty(1), isatty(2))
                args = argparse.Namespace()
                if is_tty:
                    args.prettify = ['colors'] if is_prettify else []

# Generated at 2022-06-13 22:27:22.217962
# Unit test for function write_stream
def test_write_stream():
    pass

# Generated at 2022-06-13 22:27:25.740445
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """ Should write encoded stream in color or for windows"""
    write_stream_with_colors_win_py3("Hello world", "Hello world", True)

# Generated at 2022-06-13 22:27:34.949542
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    test_obj = get_stream_type_and_kwargs(env, args)
    assert test_obj[0] == EncodedStream
    assert test_obj[1] == {'env': env}

    args.prettify = []
    test_obj = get_stream_type_and_kwargs(env, args)
    assert test_obj[0] == RawStream
    assert test_obj[1] == {'chunk_size': RawStream.CHUNK_SIZE}

    args.prettify = ['colors']
    test_obj = get_stream_type_and_kwargs(env, args)
    assert test_obj[0] == PrettyStream
    assert isinstance(test_obj[1]['conversion'], Conversion)
   

# Generated at 2022-06-13 22:27:35.680235
# Unit test for function write_message
def test_write_message():
    assert True


# Generated at 2022-06-13 22:27:46.745265
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import unittest
    import requests
    import sys

    class TestRawStream(unittest.TestCase):

        def test_output_stream_with_colors_win_py3(self):
            # init the stream
            class Args:
                prettify = ['colors']
                stream = False
            args = Args
            env = requests.Session()
            req = requests.PreparedRequest()
            req.body = '{}'
            req.headers = {'Content-Encoding': 'gzip'}
            req.method = 'GET'
            req.url = "http://httpbin.org/get"
            message = HTTPRequest(req)

# Generated at 2022-06-13 22:27:58.677156
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import httpie.output.streams as streams
    from mock import Mock
    
    requests_message = requests.PreparedRequest()
    args = Mock()
    env = Mock()
    
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    message_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }[type(requests_message)]
    out = list(stream_class(
        msg=message_class(requests_message),
        with_headers=False,
        with_body=False,
        **stream_kwargs,
    ))

# Generated at 2022-06-13 22:28:07.228882
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    args = argparse.Namespace()
    args.prettify = []
    args.stream = True
    env = Environment()

    requests_response = requests.PreparedRequest()
    requests_response.url = 'http://httpbin.org'
    requests_response.headers = {'Content-Type': 'text/plain'}
    with_headers = False
    with_body = False

    # tests that the returned object is an iterator
    assert hasattr(build_output_stream_for_message(args, env, requests_response, with_headers, with_body), '__iter__')

    # tests that the returned object has a method "next"
    assert hasattr(build_output_stream_for_message(args, env, requests_response, with_headers, with_body), '__next__')

# Generated at 2022-06-13 22:28:16.531214
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    args = argparse.Namespace()
    env = Environment()
    requests_message = requests.PreparedRequest()
    stream = BuildoutOutputStream(
        env=env,
        args=args,
        requests_message=requests_message,
    )
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(
        stream=stream,
        outfile=outfile,
        flush=False,
    )

# Generated at 2022-06-13 22:28:25.478136
# Unit test for function write_stream
def test_write_stream():
    requests_message = requests.Request('GET', 'url')
    args = argparse.Namespace(
        json='auto',
        prettify='colors'
    )
    env = Environment(
        stdout = sys.stdout,
        stderr = sys.stderr,
        stdout_isatty = True
        )
    with_headers = True
    with_body = True

    write_stream(requests_message, env, args, with_headers, with_body)

if __name__ == '__main__':
    test_write_stream()

# Generated at 2022-06-13 22:28:48.852254
# Unit test for function write_message
def test_write_message():
    # write_message(requests_message,env,args,with_headers=False,with_body=False):
    class FakeNamespace:
        def __init__(self):
            self.style = 'default'
            self.prettify = ('colors', 'format')
            self.format_options = {}

    class FakeHTTPRequest:
        def __init__(self):
            self.headers = 'Fake'
            self.request = 'Fake'
            self.url = 'Fake'
            self.error = None

        def __repr__(self):
            return self.url

    class FakeHTTPResponse:
        def __init__(self):
            self.headers = 'Fake'
            self.text = 'Fake'
            self.url = 'Fake'
            self.status_code = 'Fake'

# Generated at 2022-06-13 22:28:55.473221
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    outfile = StringIO()
    stream = [b'\x1b[32mfoo\x1b[39mbar', b'baz']
    write_stream_with_colors_win_py3(stream=stream,
                                     outfile=outfile,
                                     flush=False)
    assert outfile.getvalue() == '\x1b[32mfoo\x1b[39mbar' + 'baz'

# Generated at 2022-06-13 22:29:07.706055
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=True)
    result = get_stream_type_and_kwargs(env, args)
    assert len(result) == 2
    assert result == (BufferedPrettyStream, {'env': env,
                                             'conversion': Conversion(),
                                             'formatting': Formatting(env=env,
                                                                      groups=True,
                                                                      color_scheme=None,
                                                                      explicit_json=False,
                                                                      format_options=None)})

    env = Environment(stdout_isatty=True)
    args = argparse.Namespace(prettify=True, stream=True)
    result = get_stream_type_and_kwargs(env, args)


# Generated at 2022-06-13 22:29:20.405215
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    req = requests.Request('GET', 'http://httpbin.org/get')
    prepped = req.prepare()
    assert prepped.url == 'http://httpbin.org/get'
    assert prepped.method == 'GET'
    assert prepped.__str__() == 'GET http://httpbin.org/get'
    assert prepped.__bytes__() == b'GET http://httpbin.org/get'
    res = requests.get('http://httpbin.org/get')
    assert res.__str__() == 'GET http://httpbin.org/get'
    assert res.__bytes__() == b'GET http://httpbin.org/get'

# Generated at 2022-06-13 22:29:28.361724
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout_isatty = True
    args = argparse.Namespace()
    args.prettify = False
    args.stream = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert stream_class == PrettyStream
    assert stream_kwargs['env'] == env
    assert 'conversion' in stream_kwargs
    assert stream_kwargs['formatting'].env == env
    req = requests.PreparedRequest()
    message_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }[type(req)]

# Generated at 2022-06-13 22:29:37.975841
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # pylint: disable=too-many-locals

    import requests
    from httpie.config import Config
    from httpie.plugins import builtin
    from httpie.context import Environment
    from httpie.output.processing import Conversion, Formatting
    from httpie.output.streams import (
        BufferedPrettyStream, EncodedStream, PrettyStream, RawStream
    )
    from httpie.output import get_preferred_output_options

    def init_args():
        # type: () -> argparse.Namespace
        parser = builtin.get_parser()
        args_namespace = parser.parse_args([])
        args_namespace.output_options = get_preferred_output_options()
        return args_namespace


# Generated at 2022-06-13 22:29:49.941574
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # given
    env = Environment(stdout_isatty=True, stderr_isatty=True)
    args = argparse.Namespace(
        stream=True,
        prettify="all",
        style="default",
        json=False,
        debug=False,
        traceback=False
    )
    req = requests.PreparedRequest()
    req._url = "http://example.org/"
    req.headers = {}

    with open("httpie_test.txt", "rb") as f:
        req.body = f.read()

    # when
    stream = build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=req,
        with_headers=True,
        with_body=True
    )

    # then

# Generated at 2022-06-13 22:29:54.344208
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.input import ParseArguments
    args = ParseArguments().args
    from httpie.client import Environment
    env = Environment()

# Generated at 2022-06-13 22:30:05.000785
# Unit test for function write_message
def test_write_message():
    from httpie.cli import parser
    from httpie.cli import get_exit_status
    from httpie.core import main
    from httpie.input import SEP_CREDENTIALS
    from httpie.compat import is_windows
    from httpie.plugins import plugin_manager
    from httpie.output.streams import write_stream
    import requests
    import StringIO
    import sys
    from mock import patch
    from collections import defaultdict

    # test whether the output is a string or bytes
    if is_windows:
        fn = write_stream_with_colors_win_py3
    else:
        fn = write_stream

    # check the function write_message in class Session
    session = requests.Session()
    r = session.get('https://httpbin.org/get')

# Generated at 2022-06-13 22:30:13.562793
# Unit test for function write_message
def test_write_message():
    from httpie.core import main
    import httpie.output.streams
    import os
    import sys

    temp_filename = 'write_message_test.output'
    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    if sys.platform == 'win32':
        import subprocess as sp
        os.system('chcp 65001')
        sp.call(['powershell.exe', '-Command', '$PSVersionTable.PSVersion'])

    # Test case with just response headers
    httpie.output.streams.write_message = write_message_test
    sys.stdout = open(temp_filename, 'w')

# Generated at 2022-06-13 22:30:36.223832
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Create an environment object with all values set
    env = Environment()
    env.is_windows = False
    env.stdout_isatty = True

    # First stream type
    # Create a fake argument namespace object
    args = argparse.Namespace()
    args.prettify = False
    args.stream = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args
    )
    assert (stream_class == BufferedPrettyStream)

# Generated at 2022-06-13 22:30:44.132236
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """test_write_stream_with_colors_win_py3."""
    import io
    import sys
    import colorama

    colorama.init(autoreset=True)
    sys.stderr = io.StringIO()

    outfile = sys.stderr

    stream = BaseStream(['\x1b[33m'], with_headers=False, with_body=True)
    write_stream_with_colors_win_py3(stream, outfile, False)
    assert outfile.getvalue() == '\x1b[33m'

# Generated at 2022-06-13 22:30:54.467172
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from . import ExitStatus
    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.output.streams import (
        BufferedPrettyStream, EncodedStream, PrettyStream, RawStream,
    )
    from httpie.core import main
    from httpie.input import ParseError
    import requests
    import configparser
    import os

# Generated at 2022-06-13 22:31:06.088765
# Unit test for function write_message
def test_write_message():
    response = requests.Response()
    response.status_code = 200
    args = argparse.Namespace(
        prettify=None,
        color_style="terminal.ansi",
        style="paraiso",
        stream=True,
        traceback=False,
        debug=False,
        format_options=None,
        json=False,
    )
    env = Environment()
    env.config.style = "scheme"
    env.config.colors = None
    env.config.auto_colors = False
    environ = Environment()
    environ.is_windows = False
    environ.stdout_isatty = True
    environ.stdout = sys.stdout
    environ.stderr = sys.stderr

# Generated at 2022-06-13 22:31:14.654154
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()
    args.stream = False
    args.prettify = False
    args.style = None
    args.json = False
    args.format_options = None

    assert get_stream_type_and_kwargs(env, args) == \
           (EncodedStream, {'env': env})

    args.prettify = True
    args.stream = False
    assert get_stream_type_and_kwargs(env, args) == \
           (BufferedPrettyStream, {'env': env, 'conversion': Conversion(),
                                   'formatting': Formatting(env=env, groups=['all'],
                                                            color_scheme=None,
                                                            explicit_json=False,
                                                            format_options=None)})


# Generated at 2022-06-13 22:31:23.723137
# Unit test for function write_message
def test_write_message():
    requests_response = requests.Response()

    class FakeNamespace:
        def __init__(self):
            self.prettify = ["colors"]
            self.stream = False

    class FakeEnv:
        def __init__(self):
            self.stdout = "stdout"
            self.stdout_isatty = True
            self.is_windows = False

    args = FakeNamespace()
    env = FakeEnv()

    write_message(
        requests_message=requests_response,
        env=env,
        args=args,
        with_headers=False,
        with_body=False
    )

# Generated at 2022-06-13 22:31:37.124949
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout = StringIO()
    env.stderr = StringIO()
    env.config = Config()

    args = Namespace()
    args.prettify = ['lh']
    args.style = 'solarized'
    args.stream = False
    args.json = False
    args.format_options = {'path_separator': '/'}

    assert get_stream_type_and_kwargs(env, args)[0] == BufferedPrettyStream
    assert get_stream_type_and_kwargs(env, args)[1]['env'] == env
    assert get_stream_type_and_kwargs(env, args)[1]['formatting'].color_scheme == args.style

# Generated at 2022-06-13 22:31:44.423858
# Unit test for function write_message
def test_write_message():
    requests.PreparedRequest = ''
    requests.Response = ''
    env = Environment()
    args = argparse.Namespace()
    args.prettify = 'group1'
    args.style = 'group2'
    args.json = False
    args.format_options = 'group3'
    args.stream = True
    args.debug = False
    args.traceback = False
    env.stdout = ''
    env.stdout_isatty = True
    requests_message = ''
    with_headers = True
    with_body = True
    def build_output_stream_for_message():
        for i in range(4):
            yield i

# Generated at 2022-06-13 22:31:56.616551
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    import httpie
    from httpie.input import Url
    import argparse
    import io
    args = argparse.Namespace(prettify=['all', 'colors'], style='monokai', stream=True)
    env = httpie.context.Environment(args=args)

    # Test build_output_stream_for_message without exception
    kwargs = {
        'with_headers': True,
        'with_body': True
    }
    output = io.BytesIO()
    env.stdout = output
    requests_message = requests.PreparedRequest()
    url = Url('http://127.0.0.1')
    url.update_headers(requests_message.headers)
    url.update_auth(requests_message.headers)
    url.update_data

# Generated at 2022-06-13 22:32:02.858727
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from httpie.cli import parser
    from httpie.output.streams import ColorizingStream
    from pygments.formatters import TerminalTrueColorFormatter
    from pygments.token import Token
    import io
    import pytest
    import sys

    class FakeStdout:
        encoding = sys.stdout.encoding

        def __init__(self):
            self.buffer = io.BytesIO()

        def write(self, data):
            if isinstance(data, bytes):
                self.buffer.write(data)
            else:
                self.buffer.write(data.encode(self.encoding))

        def getvalue(self):
            return self.buffer.getvalue().decode(self.encoding)

        def flush(self):
            pass


# Generated at 2022-06-13 22:32:33.113451
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class MockNamespace(object):
        def __init__(self, stream, prettify, style, json, format_options):
            self.stream = stream
            self.prettify = prettify
            self.style = style
            self.json = json
            self.format_options = format_options

    class MockEnv(object):
        def __init__(self, a):
            self.stdout_isatty = a

    class MockRawStream(object):
        pass

    class MockPrettyStream(object):
        pass

    class MockBufferedPrettyStream(object):
        pass

    class MockEncodedStream(object):
        pass

    class MockConversion(object):
        pass

    class MockFormatting(object):
        pass

    # Check RawStream

# Generated at 2022-06-13 22:32:42.737817
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.cli import parser
    env = Environment(colors=True, stdout_isatty=False, stdout=None, stderr=None,
                      stdin_isatty=False, stdin=None)

    args = parser.parse_args(args=[])
    assert (
        get_stream_type_and_kwargs(env, args)
        == (RawStream, {'chunk_size': RawStream.CHUNK_SIZE})
    )
    args = parser.parse_args(args=['--stream', '--prettify'])

# Generated at 2022-06-13 22:32:43.368596
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:32:54.310101
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.compat import is_py2
    from httpie import ExitStatus
    from httpie.core import main
    from httpie.context import Environment

    env = Environment()
    env.config['output.stream'] = True
    env.config['default_options'] = []
    env.config['colors'] = 256
    env.stderr = io.BytesIO()
    env.stdout = io.BytesIO()
    args = main.parser.parse_args(args=[], env=env)
    http_message = requests.Response()
    http_message.request = requests.PreparedRequest()
    requests.Response.is_body_upload_chunk = False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env=env, args=args)