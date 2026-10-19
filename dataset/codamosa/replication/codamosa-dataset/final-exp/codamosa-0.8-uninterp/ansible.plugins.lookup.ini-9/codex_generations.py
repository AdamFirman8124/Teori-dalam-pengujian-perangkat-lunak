

# Generated at 2022-06-13 13:52:35.904690
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    my_lookup = LookupModule()
    my_lookup.cp = configparser.ConfigParser()
    my_lookup.cp.add_section('section')
    my_lookup.cp.set('section','key','value')
    assert my_lookup.get_value('key', 'section', None, False) == 'value'
    assert my_lookup.get_value('foo', 'section', 'bar', False) == 'bar'
    assert my_lookup.get_value('\d', 'section', 'regexp error', True) == ['value']

# Generated at 2022-06-13 13:52:45.570764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    params = {'file': 'ini.ini', 'default': '', 'encoding': 'utf-8', 're': True, 'case_sensitive': False,
              'allow_no_value': False}
    lm.set_options(var_options={}, direct=params)
    terms = ['user']
    ret = lm.run(terms)
    assert ret == ['yannig']
    params = {'file': 'ini.ini', 'default': '', 'encoding': 'utf-8', 're': True, 'case_sensitive': False,
              'allow_no_value': False}
    lm.set_options(var_options={}, direct=params)
    terms = ['user', 'group']
    ret = lm.run(terms)

# Generated at 2022-06-13 13:52:57.533491
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get instance of LookupModule
    lookModule = LookupModule()

    # Gives the path of the file test
    filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.ini')

    # Gives the path of the file test
    filePropertiesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.properties')

    # Gives the path of the file test
    nonExistFilePath = os.path.join('non', 'exist', 'file', 'vars.ini')

    # Get the path of the file for the test with non empty value

# Generated at 2022-06-13 13:53:05.765675
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a file for testing
    with open('test.ini', 'w') as testfile:
        testfile.write('[section1]\n')
        testfile.write('test = toto\n')
        testfile.write('test2 = titi\n')
        testfile.write('test3 = tata\n')
        testfile.write('test4 = tutu\n')
        testfile.write('[section2]\n')
        testfile.write('test = 1\n')
        testfile.write('test2 = 2\n')
        testfile.write('test3 = 3\n')
        testfile.write('test4 = 4\n')
        testfile.write('[section3]\n')
        testfile.write('test = 1\n')

# Generated at 2022-06-13 13:53:16.544162
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Init a Mock class
    class MockLookupModule(LookupModule):

        def __init__(self):
            self.cp = configparser.ConfigParser()
            self.cp.add_section('section1')
            self.cp.set('section1', 'key1', 'val1')
            self.cp.set('section1', 'key2', 'val2')
            self.cp.set('section1', 'key3', 'val3')
            self.cp.add_section('section2')
            self.cp.set('section2', 'key1', 'val1')
            self.cp.set('section2', 'key2', 'val2')
            self.cp.set('section2', 'key3', 'val3')
            self.cp.set('section2', 'key4', 'val4')



# Generated at 2022-06-13 13:53:29.374007
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    cp = configparser.ConfigParser()
    data = """[section]
key1=value1
key2=value2
key3=value3
key4=value4
key5=value5"""
    config = StringIO()
    config.write(data)
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)

    lk = LookupModule()
    lk.cp = cp
    assert lk.get_value('key1', 'section', None, False) == "value1"
    assert lk.get_value('key1', 'section', None, True)  == ['value1']
    assert lk.get_value('key1', 'section', 'default', False) == "value1"

# Generated at 2022-06-13 13:53:37.175474
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.set_inventory(DataLoader().load_inventory("localhost,"))
    variable_manager._extra_vars = {"var": "global" }
    # Test lookup key in parameter without [section]
    lookup = LookupModule()
    lookup.set_loader(DataLoader())
    lookup.set_options(var_options=variable_manager)
    terms = ["variable"]
    results = lookup.run(terms, variables={"var": "variable"})
    assert(results == ["variable"])
    results = lookup.run(terms, variables={"var": "var"})
    assert(results == ["global"])

# Generated at 2022-06-13 13:53:45.429793
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Case 1: section = global and user = root
    test_class = LookupModule()
    test_class.cp = configparser.ConfigParser()
    test_class.cp.add_section(u'global')
    test_class.cp.set(u'global', u'user', u'root')

    res = test_class.run([u'user'])
    assert res == [u'root'], "res should be ['root']"

    # Case 2: section = global and user = ['root', 'toto']
    test_class = LookupModule()
    test_class.cp = configparser.ConfigParser()
    test_class.cp.add_section(u'global')
    test_class.cp.set(u'global', u'user', u'root, toto')

    res = test_class

