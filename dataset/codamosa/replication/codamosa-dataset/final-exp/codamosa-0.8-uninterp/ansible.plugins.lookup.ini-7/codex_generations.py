

# Generated at 2022-06-13 13:52:38.969104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._loader = 'fake'
    l._templar = 'fake'
    l._templar.available_variables = {'inventory_dir': 'fake',
                                      'inventory_file': 'fake',
                                      'playbook_dir': 'fake'}
    l.find_file_in_search_path = lambda x, y, z: 'fake_path'
    l._loader._get_file_contents = lambda x: ('[test_section]\n'
                                              'test_instruction=instruction\n'
                                              'another_test_instruction=another_instruction\n'
                                              'yet_another_test_instruction=yet_another_instruction',
                                              'fake')
    # Test 1
    # Check if the method run

# Generated at 2022-06-13 13:52:47.625668
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import pdb
    input = [
        'user',
        'email',
        'name',
        'allow',
    ]
    section = 'Global'
    default = 'default'
    is_regexp = False

    config = LookupModule()

    tmp = config.get_value(input[0], section, default, is_regexp)
    assert tmp == 'admin', \
        "Wrong value in get_value 'user', expected 'admin' but was '%s'" \
            % tmp

    tmp = config.get_value(input[1], section, default, is_regexp)
    assert tmp == 'admin@domain.com', \
        "Wrong value in get_value 'email', expected 'admin@domain.com' but was '%s'" \
            % tmp


# Generated at 2022-06-13 13:53:00.289192
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    obj = LookupModule()
    assert obj.get_value("test", "section1", "", False) == 'test'
    assert obj.get_value("test", "section2", "", False) == 'test'
    assert obj.get_value("test", "section1", "", True) == []
    assert obj.get_value("test", "section2", "", True) == ['value', 'value1']
    assert obj.get_value("test", "section3", "", False) == 'value'
    assert obj.get_value("test", "section3", "", True) == ['value', 'value1']
    assert obj.get_value("teste", "section3", "", True) == []
    assert obj.get_value("test", "section4", "", True) == []

# Generated at 2022-06-13 13:53:11.830923
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test simple ini file
    terms = ['user', 'pwd']
    paramvals = {
        'file': 'users.ini',
        'section': 'integration',
        'default': '',
        'case_sensitive': False,
        'allow_none': False
    }
    lookup = LookupModule()
    results = lookup.run(terms, paramvals=paramvals)
    assert results[0] == 'yannig', results[0]
    assert results[1] == 'mypwd', results[1]

    # Test java properties file
    terms = ['user.name']
    paramvals = {
        'default': '',
        'type': 'properties',
        'file': 'user.properties',
        'case_sensitive': False,
        'allow_none': False
    }

# Generated at 2022-06-13 13:53:20.412502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: move to appropriate place when a structure is found
    import unittest

    class TestLookupModule(unittest.TestCase):
        def test_run(self):
            test_file = "test.ini"
            with open(test_file, "w") as f:
                f.write("""
[section1]
key1 = value1
key2 = value2

[section2]
key3 = value3
key4 = value4 """)

            lookup = LookupModule()
            ret = lookup.run(['key1', 'key3'], {}, file=test_file, section="section1")
            self.assertEqual(ret, ['value1'])

            ret = lookup.run(['key1', 'key3'], {}, file=test_file, section="section2")
           

# Generated at 2022-06-13 13:53:29.013398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # test input type
    assert type(lm.run(terms=['foo'])) == list
    assert type(lm.run(terms=['foo'])[0]) == unicode

    # test empty reference
    assert lm.run(terms=['foo']) == ['']

    # test config file
    terms = 'foo=file=ansible.ini section=global'
    assert lm.run(terms=terms.split()) == ['bar']

# Generated at 2022-06-13 13:53:36.094735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup=LookupModule()
    lookup.cp = configparser.ConfigParser(allow_no_value=True)
    term = "user"
    config = StringIO()
    config.write(u'[java_properties]\nuser=\n')
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)
    params = dict(file='file', type='properties', section='section', default='', re=False)
    ret = lookup.get_value(key=term, section='java_properties', dflt=params['default'], is_regexp=params['re'])
    assert ret == ''

