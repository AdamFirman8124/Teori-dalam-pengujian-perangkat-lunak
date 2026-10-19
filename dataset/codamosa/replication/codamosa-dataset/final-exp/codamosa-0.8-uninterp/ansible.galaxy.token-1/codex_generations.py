

# Generated at 2022-06-12 22:05:16.194233
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test different success returns
    access_token = {'access_token': 'abc123'}
    token_key = 'access_token'
    token_base = 'abc'
    token_value = access_token[token_key]
    refresh_token = 'def456'
    auth_url = 'http://some.url'
    payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=%s' % refresh_token

# Generated at 2022-06-12 22:05:20.271531
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_dict = {'access_token': '123', 'auth_url': 'www.example.com', 'client_id': 'someClientId'}
    token = KeycloakToken(**test_dict)
    assert token.get()=='123'

# Generated at 2022-06-12 22:05:22.091792
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('fake-token', 'http://fake.url')
    assert token.get() == "Bearer fake-token"



# Generated at 2022-06-12 22:05:28.620584
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    f_path = C.GALAXY_TOKEN_PATH
    os.chmod(C.GALAXY_TOKEN_PATH, 0o000)
    try:
        token = GalaxyToken()
        token.save()
        assert os.stat(f_path).st_mode == S_IRUSR | S_IWUSR
    finally:
        os.chmod(C.GALAXY_TOKEN_PATH, 0o666)

# Generated at 2022-06-12 22:05:29.285460
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    pass

# Generated at 2022-06-12 22:05:40.819556
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class FakeResponse():
        @staticmethod
        def read():
            return '{"access_token":"12345","expires_in":43199,"refresh_expires_in":0,"refresh_token":"54321","token_type":"bearer","not-before-policy":0,"session_state":"12345","scope":"create_group delete_group manage_group user"}'

    open_url = lambda url: FakeResponse()

    token = KeycloakToken('54321', auth_url='https://sso.redhat.com/auth/realms/ansible/protocol/openid-connect/token', validate_certs=True)

    assert token.get() == '12345'



# Generated at 2022-06-12 22:05:44.563683
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc = KeycloakToken('random_token', 'http://test', False, 'test_client')
    expected_headers = {'Authorization': 'Bearer random_token'}
    assert(kc.headers() == expected_headers)


# Generated at 2022-06-12 22:05:47.729680
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Setup
    kct = KeycloakToken(access_token="test_token")
    kct._token = "test_token"
    # Execute
    token = kct.get()
    # Verify
    assert token == "test_token"



# Generated at 2022-06-12 22:05:59.617475
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:06:12.324886
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import shutil
    import os

    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, "test_ansible_token")
    try:
        g_t = GalaxyToken()
        g_t.b_file = to_bytes(tmpfile)
        g_t.set("my_token")
        assert os.path.exists(tmpfile)
        assert os.path.isfile(tmpfile)
        expected = """token: my_token"""
        with open(tmpfile, "r") as f:
            actual = f.read()
        assert expected == actual
    finally:
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)

# Generated at 2022-06-12 22:06:18.287728
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    #Todo: implement
    pass

# Generated at 2022-06-12 22:06:20.201626
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken()
    headers = token.headers()
    assert 'Authorization' in headers
    assert 'Bearer' in headers['Authorization']

# Generated at 2022-06-12 22:06:22.732436
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken(access_token='123123123', auth_url='example.com')
    kct.get()



# Generated at 2022-06-12 22:06:32.835208
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os.path
    import shutil
    from tempfile import mkdtemp
    from ansible.module_utils.six import PY3

    # Create a temporary ansible.cfg file with galaxy_token_path set
    tmpdir = mkdtemp()
    config_path = os.path.join(tmpdir, 'ansible.cfg')
    with open(config_path, 'w') as f:
        f.write('[defaults]\n')
        f.write('galaxy_token_path = {}\n'.format(tmpdir))
    os.environ['ANSIBLE_CONFIG'] = config_path

    # Instantiate a token object and set a token
    token_value = 'test_value'
    token = GalaxyToken(token_value)

    # Make sure the token file doesn't exist so save will create it

