

# Generated at 2022-06-12 20:53:32.629045
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting(Setting('name1', 'type1', 'value1'))
    cd.update_setting(Setting('name2', 'type1', 'value2'))
    cd.update_setting(Setting('name3', 'type2', 'value3'))
    assert cd.get_setting('name1') == Setting('name1', 'type1', 'value1')
    assert cd.get_setting('name1').value == 'value1'
    assert cd.get_setting('name2').value == 'value2'
    assert cd.get_setting('name3').value == 'value3'
    assert cd.get_settings('type1')[0].value == 'value1'
    assert cd.get_settings('type1')[1].value == 'value2'

# Generated at 2022-06-12 20:53:43.239715
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()
    assert len(config._global_settings) == 0, "global_settings should be empty"
    assert len(config._plugins) == 0, "plugins should be empty"

    setting1 = Setting("name", "value", "string", "")
    config.update_setting(setting1)
    assert len(config._global_settings) == 1, "global_settings should have 1 entry"
    assert len(config._plugins) == 0, "plugins should be empty"
    assert config._global_settings["name"].name == "name", "name should be 'name'"
    assert config._global_settings["name"].value == "value", "value should be 'value'"
    assert config._global_settings["name"].type == "string", "type should be 'string'"

# Generated at 2022-06-12 20:53:47.036334
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config.update_setting('plugin.class', plugin='plugin.name')

    assert config.get_setting('plugin.class', plugin='plugin.name') is not None
    assert config.get_setting('plugin.class', plugin='unknown.name') is None

# Generated at 2022-06-12 20:53:54.249015
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    setting1 = ConfigSetting(name="a",
                             value="b",
                             plugin=ConfigPlugin("filter", "add_host"))
    setting2 = ConfigSetting(name="c",
                             value="d",
                             plugin=ConfigPlugin("Connection", "local"))
    setting3 = ConfigSetting(name="e",
                             value="f")

    data = ConfigData()
    data.update_setting(setting1)
    data.update_setting(setting2)
    data.update_setting(setting3)

    assert data.get_setting("a", ConfigPlugin("filter", "add_host")).name == "a"
    assert data.get_setting("c", ConfigPlugin("Connection", "local")).name == "c"
    assert data.get_setting("e").name == "e"

    assert data.get_

# Generated at 2022-06-12 20:54:06.188937
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Plugin:

        def __init__(self, type, name):
            self.type = type
            self.name = name

    class Setting:

        def __init__(self, name, value):
            self.name = name
            self.value = value

        def clone(self):
            return self

        def __repr__(self):
            return 'Setting(%s=%s)' % (self.name, self.value)

    c = ConfigData()

    s = Setting('setting1', 'value1')
    c.update_setting(s)
    assert c._global_settings['setting1'].value == 'value1'

    s = Setting('setting1', 'value2')
    c.update_setting(s, Plugin('connection', 'local'))

# Generated at 2022-06-12 20:54:07.752548
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    assert 0 == len(configdata.get_settings())


# Generated at 2022-06-12 20:54:18.218333
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from collections import namedtuple

    config_data = ConfigData()

    Plugin = namedtuple('Plugin', ['name', 'type'])
    plugin = Plugin('test_plugin', 'connection')

    Setting = namedtuple('Setting', ['name', 'section', 'subsection', 'default', 'type',
                                     'choices', 'current', 'source', 'scope', 'plugin'])
    setting = Setting('test', 'connection', 'test', None, 'str', None, 'test', 'default', 'global', plugin)

    config_data.update_setting(setting)

    assert config_data.get_setting(name='test') == setting


# Generated at 2022-06-12 20:54:28.966758
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Try to get a setting that was never created
    plugin = Plugin('test', Plugin.NETWORK)
    configdata = ConfigData()
    assert configdata.get_setting('Setting without plugin', plugin) is None
    assert configdata.get_setting('Setting without plugin') is None

    # Try to create a setting without any plugin
    plugin = None
    configdata.update_setting(Setting('Setting without plugin', 'value1'))
    assert configdata.get_setting('Setting without plugin') is not None
    assert configdata.get_setting('Setting without plugin').name == 'Setting without plugin'
    assert configdata.get_setting('Setting without plugin').value == 'value1'

    # Try to create a setting with a plugin
    plugin = Plugin('test', Plugin.NETWORK)

