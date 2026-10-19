

# Generated at 2022-06-13 13:52:40.171569
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with a good ini file
    lookup = LookupModule()
    assert lookup.run(['key1', 'key2'], variables={'ansible_lookup_plugin_ini_file': './tests/test.ini'}) == [u'value1', 'value2']

    # Test with multiple values for section1
    assert lookup.run(['key1', 'key3'], variables={'ansible_lookup_plugin_ini_file': './tests/test.ini'}) == [u'value1', 'value3']

    # Test of regexp
    assert lookup.run(['.*'], variables={'ansible_lookup_plugin_ini_file': './tests/test.ini'}, section='Unexisting') == []

# Generated at 2022-06-13 13:52:43.310190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    t = dict(
        string = 'lookup-test-string',
        number = 42
    )
    terms = ['lookup', 'lookup-test-string']
    module.run(terms, variables=t)

# Generated at 2022-06-13 13:52:53.356440
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test without regexp retrieval
    test_Lookup = LookupModule()

    options = {
        'type': 'ini',
        'file': 'default.ini',
        'section': 'section1',
        're': False,
        'encoding': 'utf-8',
        'default': ''
    }
    def run_lookup_return_val(key):
        return test_Lookup.get_value(key, options['section'], options['default'], options['re'])

    # Get values in a section
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.seek(0, os.SEEK_SET)

   

# Generated at 2022-06-13 13:53:03.784316
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # init lookupModule
    lookupModule = LookupModule()
    # init a configParser object
    lookupModule.cp = configparser.ConfigParser()
    # init a StringIO object
    config = StringIO()
    # create a ini file
    config.write(u'[section1] \n')
    config.write(u'key1 = value1 \n')
    config.write(u'key2 = value2 \n')
    config.write(u'\n')
    config.write(u'[section2] \n')
    config.write(u'key3 = value3 \n')
    config.write(u'key4 = value4 \n')
    config.seek(0, os.SEEK_SET)
    # Parse config to create a config parser object
    lookupModule.cp.readfp

# Generated at 2022-06-13 13:53:15.196756
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    lookup_obj = LookupModule()
    lookup_obj.set_loader(loader=loader)
    lookup_obj.set_variable_manager(variable_manager=variable_manager)
    path = lookup_obj._loader.path_dwim_relative('../lookup_plugins/tests/test.ini', None, '', False, [], False)
    config = StringIO()
    config.write(u'[section1]\nuser=yannig\npassword=secret\nhost=localhost\nport=22\n[section2]\nuser=yannig\npassword=secret\nhost=localhost\nport=22\n')

# Generated at 2022-06-13 13:53:22.472397
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.loader_mock import DictDataLoader
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.six.moves import configparser

    plugin = LookupModule()
    mock_loader = DictDataLoader({'test': '''[section1]
key1 = value1
key2 = value2

[section2]
key1 = value1''', 'test2': '''[section1]
key1 = value3
key2 = value4

[section2]
key1 = value1'''})

# Generated at 2022-06-13 13:53:24.672533
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule = modules.lookup_plugins.lookup.LookupModule
    lm = LookupModule()
    re = lm.run([('var=test \s','a=\s','encoding=utf-8','default=test_dflt')], {})
    assert re[0] == 'test '

