

# Generated at 2022-06-12 22:05:15.454828
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.six.moves.urllib.parse import urlencode
    from ansible.module_utils.six.moves.urllib.request import Request


# Generated at 2022-06-12 22:05:22.845630
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('12345')
    assert token.get() == '12345'

    token = KeycloakToken('12345', auth_url='https://example.com/auth/realms/redhat_ansible/protocol/openid-connect/token')
    assert token.get() == '12345'

    # TODO: write better test
    token = KeycloakToken('12345', auth_url='https://example.com/auth/realms/redhat_ansible/protocol/openid-connect/token')
    assert token.get() == '12345'

# Generated at 2022-06-12 22:05:33.947687
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'abcdefg'
    auth_url = 'https://keycloak.example.com/auth/realms/redhat/protocol/openid-connect/token'
    validate_certs = True
    client_id = 'cloud-services'
    keycloak_token = KeycloakToken(access_token=access_token, auth_url=auth_url,
                                   validate_certs=validate_certs, client_id=client_id)
    keycloak_token_headers = keycloak_token.headers()
    assert keycloak_token_headers.get('Authorization') == 'Bearer %s' % keycloak_token.get()

# Generated at 2022-06-12 22:05:39.018071
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = 'test_offline_token'
    auth_url = 'https://test.url'
    test_tokenizer = KeycloakToken(access_token=token, auth_url=auth_url)
    tokenizer_token = test_tokenizer.get()
    assert tokenizer_token



# Generated at 2022-06-12 22:05:43.792371
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kct = KeycloakToken('foo')
    assert 'Authorization' in kct.headers()
    assert kct.headers()['Authorization'] == 'Bearer foo'
    assert 'Authorization' in kct.headers()
    assert kct.headers()['Authorization'] == 'Bearer foo'



# Generated at 2022-06-12 22:05:55.495874
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token = '123456789'
    ansible_cfg_dir = os.path.dirname(C.CONFIG_FILE)
    test_file_path = os.path.join(ansible_cfg_dir, 'tmp_galaxy_token.yml')
    display.vvv('path to test token file: %s' % test_file_path)
    token_obj = GalaxyToken(token=test_token)
    token_obj.b_file = to_bytes(test_file_path, errors='surrogate_or_strict')
    token_obj.save()
    display.vvv('content of test token file: %s' % yaml_load(open(test_file_path)))

# Generated at 2022-06-12 22:05:57.509809
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    os.environ['OS_TOKEN']="token-value"
    os.environ['OS_AUTH_URL']="url-value"
    token = KeycloakToken(auth_url="url-value")
    assert token.get() == "token-value"


# Generated at 2022-06-12 22:05:59.646760
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('my_access_token', 'http://example.com')

    assert token.headers() == {'Authorization': 'Bearer my_access_token'}

# Generated at 2022-06-12 22:06:12.748260
# Unit test for constructor of class KeycloakToken

# Generated at 2022-06-12 22:06:22.266744
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Test cases
    testcases = [
        {
            "description": "Standard bearer token",
            "access_token": "sometoken",
            "auth_url": "https://somewhere.com",
            "result": "Bearer sometoken"
        },
        {
            "description": "Bearer token with a space",
            "access_token": "sometoken sometoken",
            "auth_url": "https://somewhere.com",
            "result": "Bearer sometoken sometoken"
        },
        {
            "description": "Bearer token with a colon",
            "access_token": "sometoken:sometoken",
            "auth_url": "https://somewhere.com",
            "result": "Bearer sometoken:sometoken"
        }
    ]


# Generated at 2022-06-12 22:06:30.549462
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():  # noqa: N802
    kc = KeycloakToken('access_token', 'http://127.0.0.1:8080/auth', False)
    assert kc.headers() == {'Authorization': 'Bearer None'}


# Generated at 2022-06-12 22:06:34.562618
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token",
                          access_token = "FOO")
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer FOO'


