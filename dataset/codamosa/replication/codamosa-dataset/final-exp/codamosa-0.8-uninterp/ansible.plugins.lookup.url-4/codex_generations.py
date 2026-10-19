

# Generated at 2022-06-13 14:34:36.782885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import os

    terms = ['h']


    try:
        # cannot mock object, create a temporary file and then delete it
        with tempfile.NamedTemporaryFile(delete=False) as f:
            terms[0] = (f.name)

        lookup_module = LookupModule()
        response = lookup_module.run(terms)
        assert isinstance(response, list)
        assert len(response) == 1
        assert response[0] == ''

    except:
        raise
    finally:
        # remove the temporary file if exists
        if terms[0]:
            os.unlink(terms[0])



# Generated at 2022-06-13 14:34:49.010579
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:34:58.972907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    import datetime

    geoip_data = {'country_code': 'US',
                  'region': 'CA',
                  'area_code': 0,
                  'longitude': -122.3959,
                  'country_code3': 'USA',
                  'latitude': 37.7692,
                  'postal_code': '94110',
                  'dma_code': 807,
                  'metro_code': 'San Francisco, CA',
                  'country_name': 'United States',
                  'city': 'San Francisco'
                  }

    geoip_data_str = '%s\n' % '\n'.join(["%s: %s" % (k, v) for (k, v) in geoip_data.items()])


# Generated at 2022-06-13 14:34:59.463043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:35:05.209698
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    url = 'https://www.example.com'
    lookup = LookupModule()

    # Case 1: Successfully connect to url return list of lines
    response = mock.MagicMock()
    response.read.return_value = "Lorem\nIpsum"
    connector = mock.MagicMock()
    connector.open_url.return_value = response
    with mock.patch.object(lookup, 'open_url', connector.open_url):
        result = lookup.run([url], split_lines=True)

    assert(result == ["Lorem", "Ipsum"])

    # Case 2: Successfully connect to url, but lines are not split
    response = mock.MagicMock()
    response.read.return_value = "Lorem\nIpsum"
    connector = mock.MagicMock()


# Generated at 2022-06-13 14:35:16.827510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display.verbosity = 4
    terms = ["https://dummy_url1/something", "https://dummy_url2/something2"]
    from unittest import mock
    with mock.patch('ansible.module_utils.urls.open_url') as mock_open_url:
        mock_open_url.return_value = "some content"
        module = LookupModule()
        assert module.run(terms, None) == ["some content", "some content"]
        assert mock_open_url.call_count == 2
        assert mock_open_url.call_args_list[0][0][0] == "https://dummy_url1/something"
        assert mock_open_url.call_args_list[1][0][0] == "https://dummy_url2/something2"

# Generated at 2022-06-13 14:35:28.725622
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test a good lookup
    response = open_url('https://github.com/gremlin.keys', validate_certs=False)
    response_text = response.read()
    lookup = LookupModule()
    terms = ['https://github.com/gremlin.keys']
    variables = {}
    result = lookup.run(terms, variables)
    assert(len(result) == len(response_text.splitlines()))
    i = 0
    for line in response_text.splitlines():
        assert(result[i] == line)
        i = i + 1

    # Test an error lookup with default arguments
    lookup = LookupModule()
    terms = ['https://github.com/gremlin.keys']
    variables = {}
    result = lookup.run(terms, variables)

# Generated at 2022-06-13 14:35:33.189901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    url_object = LookupModule()
    url_object.set_options(var_options=None, direct=None)
    terms = ['https://httpbin.org/headers']
    print(url_object.run(terms))
    terms = ['https://httpbin.org/user-agent']
    print(url_object.run(terms))
    terms = ['https://httpbin.org/get']
    print(url_object.run(terms))
    terms = ['https://httpbin.org/redirect/4']
    print(url_object.run(terms))
    terms = ['http://httpbin.org:8184/html']
    print(url_object.run(terms))

# Generated at 2022-06-13 14:35:45.458214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['https://github.com/gremlin.keys']
    response = LookupModule().run(terms)
    assert len(response) == 2

# Generated at 2022-06-13 14:35:52.479126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils._text import to_bytes
    # We can't simply use 'from ansible.plugins.lookup import LookupModule' because
    # this would create an import loop
    LoM = getattr(__import__('ansible.plugins.lookup.url', fromlist=['LookupModule']), 'LookupModule')

    terms = ['https://github.com/gremlin.keys']
    terms_error = ['http://github.com/gremlin.keys']

    l = LoM()
    result = l.run(terms)

