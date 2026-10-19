

# Generated at 2022-06-12 22:05:11.530576
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.set('asdf')

    # check if the file exists
    assert os.path.isfile(token.b_file)

    # check if the content is correct
    with open(token.b_file, 'r') as f:
        config = yaml_load(f)

    assert config == {'token': 'asdf'}

    # cleanup by deleting the file
    os.remove(token.b_file)


# Generated at 2022-06-12 22:05:16.149869
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                          access_token=os.getenv('OFFLINE_TOKEN'),
                          validate_certs=True)
    assert token.get() is not None


# Generated at 2022-06-12 22:05:25.270497
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    #mock the open_url method
    KeycloakToken._old_open_url = KeycloakToken.open_url
    KeycloakToken.open_url = mock_open_url

    #Validate the get method for the keycloak token
    #Validate with valid offline access token

# Generated at 2022-06-12 22:05:38.066942
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:05:44.911164
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    access_token = '<offline_access_token>'
    kt = KeycloakToken(access_token, auth_url)

    kt_token = kt.get()
    print('got token: %s' % kt_token)

if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:05:57.412982
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    expected_token = "zc5B5x5F5xQYPh87AfIxsA"

    # Client id test null (should use the default)
    token = KeycloakToken("9Y6UfT3Tbw6J1c6UfT3Tbw6J1c6UfT3Tbw6J1c6UfT3Tbw6J1c6UfT3Tbw6J1c6UfT3Tbw == ",
                      "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token",
                      client_id=None)
    assert token.get() == expected_token

    # Client id test empty (should use the default)

# Generated at 2022-06-12 22:05:59.491423
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    result = KeycloakToken().headers()
    assert len(result) == 1
    assert 'Authorization' in result


# Generated at 2022-06-12 22:06:04.015417
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    t = GalaxyToken()
    t.config = {'token': '1234'}
    t.save()
    t = GalaxyToken()
    assert t.config['token'] == '1234'

# Generated at 2022-06-12 22:06:06.092419
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('test_value')
    assert token.get() == 'test_value'

# Generated at 2022-06-12 22:06:15.398646
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # write
    token_file = '/tmp/galaxy_token'

    gt = GalaxyToken(token=None)
    gt.b_file = token_file
    gt.set('THIS_IS_A_TEST_TOKEN')

    assert os.path.isfile(token_file)

    # read
    gt = GalaxyToken(token=None)
    gt.b_file = token_file
    config = gt.config

    assert config['token'] == 'THIS_IS_A_TEST_TOKEN'

    # cleanup
    os.remove(token_file)

# Generated at 2022-06-12 22:06:26.829636
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # test that file is created
    galaxy_token = GalaxyToken(token='1234')
    galaxy_token.save()

    file_exists = os.path.isfile(C.GALAXY_TOKEN_PATH)
    assert file_exists

    # clean up
    os.remove(C.GALAXY_TOKEN_PATH)



# Generated at 2022-06-12 22:06:36.035872
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest.mock
    with open('tests/unit/module_utils/galaxy/data/auth_response.json') as f:
        auth_response = f.read()
        mock_resp = unittest.mock.Mock()
        mock_resp.read.return_value = auth_response
    with unittest.mock.patch('ansible.module_utils.urls.open_url', return_value=mock_resp) as mock_open_url:
        token = KeycloakToken(access_token='abc123', auth_url='http://some_auth_url')

# Generated at 2022-06-12 22:06:43.802538
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import os
    token_path = tempfile.NamedTemporaryFile().name
    galaxy_token = GalaxyToken()
    galaxy_token.b_file = token_path
    galaxy_token.config = {'token': '12345'}
    galaxy_token.save()
    assert os.path.isfile(token_path)
    assert os.path.getsize(token_path) > 0



# Generated at 2022-06-12 22:06:50.045157
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_auth_url = 'https://gssodemo.test.redhat.com/auth/realms/demorealm/protocol/openid-connect/token'
    test_user = 'foo'
    test_token = 'mytoken'
    test_keycloak_token = KeycloakToken(test_token, test_auth_url, False)
    headers = test_keycloak_token.headers()
    assert "Authorization" in headers
    assert headers["Authorization"] == 'Bearer {}'.format(test_token)

