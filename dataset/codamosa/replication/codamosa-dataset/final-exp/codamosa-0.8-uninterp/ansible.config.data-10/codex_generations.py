

# Generated at 2022-06-12 20:53:29.858326
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configdata = ConfigData()
    setting_name = 'setting_name'

    assert configdata.get_setting(setting_name) is None

    configdata.update_setting(Setting(setting_name, 'string', 'value'))

    assert configdata.get_setting(setting_name) is not None
    assert configdata.get_setting(setting_name).name == setting_name


# Generated at 2022-06-12 20:53:33.811054
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert cd._global_settings == {}
    assert cd._plugins == {}
    setting1 = Setting('setting1')
    cd.update_setting(setting1)
    assert cd._global_settings == {'setting1': setting1}
    assert cd._plugins == {}
    setting2 = Setting('setting2')
    cd.update_setting(setting2, Plugin('test', 'connection'))
    assert cd._global_settings == {'setting1': setting1}
    assert cd._plugins == {'connection': {'test': {'setting2': setting2}}}



# Generated at 2022-06-12 20:53:44.664828
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    global_setting = Setting("project", "Test", "path")
    module_setting = Setting("project", "Test", "path")
    module_setting.set("module_path", ["/home/Test/modules"])
    module_setting.set("module_source", ["/home/Test/module_src"])
    module_setting.set("module_utils", ["/home/Test/module_utils"])
    module_setting.set("action_plugins", ["/home/Test/action_plugins"])
    module_setting.set("cache_plugins", ["/home/Test/cache_plugins"])
    module_setting.set("lookup_plugins", ["/home/Test/lookup_plugins"])
    module_setting.set("filter_plugins", ["/home/Test/filter_plugins"])

# Generated at 2022-06-12 20:53:46.356207
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0

# Generated at 2022-06-12 20:53:55.236259
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert data.get_settings() == []
    assert data.get_settings("Test") == []
    data._global_settings = {'test': 'test'}
    assert data.get_settings() == [{'test': 'test'}]
    assert data.get_settings("Test") == []
    data._plugins = {'test': 'test'}
    assert data.get_settings() == [{'test': 'test'}]
    assert data.get_settings("Test") == []
    data._plugins = {'test': {'test': 'test'}}
    assert data.get_settings() == [{'test': 'test'}]
    assert data.get_settings("Test") == []

# Generated at 2022-06-12 20:54:07.307939
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    setting_a = ConfigSetting(name='a')
    data.update_setting(setting_a, None)
    assert data.get_setting('a', None) is setting_a

    setting_b = ConfigSetting(name='b')
    data.update_setting(setting_b, None)
    assert data.get_setting('b', None) is setting_b

    assert data.get_setting('c', None) is None

    plugin_1 = Plugin(type='module', name='foo')
    setting_c = ConfigSetting(name='c')
    data.update_setting(setting_c, plugin_1)
    assert data.get_setting('c', plugin_1) is setting_c

    plugin_2 = Plugin(type='module', name='bar')

# Generated at 2022-06-12 20:54:11.159974
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()

    assert data.get_settings() == []

    data.update_setting(Setting('test', 'testvalue'))

    assert data.get_settings() == [Setting('test', 'testvalue')]

    data.update_setting(Setting('test2', 'testvalue2'))

    assert data.get_settings(Plugin('default', 'test')) == []

    assert data.get_settings() == [Setting('test', 'testvalue'), Setting('test2', 'testvalue2')]

    data.update_setting(Setting('test2', 'testvalue3', 'default', 'test'))

    assert data.get_settings(Plugin('default', 'test')) == [Setting('test2', 'testvalue3', 'default', 'test')]


# Generated at 2022-06-12 20:54:14.851049
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_ConfigData = ConfigData()
    test_ConfigData.update_setting(None)
    assert test_ConfigData._global_settings == {}


# Generated at 2022-06-12 20:54:23.458738
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.module_utils.config_loader import ConfigData, PluginConfig, SettingConfig, OptionConfig

    config_data = ConfigData()
    config_data.update_setting(SettingConfig(name='var1', description='test setting', option=OptionConfig(name='value', type='string')))

    plugin = PluginConfig('test', 'test')
    config_data.update_setting(SettingConfig(name='var2', description='test setting', option=OptionConfig(name='value', type='string')), plugin)

    var1 = config_data.get_setting('var1')
    assert var1 is not None
    assert var1.name == 'var1'

    var2 = config_data.get_setting('var2', plugin)
    assert var2 is not None
    assert var2.name == 'var2'

# Unit

