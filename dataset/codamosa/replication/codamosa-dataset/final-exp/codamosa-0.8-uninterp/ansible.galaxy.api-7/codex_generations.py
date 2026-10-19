

# Generated at 2022-06-12 21:56:17.454476
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    url = "https://ansible.galaxy/api/v2/users/ansible/collections/azure%3Aazcollection/versions/"
    http_error = HTTPError(url, 404, 'Not Found', {}, None)
    message = 'Not found'
    galaxy_error = GalaxyError(http_error, message)
    assert galaxy_error.http_code == 404
    assert galaxy_error.url == url
    assert galaxy_error.message == 'Not found (HTTP Code: 404, Message: Not Found Code: Unknown)'

    url = "https://ansible.galaxy/api/v3/users/ansible/collections/azure%3Aazcollection/versions/"
    http_error = HTTPError(url, 404, 'Not Found', {}, None)
    message = 'Not found'
    galaxy_error = Galaxy

# Generated at 2022-06-12 21:56:21.749809
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    exception = GalaxyError("", http_code=429)
    assert is_rate_limit_exception(exception)
    exception = GalaxyError("", http_code=520)
    assert is_rate_limit_exception(exception)
    exception = GalaxyError("", http_code=403)
    assert not is_rate_limit_exception(exception)



# Generated at 2022-06-12 21:56:23.597042
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxyapi = GalaxyAPI()
    assert galaxyapi.__lt__(galaxyapi) == NotImplemented


# Generated at 2022-06-12 21:56:29.046219
# Unit test for function get_cache_id
def test_get_cache_id():
    assert get_cache_id('http://galaxy.ansible.com') == 'galaxy.ansible.com:'
    assert get_cache_id('https://galaxy.ansible.com:8080') == 'galaxy.ansible.com:8080'
    assert get_cache_id('https://user:password@galaxy.ansible.com:8080') == 'galaxy.ansible.com:8080'



# Generated at 2022-06-12 21:56:36.651956
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    test_data = [{'code': 1, 'message': 'message', 'default': 'default'}, {'code': 2, 'message': 'message'},
                 {'message': 'message'}]
    url = 'http://localhost/v1'
    for data in test_data:
        class TestHTTPMessage:
            def __init__(self, code, reason):
                self.code = code
                self.reason = reason
            def read(self):
                return json.dumps(data)
            def geturl(self):
                return url
        error = GalaxyError(TestHTTPMessage(1, 'reason'), 'message')
        assert error.http_code == 1
        assert error.url == 'http://localhost/v1'

# Generated at 2022-06-12 21:56:40.650500
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # Scenario: A message is not provided
    # Expect: The message property is set to an empty string
    try:
        GalaxyError(HTTPError('http://github.com', 500, 'server error', {}, None), '')
    except AnsibleError as e:
        assert e.message == ''


# Generated at 2022-06-12 21:56:46.984330
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    g_e = GalaxyError(HTTPError('http://example.com', 500, 'Internal Server Error', {}, None), 'HTTP Error')
    assert g_e.http_code == 500
    assert isinstance(g_e.url, string_types)
    assert isinstance(g_e.message, string_types)
    assert g_e.message.startswith('HTTP Error')
    assert g_e.message.endswith('(HTTP Code: 500, Message: Internal Server Error)')



# Generated at 2022-06-12 21:56:50.310258
# Unit test for function is_rate_limit_exception
def test_is_rate_limit_exception():
    e = GalaxyError({"code": 429, "message": "uh oh"}, http_code=429)
    assert is_rate_limit_exception(e)


# Generated at 2022-06-12 21:56:59.200035
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    if os.environ.get('GALAXY_SERVER', None) == 'https://galaxy.ansible.com':
        return

    galaxy = GalaxyAPI(os.environ.get('GALAXY_SERVER', None), token=os.environ.get('GALAXY_TOKEN', None))
    assert galaxy.api_server == os.environ.get('GALAXY_SERVER', None), "Constructor sets api_server properly"
    assert galaxy.token == os.environ.get('GALAXY_TOKEN', None), "Constructor sets token properly"
    assert galaxy.available_api_versions['v2'] == 'api/v2', "Constructor sets API V2 properly"

