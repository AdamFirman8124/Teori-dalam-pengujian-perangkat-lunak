

# Generated at 2022-06-12 20:53:33.114760
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    setting1 = Setting('setting1', 'global', 'test.setting1.plugin', 'test.setting1.value', 1)
    setting2 = Setting('setting2', 'global', 'test.setting2.plugin', 'test.setting2.value', 2)
    setting3 = Setting('setting3', 'global', 'test.setting3.plugin', 'test.setting3.value', 3)
    setting4 = Setting('setting4', 'global', 'test.setting4.plugin', 'test.setting4.value', 4)
    setting5 = Setting('setting5', 'global', 'test.setting5.plugin', 'test.setting5.value', 5)
    setting6 = Setting('setting6', 'global', 'test.setting6.plugin', 'test.setting6.value', 6)

# Generated at 2022-06-12 20:53:39.105243
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Arrange
    config_data = ConfigData()
    plugin = Plugin('plugin', 'plugin_type')
    setting = Setting('setting', 'setting_value')

    # Act
    config_data.update_setting(setting, plugin)

    # Assert
    assert config_data._plugins['plugin_type']['plugin']['setting'].value == 'setting_value'



# Generated at 2022-06-12 20:53:48.656666
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    import configparser
    import ansibullbot.parsers.config

    config_parser = configparser.ConfigParser()
    config_parser.add_section('defaults')
    config_parser.set('defaults', 'foo', 'bar')
    config_parser.set('defaults', 'baz', 'baz')

    config_parser.add_section('action_plugin')
    config_parser.set('action_plugin', 'foo', 'quux')
    config_parser.set('action_plugin', 'bar', 'quux')
    config_parser.set('action_plugin', 'baz', 'quux')

    config_parser.add_section('become_plugin')
    config_parser.set('become_plugin', 'foo', 'quux')

# Generated at 2022-06-12 20:53:52.270456
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting = {}
    assert config.get_setting('foo') == None
    assert config.get_setting('foo', 'bar') == None
    assert config.get_setting('foo', setting) == None


# Generated at 2022-06-12 20:53:56.924646
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('a', '', '', '', '', False, False))
    config_data.update_setting(Setting('b', '', '', '', '', False, False))

    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'a'
    assert settings[1].name == 'b'


# Generated at 2022-06-12 20:54:02.455285
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    print("Unit test for method get_settings of class ConfigData: " + str(config_data.get_settings()))

test_ConfigData_get_settings()

# Generated at 2022-06-12 20:54:09.073841
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = ConfigPlugin('connection', 'ssh_connection')
    setting = ConfigSetting('ansible_ssh_pass', 'password', plugin)
    config_data.update_setting(setting, plugin)
    assert config_data._global_settings == {}
    assert config_data._plugins['connection']['ssh_connection']['ansible_ssh_pass'].name == 'ansible_ssh_pass'
    assert config_data._plugins['connection']['ssh_connection']['ansible_ssh_pass'].value == 'password'


# Generated at 2022-06-12 20:54:20.658911
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    from units.mock.loader import DictDataLoader
    from units.plugins.core.vars import VariableManager
    from ansible.config.data import ConfigData
    from ansible.plugins.loader import vars_loader
    v = VariableManager()
    v.set_loader(vars_loader)
    v.extra_vars = {'local_connection': {'type': 'local', 'name': 'local'}}

    plugin_name = 'local'
    plugin = v.get_vars_manager()._get_plugin_from_context(plugin_name)

    data = dict(connection=dict(type='local', name='local'))
    loader = DictDataLoader(data)
    config_data = ConfigData()

# Generated at 2022-06-12 20:54:31.450348
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from PluginSpec import PluginSpec
    from SettingSpec import SettingSpec

    cd = ConfigData()

    setting1 = SettingSpec('setting1', 'value1')
    setting2 = SettingSpec('setting2', 'value2')
    setting3 = SettingSpec('setting3', 'value3')
    setting4 = SettingSpec('setting4', 'value4')

    cd.update_setting(setting1)
    cd.update_setting(setting2, PluginSpec('connection', 'local'))
    cd.update_setting(setting3, PluginSpec('connection', 'ssh'))
    cd.update_setting(setting4, PluginSpec('lookup', 'file'))

    assert cd.get_setting('setting1').name == 'setting1'
    assert cd.get_setting('setting1').value == 'value1'


