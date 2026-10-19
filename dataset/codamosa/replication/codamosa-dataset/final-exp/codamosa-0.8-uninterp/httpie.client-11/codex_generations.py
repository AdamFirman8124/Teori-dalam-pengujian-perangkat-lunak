

# Generated at 2022-06-13 21:30:02.856596
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    import argparse

    parser = argparse.ArgumentParser(prog="http", add_help=False)
    parser._actions.append(argparse.Action('--timeout', type=int))
    parser._option_string_actions['--timeout'] = parser._actions[-1]
    args = parser.parse_args(['--timeout', '10'])
    args.proxy = []
    args.verify = ''
    args.certs = {}
    kwargs = make_send_kwargs(args)
    print(kwargs)

# Generated at 2022-06-13 21:30:05.588488
# Unit test for function make_default_headers
def test_make_default_headers():
    args = []
    args.append('cmd')
    args.append('http')


    # Test if the default headers are correct
    if make_default_headers(args).get('User-Agent') == 'HTTPie/' + __version__:
        pass
    else:
        raise Exception("Default headers error")

# Generated at 2022-06-13 21:30:13.844938
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import argparse
    args = argparse.Namespace()
    args.method = "GET"
    args.url = "http://localhost:8080/"
    args.timeout = 5
    args.headers = {'Content-Type':'application/json'}
    args.data = {"name":"Darth Vader", "profession":"Sith Lord"}
    args.json = True
    args.verify = False
    args.auth = ("admin", "admin")
    args.params = {'embed':'records'}
    args.chunked = False
    args.offline = False
    args.path_as_is = ""
    args.form = False
    args.compress = False
    args.debug = False
    args.multipart = False
    args.files = ""
    args.max_redirect

# Generated at 2022-06-13 21:30:26.372223
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.cli import parser

    parse_kwargs = {
        'prog': 'http',
        'description': 'HTTPie %s, a CLI, cURL-like tool for humans.' % __version__
    }
    args = parser.parse_args(args=[], **parse_kwargs)

    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert isinstance(send_kwargs_mergeable_from_env, dict)
    print(send_kwargs_mergeable_from_env)
    assert send_kwargs_mergeable_from_env is not None
    assert send_kwargs_mergeable_from_env['proxies'] == {}

# Generated at 2022-06-13 21:30:31.920296
# Unit test for function max_headers
def test_max_headers():
    limit = 2
    headers = [
        ('User-Agent', 'HTTPie/0.9.9'),
        ('Accept', '*/*'),
        ('Host', 'httpbin.org'),
    ]
    with max_headers(limit):
        conn = http.client.HTTPConnection('httpbin.org')
        conn.request('GET', '/headers', headers=headers)
        resp = conn.getresponse()

# Generated at 2022-06-13 21:30:44.429859
# Unit test for function collect_messages
def test_collect_messages():
    class LineBuffer:
        def __init__(self):
            self.lines = []

        def reset(self):
            self.lines = []

        def write(self, line: str):
            self.lines.append(line)

    class ArgsMock:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    class Response:
        def __init__(self, url: str, next: object, body: str):
            self.url = url
            self.next = next
            self.body = body


# Generated at 2022-06-13 21:30:52.681335
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    """
    Unit test for function make_request_kwargs
    """
    args = argparse.Namespace(method='get', url='https://httpbin.org/post', data='{"key1": "value1"}', json="true", files=True, form = False,
                              params='{"key1": "value1"}', headers=['Accept: application/json'], auth=("user", "passwd"))
    base_headers = RequestHeadersDict()
    request_body_read_callback = lambda data: data

    final_args = make_request_kwargs(
        args=args,
        base_headers=base_headers,
        request_body_read_callback=request_body_read_callback
    )
    # print("final_args: ", final_args)


