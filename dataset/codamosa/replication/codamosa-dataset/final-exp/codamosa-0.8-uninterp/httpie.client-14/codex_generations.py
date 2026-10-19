

# Generated at 2022-06-13 21:29:59.114506
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = type('arg_values',
        (object,),
        {'timeout': None,
         'allow_redirects': False
         }
    )
    expected = {
        'timeout': None,
        'allow_redirects': False
    }
    assert make_send_kwargs(args) == expected

# Generated at 2022-06-13 21:30:05.358698
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.chunked = False
    args.compress = 0

# Generated at 2022-06-13 21:30:13.656235
# Unit test for function collect_messages
def test_collect_messages():
  config_dir = Path(".")
  args = argparse.Namespace()
  #request_body_read_callback = Callable[[bytes], None] = None
  
  # simple test
  config_dir = Path(".")
  args = argparse.Namespace()
  args.method = "GET"
  args.url = "http://httpbin.org/get"
  args.headers = {"Host": "foo.com"}
  args.auth = ("user", "pass")
  args.timeout = 0.0
  args.follow = False
  args.max_redirects = 20
  args.max_headers = 3
  args.verify = True
  args.cert = False
  args.cert_key = False
  args.json = True
  args.form = False
  
  request_kwargs = make

# Generated at 2022-06-13 21:30:26.302415
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    from httpie.cli import parser
    from httpie.plugins import AuthPlugin, TransportPlugin

    class DummyTransportPlugin(TransportPlugin):
        prefix = 'dummy+'

    class DummyAuthPlugin(AuthPlugin):
        auth_type = 'dummy'

    dummy_arg_parser = parser.argparse.ArgumentParser(add_help=False)
    
    dummy_arg_parser.add_argument(
        '--verify', action=parser.StoreTrueFalseDefault,
        default=None, dest='verify',
        help="Choose to verify SSL certificates, if set."
    )


# Generated at 2022-06-13 21:30:34.871244
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    right = {'User-Agent': DEFAULT_UA}
    assert make_default_headers(args) == right

    args = argparse.Namespace()
    args.json = True
    args.data = None
    args.form = False
    right = {'User-Agent': DEFAULT_UA,
             'Accept': 'application/json, */*;q=0.5'}
    assert make_default_headers(args) == right

    args = argparse.Namespace()
    args.json = False
    args.data = {'c': 1}
    args.form = False
    right = {'User-Agent': DEFAULT_UA,
             'Accept': 'application/json, */*;q=0.5',
             'Content-Type': 'application/json'}

# Generated at 2022-06-13 21:30:46.217944
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = {}
    args.verify = True
    args.cert = ""
    args.cert_key = ""
    args_mergeable = make_send_kwargs_mergeable_from_env(args)
    assert args_mergeable['verify'] is True
    assert args_mergeable['proxies'] == {}
    assert args_mergeable['cert'] is None
    args.verify = "true"
    args_mergeable = make_send_kwargs_mergeable_from_env(args)
    assert args_mergeable['verify'] is True
    assert args_mergeable['proxies'] == {}
    assert args_mergeable['cert'] is None
    args.verify = "yes"
    args_mer

# Generated at 2022-06-13 21:30:51.423530
# Unit test for function max_headers
def test_max_headers():
    # Setup mock args
    args = argparse.Namespace()
    args.max_headers = 2
    with max_headers(args.max_headers):
        assert http.client._MAXHEADERS == 2

# Generated at 2022-06-13 21:31:03.265813
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.method = 'GET'
    args.url = 'https://www.google.com/'
    args.json = True
    args.files = None
    args.data = {'language': 'python'}
    args.form = True
    args.multipart_data = None
    args.boundary = None
    args.headers = {'Content-Type': '{"http-ie": "post"}'}
    args.auth = None
    args.params = {'q': 'json'}
    args.timeout = None
    args.compress = None
    args.chunked = None
    args.follow = None
    args.max_redirects = None
    args.all = None
    args.offline = None
    args.debug = None
    args

# Generated at 2022-06-13 21:31:09.307399
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    return_value = make_default_headers(args)
    assert return_value == {'User-Agent': 'HTTPie/' + __version__}

