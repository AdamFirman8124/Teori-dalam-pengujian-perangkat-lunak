

# Generated at 2022-06-12 21:08:51.585235
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_manager = ConfigManager(constants=dict())
    defs = config_manager.get_configuration_definitions()
    assert isinstance(defs, dict)


# Generated at 2022-06-12 21:09:00.027221
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    from ansible.utils import template
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText

    config = ConfigManager()


# Generated at 2022-06-12 21:09:07.076930
# Unit test for function get_config_type
def test_get_config_type():

    cfg1 = 'test1.ini'
    cfg2 = 'test2.cfg'
    cfg3 = 'test3.yaml'
    cfg4 = 'test4.yml'
    cfg5 = 'test5.json'
    cfg6 = 'test6.txt'
    cfg7 = 'test7.ini.tmp'
    cfg8 = 'test8.cfg.tmp'
    cfg9 = 'test9.yaml.tmp'
    cfg10 = 'test10.yml.tmp'

    assert get_config_type(cfg1) == 'ini'
    assert get_config_type(cfg2) == 'ini'
    assert get_config_type(cfg3) == 'yaml'
    assert get_config_type(cfg4) == 'yaml'
   

# Generated at 2022-06-12 21:09:15.127381
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():

    c = ConfigManager()

    defs = c.get_configuration_definitions()
    assert len(defs) > 0
    assert 'DEFAULT_DEBUG' in defs

    defs = c.get_configuration_definitions(plugin_type="callback")
    assert len(defs) == 0

    defs = c.get_configuration_definitions(plugin_type="callback", name="mute")
    assert len(defs) == 0

    defs = c.get_configuration_definitions(plugin_type="callback", name="minimal")
    assert len(defs) > 0
    assert 'verbosity' in defs

# Generated at 2022-06-12 21:09:18.502258
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_manager = ConfigManager()
    assert (isinstance(config_manager.get_configuration_definitions(), dict))



# Generated at 2022-06-12 21:09:25.893659
# Unit test for function get_config_type
def test_get_config_type():
    for cfile, expected in (
        (None, None),
        ("/path/to/some.file", None),
        ("/path/to/some.ini", "ini"),
        ("/path/to/some.cfg", "ini"),
        ("/path/to/some.yaml", "yaml"),
        ("/path/to/some.yml", "yaml"),
        ("/path/to/some.yamlyaml", None),
    ):
        assert get_config_type(cfile) == expected, "get_config_type() failed for %s" % cfile


# FIXME: see if we can unify with similar function used by config/base

# Generated at 2022-06-12 21:09:34.506698
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from collections import UserDict
    from ansible import constants as C
    from ansible.module_utils.common.collections import is_sequence

    class FakeArgs(UserDict):
        def __init__(self, *args, **kwargs):
            super(FakeArgs, self).__init__(*args, **kwargs)
            self.ad_hoc = 'ad_hoc'

    class FakeCLIARGS(UserDict):
        def __init__(self, *args, **kwargs):
            super(FakeCLIARGS, self).__init__(*args, **kwargs)
            self.subset = 'subset'

    cm = ConfigManager()

    # Define some config entries

# Generated at 2022-06-12 21:09:36.094446
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    ''' test the method get_config_value_and_origin of class ConfigManager '''
    pass



# Generated at 2022-06-12 21:09:37.711241
# Unit test for method update_config_data of class ConfigManager
def test_ConfigManager_update_config_data():
    raise NotImplementedError('Test for ConfigManager.update_config_data is not yet implemented.')

# Generated at 2022-06-12 21:09:43.681598
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    config_file = ''
    config_manager = ConfigManager(config_file)
    config = ''
    cfile = ''
    plugin_type = ''
    plugin_name = ''
    keys = ''
    variables = ''
    direct = ''
    config_manager.get_config_value_and_origin(config, cfile, plugin_type, plugin_name, keys, variables, direct)

# Generated at 2022-06-12 21:11:56.638663
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.utils import context