# Generated at 2022-06-12 20:54:36.556772
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    c = ConfigData()

    assert c.get_setting(name='str_setting') == None

    # Adding a global setting

    s = ConfigSetting(name='str_setting')
    c.update_setting(s)
    assert c.get_setting(name='str_setting') is not None

    # Adding another global setting

    s = ConfigSetting(name='bool_setting')
    c.update_setting(s)
    assert c.get_setting(name='bool_setting') is not None

    # Adding a plugin setting

    p = ConfigPlugin('lookup', 'variables')
    s = ConfigSetting(name='FILTER_MODULES_PATTERNS')
    c.update_setting(s, p)

# Generated at 2022-06-12 20:54:47.522472
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    import os
    import tempfile
    import yaml

    from ansiblelint import RulesCollection
    from ansiblelint import Runner
    from ansiblelint.rules.UseWithStateIsNowDeprecatedRule import UseWithStateIsNowDeprecatedRule
    from ansiblelint.rules.YamlLintRule import YamlLintRule

    conf_data = ConfigData()

    # Global and plugin settings
    conf_data.update_setting(PluginSetting('plugin_name', 'null', 'env'))
    conf_data.update_setting(PluginSetting('plugin_name', 'null', 'config'))
    conf_data.update_setting(PluginSetting('plugin_name', 'null', 'env_config'))
    conf_data.update_setting(GlobalSetting('global_name', 'null', 'env'))
    conf_data

# Generated at 2022-06-12 20:54:57.000986
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()
    plugin = Plugin('module', 'mymodule')
    plugin2 = Plugin('module', 'mymodule2')

    config.update_setting(Setting('vars', '', '', '', '', None), plugin)
    config.update_setting(Setting('vars', '', '', '', '', None), plugin2)
    config.update_setting(Setting('vars', '', '', '', '', None))

    assert len(config.get_settings()) == 3



# Generated at 2022-06-12 20:55:02.578559
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data._global_settings = {"a":1, "b":2}
    config_data._plugins = {"typeA":{"nameA":{"x":1}}, "typeB":{"nameB":{"y":2}}}
    # config_data.get_setting/1 -> global setting
    assert config_data.get_setting("a") == 1 and config_data.get_setting("b") == 2
    # config_data.get_setting/2 -> plugin type does not exist
    assert config_data.get_setting("a", PluginType('typeC','nameC')) is None
    # config_data.get_setting/2 -> plugin type exists, but plugin name does not exist
    assert config_data.get_setting("a", PluginType('typeA','nameB')) is None
    # config_data

# Generated at 2022-06-12 20:55:08.613485
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting('/etc/hosts')
    config_data.update_setting('/etc/group')
    config_data.update_setting('/etc/passwd')

# Generated at 2022-06-12 20:55:10.123630
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    assert(configdata.get_settings()==[])


# Generated at 2022-06-12 20:55:17.271082
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import get_plugin_loader
    from ansible.plugins.loader import filter_conditionals
    from ansible.plugins.loader import find_plugin_candidates
    from ansible.plugins.loader import get_all_plugin_loaders

    config_data = ConfigData()

    # Test getting settings for a plugin that contains no settings
    plugin_loader = get_plugin_loader()
    plugin_loader.plugin_vars = {'plugin_type': 'action', 'plugin_name': 'ping'}

    settings = config_data.get_settings(plugin_loader)
    assert settings == []

    # Test getting settings for a plugin that contains one setting and then that setting is added to config data
    plugin_loader = get_plugin_loader()

# Generated at 2022-06-12 20:55:21.950864
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = {'name':'version', 'value': '1.0'}

    config_data.update_setting(setting)

    settings = config_data.get_settings()
    assert len(settings) == 1

    assert settings[0]['value'] == '1.0'


# Generated at 2022-06-12 20:55:25.815720
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('hostkey_checking',
                                       'boolean',
                                       'yes',
                                       True,
                                       None,
                                       None))
    assert 'hostkey_checking' in config_data._global_settings

