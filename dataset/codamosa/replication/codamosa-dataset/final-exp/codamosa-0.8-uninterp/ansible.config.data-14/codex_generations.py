

# Generated at 2022-06-12 20:53:31.373109
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('test', 'test')
    config_data.update_setting(setting)
    assert config_data.get_setting('test') is not None


# Generated at 2022-06-12 20:53:41.431215
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    conf = ConfigData()
    class Plugin:
        def __init__(self, name, type):
            self.name = name
            self.type = type
    class Setting:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    plugin = Plugin('test', 'default')
    setting = Setting('name', 'value')

    conf.update_setting(setting, plugin)

    assert plugin.name in conf._plugins['default']
    assert setting.name in conf._plugins['default'][plugin.name]
    assert conf._plugins['default'][plugin.name][setting.name].value == 'value'
    assert setting.name not in conf._global_settings


# Generated at 2022-06-12 20:53:44.037578
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    cd.update_setting(Setting('s1'))

    assert cd.get_setting('s1') is not None


# Generated at 2022-06-12 20:53:46.549477
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('') == None
    assert config_data.get_setting('abc') == None


# Generated at 2022-06-12 20:53:54.249832
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(ConfigSetting(ConfigSetting.NAME_VARS_PLUGINS, name_vars_plugins))
    assert config_data.get_setting(ConfigSetting.NAME_VARS_PLUGINS).get_value() == name_vars_plugins
    assert config_data.get_setting(ConfigSetting.NAME_VARS_PLUGINS).get_source() == 'config.cfg'
    assert config_data.get_setting(ConfigSetting.NAME_VARS_PLUGINS).get_line_number() == 4


# Generated at 2022-06-12 20:54:06.148873
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # create a test object
    data = ConfigData()

    # add values to the test object
    data.update_setting("a1")
    data.update_setting("a2")
    data.update_setting("a3", "type", "name")
    data.update_setting("a4", "type", "name")
    data.update_setting("a5", "type", "other")

    # test the get_setting method of the data object
    assert data.get_setting("a1") == "a1"
    assert data.get_setting("a3", "type", "name") == "a3"
    assert data.get_setting("a5", "type", "other") == "a5"

    # test the get_settings of the data object

# Generated at 2022-06-12 20:54:12.784463
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    assert config_data.get_settings() == []
    assert config_data.get_settings(plugin=None) == []

    class Setting(object):
        name = 'test'

    test_setting = Setting()
    test_setting_control = Setting()
    config_data.update_setting(test_setting)
    assert test_setting in config_data.get_settings()
    assert test_setting in config_data.get_settings(plugin=None)

    class Plugin(object):
        name = 'test'
        type = 'test'

    test_plugin = Plugin()
    test_plugin_control = Plugin()
    config_data.update_setting(test_setting, test_plugin)
    assert test_setting not in config_data.get_settings()

# Generated at 2022-06-12 20:54:17.864213
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    configData = ConfigData()
    setting = Setting('key', 'value')
    plugin = Plugin('plugin_type', 'plugin_name')

    configData.update_setting(setting)
    assert configData._global_settings['key'] == setting

    configData.update_setting(setting, plugin)
    assert configData._plugins['plugin_type']['plugin_name']['key'] == setting


# Generated at 2022-06-12 20:54:28.934708
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create a ConfigData object
    config_data = ConfigData()
    plugin_type = 'global'
    plugin_name = 'global'

    # Get the setting 'test_setting' and assert it isn't present
    setting = config_data.get_setting('test_setting', None)
    assert setting is None

    # Get the settings and assert that the list is empty
    settings = config_data.get_settings(None)
    assert len(settings) == 0

    # Update the config data with a test setting
    setting = Setting('test_setting', 'test_value', plugin_type, plugin_name)
    config_data.update_setting(setting)

    # Assert that the setting has been added
    setting = config_data.get_setting('test_setting', None)
    assert setting is not None
    assert setting.name

# Generated at 2022-06-12 20:54:36.532789
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

    cd = ConfigData()

    from ansiblelint.rules.TrailingWhitespaceRule import TrailingWhitespaceRule
    trailing_space_rule = TrailingWhitespaceRule()

    cd.update_setting(trailing_space_rule.get_setting('allow_leading_whitespace'))
    cd.update_setting(trailing_space_rule.get_setting('ignore_blank_lines'))

    assert len(cd.get_settings()) == 2

    cd.update_setting(trailing_space_rule.get_setting('ignore_blank_lines'),
                      Plugin('linters', 'no_trailing_spaces'))

