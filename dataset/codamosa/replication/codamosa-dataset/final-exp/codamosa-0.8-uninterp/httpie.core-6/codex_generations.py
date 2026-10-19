

# Generated at 2022-06-13 21:40:52.615171
# Unit test for function program
def test_program():
    import pytest
    from argparse import Namespace
    from httpie.cli.constants import DEFAULT_CONFIG_DIR

    env = Environment(
        config_dir=DEFAULT_CONFIG_DIR,
        # On Windows, the console may return CP_OEMCP, which is not compatible with `encode()`.
        stdin_encoding=sys.stdin.encoding or 'utf-8',
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    args = [
        '--headers',
        'Content-Type: application/json',
        'https://httpbin.org/post',
        'hello=world'
    ]

    # Test that program runs without any errors.

# Generated at 2022-06-13 21:41:02.759607
# Unit test for function main

# Generated at 2022-06-13 21:41:14.350951
# Unit test for function program
def test_program():
    import pytest
    from httpie.extendedargparser import ExtendedArgParser
    code1 = ['http', '--download', 'https://httpbin.org/get']
    code2 = ['http', '--download', '--download-resume', 'https://httpbin.org/get']
    code3 = ['http', '(https://httpbin.org/get)', 'name==value', '--form']
    code4 = ['http', 'httpbin.org/get', 'name==value', '--form', '--download', '--download-resume']
    code5 = ['http', 'httpbin.org/get', 'name==value', '--form', '--timeout=10']

# Generated at 2022-06-13 21:41:21.020001
# Unit test for function main
def test_main():
    import pytest
    # TODO: Use a mock environment.
    assert main(['httpie', '--help']) == ExitStatus.SUCCESS
    with pytest.raises(Exception):
        main(['httpie', '-d'])


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:41:29.524016
# Unit test for function program
def test_program():
    """
    Test if return value is as expected
    """
    args = argparse.Namespace(output_options="json", check_status=False, follow=True, download=False, download_resume=False, output_format=None, output_file=None, output_file_specified=False, headers=[], http2=False, ignore_stdin=False, max_redirects=None, method='GET', output_options_provided=True, output_style=None, timeout=None, verify=None, verify_tunnel=None, body_format=None, json=False, form=False, pretty=False, style=None, print_body=False, stream=False, style_provider=None, colors=256, colors_enabled=False, verbose=False, body=None, url='https://httpie.org/docs/')

   

# Generated at 2022-06-13 21:41:42.477005
# Unit test for function program
def test_program():
    from httpie.cli import httpie
    from httpie.context import Environment
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.registry import plugin_manager
    from httpie import ExitStatus
    from pipes import quote

    reload(sys)
    sys.setdefaultencoding('utf-8')

    args = parser.parse_args(
        args=['httpbin.org','get','/get','env','var','name','--follow','--body','--check-status','--download','--output','test.json','--auth','username:password','--proxy','http://10.10.10.10','--proxy-auth','username:password','--timeout','10','--max-redirects','10','--timeout','10','--max-redirects','10','--http2']
    )
    plugin_

# Generated at 2022-06-13 21:41:58.167989
# Unit test for function main
def test_main():
    import pytest
    args1 = ['test.py', 'https://www.google.com', '--cookies', '-C', 'Spam:Eggs']
    #args = ['test.py', '--debug']
    env = Environment()
    #args = ['test.py', 'https://google.com', '--traceback']
    #args = ['test.py', 'https://google.com', '--debug', '--traceback']
    #args = ['test.py', 'https://google.com', '--debug']
    status = main(args=args1, env=env)
    assert status == 0
    #assert status == ExitStatus.ERROR
    #assert status == ExitStatus.ERROR_CTRL_C
    #assert status == ExitStatus.ERROR_TIMEOUT
    #assert status == ExitStatus.ERROR_

# Generated at 2022-06-13 21:41:59.078693
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 21:42:12.696300
# Unit test for function program
def test_program():
    # Test program function with exit status 0
    import unittest
    from unittest import mock
    from httpie.context import Environment
    from httpie.cli.constants import OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
    from httpie.cli.parser import parse_args
    env = Environment()
    parsed_args = parse_args(args=['https://www.google.com/robots.txt'], env=env)
    program(parsed_args, env)
    # Test program function with exit status 0
    env = mock.Mock()
    parsed_args = mock.Mock()
    parsed_args.headers.return_value = {'testkey': 'testvalue'}

# Generated at 2022-06-13 21:42:23.822713
# Unit test for function program
def test_program():
    from io import TextIOBase
    from httpie.cli.parser import ParseResult
    from httpie.compat import CloseableMixin, isatty, string_types
    from httpie.utils import get_response_text
    import requests

    class MockEnvironment(object):
        class StderrMock(TextIOBase, CloseableMixin):
            def write(self, s):
                pass

            def writelines(self, lines):
                pass

        class StdoutMock(TextIOBase, CloseableMixin):
            def write(self, s):
                pass

            def writelines(self, lines):
                pass


# Generated at 2022-06-13 21:43:03.323798
# Unit test for function main
def test_main():
    import os

    pwd = os.getcwd()
    os.chdir(pwd+"/../..")

    args = ['--verbose', 'https://postman-echo.com/get']
    env = Environment()
    env.stdout = os.sys.stdout
    env.stderr = os.sys.stderr
    env.stdin = os.sys.stdin
    env.stdin_encoding = 'utf8'

    main(args, env)


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 21:43:08.852501
# Unit test for function program
def test_program():
    """
    Test for function program
    """
    import requests
    import httpie
    from httpie.cli.definition import parser

    def test_command_line_input(args: List[str]) -> int:
        exit_status = httpie.main(args=args)
        assert exit_status == http_status_to_exit_status(requests.codes.ok)

    test_command_line_input(args=[])
    test_command_line_input(args=['-V'])
    test_command_line_input(args=['--version'])


# Generated at 2022-06-13 21:43:09.593598
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 21:43:12.862915
# Unit test for function program
def test_program():
    args = []
    env = Environment()
    exit_status = program(args,env)
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:25.519926
# Unit test for function main
def test_main():
    class EnvStderrMock:
        text = ""
        def write(self, text):
            self.text += text

    env = Environment()
    env.program_name = "http"
    env.stderr = EnvStderrMock()

    class Args:
        def __init__(self):
            self.url = "https://www.google.com"
            self.stream = False
            self.method = "GET"
            self.headers = []
            self.timeout = 100
            self.max_redirects = 10
            self.output_file = "output_file"
            self.output_file_specified = True

    args = Args()

    assert main(args=[args], env=env) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:43:32.780352
# Unit test for function main
def test_main():
    def mock_program(args, env):
        return 123

    def mock_parser(args, env):
        class Mock:
            def parse_args(self, env, args):
                return args[1:]
        return Mock()

    # Test valid args
    assert main(['program_name'], None,
                program=mock_program,
                parser=mock_parser) == 123

    # Test no args
    assert main([], None,
                program=mock_program,
                parser=mock_parser) == 123

    # Test invalid args (exit status 1)
    assert main(['--invalid-arg'], None,
                program=mock_program,
                parser=mock_parser) == 1

    # Test Ctrl-C (exit status 130)

# Generated at 2022-06-13 21:43:36.680296
# Unit test for function main
def test_main():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.cli.parser import get_parser

    parser = get_parser()
    args = parser.parse_args(['--debug',
                              'GETT'
                              ])
    main(args)

# Generated at 2022-06-13 21:43:45.820072
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.client import collect_messages
    from httpie.context import Environment
    from httpie.downloads import Downloader
    from httpie.output.writer import write_message, write_stream, MESSAGE_SEPARATOR_BYTES
    import time
    import tempfile
    # env = Environment()
    # program_name = '/usr/bin/http'
    program_name, *args = ['/usr/bin/http']
    env = Environment()
    env.program_name = os.path.basename(program_name)
    args = decode_raw_args(args, env.stdin_encoding)
    # plugin_manager.load_installed_plugins()
    # if env.config.default_options:
    #     args = env.config.

# Generated at 2022-06-13 21:43:54.072054
# Unit test for function program
def test_program():
    import argparse
    class Args:
        def __init__(self, headers, download, output_file, output_file_specified, download_resume, output_options, follow, check_status, quiet):
            self.headers = headers
            self.download = download
            self.output_file = output_file
            self.output_file_specified = output_file_specified
            self.download_resume = download_resume
            self.output_options = output_options
            self.follow = follow
            self.check_status = check_status
            self.quiet = quiet
    input_arguments = Args(None, None, None, None, None, None, None, None, None)
    input_env = Environment()
    output_exit_status = program(input_arguments, input_env)
    assert output_

# Generated at 2022-06-13 21:43:55.245514
# Unit test for function program
def test_program():
    # TODO:
    pass

# Generated at 2022-06-13 21:45:03.994023
# Unit test for function main
def test_main():
    from .test.test_helper import Env
    import sys
    from httpie import __version__ as httpie_version
    from pygments import __version__ as pygments_version
    from requests import __version__ as requests_version

    # Version check
    sys.argv = ['http --debug']
    env = Env()
    result = main(env=env)
    env.stderr.seek(0)
    result1 = env.stderr.read()
    assert result == ExitStatus.SUCCESS
    assert ('HTTPie '+httpie_version+'\n'+'Requests '+requests_version+'\n'+'Pygments '+pygments_version in result1)
    # Debug check
    env = Env()

# Generated at 2022-06-13 21:45:05.559096
# Unit test for function main
def test_main():
    # TODO: Write unit test
    pass

# Generated at 2022-06-13 21:45:11.823081
# Unit test for function program
def test_program():
    mock = MagicMock(requests.Response)
    mock.status_code = 200
    mock.raw = None
    mock.headers = {}
    mock.body = 'abcdefg'
    mock.request.headers = {}
    mock.request.url = None
    mock.request.method = 'GET'
    mock.request.body = ''
    mock.request.is_body_upload_chunk = False
    def f(*args, **kwargs):
        yield mock
    mock.message.collect_messages = f
    mock.message.get_output_options = lambda *args: (True, True)
    mock.message.write_message = lambda *args, **kw: write_message(*args, **kw, requests_message=mock)
    mock.message.write_stream = write_stream
    mock.parser

# Generated at 2022-06-13 21:45:14.781314
# Unit test for function program
def test_program():
    args = '--download https://httpie.org/'.split(' ')
    env = Environment()
    program(args=args, env=env)

# Generated at 2022-06-13 21:45:21.596660
# Unit test for function program

# Generated at 2022-06-13 21:45:35.672935
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    from httpie.output.streams import ColorizedStdio
    from httpie.status import ExitStatus, http_status_to_exit_status
    from httpie.downloads import Downloader

    env = Environment(stdout=ColorizedStdio(), stderr=ColorizedStdio())

    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)

    args = parser.parse_args([])
    # No args
    try:
        program(args, env)
    except KeyboardInterrupt:
        env.stderr.write('\n')
        exit_status = ExitStatus.ERROR_CTRL_C

