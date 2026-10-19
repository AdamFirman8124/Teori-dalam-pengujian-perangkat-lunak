

# Generated at 2022-06-13 21:30:02.571216
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    """
    Test function make_send_kwargs_mergeable_from_env
    """
    args = argparse.Namespace()
    if sys.version_info >= (3, 7):
        args.verify = True
    else:
        args.verify = 'yes'
    args.proxy = []
    args.cert = None
    args.cert_key = None

    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    assert make_send_kwargs_mergeable_from_env(args) == expected

    args.verify = 'False'


# Generated at 2022-06-13 21:30:10.425981
# Unit test for function collect_messages
def test_collect_messages():
    class ArgsMock(object):
        def __init__(self):
            self.url = 'http://www.google.com'
            self.method = 'GET'
            self.headers = {'foo': 'bar'}
            self.auth = ('', '')
            self.params = {'q': 'hello'}
            self.data = {'data': 'test data'}
            self.json = None
            self.form = None
            self.files = None
            self.compress = None
            self.debug = None
            self.max_redirects = None
            self.follow = None
            self.all = None
            self.offline = None
            self.max_headers = None
            self.chunked = None
            self.ssl_version = None
            self.verify = None

# Generated at 2022-06-13 21:30:14.387205
# Unit test for function make_send_kwargs
def test_make_send_kwargs():

    import argparse

    assert make_send_kwargs(argparse.Namespace(
        files = None,
        timeout = None,
        allow_redirects = False,
        follow = False,
        chunked = False,
        offline = False,
    )) == {'timeout': None, 'allow_redirects': False, 'stream': True, 'verify': True}


# Generated at 2022-06-13 21:30:26.760709
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = {"key": "value"}
    headers = make_default_headers(args)
    assert headers["Content-Type"] == "application/x-www-form-urlencoded; charset=utf-8"

    args.json = True
    args.form = False
    args.data = {"key": "value"}
    headers = make_default_headers(args)
    assert headers["Content-Type"] == "application/json"

    args.json = False
    args.form = True
    args.data = {"key": "value"}
    headers = make_default_headers(args)
    assert headers["Content-Type"] == "application/x-www-form-urlencoded; charset=utf-8"

# Generated at 2022-06-13 21:30:28.914842
# Unit test for function finalize_headers
def test_finalize_headers():
    h = RequestHeadersDict()
    h['Content-Type'] = 'multipart/form-data'
    finalize_headers(h)

# Generated at 2022-06-13 21:30:34.894245
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    """
    Unit test for make_send_kwargs
    """
    args = argparse.Namespace(timeout=2,
                              allow_redirects=False)
    assert make_send_kwargs(args) == {'timeout': 2,
                                     'allow_redirects': False}

# Generated at 2022-06-13 21:30:43.168753
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://www.google.com/'
    args.headers = OrderedDict()
    args.headers['Accept'] = 'application/json'
    args.headers['User-Agent'] = 'test'
    args.form = 0
    args.json = 1
    args.data = dict()
    args.data['id'] = 1
    args.data['name'] = 'test'
    args.data['email'] = 'test@test.com'
    args.params = dict()
    args.params['page'] = 1
    args.params['per_page'] = 10
    
    base_headers = RequestHeadersDict()
    base_headers['Host'] = 'www.google.com'

# Generated at 2022-06-13 21:30:51.994674
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import sys
    import traceback
    import tempfile
    import json
    import requests

    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://foo.com'
    args.headers = {'Authorization': 'Basic 123', 'Foo': 'Bar'}

# Generated at 2022-06-13 21:31:04.451222
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.url = 'https://foo.com'
    args.method = 'GET'
    args.json = True
    args.data = {"foo": "bar"}
    args.headers = {"Content-Type": "application/json"}
    args.form = True
    args.files = {}
    args.multipart = None
    args.multipart_data = {}
    args.boundary = None
    args.chunked = False
    args.timeout = None
    args.auth = None
    args.params = {}
    args.verify = True
    args.cert = None
    args.cert_key = None
    args.proxy = [{}]
    data = make_request_kwargs(args)