# Generated at 2022-06-13 21:31:17.980551
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    assert {'proxies': {'http': 'http://localhost', 'https': 'https://localhost'},
    'stream': True,
    'verify': 'yes',
    'cert': ('cert', 'cert_key')} == make_send_kwargs_mergeable_from_env(argparse.Namespace(verify='yes', cert='cert', cert_key='cert_key', proxy=[argparse.Namespace(key='http', value='http://localhost'), argparse.Namespace(key='https', value='https://localhost')]))

# Generated at 2022-06-13 21:31:47.902913
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Test for all values of request method taken
    for method in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH']:
        args = argparse.Namespace(
            method = method,
            data = {'foo':'bar'},
            oneline = False,
            offline = False,
            json = True,
            form = True,
            chunked = False,
            headers = {'user-agent': 'HTTPie/0.9.9'},
            auth =  {'username': 'admin', 'password': 'admin'},
            params = {'foo': 'bar'},
            verity = 'true',
            cert = 'cert.pem',
            cert_key ='cert_key.pem',
            url = 'http://httpie.org/get'
        )


# Generated at 2022-06-13 21:31:53.281811
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    assert make_send_kwargs_mergeable_from_env(argparse.Namespace()) == {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None
    }

# Generated at 2022-06-13 21:32:03.106923
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    # Dummy args to test function
    dummy_args = argparse.Namespace()
    dummy_args.method = 'GET'
    dummy_args.url = 'https://httpbin.org/'
    dummy_args.headers = {'Content-Type': 'application/json'}
    dummy_args.data = {}
    dummy_args.offline = False
    dummy_args.chunked = False
    dummy_args.auth = None
    dummy_args.params = {}
    dummy_args.json = False
    dummy_args.form = False
    dummy_args.multipart = False
    dummy_args.files = {}
    dummy_args.multipart_data = {}
    dummy_args.boundary = 'AwEsOmEbOuNdArY--'
    request_body_read_

# Generated at 2022-06-13 21:32:14.925401
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:32:22.900291
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    kwargs = make_send_kwargs_mergeable_from_env(args=None)
    assert kwargs == {
        'proxies': {p.key: p.value for p in args.proxy},
        'stream': True,
        'verify': {
            'yes': True,
            'true': True,
            'no': False,
            'false': False,
        }.get(args.verify.lower(), args.verify),
        'cert': cert,
    }

# Generated at 2022-06-13 21:32:37.943064
# Unit test for function make_request_kwargs
def test_make_request_kwargs():

    from httpie.cli import parser
    from httpie.context import Environment

    env = Environment()

    args=parser.parse_args(
        args=[],
        env=env,
    )

    result = make_request_kwargs(args)
    assert result == {
        'method': 'GET',
        'url': None,
        'headers': {
            'User-Agent': DEFAULT_UA,
        },
        'data': b'',
        'auth': None,
        'params': []
    }


