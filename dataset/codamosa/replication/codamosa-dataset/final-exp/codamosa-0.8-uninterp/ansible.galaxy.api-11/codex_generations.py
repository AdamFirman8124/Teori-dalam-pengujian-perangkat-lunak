

# Generated at 2022-06-12 21:55:19.091514
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://127.0.0.1:8080/api/') == '127.0.0.1:8080'
    assert get_cache_id('https://127.0.0.1/api/') == '127.0.0.1'
    assert get_cache_id('http://127.0.0.1:80/api/') == '127.0.0.1:80'
    assert get_cache_id('http://127.0.0.1/api/') == '127.0.0.1'



# Generated at 2022-06-12 21:55:25.666347
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://foo') == 'foo:'
    assert get_cache_id('http://foo/') == 'foo:'
    assert get_cache_id('http://foo:1234/') == 'foo:1234'
    assert get_cache_id('http://[::1]/') == '[::1]:'
    # note the port number is a string
    assert get_cache_id('http://foo:port/') == 'foo:port'


# Generated at 2022-06-12 21:55:34.891243
# Unit test for function get_cache_id
def test_get_cache_id():
    print(get_cache_id('https://galaxy.com'))
    print(get_cache_id('https://galaxy.com:80'))
    print(get_cache_id('https://galaxy.com:8080'))
    print(get_cache_id('https://galaxy.com:80/api'))
    print(get_cache_id('https://httpbin.org/anything?foo=bar'))
    print(get_cache_id('https://httpsbin.org:443/anything?foo=bar'))
    print(get_cache_id('https://httpsbin.org:80/anything?foo=bar'))



# Generated at 2022-06-12 21:55:43.176809
# Unit test for function g_connect
def test_g_connect():
    versions = ['v1','v2']
    def decorator(method):
        def wrapped(self, *args, **kwargs):
            print('inside wrapped')
            if not self._available_api_versions:
                print(self.api_server)
                data = {
                    'available_versions': {
                        "v1": "v1/",
                        "v2": "v2/",
                        "v3": "v3/"
                    }
                }
                available_versions = data.get('available_versions', {u'v1': u'v1/'})
                if list(available_versions.keys()) == [u'v1']:
                    available_versions[u'v2'] = u'v2/'

                self._available_api_versions = available_versions

# Generated at 2022-06-12 21:55:48.324842
# Unit test for function g_connect
def test_g_connect():
    class TestClient(object):
        _available_api_versions = {}


    @g_connect(versions=['v1'])
    def test_api(self):
        print('testing')

    client = TestClient()
    test_api(client)



# Generated at 2022-06-12 21:55:54.910518
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api_v2 = GalaxyAPI(
        name="example",
        url="http://example.com/api/v2/",
    )
    galaxy_api_v3 = GalaxyAPI(
        name="example",
        url="http://example.com/api/v3/",
    )
    assert (galaxy_api_v2 < galaxy_api_v3)

if __name__ == '__main__':
    # Unit test this module.
    test_GalaxyAPI___lt__()

# Generated at 2022-06-12 21:56:00.216681
# Unit test for function g_connect
def test_g_connect():
    def test_g_connect_inner1(self, value):
        print(value)
    def test_g_connect_inner2(self, value):
        print(value)
    test_g_connect_inner1 = g_connect(['v1', 'v2'])(test_g_connect_inner1)
    test_g_connect_inner2 = g_connect(['v2', 'v3'])(test_g_connect_inner2)

    test_g_connect_inner1(object(), value=100)
    test_g_connect_inner2(object(), value=200)


# Generated at 2022-06-12 21:56:03.249341
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def assert_called(called):
        called.append(1)

    called = []
    assert_called(called)
    assert len(called) == 1



# Generated at 2022-06-12 21:56:13.225705
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # Create a dummy class to pass where the GalaxyAPI would usually be used.
    class MockGalaxyOptions(object):
        server = None
        ignore_certs = False
        api_key = None
        force = False
        timeout = 10
        validate_certs = False
        active = True
        galaxy_token = None
        ignore_errors = False
        ignore_errors_on_import = False
        force_on_import = False
        no_wait = False

    # Create the GalaxyAPI object, leaving the arguments empty for now.
    dummy_galaxy = GalaxyAPI(MockGalaxyOptions())
    # Verify that the GalaxyAPI object was created.
    assert dummy_galaxy



# Generated at 2022-06-12 21:56:15.313574
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    exc = GalaxyError(msg='Mock Exception', http_code=429)
    assert is_rate_limit_exception(exc)



