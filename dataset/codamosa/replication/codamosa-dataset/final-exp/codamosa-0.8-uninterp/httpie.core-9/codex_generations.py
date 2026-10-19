

# Generated at 2022-06-13 21:41:23.230031
# Unit test for function program
def test_program():
    exit_status = program(args=['--help'], env=Environment())
    assert exit_status in (
        ExitStatus.SUCCESS,
        ExitStatus.ERROR_CTRL_C,
        ExitStatus.ERROR_TIMEOUT,
        ExitStatus.ERROR_TOO_MANY_REDIRECTS,
    )
    assert exit_status != ExitStatus.ERROR

# Generated at 2022-06-13 21:41:27.111149
# Unit test for function program
def test_program():
    from httpie.cli.parser import parse_args
    prog_args = ['GET', 'https://httpbin.org/', 'key=val','-h']
    args = parse_args(args=prog_args)
    program(args=args,env=Environment())


# Generated at 2022-06-13 21:41:36.040591
# Unit test for function main
def test_main():
    import io
    import os
    import sys
    import tempfile
    from httpie.context import Environment
    from httpie import exit_status
    def get_empty_temp_dir():
        tempdir = tempfile.mkdtemp()
        os.rmdir(tempdir)
        return tempdir
    def get_temp_config_dir():
        tempdir = tempfile.mkdtemp()
        print(tempdir)
        os.mkdir(f"{tempdir}/http")
        directory = f"{tempdir}/http"
        os.mkdir(f"{directory}/config")
        return tempdir
    def get_args_output_options(args):
        env = Environment()
        env.config.directory = get_temp_config_dir()

# Generated at 2022-06-13 21:41:48.128077
# Unit test for function program

# Generated at 2022-06-13 21:41:51.113319
# Unit test for function main
def test_main():
    assert main(args=['--debug']) == 0
    assert main(args=['--debug', 'http://www.example.com/']) == 0
    assert main(args=['--traceback', 'http://www.example.com/']) == 0

# Generated at 2022-06-13 21:41:58.196141
# Unit test for function program
def test_program():
    from httpie import httpie
    from httpie.cli import args_stack
    from httpie.cli.parser import parser
    from httpie.plugins.registry import plugin_manager

    args_stack.clear()
    parser.clear_parsed_args()
    plugin_manager.clear_registered_plugins()
    args = httpie.cli.parser.parse_args(args=['--verbose', 'https://qiwihui.com/'])
    assert(program(args, Environment()))

# Generated at 2022-06-13 21:42:12.428917
# Unit test for function main
def test_main():
    assert main(['https://httpbin.org/post' , '-d' , '2' ,'json={a:1}' ]) ==0
    assert main(['https://httpbin.org/post' , '-d' , '2' ,'json={a:1,b:2}' ]) ==0
    assert main(['https://httpbin.org/post' , '-d' , '2' ,'data={a:1,b:2}' ]) ==0
    assert main(['https://httpbin.org/post' , '-d' , '2' ,'data=[1,2]' ]) ==0
    assert main(['https://httpbin.org/post' , '-d' , '2' ,'json=[1,2]' ]) ==0

# Generated at 2022-06-13 21:42:16.329162
# Unit test for function program
def test_program():
    import requests
    import pytest
    args = argparse.Namespace(headers='Accept: text/html')
    exit_status=program(args, Environment())
    assert exit_status==ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:25.404940
# Unit test for function main
def test_main():
    from httpie.context import Environment
    from httpie.output.streams import get_default_streams
    from httpie import cli
    from io import StringIO
    from httpie.downloads import Downloader
    from httpie.plugins.registry import plugin_manager

    env = Environment(
        stdin=StringIO('abc'),
        stdin_isatty=False,
        config_dir=None,
        stdout=StringIO(),
        stderr=StringIO(),
        stdout_isatty=False,
        stdin_encoding='utf8',
        stdout_encoding='utf8',
        stderr_encoding='utf8',
        is_windows=(platform.system() == 'Windows'),
        is_mac=(platform.system() == 'Darwin'),
    )
    env = env

# Generated at 2022-06-13 21:42:34.594705
# Unit test for function program
def test_program():
    import io
    import os
    import shutil
    import tempfile
    import unittest
    import httpie
    from httpie.cli import parser
    from httpie import ExitStatus
    from httpie.plugins.builtin import (
        HTTPBasicAuth,
        HTTPDigestAuth,
        HTTPHeader,
        HTTPProxyAuth,
    )

    class ProgramTest(unittest.TestCase):
        def setUp(self):
            self.temp_directory = tempfile.mkdtemp()
            self.config_dir = os.path.join(self.temp_directory, '.config', 'httpie')
            os.makedirs(self.config_dir)
            self.config_path = os.path.join(self.config_dir, 'config.json')

