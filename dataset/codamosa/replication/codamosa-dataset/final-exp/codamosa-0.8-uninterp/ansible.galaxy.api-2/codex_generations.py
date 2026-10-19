

# Generated at 2022-06-12 21:55:37.735375
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import unittest
    class GalaxyErrorTestCase(unittest.TestCase):
        def test_galaxy_error(self):
            error_msg = 'Galaxy error testing'
            http_error = urllib_mock.HTTPError('http://galaxy.ansible.com/api', 404, 'Not Found', {}, None)
            galaxy_error = GalaxyError(http_error, error_msg)

# Generated at 2022-06-12 21:55:44.136189
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    e = GalaxyError('test', http_code=429)
    assert(is_rate_limit_exception(e) is True)
    e = GalaxyError('test', http_code=403)
    assert(is_rate_limit_exception(e) is False)
    e = GalaxyError('test', http_code=0)
    assert(is_rate_limit_exception(e) is False)
    e = Exception('test')
    assert(is_rate_limit_exception(e) is False)



# Generated at 2022-06-12 21:55:54.538080
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    data = load_fixture('galaxy_api__lt__.json')
    expected = data['expected']

    galaxy = GalaxyAPI(data['server'])

    # Test str output
    result = str(galaxy)
    assert result == expected['str'], "str output didn't match, actual was '%s'" % result

    # Test repr output
    result = repr(galaxy)
    assert result == expected['repr'], "repr output didn't match, actual was '%s'" % result

    # Test __lt__ output
    galaxy2 = GalaxyAPI(data['server2'])
    result = galaxy2.__lt__(galaxy)
    assert result == expected['lt'], "__lt__ output didn't match, actual was '%s'" % result

# Generated at 2022-06-12 21:56:00.354222
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    assert is_rate_limit_exception(GalaxyError('429 Too Many Requests', http_code=429))
    assert is_rate_limit_exception(GalaxyError('429 Too Many Requests', http_code=520))
    # The following shouldn't be rate limit exceptions and shouldn't be retried:
    assert not is_rate_limit_exception(GalaxyError('blah blah blah'))
    assert not is_rate_limit_exception(GalaxyError('403 Forbidden', http_code=403))
    assert not is_rate_limit_exception(GalaxyError('429 Too Many Requests', http_code=404))
test_is_rate_limit_exception()



# Generated at 2022-06-12 21:56:07.320202
# Unit test for function get_cache_id
def test_get_cache_id():
    url_normal = 'https://galaxy.ansible.com/api/'
    url_with_port = 'https://galaxy.ansible.com:8080/api/'

    assert(get_cache_id(url_normal) == 'galaxy.ansible.com:')
    assert(get_cache_id(url_with_port) == 'galaxy.ansible.com:8080')
# End unit test



# Generated at 2022-06-12 21:56:09.530619
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():  # noqa
    api = GalaxyAPI('https://galaxy.ansible.com')
    assert isinstance(api, GalaxyAPI)


# Generated at 2022-06-12 21:56:17.920472
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # Test for invalid argument for 'api_token'
    try:
        GalaxyAPI('http://localhost:8080',
                  api_token=1)
        assert False
    except TypeError:
        pass

    # Test for invalid argument for 'timeout'
    try:
        GalaxyAPI('http://localhost:8080', timeout='10')
        assert False
    except AnsibleOptionsError:
        pass

    # Test for invalid argument for 'insecure'
    try:
        GalaxyAPI('http://localhost:8080', insecure='10')
        assert False
    except AnsibleOptionsError:
        pass



# Generated at 2022-06-12 21:56:25.318865
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    with pytest.raises(AnsibleError) as exception:
        with mock.patch.object(safe_eval, 'eval_builtin_arg', side_effect=lambda arg: arg):
            GalaxyAPI() < GalaxyAPI()
    assert exception.value.args[0] == 'GalaxyAPI instances must have a name to compare'

    with mock.patch.object(safe_eval, 'eval_builtin_arg', side_effect=lambda arg: arg):
        assert not(GalaxyAPI(name='test1') < GalaxyAPI(name='test1'))
        assert GalaxyAPI(name='test1') < GalaxyAPI(name='test2')
        assert not(GalaxyAPI(name='test2') < GalaxyAPI(name='test1'))

# Generated at 2022-06-12 21:56:31.509731
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    import tempfile

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # Create a galaxy_api in the temporary directory
    galaxy_api = GalaxyAPI(galaxy_server='https://galaxy.example.com',
                           api_key='dummy_api_key',
                           verify_ssl=False,
                           cache_path=tmp_dir)
    # Define galaxies_list_1 and verify __lt__

