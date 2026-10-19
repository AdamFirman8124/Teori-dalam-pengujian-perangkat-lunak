

# Generated at 2022-06-13 13:52:41.449429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    _terms = [
        'user',
        'user=nobody section=production file=users.ini',
        'user=nobody section=integration file=users.ini',
        'user section=production file=users.ini',
        'user,user=nobody section=integration file=users.ini',
        'user section=production file=users.ini',
        'user=nobody section=production file=users.ini',
        'user2 section=production file=users.ini',
        'user2=nobody section=integration file=users.ini',
        'user2 section=production file=users.ini',
        'user2=nobody section=production file=users.ini',
    ]


# Generated at 2022-06-13 13:52:48.990643
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    with open('./tests/unit/lookup_plugins/test.ini', 'r') as file:
        file_contents = file.read()

    test_lookup = LookupModule()

    # Test case without the plugin parameters
    test_lookup.find_file_in_search_path = lambda variables, directories, filename: './tests/unit/lookup_plugins/test.ini'
    test_lookup._loader._get_file_contents = lambda path: (file_contents, None)

    # Test case : Test the method run by reading one key of the ini file
    test_terms = ['./tests/unit/lookup_plugins/test.ini password=test_password section=section1 key=key1 default=default_value']

# Generated at 2022-06-13 13:52:57.749623
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test function of LookupModule.run()
    '''
    terms = ['ansible', 'mongo', 'mongodb']
    variables = {}
    kwargs = {'default': '', 'encoding': 'utf-8', 're': False, 'file': 'test.ini', 'section': 'test', 'type': 'ini'}
    lookup = LookupModule()
    lookup.run(terms, variables, **kwargs)

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:53:05.873382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Loading classes
    import sys
    module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, module_path)
    import ansible.plugins.lookup.ini as ini
    import ansible.plugins.loader as loader
    import ansible.vars.manager as var_manager

    # Instantiating classes
    cls = ini.LookupModule()
    ldr = loader.LookupModuleLoader()
    var = var_manager.VariableManager()

    # Looking up if the lookup_plugin is on the lookup_loader
    assert "ini" in loader.LookupModuleLoader._lookup_plugins

    # Loading the parameters
    cls.set_options({'_original_file': 'ini.yml'})


# Generated at 2022-06-13 13:53:16.630285
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import configparser

    # Build dummy configuration file
    config = configparser.ConfigParser()
    config.add_section('integration')
    config.set('integration', 'user', 'Yannig')
    config.add_section('production')
    config.set('production', 'user', 'Herve')
    cfg_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    config.write(cfg_file)
    cfg_file.close()

    # Test - get value for a given key in a given section
    assert LookupModule().run([
        'user',
        'file=%s' % cfg_file.name,
        'section=integration'
    ], variables=dict()) == ['Yannig']

# Generated at 2022-06-13 13:53:29.425929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import datetime
    # Testing LookupModule.run("...", file="...", encoding="...") when data from 'file' are read
    # -----------------------------------------------
    # Given: A file 'testLookupModule.ini' in current folder 
    #        with this data
    #
    #   [global]
    #   first_global=global
    #
    #   [section1]
    #   first_section1=section1
    #   second_section1=section1
    #
    #   [section2]
    #   first_section2=section2
    #   second_section2=section2
    #   third_section2=section2
    
    # Given: A file 'testLookupModule.properties' in current folder 
    #        with this data
    #
    #   name1=value1

# Generated at 2022-06-13 13:53:37.208155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_args = {
        "file": '',
        "default": "",
        "re": False,
        "type": "ini",
        "encoding": "utf-8",
    }
    test_args["_raw_params"] = "key1,key2"
    result = lookup_module.run([],**test_args)
    assert len(result) == 2
    assert result == ["", ""]
    # Test run with file
    test_args = {
        "file": "just-a-file",
        "default": "",
        "re": False,
        "type": "ini",
        "encoding": "utf-8",
    }
    test_args["_raw_params"] = "key1,key2"
    result = lookup_

# Generated at 2022-06-13 13:53:45.456240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Load class and method to test
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six.moves import StringIO

    # Dummy parameters
    terms = ['user', 'password']
    parameters = {
        'file': 'test_sample.ini',
        'section': 'Test_section',
        'default':'default'
    }
    config = StringIO("""
[Test_section]
user=Tester
password=TrustNo1
""")

    # Launch test
    lookup_module = LookupModule()
    result = lookup_module.run(terms, parameters, None, config, None)

    # Check results
    assert result[0] == 'Tester'
    assert result[1] == 'TrustNo1'
    assert result[0] != 'default'
   

# Generated at 2022-06-13 13:53:46.733892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for run method in class LookupModule"""
    # TODO: implement unit tests
    pass

# Generated at 2022-06-13 13:53:58.299996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    params = {
        'file': 'users.ini',
        'type': 'ini',
        'case_sensitive': False,
        'encoding': 'utf-8',
        'default': '',
        'section': 'global',
        're': False,
    }

    # Test with one key
    result = LookupModule().run(terms = ['user'], parameters = params)
    assert result == ['yannig']
    
    # Test with two keys
    result = LookupModule().run(terms = ['user', 'password'], parameters = params)
    assert result == ['yannig', 'xxxxx']

    # Test with one key and a defined section
    params['section'] = 'production'
    result = LookupModule().run(terms = ['user'], parameters = params)
    assert result == ['root']

# Generated at 2022-06-13 13:54:11.453512
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    test_ini_file = '''[global]
g_key1 = 1
g_key2 = 2
g_key3 = 3
g_key4 = 4
[section1]
s1_key1 = 1
s1_key2 = 2
s1_key3 = 3
s1_key4 = 4
[section2]
s2_key1 = 1
s2_key2 = 2
s2_key3 = 3
s2_key4 = 4
'''
    config = StringIO()
    config.write(u'%s' % test_ini_file)
    config.seek(0, os.SEEK_SET)
    cp.readfp(config)
    Lookup = LookupModule()
    Lookup.cp = cp

    # Normal use case

# Generated at 2022-06-13 13:54:20.328446
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from collections import namedtuple

    # Create a lookup object
    lookup_obj = LookupModule()

    # Configparser object
    cp = configparser.ConfigParser()
    cp.readfp(StringIO(u'[section]\nkey=value'))

    # Assign the configparser object to the lookup
    lookup_obj.cp = cp

    Params = namedtuple("Params", "section default re")

    # Testcase 1:
    params = Params("section","","False")
    assert lookup_obj.get_value("key",params.section,params.default,params.re) == "value"

    # Testcase 2:
    params = Params("section","default","True")
    assert lookup_obj.get_value("key",params.section,params.default,params.re) == "default"

# Generated at 2022-06-13 13:54:34.424797
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''
    from ansible.utils.listify import listify_lookup_plugin_terms
    import io
    import sys

    test = sys.modules[__name__]
    test.cp = configparser.ConfigParser(allow_no_value=False)
    test.cp.readfp(io.StringIO('''
