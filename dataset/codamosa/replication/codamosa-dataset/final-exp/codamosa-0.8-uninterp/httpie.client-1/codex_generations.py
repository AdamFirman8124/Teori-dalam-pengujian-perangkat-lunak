

# Generated at 2022-06-13 21:30:20.494419
# Unit test for function make_default_headers
def test_make_default_headers():
    class Args:
        json = True
        data = '{"test": "data"}'
        form = False
    args = Args()
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA
    assert default_headers['Accept'] == JSON_ACCEPT
    assert default_headers['Content-Type'] == JSON_CONTENT_TYPE

# Generated at 2022-06-13 21:30:31.044066
# Unit test for function collect_messages
def test_collect_messages():
    headers = {'aaa': 'bbb', 'aaa': 'bbb'}

# Generated at 2022-06-13 21:30:43.332683
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.auth = ""
    args.auth_type = ""
    args.auth_plugin = ""
    args.auth_endpoint = ""
    args.auth_send_missing_credentials_in_body = ""
    args.all = ""
    args.body = ""
    args.body_style = ""
    args.chunked = ""
    args.compress = ""
    args.config_dir = ""
    args.data = ""
    args.debug = ""
    args.download_rate = ""
    args.download = ""
    args.follow = ""
    args.form = ""
    args.headers = ""
    args.http2_priority = ""
    args.http2_stream_deps = ""
    args.http2 = ""
    args.ignore

# Generated at 2022-06-13 21:30:52.085274
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    test_args = argparse.Namespace(
        json=False,
        form=False,
        verify='yes',
        cert='cert.pem',
        cert_key='cert_key.pem',
        proxy=[argparse.Namespace(key='proxy.com', value='http')]
    )
    kwargs_verify = {
        'proxies': {'proxy.com': 'http'},
        'stream': True,
        'verify': True,
        'cert': 'cert.pem',
        'cert_key': 'cert_key.pem'
    }

# Generated at 2022-06-13 21:31:03.746774
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.url = "https://www.google.com"
    args.method = 'get'
    args.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    args.auth = None
    args.params = {'q': 'cute+kitten', 'page': 3}
    args.timeout = 10
    args.auth_plugin = None
    args.verify = True
    
    # testing without base_headers
    kwargs = make_request_kwargs(args)
    assert kwargs['url'] == 'https://www.google.com'
    assert kwargs['method'] == 'get'
    assert kwargs['headers']['Content-Type'] == 'application/json'

# Generated at 2022-06-13 21:31:11.334807
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.headers = {'Accept-Language': 'en-US'}
    args.method = 'GET'
    args.url = 'https://www.google.com/'
    args.verify = 'yes'
    args.follow = True
    args.all = False
    args.max_redirects = 5
    args.auth = 'google'
    args.cert = '1234'
    args.cert_key = '123456'
    args.json = False
    args.data = {'test': True}
    args.chunked = True
    args.form = False
    args.files = False
    args.compress = True
    args.compress_level = True
    args.max_headers = 20
    args.output

# Generated at 2022-06-13 21:31:21.352223
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    parser = argparse.ArgumentParser()

    parser.add_argument("--method", default='GET')
    parser.add_argument("--url", default='http://www.google.com')
    parser.add_argument("--auth", default=None)
    parser.add_argument("--headers", type=dict, default={})
    parser.add_argument("--data", default=None)
    parser.add_argument("--json", default=None)
    parser.add_argument("--params", default=None)
    parser.add_argument("--form", default=False)

    args = parser.parse_args([])
    kwargs = make_request_kwargs(args)

    assert kwargs['method'].lower() == 'get'

# Generated at 2022-06-13 21:31:33.277780
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.url = "http://www.facebook.com"
    args.method = 'GET'
    args.headers = {'Content-Type': 'application/json'}
    args.auth = {}
    args.params = {}
    args.data = {}
    args.json = True
    args.form = False
    args.multipart = False
    args.files = False
    args.multipart_data = {}
    args.boundary = None
    args.chunked = False
    args.offline = False

    https_adapter = HTTPieHTTPSAdapter(
        ciphers='HIGH',
        verify='true',
        ssl_version='TLS',
    )
    requests_session = requests.Session()