# Generated at 2022-06-12 20:54:36.183779
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('environments','/etc/ansible/environments'))
    setting = config_data.get_setting('environments')
    assert setting.name == 'environments'
    assert setting.value == '/etc/ansible/environments'


# Generated at 2022-06-12 20:54:40.634298
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert()

# Generated at 2022-06-12 20:54:42.247104
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass


# Generated at 2022-06-12 20:54:48.036158
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint.rules.RuleLoader import Rule

    config_data = ConfigData()

    assert config_data.get_setting('test') == None
    assert config_data.get_settings() == []
    assert config_data.get_setting('test', Rule('test', {'id': 'test'})) == None
    assert config_data.get_settings(Rule('test', {'id': 'test'})) == []

# Generated at 2022-06-12 20:54:50.778026
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting1 = config.get_setting('foo')
    assert setting1 is None
    setting2 = config.get_setting('foo', plugin=Plugin('lookup', 'foo'))
    assert setting2 is None


# Generated at 2022-06-12 20:54:57.090929
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings().__len__() == 0
    config_data.update_setting(Setting('test_setting', 'test_value'))
    config_data.update_setting(Setting('test_setting', 'test_value'))
    assert config_data.get_settings().__len__() == 2


# Generated at 2022-06-12 20:55:00.351044
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting("SomeItem", "value"),Plugin("test","type"))
    config_data.update_setting(Setting("AnotherItem", "another value"),Plugin("test","type"))
    assert len(config_data.get_settings(Plugin("test", "type"))) == 2


# Generated at 2022-06-12 20:55:04.032673
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    assert config_data.get_setting('foo') is None
    assert config_data.get_setting('foo', 'bar') is None


# Generated at 2022-06-12 20:55:13.756876
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    obj = ConfigData()

    setting = Settings()
    obj.update_setting(setting, _Plugin("Module","Test"))
    assert obj.get_setting("Conf_Test_key1").value == "Conf_Test_value1"

    setting = Settings("Conf_Test_key3", "Conf_Test_value3")
    obj.update_setting(setting, _Plugin("Module","Test"))
    assert obj.get_setting("Conf_Test_key3").value == "Conf_Test_value3"

    setting = Settings("Conf_Test_key1", "Conf_Test_value1_updated")
    obj.update_setting(setting, _Plugin("Module","Test"))
    assert obj.get_setting("Conf_Test_key1").value == "Conf_Test_value1_updated"


# Generated at 2022-06-12 20:55:19.395224
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Create config data, add settings and check if settings are returned as expected
    config_data = ConfigData()
    config_data.update_setting(Setting('setting1', 'value1'), None)
    config_data.update_setting(Setting('setting2', 'value2'), Plugin('test', 'test_name'))
    config_data.update_setting(Setting('setting3', 'value3'), Plugin('test2', 'test_name2'))
    assert config_data.get_settings() == [Setting('setting1', 'value1')]
    assert config_data.get_settings(Plugin('test', 'test_name')) == [Setting('setting2', 'value2')]
    assert config_data.get_settings(Plugin('test2', 'test_name2')) == [Setting('setting3', 'value3')]
   

# Generated at 2022-06-12 20:55:25.158402
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansiblelint.rules import AnsibleLintRule

    config_data = ConfigData()

    setting = AnsibleLintRule('foo', {})
    config_data.update_setting(setting)

    assert setting == config_data.get_setting('foo')

    setting = AnsibleLintRule('bar', {})
    config_data.update_setting(setting, AnsibleLintRule)

    assert setting == config_data.get_setting('bar', AnsibleLintRule)

# Generated at 2022-06-12 20:55:33.722922
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = Setting("var_name", "var_value")
    plugin1 = Plugin("module", "plugin_name")
    config_data.update_setting(setting1, plugin1)
    assert "var_name" in config_data._plugins["module"]["plugin_name"]


# Generated at 2022-06-12 20:55:44.518565
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class Plugin:
        def __init__(self):
            pass
        def set_type(self, type):
            self.type = type
        def set_name(self, name):
            self.name = name

    class Setting:
        def __init__(self):
            pass
        def set_name(self, name):
            self.name = name

    # create a ConfigData object
    config = ConfigData()

    # create a plugin object
    plugin = Plugin()
    plugin.set_type("action")
    plugin.set_name("ping")

    # create a setting object
    setting = Setting()
    setting.set_name("timeout")

    # add setting object to ConfigData object
    config.update_setting(setting, plugin)

    # check that the setting object was added properly
    assert config._global_settings