# Generated at 2022-06-13 21:31:16.074302
# Unit test for function build_requests_session
def test_build_requests_session():
    # Test default case
    requests_session = build_requests_session(verify=True, ssl_version=None, ciphers=None)
    # Test with specify ssl version
    ssl_version = '1.0'
    requests_session = build_requests_session(verify=True, ssl_version=ssl_version, ciphers=None)
    assert requests_session.adapters.get('https://').ssl_version == AVAILABLE_SSL_VERSION_ARG_MAPPING[ssl_version]


# Generated at 2022-06-13 21:31:43.905120
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    # Send kwargs with no proxy
    args = """digoal.me""",
    example_1 = make_send_kwargs(args)

    assert example_1['proxies'] == {}
    assert example_1['stream'] == True
    assert example_1['timeout'] == None
    assert example_1['verify'] == True
    assert example_1['cert'] == None
    assert example_1['allow_redirects'] == False

    # Send kwargs with proxies
    args = """digoal.me""",

    proxy_example = make_send_kwargs(args)

    assert proxy_example['proxies'] == {}
    assert proxy_example['stream'] == True
    assert proxy_example['timeout'] == None
    assert proxy_example['verify'] == True

# Generated at 2022-06-13 21:31:48.673520
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 30
    args.allow_redirects = False
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs == {'timeout': 30, 'allow_redirects': False}


# Generated at 2022-06-13 21:31:54.278759
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': 10, 'allow_redirects': False}


# Generated at 2022-06-13 21:32:00.268350
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(timeout=1, allow_redirects=False)
    assert make_send_kwargs(args) == {'timeout': 1, 'allow_redirects': False}
    args = argparse.Namespace(timeout=1, allow_redirects=True)
    assert make_send_kwargs(args) == {'timeout': 1, 'allow_redirects': False}


# Generated at 2022-06-13 21:32:04.368839
# Unit test for function max_headers
def test_max_headers():
    with max_headers(2) as _:
        try:
            http.client.HTTPConnection('localhost', timeout=1).request('GET', '/')
        except http.client.HTTPException:
            pass


# Generated at 2022-06-13 21:32:09.943068
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    #Test with good input
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False

    kwargs = make_send_kwargs(args)
    assert len(kwargs) == 2
    assert kwargs['timeout'] == 10
    assert kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:32:22.705269
# Unit test for function collect_messages
def test_collect_messages():
    """
    Test to see whether collect_messages returns the correct data type
    :return:
    """
    # test args
    headers = {'Accept': 'application/json', 'Content-Type': 'application/jason'}

# Generated at 2022-06-13 21:32:35.600866
# Unit test for function make_default_headers
def test_make_default_headers():
    old_default_headers = make_default_headers(argparse.Namespace(json=True, form=True, files=False, data='Test'))
    # Change the User-Agent of the Request
    r = RequestHeadersDict({'User-Agent': 'Test'})
    new_default_headers = make_default_headers(argparse.Namespace(json=True, form=True, files=False, data='Test', headers=r))
    assert old_default_headers != new_default_headers
    assert new_default_headers['User-Agent'] == 'Test'


# Generated at 2022-06-13 21:32:37.786723
# Unit test for function build_requests_session
def test_build_requests_session():
    verify = True
    ssl_version = None
    ciphers = None
    build_requests_session(verify, ssl_version, ciphers)

# Generated at 2022-06-13 21:32:50.799510
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args_data = argparse.Namespace() 
    args_data.offline = "0"
    args_data.chunked = ""
    args_data.multipart_data = {}
    args_data.boundary = ""
    args_data.headers = {}
    args_data.chunked = "0"
    args_data.offline = "0"
    args_data.files = []
    args_data.data = [{'name': 'python','id':'0','age':'18','sex':'nan','nation':'China'}]
    args_data.json = "0"
    args_data.form = "1"
    kwargs = make_request_kwargs(args_data)
    print(kwargs)