[test]
key1=test1
key2=test2
'''))
    test.get_value = LookupModule.get_value.__get__(test, LookupModule)

    test.get_value.__dict__.update({'cp': test.cp})
    test.run = LookupModule.run.__get__(test, LookupModule)

# Generated at 2022-06-13 13:54:45.440683
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # WARNING: This method is used by Ansible unit tests.
    #          Modification of this method may breaks some tests.

    # Setup
    lookup_manager = LookupModule()
    lookup_manager.set_options(direct={'type': 'ini', 'case_sensitive': True, 'rc': True})
    config = configparser.ConfigParser()
    config.optionxform = str  # make case sensitive
    config.add_section('global')
    config.set('global', 'key1', 'value1')
    config.add_section('section1')
    config.set('section1', 'key2', 'value2')
    config.set('section1', 'key3.subkey1', 'value3')
    config.set('section1', 'key3.subkey2', 'value4')
    config.add_section

# Generated at 2022-06-13 13:54:57.816015
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lines = StringIO("""
    [section1]
    property11=value11
    property12=value12
    [section2]
    property21=value21
    property22=value22
    """)

    cp = configparser.ConfigParser()
    cp.readfp(lines)

    look = LookupModule()
    look.cp = cp

    assert look.get_value('property11', 'section1', None, False) == 'value11'
    assert look.get_value('property11', 'section1', None, True) == ['value11']
    assert look.get_value('property1.*', 'section1', None, True) == ['value11', 'value12']
    assert look.get_value('property21', 'section1', None, False) == None

# Generated at 2022-06-13 13:55:06.398227
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["test=testv", "test2=test2v", 'lookup_item'], {}, allow_no_value=True) == ['lookup_item']
    assert LookupModule().run(["test=testv test2=test2v", 'lookup_item'], {}, allow_no_value=True) == ['lookup_item']
    assert LookupModule().run(["test=testv test2=test2v lookup_item"], {}, allow_no_value=True) == ['lookup_item']
    assert LookupModule().run(["test=testv test2=test2v", 'lookup_item'], {}, allow_no_value=True) == ['lookup_item']

# Generated at 2022-06-13 13:55:20.474127
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile
    import shutil

    # Create temporary directory
    test_dir = tempfile.mkdtemp()

    # Create file with following content
    config = os.path.join(test_dir, 'config.ini')
    content = '''
    [global]
    debug = True
    log_path = /var/log/ansible/ansible.log
    hostfile = /etc/ansible/hosts
    pattern = *
    forks = 100
    '''

    # Write content to file
    with open(config, 'w') as file:
        file.write(content)

    # Create object LookupModule
    instance_class = LookupModule()

    # Set instance_class attributes
    instance_class.cp = configparser.ConfigParser()

    # Call run method
    instance_class

# Generated at 2022-06-13 13:55:25.849456
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    cp = configparser.ConfigParser()
    cp.add_section('section')
    cp.set('section', 'key1', 'value1')
    cp.set('section', 'key2', 'value2')

    test_cases = [
        ('key1', 'section', None, False, 'value1'),
        ('key2', 'section', None, False, 'value2'),
        ('key3', 'section', None, False, None),
        ('key1', 'section', None, True, ['value1']),
        ('key2', 'section', None, True, ['value2']),
        ('key3', 'section', None, True, []),
        ('.*', 'section', None, True, ['value1', 'value2']),
    ]


# Generated at 2022-06-13 13:55:40.303673
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    """
    Test function get_value of class LookupModule
    """

    test_instance = LookupModule()

    # Prepare a fake configuration file
    config_content = (
        '[global]\n',
        'user=john\n\n',
        '[integration]\n',
        'user=alice\n',
        'user.name=Alice\n',
        'user.password=secr3t\n\n',
        '[production]\n',
        'user=bob\n')
    config_fp = StringIO()
    for line in config_content:
        config_fp.write(line)
    config_fp.seek(0, os.SEEK_SET)

    # Read the fake file
    test_instance.cp = configparser.ConfigParser()

# Generated at 2022-06-13 13:55:45.461261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Test for method run of class LookupModule '''
    obj = LookupModule()  # instantiate class
    expected = ['value1', 'value2', 'value3']
    data = obj.run(['key', 'key'], [], file='test.ini')
    assert data == expected

