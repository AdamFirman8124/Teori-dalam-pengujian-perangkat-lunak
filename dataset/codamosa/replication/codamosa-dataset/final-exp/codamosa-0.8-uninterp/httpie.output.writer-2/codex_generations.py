

# Generated at 2022-06-13 22:22:53.624474
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """This function doesn't support windows, so we just call write_stream"""
    outfile = BytesIO()
    assert write_stream_with_colors_win_py3(
        stream=None,
        outfile=outfile,
        flush=False
    ) == write_stream(
        stream=None,
        outfile=outfile,
        flush=False
    )

# Generated at 2022-06-13 22:23:04.366323
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """Should correctly write colorized chunks to the output file."""
    # Colors are written 'as is', and printed chunks are decoded.
    stream = [
        b'\x1b[1;32mfoo\x1b[0m\n',
        b'\x1b[1;33m\x1b[1;33mfoo\x1b[0m\x1b[0m\n'
    ]
    outfile = io.StringIO()

    write_stream_with_colors_win_py3(stream, outfile, False)

    assert outfile.getvalue() == '\x1b[1;32mfoo\x1b[0m\n\x1b[1;33mfoo\x1b[0m\n'

# Generated at 2022-06-13 22:23:13.168434
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    """test `write_stream_with_colors_win_py3` function

    """
    import sys
    import io
    stream = [b'\x1b[34m[1B[0m', b'\x1b[34m[2B]\x1b[0m', b'\x1b[34m[3B]\x1b[0m\n']
    outfile = io.StringIO()
    write_stream_with_colors_win_py3(stream, outfile, True)
    assert outfile.getvalue() == '[1B\x1b[34m[0m][2B][3B\n'



# Generated at 2022-06-13 22:23:16.698534
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # Arrange
    # import subprocess
    # subprocess.run(["http"])
    requests.get('https://httpbin.org/get')
    pass



# Generated at 2022-06-13 22:23:28.119134
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    from unittest.mock import Mock

    # Given
    test_data = [
        # chunk, expected output
        (b'\x1b[1;1HTest1\n', '\x1b[1;1HTest1\r\n'),
        (b'\x1b[1;1HTest2\n', '\x1b[1;1HTest2\r\n'),
        (b'Test3\n', b'Test3\r\n'),
        (b'\x1b[1;1HTest4\n', '\x1b[1;1HTest4\r\n'),
    ]
    output = StringIO()
    outfile = Mock(buffer=output)
    stream = Mock(side_effect=test_data)

   

# Generated at 2022-06-13 22:23:40.433817
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    import os
    env = Environment(
        stdin=os.devnull,
        stdout=None,
        stderr=None,
        stdout_isatty=True,
        is_windows=False,
    )
    args, _ = parser.parse_known_args()
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == EncodedStream
    assert stream_kwargs == {'env': env}

# import os
# from httpie.core import main
# args, parser = main()
# # print(args)
# # for k, v in args.__dict__.items():
# #     print(k, v)
# test_get_stream_type_and_kwargs()

# Generated at 2022-06-13 22:23:45.717666
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(
        env=Environment(),
        args=argparse.Namespace(
            style='foo',
            stream=False,
            prettify=None,
            json=False,
            style='foo',
            format_options={}
        )
    ) == (EncodedStream, {'env': Environment()})

# Generated at 2022-06-13 22:23:59.338494
# Unit test for function write_message
def test_write_message():
    import sys
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.output.streams import write_stream

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--prettify',
        nargs='*',
        default=['colors', 'format'],
        choices=['all', 'colors', 'format', 'headers', 'json', 'none']
    )

    args = parser.parse_args('-p colors format'.split())
    env = Environment()

    requests_message = requests.Response()
    class PreparedRequest(object):
        body = b'{"message": "Hello World!"}'
    requests_message.prep = PreparedRequest()


