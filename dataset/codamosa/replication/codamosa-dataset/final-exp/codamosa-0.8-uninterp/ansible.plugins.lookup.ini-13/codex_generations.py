

# Generated at 2022-06-13 13:52:34.269621
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    config_parser = configparser.ConfigParser()
    config_parser.read(os.path.join(os.path.dirname(__file__), 'test.ini'))

    # create the lookup obj
    lookup_module = LookupModule()
    lookup_module.cp = config_parser

    # test single value
    assert lookup_module.get_value("key2", "section1", "default", False) == "value2"
    assert lookup_module.get_value("key3", "section1", "default", False) == "default"

    # test multiple values with regexp
    assert lookup_module.get_value("key2", "section1", "default", True) == ["value2", "value4"]
    assert lookup_module.get_value("key[0-9]", "section1", "default", True)

# Generated at 2022-06-13 13:52:42.828385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io
    import pytest

    class FakeLoader(object):
        def __init__(self, content):
            self.content = content
        def _get_file_contents(self, path):
            return self.content, path

    class FakeVars(object):
        def __init__(self, content):
            self.content = content
        def get(self, var, default=None):
            return self.content.get(var, default)
    # Example of ini file

# Generated at 2022-06-13 13:52:49.660846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    results = lookup_plugin.run([
        'test_property',
        'regexp=True test_property_regexp',
        'section=some_section test_property_section',
        'file=tests/unit/ansible/test_lookup_ini.ini',
        'default=test_property_default',
        're=True',
        ],
        variables={}
    )
    assert results[0] == 'test_property_value'
    assert results[1] == ['test_property_regexp']
    assert results[2] == 'test_property_section'
    assert results[3] == 'test_property_default'
    assert results[4] == ['test_property_multiple']
    assert len(results) == 5


# Generated at 2022-06-13 13:53:01.378657
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def mock_get_value(key, section, dflt, is_regexp):
        return [v for k, v in mock_cp.items(section) if re.match(key, k)]

    mock_cp = configparser.ConfigParser()
    mock_cp.add_section('section1')
    mock_cp.set('section1', 'f0', 'v0')
    mock_cp.set('section1', 'f1', 'v1')
    mock_cp.set('section1', 'f2', 'v2')

    fp = StringIO()
    mock_cp.write(fp)
    fp.seek(0, os.SEEK_SET)
    mock_cp.readfp(fp)


# Generated at 2022-06-13 13:53:13.066430
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test with a regexp
    obj = LookupModule()
    key = ".*"
    obj.cp = configparser.ConfigParser()
    obj.cp.add_section("test")
    obj.cp.set("test", "key1", "value1")
    obj.cp.set("test", "key2", "value2")
    obj.cp.set("test", "key3", "value3")
    assert obj.get_value(key, "test", "", True) == ["value1", "value2", "value3"]
    # Test with a regexp but no match
    key = ".*a"
    assert obj.get_value(key, "test", "", True) == []
    # Test without a regexp
    key = "key1"

# Generated at 2022-06-13 13:53:21.209912
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a dummy file
    dummy_file = StringIO()
    dummy_file.write(u"""[default]
key1=value1
key2=value2

[section1]
key3=value3
key4=value4

[section2]
key5=value5
key6=value6
""")
    dummy_file.seek(0, os.SEEK_SET)

    # Initialize LookupModule
    cls = LookupModule()

    # Initialize config parser (with ini_file)
    cp = configparser.ConfigParser()
    cp.readfp(dummy_file)

    # Initialize attributes
    cls.cp = cp

    # Test get_value() with no regexp

# Generated at 2022-06-13 13:53:32.832351
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Read properties file
    ini = LookupModule()
    ini._loader = DictDataLoader({'user.properties': u'user.name = Alice\nuser.password = mypass'})
    res = ini.run(['user.name'], {}, type='properties')
    assert res[0] == 'Alice'

    res = ini.run(['user.name', 'user.password'], {}, type='properties')
    assert res[0] == 'Alice'
    assert res[1] == 'mypass'

    res = ini.run(['user.name', 'user.login'], {}, type='properties')
    assert res[0] == 'Alice'
    assert res[1] == ''


# Generated at 2022-06-13 13:53:41.404235
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Sample input for method run
    terms = []
    terms.append('key1')
    terms.append('key2')
    terms.append('key3')
    variables = dict()
    variables['ansible_defaults'] = 'foo'
    kwargs = dict()
    kwargs['param1'] = 'foo'
    kwargs['param2'] = 'foo'
    kwargs['param3'] = 'foo'

    # Call method run
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables, kwargs)

    # Assert result
    assert result != 'foo'

