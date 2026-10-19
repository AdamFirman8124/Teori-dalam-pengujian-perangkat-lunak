

# Generated at 2022-06-12 20:53:30.851659
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """Unit test for method get_settings"""

    data = ConfigData()
    assert len(data.get_settings()) == 0

# Generated at 2022-06-12 20:53:31.506118
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    obj = ConfigData()
    obj.update_setting()

# Generated at 2022-06-12 20:53:39.809804
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    # Missing plugin
    assert config_data.get_setting("random") is None
    assert config_data.get_setting("random", plugin=None) is None

    # Missing setting
    plugin = PluginInfo("type", "name")
    assert config_data.get_setting("random", plugin) is None

    # Valid setting
    setting = SettingInfo("name", "default", "path", "help")
    config_data.update_setting(setting)
    result_setting = config_data.get_setting("name", plugin)
    assert result_setting == setting


# Generated at 2022-06-12 20:53:49.223552
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()

    assert len(cd.get_settings()) == 0

    cd.update_setting(Setting(name='a', value='b'))

    assert len(cd.get_settings()) == 1
    assert len(cd.get_settings(plugin=SettingsPlugin(type='t', name='n'))) == 0

    cd.update_setting(Setting(name='c', value='d', plugin=SettingsPlugin(type='t', name='n')))

    assert len(cd.get_settings()) == 1
    assert len(cd.get_settings(plugin=SettingsPlugin(type='t', name='n'))) == 1

    cd.update_setting(Setting(name='e', value='f', plugin=SettingsPlugin(type='t', name='n')))

    assert len(cd.get_settings()) == 1
    assert len

# Generated at 2022-06-12 20:53:55.120699
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    config_data.update_setting(Setting('ansible_output_dir'))

    assert config_data._global_settings.get('ansible_output_dir') is not None

    config_data.update_setting(Setting('ansible_output_dir'), Plugin('ansible.console', 'console'))

    assert config_data._plugins['ansible.console']['console'].get('ansible_output_dir') is not None



# Generated at 2022-06-12 20:54:02.663871
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    # Test that update_setting of class ConfigData works as expected
    assert True
    data = ConfigData()
    setting = Setting(name="example_setting")
    data.update_setting(setting, plugin=Plugin("type", "name"))

    assert setting == data.get_setting("example_setting", Plugin("type", "name"))
    assert data.get_setting("example_setting") is None


# Generated at 2022-06-12 20:54:10.916416
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    config_data._global_settings = {'1.1': 1.1, '2.2': 2.2}

    config_data._plugins = {'type1':{'name1':{'1.1':1.1, '2.2':2.2}}, 'type2':{'name2':{'1.1':1.1, '2.2':2.2}}}

    assert config_data.get_setting('1.1') == 1.1
    assert config_data.get_setting('1.1', 'type1/name1') == 1.1
    assert config_data.get_setting('1.1', 'type2/name2') == 1.1

    assert config_data.get_setting('2.2') == 2.2
    assert config_data

# Generated at 2022-06-12 20:54:20.842865
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Test without plugin
    test_instance = ConfigData()
    assert test_instance.get_settings(plugin=None) == []

    # Test with unknown plugin type
    plugin = 'Unknown'
    assert test_instance.get_settings(plugin=plugin) == []

    # Test with unknown plugin
    plugin.type = 'Unknown'
    plugin.name = 'Unknown'
    assert test_instance.get_settings(plugin=plugin) == []

    # Test with existing plugin
    plugin.type = 'Test'
    plugin.name = 'Test'
    assert test_instance.get_settings(plugin=plugin) == []

    # Test with existing plugin and setting
    test_instance.update_setting(setting='Test')

# Generated at 2022-06-12 20:54:24.212977
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting = (None, "test_value")
    assert config_data.get_setting("test_name", None) is None
    config_data.update_setting(setting)
    assert config_data.get_setting("test_name", None) == setting

# Generated at 2022-06-12 20:54:34.474406
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import get_plugin_class

    global_settings = [{u'name': u'ANSIBLE_LIBRARY', u'value': u'/home/ansible/library'},
                       {u'name': u'ANSIBLE_FORKS', u'value': u'5'},
                       {u'name': u'ANSIBLE_ROLES_PATH', u'value': u'../../roles'},
                       {u'name': u'ANSIBLE_GATHER_TIMEOUT', u'value': u'60'}]


