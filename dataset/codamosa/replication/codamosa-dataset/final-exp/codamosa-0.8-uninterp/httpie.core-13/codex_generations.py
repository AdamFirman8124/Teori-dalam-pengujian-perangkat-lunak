

# Generated at 2022-06-13 21:40:54.267528
# Unit test for function program
def test_program():
    assert program(1,1) == 0

# Generated at 2022-06-13 21:40:57.413525
# Unit test for function program
def test_program():
    import httpie.cli.definition as cli
    args = cli.parser.parse_args(
        args=['https://httpbin.org/get'],
        env = Environment(),
    )
    program(args)


# Generated at 2022-06-13 21:41:09.835711
# Unit test for function program
def test_program():
    """
    Test the main program by making sure that no errors are thrown.

    """
    import os.path
    from httpie.config import BaseConfig
    from httpie.context import Environment
    import httpie.plugins
    from httpie.cli.definition import parser
    from httpie.output.streams import UnsupportedOutputStreamError

    config = BaseConfig(directory=os.path.expanduser('~/.httpie'))
    env = Environment(config=config, stdin=None, stdin_isatty=False, stdout=None, stdout_isatty=False, stderr=None,
                      stdout_bytes_written=0)
    env.config.output_options = ('all',)


# Generated at 2022-06-13 21:41:26.858685
# Unit test for function main
def test_main():
    import io
    import sys

    # noinspection PyUnresolvedReferences
    import pytest

    from httpie import ExitStatus
    from httpie.cli.constants import DEFAULT_TIMEOUT

    class RecordingEnvironment(Environment):
        expected_config_dir = os.path.expanduser('~/.httpie')
        log_error_called = False
        log_error_msg: Optional[str] = None

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.stdout = io.BytesIO()
            self.stderr = io.BytesIO()

        def log_error(self, msg: str, *args, **kwargs):
            self.log_error_called = True
            self.log_error_msg = msg

    env

# Generated at 2022-06-13 21:41:32.448136
# Unit test for function main
def test_main():
    assert main(['httpie']) == ExitStatus.SUCCESS
    assert main(['httpie', '--help']) == ExitStatus.SUCCESS
    assert main(['httpie', '--help', '--debug']) == ExitStatus.SUCCESS
    assert main(['httpie', 'GET', 'http://localhost']) == ExitStatus.SUCCESS



# Generated at 2022-06-13 21:41:37.992743
# Unit test for function program
def test_program():
    # TODO: https://github.com/jakubroztocil/httpie/issues/236
    pass



# Generated at 2022-06-13 21:41:45.015422
# Unit test for function program
def test_program():
    args = parse_args(['http', 'www.google.com', 'Accept:application/json'])
    env = Environment()
    env.stdout = sys.stdout
    assert program(args=args, env=env) == ExitStatus.SUCCESS


if __name__ == '__main__':
    import sys
    from . import cli

    sys.exit(cli.main())

# Generated at 2022-06-13 21:41:56.710428
# Unit test for function main
def test_main():
    from httpie.client import collect_messages
    from httpie.compat import urljoin
    from httpie.downloads import Downloader
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.output.writer import write_message, write_stream, MESSAGE_SEPARATOR_BYTES
    from httpie.plugins.registry import plugin_manager
    from httpie.status import ExitStatus, http_status_to_exit_status
    program_name = "http"
    env=Environment()
    env.program_name = os.path.basename(program_name)
    args = ['GET', 'http://httpbin.org', '--debug']

# Generated at 2022-06-13 21:42:07.168837
# Unit test for function program
def test_program():
    def mock_collect_messages():
        yield requests.PreparedRequest()
        yield requests.Response()
        yield requests.PreparedRequest()
        yield requests.Response()
        yield requests.PreparedRequest()
        yield requests.Response()
        yield requests.PreparedRequest()
        yield requests.Response()

    def mock_get_output_options():
        return False, False

    old_collect_messages = httpie.client.collect_messages
    httpie.client.collect_messages = mock_collect_messages
    old_get_output_options = httpie.cli.program.get_output_options
    httpie.cli.program.get_output_options = mock_get_output_options
    res = program(args=argparse.Namespace(), env=Environment())
    assert res == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:08.139349
# Unit test for function program
def test_program():
    pass

# Generated at 2022-06-13 21:42:36.205135
# Unit test for function main
def test_main():
    from httpie.compat import is_windows
    from httpie.context import Environment

    def invoke(args, env, exit_status):
        assert main(args=args, env=env) == exit_status

    env = Environment()
    env.config.default_options = ['--ignore-stdin']
    env.debug = False

    if is_windows:
        invoke(args=['http'], env=env, exit_status=ExitStatus.ERROR)

    invoke(args=['http', '--debug'], env=env, exit_status=ExitStatus.SUCCESS)
    invoke(args=['http', '--traceback'], env=env, exit_status=ExitStatus.ERROR)

