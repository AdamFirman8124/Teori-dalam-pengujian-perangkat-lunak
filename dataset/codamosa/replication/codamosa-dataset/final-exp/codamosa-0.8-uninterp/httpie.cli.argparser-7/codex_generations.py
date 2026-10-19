

# Generated at 2022-06-13 21:04:56.064770
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['http', 'http://example.com']
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args)
    assert args.url == 'http://example.com'


# Generated at 2022-06-13 21:04:58.296399
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argparser = HTTPieArgumentParser()
    args = httpie_argparser.parse_args([])
    assert isinstance(args, argparse.Namespace)


# Generated at 2022-06-13 21:05:03.656173
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args()
    return args
# If a config file is specified, it's loaded.
# It is then available in config.

# Generated at 2022-06-13 21:05:12.071683
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from click.testing import CliRunner
    from httpie.core import main_impl
    from httpie import core
    from httpie.plugins import builtin
    
    # Set up the core plugin
    core.plugins = builtin.core
    
    # Set up the parser
    parser = HTTPieArgumentParser(env=core.Environment())
    
    # Validate the args are parsed as expected
    args = parser.parse_args(['/'])
    assert args.url == 'http:///'
test_HTTPieArgumentParser_parse_args()
 

# Generated at 2022-06-13 21:05:23.777094
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args_list = ['--verify', 'no', '--json', '--headers', "'Authorization: Basic YXV0aDphdXRo'", 
                '--prettify', 'all', '--timeout', '5', '--output', 'res/Result/saigon.json',
                '-f', '--auth-type', 'basic', 'post', 'https://api.saigon.gov.vn/web/auth/login', 
                'username=thucnn@gmail.com', 'password=Dunglaptrinh123']
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args_list)
    assert args.headers == {'Authorization': 'Basic YXV0aDphdXRo'}
    assert args.auth_type == 'basic'
    assert args

# Generated at 2022-06-13 21:05:24.569840
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:05:34.656328
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:05:47.098075
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--json', '--pretty=all', '--headers', 'GET',
                              'http://example.com/'])
    assert not args.colors
    assert args.json
    assert args.output_options == 'hH'
    assert args.prettify == PRETTY_MAP['all']
    assert args.method == 'GET'
    assert args.debug

    args = parser.parse_args(['--json', '--stream', 'GET', 'http://example.com/'])
    assert args.stream


# Generated at 2022-06-13 21:05:48.432102
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args()

# Generated at 2022-06-13 21:05:53.317949
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = [
        'POST',
        'https://httpbin.org/post',
        'name=John',
        'foo==bar'
    ]
    method, url, request_items = HTTPieArgumentParser.parse_args(args)

    assert method == 'POST'
    assert url == 'https://httpbin.org/post'
    assert request_items == [('name', 'John'), ('foo', '=bar')]


# Generated at 2022-06-13 21:06:30.239901
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['http', 'localhost:8080/api_v1/user'])
    assert type(args) == argparse.Namespace
# Define method parse_args of class CollectingArgumentParser

# Generated at 2022-06-13 21:06:36.751480
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    BaseArgParser = HTTPieArgumentParser
    parser = BaseArgParser()
    fake_args = ['-A', 'test']
    fake_kwargs = {'prog' : 'test_prog', 'debug': True, 'output_file': 'test_output_file'}
    parser._parse_args(fake_args, fake_kwargs)
    assert parser.args.auth == 'test'
    assert parser.args.prog == 'test_prog'
    assert parser.args.debug == True
    assert parser.args.output_file == 'test_output_file'

# Generated at 2022-06-13 21:06:38.517380
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    hp = HTTPieArgumentParser()
    args = hp.parse_args()
print(test_HTTPieArgumentParser_parse_args())


# Generated at 2022-06-13 21:06:43.917402
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie import InputFile

    env = Environment()
    parser = HTTPieArgumentParser(env=env, add_help=False)
    args = parser.parse_args([
        'https://httpbin.org/get',
        'key=value',
        '--form',
        'color=red',
        '--download',
    ])
    assert args.url == 'https://httpbin.org/get'
    assert args.method == 'GET'
    assert args.headers == {'Content-Type': 'application/json'}
    assert args.data == [('key', 'value')]
    assert args.params == {}
    assert args.files == {}
    assert args.json == {}
    assert args.output_file_specified
    assert not args.output_file.closed

# Generated at 2022-06-13 21:06:58.226183
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: Add more tests
    from httpie.core import main
    args = main.parser.parse_args([
        '--json', 'http://example.com', 
        'first_name', '=', 'Jane',
        'last_name', '=', 'Doe', 
        'phone', '=', '+1234567890'
    ])
    assert args.json
    assert args.url == 'http://example.com'

