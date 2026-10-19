

# Generated at 2022-06-12 22:05:15.607536
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    username = 'gromit'
    password = 'wonttell'
    access_token = 'abcdefg12345'
    token_type = 'Bearer'
    client_id = 'cloud-services'
    auth_url = 'https://sso.redhat.com/auth/realms/ansible/protocol/openid-connect/token'
    kt = KeycloakToken(access_token=access_token, auth_url=auth_url, client_id=client_id)
    headers = kt.headers()

# Generated at 2022-06-12 22:05:19.548430
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken("test_token")
    token.get = lambda: "test_token"
    expected_result = {'Authorization': 'Bearer test_token'}
    assert token.headers() == expected_result


# Generated at 2022-06-12 22:05:26.753100
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''Test method get of class KeycloakToken

    :param cls:
    :return:
    '''
    import os
    from ansible.module_utils.urls import open_url

    auth_url = os.environ.get('AUTH_URL', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    client_id = os.environ.get('KATELLO_CLIENT_ID', 'cloud-services')
    username = os.environ.get('KATELLO_USERNAME')
    password = os.environ.get('KATELLO_PASSWORD')

    # build a request to POST to auth_url
    #  - body is form encoded
    #    - 'request_token' is the offline token

# Generated at 2022-06-12 22:05:32.635769
# Unit test for constructor of class KeycloakToken
def test_KeycloakToken():
    keycloak=KeycloakToken(access_token='abc')
    assert keycloak.access_token == 'abc'
    assert keycloak.auth_url is None
    assert keycloak.validate_certs == True
    assert keycloak.client_id == 'cloud-services'



# Generated at 2022-06-12 22:05:34.730345
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='token')
    assert token.get() == 'token'

# Generated at 2022-06-12 22:05:45.596592
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:05:58.290159
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import json
    import os
    import subprocess
    import tempfile
    import ansible

    token = KeycloakToken('offline_token_string')

    # Check that the token.get() method is called
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, 'token_file'), 'w') as f:
            f.write(json.dumps({
                'access_token': 'dummy_token',
                'expires_in': 3600,
                'refresh_expires_in': 1800,
                'refresh_token': 'dummy_refresh_token',
                'token_type': 'Bearer'
            }))
        token.auth_url = 'file://' + tmpdir
        # Need to re-instantiate because the stale instance

# Generated at 2022-06-12 22:06:04.554588
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:08.659022
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token="placeholder")
    test_data = {"access_token": "placeholder"}
    token.get = lambda : test_data["access_token"]
    assert token.get() == test_data["access_token"]

# Generated at 2022-06-12 22:06:18.244479
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os.path
    import os

    token = GalaxyToken()
    token.set(u'test_token')

    assert os.stat(C.GALAXY_TOKEN_PATH).st_mode & 0o700
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)

    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        config = yaml_load(f)

    assert isinstance(config, dict)
    assert config == {'api_server': None, 'token': u'test_token'}

    os.unlink(C.GALAXY_TOKEN_PATH)

# Generated at 2022-06-12 22:06:32.430687
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp(prefix='ansible_galaxy_test_')
    config_file_path = "%s/test_token" % temp_dir
    config_dict = {"a": 1, "b": "a string"}

    try:
        token = GalaxyToken()
        token._token = to_bytes(config_file_path, errors='surrogate_or_strict')
        token.config = config_dict

        assert token.config == config_dict
        token.save()

        with open(config_file_path, 'r') as f:
            assert f.read() == yaml_dump(config_dict, default_flow_style=False)
    finally:
        shutil.rmtree(temp_dir)

# Generated at 2022-06-12 22:06:45.088716
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests
    import responses
    import json

    t = KeycloakToken(access_token='offline_token', auth_url='https://hostname.domain/auth/realms/realm/protocol/openid-connect/token')

    # lxml.html.HtmlElement object

# Generated at 2022-06-12 22:06:52.992009
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:00.188310
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    token = 'dummy'
    gt.set(token)
    # We need to inject the config here because it will be None when testing
    gt._config = {'token': token}
    gt.save()
    gt2 = GalaxyToken()
    # Need to set token to None in order to read it from file again
    gt2._token = None
    assert token == gt2.get()


# Generated at 2022-06-12 22:07:05.982205
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'

# Generated at 2022-06-12 22:07:18.869753
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # test: get() is called the first time
    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

# Generated at 2022-06-12 22:07:20.619602
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    b = GalaxyToken(token='TEST')
    b.save()
    # TODO: use unittest

# Generated at 2022-06-12 22:07:27.861347
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kct = KeycloakToken(access_token="asdf")
    kct.get = lambda: "asdf"
    assert kct.headers() == {'Authorization': 'Bearer asdf'}
    kct = KeycloakToken(access_token="asdf", auth_url="https://auth.url.com")
    kct.get = lambda: False
    assert kct.headers() == {}


# Generated at 2022-06-12 22:07:35.292759
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as f:
        b_tempfile = to_bytes(f.name, errors='surrogate_or_strict')
        token_obj = GalaxyToken()
        token_obj.config['token'] = 'abc123'
        token_obj.b_file = b_tempfile
        token_obj.save()
        with open(b_tempfile, 'rb') as f2:
            data = f2.read()
    os.remove(b_tempfile)
    return data == b"token: abc123\n"


# Generated at 2022-06-12 22:07:46.086366
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:51.520964
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken()
    assert token.headers() == {'Authorization': 'Bearer None'}



# Generated at 2022-06-12 22:08:02.334860
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    config = {'token': '40b274c0c1f042e0dbba2b81b8aa88d2'}

    import tempfile
    b_token_file = to_bytes(tempfile.mktemp(suffix='_token'))
    token_file = to_text(b_token_file)

    g = GalaxyToken()
    g._config = config
    g.b_file = b_token_file
    g.save()

    with open(b_token_file, 'r') as f:
        data = f.read()

    assert data == 'token: 40b274c0c1f042e0dbba2b81b8aa88d2\n'

    os.unlink(token_file)

# Generated at 2022-06-12 22:08:11.695292
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    try:
        with open('/Users/zhaoyueying/Documents/GitHub/ansible-galaxy/test/test_data/keycloak_response.txt','r') as f:
            expected_token = f.read()
    except FileNotFoundError:
        return None

    # test_data/test_token
    kc_token = KeycloakToken(access_token='xxx',auth_url='https://auth.stage.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',validate_certs=False)

    kc_token._token = expected_token
    assert kc_token.get() == expected_token



# Generated at 2022-06-12 22:08:14.761820
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token="Zm9v", auth_url="http://localhost/auth/realms/ansible/protocol/openid-connect/token").get()
    assert token == 'Zm9v'


# Generated at 2022-06-12 22:08:20.954672
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    file_path = "test_GalaxyToken_save_file"
    try:
        GalaxyToken(token=NoTokenSentinel()).save(file_path=file_path)

        # Open file and read contents
        with open(file_path, 'r') as f:
            config = yaml_load(f)

        assert config == {}, "Failed reading in file after writing to it"
    finally:
        os.remove(file_path)

# Generated at 2022-06-12 22:08:25.335911
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url=None
    access_token=None
    validate_certs=True
    client_id=None
    keycloak = KeycloakToken(auth_url=auth_url, access_token=access_token,
        validate_certs=validate_certs, client_id=client_id)
    keycloak.get()



# Generated at 2022-06-12 22:08:34.456333
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Given a KeycloakToken that has a type_token and get method
    class keycloak_mock:
        token_type = 'Bearer'
        def get(self):
            return 'test_token_value'

    keycloak_mock_obj = keycloak_mock()
    # When headers is called
    headers = keycloak_mock_obj.headers()
    # Then its value is a dictionary with a single key and value
    assert len(headers) == 1
    assert headers['Authorization'] == 'Bearer test_token_value'



# Generated at 2022-06-12 22:08:38.034255
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="this_is_a_token")
    headers = token.headers()
    assert headers == {'Authorization': 'Bearer this_is_a_token'}


# Generated at 2022-06-12 22:08:39.437687
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.get()
    token.save()



# Generated at 2022-06-12 22:08:48.497255
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    """Asserts that GalaxyToken.save() writes the correct content to GALAXY_TOKEN_PATH."""

    # Set the expected path and file content.
    galaxy_token_path = os.path.join(os.path.dirname(__file__), 'galaxy_token.yml')
    expected_content = {
            'token': '<redacted>'
    }

    # Create a new token file and set the token
    token = GalaxyToken()
    token.set(expected_content['token'])
    # Save the token
    token.b_file = galaxy_token_path
    token.save()

    # Read the token file
    with open(galaxy_token_path) as f:
        actual_content = yaml_load(f)

    assert expected_content == actual_content

# Generated at 2022-06-12 22:09:02.743430
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import responses
    from ansible.module_utils.six.moves.urllib.parse import parse_qs
    KEYCLOAK_REFRESH_TOKEN = 'jh8b3e4b4b4l4j4b4b4b4b4b4b4b4b4'
    KEYCLOAK_AUTH_URL = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    KEYCLOAK_USER = 'dummy'
    KEYCLOAK_PASSWORD = 'dummy'

    # mocked response of the token feed at https://galaxy.ansible.com/api/tokens/

# Generated at 2022-06-12 22:09:17.297292
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='token', auth_url='https://auth/realms/galaxy/protocol/openid-connect/token')
    assert token.client_id == 'cloud-services'

# Generated at 2022-06-12 22:09:26.832622
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    print("Inside test get method of KeycloakToken")
    # Store the tokens into variables.
    token = "abcd"
    # Create KeycloakToken object with access token.
    token_obj = KeycloakToken(access_token=token)
    # Assert the token is returned by get() method.
    assert(token == token_obj.get())

    # Reset token to None.
    token_obj._token = None
    # Assert that get() method returns None.
    assert(token_obj.get() == None)

    # Create KeycloakToken object without access token.
    token_obj = KeycloakToken()
    # Assert that get() method returns None.
    assert(token_obj.get() == None)


# Generated at 2022-06-12 22:09:38.762387
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'ZW50cmF3YWxtZXJuaW5n'
    kt = KeycloakToken(access_token=access_token,
                       auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token',
                       validate_certs=True,
                       client_id='cloud-services')
    auth_token = kt.get()
    assert isinstance(auth_token, str)

# Generated at 2022-06-12 22:09:40.903001
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="test token")
    assert token.headers() == {'Authorization': 'Bearer test token'}

# Generated at 2022-06-12 22:09:48.286673
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """Unit test for KeycloakToken.get."""
    print("test_KeycloakToken_get")

    # todo: we need a fake auth url that returns a static response
    #       the response will be json like '{"access_token": "fake_keycloak_token"}'
    auth_url = ""
    access_token = ""
    validate_certs = True

    token = KeycloakToken(access_token=access_token, auth_url=auth_url, validate_certs=validate_certs)
    print(token.get())

# Generated at 2022-06-12 22:09:53.597785
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Arrange
    args = {
        'access_token': '123456',
        'auth_url': 'http://keycloak.com/auth',
        'validate_certs': False,
        'client_id': 'myclientid'
    }
    kcToken = KeycloakToken(**args)

    # Act
    result = kcToken.get()

    # Assert
    assert result is not None

# Generated at 2022-06-12 22:09:56.850448
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken(None)
    display = Display()
    token.save()
    assert os.path.isfile(token.b_file)
    assert os.stat(token.b_file).st_mode == 33152
    assert token.config == {}

# Generated at 2022-06-12 22:10:03.110533
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Arrange
    url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token?refresh_token='

# Generated at 2022-06-12 22:10:07.284450
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    username = 'test_username'
    password = 'test_password'
    access_token = 'test_access_token'
    auth_url = 'test_auth_url'
    token = KeycloakToken(access_token, auth_url, True, username, password)

    # should get token
    token.get()



# Generated at 2022-06-12 22:10:22.177773
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.cloud.com/auth/realms/ansible/protocol/openid-connect/token'

# Generated at 2022-06-12 22:10:24.206604
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token = KeycloakToken('ABCD-1234')
    keycloak_token.get()

# Generated at 2022-06-12 22:10:26.688530
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc_token = KeycloakToken(access_token='some_token', auth_url='some_url')
    assert kc_token.headers() == {'Authorization': 'Bearer some_token'}


# Generated at 2022-06-12 22:10:27.896830
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken()

    assert k.get() == 'a'

# Generated at 2022-06-12 22:10:37.567813
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    client_id = 'cloud-services'
    access_token = '4c4b2e24-7cb1-4604-8a0d-b9ecf7c91f66'
    kc_token = KeycloakToken(access_token=access_token, auth_url=auth_url, client_id=client_id)
    kc_token_get = kc_token.get()
    assert(kc_token_get is not None)

# Generated at 2022-06-12 22:10:46.279020
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken(access_token='testing', auth_url='https://auth.url', validate_certs='True', client_id='cloud-services')
    resp = open_url(to_native(kct.auth_url),
                    data=kct._form_payload(),
                    validate_certs=True,
                    method='POST',
                    http_agent=user_agent())
    if resp:
        data = json.loads(to_text(resp.read(), errors='surrogate_or_strict'))
        assert data.get('access_token') is not None
    else:
        assert False, "Response is null. Test Failed."

# Generated at 2022-06-12 22:10:51.088765
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''
    Test that if no token is defined, it returns None.
    '''
    galaxyToken = KeycloakToken()
    assert galaxyToken.get() is None

    '''
    Test that if the keycloak token is empty, it returns None.
    '''
    galaxyToken = KeycloakToken(None)
    assert galaxyToken.get() is None


