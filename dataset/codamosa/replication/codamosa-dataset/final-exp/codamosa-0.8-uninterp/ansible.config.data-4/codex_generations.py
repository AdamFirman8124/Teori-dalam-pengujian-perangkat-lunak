

# Generated at 2022-06-12 20:53:28.740589
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    print("Verifying if an empty list is returned when an inexistent plugin is requested")
    assert config_data.get_settings() == []



# Generated at 2022-06-12 20:53:33.160102
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()
    plugin1 = Plugin(type="cli", name="cli", path="some/path")
    setting = Setting(plugin=plugin1, name="name", value="value")
    configdata.update_setting(setting, plugin1)
    assert configdata._plugins["cli"]["cli"]["name"].value == "value"


# Generated at 2022-06-12 20:53:43.799726
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    assert len(data._global_settings) == 0
    assert len(data._plugins) == 0
    data.update_setting(Setting('testing', 'value'))
    assert len(data._global_settings) == 1
    assert len(data._plugins) == 0
    data.update_setting(Setting('testing2', 'value2'))
    assert len(data._global_settings) == 2
    assert len(data._plugins) == 0
    data.update_setting(Setting('plugin_setting', 'value3'), Plugin('aType', 'aPlugin'))
    assert len(data._global_settings) == 2
    assert len(data._plugins) == 1
    data.update_setting(Setting('another_plugin_setting', 'value4'), Plugin('aType', 'aPlugin'))
    data.update

# Generated at 2022-06-12 20:53:52.084187
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Setting1:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __repr__(self):
            return '{}:{}'.format(self.name, self.value)

    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

        def __repr__(self):
            return '{}:{}'.format(self.type, self.name)

    class TestConfigData:
        def __init__(self):
            self.config_data = ConfigData()

        def test_update_setting(self):
            setting1 = Setting1('setting1', 'value1')
            self.config_data.update_setting(setting1)


# Generated at 2022-06-12 20:53:56.553167
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible import constants as C

    data = ConfigData()
    data2 = ConfigData()
    data2.update_setting(ImmutableDict(name=C.DEFAULT_HOST_LIST))
    assert (data2.get_setting(C.DEFAULT_HOST_LIST))


test_ConfigData_update_setting()

# Generated at 2022-06-12 20:54:08.540817
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from ansible.module_utils.common.config.setting import Setting

    setting_1_1 = Setting('setting-1', 'setting-1-val')
    config_data.update_setting(setting_1_1)
    assert 'setting-1' in config_data.get_settings()
    assert config_data.get_setting('setting-1') == setting_1_1

    setting_2_1 = Setting('setting-2', 'setting-2-val')
    config_data.update_setting(setting_2_1)
    assert 'setting-2' in config_data.get_settings()
    assert config_data.get_setting('setting-2') == setting_2_1

# Generated at 2022-06-12 20:54:20.358631
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settingA = Setting('A', 'string', 'A_value', 'A_type', 'A_help')
    settingB = Setting('B', 'array', ['B_value'], 'B_type', 'B_help')
    config_data.update_setting(settingA)
    config_data.update_setting(settingB)
    # test get_setting
    settings=config_data.get_settings()
    assert settings == [settingA,settingB], "config_data.get_settings() returns a wrong list of settings"
    # test get_setting with plugin
    plugin = Plugin('action', 'shell')
    settingC = Setting('C', 'string', 'C_value', 'C_type', 'C_help')
    config_data.update_setting(settingC, plugin)


# Generated at 2022-06-12 20:54:29.278073
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class TestSetting(object):
        def __init__(self):
            self.name = 'test'
            self.value = 'value'

    class TestPlugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    config = ConfigData()
    setting = TestSetting()
    config.update_setting(setting)

    assert config._global_settings['test'] == setting

    plugin = TestPlugin('inventory', 'test')
    setting.name = 'foo'
    setting.value = 'bar'

    config.update_setting(setting, plugin)

    assert config._plugins['inventory']['test']['foo'] == setting



