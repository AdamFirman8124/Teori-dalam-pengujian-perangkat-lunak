

# Generated at 2022-06-13 13:52:38.194454
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    module = LookupModule()
    config = configparser.ConfigParser()
    config.read("test_data")
    module.cp = config

    # Test regexp
    assert module.get_value('s.*', 'section2', None, True) == ['4', '6', '777', '8']
    assert module.get_value('e.*', 'section2', None, True) == ['42']
    assert module.get_value('k.*', 'section2', None, True) == []
    # Test not regexp
    assert module.get_value('test1', 'section1', None, False) == '1'
    assert module.get_value('test3', 'section1', None, False) == '3'
    assert module.get_value('test4', 'section1', None, False) == '4'


# Generated at 2022-06-13 13:52:47.219000
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib

    lookup = LookupModule()
    lookup.set_options({'file': 'test.ini', 'section': 'test_section', 're': True})

    config = StringIO()
    config.write(u'[test_section]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'key2_bis=value2\n')
    config.write(u'key3=value3\n')
    config.seek(0, os.SEEK_SET)

    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(config)

    assert lookup.get_value('key1', 'test_section', None, False)

# Generated at 2022-06-13 13:53:00.027249
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for ini file
    # Test for file not exist
    lookup = LookupModule()
    lookup.set_options(direct={
        'file': 'test/ini_not_exist.ini'
    })
    assert lookup.run(['key1']) == []

    # Test for file with invalid content
    lookup = LookupModule()
    lookup.set_options(direct={
        'file': 'test/invalid_content.ini'
    })
    assert lookup.run(['key1']) == []

    # Test for simple key
    lookup = LookupModule()
    lookup.set_options(direct={
        'file': 'test/ini_file.ini'
    })
    assert lookup.run(['key1']) == ['value1']

# Generated at 2022-06-13 13:53:11.655670
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:53:20.295942
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()

    # List of tests
    tests = [
        ("p[0-9]", {"p1": "v1", "p2": "v2"}, None, True),
        ("p2", {"p1": "v1", "p2": "v2"}, None, False),
        ("p3", {"p1": "v1", "p2": "v2"}, "default", False),
    ]

    # Run tests
    for (key, section, dflt, is_regexp) in tests:
        assert lm.get_value(key, section, dflt, is_regexp) == section[key]

    # Run error test
    lm.get_value("p3", {"p1": "v1", "p2": "v2"}, "default", True)

# Generated at 2022-06-13 13:53:32.368304
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1
    # Check that we can retrieve the value for two different keys
    ini = '''
    [global]
    user1=yperre
    user2=aperre
    '''
    expected = ['yperre', 'aperre']

    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.readfp(StringIO(ini))
    
    assert expected == l.run(terms=['user1', 'user2'])
    
    # Test 2
    # Check that we can retrieve the values for one key, in two different section
    ini = '''
    [integration]
    user=yperre
    [production]
    user=aperre
    '''
    expected = ['yperre', 'aperre']

    l.cp.readfp

# Generated at 2022-06-13 13:53:42.910272
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    # No path and no key
    terms = ["user=root", "file=ansible.ini", "section=global"]
    assert(lookupModule.run(terms = terms, variables = None, **{}) == [])

    # No file and no key
    terms = ["user=root", "section=global"]
    assert(lookupModule.run(terms = terms, variables = None, **{}) == [])

    # No section and no key
    terms = ["user=root", "file=ansible.ini"]
    assert(lookupModule.run(terms = terms, variables = None, **{}) == [])

    # No key
    terms = ["user=root", "file=ansible.ini", "section=global"]

# Generated at 2022-06-13 13:53:50.914386
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a lookup module
    lookup = LookupModule()

    # Create test variables
    terms = ['section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2', 'section2']
    variables = 'variables'

# Generated at 2022-06-13 13:54:03.443824
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()

    # Set the value of cp
    # Create StringIO later used to parse ini
    config = StringIO()
    # Special case for java properties
    config.write(u'[java_properties]\n')
    # Open file using encoding
    contents = "user.name=bob\nuser.surname=bob\nuser.age=42\n"
    contents = to_text(contents, errors='surrogate_or_strict', encoding='utf-8')
    config.write(contents)
    config.seek(0, os.SEEK_SET)
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(config)

    # Retrieve all values from a section using a regexp

# Generated at 2022-06-13 13:54:10.704360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_m = LookupModule()
    test_m.cp = configparser.ConfigParser()
    test_m.cp.optionxform = str

    test_m.cp.readfp(StringIO("""[section1]
var1="Hello"
var2="World"

[section2]
var1=Toto
var2=Tata

[section3]
var1="foo"
var2="bar"
"""))

    # Test with a non-existing section
    result = test_m.run([['var1', 'file=none', 'section=none']])
    assert result == [None]

    # Test with a non-existing key
    result = test_m.run([['var3', 'file=none', 'section=section1']])
    assert result == [None]

    # Test

# Generated at 2022-06-13 13:54:35.618355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test the case where a key does not exist in the ini file and a default value is given
    assert lookup.run(["foo", "type=ini", "file=ansible.ini", "default=bar"], {}) == ["bar"]
    assert lookup.run(["foo", "type=properties", "file=user.properties"], {}) == []
    assert lookup.run(["user.name", "type=properties", "file=user.properties"], {}) == ["foo"]
    assert lookup.run(["user.name=foo", "type=properties", "file=user.properties"], {}) == ["foo"]
    assert lookup.run(["user.name=foo", "user.password=bar", "type=properties", "file=user.properties"], {}) == ["foo", "bar"]

# Generated at 2022-06-13 13:54:46.379547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Fake ansible options
    ansible_options = {'variable_manager': None, 'loader': None}
    module.set_options(var_options=ansible_options)

    # Add the file to the ini parser, then parse it
    StringIO_file = StringIO(u'[test]\ntest=test')
    module.cp = configparser.ConfigParser()
    module.cp.readfp(StringIO_file)

    # Test the get_value method
    assert module.get_value('test', 'test', None, False) == 'test'

    # Test the run method

# Generated at 2022-06-13 13:54:52.364418
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config = LookupModule()
    list = config.run(terms = ["user.mail=yannig@perre.fr"], variables = {"files": ['/etc']}, file='users.ini', type='ini')
    assert list == ["yannig@perre.fr"]

# Generated at 2022-06-13 13:55:03.542448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1 : call run without any arguments
    lookup = LookupModule()
    result = lookup.run([], [], [])
    assert len(result) == 0

    # Test 2 : call run with an empty list
    lookup = LookupModule()
    result = lookup.run([[]], [], [])
    assert len(result) == 0

    # Test 3 : call run with a key in a properties file
    lookup = LookupModule()
    result = lookup.run(["user.name"], [], [])
    assert len(result) == 1

    # Test 4 : call run with a key in an ini file
    lookup = LookupModule()
    result = lookup.run(["user"], [], [])
    assert len(result) == 1

    # Test 5 : call run with a key in an ini file and a parameter

# Generated at 2022-06-13 13:55:15.848295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule.run(terms, variables=None, **kwargs)
    # Create a LookupModule object
    lookup_plugin = LookupModule()
    lookup_plugin.set_options(direct={'file': 'tests/fixtures/lookup_ini/users.ini', 'encoding': 'utf-8', 'case_sensitive': False})
    lookup_plugin.run()

    terms = ['user', 'user', 'user', 'user']
    kwargs = {'section': 'integration'}

    assert lookup_plugin.run(terms, **kwargs) == ['yannig', 'neustradamus', 'beaucoup']
    kwargs = {'section': 'production', 'default': 'no_default'}

# Generated at 2022-06-13 13:55:23.093372
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case: by default, return all values
    terms = [{
        "key": "a"
    }, {
        "key": "b"
    }, {
        "key": "c"
    }, {
        "key": "d"
    }]
    results = [{
        "key": "a",
        "value": "1"
    }, {
        "key": "b",
        "value": "2"
    }, {
        "key": "c",
        "value": "3"
    }, {
        "key": "d",
        "value": "4"
    }]
    lookup_module = LookupModule()

    # Test with default value
    for term in terms:
      result = lookup_module.get_value(term["key"], "default", "default", False)

# Generated at 2022-06-13 13:55:25.662780
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=["key2", "key3"], variables={}) == ["value2", "value3"]