# Generated at 2022-06-12 22:06:46.811511
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    def _read_mock(self):
        return {
            'token_type': 'Bearer',
            'access_token': 'test_access_token',
            'resource_server_url': 'test_resource_server_url'
        }

    KeycloakToken._read = _read_mock
    KeycloakToken._form_payload = lambda self: ''
    KeycloakToken.auth_url = 'test_auth_url'

    def _open_url_mock(auth_url):
        fake_resp = ['{', '"access_token": "test_token2"', '}']
        for item in fake_resp:
            yield item

    KeycloakToken.open_url = _open_url_mock
    KeycloakToken.get = KeycloakToken.get
    token = Key

# Generated at 2022-06-12 22:06:50.655932
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
    This method was created in order to test get method of class KeycloakToken.
    """
    test = "{\"access_token\":\"RANDOM_TOKEN\"}"
    test_token = KeycloakToken("RANDOM_REFRESH_TOKEN")
    test_token.get() == test["access_token"]

# Generated at 2022-06-12 22:06:57.805591
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    print("Executing test_GalaxyToken_save")
    galaxy_token = GalaxyToken()
    galaxy_token.set('test')
    galaxy_token.save()

    with open(galaxy_token.b_file) as f:
        config = yaml_load(f)

    if config['token'] == 'test':
        print('Test was successful')
    else:
        print('Test failed!')


# Generated at 2022-06-12 22:07:07.060821
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import mock
    from ansible.module_utils.urls import open_url as _open_url
    with mock.patch('ansible.module_utils.urls.open_url', _open_url):
        # Scenario 1: request_token not valid
        with mock.patch.object(KeycloakToken, "_form_payload", return_value="grant_type=refresh_token&client_id=cloud-services&refresh_token=not_a_real_token"):
            test_token = KeycloakToken("not_a_real_token", auth_url="http://not_a_real_host")
            test_token.get()
            assert(test_token._token is None)

        # Scenario 2: request_token valid

# Generated at 2022-06-12 22:07:11.280356
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
  k = KeycloakToken('dummy_token', 'dummy_url')
  h = k.headers()
  assert(h['Authorization'] == 'Bearer None')


# Generated at 2022-06-12 22:07:22.740089
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''This function creates a temporary file, saves the content of the file using save() and checks the file content and validity'''
    import tempfile, os, shutil
    from ansible.utils.display import Display
    from ansible.module_utils.ansible_galaxy.models.token import GalaxyToken, NoTokenSentinel
    display = Display()

    fd, temp_file = tempfile.mkstemp()
    display.display("temp_file is %s" % temp_file)
    token = NoTokenSentinel()

    galaxy_token = GalaxyToken(token)
    galaxy_token.b_file = temp_file

    display.display("Creating new galaxy token file %s" % temp_file)
    galaxy_token.save()


# Generated at 2022-06-12 22:07:33.595858
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    js = json.load(open('test/test_data/sso_token.json'))

    ktk = KeycloakToken(access_token=js['access_token'],
                        auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                        client_id='automation-broker',
                        validate_certs=True)

    headers = ktk.headers()


# Generated at 2022-06-12 22:07:41.311856
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """Unit test for method get of class KeycloakToken"""

    # test case 1
    access_token = 'test_token'
    auth_url = 'test_auth_url'
    test_kc_token_obj = KeycloakToken(access_token=access_token, auth_url=auth_url)
    assert test_kc_token_obj._form_payload() == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=test_token'

    assert test_kc_token_obj.get() != 'test_token'
    # TODO: mocker support is not reentrant
    # Check exception handlinng in case of open-url error
    # TODO: This test is not exhaustive
    # https://github.com/ansible/ansible/issues/

# Generated at 2022-06-12 22:07:52.725527
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_url = "https://cloud.redhat.com/api/token"

# Generated at 2022-06-12 22:07:56.950003
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = 'foobar'
    gt = GalaxyToken()
    gt.set(token)
    assert gt.get() == token

    gt = GalaxyToken(token)
    assert gt.get() == token



# Generated at 2022-06-12 22:08:08.172539
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    """ This test case ensures that header is created twice and
        is same for the second call for the same token.
    """
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTkzNTYwODAyLCJleHAiOjE1OTM2NDcyMDJ9.y3q8cGNOtCVF_WrlfL-G5Z5bRZ1Et9Xk-fP3tqPp_g8"

# Generated at 2022-06-12 22:08:17.044403
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = 'token'
    try:
        import __builtin__ as builtins  # python2
    except:
        import builtins  # python3
    old_open = builtins.open
    to_write = ''
    def my_open(name, mode):
        if name == 'galaxy.token' and mode == 'w':
            return old_open(name, mode)
        return old_open(name, 'r')
    builtins.open = my_open
    g_token = GalaxyToken(token)
    g_token.save()
    builtins.open = old_open
    with open('galaxy.token', 'r') as f:
        to_write = f.read()
    assert to_write == 'token: {}'

# Generated at 2022-06-12 22:08:21.000142
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_get = KeycloakToken(access_token='test_token').get()
    assert test_get == 'test_token'
    test_headers = KeycloakToken(access_token='test_token').headers()
    assert test_headers['Authorization'] == 'Bearer test_token'

# Generated at 2022-06-12 22:08:28.938552
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import pytest
    from ansible.module_utils.common.json import from_json, to_json
    from ansible.module_utils.urls import open_url

    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.params = {}

    class FakeHttplibResponse(object):
        def __init__(self, resp_data):
            self.read = lambda: resp_data

    class FakeHttplibConnection(object):
        def __init__(self, resp_data):
            self.resp_data = resp_data

        def request(self, method, url, **kwargs):
            self.resp = FakeHttplibResponse(self.resp_data)

        def getresponse(self):
            res = self.resp

# Generated at 2022-06-12 22:08:40.269926
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # KeycloakToken.get should return 'token' if server response json is the expected format
    test_access_token = 'test_access_token'
    test_auth_url = 'http://example.com'
    test_client_id = 'test_client_id'
    test_server_response = '{"access_token":"test_access_token"}'
    test_inputs = {'access_token': test_access_token,
                   'auth_url': test_auth_url,
                   'client_id': test_client_id}
    test_kwargs = {'data': 'grant_type=refresh_token&client_id=%s&refresh_token=%s' % (test_client_id,
                                                                                       test_access_token)}

# Generated at 2022-06-12 22:08:44.343846
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_values = [
        (KeycloakToken('test_offline_token', 'test_url'),
         {'Authorization': 'Bearer test_access_token'}),
    ]

    for token, expected_headers in test_values:
        assert token.headers() == expected_headers

# Generated at 2022-06-12 22:08:47.278031
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # TODO: find a way to test KeycloakToken.get() in a
    # reliable way. It is a black box (no input, only output)
    # and it relies on an external Web server to get the token
    pass



# Generated at 2022-06-12 22:08:52.056993
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create a fake token file
    token = "abcdefghijklmnopqrstuvwxyz"
    fake_token = tempfile.NamedTemporaryFile()
    fake_token.write('token: "%s"' % token)
    fake_token.seek(0)
    galaxy_token = GalaxyToken(fake_token.name)
    galaxy_token.save()
    fake_token.close()
    # Check if the saved token file is the same as the fake token file
    with open(fake_token.name, 'r') as f:
        assert token == yaml_load(f)['token']

# Generated at 2022-06-12 22:09:07.170886
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kt = KeycloakToken(auth_url="http://fake.com", access_token="faketoken")
    assert kt.get() == "faketoken"

# Generated at 2022-06-12 22:09:18.902640
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    device_id = 'this-is-a-fake-device-id'
    device_name = 'this-is-a-fake-device-name'
    scope = 'this-is-a-fake-scope'
    token = KeycloakToken(auth_url='url_to_fake_keycloak_server', validate_certs=False,
                          access_token='this-is-a-fake-access-token')

    # TODO: test response error
    assert token.get() == 'this-is-a-fake-access-token'
    assert token.headers() == {'Authorization': 'Bearer this-is-a-fake-access-token'}


# Generated at 2022-06-12 22:09:29.265425
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:09:40.588627
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.parsing.vault import VaultLib
    from io import StringIO
    from tempfile import NamedTemporaryFile

    token = 'abc'
    vault_password = 'password'

    with NamedTemporaryFile(delete=True) as fp:
        v = VaultLib(vault_password)
        enctoken = v.encrypt(token)
        yaml_dump({'token': enctoken}, fp)
        fp.seek(0)

        g = GalaxyToken(NoTokenSentinel())
        g.b_file = fp.name
        # Save the new vault password
        g.set(token)

        # Write out the vault file again
        g.save()

        fp.seek(0)
        data = yaml_load(fp)
        # Check that the token has been dec

# Generated at 2022-06-12 22:09:45.678752
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('test_token', 'https://localhost/auth/realms/test/protocol/openid-connect/token', 'https://localhost/auth/realms/test/protocol/openid-connect/token')
    headers = token.headers()
    assert(headers['Authorization'] == 'Bearer test_token')

# Generated at 2022-06-12 22:09:55.720561
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:10:02.968180
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import responses
    import json

    access_token = 'offline_access'
    auth_url = 'https://keycloak.example.com/auth/realms/ansible/protocol/openid-connect/token'
    token = 'Zm9vYmFy'

    responses.add(responses.POST, auth_url,
                  body=json.dumps({'access_token': token}),
                  content_type='application/json')

    keycloak_token = KeycloakToken(access_token, auth_url)
    assert keycloak_token.get() == token

# Generated at 2022-06-12 22:10:05.594712
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='test')
    tok_dict = token.headers()
    assert tok_dict.get('Authorization') == 'Bearer test'

# Generated at 2022-06-12 22:10:17.907016
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    dname = os.path.dirname(__file__)
    tmp_dir_path = os.path.join(dname, '../../../test/integration/galaxy_token_dir')
    galaxy_token_path = os.path.join(tmp_dir_path, 'galaxy_token')
    cpath = os.path.join(dname, '../../../test/integration/galaxy_token_dir/ansible.cfg')
    C.DEFAULT_LOCAL_TMP = tmp_dir_path
    C.GALAXY_TOKEN_PATH = galaxy_token_path
    galaxy_token_test = GalaxyToken()
    galaxy_token_test.save()
    with open(cpath) as f:
        config = yaml_load(f)
    assert 'token' not in config


# Generated at 2022-06-12 22:10:20.877925
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('abcdefghijklmnopqrstuvwxyz')
    assert token.get() == 'abcdefghijklmnopqrstuvwxyz'


# Generated at 2022-06-12 22:10:41.777951
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile

    with tempfile.NamedTemporaryFile() as f:
        token = GalaxyToken(token='abc')
        token.b_file = to_bytes(f.name)
        token.save()
        f.seek(0)
        content = f.read()

    if to_text(content) != to_text('token: abc\n'):
        raise AssertionError


# Generated at 2022-06-12 22:10:47.354480
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token_content = {'token': 'foobar'}
    token.config.update(token_content)
    token.save()
    result = token._read()
    assert result == token_content
    os.remove(C.GALAXY_TOKEN_PATH)

# Generated at 2022-06-12 22:10:55.093712
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():

    test_token_path = '/etc/ansible/test_token'

    def remove_galaxy_token():
        if os.path.isfile(test_token_path):
            os.unlink(test_token_path)

    remove_galaxy_token()
    assert not os.path.isfile(test_token_path)

    token_config = C.GALAXY_TOKEN_PATH

# Generated at 2022-06-12 22:11:05.729746
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:07.543098
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='abc')
    assert token.headers() == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:11:19.691457
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # create temporary file, containing the string "token: test"
    with open(C.GALAXY_TOKEN_PATH, 'w') as f:
        f.write("token: test")

    gt = GalaxyToken()

    assert gt.get() is None
    assert gt.config == {'token': None}

    gt.set('test1')
    assert gt.get() == 'test1'
    assert gt.config == {'token': 'test1'}

    gt.set('test2')
    assert gt.get() == 'test2'
    assert gt.config == {'token': 'test2'}

    # remove temporary file
    os.remove(C.GALAXY_TOKEN_PATH)


__all__ = [KeycloakToken, GalaxyToken]

# Generated at 2022-06-12 22:11:27.856381
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Test that keycloak token type is Bearer
    access_token = 'fdsjfsdfs'
    auth_url = 'https://example/token'
    client_id = 'cloud-services'
    token = KeycloakToken(access_token=access_token, auth_url=auth_url, client_id=client_id)
    assert token.token_type == 'Bearer'

    # Test that keycloak token.headers contains the correct key/value pair
    assert token.headers() == {'Authorization': '%s %s' % (token.token_type, token.get())}


# Generated at 2022-06-12 22:11:34.256122
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    """Unit testing for save method of GalaxyToken object.
       Suppose to create new config file and save it in place specified by path"""
    # Arrange
    path = 'tempfile.yaml'
    expected_file = {'token': 'Value'}

    # Act
    token = GalaxyToken('Value')
    token.b_file = to_bytes(path)
    token.save()

    with open(path) as file:
        result = yaml_load(file)

    os.remove('tempfile.yaml')
    # Assert
    assert expected_file == result

# Generated at 2022-06-12 22:11:47.307183
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import tempfile
    import yaml

    fd, tmp = tempfile.mkstemp(prefix='ansible-token-')
    token_file = os.fdopen(fd, 'w')
    os.chmod(token_file.name, S_IRUSR | S_IWUSR)  # owner has +rw

    token = GalaxyToken()
    token._read = lambda x: {"token": "test_token"}
    token.b_file = token_file.name
    token.save()

    token_file.close()
    with open(token_file.name, 'r') as f:
        assert yaml.safe_load(f) == {'token': 'test_token'}
    os.remove(token_file.name)

# Generated at 2022-06-12 22:11:57.505350
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Testing that the file is created if not existing (with the expected rights)
    # and that it is overwritten if existing
    # Some "secrets" are printed to the stdout (right of the file, content of the file)
    # So use this code only for tests purposes
    # Note: global_args['galaxy_token_file'] is set to /tmp/test_galaxy_token
    #       global_args['server'] is set to https://galaxy.example.com
    #       global_args['ignore_certs'] is set to false
    token = '7d1f8d90b7e84b069d4a4cbf4f39397b'
    global_args = {}
    global_args['galaxy_token_file'] = '/tmp/test_galaxy_token'

# Generated at 2022-06-12 22:12:33.393538
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import uuid
    import httpretty
    from ansible.module_utils.galaxy.token import KeycloakToken
    import json


    class MockToken:
        def __init__(self, token):
            self._token = token

        def get(self):
            return self._token

    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

# Generated at 2022-06-12 22:12:45.916294
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import os
    import json
    import httpretty

    # Disable the cache
    os.environ["ANSIBLE_GALAXY__CACHE_PLUGIN_TOKEN"] = ""


# Generated at 2022-06-12 22:12:58.013944
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    from ansible.module_utils.acme import KeycloakToken
    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    token_obj = KeycloakToken("offline_token", auth_url, client_id="cloud-services")

# Generated at 2022-06-12 22:13:10.422339
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.six.moves.mock import patch, mock_open, call
    from ansible.module_utils.urls import open_url

    # patch open_url to return a canned 'access_token'

# Generated at 2022-06-12 22:13:22.311900
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import io
    import sys
    import mock

    sys.modules['requests'] = mock.MagicMock()
    # Set up mock to return valid Galaxy data when called
    mock_response = mock.MagicMock()

# Generated at 2022-06-12 22:13:33.635423
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import pytest

    mock_response_content = b'{"access_token":"eyJhbGc","expires_in":7200,"refresh_expires_in":1800,"refresh_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6Ii1h","token_type":"bearer","not-before-policy":0,"session_state":"53a8d8a1-0ac3-4de2-ae32-3f4d4e4f8324"}'
    mock_token_url = 'https://sso.redhat.com/auth/realms/ansible/protocol/openid-connect/token'

    mock_response = pytest.Mock()
    mock_response.read = pytest.Mock(return_value=mock_response_content)


# Generated at 2022-06-12 22:13:35.689187
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import uuid
    fake_token = uuid.uuid4().hex
    keycloak_token = KeycloakToken(access_token=fake_token)
    header = keycloak_token.headers()
    assert header['Authorization'] == 'Bearer %s' % fake_token


# Generated at 2022-06-12 22:13:37.924207
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # TODO: improve the test to provide actual return contents.
    kt = KeycloakToken(access_token='123')
    resp = kt.get()
    print(resp)


# Generated at 2022-06-12 22:13:43.393675
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # test with good data
    access_token = 'd3d3Ll9hdXRoX3VybF8uY29t'
    auth_url = 'https://_auth_url_.com/auth/realms/myrealm/protocol/openid-connect/token'
    validate_certs = True
    kt_object = KeycloakToken(access_token, auth_url, validate_certs)
    expected_token = 'ZW5kLXRoaXMtcmVhc29u'
    kt_get_token = kt_object.get()
    assert (kt_get_token == expected_token), "Access token should be '{0}' but instead was '{1}'".format(expected_token, kt_get_token)


# Generated at 2022-06-12 22:13:49.610993
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    test_token = '12345'
    kt = KeycloakToken('refresh_token')

    # Test with no token
    assert kt.headers() == {'Authorization': 'Bearer None'}

    # Test with token
    kt._token = test_token
    assert kt.headers() == {'Authorization': 'Bearer 12345'}

# Generated at 2022-06-12 22:14:19.185741
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class FakeResponse(object):
        def __init__(self, response):
            self._response = response
            self.headers = {'content-type': 'application/json'}
            self.status_code = 200

        def read(self):
            return self._response

        def getcode(self):
            return self.status_code

    def mocked_open_url(*args, **kwargs):
        return FakeResponse(json.dumps({u'access_token': u'access token'}))

    import __builtin__
    from ansible.module_utils.urls import open_url
    __builtin__.open_url = mocked_open_url
    token = KeycloakToken(access_token=u'offline_token', auth_url=u'keycloak auth url')

    assert token is not None


# Generated at 2022-06-12 22:14:24.555629
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    with open(C.GALAXY_TOKEN_PATH, 'w') as f:
        f.write("")
    token = GalaxyToken()
    token.set("foobar")
    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        assert f.readline() == "token: foobar\n"

# Generated at 2022-06-12 22:14:32.779348
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest
    import mock
    import httpretty
    import http.client

    class HttprettyResponse(object):
        def __init__(self, status=200, msg=None, empty=False, **kwargs):
            self.status = status
            self.reason = msg or http.client.responses.get(status)
            self._empty = empty

        def read(self):
            return "{}".encode() if self._empty else '{ "access_token": "fake_token" }'.encode()

    class TestKeycloakToken(unittest.TestCase):
        def setUp(self):
            self.auth_url = 'https://sso.redhat.com/auth/realms/cloudservices/protocol/openid-connect/token'

# Generated at 2022-06-12 22:14:38.586917
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():

    kct = KeycloakToken(access_token='abcd1234', auth_url='http://test.url')

    assert kct.headers() == {'Authorization': 'Bearer <no value>'}

    kct._token = 'token_expired'

    assert kct.headers() == {'Authorization': 'Bearer token_expired'}



# Generated at 2022-06-12 22:14:50.887424
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import boto3
    import botocore
    from botocore.exceptions import ClientError
    from ansible.module_utils.ansible_galaxy.api import GalaxyAPI

    if not (os.path.isfile('/tmp/offline_token.yml') or os.path.isfile('/tmp/offline_ticket.yml')):
        galaxy_api = GalaxyAPI('cloud.redhat.com')
        try:
            galaxy_api.login(username='cloud-services', password='cloud-services')
        except ClientError as e:
            if e.response['Error']['Code'] == 'IncompleteSignatureException':
                print('You need boto3 (or msrestazure) >= 1.4.6 to execute this test!')
                return
            else:
                raise

# Generated at 2022-06-12 22:14:56.165277
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # First test
    kt = KeycloakToken(auth_url='https://anyurl', access_token='any token')
    assert kt.get() == 'mock_token'

    # Second test
    kt.access_token = 'any token2'
    assert kt.get() == 'mock_token'

    # Third test
    kt._token = 'any token3'
    assert kt.get() == 'any token3'

# Generated at 2022-06-12 22:15:00.279034
# Unit test for method get of class KeycloakToken