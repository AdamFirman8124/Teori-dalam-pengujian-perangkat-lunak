

# Generated at 2022-06-13 21:30:18.250273
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.data=[['a', 'b'], ['c', 'd']]
    args.form = False
    args.files = False
    args.json = False
    args.offline = False
    args.multipart = False
    args.chunked = False
    args.verify = 'yes'
    args.cert = False
    args.cert_key = False
    args.http2 = False
    args.proxy = ['http://bar']
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {'http://bar': None}
    assert kwargs['stream']
    assert kwargs['verify'] is True
    assert kwargs['cert'] is None


#

# Generated at 2022-06-13 21:30:24.632577
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.proxy = dict()
    args.verify = True
    args.cert = "CERT"
    args.cert_key = "CERT_KEY"
    args.timeout = None
    args.allow_redirects = False

    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] is None
    assert kwargs['allow_redirects'] is False


# Generated at 2022-06-13 21:30:25.887185
# Unit test for function build_requests_session
def test_build_requests_session():
    pass


# Generated at 2022-06-13 21:30:34.624975
# Unit test for function finalize_headers
def test_finalize_headers():
    # wrong type
    try:
        finalize_headers(0)
    except TypeError:
        pass
    else:
        assert False, 'TypeError not raised'

    # wrong type
    try:
        finalize_headers('wrong type')
    except TypeError:
        pass
    else:
        assert False, 'TypeError not raised'

    # contains wrong type
    try:
        finalize_headers({'wrongType': 0})
    except TypeError:
        pass
    else:
        assert False, 'TypeError not raised'

    # contains wrong type
    try:
        finalize_headers({'wrongType': 'wrong type'})
    except TypeError:
        pass
    else:
        assert False, 'TypeError not raised'

    # contains wrong type

# Generated at 2022-06-13 21:30:46.020055
# Unit test for function collect_messages
def test_collect_messages():
    return
    config_dir = Path("C:\\Users\\jeremy.wermeille\\.httpie")

# Generated at 2022-06-13 21:30:53.434589
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args=argparse.Namespace()
    args.method='POST'
    args.url='http://url'
    args.headers={'key':'value'}
    args.data={'key':'value'}
    args.json='True'
    args.form='True'
    args.files='True'
    args.multipart='True'
    args.multipart_data='data'
    args.boundary='boundary'
    args.chunked='True'
    args.offline='True'
    args.auth='password'
    args.params={'key':'value'}
    req=make_request_kwargs(args)
    assert(req['url']=='http://url')
    assert(req['method']=='post')

# Generated at 2022-06-13 21:31:04.590299
# Unit test for function make_request_kwargs
def test_make_request_kwargs():

    test_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    test_headers.update({"testheadername":"testheadervalue"})
    
    args = argparse.Namespace()
    args.method = "GET"
    args.url = "http://127.0.0.1:5000/api/v1.0/users"
    args.headers = test_headers
    args.data = ""
    args.json = ""
    args.form = ""
    args.files = ""
    args.auth = ""
    args.params = ""
    
    result_kwargs = make_request_kwargs(args)

    assert result_kwargs['method'] == 'get'

# Generated at 2022-06-13 21:31:16.125687
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    url = "https://www.example.com/test"
    data = {"hello" : "world"}
    content = json.dumps(data)
    args = {"headers": {"Accept": "application/json"},
            "method": "POST",
            "url": url,
            "json": True,
            "data": data}
    kwargs = make_request_kwargs(args)
    assert kwargs["headers"]["Accept"] == "application/json"
    assert kwargs["headers"]["User-Agent"] == "HTTPie/1.0.2"
    assert kwargs["method"] == "POST"
    assert kwargs["url"] == url
    assert kwargs["data"] == content
    assert kwargs["auth"] is None
    assert kwargs["params"] == []

# Generated at 2022-06-13 21:31:20.386759
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        args=None,
        chunked=False,
        compress=0,
        offline=False,
        method='GET',
        url='https://httpbin.org/get',
        headers={},
        data={},
        auth=None,
        follow=True,
    )
    print(make_request_kwargs(args))

if __name__ == "__main__":
    test_make_request_kwargs()

# Generated at 2022-06-13 21:31:21.002863
# Unit test for function collect_messages
def test_collect_messages():
    return

# Generated at 2022-06-13 21:31:43.964648
# Unit test for function max_headers
def test_max_headers():
    import http.client as client
    # Test with 3 headers
    with max_headers(3):
        assert client._MAXHEADERS == 3
    # Test with 5 headers
    with max_headers(5):
        assert client._MAXHEADERS == 5
    # Test without headers
    with max_headers(None):
        assert client._MAXHEADERS == float('Inf')
    # Test original header limit
    assert client._MAXHEADERS == 100

