

# Generated at 2022-06-12 20:53:31.901364
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    # Empty ConfigData
    assert cd.get_settings() == []

    class Plugin(object):
        def __init__(self):
            pass

        def __str__(self):
            return "Plugin"

    class Plugin(object):
        def __init__(self):
            self.type = "type"
            self.name = "name"

        def __str__(self):
            return "[%s] %s" % (self.type, self.name)

    # Invalid plugin
    assert cd.get_settings(Plugin()) == []

    # One global setting
    class Setting(object):
        def __init__(self):
            self.name = "name"

        def __str__(self):
            return str(self.name)

    setting = Setting()
    cd.update_

# Generated at 2022-06-12 20:53:38.576157
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()

    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.strategy import StrategyBase

    plugin = PluginLoader.get('strategy', 'linear').get('linear')
    setting = plugin.get_option('forks')

    setting.value = 100
    data.update_setting(setting)

    assert data.get_setting('forks') == setting
    assert data.get_settings() == [setting]


# Generated at 2022-06-12 20:53:48.268957
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint import AnsibleLintRule
    from ansiblelint.rules.LineTooLongRule import LineTooLongRule

    test_line_too_long_rule_setting = AnsibleLintRule(id='TEST001', shortdesc='Line length test shortdesc',
                                                     description='Line length test description',
                                                     severity='MEDIUM')
    test_line_too_long_rule = LineTooLongRule(80)
    test_line_too_long_rule_setting.plugin = test_line_too_long_rule

    test_config_data = ConfigData()
    test_config_data.update_setting(test_line_too_long_rule_setting)

    settings = test_config_data.get_settings(test_line_too_long_rule)

    assert settings[0] == test_

# Generated at 2022-06-12 20:53:50.562956
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    
    config_data = ConfigData()
    assert config_data.get_setting('var1') == None
    assert config_data.get_setting('var1', plugin='plugin1') == None


# Generated at 2022-06-12 20:53:55.887300
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    plugin_type = "ansible_local"
    plugin_name = "lookup_plugins"
    setting_name = "lookup_plugins"
    setting_value = ["/usr/share/ansible/plugins/lookup"]
    cd.update_setting(Setting(name=setting_name, value=setting_value), Plugin(type=plugin_type, name=plugin_name))
    setting = cd.get_setting(name=setting_name, plugin=Plugin(type=plugin_type, name=plugin_name))
    print("setting:", setting)

test_ConfigData_update_setting()

# Generated at 2022-06-12 20:54:08.041439
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create config data
    config_data = ConfigData()

    # Add some settings to the config data
    # Create global setting
    setting1 = SettingDefinition(
        'string',
        'option_one',
        'Option one',
        'The first option',
        default='A default value'
    )
    config_data.update_setting(setting1)

    # Create another global setting
    setting2 = SettingDefinition(
        'string',
        'option_two',
        'Option two',
        'The second option',
        default='Another default value'
    )
    config_data.update_setting(setting2)

    # Create a plugin setting

# Generated at 2022-06-12 20:54:18.518417
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('arg_spec','','','','','','',''))
    config_data.update_setting(Setting('action_plugins','','','','','','',''))
    assert len(config_data._global_settings) == 2

    config_data.update_setting(Setting('debug','','','','','','',''), Plugin('callback','debug'))
    config_data.update_setting(Setting('type','','','','','','',''), Plugin('callback','debug'))
    assert len(config_data._plugins['callback']['debug']) == 2


# Generated at 2022-06-12 20:54:26.432109
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cfg = ConfigData()
    cfg.update_setting(Setting('foo', 'bar'))
    assert cfg.get_setting('foo') == Setting('foo', 'bar')
    cfg.update_setting(Setting('foo', 'a'), Plugin('connection', 'foo'))
    assert cfg.get_setting('foo') == Setting('foo', 'bar')
    assert cfg.get_setting('foo', Plugin('connection', 'foo')) == Setting('foo', 'a')


# Generated at 2022-06-12 20:54:34.068593
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.cache.memory import CacheModule

    plugin_loader = PluginLoader()
    inventory_plugin = plugin_loader.get_plugin('inventory')
    cache_plugin = plugin_loader.all(class_only=True, cls=CacheModule)[0].plugin_object

    config_data = ConfigData()

    config_data.update_setting(cache_plugin.get_setting('timeout'))
    config_data.update_setting(inventory_plugin.get_setting('some_setting'), inventory_plugin)

    assert config_data.get_setting('timeout') is not None
    assert config_data.get_setting('some_setting', inventory_plugin) is not None

# Generated at 2022-06-12 20:54:36.777864
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = ConfigData()
    config_data.update_setting(setting)
    assert setting in config_data.get_settings()