# Generated at 2022-06-13 13:53:55.763659
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    tmp_config = configparser.ConfigParser()
    tmp_config.add_section('test_section')
    tmp_config.set('test_section', 'test_key', 'test_value')
    ini_file = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    ini_file.cp = tmp_config

    # Retrieve value using a regexp
    regexp_test = ini_file.get_value('.*key', 'test_section', None, True)
    assert regexp_test == ['test_value']

    # Retrieve a single value
    assert ini_file.get_value('test_key', 'test_section', None, False) == 'test_value'

    # Test when value not set

# Generated at 2022-06-13 13:54:06.758258
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Test with a regexp
    cp = configparser.ConfigParser()
    cp.readfp(StringIO(u'''
    [section]
    key1 = value1
    key2 = value2
    key3 = value3
    '''))
    lm = LookupModule(None, None, None, None)
    lm.cp = cp
    assert lm.get_value('^key[12]', 'section', None, True) == ['value1', 'value2']

    # Test with a key
    cp = configparser.ConfigParser()
    cp.readfp(StringIO(u'''
    [section]
    key1 = value1
    key2 = value2
    key3 = value3
    '''))
    lm = LookupModule(None, None, None, None)
    l

# Generated at 2022-06-13 13:54:21.025896
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    cp = configparser.ConfigParser()

    # Create StringIO later used to parse ini
    config = StringIO()

    # Write to StringIO
    config.write('[global]\n')
    config.write('user=john\n')

    config.write('[integration]\n')
    config.write('user=john\n')

    config.write('[production]\n')
    config.write('user=jack\n')

    config.seek(0, os.SEEK_SET)

    cp.readfp(config)

    lu = LookupModule()
    lu.cp = cp
    assert 'john' == lu.get_value('user', 'production', 'default', False)
    assert 'jack' == lu.get_value('user', 'production', 'default', False)
   

# Generated at 2022-06-13 13:54:34.884837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # ConfigParser.read returns an empty list
    mock_ConfigParser_read = []

    # ConfigParser.sections returns a list with the sections
    mock_ConfigParser_sections = ['section1', 'section2', 'section3']

    # ConfigParser.items return a list of (key, value) items
    # for a given section
    mock_ConfigParser_items = [('key1', 'value1'), ('key2', 'value2')]

    # ConfigParser.get return the value for a given section and key
    mock_ConfigParser_get = 'value1'

    # ConfigParser.__init__ return an object
    mock_ConfigParser = lambda param: None

    # StringIO.seek return always 0
    mock_StringIO_seek = lambda param1, param2: 0

    # StringIO.write returns the lenght of the string

# Generated at 2022-06-13 13:54:45.739970
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO, configparser
    if PY3:
        string_types = str,
    else:
        string_types = basestring,

    lookup_module = LookupModule()

    class MockSearchPath(dict):

        def __init__(self, search_path):
            super(MockSearchPath, self).__init__(self)
            self.search_path = search_path

        def __getitem__(self, name):
            return self.search_path

    # Test the first use case: read the value of 'user' in section 'integration'.
    # This test case checks if the value returned is the expected one: 'admin'.
    # An 'ansible.ini' file is created to test

# Generated at 2022-06-13 13:54:58.612178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test `type` parameter
    try:
        lookup.run(["key1"], type="abc")
    except AnsibleOptionsError as e:
        assert str(e) == "Invalid value used for \"type\": 'abc' is not a valid choice. Value must be one of: 'ini', 'properties'"
        pass

    # Test `file` parameter
    try:
        lookup.run(["key1"], file="/tmp/abc")
    except AnsibleOptionsError as e:
        assert str(e) == "The file '/tmp/abc' does not exist"
        pass

    # Test `re` parameter

# Generated at 2022-06-13 13:55:05.621071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section("global")
    l.cp.set("global", "user", "ansible")
    l.cp.add_section("integration")
    l.cp.set("integration", "user", "yannig")
    l.cp.add_section("production")
    l.cp.set("production", "user", "perre")

    assert l.run([["user", "section=integration"], ["user", "section=production"]], None, file="users.ini") == ["yannig", "perre"]