# Generated at 2022-06-12 20:54:49.300981
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting(Setting("test.1", "test.1"))
    cd.update_setting(Setting("test.2", "test.2"))
    cd.update_setting(Setting("test.3", "test.3"))
    cd.update_setting(Setting("test.4", "test.4"))
    cd.update_setting(Setting("test.5", "test.5"))
    cd.update_setting(Setting("test.6", "test.6"))
    assert cd.get_settings() == [Setting("test.1", "test.1"), Setting("test.2", "test.2"), Setting("test.3", "test.3"), Setting("test.4", "test.4"), Setting("test.5", "test.5"), Setting("test.6", "test.6")]


# Generated at 2022-06-12 20:54:51.604639
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()



# Generated at 2022-06-12 20:55:01.972885
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    plugin = Plugin('test_plugin', 'test_type', 'test_path')

    setting_1 = Setting(plugin, 'plugin_setting_1', 'plugin_value_1')
    config_data.update_setting(setting_1, plugin)

    assert plugin.type in config_data._plugins
    assert plugin.name in config_data._plugins[plugin.type]
    assert setting_1.name in config_data._plugins[plugin.type][plugin.name]

    store_setting_1 = config_data._plugins[plugin.type][plugin.name][setting_1.name]
    assert store_setting_1.plugin.name == plugin.name
    assert store_setting_1.plugin.type == plugin.type
    assert store_setting_1.name == setting_1.name

# Generated at 2022-06-12 20:55:12.737617
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    global_settings = {
        "g1": "v1",
        "g2": "v2"
    }

    plugin_settings = {
        "p1": "v1",
        "p2": "v2"
    }

    type_name = "type"
    plugin_name = "name"

    config_data = ConfigData()

    config_data._global_settings = global_settings
    config_data._plugins[type_name] = {}
    config_data._plugins[type_name][plugin_name] = plugin_settings

    assert config_data.get_settings() == [global_settings[k] for k in global_settings]

    assert config_data.get_settings(plugin=Plugin(type_name, plugin_name)) == [plugin_settings[k] for k in plugin_settings]




# Generated at 2022-06-12 20:55:21.708470
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    # test if global setting is in list of settings
    setting1 = Setting("ansible_python_interpreter")
    config_data.update_setting(setting1)
    settings = config_data.get_settings()
    assert setting1 in settings

    # test if plugin setting is in list of settings
    setting2 = Setting("become")
    plugin = Plugin("become")
    config_data.update_setting(setting2, plugin)
    settings = config_data.get_settings(plugin)
    assert setting2 in settings



# Generated at 2022-06-12 20:55:33.594554
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import unittest
    from pprint import pprint

    from ..config import BaseSetting

    class SettingsTest(unittest.TestCase):

        def test_get_settings1(self):
            settings = ConfigData()
            setting1 = BaseSetting(name='var1')
            settings.update_setting(setting1)
            setting2 = BaseSetting(name='var2', plugin={'type': 'auth', 'name': 'foo'})
            settings.update_setting(setting2)

            self.assertEqual(settings.get_settings(), [setting1])
            self.assertEqual(settings.get_settings(plugin={'type': 'auth', 'name': 'foo'}), [setting2])

        def test_get_settings2(self):
            settings = ConfigData()

# Generated at 2022-06-12 20:55:40.859168
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    s1 = ConfigSetting("", "", "", "")
    s2 = ConfigSetting("", "", "", "")
    s3 = ConfigSetting("", "", "", "")
    config.update_setting(s1)
    config.update_setting(s2)
    config.update_setting(s3)
    assert config.get_settings() == [s1, s2, s3]

# Generated at 2022-06-12 20:55:49.640794
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    import ConfigSetting
    cs = ConfigSetting.ConfigSetting(name='ansible_python_interpreter', value='/usr/bin/python2.7', plugin=None)
    cd.update_setting(cs)
    print (cd._global_settings)
    cs1 = ConfigSetting.ConfigSetting(name='ansible_python_interpreter', value='/usr/bin/python2.6', plugin=None)
    cd.update_setting(cs1)
    print (cd._global_settings)

    plugin = ConfigSetting.Plugin('inventory', 'auto')
    cs2 = ConfigSetting.ConfigSetting(name='enable', value='True', plugin=plugin)
    cd.update_setting(cs2)
    print (cd._plugins)

    plugin2 = ConfigSetting.Plugin('inventory', 'auto')