# Generated at 2022-06-12 20:54:44.611731
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting = Setting('var1', 'value1')
    plugin = Plugin('myplugin', 'test', 'mytest')

    config.update_setting(setting)
    config.update_setting(setting, plugin)

    assert config.get_setting('var1') == setting
    assert config.get_setting('var1', plugin) == setting


# Generated at 2022-06-12 20:54:52.522712
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.loader import add_directory
    from ansible.module_utils.common.plugins import PluginConfigParser

    facts_config_path = '../../../plugins/facts/'
    add_directory(facts_config_path)
    plugin_loader = PluginLoader(config_data=ConfigData())

    # test adding a setting to the global settings
    plugin_loader._config_data.update_setting(name="test_setting", value="test value", plugin=None)
    assert plugin_loader._config_data._global_settings["test_setting"] == "test value"

    # test adding a setting to a defined plugin (setting_name, setting_value, plugin_type, plugin_name)
   

# Generated at 2022-06-12 20:55:00.306821
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    setting_1 = Setting('option_a', 'value_a')
    setting_2 = Setting('option_b', 'value_b')
    setting_3 = Setting('option_c', 'value_c')
    config.update_setting(setting_1)
    config.update_setting(setting_2, 'host_pattern')
    config.update_setting(setting_3, 'pattern')

    assert config.get_setting('option_a') == setting_1
    assert config.get_setting('option_b', 'host_pattern') == setting_2
    assert config.get_setting('option_c', 'pattern') == setting_3
    assert config.get_setting('option_a', 'pattern') is None
    assert config.get_setting('option_c', 'host_pattern') is None



# Generated at 2022-06-12 20:55:11.766943
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class Plugin(object):
        def __init__(self, name, type):
            self.name = name
            self.type = type

    # create an instance of ConfigData
    config_data = ConfigData()
    # create an instance of Setting
    setting1 = Setting(name='test_setting1')
    setting2 = Setting(name='test_setting2')
    plugin1 = Plugin(name='test_plugin1',type='test_type1')
    plugin2 = Plugin(name='test_plugin2',type='test_type2')
    # append a Setting to config_data
    config_data.update_setting(setting=setting1, plugin=None)
    assert setting1 in config_data.get_settings()
    assert setting1 in config_data.get_settings(plugin=None)
    assert setting1 in config_data

# Generated at 2022-06-12 20:55:18.069645
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert (cd.get_setting('ANSIBLE_FORKS') == None)
    cd.update_setting(Setting('ANSIBLE_FORKS', 100))
    assert (cd.get_setting('ANSIBLE_FORKS').name == 'ANSIBLE_FORKS')
    assert (cd.get_setting('ANSIBLE_FORKS').value == 100)
    plugin = Plugin('action', 'random_choice', 'foo')
    cd.update_setting(Setting('ANSIBLE_FORKS', 200, plugin))
    assert (cd.get_setting('ANSIBLE_FORKS').name == 'ANSIBLE_FORKS')
    assert (cd.get_setting('ANSIBLE_FORKS').value == 100)
    assert (cd.get_setting('ANSIBLE_FORKS', plugin).name == 'ANSIBLE_FORKS')

# Generated at 2022-06-12 20:55:22.192508
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    data.update_setting(ConfigSetting('test', 'type', 'desc'), ConfigPlugin('type', 'name'))
    assert len(data.get_settings()) == 0
    assert len(data.get_settings(ConfigPlugin('type', 'name'))) == 1

# Class used to represent plugin

# Generated at 2022-06-12 20:55:34.107787
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    # Setup
    config_data = ConfigData()
    config_data.update_setting(Setting(name="setting_1", plugin=None))
    config_data.update_setting(Setting(name="setting_2", plugin=Plugin(name="plugin_1", type="plugin_type_1")))
    config_data.update_setting(Setting(name="setting_2", plugin=Plugin(name="plugin_2", type="plugin_type_1")))
    config_data.update_setting(Setting(name="setting_3", plugin=Plugin(name="plugin_1", type="plugin_type_2")))

    # Test
    setting = config_data.get_setting("setting_1")
    assert setting is not None and setting.name == "setting_1" and setting.plugin is None

    setting = config_data.get_setting

# Generated at 2022-06-12 20:55:37.422718
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == len(config_data._global_settings)


# Generated at 2022-06-12 20:55:46.872155
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert cd.get_setting('foo') is None
    assert cd.get_settings() == []
    cd.update_setting('foo', PLUGIN_TYPE, PLUGIN_NAME)
    assert cd.get_setting('foo') == 'foo'
    assert cd.get_settings() == []
    cd.update_setting('bar', PLUGIN_TYPE, PLUGIN_NAME)
    assert cd.get_setting('bar') == 'bar'
    assert cd.get_settings() == []
    assert cd.get_setting('foo', PLUGIN_TYPE, PLUGIN_NAME) == 'foo'
    assert cd.get_setting('bar', PLUGIN_TYPE, PLUGIN_NAME) == 'bar'

