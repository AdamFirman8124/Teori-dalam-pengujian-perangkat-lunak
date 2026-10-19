

# Generated at 2022-06-13 13:52:37.890252
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import warnings
    import unittest

    # Suppress deprecation warning for method _parse_params
    warnings.filterwarnings('ignore', category=DeprecationWarning, module=r'ansible\.plugins\.lookup')

    module_path = os.path.realpath(os.path.dirname(__file__) + os.sep + '..')
    sys.path.insert(0, module_path)

    from ansible.plugins.lookup.ini import LookupModule

    l = LookupModule()

    # test all options
    terms = {'test': 'type=properties file=users.properties section=test key=user default=test_default re=True'}
    variables = {'hostvars': {}}

# Generated at 2022-06-13 13:52:47.012191
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Create LookupModule object
    lk = LookupModule()

    # Create a StringIO used to parse ini
    config = StringIO()
    config.write(u'[test]\n')
    config.write(u'key=value\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.seek(0, os.SEEK_SET)

    # Create configparser object
    cp = configparser.ConfigParser(allow_no_value=False)

    # Init LookupModule object with configparser object created
    lk.cp = cp

    # Parse ini using configparser object
    lk.cp.readfp(config)

    # Check test with regexp pattern

# Generated at 2022-06-13 13:52:59.744616
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize class
    lookup = LookupModule()
    # Test with no term
    terms = []
    terms_result = []
    assert lookup.run(terms) == terms_result
    # Test simple case
    terms = ["user"]
    terms_result = ["foo"]
    assert lookup.run(terms) == terms_result
    # Test case insensitive
    terms = ["User"]
    terms_result = ["foo"]
    assert lookup.run(terms) == terms_result
    # Test with section
    terms = ["user", "password"]
    terms_result = ["foo", "bar"]
    assert lookup.run(terms) == terms_result
    # Test with type = properties
    terms = ["user.name", "user.password"]
    terms_result = ["foo", "bar"]
    assert lookup.run(terms)

# Generated at 2022-06-13 13:53:11.432084
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a LookupModule instance
    lookup_module = LookupModule()

    # Parameters
    content = """
[default]
user = root

[integration]
user = ansible

[production]
user = ansible
"""

    # Save the content in a temporary file
    import tempfile
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(content.encode())
    fp.close()

    # Test_1
    # Test the method run
    terms = [
        "user"
    ]
    options = {
        "file": fp.name,
        "section": "production"
    }
    expected = [
        "ansible"
    ]
    result = lookup_module.run(terms, variables={}, **options)

# Generated at 2022-06-13 13:53:22.983176
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    lookup = LookupModule()

    # Test regexp
    assert lookup.get_value('bar_', 'foo', 'test', True) == ['bar1', 'bar2']
    assert lookup.get_value('bar_', 'foo', 'test', False) == 'bar1'

    # Test single value
    assert lookup.get_value('bar1', 'foo', 'test', True) == 'bar1'
    assert lookup.get_value('bar1', 'foo', 'test', False) == 'bar1'

    # Test default value
    assert lookup.get_value('bar3', 'foo', 'test', True) == 'test'
    assert lookup.get_value('bar3', 'foo', 'test', False) == 'test'

    # Test exception

# Generated at 2022-06-13 13:53:33.969947
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import StringIO

    # Test with a property file
    lookup = LookupModule()
    lookup.set_options(var_options=dict(), direct={'type': 'properties', 'file': 'lookup_plugins/test.properties', 'encoding': 'utf-8'})
    config = StringIO()
    config.write(u'user.name=Koala\n')
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)
    results = lookup.run([u'user.name'])
    assert results == [u'Koala'], results

    # Test with an ini file
    lookup = LookupModule()

# Generated at 2022-06-13 13:53:35.338752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # unit test is skipped because we do not want to install Molecule for this.
    return None


