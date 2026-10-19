

# Generated at 2022-06-12 21:55:25.222761
# Unit test for function get_cache_id
def test_get_cache_id():
    for url in ('https://galaxy.ansible.com', 'http://localhost:8080'):
        assert get_cache_id(url) == 'galaxy.ansible.com'
    assert get_cache_id('https://galaxy.ansible.com:80') == 'galaxy.ansible.com:80'
    assert get_cache_id('https://127.0.0.1:8080') == '127.0.0.1:8080'


# Generated at 2022-06-12 21:55:26.488440
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def inc(x):
        return x+1
    with _CACHE_LOCK:
        assert inc(4) == 5


# Generated at 2022-06-12 21:55:29.489548
# Unit test for function g_connect
def test_g_connect():
    versions = ['v1']
    def method(self, *args, **kwargs):
        print(kwargs)
    wrapped = g_connect(versions)(method)
    wrapped(None)



# Generated at 2022-06-12 21:55:35.674397
# Unit test for function get_cache_id
def test_get_cache_id():
    # TODO: Add a unit test for invalid URLs
    assert get_cache_id('http://localhost') == 'localhost'
    assert get_cache_id('http://localhost:9000') == 'localhost:9000'
    assert get_cache_id('https://localhost') == 'localhost'
    assert get_cache_id('https://localhost:9000') == 'localhost:9000'



# Generated at 2022-06-12 21:55:36.598865
# Unit test for function g_connect
def test_g_connect():
    assert g_connect(versions)



# Generated at 2022-06-12 21:55:44.113338
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # pylint: disable=too-few-public-methods
    class HttpError(object):
        def __init__(self, code, url, reason, msg):
            self.code = code
            self.url = url
            self.reason = reason
            self.msg = msg
        def geturl(self):
            return self.url
        def read(self):
            return self.msg

    # v1, not JSON
    http_error = HttpError(404, 'https://galaxy.ansible.com/api/v1', 'Not Found', 'default: Not Found')
    galaxy_error = GalaxyError(http_error, 'Could not find role foo')
    assert galaxy_error.http_code == 404

# Generated at 2022-06-12 21:55:48.144942
# Unit test for function get_cache_id
def test_get_cache_id():
    url = 'https://galaxy.ansible.com/api/v1/'
    test_cache_id = get_cache_id(url)
    assert test_cache_id == 'galaxy.ansible.com:443'


# Generated at 2022-06-12 21:55:50.105687
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    api1 = GalaxyAPI()
    api2 = GalaxyAPI()

    assert not api1 < api2



# Generated at 2022-06-12 21:55:58.709279
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # A test case of case 1, the error information of Galaxy can be retrieved.
    def test_case_1():
        err_info = {
            "default": "the default information of galaxy server",
        }
        http_error = HTTPError('https://xxx.xxx.xxx.xxx', status=503, reason='503 error', hdrs=None, fp=None,
                               errcode='503', _pool=None, _connection=None)
        message = 'the error should be GalaxyError'
        http_error.read = lambda: json.dumps(err_info)
        galaxy_error = GalaxyError(http_error, message)
        assert isinstance(galaxy_error, GalaxyError)
        assert galaxy_error.http_code == 503

# Generated at 2022-06-12 21:56:00.552959
# Unit test for function cache_lock
def test_cache_lock():
    with _CACHE_LOCK:
        assert 1


# Generated at 2022-06-12 21:56:55.880310
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('https://localhost:8081/v2/') == 'localhost:8081'
    assert get_cache_id('http://localhost:8081/v2/') == 'localhost:8081'
    assert get_cache_id('https://localhost/v2/') == 'localhost:'
    assert get_cache_id('http://localhost/v2/') == 'localhost:'
    assert get_cache_id('https://localhost/v2') == 'localhost:'
    assert get_cache_id('http://localhost/v2') == 'localhost:'
    assert get_cache_id('https://galaxy.ansible.com') == 'galaxy.ansible.com:'