# Generated at 2022-06-12 22:06:56.006996
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Setup test variables
    client_id = "foo"
    access_token = "bar"
    auth_url = "http://auth.url"
    validate_certs = True

    # Test call
    kct = KeycloakToken(access_token, auth_url, validate_certs, client_id)
    kct.get()

# Generated at 2022-06-12 22:07:05.679876
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.config.manager import ConfigManager
    from ansible.module_utils.six import StringIO
    from ansible.parsing.yaml.objects import AnsibleUnicode

    config_manager = ConfigManager()
    config = config_manager.data

    token_type = 'Token'
    fd, path = tempfile.mkstemp()
    b_path = to_bytes(path, errors='surrogate_or_strict')
    config.settings['GALAXY_TOKEN_PATH'] = b_path

    display = Display()
    ref_sep = '/' if os.sep != '/' else '\\'
    display.verbosity = 5
    display.columns = 80


# Generated at 2022-06-12 22:07:18.316046
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import ansible.config.base
    import ansible.constants as C
    import shutil
    import tempfile
    import yaml
    from ansible.galaxy.token import GalaxyToken

    # Setup a temp directory
    temp_dir = tempfile.mkdtemp()

    # Create temp file to be a fake ansible.cfg
    b_fake_configfile = to_bytes(os.path.join(temp_dir, "ansible.cfg"))
    b_token_dir = to_bytes(temp_dir)

    with open(b_fake_configfile, 'w') as f:
        f.write("[defaults]\n")
        f.write("galaxy_token_path = " + to_text(os.path.join(b_token_dir, "fake_token_file")) + "\n")



# Generated at 2022-06-12 22:07:22.719941
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Given
    access_token = 'b9c44acb-f681-4f5c-b5a5-2b5f51f4c7d4'
    url = 'http://keycloak.example.com/auth/realms/redhat-cloud-services/protocol/openid-connect/token'
    client_id = 'cloud-services'

    # When
    instance = KeycloakToken(access_token, url, client_id)

    # Then

# Generated at 2022-06-12 22:07:33.593851
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import ansible.module_utils.six.moves.http_client as httplib

# Generated at 2022-06-12 22:07:39.411199
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class FakeResponse():
        def __init__(self, text):
            self.text = text
        def read(self):
            return self.text

    # Test 1
    # - access_token: invalid
    # - auth_url: invalid
    # - validate_certs: True
    # - client_id: None
    # Test 1 Expect
    # 1. KeyError
    test1_access_token = 'invalid_access_token_test1'
    test1_auth_url = 'invalid_auth_url_test1'
    test1_validate_certs = True
    test1_client_id = None

# Generated at 2022-06-12 22:07:46.264209
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('token', 'http://auth.url', client_id='ansible')
    headers = token.headers()
    assert headers.get('Authorization') == 'Bearer %s' % token.get()

# Generated at 2022-06-12 22:07:48.175229
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    t = KeycloakToken(access_token='abc')
    assert t.headers()['Authorization'] == 'Bearer None'


# Generated at 2022-06-12 22:07:51.937139
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken('1234', 'http://my.url/auth/realms/redhat-external/protocol/openid-connect/token')
    k.get()

# Generated at 2022-06-12 22:07:57.103919
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'OFFline_T0k3n'
    url = 'http://sso.redhat.com/token'
    KeycloakToken(access_token=access_token, auth_url=url).get()
    assert('sso.redhat.com' in user_agent())

# Generated at 2022-06-12 22:08:01.269875
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    class DummyDisplay(object):
        verbosity = 2
        display = Display()
        
    display = DummyDisplay()
    token = GalaxyToken()
    token.set('token')
    token.save()
    display.display.clear_verbosity_cache()

# Generated at 2022-06-12 22:08:11.906771
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:08:15.999203
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    class MockKeycloakToken(KeycloakToken):
        def get(self):
            return self.access_token

    token = MockKeycloakToken('testtoken')
    assert token.headers()['Authorization'] == 'Bearer testtoken'


# Generated at 2022-06-12 22:08:23.874068
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    config_file = "./test_config.yaml"
    test_token = "test_token"

    try:
        token = GalaxyToken(None)

        # Set config path and token
        token.b_file = config_file
        token._token = test_token
        token.save()

        # Read back in and compare config
        with open(config_file, 'r') as f:
            test_config = yaml_load(f)

        if test_config['token'] == test_token:
            # Passed
            return True

    finally:
        if os.path.exists(config_file):
            os.remove(config_file)