# Generated at 2022-06-13 13:56:08.678864
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils import basic

    lm = LookupModule()
    lm.get_options = basic.FakeVars({})
    lm.run = basic.FakeModule().run
    lm.cp = configparser.SafeConfigParser()
    lm.cp.readfp(basic.FakeFile({}))

    data = {
        "basic": {
            "section": ["global"],
            "key": ["user"],
            "is_regexp": [False],
            "dflt": [""]
        },
        "regexp": {
            "section": ["global"],
            "key": [r".*"],
            "is_regexp": [True],
            "dflt": [""]
        }
    }


# Generated at 2022-06-13 13:56:17.433755
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lm = LookupModule()
    configs = StringIO()
    configs.write(u'[global]\n')
    configs.write(u'key1=value1\n')
    configs.write(u'key2=value2\n')
    configs.seek(0, os.SEEK_SET)

    lm.cp = configparser.ConfigParser(allow_no_value=True)
    lm.cp.readfp(configs)

    # retrieve key1 value in global section
    assert lm.get_value('key1', 'global', '', False) == 'value1'

    # retrieve key1 value in global section using regexp
    assert lm.get_value('.*', 'global', '', True) == ['value1', 'value2']

    # retrieve unknown key value

# Generated at 2022-06-13 13:56:27.615594
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test ini variable type
    lookup_module = LookupModule()
    assert lookup_module.run([u'user'], variables={}, section=u'integration', file=u'users.ini') == [u'ansible']

    # Test ini variable type with regexp
    lookup_module = LookupModule()
    assert lookup_module.run([u'.*'], variables={}, section=u'section1', file=u'test.ini', re=True) == [u'value1', u'value2', u'value3']
    lookup_module = LookupModule()
    assert lookup_module.run([u'.*'], variables={}, section=u'section2', file=u'test.ini', re=True) == [u'value4', u'value5', u'value6']

    # Test ini