# Generated at 2022-06-12 21:56:59.989643
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    class MockHTTPResponse(object):
        def __init__(self, http_code=200):
            self.http_code = http_code

    # Test public constructor
    galaxy_api = GalaxyAPI(server='https://api.galaxy.ansible.com', token='token')
    assert galaxy_api is not None
    assert galaxy_api.api_server == 'https://api.galaxy.ansible.com'
    assert galaxy_api.token == 'token'
    assert galaxy_api.name == 'galaxy'

    # Test Galaxy API with a mocked out API response.  The response is empty but the logic still
    # verifies the API is reachable.
    class MockHTTPConnection(object):
        def __init__(self, host):
            pass


# Generated at 2022-06-12 21:57:05.381903
# Unit test for function g_connect
def test_g_connect():
    # This function doesn't return anything, so we can't test it in a normal way
    # For now, we just assert that the wrapper function is returned
    # TODO(jamielennox): look into how we can test this

    @g_connect([u'v2'])
    def test_func(self, *args, **kwargs):
        return 42

    assert test_func.__name__ == 'wrapped'
    assert test_func.__doc__ == 'Wrapper to lazily initialize connection info to Galaxy and verify the API versions required are available on the endpoint. '



# Generated at 2022-06-12 21:57:11.585971
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    """
    Tests the behavior of the GalaxyAPI constructor.
    """
    base_api = GalaxyAPI(server_list=['https://galaxy.ansible.com'])

    assert base_api.api_server == u'https://galaxy.ansible.com'
    assert base_api.api_token is None
    assert base_api.ignore_certs is False
    assert 'v2' in base_api.available_api_versions
    assert 'v3' not in base_api.available_api_versions
    assert base_api.insecure_skip_verify is False
    assert base_api.name == u'galaxy_server'

    token_api = GalaxyAPI(server_list=['https://galaxy.ansible.com'], api_token='foo')

    assert token_api.api_server == u

# Generated at 2022-06-12 21:57:19.290994
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('https://galaxy.server/api/v2/collections/') == 'galaxy.server'
    assert get_cache_id('https://galaxy.server:8080/api/v2/collections/') == 'galaxy.server:8080'
    assert get_cache_id('https://user:password@galaxy.server/api/v2/collections/') == 'galaxy.server'
    assert get_cache_id('https://user:password@galaxy.server:8080/api/v2/collections/') == 'galaxy.server:8080'
    assert get_cache_id('https://user@galaxy.server/api/v2/collections/') == 'galaxy.server'

# Generated at 2022-06-12 21:57:23.886127
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError(http_code=429))
    assert is_rate_limit_exception(GalaxyError(http_code=520))
    assert not is_rate_limit_exception(GalaxyError(http_code=403))
    assert not is_rate_limit_exception(GalaxyError(http_code=404))
    assert not is_rate_limit_exception(GalaxyError(http_code=500))



# Generated at 2022-06-12 21:57:34.371998
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # pylint: disable=protected-access
    api = GalaxyAPI('https://galaxy.ansible.com', 'username', 'password', validate_certs=False)
    assert api.api_server == b'https://galaxy.ansible.com'
    assert api.username == 'username'
    assert api.password == 'password'
    assert api.token is None
    assert api.validate_certs is False

    api = GalaxyAPI('https://galaxy.ansible.com', 'token_value')
    assert api.api_server == b'https://galaxy.ansible.com'
    assert api.username is None
    assert api.password is None
    assert api.token == 'token_value'

    api = GalaxyAPI('https://galaxy.ansible.com/custom/')
    assert api.api

# Generated at 2022-06-12 21:57:46.534593
# Unit test for function get_cache_id
def test_get_cache_id():
    test_cases = [
        ('https://foo.com', ('foo.com', '')),
        ('https://foo.com/api', ('foo.com', '')),
        ('https://foo.com:443', ('foo.com:443', '')),
        ('https://foo.com:443/api', ('foo.com:443', '')),
        ('https://foo:redhat@foo.com', ('foo.com', '')),
        ('https://foo:redhat@foo.com/api', ('foo.com', '')),
        ('https://foo:redhat@foo.com:443', ('foo.com:443', '')),
        ('https://foo:redhat@foo.com:443/api', ('foo.com:443', '')),
    ]

    for url, expected_output in test_cases:
        output = get