# Generated at 2022-06-12 20:55:52.873776
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from collections import namedtuple
    from pytest import raises
    from content_config_reader import ContentConfig, ConfigData

    Plugin = namedtuple('Plugin', 'type name')

    # test if method update_setting of class ConfigData works correctly
    # with a global setting
    config_data = ConfigData()
    config_data.update_setting(ContentConfig('test', 'Test', 'test_value'))
    assert config_data.get_setting('test') is not None

    # test if method update_setting of class ConfigData works correctly
    # with a plugin setting
    config_data = ConfigData()
    plugin = Plugin('type', 'name')
    config_data.update_setting(ContentConfig('test', 'Test', 'test_value', plugin))
    assert config_data.get_setting('test', plugin) is not None



# Generated at 2022-06-12 20:55:57.716740
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = DeviceSetting(name="Plugin1",value=1)
    config_data.update_setting(setting)
    setting_retrieved = config_data.get_setting("Plugin1")
    assert setting_retrieved.name == "Plugin1"
    assert setting_retrieved.value == 1


# Generated at 2022-06-12 20:56:01.643771
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting(name="test1")
    config_data.update_setting(setting, plugin=None)
    assert setting == config_data.get_setting("test1", plugin=None)

# Generated at 2022-06-12 20:56:08.807299
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    setting = Setting(name='setting_name', value=None)
    plugin = Plugin('collection', 'ansible.collections.example')

    config_data.update_setting(setting, plugin)

    assert config_data._global_settings == {}
    assert config_data._plugins == {'collection': {'ansible.collections.example': {'setting_name': setting}}}

    config_data.update_setting(setting)

    assert config_data._global_settings == {'setting_name': setting}
    assert config_data._plugins == {'collection': {'ansible.collections.example': {'setting_name': setting}}}


# Generated at 2022-06-12 20:56:16.290659
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from config_data_class import ConfigDataClass
    config_data._global_settings = {'is_executing': config_data.get_setting('is_executing') or ConfigDataClass(name = 'is_executing', value = 'string')}
    config_data.update_setting(config_data.get_setting('is_executing'))

# Generated at 2022-06-12 20:56:27.885882
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='name_value_1', type='type_value_1', value='value_1'))
    config_data.update_setting(Setting(name='name_value_2', type='type_value_2', value='value_2'))
    config_data.update_setting(Setting(name='name_value_3', type='type_value_3', value='value_3'))
    assert config_data.get_setting(name='name_value_1').value == 'value_1'
    assert config_data.get_setting(name='name_value_2').value == 'value_2'
    assert config_data.get_setting(name='name_value_3').value == 'value_3'
    assert config_data.get

# Generated at 2022-06-12 20:56:34.935126
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = Setting('test1')
    config_data.update_setting(setting1)
    assert config_data.get_setting('test1') is setting1

    setting2 = Setting('test2', 'TestPlugin')
    config_data.update_setting(setting2)
    assert config_data.get_setting('test2', 'TestPlugin') is setting2

    setting3 = Setting('test3', 'TestPlugin2')
    config_data.update_setting(setting3)
    assert config_data.get_setting('test3', 'TestPlugin2') is setting3

    setting4 = Setting('test4', 'TestPlugin')
    config_data.update_setting(setting4)
    assert config_data.get_setting('test4', 'TestPlugin') is setting4


# Unit test

# Generated at 2022-06-12 20:56:35.527199
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
   pass

# Generated at 2022-06-12 20:56:41.173541
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = Setting('foo', 'bar')
    config_data.update_setting(setting1)
    
    assert config_data.get_setting(setting1.name) == setting1


# Generated at 2022-06-12 20:56:49.257553
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    cd.update_setting(Setting('month', 'april'))
    cd.update_setting(Setting('version', '2.9'))
    assert (cd.get_setting('month')  == Setting('month', 'april'))
    assert (cd.get_setting('version')  == Setting('version', '2.9'))
    assert (cd.get_setting('day')  == None)
    assert (cd.get_setting('year')  == None)


# Generated at 2022-06-12 20:56:51.942773
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    config_data.update_setting(Setting(name='display_skipped_hosts', value='False'))
    assert config_data.get_setting('display_skipped_hosts').value == 'False'


