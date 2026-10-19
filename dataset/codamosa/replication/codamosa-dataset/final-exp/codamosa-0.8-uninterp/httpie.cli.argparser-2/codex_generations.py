

# Generated at 2022-06-13 21:04:57.214389
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    '''
    Test method parse_args of class HTTPieArgumentParser.
    '''
    args = ['http', '--help']
    test = HTTPieArgumentParser()
    test.parse_args(args=args)
    # Check attributes
    assert test.args.__dict__ == {'help': True}

# Generated at 2022-06-13 21:05:02.848984
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    parser = HTTPieArgumentParser()
    args = parser.parse_args([
        '--json={hello=world}',
    ])
    assert args.json == {'hello': 'world'}
    
    

# Generated at 2022-06-13 21:05:06.950195
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser(env=Environment()).parse_args(
        ['--foo', 'bar', 'baz'])
    assert args.foo == 'bar baz'



# Generated at 2022-06-13 21:05:10.880198
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    with pytest.raises(ParserExit):
        HTTPieArgumentParser().parse_args([])
    try:
        HTTPieArgumentParser().parse_args(['http://httpbin.org/get'])
    except ParserExit:
        assert False


# Generated at 2022-06-13 21:05:15.428059
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # create an instance of the class
    obj = HTTPieArgumentParser(
        args = ['URL'],
        env = Environment(),
        error = Exception
    )

    # try running the method without arguments
    # and check that it raises an exception
    with pytest.raises(Exception) as exception_info:
        obj.parse_args()



# Generated at 2022-06-13 21:05:28.747000
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class MockEnv(object):
        config = None
        colors = 256
        is_windows = False
        stdin = None
        stdin_isatty = True
        stdout = None
        stdout_color_depth = 256
        stdout_isatty = True
        stdout_redirected = False
        stdout_encoding = None
        stderr = None
        stderr_isatty = True
        store_cookies = True
    class MockArgs(object):
        def __init__(self, args_list):
            self.config_path = None
            self.debug_traceback = False
            self.env = MockEnv()
            self.ignore_stdin = False
            self.output_options = None
            self.output_options_history = None
            self.output_file

# Generated at 2022-06-13 21:05:36.076508
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser.parse_args(['http','http://example.com'])
    assert args.url == 'http://example.com'
    assert args.method == 'GET'
    assert args.headers == []
    assert args.params == []
    assert args.output_file_specified is False
    assert args.request_items == []
    assert args.headers == []
    assert args.data == []
    assert args.files == []
    assert args.params == []
    assert args.multipart_data == []
    assert args.auth == None
    assert args.output_file == None
    assert args.output_options == 'HBS'
    assert args.output_options_history == 'HB'
    assert args.download is False
    assert args.download_resume is False
    assert args.request

# Generated at 2022-06-13 21:05:48.928514
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  # Test with default arguments
  args = HTTPieArgumentParser().parse_args().__dict__
  assert args['auth'] == None
  assert args['auth_type'] == 'basic'
  assert args['ignore_stdin'] == False
  assert args['help'] == False
  assert args['headers'] == None
  assert args['headers_arg'] == None
  assert args['host'] == None
  assert args['headers_arg'] == None
  assert args['method'] == None
  assert args['output_file'] == None
  assert args['output_file_specified'] == False
  assert args['output_options'] == None
  assert args['output_options_history'] == None
  assert args['prettify'] == None
  assert args['print_body'] == False
  assert args['print_headers'] == False

# Generated at 2022-06-13 21:05:52.459825
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['GET', 'https://httpbin.org/get'])
    assert(args.url == 'https://httpbin.org/get')
    assert(args.method == 'GET')
    assert(args.json == None)



# Generated at 2022-06-13 21:06:06.325477
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    starting_url = 'http://localhost:8001/api/folder/'
    filename = 'tests/data/testfile.ext'
    # test standalone elements
    print("test standalone elements")
    print("***********************")
    print("test 1")
    args = HTTPieArgumentParser.parse_args(args=[starting_url])
    print(args)
    print("test 2")
    args = HTTPieArgumentParser.parse_args(args=['-h'])
    print(args)
    print("test 3")
    args = HTTPieArgumentParser.parse_args(args=['--version'])
    print(args)
    print("test 4")
    args = HTTPieArgumentParser.parse_args(args=['--download'])
    print(args)
    print("test 5")
    args