# Generated at 2022-06-13 13:55:17.499607
# Unit test for method run of class LookupModule
def test_LookupModule_run():  # noqa: E501
    from nose.tools import assert_equal, assert_true  # noqa

    # Setup test case
    terms = ['database', 'user', 'password']
    section = 'integration'
    file = 'config.ini'
    encoding = 'latin-1'
    params = dict(encoding=encoding, file=file, section=section,
                  type='ini', case_sensitive=False, allow_no_value=False)
    l = LookupModule()
    l.set_options(var_options=dict(), direct=params)

    with open(file, "r") as f:
        config = StringIO()
        config.write(to_text(f.read(), errors='surrogate_or_strict', encoding=encoding))

# Generated at 2022-06-13 13:55:28.569792
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Test with simple ini file
    lookup_options = {'file': 'myhost.ini',
                      'section': 'computers',
                      '_terms': ['hostname']}

    params = {'file': 'myhost.ini',
              'default': 'localhost',
              'section': 'computers',
              '_terms': ['hostname']}

    mylookup = LookupModule()
    mylookup.set_loader(loader)

    assert mylookup.run(**lookup_options) == ['localhost']

    # Test with a wrong section
    lookup_options['section'] = 'foo'
    params['section'] = 'foo'


# Generated at 2022-06-13 13:55:33.689901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: test everything defined in doc (see top of file)
    # from ansible.plugins.lookup.ini import LookupModule
    # l = LookupModule()
    # result = l.run([], [])
    # assert result == []
    pass

# Generated at 2022-06-13 13:55:45.299812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test no parameter
    # Possible result:
    #   [ansible]
    #   host_key_checking = False
    #   [defaults]
    #   ask_sudo_pass = True
    #   [privilege_escalation]
    #   become = True

    terms = []
    terms.append('')
    terms.append('[ansible]')
    terms.append('host_key_checking = False')
    terms.append('[defaults]')
    terms.append('ask_sudo_pass = True')
    terms.append('[privilege_escalation]')
    terms.append('become = True')
    var = StringIO()
    var.write(u'')
    var.seek(0, os.SEEK_SET)
    my_lookup_module = LookupModule()

# Generated at 2022-06-13 13:55:52.505156
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test for standard lookup in a section
    t = LookupModule([])
    t.parser = configparser.ConfigParser()
    t.parser.add_section('section')
    t.parser.set('section', 'key1', 'value1')
    t.parser.set('section', 'key2', 'value2')

    assert t.get_value('key1', 'section', None, False) == 'value1'
    assert t.get_value('key3', 'section', ['default_value'], False) == ['default_value']

    # Test for regexp lookup
    assert t.get_value('^key', 'section', [], True) == ['value1', 'value2']
    assert t.get_value('^key[12]$', 'section', None, True) == ['value1', 'value2']

# Generated at 2022-06-13 13:56:04.922877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Assert
    assert True == False

# Generated at 2022-06-13 13:56:15.509328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: This test should be moved to unit/gather/lookup/test_ini.py
    # and test *all* functions in the LookupModule class

    lookup = LookupModule()

    terms = [
        "user.name",
        "user.age",
        "user.location",
        "user.male",
        "user.schools"
    ]

    # Create StringIO to parse as file
    config = StringIO()
    config.write(u'[java_properties]\n')
    config.write(u'user.name = Charles\n')
    config.write(u'user.age = 50\n')
    config.write(u'user.location = New York\n')
    config.write(u'user.male = true\n')

# Generated at 2022-06-13 13:56:26.436086
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Parameters
    terms = ["user", "password"]
    variables = {"hostname": "localhost"}
    kwargs = {"_ansible_tmpdir": "ansible", "allow_none": False, "allow_no_value": False, "case_sensitive": False, "default": "", "encoding": "utf-8", "file": "ansible.ini", "re": False, "section": "global", "type": "ini"}
    # Option -v (verbose) must be False because it is used in LookupModule and True
    # in the assertEqual of ansible.module_utils.six.moves.configparser.ConfigParser

# Generated at 2022-06-13 13:56:34.127904
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MyLookupModule(LookupModule):
        def __init__(self):
            super(MyLookupModule, self).__init__()

        def run(self, terms, variables=None, **kwargs):
            return 'test_value'

    lookup = MyLookupModule()
    result = lookup.run(['test_key'], [], file='user.ini', section='jira', default='test_value')
    assert result == 'test_value'

