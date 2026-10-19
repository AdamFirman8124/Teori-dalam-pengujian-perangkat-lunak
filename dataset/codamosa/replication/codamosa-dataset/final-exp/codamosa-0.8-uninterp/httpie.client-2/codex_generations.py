

# Generated at 2022-06-13 21:30:04.201913
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = {'httpp1.1': 'http://127.0.0.1:8080',
                  'httpp1.2': 'http://127.0.0.1:8090'}
    args.verify = 'yes'
    args.cert = r'C:\Users\Chamith\Downloads\httpie.pem'
    args.cert_key = r'C:\Users\Chamith\Downloads\httpie.key'
    kwargs = make_send_kwargs_mergeable_from_env(args)

# Generated at 2022-06-13 21:30:08.206541
# Unit test for function max_headers
def test_max_headers():
    http.client._MAXHEADERS = 1
    assert http.client._MAXHEADERS == 1
    with max_headers(None):
        assert http.client._MAXHEADERS == float('inf')
    assert http.client._MAXHEADERS == 1

# Generated at 2022-06-13 21:30:13.711305
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = ['http://a', 'http://b']
    args.verify = 'yes'
    args.cert = 'a'
    args.cert_key = 'b'
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert(kwargs['proxies']) == ({'http': 'http://a', 'https': 'http://a'}, {'http': 'http://b', 'https': 'http://b'})
    assert(kwargs['verify']) == True
    assert(kwargs['cert']) == ('a', 'b')

# Generated at 2022-06-13 21:30:17.933508
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true')
    #parser.add_argument('--form', action='store_true')
    parser.add_argument('--data', type=None, default={'foo': 'bar'})
    args = parser.parse_args(args=[])
    print(make_default_headers(args))

# Generated at 2022-06-13 21:30:27.359879
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    case_true = ['true', 'TRUE', 'True', 'yes', 'YES', 'Yes', '1', 'on', 'ON', 'On']
    case_false = ['false', 'FALSE', 'False', 'no', 'NO', 'No', '0', 'off', 'OFF', 'Off']

    for v in case_true:
        kwargs = make_send_kwargs_mergeable_from_env({'verify': v})
        assert kwargs['verify'] is True
    for v in case_false:
        kwargs = make_send_kwargs_mergeable_from_env({'verify': v})
        assert kwargs['verify'] is False

# Generated at 2022-06-13 21:30:35.516843
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.ArgumentParser().parse_args([])
    actual = make_send_kwargs_mergeable_from_env(args)
    expected = {
        'proxies': {},
        'stream': True,
        'verify': {
            'yes': True,
            'true': True,
            'no': False,
            'false': False,
        }.get('yes', 'yes'),
        'cert': 'yes',
    }
    assert actual == expected


# Generated at 2022-06-13 21:30:40.090959
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path('config_dir')
    request_body_read_callback = lambda chunk: chunk
    iterable = collect_messages(args, config_dir, request_body_read_callback)
    for i in iterable:
        print(i)

# Generated at 2022-06-13 21:30:47.902237
# Unit test for function collect_messages
def test_collect_messages():
    # Test cases
    class TestCase:
        """
        Test cases for collect_messages

        Arguments
        ----------
        args: argparse.Namespace
        config_dir: Path
        request_body_read_callback: Callable[[bytes], None]
        expected_messages: Union[requests.PreparedRequest, requests.Response]
        """
        def __init__(
            self,
            args: argparse.Namespace,
            config_dir: Path,
            request_body_read_callback: Callable[[bytes], None],
            expected_messages: Union[requests.PreparedRequest, requests.Response],
        ):
            self.args = args
            self.config_dir = config_dir
            self.request_body_read_callback = request_body_read_callback
            self.expected_mess

# Generated at 2022-06-13 21:31:01.414148
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        auth=None,
        cert=None,
        cert_key=None,
        chunked=False,
        data=None,
        form=False,
        files=None,
        json=False,
        max_headers=None,
        max_redirects=None,
        multipart=False,
        multipart_data=None,
        no_content_length=False,
        method="GET",
        offline=False,
        params=(),
        path_as_is=False,
        stream=False,
        timeout=None,
        url="ipinfo.io",
        verify=False,
        verbose=False,
        verbose_body=False,
        headers={})
    kwargs = make_request_kwargs(args)

    assert kw

# Generated at 2022-06-13 21:31:05.221996
# Unit test for function build_requests_session
def test_build_requests_session():
    """
    >>> session = build_requests_session(ssl_version=False)
    >>> session.adapters['https://'].verify_mode = ssl.CERT_NONE
    >>> assert session.adapters['https://'].verify_mode = ssl.CERT_NONE
    """