# Generated at 2022-06-13 21:33:21.647348
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()

    args.json = True
    args.data = False
    args.form = False
    args.files = False

    headers = make_default_headers(args)
    assert headers['User-Agent'] == 'HTTPie/0.9.9'
    assert headers['Accept'] == 'application/json, */*;q=0.5'

    args.json = False
    args.data = True
    args.form = False
    args.files = False

    headers = make_default_headers(args)
    assert headers['Content-Type'] == 'application/json'

    args.json = False
    args.data = True
    args.form = True
    args.files = False

    headers = make_default_headers(args)

# Generated at 2022-06-13 21:33:22.554289
# Unit test for function max_headers
def test_max_headers():
    pass

# Generated at 2022-06-13 21:33:35.630713
# Unit test for function collect_messages
def test_collect_messages():
    # TODO: Use pytest
    import os.path
    import configparser
    import tempfile

    # Construct a fake file to test collect_messages
    config_content = """[httpie-session]
foo-domain-com.auth = Basic c3VwZXItc2VjcmV0

[www.domain.com]
foo-domain-com.auth = Basic c3VwZXItc2VjcmV0
"""
    with open(os.path.join(tempfile.gettempdir(), "httpie-session.ini"), "w") as f:
        f.write(config_content)

    parser = argparse.ArgumentParser(prog="httpie-session")

# Generated at 2022-06-13 21:33:50.360246
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'POST'
    args.url = 'http://learn.com'
    args.headers = {'HOST': 'learn.com', 'Content-Type': 'text/html'}
    args.data = {'ok': 'ok'}
    args.json = True
    # args.files = 
    result = {
        'method': 'post',
        'url': 'http://learn.com',
        'headers': {'User-Agent': DEFAULT_UA, 'HOST': 'learn.com', 'Content-Type': 'text/html', 'Accept': JSON_ACCEPT},
        'data': '{\\"ok\\": \\"ok\\"}',
        'auth': None,
        'params': []
    }
    assert result == make_request_kw

# Generated at 2022-06-13 21:34:00.904014
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[],
        verify='yes',
    )
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['proxies'] == {}, "make_send_kwargs_mergeable_from_env"
    assert kwargs['stream'] == True, "make_send_kwargs_mergeable_from_env"
    assert kwargs['verify'] == True, "make_send_kwargs_mergeable_from_env"
    assert kwargs['cert'] == None, "make_send_kwargs_mergeable_from_env"


# Generated at 2022-06-13 21:34:12.790655
# Unit test for function collect_messages
def test_collect_messages():
    print("Starting test of function collect_messages")
    import os
    import sys

    pwd = os.path.abspath(sys.path[0])
    file_1 = os.path.join(pwd, "httpie\\tests\\data\\sample_http")
    file_2 = os.path.join(pwd, "httpie\\tests\\data\\random_http")
    f1 = open(file_1,'r')
    f2 = open(file_2,'r')

    headers = {}
    headers['Connection'] = 'close'
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'

# Generated at 2022-06-13 21:34:23.186167
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import requests
    args = argparse.Namespace()
    args.data = {"test": "test"}
    args.json = True
    args.form = False
    args.url = "http://test.com"
    args.method = "GET"
    args.headers = {'header1': 'header1'}
    args.cert = "fake"
    args.auth = "fake"
    args.params = {"param1": "param1"}

    result = make_request_kwargs(args)
    request = requests.Request(**result)
    request.prepare()
    assert (request.url == "http://test.com")
    assert (request.method == "GET")
    assert (request.headers['header1'] == "header1")

