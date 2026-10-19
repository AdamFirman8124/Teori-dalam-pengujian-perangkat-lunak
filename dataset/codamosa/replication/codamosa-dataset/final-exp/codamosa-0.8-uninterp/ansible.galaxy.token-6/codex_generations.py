

# Generated at 2022-06-12 22:05:16.714584
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    if not os.path.isdir("./test"):
        os.mkdir("./test")
    GALAXY_TOKEN_PATH = os.path.abspath("./test/test_galaxy_token")
    expected = {
        'token': 'aaaaa',
    }

    test_gt = GalaxyToken()
    test_gt.b_file = to_bytes(GALAXY_TOKEN_PATH, errors='surrogate_or_strict')
    # check the initial state
    assert os.path.isfile("./test/test_galaxy_token") == False
    token = test_gt.get()
    assert token == None

    # test the save method by setting a token
    test_gt.set("aaaaa")
    token = test_gt.get()

# Generated at 2022-06-12 22:05:24.374441
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # define test data
    access_token = "1234567890"
    auth_url = "https://sso.example.com/auth/realms/master/protocol/openid-connect/token"
    validate_certs = True
    client_id = "cloud-services"

    # instantiate the object
    test_object = KeycloakToken(access_token, auth_url, validate_certs, client_id)

    # execute the function under test
    response = test_object.get()

    # assert that the function under test returned the expected value
    assert response == "1234567890"