# Generated at 2022-06-12 20:56:57.210812
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    config.update_setting('a')
    config.update_setting('a', 'b')
    config.update_setting('a', 'b', 'c')
    assert config.get_setting('a') == 'a'
    assert config.get_setting('b') is None
    assert config.get_setting('a', 'b') == 'a'
    assert config.get_setting('b', 'b') is None
    assert config.get_setting('a', 'b', 'c') == 'a'
    assert config.get_setting('b', 'b', 'c') is None



# Generated at 2022-06-12 20:57:05.932597
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Declare class object
    configData = ConfigData()

    # Add global setting to class object
    configData.update_setting(Setting('global_setting', 'global_value', 'global_comment'))

    # Add local setting to class object
    configData.update_setting(Setting('local_setting', 'local_value', 'local_comment'), Plugin('test_plugin'))

    # Add private setting to class object
    configData.update_setting(Setting('private_setting', 'private_value', 'private_comment', True), Plugin('test_plugin'))

    # 1) Test case: Get global settings from class object
    assert configData.get_settings() == [Setting('global_setting', 'global_value', 'global_comment')]

    # 2) Test case: Get public local settings from class object
    assert configData.get_

# Generated at 2022-06-12 20:57:07.996428
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('setting1') == None
    assert config_data.get_setting('setting2') == None


# Generated at 2022-06-12 20:57:15.426832
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo_global', 'foo_value_global'))
    config_data.update_setting(Setting('bar_global', 'bar_value_global'))

    config_data.update_setting(Setting('foo_local', 'foo_value_local'), Plugin('bar', 'local'))
    config_data.update_setting(Setting('bar_local', 'bar_value_local'), Plugin('bar', 'local'))

    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'foo_global'
    assert settings[1].name == 'bar_global'

    settings = config_data.get_settings(Plugin('bar', 'local'))
    assert len(settings) == 2

# Generated at 2022-06-12 20:57:26.615139
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class Plugin:

        def __init__(self, type, name):
            self.type = type
            self.name = name

    c = ConfigData()
    c.update_setting("v1", Setting("p1", "v1"))
    c.update_setting("v2", Setting("p2", "v2", "plugin1"))
    c.update_setting("v3", Setting("p3", "v3", "plugin2"))

    p = Plugin("p1", "plugin1")
    settings = c.get_settings(p)

    assert len(settings) == 2

    assert settings[0].name == "p2"
    assert settings[0].value == "v2"
    assert settings[0].plugin == "plugin1"


# Generated at 2022-06-12 20:57:36.472299
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cfg = ConfigData()
    # Plugins are type:name pairs with a short and a long name option
    cfg.update_setting(Setting('short', 'short_name'))
    cfg.update_setting(Setting('long', 'long_name'))
    cfg.update_setting(Setting('short', 'short_name', 'cache', 'lookup'))
    cfg.update_setting(Setting('long', 'long_name', 'cache', 'lookup'))
    cfg.update_setting(Setting('short', 'short_name', 'connection', 'ssh'))
    cfg.update_setting(Setting('long', 'long_name', 'connection', 'ssh'))

    result = cfg.get_settings()
    assert len(result) == 4
    assert result[0].name == 'short_name'

# Generated at 2022-06-12 20:57:42.503537
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create a class instance to unit test with
    config = ConfigData()

    # Check for no available plugins where plugin is set to None
    assert config.get_settings() == []

    # Check for no available plugins where plugin is set to Global
    from ansible.plugins.loader import PluginLoader

    plugin = PluginLoader.get('connection', 'local')._load_plugin_namespace_by_type()
    assert config.get_settings(plugin) == []



# Generated at 2022-06-12 20:57:57.885374
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()

    from ansible.config.setting import Setting
    
    plugin = Setting(name='test',
                     version='v1.0.0',
                     type='Collector',
                     path='/path/to/module')
    setting = Setting(name='foo', value='bar')
    config.update_setting(setting, plugin)
    
    assert config._global_settings.get('foo') is None

    setting = config.get_setting('foo', plugin)
    assert setting.name == 'foo'
    assert setting.value == 'bar'

    setting = Setting(name='foo', value='buzz')
    config.update_setting(setting, plugin)
    setting = config.get_setting('foo', plugin)
    assert setting.value == 'buzz'

    

