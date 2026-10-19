

# Generated at 2022-06-13 13:52:37.061619
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test case for LookupModule.run """
    lm = LookupModule()
    terms = ['not_exist_key', 're=', 'user', 'type=properties', 'file=dummy_user.properties', 'user2.password']
    var_options = {}
    kwargs = {}
    ret = lm.run(terms, var_options, **kwargs)
    assert ret == [None, '', 'xavier', 'xavier', 'azerty']

# Generated at 2022-06-13 13:52:42.028967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # Create a new LookupModule object
    lm = LookupModule(loader=None, variables=None)

    # Args for method run
    terms = ['test']
    # Call method
    assert lm.run(terms, variables=None, file='test.ini') == ['test']
    del lm

# Generated at 2022-06-13 13:52:53.046382
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    section = "section_name"
    key = "key"
    k = ".*"

    # Define configparser
    config = configparser.ConfigParser()
    # Add a section
    config.add_section(section)
    # Set variables and values
    config.set(section, "key1", "value1")
    config.set(section, "key2", "value2")
    config.set(section, "key3", "value3")

    lm = LookupModule()
    lm.cp = config

    assert lm.get_value(key, section, None, False) == "value1"
    assert lm.get_value(key, section, None, True) == "value1"

# Generated at 2022-06-13 13:53:03.576526
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Test a regexp to retrieve all values of a given section
    cp = configparser.ConfigParser()
    config = StringIO()
    config.write("[section]\nkey1=value1\nkey2=value2\nkey3=value3\n[section2]\nkey1=value1")
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)

    lookup = LookupModule()
    lookup.cp = cp
    assert lookup.get_value(".*", "section", "", True) == ["value1", "value2", "value3"]

    # Test the return of a single value
    assert lookup.get_value("key1", "section", "", False) == "value1"
    assert lookup.get_value("key2", "section", "", False)

# Generated at 2022-06-13 13:53:15.127523
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_file_contents(self, path):
        return '[global]\nuser=matt.jones\n[integration]\nuser=tom.ford\n[production]\nuser=peter.chen\n', None
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.lookup_module = LookupModule()
            self.lookup_module._loader.get_file_contents = get_file_contents
            self.lookup_module.set_options({'file': 'users.ini', 'section': 'global'})


# Generated at 2022-06-13 13:53:22.439793
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    allresults = []
    lookup = LookupModule()

    for testcase in TEST_LOOKUP_MODULE_RUN:

        # init variables
        terms = []
        variables = {'ansible_env': {'HOME': '/Users/yannig'}}
        kwargs = {}
        for param, value in testcase.get('params', {}).items():
            kwargs[param] = value

        # init file (if any)
        lookup.set_loader(basic.AnsibleLoader())
        if testcase.get('file'):
            lookup._loader.path_exists = lambda x: True
            lookup._loader.get_basedir = lambda x: ''
            lookup._loader.get_file

# Generated at 2022-06-13 13:53:33.606000
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Test list of values
    cp = configparser.ConfigParser()
    cp.add_section('section1')
    cp.set('section1', 'key11', 'value11')
    cp.set('section1', 'key12', 'value12')
    cp.set('section1', 'key1', 'value1')
    l = LookupModule()
    l.cp = cp
    result = l.get_value('key1.*', 'section1', None, True)
    assert result == ['value11', 'value12']

    # Test single value
    cp = configparser.ConfigParser()
    cp.add_section('section1')
    cp.set('section1', 'key1', 'value1')
    l = LookupModule()
    l.cp = cp

# Generated at 2022-06-13 13:53:43.451193
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Prepare object LookupModule
    lookupModule = LookupModule()

    # Prepare string used to perform the test
    test_run_string = "[test_ini_section]\nkey1=value1\nkey2=value2\nkey3=value3\n"

    # Mock the class method 'set_options'
    lookupModule.set_options = lookupModule.set_options
    # Mock the class method 'get_options'
    lookupModule.get_options = lookupModule.get_options
    # Mock the class method 'find_file_in_search_path'
    lookupModule.find_file_in_search_path = lambda variables, dirs, filename: test_run_string
    lookupModule.cp = configparser.ConfigParser(allow_no_value=False)

    # Perform test

# Generated at 2022-06-13 13:53:51.414585
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    test_ini_content = StringIO("""[section]
key1=value1
key1re=value1re
key2=value2
[section2]
key3=value3
""")

    # Parse test ini file
    cp = configparser.ConfigParser()
    cp.readfp(test_ini_content)

    # Create LookupModule
    lookup_module = LookupModule()
    lookup_module.cp = cp

    # Test case 1: Retrieve a single value
    assert lookup_module.get_value("key1", "section", None, False) == "value1"

    # Test case 2: Retrieve all values from a section using a regexp
    assert lookup_module.get_value("key1", "section", None, True) == ["value1"]

# Generated at 2022-06-13 13:54:04.156736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    lookup = LookupModule()

    assert lookup.run(['user', 'port', 'db'], {}, file='hosts.ini', section='mysql') == ['root', '3306', 'db1']
    assert lookup.run(['user', 'port', 'db'], {}, file='hosts.ini', section='mysql', default=['user1', '3306', 'db1']) == ['root', '3306', 'db1']

    assert lookup.run(['built_by=root', 'db'], {}, file='hosts.ini', section='mysql') == ['db1']

# Generated at 2022-06-13 13:54:20.179604
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.add_section('section1')
    lookup_module.cp.set('section1', 'key1', 'value1')
    lookup_module.cp.set('section1', 'key2', 'value2')
    lookup_module.cp.set('section1', 'key3', 'value3')

    lookup_module.cp.add_section('section2')
    lookup_module.cp.set('section2', 'key4', 'value4')
    lookup_module.cp.set('section2', 'key5', 'value5')
    lookup_module.cp.set('section2', 'key6', 'value6')


# Generated at 2022-06-13 13:54:33.230573
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(u"""
[section1]
key1=value1
key2=value2
key3=value3
key4=value4
key5=value5
    """)
    config.seek(0, os.SEEK_SET)

    # Read config
    lookup_module.cp.readfp(config)

    # Assert values
    assert lookup_module.get_value("key1", "section1", False, False) == "value1"
    assert lookup_module.get_value("key2", "section1", False, False) == "value2"

# Generated at 2022-06-13 13:54:40.933443
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class fake_loader():
        def __init__(self):
            self._get_file_contents_calls = 0
        def _get_file_contents(self, path):
            self._get_file_contents_calls += 1
            return ("""
