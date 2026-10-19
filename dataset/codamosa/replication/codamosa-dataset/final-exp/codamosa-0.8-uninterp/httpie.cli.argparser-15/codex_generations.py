

# Generated at 2022-06-13 21:05:03.486011
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(args=['http://localhost:8000/', 'key=value'])
    assert args.url == 'http://localhost:8000/'
    assert args.request_items == [('key', 'value')]

# Generated at 2022-06-13 21:05:14.402816
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(
        ['http','GET','http://github.com','name==John','age==10'])
    assert args.verbose == False
    assert args.output_file == None
    assert args.json == None
    assert args.no_json_cls == False
    assert args.stream == False
    assert args.check_status == False
    assert args.headers == []
    assert args.style == 'colors'
    assert args.print_body_only == False
    assert args.pretty == 'all'
    assert args.download == False
    assert args.download_resume == False
    assert args.output_options == 'HBS'
    assert args.output_options_history == 'HBS'
    assert args.method == 'GET'

# Generated at 2022-06-13 21:05:27.298754
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Install argparse mock into HTTPieArgumentParser.
    HTTPieArgumentParser._parse_args = lambda self: None
    args = unittest.mock.MagicMock()
    args.headers = args.data = args.files = args.params = args.multipart_data = None
    args.form = False
    args.output_file = None
    args.output_file_specified = False
    args.download = False
    args.download_resume = False
    args.output_options = None
    args.output_options_history = None
    args.prettify = False
    args.style = None
    args.format = False
    args.print_headers = False
    args.print_body = False
    args.download_headers = False
    args.verbose = False
    args.offline

# Generated at 2022-06-13 21:05:35.575162
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    dut = HTTPieArgumentParser()
    dut.add_argument('--output-file', type=str, nargs='?', default=None, action=argparse.FileType('wb'))
    dut.add_argument('--output-options', type=str, nargs='?', default=None, dest='output_options')
    dut.add_argument('--output-options-history', type=str, nargs='?', default=None, dest='output_options_history')
    dut.add_argument('--region', type=str, default=None)
    dut.add_argument('--method', type=str, default=None)
    dut.add_argument('--no-check-status', action='store_true')

# Generated at 2022-06-13 21:05:38.646873
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
   # Test HTTPieArgumentParser().parse_args()
   parser = HTTPieArgumentParser(prog='http')
   args = parser.parse_args(['httpie.org'])
   assert args.url == 'httpie.org'


# Generated at 2022-06-13 21:05:40.259052
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:05:50.709110
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    os.environ['http_proxy'] = '192.168.0.1:3128'
    os.environ['https_proxy'] = '192.168.0.1:3128'
    os.environ['no_proxy'] = 'example.org'

# Generated at 2022-06-13 21:05:52.235002
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args([])


# Generated at 2022-06-13 21:06:05.822281
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('-v','--verbose',action='store_true')
    parser.add_argument('--version',action='version', version='test')
    parser.add_argument('url', nargs='?',action='store')
    parser.add_argument('method', nargs='?',action='store')
    parser.add_argument('items', nargs='*',action='store')
    arguments = ['httpbin.org/get', '-v', 'GET', 'a=1', 'b=2']
    namespace = parser.parse_args(arguments)
    print(namespace.url)
    print(namespace.method)
    print(namespace.items)

# test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:06:15.818351
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie = HTTPieArgumentParser()
    parser = httpie.parse_args(['--method','GET','--url','127.0.0.1','--headers','Accept:application/json','--auth','test:test'])
    assert parser.method == 'GET'
    assert parser.url == 'http://127.0.0.1'
    assert 'Accept' in parser.headers
    assert parser.headers['Accept'] == 'application/json'
    assert parser.auth.username == 'test'
    assert parser.auth.password == 'test'

test_HTTPieArgumentParser_parse_args()

HTTPIE_VERSIONS = (VERSION, __version__)
REQUIRED_VERSIONS = (2, 3)

# Generated at 2022-06-13 21:07:02.939139
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with HTTMock(mock_api_request):

        http_program = HTTPieProgram()
        http_program.args = http_program.parser.parse_args(["http", "https://api.github.com/test"])
        assert http_program.args.method == "GET"
        assert http_program.args.url == "https://api.github.com/test"
        assert http_program.args.config_dir == pathlib.Path.home() / '.httpie'
        assert http_program.args.default_options == []
        assert http_program.args.debug is False
        assert http_program.args.download is False
        assert http_program.args.download_resume is False
        assert http_program.args.follow is False
        assert http_program.args.form is False
        assert http_

