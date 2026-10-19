

# Generated at 2022-06-13 21:40:39.989015
# Unit test for function main
def test_main():
    assert main() == ExitStatus.SUCCESS

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:40:46.184137
# Unit test for function main
def test_main():
    from httpie.cli.args import DEFAULT_OPTIONS
    assert main(args=[DEFAULT_OPTIONS[0], '--debug']) == 0
    assert main(args=[DEFAULT_OPTIONS[0]]) == http_status_to_exit_status(DEFAULT_OPTIONS[1])
    assert main(args=[DEFAULT_OPTIONS[0], '--version']) == 0
    assert main(args=[DEFAULT_OPTIONS[0], '--help']) == 0
    assert main(args=[DEFAULT_OPTIONS[0], '--traceback']) == 0



# Generated at 2022-06-13 21:40:58.723282
# Unit test for function program
def test_program():
    # Test case 1: Check the status code
    # Result : Success
    # Test case 2: Check the status code with wrong username and password
    # Result : Failure
    # Test case 3: Check the content type 
    # Result : Success
    # Test case 4: Check the content type with wrong username and password
    # Result : Failure

    # Create a sample test program
    # Create a sample test arguments
    class test_arg:
        pass
    args = test_arg()
    args.headers = None
    args.timeout = 30
    args.max_redirects = 30
    args.download = False
    args.output_file = None
    args.download_resume = False
    args.output_options = []
    args.follow = True
    args.check_status = False
    args.quiet = False

# Generated at 2022-06-13 21:41:05.838069
# Unit test for function program
def test_program():
    # TODO: refactor this test
    import io
    import sys

    from httpie.context import Environment
    from httpie.output.streams import WriteFlushWrapper, StdoutBytesWrapper, StderrBytesWrapper
    from httpie.cli.parser import parser

    # monkey patch sys.stdout and sys.stderr so we can catch the output
    sys.stdout = WriteFlushWrapper(StdoutBytesWrapper(io.BytesIO()))
    sys.stderr = WriteFlushWrapper(StderrBytesWrapper(io.BytesIO()))

    # must import after monkey patching
    from httpie.cli.argtypes import KeyValueArgType, JSONDataDict

    # setup environment for testing
    env = Environment()
    env.config = parser.parse_args().config
    env

# Generated at 2022-06-13 21:41:13.295542
# Unit test for function program
def test_program():
    class Args:
        def __init__(self, check_status=False, follow=False, output_file=None, output_options=('pretty',),
                     headers='', quiet=False):
            self.check_status = check_status
            self.follow = follow
            self.output_file = output_file
            self.output_options = output_options
            self.headers = headers
            self.quiet = quiet

    from httpie.output.streams import Streams
    from httpie.input import ParseError

    out = sys.stdout.buffer if sys.version_info[:2] >= (3, 7) else sys.stdout
    err = sys.stderr.buffer if sys.version_info[:2] >= (3, 7) else sys.stderr

# Generated at 2022-06-13 21:41:25.393122
# Unit test for function main
def test_main():
    from httpie.cli.shared import mock_environment
    from io import BytesIO

    env = mock_environment()
    env.stdout = BytesIO()
    env.stderr = BytesIO()

    # TODO: mock args.
    args = [
        'http',
        '--debug',
        '--traceback',
        'httpbin.org'
    ]

    exit_status = main(args=args, env=env)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:29.050603
# Unit test for function program
def test_program():
    program(args=parser.parse_args(args=['GET', 'http://httpbin.org']))

# Generated at 2022-06-13 21:41:36.503010
# Unit test for function main
def test_main():
    # noinspection PyUnresolvedReferences
    import httpie.output.formatters.json

    raw_args = ['http', '--json', 'https://example.com']
    args = decode_raw_args(raw_args, 'utf8')

    assert main(args=args) == ExitStatus.SUCCESS
    assert main(args=args, env=Environment(variables=dict(HTTPIE_CONFIG_DIR=''))) == ExitStatus.SUCCESS
    assert main(args=args, env=Environment(variables=dict(HTTPIE_CONFIG_DIR=''))) == ExitStatus.SUCCESS
    assert main(args=args, env=Environment(variables=dict(HTTPIE_CONFIG_DIR=''))) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:48.226566
