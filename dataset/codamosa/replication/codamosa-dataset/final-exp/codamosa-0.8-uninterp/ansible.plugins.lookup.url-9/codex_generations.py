

# Generated at 2022-06-13 14:34:38.278725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test case execution
    print("Start test run")

# Generated at 2022-06-13 14:34:50.720504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["http://www.github.com"]
    validate_certs = True
    use_proxy = True
    username = "username"
    password = "password"
    force_basic_auth = False
    follow_redirects = "urllib2"
    use_gssapi = False
    unix_socket = ""
    ca_path = ""
    unredirected_headers = ""

# Generated at 2022-06-13 14:34:59.165512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = '''
    one
    two
    three
    '''

    # File not found
    lu = LookupModule()
    assert lu.run(['not_found']) == []

    # File found without split
    lu = LookupModule()
    assert lu.run(['test_file.txt'], {'split_lines': False}) == [data]

    # File found with split
    lu = LookupModule()
    assert lu.run(['test_file.txt']) == ['one', 'two', 'three']

    # File not found with split
    lu = LookupModule()
    assert lu.run(['not_found']) == []

# Generated at 2022-06-13 14:35:08.005832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['url1', 'url2']
    validate_certs = True
    use_proxy = True
    url_username = "username"
    url_password = "password"
    headers = {"header": "value"}
    force = True
    timeout = 30.0
    http_agent = "agent"
    follow_redirects = "urllib2"
    use_gssapi = True
    unix_socket = "/var/run/file-socket"
    ca_path = "/path/to/ca/cert"
    unredirected_headers = ["header1", "header2"]
    expected_response = "expected response"

# Generated at 2022-06-13 14:35:18.659554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil
    import tempfile
    from ansible.plugins.lookup.url import LookupModule
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import open_url
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)
    with open("test.txt", "w") as f:
        f.write("test")
    os.chdir(os.path.dirname(__file__))

    l = LookupModule()
    assert l.run(["test.txt"], variables={"ansible_lookup_url_force": True}, split_lines=False) == [u"test"]

# Generated at 2022-06-13 14:35:29.898529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    display = Display()

    from ansible.utils.path import unfrackpath
    from ansible.vars.reserved import DEFAULT_VAULT_ID_MATCH
    from ansible.parsing.vault import VaultLib

    terms = [unfrackpath('~/test1.txt')]
    vault_password = 'ansible'
    vault_secret_file = './test/ansible-vault/test_vault.txt'

    # create vault secret file
    vault = VaultLib([DEFAULT_VAULT_ID_MATCH], vault_password, None)
    with open(vault_secret_file, 'w+b') as secret_file:
        secret_file.write(vault.encrypt('pswd: 12345'))

    # create test file

# Generated at 2022-06-13 14:35:42.962436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Initialize the class object
    lookup_module = LookupModule()

    #Set options from vars
    lookup_module.set_options(var_options=dict(validate_certs=True,
                                               use_proxy=True,
                                               username='foo',
                                               password='bar',
                                               headers={'foo': 'bar'},
                                               force=True,
                                               timeout=30.0,
                                               http_agent='foo',
                                               force_basic_auth=True,
                                               follow_redirects='yes',
                                               unix_socket='/tmp/foo',
                                               ca_path='foo',
                                               unredirected_headers={}))

    #Call run method and test its return

# Generated at 2022-06-13 14:35:46.791021
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        'https://raw.githubusercontent.com/caoc/ansible-lookup-url/master/README.md'
    ]
    lookup.run(terms, variables={'ansible_lookup_url_agent': 'ansible'})

# Generated at 2022-06-13 14:35:59.976271
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with no urls
    lm = LookupModule()
    assert lookup_paths == lm._get_paths("/does/not/matter")
    assert lm._get_paths("/does/not/matter") == lookup_paths
    assert not lm.run([], {})
    # TODO: test with urls

    # test with terms
    terms = ['abc']
    cwd = '/root/ansible'
    lm = LookupModule()

# Generated at 2022-06-13 14:36:02.648607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_obj = LookupModule()
    terms = []
    variables = {}
    kwargs = {}
    LookupModule_obj.run(terms, variables=variables, **kwargs)

# Generated at 2022-06-13 14:36:23.716373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['https://github.com/test.keys']

# Generated at 2022-06-13 14:36:33.892628
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        'https://ansible.com/'
    ]

# Generated at 2022-06-13 14:36:36.961119
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options()


# Unit test class LookupModule
import unittest

# Generated at 2022-06-13 14:36:43.880822
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instance LookupModule
    lookup = LookupModule()
    # Expected result
    expected = ['https://github.com/ansible/ansible/commit/6d4e4dcaa6a19a4d4d3b96f42a58ee6b92473c42']
    # Return of method run
    result = lookup.run(['https://github.com/ansible/ansible/commit/6d4e4dcaa6a19a4d4d3b96f42a58ee6b92473c42'])
    assert result == expected


# Generated at 2022-06-13 14:36:56.309513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Iterate over test cases and generate tests on the fly
    """

    # Test case 1
    response = MockResponse()
    response.read.return_value = b'foo\nbar\nbaz'
    mock_open_url = Mock()
    mock_open_url.return_value = response
    lm = LookupModule()
    lm.set_options({'cache': False, 'force': True})
    lm.open_url = mock_open_url
    lm._display = MockDisplay()
    # The run method is protected, so we need to test it directly
    assert lm.run(['https://github.com/gremlin.keys']) == ['foo', 'bar', 'baz']

    # Test case 2
    response = MockResponse()

# Generated at 2022-06-13 14:37:07.792343
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = ['https://github.com/gremlin.keys', 'https://ip-ranges.amazonaws.com/ip-ranges.json']
    (ca_path, unix_socket, validate_certs) = ('/path/to/ca.pem', '/path/to/unix/socket.sock', False)

    # setup global env vars
    os.environ['ANSIBLE_LOOKUP_URL_FORCE'] = 'True'
    os.environ['ANSIBLE_LOOKUP_URL_TIMEOUT'] = '30'
    os.environ['ANSIBLE_LOOKUP_URL_AGENT'] = 'unit-test-user-agent'
    os.environ['ANSIBLE_LOOKUP_URL_UNIX_SOCKET'] = unix_socket

# Generated at 2022-06-13 14:37:16.795019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def open_url_side_effect(url, *args, **kwargs):
        # get file name from kwargs if it is there
        file_name = kwargs.get('file_name')
        # get env kwarg
        env = kwargs.get('env')
        # if file_name is not there, try getting it from env
        if file_name is None:
            file_name = env.get('ANSIBLE_LOOKUP_URL_FILE_NAME')
        # pass validation cert param
        if args[0]['validate_certs'] is False:
            raise SSLValidationError('something bad happened')
        # get user_agent var
        user_agent = env.get('ANSIBLE_LOOKUP_URL_AGENT', 'ansible-httpget')
        # raise HTTPError

# Generated at 2022-06-13 14:37:23.686931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert(module.run([['https://github.com/gremlin.keys']]) == module.run(['https://github.com/gremlin.keys']))
    assert(module.run([['https://github.com/gremlin.keys']]) != module.run(['https://github.com/no.such.keys']))
    return True

# Generated at 2022-06-13 14:37:32.698959
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import pytest
    import requests

    #--------------------------------------------------------
    # mock_open_url
    #--------------------------------------------------------
    def mock_open_url(url, *args, **kwargs):
      if url == 'url_exception':
        raise Exception('url_exception')
      elif url == 'http_exception':
        raise HTTPError('http_exception', 500, 'HTTP Error', {}, None)
      elif url == 'url_error':
        raise URLError('url_error')
      elif url == 'ssl_validation_error':
        raise SSLValidationError('ssl_validation_error')
      elif url == 'connection_error':
        raise ConnectionError('connection_error')


# Generated at 2022-06-13 14:37:38.104722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    terms = ['https://github.com/', 'https://www.google.com/']
    variables = None
    options = dict({'validate_certs': True, 'use_proxy': True, 'force': False,
                    'username': '', 'password': '', 'timeout': 10, 'http_agent': 'ansible-httpget',
                    'force_basic_auth': False, 'follow_redirects': 'urllib2', 'use_gssapi': False,
                    'unix_socket': '', 'ca_path': '', 'unredirected_headers': ''})
    lookup_obj = LookupModule()
    lookup_obj.set_options(var_options=variables, direct=options)

# Generated at 2022-06-13 14:37:51.924829
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(dict())
    terms = ["http://ip.jsontest.com/?callback=?"]
    assert lookup_module.run(terms, variables=None, **dict()) == [u'{\n   "ip": "171.78.112.51"\n}']

# Generated at 2022-06-13 14:38:01.406371
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Call run to invoke the method
    result = LookupModule().run(terms=['https://www.ansible.com/'])


# Generated at 2022-06-13 14:38:02.044214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:38:02.654834
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:38:12.494463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText as aun
    from collections import namedtuple

    terms = namedtuple("Terms", ['term'])

    my_test_term = terms("http://example.com")

    #setup mocks
    var_options = {"url": my_test_term}

    my_lookup_base = LookupModule()
    my_lookup_base.set_options = lambda x, y, z: var_options
    my_lookup_base.get_option = lambda x: var_options[x]
    my_lookup_base.get_option("url")

    assert my_lookup_base.run(terms="http://example.com") == [aun("\n")]



# Generated at 2022-06-13 14:38:20.563246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    if not hasattr(x, 'run'):
        # Old Ansible version
        pass
    else:
        y = x.run(["https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/module_utils/basic.py"], {})
        assert isinstance(y, list)
        assert len(y) == 100
        assert y[0] == "# (c) 2012-16, Michael DeHaan <michael.dehaan@gmail.com>"
        assert y[99] == "    def basic_response(module, msg, rc=None, err=None, debug=None, log=None, default=None):"

# Generated at 2022-06-13 14:38:31.957824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # content from https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/url.py

    # unit tests for class LookupModule
    # set up various objects
    # lookup = LookupModule()
    variable = "var"
    variable_value = "value"
    variable_dict = {
        variable: variable_value
    }
    variable_list = [
        variable, variable_value
    ]
    variable_terms = [
        variable,
        variable_value,
        variable_dict,
        variable_list
        ]

    url = "https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/url.py"

# Generated at 2022-06-13 14:38:41.008257
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test that dict is returned as expected
    url_output = [u'http://localhost:8080/', u'http://localhost:8080/health/', u'http://localhost:8080/docs/', u'http://localhost:8080/docs/index.html']
    lookup_module = LookupModule()
    lookup_module.set_options({'validate_certs': False, 'use_proxy': True, 'url_username': None, 'url_password': None, 'headers': {}, 'force': False, 'timeout': 10, 'http_agent': 'ansible-httpget', 'force_basic_auth': False, 'follow_redirects': 'urllib2', 'use_gssapi': False, 'unix_socket': None, 'ca_path': None, 'unredirected_headers': []})


# Generated at 2022-06-13 14:38:45.323454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    response = lookupModule.run(["https://github.com/ansible/ansible/raw/devel/lib/ansible/modules/cloud/amazon/ec2_ami_copy.py"])
    assert len(response) == 1

# Generated at 2022-06-13 14:38:54.283613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test with empty list
    terms = []
    assert [] == lookup.run(terms)

    # Test with a valid URL that returns a text
    terms = ['http://www.google.com']

# Generated at 2022-06-13 14:39:20.988247
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_instance = LookupModule()

    terms_input = ['https://github.com/gremlin.keys']

# Generated at 2022-06-13 14:39:30.008007
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import mock
    import ssl

    # When split_lines is False return the whole content
    class FakeResponse(object):
        def read(self):
            return b"some content\n"

    # When split_lines is true return an array of lines
    class FakeResponse2(object):
        def read(self):
            return b"some content\nwith lines"

    # When receiving a HTTPError
    class FakeResponseHTTPError(object):
        def read(self):
            logger.error("returned FakeResponseHTTPError")
            raise HTTPError("url", "code", "msg", "hdrs", "data")

    # When receiving a URLError
    class FakeResponseURLError(object):
        def read(self):
            logger.error("returned FakeResponseURLError")

# Generated at 2022-06-13 14:39:37.944830
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_value = "lookup_url"
    lookup_mock = LookupModule()
    lookup_mock.set_options(dict(validate_certs=True))
    lookup_mock.run_orig = LookupModule.run
    lookup_mock.run = lambda terms, variables=None, **kwargs: ["https://github.com/ansible/mazer", "https://github.com/ansible/mazer.keys", "https://github.com/ansible/mazer.keys"]
    assert test_value in lookup_mock.run([test_value])

# Generated at 2022-06-13 14:39:42.415113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._options = dict(username='someuser', password='somepass')
    terms = ['https://some.private.site.com/file.txt']
    lookup._templar = Template()
    result = lookup.run(terms=terms)
    assert result[0] == 'hello, world'

# Generated at 2022-06-13 14:39:49.921035
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock
    # Mock params
    term = 'https://github.com/gremlin.keys'

    # Initialize object
    LookupModule_instance = LookupModule()

    # Mock open_url response
    mock_response = mock.Mock()

# Generated at 2022-06-13 14:39:59.691865
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys
    import pytest
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves.urllib.error import URLError
    from ansible.module_utils.urls import ConnectionError

    # Create a fake file-like thing to stringIO to
    out = StringIO()
    err = StringIO()
    sys.stdout = out
    sys.stderr = err

    # These are the default args

# Generated at 2022-06-13 14:40:07.080206
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

# Generated at 2022-06-13 14:40:18.523537
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options({'_terms': ['https://github.com/gremlin.keys'],
                        'validate_certs': True, 'use_proxy': False, 'username': None, 'password': None,
                        'headers': {}, 'force': False, 'timeout': 10, 'http_agent': 'ansible-httpget',
                        'force_basic_auth': False, 'follow_redirects': 'urllib2', 'use_gssapi': False,
                        'unix_socket': None, 'ca_path': None, 'unredirected_headers': []})
    result = lookup.run()
    assert type(result) is list
    assert len(result) == 5

# Generated at 2022-06-13 14:40:23.026923
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import tempfile
    import time
    import os
    import random
    import shutil

    # Define the test cases
    class TestCase:
        def __init__(self, msg, terms, variables, expect):
            self.msg = msg
            self.terms = terms
            self.variables = variables
            self.expect = expect
    test_cases = []
    
    # Test case 1: Normal operation
    msg = "Standard URL lookup with one element in the list."
    terms = ["https://ip-ranges.amazonaws.com/ip-ranges.json"]
    variables = {}
    expect = [json.loads(open("ip-ranges.json").read())]
    test_cases.append(TestCase(msg, terms, variables, expect))
    
    # Test case 2: Standard operation

# Generated at 2022-06-13 14:40:25.691809
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    terms = ['http://example.com/some/file.json']
    # Test that run() returns correct data
    lu.run(terms, {'ansible_lookup_url_agent': 'test-agent'})

# Generated at 2022-06-13 14:41:09.521700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.urls import open_url
    from ansible.plugins.lookup import LookupModule
    import os
    import sys
    import pytest
    print('Unit test for method run of class LookupModule')
    print('PYTHONPATH:'+os.environ['PYTHONPATH'])
    print('sys.path:'+str(sys.path))
    lookup = LookupModule()
    lookup.set_options({'validate_certs':False, 'use_proxy':True})
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['https://test.com/test.txt'])

# Generated at 2022-06-13 14:41:18.370771
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_cases = []
    # test_case = term, wantlist, options, results
    test_case = (
        'https://www.ansible.com',
        True,
        {'validate_certs': True, 'split_lines': True},
        [
            "  <meta charset='utf-8'>",
        ],
    )
    test_cases.append(test_case)

    lookup_module = LookupModule()
    for terms, wantlist, options, results in test_cases:
        lookup_module.set_options(var_options=None, direct=options)
        assert lookup_module.run(terms, wantlist=wantlist) == results

# Generated at 2022-06-13 14:41:29.842720
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options=None, direct={'wantlist':True,'split_lines':False})
    t = 'https://github.com/gremlin.keys'
    r = l.run([t])

# Generated at 2022-06-13 14:41:40.345247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test LookupModule_run()

    :returns: (bool) test result
    """
    # Initialize test params
    terms = "https://github.com/gremlin.keys"

# Generated at 2022-06-13 14:41:53.232730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock open_url
    class MockOpenURL:
        def __init__(self, *args, **kwargs):
            pass
        def read(self):
            return "Test data from http://test.com/test.txt"
    old_open_url = LookupModule.open_url
    LookupModule.open_url = MockOpenURL
    LookupModule.open_url.side_effect = MockOpenURL
    # mock LookupBase.get_option
    class MockGetOption:
        def __init__(self, *args, **kwargs):
            pass

# Generated at 2022-06-13 14:42:01.685446
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of LookupModule
    lookup_plugin = LookupModule()

    # Create mock objects for testing
    mock_display = MagicMock()
    mock_display.vvvv = Mock(return_value=None)

    # Monkeypatch display
    lookup_plugin.display = mock_display

    # Create a test term
    test_term = "https://example.com"

    # Create a test header
    test_header = {"Accept": "application/json"}

    # Create a test response
    test_response_body = "Example Domain"

    # Create a mock object for test_response_body
    mock_response = MagicMock()
    mock_response.read.return_value = test_response_body

    # create a mock object for open_url
    mock_open_url = MagicMock()
    mock_open

# Generated at 2022-06-13 14:42:06.657952
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    terms = ['https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/plugins/lookup/my_test_url.txt']
    result = module.run(terms, None)
    for s in result:
        assert (s and "hello world")


# Generated at 2022-06-13 14:42:15.911540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup_module = LookupModule()
    test_ret = test_lookup_module.run(terms = ["http://www.example.com"], variables = {"ansible_lookup_url_force": True})

# Generated at 2022-06-13 14:42:24.607170
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case 1: ask for a URL and receive an answer
    terms = [ "http://www.google.com" ]
    l = LookupModule()
    assert l.run(terms)[0].startswith("<!doctype html>")

    # Test case 2: ask for a URL that does not exist
    terms = [ "http://www.googlecom" ]
    l = LookupModule()
    assert l.run(terms) == []

    # Test case 3: ask for a URL not using http
    terms = [ "https://www.google.com" ]
    l = LookupModule()
    assert l.run(terms)[0].startswith("<!doctype html>")

# Generated at 2022-06-13 14:42:25.402906
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:44:02.658967
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Performs unit test for method run of class LookupModule

    import mock
    import os
    import sys
    import StringIO
    import json

    # Use StringIO to avoid writing the output to stdout
    saved_stdout = sys.stdout
    out = StringIO.StringIO()

    # Use 'json' module to get the correct string format

# Generated at 2022-06-13 14:44:09.068280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test function for LookupModule._run
    '''
    # create LookupModule instance
    lookup_module = LookupModule()

    # set needed input parameters
    terms = ['www.amazon.com']

    # execute run function and catch any exception
    try:
        result = lookup_module.run(terms=terms)
        assert result is not None
    except Exception as e:
        print("oops! " + str(e))

# Generated at 2022-06-13 14:44:11.332374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: add unittest here
    pass

if __name__ == "__main__":
    print(test_LookupModule_run())

# Generated at 2022-06-13 14:44:13.465922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   LookupModule().run(["https://github.com/ansible/ansible.github.io/keys/gpgkey.py"])
   assert True

# Generated at 2022-06-13 14:44:14.074302
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:44:21.474067
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils import connection
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    import socket

    class MockClass(object):
        def __init__(self):
            self.url = None
            self.username = None
            self.password = None
            self.headers = None
            self.force = None
            self.timeout = None
            self.http_agent = None
            self.force_basic_auth = None
            self.follow_redirects = None
            self.use_gssapi = None
            self.unix_socket = None
            self.ca_path = None
            self.unredirected_headers = None
