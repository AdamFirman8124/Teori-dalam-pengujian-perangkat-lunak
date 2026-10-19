

# Generated at 2022-06-12 21:55:32.936331
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    # Example JSON output from Galaxy
    # {u'detail': u'You have exceeded your API rate limit or quota. You can increase your limits by visiting your account page at https://galaxy.ansible.com/api/account/.',
    #  u'title': u'Too Many Requests',
    #  u'url': u'/api/v1/collections/',
    #  u'code': 429}
    #
    # Exact format and content of error depend on Galaxy server version and is not guaranteed
    # to be the same.

    # a rate limit exception with a 429 HTTP code should be detected successfully
    rate_limit_429_exception = GalaxyError(http_code=429, body={"code": 429})
    assert is_rate_limit_exception(rate_limit_429_exception)

    # a rate limit

# Generated at 2022-06-12 21:55:42.120664
# Unit test for function get_cache_id
def test_get_cache_id():
    # tests a basic parsing of the cache ID
    assert get_cache_id('http://example.com/galaxy/api.json') == 'example.com'
    assert get_cache_id('http://example.com/galaxy/api.json?q=foo%20bar') == 'example.com'
    assert get_cache_id('http://example.com/galaxy/api.json#anchor') == 'example.com'
    assert get_cache_id('http://example.com/galaxy/api.json?q=foo%20bar#anchor') == 'example.com'
    assert get_cache_id('http://example.com:8080/galaxy/api.json') == 'example.com:8080'

# Generated at 2022-06-12 21:55:53.488169
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    try:
        raise GalaxyError(HTTPError('test', 400, 'test', {}, StringIO('test')), '')
        assert False, "Should have thrown"
    except GalaxyError as e:
        assert "Code: Unknown" in str(e)
        assert e.http_code == 400
        assert e.url == "test"
    try:
        raise GalaxyError(HTTPError('test', 400, 'test', {}, StringIO('{"code": "test"}')), '')
        assert False, "Should have thrown"
    except GalaxyError as e:
        assert "Code: test" in str(e)
        assert e.http_code == 400
        assert e.url == "test"

# Generated at 2022-06-12 21:55:57.261828
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = requests.HTTPError()
    message = "Test Message"
    galaxy_error = GalaxyError(http_error, message)

    assert galaxy_error.http_code == http_error.code
    assert galaxy_error.url == http_error.geturl()
    assert galaxy_error.message == message + " (HTTP Code: %d, Message: %s)" % (http_error.code, http_error.reason)


# Generated at 2022-06-12 21:56:05.609338
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    """
    Validate the constructor of the GalaxyAPI class.
    """
    api = GalaxyAPI('galaxy_server', 'api/v1')
    assert api.name is None
    assert api.api_server == 'galaxy_server/api/v1'
    assert api.verify_ssl
    assert api.ignore_certs
    assert api.auth_token is None
    assert api.available_api_versions == {'v1': 'api/v1'}