# Generated at 2022-06-12 21:57:49.513757
# Unit test for function g_connect
def test_g_connect():
    def a(self):
        return 1

    b = g_connect([1, 2])(a)
    assert b(None) == 1

    b = g_connect([1, 2])(a)
    assert b(None) == 1



# Generated at 2022-06-12 21:57:55.390374
# Unit test for function g_connect
def test_g_connect():
    def f(self, *args, **kwargs):
        return self

    f = g_connect(['v1', 'v2'])(f)
    assert f.__name__ == 'wrapped'
    assert (f.__doc__ == None or f.__doc__ == 'wrapped')
    assert f.__module__ == 'ansible.galaxy.api'



# Generated at 2022-06-12 21:58:31.361215
# Unit test for function g_connect
def test_g_connect():
    try:
        p = GalaxyInterface(token=None, server='cloud.redhat.com', force_api_version=False)
        r = p._call_galaxy('/api/v2/roles/')
        assert r.get('count') > 0
    except Exception as e:
        raise e


# Generated at 2022-06-12 21:58:33.153416
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    a = GalaxyError(test_HTTPError, 'test')
    assert isinstance(a, GalaxyError)



# Generated at 2022-06-12 21:58:37.133523
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = "test_http_error"
    message = "test_message"
    galaxy_error = GalaxyError(http_error, message)
    assert galaxy_error.http_code == http_error.code
    assert galaxy_error.url == http_error.geturl()
    assert galaxy_error.message == galaxy_error.message


# Generated at 2022-06-12 21:58:42.012678
# Unit test for function cache_lock
def test_cache_lock():
    x = 0
    def f():
        nonlocal x
        x += 1

    def g():
        nonlocal x
        x -= 1

    f()
    f()
    g()
    assert x == 1

    cached_f = cache_lock(f)
    cached_g = cache_lock(g)
    cached_f()
    cached_f()
    cached_g()
    assert x == 1


# ---
# Cache management

# Generated at 2022-06-12 21:58:49.821222
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    test_message = "Test Message"
    error = HTTPError(None, None, None, None, None)
    error.read = lambda : "{}"
    error.reason = "Test Reason"
    error.code = 200
    galaxy_error = GalaxyError(error, test_message)
    assert(galaxy_error.message.startswith(test_message))
    assert(galaxy_error.http_code == 200)
    assert(galaxy_error.url is None)


# Generated at 2022-06-12 21:58:57.747060
# Unit test for function g_connect
def test_g_connect():
    versions = ['v1', 'v2']
    method = 'ansible.galaxy.api'
    if not wrapped.available_api_versions:
        display.vvvv("Initial connection to galaxy_server: %s" % wrapped.api_server)

        # Determine the type of Galaxy server we are talking to. First try it unauthenticated then with Bearer
        # auth for Automation Hub.
        n_url = wrapped.api_server
        error_context_msg = 'Error when finding available api versions from %s (%s)' % (wrapped.name, n_url)

        if wrapped.api_server == 'https://galaxy.ansible.com' or wrapped.api_server == 'https://galaxy.ansible.com/':
            n_url = 'https://galaxy.ansible.com/api/'


# Generated at 2022-06-12 21:59:08.051278
# Unit test for function g_connect
def test_g_connect():
    """
    Test Galaxy class function initializing connection info to Galaxy.
    """
    display.vvvv("Initializing test_g_connect")
    fakeGalaxyClass = DummyGalaxyClass()
    versions = ['v2']
    testGalaxyClass = g_connect(versions)(fakeGalaxyClass.method1)
    testGalaxyClass()
    assert testGalaxyClass.__name__ == "method1"
    assert len(fakeGalaxyClass.galaxy_instances) == 1
    for galaxy_instance in fakeGalaxyClass.galaxy_instances:
        assert galaxy_instance.name == "test" and galaxy_instance.api_server == "http://test.com"
    display.vvvv("Completed test_g_connect")