# Generated at 2022-06-13 21:32:49.252691
# Unit test for function max_headers
def test_max_headers():
    os.environ['http_proxy'] = ''
    os.environ['https_proxy'] = ''
    parser = build_parser()
    args = parser.parse_args(["--session", "name", "--timeout", "100", "--max-redirects", "100", "--timeout", "30", "www.google.com"])
    config_dir = Path(os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config')))
    collect_messages(args, config_dir)

if __name__ == "__main__":
    test_max_headers()

# Generated at 2022-06-13 21:33:01.266520
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    """Unit test for function make_send_kwargs_mergeable_from_env"""
    import unittest
    import argparse
    from httpie.plugins import AUTH_PLUGIN_REGISTRY

    class TestCaseBase(unittest.TestCase):
        def _get_args(self, proxy_list=None, cert=None, cert_key=None, verify='True'):
            """
            Get Namespace from Mock Arguments
            """
            parser = argparse.ArgumentParser()
            parser.add_argument = lambda *args, **kw: None
            args = argparse.Namespace()
            args.proxy = proxy_list or []
            args.cert = cert
            args.cert_key = cert_key
            args.verify = verify

# Generated at 2022-06-13 21:33:07.835305
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    kwargs = make_send_kwargs(args)
    assert kwargs['timeout'] == 10
    assert kwargs['allow_redirects'] == False

# Generated at 2022-06-13 21:33:12.411934
# Unit test for function make_default_headers
def test_make_default_headers():
    arguments = argparse.Namespace(json=True, form=False, files=False, data=None, url='toto')
    headers = make_default_headers(arguments)
    assert headers == {'User-Agent': 'HTTPie/0.9.9.dev0', 'Accept': 'application/json, */*;q=0.5'}

    arguments = argparse.Namespace(json=False, form=True, files=False, data=None, url='toto')
    headers = make_default_headers(arguments)
    assert headers == {'User-Agent': 'HTTPie/0.9.9.dev0', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}


# Generated at 2022-06-13 21:33:35.689874
# Unit test for function collect_messages
def test_collect_messages():
    import unittest
    class TestCollectMessages(unittest.TestCase):
        def test_collect_messages(self):
            import argparse
            import os
            import warnings
            import tempfile
            import shutil
            import json

            class MyParser(argparse.ArgumentParser):
                def error(self, message):
                    pass

                def exit(self, status=0, message=None):
                    pass

            parser = MyParser()
            # fake session_name
            args = parser.parse_args(['--session', 'test'])
            args.session = 'test'
            args.session_read_only = False


            args.url = 'https://httpbin.org/post'
            args.method = 'POST'
            args.headers = []

# Generated at 2022-06-13 21:33:50.418381
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:34:01.607133
# Unit test for function finalize_headers
def test_finalize_headers():

    headers = {
        'Accept': ' application/json ',
        'Content-Type': ' application/json ',
        'User-Agent': 'HTTPie/0.9.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    expected_headers = {
        'Accept': b'application/json',
        'Content-Type': b'application/json',
        'User-Agent': b'HTTPie/0.9.9',
        'Accept-Encoding': b'gzip, deflate',
        'Connection': b'keep-alive',
    }
    final_headers = finalize_headers(headers)
    for key in final_headers:
        assert final_headers[key].decode() == expected_headers[key].decode()

# Generated at 2022-06-13 21:34:04.008613
# Unit test for function max_headers
def test_max_headers():
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == 1000

# Generated at 2022-06-13 21:34:04.969721
# Unit test for function max_headers
def test_max_headers():
    max_headers(None)

# Generated at 2022-06-13 21:34:17.456895
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:34:24.347355
# Unit test for function collect_messages
def test_collect_messages():
    url = 'http://api.github.com/repos/jakubroztocil/httpie'
    headers = {'Offline': 'false'}

# Generated at 2022-06-13 21:34:35.724518
# Unit test for function collect_messages
def test_collect_messages():
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    headers = {}
    class RequestHeadersDict:
        def update(self, _):
            pass
        def items(self):
            return headers.items()
    class Response:
        def __init__(self, next=None):
            self.next = next

# Generated at 2022-06-13 21:34:42.479924
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    kwargs = make_request_kwargs(args)
    assert kwargs['method'] == 'get'
    assert kwargs['url'] is None
    assert kwargs['headers'] == make_default_headers(args)
    assert kwargs['data'] is None
    assert kwargs['auth'] is None
    assert kwargs['params'] == []



# Generated at 2022-06-13 21:34:49.092205
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = lambda : None
    args.password = None
    args.verify = 'no'
    args.proxy = [
        lambda : None,
        lambda : None,
    ]
    args.proxy[0].key = 'foo'
    args.proxy[0].value = 'bar'
    args.proxy[1].key = 'boo'
    args.proxy[1].value = 'far'
    args.cert = '../fake_cert.pem'
    args.cert_key = '../fake_cert_key.pem'

# Generated at 2022-06-13 21:35:05.444597
# Unit test for function max_headers
def test_max_headers():
    limit = 100
    http.client._MAXHEADERS = 100
    # noinspection PyUnresolvedReferences
    with max_headers(limit):
        assert http.client._MAXHEADERS == limit
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:35:10.631959
# Unit test for function build_requests_session
def test_build_requests_session():
    requests_session = build_requests_session(verify=False, ssl_version='TLSv1.2', ciphers='DEFAULT:!LOW:!EXP:!MD5:!SSlv2:!SSLv3')
    assert requests_session.proxies == {}
    assert requests_session.verify == False
    assert requests_session.cert == None
    assert requests_session.timeout == None

# Generated at 2022-06-13 21:35:20.717406
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    headers = make_default_headers(args)
    assert headers.get('User-Agent') == DEFAULT_UA
    assert headers.get('Content-Type') is None
    assert headers.get('Accept') is None
    args.json = True
    headers = make_default_headers(args)
    assert headers.get('Accept') == JSON_ACCEPT
    args.data = '{"foo":"bar"}'
    headers = make_default_headers(args)
    assert headers.get('Content-Type') == JSON_CONTENT_TYPE
    args.json = False
    args.form = True
    args.files = False
    headers = make_default_headers(args)
    assert headers.get('Content-Type') == FORM_CONTENT_TYPE

# Generated at 2022-06-13 21:35:24.069795
# Unit test for function max_headers
def test_max_headers():
    with max_headers(5):
        assert http.client._MAXHEADERS == 5


# Generated at 2022-06-13 21:35:25.530102
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:35:31.255128
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    cmd = MagicMock()
    cmd.proxy = []
    cmd.verify = 'true'
    cmd.cert = None
    cmd.cert_key = None
    result = make_send_kwargs_mergeable_from_env(cmd)
    assert result == {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}

# Generated at 2022-06-13 21:35:39.823425
# Unit test for function make_send_kwargs

# Generated at 2022-06-13 21:35:43.970619
# Unit test for function build_requests_session
def test_build_requests_session():
    # Test call command
    from httpie.client import build_requests_session
    build_requests_session(verify=True, ssl_version='tls1.3')



# Generated at 2022-06-13 21:35:48.954991
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout=None,
        allow_redirects=False,
        proxy=['foo', 'bar'],
        stream=True,
        verify=True,
        cert=None,
    )
    assert make_send_kwargs(args) == kwargs