# Generated at 2022-06-13 21:30:57.194057
# Unit test for function make_default_headers
def test_make_default_headers():
    json_headers = make_default_headers(argparse.Namespace(json=True, data={'foo': 'barr'}))
    assert json_headers['Content-Type'] == JSON_CONTENT_TYPE
    assert json_headers['Accept'] == JSON_ACCEPT



# Generated at 2022-06-13 21:31:06.631151
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.url = "127.0.0.1"
    args.headers = {
        'Content-Type': 'application/json'
    }
    args.data = "this is test"
    args.json = True
    args.method = 'post'
    args.auth = "test"
    args.params = {
        "p1":"v1",
        "p2":"v2"
    }
    args.cert = "test"
    args.cert_key = "test"
    args.proxy = {
        "p1":"v1",
        "p2":"v2"
    }
    args.verify = 'test'
    args.chunked = True
    args.offline = True
    result = make_request_kwargs(args)


# Generated at 2022-06-13 21:31:13.249951
# Unit test for function max_headers
def test_max_headers():
    conn = http.client.HTTPConnection
    try:
        with max_headers(100):
            assert http.client._MAXHEADERS == 100
        assert http.client._MAXHEADERS == 100000
    finally:
        http.client._MAXHEADERS = 100000

# Generated at 2022-06-13 21:31:35.774700
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    args.form = True
    args.data = True
    args.headers = True
    result = make_default_headers(args)
    print(result)



# Generated at 2022-06-13 21:31:39.872520
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = {}
    print(make_default_headers(args))

# Generated at 2022-06-13 21:31:51.684942
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # given
    r = requests.Session()
    r.proxies = {'http': 'http://localhost:3128', 'https': 'http://localhost:1080'}
    r.cert = ('/path/client.cert', '/path/client.key')
    r.verify = False

    mock_args = argparse.Namespace()
    mock_args.proxy = [
        argparse.Namespace(key='http', value='http://localhost:3128'),
        argparse.Namespace(key='https', value='http://localhost:1080')
    ]
    mock_args.cert = '/path/client.cert'
    mock_args.cert_key = '/path/client.key'
    mock_args.verify = 'false'

    # when
    result = make_send_kwargs_mergeable_

# Generated at 2022-06-13 21:31:53.944167
# Unit test for function max_headers
def test_max_headers():
    import pytest

    with pytest.raises(Exception):
        with max_headers(limit=1):
            http.client.HTTPConnection("www.httpbin.org")



# Generated at 2022-06-13 21:31:58.746914
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data=False,
        form=False,
        json=True,
        files=False,
    )

    headers = make_default_headers(args)
    assert headers['Accept'] == JSON_ACCEPT


# Generated at 2022-06-13 21:32:05.982556
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.cli.parser import get_parser
    parser = get_parser()
    args = parser.parse_args(['--verify=no','--cert-key','b','--cert','a','--proxy','a:1','--proxy','b:2'])
    make_send_kwargs_mergeable_from_env(args)


# Generated at 2022-06-13 21:32:18.992819
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args_dict = {'args.data': [{'is_admin': True}],
                 'args.form': False, 'args.headers': {'Content-Type': 'application/json'},
                 'args.json': False, 'args.method': 'POST', 'args.offline': False,
                 'args.url': 'http://localhost:5000/sign_up_admin',
                 'headers': {'Content-Type': 'application/json'},
                 'kwargs': {'method': 'post', 'url': 'http://localhost:5000/sign_up_admin',
                            'headers': {'Content-Type': 'application/json'},
                            'data': b'{"is_admin": true}', 'auth': None, 'params': []}
                 }

# Generated at 2022-06-13 21:32:23.870526
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.follow = False
    args.timeout = None
    args.session = None
    args.output_file = None
    args.debug = False
    args.auth = None
    kwargs = make_send_kwargs(args)
    assert({'timeout': None,
            'allow_redirects': False} == kwargs)