# Generated at 2022-06-12 22:08:26.637852
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken(access_token='refresh_token', auth_url=None, validate_certs=True)
    assert k.get() == 'access_token'

# Generated at 2022-06-12 22:08:37.398610
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    def test_0():
        kct = KeycloakToken(access_token='my token', auth_url='https://auth.url')
        assert kct._form_payload() == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=my token'
        assert kct.get() == None
    test_0()

    def test_1():
        kct = KeycloakToken(access_token='my token', auth_url=None)
        assert kct._form_payload() == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=my token'
        assert kct.get() == None
    test_1()


# Generated at 2022-06-12 22:08:43.698031
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    try:
        token = GalaxyToken()
        token.set('this is a test')
        assert token.get() == 'this is a test'
    finally:
        # ensure we cleanup after ourselves
        os.remove(C.GALAXY_TOKEN_PATH)


# Generated at 2022-06-12 22:08:47.356000
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
    Make sure that the headers are properly formatted.
    """
    token = KeycloakToken(access_token='myofflinetoken', auth_url='http://127.0.0.1/auth')
    headers = token.headers()
    assert headers == {'Authorization': 'Bearer '}

# Generated at 2022-06-12 22:08:55.838546
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.config.manager import ConfigManager
    from ansible.module_utils._text import to_bytes
    config = ConfigManager()
    config.set_config_data({'galaxy_token': 'foo', 'serverlist': {'test_server': ['http://localhost','http://localhost:8080']}})
    token = GalaxyToken()
    token.save()
    assert os.path.exists(to_bytes(config.galaxy_token_path))
    test_token = GalaxyToken()
    assert test_token.get() == 'foo'

# Generated at 2022-06-12 22:08:58.668174
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token = KeycloakToken("dummy_token", "https://auth.example.org/auth/realms/test/protocol/openid-connect/token", validate_certs=True, client_id="dummy_client_id")

    assert keycloak_token.get() == 'dummy_token'


# Generated at 2022-06-12 22:09:03.787428
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Testcase 1: Negative case. Create GalaxyToken object with a filepath
    # which does not exist. When save method is called, it should create
    # the file and write the token data.
    try:
        os.remove(C.GALAXY_TOKEN_PATH)
    except OSError:
        pass

    galaxy_token_obj = GalaxyToken(token="Galaxy_Token")
    galaxy_token_obj.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)

    # Testcase 2: Positive case. Create GalaxyToken object with a filepath
    # which exists. When save method is called, it should overwrite the
    # existing data.
    galaxy_token_obj = GalaxyToken(token="Galaxy_Token")
    galaxy_token_obj.save()

# Generated at 2022-06-12 22:09:14.820794
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import yaml

    token_file_path = '/tmp/galaxy_token'
    galaxy_token = GalaxyToken()
    galaxy_token.set('test_token')
    galaxy_token.save()

    with open(token_file_path, "r") as stream:
        data = yaml.safe_load(stream)
        if not data:
            raise AssertionError("GalaxyToken save() function test failed. No token inside token file.")
        elif data['token'] != 'test_token':
            raise AssertionError("GalaxyToken save() function test failed. Wrong token inside token file.")
    os.remove(token_file_path)

# Generated at 2022-06-12 22:09:18.953848
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    galaxyToken = GalaxyToken()
    galaxyToken.save()
    assert os.path.isfile(galaxyToken.b_file) is True


# Generated at 2022-06-12 22:09:20.980120
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    assert KeycloakToken(access_token="123").headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:09:24.108570
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test case 1, where token is None, should return None
    auth_token = KeycloakToken()
    assert auth_token.get() is None, "Fail to return None when token is None"


# Generated at 2022-06-12 22:09:25.807932
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken("gibberish")
    assert token.get() is None


# Generated at 2022-06-12 22:09:32.679579
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    assert KeycloakToken(access_token='abcdefg').get() == 'abcdefg'

# Generated at 2022-06-12 22:09:40.541887
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    test_token = 'this_is_my_test_token'
    tmp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    galaxy_token = GalaxyToken(token=test_token)
    galaxy_token.save()

    with open(tmp_file.name, 'r') as tmp:
        token_str = tmp.read()
    os.remove(tmp_file.name)

    assert token_str == 'token: this_is_my_test_token\n'

# Generated at 2022-06-12 22:09:44.567721
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='HELLO', auth_url='http://127.0.0.1/auth/realms/master/protocol/openid-connect/token')
    token.get()



# Generated at 2022-06-12 22:09:47.518113
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('test')
    assert token.headers() == {'Authorization': 'Bearer test'}


# Generated at 2022-06-12 22:09:49.269314
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    pass


# Generated at 2022-06-12 22:09:51.874086
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(auth_url='http://foo.com/token', access_token='xyz')
    assert token.headers() == {'Authorization': 'Bearer xyz'}


# Generated at 2022-06-12 22:10:00.022766
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    url = 'https://sso.redhat.com/auth/realms/services/protocol/openid-connect/token'

# Generated at 2022-06-12 22:10:04.117039
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    args = dict(auth_url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token",
                 access_token="refreshtoken",
                 validate_certs=True,
                 client_id="cloud-services")
    KeycloakToken(**args).get()

# Generated at 2022-06-12 22:10:08.933537
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
    Provides test case for get method
    """
    # Test token creation
    test_token_request = KeycloakToken(access_token='test_access_token', auth_url='test_url')
    test_token_response = test_token_request.get()
    assert test_token_response