# Generated at 2022-06-12 20:54:40.670856
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = Mock()
    plugin = Mock()
    config_data.update_setting(setting, plugin)
    settings = config_data.get_settings(plugin)
    assert type(settings) is list and settings[0] == setting


# Generated at 2022-06-12 20:54:48.162100
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data.get_setting("module_setup") == None
    setting = Setting("module_setup", "false", "boolean")
    config_data.update_setting(setting)
    assert config_data.get_setting("module_setup").value == "false"
    setting = Setting("module_setup", "true", "boolean")
    config_data.update_setting(setting)
    assert config_data.get_setting("module_setup").value == "true"


# Generated at 2022-06-12 20:54:56.946571
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    setting = ConfigSetting('privilege_exec_level', 'privilege exec level 15')
    plugin = ConfigPlugin('ASA', 'CONFIG_ASA')

    config.update_setting(setting)
    config.update_setting(setting, plugin)

    print(config._global_settings)
    print(config._plugins)

if __name__ == '__main__':
    test_ConfigData_update_setting()

# Generated at 2022-06-12 20:55:05.016177
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ..plugin import Plugin, PluginSpec

    config_data = ConfigData()

    # test global settings
    setting = Plugin('foo', PluginSpec('action', 'standard', '', '', '', ''))
    config_data.update_setting(setting)

    settings = config_data.get_settings()
    assert(len(settings) == 1)
    assert(settings[0] == setting)

    settings = config_data.get_settings(setting)
    assert(len(settings) == 1)
    assert(settings[0] == setting)

    # test local settings
    setting = Plugin('foo', PluginSpec('action', 'standard', '', '', '', ''))
    config_data.update_setting(setting)

    settings = config_data.get_settings(setting)
    assert(len(settings) == 2)
   

# Generated at 2022-06-12 20:55:08.313892
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    settings_mgr = ConfigData()
    setting = dict(name='test', value='foo')
    settings_mgr.update_setting(setting)

    assert settings_mgr.get_setting('test') == setting


# Generated at 2022-06-12 20:55:15.723152
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0

    plugin = Plugin('my_cog', 'cog')
    config_data.update_setting(Setting('a', 'b', 'c', True), plugin)
    assert len(config_data.get_settings()) == 0

    assert len(config_data.get_settings(plugin)) == 1

    config_data.update_setting(Setting('a2', 'b2', 'c2', True), plugin)
    assert len(config_data.get_settings(plugin)) == 2

    assert config_data.get_settings(plugin)[0].value == 'b'
    assert config_data.get_settings(plugin)[1].value == 'b2'


test_ConfigData_get_settings()

# Generated at 2022-06-12 20:55:26.667432
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_config = ConfigData()
    from ansible.config.setting import Setting
    from ansible.config.ansible_config import AnsibleConfig
    from ansible.config.plugin import PluginLoader
    plugin = PluginLoader('lookup', 'ansible.plugins.lookup.file')
    test_setting = Setting(name='bar', value='bar_value', origin=AnsibleConfig('test'), plugin=plugin)
    test_config.update_setting(test_setting, plugin)
    test_setting = Setting(name='foo', value='foo_value', origin=AnsibleConfig('test'))
    test_config.update_setting(test_setting)

    assert test_setting.name in test_config._global_settings
    assert test_setting.value == test_config._global_settings[test_setting.name].value
   

# Generated at 2022-06-12 20:55:37.225196
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    # Case I. Plugin has a setting with the specified name
    # Case Ia. Plugin is a valid object
    #         Expect: Setting object is returned
    mock_plugin = "mock_plugin"
    config_data.update_setting("mock_setting", mock_plugin)
    assert mock_plugin == config_data.get_setting("mock_setting")
    # Case Ib. Passing in None as the plugin
    #         Expect: Setting object is not returned
    assert config_data.get_setting("mock_setting", None) is None
    # Case Ic. Plugin is not valid
    #         Expect: Setting object is not returned
    mock_plugin = "mock_plugin_(invalid)"
    assert config_data.get_setting("mock_setting", mock_plugin) is None
    #

