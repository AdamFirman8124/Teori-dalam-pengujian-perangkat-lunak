

# Generated at 2022-06-13 21:05:02.069278
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    help_flag = ['-h']
    assert HTTPieArgumentParser.parse_args(help_flag).help == True


# Generated at 2022-06-13 21:05:06.673536
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([])
    assert args.headers == {}
    assert args.params == {}
    assert args.data == {}
    assert args.files == {}

# Generated at 2022-06-13 21:05:11.026601
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ["https://httpbin.org/post", "foo=bar", "--json", "--form", "--pretty=all", "--download", "--output=test.json", "--auth=admin:admin"]
    parser = HTTPieArgumentParser()
    parser.parse_args(args)

# Generated at 2022-06-13 21:05:19.483630
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = parser.parse_args(['--verbose',
                              'GET',
                              'google.com',
                              'q==helloworld',
                              '--headers',
                              'Accept:"text/html"',
                              'User-Agent:"Chrome"'
                              ])
    assert args.verbose == True
    assert args.method == 'GET'
    assert args.url == 'google.com'
    assert args.headers == {'Accept':'text/html', 'User-Agent':'Chrome'}
    assert args.request_items == [KeyValueArg(key='q', value='helloworld')]
    assert args.json == False



# Generated at 2022-06-13 21:05:23.006213
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    unit = HTTPieArgumentParser()
    args = unit.parse_args()
    assert args

# Generated at 2022-06-13 21:05:33.879666
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([])
    assert isinstance(args, argparse.Namespace)

from math import ceil
from datetime import timedelta
from ..__about__ import __version__
from ..progress.bar import (
    TransferData,
    Bar,
    DownloadBar,
    UploadBar,
    BarFinished,
)
from ..progress.helpers import (
    is_hidden,
    get_render_width,
)
from ..progress.mixins import (
    TransferSpeed,
    TransferTimestamps,
    TransferEncoding,
    TransferAutoDisplay,
)
from ..progress.file import (
    FileTransferSpeed,
    FileTransferTimestamps,
    FileTransferEncoding,
    FileTransferAutoDisplay,
)

# Generated at 2022-06-13 21:05:37.015056
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args()
from urllib.parse import urlparse
from pathlib import Path
import argparse

# Generated at 2022-06-13 21:05:45.695195
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser._parse_args = MagicMock()
    # httpie(1) with no arguments
    input_args = []
    args = parser.parse_args(input_args)
    # parser._parse_args.assert_called_with()
    assert args is parser._parse_args.return_value 
    parser._parse_args.assert_called_with(args=input_args)


# Generated at 2022-06-13 21:05:54.383751
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Import libraries
    import sys
    # Define objects
    stdout_file = open('HTTPie/test_data/test_HTTPie/stdout_file.out', 'bw')
    stdin_file = open('HTTPie/test_data/test_HTTPie/stdin_file.in', 'br')
    # Create argument parser
    parser = HTTPieArgumentParser(session=None)
    # Create fake sys.stdin, sys.stdout and sys.stderr
    sys.stdout = stdout_file
    sys.stdin = stdin_file
    sys.stderr = stdout_file
    # Test method with default arguments
    args = parser.parse_args()
    # Assert

# Generated at 2022-06-13 21:06:09.225778
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([])
    assert args.verbose == False
    assert args.traceback == False
    assert args.output_file == None
    assert args.output_file_specified == False
    assert args.output_options == None
    assert args.output_options_history == None
    assert args.download == False
    assert args.download_resume == False
    assert args.download_all == False
    assert args.prettify == None
    assert args.form == False
    assert args.download_rate_limit == None
    assert args.download_rate_time_window == None
    assert args.stream == False
    assert args.print_body_on_error == False
    assert args.is_windows == True
    assert args.ignore_stdin == False