# Generated at 2022-06-13 21:42:45.739891
# Unit test for function program
def test_program():
    import os
    import httpie
    from httpie.cli.definition import parser
    from httpie.context import Environment
    path = os.path.join(httpie.__path__[0], 'tests', 'samples', 'headers.json')
    args = parser.parse_args(['--body', path, 'http://httpbin.org/post'])
    exit_status = program(args=args, env=Environment())

    assert exit_status == ExitStatus.SUCCESS
    # TODO: Add actual test code.


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:43:00.534580
# Unit test for function program
def test_program():
    from httpie import __version__ as httpie_version
    from httpie.cli.definition import parser
    from httpie.client import collect_messages
    from httpie.output.curl import write_message
    from httpie.plugins.registry import plugin_manager
    from httpie.status import ExitStatus, http_status_to_exit_status
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie import ExitStatus
    from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD

    def _main(args: List[Union[str, bytes]] = sys.argv, env=Environment()) -> ExitStatus:
        program_name, *args = args
        env.program_name = os.path.bas

# Generated at 2022-06-13 21:43:01.497805
# Unit test for function program
def test_program():
	pass
	#print(program)

# Generated at 2022-06-13 21:43:04.185970
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args()
    status = program(args=args,  env='Environment')

    assert isinstance(status, int)

# Generated at 2022-06-13 21:43:14.240385
# Unit test for function main
def test_main():
    from httpie.cli.constants import DEFAULT_CONFIG_DIR
    exit_status = main([
        'http',
        '--ignore-stdin',
        '--headers',
        'key:val',
        '--form',
        'foo=bar',
        '--timeout', '0.001',
        '--output', os.devnull,
        '--debug',
        'get',
        'http://httpbin.org/headers',
    ])
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:43:17.103829
# Unit test for function program
def test_program():
    args = "http https://httpbin.org/get".split()
    res = program(args)
    assert res == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:29.923084
# Unit test for function program

# Generated at 2022-06-13 21:43:32.459915
# Unit test for function program
def test_program():
    """
    Test function program
    """
    args = []
    env = Environment()
    print (program(args,env))

# Generated at 2022-06-13 21:43:41.153215
# Unit test for function program
def test_program():
    from httpie.cli.parser import parser, parse_formatted_key_value

    args = parser.parse_args(
        args=decode_raw_args([
            '--form',
            'testA=1,testB=2'
        ],
        'UTF-8'),
        env=Environment()
    )

    assert args.form == parse_formatted_key_value(
        s=args.form,
        key_value_sep=b',',
        item_sep=b'=',
        error_message='must be a comma-separated list of key=value pairs'
    )


if __name__ == '__main__':  # pragma: no cover
    # Unit tests for function main
    def func(a, b=2, c=3):
        return a, b, c


# Generated at 2022-06-13 21:44:03.787836
# Unit test for function program
def test_program():
    exit_status = program(args=['https://www.github.com'], env=Environment())
    assert(exit_status == ExitStatus.SUCCESS)

# Generated at 2022-06-13 21:44:11.359985
# Unit test for function program
def test_program():
    from httpie.cli import parse_items

    class Args(argparse.Namespace):
        def __init__(self):
            self.headers = []
            self.output_options = []
            self.output_file = None
            self.output_file_specified = False
            self.output_file_mode = None
            self.follow = False

    args = Args()
    args.headers = parse_items(['X-API-Token:42'])

    class Env(Environment):
        def __init__(self):
            self.stdin = '{"foo": "bar"}'
            self.stdin_isatty = False
            self.stdout_isatty = False

    program(args, Env())

# Generated at 2022-06-13 21:44:22.089444
# Unit test for function program
def test_program():
    import argparse
    env = Environment()
    args = argparse.Namespace(method='GET', url='httpbin.org/get',
                              headers=[], output_options=['all'],
                              output_file=None, output_file_specified=False,
                              proxies=None, auth_plugin=None, auth=None,
                              download=None, download_resume=True,
                              timeout=None, verify=True,
                              cert=None,
                              max_redirects=None,
                              follow=None,
                              config_dir=None,
                              env=env,
                              )
    print(program(args, env))


if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:44:22.717957
# Unit test for function program
def test_program():
    pass


# Generated at 2022-06-13 21:44:27.968062
# Unit test for function main
def test_main():
    program_name = 'http'
    args = [
        '--debug', '--follow',
        '--form', 'username=John', 'password=secret',
        '--output', './out.file',
        'httpbin.org/post'
    ]

    try:
        main(args=[program_name] + args)
    except Exception:
        raise
    finally:
        os.remove('out.file')

# Generated at 2022-06-13 21:44:29.777760
# Unit test for function main
def test_main():
    args = sys.argv
    assert main(args) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:37.337446
# Unit test for function program
def test_program():
    from . import test_root
    from .context import Environment
    from .parse import parse_args
    from .downloads import TestDownloadStatus
    from .output.streams import NullFile

    env = Environment()
    env.stdout = NullFile()
    args = parse_args(args=['--debug'], env=env)
    program(env=env, args=args)
    print_debug_info(env)

    env = Environment()
    env.stdout = NullFile()
    args = parse_args(args=[], env=env)
    program(env=env, args=args)

    env = Environment()
    env.stdout = NullFile()
    args = parse_args(args=['--output', 'json', 'GET', 'https://httpbin.org/get'], env=env)