# Generated at 2022-06-13 13:53:34.791955
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test method run of the LookupModule class.
    '''
    # If file or alternate file have different format, tests must be updated
    FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
    FILE_NAME = 'ansible.ini'
    lookup = LookupModule()
    lookup.set_basedir(FILE_PATH)
    # Section 'all' exists with keys 'key1' and 'key2'
    assert lookup.run(['key1', 'key2', 'key3'], dict(file=FILE_NAME, section='all', default='DEFAULT-VALUE')) == ['value1', 'value2', 'DEFAULT-VALUE']
    # File exists but Section 'section' does not exist

# Generated at 2022-06-13 13:53:44.093769
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import os

    # TODO: integrate with test_lookup_plugin.py for more generic test case.

    test_base = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'test_data')
    test_file = os.path.join(test_base, 'test.ini')
    test_file_with_allow_no_value = os.path.join(test_base, 'test_allow_no_value.ini')
    test_properties = os.path.join(test_base, 'user.properties')

    lookup = LookupModule()

    base = 'foo'
    f = open(test_file, "w")
    f.write(base)
    f.close()

    b = 'bar'

# Generated at 2022-06-13 13:53:53.489010
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_array = []

    test_array.append({
        'terms': ['user'],
        'params': {
            'file': 'test/fixtures/users.ini',
            'section': 'production',
            'default': '',
            're': False,
            'encoding': 'utf-8',
            'case_sensitive': False,
            'type': 'ini',
            'allow_no_value': False
        },
        'data' : u'yperre',
        'show_data' : u"<lookup_plugin.file path='/Users/yperre/devel/ansible/lib/ansible/plugins/lookup/test/fixtures/users.ini'>:2: content",
        'error' : None
    })


# Generated at 2022-06-13 13:54:17.259135
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: un-mock this
    class MockLookupModule(LookupModule):
        def __init__(self):
            self.cp = configparser.RawConfigParser()

        def find_file_in_search_path(self, variables, path_type, file):
            return 'lookup_file'

        def _loader_module_utils_common_collections_compat(self):
            return []

        def _loader_module_utils_six_moves_configparser(self):
            return configparser

        def _loader_module_utils_six_moves_configparser_RawConfigParser(self):
            return configparser.RawConfigParser()


# Generated at 2022-06-13 13:54:25.891542
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:54:34.935750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    file_content = '[global]\na=b\n'
    with open('/tmp/ansible_config_plugin.ini', 'w') as f:
        f.write(file_content)

    params = {'file': 'ansible_config_plugin.ini', 'encoding': 'utf-8', 'section': 'global', 'default': '"not_found"', 're': 'False'}
    terms = ['a']
    result = module.run(terms, {}, **params)
    assert result in [["b"], ["b\n"]]

    os.remove('/tmp/ansible_config_plugin.ini')

# Generated at 2022-06-13 13:54:45.781630
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import StringIO

    # Create StringIO later used to parse ini
    config = StringIO()

    # Special case for java properties
    config.write(u'[java_properties]\n')
    section = 'java_properties'

    # Populate config
    config.write(u'user=admin\n')
    config.write(u'group=admin\n')
    config.write(u'user.name=Yannig\n')
    config.write(u'user.surname=Perre\n')
    config.write(u'user.project=ansible\n')
    config.write(u'user.language=python\n')
    config.write(u'user.language=c\n')

# Generated at 2022-06-13 13:54:58.654381
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    import unittest

    class TestClass(unittest.TestCase):

        lookup_module = LookupModule()
        self.cp = configparser.ConfigParser()

        def test_get_value(self):

            cp = configparser.ConfigParser()
            # Setup a configparser in order to test get_value
            cp.add_section("test")
            cp.set("test", "my_value", "Hello")
            cp.set("test", "my_other_value", "World")

            # Standard test
            self.lookup_module.cp = cp
            value = self.lookup_module.get_value("my_value", "test", "", False)
            self.assertEqual("Hello", value)

            # Error case

# Generated at 2022-06-13 13:54:59.617352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "A test is required"

# Generated at 2022-06-13 13:55:07.527261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.parsing.dataloader
    import ansible.vars.manager

    class MockLookupBase(LookupBase):
        def __init__(self, variable_manager=None):
            self.variable_manager = variable_manager

    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.manager.VariableManager()
    lookup_base = MockLookupBase(variable_manager)
    terms = ['user1']

    params = {'file': 'test_ini.ini', 'section': 'user_list', 'type': 'ini', 'default': '', 're': False,
              'encoding': 'utf-8', 'case_sensitive': False}

    lookup_plugin = LookupModule(loader=loader)
    lookup_plugin.set_

# Generated at 2022-06-13 13:55:18.458981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

# Generated at 2022-06-13 13:55:24.609023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    config = StringIO()
    config.write(u'[integration]\nuser=yperre\n')
    config.write(u'[production]\nuser=yperre\n')
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()
    cp.readfp(config)
    lookup_module.cp = cp
    assert lookup_module.get_value('user', 'integration', None) == 'yperre'
    assert lookup_module.get_value('user', 'production', None) == 'yperre'

    lookup_module = LookupModule()
    config = StringIO()
    config.write(u'[integration]\nuser=yperre\n')

# Generated at 2022-06-13 13:55:38.125449
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, enable_plugins=False)
    variable_manager.set_inventory(inventory)
    testobj = LookupModule()
    options = {
        'type': 'ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False
    }

# Generated at 2022-06-13 13:55:56.757775
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # set up a class Mock
    class Mock(object):
        '''
        Create a class with two default methods
        - load_file
        - find_file_in_search_path
        '''

        def load_file(self):
            '''
            Class method load_file
            return an empty string
            '''
            return ''

        def find_file_in_search_path(self, variables, term, paramvals_file):
            '''
            Class method find_file_in_search_path
            return the value of var paramvals_file
            '''
            return paramvals_file

    # set up a class Mock

# Generated at 2022-06-13 13:56:06.485938
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with a non existing file
    lookup = LookupModule()
    with pytest.raises(AnsibleLookupError) as e:
        lookup.run([], **{"file": "no_file.ini", "section": "section1"})
        assert e.args[0] == "Could not locate file in lookup: no_file.ini"

    # Test with an existing file but a key not in the file
    from ansible.utils.path import unfrackpath
    path = unfrackpath("../../../../test/integration/lookup_plugins/")
    lookup = LookupModule()
    lookup.run([], **{"file": path + "/ini/test.ini", "section": "section1"})
    assert e.args[0] == "Could not locate file in lookup: no_file.ini"

    #

# Generated at 2022-06-13 13:56:16.386020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    test_ini_file = "test.ini"
    test_ini_file_content = """[section1]
key_1=value_1
key_2=value_2
key_3=value_3

[section2]
key_1=value_1
key_2=value_2
key_3=value_3
"""
    with open(test_ini_file, "w") as file_handler:
        file_handler.write(test_ini_file_content)
    # Test: get a single key in section1
    term = 'key_1'
    # parameters specified
    params = _parse_params(term, {'section': 'section1', 'file': test_ini_file})
    assert params[0] == 'section1'
    assert params[1]

# Generated at 2022-06-13 13:56:27.001665
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    cp.add_section('section')
    cp.set('section', 'key1', 'value11')
    cp.set('section', 'key2', 'value12')
    cp.set('section', 'key3', 'value13')

    lm = LookupModule()
    lm.cp = cp

    assert lm.get_value('key1', 'section', None, False) == 'value11'
    assert lm.get_value('key2', 'section', None, False) == 'value12'
    assert lm.get_value('key4', 'section', 'default', False) == 'default'
    assert lm.get_value('key1', 'section', 'value11', True) == ['value11']

# Generated at 2022-06-13 13:56:37.785694
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Fake class configparser.SafeConfigParser which contains two sections name and age.
    class Fake_SafeConfigParser:

        def items(self, section):
            config = {
                'name': ['John', 'Julia', 'Bil'],
                'age': ['23', '27', '72']
            }
            return config[section]

        def get(self, section, key):
            config = {
                'name': {'John': 'Marty', 'Julia': 'Marty', 'Bil': 'Marty'},
                'age': {'23': 'Marty', '27': 'Marty', '72': 'Marty'}
            }
            return config[section][key]

    # Fake class LookupModule

# Generated at 2022-06-13 13:56:42.496218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    machine_file = 'app.ini'
    terms = ['type=full', 'machine=192.168.1.1', 'file=%s' % machine_file]
    with open(machine_file, 'w') as fd:
        fd.write('[global]\ntype=full\nname=redhat7\n')
    result = lookup.run(terms)
    assert result == ['full']
    assert os.path.isfile(machine_file)
    os.remove(machine_file)

# Generated at 2022-06-13 13:56:53.104246
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import tempfile

    lookup = LookupModule()

    # Create the class property
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO(u'''[section1]

                                # comment
                                a=1
                                b=2
                                c=3

                                [section2]
                                d=4
                                e=5
                                f=6
                                '''))

    # Test the get_value method
    terms = ['foo', 'bar']
    section = 'section1'
    dflt = 'NA'
    result = lookup.get_value(terms[0], section, dflt, False)
    assert result == dflt
    result = lookup.get_value(terms[0], section, dflt, True)

# Generated at 2022-06-13 13:57:03.767503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import unittest

    TEST_VERSION_GROUP_NAME = "version"
    TEST_VERSION_GROUP_KEY = "number"
    TEST_VERSION_GROUP_VALUE = "1.0"
    TEST_SECTION_NAME = "section"
    TEST_SECTION_KEY = "key"
    TEST_SECTION_VALUE = "value"
    TEST_FILE_NAME = "test.ini"

# Generated at 2022-06-13 13:57:05.597207
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()




# Generated at 2022-06-13 13:57:08.649663
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    ret = lookup_module.run(['.*'], variables=None, **{'allow_none': False, 'encoding': 'utf-8', 'default': '', 'file': 'ansible.ini', 'section': 'global', 're': True, 'case_sensitive': False})
    print("test_LookupModule_run = {}".format(ret))

# Generated at 2022-06-13 13:57:42.594965
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    conf = configparser.RawConfigParser()
    conf_file = StringIO()
    conf_file.write(u"""
[section1]
key1=value1
key2=value2
key3=value3
[section2]
key4=value4
key5=value5
    """)
    conf_file.seek(0, os.SEEK_SET)
    conf.readfp(conf_file)
    lookup_module.cp = conf
    assert lookup_module.get_value('key1', 'section1', '', False) ==  'value1'
    assert lookup_module.get_value('.*', 'section1', '', True) == ['value1', 'value2', 'value3']

# Generated at 2022-06-13 13:57:55.228954
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    section = 'foo'
    key = 'bar'
    value = 'baz'
    dflt = 'a default value'
    config = """
[{section}]
{key} = {value}
""".format(section=section, key=key, value=value)

    cp = configparser.ConfigParser()
    cp.readfp(StringIO(config))

    lm = LookupModule()
    lm.cp = cp
    assert lm.get_value(key, section, dflt, False) == value
    assert lm.get_value(key, section, dflt, True) == value
    assert lm.get_value('any key', section, dflt, False) == dflt
    assert lm.get_value('any key', section, dflt, True) == dflt

# Generated at 2022-06-13 13:58:04.742807
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for method lookup_ini of class LookupModule with no section
    def lookup_ini(self, key, section=None, dflt=''):
        return self.get_value(key, section, dflt, False)

    # Fake that the lookup is being used as a Jinja 2 filter
    module = LookupModule()
    setattr(module, "lookup_ini", lookup_ini)
    setattr(module, "_options", {})
    setattr(module, "cp", None)
    setattr(module, "_templar", None)

    # Add fake data to lookup module

# Generated at 2022-06-13 13:58:06.190246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, 'No tests for this plugin yet.'

# Generated at 2022-06-13 13:58:15.729864
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    module = LookupModule()
    # TODO: not the most unit test
    res = module.run([], dict(file="../lookup_plugins/files/mikasa.ini", section="default"))
    assert res[0] == "red"
    assert res[1] == "1942"
    assert res[2] == "Hood"
    assert res[3] == "Prince of Wales"

# Generated at 2022-06-13 13:58:24.350751
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # We define a ini configuration file
    ini = StringIO()
    ini.write(u'''[section1]
