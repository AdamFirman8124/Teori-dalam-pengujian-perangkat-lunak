

# Generated at 2022-06-12 22:05:17.225362
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """ Unit test for method get of class KeycloakToken
    """

# Generated at 2022-06-12 22:05:20.790283
# Unit test for constructor of class KeycloakToken
def test_KeycloakToken():
    assert KeycloakToken(None, None)
    assert KeycloakToken(None, 'a_url')
    assert KeycloakToken('a_token', 'a_url')


# Generated at 2022-06-12 22:05:24.526558
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # This causes the method headers from class KeycloakToken to be called
    # The method returns a dictionary, so the test will pass
    kt = KeycloakToken(access_token='', auth_url='', validate_certs=True, client_id='')
    kt.headers()

# Generated at 2022-06-12 22:05:37.271017
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    fake_token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3aWxsaWFtLm1hb' \
                'GVyQGdtYWlsLmNvbSIsImlhdCI6MTQ2NjgwMzgyMiwiZXhwIjoxNDY2OTc2NjIyfQ.' \
                'yF0p8Nr5gqB5D-zxbZHWTIl8Bv2xo-Pd5BnwoJWg8v_5q5NKtDnZ1zRAg874vhxQOkkE' \
                'hW8CvwJ03pldacCd39A'


# Generated at 2022-06-12 22:05:44.583751
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    # Test case #1 when self._token is present
    local_token = KeycloakToken()
    local_token._token = "1"
    if local_token._token != local_token.get():
        raise Exception("Test case #1 failed!")

    # Test case #2 when self._token is not present and resp.read() returns invalid json
    local_token = KeycloakToken()
    local_token.open_url = lambda *args, **kwargs: FakeResponse(b'abcd')
    if not local_token.get():
        raise Exception("Test case #2 failed! expected exception not thrown")

    # Test case #3 when self._token is not present and resp.read() returns valid json
    local_token = KeycloakToken()
    local_token.open_url = lambda *args, **kwargs: FakeResponse

# Generated at 2022-06-12 22:05:49.475216
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    path = tempfile.mktemp()
    token = GalaxyToken({}, path)
    token.config['token'] = '12345'
    token.save()
    with open(path) as f:
        assert f.read() == 'token: \'12345\'\n'
    os.unlink(path)

# Generated at 2022-06-12 22:05:59.737442
# Unit test for constructor of class KeycloakToken
def test_KeycloakToken():
    # verify that the constructor instantiates with the proper defaults
    token = KeycloakToken()
    assert token.access_token is None
    assert token.auth_url is None
    assert token._token is None
    assert token.validate_certs is True

    # verify that the constructor instantiates with the proper values
    token = KeycloakToken(access_token='my_access_token', auth_url='https://example.com/auth', validate_certs=False)
    assert token.access_token == 'my_access_token'
    assert token.auth_url == 'https://example.com/auth'
    assert token._token is None
    assert token.validate_certs is False

# Generated at 2022-06-12 22:06:12.850582
# Unit test for constructor of class KeycloakToken

# Generated at 2022-06-12 22:06:15.028483
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    assert KeycloakToken(access_token="foo").get() == "foo"


# Generated at 2022-06-12 22:06:23.390682
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    file_name = '/tmp/ansible_galaxy_token_file'
    token = 'token'
    token_file = GalaxyToken(token)
    token_file.b_file = to_bytes(file_name, errors='surrogate_or_strict')
    token_file.save()
    b_token_file = to_bytes(token_file.b_file, errors='surrogate_or_strict')
    b_token = to_bytes(token, errors='surrogate_or_strict')
    f = open(b_token_file, 'r')
    file_content = f.read()
    if file_content:
        if b_token in file_content:
            os.remove(token_file.b_file)
            return True

# Generated at 2022-06-12 22:06:35.967446
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:40.836489
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kc = KeycloakToken(access_token='abcd')
    hdrs = kc.headers()
    assert 'Authorization' in hdrs
    assert hdrs['Authorization'].startswith('Bearer ')


# Generated at 2022-06-12 22:06:47.744768
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_token = KeycloakToken(access_token='mock_offline_token',
                               auth_url='mock_auth_url',
                               validate_certs=True,
                               client_id='mock_client_id')
    # access token not set
    assert test_token.get() is None
    # access token set
    test_token._token = 'mock_access_token'
    assert test_token.get() == 'mock_access_token'