# Generated at 2022-06-12 20:55:34.685408
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data_obj = ConfigData()
    setting_dict = [{'name':'a','value':1,'type':'int'},{'name':'b','value':'3','type':'string'}]
    for setting in setting_dict:
        config_data_obj.update_setting(ConfigSetting(**setting))

    assert config_data_obj.get_settings() == [ConfigSetting(**setting) for setting in setting_dict]
    assert config_data_obj.get_settings(plugin=ConfigPlugin(type='test', name='test')) == []



# Generated at 2022-06-12 20:55:41.865065
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    setting = Setting("a", "b", "c")
    plugin = Plugin("e", "f")
    config = ConfigData()
    config.update_setting(setting, plugin)
    assert config._plugins.get("e").get("f").get("a").name == "a"
    assert config._plugins.get("e").get("f").get("a").value == "b"
    assert config._plugins.get("e").get("f").get("a").description == "c"

# Generated at 2022-06-12 20:55:46.440772
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    
    # Test 1
    # Test with null values
    config_data = ConfigData()

    assert config_data._global_settings == {}
    assert config_data._plugins == {}

    assert config_data.get_setting('setting_name', None) == None
    assert config_data.get_setting('setting_name', 1) == None


# Generated at 2022-06-12 20:55:55.393797
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = 'test setting'
    plugin = 'test plugin'
    plugin_type = 'test plugin type'
    setting.name = 'test setting name'
    plugin.name = 'test plugin name'
    plugin.type = 'test plugin type'
    config_data.update_setting(setting, plugin)
    setting.name = 'test setting name 2'
    config_data.update_setting(setting, plugin)
    settings = config_data.get_settings(plugin)

    assert(len(settings) == 2)
    assert(settings[0].name == 'test setting name')
    assert(settings[1].name == 'test setting name 2')

# Generated at 2022-06-12 20:56:05.922304
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Set the block Count
    block_count = 2

    # Init the config
    config = ConfigData()
    assert config._global_settings == {}

    # Set the plugin name and type
    plugin_name = 'name'
    plugin_type = 'type'
    plugin = Plugin(plugin_name, plugin_type)

    # Set the setting name
    setting_name = 'name'
    setting_value = 'value'
    setting = Setting(setting_name)
    setting.value = setting_value

    # Set the setting to the plugin
    config.update_setting(setting, plugin)

    # Get the setting
    result = config.get_settings(plugin)
    assert len(result) == 1
    assert result[0].name == setting_name
    assert result[0].value == setting_value

# Generated at 2022-06-12 20:56:17.851938
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from c1_example.config import ConfigSetting
    from c1_example.config import ConfigPlugin

    # Test with unkown setting
    cd = ConfigData()
    s = cd.get_setting('unkown')
    assert s is None

    # Test with unkown plugin
    cd = ConfigData()
    p = ConfigPlugin('unkown', 'unkown')
    s = cd.get_setting('unkown', p)
    assert s is None

    # Test with known plugin, but unkown setting
    cd = ConfigData()
    p = ConfigPlugin('network', 'ios')
    s = cd.get_setting('unkown', p)
    assert s is None

    # Test with known plugin and known setting
    cd = ConfigData()
    p = ConfigPlugin('network', 'ios')

# Generated at 2022-06-12 20:56:27.540285
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()
    assert cd.get_settings() == []

    cd.update_setting(ConfigSetting('setting1', 'value1'))
    cd.update_setting(ConfigSetting('setting2', 'value2'))

    settings = cd.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'setting1'
    assert settings[0].value == 'value1'
    assert settings[1].name == 'setting2'
    assert settings[1].value == 'value2'

    assert cd.get_settings(ConfigPlugin('lookup', 'none')) == []



# Generated at 2022-06-12 20:56:34.804701
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    def test_case_1():
        cd = ConfigData()
        cd.update_setting(Setting('a', 'a', 'a'))
        cd.update_setting(Setting('b', 'b', 'b'), Plugin('c', 'c'))
        cd.update_setting(Setting('c', 'c', 'c'), Plugin('c', 'c'))
        cd.update_setting(Setting('d', 'd', 'd'), Plugin('d', 'd'))
        assert cd.get_settings() == [Setting('a', 'a', 'a')]

    def test_case_2():
        cd = ConfigData()
        cd.update_setting(Setting('a', 'a', 'a'))
        cd.update_setting(Setting('b', 'b', 'b'), Plugin('c', 'c'))