# Generated at 2022-06-13 21:07:26.784201
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from tempfile import NamedTemporaryFile
    import argparse
    ################################################################
    #### Begin with the most generic test case: no arguments #######
    ################################################################
    #################################################################################
    #### Test the case where the only argument is the 'help' argument ##############
    #################################################################################
    #################################################################################
    #### Test the case where the only argument is the 'help_all' argument ##########
    #################################################################################
    #################################################################################
    #### Test the case where only '--ignore-stdin' is specified #####################
    #################################################################################
    ################################################################################
    #### Test the case where only '--ignore-stdin' is specified #####################
    ################################################################################
    ################################################################################
    #### Test the case where

# Generated at 2022-06-13 21:07:29.993896
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    with pytest.raises(SystemExit) as exc:
        parser.parse_args(['-V'])
    assert exc.value.code == 0

# Generated at 2022-06-13 21:07:36.292288
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser._validate_args = mock.Mock()
    parser.parse_args(['url'])

# Generated at 2022-06-13 21:07:44.814040
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser.add_argument('--foo', action='store')
    parser.add_argument('--bar', action='store')
    
    args = parser.parse_args(['--foo', '1', '--bar', '2'])
    assert args.foo=='1'
    assert args.bar=='2'
    
    args = parser.parse_args(['--foo', '1', '2', '--bar', '3'])
    assert args.foo=='1'
    assert args.bar=='3'
    

# Generated at 2022-06-13 21:07:55.729447
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    HTTPieArgumentParser set instance attribute args after call method parse_args
    :return:
    """
    args_list = [
        'http',
        '--debug',
        'https://www.google.com',
        '-a',
        'name:value',
        '-o',
        'output.txt',
        '-v',
        'Content-Type'
        '--json'
    ]
    hp = HTTPieArgumentParser()
    hp.parse_args(args=args_list)
    assert len(hp.args.headers) == 1
    assert hp.args.headers[0].key == 'Content-Type'
    assert hp.args.output_file.name == 'output.txt'
    assert hp.args.debug
    assert hp.args.json


# Generated at 2022-06-13 21:08:02.189080
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Test HTTPieArgumentParser parse_args
    request_item_args = [
        'test_key_0=test_value_0',
        'test_key_1=test_value_1',
    ]
    method = 'POST'
    url = 'http://test_url/'
    stdout = io.StringIO()
    stderr = io.StringIO()
    stdin = io.StringIO()
    env = Environment(
        stdout=stdout,
        stderr=stderr,
        stdin=stdin,
    )
    args = HTTPieArgumentParser(env)
    args.prog = 'http'
    # TODO: Make the HTTPieArgumentParser class to be able to accept method, url, request_item_args and return the args object
    # args_output

# Generated at 2022-06-13 21:08:11.367091
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
   parser = HTTPieArgumentParser()
   args = parser.parse_args(['https://example.com/'])
   assert(args.url == "https://example.com/")

test_HTTPieArgumentParser_parse_args()

 
# HTTPieArgumentParser.error() raises SystemExit
# HTTPieArgumentParser.die() raises SystemExit
# HTTPieArgumentParser.exit() raises SystemExit
# HTTPieArgumentParser.print_help() raises SystemExit
# HTTPieArgumentParser.print_usage() raises SystemExit
# HTTPieArgumentParser.format_help() raises SystemExit
# HTTPieArgumentParser.format_usage() raises SystemExit
# HTTPieArgumentParser.format_option_help() raises SystemExit
# HTTPieArgumentParser.format_option_help() raises SystemExit

# HTTPieArg

# Generated at 2022-06-13 21:08:20.981885
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import argparse
    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.plugins import plugin_manager

    env = Environment()
    httpie_args = HTTPieArgumentParser(env=env)
    parser = argparse.ArgumentParser(env=env)
    plugin_manager.load_installed_plugins()

    all_args = ["http","--traceback","--verbose","--print=all","--headers","--style=all", "--download", "--follow", "--max-redirects=10"]

    args = httpie_args.parse_args(all_args)
    assert len(args) == 9

    assert args.traceback
    assert args.verbose
    assert args.output_options == 'ALL'
    assert args.headers
   

# Generated at 2022-06-13 21:08:30.284285
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    '''
    Unit test for method parse_args of class HTTPieArgumentParser
    '''
    http = HTTPieArgumentParser()

    result = http.parse_args(['-o', 'output.txt', '-v', 'google.com'])


# Generated at 2022-06-13 21:08:33.651376
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ["http://www.dlitz.net/software/python-ed25519/"]
    parser = HTTPieArgumentParser()
    parsed = parser.parse_args(args)
    assert parsed.url == args[0]
    assert parser.args.url == args[0]

# Generated at 2022-06-13 21:10:05.972284
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    class Args(object):
        def __init__(self, args):
            self.args = args
    parser = HTTPieArgumentParser()
    parser.env = MockEnvironment()
    parser.env.stdout = io.BytesIO()
    parser.env.stderr = io.BytesIO()
    parser.env.stdin = io.BytesIO()
    parser.env.stdin_isatty = True
    parser.env.stdout_isatty = True
    parser.env.stderr_isatty = True
    test_args = Args([
        'http', 'get', 'url', 'header:value'
    ])
    args = parser.parse_args(test_args.args)
    assert (args.headers == [('header', 'value')])
    
    

# Generated at 2022-06-13 21:10:18.619846
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    class TestEnv:

        def __init__(self):
            self.is_windows = False
            self.stdin = sys.stdin
            self.stdin_isatty = sys.stdin.isatty()
            self.stdout = sys.stdout
            self.stdout_isatty = sys.stdout.isatty()
            self.stdout_encoding = self.stdout.encoding
            self.stderr = sys.stderr
            self.stderr_isatty = sys.stderr.isatty()
            self.stdin_encoding = self.stdin.encoding
            self.stdin_encoding_errors = 'strict'
            self.stdin_raw = self.stdin


    env = TestEnv()

    args = HTTPie

# Generated at 2022-06-13 21:10:20.465323
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    return HTTPieArgumentParser().parse_args(["--debug"])


# Generated at 2022-06-13 21:10:28.076064
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test if, it could be past the same args that a normal parse_args function would produce
    without raising any exceptions.
    """


    args = ['http://httpbin.org/get', 'Accept-Encoding:gzip']

    parser = HTTPieArgumentParser(add_help=False)
    parser.parse_args(args=args)

    # TODO: Improve the unit test, so that we could be sure that the parser made the correct outputs.

