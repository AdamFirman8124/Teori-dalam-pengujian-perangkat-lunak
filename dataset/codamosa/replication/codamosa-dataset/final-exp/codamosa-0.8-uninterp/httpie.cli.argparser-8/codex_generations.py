

# Generated at 2022-06-13 21:05:10.531927
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # test with an empty argument list
    test_args = []
    parser = HTTPieArgumentParser()
    parser.parse_args(test_args)
    assert parser.args.method == None
    assert parser.args.url == None
    assert len(parser.args.request_items) == 0
    assert parser.args.headers == {}
    assert parser.args.data == {}
    assert parser.args.files == {}
    assert len(parser.args.args) == 0
    assert parser.args.form == False
    assert parser.args.output_file == None
    assert parser.args.output_options == 'hb'
    assert parser.args.output_options_history == 'hb'
    assert parser.args.verbose == 0
    assert parser.args.all == False

# Generated at 2022-06-13 21:05:21.049375
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(env=Environment())
    args = parser.parse_args([
        'http://httpbin.org/headers',
        'Accept:text/plain',
        'x-test:X-Test-Value',
        '--headers',
        'user-agent:httpie-test'
    ])
    assert args.url == 'http://httpbin.org/headers'
    assert args.headers == {'accept': 'text/plain', 
                            'x-test': 'X-Test-Value',
                            'user-agent': 'httpie-test'}
    assert args.headers_templatized == {'accept': 'text/plain', 
                            'x-test': 'X-Test-Value',
                            'user-agent': 'httpie-test'}

# Generated at 2022-06-13 21:05:33.266735
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['-h']
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args)
    assert args.output_options == 'h'
    assert args.output_options_history == 'H'
    assert parser.has_stdin_data == False
    assert isinstance(parser.args, argparse.Namespace)
    assert isinstance(parser.env, Environment)
    assert isinstance(parser.req_file_writer, RequestFileWriter)
    assert isinstance(parser.req_file_writer.raw_stream, RawStream)
    assert args.session_read_file == None
    assert args.session_write_file == None
    assert isinstance(args.session_name, UUID)
    assert args.verbosity == 0
    assert args.debug_traceback == False

# Generated at 2022-06-13 21:05:37.326761
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  # Input
  argv = []
  # Expected output
  expected = None
  # Output
  actual = HTTPieArgumentParser().parse_args(argv)
  # Test
  assert actual == expected

# Generated at 2022-06-13 21:05:41.664282
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args()
    assert args.auth == None
    assert args.auth_type == None

# Generated at 2022-06-13 21:05:51.651881
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    import mock
    from httpie.core import __version__
    from httpie.core import main
    from httpie import ExitStatus

    # Patch sys.argv so that we don't spam the commandline with our test
    # command.
    with mock.patch.object(sys, 'argv', ['httpie', '-vvvv']):
        # Construct a mocked argument parser so we can skip actual argument parsing
        parser = mock.Mock()
        parser.parse_args = mock.Mock()
        parser.parse_args.return_value = mock.Mock()
        parser.parse_args.return_value.method = 'GET'
        parser.parse_args.return_value.headers = None
        parser.parse_args.return_value.ignore_stdin = False
        parser.parse_args.return_

# Generated at 2022-06-13 21:06:04.778120
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # arrange
    args = ['--download', '--output=/dev/null', '--http2', 'GET', 'http://www.example.com']
    parser = HTTPieArgumentParser(prog='test_parse_args', env=Environment())
    parser.add_argument('--http1', action='store_true', help='Use HTTP/1.1.')
    parser.add_argument('--http2', action='store_true', help='Use HTTP/2.')
    parser.add_argument('--download', action='store_true', help='Download the body.')
    parser.add_argument('--output', type=str, help='Output to a file.')
    parser.add_argument('method', choices=['GET', 'POST'])
    parser.add_argument('url')
    # act

# Generated at 2022-06-13 21:06:15.340217
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # type: () -> None
    
    parser = HTTPieArgumentParser()
    # Set argument for test
    http = 'http'
    url = 'httpbin.org'
    stdin = ''
    # Parse argument
    args = parser.parse_args([http, url, '-', '-j', '-A', 'curl/7.60.0', '-b', 'foo=bar;baz=qux', '-H', 'Accept: application/json', '-h', 'Content-Type: application/json', '-h', 'Content-Length: 42', '-X', 'POST', '-d', '{ "foo": "bar", "baz": "qux" }', '-f', '-a', 'tester:pass'])
    # Check argument result