# Generated at 2022-06-12 20:56:41.020450
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    s1 = Setting('name1', 'description1', None, None)
    s2 = Setting('name2', 'description2', None, None)
    p = Plugin('plugin_typ', 'plugin_name')

    cd = ConfigData()
    cd.update_setting(s1)
    cd.update_setting(s2, plugin=p)

    assert len(cd.get_settings()) == 1
    assert len(cd.get_settings(plugin=p)) == 1
    assert s1 in cd.get_settings()
    assert s2 in cd.get_settings(plugin=p)

# Generated at 2022-06-12 20:56:52.499556
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    from ansible.config.setting import Setting
    from ansible.plugins import module_loader
    from ansible.plugins.loader import find_plugin
    test_setting_name = 'test_setting_value'
    test_value = 'test_value'
    test_plugin = module_loader.get('command', class_only=True)
    test_plugin.name = 'command'
    test_plugin.type = 'action'
    setting = Setting(test_setting_name, module_loader, plugin=test_plugin)
    setting.value = test_value
    setting.set_default()

    config_data.update_setting(setting, test_plugin)
    result = config_data.get_setting(test_setting_name, test_plugin)

    assert result.value == test_value

# Generated at 2022-06-12 20:56:59.179027
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cdata = ConfigData()
    cdata.update_setting(Setting('test', 'test_val'))
    assert cdata.get_setting('test').name == 'test'


# Generated at 2022-06-12 20:57:08.512495
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin1 = Plugin(type='type-plugin1', name='name-plugin1')
    plugin2 = Plugin(type='type-plugin2', name='name-plugin2')
    config_data.update_setting(Setting(name='setting1', value=True, origin='origin1', plugin=plugin1))
    config_data.update_setting(Setting(name='setting2', value=False, origin='origin2', plugin=plugin2))
    config_data.update_setting(Setting(name='setting3', value=True, origin='origin3'))
    assert len(config_data.get_settings()) == 3
    assert len(config_data.get_settings(plugin1)) == 2
    assert len(config_data.get_settings(plugin2)) == 2

# Generated at 2022-06-12 20:57:15.846295
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    
    # test get_settings when plugin is None
    setting1 = Setting(name='setting1', value='value1', origin='no origin', level='global')
    config_data.update_setting(setting1)
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'setting1'

    # test get_settings when plugin is not None
    setting2 = Setting(name='setting2', value='value2', origin='no origin', level='plugin')
    config_data.update_setting(setting2, Plugin('plugin name', 'plugin type', 'plugin path'))
    settings = config_data.get_settings()
    assert len(settings) == 1

    # test get_settings when plugin is not None and plugin type does not exist


# Generated at 2022-06-12 20:57:29.440653
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # create an instance of ConfigData
    config_data = ConfigData()
    # create a plugin
    plugin = Plugin("Foo", "foo")
    # create a setting
    setting = Setting("bar", "default", plugin)
    # update_setting
    config_data.update_setting(setting)
    # test value
    assert config_data._global_settings.get("bar") == setting


# Generated at 2022-06-12 20:57:36.936485
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    data.update_setting(Setting(name="value1", value=True))
    data.update_setting(Setting(name="value2", value=True))
    data.update_setting(Setting(name="value3", value=True))
    data.update_setting(Setting(name="config_file", value="./test"))

    assert len(data._global_settings) == 4

    assert data._global_settings["value1"] == True
    assert data._global_settings["value2"] == True
    assert data._global_settings["value3"] == True
    assert data._global_settings["config_file"] == "./test"



# Generated at 2022-06-12 20:57:47.009299
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert len(settings) == 0

    config_data.update_setting(Setting('a', '1', 'global'))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'a'

    config_data.update_setting(Setting('b', '2', 'global'))
    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'a'
    assert settings[1].name == 'b'

    config_data.update_setting(Setting('b', '3', 'global'))
    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name