[section1]
key1=value1
key2=value2
;comment1
key3=value3

[section2]

[section3]
key1=value1
key2=foobar
""", True)

    class fake_lookup():
        def __init__(self):
            self._loader = fake_loader()
            self.cp = configparser.ConfigParser()
            self.get_value = LookupModule.get_value
            self.find_file_in_search_path = lambda variables, dirname, filename: None



# Generated at 2022-06-13 13:54:47.847303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get a LookupModule class and its method run
    module = LookupModule()
    run = getattr(module, 'run')
    # Initialize parameters.
    # The ini file simply contains ['global'].
    # We want to retrieve the value of key 'user' in section 'global'.
    terms = ['user']
    var_options = {}
    direct = {'file': 'ansible.ini', 'default': '', 're': False, 'section': 'global'}
    # Execute run method
    result = run(terms, var_options, direct)
    assert result[0] == 'ansible'

# Generated at 2022-06-13 13:55:00.076144
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for method run of class LookupModule."""
    # pylint: disable=too-few-public-methods
    class MockTerm:
        """Mock class to create term just with key."""
        def __init__(self, key):
            self.key = key

    # create LookupModule
    lookup_module = LookupModule()

    # init params
    terms = [MockTerm('user'), MockTerm('pass')]
    options = {
        'type': 'ini',
        'file': 'tests/files/users.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
        'allow_none': False
    }