# Generated at 2022-06-13 13:53:44.431621
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a dummy file containing ini data
    ini_data = """
    [section1]
    key1=value1
    key2=value2

    [section2]
    key1=value1
    key2=value2
    """
    test_file = open('/tmp/unit_test_ini.txt', 'w')
    test_file.write(ini_data)
    test_file.close()

    ini_data_properties = """
    key1=value1
    key2=value2
    """
    test_file_properties = open('/tmp/unit_test_ini_properties.txt', 'w')
    test_file_properties.write(ini_data_properties)
    test_file_properties.close()


# Generated at 2022-06-13 13:53:54.066888
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init module
    module = LookupModule()

    # Init data
    terms = ['user', 'user2', 'group']

    # Try to ignore param on unknown key
    kwargs = {'file': 'users.ini', 'section': 'integration', 'unknown': 'True'}
    variables = {'ansible_user': 'root'}
    module.run(terms, variables, **kwargs)

    path = module.find_file_in_search_path(variables, 'files', kwargs['file'])
    config = StringIO()
    # Special case for java properties
    config.write(u'[java_properties]\n')
    kwargs['section'] = 'java_properties'

    # Open file using encoding

# Generated at 2022-06-13 13:54:05.495869
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    # Init vars
    paramvals = {
        'file': 'example.ini',
        'case_sensitive': False,
        'type': 'ini',
        'encoding': 'utf-8',
        'allow_no_value': False
    }

    # Init lookup module
    lookup = LookupModule()

    loader = DataLoader()
    lookup.set_loader(loader)

    # Init ConfigParser
    config = StringIO()
    config.write(u'[global]\n')
    config.write(u'user1=name1\n')
    config.write(u'user2=name2\n')
    config.write(u'user3=name3\n')

# Generated at 2022-06-13 13:54:20.557867
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    _cp = configparser.ConfigParser()
    _cp.add_section('section1')
    _cp.set('section1', 'key1', 'value1')
    _cp.set('section1', 'key2', 'value2')
    _cp.set('section1', 'key3', 'value3')
    _cp.set('section1', 'key4', 'value4')
    _cp.set('section1', 'my_key5', 'my_value5')
    _cp.set('section1', 'my_key6', 'my_value6')

    # Test reading a section with a regexp
    values = LookupModule.get_value('^my_key[0-9]', 'section1', None, True)
    assert sorted(values) == ['my_value5', 'my_value6']

# Generated at 2022-06-13 13:54:33.284552
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import StringIO

    class MyLookupModule(LookupModule):

        def __init__(self, *args, **kwargs):
            super(MyLookupModule, self).__init__(*args, **kwargs)
            self.cp = configparser.ConfigParser()
            self.config = StringIO()
            self.config.write(u'[section]\n')
            self.config.write(u'key1=value1\n')
            self.config.write(u'key2=value2\n')
            self.config.write(u'key3=value3\n')
            self.config.seek(0, os.SEEK_SET)
            self.cp.readfp(self.config)


# Generated at 2022-06-13 13:54:40.990333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest import TestCase as UnitTestCase, mock

    from ansible.parsing.dataloader import DataLoader

    lookup_cls = LookupModule
    loader_cls = DataLoader

    class TestLookupModule(UnitTestCase):

        def setUp(self):
            self._mock_loader()
            self._mock_search_path()

        def _mock_loader(self):
            self.loader = mock.Mock(loader_cls)
            self.loader.get_basedir.return_value = '/'

        def _mock_search_path(self):
            self.search_path = mock.Mock(search_path=[])


# Generated at 2022-06-13 13:54:52.574659
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
  # Exemple of value returned by get_value
  result = LookupModule({})
  result.cp = configparser.RawConfigParser()
  result.cp.read('test/get_value.ini')
  assert result.get_value('A','section1','default',False) == '2'
  assert result.get_value('.*','section1','default',True) == ['2','3']
  assert result.get_value('bad_key','section1','default',False) == 'default'
  assert result.get_value('A','bad_section','default',False) == 'default'
  result.cp.read('test/get_value2.ini')
  assert result.get_value('A','section1','default',False) == 'default'