# Generated at 2022-06-13 13:53:47.969937
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: replace those test by unit test
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six.moves import builtins


    class Dict(dict):
        def __setitem__(self, key, val):
            super(Dict, self).__setitem__(key, val)

        def __getitem__(self, key):
            return super(Dict, self).__getitem__(key)

        def __contains__(self, key):
            return super(Dict, self).__contains__(key)

    class CStringIO(cStringIO.StringIO):
        def write(self, val):
            return super(CStringIO, self).write(val)



# Generated at 2022-06-13 13:53:51.552412
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import configparser
    config = configparser.ConfigParser()
    config.read('../test/test.ini')
    lookup = LookupModule()
    lookup.cp = config
    assert lookup.get_value('user', 'section1', 'default value', False) == 'testuser'


# Generated at 2022-06-13 13:54:08.014231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class AnsibleModule:
        def __init__(self):
            self.params = {}

    class AnsibleLookup:
        def __init__(self):
            self.loader = None
            self.get_basedir = lambda: ''

    lookup = LookupModule()
    lookup.loader = AnsibleLookup()
    lookup.params = AnsibleModule().params
    lookup.params.update({'file': 'test.ini', 'default': '', 'encoding': 'utf-8', 'allow_no_value': True, 'allow_none': True})

    # test full path references
    result = lookup.run(['user', 'password'], {}, file='test.ini')
    assert result == ['root', 'password']

    # test relative path references

# Generated at 2022-06-13 13:54:18.152871
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    '''
        This function checks the behavior of method get_value of class LookupModule
    '''
    from ansible.plugins.lookup import LookupModule

    class FakeParser():
        def __init__(self, my_data):
            self.init_data = my_data

        def get(self, section, key):
            return self.init_data[section][key]

        def items(self, section):
            return self.init_data[section].items()

    # Test 1
    data = {'project': {'start': '19 mars 2016', 'stop': '15 juillet 2016', 'owner': 'yperre'}}
    test_parser = FakeParser(data)
    lm = LookupModule()
    lm.cp = test_parser


# Generated at 2022-06-13 13:54:26.312132
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Properties file
    properties = StringIO()
    properties.write(u'user.name=yperre\nuser.login=yperre\nuser.pass=1234')
    properties.seek(0, os.SEEK_SET)
    cp = configparser.RawConfigParser()
    cp.readfp(properties)

    # Ini file
    ini = '''
[global]
user=root

[integration]
user=yperre

[production]
user=admin
    '''
    fp = StringIO(ini)
    cpi = configparser.RawConfigParser()
    cpi.readfp(fp)

    # Tests

    # Get a key
    lookup = LookupModule()
    lookup.cp = cpi

# Generated at 2022-06-13 13:54:36.463146
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create lookup module
    lookup = LookupModule()

    # Create mock ConfigParser and configure lookup module
    faux_cp = configparser.ConfigParser()
    faux_cp.add_section('section1')
    faux_cp.set('section1', 'key1', 'value1')
    faux_cp.set('section1', 'key2', 'value2')
    faux_cp.set('section1', 'key2b', 'value2')
    faux_cp.set('section1', 'key3', 'value3')
    faux_cp.add_section('section2')
    faux_cp.set('section2', 'key1', 'value1')
    faux_cp.set('section2', 'key2', 'value2')
    faux_cp.set('section2', 'key3', 'value3')
    faux