# Generated at 2022-06-12 22:05:37.119710
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:05:47.165851
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''
    Make sure we can fetch a token from the offline token grant
    '''
    token = GalaxyToken(token=NoTokenSentinel())
    resp = None

# Generated at 2022-06-12 22:05:59.281534
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.module_utils.six import StringIO
    import tempfile
    import os

    test_data = dict(
        token="abcd-1234-efgh-5678",
        expiration='2017-04-28T15:55:55.886035Z',
    )

    fd, path = tempfile.mkstemp()
    os.close(fd)
    f = open(path, 'w+')

    try:
        g = GalaxyToken(token=test_data['token'])

        # Write the file
        g.save()

        # Now re-read and make sure the saved data is same
        f.seek(0)
        data = yaml_load(f)
        assert data == test_data
    finally:
        f.close()
        os.remove(path)

# Generated at 2022-06-12 22:06:12.326030
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Check that non-dict config is not allowed
    b_file = to_bytes(C.GALAXY_TOKEN_PATH, errors='surrogate_or_strict')
    with open(b_file, 'w') as f:
        yaml_dump('bad_value', f, default_flow_style=False)
    token = GalaxyToken()
    assert token._read() == {}

    # Check that the config file is re-read on each call to config
    token._config = {'token': 'new_value'}
    assert token.config['token'] == 'new_value'
    assert token._config is not None

    # Check the save method saves as expected
    token.set('new_value')

# Generated at 2022-06-12 22:06:22.009619
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:32.208823
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    mock_resp = "MockedResponse"
    mock_data = {'access_token': '12345'}
    mock_open = mock.mock_open(read_data=json.dumps(mock_data))
    kct = KeycloakToken()

    # Test case when access_token is set
    with mock.patch.object(kct, '_form_payload', return_value='payload_string') as mock_payload:
        with mock.patch('ansible.module_utils.urls.open_url', new=mock_open) as mock_request:
            assert kct.get() == mock_data['access_token']
            mock_payload.assert_called_once()

# Generated at 2022-06-12 22:06:36.269663
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    mock_token = KeycloakToken(access_token='mock_fenris_token', auth_url=None, validate_certs=True)
    mock_access_token = mock_token.get()
    assert(mock_access_token == 'mock_fenris_token')

# Generated at 2022-06-12 22:06:48.642808
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # TODO: Replace mock with python3 unittest.mock
    import mock
    mock_open_url = mock.Mock()
    mock_open_url.side_effect = Exception("Unexpected call to mock_open_url")
    with mock.patch('ansible.module_utils.urls.open_url', new=mock_open_url) as mock_open_url:
        kc_token = KeycloakToken(access_token='abc123')
        kc_token.get()
        args, kwargs = mock_open_url.call_args
        assert(len(args) > 0)
        assert(args[0] == to_native(kc_token.auth_url))
        payload = kc_token._form_payload()
        assert(args[3] == 'POST')


# Generated at 2022-06-12 22:06:58.269926
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Given a KeycloakToken
    auth = KeycloakToken()

    # When the method get is called
    result = auth.get()

    # Then it should return None
    assert result is None



# Generated at 2022-06-12 22:07:07.439422
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_auth_url = "https://realm.example.com/auth/realms/ansible/protocol/openid-connect/token"
    test_token = "123456789"

    test_client_id = "ansible-galaxy"
    test_payload = "grant_type=refresh_token&client_id=%s&refresh_token=%s" % (test_client_id, test_token)


# Generated at 2022-06-12 22:07:19.960751
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'hjkfgi4ew4.253423dsfds.23sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdf'
    auth_url = 'http://example.com'
    validate_certs = True
    client_id = 'test_client'
    expected_headers = {'Authorization': 'Bearer ' + access_token}
    token = KeycloakToken(access_token=access_token,
                          auth_url=auth_url,
                          validate_certs=validate_certs,
                          client_id=client_id)
    assert token.get() == access_token
    assert token.headers() == expected_headers

# Generated at 2022-06-12 22:07:27.108767
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    os.environ['GALAXY_TOKEN_PATH'] = "/tmp/test_tocken.yml"
    tocken = GalaxyToken()
    tocken.config['token'] = 'test_tocken'
    tocken.save()
    assert '' == open("/tmp/test_tocken.yml", "r").read().strip()
    assert 'test_tocken' == yaml_load(open("/tmp/test_tocken.yml", "r")).get('token')


if __name__ == "__main__":
    # Unit test for class GalaxyToken
    test_GalaxyToken_save()

# Generated at 2022-06-12 22:07:31.135895
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kt = KeycloakToken(auth_url='https://auth.example.com/realms/master/protocol/openid-connect/token',
                       access_token='abcdef')
    assert kt.headers() == {'Authorization': 'Bearer abcdef'}



# Generated at 2022-06-12 22:07:37.575384
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Unit test for method save of class GalaxyToken
    #
    # Create the token file
    token = GalaxyToken()
    token.config['token'] = "123"

    # Save the token file
    token.save()

    # Verify the token file was saved
    assert(os.path.isfile(C.GALAXY_TOKEN_PATH))

# Generated at 2022-06-12 22:07:39.609441
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('test_access_token').get()
    assert token != None
    assert len(token) > 0


# Generated at 2022-06-12 22:07:44.928459
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    #
    # Testing case when a token is provided
    #
    test_KeycloakToken = KeycloakToken(access_token='sample_token')
    assert test_KeycloakToken.get() == 'sample_token'

    #
    # Testing case when no token is returned
    #
    fake_auth_url = "https://dummy_url.example.org"

# Generated at 2022-06-12 22:07:45.880497
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    pass


# Generated at 2022-06-12 22:07:50.779445
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = '12345'
    b_file = to_bytes('/tmp/my_token', errors='surrogate_or_strict')
    galaxy_token = GalaxyToken(token)
    galaxy_token.b_file = b_file
    galaxy_token.save()

    with open(b_file, 'r') as f:
        data = yaml_load(f)
    assert data['token'] == token
    os.remove(b_file)



# Generated at 2022-06-12 22:08:09.417190
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = "https://sso.redhat.com/auth/realms/ansible/protocol/openid-connect/token"

# Generated at 2022-06-12 22:08:19.599963
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Tests with a KeycloakToken object
    token = None
    token = KeycloakToken()
    assert token.token_type == 'Bearer'
    assert token.headers() == {}
    token = KeycloakToken(access_token='abc')
    assert token.token_type == 'Bearer'
    assert token.headers()['Authorization'] == 'Bearer abc'
    # Tests with a GalaxyToken object
    token = None
    token = GalaxyToken()
    assert token.token_type == 'Token'
    assert token.headers() == {}
    token = GalaxyToken(token='abc')
    assert token.token_type == 'Token'
    assert token.headers()['Authorization'] == 'Token abc'
    # Tests with a BasicAuthToken object
    token = None
    token = BasicAuthToken()
   

# Generated at 2022-06-12 22:08:23.078866
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken(access_token="foo", auth_url="bar", validate_certs=False, client_id="baz")
    resp = keycloak_token.headers()
    assert resp == {'Authorization': 'Bearer None'}

# Generated at 2022-06-12 22:08:34.236313
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token = 'eyJhbGciOiJIUzI1NiJ9.eyJ2YWxpZCI6dHJ1ZSwiaXNzIjoiYW5zaWJsZSJ9.9ocFGZJ8bGiDdttbkHJMGyG17HLUgW6UxT6TkT_BXl0'
    test_token_file = './test_token'
    test_token_path = b'./test_token'
    display.verbosity = 4

    old_galaxy_token_path = C.GALAXY_TOKEN_PATH
    C.GALAXY_TOKEN_PATH = test_token_file
    token = GalaxyToken()
    token.set(test_token)
    token.save()
    C.G

# Generated at 2022-06-12 22:08:44.346018
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    """
    Tests GalaxyToken.save to ensure the data is written to disk
    """
    import tempfile


# Generated at 2022-06-12 22:08:55.885284
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class TestResp(object):

        def __init__(self, body, headers={}):
            self.body = body
            self.headers = headers

        def read(self):
            if isinstance(self.body, bytes):
                return self.body
            return self.body.encode('utf-8', 'surrogateescape')

    class TestOpen(object):

        def __init__(self):
            self.requests_made = []

        def request(self, method, url, data, headers, validate_certs, http_agent):
            req = {'method': method,
                   'url': url,
                   'data': data,
                   'headers': headers,
                   'validate_certs': validate_certs,
                   'http_agent': http_agent}

# Generated at 2022-06-12 22:09:00.654367
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    for token_type in ['Bearer', 'Token', 'Basic']:

        class TestToken:
            token_type = token_type
            def __init__(self, token=None):
                self._token = token
            def get(self):
                return self._token

        token = TestToken('foo')

        result = token.headers()

        if token_type == 'Bearer':
            assert 'Authorization' not in result and result == {}, ('FAIL: ' + str(result))
        else:
            assert 'Authorization' in result and result['Authorization'] == token_type + ' foo', ('FAIL: ' + str(result))

# Generated at 2022-06-12 22:09:05.697969
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    k = KeycloakToken(None)
    headers = k.headers()
    assert 'Authorization' in headers
    assert 'Bearer ' == headers['Authorization'][0:7]


# Generated at 2022-06-12 22:09:19.061091
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    url = "https://cloud.redhat.com/api"

# Generated at 2022-06-12 22:09:29.354646
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken(access_token='foobar', auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')

# Generated at 2022-06-12 22:09:50.701904
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    """Ensure that the Galaxy token file is read properly.
    The token file is expected to be YAML, and thus can contain junk around the token
    """
    # Create a fake ansible.cfg file
    b_file = to_bytes('/tmp/fake_token.yml', errors='surrogate_or_strict')
    open(b_file, 'w').close()
    os.chmod(b_file, S_IRUSR | S_IWUSR)  # owner has +rw

    galaxy_token = GalaxyToken()

    with open(b_file, 'a') as f:
        f.write('token: "fake_token"')

    # Should always return fake_token
    assert galaxy_token.get() == 'fake_token'

    galaxy_token.set('new_token')

# Generated at 2022-06-12 22:09:59.836147
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():

    gt = GalaxyToken()
    token_file = gt.b_file
    assert not gt._read()
    # No token in no token file
    assert not gt.get()
    assert not gt.config.get('token')
    # Set token
    gt.set('new_token')
    assert gt.get() == 'new_token'
    # Check token file
    assert gt._read().get('token') == 'new_token'
    # Check token is in token file
    with open(token_file, 'r') as f:
        assert yaml_load(f).get('token') == 'new_token'
    # Remove token
    gt.set(None)
    assert not gt.get()
    # Check token file
    assert not gt._read()
    # Clean

# Generated at 2022-06-12 22:10:06.552807
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    try:
        token_file = os.path.join(tmp_dir, 'test_galaxy_token')
        token = GalaxyToken(token_file)
        expected_token = "abc1234"
        token.set(expected_token)

        # Ensure new file is created
        assert os.path.isfile(token_file)

        # Ensure file contains expected token
        actual_token = token.get()
        assert actual_token == expected_token
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

# Generated at 2022-06-12 22:10:11.199814
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # No token defined
    k = KeycloakToken()
    assert k.headers() == {}

    # Token defined
    k = KeycloakToken('foo')
    assert 'Authorization' in k.headers()
    assert k.headers()['Authorization'] == 'Bearer foo'

# Generated at 2022-06-12 22:10:14.455502
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken("abcdefghij")
    assert token.headers()["Authorization"] == "Bearer %s" % token.access_token

# Generated at 2022-06-12 22:10:16.428616
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='123456')
    assert(token.get() == '123456')

# Generated at 2022-06-12 22:10:25.767259
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:10:30.859154
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('mYt0ken','https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    headers = token.headers()
    assert headers == {'Authorization': 'Bearer mYt0ken'}, "Headers do not match"

# Generated at 2022-06-12 22:10:43.337665
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import pdb; pdb.set_trace()

# Generated at 2022-06-12 22:10:53.786750
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''unit test for method save of class GalaxyToken'''
    test_filename = '.ansible_galaxy.test'
    token_file_path = os.path.join(C.DEFAULT_LOCAL_TMP, test_filename)
    test_token = GalaxyToken(token_file_path)

    # test: config is empty
    assert test_token.config == {}

    # test: token is empty
    assert test_token.get() is None

    # test: save empty token to file
    test_token.save()
    with open(token_file_path, 'w') as token_file:
        empty_token = yaml_load(token_file)
    assert empty_token == {'token': None}

    # test: config is not empty
    assert test_token.config != {}
    os.remove