# Generated at 2022-06-13 13:55:38.643125
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    config = StringIO()
    config.write(u'[section1]\nkey1=value1\nkey2=value2')
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)

    # Test a single value
    assert lookup.get_value('key1', 'section1', None, False) == 'value1'

    # Test a regexp
    assert lookup.get_value('key.', 'section1', None, True) == ['value1', 'value2']

    # Test a non existing key
    assert lookup.get_value('key3', 'section1', None, False) == None

    # Test a non existing section
    assert lookup.get_value('key3', 'section3', None, False) == None

# Generated at 2022-06-13 13:55:39.916462
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #TODO: implement unit test
    pass

# Generated at 2022-06-13 13:55:49.259186
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init
    test_obj = LookupModule()
    test_obj_cp = configparser.ConfigParser()
    test_obj.cp = test_obj_cp
    test_obj_cp.optionxform = to_native

    # Fake section
    section = 'fake_section'

    # Fake file contents
    file_contents = '[{section}]\nkey1=value1\nkey2=value2\nkey3=value3'.format(section=section)

    # Fake parameters
    paramvals = {"type": "ini", "file": "fake.ini", "section": section, "re": False, "default": "", "encoding": "utf-8", "case_sensitive": False}

    # Fake config
    config = StringIO()

# Generated at 2022-06-13 13:56:13.899420
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.errors import AnsibleOptionsError
    from ansible.utils.path import unfrackpath

    lookup = LookupModule()

    # TODO: this needs to be broken into smaller tests

    # test with no options

