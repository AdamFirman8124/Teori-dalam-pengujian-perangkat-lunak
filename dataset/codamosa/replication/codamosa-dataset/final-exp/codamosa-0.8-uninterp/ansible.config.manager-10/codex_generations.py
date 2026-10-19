

# Generated at 2022-06-12 21:10:54.137839
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_mgr = ConfigManager(data='', script_path='test_path')
    config_mgr.initialize_plugin_configuration_definitions(plugin_type='test_plugin_type', name='test_name', defs='test_defs')
    defs = config_mgr.get_configuration_definitions(plugin_type='test_plugin_type', name='test_name', ignore_private=True)
    assert defs == 'test_defs'


# Generated at 2022-06-12 21:10:58.987018
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    data = '''
    [defaults]
    # this is a comment
    hostfile = /etc/ansible/hosts
    luis = luis
    hola = mundo
    '''

    config_manager = ConfigManager()

    from ansible import constants as C
    config_manager.DEFAULTS = {'hostfile': '/etc/ansible/hosts', 'config_file': '/etc/ansible/ansible.cfg',
                               'roles_path': C.DEFAULT_ROLES_PATH, 'roles_paths': C.DEFAULT_ROLES_PATH, 'types': {}}
    config_manager.config_file = 'ansible.cfg'
    config_manager._parse_config_file(config_manager.config_file, data=data)

    config_manager._base

# Generated at 2022-06-12 21:11:06.826976
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    from ansible.utils.vars import combine_vars
    # Initialize the class
    configMgr = ConfigManager()
    configMgr.set_options()
    configMgr.data.Settings._trusted_hosts = []
    configMgr.data.Settings._vault_password = None
    configMgr.data.Settings._vault_ids = [None]
    configMgr.data.Settings._display = None
    configMgr.data.Settings._deprecation_warnings = None
    # NOTE: This will probably change in the future
    configMgr.data.Settings._ansible_vault_password_file = None
    configMgr.data.Settings._stack_prompt = ''
    configMgr.data.Settings._accelerate_port = None
    configMgr.data.Settings._ac

# Generated at 2022-06-12 21:11:12.340344
# Unit test for function get_config_type
def test_get_config_type():
    # Valid extension
    assert 'ini' == get_config_type('/path/to/file.ini')
    assert 'yaml' == get_config_type('/path/to/file.yaml')

    # Invalid extension
    with pytest.raises(AnsibleOptionsError):
        get_config_type('/path/to/file')
    with pytest.raises(AnsibleOptionsError):
        get_config_type('/path/to/file.txt')



# Generated at 2022-06-12 21:11:21.529718
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    # Test with a 'config' entry that is simply defined in the configuration
    # definitions, and test with a 'config' entry that is also set in a
    # 'direct' dict.
    config_manager = ConfigManager(defs={'foo': {'default': 'bar'}})
    assert ('bar', 'default') == config_manager.get_config_value_and_origin('foo', direct={'foo': 'bar'})
    assert ('bar', 'default') == config_manager.get_config_value_and_origin('foo')
    return
test_ConfigManager_get_config_value_and_origin()


# Generated at 2022-06-12 21:11:30.030918
# Unit test for function resolve_path
def test_resolve_path():
    cwd = os.path.abspath(os.curdir)

# Generated at 2022-06-12 21:11:34.454801
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    some_settings = {}

    # Ensure that we get configuration definitions for all plugins when plugin_type and name are not given
    _m = ConfigManager(defs=some_settings)
    _m.get_configuration_definitions()
    for plugin_type in _m._plugins:
        for name in _m._plugins[plugin_type]:
            _m.get_configuration_definitions(plugin_type, name)


# Generated at 2022-06-12 21:11:42.813567
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def make_module_args(arguments):
        arguments_bytes = {}
        for key, value in arguments.items():
            arguments_bytes[to_bytes(key, errors='surrogate_or_strict')] = value
        return arguments_bytes

    test_config_manager = ConfigManager(None, 'test_config', {}, {}, None)
    default_test_type = make_module_args({'arg1': 'default_type_arg1', 'arg2': 'default_type_arg2'})

# Generated at 2022-06-12 21:11:44.096505
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config = ConfigManager()
    print(config.get_configuration_definitions())


# Generated at 2022-06-12 21:11:49.488978
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # test a bunch of scenarios where a dir is world writable
    # but the ansible.cfg file is not
    # also test scenarios where a dir is not world writable
    # but the ansible.cfg file is world writable
    # also test a bunch of scenarios where a dir is world writable
    # and the ansible.cfg file is world writable

    # The following functions are used in the test below
    # to obtain the permissions of the files and dirs
    # for the tests

    def get_mode(path):
        return os.stat(path).st_mode

    def get_mode_string(path):
        return stat.filemode(get_mode(path))

    def get_mode_octal(path):
        return int(oct(get_mode(path)))

    import shutil
    import tempfile

    #