# Generated at 2022-06-13 21:06:26.034849
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.main import HTTPieArgumentParser

# Generated at 2022-06-13 21:06:29.908786
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([])
    assert isinstance(args, argparse.Namespace)



# Generated at 2022-06-13 21:07:24.171406
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test if it can parse a list of command line args
    (options, args) = HTTPieArgumentParser.parse_args(
        ['--form', '--pretty=all', '/'])
    assert options.prettify == PRETTY_MAP['all']
    
    # Test if it can parse a list of command line args
    (options, args) = HTTPieArgumentParser.parse_args(
        ['--form', '--pretty=all', '--ignore-stdin', '/'])
    assert options.prettify == PRETTY_MAP['all']
    


# Generated at 2022-06-13 21:07:34.015579
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # a. Create a mock object of HTTPieArgumentParser
    mock_HTTPieArgumentParser = copy.deepcopy(HTTPieArgumentParser)
    
    # b. Assign attributes of HTTPieArgumentParser
    # mock_HTTPieArgumentParser.args = Mock()
    # mock_HTTPieArgumentParser.args.traceback = False
    # mock_HTTPieArgumentParser.args.verbose = False
    # mock_HTTPieArgumentParser.args.debug = False
    mock_HTTPieArgumentParser.args.method = None
    mock_HTTPieArgumentParser.args.url = None
    # mock_HTTPieArgumentParser.args.auth = None
    # mock_HTTPieArgumentParser.args.auth_type = None
    mock_HTTPieArgumentParser.args.headers = []
    # mock

# Generated at 2022-06-13 21:07:46.663578
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = Namespace(auth=None, auth_type=None, cert=None, config_dir=None,
        data='', download=False, files=None, form=False, headers={}, 
        insecure=False, output_file=None, output_file_specified=False,
        output_options=None, output_options_history=None, 
        method=None, params={}, request_items=None, 
        traceback=False, url='http://localhost:5000/api/v1/payments')
    args = HTTPieArgumentParser().parse_args(args=args)
    assert args.auth is None
    assert args.auth_type is None
    assert args.cert is None
    assert args.config_dir is None
    assert args.data == ''
    assert args.download is False
    assert args.files

# Generated at 2022-06-13 21:07:56.981462
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    from httpie.input import SEP_CREDENTIALS
    from httpie.plugins import plugin_manager
    plugin_manager.load_builtin_plugins()
    # FIXME: Can't use `sys.modules[__name__]` as `_module` in order to mock
    # `env.stdout.isatty` because it causes issues on Python 3.4.
    parser = HTTPieArgumentParser(_module='httpie.cli')

# Generated at 2022-06-13 21:07:58.957154
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # TODO:
    assert parser.parse_args([]) == parser.parse_args([])
    pass
#############################################################################



# Generated at 2022-06-13 21:08:10.096575
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser_with_kargs = HTTPieArgumentParser(
        prog='http',
        epilog=EPILOG,
        add_help=False,
        formatter_class=CustomHelpFormatter,
        # arguments
        default_options=[],
        env=Environment(),
        stdin=None,
    )

    class FakeArgs(structs.Arguments):
        def __getattr__(self, item):
            super(FakeArgs, self).__getattr__(item)

    args = FakeArgs()
    args.headers = [parse_key_val_arg('Content-Type: application/xml')]
    args.data = [parse_key_val_arg('key=value')]
    args.files = {
        '': ('filename', 'filepath')
    }

