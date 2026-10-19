

# Generated at 2022-06-13 21:30:27.263366
# Unit test for function max_headers
def test_max_headers():
    # test for overflow
    http.client._MAXHEADERS = 32
    with max_headers(0):
        assert http.client._MAXHEADERS == float('inf')
    # test for same value
    http.client._MAXHEADERS = 32
    with max_headers(32):
        assert http.client._MAXHEADERS == 32
    # test for smaller value
    http.client._MAXHEADERS = 32
    with max_headers(31):
        assert http.client._MAXHEADERS == 31

# Generated at 2022-06-13 21:30:33.177884
# Unit test for function make_default_headers
def test_make_default_headers():
    args=argparse.Namespace(data="", form=0,json=1, files=0, timeout=0, verify=0, cert=0, cert_key=0, proxy=[], max_redirects=0, chunked=0, max_headers=0, session="", session_read_only=0, headers=(), auth="", params=0, debug=0, all=0, follow=0, offline=0, output="", auth_plugin="")
    return make_default_headers(args)
    test_make_default_headers()

# Generated at 2022-06-13 21:30:45.337294
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # This function takes in the given args, and parses it into a dictionary.
    url = 'http://httpbin.org/ip'
    method = 'get'
    args = argparse.Namespace()
    args.url = url
    args.method = method
    args.auth = ''
    args.auth_type = ''
    args.auth_plugin = 'None'
    args.headers = {}
    args.params = {}
    args.data = {}
    args.files = None
    args.form = False
    args.json = False
    args.compress = False
    args.verbose = False
    args.all = False
    args.offline = False
    args.output = None
    args.pretty = False
    args.style = 'None'
    args.download = False

# Generated at 2022-06-13 21:30:53.107776
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env['verify'] is None
    assert send_kwargs_mergeable_from_env['cert'] is None
    args = argparse.Namespace()
    args.verify = True
    args.cert = 'foo'
    args.cert_key = 'bar'
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env['verify'] is True
    assert send_kwargs_mergeable_from_env['cert'] == ('foo','bar')

# Generated at 2022-06-13 21:31:04.801540
# Unit test for function collect_messages

# Generated at 2022-06-13 21:31:18.704821
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()

    _env = ('http', '127.0.0.1', '8881', '', '', '')
    os.environ['HTTPIE_PROXY'] = 'http://127.0.0.1:8881'
    args.proxy = [os.environ['HTTPIE_PROXY']]
    assert(make_send_kwargs_mergeable_from_env(args)['proxies'] == {'http': '127.0.0.1:8881'})

    os.environ['HTTPIE_VERIFY'] = 'no'
    assert(make_send_kwargs_mergeable_from_env(args)['verify'] == False)

    os.environ['HTTPIE_VERIFY'] = 'true'

# Generated at 2022-06-13 21:31:31.026959
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import httpie.cli.parser
    args = httpie.cli.parser.parse_args(['--json', '--data', '{"key": "value"}', '--url', 'https://httpbin.org/post', '--no-verify'])
    request_kwargs = make_request_kwargs(args)
    assert(request_kwargs['method'] == 'post')
    assert(request_kwargs['url'] == 'https://httpbin.org/post')
    assert(request_kwargs['headers']['Accept'] == 'application/json, */*;q=0.5')
    assert(request_kwargs['headers']['Content-Type'] == 'application/json')
    assert(request_kwargs['data'].decode() == '{"key": "value"}')

# Generated at 2022-06-13 21:31:37.646920
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    test_data = {
    "kwargs":{},
    "kwargs_mergeable_from_env":{
        "proxies": {},
        "verify" : True
        }
    }

    # Test case: Test make_send_kwargs if no args in Namespace
    result = make_send_kwargs(argparse.Namespace())
    assert result == test_data["kwargs"]

    # Test case: Test make_send_kwargs if args in Namespace
    test_args = argparse.Namespace(verify = 'yes', timeout = 10, proxy = [])
    test_args.proxy.append(argparse.Namespace(key = 'abc', value = 'def'))

# Generated at 2022-06-13 21:31:39.336215
# Unit test for function max_headers
def test_max_headers():
    """
    Test for function max_headers
    """
    max_headers(10)

