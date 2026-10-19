

# Generated at 2022-06-13 13:52:40.449343
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Method get_value of class LookupModule is tested
    from collections import Mapping
    from six import string_types

    class ConfigParser(Mapping):

        def __init__(self, a_dict):
            self._dict = a_dict

        def __contains__(self, item):
            return item in self._dict

        def __getitem__(self, item):
            return self._dict[item]

        def __iter__(self):
            return self._dict.__iter__()

        def __len__(self):
            return len(self._dict)

        def items(self, section):
            return self._dict[section]

        def get(self, section, key):
            return self._dict[section][key]

    get_value = LookupModule.get_value.__func__

    # Section

# Generated at 2022-06-13 13:52:47.325524
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    cp.read_string(u"""
[section1]
key1 = value1
key2 = value2

[section2]
key3 = value3
key4 = value4
""")
    lookup_module = LookupModule()
    lookup_module.cp = cp

    # Retrieve a single value
    assert lookup_module.get_value('key1', 'section1', '', False) == 'value1'

    # Retrieve all values from a section using a regexp
    assert lookup_module.get_value('.*', 'section1', '', True) == ['value1', 'value2']

# Generated at 2022-06-13 13:52:58.934291
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule
    lookup_module.set_options = lambda x, y, z: None
    lookup_module.get_options = lambda x: {'type': 'ini'}
    lookup_module.find_file_in_search_path = lambda x, y, z: 'test.ini'
    lookup_module.get_value = lambda x: None
    lookup_module.run([("abc")])
    lookup_module.run([("abc=True")])
    lookup_module.run([("abc=True", "z")])
    lookup_module.run([("abc=True z")])
    lookup_module.run([("abc=True", "z=False")])



# Generated at 2022-06-13 13:53:11.283817
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import os.path

    # Create a temporary file with data
    (fd, file_name) = tempfile.mkstemp()
    test_data = u'''[test]\nkey1=value1\nkey2=value2'''
    os.write(fd, to_bytes(test_data, errors='surrogate_or_strict'))
    os.close(fd)

    # Define variables
    terms = [u'key1']
    variables = {u'ini_file': file_name}
    paramvals = {u'file':u'%(ini_file)s'}

    # Testing method
    lm = LookupModule(name="", class_name="", src_path="")
    result = lm.run(terms, variables, **paramvals)


# Generated at 2022-06-13 13:53:20.026103
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lm = LookupModule()

    # test with default parameters
    lm.run([u"user"])
    lm.run([u"user"], variables={u"ansible_local":{"files":["/test/users.ini"]}}, ansible_local_files=["/test/users.ini"])

    # test with a file
    lm.run([u"user"], variables={u"ansible_local":{"files":["/test/users.ini"]}}, ansible_local_files=["/test/users.ini"])

    # test regexp
    lm.run([u".*"], re=True)

    # test with default, regexp
    lm.run([u"user"], re=True)



    # test parse_params

# Generated at 2022-06-13 13:53:32.152789
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_mod = LookupModule()

    test_key_1 = 'test_key'
    test_key_2 = 'test_key_regexp'
    test_key_3 = 'test_key.regexp'
    test_key_4 = 't.*e'
    test_key_5 = '.*e'
    test_key_6 = '.*E'
    section = 'section1'
    dflt = 'default value'
    is_regexp = False

    test_1 = '[section1]\ntest_key=value 1\ntest_key_regexp=value 2'
    config = StringIO()
    config.write(test_1)
    config.seek(0, os.SEEK_SET)

# Generated at 2022-06-13 13:53:42.871151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pytest

    from ansible.constants import ROLE_CACHE_PLUGIN_PREFIX, ROLES_PATH
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import lookup_loader

    from ansible.plugins.lookup.ini import LookupModule, _parse_params
    from ansible.module_utils.six.moves import configparser
    from ansible.errors import AnsibleLookupError

    # TODO: this class is too tightly coupled to ansible internals to be reliably tested

    # TODO: move the ini file to the role fixtures dir

# Generated at 2022-06-13 13:53:50.912219
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of LookupModule
    _LookupModule = LookupModule()

    # Create a fake type for LookupModule
    class _LookupBase_:
        def __init__(self, variables):
            self.args = {'variables': variables}

    # Create a fake type for AnsibleModule
    class _AnsibleModule_:
        def __init__(self, argument_spec = None, **kwargs):
            self.params = kwargs
            self.argument_spec = argument_spec

    # Create a fake variables
    variables = {'ansible_env': {'HOME': '/home/vagrant'}}

    # Create a fake type for C
    class _C_(object):
        def __init__(self, paramvals):
            self.params = paramvals

    # Create a fake type for Ans