# Generated at 2022-06-12 21:56:11.244667
# Unit test for function cache_lock
def test_cache_lock():
    class Test:
        @cache_lock
        def test(self):
            self.value += 1

    test = Test()
    test.value = 0
    threads = [threading.Thread(target=test.test) for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert test.value == 1



# Generated at 2022-06-12 21:56:14.872707
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api = GalaxyAPI(api_server="https://galaxy.example.com")
    assert galaxy_api.__lt__(GalaxyAPI(api_server="https://galaxy.example.com")) is False


# Generated at 2022-06-12 21:56:24.162086
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    from ansible.galaxy.server.api import GalaxyAPI
    from ansible.utils.path import unfrackpath
    name = 'Galaxy'
    api_server = 'https://galaxy.ansible.com/'
    api_token = 'XXXXXXXXXXXXXXXXXXXXXX'
    ignore_certs = False
    is_automation_hub = False
    verify_ssl = True
    proxy_url = None
    proxy_port = None
    proxy_username = None
    proxy_password = None
    proxy_headers = None
    client_cert = None
    client_key = None
    timeout = 10
    use_short_cache = False
    allow_reconnect = True
    ignore_cache = False

# Generated at 2022-06-12 21:56:28.476149
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    try:
        raise GalaxyError(HTTPError('url', 404, 'Not Found', '', 'message not found'), 'message')
    except GalaxyError as err:
        assert err.message == 'message (HTTP Code: 404, Message: Not Found)'
        assert err.url == 'url'
        assert err.http_code == 404



# Generated at 2022-06-12 21:56:29.090888
# Unit test for function g_connect
def test_g_connect():
    pass


# Generated at 2022-06-12 21:57:06.454234
# Unit test for function g_connect
def test_g_connect():
    # Init an args object intended for AnsibleModule
    test_args = {
        'name': 'test_repo',
        'description': 'Test repo',
        'api_key': 'test_api_key',
        'api_server': 'https://galaxy.example.com',
        'validate_certs': True,
        'ignore_certs': False,
        'ignore_cache': False,
        'http_timeout': 10,
        'force': False,
        'no_wait': False,
        'no_logout': False
    }
    # Dummy method
    def test_method(self, *args, **kwargs):
        return

    # Init GalaxyClient
    test_galaxy = GalaxyClient(**test_args)

    # Mock _call_galaxy to return a fake available_versions list

# Generated at 2022-06-12 21:57:15.827612
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    msg = u"This is an error"
    exc = HTTPError(url="http://www.example.com/foo", code=503, msg=msg, hdrs="", fp=None)
    with pytest.raises(GalaxyError) as e_info:
        e = GalaxyError(exc, "This is a message")
        # Check that we've got the expected exception
        assert e.http_code == exc.code
        assert isinstance(e.url, string_types)
        assert e.message == "This is a message (HTTP Code: 503, Message: This is an error)"
        # Raise exception to make sure `__str__` works as expected
        raise e


# Get cache object (thread safe) for the cache ID/URL specified.
# If the cache doesn't exist, it will be created on demand.

# Generated at 2022-06-12 21:57:16.675505
# Unit test for function g_connect
def test_g_connect():
    pass

# Unit Test

# Generated at 2022-06-12 21:57:18.592282
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def test_func(value):
        return value + 1
    assert test_func(1) == 2



# Generated at 2022-06-12 21:57:25.842685
# Unit test for function g_connect
def test_g_connect():
    class Collections(object):
        api_server = 'https://galaxy.ansible.com/'
        name = 'Ansible Galaxy'
        _available_api_versions = {}

        def __init__(self, *args, **kwargs):
            pass

        def _call_galaxy(self, url, method='GET', data=None, headers=None, error_context_msg=None, cache=False):
            pass

    # And now to test it
    class FakeCollections(Collections):
        # Ensure we always have this initialized before making a call to use the decorator
        _available_api_versions = {u'v1': u'v1/'}

        @g_connect(versions=['v1'])
        def test_call_v1(self):
            return 'ok'


# Generated at 2022-06-12 21:57:34.692443
# Unit test for function get_cache_id
def test_get_cache_id():
    url_list = [
        'http://localhost:123/',
        'http://localhost/',
        'localhost/',
        'localhost',
        'https://localhost:123/',
        'https://localhost/',
        'https://localhost',
        'https://foo:bar@localhost/',
        'https://foo:bar@localhost',
        'https://localhost/path/to/api',
        'https://localhost/path/to/api/',
        'localhost:123',
        'localhost/path/to/api',
    ]

# Generated at 2022-06-12 21:57:42.875475
# Unit test for function cache_lock
def test_cache_lock():
    from ansible.module_utils.urls import get_url_connection
    from ansible.galaxy.role import GalaxyRole

    def _fake_get_url_connection(*args, **kwargs):
        return True

    @cache_lock
    def test_function():
        return True

    original = GalaxyRole.get_url_connection
    GalaxyRole.get_url_connection = _fake_get_url_connection
    result = test_function()
    GalaxyRole.get_url_connection = original

    # assert the wrapped function actually ran
    assert result is True


# Generated at 2022-06-12 21:57:46.786318
# Unit test for function cache_lock
def test_cache_lock():
    ins = CacheLockTest()
    ins.test_val = 1
    assert ins.test_val == 1
    ins.set_test_val()
    assert ins.test_val == 2



# Generated at 2022-06-12 21:57:57.092233
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError('', '', http_code=429))
    assert is_rate_limit_exception(GalaxyError('', '', http_code=520))
    assert not is_rate_limit_exception(GalaxyError('', '', http_code=403))
    assert not is_rate_limit_exception(GalaxyError('', '', http_code=500))
    assert not is_rate_limit_exception(GalaxyError('', '', http_code=200))
    assert not is_rate_limit_exception(GalaxyError('', '', http_code=503))
    assert not is_rate_limit_exception(ValueError())
    assert not is_rate_limit_exception(None)

# Generated at 2022-06-12 21:58:08.772303
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    test_error_message = "test error message"
    test_http_code = 404
    test_url = "https://api.galaxy.ansible.com/api/v2/collections/ansible/test-collection"
    test_v2_json_data = '''
    {
        "detail":"Not found.",
        "code":404,
        "message":"Not found.",
        "status":"error",
        "result":"error"
    }
    '''
    test_v3_json_data = '''
    {
        "errors":[
            {
                "status":404,
                "detail":"Not found.",
                "code":404,
            }
        ]
    }
    '''