# Generated at 2022-06-12 20:54:40.385098
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    import sys
    sys.path.append("../lib")
    from ansiblelint import RulesCollection
    import ansiblelint.utils
    from ansiblelint.rules import RulesCollection
    from ansiblelint.runner import Runner

    config_data = ConfigData()

    class Plugin(object):
        def __init__(self, name, type):
            self._name = name
            self._type = type
        @property
        def name(self):
            return self._name
        @property
        def type(self):
            return self._type

    # Test global setting
    setting_name = "test_setting"
    setting_value = "test_setting_value"
    config_data.update_setting(ansiblelint.utils.Setting(setting_name, setting_value))
    setting = config_data.get

# Generated at 2022-06-12 20:54:50.503926
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cfg = ConfigData()
    from ansible.config.setting import Setting
    from ansible.config.manager import ConfigManager
    cfg.update_setting(Setting('of_object', 'of_value', StringConfigParser(), None))
    cfg.update_setting(Setting('of_object2', 'of_value2', StringConfigParser(), None))
    cfg.update_setting(Setting('of_object3', 'of_value3', StringConfigParser(), ConfigManager().get_plugin_options()[0]))
    cfg.update_setting(Setting('of_object4', 'of_value4', StringConfigParser(), ConfigManager().get_plugin_options()[1]))

# Generated at 2022-06-12 20:55:01.084404
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('some_global_setting') is None
    config_data.update_setting(Setting(name='some_global_setting', value='value_some_global_setting'))
    assert config_data.get_setting('some_global_setting') is not None
    plugin = Plugin('Test', 'python')
    assert config_data.get_setting('some_plugin_setting', plugin) is None
    setting = Setting(name='some_plugin_setting', value='value_some_plugin_setting')
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('some_plugin_setting', plugin) is not None


# Generated at 2022-06-12 20:55:10.409548
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create and populate ConfigData object
    config_data = ConfigData()
    setting = Setting('Test Setting', 'Test setting value')
    config_data.update_setting(setting)

    # Create a plugin definition and add it to the ConfigData object
    plugin = Plugin('internal', 'Test Plugin', 'Test plugin description')
    config_data.update_setting(setting, plugin)

    assert len(config_data.get_settings()) == 2
    assert len(config_data.get_settings(plugin)) == 1
    assert config_data.get_settings(plugin)[0].name == setting.name


# Generated at 2022-06-12 20:55:14.348987
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # instantiate the module
    config = ConfigData()
    config.update_setting("setting1")
    # settings should now be updated with 'setting1'
    settings = config.get_settings()
    assert settings[0] == "setting1"
    settings = config.get_settings(None)
    assert settings[0] == "setting1"


# Generated at 2022-06-12 20:55:19.822583
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    class test_setting:
        def __init__(self, name, value):
            self.name = name
            self.value = value
            self.origin = 'ini'

    # test case 1: add a global setting
    setting1 = test_setting("a", "1")
    config_data.update_setting(setting1)
    assert config_data.get_settings()[0].name == 'a'
    assert config_data.get_settings()[0].value == '1'

    # test case 2: add a plugin setting
    setting2 = test_setting("b", "2")
    plugin = test_setting("test", "test")
    config_data.update_setting(setting2, plugin)

# Generated at 2022-06-12 20:55:23.162761
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    settings = ConfigData.get_settings(self, plugin=None)
    assert settings is not None
    assert settings == []

    settings = ConfigData.get_settings(self, plugin=plugin)
    assert settings is not None
    assert settings == []


# Generated at 2022-06-12 20:55:34.968277
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    class Plugin:
        def __init__(self):
            self.name = ''
            self.type = ''

    class Setting:
        def __init__(self):
            self.name = ''

    # Test with a global setting
    setting = Setting()
    setting.name = 'CONFIG_FILE_PATH'
    config_data.update_setting(setting)

    returned_settings = config_data.get_settings()

    assert len(returned_settings) == 1

    returned_setting = returned_settings[0]

    assert returned_setting is setting

    # Test with a non global setting
    plugin = Plugin()
    plugin.name = 'action'
    plugin.type = 'cache'

    setting = Setting()
    setting.name = 'CACHE_PLUGIN'
   

# Generated at 2022-06-12 20:55:45.177856
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_
    config_data = ConfigData()

    # Test when plugin is None
    setting_global = {
        "name": "C.foo",
        "value": "bar",
        "origin": "default",
        "origin_type": "default",
        "source": "global_source",
        "scope": "global",
        "plugin": None
    }
    config_data.update_setting(config_setting.ConfigSetting(setting_global))
    assert config_data._global_settings["C.foo"].value == "bar"

    # Test when plugin is not None