# Generated at 2022-06-13 13:54:42.871460
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test LookupModule._run
    """
    from ansible.plugins.lookup import LookupModule
    from ansible.parsing.dataloader import DataLoader

    lm = LookupModule()
    dl = DataLoader()
    terms = ['key=value']
    result = lm.run(terms, variables=None, **{'file': 'test/ansible.ini'})
    assert result == ['a']

# Generated at 2022-06-13 13:54:50.343000
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    terms = 'user=yperre password=pass section=integration file=users.ini'
    options = lookup.get_options()
    for term in terms.split(' '):
        params = _parse_params(term, options)
        for param in params:
            k, v = param.split('=')
            options[k] = v

    config = StringIO()
    config.write(u'[integration]\n')
    config.write(u'user=yperre\n')
    config.write(u'password=pass')
    config.seek(0, os.SEEK_SET)
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(config)


# Generated at 2022-06-13 13:55:02.076590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.readfp(StringIO(u"[section]\nvar1=value1\nvar2=value2\n"))
    assert lm.run([u'var1']) == ['value1']
    assert lm.run([u'var1', u'var2', u'var3']) == ['value1','value2']
    # Test regexp
    assert lm.run([u'var.'], re=True) == ['value1','value2']
    # Test default value
    assert lm.run([u'var3'], default=u'default value') == ['default value']
    # Test parameter

# Generated at 2022-06-13 13:55:08.346000
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    test = LookupModule()
    test.cp = configparser.RawConfigParser()
    test.cp.add_section("my_section")
    test.cp.set("my_section", "key1", "value1")
    test.cp.set("my_section", "key2", "value2")

    # Test successful run
    assert test.get_value("key1", "my_section", None, False) == "value1"
    assert test.get_value("key2", "my_section", None, False) == "value2"

    # Test error handling when section is not in ini file
    try:
        assert test.get_value("key1", "another_section", None, False)
    except configparser.NoSectionError:
        assert True

    # Test error handling when key is not in ini file

# Generated at 2022-06-13 13:55:18.891060
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    test = LookupModule()
    test.cp = configparser.ConfigParser()
    test.cp.add_section('section1')
    test.cp.set('section1', 'key1', 'value1')
    test.cp.set('section1', 'key2', 'value2')

    assert test.get_value('key1', 'section1'), 'value1'
    assert test.get_value('key2', 'section1'), 'value2'
    assert test.get_value('key3', 'section1'), None

    assert test.get_value('key1', 'section2'), None
    assert test.get_value('key1', 'Section1'), None
    assert test.get_value('key1', 'SECTION1'), None


# Generated at 2022-06-13 13:55:29.227595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    fd, p = tempfile.mkstemp()
    os.close(fd)

    terms = [
        'foo',
        'foo=bar',
        'foo bar',
        'foo bar=baz',
        'foo=bar bar=baz',
        'foo=bar baz',
        'baz=bok',
        'file=foo.ini',
        'section=toto',
        'default=not_found',
    ]

    contents = '''
[toto]
foo=bar
bar=baz
baz=bok
'''

    with open(p, 'w') as fd:
        fd.write(contents)
    l = LookupModule()


# Generated at 2022-06-13 13:55:45.675303
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test syntax error in parameters
    test_module = LookupModule()
    test_module.set_options({'file': 'test.ini'})
    test_module.params = {
        'key': 'key',
        'file': 'file',
        're': 're',
        'encoding': 'encoding',
        'default': 'default',
        'type': 'type',
        'case_sensitive': 'case_sensitive',
        'allow_no_value': 'allow_no_value',
        'section': 'section'
    }
    test_module.cp = configparser.ConfigParser()
    try:
        test_module.run(terms=['key=value key'])
        assert False  # Should not be reached
    except AnsibleOptionsError:
        pass

    # Test missing section
    test

# Generated at 2022-06-13 13:55:53.796575
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class TestLookupModule(LookupModule):
        def __init__(self):
            self.cp = configparser.ConfigParser()
            self.cp.add_section('test')
            self.cp.set('test', 'a', '1')
            self.cp.set('test', 'b', '2')
            self.cp.set('test', 'c', '')
            self.cp.set('test', 'd', '4')
            self.cp.set('test', 'e', '5')

    lookup_module = TestLookupModule()

    # Test that the test object is properly initialized
    assert len(lookup_module.cp.options('test')) == 5
    assert lookup_module.cp.get('test', 'a') == '1'

# Generated at 2022-06-13 13:55:58.744661
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Act
    data = LookupModule().run([
        'user=ansible',
        'default=',
        'file=users.ini',
        'section=integration',
    ], variables=dict())

    # Assert
    assert data == ['admin']

# Generated at 2022-06-13 13:56:08.546569
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a mock
    cp = configparser.ConfigParser()
    cp.add_section('section1')
    cp.set('section1', 'key1', 'value1')
    cp.set('section1', 'key2', 'value2')
    cp.set('section1', 'key3', 'value3')
    cp.set('section1', 'key4', 'value4')

    # Create a class for testing
    class LookupModule_test(LookupModule):
        def get_value(self, key, section, dflt, is_regexp):
            return super(LookupModule_test, self).get_value(key, section, dflt, is_regexp)


# Generated at 2022-06-13 13:56:17.348139
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # First test, invalid paramater

    # Create the lookup module
    lookup = LookupModule()

    # Create a new term, with unvalid parameter
    term = 'test=test'

    # Create a new var_options
    var_options = {}

    # Create a new direct
    direct = {}

    # Run the method run of class LookupModule
    try:
        lookup.run([term], var_options, **direct)
    except AnsibleLookupError as error:
        assert "is not a valid option" in (error.message)

    # Second test, invalid parameter and invalid regexp

    # Create the lookup module
    lookup = LookupModule()

    # Create a new term, with unvalid parameter and an unvalid regexp
    term = 'test=test test=test'

    # Create a new var_options
    var

# Generated at 2022-06-13 13:56:27.580541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def get_success_result(key):
        return "Value for key %s" % key
    def get_error_result(key):
        raise AnsibleLookupError("No value for key %s" % key)
    def get_value(key, section, dflt, is_regexp):
        if key == "abcd":
            return get_success_result(key)
        else:
            return get_error_result(key)

    # mock a object of LookupModule
    lookup_module = LookupModule()
    lookup_module.get_value = get_value

    # test happy case
    assert lookup_module.run(["abcd"]) == ["Value for key abcd"]

    # test missing key case
    assert lookup_module.run(["plop"]) == []

    # test multiple keys
   

# Generated at 2022-06-13 13:56:38.071431
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    content = '''[foo]
    bar1 = ansible
    bar3 = ansible
    bar4 = ansible
    bar5 = ansible
    [ansible]
    bar2 = ansible
    '''

    # Parse file in configparser instance
    cp = configparser.ConfigParser()
    config = StringIO()
    config.write(content)
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)

    # Create test lookup module

# Generated at 2022-06-13 13:56:50.439698
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    lm = LookupModule()
    values = {
        ('key', 'section', 'default', False): 'value',
        ('key', 'section', 'default', True): 'value',
        ('key', 'section', 'default', False): 'value',
        ('key', 'section', 'default', False): 'value',
        ('akey', 'section', 'default', True): 'default',
        ('key', 'section', 'default', False): 'value',
        ('ke', 'section', 'default', True): 'value',
        ('key', 'section', 'default', False): 'value',
        ('ke', 'section', 'default', True): 'value',
        ('key', 'section', 'default', False): 'value',
        ('ke', 'section', 'default', True): 'value',
    }


# Generated at 2022-06-13 13:57:01.974165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError
    from ansible.module_utils.six import StringIO
    import sys

    sys.path.append('./lib')
    from yaml import load
    from ansible.plugins.lookup import LookupBase

    # Retrieve data from yaml files
    f = open('../tests/ansible/lookup/plugins/ini/fixtures/users.yml')
    test_users_yml = load(f)
    f.close()
    f = open('../tests/ansible/lookup/plugins/ini/fixtures/users.properties.yml')
    test_users_properties_yml = load(f)
    f.close()
    f = open('../tests/ansible/lookup/plugins/ini/fixtures/test.yml')
    test

# Generated at 2022-06-13 13:57:13.586026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
        'key1',
        'key2',
        'key1 section2',
        'key1 section1',
        'key1 default=value_default section1',
        'key1 section1 default=value_default',
        'key2 section2',
        'key2 section2 default=value_default',
        'key2 section2 default=value_default re=True',
        'key3',
        'key3 allow_none=True',
        'key3 section1 allow_none=True',
        'key4',
        'key4 section1',
        'key4 section2',
        'key_regexp',
        'key_regexp section1',
    ]


# Generated at 2022-06-13 13:57:50.499029
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    module = LookupModule()

    assert module.get_value('a', 'section1', 'default', False) == 'a'
    assert module.get_value('b', 'section1', 'default', False) == 'b'
    assert module.get_value('c', 'section1', 'default', False) == 'c'

    assert module.get_value('a', 'section2', 'default', False) == ''

    assert module.get_value('a', 'section1', 'default', True) == ['a', 'b', 'c']
    assert module.get_value('z', 'section1', 'default', True) == []

    assert module.get_value('c', 'section1', 'default', False) == 'c'



# Generated at 2022-06-13 13:57:58.105806
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """ Test case for method get_value of class LookupModule

    Test:
        - generate a configparser object
        - call method get_value with a regexp pattern
        - call method get_value with a simple pattern and valid section
        - call method get_value with a simple pattern and invalid section

    """
    # test get_value with a regexp pattern
    cp = configparser.ConfigParser()
    cp.readfp(StringIO(u'[section1]\n'
                       u'key1=value1\n'
                       u'key2=value2\n'
                       u'key3=value3\n'
                       u'[section2]\n'
                       u'key4=value4\n'
                       u'key5=value5\n'))

# Generated at 2022-06-13 13:58:06.171964
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import os
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes

    lookup_module = LookupModule()
    test_file = 'test_get_value.ini'
    cp = configparser.ConfigParser()
    config = open(test_file, 'w')

    cp.add_section("section_2")
    cp.set("section_2", "key_1","value_1")
    cp.set("section_2", "key_2","value_2")
    cp.set("section_2", "key_3","value_3")
    cp.set("section_2", "key_4","value_4")

    cp.add_section("section_1")

# Generated at 2022-06-13 13:58:19.483297
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # common test parameters
    fp = "[section1]\nkey1=value1\nkey2=value2\n[section2]\nkey3=value3\n"
    config = StringIO()
    config.write(fp)
    config.seek(0, os.SEEK_SET)
    section1 = configparser.ConfigParser()
    section1.readfp(config)
    lm = LookupModule()
    lm.cp = section1
    # specific test parameters

# Generated at 2022-06-13 13:58:33.649307
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # New object for class LookupModule
    lmod = LookupModule()

    # Dict with options for LookupModule
    param = {
        '_terms': ['user'],
        'type': 'ini',
        'file': 'users.ini',
        'encoding': 'utf-8',
        'section': 'integration',
        'default': ''
    }

    # Test with file 'users.ini' and section 'integration'
    users_ini = [
        '[integration]',
        'user=yannig',
        '[production]',
        'user=test1',
        'user=test2'
    ]
    user_ini_file = StringIO('\n'.join(users_ini))

    # Must return ['yannig']

# Generated at 2022-06-13 13:58:44.894722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from yaml import full_load
    import pytest

    fixtures_path = "../../test/unit/lookup/fixtures/ini"

# Generated at 2022-06-13 13:58:55.509119
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1: Test with an 'ini' file
    text = """[section1]
