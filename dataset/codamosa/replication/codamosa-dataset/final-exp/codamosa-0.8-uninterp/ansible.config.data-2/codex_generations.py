

# Generated at 2022-06-12 20:53:28.927615
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    ConfigData = ConfigData()
    ConfigData.get_setting(name='blabla', plugin=None)



# Generated at 2022-06-12 20:53:39.224418
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    global_setting = {'name': 'new_global_setting', 'value': 'global_value'}
    setting = {'name': 'new_setting', 'value': 'value'}

    # Setting is global
    config_data = ConfigData()
    config_data.update_setting(global_setting)
    assert config_data._global_settings['new_global_setting'] == global_setting

    # Setting is not global, update does not exist
    config_data = ConfigData()
    plugin = {'type': 'action', 'name': 'shell'}
    config_data.update_setting(setting, plugin)
    assert config_data._plugins['action']['shell']['new_setting'] == setting

    # Setting is not global, update exists
    config_data = ConfigData()

# Generated at 2022-06-12 20:53:48.769956
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import PluginLoader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    collection_dir = AnsibleCollectionLoader().collections_paths[0]
    collection_path = collection_dir + '/my_collection/my_collection.collection.yml'
    collection_loader = AnsibleCollectionLoader()
    collections = collection_loader.load(collection_path)

    plugin_data = ConfigData()

    plugin_loader = PluginLoader(all_plugins=True)

    base_plugin = plugin_loader.get('test_plugin')
    collection_test_plugin = plugin_loader.get('test_plugin', collections)

    plugin_data.update_setting(base_plugin.get_option('my_test_option'))

# Generated at 2022-06-12 20:53:51.596266
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    setting = Setting()
    plugin = Plugin(type="lookup", name="myplugin")
    data.update_setting(setting, plugin)


# Generated at 2022-06-12 20:53:58.156414
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()

    # Global setting
    setting = Setting(name='debug', namespace=None, plugin=None)
    config.update_setting(setting, plugin=None)
    settings = config.get_settings(plugin=None)
    assert len(settings) == 1
    assert settings[0] == setting

    # Plugin setting
    plugin = Plugin(name='test', type='test')
    setting = Setting(name='debug', namespace=None, plugin=plugin)
    config.update_setting(setting, plugin=plugin)
    settings = config.get_settings(plugin=plugin)
    assert len(settings) == 1
    assert settings[0] == setting


# Generated at 2022-06-12 20:54:00.978449
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('unexistent') is None


# Generated at 2022-06-12 20:54:03.264015
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    assert cd.get_setting("FOO") is None


# Generated at 2022-06-12 20:54:11.249750
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_test_values = {
        'ANSIBLE_CONFIG': 'ansible.cfg',
        'ANSIBLE_DEBUG': True,
        'ANSIBLE_HOST_KEY_CHECKING': True,
        'ANSIBLE_PRIVATE_KEY_FILE': 'private_key',
        'DEFAULT_UNDEFINED_VAR_BEHAVIOR': 'strict'
    }

    data = ConfigData()

    for (name, value) in global_test_values.items():
        data.update_setting(Setting(name, value))

    for (name, value) in global_test_values.items():
        assert data.get_setting(name).value == value

    assert data.get_setting('ANSIBLE_CONFIG').value == 'ansible.cfg'

# Generated at 2022-06-12 20:54:20.845177
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import pytest

    # Test: Create config data with a few settings
    cd = ConfigData()
    cd.update_setting(Setting(name='settings_test'))
    cd.update_setting(Setting(name='settings_test2'))
    cd.update_setting(Setting(name='settings_default_settings'))
    cd.update_setting(Setting(name='settings_test_plugin', plugin=Plugin()))

    # Test: Get all settings
    settings = cd.get_settings()

    assert len(settings) == 3
    assert settings[0].name == 'settings_test'
    assert settings[1].name == 'settings_test2'
    assert settings[2].name == 'settings_default_settings'

    # Test: Get all settings for a plugin
    settings = cd.get_settings(Plugin())

    assert len

