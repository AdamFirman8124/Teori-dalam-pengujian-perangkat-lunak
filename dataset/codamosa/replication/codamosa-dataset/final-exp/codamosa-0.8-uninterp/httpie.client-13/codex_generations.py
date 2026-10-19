

# Generated at 2022-06-13 21:30:27.216226
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    import argparse
    args = argparse.Namespace()
    args.timeout = 'wow'
    args.allow_redirects = False
    out = make_send_kwargs(args)
    assert out == {'timeout': 'wow', 'allow_redirects': False}


# Generated at 2022-06-13 21:30:31.043901
# Unit test for function collect_messages
def test_collect_messages():
    args = parse_args(['get','http://httpbin.org','--no-ssl','--no-auth','--no-verify','--no-proxies'])
    def f(request,response):
        pass
    list(collect_messages(args,Path('D:\httpie-config-test'),f))

# Generated at 2022-06-13 21:30:37.067768
# Unit test for function max_headers
def test_max_headers():
    import os
    assert os.environ.get('HTTPIE_MAX_HEADERS') is None
    with max_headers(limit=123):
        assert os.environ['HTTPIE_MAX_HEADERS'] == '123'
    assert os.environ.get('HTTPIE_MAX_HEADERS') is None

test_max_headers()

# Generated at 2022-06-13 21:30:43.094152
# Unit test for function make_default_headers
def test_make_default_headers():
    import argparse
    args = argparse.Namespace(files=[],
                              json=False,
                              form=False,
                              compress=0,
                              data=None,
                              headers=[],
                              headers_only=False)
    default_headers = make_default_headers(args)
    assert default_headers=={'User-Agent': 'HTTPie/0.9.9'}

# Generated at 2022-06-13 21:30:47.416672
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=60, allow_redirects=False, verify='yes')
    r = make_send_kwargs(args)
    assert r['timeout'] == 60
    assert r['allow_redirects'] == False
    assert r['verify'] == 'yes'


# Generated at 2022-06-13 21:30:54.677582
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = 0
    args.form = 0
    headers = make_default_headers(args)
    assert headers['User-Agent'] == 'HTTPie/1.0.3'
    assert headers['Accept'] == 'application/json, */*;q=0.5'
    assert not headers['Content-Type']

# Generated at 2022-06-13 21:31:03.707376
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args=argparse.Namespace()
    args.timeout=None
    args.allow_redirects=False
    result=make_send_kwargs(args)
    assert result['timeout']==args.timeout
    assert result['allow_redirects']==args.allow_redirects
    args.timeout=1
    args.allow_redirects=True
    result = make_send_kwargs(args)
    assert result['timeout'] == args.timeout
    assert result['allow_redirects'] == args.allow_redirects


# Generated at 2022-06-13 21:31:18.595900
# Unit test for function collect_messages
def test_collect_messages():
    config_dir = Path()
    class Dummy_args:
        def __init__(self):
            self.url = 'http://localhost:80'
            self.method = 'POST'
            self.headers = {'Host': 'localhost', 'Content-Type': 'application/json'}
            self.json = True
            self.data = {'username': 'admin', 'password': 'admin'}
            self.auth = None
            self.auth_plugin = None
            self.stream = True
            self.verify = True
            self.max_headers = 16384
            self.debug = False
            self.offline = False
            self.follow = False
            self.max_redirects = 30
            self.timeout = 30
            self.num_iter = 0
            self.iter_mode = False
            self

# Generated at 2022-06-13 21:31:30.293899
# Unit test for function make_default_headers
def test_make_default_headers():
    import argparse
    args = argparse.Namespace()
    args.json = False
    args.form = True
    args.data = True
    args.files = True
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA
    assert default_headers['Content-Type'] == FORM_CONTENT_TYPE

    args.json = True
    args.form = False
    args.data = {}
    args.files = []
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA
    assert default_headers['Accept'] == JSON_ACCEPT
    assert default_headers['Content-Type'] == JSON_CONTENT_TYPE

# Generated at 2022-06-13 21:31:45.092703
# Unit test for function collect_messages

# Generated at 2022-06-13 21:32:11.990476
# Unit test for function collect_messages
def test_collect_messages():
    CONFIG_DIR = Path("/home/chau/.config/httpie")
    ARGS = argparse.Namespace()
    ARGS.auth = None
    ARGS.auth_plugin = None
    ARGS.boundary = None
    ARGS.body_on_error = False
    ARGS.chunked = False
    ARGS.color = 'auto'
    ARGS.compress = 0
    ARGS.debug = False
    ARGS.download = False
    ARGS.download_resume = False
    ARGS.download_status = None
    ARGS.download_unix_timestamps = False
    ARGS.download_wait = 1
    ARGS.follow = False
    ARGS.follow_redirects = None
    ARGS.form = False
    ARGS.headers = RequestHeadersDict