# Generated at 2022-06-13 21:31:42.862849
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(proxy=None, verify='False', cert=None, cert_key=None)
    assert make_send_kwargs_mergeable_from_env(args) == {'verify': False, 'proxies': {}, 'stream': True, 'cert': None}

    args = argparse.Namespace(proxy=None, verify='False', cert='abc', cert_key='def')
    assert make_send_kwargs_mergeable_from_env(args) == {'verify': False, 'proxies': {}, 'stream': True, 'cert': ('abc', 'def')}


# Generated at 2022-06-13 21:31:48.835948
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path()
    request_body_read_callback = lambda chunk: chunk

    messages = collect_messages(args, config_dir, request_body_read_callback)
    assert type(next(messages)) == requests.PreparedRequest
    assert type(next(messages)) == requests.Response

# Generated at 2022-06-13 21:31:54.964270
# Unit test for function make_default_headers
def test_make_default_headers():
    print("\nUnit test for function make_default_headers(args):")
    from httpie.cli.parser import get_parser
    args = get_parser().parse_args([])
    for key, value in make_default_headers(args).items():
        print(key, ':', value)

# Generated at 2022-06-13 21:32:02.401539
# Unit test for function make_default_headers
def test_make_default_headers():
    from httpie.cli.argtypes import KeyValueArg, KeyValueArgType

    args = argparse.Namespace()
    args.data = None
    args.form = None
    args.json = False
    args.headers = KeyValueArgType(KeyValueArg, multiple=True)()

    result_headers = make_default_headers(args)

    assert isinstance(result_headers, RequestHeadersDict)
    assert result_headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in result_headers
    assert 'Content-Type' not in result_headers



# Generated at 2022-06-13 21:32:10.851702
# Unit test for function build_requests_session
def test_build_requests_session():
    # build_requests_session(
    #     verify=False,
    #     ssl_version='tlsv1_2',
    #     ciphers=None,
    # )
    print(build_requests_session(False, 'tlsv1_2', None))
    print(build_requests_session(False, None, None))
    print(build_requests_session(False, 'tlsv1_2', 'cipher'))
    print(build_requests_session(False, 'tlsv1_2', ''))


# Generated at 2022-06-13 21:32:13.250092
# Unit test for function max_headers
def test_max_headers():
    with max_headers(4):
        assert http.client._MAXHEADERS == 4
    assert http.client._MAXHEADERS == 100


# Generated at 2022-06-13 21:32:25.017678
# Unit test for function max_headers
def test_max_headers():
    from httpie.client.__main__ import main
    from httpie.sessions import get_httpie_session
    import os

    httpie_session = get_httpie_session(
        config_dir=os.path.join(
            os.path.expanduser('~'),'.httpie'),
        session_name="testname",
        host='httpbin.org',
        url='http://httpbin.org/post',
    )

    httpie_session.headers['foo'] = ('bar'*1024)
    httpie_session.headers['too'] = ('many'*1024)

    httpie_session.save()


# Generated at 2022-06-13 21:32:27.983722
# Unit test for function collect_messages
def test_collect_messages():
    return


# Generated at 2022-06-13 21:32:36.422671
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args=argparse.Namespace(
        ssl_version=None,
        ciphers=None,
        verify=None,
        cert=None,
        cert_key=None,
        proxy=None,
        allow_redirects=True,
        off = False,
    )
    expected = {
        'proxies': None,
        'verify': True,
        'cert': None,
    }
    assert make_send_kwargs_mergeable_from_env(args)==expected

# Generated at 2022-06-13 21:32:44.327150
# Unit test for function collect_messages

# Generated at 2022-06-13 21:33:16.445314
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.plugins import AuthPlugin, AuthCredentials, Environment
    from requests.auth import HTTPBasicAuth

    # create a fake plugin so that we can add our credentials to it
    plugin = AuthPlugin(
        'fake_plugin',
        'fake_plugin',
        'Fake Auth Plugin for tests',
        {},
        {'scheme': 'http'}
    )

    # create dummy credentials and add them to our fake plugin
    credentials = AuthCredentials()
    credentials.raw_auth = 'foo:bar'
    credentials.auth = HTTPBasicAuth('foo', 'bar')
    plugin.credentials_cls = AuthCredentials

    env = Environment()
    env.add_plugin(plugin)

    # create a dummy args namespace to pass to our function
    args = argparse.Namespace()
    args.auth