# Generated at 2022-06-13 14:35:59.621500
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('url')

    assert isinstance(lookup, LookupModule) == True

# Generated at 2022-06-13 14:36:06.936123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import subprocess
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.inventory
    import ansible.playbook.play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import discovery
    from ansible.plugins.lookup import url
    from ansible.template import Template

    # Create a dummy module to use as the remote connection
    class DummyModule(object):
        def __init__(self):
            self.default_output = 'default'

    assert sys.version_info >= (2, 7)

    # Get the directory this file is in (the tests directory)

# Generated at 2022-06-13 14:36:15.762448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    terms = ['https://github.com/gremlin.keys']

# Generated at 2022-06-13 14:36:26.744154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.urls import ConnectionError
    lu = LookupModule()
    ret = lu.run(["http://www.google.com","http://www.stackoverflow.com"])
    assert ret[0].find("<title>Google</title>") != -1
    assert ret[1].find("<title>Stack Overflow</title>") != -1
    assert lu.run(["http://invaliddomain:111111"]) == []
    assert lu.run(["http://www.wronggoogle.com"]) == []

# Generated at 2022-06-13 14:36:35.869765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    terms = to_bytes('github')
    variable = to_bytes('ansible_lookup_url_force')
    value = to_bytes('True')
    kw = {variable: value}
    l = LookupModule()
    l.set_options({'var_options': {variable: value}, 'direct': kw})
    assert l.get_option('force')

# Generated at 2022-06-13 14:36:38.727819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run('https://github.com/gremlin.keys') == ['']

# Generated at 2022-06-13 14:36:46.217583
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'validate_certs': False, 'use_proxy': False})


# Generated at 2022-06-13 14:36:58.410450
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    temp_lookup = LookupModule()

    # Testing the return value of method run when all given variables are valid
    # Testing for the output for one element in terms
    terms = ['https://localhost:8080/test.html']
    variables = dict(validate_certs=True, use_proxy=True, split_lines=True, username='testuser',
                     password='testuser', force=True, timeout=10.0, http_agent='test-agent',
                     force_basic_auth=True, follow_redirects='urllib2', use_gssapi=True, unix_socket=None,
                     ca_path='ca_path', unredirected_headers=['header1'])
    returned_value = temp_lookup.run(terms=terms,variables=variables)

# Generated at 2022-06-13 14:37:05.225121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.vvvv = lambda *a, **k: None
    module = LookupModule()
    module.set_options({'run_once': True, 'no_log': True})
    try:
        results = module.run(['https://github.com/gremlin.keys'])
    except AnsibleError as e:
        print(e)
        return False
    return True

# Generated at 2022-06-13 14:37:14.286310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize LookupModule object
    lm = LookupModule()

    # Initialize test variables
    terms = ['http://ip-address.domaintools.com/']
    want_list = True
    validate_certs = True
    split_lines = True
    use_proxy = True
    username = None
    password = None
    headers = {}
    force = False
    timeout = 10
    http_agent = 'ansible-httpget'
    force_basic_auth = False
    follow_redirects = 'urllib2'
    use_gssapi = False
    unix_socket = None
    ca_path = None
    unredirected_headers = None

# Generated at 2022-06-13 14:37:31.764595
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:37:36.939153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeResponse():
        def read(self):
            return "Hello World!"

    class FakeConn(object):

        def __init__(self, data):
            self.data = data

        def __enter__(self):
            return self

        def __exit__(self, type, value, traceback):
            pass

        def getresponse(self):
            return self.data

    terms = ['https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/azure_rm.py']
    variables = dict()
    lookup = LookupModule()
    lookup.set_options(var_options=variables)
    lookup.open_url = open_url
    lookup.open_url.return_value = FakeResponse()

    response = lookup.run(terms)
    assert not response

    lookup

# Generated at 2022-06-13 14:37:47.178859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.six.moves.urllib.request import OpenerDirector
    module = AnsibleModule()
    lf = LookupModule(loader=None, templar=None, variables=None)
    lf.set_options(direct={'http_agent': 'Ansible-Test'})

# Generated at 2022-06-13 14:37:57.196250
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()
    # Test split_lines == True
    ret = test_lookup.run('https://github.com/gremlin.keys')
    assert type(ret) is list
    assert type(ret[0]) is str

