

# Generated at 2022-06-13 21:30:30.712615
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(files=None, method='GET', form=False)
    assert make_default_headers(args) == {'User-Agent': 'HTTPie/' + __version__}

    args = argparse.Namespace(files=None, method='GET', form=True)
    assert make_default_headers(args) == {
        'User-Agent': 'HTTPie/' + __version__,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}

    args = argparse.Namespace(files=None, method='GET', form=False, json=True)

# Generated at 2022-06-13 21:30:37.564332
# Unit test for function make_default_headers
def test_make_default_headers():
    # Arrange
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.data = {}
    default_headers = RequestHeadersDict({
        'User-Agent': 'HTTPie/0.9.9'
    })

    # Act
    actual = make_default_headers(args)

    # Assert

    assert(actual == default_headers)

# Generated at 2022-06-13 21:30:48.275976
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = parse_args(['-H', 'foo:bar', '-d', '{"name": "alex"}', 'http://httpbin.org/post'])
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'post'
    assert request_kwargs['url'] == 'http://httpbin.org/post'
    assert request_kwargs['headers']['User-Agent'] == DEFAULT_UA
    assert request_kwargs['headers']['foo'] == 'bar'
    assert request_kwargs['headers']['Content-Type'] == JSON_CONTENT_TYPE
    assert request_kwargs['data'] == b'{"name": "alex"}'
    assert request_kwargs['auth'] is None
    assert request_kwargs['params'] == []


# Generated at 2022-06-13 21:30:54.276712
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    proxy_auth = 'username:password'
    args = {'verify': 'false', 'cert': 'foo.pem', 'cert_key': 'bar.pem', 'proxy': [proxy_auth]}
    r = make_send_kwargs_mergeable_from_env(args)
    assert len(r['verify']) == 1
    assert r['verify'] == False
    assert len(r['cert']) == 2
    assert r['cert'][0] == 'foo.pem'
    assert r['cert'][1] == 'bar.pem'
    assert len(r['proxies']) == 1
    assert list(r['proxies'].values())[0] == proxy_auth

# Generated at 2022-06-13 21:31:05.065741
# Unit test for function make_default_headers
def test_make_default_headers():
    class Args:
        def __init__(self):
            self.json = False
            self.form = False
            self.files = False
            self.data = "test_data"
        def __contains__(self, item):
            if item == 'Content-Type':
                return True
            return False
        def get(self, item):
            if item == 'Content-Type':
                return 'the_content_type'

    args = Args()
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({
        'User-Agent': DEFAULT_UA
    })

    args = Args()
    args.json = True
    headers = make_default_headers(args)

# Generated at 2022-06-13 21:31:18.809004
# Unit test for function make_send_kwargs

# Generated at 2022-06-13 21:31:31.107690
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli.parser import parser
    from httpie.cli import env, get_response
    # from httpie.request import Request
    for args in [parser.parse_args([
        '-v', '--all', 'GET', 'https://www.google.com/'
    ]), parser.parse_args([
        '-v', 'GET', 'https://www.google.com/'
    ]), parser.parse_args([
        '-v', 'POST', 'https://www.google.com/'
    ])]:
        print(args)

        def rbc(chunk):
            pass

        responses = []

# Generated at 2022-06-13 21:31:39.412728
# Unit test for function max_headers
def test_max_headers():
    # very simple max_headers test, we're testing limit and orig values
    # here.
    with max_headers(3):
        assert http.client._MAXHEADERS == 3
        assert http.client._MAXHEADERS == 3 # for get_expired_cookies()

    assert http.client._MAXHEADERS != 3

# Generated at 2022-06-13 21:31:48.081173
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert kwargs_mergeable_from_env == correct_kwargs_mergeable_from_env


# Generated at 2022-06-13 21:31:58.553821
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args_namespace = argparse.Namespace()
    args_namespace.timeout = 1
    args_namespace.allow_redirects = False
    args_namespace.proxies = {'http': 'foo'}
    args_namespace.stream = True
    args_namespace.verify = 'no'
    args_namespace.cert = 'foo'
    send_kwargs = make_send_kwargs(args_namespace)

    assert send_kwargs == {'timeout': 1, 'allow_redirects': False}