# Generated at 2022-06-13 13:54:54.136702
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert LookupModule.run is not None

# Generated at 2022-06-13 13:55:04.419028
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ret = []
    # Trying to parse the file using the wrong type
    try:
        ret = LookupModule().run(['username', 'password'], parameters={ "param1" : "value1"})
    except AnsibleLookupError:
        pass
    assert len(ret) == 0

    # Trying to find a wrong key in a wrong section
    try:
        ret = LookupModule().run(['username', 'password'], parameters={ "type" : "ini" })
    except AnsibleLookupError:
        pass
    assert len(ret) == 0

    # Trying to find a wrong key in a wrong section

# Generated at 2022-06-13 13:55:17.085568
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockConfigParser:
        def __init__(self, path):
            self.path = path
        def readfp(self, config):
            self.config = config.read()
    class MockLookupBase:
        def set_options(self, var_options=None, direct=None):
            pass
        def get_options(self):
            return {'section':'section1', 'file':'test.ini', 're':True,
                'encoding':'utf-8', 'default': None}
        
        def _deprecate_inline_kv(self):
            pass
        def find_file_in_search_path(self, variables, files_dir, file_name):
            return file_name
        def _loader(self):
            return self

# Generated at 2022-06-13 13:55:28.528919
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Example of section:
    # [section1]
    # key1=test1
    # key2=test2
    # key3=test3
    # key4=test4
    # key5=test5

    test_lookup_module = LookupModule()

    # Test with key1
    var_returned = test_lookup_module.get_value('key1', 'section1', '', False)
    assert var_returned == 'test1'

    # Test with regexp key[1-4]
    var_returned = test_lookup_module.get_value('key[1-4]', 'section1', '', True)
    assert len(var_returned) == 4
    assert var_returned[0] == 'test1'

# Generated at 2022-06-13 13:55:40.946821
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:55:50.557411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Let's execute run() with parameters
    # [('key1', {}, {'encoding': 'utf-8', 'default': '', 'section': 'section1', 're': False, 'file': 'test.ini', 'type': 'ini'})],
    # and check the result
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    assert lookup_module.run(['key1'], {}, encoding='utf-8', default='', section='section1', re=False, file='test.ini', type='ini') == ['value1']
    # Let's execute run() with parameters
    # [('key2=value2', {}, {})],
    # and check the result
    lookup_module.cp = configparser.ConfigParser()

# Generated at 2022-06-13 13:56:06.569442
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def get_file_content(file_name):
        with open(file_name, 'r') as file_handler:
            return file_handler.read()

    def get_ini():
        return configparser.RawConfigParser()

    def set_option(ini, section, option, value):
        if not ini.has_section(section):
            ini.add_section(section)
        ini.set(section, option, value)

    def check_lookup_result(data, expected_result):
        assert data == expected_result

    def check_lookup_exception(data, expected_exception):
        check_lookup_result(data.exception, expected_exception)

    def mock_find_file_in_search_path(self, variables, dir_name, file_name):
        return file

# Generated at 2022-06-13 13:56:16.452190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a string io to use as input for LookupModule
    config = StringIO()
    config.write(u'[Global]                                               \n')
    config.write(u'                                                       \n')
    config.write(u'# The default output directory                        \n')
    config.write(u'                                                       \n')
    config.write(u'output_directory = output/                             \n')
    config.write(u'                                                       \n')
    config.write(u'[Default]                                              \n')
    config.write(u'                                                       \n')
    config.write(u'# The default output directory                        \n')
    config.write(u'                                                       \n')
    config.write(u'output_directory = output/                             \n')
   

# Generated at 2022-06-13 13:56:27.074730
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookupModule = LookupModule()
    lookupModule.cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[section1]\nkey1=value1\nkey2=value2\nkey3=value3\n\n[section2]\nkey1=value1\nkey2=value2\nkey3=value3')
    config.seek(0, os.SEEK_SET)
    lookupModule.cp.readfp(config)

    # Test with a regexp
    assert lookupModule.get_value('key1', 'section1', 'dflt', True) == ['key2=value2', 'key1=value1']
    assert lookupModule.get_value('key4', 'section1', 'dflt', True) == []

    # Test without a regexp
   