# Generated at 2022-06-12 22:11:08.925354
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='dummy access token', auth_url='https://dummy_url.com')
    assert token.headers() == {'Authorization': 'Bearer '}



# Generated at 2022-06-12 22:11:21.308921
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # test if the file is created
    gt = GalaxyToken()
    fname = to_text(C.GALAXY_TOKEN_PATH)
    # delete the galaxy token file if exists
    if os.path.isfile(fname):
        os.remove(fname)
    assert not os.path.isfile(fname)
    # save to create galaxy token file
    gt.save()
    assert os.path.isfile(fname)
    # save again to check the content of token file
    gt.set('test_token')
    gt.save()
    assert os.path.isfile(fname)
    assert gt.get() == 'test_token'

    # test if the file is readable
    os.chmod(fname, 0)

# Generated at 2022-06-12 22:11:26.510930
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    """Unit test to test headers method of class KeycloakToken"""
    myclass = KeycloakToken(access_token='here is the access token')
    assert myclass.headers() == {'Authorization': 'Bearer None'}
    myclass._token = 'here is the token'
    assert myclass.headers() == {'Authorization': 'Bearer here is the token'}

# Generated at 2022-06-12 22:11:33.845742
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    '''Test the headers method of KeycloakToken class'''
    from ansible.module_utils.six import PY3

    fake_token = 'fake_token'
    fake_url = "https://auth.example.com/auth/realms/fake_realm/protocol/openid-connect/token"
    ktoken = KeycloakToken(access_token=fake_token, auth_url=fake_url)
    ktoken.token_type = "Fake"

    # First, check the Bearer token authentication
    headers = ktoken.headers()
    bearer_token = headers['Authorization']

    if PY3:
        assert bearer_token == "Fake fake_token", "The headers() method is not generating correct token type"