# Generated at 2022-06-13 21:32:20.462463
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path()
    request_body_read_callback = lambda chunk: chunk
    for item in collect_messages(args, config_dir, request_body_read_callback):
        print(item)

# Generated at 2022-06-13 21:32:27.607471
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()  # https://github.com/httpie/httpie/blob/master/httpie/cli.py#L102
    args.auth = None
    args.auth_type = 'basic' # TODO
    args.timeout = 10000
    args.verify = False
    args.cert = None
    args.chunked = False
    args.download = False
    args.output = '.'
    args.max_redirects = None
    args.max_headers = 0
    args.compress = None
    args.compress_level = None
    args.proxy = ''
    args.session = None
    args.session_read_only = None
    args.headers = {}
    args.method = 'GET'
    args.url = 'http://example.com'
    args

# Generated at 2022-06-13 21:32:35.211813
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = None
    args.allow_redirects = False
   
    # Tuple of input and expected
    dict_in = (
        (args.timeout,args.allow_redirects),
        {'timeout': None, 'allow_redirects': False},
    )
    assert make_send_kwargs(args) == dict_in[1]

# Generated at 2022-06-13 21:32:40.059168
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    parser = argparse.ArgumentParser()
    httpie.cli.argparser.add_arguments(parser)
    args = parser.parse_args()

    kwargs = {
        'method': args.method.lower(),
        'url': args.url,
        'headers': args.headers,
        'data': None,
        'auth': args.auth,
        'params': args.params.items(),
    }

    print(kwargs)

# Generated at 2022-06-13 21:32:42.176799
# Unit test for function build_requests_session
def test_build_requests_session():
    try:
        build_requests_session(
            verify=False,
            ssl_version="default",
            ciphers=None
        )
        assert False
    except KeyError:
        assert True

# Generated at 2022-06-13 21:32:55.765752
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Generic test
    args = argparse.Namespace(method='get', url='http://fortest.com')
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'get'
    assert request_kwargs['url'] == 'http://fortest.com'

    # Test with --json
    args = argparse.Namespace(method='post', url='http://fortest.com', json=True, data={"test": "json"})
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'post'
    assert request_kwargs['url'] == 'http://fortest.com'
    assert request_kwargs['data'] == '{"test": "json"}'

# Generated at 2022-06-13 21:33:05.026447
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 5
    args.allow_redirects = False
    args.stream = True
    args.verify = 'True'
    args.cert = 'cert.pem'
    args.cert_key =  'cert_key.pem'
    args.proxies = {'http':'http://127.0.0.1:8080/'}
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] == 5
    assert kwargs['allow_redirects'] is False
    assert kwargs['stream'] is True
    assert kwargs['verify'] is True
    assert kwargs['cert'] == 'cert.pem'

# Generated at 2022-06-13 21:33:16.574781
# Unit test for function collect_messages
def test_collect_messages():
    from argparse import Namespace
    from httpie.cli.helpers import make_parser
    from httpie.config import Config

    httpie_session = 'test'
    parser = make_parser()
    args = parser.parse_args([
        '-v',
        '--session-read-only=123',
        '--session=%s' % httpie_session,
        '--headers',
        'A: 123',
        '--headers',
        'A: 456',
        '--follow',
        '--max-redirects=10',
        '--max-headers=1',
        'GET',
        'https://www.example.com/'
    ])
    config = Config(use_colors=False)
    config_dir = config.config_dir
    args.config_dir = config

# Generated at 2022-06-13 21:33:21.375959
# Unit test for function collect_messages
def test_collect_messages():
    from tempfile import mkdtemp
    import httpie.cli.parser as cli_parser

    config_dir = Path(mkdtemp())
    args = cli_parser.parse_args(['http://httpbin.org/get'])
    for message in collect_messages(args=args, config_dir=config_dir):
        assert isinstance(message, requests.PreparedRequest) or \
            isinstance(message, requests.Response)