# Generated at 2022-06-13 13:56:35.762225
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    from nose import SkipTest

    try:
        from ansible.plugins.lookup import LookupModule
    except ImportError:
        raise SkipTest('test skipped, lookup module not loaded')

    test_cp = configparser.ConfigParser(allow_no_value=False)
    test_cp.optionxform = to_native

    config = StringIO()
    config.write(u'[section_test]\n')
    config.write(u'key1=value1\n')
    config.write(u'key2=value2\n')
    config.write(u'key3=value3\n')
    config.seek(0, os.SEEK_SET)

    test_cp.readfp(config)

    t = LookupModule()
    t.cp = test_cp

    assert t.get_value

# Generated at 2022-06-13 13:56:42.912639
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    lookup.cp = configparser.ConfigParser()
    lookup.cp.add_section('section1')
    lookup.cp.set('section1', 'key1', 'value1')
    lookup.cp.set('section1', 'key2', 'value2.1')
    lookup.cp.set('section1', 'key2', 'value2.2')
    lookup.cp.add_section('section2')
    lookup.cp.set('section2', 'key1', 'value1')
    lookup.cp.set('section2', 'key2', 'value2')
    lookup.cp.set('section2', 'key3', 'value3')

# Generated at 2022-06-13 13:56:53.400333
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockConfig(object):

        def __init__(self):
            self.items = {}

        def set(self, section, key, param):
            self.items[(section, key)] = param

        def get(self, section, key):
            return self.items[(section, key)]

        def items(self, section):
            return self.items.items()

    # Mock lookup module
    module_mock = LookupModule()
    module_mock.cp = MockConfig()
    module_mock.cp.set("section", "key", "value")
    module_mock.cp.set("section", "regexp", "value1")
    module_mock.cp.set("section", "regexp2", "value2")

# Generated at 2022-06-13 13:57:03.969151
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_file = './test.ini'

    with open(test_file, 'w') as stream:
        stream.write('[section1]\n')
        stream.write('key1 = value1\n')
        stream.write('key2 = value2\n')
        stream.write('key3 = value3\n')
        stream.write('key4 = value4\n')
        stream.write('key5 = value5\n')

    loader = DictDataLoader({
        "files": {
            test_file: '',
        }})

    lookup_plugin = LookupModule()
    lookup_plugin._loader = loader

    # 1/6 : test to find all properties in a section

# Generated at 2022-06-13 13:57:10.957104
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class DummyConfigParser:

        def __init__(self):
            self.values = {
                'section': {
                    'key1': 'value1',
                    'key2': 'value2',
                    'key3': 'value3'
                }
            }

        def get(self, section, key):
            return self.values[section][key]

        def items(self, section):
            return self.values[section].items()

    lookup = LookupModule()
    lookup.cp = DummyConfigParser()

    # Test with no regexp
    ret = lookup.get_value('key1', 'section', False, False)
    assert ret == 'value1'

    # Test with regexp
    ret = lookup.get_value('key.*', 'section', False, True)

