

# Generated at 2022-06-13 21:30:10.547551
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.proxy = [argparse.Namespace(key='http', value=123)]
    args.verify = 'one'
    args.cert = 'some cert'
    args.cert_key = 'some cert key'

    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env.get('proxies') == {'http': 123}
    assert send_kwargs_mergeable_from_env.get('verify') == False
    assert send_kwargs_mergeable_from_env.get('cert') == ('some cert', 'some cert key')

# Generated at 2022-06-13 21:30:15.361482
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    expected = {'proxies': {}, 'stream': True, 'verify': False, 'cert': None}
    result = make_send_kwargs_mergeable_from_env(
        argparse.Namespace(proxy=[], verify='no'))
    if result == expected:
        print("Test case 1 : Test make_send_kwargs_mergeable_from_env passed")
    else:
        print("Test case 1 : Test make_send_kwargs_mergeable_from_env failed")



# Generated at 2022-06-13 21:30:23.623161
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = ['http://httpbin.org/get',
            '--param', 'param1', 'value1']
    # args = ['http://httpbin.org/get']
    parser = argparse.ArgumentParser()
    # args = ['-v', 'http://httpbin.org/get']
    # args = ['--ignore-stdin', '--form',
    #         '--param', 'param1', 'value1',
    #         '--param', 'param2', 'value2',
    #         '-H', 'X-Header: foo',
    #         '--traceback', '-v', 'http://httpbin.org/post']

    from httpie.cli import parser as cli_parser
    cli_parser.add_arguments(parser)
    args = parser.parse_args(args)



# Generated at 2022-06-13 21:30:25.889465
# Unit test for function max_headers
def test_max_headers():
    with max_headers(20):
        assert http.client._MAXHEADERS == 20


# Generated at 2022-06-13 21:30:28.930071
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace()
    args.timeout=9
    args.allow_redirects=False
    assert make_send_kwargs(args)=={'timeout':9,'allow_redirects':False}



# Generated at 2022-06-13 21:30:37.121607
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = True
    args.form = False
    args.data = {}
    default_headers = {}
    default_headers = make_default_headers(args)
    assert default_headers == {'User-Agent': 'HTTPie/0.9.9',
                               'Accept': 'application/json, */*;q=0.5',
                               'Content-Type': 'application/json'}

# Generated at 2022-06-13 21:30:46.217874
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    assert make_request_kwargs({
        'method': 'get', 'url': 'https://google.com',
        'headers': { 'User-Agent' : DEFAULT_UA },
        'data': { 'data': 'dummy' },
        'auth': 'dummy', 'params': { 'param': 'dummy' }
    }) == {
        'method': 'get', 'url': 'https://google.com',
        'headers': { 'User-Agent' : DEFAULT_UA },
        'data': { 'data': 'dummy' },
        'auth': 'dummy', 'params': { 'param': 'dummy' }
    }

# Generated at 2022-06-13 21:30:47.721626
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:31:01.322928
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:31:03.238579
# Unit test for function max_headers
def test_max_headers():
    # Test for a context manager for the max headers limit
    limit = 30
    with max_headers(limit):
        assert http.client._MAXHEADERS == limit

# Generated at 2022-06-13 21:31:17.597302
# Unit test for function max_headers
def test_max_headers():
    assert http.client._MAXHEADERS == 100
    

# Generated at 2022-06-13 21:31:19.127537
# Unit test for function collect_messages
def test_collect_messages():
    pass

# Generated at 2022-06-13 21:31:30.986737
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    result = {'proxies': {'http': '127.0.0.1', 'https': '127.0.0.1'}, 'stream': True, 'verify': '127.0.0.1', 'cert': None}
    args = argparse.Namespace()
    setattr(args, 'verify', '127.0.0.1')
    setattr(args, 'proxy', [argparse.Namespace(key='http', value='127.0.0.1'), argparse.Namespace(key='https', value='127.0.0.1')])
    setattr(args, 'cert', None)
    setattr(args, 'cert_key', None)
    assert make_send_kwargs_mergeable_from_env(args) == result

# Generated at 2022-06-13 21:31:39.736292
# Unit test for function build_requests_session
def test_build_requests_session():
    # Case 1: Verify mode
    requests_session = build_requests_session(verify=True)
    assert requests_session.verify == True

    # Case 2: No verify mode
    requests_session = build_requests_session(verify=False)
    assert requests_session.verify == False