# Generated at 2022-06-12 20:55:53.002990
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    plugin_name = 'test'
    plugin_type = 'test'
    name = 'test'
    value = 'test'
    setting = Setting('test', 'test', 'test')
    plugin = Plugin(plugin_name, plugin_type)
    configData.update_setting(setting, plugin)
    assert configData._plugins[plugin_type][plugin_name][name] == value


# Generated at 2022-06-12 20:55:59.125549
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = Plugin()
    setting = Setting()
    config_data.update_setting(setting)
    assert config_data._global_settings['foo'] == setting
    config_data.update_setting(setting, plugin)
    assert config_data._plugins['connection']['local']['foo'] == setting
    assert config_data._global_settings['foo'] == setting


# Generated at 2022-06-12 20:56:09.136091
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # ARRANGE
    from ansible.plugins.loader import find_plugin
    from ansible.plugins.inventory import InventoryModule
    from ansible.plugins.action import ActionModule
    from ansible.plugins.callback import CallbackModule
    from ansible.plugins.connection import ConnectionModule
    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.vars import VarsModule
    from ansible.plugins.filter import FilterModule
    from ansible.plugins.test import TestModule
    from ansible.plugins.strategy import StrategyModule

    inventory_plugin = find_plugin('inventory')
    action_plugin = find_plugin('action')
    callback_plugin = find_plugin('callback')
    connection_plugin = find_plugin('connection')
    lookup_plugin = find_plugin('lookup')
    vars_plugin

# Generated at 2022-06-12 20:56:16.393859
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert not cd.get_settings()

    cd.update_setting(Setting("test", "test"))
    assert len(cd.get_settings()) == 1

    p = Plugin("lookup", "lookup_test")
    cd.update_setting(Setting("test", "test"), p)
    assert len(cd.get_settings(p)) == 1



# Generated at 2022-06-12 20:56:27.981616
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import get_plugin_class
    from ansible.plugins.connection.ssh import ConnectionModule
    from ansible import constants as C
    from ansible.cli.config import ConnectionOption

    config_data = ConfigData()

    connection_plugin = get_plugin_class(plugin_type='connection', name='ssh')

    connection_option = ConnectionOption()
    connection_option.name = C.DEFAULT_TRANSPORT
    connection_option.value = 'ssh'
    connection_option.plugin_type = 'connection'
    connection_option.plugin_name = 'ssh'

    config_data.update_setting(connection_option, plugin=connection_plugin)

    settings = config_data.get_settings()
    assert len(settings) == 1


# Generated at 2022-06-12 20:56:36.453685
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from collections import namedtuple

    Plugin = namedtuple('Plugin', ['type', 'name'])
    plugin = Plugin(type='module', name='ping')

    Setting = namedtuple('Setting', ['name', 'value'])
    setting = Setting(name='FORKS', value='5')

    config_data = ConfigData()

    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('FORKS', plugin).value == '5'



# Generated at 2022-06-12 20:56:40.144557
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('ansible_hostname') is None
    assert config_data.get_setting('ansible_hostname', plugin='module') is None
    assert config_data.get_setting('ansible_hostname', plugin='inventory') is None


# Generated at 2022-06-12 20:56:43.321176
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert isinstance(config_data.get_settings(), list)
    assert len(config_data.get_settings()) == 0


# Generated at 2022-06-12 20:56:47.919076
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    setting = MockSetting(name='some_setting', default='some_value', path='some_path')
    config_data.update_setting(setting)

    assert config_data.get_setting(setting.name) == setting


# Generated at 2022-06-12 20:56:56.309250
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    assert config.get_setting('foo_setting', plugin=None) is None, 'An empty setting should be None'
    config.update_setting(Setting('foo_setting', value=True))
    assert config.get_setting('foo_setting', plugin=None) == [Setting('foo_setting', value=True)], \
        'The setting should be added to the global section'
    config.update_setting(Setting('foo_setting', value=False, plugin='bar', plugin_type='baz'))
    assert config.get_setting('foo_setting', plugin=Plugin('bar', 'baz')) == [Setting('foo_setting', value=False, plugin='bar', plugin_type='baz')], \
        'The setting should be added to the corresponding plugin section'



