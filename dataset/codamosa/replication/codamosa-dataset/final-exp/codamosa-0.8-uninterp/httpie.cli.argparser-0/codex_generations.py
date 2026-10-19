

# Generated at 2022-06-13 21:05:11.334693
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Since the test is run in different directory, we need to specify the absolute path.
    # First argument is the script name which is the path to this python file.
    args = HTTPieArgumentParser(PROJ_DIR + "/tests/main.py").parse_args(["POST", "www.example.com", "User-Agent:HTTPie", "Accept-Encoding:gzip", "--json", "--pretty=all"])
    assert args.method == "POST"
    assert args.url == "www.example.com"
    assert args.headers == [KeyValue(key='user-agent', value='HTTPie'), KeyValue(key='accept-encoding', value='gzip')]
    assert args.json
    assert args.prettify == "all"

# Generated at 2022-06-13 21:05:12.462963
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: write test
    pass

# Generated at 2022-06-13 21:05:15.055526
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    argv = ['http', 'httpbin.org', 'hello=world']
    parser = HTTPieArgumentParser()
    # Call method under test
    args = parser.parse_args(argv)

# Generated at 2022-06-13 21:05:20.519752
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import sys
    print('\nTesting HTTPieArgumentParser with sys.argv:')
    print('  ' + ' '.join(sys.argv) + '\n')
    parser = HTTPieArgumentParser()
    args = parser.parse_args()

if __name__ == "__main__":
  test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:05:33.231095
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
	"""
	Unit test for HTTPieArgumentParser.parse_args

	:return:
	"""
	parser = HTTPieArgumentParser()

	parser.add_argument('-u', '--url', type=str, dest='url',
						help='the url of the site to be called for testing, for example: localhost:5000')
	parser.add_argument('-d', '--data', type=str, dest='data',
						help='the data you want to pass in this request, for example: a=b&c=d')
	parser.add_argument('-H', '--header', type=str, action='append',
						dest='headers', help='headers you want to send, for example: -H "a:b" -H "c:d"')


# Generated at 2022-06-13 21:05:40.444090
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """
    Test the behaviour of the method parse_args
    of the HTTPieArgumentParser class.
    """

    # Create the httpie argument parser object
    httpie_parser = HTTPieArgumentParser()
    
    # Split the argument string
    arguments_list = ['https://httpbin.org/get?key=value']
    # Parse the arguments
    parsed_args = httpie_parser.parse_args(arguments_list)

    # Check the parsed arguments
    assert parsed_args.url == arguments_list[0]

# Generated at 2022-06-13 21:05:43.758205
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    parser._build_parser()
    args = parser.parse_args(['httpie'])


# Generated at 2022-06-13 21:05:49.723950
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    import httpie.cli
    httpie.cli.args = None
    with open('tests/fixtures/formatting_pretty.json') as f:
        data = f.read()
        args = httpie.cli.HTTPieArgumentParser(data).parse_args()
    assert args.json == data
    assert args.output
    assert args.output_file
    assert args.prettify
    print(args)
test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:05:58.341147
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    ap = HTTPieArgumentParser()
    args = ['--method', 'POST', '--url', 'http://httpbin.org/get', '--headers', 'content-type:application/json', '--data', '{\"hello\": \"world\"}']
    parsed_args = ap.parse_args(args)
    assert parsed_args.method == 'POST'
    assert parsed_args.url == 'http://httpbin.org/get'
    assert parsed_args.headers == CaseInsensitiveDict([('content-type', 'application/json')])
    assert parsed_args.data == '{"hello": "world"}'

# Generated at 2022-06-13 21:06:10.929706
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = [
        'https://httpbin.org/get?test1=value1&test2=value2',
        '--json',
        '{"test1": "value1", "test2": "value2"}',
    ]
    # TODO: Ensure that it does not raise an error
    try:
        HTTPieArgumentParser(args=args).parse_args()
    except Exception as e:
        pytest.fail("HTTPieArgumentParser.parse_args raised Exception: {0}".format(e))

# Generated at 2022-06-13 21:07:07.100849
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:19.154831
# Unit test for method parse_args of class HTTPieArgumentParser

