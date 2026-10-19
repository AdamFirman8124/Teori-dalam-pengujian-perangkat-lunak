

# Generated at 2022-06-13 13:52:37.802779
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init object
    lookup = LookupModule()
    # set up options
    options = { 'type': 'ini' }
    # set up content of ini file
    ini_content = u'[global]\nuser=yannigperre\n'
    # set up content of java properties
    properties_content = u'user=yannigperre'
    # open StringIO
    config = StringIO()
    config.write(ini_content)
    config.seek(0, os.SEEK_SET)
    # retrieve ini value
    params = _parse_params('user', options)
    # test error
    # init good

# Generated at 2022-06-13 13:52:46.941286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    test_file_folder = os.path.dirname(os.path.realpath(__file__))
    test_file_path   = os.path.join(test_file_folder, 'test_file.ini')
    test_file_path2  = os.path.join(test_file_folder, 'test_file_properties.properties')

    # test the enum of a simple ini file
    test_file = "[section]\nkey1=value1\nkey2=value2\nkey3=value3\nkey3=value3b\nkey4=\nkey5"

# Generated at 2022-06-13 13:52:59.644367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.module_utils.six.moves import configparser

    # create a fake file
    test_file = """
[global]
user=root

[integration]
user=ansible

[production]
user=root
"""
    config = StringIO()
    config.write(u'[java_properties]\n')
    config.write(u'user=ansible')
    config.seek(0, os.SEEK_SET)

    # test with a fake file
    lookup_plugin = LookupModule()
    lookup_plugin.cp = configparser.ConfigParser()
    lookup_plugin.cp.readfp(config)
    actual = lookup_plugin.get_value('user', 'java_properties', '', False)
    assert actual

# Generated at 2022-06-13 13:53:11.434125
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    path = os.path.dirname(os.path.realpath(__file__))
    property_file = os.path.join(path, "test_property_file.properties")
    ini_file = os.path.join(path, "test_ini_file.ini")
    lu = LookupModule()
    lu.cp = configparser.ConfigParser(allow_no_value=True)
    # Properties file
    lu.cp.readfp(open(property_file))
    assert lu.get_value('firstname', 'java_properties', '', False) == 'jondoe'
    assert lu.get_value('lastname', 'java_properties', '', False) == 'jdoe'
    assert lu.get_value('age', 'java_properties', '', False) == ''


# Generated at 2022-06-13 13:53:22.982743
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # default options
    default_options = {
        '_original_file': '/path/to/ansible/file',
        '_original_vars': {},
        '_load_name': 'foo.ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'type': 'ini',
    }

    # parsed options
    parsed_options = {
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
        'type': 'ini',
    }

    # test LookupModule class

# Generated at 2022-06-13 13:53:33.969509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # No option
    lookup_module = LookupModule()
    lookup_module.cp = configparser.ConfigParser()
    lookup_module.set_options(direct={'type': 'ini'})
    lookup_module.cp.readfp(StringIO(u'[section1]\nkey1=value1\nkey2=value2\n'))
    assert lookup_module.get_value('key1', 'section1', 'default', False) == 'value1'
    assert lookup_module.get_value('key1', 'section1', 'default', True) == 'value1'
    assert lookup_module.get_value('key.*', 'section1', 'default', True) == ['value1', 'value2']

# Generated at 2022-06-13 13:53:43.688893
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # For all tests, we need to be sure that "find_file_in_search_path" return the right argument
    # So we mock it
    LookupModule.find_file_in_search_path = lambda self, variables, dirs, file: file

    # For this first test, we mock _loader._get_file_contents to return what we want
    # based on the ini file given as argument

# Generated at 2022-06-13 13:53:50.800432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create LookupModule
    module = LookupModule()

    # Define parameters
    term = 'user'
    params = {
        'type': 'ini',
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'default': '',
    }

    # Define return
    return_value = 'yperre'

    # Retrieves value from ansible.ini
    assert module.run(term, **params)[0] == return_value
    # Retrieves default value
    assert module.run('bad_user', **params)[0] == params['default']



# Generated at 2022-06-13 13:53:52.029811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: write some tests for this class
    pass


