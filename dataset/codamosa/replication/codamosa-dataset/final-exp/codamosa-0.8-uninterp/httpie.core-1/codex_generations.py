

# Generated at 2022-06-13 21:44:06.635082
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch

    from httpie import ExitStatus

    with patch('sys.stdin', StringIO()):
        assert main() == ExitStatus.SUCCESS
        assert main(['--debug']) == ExitStatus.SUCCESS
        assert main(['--help']) == ExitStatus.SUCCESS
        assert main(['--version']) == ExitStatus.SUCCESS
        assert main(['GET']) == ExitStatus.ERROR
        assert main(['--ignore-stdin', 'GET']) == ExitStatus.SUCCESS
        assert main(['--help', 'GET']) == ExitStatus.ERROR
        assert main(['GET', '--help']) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:09.252893
# Unit test for function main
def test_main():
    assert main(["http", "https://httpbin.org/post", "-v"]) == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:44:11.596114
# Unit test for function program
def test_program():
    exit_status = main(['http', 'www.google.com'])
    assert exit_status == ExitStatus.SUCCESS

test_program()

# Generated at 2022-06-13 21:44:22.988306
# Unit test for function program

# Generated at 2022-06-13 21:44:35.050873
# Unit test for function main
def test_main():
	
	# 1. testing for ExitStatus.SUCCESS
	assert main(['http','--debug']) == ExitStatus.SUCCESS
	
	# 2. testing for ExitStatus.ERROR
	try:
		main(['http','-v','-f', '--traceback'])
	except:
		assert main(['http','-v','-f', '--traceback']) == ExitStatus.ERROR
		
	# 3. testing for ExitStatus.ERROR_CTRL_C
	#assert main(['http', '-v', '-f']) == ExitStatus.ERROR_CTRL_C
	
	# 4. testing for ExitStatus.ERROR_TIMEOUT
	assert main(['http', '-v', '-f', '--timeout=1', 'http://localhost:1']) == ExitStatus.ERROR_

# Generated at 2022-06-13 21:44:48.013016
# Unit test for function program
def test_program():
    test_args = sys.argv
    test_env = Environment()
    test_args = decode_raw_args(test_args, test_env.stdin_encoding)
    plugin_manager.load_installed_plugins()
    from httpie.cli.definition import parser
    if test_env.config.default_options:
        test_args = test_env.config.default_options + test_args
    parsed_args = parser.parse_args(
        args=test_args,
        env=test_env,
    )
    exit_status = program(
        args=parsed_args,
        env=test_env,
    )
    return exit_status
    
    
if __name__ == '__main__' and 'unittest' not in sys.modules:
    sys.exit(main())

# Generated at 2022-06-13 21:44:58.104155
# Unit test for function main
def test_main():
    from httpie import ExitStatus
    exit_code = main()
    assert exit_code == ExitStatus.SUCCESS  # 0 is the default
    exit_code = main(['--debug'])
    assert exit_code == ExitStatus.SUCCESS
    exit_code = main(['--traceback'])
    assert exit_code == ExitStatus.SUCCESS
    exit_code = main(['--help'])
    assert exit_code == ExitStatus.SUCCESS
    exit_code = main(['--version'])
    assert exit_code == ExitStatus.SUCCESS
    exit_code = main(['--form'])
    assert exit_code == ExitStatus.ERROR
    exit_code = main(['--download'])
    assert exit_code == ExitStatus.ERROR

# Generated at 2022-06-13 21:45:03.284260
# Unit test for function main
def test_main():
    from unittest.mock import Mock, patch

    from httpie.cli.context import Environment

    env = Environment()
    env.log_error = Mock()
    try:
        sys.argv[1] = '/'
        with patch.object(sys, 'argv', sys.argv):
            main()

    except SystemExit as e:
        assert e.code == ExitStatus.SUCCESS



# Generated at 2022-06-13 21:45:05.061493
# Unit test for function program
def test_program():
    main(args=['http', '-vv'])

# Generated at 2022-06-13 21:45:11.246784
# Unit test for function main
def test_main():
    import sys
    import os
    import inspect
    testdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    httpie_dir = os.path.join(testdir,'httpie')
    sys.path.insert(0,httpie_dir)
    sys.argv = ['http', 'example.org']
    print(os.path.dirname(sys.argv))
    print('return code:', main())


# Generated at 2022-06-13 21:46:39.108737
# Unit test for function program
def test_program():
    args = ['httpie', '--help']
    env = Environment()

    ex = program(args=args, env=env)
    assert ex is ExitStatus.SUCCESS

# Generated at 2022-06-13 21:46:51.753486
# Unit test for function main
def test_main():
    from httpie.cli.parser import get_parser
    from httpie.cli.constants import OUT_RESP, OUT_REQ, OUT_REQ_HEAD, OUT_REQ_BODY

    parser = get_parser()
    args = parser.parse_args(['--debug'])
    # args = parser.parse_args(['--debug','https://httpbin.org/get','test','test'])
    assert args.output_options == [OUT_RESP]

    args = parser.parse_args(['https://httpbin.org/get','test','test',
    '--verbose','--debug','--traceback','--output-options','vb'])
    assert '--output-options' in args.output_options