# Generated at 2022-06-12 20:54:27.585721
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    print('Test update_setting of class ConfigData')
    config = ConfigData()
    import re
    setting = Setting('roles_path', '/etc/ansible/roles', '/etc/ansible/roles:/home/foo/bar', bool(re.compile(r"^.+(:.+)?$").match('/etc/ansible/roles:/home/foo/bar')), 'roles_path')
    config.update_setting(setting)
    print(config._global_settings)


# Generated at 2022-06-12 20:54:43.301932
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    plugin_type = 'test'
    plugin_name = 'test_plugin'
    setting_name = 'test_setting'
    setting_value = 'setting_value'

    plugin = Plugin(plugin_type, plugin_name)
    setting = Setting(setting_name, setting_value, plugin)

    # check that the plugin is not defined yet, as well as the setting
    assert config_data.get_settings(plugin) == []
    assert config_data.get_settings() == []
    
    # update the config_data with the setting
    config_data.update_setting(setting, plugin)
    assert config_data.get_settings(plugin) == [setting]

    # define a setting for the global scope
    setting = Setting(setting_name, setting_value)

# Generated at 2022-06-12 20:54:44.913127
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    assert 0 == len(config.get_settings())

# Generated at 2022-06-12 20:54:51.026219
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config = ConfigSetting(name='default_vars', value='roles/vars')
    plugin = Plugin(name='inventory', type='inventory')
    config_data.update_setting(config)
    config_data.update_setting(config, plugin)
    assert config_data.get_setting('default_vars') == config
    assert config_data.get_setting('default_vars', plugin) == config


# Generated at 2022-06-12 20:55:01.731082
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    global_setting = ConfigValue(name='global')
    plugin_type = Plugin(name='plugin_type')
    plugin_name = Plugin(plugin_type, name='plugin_name')
    config_data.update_setting(global_setting)
    config_data.update_setting(global_setting, plugin_type)
    config_data.update_setting(global_setting, plugin_name)
    assert len(config_data._global_settings) == 1 and global_setting in config_data._global_settings.values()
    assert len(config_data._plugins) == 1 and plugin_type.name in config_data._plugins and len(config_data._plugins[plugin_type.name]) == 1

# Generated at 2022-06-12 20:55:12.414722
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = _ConfigData()
    setting = _Setting()
    setting.name = "setting"
    setting.value = "value"
    setting_plugin = _SettingPlugin()
    setting_plugin.type = "C"
    setting_plugin.name = "python"

    config_data.update_setting(setting)
    assert config_data._global_settings[setting.name].value == setting.value
    assert len(config_data._plugins) == 0

    config_data.update_setting(setting, plugin=setting_plugin)
    assert config_data._plugins[setting_plugin.type][setting_plugin.name][setting.name].value == setting.value
    assert len(config_data._plugins[setting_plugin.type][setting_plugin.name]) == 1



# Generated at 2022-06-12 20:55:18.477063
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    from importlib import import_module

    item_module = import_module(name='lib.galaxy.api.models.item')
    item1 = item_module.Item(name="item1", version="1.0.0", path="path1", content_type="plugin", tags=["tag1"])
    setting_module = import_module(name='lib.galaxy.api.models.setting')
    setting1 = setting_module.Setting(name="setting1", value="value1", section="section1", description="desc1")
    setting2 = setting_module.Setting(name="setting2", value="value2", section="section2", description="desc2")
    config_data.update_setting(setting1, item1)
    config_data.update_setting(setting2, item1)

# Generated at 2022-06-12 20:55:26.414970
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.module_utils.ansible_release import __version__ as RELEASE
    from ansible.module_utils.common.version import __version__ as VERSION

    config_data = ConfigData()

    config_data.update_setting(Setting('ansible_version', VERSION))
    config_data.update_setting(Setting('release', RELEASE))

    settings = config_data.get_settings()

    assert settings[0].name == 'ansible_version'
    assert settings[0].value == VERSION

    assert settings[1].name == 'release'
    assert settings[1].value == RELEASE

    assert len(settings) == 2