# Unit test for function program
def test_program():
    from io import BytesIO
    from httpie.core import main as httpie_main

    from httpie import ExitStatus
    from httpie.cli.parser import parser
    from httpie.client import httpie_stream
    from httpie import ExitStatus
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.plugins import plugin_manager

    env = Environment()
    parser.add_argument = lambda *args, **kwargs: None

    def http(*args, **kwargs):
        return httpie_main(args=args, env=env, **kwargs)

    def localhost_url(path):
        return f'http://localhost:80/{path.lstrip("/")}'

    def raw_request(method, url='/', **kwargs):
        args = []

# Generated at 2022-06-13 21:41:56.458850
# Unit test for function program
def test_program():
    from httpie.cli.args import parse_args
    from httpie.cli.definition import parser
    from httpie.cli.main import program
    from httpie.cli.main import get_output_options
    from httpie.context import Environment
    from io import BytesIO
    from httpie import __version__ as httpie_version

    args: argparse.Namespace = parser.parse_args(args=[
        'http',
        '--check-status',
        '--download'
    ])
    env = Environment()
    exit_status = program(args=args, env=env)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:01.009180
# Unit test for function main
def test_main():
    from tempfile import TemporaryDirectory
    from httpie.config import DEFAULT_CONFIG_DIR
    with TemporaryDirectory() as tempdir:
        try:
            main([
                'httpie',
                '--config-dir', tempdir,
                '--default-options', '--print=H',
                'https://httpbin.org/get',
            ])
        except SystemExit as e:
            assert e.code == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:13.174161
# Unit test for function program
def test_program():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.context import Environment
    from httpie.plugins import get_response_preprocessor_hook_map


# Generated at 2022-06-13 21:46:24.699815
# Unit test for function main
def test_main():
    from httpie.cli.environment import Environment

    env = Environment()
    http.client.HTTPConnection.debuglevel = 0

# Generated at 2022-06-13 21:46:34.645424
# Unit test for function main
def test_main():
    import pytest
    
    with pytest.raises(SystemExit) as e:
        main(args=['', '--debug'])
    assert e.value.code == ExitStatus.SUCCESS
    
    with pytest.raises(SystemExit) as e:
        main(args=['', '--traceback'])
    assert e.value.code == ExitStatus.SUCCESS

    with pytest.raises(SystemExit) as e:
        main(args=['', '--timeout', '0'])
    assert e.value.code == ExitStatus.ERROR_TIMEOUT

    with pytest.raises(SystemExit) as e:
        main(args=['', '--max-redirects', '0'])
    assert e.value.code == ExitStatus.ERROR_TOO_MANY_REDI

# Generated at 2022-06-13 21:46:41.891932
# Unit test for function main
def test_main():
    import io
    import sys
    import unittest

    class ExitStatusTestCase(unittest.TestCase):
        def test_main(self):
            args = ['--debug']
            sys.argv = args

            stdout = io.StringIO()
            stderr = io.StringIO()
            stdin = io.StringIO()

            sys.stdout = stdout
            sys.stderr = stderr
            sys.stdin = stdin

            main()

            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            sys.stdin = sys.__stdin__


# Generated at 2022-06-13 21:46:47.818009
# Unit test for function program

# Generated at 2022-06-13 21:46:53.525954
# Unit test for function program
def test_program():
    args = [
        '--download', '--default-response-headers',
        'https://httpbin.org/get'
    ]
    exit_status = main(args)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:58.770802
# Unit test for function program
def test_program():
    args = ['--form', '--output=INOUT', 'POST', 'http://httpbin.org/post']
    env = Environment(
        stdout=io.StringIO(),
        stdout_isatty=False,
        stderr=io.StringIO(),
        stderr_isatty=False,
        stdin=sys.stdin,
        stdin_isatty=False,
    )
    program(args=parser.parse_args(args=args, env=env), env=env)

# Generated at 2022-06-13 21:47:12.193095
# Unit test for function main
def test_main():
    import pytest
    from httpie.cli.context import Environment
    from httpie.cli.run import main
    from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD

    def request_body_read_callback(chunk: bytes):
        print(chunk)
        print(type(chunk))
        print(chunk.__class__.__name__)

    def test_collect():
        env = Environment()
        args = ['--debug', '--help']
        main(args=args, env=env)

    def test_collect_messages():
        import pprint
        from httpie.cli.collect import collect_messages
        from httpie.cli.definition import parser

        env = Environment()
        parsed

# Generated at 2022-06-13 21:47:19.882503
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    env = Environment()
    args = parser.parse_args(['--verbose', '--headers', '--body', 'http://127.0.0.1:8080/api/v1/login', 'username=testuser', 'password=testpass'], env)
    assert program(args, env) == ExitStatus.SUCCESS