# Generated at 2022-06-13 13:55:07.809770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the method run of class LookupModule
    """
    from ansible.module_utils.six.moves import configparser
    from ansible.plugins.lookup import LookupBase
    from ansible.errors import AnsibleLookupError, AnsibleOptionsError
    import os

    import StringIO

    lookup_module = LookupModule()

    # test case 1: config
    terms = ['user', 'password']
    parsers = configparser.ConfigParser(allow_no_value=False)
    config = StringIO.StringIO()
    config.write(u'[global]\n')
    config.write(u'user=yannig\n')
    config.write(u'password=yannig\n')
    config.seek(0, os.SEEK_SET)
    parsers.readfp

# Generated at 2022-06-13 13:55:15.545608
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    paramvals = {}
    path = lookup.find_file_in_search_path(paramvals, 'files', 'users.ini')
    assert path == 'users.ini'
    assert lookup.run(['user', 'password'], paramvals, section='integration', file='users.ini')[0] == 'yannig'
    assert lookup.run(['user', 'password'], paramvals, section='production', file='users.ini')[0] == 'david'

# Generated at 2022-06-13 13:55:22.930030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyLookupBase(LookupBase):
        def __init__(self):
            self.loader = ""
        def find_file_in_search_path(self, variables, file_paths, file_name):
            return "tests/unittests/ini/users.ini"
        def _get_file_contents(self, path):
            return "", ""

# Generated at 2022-06-13 13:55:25.836643
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    #return None because there is no key in the ini file
    assert LookupModule.get_value(None, "key", "section", "default", "is_regexp") == "default"


# Generated at 2022-06-13 13:55:40.301584
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    def test(params, result_value, result_type, exception=None):
        assert result_type in ['exception', 'value']

        term = "'=".join(params.values())
        try:
            l = LookupModule()
            l.cp = configparser.ConfigParser()
            l.cp.add_section('section')
            l.cp.set('section', 'key', 'value')
            #for k, v in params.items():
            #    l.set_option(k, v)

            returned = l.get_value('key', 'section', None, False)
            assert result_type == 'value'
            assert returned == result_value
        except Exception as e:
            assert result_type == 'exception'
            assert type(e) == type(exception)

# Generated at 2022-06-13 13:56:04.008902
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['key', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini', 'file=ansible.ini']

    """
    Should return variable key_value
    """
    variable

# Generated at 2022-06-13 13:56:13.691296
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Basic test private method _parse_params
    assert _parse_params("key", {}) == ['key']
    assert _parse_params("key1 key2", {}) == ['key1', 'key2']
    assert _parse_params("key section=prod", {'section': 'dev'}) == ['key']
    assert _parse_params("key section=prod", {'section': 'dev'}) == ['key']
    assert _parse_params("key1 key2 section=prod", {'section': 'dev'}) == ['key1', 'key2']
    assert _parse_params("key1 key2 section=prod", {}) == ['key1', 'key2']

    # Testing method private method get_value
    cp = configparser.ConfigParser(allow_no_value=False)
    s = StringIO()

# Generated at 2022-06-13 13:56:25.792347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os.path
    import tempfile

    term = "test"
    contents = """
[global]
test=test
test1=test1
test2=test2
test_1=test_1
test_2=test_2

[section1]
test1=test1
test2=test2
test_1=test_1
test_2=test_2

[section2]
test1=test1
test2=test2
test_1=test_1
test_2=test_2
"""
    # Create a temporary file and write contents to it
    fd, pathname = tempfile.mkstemp()
    fp = os.fdopen(fd, 'w+')
    fp.write(contents)
    fp.close()

    # Call LookupModule class
    lookup

# Generated at 2022-06-13 13:56:37.370916
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser(allow_no_value=False)
    cp.optionxform = str
    cp.read('test/units/lookup_plugins/test_ini.ini')
    lm = LookupModule()
    lm.cp = cp

    # test_get_value_single
    assert lm.get_value('key1', 'section1', 'default', False) == 'value1'

    # test_get_value_regexp
    assert lm.get_value('.*', 'section1', 'default', True) == ['value1', 'value2', 'value3']

    # test_get_value_not_existing
    assert lm.get_value('Not-Existing', 'section1', 'default', False) == 'default'

    # test_get_value_no_

# Generated at 2022-06-13 13:56:50.090708
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: fix this test to use AnsibleModuleTestCase in test/lib/ansible_test

    LO = LookupModule()
    LO.cp = configparser.ConfigParser()
    LO.cp.readfp(StringIO("""