# Generated at 2022-06-13 21:07:12.533587
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class RequestGet(Request):
        method = 'GET'
        url = 'http://httpbin.org/get'
        headers = {'Accept': 'application/json'}
        cookies = {'foo': 'bar'}
        auth = ('user', 'pass')
        allow_redirects = True
        
    # TODO: Add test to verify behavior is as expected.
    try:
        # Instantiate the parser
        my_parser = HTTPieArgumentParser()
        results = my_parser.parse_args()
        #results = my_parser.print_help()
        assert results.url == 'REQUIRED'
    except SystemExit:
        assert 1 == 1


# Generated at 2022-06-13 21:07:20.503332
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(env=TestEnvironment())
    args = parser.parse_args(['https://httpbin.org/get'])
    assert args.url == 'https://httpbin.org/get'
    assert args.verbose == False
    assert args.headers == ['Accept: */*', 'Accept-Encoding: gzip, deflate', 'User-Agent: HTTPie/0.9.3']


test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:07:30.673105
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with mock.patch("sys.argv") as argv:
        argv.__getitem__.return_value = 'httpie.exe'
        argv.__len__.return_value = 1
        args = HTTPieArgumentParser().parse_args()

# Generated at 2022-06-13 21:07:44.569382
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Mock
    class MockClass(object):
        pass

    mock_args = MockClass()
    mock_args.url = 'https://httpie.org'
    mock_args.output_file = sys.stdout
    mock_args.headers = []
    mock_args.output_file_specified = False
    mock_args.download = False
    mock_args.quiet = False
    mock_args.auth_plugin = None
    mock_args.auth = None
    mock_args.ignore_netrc = False
    mock_args.auth_type = None
    mock_args.method = None
    mock_args.json = False
    mock_args.form = False
    mock_args.output_options = None
    mock_args.output_options_history = None
    mock_args.headers = []
    mock

# Generated at 2022-06-13 21:07:55.535726
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with pytest.raises(SystemExit):
        HTTPieArgumentParser().parse_args([])
    # simple test
    http = HTTPie(['mockbin.org', 'GET'])
    assert len(http.args.request_item_args) == 1
    assert http.args.url == 'mockbin.org'
    assert http.args.verbose == False
    assert http.args.traceback == False
    assert http.args.method == 'GET'
    assert http.args.request_items == []
    assert http.args.headers == {}
    assert http.args.data == {}
    assert http.args.files == {}
    assert http.args.params == {}
    assert http.args.multipart_data == {}
    assert http.args.json == None

# Generated at 2022-06-13 21:07:57.694416
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args_parser = HTTPieArgumentParser()
    args = args_parser.parse_args(['--help'])
    assert args.help
    assert args.method is None


# Generated at 2022-06-13 21:08:03.316457
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    test_HTTPieArgumentParser_parse_args()
    """
    # Some dummy class that only has a parser attribute
    class TestClass(object):
        pass
    test_class = TestClass()
    # Get the HTTPieArgumentParser instance for parsing arguments
    parser = HTTPieArgumentParser(env=Environment(),
                                  stdin=None, stdout=None, stderr=None)
    test_class.parser = parser
    # Test if httpie.cli.parser.parse_args returns a parsed namespace
    test_class.args = parser.parse_args()
    assert isinstance(test_class.args, argparse.Namespace)

    # Test if httpie.cli.parser.parse_args returns a parsed namespace
    # when called with the HTTPieArgumentParser instance and
    # the user inputs '-

# Generated at 2022-06-13 21:08:11.701320
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.compat import is_windows
    from httpie.plugins import AuthPlugin, plugin_manager
    from httpie.plugins.builtin import HTTPBasicAuth

    class MockAuthPlugin(AuthPlugin):
        auth_type = 'mock'

    class MockWindowsAuthPlugin(AuthPlugin):
        auth_type = 'mock-windows'
        auth_require = True
        netrc_parse = True

    parser = HTTPieArgumentParser(env=Environment())
    assert isinstance(parser.add_argument, Callable)
    assert isinstance(parser.add_mutually_exclusive_group, Callable)
    assert isinstance(parser.add_argument_group, Callable)

    plugin_manager.register(MockAuthPlugin)
    if is_windows:
        parser.windows_legacy_auth_plugin = MockWindowsAuth

# Generated at 2022-06-13 21:08:27.755542
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test case:
    http --https-port=4000 localhost:3000
    http --auth=user:password --auth-type=digest localhost:3000
    http --ignore-stdin --auth=user:password --form POST localhost:3000 hello=world
    """
    import argparse
    from httpie.core import main
    from httpie.context import Environment
    from httpie.settings import __version__ as version

