

# Generated at 2022-06-12 22:05:16.149726
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest
    import requests_mock
    from json import loads

    class TestKeycloakTokenGet(unittest.TestCase):

        def setUp(self):
            self.rhel_token = KeycloakToken(
                access_token='my-offline-key-in-ansible-cfg',
                auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                validate_certs=True)


# Generated at 2022-06-12 22:05:19.698075
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(access_token='test_refresh_token')
    assert kt.headers() == {'Authorization': 'Bearer test_access_token'}


# Generated at 2022-06-12 22:05:28.079862
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    with open('/tmp/test_GalaxyToken_save', 'w') as f:
        yaml_dump({'token': '', 'server': ''}, f, default_flow_style=False)
        os.chmod('/tmp/test_GalaxyToken_save', S_IRUSR | S_IWUSR)
    galaxyToken = GalaxyToken('/tmp/test_GalaxyToken_save')
    galaxyToken.save()
    galaxyToken2 = GalaxyToken('/tmp/test_GalaxyToken_save')
    assert galaxyToken2._config == {'token': '', 'server': ''}
    os.remove('/tmp/test_GalaxyToken_save')

# Generated at 2022-06-12 22:05:30.924466
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    t = KeycloakToken('secret')
    assert 'secret' == t.get()


# Generated at 2022-06-12 22:05:34.567838
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    gt.set('aa')
    assert gt.get() == 'aa'
    gt.save()
    assert gt.get() == 'aa'

# Generated at 2022-06-12 22:05:45.470192
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    cls = KeycloakToken("ye.mc.auth.tok.en", "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token", True, "cloud-services")

    import mock

    # Patch the method

# Generated at 2022-06-12 22:05:54.139305
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token = 'V1.1Q2W3E4R5T6'
    test_file = os.path.join('/tmp/ansible/test/.ansible/galaxy/tokens.yml')
    if os.path.isfile(test_file):
        os.remove(test_file)
    token = GalaxyToken(token=test_token)
    token.save()
    assert os.path.isfile(test_file)
    os.remove(test_file)



# Generated at 2022-06-12 22:06:02.732804
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    def open_url_side_effect(url, data=None, validate_certs=True, method=None, http_agent=None):
        class ResponseMock(object):
            def __init__(self, return_text):
                self.return_text = return_text
            def read(self):
                return self.return_text
        if data == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=token':
            return ResponseMock('{"access_token":"access_token"}')
        elif data == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=bad_token':
            return ResponseMock('{"error_description": "bad_token"}')

# Generated at 2022-06-12 22:06:05.272098
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken('dummy token')
    kct.get()


# Generated at 2022-06-12 22:06:17.165459
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.urls import open_url_static
    import base64

    class KeycloakToken():

        def __init__(self, access_token=None, auth_url=None, validate_certs=True, client_id=None):
            self.access_token = access_token
            self.auth_url = auth_url
            self._token = None
            self.validate_certs = validate_certs
            self.client_id = client_id
            if self.client_id is None:
                self.client_id = 'cloud-services'


# Generated at 2022-06-12 22:06:22.781358
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='12345')
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer 12345'



# Generated at 2022-06-12 22:06:30.809422
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:40.532829
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.galaxy.token import GalaxyToken
    token_file = '/tmp/token_file.yml'
    token = 'mytesttoken'
    token_file_object = GalaxyToken(token)
    token_file_object.b_file = token_file
    token_file_object.save()
    assert os.path.isfile(token_file)
    #open the file and read the content
    fd = open(token_file, 'r')
    token_dict = yaml_load(fd)
    fd.close()
    #clean up
    os.remove(token_file)
    #check token value is same in file
    assert token_dict['token'] == token



# Generated at 2022-06-12 22:06:50.784537
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class MockResponse(object):
        def __init__(self, data):
            self._data = data

        def read(self):
            return self._data

    class MockOpenUrl(object):
        def __init__(self, token_data):
            self._token_data = token_data

        def __call__(self, url, data, validate_certs, method, http_agent):
            payload = data.split('=')[1]
            return MockResponse(self._token_data.get(payload) or "Not found")

    access_token = 'dummy_token'

