

# Generated at 2022-06-12 22:05:16.239938
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create fake file for test
    import tempfile
    fd, path = tempfile.mkstemp()
    os.close(fd)
    config = {'token': 'value'}

    # Create the object to test
    galaxy_token = GalaxyToken()
    # Force the token file to the one created
    galaxy_token.b_file = path
    # Force the token value in the config
    galaxy_token._config = config

    # Run the code to test
    galaxy_token.save()

    # Open the fake file to check the result
    with open(path, 'r') as f:
        try:
            assert f.read() == 'token: %s\n' % config['token']
        except AssertionError:
            # Delete the file and raise the error
            os.remove(path)
            raise


# Generated at 2022-06-12 22:05:25.330723
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import httpretty
    from ansible.module_utils.urls import open_url

    filename = '%s/%s' % (os.path.dirname(os.path.realpath(__file__)), '../fixtures/KeycloakToken-get.json')
    with open(filename, 'r') as f:
        token = f.read()
        token_json = json.loads(token)

    httpretty.register_uri(httpretty.POST, 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')

    httpretty.enable()

# Generated at 2022-06-12 22:05:37.271108
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    ''' this method tests if the save method of the GalaxyToken class
        actually does what it is supposed to do.
    '''
    # create a new GalaxyToken object for testing purposes
    test_token = GalaxyToken()

    # get the test config from the built in test file
    test_config = test_token._read()

    # write the test config to the config file
    test_token.config = test_config
    test_token.save()

    # read the test config back from the config file
    token_file_config = test_token._read()

    # compare the test config and the config read back from the config file
    # ensure they are the same
    assert test_config == token_file_config

# testing _encode_token of GalaxyToken

# Generated at 2022-06-12 22:05:37.912126
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    pass
# s = GalaxyToken()
# s.save()



# Generated at 2022-06-12 22:05:47.730062
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class MockUrl(object):
        def __init__(self, response, code):
            self.code = code
            self.response = response

        def read(self):
            return self.response

    class MockOpenUrl(object):
        def __init__(self, data, code, error=None, **kwargs):
            self.data = data
            self.code = code
            self.error = error
            self.kwargs = kwargs

        def __call__(self, url, data=None, validate_certs=True, method='POST',
                     headers=None, http_agent=None):
            if data != self.data:
                return MockUrl('Error: wrong payload', 400)
            elif self.error:
                return MockUrl(self.error, self.code)
            else:
                return MockUrl

# Generated at 2022-06-12 22:05:59.620099
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:05.107416
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken(access_token=to_text('123'))
    assert keycloak_token.token_type == 'Bearer'
    assert keycloak_token.headers() == {'Authorization': 'Bearer 123'}


# Generated at 2022-06-12 22:06:08.771140
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    t = KeycloakToken(access_token='abc')
    assert t.get() == 'abc'

if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:06:19.718098
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:06:23.244492
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('foobar', auth_url='http://example.com/auth')
    assert token.headers() == {
        'Authorization': 'Bearer foobar',
    }


# Generated at 2022-06-12 22:06:35.853732
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    """
        This method tests the get method of the class KeycloakToken.
        It will extract the 'access_token' from the body of the response.
    """

# Generated at 2022-06-12 22:06:48.262056
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import sys
    import tempfile

    # create tempfile
    fd, tmpfile = tempfile.mkstemp()
    f = open(tmpfile, 'w')
    f.close()
    os.remove(tmpfile)

    # create a tempfile and populate it with some data
    with open(tmpfile, 'w') as config_file:
        config_file.write('# Ansible Galaxy configuration file\n')
        config_file.write('# This file should be in yaml format.\n')
        config_file.write('# If this file does not exist in the requested\n')
        config_file.write('# location, it is ignored.\n')
        config_file.write('#\n')

# Generated at 2022-06-12 22:07:00.720340
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:07:06.343848
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(None, None, False, None)
    token.access_token = 'abcdef'
    token.validate_certs = False
    token.auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
    token.client_id = 'cloud-services'
    token.get()
    assert token.get() == 'abcdef'


# Generated at 2022-06-12 22:07:11.332031
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = 'some-token'
    k = KeycloakToken(access_token=token)
    assert k.get(), 'get() is expected to return a token'
    assert k.get() == token, 'token is expected to be equal to `%s`' % token

# Generated at 2022-06-12 22:07:14.332420
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token='123', auth_url='https://foo.com/auth')
    assert token.get() == '123'


