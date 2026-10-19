

# Generated at 2022-06-12 21:55:26.714656
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('https://galaxy.ansible.com/api/') == 'galaxy.ansible.com:'
    assert get_cache_id('http://galaxy.ansible.com/api/') == 'galaxy.ansible.com:'
    assert get_cache_id('http://galaxy.ansible.com:8080/api/') == 'galaxy.ansible.com:8080'
    assert get_cache_id('https://galaxy.ansible.com:8080/api/') == 'galaxy.ansible.com:8080'



# Generated at 2022-06-12 21:55:27.051956
# Unit test for function g_connect
def test_g_connect():
    pass



# Generated at 2022-06-12 21:55:35.303209
# Unit test for function g_connect
def test_g_connect():
    class ApiClientFake(object):
        def __init__(self):
            self.name = 'names'
            self.api_server = "api_server"
            self._available_api_versions = ['v1', 'v2']

    @g_connect(versions=["v1", "v2"])
    def galaxy_api_method(self, *args, **kwargs):
        pass

    api_client = ApiClientFake()

    # galaxy_api_method is wrapped in g_connect decorator
    assert galaxy_api_method(api_client) == None



# Generated at 2022-06-12 21:55:43.368512
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy.server.fixtures import GalaxyServerFixture
    galaxy_server = GalaxyServerFixture()

    class GoodConnection(GalaxyConnection):
        """
        A GalaxyConnection that supports v1 and v2.
        """
        @g_connect(versions=['v1', 'v2'])
        def test_api(self):
            pass
    galaxy_server.add_connection(GoodConnection())
    galaxy_server.test_api()

    class BadConnection(GalaxyConnection):
        """
        A GalaxyConnection that supports v1 and v2, but we have restricted those.
        """
        @g_connect(versions=['v3'])
        def test_api(self):
            pass
    galaxy_server.add_connection(BadConnection())

# Generated at 2022-06-12 21:55:54.705928
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # To test the constructor of class GalaxyError.
    from test.unit.galaxy.test_galaxy import _TempTestFile
    from ansible.module_utils.six import b

    with _TempTestFile(b('{"default": "Error!","user_email": "admin@localhost"}')) as test_file:
        http_error = HTTPError(url='/galaxy/', code=404, msg='Not Found', hdrs=None, fp=None)
        http_error.read = test_file.read
        err = GalaxyError(http_error, 'Error test.')

    assert err.message == "Error test. (HTTP Code: 404, Message: Error! Code: Unknown)"
    assert err.http_code == 404
    assert err.url == "http://localhost/"
    assert err.http_error == http_

# Generated at 2022-06-12 21:56:01.448019
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import sys
    class fake_exception():
        def __init__(self, code, reason):
            self.code = code
            self.reason = reason
        def read(self):
            return '{"default": "Galaxy message"}'

    # Here we create a fake HTTPError so that we can check whether the message of GalaxyError is constructed properly.
    fake_http_error = fake_exception(404, 'Not found')
    error = GalaxyError(fake_http_error, 'Cannot find the requested URL on Galaxy')
    assert error.message == "Cannot find the requested URL on Galaxy (HTTP Code: 404, Message: Galaxy message)"

    # Next we test for the case where we cannot read the message from the HTTPError.
    fake_http_error = fake_exception(404, 'Not found')

# Generated at 2022-06-12 21:56:09.211090
# Unit test for function g_connect
def test_g_connect():
    class GalaxyConnection:
        def __init__(self):
            self._available_api_versions = {}
            self.api_server = u'https://galaxy.ansible.com'
            self.name = u'galaxy_server'

        @g_connect([u'v1',u'v2'])
        def test_connection(self, *args, **kwargs):
            print("unit test success")
            return None

    gc = GalaxyConnection()
    gc.test_connection()


# Generated at 2022-06-12 21:56:14.004043
# Unit test for function cache_lock
def test_cache_lock():
    from unittest import mock
    from threading import Lock

    # use mock to ensure lock is acquired and then released
    @cache_lock
    def wrapped():
        pass
    assert isinstance(wrapped.__wrapped__, mock.Mock)
    wrapped.__wrapped__.assert_called_once_with(Lock())


# Generated at 2022-06-12 21:56:23.526611
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    error_msg = u"Galaxy message."
    error_code = 401
    http_error = HTTPError(url="http://galaxy.ansible.com", code=error_code, msg=error_msg, hdrs=[], fp=None)
    galaxy_error = GalaxyError(http_error, "Galaxy error.")
    assert galaxy_error.message == u"Galaxy error. (HTTP Code: 401, Message: Galaxy message. Code: Unknown)"

    error_msg = u"Galaxy message."
    error_code = 401
    http_error = HTTPError(url="http://galaxy.ansible.com", code=error_code, msg=error_msg, hdrs=[], fp=None)
    galaxy_error = GalaxyError(http_error, "Galaxy error.")
    assert galaxy_error.message == u