# Generated at 2022-06-12 22:11:01.902514
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:03.557676
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken('some_token', '/auth', False)
    kct.get()



# Generated at 2022-06-12 22:11:06.256978
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    galaxy_token = GalaxyToken()
    galaxy_token.config = {'token': 'test'}
    galaxy_token.save()
    with open(galaxy_token.b_file, 'r') as f:
        config = yaml_load(f)
    assert config['token'] == 'test'

# Generated at 2022-06-12 22:11:12.727835
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():  # noqa
    token = KeycloakToken(access_token='mytoken', auth_url='myauthurl')
    display.vvv(token.get())



# Generated at 2022-06-12 22:11:24.422283
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    client_id = 'cloud-services'

    # Test 1: The existence of an auth_url present should be a string
    access_token = 'e6ac8b7f-f6c1-4862-ae6f-076e3fc6e264'
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    c = KeycloakToken(access_token, auth_url)
    assert isinstance(c.get(), str), 'get() should return a string'

    # Test 2: The existence of an auth_url present should not be a string
    access_token = 'e6ac8b7f-f6c1-4862-ae6f-076e3fc6e264'

# Generated at 2022-06-12 22:11:26.177046
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    kct = KeycloakToken(access_token='moon_the_dog', auth_url='http://localhost', client_id='redhat_cloud')
    kct.get()