# Generated at 2022-06-12 21:59:19.771608
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    galaxy = GalaxyAPI('https://galaxy.example.org', 'v2')
    assert 'v2' in galaxy.available_api_versions
    assert len(galaxy.available_api_versions) == 1

    galaxy = GalaxyAPI('https://galaxy.example.org', 'v2,v3')
    assert 'v2' in galaxy.available_api_versions
    assert 'v3' in galaxy.available_api_versions
    assert len(galaxy.available_api_versions) == 2

    galaxy = GalaxyAPI('https://galaxy.example.org', 'v2, v3')
    assert 'v2' in galaxy.available_api_versions
    assert 'v3' in galaxy.available_api_versions
    assert len(galaxy.available_api_versions) == 2

    # On error GalaxyAPI should set version to

# Generated at 2022-06-12 21:59:29.566058
# Unit test for function g_connect
def test_g_connect():
    # Arrange
    from ansible.galaxy import api
    from ansible.galaxy.api import GalaxyError

    versions = ['v1']
    my_self = api.GalaxyAPI('https://galaxy.ansible.com/')
    my_self._available_api_versions = {}

    # Act
    @g_connect(versions)
    def my_method(self, *args, **kwargs):
        return "OK"

    # Assert
    try:
        assert my_method(my_self) == "OK"
        my_new_self = api.GalaxyAPI('https://galaxy.ansible.com/')
        assert my_method(my_new_self) == "OK"
    except GalaxyError as err:
        assert False, err



# Generated at 2022-06-12 21:59:41.770618
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('https://example.org') == 'example.org:'
    assert get_cache_id('https://example.org:') == 'example.org:'
    assert get_cache_id('https://example.org:1') == 'example.org:1'
    assert get_cache_id('https://example.org/') == 'example.org:'
    assert get_cache_id('https://example.org:1/') == 'example.org:1'
    assert get_cache_id('https://1.2.3.4') == '1.2.3.4:'
    assert get_cache_id('https://1.2.3.4:') == '1.2.3.4:'

# Generated at 2022-06-12 22:00:22.174535
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    try:
        api = GalaxyAPI(galaxy_server=u'https://galaxy.example.com', galaxy_token=u'ANSIBLE-API-TOKEN',
                        galaxy_user=u'admin', verify_ssl=False)
    except:
        raise
    else:
        assert api.api_server == u'https://galaxy.example.com', api.api_server
        assert api.api_token == u'ANSIBLE-API-TOKEN', api.api_token
        assert api.api_user == u'admin', api.api_user
        assert not api.verify_ssl, api.verify_ssl
        assert api.available_api_versions == {'v2': '/api/v2/', 'v3': '/api/v3/'}, api.available_api_versions

# Generated at 2022-06-12 22:00:27.327090
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    obj = GalaxyAPI(name='ansible_galaxy_net', api_server='https://galaxy.ansible.com')
    assert not obj.__lt__(GalaxyAPI(name='ansible_galaxy_net', api_server='https://galaxy.ansible.com'))

    assert obj.__lt__(GalaxyAPI(name='ansible_galaxy_net', api_server='https://galaxy_net'))
    assert not obj.__lt__(GalaxyAPI(name='ansible_galaxy_net', api_server='https://galaxy.ansible.io'))

    assert obj.__lt__(GalaxyAPI(name='ansible_galaxy', api_server='https://galaxy.ansible.com'))

# Generated at 2022-06-12 22:00:37.265219
# Unit test for function g_connect
def test_g_connect():
    # noinspection PyUnusedLocal
    @g_connect(versions=['v1', 'v2'])
    def common_versions(self, *args):
        pass

    # noinspection PyUnusedLocal
    @g_connect(versions=['v3'])
    def not_common_versions(self, *args):
        pass

    try:
        common_versions(None)
    except Exception as e:
        raise AssertionError(to_native(e))

    try:
        not_common_versions(None)
    except AnsibleError:
        pass
    else:
        raise AssertionError("Exception not raised for unknown API version")