# Generated at 2022-06-12 20:55:41.040018
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    setting = {'key':'value'}
    cd.update_setting(setting)

    assert cd.get_settings() == [{'key':'value'}]


# Generated at 2022-06-12 20:55:50.787704
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # GIVEN:
    import configparser

    plugin_1 = configparser.ConfigParser()
    plugin_1.add_section('defaults')
    plugin_1['defaults']['option_1'] = 'value_1'
    plugin_1['defaults']['option_2'] = 'value_2'
    plugin_1['defaults']['option_3'] = 'value_3'
    plugin_1['defaults']['option_4'] = 'value_4'
    plugin_type_1 = 'type_1'
    plugin_type_1_name_1 = 'name_1'
    plugin_type_1_name_2 = 'name_2'

    plugin_type_2 = 'type_2'
    plugin_type_2_name_1 = 'name_1'
   

# Generated at 2022-06-12 20:55:59.606580
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    test_config_data = [{'name':'test_config_data'}]
    config_data._global_settings = test_config_data
    assert config_data.get_settings() == test_config_data

# Generated at 2022-06-12 20:56:08.187491
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import PluginLoader
    from ansible_collections.ansible.netcommon.plugins.filter.network import ConfigurableBase

    test_values = [
        {
            'name': 'test',
            'value': 'test1'
        },
        {
            'name': 'test2',
            'value': 'test2'
        },
        {
            'name': 'test3',
            'value': 'test3'
        }
    ]

    test_data = ConfigData()

    for test_value in test_values:
        setting = ConfigurableBase.create(test_value)
        test_data.update_setting(setting)

    settings = test_data.get_settings()

    assert len(settings) == 3
    assert settings[0].name == 'test'
    assert settings

# Generated at 2022-06-12 20:56:18.441073
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    from ansible.plugins.vars import BaseVars
    from ansible.utils.vars import combine_vars
    from ansible.plugins.config import Config

    type = 'vars'
    name = 'foo'
    file = '/path/to/foo.yml'
    plugin = BaseVars(type, name, file)

    data = ConfigData()

    data.update_setting(Config('foo', 'bar', 'baz'), plugin)
    setting = data.get_setting(name, plugin)

    assert setting.name == 'foo'
    assert setting.value == 'baz'
    assert setting.priority == 'baz'


# Generated at 2022-06-12 20:56:22.887555
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting(Setting(name='test_setting'))
    settings_list = cd.get_settings()
    assert(len(settings_list) == 1)
    assert(settings_list[0].name == 'test_setting')


# Generated at 2022-06-12 20:56:29.748297
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(
        name='timeout',
        value='10',
        type='int',
        plugin=ConfigPlugin(
            name='Copy',
            type=ConfigPlugin.ACTION,
            module='modules.core.copy',
            class_name='ActionModule',
            parent=None)
    ))

    assert config_data._global_settings['timeout'].name == 'timeout'


# Generated at 2022-06-12 20:56:41.129625
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    setting = Setting('name', 'value', 'comment', 'TEST')

    config_data.update_setting(setting)

    assert config_data.get_setting(setting.name).name == setting.name
    assert config_data.get_setting(setting.name).value == setting.value
    assert config_data.get_setting(setting.name).comment == setting.comment
    assert config_data.get_setting(setting.name).tag == setting.tag

    assert config_data.get_setting('name', 'TEST').name == setting.name
    assert config_data.get_setting('name', 'TEST').value == setting.value
    assert config_data.get_setting('name', 'TEST').comment == setting.comment

# Generated at 2022-06-12 20:56:43.656852
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0


# Generated at 2022-06-12 20:56:53.964017
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from units.mock.loader import DictDataLoader

    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.inventory import InventoryPlugin

    # create mock config data class
    config_data = ConfigData()

    # create settings for test
    test_settings = {
        'foo': 'bar',
        'baz': 'moo'
    }

    # create global settings
    for k, v in test_settings.items():
        config_data.update_setting(Setting(k, v))

    # create settings for plugins
    data_loader = DictDataLoader({'/etc/ansible/hosts': 'mock_content', '/etc/ansible/ansible.cfg': 'mock_content'})