# Generated at 2022-06-12 21:56:50.745347
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api_server = 'https://galaxy.ansible.com'
    api_token = 'TEST_TOKEN'
    name = 'Test Galaxy'
    galaxyAPI = GalaxyAPI(api_server=api_server, api_token=api_token, name=name)

    assert galaxyAPI.api_server == api_server
    assert galaxyAPI.api_token == api_token
    assert galaxyAPI.name == name
    assert galaxyAPI.requests_session is None

# Generated at 2022-06-12 21:56:57.546448
# Unit test for function g_connect
def test_g_connect():
    class FakeGalaxyConnection(object):
        def __init__(self):
            self.api_server = ""
            self.name = ""
            self._available_api_versions = {}
        def _call_galaxy(self, url, method='GET', error_context_msg=None, cache=True):
            return {}
    f = FakeGalaxyConnection()
    def test_g_connect_wrapper(self, *args, **kwargs):
        return
    wrapped = g_connect(['v1'])(test_g_connect_wrapper)
    assert wrapped(f, 1) == None



# Generated at 2022-06-12 21:57:05.351885
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def fun():
        return True

    fake_lock = threading.Lock()
    with mock.patch("ansible.module_utils.basic.MutableMapping.__enter__", return_value=fake_lock):
        with mock.patch.object(fake_lock, '__enter__', return_value=fake_lock):
            assert fun() == True
            fake_lock.__enter__.assert_called_once()
            fake_lock.__enter__.return_value.__enter__.assert_called_once()
            fake_lock.__enter__.return_value.__exit__.assert_called_once()


# The "fs" backend is not really a backend. It can be a local
# filesystem, or any filesystem that looks like a local one.
# Used for testing and in Galaxy projects

# Generated at 2022-06-12 21:57:06.266020
# Unit test for function cache_lock
def test_cache_lock():
    assert cache_lock


# Generated at 2022-06-12 21:57:09.353994
# Unit test for function g_connect
def test_g_connect():
    versions = ['v1', 'v2']
    def method():
        return [1, 2]
    return g_connect(versions)(method)()
#print(test_g_connect())




# Generated at 2022-06-12 21:57:15.064779
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    config = {
        'name': 'galaxy_server',
        'server': 'http://galaxy.ansible.com',
    }

    galaxy_api = GalaxyAPI(config)

    assert galaxy_api.name == 'galaxy_server'
    assert galaxy_api.api_server == 'http://galaxy.ansible.com'

    assert not galaxy_api.ignore_certs
    assert not galaxy_api.ignore_errors
    assert not galaxy_api.api_token
    assert not galaxy_api.api_version
    assert not galaxy_api.auth_url
    assert not galaxy_api.token_url
    assert not galaxy_api.client_id
    assert not galaxy_api.client_secret

# Generated at 2022-06-12 21:57:23.274520
# Unit test for function g_connect
def test_g_connect():
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.urls import ConnectionInfo

    loader = DataLoader()
    user_agent = 'ANSIBLE_TEST_USER_AGENT'
    connection_info = ConnectionInfo(
        uri='https://testgalaxy.com',
        force_basic_auth=False,
        token='test_token',
        client_cert=None,
        validate_certs=False,
        timeout=10,
        headers=dict(),
        url_username='test_username',
        url_password='test_password',
        force=False,
        follow_redirects='safe',
    )
    galaxy_api_server = 'https://testgalaxy.com'

    # test the function g_connect
    test_class = Mock_Gal

# Generated at 2022-06-12 21:57:33.240561
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():

    """Test __lt__ method of class GalaxyAPI"""

    data1 = {
        "name": "test1",
        "api_server": "https://galaxy1.example.com",
        "api_key": "12345"
    }

    data2 = {
        "name": "test2",
        "api_server": "https://galaxy2.example.com",
        "api_key": "12345"
    }

    test_obj1 = GalaxyAPI(**data1)
    test_obj2 = GalaxyAPI(**data2)

    assert test_obj1.__lt__(test_obj2) == True


# Generated at 2022-06-12 21:57:41.043667
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    from ansible.galaxy import collections
    from ansible.galaxy import GalaxyAPI
    try:
        collections.__version__ = '1.1.0'
    except:
        pass

    # assert not exceptions raised
    x = GalaxyAPI('server', 'api_key', 'username')
    collections.__version__ = '1.1.0'
    assert x == collections.__version__
    collections.__version__ = '2.0.0'
    assert x < collections.__version__