# Generated at 2022-06-13 21:45:08.090562
# Unit test for function main
def test_main():
    main(['hello', 'world'])

# Generated at 2022-06-13 21:45:18.481859
# Unit test for function program
def test_program():
    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)
    from httpie.cli.definition import parser
    from httpie.config import Environment, Config
    from httpie.output.streams import StdoutBytesIO
    from httpie.status import ExitStatus, http_status_to_exit_status
    from httpie.downloads import Downloader
    env = Environment()
    env.stdin = None
    env.stdout = StdoutBytesIO()
    env.stderr = StdoutBytesIO()
    parser.parse_args(['--download', '-L', 'https://httpbin.org/delay/5', '--timeout', '1', '--max-redirects', '5'], env=env)


# Generated at 2022-06-13 21:45:23.554436
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args = parser.parse_args(
        [
            '--headers',
            'Content-Type: application/json',
            'http://example.com/',
            'k1=v1',
            'k2=v2',
            'k3=',
            'k4'
        ]
    )
    args.follow = True  # --download implies --follow.
    downloader = Downloader(output_file=args.output_file, progress_file=sys.stderr, resume=args.download_resume)
    
    # 参数化测试
    class Test:
        def __init__(self):
            self.status_code = 309
            

# Generated at 2022-06-13 21:45:27.053645
# Unit test for function main
def test_main():
    # Initialization

    # Execution

    # Verification

    pass  # if we got here then the test passed

# Generated at 2022-06-13 21:45:30.202381
# Unit test for function program
def test_program():
    program(args=['--help'])

if __name__ == '__main__':
    try:
        exit(main())
    except Exception as e:
        raise e
        exit(1)

# Generated at 2022-06-13 21:45:32.270833
# Unit test for function main
def test_main():
    exit_status = main()
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:36.180776
# Unit test for function program
def test_program():
    env = Environment()
    assert main(program_name='', args=[], env=env) == ExitStatus.SUCCESS
    assert env.stdout._buffer.getvalue() == ''

# Generated at 2022-06-13 21:45:38.905991
# Unit test for function program
def test_program():
    exit_status = program()
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:45:45.694485
# Unit test for function main
def test_main():
    from io import StringIO
    import sys

    sys.argv = ['/usr/local/bin/http', 'www.google.com']
    sys.stdin = StringIO('')
    sys.stdout = StringIO('')
    sys.stderr = StringIO('')
    exit_status = main()


# Generated at 2022-06-13 21:45:50.835860
# Unit test for function program
def test_program():
    # Example 1
    def program(args: argparse.Namespace, env: Environment) -> ExitStatus:
        return ExitStatus.SUCCESS

    assert program(argparse.Namespace(), Environment()) == ExitStatus.SUCCESS
    # Example 2
    def program(args: argparse.Namespace, env: Environment) -> ExitStatus:
        return ExitStatus.ERROR
    assert program(argparse.Namespace(), Environment()) == ExitStatus.ERROR


# Generated at 2022-06-13 21:46:58.503224
# Unit test for function program
def test_program():
    assert program(args=None, env=None) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:00.055190
# Unit test for function program
def test_program():
    """
    Test for program.
    """
    print(program())

# Generated at 2022-06-13 21:47:14.130160
# Unit test for function program
def test_program():
    from click.testing import CliRunner
    from httpie.cli import cli
    import tempfile

    test_file_path = './test-tmp-file'
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        test_file_path = temp_file.name
    test_args = [
        '--download',
        '--output-file={}'.format(test_file_path),
        'httpbin.org/get', '--json',
    ]

    runner = CliRunner()
    r = runner.invoke(cli.main, test_args)
    assert 200 == r.exit_code


# Generated at 2022-06-13 21:47:26.500039
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.security import get_auth
    from httpie.help import Help
    from httpie.config import Config
    from httpie.output.streams import Stream, StdoutBytesIO, StderrBytesIO
    from httpie.streams import RawRequestBytesIO, RawResponseBytesIO
    from httpie.status import ExitStatus
    from httpie.downloads import Downloader
    import requests
    import pytest
    import os
    import platform
    import sys
    import traceback

    args = parser.parse_args(args = ['--help'])
    config = Config(args=args)
    help_ = Help(args=args, config=config)
    auth = get_auth(args = args, config = config)
    verbose = 0
    debug = True
   