# Generated at 2022-06-13 21:33:23.842802
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        auth = '(user:pass)',
        chunked = False,
        data = "hello python",
        files = None,
        form = True,
        json = None,
        method = 'POST',
        multipart = False,
        multipart_data = None,
        proxy = None,
        url = 'https://www.baidu.com',
        verify = 'yes',
        headers = {
            'Cookies': 'name=value; name2=value2',
            'Transfer-Encoding': 'chunked',
            'Content-Length': '11'
        },
        params = {'aa': 'bb'}
    )
    base_headers = {
        'Host': 'www.baidu.com',
    }
    request_body_read_callback

# Generated at 2022-06-13 21:33:37.574381
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2022-06-13 21:33:43.470260
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    class Args:
        def __init__(self):
            self.timeout = 30
            self.follow = True
    args = Args()
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] == 30
    assert kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:33:57.237695
# Unit test for function make_default_headers
def test_make_default_headers():
	args = argparse.Namespace(
        data = str(),
        form = False,
        json = False,
        files = False
    )

	default_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })

	auto_json = args.data and not args.form
	if args.json or auto_json:
		default_headers['Accept'] = JSON_ACCEPT
		if args.json or (auto_json and args.data):
			default_headers['Content-Type'] = JSON_CONTENT_TYPE

	elif args.form and not args.files:
		# If sending files, `requests` will set
		# the `Content-Type` for us.
		default_headers['Content-Type'] = FORM_CONTENT_TYPE


# Generated at 2022-06-13 21:34:11.981626
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    from httpie import main
    from io import BytesIO
    args = main.parse_args([
        'http', '--verbose', 'http://httpbin.org/get'
    ])
    args.headers = dict()
    args.form = True
    args.data = {'from': 'user', 'passwd': 'pass'}
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['url'] == 'http://httpbin.org/get'
    assert request_kwargs['method'] == 'get'
    expected_data = b'from=user&passwd=pass'
    assert request_kwargs['data'].read() == expected_data
    assert request_kwargs['files'] == []
    assert request_kwargs['headers']['Content-Type'] == FORM_

# Generated at 2022-06-13 21:34:15.127794
# Unit test for function build_requests_session
def test_build_requests_session():
    try:
        if build_requests_session(verify=False) is not None:
            print("build_requests_session test succeed")
        else:
            print("build_requests_session test failed")
    except requests.exceptions.HTTPError as err:
        print(err)


# Generated at 2022-06-13 21:34:18.430324
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    test_args = make_send_kwargs(args)
    assert test_args == {'timeout': None, 'allow_redirects': False}



# Generated at 2022-06-13 21:34:21.382470
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    kwargs = make_send_kwargs(args)
    assert kwargs == {
        "timeout": None,
        "allow_redirects": False
    }


# Generated at 2022-06-13 21:34:34.255875
# Unit test for function make_default_headers

# Generated at 2022-06-13 21:35:12.286719
# Unit test for function make_default_headers
def test_make_default_headers():
    test_args = argparse.Namespace()
    default_headers = make_default_headers(test_args)
    assert default_headers == {'User-Agent': DEFAULT_UA}

# Generated at 2022-06-13 21:35:19.137287
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.registry import plugin_manager
    # Remove all plugins and reload only the default ones
    plugin_manager.clear_registration_cache()
    plugin_manager._deprecated_plugins = []
    FormatterPlugin.get_plugins()
    results = list(collect_messages(
        RequestHeadersDict({'X-Test': 'foo'}),
        'POST',
        request_body_read_callback=None,
    ))
    assert results[0].method == 'POST'

# Generated at 2022-06-13 21:35:32.976735
# Unit test for function max_headers
def test_max_headers():
    from httpie.stream import write_chunk_headers
    
    # Without max_headers
    response_headers = {
        'Transfer-Encoding': 'chunked',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Server': 'AIOHTTP/3.6.2',
        'Date': 'Sun, 17 Nov 2019 00:41:34 GMT',
        'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
        'Access-Control-Allow-Origin': '*'
    }
    # Without max_header, no truncation
    test_headers = write_chunk_headers(response_headers)

# Generated at 2022-06-13 21:35:40.602595
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:35:51.027592
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    """
    The code should be able to handle different type of args.
    """
    arg_dict = {"method": 'GET', "url": 'http://127.0.0.1', "headers": {"header1": "value1"}, "data": '{"name": "x"}',\
    "auth": None, "params": [('name', 'x'), ('age', '20')]}
    ret = make_request_kwargs(arg_dict)
    assert ret['method'] == 'get'
    assert ret['url'] == 'http://127.0.0.1'
    assert ret['headers']['header1'] == 'value1'
    assert ret['params'] == [('name', 'x'), ('age', '20')]