# Generated at 2022-06-13 14:38:07.055113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TERMS=['https://github.com/gremlin.keys', 'https://github.com/bcoca.keys']
    # TERMS=['https://ip-ranges.amazonaws.com/ip-ranges.json']
    TERMS=['https://raw.githubusercontent.com/mikeytown2/Lookup-Plugins/master/url/url_lookup.py']
    # TERMS=['https://ip-ranges.amazonaws.com/ip-ranges.json', 'https://raw.githubusercontent.com/mikeytown2/Lookup-Plugins/master/url/url_lookup.py', 'https://raw.githubusercontent.com/mikeytown2/Lookup-Plugins/master/url/url_lookup.py', 'https://raw.githubusercontent.com/mikeytown

# Generated at 2022-06-13 14:38:08.665057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = LookupModule()
    test_module.run('https://github.com/gremlin.keys')

# Generated at 2022-06-13 14:38:14.259195
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six.moves.urllib.error import URLError
    lookup_module = LookupModule()
    terms = ['https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/modules/system/setup.py']
    try:
        lookup_module.run(terms)
    except URLError as e:
        if "certificate verify failed" in to_text(e):
            test = True
        else:
            test = False
    except Exception as e:
        test = False
    assert test

# Generated at 2022-06-13 14:38:18.623861
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # ansible.plugins.lookup.url.LookupModule.run is a function
    # and is used in module_utils.urls , here is a patch to test module_utils.urls
    # ansible.module_utils.urls.open_url is patched to return a list of terms
    # after calling run method the list of terms are returned
    # if run executes successfully no exception is raised
    from ansible.plugins.lookup.url import LookupModule
    from ansible.module_utils.urls import open_url as open_url_orig
    from ansible.module_utils.six.moves.urllib.error import URLError
    import mock

# Generated at 2022-06-13 14:38:29.158374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup LookupModule to test
    ######################################

    # Dummy LookupModule for testing
    class Dummy_LookupModule(LookupModule):
        def __init__(self, loader=None, templar=None, **kwargs):
            pass
        def run(self, terms, variables=None, **kwargs):
            return terms

    # Dummy response from open_url
    class Dummy_response:
        def __init__(self, text_content):
            self.text_content = text_content
        def read(self):
            return self.text_content

    # Dummy loader
    class Dummy_loader:
        def __init__(self):
            pass

    # Dummy templar
    class Dummy_templar:
        def __init__(self):
            pass



# Generated at 2022-06-13 14:38:39.018710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()

    def stub_set_options(var_options, direct):
        var_options['follow_redirects'] = 'urllib2'
        var_options['validate_certs'] = True
        var_options['use_proxy'] = True

# Generated at 2022-06-13 14:39:02.380706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    host, unix_socket = LookupBase._get_socket_info()

    ca_path = LookupBase._get_ca_path()
    header_value = {'header1': "value1", 'header2': 'value2'}


# Generated at 2022-06-13 14:39:06.248681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule class
    lookup = LookupModule()
    # Give value to term
    term = "https://httpbin.org/get"
    # Call method run of class LookupModule
    response = lookup.run(terms=term)
    # Decode the response in JSON format
    json_response = json.loads(response[0])
    # Check if the value of url key in response is equal to term
    assert json_response['url'] == term

# Generated at 2022-06-13 14:39:14.697302
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # make a test stub
    class StubLookupBase(LookupBase):
        def __init__(self, terms, variables=None, **kwargs):
            self._terms = terms
            self._variables = variables
            self._kwargs = kwargs
            self.test_dict = dict(test_key='test_value', test_key_2='test_value_2')

        def get_option(self, key):
            if key in self.test_dict.keys():
                return self.test_dict[key]
            else:
                raise AnsibleError("Invalid key %s" % key)

        def run(self, terms, variables=None, **kwargs):
            return self.test_dict

    terms = 'test_terms'
    variables = dict(test_key_3='test_value_3')


# Generated at 2022-06-13 14:39:25.124430
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()
    lookup_plugin.set_options({'URL_VALIDATE_CERTS': False, 'USE_PROXY': False})

    # test that for valid url, list of lines is returned
    response = 'line1\nline2\nline3\n'
    assert lookup_plugin.run(['http://validurl'], validate_certs=False,
                             use_proxy=False) == [response]

    # test that for invalid url, AnsibleError is thrown
    try:
        lookup_plugin.run(['http://invalidurl'])
        assert False
    except AnsibleError:
        assert True

    # test that for valid url, list of lines is returned
    response = 'line1\nline2\nline3\n'