# Generated at 2022-06-12 20:54:34.133554
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from PluginSetting import PluginSetting
    from PluginSpec import PluginSpec

    config_data = ConfigData()
    config_data.update_setting(setting=PluginSetting(name='setting1', value='value1'))
    config_data.update_setting(plugin=PluginSpec('plugin1', 'plugin_type1'), setting=PluginSetting(name='setting2', value='value2'))
    config_data.update_setting(plugin=PluginSpec('plugin1', 'plugin_type1'), setting=PluginSetting(name='setting3', value='value3'))
    config_data.update_setting(plugin=PluginSpec('plugin2', 'plugin_type1'), setting=PluginSetting(name='setting4', value='value4'))


# Generated at 2022-06-12 20:54:46.060520
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    plugin = Plugin('test_plugin', 'test_type')

    setting = BaseSetting('test_key', 'test_value')
    config_data.update_setting(setting)
    assert config_data.get_setting('test_key') == setting
    assert config_data.get_setting('test_key', plugin) is None

    setting = BaseSetting('test_key', 'test_value2')
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('test_key') == BaseSetting('test_key', 'test_value')
    assert config_data.get_setting('test_key', plugin) == setting


# Generated at 2022-06-12 20:54:47.957730
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.config.setting import Setting

    config_data = ConfigData()
    config_data.update_setting(Setting('foo', 'bar', 'lorem ipsum'))

    assert config_data.get_setting('foo').value == 'lorem ipsum'


# Generated at 2022-06-12 20:54:51.836603
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Setting():
        def __init__(self, name, _type):
            self.name = name
            self.type = _type

    cd = ConfigData()

    for plugin_type in ['connection', 'become', 'lookup', 'callback', 'cache', 'shell', 'strategy', 'vars', 'terminal', 'action']:
        for index in range(0, 4):
            name = '%s-%d' % (plugin_type, index)
            setting = Setting(name, plugin_type)
            cd.update_setting(setting)

    assert len(cd.get_settings()) == 40


# Generated at 2022-06-12 20:54:59.579238
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    from ansible.plugins.loader import PluginLoader

    # Test getting setting from a plugin
    from ansible.plugins.test import TestBase

    plugin_loader = PluginLoader("action", "test")
    plugin = plugin_loader.get("test_name")
    setting_name = "action_plugins"
    setting = config_data.get_setting(setting_name)
    assert setting is None
    setting = config_data.get_setting(setting_name, plugin)
    assert setting is None
    setting = config_data.get_settings()
    assert len(setting) == 0
    setting = config_data.get_settings(plugin)
    assert len(setting) == 0
    setting = TestBase.add_setting(setting_name, ['test'])
    assert setting.name == setting_name

# Generated at 2022-06-12 20:55:07.140488
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='setting1', description="This is a description.",
                                       value_type=SettingValueType.INTEGER, default=1,
                                       values=[1, 2, 3, 4], min_value=1, max_value=100))
    config_data.update_setting(Setting(name='setting2', description="This is a description.",
                                       value_type=SettingValueType.INTEGER, default=1,
                                       values=[1, 2, 3, 4], min_value=1, max_value=100))

# Generated at 2022-06-12 20:55:15.016937
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Test case input data
    class TestSetting:

        def __init__(self, name):
            self.name = name

    # Test case workflow
    data = ConfigData()

    # Test case assertion
    name = "test"
    setting = TestSetting(name)
    data.update_setting(setting)
    assert(data._global_settings[name].name == name)
    assert(data._global_settings[name].name == data.get_setting(name).name)
    assert(data.get_settings()[0].name == name)



# Generated at 2022-06-12 20:55:25.615595
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='1',value='a',priority=0,plugin=None))
    assert config_data.get_setting('1').value == 'a'
    config_data.update_setting(Setting(name='1',value='A',priority=0,plugin=None))
    assert config_data.get_setting('1').value == 'a'
    config_data.update_setting(Setting(name='1',value='B',priority=1,plugin=None))
    assert config_data.get_setting('1').value == 'B'
    config_data.update_setting(Setting(name='1',value='c',priority=7,plugin=None))
    assert config_data.get_setting('1').value == 'B'
    config_data.update

# Generated at 2022-06-12 20:55:36.664671
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    global_setting_one = {}
    global_setting_two = {}
    global_setting_three = {}
    plugin_setting_one = {}
    plugin_setting_two = {}
    plugin_setting_three = {}

    global_setting_one['type'] = 'plugin'
    global_setting_one['plugin_type'] = 'foo'
    global_setting_one['plugin'] = 'bar'
    global_setting_two['type'] = 'plugin'
    global_setting_two['plugin_type'] = 'foo'
    global_setting_two['plugin'] = 'bar'
    global_setting_three['type'] = 'plugin'
    global_setting_three['plugin_type'] = 'foo'
    global_setting_three['plugin'] = 'bar'

    plugin_setting_one['type'] = 'plugin'

