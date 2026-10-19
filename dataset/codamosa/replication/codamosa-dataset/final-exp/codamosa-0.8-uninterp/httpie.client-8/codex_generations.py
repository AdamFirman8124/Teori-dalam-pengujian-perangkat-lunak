

# Generated at 2022-06-13 21:30:27.953333
# Unit test for function collect_messages

# Generated at 2022-06-13 21:30:30.674418
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=None, allow_redirects=False)
    assert make_send_kwargs(args)=={'timeout': None, 'allow_redirects': False}

# Generated at 2022-06-13 21:30:34.892627
# Unit test for function build_requests_session
def test_build_requests_session():
    session = build_requests_session(
        verify=True,
        ssl_version=None,
        ciphers=None
    )
    assert isinstance(session, requests.Session)

# Generated at 2022-06-13 21:30:36.621786
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    kwargs = {'timeout': 15,
              'allow_redirects': False}
    assert make_send_kwargs(kwargs) == kwargs



# Generated at 2022-06-13 21:30:40.716827
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = ''
    request_body_read_callback = None
    messages = collect_messages(args, config_dir, request_body_read_callback)
    assert type(messages) == requests.PreparedRequest


# Generated at 2022-06-13 21:30:55.565549
# Unit test for function collect_messages
def test_collect_messages():
    import httpie.cli.argtypes
    import httpie.cli
    # args is the result returned by parse_args()
    args = httpie.cli.parse_args(
        args=['--auth', 'alice:password1', '--form', 'a=b', 'https://httpbin.org/post'],
        env=None
    )
    # config_dir is the result returned by get_config_dir()
    config_dir = httpie.cli.get_config_dir()
    # Use the arguments above to create an iterator
    code = 0
    for output in collect_messages(args, config_dir):
        # Convert the iterator to a list
        output_list = list(output)
        if type(output_list) != list:
            code = 1

# Generated at 2022-06-13 21:31:05.392954
# Unit test for function make_default_headers
def test_make_default_headers():
    assert sorted(make_default_headers(1).items(), key=lambda x: x[0]) == [('Accept', 'application/json, */*;q=0.5'), ('Content-Type', 'application/json'), ('User-Agent', 'HTTPie/1.0.3')]
    assert sorted(make_default_headers(2).items(), key=lambda x: x[0]) == [('Accept', 'application/json, */*;q=0.5'), ('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8'), ('User-Agent', 'HTTPie/1.0.3')]
    assert make_default_headers(3).get("Content-Type") == None


# Generated at 2022-06-13 21:31:15.964597
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(key=1, value=2)]
    args.verify = "no"
    args.cert = 1
    args.cert_key = 2
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {1: 2}
    assert kwargs['verify'] == False
    assert kwargs['cert'] == (1, 2)

# Generated at 2022-06-13 21:31:19.777722
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == 'HTTPie/1.0.2'
    assert headers['Content-Type'] == 'application/json'
    assert headers['Accept'] == 'application/json, */*;q=0.5'

# Generated at 2022-06-13 21:31:31.870359
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.debug = True
    args.follow = False
    args.max_redirects = 10
    args.max_headers = 500
    args.timeout = 0.5
    args.cert = 'test certificate'
    args.verify = True
    args.ciphers = 'test ciphers'
    args.proxy = None
    args.ssl_version = 'v2'
    args.data = {'name': 'value'}
    args.method = 'GET'
    args.headers = {'Content-Type': 'application/json'}
    args.url = 'http://example.com'
    args.json = True
    args.chunked = True
    args.offline = True

    request_kwargs = make_request_kwargs(args)
   

# Generated at 2022-06-13 21:32:04.239833
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace(
        data=None, files=[], form=False, json=False,
        max_redirects=None, max_headers=None,
        multipart=False, multipart_data=[], chunked=False,
        body_read_callback=None, params=argparse.Namespace(items=[]),
        url='https://httpbin.org/post', method='POST',
        headers=RequestHeadersDict({'User-Agent': 'HTTPie/0.9.9'})
    )

    messages = list(collect_messages(
        args=args,
        config_dir=Path('/Users/mike/.httpie'),
        request_body_read_callback=lambda chunk: chunk
    ))
    assert messages[0].url == 'https://httpbin.org/post'