# Generated at 2022-06-12 22:07:02.108204
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:09.644177
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Confirm that the token can be saved to disk, then removed
    path = "/tmp/galaxy-token-test"
    token = GalaxyToken()
    token.b_file = to_bytes(path)
    token.set("test-token")
    assert os.path.isfile(token.b_file)
    assert token.get() == "test-token"

    # Restore the token to it's original value if any
    token = GalaxyToken()
    token.b_file = to_bytes(path)
    if token.get():
        token.set(token.get())
    else:
        token.set(NoTokenSentinel)

    # Remove the test file
    os.unlink(token.b_file)

# Generated at 2022-06-12 22:07:18.821667
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kt = KeycloakToken('test', 'test', False, 'test')
    data = {'access_token': 'test'}
    resp = MagicMock()
    resp.read.return_value = json.dumps(data).encode('utf-8')
    open_url_mock = MagicMock(return_value = resp)
    kt.open_url = open_url_mock
    assert kt.get() == 'test'
    assert open_url_mock.call_count == 1


# Generated at 2022-06-12 22:07:27.370202
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:35.036967
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # These values are from environment variables set by RHSM in RPM based systems
    # RHSM_TOKEN
    # RHSM_TOKEN_FILE
    # RHSM_URL
    import os
    token = os.environ.get('RHSM_TOKEN')

    url = os.environ.get('RHSM_URL')
    client_id = os.environ.get('RHSM_CLIENT_ID', 'cloud-services')
    t = KeycloakToken(token, url, client_id=client_id)
    t.get()


if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:07:45.838554
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:08:03.037175
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    for token_dict, token_info in {'access_token': '1234-abcd-5678-efgh',
                                   'auth_url': 'http://localhost:8080/auth/realms/master/protocol/openid-connect/token',
                                   'validate_certs': True,
                                   'client_id': 'cloud-services'}, \
                                  {'test_type': 'positive',
                                   'input_data': {'access_token': '1234-abcd-5678-efgh',
                                                  'auth_url': 'https://acme.org/api/authenticate/realms/me',
                                                  'validate_certs': False,
                                                  'client_id': 'cloud-services'}}:
        kt = KeycloakToken(**token_dict)

# Generated at 2022-06-12 22:08:13.386322
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_hmac = 'eyJhbGc...'
    test_json = {'access_token': 'eyJhbGc...',
                 'token_type': 'bearer',
                 'expires_in': 300,
                 'refresh_expires_in': 1800,
                 'refresh_token': 'eyJhbGc...',
                 'scope': 'openid'}

    import json
    import requests
    from mock import Mock
    from requests.exceptions import ConnectionError, HTTPError, Timeout
    from ansible.module_utils.urls import open_url
    from ansible.galaxy.token import KeycloakToken

    test_auth_url = 'https://auth.ansible.com/auth/realms/ansible/protocol/openid-connect/token'

    # test if

# Generated at 2022-06-12 22:08:20.405863
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:08:23.197639
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='test')
    assert token.get() is None
    token._token = 'test'
    assert token.get() == 'test'

# Generated at 2022-06-12 22:08:29.948040
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    print("test_KeycloakToken_headers")
    test_token = 'test-token'
    test_auth_url = 'test-auth-url'
    test_client_id = 'test-client-id'

    kctoken = KeycloakToken(test_token, test_auth_url, client_id=test_client_id)

    assert kctoken.headers() == {'Authorization': 'Bearer %s' % test_token}

# Generated at 2022-06-12 22:08:34.468100
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token_file = token.b_file
    token.set(token=True)
    token_file_content = open(token_file, 'r').read()
    assert token_file_content == 'token: true'

# Generated at 2022-06-12 22:08:41.446459
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import shutil

    token_file_path = os.path.join(C.TEST_DIR, C.GALAXY_TOKEN_PATH)
    shutil.copy(token_file_path, C.GALAXY_TOKEN_PATH)

    token = GalaxyToken().get()
    assert token
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)
    assert os.access(C.GALAXY_TOKEN_PATH, os.W_OK)

    GalaxyToken().save()

# Generated at 2022-06-12 22:08:46.795533
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    print("test_get_keycloak_token")
    kt = KeycloakToken()
    kt.auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    kt.access_token = "test"
    kt._token = "test2"
    assert kt.get() == "test2"



# Generated at 2022-06-12 22:08:50.515255
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    TOKEN_FILEPATH = '/tmp/token.yml'

    token = "1234567890123456789012345678901234567890"
    token_obj = GalaxyToken(token=token)

    token_obj.save()

    with open(TOKEN_FILEPATH, 'r') as f:
        config = yaml_load(f)

    assert config['token'] == token

