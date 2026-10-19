

# Generated at 2022-06-13 13:52:37.801974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO

    old_stdout = sys.stdout
    with patch("__builtin__.open") as open_mock:
        self = LookupModule('ini')
        open_mock.return_value = StringIO("""[global]
env=test
user=johndoe
""")

        result = self.run([
            "[section1]test=test1",
            "[section2]te=test2",
            "[section2]test=test3",
            "test",
            "test=test1",
            "te=test2",
            "test=test3",
            "file=test.ini",
            "type=ini",
            "re=True"
        ])

        assert len(result) == 5
        assert result[0]

# Generated at 2022-06-13 13:52:46.940534
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test if the ini file can be read
    def test_load(tmpdir, section, file, file_content, key, value, type, encoding):
        test = tmpdir.mkdir("lookup_plugins").join(file)
        test.write(file_content)

        lm = LookupModule()

        if type == "ini":
            terms = [key]
        elif type == "properties":
            terms = [key + "=" + value]

        assert lm.run(terms=terms, variables=dict(files=[str(tmpdir)]),
                     file=file, section=section, type=type, encoding=encoding) == [value]

    # Create a tmp folder
    tmpdir = py.path.local()

    # Test if the ini file can be read using utf-8

# Generated at 2022-06-13 13:52:59.642184
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    # Retrieve all values from a section using a regexp
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('ini')
    lookup.cp.set('ini', 'key1', 'value1')
    lookup.cp.set('ini', 'key2', 'value2')
    lookup.cp.set('ini', 'key3', 'value3')

    key = 'key[0-2]'
    section = 'ini'
    dflt = ''
    is_regexp = True

    assert lookup.get_value(key, section, dflt, is_regexp) == ['value1', 'value2']

    # Retrieve a single value
    key = 'key2'
    section = 'ini'
    dflt = None
    is_regexp

# Generated at 2022-06-13 13:53:11.433084
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Term(object):
        def __init__(self, key, section='', filename='', default='', regexp=False, negate=False):
            self.key = key
            self.section = section
            self.filename = filename
            self.default = default
            self.regexp = regexp
            self.negate = negate

    def test_value(key, section, expected_value):
        term = Term(key, section=section)
        ret = LookupModule().run([term])
        assert ret[0] == expected_value

    def test_value_err(key, section):
        term = Term(key, section=section)

# Generated at 2022-06-13 13:53:17.110372
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options:
        default = None
        file = 'ansible.ini'
        section = 'global'
        re = False
        encoding = 'utf-8'
        allow_no_value = False

    lookup_ins = LookupModule()
    terms = ['user']
    variables = None
    options = Options
    result = lookup_ins.run(terms, variables, options)
    assert result == ['joe']



# Generated at 2022-06-13 13:53:29.967458
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a ini file
    tmp_inifile = open("test.ini", "w")
    tmp_inifile.write("[section1]\n")
    tmp_inifile.write("key1=value1\n")
    tmp_inifile.write("key2=value2\n")
    tmp_inifile.write("key3=value3\n")
    tmp_inifile.close()

# Generated at 2022-06-13 13:53:37.460487
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    li_lookup = LookupModule()
    print(li_lookup.run(["foo", "bar=baz"], {}))  # Expected: ['foo', 'baz']
    print(li_lookup.run(["foo", "[bar=baz"], {}))  # Expected: ['foo', 'baz']
    print(li_lookup.run(["foo", "['bar'=baz"], {}))  # Expected: ['foo', 'baz']
    print(li_lookup.run(["foo", "bar='baz"], {}))  # Expected: ['foo', 'baz']
    print(li_lookup.run(["foo", "'bar'=baz"], {}))  # Expected: ['foo', 'baz']

# Generated at 2022-06-13 13:53:45.600644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test an empty ansible.ini file
    ansible_ini = configparser.ConfigParser()
    ansible_ini.readfp(StringIO(u''))
    lookup_module.cp = ansible_ini

    # Test a file with a parameter specified
    kwargs = {'file': 'ansible.ini', 'section': 'global', 're': False}
    param = 'user=jenkins_operator'
    assert lookup_module.run([param], **kwargs) == []
    assert lookup_module.run(['user'], **kwargs) == []

    # Test a file with no section specified (properties type)
    kwargs = {'file': 'ansible.ini', 'section': 'java_properties', 'type': 'properties', 're': False}