# Generated at 2022-06-13 13:54:03.444783
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Retrieve a single value
    term = 'user'
    # parameters specified?
    if '=' in term or ' ' in term.strip():
        params = _parse_params(term, paramvals)

# Generated at 2022-06-13 13:54:05.646159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('*** test_LookupModule_run ***')
    terms = ["user", "foo"]
    variables = None
    kwargs = {'file': 'users.ini', 'section': 'integration', 'default': 'nobody'}
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['root', 'nobody']


# Generated at 2022-06-13 13:54:20.798475
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.add_section('sec1')
    lm.cp.set('sec1', 'key1', 'value1')
    lm.cp.set('sec1', 'key2', 'value2')
    lm.cp.set('sec1', 'key3', 'value3')
    lm.cp.set('sec1', 're1', 'valuere1')
    lm.cp.set('sec1', 're2', 'valuere2')
    assert lm.get_value('nokey', 'sec1', False, False) == False
    assert lm.get_value('key1', 'sec1', False, False) == 'value1'

# Generated at 2022-06-13 13:54:31.941859
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Initialize
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.optionxform = str

    # Test
    section = 'section1'
    key = 'key1'
    value = 'value1'

    lm.cp.add_section(section)
    lm.cp.set(section, key, value)

    r = lm.get_value(key, section, None, False)
    assert r == value
    r = lm.get_value(key, section, None, True)
    assert r == value

# Generated at 2022-06-13 13:54:40.243497
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # settings
    test_ini_file = 'tests/unit/lookup_plugins/ini/test_ini'
    test_properties_file = 'tests/unit/lookup_plugins/ini/test_properties'

    # init
    module = LookupModule()
    expected_value = None

    # test ini file
    expected_value = 'value1'
    term = 'param1'
    paramvals = {'file': test_ini_file, 'section': 'section1', 're': False, 'default': None}
    value = module.get_value(term, paramvals['section'], paramvals['default'], paramvals['re'])
    assert value == expected_value

    expected_value = 'value2'
    term = 'param2'

# Generated at 2022-06-13 13:54:45.174383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    # Assuming this file is inside tests directory, change directory to get relative path
    os.chdir('../')

    # Create LookupModule object
    a = LookupModule()

    # Initialize file,section,key and expected values
    # Check for standard ini file
    terms = 'user'
    variables = None
    section = 'global'
    file = 'examples/ansible.ini'
    expected = 'root'
    actual = a.run(terms, variables, file=file, section=section)

    # Check whether the default value is returned when key doesn't exist
    assert expected == actual[0], 'Key doesn\'t exist in file'

    # Check when not passing file and section parameters
    file = 'ansible.ini'
    section = 'global'
    expected = 'root'
    actual = a

# Generated at 2022-06-13 13:54:52.182574
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:55:03.413881
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Successful case
    class TestLookupModule(LookupModule):
        def __init__(self):
            pass

        def run(self):
            return list()

        def set_options(self):
            pass

        def find_file_in_search_path(self):
            return os.path.join(os.getcwd(), 'test_LookupModule_get_value.ini')

        def _loader(self):
            return True

    f = open(os.path.join(os.getcwd(), 'test_LookupModule_get_value.ini'), 'a')
    f.write("\n[test]\n")
    f.write("item1=value1\n")
    f.write("item2=value2\n")
    f.write("item3=value3\n")


# Generated at 2022-06-13 13:55:15.750048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    safe_eval = LookupModule._safe_eval
    data = ['key1=value1', 'key2=value2', 'key3=', 'key4']
    paramvals = dict()
    paramvals['key1'] = None
    paramvals['key2'] = None
    paramvals['key3'] = None
    paramvals['key4'] = None
    result = list()
    for term in data:
        params = _parse_params(term, paramvals)
        try:
            for param in params:
                if '=' in param:
                    name, value = param.split('=')
                    paramvals[name] = value
                elif term == data[0]:
                    t = safe_eval(term)
            result.append(t)
        except ValueError:
            pass
    return result

