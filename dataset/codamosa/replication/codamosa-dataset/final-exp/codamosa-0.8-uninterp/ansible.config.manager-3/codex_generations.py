

# Generated at 2022-06-12 21:11:00.516647
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    import os
    import random
    import sys
    import subprocess
    import shutil
    import tempfile
    import traceback
    import sys

    from ansible import context
    from ansible.cli.arguments import options as cli_args
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    from ansible.utils.path import unfrackpath
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    def set_config(options, section, key, value):
        if not hasattr(options, 'config_file'):
            options.config_file = []
        options.config_file += ['%s:%s=%s' % (section, key, value)]

# Generated at 2022-06-12 21:11:04.979916
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    import tempfile
    import shutil

    def make_ansible_cfg(text, dir="."):
        """ Create an ansible.cfg file with the given content """
        cfg = os.path.join(dir, "ansible.cfg")
        with open(cfg, "w") as f:
            f.write(text)

        return cfg

    def make_executable(path):
        mode = os.stat(path).st_mode
        os.chmod(path, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        return path

    # If we don't have an ANSIBLE_CONFIG, we should see the config in the current working directory
    # even if it's world writable
    curdir = os.getcwd()
    cwd_cfg

# Generated at 2022-06-12 21:11:10.176365
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    runner_mock = Mock()
    runner_mock.omit_queue = False
    config_manager = ConfigManager(runner_mock, 'unittest')
    config_manager.parse()
    cfile = config_manager._config_file
    plugins = config_manager._plugins
    config1 = 'hostfile'
    return_result = config_manager.get_config_value_and_origin(config1, cfile)
    #assert return_result == None, 'Expected return result is None'
    return_result = config_manager.get_config_value_and_origin(config1, cfile, 'runner', 'unittest')
    #assert return_result == None, 'Expected return result is None'
    config1 = 'ANSIBLE_CONFIG'
    return_result = config_manager.get_config

# Generated at 2022-06-12 21:11:19.625937
# Unit test for function resolve_path
def test_resolve_path():
    ''' ansible.module_utils.common.config.resolve_path() units tests'''

    path = '/path/to/file'

    assert resolve_path(path) == path

    # FIXME: This will not be true in all cases, as we don't know what the
    # current working directory is when running these tests.  If we use an
    # absolute path in the test, this will always pass.
    cwd = os.getcwd()
    assert resolve_path(cwd) == cwd

    # This is testing os.path.expandvars() and os.path.expanduser()
    assert resolve_path('~/foo') == os.path.expanduser('~/foo')



# Generated at 2022-06-12 21:11:26.475615
# Unit test for function ensure_type
def test_ensure_type():
    '''
    Function to run make sure that the functionality of ensure_type continues to function
    '''
    # Value is None
    assert None == ensure_type(None, value_type='none')
    assert None == ensure_type(None, value_type='bool')

    # Value is single string
    assert 'str' == ensure_type('str', value_type='str')
    assert u'str' == ensure_type(u'str', value_type='str')
    assert 'str' == ensure_type(u'str', value_type='str')
    assert ['str'] == ensure_type('str', value_type='list')
    assert u'True' == ensure_type('True', value_type='str')
    assert 'True' == ensure_type(u'True', value_type='str')
    assert True == ensure

# Generated at 2022-06-12 21:11:29.672984
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    # No instance created test
    _ConfigManager.get_configuration_definitions()

    # Instance created but no data test
    _ConfigManager.get_configuration_definitions


# Generated at 2022-06-12 21:11:37.586404
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type("/etc/ansible/ansible.cfg") == "ini"
    assert get_config_type("/usr/local/etc/ansible/ansible.yml") == "yaml"
    assert get_config_type("/etc/ansible/roles/foobar/vars/main.yml") == "yaml"
    assert get_config_type("/etc/ansible/roles/foobar/vars/main.ini") == "ini"
    assert get_config_type("/etc/ansible/roles/foobar/vars/main.cfg") == "ini"
    assert get_config_type("/etc/ansible/ansible.yaml") == "yaml"

# Generated at 2022-06-12 21:11:39.477934
# Unit test for method get_config_value of class ConfigManager
def test_ConfigManager_get_config_value():
    config = ConfigManager()
    config.set_config_file('')
    config.parse()

    # TODO: Add unit test here
# End of unit test

# Generated at 2022-06-12 21:11:45.932165
# Unit test for function ensure_type
def test_ensure_type():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.path import makedirs_safe, unfrackpath, resolve_path

# Generated at 2022-06-12 21:11:50.461526
# Unit test for method update_config_data of class ConfigManager
def test_ConfigManager_update_config_data():
    mock_config_defs = dict()
    mock_config_defs['CONFIG_FILE'] = {'default': 'ansible.cfg', 'type': 'string'}
    mock_config_defs['DEFAULT_REMOTE_PORT'] = {'default': '22', 'type': 'int'}
    mock_config_defs['HOST_KEY_CHECKING'] = {'default': 'True', 'type': 'bool'}
    config_manager = ConfigManager([], mock_config_defs)
    config_manager.update_config_data()
    assert config_manager.data['CONFIG_FILE'].value == 'ansible.cfg'
    assert config_manager.data['CONFIG_FILE'].origin == 'default'
    assert config_manager.data['CONFIG_FILE'].type == 'string'