# Generated at 2022-06-13 13:53:56.018922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Test LookupModule_run")

    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(StringIO('[java_properties]\n'))

    # Test case for one key
    terms = ['user']
    variables = {}
    kwargs = {}
    kwargs['file'] = 'ansible.ini'
    kwargs['case_sensitive'] = False
    kwargs['allow_no_value'] = False
    kwargs['encoding'] = 'utf-8'
    kwargs['type'] = 'ini'
    kwargs['re'] = False
    kwargs['section'] = 'global'
    kwargs['default'] = ''

# Generated at 2022-06-13 13:54:06.986442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get the absolute path
    abs_path = os.path.abspath('')
    # Test the section
    # Test the key
    # Test the key with regexp
    # Test the default value
    # Test if the property file contains section
    # Test if the ini file contains multiple values for one key
    # Test get multiple values for one key
    # Test get multiple keys for one section
    # Test the allow_no_value

# Generated at 2022-06-13 13:54:21.263232
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()
    config = StringIO()
    config.write(u'[java_properties]\n')
    config.write(u'# This is a comment\n')
    config.write(u'color=green\n')
    config.write(u'color1=red\n')
    config.seek(0, os.SEEK_SET)

    lm.cp = configparser.ConfigParser()

    lm.cp.readfp(config)

    # Comment
    assert lm.get_value('color', 'java_properties', '', True) == ['green']
    # TODO: Look if possible to handle comment
    #print lm.get_value('#', 'java_properties', '', False)

    # Key  does not exist

# Generated at 2022-06-13 13:54:32.617832
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    terms = 'key1'
    paramvals = {'section': 'section1', 'default': '', 're': False, 'encoding': 'utf-8', 'case_sensitive': False, 'file': 'test.ini', 'allow_none': True}
    cp = configparser.ConfigParser(allow_no_value=True)
    lookup = LookupModule(None)
    lookup.cp = cp
    assert lookup.get_value(terms, paramvals['section'], paramvals['default'], paramvals['re']) == 'value1'
    assert cp.get('section1', 'key1') == 'value1'


# Generated at 2022-06-13 13:54:40.586745
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lu = LookupModule()
    lu.cp = configparser.ConfigParser()
    lu.cp.optionxform = to_native
    lu.cp.add_section('section1')
    lu.cp.set('section1','key1','value1')
    lu.cp.set('section1','key2','value2')
    lu.cp.set('section1','key3','value3')
    assert lu.get_value('key1','section1','', False) == 'value1'
    assert lu.get_value('key1','section1','', True) == 'value1'
    assert lu.get_value('key2','section1','', True) == 'value2'
    assert lu.get_value('key3','section1','', False) == 'value3'

# Generated at 2022-06-13 13:54:45.429504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # StringIO used in a config file
    config_file = StringIO()
    config_file.write(u'[test]\n')
    config_file.write(u'key1=1\n')
    config_file.write(u'key2=2\n')
    config_file.write(u'key3=value1\n')
    config_file.write(u'key4=value2\n')
    config_file.seek(0, os.SEEK_SET)

    # Init LookupModule class
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.readfp(config_file)

    # Get all values from section test
    values = [(k, v) for k, v in l.cp.items('test')]

# Generated at 2022-06-13 13:54:58.212434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    terms = [
        "user",
        "user.name",
        "user=",
        "user =",
        "user = javajoe",
        "user=javajoe",
        "type=properties user=javajoe",
        "type=ini file=ansible.ini user=javajoe",
        "type=properties file=user.properties user.name=javajoe",
        "type=ini file=ansible.ini user.name=javajoe"
    ]
    variables = {}
    kwargs = {}

    # Exercise
    result = {}
    looker_upper = LookupModule()
    for term in terms:
        result[term] = looker_upper.run([term], variables, **kwargs)

    # Verify

# Generated at 2022-06-13 13:55:06.981541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    from ansible.plugins.lookup.ini import LookupModule

    test_ini = StringIO()
    test_ini.write(u"[section1]\n")
    test_ini.write(u"key1=value1\n")
    test_ini.write(u"key2=value2\n")
    test_ini.write(u"key3:value3\n")
    test_ini.write(u"key4\n")
    test_ini.write(u"foo=bar\n")
    test_ini.seek(0, os.SEEK_SET)

    display = Display()