# Generated at 2022-06-13 21:32:38.294885
# Unit test for function collect_messages
def test_collect_messages():
    import argparse
    import httpie.cli as cli
    import httpie.input
    import httpie.output
    import httpie.config
    import httpie.plugins
    args = cli.parser.parse_args(["--json"])
    input_options = httpie.input.Options()
    output_options = httpie.output.Options()
    auth_options = httpie.cli.AuthCredentials()
    config = httpie.config.Config(CLIConfig=vars(args),
                                  env=os.environ,
                                  config_dir=None)

# Generated at 2022-06-13 21:32:41.937180
# Unit test for function max_headers
def test_max_headers():
    http.client._MAXHEADERS = float('Inf')
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == float('Inf')

# Generated at 2022-06-13 21:33:16.260613
# Unit test for function max_headers
def test_max_headers():
    try:
        with max_headers(20):
            sys.stderr.write('\n## http.client._MAXHEADERS = %s\n' %
                             str(http.client._MAXHEADERS))
    finally:
        sys.stderr.write('## http.client._MAXHEADERS = %s\n' %
                         str(http.client._MAXHEADERS))
        sys.stderr.flush()


# Generated at 2022-06-13 21:33:23.780464
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class Arguments:
        def __init__(self):
            self.url = "www.example.com"
            self.method = "GET"
            self.headers = {"header1": "test1", "header2": "test2"}
            self.json = False
            self.form = False
            self.data = False
            self.files = False
            self.multipart = False
            self.offline = False
            self.chunked = False
            self.path_as_is = False
            self.multipart_data = False
            self.boundary = False
            self.compress = False

    args = Arguments()

    request_body_read_callback = lambda chunk: chunk

# Generated at 2022-06-13 21:33:36.123208
# Unit test for function collect_messages

# Generated at 2022-06-13 21:33:39.959743
# Unit test for function max_headers
def test_max_headers():
    http.client._MAXHEADERS = float('Inf')
    with max_headers(100):
        assert http.client._MAXHEADERS == 100
    assert http.client._MAXHEADERS == float('Inf')

# Generated at 2022-06-13 21:33:41.705726
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    print(make_request_kwargs(argparse.Namespace))



# Generated at 2022-06-13 21:33:55.780819
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.headers = {}
    args.data = {}
    assert make_default_headers(args)['User-Agent'] == DEFAULT_UA
    args.headers = {'User-Agent': 'Safari'}
    assert make_default_headers(args)['User-Agent'] == 'Safari'
    args.headers = {'Accept': 'text/html'}
    args.data = {'data': 'data'}
    assert make_default_headers(args)['User-Agent'] == DEFAULT_UA
    assert make_default_headers(args)['Accept'] == 'text/html'
    assert make_default_headers(args)['Content-Type'] == 'application/json'
    args.headers = {'Content-Type': 'application/json'}
    assert make

# Generated at 2022-06-13 21:33:56.447323
# Unit test for function collect_messages
def test_collect_messages():
    pass

# Generated at 2022-06-13 21:33:59.089708
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    default_headers_dict = make_default_headers(args)
    default_headers_dict['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:34:03.428788
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args=argparse.Namespace()
    args.headers={}
    args.timeout = 45

    for k,v in make_send_kwargs(args).items():
        print(f"{k}:{v}")
    print("======================")

    for k,v in make_send_kwargs_mergeable_from_env(args).items():
        print(f"{k}:{v}")


# Generated at 2022-06-13 21:34:15.555109
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    assert isinstance(headers, RequestHeadersDict)
    assert headers['User-Agent'] == DEFAULT_UA

    args.json = True
    args.data = [1, 2, 3]
    args.headers = RequestHeadersDict()
    headers = make_default_headers(args)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

    args.json = False
    args.data = None
    headers = make_default_headers(args)
    assert headers['Content-Type'] is None

    args.form = True
    args.files = [123, 456, 789]
    headers = make_default_headers(args)

# Generated at 2022-06-13 21:35:21.408871
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        auth=None,
        auth_plugin=None,
        chunked=None,
        verify='yes',
        cert=None,
        cert_key=None,
        data=None,
        download=None,
        files={},
        form=False,
        headers={'host': 'host'},
        json=False,
        method='GET',
        offline=False,
        params={},
        output_file=None,
        path_as_is=None,
        proxy=[],
        session=None,
        session_read_only=None,
        stream=None,
        url='http://www.baidu.com',
        auth_plugin=None,
    )
    base_headers = RequestHeadersDict({})
    result = make_request_kw