[global]
key=value
key2=value2

[section1]
key=value
key2=value2

[section2]
key=value
key2=value2
        """))
    result = LO.get_value("key", "section1", "", False)
    assert(result == "value")
    result = LO.get_value(".*", "section1", [], True)
    assert(result == ["value", "value2"])
    result = LO.get_value("key", "section1", "", False)

# Generated at 2022-06-13 13:56:53.648305
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Write test
    print("TODO: Write test for method 'run' of class LookupModule")
    return False

test_LookupModule_run()


# Generated at 2022-06-13 13:57:04.090454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    #
    # Import module
    #
    import ansible.plugins.lookup.ini
    #
    # Create mock object to use `LookupBase`
    #
    class args:
        def __init__(self):
            self.fail_on_undefined_errors = False
    #
    # Create class to mock
    #
    class MockLookupModule(ansible.plugins.lookup.ini.LookupModule):

        def __init__(self, loader=None, templar=None, variables=None):
            self.args = args()
            self.loader = loader
            self.templar = templar
            self._templar = templar

        def _deprecate_inline_kv(self):
            return


# Generated at 2022-06-13 13:57:14.986565
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_input = ['''[section1]
key1=value1
key2=value2
key3=value3
key4=value4
''','''[section2]
key1=value1
key2=value2
key3=value3
key4=value4
''','''[section3]
key1=value1
key2=value2
key3=value3
key4=value4
''']


# Generated at 2022-06-13 13:57:27.696311
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Only test for python3 for now
    # This test is only meaningfull if we have the exact same behavior
    # whatever the used configparser version of python2 or python3
    if configparser.__name__ == "configparser":
        # python 3
        key  = "user"
        section = "mysqld"
        cp = configparser.ConfigParser(allow_no_value=True)
        lm = LookupModule(cp)
        try:
            # lm.get_value(key, section, dflt, is_regexp)
            assert(lm.get_value(key, section, "default", False) is None)
        except Exception as e:
            raise
        finally:
            cp = configparser.SafeConfigParser()
            lm = LookupModule(cp)

# Generated at 2022-06-13 13:57:39.573926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # Create a lookup_module
    lookup_module = lookup_loader.get('ini', basedir=[])
    assert lookup_module

    # Create an object of type LookupModule
    lm = lookup_module(None, {'file': '../test/test.ini', 'type': 'properties', 'default': 'default value', 'case_sensitive': True,
                              'allow_no_value': True}, [], [], [])

    # Run method run
    result = lm.run(terms=[], variables={'playbook_dir': os.getcwd()})
    assert result == [AnsibleUnsafeText(u'')]

# Generated at 2022-06-13 13:58:18.787159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Dummy class to provide options for the run
    class Options:
        section = 'section1'
        file = 'test.ini'
        default = ''
        encoding = 'utf-8'
        case_sensitive = False
        allow_no_value = False
        allow_none = False
        re = True

    terms = [
        'key1', 'key2', 'key3', 'unknown', 'key6', 'key6',
        'MyKey1', 'MyKey2', 'MyKey3', 'MyUnknown', 'MyKey6', 'MyKey6',
    ]

    test_re = re.compile(r'^key\d|^unknown|^key6|^M|^MyKey\d|^MyUnknown')


# Generated at 2022-06-13 13:58:23.729993
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test default
    assert lookup.run(["key"], dict()) == []

    # Test default
    assert lookup.run(["key"], dict(lookup__ini__default="foo")) == ["foo"]

    # Test direct arguments
    assert lookup.run(["key"], dict(), file="ansible.ini", section="DEFAULT") == []

# Generated at 2022-06-13 13:58:36.684711
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Given
    # A mock class with mocked config parser
    class MockLookupModule(LookupModule):

        def __init__(self):
            super(MockLookupModule, self).__init__()
            self.cp = configparser.ConfigParser()

    # When
    # Create LookupModule instance
    lookup_module = MockLookupModule()
    lookup_module.cp.add_section('sectionA')
    lookup_module.cp.set('sectionA', 'key', 'value')
    lookup_module.cp.set('sectionA', 'key1', 'value1')
    lookup_module.cp.set('sectionA', 'key2', 'value2')
    res = lookup_module.get_value('key', 'sectionA', 'default', False)

# Generated at 2022-06-13 13:58:43.488339
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    key = 'a'
    section = 'global'
    dflt = None
    is_regexp = False
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.add_section(section)
    lookup_module.cp.set(section, key, '1')
    result = lookup_module.get_value(key, section, dflt, is_regexp)
    assert result == '1'

# Generated at 2022-06-13 13:58:55.130407
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    LookupModule.run() Test
    """
    # Create configuration file for tests
    file = open('test.ini', 'w')
    file.write('[section1]\nkey11=value11\nkey12=value12\n[section2]\nkey21=value21\nkey22=value22')
    file.close()

    # Import LookupModule to test run method (to get the mock)
    from ansible.plugins.lookup import LookupModule
    # Mock LookupBase to test the parent class
    class MockLookupBase(LookupBase):
        def __init__(self, loader=None, templar=None, **kwargs):
            self.loader = loader
            self.templar = templar
            self._options = kwargs
    # Instantiate LookupModule

