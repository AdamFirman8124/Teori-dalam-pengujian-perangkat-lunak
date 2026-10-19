

# Generated at 2022-06-13 21:40:37.727924
# Unit test for function program
def test_program():
    arg = argparse.Namespace()
    arg.download = False
    assert program(args = arg, env = Environment) == ExitStatus.SUCCESS
    arg.download = True
    arg.follow = True
    assert program(args = arg, env = Environment) == ExitStatus.SUCCESS
    assert program(args = arg, env = Environment) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:40:40.489937
# Unit test for function main
def test_main():
    """test function main"""
    # No args
    main(args=['http'])

    # Invalid option
    import pytest
    with pytest.raises(SystemExit) as exc:
        main(args=['http', '--debug', '--invalid'])
    assert exc.value.code == ExitStatus.ERROR

# Generated at 2022-06-13 21:40:47.993864
# Unit test for function program
def test_program():
    import pytest
    import httpie.cli.parser
    args = httpie.cli.parser.parser.parse_args('https://httpbin.org/get'.split())
    env = Environment()
    exit_status = program(args=args, env=env)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:40:59.912241
# Unit test for function main
def test_main():
    def test_args(*args: str, expected_return_value: int) -> None:
        from io import StringIO
        from contextlib import redirect_stderr
        for stdin_encoding in ('utf8', 'latin1'):
            ret = main([sys.argv[0]] + [f.encode(stdin_encoding) for f in args],
                       Environment(stdin=None, stdout=StringIO(), stderr=StringIO(),
                                   stdin_encoding=stdin_encoding))
            assert ret == expected_return_value
    # Unit test function main
    test_args('GET', '--help', expected_return_value=0)
    test_args('GET', '--debug', expected_return_value=0)

# Generated at 2022-06-13 21:41:01.995634
# Unit test for function main
def test_main():
    httpie.main()

if __name__ == '__main__':
    httpie.main()

# Generated at 2022-06-13 21:41:10.988413
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.status import ExitStatus
    HTTPiePlugin().load()
    args = parser.parse_args(
        args=[
            '--output-options=b',
            '--follow',
            'http://httpbin.org/get'
        ],
        env=Environment(),
    )
    assert program(args=args, env=Environment()) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:13.463676
# Unit test for function program
def test_program():
    assert program() == ExitStatus.SUCCESS



# Generated at 2022-06-13 21:41:25.096141
# Unit test for function main
def test_main():
    from httpie.cli.config import Config
    from httpie.cli.environment import Environment
    # noinspection PyTypeChecker
    env = Environment()
    setattr(env, 'program_version', '0.9.9')
    setattr(env, 'default_options', [])
    setattr(env, 'config_dir', 'httpie')
    setattr(env, 'config', Config())

    args = ['--download', 'http://localhost:5000/api/search/', '-o', './sample.json']  # test --download option
    # args = ['http://localhost:5000/api/search/', '-o', './sample.json']  # test --download option
    main(args, env)

# Generated at 2022-06-13 21:41:32.055195
# Unit test for function program
def test_program():
    import os
    #construct the path
    filepath = os.path.dirname(os.path.abspath(__file__))+"/test.json"

    # run the program
    exit_status = program(['-j'], '{"hello":"world"}')

    # test the output of the program
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:36.980849
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args([
        'www.google.com'
    ])
    env = Environment()
    program(args, env)
    assert not env.stderr.isatty()
    assert not env.stdout.isatty()

test_program()

# Generated at 2022-06-13 21:42:39.280824
# Unit test for function main
def test_main():
    args = ['http', 'localhost:1213']
    exit_status = main(args)
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:42:45.392284
# Unit test for function program
def test_program():
    args = argparse.Namespace(follow=True, headers=[], method='GET', output_file=None, output_file_specified=False, output_options=['H', 'B'], quiet=False, traceback=False, url='http://www.google.com')
    test_env = Environment()
    main(program(args=args, env=test_env))

# Generated at 2022-06-13 21:43:00.499678
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie import ExitStatus


# Generated at 2022-06-13 21:43:06.362663
# Unit test for function main
def test_main():
    from httpie.cli.constants import UTF8
    #from httpie.cli.context import Environment
    from httpie.cli.definitions.parser import parse_args

    env = Environment()
    args = decode_raw_args(sys.argv, UTF8)
    if env.config.default_options:
        args = env.config.default_options + args
    parsed_args = parse_args(args=args, env=env)
    program(args=parsed_args, env=env)

