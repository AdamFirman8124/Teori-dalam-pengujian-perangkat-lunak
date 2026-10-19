

# Generated at 2022-06-13 21:30:28.971510
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
  args = {'proxy':[], 'gss': [], 'verify': 'yes', 'cert': [], 'cert_key':[]}
  # Test case 1: If no proxy, gss and cert, it only returns verify variable
  assert make_send_kwargs_mergeable_from_env(args) == {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}
  # Test case 2: If there is no proxy, gss and cert, but verify is False, it returns verify and stream variable
  args = {'proxy':[], 'gss': [], 'verify': 'no', 'cert': [], 'cert_key':[]}

# Generated at 2022-06-13 21:30:30.542252
# Unit test for function max_headers
def test_max_headers():
    max_headers(5)

# Generated at 2022-06-13 21:30:42.845447
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:30:48.236225
# Unit test for function make_default_headers
def test_make_default_headers():
    import json
    args = argparse.Namespace()
    r_dict = {}
    r_dict['User-Agent'] = DEFAULT_UA
    for header in make_default_headers(args).items():
        r_dict[header[0]] = header[1]
    assert(json.dumps(r_dict) == '{"User-Agent": "HTTPie/1.0.3"}')

# Generated at 2022-06-13 21:31:01.549480
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--data', default='')
    parser.add_argument('--files', action='append')
    args = parser.parse_args([])
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA

    args = parser.parse_args(['--json', '--data', '{}'])
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Content-Type'] == JSON_CONTENT_TYPE
    assert headers['Accept'] == JSON_ACCEPT


# Generated at 2022-06-13 21:31:09.850246
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(json=False, form=False, data=['foo'])
    headers = make_default_headers(args)
    if not headers.get('User-Agent') == DEFAULT_UA:
        print("Error:")
        print("User-Agent: %s expected, get: %s" % (DEFAULT_UA, headers.get('User-Agent')))
        return
    print("Success:")
    print("User-Agent: %s" % headers.get('User-Agent'))
    print("Accept: %s" % headers.get('Accept'))


# Generated at 2022-06-13 21:31:14.219327
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    request_body_read_callback = None
    for i in collect_messages(args, Path.cwd()):
        print(i)

# Generated at 2022-06-13 21:31:18.892423
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data=True,
        form=False,
        json=False,
    )
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE



# Generated at 2022-06-13 21:31:31.146224
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import argparse
    args = argparse.Namespace(
        method='GET',
        url='http://www.domain.com/',
        headers={'Accept': 'application/json'},
        data={'key1':'value1','key2':'value2'},
        timeout=5,
        form=True,
        cert=False,
        verify=True,
        proxy=[],
        offline=False,
        json=True,
        max_headers=None,
        auth=None,
        params={}
    )
    base_headers = None
    request_body_read_callback = lambda chunk: chunk
    kwargs = make_request_kwargs(
        args=args,
        base_headers=base_headers,
        request_body_read_callback=request_body_read_callback
    )

# Generated at 2022-06-13 21:31:38.320064
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    send_kwargs = make_send_kwargs(argparse.Namespace(timeout=True, allow_redirects=False))
    assert send_kwargs['timeout'] and not send_kwargs['allow_redirects']


# Generated at 2022-06-13 21:32:02.968267
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:32:14.595020
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:32:25.383244
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://www.example.com/'
    args.headers = {}
    args.auth = None
    args.params = {}
    args.files = None
    args.data = None
    args.json = False
    args.form = False
    args.timeout = None
    args.verify = False
    args.cert = None
    args.cert_key = None
    args.proxy = None
    args.debug = 0
    args.compress = 0
    args.max_headers = None
    args.follow = False
    args.max_redirects = 5
    args.all = False
    args.offline = False
    args.chunked = False
    args.multipart = False
    args

# Generated at 2022-06-13 21:32:33.849776
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    a = argparse.Namespace(**{'timeout': '30', 'allow_redirects': 'False'})
    kwargs = make_send_kwargs(a)

    assert (kwargs['timeout'] == 30)
    assert (kwargs['allow_redirects'] == False)



