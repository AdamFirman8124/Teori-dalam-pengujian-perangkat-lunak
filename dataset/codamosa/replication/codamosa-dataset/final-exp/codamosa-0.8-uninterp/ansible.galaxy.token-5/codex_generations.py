

# Generated at 2022-06-12 22:05:12.290426
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    _token = KeycloakToken(access_token=None, auth_url=None, validate_certs=True, client_id=None)
    headers = _token.headers()
  

# Generated at 2022-06-12 22:05:12.857281
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
   return True

# Generated at 2022-06-12 22:05:19.189776
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # TODO: mock the http call
    # http = Mock()
    # http.request.return_value = ( status_code, data )
    #
    # urllib2.build_opener.return_value = http
    #
    # c = KeycloakToken( access_token, auth_url, cert_valid='False' )
    # t = c.get()
    # assert t == access_token
    pass

# Generated at 2022-06-12 22:05:24.831458
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Test if KeycloakToken.headers() returns what is expected
    # for a given input
    assert KeycloakToken("abc", "https://example.com",
                         False, "example").headers() == {'Authorization': 'Bearer abc'}
    assert KeycloakToken("abc", "https://example.com").headers() == {'Authorization': 'Bearer abc'}
    assert KeycloakToken("abc", auth_url="https://example.com").headers() == {'Authorization': 'Bearer abc'}

# Generated at 2022-06-12 22:05:27.649302
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    gt.set(token='test')
    assert isinstance(gt.get(), str)
    # TODO: Mock and write a real test

# Generated at 2022-06-12 22:05:40.557731
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # TODO: mock the open_url return
    #  - make a real auth_url with a token in the test_data dir
    #  - run the test from the galaxy root (with the .tox env)
    #  - make this run before package installation and open_url call removed from method
    from unittest import TestCase
    from unittest.mock import Mock, patch

    class KeycloakTokenGetTest(TestCase):
        def test_get(self):
            display.vvv = Mock()
            open_url = Mock()
            with patch('galaxy_token.open_url', open_url):
                ktc = KeycloakToken(access_token='12345', auth_url='http://foo.com')
                token = ktc.get()

# Generated at 2022-06-12 22:05:46.724941
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_client_id = 'test_client'
    auth_url = 'www.test-auth-url.com'
    access_token = 'test'
    test_token = KeycloakToken(access_token=access_token, auth_url=auth_url, client_id=test_client_id)
    assert test_token._form_payload() == "grant_type=refresh_token&client_id=%s&refresh_token=%s" % (test_client_id, access_token)

# Generated at 2022-06-12 22:05:58.938415
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # get() is to return _token
    keycloak_token = KeycloakToken(access_token='access_token', auth_url='auth_url')
    keycloak_token._token = 'token'
    assert keycloak_token.get() == 'token'

    # get() is to call set()
    keycloak_token = KeycloakToken(access_token='access_token', auth_url='auth_url')
    # mock open_url
    def open_url(url, data, validate_certs, method, http_agent):
        class Response():
            def read(self):
                return '{"access_token": "token"}'

        return Response()
    keycloak_token.open_url = open_url
    assert keycloak_token.get() == 'token'

# Unit test

# Generated at 2022-06-12 22:06:11.908685
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest

    class TestKeycloakToken(unittest.TestCase):
        class Response(object):
            def __init__(self, text):
                self.text = text

            def read(self):
                return self.text

        def test_get(self):
            access_token = 'foobar'
            auth_url = 'example.com'
            k = KeycloakToken(access_token=access_token, auth_url=auth_url)
            payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=%s' % access_token

# Generated at 2022-06-12 22:06:16.593252
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc_token = KeycloakToken(access_token='test')
    assert 'Authorization' in kc_token.headers()
    assert 'Bearer' in kc_token.headers()['Authorization']
    #assert kc_token.headers()['Authorization'] == 'Bearer test'


# Generated at 2022-06-12 22:06:29.461991
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token_data = {'access_token': 'foo',
                  'token_type': 'Bearer',
                  'expires_in': 7200,
                  'refresh_expires_in': 1800,
                  'refresh_token': 'bar',
                  'not-before-policy': 0,
                  'session_state': 'session_state',
                  'scope': 'openid'}
    token = KeycloakToken(**token_data)
    token_headers = token.headers()
    assert token_headers['Authorization'] == 'Bearer foo', 'Keycloak token not properly formatted'



# Generated at 2022-06-12 22:06:32.120450
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    g = GalaxyToken()
    g.config['token'] = 'test'
    g.save()
    config = g._read()
    assert config['token'] == 'test'

