

# Generated at 2022-06-13 21:05:06.722725
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Pass in the valid command line arguments - foo bar
    args = parser.parse_args(['foo', 'bar'])
    # Tests if args.foo == 'foo'
    assert args.foo == 'foo'
    # Tests if args.bar == 'bar'
    assert args.bar == 'bar'


# Generated at 2022-06-13 21:05:16.264589
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('-o', '--output-file', action=StoreOnceAction)
    parser.add_argument('-t', '--timeout', type=float, action=StoreOnceAction)
    parser.add_argument('-k', '--insecure', action=StoreTrueOnceAction)
    args = parser.parse_args(['--output-file=file', '--insecure', '-t', '5', '--insecure'])
    
    
    test_file = 'file'
    test_timeout = 5
    
    
    if not args.output_file == test_file:
        print('args.output_file:', args.output_file, 'should be', test_file)
        return 1
    

# Generated at 2022-06-13 21:05:25.760713
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.parse_args(['-f', 'www.httpbin.org', '-A', 'httpbin', 
                       'http://www.httpbin.org/headers', 'Accept:application/*+json'])
    
    return parser.args
# Test HTTPieArgumentParser
parser_args = test_HTTPieArgumentParser_parse_args()
print(parser_args.headers)

# Output
# {'Accept': 'application/*+json'}

# Emulate HTTPie

# Generated at 2022-06-13 21:05:35.236693
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # 1. Setup
    # 1.1. Arguments
    # - Provided Arguments
    arguments_in = ['--ignore-stdin', '--traceback', '--debug', '--pretty', 'all', '--print', 'B', '--history-print', 'hB', '--style', '/Users/riccardo/.config/httpie/styles/parrot.py', '--download', '--output', '/Users/riccardo/Desktop/httpie-completion.bash', 'PUT', 'https://httpbin.org/put', 'user-agent:joe.doe', 'content-type:text/plain', '12345']
    # - Expected Output
    arguments_out = HTTPieArgumentParser(argparse.ArgumentParser, custom_params={'foo': 'bar'}).parse_args(arguments_in)

# Generated at 2022-06-13 21:05:47.856171
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    parser = HTTPieArgumentParser(prog='httpie' , env=Environment(), add_help=False)

    # Test _infer_url_scheme()
    # Test output of method _infer_url_scheme()
    assert parser._infer_url_scheme('http://example.com/') == 'http'
    assert parser._infer_url_scheme('https://example.com/') == 'https'
    assert parser._infer_url_scheme('ws://example.com/') == 'ws'
    assert parser._infer_url_scheme('wss://example.com/') == 'wss'
    assert parser._infer_url_scheme('ftp://example.com/') == 'ftp'
    assert parser._infer_url_scheme('file://example.com/')

# Generated at 2022-06-13 21:05:57.972900
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test for method parse_args of class HTTPieArgumentParser
    import os
    import pytest
    from tempfile import NamedTemporaryFile
    from httpie.core import HTTPieArgumentParser
    from httpie.plugins import plugin_manager
    from httpie.plugins.builtin import DebugPlugin
    from httpie.plugins.builtin import FormAuthPlugin
    from httpie.plugins.builtin import HTTPBasicAuthPlugin
    from httpie.plugins.builtin import HTTPGzipPlugin
    from httpie.plugins.builtin import HTTPX11AuthPlugin
    from httpie.plugins.builtin import NetrcAuthPlugin
    from httpie.plugins.builtin import ResponseHeaders
    from httpie.compat import is_py26
    if is_py26:
        import unittest2 as unittest  # noqa: F

# Generated at 2022-06-13 21:06:12.998780
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    argumentParser = HTTPieArgumentParser()
    args = argumentParser.parse_args(['https://httpbin.org/post', '--form', 'foo=bar', 'zip=zap'])
    assert args.url == 'https://httpbin.org/post'
    assert args.request_items == [KeyValue(key='foo', value='bar', sep='='), KeyValue(key='zip', value='zap', sep='=')]
    with pytest.raises(SystemExit):
        argumentParser.parse_args(['https://httpbin.org/post', '--form', 'foo=bar', 'zip'])
    args = argumentParser.parse_args(['https://httpbin.org/post', '--form', 'foo', 'bar'])