# Generated at 2022-06-12 21:59:30.384966
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    class NotRateLimitException(Exception): pass
    class RateLimitException(GalaxyError):
        def __init__(self, *args, **kwargs):
            super(RateLimitException, self).__init__(*args, **kwargs)
            self.url = 'https://galaxy.ansible.com:443/api/v1/'
            self.http_code = 429
            self.method = 'GET'
            self.cause = 'Too Many Requests'
    assert is_rate_limit_exception(RateLimitException()) is True
    assert is_rate_limit_exception(NotRateLimitException()) is False

# TODO: Add unit tests

# Generated at 2022-06-12 21:59:43.229540
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    args = dict(
        api_server='https://galaxy.ansible.com',
        galaxy_token=None,
        ignore_certs=False,
        validate_certs=True,
    )
    ga1 = GalaxyAPI(**args)

    args = dict(
        api_server='https://galaxy.ansible.com',
        galaxy_token=None,
        ignore_certs=False,
        validate_certs=True,
    )
    ga2 = GalaxyAPI(**args)
    assert ga1 < ga2 is False

    args = dict(
        api_server='https://galaxy.ansible.com',
        galaxy_token=None,
        ignore_certs=False,
        validate_certs=True,
    )
    ga3 = GalaxyAPI(**args)
    assert ga

# Generated at 2022-06-12 21:59:49.453247
# Unit test for function get_cache_id
def test_get_cache_id():
    test_url = "https://localhost?foo=bar"
    ret_val = get_cache_id(test_url)
    assert ret_val == "localhost"
    test_url = "http://localhost:4242?foo=bar"
    ret_val = get_cache_id(test_url)
    assert ret_val == "localhost:4242"
test_get_cache_id()



# Generated at 2022-06-12 21:59:55.032885
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError("", 404, "Not Found", {}, None)
    try:
        raise GalaxyError(http_error, "Error")
    except GalaxyError as err:
        assert err.message == "Error (HTTP Code: 404, Message: Not Found)"
        assert err.http_code == 404
        assert err.url == ""