# Generated at 2022-06-13 21:35:29.303113
# Unit test for function max_headers
def test_max_headers():
    # test case 1
    # error
    source = "GET / HTTP/1.0\r\n" \
             "X-Foo-Header: 123456789a\r\n" \
             "X-Bar-Header: 123456789a\r\n" \
             "X-Bar-Header: 123456789a\r\n" \
             "X-Bar-Header: 123456789a\r\n" \
             "X-Bar-Header: 123456789a\r\n" \
             "X-Bar-Header: 123456789a\r\n" \
             "X-Echo-Header: 789\r\n" \
             "Host: localhost\r\n" \
             "\r\n"

# Generated at 2022-06-13 21:35:34.706755
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files={}
    )
    default_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    verify_headers = make_default_headers(args)
    assert verify_headers == default_headers


# Generated at 2022-06-13 21:35:36.827901
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    return


# Generated at 2022-06-13 21:35:39.869263
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(data=None, form=False, json=False, timeout=False)
    headers = make_default_headers(args)
    assert headers == {"User-Agent": "HTTPie/0.9.9"}



# Generated at 2022-06-13 21:35:51.237912
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.cli.args import parse_args
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.sunos import SunOSProxyFixPlugin
    
    args = parse_args(args=[
        '--proxy', 'type://user:pass@server:port',
        '--proxy', 'type2://user2:pass2@server2:port2',
        '--verify', 'no',
        '--cert', 'cert',
        '--cert-key', 'cert-key',
        'GET', 'http://dummy',
    ])
    args.auth_plugin = HTTPBasicAuth(username='user', password='pass')
    args.plugins = [
        HTTPBasicAuth,
        SunOSProxyFixPlugin,
    ]
    args.method = 'GET'

    assert make_send_kwargs

# Generated at 2022-06-13 21:35:58.270609
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()

    test_args = []
    # test make_default_headers with form data
    args.form = True
    args.files = None
    test_args.append(args)

    # test make_default_headers with json data
    args.json = True
    test_args.append(args)

    # test make_default_headers with json data
    args.json = None
    args.data = dict()
    test_args.append(args)

    # test make_default_headers with empty data
    args.data = None
    test_args.append(args)

    # test make_default_headers with files
    args.files = []
    test_args.append(args)

    # test make_default_headers with args.form = None
    args.form = None
   

# Generated at 2022-06-13 21:36:01.037756
# Unit test for function max_headers
def test_max_headers():
    import http

    with max_headers(2):
        assert http.client._MAXHEADERS == 2
        # test _MAXHEADERS reset to original value
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:36:12.017281
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.cert = "mycert"
    args.cert_key = "mykey"
    args.proxy = [argparse.Namespace(key='a', value='1'), argparse.Namespace(key='b', value='2')]
    args.verify = 'no'
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {'a':'1', 'b':'2'}
    assert kwargs['verify'] == False
    assert kwargs['cert'] == ('mycert', 'mykey')

# Generated at 2022-06-13 21:36:15.337679
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    test_args = argparse.Namespace()
    test_args.proxy = []
    test_args.verify = 'yes'
    test_args.cert = None
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    assert expected == make_send_kwargs_mergeable_from_env(test_args)