# Generated at 2022-06-12 20:57:57.460878
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin_type = 'action_plugin'
    plugin_name = 'debug'
    setting_name = 'terminal'
    setting = {'name': setting_name}

    assert config_data.get_setting(setting_name) is None, 'Global setting should not be set (1)'
    assert config_data.get_setting(setting_name, plugin=None) is None, 'Global setting should not be set (2)'

    config_data.update_setting(setting)

    assert config_data.get_setting(setting_name) is not None, 'Global setting should be set (1)'
    assert config_data.get_setting(setting_name, plugin=None) is not None, 'Global setting should be set (2)'
    assert config_data.get_setting(setting_name) == setting

# Generated at 2022-06-12 20:58:05.434371
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    plugin = ConfigPlugin()
    plugin.type='connection';
    plugin.name='ssh'
    config_setting = ConfigSetting()
    config_setting.name = 'timeout'
    config_setting.value = '100'
    
    config_data = ConfigData()
    config_data.update_setting(config_setting, plugin)
    settings = config_data.get_settings(plugin)
    
    assert 1 == len(settings)
    assert settings[0].value == '100'
   

# Generated at 2022-06-12 20:58:11.780212
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.vars.vars import VarModule

    # Create ConfigData object
    config_data = ConfigData()

    # Create builtin plugin
    plugin_loader = PluginLoader('lookup', 'ansible.plugins.vars.vars', 'VarModule', 'vars')
    for plugin_path in plugin_loader._get_plugins_in_paths(plugin_loader.package, plugin_loader.directories):
        if plugin_loader._package_name not in plugin_path:
            continue
        plugin = plugin_loader._get_plugin_from_path(plugin_path)._load_plugin()
        if not isinstance(plugin, VarModule):
            raise ValueError("Plugin %s did not match expected type %s" % (plugin, VarModule))

# Generated at 2022-06-12 20:58:19.636483
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import json


# Generated at 2022-06-12 20:58:22.002125
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting("test") is None


# Generated at 2022-06-12 20:58:27.801200
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = Plugin('shell', 'echo', 'command')
    setting = Setting('version', '2.2', 'command', 'echo')
    config_data.update_setting(setting, plugin)
    assert plugin.type in config_data._plugins
    assert plugin.name in config_data._plugins[plugin.type]
    assert setting.name in config_data._plugins[plugin.type][plugin.name]


# Generated at 2022-06-12 20:58:38.761619
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data._global_settings = {
        "foo": ["foo", "foo", "foo", "bar"],
        "bar": [1, 2, 3]
    }
    config_data._plugins = {
        "foo": {
            "foo": {
                "foo": ["bar", "bar"],
                "baz": [1, 2, 3]
            },
            "bar": {
                "foo": [3, 4, 5],
                "bar": ["foo", "bar", "baz"]
            }
        }
    }
    assert config_data.get_settings() == config_data._global_settings.values()
    assert config_data.get_settings(Plugin(type="foo", name="foo")) == config_data._plugins["foo"]["foo"].values

# Generated at 2022-06-12 20:58:57.125517
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # create Plugin object
    class my_plugin():

        def __init__(self, type, name):
            self.type = type
            self.name = name

    # create ConfigData object
    config_data = ConfigData()

    # create Setting object
    class my_setting():

        def __init__(self, name, value, origin=None):
            self.name = name
            self.value = value
            self.origin = origin

    # create Setting for plugin
    s1 = my_setting('s1', 1)

    # create Plugin object
    plugin = my_plugin('my_type', 'my_name')

    # check if get_settings works
    assert (config_data.get_settings(plugin) == [])

    # update the setting
    config_data.update_setting(s1, plugin)

   

# Generated at 2022-06-12 20:58:58.639738
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    print(config_data.get_settings())

# Generated at 2022-06-12 20:59:10.355371
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    
    # Instanciate a ConfigData object
    config_data = ConfigData()

    # Setting at global scope
    global_setting = Setting("my_setting", "This is a global setting")
    config_data.update_setting(global_setting)

    # Setting for a module
    module_setting = Setting("my_setting", "This is a module setting")
    config_data.update_setting(module_setting, Plugin("module", "my_module"))

    # Setting for a cli param
    cli_setting = Setting("my_setting", "This is a cli setting")
    config_data.update_setting(cli_setting, Plugin("cli", "my_cli"))

    # Setting for a connection
    connection_setting = Setting("my_setting", "This is a connection setting")