# Generated at 2022-06-13 21:32:24.132019
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store', default=True,
                        const=True, nargs='?')
    parser.add_argument('--cert', action='store', default=None)
    parser.add_argument('--cert-key', action='store', default=None)
    parser.add_argument('--proxy', action='append', default={},
                        dest='proxy', default={}, type=lambda p:
                        ProxyArg(p), metavar="SCHEME://USER:PASSWORD@HOST:PORT")
    args = parser.parse_args()

    args.verify = "True"
    args.cert = None
    args.cert_key = None
    args.proxy = None


# Generated at 2022-06-13 21:32:38.368184
# Unit test for function max_headers

# Generated at 2022-06-13 21:32:48.323927
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    #Test for method POST
    args = argparse.Namespace(method='POST',url='http://httpbin.org/post',headers={'content-type':'application/json','Host':'httpbin.org','Accept':'application/json','User-Agent':'HTTPie/1.0.3'},auth_plugin='',auth=[],data='{"hello": "world"}',json=False,form=False,files=[],params=[],compress=False,compress_level=6,chunked=False,max_redirects=None,max_headers=1000,max_body=10475274)
    kwargs = make_request_kwargs(args)
    request = requests.Request(**kwargs)
    response = requests.Session().send(request)
    assert response.status_code == 200

    #Test for method

# Generated at 2022-06-13 21:32:58.709577
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = {'allow_redirects': False, 'timeout': None, 'stream': True, 'cert': None, 'verify': None, 'proxies': None}
    assert make_send_kwargs({}) == args, 'send kwargs incorrect'
    args = {'allow_redirects': False, 'timeout': None, 'stream': True, 'cert': None, 'verify': None, 'proxies': '192.168.0.1:8080'}
    assert make_send_kwargs({'proxy': ['192.168.0.1:8080']}) == args, 'send kwargs incorrect'


# Generated at 2022-06-13 21:33:02.607975
# Unit test for function max_headers
def test_max_headers():
    limit = 10
    assert http.client._MAXHEADERS == limit
    http.client._MAXHEADERS = limit + 1
    assert http.client._MAXHEADERS == limit + 1

    with max_headers(limit):
        assert http.client._MAXHEADERS == limit

    assert http.client._MAXHEADERS == limit + 1

# Generated at 2022-06-13 21:33:03.980393
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    make_send_kwargs(args)

# Generated at 2022-06-13 21:33:08.692015
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    assert make_send_kwargs({
        'timeout': 5,
        'allow_redirects': False,
    }) == {
        'timeout': 5,
        'allow_redirects': False,
    }

# Generated at 2022-06-13 21:33:19.105272
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class fake_args:
        def __init__(self):
            self.method = 'GET'
            self.url = 'http://www.google.com'
            self.headers = {
                'User-Agent': 'test_python',
                'Accept': '*/*'
            }
            self.data = {'foo': 'bar'}
            self.json = True
            self.auth = ('test_username', 'test_password')
            self.params = {'baz': 'qux'}
            self.files = ()
            self.form = False
            self.multipart = False
            self.multipart_data = None
            self.boundary = 'ABCDEF'
            self.verify = True
            self.timeout = None
            self.chunked = False
            self.debug = False

# Generated at 2022-06-13 21:33:33.207122
# Unit test for function make_default_headers
def test_make_default_headers():
    from httpie.cli.parser import parse_args
    args = parse_args(['--form', '--json', '--data={"key":"value"}', 'http://example.com'])
    h = make_default_headers(args)
    assert('User-Agent' in h)
    assert('Accept' in h)
    assert('Content-Type' in h)
    assert(h.get('User-Agent') == DEFAULT_UA)
    assert(h.get('Accept') == JSON_ACCEPT)
    assert(h.get('Content-Type') == JSON_CONTENT_TYPE)

    args = parse_args(['--form', 'http://example.com'])
    h = make_default_headers(args)
    assert('User-Agent' in h)
    assert('Accept' in h)

# Generated at 2022-06-13 21:33:53.837707
# Unit test for function build_requests_session
def test_build_requests_session():
    assert build_requests_session(verify=True, ssl_version="secure", ciphers=None) != None

