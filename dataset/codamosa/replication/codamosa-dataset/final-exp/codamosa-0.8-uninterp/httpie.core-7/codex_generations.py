

# Generated at 2022-06-13 21:41:04.409829
# Unit test for function program
def test_program():
    from httpie import ExitStatus
    from httpie.cli.parser import get_parser

    args = get_parser().parse_args(args=[
        '--traceback',
        'https://httpbin.org/get',
        'a=1',
        'b == \'2\'',
    ])
    assert args.output_options == {OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD}
    assert program(args=args, env=Environment()) == ExitStatus.SUCCESS


test_program()
exit(main())

# Generated at 2022-06-13 21:41:14.989359
# Unit test for function program
def test_program():
    class MockArgs(object):
        output_options = {OUT_RESP_HEAD, OUT_RESP_BODY}
        follow = True
        check_status = True
        quiet = False
        output_file = None
        output_file_specified = False

    class MockInput(object):
        def __init__(self, f):
            self.f = f
            self.status_code = 200
            self.reason = 'ok'
            self.raw = object()
            self.headers = 'headers'
            self.request = None
            self.url = 'url'
            self.encoding = 'utf-8'
            self.text = 'text'
            self.content = b'content'
            self.elapsed = 1.0

        def read(self):
            yield MockInput(self.f)

   

# Generated at 2022-06-13 21:41:28.723230
# Unit test for function program
def test_program():
    """
    Run unit test on function program 
    """
    import io
    import unittest
    from unittest.mock import patch
    from httpie.context import Environment
    from httpie.cli import parser
    import requests
    import http.client


    class TestProgram(unittest.TestCase):
        def setUp(self):
            self.env = Environment()

        def test_error_exit_status(self):
            args = parser.parse_args("http://httpbin.org/post --json '{}'".split(" "), self.env)
            exit_status = program(args, self.env)
            self.assertEqual(exit_status, ExitStatus.SUCCESS)


# Generated at 2022-06-13 21:41:33.188393
# Unit test for function main
def test_main():
    # assert main(['--debug']) in (ExitStatus.SUCCESS, ExitStatus.ERROR)
    # assert main(['--debug', 'http://example.org']) in (ExitStatus.SUCCESS, ExitStatus.ERROR)
    # assert main(['http://httpbin.org', 'GET', 'Accept:']) in (ExitStatus.SUCCESS, ExitStatus.ERROR)
    pass