# Generated at 2022-06-12 22:10:19.363933
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.galaxy.token import GalaxyToken
    from ansible.module_utils.common.yaml import yaml_load
    import os
    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmp_dir, 'test_galaxy_token')
    dummy_token = 'abc123'
    test_token = GalaxyToken(dummy_token)
    test_token.save(tmp_file)
    with open(tmp_file, 'r') as f:
        test_config = yaml_load(f)
    assert test_config['token'] == dummy_token
    shutil.rmtree(tmp_dir)

# Generated at 2022-06-12 22:10:33.673727
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = "accesstoken"
    url = "https://url"
    kc = KeycloakToken(token, url)
    assert kc.get() == token

# Generated at 2022-06-12 22:10:44.852202
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # unit under test
    from ansible.galaxy.token import GalaxyToken
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six.moves import configparser

    # construct a mock 'token' file
    content = StringIO(u'[galaxy_server]\n')
    content.write(u'token = ')
    content.write(u'\n')
    mock_file = cStringIO(content.getvalue().encode('utf-8'))

    # construct the token object
    token = GalaxyToken()

    # alter the GalaxyToken._read() method
    def _read(self):
        ini_parser = configparser.ConfigParser()

# Generated at 2022-06-12 22:10:54.109576
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    new_token = 'test_token'

    galaxy_token_file_path = 'test_galaxy_token_file'
    galaxy_token_file = open(galaxy_token_file_path, 'w')
    galaxy_token_file.close()

    # Calling save with token None should not change the token
    galaxy_token = GalaxyToken(token=None)
    galaxy_token.b_file = to_bytes(galaxy_token_file_path)
    galaxy_token.save()

    with open(galaxy_token_file_path, 'r') as f:
        data = yaml_load(f)

    assert data == {}

    # Calling save with non None token should write this token to token file
    galaxy_token = GalaxyToken(token=new_token)
    galaxy_token.b_file = to_

# Generated at 2022-06-12 22:11:02.079796
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    k = KeycloakToken(auth_url=auth_url, access_token='12345')
    h = k.headers()
    assert h == {'Authorization': 'Bearer <TOKEN>'}
    # The token is only fetched if the property is accessed, so the
    # "TOKEN" present in the above string is never actually obtained.

# Generated at 2022-06-12 22:11:09.820932
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest
    import requests_mock


# Generated at 2022-06-12 22:11:21.918108
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token_file = '/tmp/test_token_file'

    c = {
        'token': 'abcxyz'
    }

    gt = GalaxyToken(token_file)

    gt.config = c
    gt.save()

    gt = GalaxyToken(token_file)
    assert gt.config == c

    token_file = '/tmp/test_token_file_malformed'
    with open(to_bytes(token_file, errors='surrogate_or_strict'), 'w') as f:
        f.write("12345678")
    gt = GalaxyToken(token_file)
    assert gt.get() is None

    token_file = '/tmp/test_token_file_missing'
    gt = GalaxyToken(token_file)
    assert gt.get() is None