# Generated at 2022-06-12 21:56:28.713822
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    err = GalaxyError(HTTPError(url='http://redhat.com', code=123, msg='test', hdrs=[], fp=None),
                      message='test_GalaxyError')
    assert err.http_code == 123
    assert err.url == 'http://redhat.com'
    assert err.message == 'test_GalaxyError (HTTP Code: 123, Message: test)'



# Generated at 2022-06-12 21:57:36.849017
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy import Galaxy
    galaxy = Galaxy('https://galaxy.test.test', 'http://localhost:8080', 'test', 'test')
    def test_method(self, *args, **kwargs):
        return True
    test_method = g_connect([1, 2])(test_method)
    test_method(galaxy)



# Generated at 2022-06-12 21:57:42.416381
# Unit test for function cache_lock
def test_cache_lock():
    global _CACHE_LOCK
    global cache_lock
    _CACHE_LOCK = threading.Lock()
    # NOTE: We don't just wrap the function and return it because the decorator
    # will be invoked in the function definition scope and the _CACHE_LOCK will
    # be evaluated in the caller's scope.
    cache_lock = cache_lock(lambda func: func)
    cache_lock(lambda: None)()



# Generated at 2022-06-12 21:57:51.108107
# Unit test for function get_cache_id
def test_get_cache_id():
    url = 'https://localhost:1234'
    assert get_cache_id(url) == 'localhost:1234'
    url = 'http://localhost:1234'
    assert get_cache_id(url) == 'localhost:1234'
    url = 'http://localhost'
    assert get_cache_id(url) == 'localhost'
    url = 'http://localhost:80'
    assert get_cache_id(url) == 'localhost:80'
    url = 'http://localhost:443'
    assert get_cache_id(url) == 'localhost'



# Generated at 2022-06-12 21:58:00.015569
# Unit test for function cache_lock
def test_cache_lock():
    import threading

    @cache_lock
    def ret_one():
        return 1
    @cache_lock
    def ret_two():
        return 2
    @cache_lock
    def ret_three():
        return 3

    class test_thread(threading.Thread):
        def __init__(self, func):
            super(test_thread, self).__init__()
            self.func = func

        def run(self):
            self.result = self.func()

    t_one = test_thread(ret_one)
    t_two = test_thread(ret_two)
    t_three = test_thread(ret_three)
    t_one.start()
    t_two.start()
    t_three.start()
    t_one.join()
    t_two.join()


# Generated at 2022-06-12 21:58:10.622858
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://localhost:6000/') == 'localhost:'
    assert get_cache_id('https://localhost:6000/api/') == 'localhost:'
    assert get_cache_id('http://galaxy.server.host.name/api/') == 'galaxy.server.host.name:'
    assert get_cache_id('https://user:password@galaxy.server.host.name/api/') == 'galaxy.server.host.name:'
    assert get_cache_id('http://user:password@galaxy.server.host.name/api/') == 'galaxy.server.host.name:'
    assert get_cache_id('https://user:password@galaxy.server.host.name:6000/api/') == 'galaxy.server.host.name:6000'



# Generated at 2022-06-12 21:58:22.107188
# Unit test for function g_connect
def test_g_connect():
    def dummy_method(self, *args, **kwargs):
        pass

    class DummyGalaxy(object):
        _available_api_versions = {}
        api_server = 'https://galaxy.ansible.com'
        name = 'Galaxy'

        def _call_galaxy(self, *args, **kwargs):
            pass

    dg = DummyGalaxy()

    # Should fail with v2 if available_versions is an empty dict
    methods = [
        g_connect(['v1', 'v2']),
        g_connect(['v2', 'v3']),
        g_connect(['v1', 'v4'])]
    for m in methods:
        f = m(dummy_method)

# Generated at 2022-06-12 21:58:32.716520
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy.api import GalaxyAPI
    g = GalaxyAPI(None, None, None)
    g.api_server = 'https://galaxy.ansible.com'

    @g_connect([u"v1", u"v2"])
    def _test_g_connect(self):
        return 1

    # Test the decorator
    assert _test_g_connect(g) == 1

    # Test that an exception is raised if the required version is not available
    @g_connect([u"not_a_version"])
    def _test_g_connect_exception(self):
        return 1

    try:
        _test_g_connect_exception(g)
        assert False, "Expected an exception, didn't get one"
    except AnsibleError:
        pass



# Generated at 2022-06-12 21:58:37.643476
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api = GalaxyAPI('https://galaxy.example.com/api/', 'ansible', 'mytoken')
    assert api.api_server == 'https://galaxy.example.com/api/'
    assert api.api_token == 'mytoken'
    assert api.api_user == 'ansible'
    assert api.headers == {'Authorization': 'Bearer mytoken', 'Content-type': 'application/json'}