# Generated at 2022-06-13 21:31:45.494049
# Unit test for function finalize_headers
def test_finalize_headers():
    # General test
    headers = {'Accept-Encoding': ' gzip', 'Host': ' httpie.org   '}
    assert finalize_headers(headers) == {'Accept-Encoding': 'gzip', 'Host': 'httpie.org'}

    # Test for issue #212
    headers = {'Host': ' httpie.org '}
    assert finalize_headers(headers) == {'Host': 'httpie.org'}

# Generated at 2022-06-13 21:31:46.997171
# Unit test for function max_headers
def test_max_headers():
    # dummy function to test the context manager in max_headers
    with max_headers(20):
        assert http.client._MAXHEADERS==20

# Generated at 2022-06-13 21:31:53.623319
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():
    args = argparse.Namespace()
    args.cert = None
    args.cert_key = None
    args.proxy = []
    args.verify = True
    send_kwargs_mergeable_from_env = make_send_kwargs_mergeable_from_env(args)
    assert send_kwargs_mergeable_from_env == {'proxies': {}, 'stream': True, 'verify': True, 'cert': None}

# Generated at 2022-06-13 21:32:02.526639
# Unit test for function make_default_headers
def test_make_default_headers():
    
    # test passing a dictionary to data will yield a default header that accepts Json
    args = argparse.Namespace(
        json=False, form=False, data={}, method="GET", url="",
        headers={}, files={}, verify="", timeout=None, auth=None,
        params={}, chunked=False, all=False, follow=False,
        session=None, session_read_only=None, max_redirects=None,
        max_headers=None
    )

    default_headers = make_default_headers(args=args)
    assert default_headers['Accept'] == JSON_ACCEPT
    assert default_headers['Content-Type'] == JSON_CONTENT_TYPE


# Generated at 2022-06-13 21:32:02.989536
# Unit test for function collect_messages
def test_collect_messages():
    pass

# Generated at 2022-06-13 21:32:06.473902
# Unit test for function max_headers
def test_max_headers():
    import http.client
    with max_headers(2):
        assert http.client._MAXHEADERS == 2

    # https://github.com/httpie/httpie/issues/802
    # http.client._MAXHEADERS is restored
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:32:25.728471
# Unit test for function max_headers
def test_max_headers():
    with max_headers(10):
        assert http.client._MAXHEADERS

# Generated at 2022-06-13 21:32:34.912562
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        timeout = 10,
        allow_redirects = True,
    )

    kwargs = make_send_kwargs(args)
    correct_kwargs = {
        'timeout': 10,
        'allow_redirects': True,
    }
    assert kwargs == correct_kwargs, "test_make_send_kwargs failed"


# Generated at 2022-06-13 21:32:37.172957
# Unit test for function max_headers
def test_max_headers():
    limit = 10
    with max_headers(limit):
        assert http.client._MAXHEADERS == limit
    assert http.client._MAXHEADERS > limit


# Generated at 2022-06-13 21:32:50.650162
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace(form='false')
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == 'HTTPie/0.9.8'
    assert 'Content-Type' not in default_headers
    assert 'Accept' not in default_headers
    args = argparse.Namespace(form='true')
    default_headers = make_default_headers(args)
    assert default_headers['User-Agent'] == 'HTTPie/0.9.8'
    assert default_headers['Content-Type'] == 'application/x-www-form-urlencoded; charset=utf-8'
    assert 'Accept' not in default_headers
    args = argparse.Namespace(json='true')
    default_headers = make_default_headers(args)
    assert default_

# Generated at 2022-06-13 21:33:02.369899
# Unit test for function make_request_kwargs

# Generated at 2022-06-13 21:33:13.098424
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    args = argparse.Namespace(
        auth=None,
        auth_plugin=None,
        verify=True,
        cert=None,
        cert_key=None,
        proxy=None,
        timeout=None,
    )
    kwargs = make_send_kwargs(args)
    assert(kwargs['timeout'] is None)
    assert(kwargs['allow_redirects'] is False)
    assert('proxies' not in kwargs)
    assert(kwargs['stream'] is True)
    assert(kwargs['verify'] is True)
    assert(kwargs['cert'] is None)