# Generated at 2022-06-13 21:07:33.333567
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argument_parser = HTTPieArgumentParser(prog='http')
    args = httpie_argument_parser.parse_args(['--help'])
    assert args.command == 'help'
    args = httpie_argument_parser.parse_args(['--version'])
    assert args.command == 'version'
    args = httpie_argument_parser.parse_args(['-v'])
    assert args.command == 'version'
    args = httpie_argument_parser.parse_args(['httpbin.org'])
    assert args.command == 'httpbin.org'
    args = httpie_argument_parser.parse_args(['localhost:8080'])
    assert args.command == 'localhost:8080'
    args = httpie_argument_parser.parse_args(['post'])


# Generated at 2022-06-13 21:07:36.521138
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    assert 1==1

# Class for unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:48.373264
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with pytest.raises(SystemExit):
        parser = HTTPieArgumentParser()
        parser.parse_args([])
    parser = HTTPieArgumentParser()
    r = parser.parse_args(['httpbin.org'])
    assert r.url == 'httpbin.org'
    r = parser.parse_args(['-A', 'Basic', 'localhost'])
    assert r.auth == 'Basic'
    assert r.auth_type == 'basic'
    r = parser.parse_args(['-a', 'foo:bar', 'localhost'])
    assert r.auth == 'foo:bar'
    assert r.auth_type == 'basic'
    
    with pytest.raises(SystemExit):
        parser.parse_args(['-a', ':', 'localhost'])

# Generated at 2022-06-13 21:07:58.053722
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # Args:
    #    parser_args (dict): a dictionary of argument as expected by HTTPieArgumentParser.__init__(). Note that at least a "prog" value is needed.
    #    argv (list): the CLI arguments list to parse.
    #
    # Returns:
    #    an HTTPieArgumentParser instance.
    #
    # Raises:
    #    unittest.case.SkipTest: if any of the required arguments are missing from the arguments list.
    #    AssertionError: if any of the parsed arguments values is incorrect.
    #
    def parse_args_tester(parser_args, argv):

        # Check for missing arguments
        assert "prog" in parser_args, "missing parser_args['prog'] argument"

# Generated at 2022-06-13 21:08:08.925956
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args()
    eq_(args.headers, [])
    eq_(args.compress, True)
    eq_(args.debug, False)
    eq_(args.download, False)
    eq_(args.download_resume, False)
    eq_(args.form, False)
    eq_(args.headers, [])
    eq_(args.ignore_stdin, False)
    eq_(args.prettify, "all")
    eq_(args.print_headers, False)
    eq_(args.timeout, DEFAULT_TIMEOUT_SECONDS)
    eq_(args.traceback, False)
    eq_(args.verbose, False)

# Generated at 2022-06-13 21:08:14.429678
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Env()
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args(['--json', '{}', 'https://google.com'])
    assert args.json == '{}'


# Generated at 2022-06-13 21:08:19.449510
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with pytest.raises(SystemExit, match='2'):
        parser = HTTPieArgumentParser()
        parser.main()
import random
import pytest


# Generated at 2022-06-13 21:08:22.927200
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(desc=None, prog=None, usage=None)
    # parser.parse_args([])


# ============================================================================
# class HTTPiePlugin
# ============================================================================

# Generated at 2022-06-13 21:08:28.793912
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['http', '--timeout=123', 'http://httpie.org/']

    env = MockEnvironment()
    parser = HTTPieArgumentParser(prog=PROGRAM_NAME, env=env, env_prefix=ENV_PREFIX)
    args = parser.parse_args(args)

    assert args.timeout == 123
    assert args.url == 'http://httpie.org/'



# Generated at 2022-06-13 21:08:44.021094
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    import io
    import tempfile

    stdout = sys.stdout
    stderr = sys.stderr
    stdin = sys.stdin
    try:
        stdout_bytes_io = sys.stdout = io.BytesIO()
        stderr_bytes_io = sys.stderr = io.BytesIO()
        sys.stdin = tempfile.TemporaryFile()
        with pytest.raises(ParseError):
            args = parser.parse_args([])
        sys.stdout = stdout
        sys.stderr = stderr
        sys.stdin = stdin
    except Exception:
        sys.stdout = stdout
        sys.stderr = stderr
        sys.stdin = stdin

