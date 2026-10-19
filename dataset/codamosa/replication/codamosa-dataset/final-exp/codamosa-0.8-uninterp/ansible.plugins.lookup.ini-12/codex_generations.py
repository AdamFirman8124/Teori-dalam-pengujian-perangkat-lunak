

# Generated at 2022-06-13 13:52:35.491075
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create dict for test
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # get one value
    assert LookupModule.get_value('a', test_dict, None, False) == '1'
    # get a value with regexp
    assert LookupModule.get_value('[a-z]', test_dict, None, True) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 13:52:42.310139
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test param _terms of lookup
    path = os.getcwd()
    _terms = '*'
    _params = {}
    _results = []
    lkp = LookupModule()
    lkp.set_options(_params)
    _results = lkp.run(_terms, path=path)
    assert _results == []

    _terms = '*'
    _params = {}
    _results = []
    lkp = LookupModule()
    lkp.set_options(_params)
    _results = lkp.run(_terms, path=path+"/files")
    assert _results == []

# Generated at 2022-06-13 13:52:53.097931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    lookup = lookup_loader.get('ini', loader=None, templar=None)

    assert 'foobar' == lookup.run([
        AnsibleUnsafeText('[section]\nkey=foobar\n\ninittest=inittest'),
        'key',
        AnsibleUnsafeText('file=stringio\nsection=section'),
    ])[0]

    assert 'foobar' == lookup.run([
        AnsibleUnsafeText('[section]\nkey=foobar\n\ninittest=inittest'),
        'key',
        AnsibleUnsafeText('section=section\nfile=stringio'),
    ])[0]


# Generated at 2022-06-13 13:53:03.614513
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()

    # Test with an empty section
    section = 'section'
    lm.cp = configparser.ConfigParser(allow_no_value=True)
    lm.cp.add_section(section)
    key = 'key'
    value = 'value'
    lm.cp.set(section, key, value)
    returned_value = lm.get_value(key, section, 'default', True)
    assert returned_value == [value]

    # Test with a regex and multiple values
    key = 'key'
    key2 = 'key2'
    value = 'value'
    value2 = 'value2'
    lm.cp = configparser.ConfigParser(allow_no_value=True)
    lm.cp.add_section(section)

# Generated at 2022-06-13 13:53:15.198187
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Default values
    file = "ansible_test.ini"
    section = "section"
    key = "key"
    is_regexp = False
    dflt = "default"

    # Test for a single value with dflt
    config = StringIO()
    config.write(u'[{0}]\n{1}=value1'.format(section, key))
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()
    cp.readfp(config)
    lm = LookupModule()
    lm.cp = cp
    value = lm.get_value(key, section, dflt, is_regexp)
    assert value == "value1"

    # Test for a single value without dflt
    config = StringIO()

# Generated at 2022-06-13 13:53:27.622863
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Config file where test ini data will be written
    filename = 'test.ini'

    lookup = LookupModule()
    # Setting up test data
    data = """[env_prod_test]
user=johnd
password=password


[env_dev_test]
user=johnd
password=password


[env_prod_prod]
user=johnd
password=password


[env_dev_prod]
user=johnd
password=password


[section1]
key1=value1
key2=value2

[section2]
key3=value3
key4=value4"""
    # Write data to test.ini
    with open(filename, 'w') as f: f.write(data)
    # Test parameter without space

# Generated at 2022-06-13 13:53:36.396285
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    lookup = LookupModule()
    # Look for a property in a properties file
    result = lookup.run([ "user.name=", "type=properties", "file=test.properties"], variables=None, **{'_ansible_lookup_plugin':'ini'})
    assert result == ["foo"]

    # Look for a property in a properties file with a section java_properties
    result = lookup.run([ "user.name=", "type=properties", "file=test.properties", "section=java_properties"], variables=None, **{'_ansible_lookup_plugin':'ini'})
    assert result == ["foo"]

    # Look for a property in a properties file, section java_properties and default value