# Generated at 2022-06-13 21:44:38.660698
# Unit test for function main
def test_main():
    assert main() == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:42.413680
# Unit test for function program
def test_program():
    from httpie.cli import parser

    args = parser.parse_args(
        args=['https://httpbin.org/get'],
        env=Environment(),
    )
    program(args=args, env=Environment())

# Generated at 2022-06-13 21:44:44.944008
# Unit test for function program
def test_program():
    exit_status = main()
    assert exit_status == ExitStatus.SUCCESS

if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:45:39.738713
# Unit test for function program

# Generated at 2022-06-13 21:45:51.200346
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args('http google.com/'.split())
    assert program(args,Environment())==0
    args = parser.parse_args('http post google.com/'.split())
    assert program(args,Environment())==0
    args = parser.parse_args('http post google.com/ -f name=kishan'.split())
    assert program(args,Environment())==0
    args = parser.parse_args('http post google.com/ -f name=kishan -f email=kishan23@iitk.ac.in'.split())
    assert program(args,Environment())==0
    args = parser.parse_args('http post google.com/ -i'.split())
    assert program(args,Environment())==0

# Generated at 2022-06-13 21:46:03.122770
# Unit test for function program
def test_program():
    env = Environment(
        outfile=sys.stdout,
        errfile=sys.stderr,
        stdin=sys.stdin,
        stdin_isatty=sys.stdin.isatty(),
        stdout_isatty=sys.stdout.isatty(),
        stderr_isatty=sys.stderr.isatty(),
    )
    program(
        args=['/home/yi/PycharmProjects/httpie/venv/bin/httpie', '--check-status', '--download', 'https://httpbin.org/get'],
        env=env,
    )

# Generated at 2022-06-13 21:46:06.409012
# Unit test for function main
def test_main():
    # TODO: Re-enable and improve test.
    return
    status_code = main(['--debug'])
    assert status_code == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:18.790597
# Unit test for function program
def test_program():
    assert ExitStatus.ERROR == main(args=["hello.py", "http://httpbin.org/ip"])
    assert ExitStatus.ERROR == main(args=["hello.py", "http://httpbin.org/status/400"])
    assert ExitStatus.ERROR == main(args=["hello.py", "http://httpbin.org/status/404"])
    assert ExitStatus.ERROR == main(args=["hello.py", "http://httpbin.org/status/500"])
    assert ExitStatus.ERROR == main(args=["hello.py", "http://httpbin.org/delay/10"])
    assert ExitStatus.ERROR_TIMEOUT == main(args=["hello.py", "http://httpbin.org/delay/10", "--timeout=1"])

# Generated at 2022-06-13 21:46:28.956870
# Unit test for function program
def test_program():
    import io
    import sys

    from contextlib import redirect_stderr
    from httpie.cli.constants import DEFAULT_CONFIG_DIR
    from httpie.cli.definition import get_parser

    stdin = io.BytesIO()
    stdin.buffer.write(b'{"name":"value"}')
    stdin.buffer.seek(0)

    stdout = io.BytesIO()
    with redirect_stderr(stdout):
        parser = get_parser()
        args = parser.parse_args(['--json', '--verbose', '--pretty=all', 'httpbin.org/post'],
                                                                           env={'stdin': stdin, 'stdout': stdout,
                                                                                'config_dir': DEFAULT_CONFIG_DIR})

# Generated at 2022-06-13 21:46:32.431168
# Unit test for function program
def test_program():
    program(["https://requestb.in/1cabh3q1", "-v", "-d", "a=b", "-H", "Content-Type: application/json"], Environment())

if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:46:33.989625
# Unit test for function program
def test_program():
    assert program(['--follow'], Environment()) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:39.586077
# Unit test for function program
def test_program():
    import unittest

    class TestProgram(unittest.TestCase):

        def test_program_error(self):
            # testing on a valid args
            args = "test"
            env = "env"
            # this should not raise the exception
            self.assertEqual(program(args, env), ExitStatus.ERROR)

    unittest.main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:46:52.297861
# Unit test for function main
def test_main():
    # Test program
    class CliTestEnvironment(Environment):
        def __init__(self, args):
            self.args = args
            self.program_name = "test_program"
            self.stdin = "stdin"
            self.stdin_encoding = 'UTF-8'
            self.stdout = "stdout"
            self.stderr = "stderr"
            self.stdout_isatty = True

    # Successful finish
    assert main(['test_program'], CliTestEnvironment(['test_program'])) == ExitStatus.SUCCESS
    # Wrong argument
    assert main(['test_program', '--wrong-argument'], CliTestEnvironment(['test_program', '--wrong-argument'])) == ExitStatus.ERROR
    # Exception