# Generated at 2022-06-12 20:55:38.096900
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting('foo') == None

# Generated at 2022-06-12 20:55:44.945967
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    new_global_setting = MockSetting('global_setting1')
    new_plugin_setting = MockSetting('plugin_setting1')
    new_plugin = MockPlugin('type1', 'name1')
    config_data = ConfigData()
    config_data.update_setting(new_global_setting)
    config_data.update_setting(new_plugin_setting, new_plugin)
    assert config_data.get_setting('global_setting1') == new_global_setting
    assert config_data.get_setting('plugin_setting1', new_plugin) == new_plugin_setting


# Generated at 2022-06-12 20:55:53.636364
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

#   instance of class ConfigData
    config_data = ConfigData()

#   get global setting
    assert config_data.get_setting('ANSI_COLOR') is None

#   update setting
    from ansible.config.manager import Setting
    config_data.update_setting(Setting('ANSI_COLOR', 'true', 'ansible.cfg'))

#   get global setting
    assert config_data.get_setting('ANSI_COLOR') is not None

#   get plugin setting
    assert config_data.get_setting('ACTION_WARNINGS', 'stdout_callback') is None

#   get plugin setting
    assert config_data.get_setting('ACTION_WARNINGS', 'stdout_callback') is None

#   update setting

# Generated at 2022-06-12 20:55:59.175629
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting = Setting()
    plugin = Plugin()
    plugin.type = 'action'
    plugin.name = 'awx'
    cd.update_setting(setting, plugin)
    assert cd.get_setting('value', plugin) == 'bar' # key-value pair in action awx plugin
    

# Generated at 2022-06-12 20:56:04.658302
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting("setting", "value", "description", ["plugin1", "plugin2"])
    plugin = Plugin("test", "test", "test")
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting("setting", plugin) == setting
    config_data.update_setting(setting)
    assert config_data.get_setting("setting") == setting


# Generated at 2022-06-12 20:56:05.180857
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass

# Generated at 2022-06-12 20:56:11.319795
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    import ansible.plugins.action
    plugin = ansible.plugins.action.ActionBase.load(None, 'ping', None, '.')
    plugin_name = plugin.__class__.__name__

    config_data.update_setting(Setting('max_fail_percentage', '10', plugin=plugin))
    config_data.update_setting(Setting('show_custom_stats', 'true', plugin=plugin))
    config_data.update_setting(Setting('pipelining', 'true'))

    assert config_data.get_setting('max_fail_percentage', plugin=plugin).value == '10'
    assert config_data.get_setting('show_custom_stats', plugin=plugin).value == 'true'

# Generated at 2022-06-12 20:56:23.109560
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
  configData = ConfigData()
  set1 = Setting('host', 'localhost', 'host')
  configData.update_setting(set1)
  assert configData.get_settings() == [set1]
  set2 = Setting('cache_timeout', 2, 'seconds')
  configData.update_setting(set2)
  assert configData.get_settings() == [set1, set2]
  assert configData.get_settings(Plugin('action','local')) == []
  set3 = Setting('host', 'localhost', 'host')
  configData.update_setting(set3, Plugin('action','local'))
  assert configData.get_settings(Plugin('action','local')) == [set3]
  assert configData.get_settings(Plugin('action','another_local')) == []


# Generated at 2022-06-12 20:56:29.295086
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    plugin = Plugin('cliconf', 'ios')
    setting = Setting('host', 'localhost')
    config.update_setting(setting)
    config.update_setting(setting, plugin)
    assert setting.name == config.get_setting(setting.name).name
    assert setting.name == config.get_setting(setting.name, plugin).name


# Generated at 2022-06-12 20:56:39.992014
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    class FakePlugin():
        def __init__(self, name, type):
            self._name = name
            self._type = type

    config_data = ConfigData()

    fake_plugin = FakePlugin("fake_plugin", "fake_type")
    assert config_data.get_setting("fake_setting", fake_plugin) is None

    config_data.update_setting("fake_setting", fake_plugin)
    assert config_data.get_setting("fake_setting", fake_plugin) == "fake_setting"

    config_data.update_setting("fake_setting2", fake_plugin)
    assert config_data.get_setting("fake_setting2", fake_plugin) == "fake_setting2"