# Generated at 2022-06-13 21:31:46.050915
# Unit test for function make_default_headers
def test_make_default_headers():
    args = {
        'json': False,
        'form': False,
        'data': None,
        'headers': {}
    }
    head = make_default_headers(**args)
    assert head == {
        'User-Agent': DEFAULT_UA
    }, 'Failed to create default headers'
    args = {
        'json': False,
        'form': True,
        'data': None,
        'headers': {}
    }
    head = make_default_headers(**args)
    assert head == {
        'Content-Type': FORM_CONTENT_TYPE,
        'User-Agent': DEFAULT_UA
    }, 'Failed to create default headers'

# Generated at 2022-06-13 21:31:46.735196
# Unit test for function collect_messages
def test_collect_messages():
    pass

# Generated at 2022-06-13 21:32:05.572881
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 100
    with max_headers(50):
        assert http.client._MAXHEADERS == 50
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:32:08.893990
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=3)
    assert make_send_kwargs(args) == {
        'timeout': args.timeout or None,
        'allow_redirects': False
    }

# Generated at 2022-06-13 21:32:17.008620
# Unit test for function make_default_headers
def test_make_default_headers():
    argparse.Namespace.json = 'json'
    argparse.Namespace.data = 'data'
    argparse.Namespace.form = 'form'
    default_headers = make_default_headers('args')
    assert default_headers['Content-Type'] == 'application/json'

    argparse.Namespace.json = None
    argparse.Namespace.data = 'data'
    argparse.Namespace.form = 'form'
    default_headers = make_default_headers('args')
    assert default_headers['Content-Type'] == 'application/x-www-form-urlencoded; charset=utf-8'

    argparse.Namespace.json = None
    argparse.Namespace.data = None
    argparse.Namespace.form = None
    default_headers = make_default_headers('args')

# Generated at 2022-06-13 21:32:22.783221
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    assert make_send_kwargs_mergeable_from_env(argparse.Namespace()) == {'cert': None, 'proxies': {}, 'verify': True}
    assert make_send_kwargs_mergeable_from_env(argparse.Namespace(verify='no')) == {'cert': None, 'proxies': {}, 'verify': False}

# Generated at 2022-06-13 21:32:37.941542
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        files='',
        data='',
        form=False,
        auto_json='',
        data_as_json=False,
        json=False,
        method='',
        url='',
        headers='',
        offline=False,
        chunked=False,
        request_body_read_callback='',
        auth='',
        params='',
        verify='',
        cert='',
        cert_key='',
        max_headers='',
        session='',
        session_read_only='',
        timeout='',
        auth_plugin='',
        debug=False,
        follow=False,
        max_redirects=False,
        all=False,
        multipart='',
        multipart_data='',
        boundary=''
    )
   

# Generated at 2022-06-13 21:32:43.560145
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout=None, allow_redirects=False,
    )
    kwargs = make_send_kwargs(args)
    assert (kwargs == {'timeout': None, 'allow_redirects': False})



# Generated at 2022-06-13 21:32:56.622557
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
    )
    default_headers = make_default_headers(args)
    print(default_headers)

    args = argparse.Namespace(
        data=None,
        form=True,
        json=False,
    )
    default_headers = make_default_headers(args)
    print(default_headers)

    args = argparse.Namespace(
        data=None,
        form=False,
        json=True,
    )
    default_headers = make_default_headers(args)
    print(default_headers)

    args = argparse.Namespace(
        data=[1,2,3],
        form=False,
        json=False,
    )