# Generated at 2022-06-12 21:56:35.014360
# Unit test for function g_connect
def test_g_connect():
    def test_func(self, *args, **kwargs):
        return 'HI'
    test_func = g_connect(versions=['v3'])(test_func)
    galaxy = _GalaxyAPI('TEST', 'TEST', 'TEST')
    assert test_func(galaxy, 'TEST') == 'HI'



# Generated at 2022-06-12 21:57:09.217269
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import http.client
    # This function is only for unit test, so it uses to_native error.
    # pylint: disable=undefined-variable
    mock_error = http.client.HTTPException()
    mock_error.code = 400
    mock_error.reason = "Bad Request"

    galaxy_error = GalaxyError(mock_error, "Test message")
    assert galaxy_error.message == "Test message (HTTP Code: 400, Message: Bad Request)"



# Generated at 2022-06-12 21:57:17.682574
# Unit test for function g_connect
def test_g_connect():
    print("Test Galaxy API decorator")
    from collections import namedtuple
    from ansible.galaxy import GalaxyAPI
    g = GalaxyAPI('https://galaxy.ansible.com')
    g._available_api_versions = None
    # Make a namedtuple with all the values we need to fake a request
    args = namedtuple(
        'args',
        ['action', 'api_server', 'ignore_certs', 'ignore_cache', 'ignore_errors', 'keep_remote_artifacts',
         'name',
         'no_cache', 'role_file', 'roles_path', 'server', 'token', 'tol', 'verify', 'wait'],
    )

    # Args for the following test cases

# Generated at 2022-06-12 21:57:19.945132
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    error = GalaxyError('Rate limit error', '', url='', http_code=429)
    assert is_rate_limit_exception(error) is True



# Generated at 2022-06-12 21:57:24.133229
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    from ansible.galaxy.api import GalaxyError
    exc = GalaxyError(msg='', http_code=401)
    assert not is_rate_limit_exception(exc)
    exc = GalaxyError(msg='', http_code=403)
    assert not is_rate_limit_exception(exc)
    exc = GalaxyError(msg='', http_code=429)
    assert is_rate_limit_exception(exc)



# Generated at 2022-06-12 21:57:26.864193
# Unit test for function cache_lock
def test_cache_lock():
    import pytest
    from ansible.galaxy.api import GalaxyAPI
    ga = GalaxyAPI(url='http://localhost:8081')

    @cache_lock
    def successful_function():
        return True

    @cache_lock
    def failing_function():
        raise HTTPError(None, None, None, None, None)

    assert successful_function() is True
    with pytest.raises(HTTPError):
        failing_function()



# Generated at 2022-06-12 21:57:32.380607
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    test_obj = GalaxyAPI('test_url', 'test_token', [], 'test_name', 'test_verify')
    assert test_obj < None is False
    test_obj_2 = GalaxyAPI('test_url_2', 'test_token', [], 'test_name', 'test_verify')
    assert test_obj < test_obj_2 is True
    assert test_obj_2 < test_obj is False



# Generated at 2022-06-12 21:57:36.371541
# Unit test for function g_connect
def test_g_connect():
    with pytest.raises(AnsibleError) as exc:
        g_connect(["foo"])(lambda x: None)(None)
    assert exc.value.message == "Galaxy action <lambda> requires API versions 'foo' but only '' are available on  ''"


# Generated at 2022-06-12 21:57:48.218213
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError("", 404, "", {}, None)
    message = "Fake Message"
    galaxy_error = GalaxyError(http_error, message)
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == ""
    assert galaxy_error.message == u"Fake Message (HTTP Code: 404, Message: None)"

# Unit test that can't be run directly.
# Need to write test application that will mock the response.
# def test_GalaxyError_v2():
#     http_error = HTTPError("", 404, "", {}, None)
#     message = "Fake Message"
#     galaxy_error = GalaxyError(http_error, message)
#     assert galaxy_error.http_code == 404
#     assert galaxy_error.url == ""
#     assert galaxy_error.message

# Generated at 2022-06-12 21:57:58.460860
# Unit test for function g_connect
def test_g_connect():
    class DummyGalaxy(object):
        def __init__(self):
            self._available_api_versions = None
            self.api_server = 'https://galaxy.ansible.com'
            self.name = 'my-galaxy'

    def get_extras():
        # API versions v1 and v2 supported
        @g_connect(versions=['v1', 'v2'])
        def extras(self):
            return 'v1 extras'

        @g_connect(versions=['v2'])
        def extras2(self):
            return 'v2 extras'

        dg = DummyGalaxy()
        if extras(dg) != 'v1 extras':
            raise Exception("Wrong return value for the extras() function")
        if extras2(dg) != 'v2 extras':
            raise

