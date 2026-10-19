

# Generated at 2022-06-13 21:41:03.816284
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie import __version__ as httpie_version

    args = parser.parse_args(
        args=[
            'http',
            'localhost:80',
            '--auth=username:password',
            '--auth=username2:password2',
            '--json',
            '--max-redirects=5',
            '--proxy=proxy.com:8080',
            '--timeout=60',
            '--verify=no',
            '--verbose',
        ],
        env=Environment(
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr,
        ),
    )
    args.headers = ['Content-Type: application/json']


# Generated at 2022-06-13 21:41:14.840880
# Unit test for function program
def test_program():
    from httpie import program
    from httpie.cli.parser import parser, parse_args
    from httpie.output.writer import write_message
    from httpie.status import ExitStatus
    import httpie
    #
    #     def test_program_when_interrupted_before(self):
    #         """
    #         When the program is interrupted
    #         before the first request.
    #         """
    #         args = parse_args()
    #         args.url = 'httpbin.org/get'
    #         args.output_options = (OUT_REQ_HEAD,)
    #         args.stdin.inject_line('X')
    #         args.stdin.inject_line('\x03')  # Ctrl+C
    #         program(args=args, env=self.env)
    #

# Generated at 2022-06-13 21:41:18.762234
# Unit test for function main
def test_main():
    assert main(["httpie.py","http://httpbin.org/get"])==0


# Generated at 2022-06-13 21:41:23.087406
# Unit test for function program
def test_program():
    import sys
    exit_status = main(['http', '--json', 'http://httpbin.org/'])
    print(exit_status)

# Generated at 2022-06-13 21:41:24.504997
# Unit test for function program
def test_program():
    x = main()
    assert x == 0

# Generated at 2022-06-13 21:41:35.518577
# Unit test for function program
def test_program():
    from io import StringIO
    import sys
    stdout = sys.stdout
    sys.stdout = StringIO()
    args = ['-v', 'https://httpbin.org/get']
    program(args, env)
    output = sys.stdout.getvalue()
    print(output)

# Generated at 2022-06-13 21:41:37.617326
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:41:46.849333
# Unit test for function main
def test_main():
    from httpie.context import Environment
    from httpie.output.writer import write_message, write_stream, MESSAGE_SEPARATOR_BYTES
    from httpie.plugins.registry import plugin_manager
    from httpie.cli.definition import parser
    from httpie.config import Config
    from httpie.downloads import Downloader
    from httpie.status import ExitStatus, http_status_to_exit_status
    from httpie.client import collect_messages
    def separate():
            getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)
    main('test_httpie')

    plugin_manager.load_installed_plugins()
    config_dir = "~/.httpie"

# Generated at 2022-06-13 21:41:54.711258
# Unit test for function program
def test_program():
    import sys
    import os
    sys.argv = ['http', 'https://httpbin.org/get']
    sys.stdout.isatty = lambda: False
    sys.stderr.isatty = lambda: False
    main()
    assert os.path.isfile('plik.pdf')
    os.remove('plik.pdf')
    sys.argv = ['http', 'https://httpbin.org/get', '--output', 'plik.pdf', '--download']
    main()
    assert os.path.isfile('plik.pdf')
    os.remove('plik.pdf')

# Generated at 2022-06-13 21:42:06.282998
# Unit test for function program
def test_program():
    # Testing a successful request
    from unittest.mock import Mock

    env = Mock(stdout_isatty=False)
    class Args:
        output_options = [OUT_REQ_HEAD, OUT_RESP_BODY]
        check_status = True
        follow = True
        quiet = False

    class Response:
        status_code = 200

    class Request:
        url = "httpbin.org"
    request = Request()
    response = Response()
    response.request = request
    def mock_collect_messages(args,config_dir,request_body_read_callback):
        yield request
        yield response
    def mock_http_status_to_exit_status(code,follow):
        return 0
    env.log_error=Mock()

# Generated at 2022-06-13 21:43:12.008148
# Unit test for function program
def test_program():
    # noinspection PyProtectedMember
    test_args = Namespace(
                body='yes', 
                check_status=True, 
                download=False, 
                follow=False, 
                headers=[('User-Agent', 'HTTPie/0.9.9')], 
                ignore_stdin=False, 
                method='GET', 
                output_file=None, 
                output_file_specified=False, 
                output_options=[], 
                output_options_specified=False, 
                redirect=True, 
                style=None, 
                timeout=30, 
                traceback=False, 
                url='http://httpbin.org/post', 
                verify=True
    )
    test_env = Environment()