# Generated at 2022-06-12 20:58:01.729180
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    config_data.update_setting("test")

    settings = config_data.get_settings()
    assert(len(settings) == 1)
    assert(settings[0] == "test")

# Generated at 2022-06-12 20:58:09.914540
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import sys
    import os
    import inspect
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))))
    from plugins.lib.configdata import ConfigData
    from plugins.lib.configfile import ConfigFile
    configdata = ConfigData()
    testconfig_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), "testdata", "config_file.ini")
    plugin = ConfigFile(testconfig_file)
    configdata.update_setting(plugin.get_setting("timeout"))

# Generated at 2022-06-12 20:58:16.003911
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()
    config.update_setting(ConfigData.Setting('setting1','value1',None))
    config.update_setting(ConfigData.Setting('setting2','value2',None))

    assert config.get_setting('setting1') == 'value1'
    assert config.get_setting('setting2') == 'value2'
    assert config.get_setting('setting3') is None
    assert config.get_setting('setting4', ConfigData.Plugin('plugin_type1','plugin_name1')) is None



# Generated at 2022-06-12 20:58:21.979717
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Import
    from ansiblelint.rules.AnsibleLintRule import AnsibleLintRule
    from ansiblelint.rules.ShellUseCommandRule import ShellUseCommandRule
    from ansiblelint.rules.LineTooLongRule import LineTooLongRule
    # Instantiate ConfigData
    c = ConfigData()
    # Test with plugin set to None
    # Setting up a new AnsibleLintRule
    rule = AnsibleLintRule('999', 'Line is too long ({{x}}>{{y}})',"")
    rule.id = '999'
    rule.shortdesc = 'Line is too long ({{x}}>{{y}})'
    rule.description = ''
    rule._tags = ['formatting', 'whitespace']
    rule.add_match_type('line-too-long')
    # Assert

# Generated at 2022-06-12 20:58:32.774243
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()

    # update a global setting
    s = Setting(name='test', plugintype=None, pluginname=None, value='1', plugin=None)
    cd.update_setting(s)
    assert cd._global_settings['test'].name == 'test'
    assert cd._global_settings['test'].value == '1'

    # update a plugin setting
    p = Plugin('test', 'test', 'test', plugin=None)
    s = Setting(name='test', plugintype='test', pluginname='test', value='2', plugin=p)
    cd.update_setting(s)
    assert cd._plugins['test']['test']['test'].name == 'test'
    assert cd._plugins['test']['test']['test'].value == '2'

#

