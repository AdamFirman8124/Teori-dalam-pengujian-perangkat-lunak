

# Generated at 2022-06-12 21:12:58.315566
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    import tempfile
    import os
    import shutil
    import stat

    current_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)
    open('ansible.cfg', 'a').close()
    assert find_ini_config_file() == to_text(os.path.join(temp_dir, 'ansible.cfg'))
    assert not find_ini_config_file(warnings=set())

    # Modify perms of ansible.cfg to test warnings
    os.chmod(os.path.join(temp_dir, 'ansible.cfg'), stat.S_IWOTH)

    # Now test with warnings
    assert find_ini_config_file(warnings=set()) == None

    # Clean up after yourself

# Generated at 2022-06-12 21:13:07.223344
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    """The only way to test this function is to mock the config file in CWD and make the CWD world writable.
    The function should NOT find the config file and return None.
    """
    import pytest

    # create a temp dir
    temp_dir = tempfile.mkdtemp(prefix='tmp_ansible_test_find_ini_config_file')

# Generated at 2022-06-12 21:13:13.925887
# Unit test for function get_config_type
def test_get_config_type():
    '''
    get_config_type return the filetype of the configuration file with the provided extension
    '''
    assert get_config_type('/etc/ansible/ansible.cfg') == 'ini'
    assert get_config_type('/etc/ansible/ansible.yml') == 'yaml'
    assert get_config_type('/etc/ansible/ansible.yaml') == 'yaml'
    assert get_config_type('/etc/ansible/ansible.ini') == 'ini'


# Generated at 2022-06-12 21:13:16.363056
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    with pytest.raises(AnsibleOptionsError):
        get_config_type(find_ini_config_file())


# Generated at 2022-06-12 21:13:19.073850
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.config.settings.config_manager import ConfigManager
    from ansible.config.settings.constants import (DEFAULTS,
                                                   ConfigurationError)

    for config in DEFAULTS:
        ConfigManager(config, _config_file=None)
        assert True

# Generated at 2022-06-12 21:13:23.921309
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.config.manager import ConfigManager
    from ansible.config.data import ConfigData
    from ansible.config.setting import Setting

    cfg = ConfigManager()
    cfg.data = ConfigData()

    cfg._config_file = 'test_defaults'
    cfg.get_config_value_and_origin('units')
    assert cfg.data.units == 's'

    cfg.data = ConfigData()
    arg = {'units': 'm'}
    cfg.get_config_value_and_origin('units', direct=arg)
    assert cfg.data.units == 'm'

    cfg.data = ConfigData()
    arg = {'units': 'm'}
    cfg.get_config_value_and_origin('units', direct=arg)

# Generated at 2022-06-12 21:13:26.084431
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    # Testing a non existent file
    fd, fd_path = tempfile.mkstemp(prefix='ansible-test-config-')
    config_manager = ConfigManager(fd_path)
    #No option defined
    assert(config_manager.get_config_value('ANSIBLE_REMOTE_USER') == 'root')


# Generated at 2022-06-12 21:13:28.031363
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    origin = None
    configmanager = ConfigManager()
    configmanager._config_file = None
    configmanager.get_config_value_and_origin(config = 'DEFAULT_LOG_PATH',cfile = configmanager._config_file)
test_ConfigManager_get_config_value_and_origin()

# Generated at 2022-06-12 21:13:29.602532
# Unit test for function resolve_path
def test_resolve_path():
    assert resolve_path('/home/user') == '/home/user'
    assert resolve_path(None) is None



# Generated at 2022-06-12 21:13:32.634739
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.config.manager import ConfigManager
    configmanager = ConfigManager()

    # normal case
    value, origin = configmanager.get_config_value_and_origin('config_file')
    assert 'default' == origin
    # test if case don't exist
    configmanager.set_config_file("/tmp/notexist.cfg")
    value, origin = configmanager.get_config_value_and_origin('config_file','/tmp/notexist.cfg')
    assert 'default' == origin