# Generated at 2022-06-13 13:55:23.041018
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule.
    """
    # These are the methods that will be replaced by mocks
    LookupModule.find_file_in_search_path = find_file_in_search_path
    LookupModule._loader = _loader

    # Configuration
    test_conf = u"""
[test]
user: foo
password: bar
address: http://www.example.com
"""

    # Case 1: no params, default values
    term_list = [u"user"]
    params = {
        'file': 'ansible.ini',
        'section': 'global',
        'default': '',
        're': False,
    }
    assert LookupModule().run(terms=term_list, variables=params) == [u'default_user']

    # Case 2

# Generated at 2022-06-13 13:55:31.135055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # get_value test
    class DummyConfigParser():
        def __init__(self):
            self.params = {}

        def items(self, section):
            return self.params[section].items()

        def get(self, section, option):
            return self.params[section][option]

    cp = DummyConfigParser()
    cp.params['section1'] = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    lookup.cp = cp
    assert lookup.get_value('key2', 'section1', None, False) == 'value2'
    assert lookup.get_value('key4', 'section1', 'default', False) == 'default'

# Generated at 2022-06-13 13:55:39.215500
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a new LookupModule object
    lookup = LookupModule()

    # Try to retrieve all keys from a section
    terms = [""]
    terms[0] = "repo_user.*"
    result = lookup.run(terms, variables={"section":"section1", "file":"test.ini", "re":True})

    # Check if result is the expected one
    assert result == ['user1', 'user2'], "Unexpected result returned, test_LookupModule_run()"


# Generated at 2022-06-13 13:56:04.834402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    # Test with file ansible.ini and section global
    terms = [('user', 'global'), ('uid', 'global', '1000')]
    result = l.run(terms)
    assert result == ['yannig','1000']

    # Test with file ansible.ini and section integration
    terms = [('user', 'integration'), ('uid', 'integration')]
    result = l.run(terms)
    assert result == ['user1', '1000']

    # Test with file ansible.ini and section production
    terms = [('user', 'production'), ('uid', 'production')]
    result = l.run(terms)
    assert result == ['user2', '1001']

    # Test with file users.properties and section java_properties

# Generated at 2022-06-13 13:56:15.442815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    lookup_plugin = LookupModule()
    cp = configparser.ConfigParser()

    # Mock
    lookup_plugin.cp = cp
    lookup_plugin.cp.readfp = lambda x: None

    # Test with first only
    assert lookup_plugin.run([u'test']) == [None]

    # Test with one param
    lookup_plugin.cp.get = lambda x, y: u'my_test'
    assert lookup_plugin.run([u'test=blah', u'test2']) == [u'my_test', u'my_test']

    # Test with two params
    assert lookup_plugin.run([u'test=blah test2=blah', u'test2']) == [u'my_test', u'my_test']

# Generated at 2022-06-13 13:56:26.398794
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.plugins import lookup_loader
    lookup_plugins = lookup_loader.LookupBase.get_lookup_plugins()
    lookup = lookup_plugins['ini'](None, {})

    # Get path lookup plugin ini
    path = unfrackpath("/simple/path/to/ansible/lib/ansible/plugins/lookup/ini.py")
    path = path.replace("/lib/ansible/plugins/lookup/ini.py", "/test/unit/test_lookup_plugin.py")

    # Create ini test file
    ini_test_file1 = open(path, "w")

# Generated at 2022-06-13 13:56:37.711199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    #  some test data, a parametrized test would be possible, but probably overkill for for this puprose
    ini_data ={
        'section1': {
            'key1': 'val1',
            'key2': 'val2',
            'key3': 'val3',
            'key4': 'val4'
        },
        'section2': {
            'key1': 'val1',
            'key2': 'val2',
            'key3': 'val3',
            'key4': 'val4'
        }
    }

# Generated at 2022-06-13 13:56:50.344823
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create a LookupModule
    module = LookupModule()

    # Create a StringIO to use with configparser
    config = StringIO()

    # Define a StringIO content to parse
    config.write(u"""\