# Generated at 2022-06-12 20:58:42.040044
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    class Setting(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    class Plugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    # update global setting value
    config = ConfigData()
    setting = Setting("foo", "foo")
    config.update_setting(setting)
    assert config.get_setting("foo") == setting

    # update global setting value
    config = ConfigData()
    plugin_type = 'foo'
    plugin_name = 'bar'
    setting = Setting("foo", "foo")
    plugin = Plugin(plugin_type, plugin_name)
    config.update_setting(setting, plugin=plugin)

# Generated at 2022-06-12 20:58:46.522041
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    config_data.update_setting(Setting('timeout', '5'))
    assert config_data._global_settings['timeout'].value == '5'

    config_data.update_setting(Setting('timeout', '10', 'network.yml'))
    assert config_data._plugins['network.yml']['timeout'].value == '10'


# Generated at 2022-06-12 20:58:52.206994
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_setting = Setting("time", "5", "", "", "", None)
    config_data.update_setting(test_setting)
    settings = config_data.get_settings()
    assert(len(settings) == 1)
    assert(settings[0].value == "5")


# Generated at 2022-06-12 20:58:53.661289
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings() == []


# Generated at 2022-06-12 20:59:14.204866
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    import unittest
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.plugins.loader import PluginLoader
    from ansible.utils.plugin_docs import get_docstring
    import ansible.constants

    settings = config_data.get_settings()
    assert len(settings) == 0

    # check with action plugin
    file = 'copy'
    name = 'copy'
    plugin = PluginLoader.find_plugin(name, 'action')

# Generated at 2022-06-12 20:59:22.529887
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_data = ConfigData()
    setting1 = Setting('setting1', 'string', 'test')
    setting2 = Setting('setting2', 'string', 'test')
    setting3 = Setting('setting3', 'string', 'test')
    test_data.update_setting(setting1)
    test_data.update_setting(setting2)
    test_data.update_setting(setting3, plugin=Plugin('plugin_type', 'plugin_name'))
    actual = test_data.get_settings()
    assert len(actual) == 2
    assert setting1 in actual
    assert setting2 in actual
    assert setting3 not in actual


# Generated at 2022-06-12 20:59:32.021165
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    setting_global_1 = {'name': 'test_global_1',
                        'default': False,
                        'data': False}
    setting_global_2 = {'name': 'test_global_2',
                        'default': True,
                        'data': True}
    setting_module_1 = {'name': 'test_module_1',
                        'default': 'ansible',
                        'data': 'ansible'}
    setting_module_2 = {'name': 'test_module_2',
                        'default': 'ansible',
                        'data': 'ansible'}
    setting_module_3 = {'name': 'test_module_3',
                        'default': 'ansible',
                        'data': 'ansible'}

    config_data = ConfigData()

    # Test global settings
    config_data

# Generated at 2022-06-12 20:59:39.447662
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # prepare config data
    config_data = ConfigData()
    plugin = path_plugin.PathPlugin()
    plugin.name = "git"
    plugin.type = "inventory"

    # setting 1, with type and description
    setting1 = path_setting.PathSetting(name='paths', type='ListOfStrings', default='', description='Specify paths for the plugin to scan')
    setting1.value = ['/path1']
    config_data.update_setting(setting1, plugin)

    # setting1.value should be list
    assert isinstance(setting1.value, list)

    # setting 2, with type
    setting2 = path_setting(name='unknown_variable', type='String', default='', description='Specify default variable for unknown hosts')
    setting2.value = 'var1'
    config_data.update

# Generated at 2022-06-12 20:59:46.946927
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from units.mock.loader import DictDataLoader
    from units.plugins.vars.test_vars import TestVarsPlugin as FakeVarsPlugin

    fake_value = 'fake_value'

    fake_vars_plugin = FakeVarsPlugin()
    fake_vars_plugin.name = 'fake_vars_plugin'
    fake_vars_plugin.P, fake_vars_plugin.D = {}, {}
    fake_vars_plugin.P['test_vars_plugin_setting'] = {'default': fake_value, 'type': 'str', 'env': [], 'ini': []}

    fake_data_loader = DictDataLoader({'fake_vars_plugin.yml': '''
    test_vars_plugin_setting: fake_setting_value
    '''})

    fake

# Generated at 2022-06-12 20:59:49.664654
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('display_skipped_hosts', 'on'))
    assert config_data._global_settings['display_skipped_hosts'].value == 'on'


# Generated at 2022-06-12 20:59:57.654670
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    settings = [{'name': 'ANSIBLE_LIBRARY'}, {'name': 'ANSIBLE_MODULE_UTILS'}, {'name': 'ANSIBLE_STDOUT_CALLBACK'}]

    config_data = ConfigData()

    for setting in settings:
        config_data.update_setting(setting)

    # Check that settings have been added to global settings
    for setting in settings:
        assert setting['name'] in config_data._global_settings


if __name__ == '__main__':
    test_ConfigData_update_setting()

# Generated at 2022-06-12 21:00:08.284506
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # testing that a config can be created properly
    config = ConfigData()

    # testing that a new config has no setting
    settings = config.get_settings()
    assert len(settings) == 0

    # testing that a config setting can be updated
    from ansible.plugins.loader import get_plugin_class
    from ansible.plugins.test.test_test import TestTest

    test_test = get_plugin_class('test', 'test')
    config.update_setting(test_test.get_option('test_setting_name'))
    settings = config.get_settings()
    assert len(settings) == 1

    # testing that a config setting can be updated with no plugin
    config.update_setting(test_test.get_option('test_setting_name'))
    settings = config.get_settings()
    assert len

# Generated at 2022-06-12 21:00:13.001179
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data = ConfigData()
    config_data._global_settings['test_setting'] = {"a"}
    plugin = 'test_plugin'
    assert({'a'} == config_data.get_setting('test_setting', plugin))
    assert([] == config_data.get_setting('test_setting'))



# Generated at 2022-06-12 21:00:15.117724
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    print("Global settings: ")
    for setting in data.get_settings():
        print("- " + setting.name + ": " + setting.value)