# Generated at 2022-06-13 13:53:44.900454
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import StringIO
    # Create cfg_file and data to mock the cfg file
    cfg_file = StringIO()
    cfg_file.write(u'[section1]\nalpha=1\nbeta=2\n[section2]\nalpha=3\nbeta=4')
    cfg_file.seek(0, os.SEEK_SET)
    lookup_module = LookupModule()
    # Create a test configParser object
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(cfg_file)
    # Call get_value function
    # Get the value of an existing key
    assert lookup_module.get_value('alpha', 'section1', '', False)

# Generated at 2022-06-13 13:53:54.721204
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    term = "port"
    paramvals = {
        "file": "tests/ansible/test_lookup_plugin.ini",
        "section": "server",
        "default": "22",
        "re": "False",
        "type": "ini",
    }

    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.read('tests/ansible/test_lookup_plugin.ini')
    lookup_module.cp.optionxform = str

    result_with_section = lookup_module.get_value(term, paramvals['section'], paramvals['default'], paramvals['re'])

# Generated at 2022-06-13 13:54:06.001654
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Mocking
    import ConfigParser
    ConfigParser.get = lambda self, section, key: 'OK'
    ConfigParser.items = lambda self, section: [('abc', 'abc'), ('def', 'def')]

    # Method to test
    l = LookupModule()
    l.term = 'myterm'
    l.cp = ConfigParser.ConfigParser()

    # Test regexp
    ret = l.get_value('abc', 'section', 'unknown', True)
    assert ret == ['abc']
    ret = l.get_value('ab', 'section', 'unknown', True)
    assert ret == []

    # Test not regexp
    ret = l.get_value('abc', 'section', 'unknown', False)
    assert ret == 'OK'

# Generated at 2022-06-13 13:54:26.344184
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    key = 'user'
    section = 'integration'
    dflt = 'root'
    is_regexp = False
    lookup.cp = configparser.ConfigParser()
    # Create StringIO later used to parse ini
    config = StringIO()
    # Special case for java properties
    paramvals = {'section': section, 'type': 'properties'}
    config.write(u'[{section}]\n'.format(section=section))
    config.write(u'{key}=testuser\n'.format(key=key))
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)
    value = lookup.get_value(key, section, dflt, is_regexp)
    assert value == 'testuser'

# Generated at 2022-06-13 13:54:37.073048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Change here the values in order to test different params
    test_file = 'ansible.ini'
    test_key = 'key1'
    test_section = 'section1'
    test_default = None
    test_encoding = 'utf-8'
    test_re = False
    test_module_path = os.path.dirname(os.path.realpath(__file__))
    test_params = {'file': test_file, 'section': test_section, 'default': test_default,
                   'encoding': test_encoding, 're': test_re}
    # Create test class
    test_class = LookupModule()
    # Process test
    test_result = test_class.run([test_key], test_params, variables={'files': test_module_path})
    # value of

# Generated at 2022-06-13 13:54:47.141015
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import tempfile

    # Return a unique string
    def unique():
        return str(tempfile.mkstemp())

    # Create an unittest for test LookupModule class
    class LookupModuleTest(unittest.TestCase):

        # Return a content from a file
        def readFile(self, fileName):
            openedFile = open(fileName)
            fileContent = openedFile.read()
            openedFile.close()
            return fileContent

        # Return a temporary file name
        def createFile(self, content):
            tmpFile = unique()
            openedFile = open(tmpFile, 'w')
            openedFile.write(content)
            openedFile.close()
            return tmpFile


        # Return an instance of LookupModule class
        def lookup_module(self):
            return Look

# Generated at 2022-06-13 13:54:52.142642
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['key1', 'key2']
    variables = dict()
    kwargs = dict(file='file', section='section')
    module.run(terms=terms, variables=variables, **kwargs)

# Generated at 2022-06-13 13:55:03.373526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['key=value', 'section=first'], None, file='ini.ini')[0] == 'string'
    assert lm.run(['key', 'section=first'], None, file='ini.ini')[0] == 'string'
    assert lm.run(['key', 'section=second'], None, file='ini.ini')[0] == 'string'
    assert lm.run(['key', 'section=second', 'default=yeah'], None, file='ini.ini')[0] == 'string'
    assert lm.run(['key', 'section=third'], None, file='ini.ini')[0] == ''

# Generated at 2022-06-13 13:55:15.698510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Prepare tests
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=[]))