# Generated at 2022-06-13 21:06:19.498028
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:06:25.986498
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    output = parser.parse_args([])
    assert output.exit_status == ExitStatus.OK
    assert output.output_path == None
    assert output.args == ['--form']
    assert output.format == 'pretty'
    assert output.options == {'follow': True}

    output = parser.parse_args(['dummy.txt'])
    assert output.args == ['dummy.txt']


# Generated at 2022-06-13 21:06:36.499733
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:29.828183
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test with a single defined argument
    args = HTTPieArgumentParser().parse_args([
        "--max-redirects", "5"
    ])
    assert args.max_redirects == 5

    # Test with multiple defined arguments
    args = HTTPieArgumentParser().parse_args([
        "--max-redirects", "5",
        "--max-header-count", "10000"
    ])
    assert args.max_redirects == 5
    assert args.max_header_count == 10000

# Generated at 2022-06-13 21:07:31.464701
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie = HTTPieArgumentParser()
    httpie.parse_args()


# Generated at 2022-06-13 21:07:36.431059
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    _ans = parser.parse_args([])

if __name__ == '__main__':
    test_HTTPieArgumentParser_parse_args()
    print('Test finished')

# Generated at 2022-06-13 21:07:38.684519
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = httpie.cli.parser.HTTPieArgumentParser().parse_args()
    assert args.output == sys.stdout

# Generated at 2022-06-13 21:07:50.883718
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ['http', 'localhost:5000/api/v1/auth', 'Content-Type:application/json', 'Accept:application/json',
            'username=admin', 'password=mypass', 'grant_type=password']
    argument_parser = HTTPieArgumentParser()
    httpie_args = argument_parser.parse_args(args)
    log.debug(f'httpie_args: {httpie_args}')

# Generated at 2022-06-13 21:07:59.551275
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    http = HTTPie()
    http.env = Environment()
    parser = HTTPieArgumentParser(prog=BIN_NAME, env=http.env, http=http)
    parser.add_argument('URL', nargs='?', default=None)
    args = parser.parse_args(['http://www.example.com/'])
    assert args.URL == 'http://www.example.com/'
    assert parser.http.args.URL == 'http://www.example.com/'
    assert parser.http.args.headers == []
    assert parser.http.args.output_file_specified == False
    assert parser.http.args.output_file is None
    assert parser.http.args.verbose == False
    assert parser.http.args.all == False
    assert parser.http.args.download == False

# Generated at 2022-06-13 21:08:05.522781
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    print(sys.getdefaultencoding())

# python src/httpie/cli.py url --help
if __name__ == '__main__':
    import sys
    print(__file__, sys.argv)
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:08:07.888018
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(['https://httpbin.org/get', '-H', 'Accept: application/json'])
    print(args)


# Generated at 2022-06-13 21:08:13.661166
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser(env=Environment())
    args = parser.parse_args(['get', 'httpbin.org', 'Accept:text/json'])
    assert isinstance(args, argparse.Namespace)
 

# Generated at 2022-06-13 21:08:21.705646
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import argparse
    args = ['http', '-v', 'http://httpbin.org/get']
    result = HTTPieArgumentParser().parse_args(args)
    assert result.__dict__ == {'form': False,
 'headers': [],
 'ignore_stdin': False,
 'index_errors': {'default': 'default',
  'default_other': 'default_other'},
 'method': 'GET',
 'output_file': None,
 'output_file_specified': False,
 'output_options': 'HBF',
 'output_options_history': 'HBF',
 'stream': False,
 'traceback': False,
 'url': 'http://httpbin.org/get',
 'verbose': True,
 'verify': True}

# Generated at 2022-06-13 21:09:57.965854
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import click
    from click.testing import CliRunner
    # Create an instance of the HTTPieArgumentParser class
    parser = HTTPieArgumentParser()
    # Create an instance of the click.testing.CliRunner class
    runner = CliRunner()

    # Test for a simple POST request
    result = runner.invoke(parser.parse_args, ['POST', 'http://httpbin.org/post'])
    assert result.exit_code == 0
    # Test for a POST request with a data parameter
    result = runner.invoke(parser.parse_args, ['POST', 'http://httpbin.org/post', 'foo=bar'])
    assert result.exit_code == 0
    # Test for a POST request with a header