# Generated at 2022-06-12 22:11:47.308717
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.config.manager import ConfigManager

    config = ConfigManager(['ansible.cfg'])
    token = "243325.at.9sjdafkj34.424"
    galaxy_token = GalaxyToken(token)
    # Check to make sure the token was set correctly
    assert galaxy_token.get() is token

    # Check to make sure the new token is saved to the file
    galaxy_token.save()
    assert galaxy_token.config.get('token') == token
    with open(galaxy_token.b_file, 'r') as f:
        config = yaml_load(f)
        assert 'token' in config
        assert config['token'] == token

    # check to make sure the old token is removed

# Generated at 2022-06-12 22:11:53.924542
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token_file = "/tmp/test-token-file"

    # Write a token to the test file
    t = GalaxyToken()
    t.set("dummy-token")
    t.b_file = to_bytes(test_token_file, errors='surrogate_or_strict')
    t.save()

    # Read the token back in
    t = GalaxyToken()
    t.b_file = to_bytes(test_token_file, errors='surrogate_or_strict')
    assert t.get() == "dummy-token"

    # Remove the test file
    os.remove(test_token_file)

# Generated at 2022-06-12 22:12:02.332817
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Test with NoneToken
    # (from the default ansible.cfg)
    access_token = None
    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    validate_certs = True
    client_id = None
    test_token1 = KeycloakToken(access_token=access_token, auth_url=auth_url, validate_certs=validate_certs, client_id=client_id)
    assert test_token1.headers() =={}

    # Test with valid token
    # (from the default ansible.cfg)
    access_token = "ejreiojreoeioeee"