# Generated at 2022-06-12 20:57:02.120868
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_global_settings = {}
    test_global_settings["foo"] = "bar"
    test_global_settings["bar"] = "foo"
    test_plugins_settings = {}
    test_plugins_settings["lookup"] = {}
    test_plugins_settings["lookup"]["myplugin"] = {}
    test_plugins_settings["lookup"]["myplugin"]["foo"] = "bar"
    test_plugins_settings["lookup"]["myplugin"]["bar"] = "foo"

    config_data = ConfigData()
    config_data._global_settings = test_global_settings
    config_data._plugins = test_plugins_settings

    settings = config_data.get_settings()
    assert len(settings) == 2
    for s in settings:
        assert s.plugin is None
       

# Generated at 2022-06-12 20:57:04.722507
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('mock_setting') is None


# Generated at 2022-06-12 20:57:08.269924
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    print(config_data.get_settings())



# Generated at 2022-06-12 20:57:08.783341
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass

# Generated at 2022-06-12 20:57:12.320916
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    assert config_data.get_settings() == []

    import unittest.mock as mock

    setting = mock.MagicMock(name='setting1')
    config_data.update_setting(setting)

    assert config_data.get_settings() == [setting]



# Generated at 2022-06-12 20:57:24.444577
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    import plugins
    import settings
    import sys

    config_data = ConfigData()

    # Create different types of settings
    update_strategy_setting = settings.UpdateStrategySetting('update_strategy', 'off', 'Update strategy for the plugin')
    config_setting = settings.ConfigSetting('config', 'base.yml', 'YAML configuration file for the plugin')
    bool_setting = settings.BoolSetting('yes', True, 'A boolean value')
    float_setting = settings.FloatSetting('threshold', 0.8, 'A float value')
    int_setting = settings.IntSetting('count', 10, 'An int value')
    list_setting = settings.ListSetting('extensions', ['yml', 'yaml'], 'A list value')

# Generated at 2022-06-12 20:57:31.555179
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.utils.plugin import Plugin
    import pytest

    plugin = Plugin('action', 'test', 'test')
    config_data = ConfigData()
    config_data.update_setting('test')
    config_data.update_setting('test1', plugin)

    assert len(config_data.get_settings()) == 1
    assert len(config_data.get_settings(plugin)) == 1

    with pytest.raises(Exception):
        config_data.get_settings('test')


# Generated at 2022-06-12 20:57:39.322918
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Set of plugins
    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

    plugin1 = Plugin('foo', 'bar')
    plugin2 = Plugin('baz', 'qux')

    # Set of settings
    class Setting:
        def __init__(self, type, name, value, plugin=None):
            self.type = type
            self.name = name
            self.value = value
            self.plugin = plugin

    setting1 = Setting('boolean', 'g_bool', 'True')
    setting2 = Setting('string', 'g_str', 'foo')
    setting3 = Setting('float', 'g_float', '2.0')
    setting4 = Setting('int', 'g_int', '2')

# Generated at 2022-06-12 20:57:41.895992
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data=ConfigData()
    plugin = AnsiblePlugin('action', 'copy')

# Generated at 2022-06-12 20:57:47.626799
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()

    plugin = Plugin(type='callback', name='debug')
    setting = Setting(name='callback_whitelist', value='debug')
    config.update_setting(setting, plugin=plugin)

    value = config.get_setting(name='callback_whitelist', plugin=plugin)
    assert value.name == 'callback_whitelist'
    assert value.value == 'debug'


# Generated at 2022-06-12 20:57:49.442808
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    a = config.get_settings(plugin=None)
    assert a == []

# Generated at 2022-06-12 20:57:59.480775
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from units.mock.loader import DictDataLoader
    from units.mock.path import MockPath

    from ansible.plugins.loader import PluginLoader

    core = PluginLoader('core', 'core', 'core', 'core', C.DEFAULT_CORE_PATH, '', None)
    shell = PluginLoader('shell', 'shell', 'shell', 'shell', C.DEFAULT_SHELL_PATH, '', None)

    path = MockPath({
        'test_config': {
            'ansible.cfg': '''
[defaults]
some_setting=some_value

[shell]
enable = False

[sudo]
enable = False

[persistent_connection]
enable = False

[suricata]
enable = True
        '''
        }
    })

    data_loader = DictData