# Generated at 2022-06-13 13:56:37.821978
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('section')
    l.cp.set('section', 'key1', 'value1')
    l.cp.set('section', 'key2', 'value2')

    assert(l.get_value('key1', 'section', 'default', False) == 'value1')
    assert(l.get_value('key2', 'section', 'default', False) == 'value2')
    assert(l.get_value('notexist', 'section', 'default', False) == 'default')
    assert(l.get_value('key1', 'notexist', 'default', False) == 'default')

# Generated at 2022-06-13 13:56:44.595465
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init of lookup plugin
    lookup_plugin = LookupModule()

    # Init of config
    class Config:
        def __init__(self):
            self.optionxform = to_native

    # Init of configparser
    class ConfigParser:
        def __init__(self, allow_no_value=False):
            self.cp = Config()

        def readfp(self, config):
            self.cp.readfp(config)

        def items(self, section):
            return self.cp.items(section)

        def get(self, section, key):
            return self.cp.get(section, key)

    # Init of StringIO
    class StringIO:
        def __init__(self):
            self.content = ""
            self.seek_pos = 0


# Generated at 2022-06-13 13:56:54.115094
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    test_file = os.path.join(os.path.dirname(__file__), 'ansible.ini')
    terms = [
        'user',
        'user=',
        'user=ansible',
        'type=ini file=',
        'type=ini file=ansible.ini',
        'type=ini file=ansible.ini section=',
        'type=ini file=ansible.ini section=global',
        'user=ansible type=ini file=ansible.ini section=global',
        'user=ansible type=ini file=ansible.ini section=global default=ansible',
        'user=ansible type=ini file=ansible.ini section=global default=ansible re=False'
    ]

# Generated at 2022-06-13 13:57:04.199129
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import sys
    module = sys.modules[__name__]
    class TestLookupModule(LookupModule):
        def __init__(self, **kwargs):
            super(TestLookupModule, self).__init__(**kwargs)
            self.cp = configparser.ConfigParser()

    lookup = TestLookupModule()

    cp = configparser.ConfigParser()
    cp.add_section('test_get_value')
    cp.set('test_get_value', 'user', 'John Doe')
    cp.set('test_get_value', 'base64_user', 'SG9yZW0gaXBzdW0=')
    lookup.cp = cp

    section = 'test_get_value'
    assert lookup.get_value('user', section, '', False) == 'John Doe'
   

# Generated at 2022-06-13 13:57:15.056957
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()
    # test for #7974
    # test for #7974 will pass if no exception raise
    params = [
        'a=b',
        'c=d',
        'key1',
    ]
    try:
        test_LookupModule.run(params, variables=None, file="test.ini")
    except AnsibleOptionsError:
        assert False
    # test for #18308: an example in lookup_plugin.py
    params = [
        'user',
        'section=integration',
        'file=users.ini',
    ]
    # if "AnsibleOptionsError" will raise, test_LookupModule_run() will fail

# Generated at 2022-06-13 13:57:17.587749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(['test', 'key']) == ['value']


# Generated at 2022-06-13 13:57:29.057675
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test to retrieve a single value
    cp = configparser.ConfigParser(allow_no_value=True)
    cp.optionxform = str
    config = StringIO()
    config.write(u'[section]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)
    test_obj = LookupModule()
    test_obj.cp = cp
    actual_result = test_obj.get_value('key1', 'section', '', False)
    expected_result = 'value1'
    assert actual_result == expected_result

    # Test to retrieve multiple value based on a regexp
    actual_result = test_obj.get

# Generated at 2022-06-13 13:57:47.024518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    from ansible.plugins.lookup import LookupBase
    from ansible.utils import context_objects as co

    # Create mock stdin
    sys.stdin = open('/dev/null', 'r')

    # Create the temp files
    file_name = "tmp_test_LookupModule_run_" + os.urandom(8).encode('hex') + ".ini"
    file = open(file_name, "w")

# Generated at 2022-06-13 13:57:59.192227
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=[])
    variable_manager.set_inventory(inventory)

    # Create play