# Generated at 2022-06-13 21:10:18.809873
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['--verify=no', '--json', '--print=bBhH', '--auth', 'user:password', '--proxy=http://127.0.0.1:8081', 'http://httpbin.org/headers', 'Host:httpbin.org', 'User-Agent:HTTPie/0.9.9']

    parser = HTTPieArgumentParser()
    parsed_args = parser.parse_args(args)

    assert parsed_args.auth_plugin is not None
    assert parsed_args.auth_plugin._username == 'user'
    assert parsed_args.auth_plugin._password == 'password'
    assert parsed_args.auth_type == 'basic'
    assert parsed_args.prettify == 'all'
    assert parsed_args.output_options == 'bBhH'

    assert parsed

# Generated at 2022-06-13 21:10:21.607150
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # parser.parse_args([])
    parser.parse_args(['http', '--version'])



# Generated at 2022-06-13 21:10:33.775897
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    obj = HTTPieArgumentParser()
    # Call method
    obj.parse_args(["/usr/lib/python3.6/httpie/plugins/json/__init__.py"])
    # Check for failure when unexpected keyword argument specified
    try:
        obj.parse_args(["/usr/lib/python3.6/httpie/plugins/json/__init__.py"],
                       invalid_argument=True)
    except TypeError:
        assert True
    else:
        assert False
    # Check for failure when incorrect argument specified
    try:
        obj.parse_args(["invalid_file_path"])
    except SystemExit:
        assert True
    else:
        assert False
    # Check for failure when invalid flag specified

# Generated at 2022-06-13 21:10:37.342117
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    print(parser.parse_args_ensure_exit(['-k', '--auth-type', 'basic', 'user:password@localhost']))
    assert False, "HTTPieArgumentParser.parse_args not implemented"


# Generated at 2022-06-13 21:10:48.274136
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    test_parser = HTTPieArgumentParser()
    args = test_parser.parse_args(['www.google.com', 'GET'])
    assert args.url == 'http://www.google.com'
    assert args.method == 'GET'
    assert test_parser.format_options == test_parser.PARSED_DEFAULT_FORMAT_OPTIONS

    args = test_parser.parse_args(['www.google.com', 'GET', '--json'])
    assert args.url == 'http://www.google.com'
    assert args.method == 'GET'
    assert args.json == True
    assert args.headers == None
    assert args.data == None
    assert isinstance(test_parser.format_options, dict)

# Generated at 2022-06-13 21:10:55.666046
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Unit test for method parse_args of class HTTPieArgumentParser"""

    parser = HTTPieArgumentParser()
    args = parser.parse_args([])

    assert args.headers is None
    assert args.traceback is False
    assert args.form is False
    assert args.verify is True
    assert args.follow_redirects is True
    assert args.max_redirects is 10
    assert args.timeout is None
    assert args.check_status is True
    assert args.download is False
    assert args.download_resume is False
    assert args.download_flat is False
    assert args.output_file is None
    assert args.output_file_specified is False
    assert args.output_options is None
    assert args.output_options_history is None
    assert args.prettify is PRETTY

# Generated at 2022-06-13 21:11:07.513232
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """ Unit test for the method parse_args of class HTTPieArgumentParser """
    # pylint: disable=protected-access, 
    httpieargumentparser = HTTPieArgumentParser()
    # Test good arguments
    httpieclient = httpieargumentparser.parse_args(
        ['http', 'http://echo.jpillora.com', 'hello=world'])
    assert httpieclient.args.url == 'http://echo.jpillora.com'
    assert httpieclient.args.auth == None
    assert httpieclient.args.headers == []
    assert httpieclient.args.params == []
    assert httpieclient.args.files == {}
    assert httpieclient.args.data == [b'hello=world']
    assert httpieclient.args.output_file == None

    # Test bad

# Generated at 2022-06-13 21:11:18.329186
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:11:23.712441
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
	a= HTTPieArgumentParser()
	a.debug = 1
	a.parse_args("google.com".split())

# Generated at 2022-06-13 21:11:31.732576
# Unit test for method parse_args of class HTTPieArgumentParser