# Generated at 2022-06-13 22:24:07.346979
# Unit test for function write_message
def test_write_message():
    parser = get_parser()
    args = parser.parse_args()
    env = Environment(args, vars(args), vars(args))
    http_response = HTTPResponse(requests.Response())
    write_stream_kwargs = {
        'stream': build_output_stream_for_message(
            args=args,
            env=env,
            requests_message=http_response,
            with_body=True,
            with_headers=True,
        ),
        # NOTE: `env.stdout` will in fact be `stderr` with `--download`
        'outfile': env.stdout,
        'flush': env.stdout_isatty or args.stream
    }
    assert write_stream(**write_stream_kwargs) == None


# Generated at 2022-06-13 22:24:15.355786
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Test Case 1: no color, not pretty and not stream
    environment = Environment(stdout_isatty=False)
    args = argparse.Namespace(
        prettify=None,
        stream=False,
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=environment,
        args=args,
    )
    assert stream_class == RawStream

    # Test Case 2: color, stream and not prettify
    environment = Environment(stdout_isatty=True)
    args = argparse.Namespace(
        prettify=None,
        stream=True,
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=environment,
        args=args,
    )
    assert stream_class

# Generated at 2022-06-13 22:24:31.652159
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests

    env = Environment(
        stdin=open(os.devnull),
        stdout=sys.stdout,
        stdout_isatty=True,
        stderr=sys.stderr,
        color_depth=None
    )
    args = argparse.Namespace(
        download=False,
        follow=False,
        max_redirects=10,
        output=None,
        output_dir=None,
        output_file=None,
        prettify=False,
        style=False,
        verbose=False,
        traceback=False,
        debug=False,
        stream=False,
        json=False,
        format_options={}
    )
    rq=requests.Request(method='get', url='http://httpbin.org/get')


# Generated at 2022-06-13 22:24:44.701678
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace()
    env = Environment()
    stream_class1, stream_kwargs1 = get_stream_type_and_kwargs(args=args, env=env)
    assert stream_class1 == EncodedStream
    assert 'env' in stream_kwargs1

    args = argparse.Namespace(prettify=['headers'])
    env = Environment()
    stream_class2, stream_kwargs2 = get_stream_type_and_kwargs(args=args, env=env)
    assert stream_class2 == BufferedPrettyStream
    assert 'env' in stream_kwargs2
    assert 'conversion' in stream_kwargs2
    assert 'formatting' in stream_kwargs2

    args = argparse.Namespace(prettify=['headers'], stream=True)


# Generated at 2022-06-13 22:24:57.113959
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace(
        stream=True,
        prettify=['headers'],
        style='none',
        json=False,
        format_options={},
    )

    env = Environment(
        stdout_isatty=False,
        colors=256,
        stdin_isatty=True,
        is_windows=False,
        config_dir=None
    )

    raw_stream_type, raw_stream_kwargs = get_stream_type_and_kwargs(
        args=args,
        env=env
    )
    assert raw_stream_type == RawStream
    assert raw_stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE_BY_LINE


# Generated at 2022-06-13 22:25:05.492611
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args.prettify = True
    args.stream = True
    args.style = None
    args.json = False
    args.format_options = None
    env.stdout_isatty = None
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    assert stream_class == PrettyStream
    assert stream_kwargs == {'env': env, 'conversion': Conversion(), 'formatting': Formatting(env=env, groups=True, color_scheme=None, explicit_json=False, format_options=None)}

    env.stdout_isatty = True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )

# Generated at 2022-06-13 22:25:12.297165
# Unit test for function write_message
def test_write_message():
    env = Environment.somewhere(env=None)
    args = argparse.Namespace()
    with_headers = False
    with_body = False
    requests_message = requests.PreparedRequest()
    write_message(requests_message, env, args, with_headers, with_body)
    with_headers = True
    with_body = True
    requests_message = requests.PreparedRequest()
    write_message(requests_message, env, args, with_headers, with_body)