# Generated at 2022-06-12 20:55:48.110716
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data.update_setting({'name' : 'example', 'default' : 'default-value'})
# Test for method get_setting of class ConfigData

# Generated at 2022-06-12 20:55:54.721569
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    myConfigData = ConfigData()
    myConfigData.update_setting({'name': 'key', 'value': 'value', 'plugin_type': 'plugin_type', 'plugin_name': 'plugin_name'})
    assert myConfigData._plugins['plugin_type']['plugin_name']['key']['name'] == 'key'
    assert myConfigData._plugins['plugin_type']['plugin_name']['key']['value'] == 'value'
    assert myConfigData._plugins['plugin_type']['plugin_name']['key']['plugin_type'] == 'plugin_type'
    assert myConfigData._plugins['plugin_type']['plugin_name']['key']['plugin_name'] == 'plugin_name'


# Generated at 2022-06-12 20:56:05.614696
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    # Instantiate Config Data
    config_data = ConfigData()

    # Test the global setting
    setting = ConfigSetting(
        name="config_name",
        value="config_val"
    )
    config_data.update_setting(setting)
    global_settings = config_data.get_settings()
    assert len(global_settings) == 1 and global_settings[0].value == "config_val"

    # Test the plugin setting
    plugin = ConfigPlugin(
        type="module",
        name="foobar"
    )
    setting = ConfigSetting(
        name="config_name",
        value="config_val_2"
    )
    config_data.update_setting(setting, plugin)
    plugin_settings = config_data.get_settings(plugin)

# Generated at 2022-06-12 20:56:20.090325
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Plugin:
        def __init__(self, type_='', name=''):
            self.type = type_
            self.name = name

    class Setting:
        def __init__(self, name='', value='', origin=''):
            self.name = name
            self.value = value
            self.origin = origin

    config = ConfigData()
    
    assert len(config.get_settings()) == 0
    assert config.get_setting('test') is None

    setting = Setting('test', 'global', 'global')
    config.update_setting(setting)
    assert len(config.get_settings()) == 1
    assert config.get_setting('test') == setting

    del setting
    del config

# Generated at 2022-06-12 20:56:31.267337
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    plugin = Plugin({'type': 'foo', 'name': 'bar'})
    data.update_setting(Setting('foo', 'foo'))
    data.update_setting(Setting('foo2', 'foo'), plugin)
    data.update_setting(Setting('foo3', 'foo'), plugin)
    data.update_setting(Setting('foo4', 'foo'), plugin)
    data.update_setting(Setting('foo5', 'foo'), plugin)
    data.update_setting(Setting('foo6', 'foo', 'bar'))
    data.update_setting(Setting('foo7', 'foo', 'bar'))
    data.update_setting(Setting('foo8', 'foo', 'bar'))
    assert data.get_settings()[0].name == 'foo'

# Generated at 2022-06-12 20:56:38.128488
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import pytest
    test_instance = ConfigData()
    plugin_dict={'type':'cache', 'name':'redis'}
    assert test_instance.get_setting('host', plugin=plugin_dict) is None
    test_instance.update_setting('host', plugin=plugin_dict)
    assert test_instance.get_setting('host', plugin=plugin_dict) is not None


# Generated at 2022-06-12 20:56:47.964101
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import PluginLoader

    plugin_loader = PluginLoader()
    plugin_loader.load_all()
    plugins = plugin_loader.all()

    data = ConfigData()

    for ptype in plugins:
        for pname in plugins[ptype]:
            plugin = plugins[ptype][pname]
            data.update_setting(plugin.get_option("plugin_configuration_file"), plugin)

    for ptype in plugins:
        for pname in plugins[ptype]:
            plugin = plugins[ptype][pname]
            assert data.get_setting("plugin_configuration_file", plugin) is not None
            assert data.get_settings(plugin) is not None

# Generated at 2022-06-12 20:56:48.584909
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass



# Generated at 2022-06-12 20:56:56.641929
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    assert(config_data.get_setting('fact_caching_timeout') == None)
    assert(config_data.get_setting('stdout_callback') == None)
    assert(config_data.get_setting('command_warnings') == None)
    assert(config_data.get_setting('action_plugins') == None)
    assert(config_data.get_setting('shell_executable') == None)
    assert(config_data.get_setting('lookup_plugins') == None)
    assert(config_data.get_setting('callback_whitelist') == None)
    assert(config_data.get_setting('remote_tmp') == None)
    assert(config_data.get_setting('stdout_callback') == None)

# Generated at 2022-06-12 20:56:57.834916
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    assert config_data.get_setting('name')  is None



# Generated at 2022-06-12 20:57:07.503001
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # test1: no plugin defined
    testcd = ConfigData()
    assert testcd.get_settings() == []

    # test 2: no plugin defined, but we have a setting
    testcd._global_settings['testsetting'] = 'settingvalue'
    assert testcd.get_settings()[0].name == 'testsetting'

    # test 3: plugin defined, but unknown
    testplugin = Plugin(name='testplugin', type='testtype')
    assert testcd.get_settings(testplugin) == []

    # test4: plugin defined and known, but no config for plugin
    testcd._plugins['testtype'] = {}
    assert testcd.get_settings(testplugin) == []

    # test5: plugin defined and known, with config
    testcd._plugins['testtype']['testplugin'] = {}
    testcd

# Generated at 2022-06-12 20:57:14.513107
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    config_data.update_setting(Setting('key1', 'value1')) # add a global setting
    config_data.update_setting(Setting('key2', 'value2'), Plugin('action', 'example')) # add a plugin-specific setting
    config_data.update_setting(Setting('key1', 'value1'), Plugin('action', 'example')) # add a another plugin-specific setting with the same key

    assert len(config_data._global_settings) == 1
    assert len(config_data._plugins) == 1
    assert len(config_data._plugins['action']) == 1
    assert len(config_data._plugins['action']['example']) == 2



# Generated at 2022-06-12 20:57:26.572772
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansiblelint.utils.object_dictionary_class import Plugin
    from ansiblelint.utils.object_dictionary_class import Setting

    config_data = ConfigData()

    # test for global setting
    global_setting = Setting(name='test_setting', default=True)
    config_data.update_setting(global_setting)
    actual_setting = config_data.get_setting('test_setting')
    assert actual_setting.name == global_setting.name
    assert actual_setting.default == global_setting.default

    # test for plugin setting
    plugin = Plugin(type='ANSIBLE0002', name='test_plugin')
    plugin_setting = Setting(name='test_plugin_setting', default=True)
    config_data.update_setting(plugin_setting, plugin)
    actual_setting = config_data

# Generated at 2022-06-12 20:57:35.494873
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd=ConfigData()
    assert cd._global_settings == {}
    assert cd._plugins == {}
    s = {'name': 'name', 'value': 'value'}
    cd.update_setting(s)
    assert cd._global_settings == {'name': {'name': 'name', 'value': 'value'}}
    assert cd._plugins == {}


# Generated at 2022-06-12 20:57:45.098140
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configData = ConfigData()

    # create a setting
    setting = ConfigSetting()
    setting.name = "setting1"
    setting.value = "value1"
    setting.plugin = None
    setting.plugin_specific = False
    setting.source = "source1"
    setting.section = "section1"
    setting.scope = "scope1"

    # add the setting
    configData.update_setting(setting)

    # get the setting
    setting = configData.get_setting("setting1")
    assert setting.name == "setting1"
    assert setting.value == "value1"
    assert setting.plugin == None
    assert setting.plugin_specific == False
    assert setting.source == "source1"
    assert setting.section == "section1"
    assert setting.scope == "scope1"

#

# Generated at 2022-06-12 20:57:47.342421
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert len(settings) == 0


# Generated at 2022-06-12 20:57:57.801633
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    import sys
    from units.mock.loader import DictDataLoader
    from ansible.parsing.vault import VaultLib
    config_data.update_setting(Setting('vault_password_file', 'default', ['/path/vault/file'], False, '', '', '', '', ''))
    config_data.update_setting(Setting('role_path', 'default', ['/path/roles'], False, '', '', '', '', ''))
    config_data.update_setting(Setting('lookup_plugins', 'default', ['/path/lookup'], False, '', '', '', '', ''))