# Generated at 2022-06-12 20:55:51.324813
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    from ansible.plugins.loader import get_all_plugin_loaders
    from collections import namedtuple
    PluginDescriptor = namedtuple('PluginDescriptor', 'type,name')
    for plugin_type in get_all_plugin_loaders():
        for plugin in plugin_type:
            settings = config_data.get_settings(PluginDescriptor(plugin_type.type, plugin))
            assert settings



# Generated at 2022-06-12 20:55:56.452871
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    data.update_setting(Setting('a', 'b', 'c'))
    assert data.get_setting('a').value == 'b'


# Generated at 2022-06-12 20:55:58.874227
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert not config_data.get_settings()


# Generated at 2022-06-12 20:56:03.020261
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = Setting(0, 'force_color', 'on')
    config_data.update_setting(setting)
    assert config_data.get_settings()[0] == setting
    assert config_data.get_setting('force_color') == setting


# Generated at 2022-06-12 20:56:09.302290
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    assert config_data.get_setting("ANSIBLE_CALLBACK_PLUGINS") is None

    config_data.update_setting(Setting("ANSIBLE_CALLBACK_PLUGINS", "test"))
    assert config_data.get_setting("ANSIBLE_CALLBACK_PLUGINS") is not None

    for setting in config_data.get_settings():
        assert type(setting) is Setting

    assert config_data.get_setting("ANSIBLE_CALLBACK_PLUGINS",
                                   Plugin("callback", "test")) is None
    print("test_ConfigData_get_setting: Pass")


# Generated at 2022-06-12 20:56:20.964495
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import plugin_loader

    cd = ConfigData()
    plugin = plugin_loader.find_plugin(None, 'action', 'test')
    assert plugin is not None

    # Assert: when there are no settings, the setting is added
    cd.update_setting(plugin.get_setting('test_setting'))
    assert cd.get_setting('test_setting') is not None
    print(cd.get_setting('test_setting'))

    # Assert: when the setting is already defined, the value is updated
    cd.update_setting(plugin.get_setting('test_setting'))
    print(cd.get_setting('test_setting'))
    assert cd.get_setting('test_setting').value == 'new_value'
test_ConfigData_update_setting()

# Generated at 2022-06-12 20:56:31.982577
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    assert config_data.update_setting({'name': 'ansible_python_interpreter'}, None) == True

    config_data = ConfigData({ 'name': 'ansible_python_interpreter' })

    assert config_data.update_setting({'name': 'foo'}, None) == True

    #config_data.update_setting('foo', 'bar', None)
    #config_data.update_setting('foo', 'bar', {'type': 'core', 'name': 'bar'})

    #assert config_data.get_setting('foo', None) == {'name': 'foo'}
    #assert config_data.get_setting('foo', {'type': 'core', 'name': 'bar'}) == {'name': 'foo'}



# Generated at 2022-06-12 20:56:40.409455
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    plugin = Plugin()
    plugin.type = "test_type"
    plugin.name = "test_name"

    setting = Setting()
    setting.name = "test_setting"
    setting.value = "test_value"

    setting1 = Setting()
    setting1.name = "test_setting1"
    setting1.value = "test_value1"

    config_data.update_setting(setting, plugin)
    assert config_data.get_setting(setting.name, plugin) == setting
    assert config_data.get_setting(setting1.name, plugin) == None


# Generated at 2022-06-12 20:56:51.796847
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()

    # Create a plugin
    plugin = Plugin('my_plugin', 'Test Plugin')
    plugin.version = '1.0'
    plugin.short_description = 'This is a test'

    # Create a setting
    setting = Setting('plugin_setting', 'Plugin Setting', plugin)
    setting.version = '1.0'
    setting.default = 'test'
    setting.description = 'A test plugin setting'
    setting.type = 'str'

    # Add setting to ConfigData object
    config.update_setting(setting)

    # Test that the Plugin exists in ConfigData object
    assert(plugin.name in config._plugins[plugin.type])
    assert(plugin.type in config._plugins)
    assert(plugin.name in config._plugins[plugin.type])

    # Test that the Setting exists in Config

# Generated at 2022-06-12 20:56:56.997261
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from unit.plugins.test.lib.config.objects import ConfigObject

    config_data = ConfigData()
    config_data.update_setting(ConfigObject('name1', 'value1'))
    config_data.update_setting(ConfigObject('name2', 'value2'))
    assert config_data.get_setting('name1') == ConfigObject('name1', 'value1')
    assert config_data.get_setting('name2') == ConfigObject('name2', 'value2')
    assert config_data.get_setting('name3') is None