# Generated at 2022-06-13 21:34:25.872937
# Unit test for function max_headers
def test_max_headers():
    def foo():
        pass
    with max_headers(1):
        foo()

# Generated at 2022-06-13 21:34:36.127106
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import os
    import tempfile
    import urllib3

    # input
    httpie_host = "www.google.com"
    args = argparse.Namespace()
    args.proxy = []
    args.timeout = None
    args.verify = True
    args.cert = None
    args.cert_key = None

    # expected
    expected_kwargs = {
        'proxies': {p.key: p.value for p in args.proxy},
        'stream': True,
        'verify': {
            'yes': True,
            'true': True,
            'no': False,
            'false': False,
        }.get(args.verify.lower(), args.verify),
        'cert': args.cert,
    }

    # function
    kwargs = make_

# Generated at 2022-06-13 21:34:46.253977
# Unit test for function collect_messages
def test_collect_messages():
    import unittest
    import httpie
    class TestCollectMessages(unittest.TestCase):
        def test_collect_messages(self):
            # TODO: write test in the near future
            #self.assertEqual(httpie.collect_messages(["--config-dir",
            #                                          ".httpie/configs/sessions/", "--session=jiraxu", 
            #                                          "-m", "GET", "--headers", "Content-Type: application/json",
            #                                          "https://api.github.com/user/repos", "--timeout", "60"],
            #                                          "httpie/configs/sessions/jiraxu.json"), "NULL")
            self.assertEqual("NULL", "NULL")

    unittest.main()

# Generated at 2022-06-13 21:35:33.081592
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    print(
        make_send_kwargs_mergeable_from_env(
            argparse.Namespace(
                verify='yes',
                cert='tests/data/certs/client.crt',
                cert_key=None,
            )
        )
    )

# Generated at 2022-06-13 21:35:39.132205
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    class Arguments:
        def __init__(self):
            self.proxy = []
            self.verify = 'yes'
            self.cert = ''
            self.cert_key = ''
    args = Arguments()
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert isinstance(kwargs, dict)
    assert kwargs['proxies'] == {}
    assert kwargs['stream'] == True
    assert kwargs['verify'] == True
    assert kwargs['cert'] == None



# Generated at 2022-06-13 21:35:44.079263
# Unit test for function max_headers
def test_max_headers():
    import http.client
    with max_headers(10):
        assert http.client._MAXHEADERS == 10

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # test_max_headers()

# Generated at 2022-06-13 21:35:52.639535
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    assert make_send_kwargs(args=argparse.Namespace(timeout=None)) == {'timeout': None, 'allow_redirects': False}
    assert make_send_kwargs(args=argparse.Namespace(timeout=None, allow_redirects=True)) == {'timeout': None, 'allow_redirects': True}
    assert make_send_kwargs(args=argparse.Namespace(timeout=10.0)) == {'timeout': 10.0, 'allow_redirects': False}
    assert make_send_kwargs(args=argparse.Namespace(timeout=10.0, allow_redirects=True)) == {'timeout': 10.0, 'allow_redirects': True}


# Generated at 2022-06-13 21:36:03.453734
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    data = "{'foo':'bar'}"
    args.data = data
    args.url = "http://localhost"
    args.method = "POST"
    args.headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Content-Type': "application/json",
        'HTTP2': "test"})
    args.json = None
    args.form = None
    args.files = None
    args.multipart = None
    args.auth = None
    args.params = {'foo':'bar'}
    args.cert = None
    args.cert_key = None
    args.verify = None
    args.timeout = 3
    args.offline = False
    args.chunked = True

# Generated at 2022-06-13 21:36:15.314136
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.data = {'foo': 'bar'}
    args.json = True
    args.headers = {'Accept': 'application/json'}
    base_headers = {'Content-Type': 'application/json'}
    request_body_read_callback = lambda chunk: chunk
    actual = make_request_kwargs(
        args=args,
        base_headers=base_headers,
        request_body_read_callback=request_body_read_callback
    )