# Generated at 2022-06-13 21:33:05.592186
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    data = json.dumps({"test":"test"})
    if data:
        print(data)
    else:
        # We need to set data to an empty string to prevent requests
        # from assigning an empty list to `response.request.data`.
        data = ''
    print(data)
    args = argparse.Namespace()
    print(args.data)
    print(args.form)
    print(args.json)
    print(args.json or args.data)
    args.json = True
    print(args.json or args.data)
    args.json = False
    print(args.json or args.data)
    args.data = True
    print(args.json or args.data)
    args.data = False
    print(args.json or args.data)

# Generated at 2022-06-13 21:33:17.210700
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    from argparse import Namespace
    files = []
    data = {'test_1': '1', 'test_2': '2'}
    base_headers = {'test_3': '3', 'test_4': '4'}
    args_dict = {
        'method': 'get',
        'url': 'www.google.com',
        'headers': {'test_5': '5', 'test_6': '6', 'Content-Type': 'application/json'},
        'data': data,
        'auth': ('user', 'password1'),
        'params': {'test_7': '7', 'test_8': '8'},
        'files': files,
        'json': True,
        'form': True,
    }
    args = Namespace(**args_dict)

    k

# Generated at 2022-06-13 21:33:31.177875
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    d = get_test_args()
    d.proxy = [ProxyArg(key='https', value='https://192.168.2.2:8080')]
    d.verify = 'true'
    d.cert = '/path/to/local/cert'
    d.cert_key = '/path/to/local/cert_key'
    assert d.proxy == [ProxyArg(key='https', value='https://192.168.2.2:8080')]
    assert d.verify == 'true'
    assert d.cert == '/path/to/local/cert'
    assert d.cert_key == '/path/to/local/cert_key'

    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(d)
    assert send_kw

# Generated at 2022-06-13 21:34:47.791853
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    headers = make_default_headers(args)
    assert ('Accept', 'application/json, */*;q=0.5') in headers.items()
    assert ('Content-Type', 'application/json') in headers.items()
    args = argparse.Namespace()
    args.data = {}
    args.form = True
    headers = make_default_headers(args)
    assert ('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8') in headers.items()

# Generated at 2022-06-13 21:34:53.333581
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.verify = False
    assert make_send_kwargs_mergeable_from_env(args)['verify'] \
        == {False: False}.get(args.verify.lower(), args.verify)

# Generated at 2022-06-13 21:34:55.822620
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    for i in collect_messages(args, Path('.')):
        print(i)

# test_collect_messages()

# Generated at 2022-06-13 21:35:03.606612
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        chunked=False,
        data=3,
        form=False,
        headers=None,
        json=True,
        method='GET',
        url='http://httpbin.org/get',
        verify='no',
    )
    data = args.data
    auto_json = data and not args.form
    if (args.json or auto_json) and isinstance(data, dict):
        if data:
            data = json.dumps(data)
        else:
            # We need to set data to an empty string to prevent requests
            # from assigning an empty list to `response.request.data`.
            data = ''

    # Finalize headers.
    headers = make_default_headers(args)

# Generated at 2022-06-13 21:35:12.545978
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:35:14.254759
# Unit test for function collect_messages
def test_collect_messages():
    sys.stderr.write(str(collect_messages('https://httpie.org', None)))

# Generated at 2022-06-13 21:35:20.281260
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    result = make_send_kwargs_mergeable_from_env(args=argparse.Namespace())
    assert result == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }

# Generated at 2022-06-13 21:35:28.637823
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2022-06-13 21:35:38.454370
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json, args.form, args.data = False, False, None
    assert make_default_headers(args) == {}

    args.json, args.form, args.data = False, False, {}
    assert make_default_headers(args) == {}

    args.json, args.form, args.data = True, False, {}
    assert make_default_headers(args) == {
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    }

    args.json, args.form, args.data = False, True, {}
    assert make_default_headers(args) == {
        'Content-Type': FORM_CONTENT_TYPE
    }

    args.json, args.form, args.data = True, True, {}