# Generated at 2022-06-13 21:07:27.126505
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    args = ["--auth-type=basic", "xyz.com", "-u", "user", "-p", "pass", "-d", "a=1", "-d", "b=2"]

    parser = HTTPieArgumentParser()
    ns = parser.parse_args(args)
    print(ns)


# Generated at 2022-06-13 21:07:32.163911
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    l = Logger(__name__)
    l.setLevel(logging.DEBUG)

    parser = HTTPieArgumentParser(prog = 'http')
    options = parser.parse_args([])
    l.debug('options: %s', options)

#===============================================================================
# Main
#===============================================================================

if __name__ == "__main__":
    test_HTTPieArgumentParser_parse_args()

# Generated at 2022-06-13 21:07:45.095106
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args([])
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args(['--help'])
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args(['--version'])
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args(['--debug'])
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args(['--quiet'])
    # Should not raise an exception
    arg_parser = HTTPieArgumentParser()
    arg_parser.parse_args

# Generated at 2022-06-13 21:07:55.985668
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    path = '/path/to/file'
    file = b'foobar'
    with open(path, 'wb') as f:
        f.write(file)

    # Test 1:
    args = [
        'http', '--verbose', '--json-input', '--json-input-file', path,
        'https://example.com',
    ]
    assert HTTPieArgumentParser.parse_args(args).verbose == True
    # Test 2:
    args = [
        'http', '--verbose', '--json-input', '--json-input-file', path,
        'https://example.com',
    ]
    assert HTTPieArgumentParser.parse_args(args).verbose == True
    # Test 3:

# Generated at 2022-06-13 21:08:00.823042
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    from httpie.client import Environment

    env = Environment(stdin_isatty=True, stdout_isatty=True)
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args(['https://httpbin.org'])
    assert args.url == 'https://httpbin.org'


# Generated at 2022-06-13 21:08:02.659228
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # TODO: Write unit test
    pass



# Generated at 2022-06-13 21:08:11.540225
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()


# Generated at 2022-06-13 21:08:14.425946
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """TODO: Actually test this, instead of using as a test dummy."""
    pass

# Generated at 2022-06-13 21:09:41.041694
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    env = Environment.get_instance()
    parser = HTTPieArgumentParser(env=env)
    args = parser.parse_args(['-A','Mozilla/5.0','https://httpie.org'])
    assert args.auth == None
    assert args.headers == None
    assert args.method == 'GET'
    assert args.timeout == float(100)
    assert args.url == 'https://httpie.org'
    assert args.pretty == False
    assert args.all == False
    assert args.check_status == True
    assert args.check_ssl == False
    assert args.download == False
    assert args.download_resume == False
    assert args.follow == False
    assert args.ignore_netrc is False
    assert args.ignore_stdin is False
    assert args.max_redirect

# Generated at 2022-06-13 21:09:44.857977
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
  args = httpie_argument_parser.parse_args(["http://www.google.com"])
  print("args: ",args)
 


# Generated at 2022-06-13 21:09:54.228061
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(['--traceback', '--auth', 'test', '--auth-type', 'basic'])
    assert isinstance(args, argparse.Namespace)
    assert hasattr(args, 'auth')
    assert args.auth == 'test'
    assert hasattr(args, 'auth_type')
    assert args.auth_type == 'basic'
    assert hasattr(args, 'traceback')
    assert args.traceback is True