# Generated at 2022-06-12 20:59:14.795535
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('test', 'test', 'test'))
    config_data.update_setting(Setting('test2', 'test2', 'test2'))
    setting = config_data.get_settings()
    assert len(setting) == 2


# Generated at 2022-06-12 20:59:25.045727
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    setting1 = Setting(name="setting1", value="one", plugin="global", plugin_type="global")
    setting2 = Setting(name="setting2", value="two", plugin="global", plugin_type="global")
    setting3 = Setting(name="setting3", value="three", plugin="mymodule", plugin_type="module")
    setting4 = Setting(name="setting4", value="four", plugin="mymodule", plugin_type="module")

    # One global setting
    config.update_setting(setting1)
    assert config.get_setting(setting1.name) == setting1

    # Update global setting
    config.update_setting(setting2)
    assert config.get_setting(setting2.name) == setting2

    # Update global setting
    config.update_setting(setting1)
   

# Generated at 2022-06-12 20:59:29.575559
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    c_data = ConfigData()
    setting1 = Setting("ANSIBLE_HOST_KEY_CHECKING", "True", plugin=Plugin("sshconnection", "ssh"))
    c_data.update_setting(setting1)
    settings = c_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == "ANSIBLE_HOST_KEY_CHECKING"

# Generated at 2022-06-12 20:59:39.949276
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
	
	config_data = ConfigData()
	
	# Add a global config setting
	global_setting = ConfigSetting('global_setting_1', 'global_setting_value_1')
	config_data.update_setting(global_setting)
	actual = config_data.get_setting('global_setting_1')
	expected = global_setting
	assert actual == expected
	
	# Add a plugin config setting for a plugin
	plugin_setting = ConfigSetting('global_setting_2', 'global_setting_value_2')
	plugin = Plugin('plugin_name', 'plugin_type')
	config_data.update_setting(plugin_setting, plugin)
	actual = config_data.get_setting('global_setting_2', plugin)
	expected = plugin_setting
	assert actual == expected
	
	# Ensure that global setting

# Generated at 2022-06-12 20:59:47.357343
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    class Plugin(object):

        TYPE = 'type'
        NAME = 'name'

        def __init__(self):
            self.type = Plugin.TYPE
            self.name = Plugin.NAME

    config_data = ConfigData()
    assert config_data.get_setting('foo') is None

    foo_setting = {'name': 'foo', 'value': 'bar'}
    config_data.update_setting(foo_setting)
    setting = config_data.get_setting('foo')
    assert setting is not None
    assert setting.name == foo_setting['name']
    assert setting.value == foo_setting['value']

    foo_setting = {'name': 'foo_plugin', 'value': 'bar_plugin'}
    plugin = Plugin()

# Generated at 2022-06-12 20:59:50.836666
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    setting = Setting("Name", "Description", "Value")
    cd.update_setting(setting)
    cd.update_setting(setting, Plugin("cache", "local"))
    assert cd.get_setting("Name") == setting
    assert cd.get_setting("Name", Plugin("cache", "local")) == setting


# Generated at 2022-06-12 20:59:56.522316
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting("setting")
    assert config_data.get_setting("setting") == "setting"
    config_data.update_setting("plugin_setting", "plugin")
    assert config_data.get_setting("plugin_setting", "plugin") == "plugin_setting"



# Generated at 2022-06-12 21:00:17.733112
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    # 1. test if there is a plugin with the given name and type
    plugin = Plugin('lookup', 'linode')
    setting = Setting('linode.api_key', 'mykey')
    config.update_setting(setting, plugin)
    returned_setting = config.get_setting('linode.api_key', plugin)
    assert returned_setting is not None
    assert returned_setting.name == 'linode.api_key'
    assert returned_setting.value == 'mykey'

    # 2. test if there is a plugin but there is no setting
    returned_setting = config.get_setting('linode.api_key')
    assert returned_setting is None
    returned_setting = config.get_setting('linode.api_key', Plugin('no_type', 'no_name'))