# Generated at 2022-06-13 21:34:02.847233
# Unit test for function collect_messages
def test_collect_messages():
    class Args:
        def __init__(self):
            self.method="GET"
            self.url="https://baidu.com"
            self.headers={}
            self.data=""
            self.files=""
            self.auth=""
            self.auth_type=""
            self.auth_plugin=""
            self.compress=0
            self.compress_level=0
            self.json=False
            self.form=False
            self.verbose=False
            self.all=False
            self.download=False
            self.output_file=""
            self.output_dir=""
            self.output_options=""
            self.session=""
            self.session_read_only=""
            self.max_redirects=0
            self.max_headers=0
            self.offline=False

# Generated at 2022-06-13 21:34:07.499088
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    #Initializing argument
    args = argparse.Namespace(stream=True)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': None, 'allow_redirects': False}
    assert kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:34:10.072753
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    if headers['User-Agent'] != DEFAULT_UA:
        print('Error: User-Agent header value is not correct')


# Generated at 2022-06-13 21:34:17.201496
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(
        proxy=[],
        verify=True,
        cert=None,
        cert_key=None
    )
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs.get('proxies', {}) == {}
    assert kwargs.get('verify', True) == True
    assert kwargs.get('cert', None) == None

# Generated at 2022-06-13 21:34:21.041814
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser()
    args, unknown = parser.parse_known_args()
    make_default_headers(args)
    args.json = True
    make_default_headers(args)
    args.json = False
    args.form = True
    args.data = True
    make_default_headers(args)



# Generated at 2022-06-13 21:34:31.479557
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(key="1", value="2")]
    args.verify = "true"
    args.cert = "3"
    args.cert_key = "4"
    assert make_send_kwargs_mergeable_from_env(args) == {
        "proxies": {
            "1": "2",
        },
        "stream": True,
        "verify": True,
        "cert": "3",
        "cert": "4",
    }


# Generated at 2022-06-13 21:34:44.387083
# Unit test for function collect_messages
def test_collect_messages():
    # Set up a Namespace class
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # Set up the fake arguments

# Generated at 2022-06-13 21:34:49.836785
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    assert make_send_kwargs(args) == {'timeout': 10, 'allow_redirects': False}


# Generated at 2022-06-13 21:34:54.856230
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout=None,
        allow_redirects=False,
    )
    kwargs = make_send_kwargs(args)
    assert kwargs
    assert kwargs['timeout'] == None
    assert not kwargs['allow_redirects']


# Generated at 2022-06-13 21:35:30.608195
# Unit test for function max_headers
def test_max_headers():
    with max_headers(1):
        pass

# Generated at 2022-06-13 21:35:31.781280
# Unit test for function max_headers
def test_max_headers():
    max_headers(10)