# Generated at 2022-06-13 13:54:04.660610
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import os
    import re

    from ansible.errors import AnsibleLookupError, AnsibleOptionsError
    from ansible.module_utils.six.moves.configparser import ConfigParser

    from ansible.plugins.lookup.ini import LookupModule

    test_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', '..', 'test_data', 'lookup_plugins', 'ini', 'test.ini')
    test_ini_file = open(test_file_path)
    test_ini_config = ConfigParser()
    test_ini_config.readfp(test_ini_file)
    test_ini_file.close()
    lookup_module = LookupModule()
    lookup_module.cp = test_ini

# Generated at 2022-06-13 13:54:20.088962
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock object to replace configparser.ConfigParser.get
    class ConfigParserMock:
        def __init__(self, allow_no_value):
            self.allow_no_value = allow_no_value
        def get(self, section, key):
            config_dict = {
                'section3': {
                    'test_key_1': 'test_value_1',
                    'test_key_2': 'test_value_2',
                    'test_key_3': 'test_value_3',
                    'test_key_4': 'test_value_4',
                },
            }
            if self.allow_no_value:
                config_dict['section4'] = {
                    'test_key_5': None,
                }
            return config_dict[section][key]


# Generated at 2022-06-13 13:54:23.949265
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(['arg1', 'arg2'], {'file': 'test.ini', 'section': 'section1'}, type='ini') is None


# Generated at 2022-06-13 13:54:35.546331
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Initialization of a LookupModule instance
    lm = LookupModule()
    # Initialization of the configuration parser
    lm.cp = configparser.ConfigParser()

    # Tests for a section containing several keys and a regexp, both case-sensitive and insensitive
    lm.cp.read_dict({'SECTION': {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}})
    assert ['val1', 'val2', 'val3'] == lm.get_value('.*', 'SECTION', None, True)
    lm.cp = configparser.ConfigParser(strict=False)
    lm.cp.read_dict({'SECTION': {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}})


# Generated at 2022-06-13 13:54:46.300198
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lu = LookupModule()
    cp = configparser.ConfigParser()
    lu.cp = cp
    cp.add_section("NETWORK")
    cp.set("NETWORK", "eth0", "192.168.0.2")
    cp.set("NETWORK", "eth1", "192.168.1.2")
    cp.set("NETWORK", "eth2", "192.168.2.2")
    cp.add_section("eth0")
    cp.set("eth0", "IPV4", "192.168.0.2")
    cp.set("eth0", "IPV6", "2001:db8:10::2/64")
    cp.add_section("eth1")
    cp.set("eth1", "IPV4", "192.168.1.2")
   

# Generated at 2022-06-13 13:54:59.357153
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get the class
    lookup = LookupModule()

    # Create a test file
    f = open('test_file', 'w')

    # Write test content in file
    f.write('[section2]\n')
    f.write('key1=value1\n')
    f.write('key2=value2\n')
    f.write('[section1]\n')
    f.write('key1=value3\n')
    f.write('key2=value4\n')
    f.write('\n')
    f.write('[section3]\n')
    f.write('key1=value5\n')
    f.write('key2=value6\n')

    # Close test file
    f.close()

    # Run the tests

# Generated at 2022-06-13 13:55:07.360709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    config = StringIO()
    config.write(u'''[test]
        firstkey1 = 1st value
        firstkey2 = 2nd value
        firstkey3 = 3rd value
        secondkey1 = 4th value
        secondkey2 = 5th value
        secondkey3 = 6th value
        thirdkey1 = 7th value
        thirdkey2 = 8th value
        thirdkey3 = 9th value
    ''')
    config.seek(0, os.SEEK_SET)
    lookup_module.cp.readfp(config)
    path = os.path.dirname(__file__)
    paramvals = {'type': 'ini', 'file': 'test.ini'}
    msg = {}
    msg['section'] = 'test'
    msg['re']

# Generated at 2022-06-13 13:55:18.037754
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input data
    terms = ['user']
    term = 'user'
    dict = {'type': 'ini'}
    # Expected output
    expected = ['value_user']

    # Construct the LookupModule object
    lookup = LookupModule()

    # Create stringIO object
    config = StringIO()
    config.write(u'[section]\n')
    config.write(u'user=value_user\n')
    config.write(u'user2=value_user2\n')
    config.seek(0, os.SEEK_SET)

    lookup.cp = configparser.ConfigParser()
    lookup.cp.readfp(config)
    value = lookup.get_value(term, 'section', '', False)
    return value