# Generated at 2022-06-13 13:58:59.348758
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookups = LookupModule()
    # TODO: mock the file and the default parameters
    # lookups.cp = configparser.ConfigParser()
    # lookups.cp.readfp(config)
    # assert lookups.get_value('foo', 'section', 'default', False) == ??
    # assert lookups.get_value('foo', 'section', 'default', True) == ??
    return

# Generated at 2022-06-13 13:59:10.042212
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm=LookupModule()

    # Read a section
    config = StringIO()
    config.write(u'[foo]\n')
    config.write(u'bar=baz\n')
    config.seek(0, os.SEEK_SET)
    lm.cp = configparser.ConfigParser()
    lm.cp.readfp(config)
    var = lm.get_value('bar', 'foo', None, False)
    assert var == 'baz'

    # Read a section with regex
    var = lm.get_value('.*', 'foo', None, True)
    assert var == ['baz']

    # Read a section with an key not present in ini file
    var = lm.get_value('toto', 'foo', None, False)
    assert var is None

# Generated at 2022-06-13 13:59:21.215427
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes

    # configparser seems to give problems with unicode, so the replace below is a workaround...
    try:
        u'\xb5'.encode('utf-8')
    except UnicodeEncodeError:
        configparser.DEFAULT_ENCODING = "iso8859-1"

    if PY3:
        unicode = str

    config = configparser.RawConfigParser()
    config.add_section('integration')
    config.set('integration', 'user', 'YOUR_USER')

    config.add_section('production')
    config.set('production', 'user', 'YOUR_PROD_USER')


# Generated at 2022-06-13 13:59:28.764676
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Given
    cp = configparser.ConfigParser()
    test_section = 'SECTION'
    cp.add_section(test_section)
    test_file = 'test'
    cp.set(test_section, 'test_key', 'test_value')

    # When
    lookup_module = LookupModule()
    lookup_module.cp = cp
    get_value_result = lookup_module.get_value('test_key', test_section, None, False)

    # Then
    assert 'test_value' == get_value_result


# Generated at 2022-06-13 13:59:40.393421
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create configuration parser
    config = StringIO()
    config.write("""
    [global]
    user = Yannig
    user2 =
    [integration]
    db = integration_db
    user = integration_user
    """)
    config.seek(0, os.SEEK_SET)

    # create a new instance and load the config file
    lookup_mod = LookupModule()
    lookup_mod.cp = configparser.ConfigParser()
    lookup_mod.cp.readfp(config)

    # no default value and section provided
    terms = ['user']
    ret = lookup_mod.run(terms)
    assert len(ret) == 1
    assert ret[0] == 'Yannig'
    # default value provided
    terms = ['user', 'default=the_user']
    ret = lookup