# Generated at 2022-06-13 21:33:15.763838
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    kwargs = {
        'timeout': 2 or None,
        'allow_redirects': False,
    }
    return kwargs


# Generated at 2022-06-13 21:33:20.550350
# Unit test for function make_send_kwargs
def test_make_send_kwargs():
    """
    This function tests the make_send_kwargs function of http.py
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int)

    args = parser.parse_args(['--timeout', '5'])
    kwargs = make_send_kwargs(args)

    assert kwargs == {'timeout': 5, 'allow_redirects': False}



# Generated at 2022-06-13 21:33:31.115704
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class TestClass:
        def __init__(self):
            self.data = {}
            self.form = False
            self.files = False
            self.method = 'GET'
            self.headers = {}

    args = TestClass()

    assert make_request_kwargs(args) == {'method': 'get', 'url': 'http://127.0.0.1:8000/setup', 'headers': {'User-Agent': 'HTTPie/0.9.7'}, 'data': {}, 'auth': None, 'params': []}


# Generated at 2022-06-13 21:33:36.972593
# Unit test for function collect_messages
def test_collect_messages():
    print('Test function collect_messages...', end='')
    args = argparse.Namespace()
    config_dir = Path.cwd()
    assert next(collect_messages(
        args=args,
        config_dir=config_dir,
    )) == 0
    print('Done.')


# Generated at 2022-06-13 21:34:24.368993
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.data = None
    args.form = False
    default_headers = make_default_headers(args)
    assert(default_headers['User-Agent'] == 'HTTPie/' + __version__)
    assert(default_headers['Accept'] == 'application/json, */*;q=0.5')
    args.json = True
    args.data = {'test': 'test'}
    default_headers = make_default_headers(args)
    assert(default_headers['User-Agent'] == 'HTTPie/' + __version__)
    assert(default_headers['Accept'] == 'application/json, */*;q=0.5')
    assert(default_headers['Content-Type'] == 'application/json')

# Generated at 2022-06-13 21:34:26.742699
# Unit test for function max_headers
def test_max_headers():
    with max_headers(64):
        assert http.client._MAXHEADERS == 64

# Generated at 2022-06-13 21:34:31.374040
# Unit test for function make_default_headers
def test_make_default_headers():
    args = argparse.Namespace()
    args.json = False
    args.form = False
    args.user_agent = None
    args.data = False
    assert make_default_headers(args) == {'User-Agent': DEFAULT_UA}



# Generated at 2022-06-13 21:34:44.309370
# Unit test for function collect_messages
def test_collect_messages():
    # Arrange
    import utils
    files = {'file': open('test_data/test_file.txt', 'rb')}
    args = utils.mock_args(
         'https://httpbin.org/post',
         '-f', 'key=value',
         '--files', files,
         '--print=HbB',
         '--session=fake-session',
         '--debug'
    )
    # Act
    request, response = None, None
    for item in collect_messages(args=args, config_dir=utils.mock_config_dir()):
        if isinstance(item, requests.PreparedRequest):
            request = item
        if isinstance(item, requests.Response):
            response = item
    # Assert
    assert request
    assert response

test_

# Generated at 2022-06-13 21:34:56.805890
# Unit test for function collect_messages
def test_collect_messages():
    import sys
    import json
    from contextlib import contextmanager
    from pathlib import Path
    import argparse
    import urllib3
    import requests
    # noinspection PyProtectedMember
    from httpie import __version__
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.sessions import get_httpie_session
    from httpie.ssl import AVAILABLE_SSL_VERSION_ARG_MAPPING, HTTPieHTTPSAdapter
    from httpie.uploads import (
        compress_request, prepare_request_body,
        get_multipart_data_and_content_type,
    )
    from httpie.utils import get_expired_cookies, repr_dict
    urllib3.disable_warnings()

    default_headers = RequestHeadersDict

# Generated at 2022-06-13 21:34:57.879276
# Unit test for function collect_messages
def test_collect_messages():
    collect_messages(None, None)

# Generated at 2022-06-13 21:35:04.214383
# Unit test for function make_default_headers
def test_make_default_headers():
    test_arg = argparse.Namespace()
    test_arg.json = False
    test_arg.form = False
    test_arg.data = None
    default_headers = make_default_headers(test_arg)
    assert default_headers == {'User-Agent': DEFAULT_UA}

# Generated at 2022-06-13 21:35:07.165856
# Unit test for function collect_messages
def test_collect_messages():
    print(list(collect_messages(args)))



if __name__ == '__main__':
    test_collect_messages()

# Generated at 2022-06-13 21:35:19.386740
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    '''
    Tests for make_request_kwargs function
    '''
    print("\n\nTesting make_request_kwargs function\n")

    from httpie import cli
    args = cli.parser.parse_args(args=[])
    files = args.files
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

# Generated at 2022-06-13 21:35:22.951134
# Unit test for function collect_messages
def test_collect_messages():
    http = collect_messages([], [])
    for i in http:
        print(i)



# Generated at 2022-06-13 21:36:46.172357
# Unit test for function collect_messages
def test_collect_messages():
    import unittest
    import contextlib
    from .context import cli as cmd

    class TestCollectMessages(unittest.TestCase):
        def setUp(self):
            self.parser = cmd.parser

        @contextlib.contextmanager
        def captured_output(self):
            new_out, new_err = StringIO(), StringIO()
            old_out, old_err = sys.stdout, sys.stderr
            try:
                sys.stdout, sys.stderr = new_out, new_err
                yield sys.stdout, sys.stderr
            finally:
                sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-13 21:36:48.722364
# Unit test for function max_headers
def test_max_headers():
    with max_headers(1):
        assert http.client._MAXHEADERS == 1
    assert http.client._MAXHEADERS == 0x10000

# Generated at 2022-06-13 21:37:03.819490
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    class Args:
        def __init__(self):
            # The important thing is the value of these attributes,
            # not what they are called.
            # The content of this is validated in other tests.
            self.chunked = True
            self.data = {'a': 'b'}
            self.headers = {}
            self.json = True
            self.method = 'POST'
            self.headers = {'Content-Type': 'text/plain'}
            self.offline = True
            self.params = {'c': 'd'}
            self.url = 'http://foo.bar:1234'

    request_kwargs = make_request_kwargs(
        args=Args(),
        base_headers=None,
        request_body_read_callback=lambda chunk: chunk,
    )
   

# Generated at 2022-06-13 21:37:06.023452
# Unit test for function max_headers
def test_max_headers():
    with max_headers(1):
        assert http.client._MAXHEADERS == 1
    assert http.client._MAXHEADERS == 100

# Generated at 2022-06-13 21:37:20.303474
# Unit test for function collect_messages
def test_collect_messages():
    import argparse

# Generated at 2022-06-13 21:37:29.240222
# Unit test for function make_default_headers
def test_make_default_headers():
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--data', action='store_true')
    args = parser.parse_args(["--form"])
    headers = make_default_headers(args)
    print(headers)
    assert headers == {'User-Agent': 'HTTPie/0.9.9','Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    args = parser.parse_args(["--data"])
    headers = make_default_headers(args)
    print(headers)

# Generated at 2022-06-13 21:37:29.935496
# Unit test for function make_default_headers
def test_make_default_headers():
    assert make_default_headers()['User-Agent'] == DEFAULT_UA

# Generated at 2022-06-13 21:37:33.970221
# Unit test for function collect_messages
def test_collect_messages():
    args = argparse.Namespace()
    config_dir = Path('/path/to/config')
    request_body_read_callback = lambda chunk: chunk
    collect_messages(args, config_dir, request_body_read_callback)

# Generated at 2022-06-13 21:37:42.310940
# Unit test for function make_request_kwargs
def test_make_request_kwargs():
    args = argparse.Namespace()
    args.data = 'abc'
    args.files = [1]
    args.chunked=False
    args.method = 'GET'
    args.url = 'http://foo.bar'
    args.headers = {}
    args.json = False
    args.form = False
    args.multipart = False
    args.multipart_data = []
    args.auth_plugin = None
    args.auth = None
    args.params = {'foo': 'bar'}
    args.compress = False
    args.timeout = 42.0
    args.session = None
    args.session_read_only = None
    args.offline = False
    args.max_redirects = 30
    args.follow = False
    args.max_headers = 1000

# Generated at 2022-06-13 21:37:45.736461
# Unit test for function max_headers
def test_max_headers():
    with max_headers(0):
        assert http.client._MAXHEADERS == 0
    with max_headers(None):
        assert http.client._MAXHEADERS == float('Inf')
    assert http.client._MAXHEADERS == 1000