[section1]
key1=value1
key2=value2
key3=value3
[section2]
key4=value4
key5=value5
key6=value6
""")
    config.seek(0, os.SEEK_SET)

    # Initialize the configuration parser
    module.cp = configparser.ConfigParser()
    module.cp.readfp(config)

    # Test on multiple result using regexp
    ret = module.get_value(".*", "section1", None, True)
    assert len(ret) == 3
    assert "value1" not in ret

# Generated at 2022-06-13 13:57:01.891291
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    module = LookupModule()
    cp = configparser.ConfigParser()
    cp.add_section('global')
    cp.set('global', 'user', 'yperre')
    cp.add_section('section1')
    cp.set('section1', 'port', '80')
    cp.set('section1', 'host', 'example.com')
    module.cp = cp

    # get the value of a key in a section
    assert module.get_value('user', 'global', None, False) == 'yperre'

    # get the value of a key with a regexp in a section
    assert module.get_value('por.*', 'section1', None, True) == ['80']

    # get the value of a key with a regexp in a section

# Generated at 2022-06-13 13:57:13.501611
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # DummyIniFile
    ini_file = """
[section1]
key1=value1
key2=value2

[section2]
key3=value3
key4=value4
    """

    # Ansible Variables
    test_variables = None

    # Ansible Parameters
    test_terms = [u'key1=key1', u'key3']
    test_kwargs = {'file': u'DummyIniFile.ini', 'section': u'section1', 'encoding': u'utf-8', 'default': u'', 're': False, 'case_sensitive': False}

    # Expected Result
    expected_result = [u'value1']

    # Test LookupModule
    test_lookup_module = LookupModule()

    # Add DummyIniFile to

# Generated at 2022-06-13 13:57:25.785868
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # prepare lookupmodule
    term = 'user.name'
    options = {'type': 'properties', 'file': 'test.properties'}
    lookupmodule = LookupModule()
    lookupmodule.set_options(direct=options)
    # prepare data
    config = StringIO()
    config.write(u'[java_properties]\nuser.name=Dude\n')
    config.write(u'user.pass=password')
    config.seek(0, os.SEEK_SET)
    lookupmodule.cp = configparser.ConfigParser()
    lookupmodule.cp.readfp(config)
    # run
    var = lookupmodule.get_value(term, 'java_properties', lookupmodule.get_options()['default'], False)
    assert var == 'Dude'

# Generated at 2022-06-13 13:57:33.171700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a mock class to replace the ansible.utils.unsafe_proxy.AnsibleUnsafeText class
    class MyUnsafeText:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

    # create a mock class to replace the ansible.utils.vars.VariableManager class
    class MyVariableManager:
        def __init__(self):
            pass

        def __getitem__(self, name):
            return str(self.value)

        def __setitem__(self, name, value):
            self.value = value

    # create a mock class to replace the ansible.vars.unsafe.AnsibleVars class

# Generated at 2022-06-13 13:57:43.246226
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO

    l = LookupModule()
    l.cp = configparser.ConfigParser()

    l.cp.readfp(StringIO(u"""
[global]
user = root
port = 22
""".lstrip()))

    ret = l.run(['user', 'port'], parameters={'section': 'global'})
    assert ret == ['root', '22']

    l.cp.readfp(StringIO(u"""