# Generated at 2022-06-12 22:08:55.739153
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken('test_access_token', 'test_auth_url')
    expected_headers = {'Authorization': 'Bearer %s' % keycloak_token.get()}
    assert expected_headers == keycloak_token.headers()


# Generated at 2022-06-12 22:09:19.161163
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.config.manager import ConfigManager, get_ini_config_value, get_yaml_config
    from ansible.galaxy.token import GalaxyToken, KeycloakToken, BasicAuthToken
    import six
    import os

    config = ConfigManager()._config

    # initialize GalaxyToken with None
    token = GalaxyToken(None)

    galaxy_token_path = None
    if six.PY3:
        galaxy_token_path = os.path.join(os.path.dirname(__file__), "ansible.cfg")
    else:
        galaxy_token_path = os.path.join(os.path.dirname(__file__), "ansible.cfg")

    #test with no token specified
    token = GalaxyToken(None)
    assert token.get() is None

    #test with token already

# Generated at 2022-06-12 22:09:25.248240
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''Unit test for method save of class GalaxyToken'''
    # setup
    token = GalaxyToken()
    token.config = {'token': '12345'}

    # test
    token.save()

    # verify
    config = token._read()
    assert 'token' in config
    assert config['token'] == '12345'
    os.remove(C.GALAXY_TOKEN_PATH)



# Generated at 2022-06-12 22:09:30.190650
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Get token first time
    token = KeycloakToken(access_token = "abcd", auth_url = "http://testurl.com").get()
    assert token == "some_token"

    # Get token second time, this time we check that it is cached
    token = KeycloakToken(access_token = "abcd", auth_url = "http://testurl.com").get()
    assert token == "some_token"

# Generated at 2022-06-12 22:09:41.182246
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    client_id = 'cloud-services'
    ValidateCerts = True


# Generated at 2022-06-12 22:09:50.547362
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # patch the class method _form_payload
    def _form_payload(self):
        return 'grant_type=refresh_token&client_id=%s&refresh_token=%s' % ('cloud-services',
                                                                           'test_refresh_token')

    KeycloakToken._form_payload = _form_payload

    # patch the class method get
    def get(self):
        return 'test_token'

    KeycloakToken.get = get

    # prepare input/output data
    token = KeycloakToken(access_token='test_refresh_token',
                          auth_url='https://test_auth_url/')
    expected_headers = {'Authorization': 'Bearer test_token'}

    # test the method headers of class KeycloakToken
   

# Generated at 2022-06-12 22:09:57.053713
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test for method get of class KeycloakToken
    # Success path. Expected output = 'abc123def456'
    token = KeycloakToken(access_token='xyz789', auth_url='https://example.com')
    token.get()
    # Token should be valid, so it should match the example value above.
    assert token._token == 'abc123def456'

    # Failure path. Expected output = None
    token = KeycloakToken(access_token=None, auth_url=None)
    token.get()
    # Token should be invalid, so it should be None
    assert token._token is None

# Generated at 2022-06-12 22:10:00.170081
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    k = KeycloakToken(access_token='foobar')
    headers = k.headers()
    assert isinstance(headers, dict)
    assert headers['Authorization'] == 'Bearer None'


# Generated at 2022-06-12 22:10:03.232853
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken(access_token='test_token')
    keycloak_token.get()

    assert keycloak_token.headers() == {'Authorization': 'Bearer test_token'}


# Generated at 2022-06-12 22:10:05.845420
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(auth_url='https://foo.bar',access_token="1234567890")
    headers = kt.headers()
    assert headers['Authorization'] == "Bearer None"

# Generated at 2022-06-12 22:10:14.353628
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_url = 'https://auth.service.com/auth/realms/acme/protocol/openid-connect/token'
    access_token = 'TOKEN_TO_REFRESH'
    keycloak_token = KeycloakToken(access_token=access_token, auth_url=auth_url)

    headers = keycloak_token.headers()
    expected_headers = {'Authorization': 'Bearer <access_token>'}
    assert headers == expected_headers


# Generated at 2022-06-12 22:10:41.104119
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_token = KeycloakToken(access_token='foo')
    headers = test_token.headers()
    assert (headers == {'Authorization': 'Bearer foo'})



# Generated at 2022-06-12 22:10:44.142108
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='1234abcd')
    headers = token.headers()
    assert 'Bearer 1234abcd' in headers['Authorization']
    return


# Generated at 2022-06-12 22:10:53.607323
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token_content = "temp_token"
    test_token_file = '/tmp/test_token'
    token = GalaxyToken(token=test_token_content)
    saved_token_file = os.path.join(os.environ['HOME'], '.ansible', 'test_token')
    os.environ['HOME'] = '/tmp'
    token.b_file = saved_token_file
    token.save()
    token.config['token'] = None
    token.save()
    with open(saved_token_file, 'r') as f:
        saved_token_content = yaml_load(f)
    assert saved_token_content['token'] == test_token_content
    # Clean up
    os.remove(saved_token_file)

# Generated at 2022-06-12 22:10:56.608807
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='dummy', auth_url='http://example.com')
    token.get()

# Generated at 2022-06-12 22:11:01.288396
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    t = GalaxyToken(token="thisisatoken")
    t.save()
    with open(t.b_file, 'r') as f:
        config = yaml_load(f)
    assert config['token'] == "thisisatoken"
    os.remove(t.b_file)


# Generated at 2022-06-12 22:11:03.922059
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    mytoken = KeycloakToken(access_token="dummy_token", auth_url="http://dummyurl.com/", client_id="dummy_client_id")
    assert mytoken.get() == "dummy_token"


# Generated at 2022-06-12 22:11:09.343376
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class mock_open_url(object):
        def __init__(self, *args, **kwargs):
            pass

        def read(self):
            return '{"access_token": "my_access_token"}'

    mocker = mock.patch("ansible.module_utils.urls.open_url")
    mocker.side_effect = mock_open_url

    keycloak_token = KeycloakToken("REFRESH_TOKEN")
    assert keycloak_token.get() == 'my_access_token'



# Generated at 2022-06-12 22:11:12.260971
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(access_token='foo', auth_url='http://localhost')
    headers = kt.headers()
    assert headers['Authorization'] == 'Bearer bar'

# Generated at 2022-06-12 22:11:16.308858
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():

    token_content = {'token': 'my_token', 'ignore_certs': True}

    class FakeFile():
        content = 'fakecontent'
        def __init__(self, filename, mode):
            if mode is not 'w':
                raise Exception('Unable to open the file')

        def write(self, content):
            self.content = content

        def close(self):
            pass

    def fake_yaml_dump(content, file):
        file.write(content)

    f_open = FakeFile(to_bytes("path", errors='surrogate_or_strict'), 'w')

    token = GalaxyToken()


# Generated at 2022-06-12 22:11:22.475751
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = 'abc'
    auth_url = 'https://auth.example.com/auth/realms/test/protocol/openid-connect/token'
    client_id = 'test-client'

    kc_token = KeycloakToken(access_token=token, auth_url=auth_url, client_id=client_id)
    assert kc_token.headers() == {'Authorization': 'Bearer %s' % token}

# Generated at 2022-06-12 22:11:50.355468
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile

    fd, filename = tempfile.mkstemp()
    try:
        os.close(fd)

        gt = GalaxyToken(token='abcd-1234')
        gt.b_file = to_bytes(filename, errors='surrogate_or_strict')

        gt.save()

        with open(filename, 'r') as f:
            content = yaml_load(f)

        assert {'token': 'abcd-1234'} == content
    finally:
        os.unlink(filename)


# Generated at 2022-06-12 22:11:53.330618
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kc_token = KeycloakToken(access_token='test_token')
    # It's expected to be empty, since the method does not do anything with the passed access_token
    assert kc_token.get() == None


# Generated at 2022-06-12 22:11:59.785449
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJmajVrUG1fN1JzdG9xdXZNUGZ3WEVLZ3lNbk1NVy1RV29OdVB0R0VlVWI2In0"
    expected_headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJmajVrUG1fN1JzdG9xdXZNUGZ3WEVLZ3lNbk1NVy1RV29OdVB0R0VlVWI2In0'}
   

# Generated at 2022-06-12 22:12:09.615045
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = "https://devfederate.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    access_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfTTJmZk1rdHBvTHY2Q2tybXZZT0ZzTlZtbGZ30080000"
    token = KeycloakToken(access_token, auth_url)

# Generated at 2022-06-12 22:12:14.979494
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_token = KeycloakToken(access_token='test_access_token', client_id='test_client_id')
    test_dict = {'Authorization': 'Bearer test_access_token'}
    assert test_token.headers() == test_dict


# Generated at 2022-06-12 22:12:20.018814
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''
    Test for method save of class GalaxyToken
    :return: None
    '''
    gt = GalaxyToken()
    new_token = "new_token"
    gt._token = new_token
    gt.save()
    assert gt.get() == new_token