# Generated at 2022-06-13 21:32:47.586821
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://1234.com'
    args.headers = {}
    args.data = {}
    args.json = False
    args.form = False
    args.files = False
    args.multipart = False
    args.multipart_data = []
    args.boundary = '791793854c69be6e'
    args.chunked = False
    args.offline = False
    args.compress = True
    args.compress_level = 9
    args.timeout = None
    args.max_headers = 8192
    args.max_redirects = 30
    args.follow = False
    args.auth = 'auth'
    args.session = 'session'
    args.session_

# Generated at 2022-06-13 21:33:00.140037
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    kwargs = make_request_kwargs(
        args = argparse.Namespace(
            data = None,
            form = False,
            json = False,
            files = None,
            chunked = False,
            offline = False,
            method = 'POST',
            url = "http://test",
            headers = RequestHeadersDict({
                'User-Agent': 'HTTPie/1.0.0'
            }),
            auth = None,
            params = dict(),
        )
    )
    assert kwargs == {
        'method': 'post',
        'url': 'http://test',
        'headers': {
            'User-Agent': 'HTTPie/1.0.0'
        },
        'data': None,
        'auth': None,
        'params': []
    }

# Generated at 2022-06-13 21:33:14.118919
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.json = False
    args.form = True
    args.files = 'e:/test'
    args.multipart = False
    args.multipart_data = '{"name":"liqing"}'
    args.boundary = 'KjY5MehX9xgLuJjK'
    args.headers = {}
    args.data = {'name': 'liqi'}
    args.method = "GET"
    args.url = "http://localhost:8080?id=1"
    args.chunked = False
    args.offline = False

    kwargs = make_request_kwargs(args)
    print(json.dumps(kwargs, ensure_ascii=False, indent=4))


# Generated at 2022-06-13 21:33:17.629391
# Unit test for function collect_messages
def test_collect_messages():
    args = None
    config_dir = None
    request_body_read_callback = None
    for each in collect_messages(args,config_dir,request_body_read_callback):
        pass


# Generated at 2022-06-13 21:33:31.599588
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace(
        auth=b':',
        chunked=False,
        compress=False,
        data=[b'a',b'b'],
        debug=False,
        files=[],
        form=False,
        headers={},
        json=False,
        max_headers=0,
        method='GET',
        multipart=False,
        multipart_data={},
        offline=False,
        params=[('a', ' b'), ('c', 'd')],
        path_as_is=False,
        proxy=[],
        session='',
        session_read_only=None,
        timeout=120,
        url='http://httpbin.org/get',
        verify='true',
    )

# Generated at 2022-06-13 21:33:41.362321
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    # args.json, args.data
    test_args_json = argparse.Namespace(
        json=True,
        data=True
    )
    test_args_data = argparse.Namespace(
        json=False,
        data=True
    )

    # args.verify
    test_args_verify_true = argparse.Namespace(
        verify='true'
    )
    test_args_verify_false = argparse.Namespace(
        verify='false'
    )

    # args.proxy
    test_args_proxy = argparse.Namespace(
        proxy=[('HTTP', 'http://127.0.0.1:8080')]
    )

    # args.cert

# Generated at 2022-06-13 21:33:57.414754
# Unit test for function build_requests_session
def test_build_requests_session():
    expected_result = '<requests.sessions.Session object at 0x7ff562708e80>'
    result = build_requests_session(True, 'tls1.2', "ECDHE-RSA-AES256-GCM-SHA384")
    assert str(result) == expected_result

# Generated at 2022-06-13 21:34:04.831484
# Unit test for function collect_messages
def test_collect_messages():
    import argparse
    config_dir = Path('test_collect_messages')

# Generated at 2022-06-13 21:34:09.297457
# Unit test for function max_headers
def test_max_headers():
    max_headers_num = 512
    assert max_headers(max_headers_num).__exit__() == None
    assert max_headers(max_headers_num).__enter__()._MAXHEADERS == max_headers_num



# Generated at 2022-06-13 21:34:20.424157
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://httpbin.org/get?foo=bar'
    args.headers = RequestHeadersDict({})
    args.files = None
    args.data = None
    args.json = False
    args.form = False
    args.multipart = False
    args.multipart_data = {}
    args.boundary = None
    args.params = {}
    args.auth = 'auth'
    args.chunked = False
    args.timeout = 60.0
    args.max_redirects = 30
    args.verify = True
    args.cert = None
    args.cert_key = None
    args.debug = True
    args.follow = True
    args.max_headers = 1000