# Generated at 2022-06-13 21:41:47.281317
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser

    args = ['https://google.com']
    parsed_args = parser.parse_args(args=args)
    assert main(['', *args]) == ExitStatus.SUCCESS
    assert main(['', '--help']) == ExitStatus.SUCCESS
    assert main(['', '-h']) == ExitStatus.SUCCESS
    assert main(['', '--help-all']) == ExitStatus.SUCCESS
    assert main(['', '--version']) == ExitStatus.SUCCESS
    assert main(['', '--debug']) == ExitStatus.SUCCESS
    assert main(['', '--traceback']) == ExitStatus.SUCCESS
    assert main(['', '--check-status']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:56.244783
# Unit test for function main
def test_main():
    import argparse
    import os
    import sys
    from httpie.compat import urlsplit

    from httpie.cli.context import Environment

    def _decode_urlsplit(url):
        url = urlsplit(url)
        url = url._replace(netloc=url.netloc.encode('latin1').decode('utf8'))
        return url

    # parse_args
    parser = argparse.ArgumentParser()
    args, remain = parser.parse_known_args(['--ignore-stdin', '--json', '{"k":"v"}'])
    assert args.ignore_stdin
    assert args.json == '{"k":"v"}'
    assert not remain

    # decode_raw_args
    assert decode_raw_args(['a']) == ['a']

# Generated at 2022-06-13 21:42:02.012847
# Unit test for function program
def test_program():
    import mock
    import pytest
    from httpie.cli.parser import parser
    args = parser.parse_args([])
    with pytest.raises(NotImplementedError):
        program(args, mock.Mock())
        # assert program(args, mock.Mock()) is None

# Generated at 2022-06-13 21:42:13.523241
# Unit test for function program
def test_program():
    # test case where:
    # * url is not given and it is stdin,
    # * there are two headers (no value),
    # * only response body is required.
    # * compression (gzip) is used.
    # * verbose is required.
    # * output is redirected to file.
    # * stdout is not a tty.

    class MockArgs:
        url = None
        stdin = '-'
        headers = ['Accept', 'Content-type']
        output_options = [OUT_RESP_BODY]
        output_file_specified = True
        output_file = "mock.txt"
        check_status = False
        follow = False
        download = False
        quiet = False
        verbose = True
        debug = False
        traceback = False


# Generated at 2022-06-13 21:42:17.416694
# Unit test for function program
def test_program():
    args = main(['https://www.v2ex.com/api/members/show.json'])
    assert args == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:18.729602
# Unit test for function program
def test_program():
    # TODO: write unit test for function program
    pass

# Generated at 2022-06-13 21:42:36.484529
# Unit test for function program
def test_program():
    exit_status = program(['https://httpbin.org/ip'])
    assert exit_status == 0

# Generated at 2022-06-13 21:42:38.248027
# Unit test for function main
def test_main():
    try:
        main()
    except:
        assert False


# Generated at 2022-06-13 21:42:41.893752
# Unit test for function main
def test_main():
    exit_status, _ = main(['http','httpie.org','--json','a=b'])
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:46.682078
# Unit test for function main
def test_main():
    assert main(args=['httpie.py']) == ExitStatus.ERROR
    assert main(args=['httpie.py', 'http://example.org']) == ExitStatus.SUCCESS
    assert main(args=['httpie.py', 'http://example.org:1']) == ExitStatus.ERROR

# Generated at 2022-06-13 21:43:00.812282
# Unit test for function program

# Generated at 2022-06-13 21:43:09.114771
# Unit test for function program
def test_program():
    try:
        import http.client
    except ImportError:
        import httplib as http_client  # type: ignore
    try:
        import urllib.parse
    except ImportError:
        import urlparse as urllib_parse  # type: ignore
    env = Environment()
    parser = argparse.ArgumentParser('program', 'program', 'program')
    env.stdout = open('/tmp/stdout', 'wb')

# Generated at 2022-06-13 21:43:15.682713
# Unit test for function main
def test_main():
    class StderrMock:
        text = ''
        def write(self, string):
            self.text += string
        pass
    mock_stderr = StderrMock()
    main(['httpie', '-F', './client.py', 'http://localhost:5000/test'],
         env=Environment(stderr=mock_stderr))
    assert "Incomplete download" in mock_stderr.text

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:43:19.497425
# Unit test for function main
def test_main():
    assert main(['http', 'httpbin.org', 'Accept:application/json']) == 0
    assert main(['http', 'httpbin.org', 'Accept:text/html']) == 0

# Generated at 2022-06-13 21:43:30.757177
# Unit test for function program
def test_program():
    from httpie import ExitStatus
    from httpie import cli
    from httpie.cli.argtypes import KeyValueArgType
    from httpie import configure
    from httpie.compat import OrderedDict
    from httpie.context import Environment
    from httpie.plugins import plugin_manager
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPTokenAuth
    from httpie.plugins.registry import plugin_manager
    """
    The program unit test
    """
    plugin_manager.load_installed_plugins()
    env = Environment()
    configure.load_config(env)
    env.stdout.isatty = lambda: True

# Generated at 2022-06-13 21:43:40.325638
# Unit test for function program
def test_program():
    env = Environment(
        headers=[],
        stdin_encoding='utf-8',
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    env.config.detect_proxy = False
    env.config.default_options = []
    env.config.default_headers = []
    env.config.output_options = []
    env.config.directory = os.getcwd()
    env.config.history_file = "history.txt"
    env.config.download_dir = None
    env.config.default_options = []

# Generated at 2022-06-13 21:46:56.939369
# Unit test for function main
def test_main():
    status = main()
    assert status == 0

# Generated at 2022-06-13 21:47:03.214985
# Unit test for function main
def test_main():
    args = [
        'httpie',
        '-m',
        'GET',
        'https://httpbin.org/get',
        'User-Agent:HTTPie/0.9.2',
        'Accept-Encoding:gzip,deflate',
        'Accept: */*',
        'Connection:keep-alive'
    ]
    main(args)


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 21:47:10.467337
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args(['--json', 'http://example.org/get'])
    env = Environment()
    program(args=args, env=env)
    get_output_options(args=args, message='requests.PreparedRequest')

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:47:17.463985
# Unit test for function program
def test_program():
    from httpie.context import Environment
    from httpie.cli.parser import parser

    args = parser.parse_args(
        args=[
            '--output-options=Hb',
            '--pretty=none',
            'https://httpie.org/',
            'https://httpie.org/docs/'
        ],
        env=Environment()
    )
    exit_status = program(args=args, env=Environment())
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:47:20.715815
# Unit test for function program
def test_program():
    args = "get httpbin.org/get".split(" ")
    print(program(args))

if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:47:36.235039
# Unit test for function program
def test_program():
    import io
    import shlex
    import sys
    # noinspection PyTypeChecker
    import unittest

    from httpie.cli.argtypes import KeyValueArgType
    from httpie.compat import is_py26, is_windows
    from httpie.context import Environment
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.plugins import builtin
    from httpie.status import ExitStatus

    from tests.httpbin import RESOURCES

    class TestProgramTestCase(unittest.TestCase):

        def setUp(self):
            self.default_args = [
                '--ignore-stdin',
                '--print=B',
                '--verbose',
                '--style=foo',
            ]
            self.style = builtin.style

# Generated at 2022-06-13 21:47:39.989700
# Unit test for function main
def test_main():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    # import sys
    # print(main(sys.argv))
    test_main()

# Generated at 2022-06-13 21:47:53.190953
# Unit test for function main
def test_main():
    from unittest.mock import Mock, patch
    from httpie.cli import default_options
    from httpie.cli.constants import OUT_BODY
    from httpie.context import Environment
    program_name = '/usr/local/bin/http'
    # 这里的env我没有用到，这是传入的参数。
    # 这里的env是可以的，因为httpie.context里的Environment的构造函数，初始化的时候，已经有了默认值，所以可以传None
    # 这是个

# Generated at 2022-06-13 21:47:58.051494
# Unit test for function main
def test_main():
    import httpie.cli.args
    from httpie.core import main
    from httpie.core import httpie
    args = httpie.cli.args.parse_args()
    result = main(args=args)
    assert result == 0

if __name__ == '__main__':
    test_main()
    result = main()
    sys.exit(result)

# Generated at 2022-06-13 21:48:00.917973
# Unit test for function main
def test_main():
    assert main([]) == 0
    assert main(['--debug']) == 0
    assert main(['httpbin.org']) == 0


if __name__ == "__main__":
    test_main()

# Generated at 2022-06-13 21:49:13.470470
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser

    # TODO: Consider removing the following tests and just running `http --version --debug`.
    # Test 1.
    exit_status = main(args=['--version', '--debug'])
    assert exit_status == ExitStatus.SUCCESS

    # Test 2.
    exit_status = main(args=['--version', '--debug', '--output-file=-'])
    assert exit_status == ExitStatus.SUCCESS

    # Test 3.
    exit_status = main(args=['--version', '--debug', '--output-file', '-'])
    assert exit_status == ExitStatus.SUCCESS

    # Test 4.
    exit_status = main(args=['--version', '--debug', '--output-file', '-', 'example.org'])

# Generated at 2022-06-13 21:49:16.641842
# Unit test for function program
def test_program():
    from . import env

    args = parser.parse_args(
        args=[],
        env=env.Environment(),
    )
    return program(args, env.Environment())

# Generated at 2022-06-13 21:49:29.422214
# Unit test for function main
def test_main():
    class Stdout(object):
        def __init__(self):
            self.written = []
        def write(self, data):
            self.written.append(data)
    args = ['a','b','--style','solarized']
    env = Environment()
    env.log_error = Stdout().write
    env.log_info = Stdout().write
    # Test --style and control chars
    assert main(args, env) == 0
    assert '\x1b[33m' in env.log_error.written
    # Test --debug and control chars
    assert main(['--debug']) == 0
    assert '\x1b[33m' in env.log_info.written
    # Test --help and control chars
    assert main(['--help']) == 1

# Generated at 2022-06-13 21:49:36.198340
# Unit test for function main
def test_main():
    import io
    from httpie.cli.constants import URL
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.context import Environment
    env = Environment()
    env.stdout = io.StringIO()
    env.stderr = io.StringIO()
    env.stdin = io.StringIO()
    env.config.directory = DEFAULT_CONFIG_DIR
    exit_status = main(args=['httpie', URL], env=env)
    assert env.stdout.getvalue() != ''
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:39.343623
# Unit test for function program
def test_program():
    from click.testing import CliRunner

    from httpie.cli.definition import parser as cli
    from httpie import version

    runner = CliRunner()
    result = runner.invoke(cli, ['--debug'])
    assert 'HTTPie ' + version.__version__ in result.output



# Generated at 2022-06-13 21:49:49.695810
# Unit test for function main
def test_main():
    from httpie.cli.parser import parser
    parsed_args = parser.parse_args(
        args=[
            '--json',
            'https://example.com/',
            'Content-Type:application/json',
            'x:1',
            'y:2'
        ],
    )
    try:
        main(
            args=[
                'http',
                '--json',
                'https://example.com/',
                'Content-Type:application/json',
                'x:1',
                'y:2'
            ]
        )
    except SystemExit as e:
        assert e.code == 200
    try:
        main(
            args=[
                'http',
                '--debug'
            ]
        )
    except SystemExit as e:pass

# Generated at 2022-06-13 21:49:59.601251
# Unit test for function program
def test_program():
    import pytest
    import httpie.cli.argtypes
    #import io
    #from httpie.compat import is_windows
    #from httpie.cli.exceptions import ParseError
    #env.stdout = io.BytesIO()
    try:
        program([
            'httpie',
            'GET',
            'https://httpbin.org/get',
            'foo:bar',
            'baz',
            'bin',
            "Authorization: 'oauth' something",
        ], env=Environment())
    except SystemExit as e:
        assert e.code == 0
    else:
        assert False
    #with open('httpie/tests/mytest.txt', 'w') as file:
    #    file.write(str(env.stdout.getvalue()))


# Generated at 2022-06-13 21:50:04.832439
# Unit test for function main
def test_main():
    assert main() == ExitStatus.SUCCESS

    assert main(args=['foo']) == ExitStatus.ERROR

    assert main(args=['foo', 'http://httpbin.org/']) == ExitStatus.SUCCESS

if __name__ == '__main__':
    # Unit test for function main
    test_main()

# Generated at 2022-06-13 21:50:06.874662
# Unit test for function main
def test_main():
    assert main(args=['--version']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:50:22.940848
# Unit test for function program
def test_program():
    args = argparse.Namespace(
        headers = [
            'Content-Type: application/json',
            'Accept: application/json'
        ],
        output_options = [],
        output_file = open('/dev/null', 'wb'),
        output_file_specified = True,
        output_file_opener = open,
        download = True,
        follow = [],
        timeout = '',
        max_redirects = '',
        check_status = [],
        download_resume = True,
        quiet = [],
        style = '',
        style_sheet = '',
        colors = False,
        form = [],
        body = [],
        body_type = ''
    )

    env = Environment({})

    program(args=args, env=env)