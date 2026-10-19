

# Generated at 2022-06-13 21:30:03.156024
# Unit test for function make_default_headers
def test_make_default_headers():
    a = argparse.Namespace(
        data = 'Hello World',
        form = True
    )
    assert make_default_headers(a)
    assert make_default_headers(a).get('Content-Type') == 'application/x-www-form-urlencoded; charset=utf-8'


# Generated at 2022-06-13 21:30:05.421781
# Unit test for function collect_messages
def test_collect_messages():
    args = "args"
    config_dir = "config_dir"
    request_body_read_callback = "request_body_read_callback"
    assert collect_messages(args, config_dir, request_body_read_callback)

# Generated at 2022-06-13 21:30:10.293408
# Unit test for function max_headers
def test_max_headers():
    print("\n\n\t*****Running max headers method of requests.py*****\n\n")
    print("Running for limit=None")
    try:
        with max_headers(None):
            print("In try block")
            assert http.client._MAXHEADERS == float('Inf')
    except Exception as e:
        print("Exception", e)
    finally:
        print("In finally block")


# Generated at 2022-06-13 21:30:18.175856
# Unit test for function collect_messages
def test_collect_messages():
    class MockRequest():
        def __init__(self, url):
            self.url = url
    class MockResponse():
        def __init__(self, next_response, status_code, history_response=None):
            self.next = next_response
            self.status_code = status_code
            self.history = history_response

    class MockNamespace():
        headers = {
            'Host': 'www.google.com',
            'User-Agent': DEFAULT_UA
        }
        url = 'http://www.google.com'
        method = 'GET'
        params = dict()
        data = dict()


# Generated at 2022-06-13 21:30:23.682046
# Unit test for function max_headers
def test_max_headers():
    input = {
        'method': 'GET',
        'url': 'https://google.com/',
        'timeout': 2,
        'allow_redirects': True,
    }

    output = make_send_kwargs(input)
    expected_output = {
        'timeout': 2,
        'allow_redirects': True
    }

    assert output == expected_output

# Generated at 2022-06-13 21:30:27.686302
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    assert make_send_kwargs(args) == {'timeout': 10, 'allow_redirects': False}


# Generated at 2022-06-13 21:30:30.800298
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = make_request_kwargs({'method': 'GET', 'url': 'http://www.baidu.com'})
    print(args)

if __name__ == '__main__':
    test_make_request_kwargs()

# Generated at 2022-06-13 21:30:36.367518
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 30
    args.allow_redirects = False
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] == 30
    assert kwargs['allow_redirects'] == False



# Generated at 2022-06-13 21:30:40.033477
# Unit test for function max_headers
def test_max_headers():
    http.client._MAXHEADERS = 0
    assert http.client._MAXHEADERS == 0
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == 0


# Generated at 2022-06-13 21:30:50.231636
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:31:20.447445
# Unit test for function collect_messages
def test_collect_messages():
    print("Test collect_messages")

# Generated at 2022-06-13 21:31:32.380042
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    parser_obj = argparse.ArgumentParser(
        description='Send HTTP requests from a terminal',
        prog='httpie-test',
    )
    args_obj = parser_obj.parse_args()
    args_obj.verify = 'yes'
    args_obj.proxy = ['http']
    args_obj.cert = 'cert.pem'
    args_obj.cert_key = 'cert_key.pem'
    kwargs = make_send_kwargs_mergeable_from_env(args_obj)
    assert kwargs['verify'] is True
    assert kwargs['cert'][0] == args_obj.cert
    assert kwargs['cert'][1] == args_obj.cert_key

# Generated at 2022-06-13 21:31:45.737250
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class Args:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    args = Args(
        auth='user:password',
        chunked='auto',
        data='{"name": "value"}',
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        json='streamed',
        method='GET',
        params={'k': 'v'},
        url='http://httpbin.org',
    )

    # Force data to be json encoded.
    args.data = json.dumps(args.data)

    # Merge the headers
    headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    headers.update(args.headers)

    #

# Generated at 2022-06-13 21:31:49.848003
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Unit test for function make_request_kwargs
    from requests.models import Request
    from httpie.cli.parser import create_parser
    args = create_parser().parse_args(['--json', 'localhost'])
    kwargs = make_request_kwargs(args)
    import pprint
    pprint.pprint(kwargs)