# Generated at 2022-06-13 21:32:05.244910
# Unit test for function build_requests_session
def test_build_requests_session():
    # TODO
    pass

# Generated at 2022-06-13 21:32:17.792803
# Unit test for function collect_messages
def test_collect_messages():
    request_kwargs = {}
    request_kwargs['method'] = 'POST'
    request_kwargs['url'] = 'https://httpbin.org/post'
    request_kwargs['headers'] = {'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json'}
    request_kwargs['data'] = b''
    request_kwargs['params'] = []
    request_kwargs['auth'] = None
    send_kwargs = {'timeout': None, 'allow_redirects': False}
    send_kwargs_mergeable_from_env = {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}
    request = requests.Request(**request_kwargs)
    prepared_request = requests.Session().prep

# Generated at 2022-06-13 21:32:24.953869
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = ""
    args.cert = None
    args.cert_key = None

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }

    args.proxy = [argparse.Namespace(key='https', value='10.0.0.1:8080')]
    args.verify = 'no'
    cert = 'userCert.pem'
    cert_key = 'userKey.pem'
    args.cert = cert
    args.cert_key = cert_key
    kwargs = make_send_kw

# Generated at 2022-06-13 21:32:35.203636
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = True
    args.cert = None
    args.cert_key = None
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    output = make_send_kwargs_mergeable_from_env(args)
    assert output == expected


# Generated at 2022-06-13 21:32:43.988560
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser(description='test')

    args = parser.parse_args(['-H', 'host: foo'])
    args.json = True
    args.data = {'hello': 'world'}
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA
    assert default_headers['host'] == 'foo'
    assert default_headers['Content-Type'] == 'application/json'
    assert default_headers['Accept'] == JSON_ACCEPT

# Generated at 2022-06-13 21:32:56.112457
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [Proxy('http', 'http://192.168.0.1:80')]
    args.verify = 'false'
    args.cert = '/root/.ssh/id_rsa.pub'
    args.cert_key = '/root/.ssh/id_rsa'

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == {'proxies': {'http': 'http://192.168.0.1:80'},
                      'stream': True, 'verify': False,
                      'cert': ('/root/.ssh/id_rsa.pub', '/root/.ssh/id_rsa')}

# Generated at 2022-06-13 21:33:05.233414
# Unit test for function collect_messages
def test_collect_messages():
    mock_request_body_read_callback = lambda chunk: chunk
    mock_args = argparse.Namespace()
    mock_args.auth = None
    mock_args.auth_type = None
    mock_args.auth_plugin = None
    mock_args.chunked = None
    mock_args.cert = None
    mock_args.cert_key = None
    mock_args.ciphers = None
    mock_args.compress = None
    mock_args.data = None
    mock_args.debug = None
    mock_args.form = None
    mock_args.files = None
    mock_args.headers = {'Content-Type': 'application/json'}
    mock_args.max_headers = None
    mock_args.json = None
    mock_args.multipart = None
   

# Generated at 2022-06-13 21:33:16.768023
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2022-06-13 21:33:22.235389
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    data = PATH_AS_IS_TEST_DATA
    args = []
    for case in data:
        args = case['args']
        kwargs = make_send_kwargs_mergeable_from_env(args)
        if kwargs != case['kwargs']:
            print('test failure')
            print('kwargs actual: %s' % kwargs)
            print('kwargs expect: %s' % case['kwargs'])
            assert kwargs == case['kwargs']


# Generated at 2022-06-13 21:33:53.373804
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'yes'
    args.cert = None
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {}
    assert kwargs['stream'] == True
    assert kwargs['verify'] == True
    assert kwargs['cert'] == None
    #
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'no'
    args.cert = None
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {}
    assert kwargs['stream'] == True
    assert kwargs['verify'] == False