# Generated at 2022-06-13 13:56:19.849734
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    module = LookupModule()
    key = 'key'
    section = 'section'
    dflt = 'dflt'
    is_regexp = False
    assert module.get_value(key, section, dflt, is_regexp) == 'value'
    key = 'ke'
    section = 'section'
    dflt = 'dflt'
    is_regexp = True
    assert module.get_value(key, section, dflt, is_regexp) == ['y=value', 'y2=value2']
    key = 'y'
    section = 'no-section'
    dflt = 'dflt'
    is_regexp = True
    assert module.get_value(key, section, dflt, is_regexp) == dflt

# Generated at 2022-06-13 13:56:28.803845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    class TestLookupModule(unittest.TestCase):
        class MockedModule:
            class MockedLoader:
                class MockedFileLoader:
                    def get_basedir(self, c):
                        return ""
                    def path_dwim_relative(self, a, b):
                        return ""
                    def is_file(self, f):
                        return True
            def __init__(self):
                self.loader = self.MockedLoader()
                self.basedir = ''
            def get_basedir(self):
                return self.basedir
        class MockConfigParser():
            def __init__(self):
                self.sections = []
                self.options = {}

# Generated at 2022-06-13 13:56:37.748044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a mocked copy of the main class
    mocked = LookupModule()

    # mock the configparser module by replacing it in the lookup
    mocked.cp = configparser.ConfigParser()
    # create a fake file and populate it with an ini file
    mocked.cp.read_string(u'''
    [global]
    base_url = https://www.example.com/
    ''')

    # actual test
    terms = ['base_url']
    variables = None
    kwargs = {}
    ret = mocked.run(terms=terms, variables=variables, **kwargs)
    assert ret == ['https://www.example.com/']