# Generated at 2022-06-12 20:56:44.281835
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting = Setting()
    setting.name = 'Inventory'
    setting.value = 'my_inventory.yaml'
    setting.plugin.type = 'Inventory'
    setting.plugin.name = 'InventoryPlus'
    config_data.update_setting(setting, setting.plugin)
    assert config_data.get_setting('Inventory', None) is None
    assert config_data.get_setting('Inventory', setting.plugin) == setting


# Generated at 2022-06-12 20:56:54.414008
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # calling method with an empty config_data, should return an empty list
    config_data = ConfigData()
    assert [] == config_data.get_settings()

    # calling method with a global setting in config_data, should return a list with a single element
    config_data._global_settings = {'global_setting1': {'name': 'global_setting1'}}
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0]['name'] == 'global_setting1'

    # calling method with a plugin setting in config_data, should return a list with a single element
    config_data._plugins = {'plugin_type1': {'plugin_name1': {'plugin_setting1': {'name': 'plugin_setting1'}}}}
    settings = config_data.get_

# Generated at 2022-06-12 20:57:06.368346
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    settings = ConfigData()

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.action import ActionBase
    from ansible.utils.plugin_docs import get_docstring
    import os

    # Create new type of settings
    class TestSetting(MutableMapping):
        def __init__(self, module):
            self.data = {}
            self.module = module
            self.name = 'TEST'
            self.description = 'Test setting.'
            self.default = False
            self.env = ('ANSIBLE_TEST',)
            self.ini = ('test',)
            self.yaml = ('test',)

        def __getitem__(self, key):
            return self.data[key]

# Generated at 2022-06-12 20:57:16.238026
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    assert config_data.get_setting('something') is None
    assert config_data.get_setting('something', 'else') is None

    from ansible.config.setting import Setting
    from ansible.config.plugin import Plugin

    setting = Setting('somename', 'somevalue')

    config_data.update_setting(setting)

    assert config_data.get_setting(setting.name) is not None
    assert config_data.get_setting(setting.name + 'nope') is None
    assert config_data.get_setting(setting.name, 'else') is None

    plugin = Plugin('someplugin', 'somepluginpath', 'sometype')

    config_data.update_setting(setting, plugin)


# Generated at 2022-06-12 20:57:22.159674
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cfg = ConfigData()
    setting = Setting('DEFAULT_ANSIBLE_HOST_KEY_CHECKING', 'boolean')
    cfg.update_setting(setting)
    assert cfg.get_setting('DEFAULT_ANSIBLE_HOST_KEY_CHECKING') == setting
# end of test_ConfigData_update_setting()


# Generated at 2022-06-12 20:57:23.705737
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert data.get_settings() == []


# Generated at 2022-06-12 20:57:33.935868
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # init test obj
    test_obj = ConfigData()

    # fake settings
    test_setting_1 = {"name": "test_setting_1", 'value': "test_value_1"}
    test_setting_2 = {"name": "test_setting_2", 'value': "test_value_2"}

    # test global settings
    # add setting 1
    test_obj._global_settings[test_setting_1['name']] = test_setting_1
    assert test_obj.get_setting(name=test_setting_1['name'])['name'] == test_setting_1['name']

    # update setting 1
    test_obj.update_setting(setting=test_setting_1)
    assert test_obj.get_setting(name=test_setting_1['name'])['value'] == test_setting

# Generated at 2022-06-12 20:57:35.450485
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    d = ConfigData()

    settings = d.get_settings()
    assert len(settings) == 0

    # TODO: Test get_settings on specific plugin
    pass


# Generated at 2022-06-12 20:57:45.051669
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    config.update_setting(Setting('defaults', default=24, value=None, origin='ansible.cfg'))
    config.update_setting(Setting('timeout', default=10, value=None, origin='ansible.cfg'))
    config.update_setting(Setting('max_fail_percentage', default=None, value=None, origin='ansible.cfg'))
    plugin = Plugin('shell', 'sh')
    config.update_setting(Setting('executable', default='/bin/sh', value=None, origin='ansible.cfg'))
    config.update_setting(Setting('other_executable', default='/bin/bash', value=None, origin='ansible.cfg'))

# Generated at 2022-06-12 20:57:55.709074
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock, patch
    from ansible.config.plugin import PluginConfig, PluginSettings

    configdata = ConfigData()
    plugin_config1 = PluginConfig('mytype1', 'myname', 'mypath', 'myclass')
    setting1 = PluginSettings('myname1', 'myvalue1', 'myorigin1')
    setting2 = PluginSettings('myname2', 'myvalue2', 'myorigin2')

    configdata.update_setting(setting1, plugin_config1)
    assert len(configdata.get_settings(plugin_config1)) == 1
    assert configdata.get_setting(plugin_config1.name, plugin_config1).value == 'myvalue1'
    assert len(configdata.get_settings()) == 0


