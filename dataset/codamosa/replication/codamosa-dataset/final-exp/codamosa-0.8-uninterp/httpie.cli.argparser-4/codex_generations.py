

# Generated at 2022-06-13 21:05:06.460917
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()

    # case 1
    args_ = ['--auth-type', 'basic', '-h', 'Host-header', '--pretty', 'all', '--method', 'PUT', '--body', 'post_data', '--headers', 'header1', '--output', 'output', '--print', 'format', '--download', '--insecure', '--verify', 'verify', 'URL']
    args = parser.parse_args(args_)
    assert args.auth_type == 'basic'
    assert args.headers == [HTTPHeader('Host-header')]
    assert args.request_items == []
    assert args.input_file == None
    assert args.method == 'PUT'
    assert args.body == 'post_data'
    assert args.output_file == 'output'


# Generated at 2022-06-13 21:05:13.493602
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args(): #(self):
    parser = HTTPieArgumentParser()
    parser.add_argument('--arg', dest='arg')
    parser.add_argument('rest', nargs=argparse.REMAINDER)

    args = parser.parse_args(
        ['get', 'http://httpbin.org/', 'r1', 'r2', '--arg', 'v1', 'v2'])
    assert args.arg == 'v1'
    assert args.rest == ['r1', 'r2', '--arg', 'v2']



# Generated at 2022-06-13 21:05:25.575937
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    print('########## HTTPieArgumentParser.parse_args(): ##############')
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args(args=['http://httpbin.org'])
    print(arg_parser.args)
    print(arg_parser.args.method)
    print(arg_parser.args.url)
    print(arg_parser.args.headers)
    print(arg_parser.args.data)
    print(arg_parser.args.params)
    print(arg_parser.args.files)
    print('########## HTTPieArgumentParser.parse_args(): ##############')

    print('########## HTTPieArgumentParser.parse_args(): ##############')
    arg_parser = HTTPieArgumentParser()

# Generated at 2022-06-13 21:05:35.170830
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # Test for method parse_args of class HTTPieArgumentParser
    # Input arguments for the HTTPieArgumentParser.parse_args() method
    args = ['https://httpbin.org/get', 'Accept:application/json', 'User-Agent:HTTPie/1.0.0']

    # Setup argument parser
    parser = HTTPieArgumentParser()

    # Parse arguments
    args = parser.parse_args(args)

    # Check for expected output

# Generated at 2022-06-13 21:05:37.660383
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(['--colors'])
    assert args.colors == True


# Generated at 2022-06-13 21:05:49.686815
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    example_args = [
        '-o', 'myfile.txt',
        '--output', 'myfile.txt',
        '-p', 'socks5', 'https://httpbin.org/get'#,
        #'-p', 'http', 'https://httpbin.org/get',
        #'-p', 'HTTPS', 'http://httpbin.org/get',
        #'-p', 'HTTP', 'http://httpbin.org/get'
    ]
    hp = HTTPieArgumentParser()
    args = hp.parse_args(example_args)
    if 'myfile.txt' in args.output_file.name:
        print('-o and --output option for output file are  working')
    else:
        print('-o and --output option for output file not working')


# Generated at 2022-06-13 21:06:01.233755
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import tempfile
    import io

    parser = HTTPieArgumentParser()
    parser.add_argument('--proxy', '-p')
    # FIXME: Check encoding
    parser.add_argument('--output', metavar='FILE', type=io.open)
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--download-resume', action='store_true')
    parser.add_argument('--ignore-netrc', action='store_true')
    parser.add_argument('--ignore-stdin', action='store_true')
    parser.add_argument('--session', action='store')
    parser.add_argument('--auth-type', action='store')
    parser.add_argument('--auth', action='store')

# Generated at 2022-06-13 21:06:15.595753
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Creating a mock
    mock_sys = Mock()
    # Setting the attributes of mock object
    mock_sys.argv = ['http', 'test']
    mock_sys.stdout = Mock
    mock_sys.stdout.buffer = Mock()
    mock_sys.stderr = Mock
    mock_sys.stderr.buffer = Mock()
    mock_sys.stderr_isatty = True
    mock_sys.stdout_encoding = 'utf-8'
    mock_sys.stderr_encoding = 'utf-8'
    mock_sys.stdin = Mock()
    mock_sys.stdin.buffer = Mock()
    mock_sys.stdin.encoding = 'utf-8'
    mock_sys.stdin_isatty = True