# Generated at 2022-06-12 22:06:39.314585
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:48.596865
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Testing with Access Token
    kct = KeycloakToken(access_token='foo')
    h = kct.headers()
    assert h['Authorization'] == 'Bearer foo'

    # Testing without token ('token' = None)
    kct.access_token = None
    h = kct.headers()
    assert h['Authorization'] == 'Bearer None'

    # Testing with no token
    kct.access_token = 'bar'
    kct._token = None
    h = kct.headers()
    assert h['Authorization'] == 'Bearer bar'


# Generated at 2022-06-12 22:07:00.945570
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    # Test with a 'mock' http request.
    def _open_url(url, data, method, validate_certs, url_username, url_password, headers, force_basic_auth, http_agent):

        # Initialize a HTML object
        class HTML(object):
            pass
        html = HTML()

        # Build a response

# Generated at 2022-06-12 22:07:09.405906
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import responses
    import mock


# Generated at 2022-06-12 22:07:10.676214
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    pass

# Generated at 2022-06-12 22:07:17.534488
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    KT = KeycloakToken('MYSUPERTOKEN',
                       'https://cloud.redhat.com/api/automation-hub/v1/token?client_id=cloud-services',
                       validate_certs=True,
                       client_id='cloud-services')
    assert KT.headers() == {'Authorization': 'Bearer MYSUPERTOKEN'}


# Generated at 2022-06-12 22:07:23.174410
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken('dummykey', auth_url='https://auth.url.com/auth/realms/realm/protocol/openid-connect/token')
    kct._form_payload = lambda: 'grant_type=refresh_token&client_id=cloud-services&refresh_token=dummykey'
    kct.get()
    assert kct._token == 'dummytoken'

# Generated at 2022-06-12 22:07:28.960215
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken(token=None)
    config = {
        "host": "https://cloud.redhat.com",
        "token": "adfadf"
    }
    gt.config = config
    gt.save()
    with open(gt.b_file, 'r') as f:
        assert yaml_load(f) == config

# Generated at 2022-06-12 22:07:36.093029
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc = KeycloakToken(access_token='123456789', auth_url='example.com',
                       validate_certs=True, client_id='myclient')
    assert kc.headers() == {'Authorization': 'Bearer 123456789'}

# Generated at 2022-06-12 22:07:46.844023
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    class ConfigObj(object):
        def __init__(self):
            self.data = {}

        def update(self, data):
            self.data.update(data)

        def get(self, key):
            return self.data.get(key, None)

    class MockedOs(object):
        def __init__(self):
            self.path = MockedPath()

    class MockedPath(object):
        def __init__(self):
            self.exists = False

        def isfile(self, path):
            return self.exists

    path = MockedPath()
    m_os = MockedOs()
    m_os.path = path
    galaxy_token = GalaxyToken()
    galaxy_token._os = m_os
    galaxy_token._token = "token"
    galaxy_token._

# Generated at 2022-06-12 22:07:54.745633
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
  client_id = "test"
  access_token = "test"
  auth_url = "https://test"
  validate_certs = False

  keycloak_token = KeycloakToken(access_token, auth_url, validate_certs, client_id)
  token = keycloak_token.get()
  print("Token:", token)

if __name__ == "__main__":
  test_KeycloakToken_get()

# Generated at 2022-06-12 22:07:59.086201
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    t = KeycloakToken(access_token='1', auth_url='2')
    result = t.headers()
    assert "Authorization" in result
    assert result['Authorization'].startswith('Bearer ')
    assert result['Authorization'].endswith(t.get())


# Generated at 2022-06-12 22:08:02.920408
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(auth_url='https://auth.testing.com/auth/realms/sso/protocol/openid-connect/token',
                          access_token='random')
    token.get()

# Generated at 2022-06-12 22:08:09.734428
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create empty galaxy token file
    filepath = C.GALAXY_TOKEN_PATH
    galaxy_token_file = open(filepath, 'w')
    galaxy_token_file.close()

    # Initialize galaxy token class
    galaxy_token = GalaxyToken()

    # Save the token and verify file is not empty
    galaxy_token.set('1234')
    assert os.path.getsize(filepath) > 0

    # Cleanup
    os.remove(filepath)

# Generated at 2022-06-12 22:08:20.061466
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    # test that save function works with unicode objects
    token.config['token'] = {'unicode': u'\u5168\u5c40\u4fe1\u606f\u4f20\u9001'}
    token.save()

    # test that save function works with non-ascii characters
    token.config['token'] = {'list': [u'\u5168', u'\u5c40', u'\u4fe1', u'\u606f', u'\u4f20', u'\u9001']}
    token.save()

    # test that save function works with byte strings