# Generated at 2022-06-13 21:35:36.849946
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        json=False,
        data=None,
        form=False,
        files=False,
        verify='yes',
        cert=None,
        cert_key=None,
        timeout=None,
    )
    default_headers = make_default_headers(args)
    assert len(default_headers) == 1 and default_headers['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:35:44.509583
# Unit test for function make_request_kwargs
def test_make_request_kwargs():

    args = argparse.Namespace(
        auth=None,
        auth_plugin=None,
        cert=None,
        cert_key=None,
        chunked=False,
        form=False,
        headers={},
        json={},
        max_headers=None,
        method='POST',
        offline=False,
        params={},
        path_as_is=False,
        proxy=[],
        timeout=None,
        url='http://localhost:8080/write',
        verify='yes',
        json=True,
        timeout=60,
        data={"CPU": "0.703", "GPU": "0.554"},
        user_agent=None
    )

# Generated at 2022-06-13 21:35:48.751424
# Unit test for function build_requests_session
def test_build_requests_session():
    verify = False
    ssl_version = 'TLS1.2'
    ciphers = None
    requests_session = build_requests_session(verify, ssl_version, ciphers)
    assert requests_session is not None

# Generated at 2022-06-13 21:35:58.463259
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    hub_url = 'http://www.hub.com'
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'true'
    args.cert = None
    args.cert_key = None

    # Execute the function
    kwargs = make_send_kwargs_mergeable_from_env(args)

    # Verify the result
    assert kwargs['proxies'] == {}
    assert kwargs['verify'] == True
    assert kwargs['cert'] == None



# Generated at 2022-06-13 21:36:02.084616
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    sys.argv = "http --form POST http://httpbin.org/post name=John".split()
    from httpie.cli import parser
    args = parser.parse_args()
    res = make_request_kwargs(args)
    print(res['data'])

# Generated at 2022-06-13 21:36:08.148391
# Unit test for function max_headers
def test_max_headers():
    import http.client
    orig = http.client._MAXHEADERS
    try:
        with max_headers(10):
            assert http.client._MAXHEADERS == 10
        assert http.client._MAXHEADERS == orig
    except:
        http.client._MAXHEADERS = orig
        raise

# Generated at 2022-06-13 21:36:18.035572
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.data = {"key": "value"}
    args.url = "http://https"
    args.method = "GET"
    args.params = []
    args.json = True
    args.auth = None
    args.headers = []
    args.form = False
    args.files = []
    args.max_headers = None
    args.max_redirects = None
    args.timeout = None
    args.verify = True
    args.auth_plugin = None
    args.session = None
    args.session_read_only = None
    args.compress = 0
    args.chunked = None
    args.offline = False
    args.debug = False
    args.stream = False
    args.follow = False
    args.all = False


# Generated at 2022-06-13 21:36:18.556649
# Unit test for function max_headers
def test_max_headers():
    pass

# Generated at 2022-06-13 21:37:28.879159
# Unit test for function build_requests_session
def test_build_requests_session():
    req = requests.Session()
    assert isinstance(req, requests.Session)

# Generated at 2022-06-13 21:37:37.223053
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    args.data = {}
    headers = make_default_headers(args)
    assert isinstance(headers, RequestHeadersDict)
    assert len(headers) == 2
    args.json = False
    headers = make_default_headers(args)
    assert len(headers) == 1
    args.headers = {'Accept': 'application/json'}
    args.files = True
    args.form = True
    headers = make_default_headers(args)
    assert len(headers) == 1

# Generated at 2022-06-13 21:37:39.330757
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    assert make_send_kwargs_mergeable_from_env([]) == {}

# Generated at 2022-06-13 21:37:49.612982
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verify', default=False, type=bool, help='Only https protocol is allowed')
    parser.add_argument('--cert', default=None, type=str, help='Path to the client certificate, (a single file containing the private key and the certificate in PEM format)')
    parser.add_argument('--cert-key', default=None, type=str, help='Path to the client certificate key')
    parser.add_argument('--proxy', default=[], type=str, action='append', help='Proxy URL for requests (default: None)')

    args = parser.parse_args(['--verify', '--proxy', 'localhost:8080', '--cert', './cert.pem', '--cert-key', './key.pem'])
    print

# Generated at 2022-06-13 21:37:52.245683
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=12, allow_redirects=False)
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs['timeout'] == 12
    assert send_kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:37:54.099633
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    assert make_send_kwargs(argparse.Namespace(
        timeout=5,
        allow_redirects=False,
    )) == {'timeout': 5, 'allow_redirects': False}


# Generated at 2022-06-13 21:37:55.270050
# Unit test for function collect_messages
def test_collect_messages():
    pass

# Generated at 2022-06-13 21:37:59.460176
# Unit test for function max_headers
def test_max_headers():
    import http
    # noinspection PyProtectedMember
    orig = http.client._MAXHEADERS

    with max_headers(limit=2):
        # noinspection PyProtectedMember
        assert http.client._MAXHEADERS == 2

    assert orig == http.client._MAXHEADERS

# Generated at 2022-06-13 21:38:11.861980
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Arrange
    args = argparse.Namespace()
    args.data = ""
    args.files = None
    args.querystring = []
    args.headers = []
    args.method = ""
    args.url = ""
    args.auth = None
    args.verify = None
    args.json = False
    args.form = False
    args.multipart = False
    args.multipart_data = ""
    args.boundary = ""

    # Act
    kwargs = make_request_kwargs(args)

    # Assert
    assert kwargs['method'] == ""
    assert kwargs['url'] == ""
    assert kwargs['auth'] == None
    assert kwargs['data'] == ""
    assert kwargs['params'] == []
    assert kwargs

# Generated at 2022-06-13 21:38:20.988993
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'post'
    args.url = 'http://localhost:8080'
    args.headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    args.data = '{"a": 1, "b": 2}'
    args.json = True
    args.form = None
    args.files = []
    args.multipart_data = None
    args.multipart = None
    args.follow = False
    args.timeout = 30
    args.max_redirects = None
    args.save_stream = False
    args.auth = None
    args.params = {}
    args.compress = None
    args.output_file = None
    args.session = None