# Generated at 2022-06-13 13:55:21.286329
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # Test case 1: Load ini file with section
    terms = 'user'
    variables = {}
    kwargs = {
        'type': 'ini',
        'file': 'users.ini',
        'section': 'production',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False
    }
    assert lookup.run(terms, variables, **kwargs) == ['admin']

    # Test case 2: Load ini file without section
    terms = 'user.name'
    variables = {}

# Generated at 2022-06-13 13:55:30.342213
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Define LookupModule variable
    lookup = LookupModule()
    # Declare variable containing the file path
    file_name = path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lookup_ini.ini')
    # Give three terms to the method run
    terms = [
             'user',
             'user=john',
             'user=john section=production']
    # Execute LookupModule.run
    lookup.run(terms, variables={}, file=file_name)
    # Define variable containing the result of LookupModule.run
    result = [
              'john',
              'john',
              'bob']
    assert len(result) == len(lookup)

# Generated at 2022-06-13 13:55:43.226609
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock inventory to load the module with
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    # Options are defined in the module's docstring
    options = {'file': 'ansible.ini',
               'section': 'global',
               're': 'False',
               'encoding': 'utf-8',
               'default': ''}
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 13:55:51.745555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import the lookups
    import ansible.plugins
    lookup = ansible.plugins.lookup.ini
    # create lookup
    look = lookup.LookupModule()

    # create terms
    terms = ['user', 'password', 'undefined']

    # create additional variables
    variables = {
        'file': 'users.ini',
        'section': 'integration'
    }

    # test method run
    ret = look.run(terms, variables)
    assert ret[0] == "superuser"
    assert ret[1] == "Password123$"
    assert ret[2] == ""

    # create terms
    terms = ['user', 'password']

    # create additional variables
    variables = {
        'file': 'users.ini',
        'section': 'production'
    }

    # test method run


# Generated at 2022-06-13 13:56:04.638516
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Change the return type to test different cases
    pass

# Generated at 2022-06-13 13:56:13.691287
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'file': 'test.ini', 'section': 'section1'})
    config = StringIO()
    contents = """
[section1]
key1 = value1
key2 = value2
key3 = value3
"""
    config.write(contents)
    config.seek(0, os.SEEK_SET)
    lookup_module.cp.readfp(config)

    # Act
    keys = ['key1', 'key2', 'key3']
    values = lookup_module.run(keys)

    # Assert
    assert values == ['value1', 'value2', 'value3']


# Generated at 2022-06-13 13:56:25.792154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = []

    # Create StringIO later used to parse ini
    config = StringIO()

    config.write(u'[section1]\n')
    config.write(u'user=value1\n')
    config.write(u'password=value2\n')
    config.write(u'\n')
    config.write(u'[section2]\n')
    config.write(u'user=value3\n')
    config.write(u'password=value4\n')
    config.seek(0, os.SEEK_SET)

    # Initialize LookupModule
    lookup_module = LookupModule()
    lookup_module.cp = configparser.SafeConfigParser()
    lookup_module.cp.readfp(config)

    # Test first item
    key = 'user'


# Generated at 2022-06-13 13:56:37.371331
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Setup the correct value for the key to find in the section
    section = 'section1'
    key = 'key1'
    value = 'value1'
    dflt = 'default'
    # Setup the text file to test
    config_file = StringIO()
    config_file.write("[section1]\nkey1=value1\nkey2=value2\n")
    config_file.seek(0, os.SEEK_SET)
    # Setup the LookupModule object
    module = LookupModule()
    module.cp = configparser.ConfigParser()
    module.cp.readfp(config_file)
    # Test the get_value method
    assert module.get_value(key, section, dflt, False) == value
    assert module.get_value(key, section, dflt, True)

# Generated at 2022-06-13 13:56:44.233706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with invalid file
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup_plugin = LookupModule()
        lookup_plugin.run([], {}, file="invalid_file.ini")
    assert 'The path "/home/runner/work/ansible/ansible/test/units/modules/files/invalid_file.ini" does not exist' in str(excinfo.value)
    assert 'was not found in the lookup path' in str(excinfo.value)

    # Test with invalid section
    with pytest.raises(AnsibleLookupError) as excinfo:
        lookup_plugin = LookupModule()
        lookup_plugin.run([], {}, file="test_ini.ini", section="invalid_section")