# Generated at 2022-06-13 13:56:42.213602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    terms = ['var1', 'var2', 'var3', 'var4', 'var5', 'var6', 'var7', 'var8']
    config = StringIO()
    config.write(u'[global]\n')
    config.write(u'var1 = 127.0.0.1\n')
    config.write(u'var2 = string\n')
    config.write(u'var3 = list1, list2\n')
    config.write(u'var4 = "string1, string2"\n')
    config.write(u'var5 = "list1, list2, list3"\n')
    config.write(u'var6 = "list1, list2" "list1, list2"\n')

# Generated at 2022-06-13 13:56:43.337384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO
    pass

# Generated at 2022-06-13 13:56:51.173055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Negatif test : an empty term
    template = "{{ lookup('ini', None) }}"
    mocker.patch('ansible.plugins.lookup.ini.LookupBase.get_basedir', return_value='.')
    mocker.patch('ansible.plugins.lookup.ini.LookupBase.run', side_effect=AnsibleOptionsError)
    lookup = LookupModule()
    with pytest.raises(AnsibleOptionsError):
        assert lookup.run(terms=None, variables={})


# Generated at 2022-06-13 13:57:02.052956
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ###################################################################################
    # --------------- TEST for section 'properties' -----------------------------------
    ###################################################################################
    test_ini_string = StringIO()
    test_ini_string.write(u"""
[java_properties]
user.name=John
user.age=24
    """)
    test_ini_string.seek(0, os.SEEK_SET)
    test_cp = configparser.ConfigParser()
    test_cp.readfp(test_ini_string)

    # TEST 1: use valid params
    lm = LookupModule(None)
    lm.cp = test_cp
    key = 'user.name'
    section = 'java_properties'
    dflt = None
    is_regexp = False

# Generated at 2022-06-13 13:57:04.171143
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([],) == []
    assert LookupModule().run([''],) == ['']

# Generated at 2022-06-13 13:57:15.021654
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:57:51.840667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    lookup_plugin.cp = configparser.ConfigParser()
    test_file = """
[global]
global=global
global_section_value=global_section_value
[section1]
key1=value1
[section2]
key2=value2
key3=value3
"""
    with open("test.ini", "w") as file:
        file.write(test_file)
    lookup_plugin.cp.read("test.ini")
    terms = [
        "global",
        "global_section_value",
        "key1",
        "key2",
        "key3",
        "re=key[23]",

        "non_existent_param",
        "re=non_existent_param",
    ]

# Generated at 2022-06-13 13:58:02.785696
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _get_config(content):
        config = StringIO()
        config.write(content)
        config.seek(0, os.SEEK_SET)
        return config

    # Unit test for method run of class LookupModule
    # There is 2 cases:
    # - 1 if the user specifies a regexp
    # - 1 if the user doesn't use a regexp

    # First case:
    # The user specifies a regexp
    # We want to test only the regexp branch of self.get_value method,
    # so we use a section and a regexp that result in a match
    # The values of this file are OK


    # Test for a valid file
    # Test for a .ini file

# Generated at 2022-06-13 13:58:11.529890
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing the ini file
    iniPath = "./ansi_test.ini"
    # build the module
    lmodule = LookupModule()
    # build the args
    args = {
        "terms": ["user"],
        "file": iniPath,
        "section": "integration",
        "re": False
    }
    result = lmodule.run([args["terms"]], **args)
    assert result == ["user_integration"]