# Generated at 2022-06-13 13:53:45.100720
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    '''
    Test method get_value of class LookupModule
    '''
    # Create a class LookupModule instance with a configparser.ConfigParser mock
    cp_mock = configparser.ConfigParser()
    cp_mock.add_section('section')
    cp_mock.set('section', 'foo', 'foovalue')
    cp_mock.set('section', 'bar', 'barvalue')
    cp_mock.set('section', 'foobaz', 'foobazvalue')
    lm = LookupModule(None)
    lm.cp = cp_mock
    # Retrieve all values from a section using a regex
    assert lm.get_value('foo.*', 'section', None, True) == ['foovalue', 'foobazvalue']
    # Retrieve a single value
   

# Generated at 2022-06-13 13:53:55.136549
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.vault import VaultLib
    from ansible.utils.display import Display
    from ansible.utils.path import makedirs_safe

    display = Display()
    display.verbosity = 4

    tmpdir = '/tmp/ansible-test'
    makedirs_safe(tmpdir)

    test = """
[global]
user = admin
password = adminpass

[integration]
user = john
password = johnpass

[production]
user = jack
password = jackpass

[section1]
key1=value1
key2=value2
key3=value3
key4=value4
key5=value5

[section2]
key1=value1
key2=value2
key3=value3
key4=value4
key5=value5
"""

# Generated at 2022-06-13 13:54:06.372414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Default options
    find_in_search_path_options = {
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False
    }

    # Construct module
    module = LookupModule()

    # Init module
    module.set_options(var_options={}, direct=find_in_search_path_options)

    # Test for no section
    module.run(terms=['key1'], variables={}, file='ansible.ini', section='none')

    # Test for no section
    module.run(terms=['key1'], variables={}, file='ansible.ini', section='none')

   

# Generated at 2022-06-13 13:54:20.874017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test no value
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.add_section('newssearch')
    lookup_module.cp.set('newssearch', 'key', '')
    assert lookup_module.get_value('key') == ''

    # Test value
    lookup_module.cp.set('newssearch', 'key', 'value')
    assert lookup_module.get_value('key') == 'value'

    # Test regexp on section
    lookup_module.cp.add_section('newssearch')
    lookup_module.cp.set('newssearch', 'key1', 'value1')
    lookup_module.cp.set('newssearch', 'key2', 'value2')

# Generated at 2022-06-13 13:54:34.884956
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleOptionsError
    from ansible.module_utils.common.collections import ImmutableDict

    lu = LookupModule()
    params = {'type': 'ini',
            'default': '',
            're': False,
            'encoding': 'utf-8',
            'file': 'ansible.ini'}

    with pytest.raises(AnsibleOptionsError) as exc:
        lu.run(['foo bar'], ImmutableDict(params))
    assert 'No key to lookup was provided as first term with in string inline options' in to_native(exc.value)

    with pytest.raises(AnsibleOptionsError) as exc:
        lu.run(['foo=baz bar'], ImmutableDict(params))

# Generated at 2022-06-13 13:54:45.741695
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create an instance of class LookupModule
    lookup_module = LookupModule()
    # Create an instance of class 'ConfigParser'
    cp = configparser.ConfigParser()
    # Set 'cp' as attribute of class LookupModule
    lookup_module.cp = cp
    # Add section '[section]' to 'cp'
    cp["section"] = {"key1" : "value1",
                     "key2" : "value2",
                     }
    # Test method get_value without regular expressions
    assert lookup_module.get_value("key1", "section", None, False) == "value1"
    assert lookup_module.get_value("key2", "section", None, False) == "value2"
    # Test method get_value with regular expressions

# Generated at 2022-06-13 13:54:58.654343
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    '''
    Unit test for method get_value of class LookupModule
    '''
    cp = configparser.RawConfigParser()
    cp.optionxform = str
    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(u'[test]\nfoo=bar\nbar.foo=foobar\nbaz=baz\n')
    config.seek(0, 0)

    cp.readfp(config)
    test_lookup = LookupModule()
    test_lookup.cp = cp

    # Retrieve a single value
    assert 'bar' == test_lookup.get_value('foo', 'test', None, False)
    # Retrieve values from a section using a regexp