# Generated at 2022-06-12 22:08:22.483912
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='foo_access')
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer foo_access'

# Generated at 2022-06-12 22:08:25.773549
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = 'mYsUpErSeCrEtClOuD'
    k = KeycloakToken(access_token=token)
    assert k.headers() == {'Authorization': 'Bearer mYsUpErSeCrEtClOuD'}


# Generated at 2022-06-12 22:08:34.992539
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import tempfile

    b_tmpfile = os.path.join(tempfile.gettempdir(), 'test_token')
    test_token = GalaxyToken()
    test_token.b_file = b_tmpfile
    config = {'token': 'mytocken'}
    test_token._config = config
    test_token.save()
    with open(test_token.b_file, 'r') as f:
        yaml_config = yaml_load(f)

    assert yaml_config == config, 'Config saved incorrectly'
    os.remove(b_tmpfile)

# Generated at 2022-06-12 22:08:44.876527
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kctoken = KeycloakToken("my_access_token", "http://fake.url", False)
    assert kctoken.get() == "my_access_token"


# Generated at 2022-06-12 22:08:51.863252
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    url = 'http://localhost:8080/auth/realms/master/protocol/openid-connect/token'

# Generated at 2022-06-12 22:08:57.130423
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:09:05.394055
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Return a mock open object that mocks the method 'write' and 'close'
    class mock_open:
         def __init__(self):
             self.data = ""
         def __call__(self, filename):
             return self
         def write(self, string):
             self.data = self.data + string
         def close(self):
             self.data = ""

    # Save a token and test if data is empty
    open_orginal = open
    open = mock_open()
    galax = GalaxyToken("test_token")
    galax.save()
    assert open.data == ""

    # Save a token and test if data is written correctly
    galax.set("1234567890")
    galax.save()
    assert open.data == "token: 1234567890\n"

# Generated at 2022-06-12 22:09:11.962806
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token_file = '/tmp/galaxy.token'
    token = 'yumyum'

    g = GalaxyToken(token)
    g.b_file = token_file

    g.save()
    with open(g.b_file, 'r') as f:
        raw_data = f.read()

    assert json.loads(raw_data)['token'] == token

# Generated at 2022-06-12 22:09:24.258681
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''
    test ansible.galaxy token save
    '''
    import os
    import shutil
    import tempfile

    t_file = tempfile.NamedTemporaryFile()
    t_file.close()

    # Use temp token file path
    C.GALAXY_TOKEN_PATH = t_file.name

    # Create token
    token = GalaxyToken()
    token_path = token.b_file

    # Delete token file
    try:
        os.remove(token_path)
    except OSError:
        pass

    # Write token
    token.set('123456789')

    # Test token
    with open(token_path, 'r') as f:
        token_file = f.read()
    assert token_file == 'token: 123456789\n'



# Generated at 2022-06-12 22:09:35.482635
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import httpretty
    from ansible.utils.hashing import secure_hash

    token = KeycloakToken('dummy_token')
    token.auth_url = 'https://auth.example.com'
    response = {
        'expires_in': 1800,
        'token_type': 'Bearer',
        'access_token': 'dummy_token',
        'refresh_expires_in': 1800,
        'refresh_token': 'dummy_refresh_token',
    }

    httpretty.enable()

# Generated at 2022-06-12 22:09:41.181127
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(access_token='abcdefgh')
    assert kt.headers() == {'Authorization': 'Bearer None'}
    kt.get()
    assert kt.headers() == {'Authorization': 'Bearer None'}
    kt._token = '12345678'
    assert kt.headers() == {'Authorization': 'Bearer 12345678'}

# Generated at 2022-06-12 22:09:50.548355
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    ua = "ansible/0.1 (linux)"
    token = KeycloakToken(auth_url="auth_url", access_token="access_token")
    headers = token.headers()

# Generated at 2022-06-12 22:09:53.290750
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token=None,
                          auth_url=None,
                          validate_certs=True,
                          client_id=None)
    assert token.headers() == {}

# Generated at 2022-06-12 22:10:12.649073
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # create an instance of KeycloakToken with an access_token
    k = KeycloakToken('access_token')
    # call method headers, should return a dictionary with key 'Authorization'
    headers = k.headers()
    assert 'Authorization' in headers
    # example of the value of key 'Authorization'
    assert headers['Authorization'] == 'Bearer access_token'

# Generated at 2022-06-12 22:10:23.572970
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest
    from ansible.galaxy.token import KeycloakToken
    import base64

    class KeycloakTokenTestCase(unittest.TestCase):
        def test_get(self):
            ktc = KeycloakToken(access_token='access_token')
            self.assertEqual(ktc._token, None)
            ktc.get()
            self.assertNotEqual(ktc._token, None)
            self.assertEqual(ktc._token, 'returned_access_token')

    # This function is called as a side effect. It would be nice to be
    # able to return the bytes of the encoded string, but we can't figure
    # out how to get the bytes (rather than the str) into the body of the
    # request. The best we can do is put a string into

# Generated at 2022-06-12 22:10:29.979380
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kctoken = KeycloakToken(auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                            access_token='offline_token',
                            validate_certs=True)
    headers = kctoken.headers()
    assert headers
    assert headers['Authorization'].startswith('Bearer ')

    kctoken = KeycloakToken(auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                            access_token='offline_token',
                            validate_certs=False)
    headers = kctoken.headers()
    assert headers
    assert headers['Authorization'].startswith('Bearer ')



# Generated at 2022-06-12 22:10:40.282775
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''
    Function to test get method of class KeycloakToken
    '''
    # remove the file if it exists
    try:
        os.remove('/tmp/token.txt')
    except OSError:
        pass

    # initialize KeycloakToken object with arguments
    kt = KeycloakToken(auth_url='http://some-url.redhat.com',
                       access_token='some-fake-key')

    # call to get() method
    kt.get()

    # check if the file was created
    assert os.path.isfile('/tmp/token.txt')