# Generated at 2022-06-13 13:55:28.681747
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Test 1
    lookup = lookup_module.run(["user"], file="test1.ini", section="integration", type="ini")
    assert lookup == ['user_value']
    # Test2
    lookup = lookup_module.run(["user"], file="test1.ini", section="production", type="ini")
    assert lookup == ['user_value_2']
    # Test3
    lookup = lookup_module.run(["user.name"], file="test2.ini", section="integration", type="properties", re=True)
    assert lookup == ['user.name']
    # Test4
    lookup = lookup_module.run(["user"], file="test2.ini", section="integration", type="properties", re=True)
    assert lookup == ['user']

# Generated at 2022-06-13 13:55:41.022021
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Run the lookup against a sample ini file with the given search_paths
    def run_lookup(terms, search_paths, variables=None):
        return LookupModule().run(terms, variables, search_paths=search_paths, file='sample.ini')
    # Run the lookup against a sample ini file with the given search_paths
    def run_lookup_with_variables(terms, search_paths, variables):
        return LookupModule().run(terms, variables, search_paths=search_paths, file='sample.ini')

    # Create a search path from the given directory
    def set_search_path(directory):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        return [os.path.join(current_directory, directory)]



# Generated at 2022-06-13 13:55:49.846507
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # No option, key and section
    terms = "login=user1"
    variables = None
    lookup_values = lookup_module.run(terms, variables)
    assert len(lookup_values) == 1

    # No section
    terms = "login="
    variables = None
    kwargs = {'file': 'test.ini', 'default': 'user1'}
    lookup_values = lookup_module.run(terms, variables, **kwargs)
    assert len(lookup_values) == 1
    assert lookup_values[0] == 'user1'

    # With Direct option
    terms = "login="
    variables = None
    kwargs = {'file': 'test.ini', 'default': 'user1', 'section': 'section1'}
    lookup_

# Generated at 2022-06-13 13:56:14.470826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    def test_run_ok(terms, expected):
        assert lm.run(terms) == expected

    test_run_ok(['first_key', 'second_key', 'third_key'], ['first_val', 'second_val', 'third_val'])
    test_run_ok(['.*'], ['first_val', 'second_val', 'third_val', 'fourth_val'])
    test_run_ok(['.*', 'second_key'], ['first_val', 'second_val', 'third_val', 'fourth_val', 'second_val'])
    test_run_ok(['first_key', 'second_key', 'fourth_key'], ['first_val', 'second_val', 'third_val'])


# Generated at 2022-06-13 13:56:25.834908
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    class opts(object):
        encoding = 'utf-8'
        default = ''
    lookup.set_options(direct=opts())
    term = 'user1'
    terms = [term]
    paramvals = {'type': 'ini', 'file': 'test.ini', 'section': 'user.section', 're': False, 'encoding': 'utf-8', 'default': ''}
    lookup.cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[user.section]\n')
    config.write(u'user1=user1.name\n')
    config.seek(0, os.SEEK_SET)
    lookup.cp.readfp(config)
    assert lookup.cp.sections() == ['user.section']


# Generated at 2022-06-13 13:56:37.411010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import mock
    import shutil
    import tempfile


# Generated at 2022-06-13 13:56:50.243030
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import PY3
    import mock

    lookup_plugin = LookupModule()

    # Parse parameters
    # TODO: inside params

# Generated at 2022-06-13 13:57:01.767971
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class ConfigParserMock:
        def __init__(self, *args, **kwargs):
            self.contents = {
                'section1': {
                    'key1': 'value1_section1',
                    'key2': 'value2_section1'
                },
                'section2': {
                    'key1': 'value1_section2',
                    'key2': 'value2_section2'
                }
            }

        def items(self, section):
            return self.contents[section].items()

        def get(self, section, key):
            return self.contents[section][key]

    # Get all values from a section using a regexp
    cp = ConfigParserMock(allow_no_value=False)
    lu = LookupModule()
    lu.cp = cp
   