key1=value1 key1
key2=value2
key3=value3
key4=value4
[section2]
key1=value1 key1

[section3]
key1=value1 key1
"""
    test = StringIO()
    test.write(text)
    test.seek(0, os.SEEK_SET)

    cp = configparser.ConfigParser()
    cp.readfp(test)

    t = LookupModule()
    t.cp = cp
    t.cp.optionxform = to_native
    t.get_value = t.get_value

# Generated at 2022-06-13 13:59:02.298249
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    assert LookupModule().get_value("user", "section1", "", False) == "user1"
    assert LookupModule().get_value(".*", "section1", "", True) == ['user1', 'user2']
    assert LookupModule().get_value("user", "section2", "", False) == ""
    assert LookupModule().get_value("user", "section2", "default_value", False) == "default_value"

# Generated at 2022-06-13 13:59:12.390049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test the method run from LookupModule class."""

    # Create and return a Test class instance
    test_inst = Test()

    # Test basic and complex cases.
    test_inst.run_test(
        test_name="test_01",
        term="user",
        section="integration",
        file="users.ini",
        expected_result="yperre"
    )
    test_inst.run_test(
        test_name="test_02",
        term="user=plop",
        section="integration",
        file="users.ini",
        expected_result="yperre"
    )

# Generated at 2022-06-13 13:59:13.087534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:00:12.976879
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookupModule = LookupModule()

    config = StringIO()
    config.write(u'[mysqld]\n')
    config.write(u'user=mysql\n')
    config.write(u'user2=mysql\n')
    config.write(u'user3=mysql\n')
    config.write(u'#user4=foo\n')
    config.write(u'user4\n')
    config.write(u'#user5=\n')
    config.write(u'user5\n')
    config.write(u'user_dave=dave\n')
    config.seek(0, os.SEEK_SET)
    lookupModule.cp.readfp(config)