# Generated at 2022-06-13 13:56:53.939171
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create a Properties class
    class Properties(configparser.ConfigParser):
        def __init__(self, allow_no_value=False):
            configparser.ConfigParser.__init__(self, allow_no_value=allow_no_value)
        def set_property(self, property, value):
            return self.set('java_properties', property, value)
        def get_property(self, property):
            return self.get('java_properties', property)

    # Create a LookupModule class
    class LookupModule_test(LookupModule):
        def get_value(self, key, section, dflt, is_regexp):
            return super(LookupModule_test, self).get_value(key, section, dflt, is_regexp)

    # Init classes
    properties = Properties()
   

# Generated at 2022-06-13 13:57:02.942284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    terms = ['user', 'password']
    args = {'file': 'users.ini', 'section': 'global'}
    lu = LookupModule()

    # Write a file
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b'''
    [global]
    user=root
    password=secret
    ''')
    f.close()

    # When
    ret = lu.run(terms, **args)

    # Then
    assert ret == ['root', 'secret']

    # Remove the file
    os.remove(f.name)


# Generated at 2022-06-13 13:57:14.203524
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Initialization
    temp = StringIO()
    temp.write(u'[global]\n')
    temp.write(u'var1=test1\n')
    temp.write(u'var2=test2\n')
    temp.write(u'var3=test3\n')
    temp.write(u'[section1]\n')
    temp.write(u'var1=test4\n')
    temp.write(u'var4=test5\n')
    temp.write(u'var5=test6\n')
    temp.write(u'[section2]\n')
    temp.write(u'var3=test7\n')
    temp.write(u'var5=test8\n')
    temp.write(u'var8=test9\n')

# Generated at 2022-06-13 13:57:26.740745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Example:
    [section1]
    var1 = value1
    var2 = value2
    var3 = value3
    var4 = value4
    var5 = value5

    [section2]
    var6 = value6
    var7 = value7

    [section3]
    var8 = value8
    """

    import pytest
    from ansible.plugins.lookup.ini import LookupModule

    fh = open('test.ini', 'w')
    fh.write("""
[section1]
var1 = value1
var2 = value2
var3 = value3
var4 = value4
var5 = value5

[section2]
var6 = value6
var7 = value7

[section3]
var8 = value8
""")

# Generated at 2022-06-13 13:57:38.709369
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    class MockConfigParser:

        def __init__(self, allow_no_value):
            self.allow_no_value = allow_no_value
            self.config = {'section1': {'key1': 'value1', 'key2': 'value2'}}

        def items(self, section):
            return self.config[section].items()

        def get(self, section, key):
            return self.config[section].get(key)

    instance = LookupModule()
    cp = MockConfigParser(allow_no_value=True)
    instance.cp = cp

    # Test getter with no regexp
    assert instance.get_value('key1', 'section1', None, False) == 'value1'

# Generated at 2022-06-13 13:58:02.278844
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """
    Unit test for method run of class LookupModule
    """
    list_terms = ['host', 'host:host=host1', 'host:host=host1 host=host2', '']

    list_terms_results = [[], ['host1'], ['host1', 'host2'], []]

    class TestLookupModule(LookupModule):

        def get_value(self, key, section, dflt, is_regexp):
            if is_regexp:
                return [v for k, v in self.cp.items(section) if re.match(key, k)]
            try:
                return self.cp.get(section, key)
            except configparser.NoOptionError:
                return dflt

    for term in range(len(list_terms)):

        cp = configparser.ConfigParser

# Generated at 2022-06-13 13:58:10.245701
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l_module = LookupModule()
    params = {
        'type':'ini',
        'file':'users.ini',
        're':False,
        'encoding':'utf-8',
        'default':'',
        'case_sensitive':False,
    }
    ret = l_module.run(["user"], params=params)
    assert ret == ['ansible'], "The lookupmodule return a wrong value."

# Generated at 2022-06-13 13:58:21.267542
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.parsing.vault import get_vault_secret
    from ansible.plugins.lookup.ini import LookupModule
    from io import StringIO

    # Check one value
    config = StringIO(u'[global]\nuser=admin')
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()
    cp.readfp(config)
    module = LookupModule()
    module.cp = cp

    assert module.get_value('user', 'global', None, False) == 'admin'

    # Check multiple values
    config = StringIO(u'[global]\nuser1=admin\nuser2=admin')
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()

# Generated at 2022-06-13 13:58:30.451184
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from io import StringIO

    cp = configparser.ConfigParser()
    f = StringIO("""
