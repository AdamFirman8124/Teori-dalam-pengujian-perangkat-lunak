

# Generated at 2022-06-13 21:04:56.012141
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Set up HTTPieArgumentParser
    parser = HTTPieArgumentParser()
    
    # Create the args list for the -h option
    args = ["-h"]
    # Parse the args
    args = parser.parse_args(args)
    

# Generated at 2022-06-13 21:05:08.285318
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    config = cli.Config(
        color=True,
        default_options=['--form'],
        default_options_from_config_file=[],
        env=cli.Environment(),
    )
    args = ['-f', '--form', 'foo=bar', 'GET', 'https://httpbin.org/get']
    httpie_args = HTTPieArgumentParser(config=config).parse_args(args)
    assert httpie_args.output_options == 'H'
    assert httpie_args.headers['foo'] == 'bar'
    assert httpie_args.method == 'GET'
    assert httpie_args.url == 'https://httpbin.org/get'
    assert httpie_args.prettify == PRETTY_OPTIONS_MAP['all']

# Generated at 2022-06-13 21:05:18.290922
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argument_parser = HTTPieArgumentParser()

    args = httpie_argument_parser.parse_args(['www.google.com'])

    #import pdb; pdb.set_trace()

    assert args.url == 'https://www.google.com'
    assert args.headers == []
    assert args.method == 'GET'
    assert args.prettify == 'all'
    assert args.verify == True
    assert args.verify == True
    assert args.auth == None
    assert args.auth_type == None
    assert args.trust_env == False
    assert args.timeout == DEFAULT_TIMEOUT
    assert args.max_redirects == DEFAULT_MAX_REDIRECTS
    assert args.session == None
    assert args.session_read_only == False
    assert args

# Generated at 2022-06-13 21:05:31.939596
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Environment()
    httpie_args = HTTPieArgumentParser(env)

    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args()
    no_args = parser.parse_args([])

    assert args.max_redirects == 5
    assert no_args.max_redirects == 5
    assert args.output_file == None
    assert no_args.output_file == None
    assert args.truncate == 0
    assert no_args.truncate == 0
    assert args.auth == None
    assert no_args.auth == None
    assert args.output_options == 'hb'
    assert no_args.output_options == 'hb'
    assert args.output == None
    assert no_args.output == None
    assert args.download == False

# Generated at 2022-06-13 21:05:42.592664
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args, _ = parser.parse_args()
    assert args.method == 'GET'
    assert args.json == False
    assert args.headers == []
    assert args.follow == False
    assert args.auth_type == 'basic'
    assert args.download == False
    assert args.body == False
    assert args.prettify == {
        'sorted': False,
        'reindent': False,
        'color': True,
        'pretty': False,
        'all': True}
    assert args.verify == True
    assert args.download_resume == False
    assert args.traceback == False
    assert args.params == {}
    assert args.format_options == PARSED_DEFAULT_FORMAT_OPTIONS
    assert args.data == {}


# Generated at 2022-06-13 21:05:52.274900
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Tests for method parse_args of class HTTPieArgumentParser.
    args = [
        '-v',
        '--json',
        '--form',
        'key=val',
        '--print',
        'H',
        'example.com',
        'key=value',
        'other-key=other-value',
    ]
    parser = HTTPieArgumentParser()
    parser.parse_args(args)
    expected_args = parser.args
    expected_args.check_origin = True
    expected_args.cli_compat = False
    expected_args.debug = False
    expected_args.download = False
    expected_args.download_resume = False
    expected_args.follow = False
    expected_args.headers = {'key': 'val'}
    expected_args.json

# Generated at 2022-06-13 21:06:05.898478
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:15.870500
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # save stdout so we can restore it later
    orig_stdout = sys.stdout
    # save stdin so we can restore it later
    orig_stdin = sys.stdin
    # save stderr so we can restore it later
    orig_stderr = sys.stderr
    # test_streams.py
    # Replace stdout with a StringIO object so it can be captured.
    stdout = io.StringIO()
    sys.stdout = stdout
    # Replace stdin with a StringIO object so it can be captured.
    stdin = io.StringIO()
    sys.stdin = stdin
    # Replace stderr with a StringIO object so it can be captured.
    stderr = io.StringIO()
    sys.stderr = stderr


# Generated at 2022-06-13 21:06:16.618800
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:06:28.281556
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([])