# Generated at 2022-06-13 21:36:18.215189
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli.parser import parser
    args = parser.parse_args(['-v', 'GET', 'https://httpbin.org/get'])
    res = collect_messages(args, Path('.'))
    for i in res:
        print(i)



# Generated at 2022-06-13 21:36:20.514668
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS is None
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS is None

# Generated at 2022-06-13 21:36:32.467992
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    """
    Tests that the function make_request_kwargs returns a dictionary with the correct keys
    """


# Generated at 2022-06-13 21:36:34.611563
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = None
    ans = make_default_headers(args)
    print(ans)


# Generated at 2022-06-13 21:38:56.637209
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    from httpie import parse_args, DocoptExit
    from httpie.compat import str

    args = parse_args([
        '-H', 'Accept: application/json',
        '-H', 'Content-Type: application/json',
        '-d', '{"foo": "bar"}',
        'https://test.test'
    ])
    kwargs = make_request_kwargs(args)
    assert kwargs['url'] == 'https://test.test'
    assert kwargs['method'] == 'get'
    assert kwargs['headers']['Accept'] == 'application/json'
    assert kwargs['headers']['Content-Type'] == 'application/json'
    assert kwargs['data'] == b'{"foo": "bar"}'

    # Test if data is serialized
   

# Generated at 2022-06-13 21:39:00.464798
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    assert make_send_kwargs(argparse.Namespace(
        timeout='1',
    )) == {'timeout': 1, 'allow_redirects': False}


# Generated at 2022-06-13 21:39:12.299477
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'get'
    args.headers = RequestHeadersDict()
    args.auth = None
    args.params = {'foo': 'bar'}
    args.url = 'www.google.com'
    args.json = True
    args.offline = False
    args.chunked = False
    args.data = '{"foo": "bar"}'
    args.form = None
    args.files = False
    args.multipart_data = []
    args.boundary = None
    args.verify = 'yes'
    args.cert = None
    args.cert_key = None
    args.proxy = None
    args.timeout = None
    args.max_headers = None


# Generated at 2022-06-13 21:39:15.582092
# Unit test for function build_requests_session
def test_build_requests_session():
    verify = 'ok'
    ssl_version = 'ok'
    ciphers = 'ok'
    assert build_requests_session(verify, ssl_version, ciphers)


# Generated at 2022-06-13 21:39:19.411580
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(
        data = None,
        form =  False,
        json = False,
    )
    args.headers = {'test': 'test'}
    headers = make_default_headers(args)
    assert(headers['test'] == 'test')
    assert(headers['User-Agent'] == 'HTTPie/2.1.0')


# Generated at 2022-06-13 21:39:29.984520
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = ['http://proxyserver.com:80']
    args.verify = 'somewhere/cert.pem'
    args.cert = 'somewhere/cert.pem'
    args.cert_key = 'somewhere/cert.pem'
    expected = {
        'proxies': {'http://proxyserver.com:80': ''},
        'stream': True,
        'verify': 'somewhere/cert.pem',
        'cert': ('somewhere/cert.pem', 'somewhere/cert.pem')
    }
    actual = make_send_kwargs_mergeable_from_env(args)
    assert expected == actual

# Generated at 2022-06-13 21:39:37.099250
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = '''
    {
        "data": {
            "spam": "eggs"
        },
        "headers": {},
        "method": "POST",
        "url": "http://httpbin.org/post"
    }
    '''
    args = json.loads(args)
    kwargs = make_request_kwargs(args)
    print(repr(kwargs))


# Generated at 2022-06-13 21:39:42.670728
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    filename = sys.modules[__name__].__file__
    args = argparse.Namespace()
    with open(filename,'r') as f:
        args.data = {'data': f.read()}

    make_request_kwargs(args=args)
    pass

if __name__ == "__main__":
    test_make_request_kwargs()