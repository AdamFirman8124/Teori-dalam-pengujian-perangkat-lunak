

# Generated at 2022-06-13 21:05:05.716575
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    test_args_1 = ['https://httpbin.org/anything', 
                   'Authorization:Basic AAADDD**++', 
                   'X-a:1',
                   'Accept:application/json',
                   'Content-type:application/xml',
                   'X-b:2',
                   'X-c:3',
                   '"a=1&b=2&c=3"',
                   'X-d:4']
    args = parser.parse_args(test_args_1)
    args.command = None
    args.method = 'GET'
    args.download = False
    args.output_file = None
    args.output_file_specified = False
    args.output_options_history = None
    args.prettify = False
    args.pretty

# Generated at 2022-06-13 21:05:15.508173
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    argparser = HTTPieArgumentParser()
    args = argparser.parse_args('http://localhost/')
    expected_result = Namespace(
        auth = None, 
        auth_type = None, 
        data = None, 
        download = False, 
        download_resume = False, 
        files = {}, 
        headers = {'Accept': '*/*'}, 
        ignore_stdin = False, 
        max_redirects = 10, 
        method = 'GET', 
        params = None, 
        timeout = DEFAULT_TIMEOUT_SECONDS, 
        url = 'http://localhost/'
    )
    assert args == expected_result

if __name__ == '__main__':
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:05:23.597486
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    parse_args(self, args=None, namespace=None)
    Parse known args from *args* and return a Namespace object.

    *namespace* should be None or a Namespace object.  If it is
    None (the default), a new empty Namespace object is created for
    the attributes parsed into it.
    """
    # Setup
    httpie_args = HTTPieArgumentParser()
    # Exercise
    # Verify
    pass

# Generated at 2022-06-13 21:05:34.174142
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    result = parser.parse_args([])
    assert result.method == HTTP_GET
    assert result.headers == {}
    assert result.ignore_stdin is False
    assert result.auto_json is False
    assert result.output_file is None
    assert result.output_options == OUTPUT_OPTIONS_DEFAULT
    assert result.body == {}
    assert result.data_items == []
    assert result.headers_items == []
    assert result.url == ''
    assert result.prettify == PRETTY_STDOUT_TTY_ONLY
    assert result.request_items == []
    assert result.download is False
    assert result.download_resume is False
    assert result.verbose is False
    assert result.all is False
    assert result.follow is False
   

# Generated at 2022-06-13 21:05:36.262080
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO 완성하기
    assert False
    pass

# Generated at 2022-06-13 21:05:46.707575
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    config = Config()
    config.merge({'output_options':'Hh'})
    argument_parser = HTTPieArgumentParser(initial_config=config)
    myargs = argument_parser.parse_args([
        '--headers', 
        'a:b',
        '-h', 'c:d',
        'https://httpbin.org/headers',
    ])
    assert(myargs.headers == [
        'a:b',
        'c:d'
    ])
test_HTTPieArgumentParser_parse_args()
 

# Generated at 2022-06-13 21:05:55.539359
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:02.848569
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():    
    
    ap = HTTPieArgumentParser()
    args = ap.parse_args(["echo.httpie.org", "get"])
    
    assert args.method == 'GET'
    assert args.url == 'http://echo.httpie.org'
    
test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:06:17.167635
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Test method HTTPieArgumentParser.parse_args()"""
    CUSTOM_PLUGIN_DIR = os.path.join(os.path.dirname(__file__), 'external_plugins')
    parser = HTTPieArgumentParser()
    if os.path.isdir(CUSTOM_PLUGIN_DIR):
        parser.plugin_manager.add_directory(CUSTOM_PLUGIN_DIR)

    args = parser.parse_args(args=['--json={"foo":["bar","baz"]}', 'https://httpbin.org/get'])
    assert args.json == {'foo': ['bar', 'baz']}
    assert not args.download
    assert not args.output_file
    assert args.prettify is PRETTY_STDOUT_TTY_ONLY
    assert args.pre