# Generated at 2022-06-13 13:55:07.010722
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.set('section1', 'var1', 'value1')
    lookup_module.cp.set('section1', 'var2', 'value2')
    lookup_module.cp.set('section2', 'var1', 'value3')
    lookup_module.cp.add_section('section3')

    assert lookup_module.get_value('var1', 'section1', '', False) == 'value1'
    assert lookup_module.get_value('var2', 'section1', '', False) == 'value2'
    assert lookup_module.get_value('var1', 'section2', '', False) == 'value3'

# Generated at 2022-06-13 13:55:16.604973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        u'test.name',
        u'test.another_name',
        u''
    ]
    paramvals = {
        u're': True,
        u'section': u'test',
        u'type': u'ini',
        u'encoding': u'utf-8',
        u'file': u'test.ini'
    }
    l = LookupModule()
    l._templar = DummyTemplar()

    assert l.run(terms, paramvals=paramvals) == [
        u'name',
        u'another_name',
        u''
    ]



# Generated at 2022-06-13 13:55:23.512242
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """Generate object and test its get_value method"""

    cp = configparser.ConfigParser()
    cp.add_section('section')
    cp.set('section', 'key', 'value')

    # Object test
    my_test = LookupModule()
    my_test.cp = cp

    assert 'value' == my_test.get_value('key', 'section', None, False)
    assert None == my_test.get_value('not_existing_key', 'section', None, False)
    assert None == my_test.get_value('not_existing_key', 'not_existing_section', None, False)

    # Regexp test
    cp.set('section', 'key1', 'value1')
    cp.set('section', 'key2', 'value2')

# Generated at 2022-06-13 13:55:37.150854
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Init the LookupModule
    lookup_module = LookupModule()

    data = """
[section]
key1=val1
key2=val2
key3=val3
"""

    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(StringIO(to_text(data)))

    # Test with a regular key
    assert lookup_module.get_value("key1", "section", None, False) == "val1"

    # Test with a key that does not exists
    assert lookup_module.get_value("key4", "section", "default value", False) == "default value"

    # Test with a regexp that matches all keys
    assert lookup_module.get_value(".*", "section", None, True) == ["val1", "val2", "val3"]

# Generated at 2022-06-13 13:55:41.688650
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create the class instance
    lookup = LookupModule()

    # Store values
    os_environ_bck = dict(os.environ)
    os.environ["ANSIBLE_LOOKUP_PLUGINS"] = '/home/user/ansible_plugins_lookup'

    # Return
    assert lookup.run(["db_user"], variables=None, file="users.ini", section="integration") == "bob"

# Generated at 2022-06-13 13:55:50.902527
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    lm = LookupModule()

    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(u'[section]\n')
    config.write(u'key = value\n')
    config.write(u'key2 = value2\n')
    config.seek(0, os.SEEK_SET)

    lm.cp = configparser.ConfigParser()
    lm.cp.readfp(config)

    assert lm.get_value('key', 'section', 'default_value', False) == 'value'
    assert lm.get_value('key', 'section', 'default_value', True) == ['value']
    assert lm.get_value('key3', 'section', 'default_value', False) == 'default_value'
    assert lm.get

# Generated at 2022-06-13 13:56:13.728384
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Startup
    lookup_plugin = LookupModule()

    # Default values
    assert lookup_plugin.run([]) == []

    # Without params
    assert lookup_plugin.run(['user']) == ['John Doe']

    # With params property file
    assert lookup_plugin.run(['user.name'], variable=dict(type='properties', file='properties.ini')) == ['John Doe']

    # With params
    assert lookup_plugin.run(['user', 'password'], variable=dict(section='test', file='test.ini')) == ['Bob', 'secret']

    # With params and regexp
    assert lookup_plugin.run(['user*'], variable=dict(section='test', file='test.ini', re=True)) == ['Bob', 'John']

    # Test if_exists
    assert lookup_plugin