# Generated at 2022-06-13 13:58:08.479731
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword
    from ansible.plugins.lookup import LookupBase as lookup_base
    from ansible.plugins.lookup import LookupModule as lookup_module
    from ansible.plugins.lookup import LookupBase as LookupBaseClass
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    from ansible.utils.path import unfrackpath

    display = Display()
    lookup_base.get_basedir = lambda self, variables: '/'

# Generated at 2022-06-13 13:58:20.564538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test get_value
    lm = LookupModule()
    cp = configparser.ConfigParser(allow_no_value=True)
    cp.readfp(StringIO('[java_properties]\nkey=value'))
    lm.cp = cp
    assert 'value' == lm.get_value('key', 'java_properties', '', False)
    assert '' == lm.get_value('key', 'java_properties', '', True)
    assert 'value' == lm.get_value('.*', 'java_properties', '', True)[0]
    # test_get_value_regexp
    cp = configparser.ConfigParser(allow_no_value=True)
    cp.readfp(StringIO('[java_properties]\nkey=value\nkey2=value2'))


# Generated at 2022-06-13 13:58:34.385789
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test retrieve all values from a section using a regexp
    test_ini_file = StringIO("""
[test_section]
name=Sinza
description=good_description
address=test_address
test_key=test_value
test_key2=test_value2""")
    cp = configparser.ConfigParser()
    cp.readfp(test_ini_file)
    test_lookup_module = LookupModule()
    test_lookup_module.cp = cp
    assert test_lookup_module.get_value(".*key", "test_section", None, True) == ['test_value', 'test_value2']
    assert test_lookup_module.get_value("description", "test_section", None, False) == 'good_description'
    assert test_lookup_module.get_value

# Generated at 2022-06-13 13:58:45.384284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config = LookupModule()
    # Test retreiving a single value
    config.cp = configparser.ConfigParser(allow_no_value=False)
    terms = ['user']
    paramvals = {
        'type': 'ini',
        'section': 'global',
        'file': 'ansible.ini',
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
    }
    config.cp.add_section('global')
    config.cp.set('global', 'user', 'ansible')
    value = config.run(terms, paramvals)
    assert value == ['ansible']

    # Test retreiving a single value from a property file
    config.cp = configparser.ConfigParser(allow_no_value=False)

# Generated at 2022-06-13 13:58:50.636504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Test LookupModule_run")

    res = LookupModule().run(
        [ 'user.name' ],
        variables={ 'role_path': './unit_tests/roles/role_1/' },
        type="properties",
        file='user.properties'
    )
    assert res == ['Bob']

    res = LookupModule().run(
        [ 'user' ],
        variables={ 'role_path': './unit_tests/roles/role_1/' },
        file='users.ini'
    )
    assert res == ['Bob']



# Generated at 2022-06-13 13:58:59.760841
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test cases for method get_value of class LookupModule
    # Test case for normal case
    class TestLookupModule(LookupModule):
        def __init__(self):
            self.cp = configparser.ConfigParser()
            self.cp.add_section('section')
            self.cp.set('section', 'key', 'value')
    lookup = TestLookupModule()
    value = lookup.get_value('key', 'section', 'dflt', False)
    assert value == 'value'
    # Test case for no section
    with pytest.raises(AnsibleLookupError, match=r"No section 'wrong_section' in file"):
        lookup.get_value('key', 'wrong_section', 'dflt', False)
    # Test case for no key
    # On Python 2.7, with