# Generated at 2022-06-12 22:11:28.490468
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token="testtoken", auth_url="http://auth.example.com")
    assert token.get() == "testtoken"

# Generated at 2022-06-12 22:11:30.047284
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token = GalaxyToken()
    test_token.set('test token')
    test_token.save()


# Generated at 2022-06-12 22:11:32.390859
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    testobj = KeycloakToken()
    testobj._token = None
    testobj._token = 'testtoken'
    assert testobj.get() == 'testtoken'


# Generated at 2022-06-12 22:11:40.719936
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test if the KeycloakToken get method works,
    # by printing the API access token obtained from the API server.
    kc = KeycloakToken(os.environ['ANSIBLE_GALAXY_API_TOKEN'],
                       auth_url=os.environ['ANSIBLE_GALAXY_API_TOKEN_URL'],
                       validate_certs=False)
    print(kc.get())

if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:11:51.627440
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """ Test that KeycloakToken.get() works """
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.urls import ConnectionError
    from ansible.module_utils.compat.urllib.parse import urlparse, urlunparse

    token = '69fea6e7-2c13-4391-aefc-d60f7b2422c8'
    auth_url = 'https://sso.cloud.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    client_id = 'cloud-services'

    #######################################################################
    #
    #  tests with a mocked web server
    #
    #######################################################################
    #
    #  BadURL