# Generated at 2022-06-12 22:07:20.433916
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    obj = KeycloakToken(auth_url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token",
                        access_token="mY3G3Jjm")
    headers = obj.headers()
    assert headers["Authorization"] == "Bearer mY3G3Jjm"


# Generated at 2022-06-12 22:07:27.908244
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    b_file = '.test_galaxy_token'
    data = {'key': 'value'}
    with open(b_file, 'w') as f:
        yaml_dump(data, f, default_flow_style=False)

    # Ensure we have write permissions
    os.remove(b_file)

    test_token = GalaxyToken()
    test_token.config['token'] = 'foo'
    test_token._config['key'] = 'value'
    test_token.save()

    # Verify the config was saved properly
    with open(b_file, 'r') as f:
        config = yaml_load(f)
    assert config == test_token.config
    os.remove(b_file)

# Generated at 2022-06-12 22:07:36.513795
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import requests
    import unittest.mock

# Generated at 2022-06-12 22:07:47.191268
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:08:03.284660
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    keycloak_token = KeycloakToken(access_token='abcd-1234', auth_url='https://sso.redhat.com/auth/realms/redhat-external')

    # need to mock return value of keycloak_token.get()
    keycloak_get = keycloak_token.get
    keycloak_token.get = lambda: 'efgh-5678'

    keycloak_headers = keycloak_token.headers()
    assert keycloak_headers.get('Authorization') == 'Bearer efgh-5678'

    # restore mocked keycloak_token.get()
    keycloak_token.get = keycloak_get

# Generated at 2022-06-12 22:08:12.115406
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create a token file
    token = 'abc'
    token_file = '/tmp/test_token.yml'
    try:
        tok = GalaxyToken()
        tok.set(to_text(token, errors='surrogate_or_strict'))
        tok.b_file = to_bytes(token_file, errors='surrogate_or_strict')
        tok.save()
        with open(tok.b_file, 'r') as f:
            config = yaml_load(f)
        assert config.get('token') == token
    finally:
        os.remove(token_file)


# Generated at 2022-06-12 22:08:16.172017
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    kcToken = KeycloakToken(auth_url='http://example.com', validate_certs=True, client_id='test-client')

    kcToken._token = "abc123"
    assert kcToken.headers() == {"Authorization": "Bearer abc123"}

# Generated at 2022-06-12 22:08:19.375148
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=True)
    config = {'token': '123456789'}
    t = GalaxyToken(token='123456789')
    assert config == t.config

# Generated at 2022-06-12 22:08:19.977896
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    pass

# Generated at 2022-06-12 22:08:28.209791
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    type = 'Token'
    token = 'foo'
    test_file = '/tmp/test_GalaxyToken'
    token_check = None

    with open(test_file, 'w') as outfile:
        outfile.close()

    galaxy_token = GalaxyToken()
    galaxy_token.set(token)

    with open(test_file, 'r') as infile:
        token_check = yaml_load(infile)

    if token_check is None:
        raise Exception("Write to yaml file failed")

    if type != (token_check.get('type')):
        raise Exception("Wrong type written to yaml file")

    if token != (token_check.get('token')):
        raise Exception("Wrong token written to yaml file")


# Generated at 2022-06-12 22:08:39.250956
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import tempfile
    import unittest

    from ansible.module_utils.urls import open_url

    class FakeResponse(object):
        def read(self):
            return response
    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.fail_json = self.fail

        def fail(self, msg):
            raise unittest.TestCase.failureException(msg)
    class FakeCommand(object):
        def __init__(self):
            self.module = FakeModule()

    token_type = 'Bearer'
    client_id = 'cloud-services'
    access_token = 'abcdef123456'
    auth_url = 'https://example.com/auth'

# Generated at 2022-06-12 22:08:46.177615
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # test we can set and save a GalaxyToken, and that it reads and verifies
    # the token stored in an ansible.cfg file.
    token_str = "some-token-str"
    token = GalaxyToken()

    # a new token should not have a token in it
    assert not token.get()

    # set the token and save it
    token.set(token_str)
    token.save()

    # now read the token back in and test the content
    token_read = GalaxyToken()
    assert token_read.get() == token_str


# Generated at 2022-06-12 22:08:53.003485
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    args = {}
    args['auth_url'] = "https://example.com"
    args['validate_certs'] = True
    args['client_id'] = 'client_id'
    args['access_token'] = "offline_token"
    token = KeycloakToken(**args)
    assert token.get() is not None