# Generated at 2022-06-12 20:55:31.341690
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    config_data.update_setting(Setting('temp', 'ansible.cfg'))
    assert config_data.get_setting('temp') == Setting('temp', 'ansible.cfg')


# Generated at 2022-06-12 20:55:36.901486
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible_galaxy.models.config_data import ConfigData
    from ansible_galaxy.models.setting import Setting
    Config_data=ConfigData()
    name='galaxy_server'
    plugin=None
    setting=Setting(name, 'https://galaxy.ansible.com/api/', 0)
    Config_data.update_setting(setting,plugin)
    assert Config_data.get_setting(name,plugin).value=='https://galaxy.ansible.com/api/'


# Generated at 2022-06-12 20:55:46.486968
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping

    assert True
    cd = ConfigData()
    setting1 = SettingData(name="display", value="True", plugin=None)
    cd.update_setting(setting1)
    setting2 = SettingData(name="timeout", value="10", plugin=None)
    cd.update_setting(setting2)
    setting3 = SettingData(name="host", value="localhost", plugin=None)
    cd.update_setting(setting3)
    assert isinstance(cd, ConfigData)
    assert isinstance(cd.get_settings(), list)
    assert len(cd.get_settings()) == 3
    for setting in cd.get_settings():
        assert isinstance(setting, SettingData)

# Generated at 2022-06-12 20:56:05.888999
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Create ConfigData object
    config_data = ConfigData()

    # Create new setting
    from ansible.module_utils.config_data import Setting
    setting = Setting()
    setting.name = 'foo'
    setting.value = 'bar'
    setting.origin = 'test'

    # Test get_setting with empty config
    assert config_data.get_setting('foo') is None

    # Test get_setting with global setting
    config_data.update_setting(setting)
    assert config_data.get_setting('foo') is setting

    # Test get_setting with global and plugin setting
    from ansible.module_utils.config_data import Plugin
    plugin = Plugin('foo', 'amazon')
    plugin_setting = Setting()
    plugin_setting.name = 'baz'

# Generated at 2022-06-12 20:56:08.435682
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()

    setting = Setting('type', 'name', None, None, None, None, None, 'default')
    config.update_setting(setting)


# Generated at 2022-06-12 20:56:10.668352
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert [] == cd.get_settings()


# Generated at 2022-06-12 20:56:22.415573
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    data = ConfigData()

    setting1 = Setting('setting1', 'setting1', 'setting1 value')
    data.update_setting(setting1)
    setting2 = Setting('setting2', 'setting2', 'setting2 value')
    plugin = Plugin('plugin')
    data.update_setting(setting2, plugin)
    setting3 = Setting('setting3', 'setting3', 'setting3 value')
    data.update_setting(setting3, plugin)

    settings = data.get_settings()
    assert len(settings) == 1

    settings = data.get_settings(plugin)
    assert len(settings) == 2

    setting4 = Setting('setting4', 'setting4', 'setting4 value')
    data.update_setting(setting4, plugin)
    settings = data.get_settings(plugin)
    assert len(settings)

# Generated at 2022-06-12 20:56:32.485184
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    settings_file = """
    [defaults]
    callback_whitelist =
    console_callback = default
    default_callback = default
    display_skipped_hosts = True
    host_key_checking = False
    inventory = /home/ansible/inventory
    retry_files_enabled = False
    stdout_callback = default
    """

    config_data = ConfigData()

    with open('/tmp/settings.cfg', 'w') as file:
        file.write(settings_file)

    from ansible.parsing.config.loader import ConfigLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    var_manager = VariableManager()
    loader = DataLoader()
   

# Generated at 2022-06-12 20:56:43.081850
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    _global_settings = [
        {'name': 'my_global_setting', 'value': 'i am a global setting'},
        {'name': 'my_global_setting2', 'value': 'i am a global setting2'},
    ]

    _plugin_settings = [
        {
            'plugin': {'type': 'action', 'name': 'Copy'},
            'settings': [
                {'name': 'my_action_setting', 'value': 'i am an action setting'},
            ]
        },
        {
            'plugin': {'type': 'connection', 'name': 'Local'},
            'settings': [
                {'name': 'my_connection_setting', 'value': 'i am a connection setting'},
            ]
        },
    ]

    cd = ConfigData()