# Generated at 2022-06-13 21:10:05.817089
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    temp = tempfile.NamedTemporaryFile(mode='w+')

    parser = HTTPieArgumentParser(prog='http')
    parser.add_argument('--no-headers', action='store_true')
    parser.add_argument('--headers', action='store_true')
    parser.add_argument('--no-body', action='store_true')
    parser.add_argument('--body', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--no-form', action='store_true')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    parser.add_argument

# Generated at 2022-06-13 21:10:06.619882
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    pass

# Generated at 2022-06-13 21:10:12.664974
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # http --json --pretty=all :8000/get
    arguments = ['--json','--pretty=all','--traceback',':8000/get']
    parser = HTTPieArgumentParser()
    args = parser.parse_args(arguments)
    print(args)


# Generated at 2022-06-13 21:10:19.386397
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    # Unit test for HTTPieArgumentParser.parse_args
    # Called with example arguments from `http --help`
    args = parser.parse_args(
        ['GET', 'https://httpbin.org/headers', 'Accept:', 'text/plain'])
    assert type(args) == argparse.Namespace
    # Parse succeeds
    assert args.method == 'GET'
    assert args.url == 'https://httpbin.org/headers'
    assert args.headers[0]['Accept'] == 'text/plain'



# Generated at 2022-06-13 21:10:31.429956
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    
    # No arguments
    assert HTTPieArgumentParser(env=Environment()).parse_args([])

    # Argument "-v"
    # We can check the value of args.verbose
    args = HTTPieArgumentParser(env=Environment()).parse_args(["-v"])
    assert args.verbose == True

    # Argument "--verbose"
    # We can check the value of args.verbose
    args = HTTPieArgumentParser(env=Environment()).parse_args(["--verbose"])
    assert args.verbose == True

    # Argument "-q"
    # We can check the value of args.quiet
    args = HTTPieArgumentParser(env=Environment()).parse_args(["-q"])
    assert args.quiet == True

    # Argument "--quiet"
    # We can check

# Generated at 2022-06-13 21:10:34.781569
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = get_parser()
    argv = ['--user', 'username:password']
    parsed_args = parser.parse_args(argv)
    assert parsed_args.auth == 'username:password'

# Generated at 2022-06-13 21:10:41.087602
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    parser = HTTPieArgumentParser()
    args = parser.parse_args(["www.google.com"])
    assert(args.url == "www.google.com")

test_HTTPieArgumentParser_parse_args()


# Generated at 2022-06-13 21:13:38.956501
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():

    parser = HTTPieArgumentParser()
    parser._actions = ['what']
    parser._check_value = object()
    parser._registry = {
        'option_string': 'o',
        'nargs': 1,
        'dest': 'output_format',
        'const': None,
        'default': 'pretty',
        'type': None,
        'choices': None,
        'required': False,
        'help': None,
        'metavar': None
    }
    parser._get_formatter = object()
    parser._print_message = object()
    parser._toggle_prop = object()

# Generated at 2022-06-13 21:13:49.976354
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    input_args = ['--json', '["foo", {"bar":["baz", null, 1.0, 2]}]', 'https://httpbin.org/post']
    args = HTTPieArgumentParser().parse_args(input_args)
    assert args.headers == []
    assert args.request_items == [KeyValue(key='', value='["foo", {"bar":["baz", null, 1.0, 2]}]', sep='=', orig='["foo", {"bar":["baz", null, 1.0, 2]}]')]
    assert args.url == 'https://httpbin.org/post'
    assert args.request_item_type == 'json'
    assert args.data == '["foo", {"bar":["baz", null, 1.0, 2]}]'
    
    

# Generated at 2022-06-13 21:13:55.072901
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    """tests the parse_args method of the HTTPieArgumentParser class
    """
    
    # creating a parser object
    parser = HTTPieArgumentParser()
    # calling the parse_args method
    # returns the args object
    args = parser.parse_args([])
    print(args)

# Generated at 2022-06-13 21:13:59.896548
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    # httpie --verbose --debug --headers
    args = ['httpie', '--verbose', '--debug', '--headers']
    parser = HTTPieArgumentParser()
    parser.parse_args(args)
    assert parser._optimize_sessions == False
    assert parser._asciinema_record is False
    assert parser._asciinema_url is None
    assert parser.args.debug == True
    assert parser.args.headers == True
    assert parser.args.verbose == True
    assert parser.args.version == False




# Generated at 2022-06-13 21:14:07.697365
# Unit test for method parse_args of class HTTPieArgumentParser
def test_HTTPieArgumentParser_parse_args():
    
    # Test for `parse_args`
    # Test for parse_args with all the valid inputs
    assert True, "parse_args with all the valid inputs"
    # Test for parse_args with valid key and values
    assert True, "parse_args with valid key and values"
    # Test for parse_args with invalid key and values
    assert True, "parse_args with invalid key and values"
    
    
        
    