# Generated at 2022-06-13 21:34:23.148930
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.ArgumentParser()
    args.json = True
    args.data = {"message": "Hello World!","time": "20200121"}
    headers,content_type = make_default_headers(args)
    print(headers)

# Generated at 2022-06-13 21:34:35.235055
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class args(object):

        def __init__(self, method, url, data, json, form, files,
        headers, auth, params, offline, chunked, verify, cert, cert_key,
        proxy, timeout, max_redirects, max_headers, all, follow, chunked,
        debug, session, session_read_only, json_pp, style, print_body,
        compress, multipart, boundary, multipart_data, auth_plugin, path_as_is):

            self.method = method
            self.url = url
            self.data = data
            self.json = json
            self.form = form
            self.files = files
            self.headers = headers
            self.auth = auth
            self.params = params
            self.offline = offline
            self.chunked = chunked


# Generated at 2022-06-13 21:34:41.366611
# Unit test for function collect_messages
def test_collect_messages():
    arg_parser = argparse.ArgumentParser(description='httpie parser')
    args = arg_parser.parse_args()
    args.url = 'http://httpbin.org'
    config_dir = Path("/home/yuzhang/.config/httpie")
    for i in collect_messages(args,config_dir):
        print(i)


# Generated at 2022-06-13 21:34:48.687571
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(json=True, data=True, form=False, files=False)
    result = make_default_headers(args)
    expected = {'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json', 'User-Agent': 'HTTPie/0.3.0'}
    for key, value in result.items():
        assert expected[key] == value


# Generated at 2022-06-13 21:34:57.528004
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = False
    args.files = False
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({'User-Agent': 'HTTPie/0.9.9'})
    args.json = True
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({
        'Accept': 'application/json, */*;q=0.5',
        'Content-Type': 'application/json',
        'User-Agent': 'HTTPie/0.9.9',
    })

# Generated at 2022-06-13 21:34:58.705188
# Unit test for function make_default_headers
def test_make_default_headers():
    print(make_default_headers('args'))

# Generated at 2022-06-13 21:35:33.081616
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(headers=None, json="{}", form=None, files=None, data=None)

    default_headers = make_default_headers(args)

    assert default_headers['User-Agent'] == "HTTPie/{__version__}"
    assert default_headers['Accept'] == "application/json, */*;q=0.5"
    assert default_headers['Content-Type'] == "application/json"


# Generated at 2022-06-13 21:35:42.972548
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import argparse
    args = argparse.Namespace()
    args.verify = 'true'
    args.proxy = [('http', 'http://127.0.0.1:1234'), ('https', 'http://127.0.0.1:5678')]
    args.cert = 'cert.pem'
    args.cert_key = 'cert_key.pem'
    expected_kwargs = {
        'proxies': {'http': 'http://127.0.0.1:1234', 'https': 'http://127.0.0.1:5678'},
        'stream': True,
        'verify': True,
        'cert': 'cert.pem',
    }
    actual_kwargs = make_send_kwargs_mergeable_from_env(args)


# Generated at 2022-06-13 21:35:45.790439
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(
    verify=False,
    ssl_version=False,
    ciphers=None,
)

# Generated at 2022-06-13 21:35:48.463680
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:36:01.155317
# Unit test for function make_default_headers
def test_make_default_headers():
    class arg:
        def __init__(self):
            self.json = None
            self.data = None
            self.form = None
        def __contains__(self, item):
            return False
    args = arg()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    args.json = True
    args.data = '{"a": "b"}'
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE
    args.json = False
    args.data = None
    args.form = True
    headers = make_default_headers(args)
    assert headers['User-Agent']

# Generated at 2022-06-13 21:36:07.206950
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(proxy=[], verify=False, cert=None, cert_key=None)
    env = {
        'no_proxy': '*',
        'http_proxy': 'http://127.0.0.1:8888',
        'HTTP_PROXY': 'http://127.0.0.1:8888',
        'https_proxy': 'http://127.0.0.1:8888',
        'HTTPS_PROXY': 'http://127.0.0.1:8888',
        'REQUESTS_CA_BUNDLE': 'cacert.pem',
        'CURL_CA_BUNDLE': 'cacert.pem',
    }


