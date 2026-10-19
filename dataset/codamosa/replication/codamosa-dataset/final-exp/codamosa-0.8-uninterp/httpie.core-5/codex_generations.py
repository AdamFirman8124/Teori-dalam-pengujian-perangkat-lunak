

# Generated at 2022-06-13 21:41:04.543471
# Unit test for function program
def test_program():
    from io import StringIO
    env = Environment()
    env.stdout = StringIO()
    parsed_args = argparse.Namespace()
    parsed_args.headers = {
        'Content-Type': 'text/plain',
        'Content-Length': '4'
    }
    parsed_args.output_options = {
        'verbose',
    }
    parsed_args.verbose = True
    parsed_args.output_options = {
        'verbose',
    }
#     parsed_args_completed = main()
    requests.PreparedRequest.url = 'http://www.google.com'
    program(parsed_args, env)
    assert True

test_program()

# Generated at 2022-06-13 21:41:14.568527
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.cli.parser import parser_setup, parser_epilog
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.plugins import plugin_manager

    args = parser.parse_args(
        args=['GET', 'https://google.com/', '-A', 'Chrome/70.0.3538.77'],
        env=Environment())
    plugin_manager.lazy_load_plugins = lambda: None
    plugin_manager.plugin_classes = [HTTPiePlugin]
    plugin_manager.load_installed_plugins()

    parser_setup(parser)
    parser_epilog(parser)

    return program(args, Environment())

# Generated at 2022-06-13 21:41:24.448667
# Unit test for function main
def test_main():
    test_list = ['python3', 'httpie.py', '--debug', '--method', 'get', '--headers', 'Content-Type: application/json', '127.0.0.1:8080', '--body', '{"name": "httpie"}']
    res = main(test_list)
    assert(res == ExitStatus.SUCCESS)

# Generated at 2022-06-13 21:41:34.949725
# Unit test for function program
def test_program():
    env = Environment()
    env.config.debug = True
    env.stdout.buffer = BytesIO()
    """
    Test program with a request to localhost:5000/test with GET method
    that has MockResponse
    with content-type: application/json
    and body: {"hello": "world"}.
    """
    args = [
        "http",
        "localhost:5000/test",
        "--json"
        ]
    program(args=args, env=env)
    assert env.stdout.buffer.getvalue() == b'{\n    "hello": "world"\n}\n'
    assert env.stdout.buffer.getvalue() != b'{\n    "hello": "wrong"\n}\n'

# Generated at 2022-06-13 21:41:47.759019
# Unit test for function main
def test_main():
    from unittest import TestCase
    from unittest.mock import patch
    import tempfile
    from httpie.cli.parser import parse_options

    from httpie import ExitStatus
    from httpie import __main__

    class MainTestCase(TestCase):
        def setUp(self):
            self.temp_dir = tempfile.TemporaryDirectory()
            self.temp_file = tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8')

        def tearDown(self):
            self.temp_file.close()
            self.temp_dir.cleanup()

        def test_parse_error_and_debug(self):
            args = ['GET', 'foo']
            env = Environment()

# Generated at 2022-06-13 21:41:56.848152
# Unit test for function program
def test_program():
    import argparse
    from .context import Environment
    from .output.streams import Streams
    from .config import Config
    from httpie.downloads import Downloader
    from httpie.cli.constants import OUT_REQ_HEAD
    env = Environment()
    env.config = Config(None)
    env.stdout = Streams(None, None)
    env.stderr = Streams(None, None)
    env.stdin = Streams(None, None)
    args = argparse.Namespace()
    args.headers = {}
    args.download = True
    args.follow = True
    args.download_resume = True
    args.output_file = None
    args.check_status = True
    args.output_options = OUT_REQ_HEAD
    program(args, env)



# Generated at 2022-06-13 21:42:01.148409
# Unit test for function program
def test_program():
    args = {
        'headers': [],
        'output_file': '',
        'output_file_specified': True,
        'download': True,
        'check_status': True,
        'download_resume': True,
        'quiet': False,
        'output_options': ['verbose'],
        'follow': True}
    env = Environment()
    assert program(args=args, env=env) is ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:02.112478
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 21:42:08.537017
# Unit test for function main
def test_main():
    import sys
    env = Environment()
    env.stdin_encoding = 'utf-8'
    sys.argv = ['http', '--debug', 'www.baidu.com']
    main(args=sys.argv, env=env)