# Generated at 2022-06-13 21:34:02.555102
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:34:13.925602
# Unit test for function collect_messages
def test_collect_messages():
    # Mock the object of Arguments
    class Namespace:
        def __init__(self, arg):
            self.json = arg["json"]
            self.data = arg["data"]
            self.form = arg["form"]
            self.files = arg["files"]
            self.method = arg["method"]
            self.url = arg["url"]
            self.headers = arg["headers"]
            self.max_headers = arg["max_headers"]
            self.params = arg["params"]
            self.auth = arg["auth"]
            self.auth_plugin = arg["auth_plugin"]
            self.timeout = arg["timeout"]
            self.verify = arg["verify"]
            self.cert = arg["cert"]
            self.cert_key = arg["cert_key"]
            self.proxy = arg["proxy"]

# Generated at 2022-06-13 21:34:16.065842
# Unit test for function collect_messages
def test_collect_messages():
    assert collect_messages(args, config_dir)



# Generated at 2022-06-13 21:34:18.744972
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=3.0, follow='True')
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs['allow_redirects'] == False
    assert send_kwargs['timeout'] == 3.0


# Generated at 2022-06-13 21:34:25.889137
# Unit test for function make_default_headers
def test_make_default_headers():
    args = dict()
    args['data'] = None
    args['form'] = None
    args['files'] = None
    args['json'] = None
    assert make_default_headers(args) == {'User-Agent': 'HTTPie/0.9.8'}
    args['data'] = dict()
    assert make_default_headers(args) == {'User-Agent': 'HTTPie/0.9.8', 'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json'}
    args['json'] = False
    assert make_default_headers(args) == {'User-Agent': 'HTTPie/0.9.8', 'Content-Type': 'application/json'}
    args['form'] = True

# Generated at 2022-06-13 21:34:36.157318
# Unit test for function build_requests_session
def test_build_requests_session():
    from httpie.plugins.builtin.transport.http import HTTPTransport
    from httpie.plugins.builtin.transport.https import HTTPSTransport
    session = build_requests_session(
        verify=False,
        ssl_version=None,
        ciphers=None,
    )
    plugin_cls = [cls for cls in plugin_manager.get_transport_plugins() if cls.prefix == 'http'][0]
    transport_plugin = plugin_cls()
    assert isinstance(transport_plugin, HTTPTransport)
    assert session.adapters['http://'].cert_verify is False
    assert session.adapters['http://'].ssl_version is None
    assert session.adapters['http://'].ciphers is None

# Generated at 2022-06-13 21:34:46.286355
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = None
    args.data = None
    args.form = None
    args.files = None
    args.headers = RequestHeadersDict()
    default_headers = make_default_headers(args)
    assert default_headers == RequestHeadersDict({'User-Agent': DEFAULT_UA})

    args.json = True
    args.data = 4
    default_headers = make_default_headers(args)
    assert default_headers == RequestHeadersDict({
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE,
        'User-Agent': DEFAULT_UA
    })

    args.json = True
    args.data = None
    default_headers = make_default_headers(args)
    assert default_headers

# Generated at 2022-06-13 21:34:53.843738
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args1 = argparse.Namespace()
    args1.timeout = 10
    assert(make_send_kwargs(args1)['timeout'] == 10)

    args2 = argparse.Namespace()
    assert('timeout' not in make_send_kwargs(args2))

    args3 = argparse.Namespace()
    args3.timeout = -1
    assert('timeout' not in make_send_kwargs(args3))



# Generated at 2022-06-13 21:35:01.135940
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    r = make_default_headers(args)
    assert r['Accept'] == JSON_ACCEPT
    assert r['Content-Type'] == JSON_CONTENT_TYPE
    args = argparse.Namespace()
    args.form = True
    r = make_default_headers(args)
    assert r['Content-Type'] == FORM_CONTENT_TYPE
    args = argparse.Namespace()
    args.files = True
    r = make_default_headers(args)
    assert 'Content-Type' not in r
    args = argparse.Namespace()
    args.data = True
    args.files = True
    r = make_default_headers(args)
    assert 'Content-Type' not in r
    args = argparse.Namespace()