# Generated at 2022-06-12 20:58:07.115660
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo', 'string', 'value'))
    config_data.update_setting(Setting('bar', 'int', '2'))

    assert len(list(config_data.get_settings())) == 2
    assert len(list(config_data.get_settings(Plugin(type='bar', name='foo')))) == 0



# Generated at 2022-06-12 20:58:08.467561
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cfg = ConfigData()
    cfg.update_setting(plugin=None, setting=None)
    cfg.global_settings == {}


# Generated at 2022-06-12 20:58:17.025258
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting({'name': 'setting1'}, plugin=None)
    config_data.update_setting({'name': 'setting2'}, plugin={'type': 'type1', 'name': 'name1'})
    config_data.update_setting({'name': 'setting3'}, plugin={'type': 'type1', 'name': 'name2'})
    config_data.update_setting({'name': 'setting4'}, plugin={'type': 'type2', 'name': 'name1'})
    config_data.update_setting({'name': 'setting5'}, plugin={'type': 'type2', 'name': 'name2'})


# Generated at 2022-06-12 20:58:21.506527
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    a = ConfigData()
    a.update_setting("a")
    a.update_settings("b")
    a.get_settings()


# Generated at 2022-06-12 20:58:23.575711
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:58:25.274984
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('foo') is None


# Generated at 2022-06-12 20:58:25.890757
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass

# Generated at 2022-06-12 20:58:36.625522
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # create an instance of the class MyModule
    config_data = ConfigData()
    # create an instance of the class Setting
    setting = Setting('test_setting', ['test1', 'test2'], 'test2')
    # create an instance of the class Plugin
    plugin1 = Plugin(alias='test_plugin1', name='test_plugin1', type='module')
    # call the method update_setting
    config_data.update_setting(setting, plugin1)
    # check the method returns the expected result
    assert config_data._plugins['module']['test_plugin1']['test_setting'].name == 'test_setting'
    assert config_data._plugins['module']['test_plugin1']['test_setting'].default_value == 'test2'



# Generated at 2022-06-12 20:58:40.170545
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config = ConfigData()
    setting = Setting('foo', 'Settin1', 'Settin1 value')
    config.update_setting(setting)

    settings = config.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'foo'


# Generated at 2022-06-12 20:58:47.266570
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()

    # Test the method by adding global setting
    setting = {"module": "foo", "name": "bar"}
    cd.update_setting(setting)
    assert cd._global_settings["bar"] == setting

    # Test the method by adding plugin setting
    setting2 = {"module": "fizz", "name": "buzz"}
    plugin = {"type": "fizzbuzz", "name": "foobar"}
    cd.update_setting(setting2, plugin)
    assert cd._plugins["fizzbuzz"]["foobar"]["buzz"] == setting2


# Generated at 2022-06-12 20:58:59.637811
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    setting_fake_1 = Setting('fake_setting_1', 'fake_name', 'faker_value', 'fake_type')
    setting_fake_2 = Setting('fake_setting_2', 'fake_name', 'faker_value', 'fake_type')
    setting_fake_3 = Setting('fake_setting_3', 'fake_name', 'faker_value', 'fake_type')
    plugin = Plugin('fake_plugin', 'fake_plugin_type')
    plugin_2 = Plugin('fake_plugin_2', 'fake_plugin_type_2')
    config.update_setting(setting_fake_1, plugin)
    config.update_setting(setting_fake_2)
    config.update_setting(setting_fake_3, plugin_2)

# Generated at 2022-06-12 20:59:05.208330
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = PluginInfo()
    plugin.type = 'type'
    plugin.name = 'name'
    setting = 'setting'
    config_data.update_setting(setting, plugin)
    assert config_data._plugins['type']['name'][setting.name] == setting


# Generated at 2022-06-12 20:59:12.797515
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    config.update_setting(SettingNameValue('factprovider','somefactprovier','somesetting','somedefault','somevalue'))
    setting = config.get_setting('somesetting')
    assert setting is not None
    assert 'factprovider' == setting.plugin_type
    assert  'somefactprovier' == setting.plugin_name
    assert 'somesetting' == setting.name
    assert 'somedefault' == setting.default
    assert 'somevalue' == setting.value