# Generated at 2022-06-13 22:25:22.563905
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream, PrettyStream, EncodedStream, BufferedPrettyStream
    # check for RawStream
    env = Environment(stdout_isatty=False)
    args = argparse.Namespace(prettify=False)
    args.stream=False
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert(stream_class == RawStream)
    assert(stream_kwargs['chunk_size'] == RawStream.CHUNK_SIZE)
    args.stream=True
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert(stream_class == RawStream)

# Generated at 2022-06-13 22:25:35.235315
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():

    # Prepare to create a fake requests.Response object
    class Response:
        pass

    response = Response()
    response.status_code = 200
    response.headers = {'content-type': 'text/html;charset=utf-8',
                        'date': 'Wed, 28 Feb 2018 19:07:50 GMT'}
    response.content = '<html> <body> This is a test. </body> </html>'

    # Prepare to create a fake argparse.Namespace object
    class Namespace:
        pass

    args = Namespace()
    args.stream = 0
    args.style = 'default'
    args.prettify = []
    args.json = ''
    args.format_options = ''
    args.debug = 0
    args.traceback = 0

    # Prepare to create a fake Environment object

# Generated at 2022-06-13 22:25:43.548777
# Unit test for function write_stream
def test_write_stream():
    from httpie.output.streams import PrettyStream, BaseStream
    from httpie.models import HTTPRequest

    def write_all(stream, outfile):
        for chunk in stream:
            outfile.write(chunk)

    class Stream(BaseStream):
        def __iter__():
            yield from [b'']

    stream = Stream(
        msg=HTTPRequest(
            method='GET',
            url='https://httpie.org',
            headers=()
        ),
        with_headers=True,
        with_body=True,
    )

    outfile = io.BytesIO()
    write_all(
        stream,
        outfile
    )

# Generated at 2022-06-13 22:25:54.383006
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace()

    args.prettify = ['all', 'colors']
    args.stream = True
    args.style = "solarized"
    args.format_options = {}
    args.json = ""

    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)

    assert(stream_class == PrettyStream)

    assert(stream_kwargs["env"] == env)

    assert(stream_kwargs["conversion"].__class__ == Conversion)

    assert(stream_kwargs["formatting"].__class__ == Formatting)
    assert(stream_kwargs["formatting"].env == env)
    assert(stream_kwargs["formatting"].groups[0] == "all")

# Generated at 2022-06-13 22:26:03.011143
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    args = argparse.Namespace(prettify = 'all', style = 'parrot')
    env = Environment()
    requests_message = requests.Response()
    requests_message.status_code = 200

    stream = build_output_stream_for_message(
        args=args,
        env=env,
        requests_message=requests_message,
        with_headers=True,
        with_body=True,
    )
    assert(isinstance(stream, PrettyStream))

# Generated at 2022-06-13 22:26:23.245761
# Unit test for function write_message
def test_write_message():
    requests_message = '''GET / HTTP/1.1
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: HTTPie/2.2.0


HTTP/1.1 200 OK
Content-Length: 29
Content-Type: text/html
Date: Fri, 24 Jan 2020 13:43:49 GMT
Server: nginx/1.17.10

<html><body>Hello, world!</body></html>'''
    print(write_message(requests_message,with_body=True,with_headers=True))


# Generated at 2022-06-13 22:26:30.963193
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment('/', '/')
    args = argparse.Namespace(style='none', stream=False)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env,args)
    assert stream_class == EncodedStream
    assert stream_kwargs['env'] == env
    
    args = argparse.Namespace(style='none', stream=True)
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env,args)
    assert stream_class == PrettyStream

# Generated at 2022-06-13 22:26:43.271876
# Unit test for function write_message
def test_write_message():

    # Test --pretty flag, should show pretty print version of the message
    env = Environment()
    args = argparse.Namespace(prettify=['all'])
    requests_message = requests.Request()
    requests_message.prepare(method="GET", url="http://test.com", data={"value": "test"})
    output = []
    write_message(requests_message, env, args, with_body=True, with_headers=True)
    output.append(env.stdout.getvalue())