# Generated at 2022-06-12 20:57:58.698536
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    a = ConfigData()
    assert a.get_setting('a') == None
    setting = Setting('a')
    a.update_setting(setting)
    assert a.get_setting('a') == setting


# Generated at 2022-06-12 20:58:04.659336
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data=ConfigData()

    class Setting:
        def __init__(self, name, value=None, origin=None):
            self.name = name
            self.value = value
            self.origin = origin

    class Plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

    setting=Setting("ansible_python_interpreter", "/usr/bin/python", "env")
    config_data.update_setting(setting)
    assert config_data._global_settings['ansible_python_interpreter'].name == 'ansible_python_interpreter'
    assert config_data._global_settings['ansible_python_interpreter'].origin == 'env'

# Generated at 2022-06-12 20:58:17.443027
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data._global_settings == {}
    assert config_data._plugins == {}

    class plugin(object):
        name = 'host'
        type = 'inventory'

    class setting(object):
        name = 'ansible'
        value = 'data'
        vault_password = 'secret'

    setting1 = setting()
    setting2 = setting()
    setting3 = setting()
    setting1.name = 'value1'
    setting2.name = 'value2'
    setting3.name = 'value3'
    config_data.update_setting(setting1)
    config_data.update_setting(setting2)
    config_data.update_setting(setting3, plugin())

# Generated at 2022-06-12 20:58:24.772251
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(ConfigDataSetting('A', 'B'))
    config_data.update_setting(ConfigDataSetting('C', 'D'))
    assert config_data.get_setting('A') == ConfigDataSetting('A', 'B')
    assert config_data.get_setting('C') == ConfigDataSetting('C', 'D')


# Generated at 2022-06-12 20:58:32.311789
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data._global_settings == {}

    from ansiblelint.rules.ConfigureWarnings import ConfigureWarnings
    from ansiblelint.config import Settings
    from ansiblelint.config.rule import RulesCollection

    setting = Settings.get_setting(ConfigureWarnings, {'id': '202'}, RulesCollection)
    config_data.update_setting(setting)
    assert setting.name == 'id'
    assert config_data._global_settings['id'] == setting

# Generated at 2022-06-12 20:58:35.783106
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configData = ConfigData()

    setting = Setting(name='foo')
    configData.update_setting(setting)

    assert configData.get_setting('foo') == setting


# Generated at 2022-06-12 20:58:46.037163
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd._global_settings['abc'] = 'abc'
    cd._global_settings['xyz'] = 'xyz'

    assert len(cd.get_settings()) == 2
    assert len(cd.get_settings(plugin=None)) == 2
    assert cd.get_settings() == cd.get_settings(plugin=None)

    cd._plugins['type1'] = {}
    cd._plugins['type1']['name1'] = {}
    cd._plugins['type1']['name2'] = {}
    cd._plugins['type1']['name1']['abc'] = 'abc'
    cd._plugins['type1']['name1']['xyz'] = 'xyz'
    cd._plugins['type1']['name2']['abc'] = 'abc'
   

# Generated at 2022-06-12 20:58:57.124892
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    
    config_data = ConfigData()

    import inspect
    import os
    import sys

    # Get the directory of the test script
    test_script_dir = os.path.dirname(inspect.currentframe().f_code.co_filename)

    # Get the path of the source code directories
    src_dir = os.path.join(test_script_dir, os.pardir, os.pardir, os.pardir, "src")
    sys.path.append(src_dir)

    from config.setting import Setting
    from plugins.plugin.plugin_info import PluginInfo

    plugin = PluginInfo("TestType", "TestName")
    setting = Setting("TestName", "Test value")

    config_data.update_setting(setting, plugin)

    assert config_data._global_settings == {}
    assert config_

# Generated at 2022-06-12 20:59:05.710194
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import get_plugin_class, Plugin
    from ansible.parsing.plugin_docs import read_docstring

    # Use a copy of the docs so we can modify them, doesn't affect the plugin anymore.
    docs = read_docstring(get_plugin_class(Plugin.CLI))
    assert docs

    plugin = Plugin.CLI()
    data = ConfigData()
    data.update_setting(docs['options'][0], plugin)

    assert data.get_setting('help')