[global]
key = value
port = 22
key = value2
""".lstrip()))

    ret = l.run(['key'], parameters={'section': 'global'})
    assert ret == ['value', 'value2']


# Generated at 2022-06-13 13:58:24.761953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # No section test
    class TestClass(MutableMapping):
        def __init__(self, opt):
            self.opt = opt

        def __getitem__(self, key):
            return self.opt[key]

        def __setitem__(self, key, value):
            self.opt[key] = value

        def __delitem__(self, key):
            del self.opt[key]

        def __iter__(self):
            return self.opt.__iter__()

        def __len__(self):
            return self.opt.__len__()


# Generated at 2022-06-13 13:58:30.830534
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of class LookupModule
    lm = LookupModule()

    # Create an instance of class configparser.ConfigParser
    # for testing
    cp = configparser.ConfigParser()
    config = StringIO()
    config.write(u'[vars]\n')
    config.write(u'key=value\n')
    config.write(u'foo=bar\n')
    config.write(u'foo=baz\n')
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)

    # Define test cases for method run

# Generated at 2022-06-13 13:58:43.258538
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module = LookupModule()
    # Test with empty file
    cp = configparser.ConfigParser()
    lookup_module.cp = cp
    # Test get_value
    assert lookup_module.get_value("test", "DEFAULT", "default", False) == "default"
    # Test get_value with regexp
    assert lookup_module.get_value(".*", "DEFAULT", "default", True) == []
    # Test get_value with regexp and value
    cp.readfp(StringIO('[DEFAULT]\ntest=val\nhello=world'))
    assert lookup_module.get_value(".*", "DEFAULT", "default", True) == ["val", "world"]
    # Test get_value with regexp and value

# Generated at 2022-06-13 13:58:55.042033
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule

    class AnsibleOptions(object):
        def __init__(self):
            self.encoding = 'utf-8'
            self.file = None
            self.section = 'mysection'
            self.default = None
            self.re = False
            self.type = 'ini'

    class AnsibleVars(object):
        def __init__(self):
            self.loader = 'default'
            self.lookupfile = 'default'

    lookup_module = LookupModule()
    options = AnsibleOptions()
    options.file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../lookup_plugins/tests/ini_test.ini')
    options.type = 'properties'
   

# Generated at 2022-06-13 13:59:02.694903
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Define ansible options
    ansible_options = {'file': 'test.ini',
                       'default': '',
                       'encoding': 'utf-8',
                       'section': 'global'}
    module = LookupModule()

    # Define ini file format
    config = StringIO()
    config.write(u'[global]\n')
    config.write(u'key=value')
    config.seek(0, os.SEEK_SET)

    try:
        module.cp.readfp(config)
    except configparser.DuplicateOptionError as doe:
        raise AnsibleLookupError("Duplicate option in '{file}': {error}".format(file=ansible_options['file'], error=to_native(doe)))

    # Test lookup

# Generated at 2022-06-13 13:59:03.938014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TBD
    return


# Generated at 2022-06-13 13:59:13.608591
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['foo', 'bar']
    result = "foo"
    file_path = os.path.join(os.path.dirname(__file__), 'test.ini')
    default_file_path = os.path.join(os.path.dirname(__file__), 'ansible.ini')
    variables = None
    paramvals = {'type': 'ini', 'file': file_path, 'section': 'test', 'default': None, 're': False}
    c = configparser.ConfigParser()
    lookup_module = LookupModule()
    c.readfp(open(paramvals['file']))
    for term in terms:
        result = lookup_module.get_value(term, paramvals['section'], paramvals['default'], paramvals['re'])
        assert result != None
        assert term

# Generated at 2022-06-13 13:59:24.501020
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Create a LookupModule object and a configparser object
    lookup_module = LookupModule()
    configparser = lookup_module.cp

    # Define section, key and value
    section = 'php'
    key = 'user=www-data'
    value = 'www-data'

    # Define a config file
    config_string = '[php]\n\
    user=www-data'

    # Create StringIO later used to parse ini
    config = StringIO()
    config.write(config_string)
    config.seek(0, os.SEEK_SET)

    # Parse config
    configparser.readfp(config)

    # Test 1
    result = lookup_module.get_value(key, section, None, False)
    assert result == value

    # Test 2
    result = lookup

# Generated at 2022-06-13 13:59:25.456249
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: not implemented
    pass

# Generated at 2022-06-13 13:59:33.386189
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup_module_obj = LookupModule()

    # No section and key in config
    lookup_module_obj.cp = configparser.ConfigParser()
    lookup_module_obj.cp.add_section('section1')
    lookup_module_obj.cp.set('section1', 'key1', 'value1')
    lookup_module_obj.cp.set('section1', 'key2', 'value2')
    lookup_module_obj.cp.set('section1', 'key3', 'value3')
    assert lookup_module_obj.get_value('key4', 'section1', 'default', False) == 'default'

    # Section without key in config
    lookup_module_obj.cp = configparser.ConfigParser()
    lookup_module_obj.cp.add_section('section2')
    assert lookup_module_

# Generated at 2022-06-13 14:00:51.775740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    params_list = [["user", "section=integration,file=users.ini"],
                   ["user", "section=production,file=users.ini"],
                   ["user.name", "type=properties,file=user.properties"]]
    for params in params_list:
        ret = lookup_obj.run(params, variables=None, **{'file': 'ci.ini'})
        lookup_obj.run(params, variables=None, **{'file': 'ci.ini'})
        assert(isinstance(ret[0], str) or isinstance(ret[0], unicode))


# Generated at 2022-06-13 14:01:04.903681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    params = {
        'file': 'users.ini',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
        're': False
    }
    # Read 'user' in global section
    params['section'] = 'global'
    # Verify that the call works with python3
    # This is a dummy class because we can't instantiate LookupBase
    class DummyLoader:
        def __init__(self):
            pass

        def _get_file_contents(self, path):
            return '', True
    lmodule = LookupModule(loader=DummyLoader())
    terms = ['user']
    result = lmodule.run(terms, variables=None, **params)
    assert result == ['yannig']

    # Read 'user' in global section


# Generated at 2022-06-13 14:01:15.527992
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    class Options(object):
        def __init__(self, connection, remote_user, ask_sudo_pass, verbosity,
                     module_path, forks, become, become_method, become_user,
                     check, diff, listhosts, listtasks, listtags, syntax):
            self.connection = connection
            self.remote_user = remote_user
            self.ask_pass = ask_sudo_pass
            self.verbosity = verbosity
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method

# Generated at 2022-06-13 14:01:25.951387
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """
    test to get value
    """
    lookup = LookupModule()
    temp_c = configparser.ConfigParser()
    temp_c.add_section('test1')
    temp_c.set('test1', 'abc', 'abc')
    temp_c.set('test1', 'def', 'def')
    temp_c.set('test1', 'abcd', 'abcd')
    lookup.cp = temp_c
    section = 'test1'
    dflt = 'default'
    is_regexp = True
    result = lookup.get_value('abc', section, dflt, is_regexp)
    assert result == ['abc','abcd']

# Generated at 2022-06-13 14:01:33.076998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    retval = None

    class TestLookupModule(LookupModule):
        def __init__(self):
            self.cp = None
            return

        def run(self, terms, variables=None, **kwargs):
            nonlocal retval
            retval = super(TestLookupModule, self).run(terms, variables, **kwargs)
            return

    t = TestLookupModule()
    t.run([
        'foo=bar arg1 arg2', 
        'bar baz=foo arg3 arg4'
        ], variables={'files': [os.curdir]}, file='test.ini', section='section1')
    assert (retval == ['arg1', 'arg3'])

# Generated at 2022-06-13 14:01:40.974280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This function test method LookupModule.run.
    """

    ret = LookupModule().run([
        'user',
        'ssh_key=',
        'user_name=+-_',
        'user',
        'other_key=',
        'user'], variables={},
        file='ansible.ini', section='section1',
        case_sensitive=True)
    assert ret == ['user1', 'user2', 'value', 'value2', 'user3']

    ret = LookupModule().run([
        'user', 'ssh_key=', 'user', 'other_key=', 'user'], variables={},
        file='ansible.ini', section='section2', case_sensitive=True)