# Generated at 2022-06-13 22:26:55.370816
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.output import get_response_writer
    from httpie.output.streams import EncodedStream

    env = Environment(
        stdout_isatty=True,
        stderr_isatty=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
        stdin=sys.stdin,
    )
    args = argparse.Namespace(prettify=["json"], stream=True)
    r = requests.Response()
    w = get_response_writer(r, env, args)
    w.write_headers(r)
    content = "aa"
    r._content = content.encode("utf-8")
    w.write_body(r)
    assert isinstance(w.stream, EncodedStream)



# Generated at 2022-06-13 22:27:00.212271
# Unit test for function write_message
def test_write_message():
    message_class = requests.PreparedRequest
    requests_message = requests.PreparedRequest
    with_body=True
    with_headers=True
    write_message(requests_message, Environment(), argparse.Namespace(), with_body, with_headers)

# Generated at 2022-06-13 22:27:09.364896
# Unit test for function write_stream
def test_write_stream():
    from io import BytesIO, StringIO
    from tempfile import TemporaryDirectory
    from httpie.output.streams import EncodedStream
    from httpie.context import Environment

    example_input = b'Hallo World!'
    example_input_len = len(example_input)

    # Test case 1: IO stream
    with TemporaryDirectory() as tmpdir:
        filename = tmpdir + '\\testfile.txt'
        file = open(filename, 'wb')

# Generated at 2022-06-13 22:27:19.601529
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import tempfile
    import requests
    import argparse
    import httpie.input
    import httpie.cli
    import httpie.output.streams

    parser = argparse.ArgumentParser()
    httpie.cli.parser_args(parser)
    args = parser.parse_args()
    env = httpie.cli.Environment()
    env.config['output.stream'] = True
    env.stdout.encoding = 'utf-8'
    env.stderr.encoding = 'utf-8'
    kwargs = {'headers': {'content-type': 'application/json'}, 'data': '{"a":1}'}
    _, http_response_file = tempfile.mkstemp()
    with open(http_response_file, 'wb') as f:
        http_response_bytes

# Generated at 2022-06-13 22:27:31.898172
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    from httpie.cli.parser import parser
    from httpie.core import main
    import httpie
    import httpie.output
    import pytest
    from requests.models import PreparedRequest, Response
    req = PreparedRequest()
    req.method = "GET"
    req.url = "http://www.google.com"
    req.method = "POST"
    res = Response()
    res.req = req
    res.status_code = 200
    res.headers["Content-Type"] = "application/json"
    res.encoding = "utf-8"
    res.text = "{\"name\": \"Kunal\"}"
    res.ok = True
    res.raw = ''
    res.request = req
    res.connection = ''
    res.history = ['']


# Generated at 2022-06-13 22:27:43.501871
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(Environment(None,None,None), 'prettify') == (
    BufferedPrettyStream,
    {'env': None, 'conversion': Conversion(), 'formatting': Formatting(env=None, groups='prettify',
                                                        color_scheme=None, explicit_json=None,
                                                        format_options=None)})
    assert get_stream_type_and_kwargs(Environment(None,None,None), 'json') == (
    PrettyStream,
    {'env': None, 'conversion': Conversion(), 'formatting': Formatting(env=None, groups='json',
                                                        color_scheme=None, explicit_json=None,
                                                        format_options=None)})

# Generated at 2022-06-13 22:27:55.969287
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    import mock
    import string

    outfile = mock.MagicMock()

    def _write(data):
        # Make sure we write bytes.
        assert isinstance(data, bytes)
        outfile.write.assert_any_call(data.decode('ascii'))
        return len(data)

    def _flush():
        outfile.flush.assert_called_with()

    outfile.buffer.write = _write
    outfile.buffer.flush = _flush
    outfile.flush = _flush
    outfile.isatty.return_value = True
    outfile.encoding = 'ascii'

    color = b'\x1b['

    # First plain text chunk

