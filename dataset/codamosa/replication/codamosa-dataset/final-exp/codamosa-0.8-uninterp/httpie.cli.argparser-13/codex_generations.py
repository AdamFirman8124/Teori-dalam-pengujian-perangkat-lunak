

# Generated at 2022-06-13 21:05:08.202359
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args(['https://localhost:9000', 'mykey=myvalue'])
    assert parser.args.url == 'https://localhost:9000'
    assert parser.args.method == 'GET'
    assert parser.args.request_items[0].key == 'mykey'
    assert parser.args.request_items[0].value == 'myvalue'
# Testing method HTTPieArgumentParser._process_format_options

# Generated at 2022-06-13 21:05:09.135154
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    main()


# Generated at 2022-06-13 21:05:15.351048
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['GET', 'httpbin.org'])
    assert args.url == 'httpbin.org'
    assert args.method == 'GET'
    
    
parser = HTTPieArgumentParser()
args = parser.parse_args(['GET', 'httpbin.org'])
args.url

args.__dict__

args.output_file

# args.headers

args.method
 

# Generated at 2022-06-13 21:05:28.657972
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with patch('sys.argv', ['http', 'httpbin.org', 'GET', 'X-Api-Key:abc123']):
        args = HTTPieArgumentParser().parse_args()

    assert args.url == 'httpbin.org'
    assert args.method == 'GET'
    assert args.headers == [('X-Api-Key', 'abc123')]
    assert args.timeout == DEFAULT_TIMEOUT
    assert args.check_status is False
    assert args.follow is False
    assert args.follow_redirects is True
    assert args.max_redirects == DEFAULT_MAX_REDIRECTS
    assert args.output_file == None
    assert args.output_options == 'hbH'
    assert args.output_options_history == 'hbH'
    assert args.pre

# Generated at 2022-06-13 21:05:35.157740
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args_in_str = 'http google.com --json'
    args_in_list = args_in_str.split()
    parser = HTTPieArgumentParser()
    res = parser.parse_args(args_in_str)
#     res = parser.parse_args(args_in_list)
    
    return res

res = test_HTTPieArgumentParser_parse_args()
res

# https://github.com/jakubroztocil/httpie/blob/master/httpie/cli.py#L528

'''
https://github.com/jakubroztocil/httpie/blob/master/httpie/cli.py#L528
'''

# Generated at 2022-06-13 21:05:39.681339
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['https://www.kennethreitz.org/']
    parser = HTTPieArgumentParser()
    parsed = parser.parse_args(args)
    assert parsed.url == 'https://www.kennethreitz.org/'
    assert parsed.method == 'GET'
    assert parsed.headers == {}
    assert parsed.request_items == []
    assert parsed.data is None

# Generated at 2022-06-13 21:05:46.440820
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--auth-type=basic'])
    assert args.auth_type == 'basic'
    args = parser.parse_args(['--auth-type=basic:basic'])
    assert args.auth_type == 'basic'
    args = parser.parse_args(['--auth='])
    assert not args.auth


# Generated at 2022-06-13 21:05:55.083307
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test case from docstring.
    parser = HTTPieArgumentParser(prog='http')
    args = parser.parse_args([
        '--verbose',
        'http://httpbin.org/get', 'key==value',
        'baz', 'bar', '--', 'boo', '-b', 'moo'
    ])
    print(args)
    # Following mock output

# Generated at 2022-06-13 21:05:59.572484
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    #
    #
    # TODO:
    #
    #
    pass
# End of unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:14.434609
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.core import parse_args
    from httpie.context import Environment

# Generated at 2022-06-13 21:07:09.977368
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = [
        '--json',
        '-v',
        '-z',
        '--download',
        'GET',
        'https://api.github.com/users/jkbrzt',
        'Accept:application/json'
    ]

# Generated at 2022-06-13 21:07:17.020355
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Not a complete unit test; this is just to test the addition of the -F
    # option by the httpie-unix-socket-plugin:
    args = parser.parse_args(['-F', '/var/run/httpie.sock'])


if __name__ == '__main__':
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:07:19.934762
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Arrange
    parser = HTTPieArgumentParser(add_help=False)
    arguments = ['--method', 'post', '--body', 'item1=value1&item2=value2']

    # Act
    args = parser.parse_args(arguments)

    # Assert
    assert args.method == 'post'
    assert args.stdin_isatty == sys.stdin.isatty()
    assert args.method == 'post'
    assert args.data

# Generated at 2022-06-13 21:07:28.667135
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class Tester(HTTPieArgumentParser):
        def __init__(self, *args, **kwargs):
            super(Tester, self).__init__(*args, **kwargs)
        def parse_args(self, args=None, namespace=None):
            super(Tester, self).parse_args(args, namespace)
    parser = Tester()
    parser.parse_args()
# Unit tests for method error of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:29.600703
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    assert False


# Generated at 2022-06-13 21:07:36.096341
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['http', '--json', '--form', 'GET', 'http://httpbin.org/get']
    parser = HTTPieArgumentParser()
    result = parser.parse_args(args)

# Generated at 2022-06-13 21:07:47.618296
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:52.429635
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Creating an instance of a class
    parser = HTTPieArgumentParser()

    #Calling method parse_args
    parser.parse_args([])
    
    # Asserting if the method returned None
    assert parser.parse_args([]) is None, "Method parse_args should return None"

# Generated at 2022-06-13 21:08:00.408355
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['GET', 'http://foo'])
    assert args.method == 'GET'
    assert args.url == 'http://foo'
    assert 'Accept' not in args.headers
    assert args.headers['Host'] == 'foo'
    assert args.headers['User-Agent'] == 'HTTPie/' + __version__
    assert args.headers['Connection'] == 'keep-alive'

    args = parser.parse_args(
        ['GET', 'http://foo', 'Accept:foo/bar', 'Foo:bar=baz'])
    assert 'Accept' in args.headers
    assert args.headers['Accept'] == 'foo/bar'
    assert 'Foo' in args.headers