# Generated at 2022-06-13 21:35:43.529300
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [
        argparse.Namespace(key='http', value='http://http.proxy:3128/'),
        argparse.Namespace(key='https', value='http://https.proxy:3128/')]
    args.verify = 'true'
    args.cert = '/foo/cert.pem'
    args.cert_key = '/foo/cert_key.pem'
    kwargs = make_send_kwargs_mergeable_from_env(args)

# Generated at 2022-06-13 21:35:52.825219
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        chunked=False,
        data=None,
        files=argparse.Namespace(),
        form=False,
        headers={
            'Content-Type': 'application/json'
        },
        json=False,
        method='get',
        offline=False,
        params={},
        session=None,
        session_read_only=False,
        success_codes=[2],
        timeout=None,
        url='https://localhost:8000/auth',
        verify=False,
        auth_plugin=None,
        chunked_transfer_encoding=True,
        debug=False,
        path_as_is=False,
        upload_files=[]
    )


# Generated at 2022-06-13 21:36:00.574254
# Unit test for function collect_messages
def test_collect_messages():
    return
    print ('test_collect_messages')
    import Args
    from Plugins import AuthPlugin
    args = Args.parser.parse_args([
        '-v',
        '-t', '1',
        'get',
        'http://httpbin.org/',
    ])
    args.auth_plugin = AuthPlugin.BasicAuthPlugin()
    args.auth_plugin.add_auth('username', 'password')
    list(collect_messages(args, '', None))

# Generated at 2022-06-13 21:36:09.048694
# Unit test for function max_headers
def test_max_headers():
    import http.client
    import httpie.core

    args = argparse.Namespace(headers=['a: 1', 'b: 1', 'c: 1', 'd: 1', 'e: 1', 'f: 1', 'g: 1', 'h: 1', 'i: 1', 'j: 1', 'k: 1'])
    httpie.core.max_headers(args)
    assert http.client._MAXHEADERS == 11

# Generated at 2022-06-13 21:36:16.993961
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = ['http=127.0.0.1', 'https=10.0.0.1']
    args.verify = "none"
    args.cert = '/dev/null'

    expected_result = {
        'proxies': {'http': '127.0.0.1', 'https': '10.0.0.1'},
        'stream': True,
        'verify': False,
        'cert': '/dev/null'
    }

    assert make_send_kwargs_mergeable_from_env(args) == expected_result

# Generated at 2022-06-13 21:36:28.109655
# Unit test for function collect_messages
def test_collect_messages():
    import argparse
    args = argparse.Namespace()
    args.url = 'https://www.google.com'
    args.headers = {'User-Agent': 'HTTPie/1.0.0'}
    args.json = True
    args.data = {'q': 'foo'}
    # args.offline = True
    args.path_as_is = True
    # args.debug = True
    args.compress = 1
    args.offline = False
    args.follow = True
    args.all = True
    args.cert = None
    args.cert_key = None
    args.timeout = 20
    args.auth = None
    args.verify = 'yes'
    args.files = None
    args.form = False
    args.multipart = False
    args.mult

# Generated at 2022-06-13 21:36:33.414747
# Unit test for function max_headers
def test_max_headers():
    limit = 100
    orig_limit = http.client._MAXHEADERS
    http.client._MAXHEADERS = "this will not work"
    try:
        with max_headers(limit):
            assert http.client._MAXHEADERS == limit
    except:
        raise AssertionError("Max-headers test failed")
    finally:
        http.client._MAXHEADERS = orig_limit


# Generated at 2022-06-13 21:36:39.378405
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = None
    args.verify = True
    args.cert = None
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None
    }
    args.proxy = []
    args.verify = False
    args.cert = "asdf"
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == {
        'proxies': {},
        'stream': True,
        'verify': False,
        'cert': "asdf"
    }

# Generated at 2022-06-13 21:36:43.502720
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser()
    args = parser.parse_args([""])
    headers_dict = make_default_headers(args)
    assert headers_dict['User-Agent'] == f"HTTPie/{__version__}"