# Generated at 2022-06-12 22:11:59.491555
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    #create a sample access_token
    access_token = "2edcbfe1-e037-4637-b8a5-7c13e5d1e930"
    #create a sample auth_url
    auth_url = "https://sso.redhat.com/auth/realms/rh-cloudservices/protocol/openid-connect/token"
    #create a sample KeycloakToken object
    keycloak_token = KeycloakToken(access_token=access_token, auth_url=auth_url)
    #expect the access_token to be returned as the _token
    assert keycloak_token._token == access_token

# Generated at 2022-06-12 22:12:09.258527
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    if hasattr(os.path, 'exists'):
        # python2
        exists = os.path.exists
    else:
        # python3
        exists = os.path.isfile
    b_token_file = C.GALAXY_TOKEN_PATH
    token_file = to_text(b_token_file, errors='surrogate_or_strict')
    galaxy_token = GalaxyToken(token='faketoken')
    if exists(token_file):
        os.remove(token_file)
    galaxy_token.save()
    assert exists(token_file)
    with open(token_file, 'r') as f:
        config = yaml_load(f)
    assert config['token'] == 'faketoken'

# Generated at 2022-06-12 22:12:16.921824
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken(token='123123')
    token.save()
    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        result = yaml_load(f)
    assert result == {'token': '123123'}