# Generated at 2022-06-13 21:10:03.845198
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # http --ignore-stdin httpbin.org/post < myfile.txt
    args = ['http', '--ignore-stdin', '--headers', 'Accept:text/html', '--form', '-v', 'httpbin.org/post', 'key=value']
    parser = HTTPieArgumentParser()
    print(parser.parse_args(args))



# Generated at 2022-06-13 21:10:09.766106
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """Unit test for method parse_args of class HTTPieArgumentParser"""

    env = Environment(colors=256,
        stdin_isatty=True,
        stdin=sys.stdin,
        stdout_isatty=True,
        stdout=sys.stdout,
        stderr_isatty=True,
        stderr=sys.stderr,
        stdout_encoding='utf8',
        stdin_encoding='utf8')
    args = Namespace()
    args.headers = []
    args.data = []
    args.params = []
    args.files = []
    args.auth = None
    args.auth_type = None
    args.auth_plugin = None
    args.config_dir = None
    args.config_file = None
    args.output

# Generated at 2022-06-13 21:10:20.189411
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('--foo', dest='foo', type=str)
    parser.add_argument('--bar')
    parser.add_argument('--baz', default=3)
    parser.add_argument('--bool', choices=('true', 'false'), action='store_true', default=True)
    parser.add_argument('--list', type=list)
    args = parser.parse_args(['--foo=bar', '--bar', 'test', '--baz=4', '--bool=false', '--list=a:b:c', '--list=d:e:f'])
    print(args)
    print(args.foo, args.bar, args.baz, args.bool, args.list)
    assert args.foo == 'bar'
   

# Generated at 2022-06-13 21:10:31.093807
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    httpie_argparse = HTTPieArgumentParser()
    args = httpie_argparse.parse_args()
    assert args.auth is None
    assert args.form is False
    assert args.json_param_separators == (',', ':')
    assert args.output_options is None
    assert args.output_options_history is None
    assert args.prettify == PRETTY_STDOUT_TTY_ONLY
    assert args.style == DEFAULT_STYLE
    assert args.style_sheet == DEFAULT_STYLE_SHEET
if __name__ == "__main__":
    test_HTTPieArgumentParser_parse_args()
    test_HTTPieArgumentParser_add_argument()

# Generated at 2022-06-13 21:10:40.275769
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Setup
    http = HTTPieArgumentParser(HTTPie())
    http.args = mock.MagicMock()
    http.args.stdin = ('',)
    args = ['http', 'httpbin.org', 'Content-Type:', 'foo=bar']

    # Exercise
    http.parse_args(args)

    # Verify
    http.args.headers.__setitem__.called_once_with('Content-Type', 'application/json')
    http.args.headers.__getitem__.called_once_with('Content-Type')
    http.args.data.__setitem__.called_once_with('foo', 'bar')
    http.args.data.__getitem__.called_once_with('foo')
    http.args.method = 'POST'

# Generated at 2022-06-13 21:10:49.421023
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.input import KeyValue, KeyValueArgType
    from httpie.cli import environment

    argv = ['--json', 'FOO=BAR', 'BAZ=BAH']

    env = environment.Environment()
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args(argv)

    assert args.json == [KeyValue(KeyValueArgType.SEP_EQUAL, 'FOO', 'BAR')]
    assert args.headers == {'Content-Type': 'application/json',
                            'Accept': 'application/json'}

# Generated at 2022-06-13 21:10:56.396661
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    assert True 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#line:911

#line:1174

#line:1237

#line:1274

#line:1311

#line:1348

#line:1385

#line:1422

#line:1464

#line:1507


#line:1551

#line:1588

#line:1625

#line:1662

#line:1699

#line:1736

#line:1775

#line:1812

#line:1849

#line:1886

#line:1923

#line:1960

#line:1997

# Generated at 2022-06-13 21:11:07.805813
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:11:18.514924
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    config_dir = tempfile.mkdtemp()