# Generated at 2022-06-13 21:36:01.680559
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli.argtypes import KeyValueArgType


# Generated at 2022-06-13 21:36:29.829865
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    import argparse
    args = argparse.Namespace()
    args.proxy = None
    args.verify = True
    args.cert = None
    args.cert_key = None
    print(make_send_kwargs_mergeable_from_env(args))



# Generated at 2022-06-13 21:36:35.617313
# Unit test for function make_default_headers
def test_make_default_headers():
    from httpie.core import main
    parser = main.parser.get_parser()
    args = parser.parse_args(args=['--json', 'http://foo/'])
    headers = make_default_headers(args)
    assert headers['Accept'] == "application/json, */*;q=0.5"

    args = parser.parse_args(args=['--form', 'http://foo/'])
    headers = make_default_headers(args)
    assert headers['Content-Type'] == "application/x-www-form-urlencoded; charset=utf-8"


# Generated at 2022-06-13 21:36:46.142882
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    final_header = make_default_headers(args)
    assert final_header['User-Agent'] == DEFAULT_UA
    args.json = True
    final_header = make_default_headers(args)
    import json
    assert json.loads(final_header['Accept'])[0]['mime'] == 'application/json'
    assert json.loads(final_header['Accept'])[0]['q'] == 0.5
    assert 'Content-Type' not in final_header
    args.json = False
    args.form = True
    args.files = True
    final_header = make_default_headers(args)
    assert 'Content-Type' not in final_header
    args.files = False
    final_header = make_default_headers(args)
   

# Generated at 2022-06-13 21:36:55.235835
# Unit test for function collect_messages
def test_collect_messages():
    class mock_argparse_namespace:
        def __init__(self, args):
            self._args = args

        def __getattr__(self, key):
            return self._args[key]

    class mock_config_dir:
        pass

    class mock_callback:
        def __init__(self, data):
            self._data = data

        def __call__(self, data):
            return self._data


# Generated at 2022-06-13 21:37:07.394778
# Unit test for function collect_messages
def test_collect_messages():
    from httpie.cli import parser as parser_module
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.tests.compat import mock
    from httpie.tests.utils import TestEnvironment

    env = TestEnvironment()

    def mock_get_config_dir():
        return env.config_dir

    parser = parser_module.parser
    args = parser.parse_args(
        [
            '--session=httpbin',
            '--auth-type=basic',
            '--auth=user:password',
            '--headers', 'Foo:Bar',
            'GET', 'http://httpbin.org/'
        ],
    )
    args.auth_plugin = HTTPBasicAuth()

    args.offline = False
    args.debug = True
    args.json = True