# Generated at 2022-06-13 14:00:35.032817
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Test get_value method of LookupModule 
    """
    assert type(LookupModule.get_value) == type(test_LookupModule_get_value)

# Generated at 2022-06-13 14:00:42.615504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Basic test
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.add_section("section1")
    lm.cp.set("section1", "key1", "val1")
    lm.cp.add_section("section2")
    lm.cp.set("section2","key2", "val2")
    lm.cp.add_section("section3")
    lm.cp.set("section3","key3","val3")
    lm.cp.set("section3","key4","val4")

    #  call run()
    result = lm.run([u"key1", u"key2", u"key3"])
    assert result == ['val1', 'val2', 'val3']

    # call run() with

# Generated at 2022-06-13 14:00:53.127983
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from io import StringIO

    # create ini content
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'key3=value3\n')
    config.write(u'[section2]\n')
    config.write(u'key11=value11\n')
    config.write(u'key21=value21\n')
    config.seek(0, os.SEEK_SET)

    # create LookupModule object
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(config)

    # test non regexp
    assert lookup.get_value

# Generated at 2022-06-13 14:01:03.705821
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('section1')
    l.cp.set('section1', 'key1', 'value1')
    l.cp.set('section1', 'key2', 'value2')

    assert 'value1' == l.get_value('key1', 'section1', None, False)
    assert None == l.get_value('key3', 'section1', None, False)
    assert None == l.get_value('key3', 'section2', None, False)
    assert ['value1', 'value2'] == l.get_value('.*', 'section1', None, True)

# Generated at 2022-06-13 14:01:14.712577
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test: load single key
    terms = ['key1']
    contents = '[section1]\nkey1=value1'
    parameters = {'type': 'ini', 'section': 'section1', 'encoding': 'utf-8', 'default': None, 'case_sensitive': False, 're': False}
    file = 'test.ini'

    # Load "file" with "contents"
    lookup.set_loader_for_testing(contents, file)

    # Execute test "run" method
    results = lookup.run(terms, variables=None, **parameters)

    # Verify one result
    assert len(results) == 1
    assert results[0] == 'value1'

    # Test: load multiple keys
    terms = ['key1', 'key2']
    contents

# Generated at 2022-06-13 14:01:27.021092
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: refactor this
    import __main__
    __main__.__file__ = 'test.ini'
    # Create LookupModule object
    lup = LookupModule()

    # Create a StringIO for the test
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'keyToReturn=value\n')
    config.write(u'[section2]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'key3=value3\n')

# Generated at 2022-06-13 14:01:30.954007
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    ret = lm.run(["user", "group"], variables=dict(ansible_lookup_plugin_path=['/srv/myplugins']), file='test.ini', section='test')
    assert ret[0] == "yannig"
    assert ret[1] == "test"

# Generated at 2022-06-13 14:01:40.105299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.parsing.plugin_docs import read_docstring

    test_ini = '[section1]\nkey=value\n'

    # Compose test options
    import base64
    options = base64.b64encode(ImmutableDict({'file': 'ansible.ini', 'default': '', 'case_sensitive': 'False', 're': 'False', 'allow_no_value': 'False', 'type': 'ini'})._data)

    # Create a Lookup module object
    lookup = LookupModule()

    # Assign necessary value
    lookup.loader = DictDataLoader({'files': {'ansible.ini': test_ini}})



# Generated at 2022-06-13 14:01:49.405655
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:01:55.640825
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    lookup = LookupModule()
    # Read a properties file
    lookup.set_options({'file':'test_property.properties', 'type':'properties'})
    # Call run with the key 'properties.test.key'
    terms = lookup.run([u"properties.test.key"])
    # Key value is 'toto'
    assert terms == [u"toto"]