# Generated at 2022-06-13 14:00:22.124846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mock_loader = Mock(
        _get_file_contents=Mock(return_value=('[section1]\nkey1=val1\nkey1=val2\nkey2=val3\nkey3=val4', {})),
        path_dwim=Mock(return_value='/file/path')
    )
    mock_template_uid = Mock(
        get_basedir=Mock(return_value='/playbook/basedir'),
        get_loader_name=Mock(return_value='loader')
    )
    mock_template_uid.template_host = Mock(
        get_search_path=Mock(return_value=[])
    )

# Generated at 2022-06-13 14:00:29.968352
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import os
    from ansible.parsing.dataloader import DataLoader

    # This method uses data loader for file lookup, so we have to
    # create a data loader
    D = DataLoader()
    # Create a temp file
    (tmp_fd, path) = tempfile.mkstemp()
    # Drop the file if it exists
    try:
        os.unlink(path)
    except OSError:
        pass
    # Create file
    open(path, 'a').close()
    # Create test string
    test_string="""
[section]
one: 1
two: 2
three: 3
four: 4
"""
    # Write test string to file
    with open(path, 'wb') as f:
        f.write(test_string)
    # Get test string file path
   

# Generated at 2022-06-13 14:00:41.570677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule instance
    inst_lm = LookupModule()


    # Test the method run with no terms
    terms = []
    variables = {}
    direct = {}
    res = inst_lm.run(terms, variables, **direct)
    assert res == [], 'No result is expected'


    # Test the method run with term, variables and direct
    terms = [u'plop=plip /tmp/users.ini section1']
    variables = {}
    direct = {}
    inst_lm.set_options(var_options=variables, direct=direct)
    res = inst_lm.run(terms, variables, **direct)
    assert (type(res) == list), 'Result is expected to be a list'