# Generated at 2022-06-13 21:31:55.052776
# Unit test for function make_default_headers
def test_make_default_headers():
    # Scenario 1: JSON mode
    # Expected output:
    # {'User-Agent': 'HTTPie/1.0.3', 'Accept': 'application/json, */*;q=0.5'}
    arguments = argparse.Namespace(json=True)
    output = make_default_headers(arguments)
    expected_output = {'User-Agent': 'HTTPie/1.0.3', 'Accept': 'application/json, */*;q=0.5'}
    assert output == expected_output
    
    # Scenario 2: Data mode
    # Expected output:
    # {'User-Agent': 'HTTPie/1.0.3'}
    arguments = argparse.Namespace(data="123")
    output = make_default_headers(arguments)

# Generated at 2022-06-13 21:32:04.883183
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class args_mock:
        pass
    
    args = args_mock()
    args.json = None
    args.form = None
    args.method = 'GET'
    args.url = 'http://example.com'
    args.headers = None
    args.data = None
    args.form = None
    args.files = None
    args.multipart = None
    args.multipart_data = None
    args.boundary = None
    args.auth = None
    args.params = {'foo': 'bar'}
    args.chunked = None
    args.offline = None

    kwargs = make_request_kwargs(args)
    
    print(kwargs)

# Generated at 2022-06-13 21:32:17.450733
# Unit test for function collect_messages
def test_collect_messages():
    import requests
    from httpie.debugging import collect_messages
    import json
    import argparse
    from pathlib import Path

# Generated at 2022-06-13 21:32:22.045823
# Unit test for function collect_messages
def test_collect_messages():
    output_list=[]
    output_list=list(collect_messages())
    print(output_list)
    # If a collect_messages function returns an empty list, the function is not working.
    assert len(output_list) != 0


# Generated at 2022-06-13 21:32:30.228901
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(json=False, form=False, files=False, data=None)
    headers = make_default_headers(args)

    assert len(headers) == 1
    assert headers['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:32:34.595610
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = None
    args.allow_redirects = False
    kwargs = make_send_kwargs(args)

    assert kwargs['timeout'] == None
    assert kwargs['allow_redirects'] == False

# Generated at 2022-06-13 21:32:37.988688
# Unit test for function max_headers
def test_max_headers():
    with max_headers(100):
        assert http.client._MAXHEADERS == 100
    assert http.client._MAXHEADERS != 100

# Generated at 2022-06-13 21:32:45.670401
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()

    # Simple args
    args.method = 'GET'
    args.url = 'http://www.google.com'
    args.compress = False
    args.json = False
    args.form = False
    args.multipart = False
    args.session = False
    args.session_read_only = False
    args.verify = True
    args.cert = None
    args.headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })
    args.cert = None
    args.files = None
    args.data = {}

    # Advanced args
    args.auth = None
    args.params = {}
    args.proxy = []

    # Debug args
    args.debug = False
    args.path_as_is = False