# Generated at 2022-06-13 21:43:08.087391
# Unit test for function program
def test_program():
    program()
    assert True

# Generated at 2022-06-13 21:43:11.414649
# Unit test for function program
def test_program():
    """
    Any function that has a yield statement is a generator.
    """
    args = program(['soup'], 'env')
    assert isinstance(args, ExitStatus)



# Generated at 2022-06-13 21:43:24.482478
# Unit test for function main
def test_main():
    import sys
    import os
    import platform
    import subprocess
    #import pytest
    #import click
    from httpie.cli.constants import OUT_REQ_BODY, OUT_RESP_HEAD
    from httpie.context import Environment
    from httpie.status import ExitStatus, http_status_to_exit_status
    from httpie.downloads import Downloader
    from httpie.output.writer import write_message, write_stream, MESSAGE_SEPARATOR_BYTES
    from httpie.plugins.registry import plugin_manager
    from httpie.client import collect_messages

    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)


# Generated at 2022-06-13 21:43:32.416631
# Unit test for function main
def test_main():
    """
    Test case for function main
    """
    def test_pass():
        env = Environment()
        args = ['--debug']
        assert main(args, env) == 0

    def test_success():
        env = Environment()
        args = ['httpie', '--debug']
        assert main(args, env) == 0

    def test_fail():
        env = Environment()
        args_fail = ['httpie', 'www.google.com', '--traceback']
        assert main(args_fail, env) == 1

    def test_timeout():
        env = Environment()
        args_fail = ['httpie', 'www.google.com', '--timeout=0.05', '--traceback']
        assert main(args_fail, env) == 52


# Generated at 2022-06-13 21:43:41.125431
# Unit test for function program
def test_program():
    import requests
    import pytest
    from httpie import ExitStatus
    from httpie.cli.parser import parse_args
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE

    args = parse_args(args=tuple(HttpieArgumentParser().parse_args(['--debug'])))
    exit_status = program(args=args, env=Environment())
    assert exit_status == ExitStatus.ERROR

    args = parse_args(args=tuple(HttpieArgumentParser().parse_args(['--debug', '--traceback', 'https://httpbin.org/get'])))
    with pytest.raises(requests.ConnectionError):
        program(args=args, env=Environment())
        exit_status = ExitStatus.ERROR


# Generated at 2022-06-13 21:43:52.628111
# Unit test for function program