# Generated at 2022-06-12 22:00:04.528595
# Unit test for function cache_lock
def test_cache_lock():
    global _INVOKE_COUNT

    _INVOKE_COUNT = 0

    @cache_lock
    def func():
        global _INVOKE_COUNT
        _INVOKE_COUNT += 1
        return _INVOKE_COUNT

    num_threads = 4
    num_runs_per_thread = 10

    def invoke_func():
        for i in range(0, num_runs_per_thread):
            func()

    threads = [threading.Thread(target=invoke_func) for x in range(0, num_threads)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    assert _INVOKE_COUNT == num_threads * num_runs_per_thread



# Generated at 2022-06-12 22:00:10.617218
# Unit test for function get_cache_id
def test_get_cache_id():
    def _test(url, expected_id):
        id = get_cache_id(url)
        assert id == expected_id, "Expected %s but got %s" % (expected_id, id)


# Generated at 2022-06-12 22:00:19.695467
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import collections
    stub_http_error_dict = collections.namedtuple('stub_http_error_dict', ('code', 'read', 'geturl', 'reason'))
    stub_http_error = stub_http_error_dict(code=1, read=lambda: {'message': 'Stub message', 'code': 'Stub code'}, geturl=lambda: 'https://galaxy.ansible.com', reason='Stub reason')
    test = GalaxyError(stub_http_error, 'Stub message')
    assert test.http_code == 1
    assert test.url == 'https://galaxy.ansible.com'
    assert test.message == 'Stub message (HTTP Code: 1, Message: Stub message Code: Stub code)'


# Generated at 2022-06-12 22:00:22.419617
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    def __lt__(self, other):
        return self.api_server.__lt__(other.api_server)

    GalaxyAPI.__lt__ = __lt__

    test_instance = GalaxyAPI('https://localhost')
    target_instance = GalaxyAPI('https://localhost')

    assert test_instance < other


# Generated at 2022-06-12 22:00:24.560743
# Unit test for function g_connect
def test_g_connect():
    return wr.g_connect(['v1','v2'])



# Generated at 2022-06-12 22:00:29.729108
# Unit test for function get_cache_id
def test_get_cache_id():
    def check_cache_id(input, output):
        assert get_cache_id(input) == output
    check_cache_id('http://site.name/path', 'site.name')
    check_cache_id('http://site.name:8080/path', 'site.name:8080')
    check_cache_id('http://user:password@site.name:8080/path', 'site.name:8080')


# Generated at 2022-06-12 22:03:01.469961
# Unit test for function g_connect
def test_g_connect():
    import collections
    import mock
    import pytest
    versions = ['v1']
    mock_method = collections.namedtuple('MockMethod', ['__name__'])('test_method')
    mock_self = collections.namedtuple('MockSelf', ['_available_api_versions', 'api_server', 'name'])({}, 'test_server', 'test_server_name')
    mock_self._available_api_versions = {}
    mock_self.api_server = 'test_server'
    mock_self.name = 'test_server_name'

# Generated at 2022-06-12 22:03:07.465512
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    response = '{"default": "Ansible-Galaxy error message"}'
    http_error = HTTPError('http://examp.le/api/', 400, 'Bad Request', {}, io.StringIO(response))
    error_msg = "Ansible-Galaxy error message (HTTP Code: 400, Message: Ansible-Galaxy error message)"
    galaxy_error = GalaxyError(http_error, "foo")

    assert error_msg == galaxy_error.message



# Generated at 2022-06-12 22:03:14.819339
# Unit test for function g_connect
def test_g_connect():
    import collections
    class test_class:
        def __init__(self, a_server, name):
            self._available_api_versions = None
            self.api_server = a_server
            self.name = name

        def _call_galaxy(self, url, method='GET', data=None, error_context_msg=None, cache=False):
            return {u'available_versions': {u'v1': u'v1/'}}

    t1 = test_class("https://galaxy.ansible.com", "Galaxy")
    t2 = test_class("https://localhost", "local")

    @g_connect([u'v1'])
    def test_api(self):
        return "testing"

    # Test for v1 API which is available on galaxy.ansible.com
    assert test

# Generated at 2022-06-12 22:03:17.568451
# Unit test for function cache_lock
def test_cache_lock():
    var = 0
    @cache_lock
    def function():
        nonlocal var
        var = 1
        return var

    function()
    assert var == 1
    var = 0
    function()
    assert var == 1



# Generated at 2022-06-12 22:03:23.555544
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    error_message = 'An error message'
    http_error = HTTPError(url='https://galaxy.ansible.com', code=404, msg='not found', hdrs='No headers', fp=None)
    galaxy_error = GalaxyError(http_error, message=error_message)
    assert galaxy_error.message == 'An error message (HTTP Code: 404, Message: not found)'
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == 'https://galaxy.ansible.com'


# Generated at 2022-06-12 22:03:29.649789
# Unit test for function get_cache_id
def test_get_cache_id():
    # test with a basic url
    assert get_cache_id("https://galaxy.ansible.com") == "galaxy.ansible.com:"

    # test with credentials
    assert get_cache_id("https://ansible:ansible@galaxy.ansible.com") == "galaxy.ansible.com:"

    # test with a custom port
    assert get_cache_id("https://galaxy.ansible.com:1") == "galaxy.ansible.com:1"

    # test with a numeric port
    assert get_cache_id("https://galaxy.ansible.com:443") == "galaxy.ansible.com:443"



# Generated at 2022-06-12 22:03:41.923628
# Unit test for function get_cache_id
def test_get_cache_id():
    url = "http://test.server:80/path/to/endpoint?a=1&b=2"
    cache_id = get_cache_id(url)
    assert cache_id == "test.server:80"
    cache_id = get_cache_id("http://test.server/path/to/endpoint?a=1&b=2")
    assert cache_id == "test.server"  # No port specified
    cache_id = get_cache_id("http://test.server:8080/path/to/endpoint?a=1&b=2")
    assert cache_id == "test.server:8080"
    cache_id = get_cache_id("http://test.server/")
    assert cache_id == "test.server"

# Generated at 2022-06-12 22:03:44.147853
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    import pytest

    with pytest.raises(AnsibleError):
        GalaxyAPI.__lt__(None, None)



# Generated at 2022-06-12 22:03:54.289452
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    from ansible.module_utils.api import open_url
    from ansible.module_utils.urls import ConnectionError
    assert is_rate_limit_exception(GalaxyError(open_url.DEFAULT_ERROR_MESSAGE, code=429, url='/',
                                               method='GET'))
    assert not is_rate_limit_exception(GalaxyError(open_url.DEFAULT_ERROR_MESSAGE, code=404, url='/',
                                                   method='GET'))
    assert not is_rate_limit_exception(ConnectionError(open_url.DEFAULT_ERROR_MESSAGE))

# Generated at 2022-06-12 22:04:00.251816
# Unit test for function g_connect
def test_g_connect():
    def a():
        print('a')
    def b():
        print('b')
    def c():
        print('c')
    d = g_connect(['1','2'])(a)
    e = g_connect(['2','3'])(b)
    f = g_connect(['4','5'])(c)
    d()
    e()
    f()
# test_g_connect()