# Generated at 2022-06-13 13:56:47.070127
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    vars = ["user=","username=","user.name=","user"]
    section = "integration"
    is_regexp = True
    in_file = "users.ini"
    dflt = "false"
    test = LookupModule()

    test.cp = configparser.ConfigParser()
    path = test.find_file_in_search_path(vars, 'files', in_file)

    # Create StringIO later used to parse ini
    config = StringIO()

    # Open file using encoding
    contents, show_data = test._loader._get_file_contents(path)
    contents = to_text(contents, errors='surrogate_or_strict', encoding='utf-8')
    config.write(contents)
    config.seek(0, os.SEEK_SET)

# Generated at 2022-06-13 13:56:55.444506
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    l = {"section1": {"key1": "value1"}, "section2": {"key2": "value2"}}
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.read_dict(l)

    # Normal mode
    terms = ["key1"]
    paramvals = {"section": "section1", "re": False}
    ret = lookup_module.get_value(terms[0], paramvals["section"], None, paramvals["re"])
    assert "value1" == ret

    # Regex mode
    terms = [".*"]
    paramvals = {"section": "section1", "re": True}
    ret = lookup_module.get_value(terms[0], paramvals["section"], None, paramvals["re"])

# Generated at 2022-06-13 13:57:04.619240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create mock_lookup object
    class MockLookupModule(object):
        # Mock method to return a specific value
        def find_file_in_search_path(self, variables, directory, filename):
            return filename

        # Mock method to return a specific value
        def _get_file_contents(self, path):
            class _StringIO(StringIO):
                # Mock method to return a specific value
                def close(self):
                    pass
            # Create StringIO to mock a file
            test_string = '[global]\nuser=yannig\n'
            config = _StringIO(test_string)
            return config, 'fake_data'

    # Create mock_loader object for the _loader attribute

# Generated at 2022-06-13 13:57:13.136464
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyClass:
        pass

    dummy = DummyClass()
    lookup = LookupModule()
    lookup.set_options(var_options=None, direct=None)
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(open("/tmp/ansible.ini"))
    ret = lookup.get_value("user", "integration", "pas de user", False)
    assert ret == "lna"
    ret = lookup.get_value("user", "production", "pas de user", False)
    assert ret == "pas de user"

# Generated at 2022-06-13 13:57:25.786132
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.parsing.dataloader import DataLoader
    class TestLookupModule(LookupModule):
        def _flatten(self, terms, variables=None, **kwargs):
            return terms

    lookup = TestLookupModule()
    loader = DataLoader()
    contents = """
[section1]
key=val
[section2]
key=val
"""
    lookup.cp = configparser.ConfigParser()
    # Create StringIO later used to parse ini
    config = StringIO()
    # Special case for java properties
    config.write(u'[java_properties]\n')
    paramvals = {'section': 'java_properties'}
    # Open file using encoding
    config.write(contents)
    config.seek(0, os.SEEK_SET)

# Generated at 2022-06-13 13:57:29.865575
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    file = 'tests/ini/users.ini'
    section = 'integration'
    key = 'user'
    expected_value = 'ygalop'
    actual_value = ''
    actual_value = LookupModule().run(terms=[key], variables={}, file=file, section=section)[0]
    assert actual_value == expected_value, "Actual value '" + actual_value + "' is different from expected value '" + expected_value + "'"

    section = 'production'
    expected_value = 'root'
    actual_value = ''
    actual_value = LookupModule().run(terms=[key], variables={}, file=file, section=section)[0]

# Generated at 2022-06-13 13:57:56.858503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    lookupModule = LookupModule()

    # Act
    ret = lookupModule.run([''], variables={}, type="properties", file="user.properties", re="False", section="global", encoding="utf-8")

    # Assert
    assert ret == []