# Generated at 2022-06-12 21:57:00.106442
# Unit test for function g_connect
def test_g_connect():
    assert True == True

# Generated at 2022-06-12 21:57:29.769469
# Unit test for function g_connect
def test_g_connect():
    def test_func(self,*args,**kwargs):
        return 0
    test_func = g_connect(['v1','v2'])(test_func)
    assert test_func(None) == 0


# Generated at 2022-06-12 21:57:34.891742
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    http_error = HTTPError(url='http://localhost/api/v2/',
                           code=404,
                           msg='Not Found',
                           hdrs=[('Content-Type', 'application/json')],
                           fp=None)
    http_error.read = lambda: to_bytes(json.dumps({
        'code': 404,
        'message': 'Not found.',
    }))
    error_msg = 'Error when creating a repository'
    ex = GalaxyError(http_error, message=error_msg)
    assert ex.message == error_msg + ' (HTTP Code: 404, Message: Not found. Code: 404)'

# Generated at 2022-06-12 21:57:36.592982
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    galaxy_api = GalaxyAPI()
    assert galaxy_api < GalaxyAPI()



# Generated at 2022-06-12 21:57:38.934645
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    g1 = GalaxyAPI(name='galaxy', api_server='galaxy.example.com')
    g2 = GalaxyAPI(name='galaxy_two', api_server='galaxy_two.example.com')
    assert g1 < g2



# Generated at 2022-06-12 21:57:51.310177
# Unit test for function g_connect
def test_g_connect():
    class FakeGalaxyAPI(object):
        def __init__(self):
            self.api_server = None
            self.name = 'mock'
            self._available_api_versions = None

        def _call_galaxy(self, url, method=None, data=None, cache=False, error_context_msg=None):
            if url == 'https://galaxy.ansible.com/api/':
                return {'available_versions': {u'v1': u'v1/'}}
            elif url == 'https://api.galaxy.example.com/api/':
                return {'available_versions': {u'v1': u'v1/', u'v2': u'v2/'}}

# Generated at 2022-06-12 21:57:56.828809
# Unit test for function g_connect
def test_g_connect():
    def test_method():
        pass
    g_connect_wraped=g_connect(['v1', 'v2'])(test_method)
    galaxy_api = GalaxyAPI('https://galaxy.ansible.com')
    galaxy_api._available_api_versions = {u'v1': u'v1/', u'v2': u'v2/'}
    g_connect_wraped(galaxy_api)



# Generated at 2022-06-12 21:58:02.852768
# Unit test for function g_connect
def test_g_connect():
    API = 'https://galaxy.ansible.com'
    COLLECTION_NAME = 'hello'
    COLLECTION_VERSION = '0.1.0'
    a_inst = Galaxy(api_server=API, token=None)
    b_inst = Galaxy(api_server=API, token=None)
    c_inst = Galaxy(api_server=API, token=None)

    @g_connect(versions=[u'v1'])
    def g_connect_method(self):
        return self._available_api_versions

    @g_connect(versions=[u'v2'])
    def g_connect_method_v2(self):
        return self._available_api_versions

    assert g_connect_method(a_inst) == {u'v1': u'v1/'}


# Generated at 2022-06-12 21:58:10.980024
# Unit test for function g_connect
def test_g_connect():
    class GalaxyConnection(object):
        _available_api_versions = None
        api_server = 'https://galaxy-server.com'
        name = 'galaxy'
        def _call_galaxy(self, *args, **kwargs):
            pass

    class Test(object):
        def test_method(self, *args, **kwargs):
            pass

    test = Test()
    test.test_method = g_connect([u'v2'])(test.test_method)

    test._galaxy_connection = GalaxyConnection()
    test._galaxy_connection._available_api_versions = {u'v2': u'v2/'}

    test.test_method()


# Generated at 2022-06-12 21:58:15.606376
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    try:
        error = HTTPError('https://localhost/', 404, 'Failed', {}, None)
        raise GalaxyError(error, 'Detail error message')
    except AnsibleError as e:
        assert 'Detail error message (HTTP Code: 404, Message: Failed)' == to_native(e)