# Generated at 2022-06-12 20:56:51.471158
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings() == []
    assert cd.get_settings(None) == []
    assert cd.get_settings(object()) == []

    # Test plugin type
    plugin = object()
    plugin.type = 'core'

    # Test plugin name
    plugin.name = 'test_plugin'

    # Test setting
    setting = object()
    setting.name = 'test_setting'

    cd.update_setting(setting, plugin)
    settings = cd.get_settings(plugin)

    assert len(settings) == 1
    assert settings[0] == setting



# Generated at 2022-06-12 20:56:58.227166
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Arrange

    # Act
    config = ConfigData()
    config_data = dict()
    config_data['settings'] = dict()
    config_data['settings']['short_option_name'] = {
        'n': {
            'section': 'global',
            'key': None,
            'value': 'test_data'
        }
    }
    config_data['settings']['long_option_name'] = {
        'name': {
            'section': 'test_section',
            'key': 'test_key',
            'value': 'test_value'
        }
    }


# Generated at 2022-06-12 20:57:07.810186
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting("setting1", "plugin1")
    config_data.update_setting("setting2", "plugin2")
    config_data.update_setting("setting3", "plugin3")
    config_data.update_setting("settings1", "plugin1")
    config_data.update_setting("settings2", "plugin2")
    config_data.update_setting("settings3", "plugin3")
    assert config_data.get_setting("setting1") == "plugin1"
    assert config_data.get_setting("setting2") == "plugin2"
    assert config_data.get_setting("setting3") == "plugin3"
    assert config_data.get_setting("settings1") == "plugin1"

# Generated at 2022-06-12 20:57:17.193458
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import find_plugin

    config_data = ConfigData()

    plugin = find_plugin('action')
    assert config_data.get_settings(plugin) == []

    # Test filtering of settings
    config_data.update_setting(Setting('abc', 'abc value'))
    config_data.update_setting(Setting('abc2', 'abc2 value'))
    config_data.update_setting(Setting('abc2', 'abc2 value', plugin=plugin))
    config_data.update_setting(Setting('abc3', 'abc3 value', plugin=plugin))
    config_data.update_setting(Setting('abc4', 'abc4 value'))

    settings = config_data.get_settings(plugin)
    assert len(settings) == 2
    assert settings[0].name == 'abc2'


# Generated at 2022-06-12 20:57:40.550897
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='default_locale', value='french', plugin=None))
    assert len(config_data.get_settings()) == 1
    config_data.update_setting(Setting(name='default_locale', value='french', plugin=Plugin('inventory', 'test')))
    assert len(config_data.get_settings()) == 2
    config_data.update_setting(Setting(name='default_locale', value='french', plugin=Plugin('inventory', 'test')))
    assert len(config_data.get_settings()) == 2
    assert len(config_data.get_settings(plugin=Plugin('inventory', 'test'))) == 1



# Generated at 2022-06-12 20:57:45.192672
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    plugin = ConfigPlugin(type='inventory', name='my_plugin')
    setting = ConfigSetting(name='my_setting')

    data.update_setting(setting, plugin)

    settings = data.get_settings(plugin)

    assert len(settings) == 1
    assert settings[0] == setting

# Generated at 2022-06-12 20:57:51.418390
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin1 = PluginDefinition('ansible', 'network', 'ios', 'default')
    plugin2 = PluginDefinition('ansible', 'network', 'ios', 'ios1')
    setting1 = SettingDefinition('timeout', '30', 'How long should we wait?')
    setting2 = SettingDefinition('timeout', '40', 'How long should we wait?')

    config_data.update_setting(setting1, plugin1)
    config_data.update_setting(setting2, plugin2)

    assert len(config_data._global_settings) == 0
    assert len(config_data._plugins) == 2
    assert len(config_data._plugins['network']['ios']['default']) == 1

