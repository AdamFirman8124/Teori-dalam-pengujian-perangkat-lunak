

# Generated at 2022-06-13 13:52:38.235812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves.configparser import ConfigParser
    from ansible.module_utils.six import StringIO
    test_lookup_module = LookupModule()
    test_lookup_module.cp = ConfigParser()

# Generated at 2022-06-13 13:52:47.252960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This is not a full list of test cases; it's just some basic ones to keep us honest.
    # New tests should be added when bugs are discovered, but note that the LookupModule API
    # is not considered stable and is subject to change at any time.

    # Exceptions can be raised due to encoding errors
    if os.environ.get('EXAMPLES_INI_FILE'):
        os.environ['ANSIBLE_INI_PATH'] = os.environ['EXAMPLES_INI_FILE']

    lm = LookupModule()
    with pytest.raises(AnsibleLookupError):
        lm.run(['foo'], variables={}, file='/path/does/not/exist.ini', section='bad', default='', encoding='ascii')

# Generated at 2022-06-13 13:53:00.067406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import errors
    lookup = LookupModule()

    class TestModule(object):
        """TestModule dummy class"""
        def __init__(self, *args, **kwargs):
            self.params = args

        def fail_json(self, *args, **kwargs):
            """fail_json dummy"""
            pass

    # Empty term
    result = lookup.run([''], TestModule())
    assert result == [''], result

    # Bad term
    with pytest.raises(AnsibleLookupError):
        lookup.run(['a=b'], TestModule())

    # Bad term with '=' in key and space in value
    with pytest.raises(AnsibleLookupError):
        lookup.run(['a=b c'], TestModule())

    # Bad term with '=' in key

# Generated at 2022-06-13 13:53:11.655774
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a dummy config file
    config = StringIO()
    config.write(u'[CA]\n')
    config.write(u'username=qxb7a\n')
    config.write(u'password=qxb7a\n')
    config.write(u'[dev]\n')
    config.write(u'username=qxb7a\n')
    config.write(u'password=qxb7a\n')
    config.write(u'[crm]\n')
    config.write(u'username=qxb7a\n')
    config.write(u'password=qxb7a\n')
    config.seek(0, os.SEEK_SET)

    # Create a Lookup module
    mod = LookupModule()

    # Should return all the keys


# Generated at 2022-06-13 13:53:20.295703
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of LookupModule
    l = LookupModule()

    # Check that no terms raises an error
    terms = []
    with pytest.raises(AnsibleOptionsError):
        l.run(terms)

    # Create a file to use for test
    # This example file contains a list of [sections] which includes global,
    # integration, production. global and integration have different keys
    # and values
    tmpdir = tempfile.mkdtemp()
    test_file_path = os.path.join(tmpdir, "ansible.ini")
    test_file = open(test_file_path, "w")
    test_file.write("[global]\n")
    test_file.write("user=globaluser\n")
    test_file.write("password=globalpassword\n")
    test