# Generated at 2022-06-12 21:00:29.802610
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()
    test_setting_1 = Setting("host_key_checking", "False")
    test_setting_2 = Setting("retry_files_enabled", "True")
    test_setting_3 = Setting("callback_whitelist", "cowsay")
    configData.update_setting(test_setting_1)
    configData.update_setting(test_setting_2)
    configData.update_setting(test_setting_3, Plugin("callback", "cowsay"))
    settings = configData.get_settings()
    assert settings[0].name == "host_key_checking"
    assert settings[1].name == "retry_files_enabled"
    assert len(settings) == 2
    settings = configData.get_settings(Plugin("callback", "cowsay"))

# Generated at 2022-06-12 21:00:38.811239
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_object = ConfigData()
    # Test with no plugin
    assert len(test_object.get_settings()) == 0
    # Test with non-existent plugin
    from ansible.plugins import core
    fake_plugin = core.Plugin('FakePlugin')
    fake_plugin.type = 'connection'
    fake_plugin.name = 'FakePluginName'
    assert len(test_object.get_settings(plugin=fake_plugin)) == 0
    # Test with valid plugin
    from ansible.plugins import connection
    plugin_to_test = connection.NetworkCli('NetworkCli')
    assert len(test_object.get_settings(plugin=plugin_to_test)) == 0


# Generated at 2022-06-12 21:00:48.462112
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = Plugin('action', 'test')
    setting = Setting('test', 'test')
    setting.value = 'test'
    config_data.update_setting(setting, plugin=plugin)
    setting = Setting('test', 'test')
    setting.value = 'test'
    config_data.update_setting(setting)

    assert config_data.get_setting('test', plugin=plugin) == setting
    assert config_data.get_setting('test') == setting
    assert config_data.get_setting('fail', plugin=plugin) == None
    assert config_data.get_setting('fail') == None


# Generated at 2022-06-12 21:00:51.800434
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('NAME', 'VALUE')
    config_data.update_setting(setting)
    assert config_data.get_setting('NAME') is setting


# Generated at 2022-06-12 21:00:57.456144
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting_plugin = SettingPlugin(name="MaxErrorRetry", value="10", pluginType="core", pluginName="global")
    config_data.update_setting(setting_plugin)
    assert config_data.get_setting("MaxErrorRetry") == setting_plugin
    # Test not existing setting
    assert config_data.get_setting("not_existing_setting") == None


# Generated at 2022-06-12 21:01:04.353245
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config = ConfigData()
    config.update_setting(ConfigSetting('foo', 'bar'))
    config.update_setting(ConfigSetting('fizz', 'buzz'))
    assert len(config.get_settings()) == 2
    assert config.get_settings()[0].name == 'foo'
    assert config.get_settings()[1].name == 'fizz'


# Generated at 2022-06-12 21:01:08.530256
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    plugin = PluginDependency('test', 'testplugin', 'lib')
    setting = PluginSetting('test', 'test')
    config_data = ConfigData()
    config_data.update_setting(setting, plugin)

    assert setting == config_data._plugins[plugin.type][plugin.name][setting.name]



# Generated at 2022-06-12 21:01:13.630888
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    assert config_data.get_setting('my_setting') is None

    config_data.update_setting(Setting('my_setting', 'my_value'))
    assert config_data.get_setting('my_setting') == Setting('my_setting', 'my_value')

    config_data.update_setting(Setting('my_other_setting', 'my_other_value'))
    assert config_data.get_setting('my_other_setting') == Setting('my_other_setting', 'my_other_value')