# Generated at 2022-06-13 21:35:45.378800
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.__dict__.update({
        'json': False,
        'form': False,
        'files': None
    })

    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == DEFAULT_UA, "Test failed on User-Agent"
    assert default_headers['Accept'] == 'application/json, */*;q=0.5', "Test failed on Accept, when json is not set"
    assert 'Content-Type' not in default_headers, "Test failed on Content-Type, when json is not set"
    
    args.__dict__.update({
        'json': True,
        'form': False,
        'files': None
    })
    default_headers = make_default_headers(args)
    assert default_

# Generated at 2022-06-13 21:36:43.349774
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=10, allow_redirects=False)
    kwargs = {'timeout': args.timeout or None, 'allow_redirects': False}
    assert make_send_kwargs(args) == kwargs


# Generated at 2022-06-13 21:36:55.450932
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:37:07.544385
# Unit test for function collect_messages
def test_collect_messages():
    # Arrange
    import argparse
    args = argparse.Namespace()
    args.auth = None
    args.auth_plugin = None
    args.auth_type = None
    args.all = False
    args.compress = False
    args.compression_level = 6
    args.debug = False
    args.files = None
    args.form = False
    args.headers = {'User-Agent': 'HTTPie/0.9.9'}
    args.json = False
    args.method = 'GET'
    args.max_redirects = None
    args.offline = False
    args.output = None

# Generated at 2022-06-13 21:37:21.212019
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace();
    args.json = True
    args.data = {"name": "alex"}
    args.headers = {'Host': "localhost"}
    args.method = "POST"
    args.url = "http://localhost:9200/test/_doc/1"
    args.files = None
    args.chunked = False
    args.compress = False
    args.form = False
    result = make_request_kwargs(args)
    assert result['url'] == 'http://localhost:9200/test/_doc/1'
    assert result['method'] == 'POST'
    assert result['headers']['Host'] == 'localhost'
    assert result['headers']['Accept'] == 'application/json, */*;q=0.5'

# Generated at 2022-06-13 21:37:30.031253
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():

    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(key='http://www.example.com', value='www.example.com')]
    args.verify = 'true'
    args.cert = 'false'
    args.cert_key = 'false'
    
    assert make_send_kwargs_mergeable_from_env(args) == {'proxies': {'http://www.example.com': 'www.example.com'}, 'stream': True, 'verify': True, 'cert': None}

# Generated at 2022-06-13 21:37:39.968437
# Unit test for function make_default_headers
def test_make_default_headers():
    import copy
    import requests

    default_headers = {
        'User-Agent': DEFAULT_UA
    }
    request_headers = RequestHeadersDict()

    args = copy.deepcopy(requests.get('http://httpbin.org/get').request.kwargs)
    kwargs = {'headers': request_headers}
    args.update(kwargs)

    headers = make_default_headers(args)
    assert(headers == default_headers)
    assert(headers != request_headers)
    assert(len(headers) == 1)
    assert(headers['User-Agent'] == kwargs['headers']['User-Agent'])
    #
    default_headers = {
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT
    }
    request_headers = Request

# Generated at 2022-06-13 21:37:44.180947
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    arg = argparse.Namespace()
    arg.timeout = 1
    arg.allow_redirects = False
    kw = make_send_kwargs(arg)
    assert kw == {'timeout': 1, 'allow_redirects': False}


# Generated at 2022-06-13 21:37:48.105868
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    result = make_send_kwargs(args)
    assert result['timeout'] == 10
    assert result['allow_redirects'] == False


# Generated at 2022-06-13 21:38:00.607697
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()

    args.url = 'http://www.baidu.com'
    args.method = 'GET'
    args.cert = 'test'
    args.cert_key = 'test'
    args.verify = 'yes'
    args.verify = True
    args.data = 'test'
    args.form = True
    args.files = 'test'
    args.multipart = True
    args.multipart_data = 'test'
    args.boundary = 'test'
    args.headers = RequestHeadersDict()
    base_headers = RequestHeadersDict({'hello':'world'})
    request_body_read_callback = lambda chunk: chunk

    make_request_kwargs(args,base_headers,request_body_read_callback)



# Generated at 2022-06-13 21:38:11.379388
# Unit test for function make_default_headers