# Generated at 2022-06-12 22:12:22.555926
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.set('12345')
    token.save()
    token_file = token.b_file
    assert os.path.isfile(token_file) is True
    with open(token_file) as f:
        assert f.read() == 'token: 12345\n'
    os.remove(token_file)
    assert os.path.isfile(token_file) is False


# Generated at 2022-06-12 22:12:33.942604
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Create test instance
    auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    token_id='5f5d5d5a-9f9f-1234-a8a8-5e5e5e5e5e5e'
    client_id='SomeClient'
    token=KeycloakToken(access_token=token_id, auth_url=auth_url, validate_certs=True, client_id=client_id)
    # Call method get
    token_id=token.get()
    # Assert results

# Generated at 2022-06-12 22:12:46.448613
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:12:49.863491
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_token = KeycloakToken(access_token='myaccess_token')
    assert auth_token.get() == 'myaccess_token'

# Generated at 2022-06-12 22:12:59.905710
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.urls import ConnectionError
    from ansible.module_utils.six.moves import mock
    from io import BytesIO

    token = KeycloakToken(access_token='access_token', auth_url='https://login.ansible.com')
    b_auth_url = to_bytes(token.auth_url, errors='surrogate_or_strict')

    def mock_open_url(url, data, validate_certs, method, http_agent):
        return BytesIO(b"{\"access_token\":\"access_token_response\"}")

    with mock.patch('ansible.module_utils.urls.open_url', mock_open_url):
        assert token