# Generated at 2022-06-12 20:57:59.288574
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('enforce_serial', False))
    config_data.update_setting(Setting('enforce_serial', False, PluginSpec('action_plugin', 'add_host')))

    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'enforce_serial'

    settings = config_data.get_settings(plugin=PluginSpec('action_plugin', 'add_host'))
    assert len(settings) == 1
    assert settings[0].name == 'enforce_serial'


# Generated at 2022-06-12 20:58:03.969944
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = Setting('verbosity', 'int', '2', None)
    config_data.update_setting(setting)
    assert config_data.get_settings() == [setting]


# Generated at 2022-06-12 20:58:04.875758
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0


# Generated at 2022-06-12 20:58:06.412732
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0


# Generated at 2022-06-12 20:58:11.205455
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    # test empty config data
    assert config_data.get_settings() == []

    # test update config data by global setting
    setting_1 = Setting('setting_1', 'setting_1_value')
    config_data.update_setting(setting_1)
    assert config_data.get_settings() == [setting_1]

    # test update config data by plugin setting
    plugin_1 = Plugin('plugin_1', 'plugin_type_1')
    config_data.update_setting(Setting('setting_1', 'setting_1_value'), plugin_1)
    assert config_data.get_settings(plugin_1) == [Setting('setting_1', 'setting_1_value')]
    assert config_data.get_settings() == [setting_1]

    # test update config data

# Generated at 2022-06-12 20:58:17.116134
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert len(config_data._global_settings) == 0
    setting = ConfigSetting('color', 'blue')
    config_data.update_setting(setting)
    assert len(config_data._global_settings) == 1
    assert config_data._global_settings.get('color').name == 'color'
    assert config_data._global_settings.get('color').value == 'blue'
    assert config_data.get_setting('color') is not None



# Generated at 2022-06-12 20:58:28.987655
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    
    from ansible.plugins.loader import find_plugin_file
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    import ansible.plugins.loader as p
    import ansible.plugins.action
    import ansible.plugins.callback
    import ansible.plugins.connection
    import ansible.plugins.filter as filters
    import ansible.plugins.module_utils
    import ansible.plugins.strategy
    import ansible.plugins.shell
    import os

    # Prepare configData
    configData = ConfigData()

    # Prepare play_context
    play_context = PlayContext()
    play_context.network_os = 'iosxr'
    play_context.become = False
    play_context.become

# Generated at 2022-06-12 20:59:10.270715
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    print(cd._global_settings)
    assert isinstance(cd._global_settings, dict)
    print(cd._plugins)
    assert isinstance(cd._plugins, dict)
    cd.update_setting('abc')
    print(cd._global_settings)
    cd.update_setting(plugin='xyz')
    print(cd._plugins)

# Generated at 2022-06-12 20:59:18.667918
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    # test case where setting is not specified
    assert config.get_setting("host_key_checking") is None

    # test case where setting is specified on global level
    global_setting = Setting("host_key_checking", "true", Plugin.global_plugin())
    config.update_setting(global_setting)
    assert config.get_setting("host_key_checking") == global_setting

    # test case where setting is specified on plugin level
    plugin_setting = Setting("host_key_checking", "false", Plugin.new_plugin("connection", "ssh"))
    config.update_setting(plugin_setting)
    assert config.get_setting("host_key_checking", plugin_setting.plugin) == plugin_setting
    assert config.get_setting("host_key_checking").plugin == Plugin.global_plugin()

# Generated at 2022-06-12 20:59:28.694466
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class test_setting:
        def __init__(self, name, value, origin):
            self.name = name
            self.value = value
            self.origin = origin

    config_data = ConfigData()

    plugin1 = test_plugin('plugin1', 'test')
    plugin2 = test_plugin('plugin2', 'test')
    plugin3 = test_plugin('plugin3', 'test')