# Generated at 2022-06-13 13:56:25.792114
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import pytest
    from ansible.plugins.lookup.ini import LookupModule
    from io import StringIO
    config = StringIO()
    config.write(
      u"""
      [defaults]
      a = b
      [section1]
      a = b
      """
    )
    config.seek(0, os.SEEK_SET)
    cp = configparser.RawConfigParser()
    cp.readfp(config)
    lm = LookupModule()
    lm.cp = cp
    assert lm.get_value("a", "section1", "dflt", False) == u"b"
    assert lm.get_value("a", "section2", "dflt", False) == u"dflt"

# Generated at 2022-06-13 13:56:27.661429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 13:56:38.122799
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    lookup_module = LookupModule()
    cp = configparser.ConfigParser(allow_no_value=True)

    sectionName = "section1"
    cp.add_section(sectionName)
    cp.set(sectionName, "key1", "value1")
    cp.set(sectionName, "key2", "value2")
    cp.set(sectionName, "test", "value3")
    cp.set(sectionName, ".*", "value4")
    cp.set(sectionName, ".*|test", "value5")

    lookup_module.cp = cp

    assert lookup_module.get_value("key1", sectionName, "", False) == "value1"
    assert lookup_module.get_value("key1", sectionName, "", True) == "value1"

# Generated at 2022-06-13 13:56:44.825327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialisation
    lookupModule = LookupModule()
    lookupModule.cp = configparser.ConfigParser()
    lookupModule.cp.readfp(StringIO(u"[section1]\n"
                                    "key1=value1\n"
                                    "key2=value2\n"
                                    "key3=value3\n"
                                    "key4=value4\n\n"
                                    "[section2]\n"
                                    "key1=value5\n"
                                    "key2=value6\n"
                                    "key3=value7\n"
                                    "key4=value8\n"))

    # Test 1 : read a key that exists in a section

# Generated at 2022-06-13 13:56:53.045713
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test LookupModule.run
    lookup = LookupModule()

    # Test property file without section (type=properties)
    ini_file = '''user.name=Ansible User
    '''
    lookup.cp = configparser.ConfigParser(allow_no_value=True)
    if lookup.cp.optionxform('NO_SENSITIVE'):
        lookup.cp.optionxform = to_native
    config = StringIO()
    config.write(ini_file)
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)
    lookup.cp.options('java_properties')
    assert lookup.get_value('user.name', 'java_properties', '', False) == 'Ansible User'

# Generated at 2022-06-13 13:57:03.696538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Parameter check
    try:
        LookupModule.run(None, None)
    except Exception as e:
        assert(str(e) == "terms parameter is required")

    try:
        LookupModule.run(None, None, file=None)
    except Exception as e:
        assert(str(e) == "terms parameter is required")

    # Empty
    result = LookupModule.run(None, None, file='')
    assert(result == [])

    # Read ini file
    result = LookupModule.run(None, None, file='tests/files/test.ini')
    assert(result == [])

    result = LookupModule.run(None, None, file='tests/files/test.ini', section='section1', key='key1')
    assert(result == ['value1'])

# Generated at 2022-06-13 13:57:05.476839
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert l is not None


# Generated at 2022-06-13 13:57:15.634894
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleUnicode
    if PY3:
        from configparser import ConfigParser
    else:
        from ConfigParser import ConfigParser
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    m = lookup_loader.get('ini', loader=None, templar=None)

    class MockVariableManager():
        def __init__(self):
            self.vars = {
                "env": "prod",
                "dynamic_inventory_path": "%(playbook_dir)s/../dynamic_inventory.py",
            }


# Generated at 2022-06-13 13:57:28.335127
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section("section")
    l.cp.set("section", "key1", "value1")
    l.cp.set("section", "key2", "value2")
    l.cp.set("section", "key3", "value3")
    l.cp.set("section", "key4", "value4")

    assert l.get_value("key1", "section", "", False) == "value1"
    assert l.get_value("key2", "section", "", False) == "value2"
    assert l.get_value("key5", "section", "default", False) == "default"