# Generated at 2022-06-13 21:45:45.012094
# Unit test for function main
def test_main():
    import sys

    def test_kwargs(**kwargs):
        sys.argv = ['http', 'www.baidu.com']
        main(env=Environment(**kwargs))

    test_kwargs()
    test_kwargs(stdin_isatty=False)
    test_kwargs(stdin_isatty=False, stdin_encoding='utf8', stdout_isatty=False)



# Generated at 2022-06-13 21:45:56.166156
# Unit test for function program
def test_program():
    import unittest
    import unittest.mock

    class FakeConfig(object):
        directory = None

    class FakeEnvironment(object):
        config = FakeConfig()
        stdout = unittest.mock.Mock()
        stderr = unittest.mock.Mock()

        def log_error(self, message, level):
            pass

        def stdout_isatty(self):
            return True

    class FakeNamespace(object):
        output_options = {OUT_REQ_HEAD, OUT_RESP_BODY}

    class FakeRequestsMessage(object):
        pass

    class FakePreparedRequest(FakeRequestsMessage):
        pass

    class FakeResponse(FakeRequestsMessage):
        pass

    class FakeDownloader(object):
        finished = True


# Generated at 2022-06-13 21:45:59.299907
# Unit test for function main
def test_main():
    assert main(['httpie', ' ']) == ExitStatus.ERROR

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:46:08.491183
# Unit test for function program
def test_program():
    import tempfile
    from httpie.cli.definition import parser, format_request_headers
    from httpie import ExitStatus, http

    file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8')
    program_name = 'http'
    args = ['http', 'https://www.google.com', '--output', file.name]
    parsed_args = parser.parse_args(args=args)
    exit_status = program(args=parsed_args, env=Environment())
    assert exit_status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:42.710977