# Generated at 2022-06-12 22:11:25.157837
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='foo', auth_url='http://auth.example.com')
    assert token.get() == 'mock_data.auth_url.json.data.access_token'

# Generated at 2022-06-12 22:11:29.226586
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'access_token'
    auth_url = 'https://auth.url'

    obj = KeycloakToken(access_token=access_token, auth_url=auth_url)
    result = obj.headers()
    assert 'Authorization' in result
    assert result['Authorization'] == 'Bearer access_token'



# Generated at 2022-06-12 22:11:40.401002
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    class TestKeycloakToken(KeycloakToken):
        def _form_payload(self):
            return 'grant_type=refresh_token&client_id=pytest&refresh_token=666'
    # unit test with a good token
    kt = TestKeycloakToken(access_token='666', auth_url='https://auth.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token', client_id='pytest')
    assert kt.headers() == {'Authorization': 'Bearer 666'}
    # unit test with a bad token

# Generated at 2022-06-12 22:11:51.405935
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from io import StringIO
    from ansible.module_utils.six import StringIO
    s = StringIO()
    def mock_open(name, mode, encoding=None):
        # print('mock_open(%r, %r, %r)' % (name, mode, encoding))
        return s

    import __builtin__
    __builtin__.open = mock_open

    def mock_chmod(name, mode, encoding=None):
        # print('mock_chmod(%r, %r, %r)' % (name, mode, encoding))
        return

    import os
    os.chmod = mock_chmod

    t = GalaxyToken()
    t.set('foobar')

    result = yaml_load(s.getvalue())
    assert result.get('token') == 'foobar'

# Generated at 2022-06-12 22:12:11.183297
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:12:21.470657
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    expected_dict = {
        'Authorization': 'Bearer XXXXXXXXXXXXXXXXXXXXXX'
    }

    class Resp:
        def __init__(self, resp):
            self.read = resp

    resp = Resp(json.dumps(
        {
            'access_token':'XXXXXXXXXXXXXXXXXXXXXX'
        }
    ))

    token = KeycloakToken(
        access_token='XXXXXXXXXXXXXX',
        auth_url='https://auth.redhat.com',
        validate_certs=True
    )

    with patch('ansible.module_utils.urls.open_url', return_value=resp):
        headers = token.headers()
        assert headers == expected_dict

# Generated at 2022-06-12 22:12:28.785967
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import tempfile

    b_file = '/tmp/test.yaml'

    if os.path.exists(b_file):
        os.remove(b_file)

    g = GalaxyToken()
    g.set('abcdef0123456789')

    with open(b_file, 'r') as f:
        config = yaml_load(f)

    assert 'token' in config
    assert config['token'] == 'abcdef0123456789'


# Generated at 2022-06-12 22:12:32.056784
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='test_token')
    header = token.headers().get('Authorization')
    assert header == 'Bearer test_token'

# Generated at 2022-06-12 22:12:39.009656
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:12:43.584018
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = '12345'
    galaxy_token = GalaxyToken(token)

    galaxy_token.save()

    with open(C.GALAXY_TOKEN_PATH) as f:
        content = f.read()
        assert to_text(token) in content

# Generated at 2022-06-12 22:12:54.673644
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create a fake temp file
    tempfile = open('/tmp/test_galaxy_token', 'w+')
    # Create a GalaxyToken instance
    token_instance = GalaxyToken()
    # Set the file to the instance
    token_instance._config = {'token': 'test_galaxy_token'}
    # Create a GalaxyToken instance
    token_instance.save()
    # Get data from the temp file to compare
    tempfile.seek(0)
    data = tempfile.read()
    tempfile.close()
    # Assert that the file match with the config
    assert data == "token: test_galaxy_token\n"
    # Remove the file to maintain filesystem clean
    os.remove('/tmp/test_galaxy_token')

# Generated at 2022-06-12 22:12:59.142116
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class response:
        def read(self):
            return b'{"access_token":"test123"}'
    resp = response()

    token = KeycloakToken(access_token='offline123', auth_url='http://auth', validate_certs=True)

    # Fake the response and make sure it extracts the access_token
    token.get() == 'test123'


