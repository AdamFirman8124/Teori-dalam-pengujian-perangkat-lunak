

# Generated at 2022-06-12 21:10:41.647629
# Unit test for function ensure_type
def test_ensure_type():
    # Test booleans
    assert True == ensure_type('true', 'bool')
    assert True == ensure_type('t', 'bool')
    assert False == ensure_type('false', 'bool')
    assert False == ensure_type('f', 'bool')
    try:
        assert 'fdsa' == ensure_type('fdsa', 'bool')
    except ValueError:
        pass
    else:
        assert False

    # Test integers
    assert 10 == ensure_type('10', 'int')
    assert 10 == ensure_type(10, 'int')
    try:
        assert -1 == ensure_type('-1', 'int')
    except ValueError:
        pass
    else:
        assert False

    # Test floats

# Generated at 2022-06-12 21:10:44.585736
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    config_manager = ConfigManager() # instantiate class
    # check instance is created
    if not isinstance(config_manager, ConfigManager):
        raise Exception("Cannot create instance of ConfigManager")

    print("Success: instance of ConfigManager created")

    # TODO add test cases


# Generated at 2022-06-12 21:10:47.137443
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():
    plugin_type = 'some_type'
    name = 'some_name'
    defs = {'some_def': True}

    config_manager = ConfigManager()
    config_manager.initialize_plugin_configuration_definitions(plugin_type, name, defs)

    assert config_manager._plugins == {'some_type': {'some_name': {'some_def': True}}}



# Generated at 2022-06-12 21:10:53.387464
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    
    # Fixture to provide test config
    # os.getcwd() returns directory where this file is located
    # ~/projects/ansible/lib/ansible/config/base.yml
    ini_file = os.path.join(os.getcwd(), 'config', 'base.yml')
    config_manager = ConfigManager()
    config_manager._parse_config_file(ini_file)
    
    # Fixture to provide test environment variables
    test_env_vars = {'ANSIBLE_REMOTE_USER': 'guido', 'ANSIBLE_HOSTS': '/path/to/hosts', 'ANSIBLE_FORKS': '4'}

# Generated at 2022-06-12 21:10:58.197765
# Unit test for function ensure_type
def test_ensure_type():
    assert ensure_type("123", 'integer') == 123
    assert ensure_type("123", 'int') == 123
    assert ensure_type("123.012", 'float') == 123.012
    assert ensure_type("True", 'bool') is True
    assert ensure_type("False", 'boolean') is False

    assert ensure_type("a,b,c,d", 'list') == ['a', 'b', 'c', 'd']

    assert ensure_type("/test/path", 'path') == to_text(unf('/test/path'))
    assert ensure_type("/test/path,/another/path", 'pathspec') == [to_text(unf('/test/path')), to_text(unf('/another/path'))]

# Generated at 2022-06-12 21:11:01.183873
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # simulating the cwd path
    cwd = None
    # simulating the env variable
    env = None

    # simulating the env variable with a path
    test_env = '/tmp'
    env = 'ANSIBLE_CONFIG=' + test_env
    cwd = test_env

    assert find_ini_config_file() == '~/.ansible.cfg'
    assert find_ini_config_file(warnings=set()) == '/etc/ansible/ansible.cfg'
    assert find_ini_config_file(warnings=set()) == None



# Generated at 2022-06-12 21:11:07.806451
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    cac = ConfigManager()

# Generated at 2022-06-12 21:11:17.520990
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    import ansible.constants as C
    from ansible.config.manager import ConfigManager

    cfg = ConfigManager(C.ANSIBLE_CONFIG)
    cfg.data.update_setting(Setting('ANSIBLE_NOCOWS', False))

    print("Configuration file: " + cfg._config_file)
    print

    print("Direct calls (section.name)")
    print("-----------------------")
    print

    for option in C.ANSIBLE_CONFIG_DEFAULTS:
        print(option)
        print(cfg.get_config_value_and_origin(option))
        print

    print("Calls for strings (section.name)")
    print("-----------------------")
    print


# Generated at 2022-06-12 21:11:25.633784
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # NOTE: This only tests the 'default' call - no environment variable
    #       is set.

    # Turn off any existing ANSIBLE_CONFIG variable
    if 'ANSIBLE_CONFIG' in os.environ:
        del os.environ['ANSIBLE_CONFIG']

    expected = os.path.join(os.getcwd(), "ansible.cfg")
    assert expected == find_ini_config_file()

    # NOTE: This also tests if the current working directory is world writable.
    #       Files found in those directories are ignored.
    expected = None
    with py3compat.tempfile_mkdtemp() as tmpdir:
        tmpdir_stat = os.stat(to_bytes(tmpdir))
        old_permissions = tmpdir_stat.st_mode

# Generated at 2022-06-12 21:11:33.788261
# Unit test for function ensure_type
def test_ensure_type():
    from ansible.constants import DEFAULTS
    from ansible.defaults import load_default_config
    from ansible.plugins.loader import find_plugin_files, plugin_loaders
    from ansible.parsing.utils.yaml import from_yaml
    import types
    import contextlib
    import textwrap

    # use a fake manager to make all of the plugin paths available
    mgr = plugin_loaders['action'](cls='FakeActionPlugin', subdir=None)

    # use a fake loader, since we don't want to import the actual plugin classes
    mgr.loader = types.ModuleType('loader')
    mgr.loader.find_plugin_files = find_plugin_files

    # gather the lookup plugin paths
    base_paths = set()