# Generated at 2022-06-12 20:59:19.944610
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    plugin_1 = PluginInfo('test_plugin', 'test_type')
    plugin_2 = PluginInfo('test_plugin_2', 'test_type_2')
    setting = ConfigSetting('test_setting', 'test_value')
    setting_2 = ConfigSetting('test_setting_2', 'test_value_2')
    
    # check that plugin is None return global settings
    data.update_setting(setting)
    assert(data.get_settings() == [setting])

    # check that plugin is not None return specific settings
    data.update_setting(setting, plugin_1)
    assert(data.get_settings(plugin_1) == [setting])

    # check that the plugin not present return empty list
    assert(data.get_settings(plugin_2) == [])
    

#

# Generated at 2022-06-12 20:59:29.602297
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Test scenario 1: One plugin
    cfg_data = ConfigData()
    cfg_data.update_setting(Setting('a', 'b', 'c'))
    cfg_data.update_setting(Setting('d', 'e', 'f'))
    cfg_data.update_setting(Setting('g', 'h', 'i'))
    expected_settings = [Setting('a', 'b', 'c'), Setting('d', 'e', 'f'), Setting('g', 'h', 'i')]
    actual_settings = cfg_data.get_settings(Plugin(None, None))

    assert actual_settings == expected_settings

    # Test scenario 2: One plugin and one setting
    cfg_data = ConfigData()
    cfg_data.update_setting(Setting('a', 'b', 'c'))
   

# Generated at 2022-06-12 20:59:39.982889
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    import copy
    import unittest
    from unittest import mock

    from plugins.loader import PluginLoader
    from settings import ConfigurationSetting
    from settings import PluginConfigurationSetting

    class MockPlugin(object):

        def __init__(self, type, name, version, config=None):

            self.type = type
            self.name = name
            self.version = version

            self.config = config

    class TestPlugin(object):

        def __init__(self):
            pass

        def get_configuration_template(self):
            return {
                'TEST_SETTING': {
                    'description': 'Test setting',
                    'type': 'str',
                    'default': 'test_default'
                }
            }


# Generated at 2022-06-12 20:59:45.160380
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    plugin = Plugin("lookup", "ldap")
    config = ConfigData()
    setting1 = Setting("uri", "ldap://172.16.3.20")
    setting2 = Setting("basedn", "dc=myorg,dc=com")
    config.update_setting(setting1, plugin)
    config.update_setting(setting2, plugin)
    assert config.get_setting("uri", plugin) == setting1
    assert config.get_setting("basedn", plugin) == setting2

# Generated at 2022-06-12 20:59:52.783801
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.connection import ConnectionBase
    from ansible.plugins.cache import FactCache

    my_connection = {
        'name': 'my_connection',
        'type': ConnectionBase.__name__,
        'config_data': {'CONNECTION_DEBUG': False}
    }
    config_data.update_setting(ConnectionBase(**my_connection))
    my_fact_cache = {
        'name': 'my_fact_cache',
        'type': FactCache.__name__,
        'config_data': {'FACT_CACHE': False}
    }
    config_data.update_setting(FactCache(**my_fact_cache))

    plugin_loader = PluginLoader(config_data)


# Generated at 2022-06-12 21:00:01.845399
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class Plugin1(object):
        def __init__(self):
            self.type = 'L'
            self.name = 'M'

    class Setting1(object):
        def __init__(self):
            self.name = 'N1'

    class Setting2(object):
        def __init__(self):
            self.name = 'N2'

    config_data = ConfigData()

    setting1 = Setting1()
    config_data.update_setting(setting1)

    setting2 = Setting2()
    config_data.update_setting(setting2)

    assert len(config_data.get_settings()) == 2


# Generated at 2022-06-12 21:00:04.172222
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from ansible.plugins.loader import config
    setting = config.Setting('fact_caching', 'memory', cache='facts')
    config_data.update_setting(setting)


# Generated at 2022-06-12 21:00:16.112048
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting(): 
    # setup
    configData = ConfigData()
    plugin = Plugin('name')
    setting = Setting('setting', 'value', None)
    
    # execution
    configData.update_setting(setting,plugin)

    # assertion
    assert (configData.get_setting('setting', 'name') == setting)
    assert (configData.get_setting('setting') != setting)



# Generated at 2022-06-12 21:00:19.764784
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    global_settings = config_data.get_settings()
    assert len(global_settings) == 0