# Generated at 2022-06-12 21:58:21.292353
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    httpError = HTTPError('url', 400, 'Reason', [], 'Response')
    galaxyError = GalaxyError(httpError, 'message')
    assert isinstance(galaxyError, GalaxyError) == True
    assert galaxyError.http_code == 400
    assert galaxyError.url == 'url'
    assert galaxyError.message == 'message (HTTP Code: 400, Message: Reason)'


# Generated at 2022-06-12 21:58:55.825934
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    from requests import Request, Response
    url = 'https://galaxy.ansible.com/v2/api/'
    headers = {'Content-Type': 'application/json', 'User-Agent': user_agent()}
    req = Request('GET', url, headers=headers).prepare()
    resp = Response()
    resp.status_code = 404
    resp._content = b'{"message": "Not Found", "code": "not_found"}'
    http_error = HTTPError(url, resp.status_code, resp.reason, resp.headers, fp=resp.raw)
    error = GalaxyError(http_error, "test")
    assert error.http_code == 404
    assert error.url == url
    assert error.message == "test (HTTP Code: 404, Message: Not Found Code: not_found)"


# Generated at 2022-06-12 21:59:01.315005
# Unit test for function get_cache_id
def test_get_cache_id():
    assert 'ansible.com' == get_cache_id('http://ansible.com')
    assert 'ansible.com' == get_cache_id('https://ansible.com')
    assert 'ansible.com:443' == get_cache_id('https://ansible.com:443')
    assert 'ansible.com:443' == get_cache_id('https://ansible.com:443/')
    assert 'ansible.com:443' == get_cache_id('https://ansible.com:443/test')
    assert 'ansible.com:443' == get_cache_id('https://ansible.com:443/test/')
    assert 'ansible.com:443' == get_cache_id('https://ansible.com:443/test#fragment')

# Generated at 2022-06-12 21:59:07.110102
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    api1 = GalaxyAPI(
        name='galaxy_test1',
        api_server='https://galaxy-test1.com',
    )
    api2 = GalaxyAPI(
        name='galaxy_test2',
        api_server='https://galaxy-test2.com',
    )
    assert api1 < api2


# Generated at 2022-06-12 21:59:11.648344
# Unit test for function g_connect
def test_g_connect():
    versions = [u'v2',u'v3']
    def f(x):
        print("This is the function %s"%x)

    rt_f = g_connect(versions)(f)
    rt_f("test")
test_g_connect()



# Generated at 2022-06-12 21:59:18.025255
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    f = GalaxyAPI(galaxy_context=GalaxyTestContext(), oauth_token=None, ignore_certs=False)
    g = GalaxyAPI(galaxy_context=GalaxyTestContext(), oauth_token=None, ignore_certs=False)
    g._api_server = 'abc'
    f._api_server = 'def'
    assert f < g
    assert f <= g
    assert g > f
    assert g >= f


# Generated at 2022-06-12 21:59:25.696211
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    expexted_result = True
    galaxy_api_1 = GalaxyAPI(name='test_galaxy_api_1', api_server='https://1_galaxy_server.org', force_api_version='')
    galaxy_api_2 = GalaxyAPI(name='test_galaxy_api_2', api_server='https://2_galaxy_server.org', force_api_version='')
    actual_result = galaxy_api_1 < galaxy_api_2

    assert expexted_result == actual_result


# Generated at 2022-06-12 21:59:33.212395
# Unit test for function get_cache_id
def test_get_cache_id():
    # should be empty string for no URL
    assert get_cache_id(None) == ''
    # for a simple URL, should return the host name with no port
    assert get_cache_id('https://www.ansible.com') == 'www.ansible.com'
    assert get_cache_id('https://www.ansible.com:443') == 'www.ansible.com'
    assert get_cache_id('https://www.ansible.com:80') == 'www.ansible.com'
    assert get_cache_id('https://www.ansible.com:8443') == 'www.ansible.com:8443'
    # should not attempt to parse credentials
    assert get_cache_id('https://user:pass@www.ansible.com') == 'www.ansible.com'