# Generated at 2022-06-12 22:10:48.030658
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import os
    t = tempfile.NamedTemporaryFile(delete=False)
    t_path = t.name
    t.close()
    os.chmod(t_path, S_IRUSR | S_IWUSR)  # owner has +rw
    g = GalaxyToken()
    g._config = {'Some': 'value'}
    g.b_file = to_bytes(t_path, errors='surrogate_or_strict')
    g.save()
    with open(t_path, 'r') as f:
        config = yaml_load(f)
    assert config == {'Some': 'value'}
    os.unlink(t_path)


# Generated at 2022-06-12 22:10:55.423245
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:10:59.903717
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''Test KeycloakToken class to get token'''

    token = KeycloakToken('dummy_token', auth_url='https://dummy_auth_url')
    if token.get() is None:
        raise Exception('Token is None')


# Generated at 2022-06-12 22:11:01.808770
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='abc')
    assert token.get() == 'abc'

# Generated at 2022-06-12 22:11:09.654835
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    config = {'token': 'token_x'}

    # Conditional Create
    path = 'launcher_test/test_GalaxyToken_save/token'
    fh = open(path, 'w')
    fh.close()

    try:
        gt = GalaxyToken()
        gt._config = config
        gt._token = config['token']
        gt.b_file = to_bytes(path, errors='surrogate_or_strict')
        gt.save()

        # Verify the content of the file
        f = open(path, 'r')
        content = f.read()
        f.close()

        assert content == "token: token_x\n"

    finally:
        # Remove the file
        os.remove(path)


# Generated at 2022-06-12 22:11:11.604312
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('foo')
    assert token.headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:11:40.080013
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.set("mytesttoken")
    token.save()
    assert token.get() == "mytesttoken"



# Generated at 2022-06-12 22:11:51.179663
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:11:55.832957
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken(auth_url="https://sso.redhat.com/auth/realms/redhat/protocol/openid-connect/token",
                                   access_token="refresh_token",
                                   validate_certs=True)
    assert "Authorization Bearer " in keycloak_token.headers().values()



# Generated at 2022-06-12 22:11:57.882677
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('foo')
    assert token.headers() == {'Authorization': 'Bearer foo'}



# Generated at 2022-06-12 22:12:02.212794
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='<fake access token>',
                          auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    token.get()

    # TODO: we will need a mock to test the responses from the server
    # - see test/utils/test_urls.py::test_open_url() for an example
    pass

# Generated at 2022-06-12 22:12:11.414939
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token_file = '/tmp/galaxy_token_test.yml'
    utg = GalaxyToken()
    utg.b_file = to_bytes(token_file, errors='surrogate_or_strict')

    # Check if the file was created and has only USER access
    utg.save()
    assert os.stat(token_file).st_mode == 33152

    # Check if the file was updated with the token info
    token = 'test_token'
    utg.set(token)
    assert utg.get() == token
    assert utg.config.get('token') == token
    assert utg.config.get('refresh_token') == None
    assert utg.config.get('token_url') == None
    assert utg.config.get('client_id') == None

   

# Generated at 2022-06-12 22:12:14.110722
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken("utf8_test")
    token.get()


# Generated at 2022-06-12 22:12:16.473267
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="MyTokenString")

    assert token.headers() == {'Authorization': 'Bearer MyTokenString'}

# Generated at 2022-06-12 22:12:22.246926
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Initialise test data
    kt = KeycloakToken('dummy_token', 'dummy_url')
    kt._form_payload = lambda: 'dummy_payload'
    kt._open_url = lambda x: 'dummy_token'

    # Call method to test
    kt.get()

    # Check method created a token
    assert kt._token == 'dummy_token'


# Generated at 2022-06-12 22:12:30.616262
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'wibble'
    auth_url = 'http://example.com/auth/realms/rhcc/protocol/openid-connect/token'
    validate_certs = True
    client_id = 'cloud-services'
    token = KeycloakToken(access_token, auth_url, validate_certs, client_id)

    test_headers = token.headers()

    auth_string = '%s %s' % (token.token_type, token.get())

    assert test_headers['Authorization'] == auth_string

# Generated at 2022-06-12 22:13:10.369405
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = '123'

    gt = GalaxyToken(token)
    gt.config = {'token': token}
    gt.b_file = '/tmp/' + token
    gt.save()

    gt_read = GalaxyToken(token)

    assert(gt_read.config['token'] == token)
    assert(gt_read.get() == token)

    os.unlink(gt.b_file)

# Generated at 2022-06-12 22:13:18.928773
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    gt.config = {'token': 'test_token'}
    assert gt.get() == gt.config.get('token')
    gt.save()
    assert os.path.isfile(gt.b_file)
    with open(gt.b_file, 'r') as f:
        config = yaml_load(f)
    gt.config = config
    assert gt.get() == gt.config.get('token')


# Generated at 2022-06-12 22:13:21.744266
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    config = {"token": "xxxx-xxxx-xxxx-xxxx-xxxx"}
    galaxy_token = GalaxyToken()
    galaxy_token._config = config
    galaxy_token.save()


# Generated at 2022-06-12 22:13:33.372918
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken('ced0d2c0-a6cc-4d3a-86b9-fcf35a6e4a6e')
    assert (token.get() == 'ced0d2c0-a6cc-4d3a-86b9-fcf35a6e4a6e')
    token.set('ced0d2c0-a6cc-4d3a-86b9-fcf35a6e4a6e')
    assert (token.headers() == {'Authorization': 'Token ced0d2c0-a6cc-4d3a-86b9-fcf35a6e4a6e'})

# Generated at 2022-06-12 22:13:37.865091
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Initialize with an invalid token
    token = KeycloakToken('invalid_token', 'https://localhost')
    assert token.get() is not None
    assert isinstance(token.get(), str)
    # Initialize with no token
    token = KeycloakToken(None, 'https://localhost')
    assert token.get() is None
    assert isinstance(token.get(), type(None))

# Generated at 2022-06-12 22:13:41.653649
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken("fake_access_token", "fake_auth_url")
    assert token.headers() == {'Authorization': 'Bearer '}



# Generated at 2022-06-12 22:13:53.356037
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.module_utils._text import to_bytes
    import shutil
    home = to_bytes(os.path.expanduser("~"))
    token_file = os.path.join(home, '.ansible', 'galaxy.yml')
    token_file_copy = os.path.join(home, '.ansible', 'galaxy.yml.copy')
    shutil.copy(token_file, token_file_copy)
    token = GalaxyToken()
    token.set('testtoken')
    assert token.get() == 'testtoken'
    assert token.config['token'] == 'testtoken'
    token.save()
    with open(token_file, 'r') as f:
        assert f.read() == "token: testtoken\n"

# Generated at 2022-06-12 22:14:03.109725
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:14:12.568746
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile, os
    tmpfile = tempfile.NamedTemporaryFile()

    token = '1234567890'
    gt = GalaxyToken(token)
    gt.save()

    assert os.path.isfile(tmpfile.name)

    with open(tmpfile.name, 'r') as f:
        assert token == f.read()

    gt.set('0987654321')
    gt.save()

    with open(tmpfile.name, 'r') as f:
        assert '0987654321' == f.read()

    os.unlink(tmpfile.name)

# Generated at 2022-06-12 22:14:22.900832
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import copy
    import sys
    import base64
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    client_id = 'cloud-services'