# Generated at 2022-06-12 20:57:05.060801
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    assert data.get_setting('foo') is None

    data.update_setting(ConfigSetting(name='foo', type='integer', value=1, plugin=None))
    assert data.get_setting('foo') is not None

    data.update_setting(ConfigSetting(name='bar', type='integer', value=2,
                                      plugin=ConfigSettingPlugin(name='my_plugin', type='connection')))
    assert data.get_setting('foo', ConfigSettingPlugin(name='my_plugin', type='connection')) is None
    assert data.get_setting('bar', ConfigSettingPlugin(name='my_plugin', type='connection')) is not None


# Generated at 2022-06-12 20:57:20.406908
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()

    from ansible.plugins.action import ActionBase

    data.update_setting(Setting('a', '1', '', '', ActionBase, 'ping', ''), None)
    data.update_setting(Setting('b', '2', '', '', ActionBase, 'ping', ''), None)
    data.update_setting(Setting('c', '3', '', '', ActionBase, 'ping', ''), None)

    assert data._global_settings['a'] == Setting('a', '1', '', '', ActionBase, 'ping', '')
    assert data._global_settings['b'] == Setting('b', '2', '', '', ActionBase, 'ping', '')
    assert data._global_settings['c'] == Setting('c', '3', '', '', ActionBase, 'ping', '')


# Generated at 2022-06-12 20:57:22.254046
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:57:32.869611
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()

    setting = ConfigSetting('my_plugin', 'my_plugin_setting', 'my_plugin_value', 'my_plugin_type', 'my_plugin_config_file', 'my_plugin_option_name', 'my_plugin_section', 'my_plugin_section_key')
    config.update_setting(setting, 'my_plugin')

    setting = ConfigSetting('my_plugin', 'my_plugin_setting2', 'my_plugin_value2', 'my_plugin_type2', 'my_plugin_config_file2', 'my_plugin_option_name2', 'my_plugin_section2', 'my_plugin_section_key2')
    config.update_setting(setting, 'my_plugin')

    assert 2 == len(config.get_settings('my_plugin'))
    assert config.get

# Generated at 2022-06-12 20:57:35.784883
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    plugin_name = "my_plugin"
    plugin = Plugin(plugin_type=PluginType.DOCUMENTATION, name=plugin_name)
    data = ConfigData()
    assert not data.get_settings(plugin=plugin)



# Generated at 2022-06-12 20:57:45.525066
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data.get_setting("foo") is None

    config_data.update_setting(ConfigSetting("foo", "bar"))
    assert config_data.get_setting("foo") == ConfigSetting("foo", "bar")

    config_data.update_setting(ConfigSetting("baz", "bla"))
    assert config_data.get_setting("baz") == ConfigSetting("baz", "bla")
    assert config_data.get_setting("foo") == ConfigSetting("foo", "bar")

    config_data.update_setting(ConfigSetting("baz", "blub"))
    assert config_data.get_setting("baz") == ConfigSetting("baz", "blub")
    assert config_data.get_setting("foo") == ConfigSetting("foo", "bar")




# Generated at 2022-06-12 20:57:53.022057
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    d = ConfigData()
    print(d.get_setting("bar"))
    d.update_setting("foo")
    assert d.get_setting("bar") is None
    d.update_setting("bar")
    assert d.get_setting("bar") == "bar"

    assert d.get_setting("bar") == "bar"
    d.update_setting("baz", "baz")
    assert d.get_setting("baz", "baz") == "baz"
    assert d.get_setting("baz") == "bar"


# Generated at 2022-06-12 20:57:57.027181
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert [] == config_data.get_settings()
    assert [] == config_data.get_settings(None)
    assert [] == config_data.get_settings(dict(type=None, name=None))



# Generated at 2022-06-12 20:58:03.738774
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    s1 = Setting("s1", "global")
    s1.value=True
    config.update_setting(s1)

    s2 = Setting("s2", "plugin")
    s2.value=True
    s2.plugin.name="p1"
    s2.plugin.type="type1"
    config.update_setting(s2)

    s3 = Setting("s3", "plugin")
    s3.value=True
    s3.plugin.name="p1"
    s3.plugin.type="type1"
    config.update_setting(s3)

    s4 = Setting("s4", "plugin")
    s4.value=True
    s4.plugin.name="p2"
    s4.plugin.type="type1"

# Generated at 2022-06-12 20:58:07.545733
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = Plugin()
    plugin.name = 'test'
    plugin.type = 'core'
    setting = Setting()
    setting.name = 'test'
    setting.value = 'test'
    setting.scope = ['']
    setting.default = 'test'
    setting.type = 'test'
    setting.parsing_function = parse_test
    config_data.update_setting(setting)
    assert config_data.get_settings() == [setting]
    assert config_data.get_settings(plugin) == []