# Generated at 2022-06-12 22:13:13.121575
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import shutil
    def open_url_mock(url, data, validate_certs, method, http_agent):
        return open('/tmp/rhsm-output.json', 'r')
    open_url_bkup = open_url
    open_url = open_url_mock

    b_file = '/tmp/GALAXY_TOKEN_PATH'
    shutil.copy('/tmp/rhsm-output.json', b_file)

    access_token = 'RmVlY2VyIFRva2Vu'
    auth_url = 'https://auth.api.openshift.io/api/token/refresh'
    validate_certs = True
    client_id = 'cloud-services'

# Generated at 2022-06-12 22:13:23.960182
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:13:28.404747
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    '''
    Test KeycloakToken headers method
    '''
    a_token = KeycloakToken("foo", auth_url="https://example.com")
    header = a_token.headers()
    assert header.get('Authorization') == "Bearer foo"

# Generated at 2022-06-12 22:13:31.667057
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    import pytest
    kct = KeycloakToken(access_token="some_token")
    assert kct.headers() == {'Authorization': 'Bearer some_token'}


# Generated at 2022-06-12 22:13:43.446122
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken('fake')
    token.config['token'] = 'abc'
    token.save()

    path = os.path.join(C.DEFAULT_LOCAL_TMP, '.ansible')
    if not os.path.exists(path):
        os.mkdir(path)

    path = os.path.join(path, 'galaxy_token')
    with open(path, 'r') as file:
        assert file.read() == "token: abc"

# Generated at 2022-06-12 22:13:47.121630
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gt = GalaxyToken()
    gt.config['token'] = 'new_token'
    gt.save()
    assert(gt.get() == 'new_token')

# Generated at 2022-06-12 22:13:58.588339
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://apb-registry.cloud.example.com/auth/realms/apb/protocol/openid-connect/token'

# Generated at 2022-06-12 22:14:01.547435
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken('my_access_token')
    actual = kt.headers()
    assert actual == { 'Authorization': 'Bearer my_access_token' }

# Generated at 2022-06-12 22:14:13.467115
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    # test_KeycloakToken_get:
    #   test_KeycloakToken_get_good_refresh_token

    access_token = '0123456789-ABCDE-FGHIJ-abcdefghij-abcdefghij'
    auth_url = 'https://sso.cloud.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    validate_certs = True
    client_id = 'ansible-automation-service'
    token = KeycloakToken(access_token=access_token, auth_url=auth_url, validate_certs=validate_certs, client_id=client_id)

# Generated at 2022-06-12 22:14:14.489133
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    pass


# Generated at 2022-06-12 22:14:25.311215
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='test_token',
                          auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    result = token.get()

# Generated at 2022-06-12 22:14:31.078374
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    b_file = to_bytes(C.GALAXY_TOKEN_PATH, errors='surrogate_or_strict')
    open(b_file, 'w').close()
    os.chmod(b_file, S_IRUSR | S_IWUSR)  # owner has +rw
    token = GalaxyToken(token='this is a test token')
    token.save()
    token = GalaxyToken()
    token.set('this is a test token')
    assert token.get() == 'this is a test token'

# Generated at 2022-06-12 22:14:33.675522
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = 'keycloak_token'
    auth_url = 'some_url'
    client_id = 'my_client_id'
    kc = KeycloakToken(token, auth_url, validate_certs=True, client_id=client_id)
    # Run the unit test
    assert token == kc.get()

# Generated at 2022-06-12 22:14:42.665281
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token="refresh123token456")
    token.auth_url="https://auth.example.com/realms/foo/protocol/openid-connect/token"
    token.client_id="example-client"

# Generated at 2022-06-12 22:14:47.306660
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken()
    token.get()

# Generated at 2022-06-12 22:14:54.584232
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # test when not valid access_token
    access_token = 'invalid'
    auth_url = 'http://example.com'
    validate_certs = True
    client_id = 'test'
    # initialize the class
    keycloakTokenObj = KeycloakToken(access_token, auth_url, validate_certs, client_id)
    # test when not valid access_token
    _token = keycloakTokenObj.get()
    assert _token == None


# Generated at 2022-06-12 22:15:01.914799
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests_mock