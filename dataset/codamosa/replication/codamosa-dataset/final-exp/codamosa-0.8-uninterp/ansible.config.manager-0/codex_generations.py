

# Generated at 2022-06-12 21:11:26.514672
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    import unittest
    import os
    import shutil
    from ansible.config.manager import ConfigManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    class MockOptions(object):
        def __init__(self):
            self.config_file = os.path.join(os.path.dirname(__file__), "test_config_manager.conf")
            self.remote_user = "batman"
            self.ansible_connection = "local"

    class TestConfigManager(unittest.TestCase):
        def setUp(self):
            self.loader = DataLoader()

# Generated at 2022-06-12 21:11:34.884390
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():

    def build_cfile_parser(parser_type, sections, keys, values):
        if parser_type == 'ini':
            parser = configparser.ConfigParser()
            for section in sections:
                parser.add_section(section)
            for key, value in zip(keys, values):
                parser.set(*key, value=value)
            return parser
        else:
            raise TypeError("Unsupported config file type: %s" % parser_type)

    def mock_get_ini_config_value(parser, entry):
        return parser.get(entry['section'], entry['key'])

    def build_env(entries):
        env = {}
        for entry in entries:
            env[entry['name']] = entry['value']
        return env

    def build_vars(values):
        vars = {}

# Generated at 2022-06-12 21:11:37.618354
# Unit test for function get_config_type
def test_get_config_type():
    ftype = get_config_type('/etc/ansible/ansible.cfg')
    assert ftype == 'ini'


# FIXME: see if we end up pulling this into utils/vars

# Generated at 2022-06-12 21:11:44.270454
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    import shutil

    tmp_dir = os.path.realpath(tempfile.mkdtemp())
    ansible_cfg_path = os.path.join(tmp_dir, "ansible.cfg")

# Generated at 2022-06-12 21:11:46.748019
# Unit test for function resolve_path
def test_resolve_path():
    assert resolve_path('.') == os.path.abspath('.')
    assert resolve_path('{{CWD}}') == os.path.abspath(os.curdir)
    assert resolve_path('~/foo') == os.path.expanduser('~/foo')



# Generated at 2022-06-12 21:11:51.277078
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    # This sets up the config manager for testing
    config = ConfigManager(Options())

    # Test for global settings
    config.data.CONFIG_FILE = "test.cfg"
    config.data.DEFAULT_PRIVATE_ROLE_VARS = True
    config.data.DEFAULT_PRIVATE_TASK_VARS = True
    config.data.DEFAULT_PRIVATE_INVENTORY_VARS = True
    config.data.DEFAULT_HOST_LIST = "test_hosts"
    config.data['COW_SELECTION'] = "beavis.zen"
    config.data.HOST_KEY_CHECKING = False
    config.data.DEPRECATED_HOST_KEY_CHECKING = False
    config.data.DEFAULT_MODULE_LANG = "pythonesque"

# Generated at 2022-06-12 21:11:55.680854
# Unit test for method get_plugin_vars of class ConfigManager
def test_ConfigManager_get_plugin_vars():
    from ansible import constants as C
    configfile = '~/.ansible.cfg'
    c = ConfigManager(configfile)
    assert 'sudo_user' in c.get_plugin_vars('connection', 'ssh')
    assert 'sudo_user' in c.get_plugin_vars('connection')
    assert 'sudo_user' in c.get_plugin_vars()
    assert 'ssh_config_file' not in c.get_plugin_vars('connection', 'ssh')
    assert 'ssh_config_file' not in c.get_plugin_vars('connection')
    assert 'ssh_config_file' in c.get_plugin_vars()
    assert 'extras' in c.get_plugin_vars('cache', 'memory')


# Generated at 2022-06-12 21:12:04.118834
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type('/etc/ansible/ansible.cfg') == 'ini'
    assert get_config_type('/etc/ansible/ansible.yaml') == 'yaml'
    assert get_config_type('/etc/ansible/ansible.yml') == 'yaml'
    assert get_config_type('/etc/ansible/ansible.json') == 'yaml'
    assert get_config_type('/etc/ansible/ansible') == 'yaml'
    assert get_config_type(None) is None
    try:
        get_config_type('/etc/ansible/ansible.txt')
    except AnsibleOptionsError as e:
        assert str(e) == "Unsupported configuration file extension for /etc/ansible/ansible.txt: .txt"


# Generated at 2022-06-12 21:12:07.488582
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():
    c = ConfigManager()

    # set base definitions
    c.set_base_defs(KEY_DEFS)
    c.initialize_plugin_configuration_definitions('test', 'test', {'foo': 'bar'})
    c.initialize_plugin_configuration_definitions('test', 'test2', {'foo': 'bar2'})
    assert c._plugins['test']['test']['foo'] == 'bar'
    assert c._plugins['test']['test2']['foo'] == 'bar2'



# Generated at 2022-06-12 21:12:10.709866
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    ''' returns the value of last ini entry found '''
    expected_output = "/etc/ansible/ansible.cfg"
    actual_output = find_ini_config_file()
    assert actual_output == expected_output