# Generated at 2022-06-13 21:31:48.024244
# Unit test for function make_request_kwargs
def test_make_request_kwargs():

    args = argparse.Namespace(
        auth=None,
        auth_plugin=None,
        chunked=False,
        cert=None,
        cert_key=None,
        data=None,
        files=None,
        form=False,
        headers=RequestHeadersDict(),
        json=False,
        method='get',
        timeout=None,
        url='http://example.com/',
        params=[],
        verify='yes',
        session=None,
        session_read_only=None,
        offline=False,
        multipart_data=[],
        multipart=False,
        boundary=None
    )

    base_headers = RequestHeadersDict()
    base_headers['content-type'] = 'application/json'

# Generated at 2022-06-13 21:32:23.754497
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://www.baidu.com'
    # Finalize headers.
    headers = make_default_headers(args)
    headers.update({'Host':'www.baidu.com'})
    headers = finalize_headers(headers)
    # Serialize JSON data, if needed.
    data = {"key1":"value1","key2":"value2"}
    auto_json = data and not args.form
    if (args.json or auto_json) and isinstance(data, dict):
        if data:
            data = json.dumps(data)

# Generated at 2022-06-13 21:32:33.524159
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.verify = 'true'
    args.proxy = [1, 2, 3]

    ans = make_send_kwargs_mergeable_from_env(args)
    assert ans['verify'] == True
    assert ans['proxies'] == [1, 2, 3]

# Generated at 2022-06-13 21:32:47.462409
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    # DEFAULT
    args = argparse.Namespace()
    args.timeout = None
    args.allow_redirects = False
    args.verify = None
    args.proxy = None
    args.cert_key = None
    args.cert = None
    args.max_redirects = None
    send_kwargs = make_send_kwargs(args)
    assert ('timeout' in send_kwargs)
    assert ('allow_redirects' in send_kwargs)
    assert (not ('verify' in send_kwargs))
    assert (not ('proxy' in send_kwargs))
    assert (not ('cert_key' in send_kwargs))
    assert (not ('cert' in send_kwargs))
    assert (not ('max_redirects' in send_kwargs))

# Generated at 2022-06-13 21:32:59.992314
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(auth=None, chunked=False, data=None, form=False, files=None, follow=False, json=False, max_redirects=None, max_headers=None, method='GET', multiform=[], multipart=False, params=[], path_as_is=False, session=None, session_read_only=None, timeout=None, url='http://httpbin.org/get', verify=True, cert=None, cert_key=None, proxy=[], headers={}, data_explicit=False, json_explicit=False)
    base_headers = RequestHeadersDict()
    kwargs = make_request_kwargs(args, base_headers)
    assert kwargs['method'] == 'get'

# Generated at 2022-06-13 21:33:07.508150
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import argparse
    args = argparse.Namespace()
    args.url = 'http://localhost'
    args.method = 'post'
    args.params = {}
    args.json = False
    args.form = False
    args.data = {'name': 'foo'}
    args.auth = ''
    args.headers = {}
    args.files = False
    args.compress = False
    args.timeout = None
    args.verify = 'yes'
    args.cert = ''
    args.cert_key = ''
    args.json_pp = False
    args.follow = False
    args.max_redirects = 10
    args.offline = False
    args.websocket = False
    args.all = False
    args.debug = False
    kwargs = make_request_

# Generated at 2022-06-13 21:33:08.750502
# Unit test for function make_default_headers
def test_make_default_headers():
    make_default_headers(args)

# Generated at 2022-06-13 21:33:12.951050
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    argv = ["-a", "test"]
    args = parser.parse_args(argv)
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] is None
    assert kwargs['allow_redirects'] is False


# Generated at 2022-06-13 21:33:18.729108
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    namespace_args = argparse.Namespace()
    namespace_args.verify = 'true'
    namespace_args.proxy = []
    namespace_args.cert = None
    namespace_args.cert_key = None

    actual = make_send_kwargs_mergeable_from_env(namespace_args)
    expected = {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}
    assert actual == expected

# Generated at 2022-06-13 21:33:28.556292
# Unit test for function build_requests_session
def test_build_requests_session():
    assert build_requests_session(verify=True, ssl_version='TLSv1_2', ciphers="EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH EDH+aRSA !RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS")