# Generated at 2022-06-13 13:57:13.421825
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Case 1 - regexp = False
    # key = test_ini_key
    # section = test_ini_section
    # expected_return = "test_ini_value"
    lm = LookupModule()
    terms = ['']
    variables = {}
    kwargs = {
        '_original_file': '/home/yannig/workspace/git/ansible/hacking/test/utils/test.ini',
        'file': '/home/yannig/workspace/git/ansible/hacking/test/utils/test.ini',
        'section': 'test_ini_section',
        're': False
    }

    lm.run(terms, variables, **kwargs)
    key = "test_ini_key"


# Generated at 2022-06-13 13:57:25.695347
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # First test why there is no key in the ini file
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.add_section('test')
    lm.cp.set('test', 'key1', 'toto')
    assert lm.get_value('key2', 'test', 'tata', False) == 'tata'

    # Second test with key1
    assert lm.get_value('key1', 'test', 'tata', False) == 'toto'

    # Third test with regexp
    lm.cp.set('test', 'key2', 'titi')
    assert lm.get_value('key.', 'test', 'tata', True) == 'toto'



# Generated at 2022-06-13 13:57:33.120953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import StringIO
    from ansible.plugins.lookup.ini import LookupModule
    ini_file = StringIO()

# Generated at 2022-06-13 13:57:42.926392
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule object
    lookup = LookupModule()

    # Create a term
    term = "user=root re=False section=global default= default_user file=ansible.ini type=ini"

    # Create a dict to store parameters
    paramvals = {'user': None, 're': False, 'section': 'global', 'default': 'default_user', 'file': 'ansible.ini', 'type': 'ini'}

    # Split the term
    (key, params) = term.split("=", 1)
    paramvals['user'] = params

    # Return a string
    user = lookup.get_value("user", paramvals['section'], paramvals['default'], paramvals['re'])
    assert user == 'root'



# Generated at 2022-06-13 13:57:55.526650
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_parse_params(term, paramvals):
        # reset the value of kv_parser attribute
        try:
            del LookupModule.kv_parser
        except AttributeError:
            pass
        return LookupModule.parse_params(term, paramvals)

    # test if params are correctly parsed
    p = {'name': 'test', 'val': ''}
    arr = test_parse_params('foo=bar', p)
    assert arr == [p['name'] + '=foo', p['val']]

    # test if the first param is not overwritten
    p = {'name': 'test', 'val': 'default'}
    arr = test_parse_params('foo=bar default', p)
    assert arr == [p['name'] + '=foo', 'default']

# Generated at 2022-06-13 13:58:20.623426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize class to test
    lookup_module = LookupModule()

    # Create the parameters for the test
    term = "**test**"
    variables = {
        "ansible_lookup_file": "file"
    }
    kwargs = {
        "encoding": "utf-8",
        "default": "",
        "section": "global",
        "re": False,
        "case_sensitive": True,
        "allow_no_value": True,
        "file": "test.ini"
    }

    # Create a ConfigParser
    lookup_module.cp = configparser.ConfigParser()

    # Call the run method
    lookup_module.run([term], variables=variables, **kwargs)

# Generated at 2022-06-13 13:58:34.440159
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lu = LookupModule()

    # Check that a single value is returned with good key and section
    class Config:
        def __init__(self):
            self.key = "value"
            self.key2 = "other"
    lu.cp = Config()
    assert lu.get_value("key", None, None, None) == "value"
    assert lu.get_value("key", "", None, None) == "value"

    # Check default value is returned with bad key
    assert lu.get_value("bad", None, "default", None) == "default"

    # Check values are returned with regexp
    class Config:
        def __init__(self):
            self.key1 = "value1"
            self.key2 = "value2"
            self.key3 = "other"

# Generated at 2022-06-13 13:58:38.337944
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    var = lookup.run(terms=['key'],
                     variables={},
                     file='users.ini',
                     section='section1')
    assert var[0] == 'value'


# Generated at 2022-06-13 13:58:51.742853
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:59:00.278575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # default values
    paramvals = {
        'file': 'ansible.ini',
        'section': 'global',
        're': False,
        'encoding': 'utf-8',
        'type': 'ini',
        'default': ''
    }

    # test file
    config = StringIO()
    config.write("[global]\nsection1=value2\nsection2=value2\n")
    config.seek(0, os.SEEK_SET)
    lookup_plugin.cp = configparser.ConfigParser()
    lookup_plugin.cp.readfp(config)

    # Test simple key
    params = _parse_params("section1", paramvals)