# Generated at 2022-06-13 14:39:28.515711
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # run method raises HTTPError (on failure), returns lookups otherwise
    assert isinstance(module.run(terms=[], variables={}), list)


if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:39:39.435124
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_obj = LookupModule()

    test_terms = (
        'https://www.ansible.com/resources/resources/videos',
        'https://www.ansible.com/resources/resources/webinars',
        'https://www.ansible.com/resources/resources/webinars',
    )


# Generated at 2022-06-13 14:39:47.916980
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_obj = LookupModule()

    # First test
    terms = ["https://github.com/gremlin.keys"]
    variables = None
    kwargs_default = {'validate_certs': True, 'use_proxy': True, 'username': None,
                      'password': None, 'headers': {}, 'force': False, 'timeout': 10,
                      'http_agent': 'ansible-httpget', 'force_basic_auth': False,
                      'follow_redirects': 'urllib2', 'use_gssapi': False, 'unix_socket': None,
                      'ca_path': None, 'unredirected_headers': []}

# Generated at 2022-06-13 14:39:48.548666
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:39:58.362642
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import pytest
    import ansible.module_utils.urls
    import os

    ansible.module_utils.urls.urlopen = fake_urlopen
    fixture_path = os.path.join(os.path.dirname(__file__), '../fixtures/')
    with open(fixture_path+'lookup_url_fixture_2.txt') as f:
        expected_output = f.read()

    # Old signatures for LookupBase.set_options and LookupBase.run
    # which use *args and **kwargs ignored. New functionality is
    # exercised in the module being tested (lookup_plugins/url.py).

# Generated at 2022-06-13 14:40:06.430610
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class module:
        def __init__(self, verbosity=False):
            self.params = {}
            self.params['lookup_plugin'] = 'url'
            self.params['_raw_params'] = 'https://github.com/gremlin.keys'
            self.params['split_lines'] = True
            self.params['wantlist'] = True
            self.params['username'] = False
            self.params['password'] = False
            self.params['headers'] = False
            self.params['force'] = False
            self.params['timeout'] = 10
            self.params['validate_certs'] = True
            self.params['http_agent'] = 'ansible-httpget'
            self.params['force_basic_auth'] = False

# Generated at 2022-06-13 14:40:45.774813
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    terms = ['http://www.example.com/']
    validate_certs = True
    split_lines = True
    use_proxy = True
    username = None
    password = None
    headers = {}
    force = False
    timeout = 10
    http_agent = 'ansible-httpget'
    force_basic_auth = False
    follow_redirects = 'urllib2'
    use_gssapi = False
    unix_socket = None
    ca_path = None
    unredirected_headers = None

# Generated at 2022-06-13 14:40:53.198543
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    response = lookup.run(terms=["https://github.com/gremlin.keys"], variables=None, validate_certs=True, use_proxy=True, username="username", password="password",
                                                                           headers={"header1":"value1", "header2":"value2"}, force=True, timeout=100, http_agent="agent", force_basic_auth=True,
                                                                           follow_redirects="all", use_gssapi=True, unix_socket="/path/to/file", ca_path="/path/to/CA/file", split_lines=True, unredirected_headers=None)
    return response

# Generated at 2022-06-13 14:41:00.023950
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import json
    import tempfile

    print("\nUnit test for method run of class LookupModule")

    temp_dir = tempfile.TemporaryDirectory()

# Generated at 2022-06-13 14:41:00.759201
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert True

# Generated at 2022-06-13 14:41:09.568048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "https://www.google.com/"
    ]
    options = {
        "validate_certs": True,
        "use_proxy": True,
        "username": None,
        "password": None,
        "headers": None,
        "force": True,
        "timeout": 10,
        "http_agent": "ansible-httpget",
        "force_basic_auth": False,
        "follow_redirects": 'urllib2',
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": [],
        "split_lines": True
    }
    output = lookup.run(terms=terms, variables=options)