# Generated at 2022-06-13 13:58:05.708040
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Unit test for method run of class LookupModule '''

    lookup_module = LookupModule()

    # Initializes lookup_module
    lookup_module.set_options()
    lookup_module.cp = configparser.ConfigParser(allow_no_value=True)

    lookup_module.cp.add_section("global")
    lookup_module.cp.set("global", "key1", "value1")
    lookup_module.cp.set("global", "key2", "value2")
    lookup_module.cp.set("global", "key3", "value3")
    lookup_module.cp.set("global", "key3", "value3")

    lookup_module.cp.add_section("section")
    lookup_module.cp.set("section", "key1", "value1")

# Generated at 2022-06-13 13:58:16.934161
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class DummyLookup(LookupModule):

        def find_file_in_search_path(self, variables, search_path, file):
            return '/some/dir/file.ini'

        def get_value(self, key, section, dflt, is_regexp):
            return 'foo'

    l = DummyLookup()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('foo')
    l.cp.set('foo', 'key', 'value')
    ret = l.run(['key'], dict(), file='file.ini', section='foo')
    assert ret == ['foo']

# Generated at 2022-06-13 13:58:24.775236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.cp  = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.set('section1', 'key3', 'value3')
    lookup.cp.set('section1', 'key4', 'value4')
    lookup.cp.set('section1', 'key5', 'value5')
    lookup.cp.set('section1', 'key6', 'value6')
    lookup.cp.set('section1', 'key7', 'value7')
    lookup.cp.set('section1', 'key8', 'value8')

# Generated at 2022-06-13 13:58:30.879503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test LookupModule run method
    lookup_module_obj = LookupModule()

    # Create a string-element list to be used as term of LookupModule.run()
    term_list = [
        u"key1=value1",
        u"key2=value2",
        u"key3=value3=value4",
        u"key4 value5",
        u"key5",
        u"key6=value6 value7",
        u"key7 value8=value9",
    ]

    # Create a set of valid options for the method

# Generated at 2022-06-13 13:58:42.311436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: update this test
    '''
    input:
      terms: [ 'user1', 'user2']
      file: 'users.ini'
    '''

    # TODO: use Ansible Mock instead
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager()
    variable_manager = VariableManager(loader=lookup_loader, inventory=inventory)
    test_lookup = lookup_loader.get('ini')

    assert test_lookup.run(terms=['user1', 'user2'], variables=variable_manager, file='users.ini') == ['Titi', 'Toto']

# Generated at 2022-06-13 13:58:54.306414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Test:
        def __init__(self, tmp_path):
            self.tmp_path = tmp_path
            self.test_file = self.tmp_path / 'ansible.ini'
            self.test_file.write_text(text='[global]\nuser=ansible\n' +
                                           '[integration]\nuser=yperre\n' +
                                           '[production]\nuser=jdehaan\n',
                                      encoding='utf-8')
            self.test_file2 = self.tmp_path / 'users.ini'

# Generated at 2022-06-13 13:59:02.365753
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['./test/inventory'])
    var_manager = VariableManager(loader=loader, inventory=inv_manager)
    play_source = dict(
        name="test",
        hosts="all",
        gather_facts="no",
        tasks=[
            dict(
                name="test",
                lookup="ini",
                register="ini_values"
            ),
        ]
    )


# Generated at 2022-06-13 13:59:12.430753
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check property file
    lookup_params = {
        'type': 'properties',
        'default': 'user.name=',
        'file': 'user.properties',
        'section': 'java_properties',
        're': False,
        'case_sensitive': False,
        'allow_no_value': False,
    }
    lm = LookupModule(loader=None, templar=None)
    config = lm.run([], lookup_params)
    assert isinstance(config, list), "parse_properties return value should be a list"
    assert len(config) == 1, "there is only one key"
    assert config[0] == 'user.name=yperre', "parse_properties should return the right value"

    # Check ini file

# Generated at 2022-06-13 13:59:18.749429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils import common as module_common

    # Create a file named test_LookupModule_run_file.ini
    with open("test_LookupModule_run_file.ini", 'w') as configfile:
        configfile.write("[section1]\n")
        configfile.write("foo=bar\n")
        configfile.write("foo1=foo\n")
        configfile.write("foo2=foo\n")
        configfile.write("[section2]\n")
        configfile.write("foo=baz\n")
    configfile.close()
    # Create a file named test_LookupModule_run_file.properties

# Generated at 2022-06-13 14:00:12.885818
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Unit test
    lookup_command = LookupModule()

    # Test with a simple ini file
    terms = ['user0', 'user1', 'user2=user5', 'user3=user6', 'user4']
    variables = {
        'ini_file': {
            'section1': {
                'user0': 'foo',
                'user1': 'bar',
                'user2': 'baz',
                'user4': 'bat'
                }
            }
        }
    kwargs = {
        'file': 'some_file.ini',
        'default': 'hue'
        }
    assert lookup_command.run(terms, variables=variables, **kwargs) == ['foo', 'bar', 'user5', 'user6', 'bat']

    # Test with regexp


# Generated at 2022-06-13 14:00:22.066916
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a new LookupModule object
    lookup_module = LookupModule()

    # Create a configparser object
    cp = configparser.ConfigParser()

    # Create a config file for unit tests
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'value1=test1\n')
    config.write(u'value2=test2\n')
    config.write(u'value3=test3\n')
    config.write(u'[section2]\n')
    config.write(u'value1=test1\n')
    config.write(u'value2=test2\n')
    config.write(u'value3=test3\n')
    config.write(u'[section3]\n')

# Generated at 2022-06-13 14:00:29.708895
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class LookupModule for test and set some options
    class LookupModule_test(LookupModule):
        def __init__(self, basedir=None, **kwargs):
            self.basedir = basedir
        def get_basedir(self, variables):
            return self.basedir
        def run(self, terms, variables=None, **kwargs):
            self.set_options(var_options=variables, direct=kwargs)
            return terms

    lookup_plugin = LookupModule_test(basedir='/home')
    # Check that run return ['item1', 'item2']
    assert lookup_plugin.run(['item1', 'item2'], {'type':'ini', 'file':'test.ini'}) == ['item1', 'item2']

# Generated at 2022-06-13 14:00:40.806753
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Check expected output of method run of class LookupModule"""
    # Section
    section = "section1"
    # Content of file
    ini_content = "[" + section + "]\n" + \
        "key1=value1\n" + \
        "key2=value2\n" + \
        "key3=value3\n" + \
        "key4=value4\n"
    # Configuration file
    ini_file = 'test.ini'
    with open(ini_file, 'w') as f:
        f.write(ini_content)
    # LookupModule
    lm = LookupModule()
    # Run the method
    res = lm.run(['key1', 'key2'], {}, file=ini_file, section=section)
    # Check result

# Generated at 2022-06-13 14:00:51.168435
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Look for a key with a section
    test_subject = LookupModule()
    test_subject.get_options = lambda: {'type': 'ini', 'file': 'file_with_a_section.ini', 'section': "section", 'default': '', 're': False}

    # Execute
    result = test_subject.run(['key'], {})

    assert result == ['value']

    # Look for a key with a section
    test_subject = LookupModule()
    test_subject.get_options = lambda: {'type': 'properties', 'file': 'file_with_no_section.ini', 'default': '', 're': False}

    # Execute
    result = test_subject.run(['key'], {})

    assert result == ['value']

# Generated at 2022-06-13 14:00:57.950696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io
    import os
    import datetime
    import unittest
    import tempfile

    from ansible.plugins.loader import lookup_loader

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            os.environ['ANSIBLE_CONFIG'] = '{0}/test/integration/shared/ansible.cfg'.format(os.environ['PWD'])
            self.context = {}
            self.lookup_loader = lookup_loader._create_lookup_loader(self.context)

        def tearDown(self):
            os.environ.pop('ANSIBLE_CONFIG')
            del self.context
            del self.lookup_loader

        def test_run(self):
            lookup = self.lookup_loader.get('ini')

# Generated at 2022-06-13 14:01:09.880286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    play_source = dict(
        name="test",
        hosts='localhost',
        gather_facts='no',
        tasks=[dict(action=dict(module="fail", args=dict(msg='{{lookup("ini" , "foo" , file="./tests.ini" , section="global", default="ok")}}')))]
    )


# Generated at 2022-06-13 14:01:18.178228
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class MockCp(object):
        def __init__(self, value=None):
            self._value = value

        def get(self, _section, key):
            return self._value

    lm = LookupModule()
    lm.cp = MockCp()

    lm.cp.get = Mock()

    # retrieve a single value
    lm.cp._value = 'foo'
    lm.get_value('bar', 'baz', 'default', False)
    lm.cp.get.assert_called_with('baz', 'bar')

    # return default value if key is not in the ini file
    lm.cp.get = Mock(side_effect=configparser.NoOptionError)
    assert lm.get_value('bar', 'baz', 'default', False) == 'default'

# Generated at 2022-06-13 14:01:28.090316
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence

    path = "tests/files/test.ini"

    # test with no matching key : term = key1, args = section=section1, default=abcd
    term = "key1"
    args = dict(section="section1", default="abcd")
    expected = "abcd"
    actual = LookupModule().run([term], params=args)[0]
    assert actual == expected

    # test with matching key : term = key1, args = section=section1, default=abcd
    term = "key1"
    args = dict(section="section1", default="abcd")
    expected = "value1"
    actual = LookupModule().run([term], params=args)[0]
    assert actual == expected



# Generated at 2022-06-13 14:01:37.149639
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('section')
    l.cp.set('section', 'key1', 'value1')
    l.cp.set('section', 'key2', 'value2')
    l.cp.set('section', 'key3', 'value3')

    ret1 = l.get_value('key1', 'section', None, False)
    assert ret1 == 'value1'

    ret2 = l.get_value('key1', 'section', None, True)
    assert ret2 == ['value1']
