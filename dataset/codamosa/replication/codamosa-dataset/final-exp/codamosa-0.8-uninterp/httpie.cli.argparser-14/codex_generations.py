

# Generated at 2022-06-13 21:05:12.378399
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:05:15.311749
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_args = HTTPieArgumentParser()
    test_args = ['http', '--output=json', 'httpbin.org/get']
    assert httpie_args.parse_args(test_args) == test_args

# Generated at 2022-06-13 21:05:28.627114
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:05:33.921733
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['GET', 'http://httpbin.org/get']
    parsed_args = HTTPieArgumentParser.parse_args(args)
    print(parsed_args)
    print(vars(parsed_args))

    args1 = ['GET', 'http://httpbin.org/get', 'var1=value1']
    parsed_args1 = HTTPieArgumentParser.parse_args(args1)
    print(parsed_args1)
    print(vars(parsed_args1))

# Generated at 2022-06-13 21:05:46.137845
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    
    #####################
    # Example 1
    
    args = cmd_args + ["-p"]
    app_args_list = HTTPieArgumentParser().parse_args(args)

# Generated at 2022-06-13 21:05:51.468737
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Configure and parse the arguments
    args = HTTPieArgumentParser().parse_args([])
    assert args.output_options == 'hHb'
    assert args.output_options_history == 'hHb'
    args = HTTPieArgumentParser().parse_args(['--output', 'json', 'google.com'])
    assert args.output_options == 'hHbj'
    assert args.output_options_history == 'hHbj'


# Generated at 2022-06-13 21:05:52.352314
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass


# Generated at 2022-06-13 21:06:06.127362
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(prog='http')

# Generated at 2022-06-13 21:06:10.371093
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:17.221760
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """HTTPieArgumentParser.parse_args() method returns parsed args.

    """
    args = HTTPieArgumentParser().parse_args(['--json', '--ignore-stdin', 'http://example.com/'])
    assert args.json
    assert args.ignore_stdin
    assert args.url == 'http://example.com/'


# Generated at 2022-06-13 21:07:13.971373
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class MockHTTPieArgumentParser():   
        def __init__(self, args, env):
            self.args = args
            self.env = env
        def error(self, message):
            raise Exception(message)
        def _guess_method(self):
            pass
    
        def _parse_items(self):
            pass

        def _process_output_options(self):
            pass

        def _process_pretty_options(self):
            pass

        def _process_download_options(self):
            pass

        def _process_format_options(self):
            pass
    
        def parse_args(self):
            pass

# Generated at 2022-06-13 21:07:24.811126
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from tests.config import config_dir
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--config-dir', config_dir, 'httpie://user:pass@127.0.0.1:8080/some/path?some=query'])
    assert args.url == 'httpie://user:pass@127.0.0.1:8080/some/path?some=query'
    assert args.auth_plugin is None
    assert args.auth is None
    assert args.config_dir == config_dir
    assert args.headers == []
    assert args.data is None
    assert args.files == {}
    assert args.params == []
    assert args.method is None
    assert args.ignore_stdin is False
    assert args.download is None
    assert args.download_resume

# Generated at 2022-06-13 21:07:33.798242
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    for use_long_options in True, False:
        # Requests related configuration.
        for scheme in 'http', 'https':
            for host in 'www.python.org', 'www.python.org:80':
                for host_header in None, 'localhost:5000':
                    for port in ':80', ':443':
                        for path in '/', '/%20/':
                            for query_string in '', 'foo=bar&baz=bar':
                                for fragment in '', 'anchor':
                                    url = urlunsplit((scheme, host, path, query_string, fragment))
                                    r = HTTPieArgumentParser().parse_args(url.split())
                                    assert r.url == url
                                    assert r.host == host
                                    assert r.host_header == host_header
                                   

# Generated at 2022-06-13 21:07:43.860857
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_arg_parser = HTTPieArgumentParser()
    args = httpie_arg_parser.parse_args("--auth-type basic --auth-plugin .\\httpie_plugins\\auth\\basic.py --auth-parse --auth-require http://localhost:8001/auth/login/".split(" "))
    assert args.auth_type == 'basic' and args.auth_plugin == '.\\httpie_plugins\\auth\\basic.py' and args.auth_parse == True and args.auth_require==True and args.url == 'http://localhost:8001/auth/login/'

# Generated at 2022-06-13 21:07:50.083979
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Environment()
    args = HTTPieArgumentParser(env=env)
    raw_args = 'http://example.com/ping -v'
    args_list = args.parse_args(raw_args.split())
    # print("args_list: ", args_list)
    assert args_list.url == 'http://example.com/ping'
    assert args_list.verbose == 1


# Generated at 2022-06-13 21:07:59.051884
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    argv = [
        '--traceback',
        '--print=H',
        '--all',
        '--style=foo',
        '--style=bar',
        '--style=auto',
        'http://httpbin.org/get',
        'Foo:bar',
        'foo==bar',
        'baz:=bar',
        '@/dev/null',
        'wget'
    ]
    parser = HTTPieArgumentParser()
    parser.parse_args(argv)
    
    assert parser.args.url == 'http://httpbin.org/get'
    assert parser.args.output_options == 'H'
    assert parser.args.prettify == PRETTY_MAP['all']
    assert parser.args.style == [ 'foo', 'bar', 'auto' ]

# Generated at 2022-06-13 21:08:10.125529
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args([
        '--method', 'POST',
        '--url', 'http://httpbin.org/post',
        '--data', 'val1',
        '--data', 'val2=val3',
        'alpha',
        '--verbose',
        '--output', 'test.txt',
        '--output-options', 'hH',
    ])