# Generated at 2022-06-13 22:28:16.558562
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(
        Environment(),
        argparse.Namespace(
            stream=True,
            prettify=True,
            style='default',
            json=False,
            format_options={},
        )
    ) == (
        PrettyStream,
        {
            'env': Environment(),
            'conversion': Conversion(),
            'formatting': Formatting(
                env=Environment(),
                groups={'default'},
                color_scheme='default',
                explicit_json=False,
                format_options={},
            )
        },
    )


# Generated at 2022-06-13 22:28:17.068956
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:28:28.696300
# Unit test for function write_stream_with_colors_win_py3

# Generated at 2022-06-13 22:28:32.334527
# Unit test for function write_stream
def test_write_stream():
    write_stream(['a', 'b', 'c'], io.BytesIO(), False)
    write_stream(['a', 'b', 'c'], io.StringIO(), False)
    write_stream(['a', 'b', 'c'], sys.stdout, True)



# Generated at 2022-06-13 22:28:45.660126
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    env.stdout_isatty = True
    args = argparse.Namespace(
        stream=True,
        prettify=True,
        style="none",
        json=False,
        format_options={"pretty": None}
    )
    assert get_stream_type_and_kwargs(env, args) == (
        PrettyStream,
        {
            'env': env,
            'conversion': Conversion(),
            'formatting': Formatting(
                env=env,
                groups=["pretty"],
                color_scheme="none",
                explicit_json=False,
                format_options={"pretty": None}
            )
        }
    )

# Generated at 2022-06-13 22:28:55.483209
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.output.streams import RawStream
    from httpie.context import Environment
    from httpie.output.processing import Conversion, Formatting
    from httpie.cli import parser
    from httpie.config import Config
    from httpie.models import Environment as Env
    from httpie.output.streams import PrettyStream, BufferedPrettyStream, EncodedStream
    from settings import DEFAULT

    env = Environment(stdin=None, stdout=None, stderr=None, vars=Env())
    parsed_args = argparse.Namespace()
    parsed_args.config_dir = DEFAULT
    parsed_args.config = DEFAULT
    parsed_args.prettify = None
    parsed_args.style = 'none'
    parsed_args.json = ''
    parsed_args.format_options = ''


# Generated at 2022-06-13 22:28:57.723759
# Unit test for function write_stream
def test_write_stream():
    assert 'chunk' == write_stream('chunk', 'outfile', 'flush')

# Generated at 2022-06-13 22:29:08.461820
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    assert get_stream_type_and_kwargs(Environment(), argparse.Namespace(stream=True, prettify=[])) == (PrettyStream, {'env': Environment(), 'formatting': Formatting(env=Environment(), groups=[], explicit_json=False, format_options=None, color_scheme=None), 'conversion': Conversion()})
    assert get_stream_type_and_kwargs(Environment(), argparse.Namespace(stream=False, prettify=[])) == (BufferedPrettyStream, {'env': Environment(), 'formatting': Formatting(env=Environment(), groups=[], explicit_json=False, format_options=None, color_scheme=None), 'conversion': Conversion()})
    assert get_stream_type_and_kwargs(Environment(), argparse.Namespace(stream=True, prettify=['colors']))

# Generated at 2022-06-13 22:29:23.491074
# Unit test for function write_message
def test_write_message():
    env = Environment(
        colormode='never',
        colorscheme='test',
        format='test',
        isatty=False,
        stdin_isatty=False,
        stdout_isatty=False,
        stderr_isatty=False,
    )

# Generated at 2022-06-13 22:29:24.008569
# Unit test for function write_stream
def test_write_stream():
    pass

# Generated at 2022-06-13 22:29:39.346343
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    class FakeEnvironment:
        def __init__(self):
            self.stdout_isatty = True

    fake_env = FakeEnvironment()
    assert get_stream_type_and_kwargs(env=fake_env, args={}
    ) == (PrettyStream, {
        'env': fake_env,
        'conversion': Conversion(),
        'formatting': Formatting(
            env=fake_env,
            groups=[],
            color_scheme=None,
            explicit_json=False,
            format_options=None
        )
    })