# Generated at 2022-06-13 21:33:35.126256
# Unit test for function collect_messages
def test_collect_messages():
    class argparse:
        class Namespace:
            def __init__(self, session_name=None, session_read_only=None, headers=None, url=None, debug=None,
                         offline=None, compress=None, compress_level=None, path_as_is=None, max_redirects=None,
                         follow=None, all=None, method=None, params=None, json=None, data=None, form=None, files=None,
                         auth=None, auth_plugin=None, timeout=None, max_headers=None, verify=None, cert=None,
                         cert_key=None, chunked=None, ssl_version=None, ciphers=None, multipart=None,
                         multipart_data=None, boundary=None):
                self.session_name = session_name
               

# Generated at 2022-06-13 21:34:48.798885
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(
                verify=False,
                ssl_version="",
                ciphers=None)
    assert bool(requests_session)


# Generated at 2022-06-13 21:34:58.584015
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.json = True
    args.url = 'http://localhost:4000/api/v1/test_json'
    args.method = 'POST'
    args.data = {'name':'dummy','age':20}
    args.auth = ('admin', 'password')
    args.headers = {'Content-Type':'application/json'}

    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'post'
    assert request_kwargs['url'] == 'http://localhost:4000/api/v1/test_json'
    assert request_kwargs['data'].decode('utf-8') == '{\n    "name": "dummy",\n    "age": 20\n}\n'
    assert request_

# Generated at 2022-06-13 21:35:10.663032
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import os

    try:
        os.environ['http_proxy']
        os.environ['https_proxy']
        os.environ['no_proxy']
    except KeyError:
        sys.stderr.write(
            '\n\n'
            'I need HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables '
            'set in order to run make_send_kwargs_mergeable_from_env test.\n\n'
        )
        sys.exit(1)

    args = argparse.Namespace()
    args.proxy = None
    args.verify = 'yes'


# Generated at 2022-06-13 21:35:11.006653
# Unit test for function collect_messages
def test_collect_messages():
    collect_messages()

# Generated at 2022-06-13 21:35:18.720561
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.proxy = []
    args.timeout = 40
    args.verify = 'True'
    expected_kwargs = {'proxies': {},
                       'stream': True,
                       'verify': True,
                       'timeout': 40,
                       'cert': None,
                       'allow_redirects': False}
    result_kwargs = make_send_kwargs_mergeable_from_env(args)
    assert expected_kwargs == result_kwargs


# Generated at 2022-06-13 21:35:23.116180
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args=["-X", "GET", "www.csuohio.edu"]
    assert make_request_kwargs(args) == ['GET', 'www.csuohio.edu']

# Generated at 2022-06-13 21:35:35.234343
# Unit test for function max_headers
def test_max_headers():
    # set max_headers to 2, setup two headers to test
    http.client._MAXHEADERS = 2
    headers = {'test': 'test', 'test2': 'test2'}
    orig_headers = headers.copy()
    # test if it changes
    for name, value in headers.items():
        if value is not None:
            # “leading or trailing LWS MAY be removed without
            # changing the semantics of the field value”
            # <https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html>
            # Also, requests raises `InvalidHeader` for leading spaces.
            value = value.strip()

# Generated at 2022-06-13 21:35:44.021722
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import pytest
    from httpie.cli import parser
    from httpie.plugins.builtin import HTTPBasicAuth
    args = parser.parse_args([
        '--verify=no',
        '--cert=./tests/fixtures/client.crt',
        '--cert-key=./tests/fixtures/client.key',
        '--proxy=http://proxy:443',
        '--proxy=https://proxy2:443'
    ])
    args.auth_plugin = HTTPBasicAuth()
    args.auth_plugin.raw_auth = 'username:password'
    args.json = True

    parsed_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)

