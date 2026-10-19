

# Generated at 2022-06-13 21:05:12.377079
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test with empty argument list
    argv_list = []
    argv_bytes = b''
    parser = HTTPieArgumentParser()
    args = parser.parse_args(argv_list)
    # Compare against the command line arguments parsed by the parser
    assert argv_list==parser.argv_list
    # Compare against the command line argument bytes parsed by the parser
    assert argv_bytes==parser.argv_bytes
    # Compare against the default values defined in the parser
    assert parser.default_values==args
    
    # Test with non-empty argument list

# Generated at 2022-06-13 21:05:24.108667
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: fix this test, as it fails when run in a directory that
    # contains a file named 'GET.json'.
    parser = HTTPieArgumentParser()
    args = parser.parse_args([
        '--pretty=none',
        '--body',
        '--verbose',
        'http://httpie.org/get',
        'name==John',
        'age==30',
        '--json',
        '{"A":1234}'
    ])

# Generated at 2022-06-13 21:05:34.416432
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('--auth', type=parse_auth)
    parser.add_argument('--config')
    parser.add_argument('--debug')
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--headers', type=KeyValueArgType())
    parser.add_argument('--max-timeout', type=float)
    parser.add_argument('--output-file', type=open)
    parser.add_argument('--session-read-only', action='store_true')
    parser.add_argument('--stream', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add

# Generated at 2022-06-13 21:05:43.469351
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Arrange
    args_str = ''
    # Act
    args = HTTPieArgumentParser().parse_args(shlex.split(args_str))
    # Assert
    assert args is not None

    # Arrange
    args_str = '--output-file httpie.log'
    # Act
    args = HTTPieArgumentParser().parse_args(shlex.split(args_str))
    # Assert
    assert args.output_file is not None

    # Arrange
    args_str = '--json --form'
    # Act
    args = HTTPieArgumentParser().parse_args(shlex.split(args_str))
    # Assert
    assert args.form is True

    # Arrange
    args_str = '--json --form --body'
    # Act
    args = HTTP

# Generated at 2022-06-13 21:05:52.440823
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    print("Running test_HTTPieArgumentParser_parse_args")

    # Unit test case:
    #   Command: http POST httpbin.org/post first_name=John last_name=Doe
    #   URL:
    #   Request: POST
    #   Method: httpbin.org/post
    #   Arguments: first_name=John last_name=Doe
    #   Options:
    #   Headers:
    #   Body:
    #   Expected Output:
    #   Error:
    #   Output:

    class A(object):
        pass

    args = A()
    args.default_options = []
    args.ignore_stdin = False
    args.ignore_netrc = False
    args.url = 'httpbin.org/post'
    args.method = HTTP_POST


# Generated at 2022-06-13 21:06:06.260427
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:19.290256
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(args=[])

# Generated at 2022-06-13 21:06:28.879542
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    key=True
    env = Environment(colors=256, stdin_isatty=True, stdout_isatty=True)
    if key:
        input_args = list(['--body', 'hello', 'http://httpbin.org/post'])
    else:
        input_args = list(['http://httpbin.org/post', '--body', 'hello'])
    parser = HTTPieArgumentParser(env=env, add_help=False)
    parser.parse_args(input_args)
    
    
test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:06:37.377435
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test with 0 arguments
    sys.argv = ['http']
    args = HTTPieArgumentParser().parse_args()
    assert args.url is None
    assert args.headers == []
    assert args.request_items == []
    assert args.method is None  # Guess
    assert args.output_file is None
    assert args.output_options is None
    assert args.output_options_history is None
    assert args.download is False
    assert args.download_resume is False
    assert args.timeout is None
    assert args.check_status is False
    assert args.follow is False
    assert args.follow_redirects is None
    assert args.max_redirects is None
    assert args.download_all is False
    assert args.output_file_specified is False
    assert args.ignore_stdin

# Generated at 2022-06-13 21:06:43.153516
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    common_args = ['-v', 'https://httpbin.org/get']
    schema_args_list = ['key:value', 'key:', ':value', 'key=value']
    request_items_list = [
        'Name:Elvis',
        'Age:42',
        ':0',
        'Status=False',
        'Is Married',
        ':null',
        ':',
        '',
        '=',
        'Is Married:false',
        ':true'
    ]

# Generated at 2022-06-13 21:07:57.342475
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    import subprocess
    from furl import furl
    from httpie.core import main
    from httpie.input import InputFile
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPDigestAuth
    
    # Set up a Stream for stdout
    output = io.TextIOWrapper(io.BytesIO(),sys.stdout.encoding,errors='replace')
    fake_stdout = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output

    # Test cases
    # - Test all optional values
    # - Test some optional values
    # - Test no optional values
    # - Test different value types
    # - Test upper-case characters
    # - Test lower-case characters
    # - Test digits

# Generated at 2022-06-13 21:08:08.960236
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    config_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'configs')
    config_path = os.path.join(config_dir, 'config.json')
    env = Environment(stdout_isatty=False, colors=256)
    parser = HTTPieArgumentParser(env=env)
    config_dirs = [config_dir]
    args = parser.parse_args(['--config-dir', config_dir, 'http://httpbin.org/get'], config_dirs=config_dirs)
    assert args.headers['Accept'] == 'application/json'
    config_dirs = [config_dir]
    args = parser.parse_args(['http://httpbin.org/get'], config_dirs=config_dirs)
    assert args