# Generated at 2022-06-13 22:29:43.075321
# Unit test for function write_message
def test_write_message():
    requests_message = requests.PreparedRequest()
    args = argparse.Namespace()
    env = Environment()
    with_headers = False
    with_body = False
    write_message(requests_message,env,args,with_headers,with_body)

# Generated at 2022-06-13 22:29:52.270929
# Unit test for function write_message
def test_write_message():
    from requests_toolbelt.downloadutils import stream
    from httpie.cli import get_response

    cli_args = argparse.Namespace(
        body=None,
        download=False,
        form=None,
        headers=None,
        max_redirects=None,
        method='GET',
        output_file=None,
        output_options_provided=False
    )


# Generated at 2022-06-13 22:30:06.995472
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    # TODO : this test fails

    class mock_env(Environment):

        def __init__(self, **kwargs):
            self.stdout = kwargs['stdout']
            self.stdout_isatty = kwargs['stdout_isatty']

    class mock_request(requests.Request):

        def __init__(self, **kwargs):
            self.headers = kwargs['headers']
            self.body = kwargs['body']

    class mock_args(argparse.Namespace):

        def __init__(self, **kwargs):
            self.stream = kwargs['stream']

    mock_env = mock_env(stdout = '', stdout_isatty = False)

# Generated at 2022-06-13 22:30:20.125829
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import io
    import requests

    import httpie
    from httpie import input
    from httpie.core import main
    from httpie.core import get_response


# Generated at 2022-06-13 22:30:31.259635
# Unit test for function write_stream_with_colors_win_py3
def test_write_stream_with_colors_win_py3():
    from io import StringIO
    import sys
    import unittest
    from unittest.mock import Mock, patch

    # Run the function being tested.
    with patch('httpie.output.streams.colorama_text') as coloring:
        coloring.return_value = 'GOOD'
        class FakeStream(BaseStream):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.chunks = [
                    b'foo ',
                    b'\x1b[1mERROR\x1b[22m bar',
                    b'\x1b[1mok\x1b[22m',
                    b' baz'
                ]

            def __iter__(self):
                return iter(self.chunks)

        fake_args

# Generated at 2022-06-13 22:30:37.923030
# Unit test for function write_message
def test_write_message():
    print("Testing write_message()...")
    print("Test case 1: ")
    print("Write message with headers and body")
    args = argparse.Namespace()
    args.prettify = "all"
    env = Environment()
    env.stdout = sys.stdout
    yield from write_stream_with_colors_win_py3()


if __name__ == '__main__':
    test_write_message()

# Generated at 2022-06-13 22:30:39.562472
# Unit test for function write_message
def test_write_message():
    # TODO
    assert(False)

# Generated at 2022-06-13 22:30:48.822266
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    import requests
    response = requests.Response()
    response.status_code = 200
    response.headers['Content-Type'] = 'text/html'

    response._content = b'''<html>
    <head>
        <title> titre de mon super site</title>
    </head>
    <body>
        <p>
            Hello world !
        </p>
    </body>
</html>'''
    response.url = 'https://google.com'
    response.encoding = 'euc-kr'

    args = argparse.Namespace()
    args.json = False
    args.stream = False
    args.prettify = []
    args.style = ''
    args.format_options = []
    env = Environment()
    env.stdout_isatty = True
    env

# Generated at 2022-06-13 22:30:51.159434
# Unit test for function write_message
def test_write_message():
    """
    Test for function write_message
    :return:
    """

# Generated at 2022-06-13 22:31:24.318698
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    args = argparse.Namespace()
    env = Environment()
    requests_message = requests.PreparedRequest()
    requests_message.prepare_body(None, None)
    requests_message.prepare_headers(None)
    requests_message.url = 'http://example.com/a/b/c'
    requests_message.body = 'foo'
    requests_message.headers = {'bar':'baz'}
    requests_message.method = 'GET'
    with_headers = True
    with_body = True

    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    message_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }

