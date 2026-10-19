

# Generated at 2022-06-13 21:41:10.482342
# Unit test for function program
def test_program():
   assert program(['GET','http://www.httpbin.org/']) == True
   assert program(['POST','http://www.httpbin.org/post']) == True
   assert program(['PUT','http://www.httpbin.org/put']) == True
   assert program(['DELETE','http://www.httpbin.org/delete']) == True
   assert program(['http://www.httpbin.org/']) == True

# Generated at 2022-06-13 21:41:18.145762
# Unit test for function program
def test_program():
    sys.argv = ["httpie", "http://localhost:8080/api/1.0/items_list"]
    main()
    sys.argv = ["httpie", "--headers", "http://localhost:8080/api/1.0/items_list"]
    main()

# Generated at 2022-06-13 21:41:24.330954
# Unit test for function program
def test_program():
    env = Environment()
    args = argparse.Namespace(method='GET', url='http://httpbin.org/get', output_options=['hb'])
    assert program(args=args, env=env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:41:31.048284
# Unit test for function program
def test_program():
    args = [ "http","-v","-H","Accept:application/json", "http://httpbin.org/get","--body"]
    env = Environment()
    program(args,env)
    assert env.stdout_isatty == True

#Unit test for function get_output_options

# Generated at 2022-06-13 21:41:42.422913
# Unit test for function program
def test_program():
    import pytest
    # Custom stdout: https://stackoverflow.com/a/16571630/43055
    import builtins
    old_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    from httpie.cli.definition import parser
    args = parser.parse_args(['--output', 'tests/samples/test_outputs.txt', 'http://google.com'])
    program(args=args, env=Environment())
    sys.stdout = old_stdout
    file = open("tests/samples/test_outputs.txt")
    # Compare stdout to sample output file
    assert captured_output.getvalue() == file.read()
    file.close()



# Generated at 2022-06-13 21:41:58.088833
# Unit test for function main
def test_main():
    # Test: --debug no args
    status, output = unittest_helper(['http', '--debug'], b'', b'', '')
    assert status == ExitStatus.SUCCESS
    assert output.startswith('HTTPie 1.')
    assert output.endswith(' win32\r\n')

    # Test: --help no args
    status, output = unittest_helper(['http', '--help'], b'', b'', '')
    assert status == ExitStatus.SUCCESS
    assert output.startswith('usage: http')

    # Test: --version no args
    status, output = unittest_helper(['http', '--version'], b'', b'', '')
    assert status == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:42:12.401580
# Unit test for function main
def test_main():
    from httpie.cli.constants import DEFAULT_CONFIG_DIR
    from httpie.config import Config, ConfigFileNotFound
    import os
    import os.path as pth
    from tempfile import TemporaryDirectory
    from unittest import mock
    import shutil
    from httpie.compat import is_windows

    # This helper function is required since Windows paths are different from the Unix paths
    def remove_path_prefix(orignal_string):
        if is_windows:
            return orignal_string[3:]
        else:
            return orignal_string

    def remove_path_prefix_windows(orignal_string):
        return orignal_string[3:]

    # Open existing httpie config file

# Generated at 2022-06-13 21:42:23.625226
# Unit test for function program
def test_program():
    from requests import PreparedRequest
    from httpie.output.streams import StdoutBytesIO, StderrBytesIO
    from httpie.cli.parser import args_parser
    from httpie.config import Config

    env = Environment(
        stdin=StdoutBytesIO(),
        stdin_isatty=False,
        stdout=StdoutBytesIO(),
        stdout_isatty=False,
        stderr=StderrBytesIO(),
        stdout_isatty=False,
        config=Config(),
    )

    msg = PreparedRequest()
    msg.url = 'https://example.org/'
    msg.method = 'GET'
    msg.headers = {'Accept': '*/*'}
    msg.is_body_upload_chunk = False

# Generated at 2022-06-13 21:42:33.744606
# Unit test for function program
def test_program():
    from pytest import raises
    from httpie import __version__
    from io import BytesIO
    from httpie.cli.definition import Arg, Args, parser
    from httpie.cli.argtypes import KeyValueArg, KeyValueType
    from httpie.downloads import Downloader
    from httpie.output import Writer
    from httpie.status import ExitStatus
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.output.streams import get_binary_stream
    from httpie.output.writers.streamwriter import StreamWriter
    from httpie.plugins.manager import PluginManager
    from httpie.client import collect_messages
    from httpie.input import ParseError
    from httpie.util import get_response_type
    from httpie.input.auth import parse_auth
   

# Generated at 2022-06-13 21:42:37.423000
# Unit test for function main
def test_main():
    args = ['http', '--ignore-stdin', 'https://httpbin.org/get']
    result = main(args=args)
    assert result == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:43:53.541189
# Unit test for function program
def test_program():
    from httpie.context import Environment
    from httpie.cli.definition import parser
    from httpie import ExitStatus
    from httpie.input import ParseError
    from tests.utils import TestEnvironment, http
    from httpie.plugins.builtin.forms import urlencoded
    from httpie.plugins.builtin.tests.non_ascii import TestNonAscii
    env = TestEnvironment(stdout_isatty=True)
    TestNonAscii.test_utf8_request_body_and_headers(httpbin=http)
    TestNonAscii.test_nonascii(httpbin=http)
    TestNonAscii.test_binary_request_content(httpbin=http)
    TestNonAscii.test_binary_response_content(httpbin=http)
    TestNonAsci

# Generated at 2022-06-13 21:44:05.654307
# Unit test for function program
def test_program():
    import unittest.mock
    from httpie.cli.definition import parser
    class testArgs():
        pass
    args = testArgs()
    args.headers = []
    args.output_options = [OUT_REQ_HEAD]
    args.check_status = False
    args.follow = True
    args.quiet = False
    args.download = False
    args.download_resume = False
    args.output_file = None
    args.output_file_specified = False
    args.data = None
    args.json = None
    args.verbose = False
    args.url = 'https://httpbin.org/get'
    parsed_args = parser.parse_args(args=args, env=testEnv())


# Generated at 2022-06-13 21:44:17.452298
# Unit test for function main
def test_main():
    from httpie.cli.constants import CONFIG_DIR
    from os.path import join
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory(prefix='httpie-test-') as tmp_dir:
        test_config_dir = join(tmp_dir, CONFIG_DIR)
        os.environ['HOME'] = tmp_dir
        Path(test_config_dir).mkdir(exist_ok=True, parents=True)

        env = Environment()
        assert main(args=[sys.argv[0], '--debug'], env=env) == ExitStatus.SUCCESS
        assert main(args=[sys.argv[0], '--follow'], env=env) == ExitStatus.ERROR
        assert main(args=[sys.argv[0], 'http://google.com'], env=env)

# Generated at 2022-06-13 21:44:25.512475
# Unit test for function program
def test_program():
    args = [
        'https://jsonplaceholder.typicode.com/posts/1',
        '--verbose',
        '--json',
        '--output',
        '.\\result.json'
    ]
    program(args)

# Generated at 2022-06-13 21:44:35.950445
# Unit test for function program
def test_program():
    import pytest
    from httpie.cli import parse_args
    from httpie.output.streams import OutputStream

    def mock_collect_messages(args, config_dir, request_body_read_callback):
        for msg in [args, args]:
            if msg == args and (OUT_REQ_BODY in args.output_options):
                request_body_read_callback(b'123')
            yield msg

    # noinspection PyShadowingNames
    def program(args):
        if args.check_status:  # pragma: no cover
            if args.follow:
                ExitStatus.SUCCESS
            else:
                ExitStatus.ERROR
        else:
            ExitStatus.SUCCESS


# Generated at 2022-06-13 21:44:37.529704
# Unit test for function main
def test_main():
    assert main(['http', '--help']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:41.739655
# Unit test for function main
def test_main():
    ## Test for main function without any arguments
    assert main() == ExitStatus.SUCCESS
    ## Test for main function with specified arguments
    assert main(args=['x', 'y', 'z']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:53.682594
# Unit test for function program
def test_program():
    """Unit test for function program"""
    os.environ['HTTPS_PROXY'] = 'https://127.0.0.1:8080'
    os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8080'

    os.environ['NO_PROXY'] = 'localhost, localhost.localdomain, local, 127.0.0.1, 127.0.0.1.1'
    os.environ['REQUESTS_CA_BUNDLE'] = '<path>'
    os.environ['SSL_CERT_DIR'] = '<path>'
    os.environ['ssl_cert_file'] = '<path>'
    os.environ['REQUESTS_CA_BUNDLE'] = '<path>'
    os

# Generated at 2022-06-13 21:44:55.585428
# Unit test for function main
def test_main():
    assert main(['--debug']) == 0

# Generated at 2022-06-13 21:44:59.174924
# Unit test for function main
def test_main():
    try:
        result = main(["httpie","--debug"])
        assert result == ExitStatus.SUCCESS
    except AssertionError:
        print("AssertionError")
    except Exception as e:
        print(e)


# Generated at 2022-06-13 21:45:34.409706
# Unit test for function main
def test_main():
    test_main.__doc__ = main.__doc__

    print("Running tests")



# Generated at 2022-06-13 21:45:41.741064
# Unit test for function main
def test_main():
    assert main(['--debug']) == ExitStatus.SUCCESS
    assert main(['--debug', '--traceback']) == ExitStatus.ERROR
    assert main(['--debug', 'g', 'h', 'i']) == ExitStatus.ERROR
    assert main(['--debug', '--form', 'a=1']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:45:43.945460
# Unit test for function main
def test_main():
  args = ["http", "--timeout", "5", "www.google.com"]
  main(args)

# Generated at 2022-06-13 21:45:55.713103
# Unit test for function main
def test_main():
    # Test: empty args
    import httpie
    _, _ = main(['http'])
    # Test: default arguments
    _, _ = main(['http', 'get', '-b', 'httpbin.org', '-h', 'Accept: application/json'])
    # Test: default arguments
    _, _ = main(['http', 'get', '-b', 'httpbin.org', '-h', 'Accept: application/json'])
    # Test: with -v
    _, _ = main(['http', 'get', '-b', 'httpbin.org', '-v', '-h', 'Accept: application/json'])
    # Test: with --debug

# Generated at 2022-06-13 21:46:03.833408
# Unit test for function main
def test_main():
    class MockStdStream:
        def __init__(self):
            self.args = list()
            self.stderr = list()

        def write(self, bs):
            self.args.append(bs)

    try:
        sys.argv = ['http']
        print(
            main(env=Environment(stdout=MockStdStream(), stderr=MockStdStream()))
        )
    except Exception as e:
        print(e)

# Generated at 2022-06-13 21:46:05.601965
# Unit test for function program
def test_program():
    import pytest
    main(["www.google.com"])



# Generated at 2022-06-13 21:46:09.589803
# Unit test for function main
def test_main():
    env = Environment()
    # TODO: Write unit tests for main
    test_argv = ['http', '--debug', '--traceback']
    main(args=test_argv, env=env)

# Generated at 2022-06-13 21:46:14.202937
# Unit test for function program
def test_program():
    args = parser.parse_args(args=['https://example.org'], env=Environment())
    print(program(args=args, env=Environment()))


if __name__ == '__main__':
    test_program()

# Generated at 2022-06-13 21:46:22.084186
# Unit test for function program
def test_program():
    ## for test_program
    from httpie.cli import program
    import sys


    def get_input_data():
        return sys.stdin.read()
        ##
    assert program([sys.argv[0], "https://httpbin.org/get"]) == 0
    assert program([sys.argv[0], "https://httpbin.org/status/418"]) == ExitStatus.ERROR_HTTP_418


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:46:24.839369
# Unit test for function program
def test_program():
    # TODO: Add test of piped input
    # TODO: Add test of file input
    # TODO: Add test of file output
    pass

# Generated at 2022-06-13 21:47:13.816070
# Unit test for function main
def test_main():
    from httpie.context import Environment
    from io import StringIO
    import sys

    out = StringIO()

    env = Environment()
    env.stderr = StringIO()
    env.stdout = out
    old_args = sys.argv
    sys.argv = ['http']
    try:
        main(args=['GET', 'https://api.github.com/repos/jakubroztocil/httpie/commits'], env=env)
        sys.argv = old_args
    except SystemExit:
        assert False


# Generated at 2022-06-13 21:47:22.062689
# Unit test for function program
def test_program():
    env = Environment()
    args = [
        'http',
        '--output-options',
        'resp.body,req.headers',
        '--verbose',
        'example.org'
    ]
    args = decode_raw_args(args, env.stdin_encoding)
    from httpie.cli.definition import parser
    parsed_args = parser.parse_args(args=args, env=env)
    program(parsed_args, env)

# Generated at 2022-06-13 21:47:25.669348
# Unit test for function program
def test_program():
    args = argparse.Namespace()
    env = Environment()
    assert program(args, env) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:47:36.159668
# Unit test for function program
def test_program():
    '''
    This function will test the program function
    '''
    import pytest
    from argparse import Namespace
    from httpie.cli.argtypes import KeyValueArg
    from httpie.cli.definition import parser
    from httpie.cli.utils import get_response_data
    from httpie.client import collect_messages
    from httpie.output.streams import StdoutBytesIO
    from httpie.context import Environment
    
    class MockPreparedRequest(object):
        is_body_upload_chunk = None
        body = None
        headers = None
        
    class MockResponse(object):
        raw = None
        status_code = None
        
    class MockDownloader(object):
        output_file = None
        progress_file = None
        resume = None
        status = None
       

# Generated at 2022-06-13 21:47:40.736084
# Unit test for function program
def test_program():
    import pytest
    class Mock:
        def __init__(self,type_):
            self.code = type_
    class MockEnv:
        def __init__(self):
            self.stdout = None

    with pytest.raises(SystemExit):
        program(Mock(ExitStatus.SUCCESS),MockEnv())

# Generated at 2022-06-13 21:47:43.059129
# Unit test for function program
def test_program():
    program('program', 'args', Environment('env'))


# Generated at 2022-06-13 21:47:49.546065
# Unit test for function main
def test_main():
    # TODO: Mock os.path.basename, sys.argv, run(), and pygments.token
    argv = ["C:\\Users\\username\\AppData\\Local\\Programs\\Python\\Python38\\python.exe","http"]
    result = main(argv)
    assert result == 2

# Generated at 2022-06-13 21:47:50.463258
# Unit test for function program
def test_program():
    print(program)

# Generated at 2022-06-13 21:48:00.340649
# Unit test for function main
def test_main():
    # generate the test strings
    test_string = 'This is the test string'
    test_file = 'test_file.txt'
    # generate a test file
    with open(test_file, 'w') as f:
        f.write(test_string)
    # build the argument list
    args = ['www.test.com', '--verbose', '--body', '~/' + test_file, '--headers']
    # check if the arguments are valid
    code = main(args)
    assert code == ExitStatus.SUCCESS
    # clean up
    os.remove(test_file)


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-13 21:48:04.080608
# Unit test for function main
def test_main():
    assert main(['httpie']) == ExitStatus.SUCCESS  # noqa: E501

# Generated at 2022-06-13 21:48:40.178355
# Unit test for function program
def test_program():
    args = mock.create_autospec(argparse.Namespace)
    env = mock.create_autospec(Environment)
    program(args,env)

# Generated at 2022-06-13 21:48:56.100685
# Unit test for function program

# Generated at 2022-06-13 21:49:05.985993
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser, args2env
    try:
        from httpie import __main__
    except ImportError:
        exit("Import error." + " Please check the installation of httpie.")
    args_str = '--download=www.google.com'
    args = parser.parse_args(
        args=args_str.split(),
        env=args2env(args=args_str.split())
    )
    assert program(
        args=args,
        env=args2env(args=args_str.split())
    ) == ExitStatus.SUCCESS


# Generated at 2022-06-13 21:49:08.472599
# Unit test for function program
def test_program():
    main(args = ["testapi.sh", "https://httpbin.org/get"], env = Environment())

# Generated at 2022-06-13 21:49:19.717895
# Unit test for function program
def test_program():
    from httpie import ExitStatus
    from httpie.cli.definition import parser
    from httpie.client import collect_messages
    #
    # args = parser.parse_args(args = ['-h'])
    args = parser.parse_args(args = ['--download', 'http://httpbin.org/get', '--output=../test.txt'])
    env = Environment()
    exit_status = ExitStatus.SUCCESS
    downloader = None
    initial_request: Optional[requests.PreparedRequest] = None
    final_response: Optional[requests.Response] = None

    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)


# Generated at 2022-06-13 21:49:29.534440
# Unit test for function program
def test_program():
    args = argparse.Namespace(url='http://www.google.com', method='GET', data={'key1': 'value1', 'key2': 'value2'},
                              headers={'Accept': 'text/html', 'Accept-Charset': 'utf-8'}, output_options=['arjun'],
                              form=False, json=False, verbose=True, output_file=None, output_file_specified=False,
                              download=True, download_resume=False, follow=True, check_status=True, quiet=False)
    env = Environment()
    exit_status = program(args, env)
    print(exit_status)


# Generated at 2022-06-13 21:49:38.923766
# Unit test for function main
def test_main():
    from httpie.cli.constants import (
        DEV_NULL,
        DEV_STDIN,
        DEV_STDOUT,
    )
    from httpie.cli.definition import parser

    parser.error = lambda msg: print(msg)


# Generated at 2022-06-13 21:49:49.578379
# Unit test for function program
def test_program():
    from httpie.cli.parser import parser
    from httpie.environment import Environment
    from httpie.output.writer import write_message, write_stream, MESSAGE_SEPARATOR_BYTES
    import argparse
    import requests
    import sys
    env = Environment()
    env.program_name = 'http'
    args = parser.parse_args(
        args=sys.argv,
        env=env,
    )
    exit_status = ExitStatus.SUCCESS
    downloader = None
    initial_request: Optional[requests.PreparedRequest] = None
    final_response: Optional[requests.Response] = None

    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)


# Generated at 2022-06-13 21:50:04.871559
# Unit test for function main
def test_main():
    import io
    from httpie.cli.constants import DEFAULT_CONFIG_DIR
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.plugins.manager import PluginManager

    env = Environment(
        stdin=io.BytesIO(),
        stdout=io.BytesIO(),
        stderr=io.BytesIO(),
        stdin_isatty=False,
        stdout_isatty=False,
        stderr_isatty=False,
        config=Config(directory=DEFAULT_CONFIG_DIR),
        env=None,
        plugins=PluginManager(),
    )
    assert main(['http', 'httpbin.org'], env=env) == 0

# Generated at 2022-06-13 21:50:20.085076
# Unit test for function program
def test_program():
    from io import BytesIO
    from httpie.context import Environment
    from httpie.cli.parser import parser_kwargs

    env = Environment()
    kwargs = parser_kwargs(env)
    args = parser.parse_args(['http://google.com'], **kwargs)
    args.output_file = BytesIO()

    status = program(args, env)
    assert status == ExitStatus.SUCCESS

    args = parser.parse_args(['--output=foo', 'http://google.com'], **kwargs)
    args.output_file = BytesIO()

    status = program(args, env)
    assert status == ExitStatus.SUCCESS

    args = parser.parse_args(['--output=google.com', 'http://google.com'], **kwargs)