# Generated at 2022-06-13 21:31:55.174175
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=3, allow_redirects=False)
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] == 3
    assert kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:31:59.839245
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        json=False,
        form=False,
        files=False,
        data=False,
    )
    default_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    assert make_default_headers(args) == default_headers

# Generated at 2022-06-13 21:32:03.266765
# Unit test for function build_requests_session
def test_build_requests_session():
    assert build_requests_session(
        ssl_version='TLSv2',
        ciphers=None,
        verify=True,
    )

# Generated at 2022-06-13 21:32:07.018636
# Unit test for function max_headers
def test_max_headers():
    limit_value = 10
    http.client._MAXHEADERS = limit_value
    with max_headers(None):
        print('http.client._MAXHEADERS: ', http.client._MAXHEADERS)

if __name__ == '__main__':
    test_max_headers()

# Generated at 2022-06-13 21:32:19.874262
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'Get'
    args.url = 'http://www.example.com/'
    args.headers = finalize_headers(RequestHeadersDict({'Host': 'www.example.com'}))
    args.data = 'foo=bar&baz=bar'
    args.json = 0
    args.form = 1
    args.files = 0
    args.multipart = 0
    args.multipart_data = []
    args.boundary = '-----------------------------28947758029299'
    args.auth = 'admin:admin'
    args.params = {'foo': 'bar'}
    

# Generated at 2022-06-13 21:32:36.805013
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:33:09.061636
# Unit test for function max_headers
def test_max_headers():
    adict = {
        'Accept': 'application/json',
        'cookie': 'foo=bar',
        'Set-Cookie': 'bat=baz'
    }
    assert len(adict) == 3
    with max_headers(2):
        assert len(adict) == 2
    assert len(adict) == 3

# Generated at 2022-06-13 21:33:19.297699
# Unit test for function collect_messages
def test_collect_messages():
    import sys
    import json
    import ssl

    class Args:
        args = []
        data = None
        files = None
        json = False
        form = False
        params = []
        headers = {}
        chunked = False
        offline = False
        timeout = None
        auth = None
        cert = None
        cert_key = None
        verify = None
        proxy = []
        session = None
        http_version = None
        debug = False
        max_redirects = None
        follow = True
        all = False
        stream = True
        method = 'GET'
        url = 'http://example.org/'
        max_headers = None
        path_as_is = False
        compress = True
        ssl_version = None
        ciphers = None

    arg = Args()

# Generated at 2022-06-13 21:33:21.971835
# Unit test for function max_headers
def test_max_headers():
    with max_headers(float('Inf')):
        assert http.client._MAXHEADERS == float('Inf')


# Generated at 2022-06-13 21:33:30.858628
# Unit test for function max_headers
def test_max_headers():
    # Test we can set the limit
    limit = 10
    with max_headers(limit):
        assert http.client._MAXHEADERS == limit
    # Test we can set it to None
    with max_headers(None):
        assert http.client._MAXHEADERS == float("inf")
    # Test we can set it back to default
    with max_headers(0):
        assert http.client._MAXHEADERS != 0
        assert http.client._MAXHEADERS != float("inf")



# Generated at 2022-06-13 21:33:35.510189
# Unit test for function make_default_headers
def test_make_default_headers():
    args = lambda: None
    args.json = False
    args.form = False
    args.compress = 0
    args.data = None
    args.files = None
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA


# Generated at 2022-06-13 21:33:43.161026
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.verify = 'yes'
    args.proxy = []
    args.cert = None
    args.cert_key = None

    expected = {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}
    assert make_send_kwargs_mergeable_from_env(args) == expected

#Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:33:47.986380
# Unit test for function collect_messages
def test_collect_messages():
    encoded_url = "http://www.example.com/foo/bar?baz=qux"
    x = collect_messages(encoded_url)
    assert next(x) == "foo"

if __name__ == "__main__":
    test_collect_messages()

# Generated at 2022-06-13 21:33:56.874612
# Unit test for function collect_messages
def test_collect_messages():
    global_args = argparse.Namespace()
    global_args.debug = True
    global_args.method = 'GET'
    global_args.url = 'http://localhost:8000'
    global_args.headers = get_default_headers()
    global_args.session = None
    global_args.session_read_only = None
    global_args.auth = None
    global_args.auth_plugin = None
    global_args.compress = None
    global_args.verify = True
    global_args.json = False
    global_args.form = False
    global_args.data = None
    global_args.params = {}
    global_args.files = []
    global_args.max_redirects = None
    global_args.follow = False
    global_args.path_as_

