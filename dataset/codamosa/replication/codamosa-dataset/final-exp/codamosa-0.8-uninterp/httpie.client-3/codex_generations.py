

# Generated at 2022-06-13 21:30:21.960964
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    #from httpie.cli.parser import parse_args
    args=['httpie','--timeout','10','--allow-redirect','false','http://fake']
    args= parse_args(args)
    kwargs = {
        'timeout': 10 or None,
        'allow_redirects': False,
    }

    assert make_send_kwargs(args) == kwargs


# Generated at 2022-06-13 21:30:32.076865
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    import collections
    import json
    import os
    import sys
    # Add parent directory to path so we can import httpie
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import httpie

    RequestKwargs = collections.namedtuple(
        'RequestKwargs', ['args', 'expected_result'])

# Generated at 2022-06-13 21:30:35.283758
# Unit test for function make_default_headers
def test_make_default_headers():
    args = check_args_for_test()
    print(make_default_headers(args))


# Generated at 2022-06-13 21:30:38.937351
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.ArgumentParser()
    config_dir = Path()
    request_body_read_callback = Callable[[bytes], None]
    print(collect_messages(args, config_dir, request_body_read_callback))

# Generated at 2022-06-13 21:30:44.143253
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = []
    args.verify = 'yes'
    args.cert = None
    args.cert_key = None
    kwargs_mergeable = make_send_kwargs_mergeable_from_env(args)
    assert kwargs_mergeable['verify'] is True

# Generated at 2022-06-13 21:30:52.533170
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # parse arguments
    args = argparse.Namespace()
    # default arguments
    args.verify = True
    args.cert = None
    args.cert_key = None
    args.proxy = None
    # test with default arguments
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['verify'] == True
    assert kwargs['cert'] == None
    assert kwargs['proxies'] == {}
    # Test with custom arguments
    args.verify = False
    args.cert = 'my_cert'
    args.proxy = ProxyArg(key='http', value='http://my_proxy')
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs['verify'] == False


# Generated at 2022-06-13 21:31:04.015767
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:31:14.961798
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.url = 'http://foo.com'
    args.form = False
    args.json = False
    args.data = {}
    args.files = {}
    args.headers = {}
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers
    assert 'Content-Type' not in headers

# Generated at 2022-06-13 21:31:22.464871
# Unit test for function collect_messages

# Generated at 2022-06-13 21:31:27.172296
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path()
    request_body_read_callback = lambda chunk: chunk

    assert collect_messages(args, config_dir, request_body_read_callback)


# Generated at 2022-06-13 21:31:48.108134
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:31:50.560586
# Unit test for function max_headers
def test_max_headers():
    with max_headers(limit=10):
        assert http.client._MAXHEADERS == 10

# Generated at 2022-06-13 21:31:56.759284
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
	kwargs = make_send_kwargs(args=argparse.Namespace(
		timeout=None,
		allow_redirects=False,
		arg_str=''
	))
	assert kwargs == {
		'timeout': None,
		'allow_redirects': False,
	}


# Generated at 2022-06-13 21:31:58.553873
# Unit test for function max_headers
def test_max_headers():
    # TODO: unit test for max_headers
    pass



# Generated at 2022-06-13 21:32:03.660878
# Unit test for function max_headers
def test_max_headers():
    assert(http.client._MAXHEADERS == 100)
    with max_headers(10):
        assert(http.client._MAXHEADERS == 10)
    assert(http.client._MAXHEADERS == 100)

# Generated at 2022-06-13 21:32:08.193606
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.files = []
    args.json = False
    args.headers = RequestHeadersDict()

    default_headers = make_default_headers(args)

    assert default_headers == RequestHeadersDict(
        {'User-Agent': DEFAULT_UA})



# Generated at 2022-06-13 21:32:09.608508
# Unit test for function make_default_headers
def test_make_default_headers():
    return make_default_headers("UA")
    

# Generated at 2022-06-13 21:32:22.458820
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', default='GET')
    parser.add_argument('--params', default={})
    parser.add_argument('--headers', default={})
    parser.add_argument('--auth')
    parser.add_argument('--data')
    parser.add_argument('--json')
    parser.add_argument('--form')
    parser.add_argument('--files')
    parser.add_argument('--chunked')
    parser.add_argument('--offline')
    args, _ = parser.parse_known_args()
    result = make_request_kwargs(args)