# Unit

# Generated at 2022-06-12 21:59:45.474504
# Unit test for function g_connect
def test_g_connect():
    class TestGalaxy():
        _available_api_versions = []
        api_server = ""
        name = "test_galaxy"
        def _call_galaxy(self, *args, **kwargs):
            if self.api_server == "https://galaxy.ansible.com":
                return {"available_versions": {"v3": "v3/"}}

        def _get_error_context_message(self, *args, **kwargs):
            pass
    galaxy = TestGalaxy()
    galaxy.api_server = "https://galaxy.ansible.com"
    decorated_function = g_connect(['v3'])(lambda self, *args, **kwargs: {"worked": True})
    assert decorated_function(galaxy) == {"worked": True}


# Generated at 2022-06-12 21:59:57.590664
# Unit test for function g_connect
def test_g_connect():
    """
    function g_connect's unit test
    """
    def decorator(method):
        def wrapped(self, *args, **kwargs):
            if not self._available_api_versions:
                display.vvvv("Initial connection to galaxy_server: %s" % self.api_server)

                # Determine the type of Galaxy server we are talking to. First try it unauthenticated then with Bearer
                # auth for Automation Hub.
                n_url = self.api_server
                error_context_msg = 'Error when finding available api versions from %s (%s)' % (self.name, n_url)