# Generated at 2022-06-12 22:12:06.704026
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token_instance = KeycloakToken(auth_url='http://example.com')
    assert token_instance.get() == token_instance._token
    token_instance._token = 'test_Get_Token'
    assert token_instance.get() == 'test_Get_Token'



# Generated at 2022-06-12 22:12:09.330122
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    url = 'https://redhat.com'
    token = '1234'
    kt = KeycloakToken(url, token)
    assert kt.get() == token


# Generated at 2022-06-12 22:12:15.113899
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='1t9JvQoQN_CbFyG3qENgYgiBhFxJEk-D')

# Generated at 2022-06-12 22:12:31.048380
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    galaxy_token = GalaxyToken(token=None)
    galaxy_token.save()

    assert os.path.isfile(galaxy_token.b_file) is True

# Generated at 2022-06-12 22:12:35.901626
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'foo'
    auth_url = 'http://localhost/auth/realms/redhat_rhmi/protocol/openid-connect/token'
    client_id = 'client_id'
    token = KeycloakToken(access_token=access_token, auth_url=auth_url, client_id=client_id)
    token.get()
    assert token._token == 'bar'



# Generated at 2022-06-12 22:12:41.860618
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    k = KeycloakToken(access_token='access_token', auth_url='auth_url')
    headers = k.headers()
    assert 'Authorization' == list(headers.keys())[0]
    assert 'Bearer access_token' == headers['Authorization']

# Generated at 2022-06-12 22:12:49.018215
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # create arguments for KeycloakToken.get
    # TODO update to test with more than one KeycloakToken.get
    auth_url = 'http://stubs/auth/realms/redhat-external/protocol/openid-connect/token'

# Generated at 2022-06-12 22:12:55.871395
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token_string = "test_GalaxyToken_save"
    token = GalaxyToken(token_string)
    token.save()
    with open(C.GALAXY_TOKEN_PATH, "r") as token_file:
        json_string = token_file.read()
        assert json_string == "{'token': '" + token_string + "'}"
        os.remove(C.GALAXY_TOKEN_PATH)


# Generated at 2022-06-12 22:12:58.896744
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    '''
    Ensure test_KeycloakToken_headers passes
    '''
    token = KeycloakToken(access_token='abc123')
    assert token.headers() == {'Authorization': 'Bearer abc123'}