# Generated at 2022-06-12 21:57:43.368064
# Unit test for function g_connect
def test_g_connect():
    c = GalaxyClient(api_server='https://galaxy.ansible.com')
    assert isinstance(c, GalaxyClient)



# Generated at 2022-06-12 21:58:33.153471
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    src =  {
        'name': 'g_api', 
        'server': 'https://g_api_server', 
        'ignore_certs': False, 
        'ignore_certs_path': '/path/to/nothing'}
    galaxy_api_0 = GalaxyAPI(src)
    galaxy_api_1 = GalaxyAPI(src)
    assert galaxy_api_0 == galaxy_api_1

# Generated at 2022-06-12 21:58:34.740753
# Unit test for function cache_lock
def test_cache_lock():
    @cache_lock
    def test_func():
        return True
    assert test_func()



# Generated at 2022-06-12 21:58:43.438845
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    """ Test for error message in GalaxyError constructor.

    Args:
        None.

    Returns:
        None.

    Raises:
        AssertionError: If testing fails.
    """
    error_message = 'Bad server response'
    http_error = HTTPError(url='https://galaxy.example.com/', code='403', msg='Bad server response', hdrs={}, fp=None,
                           errcode='404', reason='Bad server response')
    try:
        galaxy_error = GalaxyError(http_error, error_message)
        raise AssertionError('GalaxyError was raised correctly.')
    except GalaxyError as ex:
        assert (ex.http_code == 403)
        assert (ex.url == 'https://galaxy.example.com/')

# Generated at 2022-06-12 21:58:51.050785
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError('http://galaxy.server', 404, 'Not Found', {}, None)
    error = GalaxyError(http_error, 'Collection not found')
    assert isinstance(error, GalaxyError)
    assert error.http_code == 404
    assert error.url == 'http://galaxy.server'
    assert error.message == 'Collection not found (HTTP Code: 404, Message: Not Found)'


# Generated at 2022-06-12 21:58:54.562897
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    g = GalaxyAPI("localhost", False, False, "username", "password", "token")
    h = GalaxyAPI("localhost", False, False, "username", "password", "token")
    h.name = "b"
    assert g < h


# Generated at 2022-06-12 21:58:59.868807
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    rate_limit_error = GalaxyError(msg="Request limit reached", http_code=429)
    # Test both known error codes
    assert is_rate_limit_exception(rate_limit_error)
    # Test some unknown error codes
    rate_limit_error.http_code = 503
    assert not is_rate_limit_exception(rate_limit_error)
    rate_limit_error.http_code = 404
    assert not is_rate_limit_exception(rate_limit_error)



# Generated at 2022-06-12 21:59:05.325309
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy.api import GalaxyAPI
    # TODO: Mock out the GalaxyAPI._call_galaxy method
    g = GalaxyAPI('https://galaxy.ansible.com', token='token')
    assert g.api_server == 'https://galaxy.ansible.com/api/'

# Generated at 2022-06-12 21:59:14.459073
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError('https://ansible-galaxy.org/api/', 401, 'Unauthorized', '', None)
    message = 'Problem connecting to Galaxy - received 401 response'
    g_error = GalaxyError(http_error, message)
    assert g_error.http_code == 401
    assert g_error.message == 'Problem connecting to Galaxy - received 401 response (HTTP Code: 401, Message: Unauthorized)'
    assert g_error.url == 'https://ansible-galaxy.org/api/'

    http_error = HTTPError('https://ansible-galaxy.org/api/v1/', 401, 'Unauthorized', '', None)
    message = 'Problem connecting to Galaxy - received 401 response'
    g_error = GalaxyError(http_error, message)

# Generated at 2022-06-12 21:59:22.269506
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    # Configure mocks for GalaxyAPI.__lt__
    galaxy_api = GalaxyAPI(args=None, galaxy_token=None, galaxy_ignore_certs=False, galaxy_force_api_version=None,
                           galaxy_server=None, validate_certs=True)
    other = object()

    # Execute code to be tested
    result = galaxy_api.__lt__(other)

    # Verify results of code to be tested
    assert isinstance(result, bool)



# Generated at 2022-06-12 21:59:30.112700
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    msg = "Test GalaxyError"
    try:
        # Raise HTTPError
        raise HTTPError('http://www.example.com', 500, msg, {}, None)
    except HTTPError as e:
        # Construct GalaxyError instance
        galaxy_error = GalaxyError(e, msg)
        assert galaxy_error.http_code == 500
        assert str(galaxy_error) == msg + ' (HTTP Code: 500, Message: ' + msg + ')'
        assert galaxterr_hasattr(galaxy_error, 'http_code')
        assert galaxterr_hasattr(galaxy_error, 'url')
        assert galaxterr_hasattr(galaxy_error, 'message')



