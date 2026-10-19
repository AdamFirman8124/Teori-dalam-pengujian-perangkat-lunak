

# Generated at 2022-06-13 21:40:52.351391
# Unit test for function program
def test_program():
    assert program(args = ['httpie.org'], env = Environment()) == 0

# Generated at 2022-06-13 21:40:56.160179
# Unit test for function main
def test_main():
    env = Environment()
    assert main(env=env)
    assert main(env=env, args='--debug'.split())
    assert main(env=env, args='--debug --verbose'.split())

# Generated at 2022-06-13 21:41:05.130332
# Unit test for function main
def test_main():
    def check_main_status(args, expected_status):
        status = main(args=args + ['httpbin.org/status/200'],
                      env=Environment(stdin=io.StringIO('a\nb\nc\n'),
                                      stdin_isatty=False))
        assert status == expected_status, status

    def check_main_stderr(args, expected_stderr):
        env = Environment(stderr=io.StringIO())
        main(args=args + ['httpbin.org/status/200'], env=env)
        actual_stderr = env.stderr.getvalue()
        assert actual_stderr == expected_stderr, actual_stderr

    # Successful invocation.
    check_main_status(args=[], expected_status=0)

   

# Generated at 2022-06-13 21:41:07.136112
# Unit test for function program
def test_program():
    pass;


# Generated at 2022-06-13 21:41:15.839019
# Unit test for function main
def test_main():
    from io import StringIO
    def run_main(*argv):
        sio = StringIO()
        try:
            with redirect_stdout(sio):
                main(argv)
        except SystemExit as e:
            exit_status = e.code
        else:
            exit_status = ExitStatus.SUCCESS
        return exit_status, sio.getvalue()

    assert run_main() == (ExitStatus.SUCCESS, '')

    assert run_main('http') == (ExitStatus.ERROR, '')

# Generated at 2022-06-13 21:41:27.957999
# Unit test for function main
def test_main():
    assert main(args=['--version']) == ExitStatus.SUCCESS
    assert main(args=['--traceback', '--help']) == ExitStatus.SUCCESS
    assert main(args=['--debug']) == ExitStatus.SUCCESS
    assert main(args=['--debug', '--help']) == ExitStatus.SUCCESS
    assert main(args=['--debug', '--version']) == ExitStatus.SUCCESS
    assert main(args=['--debug', '--traceback', '--help']) == ExitStatus.SUCCESS
    assert main(args=['--debug', '--traceback', '--version']) == ExitStatus.SUCCESS



# Generated at 2022-06-13 21:41:36.354780
# Unit test for function program
def test_program():
    from argparse import Namespace
    from httpie.cli.parser import parser
    class Env:
        def __init__(self):
            self.config = config()
            self.stdout = sys.stdout
            self.stderr = sys.stderr
            retur

        def log_error(self, msg, level=None):
            print(msg, file=self.stderr)
            return
        def log(self, msg, level=None):
            print(msg, file=self.stdout)
            return
    def config():
        class config:
            def __init__(self):
                self.default_options = []
                self.options = {'verbose': True}
                self.directory = os.path.dirname(os.path.abspath(__file__))
                self

# Generated at 2022-06-13 21:41:40.492797
# Unit test for function program
def test_program():
    print(program(['', 'http://httpbin.org/get']))
    assert program(['', 'http://httpbin.org/get']) == 'SUCCESS'



# Generated at 2022-06-13 21:41:42.530442
# Unit test for function main
def test_main():
    assert main([]) == ExitStatus.ERROR


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:41:58.249699
# Unit test for function program
def test_program():
    env = Environment()
    args_obj = argparse.Namespace(
        check_status = False,
        download = False,
        download_resume = False,
        follow = False,
        output_file = None,
        output_file_specified = None,
        output_options = [OUT_RESP_BODY],
        quiet = False,
        timeout = 30
    )
    assert program(args_obj, env) == ExitStatus.SUCCESS

    args_obj = argparse.Namespace(
        check_status = True,
        download = False,
        download_resume = False,
        follow = False,
        output_file = None,
        output_file_specified = None,
        output_options = [OUT_RESP_BODY],
        quiet = False,
        timeout = 30
    )

# Generated at 2022-06-13 21:42:28.797600
# Unit test for function program
def test_program():
    a = ['http', '--download', '--check-status', 'http://httpbin.org/get']
    print(program(argparse.Namespace(a), Environment()))

# Generated at 2022-06-13 21:42:36.108868
# Unit test for function program
def test_program():
    args = argparse.Namespace()
    args.output_options = [OUT_REQ_BODY, OUT_RESP_BODY]
    args.download = False
    args.output_file = None
    args.output_file_specified = False
    args.headers = None
    args.download_resume = False
    args.follow = False
    args.check_status = False
    args.quiet = False
    env = Environment()
    env.config.directory = os.path.expanduser('~/.httpie')
    env.config.config_file = os.path.expanduser('~/.httpie/config.json')
    env.config.default_options = ['--headers']
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env.stdin