# Generated at 2022-06-12 21:01:23.986007
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    class Plugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    class ConfigSetting(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    cd = ConfigData()

    cd.update_setting(ConfigSetting('foo', 'bar'))
    settings = cd.get_settings()
    assert {s.name for s in settings} == {'foo'}

    cd.update_setting(ConfigSetting('foo', 'baz'))
    settings = cd.get_settings()
    assert {s.name for s in settings} == {'foo'}

    plugin1 = Plugin('script', 'hello')
    cd.update_setting(ConfigSetting('foo', 'baz'), plugin1)


# Generated at 2022-06-12 21:01:58.018536
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    assert config.get_setting('something') is None
    assert config.get_setting('something', 'something') is None

    config.update_setting('something')
    assert config.get_setting('something') == 'something'
    assert config.get_setting('something', 'something') is None


# Generated at 2022-06-12 21:02:06.868070
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    assert config_data.get_setting("abc") is None

    from collections import namedtuple
    Plugin = namedtuple("Plugin", "type name")

    from ansible.module_utils.config_data import Setting
    global_setting = Setting("abc", True, "some description")
    plugin_setting = Setting("def", True, "some description")
    module_plugin = Plugin("module", "copy")
    inventory_plugin = Plugin("inventory", "test")
    cache_plugin = Plugin("cache", "jsonfile")

    config_data.update_setting(global_setting)
    assert config_data.get_setting("abc") == global_setting
    assert config_data.get_setting("abc", module_plugin) == global_setting


# Generated at 2022-06-12 21:02:12.752834
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = Plugin()
    plugin.name = "TestPlugin"

    assert config_data.get_settings(plugin) == []

    plugin.type = "INVENTORY"
    assert config_data.get_settings(plugin) == []

    plugin.type = "UNKNOWN"
    assert config_data.get_settings(plugin) == []

# Generated at 2022-06-12 21:02:20.535134
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    import pprint

    global_settings = {'test1': 'test1', 'test2': 'test2'}
    plugins = {}
    plugins['lookup'] = {}
    plugins['callback'] = {}
    plugins['connection'] = {}
    plugins['invenory'] = {}
    plugins['shell'] = {}
    plugins['vars'] = {}
    plugins['filter'] = {}
    plugins['action'] = {}
    plugins['become'] = {}
    plugins['cache'] = {}
    plugins['terminal'] = {}
    plugins['connection']['local'] = {'test3': 'test3'}
    plugins['connection']['ssh'] = {'test4': 'test4', 'test5': 'test5'}

    config_data = ConfigData()
    config_data._global_settings = global_settings

# Generated at 2022-06-12 21:02:23.027686
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert(config_data.get_settings() == [])

# Generated at 2022-06-12 21:02:31.583099
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    setting = Setting('foo', 'baz')
    plugin = Plugin('bar', 'baz')

    # Test behavior when no settings are present
    assert len(config_data.get_settings(plugin=plugin)) == 0
    assert len(config_data.get_settings()) == 0

    # Add a global setting
    config_data.update_setting(setting)

    assert len(config_data.get_settings(plugin=plugin)) == 0
    assert len(config_data.get_settings()) == 1
    assert config_data.get_settings().pop().name == 'foo'

    # Add a plugin setting
    config_data.update_setting(setting, plugin)

    assert len(config_data.get_settings(plugin=plugin)) == 1

# Generated at 2022-06-12 21:02:33.694502
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.get_settings()

# Generated at 2022-06-12 21:02:39.036511
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create a ConfigData object
    test_data = ConfigData()

    # Update a setting to the global_settings list
    test_setting = Setting('default_log_path')
    test_setting.value = '../log/log.txt'
    test_setting.is_changed = False
    test_setting.section = 'DEFAULT'
    test_setting.plugin = None
    test_data.update_setting(test_setting)

    assert test_data.get_settings()[0].value == '../log/log.txt'

    # Update a plugin to the plugins list
    test_plugin = Plugin('BC-Test', 'Test')
    test_setting = Setting('default_log_path')
    test_setting.value = '../log/log.txt'
    test_setting.is_changed = False
    test_setting

# Generated at 2022-06-12 21:02:45.188188
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Create objects of the classes
    config_data = ConfigData()
    setting1 = Setting('setting1', 'setting1 type', 'setting1 description')
    setting2 = Setting('setting2', 'setting2 type', 'setting2 description')
    plugin1 = Plugin(Plugin.CORE, 'plugin1')

    # Update 'setting1' for 'plugin1'
    config_data.update_setting(setting1, plugin1)
    assert config_data._plugins[plugin1.type][plugin1.name][setting1.name] == setting1

    # Update 'setting2' for 'plugin1'
    config_data.update_setting(setting2, plugin1)
    assert config_data._plugins[plugin1.type][plugin1.name][setting2.name] == setting2

    # Update 'setting1' for global scope
    config_

# Generated at 2022-06-12 21:02:46.171348
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