if __name__ == '__main__':
    test_KeycloakToken_get()

# Generated at 2022-06-12 22:08:56.598633
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    assert KeycloakToken(access_token='angrybird', auth_url='http://com').get() is not None
    assert KeycloakToken(access_token='angrybird', auth_url='http://com').get() == 'angrybird'

# Generated at 2022-06-12 22:09:07.659568
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(auth_url='https://auth.url.com', access_token='1234567890')
    token.get()
    assert token.headers() == {'Authorization': 'Bearer 1234567890'}

# Generated at 2022-06-12 22:09:10.270076
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    _token = "testtoken"
    _file = C.GALAXY_TOKEN_PATH

    # create token file
    token = GalaxyToken(_token)
    token.save()

    # check silent log
    f = open(_file, 'r')
    assert f.read() == "token: {}\n"
    f.close()



# Generated at 2022-06-12 22:09:16.740051
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:09:20.221039
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    k = KeycloakToken(access_token="12345", auth_url="http://auth_url")
    assert k.headers() == {'Authorization': 'Bearer None'}


# Generated at 2022-06-12 22:09:29.957399
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest
    import mock

    class TestKeycloakToken(unittest.TestCase):
        def setUp(self):
            self.access_token = '12345'
            self.url = 'http://some.url/some.endpoint'
            self.response = mock.MagicMock()
            self.error = 'some error'
            self.result = mock.MagicMock()
            self.result.read.return_value = json.dumps({'access_token': self.access_token})


# Generated at 2022-06-12 22:09:36.044742
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    test_token_text = 'xTEST123x'
    test_token = GalaxyToken(test_token_text)
    test_token.save()
    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        data = yaml_load(f)
        assert data['token'] == test_token_text
    os.remove(C.GALAXY_TOKEN_PATH)

# Generated at 2022-06-12 22:09:46.778272
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = '5b5f9db9-8dde-4d22-b4bf-fcb1c6745a5d'
    auth_url = 'https://someurl'
    client_id = 'cloud-services'
    validate_certs = False

    kct = KeycloakToken(access_token, auth_url, validate_certs, client_id)

    # - build a request to POST to auth_url
    #  - body is form encoded
    #    - 'request_token' is the offline token stored in ansible.cfg
    #    - 'grant_type' is 'refresh_token'
    #    - 'client_id' is 'cloud-services'
    #       - should probably be based on the contents of the
    #         offline_ticket's JWT payload 'aud' (

# Generated at 2022-06-12 22:09:55.253906
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    class TestUrl(object):
        def read(self):
            return '{"access_token": "testtoken"}'

    def test_open_url(url, data, validate_certs=True, method='GET', http_agent=None):
        return TestUrl()

    # Mock open_url with the test_open_url function
    GalaxyToken.open_url = staticmethod(test_open_url)

    # Initialize the Keycloak token
    token = KeycloakToken('valid_token', 'https://www.example.com')

    # Test request to Keycloak for access_token
    assert token.get() == 'testtoken'


# Generated at 2022-06-12 22:09:57.471744
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token='abcdefg')
    assert token.headers() == {'Authorization': 'Bearer abcdefg'}


# Generated at 2022-06-12 22:09:59.493216
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    k = KeycloakToken('foo')
    assert k.get() == 'foo'

# Generated at 2022-06-12 22:10:19.106308
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:10:26.604529
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import unittest

    class MockResponse(object):
        def __init__(self, body):
            self._body = body

        def read(self):
            return self._body

    # test KeycloakToken._form_payload, access_token
    class TestKeycloakToken_get_00(unittest.TestCase):
        def test_get_access_token(self):
            auth_url = "https://anywhere"
            access_token = "aaaa-aaaa-aaaa"
            client_id="nemo"
            token = KeycloakToken(access_token=access_token, auth_url=auth_url, validate_certs=True, client_id=client_id)

# Generated at 2022-06-12 22:10:29.491338
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    tt = KeycloakToken('foo', auth_url='https://example.com')
    assert tt.headers() == {'Authorization': 'Bearer foo'}