# Generated at 2022-06-13 21:33:58.214387
# Unit test for function collect_messages
def test_collect_messages():
    collect_messages(args=argparse.Namespace(), config_dir=Path())

# Generated at 2022-06-13 21:34:01.130052
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    result = json.dumps(headers)
    assert result == "{\"User-Agent\":\"HTTPie/0.9.9\"}"



# Generated at 2022-06-13 21:34:26.191787
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        offline=False,
        chunked=False,
        timeout=30,
        follow=False,
        max_redirects=5,
        verify="yes",
        cert="cert",
        cert_key="cert_key",
        proxy=[argparse.Namespace(key="key", value="value")],
        stream=True,
        data="data"
    )

    kwargs = make_send_kwargs(args)
    assert len(kwargs) == 2
    assert kwargs['timeout'] == 30
    assert not kwargs['allow_redirects']

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert len(kwargs) == 5

# Generated at 2022-06-13 21:34:35.271090
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from argparse import Namespace
    from httpie.compat import ProxyDict
    import json

    proxy = ProxyDict({'key': 'value'})
    args = Namespace(
        proxies = [proxy],
        verify = 'yes',
        cert = 'cert.pem',
        cert_key = 'cert_key.pem'
    )

    assert make_send_kwargs_mergeable_from_env(args) == {
        'cert': ('cert.pem', 'cert_key.pem'),
        'proxies': {'key': 'value'},
        'stream': True,
        'verify': True
    }

# Generated at 2022-06-13 21:34:45.690322
# Unit test for function max_headers

# Generated at 2022-06-13 21:34:57.248400
# Unit test for function collect_messages
def test_collect_messages():

    import httpie.cli
    import httpie.cli.args
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.compat import is_windows
    
    args = httpie.cli.parse_args(args=[],env=False)
    args_httpbin = httpie.cli.parse_args(args=['httpbin.org'],env=False)
    
    
    
    assert args_httpbin.auth == ''
    assert args_httpbin.auth_plugin == None
    assert args_httpbin.cert == None
    assert args_httpbin.cert_key == None
    assert args_httpbin.check_status == True
    assert args_httpbin.compress == False
    assert args_httpbin.debug == False
    assert args_httpbin.default_options == []
   

# Generated at 2022-06-13 21:35:02.668681
# Unit test for function max_headers
def test_max_headers():
    limit = 1
    assert (http.client._MAXHEADERS==None)
    with max_headers(limit):
        assert (http.client._MAXHEADERS==limit)
    assert (http.client._MAXHEADERS==None)

# Generated at 2022-06-13 21:35:07.385303
# Unit test for function make_default_headers
def test_make_default_headers():
    request_headers_dict = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    assert request_headers_dict == make_default_headers(argparse.Namespace(form=True, data=None, files=None))