# Generated at 2022-06-12 20:59:13.077504
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting("SHOW_TRACEBACK", "Autocompletion")
    cd.update_setting("SHOW_TRACEBACK", "API")
    cd.update_setting("SHOW_TRACEBACK", None)
    assert cd.get_setting("SHOW_TRACEBACK") is not None
    assert cd.get_setting("SHOW_TRACEBACK", "Autocompletion") is not None
    assert cd.get_setting("SHOW_TRACEBACK", "API") is not None


# Generated at 2022-06-12 20:59:20.095201
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    '''
    test for updating setting for plugins of types 'lookups' and 'filters'
    '''
    cd = ConfigData()
    setting = PluginSetting(
        name='intersect',
        plugin='mylookup',
        plugin_type='lookup',
        default='_unset',
        description='intersect option for lookup plugins',
        value='',
        ini_section=None,
        ini_key=None)
    cd.update_setting(setting)
    assert cd.get_setting('intersect').name == 'intersect'


# Generated at 2022-06-12 20:59:25.404702
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='test1', value='value1', plugin=None))
    config_data.update_setting(Setting(name='test2', value='value2', plugin=None))
    config_data.update_setting(Setting(name='test3', value='value3', plugin=None))

    assert len(config_data.get_settings()) == 3



# Generated at 2022-06-12 20:59:38.349248
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    assert len(config.get_settings()) == 0

    config.update_setting(Setting('name', 'value'))
    assert len(config.get_settings()) == 1
    config.update_setting(Setting('name', 'value2'))
    assert len(config.get_settings()) == 1
    config.update_setting(Setting('name2', 'value'))
    assert len(config.get_settings()) == 2
    config.update_setting(Setting('name3', 'value'))
    assert len(config.get_settings()) == 3


# Generated at 2022-06-12 20:59:40.553218
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting("some_setting") is None
    assert config_data.get_setting("some_setting", "Plugin") is None


# Generated at 2022-06-12 20:59:43.540408
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = get_test_setting()
    plugin = get_test_plugin()
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting(setting.name, plugin)



# Generated at 2022-06-12 20:59:49.649713
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    assert config_data._global_settings == {}
    assert config_data._plugins == {}

    config_data._global_settings = {
            "setting1" : True,
            "setting2" : "some value",
            "setting3" : {
                "key" : "value"
                }
            }
    config_data._plugins = {
            "type1" : {
                "name1" : {
                    "setting1" : True,
                    "setting2" : "some value",
                    "setting3" : {
                        "key" : "value"
                        }
                    }
                }
            }

    # Test valid setting
    setting = config_data.get_setting("setting2")
    assert setting.name == "setting2"
    assert setting.is_global_

# Generated at 2022-06-12 20:59:57.610966
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    # Test for _global_settings
    setting = ansibled_global_setting()
    config_data.update_setting(setting)
    assert len(config_data._global_settings) == 1
    assert config_data._global_settings['retry_files_enabled'] == setting

    # Test for _plugins
    setting = ansibled_plugin_setting()
    config_data.update_setting(setting)
    assert config_data._plugins['callback']['slack']['color'] == setting


# Generated at 2022-06-12 21:00:08.218639
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import os
    import sys
    sys.path.insert(1,os.path.sep.join((sys.path[0].split(os.path.sep))[:-2]+['plugins']))

    from _init import BasePlugin
    import _init

    ansible_plugin = _init.BasePlugin(name="ansible",type=_init.C.DEFAULT)
    ansible_setting = _init.BaseSetting(name="foo")

    config_data = ConfigData()
    config_data.update_setting(ansible_setting)
    setting = config_data.get_setting(ansible_setting.name)
    assert setting.name == ansible_setting.name, "Names for settings do not match"

    my_plugin = BasePlugin(name="my_plugin",type=C.DEFAULT)
    my_setting

# Generated at 2022-06-12 21:00:10.694414
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert settings == []


# Generated at 2022-06-12 21:00:16.592259
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('ansible_connection', 'smart'))
    setting = config_data.get_setting('ansible_connection')
    assert setting.name == 'ansible_connection'
    assert setting.value == 'smart'

    config_data.update_setting(Setting('library', '/usr/share/ansible/plugins/modules'), Plugin('file', 'default'))
    setting = config_data.get_setting('library', Plugin('file', 'default'))
    assert setting.name == 'library'
    assert setting.value == '/usr/share/ansible/plugins/modules'