# Generated at 2022-06-12 20:58:13.639028
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    for s in [Setting(name="setting1", default=False, type='bool', scope="basic", plugin="Core"),
              Setting(name="setting2", default="abc", type='string', scope="basic", plugin="Core")]:
        cd.update_setting(s)

    assert(cd.get_setting("setting1") == s)
    assert(cd.get_setting("setting2") == s)



# Generated at 2022-06-12 20:58:31.083233
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    c = ConfigData()
    c.update_setting("alice")
    assert c.get_setting("alice") == "alice"

    d = ConfigData()
    d.update_setting("alice", plugin="bob")
    print(d.get_setting("alice"))
    with pytest.raises(NameError):
        d.get_setting("alice") == "alice"

    e = ConfigData()
    e.update_setting("alice", plugin=["bob", "a_type"])
    print(e.get_setting("alice"))
    with pytest.raises(NameError):
        e.get_setting("alice") == "alice"

# Generated at 2022-06-12 20:58:37.457729
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('test_setting', 'test_value', 'test description')
    plugin = Plugin('test_plugin_type', 'test_plugin_name', 'test_plugin_path')
    config_data.update_setting(setting, plugin)
    updated_setting = config_data.get_setting('test_setting', plugin)
    assert setting == updated_setting, 'Setting did not update properly'


# Generated at 2022-06-12 20:58:44.837816
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    from ansible.config.plugin import PluginConfig
    from ansible.config.setting import Setting

    setting_1 = Setting('setting_1', [], None, 'config.ini', 30, 30, 30)
    setting_2 = Setting('setting_2', [], None, 'config.ini', 31, 31, 31)
    setting_3 = Setting('setting_3', [], None, 'config.ini', 32, 32, 32)
    setting_4 = Setting('setting_4', [], None, 'config.ini', 33, 33, 33)
    setting_5 = Setting('setting_5', [], None, 'config.ini', 34, 34, 34)

    section_1 = 'test_section_1'
    key_1 = 'test_key_1'
    section_2 = 'test_section_2'
    key

# Generated at 2022-06-12 20:58:46.994056
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    setting = Setting('test_setting')
    data.update_setting(setting)
    settings = data.get_settings()
    assert 'test_setting' in settings



# Generated at 2022-06-12 20:58:57.194401
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_data = ConfigData()
    setting_global_1 = Setting('global_setting_1', 'No value set')
    setting_global_2 = Setting('global_setting_2', 'No value set')
    test_data.update_setting(setting_global_1)
    test_data.update_setting(setting_global_2)
    assert test_data._global_settings['global_setting_1'] == setting_global_1
    assert test_data._global_settings['global_setting_2'] == setting_global_2
    
    setting_plugin_local_1 = Setting('plugin_local_setting_1', 'No value set')
    setting_plugin_local_2 = Setting('plugin_local_setting_2', 'No value set')
    plugin_local = Plugin('local', 'shell')

# Generated at 2022-06-12 20:59:03.894056
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data_test = ConfigData()
    config_data_test.update_setting(Setting(name='foo', value='bar', origin='task', task_name='foobar'), plugin=None)
    config_data_test.update_setting(Setting(name='foo2', value='bar2', origin='task', task_name='foobar'), plugin=None)
    assert len(config_data_test._global_settings) == 2



# Generated at 2022-06-12 20:59:09.667500
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo', 'bar'))
    assert config_data.get_setting('foo') == config_data.get_settings()[0]
    assert config_data.get_setting('not_there') is None


if __name__ == "__main__":
    test_ConfigData_get_setting()

# Generated at 2022-06-12 20:59:18.255449
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    setting = {
        'name': 'ansible_module_generated_output_dir',
        'description': 'Directory where to generate the output from the Ansible module generation.',
        'default': 'generated_module'
    }
    config_data.update_setting(setting)

    # Test for global settings
    settings = config_data.get_settings()
    assert settings[0].default == 'generated_module'

    # Test for plugin settings
    from plugin import CppSettings, PluginType, Plugin
    plugin = Plugin(PluginType.HOOK, 'hook_test')

# Generated at 2022-06-12 20:59:28.592387
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create ConfigData instance and put some test data in it
    config_data = ConfigData()

    # Global settings
    setting = Setting('foo', 'bar')
    config_data.update_setting(setting)

    setting = Setting('hello', 'world')
    config_data.update_setting(setting)

    # Plugin settings
    setting = Setting('foo', 'baz', Plugin('test_plugin', 'test_type'))
    config_data.update_setting(setting)

    setting = Setting('hello', 'mars', Plugin('test_plugin', 'test_type'))
    config_data.update_setting(setting)

    #Unit test: get global settings
    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'foo'