# Generated at 2022-06-13 14:01:50.188580
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic
    module_args = dict(
        terms=[
            "user",
            "group"
        ],
        section="integration"
    )
    module = basic.AnsibleModule(argument_spec={})

    # Fake file
    test_ini_file = """
[integration]
user = ansible
group = admins

[production]
user = root
group = root
"""
    # Create fake file and put it in fake search
    fake_file = """
[integration]
user = ansible
group = admins

[production]
user = root
group = root
"""
    fake_search = [os.path.join(os.path.dirname(__file__), 'fake_search')]

    # Fake lookup object

# Generated at 2022-06-13 14:01:55.769552
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check if returned type is a dict
    def test_returned_type():
        test_term = [
            {
                "file": "test.ini",
                "key": "test.int",
                "section": "test",
                "type": "ini"
            },
        ]

        for test_arg in test_term:
            assert(isinstance(LookupModule().run(terms=[test_arg]), dict))

# Generated at 2022-06-13 14:02:02.376481
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input_data = """
[section1]
test1=value1
test2=value2
test3=
test4=value4
test5=
test6=value6
test7=value7
    """
    config = configparser.ConfigParser()
    config.read_string(input_data)
    lookup_params = {
        'type': 'ini',
        'file': 'file',
        'section': 'section1',
        're': True,
        'encoding': 'utf-8',
        'default': '',
        'case_sensitive': False,
        'allow_no_value': False,
        'allow_none': False,
        '_terms': [],
        '_terms_slurped': [],
    }
    lookup_params['_terms'] = ['value1']
   

# Generated at 2022-06-13 14:02:13.798237
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with ini file
    lookup_plugin = LookupModule()
    terms = ["user"]
    paramvals = dict(
        file='test.ini',
        section="test",
        type='ini',
        re=False,
        encoding='utf-8'
    )
    ret = [
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig",
        "yannig"
    ]
    res = lookup_plugin.run(terms, variables=None, **paramvals)
    assert ret == res

    # Test with properties