[section1]
key1=foo
""")
    cp.readfp(f)

    lookup = LookupModule()
    lookup.cp = cp

    assert 'foo' == lookup.get_value('key1', 'section1', '', False)
    assert '' == lookup.get_value('key2', 'section1', '', False)
    assert 'foo' == lookup.get_value('key1', 'section1', '', True)

# Generated at 2022-06-13 13:58:42.737452
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # testing the INI file case
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader
    import os
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='/dev/null')
    variable_manager.set_inventory(inventory)
    fake_play = Play().load({}, variable_manager=variable_manager, loader=loader)

    # Test with different types
    # Test with user properties
    _lookup_plugin = lookup_loader.get('ini')

# Generated at 2022-06-13 13:58:50.775729
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.module_utils.six.moves import configparser
    key = "user"
    section = "mysqld"
    dflt = None
    is_regexp = False
    cp = configparser.ConfigParser()
    cp.read('../test.ini')
    result = LookupModule.get_value(cp,key,section,dflt,is_regexp)
    assert result == "root"

# Generated at 2022-06-13 13:58:59.821043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # (1) test case where key is not in the ini file
    # case where key is not in ini file
    module = LookupModule()
    terms = [ 'user', 'user2' ]
    variables = {}
    kwargs = { 'allow_none': True }
    ret = module.run(terms, variables, **kwargs)
    assert ret == ['', ''], "method run of class LookupModule return %s instead of ['', '']" % ret
    
    # (2) test case where key is in the ini file with good values
    terms = ['user', 'user2' ]
    with open('./ansible/test/units/plugins/lookup/fixtures/test_LookupModule_run.ini', 'r') as f:
        content = f.read()
    lPath = LookupBase

# Generated at 2022-06-13 13:59:05.828088
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ret = lookup.run([
        r"user=ubuntu file=test.ini section=default",
        r"section=default file=test.ini user=ubuntu",
        r"file=test.ini section=default user=ubuntu"
    ], variables=None, **{})[0]
    assert ret == "ubuntu"

# Generated at 2022-06-13 13:59:12.839055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={'ansible_python_interpreter': '/usr/bin/python3'})
    result = lookup_module.run([], variables={'ansible_python_interpreter': '/usr/bin/python3'})
    assert result == []


# Generated at 2022-06-13 13:59:18.890926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    module_path = os.path.dirname(os.path.realpath(__file__))
    test_values_file = os.path.join(module_path, 'lookup_plugin_test_values.ini')
    with open(test_values_file) as f:
        content = f.read()

    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[integration]\n')
    config.write(content)
    config.seek(0, os.SEEK_SET)

# Generated at 2022-06-13 13:59:50.597630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('section')
    l.cp.set('section', 'key', 'value')
    assert l.run(['key'], {}, section='section', file='') == ['value']
    assert l.run(['key=value'], {}, section='section', file='') == ['value']
    assert l.run(['key', '=', 'value'], {}, section='section', file='') == ['value']
    try:
        l.run(['key', 'key=value'], {}, section='section', file='')
        assert False
    except AnsibleOptionsError:
        assert True

# Generated at 2022-06-13 13:59:56.725724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import Mock, patch
    from ansible.module_utils._text import to_bytes
    from tempfile import NamedTemporaryFile

    # retrieve value
    f = NamedTemporaryFile()
    with f as temp_ini_file:
        temp_ini_file.write(to_bytes('[global]\nkey1=value1'))
        temp_ini_file.seek(0)

        lookup_module = LookupModule()
        lookup_module.cp = configparser.ConfigParser()
        lookup_module.cp.readfp(temp_ini_file)

        value = lookup_module.get_value('key1', 'global', '', False)
        assert value == 'value1'

    # retrieve value for key without value

# Generated at 2022-06-13 14:00:06.634595
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    value = "test"
    dflt = "test_default"
    section_name = "test_section"
    file_name = "test.ini"
    error_msg = "Error"
    key = "test_key"

    test_data = """