# Generated at 2022-06-12 22:06:54.255270
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    client_id = 'cloud-services'
    token = KeycloakToken(access_token, auth_url, True, client_id)
    assert token.get() is not None

# Generated at 2022-06-12 22:07:01.659542
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import pytest
    test_token_class = KeycloakToken(
        access_token='test_access_token',
        auth_url='test_auth_url',
        validate_certs=True,
        client_id='test_client_id')
    test_payload = test_token_class._form_payload()
    assert test_payload == 'grant_type=refresh_token&client_id=test_client_id&refresh_token=test_access_token'

# Generated at 2022-06-12 22:07:09.818129
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
            return 'grant_type=refresh_token&client_id=%s&refresh_token=%s' % (self.client_id, self.access_token)


# Generated at 2022-06-12 22:07:15.559359
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    KCT_token = KeycloakToken('7872c5b5-5fe5-4b00-80d7-782aa2f2cff2')
    KCT_token.get()
    # TODO: Need to write unit tests to verify KCT_token.get() has correct response


# Generated at 2022-06-12 22:07:25.303255
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Create a KeycloakToken instance with an offline token
    kt_instance = KeycloakToken(access_token='<offline token>', auth_url='http://localhost:8080/auth/realms/test/protocol/openid-connect/token')

    # Mock the open_url method of the urls module to simulate the response from a Keycloak server.
    # The response contains an access token
    kt_instance_get = KeycloakToken(access_token='<offline token>', auth_url='http://localhost:8080/auth/realms/test/protocol/openid-connect/token')
    # Disable secure certificate validation.
    kt_instance_get.validate_certs = False
    kt_instance_get.get()

    # The _token attribute should not be None
    assert k

# Generated at 2022-06-12 22:07:35.115259
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile

    # valid test
    temp_dir = tempfile.gettempdir()
    test_token = GalaxyToken()
    test_token.b_file = os.path.join(temp_dir, "test_galaxy_token_file")
    test_token.config = {'default_output': 'json'}
    test_token.save()
    assert os.path.isfile(test_token.b_file)

    # invalid test
    temp_dir = tempfile.gettempdir()
    test_token = GalaxyToken()
    test_token.b_file = os.path.join(temp_dir, "test_galaxy_token_file")
    test_token.config = None
    test_token.save()
    assert os.path.isfile(test_token.b_file)




# Generated at 2022-06-12 22:07:45.562951
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import shutil
    global _context
    tmp = _context.scratch_path + '/token_file'
    token = GalaxyToken()
    token.b_file = tmp
    token._read()
    token.config['token'] = 'my-token'
    token.save()
    assert os.path.isfile(tmp)
    # token file should exist and have the right permissions
    assert os.stat(tmp).st_mode & 0o777 == 0o600
    # test that the content is what we expect
    with open(tmp, 'r') as f:
        config = yaml_load(f)
    assert config == token.config
    # remove tmp
    os.remove(tmp)
    # clean up
    shutil.rmtree(_context.scratch)

# Generated at 2022-06-12 22:08:01.322363
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:08:08.810285
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # prepare
    test_file = 'test.yaml'
    token = 'token'

    # execute
    galaxy_token = GalaxyToken(token=token)
    galaxy_token.save()

    # assert
    with open(galaxy_token.b_file, 'r') as f:
        result = yaml_load(f)

    # delete test.yaml
    os.remove(galaxy_token.b_file)

    assert result == {'token': token}



# Generated at 2022-06-12 22:08:17.162284
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.module_utils.urls import HttpClient
    from ansible.module_utils.six.moves.urllib.error import HTTPError

    kctoken = KeycloakToken(access_token='refreshtoken', auth_url='https://authurl.com')

    class MyClient(HttpClient):

        def get_url(self, *args, **kwargs):
            return None

        def open(self, *args, **kwargs):
            self.method = 'POST'
            self.body = kwargs['data']
            self.headers = kwargs['headers']
            return MyResponse()

    class MyResponse(object):

        def read(self):
            return '{"access_token": "accesstoken"}'

        def getcode(self):
            return 200

    MyClient.get