# Generated at 2022-06-12 22:00:47.358834
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id("http://mygalaxy.com/") == "mygalaxy.com"
    assert get_cache_id("http://mygalaxy.com") == "mygalaxy.com"
    assert get_cache_id("http://mygalaxy.com:8080") == "mygalaxy.com:8080"
    assert get_cache_id("http://user:pass@mygalaxy.com") == "mygalaxy.com"
    assert get_cache_id("http://user:pass@mygalaxy.com/") == "mygalaxy.com"
    assert get_cache_id("http://user:pass@mygalaxy.com:8080") == "mygalaxy.com:8080"

# Generated at 2022-06-12 22:00:48.635579
# Unit test for function cache_lock
def test_cache_lock():
    with _CACHE_LOCK:
        return True
test_cache_lock()



# Generated at 2022-06-12 22:00:56.274480
# Unit test for function cache_lock
def test_cache_lock():
    lock_test_variable = 0
    def test_function():
        nonlocal lock_test_variable
        lock_test_variable += 1
    # Test that cache_lock is using a context manager
    cache_locked_function = cache_lock(test_function)
    with _CACHE_LOCK:
        cache_locked_function()
        assert lock_test_variable == 1
    with _CACHE_LOCK:
        cache_locked_function()
        assert lock_test_variable == 2
    with _CACHE_LOCK:
        cache_locked_function()
        assert lock_test_variable == 3



# Generated at 2022-06-12 22:01:03.058551
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
	galaxy_api = GalaxyAPI()
	galaxy_api.name = 'test_name'
	galaxy_api.api_server = 'test_api_server'
	galaxy_api.available_api_versions = {
		"test_api_version": "test_available_api_version",
	}
	assert not (galaxy_api < GalaxyAPI())
	assert not (GalaxyAPI() < galaxy_api)


# Generated at 2022-06-12 22:01:14.996639
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # Test creating a new Galaxy API instance
    # Ensure the initialized instance has the expected attributes set
    # and can make API calls
    api_example_com = GalaxyAPI(server="https://api.example.com", name="example API")
    assert api_example_com.name == "example API"
    assert api_example_com.api_server == "https://api.example.com"
    assert api_example_com.token == None
    assert api_example_com.verify_ssl == True
    assert api_example_com.ignore_certs == False
    assert api_example_com.cache is None
    assert api_example_com.available_api_versions == {}

    # Making API calls should raise an error before connect has been called

# Generated at 2022-06-12 22:01:20.327448
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
  # Test unauthed GalaxyAPI
  GalaxyAPI(server='server')

  # Test authed GalaxyAPI
  GalaxyAPI(server='server', api_key='api_key', ignore_certs=True)
  GalaxyAPI(server='server', username='username', password='password', ignore_certs=True)

  # Test missing required parameters to GalaxyAPI constructor
  with pytest.raises(AnsibleError):
    GalaxyAPI(server=None)


# Generated at 2022-06-12 22:01:27.592614
# Unit test for function g_connect
def test_g_connect():
    class MockGalaxyAPI(object):

        def __init__(self, api_server):
            self.name = u'Mock'
            self.api_server = api_server
            self._available_api_versions = None
            self._token = None

        def _call_galaxy(self, url, method='GET', data=None, error_context_msg=None, cache=True):
            if url == u'https://galaxy.ansible.com/api/':
                return {'available_versions': {u'v1': u'v1/', u'v2': u'v2/'}}
            elif url == u'https://cloud.redhat.com/api/':
                return {'available_versions': {u'v1': u'v1/'}}

# Generated at 2022-06-12 22:02:36.083857
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    exc = HTTPError("https://galaxy.ansible.com/api/v2/", 500, "Internal Server Error", None, None)
    assert GalaxyError(exc, "Error when finding available api versions from galaxy.ansible.com").message == "Error when finding available api versions from galaxy.ansible.com (HTTP Code: 500, Message: Internal Server Error)"


# Generated at 2022-06-12 22:02:37.794652
# Unit test for function cache_lock
def test_cache_lock():
    with cache_lock(cache_lock):
        assert cache_lock.__name__ == "wrapped"