key1=value1
key2=value2

[section2]
key3=value3
key4=value4''')
    ini.seek(0, os.SEEK_SET)

    # We define a properties configuration file
    properties = StringIO()
    properties.write(u'user.name=My Name')
    properties.write(u'user.organization=My Organisation')
    properties.seek(0, os.SEEK_SET)

    # Retrieve List of keys without section
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(properties)

# Generated at 2022-06-13 13:58:34.944839
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    cp.add_section('section1')
    cp.set('section1', 'key1', 'value1')
    cp.set('section1', 'key2', 'value2')
    assert LookupModule(None, cp).get_value('key1', 'section1', 'defaultvalue', False) == 'value1'
    assert LookupModule(None, cp).get_value('key1', 'section1', 'defaultvalue', True) == ['value1']
    assert LookupModule(None, cp).get_value('.*', 'section1', 'defaultvalue', True) == ['value1', 'value2']



# Generated at 2022-06-13 13:58:45.829171
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:58:57.559394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    test_LookupModule_run: test run method with different case (ini or
    properties) and combined options

    """

    # Load parameters
    module_params = {
        'file': 'test.ini',
        'section': 'section1',
        'default': '',
        'encoding': 'utf-8',
        '_original_basename': 'test.ini',
        're': False,
    }
    # Create LookupModule object
    l = LookupModule()

    # Test with an existing section
    assert l.run(
        ['key1'],
        module_params,
        type='ini') == ['value1']
    assert l.run(
        ['key2'],
        module_params,
        section='section2') == ['value2'], "wrong section"
    #

# Generated at 2022-06-13 13:59:03.465798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    module = LookupModule(loader=DataLoader())
    terms = [ 'db:user', 'db:password' ]
    var = { 'file': '../../../test/integration/lookup/test.ini',
            'section': 'db' }
    assert module.run(terms, var) == [ 'test', 'test' ]

# Generated at 2022-06-13 14:00:02.909114
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    lm = LookupModule()
    cp.readfp(StringIO('[sections]\nvalue=test\ntest="a test"\n'))

    lm.cp = cp

    assert lm.get_value('doesnotexist', 'sections', None, False) == None
    assert lm.get_value('doesnotexist', 'sections', 'dflt', False) == 'dflt'
    assert lm.get_value('value', 'sections', 'dflt', False) == 'test'
    assert lm.get_value('test', 'sections', 'dflt', False) == 'a test'
    assert lm.get_value('value', 'sections', 'dflt', True) == ['test', 'test']

# Generated at 2022-06-13 14:00:10.847973
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleLookupError, AnsibleOptionsError

    config = StringIO()
    config.write(u'[dummy]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'\n')
    config.write(u'[dummy2]\n')
    config.write(u'key3=value3\n')
    config.write(u'key4=value4\n')
    config.seek(0, os.SEEK_SET)

    lm = LookupModule()
    cp = configparser.ConfigParser()
    cp.readfp(config)
    lm.cp = cp


# Generated at 2022-06-13 14:00:19.966268
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    import ansible.plugins.loader as plugin_loader

    # Needed to get LookupModule
    lookup_loader = plugin_loader.LookupModule()

    config = """
[faust]
gretchen = Faust_und_Gretchen
faust = Faust
"""

    # properties file
    properties = """
user.name = Jimbo
user.password = gretchen
"""

    # Run test for config file
    lookup = lookup_loader.get('ini', loader=None, templar=None, shared_loader_obj=None)
    ret = lookup.run([u'gretchen', 'gender'], variables={},
                     file="test.cfg",
                     section="faust",
                     default="",
                     re=False,
                     encoding="utf-8")

# Generated at 2022-06-13 14:00:34.776178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(LookupModule(),
                            ["user", "passwd"],
                            variables={},
                            file="test.ini",
                            section="dummy") == ["root", "secret"]
    assert LookupModule.run(LookupModule(),
                            ["user", "passwd"],
                            variables={},
                            file="empty.ini",
                            section="dummy",
                            default="N/A") == ["N/A", "N/A"]
    assert LookupModule.run(LookupModule(),
                            ["user", "passwd"],
                            variables={},
                            file="empty.ini",
                            section="dummy") == ["", ""]

# Generated at 2022-06-13 14:00:35.323945
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:00:42.791070
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    from ansible.module_utils.six.moves import StringIO
    import configparser

    # Create configparser object
    cp = configparser.ConfigParser()
    # Create stream
    config = StringIO()
    # Write on config
    config.write(u'[section1]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'key3=value3\n')
    config.write(u'key4=value4\n')
    config.write(u'key5=value5\n')
    config.write(u'key6=value6\n')
    config.write(u'key7=value7\n')
    config.write(u'key8=value8\n')

# Generated at 2022-06-13 14:00:49.385347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # LookupModule._options = {'file': 'test.ini', 'section': 'section1', 'encoding': 'utf-8', 'case_sensitive': False}
    terms = ['k1', 'k2=v2', 'key1=value1 key2=value2', 'k3=v3 key4=value4']
    for term in terms:
        module.run([term])


# Generated at 2022-06-13 14:00:50.709349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Write unit test LookupModule.run
    pass

# Generated at 2022-06-13 14:00:57.635798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # unit_tests/test_lookup_ini.ini
    lookup.cp = configparser.RawConfigParser()
    lookup.cp.read('unit_tests/test_lookup_ini.ini')
    assert lookup.run([
        'test_key=test_value section=test_section',
        'test_key2 test_section2'],
        variables=None,
        file='test_file',
        section='test_section',
        re=False,
        encoding='test_encoding',
        default='test_default') == ['test_value', 'test_value2']

    # unit_tests/test_lookup_ini.ini
    lookup.cp = configparser.RawConfigParser()
    lookup.cp.read('unit_tests/test_lookup_ini.ini')


# Generated at 2022-06-13 14:01:07.162820
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six.moves import configparser

    # Mock the get_value method
    cp = configparser.ConfigParser()
    cp.add_section("global")
    cp.set("global", "a", "A")
    cp.set("global", "b", "B")
    cp.set("global", "c", "C")
    cp.add_section("section1")
    cp.set("section1", "a", "A1")
    cp.set("section1", "b", "B1")
    dummy_module = LookupModule()
    dummy_module.cp = cp
    dummy_module.get_value = lambda x, y, z, w: cp.get(y, x)

    # No section =>