# Generated at 2022-06-13 21:32:34.256848
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = {'This':'That'}
    result = make_default_headers(args)
    assert sorted(result.items()) == [('Accept', 'application/json, */*;q=0.5'), ('Content-Type', 'application/json'), ('User-Agent', 'HTTPie/0.9.9')]


# Generated at 2022-06-13 21:32:44.090680
# Unit test for function max_headers
def test_max_headers():
    import http.client
    import httpie.context

    max_header = {'Test-Header': ['a', 'b', 'c']}

    with httpie.context.max_headers(len(max_header)):
        assert http.client._MAXHEADERS == len(max_header)
    assert http.client._MAXHEADERS == 100

    with httpie.context.max_headers(len(max_header) + 1):
        assert http.client._MAXHEADERS == len(max_header) + 1
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:33:05.812759
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Test for TypeError on input url with less than 5 parts
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://www.google.com'
    args.headers = RequestHeadersDict({})
    args.auth = None
    args.params = {}
    
    try:
        make_request_kwargs(args)
    except TypeError:
        pass
    else:
        assert False

    # Test for TypeError on passing data with invalid type
    args.data = ()
    try:
        make_request_kwargs(args)
    except TypeError:
        pass
    else:
        assert False
    args.data = None

    # Test for ValueError on passing auth with invalid type
    args.auth = ()

# Generated at 2022-06-13 21:33:17.362216
# Unit test for function max_headers
def test_max_headers():
    # noinspection PyProtectedMember
    orig = http.client._MAXHEADERS
    limit = 100
    try:
        with max_headers(limit):
            assert http.client._MAXHEADERS == limit
    finally:
        http.client._MAXHEADERS = orig
    assert http.client._MAXHEADERS == orig

if __name__ == '__main__':
    import argparse
    import httpie.cli

    parser = argparse.ArgumentParser()
    httpie.cli.parser.add_argument = parser.add_argument
    httpie.cli.parser.add_argument('--url', default='https://www.example.com/')
    httpie.cli.parser.add_argument('--max-headers', type=int, default=100)
    args = httpie.cli.parser.parse_args()


# Generated at 2022-06-13 21:33:31.363950
# Unit test for function collect_messages
def test_collect_messages():
    class Args:
        cert=None
        cert_key=None
        verify=True
        auth=None
        auth_plugin=None
        data=None
        files=None
        form=False
        headers=RequestHeadersDict()
        json=False
        params={}
        method='GET'
        url='http://localhost/'
        offline=False
        chunked=False
        all=False
        follow=False
        max_redirects=0
        max_headers=None
        config_dir=Path()
        path_as_is=False
        compress=None
        session=None
        session_read_only=None
        debug=False

    class Response:
        def __init__(self):
            self.next = None

    a = Args()

# Generated at 2022-06-13 21:33:37.131676
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout=None,
        allow_redirects=False
    )
    send_kwargs = make_send_kwargs(args)
    assert send_kwargs.items() == dict(timeout=None, allow_redirects=False).items(), "test_make_send_kwargs failed"


# Generated at 2022-06-13 21:33:50.181596
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(
        verify=True,
        ssl_version='TLSv1',
        ciphers='ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AES:RSA+3DES:!ADH:!AECDH:!MD5'
    )
    print(requests_session)
    print(requests_session.mounts)
    print(requests_session.adapters)


if __name__ == '__main__':
    test_build_requests_session()

# Generated at 2022-06-13 21:33:59.562361
# Unit test for function make_default_headers
def test_make_default_headers():
    # get the function we want to test
    target_function = make_default_headers
    args = []
    args.append(argparse.Namespace(data=None, files=None, auth=None,
                                   json=None, form=None,
                                   data={"foo": "bar"}, json=True,
                                   headers={'Content-Type': 'text/plain'}))
    # call our function
    results = target_function(*args)
    assert results == {"User-Agent": "HTTPie/XX",
                       "Accept": "application/json, */*;q=0.5"}