# Generated at 2022-06-12 21:12:04.414300
# Unit test for function get_ini_config_value
def test_get_ini_config_value():
    c = configparser.ConfigParser()
    test_ini = """
[plugin:test_ini_user]
b = 2
"""
    c.readfp(io.BytesIO(test_ini))
    assert get_ini_config_value(c, {'key': 'b', 'section': 'plugin:test_ini_user'}) == '2'
    assert get_ini_config_value(c, {'key': 'b'}) == None
    assert get_ini_config_value(c, {'key': 'b', 'section': 'plugin:fail'}) == None
    assert get_ini_config_value(c, {'key': 'b', 'section': 'plugin:test_ini_user', 'default': '3'}) == '2'

# Generated at 2022-06-12 21:12:05.713470
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    # test case 1
    # uncomment below line to run the utility
    #response = get_configuration_definitions(arg)
    pass


# Generated at 2022-06-12 21:12:12.774221
# Unit test for function ensure_type
def test_ensure_type():
    res = ensure_type('30', 'integer')
    assert res == 30
    res = ensure_type('30.0', 'float')
    assert res == 30.0
    res = ensure_type('a,b,c,d', 'list')
    assert res == ['a', 'b', 'c', 'd']
    res = ensure_type('a,b,c,d', 'pathlist')
    assert res == ['a', 'b', 'c', 'd']



# Generated at 2022-06-12 21:12:21.136762
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    ''' find_ini_config_file should return the last found file '''

    def mock_getenv(varname, default=None):
        if varname == 'ANSIBLE_CONFIG':
            return '/etc/ansible/ansible.cfg'
        return default

    def mock_getcwd():
        return '/tmp'

    def mock_access(path, mode):
        possible = {
            '0': False,
            '2': False,
            '4': False,
            '6': False,
        }
        if 'r' in mode:
            possible['4'] = True
            possible['6'] = True
        if 'w' in mode:
            possible['2'] = True
            possible['6'] = True
        if 'x' in mode:
            possible['1'] = True

# Generated at 2022-06-12 21:12:25.750486
# Unit test for function resolve_path
def test_resolve_path():
    ''' test string input '''
    assert resolve_path(to_text(__file__)) == to_text(__file__)

    ''' test non-string input '''
    assert resolve_path(100) == '100'



# Generated at 2022-06-12 21:12:33.867265
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_manager = ConfigManager()
    config_manager.initialize_plugin_configuration_definitions('SUPER', 'plugin', {'plugin1':
        {'type':'string', 'required':True},
        'plugin2':{'type':'integer', 'required':True},
        'plugin3':{'type':'list', 'required':True},
        })

    defs = config_manager.get_configuration_definitions('SUPER', 'plugin')
    ## check for equality for defs
    assert_equal(defs,
        {'plugin1':
            {'type':'string', 'required':True},
        'plugin2':{'type':'integer', 'required':True},
        'plugin3':{'type':'list', 'required':True},
        })

    # Unit test for method get_

# Generated at 2022-06-12 21:12:39.155595
# Unit test for function resolve_path
def test_resolve_path():
    assert resolve_path('{{CWD}}/foo') == os.getcwd() + '/foo'
    assert resolve_path('/tmp/{{CWD}}/foo') == '/tmp/{{CWD}}/foo'
    with tempfile.NamedTemporaryFile() as tfile:
        fname = tfile.name
    assert resolve_path('~/%s' % fname) == os.path.expanduser('~/%s' % fname)


# FIXME: see if we can unify in module_utils with similar function used by argspec

# Generated at 2022-06-12 21:12:41.140188
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    instance = ConfigManager(None)
    # Assert
    assert False == False

test_ConfigManager_get_configuration_definitions()


# Generated at 2022-06-12 21:12:46.051099
# Unit test for method update_config_data of class ConfigManager
def test_ConfigManager_update_config_data():
    defs = dict()
    defs['FOO'] = dict()
    defs['FOO']['type'] = 'str'
    defs['FOO']['default'] = 'foo'
    defs['FOO']['env'] = [{'name': 'FOO'}]
    cm = ConfigManager()
    cm.update_config_data(defs=defs, configfile='test')
    assert cm.data.FOO == 'foo'