# Generated at 2022-06-12 22:06:45.823045
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:53.324655
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create a dummy token file
    test_token_file = '/tmp/test_token.yml'
    f = open(test_token_file, 'w')
    f.write("""
    token: 11111-22222-33333
    """)
    f.close()
    # Now read the token file with GalaxyToken
    g = GalaxyToken()
    g.b_file = to_bytes('/tmp/test_token.yml')
    c = g.config
    # Make a change to the token file
    g.set('44444-55555-66666')
    g.save()

    # Read it back
    f = open(test_token_file)
    fc = f.read()
    f.close()

    # Verify the file was changed

# Generated at 2022-06-12 22:06:57.369085
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    expected = {
        'Authorization': 'Bearer foobar'
    }
    token = KeycloakToken(access_token='foobar')
    headers = token.headers()
    assert headers == expected



# Generated at 2022-06-12 22:06:59.916591
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():

    t = KeycloakToken(access_token='asdf', auth_url='asdf')

    assert t.headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:07:01.894504
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # setup a KeycloakToken object
    kct = KeycloakToken('offline-token-value')

    headers = kct.headers()

    assert headers['Authorization'].startswith('Bearer ')



# Generated at 2022-06-12 22:07:04.638585
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloakToken = KeycloakToken(access_token="keycloakaccess", auth_url="keycloakurl")
    assert keycloakToken.get() == "keycloakaccess"


# Generated at 2022-06-12 22:07:20.617669
# Unit test for method save of class GalaxyToken

# Generated at 2022-06-12 22:07:25.569753
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="eyJhbGciOiJSUzI1NiIsI",
                          auth_url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token")
    expected = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsI'}
    assert token.headers() == expected



# Generated at 2022-06-12 22:07:28.569604
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Test no token
    token = KeycloakToken()
    assert token.headers() == {'Authorization': 'Bearer None'}

    # Test with a token
    token = KeycloakToken(access_token='some_random_string')
    assert token.headers() == {'Authorization': 'Bearer some_random_string'}

# Generated at 2022-06-12 22:07:36.897062
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:38.387836
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kc_token = KeycloakToken(access_token='dupya', auth_url='http://keycloak/auth', validate_certs=False)
    print(kc_token.get())


# Generated at 2022-06-12 22:07:38.948428
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    pass

# Generated at 2022-06-12 22:07:41.722460
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('')
    token.get = lambda: 'my_random_access_token'
    assert(token.headers() == {'Authorization': 'Bearer my_random_access_token'})

# Generated at 2022-06-12 22:07:51.300728
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    kct = KeycloakToken(
                access_token='e7bd337c-6083-459f-9530-b0d23b70c1b7',
                auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                validate_certs=True)

    token = kct.get()

# Generated at 2022-06-12 22:08:00.222931
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    (tempfd, temp_file) = tempfile.mkstemp()
    os.close(tempfd)
    os.unlink(temp_file)
    config = {'token': 'fake'}
    token = GalaxyToken(token=None)
    token.b_file = to_bytes(temp_file, errors='strict')
    token._config = config
    token.save()
    with open(token.b_file, 'r') as f:
        saved_config = yaml_load(f)
    os.unlink(temp_file)
    assert saved_config == config

# Generated at 2022-06-12 22:08:01.009844
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    pass

# Generated at 2022-06-12 22:08:12.761726
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='<ACCESS_TOKEN>',
                          auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                          client_id='cloud-services')
    assert token.get() == '<ACCESS_TOKEN>'

# Generated at 2022-06-12 22:08:19.808930
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    import responses
    import unittest

    def auth_url_callback(request):
        return(200, '{"access_token":"this-is-a-token"}')

    class KeycloakTokenTest(unittest.TestCase):

        @responses.activate
        def test_KeycloakToken_get(self):
            responses.add_callback(responses.POST, 'https://auth.url', callback=auth_url_callback)
            kt = KeycloakToken(access_token='offline-token', auth_url='https://auth.url')
            self.assertEqual(kt.get(), 'this-is-a-token')

    t = KeycloakTokenTest()
    t.test_KeycloakToken_get()



# Generated at 2022-06-12 22:08:22.227939
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='foo', auth_url='http://dummy.url')
    assert token.get() == 'foo'