# Generated at 2022-06-13 14:00:52.164144
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an examplar lookup module
    lookup_module = LookupModule()

    # create an examplar configparser for the lookup module to use during execution
    config = configparser.ConfigParser(allow_no_value=True)
    config.add_section("test")
    config.set("test", "key1", "value1")
    config.set("test", "key2", "value2")
    config.set("test", "key3", "value3")
    config.set("test", "key4", "value4")
    lookup_module.cp = config

    # create a set of examplar terms to use as input
    terms = ["key1", "key2", "key3", "key4"]

    # create an examplar variable container to pass to the lookup module

# Generated at 2022-06-13 14:01:04.949801
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # TODO: test case_sensitive option
    lm = LookupModule()
    cp = configparser.ConfigParser()
    cp.optionxform = to_native
    cp.add_section('section1')
    cp.add_section('section2')
    cp.set('section1', 'key1', 'value1')
    cp.set('section1', 'key2', 'value2')
    cp.set('section1', 'key3', 'value3')
    cp.set('section2', 'key4', 'value4')
    cp.set('section2', 'key5', 'value5')
    cp.set('section2', 'key6', 'value6')
    lm.cp = cp
    # Test case: key is not found in file and default value is given in parameter
    assert lm.get_

# Generated at 2022-06-13 14:01:13.978651
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    cp_str = """
[section1]
key1=value1
key2=value2

[section2]
key3=value3
"""
    config = StringIO()
    config.write(to_text(cp_str))
    config.seek(0, os.SEEK_SET)

    cp = configparser.ConfigParser()
    cp.readfp(config)

    # Test case: no regex, section and key exists
    paramvals = {'section': 'section1', 're': False, 'file': 'test.ini'}
    assert LookupModule(cp).get_value('key1', **paramvals) == 'value1'

    # Test case: no regex, section exists but key does not exist

# Generated at 2022-06-13 14:01:26.697286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Preparation
    l = LookupModule()

    # Check with a not valid ini file
    with open('/tmp/ansible_test.ini', 'w') as f:
        f.write('[sect]\n')
    terms = [
        'key1',
        'key2 key=value',
        'key3 type=ini',
        'key4 file=/tmp/ansible_test.ini',
        'key5 section=sect',
        'key6 re=true',
        'key7 default=test',
        'key8 encoding=utf-8'
    ]

# Generated at 2022-06-13 14:01:35.720353
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Assume file test.ini with the following content
    # [section1]
    # key1 = value1
    # key2 = value2
    # key3 = value3
    # key4 = value4

    # Constructing the parameters
    my_arguments = {
        '_terms': ['key1', 'key2'],
        '_attributes': {'type': 'ini', 'section': 'section1', 'file': 'test.ini'},
        'file': "test.ini",
        'type': 'ini',
        'section': 'section1',
        're': 'False',
        'default': ''
    }

    # Creating a LookupModule object
    my_lookup_obj = LookupModule()

    # Calling run method of LookupModule object
    my_result = my_lookup_

# Generated at 2022-06-13 14:01:42.799765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #variable set to return the value of the key 'yannig' in section 'users' of the file 'user.ini'
    variable = "{{ lookup('ini', 'yannig', section='users', file='user.ini') }}"

    #Generation of a lookup object with variable as argument
    lookup_obj = LookupModule()
    res = lookup_obj.run([variable], None)
    assert res == ['yannig']