# Generated at 2022-06-13 21:08:11.952047
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # assert False # TODO: implement your test here
    pass


# Generated at 2022-06-13 21:08:21.200458
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    m = Mock()

# Generated at 2022-06-13 21:08:31.082504
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Setup
    args = []
    args.append('--pretty')
    args.append('all')
    args.append('https://httpie.org/get')
    args.append('Content-Type:')
    args.append('application/json')
    args.append('Accept:')
    args.append('application/json')
    argparser = HTTPieArgumentParser(prog='http')
    argparser.add_argument('--pretty', default='all')
    argparser.add_argument('url')
    argparser.add_argument('request_items', nargs='*')
    # Exercise
    parsed_args = argparser.parse_args(args)
    # Verify
    assert parsed_args.pretty == 'all'
    assert parsed_args.url == 'https://httpie.org/get'
    assert parsed

# Generated at 2022-06-13 21:08:38.052679
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    HTTPieArgumentParser = HTTPieArgumentParser(prog='http', add_help=False)

    # Test HTTPieArgumentParser._parse_items()

# Generated at 2022-06-13 21:08:52.191794
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(['http', 'localhost'])
    assert args.url == 'http://localhost'
    assert args.auth == None
    assert args.method == 'GET'
    assert args.data == None
    assert args.params == None
    assert args.headers == None
    assert args.files == None
    assert args.output_options == None
    assert args.output_options_history == None
    assert args.output_file == None
    assert args.output_file_specified == False
    assert args.download == False
    assert args.download_resume == False
    assert args.download_all == False
    assert args.upload == None
    assert args.session == None
    assert args.session_read_only == False
    assert args.check_status == False
    assert args.follow

# Generated at 2022-06-13 21:09:03.105102
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # test_arg_format
    env = Environment(colors=256,
                      stdin_isatty=True,
                      stdin=BytesIO(b'{"foo":"bar"}'),
                      stdout_isatty=True,
                      stdout=BytesIO(),
                      stderr=BytesIO(),
                      is_windows=False,
                      stdin_encoding=None)
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args('--json --print=A foo=bar')
    assert args.arg_format == 'json'
    assert args.output_options == 'A'
    # test_default_headers_when_shebang_is_present

# Generated at 2022-06-13 21:09:13.027689
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # test with no arguments
    argv = []
    args = HTTPieArgumentParser().parse_args(argv)
    assert args.url == 'https://httpbin.org/get'
    assert not hasattr(args,'method')
    assert args.headers is None
    assert args.params is None
    assert args.data is None
    assert args.files is None
    assert not hasattr(args,'output')
    
    
    # test with a simple argument
    argv = ['https://httpbin.org/get']
    args = HTTPieArgumentParser().parse_args(argv)
    assert args.url == 'https://httpbin.org/get'
    
    
    # test with another simple argument
    argv = ['https://httpbin.org/get/hello']
    args = HTTPieArgumentParser

# Generated at 2022-06-13 21:09:19.469389
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    try:
        const.FORMAT_OPTIONS_SPEC = const.FORMAT_OPTIONS_SPEC_H
        arg = HTTPieArgumentParser(prog='http', env=Environment())
        return arg.parse_args(['http', 'GET', 'http://www.google.com'])
    finally:
        const.FORMAT_OPTIONS_SPEC = const.FORMAT_OPTIONS_SPEC_DEFAULT



# Generated at 2022-06-13 21:10:41.543596
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Bind the content of the arg parser 
    parser = HTTPieArgumentParser()
    # args to be tested.