# Generated at 2022-06-12 22:08:25.513767
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    key = KeycloakToken(access_token="abcdefg", auth_url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token")
    assert key.get() == "abcdefg"


# Generated at 2022-06-12 22:08:32.048387
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Create a dummy access_token
    test_access_token = '7b70ca49-401e-4f19-a77b-a2622548ab0c'
    # Create a dummy auth_url
    test_auth_url = 'https://ssodev.dev.rhcloud.com/auth/realms/ansible/protocol/openid-connect/token'
    token = KeycloakToken(access_token=test_access_token, auth_url=test_auth_url)
    token.get()
    assert token.get()



# Generated at 2022-06-12 22:08:42.198277
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.galaxy.token import GalaxyToken
    import os
    import tempfile

    config = {'token': 'foo'}

    with tempfile.NamedTemporaryFile(mode='w+') as f:
        b_file = to_bytes(f.name, errors='surrogate_or_strict')
        token = GalaxyToken(token='foo')

        # ensure the file doesn't exist before
        assert(not os.path.isfile(b_file))

        # save the config to the file
        token.save()
        assert(os.path.isfile(b_file))

        # verify the file content
        with open(b_file, 'r') as f:
            assert(f.read() == 'token: foo\n')

# Generated at 2022-06-12 22:08:50.734028
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from tempfile import NamedTemporaryFile
    from os.path import basename
    import ansible.constants as C

    class Token(GalaxyToken):
        def __init__(self, token=None):
            # create a tempfile to test with
            super(Token, self).__init__(token=token)
            tempfile = NamedTemporaryFile(delete=False)
            tempfile.close()
            self.b_file = tempfile.name

    tok = Token('faketoken')
    tok.save()
    assert os.path.isfile(tok.b_file), 'Token not saved'
    with open(tok.b_file, 'r') as f:
        assert f.read() == 'token: faketoken', 'Token not saved'

# Generated at 2022-06-12 22:09:01.197533
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    token_path = os.path.join(temp_dir.name, 'test_token.yml')
    test_token = {'token': 'test_set'}
    with open(token_path, 'w') as f:
        yaml_dump(test_token, f, default_flow_style=False)
    token = GalaxyToken(token=test_token['token'])
    token.b_file = token_path
    token.save()
    # assert if the file has changed
    with open(token_path, 'r') as f:
        new_token = yaml_load(f)
    assert new_token['token'] == 'test_set'



# Generated at 2022-06-12 22:09:14.768448
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    import unittest
    import urllib3
    from ansible.module_utils.six.moves import mock
    import ansible.module_utils.urls as urls

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.access_token = 'some_token'
            self.auth_url = 'https://sso.example.com/auth/realms/some_realm/protocol/openid-connect/token'
            self.validate_certs = True
            self.client_id = 'client_id'


# Generated at 2022-06-12 22:09:26.571188
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    json_str='''
    {
      "access_token":"abcde",
      "expires_in":300,
      "refresh_expires_in":1800,
      "refresh_token":"fghij",
      "token_type":"Bearer",
      "not-before-policy":0,
      "session_state":"abcd-efgh-ijkl",
      "scope":"email"
    }
    '''
    def mocked_open_url(url, data, validate_certs, method, http_agent):
        resp = type('Mock', (object,), {})
        resp.read = lambda: json_str
        return resp

    # Overwrite open_url
    open_url_backup = open_url.__globals__['open_url']
    open_url.__gl

# Generated at 2022-06-12 22:09:49.751264
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class FakeResponse:
        def __init__(self, token):
            self.token = token

        def read(self):
            return self.token

    fake_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
    fake_data = {'access_token': fake_token}
    

# Generated at 2022-06-12 22:09:58.451125
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjRzlmYlRYTmUzTjhOU'
    access_token += '0ZGaGg2Qnk1Mkg4S0hYMlF4WGpzNVZ4a1ZMIn0.eyJqdGkiOiI5NGMyYjBkNS1lMDRhLTRkZD'
    access_token += 'ItODY3My03ZDQ2M2Q1MjVhNDMiLCJleHAiOjE1MDY5ODk0OTUsIm5iZiI6MCwiaWF0Ij'

# Generated at 2022-06-12 22:10:01.676993
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(auth_url='http://auth.net/auth', access_token='abc-123', client_id='abc')

    assert token.headers() == {
        'Authorization': 'Bearer null'
    }


# Generated at 2022-06-12 22:10:04.979831
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    api_url = 'https://auth.testing.com'
    access_token = 'access_token'
    token = KeycloakToken(access_token=access_token, auth_url='https://auth.testing.com')
    assert access_token == token.get()

# Generated at 2022-06-12 22:10:17.198844
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token_path = "/tmp/ansible_galaxy_token"

    try:
        open(test_token_path, 'w').close()
        os.chmod(test_token_path, S_IRUSR | S_IWUSR)  # owner has +rw

        tok = GalaxyToken(None)
        tok.b_file = test_token_path

        tok.set("test of a token")

        with open(test_token_path) as f:
            assert f.readlines()[0] == 'token: test of a token\n'
        assert tok.get() == "test of a token"

        os.remove(test_token_path)
    except:
        raise


# Generated at 2022-06-12 22:10:20.607434
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Arrange
    gt = GalaxyToken()
    my_dict = {'token': 'a_token'}

    # Act
    gt.set('a_token')

    # Assert
    assert gt.config == my_dict

# Generated at 2022-06-12 22:10:28.283316
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = "testtoken"
    instance = GalaxyToken(token)

    def mock_open(file, mode):
        assert file == C.GALAXY_TOKEN_PATH
        assert mode == 'w'
        return file

    m_open = 'ansible.galaxy.token.open'
    m_dump = 'ansible.module_utils.common.yaml.yaml_dump'

    with mock.patch(m_dump) as m_yaml_dump:
        with mock.patch(m_open, mock_open) as m_mock_open:
            instance.save()
            m_yaml_dump.assert_called_once_with({'token': token}, m_mock_open.return_value, default_flow_style=False)
            m_mock_open.assert_called_once

# Generated at 2022-06-12 22:10:33.877884
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token._config = {'token': 'test'}
    token.save()
    with open(token.b_file, 'r') as f:
        config = yaml_load(f)
    os.remove(token.b_file)
    assert config == token._config

# Generated at 2022-06-12 22:10:37.619093
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test = KeycloakToken('offline_token', 'auth_url')
    test._token = 'access_token'
    assert test.headers() == {'Authorization': 'Bearer access_token'}


# Generated at 2022-06-12 22:10:47.385384
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # 1.
    # |- Create an object of KeycloakToken
    # |- Verify the token is 'None'
    # |- Call get() to get the token
    # |- Compare the token with the response of the post call
    token = KeycloakToken('test_token', 'some_auth_url', True, 'client_id')
    assert token._token is None
    token._form_payload = lambda: 'test_payload'
    token.get()
    should_be_none = to_text(json.loads(to_text(token._response.read(), errors='surrogate_or_strict')).get('access_token'))
    assert token._token == should_be_none
    # 2.
    # |- Create an object of KeycloakToken
    # |- Set _token to '

# Generated at 2022-06-12 22:11:31.498590
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_obj = KeycloakToken('foo')
    assert auth_obj.headers() == {'Authorization': 'Bearer foo'}

# Generated at 2022-06-12 22:11:35.436122
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(
        access_token='1234567890',
        auth_url='http://localhost:8080/auth/realms/master/protocol/openid-connect/token'
    )

    assert token.get() == '1234567890'

# Generated at 2022-06-12 22:11:43.546277
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    class MockKeycloakToken:
        def get(self):
            return "MockKeycloakToken_get_return"

    mock_kc = MockKeycloakToken()
    kc = KeycloakToken()
    kc._token = mock_kc.get()
    assert kc.headers() == {'Authorization': 'Bearer MockKeycloakToken_get_return'}

# Generated at 2022-06-12 22:11:50.054221
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    """test and verify KeycloakToken.headers returns dict of auth headers and format"""
    kc = KeycloakToken('refresh_token')
    h = kc.headers()
    assert 'Authorization' in h
    assert h['Authorization'].startswith('Bearer ')


# Generated at 2022-06-12 22:11:59.245807
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:12:08.958373
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:12:16.316333
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    ''' Unit test for method get of class KeycloakToken '''

    ktoken = KeycloakToken(access_token='foo', auth_url='http://localhost:3000')
    assert ktoken.get() == 'foo'

    ktoken._token = 'foo'
    assert ktoken.get() == 'foo'

    ktoken.access_token = 'bar'
    assert ktoken.get() == 'bar'


# Generated at 2022-06-12 22:12:20.065622
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken(access_token='foo', auth_url='bar')
    assert kct.get() is None
    kct._token = 'bar'
    assert kct.get() == 'bar'


# Generated at 2022-06-12 22:12:22.565653
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="abc1234")
    token.get()
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer abc1234'