# Generated at 2022-06-12 22:02:46.222729
# Unit test for function g_connect
def test_g_connect():
    class GalaxyTest:
        def __init__(self):
            self.api_server = 'http://galaxy.ansible.com'
            self.name = 'server'
            self._available_api_versions = {}

        def _call_galaxy(self, *args, **kwargs):
            return {'available_versions': {u'v1': u'v1/'}}

        @g_connect(['v1', 'v2'])
        def galaxy_v1_and_v2(self):
            return 1

        @g_connect(['v2', 'v3'])
        def galaxy_v2_and_v3(self):
            return 1

    g = GalaxyTest()

    assert g.galaxy_v1_and_v2() == 1

# Generated at 2022-06-12 22:02:48.887385
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id("http://galaxy.example.com/api/") == "galaxy.example.com:"
    assert get_cache_id("http://galaxy.example.com/api/v2") == "galaxy.example.com:"


# Generated at 2022-06-12 22:02:58.764000
# Unit test for function g_connect
def test_g_connect():
    class TestClass():
        """"""
        def __init__(self, api_server, name=''):
            self.api_server = api_server
            self.name = name
            self._available_api_versions = None

        @g_connect(versions=['v1', 'v2'])
        def test(self, *args, **kwargs):
            """"""
            pass

    test_class = TestClass(api_server='https://galaxy.ansible.com', name='galaxy')
    test_class.test()

    test_class = TestClass(api_server='https://galaxy.ansible.com/', name='galaxy')
    test_class.test()


# Generated at 2022-06-12 22:03:05.818593
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api = GalaxyAPI('my_server', 'my_email', 'my_token')
    assert api.api_server == 'my_server'
    assert api.api_token == 'my_token'
    assert api.api_email == 'my_email'
    assert api.available_api_versions == {'v2': 'api/v2'}
    assert api.api_url is None
    assert api.api_server_version is None
    assert api.name == 'my_server'

# Generated at 2022-06-12 22:03:13.797060
# Unit test for function g_connect
def test_g_connect():
    class TestGalaxyClient(object):
        def __init__(self):
            self.api_server = 'https://galaxy.ansible.com'
            self.name = 'galaxy.ansible.com'

        @g_connect(versions=['v1'])
        def test_method(self, foo, bar):
            return "%s %s" % (foo, bar)

        def _call_galaxy(self, url, method, error_context_msg, cache=False):
            return {
                "available_versions": {
                    "v1": "v1/",
                }
            }

    c = TestGalaxyClient()
    # Test v1 API method with v1 API endpoint
    assert c.test_method("foo", "bar") == "foo bar"

    # Test v1 API method with v2

# Generated at 2022-06-12 22:03:21.815304
# Unit test for constructor of class GalaxyError
def test_GalaxyError():

    galaxy_error_response_v2 = {u'code': u'error', u'message': u'invalid request'}
    galaxy_error_response_v3_1 = {u'errors': [{u'detail': u'problem found with input', u'code': u'error', u'title': u'not found'}]}
    galaxy_error_response_v3_2 = {u'errors': [{u'title': u'not found'}]}
    galaxy_error_response_v3_3 = {u'errors': [{u'code': u'error'}]}
    galaxy_error_response_v3_4 = {u'errors': [{}]}

    # galaxy_error_response_v2 is the JSON response from galaxy-v2 API endpoints.
    # http_code is the http status code

# Generated at 2022-06-12 22:03:29.357723
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api = GalaxyAPI()
    assert api.name == 'galaxy'
    assert api.api_server == 'https://galaxy.ansible.com'
    assert api.ignore_certs is False
    assert api.timeout == 10
    assert api.token is None
    assert api.user is None
    assert api.password is None

    api = GalaxyAPI(api_server='http://galaxy.ansible.com', ignore_certs=True, timeout=5, token='foobar',
                    user='foo', password='bar')
    assert api.api_server == 'http://galaxy.ansible.com'
    assert api.ignore_certs is True
    assert api.timeout == 5
    assert api.token == 'foobar'
    assert api.user == 'foo'
    assert api.password == 'bar'




# Generated at 2022-06-12 22:03:36.195693
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    err = GalaxyError(HTTPError('', -1, '', {}, None), message="GalaxyError")
    assert isinstance(err, GalaxyError)
    assert err.http_code == -1
    assert err.url == ''
    assert err.message == GalaxyError.__doc__

test_GalaxyError()