# Generated at 2022-06-12 20:57:05.693732
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from collections import namedtuple

    Plugin = namedtuple('Plugin', ['type', 'name'])

    config = ConfigData()
    plugin_1 = Plugin(type='foo', name='bar')

    assert config.get_setting('setting1') is None
    assert config.get_setting('setting1', plugin_1) is None
    config.update_setting(Setting('setting1', 'value1', 'path1'))
    assert config.get_setting('setting1') is not None
    assert config.get_setting('setting1', plugin_1) is None

    config.update_setting(Setting('setting2', 'value2', 'path2'), plugin_1)
    assert config.get_setting('setting2') is None
    assert config.get_setting('setting2', plugin_1) is not None



# Generated at 2022-06-12 20:57:09.964451
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    setting = {}
    setting['name'] = 'retryfiles_save_path'
    setting['value'] = '/home/<username>/.ansible/retry_files'
    setting['section'] = 'defaults'
    setting['plugin'] = None
    config.update_setting(setting)

    assert config._global_settings['retryfiles_save_path'] == setting


# Generated at 2022-06-12 20:57:19.200052
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings(plugin=None)
    assert(settings == [])
    settings = config_data.get_settings(Plugin("filter", "lookup"))
    assert(settings == [])


# Generated at 2022-06-12 20:57:26.408530
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data_instance = ConfigData()
    assert len(config_data_instance._global_settings) == 0
    assert len(config_data_instance._plugins) == 0
    # create test setting
    class TestSetting():
        def __init__(self, name, value):
            self.name = name
            self.value = value

    test_setting = TestSetting('test_setting', 'test_value')
    config_data_instance.update_setting(test_setting)
    assert len(config_data_instance._global_settings) == 1
    assert len(config_data_instance._plugins) == 0
    # create test plugin
    class TestPlugin():
        def __init__(self, type, name):
            self.type = type
            self.name = name


# Generated at 2022-06-12 20:57:36.272979
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    class Plugin(object):

        def __init__(self, type, name):
            self.type = type
            self.name = name

    class Setting(object):

        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

    plugin_one = Plugin(type='foo', name='bar')
    plugin_two = Plugin(type='foo', name='baz')
    plugin_three = Plugin(type='foo', name='qux')
    plugin_four = Plugin(type='foo', name='spam')

    setting_one = Setting(name='eggs', value='ham')

# Generated at 2022-06-12 20:57:46.301320
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    plugin1 = Plugin('cache', 'memory')
    plugin2 = Plugin('persistent_cache', 'json_file')
    config_data = ConfigData()

    assert config_data.get_setting('timeout', plugin1) == None
    assert config_data.get_setting('timeout', plugin2) == None

    s = Setting('timeout', 300)
    config_data.update_setting(s)
    assert config_data.get_setting('timeout') == s

    s = Setting('timeout', 30)
    config_data.update_setting(s, plugin1)
    assert config_data.get_setting('timeout') == Setting('timeout', 300)
    assert config_data.get_setting('timeout', plugin1) == s
    assert config_data.get_setting('timeout', plugin2) == None

# Generated at 2022-06-12 20:57:56.854143
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cfg = ConfigData()

    assert len(cfg.get_settings()) == 0

    from ansible.cli.arguments import Setting
    cfg.update_setting(Setting("asdf", ["asdf"]))
    assert len(cfg.get_settings()) == 1

    cfg.update_setting(Setting("fdsa", ["fdsa"]))
    assert len(cfg.get_settings()) == 2
    cfg._global_settings.clear()

    import ansible.plugins
    from ansible.plugins.connection import ConnectionBase

    plugin = ansible.plugins.connection.ConnectionBase()
    cfg.update_setting(Setting("asdf", ["asdf"]), plugin)
    assert len(cfg.get_settings()) == 1

    plugin.name = "fdsa"

# Generated at 2022-06-12 20:58:02.620164
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Setting(object):
        def __init__(self,name):
            self.name = name
    config_data = ConfigData()
    setting = Setting('name')
    config_data.update_setting(setting)
    assert config_data._global_settings == {'name':setting}, "config_data._global_settings should be {'name':setting}"