# Generated at 2022-06-12 20:59:35.822356
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()
    plugin = AnsiblePlugin(type='runner', name='shell')
    setting = AnsibleSetting(name='ANSIBLE_SHELL_EXECUTABLE', value='/bin/bash')
    configdata.update_setting(setting, plugin)

    print(configdata.get_setting(setting.name, plugin))
    print(configdata.get_setting('ANSIBLE_RETRY_FILES_ENABLED',plugin))
    print(configdata.get_settings())
    print(configdata.get_settings(plugin))

if __name__ == '__main__':
    test_ConfigData_update_setting()

# Generated at 2022-06-12 20:59:49.955828
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from collections import namedtuple
    from packaging.version import Version
    from ansible.module_utils.six import string_types

    Plugin = namedtuple('Plugin', 'type,name')

    config_data = ConfigData()

    setting = Setting('setting', Option('x'), 'hi')
    config_data.update_setting(setting)

    assert config_data.get_setting('setting').value == 'hi'
    assert isinstance(config_data.get_setting('setting').value, string_types)
    assert config_data.get_setting('setting').value == setting.value

    setting2 = Setting('setting2', Option('{x}', version=Version('2.5')), 'hi')
    config_data.update_setting(setting2)

    setting3 = Setting('setting3', Option('x'), 'hi2')


# Generated at 2022-06-12 21:00:00.561461
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    test_data = ConfigData()

    assert len(test_data.get_settings()) == 0
    assert  len(test_data.get_settings(plugin=None)) == 0

    test_data.update_setting(Setting("test_name", None))
    test_data.update_setting(Setting("test_name", "test_plugin", "test_plugin_type"))

    assert len(test_data.get_settings()) == 1
    assert len(test_data.get_settings(plugin=None)) == 1

    test_data.update_setting(Setting("test_name2", None))
    test_data.update_setting(Setting("test_name2", "test_plugin", "test_plugin_type"))

    assert len(test_data.get_settings()) == 2

# Generated at 2022-06-12 21:00:04.237854
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config.update_setting(config_setting.ConfigSetting("test_setting_name", "test_setting_description"))
    assert config.get_setting("test_setting_name") == config_setting.ConfigSetting("test_setting_name", "test_setting_description")



# Generated at 2022-06-12 21:00:15.237310
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    import unittest
    import os
    import sys
    import platform
    import xunitparser
    import datetime
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.config.manager import (ConfigManager,
                                        Setting,
                                        BOOLEAN,
                                        CERT_VALIDATION_NONE,
                                        CERT_VALIDATION_REQUIRED,
                                        CONFIG_FILE_ENV_VARS,
                                        DEFAULTS,
                                        PRIVILEGE_ESCALATION_METHODS,
                                        )

    class TestConfigManager(unittest.TestCase):

        def setUp(self):

            self.config_data = ConfigData()

# Generated at 2022-06-12 21:00:26.757175
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # set up config data
    plugin = Plugin('', '', '', '')
    plugin2 = Plugin('', '', '', '')
    configdata = ConfigData()
    setting1 = Setting('', 'foo', '', '', None, None)
    setting2 = Setting('', 'bar', '', '', None, None)
    setting3 = Setting('', 'baz', '', '', None, None)

    # update the config data
    configdata.update_setting(setting1, plugin)
    configdata.update_setting(setting2, plugin2)
    configdata.update_setting(setting3)

    # check what the data looks like
    settings = configdata.get_settings(plugin)
    assert len(settings) == 1, 'ConfigData should contain zero settings'