# Generated at 2022-06-12 22:00:10.009493
# Unit test for function cache_lock
def test_cache_lock():
    from ansible.galaxy.api import GalaxyAPI, cache_lock
    galaxy_api = GalaxyAPI(galaxy_url='https://galaxy.ansible.com')
    res = galaxy_api.get_api_version()
    api_version = res.get('api_version', -1)
    assert api_version > 0
# end of unit test for function cache_lock



# Generated at 2022-06-12 22:00:17.230925
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    try:
        raise HTTPError(url="", code=404, msg="HTTP Error", hdrs="", fp=None)
    except HTTPError as exc:
        exc_galaxy_error = GalaxyError(exc, "Test galaxy error")
        assert to_text(exc_galaxy_error.message) == "Test galaxy error (HTTP Code: 404, Message: HTTP Error)"
        assert to_text(exc_galaxy_error.http_code) == "404"
        assert to_text(exc_galaxy_error.url) == ""



# Generated at 2022-06-12 22:00:25.068752
# Unit test for function cache_lock
def test_cache_lock():
    global _CACHE_LOCK
    assert _CACHE_LOCK is None
    _CACHE_LOCK = threading.Lock()
    @cache_lock
    def foo():
        pass
    _CACHE_LOCK.acquire()
    try:
        foo()
    except AssertionError as e:
        # Make sure we're not acquiring the lock twice
        assert 'Already acquired' in str(e)
        raise
    finally:
        _CACHE_LOCK.release()
    _CACHE_LOCK = None



# Generated at 2022-06-12 22:00:33.363940
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    error = HTTPError(url='https://galaxy.ansible.com/api/v2/', code=404, msg='message', hdrs={}, fp=None)
    # Test case with v2 API
    galaxy_error = GalaxyError(error, 'message')
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == 'https://galaxy.ansible.com/api/v2/'
    assert galaxy_error.message == 'message (HTTP Code: 404, Message: message Code: Unknown)'

    # Test case with v3 API
    error = HTTPError(url='https://galaxy.ansible.com/api/v3/', code=404, msg='message', hdrs={}, fp=None)
    galaxy_error = GalaxyError(error, 'message')
    assert galaxy_error

# Generated at 2022-06-12 22:00:45.043638
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    """ Unit test for constructor of class GalaxyError """
    # This is a class and not a function, so it can't be mocked directly.
    # We do this dance to mock the attributes we need, then pass it in.
    url = 'https://cloud.example.com/api/v4'
    http_errors = collections.namedtuple('HTTP_Error', ['code', 'reason', 'geturl', 'read'])
    message = u"Some error"
    http_error = http_errors(http_code=403, reason='Forbidden', geturl=url, read=lambda: u"{'default': '{0}'}".format(message))
    http_code = http_error.code
    obj_galaxy_error = GalaxyError(http_error=http_error, message=u"Issue with Galaxy server")
    # Check if

# Generated at 2022-06-12 22:00:52.460800
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    a = GalaxyAPI('name')
    b = GalaxyAPI('name')

    # Default
    actual = a.__lt__(b)
    assert actual == 0

    # Equal
    a.version = b.version = [1, 0, 0]
    actual = a.__lt__(b)
    assert actual == 0

    # 1.1.0 < 1.0.0
    a.version = [1, 1, 0]
    b.version = [1, 0, 0]
    actual = a.__lt__(b)
    assert actual == 1

    # 1.0.0 > 1.1.0
    a.version = [1, 0, 0]
    b.version = [1, 1, 0]
    actual = a.__lt__(b)
    assert actual == -1

    # 1

# Generated at 2022-06-12 22:01:03.588418
# Unit test for function g_connect
def test_g_connect():
    # test if the decorator works
    test_inst = AnsibleGalaxyAPI(galaxy_server='http://fake-galaxy.com/')
    test_inst.api_server = None
    test_inst._available_api_versions = None
    decorator = g_connect([u'v1', u'v2'])

    def fake_call_method(test_inst):
        return "test string"

    decorated_method = decorator(fake_call_method)
    assert decorated_method(test_inst) == "test string"
    assert test_inst.api_server == "http://fake-galaxy.com/api/"
    assert test_inst._available_api_versions == {u'v1': u'v1/', u'v2': u'v2/'}