# Generated at 2022-06-13 13:57:57.801880
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    obj = LookupModule()

    # check that the method returns a list when highlight is a regexp
    section = "section1"
    dflt = "default"
    is_regexp = True
    obj.cp = configparser.ConfigParser()
    obj.cp.add_section(section)
    obj.cp.set(section, "foo", "FOO")
    obj.cp.set(section, "bar", "BAR")
    value = obj.get_value("fo*", section, dflt, is_regexp)
    assert(isinstance(value, MutableSequence))
    assert(len(value) == 1)
    assert(value[0] == "FOO")
    value = obj.get_value("f*", section, dflt, is_regexp)

# Generated at 2022-06-13 13:58:06.002573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def mocked_find_file_in_search_path(variables, pathname, filename):
        # Return the filepath of the file in argument
        return filename
    def mocked_get_file_contents(filepath):
        # Return a predefined filepath
        return "{section1: {key1: 'value1'}}", filepath

    lookup_plugin = LookupModule()

    lookup_plugin.find_file_in_search_path = mocked_find_file_in_search_path
    lookup_plugin._loader.get_file_contents = mocked_get_file_contents

    terms = ["key1", "key2", "key3", "key4", "key5"]
    expected_results = ["value1", "value2", "value3", "value4", "value5"]

# Generated at 2022-06-13 13:58:10.245464
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.lookup import LookupBase

    class DummyLookupModule(LookupBase):

        def run(self, terms, variables=None, **kwargs):
            return terms


# Generated at 2022-06-13 13:58:21.236792
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lmodule = LookupModule()
    mock_configparser = MockConfigParser()

    lmodule.cp = mock_configparser

    # Test get value with regex
    assert lmodule.get_value('key[0-9]+', 'section1', 'value1', True) == ['value2', 'value3']

    # Test get a single value
    assert lmodule.get_value('key1', 'section1', 'value1', False) == 'value1'

    # Test get not existing value
    assert lmodule.get_value('key4', 'section1', 'value1', False) == 'value1'

    # Test get value on unexisting section
    with pytest.raises(AnsibleLookupError):
        lmodule.get_value('key1', 'section2', 'value1', False)


# Generated at 2022-06-13 13:58:34.536412
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class MockLookupModule:
        def __init__(self):
            self.cp = configparser.ConfigParser()
            config = StringIO()
            config.write(u'[section1]\n')
            config.write(u'option1=value1\n')
            config.write(u'option2=value2\n')
            config.write(u'[section2]\n')
            config.write(u'option3=value3\n')
            config.seek(0, os.SEEK_SET)
            self.cp.readfp(config)

    lookup_module = LookupModule()
    lookup_module.get_value = MockLookupModule.get_value
    assert lookup_module.get_value("option1", "section1", "default", False) == "value1"
    assert lookup

# Generated at 2022-06-13 13:58:45.499360
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import configparser
    from units.mock.loader import DictDataLoader

    lk = LookupModule()
    lk.set_loader(DictDataLoader({}))

    expected_result = [u'test', u'value']
    result = lk.run(terms=['test', 'test2'], variables={}, file='test.ini', section='section1', re=True)
    assert result == expected_result

    expected_result = [u'test']
    result = lk.run(terms=['test2'], variables={}, file='test.ini', section='section1', re=True)
    assert result == expected_result

    expected_result = [u'test', u'value']

# Generated at 2022-06-13 13:58:57.189911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest

    # Create a simple ini file
    ini_file = u"""# This is a comment
; This is also a comment

[section1]
key1=value1
key2=value2
key3=value3

[section2]
; This is a comment
key4=value4
key5=value5
key6=value6
"""
    # Create a simple Java properties file
    properties_file = u"""# This is a comment
; This is also a comment

user.name=value1
user.password=value2
user.hostname=value3

[section2]
; This is a comment
key4=value4
key5=value5
key6=value6
"""