# Generated at 2022-06-12 20:58:08.171080
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Create a config data object
    config = ConfigData()

    # Create a setting object
    setting = Object()
    setting.name = 'test'

    # Ensure that the setting is not found in the global settings
    assert config.get_setting('test') is None

    # Update the setting
    config.update_setting(setting)

    # Ensure that the setting is found in the global settings
    assert config.get_setting('test') is not None

    # Create a plugin object
    plugin = Object()
    plugin.type = 'type'
    plugin.name = 'name'

    # Make sure the plugin is not found
    assert config.get_setting('test', plugin) is None

    # Update the setting again, adding the plugin attributes
    config.update_setting(setting, plugin)

    # Ensure that the setting is found in the plugin


# Generated at 2022-06-12 20:58:10.350847
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert len(data.get_settings()) == 0



# Generated at 2022-06-12 20:58:18.725077
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    # update global setting
    setting = Setting(name='global_setting', value='global_value')
    config_data.update_setting(setting)
    assert(config_data.get_setting('global_setting').value == 'global_value')
    assert(config_data.get_settings()[0].value == 'global_value')

    # update plugin setting
    plugin = Plugin(type='module', name='module_name')
    setting = Setting(name='module_setting', value='module_value')
    config_data.update_setting(setting, plugin=plugin)
    assert(config_data.get_setting('module_setting', plugin=plugin).value == 'module_value')
    assert(config_data.get_settings(plugin=plugin)[0].value == 'module_value')




# Generated at 2022-06-12 20:58:26.515520
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config.update_setting(Setting('password', 'ldap_role1_password', 'secret'))
    config.update_setting(Setting('lookup', 'lookup_plugin_config', 'lookup_plugin.yml'), Plugin('lookup', 'my_lookup'))

    assert config.get_setting('password').value == 'secret'
    assert config.get_setting('lookup', Plugin('lookup', 'my_lookup')).value == 'lookup_plugin.yml'



# Generated at 2022-06-12 20:58:37.641167
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    assert (len(config_data._global_settings) == 0)
    assert (config_data._plugins == {})

    setting = MetadataSetting()
    setting.name = "ansible_host_name"
    setting.value = "host-abc"
    plugin = MetadataPlugin()
    plugin.name = "inventory"
    plugin.type = "INVENTORY"
    config_data.update_setting(setting, plugin)

    plugin = MetadataPlugin()
    plugin.name = "inventory"
    plugin.type = "INVENTORY"
    setting = config_data.get_setting("ansible_host_name", plugin)

    assert (setting.name == "ansible_host_name")
    assert (setting.value == "host-abc")

    setting = config_data

# Generated at 2022-06-12 20:58:44.725380
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin_type = PluginType('TestPluginType')
    plugin_name = PluginName('TestPlugin')
    plugin = Plugin(plugin_type, plugin_name)
    setting_names = ['test_setting_1', 'test_setting_2']
    for setting_name in setting_names:
        config_data.update_setting(Setting(setting_name, 'TestValue'))
        config_data.update_setting(Setting(setting_name, 'TestValue'), plugin)
    settings = config_data.get_settings()
    settings_filtered = config_data.get_settings(plugin)
    assert len(settings) == 2 * len(setting_names)
    assert len(settings_filtered) == len(setting_names)



# Generated at 2022-06-12 20:58:56.795241
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('test_setting_name', 'test_value1', 'test_plugins_dir1')
    config_data.update_setting(setting)
    assert config_data.get_setting('test_setting_name') == setting



# Generated at 2022-06-12 20:59:08.816684
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    plugin_type = "action"
    plugin_name = "setup"
    plugin = Plugin(plugin_type, plugin_name)
    config_data = ConfigData()

    # Insert settings
    config_data.update_setting(Setting("greet", "hello"))
    config_data.update_setting(Setting("farewell", "bye"), plugin)

    # Check global settings
    result = config_data.get_settings()
    assert len(result) == 1
    assert result[0].name == "greet"
    assert result[0].value == "hello"
    assert result[0].plugin is None

    # Check plugin settings
    result = config_data.get_settings(plugin)
    assert len(result) == 1
    assert result[0].name == "farewell"
    assert result[0].value == "bye"