# Generated at 2022-06-12 22:08:19.883237
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
        fail_on_missing_ansible_vars = False
        token_class = GalaxyToken()
        token_class.save()
        token_class.set('test')
        token_class.save()

# Generated at 2022-06-12 22:08:22.314191
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="Abcd")
    assert token.headers() == {'Authorization': 'Bearer Abcd'}, "Token header mismatch"

# Generated at 2022-06-12 22:08:25.594507
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    cls = KeycloakToken()
    cls.get = lambda: 'abc'
    assert cls.headers() == {'Authorization': 'Bearer abc'}

if __name__ == '__main__':
    test_KeycloakToken_headers()

# Generated at 2022-06-12 22:08:35.933812
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests_mock
    import requests.exceptions
    with requests_mock.Mocker() as m:
        url = 'https://sso.redhat.com/auth/realms/redhat-internal/protocol/openid-connect/token'
        payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=abcdefghijk'
        m.post(url, text='{"access_token": "12345678901234567890"}')
        kc_token = KeycloakToken('abcdefghijk', auth_url=url)
        token = kc_token.get()
        assert token == '12345678901234567890'



# Generated at 2022-06-12 22:08:39.635675
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    class TestGalaxyToken(GalaxyToken):
        # Override GalaxyToken.save() to not write to file
        def save(self):
            pass

    token = TestGalaxyToken("")
    token.set("test-token")
    assert token.config == {"token":"test-token"}

# Generated at 2022-06-12 22:08:45.193270
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # Case 1
    token = KeycloakToken(access_token='abc123', auth_url='http://test.com')
    out = token.headers()
    assert out == {'Authorization': 'Bearer abc123'}
    assert token.token_type == 'Bearer'

    # Case 2
    token = KeycloakToken()
    out = token.headers()
    assert out == {'Authorization': 'Bearer None'}
    assert token.token_type == 'Bearer'

    # Case 3
    token = KeycloakToken(access_token='abc123', auth_url='http://test.com', client_id='redhat')
    out = token.headers()
    assert out == {'Authorization': 'Bearer abc123'}
    assert token.token_type == 'Bearer'



# Generated at 2022-06-12 22:08:52.047940
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    tok = KeycloakToken('abc')
    assert tok.headers() == {'Authorization': 'Bearer None'}
    tok.get()
    assert tok.headers() == {'Authorization': 'Bearer None'}
    tok._token = 'xyz'
    assert tok.headers() == {'Authorization': 'Bearer xyz'}


# Generated at 2022-06-12 22:09:39.768893
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'this-is-a-token'
    sso_url = 'https://sso-dev.redhat.com/auth'
    ktk = KeycloakToken(access_token=access_token,
                        auth_url=sso_url,
                        validate_certs=True,
                        client_id=None)
    auth = ktk.headers()
    assert auth['Authorization'] == 'Bearer %s' % access_token

