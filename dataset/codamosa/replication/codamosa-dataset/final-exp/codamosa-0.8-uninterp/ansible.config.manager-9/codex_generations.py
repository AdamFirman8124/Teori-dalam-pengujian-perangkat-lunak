

# Generated at 2022-06-12 21:12:18.262137
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():

    cm = ConfigManager()
    cm._config_file = '/etc/ansible/ansible.cfg'
    cm.DATA = {
        'ANSIBLE_CONFIG': '/path/to/ansible.cfg',
        'ANSIBLE_FOO': 'FOO',
        'PATH': '/bin:/usr/bin'
    }
    cm._parsers = {
        '/etc/ansible/ansible.cfg': {
            ('section', 'key'): ('value', 'file'),
            ('section2', 'key2'): ('value2', 'file2')
        },
        '/path/to/ansible.cfg': {},
    }

# Generated at 2022-06-12 21:12:19.935419
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():
    '''
    Unit test for the method initialize_plugin_configuration_definitions of class ConfigManager
    '''
    # create a ConfigManager object with fake data
    # FIXME: write test
    return

# Generated at 2022-06-12 21:12:22.430759
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    fixture = ConfigManager()
    fixture.update_config_data(fixture._base_defs)
    # test expected return value
    assert fixture.get_config_value_and_origin('DEFAULT_MODULE_NAME') == (default_module_name, 'default')


# Generated at 2022-06-12 21:12:28.517723
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    config_manager = ConfigManager()
    config_manager.initialize_plugin_configuration_definitions(plugin_type=None, name=None, defs=INTERNAL_DEFS.get(None))
    assert config_manager.get_config_value_and_origin(config=config, cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None) == ("default", "default") 


# Generated at 2022-06-12 21:12:36.446765
# Unit test for function resolve_path
def test_resolve_path():
    '''
    Test cases for function resolve_path

    :return: return true when all test cases passed
    '''
    assert resolve_path('') == ''
    assert resolve_path('.') == '.'
    assert resolve_path('..') == '..'
    assert resolve_path('/etc/sudoers') == '/etc/sudoers'
    assert resolve_path('/etc/../etc/sudoers') == '/etc/sudoers'
    assert resolve_path('/etc/../../../../etc/sudoers') == '/etc/sudoers'
    assert resolve_path('/etc/../../../etc/./sudoers') == '/etc/sudoers'
    assert resolve_path('~') == os.path.expanduser('~')
    assert resolve_path('~root') == '/root'
    assert resolve_path

# Generated at 2022-06-12 21:12:42.640792
# Unit test for function get_config_type
def test_get_config_type():
    ftype1 = get_config_type('/root/ansible/lib/ansible/module_utils/basic.py')
    ftype2 = get_config_type('/root/.ansible.cfg')
    ftype3 = get_config_type('/root/.ansible.yml')
    assert ftype1 is None
    assert ftype2 == 'ini'
    assert ftype3 == 'yaml'
    try:
        ftype4 = get_config_type('/root/ansible/test')
        assert False
    except AnsibleOptionsError as e:
        assert e.message == "Unsupported configuration file extension for /root/ansible/test: "



# Generated at 2022-06-12 21:12:50.453590
# Unit test for function get_config_type
def test_get_config_type():
    ftype = get_config_type('/path/to/ini/file.ini')
    assert ftype == 'ini'
    ftype = get_config_type('/path/to/yaml/file.yaml')
    assert ftype == 'yaml'
    try:
        ftype = get_config_type('/path/to/other/file.txt')
        assert False
    except AnsibleOptionsError as e:
        assert "Unsupported configuration file extension for /path/to/other/file.txt" in to_text(e)

    # Invalid path

# Generated at 2022-06-12 21:12:58.814749
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    plugin_defs = {'foo': {'default': None, 'env': [{'name': 'ANSIBLE_FOO'}]},
                   'bar': {'default': None, 'env': [{'name': 'ANSIBLE_BAR'}]},
                   'baz': {'default': None, 'env': [{'name': 'ANSIBLE_BAZ'}]},
                   'qux': {'default': None, 'env': [{'name': 'ANSIBLE_QUX'}]}}


# Generated at 2022-06-12 21:13:07.858014
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    # ConfigManager, ConfigManager.get_config_value
    cfg = ConfigManager()


# Generated at 2022-06-12 21:13:17.445885
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    '''
    get_config_value is the real work horse of the configuration module.
    We test it under all conditions that are known to us.
    '''
    # Unfortunately, there are a lot of conditions, and we're merely testing
    # this for the default ANSIBLE_* configuration, not any other configuration
    # that plugins or even modules might use.
    from ansible import constants as C
    from ansible.utils import context_objects as co

    cm = ConfigManager()

    # test the basic structure of the configuration
    assert isinstance(cm.configuration_definitions, dict)
    assert isinstance(cm._parsers, dict)

    # test that configuration_definitions is a copy and not a reference,
    # so we can change it without mutating the singleton