# Generated at 2022-06-13 21:35:47.290679
# Unit test for function max_headers
def test_max_headers():
    with max_headers(2):
        assert http.client._MAXHEADERS == 2
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:35:51.637866
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = "~/.config/httpie"
    request_body_read_callback = lambda chunk: chunk

# Generated at 2022-06-13 21:37:17.264339
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = None
    args.allow_redirects = False
  
    kwargs = {
        'timeout': args.timeout or None,
        'allow_redirects': False,
    }

    if args.timeout != None:
        assert kwargs.get('timeout') == args.timeout
    if not args.allow_redirects:
        assert kwargs.get('allow_redirects') == False


# Generated at 2022-06-13 21:37:28.116935
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = None
    args.files = None
    args.form = None
    args.data = None

    headers = make_default_headers(args)
    assert len(headers) == 1
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers

    args.json = True
    headers = make_default_headers(args)
    assert len(headers) == 2
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert 'Content-Type' not in headers

    args.data = {'key': 'value'}
    headers = make_default_headers(args)
    assert len(headers) == 2
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers

# Generated at 2022-06-13 21:37:38.824229
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # usage: 
    # python -m unittest test_make_request_kwargs
    import unittest

    class TestMakeRequestKwargs(unittest.TestCase):
        def test_make_request_kwargs(self):
            from collections import OrderedDict
            from httpie import input
            from httpie.cli.argtypes import KeyValue
            from httpie.cli import parser


# Generated at 2022-06-13 21:37:42.835394
# Unit test for function max_headers
def test_max_headers():
    # noinspection PyProtectedMember
    http.client._MAXHEADERS = 120
    with max_headers(10) as _:
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == 120


# Generated at 2022-06-13 21:37:51.948433
# Unit test for function collect_messages
def test_collect_messages():
    import io
    import unittest
    from py._xmlgen import html as html_module
    from httpie.context import Environment
    from httpie.output.streams import Streams
    from httpie.cli.parser import get_parser
    from httpie import ExitStatus
    from httpie.utils import get_fileno
    from httpie.config import Config
    from pathlib import Path
    import socket
    import pytest
    from pytest import fixture
    from httpie.plugins.builtin import HTTPBasicAuth


    class TestCollectMessages(unittest.TestCase):

        def setUp(self):
            self.parser = get_parser()
            args = self.parser.parse_args(['--ignore-stdin', 'https://httpbin.org/get'])

# Generated at 2022-06-13 21:37:53.438564
# Unit test for function max_headers
def test_max_headers():
    with max_headers(10) as m:
        assert(m==10)

# Generated at 2022-06-13 21:38:04.811198
# Unit test for function make_request_kwargs
def test_make_request_kwargs():

    # Create a argparse instance
    parser = argparse.ArgumentParser()

    # Create a fake arguments with values

# Generated at 2022-06-13 21:38:12.813301
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.cli.base import Parser

    parser = Parser()
    args = parser.parse_args(['--cert=test-cert', '--cert-key=test-cert-key',
                              '--verify=True', '--proxy=http://test-proxy',
                              'test-url'])
    actual_kwargs = make_send_kwargs_mergeable_from_env(args)

    assert 'cert' in actual_kwargs
    assert 'test-cert' in actual_kwargs['cert']
    assert 'test-cert-key' in actual_kwargs['cert']
    assert 'proxies' in actual_kwargs
    assert 'http://test-proxy' in actual_kwargs['proxies'].values()
    assert 'verify' in actual_kwargs

# Generated at 2022-06-13 21:38:30.376233
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()

# Generated at 2022-06-13 21:38:44.322239
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    # pylint: disable=unused-import, import-outside-toplevel
    # pylint: disable=no-name-in-module
    from httpie.cli import parser

    args = parser.parse_args(['GET', 'http://example.com'])
    verify = {'yes': True, 'true': True, 'no': False, 'false': False}.get(args.verify.lower())
    kwargs = {
        'proxies': {},
        'stream': True,
        'verify': verify,
        'cert': None,
    }
    assert kwargs == make_send_kwargs_mergeable_from_env(args)