# unit test for method get of class GalaxyToken

# Generated at 2022-06-12 22:12:31.106786
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Success case
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    access_token = 'ZHV262bPxBaIRpzgfMhcJlD0rAo=:1452535204783:a0a25c4960d3b3d8fb2cdd764d60e22c79bca681'
    kct = KeycloakToken(access_token=access_token, auth_url=auth_url)
    assert kct.get() == 'ZHV262bPxBZkzG8Cc7J0hP29oHpFvAl9nWtZNyrtHdA='

    # Failure case

# Generated at 2022-06-12 22:12:33.382884
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = '12345'
    kt = KeycloakToken(access_token=token)
    headers = kt.headers()
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Bearer %s' % token

# Generated at 2022-06-12 22:12:45.951245
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:12:50.127488
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    tkn = GalaxyToken()
    tkn.set('test')
    for line in open(C.GALAXY_TOKEN_PATH).readlines():
        assert 'test' in line

# Generated at 2022-06-12 22:13:30.528786
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    assert KeycloakToken(access_token="abcdefg").headers() == {'Authorization': u'Bearer abcdefg'}



# Generated at 2022-06-12 22:13:35.595982
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    try:
        # get a random file name and verify it doesn't exist
        import tempfile
        fn = tempfile.mktemp()
        assert not os.path.exists(fn)
        gt = GalaxyToken()
        gt.b_file = fn
        gt.set('ATOKEN')
        assert os.path.exists(fn)
    finally:
        os.remove(fn)