# Generated at 2022-06-13 21:33:35.907198
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # Arrange
    args = argparse.Namespace()
    args.verify = 'yes'
    args.cert = None
    args.cert_key = None
    args.proxy = [argparse.Namespace]
    args.proxy[0].key = 'http'
    args.proxy[0].value = 'http://127.0.0.1'

    # Act
    r = make_send_kwargs_mergeable_from_env(args)

    # Assert
    assert r



# Generated at 2022-06-13 21:34:01.021350
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path.cwd()
    result = list(collect_messages(args, config_dir))
    assert result[-1] == None

# Generated at 2022-06-13 21:34:06.560269
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 2
    args.allow_redirects = False
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs['timeout'] == 2
    assert send_kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:34:12.660051
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    kwargs = make_send_kwargs(args)
    assert('timeout' in kwargs)
    assert(kwargs['timeout'] == args.timeout)
    assert('allow_redirects' in kwargs)
    assert(kwargs['allow_redirects'] == args.allow_redirects)



# Generated at 2022-06-13 21:34:20.971079
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.headers = ['Content-Type: json']
    args.timeout = 30
    args.verify = True
    args.cert = "cert"
    args.cert_key = "cert_key"
    args.proxy = ['http:localhost:8080']
    args.url = 'http://www.example.com'
    request_kwargs = make_request_kwargs(args=args)
    assert request_kwargs['timeout'] == args.timeout
    assert request_kwargs['headers'] == args.headers


# Generated at 2022-06-13 21:34:23.881275
# Unit test for function max_headers
def test_max_headers():
    from httpie.core import main as httpie_core

    parsed_args = httpie_core.parser_for_main().parse_args(
        ['--debug', '--max-headers', '5', 'GET', 'http://google.com'])
    _ = collect_messages(parsed_args, Path(), None)

# Generated at 2022-06-13 21:34:35.482517
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:34:39.313964
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.data = None
    args.form = None
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:34:43.900382
# Unit test for function max_headers
def test_max_headers():
    import httpie.cli
    args = httpie.cli.parser.parse_args(['--max-headers', '5',
                                         'https://httpbin.org/headers'])
    for _ in collect_messages(args, config_dir=None):
        pass
    assert http.client._MAXHEADERS == 5

# Generated at 2022-06-13 21:34:51.506148
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data = {},
        json = False,
        form = False,
    )
    default_headers = make_default_headers(args)
    print("\n",default_headers,"\n")
    assert default_headers == {'User-Agent': 'HTTPie/2.2.0'}


# Generated at 2022-06-13 21:34:55.849626
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    class MockedArgs:
        def __init__(self):
            self.proxy = []
            self.verify = False
            self.cert = None
            self.cert_key = None

        def __repr__(self):
            attrs = vars(self)
            return ', '.join("%s: %s" % item for item in attrs.items())

    args = MockedArgs()
    arg_dict = make_send_kwargs_mergeable_from_env(args)
    assert arg_dict['proxy'] == {}
    assert arg_dict['verify'] is False
    assert arg_dict['cert'] is None

    args.verify = "false"
    args.cert = "httpie.cert"
    args.cert_key = "httpie.key"
    assert make_send_kwargs

# Generated at 2022-06-13 21:35:19.404990
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    assert make_request_kwargs(args=None, base_headers=None,
                               request_body_read_callback=None) == {}



# Generated at 2022-06-13 21:35:20.581864
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    pass

# Generated at 2022-06-13 21:35:33.805487
# Unit test for function make_default_headers
def test_make_default_headers():
    headers = make_default_headers(argparse.Namespace(json=True, data=None, form=False))
    assert headers['Accept'] == JSON_ACCEPT
    assert 'Content-Type' not in headers

    headers = make_default_headers(argparse.Namespace(json=False, data=None, form=True))
    assert 'Accept' not in headers
    assert 'Content-Type' in headers

    headers = make_default_headers(argparse.Namespace(json=True, data='foo', form=False))
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

    headers = make_default_headers(argparse.Namespace(json=True, data={}, form=False))
    assert headers['Accept'] == JSON_ACCEPT