# Generated at 2022-06-13 21:07:17.033268
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # test case 1
    args = ['https://httpbin.org/get', 'Accept:application/json', 'User-Agent:HTTPie/0.9.8']
    parser = HTTPieArgumentParser()
    parsed_args = parser.parse_args(args, env=Environment())
    pass



# Generated at 2022-06-13 21:07:21.810218
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    
    httpie = HTTPieArgumentParser(
        prog='http',
        env={},
        force_colors=True,
        timeout=None,
        max_redirects=10,
        max_request_items_limit=200,
        max_response_size=None, # default: no limit
        verify=True,
        cert=None,
        traceback=False,
        default_options=[],
        default_options_using_env_vars={},
        print_help=False,
        print_version=False,
        output_file=None,
        overrides=None,
    )
    
    # Case 1
    argv = ['-v']
    args = httpie.parse_args(argv)
    assert args.verbose == 1, "Failed test case 1"
    


# Generated at 2022-06-13 21:07:33.084734
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:44.953959
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test case 1
    text = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    session = Session()
    config_dir =  os.path.expanduser('~/.httpie')
    config_path = os.path.join(config_dir, 'config.json')
    session.config = load_config_file(config_path)
    parser = get_parser(session=session)
    
    args = parser.parse_args(['--headers', 'User-Agent:' + text])
    assert args.headers == [('User-Agent', text)]


# Generated at 2022-06-13 21:07:55.845035
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: Only run a subset of the test.
    from httpie.cli import parser
    from httpie import exit_status
    from httpie.core import main

    args = parser.parse_args(args=[])
    assert args.output_file
    assert args.download
    assert args.check_status
    assert 'headers' not in args.output_options
    assert args.prettify == PRETTY_STDOUT_TTY_ONLY
    assert args.follow
    assert args.max_redirects == 5
    assert args.timeout == DEFAULT_TIMEOUT
    assert args.debug
    assert args.traceback

    args = parser.parse_args(['--pretty=all'])
    assert args.output_file
    assert args.download
    assert args.check_status
    assert 'headers' not in args

# Generated at 2022-06-13 21:08:07.200261
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:08:20.100141
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Create an instance of the class
    httpie_arg_parser = HTTPieArgumentParser(description=DESCRIPTION,
                                             formatter_class=argparse.RawDescriptionHelpFormatter,
                                             prog='http')
    args = httpie_arg_parser.parse_args(['--help'])
    assert type(args) == argparse.Namespace
    assert type(args.__dict__) == dict
    for i in args.__dict__:
        if i == 'method':
            assert args.__dict__[i] == None
        elif i == 'request_items':
            assert args.__dict__[i] == []
        elif i == 'config_dir':
            assert args.__dict__[i] == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:08:30.066926
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    kwargs = dict()
    kwargs['argv'] = [
        'https://httpbin.org/patch',
        '-d', '{"hello": "world"}'
    ]
    nargs = len(sys.argv)

# Generated at 2022-06-13 21:08:37.424949
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test `HTTPieArgumentParser` class's `parse_args` method.
    """
    
    # Some arguments for method parse_args of class HTTPieArgumentParser
    command_line_args = ['http', '--debug']
    stdin = sys.stdin
    stdin_isatty = sys.stdin.isatty()
    
    # Create an instance of the class
    httpie_argument_parser_instance = HTTPieArgumentParser(
        stdin=stdin,
        stdin_isatty=stdin_isatty
    )
    
    # Call method parse_args of class HTTPieArgumentParser
    httpie_argument_parser_instance.parse_args(
        args=command_line_args,
        env=os.environ.copy()
    )
    
   

# Generated at 2022-06-13 21:08:51.647898
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(argv[:1])
    assert args.url == 'https://httpie.org'

    args = parser.parse_args(argv[:5])
    assert args.method == 'POST'
    assert args.quiet
    assert args.headers == [
        ('authorization', 'Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=='),
        ('accept-encoding', 'gzip, deflate'),
        ('user-agent', 'HTTPie/0.9.2'),
        ('accept', 'application/json'),
        ('content-type', 'application/json'),
    ]
    assert args.data == '{"hello":"world"}'
    assert args.params == {'q': 'name:httpie'}

# Generated at 2022-06-13 21:10:11.203105
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    the_parser = HTTPieArgumentParser()
    assert_equal(the_parser.parse_args([]), None)


# Generated at 2022-06-13 21:10:21.525390
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Test parse_args method of class HTTPieArgumentParser"""
    # Initialize a parser
    parser = HTTPieArgumentParser()
    # tests with stdin_data = False and stdout_isatty = False
    assert parser.parse_args(args=[], env=EnvironmentTrue, stdin_data=False) == None
    assert parser.parse_args(args=['--json', '--json'], env=EnvironmentTrue, stdin_data=False) == None
    assert parser.parse_args(args=['-j', '-j'], env=EnvironmentTrue, stdin_data=False) == None
    assert parser.parse_args(args=['foo.json'], env=EnvironmentTrue, stdin_data=False) == None