# Generated at 2022-06-12 20:58:10.106629
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Setup
    global_setting_1 = Setting(name="key 1", plugin=None)
    global_setting_2 = Setting(name="key 2", plugin=None)
    setting_1 = Setting(name="key 3", plugin=Plugin(name="name 1", type="type 1"))
    setting_2 = Setting(name="key 4", plugin=Plugin(name="name 1", type="type 1"))
    setting_3 = Setting(name="key 5", plugin=Plugin(name="name 2", type="type 2"))
    config_data = ConfigData()
    config_data.update_setting(global_setting_1)
    config_data.update_setting(global_setting_2)
    config_data.update_setting(setting_1)
    config_data.update_setting(setting_2)
    config_data.update_

# Generated at 2022-06-12 20:58:14.527984
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting('setting_A')
    config_data.update_setting('a', 'plugin_B')
    assert config_data.get_setting('setting_A') == 'setting_A'
    assert config_data.get_setting('a', 'plugin_B') == 'a'


# Generated at 2022-06-12 20:58:21.163520
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    global_settings = ConfigData().get_settings()
    assert global_settings == []

    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

    class Setting:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    settings = []
    settings.append(Setting('foo', 'bar'))
    settings.append(Setting('bar', 'foo'))

    config = ConfigData()
    config.update_setting(settings[0])
    config.update_setting(settings[1])

    plugin = Plugin('type', 'name')

    assert config.get_settings() == settings
    assert config.get_settings('test') == []
    assert config.get_settings(plugin) == []

# Generated at 2022-06-12 20:58:22.867149
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    # Create a ConfigData object
    config_data = ConfigData()

    # Add a setting to the object
    setting = Sett

# Generated at 2022-06-12 20:58:34.334885
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    d = ConfigData()
    s = ConfigSetting("test","test")
    d.update_setting(s)
    s = d.get_setting("test")
    assert s.value == "test"


# Generated at 2022-06-12 20:58:40.787973
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    import ansible.config.setting as setting
    import ansible.config.constants as C

    # create default config data
    config_data = ConfigData()

    # create a fake config setting
    s = setting.Setting(C.CONFIG_DEFAULT_SECTION, 'fake_setting', 'fake_value')

    # update it in config data
    config_data.update_setting(s)

    # check if it matches
    s2 = config_data.get_setting('fake_setting')
    assert s2 == s


# Generated at 2022-06-12 20:58:48.808968
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin_type = 'my_plugin_type'
    plugin_name = 'my_plugin_name'

    # Case 1: there is no setting in the data
    setting = config_data.get_setting('my_setting')
    # expecting setting is None
    assert setting is None

    # Case 1: plugin is None and there is one setting in the data
    plugin = None
    config_data.update_setting('my_setting', plugin)
    setting = config_data.get_setting('my_setting', plugin)
    # expecting setting is 'my_setting'
    assert setting == 'my_setting'

    # Case 2: there is one setting in the data
    plugin = Plugin(plugin_type, plugin_name)
    config_data.update_setting('my_setting', plugin)
    setting

# Generated at 2022-06-12 20:58:58.195525
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    from ansible.plugins.loader import PluginLoader
    plugin_loader = PluginLoader()
    all_plugin_names = plugin_loader.all_plugin_names
    config_data = ConfigData()
    for plugin in all_plugin_names:
        plugin_setting = plugin_loader.setting_info[plugin]
        plugin_type = plugin_setting['type']
        plugin_name = plugin_setting['name']
        plugin_namespace = plugin_setting['namespace']
        plugin_class = plugin_loader.get(plugin_type, plugin_name)
        plugin_instance = plugin_class(plugin_name, plugin_namespace, plugin_settings={}, plugin_options={})
        from ansible.plugins.loader import get_all_plugin_loaders

# Generated at 2022-06-12 20:59:03.979276
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    
    config = ConfigData()
    setting = Setting('test', 'test', 'test')
    config.update_setting(setting)
    result = config.get_setting('test')
    if result == setting:
       print("Unit test for ConfigData.get_setting() succeeded")
    else:
       print("Unit test for ConfigData.get_setting() failed")