# Generated at 2022-06-13 13:58:22.472583
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test ansible.plugins.lookup.ini.LookupModule.run

    To run this test, put a file named 'hoge.ini' in your module_utils directory.
    The contents are as follows:

    [global]
    hoge = ansible
    foo = bar
    bar = baz
    qux = quux
    [section1]
    hoge = ansible
    foo = bar
    bar = baz
    qux = quux
    [section2]
    hoge = ansible
    foo = bar
    bar = baz
    qux = quux

    """
    lu = LookupModule()
    params = {}
    params["file"] = 'hoge.ini'
    params["section"] = 'global'
    params["default"] = ''

    # Test case without section

# Generated at 2022-06-13 13:58:35.480771
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case 1
    terms = ['user']
    variables = {'ansible_basedir': '../../examples'}
    kwargs = {'file': 'ansible.ini'}
    ini = LookupModule()
    assert ini.run(terms, variables, **kwargs) == ["tester"]

    # Test case 2
    terms = ['user']
    variables = {'ansible_basedir': '../../examples'}
    kwargs = {'file': 'hosts', 'section': 'integration'}
    ini = LookupModule()
    assert ini.run(terms, variables, **kwargs) == []

    # Test case 3
    terms = ['user']
    variables = {'ansible_basedir': '../../examples'}

# Generated at 2022-06-13 13:58:46.268747
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # First case
    terms = ['user']
    variables = None
    kwargs = {
        'file': 'users.ini',
        'default': '',
        'encoding': 'utf-8',
        'allow_no_value': False,
        'section': 'integration',
        're': False,
        'type': 'ini',
        'case_sensitive': False,
    }
    expected_result = ['jones']
    lookup_obj = LookupModule()
    lookup_obj.cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[integration]\n')
    config.write(u'user=jones\n')
    config.seek(0, os.SEEK_SET)
    lookup_obj.cp.readfp(config)
   

# Generated at 2022-06-13 13:58:48.322898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup_module = LookupModule()
    # Add test for LookupModule
    return

# Generated at 2022-06-13 13:58:56.497444
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()

    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key', 'value')

    assert lookup.get_value('key', 'section1', None, False) == 'value'
    assert lookup.get_value('.*',  'section1', None, True)  == ['value']
    assert lookup.get_value('key', 'section2', None, False) is None


# Generated at 2022-06-13 13:59:03.376835
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialization
    options = {"encoding": "utf-8",
               "file": "test_ansible.ini",
               "default": "",
               "re": False,
               "type": "ini",
               "case_sensitive": False,
               "allow_no_value": False}
    terms = ["user_test", "pass_test", "pass_test_1"]
    unittest_path = os.path.join(os.path.dirname(__file__), "unittest_data")
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=None, direct=options)

    # Test 1: No regexp, section "test"
    options["section"] = "test"
    options["re"] = False

# Generated at 2022-06-13 13:59:06.907150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    term = ''' key1=value1 key2=value2 '''
    terms = [term]
    lookup_module.run(terms=terms)

# Generated at 2022-06-13 14:00:04.111613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import  lookup_loader
    lookup = lookup_loader.get('ini')

    # Test a key looked with a regexp
    terms = ['.*']
    variables = {}
    kwargs = {
        'file': '../../lookup_plugins/test/ini/ansible.ini',
        'section': 'global',
        're': True
    }
    ret = lookup.run(terms, variables, **kwargs)
    assert ret == [u'secret-key', u'ansible-ssh', u'ansible-user']

# Generated at 2022-06-13 14:00:11.697381
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    terms = ["key1=1234", "key2=5678", "key3=abcd", "key4=\"eee mmm\""]
    variables = {'file': 'tests/files/test.ini'}
    options = {'case_sensitive': False, 'default': '', 'encoding': 'utf-8', 'file': 'ansible.ini', 're': False, 'section': 'section1'}
    options.update(variables)
    module = LookupModule()
    module.set_options(var_options=variables, direct=options)
    paramvals = module.get_options()

    cp = configparser.ConfigParser(allow_no_value=paramvals.get('allow_no_value', paramvals.get('allow_none')))


# Generated at 2022-06-13 14:00:21.721582
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common._collections_compat import MutableSequence

    lookup = LookupModule()

    IniFilePath = 'test_ini_file'

# Generated at 2022-06-13 14:00:29.737872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1
    terms1 = ['user', 'password=foo']
    filename = 'test/ansible_test/lookup_plugins/test_ini/test1.ini'
    kwargs = [{'file': filename, 'section': 'integration'},
              {'file': filename, 'section': 'production'},
              {'file': filename, 'case_sensitive': True},
              {'file': filename, 'section': 'integration', 'case_sensitive': True},
              {'file': filename}]
    variables1 = {}
    data = LookupModule().run(terms1, variables1, **kwargs[0])
    assert data == ['test-user-integration']
    data = LookupModule().run(terms1, variables1, **kwargs[1])

# Generated at 2022-06-13 14:00:38.354927
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """
    Check that get_value returns the right value
    """

    def test_get_value(cp, key, section, dflt, is_regexp, ret):
        l = LookupModule()
        l.cp = cp
        assert l.get_value(key, section, dflt, is_regexp) == ret

    def get_configparser(is_regexp):
        """
        Create a configparser and fill it with some data
        """
        cp = configparser.ConfigParser()
        cp.add_section("global")
        cp.set("global", "key1", "value1")
        cp.set("global", "key2", "value2")
        if is_regexp:
            cp.set("global", "key3", "value3")
        return cp


# Generated at 2022-06-13 14:00:48.515668
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Parameters to create the basic ini file read by the first test
    parameters_ini_file = {'section': 'global',
                           'key': 'server',
                           'value': '192.168.1.1',
                           'key_to_find': 'server',
                           'value_return': '192.168.1.1',
                           'value_returned_by_method__run': '192.168.1.1',
                           'path_file': 'test.ini',
                           'file': 'test.ini',
                           'data': '[global]\nserver = 192.168.1.1'}

    # Creation of the basic ini file read by the first test
    file_ini = open(parameters_ini_file['path_file'], 'w')
    file_ini.write

# Generated at 2022-06-13 14:00:53.514425
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    ins = {'key': 'world', 'section': 'test', 'dflt': '', 'is_regexp': False}
    lookup = LookupModule()
    cp = configparser.ConfigParser()
    cp.add_section(ins['section'])
    cp.set('test', 'hello', 'world')
    lookup.cp = cp
    assert lookup.get_value(**ins) == 'world'


# Generated at 2022-06-13 14:01:05.279430
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    fake_file = StringIO()
    fake_file.write("""