# Generated at 2022-06-13 21:47:00.109580
# Unit test for function main
def test_main():


    import io
    import unittest
    import unittest.mock

    from httpie.cli.base import BASE_ENV
    from httpie.context import Environment

    class MainTestCase(unittest.TestCase):
        def setUp(self):
            self.runner = unittest.mock.Mock()
            self.runner.return_value = ExitStatus.SUCCESS
            self.stdin = io.BytesIO()
            self.stdout = io.BytesIO()
            self.env = Environment(
                stdin=self.stdin,
                stdout=self.stdout,
                colors=256,
                stdin_isatty=True,
                stdout_isatty=True,
            )


# Generated at 2022-06-13 21:47:02.350491
# Unit test for function program
def test_program():
  program()

if __name__ == '__main__':
  main()

# Generated at 2022-06-13 21:47:04.437944
# Unit test for function program
def test_program():
    pass


# Generated at 2022-06-13 21:47:17.148822
# Unit test for function program
def test_program():
    import os
    import sys
    import shutil
    import tempfile

    def call_program(args):
        return program.__wrapped__(argparse.Namespace(args), Environment())

    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)


# Generated at 2022-06-13 21:47:33.783351
# Unit test for function program
def test_program():
    from httpie.cli.constants import OUT_BODY, OUT_HEADERS, OUT_REQ_HEAD, OUT_RESP_HEAD
    from httpie.context import Environment
    from httpie.plugins import builtin
    from httpie.plugins.manager import plugin_manager
    import httpie.plugins.builtin
    from httpie import ExitStatus
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from httpie.downloads import Downloader
    import argparse
    import io
    import sys
    import os
    import json
    import unittest
    import pytest

    class StdoutBytesIO(io.BytesIO):
        def write(self, b: bytes):
            sys.stdout.buffer.write(b)


# Generated at 2022-06-13 21:47:42.892684
# Unit test for function program
def test_program():
    import httpie
    import os
    import time
    import urllib
    import urllib.request
    # os.system("touch log.txt")
    # os.system("touch log2.txt")
    start = time.time()
    arg = ['GET', 'https://httpie.org/', '--verbose']
    out_req_body = []
    out_req_headers = []
    out_resp_body = []
    out_resp_headers = []
    out = open("log.txt","a+")
    log = open("log2.txt","a+")
    class Namespace:
        def __init__(self):
            self.output_file = out
            self.output_file_specified = True
            self.headers = out_req_headers

# Generated at 2022-06-13 21:47:45.035434
# Unit test for function main
def test_main():
    assert main(args = ['http', '--debug', '-v']) == 0


# Generated at 2022-06-13 21:47:49.596733
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser
    args=parser.parse_args(['-v', 'GET', 'www.example.com'])
    env=Environment()
    env.configure()
    assert "www.example.com" in program(args, env)

# Generated at 2022-06-13 21:49:27.929186
# Unit test for function main
def test_main():
    from click.testing import CliRunner

    runner = CliRunner()
    result = runner.invoke(main)
    assert result.output == ''
    assert result.exit_code == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:49:35.603385
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    assert main(['http', '--help']) == ExitStatus.SUCCESS
    assert main(['http', 'https://a.com']) == ExitStatus.SUCCESS
    assert main(['http', '--method', 'POST', '--json', '{"a":"b"}', 'https://a.com']) == ExitStatus.SUCCESS
    with raised(SystemExit):
        main(['httpie', '-hh'])
        main(['httpie', '--h'])
        main(['httpie', '-A', 'User-Agent', '-h'])



# Generated at 2022-06-13 21:49:39.343780
# Unit test for function main
def test_main():
    from httpie.cli.definition import parser
    from httpie.context import Environment
    from httpie.plugins.manager import PluginManager
    plugin_manager.__init__(PluginManager())
    args = parser.parse_args(args=[], env=Environment())
    main(args=args, env=Environment())


if __name__ == "__main__":
    main()

# Generated at 2022-06-13 21:49:49.694678
# Unit test for function main
def test_main():
    import os
    import requests
    import pytest
    from httpie import ExitStatus

    env = os.environ.copy()
    # Setup test urls
    test_urls = [
        "https://www.google.com",
        "https://www.yahoo.com",
        "https://www.wikipedia.org"
    ]

    # Check if url is responding
    def check_url(link):
        try:
            r = requests.head(link)
            return r.status_code == 200
        except Exception as e:
            return False

    # Test urls to see if they are working
    url_status = [check_url(link) for link in test_urls]
    assert all(url_status)

    # Test for encoding

# Generated at 2022-06-13 21:49:54.414012
# Unit test for function program
def test_program():
    args = parser.parse_args(
        args=['http://example.org'],
        env=Environment()
    )
    result = program(args=args)
    assert result == ExitStatus.SUCCESS

# Generated at 2022-06-13 21:50:01.547671
# Unit test for function program
def test_program():
    from httpie.cli.definition import parser

    parsed_args = parser.parse_args([
        '--user', 'test:test',
        '--headers', 'Accept-Encoding:gzip',
        'https://www.baidu.com/'
    ])

    class MockStdout(object):
        def __init__(self):
            self.buffer = None

    class MockRequest(object):
        def __init__(self, raw):
            self.raw = raw

    class Request1(object):
        status = 200
        reason = 'OK'
        headers = {}
        body = '123'

    class Request2(object):
        status = 201
        reason = 'Unsupported'
        headers = {}
        body = '456'


# Generated at 2022-06-13 21:50:13.290713
# Unit test for function main
def test_main():
    import os
    import sys
    from httpie.cli.definition import parser

    # Creates a test directory to store the mock configuration
    test_dir = 'tmp/'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    # Creates a mock configuration directory to store .httpie configuration file.
    config_file = test_dir + '.httpie'