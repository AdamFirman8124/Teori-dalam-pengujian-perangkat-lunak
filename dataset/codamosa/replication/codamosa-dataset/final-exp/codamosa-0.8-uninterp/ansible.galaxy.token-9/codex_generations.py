

# Generated at 2022-06-12 22:05:06.919929
# Unit test for constructor of class KeycloakToken
def test_KeycloakToken():
    token = KeycloakToken()
    assert token.token_type == 'Bearer'

# Generated at 2022-06-12 22:05:11.720517
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    # Test when the token is not None
    tok = KeycloakToken(access_token='test_token_1')
    assert tok.get() == 'test_token_1'

    # Test when the token is None
    tok2 = KeycloakToken(access_token=None)
    assert tok2.get() is None

# Generated at 2022-06-12 22:05:21.714702
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # create a test case of GalaxyToken
    token_file_origin = C.GALAXY_TOKEN_PATH
    C.GALAXY_TOKEN_PATH = '.ansible_galaxy_token'
    gt = GalaxyToken()
    token = 'test-token'
    gt.set(token)
    # simulate the save operation
    gt.save()
    # restore the global state
    C.GALAXY_TOKEN_PATH = token_file_origin
    # assert the content of token file
    with open('.ansible_galaxy_token', 'r') as f:
        assert f.read() == 'token: test-token\n'
    # clear the temporary token file
    os.remove('.ansible_galaxy_token')

# Generated at 2022-06-12 22:05:34.097761
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:05:39.194075
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken(access_token=None, auth_url="http://auth.example.com")
    assert k.get() == None
    k = KeycloakToken(access_token="123", auth_url="http://auth.example.com")
    assert k.get() == None

# Generated at 2022-06-12 22:05:48.416046
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:05:58.849682
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import filecmp
    try:
        cwd = os.getcwd()
        os.chdir(os.path.dirname(os.path.realpath(__file__)))

        galaxy_token = GalaxyToken()
        galaxy_token.set('the-token')
        galaxy_token.save()

        assert os.path.isfile('/tmp/ansible_galaxy_token')
        assert filecmp.cmp('/tmp/ansible_galaxy_token', './data/ansible_galaxy_token')

    finally:
        os.remove('/tmp/ansible_galaxy_token')
        os.chdir(cwd)



# Generated at 2022-06-12 22:06:11.804516
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Params
    access_token = "test_auth"
    auth_url = 'https://auth.com/'
    validate_certs = True
    client_id = "test_client"

    # Mock Open Url
    class MockUrl(object):
        def read(self):
            json_str = u'{"access_token":"test_response"}'
            return json_str

    open_url_mock = MockUrl()

    def _open_url(url, *args, **kwargs):
        return open_url_mock

    # Mock
    KeycloakToken._open_url = _open_url

    # Get new token
    token = KeycloakToken(access_token, auth_url, validate_certs, client_id)
    token.get()

    # Assert
    assert token._

# Generated at 2022-06-12 22:06:21.639716
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='123456789',
                          auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                          validate_certs=True, client_id='cloud-services')

# Generated at 2022-06-12 22:06:26.779504
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class FakeResponse():
        def read(self):
            return "{\"access_token\":\"12345\"}"

    fake_token = KeycloakToken(access_token="12345", auth_url="http://foo.com", validate_certs=True)
    fake_token.open_url = lambda x: FakeResponse()
    assert fake_token.get() == "12345"

# Generated at 2022-06-12 22:06:34.444243
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(auth_url='https://sso.redhat.com/auth/realms/ansible/protocol/openid-connect/token',
                          access_token='some-token')
    assert token.headers() == {'Authorization': 'Bearer Some-token'}


# Generated at 2022-06-12 22:06:43.961712
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    my_access_token = "ab7e544e-6b66-43be-82f0-c7d26b6c351b"
    my_auth_server_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    my_client_id = "galaxy-cli"
    my_obj = KeycloakToken(access_token=my_access_token, auth_url=my_auth_server_url, client_id=my_client_id)
    my_obj.get()