# Generated at 2022-06-13 13:59:10.549382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ###############################
    # Case 1:
    #   - key: user
    #   - section: integration
    #   - file: "ansible.ini"
    #   - type: "ini"
    #   - default: ""
    #   - re: False
    #   - encoding: "utf-8"
    ###############################
    # Arrange
    terms = ['user']
    variables = {}
    kwargs = {'type': 'ini', 'section': 'integration', 'file': 'ansible.ini', 'default': '', 're': False, 'encoding': 'utf-8'}
    l = LookupModule()

    # Act
    l.run(terms=terms, variables=variables, **kwargs)

    # Assert
    assert(l.cp != None)


# Generated at 2022-06-13 13:59:21.583565
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil

    test_config_path = os.path.join("test_ini_lookup.cfg")
    test_config_file = open(test_config_path,"w")
    test_config_content = """
#
# this is a comment
#
[java_properties]
    user = root
    password = secret
[server]
    host = localhost
    port = 22
    """
    test_config_file.write(test_config_content)
    test_config_file.close()

    # Test ansible.cfg
    real_config_path = os.path.realpath("/etc/ansible/ansible.cfg")
    real_config_dir = os.path.dirname(real_config_path)

# Generated at 2022-06-13 13:59:31.276263
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test parameters
    terms = [ 'user', 'date' ]
    variables = None
    file = 'test.ini'
    section = 'section1'
    type = 'ini'
    default = ''
    encoding = 'utf-8'
    re = False
    # Create an empty instance of LookupModule
    lookup_module = LookupModule()
    # Set parameters
    lookup_module.set_options(var_options = variables, direct = { 'file': file, 'section': section, 'type': type, 'default': default, 'encoding': encoding, 're': re })
    # Test the method
    result = lookup_module.run(terms)
    # Asserts
    assert len(result) == 2
    assert result[0] == 'testuser'

# Generated at 2022-06-13 13:59:42.118428
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    cp = configparser.ConfigParser()
    lookup_module.cp = cp
    cp.add_section('Section')
    cp.set('Section', 'key1', 'value1')
    cp.set('Section', 'key2', 'value2')
    cp.set('Section', 'key3', 'value3')
    cp.set('Section', 'key4', 'value4')
    cp.set('Section', 'key5', 'value5')

    assert lookup_module.get_value('key1', 'Section', 'default', False) == 'value1'
    assert lookup_module.get_value('key2', 'Section', 'default', False) == 'value2'
    assert lookup_module.get_value('key3', 'Section', 'default', False) == 'value3'

# Generated at 2022-06-13 13:59:50.478771
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import os
    import tempfile

    (fd, path) = tempfile.mkstemp()
    content = """
[section1]
key1 = value1
key2 = value2
"""
    os.write(fd, content)
    os.close(fd)

    # Retrieve a single value
    # Should return the value of the key 'key1' in the section 'section1'
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.read(path)
    value = lookup.get_value('key1', 'section1', '', False)
    assert value == 'value1'

    # Retrieve all values from a section using a regexp
    # Should return all the keys of the section 'section1' that match the regexp 'k.*'
    value = lookup.get

# Generated at 2022-06-13 14:00:23.986226
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    import sys
    import os
    search_paths = [os.path.dirname(os.path.abspath(__file__))]
    lookup_module = LookupModule(loader=None, templar=None, loader_available=False)
    lookup_module.set_options(loader_available=False, basedir=search_paths[0])

    # test 1
    path = lookup_module.find_file_in_search_path(None, 'files', 'test.ini')
    file = open(path).read()
    f = StringIO()
    f.write(file)
    f.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()
    cp.readfp(f)

    assert 'section1' in list(cp.sections())

# Generated at 2022-06-13 14:00:35.246953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with one key in a section
    test_module = LookupModule()
    test_module.cp = configparser.ConfigParser()
    test_module.cp.read("tests/fixtures/ini/test.ini")
    with open("tests/fixtures/ini/test.ini", "r") as f:
        contents = f.read()
    test_module.get_value = lambda key, section, dflt, is_regexp: key+" in "+section