# Generated at 2022-06-13 14:41:19.553802
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_mock = {}
    class DisplayFactory:
        def Display(self):
            return DisplayMock()
    display_factory = DisplayFactory()

    from ansible.plugins.lookup import LookupBase
    lu = LookupBase()
    lu.set_options(var_options=None, direct=None)
    import mock
    mock_open_url_full = mock.MagicMock(side_effect=[
        ('{"foo": "bar"}'),
        ('{"foo": "bar"}'),
        ('{"foo": "bar"}')
    ])


# Generated at 2022-06-13 14:41:31.224893
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a Mock class to replace the one from module_utils
    import types
    class MockClassMaker(type):
        @classmethod
        def __prepare__(metacl, name, bases):
            return {'MockOpenUrl': None, 'MockResponse': None, 'MockRead': None, 'MockSSLValidationError': None}

        def __new__(cls, name, bases, attrs):
            class MockClass(object): pass
            MockClass.__name__ = name
            for attr, value in attrs.items():
                setattr(MockClass, attr, value)
            return MockClass


# Generated at 2022-06-13 14:41:41.210102
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import json
    import random
    import string

    from ansible.module_utils.urls import open_url
    from ansible.module_utils._text import to_text

    from ansible.plugins.lookup import LookupModule

    # Mock result for urlopen
    class MockResult(object):

        def __init__(self, body):
            self.read = lambda: body

    # Random string generator
    def random_string(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # Mock open_url function
    def mock_open_url(url, validate_certs=True, use_proxy=True, **kwargs):

        assert validate_certs is True

# Generated at 2022-06-13 14:41:53.542918
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options:
        split_lines=True
        validate_certs=False
    lm = LookupModule()
    lm.set_options(var_options=Options)
    terms = ['https://github.com/gremlin.keys']

# Generated at 2022-06-13 14:42:01.909469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()

# Generated at 2022-06-13 14:43:34.992758
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    l = LookupModule()
    l.get_option = lambda x: True
    l.set_options({'wantlist': False})
    terms = ['http://foo.com/bar.txt']
    assert l.run(terms) == [
        '# this is a comment\n',
        'foo: 3\n',
        'bar: something\n',
        '\n',
        '# this is another comment\n',
        'test: ansible\n',
    ]


# Generated at 2022-06-13 14:43:42.360834
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:43:53.226689
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test if LookupModule.run method does what is expected.
    """
    from collections import namedtuple
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.urls import open_url

    TestConfig = namedtuple('Config', ['validate_certs', 'use_proxy', 'username', 'password', 'headers',
                                       'force', 'timeout', 'http_agent', 'force_basic_auth', 'follow_redirects',
                                       'use_gssapi', 'unix_socket', 'ca_path', 'unredirected_headers'])

# Generated at 2022-06-13 14:44:04.708512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import requests
    import responses
    import urlparse

    def request_callback(request):
        url = urlparse.urlparse(request.url)
        assert url.path == '/test-path'
        assert url.query == 'test-query'
        return (200, {}, 'test-body')

    terms = [
        'http://test-domain.com/test-path?test-query',
        'http://test-domain.com/test-path',
    ]

    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        for term in terms:
            rsps.add_callback(responses.GET, term, callback=request_callback)

        module = LookupModule()

        # Replace the request method of LookupModule class with the one provided by `responses`

# Generated at 2022-06-13 14:44:15.169774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mocking 'module_utils.urls.open_url' for the duration of the unit test.
    # Since it is a function and not a class, I'm using a static method function to
    # mock it in the 'module_utils.urls' module and then call the method I want to
    # test.
    # NOTE : Borrowed from 'ansible.plugins.lookup.file'.
    # TODO : How do we un-mock the class after the unit test is complete ?
    import __builtin__
    import module_utils.urls
    old_open_url = module_utils.urls.open_url
    def open_url_test(url, *args, **kwargs):
        return url
    module_utils.urls.open_url = open_url_test

    # Executing the run() method

# Generated at 2022-06-13 14:44:22.272493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.urls import open_url
    import json, socket

    class ErrLookupModule(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            raise Exception('Lookup error')

    #new object
    test_obj = LookupModule()
    assert test_obj

    #success
    result = test_obj.run(['http://www.google.com'])
    assert result is not None
    assert len(result) > 0
    assert result[0].startswith("<!doctype html>")

    #failure
    try:
        test_obj.run(['http://www.notexistsdomain123454321.com'])
    except AnsibleError:
        pass

    #success