# Generated at 2022-06-12 20:59:14.720721
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    config_data.update_setting(Setting("foo", "foo plugin"))
    assert config_data.get_setting("foo") != None
    assert config_data.get_setting("foo", Plugin("foo", "foo plugin")) == None
    assert config_data.get_setting("foo", Plugin("bar", "bar plugin")) == None

    config_data.update_setting(Setting("bar", "foo plugin"), Plugin("foo", "foo plugin"))
    assert config_data.get_setting("bar") == None
    assert config_data.get_setting("bar", Plugin("foo", "foo plugin")) != None
    assert config_data.get_setting("bar", Plugin("bar", "bar plugin")) == None


# Generated at 2022-06-12 20:59:19.302578
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('explanation', 'my explanation'))
    # This should return the Setting object with name 'explanation'
    assert config_data.get_setting('explanation') == Setting('explanation', 'my explanation')


# Generated at 2022-06-12 20:59:23.410569
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='foo', value='bar'))
    assert(config_data.get_setting('foo') == Setting(name='foo', value='bar'))
    assert(config_data.get_setting('bar') is None)


# Generated at 2022-06-12 20:59:28.302047
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config = ConfigData()
    fake_setting = Setting()
    fake_setting.name = 'foo'
    fake_setting.value = 'baz'

    # pylint: disable=protected-access
    config._global_settings[fake_setting.name] = fake_setting
    settings = config._global_settings

    assert config.get_settings()[0].value == 'baz'


# Generated at 2022-06-12 20:59:33.039368
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('setting1', 'value1'))
    config_data.update_setting(Setting('setting2', 'value2'))

    assert config_data.get_settings() == [
        Setting('setting1', 'value1'),
        Setting('setting2', 'value2')
    ]


# Generated at 2022-06-12 20:59:55.194790
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    name = "unittest_setting2"
    path = "unittest"
    value = True
    setting = ConfigSetting(name, value, path)
    config_data.update_setting(setting)

    settings = config_data.get_settings()

    assert len(settings) == 1
    assert settings[0] == setting


# Generated at 2022-06-12 21:00:03.896840
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """test_ConfigData_get_settings"""

    config_data = ConfigData()

    setting_1 = Setting(name='setting_1', value='setting_1_value')
    setting_2 = Setting(name='setting_2', value='setting_2_value', origin='file_1')
    setting_3 = Setting(name='setting_3', value='setting_3_value')
    setting_4 = Setting(name='setting_4', value='setting_4_value', origin='file_2')
    setting_5 = Setting(name='setting_5', value='setting_5_value', origin='file_3')
    setting_6 = Setting(name='setting_6', value='setting_6_value')
    setting_7 = Setting(name='setting_7', value='setting_7_value', origin='file_2')



# Generated at 2022-06-12 21:00:11.274442
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configData.update_setting(setting=Setting(name="key1",value="value1"))
    configData.update_setting(setting=Setting(name="key2", value="value2"))
    assert configData._global_settings["key1"].value == "value1"
    assert configData._global_settings["key2"].value == "value2"


# Generated at 2022-06-12 21:00:14.547573
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    settings_config_data = ConfigData()
    setting = {}
    setting['name'] = 'setting1'
    setting['value'] = 10

    settings_config_data.update_setting(setting)

    assert settings_config_data.get_setting('setting1') == setting


# Generated at 2022-06-12 21:00:15.393084
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    assert True

# Generated at 2022-06-12 21:00:25.055981
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('test', 'string'))
    assert config_data.get_setting('test').name == 'test'
    assert config_data.get_setting('test').type == 'string'

    config_data.update_setting(Setting('test', 'string'), Plugin('cache', 'connection', 'redis'))
    assert config_data.get_setting('test', Plugin('cache', 'connection', 'redis')).name == 'test'
    assert config_data.get_setting('test', Plugin('cache', 'connection', 'redis')).type == 'string'



# Generated at 2022-06-12 21:00:31.756710
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_setting = {'name': 'hostname', 'value': 'localhost', 'kv': {'hostname': 'localhost'}}
    plugin_setting = {'name': 'hostname', 'value': 'localhost', 'kv': {'hostname': 'localhost'}}
    cd = ConfigData()
    cd.update_setting(Setting(global_setting))
    cd.update_setting(Setting(plugin_setting), plugin=Plugin({'name': 'test', 'type': 'test_type'}))

    print("test_ConfigData_update_setting: global_setting: {0}".format(global_setting))
    print("test_ConfigData_update_setting: plugin_setting: {0}".format(plugin_setting))