# Generated at 2022-06-13 13:53:25.886007
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.optionxform = to_native
    lookup_module.cp.read_dict({
        'section1': {
            '_': 'comment on section1',
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        },
        'section2': {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
    })
    # Get all values of section1
    values1 = lookup_module.get_value(r'.*', 'section1', 'dflt', True)
    assert values1 == ['value1', 'value2', 'value3']



# Generated at 2022-06-13 13:53:33.078161
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test the regexp case
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(StringIO("""[section]
key1=value1
key2=value2
"""))
    assert lookup.run([
        'key2',
        'key=key1',
        'section=section',
        're=True'
    ]) == [
        'value1',
        'value1',
        'value2',
        'value2'
    ]



# Generated at 2022-06-13 13:53:43.061519
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    config_parser = configparser.ConfigParser()
    config_parser.optionxform = lambda option: option
    config_parser.add_section('section_test')
    config_parser.set('section_test', 'key1', 'value1')
    config_parser.set('section_test', 'key2', 'value2')
    config_parser.set('section_test', 'key3', 'value3')
    config_parser.set('section_test', 'key4', 'value4')
    lookup_module.cp = config_parser
    assert lookup_module.get_value('key1', 'section_test', 'default_value', False) == 'value1'

# Generated at 2022-06-13 13:53:51.020303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    config = StringIO()
    config.write(u"""[section1]
id=1
value=True

[section2]
id=2
value=True

[section1]
id=3
value=False
""")
    config.seek(0,os.SEEK_SET)
    parser = configparser.ConfigParser()
    parser.readfp(config)

    # Test regular expression of key
    value = LookupModule().get_value('.*', section='section1', dflt=False, is_regexp=True)
    assert value == ['1', 'True', '3', 'False']

    # Test regular expression with default value
    value = LookupModule().get_value('.*', section='section3', dflt='Nothing', is_regexp=True)
    assert value == 'Nothing'

# Generated at 2022-06-13 13:54:03.575814
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    test_file = StringIO()
    test_file.write(u'[test_section]\n')
    test_file.write(u'key1=value1\n')
    test_file.write(u'key2=value2\n')
    test_file.write(u'key3=value3\n')
    test_file.seek(0, os.SEEK_SET)

    test_case_1_cp = configparser.ConfigParser()
    test_case_1_cp.readfp(test_file)
    test_case_1_um = LookupModule('')
    test_case_1_um.cp = test_case_1_cp

    test_case_2_cp = configparser.ConfigParser()
    test_case_2_cp.readfp(test_file)


# Generated at 2022-06-13 13:54:25.306736
# Unit test for method get_value of class LookupModule

# Generated at 2022-06-13 13:54:36.117122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test properties
    assert lookup.run(["user.name=foo"], type="properties", file="file") == ["foo"]
    # Test INI
    assert lookup.run(["user"], file="file") == ["bar"]
    assert lookup.run(["user"], file="file", section="section") == ["bar"]
    assert lookup.run(["user"], default="default", file="file", section="section") == ["bar"]
    assert lookup.run(["user1"], default="default", file="file", section="section") == ["default"]
    # Test regexp
    assert lookup.run(["user"], file="file", section="section", re="True") == ["bar"]
    assert lookup.run(["user"], file="file", section="section", re="False") == ["bar"]
    assert lookup

# Generated at 2022-06-13 13:54:46.300605
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    l = LookupModule()
    l.cp = configparser.ConfigParser()
    l.cp.read_string(u'[section1]\nkey1=value1\nkey2=value2\n[section2]\nkey3=value3')
    assert l.get_value("key1", "section1", None, False) == "value1"
    assert l.get_value("key2", "section1", None, False) == "value2"
    assert l.get_value("key3", "section2", None, False) == "value3"
    assert l.get_value("key3", "section3", None, False) is None

    assert l.get_value(".*", "section1", None, True) == ["value1", "value2"]

# Generated at 2022-06-13 13:54:59.361999
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [u"user", u"user=test user", u"user=test user=test2"]
    params = [
        dict(file="ansible.ini", section="global", type="ini", re=True, encoding="utf-8", case_sensitive=False),
        dict(file="ansible.properties", section="global", type="properties", re=True, encoding="utf-8", case_sensitive=False),
        dict(file="ansible.properties", section="global", type="properties", re=True, encoding="utf-8", case_sensitive=False),
    ]

    contents = [
        '''
        [global]
        user=test
        ''',
        '''
        user.name=test
        ''',
        '''
        user.name=test
        ''',
    ]
    # Test with

# Generated at 2022-06-13 13:55:07.361671
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    _config_string = u'[global]\nuser = yannig\n'
    config = StringIO()
    config.write(_config_string)
    config.seek(0, os.SEEK_SET)
    _cp = configparser.ConfigParser()
    _cp.readfp(config)

    obj = LookupModule()
    obj.cp = _cp
    assert obj.get_value('user', 'global', '', False) == "yannig"
    assert obj.get_value('user', 'production', '', False) is None
    assert obj.get_value('user', 'production', '', True) == []
    assert obj.get_value('.*', 'global', '', True) == ['yannig']

    # Properties file


# Generated at 2022-06-13 13:55:18.340946
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import MutableSequence

    # Prepare temporary directory
    tmpdir = tempfile.mkdtemp()
    # Prepare temporary file
    path = os.path.join(tmpdir, 'config')
    f = open(path, 'w')
    f.write(to_text(u'[section1]\n'
                    u'value=foovalue\n'
                    u'value2=barvalue\n'
                    u'[section2]\n'
                    u'value=foovalue\n'
                    u'[section1:section2]\n'
                    u'value=foovalue2\n'
                    ))
    f.close()



# Generated at 2022-06-13 13:55:28.869633
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test using default options
    lookup = LookupModule()
    lookup.cp = configparser.SafeConfigParser()
    lookup.set_options(var_options={}, direct={})
    paramvals = {'file': 'ansible.ini', 'section': 'global', 'type': 'ini', 'encoding': 'utf-8', 'default': '', 'case_sensitive': False, 'allow_no_value': False}

    # Create StringIO later used to parse ini
    config = StringIO()

    # Open file using encoding
    contents = 'user = admin\n'
    contents = to_text(contents, errors='surrogate_or_strict', encoding=paramvals['encoding'])
    config.write(contents)
    config.seek(0, os.SEEK_SET)

    lookup.cp.read

# Generated at 2022-06-13 13:55:42.518266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a test environment
    mkdtemp = tempfile.mkdtemp()

    # create a simple ini
    test_file = os.path.join(mkdtemp, "test.ini")
    with open(test_file, "w") as fh:
        fh.write("""[section1]
user1=user1@example.com
user2=user2@example.com
user3=user3@example.com

[section2]
user4=user4@example.com
user5=user5@example.com
user6=user6@example.com
""")
    # create an instance of LookupModule with all default parameters
    lookup_m = LookupModule()

    # read all values in 'section1'
    terms = ['*']

# Generated at 2022-06-13 13:55:51.387053
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set variables
    plugin = LookupModule()

    path = plugin.find_file_in_search_path(None, 'files', 'ansible.ini')

    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(u'[java_properties]\n')
    config.write(u'user.name = jdoe')
    config.seek(0, os.SEEK_SET)

    cp = configparser.ConfigParser()
    cp.readfp(config)

    # Return value in case of success
    assert plugin.get_value('user.name', 'java_properties', '', False) == 'jdoe'

    # Return value in case of regex

# Generated at 2022-06-13 13:56:03.286474
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test params
    lookup_params = {
        'file': 'test/ansible_test.ini',
        'type': 'ini',
        're': False,
        'case_sensitive': False,
        'allow_no_value': False,
    }

    # Unit test call
    lookup_class = LookupModule()
    lookup_class.set_options({'file': 'test/ansible_test.ini'})

# Generated at 2022-06-13 13:56:38.249404
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with no regexp key
    lm = LookupModule()
    terms = ["user", "password"]
    variables = {'file': 'ansible.ini'}
    ret = lm.run(terms, variables)
    assert ret == ['yannig', '123456'], ret
    # Test with regexp key
    lm = LookupModule()
    terms = ["user.*"]
    variables = {'file': 'ansible.ini'}
    ret = lm.run(terms, variables)
    assert sorted(ret) == sorted(['yannig', '123456', 'user.name=yannig', 'user.password=123456']), ret
    # Test with no regexp key but with invalid section
    lm = LookupModule()
    terms = ["user"]

# Generated at 2022-06-13 13:56:44.935902
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    cp = configparser.ConfigParser()
    filepath = "/etc/ansible/hosts"
    cp.readfp(StringIO("[group1]\ngroup1_key=group1_value\nkey=value"))
    assert cp.get("group1", "group1_key") == "group1_value"
    assert cp.get("group1", "key") == "value"
    assert cp.get("group1", "test_key", fallback="test_value") == "test_value"
    assert cp.get("group1", "test_key") == ""

    lm = LookupModule()
    lm.cp = cp
    lm.set_options(var_options=None, direct=False)
    lm.get_options()

# Generated at 2022-06-13 13:56:53.247321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2')
    lookup.cp.set('section1', 'key3', 'value3')
    lookup.cp.set('section1', 'key4', 'value4')
    lookup.cp.set('section1', 'key5', 'value5')
    lookup.cp.set('section1', 'key6', 'value6')
    lookup.cp.add_section('section2')
    lookup.cp.set('section2', 'key1', 'value1')
    lookup.cp.set('section2', 'key2', 'value2')
   

# Generated at 2022-06-13 13:57:03.869154
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    test_lookup = LookupModule()

    # [Setup] Create mock ConfigParser (test_cp)
    test_cp = configparser.ConfigParser(allow_no_value=False)

    # Create mock INI file
    config = StringIO()
    config.write(u'[global]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.seek(0, os.SEEK_SET)

    # Parse the mock INI file
    test_cp.readfp(config)
    test_lookup.cp = test_cp

    # [Test]
    # (1) Test normal case
    # (1-1) Get a string
    key = 'key1'
    section = 'global'
    dflt

# Generated at 2022-06-13 13:57:14.841344
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()

    # Build an INI file
    config = StringIO()
    config.write(u'[section1]\n')
    config.write(u'default=False\n')
    config.write(u'user.name=John Doe\n')
    config.write(u'user.email=john@doe.com\n')
    config.write(u'user.phone=0123456789\n')
    config.write(u'user.phone_home=9876543210\n')
    config.write(u'user2.name=Jane Doe\n')
    config.write(u'user2.email=jane@doe.com\n')

# Generated at 2022-06-13 13:57:27.572723
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    test_class = LookupModule()
    test_class.cp = configparser.ConfigParser()
    test_class.cp.readfp(StringIO(u'[section1]\nkey1=value1\nkey2=value2\nkey3=value3\n'))
    # key exists in section
    assert test_class.get_value('key1', 'section1', '', False) == 'value1'
    # key does not exist in section
    assert test_class.get_value('key4', 'section1', 'defaultValue', False) == 'defaultValue'
    # key exists in section and regexp match
    assert test_class.get_value('^key[12]', 'section1', '', True) == ['value1', 'value2']
    # key exists in section and regexp does not match


# Generated at 2022-06-13 13:57:34.922888
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class Options:
        file = "ansible.ini"
        section = "global"
        default = "42"
        re = False
        encoding = "utf-8"
        allow_no_value = False
        case_sensitive = False

    module = LookupModule()
    module.cp = configparser.ConfigParser(allow_no_value=False)
    module.set_options(direct=Options.__dict__)
    contents = "[global]\nuser=ansible\ncount=42\n"
    config = StringIO(contents)
    module.cp.readfp(config)
    assert module.get_value("user", "global", Options.default, Options.re) == "ansible"
    assert module.get_value("user", "global", Options.default, True) == ["ansible"]

# Generated at 2022-06-13 13:57:43.278285
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Test with a valid key, section, default and return value
    lm = LookupModule()
    cp = configparser.ConfigParser()
    cp.optionxform = to_native
    cp.add_section("integration")
    cp.set("integration", "user", "yperre")
    lm.cp = cp
    assert lm.get_value("user", "integration", "default", False) == 'yperre'

    # Test with a default value
    assert lm.get_value("foo", "integration", "default", False) == 'default'

    # Test with a regexp key
    assert lm.get_value("user", "integration", "default", True) == ['user']

# Generated at 2022-06-13 13:57:55.485873
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
  section = 'section'
  key = 'key'
  content = "[section]\nkey1 = value1\nkey2 = value2"

  cp = configparser.ConfigParser()
  config = StringIO()
  try:
    config.write(u'[%s]\n' % section)
    config.write(content)
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)
  except configparser.DuplicateOptionError as doe:
    raise AnsibleLookupError("Duplicate option in '{file}': {error}".format(file='', error=to_native(doe)))

  assert LookupModule.get_value(None, key, section, None, False) == 'value1'

# Generated at 2022-06-13 13:58:00.334068
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    return_value = ['user1', 'user2', 'user3']
    module = LookupModule()
    terms = ["user"]
    module.run(terms)
    return_value = module.run(terms)
    assert return_value == ["user1", "user2", "user3"]
        

# Generated at 2022-06-13 13:58:59.248182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    terms = ["user=yannig"]
    expected = "yannig"
    variables = {'ansible_module_generated': {'lookup_file': "ansible.ini", 'lookup_plugin': 'ini', 'lookup_terms': ['user=yannig']}}
    options = {
        'file': "ansible.ini",
        'section': "global",
        're': False,
        'encoding': "utf-8",
        'default': "",
        'type': "ini",
        'case_sensitive': False,
    }

    cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[global]\nuser = yannig')
    config.seek(0, os.SEEK_SET)
    cp

# Generated at 2022-06-13 13:59:09.974925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # GIVEN
    # content of the ini file
    ini_c = "[section]\nfirst=val1\nsecond=val2\nthird=val3\n"
    # instance of LookupModule and configparser.ConfigParser
    lm = LookupModule()
    cp = configparser.ConfigParser()
    # create a file
    f = open('/tmp/test.ini', 'w')
    f.write(ini_c)
    f.close()
    # mock open()
    def mockopen(name, mode, encoding=None):
        if name == '/tmp/test.ini':
            return open('/tmp/test.ini', 'r')
    # mock find_file_in_search_path()

# Generated at 2022-06-13 13:59:21.166403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Imports
    import ansible.plugins.lookup
    import ansible.module_utils
    # Instantiate lookup module
    lookup_module = ansible.plugins.lookup.LookupModule()
    # Instantiate variable module
    variable_module = ansible.module_utils.basic.AnsibleModule()
    # Create terms to lookup
    terms = ['user', 'password']
    # Create variables to set
    variables = dict(file='ansible.ini', section='global')
    # Run method run
    result = lookup_module.run(terms, variables)
    # Assertions
    assert result[:2] == ['ansible', 'ansible'], "Failed to retrieve value for key %s, got %s" % ("user", result[0])

# Generated at 2022-06-13 13:59:30.916981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    import os

    print("Test LookupModule for method run")

    base = 'lookup/ini/'
    term = 'user'

    print("Test LookupModule with no value in ini file")
    file_path = base + "empty.ini"
    lookupModule = LookupModule()
    result = lookupModule.run((term,), {}, file=file_path)
    assert result[0] == ''

    print("Test LookupModule with single value in ini file")
    file_path = base + "singleValue.ini"
    lookupModule = LookupModule()
    result = lookupModule.run((term,), {}, file=file_path)
    assert result[0] == 'johndoe'


# Generated at 2022-06-13 13:59:41.666266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Tests run method of class LookUpModule

    Test cases : should return a list of found values for each term
                 if no value matching the key is found in the ini or properties file
                 should return a empty list.
    '''
    # Create lookup object with a value = "yannig" for key "user" in section "integration" of the ini file users.ini
    lookup_obj = LookupModule()
    lookup_obj.cp = configparser.ConfigParser()
    lookup_obj.cp.read(['users.ini'])
    lookup_obj.cp.set('integration', 'user', 'yannig')

# Generated at 2022-06-13 13:59:44.031565
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This test must be run as part of the test_lookup_ini tests
    return None



# Generated at 2022-06-13 13:59:51.240070
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # initialize plugin
    l = LookupModule()

    # Initialize parameters
    paramvals = {
        'allow_no_value': False,
        'case_sensitive': False,
        'file': '/ansible/tests/test.ini',
        're': False,
        'section': 'global',
        'type': 'ini',
        'encoding': 'utf-8',
        'default': '',
    }

    # Attach parameters to l
    l.set_options(paramvals=paramvals)

    # Enter dans la methode run()
    l.run(terms=['test_key1'], variables=None)

    # Check content of return
    assert l.run(terms=['test_key1'], variables=None) == ['value1']

    # Check content of return for multiple key lookup


# Generated at 2022-06-13 14:00:02.665381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup = LookupModule()
    # Check if sections and keys exist in config file
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms=[".*"], variables="", section=["section1"], file="files/test.ini", re=False)
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms=[".*"], variables="", section=["section3"], file="files/test.ini", re=False)
    with pytest.raises(AnsibleLookupError):
        lookup.run(terms=[".*"], variables="", section=["section4"], file="files/test.ini", re=False)
    # Check if section exists in config file
    with pytest.raises(AnsibleLookupError):
        lookup.run

# Generated at 2022-06-13 14:00:10.176999
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up test
    lookupplugin = LookupModule()
    # Create variables for lookup
    variables = {}
    # Create dictionnary for test
    test_dic = {
        'type': 'ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8'
    }
    # Create terms for test
    terms = ['user', 'password']
    # Run test
    result = lookupplugin.run(terms, variables, **test_dic)
    # Asserts
    assert result[0] == 'ansible'
    assert result[1] == 'ansible'
    # End of test


# Generated at 2022-06-13 14:00:20.850243
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Load a test INI file
    dummy_data = StringIO()
    dummy_data.write(u"[section1]\n")
    dummy_data.write(u"user=yannig\n")
    dummy_data.write(u"pass=s3cr3t\n")
    dummy_data.write(u"\n")
    dummy_data.write(u"[section2]\n")
    dummy_data.write(u"user=foo\n")
    dummy_data.write(u"pass=foo\n")
    dummy_data.seek(0, os.SEEK_SET)

    # Create a new instance of LookupModule class
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(dummy_data)

    # Use

# Generated at 2022-06-13 14:01:17.693258
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()

    # Create StringIO later used to parse ini
    config = StringIO.StringIO()
    config.write('[section1]\n')
    config.write('key1=value1\n')
    config.write('key2=value2\n')
    config.seek(0, os.SEEK_SET)

    cp.readfp(config)
    lookup = LookupModule()
    assert lookup.get_value('key1', 'section1', None, False) == 'value1'
    assert lookup.get_value('key1', 'section1', 'default_value', False) == 'value1'
    assert lookup.get_value('key3', 'section1', 'default_value', False) == 'default_value'

# Generated at 2022-06-13 14:01:22.020416
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = "jdoe"
    # path to file located in 'files' (see ansible.cfg)
    default_file = "../../files/ansible.ini"

    lookup_module = LookupModule(None, None, None)

    # Should return 'john' if the term "jdoe" is found in the 'ini' file
    assert lookup_module.run([terms], {}, file=default_file)[0] == "john"

    # Should return 'john' if the term "jdoe" is found in the 'ini' file with
    # the default value of None (and not the empty string)
    assert lookup_module.run([terms], {}, file=default_file, default=None)[0] == "john"

    # Should return the empty string if the term "johndoe" is not found in the '

# Generated at 2022-06-13 14:01:32.149134
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Generate a test ini file
    config = StringIO()
    config.write(u'''
[global]
db_user=gromit
db_pass=keeeek

[integration]
user=penguin

[production]
user=wallace
''')

    config.seek(0, os.SEEK_SET)

    # Create a LookupModule
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.cp.readfp(config)

    # Test the retrieval of a value without any options
    # should retrieve 'gromit' and 'keeeek'
    terms = [ 'db_user', 'db_pass' ]
    result = lookup_module.run(terms, dict())

# Generated at 2022-06-13 14:01:40.499853
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os

    if sys.version_info.major < 3:
        import __builtin__ as builtins
    else:
        import builtins

    if not os.path.exists('/tmp/test_file.ini'):
        with open('/tmp/test_file.ini', 'w') as f:
            f.write(
"""
[section1]
key1=value1

[section2]
key2=value2

[section3]
key3=value3_1
key3=value3_2
key3=value3_3
"""
            )


# Generated at 2022-06-13 14:01:49.739183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()
    variables = {}
    # Check file ansible.ini
    # Section: global
    ret = obj.run(["bar=foo", "key1"], variables=variables)
    assert (ret == ['value10'])
    ret = obj.run(["bar=foo", "key1"], variables, type="properties")
    assert (ret == ["value1.0"])
    ret = obj.run(["bar=foo", "key2"], variables=variables)
    assert (ret == ['value2'])
    ret = obj.run(["bar=foo", "key2"], variables, type="properties")
    assert (ret == ["value2"])
    # Section: section1
    ret = obj.run(["bar=foo", "key1 section1"], variables=variables)

# Generated at 2022-06-13 14:01:53.129548
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import configparser
    module = LookupModule()
    assert isinstance(module, LookupBase)



# Generated at 2022-06-13 14:02:00.552748
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for a property file
    lu = LookupModule()
    params = {'type': 'properties', 'file': 'user.properties', 'default': '', 'encoding': 'utf-8', 'case_sensitive': False}
    terms = ['user.name']
    res = lu._run_terms(terms, params, inject={})
    assert res[0] == 'Yannig Perre'
    # Test for a ini file
    lu = LookupModule()
    params = {'type': 'ini', 'file': 'passwords.ini', 'default': '', 'encoding': 'utf-8', 'section': 'integration', 'case_sensitive': False}
    terms = ['pass']
    res = lu._run_terms(terms, params, inject={})

# Generated at 2022-06-13 14:02:05.922554
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.add_section('section1')
    lm.cp.set('section1', 'key1', 'value1')
    lm.cp.set('section1', 'key2', 'value2')
    lm.cp.set('section1', 'key3', 'value3')
    lm.cp.set('section1', 'key4', 'value4')
    lm.cp.set('section1', 'key5', 'value5')

    assert(lm.get_value('key1', 'section1', '', False) == 'value1')

# Generated at 2022-06-13 14:02:16.157953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test the method run of class LookupModule
    # This method test the method run of class LookupModule
    # It check several cases :
    #    -
    #    -
    #    -
    # Tested method is run and get_value of class LookupModule
    from ansible.plugins.lookup import LookupBase
    from ansible.errors import AnsibleLookupError

    lookup_mock = LookupModule()
    path = lookup_mock.find_file_in_search_path(None, 'files', 'ansible.ini')
    config = StringIO()
    with open(path) as f:
        for line in f:
            config.write(line)
    config.seek(0, os.SEEK_SET)
    lookup_mock.cp.readfp(config)

# Generated at 2022-06-13 14:02:25.030656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ini_content = u"""[section1]
key1=value1
key2=value2

[section2]
key3=value3
key4=value4
key5=value5

[section3]
key6=value6
"""
    test = LookupModule()
    test.cp = configparser.ConfigParser()
    test.cp.readfp(StringIO(ini_content))
    # test reading a single value
    assert test.run(["key1", "file=test.ini", "default=value1", "section=section1"]) == ["value1"]
    # test reading a single value with regex