[unit]
test1=test
test2=test
test_no_value

[unit2]
test1=test
test2=test""")
    fake_file.seek(0)

    l = LookupModule()
    l.cp = configparser.ConfigParser(allow_no_value=True)
    l.cp.readfp(fake_file)

    assert len(l.run(["test1", "test2"], file=fake_file, section="unit")) == 2
    assert len(l.run(["test1", "test2", "test"], file=fake_file, section="unit")) == 3

# Generated at 2022-06-13 14:01:15.706796
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Simple check
    config = StringIO("""
[general]
foo = bar
""")
    cp = configparser.ConfigParser()
    cp.readfp(config)
    test_dict = dict()
    test_dict["allow_no_value"] = False
    test_dict["case_sensitive"] = False
    test_dict["encoding"] = "utf-8"
    test_dict["file"] = "test.ini"
    test_dict["re"] = False
    test_dict["section"] = "general"
    test_dict["type"] = "ini"
    test_dict["default"] = ""

    l = LookupModule()
    l.cp = cp

    assert l.get_value("foo", "general", "", False) == "bar"

# Generated at 2022-06-13 14:01:27.357250
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Test LookupModule method run '''
    from ansible.module_utils.six import PY2

    # Default parameters
    contents = "[section]\nkey=value"
    expected = ['value']
    terms = ['key']
    # Very few tests with Python 2.7
    if PY2:
        # No section or key error
        with pytest.raises(AnsibleLookupError):
            module = LookupModule()
            module.run(terms, dict())
    # Create a test class for lookup module
    class TestClass:
        def __init__(self, contents):
            self.contents = contents

        def find_file_in_search_path(self, variables, directories, filename):
            return 'test_file_path'