# Generated at 2022-06-13 21:37:21.016979
# Unit test for function collect_messages
def test_collect_messages():
    class args:
        def __init__(self):
            self.url = None
            self.method = 'GET'
            self.headers = dict()
            self.data = None
            self.json = None
            self.form = None
            self.files = None
            self.session = None
            self.session_read_only = None
            self.auth = None
            self.auth_plugin = None
            self.debug = None
            self.timeout = None
            self.chunked = None
            self.offline = None
            self.follow = None
            self.max_redirects = None
            self.params = dict()
            self.ssl_version = None
            self.ciphers = None
            self.compress = None
            self.verify = None
            self.proxy = dict()


# Generated at 2022-06-13 21:37:33.794823
# Unit test for function collect_messages
def test_collect_messages():
   args = argparse.Namespace()
   config_dir= Path('this')
   request_body_read_callback=None
   args.session = ""
   args.session_read_only=False
   args.session_read_only = ""
   args.url = ''
   args.headers = {}
   args.debug = False
   args.offline = False
   args.max_headers = None
   args.path_as_is = False
   args.compress = False
   args.method="GET"
   args.files=None
   args.json = False
   args.data = None
   args.form = False
   args.auth_plugin = None
   args.verify= []
   args.verify = ""
   args.verify = "true"
   args.verify = "yes"
  

# Generated at 2022-06-13 21:37:39.330510
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout = 10
    args.allow_redirects = False
    assert make_send_kwargs(args) == {
        'timeout': 10,
        'allow_redirects': False,
    }


# Generated at 2022-06-13 21:37:44.948552
# Unit test for function collect_messages

# Generated at 2022-06-13 21:37:45.545661
# Unit test for function max_headers
def test_max_headers():
    pass

# Generated at 2022-06-13 21:39:07.170813
# Unit test for function collect_messages
def test_collect_messages():
    class args:
        pass

    args.compress = False
    args.debug = False
    args.max_headers = None
    args.chunked = False
    args.offline = False
    args.session = None
    args.session_read_only = None
    args.path_as_is = False
    args.all = True
    args.auth = None
    args.auth_plugin = False
    args.auth_type = 'basic'
    args.cert = None
    args.cert_key = None
    args.ciphers = None
    args.data = {}
    args.files = None
    args.follow = True
    args.form = False
    args.headers = {}
    args.json = False
    args.method = 'GET'
    args.multipart = False
    args

# Generated at 2022-06-13 21:39:17.940527
# Unit test for function collect_messages

# Generated at 2022-06-13 21:39:20.638104
# Unit test for function make_default_headers
def test_make_default_headers():
    assert make_default_headers(argparse.Namespace()) == {'User-Agent': 'HTTPie/2.2.0'}


# Generated at 2022-06-13 21:39:30.846187
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.form = False
    args.data = {"key1":"value1"}
    headers = make_default_headers(args)
    assert headers.get("Content-Type") == "application/json"
    assert headers.get("Accept") == JSON_ACCEPT
    args.data = None
    args.headers = {"Key":"Value"}
    args.json = True
    headers = make_default_headers(args)
    assert headers.get("Content-Type") == "application/json"
    assert headers.get("Accept") == JSON_ACCEPT
    args.headers = None
    args.json = False
    headers = make_default_headers(args)
    assert headers.get("User-Agent") == DEFAULT_UA
    assert headers.get("Accept") == None
    assert headers.get

# Generated at 2022-06-13 21:39:38.161382
# Unit test for function collect_messages
def test_collect_messages():
    args.url = "https://www.google.com"
    url = "https://www.google.com"
    config_dir = Path("")
    request_body_read_callback = None

    httpie_session = None
    httpie_session_headers = None
    if args.session or args.session_read_only:
        httpie_session = get_httpie_session(
            config_dir=config_dir,
            session_name=args.session or args.session_read_only,
            host=args.headers.get('Host'),
            url=url,
        )
        httpie_session_headers = httpie_session.headers