# Generated at 2022-06-13 21:32:58.422743
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    class Module(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __getitem__(self, key):
            return self.value

    class Arg:
        def __init__(self, verify):
            self.verify = verify

        def lower(self):
            return self.verify

    class Proxy(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

    args = argparse.Namespace(verify=Arg('true'), proxy=[Proxy('key', 'val')])

# Generated at 2022-06-13 21:34:03.689906
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args_test = argparse.Namespace()
    args_test.proxy = None
    args_test.verify = "FALSE"
    args_test.key_file = None
    args_test.cert_file = None

    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(
        args_test)

    assert send_kwargs_mergeable_from_env['proxies'] == None
    assert send_kwargs_mergeable_from_env['verify'] == False



# Generated at 2022-06-13 21:34:15.898881
# Unit test for function collect_messages
def test_collect_messages():
    class TestArgs:
        def __init__(self):
            self.session = None
            self.session_read_only = None
            self.headers = None
            self.url = 'http://example.com'
            self.auth = None
            self.debug = False
            self.json = False
            self.form = False
            self.data = False
            self.files = False
            self.multipart = False
            self.multipart_data = False
            self.boundary = False
            self.auth_plugin = None
            self.chunked = False
            self.offline = False
            self.timeout = False
            self.ssl_version = None
            self.ciphers = None
            self.cert = None
            self.follow = False
            self.max_redirects = None


# Generated at 2022-06-13 21:34:24.476734
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://httpbin.org/anything'
    args.headers = {}
    args.data = '{"hoge": "ほげ"}'
    args.files = {}
    args.multipart = False
    args.multipart_data = {}
    args.form = True
    args.json = False
    args.path_as_is = True
    args.compress = False
    args.chunked = False
    args.offline = True
    args.debug = False
    args.session = None
    args.session_read_only = None
    args.auth_plugin = None
    args.timeout = 30
    args.max_redirects = 0
    args.follow = False

# Generated at 2022-06-13 21:34:30.190469
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data = ('{"msg":"hello world"}'),
        form = True,
        files = ['test.txt'],
        json = True,
        verify = True)
    headers = make_default_headers(args)
    print(headers)



# Generated at 2022-06-13 21:34:33.741161
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    headers = make_default_headers(args)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

# Generated at 2022-06-13 21:34:38.731508
# Unit test for function max_headers
def test_max_headers():
    # noinspection PyProtectedMember
    assert http.client._MAXHEADERS == 200
    with max_headers(None):
        # noinspection PyProtectedMember
        assert http.client._MAXHEADERS == float('Inf')
    assert http.client._MAXHEADERS == 200

# Generated at 2022-06-13 21:34:47.025420
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.url = 'http://0.0.0.0:5000/foo'
    args.data = {'q': 'test'}
    headers = make_default_headers(args)
    assert headers['User-Agent'] != None
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE


# Generated at 2022-06-13 21:34:58.238544
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    default_headers = make_default_headers(args)
    assert default_headers == {'User-Agent':'HTTPie/1.0.3'}

    args.json = True
    default_headers = make_default_headers(args)
    assert default_headers == {'Accept':'application/json, */*;q=0.5', 'User-Agent':'HTTPie/1.0.3'}

    args.json = False
    args.form = True
    default_headers = make_default_headers(args)

# Generated at 2022-06-13 21:34:59.236165
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:35:10.379171
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.auth = None
    args.compress = False
    args.data = None
    args.download = False
    args.files = None
    args.form = False
    args.headers = []
    args.json = False
    args.method = 'get'
    args.params = []
    args.url = 'http://localhost:5000'
    args.verify = True
    args.verify = True
    args.verify = True
    args.verify = True
    args.verify = True
    args.verify = True
    args.verify = True
    assert make_request_kwargs(args)



# Generated at 2022-06-13 21:36:35.445764
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(
        ssl_version='TLSV1.0',
        ciphers='RC4',
        verify=False
    )
    assert(requests_session.adapters['https://'].ssl_options['ssl_version'] == ssl.PROTOCOL_TLSv1)
    assert(requests_session.adapters['https://'].ssl_options['ciphers'] == 'RC4')
    assert(requests_session.adapters['https://'].ssl_options['verify'] == False)


# Generated at 2022-06-13 21:36:41.143880
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.headers = {"Content-Type":"text/plain"}
    args.method = 'GET'
    args.url = 'https://httpbin.org/get'
    args.auth = None
    args.data = '{ "data" : "123"}'
    args.form = False
    args.json = True
    args.timeout = None
    args.verify = 'True'
    args.cert = None
    args.multipart = False
    args.boundary = None
    args.compress = 0
    args.debug = False
    args.max_redirects = None
    args.max_headers = None
    args.param=None
    args.proxy = None
    args.follow = False
    args.session = 'session'

# Generated at 2022-06-13 21:36:47.856900
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'false'
    args.cert = './test.pem'
    args.cert_key = './test.key'
    assert make_send_kwargs_mergeable_from_env(args) == {'proxies': {}, 'stream': True, 'verify': False, 'cert': args.cert}


# Generated at 2022-06-13 21:36:49.481416
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 1000


# Generated at 2022-06-13 21:36:56.854587
# Unit test for function make_default_headers
def test_make_default_headers():
    # Set arguments
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = {}
    args.files = {}
    # Method call
    result = make_default_headers(args)
    # Assertion
    assert result == RequestHeadersDict({"User-Agent": "HTTPie/1.0.2"})

# Generated at 2022-06-13 21:37:00.529891
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = None
    args.allow_redirects = None
    result = make_send_kwargs(args)


# Generated at 2022-06-13 21:37:04.080591
# Unit test for function max_headers
def test_max_headers():
    limit = 1024
    with max_headers(limit):
        assert http.client._MAXHEADERS == limit
    assert http.client._MAXHEADERS != limit


# Generated at 2022-06-13 21:37:08.071021
# Unit test for function max_headers
def test_max_headers():
    # GIVEN an args with max_headers
    args = argparse.Namespace()
    args.max_headers = 10

    with max_headers(args.max_headers):
        # THEN http.client._MAXHEADERS is set to the max headers
        # noinspection PyUnresolvedReferences
        assert http.client._MAXHEADERS == 10

# Generated at 2022-06-13 21:37:13.698547
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    from httpie.cli import parser
    args = parser.parse_args(['--timeout', '0.1', '--verify', 'no'])
    kwargs = make_send_kwargs(args)
    assert kwargs == {'allow_redirects': False, 'timeout': 0.1}

# Generated at 2022-06-13 21:37:24.793346
# Unit test for function make_request_kwargs