# Generated at 2022-06-13 21:36:08.946440
# Unit test for function collect_messages
def test_collect_messages():
    # If this function runs, the test is successful and the function is working
    assert True

# Generated at 2022-06-13 21:36:17.754877
# Unit test for function max_headers
def test_max_headers():
    from unittest import mock
    import http
    import httpie.core

    with mock.patch('httpie.core.http.client._MAXHEADERS', 999):
        import http.client
        http.client._MAXHEADERS = 111
        with max_headers(100):
            assert http.client._MAXHEADERS == 100
        assert http.client._MAXHEADERS == 111

    with mock.patch('httpie.core.http.client._MAXHEADERS', 999):
        import http.client
        http.client._MAXHEADERS = 111
        with max_headers(None):
            assert http.client._MAXHEADERS == float('inf')
        assert http.client._MAXHEADERS == 111

# Generated at 2022-06-13 21:36:23.558238
# Unit test for function build_requests_session
def test_build_requests_session():
    ssl_version = None
    ciphers = None
    verify = False
    requests_session = build_requests_session(
        ssl_version=ssl_version,
        ciphers=ciphers,
        verify=verify
    )
    assert requests_session.verify == False
    assert isinstance(requests_session.adapters['https://'], HTTPieHTTPSAdapter)
    assert not requests_session.proxies
    assert not requests_session.headers


# Generated at 2022-06-13 21:36:29.829590
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.data = {'foo': 'bar'}
    args.form = False
    args.json = True
    default_headers = make_default_headers(args)
    assert default_headers['Accept'] == JSON_ACCEPT

# Generated at 2022-06-13 21:37:06.970708
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(
        ssl_version='TLSv1_2',
        ciphers='TLS_AES_128_GCM_SHA256',
        verify=True
    )

    assert requests_session is not None



# Generated at 2022-06-13 21:37:12.781371
# Unit test for function make_default_headers
def test_make_default_headers():
    from argparse import Namespace
    args = Namespace()
    args.data = {}
    args.headers = {}
    args.json = False
    args.form = False

    result = make_default_headers(args)
    assert 'Accept' not in result
    assert 'Content-Type' not in result


# Generated at 2022-06-13 21:37:19.308044
# Unit test for function collect_messages
def test_collect_messages():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-offline", action='store_true', default=False)
    args = parser.parse_args()
    config_dir = None
    request_body_read_callback = None
    print(list(collect_messages(args, config_dir, request_body_read_callback)))


# Generated at 2022-06-13 21:37:26.226093
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    headers = make_default_headers(args)
    assert headers['User-Agent'] == 'HTTPie/0.9.9'
    assert headers['Content-Type'] == 'application/json'
    assert headers['Accept'] == 'application/json, */*;q=0.5'

# Generated at 2022-06-13 21:37:29.190298
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli import parser
    args = parser.parse_args()
    config_dir = Path.home() / '.httpie'
    for item in collect_messages(args, config_dir):
        print(item)


if __name__ == "__main__":
    test_collect_messages()

# Generated at 2022-06-13 21:37:36.153689
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    args.json = True
    args.method = 'POST'
    args.url = 'http://myhost.com'
    config_dir = Path('test')
    request_body_read_callback = lambda chunk: chunk
    if(collect_messages(args, config_dir, request_body_read_callback)!=None):
        print('test passed')
        return True
    else:
        print('test not passed')
        return False

# Generated at 2022-06-13 21:37:48.147946
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.context import Environment
    from httpie.compat import urlparse

    class Namespace:
        pass

    args = Namespace()
    env = Environment()
    args.verify = env.config.get('verify', True)
    args.proxy = env.config.get('proxy', None)
    args.cert = env.config.get('cert', None)
    args.cert_key = env.config.get('cert_key', None)

    kwargs = make_send_kwargs_mergeable_from_env(args)

    assert kwargs['verify'] == env.config.get('verify', True)
    assert kwargs['cert'] == env.config.get('cert', None)
    proxy = env.config.get('proxy', None)
    if proxy:
        assert k

# Generated at 2022-06-13 21:37:56.011635
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env("args")
    assert send_kwargs_mergeable_from_env['proxies']
    assert send_kwargs_mergeable_from_env['stream']
    assert send_kwargs_mergeable_from_env['verify']
    assert send_kwargs_mergeable_from_env['cert']