# Generated at 2022-06-12 21:58:01.754592
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    # Initializes GalaxyAPI
    galaxy_api = GalaxyAPI()

    assert galaxy_api < "__lt__"

# Generated at 2022-06-12 21:58:37.697554
# Unit test for function g_connect
def test_g_connect():
    """
    Wrapper to lazily initialize connection info to Galaxy and verify the API versions required are available on the
    endpoint.

    :param versions: A list of API versions that the function supports.
    """
    def decorator(method):
        def wrapped(self, *args, **kwargs):
            if not self._available_api_versions:
                display.vvvv("Initial connection to galaxy_server: %s" % self.api_server)

                # Determine the type of Galaxy server we are talking to. First try it unauthenticated then with Bearer
                # auth for Automation Hub.
                n_url = self.api_server
                error_context_msg = 'Error when finding available api versions from %s (%s)' % (self.name, n_url)


# Generated at 2022-06-12 21:58:41.339553
# Unit test for function get_cache_id
def test_get_cache_id():
    url = 'http://galaxy.example.com/'
    cache_id = get_cache_id(url)
    assert cache_id == 'galaxy.example.com:', "Expected cache ID 'galaxy.example.com:' but got '%s'" % cache_id

    url = 'http://galaxy.example.com:1000/'
    cache_id = get_cache_id(url)
    assert cache_id == 'galaxy.example.com:1000', "Expected cache ID 'galaxy.example.com:1000' but got '%s'" % cache_id

    url = 'http://galaxy.example.com:1000/'
    cache_id = get_cache_id(url)

# Generated at 2022-06-12 21:58:46.959396
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    galaxy_error = GalaxyError(HTTPError('http://foo', 400, 'Bad Request', {}, None), 'Sample error message')
    assert galaxy_error.http_code == 400
    assert galaxy_error.url == 'http://foo'
    assert galaxy_error.message == 'Sample error message (HTTP Code: 400, Message: Bad Request)'



# Generated at 2022-06-12 21:58:47.673036
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    pass

# Generated at 2022-06-12 21:58:56.538196
# Unit test for function g_connect
def test_g_connect():
    class TestGalaxyAPI:
        __doc__ = 'Unit test for g_connect'
        name = 'https://api.galaxy.ansible.com/'
        api_server = 'https://api.galaxy.ansible.com/'
        version = 'v2'
        allow_overwrites = True
        ignore_certs = False
        ignore_certs_warning = False
        no_wait = False
        token = None
        _available_api_versions = None
        _collections = {}

        def __init__(self, *args, **kwargs):
            return

        # this is a unit test so we need to pretend that _call_galaxy responds the way we want

# Generated at 2022-06-12 21:59:04.412775
# Unit test for function get_cache_id
def test_get_cache_id():
    assert "galaxy.ansible.com:443" == get_cache_id("https://galaxy.ansible.com/api/")
    assert "galaxy.ansible.com:443" == get_cache_id("https://galaxy.ansible.com:443/api/")

    assert "galaxy.ansible.com:80" == get_cache_id("http://galaxy.ansible.com/api/")
    assert "galaxy.ansible.com:80" == get_cache_id("http://galaxy.ansible.com:80/api/")

    assert "galaxy.ansible.com:80" == get_cache_id("http://galaxy.ansible.com")

# Generated at 2022-06-12 21:59:12.058482
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    galaxy_error = GalaxyError(HTTPError(url='https://ansible.com/v2/namespaces/jctanner/collections/', hdrs={},
                                         fp=None, code=404, msg='Not Found', hdrs=[],
                                         info=None),
                               message='not found')
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == 'https://ansible.com/v2/namespaces/jctanner/collections/'
    assert galaxy_error.message == "not found (HTTP Code: 404, Message: Not Found Code: Unknown)"



# Generated at 2022-06-12 21:59:17.981196
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id("http://example.com:80") == 'example.com:80'
    assert get_cache_id("http://example.com") == 'example.com:'
    assert get_cache_id("http://example.com/:80") == 'example.com/:80'
    assert get_cache_id("http://example.com/:80/") == 'example.com/:80/'



# Generated at 2022-06-12 21:59:20.223585
# Unit test for function cache_lock
def test_cache_lock():
    val = [None]
    @cache_lock
    def test():
        val[0] = 1
    test()
    assert val == [1]