# Generated at 2022-06-13 21:42:09.732181
# Unit test for function main
def test_main():
    main(['httpie', 'https://api.github.com/users/jakubroztocil'])

# Generated at 2022-06-13 21:43:10.113235
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from io import StringIO
    from httpie.context import Environment
    from httpie.cli.definition import parser
    from httpie.cli.context import Context
    # TODO: Refactor this to use an object instead of a dictionary
    from httpie.output.writer import MESSAGE_SEPARATOR

    args = ['--debug']
    main(args=args)
    res = args[0]
    exp = '--debug'
    assert res == exp, 'Main did not return: "' + exp + '" but: "' + str(res) + '"'
    args = ['-h']
    with patch('sys.stderr') as mock_stderr:
        main(args=args)
        res = mock_stderr.write.call_args[0][0]

# Generated at 2022-06-13 21:43:23.237171
# Unit test for function main
def test_main():
    # mock env
    class StdIO:
        def __init__(self):
            self.stdout = self
            self.stderr = self
            self.stdin = "stdin"
            self.stdout_encoding = "utf8"

        def write(self, *args):
            return "stdout"

    class Env:
        def __init__(self):
            self.stdout = StdIO()
            self.stderr = StdIO()
            self.stdin = "stdin"
            self.stdin_encoding = "utf8"
            self.program_name = "program_name"

        def log(self, level, message, flush):
            pass

        def log_error(self, message: str, level: str = "error"):
            pass


# Generated at 2022-06-13 21:43:31.982922
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli.definition import parser
    import requests
    from requests.exceptions import Timeout

    stdin_encoding = sys.stdin.encoding or 'utf8'
    args = parser.parse_args(
        args=[b'-pvh'],
        env=Environment(stdin_encoding=stdin_encoding),
    )
    env = Environment()

    with pytest.raises(Timeout):
        program(args, env)

    with pytest.raises(requests.TooManyRedirects):
        args = parser.parse_args(
            args=[b'-pvh', '--max-redirects', '0'],
            env=Environment(stdin_encoding=stdin_encoding),
        )
        program(args, env)

# end

# Generated at 2022-06-13 21:43:37.974754
# Unit test for function program
def test_program():
    mock_args = argparse.Namespace(timeout=100, check_status='', output_options='', follow='',
                                   download='', headers='', download_resume='', output_file='',
                                   output_file_specified='', debug='', traceback='', quiet='',
                                   max_redirects='')
    mock_env = Environment()
    assert program(mock_args, mock_env) == ExitStatus.SUCCESS