# Generated at 2022-06-12 22:13:12.133478
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import os
    import sys
    import unittest
    import urllib3.exceptions
    import responses

    os.environ['ANSIBLE_DEBUG'] = '1'

    from ansible import context

    from ansible.module_utils.urls import open_url

    from ansible.parsing.vault import VaultLib

    # Mock the responses

# Generated at 2022-06-12 22:13:12.752693
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    pass

# Generated at 2022-06-12 22:13:23.671455
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    # - test defaults
    #  - all params not passed
    #  - 'access_token' and 'auth_url' are None

    kt = KeycloakToken()
    assert kt.get() == None

    # - test access_token
    #  - access_token passed but auth_url is None


# Generated at 2022-06-12 22:13:25.897247
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(auth_url='https://url', access_token='abcdef')
    assert token.get() == 'abcdef'

# Generated at 2022-06-12 22:13:50.319452
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    '''Unit tests for the galaxy token

    Should correctly validate behaviour for actions:
    - create a token file
    - write to a token file
    - read from a token file
    - fail reading from malformed token file
    '''
    import tempfile
    import shutil
    import os

    test_dir = tempfile.mkdtemp()
    test_file = os.path.join(test_dir, 'galaxy_token')

# Generated at 2022-06-12 22:13:54.750961
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

# Generated at 2022-06-12 22:14:03.508074
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:14:15.083174
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """ Basic unit test for method get of class KeycloakToken """
    kt = KeycloakToken(auth_url='https://auth.url.example.com')
    kt.access_token = 'these are not the droids you are looking for'
    kt._token = None
    payload = kt._form_payload()
    assert payload == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=these are not the droids you are looking for', \
        "Payload created by KeycloakToken.get() not formed correctly"

    # Validate that the auth URL contains the right info
    assert kt.auth_url == 'https://auth.url.example.com', \
        "auth_url not stored correctly"

# Generated at 2022-06-12 22:14:17.009984
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'foo'
    auth_url = 'https://www.example.com'
    token_object = KeycloakToken(access_token=access_token, auth_url=auth_url)
    assert token_object.get() == 'bar'


# Generated at 2022-06-12 22:14:27.665748
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:14:39.971316
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests
    import requests_mock
    import mock
    from ansible.galaxy.token import KeycloakToken

    # test refresh token that is None
    token = KeycloakToken(access_token=None, auth_url='http://auth.example.com')
    assert token is not None
    assert token.get() is None

    # test refresh token that is empty string
    token = KeycloakToken(access_token='', auth_url='http://auth.example.com')
    assert token is not None
    assert token.get() is None

    # test refresh token that is invalid string
    token = KeycloakToken(access_token='1234567890', auth_url='http://auth.example.com')
    assert token is not None
    assert token.get() is None

    # test with a valid refresh token that

# Generated at 2022-06-12 22:14:52.122913
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='1', auth_url='https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')

# Generated at 2022-06-12 22:15:00.287443
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import sys, os
    import ansible.module_utils.ansible_galaxy
    import ansible.module_utils.ansible_galaxy.api

    # Locate the real config file
    conf_file = ansible.module_utils.ansible_galaxy.GALAXY_ROOT
    conf_file = os.path.join(conf_file, ansible.module_utils.ansible_galaxy.GALAXY_CONF)
    if not os.path.isfile(conf_file):
        sys.stderr.write("Ansible Galaxy config file '%s' does not exist\n" % conf_file)
        sys.exit(-1)

    # Load the config file
    with open(conf_file, 'r') as f:
        conf = yaml_load(f)
        api

# Generated at 2022-06-12 22:15:08.169106
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    token = KeycloakToken(access_token='test_access_token', auth_url='https://dummy_url/token')

    # Test _form_payload method that is used in get method
    payload = token._form_payload()
    assert payload == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=test_access_token'

    # Test get method
    token.get()