# Generated at 2022-06-12 22:12:33.983438
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class Response:
        def __init__(self, response_content):
            self.response_content = response_content

        def read(self):
            return self.response_content

    response_token_valid_mode = '{"access_token": "my_token_valid_mode", "expires_in": 1800, "refresh_token": "my_refresh_token", "token_type": "bearer"}'
    response_token_invalid_mode = '{"access_token": "my_token_invalid_mode", "expires_in": 1800, "refresh_token": "my_refresh_token", "token_type": "bearer_invalid_token_type"}'

    response_valid_mode = Response(response_token_valid_mode)

# Generated at 2022-06-12 22:13:23.853277
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    try:
        # Create temp file
        temp_fd, temp_file = tempfile.mkstemp(prefix='ansible_galaxy_token_test_')
        os.close(temp_fd)

        # Create token file
        g = GalaxyToken()
        g.b_file = to_bytes(temp_file, errors='surrogate_or_strict')
        g.set('foo')

        with open(temp_file, 'r') as f:
            config = yaml_load(f)

        assert config['token'] == 'foo'

    finally:
        # Cleanup
        try:
            os.remove(temp_file)
        except:
            pass

# Generated at 2022-06-12 22:13:25.733080
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token = KeycloakToken("pwd")
    assert keycloak_token.get() == None