# Generated at 2022-06-12 21:00:44.063631
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    # Test None
    assert config_data.get_settings() == []
    # Test setting_type == 'string'
    setting = ConfigSetting(
        name='string_setting',
        setting_type='string',
        value='string_value',
        aliases=[],
        description='string description',
        category='string category')
    config_data.update_setting(setting)
    assert config_data.get_settings() == [setting]
    # Test setting_type == 'bool'
    setting = ConfigSetting(
        name='bool_setting',
        setting_type='bool',
        value='True',
        aliases=[],
        description='bool description',
        category='bool category')
    config_data.update_setting(setting)

# Generated at 2022-06-12 21:00:52.918686
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import unittest

    class TestingConfigData(unittest.TestCase):

        def test_get_settings(self):
            configData = ConfigData()

            self.assertEqual(configData.get_settings(), [])

            configData.update_setting(Setting('foo', 'bar'))
            configData.update_setting(Setting('foo.', 'foobar'))
            configData.update_setting(Setting('baz', 42), Plugin('foo', 'bar'))
            configData.update_setting(Setting('baz.', 'bar'))
            configData.update_setting(Setting('qux', False))

            settings = [s.name for s in configData.get_settings()]
            self.assertEqual(settings, ['foo', 'foo.', 'qux'])


# Generated at 2022-06-12 21:00:57.231918
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    setting = ConfigSetting("test_setting", "", "", "", "", "", "")
    config_data.update_setting(setting)

    assert setting in config_data.get_settings()
    assert config_data.get_setting("test_setting") == setting


# Generated at 2022-06-12 21:01:01.009289
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    print(cd._global_settings)
    print(cd._plugins)

test_ConfigData_update_setting()

# Generated at 2022-06-12 21:01:10.521264
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    from unittest import TestCase
    from unittest import mock
    from lib.config.data import ConfigData
    from lib.config.setting import ConfigSetting
    from lib.config.setting import ConfigSettingBool
    from lib.config.setting import ConfigSettingInt
    from lib.config.setting import ConfigSettingList
    from lib.config.setting import ConfigSettingPath
    from lib.config.setting import ConfigSettingString
    from lib.config.setting import ConfigSettingVersion

    class ConfigDataTest(TestCase):
        def test_get_settings(self):
            config_data = ConfigData()


# Generated at 2022-06-12 21:01:17.066584
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configSetting = ConfigSetting(name="name",
                                  value_type=SettingType.BOOLEAN,
                                  scope=Scope.pattern,
                                  short_description="description",
                                  long_description="long description",
                                  default_value=False,
                                  read_only=False,
                                  require_restart=False)
    configData.update_setting(configSetting)


# Generated at 2022-06-12 21:01:26.861455
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    settings = ConfigData()

    setting1 = ConfigSetting(name='setting1')
    settings.update_setting(setting1)

    assert isinstance(settings._global_settings, dict)
    assert isinstance(settings._plugins, dict)
    assert 'setting1' in settings._global_settings
    assert 'setting1' in settings.get_settings()
    assert settings.get_setting('setting1') == setting1

    setting2 = ConfigSetting(name='setting2')
    settings.update_setting(setting2, Plugin('test', 'test-plugin'))

    assert 'test' in settings._plugins
    assert 'test-plugin' in settings._plugins['test']
    assert 'setting2' in settings._plugins['test']['test-plugin']

# Generated at 2022-06-12 21:01:31.646267
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    config_data.update_setting('setting1')
    assert config_data.get_setting('setting1') == 'setting1'
    config_data.update_setting('setting2')
    assert config_data.get_setting('setting2') == 'setting2'
    assert config_data.get_setting('setting3') is None


# Generated at 2022-06-12 21:01:40.790777
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    CONFIG_DATA = ConfigData()

    config_setting_global = ConfigSetting(name="ansible_managed",
                                          description="Line used as a header in ansible managed files to indicate modification is done by ansible and shouldn't be done manually",
                                          default="Ansible managed",
                                          current="Ansible managed",
                                          origin="plugin",
                                          type="str",
                                          level="basic")

    CONFIG_DATA.update_setting(config_setting_global)
    assert CONFIG_DATA.get_setting("ansible_managed") is not None
    assert CONFIG_DATA.get_setting("ansible_managed").name == "ansible_managed"

# Generated at 2022-06-12 21:01:47.939328
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    conf = ConfigData()
    setting1 = Setting('setting1', None, None, 'default_setting1')
    setting2 = Setting('setting2', None, None, 'default_setting2')
    conf.update_setting(setting1)
    conf.update_setting(setting2)
    assert [setting1, setting2] == conf.get_settings()