# Generated at 2022-06-13 21:43:45.900193
# Unit test for function program
def test_program():
    import pytest

    from httpie.cli.constants import OUT_REQ_HEAD, OUT_RESP_BODY
    from httpie.context import Environment
    from httpie.cli.definition import parser

    env = Environment()
    env.stdout_isatty = False
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env.log_error = env.stderr.write

    args = parser.parse_args(
        args=['http', 'example.com', '--output=REQ_HEAD', '--output=RESP_BODY'],
        env=env,
    )
    assert program(args=args, env=env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:54.100486
# Unit test for function program
def test_program():
    import pytest
    import httpie.cli.args
    import httpie.cli.argtypes

    args = [
        'https://www.google.com',
        '--print',
        'all',
        '-v',
        '-A',
        '1.1'
    ]

    env = httpie.cli.args.Environment(
        stdin=None,
        stdin_isatty=False,
        stdout=None,
        stdout_isatty=False,
        stderr=None,
        stderr_isatty=False,
        argv=args,
        config=None,
        output_options=httpie.cli.argtypes.OutputOptions(
            default=None,
            options=[],
        ),
    )

    httpie.cli.args.parse_

# Generated at 2022-06-13 21:44:00.137850
# Unit test for function main
def test_main():
    RETURN_CODE = 7
    with patch('httpie.cli.program') as mock_program:
        # Mock program to return exit code
        mock_program.return_value = RETURN_CODE
        # Call main
        assert main(args=['http']) == RETURN_CODE

# Generated at 2022-06-13 21:44:00.716863
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 21:44:09.984328
# Unit test for function program
def test_program():
    from httpie.core import main
    from httpie.compat import is_windows
    from httpie.output.streams import DefaultEnvironment
    import os
    import subprocess
    import sys
    from tempfile import mkdtemp, mkstemp
    from unittest.mock import patch
    from urllib.parse import urlparse

    class CaptureStdoutStderr(object):
        def __init__(self):
            self.stderr = sys.stderr
            self.stdout = sys.stdout
            self.stderr_fd = None
            self.stdout_fd = None
            self.stdout_filename = None
            self.stderr_filename = None
            self.stderr_r, self.stderr_w = None, None
            self.stdout_r,

# Generated at 2022-06-13 21:44:15.600662
# Unit test for function program
def test_program():
    env = Environment()
    exit_status = program(args=['http', '--output='], env=env)
    assert exit_status  == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:37.136432
# Unit test for function main
def test_main():
    import os
    import unittest
    import tempfile
    import shutil

    # noinspection PyUnresolvedReferences
    import httpie.environment
    # noinspection PyUnresolvedReferences
    from httpie.compat import is_win32
    from httpie.cli.constants import OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
    from httpie.compat import urlopen
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.status import ExitStatus

    from tests.compat import patch, HTTPBIN

    class MainTestCase(unittest.TestCase):
        def setUp(self):
            """Test the main function with some environment."""
            self.temp_config_dir = tempfile.mkdtemp()
            self.env = http

# Generated at 2022-06-13 21:45:38.098267
# Unit test for function main
def test_main():
    print(main(["httpie", "--help"]))

# Generated at 2022-06-13 21:45:51.678222
# Unit test for function program
def test_program():
    import argparse
    args = argparse.Namespace()
    class env:
        log_error = lambda *_: None
    main(['--download'], env)
    main(['--download', '--verbose'], env)
    main(['--download', '--quiet'], env)
    main(['--download', '--output', 'a.txt'], env)
    main(['--download', '--output', 'a.txt', '--verbose'], env)
    main(['--download', '--output', 'a.txt', '--quiet'], env)
    main(['--download', '--output', '-', '--check-status', 'https://httpbin.org/get'], env)

# Generated at 2022-06-13 21:46:03.217747
# Unit test for function program
def test_program():
    from httpie import __version__ as httpie_version
    env = Environment()
    env.program_name = 'http'
    args = argparse.Namespace()
    args.headers = ('')
    args.output_options = ([requests.PreparedRequest])
    args.download = True
    args.output_file = ('')
    args.download_resume = True
    args.follow = True
    args.check_status = True
    args.quiet = True
    args.output_file_specified = True

    # Test cases
    assert program(args, env) is 0
    assert program(args, env)

# Generated at 2022-06-13 21:46:15.663728
# Unit test for function program
def test_program():
    import unittest
    import argparse
    import mock
    import os
    import sys
    import httpie
    from urllib.parse import urlparse, urljoin
    import httpie.cli.argtypes
    import httpie.config
    import httpie.plugins
    import httpie.downloads

    class AssertExitStausTestCase(unittest.TestCase):
        def setUp(self):
            super(AssertExitStausTestCase, self).setUp()
            self.sys_argv = sys.argv
            self.env = os.environ.copy()
            sys.argv = ['http']
            os.environ = {}

        def tearDown(self):
            sys.argv = self.sys_argv
            os.environ = self.env

# Generated at 2022-06-13 21:46:17.435187
# Unit test for function program
def test_program():
    assert program(main, ExitStatus) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:21.114182
# Unit test for function program
def test_program():
    exit_status = program(args=[], env=Environment(stdout=io.StringIO()))
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:46:31.883039
# Unit test for function main
def test_main():
    # Need to import test_main to aid TestMain in test_program.raw()
    # noinspection PyUnresolvedReferences
    from httpie.platform import is_windows
    # noinspection PyUnresolvedReferences
    from httpie.compat import is_py26

    assert (is_py26 or not is_windows)

    from httpie.cli.parser import parser as main_parser
    from httpie.cli.argtypes import KeyValueArgType
    from io import StringIO

    class CaptureOutput:
        def __init__(self, output=StringIO()):
            self.output = output
            self.stdout = output
            self.stderr = output

    class FakeEnvironment:
        def __init__(self):
            self.config = FakeConfig()

# Generated at 2022-06-13 21:46:34.704702
# Unit test for function program
def test_program():
    import httpie.cli.args
    args = httpie.cli.args.parser.parse_args(['https://httpbin.org/get'], env=Environment(stdout_isatty=False))
    assert program(args, env=Environment(stdout_isatty=False)) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:40.804234
# Unit test for function main
def test_main():
    from .cli import program
    from io import StringIO
    from unittest.mock import patch
    from httpie import ExitStatus
    from contextlib import redirect_stdout
    stringio = StringIO()
    args = ['https://www.google.com']
    with patch('sys.stderr', stringio):
        with redirect_stdout(stringio):
            result = program(args=args)
            assert result == ExitStatus.SUCCESS


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:48:29.133691
# Unit test for function program
def test_program():
    result = program()
    assert result == 1

# Generated at 2022-06-13 21:48:33.481062
# Unit test for function program
def test_program():
    from io import StringIO
    args = [
        "http",
        "localhost",
    ]
    env = Environment()
    env.config.directory = ".httpie"
    env.stdin_encoding = "UTF-8"
    env.stdout = StringIO()
    env.stderr = StringIO()
    program(env=env, args=args)


# Generated at 2022-06-13 21:48:35.013680
# Unit test for function program
def test_program():
    assert program([],Environment()) == 0

# Generated at 2022-06-13 21:48:37.031428
# Unit test for function program
def test_program():
    pass



if __name__ == '__main__':
    exit_status = main()
    sys.exit(exit_status)

# Generated at 2022-06-13 21:48:45.368063
# Unit test for function program
def test_program():
    from httpie import config
    from httpie.config import OutputOptions

    class Args:
        def __init__(self, headers, output_options, output_file, quiet, check_status, follow, download, download_resume):
            self.headers = headers
            self.output_options = output_options
            self.output_file = output_file
            self.quiet = quiet
            self.check_status = check_status
            self.follow = follow
            self.download = download
            self.download_resume = download_resume
            self.output_file_specified = output_file is not None

    class Environment:
        def __init__(self):
            self.stderr = sys.stderr


# Generated at 2022-06-13 21:48:57.456144
# Unit test for function program
def test_program():
    args = argparse.Namespace()
    args.config_dir = "D:\Learning\httpie-master\httpie\httpie\config"
    args.default_options = []
    args.download = False
    args.download_resume = True
    args.follow = False
    args.headers = []
    args.output_file = None
    args.output_file_specified = False
    args.output_options = ['h', 'b']
    args.quiet = False
    args.timeout = 30
    args.check_status = True
    args.max_redirects = 30
    args.method = 'GET'
    args.session = None

# Generated at 2022-06-13 21:49:12.326986
# Unit test for function program
def test_program():
    import argparse
    class test_args():
        def __init__(self):
            self.headers = {}
            self.output_options = ['h','b','v']
            self.check_status = False
            self.download = False
            self.quiet = False
            self.max_redirects = 10
            self.output_file_specified = False
            self.output_file = None
            self.download_resume = True
            self.stream = True
            self.timeout = 60
            self.follow = False
            self.method = 'GET'
            self.url = 'http://www.google.com'
    class test_env():
        def __init__(self):
            self.config = None
            self.program_name = ''
        def log_error(self, *arg):
            pass


# Generated at 2022-06-13 21:49:20.576285
# Unit test for function main
def test_main():
    main(['httpie', '--debug'])
    main(['httpie', '--traceback'])
    main(['httpie', '--traceback', 'https://httpbin.org/anything'])
    main(['httpie', '--debug', 'https://httpbin.org/anything'])
    main(['httpie', '--debug', 'https://httpbin.org/anything'])
    main(['httpie'])
    main(['httpie', '--version'])
    main(['httpie', '--help', 'argparse'])
    main(['httpie', '--help', 'request'])
    main(['httpie', 'https://httpbin.org/anything'])
    main(['httpie', 'https://httpbin.org/anything', '--help'])

# Generated at 2022-06-13 21:49:32.722521
# Unit test for function program
def test_program():
    from httpie import parser
    from httpie.cli.definition import parser
    from httpie.output.streams import Streams
    from httpie.context import Environment
    import tempfile
    import io
    output_file = tempfile.TemporaryFile()

# Generated at 2022-06-13 21:49:34.001570
# Unit test for function main
def test_main():
    args = ['main']
    main(args)