# Generated at 2022-06-12 22:10:40.598903
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Test with a valid request
    token = KeycloakToken(access_token = 'valid_offline_token', auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    token.get()
    assert token._token
    assert token._token != 'valid_offline_token'

    # Test with an invalid request
    token = KeycloakToken(access_token = 'invalid_offline_token', auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token')
    token.get()
    assert token._token == None



# Generated at 2022-06-12 22:10:41.739449
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken('dummy')
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer None'



# Generated at 2022-06-12 22:10:52.402825
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:11:03.455579
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    print('\ntest_KeycloakToken_headers')
    auth_url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'

# Generated at 2022-06-12 22:11:07.812088
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    temp_path = tempfile.gettempdir()
    token = GalaxyToken()
    token.b_file = to_bytes(os.path.join(temp_path, '.ansible-galaxy.token'))
    token.set('my_token')
    token.save()
    token.config = None
    token.set(None)
    assert token.get() == 'my_token'

# Generated at 2022-06-12 22:11:11.861255
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    from ansible.galaxy.token import KeycloakToken
    token = KeycloakToken('12345')
    assert(token.get() is not None)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-12 22:11:24.044547
# Unit test for method headers of class KeycloakToken

# Generated at 2022-06-12 22:11:45.648695
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    from ansible.galaxy.token import GalaxyToken
    import os
    import json
    import shutil

    # Use a testing directory
    test_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_files')
    token_path = os.path.join(test_path, 'token_file.yaml')
    # Copy the test file in the test directory
    if not os.path.exists(test_path):
        os.mkdir(test_path)
    shutil.copyfile(C.GALAXY_TOKEN_PATH, token_path)
    # Create the token and set a token
    token = GalaxyToken()
    token.set('test_token')
    # Read the file

# Generated at 2022-06-12 22:11:47.510686
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken('foo', 'bar').get()
    assert token == 'foo'

# Generated at 2022-06-12 22:11:51.270694
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    # Passing in none
    token = KeycloakToken()
    assert token.get() == None

    token = KeycloakToken("this is access_token", "this is auth_url", "this is client_id")
    assert token.get() == None

# Generated at 2022-06-12 22:11:58.013709
# Unit test for method get of class KeycloakToken

# Generated at 2022-06-12 22:12:01.322007
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():

    # Initialise a GalaxyToken object
    token = GalaxyToken()

    # Store a token
    token.set('testtoken')

    # Set the token to None
    token._token = None

    # Call the `get` method
    token_value = token.get()

    # Check the returned value
    assert token_value == 'testtoken', 'Returned token does not match the token set into the object'

# Generated at 2022-06-12 22:12:07.701408
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    access_token = 'abcdefghijklmnopqrstuvwxyz'
    auth_url = 'https://sso.redhat.com/auth/realms/cloudservices/protocol/openid-connect/token'
    client_id='cloud-services'
    validate_certs=True
    test_token = KeycloakToken(access_token, auth_url, validate_certs, client_id)
    assert test_token.get() is not None

# Generated at 2022-06-12 22:12:15.306967
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import yaml
    from ansible.module_utils.common.yaml import yaml_load
    token = 'token'

    gt = GalaxyToken()
    assert gt.config == {}

    gt.config['token'] = token
    gt.save()

    with open(C.GALAXY_TOKEN_PATH, 'r') as f:
        config = yaml_load(f)
    assert config['token'] == token

# Generated at 2022-06-12 22:12:24.493804
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import mock
    import collections
    import requests

    testcase = {}
    testcase['description'] = ('Unit test for KeycloakToken.get()')
    testcase['request_url'] = ('https://sso.example.com/auth/realms/ansible/protocol/openid-connect/')
    testcase['request_payload'] = ('grant_type=refresh_token&client_id=cloud-services&refresh_token=offline_token')
    testcase['request_headers'] = {
        'User-Agent': 'ansible-galaxy/1.0',
        'Content-Type': 'text/plain'
    }
    testcase['keycloak_response_status'] = 200

# Generated at 2022-06-12 22:12:34.920804
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    # Create a test token file
    test_file = to_bytes(C.GALAXY_TOKEN_PATH, errors='surrogate_or_strict')
    open(test_file, 'w').close()
    os.chmod(test_file, S_IRUSR | S_IWUSR)
    # Test if token file has diplayed 'opened' or 'created'
    # at the end, but remove this to not confuse the display.vvv()
    # unit test
    token_file_out = str.split(str(display.display._output),'\n')[-2]
    assert 'Opened' in token_file_out or 'Created' in token_file_out
    # Check if the token file is a valid yaml file
    display.plug()
    test_token = GalaxyToken()


# Generated at 2022-06-12 22:12:39.481536
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    token = KeycloakToken(access_token="x")
    token.get()
    assert token.headers() == {'Authorization': 'Bearer x'}



# Generated at 2022-06-12 22:12:58.140266
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import mock
    mock_resp = mock.MagicMock(read=lambda: '{"access_token": "test_token"}')
    with mock.patch('ansible.galaxy.token.open_url', return_value=mock_resp):
        token = KeycloakToken(auth_url='http://somehost-dummy', access_token='test_access_token')
        result = token.get()
        assert result == 'test_token'


# Generated at 2022-06-12 22:13:10.602135
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import tempfile
    old_file = tempfile.NamedTemporaryFile()
    old_file.write(b'test: 123\nyaml: test\n')
    old_file.seek(0)

    # Create a token file and chmod it to avoid any permission issues
    new_file = tempfile.NamedTemporaryFile()
    new_file.write(b'test: 123\n')
    new_file.seek(0)

    os.chmod(new_file.name, S_IRUSR | S_IWUSR)  # owner has +rw

    C.GALAXY_TOKEN_PATH = new_file.name
    galaxy_token = GalaxyToken()
    galaxy_token.save()


# Generated at 2022-06-12 22:13:16.083741
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    keycloak_token = KeycloakToken(access_token = "refreshtoken", auth_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token")
    assert keycloak_token.get() == "Bearer"

# Generated at 2022-06-12 22:13:25.365056
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = None
    package_name = 'python'
    version = '3.7.3'
    galaxy_token_path = C.GALAXY_TOKEN_PATH
    galaxy_token_old_content = ''

    galaxy_token = GalaxyToken(token=token)
    galaxy_token.config.update({'token': token})
    galaxy_token.config.update({'packages': {package_name: {version: {} }}})

    with open(galaxy_token_path, 'r') as f:
        galaxy_token_old_content = f.read()

    galaxy_token.save()

    with open(galaxy_token_path, 'r') as f:
        galaxy_token_new_content = f.read()

    assert galaxy_token_new_content != galaxy_token_old_content

# Generated at 2022-06-12 22:13:29.413768
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    token = GalaxyToken("token")
    token.set("token_1")
    token.set("token_2")
    assert token.get() == "token_2"
    assert token.config['token'] == "token_2"

# Generated at 2022-06-12 22:13:38.498158
# Unit test for method save of class GalaxyToken
def test_GalaxyToken_save():
    import os
    import tempfile

    def _remove_file(f):
        if os.path.isfile(f):
            os.remove(f)
        if os.path.isdir(os.path.dirname(f)):
            os.rmdir(os.path.dirname(f))

    tmpdir = tempfile.mkdtemp()
    f = os.path.join(tmpdir, 'galaxy.yml')

# Generated at 2022-06-12 22:13:45.358913
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    token = KeycloakToken(access_token = 'test_access_token',
                          auth_url = 'https://test_auth_url/auth/realms/redhat-external/protocol/openid-connect/token')
    token.get()
    assert token._token == 'test_access_token'


# Generated at 2022-06-12 22:13:53.813390
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():

    test_token_type = 'Bearer'
    access_token = 'test_access_token'
    auth_url = 'https://test_auth_url'
    validate_certs = True
    client_id = 'test_client_id'

    test_token = KeycloakToken(access_token, auth_url, validate_certs, client_id)
    headers = test_token.headers()

    assert test_token_type == headers['Authorization'].split(' ')[0]

    token = headers['Authorization'].split(' ')[1]
    assert token == access_token + 'Failed to get token'

# Generated at 2022-06-12 22:14:03.416885
# Unit test for method headers of class KeycloakToken
def test_KeycloakToken_headers():
    """ Unit test for KeycloakToken headers method """

# Generated at 2022-06-12 22:14:15.334255
# Unit test for method get of class KeycloakToken
def test_KeycloakToken_get():
    import json
    import os

    import requests_mock

    test_auth_url = 'http://test.com/auth/realms/redhat-external/protocol/openid-connect/token'
    test_token = '1234567890ABCDEF'
    test_client_id = 'my-app'
    test_validate_certs = True

    with requests_mock.Mocker() as m:
        m.post(test_auth_url, json={'access_token': test_token})
        tok = KeycloakToken(access_token=test_token, auth_url=test_auth_url,
                            validate_certs=test_validate_certs, client_id=test_client_id)

        # test with no auth_url set
        token = tok.get()
       