# Generated at 2022-06-12 22:09:49.532821
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
    Checks KeycloakToken.get() returns the correct value for a good token.

    This unit test does the following:
    1. Creates object of class KeycloakToken
    2. Calls get() on the object created in step 1
    3. Confirms that the value returned from get() matches expected value
    """

# Generated at 2022-06-12 22:09:51.113995
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='test')
    assert token.get() == 'test'

# Generated at 2022-06-12 22:09:54.341151
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    headers = KeycloakToken(auth_url='https://sso.redhat.com/auth', access_token='test-access-token').headers()
    assert headers['Authorization'] == 'Bearer test-access-token'



# Generated at 2022-06-12 22:10:01.616416
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():

    tests = (
        # test-name, access_token, auth_url, validate_certs, client_id, access_token from response
        ("Simple", 'token', 'http://url', None, None, 'token=foo'),
        ("Ignore None client_id key", 'token', 'http://url', None, None, 'token=foo'),
        ("Verify client_id in post", 'token', 'http://url', None, 'client', 'token=foo'),
    )

    for test_name, access_token, auth_url, validate_certs, client_id, access_token_response in tests:
        # create mock KeycloakToken object
        kct = KeycloakToken(access_token, auth_url, validate_certs, client_id)

        # create class mock of open_url

# Generated at 2022-06-12 22:10:05.948969
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    """Test the headers method of KeycloakToken class

    This method is not covered by Ansible Galaxy integration tests because
    it is not a method of keycloak.KeycloakOAuth2.
    """
    test_token = KeycloakToken(access_token="some token", auth_url="https://someurl")
    expected = {'Authorization': 'Bearer some token'}
    assert test_token.headers() == expected

# Generated at 2022-06-12 22:10:16.181315
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(
        access_token=os.environ.get('KEYCLOAK_REFRESH_TOKEN', '<Undefined>'),
        auth_url=os.environ.get('KEYCLOAK_AUTH_URL', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    )
    token_data = token.get()
    if token_data:
        # Got a valid token, print it
        print(token_data)
    else:
        print('Failed to get a token: %s' % token)
        exit(1)

# Generated at 2022-06-12 22:10:25.550260
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'fkjasldkjfdlkjfldjfd'
    auth_url = 'https://example.com'
    validate_certs = True
    token = KeycloakToken(access_token, auth_url, validate_certs)

    expected_response = 'asdgdfsgsdfgdfbdfbsdg'
    test_data = '{"access_token":"%s"}' % expected_response
    class _Response:
        def __init__(self, test_data):
            self.read = lambda: test_data
    token._form_payload = lambda: ''
    token.open_url = lambda a, **kw: _Response(test_data)

    assert token.get() == expected_response

if __name__ == '__main__':
    test_KeycloakToken_

# Generated at 2022-06-12 22:10:30.007025
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:10:41.616247
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import shutil
    import tempfile
    temp_dir = tempfile.mkdtemp()
    C.GALAXY_TOKEN_PATH = os.path.join(temp_dir, 'ansible.cfg')
    test_galaxy_token = GalaxyToken('test_token')
    test_galaxy_token.config['token'] = 'test_token'
    test_galaxy_token.save()

    assert os.path.exists(test_galaxy_token.b_file)
    with open(test_galaxy_token.b_file, 'r') as myfile:
        data = myfile.read()
    assert data == "token: test_token\n"

    shutil.rmtree(temp_dir)

# Generated at 2022-06-12 22:10:48.839093
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:10:52.363327
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = None
    tk = KeycloakToken(token)
    assert(tk.headers()['Authorization'] == 'Bearer None')
    token = 'loremipsum'
    tk = KeycloakToken(token)
    assert(tk.headers()['Authorization'] == 'Bearer loremipsum')

# Generated at 2022-06-12 22:10:59.535868
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    gal_token = GalaxyToken()
    gal_token.config['foo'] = 'bar'
    gal_token.config['token'] = "I am a token"
    gal_token.config['baz'] = 'boo'

    gal_token.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)

    # Should contain what was saved
    assert gal_token.config['token'] == "I am a token"

# Generated at 2022-06-12 22:11:08.322073
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:20.664559
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:30.310225
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:43.330356
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:46.972098
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token="abc",
                          auth_url="https://auth.example.com",
                          validate_certs=True,
                          client_id="my-app")

    token.get()

# Generated at 2022-06-12 22:11:55.049420
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    '''
    @summary:
    This method unit test KeycloakToken.get() to make sure it returns a token
    @param:
    No input parameters
    @result
    This method will succeed if test passes
    '''

    # - build a request to POST to auth_url
    #  - body is form encoded
    #    - 'request_token' is the offline token stored in ansible.cfg
    #    - 'grant_type' is 'refresh_token'
    #    - 'client_id' is 'cloud-services'
    #       - should probably be based on the contents of the
    #         offline_ticket's JWT payload 'aud' (audience)
    #         or 'azp' (Authorized party - the party to which the ID Token was issued)


# Generated at 2022-06-12 22:11:59.611292
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = '1234567890abcdef'
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    kt = KeycloakToken(access_token=token, auth_url=auth_url)
    auth_token = kt.get()
    assert auth_token != token

# Generated at 2022-06-12 22:12:12.264852
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'

    # No offline_token
    token = KeycloakToken(username='foo', auth_url=auth_url)
    assert token.get() is None

    # There is an offline token, but it is not a JWT
    token = KeycloakToken(access_token='foo', auth_url=auth_url)
    assert token.get() is None

    # There is an offline token, and it is a JWT, but we can't decode it

# Generated at 2022-06-12 22:12:23.120949
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    TEST_DATA = '/tmp/test_KeycloakToken_get'
    url = 'https://default.com'
    refresh_token = 'foobar'
    valid_response = {u'access_token': 'abc123', u'token_type': u'bearer', u'expires_in': 86400,
                      u'refresh_expires_in': 172800, u'refresh_token': u'123abc', u'not-before-policy': 0,
                      u'session_state': u'8b457115-9827-4d65-b7c0-8e37b62cb2f1', u'scope': u'email profile'}
    invalid_response = {u'error': u'invalid_grant', u'error_description': u'Bad credentials'}

# Generated at 2022-06-12 22:12:33.177706
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    """Ensure that the GalaxyToken class can save a token file.

    For testing Ansible.

    """
    import tempfile
    import shutil
    import os

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    token_path = os.path.join(tmpdir, 'token')

    # Create a test GalaxyToken with custom path
    test_token = GalaxyToken()
    test_token.b_file = token_path

    # Write a token file to the temp path
    test_token.set('test_token')

    # Verify the file was written
    assert os.path.exists(token_path)

    # Remove the temporary directory
    shutil.rmtree(tmpdir)

# Generated at 2022-06-12 22:12:40.068237
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='my_token')
    assert token.headers() == {'Authorization': 'Bearer None'}
    assert token.headers() == {'Authorization': 'Bearer None'}
    token._token = 'auth_token'
    assert token.headers() == {'Authorization': 'Bearer auth_token'}



# Generated at 2022-06-12 22:12:44.071527
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken('fake_token')
    token.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)
    os.remove(C.GALAXY_TOKEN_PATH)


# Generated at 2022-06-12 22:12:48.567502
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken()
    token.save()
    test_file_path = C.GALAXY_TOKEN_PATH
    assert os.path.isfile(test_file_path)


# Generated at 2022-06-12 22:12:52.737691
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    galaxynode = GalaxyToken()
    galaxynode.config['token'] = "123456789"
    galaxynode.save()
    assert os.path.isfile(C.GALAXY_TOKEN_PATH)



# Generated at 2022-06-12 22:13:01.621900
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.utils.path import unfrackpath
    from tempfile import mkdtemp
    from shutil import rmtree
    from os.path import isdir, isfile
    from time import time

    # Create tmp dir
    tmpdir = mkdtemp(prefix='ansible-tmp-GalaxyToken')

    # Make sure we can't create a GalaxyToken object in the wrong place
    try:
        gt = GalaxyToken()
    except RuntimeError:
        pass
    else:
        assert False, 'GalaxyToken should throw when created outside of ANSIBLE_CONFIG'

    # Use with an alternate ANSIBLE_CONFIG
    save_ac = None

# Generated at 2022-06-12 22:13:05.730536
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    k = KeycloakToken(access_token=None, auth_url=None, validate_certs=True, client_id=None)
    print(k)


#########################################################################
#

# Generated at 2022-06-12 22:13:18.877325
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    # method being tested
    def test_headers(token):
        return json.dumps(token.headers())

    ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxx'
    AUTH_URL = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    VALIDATE_CERTS = True
    CLIENT_ID = 'cloud-services'

    # Test 1: Test get token
    keycloak_token = KeycloakToken(access_token=ACCESS_TOKEN, auth_url=AUTH_URL, validate_certs=VALIDATE_CERTS, client_id=CLIENT_ID)
    result = json.loads(test_headers(keycloak_token))
    assert result["Authorization"] == 'Bearer xxxxxxxxxxxxxxxxxxxxxxx'



# Generated at 2022-06-12 22:13:33.595709
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # create temporary file and call set with a value
    from tempfile import NamedTemporaryFile as tmpfile
    from shutil import copy

    # create temporary file
    with tmpfile(delete=False) as f:
        temp_file = f.name
    galaxy_token = GalaxyToken(None)
    galaxy_token.b_file = to_bytes(temp_file)

    # test - galaxy token file is created and token saved with save
    galaxy_token.set(b'test')
    assert os.path.isfile(temp_file) is True
    with open(temp_file, 'r') as f:
        saved_token = yaml_load(f)

    # check if file contains the token
    assert 'test' == saved_token.get('token')

    # test - if galaxy token file is missing new file is created and

# Generated at 2022-06-12 22:13:41.025589
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # path not exist
    token = 'token'
    test_file = 'test_file'
    t = GalaxyToken(token)
    t.b_file = to_bytes(test_file, errors='surrogate_or_strict')
    t.save()
    assert os.path.isfile(test_file)
    os.remove(test_file)
    # path exist, but content with errors
    token = 'token'
    test_file = 'test_file'
    with open(test_file, 'w') as f:
       f.write('abc')
    t = GalaxyToken(token)
    t.b_file = to_bytes(test_file, errors='surrogate_or_strict')
    t.save()
    assert os.path.isfile(test_file)
    os

# Generated at 2022-06-12 22:13:52.872222
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.module_utils.six.moves.builtins import open

    token_str = 'abcdefghijklmnop'
    test_file = to_text(os.path.expanduser('~/.ansible/tmp/galaxy_token'), errors='surrogate_or_strict')
    open(test_file, 'w').close()
    os.chmod(test_file, S_IRUSR | S_IWUSR)
    # Create GalaxyToken object
    galaxy_token = GalaxyToken(token=token_str)
    # Save token_str to test file
    galaxy_token.save()
    # Load token from test file
    with open(test_file, 'r') as f:
        loaded_token = yaml_load(f)
    # Validate loaded token
    assert loaded_

# Generated at 2022-06-12 22:14:02.796386
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    test_token = KeycloakToken('test_token', 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token', validate_certs=True)

# Generated at 2022-06-12 22:14:14.677602
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os.path
    import tempfile
    import shutil
    import json

    def create_config_file(config):
        (fd, path) = tempfile.mkstemp()
        with os.fdopen(fd, 'w') as f:
            json.dump(config, f)
        return path

    def test_save(config, expected_config_string):
        # create a config file
        path = create_config_file(config)
        token = GalaxyToken()
        token.b_file = to_bytes(path)

        # save new config
        token.save()

        # verify the new config
        with open(path) as f:
            new_config_string = f.read()
        assert new_config_string == expected_config_string

    # test config with no `token`
    test_

# Generated at 2022-06-12 22:14:25.487605
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    access_token = 'abcdefg'
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    validate_certs = True
    client_id = 'test'

    token = KeycloakToken(access_token, auth_url, validate_certs, client_id)

    # mock the getter for the token so we can assert the
    #  call to its get method
    old_token_getter = token.get
    def getter():
        old_token_getter()
        return access_token
    token.get = getter

    expected_headers = {'Authorization': 'Bearer %s' % access_token}
    assert token.headers() == expected_headers

# Generated at 2022-06-12 22:14:35.549576
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import os
    access_token = os.getenv('SSO_REFRESH_TOKEN')
    auth_url = os.getenv('SSO_AUTH_URL')
    client_id = os.getenv('SSO_CLIENT_ID')
    validate_certs = os.getenv('SSO_AUTH_VALIDATE_CERT', 'True') == 'True'

    token = KeycloakToken(access_token=access_token, auth_url=auth_url, validate_certs=validate_certs, client_id=client_id).get()
    print(token)

if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:14:38.764942
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token = 'foo')
    assert token.headers() == {'Authorization': 'Bearer None'}


# Generated at 2022-06-12 22:14:43.525154
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """ Test for method get of class KeycloakToken """
    key_cloak_token = KeycloakToken('aaabbbccc', 'url', True, 'client_id')
    key_cloak_token._form_payload()
    key_cloak_token.get()


# Generated at 2022-06-12 22:14:48.575408
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    expected = {'Authorization': 'Bearer test123'}
    auth_url = 'https://test.domain.com'

    token = 'test123'
    k_token = KeycloakToken(token, auth_url)

    assert(k_token.headers() == expected)


# Generated at 2022-06-12 22:15:00.412205
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:15:04.435341
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    galaxy_token = GalaxyToken()
    try:
        galaxy_token.set('1234567890')
        assert os.path.isfile(to_bytes(C.GALAXY_TOKEN_PATH))
    finally:
        # Clean up
        os.remove(to_bytes(C.GALAXY_TOKEN_PATH))