# Generated at 2022-06-13 21:06:28.877948
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([
        '--headers',
        'Cache-Control: no-cache',
        '--verbose',
        '--method',
        'POST',
        '--form',
        '--body',
        'name:Jack',
        '--download',
        '--output',
        'books.xml',
        '--pretty',
        'all',
        'https://httpbin.org/post',
    ])
    assert args.headers == 'Cache-Control: no-cache', 'args.headers error'
    assert args.verbose == True, 'args.verbose error'
    assert args.method == 'POST', 'args.method error'
    assert args.form == True, 'args.form error'

# Generated at 2022-06-13 21:07:23.079562
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  # Fixture: Create mock objects
  httpie_args = HTTPieArgumentParser()
  httpie_args.args = MockHTTPieArgs()
  httpie_args.env = MockHTTPieEnv()
  httpie_args._actions = MockHTTPieActions()
  httpie_args.error = MockHTTPieError()
  httpie_args.has_stdin_data = MockHTTPieHasStdinData()
  httpie_args.parse_args = MockHTTPieParseArgs()
  httpie_args.parse_known_args = MockHTTPieParseKnownArgs()
  httpie_args._process_headers = MockHTTPieProcessHeaders()
  httpie_args._process_request_items = MockHTTPieProcessItems()
  httpie_args._process_url = MockHTTPieProcessUrl()
  httpie_

# Generated at 2022-06-13 21:07:33.468761
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.core import DEFAULT_UA
    from httpie.core import DEFAULT_UA_STRING
    from httpie.core import DEFAULT_VERBOSE

    # Test for method __call__ of class HTTPieArgumentParser
    class TestHTTPieArgumentParser(object):
        def __init__(self):
            self.stdout = None
            self.stderr = None
            self.stdin = None
            self.stdin_isatty = None
            self.stderr_isatty = None
            self.stdout_isatty = None
            self.stdout_encoding = None
            self.config_dir = None
            self.is_windows = False


# Generated at 2022-06-13 21:07:34.926073
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass




# Generated at 2022-06-13 21:07:47.353644
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # parser.add_argument('--verbose', '-v', action='store_true')
    # parser.add_argument('--output', nargs='?')
    # parser.add_argument('--download', '-d', action='store_true')
    # parser.add_argument('--url', default=None, dest='url', metavar='URL')
    parser.add_argument('-a', '--auth')
    parser.add_argument('--auth-type', dest='auth_type')
    
    url = 'http://127.0.0.1:8000/login'
    
    data = {
        'username': 'root',
        'password': 'root'
    }
    

# Generated at 2022-06-13 21:07:55.686014
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--print', 'H', '--all', '--verbose',
        '--headers', '--form', '--json', '--pretty', 'all',
        'http://example.com'])
    assert args.output_options == 'H'
    assert args.all
    assert args.verbose
    assert args.headers
    assert args.form
    assert args.json
    assert args.prettify == PRETTY_MAP['all']
    assert args.url == 'http://example.com'


# Generated at 2022-06-13 21:08:02.154764
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('req_strs', nargs='+')
    parser.add_argument('--data', action='store', dest='data')
    parser.add_argument('-v', '--verbose', action='count', dest='verbose', default=0)
    parser.add_argument('--debug', action='store_true', dest='debug')
    parser.add_argument('--headers', action='store_true', dest='headers')
    parser.add_argument('-o', '--output', action='store', dest='output')
    parser.add_argument('--print', action='store', dest='print')
    parser.add_argument('--json', action='store_true', dest='json')
    parser.add_argument('--pretty', action='store', dest='pretty')

# Generated at 2022-06-13 21:08:11.366382
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Note:
    # this test is here because testing it as a normal unit test will
    # make it very hard to test since it is a class method
    # this is the easiest way it can be tested

    # GIVEN:
    # the configuration options of the HTTPieArgumentParser
    parser = HTTPieArgumentParser(
        prog='HTTPieTest',
        default_options=[],
        env=Environment(colors=256)
    )
    parser.add_argument('--version', action='version', version='2.0.0')