# Generated at 2022-06-12 20:59:11.725159
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    setting = Setting("test", "The test setting")
    cd.update_setting(setting)
    settings = cd.get_settings()
    assert setting in settings

# Generated at 2022-06-12 20:59:19.344497
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    class Plugin(object):
        def __init__(self, type=None, name=None):
            self.type = type
            self.name = name

    class Setting(object):
        def __init__(self, name=None):
            self.name = name

    plugin = Plugin(type='test_type', name='test_name')

    setting1 = Setting(name='test_name_1')
    setting2 = Setting(name='test_name_2')
    setting3 = Setting(name='test_name_3')

    config_data.update_setting(setting1)
    config_data.update_setting(setting2, plugin)
    config_data.update_setting(setting3)

    settings = config_data.get_settings(plugin)

# Generated at 2022-06-12 20:59:23.399746
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # Test if method returns None
    assert config_data.get_setting('c.does_not_exist') is None

    # Test if method returns value
    assert config_data.get_setting('c.color_stdout_highlight') == 'magenta'



# Generated at 2022-06-12 20:59:32.792945
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    plugin1 = Plugin(type='connection', name='ssh')
    plugin2 = Plugin(type='connection', name='winrm')
    plugin3 = Plugin(type='become', name='su')
    plugin4 = Plugin(type='become', name='become')
    setting1 = Setting(name='noconfig_setting', value='setting1_value', origin='noconfig')
    setting2 = Setting(name='config_setting', value='setting2_value', origin='config')
    setting3 = Setting(name='noconfig_setting_plugin1', value='setting3_value', origin='noconfig')
    setting4 = Setting(name='config_setting_plugin1', value='setting4_value', origin='config')

# Generated at 2022-06-12 20:59:39.956951
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    # TEST: should return empty list if no data is present
    assert not config_data.get_settings()

    # TEST: should return list of global settings
    setting1 = Setting('setting1')
    setting2 = Setting('setting2')
    config_data.update_setting(setting1)
    config_data.update_setting(setting2)
    assert len(config_data.get_settings()) == 2

    # TEST: should return empty list if no data is present
    plugin = Plugin('test', 'action')
    assert not config_data.get_settings(plugin)

    # TEST: should return list of settings for the plugin
    setting3 = Setting('setting3')
    setting4 = Setting('setting4')
    config_data.update_setting(setting3, plugin)

# Generated at 2022-06-12 20:59:47.359293
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    assert len(data.get_settings()) == 0
    data.update_setting(Setting("foo", "bar"))
    assert len(data.get_settings()) == 1
    data.update_setting(Setting("foo", "baz"))
    assert data.get_settings()[0].value == "baz"

    from collections import namedtuple
    Plugin = namedtuple("Plugin", ["type", "name"])
    p = Plugin("someplugin", "some_plugin")
    data.update_setting(Setting("baz", "qux"), p)
    assert len(data.get_settings()) == 2
    data.update_setting(Setting("fobar", "quxqux"), p)
    assert len(data.get_settings(p)) == 2


# Generated at 2022-06-12 20:59:59.017358
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from units.mock.loader import DictDataLoader
    from ansible.config.manager import ConfigManager

    confmgr = ConfigManager(loader=DictDataLoader(
        {'f': {'a': '1', 'b': '2'},
         'c': {'d': '3'}
         }
    ))

    assert confmgr.configdata.get_setting('a').value == '1'
    assert confmgr.configdata.get_setting('a', plugin=confmgr.config.Plugin(name='f', type='iniconfig')).value == '1'

    assert confmgr.configdata.get_setting('b').value == '2'

# Generated at 2022-06-12 21:00:10.265528
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    def test_helper(msg, c, plugin, setting_name, should_exist):
        if should_exist:
            print(msg)
            assert c.get_setting(setting_name, plugin).name == setting_name
        else:
            print(msg)
            assert c.get_setting(setting_name, plugin) is None

    class Plugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    c = ConfigData()

    class Setting(object):
        def __init__(self, name):
            self.name = name

    # No setting
    test_helper('test_helper_1', c, None, 'test_setting', False)

    # Setting for None plugin