# Generated at 2022-06-13 13:55:23.013838
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:55:31.109518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # Create StringIO later used to parse ini
    config = StringIO()

    # Special case for java properties
    config.write(u'[java_properties]\n')
    config.write(u'key1=val1\n')
    config.write(u'key2=val2\n')

    config.seek(0, os.SEEK_SET)

    lm.cp.readfp(config)

    # Return a list
    assert type(lm.get_value('key1', 'java_properties', '', False)) is list
    # Retrieve a single value
    assert lm.get_value('key1', 'java_properties', '', False) == ['val1']
    # Retrieve all values using regexp

# Generated at 2022-06-13 13:55:43.622576
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    class TestClass(object):
        def __init__(self, value):
            self.value = value

    ref = defaultdict(lambda: TestClass('default_value'))
    ref['section'] = TestClass(defaultdict(lambda: TestClass('default_value')))
    ref['section'].value['key'] = TestClass('value')
    ref['section'].value['key_re'] = TestClass('value_re')
    ref['section'].value['key_re_default'] = TestClass('value_re_default')

    l = LookupModule()
    l.cp = ref

    assert l.get_value('key', 'section', 'default', False) == 'value'
    assert l.get_value('key', 'section', 'default', True) == ['value']

# Generated at 2022-06-13 13:55:51.954968
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initialization
    lm = LookupModule()

    # creation of a configParser
    cp = configparser.ConfigParser()

    # content of the file
    config = StringIO()
    config.write(u'[global]\n')
    config.write(u'user = root\n')
    config.write(u'password = password\n')
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)

    # test of the method get_value
    res = lm.get_value('user', 'global', '', False)
    assert res == 'root'

    # test of the method run
    terms = ['user']
    terms.append('user')
    res = lm.run(terms)
    assert res[0] == 'root'

# Generated at 2022-06-13 13:56:15.308258
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import pytest
    lookupModule = LookupModule()
    config = configparser.ConfigParser()
    config.add_section('Section1')
    config.set('Section1', 'user', 'Fred')
    config.add_section('Section2')
    config.set('Section2', 'user', 'Foo')
    lookupModule.cp = config

    # check lookup of a key
    assert lookupModule.get_value(key='user', section='Section1', dflt=None, is_regexp=False) == 'Fred'
    # check lookup of a key with default value
    assert lookupModule.get_value(key='password', section='Section1', dflt='foobar', is_regexp=False) == 'foobar'
    # check lookup of multiple keys using regexp

# Generated at 2022-06-13 13:56:26.320058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test(terms, variables, **kwarg):
        res = LookupModule().run(terms, variables, **kwarg)
        return res
    # INI file
    config = StringIO()
    config.write(u'[section1]')
    config.write(u'\nkey1=value1')
    config.write(u'\nkey2=value2')
    config.write(u'\nkey3=')
    config.write(u'\n\n[section2]')
    config.write(u'\nkey4=value4')
    config.write(u'\nkey5=value5')
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()
    cp.readfp(config)

# Generated at 2022-06-13 13:56:37.711117
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic

    '''
    Create a mock class of type LookupModule
    '''
    class MockLookupModule(LookupModule):
        def __init__(self, *args, **kwargs):
            super(MockLookupModule, self).__init__(*args, **kwargs)

        def run(self, *args, **kwargs):
            return super(MockLookupModule, self).run(*args, **kwargs)

        def get_value(self, *args, **kwargs):
            return super(MockLookupModule, self).get_value(*args, **kwargs)

    '''
    Test the run method with type ini, section and re
    '''
    lookup_module = MockLookupModule()

# Generated at 2022-06-13 13:56:44.506693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 13:56:48.379121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['user',
             'username=root',
             'username = root',
             'username= root',
             'username =root',
             'username= root '
            ]
    for term in terms:
        l = LookupModule()
        l.set_options({'file':'users.ini'})
        ret = l.run([term])
        assert ret[0] == 'root'

# Generated at 2022-06-13 13:56:56.172483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Path
    path = os.path.dirname(__file__)

    # Lookup module
    lm = LookupModule()

    # INI file
    ini_file = os.path.join(path, "test.ini")

    # Properties file
    properties_file = os.path.join(path, "test.properties")

    # Test run
    # Ini file, section 'section1', key 'key1'
    result = lm.run([
        "key1",
        "key2",
        "key1",
    ], {'_fqpn': ini_file, '_filesystem_path': ini_file})

    assert result == ["value1", "value2", "value1"]

    # Properties file, no section, key 'key1'