# Generated at 2022-06-13 13:57:18.391321
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    class ConfigParserFake:
        def __init__(self):
            self.all_values = [('fqdn', 'localhost'), ('type', 'frontend'), ('status', 'production'), ('nodes', '5')]

        def items(self, section):
            return self.all_values

    lookup = LookupModule()
    cp = ConfigParserFake()
    lookup.cp = cp

    assert lookup.get_value('fqdn', 'global', None, False) == 'localhost'
    assert lookup.get_value('type', 'global', None, False) == 'frontend'
    assert lookup.get_value('fqdn', 'global', None, True) == ['localhost']
    assert lookup.get_value('type', 'global', None, True) == ['frontend']

# Generated at 2022-06-13 13:57:28.296595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_ini = LookupModule()
    terms = ["key1", "key2", "key3", "key4=value4"]

    kwargs = {
        "type": "properties",
        "file": "test.properties",
        "section": "test",
        "re": False,
        "encoding": "utf-8",
        "default": "",
        "case_sensitive": True,
        "allow_no_value": False,
    }
    result = lookup_ini.run(terms, **kwargs)

    assert result[0] == "value1"
    assert result[1] == "value2"
    assert result[2] == "value3"

# Generated at 2022-06-13 13:58:04.216666
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Create a lookupModule instance
    lookupMod = LookupModule()

    # Create a configParser instance
    cp = configparser.ConfigParser()

    # Add a section named 'global' and add a property named 'user' with value 'test'
    cp.add_section('global')
    cp.set('global', 'user', 'test')

    # Add a section named 'production' and add a property named 'user' with value 'prod'
    cp.add_section('production')
    cp.set('production', 'user', 'prod')

    # Add a section named 'integration' and add a property named 'user' with value 'int'
    cp.add_section('integration')
    cp.set('integration', 'user', 'int')

    # Inject the configParser
    lookupMod.cp = cp

    #

# Generated at 2022-06-13 13:58:18.168980
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    sample_as_str = u'\n'.join(["[section1]", "key1 = value1", "key2 = value2", "key3 = value3", "[section2]", "key1 = value1", "key2 = value2", "key3 = value3", ""])
    sample = StringIO(sample_as_str)
    lm = LookupModule()
    lm.cp = configparser.ConfigParser()
    lm.cp.readfp(sample)
    assert lm.get_value("key1", "section1", "", False) == "value1"
    assert lm.get_value("key1", "section1", "", True) == ["value1", "value2", "value3"]

# Generated at 2022-06-13 13:58:25.137120
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    # Get test content
    content = """
#
# Ansible managed
#
[defaults]
host = fqdn = shortname = 127.0.0.1
port = 80
timeout = 5
"""
    # Check normal use of run method
    module = LookupModule()
    terms = ['host', 'port', 'timeout']
    vars = {'ansible_lookup_file_content': {'files/lookup/ini': content}}
    result = module.run(terms=terms, variables=vars, file="files/lookup/ini")
    assert result == ['fqdn = shortname = 127.0.0.1', '80', '5']

    # Check run method when type option is java properties
    terms = ['host']

# Generated at 2022-06-13 13:58:33.342415
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    cp = configparser.ConfigParser()

    # Parse file ini
    f = open('test.ini')
    cp.readfp(f)
    f.close()

    # Test for get_value methods on a key that exist
    assert LookupModule.get_value("user", "global", None, False) == "toto"

    # Test for get_value methods on a key that doesn't exist
    assert LookupModule.get_value("user2", "global", "test", False) == "test"

# Generated at 2022-06-13 13:58:44.798357
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    import pytest
    import configparser
    config = StringIO()
    config.write(u'[section]\n')
    config.write(u'key1 = value1\n')
    config.write(u'key2 = value2\n')
    config.write(u'key3 = value3\n')
    config.seek(0, os.SEEK_SET)
    cp = configparser.ConfigParser()

    cp.readfp(config)

    lm = LookupModule()
    lm.cp = cp

    all_values = lm.get_value(key='key.*', section='section', dflt=[], is_regexp=True)
    assert all_values == ['value1', 'value2', 'value3']