# Generated at 2022-06-12 21:00:28.804479
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()   # test object

    # test get_setting with an empty setting
    assert config.get_setting("empty") is None

    # test get_setting with an invalid plugin
    assert config.get_setting("empty", "invalid plugin") is None

    # test get_setting with a valid setting and without a plugin
    setting_1 = ("bool", "test_1")
    config.update_setting(setting_1)
    assert config.get_setting("test_1") == setting_1

    # test get_setting with a valid setting and with a plugin
    setting_2 = ("bool", "test_2")
    config.update_setting(setting_2, "valid plugin")
    assert config.get_setting("test_2", "valid plugin") == setting_2


# Generated at 2022-06-12 21:00:36.082716
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configdata = ConfigData()
    setting1 = Setting(name='plugin1_setting1')
    setting2 = Setting(name='plugin1_setting2')
    setting3 = Setting(name='plugin2_setting1')
    configdata.update_setting(setting1, plugin=Plugin(type='plugins',name='plugin1'))
    configdata.update_setting(setting2, plugin=Plugin(type='plugins',name='plugin1'))
    configdata.update_setting(setting3, plugin=Plugin(type='plugins',name='plugin2'))
    assert configdata.get_setting('plugin1_setting1', plugin=Plugin(type='plugins',name='plugin1')).name == 'plugin1_setting1'

# Generated at 2022-06-12 21:00:45.274095
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    instance = ConfigData()

    setting = Setting(name="Verbosity", value="2")
    instance.update_setting(setting)

    plugin = Plugin(type="foo", name="bar")
    instance.update_setting(setting, plugin)



# Generated at 2022-06-12 21:00:49.150355
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = PluginDefinition("SamplePlugin", "lookup")
    setting = Setting("name", "David")
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting("name", plugin) == setting


# Generated at 2022-06-12 21:01:00.501701
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configData = ConfigData()
    setting = Setting(
        name='test_setting',
        description='test setting',
        short_description='test setting',
        value=[1, 2, 3],
        type=SettingType.LIST,
        scope=[]
    )
    configData.update_setting(
        setting=setting
    )

    setting_test = Setting(
        name='test_setting_test',
        description='test setting test',
        short_description='test setting test',
        value=[1, 2, 3, 4],
        type=SettingType.LIST,
        scope=[]
    )
    configData.update_setting(
        setting=setting_test
    )

    settings = configData.get_setting('test_setting')
    assert settings is not None
    assert settings.name == 'test_setting'

# Generated at 2022-06-12 21:01:01.846048
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert data.get_settings() == []

# Generated at 2022-06-12 21:01:11.147321
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.utils.plugin_docs import get_docstring
    from ansible.plugins.loader import get_all_plugin_loaders

    data = ConfigData()

    for loader_type in get_all_plugin_loaders():
        for plugin in loader_type.all():
            doc, plainexamples, returndocs, metadata = get_docstring(plugin, loader_type, verbose=False)

            if doc is not None:
                for setting in doc.get_settings():
                    data.update_setting(setting, plugin)

    assert data.get_setting('connection', None) is not None
    assert data.get_setting('connection', None).name == 'connection'
    assert data.get_setting('connection', None).value == 'smart'
    assert data.get_setting('connection', None).plugin is None



# Generated at 2022-06-12 21:01:16.362996
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    plugin = PluginDependency()
    plugin.name = "plugin1"
    plugin.type = "network"
    setting = PluginSetting()
    setting.name = "setting1"
    config.update_setting(setting, plugin)
    assert config._plugins['network']['plugin1']['setting1'] == setting


# Generated at 2022-06-12 21:01:18.153164
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    
    assert config.get_setting("retries", "core") is None


# Generated at 2022-06-12 21:01:22.204997
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting(Setting('', '', '', '', '', '', ''))
    assert cd._global_settings['fg_color'] == Setting('fg_color', '', '', '', '', '', '')


# Generated at 2022-06-12 21:01:33.449079
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting1 = Setting("setting1", "setting1_value")
    setting2 = Setting("setting2", "setting2_valu2")
    config_data.update_setting(setting1)
    config_data.update_setting(setting2)
    plugin_type = PluginType("test_plugin_type")
    plugin_name = PluginName("test_plugin_name")
    plugin = Plugin(plugin_type, plugin_name)

    config_data.update_setting(setting1, plugin)
    config_data.update_setting(setting2, plugin)
    assert len(config_data.get_settings()) == 2
    assert len(config_data.get_settings(plugin)) == 2



# Generated at 2022-06-12 21:01:38.155084
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    t_config_data = ConfigData()
    t_plugin = Plugin('tplugin')
    t_setting = Setting('tname', 'tvalue')
    t_config_data.update_setting(t_setting, t_plugin)
    assert t_config_data.get_setting('tname', t_plugin) == t_setting