# Generated at 2022-06-12 21:59:24.374180
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def test_func():
        pass
    assert hasattr(test_func, '_ansible_cache_lock_')
    assert test_func._ansible_cache_lock_



# Generated at 2022-06-12 22:00:01.668684
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import unittest
    import unittest.mock
    from urllib.error import HTTPError
    from io import BytesIO

    class MyTestCase(unittest.TestCase):
        def test_init(self):
            HTTPErrorObject = HTTPError(url='https://galaxy.ansible.com/api/v2/roles/', code=200, msg='OK', hdrs=[], fp=BytesIO(b'{ "message": "ok", "code": "ok", "default": "ok" }'))

# Generated at 2022-06-12 22:00:11.183531
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    message = "Test"
    http_code = 500
    url = "http://www.example.com/v3/test"
    err_info = {"title": "test", "detail": "test123", "code": "12345"}
    http_error = HTTPError(url, http_code, "test", None, None)
    galaxy_error = GalaxyError(http_error, message)
    full_error_msg = u"%s (HTTP Code: %d, Message: %s Code: %s)" % (message, http_code, err_info["title"], err_info["code"])
    assert galaxy_error.message == full_error_msg


# Generated at 2022-06-12 22:00:20.809309
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    api = GalaxyAPI('galaxy.server')

    # Test that two GalaxyAPI objects can be compared and return the correct result
    api_same = GalaxyAPI('galaxy.server')
    assert api != api_same
    assert not api == api_same
    assert api.__lt__(api_same)
    assert not api_same.__lt__(api)

    # Test that two GalaxyAPI objects from the same server with different api_servers can be compared and return the correct result
    api_different = GalaxyAPI('galaxy.server/api')
    assert api != api_different
    assert not api == api_different
    assert not api.__lt__(api_different)
    assert api_different.__lt__(api)

    # Test that two GalaxyAPI objects with different server/URL can be compared and return the correct result
    api_

# Generated at 2022-06-12 22:00:22.668783
# Unit test for function g_connect
def test_g_connect():
    assert True  # No test available at this time

# Generated at 2022-06-12 22:00:27.636298
# Unit test for function get_cache_id
def test_get_cache_id():
    # Test with no port specified in the URL
    cache_id = get_cache_id('http://hello.world.example.com/')
    assert cache_id == 'hello.world.example.com:'
    # Test with port 80 specified in the URL
    cache_id = get_cache_id('http://hello.world.example.com:80/')
    assert cache_id == 'hello.world.example.com:80'
    # Test with a path specified after the server URL
    cache_id = get_cache_id('http://hello.world.example.com/v1/')
    assert cache_id == 'hello.world.example.com:'
    # Test with a different port specified in the URL
    cache_id = get_cache_id('http://hello.world.example.com:8888/')
    assert cache

# Generated at 2022-06-12 22:00:31.567976
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id("https://galaxy.server/api/v2/") == "galaxy.server"
    assert get_cache_id("https://user:password@galaxy.server:1234/api/v2/") == "galaxy.server:1234"


# Generated at 2022-06-12 22:00:37.038529
# Unit test for function g_connect
def test_g_connect():
    dummy_versions=['v1','v2']
    @g_connect(versions=dummy_versions)
    def wrapped(self, *args, **kwargs):
        pass
    assert wrapped.__name__=='wrapped'
# end of test_g_connect



# Generated at 2022-06-12 22:00:47.156474
# Unit test for function is_rate_limit_exception

# Generated at 2022-06-12 22:00:56.498998
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # Test v1 GalaxyError
    try:
        http_error = HTTPError(url='http://test.galaxy.com/api/v1/', code=404, msg="404 Not Found", hdrs=None, fp=None)
        http_error.read = lambda: '{"default": "error"}'
        raise GalaxyError(http_error,'Not Found')
    except GalaxyError as e:
        assert e.message == 'Not Found (HTTP Code: 404, Message: error)'
    # Test v2 GalaxyError

# Generated at 2022-06-12 22:01:02.292599
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    class MockGalaxyAPI:
        def __init__(self, api_server, version):
            self.api_server = api_server
            self.version = version

    mock = MockGalaxyAPI('https://someurl.com', 'v3')

    assert mock < GalaxyAPI('https://someurl.com', 'v3')

# Generated at 2022-06-12 22:02:44.370046
# Unit test for function cache_lock
def test_cache_lock():
    import time
    import threading

    def myfunc(time):
        time.sleep(3)

    def test_func(time):
        cache_lock(myfunc(time))

    t = threading.Thread(target=test_func, args=(time,))
    t.start()

    assert t.is_alive()