# Generated at 2022-06-13 21:36:46.884354
# Unit test for function max_headers
def test_max_headers():
    with max_headers(2):
        assert (http.client._MAXHEADERS == 2)

# Generated at 2022-06-13 21:38:00.563233
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.verify = "yes"
    args.proxy = []
    args.cert_key = None
    args.cert = None

    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env["verify"] == True

# Generated at 2022-06-13 21:38:06.840890
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace
    config_dir = Path
    request_body_read_callback = Callable[[bytes], None]
    test_return = collect_messages(
        args,
        config_dir,
        request_body_read_callback
    )
    assert isinstance(test_return, Iterable)


# Generated at 2022-06-13 21:38:08.551155
# Unit test for function collect_messages
def test_collect_messages():
    import sys
    print(sys.path)
    print('hello')

# Generated at 2022-06-13 21:38:15.373158
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli.args import parser
    from httpie.session import Session
    import os
    import tempfile
    from .mocking import MockResponse, MockSessionRedirect
    parser.add_argument('--verify', metavar='yes/no', default='yes', help="Whether to verify the server's TLS certificate. Defaults to 'yes'.", choices=('yes', 'no', 'true', 'false'))
    args = parser.parse_args("get http://127.0.0.1:8080/".split())
    config_dir = os.path.expanduser('~')
    httpie_session = get_httpie_session(config_dir, None, None, None)
    assert httpie_session is not None, \
        "Something went wrong in initializing the httpie session"

# Generated at 2022-06-13 21:38:23.671709
# Unit test for function make_default_headers
def test_make_default_headers():
    args = type('FakeArgs', (), {'json': False, 'form': False, 'data': None})
    assert 'User-Agent' in make_default_headers(args)
    args = type('FakeArgs', (), {'json': True, 'form': False, 'data': None})
    assert 'Accept' in make_default_headers(args)
    assert 'Content-Type' not in make_default_headers(args)
    args = type('FakeArgs', (), {'json': False, 'form': True, 'data': None})
    assert 'Content-Type' in make_default_headers(args)
    assert 'Accept' not in make_default_headers(args)

# Generated at 2022-06-13 21:38:31.731604
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    requests.request(**{
        'data': None,
        'url': 'https://www.yahoo.com',
        'headers': {
            'Content-Length': None,
            'User-Agent': 'HTTPie/0.9.9',
            'Accept': 'application/json, */*;q=0.5'
        },
        'auth': None,
        'params': [
            ('foo', 'bar'),
            ('fiz', 'fuz')
        ],
        'method': 'GET'
    })

# Generated at 2022-06-13 21:38:44.250551
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://google.com'
    args.files = None
    args.data = {'test': 'test'}
    args.form = False
    args.json = True
    args.headers = {'test': 'test'}
    args.offline = False
    args.chunked = True
    args.auth = False
    args.params = {'test': 'test'}
    kwargs = make_request_kwargs(args)
    assert(kwargs['method'] == args.method.lower())
    assert(kwargs['url'] == args.url)
    assert(kwargs['data'] != None)
    assert(kwargs['auth'] == args.auth)


# Generated at 2022-06-13 21:38:47.096872
# Unit test for function max_headers
def test_max_headers():
    try:
        with max_headers(0):
            sys.stderr.write(str(http.client._MAXHEADERS))
    except AttributeError:
        pass

# Generated at 2022-06-13 21:38:52.213994
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(
        proxy=[],
        verify='True'
    )
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None
    }

# Generated at 2022-06-13 21:38:58.725366
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(method='POST', url='http://localhost:8000/', headers={'accept': 'application/json'}, data={'a': 1, 'b': '2'}, json=False, form=False, files=[], auth=None, params=[], chunked=False, timeout=10, verify=False, cert=None, cert_key=None, proxy=[], debug=False, session=None, session_read_only=None, auth_plugin=None, max_headers=200, max_redirects=10, path_as_is=False, follow=False, all=False, offline=False, chunk_size=4096, compress=0, multipart=False, multipart_data=[], boundary=None)
    print(make_request_kwargs(args))