# Generated at 2022-06-12 21:00:35.225364
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pathfinder = ConfigData()
    pathfinder.update_setting(Setting('action_plugins', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('callback_plugins', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('library', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('lookup_plugins', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('filter_plugins', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('vars_plugins', path='/foo/bar/baz'))
    pathfinder.update_setting(Setting('terminal_plugins', path='/foo/bar/baz'))

# Generated at 2022-06-12 21:00:45.015803
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansibullbot.wrappers.configsetting import ConfigSetting

    global_setting = ConfigSetting(name='bot_meta_dir', section='default', value=['/path/to/meta'])
    plugin_setting = ConfigSetting(name='add_issue_url', section='default', value=['http://jira.company.com'])

    plugin = {'type': 'botmeta', 'name': 'main'}

    config_data = ConfigData()

    config_data.update_setting(global_setting)
    config_data.update_setting(plugin_setting, plugin)

    assert config_data.get_setting('bot_meta_dir') == global_setting
    assert config_data.get_setting('add_issue_url') == plugin_setting

# Generated at 2022-06-12 21:00:53.285490
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    class Plugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name
    
    class Setting(object):
        def __init__(self, name, value, plugin):
            self.name = name
            self.value = value
            self.plugin = plugin

    # update global setting
    setting = Setting("abc", "abc", None)
    config_data.update_setting(setting)
    assert setting == config_data.get_setting("abc")
    assert setting == config_data.get_setting("abc", Plugin("foo", "bar"))
    assert setting == config_data.get_setting("abc", Plugin("baz", "qax"))

    # update plugin settings

# Generated at 2022-06-12 21:00:55.612176
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    mock_data = ConfigData()
    result = mock_data.get_setting('foo')
    assert result is None


# Generated at 2022-06-12 21:01:01.464529
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    from ansible.module_utils.common.validation import Validator, ValidationError, Entitlement
    def test_get_setting():
        config_data.get_setting('test')

    # Test that method get_setting does not throw an exception
    test_get_setting()



# Generated at 2022-06-12 21:01:15.534508
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert cd._global_settings == {}
    assert cd._plugins == {}
    assert cd.get_settings() == []
    assert cd.get_settings(None) == []

    setting = AnsibleConfigSetting(name='name', value='value', origin='playbook')
    cd.update_setting(setting)
    assert cd._global_settings == {'name': setting}
    assert cd._plugins == {}
    assert cd.get_settings() == [setting]
    assert cd.get_settings(None) == [setting]

    plugin = Plugin('lookup', 'first')
    setting = AnsibleConfigSetting(name='name', value='value', origin='playbook')
    cd.update_setting(setting, plugin)
    assert cd._global_settings == {'name': setting}

# Generated at 2022-06-12 21:01:17.962795
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()

    assert cd.get_settings() == []

    assert cd.get_settings(Plugin('core', 'vultr')) == []

# Generated at 2022-06-12 21:01:22.397790
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()
    settings = configData.get_settings()
    assert len(settings) == 0

    setting = Setting("name1")
    configData.update_setting(setting)
    settings = configData.get_settings()
    assert len(settings) == 1


# Generated at 2022-06-12 21:01:28.562256
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    config.update_setting(Setting('setting1', 'value1'))
    config.update_setting(Setting('setting2', 'value2'))
    assert config.get_settings() == [Setting('setting1', 'value1'), Setting('setting2', 'value2')]



# Generated at 2022-06-12 21:01:38.438231
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    from ansible.parsing.utils.addresses import parse_address
    from ansible.plugins.loader import PluginLoader
    import ansible.plugins.loader as plugin_loader

    connection = PluginLoader('Connection', 'local', config_data, '', None)
    connection_plugin = connection.get_plugin(parse_address('localhost'))

    connection_plugin.update_setting('foo', 'bar', value=1)
    assert config_data.get_setting('foo') == None
    assert config_data.get_setting('foo', plugin=connection_plugin) == None

    config_data.update_setting(connection_plugin.get_setting('foo'))

    assert config_data.get_setting('foo') == None

# Generated at 2022-06-12 21:01:45.241008
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    data.update_setting(Setting('name1', 'info1', 'global', 'type', 'name'))
    data.update_setting(Setting('name2', 'info2', 'global', 'type', 'name'))
    data.update_setting(Setting('name3', 'info3', 'global', 'type', 'name'))
    data.update_setting(Setting('name4', 'info4', 'global', 'type', 'name'))
    assert data.get_setting('name4') is not None
    assert data.get_setting('name4', Plugin('type', 'name')) is not None
    assert data.get_setting('name99') is None
    assert data.get_setting('name99', Plugin('type', 'name')) is None


# Generated at 2022-06-12 21:01:48.950663
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    settings


# Generated at 2022-06-12 21:01:53.519182
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    print("ConfigData unit test")
    configData = ConfigData()
    print("ConfigData successfully initialized")
    setting = Setting()
    print("Setting successfully initialized")
    configData.update_setting(setting)
    print("ConfigData:properly updated")


# Generated at 2022-06-12 21:01:55.822197
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    new_config = ConfigData()
    new_config.update_setting("hi")
    assert 1 == len(new_config._global_settings)


# Generated at 2022-06-12 21:02:05.861073
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()

    class test_plugin:
        def __init__(self):
            self.type = 'module'
            self.name = 'test_plugin'

    class test_setting(object):
        def __init__(self):
            self.name = 'test_name'
            self.value = 'test_value'
            self.origin = 'test_origin'
            self.plugin = test_plugin()
            self.scope = 'test_scope'

    setting = test_setting()
    data.update_setting(setting)

    assert data._global_settings == {setting.name: setting}
    assert data._plugins == {setting.plugin.type: {setting.plugin.name: {setting.name: setting}}}

    data._global_settings = {}
    data._plugins = {}

    data.update_setting

# Generated at 2022-06-12 21:02:21.341771
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Create test instances of the classes Plugin and PluginSetting
    from ansible.module_utils.ansible_release import __version__
    from ansible.plugins import module_loader, Plugin, PluginLoader
    class Foo(object):
        def __init__(self):
            self.foo = 'bar'
        def bar(self):
            pass

    class TestPlugin(Plugin):
        pass

    class TestPluginLoader(PluginLoader):
        pass

    plugin = TestPlugin()
    plugin._load_name = 'test_plugin'
    plugin._name = 'test_plugin'
    plugin._path = 'test_plugin'
    plugin._show_as = ['test_plugin']
    plugin.original_path = 'test_plugin'
    plugin.module_loader = module_loader
    plugin.plugin_loader = TestPluginLoader()
    plugin

# Generated at 2022-06-12 21:02:30.742413
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    plugin_rel = Plugin('plugin-relation', 'plugin-relation-test')
    plugin_dep = Plugin('plugin-dependency', 'plugin-dependency-test')

    config_data = ConfigData()

    # Update some settings
    config_data.update_setting(Setting(name="envvar", value="env", plugin=plugin_dep))
    config_data.update_setting(Setting(name="envvar", value="env", plugin=plugin_rel))
    config_data.update_setting(Setting(name="ini", value="ini", plugin=plugin_dep))
    config_data.update_setting(Setting(name="ini", value="ini", plugin=plugin_rel))

    # Check if the methods to get settings return the same settings
    assert (config_data.get_setting(name="envvar", plugin=None) is None)


# Generated at 2022-06-12 21:02:33.498341
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    import types
    assert type(config_data.update_setting) == types.MethodType

# Generated at 2022-06-12 21:02:38.824233
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from units.mock.loader import DictDataLoader
    from units.compat.mock import create_autospec
    from units.compat.mock import MagicMock
    from units.compat.mock import patch

    config_data = ConfigData()

    # Patch base class of  plugin to mock Plugin.get_setting method.
    plugin = create_autospec(MagicMock)
    plugin.type = 'module'
    plugin.name = 'yum'
    plugin.get_setting.return_value = None

    # Patch base class of  plugin to mock Plugin.get_settings method.
    plugin_2 = create_autospec(MagicMock)
    plugin_2.type = 'module'
    plugin_2.name = 'yum'

# Generated at 2022-06-12 21:02:45.069274
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    setting1 = Setting("key1", "value1")
    setting2 = Setting("key2", "value2")
    plugin = Plugin("type1", "name1")
    config_data = ConfigData()
    config_data.update_setting(setting1)
    config_data.update_setting(setting2, plugin)

    assert config_data.get_settings()[0].name == "key1"
    assert config_data.get_settings()[0].value == "value1"
    assert config_data.get_settings(plugin)[0].name == "key2"
    assert config_data.get_settings(plugin)[0].value == "value2"
    assert config_data.get_settings(Plugin("type2", "name2")) == []

# Generated at 2022-06-12 21:02:54.969753
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    conf = ConfigData()
    # Test global setting
    setting1 = ConfigSetting('var1', 'val1')
    conf.update_setting(setting1)
    assert conf._global_settings['var1'].name == 'var1'
    assert conf._global_settings['var1'].value == 'val1'

    # Test setting via plugin
    setting2 = ConfigSetting('var2', 'val2')
    plugin = Plugin('foo', 'bar')
    conf.update_setting(setting2, plugin)
    assert conf._plugins['foo']['bar']['var2'].name == 'var2'
    assert conf._plugins['foo']['bar']['var2'].value == 'val2'


# Generated at 2022-06-12 21:03:01.935543
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
	#Create empty object for class ConfigData
	config_data = ConfigData()
	
	#Create Setting object that will be added to the object config_data
	global_setting = Setting()
	global_setting.name = "somesetting"
	global_setting.plugin = None
	global_setting.plugin_type = None
	global_setting.plugin_name = None
	global_setting.value = "test"
	global_setting.origin = "file"
	
	#Update the Settings dictionary of config_data
	config_data.update_setting(global_setting, None)

	#Check if the method get_setting return the same setting that was added
	assert config_data.get_setting("somesetting", None) == global_setting
	

# Generated at 2022-06-12 21:03:03.725092
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    assert config_data.get_setting('foo') is None


# Generated at 2022-06-12 21:03:07.901944
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting('foobar') is None
    assert config.get_setting('foobar', object()) is None
    assert config.get_setting('foobar', object()) is None

# Generated at 2022-06-12 21:03:16.204105
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='foo', value='bar'))

    assert config_data.get_setting('foo') is not None
    assert config_data.get_setting('foo').value == 'bar'

    plugin = Plugin(type='foo', name='bar')
    config_data.update_setting(Setting(name='foo', value='bar'), plugin=plugin)

    assert config_data.get_setting('foo', plugin=plugin) is not None
    assert config_data.get_setting('foo', plugin=plugin).value == 'bar'