# Generated at 2022-06-12 22:13:36.445503
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc_token = KeycloakToken()


# Generated at 2022-06-12 22:13:40.296597
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Arrange
    token = KeycloakToken()

    # Act
    h = token.headers()

    # Assert
    assert h
    assert 'Authorization' in h
    assert h['Authorization'] == 'Bearer '


# Generated at 2022-06-12 22:13:50.546328
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    gt.set('token')
    test_path = 'tmp/galaxy_token'
    constants_backup = C.GALAXY_TOKEN_PATH
    C.GALAXY_TOKEN_PATH = test_path
    gt.save()
    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        test = yaml_load(f)
    assert test == {'token': 'token'}
    # restore original
    C.GALAXY_TOKEN_PATH = constants_backup
    # remove tmp file
    os.remove(C.GALAXY_TOKEN_PATH)

# Generated at 2022-06-12 22:14:00.392063
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import shutil
    import os
    import yaml

    TOKEN_CONTENT = {'token': '1234567890'}
    temp_dir = tempfile.mkdtemp()
    token_path = os.path.join(temp_dir, 'test_ansible_token')
    token = GalaxyToken(token_path)
    token.set(TOKEN_CONTENT['token'])
    assert token.get() == TOKEN_CONTENT['token']
    with open(token_path, 'r') as f:
        written_content = yaml.load(f)
    assert TOKEN_CONTENT == written_content
    shutil.rmtree(temp_dir)

# Generated at 2022-06-12 22:14:08.921212
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    b_file = to_bytes(C.GALAXY_TOKEN_PATH, errors='surrogate_or_strict')
    try:
        os.remove(b_file)
    except OSError:
        pass

    b_token = to_bytes("test_file_token1")

    token = GalaxyToken(b_token)
    token.save()
    token = GalaxyToken()
    assert(os.path.isfile(b_file))
    assert(token.get() == to_text(b_token))
    os.remove(b_file)


# Generated at 2022-06-12 22:14:12.518976
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kct = KeycloakToken(access_token='test-token')
    headers = kct.headers()
    assert headers['Authorization'] == 'Bearer test-token'

# Generated at 2022-06-12 22:14:19.863939
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Given a mock access_token for KeycloakToken
    access_token="dummy_access_token"
    # And a mock auth_token for KeycloakToken
    auth_url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    # When the KeycloakToken.get() method is executed
    token = KeycloakToken(access_token, auth_url).get()

    # Then the value returned is obviously 
    assert token == "mock_token_returned_by_keycloak_server"

# Generated at 2022-06-12 22:14:25.533041
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Create class instance
    keycloak_instance = KeycloakToken(access_token="123456789", auth_url="https://example.com/auth/realms/realm/protocol/openid-connect/token", client_id="example_client")
    resp = keycloak_instance.get()
    assert resp == "123456789"