# Generated at 2022-06-13 13:57:04.981242
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create plugin object LookupModule
    obj = LookupModule()

    # Create variables use in unit test
    class Options:
        def __init__(self, allow_no_value, default, file, section, type):
            self.allow_no_value = allow_no_value
            self.default = default
            self.file = file
            self.section = section
            self.type = type

    class Variable:
        def __init__(self, allow_no_value, default, file, section, type, terms):
            self.allow_no_value = allow_no_value
            self.default = default
            self.file = file
            self.section = section
            self.type = type
            self.terms = terms

    class Term:
        def __init__(self, value):
            self.value = value

# Generated at 2022-06-13 13:57:15.480194
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test to verify results of method LookupModule.run()'''

    # Initialization
    mylookup = LookupModule()

    # Test 1 : a simple lookup
    myterms = [u'user']
    myvariables = {u'ansible_user': u'ansible'}
    mykwargs = {u'file': u'test.ini', u'section': u'user_section'}

    myresult = mylookup.run(myterms, myvariables, **mykwargs)
    assert myresult == [u'ansible_user']

    # Test 2 : a lookup included options
    myterms = [u'user']
    myvariables = {u'ansible_user': u'ansible'}

# Generated at 2022-06-13 13:57:28.217886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io

    input_file = io.StringIO(
        u'''
        [section1]
        key1=value1
        key2=value2

        [section2]
        key3=value3
        '''
    )

    # Case not in section
    terms = [u'section2.key2']
    paramvals = {
        'file': '/path/to/ini_file',
        'section': 'section2',
        'default': None,
        're': False,
        'encoding': 'utf-8',
        'case_sensitive': False,
        'type': None,
    }
    lm = LookupModule()
    lm.cp.readfp(input_file)
    assert lm.run(terms, var_options=paramvals) == [None]

    #

# Generated at 2022-06-13 13:57:39.739486
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import string_types
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section("global")
    lookup.cp.set("global", "user", "mike")
    lookup.cp.add_section("integration")
    lookup.cp.set("integration", "user", "yannig")
    lookup.cp.add_section("production")
    lookup.cp.set("production", "user", "jane")

# Generated at 2022-06-13 13:58:20.299258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

    # Create a temporary INI-style file with the data
    ini_file = u"""
# Ansible managed

[defaults]
log_path=/tmp/ansible.log
nocows = 1

[developer]
name = Yannig
favorite_editor = emacs

[company]
name = Ansible
location = San Francisco
"""


# Generated at 2022-06-13 13:58:33.960389
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.RawConfigParser()
    lookup_module.cp.optionxform = lambda x: x
    lookup_module.cp.add_section("test")
    lookup_module.cp.set("test", "key1", "value1")
    lookup_module.cp.set("test", "key2", "value2")
    lookup_module.cp.set("test", "key3", "value3")
    lookup_module.cp.set("test", "key4", "value4")
    lookup_module.cp.set("test", "key5", "value5")
    assert lookup_module.get_value("key1", "test", "", False) == "value1"

# Generated at 2022-06-13 13:58:45.231961
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import os.path
    from ansible.parsing.vault import VaultLib

    path = os.path.join(os.path.dirname(__file__), 'test.ini')

    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.read(path)

    # Return a list of values when a regex pattern is supplied
    assert l.get_value('^bar', 'foobar', 'default', True) == ['1', '2', '3']

    # Return a single value when a regex pattern isn't supplied
    assert l.get_value('bar', 'foobar', 'default', False) == '1'

    # Return the value for a key which is not in the ini file

# Generated at 2022-06-13 13:58:55.493711
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import yaml
    test_terms = yaml.load("""
        - key1
        - key2
        - key3
        - key4:
            type: properties
            file: test.properties
            default: default_value
        - 'key5 a=b c=d'
        - 'key6 a=b c=d'
        - 'key7 a=b c=d'
        - key8:
            file: test.properties
            section: java_properties
            type: properties
            default: default_value
    """)
    expected_results = [
        "value1",
        "value2",
        "value3",
        "value4",
        "value5",
        "value6",
        "value7",
        "value8"
    ]

    # Create temporary file to test ini

# Generated at 2022-06-13 13:59:02.872145
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    class LookupModuleTest(LookupModule):

        def run(self, terms, variables=None, **kwargs):
            return

    # Test regexp
    lookup = LookupModuleTest()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section')
    lookup.cp.set('section', 'key', 'value')
    assert lookup.get_value('key', 'section', '', False) == 'value'
    assert lookup.get_value('key', 'section', '', True) == ['value']

    lookup.cp.set('section', 'key2', 'value2')
    assert lookup.get_value('key', 'section', '', True) == ['value']

    assert lookup.get_value('ke', 'section', '', True) == ['value', 'value2']

    #

# Generated at 2022-06-13 13:59:12.182287
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    test_LookupModule = LookupModule()
    test_LookupModule.cp = configparser.ConfigParser()
    test_LookupModule.get_value = lambda key, section, default, is_regexp: 'under_test'
    terms = ['test']
    variables = {'hostvars': {'testhost': {'docker_compose_dir': './test'}}}
    kwargs = {'file': 'testfile', 'default': None, 're': False, 'section': 'testsection', 'type': 'testtype'}

    # Act
    result = test_LookupModule.run(terms, variables=variables, **kwargs)

    # Assert
    assert result == ['under_test']

# Generated at 2022-06-13 13:59:20.072032
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test the LookupModule.run() method.
    """
    #TODO: better test case on lookupModule.run() with a file as parameter
    lookupModule = LookupModule()
    params = {
        'encoding': 'utf-8', 'file': 'ansible.ini', 'section': 'global',
        'default': '', 're': False
    }
    term = 'user'
    exp = ['yperre']
    res = lookupModule.run([term], params)
    assert res == exp, 'res: {}, exp: {}'.format(res, exp)

# Generated at 2022-06-13 13:59:30.109596
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()

    config = StringIO()
    config.write(u'[section]\na=1\nb=2\n')
    config.seek(0, os.SEEK_SET)

    cp = configparser.ConfigParser()
    cp.readfp(config)

    lookup.cp = cp

    assert lookup.get_value('a', 'section', None, False) == "1"
    assert lookup.get_value('c', 'section', None, False) is None
    assert lookup.get_value('a', 'section', 'default', False) == "1"
    assert lookup.get_value('c', 'section', 'default', False) == "default"
    assert lookup.get_value('a', 'section', 'default', True) == '1'

# Generated at 2022-06-13 13:59:37.584289
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import configparser

    class MockLookupModule(LookupModule):

        def __init__(self):
            # create a configparser object which contains ini file content
            self.cp = configparser.ConfigParser()
            self.cp.readfp(StringIO(u'[section]\nkey=value'))

    mock = MockLookupModule()

    # test with is_regexp = True
    result = mock.get_value('key', 'section', None, True)
    assert result == ['value']

    # test with is_regexp = False
    result = mock.get_value('key', 'section', None, False)
    assert result == 'value'

    # test with default value
    result = mock.get_value('other_key', 'section', 'test', False)
    assert result == 'test'

# Generated at 2022-06-13 13:59:47.371097
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()

    terms = []
    variables = {}
    kwargs = {}

    # Test with a key and a section
    lookup.cp.add_section('Credentials')
    lookup.cp.set('Credentials', 'user', 'testuser')
    lookup.cp.set('Credentials', 'password', 'p4ssw0rd')
    result = lookup.run(terms, variables, file='test.ini', section='Credentials', key='user')
    assert result == ['testuser']

    # Test with a key, a section and default value
    result = lookup.run(terms, variables, file='test.ini', section='Credentials', key='key_not_existed', default='default_value')

# Generated at 2022-06-13 14:01:04.904168
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.plugins.lookup.ini import LookupModule

    # Test for method get_value for one key and one value
    key = 'project'
    section = 'global'
    dflt = ''
    is_regexp = False
    config_content = """[%s]
    project = ProjA
    version = 0.1
    """ % section

    lk = LookupModule()
    config = StringIO(config_content)
    lk.cp.readfp(config)
    assert lk.get_value(key, section, dflt, is_regexp) == "ProjA"

    # Test for method get_value for one key and more values
    key = 'project'
    section = 'global'
    dflt = ''
    is_regexp = False
    config_content

# Generated at 2022-06-13 14:01:06.549914
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(True)


# Generated at 2022-06-13 14:01:16.191858
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create Dummy Ansible modules
    class DummyAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    class DummyAnsibleVars(dict):
        def __init__(self):
            self.params = None

    # Create instance of LookupModule
    lm = LookupModule()

    # Create parameter dict
    params = {
        'file': 'test/test.ini',
        'type': 'ini',
        'section': 'section1',
        'default': 'default_value',
        'encoding': 'utf-8',
        'case_sensitive': False
    }

    # Create dummy Ansible modules
    lm.set_options(var_options=None, direct=params)

    # create dummy Ansible variables
    vars = Dummy

# Generated at 2022-06-13 14:01:27.459617
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test LookupModule.get_value with no parameter
    lookup_module = LookupModule()
    lookup_module.cp = configparser.RawConfigParser()
    lookup_module.cp.add_section('test_section')
    lookup_module.cp.set('test_section', 'test_key', 'test_value')
    assert lookup_module.get_value('test_key', 'test_section', None, False) == 'test_value'
    assert lookup_module.get_value('test_key', 'test_section', None, True) == ['test_value']
    assert lookup_module.get_value('non_existent_key', 'test_section', None, True) == None

    # Test LookupModule.get_value with default value

# Generated at 2022-06-13 14:01:38.097828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Retrieve value of key user in section integration from file users.ini
    import os
    import sys
    import tempfile
    import json

    lookup = LookupModule()
    lookup._options = {'file': "users.ini"}
    lookup.run([])
    # This is a hack because of Loader is not available in this context
    lookup.set_loader(None)
    lookup._colorize = lambda x: x
    lookup.basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(b"[integration]\nuser=integration")
    tmp.flush()
    lookup.find_

# Generated at 2022-06-13 14:01:49.035406
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #################################################################
    #
    # Test case 1: List of keys provided
    #  Example of ini file:
    #       [section1]
    #       key1=value1
    #       key2=value2
    #       key3=value3
    #
    #  Expected result:
    #       Value of key1, value of key2 and value of key3
    #
    #################################################################

    terms = ['key1', 'key2', 'key3']
    cp_obj = configparser.RawConfigParser()
    cp_obj.add_section('section1')
    cp_obj.set('section1', 'key1', 'value1')
    cp_obj.set('section1', 'key2', 'value2')
    cp_obj.set('section1', 'key3', 'value3')

# Generated at 2022-06-13 14:01:58.589573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.ini import LookupModule

    contents = u'\n'.join(('[global]', 'foo=bar', 'baz=', 'boo=123', 'foo=bar2', '', '', '[section1]', 'foo=bar3'))
    file_content = {'test.ini': contents}
    loader = DictDataLoader(file_content)
    lookup = LookupModule(loader=loader)
    params = {'type': 'ini', '_terms': ['foo', 'boo'], 'section': 'global', 'encoding': 'utf-8', 'default': '', 'case_sensitive': False, 'allow_no_value': False}
    ret = lookup.run(terms=['foo', 'boo'], variables={}, **params)

# Generated at 2022-06-13 14:02:06.500058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    lookup = lookup_loader.get('ini')

    assert lookup.run(terms=['user'], section='global', file='test.ini')[0] == 'global user'

    assert lookup.run(terms=['user=foo'], section='integration', file='test.ini')[0] == 'integration foo'

    assert lookup.run(terms=['foo'], section='nosection', file='test.ini')[0] == ''

# Generated at 2022-06-13 14:02:16.371172
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    test.set_options(direct={
        'file': 'test/ansible.ini',
        'encoding': 'utf-8'
    })
    test.cp = configparser.ConfigParser()
    res = test.get_value('user', 'config', "", False)
    assert res == 'ansible'

    # Test a section that does not exist
    test.cp = configparser.ConfigParser(allow_no_value=True)
    res = test.get_value('user', 'config_none', "", False)
    assert res == ""

    # Test a key that does not exist
    res = test.get_value('user_none', 'config', "", False)
    assert res == ""

    # Test a value that is empty

# Generated at 2022-06-13 14:02:24.676695
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test with a non regexp key
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(StringIO('[global]\nfoo=bar\njohn=doe'))
    assert lookup_module.get_value('foo', 'global', None, False) == 'bar'
    assert lookup_module.get_value('john', 'global', None, False) == 'doe'

    # Test with a regexp key
    assert lookup_module.get_value('f.+', 'global', None, True) == ['foo=bar']
    assert lookup_module.get_value('.*n', 'global', None, True) == ['john=doe']