# Generated at 2022-06-13 21:08:24.135197
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([
        'http://example.com/test',
        '--get',
        '--headers',
        'User-Agent:TestAgent',
        '--body',
        '"test_body"'
    ])
    assert args.get
    assert args.headers == ['User-Agent:TestAgent']
    assert args.data == 'test_body'
    assert args.method == 'GET'
    assert args.url == 'http://example.com/test'
    assert args.auth == None


# Generated at 2022-06-13 21:08:33.687119
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # prepare
    parser = HTTPieArgumentParser(prog='http')
    parser.is_finalized = True
    # execute
    args = parser.parse_args(['http', 'localhost'])
    # verify
    assert args.url == 'localhost'
    assert args.auth_type == 'Basic'
    assert args.download == False
    assert args.follow == False
    assert args.ignore_netrc == False
    assert args.max_redirects == DEFAULT_MAX_REDIRECTS
    assert args.output_file is None
    assert args.stdin_isatty == None
    assert args.timeout == DEFAULT_TIMEOUT
    assert args.verify == True
    assert isinstance(args.parser, HTTPieArgumentParser)
    assert isinstance(args.env, Environment)
    assert isinstance

# Generated at 2022-06-13 21:08:34.532690
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    return ""



# Generated at 2022-06-13 21:10:05.942197
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args = [])

# Generated at 2022-06-13 21:10:18.673334
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args_list = ["http","--ignore-stdin","--ignore-hosts","--method=POST","--json","--debug","--traceback"]
    env = Environment()
    parser = HTTPieArgumentParser(env=env)
    assert parser.parse_args(args_list) is not None
    assert parser.parse_args(args_list).ignore_hosts == True
    assert parser.parse_args(args_list).url == "http"
    assert parser.parse_args(args_list).method == "POST"
    assert parser.parse_args(args_list).json == True
    assert parser.parse_args(args_list).debug == True
    assert parser.parse_args(args_list).traceback == True

# Generated at 2022-06-13 21:10:26.359400
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.arguments_to_remove.append('-h')
    parser.arguments_to_remove.append('--help')
    parser.arguments_to_remove.append('--traceback')
    parser.arguments_to_remove.append('-v')
    parser.arguments_to_remove.append('--verbose')
    try:
        parser.parse_args()
    except SystemExit:
        pass
    args = parser.parse_args('')
    assert not args.offline
    assert not args.download_resume
    assert not args.download
    assert args.timeout == DEFAULT_TIMEOUT
    assert args.max_redirects == DEFAULT_MAX_REDIRECTS
    assert args.max_headers == DEFAULT_MAX_HEADERS
   

# Generated at 2022-06-13 21:10:37.087332
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.input import KeyValue

    def get_parser():
        return HTTPieArgumentParser()

    def get_args(args, env=ENVVAR_PREFIX_DEFAULT + '_ARG_VAR_IS_NOT_SET'):
        return get_parser().parse_args(args=args, env=env)

    def set_env(env):
        os.environ[ENVVAR_PREFIX_DEFAULT + '_ARG_VAR'] = env

    def unset_env():
        os.environ.pop(ENVVAR_PREFIX_DEFAULT + '_ARG_VAR', None)

    # Import here to avoid an import cycle.
    from httpie.input import KeyValueArgType

    # The following methods also test parse_items() indirectly.

# Generated at 2022-06-13 21:10:48.230998
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:10:52.885080
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Arrange
    httpie_parser = HTTPieArgumentParser()
    with pytest.raises(SystemExit) as excinfo:
        httpie_parser.error("test error")
    assert str(excinfo.value) == "test error"
    # Act
    args = httpie_parser.parse_args(['--status-code', '200'])
    # Assert
    assert args.status_code == 200