# Generated at 2022-06-12 22:01:15.737333
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    server = 'https://galaxy.ansible.com'
    username = 'user'
    password = 'p@ssword!'
    verify_ssl = False
    ignore_certs = True
    token = 'Bw8H-f27yCKk-sJVhX0H-G0xrZ'

    g = GalaxyAPI(server, username=username, password=password, token=token, ignore_certs=ignore_certs,
                  verify_ssl=verify_ssl)

    assert g.name == username
    assert g.api_server == server
    assert g.token == token
    assert g.ignore_certs == ignore_certs
    assert g.verify_ssl == verify_ssl

    g = GalaxyAPI(server, token=token, ignore_certs=ignore_certs)


# Generated at 2022-06-12 22:01:19.270334
# Unit test for function g_connect
def test_g_connect():
    from ansible.galaxy import Galaxy
    versions = ['v1']

    @g_connect(versions)
    def func(self):
        return True

    galaxy = Galaxy('test', 'http://localhost/')
    assert func(galaxy) is True
# Unit tests end


# Generated at 2022-06-12 22:01:20.571136
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    GalaxyAPI.__lt__(instance)


# Generated at 2022-06-12 22:01:49.771937
# Unit test for function g_connect
def test_g_connect():
    class TestClass:
        def __init__(self):
            self.name = "Ansible Automation"
            self.api_server = "https://galaxy.example.com"
            # Default to only supporting v1, if only v1 is returned we also assume that v2 is available even though
            # it isn't returned in the available_versions dict.
            self._available_api_versions = []
            self._call_galaxy = self._call_galaxy

    test_obj = TestClass()
    assert hasattr(test_obj, '_test_method') is False
    test_obj._test_method = test_method
    g_connect(['v1'])(test_obj._test_method)
    assert hasattr(test_obj, '_test_method') is True



# Generated at 2022-06-12 22:01:51.880932
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    galaxy_error = GalaxyError("error", http_code=429)
    assert is_rate_limit_exception(galaxy_error)



# Generated at 2022-06-12 22:02:02.287001
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    # Test with v1.1 and v1.0.0.0
    api = GalaxyAPI('name', 'server', {'v1.1': 'api_server', 'v1.0.0.0': 'api_server'})
    assert api < 'v1.1'
    assert api < 'v2'
    assert api >= 'v1.0.0.0'

    # Test with v2 and v1.1
    api = GalaxyAPI('name', 'server', {'v2': 'api_server', 'v1.1': 'api_server'})
    assert api < 'v2'
    assert api >= 'v1.1'

    # Test with v2 and v3

# Generated at 2022-06-12 22:02:05.462334
# Unit test for function g_connect
def test_g_connect():
    assert g_connect(['v1'])(lambda self: self)
    assert g_connect(['v1'])(lambda self: self)


# Generated at 2022-06-12 22:02:16.483023
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    _test_GalaxyAPI = GalaxyAPI(None, None, None)
    _test_GalaxyAPI.api_server = 'https://galaxy-sdk.ansible.com'
    assert _test_GalaxyAPI.__lt__(_test_GalaxyAPI) is False, 'GalaxyAPI.__lt__ returned ' + str(_test_GalaxyAPI.__lt__(_test_GalaxyAPI))
    _test_GalaxyAPI2 = GalaxyAPI(None, None, None)
    _test_GalaxyAPIFake = GalaxyAPI(None, None, None)
    _test_GalaxyAPIFake.api_server = 'https://galaxy.ansible.com'

# Generated at 2022-06-12 22:02:27.932324
# Unit test for method __lt__ of class GalaxyAPI

# Generated at 2022-06-12 22:02:28.612294
# Unit test for function g_connect
def test_g_connect():
    pass


# Generated at 2022-06-12 22:02:29.175244
# Unit test for function g_connect
def test_g_connect():
    pass



# Generated at 2022-06-12 22:02:30.080478
# Unit test for function g_connect
def test_g_connect():
    #TBD
    return True


# Generated at 2022-06-12 22:02:39.585499
# Unit test for function g_connect
def test_g_connect():
    def rundecorator(method):
        def wrapped(*args, **kwargs):
            return method(*args, **kwargs)
        return wrapped

    # default good case
    old_method = g_connect(['v1', 'v2'])(rundecorator)
    assert old_method.__name__ == 'wrapped'

    def rundecorator(method):
        def wrapped(*args, **kwargs):
            raise AnsibleError("bad")
        return wrapped

    # raises an AnsibleError
    with pytest.raises(AnsibleError):
        g_connect(['v1'])(rundecorator)