# Generated at 2022-06-13 21:10:43.535049
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    p = HTTPieArgumentParser(env=Environment())
    args = p.parse_args([])



# Generated at 2022-06-13 21:10:53.114793
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = ArgumentParser()
    parser.add_argument('--foo', nargs='?', type=int)
    parser.add_argument('bar', nargs='?')
    parser.add_argument('koo', nargs='?')
    parser.add_argument('--moo', nargs='?', type=int)
    parser.add_argument('--koo')
    
    args=['--foo','1','--koo=3','4444']
    
    # expected result
    expected = SimpleNamespace()
    expected.foo = 1
    expected.bar = None
    expected.koo = '4444'
    expected.moo = None
    expected.koo = '3'
    
    # actual result
    result = parser.parse_args(args)
    
    # compare the results

# Generated at 2022-06-13 21:11:05.107097
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    parser.add_argument('-c')
    parser.add_argument('-d')
    parser.add_argument('-e')
    
    pasrser = HTTPieArgumentParser(parser)
    args = pasrser.parse_args()
    print(args)
test_HTTPieArgumentParser_parse_args()

# Test for format_option
parser1 = HTTPieArgumentParser(
    argparse.ArgumentParser(),
    is_windows=False,
    stdin_isatty=False,
    stdout_isatty=False,
    stdout_encoding='utf8'
)
print(parser1)


# Generated at 2022-06-13 21:11:15.592438
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    args = HTTPieArgumentParser().parse_args([
        'http://httpbin.org/post',
        'foo=bar',
        'baz',
        'buzz==',
        'key'
    ])
    assert args.url == 'http://httpbin.org/post'
    assert args.items == [
        KeyValue(key='foo',
                 value='bar',
                 sep='='),
        KeyValue(key='baz',
                 value='',
                 sep=' '),
        KeyValue(key='buzz',
                 value='=',
                 sep='=='),
        KeyValue(key='key',
                 value='',
                 sep=' '),
    ]



# Generated at 2022-06-13 21:11:31.700944
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args, extra = parser.parse_args([])
    assert args.output_file is None
    assert args.output_file_specified is False
    assert args.prettify is None
    assert args.progress_indicators == [True, True]
    assert args.method == 'GET'
    assert args.pretty == 'all'
    assert args.style == PYCHARM
    assert args.style_error == RED_BOLD
    parser = HTTPieArgumentParser()
    args, extra = parser.parse_args(['-d', '{}'])
    assert args.data == '{}'
    assert args.files == {}
    assert args.headers == (['Accept: */*'], [])
    assert args.method == 'GET'
    assert args.params == {}


# Generated at 2022-06-13 21:11:42.573823
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Test for parse_args method"""
    from httpie import __main__ as cli
    _valid_cli_request = ['http', 'httpbin.org/headers', 'User-Agent:curl/7.51.0']
    args_text = 'httpbin.org/headers User-Agent:curl'
    parser = HTTPieArgumentParser(prog='httpie',args_text=args_text,default_options=cli.DEFAULT_OPTIONS)
    args = parser.parse_args(_valid_cli_request)
    assert args.url == 'httpbin.org/headers'
    #assert args.headers == ['User-Agent:curl']
    assert args.method == 'GET'
    assert args.verbose == False
    assert args.all == False
 

# Generated at 2022-06-13 21:11:49.816109
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Use this method to find out how to call the method.
    # Now test it.
    args = ['--form', '{"name":"Test"}', '--json', 'http://localhost:8080/']
    httpie = HTTPieArgumentParser(description='')
    httpie.parse_args(args)
    args = ['--download', '--download-resume', '--output', 'output.txt', 'http://localhost:8080/']
    httpie = HTTPieArgumentParser(description='')
    httpie.parse_args(args)
# Class HTTPiePlugin

# Generated at 2022-06-13 21:11:57.504253
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args()

# Generated at 2022-06-13 21:12:08.121677
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    examples =[
        ("--auth", "username:password", "--format", "colors"),
        ("--auth", "username:password", "--format", "colors"),
        ("--traceback", "--auth", "username:password", "--format", "colors")
    ]
    #examples = [("-a", "username:password", "-f", "colors")]
    for example in examples:
        _, args = HTTPieArgumentParser().parse_args(example)
        print("\n")
        print(args)
        print("\n")
        print(args.auth)
        print("\n#raw_auth")
        print(args.auth_plugin.raw_auth)
        print("\n#username")
        print(args.auth.username)
        print("\n#password")