# Generated at 2022-06-12 21:00:23.939673
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint import Runner

    config_data = ConfigData()

    # setting 1
    config_data.update_setting(Runner._create_setting(None, 'ansible-lint', None, 'rulesdir', ['/etc/ansible-lint/rules']))

    # setting 2
    config_data.update_setting(Runner._create_setting(None, 'ansible-lint', None, 'excludefiles', ['/etc/ansible-lint/excludefiles']))

    # setting 3
    config_data.update_setting(Runner._create_setting(None, 'ansible-lint', None, 'skippaths', ['/etc/ansible-lint/skippaths']))

    # setting 4

# Generated at 2022-06-12 21:00:31.158740
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from units.mock.config import ConfigSetting

    # ConfigData object
    config_data = ConfigData()

    # set settings
    for setting in (ConfigSetting("setting1", "value"), ConfigSetting("setting2", "value")):
        config_data.update_setting(setting)

    assert len(config_data.get_settings()) == 2
    assert config_data.get_settings()[0].name == "setting1"
    assert config_data.get_settings()[1].name == "setting2"

# Generated at 2022-06-12 21:00:41.632963
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('test_setting_1', 'test_value'))
    config_data.update_setting(Setting('test_setting_2', 'test_value_2'))
    config_data.update_setting(Setting('test_setting_3', 'test_value_3'))
    config_data.update_setting(Setting('test_setting_4', 'test_value_4', plugin=Plugin('test_type', 'test_name')))
    config_data.update_setting(Setting('test_setting_5', 'test_value_5', plugin=Plugin('test_type', 'test_name')))

# Generated at 2022-06-12 21:00:51.754400
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansiblelint.rules import RulesCollection
    from ansiblelint.runner import Runner

    collection = RulesCollection()
    collection.register(DeprecatedModuleRule())
    config_data = ConfigData()
    runner = Runner(collection, config_data, [], [], [])

    assert len(config_data.get_settings()) == 1
    assert len(config_data.get_settings(plugin=runner)) == 1

    assert config_data.get_setting('deprecated_modules') is not None
    assert config_data.get_setting('deprecated_modules', runner) is not None

    collection.register(DeprecatedModuleRule())
    assert len(config_data.get_settings()) == 1
    assert len(config_data.get_settings(plugin=runner)) == 1


# Generated at 2022-06-12 21:01:03.108527
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    def mock_get_setting_global():
        config_data = ConfigData()
        setting = Setting()
        setting.name = 'plugins'
        setting.value = 'plugins/action,plugins/cache,plugins/callback,plugins/connection,plugins/filter'
        setting.scope = 'global'
        setting.plugin_type = None
        setting.plugin_name = None
        config_data.update_setting(setting)
        assert 'plugins' == config_data.get_setting('plugins')
        assert 'plugins/action,plugins/cache,plugins/callback,plugins/connection,plugins/filter' == config_data.get_setting(
            'plugins').value

    def mock_get_setting_plugin_not_exist():
        config_data = ConfigData()
        setting = Setting()
        setting.name = 'plugins'

# Generated at 2022-06-12 21:01:10.289206
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    setting_name1 = "ansible_connection"
    setting_value1 = "local"
    setting_plugin_name = "inventory"
    setting_plugin_type = "inventory"
    setting1 = Setting(setting_name1, setting_value1, None, None)
    configData.update_setting(setting1)
    plugin = Plugin(setting_plugin_type, setting_plugin_name)
    assert configData.get_setting(setting_name1) == setting1
    assert configData.get_setting(setting_name1, plugin) is None



# Generated at 2022-06-12 21:01:13.630260
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data_obj = ConfigData()
    config_data_obj.update_setting()
    assert config_data_obj._global_settings == {}


# Generated at 2022-06-12 21:01:16.850700
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('setting', 'test_value'))
    assert config_data.get_setting('setting') == 'test_value'


# Generated at 2022-06-12 21:01:42.440856
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """ Test the method get_settings of class ConfigData."""

    # Test arguments
    config_data = ConfigData()

    # Test basic case
    dummy_plugin = DummyPlugin()
    dummy_plugin.name = 'Dummy Plugin'
    dummy_plugin.type = 'dummy'

    dummy_setting = DummySetting()
    dummy_setting.name = 'Dummy Setting'
    dummy_setting.value = 'Dummy Value'

    config_data.update_setting(dummy_setting, dummy_plugin)

    test_settings = config_data.get_settings(dummy_plugin)

    assert len(test_settings) == 1
    assert test_settings[0].name == dummy_setting.name
    assert test_settings[0].value == dummy_setting.value

    # Test nothing added
    test_settings = config