# Generated at 2022-06-13 14:00:44.090442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the LookupModule class with simple configuration file
    """
    from ansible.parsing.vault import VaultLib
    contents = '''
[section_name]
key1=value1
key2=value2
    '''

    # Create VaultLib object
    vault_secret = VaultLib('test')

    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(contents)
    config.seek(0, os.SEEK_SET)

    cp = configparser.ConfigParser(allow_no_value=True)
    cp.readfp(config)

    # Create LookupModule object
    lookup = LookupModule()
    lookup.cp = cp

    # Simple test
    result = lookup.get_value('key1', 'section_name', 'default', False)

# Generated at 2022-06-13 14:00:53.830452
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule.
    """
    file = tmp_path('ini.tmp')
    with open(file, 'w') as file_writer:
        file_writer.write('[section1]\nkey1=value1\nkey2=value2\nkey3=value3\n')
        file_writer.write('[section2]\nkey4=value4\n')

    terms = ["key1"]
    options = {'file': str(file), 'section': 'section1', 'encoding': 'utf-8', 'default': '', 'case_sensitive': False}
    variables = {}
    lookup = LookupModule()
    lookup.set_options(var_options=variables, direct=options)
    ret = lookup.run(terms, variables)
    assert ret

# Generated at 2022-06-13 14:01:05.840964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.strategy import StrategyBase

    class TestLookupModule(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return terms

    class TestStrategy(StrategyBase):
        def __init__(self, tqm):
            self.tqm = tqm

        def run(self, iterator, play):
            pass

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['test_lookup_plugin_ini/hosts'])

# Generated at 2022-06-13 14:01:15.903697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    assert look.run(terms=['user', 'password'], variables=None, file='users.ini', section='integration') == ['john', 'secret']
    assert look.run(terms=['user.name'], variables=None, file='user.properties', type='properties') == ['John Doe']
    assert look.run(terms=['non_existent'], variables=None, file='users.ini', section='integration', default='no_one') == ['no_one']
    assert look.run(terms=['non_existent'], variables=None, file='users.ini', section='integration') == ['']
    assert look.run(terms=['user=root', 'password=secret'], variables=None, file='users.ini', section='integration') == ['', '']
    assert look

# Generated at 2022-06-13 14:01:26.820615
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Mock the search for file in seach path to find ini file
    module.find_file_in_search_path = lambda *args: '/home/gosty/test.ini'
    # Mock the method to get the file contents
    module._loader = MockLoader._loader
    # Unit test of method run
    assert module.run((["lookup", "key1=val1", "key2=val2", "key3"],)) == [u'value1']
    assert module.run((["lookup", "key1=val1", "key2=val2", "key3", "key4=val4", "key5=val5"],)) == [u'value1', u'value4']

# Generated at 2022-06-13 14:01:27.680600
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:01:38.387799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule object
    lookup_plugin = LookupModule()
    # Create a config file
    path = os.path.join(os.path.dirname(__file__), 'test_lookup_ini.ini')
    f = open(path, 'w')
    f.write('foo=bar')
    f.close()
    # Create a variable
    variables = dict(
        ansible_python_interpreter=sys.executable,
    )
    # Create a term
    terms = [
        """file='test_lookup_ini.ini' section='test_lookup_ini.ini' key='foo' default='nope' """
    ]
    # Test run
    ret = lookup_plugin.run(terms, variables=variables, **{'_terms': terms})

# Generated at 2022-06-13 14:01:49.131560
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test `LookupModule.run([...])` method
    """
    from ansible.module_utils._text import to_bytes
    lookup_instance = LookupModule()
    lookup_instance.set_options(
        var_options=None,
        direct={'section': 'section1', 'file': 'test.ini'})

    # Create a mocked configparser object
    cp_inst = configparser.ConfigParser()
    cp_inst.add_section('section1')
    cp_inst.set('section1', 'foo', 'bar1')
    cp_inst.set('section1', 'bar', 'foo1')
    cp_inst.set('section1', 'foobar', 'barfoo')
    cp_inst.set('section1', 'barfoobar', 'foobarbar')
    cp_inst.set