# Generated at 2022-06-13 21:37:58.350961
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()

    headers = make_default_headers(args)

    assert 'User-Agent' in headers


# Generated at 2022-06-13 21:38:10.963778
# Unit test for function collect_messages
def test_collect_messages():
    print("Testing collect_messages")
    import argparse
    import os
    import unittest

    from httpie.utils import detect_raw_data_type
    from httpie.client import stdin_bytes

    from httpie.core import main

    def prepare_args(args, stdin, *extra_args):
        class StdInBytes(io.BytesIO):
            def read(self, size=None):
                return super().read().rstrip(b'\n')

        class StdInText(io.TextIOWrapper):
            def read(self, size=None):
                return super().read().rstrip('\n')

        parser = argparse.ArgumentParser()
        if len(args):
            parser.parse_args(args)

        class args:
            url = ''
            headers = []

# Generated at 2022-06-13 21:38:41.837097
# Unit test for function make_default_headers
def test_make_default_headers():
    # use args.json or args.data
    args1 = argparse.Namespace(
        json=True,
        data={'a': 1, 'b': 2}
    )
    expected_headers1 = {
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    }
    assert make_default_headers(args1) == expected_headers1
    # use args.form
    args2 = argparse.Namespace(
        form=True,
        files=False
    )
    expected_headers2 = {
        'User-Agent': DEFAULT_UA,
        'Content-Type': FORM_CONTENT_TYPE
    }
    assert make_default_headers(args2) == expected_headers2


# Generated at 2022-06-13 21:38:52.877514
# Unit test for function make_default_headers
def test_make_default_headers():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default=None)
    parser.add_argument('--form', action='store_true', default=False)
    parser.add_argument('--json', action='store_true', default=False)

    args = parser.parse_args(['--data','{"hello":"world"}'])
    default_headers = make_default_headers(args)
    print(default_headers)

    args.json = True
    args.data = {"hello":"world"}
    default_headers = make_default_headers(args)
    print(default_headers)

    args.form = True
    default_headers = make_default_headers(args)
    print(default_headers)



# Generated at 2022-06-13 21:39:05.905576
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    assert make_send_kwargs_mergeable_from_env(argparse.Namespace(
        cert=["/path/to/my/cert.pem", "/path/to/my/key.pem"], proxy=[], verify='yes')) == {
            'proxies': {},
            'stream': True,
            'verify': True,
            'cert': ['/path/to/my/cert.pem', '/path/to/my/key.pem']}
    assert make_send_kwargs_mergeable_from_env(argparse.Namespace(
        cert=None, proxy=[], verify='yes')) == {
            'proxies': {},
            'stream': True,
            'verify': True,
            'cert': None}
    assert make_send_kwargs_mer

# Generated at 2022-06-13 21:39:08.023122
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:39:11.006818
# Unit test for function max_headers
def test_max_headers(): 
    headers = {'Content-Type': 'application/json'}
    with max_headers(2):
        assert 'Content-Type' not in headers
    assert 'Content-Type' in headers

# Generated at 2022-06-13 21:39:17.764611
# Unit test for function make_default_headers
def test_make_default_headers():
    import argparse
    args = argparse.Namespace()
    args.json=True
    args.data={'name':'Siavash','last_name':'Sabaie','skill':'Python','job':'software_engineer'}
    headers=make_default_headers(args)
    assert headers=={'User-Agent': f'HTTPie/{__version__}', 'Accept': 'application/json, */*;q=0.5', 'Content-Type': 'application/json'}

# Generated at 2022-06-13 21:39:28.869233
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # noinspection PyPep8Naming
    class Args():
        def __init__(self, proxy=None, verify=None, cert=None, cert_key=None):
            self.proxy = proxy
            self.verify = verify
            self.cert = cert
            self.cert_key = cert_key

    # Case where proxy, verify, cert and cert_key are set to None
    actual = make_send_kwargs_mergeable_from_env(Args())
    expected = {'proxies': {}, 'verify': None, 'cert': None}
    assert actual == expected

    # Case where proxy, verify, cert and cert_key are set to values

# Generated at 2022-06-13 21:39:40.370079
# Unit test for function make_request_kwargs