# Generated at 2022-06-12 21:01:48.261021
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    result = None

    config_data = ConfigData()
    setting = {'name': 'test', 'value': 'test1'}

    result = config_data.update_setting(setting)

    assert setting == result


# Generated at 2022-06-12 21:01:59.388044
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert (config_data._global_settings == {})
    assert (config_data._plugins == {})
    config_data1 = ConfigData()
    assert (config_data1._global_settings == {})
    assert (config_data1._plugins == {})
    config_data1.update_setting('ansible.builtin', 'str', 'testing', 'testing_value')
    assert (config_data.get_setting('testing') == 'testing_value')
    plugin1 = Plugin('action', 'connect')
    config_data1.update_setting('ansible.action.connect', 'str', 'testing', 'testing_value', plugin1)
    assert (config_data1.get_setting('testing', plugin1) == 'testing_value')


# Generated at 2022-06-12 21:02:02.709943
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert len(config_data._global_settings) == 0

    config_data.update_setting("test", "test")
    assert len(config_data._global_settings) == 1


# Generated at 2022-06-12 21:02:09.604661
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.connection.ssh import Connection as SSHConnection

    config_data = ConfigData()
    config_data.update_setting(SSHConnection.shared_setting(
        'host'
    ))

    config_data.update_setting(SSHConnection.shared_setting(
        'port',
        default=22
    ))

    return config_data.get_settings()

print(test_ConfigData_update_setting())

# Generated at 2022-06-12 21:02:11.893013
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('host_key_checking') is None

# Generated at 2022-06-12 21:02:20.049588
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from files import ConfigData
    configdata = ConfigData()

    from files import C, C1, C2, C3, C4
    from files import S, S1, S2, S3, S4
    from files import R, R1, R2, R3, R4
    from files import DEFAULT

    plugin = C(name='name',
               type='type',
               file='file',
               enabled=True,
               interfaces=['a1', 'b2'],
               dependencies=['c3'])

    setting = S(name='name',
                plugin=plugin,
                value='value',
                category='category',
                context='context',
                scope='scope',
                password=False,
                default=DEFAULT)

    configdata.update_setting(setting)

# Generated at 2022-06-12 21:02:30.452047
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    settings = {
        'activation': 'auto',
        'timeout': 1,
        'retries': 42,
        'transport': 'ssh',
        'become': True,
        'become_method': 'sudo',
        'become_user': 'root',
        'check': True,
        'user': 'ansible',
        'port': 22
    }
    settings2 = {
        'activation': 'manual',
        'timeout': 2,
        'retries': 42,
        'transport': 'ssh',
        'become': True,
        'become_method': 'sudo',
        'become_user': 'root',
        'check': True,
        'user': 'ansible',
        'port': 22
    }

    config_data = ConfigData()


# Generated at 2022-06-12 21:02:35.790246
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('name', 'value'))

    settings = config_data.get_settings()

    assert len(settings) == 1
    assert settings[0].name == 'name'
    assert settings[0].value == 'value'



# Generated at 2022-06-12 21:02:44.011958
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    assert config_data.get_settings() == []
    assert config_data.get_settings(plugin=None) == []

    config_data.update_setting(Setting(name='foo', path='foo/bar'))
    assert config_data.get_settings()[0].name == 'foo'
    assert config_data.get_settings()[0].path == 'foo/bar'
    assert config_data.get_settings(plugin=None)[0].name == 'foo'
    assert config_data.get_settings(plugin=None)[0].path == 'foo/bar'

    config_data.update_setting(Setting(name='bar', path='bar/foo'),
                               plugin=Plugin('my_plugin', 'my_type'))

# Generated at 2022-06-12 21:03:24.180210
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting("enforce_deprecations") is None
    assert config_data.get_setting("enforce_deprecations", 'BAR') is None


# Generated at 2022-06-12 21:03:29.411183
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data_object = ConfigData()
    data_object.update_setting(name="AAAA",plugin=None)
    assert data_object._global_settings['AAAA'] is not None
    data_object2 = ConfigData()
    data_object2.update_setting(name="BBBB",plugin="plugins.name")
    assert data_object2._plugins['plugins']['name']['BBBB'] is not None