# Generated at 2022-06-12 22:03:23.555920
# Unit test for constructor of class GalaxyError
def test_GalaxyError():

    def test_error_by_http_code(http_code):
        try:
            raise HTTPError(url="http://galaxy.ansible.com/api/v2/", code=http_code, msg="", hdrs="", fp="")
        except HTTPError as error:
            galaxy_error = GalaxyError(error, "HTTP error")
        assert galaxy_error.http_code == http_code

    test_error_by_http_code(403)
    test_error_by_http_code(520)


# Generated at 2022-06-12 22:03:31.127229
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    galaxy_err = GalaxyError(Exception("Testing Exception"), "Exception message")
    assert galaxy_err.http_code == 500
    assert galaxy_err.message == 'Exception message (HTTP Code: 500, Message: Testing Exception Code: Unknown)'
    assert galaxy_err.url == ''

    try:
        raise GalaxyError(Exception("Testing Exception"), "Exception message")
    except GalaxyError as galaxy_err:
        assert galaxy_err.http_code == 500
        assert galaxy_err.message == 'Exception message (HTTP Code: 500, Message: Testing Exception Code: Unknown)'
        assert galaxy_err.url == ''



# Generated at 2022-06-12 22:03:42.652486
# Unit test for function g_connect
def test_g_connect():
    # Create a class that has the needed attributes to use the g_connect wrapper
    class GalaxyBase(object):
        def __init__(self):
            self.name = 'test_galaxy'
            self.api_server = 'https://galaxy.ansible.com'
            self._available_api_versions = {}

        def _call_galaxy(self, url, method, error_context_msg, cache=False):
            if url == 'https://galaxy.ansible.com/api/':
                return {'available_versions': {u'v1': u'v1/'}}
            elif url == 'https://galaxy.ansible.com/api/v1/':
                return {'collections': 'v1 collections'}

# Generated at 2022-06-12 22:03:50.518211
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    exception = GalaxyError(
        'too many requests',
        http_code=429,
        url='https://cloud.redhat.com/api/galaxy/namespaces/',
    )
    assert is_rate_limit_exception(exception) is True
    exception = GalaxyError(
        'too many requests',
        http_code=403,
        url='https://cloud.redhat.com/api/galaxy/namespaces/',
    )
    assert is_rate_limit_exception(exception) is False


# For backwards-compatibility

# Generated at 2022-06-12 22:04:02.104952
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('https://galaxy.ansible.com:443/api/') == 'galaxy.ansible.com:443'
    assert get_cache_id('https://galaxy.ansible.com/api/') == 'galaxy.ansible.com'
    assert get_cache_id('https://galaxy.ansible.com') == 'galaxy.ansible.com'
    assert get_cache_id('https://galaxy.ansible.com:80/api/') == 'galaxy.ansible.com:80'
    assert get_cache_id('https://user:pass@galaxy.ansible.com:443/api/') == 'galaxy.ansible.com:443'

# Generated at 2022-06-12 22:04:11.024894
# Unit test for function g_connect
def test_g_connect():
    # Test that versions are checked correctly
    success = []
    expect = ['v1']
    galaxy = Galaxy(None, None, None)
    galaxy.api_server = 'foo'
    galaxy._available_api_versions = {'v1': 'v1'}
    @g_connect(expect)
    def _test1(self, *args, **kwargs):
        success.append(True)
        return _test1
    galaxy._test1()
    assert success == [True]

    success = []
    expect = ['v2']
    @g_connect(expect)
    def _test2(self, *args, **kwargs):
        success.append(True)
        return _test2
    try:
        galaxy._test2()
    except AnsibleError:
        pass
    assert success == []

# Generated at 2022-06-12 22:04:23.144915
# Unit test for method __lt__ of class GalaxyAPI

# Generated at 2022-06-12 22:04:30.920757
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    # test init with keyword argument
    galaxy_api = GalaxyAPI('http://galaxy.ansible.com', 'user', 'pass')
    assert galaxy_api.api_server == 'http://galaxy.ansible.com'
    assert galaxy_api.username == 'user'
    assert galaxy_api.password == 'pass'

    # test init without keyword argument
    galaxy_api = GalaxyAPI('http://galaxy.ansible.com', 'user', 'pass')
    assert galaxy_api.api_server == 'http://galaxy.ansible.com'
    assert galaxy_api.username == 'user'
    assert galaxy_api.password == 'pass'