# Generated at 2022-06-12 22:13:31.565326
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Given the KeycloakToken class
    # When I create a KeycloakToken instance
    kt = KeycloakToken(access_token='foo', auth_url='http://example.com')
    # And I set the instance state
    kt._token = 'bar'
    # Then I expect that token to be returned
    assert kt.get() == 'bar'


# Generated at 2022-06-12 22:13:34.439267
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='test_token', auth_url='test_auth_url')
    assert token.get() is not None
    assert token.get() == 'test_token'



# Generated at 2022-06-12 22:13:41.494954
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'access_token'
    auth_url = 'auth_url'
    client_id = 'client_id'
    keycloak_token = KeycloakToken(access_token, auth_url, client_id=client_id)

    payload = "grant_type=refresh_token&client_id=%s&refresh_token=%s" % (client_id, access_token)

    def mock_open_url(url, data=None, validate_certs=False, method='GET', http_agent='Ansible-Galaxy'):
        """ We try to mock open_url to send the payload we want with the authentication url """
        if url == auth_url and data == payload:
            return json.dumps({'access_token': 'access_token_mock'})

    # We

# Generated at 2022-06-12 22:13:53.224675
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    import requests
    from requests_mock.contrib import fixture

    from ansible.galaxy.token import KeycloakToken

    auth_url = 'http://example.com/auth'
    access_token = 'foobar'
    client_id = 'client-id'

    auth_response = {
        'access_token': 'new-access-token',
    }

    # Mock the mock_session.get request
    def fake_auth_token(url, method='GET', json_body=None, **kwargs):
        assert url == auth_url
        assert method == 'POST'
        assert json_body['grant_type'] == 'refresh_token'
        assert json_body['client_id'] == client_id

        return auth_response

    mocker = fixture()

# Generated at 2022-06-12 22:13:57.101829
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    assert KeycloakToken('test_access_token', 'test_auth_url').headers() == {'Authorization': 'Bearer test_access_token'}


# Generated at 2022-06-12 22:14:00.520956
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # GIVEN
    token = KeycloakToken(access_token='yyy', auth_url='http://example.com/foo')

    # WHEN
    headers = token.headers()

    # THEN
    assert headers == {'Authorization': 'Bearer None'}



# Generated at 2022-06-12 22:14:12.465530
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    class KeycloakToken(object):
        token_type = 'Bearer'
        def __init__(self, access_token=None, auth_url=None, validate_certs=True, client_id=None):
            self.access_token = access_token
            self.auth_url = auth_url
            self._token = None
            self.validate_certs = validate_certs
            self.client_id = client_id
            if self.client_id is None:
                self.client_id = 'cloud-services'

        def _form_payload(self):
            return 'grant_type=refresh_token&client_id=%s&refresh_token=%s' % (self.client_id,
                                                                           self.access_token)


# Generated at 2022-06-12 22:14:22.806196
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import requests_mock
    from ansible.module_utils.common.collections import ImmutableDict

    with open('fixtures/authserver_resp.json') as f:
        resp = json.loads(f.read())

    with requests_mock.Mocker() as mock:
        mock.post(base_url, json=resp)

        offline_ticket = 'fd0c9d3d-3b07-4a90-b37e-6e2d6eb96cba'
        auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
        keycloak_tk = KeycloakToken(offline_ticket, auth_url)
        token = keycloak_tk.get()
        assert token