# Generated at 2022-06-13 13:59:10.306139
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for method run of class LookupModule
    # When both key and section are valid
    # assert the return value is not empty
    def test_positive_init():
        fp = open('/tmp/user1.ini', 'w')
        fp.write('[users]\n')
        fp.write('test=test')
        fp.close()
        lookup = LookupModule()
        lookup.run([{"file": '/tmp/user1.ini', "section": 'users', "key": "test"}], {})
        assert lookup.run([{"file": '/tmp/user1.ini', "section": 'users', "key": "test"}], {})
        os.remove('/tmp/user1.ini')


# Generated at 2022-06-13 13:59:21.402690
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    ini_file = configparser.ConfigParser()
    ini_file.readfp(open('tests/unit/lookup_plugins/ini/ini_test.ini'))
    lm = LookupModule()
    lm.cp = ini_file
    assert lm.get_value('key1', 'section1', '', False) == 'value1'
    assert lm.get_value('key1', 'section1', '', True) == ['value1']
    assert lm.get_value('key2', 'section2', '', False) == 'value2'
    # Test default value
    assert lm.get_value('key3', 'section3', 'default', False) == 'default'
    # Test regexp

# Generated at 2022-06-13 13:59:53.584270
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # _parse_params unit test
    _parse_params('key1 key2=value2', [])
    if _parse_params('key1 key2=value2', []) != ['key1', 'key2=value2']:
        raise Exception("_parse_params unit test returned unexpected result")
    # _parse_params unit test

    # unit tests for various cases
    # test one good case
    params = {'type': 'ini', 'section': 'test_section', 'file': 'test.ini', 're': 'False', 'default': 'default_value', 'case_sensitive': 'False'}
    terms = ['key1']
    config = StringIO()
    config.write("[test_section]\nkey1=value1\nkey2=value2\n")

# Generated at 2022-06-13 14:00:03.841749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test a simple use case
    ini_file = "[global]\nuser=foo\n"
    term = "user"
    variables = {
        "_terms": [term],
        "file": "ansible.ini",
        "section": "global"
    }
    options = {
        "encoding": "utf-8",
        "case_sensitive": False,
        "allow_no_value": False
    }
    expected = "foo"

    # Create an instance of LookupModule
    lm = LookupModule()
    lm.set_options(var_options=variables, direct=options)
    lm.cp = configparser.ConfigParser()
    lm.cp.readfp(StringIO(ini_file))

    # Retrieve the value

# Generated at 2022-06-13 14:00:11.075205
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lu = LookupModule()
    cp = configparser.ConfigParser()
    cp.add_section('qt')
    cp.set('qt', '1', '1')
    cp.set('qt', '2', '2')
    cp.set('qt', '3', '3')
    lu.cp = cp
    assert lu.get_value('1', 'qt', None, False) == '1'
    assert lu.get_value('1', 'qt', None, True) == '1'
    assert lu.get_value('[0-9]', 'qt', None, True) == ['1', '2', '3']
    assert lu.get_value('[A-Z]', 'qt', None, True) == []

# Generated at 2022-06-13 14:00:20.198252
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create a lookkup module
    lookup_module = LookupModule()

    # Create a configParser object
    cp = configparser.ConfigParser()

    # Create a StringIO object
    config = StringIO()

    # Write properties in the config object
    config.write(u'[java_properties]\n')

    config.write(u'firstname=John\n')
    config.write(u'lastname =Smith\n')
    config.write(u'age = 25\n')
    config.write(u'height = 1.87\n')

    # Set StringIO cursor back to beginning
    config.seek(0, os.SEEK_SET)

    cp.readfp(config)

    # Test method get_value with a single string
    # Test 1: not case_sensitive
    lookup_module.cp

# Generated at 2022-06-13 14:00:34.856139
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ["a", "b", "c"]
    path = "mypath"
    # Ugly way to test that the method find_file_in_search_path is called with expected parameters
    module.find_file_in_search_path = lambda x, y, z: z if z == path else None

    # Test with type = "properties"
    try:
        module.run(terms=terms, variables=None, file=path, type="properties")
    except Exception as e:
        raise AssertionError("unexpected exception", e)

    # Test with type = "ini"
    try:
        module.run(terms=terms, variables=None, file=path, type="ini")
    except Exception as e:
        raise AssertionError("unexpected exception", e)