# Generated at 2022-06-12 21:58:43.195828
# Unit test for function g_connect
def test_g_connect():
    class dummy:
        def __init__(self):
            self._available_api_versions = None
            self.api_server = 'https://galaxy.ansible.com'
            self.name = 'ansible'
        def _call_galaxy(self, *args, **kwargs):
            return {'available_versions': {u'v1': u'v1/', u'v2': u'v2/'}, u'prefix': u'', u'name': u'ansible'}

    @g_connect([u'v1', u'v2'])
    def connect_test(self, **kwargs):
        return self._available_api_versions

    dum = dummy()


# Generated at 2022-06-12 21:58:47.105799
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():  # pylint: disable=missing-docstring
    a = GalaxyAPI(server='https://galaxy.ansible.com')
    assert a.cache == {}



# Generated at 2022-06-12 21:59:24.764530
# Unit test for function cache_lock
def test_cache_lock():
    with _CACHE_LOCK:
        return 'Hello'


# Generated at 2022-06-12 21:59:28.941981
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    class GalaxyErrorStub(GalaxyError, collections.namedtuple('GalaxyErrorStub', 'http_code')):
        pass
    for code in [200, 403, 500]:
        input = GalaxyErrorStub(http_code=code)
        assert not is_rate_limit_exception(input)
    for code in RETRY_HTTP_ERROR_CODES:
        input = GalaxyErrorStub(http_code=code)
        assert is_rate_limit_exception(input)



# Generated at 2022-06-12 21:59:29.387096
# Unit test for function g_connect
def test_g_connect():
    pass



# Generated at 2022-06-12 21:59:41.480887
# Unit test for function g_connect
def test_g_connect():
    version=['v1','v2']
    class GalaxyConn:
        def __init__(self,api_server,name,token=None):
            self._available_api_versions = None
            self.api_server = 'https://galaxy.ansible.com/api/'
            self.name = 'name'
            self.token = 'token'
            

# Generated at 2022-06-12 21:59:41.883623
# Unit test for function g_connect
def test_g_connect():
    pass

# Generated at 2022-06-12 21:59:53.646238
# Unit test for function g_connect
def test_g_connect():
    """Test the g_connect decorator"""
    class FakeGalaxyClient:
        def __init__(self, api_server):
            self.api_server = api_server
            self._available_api_versions = None
        def _call_galaxy(self, url, error_context_msg, cache=False):
            pass
        @g_connect(['v1'])
        def method_with_galaxy_connection_required(self):
            pass

    with pytest.raises(AnsibleError):
        FakeGalaxyClient('http://api-server').method_with_galaxy_connection_required()

    with pytest.raises(AnsibleError):
        FakeGalaxyClient('http://api-server')._available_api_versions = {'v2': 'v2/'}
        FakeGalaxyClient

# Generated at 2022-06-12 21:59:54.810646
# Unit test for function g_connect
def test_g_connect():
    a = g_connect(versions=['v1'])
    assert a.__name__ == 'wrapped'


# Generated at 2022-06-12 22:00:03.668231
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():  # pylint: disable=too-few-public-methods
    """Unit test for constructor of class GalaxyAPI."""
    from ansible.module_utils.six.moves.urllib.parse import urlparse

    galaxy_api = GalaxyAPI(api_server='http://localhost:8080', validate_certs=True, force=True,
                           ignore_certs=False, ignore_errors=False, token='your-token',
                           disable_cache=True, available_api_versions={'v3': 'api/v3', 'v2': 'api/v2'},
                           timeout=60)
    assert galaxy_api.api_server == 'http://localhost:8080/'
    assert urlparse(galaxy_api.api_server).scheme == 'http'

# Generated at 2022-06-12 22:00:14.819905
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    from ansible_galaxy.models.api import GalaxyAPI
    #
    # Test with a simple example.
    #
    galaxy_api_obj__1 = GalaxyAPI(name='foo', api_server='http://127.0.0.1:8080', github_token=None, ignore_certs=False, galaxy_token=None)
    galaxy_api_obj__2 = GalaxyAPI(name='foo', api_server='http://127.0.0.1:8080', github_token=None, ignore_certs=False, galaxy_token=None)
    assert not galaxy_api_obj__1 < galaxy_api_obj__2

# Generated at 2022-06-12 22:00:16.760742
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert not is_rate_limit_exception(HTTPError(None, 408, None, None, None))
    assert is_rate_limit_exception(GalaxyError(None, "foo", None, 429))
    assert is_rate_limit_exception(GalaxyError(None, "foo", None, 520))
    assert not is_rate_limit_exception(GalaxyError(None, "foo", None, 403))



# Generated at 2022-06-12 22:01:46.977687
# Unit test for function g_connect
def test_g_connect():
    from ansible_galaxy_cli.api import collections_api

    # Set up fake GalaxyServer
    # Note: No actual HTTP/HTTPS requests are made so no need to mock them here.
    server = collections_api.GalaxyServer('http://fake.galaxy.com')
    server._available_api_versions = {}

    @g_connect([u'v1', u'v2'])
    def method(self):
        return self

    assert server == method(server)
    server._available_api_versions[u'v2'] = 'v2/'
    assert server == method(server)
    server._available_api_versions[u'v1'] = 'v1/'
    assert server == method(server)

    # No version requirement
    server._available_api_versions = {}


# Generated at 2022-06-12 22:01:59.094998
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError('http://galaxy.ansible.com', 404, 'Not found', {}, None)
    url_split = http_error.geturl().split('/')
    if 'v2' in url_split:
        http_error_msg = json.dumps({'message': 'HTTP Error 404: Not found', 'code': '404'})
    elif 'v3' in url_split:
        http_error_msg = json.dumps({'errors': [{'detail': 'HTTP Error 404: Not found', 'code': '404'}]})
    else:
        http_error_msg = json.dumps({'default': 'HTTP Error 404: Not found'})
    http_error.read = lambda: http_error_msg

# Generated at 2022-06-12 22:02:07.507500
# Unit test for function get_cache_id
def test_get_cache_id():
    """Unit test for get_cache_id."""
    assert get_cache_id('http://www.ansible.com') == 'www.ansible.com:'
    assert get_cache_id('http://www.ansible.com:8080') == 'www.ansible.com:8080'
    assert get_cache_id('https://www.ansible.com') == 'www.ansible.com:'
    assert get_cache_id('http://example.com:8080') == 'example.com:8080'


# Generated at 2022-06-12 22:02:14.853915
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    message = "message"
    http_code = 404
    http_error = HTTPError("http://localhost/v2/api/", http_code, message, None, None)
    err = GalaxyError(http_error, message)
    assert err.http_code == http_code
    assert err.url == "http://localhost/v2/api/"
    assert err.message == "(HTTP Code: %d, Message: %s)" % (http_code, message)



# Generated at 2022-06-12 22:02:25.768891
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    h = HTTPError('https://galaxy.ansible.com/api/v3/',
                  500, 'Internal Server Error', {}, None)
    e = GalaxyError(h, 'meh.')
    assert e.http_code == 500
    assert e.url == 'https://galaxy.ansible.com/api/v3/'
    assert e.message == 'meh. (HTTP Code: 500, Message: Internal Server Error Code: Unknown)'

    h = HTTPError('https://galaxy.ansible.com/api/v2/',
                  500, 'Internal Server Error', {}, None)
    e = GalaxyError(h, 'meh.')
    assert e.http_code == 500
    assert e.url == 'https://galaxy.ansible.com/api/v2/'
    assert e.message

# Generated at 2022-06-12 22:02:33.840351
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api = GalaxyAPI(auth_token="auth_token",
                           ignore_certs=False,
                           force=False,
                           server="server",
                           skip_issues=None,
                           api_server="api_server")
    other = GalaxyAPI(auth_token="auth_token",
                      ignore_certs=False,
                      force=False,
                      server="server",
                      skip_issues=None,
                      api_server="api_server")

    galaxy_api.name = None
    other.name = "other"
    # GalaxyAPI(auth_token='auth_token', ignore_certs=False, force=False, server='server',
    #  skip_issues=None, api_server='api_server', name=None) < GalaxyAPI(auth_token='auth_token',
    # ignore

# Generated at 2022-06-12 22:02:37.503037
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError(http_code=429))
    assert is_rate_limit_exception(GalaxyError(http_code=520))
    assert not is_rate_limit_exception(GalaxyError(http_code=403))



# Generated at 2022-06-12 22:02:40.156995
# Unit test for function get_cache_id
def test_get_cache_id():
    url = "http://galaxy.ansible.com/api/"
    result = get_cache_id(url)
    assert result == "galaxy.ansible.com:" 


# Generated at 2022-06-12 22:02:44.487592
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    a = GalaxyAPI('foo', 'foo.com')
    b = GalaxyAPI('bar', 'bar.com')

    assert a.__lt__(b) is True
    assert b.__lt__(a) is False

    a.name = 'bar'
    assert a.__lt__(b) is False
    assert b.__lt__(a) is False



# Generated at 2022-06-12 22:02:48.857627
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    error = GalaxyError("", http_code=429)
    assert is_rate_limit_exception(error)
    error = GalaxyError("", http_code=520)
    assert is_rate_limit_exception(error)
    error = GalaxyError("", http_code=400)
    assert not is_rate_limit_exception(error)
    error = GalaxyError("", http_code=403)
    assert not is_rate_limit_exception(error)