# Generated at 2022-06-13 21:47:37.386032
# Unit test for function program
def test_program():
    from httpie.cli.args import parse_args
    from httpie.cli.context import Environment
    import os
    import json
    import httpie.output.formatters
    import httpie.output.streams
    import httpie.output.writers
    import httpie.input
    import httpie.cli.argtypes
    import httpie.context
    import httpie.plugins
    import httpie.downloads
    import httpie.status
    import httpie.compat
    import httpie.cli.definition
    import httpie.auth
    import httpie.plugins.manager
    import httpie.models
    import httpie.plugins.builtin.auth
    import httpie.plugins.builtin.downloads
    import httpie.plugins.builtin.format


# Generated at 2022-06-13 21:47:49.014436
# Unit test for function program
def test_program():
    def run(args, **kwargs):
        args = [''] + args
        import json
        import os
        import requests
        import sys
        import threading
        import time
        import urllib

        import httpie
        from httpie.context import Environment
        from httpie.plugins.registry import plugin_manager
        from httpie.tests import mock

        from httpie.cli.definition import parser
        from httpie.cli.parser import get_default_options
        from httpie.plugins import builtin


# Generated at 2022-06-13 21:48:00.001726
# Unit test for function program
def test_program():
    # Unit test --check-status with no error
    def test_program_exit_status_check_status():
        class FakeNamespace():
            def __init__(self, check_status):
                self.check_status = check_status
            check_status = True
            follow = False
            output_options = ["all"]
            headers = ""
            output_file = None
            def get_param(self, param):
                return param
        
        class FakeEnvironment():
            def __init__(self, stdout_isatty, stdout):
                self.stdout_isatty = stdout_isatty
                self.stdout = stdout
            def log_error(self, error, level):
                pass
            stdout_isatty = False
            stdout = ""


# Generated at 2022-06-13 21:48:05.040779
# Unit test for function main
def test_main():
    from httpie.cli.runner import main
    from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
    from httpie import cli
    # cli.parser.add_argument('--output-options', type=str, help="Set output options", default='')
    args = ['--output-options', OUT_REQ_BODY + ',' + OUT_REQ_HEAD + ',' + OUT_RESP_BODY + ',' + OUT_RESP_HEAD,
            '--debug',
            '--download',
            'http://127.0.0.1:8000/api/toc/',
            '-H',
            'Authorization:aaadfsadfsdafsadfsafsd']
    # main

# Generated at 2022-06-13 21:48:06.621295
# Unit test for function main
def test_main():
    main(args = ['http', '--help'])

# Generated at 2022-06-13 21:48:12.388053
# Unit test for function program
def test_program():
    """
    Simple unit test for the function program
    """
    from httpie.cli.parser import get_parser

    parser = get_parser()
    args = parser.parse_args(['--ignore-stdin', 'https://httpbin.org/get'])
    assert program(args) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:38.643732
# Unit test for function main
def test_main():
    test_args = ['http']
    assert main(test_args) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:49.182017
# Unit test for function program
def test_program():
    from tempfile import mkstemp
    from httpie.cli.definition import parser
    from httpie.output.writer import write_message

    def program(args: argparse.Namespace, env: Environment):
        exit_status = ExitStatus.SUCCESS
        # test_request_body_read_callback
        request_body_read_callback = args.request_body_read_callback
        if request_body_read_callback:
            request_body_read_callback(b'xy')
        # test_output_options
        with_headers, with_body = get_output_options(args, requests.Response())
        assert with_headers == (OUT_RESP_HEAD in args.output_options)
        assert with_body == (OUT_RESP_BODY in args.output_options)
        # test_separator
       

# Generated at 2022-06-13 21:49:54.497809
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli.argtypes import KeyValue, KeyValueArgType

    args = program('httpie.org'.split(), Environment())
    assert args == 0, 'The environment can’t be created.'


# Generated at 2022-06-13 21:50:06.405995
# Unit test for function program
def test_program():
    def test_output(args):
        class Args():
            def __init__(self, args):
                super().__init__()
                self.args = args
            def __getattr__(self, item):
                return self.args.get(item)
        
        class Env():
            def __init__(self):
                super().__init__()
                self.stdout_isatty = False
            def log_error(self, *args):
                print(*args)
        
        args = Args(args)
        env = Env()
        program(args, env)

    # test_output({'args': ['-v', '--debug', '-j']})
    # test_output({'args': ['-v', '-b']})
    # test_output({'args': ['-v

# Generated at 2022-06-13 21:50:10.158481
# Unit test for function main
def test_main():
    args = ['--debug', '--traceback', 'GET', 'https://httpie.org/', 'User-Agent:test']
    assert main(args) == ExitStatus.SUCCESS