# Generated at 2022-06-12 21:00:34.989387
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    plugin = Plugin('action', 'await_file')
    setting = Setting(plugin, 'path', '/path/should/be/True/or/False', '/path/should/be/True/or/False')
    configData.update_setting(setting, plugin)
    assert(configData.get_setting('path', plugin) == setting)


# Generated at 2022-06-12 21:00:40.780713
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    class plugin:
        pass

    a = plugin()
    a.type = 'connection'
    a.name = 'basic'
    config_data.update_setting(a)

    print(config_data.get_settings(a))
    assert config_data.get_settings() == []


# Generated at 2022-06-12 21:00:42.560816
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(setting=None, plugin=None)


# Generated at 2022-06-12 21:01:03.640064
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert isinstance(config_data, ConfigData)

    config_data.update_setting(Setting('setting1', 'value1', 'string', []))
    assert config_data.get_setting('setting1') != None 



# Generated at 2022-06-12 21:01:12.236507
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    data.update_setting(Setting(name='foo', value='bar'))
    data.update_setting(Setting(name='baz', value='quxx', plugin=Plugin(type='v1', name='x'), origin='y'))
    data.update_setting(Setting(name='quox', value='quuz', plugin=Plugin(type='v1', name='x')))
    data.update_setting(Setting(name='bam', value='baz', plugin=Plugin(type='v2', name='y')))
    data.update_setting(Setting(name='zam', value='zaz', plugin=Plugin(type='v2', name='z')))

    settings = data.get_settings()
    assert len(settings) == 1 and settings[0].name == 'foo'

    settings = data

# Generated at 2022-06-12 21:01:22.729945
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    # test scenario 1
    # About: Adding a new setting to global config data
    setting = ConfigSetting('test_setting')
    setting.value = 'value'
    setting.origin = 'test'
    config_data.update_setting(setting)
    assert config_data.get_setting('test_setting').value == 'value'
    assert config_data.get_setting('test_setting').origin == 'test'

    # test scenario 2
    # About: Adding a new setting to config data of type_1 plugin
    setting = ConfigSetting('test_setting')
    setting.value = 'value'
    setting.origin = 'test'
    config_data.update_setting(setting, Plugin('type_1', 'name_1'))

# Generated at 2022-06-12 21:01:34.220109
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_config_data = ConfigData()

    # Mock global setting
    global_setting = {
        'name': 'test_setting',
        'value': 'test_value',
        'origin': 'test_origin',
        'plugin': {
            'name': 'test_plugin',
            'type': 'test_plugin_type'
        }
    }

    test_config_data.update_setting(global_setting)
    assert test_config_data._global_settings[global_setting['name']] == global_setting
    assert test_config_data.get_setting(global_setting['name']) == global_setting
    assert test_config_data.get_setting(global_setting['name'], plugin=global_setting['plugin']) == global_setting

    # Mock plugin setting

# Generated at 2022-06-12 21:01:42.930404
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    c = ConfigData()
    assert c.get_setting("ANSIBLE_HOST_KEY_CHECKING") is None

    from ansible.module_utils.common._collections_compat import MutableMapping
    import copy
    import os
    import sys

    s = {}
    s.update(os.environ)
    s.update(sys.__dict__)

    class Prefix:
        def __getitem__(self, key):
            return 'ANSIBLE_' + key

    pref = Prefix()
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/constants.py#L174

# Generated at 2022-06-12 21:01:55.993418
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()

    # Test empty config
    assert config.get_setting('setting') is None

    # Test unknown setting
    config._global_settings = {'setting': {'name': 'setting', 'value': 'value'}}
    assert config.get_setting('setting2') is None

    # Test unknown plugin
    config._global_settings = {}
    config._plugins = {}
    assert config.get_setting('setting2', {
        'type': 'foo',
        'name': 'bar'
    }) is None

    # Test unknown type in plugin
    config._global_settings = {}
    config._plugins = {
        'foo': {
            'bar': {
                'setting': {'name': 'setting', 'value': 'value'}
            }
        }
    }
    assert config.get_setting