# Generated at 2022-06-13 21:11:04.807225
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    mock_parser = mock.create_autospec(HTTPieArgumentParser)
    parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:11:13.795753
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Arrange
    parser = HTTPieArgumentParser()
    argv=['http', '--help']
    # Act
    try:
        args = parser.parse_args(argv)
    except SystemExit as ex:
        # Assert
        assert ex.code == 0

    # Arrange
    parser = HTTPieArgumentParser()
    argv = ['http', '--foo']
    # Act
    try:
        args = parser.parse_args(argv)
    except SystemExit as ex:
        # Assert
        assert ex.code == 2


# Generated at 2022-06-13 21:11:16.808988
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser=HTTPieArgumentParser()
    res = parser.parse_args(['www.baidu.com', 'baidu'])
    pdb.set_trace()
    print(res)


# Generated at 2022-06-13 21:11:33.236009
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # setup
    args = [
        "http",
        "localhost",
        "-f",
        "-a"
    ]
    # test
    parser = HTTPieArgumentParser()
    parser.parse_args(args)
    # verify
    assert(parser.args.url == 'localhost')
    assert(parser.args.method == 'GET')
    assert(parser.args.follow)
    assert(parser.args.output_file is None)

    # setup
    args = [
        "http",
        "localhost",
        "name=admin",
        "-v"
    ]
    # test
    parser = HTTPieArgumentParser()
    parser.parse_args(args)
    # verify
    assert(parser.args.url == 'localhost')

# Generated at 2022-06-13 21:13:27.150604
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test if all the arguments of the class HTTPieArgumentParser are
    correctly parsed.
    """

    # Create a string containing all the arguments to parse
    args_str = '-v --form --headers --body --download --ignore-stdin --verify=no --auth-type=basic --auth=user:password --auth-plugin=httpie-aws-auth --timeout=30 --max-redirects=30 --output=output_file.txt --output-file-specified --output-options=colors --output-options-history=colors --pretty=all --prettify=all --prettify=all --download-resume --download --form --default-scheme=https --verify=no --ignore-netrc --traceback url user:password@www.google.com OPTIONS Item=Item value'
    args_str = args

# Generated at 2022-06-13 21:13:37.981583
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Environment()
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args([])
    assert(type(env.stdout) == io.TextIOWrapper)
    assert(args.verbose == False)
    assert(args.explain == None)
    assert(args.traceback == False)
    assert(args.check_status == True)
    assert(args.headers == ["Accept: */*"])
    assert(args.output_options == "H")
    assert(args.output_options_history == "H")
    assert(args.prettify == False)
    assert(args.json_indent == 2)
    assert(args.style == 'solarized-dark')
    assert(args.style_sheet == 'default')

# Generated at 2022-06-13 21:13:49.473686
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['http://httpie.org'])
    # Testing for attributes of the args object
    assert args.url == 'http://httpie.org'
    assert args.auth_plugin == None
    assert not args.output_file_specified
    assert args.output_file == None
    assert args.quiet == False
    assert args.auth == None
    assert args.auth_type == None
    assert not args.ignore_netrc
    assert args.ignore_stdin == False
    assert args.method is None
    assert args.request_items == [], 'request items list cannot be empty'
    assert not args.form
    assert args.headers == []
    assert args.data == None
    assert args.files == {}
    assert args.params == []
   

# Generated at 2022-06-13 21:13:59.008664
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    def _check_HTTPieArgumentParser_parse_args(expected_args, args):
        args = HTTPieArgumentParser().parse_args(args)
        assert args == expected_args, \
            '\n{}\n!=\n{}'.format(str(args), str(expected_args))


# Generated at 2022-06-13 21:14:13.372798
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Init
    parser = HTTPieArgumentParser()
    
    # Asserts
    assert parser._parse_existing_file_and_dir is None
    assert parser._parse_key_value_arg is None
    assert parser._parse_netrc_auth is None
    assert parser._print_message is None
    assert parser._setup_standard_streams is None
    assert parser._process_auth is None
    assert parser._apply_no_options is None
    assert parser._body_from_file is None
    assert parser._guess_method is None
    assert parser._parse_items is None
    assert parser._process_output_options is None
    assert parser._process_pretty_options is None
    assert parser._process_download_options is None
    assert parser._process_format_options is None