# Generated at 2022-06-13 21:10:00.793788
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser(prog = "ut-prog",
                                config_dir = "ut-config")
    arg_list = ["https://httpie.org",
                "Content-Type:application/json",
                "q=httpie"]
    params = args.parse_args(arg_list)
    assert params.url == "https://httpie.org"
    assert params.headers == [("Content-Type", "application/json")]
    assert params.data == [("q", "httpie")]

# Generated at 2022-06-13 21:10:08.869486
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:10:19.776865
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    resp = parser.parse_args(
        ['-p', '--form', 'url=http://example.com', 'foo=bar'],
    )
    assert resp.auth is None
    assert resp.auth_type is None
    assert resp.body is None
    assert not resp.body_as_form
    assert not resp.body_as_json
    assert resp.download == False
    assert resp.download_resume == False
    assert len(resp.files) == 0
    assert not resp.form
    assert not resp.follow
    assert not resp.ignore_netrc
    assert not resp.ignore_stdin
    assert resp.include == False
    assert resp.max_redirects == None
    assert resp.method == 'GET'
    assert resp.output_file is None

# Generated at 2022-06-13 21:10:31.759351
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:10:39.086392
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    print(parser.parse_args(['http://url.com', 'dict:a:1']))
    print(parser.parse_args(['http://url.com', 'dict:a:1', 'dict:b:2']))
    print(parser.parse_args(['http://url.com', 'dict:a:1', 'dict:b:2', '--form']))
    print(parser.parse_args(['dict:a:1', 'dict:b:2', '--form']))
 
#test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:10:44.654835
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(env=Environment())
    args = parser.parse_args(['http', 'GET', 'http://www.test.com'])
    assert args.url == 'http://www.test.com'
    assert args.method == 'GET'


# Generated at 2022-06-13 21:10:53.423304
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
	from tempfile import TemporaryDirectory


# Generated at 2022-06-13 21:11:05.369443
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Unit test for method parse_args of class HTTPieArgumentParser"""

    try:
        from httpie import client
        from httpie.input import get_response_stream
        from httpie.plugins.builtin import HTTPBasicAuth
        from httpie.plugins.builtin import HTTPTokenAuth
        from httpie.plugins.builtin import HTTPDigestAuth
    except ImportError:
        print('Module httpie is required to run this test')
        raise
    except Exception as exp:
        print('Unexpected exception raised, this should not happen in unit test')
        raise

    # Test with no args
    args = client.parse_args([])
    assert not args.output_file
    assert not args.output_options
    assert not args.output_options_history
    assert not args.headers
    assert not args.data
   

# Generated at 2022-06-13 21:11:11.487602
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # learn about a class
    mock_class = create_autospec(HTTPieArgumentParser)
    # use the class to create objects
    mock_instance = mock_class()
    mock_instance.parse_args(['--pretty=all', 'http', '--help'])
    # test the class
    mock_class.assert_called_once()

# Generated at 2022-06-13 21:11:20.450275
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argparse_instance = HTTPieArgumentParser()
    default_args = httpie_argparse_instance.parse_args('')
    assert default_args.format_options == {
        'colors': DEFAULT_COLORS,
        'style': DEFAULT_STYLE,
        'format': DEFAULT_FORMAT,
        'headers': DEFAULT_HEADERS,
        'indent': DEFAULT_INDENT,
        'separators': DEFAULT_SEPARATORS,
        'verify': DEFAULT_VERIFY,
    }
    assert default_args.method is None
    assert default_args.json_indent is None
    default_args = httpie_argparse_instance.parse_args('a b')
    assert default_args.method == 'a'
    assert default_args.url