# Generated at 2022-06-12 22:00:06.147964
# Unit test for function cache_lock
def test_cache_lock():
    global test_cache_lock_count
    test_cache_lock_count = 0

    @cache_lock
    def test_cache_lock_func():
        global test_cache_lock_count
        test_cache_lock_count += 1

    t1 = threading.Thread(target=test_cache_lock_func)
    t2 = threading.Thread(target=test_cache_lock_func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    assert test_cache_lock_count == 1



# Generated at 2022-06-12 22:01:16.015404
# Unit test for function g_connect
def test_g_connect():
    class Test(object):
        def __init__(self):
            self.api_server = 'https://galaxy.ansible.com'
            self._available_api_versions = {}

        @g_connect(['v1', 'v2'])
        def foo(self):
            return True

        @g_connect(['v1', 'v2'])
        def foo1(self):
            return True

        @g_connect(['v1', 'v2', 'v3'])
        def foo3(self):
            return True

        def _call_galaxy(self, url, *args, **kwargs):
            return {'available_versions': {'v1': '/api/v1/', 'v2': '/api/v2/'}}

    test_obj = Test()
    assert test_obj

# Generated at 2022-06-12 22:01:21.715088
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    class TestHTTPError(Exception):
        def __init__(self):
            self.code = 123
            self.reason = 'HTTP Error'

        def read(self):
            return json.dumps(dict(message='Galaxy Error'))

        def geturl(self):
            return '/v2/foobar'

    assert isinstance(GalaxyError(TestHTTPError(), 'Test Message'), AnsibleError)
    assert isinstance(GalaxyError(TestHTTPError(), 'Test Message'), GalaxyError)



# Generated at 2022-06-12 22:01:27.277947
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    # Error for bad Galaxy server responses.
    # Create an error that represents a HTTP error code: message
    http_code = 443
    message = "test message"
    http_error = HTTPError("http://test.com:8080/path", http_code, message, None, None)
    galaxyError = GalaxyError(http_error, "error")
    assert isinstance(galaxyError, GalaxyError)
    assert galaxyError.http_code == http_code
    assert galaxyError.url == http_error.geturl()
    assert galaxyError.message == "error (HTTP Code: 443, Message: test message)"


# Generated at 2022-06-12 22:01:37.710440
# Unit test for function g_connect
def test_g_connect():
    versions = ['v1', 'v2']
    versions_not_supported = ['v5']
    versions_invalid = ['v2', 'v3']

    # Test case 1: methods only support v1 and v2 API, Galaxy API supports v1 and v2 API
    @g_connect(versions=versions)
    def test_method_1():
        pass
    test_obj_1 = GalaxyServer()
    test_obj_1._available_api_versions = {u'v1': u'v1/', u'v2': u'v2/'}
    try:
        test_method_1(test_obj_1)
    except: #pylint: disable=bare-except
        assert False, 'The function test_method_1 should be called'

    # Test case 2: methods support v1 and v2

# Generated at 2022-06-12 22:01:47.967886
# Unit test for function get_cache_id
def test_get_cache_id():
    url = 'https://galaxy.ansible.com/api/v1/collections'
    url2 = 'https://localhost:8088'
    url3 = 'https://localhost'
    url4 = 'https://username:password@galaxy.ansible.com'
    url5 = 'https://galaxy.ansible.com/api/v1/collections/'
    assert get_cache_id(url) == 'galaxy.ansible.com'
    assert get_cache_id(url2) == 'localhost:8088'
    assert get_cache_id(url3) == 'localhost'
    assert get_cache_id(url4) == 'galaxy.ansible.com'
    assert get_cache_id(url5) == 'galaxy.ansible.com'
test_get_cache_id()

# Generated at 2022-06-12 22:01:52.949310
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():  # type: () -> None
    g = GalaxyAPI("https://galaxy.ansible.com/api", "username", "secret")
    assert g.api_server == "https://galaxy.ansible.com/api"
    assert g.username == "username"
    assert g.password == "secret"
    assert g.verify_ssl is True

# Generated at 2022-06-12 22:02:02.841394
# Unit test for function g_connect
def test_g_connect():
    class Connection():
        def __init__(self, name, api_server, verify_ssl=True):
            self._available_api_versions = {}
            self.name = name
            self.api_server = api_server
            self._available_api_versions = {}
            self.verify_ssl = verify_ssl
            self._session = None

        def _call_galaxy(self, url, method='GET', data=None, error_context_msg=None, cache=True):
            pass

    class Test():
        def __init__(self):
            self.test = True

        @g_connect(versions=['v1', 'v2'])
        def test(self):
            pass

    a = Connection(name='test', api_server='https://galaxy.ansible.com')
    b = Test()

# Generated at 2022-06-12 22:02:10.882944
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    # Arrange
    galaxy_api = GalaxyAPI(name='test', api_server='test', token='test')
    galaxy_api.__dict__['token'] = 'test'
    galaxy_api_2 = GalaxyAPI(name='test', api_server='test', token='test')
    galaxy_api_2.__dict__['token'] = 'test'

    # Act
    response = galaxy_api.__lt__(galaxy_api_2)

    # Assert
    assert response == False

# Generated at 2022-06-12 22:02:14.219811
# Unit test for function cache_lock
def test_cache_lock():
    lock = threading.Lock()
    assert not lock.locked()

    @cache_lock
    def _lock():
        assert lock.locked()

    _lock()


# Generated at 2022-06-12 22:02:25.612067
# Unit test for method __lt__ of class GalaxyAPI
def test_GalaxyAPI___lt__():
    """Test if ``GalaxyAPI.__lt__`` method behaves as expected"""
    # we want to test only the user-originated comparison
    # pylint: disable=protected-access
    
    # we should use the class from the tested module
    import ansible_galaxy.galaxy.api as tested_api_module
    tested_GalaxyAPI_class = tested_api_module.GalaxyAPI
    
    # create objects that should compare to be equal
    aa = tested_GalaxyAPI_class('tatiana')
    bb = tested_GalaxyAPI_class('tatiana')
    
    c = aa.__lt__(bb)
    assert(c == False), "`GalaxyAPI.__lt__` method behaves in an unexpected way"
    d = bb.__lt__(aa)

# Generated at 2022-06-12 22:03:18.734145
# Unit test for function cache_lock
def test_cache_lock():
    """
    This should return True if the cache_lock is available.
    """
    display.vvvv('Testing cache lock')
    return True



# Generated at 2022-06-12 22:03:23.942813
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    error_msg = 'test message'
    http_error = HTTPError(None, error_msg, None, None, None)
    galaxy_error = GalaxyError(http_error, error_msg)
    assert galaxy_error.http_code == http_error.code
    assert galaxy_error.url == http_error.geturl()

# https://github.com/ansible/ansible/blob/stable-2.9/lib/ansible/module_utils/six/moves/urllib/request.py#L569-L581

# Generated at 2022-06-12 22:03:35.558807
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    galaxy_error = GalaxyError(HTTPError("http://bad_url", 500, "msg", {}, None), "Galaxy error")
    assert galaxy_error.http_code == 500
    assert galaxy_error.url == "http://bad_url"
    assert galaxy_error.message == "Galaxy error (HTTP Code: 500, Message: msg)"

    galaxy_error = GalaxyError(HTTPError("http://bad_url", 500, "msg", {}, None), "Galaxy error")
    galaxy_error._http_error_obj = HTTPError("http://bad_url", 500, "msg", {}, StringIO("""
    {
        "detail": "error detail",
        "title": "error title",
        "code": "error code"
    }
    """))
    assert galaxy_error.http_code == 500
    assert galaxy

# Generated at 2022-06-12 22:03:41.343133
# Unit test for constructor of class GalaxyError
def test_GalaxyError():
    import test.utils.unit as unit
    import io

    def fake_urlopen(url, *args, **kwargs):
        ''' Fake wrapper around urllib2.urlopen that produces a fake HTTPError. '''
        try:
            raise HTTPError(url, 500, '', {}, io.BytesIO(to_bytes('{ "default": "default" }')))

        except (IOError, ValueError):
            raise HTTPError(url, 500, '', {}, io.BytesIO(to_bytes('')))

    unit.patch_module('ansible.galaxy.api.urlopen', fake_urlopen)


# Generated at 2022-06-12 22:03:51.983533
# Unit test for function g_connect
def test_g_connect():
    versions = ['v2']
    def decorator(method):
        def wrapped(self, *args, **kwargs):
            if not self._available_api_versions:
                display.vvvv("Initial connection to galaxy_server: %s" % self.api_server)

                # Determine the type of Galaxy server we are talking to. First try it unauthenticated then with Bearer
                # auth for Automation Hub.
                n_url = self.api_server
                error_context_msg = 'Error when finding available api versions from %s (%s)' % (self.name, n_url)


# Generated at 2022-06-12 22:04:03.600338
# Unit test for function cache_lock
def test_cache_lock():
    from ansible.module_utils.common.collections import ImmutableDict

    dummy_shared_mutable_dict = {'a': 'one'}
    dummy_cls_mutable_dict = ImmutableDict({'a': 'two'})
    dummy_global_mutable_dict = {}
    dummy_global_counter = 0

    def dummy_func(shared_dict, cls_dict, cond_counter, dummy_counter, *args, **kwargs):
        shared_dict['a'] = 'three'
        cls_dict['a'] = 'four'
        cond_counter['a'] = 'five'
        dummy_counter += 1
        return shared_dict, cls_dict, cond_counter, dummy_counter

    # Apply lock decorator to function

# Generated at 2022-06-12 22:04:04.936509
# Unit test for function cache_lock
def test_cache_lock():
    wrapped()
    _CACHE_LOCK()



# Generated at 2022-06-12 22:04:09.100862
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    galaxy = GalaxyAPI('test', 'https://galaxy.server.com')
    assert galaxy.name == 'test'
    assert galaxy.api_server == 'https://galaxy.server.com'
    assert not galaxy.verify_ssl
    galaxy = GalaxyAPI('test', 'https://galaxy.server.com', verify_ssl=True)
    assert galaxy.verify_ssl



# Generated at 2022-06-12 22:04:12.551585
# Unit test for function g_connect
def test_g_connect():
    class Foo:
        name = 'foo'
        api_server = 'http://foo.com'
        _available_api_versions = None

        @g_connect(['v2', 'v1'])
        def run(self):
            return self._available_api_versions

    foo = Foo()
    assert foo.run()



# Generated at 2022-06-12 22:04:16.142780
# Unit test for constructor of class GalaxyAPI
def test_GalaxyAPI():
    api = GalaxyAPI(url='https://foo.galaxy', token='bar')

    assert api.url == 'https://foo.galaxy'
    assert api.token == 'bar'