# Generated at 2022-06-13 13:58:55.481995
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''

    terms = ['foo', 'bar']
    kwargs = {'file': 'foo.ini',
              'type': 'ini',
              'default': '',
              're': False,
              'encoding': 'utf-8',
              'section': 'global'}
    config = {'global': {'foo': 'foo', 'bar': 'bar'}}
    test_lookup = LookupModule()
    test_lookup.cp = configparser.ConfigParser()
    for section, key_value in config.items():
        test_lookup.cp.add_section(section)
        for key, value in key_value.items():
            test_lookup.cp.set(section, key, value)
    assert terms == test_lookup.run

# Generated at 2022-06-13 13:59:02.448003
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    cp = configparser.ConfigParser()
    cp.readfp(StringIO(u'[section]\nkey=value'))

    lookup = LookupModule()
    lookup.cp = cp

    assert lookup.get_value('key', 'section', None, False) == 'value'
    assert lookup.get_value('key', 'section', 'default', False) == 'value'
    assert lookup.get_value('key', 'section', None, True) == 'value'
    assert lookup.get_value('key', 'section', 'default', True) == 'value'
    assert lookup.get_value('key', 'section1', None, False) == None
    assert lookup.get_value('key', 'section1', 'default', False) == 'default'

# Generated at 2022-06-13 13:59:12.141449
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.inventory.host import Host

    terms = [
        "foo=bar sec=toto",
        "foo=bar sec=toto apache",
        "foo=bar sec=toto apache value=42",
        "foo bar apache",
        "foo=bar re=False apache",
    ]
    class MockModule:
        def __init__(self):
            self.params = {}

    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    host = Host("test")
    variables = host.get_vars()
    ret = lookup_module.run(terms, variables)
    assert ret == [
        'foo',
        'apache',
        '42',
        'foo',
        '42',
    ]

# Generated at 2022-06-13 13:59:16.007008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options()
    result = lookup_module.run(['user', 'ssh', 'password', 'ip'], variables={}, file='ansible.ini')
    assert result == ['admin', '127.0.0.1', 'secret', '192.168.1.1']

# Generated at 2022-06-13 13:59:26.720230
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run(terms='user', variables=dict(files=[], file='./tests/fixtures/test_ini.ini'), section='integration') == ['Tina']

    assert lookup.run(terms='user.name', variables=dict(files=[], file='./tests/fixtures/test_ini.ini', type='properties')) == ['Tina']

    assert lookup.run(terms=['user1', 'user2', 'user3'], variables=dict(files=[], file='./tests/fixtures/test_ini.ini'), section='users') == ['Peter', 'Tina', 'Josh']


# Generated at 2022-06-13 14:00:34.097644
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    lk = LookupModule()
    key = 'key'
    section = 'section'
    dflt = None
    is_regexp = False

    ## Test with a not existing option
    lk.cp = configparser.ConfigParser()
    lk.cp.add_section(section)
    assert(lk.get_value(key, section, dflt, is_regexp) == dflt)
    assert(lk.get_value(key, section, dflt, is_regexp) is None)

    ## Test with a existing option
    value_expected = 'value'
    lk.cp.set(section, key, value_expected)
    assert(lk.get_value(key, section, dflt, is_regexp) == value_expected)

# Generated at 2022-06-13 14:00:41.942907
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    lookup = LookupModule()
    # Initialize configparser
    cp = configparser.ConfigParser()
    content = """[section1]
key1 = value1
key2 = value2

[section2]
key1 = value3
key2 = value4
"""
    cp.readfp(StringIO(content))
    lookup.cp = cp
    # Normal case
    assert lookup.get_value('key1', 'section1', 'default1', False) == 'value1'
    assert lookup.get_value('key2', 'section2', 'default2', False) == 'value4'
    # Key does not exist
    assert lookup.get_value('key3', 'section1', 'default3', False) == 'default3'
    # Section does not exist

