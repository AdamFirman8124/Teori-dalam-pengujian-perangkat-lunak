

# Generated at 2022-06-13 21:40:48.929862
# Unit test for function program
def test_program():
    class Test_config:
        def __init__(self):
            self.stdin_encoding = 'utf-8'

    class Test_env:
        def __init__(self):
            self.config = Test_config()
            self.stderr = sys.stderr
            self.stdout = sys.stdout

    test_env = Test_env()
    exit_status = program(args=['--debug'], env=test_env)
    print('status code: ', exit_status)


if __name__ == '__main__':

    print_debug_info()

# Generated at 2022-06-13 21:40:54.340275
# Unit test for function main
def test_main():
    # One time initialization and setup.
    import tempfile
    import csv
    import time
    from httpie.downloads import Downloader
    from httpie.output.writer import write_message, MESSAGE_SEPARATOR_BYTES
    from httpie.cli.argtypes import KeyValueArgType
    import httpie.plugins
    httpie.plugins.load_installed_plugins()
    # Create the temp file
    # tempfile.mktemp()
    (fd, filename) = tempfile.mkstemp()
    # Create the output file object
    output_file = open(filename, 'w')
    # Create the temp file
    # tempfile.tempdir
    # Create the env object
    env = Environment()
    # Create the argparse.Namespace object
    # args = argparse.Namespace()
    #

# Generated at 2022-06-13 21:40:56.554227
# Unit test for function program
def test_program():
    return program(args="httpbin.org",env="httpbin")


# Generated at 2022-06-13 21:41:02.450480
# Unit test for function main
def test_main():
    for args in (['--debug'], [], ['-j', '{}'], ['https://httpbin.org/get'], ['key', 'value']
    ):
        # print(args)
        _main = main(args)
        # print('Exit code:', _main)

    # output = main(['https://get.httpbin.org/'])
test_main()

# Generated at 2022-06-13 21:41:04.437077
# Unit test for function program
def test_program():
    args = argparse.Namespace()
    program(args, Environment())

# Generated at 2022-06-13 21:41:14.989459
# Unit test for function program
def test_program():
    main(['httpie', '--headers', 'www.baidu.com'])
    main(['httpie', '--body', 'www.baidu.com'])
    main(['httpie', '--download', 'www.baidu.com', '--output', '/Users/lisong/ba.html'])
    main(['httpie', '--check-status', 'www.baidu.com'])
    main(['httpie', '--quiet', 'www.baidu.com'])
    main(['httpie', '--form', 'www.baidu.com'])
    main(['httpie', '--json', 'www.baidu.com'])
    main(['httpie', '--output-options', 'www.baidu.com'])

# Generated at 2022-06-13 21:41:28.719324
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli import parser
    from httpie.cli.parser import get_parser

    parser = get_parser()
    args = parser.parse_args(['https://httpbin.org/get'])
    #from urllib import parse
    #from httpie.models import URL
    #args.headers['host'] = 'httpbin.org'
    #from httpie.core import main
    #from httpie.output.formatters.colors import get_lexer
    #from httpie.output.streams import write_headers
    #from httpie.output.writers import write_headers as write_headers2
    from httpie.output.streams import write_bytes
    from httpie.output.formatters.colors import get_lexer
    from httpie import ExitStatus
    #response = main

# Generated at 2022-06-13 21:41:36.403511
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli.argtypes import KeyValueArg
    from httpie.compat import is_windows
    from httpie.core import Environment, main
    from httpie.plugins import builtin

    env = Environment()
    class TestDownloader:
        def __init__(self):
            self.args = []
            self.output_files = []
        def pre_request(self, headers): pass
        def start(self, initial_url, final_response):
            self.args.append(final_response)
            self.output_files.append(open("final_res", 'w'))
            return open("final_res", 'r'), open("out", 'w')
        def finish(self): pass
        def failed(self): pass
        @property
        def finished(self):
            return True


# Generated at 2022-06-13 21:41:46.410604
# Unit test for function main
def test_main():
    class MockStderr:
        def __init__(self):
            self.lines = []
        def write(self, line):
            self.lines.append(line)
        def flush(self):
            pass

    class MockStdin:
        def __init__(self, encoding):
            self.lines = [b'chunk1', b'chunk2']
            self.encoding = encoding

        def read(self, size):
            if len(self.lines) > 0:
                return self.lines.pop()
            else:
                return None


    # This test is a bit complex to get the control flow..
    # The function main is a proxy to the function `program`
    # and it contains exception handling.
    # In this unit test we have three basic cases:
    # * `program` raises an exception.