# Generated at 2022-06-13 21:10:29.002700
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:10:38.600662
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args('http https://httpbin.org/get')
    assert args.url == 'https://httpbin.org/get'
    assert not args.auth
    assert not args.data
    assert not args.download
    assert not args.files
    assert not args.form
    assert not args.headers
    assert args.help is False
    assert not args.json
    assert not args.params
    assert not args.data_binary
    assert not args.method
    assert not args.output_file
    assert not args.output_file_specified
    assert not args.output_options_history
    assert not args.output_options
    assert args.prettify is False
    assert not args.pretty_options
    assert not args.session
    assert not args.session

# Generated at 2022-06-13 21:10:44.763720
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = np()
    args.url = 'http://www.google.com'
    args.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    args.data = {'key': 'value'}
    args.auth = 'username:password'
    args.download = True
    args.verbose = True
    args.traceback = True
    args.all = True
    args.timeout = 30
    args.cert = 'self-signed.crt'
    args.output_file = 'output-file'
    args.output_options = 'b'
    args.prettify = 'form'
    args.download_resume = True

    # test_parse_args: data_type_group

# Generated at 2022-06-13 21:10:50.666379
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser().parse_args(['--debug', '--timeout=5', 'http://httpbin.org/headers'])
    assert args.debug is True
    assert args.timeout == 5
    assert args.url == 'http://httpbin.org/headers'

    args = HTTPieArgumentParser().parse_args(['http://httpbin.org/headers', ':method=GET', ':path=/get'])
    assert args.url == 'http://httpbin.org/headers'
    assert args.request_items[0].key == 'method'
    assert args.request_items[0].value == 'GET'
    assert args.request_items[1].key == 'path'
    assert args.request_items[1].value == '/get'
import pytest
import sys
from io import StringIO


# Generated at 2022-06-13 21:11:02.117621
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = HTTPieArgumentParser.parse_args(['-h'])
    assert args.help == True

    args = HTTPieArgumentParser.parse_args(['--http2'])
    assert args.http2 == True

    args = HTTPieArgumentParser.parse_args(['--style', 'colors'])
    assert args.style == 'colors'

    args = HTTPieArgumentParser.parse_args(['--print', 'H'])
    assert 'H' in args.output_options

    # TODO: add more test for style/print/style options
    args = HTTPieArgumentParser.parse_args(['--download'])
    assert args.download == True

    args = HTTPieArgumentParser.parse_args(['--json-pp'])
    assert args.json_pp == True




# Generated at 2022-06-13 21:11:14.748746
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # get stdout and stderr from stdout
    sys.stdout = io.StringIO()
    sys.stderr = stream = io.StringIO()
    
    args = ['http', 'https://httpbin.org/headers', 'User-Agent: HTTPie/0.9.9', 'Accept: */*']
    parser = HTTPieArgumentParser()
    try:
        parser.parse_args(args)
    except SystemExit:
        pass
    result = stream.getvalue()
    # release stdout and stderr to stdout
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    
    assert result.startswith("(HTTPieArgs)")
    assert result.endswith("'--ignore-stdin'\n")