# Generated at 2022-06-12 22:06:52.454302
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # testing with -vvv
    display.verbosity = 4

    # test with invalid token and no keycloak_client_id in ansible.cfg
    kc_token = KeycloakToken()
    assert kc_token.get() is None

    # test with valid token and no keycloak_client_id in ansible.cfg
    kc_token = KeycloakToken(access_token='test_access_token')
    assert kc_token.get() is None

    # test with valid token and keycloak_client_id in ansible.cfg

    # setup test for get()
    kc_token = KeycloakToken(access_token='test_access_token', auth_url='this_is_a_test_url', validate_certs=True)

# Generated at 2022-06-12 22:06:58.545783
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                          access_token='111111111-2222-3333-4444-555555555555')
    token.get()
    print(token._token)
    print(token.headers())

# Generated at 2022-06-12 22:07:00.675477
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='test')
    expected = {'Authorization': 'Bearer None'}
    assert token.headers() == expected

# Generated at 2022-06-12 22:07:09.234227
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    KEYCLOAK_CLIENT_ID = 'test-client-id'
    KEYCLOAK_TOKEN_TYPE = 'Bearer'
    TOKEN = 'test-token'
    VALIDATE_CERTS = False

    obj = KeycloakToken(access_token=TOKEN,
                        auth_url='https://auth.com',
                        validate_certs=VALIDATE_CERTS,
                        client_id=KEYCLOAK_CLIENT_ID)

    token = obj.get()
    headers = obj.headers()

    assert token == TOKEN
    assert type(headers) is dict
    assert len(headers) == 1
    assert headers.get('Authorization') == '{} {}'.format(KEYCLOAK_TOKEN_TYPE, TOKEN)


# Generated at 2022-06-12 22:07:19.345440
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import os
    import tempfile
    tf = tempfile.NamedTemporaryFile(delete=False)
    dummy = {'access_token': 'asdf'}
    tf.write(to_bytes(json.dumps(dummy), errors='surrogate_or_strict'))
    tf.close()

    token = KeycloakToken(access_token='asdf',
                        auth_url='file://%s' % tf.name,
                        validate_certs=False)

    try:
        assert token.get() == 'asdf'
    finally:
        os.unlink(tf.name)

# Generated at 2022-06-12 22:07:27.705928
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_client_id = 'cloud-services'

# Generated at 2022-06-12 22:07:36.362891
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:47.065784
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Test saving config
    token = "123456"
    test_f = "test_token_save"
    config = "{'token' : '%s', 'server': 'https://localhost'} " % token

    t = GalaxyToken(None)
    t.b_file = to_bytes(test_f, errors='surrogate_or_strict')
    t._config = yaml_load(config)
    t.save()

    assert os.path.isfile(test_f)

    with open(test_f, 'r') as f:
        content = f.read()

    expected = "token: '%s'\nserver: https://localhost\n" % token

    assert content == expected
    os.unlink(test_f)

    # Test saving config with no server

# Generated at 2022-06-12 22:08:04.143820
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:08:14.280208
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    t = KeycloakToken(access_token='cGFzc3dvcmQ=')
    t.auth_url = 'http://sso.redhat.com'
    t.validate_certs = True
    t.client_id = 'cloud-services'

# Generated at 2022-06-12 22:08:21.011296
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kct = KeycloakToken('foo', auth_url='bar')
    kct._token = None
    kct.get()
    assert kct.headers() == {'Authorization': 'Bearer some_token'}
    #
    # This should be mocked
    #
    class Mock_Response(object):
        def __init__(self, body):
            self.body = body
            self.getcode = lambda: 200
        def read(self):
            return self.body
    #
    body = '{"access_token": "some_token", "refresh_token": "some_other_token"}'
    kct._token = None
    kct.get = lambda: Mock_Response(body)
    assert kct.headers() == {'Authorization': 'Bearer some_token'}