# Generated at 2022-06-13 21:42:49.615291
# Unit test for function program
def test_program():
    class TestEnvironment():
        def __init__(self):
            self.parser = argparse.ArgumentParser()
            self.parser.add_argument('--b', nargs=1)
            self.parser.add_argument('--c', nargs=1, action='append')
            self.parser.add_argument('--d', nargs=1, action='append', default=[])
            self.parser.add_argument('-e', action='append')

            self.args = self.parser.parse_args('--b b --c c --c cc -e e1 -e e2'.split())
            self.args.output_options = ['d']
            
            self.config = self
            self.directory = None
            self.default_options = []
            self.default_options_overrides = []


# Generated at 2022-06-13 21:42:55.615757
# Unit test for function program
def test_program():
    import httpie.cli.constants
    import httpie.output.streams
    import pygments.util
    import re
    import requests.exceptions
    import urllib3
    import httpie.status
    import io
    import tempfile
    import httpie.cli.argtypes
    from httpie.input import ParseError
    from httpie.cli.definition import parser
    from httpie.core import main
    return program(parser.parse_args(['https://httpbin.org/get']), Environment())


# Generated at 2022-06-13 21:42:57.077090
# Unit test for function program
def test_program():
    status = program([], None)
    # TODO: Unit test

# Generated at 2022-06-13 21:43:04.366629
# Unit test for function main
def test_main():
    assert main(['--version']) == ExitStatus.SUCCESS
    assert main(['--help']) == ExitStatus.SUCCESS
    assert main([]) == ExitStatus.ERROR
    assert main(['httpie']) == ExitStatus.ERROR
    assert main(['httpie', 'get']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:12.246088
# Unit test for function program
def test_program():
    print("Unit test for function program")
    import argparse
    args = argparse.Namespace()
    args.output_options = "json"
    args.output = ""
    args.check_status = ""
    args.quiet = ""
    args.follow = ""
    args.download = ""
    args.output_file = ""
    args.output_file_specified = ""
    env = Environment()
    program(args=args, env=env)
    return


if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:43:24.878590
# Unit test for function program
def test_program():
    from httpie.context import Environment
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.parser import parser

    # Test with file
    content = 'Hello World'
    with open('tmp.txt', 'w') as f:
        f.write(content)
    args = parser.parse_args(['--output-file=tmp.txt', '-v', 'GET', 'httpbin.org/get'])
    program(args=args, env=Environment())

    with open('tmp.txt', 'r') as f:
        text = f.read()
    assert content in text

    # Test without file
    content = 'Hello World'
    with open('tmp.txt', 'w') as f:
        f.write(content)

# Generated at 2022-06-13 21:43:29.795339
# Unit test for function main
def test_main():
    class myclass:
        exit_status = 0
        def write(self,*arg):
            print(arg)
    class myclass1:
        pass
    sys.argv = ['http']
    args = sys.argv
    env = myclass1()
    env.stderr = myclass()
    sys.exit = myclass()
    main(args=args,env=env)

# Generated at 2022-06-13 21:43:39.640238
# Unit test for function main
def test_main():
    """
    Testing the main function

    """
    def fake_program(args: argparse.Namespace, env: Environment) -> ExitStatus:
        """
        Fake program to test the main function.

        """
        if args.url == 'http://www.google.com':
            return ExitStatus.SUCCESS
        elif args.url == 'http://www.google.com/fail':
            return ExitStatus.ERROR
        else:
            return ExitStatus.ERROR_BAD_URL

    try:
        import io
    except ImportError:
        from io import StringIO as io
    import sys
    from httpie.context import Environment
    from httpie.cli.constants import DEFAULT_UA

    success_args = ['--verbose', 'http://www.google.com']

# Generated at 2022-06-13 21:45:37.010236
# Unit test for function program
def test_program():
    from httpie.client import Client
    from httpie.output.streams import UnsupportedOutputStream
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPHeaders
    from httpie.plugins import registry


# Generated at 2022-06-13 21:45:38.048704
# Unit test for function program
def test_program():
    pass
    #print(program(args, env))

# Generated at 2022-06-13 21:45:51.679848
# Unit test for function program
def test_program():
    import pytest
    from httpie.client import collect_messages
    from httpie.config import Config
    from httpie.output.streams import StdoutBytesIO
    from httpie.output.writer import RequestBodyWriteError
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth
    from httpie.status import ExitStatus
    from httpie.utils import get_response_as_json
    url = 'http://httpbin.org/headers'
    args = parse_args(['--form', 'POST', url], env=Environment())
    args.follow = True
    args.output_options = [OUT_REQ_HEAD]
    args.config = Config(root_dir=None, defaults={'default_options': []})
    args.config.default_options = []

# Generated at 2022-06-13 21:45:53.777690
# Unit test for function main
def test_main():
    import httpie.cli.definition as cli
    cli.parser.parse_args(['--download','http://localhost:8080/ping'])

# Generated at 2022-06-13 21:46:06.287105
# Unit test for function program
def test_program():
    # setup
    args = argparse.ArgumentParser()

    # create empty class
    class Empty:
        # populate class with the __init__ function and specified parameters
        def __init__(self, exit_status, stdout, stderr):
            self.exit_status = exit_status
            self.stdout = stdout
            self.stderr = stderr

    # populate class
    env = Empty(ExitStatus.SUCCESS, stdout=[], stderr=[])

    # run program with mock values
    assert(program(args, env) == ExitStatus.SUCCESS)

    # cleanup
    args, env = None, None

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:46:11.856643
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile

    from click.testing import CliRunner

    # Prepare an empty dir
    tmp = tempfile.mkdtemp()
    old_cwd = os.getcwd()
    os.chdir(tmp)
    
    # Clean up
    def cleanup():
        os.chdir(old_cwd)
        shutil.rmtree(tmp)

    def _test_main():
        runner = CliRunner()
        result = runner.invoke(main, '--debug')
        assert result.exit_code == 0
        assert 'HTTPie' in result.output
    
    try:
        _test_main()
    finally:
        cleanup()

# Generated at 2022-06-13 21:46:23.492596
# Unit test for function program
def test_program():
    from pygments import __version__ as pygments_version
    from httpie import __version__ as httpie_version
    from requests import __version__ as requests_version
    import sys
    program_name, *args = sys.argv
    args = decode_raw_args(args)
    program_name, *args = sys.argv
    exit_status = main(args=[program_name, '--debug'])
    assert exit_status == ExitStatus.SUCCESS
    exit_status = main(args=[program_name, '--traceback', '--download', 'google.com'])
    assert exit_status == ExitStatus.SUCCESS
    exit_status = main(args=[program_name, '--debug', '--download', 'google.com'])
    assert exit_status == ExitStatus.SUCCESS
    exit

# Generated at 2022-06-13 21:46:26.166141
# Unit test for function program
def test_program():
    args = ['http', '--verbose', 'https://httpie.org']
    env = Environment()
    assert program(args, env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:31.028055
# Unit test for function main
def test_main():
    assert ExitStatus.SUCCESS == main(['http', '--debug'])
    assert ExitStatus.ERROR == main(['http', '--debug', '--output-options', 'xxx'])
    assert ExitStatus.ERROR == main(['http', '--debug', 'xxx'])


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:46:34.422789
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args('GET http://httpbin.org/'.split())
    env = Environment()
    program(args, env)

# Helper function to set the environment

# Generated at 2022-06-13 21:47:06.717208
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser, args_to_ui_args
    from httpie.config import Config
    from httpie.context import Environment
    import os, sys
    ui = parser.parse_args(
        args=['https://httpie.org'],
        env=Environment(
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr,
            config=Config(directory=os.getcwd())
        )
    )
    program(args=ui, env=Environment())

# Generated at 2022-06-13 21:47:10.601559
# Unit test for function program
def test_program():
    """
    Unit test for function program.

    """
    assert program(args=argparse.Namespace(), env=Environment()) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:47:19.152346
# Unit test for function main
def test_main():
    import httpie.cli.argtypes  # noqa
    import httpie.cli.constants  # noqa
    import httpie.cli.definition  # noqa
    import httpie.cli.parser  # noqa
    import httpie.cli.shell  # noqa
    import httpie.cli.utils  # noqa
    import httpie.compat  # noqa
    import httpie.config  # noqa
    import httpie.context  # noqa
    import httpie.downloads  # noqa
    import httpie.output  # noqa
    import httpie.plugins  # noqa
    import httpie.status  # noqa
    import httpie.utils  # noqa
    sys.modules['httpie.cli.argtypes'] = httpie.cli.argtypes

# Generated at 2022-06-13 21:47:35.683833
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch

    from httpie.cli.constants import DEFAULT_PRESET
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.plugins import plugin_manager

    plugin_manager.clear()
    output = StringIO()
    with patch.object(Environment, 'stdout', output):
        env = Environment()
        conf = Config(env=env, config_dir=env.config.directory)
        conf.default_options = ['--no-stream']
        args = [
            '--headers',
            '--style=colorful',
            '--user=seb',
        ] + DEFAULT_PRESET + [
            'https://httpie.org/headers',
        ]

# Generated at 2022-06-13 21:47:41.686353
# Unit test for function program
def test_program():
    args = argparse.Namespace(download=False,download_resume=False,follow=False,headers="",method="GET",output_file=None,output_file_specified=None,output_options=[],quiet=False,timeout=None,verbose=0,verify=True,max_redirects=None,check_status=True)
    env = Environment()
    assert program(args=args,env=env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:54.596166
# Unit test for function main
def test_main():
    assert main(['http', '--verbose', 'https://httpbin.org/get']) == ExitStatus.SUCCESS
    assert main(['http', 'https://httpbin.org/status/404']) == ExitStatus.ERROR_HTTP_3XX
    assert main(['http', '--traceback', 'https://httpbin.org/status/404']) == ExitStatus.ERROR
    assert main(['http', '--traceback', 'https://httpbin.org/get']) == ExitStatus.SUCCESS
    assert main(['http', '--debug', 'https://httpbin.org/get']) == ExitStatus.SUCCESS
    assert main([sys.executable, 'httpie/__main__.py',  '--debug']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:58.992171
# Unit test for function program
def test_program():
    a = [ 'httpie', 'post', 'http://httpbin.org/post' ]
    env = Environment()
    b = main(a,env)
    print(b)

if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:48:00.339563
# Unit test for function program
def test_program():
    assert program(args=['--debug'], env=Environment()) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:48:02.483872
# Unit test for function program
def test_program():
    #args = argparse.Namespace(
    #    arg_parsed,
    #    stream = sys.stdin
    #)
    pass

# Generated at 2022-06-13 21:48:08.089688
# Unit test for function main
def test_main():
    # sys.argv[0] = __file__
    args = ['httpie', '--help']
    exit_status = main(args)
    assert exit_status == ExitStatus.SUCCESS
    args = ['httpie', '--version']
    exit_status = main(args)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:28.435568
# Unit test for function program
def test_program():
    from httpie.cli.constants import DEFAULT_OPTIONS
    from httpie.cli.definition import parser
    from httpie.cli.utils import get_ui_colors
    from httpie.compat import str
    from httpie.config import Config
    from httpie.output.streams import FileLikeStream
    from httpie.plugins import builtin_plugins
    from httpie.plugins.manager import PluginManager

    class DebugEnvironment(Environment):
        def __init__(self):
            super().__init__()
            self.debug = True
            self.is_windows = False
            self.config = Config(directory="/home/sugar")
            self.stdin = FileLikeStream(isatty=True)
            self.stdout = FileLikeStream(isatty=True)
            self.stderr = File

# Generated at 2022-06-13 21:49:32.809566
# Unit test for function program
def test_program():
    args = parser.parse_args(
        args=[
            'https://httpbin.org/post',
            'name=DaYeon',
            '--headers',
            'Host: localhost'
        ],
        env=Environment(),
    )
    program(args, Environment())

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:49:34.042122
# Unit test for function program
def test_program():
    assert program(None, None) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:36.189943
# Unit test for function main
def test_main():
    args = ['--debug']
    main(args)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 21:49:46.090326
# Unit test for function program
def test_program():
    import sys
    from httpie.cli.context import Environment
    from httpie.cli.definition import parser
    
    env = Environment()
    args = sys.argv
    args = ["http", "--download", "--download-resume", "https://drive.google.com/uc?export=download&id=1pPnIwlsa_V0rABr_jXb7a0NjGr0d7fZH", "--output-file=httpie"]
    args = parser.parse_args(args=args, env=env)
    program(args, env)

if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:49:52.999308
# Unit test for function program
def test_program():
    import logging
    import os.path
    import tempfile


# Generated at 2022-06-13 21:50:00.793901
# Unit test for function program
def test_program():
    args: argparse.Namespace = argparse.Namespace()
    env: Environment = Environment()
    args.headers = {'Accept-Encoding': '', 'Accept': '*/*', 'User-Agent': 'curl/7.54.0'}
    args.method = 'GET'
    args.output_file = None
    args.output_file_specified = ''
    args.output_options = []
    args.output_options_specified = ''
    args.output_stream = 'None'
    args.output_stream_specified = ''
    args.output_stream_encoding = ''
    args.timeout = ''
    args.check_status = ''
    args.max_redirects = ''
    args.session = ''
    args.session_read = ''
    args.session_read_strict = ''

# Generated at 2022-06-13 21:50:12.667381
# Unit test for function main
def test_main():
    from pytest import raises
    from httpie.context import Environment

    def stdout_empty(stdout):
        return not stdout or stdout.getvalue() == ''

    env = Environment()
    env.config.directory = os.path.join(os.getcwd(), '.httpie')
    env.stdout = io.StringIO()
    env.stderr.error_log_file = io.StringIO()
    env.stderr.isatty = False
    env.stdin_encoding = 'utf-8'
    env.config.default_options = ['--traceback', '--debug']

    program_name, *args = 'http'.split()
    env.program_name = os.path.basename(program_name)

    # Check with --debug is the only argument