# Generated at 2022-06-13 21:43:19.620849
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.output.formatters.json import JSONFormatter
    from httpie.output.formatters.pretty import PrettyFormatter
    import json

    args = parser.parse_args(['--verify=no', 'https://httpbin.org/get'])
    env = Environment()
    wrapper = program(args, env)

    assert wrapper is not None
    #assert wrapper == True

# Generated at 2022-06-13 21:43:21.246968
# Unit test for function program
def test_program():
    args = Namespace
    env = Environment
    print(program(args, env))

# Generated at 2022-06-13 21:43:31.109829
# Unit test for function main
def test_main():
    from . import api
    from .compat import get_stderr_bytes, get_stderr_text, is_windows
    from .output.formats import JSON
    from .output.streams import get_binary_stream
    from .__pkginfo__ import __version__
    args = ['--debug', '--verbose']
    env = Environment()
    output_stream = get_binary_stream('stdout', binary_stream=True)
    error_stream = get_binary_stream('stderr', binary_stream=True)
    env.stdout = output_stream
    env.stderr = error_stream
    main(args, env)

# Generated at 2022-06-13 21:43:33.717784
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args(['--debug'])
    assert main(args=args) == 0

# Generated at 2022-06-13 21:43:39.077362
# Unit test for function main
def test_main():
  assert main() == ExitStatus.SUCCESS
  assert main(['--debug']) == ExitStatus.SUCCESS
  assert main(['--debug', 'GET', 'www.httpbin.org']) == ExitStatus.SUCCESS
  assert main(['--debug', 'GET', 'www.httpbin.org/get']) == ExitStatus.SUCCESS
  assert main(['-v', 'GET', 'www.httpbin.org']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:41.596825
# Unit test for function main
def test_main():
    # TODO: Fix this.
    # exit_status = main(['--debug'])
    # assert exit_status == ExitStatus.SUCCESS
    pass

# Generated at 2022-06-13 21:43:52.930714
# Unit test for function main
def test_main():
    import unittest
    from unittest.mock import Mock
    from httpie.cli.argtypes import KeyValueArg
    from httpie.input import ParseError

    class TestMain(unittest.TestCase):
        def test_main(self):
            argv = ['http', 'https://httpie.org']
            args = main(argv)
            self.assertEqual(args, 0)

        def test_headers(self):
            argv = ['http', 'http://httpie.org', 'Accept:application/json', 'accept-encoding:gzip']
            args = main(argv)
            self.assertEqual(args, 0)


# Generated at 2022-06-13 21:44:02.523360
# Unit test for function main
def test_main():
    from io import BytesIO
    from httpie.cli.context import Context

    ctx = Context()
    ctx.stdin = BytesIO(b'bar\n')
    ctx.stdout = BytesIO()
    ctx.stderr = BytesIO()
    status = main(['http', '--form', '--json=indent=2', 'foo=bar', 'http://httpbin.org/anything'], env=ctx)
    assert status == ExitStatus.SUCCESS
    resp = ctx.stdout.getvalue().decode('utf8')
    assert "Content-Type: application/json" in resp
    assert "Meow: meow" in resp

# Generated at 2022-06-13 21:44:10.527570
# Unit test for function program
def test_program():
    env = Environment()
    args = argparse.Namespace()
    program(args, env)


if __name__ == '__main__':
    try:
        exit_status = main()
    except KeyboardInterrupt:
        # We want the error message from httpie itself, not from Python.
        sys.exit(ExitStatus.ERROR_CTRL_C)
    else:
        sys.exit(exit_status)

# Generated at 2022-06-13 21:44:57.824099
# Unit test for function program
def test_program():
    sys.argv = ['httpie', "http://httpbin.org/get"]
    env = Environment()
    status = program(argparse.Namespace, env)
    assert status == ExitStatus.SUCCESS
    if status == ExitStatus.SUCCESS:
        print("Test passed")
    else:
        print("Test failed")

test_program()

# Generated at 2022-06-13 21:45:06.904033
# Unit test for function main
def test_main():
    import unittest
    import unittest.mock
    import io

    class MainTests(unittest.TestCase):

        def setUp(self) -> None:
            self.env = Environment()
            self.env.stdout = io.BytesIO()
            self.env.stderr = io.BytesIO()

        @unittest.mock.patch('httpie.cli.program')
        def test_success(self, mock_program):
            # Given
            mock_program.return_value = ExitStatus.SUCCESS

            # When
            exit_status = main(['GET', 'https://httpbin.org/get'], env=self.env)

            # Then
            mock_program.assert_called_once()
            self.assertEqual(exit_status, ExitStatus.SUCCESS)

# Generated at 2022-06-13 21:45:17.571609
# Unit test for function main
def test_main():
    from io import TextIOWrapper
    from httpie import __main__
    from httpie.cli.definition import parser

    try:
        from unittest import mock
    except ImportError:  # pragma: no cover
        # noinspection PyUnresolvedReferences
        import mock
    from unittest.mock import MagicMock, call, patch

    # noinspection PyTypeChecker
    from httpie.context import Environment
    from httpie.config import Config
    from pygments import __version__ as pygment_version
    from httpie.downloads import Downloader
    # noinspection PyProtectedMember
    from httpie.output.writer import MESSAGE_SEPARATOR_BYTES
    from httpie.plugins.registry import plugin_manager
    from requests import __version__ as request_version
   

# Generated at 2022-06-13 21:45:27.774946
# Unit test for function main
def test_main():
    #def test_program(args=['http', 'https://httpie.org', 'http://httpie.org'], env=Environment()):
    def test_program(args=['http', 'https://httpbin.org/get', 'http://httpbin.org/status/500', 'http://httpbin.org/status/401'], env=Environment()):
        #def test_program(args=['http', 'https://httpbin.org/get', 'http://httpbin.org/status/500'], env=Environment()):
        #def test_program(args=['http', 'http://httpbin.org/status/500'], env=Environment()):
        exit_status = ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:38.230609
# Unit test for function program
def test_program():
    import requests
    import argparse
    import os
    import sys
    class Env:
        def __init__(self):
            self.program_name = "httpie"
            self.stdin = os.fdopen(0)
            self.stdout = os.fdopen(1)
            self.stderr = os.fdopen(2)
            self.stdout_isatty = False
            self.stderr_isatty = False
            self.stdin_encoding = "utf-8"
            self.is_windows = False
    class Config:
        def __init__(self):
            self.default_options = None
            self.directory = None
            self.plugins = []
            self.colors = argparse.Namespace()
            self.colors.scheme = "none"


# Generated at 2022-06-13 21:45:42.735019
# Unit test for function main
def test_main():
    from httpie.context import Environment
    env=Environment()
    assert main() == ExitStatus.ERROR


if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-13 21:45:46.875392
# Unit test for function main
def test_main():
    import unittest
    class TestMain(unittest.TestCase):
        def test_main(self):
            main()
    unittest.main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 21:45:56.772625
# Unit test for function main
def test_main():
    from io import StringIO
    import httpie
    from httpie import __main__ as main

    args = ['http', '--debug', 'http://localhost:8000']
    env = Environment()
    env.stdin = StringIO()
    env.stdin_isatty = False
    env.stdout = StringIO()
    env.stdout_isatty = False
    env.stderr = StringIO()
    env.stderr_isatty = False
    env.stdout_raw = False
    env.stdout_binary = False
    env.config = httpie.Config()
    env.config.__dict__.update({
        'default_options': [],
        'directory': '~/.config/httpie',
    })
    exit_status = main.main(args, env=env)


# Generated at 2022-06-13 21:46:10.041656
# Unit test for function program
def test_program():
    from httpie.cli.constants import DEFAULT_TIMEOUT
    from httpie.cli.parser import get_parser
    parser = get_parser()
    args = parser.api_args()
    env = Environment()
    args.url = 'https://httpbin.org/ip'
    args.body = 'hello=world&status=200'
    args.output_file_specified = False
    args.output_file = None
    args.method = 'GET'
    args.headers = []
    args.data = "{'hello': 'world', 'status': '200'}"
    args.timeout = DEFAULT_TIMEOUT
    args.check_status = False
    args.follow = True
    args.download = False
    args.download_resume = False
    args.output_options = {'b'}
    args

# Generated at 2022-06-13 21:46:20.820097
# Unit test for function main
def test_main():
    env = Environment()
    env.stdout = sys.stdout
    env.debug = True
    env.config = config = argparse.Namespace()

    config.default_options = []
    assert main(args=['--debug'], env=env) == ExitStatus.SUCCESS  # --debug

    config.default_options = ['--debug']
    assert main(args=[], env=env) == ExitStatus.SUCCESS
    assert main(args=['test', 'get'], env=env) == ExitStatus.SUCCESS

    config.default_options = []
    assert main(args=['test', 'get'], env=env) == ExitStatus.ERROR

    # TODO: test "normal" program execution

# Generated at 2022-06-13 21:46:54.468768
# Unit test for function program
def test_program():
    assert program(argparse.Namespace(output_options=["request", "none"]), Environment()) == 0

# Generated at 2022-06-13 21:47:05.874172
# Unit test for function main
def test_main():
    import io
    import sys
    env = Environment()
    env.stdout = io.StringIO()
    env.stderr = io.StringIO()
    args = []
    sys.argv = ['http', '--debug']
    main(args, env)
    sys.argv = ['http', '--download']
    main(args, env)
    sys.argv = ['http', '--download', '--download-resume']
    main(args, env)
    sys.argv = ['http', '--download', '--download-resume', '--check-status']
    main(args, env)
    sys.argv = ['http', '--download', '--download-resume', '--check-status', '--follow']
    main(args, env)

# Generated at 2022-06-13 21:47:17.713149
# Unit test for function program
def test_program():
    test_args1 = ['http', 'http://httpbin.org/get', 'Accept:application/json']
    expected_output1 = b'{'
    test_args2 = ['http', 'http://httpbin.org/get', 'Accept:application/json', '--debug']
    expected_output2 = b'{'
    test_args3 = ['http', 'http://httpbin.org/get', '--debug']
    expected_output3 = b'{'
    
    # Test case 1 - pass correct test case
    env_unit_test1 = Environment()
    env_unit_test1.stdout = io.BytesIO()
    parsed_args1 = main(test_args1, env_unit_test1)
    assert parsed_args1 == ExitStatus.SUCCESS
    assert env_unit_test1

# Generated at 2022-06-13 21:47:33.705371
# Unit test for function program
def test_program():
    expected_result=get_output_options(args=parser.parse_args(
        # args=["--output-options","request,request_body","--print","hb","--output-file=testfile","--headers=Authorization:Basic YmFzaWNfdXNlcjpwYXNzd29yZA==","POST","http://example.com"]
        args=["--output-options","request,request_body","--print","hb","--headers=Authorization:Basic YmFzaWNfdXNlcjpwYXNzd29yZA==","POST","http://example.com"]
    ),message = requests.PreparedRequest())
    print(expected_result)
    actual_result = (True, True)
    assert expected_result == actual_result


# Generated at 2022-06-13 21:47:42.414633
# Unit test for function program
def test_program():
    from httpie import input as inputs
    from httpie.cli.constants import OUT_REQ_HEAD, OUT_RESP_BODY
    from httpie.input import ParseError
    from httpie.output.streams import write_stream_noop
    class Args():
        output_options = [OUT_REQ_HEAD, OUT_RESP_BODY]
        output_file_specified = True
        headers = []
        json = False
        output_file = write_stream_noop
        form = False
        quiet = False
        body = 'test'

    class Env(Environment):
        pass
    env = Env()
    args = Args()

    print(program(args=args,env=env))

# Generated at 2022-06-13 21:47:55.227590
# Unit test for function main
def test_main():
    from httpie.client import main as httpie_main
    assert httpie_main(['google.com']) == ExitStatus.SUCCESS  # 200
    assert httpie_main(['-i', 'google.com']) == ExitStatus.SUCCESS  # 200
    assert httpie_main(['-I', 'google.com']) == ExitStatus.SUCCESS  # 200
    assert httpie_main(['-o', 'google.com']) == ExitStatus.SUCCESS  # 200
    assert httpie_main(['-p', 'google.com']) == ExitStatus.SUCCESS  # 200
    assert httpie_main(['-r', 'google.com']) == ExitStatus.SUCCESS  # 200

# Generated at 2022-06-13 21:47:57.540650
# Unit test for function program
def test_program():
    assert program() == ExitStatus.SUCCESS
    

# Generated at 2022-06-13 21:47:58.151686
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 21:48:02.167308
# Unit test for function program
def test_program():
    env = Environment()
    args = ['https://www.google.com/search?q=machine+learning']
    exit_status = program(args=args, env=env)
    return exit_status == ExitStatus.SUCCESS

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:48:12.833754
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.cli.parser import get_parser
    from httpie.cli.constants import DEFAULT_FORMAT

    args = get_parser().parse_args(["--json", "http://127.0.0.1:5000/get"])
    assert program(args=args, env=Environment()) == ExitStatus.SUCCESS

    args = get_parser().parse_args(["http://127.0.0.1:5000/get", "Accept: application/json"])
    assert program(args=args, env=Environment()) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:48:48.297027
# Unit test for function program
def test_program():
    args = argparse.Namespace()
    args.headers = b'Content-Type: application/json'
    env = Environment()
    expected = ExitStatus.SUCCESS
    actual = program(args=args, env=env)
    assert actual == expected


# Generated at 2022-06-13 21:48:53.956278
# Unit test for function main
def test_main():
    assert main(['httpie', '--json', 'http://httpbin.org/get']) == ExitStatus.SUCCESS
    assert main(['httpie', '--version']) == ExitStatus.SUCCESS


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:48:57.455086
# Unit test for function main
def test_main():
    args = '--debug'.split()
    assert main(args=args, env=Environment(stdin_encoding='ascii')) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:49:06.829706
# Unit test for function main
def test_main():

    # Unit tests for lines:10,24,25-27,35,37-53,63,69
    env = Environment()
    env.log_error = lambda msg, level=None: None
    args = [
        'program_name',
        'get',
        '--json',
        '--traceback',
        'https://httpbin.org/ip',
        'q==123'
    ]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(args=args, env=env)
        pytest_wrapped_e.match(r'^\d+$')



# Generated at 2022-06-13 21:49:10.606489
# Unit test for function main
def test_main():
    args = decode_raw_args(args=[b'/usr/local/bin/http', b'https://postman-echo.com/get?foo=bar', b'--body'], stdin_encoding='utf-8')

# Generated at 2022-06-13 21:49:20.182383
# Unit test for function main
def test_main():
    import pytest
    import shutil
    import subprocess
    import tempfile

    args = [
        sys.executable,
        '-m', 'httpie',
        '--output=/dev/null',
        '--print=H',
        'https://postman-echo.com/get?foo=bar',
    ]
    code = subprocess.call(args=args)
    assert code == ExitStatus.SUCCESS
    args = [
        sys.executable,
        '-m', 'httpie',
        'https://postman-echo.com/get',
    ]
    code = subprocess.call(args=args)
    assert code == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:49:30.989220
# Unit test for function main
def test_main():
    import sys, os
    import builtins

    old_argv = sys.argv
    sys.argv = ["http"]

    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    old_exit = builtins.exit
    def fake_exit(status):
        if status != ExitStatus.SUCCESS:
            raise SystemExit(status)

    builtins.exit = fake_exit

    try:
        main()
    except SystemExit as e:
        assert e.code == ExitStatus.ERROR
    else:
        assert False

    sys.argv = ["http", "--debug"]
    main()


# Generated at 2022-06-13 21:49:40.767125
# Unit test for function main
def test_main():
    # setup test
    import io
    import contextlib
    stdin_tmp = None
    stdin = None
    stdout = None
    stderr = None

# Generated at 2022-06-13 21:49:44.024522
# Unit test for function main
def test_main():
    assert main() == ExitStatus.SUCCESS
    assert main(['https://httpbin.org/get']) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:49:54.805438
# Unit test for function program
def test_program():
    exit_status = ExitStatus.SUCCESS
    downloader = 'downloader'
    url = 'https://httpie.org/test-response'
    final_response = Response()
    final_response.status_code = 200
    initial_request = 'initial_request'
    env = Environment()
    args = argparse.Namespace()
    args.output_options = []
    args.output_file = None
    args.download = False
    args.headers = {'secret-header': 'dev'}
    args.follow = False
    args.check_status = False
    args.quiet = False
    args.output_file_specified = False
    args.download_resume = False