# Unit test for function program
def test_program():
    import pytest
    # I have no idea why the pytest settings are not working
    import os
    os.environ["HTTPIE_CONFIG_DIR"] = "./config/"
    os.environ["HTTPIE_CONFIG_PATH"] = "./config/config"
    from . import funcs
    from . import funcs_test
    from httpie.cli.constants import OUT_REQ_HEAD,OUT_REQ_BODY,OUT_RESP_HEAD ,OUT_RESP_BODY
    os.environ["HTTPIE_OPTIONS"]=f"{OUT_REQ_HEAD} {OUT_REQ_BODY} {OUT_RESP_HEAD} {OUT_RESP_BODY}"
    #os.environ["HTTPIE_OPTIONS"]=f"--form"
    r = funcs

# Generated at 2022-06-13 21:47:54.167806
# Unit test for function program
def test_program():
    # empty request
    class MyNamespace:
        headers="Content-Type: application/json"
        output_options="req_head"
        quiet=False
        output_file=None
        output_file_specified=False
        download=False
        download_resume=False
        follow=False
        check_status=False
    class MyEnv:
        class Config:
            directory=None
        debuglevel=None
        log_level=None
        stderr=''
        stdout=''
        stdin=''
        colors = {}
    res = program(MyNamespace, MyEnv)
    assert res==0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:48:02.574644