# Generated at 2022-06-13 21:08:10.378600
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # case 1
    parser = HTTPieArgumentParser()
    args = parser.parse_args(["https://www.bitmex.com/api/v1/instrument/active"])
    assert args.url == 'https://www.bitmex.com/api/v1/instrument/active'
    # case 2
    parser = HTTPieArgumentParser()
    args = parser.parse_args(["https://www.bitmex.com/api/v1/instrument/active?count=8"])
    assert args.url == 'https://www.bitmex.com/api/v1/instrument/active?count=8'
    # case 3
    parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:09:38.845968
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class T1(HTTPieArgumentParser):
        def __init__(self, *args, **kwargs):
            HTTPieArgumentParser.__init__(self, *args, **kwargs)

    arg_parse = T1()
    ret = arg_parse.parse_args(['--help'])

# Generated at 2022-06-13 21:09:53.795728
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    ap = HTTPieArgumentParser()
    parsed = ap.parse_args()

    assert(parsed.verbose == False)
    assert(parsed.skip_history == False)
    assert(parsed.traceback == False)
    assert(parsed.download == False)
    assert(parsed.download_resume == False)
    assert(parsed.offline == False)
    assert(parsed.help_flag == False)
    assert(parsed.version_flag == False)
    assert(parsed.get_flags == False)
    assert(parsed.headers_file == None)
    assert(parsed.save == False)
    assert(parsed.config_file == None)
    assert(parsed.session == None)

# Generated at 2022-06-13 21:09:54.881180
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:10:00.313738
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test if HTTPieArgumentParser.parse_args() actually works
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--debug', 'http://example.com'])
    assert args.debug
    assert args.url == 'http://example.com'
    args = parser.parse_args('--debug'.split())
    assert args.debug


# Generated at 2022-06-13 21:10:07.322712
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    stdout_encoding = 'utf8'
    is_windows = False
    parser_kwargs = {
        'is_windows': is_windows,
        'stdout_encoding': stdout_encoding,
    }
    env = Environment(is_windows=is_windows, stdout_encoding=stdout_encoding)
    parser = HTTPieArgumentParser(env=env, **parser_kwargs)
    args = parser._parse_args(['http://localhost:8080/post'], stdin=BytesIO(b''))
    print(args)



# Generated at 2022-06-13 21:10:19.176908
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from .helpers import get_args

    args = get_args(
        [],
        [
            'https://httpbin.org/get',
            'user-agent:HTTPie/0.9.8',
            'Accept:application/json',
            'X-Header:true',
        ]
    )._get_kwargs()
    args['stdin_isatty'] = False
    args['stdout_isatty'] = False
    args['stderr_isatty'] = False
    args['stdin'] = io.BytesIO()
    args['stdout'] = io.BytesIO()
    args['stderr'] = io.BytesIO()

    parser = HTTPieArgumentParser(**args)
    parser.add_argument('--ignore-stdin', action='store_true')

# Generated at 2022-06-13 21:10:31.222969
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['http', '--help'])
    ok_(args.help)

    # Test that the HTTPieArgumentParser._parser_main is executed once,
    # and then the original parser_main is restored.
    class FakeHTTPieArgumentParser(HTTPieArgumentParser):
        def __init__(self):
            self.parser_main_executed = 0

        def _parser_main(self, *args, **kwargs):
            self.parser_main_executed += 1

    parser = FakeHTTPieArgumentParser()
    args = parser.parse_args(['http', '--help'])
    eq_(parser.parser_main_executed, 0)
    eq_(args.help, 1)
    # TODO: this currently does not work


# Generated at 2022-06-13 21:10:40.381391
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # testing method parse_args of class HTTPieArgumentParser
    parser = HTTPieArgumentParser()

    args_string = 'http://httpbin.org/headers'
    args = parser.parse_args(args_string.split())
    assert args.url == 'http://httpbin.org/headers', "parse_args(args_string) failed"
    
    
    args_string = 'http://httpbin.org/headers'
    args = parser.parse_args(args_string.split() + ['Accept:'])
    assert args.headers == [KeyValue(key='Accept', value=None, sep='', orig=None, sep_value=None, key_orig=None)], "parse_args(args_string) failed"
    
    
    args_string = 'http://httpbin.org/headers'

# Generated at 2022-06-13 21:10:45.741787
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args(['http', 'POST', '--json={"test": "body"}', 'httpbin.org/post'])
test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:10:54.088317
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args('--ignore-stdin'.split())
    assert args.ignore_stdin == True
    assert args.headers == []
    assert args.ignore_stdin == True
 
    parser = HTTPieArgumentParser()
    args = parser.parse_args('--ignore-stdin --verbose'.split())
    assert args.verbose == True
    assert args.headers == []
    assert args.ignore_stdin == True
    assert args.verbose == True
    
    parser = HTTPieArgumentParser()
    args = parser.parse_args('--ignore-stdin --all'.split())
    assert args.ignore_stdin == True
    assert args.headers == []
    assert args.ignore_stdin == True
    assert args.all == True
    

# Generated at 2022-06-13 21:14:07.166602
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['-v'])
    assert args.verbose == True


# HTTPie Arguments

# Set the 'python' executable to our version of Python
# so it is callable on Windows
sys.executable = sys.executable.lower() if sys.platform == 'win32' else sys.executable


# Generated at 2022-06-13 21:14:08.007185
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass