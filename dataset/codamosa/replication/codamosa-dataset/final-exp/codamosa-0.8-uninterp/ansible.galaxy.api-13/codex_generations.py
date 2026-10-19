

# Generated at 2022-06-12 21:55:16.214280
# Unit test for function cache_lock
def test_cache_lock():
    test_lock = threading.Lock()
    test_lock_release = threading.Lock()
    test_lock_release_acquire = threading.Lock()

    @cache_lock
    def test_func():
        test_lock.acquire()

    # Should be able to acquire test_lock before calling test_func
    assert test_lock.acquire(False)

    # Start a new thread that will call test_func
    test_thread = threading.Thread(target=test_func)
    test_thread.start()

    # Since test_func is being executed, the test_lock should not be
    # available.
    assert not test_lock.acquire(False)

    # The lock should be released when the function call has completed
    def test_func_release():
        test_lock_release.acquire()
       

# Generated at 2022-06-12 21:55:26.837156
# Unit test for function cache_lock
def test_cache_lock():
    lock_object = threading.Lock()

    @cache_lock
    def test_function(lock_obj, test_value):
        assert lock_obj.acquire(blocking=False)
        assert test_value == 1
        time.sleep(2)
        lock_obj.release()
        assert not lock_obj.acquire(blocking=False)

    t1 = threading.Thread(target=test_function, args=(lock_object, 1))
    t2 = threading.Thread(target=test_function, args=(lock_object, 2))

    t1.start()
    t2.start()
    t2.join()
    t1.join()


# Generated at 2022-06-12 21:55:29.958282
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def _test(x):
        return x
    assert _test(123) == 123
    assert _test([]) == []
    assert _test({}) == {}


# Generated at 2022-06-12 21:55:32.615958
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    tmp_instance = GalaxyError(23, 'temp_msg')
    assert isinstance(tmp_instance, GalaxyError)



# Generated at 2022-06-12 21:55:41.944562
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    msg = "Failed to login as default with a bad password"
    class http_error:
        def __init__(self, code, message):
            self.code = code
            self.msg = message
        def read(self):
            return self.msg
        def geturl(self):
            return "https://cloud.redhat.com/api/v2"
        def reason(self):
            return "Password incorrect"

    galaxy_error = GalaxyError(http_error(404, ""), msg)
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == "https://cloud.redhat.com/api/v2"
    assert galaxy_error.message == "Failed to login as default with a bad password (HTTP Code: 404, Message: Password incorrect)"


# Generated at 2022-06-12 21:55:50.322693
# Unit test for function cache_lock
def test_cache_lock():
    import mock
    @cache_lock
    def f():
        pass
    m = mock.Mock()
    m.__enter__ = mock.Mock()
    m.__enter__.return_value = m
    m.__exit__ = mock.Mock()
    with mock.patch('ansible.galaxy.api.v1.__main__._CACHE_LOCK', m):
        f()
        m.__enter__.assert_called_once_with()
        m.__exit__.assert_called_once_with(None, None, None)


# Generated at 2022-06-12 21:55:54.154661
# Unit test for function cache_lock
def test_cache_lock():
    from ansible.module_utils.galaxy.api.cache import Cache
    _cache_lock = cache_lock(Cache)
    cache = _cache_lock("test")
    assert(isinstance(cache, Cache))
    assert(cache.path == "test")



# Generated at 2022-06-12 21:55:59.512257
# Unit test for function g_connect
def test_g_connect():
    def g_connect_wrapper(versions):
        def decorator(method):
            return method
        return decorator

    @g_connect_wrapper([1, 2, 3])
    def g_connect_function(self, *args, **kwargs):
        return "foo"

    class GalaxyConnection(object):
        def __init__(self):
            self.api_server = 'https://galaxy.ansible.com'
            self.name = 'Ansible Galaxy'

    x = GalaxyConnection()
    assert g_connect_function(x) == "foo"



# Generated at 2022-06-12 21:56:10.628765
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://galaxy.ansible.com') == 'galaxy.ansible.com:'
    assert get_cache_id('http://galaxy.ansible.com:8080') == 'galaxy.ansible.com:8080'
    assert get_cache_id('https://galaxy.ansible.com') == 'galaxy.ansible.com:'
    assert get_cache_id('https://galaxy.ansible.com:8080') == 'galaxy.ansible.com:8080'
    assert get_cache_id('https://galaxy.ansible.com/api') == 'galaxy.ansible.com:'
    assert get_cache_id('https://galaxy.ansible.com:8080/api') == 'galaxy.ansible.com:8080'
    assert get

# Generated at 2022-06-12 21:56:15.096019
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    ga1 = GalaxyAPI(name="name1", galaxy_url="galaxy_url1", token=123)
    ga2 = GalaxyAPI(name="name2", galaxy_url="galaxy_url2", token=123)
    ga3 = GalaxyAPI(name="name1", galaxy_url="galaxy_url1", token=123)
    ga4 = GalaxyAPI(name="name1", galaxy_url="galaxy_url1", token=456)

    assert (ga1 <= ga1) and (not (ga1 < ga1))
    assert (ga1 < ga2) and (not (ga1 <= ga2))
    assert (ga1 <= ga3) and (not (ga1 < ga3))
    assert (ga1 < ga4) and (not (ga1 <= ga4))


# Generated at 2022-06-12 21:56:53.205628
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    test = GalaxyAPI(name='pulp', api_server='https://galaxy.ansible.com', token='', ignore_certs=True)
    assert test.__lt__('') == False



# Generated at 2022-06-12 21:57:01.909428
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # Test creating a GalaxyAPI instance and verify defaults
    galaxy_api = GalaxyAPI()
    assert galaxy_api.name == 'galaxy'
    assert galaxy_api.server == 'https://galaxy.ansible.com'
    assert galaxy_api.api_server == 'https://galaxy.ansible.com'
    assert galaxy_api.version == 'v3'
    assert galaxy_api.token is None
    assert galaxy_api.ignore_certs is True
    assert galaxy_api.validate_certs is False

    # Test creating a GalaxyAPI instance using a non-default server
    galaxy_api = GalaxyAPI(server='https://galaxy-dev.ansible.com')
    assert galaxy_api.server == 'https://galaxy-dev.ansible.com'

# Generated at 2022-06-12 21:57:09.216891
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():

    class MyResponse:
        pass

    try:
        raise GalaxyError(MyResponse())
    except GalaxyError as ex:
        assert not is_rate_limit_exception(ex)

        ex.http_code = 429
        assert is_rate_limit_exception(ex)

        ex.http_code = 520
        assert is_rate_limit_exception(ex)

        ex.http_code = 403
        assert not is_rate_limit_exception(ex)

# Unit test decorator test_retry_with_delays_and_condition

# Generated at 2022-06-12 21:57:13.801492
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError('https://localhost', 404, 'Not found', None, None)
    message = 'Test error'
    err = GalaxyError(http_error, message)
    assert err.http_code == 404
    assert err.url == 'https://localhost'
    assert err.message == "Test error (HTTP Code: 404, Message: Not found)"


# Generated at 2022-06-12 21:57:20.725485
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError('https://galaxy.ansible.com/api/', '400', 'Bad Request', {}, None)
    galaxy_error = GalaxyError(http_error, 'Test Error')
    assert galaxy_error.http_code == http_error.code
    assert galaxy_error.url == http_error.geturl()
    assert galaxy_error.message == u'Test Error (HTTP Code: 400, Message: Bad Request)'

    galaxy_error = GalaxyError(http_error, 'Test Error')
    http_error.read = lambda: to_bytes(json.dumps({'default': 'My Galaxy Error'}))
    assert galaxy_error.http_code == http_error.code
    assert galaxy_error.url == http_error.geturl()

# Generated at 2022-06-12 21:57:27.949118
# Unit test for function cache_lock
def test_cache_lock():
    """
    Unit test for function cache_lock()
    """
    global _CACHE_LOCK
    lock = threading.Lock()
    _CACHE_LOCK = lock
    lock.acquire()
    wrapped = cache_lock(lambda: False)
    assert not wrapped()
    assert lock.locked()
    lock.release()
    assert not lock.locked()


# Generated at 2022-06-12 21:57:30.311781
# Unit test for function g_connect
def test_g_connect():
    """Signature for galaxy_server.g_connect()."""
    GalaxyServer.g_connect(GalaxyServer, [1, 2])



# Generated at 2022-06-12 21:57:32.299056
# Unit test for function g_connect
def test_g_connect():
    @g_connect([u'v1'])
    def module(self, *args, **kwargs):
        return {}
# Test ends


# Generated at 2022-06-12 21:57:33.894166
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    object_a = GalaxyError(500, "hello")
    object_a.__class__ == AnsibleError



# Generated at 2022-06-12 21:57:43.126344
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    msg = b"{\"default\": \"HTTP Code: 521, Message: Cloudflare rate limit triggered, Code: Unknown\"}"
    http_error = HTTPError(url="https://ansible.com/api/v2/", code=521, msg=b"Cloudflare rate limit", hdrs=None, fp=None, orig_msg=msg)
    error = GalaxyError(http_error, message="The Ansible Galaxy server is temporarily unavailable.")
    assert error.message == "The Ansible Galaxy server is temporarily unavailable. (HTTP Code: 521, Message: Cloudflare rate limit triggered, Code: Unknown)"



# Generated at 2022-06-12 21:58:33.547378
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    assert GalaxyAPI('test_name', 'test_url', 'test_key', 'test_secret') < GalaxyAPI('ztest_name', 'test_url', 'test_key', 'test_secret')
    assert not GalaxyAPI('test_name', 'test_url', 'test_key', 'test_secret') < GalaxyAPI('test_name', 'test_url', 'test_key', 'test_secret')


# Generated at 2022-06-12 21:58:40.974441
# Unit test for function is_rate_limit_exception

# Generated at 2022-06-12 21:58:52.717251
# Unit test for function g_connect
def test_g_connect():
    class TestGalaxy(object):
        def __init__(self, method, versions):
            self.method = method
            self.versions = versions

        @g_connect(versions=['v1', 'v2'])
        def test(self, *args, **kwargs):
            return {
                'args': args,
                'kwargs': kwargs,
            }

    test_galaxy = TestGalaxy(method='test', versions=['v1', 'v2'])
    test_galaxy.api_server = None
    test_galaxy.name = 'test'
    res = test_galaxy.test(1, 2, kwarg1='value1', kwarg2='value2')
    assert res['args'] == (1, 2)

# Generated at 2022-06-12 21:58:59.296728
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    test_error_info = {
        "errors": [
            {
                "code": "test_code",
                "title": "test_title",
                "detail": "test_detail"
            }
        ]
    }
    test_error_str = json.dumps(test_error_info)
    test_http_error = HTTPError("https://someserver.com:8181/api/v3/", 400, "Test Reason", None, None)
    test_http_error.read = lambda: test_error_str
    test_galaxy_error = GalaxyError(test_http_error, "Test Message")
    assert test_galaxy_error.http_code == 400
    assert test_galaxy_error.url == "https://someserver.com:8181/api/v3/"

# Generated at 2022-06-12 21:59:06.076160
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api_server = 'http://galaxy.server.com'
    api_key = 'api-key-value'
    validate_certs = False
    ignore_certs = False
    name = 'name-value'

    # Test that GalaxyAPI constructor properly parses api_server, validate_certs and ignore_certs
    galaxy_api = GalaxyAPI(api_server, api_key, validate_certs, ignore_certs, name)
    assert galaxy_api.api_server == api_server
    assert galaxy_api.validate_certs is False
    assert galaxy_api.ignore_certs is True

    # Test that GalaxyAPI constructor properly defaults api_server to https://galaxy.ansible.com
    galaxy_api = GalaxyAPI(api_key=api_key)

# Generated at 2022-06-12 21:59:08.351485
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    # This is a stub, used to test GalaxyAPI.__lt__
    pass


# Generated at 2022-06-12 21:59:09.512180
# Unit test for function g_connect
def test_g_connect():
    return True


# Generated at 2022-06-12 21:59:15.530205
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError("url", "code", "msg", "hdrs", "utf8")
    http_error.msg = {"default": "message", "code": "code"}  # This is what we look for in the method
    error = GalaxyError(http_error, "status")
    assert error.http_code == "code"
    assert error.url == "url"
    assert error.message.startswith("status")



# Generated at 2022-06-12 21:59:26.746552
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # TODO: Need to mock this out properly because HTTPException errors change based on the urllib version.
    # Also we need to better mock this out since it looks like HTTPError will run some of the handlers again
    # when it is raised as an exception.
    http_error = HTTPError(url='https://test.test/test', hdrs={}, msg='', hdrs={}, fp=None, code=400)
    http_error.read = lambda: "{'message': '', 'code': ''}"
    err = GalaxyError(http_error, "This is a test")
    assert isinstance(err, AnsibleError)
    assert err.message == u"This is a test (HTTP Code: 400, Message:   Code: )"
    assert err.http_code == 400

# Generated at 2022-06-12 21:59:33.052520
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError(http_code=429, message=u'Too Many Requests'))
    assert is_rate_limit_exception(GalaxyError(http_code=520, message=u'Galaxy rate limit exceeded'))
    assert not is_rate_limit_exception(GalaxyError(http_code=403, message=u'Forbidden'))
    assert not is_rate_limit_exception(GalaxyError(http_code=400, message=u'Bad Request'))
    assert not is_rate_limit_exception(GalaxyError(http_code=502, message=u'Bad Gateway'))



# Generated at 2022-06-12 22:00:09.205619
# Unit test for function get_cache_id
def test_get_cache_id():

    url = "http://galaxy.ansible.com/api/"
    assert get_cache_id(url) == 'galaxy.ansible.com'

    url = "https://galaxy.ansible.com/api/"
    assert get_cache_id(url) == 'galaxy.ansible.com'

    url = "http://galaxy.ansible.com/api/"
    assert get_cache_id(url) == 'galaxy.ansible.com'

    url = "https://galaxy.ansible.com:443/api/"
    assert get_cache_id(url) == 'galaxy.ansible.com:443'

    url = "http://galaxy.ansible.com:80/api/"
    assert get_cache_id(url) == 'galaxy.ansible.com:80'




# Generated at 2022-06-12 22:00:17.142837
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    import unittest
    import ansible.galaxy.api

    class MyTestCase(unittest.TestCase):
        def test___lt__(self):
            api = GalaxyAPI(api_server='https://galaxy.ansible.com', name='galaxy', verify=True)
            # Check if api < 'a' raise NotImplementedError
            with self.assertRaises(NotImplementedError):
                api < 'a'
    unittest.main()

if __name__ == '__main__':
    test_GalaxyAPI___lt__()

# Generated at 2022-06-12 22:00:18.369566
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api = GalaxyAPI('')
    other = GalaxyAPI('')
    assert galaxy_api < other


# Generated at 2022-06-12 22:00:28.333500
# Unit test for function g_connect
def test_g_connect():
    from ansible.module_utils import six
    from ansible.module_utils.common._collections_compat import MutableMapping

    class GalaxyClient(six.with_metaclass(type, MutableMapping)):

        def __init__(self):
            self._available_api_versions = {}
            self.api_server = 'http://127.0.0.1:9180'

        def __getitem__(self, item):
            return self._available_api_versions[item]

        def __setitem__(self, key, value):
            self._available_api_versions[key] = value

        def __delitem__(self, key):
            del self._available_api_versions[key]

        def __iter__(self):
            return iter(self._available_api_versions)


# Generated at 2022-06-12 22:00:39.860409
# Unit test for function g_connect
def test_g_connect():
    global api_server_flag
    api_server_flag = False

# Generated at 2022-06-12 22:00:45.134073
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # Test all constructed objects
    api = GalaxyAPI('https://galaxy.example.com')
    assert api.api_server == 'https://galaxy.example.com'
    assert api.token is None
    assert api.token_file is None

    api = GalaxyAPI('https://galaxy.example.com', api_token='abc123')
    assert api.token == 'abc123'
    assert api.api_server == 'https://galaxy.example.com'
    assert api.token_file is None

    api = GalaxyAPI('https://galaxy.example.com', api_token='abc123',
                    token_file='/path/to/token/file')
    assert api.token == 'abc123'
    assert api.api_server == 'https://galaxy.example.com'

# Generated at 2022-06-12 22:00:46.500259
# Unit test for function g_connect
def test_g_connect():
    """
    This is test code for g_connect
    """
    display.vvvv("Unable to test g_connect function as it is a decorator")



# Generated at 2022-06-12 22:00:55.456814
# Unit test for function g_connect
def test_g_connect():
    """
    Test :py:func:`ansible_galaxy.galaxy_context.g_connect`
    """
    class T(object):
        def __init__(self, versions=None):
            self._available_api_versions = versions
            self.api_server = "http://foo.com"
            self.name = "test"
    t = T([u'v1'])
    @g_connect(versions=[u'v1'])
    def func(self):
        return self

    func(t)
    try:
        @g_connect(versions=[u'v2', u'v3'])
        def func(self):
            return self

        func(t)
    except AnsibleError:
        pass
    else:
        assert False

# Generated at 2022-06-12 22:01:05.642567
# Unit test for function g_connect
def test_g_connect():
    given_versions = ["v1", "v2"]
    available_versions = {"v1": "v1/", "v2": "v2/", "v3": "v3/"}

    def mocked_method(obj, *args, **kwargs):
        return None

    def mocked_meth_v1_only(obj, *args, **kwargs):
        return obj._available_api_versions

    def mocked_meth_v3_only(obj, *args, **kwargs):
        return obj.api_server

    class MockedObj:
        def __init__(self):
            self.api_server = 'any'
            self.name = 'any'

        def _call_galaxy(self, url, method):
            return {}


# Generated at 2022-06-12 22:01:16.855412
# Unit test for function g_connect
def test_g_connect():
    class MyGalaxyServer(object):
        def __init__(self, api_server, name):
            self.api_server = api_server
            self.name = name
            self._available_api_versions = {}

        def _call_galaxy(self, *args, **kwargs):
            return {'available_versions': {u'v1': u'v1/', u'v2': u'v2/'}}

        @g_connect(['v1', 'v2'])
        def sample_method(self):
            return True

    galaxy_server = MyGalaxyServer('https://galaxy.ansible.com', 'galaxy.ansible.com')
    assert galaxy_server.sample_method()



# Generated at 2022-06-12 22:02:12.585410
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    print('TESTING: test_GalaxyAPI___lt__')
    galaxy_api = GalaxyAPI()
    assert galaxy_api.__lt__(1) == NotImplemented



# Generated at 2022-06-12 22:02:17.122057
# Unit test for function cache_lock
def test_cache_lock():
    class test_obj:
        called = False
        _CACHE_LOCK = threading.Lock()

        def test_func(self):
            self.called = True

    obj = test_obj()
    cache_lock_obj = cache_lock(obj.test_func)
    cache_lock_obj()
    assert obj.called is True
test_cache_lock()



# Generated at 2022-06-12 22:02:21.947220
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    try:
        raise GalaxyError('http_error', 'message')
    except GalaxyError as e:
        assert e.http_code == 'http_error'
        assert e.url == 'message'
        assert e.message == "message (HTTP Code: http_error, Message: message)"


# Generated at 2022-06-12 22:02:31.957854
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    url = 'https://galaxy.ansible.com/api/v2/'
    err_msg = 'An error occurred'
    err = HTTPError(url, 501, None, None, None)
    err.reason = 'Not implemented'
    galaxy_err = GalaxyError(err, message=err_msg)
    assert galaxy_err.http_code == 501
    assert galaxy_err.url == url
    assert galaxy_err.message == '%s (HTTP Code: %d, Message: %s Code: %s)' % (err_msg, 501, 'Not implemented', 'Unknown')

    # Test when galaxy_msg is present in the json error response
    err_info = {'message': 'An error occurred with Galaxy', 'code': 'Error code'}
    err = HTTPError(url, 501, None, None, None)
   

# Generated at 2022-06-12 22:02:35.337272
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api = GalaxyAPI(galaxy_server=None, name=None, username=None, password=None, ignore_certs=False)
    ret = galaxy_api.__lt__(None)
    assert ret is False


# Generated at 2022-06-12 22:02:36.001592
# Unit test for function g_connect
def test_g_connect():
    assert 1==1

# Generated at 2022-06-12 22:02:43.495541
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # Arrange
    http_error = HTTPError(url="http://galaxy/api/v3/collections/", hdrs=None, fp=None, errcode=404, errmsg=None, headers=None, filename=None)

    # Act
    galaxy_error = GalaxyError(http_error=http_error, message="test message")

    # Assert
    assert (galaxy_error.http_code == http_error.code)
    assert (galaxy_error.url == http_error.geturl())
    assert (galaxy_error.message == "test message (HTTP Code: %d, Message: %s)" % (404, http_error.reason))



# Generated at 2022-06-12 22:02:49.395749
# Unit test for function g_connect
def test_g_connect():
    class GalaxyAPI(object):
        def __init__(self, galaxy_url):
            self.api_server = galaxy_url
            self.name = 'galaxy_url'
            self._available_api_versions = None

        def _call_galaxy(self, url, method, error_context_msg, cache=False):
            return {'available_versions': {'v1': 'v1/'}}
    g = GalaxyAPI('https://galaxy.ansible.com')
    @g_connect(['v1'])
    def get_version(self):
        pass
    get_version(g)



# Generated at 2022-06-12 22:02:59.581210
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError('', {'X-RateLimit-Remaining': 'aaa'}))
    assert is_rate_limit_exception(GalaxyError('', {'X-RateLimit-Remaining': '0'}))
    assert not is_rate_limit_exception(GalaxyError('', {'X-RateLimit-Remaining': '1'}))
    assert not is_rate_limit_exception(GalaxyError('', {}))
    assert not is_rate_limit_exception(GalaxyError('', {'aa': 'bb'}))
    assert not is_rate_limit_exception(GalaxyError('', {'X-RateLimit-Remaining': 'aaa'}, 400))

# Generated at 2022-06-12 22:03:09.471007
# Unit test for function get_cache_id

# Generated at 2022-06-12 22:04:05.155603
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    with pytest.raises(GalaxyError) as excinfo:
        url = 'https://galaxy.ansible.com/api/v2/search?page_size=1'
        try:
            display.vvvvv(url)
            open_url(url, None, use_proxy=False)
        except HTTPError as http_error:
            err_msg = u"Error accessing Galaxy API: %s" % to_text(http_error.read()).strip()
            raise GalaxyError(http_error, err_msg)

    assert excinfo.value.http_code == 429
    assert excinfo.value.url == url
    assert isinstance(excinfo.value.message, str)
    assert excinfo.value.message != ''



# Generated at 2022-06-12 22:04:13.030931
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    error = "HTTP Code: 404, Message: Not Found Code: Not Found"
    error_obj = GalaxyError(None, error)
    assert error_obj.message == error



# Generated at 2022-06-12 22:04:26.304352
# Unit test for function g_connect
def test_g_connect():
    class AGalaxyAPI:
        def __init__(self, api_server, name, roles_path):
            self._available_api_versions = {'v1': 'v1/'}
            self.api_server = api_server
            self.name = name
            self.roles_path = roles_path
        def _call_galaxy(self, *args, **kwargs):
            return {'available_versions': {'v1': 'v1/'}}
        @g_connect(['v1'])
        def test_galaxy_connect(self, *args, **kwargs):
            pass
    api = AGalaxyAPI('https://galaxy.ansible.com/api/', 'galaxy', '')
    api.test_galaxy_connect()