# Generated at 2022-06-13 14:00:42.510048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    # Test with non existing file
    lookup.set_options(paths=['./', './roles/project/files/'])
    assert len(lookup.run([], {})) == 0

    # Test with a file with one value
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'lookupitem1', 'value1')
    assert lookup.run([], {'options': {'file': 'test.ini'}}) == ['value1']

    # Test with a file with multiple values
    lookup.cp.set('section1', 'lookupitem2', 'value2')

# Generated at 2022-06-13 14:00:43.595943
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:00:53.547161
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Test case :
    # - file :      test.ini
    # - sections :  [section1], [section2]
    # - key :       type
    # Expected :    [section1_key1, section2_key2]
    with open('test.ini', 'w') as f:
        f.write("[section1]\ntype=section1_key1\n[section2]\ntype=section2_key2")
    result = lookup_module.run([ "type", "file=test.ini", "section=section1"], variables=None)
    assert result == [ 'section1_key1' ]
    result = lookup_module.run([ "type", "file=test.ini", "section=section2"], variables=None)

# Generated at 2022-06-13 14:01:05.279681
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # initialize
    lm = LookupModule()
    # test regexp
    lm.cp = configparser.RawConfigParser()
    lm.cp.add_section('section1')
    lm.cp.set('section1', 'key1', 'value1')
    lm.cp.set('section1', 'key2', 'value2')
    # test simple key and not matches
    assert(lm.get_value('key1', 'section1', None, False) == 'value1')
    assert(lm.get_value('key2', 'section1', None, False) == 'value2')
    assert(lm.get_value('key3', 'section1', None, False) is None)
    # test regexp keys and not matches

# Generated at 2022-06-13 14:01:09.909664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    hostname = socket.getfqdn()

    c1 = LookupModule()
    c2 = LookupModule()

    # Check read of properties type file
    c1.cp = configparser.ConfigParser(allow_no_value=False)
    c1.cp.optionxform = to_native
    c1.cp.read(['user.properties'])
    assert c1.get_value('name', 'java_properties', '', False) == 'ansible'

    # Check read of ini type file
    #  - no value found in file
    c2.cp = configparser.ConfigParser(allow_no_value=False)
    c2.cp.optionxform = to_native
    c2.cp.read(['empty.ini'])

# Generated at 2022-06-13 14:02:09.868295
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.SafeConfigParser()

    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'mykey1 = myvalue1\n')
    config.write(u'mykey2 = myvalue2\n')
    config.seek(0, os.SEEK_SET)
    l.cp.readfp(config)

    # Test with key mykey1
    val = l.get_value('mykey1', 'section1', 'default', False)
    assert val == 'myvalue1'

    # Test with key mykey2
    val = l.get_value('mykey2', 'section1', 'default', False)

# Generated at 2022-06-13 14:02:16.639738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Can't test on Travis-CI because of missing INI-parseable files on filesystem
    # fail without config
    try:
        LookupModule().run([], variables={}, file="ansible.ini", section=None)
        assert False, "Should have raised AnsibleLookupError"
    except AnsibleLookupError:
        pass

    # fail with garbage
    try:
        LookupModule().run([], variables={}, file="ansible.ini", section=None)
        assert False, "Should have raised AnsibleLookupError"
    except AnsibleLookupError:
        pass

# Generated at 2022-06-13 14:02:25.483523
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    def get_value(key, section, dflt, is_regexp):
        class Test():
            def __init__(self):
                pass
        test = Test()
        test.set_options = lambda x, y: True
        test.get_options = lambda: dict(allow_no_value=True)
        cp = configparser.ConfigParser()
        test.cp = cp
        cp.read_string("""[section1]
value1=a

[section2]
value1=b
value2=c""")
        return test.get_value(key, section, dflt, is_regexp)

    # test for retrieving all values from a section using a regexp
    assert get_value('.*', 'section1', None, True) == ['a']
    # test for retrieving a single value
   