# Generated at 2022-06-13 21:34:12.210170
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(), argparse.Namespace()]
    args.proxy[0].key = "key1"
    args.proxy[1].key = "key2"
    args.proxy[0].value = "value1"
    args.proxy[1].value = "value2"
    args.verify = "1"
    args.cert = "cert"
    args.cert_key = "cert_key"
    args_proxy = []
    for arg in args.proxy:
        args_proxy.append(vars(arg))

# Generated at 2022-06-13 21:34:22.774460
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout=10,
        follow='yes',
        verify='no',
        cert='/path/to/cert',
        cert_key='/path/to/cert/key',
        proxy=[
            argparse.Namespace(key='foo', value='bar'),
            argparse.Namespace(key='baz', value='qux'),
        ]
    )

    assert make_send_kwargs(args) == {
        'timeout': 10,
        'allow_redirects': False,
    }, 'send_kwargs has wrong keys or values'


# Generated at 2022-06-13 21:34:33.370138
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-verify', action='store_false', dest='verify', default=True)
    parser.add_argument('--verify', action='store_true', dest='verify', default=True)
    parser.add_argument('--verify')
    parser.add_argument('--proxy')
    parser.add_argument('--cert')
    parser.add_argument('--cert-key')
    args = parser.parse_args('--no-verify --verify /path/to/ca_file.pem --proxy http://localhost:3128 --cert /path/to/client.crt --cert-key /path/to/client.key'.split())

    print(make_send_kwargs_mergeable_from_env(args))
   

# Generated at 2022-06-13 21:34:39.112287
# Unit test for function max_headers
def test_max_headers():
    try:
        with max_headers(limit=2):
            assert http.client._MAXHEADERS == 2
    finally:
        assert http.client._MAXHEADERS == 100

    try:
        with max_headers(_hush_pyflakes=None):
            pass
    except TypeError:
        pass

# Generated at 2022-06-13 21:35:13.553674
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:35:25.296877
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:35:36.297861
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'http://127.0.0.1:8080'
    args.data = None
    args.form = False
    args.json = False
    args.headers = RequestHeadersDict()
    args.auth = None
    args.params = {}
    args.follow = False
    args.max_redirects = None
    args.timeout = None
    args.max_headers = None
    args.compress = False
    args.chunked = False
    args.offline = False
    args.verify = True
    args.cert = None
    args.ssl_version = None
    args.ciphers = None
    args.proxy = None
    args.files = None
    args.debug = False


# Generated at 2022-06-13 21:35:37.113842
# Unit test for function max_headers
def test_max_headers():
     # always succeed
    assert(max_headers(5) is not None)

# Generated at 2022-06-13 21:35:39.493447
# Unit test for function max_headers
def test_max_headers():
    import http.client as http_client
    temp_maxheaders = http_client._MAXHEADERS
    http_client._MAXHEADERS = 10
    assert (max_headers(5) is None)
    http_client._MAXHEADERS = temp_maxheaders

# Generated at 2022-06-13 21:35:51.205700
# Unit test for function collect_messages
def test_collect_messages():
    parser = argparse.ArgumentParser()
    args = parser.parse_args([])
    config_dir = Path()
    request_body_read_callback = lambda chunk: chunk
    messages = collect_messages(args, config_dir, request_body_read_callback)
    kwargs = make_request_kwargs(args)
    send_kwargs = make_send_kwargs(args)
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    requests_session = build_requests_session(bool(send_kwargs_mergeable_from_env['verify']))
    request = requests.Request(**kwargs)
    prepared_request = requests_session.prepare_request(request)

# Generated at 2022-06-13 21:35:55.452678
# Unit test for function collect_messages
def test_collect_messages():
    from argparse import Namespace
    from httpie.cli.dicts import RequestHeadersDict
    from pathlib import Path
    args = Namespace()
    config_dir = Path()
    args.url = 'localhost'

    args.headers = RequestHeadersDict()
    args.headers['User-Agent'] = DEFAULT_UA

    kwargs = make_request_kwargs(args)
    response = collect_messages(args, config_dir)
    next(response)
    next(response)

# Generated at 2022-06-13 21:36:02.449590
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = {
        'proxy': [],
        'verify': 'yes',
        'cert': None,
    }
    make_send_kwargs_mergeable_from_env(args)
    # noinspection SpellCheckingInspection
    expected_result = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None
    }

    assert(make_send_kwargs_mergeable_from_env(args) == expected_result)