# Generated at 2022-06-13 21:10:33.724159
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    from io import StringIO
    from core.parser import HTTPieArgumentParser
    from core.config import Config
    from core.environment import Environment
    config = Config(Environment())
    parser = HTTPieArgumentParser(config, args=[])
    args = parser.parse_args(["--stream", "--all", "https://httpbin.org/get"])
    assert args.stream==True
    assert args.all==True
    assert args.url=="https://httpbin.org/get"
    args = parser.parse_args(["GET", "https://httpbin.org/get", "API-Key:123456789", "id:1"])
    assert args.method=="GET"
    assert args.url=="https://httpbin.org/get"

# Generated at 2022-06-13 21:10:41.924866
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.context import Environment
    from httpie.config import Config
    from httpie.cli.base import parse_config_file_paths
    from httpie.plugins import AuthPlugin

    class FakeAuthPlugin(AuthPlugin):
        auth_type = 'fake'

    env = Environment(config=Config(load_config_paths=parse_config_file_paths([])))
    parser = HTTPieArgumentParser(env=env)
    parser.add_argument('-h', '--help', dest='help', action='store_true', help='Display this message')
    parser.add_argument('-X', '--method', dest='method', type=str.upper, help="Specify request method to use")

# Generated at 2022-06-13 21:10:45.347360
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_args = HTTPieArgumentParser.parse_args([])
    assert httpie_args is not None
    

# Generated at 2022-06-13 21:10:50.437907
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['echo.httpbin.org', 'get', 'foo=bar', 'baz', '--download']
    options = HTTPieArgumentParser().parse_args(args=args)
    assert options.url == 'http://echo.httpbin.org'
    assert options.method == 'GET'
    assert options.headers['foo'] == ['bar']
    assert options.data == 'baz'
    assert options.download



# Generated at 2022-06-13 21:11:01.964048
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args()
    global_args = [args.compress, args.download, args.download_resume,
                   args.form, args.headers, args.ignore_netrc,
                   args.ignore_stdin, args.max_download,
                   args.max_redirects, args.output_dir,
                   args.output_file, args.output_options,
                   args.output_options_history, args.parameters,
                   args.prettify, args.proxy, args.request,
                   args.traceback, args.upload, args.verbose]
    for arg in global_args:
        assert arg == None
    # Check auth
    assert args.auth == None
    assert args.auth_plugin == None
    assert args.auth_type == None

# Generated at 2022-06-13 21:11:14.689939
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  import pytest
  from urllib.parse import urlparse
  
  http = HTTPieArgumentParser(prog="http", add_help=False)
  args = http.parse_args(["http://example.com"])
  assert args.url == "http://example.com"
  assert args.all == False, "Default value of args.all is False"
  assert args.check_status == False, "Default value of args.check_status is False"
  assert args.download == False, "Default value of args.download is False"
  assert args.form == False, "Default value of args.form is False"
  assert args.headers == [], "Default value of args.headers is []"
  assert args.ignore_stdin == False, "Default value of args.ignore_stdin is False"

# Generated at 2022-06-13 21:11:21.842362
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.error = lambda msg: msg
    parser.parse_args('GET http://example.com')
    assert parser.args.method == 'GET'
    assert parser.args.url == 'http://example.com'

# Test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:11:35.550060
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    result = HTTPieArgumentParser(env=Environment()).parse_args(
        ['https://www.python.org/', 'Accept', 'content-type', 'Accept-Encoding'] +
        ['--auth', 'user:pass']
    )
    assert result.method == 'GET'
    assert result.url == 'https://www.python.org/'
    assert result.auth == 'user:pass'
    assert result.headers == {
        'Accept': 'content-type',
        'Accept-Encoding': '',
    }
test_HTTPieArgumentParser_parse_args()