[{section_name}]
{key}={value}""".format(section_name=section_name, key=key, value=value)

    lookup_obj = LookupModule()

    # Test for method get_value
    with open("test_data.txt", "w") as fd:
        fd.write(test_data)
    lookup_obj.cp = configparser.ConfigParser()
    lookup_obj.cp.read("test_data.txt")

# Generated at 2022-06-13 14:00:10.988442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['user', 'password']
    vars = {'file': 'users.ini', 'section': 'integration'}
    assert lookup.run(terms, vars) == ['yperre', 'secret']



# Generated at 2022-06-13 14:00:11.771696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "TODO"

# Generated at 2022-06-13 14:00:19.757827
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    test_LookupModule_run: test init and get_value method of class LookupModule
    """

    # Test with properties file
    properties = "key=value"
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.optionxform = str
    assert not lm.cp.readfp(properties)

    # Test with ini file
    ini = """[section]
key=value"""
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.optionxform = str
    assert not lm.cp.readfp(ini)



# Generated at 2022-06-13 14:00:34.699260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test1: One key, one value
    test1 = LookupModule()
    test1.cp = configparser.ConfigParser({'section': {'user': 'ansible'}})
    test1.cp.readfp(StringIO('[section]\nuser=ansible'))
    assert test1.get_value('user', 'section', "", False) == 'ansible'

    # Test2: One key, one value, case sensitive
    test2 = LookupModule()
    test2.cp = configparser.ConfigParser({'section': {'User': 'ansible'}})
    test2.cp.readfp(StringIO('[section]\nUser=ansible'))
    test2.cp.optionxform = to_native
    assert test2.get_value('user', 'section', "", False)

# Generated at 2022-06-13 14:00:42.399732
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class LookupModuleMock(LookupModule):
        def __init__(self):
            super(LookupModuleMock, self).__init__()
            self.cp = configparser.ConfigParser()
            self.cp.add_section('section')
            self.cp.set('section', 'key1', 'value1')
            self.cp.set('section', 'key2', 'value2')

    l = LookupModuleMock()
    assert l.get_value('key1', 'section', 'default', False) == 'value1'
    assert l.get_value('key2', 'section', 'default', False) == 'value2'
    assert l.get_value('key3', 'section', 'default', False) == 'default'

# Generated at 2022-06-13 14:00:53.011319
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Create an INI file
    ini_stream = StringIO(u'[section1]\nkey1=value1\nkey2=value2\n')
    ini_stream.seek(0, os.SEEK_SET)
    # Create a dummy file
    props_stream = StringIO(u'user.name=foo')
    props_stream.seek(0, os.SEEK_SET)

    # Load an INI file
    lookup.cp.readfp(ini_stream)
    # Load a property file
    lookup.cp.readfp(props_stream)

    # Retrieve the value of key key1 in section section1
    assert lookup.get_value('key1', 'section1', '', False) == 'value1'
    # Retrieve all the keys in section

# Generated at 2022-06-13 14:01:05.003837
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.add_section('test')
    l.cp.set('test', 'key1', 'value1a')
    l.cp.set('test', 'key2', 'value2a')
    l.cp.set('test', 'key3', 'value3a')
    l.cp.set('test', 'key4', 'value4a')
    l.cp.set('test', 'key5', 'value5a')

    # Test a regexp matching several keys in a given section
    r = l.get_value(r'^key[345]$', 'test', 'default', True)
    assert len(r) == 3

# Generated at 2022-06-13 14:02:15.381136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.errors
    lookup = LookupModule()

    # if the file does not exist, should raise an exception
    with pytest.raises(ansible.errors.AnsibleFileNotFound):
        lookup.run([], dict(file='file_does_not_exist', section='whatever'))

    # if the section does not exist, should return an empty list
    result = lookup.run([], dict(file='files/does_not_exist.ini', section='whatever'))
    assert result == []

    # file exists, section exists, key exists
    result = lookup.run([], dict(file='files/ansible.ini', section='defaults'))
    assert result == ['~/.ansible']

    # file exists, section exists, key does not exist, default is set

# Generated at 2022-06-13 14:02:24.268490
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_bytes, to_text

    lookup = LookupModule()
    lookup.set_options({'section': 'section1', 'file': 'test.ini'})
    terms = ['regexp', 'regexp1']
    results = lookup.run(terms)
    assert results[0] == 'value2'
    assert results[1] == 'value1'

    lookup.set_options({'section': 'section1'})
    terms = ['bu', 'baza']
    results = lookup.run(terms)