# Generated at 2022-06-13 21:36:11.885460
# Unit test for function max_headers
def test_max_headers():
    # create a new http object
    c = http.client.HTTPConnection('localhost')
    # create a new max_headers object and limit it to 1
    with max_headers(1):
        # add headers and check the output is a list and that the length is 1
        c.putrequest('GET', '/', skip_accept_encoding=True)
        assert isinstance(list(c.putheader('test', '1')), list)
        assert len(list(c.putheader('test', '1'))) == 1
    # return back to normal
    c.close()

# Generated at 2022-06-13 21:36:26.613131
# Unit test for function make_default_headers
def test_make_default_headers():
    # print(make_default_headers({'headers': None}))
    print(make_default_headers({'headers': {'Accept': 'application/json'}}))
    print(make_default_headers({'headers': {'Accept': 'application/json', 'Content-Type': 'applicatipon/json'}, 'form':True, 'files':True}))
    print(make_default_headers({'headers': {'Accept': 'application/json', 'Content-Type': 'applicatipon/json'}, 'form':True, 'files':False}))

if __name__ == '__main__':
    test_make_default_headers()

# Generated at 2022-06-13 21:37:27.687411
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace(verify=True, cert="https://foo.com", cert_key="https://foo.com/key.pem")
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == {'proxies': {}, 'stream': True, 'verify': True, 'cert': ('https://foo.com', 'https://foo.com/key.pem')}

# Generated at 2022-06-13 21:37:36.514924
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(auth='admin', auth_type='basic', chunked=1,
                              cert='/tmp/cert.pem', cert_key='/tmp/key.pem',
                              data='', files=[], form=0, headers={}, json=0,
                              max_headers='', method='GET',
                              multipart_data=[], params={},
                              path_as_is=0, proxy=[],
                              timeout='', url='', verify='', ssl_version='', ciphers='')
    make_send_kwargs(args)


# Generated at 2022-06-13 21:37:41.976917
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = {
        'verify': 'no'
    }
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env['verify'] == 'no'

# Generated at 2022-06-13 21:37:51.470811
# Unit test for function make_default_headers

# Generated at 2022-06-13 21:37:56.225698
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    kwargs = make_send_kwargs(args=args)
    assert kwargs['timeout'] == args.timeout
    assert kwargs['allow_redirects'] == False


# Generated at 2022-06-13 21:37:59.238979
# Unit test for function max_headers
def test_max_headers():
    with max_headers(100):
        assert http.client._MAXHEADERS == 100
    # noinspection PyUnresolvedReferences
    assert http.client._MAXHEADERS != 100

# Generated at 2022-06-13 21:38:02.260221
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = None
    assert make_send_kwargs(args) == {'timeout': None, 'allow_redirects': False}


# Generated at 2022-06-13 21:38:05.550348
# Unit test for function max_headers
def test_max_headers():
    args = argparse.Namespace(max_headers = 200)
    with max_headers(args.max_headers):
        assert http.client._MAXHEADERS == 200

# Generated at 2022-06-13 21:38:17.580667
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = "POST"
    args.url = "http://httpbie.org"
    args.headers = {'Content-Type': 'application/json'}
    args.data = {}
    args.auth = "mohamed"
    args.params = {'name': 'mohamed'}
    args.json = True
    args.form = False

    args.session = None
    args.session_read_only = None
    args.compress = True
    args.path_as_is = False
    args.debug = False
    args.offline = False
    args.chunked = True
    args.timeout = None
    args.verify = True
    args.verify = True
    args.verify = True

    args.headers = RequestHeaders

# Generated at 2022-06-13 21:38:30.216321
# Unit test for function make_default_headers
def test_make_default_headers():
    from io import StringIO
    from _pytest.monkeypatch import MonkeyPatch
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(sys, "stdin", StringIO('myinput'))

    from httpie.cli import parser

    args = parser.parse_args(['-f', 'http://www.google.com'])
    default_headers = make_default_headers(args)
    print(default_headers)
    print(args.headers)
    print(finalize_headers(args.headers))
    print(make_request_kwargs(args)[headers])
    monkeypatch.undo()
    return True