# Generated at 2022-06-12 21:02:05.958448
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint.rules.rules_loader import RulesCollection
    from ansiblelint.rules.rules_loader import get_plugin_type

    configdata = ConfigData()
    configdata.update_setting(
        Setting('foo', 'bar'),
        None)
    assert configdata.get_setting('foo') == Setting('foo', 'bar')
    assert configdata.get_setting('foo', None) == Setting('foo', 'bar')
    assert configdata.get_setting('foo', get_plugin_type('AnsibleLintRule')) == Setting('foo', 'bar')

    configdata.update_setting(
        Setting('foo', 'bar', 'AnsibleLintRule', 'ANSIBLE0004'),
        RulesCollection('ANSIBLE0004'))

# Generated at 2022-06-12 21:02:11.976872
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    instance = ConfigData()
    setting = Setting('test_setting', 'test value', plugin=Plugin('test_plugin', 'test_type'))
    instance.update_setting(setting)
    assert instance.get_setting('test_setting', plugin=Plugin('test_plugin', 'test_type')) == setting
    assert instance.get_setting('test_setting') == None


# Generated at 2022-06-12 21:02:18.099015
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(TestSetting("foo"))
    assert config_data.get_setting("foo").value == "bar"

    config_data.update_setting(TestSetting("foo", "baz"), TestPlugin("my_plugin", "foo"))
    assert config_data.get_setting("foo").value == "bar"
    assert config_data.get_setting("foo", TestPlugin("my_plugin", "foo")).value == "baz"



# Generated at 2022-06-12 21:02:28.181803
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from units.mock.loader import DummyCatalog

    # test for global config
    config_data = ConfigData()
    config_data.update_setting(DummyCatalog.GLOBAL_CONFIG)
    assert config_data.get_setting('default_action_plugin') == DummyCatalog.GLOBAL_CONFIG

    # test for plugin config
    config_data.update_setting(DummyCatalog.MODULE_PLUGIN_CONFIG['action']['ping'])
    assert config_data.get_setting('default_action_plugin', DummyCatalog.PLUGIN_CATALOG_ACTION['ping']) == DummyCatalog.MODULE_PLUGIN_CONFIG['action']['ping']

# Generated at 2022-06-12 21:03:13.123363
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting(ConfigSetting('setting1', 'value1', 'string', None))
    cd.update_setting(ConfigSetting('setting2', 'value2', 'string', None))
    cd.update_setting(ConfigSetting('setting3', 'value3', 'string', Plugin('plugin1', 'connection')))
    cd.update_setting(ConfigSetting('setting4', 'value4', 'string', Plugin('plugin2', 'callback')))

    assert(len(cd.get_settings()) == 2)
    for setting in cd.get_settings():
        assert(isinstance(setting,ConfigSetting))

    assert(len(cd.get_settings(Plugin('plugin1', 'connection'))) == 1)
    assert(len(cd.get_settings(Plugin('plugin2', 'callback'))) == 1)


# Generated at 2022-06-12 21:03:16.469061
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    c = ConfigData()
    s = Setting('a', 'b')
    c.update_setting(s)
    ns = c.get_settings()
    assert(s == ns[0])

test_ConfigData_get_settings()

# Generated at 2022-06-12 21:03:20.150406
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    from ansible.plugins.loader import load_plugin
    plugin = load_plugin('connection', 'local')
    ret = data.get_settings(plugin)
    print(ret)


if __name__ == '__main__':
    test_ConfigData_get_settings()

# Generated at 2022-06-12 21:03:24.654536
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting1 = Setting('g_name1', 'g_value1')
    config_data.update_setting(setting1)

    plugin1 = Plugin('i1', 'c1')
    setting2 = Setting('name2', 'value2')
    config_data.update_setting(setting2, plugin1)

    assert config_data.get_setting(setting1.name) == setting1
    assert config_data.get_setting(setting2.name, plugin1) == setting2


# Generated at 2022-06-12 21:03:26.063988
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 21:03:28.932275
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configData.update_setting('setting', 'plugin')
    assert configData._global_settings == {'setting': 'plugin'}