# Generated at 2022-06-13 21:38:18.139097
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        method="POST",
        headers=[],
        url="http://localhost",
        data=[],
        auth=None,
        params=[],
        json=None,
        files=[],
        form=None,
        verify=None,
        cert=None,
        cert_key=None,
        timeout=None,
        proxy=[],
        allow_redirects=False,
        max_redirects=30,
        max_headers=None,
        chunked=False,
        compression=None,
        compress=True,
        path_as_is=False,
        follow=False,
        all=False,
        offline=False
    )
    kwargs = make_request_kwargs(args)
    print(kwargs)

# Generated at 2022-06-13 21:38:22.646313
# Unit test for function max_headers
def test_max_headers():
    http = importlib.import_module("http")
    orig = http.client._MAXHEADERS
    with max_headers(None):
        assert http.client._MAXHEADERS == float('Inf')
    assert http.client._MAXHEADERS == orig
    with max_headers(2):
        assert http.client._MAXHEADERS == 2
    assert http.client._MAXHEADERS == orig

# Generated at 2022-06-13 21:38:31.630675
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.data = None
    args.form = False
    args.json = True

    assert make_default_headers(args) == {'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json', 'User-Agent': 'HTTPie/0.9.9'}

if __name__ == '__main__':
    args = argparse.Namespace()
    args.data = None
    args.form = True
    args.json = False

    test_make_default_headers()

# Generated at 2022-06-13 21:38:44.165626
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2022-06-13 21:38:54.159402
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = namedtuple('args', ['cert', 'cert_key', 'proxy', 'verify'])
    args.cert = 'key.pem'
    args.cert_key = 'cert.key'
    args.proxy = namedtuple('proxy', ['key', 'value'])
    args.proxy.key = 'http'
    args.proxy.value = 'http://127.0.0.1:63509'
    args.verify = 'yes'
    output = make_send_kwargs_mergeable_from_env(args)
    assert output == {'proxies': {'http': 'http://127.0.0.1:63509'},
                      'stream': True, 'verify': True,
                      'cert': ('key.pem', 'cert.key')}

# Generated at 2022-06-13 21:38:55.974675
# Unit test for function make_default_headers
def test_make_default_headers():
    assert make_default_headers({}) == {
        'User-Agent': DEFAULT_UA
    }

# Generated at 2022-06-13 21:39:05.720690
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    url = 'http://127.0.0.1:8222/post'
    data = {'sn': 123456, 'key1': 'value1', 'key2': 'value2'}
    request_kwargs = make_request_kwargs(args=args)
    assert (request_kwargs['kwargs']['method'] == 'post')
    assert(request_kwargs['kwargs']['data'] == data)
    assert(request_kwargs['kwargs']['url'] == url)
    assert(headers['Content-Type'] == 'application/json')

# Generated at 2022-06-13 21:39:08.743267
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(data = {'s': 2, 'a': 3}, form = False, json = False, files = False)
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({'User-Agent': DEFAULT_UA, 'Accept': JSON_ACCEPT, 'Content-Type': JSON_CONTENT_TYPE})

# Generated at 2022-06-13 21:39:13.183448
# Unit test for function max_headers
def test_max_headers():
    import http.client
    assert max_headers(10).__enter__() == None
    assert http.client._MAXHEADERS == 10
    assert max_headers(None).__enter__() == None
    assert http.client._MAXHEADERS == float('Inf')

# Generated at 2022-06-13 21:39:20.816686
# Unit test for function max_headers
def test_max_headers():
    class MockRequest:
        pass
    class MockConnection:
        class MockMessage:
            def __init__(self):
                self._headers = []
        def __init__(self):
            self.msg = self.MockMessage()
    class MockResponse:
        def __init__(self):
            self._original_response = MockConnection()
    class MockSession:
        def __init__(self, limit: int):
            self.limit = limit
        def merge_environment_settings(self, url, **kwargs):
            return kwargs
        def send(self, request, **kwargs):
            response = MockResponse()
            with max_headers(self.limit):
                MockRequest().add_header('foo', 'bar ' * (self.limit + 1))