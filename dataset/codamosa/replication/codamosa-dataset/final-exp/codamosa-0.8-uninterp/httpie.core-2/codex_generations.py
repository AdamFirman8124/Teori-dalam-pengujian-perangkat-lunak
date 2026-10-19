

# Generated at 2022-06-13 21:40:55.700744
# Unit test for function program
def test_program():
    import argparse
    import httpie
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://httpie.org'
    args.headers = []
    args.output_options = ['--print', 'h']
    args.output_file = None
    env = httpie.Environment()
    assert program(args, env) == 0

# Generated at 2022-06-13 21:41:00.158410
# Unit test for function main
def test_main():
    assert main(['http', '--debug', 'www.google.com']) == ExitStatus.SUCCESS
    assert main(['http', '--debug']) == ExitStatus.SUCCESS
    assert main(['http', '--traceback', 'www.google.com']) == ExitStatus.SUCCESS
    assert main(['http', '--traceback']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:12.647968
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    from httpie import ExitStatus
    from httpie.context import Environment

    env = Environment()
    env.stdout_isatty = False
    env.stdin_encoding = 'utf8'
    exit_status = main(args=['http', '--version'], env=env)
    assert exit_status == ExitStatus.SUCCESS

    exit_status = main(args=['http', '--download', 'https://httpbin.org/image/jpeg'], env=env)
    assert exit_status == ExitStatus.SUCCESS

    exit_status = main(args=['http', '--download', 'https://httpbin.org/image/jpeg'], env=env)
    assert exit_status == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:41:18.226692
# Unit test for function program
def test_program():
    env = Environment()
    import requests as req
    req.post('http://jsonplaceholder.typicode.com/posts',
    json={
        "title": "foo",
        "body": "bar",
        "userId": 1
    })

# Generated at 2022-06-13 21:41:21.574537
# Unit test for function program
def test_program():
    args = ['GET', 'https://www.google.com']
    program(args, '--quiet')

# Generated at 2022-06-13 21:41:30.276564
# Unit test for function main
def test_main():
    from httpie.cli.constants import DEFAULT_AUTO_METHOD
    from httpie.context import Environment
    from httpie.core import main
    from httpie.core import program
    from httpie.core import separate
    from httpie.core import write_message
    from httpie.core import write_stream
    test_args = ['http', 'example.com']
    test_env = Environment()
    if main(args=test_args) == 0:
        print('Main is working.')
    if program(args=['GET'], env=Environment()) == 0:
        print('Program is working.')
    else:
        print('Program is not working.')
    if separate(test_args, test_env) == 0:
        print('Separate is working.')

# Generated at 2022-06-13 21:41:42.641034
# Unit test for function main
def test_main():
    import httpie.context
    import httpie.downloads
    import httpie.output.writer
    import builtins
    import os
    import time
    import types
    class OutputString(types.SimpleNamespace):
        def __init__(self):
            super().__init__()
            self.value = ''
        def write(self, s):
            self.value = self.value + s
    import httpie.status
    from httpie.status import ExitStatus
    import httpie.cli.constants
    import httpie.cli.definition
    import httpie.client
    import httpie.plugins.registry
    import httpie.plugins.builtin.forms
    import httpie.plugins.builtin.auth
    import httpie.plugins.builtin.hsts
    import httpie.plugins.builtin.pretty_

# Generated at 2022-06-13 21:41:43.537392
# Unit test for function program
def test_program():
    assert True


# Generated at 2022-06-13 21:41:54.740906
# Unit test for function program
def test_program():
    class FakeResponses:
        def __init__(self):
            # class variables are needed for testing
            self.PreparedRequest = "PreparedRequest"
            self.Response = "Response"

    class FakeRequests:
        def __init__(self):
            self.PreparedRequest = FakeResponses().PreparedRequest
            self.Response = FakeResponses().Response

    class FakeArgmentParser:
        def __init__(self):
            # class variables are needed for testing
            self.Namespace = "Namespace"

    class FakeArgumentParserObject:
        def __init__(self):
            # class variables are needed for testing
            self.namespace = "namespace"
            self.parse_args = "parse_args"
            self.output_options = "output_options"


# Generated at 2022-06-13 21:42:03.153708
# Unit test for function main
def test_main():
    import io
    argv = [b'http']
    sys.stdin = io.BytesIO()
    sys.stdout = io.BytesIO()
    sys.stderr = io.BytesIO()
    result = main(argv)
    assert result == ExitStatus.ERROR

# Generated at 2022-06-13 21:42:40.913518
# Unit test for function main
def test_main():
    class myEnv:
        def __init__(self):
            self.program_name = ""

    env = myEnv()
    args = ["httpie.exe"]
    s = main(args, env)
    

# Generated at 2022-06-13 21:42:52.146418
# Unit test for function main
def test_main():
    """
    Unit test for function main.
    """
    from io import StringIO
    from unittest.mock import patch
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.context import Environment
    from httpie.status import ExitStatus
    env = Environment(
        stdin=StringIO(''),
        stdin_isatty=True,
        stdout=StringIO(),
        stdout_isatty=True,
        stderr=StringIO(),
        stderr_isatty=True,
        configuration_dir=DEFAULT_CONFIG_DIR,
    )
    url = 'https://httpie.org'

# Generated at 2022-06-13 21:42:58.520188
# Unit test for function main
def test_main():
    from httpie.context import Environment

    from . import CLI_RELEASE

    env = Environment()
    for arg in CLI_RELEASE:
        print(arg)
        main(arg, env)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 21:43:03.775829
# Unit test for function main
def test_main():
    """
    unit testing for function main
    :return:
    """
    # not real testing
    from httpie.cli.parser import get_parser
    args = get_parser().parse_args(['--debug'])
    print(args.debug)

# Generated at 2022-06-13 21:43:12.868722
# Unit test for function program
def test_program():
    try:
        args = argparse.Namespace(url='http://www.google.com', headers=None, verify=True, response_headers=None, output_file=None, output_options=['h', 'b'], output=None, timeout=30.0, max_redirects=10, method=None, download=False)
        env = Environment()
        program(args, env)
    except Exception as e:
        return False
    if env.log_messages[0][0] != 'HTTP 200 OK':
        return False
    if len(env.log_messages) > 1:
        return False
    return True


# Generated at 2022-06-13 21:43:14.836521
# Unit test for function program
def test_program():
    assert ('', ExitStatus.SUCCESS) == main(args=['https://httpbin.org/get'])

# Generated at 2022-06-13 21:43:26.655580
# Unit test for function main
def test_main():
    """
    Assert that main() exit status is the same as program() exit status.
    """
    from httpie.cli.parser import parser
    from httpie.compat import bytes, stdin
    from httpie.context import Environment
    from httpie.status import ExitStatus
    
    env = Environment()
    argv = ['http', '--headers', 'https://www.google.com']
    # Assert result for main program
    program_result = program(parser.parse_args(argv, env), env)
    # Assert result for main()
    main_result = main(argv, env)
    # Compare the results
    assert program_result == main_result
    assert program_result == ExitStatus.SUCCESS
    assert main_result == ExitStatus.SUCCESS
    # More assertions
    assert isinstance

# Generated at 2022-06-13 21:43:38.697326
# Unit test for function main
def test_main():
    from io import BytesIO
    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.status import http_status_to_exit_status, ExitStatus
    from tests.compat import Mock

    environment = Environment(
        stdin=Mock(), stdout=Mock(), stderr=Mock(),
        stdin_isatty=False, stdout_isatty=False, stderr_isatty=False
    )

    def assert_stdout_stderr(stdout, stderr):
        assert environment.stdout.getvalue() == stdout
        assert environment.stderr.getvalue() == stderr

    # --print=H

# Generated at 2022-06-13 21:43:46.189333
# Unit test for function program
def test_program():
    from contextlib import contextmanager
    from io import StringIO
    from unittest import TestCase
    from .compat import is_windows
    from .constants import DEFAULT_CONFIG_DIR
    from .context import Environment
    from .downloads import Downloader
    from .models import Environment as Env
    from .status import ExitStatus

    class ProgramTest(TestCase):

        @contextmanager
        def capture_stdout(self):
            stdout = sys.stdout
            try:
                sys.stdout = StringIO()
                yield sys.stdout
            finally:
                sys.stdout = stdout


        def test_get_output_options(self):
            req = requests.PreparedRequest()
            resp = requests.Response()
            args = argparse.Namespace(output_options=[])

# Generated at 2022-06-13 21:43:54.042437
# Unit test for function main
def test_main():
    from httpie.cli import definitions
    from httpie.cli.parser import parser
    from httpie.cli.args import Namespace

    parsed = parser.parse_args(['-J', 'GET', '--traceback', 'https://httpbin.org/get'], env=Environment())
    assert parsed.stdout_isatty is None
    assert isinstance(parsed, Namespace)
    assert parsed.json is True
    assert parsed.output_options == ['all']
    assert parsed.timeout == definitions.DEFAULT_TIMEOUT
    assert parsed.max_redirects == definitions.DEFAULT_MAX_REDIRECTS
    assert parsed.follow == True
    assert parsed.check_status == False


# TODO: test_program
# TODO: test_decode_raw_args