# Generated at 2022-06-13 21:08:20.694902
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Test HTTPieArgumentParser.parse_args method"""
    argument_parser = HTTPieArgumentParser()
    result = argument_parser.parse_args([])
    assert result.headers == {}
    assert result.auth is None
    assert result.download is False
    assert result.download_resume is False
    assert result.form is False
    assert result.ignore_netrc is False
    assert result.ignore_stdin is False
    assert result.json is False
    assert result.method is None
    assert result.multipart_data == []
    assert result.output_file is None
    assert result.output_file_specified is False
    assert result.output_options is None
    assert result.output_options_history is None
    assert result.params == {}
    assert result.prettify == PRETTY_STDOUT_

# Generated at 2022-06-13 21:08:25.608880
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    
    parser_output = HTTPieArgumentParser.parse_args(['https://www.google.com/'])
    assert isinstance(parser_output, argparse.Namespace)
    
    
    

# Generated at 2022-06-13 21:08:30.093237
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['http', '-v', 'httpbin.org/get'])
    assert args.verbose == 1
    args = parser.parse_args(['http', '--verbose', 'httpbin.org/get'])
    assert args.verbose == True


# Generated at 2022-06-13 21:08:32.394608
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie = HTTPieArgumentParser(None, None, None)
    if hasattr(httpie, 'parse_args'):
        httpie.parse_args()
    
test_HTTPieArgumentParser_parse_args()
from requests.exceptions import MissingSchema

from httpie.client import HTTPieRequest
from httpie.plugins import plugin_manager
from httpie.session import *



# Generated at 2022-06-13 21:10:05.539561
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    cases = [
        # case 1
        # (
        #     [
        #
        #     ],
        #     "",  # expected
        # ),
        # case 2
        # (
        #     [
        #
        #     ],
        #     "",  # expected
        # ),
        # case 3
        # (
        #     [
        #
        #     ],
        #     "",  # expected
        # ),
    ]
    for args, expected in cases:
        assert expected == HTTPieArgumentParser(*args).parse_args()
 

# Generated at 2022-06-13 21:10:10.284626
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(False, True)
    args = parser.parse_args(['--form', 'foo=bar'], env=None)
    assert args.form
# class RequestItems

# Generated at 2022-06-13 21:10:17.860891
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.core import main as core_main
    from httpie.core import main_help as core_main_help

    # Set the `--version` flag for the run
    sys.argv.append('--version')
    # Run the main function for `http`
    core_main()

    # Set the `--help` flag for the run
    sys.argv.append('--help')
    # Run the `main_help` function for `http`
    core_main_help()

# Generated at 2022-06-13 21:10:18.489831
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:10:27.971437
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test with an empty list
    args = []
    env = Environment(stdout_isatty=True, stdin_isatty=True, stderr_isatty=True)
    with pytest.raises(SystemExit):
        HTTPieArgumentParser().parse_args(args, env)
    # Test with a valid list of arguments
    args = ['--help']
    env = Environment(stdout_isatty=True, stdin_isatty=True, stderr_isatty=True)
    HTTPieArgumentParser().parse_args(args, env)

# Generated at 2022-06-13 21:10:38.062823
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    print('Testing HTTPieArgumentParser.parse_args()')
    
    argv = [
        '--form', 'foo=bar', 'name@example.com',
        'password:hunter2', 'baz=@example.json',
        '--compress'
    ]
    
    parser = HTTPieArgumentParser()
    args = parser.parse_args(argv)
    assert args.form
    assert args.request_items[0].key == 'username'
    assert args.request_items[0].value == 'name@example.com'
    assert args.request_items[1].key == 'password'
    assert args.request_items[1].value == 'hunter2'
    assert args.files[0].key == 'baz'
    assert args.files[0].filename == 'example.json'

# Generated at 2022-06-13 21:10:48.514939
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # --arg Some value
    def test_1():
        args = HTTPieArgumentParser().parse_args('--arg Some value'.split())
        #print(args)
        assert args.arg == 'Some value'
        assert args.verbose is False


    # --arg=Some value
    def test_2():
        args = HTTPieArgumentParser().parse_args('--arg=Some value'.split())
        assert args.arg == 'Some value'
        assert args.verbose is False


    # --auth-type=basic
    def test_3():
        args = HTTPieArgumentParser().parse_args('--auth-type=basic'.split())
        assert args.auth_type == 'basic'
        assert args.verbose is False


    # --auth-type basic
    def test_4():
        args

# Generated at 2022-06-13 21:10:51.290031
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass
    # Need to test httpie.cli.parser.parse_args
if __name__ == "__main__":
    test_HTTPieArgumentParser_parse_args()

# Methods from class HTTPieHelpFormatter

# Generated at 2022-06-13 21:11:02.724048
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args(['--help'])
    parser.parse_args(['httpbin.org'])
    parser.parse_args(['--version'])
    parser.parse_args(['--verbose'])
    parser.parse_args(['--verbose','httpbin.org','status','200'])
    parser.parse_args(['--debug'])
    parser.parse_args(['--headers'])
    parser.parse_args(['--b','--'])
    parser.parse_args(['--body-only'])
    parser.parse_args(['--pretty','all'])
    parser.parse_args(['httpbin.org','--pretty=all'])
    parser.parse_args(['--style','solarized'])

# Generated at 2022-06-13 21:11:06.064751
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: make HTTPieArgumentParser() become a unittest.mock
    # to properly test this
    pass