# Generated at 2022-06-13 21:35:40.504359
# Unit test for function max_headers
def test_max_headers():
    import http.client

    assert http.client._MAXHEADERS == 1000  # Default number of allowed headers

    http.client._MAXHEADERS = 800

    with max_headers(1):
        assert http.client._MAXHEADERS == 1

    assert http.client._MAXHEADERS == 800

    with max_headers(None):
        assert http.client._MAXHEADERS == float('inf')

    assert http.client._MAXHEADERS == 800



# Generated at 2022-06-13 21:35:51.575223
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.context import Environment
    import os

    os.environ['http_proxy'] = 'http://234.23.11.1:9999'
    os.environ['https_proxy'] = 'http://234.23.11.2:9999'
    os.environ['no_proxy'] = 'baidu.com,a.com'
    os.environ['HTTP_PROXY'] = 'http://234.23.11.3:9999'
    os.environ['HTTPS_PROXY'] = 'http://234.23.11.4:9999'
    os.environ['NO_PROXY'] = 'c.com,d.com'
    os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/asd/cert.pem'
    os.environ

# Generated at 2022-06-13 21:36:02.697574
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float, default=None)
    parser.add_argument('--follow', action='store_true')
    args = parser.parse_args(args=[])
    expected_kwargs = {
        'timeout': None,
        'allow_redirects': False,
    }
    assert make_send_kwargs(args) == expected_kwargs
    args = parser.parse_args(args=['--timeout', '0.2'])
    expected_kwargs = {
        'timeout': 0.2,
        'allow_redirects': False,
    }
    assert make_send_kwargs(args) == expected_kwargs
    parser.add_argument('--follow', action='store_true')
    args = parser.parse

# Generated at 2022-06-13 21:36:15.029240
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(method="get", url="http://example.com/")
    args.headers = dict()
    args.json = None
    args.data = None
    args.form = None
    args.files = None

    actual = make_default_headers(args)
    expected = {'User-Agent': DEFAULT_UA}
    assert actual == expected

    # See https://github.com/jakubroztocil/httpie/issues/212
    args = argparse.Namespace(method="get", url="http://example.com/")
    args.headers = dict(":")
    args.json = None
    args.data = None
    args.form = None
    args.files = None
    actual = make_default_headers(args)

# Generated at 2022-06-13 21:36:17.009211
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    assert make_send_kwargs({}) == {
        'timeout': None,
        'allow_redirects': False,
    }



# Generated at 2022-06-13 21:36:22.525858
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.data = ['a', 'b']
    args.headers = ['a', 'b', 'A-Header']
    args.json = True
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA
    assert default_headers['Content-Type'] == JSON_CONTENT_TYPE
    assert default_headers['Accept'] == JSON_ACCEPT
    assert default_headers['A-Header'] == 'b'

# Generated at 2022-06-13 21:36:30.962373
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    args.proxy = ""
    args.stream = True
    args.verify = True
    args.cert = None
    res = make_send_kwargs(args)
    assert res == {'timeout': 10, 'allow_redirects': False, 'stream': True, 'verify': True, 'cert': None}

# Generated at 2022-06-13 21:37:03.948575
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:37:14.500613
# Unit test for function make_default_headers
def test_make_default_headers():
    from httpie import ExitStatus
    from httpie.cli import parser
    from httpie.context import Environment
    from httpie.plugins import manager as plugin_manager
    plugin_manager.load_installed_plugins()
    env = Environment()
    args = parser.parse_args([
        'GET',
        'https://www.baidu.com/'
    ])
    env.config['default_options'] = [
        'pretty=all',
        'style=monokai'
    ]
    env.config['output_options'] = {
        'pretty': 'all',
        'style': 'monokai',
        'format': 'colors',
        'stream': 'stdout'
    }
    env.stdout = io.BytesIO()
    args.colors = True
    args.stream = True
   