# Generated at 2022-06-13 21:08:16.699602
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    tmp_args=['https://httpie.org', 'Home=Page']
    parser=HTTPieArgumentParser()
    parser.parse_args(tmp_args)
    assert parser.args.url is 'https://httpie.org'
    assert parser.args.request_items[0].key is 'Home'
    assert parser.args.request_items[0].value is 'Page'

# Generated at 2022-06-13 21:08:26.067085
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser
    assert_equal(parser.parse_args(args=["GET","URL"]),parser.parse_args(args=["GET","URL"]))
    assert_equal(parser.parse_args(args=["GET","URL"]), parser.parse_args(args=["GET","URL"]))
    assert_equal(parser.parse_args(args=["GET","URL"]), parser.parse_args(args=["GET","URL"]))
    
    

test_HTTPieArgumentParser_parse_args()
 
 
 


# Generated at 2022-06-13 21:08:35.023496
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # Command Line arguments 
    args = ['http', 'httpbin.org/post', 'color=on', 'television=smart', '--debug','--form','--verbose'] 
    # Convert argument list to args-string
    CommandLine = ''
    for s in args: 
        CommandLine = CommandLine + str(s) + ' '
    # Run method parse_args from class HTTPieArgumentParser
    namespace = parser.parse_args(args)
    # Assertion
    assert namespace.url == 'http://httpbin.org/post'
    assert namespace.method == 'POST'
    assert namespace.data == [('color', 'on'), ('television', 'smart')]
    assert namespace.auth is None
    assert namespace.auth_plugin is None
    assert namespace.headers

# Generated at 2022-06-13 21:10:18.168680
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import httpie.core

    def parser_test(test_data):
        parser = httpie.core.HTTPieArgumentParser()
        # argparse.ArgumentParser.parse_args will parse sys.argv by default.
        # Here we explicitly pass in a list.
        return parser.parse_args(test_data)

    def _test(test_data, expected_args):
        args = parser_test(test_data)
        assert args.method == expected_args.method
        assert args.url == expected_args.url
        assert args.headers == expected_args.headers
        assert args.params == expected_args.params
        assert args.data == expected_args.data
        assert args.files == expected_args.files
        assert args.output_file == expected_args.output_file
        assert args.output_

# Generated at 2022-06-13 21:10:21.441516
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.env = Environment()
    args = parser.parse_args(['https://httpbin.org/get','--json'])
    print(args)

# Generated at 2022-06-13 21:10:23.985939
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    assert True

test_HTTPieArgumentParser_parse_args()
 

# Generated at 2022-06-13 21:10:32.130942
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    args = ['http', 'https://api.example.com/items', 'a=1', 'b=2']

    env = Environment(
        colors=256,
        stdin_isatty=True,
        stdout_isatty=True,
        stdout_bytes_only=False,
        plugins=[]
    )

    parser = HTTPieArgumentParser(args=args, env=env)
    args = parser.parse_args()

    return args.url == 'https://api.example.com/items'


# Generated at 2022-06-13 21:10:34.413263
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    assert parser.parse_args([]) == parser.args


# Generated at 2022-06-13 21:10:39.648620
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(mode='w+') as fd:
        fd.write('data')
        fd.seek(0)
        args = ['-b', fd.name]
        parser = HTTPieArgumentParser()
        parsed_args = parser.parse_args(args=args)
        assert os.path.getsize(parsed_args.output_file.name) == 0

# Generated at 2022-06-13 21:10:48.855623
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class MockHTTPieArgumentParser(HTTPieArgumentParser):
        def __init__(self, args=None, env=None, prog=None):
            self._prog = prog
            self.env = env = StandaloneEnvironment(
                stdin=None,
                stdin_isatty=True,
                stdout=None,
                stdout_isatty=True,
                stderr=None,
                stderr_isatty=True,
                stdout_encoding='UTF-8',
                stdin_encoding='UTF-8',
                is_windows=False,
                color_mode=True
            )
            self.args = None
            super().__init__(
                args=args,
                env=env,
                standalone_mode=True
            )
            self.parse_args()

# Generated at 2022-06-13 21:10:51.021449
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # noinspection PyTypeChecker
    httpie_args = HTTPieArgumentParser().parse_args(args=[])
    assert httpie_args.json == False


# Generated at 2022-06-13 21:11:02.309098
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    # get a mocked version of the httpie argument parser
    mock_parser = HTTPieArgumentParser()
    # get the arguments the user of httpie could use
    args = []

    # get the arguments that cannot be parsed
    invalid_args = []

    # get the arguments that belong to a mutually exclusive group
    mutually_exclusive_args = []
    for action in parser._actions:
        if isinstance(action, argparse._MutuallyExclusiveGroup):
            for subaction in action._group_actions:
                for option_string in subaction.option_strings:
                    mutually_exclusive_args.append(option_string)

    # get the arguments for which we cannot generate a default value
    # get the arguments that can be parsed

# Generated at 2022-06-13 21:11:14.785778
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test for method parse_args of class HTTPieArgumentParser.
    """

    parser = HTTPieArgumentParser()
    parser.parse_args(args = ['http', '--help'])
    parser.parse_args(args = ['http', 'http://127.0.0.1'])
    parser.parse_args(args = ['http', '--version'])
    parser.parse_args(args = ['http', '--traceback'])
    parser.parse_args(args = ['http', 'GET', 'http://example.org/'])
    parser.parse_args(args = ['http', 'http://127.0.0.1', 'key=value'])
    parser.parse_args(args = ['http', '--help-auth'])