# Generated at 2022-06-12 20:59:37.393553
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name
    plugin_1 = Plugin("dynamic", "netconf")
    plugin_2 = Plugin("dynamic", "redfish")
    plugin_3 = Plugin("connection", "network_cli")
    plugin_4 = Plugin("connection", "netconf")

    class Setting:
        def __init__(self, name):
            self.name = name
    setting_1 = Setting("module_defaults")
    setting_2 = Setting("connection_defaults")
    setting_3 = Setting("persistent_connection")
    setting_4 = Setting("http_socket_timeout")
    setting_5 = Setting("host")


# Generated at 2022-06-12 20:59:48.495238
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.module_utils.common._collections_compat import MutableMapping
    import pytest

    @pytest.fixture
    def config_data():
        config_data = ConfigData()
        return config_data

    @pytest.fixture
    def request_patch(mocker):
        request_patch = mocker.patch("ansible.plugins.action.ActionBase.request_module")
        return request_patch

    @pytest.fixture
    def empty_config():
        return {'module_defaults': {},
                'shell_defaults': {},
                'strategy_defaults': {},
                'lookup_defaults': {},
                'inventory_defaults': {},
                'connection_defaults': {}}


# Generated at 2022-06-12 20:59:51.693496
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting('setting1')
    assert config_data.get_setting('setting1') == 'setting1'


# Generated at 2022-06-12 21:00:02.069739
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    # Create a dummy setting
    def make_setting(name):
        setting = Setting()
        setting.name = name
        return setting
    dummy_setting1 = make_setting('dummy_setting1')
    dummy_setting2 = make_setting('dummy_setting2')
    dummy_setting3 = make_setting('dummy_setting3')

    # Create a dummy plugin
    def make_plugin(name, type):
        plugin = Plugin()
        plugin.name = name
        plugin.type = type
        return plugin
    dummy_plugin1 = make_plugin('dummy_plugin1', 'shell')
    dummy_plugin2 = make_plugin('dummy_plugin2', 'python')

    # Create a dummy config data object
    config_data = ConfigData()

    # Assign a global setting
    config_data.update_

# Generated at 2022-06-12 21:00:06.276711
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting('test_setting_0', plugin=None)
    cd.update_setting('test_setting_1', plugin=None)
    cd.update_setting('test_setting_2', plugin=None)
    assert cd.get_settings() == ["test_setting_0", "test_setting_1", "test_setting_2"]

# Generated at 2022-06-12 21:00:15.719109
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.plugins import get_all_plugin_loaders
    from ansible.plugins.loader import PluginLoader

    assert config_data.get_setting('gsetting') is None
    assert config_data.get_setting('setting') is None
    assert config_data.get_setting('setting', PluginLoader('connection', 'local', 'units.mock.plugins', None)) is None
    assert config_data.get_setting('setting', PluginLoader('modules', 'debug', 'units.mock.plugins', None)) is None
    assert config_data.get_setting('setting', PluginLoader('callback', 'default', 'units.mock.plugins', None)) is None

# Generated at 2022-06-12 21:00:24.447972
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = ConfigDataSetting("http_port","8080")
    setting2 = ConfigDataSetting("http_port","8081")
    plugin = Plugin("test_plugin","test_plugin")
    config_data.update_setting(setting1)
    config_data.update_setting(setting2,plugin)
    assert config_data.get_settings()[0].get_value() == "8080"
    assert config_data.get_settings(plugin)[0].get_value() == "8081"



# Generated at 2022-06-12 21:01:09.597798
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import PluginLoader
    import ansible.config.constants as C
    from ansible.config.data import ConfigData

    config = ConfigData()

    # Create new dictionary that contains all the setting names as keys
    def setting_dict():
        settings = {}
        for plugin_type in C.PLUGIN_PATH_CACHE:
            plugins = PluginLoader(config=config, plugin_type=plugin_type, namespaces=C.PLUGIN_PATH_CACHE[plugin_type]).all()
            for plugin in plugins:
                setting_names = [s.name for s in plugin.get_settings()]
                settings.update(dict.fromkeys(setting_names, None))

        return settings

    assert config.get_settings() == []

    # Create a setting name and create a Setting object