# Generated at 2022-06-13 21:35:58.462452
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[],
        verify='True'
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    assert make_send_kwargs_mergeable_from_env(args) == expected
    


# Generated at 2022-06-13 21:36:03.821493
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'true'
    args.cert = ''
    args.cert_key = ''
    assert make_send_kwargs_mergeable_from_env(args) == {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}
    args.proxy = [argparse.Namespace(key='test', value='test')]
    args.verify = 'yes'
    assert make_send_kwargs_mergeable_from_env(args) == {'proxies': {'test': 'test'}, 'stream': True, 'verify': True, 'cert': None}
    args.proxy = []
    args.verify = 'no'
    assert make_send_kwargs_merge

# Generated at 2022-06-13 21:36:15.474797
# Unit test for function collect_messages
def test_collect_messages():
    import os
    import requests
    from requests.adapters import HTTPAdapter

    from httpie.sessions import get_session_dir, Session
    from httpie.context import Environment

    from httpie.plugins.transport.http import HTTPTransport

    from httpie import __version__
    from httpie.cli.dicts import RequestHeadersDict

    def make_env(args_namespace):
        class MockEnv(Environment):

            def __init__(self):
                self.args = args_namespace

        return MockEnv()


# Generated at 2022-06-13 21:36:20.994682
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    # go to "path/to/httpie". Assert we're in the right directory.
    config_dir = Path('.').resolve()
    # go to "path/to/httpie/tests"
    config_dir = config_dir / 'tests'
    request_body_read_callback = lambda chunk: chunk
    # noinspection PyTypeChecker
    messages = collect_messages(args,config_dir,request_body_read_callback)
    for message in messages:
        if type(message) is requests.PreparedRequest:
            print(message)
        elif type(message) is requests.Response:
            print (message)

# Generated at 2022-06-13 21:36:27.463062
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        json=False,
        form=False,
        files=[],
        data={},
        headers={})
    expected_default_headers = {
        'User-Agent': DEFAULT_UA
    }
    default_headers = make_default_headers(args)
    assert default_headers == expected_default_headers



# Generated at 2022-06-13 21:37:45.836392
# Unit test for function make_send_kwargs

# Generated at 2022-06-13 21:37:47.882073
# Unit test for function max_headers
def test_max_headers():
    with max_headers(3):
        # noinspection PyProtectedMember
        assert http.client._MAXHEADERS == 3

# Generated at 2022-06-13 21:37:52.917892
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.headers = {}
    args.json = False
    headers = make_default_headers(args)
    assert isinstance(headers, dict)
    assert headers['User-Agent'] == DEFAULT_UA


# Generated at 2022-06-13 21:37:56.388993
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path('httpie/')
    collect_messages(args=args,
                     config_dir=config_dir)

# Generated at 2022-06-13 21:37:59.690169
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    expected_default_headers = {'User-Agent': f'HTTPie/{__version__}'}
    assert make_default_headers(args) == expected_default_headers

# Generated at 2022-06-13 21:38:05.605792
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = ['-H', 'content-type: application/json', 'www.google.com']
    args = httpie.cli.parser.parse_args(args)
    assert make_send_kwargs_mergeable_from_env(args) == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None
    }

# Generated at 2022-06-13 21:38:14.292588
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'no'
    args.proxy = []
    args.cert = 'cert'
    args.cert_key = 'cert_key'
    a = make_send_kwargs_mergeable_from_env(args)
    assert a['proxies'] == {}
    assert a['stream'] == True
    assert a['verify'] == False
    assert a['cert'] == 'cert'
    assert a['cert_key'] is None


# Generated at 2022-06-13 21:38:24.159613
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(key=1, value=1)]
    args.verify = 'yes'
    args.cert = 'yes'
    args.cert_key = 'yes'
    print(make_send_kwargs_mergeable_from_env(args))


# Generated at 2022-06-13 21:38:30.767269
# Unit test for function make_default_headers
def test_make_default_headers():
    # Arrange
    args = argparse.Namespace()
    args.headers = {}
    args.files = None
    args.data = None
    args.json = False
    args.form = False
    # Act
    ret = make_default_headers(args)
    # Assert
    assert ret == {'User-Agent': 'HTTPie/1.0.2'}


# Generated at 2022-06-13 21:38:34.681268
# Unit test for function max_headers
def test_max_headers():
    try:
        with max_headers(2):
            assert http.client._MAXHEADERS == 2
        assert http.client._MAXHEADERS == 1000
    except:
        return False
    return True