# Generated at 2022-06-12 21:01:55.399498
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert not config_data.get_settings()
    assert not config_data.get_settings(None)
    assert not config_data.get_settings(ConfigData)

# Generated at 2022-06-12 21:02:04.946346
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
	from ansible.plugins.loader import plugin_loader

	# create ConfigData instance
	config_data = ConfigData()
	
	# init variables
	plugin_output_map_init = {'shell': {'name': 'shell', 'doc': None, 'args': []}}
	
	# create Setting instance

# Generated at 2022-06-12 21:02:12.056188
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(ConfigSetting(name='setting1', value='value1', origin='origin1'))
    config_data.update_setting(ConfigSetting(name='setting2', value='value2', origin='origin2'))

    assert get_setting(config_data, name='setting1') == 'value1'
    assert get_setting(config_data, name='setting2') == 'value2'


# Generated at 2022-06-12 21:02:20.155809
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.config.base import Setting

    config_data = ConfigData()
    config_data.update_setting(Setting('ansible_user', 'ansible', '', 'user that ansible runs as', "__global__"))
    assert config_data.get_setting('ansible_user').value == 'ansible'
    assert config_data.get_setting('ansible_user').default == 'ansible'
    assert config_data.get_setting('ansible_user').description == 'user that ansible runs as'
    assert config_data.get_setting('ansible_user').origin == "__global__"
    assert config_data.get_setting('ansible_user').action == 'store'
    assert config_data.get

# Generated at 2022-06-12 21:02:30.510837
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import sys
    sys.path.append("..")
    from lib.config import ConfigData
    config_data = ConfigData()

    from test.unit.lib.config.test_config_setting import test_ConfigSetting_init
    setting = test_ConfigSetting_init()

    import ansible.utils.plugin_docs
    plugin_type = ansible.utils.plugin_docs.C.DOCUMENTABLE_PLUGINS[0]
    plugin_name = ansible.utils.plugin_docs.C.DOCUMENTABLE_PLUGINS[plugin_type][0]
    plugin_version = ansible.utils.plugin_docs.C.DOCUMENTABLE_PLUGINS[plugin_type][plugin_name][0]
    plugin = ansible.utils.plugin_docs.Plugin(plugin_type, plugin_name, plugin_version)

# Generated at 2022-06-12 21:02:41.732813
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()
    assert [] == cd.get_settings()
    assert cd.get_setting('test_setting') is None

    cd._global_settings = {'test_setting': 'setting1'}
    assert cd.get_setting('test_setting') == 'setting1'

    cd._plugins['some_type'] = {'some_name': {'test_setting': 'setting2'}}
    assert cd.get_setting('test_setting') == 'setting1'
    assert cd.get_setting('test_setting', plugin=None) == 'setting1'
    assert cd.get_setting('test_setting', plugin='some_type.some_name') == 'setting2'
    assert cd.get_setting('test_setting', plugin='other_type.other_name') is None
    assert cd.get_settings()

# Generated at 2022-06-12 21:02:53.296181
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # when
    g = ConfigData()
    setting1 = ConfigSetting(name="setting1", value="default value")
    setting2 = ConfigSetting(name="setting2", value="default value")
    setting3 = ConfigSetting(name="setting3", value="default value")
    setting4 = ConfigSetting(name="setting4", value="default value")
    setting5 = ConfigSetting(name="setting5", value="default value")
    g.update_setting(setting1)
    g.update_setting(setting2)
    g.update_setting(setting3, plugin="Plugin1")
    g.update_setting(setting4, plugin="Plugin2")
    g.update_setting(setting5, plugin="Plugin3")

    # then
    assert g.get_setting('setting1') == setting1

# Generated at 2022-06-12 21:02:54.970036
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    # config_data.update_setting(setting = 1, plugin = 2)

# Generated at 2022-06-12 21:02:55.736522
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass

# Generated at 2022-06-12 21:03:07.029566
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    plugin_type = 'module'
    plugin_name = 'copy'
    setting_name = 'ACTION_WARNINGS'
    setting_value = '1'
    config_data = ConfigData()
    assert config_data.get_settings() == []
    config_data.update_setting(Setting(setting_name, setting_value))
    assert config_data.get_settings() == [Setting(setting_name, setting_value)]
    config_data.update_setting(Setting(setting_name, setting_value, Plugin(plugin_type, plugin_name)))
    assert config_data.get_settings() == [Setting(setting_name, setting_value)]
    assert config_data.get_settings(Plugin(plugin_type, plugin_name)) == [Setting(setting_name, setting_value)]