# Generated at 2022-06-13 13:59:08.567176
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test the basic case
    lookup = LookupModule()
    assert lookup.run([u"user"], {u'files': u'.files'}, file=u'ansible.ini') == [u'alice']

    # Add params to the terms
    terms = [u"user file=users.ini"]
    assert lookup.run(terms, {u'files': u'.files'}) == [u'alice']

    # Check the section param
    terms = [u"user section=integration"]
    assert lookup.run(terms, {u'files': u'.files'}) == [u'bob']

    # Check the type param
    assert lookup.run([u"user.name type=properties"], {u'files': u'.files'}) == [u'Alice']

    # Check the default param

# Generated at 2022-06-13 13:59:20.702279
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six.moves import StringIO
    from ansible.plugins.lookup import LookupModule

    # Unit test to test method run of class LookupModule
    # Given a file containing
    # [section1]
    # key1=value1
    # key2=value2
    # key3=value3
    #
    # [section2]
    # key1=value1
    # key2=value2
    # key3=value3
    #
    # [section3]
    # key1=value1
    # key2=value2
    # key3=value3
    #
    # [section4]
    # key1_section4=value1
    # key2_section4=value2
    # key3_section4=value3
    #
    #

# Generated at 2022-06-13 13:59:30.623412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test no section or key
    try:
        lookup.run([])
    except AnsibleLookupError:
        pass

    # test empty section
    try:
        lookup.run([""], section="")
    except AnsibleLookupError:
        pass

    # test no section specified
    try:
        lookup.run(["key"])
    except AnsibleLookupError:
        pass

    # test no section specified but section in term
    try:
        lookup.run(["[section]"])
    except AnsibleLookupError:
        pass

    # test no key specified
    try:
        lookup.run([], section="section")
    except AnsibleLookupError:
        pass

    # test no key specified but key in term

# Generated at 2022-06-13 14:00:17.209866
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Method get_value should return the value of a key if it exists in the given section of the ini file,
    # the given default value if the key does not exist in the given section, and
    # a list of values if the key is a regexp that match several keys in the given section of the ini file.
    l = LookupModule()
    config2 = StringIO()
    config2.write(u'[section1]\n')
    config2.write(u'key4=value4\n')
    config2.write(u'key5=value5\n')
    config2.seek(0, os.SEEK_SET)
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'key1=value1\n')

# Generated at 2022-06-13 14:00:24.090560
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from collections import defaultdict

    # Simple value
    lm = LookupModule()

    lm.cp = configparser.ConfigParser()
    lm.cp.optionxform = to_native
    lm.cp.add_section("section_1")
    lm.cp.set("section_1", "prop_1", "test_1")

    assert lm.get_value("prop_1", "section_1", "test_2", False) == "test_1"

    # Multiple values
    lm = LookupModule()

    lm.cp = configparser.ConfigParser()
    lm.cp.optionxform = to_native
    lm.cp.add_section("section_1")
    lm.cp.set("section_1", "prop_1", "test_1")
    l

# Generated at 2022-06-13 14:00:35.245798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup_module = LookupModule()

    ############################################################################################
    ##
    ##                           test_get_value_with_regexp
    ##
    ############################################################################################
    #
    # valid input parameters
    #
    # test get_value with a regexp
    # test get_value with an empty key
    # test get_value with a regexp not matching any key
    # test get_value with a key corresponding to a list of keys
    # test get_value with a key corresponding to several values
    # test get_value with a key corresponding to empty values
    # test get_value with a key corresponding to an empty line
    # test get_value with a key corresponding to several empty lines
    # test get_value with a key corresponding to a single empty line
    # test get_value with

# Generated at 2022-06-13 14:00:42.743172
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    class TestLookupModule(LookupModule):

        class configparser():

            @staticmethod
            def ConfigParser(allow_no_value):
                return {}

            @staticmethod
            def items(section):
                if section == "section1":
                    return [("key", "value")]
                else:
                    return []

            @staticmethod
            def get(section, option):
                if section == "section1" and option == "key":
                    return "value"
                else:
                    return None

        class ansible_options():

            case_sensitive = True
            allow_no_value = False

        def __init__(self):
            self.cp = TestLookupModule.configparser().ConfigParser(self.ansible_options.allow_no_value)
            self.ansible_options = TestLookupModule.ans