# Generated at 2022-06-13 22:31:31.181620
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    from httpie.config import Config
    import requests
    from httpie.input import ParseRequest
    from httpie.models import JSONDataDict
    from httpie.plugins import builtin
    environment = Environment(
        config=Config(),
        stdin_isatty=False,
        stdout_isatty=True,
        stderr_isatty=True,
        stdout=builtin.get_response_stream_factory(),
        stderr=builtin.get_response_stream_factory(),
    )
    environment.config.json = {'stream': True}
    session = requests.Session()
    body = JSONDataDict({'foo': 'bar'})
    args = ParseRequest(environment).transform(['--body=foo=bar'])[0]

# Generated at 2022-06-13 22:31:41.545961
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    # Redirect the output to get the data that is printed
    sys.stdout = io.StringIO()

    args = httpie.cli.parser.parse_args(args=[
        'get',
        'https://httpbin.org/json',
        'Accept:application/json'
    ])

    env = Environment()
    response = requests.Response()
    response.status_code = 200
    response.raw = io.BytesIO(b'{"args": {"Accept": "application/json"}}')
    response.headers['Content-Type'] = 'application/json'
    response.encoding = 'utf-8'
    response.url = 'http://httpbin.org/get'
    response.request = requests.Request(method='GET', url=response.url).prepare()
    response.connection = None

# Generated at 2022-06-13 22:31:55.339080
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    env = Environment()
    args = argparse.Namespace(
        prettify=list(),
        stream=True,
        style=None,
        json=None,
        format_options=''
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs(env, args)
    assert stream_class == PrettyStream
    assert isinstance(stream_kwargs, dict)
    assert 'env' in stream_kwargs
    assert 'conversion' in stream_kwargs
    assert 'formatting' in stream_kwargs

    args = argparse.Namespace(
        prettify=list(),
        stream=False,
        style=None,
        json=None,
        format_options=''
    )
    stream_class, stream_kwargs = get_stream_type_and_kwargs

# Generated at 2022-06-13 22:32:03.091658
# Unit test for function write_message
def test_write_message():
    msg = requests.PreparedRequest()
    msg.prepare_url = "http://google.com"
    env = Environment()
    args = argparse.Namespace()
    # write_message(msg, env, args)
    write_message(msg, env, args, True, True)

if __name__ == "__main__":
    test_write_message()

# Generated at 2022-06-13 22:32:03.719733
# Unit test for function build_output_stream_for_message
def test_build_output_stream_for_message():
    pass

# Generated at 2022-06-13 22:32:14.899604
# Unit test for function get_stream_type_and_kwargs
def test_get_stream_type_and_kwargs():
    args = argparse.Namespace(style='none', format_options=dict(), stream=False, prettify=['body'])
    env = Environment(is_windows=False, stdout_isatty=True)

    assert get_stream_type_and_kwargs(env, args) == (BufferedPrettyStream, {'env': env,
                                                                       'conversion': Conversion(),
                                                                       'formatting': Formatting(env=env,
                                                                                                groups=['body'],
                                                                                                color_scheme='none',
                                                                                                explicit_json=False,
                                                                                                format_options=dict())})

    args = argparse.Namespace(style='none', format_options=dict(), stream=False, prettify=['headers'])
    env = Environment

# Generated at 2022-06-13 22:32:16.521710
# Unit test for function write_message
def test_write_message():
    # FIXME: to test url join of redirect url
    pass

# Generated at 2022-06-13 22:32:17.898227
# Unit test for function write_message
def test_write_message():
    print(write_message)

# Generated at 2022-06-13 22:32:26.319438
# Unit test for function write_message
def test_write_message():
    import requests
    from httpie.context import Environment
    from httpie.models import HTTPResponse
    from httpie import cli
    from httpie.output.processing import EncodedFormatters
    from httpie.output.formatters import DEFAULT_FORMATTERS
    from httpie.output.streams import BufferedPrettyStream
    from httpie.output.styles import DEFAULT_STYLE
    from httpie.compat import isnumber
    from httpie.output.streams import build_output_stream_for_message
    from httpie.output.scheme import SCHEME
    import json
    import base64
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 65432))