# Generated at 2022-06-12 21:00:38.134808
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import config_loader, plugin_loader

    # initialize data objects
    config_data = ConfigData()
    plugin = plugin_loader.get('action', 'win_updates')

    # revert config object back to original state
    config_data.update_setting(config_loader.get_setting('gather_timeout'))

    # test update_setting method
    # TODO: randomly generate test values
    config_data.update_setting(config_loader.get_setting('gather_timeout'))
    assert config_data.get_setting('gather_timeout').value == 300

    config_data.update_setting(config_loader.get_setting('gather_facts', plugin.namespace))
    assert config_data.get

# Generated at 2022-06-12 21:00:42.043996
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    setting_test = ConfigData()
    setting_test.update_setting(Setting("Test", "Test setting"))
    setting_test.update_setting(Setting("Test2", "Test2 setting"))
    assert setting_test.get_settings() == [Setting("Test", "Test setting"),
                                           Setting("Test2", "Test2 setting")]

# Generated at 2022-06-12 21:00:49.233545
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()

    set1 = ConfigSetting()
    set1.name = 'test1'
    set1.value = 'value1'
    set1.plugin = ConfigPluginInfo('plugin1', 'plugin1', 'type1')

    configdata.update_setting(set1)

    assert configdata.get_setting('test1').value == 'value1'
    assert configdata.get_setting('test1', 'plugin1') == None



# Generated at 2022-06-12 21:00:53.970744
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Test case for the default case, i.e., setting is not found in any plugin
    # and also not in the global settings
    config_data = ConfigData()
    expected_setting = None
    assert expected_setting == config_data.get_setting('not_present')
    assert expected_setting == config_data.get_setting('not_present', plugin)


# Generated at 2022-06-12 21:01:04.146524
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = {
        'name': 'foo',
        'value': 'bar',
        'section': 'common',
        'source': 'ansible.cfg',
        'scope': 'test scope'
    }
    config_data.update_setting(setting)
    assert config_data._global_settings['foo'].name == 'foo'
    assert config_data._global_settings['foo'].value == 'bar'
    assert config_data._global_settings['foo'].section == 'common'
    assert config_data._global_settings['foo'].source == 'ansible.cfg'
    assert config_data._global_setting

# Generated at 2022-06-12 21:01:10.053550
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible_collections.ansible.community.plugins.module_utils.config import Setting

    config_data = ConfigData()
    setting1 = Setting(name='setting1')
    setting2 = Setting(name='setting2')
    config_data.update_setting(setting1)
    config_data.update_setting(setting2)

    assert len(config_data.get_settings()) == 2
    assert setting1 in config_data.get_settings()
    assert setting2 in config_data.get_settings()

# Generated at 2022-06-12 21:01:21.740931
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    settings_plugin_1 = ["ansible", "inventory", "/etc/ansible/hosts"]
    setting_plugin_2 = "inventory"
    config_data = ConfigData()
    for i in range(3):
        setting = ConfigSetting(settings_plugin_1[i], i, settings_plugin_1[i], settings_plugin_1[i], "global")
        config_data.update_setting(setting)
    for i in range(3):
        setting = ConfigSetting(setting_plugin_2, i, "xyz", "xyz", "xyz")
        config_data.update_setting(setting, ConfigPlugin(setting_plugin_2, "xyz"))
    settings = config_data.get_settings(ConfigPlugin(setting_plugin_2, "xyz"))

# Generated at 2022-06-12 21:01:25.920047
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('name', 'value')
    plugin = Plugin('plugin_type', 'plugin_name')
    config_data.update_setting(setting)
    assert config_data.get_setting('name') == setting
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('name', plugin) == setting


# Generated at 2022-06-12 21:01:32.074958
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data._global_settings = {
        'host_key_checking': {'value': 'False', 'origin': 'default'},
        'log_path': {'value': 'False', 'origin': 'default'},
    }
    assert config_data._global_settings == config_data.get_setting(None)
    assert config_data._global_settings['log_path'] == config_data.get_setting('log_path', None)



# Generated at 2022-06-12 21:01:36.977113
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = Plugin('plugin', 'type')
    setting = Setting('settings', 'value', None)
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('settings') is None
    assert config_data.get_setting('settings', plugin) is not None


# Generated at 2022-06-12 21:02:17.730361
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting = ConfigSetting('name', 'value')
    plugin = Plugin('name', 'type')
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('name', plugin) == setting


