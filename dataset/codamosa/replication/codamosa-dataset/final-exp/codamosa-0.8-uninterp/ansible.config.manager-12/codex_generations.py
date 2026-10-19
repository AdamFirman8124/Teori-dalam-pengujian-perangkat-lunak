

# Generated at 2022-06-12 21:07:59.630927
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    # configManager = ConfigManager()
    # test_configManager = configManager.get_configuration_definitions()
    pass


# Generated at 2022-06-12 21:08:03.324894
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    '''
    unit test for get_configuration_definitions
    '''
    configmanager = ConfigManager()
    # Test 1
    # test case data
    plugin_type = 'kind' 
    # test expectation
    expected_result = {} 
    # test execution
    result = configmanager.get_configuration_definitions(plugin_type)
    # test result
    assert result == expected_result

# Generated at 2022-06-12 21:08:09.999925
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    """Unit test for find_ini_config_file().
    It is limited, as it's difficult to test environment settings and the like.
    """
    # ansible.cfg in CWD
    # FIXME: can we do something about the warning?
    old_cwd = os.getcwd()
    cwd = tempfile.mkdtemp()
    open(os.path.join(cwd, "ansible.cfg"), "w").close()
    os.chdir(cwd)
    path = find_ini_config_file()
    assert path == os.path.join(cwd, "ansible.cfg")
    os.chdir(old_cwd)
    os.rmdir(cwd)

    # ansible.cfg in ~
    old_home = os.getenv("HOME")
    home = temp

# Generated at 2022-06-12 21:08:19.087791
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_manager = ConfigManager()
    defs = config_manager.get_configuration_definitions()
    assert isinstance(defs, dict)
    assert len(defs) == 18

# Generated at 2022-06-12 21:08:22.401975
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
   c = ConfigManager()
   defs = {'test_key': {'name': 'test_key', 'default': 'test_val', 'type': 'string'}}
   c.update_config_data(defs)
   assert c.get_config_value('test_key') == 'test_val'

# Generated at 2022-06-12 21:08:29.031330
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():
    # ensure that an error is raised for unknown plugin_type
    c = ConfigManager()
    test_name = 'test_initialize_plugin_configuration_definitions'
    test_defs = {
        'test_setting': dict(default='test_value', type='string'),
    }
    c.initialize_plugin_configuration_definitions(test_name, test_name, test_defs)
    assert test_name in c._plugins
    assert test_name in c._plugins[test_name]
    assert test_defs == c._plugins[test_name][test_name]

    # test reset
    c._plugins[test_name][test_name] = {}
    assert test_name in c._plugins
    assert test_name in c._plugins[test_name]

# Generated at 2022-06-12 21:08:37.290243
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    from ansible.utils.vars import merge_hash
    from ansible.cli.arguments import parse_cli_args
    from ansible.errors import AnsibleError
    from ansible.module_utils.common.collections import is_sequence
    from ansible.constants import get_config, load_config_file

    tmp_config = load_config_file()
    args = parse_cli_args()
    defaults = tmp_config.DEFAULTS
    cli_args = tmp_config.parse_cli_vars(args)
    env_args = tmp_config.parse_environment()
    config_file = os.path.expanduser(os.path.expandvars(get_config(cli_args, env_args, os.path.dirname(__file__), args, 'config_file')))
   

# Generated at 2022-06-12 21:08:39.397588
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config_manager = ConfigManager(None)
    result = config_manager.get_configuration_definitions()
    assert isinstance(result, dict) is True

# Generated at 2022-06-12 21:08:49.350530
# Unit test for method get_plugin_vars of class ConfigManager
def test_ConfigManager_get_plugin_vars():

    # ConfigManager unit test mock object
    class ConfigManagerMock(ConfigManager):

        def __init__(self, config_file=None):
            super(ConfigManagerMock, self).__init__(config_file)

    # If the module needs to be mocked, patch here.
    from ansible.module_utils import basic

    # Use AnsibleModule Mocking

    mock_module = basic.AnsibleModuleMock
    def_dict = {
        'plugin_type': {'plugin_type': {'required': True, 'aliases': ['type'], 'type': 'str'}},
        'name': {'name': {'required': True, 'aliases': ['plugin'], 'type': 'str'}}
    }
    name = {'name': 'Cisco'}

# Generated at 2022-06-12 21:08:58.209175
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    with py3compat.TemporaryDirectory() as tmp_dir:
        # Create some fake config files to test with
        tmp_cwd = os.path.join(tmp_dir, "cwd")
        tmp_home = os.path.join(tmp_dir, "home")
        tmp_etc = os.path.join(tmp_dir, "etc")
        tmp_bad_etc = os.path.join(tmp_dir, "bad_etc")  # We'll make it not readable
        tmp_env = os.path.join(tmp_dir, "env")
        tmp_dirs = [tmp_cwd, tmp_home, tmp_etc, tmp_bad_etc, tmp_env]

        for tmp_dir in tmp_dirs:
            os.mkdir(tmp_dir)