# Generated at 2022-06-12 21:02:11.088529
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting("dummy_setting")
    assert cd._global_settings == "dummy_setting"


# Generated at 2022-06-12 21:02:17.899067
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data._global_settings = {'foo': 'bar', 'wiz': 'bang'}
    config_data._plugins = {'action': {'my_custom_action': {'foo': 'wiz'}}}

    assert config_data.get_setting('foo') == 'bar'
    assert config_data.get_setting('wiz') == 'bang'
    assert config_data.get_setting('foo', 'action.my_custom_action') == 'wiz'


# Generated at 2022-06-12 21:02:29.186443
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    from ansible.plugins.action import ActionBase
    from ansible.plugins.doc_fragments import DOC_ANSIBLE_FLAGS, DOC_COMMON_ARGUMENTS
    from ansible.module_utils.six.moves.urllib.error import URLError

    class MockModule(ActionBase):
        ACTIONS = []
        ARGSPECS = {}
        IGNORE_RESULT = True

        def __init__(self, action, *args, **kwargs):
            self.action = action
            self.args = args
            self.kwargs = kwargs

    class MockPlugin:
        def __init__(self, name, type):
            self.name = name
            self.type = type


# Generated at 2022-06-12 21:02:34.324975
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config.update_setting(Setting("host", "192.168.0.1"))
    assert config.get_setting("host") == "192.168.0.1"



# Generated at 2022-06-12 21:02:41.796726
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    # Create configdata instance
    configdata = ConfigData()

    # Add one global setting and one setting for a module
    configdata.update_setting(Setting('global_setting', 'global_value'))
    plugin = Plugin('local', 'test_module')
    configdata.update_setting(Setting('module_setting', 'module_value'), plugin)

    # Get the global setting and module setting and test output
    assert configdata.get_setting('global_setting').value == 'global_value'
    assert configdata.get_setting('module_setting', plugin).value == 'module_value'


# Generated at 2022-06-12 21:02:52.116635
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    # add three Setting objects to _global_settings
    config_data._global_settings = {'foo': Setting('foo'), 'bar': Setting('bar'), 'baz': Setting('baz')}
    # in this test, none plugin is defined, so all 3 Setting objects in _global_settings should be returned
    print(config_data.get_settings())
    assert (len(config_data.get_settings()) == 3)
    # the same test but with a defined plugin
    plugin = Plugin('foo', 'bar')
    print(config_data.get_settings(plugin))
    assert (len(config_data.get_settings(plugin)) == 3)



# Generated at 2022-06-12 21:02:54.929862
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import call
    import collections
    import unittest.mock as mock

    config_data = ConfigData()

    # Setting object
    plugin = mock.Mock()
    plugin.type = 'connection'
    plugin.name = 'ssh'
    setting = mock.Mock()
    setting.name = 'retries'

    # Verify calling get_setting with correct settings returns the correct settings
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting(setting.name, plugin) == setting


# Generated at 2022-06-12 21:02:59.999415
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    assert len(data.get_settings()) == 0
    assert data.get_setting('test') is None
    setting = Setting('test', 'test', 'test', 'test')
    data.update_setting(setting)
    assert len(data.get_settings()) == 1
    assert len(data.get_settings(Plugin('test', 'test'))) == 0
    assert data.get_setting('test') is not None
    assert data.get_setting('test').plugin is None



# Generated at 2022-06-12 21:03:10.367077
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='ansible_connection', value='ansible.netcommon.network_cli'))
    config_data.update_setting(Setting(name='ansible_network_os', value='junos'))
    assert(config_data.get_setting(name='ansible_network_os').value == 'junos')
    assert (config_data.get_setting(name='ansible_connection').value == 'ansible.netcommon.network_cli')
    assert (config_data.get_setting(name='ansible_network_os', plugin=NetworkPlugin(type='resource', name='network_cli')) is None)



# Generated at 2022-06-12 21:03:17.256940
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting_1 = Setting('host_key_checking', 'True')
    setting_2 = Setting('host_key_checking', 'True')
    config_data.update_setting(setting_1)
    config_data.update_setting(setting_2)
    got_setting = config_data.get_setting('host_key_checking')
    assert got_setting.name == 'host_key_checking'
    assert got_setting.value == 'True'