# Generated at 2022-06-13 21:45:14.679557
# Unit test for function main
def test_main():
    assert main(['--debug']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:21.549240
# Unit test for function program
def test_program():
    import os
    from httpie.compat import unquote
    from urllib.parse import urlparse
    from httpie.utils import get_path_and_query_from_url
    from httpie.input import ParseError, KeyValue
    from httpie.auth import get_auth_from_url, get_netrc_auth, HTTPBasicAuth
    from httpie.status import ExitStatus
    from httpie.cli.definition import parser
    from httpie.client import load_auth_from_auth_plugin, load_auth
    from httpie import ExitStatus
    from httpie.argumentparser import CustomParser
    from httpie.downloads import Downloader
    from httpie.input import KeyValue
    from httpie.config import Config
    from httpie.utils import get_path_and_query_from_url, get_headers_

# Generated at 2022-06-13 21:45:30.677316
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.tests.compat import patch
    from httpie.tests.data import (
        HTTP_OK,
        HTTP_PROXY_OK,
        HTTP_PROXY_OK_IPV6,
        NORMAL_FORM,
        JSON_DATA
    )
    from httpie.client import collect_messages
    from httpie.output.writer import write_message
    from httpie.cli.parser import parse_querystring
    args = parser.parse_args(['http://127.0.0.1', 'param1==value1', 'param2==value2'])
    messages = collect_messages(args)
    with patch('sys.stdin', StringIO(NORMAL_FORM)):
        stdout = StringIO()

# Generated at 2022-06-13 21:45:46.983070
# Unit test for function main
def test_main():
    from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
    from httpie.context import Environment

    class MockStdout:
        text = ''

        def write(self, txt):
            self.text += txt

    class MockStderr:
        text = ''

        def write(self, txt):
            self.text += txt

    class MockArgs:
        output_options = []
        data = None
        file = None
        headers = {}

    stdout = MockStdout()
    stderr = MockStderr()
    args = MockArgs()

    def program(args, env):
        env.stdout.write('ok')
        return ExitStatus.SUCCESS


# Generated at 2022-06-13 21:45:48.179614
# Unit test for function program
def test_program():
    assert ExitStatus.SUCCESS == program(args="httpie", env="")

# Generated at 2022-06-13 21:45:58.939366
# Unit test for function program
def test_program():
    from httpie import cli

    exit_status = None
    sys.argv = ['httpie', '-B', 'http://httpbin.org/get']
    exit_status = cli.program(['httpie', '-B', 'http://httpbin.org/get'])
    print(exit_status)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:08.190978
# Unit test for function program
def test_program():
    try:
        program(['--download'])
    except KeyboardInterrupt:
        exit_status = ExitStatus.ERROR_CTRL_C
    except requests.Timeout:
        exit_status = ExitStatus.ERROR_TIMEOUT
    except requests.TooManyRedirects:
        exit_status = ExitStatus.ERROR_TOO_MANY_REDIRECTS
    except Exception:
        exit_status = ExitStatus.ERROR

    assert exit_status == ExitStatus.SUCCESS


if __name__ == '__main__':
    code = main()
    sys.exit(code)

# Generated at 2022-06-13 21:46:15.783999
# Unit test for function main
def test_main():
    assert main(['http', '--version']) == 0
    assert main(['http', '--help']) == 0
    # with pytest.raises(SystemExit) as excinfo:
    #     main(['http', 'https://httpbin.org/put', 'hehe=a'])
    #     assert excinfo.value.code == 0
    # with pytest.raises(SystemExit) as excinfo:
    #     main(['http', 'https://httpbin.org/put', 'haha'])
    #     assert excinfo.value.code == 2
    # with pytest.raises(SystemExit) as excinfo:
    #     main(['http', 'https://httpbin.org/put', 'noexistfile'])
    #     assert excinfo.value.code == 3
    # with py

# Generated at 2022-06-13 21:46:20.057941
# Unit test for function main
def test_main():
    assert main(['http', 'https://google.com']) == 0
    assert main(['http', 'https://google.com', '--debug']) == 0
    assert main(['http', 'https://google.com', '--traceback']) == 3

# Generated at 2022-06-13 21:46:21.727331
# Unit test for function program
def test_program():
    print(program(args=['https://github.com']))

# Generated at 2022-06-13 21:47:05.749868
# Unit test for function program
def test_program():
    env = Environment()
    args = ['--download', '--output=file.html']
    status = program(argparse.Namespace(args), env)
    assert status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:16.992756
# Unit test for function main
def test_main():
    env = Environment()
    env.stderr = sys.stderr
    env.stdout = sys.stdout
    args = ["--check-status", "https://httpbin.org/status/200"]
    exit_status = main(args, env)
    assert exit_status == 0

    args = ["--check-status", "https://httpbin.org/status/404"]
    exit_status = main(args, env)
    assert exit_status == ExitStatus.ERROR_HTTP_4XX

    args = ["--check-status", "https://httpbin.org/status/500"]
    exit_status = main(args, env)
    assert exit_status == ExitStatus.ERROR_HTTP_5XX

# Generated at 2022-06-13 21:47:33.628632
# Unit test for function main
def test_main():
    import pytest
    import os
    import sys
    import platform as _platform
    print ("test_main:")

    # set env for test
    os.environ['HTTPIE_DEBUG'] = 'True'
    os.environ['HTTPIE_CONFIG_DIR'] = './config'
    os.environ['HTTPIE_CONFIG_PATH'] = './config/config.json'
    os.environ['HTTPIE_SESSION_PATH'] = './config/session.json'

    # check HTTPIE version & arguments
    assert __version__ == httpie_version
    assert sys.argv[0] is not None

    # check output
    sys.stdout = open(os.devnull, 'wb')
    sys.stderr = open(os.devnull, 'wb')

    # check Platform info &

# Generated at 2022-06-13 21:47:34.303613
# Unit test for function program
def test_program():
    pass

# Generated at 2022-06-13 21:47:43.126743
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.cli.parse import get_parser
    env = Environment()
    args = parser.parse_args(get_parser(env=env).parse_args(['https://httpbin.org/get', '--json']))
    assert program(args=args, env=env) == ExitStatus.SUCCESS
    assert program(args=parser.parse_args(get_parser(env=env).parse_args(['https://httpbin.org/status/500', '--json'])), env=env) == ExitStatus.ERROR_HTTP
    assert program(args=parser.parse_args(get_parser(env=env).parse_args(['https://httpbin.org/status/202', '--json'])), env=env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:54.271382
# Unit test for function program
def test_program():
    def _test_program_with_args(args: List[str], expected_exit_status: int = ExitStatus.SUCCESS):
        actual_exit_status = main(['http', *args])
        assert actual_exit_status == expected_exit_status

    from httpie.cli import builtin_plugins

    builtin_plugins.load_default_plugins()

    _test_program_with_args(
        args=['https://httpbin.org/get'],
        expected_exit_status=ExitStatus.SUCCESS,
    )

    _test_program_with_args(
        args=['https://httpbin.org/status/404'],
        expected_exit_status=ExitStatus.ERROR_HTTP_4XX,
    )


# Generated at 2022-06-13 21:48:00.332798
# Unit test for function main
def test_main():
    assert main(['http', 'get', 'example.com']) == ExitStatus.SUCCESS
    assert main(['http', 'get', 'http://example.com']) == ExitStatus.SUCCESS
    assert main(['http', 'get', 'https://example.com']) == ExitStatus.SUCCESS


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:48:03.588398
# Unit test for function main
def test_main():
    import os
    env = Environment(directory=os.path.expanduser('~/.httpie'))
    exit_status = main(['--help'],env=env)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:48:13.645935
# Unit test for function program
def test_program():
    assert main(["httpie.py", "--json", "http://httpbin.org/status/200"]) ==ExitStatus.SUCCESS
    assert main(["httpie.py", "--json", "http://httpbin.org/status/404"]) ==ExitStatus.ERROR_HTTP_4XX
    assert main(["httpie.py", "--json", "http://httpbin.org/status/500"]) ==ExitStatus.ERROR_HTTP_5XX
    assert main(["httpie.py", "--json", "http://httpbin.org/status/300"]) ==ExitStatus.ERROR_TOO_MANY_REDIRECTS
    assert main(["httpie.py", "--json", "http://httpbin.org/status/300", "--max-redirects=0"]) ==ExitStatus.ERROR_T

# Generated at 2022-06-13 21:48:26.082370
# Unit test for function program
def test_program():
    """
    Unit tests for main program.

    """
    env = Environment()
    class TestParser(argparse.ArgumentParser):
        def __init__(self):
            super().__init__(add_help=False)
            self.add_argument('-v', '--verbose', action='store_true')
            self.add_argument('-F', '--form', action='store_true')
            self.add_argument('-A', '--auth', action='store_true')
            self.add_argument('-H', '--headers', action='store_true')
            self.add_argument('-b', '--body', action='store_true')
            self.add_argument('-f', '--follow', action='store_true')

# Generated at 2022-06-13 21:50:00.506760
# Unit test for function main
def test_main():
    from httpie import ExitStatus
    from httpie._compat import is_windows

    args = ['main', 'https://example.org']
    from httpie.cli import env
    env.stdin_encoding = 'utf8'
    assert main(args, env) == ExitStatus.SUCCESS

    args = ['main', 'https://example.org']
    assert main(args) == ExitStatus.SUCCESS

    args = ['main', '--output', '-', 'https://example.org']
    assert main(args) == ExitStatus.SUCCESS

    args = ['main', '--output=-', 'https://example.org']
    assert main(args) == ExitStatus.SUCCESS

    args = ['main', '--debug']
    assert main(args) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:50:12.417113
# Unit test for function main
def test_main():
    import os
    import sys
    from contextlib import contextmanager
    from io import StringIO
    from tempfile import TemporaryDirectory
    from unittest import TestCase

    from httpie.config import Config
    from httpie.context import Environment

    from . import main, MESSAGE_SEPARATOR_BYTES

    class IntegrationTestCase(TestCase):

        def setUp(self):
            self.env = Environment()
            self.env.stdout = self.env.stderr = StringIO()
            self.config_dir = os.path.join(os.path.dirname(__file__), 'config')

        @contextmanager
        def env(self, **kwargs):
            old_env_attrs = dict((name, getattr(self.env, name)) for name in kwargs)