# Generated at 2022-06-12 22:08:23.020030
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('testtoken')
    assert token.get() == 'testtoken'


# Generated at 2022-06-12 22:08:31.918598
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloakToken = KeycloakToken()
    keycloakToken.get()

# Generated at 2022-06-12 22:08:40.091074
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test 1 - should fail because of missing access_token
    # token = KeycloakToken(access_token=None, auth_url=None)
    # assert token.get() is None

    # Test 2 - should fail because of missing auth_url
    # token = KeycloakToken(access_token="bogus", auth_url=None)
    # assert token.get() is None

    # Test 3 - should pass with valid access_token and auth_url
    token = KeycloakToken(access_token="bogus", auth_url="http://authhost.com")
    assert token.get() is not None

# Generated at 2022-06-12 22:08:48.748846
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    test_file = to_bytes(C.GALAXY_TOKEN_SAVE_TEST_PATH, errors='surrogate_or_strict')
    try:
      unlink(test_file)
    except:
      pass
    gt.b_file = test_file
    gt.save()
    assert os.path.isfile(test_file)
    assert os.path.getsize(test_file) == 0
    gt.set('foobar')
    gt.save()
    assert os.path.getsize(test_file)
    with open(test_file) as f:
        data = yaml_load(f)
        assert data['token'] == 'foobar'
    unlink(test_file)

# Generated at 2022-06-12 22:09:00.303168
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    tk = GalaxyToken()
    tk.config = {'token': 'my_token'}
    assert tk.get() == 'my_token'
    tk.save()
    tk = GalaxyToken()
    assert tk.get() == 'my_token'
    tk.set('new_token')
    assert tk.get() == 'new_token'
    tk.save()
    tk = GalaxyToken()
    assert tk.get() == 'new_token'
    tk.set(NoTokenSentinel)
    assert tk.get() is None
    tk.save()
    tk = GalaxyToken()
    assert tk.get() is None
    # put back the original token
    tk.set('my_token')
    tk.save()

# Generated at 2022-06-12 22:09:05.105917
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    a = KeycloakToken(access_token="access_token")
    b = a.headers()
    c = {"Authorization": "Bearer access_token"}
    assert b == c