# Unit test for function program
def test_program():
    class env:
        class stderr:
            def write(p):
                print(p)

    class config:
        class directory:
            def __init__(self):
                self.dir = "dir"

    class args:
        check_satus = False
        quiet = False
        follow = False
        output_options = [OUT_REQ_BODY]
        headers = None

    class Downloader:
        def __init__(self, output_file, progress_file, resume):
            self.output_file = output_file
            self.progress_file = progress_file
            self.resume = resume

        def init(self):
            pass
        def start(self, initial_url, final_response):
            pass
        def finish(self):
            pass
        def failed(self):
            pass



# Generated at 2022-06-13 21:48:12.989237
# Unit test for function program
def test_program():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.parser import ParseResult

    # Set up a dummy environment
    env = Environment()
    env.stdin_encoding = 'utf8'
    env.colors = 256
    env.stdout_isatty = False
    env.config.directory = '/home/user/.config/httpie'
    env.config.config_dir = '/home/user/.config/httpie'
    env.config.config_path = '/home/user/.config/httpie/config.json'
    env.config.config_dir_exists = True

    env.default_options = ['--json', '--verbose', '--pretty=all']

    # Set up dummy arguments

# Generated at 2022-06-13 21:48:20.807828
# Unit test for function program
def test_program():
    ut_args = ['http://localhost:8080', '--json', '{"key":"value"}']
    ut_env = Environment()
    ut_env.stdout = StringIO()
    ut_env.stdin = StringIO()
    ut_env.stderr = StringIO()
    ut_env.stdin_isatty = False
    ut_env.stdout_isatty = True
    assert program(args=ut_args, env=ut_env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:48:23.539559
# Unit test for function main
def test_main():
    s = main()
    assert (s == 0)


# Generated at 2022-06-13 21:48:35.352565
# Unit test for function main
def test_main():
    from httpie.cli.parser import parse_form, parse_headers, parse_json
    from httpie.compat import str
    from httpie.config import Environment
    from httpie.context import Environment
    from httpie.downloads import Downloader
    from httpie.output.writer import write_message
    from httpie.status import http_status_to_exit_status
    from httpie.version import __version__ as httpie_version
    from pygments import __version__ as pygments_version
    from requests import __version__ as requests_version
    from sys import exit, version
    from time import time
    def main(args, env=Environment()):
        env.program_name = "http"
        args = decode_raw_args(args, env.stdin_encoding)
        plugin_manager.load_installed_plugins

# Generated at 2022-06-13 21:48:44.261370
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser as cli
    from httpie.core import main
    parser = cli.parser

    # Test if no argument
    sys.argv = []
    sys.argv = ['http']
    result = parser.parse_args(args=['http'])
    assert result.url == 'http://httpie.org', 'url is undefined'
    assert result.headers == {}, 'headers is not empty'
    assert result.method == 'GET', 'method is not GET'
    assert result.output_file is None, 'output is defined'
    sys.argv = ['http']
    result = parser.parse_args(args=['http', '--help'])
    assert result.url == 'http://httpie.org', 'url is undefined'

# Generated at 2022-06-13 21:48:57.033697
# Unit test for function program
def test_program():
    import io
    import sys
    from httpie.context import Environment
    from httpie.cli.parser import parser

    raw_args = ['h', '--print', 'B', '--headers', '-H', 'some: thing', '-v', 'http://httpbin.org/anything']
    args = parser.parse_args(args=raw_args, env=Environment())

    # Because this function calls main() and not main() calls it,
    #  there's no need to create a new environment.
    # Use the default stdout and stderr.

# Generated at 2022-06-13 21:49:10.404448
# Unit test for function main
def test_main():
    import pytest
    from httpie.cli.constants import DEFAULT_TIMEOUT
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.output.writer import write_message
    env = Environment()
    parser.parse_args(['--help'], env=env)
    args = parser.parse_args(['http://httpbin.org/ip'], env=env)
    main(args=['--help'])
    main(args=['GET', 'http://httpbin.org/get'])
    main(args=['http://httpbin.org/get'])
    main(args=['GET', 'http://httpbin.org/ip'])
    main(args=['http://httpbin.org/ip'])