# Generated at 2022-06-13 21:07:10.107571
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(prog='http')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output.')
    parser.add_argument('--version', action='version',
                        version='httpie {0}'.format(__version__))
    parser.add_argument('-h', '--help', action='help',
                        help='Print help information and exit.')
    parser.add_argument('-a', '--auth', metavar='[USERNAME[:PASSWORD]]',
                        help='Specify a username and password for HTTP '
                             'authentication.')
    parser.add_argument('-A', '--auth-type', dest='auth_type',
                        help='Specify the type of HTTP authentication to use.')

# Generated at 2022-06-13 21:07:22.436564
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('-a', '--aaa')
    parser.add_argument('-b', '--bbb')
    parser.add_argument('-c', '--ccc')
    cli_args = parser.parse_args('--aaa 1 --bbb 2 --ccc 3'.split())
    assert cli_args.aaa == '1'
    assert cli_args.bbb == '2'
    assert cli_args.ccc == '3'
    cli_args = parser.parse_args('-a 1 -b 2 -c 3'.split())
    assert cli_args.aaa == '1'
    assert cli_args.bbb == '2'
    assert cli_args.ccc == '3'

# Generated at 2022-06-13 21:07:31.808338
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    if not unittest.case._TextTestResult.showAll:
        unittest.case._TextTestResult.showAll = True
    if not unittest.case._TextTestResult.dots:
        unittest.case._TextTestResult.dots = True
    suite = unittest.TestSuite()
    suite.addTest(HTTPieArgumentParserTestCase("test_parse_args"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:07:42.794269
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args_ = parser.parse_args(['http', '127.0.0.1'])
    expected_args = object()

    parser.error = mock.Mock()
    parser.parse_known_args = mock.Mock(return_value=(expected_args, []))
    assert parser.parse_args(['http', '127.0.0.1']) == expected_args
    parser.parse_known_args.assert_called_once_with(['http', '127.0.0.1'])
    parser.error.assert_not_called()


# Generated at 2022-06-13 21:07:53.906644
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # Test case 1
    args = HTTPieArgumentParser().parse_args([
        'http',
        '--verify',
        'no',
        '--headers',
        "Accept-Encoding: gzip,deflate",
        'GET',
        'http://httpbin.org/ip'
    ])
    # Expected result
    args.verify = False
    args.headers.__setitem__('Accept-Encoding','gzip,deflate')
    args.headers.__setitem__('Accept','*/*')
    args.headers.__setitem__('Accept-Encoding', 'gzip, deflate')
    args.headers.__setitem__('User-Agent', 'HTTPie/0.9.9')
    # Actual result

# Generated at 2022-06-13 21:09:09.892962
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    '''Unit test for method parse_args of class HTTPieArgumentParser'''
    native_mock = mock.MagicMock()
    native_mock.stdout.encoding = 'utf-8'
    native_mock.stdout = sys.stdout
    native_mock.stdin = sys.stdin
    native_mock.argv = ['http', 'g.cn', '-v']
    native_mock.stderr = sys.stderr
    native_mock.stderr_isatty = True
    native_mock.stdout_isatty = True
    native_mock.is_windows = False

    args = HTTPieArgumentParser(env=native_mock).parse_args()
    assert type(args is (argparse.Namespace))


# Generated at 2022-06-13 21:09:16.594086
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from requests.models import RequestEncodingMixin
    
    # Unit tests for the class HTTPieArgumentParser
    #
    # Args:
    #    HTTPieArgumentParser

    # Test case 1
    
    #def __init__(
        #self,
        #stdin=None,
        #stdout=None,
        #stderr=None,
        #env=None,
        #default_options=None,
        #cli_args=None,
        #**kwargs):

    #    if stdin is None:
    #        stdin = io.open(sys.stdin.fileno(), 'rb', closefd=False)
        
    #    env = env or Environment()
    #    kwargs['fromfile_prefix_chars'] = '@'
    #    kwargs['

# Generated at 2022-06-13 21:09:18.476079
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(args=[])
    assert args.get('method') == HTTP_GET

# Generated at 2022-06-13 21:09:28.106072
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Raise an exception if the method is called without params
    try:
        HTTPieArgumentParser().parse_args()
    except Exception as e:
        return e.args[0] == 'the following arguments are required: [url]'

    # Raise an exception if the method is called with more than one positional arguments
    try:
        HTTPieArgumentParser().parse_args(['https://example.com', 'https://example.com'])
    except Exception as e:
        return e.args[0].startswith('too many values to unpack')


# Generated at 2022-06-13 21:09:40.334974
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import io
    import sys
    p = HTTPieArgumentParser()
    # params = {'url': 'https://httpbin.org', 'pretty': 'all', 'output': 'file.json', 'download': True, 'output_options': 'hHb'}
    sys.argv = ['http', '--pretty=all', '--output=file.json', '--download', '--output-options=hHb', 'https://httpbin.org']
    args = p.parse_args()
    assert args.url == 'https://httpbin.org'
    assert args.pretty == 'all'
    assert args.output == 'file.json'
    assert args.download == True
    assert args.output_options == 'hHb'
    assert args.output_options_history == 'hHb'
    
    

# Generated at 2022-06-13 21:09:52.443061
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # ARRANGE #

    # inpout / control
    argv = ['invocation', 'url']
    args = Namespace(request_items=None)

    expected_output = Namespace(
        request_items=[['url']]
    )

    parser = HTTPieArgumentParser()
    parser.add_argument('url', type=str)
    parser.add_argument('request_items', type=RequestItemArgType.from_cli, nargs='*')

    # ACT #
    actual_output = parser.parse_args(argv)

    # ASSERT #
    assert actual_output == expected_output



# Generated at 2022-06-13 21:09:57.739735
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args(): 
    with pytest.raises(SystemExit):
        HTTPieArgumentParser().parse_args()
    args = HTTPieArgumentParser().parse_args(['http://example.com/'])
    assert args.url == 'http://example.com/'


# Generated at 2022-06-13 21:10:00.411037
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Arrange
    parser = HTTPieArgumentParser()
    
    # Act
    args = parser.parse_args()
    
    # Assert
    
    
    

# Generated at 2022-06-13 21:10:08.309109
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:10:19.539987
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    ap = HTTPieArgumentParser()
    ap.stderr.write = lambda *args, **kwargs: None
    ap.stdout.write = lambda *args, **kwargs: None
    
    #test the help option

# Generated at 2022-06-13 21:13:03.529367
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Testin args = None
    parser = HTTPieArgumentParser(args=None)
    args = parser.parse_args()
    assert args == 'None'
    # Testin args = ["http", "localhost:3000"]
    parser = HTTPieArgumentParser(args=["http", "localhost:3000"])
    args = parser.parse_args()
    assert args == 'None'

# Generated at 2022-06-13 21:13:14.049406
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argument_parser = HTTPieArgumentParser()
    httpie_argument_parser.add_argument('--httpie')
    httpie_argument_parser.add_argument('--user-agent')
    httpie_argument_parser.add_argument('--url')
    httpie_argument_parser.add_argument('--auth')
    httpie_argument_parser.add_argument('--auth-type')
    httpie_argument_parser.add_argument('--ignore-netrc')
    httpie_argument_parser.add_argument('--output')
    httpie_argument_parser.add_argument('--output-file')
    httpie_argument_parser.add_argument('--download')
    httpie_argument_parser.add_argument('--pretty')

# Generated at 2022-06-13 21:13:28.590501
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # No parameter
    args = parser.parse_args()
    assert args.auth is None
    assert args.auth_type is None
    assert args.check_status is True
    assert args.default_options is True
    assert args.download is False
    assert args.download_resume is False
    assert args.follow is False
    assert args.form is False
    assert args.headers == {}
    assert args.ignore_stdin is False
    assert args.max_redirects is 30
    assert args.method == 'GET'
    assert args.output_file is None
    assert args.output_options is None
    assert args.output_options_history is None
    assert args.prettify == 'all'
    assert args.print_body is None

# Generated at 2022-06-13 21:13:38.041057
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parsed_args = parser.parse_args(['--assert=body', '--timeout=5', '--verify=true', '--cert=auth.cert', '--ignore-stdin', '--json', '--form', '--pretty=all', '--stream', '--download', '--download-resume', '--output=outfile.txt', '--output-options=H', '--output-options-history=H', '--history-print=H', '--download-output=outfile.txt', '--print=hH', '--traceback', '--headers', 'X-Custom-Header: validate-me', 'https://httpbin.org/get', 'request-headers:accept:application/json'])
    assert parsed_args.assert_ == 'body'

# Generated at 2022-06-13 21:13:49.470251
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:13:59.007551
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.cli.argtypes import KeyValueArgType
    KeyValueArgType.sep = ':'
    
    http = HTTPieArgumentParser()
    url = 'http://www.yandex.ru/'
    # Method 1:
    request_items = ['X-API-Token:123abc', 'qq:pony','{"user": "john"}']
    args= http.parse_args(['-m','POST','-v',url,*request_items])
    print(args)
    # Request(method='POST', url='http://httpbin.org/post', headers=headers, data=data)

#     # Method 2:
#     request_items = ['-H', 'X-API-Token:123abc', '-d', '{"user": "john"}']
#     args= http.parse

# Generated at 2022-06-13 21:14:11.815901
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  # Case 1:
  #Given
  args = ['GET', 'GET', 'https://www.google.com']
  #When
  parser = HTTPieArgumentParser()
  parsed_args = parser.parse_args(args)
  #Then
  assert parsed_args.url == 'https://www.google.com'
  assert parsed_args.request_items == []
  assert parsed_args.method == 'GET'

  # Case 2:
  #Given
  args = ['GET', 'GET', 'https://www.google.com', 'name=Lucas']
  #When
  parser = HTTPieArgumentParser()
  parsed_args = parser.parse_args(args)
  #Then
  assert parsed_args.url == 'https://www.google.com'