# Generated at 2022-06-12 22:13:12.391912
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('access_token_123', 'https://auth.url.com')
    assert None == token.get()

    with open('test_token.txt', 'r') as f:
        token = KeycloakToken(f.read(), 'https://auth.url.com')

# Generated at 2022-06-12 22:13:17.375138
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import responses
    import json

    auth_url = 'https://sso.redhat.com/auth/realms/cloud-services/protocol/openid-connect/token'
    ok_token = None
    with open(os.path.join(os.path.dirname(__file__), 'data', 'keycloak_token_mock.json'), 'r') as f:
        ok_token = json.load(f)

    bad_token = None
    with open(os.path.join(os.path.dirname(__file__), 'data', 'keycloak_token_mock_client_id.json'), 'r') as f:
        bad_token = json.load(f)

    # Success case

# Generated at 2022-06-12 22:13:37.972042
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import unittest
    import base64

    class KeycloakTokenTest(unittest.TestCase):
        def setUp(self):
            self.token = KeycloakToken('dummy_token')

        def test_headers(self):
            headers = self.token.headers()
            self.assertEqual(headers['Authorization'], "Bearer %s" % self.token._token)

        def tearDown(self):
            pass

    suite = unittest.TestLoader().loadTestsFromTestCase(KeycloakTokenTest)
    unittest.TextTestRunner(verbosity=2).run(suite)



# Generated at 2022-06-12 22:13:44.361143
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = 'some token'
    auth_url = 'https://some.url/auth/realms/some-realm/protocol/openid-connect/token'
    kc = KeycloakToken(access_token=token, auth_url=auth_url)
    kc.get()
    assert kc.get() == token

# Generated at 2022-06-12 22:13:50.274332
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test normal path with no token in config file and no token passed in
    keycloak = KeycloakToken()
    assert keycloak.get() is None

    # Test normal path with token in config file and token passed in
    keycloak = KeycloakToken('12345678')
    assert keycloak.get() == '12345678'



# Generated at 2022-06-12 22:14:01.200598
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import random
    import os.path

    b_file = to_bytes(os.path.join(tempfile.gettempdir(), ''.join(str(random.randint(0, 9)) for i in range(10))), errors='surrogate_or_strict')
    # create object and set token
    token = GalaxyToken()
    token.b_file = b_file
    stored_token = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(40))
    token.set(stored_token)
    # reload object and check token is the same
    token = GalaxyToken()
    token.b_file = b_file
    assert token.get() == stored_token
    # teardown

# Generated at 2022-06-12 22:14:04.470686
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token = KeycloakToken(
        auth_url='http://auth.url.example',
        access_token='aaa')

    response = keycloak_token.get()
    assert response == 'bbb'

# Generated at 2022-06-12 22:14:11.646254
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.config['token'] = 'test'
    token.save()

    if os.path.isfile(token.b_file):
        with open(token.b_file, 'r') as f:
            config = yaml_load(f)
            assert config.get('token', None) == 'test'
        os.remove(token.b_file)

# Generated at 2022-06-12 22:14:15.182958
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken()
    assert token.headers() == {'Authorization': 'Bearer None'}
    token.get()
    assert token.headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:14:25.937726
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:14:28.918412
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_token = KeycloakToken("testToken")
    auth_token.get()
    assert auth_token.headers() == {'Authorization': 'Bearer %s' % auth_token.access_token}


# Generated at 2022-06-12 22:14:33.752451
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test should be removed when the class is being deployed
    kt = KeycloakToken(access_token='1234')
    assert kt.get() == '1234'


# Generated at 2022-06-12 22:14:56.927764
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    '''
    keycloak_token = KeycloakToken('9d0a5b89-0b00-401e-960d-b45f881a2f10')
    keycloak_token.get()
    keycloak_token.headers()
    '''
    pass


# Generated at 2022-06-12 22:15:06.025118
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken('testtoken')
    assert not os.path.isfile(C.GALAXY_TOKEN_PATH)
    gt.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)
    with open(C.GALAXY_TOKEN_PATH, 'r') as stream:
        content = yaml_load(stream)
        assert content.get('token', None) == 'testtoken'
    os.remove(C.GALAXY_TOKEN_PATH)