# Generated at 2022-06-13 21:35:19.488260
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(data=True, form=False, json=False)
    ans = make_default_headers(args)
    assert ans['User-Agent'] == DEFAULT_UA
    assert ans['Accept'] == JSON_ACCEPT
    assert ans['Content-Type'] == JSON_CONTENT_TYPE

    args = argparse.Namespace(data=True, form=True, json=False)
    ans = make_default_headers(args)
    assert ans['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in ans
    assert ans['Content-Type'] == FORM_CONTENT_TYPE

    args = argparse.Namespace(data=False, form=False, json=False)
    ans = make_default_headers(args)
    assert ans['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:35:33.288042
# Unit test for function collect_messages

# Generated at 2022-06-13 21:35:40.343327
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import argparse
    from httpie.cli import parser

    # Get the parser
    args = parser.parse_args()

    # Override default values
    args.verify = 'yes'
    args.cert_key = ''
    args.cert = ''
    args.proxy = ''

    # Call the function
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)

    # Prepare expected output
    expected_kwargs = {
        'proxies': '',
        'stream': True,
        'verify': True,
        'cert': ''
    }

    assert send_kwargs_mergeable_from_env == expected_kwargs



# Generated at 2022-06-13 21:35:51.544275
# Unit test for function max_headers
def test_max_headers():
    from httpie.cli import parser

    args = parser.parse_args(["http"])
    args.max_headers = 999
    args.timeout = 1
    args.url = "http://httpbin.org"
    args.max_redirects = 1
    args.proxies = []
    args.follow = True
    args.headers = {}
    args.auth_plugin = None
    args.auth = None
    args.output_opts = argparse.Namespace()
    args.session = None
    args.session_read_only = None
    args.stream = True
    args.output_file = None
    args.output_file_q = False
    args.verify = True
    args.verify_q = False
    args.timeout_q = False
    args.verbose = False
   

# Generated at 2022-06-13 21:36:17.277896
# Unit test for function make_default_headers
def test_make_default_headers():
    from httpie.cli.parser import get_parser
    args = get_parser().parse_args(
        [
            "--json",
            "--data",
            "{\"name\":\"花\",\"value\":\"flower\"}"
        ],
        env={"LANG": "en_US.UTF-8"}
    )
    default_headers = make_default_headers(args)
    assert default_headers == {'User-Agent': 'HTTPie/'+__version__, 'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json'}

# Generated at 2022-06-13 21:36:29.751224
# Unit test for function build_requests_session

# Generated at 2022-06-13 21:36:44.100425
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = ["http", "http://127.0.0.1:8080/api/v1/hype/user", "-j", "{\"accessToken\":\"\",\"userID\":\"\"}"]
    parser = httpie.cli.parser.get_argparser()
    parsed = parser.parse_args(args)
    # res = make_request_kwargs(parsed)
    # res = make_send_kwargs(parsed)
    # res = make_send_kwargs_mergeable_from_env(parsed)
    # res = build_requests_session(False)
    # res = dump_request({})
    res = finalize_headers(parsed.headers)
    res = make_default_headers(parsed)
    pass

# Generated at 2022-06-13 21:36:54.895044
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Unit tests
    # Test part 1:
    # Test if return type of make_request_kwargs is a dictionary
    # Test if request_body_read_callback is a function which return a dictionary
    assert type(make_request_kwargs(args=None,
                                    base_headers={'Content-Type': 'json/blah'},
                                    request_body_read_callback=None)) == dict
    assert type(make_request_kwargs(args=None,
                                    base_headers={'Content-Type': 'json/blah'},
                                    request_body_read_callback=lambda x: x)) == dict
    # Test if request_body_read_callback is not a function

# Generated at 2022-06-13 21:36:59.016484
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs['timeout'] == args.timeout
    assert send_kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:37:09.502525
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    namespace = argparse.Namespace(
        method = 'POST',
        json = True,
        data = {
            "a":1,
            "b":2,
            "c":3
        },
        headers = {
            "Accept":"application/x-www-form-urlencoded; charset=utf-8"
        },
        url = "https://httpbin.org/anything",
        auth = None

    )
    kwargs = make_request_kwargs(namespace)
    assert kwargs['headers']['Accept'] == "application/x-www-form-urlencoded; charset=utf-8"
    assert kwargs['url'] == "https://httpbin.org/anything"
    assert kwargs['method'] == "post"

# Generated at 2022-06-13 21:37:13.429699
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(proxy=[])
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['verify'] == True
    assert result['proxies'] == {}

# Generated at 2022-06-13 21:37:24.677904
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://www.google.com'
    args.headers = {}
    args.json = None
    args.form = None
    args.files = None
    args.data = None
    args.auth = None
    args.params = []
    args.compress = None
    args.compress_level = 0
    args.timeout = None
    args.max_redirects = None
    args.follow = None
    args.max_headers = None
    args.traceback = None
    args.check_status = None
    args.referer = None
    args.allow_redirects = None
    args.stream = None
    args.verify = None
    args.cert = None
    args.cert_key

# Generated at 2022-06-13 21:37:28.223613
# Unit test for function make_default_headers
def test_make_default_headers():
    expected = {
        'User-Agent': 'HTTPie/0.9.9',
    }
    args = argparse.Namespace()
    assert make_default_headers(args) == expected


# Generated at 2022-06-13 21:37:38.099797
# Unit test for function make_default_headers
def test_make_default_headers():
    https_adapter = HTTPieHTTPSAdapter(
        ciphers='ALL',
        verify=True,
        ssl_version='SSLv23'
    )
    assert https_adapter.cert_verify == True
    assert https_adapter.ciphers == 'ALL'
    assert https_adapter.ssl_version == 'SSLv23'
    requests_session = requests.Session()
    assert requests_session.proxies == {}
    assert 'stream' in requests_session.__dict__
    assert 'verify' in requests_session.__dict__
    assert requests_session.cert == None
    assert requests_session.stream == True
    assert requests_session.verify == True

# Generated at 2022-06-13 21:38:25.255853
# Unit test for function collect_messages
def test_collect_messages():

    from httpie.cli.parser import parser
    args = parser.parse_args([
        'doc/httpie.org',
        '-X', 'PUT',
        '-H', 'Content-Type: application/json; charset=utf-8'
    ])

    args.path_as_is = True
    args.compress = True
    args.max_headers = 2
    args.max_redirects = 3
    args.follow = True
    args.all = True
    args.debug = True
    args.offline = False
    args.timeout = 1
    args.verify = True
    args.cert = True
    args.cert_key = True
    args.proxy = [True]
    args.stream = True
    args.method = 'GET'

# Generated at 2022-06-13 21:38:34.552402
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    class Args:
        def __init__(self, cert, cert_key, proxy, verify):
            self.cert = cert
            self.cert_key = cert_key
            self.proxy = proxy
            self.verify = verify

    proxy_key = "http://127.0.0.1"
    proxy_value = "127.0.0.1:8080"
    proxy = (proxy_key, proxy_value)
    args_list = [
        Args(None, None, proxy, "yes"),
        Args(None, None, proxy, "true"),
        Args(None, None, proxy, "no"),
        Args(None, None, proxy, "false")
    ]

# Generated at 2022-06-13 21:38:46.861568
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import io
    data = dict()
    data['a'] = 'a'
    data['b'] = 'b'
    data = json.dumps(data)
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://127.0.0.1:5000/api/'
    args.headers = RequestHeadersDict()
    args.headers['Content-Type'] = 'application/json'
    args.data = data
    args.json = False
    args.auth = None
    args.params = dict()
    args.params['a'] = 'a'
    args.params['b'] = 'b'
    args.compress = False
    args.compress_level = 9
    args.form = False
    args.files = None
    args.mult

# Generated at 2022-06-13 21:38:55.863250
# Unit test for function collect_messages

# Generated at 2022-06-13 21:39:06.076836
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path()
    messages = collect_messages(args,config_dir=Path())
    request_body_read_callback()
    args.session = None
    args.session_read_only = None
    args.url = 'https://www.baidu.com'
    args.method = 'GET'
    make_request_kwargs(args=args,base_headers=None,request_body_read_callback=None)
    make_send_kwargs_mergeable_from_env(args=args)


# Generated at 2022-06-13 21:39:08.186118
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    send_kwargs = make_send_kwargs(args=None)
    assert(send_kwargs["allow_redirects"] == False)

# Generated at 2022-06-13 21:39:14.194019
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.url = 'http://example.com/'
    args.headers = {}
    args.json = None
    args.form = None
    args.data = None
    args.files = None
    default_headers = make_default_headers(args)
    assert default_headers == {'User-Agent': 'HTTPie/0.101'}

# Generated at 2022-06-13 21:39:21.208368
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--session')
    parser.add_argument('--timeout')
    parser.add_argument('--allow-redirects')
    parser.add_argument('--verify')
    parser.add_argument('--cert')
    parser.add_argument('--cert-key')
    parser.add_argument('--proxy', action='append')
    parser.add_argument('--method', default='GET')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--data', action='append')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--files', action='append')
    parser.add_argument('--chunked', action='store_true')
    parser

# Generated at 2022-06-13 21:39:26.847012
# Unit test for function collect_messages
def test_collect_messages():

    args = argparse.Namespace()
    config_dir = Path()
    request_body_read_callback = lambda chunk: chunk
    all_messages = collect_messages(
        args=args,
        config_dir=config_dir,
        request_body_read_callback=request_body_read_callback
    )
    assert type(all_messages) == type(list())

test_collect_messages()

# Generated at 2022-06-13 21:39:33.776545
# Unit test for function collect_messages
def test_collect_messages():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u')
    parser.add_argument('--headers', '-h')

    args = parser.parse_args(['-u', '127.0.0.1:20000', '-h', 'Content-Type:application/json'])

    for a in collect_messages(args, ''):
        print(a)


if __name__ == '__main__':
    test_collect_messages()