# Generated at 2022-06-13 14:00:53.199712
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create lookup
    lookup_plugin = LookupModule()

    # Create configuration
    config = StringIO()
    config.write("""[section1]
key1 = valueA
key2 = valueB

[section2]
key1 = valueC
key2 = valueD
""")
    config.seek(0, os.SEEK_SET)

    # Parse configuration
    cp = configparser.ConfigParser()
    cp.readfp(config)

    # Create lookup object
    lookup_plugin.cp = cp

    # Test match with key and section
    results = lookup_plugin.get_value("key1", "section1", "", False)
    assert results == "valueA"

    # Test match with regexp and section
    results = lookup_plugin.get_value(".*", "section1", "", True)

# Generated at 2022-06-13 14:01:05.043316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import sys
    # sys.path.append('/Users/yannig/PycharmProjects/ansible/lib/ansible/plugins/lookup')
    # from ini import LookupModule

    import platform
    is_macos = platform.system() is 'Darwin'
    if is_macos:
        encoding = 'utf-8'
    else:
        encoding = 'latin-1'
    lookup = LookupModule()

    # test get type properties with a value
    result = lookup.run([
        'user.name=Yannig',
        'user.surname=Perre'], variables={'user.password': 'pwd'}, type='properties', file='user.properties',
                                 encoding=encoding, re=False)

# Generated at 2022-06-13 14:01:15.563987
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('\n>>> test_LookupModule_run: START')
    lm = LookupModule()
    # Test deprecated parameters
    for term in ['a', 'a=b', 'a=b ', 'a=b  ', 'a=b x=y']:
        print('Test term : %s' % term)
        try:
            lm.run([term])
        except AnsibleOptionsError as err:
            assert 'first term' in str(err), 'Error expected when deprecated parameters are used.'
        else:
            raise AssertionError('AnsibleOptionsError not raised')
    # Test mandatory parameters

# Generated at 2022-06-13 14:01:27.359047
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Note: test is not run inside the plugin unit test framework because
    # plugins have a dependency on a playbook.

    # TODO: implement for ansible 2.4
    # TODO: use mock for side effect
    # TODO: remove deprecated `do_lookup_params`
    return

    class Options():
        default = ''
        case_sensitive = False
        allow_none = False
        type = 'ini'
        re = False
        encoding = 'utf-8'
        section = 'global'
        file = 'ansible.ini'

    optionvals = Options()

    class ConfigParser():
        def __init__(self, allow_no_value):
            pass

    class LookupModule(plugins.lookup.LookupModule):
        def set_options(self, **kwargs):
            return optionvals


# Generated at 2022-06-13 14:01:38.026040
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # create the config parser
    config = configparser.ConfigParser(allow_no_value=True)
    config.add_section("section1")
    config.add_section("section2")
    config.set("section1", "key1", "value1")
    config.set("section1", "key2", "value2")
    config.set("section1", "key3", "value3")
    config.set("section2", "key4", "value4")

    lookupModule = LookupModule()

    # false for not using regexp
    assert lookupModule.get_value("key1", "section1", "", False) == "value1"
    assert lookupModule.get_value("key2", "section1", "", False) == "value2"

# Generated at 2022-06-13 14:01:48.979518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # TODO: test options in params
    # TODO: test option file with file not in searchpath

    # # test sections:
    # get value of key 'user' in section 'integration' in file users.ini
    ret = lookup.run([u'user', u'section=integration', u'file=users.ini'])
    assert ret == [u'ibou'], ret
    # get value of key 'user' in section 'integration' in file users.ini
    ret = lookup.run([u'user', u'file=users.ini', u'section=integration'])
    assert ret == [u'ibou'], ret
    # get value of key 'user' in section 'production' in file users.ini