# Generated at 2022-06-12 21:02:28.949760
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()
    cd.update_setting(Setting('my_setting'))
    cd.update_setting(Setting('my_other_setting'))
    cd.update_setting(Setting('my_last_setting'))

    # test getting all settings
    assert len(cd.get_settings()) == 3

    oneplugin = Plugin('oneplugin')
    oneplugin.set_type('oneplugin_type')
    cd.update_setting(Setting('setting_for_oneplugin'), plugin=oneplugin)

    assert len(cd.get_settings()) == 4
    assert len(cd.get_settings(plugin=oneplugin)) == 1

    two_plugin = Plugin('two_plugin')
    two_plugin.set_type('two_plugin_type')

# Generated at 2022-06-12 21:02:41.312244
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    from collections import namedtuple

    ConfigData = ConfigData()
    Plugin = namedtuple('Plugin', ['type', 'name'])

    assert ConfigData.get_setting('collections_paths') is None
    assert ConfigData.get_setting('collections_paths', Plugin.__new__(Plugin, '', '')) is None

    ConfigData.update_setting('collections_paths', 'hello')

    assert ConfigData.get_setting('collections_paths') is not None
    assert ConfigData.get_setting('collections_paths') == 'hello'
    assert ConfigData.get_setting('collections_paths', Plugin.__new__(Plugin, '', '')) is None
    assert ConfigData.get_setting('') is None


# Generated at 2022-06-12 21:02:46.162741
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('my_setting', 'my_value'))
    assert config_data.get_setting('my_setting')   # Global setting
    assert config_data.get_setting('my_setting', Plugin('my_plugin', 'action'))
    assert not config_data.get_setting('my_setting2')   # Unknown setting
    assert not config_data.get_setting('my_setting', Plugin('my_plugin2', 'action'))   # Unknown plugin
    assert not config_data.get_setting('my_setting', Plugin('my_plugin', 'connection'))   # Unknown plugin type



# Generated at 2022-06-12 21:02:48.970459
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting = config_data.get_setting('module_name')
    assert setting is None



# Generated at 2022-06-12 21:02:52.792816
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(value='test', name='test_setting', plugin=Plugin('test_plugin', 'test_type')))
    assert(config_data.get_setting('test_setting').value == 'test')



# Generated at 2022-06-12 21:03:00.883602
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from unit.plugins.modules.utils import set_module_args
    from ansible.plugins.loader import config_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader

    from ansible.module_utils._text import to_text

    from ansible.plugins.connection import ConnectionBase
    from ansible.plugins.action.normal import ActionModule

    class MockConnection(ConnectionBase):

        def open(self):
            return None

        def close(self):
            return None

        def exec_command(self, cmd):
            return None

    class MockActionModule(ActionModule):

        def run(self, tmp=None, task_vars=None):
            self._task_vars = task_vars


# Generated at 2022-06-12 21:03:12.696014
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    plugin_type = "test_plugin_type"
    plugin_name = "test_plugin_name"

    plugin_type2 = "test_plugin_type2"
    plugin_name2 = "test_plugin_name2"

    setting_name = "test_setting_name"

    setting = Setting(setting_name)

    config_data.update_setting(setting)
    actual = config_data.get_setting(setting_name)
    assert actual is not None
    assert actual.name == setting_name
    assert actual.plugin_name == None
    assert actual.plugin_type == None

    config_data.update_setting(setting, PluginDefinition(plugin_type, plugin_name))

# Generated at 2022-06-12 21:03:21.771630
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    from ansible.plugins.loader import PluginLoader
    config.update_setting(Setting('foo', 'global', 'bar', 'global', 'global', 'global', -1, 'global'))
    assert config.get_setting('foo').value == 'bar'
    foo = PluginLoader('foo')
    bar = PluginLoader('bar')
    config.update_setting(Setting('foo', 'global', 'bar', 'global', 'global', 'global', -1, 'global'), plugin=foo)
    config.update_setting(Setting('foo', 'global', 'baz', 'global', 'global', 'global', -1, 'global'), plugin=bar)
    config.update_setting(Setting('foo', 'global', 'buzz', 'global', 'global', 'global', -1, 'global'))

# Generated at 2022-06-12 21:03:25.233617
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    c = config_data.update_setting(Setting(name='foo', value='bar'))
    assert c == True