# Generated at 2022-06-12 21:01:16.158518
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    setting = Setting(name='some_name', value='some_value')
    configdata.update_setting(setting)
    settings = configdata.get_settings()
    assert len(settings) is 1
    assert settings[0].name is 'some_name'
    assert settings[0].value is 'some_value'



# Generated at 2022-06-12 21:01:18.383115
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('test', 'test') is None


# Generated at 2022-06-12 21:01:21.543333
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    config.update_setting(Setting(name='setting_1'))
    setting = config.get_setting('setting_1')
    assert setting.name == 'setting_1'


# Generated at 2022-06-12 21:01:31.042593
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
	global_settings = ConfigData()
	global_settings.update_setting(Config('CACHE_SIZE', '10', 'none', 'none', 'none'))
	assert global_settings.get_setting('CACHE_SIZE') is not None, 'test_ConfigData_get_setting failed, get_setting() unexpected None.'
	assert global_settings.get_setting('CACHE_SIZE').name == 'CACHE_SIZE', 'test_ConfigData_get_setting failed, CACHE_SIZE not found.'

	plugin = Plugin('vault', 'password')
	global_settings.update_setting(Config('CONSUL_HOST', 'localhost', 'none', 'vault', 'password'))

# Generated at 2022-06-12 21:01:40.245309
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    # test config_data.get_setting method
    assert config_data.get_setting("ANSI_COLOR", "shell") == None

    # test global config setting
    global_setting = {"name": "ANSI_COLOR", "value": "True"}
    config_data._global_settings["ANSI_COLOR"] = global_setting
    assert config_data.get_setting("ANSI_COLOR") == global_setting
    assert config_data.get_setting("ANSI_COLOR", "shell") == global_setting

    # test plugin based config setting
    plugin_config_data = {"name": "ANSIBLE_SHELL_EXECUTABLE", "value": "/bin/bash"}
    shell_plugin = {"name": "shell", "type": "shell", "config_data": plugin_config_data}

# Generated at 2022-06-12 21:01:48.908278
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo', 'foo_value'))
    assert config_data._global_settings['foo'].name == 'foo'

    from ansible.plugins.loader import plugin_loader
    plugin = plugin_loader.get('inventory', 'test')
    config_data.update_setting(Setting('foo', 'foo_value'), plugin)
    assert config_data._plugins['inventory']['test']['foo'].name == 'foo'

# Generated at 2022-06-12 21:02:00.141669
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configdata = ConfigData()

# Generated at 2022-06-12 21:02:04.173217
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    result = data.get_settings()
    assert data._global_settings == {}, "Wanted %s, but returned %s" % (data._global_settings, result)
    print("Test get_settings: Passed")


# Generated at 2022-06-12 21:02:14.729709
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    config_data.update_setting(Setting('foo', description='bar'))
    config_data.update_setting(Setting('foo2', description='bar2'))
    config_data.update_setting(Setting('foo3', description='bar3', plugin=Plugin('test')))

    settings = config_data.get_settings()

    assert len(settings) == 2
    assert settings[0].name == 'foo'
    assert settings[0].description == 'bar'
    assert settings[1].name == 'foo2'
    assert settings[1].description == 'bar2'
    assert settings[1].plugin is None

    settings = config_data.get_settings(Plugin('test'))

    assert len(settings) == 1
    assert settings[0].name == 'foo3'
    assert settings

# Generated at 2022-06-12 21:03:31.936261
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting = []
    setting.append({
        "name": "NOPLUGIN",
        "value": "NULL",
        "type": "NULL",
        "section": "NULL",
        "key": "NULL",
        "config_file": "NULL",
        "origins": [
            {
                "type": "NULL",
                "file": "NULL",
                "line": 0,
                "vars": [
                    {
                        "name": "NOPLUGIN",
                        "value": "NULL",
                        "raw_value": "NULL"
                    }
                ]
            }
        ]
    })