# Generated at 2022-06-13 21:06:20.361394
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Unit test for method HTTPieArgumentParser.parse_args
    See https://docs.pytest.org/en/latest/
    """
    parser = HTTPieArgumentParser()
    with pytest.raises(SystemExit) as exc_info:
        parser.parse([])
    assert exc_info.value.code == 2



# Generated at 2022-06-13 21:06:32.265832
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class MockArgs(object):
        """
        Args to mock the default argparser.parse_args()
        """
        # dictionary: {'name': value}
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
    # Get mock args

# Generated at 2022-06-13 21:07:26.570262
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    HTTPieArgumentParser = ArgumentParser.HTTPieArgumentParser
    args = ['--help']
    assert type(HTTPieArgumentParser(prog='test_HTTPieArgumentParser_parse_args')) == HTTPieArgumentParser
    assert type(HTTPieArgumentParser().parse_args(args)) == argparse.Namespace
    assert type(HTTPieArgumentParser().parse_known_args(args)) == (list,tuple)
    args = ['--debug']
    assert type(HTTPieArgumentParser().parse_args(args)) == argparse.Namespace
    assert type(HTTPieArgumentParser(prog='test_HTTPieArgumentParser_parse_args').add_argument('--foo')) == HTTPieArgumentParser

# Generated at 2022-06-13 21:07:34.594672
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    assert parser.parse_args([])

if __name__ == "__main__":
    test_HTTPieArgumentParser_parse_args()


# This file is adapted from HTTPie (<https://httpie.org>)
# Copyright (c) 2016, Jakub Roztocil, @jkbrzt
# Copyright (c) 2016, Hynek Schlawack, @hynek
#
# This file is licensed under the BSD 3-clause license.
# See the LICENSE file for details.

__all__ = ['__version__', '__author__', '__licence__']
__version__ = '0.9.2-dev'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD License'



# Generated at 2022-06-13 21:07:37.106107
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:49.099215
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie import __version__
    from httpie.client import DEFAULT_UA
    from httpie.plugins.builtin import HTTP_HEAD
    from httpie.compat import is_windows
    from httpie.constants import (
        OUT_REQ_HEAD, OUT_REQ_BODY, OUT_REQ_LINE, OUT_RESP_HEAD,
        OUT_RESP_BODY, OUT_RESP_COOKIE, OUT_RESP_CODE, OUT_RESP_COLOR
    )
    from httpie.downloads import (
        Downloader, DEFAULT_CONTENT_STREAM, DEFAULT_DOWNLOAD_BUFFER_SIZE,
        DEFAULT_DOWNLOAD_MAX_REDIRECTS
    )
    from httpie.output.streams import DEFAULT_STDOUT_REDIRECTED_ENCODING

# Generated at 2022-06-13 21:07:58.430139
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    cli = HTTPieArgumentParser()
    # Unit test for '--auth' option
    args = cli.parse_args([])
    assert hasattr(args, 'auth')
    assert args.auth is None
    args = cli.parse_args(['--auth'])
    assert hasattr(args, 'auth')
    assert args.auth is None
    args = cli.parse_args(['--auth='])
    assert hasattr(args, 'auth')
    assert args.auth is None
    args = cli.parse_args(['--auth', 'test'])
    assert hasattr(args, 'auth')
    assert args.auth == 'test'
    args = cli.parse_args(['--auth', 'test:test'])
    assert hasattr(args, 'auth')

# Generated at 2022-06-13 21:08:07.474627
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    req = 'test/test_request/test_HTTPieArgumentParser_parse_args.txt'
    res = 'test/test_request/test_HTTPieArgumentParser_parse_args.res.txt'
    with open(req) as f:
        args = f.read().strip().split('\n')
    args = HTTPieArgumentParser().parse_args(args)
    with open(res) as f:
        res = f.read().strip()
    assert str(args) == res

# Generated at 2022-06-13 21:08:09.599349
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    p = HTTPieArgumentParser()
    p.parse_args([])

# Generated at 2022-06-13 21:08:13.363766
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args([])


if __name__ == '__main__':
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:08:21.058171
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['http', 'GET', 'http://www.google.com/search?q=httpie'])
    assert len(vars(args)) > 0
    assert 'q' in args.params
    assert 'httpie' in args.params['q']
    assert args.auth_plugin is None
    assert args.auth is None
    assert args.auth_type is None
    assert args.body is None
    assert args.download is False
    assert args.download_resume is False
    assert args.exit_status is False
    assert args.follow is False
    assert args.ignore_netrc is False

# Generated at 2022-06-13 21:08:31.040087
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from io import StringIO
    from httpie.config import merge_dicts
    from httpie.context import Environment
    from httpie.compat import bytes, is_windows
    from httpie.input import ParseError
    from httpie.plugins import plugin_manager
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPPassAuth

    env = Environment(colors=256)
    env.stdin = StringIO()
    env.stdin_isatty = True
    env.stdout_isatty = True
    env.config = {}
    plugin_manager.load_builtin_plugins()
    parser = HTTPieArgumentParser(prog='http', env=env, formatter_class=lambda prog: TestHelpFormatter(prog, max_help_position=40))

# Generated at 2022-06-13 21:10:06.822647
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parse_args_cli = HTTPieArgumentParser().parse_args
    argString = 'httpie http://localhost:8500/v1/agent/self/services'
    args = parse_args_cli(argString.split())
    print(args)
    # Out: Namespace(auth=None, auth_type=None, data=None, download=False, 
    #               download_resume=False, files=None, form=False, headers=[], 
    #               ignore_netrc=False, ignore_stdin=False, 
    #               is_windows=False, json=False, max_redirects=10, method=None, 
    #               output_file=None, output_file_specified=False, output_options=None, 
    #               output_options_history=None, params=None, prett

# Generated at 2022-06-13 21:10:19.008857
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['https://httpbin.org/get', 'My-Key:My-value'])
    assert args.url == 'https://httpbin.org/get'
    assert args.request_items == ['My-Key:My-value']

    args = parser.parse_args(['https://httpbin.org/get', 'My-Key:My-value', '--output' ,'file.txt'])
    assert args.url == 'https://httpbin.org/get'
    assert args.request_items == ['My-Key:My-value']
    assert args.output_file.name == 'file.txt'


# Generated at 2022-06-13 21:10:31.128753
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # We need to instantiate the parser first, so that we can get a fresh
    # idea about the arguments and their values.
    parser = HTTPieArgumentParser()

    arguments = [
        'httpbin.org',
        'get',
        'Accept:application/json',
        'X-API-Token:123',
        'Hello:World',
        'foo=bar',
        'baz=bar'
    ]

    parsed_args = parser.parse_args(arguments)
    assert parsed_args.url == 'http://httpbin.org'
    assert parsed_args.headers['Accept'] == 'application/json'
    assert parsed_args.headers['X-API-Token'] == '123'
    assert parsed_args.headers['Hello'] == 'World'

# Generated at 2022-06-13 21:10:40.275493
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: this method is too large and should be refactored.
    def cli(argv):
        return HTTPieArgumentParser().parse_args(argv)

    res = cli(['http', '--json', '--verbose', '--debug', 'https://httpie.org/'])
    assert res.json
    assert res.verbose
    assert res.debug
    assert res.style == 'solarized'
    assert res.output_file == sys.stdout
    assert res.method == 'GET'

    def test_default_options(argv, style, stdout=sys.stdout):
        res = cli(argv)
        assert res.style == style
        assert res.output_file == stdout
        assert res.output_options == OUTPUT_OPTIONS_DEFAULT


# Generated at 2022-06-13 21:10:49.026769
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Create a parser
    parser = HTTPieArgumentParser()

    # Create the default namespace
    namespace = parser.get_default_namespace()

    # Run the parse_args method and capture the parsed namespace
    args = parser.parse_args(['URL'], namespace=namespace)

    # And check that the namespace has all the right attributes
    assert args.url == "URL"
    assert args.method == "GET"
    assert len(args.headers) == 1
    assert args.headers[0] == ("Accept", "application/json")
    assert args.data is None
    assert args.files is None
    assert args.form is False
    assert args.params is None
    assert args.prettify is True
    assert args.style == "HTTPie"
    assert args.download is False
    assert args.download_res

# Generated at 2022-06-13 21:11:01.577967
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    ###########################################################################
    # Required
    # url: url to connect to
    ###########################################################################
    sys.argv = ['http', 'https://httpbin.org/']
    args = parser.parse_args()
    assert args.url == 'https://httpbin.org/'
    ###########################################################################
    # item: key=value string for POST, PUT
    ###########################################################################
    sys.argv = ['http', 'https://httpbin.org/', 'key1=value1']
    args = parser.parse_args()
    assert args.url == 'https://httpbin.org/'
    assert args.request_items == [KeyValueArgType('key1', 'value1', sep='=')]
    ###########################################################################
    # item

# Generated at 2022-06-13 21:11:14.256671
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # test case 1:
    # input:
    #   obj = HTTPieArgumentParser()
    #   args = ['--version']
    # expected output:
    #   Namespace(debug=False, ignore_stdin=False,
    #       output_file_specified=False, quiet=False, traceback=False,
    #       version=True, verbose=False)
    obj = HTTPieArgumentParser()
    args = ['--version']
    assert obj.parse_args(args) == \
    Namespace(debug=False, ignore_stdin=False, output_file_specified=False, quiet=False, traceback=False, version=True, verbose=False)

    # test case 2:
    # input:
    #   obj = HTTPieArgumentParser()
    #   args = []
    # expected

# Generated at 2022-06-13 21:11:20.854639
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Warning: test only pass if the environnement variable
    """
    #     print("\nTEST HTTPieArgumentParser._parse_args")
    #     print(" !! IF THE TEST CRASH, IT MUST BE TESTED MANUALLY !!")
    #     print(" TO TEST IT, JUST RUN FOR EXAMPLE:")
    #     print("     http --download 127.0.0.1:5000/toilets/1.jpg")
    #     os.environ['LANG'] = "en"
    #     os.environ['TERM'] = "xterm"
    #     parser = HTTPieArgumentParser()
    #     args = parser.parse_args(['--download', "127.0.0.1:5000/toilets/1.jpg"])
    #     assert parser.args.

# Generated at 2022-06-13 21:11:26.169073
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO
    print("Not implemented")

# Generated at 2022-06-13 21:11:31.809135
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args()