# Generated at 2022-06-13 14:00:52.530161
# Unit test for method get_value of class LookupModule

# Generated at 2022-06-13 14:01:04.949551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.ini import LookupModule
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import os
    my_loader = None
    my_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    my_path = os.path.join(my_path, "test/test_playbooks/lookup_plugins/ini/test_files")
    my_path = os.path.join(my_path, "user.properties")
    lm = LookupModule(my_loader, run_once=True, basedir=my_path)

# Generated at 2022-06-13 14:01:08.793619
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    look = LookupModule()
    # Init configparser with [section1]
    s = StringIO("[section1]\nkey=value\nkey1=value1\nkey2=value2")
    look.cp = configparser.ConfigParser()
    look.cp.readfp(s)
    # Test if it returns value of key1 when re=False
    assert look.get_value("key1","section1","",False) == "value1"
    # Test if it returns list when re=True
    assert look.get_value("key","section1","",True) == ['key=value','key1=value1','key2=value2']

# Generated at 2022-06-13 14:01:17.359829
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    # Test for list value
    lookup = LookupModule()

    result = lookup.get_value('list', 'test', [], False)
    assert result == ['1', '2', '3']

    # Test for single value
    result = lookup.get_value('single', 'test', 'default', False)
    assert result == 'value'

    # Test for regexp
    result = lookup.get_value('(list|single)', 'test', 'default', True)
    assert result == ['1', '2', '3', 'value']

    # Test for default
    result = lookup.get_value('default', 'test', 'default', False)
    assert result == 'default'

    # Test for regexp with default
    result = lookup.get_value('none', 'test', 'default', True)

# Generated at 2022-06-13 14:01:27.704973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Define test ini file
    ini_content = """
[global]
url=http://example.com

[section1]
name=section1
value=section1_value

[section2]
name=section2
value=section2_value

[section3]
name=section3
value=section3_value

[section4]
name=section4
value=section4_value

[section5]
name=section5
value=section5_value
"""

    # Write test ini file
    with open('test.ini', 'w') as test_ini:
        test_ini.write(ini_content)

    # Define test class for test method run

# Generated at 2022-06-13 14:01:36.066642
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():
    # Instantiate LookupModule
    lookup_plugin = LookupModule()
    # Load INI file into LookupModule
    lookup_plugin.cp = configparser.ConfigParser()
    lookup_plugin.cp.read('ini.test')

    # Test multiple values
    assert lookup_plugin.get_value('.*', 'section1', None, True) == ['value1', 'value2']

    # Test single value
    assert lookup_plugin.get_value('key1', 'section1', None, False) == 'value1'
    assert lookup_plugin.get_value('missing_key', 'section1', None, False) == None
    assert lookup_plugin.get_value('missing_key', 'section1', 'default_value', False) == 'default_value'

# Generated at 2022-06-13 14:01:47.251475
# Unit test for method get_value of class LookupModule
def test_LookupModule_get_value():

    contents = u'\n'.join(["[section]", "foo=bar", "baz=qux", "moo=foo", "quxx=corge", "quxx=grault", "quxx=garply", "quxx=waldo", "quxx=fred", "quxx=plugh", "quxx=xyzzy", "quxx=thud"])

    lookup1 = LookupModule()
    cp1 = configparser.ConfigParser()
    config1 = StringIO()
    config1.write(contents)
    config1.seek(0, os.SEEK_SET)
    cp1.readfp(config1)
    lookup1.cp = cp1

    assert lookup1.get_value("foo", "section", False, False) == "bar"

# Generated at 2022-06-13 14:01:55.776728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Test method run of class LookupModule '''

    # Create a class object
    config_manager = LookupModule()

    # Test with a ini file with a section (in this case section "user")
    config_manager.cp = configparser.ConfigParser()
    config_manager.cp.read(u'ansible/test/units/module_utils/lookup/ini/user.ini')
    assert type(config_manager.run(terms=['user'], variables=None, **{'section': u'user'})) == list,\
        "test_LookupModule_run() : failed to test method run()"