# Generated at 2022-06-13 21:41:55.930250
# Unit test for function main
def test_main():
    import os
    import io

    class MockStdOut:
        def __init__(self):
            self.content = io.StringIO()
        def write(self, msg):
            self.content.write(msg)
        def getvalue(self):
            return self.content.getvalue()

    class MockStdErr:
        def __init__(self):
            self.content = io.StringIO()
        def write(self, msg):
            self.content.write(msg)
        def getvalue(self):
            return self.content.getvalue()

    class MockStdIn:
        def __init__(self):
            self.content = io.StringIO()
        def write(self, msg):
            self.content.write(msg)
        def getvalue(self):
            return self.content

# Generated at 2022-06-13 21:46:59.451573
# Unit test for function program
def test_program():
    assert True



# Generated at 2022-06-13 21:47:13.694329
# Unit test for function main
def test_main():
    """
    Mock environment for unit test for function main

    """
    class MockStdin():
        def __init__(self):
            self.encoding = 'utf-8'

        def isatty(self):
            return True

    class MockStderr():
        def __init__(self):
            self.encoding = 'utf-8'

        def isatty(self):
            return True

    class MockStdout():
        def __init__(self):
            self.encoding = 'utf-8'

        def isatty(self):
            return True

    class MockConfig():
        def __init__(self):
            self.directory = 'httpie'
            self.default_options = ['-p']

    class MockEnvironment:
        program_name = 'http'

    mock_env = Environment

# Generated at 2022-06-13 21:47:21.124694
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    print(parser.parse_args(['http://127.0.0.1:8000/sport/']))


if __name__ == '__main__':
    # Unit test for function main
    print(main())
    # Unit test for function main
    print(program(['http://127.0.0.1:8000/sport/']))

# Generated at 2022-06-13 21:47:25.419238
# Unit test for function main
def test_main():
    assert main(['http', 'example.com']) == main(['http', '--download', 'example.com'])

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 21:47:37.542107
# Unit test for function main
def test_main():
    # pylint:disable=E1120
    import subprocess
    import sys
    # noinspection PyUnresolvedReferences
    import tests.httpbin  # noqa
    import pytest

    @pytest.mark.parametrize(
        'exit_status',
        [ExitStatus.SUCCESS, ExitStatus.ERROR]
    )
    def test_exit_status_from_system_exit(exit_status):
        if exit_status == ExitStatus.SUCCESS:
            subprocess.check_output([sys.executable, '-m', 'httpie', '--debug'])

# Generated at 2022-06-13 21:47:49.126060
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    def dummy_program(*args, **kwargs):
        return ExitStatus.SUCCESS
    from httpie.context import Environment
    def test_main(cmd_line_args, env=Environment()):
        args = cmd_line_args.split(' ')
        program_name, *args = args
        args = decode_raw_args(args, env.stdin_encoding)
        return main(program_name, args, env)
    import argparse
    def parse_args(cmd_line_args, env=Environment()):
        args = cmd_line_args.split(' ')
        program_name, *args = args
        args = decode_raw_args(args, env.stdin_encoding)
        return parser.parse_args(args, env=env)


# Generated at 2022-06-13 21:47:51.489123
# Unit test for function main
def test_main():
    from httpie.context import Environment
    env = Environment()
    main(["httpie", "--debug"], env)

# Generated at 2022-06-13 21:48:02.167628
# Unit test for function program
def test_program():
    class mock_args():
        check_status = False
        download = False
        download_resume = False
        follow = False
        headers = []
        max_redirects = 10
        output_file = None
        output_file_specified = False
        output_options = []
        quiet = False
        timeout = 30.0

    class mock_stdout():
        def __init__(self):
            self.mock_val = []

        def write(self,str):
            self.mock_val = str

        def get_value(self):
            return self.mock_val

    class mock_stderr():
        def __init__(self):
            self.__var = ""

        def write(self,str):
            self.__var = str

        def get_value(self):
            return

# Generated at 2022-06-13 21:48:12.835110
# Unit test for function program
def test_program():
    env = Environment()
    args = argparse.Namespace(print=False, traceback=False, config_dir=None, output_file_specified=False,
                              output_file=None, https_proxy=None, headers=None, max_redirects=30, use_http2=None,
                              verify=True, debug=False, quiet=False, body=None, json=False, output_options=None,
                              session=None, style=None, download=False, download_resume=False)
    args.output_options = [OUT_REQ_HEAD, OUT_REQ_BODY, OUT_RESP_HEAD, OUT_RESP_BODY]
    headers = None

# Generated at 2022-06-13 21:48:16.222958
# Unit test for function program
def test_program():
    args = ['GET', 'http://example.com']
    env = Environment()
    status = program(args, env)
    assert status is 0