# Generated at 2022-06-12 22:02:51.059735
# Unit test for function g_connect
def test_g_connect():
    # TODO Simplify testing for g_connect
    # 1. Create a class with a method decorated by g_connect
    # 2. Create an instance of the class
    # 3. Set _available_api_versions for the instance (dict with keys matching the versions to check for)
    # 4. Call the method
    class testConnect():
        def __init__(self):
            self.name = "testServer"
            self.api_server = "testApiServer"
            self._available_api_versions = {}

        @g_connect(["v1","v2"])
        def testMethod(self):
            pass

    server = testConnect()

    # Test when API versions are not set
    try:
        server.testMethod()
    except AnsibleError as e:
        assert "requires API versions" in str(e)


# Generated at 2022-06-12 22:03:01.270420
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    api1 = GalaxyAPI('devhub', 'https://galaxy.server.here', [])
    api1.name = 'Test API'
    api1.api_server = 'Test API'

    # Case 1:
    # Both API objects are GalaxyAPI instances
    api2 = GalaxyAPI('devhub', 'https://galaxy.server.here', [])
    api2.name = 'Test API 2'
    api2.api_server = 'Test API 2'
    expected_result = -1
    result = api1.__lt__(api2)

    assert expected_result == result

    # Case 2:
    # The first API objects is not a GalaxyAPI instance
    api2 = GalaxyAPI('devhub', 'https://galaxy.server.here', [])
    api2.name = 'Test API 2'
    api2

# Generated at 2022-06-12 22:03:10.819411
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy import api

    class FakeGalaxy:
        def __init__(self, name, api_server, ignore_certs=False):
            self.name = name
            self.api_server = api_server
            self._available_api_versions = {}
            self.ignore_certs = ignore_certs
            self.http_timeout = 10.0
            self.allow_redirects = True
            self.max_redirects = 10
            self.redirect_history = []

        @g_connect(versions=['v2'])
        def get_role_by_id(self, role_id, **kwargs):
            return {}


# Generated at 2022-06-12 22:03:16.094934
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError(url="https://galaxy.ansible.com", code=400, msg="Bad Request", hdrs=None, fp=None)
    http_error.read = lambda: '{"message": "Oops", "code": "BadRequest"}'
    galaxy_error = GalaxyError(http_error, "V2 error")
    assert galaxy_error.http_code == 400
    assert galaxy_error.url == "https://galaxy.ansible.com"
    assert galaxy_error.message == u'V2 error (HTTP Code: 400, Message: Oops Code: BadRequest)'

    http_error = HTTPError(url="https://galaxy.ansible.com", code=400, msg="Bad Request", hdrs=None, fp=None)

# Generated at 2022-06-12 22:03:16.944075
# Unit test for function g_connect
def test_g_connect():
    g_connect(["v2"])



# Generated at 2022-06-12 22:03:20.395697
# Unit test for function g_connect
def test_g_connect():
    with pytest.raises(AnsibleError):
        g_connect([u'v2', u'v3'])(DummyFunc)(DummyClass(), None, None)

# Generated at 2022-06-12 22:03:24.031636
# Unit test for function cache_lock
def test_cache_lock():
    lock = threading.Lock()
    lock.acquire()

    @cache_lock
    def test_func():
        if lock.acquire(False):
            lock.release()
            return 1
        return 0

    assert test_func() == 0
    lock.release()
    assert test_func() == 1



# Generated at 2022-06-12 22:03:28.290007
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://localhost:1234') == 'localhost:1234'
    assert get_cache_id('http://user:pass@localhost:1234') == 'localhost:1234'
    assert get_cache_id('http://localhost') == 'localhost'
    assert get_cache_id('http://localhost/data') == 'localhost'
    assert get_cache_id('http://localhost/data/file') == 'localhost'


# Generated at 2022-06-12 22:03:41.564519
# Unit test for function get_cache_id
def test_get_cache_id():
  url = 'https://galaxy.ansible.com'
  assert get_cache_id(url) == 'galaxy.ansible.com'
  url = 'https://galaxy.ansible.com:8443'
  assert get_cache_id(url) == 'galaxy.ansible.com:8443'
  url = 'https://ansible:ansible@galaxy.ansible.com:8443/'
  assert get_cache_id(url) == 'galaxy.ansible.com:8443'
  assert get_cache_id('https://abc') == 'abc'
  assert get_cache_id('https://abc:8080') == 'abc:8080'
  assert get_cache_id('https://abc.com') == 'abc.com'