# Generated at 2022-06-12 22:09:18.688388
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kc_token = KeycloakToken(client_id='unit_test',
                             access_token='03f1c9a9-b318-4b51-a82a-7d174e6cef76',
                             auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    token = kc_token.get()

# Generated at 2022-06-12 22:09:45.943189
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='__YOUR_OFFLINE_TOKEN__', auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    token.get()

# Generated at 2022-06-12 22:09:56.003382
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    from ansible.module_utils import six
    from ansible.module_utils.urls import open_url

    original_open_url = open_url

    def test_open_url(*args, **kwargs):
        class Response():
            def __init__(self):
                self.code = 200
                data = {
                    'access_token': 'testtoken',
                    'refresh_token': 'testrefresh',
                    'expires_in': 3600,
                    'token_type': 'Bearer'
                }
                self.read = six.StringIO(json.dumps(data)).read

            def getcode(self):
                return self.code

            def read(self):
                return self.read()

        return Response()

    open_url = test_open_url


# Generated at 2022-06-12 22:10:05.227463
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'

# Generated at 2022-06-12 22:10:14.405077
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():

    # Test with valid KeycloakToken object
    kct = KeycloakToken('refresh_token', 'auth_url', 'validate_certs', 'client_id')
    assert 'Authorization' in kct.headers()
    assert kct.headers()['Authorization'] == 'Bearer None'

    # Test with invalid KeycloakToken object and ensure headers has correct key and data
    kct = KeycloakToken('')
    assert 'Authorization' in kct.headers()
    assert kct.headers()['Authorization'] == 'Bearer None'

# Generated at 2022-06-12 22:10:18.051822
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = 'foo'
    gt = GalaxyToken(token)
    gt.set(token)

    with open(gt.b_file, 'r') as f:
        assert token in f.read()


# Generated at 2022-06-12 22:10:21.367871
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.config['token'] = 'foobar'
    token.save()
    with open(token.b_file) as fd:
        data = fd.read()
    assert data == "token: foobar\n"

# Generated at 2022-06-12 22:10:26.688652
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.six.moves.mock import patch
    from ansible.module_utils.six.moves.urllib.parse import urlencode
    from ansible.module_utils.six.moves.urllib.error import HTTPError

    payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=12345'

    with patch.object(open_url, 'side_effect') as url_mock:
        url_mock.return_value = open(os.path.join(C.TESTS_DIR, 'unit/galaxy/responses/keycloak_token.json'))

# Generated at 2022-06-12 22:10:38.547904
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
    Unit test for the class method get()
    - ok. access_token is valid
    - ok. access_token is invalid (doesn't exist)
    """
    # testing the code path where the token is valid
    class FakeResponse(object):
        def __init__(self, readable, http_code=200, headers=None):
            self.content = readable
            self.code = http_code
            self.headers = headers

        def read(self):
            return self.content

    class FakeOpenUrl(object):
        def __init__(self, reponse):
            self.reponse = reponse

        def __call__(self, url, data=None, validate_certs=True, method='GET', http_agent=None):
            return self.reponse


# Generated at 2022-06-12 22:10:42.498236
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(access_token='xxx')
    assert kt.headers().get('Authorization') == 'Bearer None'



# Generated at 2022-06-12 22:10:44.423719
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    t = GalaxyToken()
    t.config['token'] = 'test'
    t.save()
    assert t.get() == 'test'

# Generated at 2022-06-12 22:10:55.715085
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests_mock
    kt = KeycloakToken('access_token', 'auth_url')

    payload = {
        'access_token': 'abc123',
        'refresh_token': 'dummy',
        'expires_in': '3600'
    }

    with requests_mock.mock() as m:
        m.post('auth_url', text=json.dumps(payload))
        assert kt.get() == 'abc123'

# Generated at 2022-06-12 22:10:57.872581
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='test')
    assert token.get() == 'test'


# Generated at 2022-06-12 22:11:05.523987
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.compat.tests.mock import patch

    with patch('ansible.galaxy.token.open_url') as mock_open:
        mock_open.return_value.read.return_value = '{"access_token": "abc123"}'

        token = KeycloakToken('fake_offline_token', auth_url='http://fake.com/auth/realms/ansible/protocol/openid-connect/token')

        headers = token.headers()

        assert 'Authorization' in headers
        assert headers['Authorization'] == 'Bearer abc123'



# Generated at 2022-06-12 22:11:17.061270
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    from ansible.module_utils.urls import open_url
    from ansible.module_utils.six.moves.urllib.error import HTTPError

    def fake_open_url(*args, **kwargs):
        raise HTTPError('', 500, '', {}, None)

    class FakeResponse(object):
        def __init__(self, code, data):
            self.code = code
            self.data = data

        def read(self):
            return self.data

    class FakeArgs(object):
        pass

    args = FakeArgs()
    args.data = "grant_type=refresh_token&client_id=cloud-services&refresh_token=abc"
    args.method = 'POST'
    args.http_agent = ''


# Generated at 2022-06-12 22:11:19.048317
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.set("test")
    token.save()


# Generated at 2022-06-12 22:11:27.339267
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class MockResponse:
        def __init__(self):
            self.m_read = b'{ "access_token": "something" }'
        def read(self):
            return self.m_read

    # Create an authenticated session to the test server
    token = KeycloakToken(access_token="12345", auth_url="http://localhost:5000/v1/auth/token")

    # Perform a mock call to the server
    token.get()

    # Set the mock response
    token._token = MockResponse()
    # Make sure the response is read
    response = token.get()
    assert response == "something"


# Generated at 2022-06-12 22:11:30.524637
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token1 = KeycloakToken(access_token='AaAa', auth_url='http://jdoe.com/auth', validate_certs=True, client_id=None)
    assert token1.get() == 'AaAa'

# Generated at 2022-06-12 22:11:35.859464
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    b_file = '/tmp/test_galaxy_token_save'
    token = 'test_save'
    GalaxyToken(token).save()
    with open(b_file, 'r') as f:
        config = yaml_load(f)
    # Remove the file
    os.remove(b_file)
    assert config == {'token': token}

# Generated at 2022-06-12 22:11:48.753076
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils import basic

    print("Testing KeycloakToken.get()")
    print("Initializing KeycloakToken")
    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

# Generated at 2022-06-12 22:11:57.970650
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.compat.tests import unittest

    class TestGalaxyToken(unittest.TestCase):
        def setUp(self):
            self.token = GalaxyToken()
            self.token.config = {'token': None}

        def tearDown(self):
            self.token = None

        def test_empty_config(self):
            self.token.config = {}
            self.token.save()
            self.assertTrue(os.path.isfile(self.token.b_file))

        def test_set_token(self):
            self.token.config = {'token': 'test_token'}
            self.token.save()
            with open(self.token.b_file, 'r') as f:
                data = yaml_load(f)

# Generated at 2022-06-12 22:12:22.775324
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(auth_url="https://auth.openshift.io/api/token/aws/api/token/azure",
                          access_token="just a dummy token")
    token_value = token.get()

# Generated at 2022-06-12 22:12:34.146274
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:12:40.129841
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    '''Test for method headers of class KeycloakToken'''

# Generated at 2022-06-12 22:12:43.005694
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token_obj = KeycloakToken('abc')
    assert keycloak_token_obj.get() == None


# Generated at 2022-06-12 22:12:49.600087
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    u = KeycloakToken('test_token', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                      True, 'galaxy')
    assert u.get() == 'test_token'

    u = KeycloakToken('test_token', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                      True, 'galaxy')
    assert u.get().startswith('ey')

    u = KeycloakToken('test_token', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                      True, 'galaxy')
    assert isinstance(u.get(), str)

# Generated at 2022-06-12 22:12:52.396688
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    current_version = '0.0.0'

    token = KeycloakToken.get(current_version)

    assert token.get() is not None


# Generated at 2022-06-12 22:12:58.939757
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = '123'
    mytoken = GalaxyToken(token=token)
    mytoken.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)
    assert mytoken.config == {'token': token}
    # try to read it back
    with open(C.GALAXY_TOKEN_PATH, 'r', encoding='utf-8') as f:
        config = yaml_load(f)
    assert config == {'token': token}



# Generated at 2022-06-12 22:13:08.356424
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Create an instance of KeycloakToken class
    test_token = KeycloakToken("test", "https://www.example.com/auth/realms/test/protocol/openid-connect/token", True, "client_id")

    # Verify that the token is returned correctly (token is None)
    assert test_token.get() is None

    # Set the token
    test_token._token = "test_token"

    # Verify that the token is returned correctly (token is not None)
    assert test_token.get() is not None


# Generated at 2022-06-12 22:13:18.877126
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    #create a token with a test token
    token = GalaxyToken()
    token.set('test-token')
    #Check if the token is set to the desired test value
    assert token.get() == 'test-token'
    #save the token
    token.save()
    #check if the token is saved in the galaxy configuration file
    token = GalaxyToken()
    assert token.get() == 'test-token'
    #remove the test token from the galaxy configuration file
    token.set(None)
    token.save()
    #check if the test token is removed
    token = GalaxyToken()
    assert token.get() == None

# Generated at 2022-06-12 22:13:26.526821
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():

    # create test file
    GALAXY_TOKEN_PATH = 'test_galaxy_token'
    b_file = to_bytes(GALAXY_TOKEN_PATH, errors='surrogate_or_strict')

    if os.path.isfile(b_file):
        os.remove(b_file)

    open(b_file, 'w').close()
    os.chmod(b_file, S_IRUSR | S_IWUSR)  # owner has +rw

    # create test GalaxyToken
    galaxy_token = GalaxyToken(token='test_token')

    # save test GalaxyToken
    galaxy_token.save()

    # check if resulting file is a yaml file
    with open(GALAXY_TOKEN_PATH, 'r') as f:
        result = yaml

# Generated at 2022-06-12 22:13:40.094876
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken(token="1234")
    token.save()

    with open(C.GALAXY_TOKEN_PATH) as f:
        config = yaml_load(f)

    assert config['token'] == "1234"

# Generated at 2022-06-12 22:13:45.411430
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    assert KeycloakToken(access_token='valid.access.token', auth_url='https://hostname/openid-connect/token', validate_certs=True, client_id='validclientid').get() == 'valid_access_token'


# Generated at 2022-06-12 22:13:57.105496
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:14:07.814531
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Arrange
    token_path = 'token.yml'
    token_content = 'token: abcd1234'
    token_content_b64 = 'dG9rZW46IGFiY2QxMjM0'

    # Act
    token = GalaxyToken()
    token._token = to_bytes(token_content)
    token.b_file = to_bytes(token_path, errors='surrogate_or_strict')
    token.save()

    # Assert
    assert os.path.isfile(token_path)
    assert os.stat(token_path).st_mode == 33152

    with open(token_path, 'r') as f:
        token_read = f.read()
        assert token_read == token_content_b64


# Generated at 2022-06-12 22:14:10.761172
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='test_token')
    assert token.headers() == {'Authorization': 'Bearer test_token'}

# Generated at 2022-06-12 22:14:21.256482
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    class FakeRequest(object):
        def __init__(self, resp_body):
            self.resp_body = resp_body

        def read(self):
            return self.resp_body

        def close(self):
            pass

    class FakeUrlOpen(object):
        def __init__(self, val):
            self.resp = val
            self.payload = None

        def __call__(self, url, data=None, **kwargs):
            self.payload = data
            return self.resp

        def get_payload(self):
            return self.payload

    resp = FakeRequest('{"access_token": "foobar"}')
    open_url = FakeUrlOpen(resp)

# Generated at 2022-06-12 22:14:24.865018
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak = KeycloakToken('abcd')
    keycloak.token_type = 'abc'
    assert keycloak.headers() == {'Authorization': 'abc ' + 'abcd'}

# Generated at 2022-06-12 22:14:27.998224
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('abcdefghijklmnopqrstuvwxwz1234567890')
    assert(token.get()=='abcdefghijklmnopqrstuvwxwz1234567890')

# Generated at 2022-06-12 22:14:30.938967
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken('a_token', 'https://keycloak.com/auth/realms/rh-integ-auth/protocol/openid-connect/token')
    assert kt.headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:14:33.348906
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken("test")
    assert token.headers() == {'Authorization': 'Bearer None'}
    token.access_token = 'test'
    token._token = 'test'
    assert token.headers() == {'Authorization': 'Bearer test'}


# Generated at 2022-06-12 22:14:55.750576
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Testing that function returns a dict containing 'Authorization'
    token = KeycloakToken('123-abc')
    headers = token.headers()
    assert 'Authorization' in headers
    # Testing that the value of 'Authorization' is 'Bearer <token>'
    assert headers['Authorization'][:6] == 'Bearer'
    # Testing that the value of 'Authorization' is not empty after requiring a token
    token.get()
    assert headers['Authorization'][7:] != ''


# Generated at 2022-06-12 22:15:01.747552
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken(access_token='faketoken', auth_url='https://auth.url', validate_certs=True, client_id='client_id')