# Generated at 2022-06-13 21:37:25.467206
# Unit test for function collect_messages
def test_collect_messages():
    import os
    import shutil
    from tempfile import TemporaryDirectory
    from httpie import ExitStatus
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.cli.parser import get_parser
    from httpie.compat import is_windows
    from httpie.context import Environment

    def get_exit_status(kwargs):
        with TemporaryDirectory() as config_dir:
            # For some reason, this needs to be done in order for the
            # tests to pass on Windows.
            config_dir = Path(config_dir)

            # needed to make plugins work
            os.environ['HTTPIE_CONFIG_DIR'] = str(config_dir)
            kwargs['config_dir'] = config_dir
            kwargs['env'] = Environment()
            parser = get_parser()
            args

# Generated at 2022-06-13 21:37:36.976987
# Unit test for function collect_messages

# Generated at 2022-06-13 21:37:48.440598
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2022-06-13 21:38:00.933637
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # Arrange
    args = argparse.Namespace(
        cert='/home/user/test.pem',
        cert_key='/home/user/test.key',
        proxy=[
            argparse.Namespace(key='http', value='test_value'),
            argparse.Namespace(key='http', value='test_value2')
        ],
        verify='yes',
    )
    expected_kwargs = {
        'proxies': {'http': 'test_value'},
        'stream': True,
        'verify': True,
        'cert': ('/home/user/test.pem', '/home/user/test.key'),
    }

    # Act
    kwargs = make_send_kwargs_mergeable_from_env(args)

    # Assert

# Generated at 2022-06-13 21:38:04.304777
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(True, 'TLSv1_1', None)



# Generated at 2022-06-13 21:38:06.963955
# Unit test for function max_headers
def test_max_headers():
    with max_headers(10):
        assert http.client._MAXHEADERS == 10  # noqa
    assert http.client._MAXHEADERS != 10  # noqa

# Generated at 2022-06-13 21:38:18.267746
# Unit test for function make_send_kwargs

# Generated at 2022-06-13 21:38:29.124851
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = [
        '-t', 'foo',
        '--download', '/tmp'
    ]
    args_namespace = parse_args(args)
    send_kwargs = make_send_kwargs(args_namespace)
    assert send_kwargs['timeout'] == 'foo'
    assert send_kwargs['stream'] is True
    assert 'verify' not in send_kwargs
    assert 'proxies' not in send_kwargs
    assert 'cert' not in send_kwargs

# Generated at 2022-06-13 21:39:13.382189
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = type("Args", (object,), {"verify": True, "cert": "certfile",\
    "cert_key": "certkey", "proxy": [("http://localhost","")]})
    assert make_send_kwargs_mergeable_from_env(args)["proxies"] == {"http://localhost":""}
    assert make_send_kwargs_mergeable_from_env(args)["verify"] == True
    assert make_send_kwargs_mergeable_from_env(args)["cert"] == "certfile"

# Generated at 2022-06-13 21:39:15.759031
# Unit test for function max_headers
def test_max_headers():
    with max_headers(1) as r:
        assert r == None
    with max_headers(None) as r:
        assert r == None

# Generated at 2022-06-13 21:39:18.829636
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data=None,
        files=None,
        form=False,
        json=False,
    )
    default_headers = make_default_headers(args)
    assert default_headers == {'User-Agent': DEFAULT_UA}


# Generated at 2022-06-13 21:39:29.848323
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:39:40.193673
# Unit test for function make_default_headers
def test_make_default_headers():
    headers = make_default_headers(None)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers.get('Accept') == None

    args = mock.MagicMock()
    args.json = True
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers.get('Accept') == JSON_ACCEPT
    assert headers.get('Content-Type') == None

    args.form = True
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers.get('Accept') == JSON_ACCEPT
    assert headers.get('Content-Type') == FORM_CONTENT_TYPE

# Generated at 2022-06-13 21:39:48.092703
# Unit test for function make_default_headers
def test_make_default_headers():
    class args(argparse.Namespace):
        def __init__(self):
            self.data = None
            self.form = None
            self.json = None
            self.headers = RequestHeadersDict()

    print(make_default_headers(args()))

    args.json = True
    print(make_default_headers(args()))

    args.json = False
    args.headers['Content-Type'] = "application/json"
    args.data = '{}'
    print(make_default_headers(args()))

    args.data = None
    args.form = True
    print(make_default_headers(args()))

    args.form = False
    args.data = {}
    print(make_default_headers(args()))

    args.data = None