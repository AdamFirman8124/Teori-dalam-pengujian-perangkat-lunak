

# Generated at 2022-06-12 20:53:30.749510
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('key1','value1'))
    assert (config_data.get_setting('key1') == Setting('key1','value1'))

# Generated at 2022-06-12 20:53:41.614747
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin1 = Plugin('module', 'ping')
    plugin2 = Plugin('module', 'apt')
    setting1 = ConfigSetting('ANSIBLE_CALLBACK_WHITELIST',
                             'debug,skippy',
                             plugin1, {})
    setting2 = ConfigSetting('ANSIBLE_CALLBACK_WHITELIST',
                             'debug,skippy',
                             plugin2, {})
    config_data.update_setting(setting1, plugin1)
    config_data.update_setting(setting2, plugin2)
    config_data.update_setting(setting1, None)
    config_data.update_setting(setting2, None)
    assert config_data.get_setting('ANSIBLE_CALLBACK_WHITELIST', plugin1) == setting1
   

# Generated at 2022-06-12 20:53:50.570513
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    plugin_none = None
    setting = Setting(name='test', value='test_value')
    config_data.update_setting(setting, plugin_none)
    assert config_data._global_settings['test'].value == 'test_value'

    plugin_none = Plugin(type='parser', name='parser_name')
    setting = Setting(name='test', value='test_value')
    config_data.update_setting(setting, plugin_none)
    assert config_data._plugins['parser']['parser_name']['test'].value == 'test_value'

    plugin_none = Plugin(type='new_type', name='new_name')
    setting = Setting(name='test', value='test_value')
    config_data.update_setting(setting, plugin_none)

# Generated at 2022-06-12 20:53:56.075280
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    plugin = Plugin('callback')
    plugin.name = 'first_plugin'
    plugin.enabled = True
    plugin.path = 'the/path/to/the/first/plugin'

    data.update_setting(Setting('a'), plugin)
    data.update_setting(Setting('b'), plugin)
    data.update_setting(Setting('c'))

    assert len(data.get_settings()) == 3
    assert len(data.get_settings(plugin)) == 2

# Generated at 2022-06-12 20:54:03.925261
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0
    setting = Setting("bar", "baz")
    config_data.update_setting(setting)
    assert len(config_data.get_settings()) == 1
    config_data.update_setting(setting, plugin='foo')
    assert len(config_data.get_settings()) == 1



# Generated at 2022-06-12 20:54:07.714067
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # given
    config_data = ConfigData()
    setting = 'blah blah blah'
    plugin = 'ansible.builtin.ping'
    # when
    config_data.update_setting(setting, plugin)
    # then
    assert (setting, plugin) in config_data

# Generated at 2022-06-12 20:54:13.514814
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert len(config_data._global_settings) == 0
    assert len(config_data._plugins) == 0

    setting = ConfigSetting('test', 'Type', 'test_value')
    config_data.update_setting(setting)
    assert len(config_data._global_settings) == 1
    assert len(config_data._plugins) == 0
    assert config_data._global_settings['test'].value == 'test_value'

    setting = ConfigSetting('test', 'Type', 'test_value')
    plugin = ConfigPlugin('Test', 'Type')
    config_data.update_setting(setting, plugin)
    assert len(config_data._global_settings) == 1
    assert len(config_data._plugins) == 1

# Generated at 2022-06-12 20:54:22.601662
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    #test1, plugin is None and there is one global setting with the same name
    setting1 = Setting('setting1', 'value1')
    config_data.update_setting(setting1)
    assert config_data.get_setting('setting1') == setting1

    #test2, plugin is none and there is no global setting with the same name
    assert config_data.get_setting('not_unkown_setting') is None

    #test3, plugin is not none and there is one setting with the same name in the plugin
    setting2 = Setting('setting2', 'value2', 'plugin', 'type')
    config_data.update_setting(setting2)
    assert config_data.get_setting('setting2', Plugin('plugin', 'type')) == setting2

    #test4, plugin is not

# Generated at 2022-06-12 20:54:32.091927
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    global_config_data = ConfigData()

    list_of_settings = {
        'defaults_connection_timeout': 2,
        'defaults_remote_user': 'root',
        'defaults_private_key_file': './id_rsa'
    }

    for name, value in list_of_settings.items():
        global_config_data.update_setting(name, value)

    assert global_config_data.get_setting('defaults_connection_timeout') == 2
    assert global_config_data.get_setting('defaults_remote_user') == 'root'
    assert global_config_data.get_setting('defaults_private_key_file') == './id_rsa'

# Generated at 2022-06-12 20:54:42.149127
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()

    # Test with invalid plugin name
    assert config.get_setting("invalid") == None

    # Test with no plugin name
    setting = { "name": "collection", "value": "mycollection" }
    assert config.get_setting("collection") == None
    config.update_setting(setting)
    assert config.get_setting("collection") == setting

    # Test with plugin name
    setting = { "name": "timeout", "value": "12345" }
    assert config.get_setting("timeout", "myplugin") == None
    config.update_setting(setting, "myplugin")
    assert config.get_setting("timeout", "myplugin") == setting


# Generated at 2022-06-12 20:54:46.192132
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('test') is None


# Generated at 2022-06-12 20:54:47.102753
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert(config_data.get_settings() == [])


# Generated at 2022-06-12 20:54:55.074526
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from ansible.plugins.loader import PluginLoader
    from ansible.utils.plugin_docs import get_docstring

    plugin_loader = PluginLoader()

    for plugin in plugin_loader.all():
        p = plugin_loader.get(plugin.name, plugin.package)

        doc = get_docstring(p)
        if doc is None:
            continue
        for config_spec in doc.get('config_options', []):

            config_setting = config_spec.copy()
            config_setting['name'] = config_spec['key']
            config_setting['plugin'] = plugin

            if config_setting.get('section'):
                config_setting.pop('section')

            config_data.update_setting(config_setting)


# Generated at 2022-06-12 20:55:00.781076
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    plugin = PluginDefinition("Lookup", "cisco_ios", "lookup_plugin")
    setting = SettingDefinition("foo", "True")
    setting_global = SettingDefinition("foo2", "True")
    configData.update_setting(setting)
    configData.update_setting(setting_global, plugin=None)
    configData.update_setting(setting, plugin=plugin)
    assert configData._global_settings["foo2"] == setting_global
    assert configData._plugins["Lookup"]["cisco_ios"]["foo"] == setting
    assert configData._global_settings["foo"] == setting


# Generated at 2022-06-12 20:55:05.409885
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    test_config_data = ConfigData()
    setting = test_config_data.get_setting("default", None)

    assert setting == None


# Generated at 2022-06-12 20:55:13.474313
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_setting('my_setting') is None
    assert config_data.get_setting('my_setting', 'my_plugin') is None

    # Test on global settings
    plugin_type = None
    plugin_name = None
    setting_name = 'my_setting'
    setting = {}
    setting['name'] = setting_name
    config_data.update_setting(setting)
    assert config_data.get_setting('my_setting') == setting
    assert config_data.get_settings() == [setting]
    assert config_data.get_setting('my_setting', 'my_plugin') is None
    assert config_data.get_settings('my_plugin') == []



# Generated at 2022-06-12 20:55:16.705504
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()
    data.update_setting(None)

    assert data.get_setting(None) == None
    assert data.get_setting("test", None) == None


# Generated at 2022-06-12 20:55:23.333453
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting(name = 'config_file', value = '/home/ansible/ansible.cfg')
    plugin = Plugin(type = 'configuration', name = 'config')
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting(name = 'config_file') == setting
    assert config_data.get_setting(name = 'config_file', plugin = plugin) == setting


# Generated at 2022-06-12 20:55:35.166702
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    import ansible_collections.ansible.community.plugins.module_utils.network.cloudengine.ce.config_data as config_data
    from ansible_collections.ansible.community.plugins.module_utils.network.cloudengine.ce.plugin_loader import PluginLoader
    from ansible_collections.ansible.community.plugins.module_utils.network.cloudengine.ce.plugin import Plugin

    class TestConfigData(unittest.TestCase):

        def test_update_setting(self):
            config_data_obj = config_data.ConfigData()
            config_data_obj.update_setting(setting=PluginLoader.get_setting("ce_vrrp_global_version"))
            setting = config_data_

# Generated at 2022-06-12 20:55:45.177749
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting(name="setting1", plugin=Plugin(name="plugin1", type="type1")))
    config_data.update_setting(Setting(name="setting2", plugin=Plugin(name="plugin2", type="type1")))
    config_data.update_setting(Setting(name="setting3", plugin=Plugin(name="plugin3", type="type1")))
    config_data.update_setting(Setting(name="setting4", plugin=Plugin(name="plugin4", type="type1")))
    config_data.update_setting(Setting(name="setting5", plugin=Plugin(name="plugin5", type="type1")))

# Generated at 2022-06-12 20:55:49.338392
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()
    config.update_setting('instance name')
    result = config.get_setting('instance name')
    assert result == 'instance name'




# Generated at 2022-06-12 20:55:51.357279
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    configdata.update_setting(setting)
    assert setting in configdata.get_settings()
    assert len(configdata.get_settings()) == 1


# Generated at 2022-06-12 20:55:53.135469
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert cd.get_setting('a') is None
    cd.update_setting(Setting('a', True))
    assert cd.get_setting('a').get_value() is True

# Generated at 2022-06-12 20:55:54.545525
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    assert config_data.get_settings() == []



# Generated at 2022-06-12 20:55:57.050678
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('', None) is None



# Generated at 2022-06-12 20:56:05.299376
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting("foo", "Foo", "FOO"))
    config_data.update_setting(Setting("bar", "Bar", "BAR", plugin=Plugin("test", "new", "test-plugin")))

    print("setting for foo: " + str(config_data.get_setting("foo")))
    test_plugin = Plugin("test", "new", "test-plugin")
    print("setting for bar (test-plugin): " + str(config_data.get_setting("bar", plugin=test_plugin)))

test_ConfigData_get_setting()


# Generated at 2022-06-12 20:56:11.340071
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    config_data.update_setting('value1')
    config_data.update_setting('value2')
    config_data.update_setting('value3')
    config_data.update_setting('value4')
    config_data.update_setting('value5')
    assert len(config_data.get_settings()) == 5
    assert len(config_data.get_settings()) == 5


# Generated at 2022-06-12 20:56:15.425007
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []

#This file was created to test the functionality of class ConfigData,
#you can run this file to  check the functionality of this class.

# Generated at 2022-06-12 20:56:23.273422
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()

    # Testing with global setting
    data.update_setting(Setting('display_skipped_hosts', 'boolean', 'on'))

    assert data._global_settings['display_skipped_hosts'].value == 'on'

    # Testing with plugin setting
    data.update_setting(Setting('display_skipped_hosts', 'boolean', 'on'), Plugin('callback', 'json', [], []))

    assert data._plugins['callback']['json']['display_skipped_hosts'].value == 'on'



# Generated at 2022-06-12 20:56:31.073399
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config_update_setting = dict(
        name='ansible_automatic_inventory',
        setting_type='bool',
        value=True,
        specified_at='/Users/username/.ansible.cfg',
        default_value=True,
        default_specified_at='/Users/username/.ansible.cfg'
    )
    config.update_setting(setting=config_update_setting)
    assert config.get_setting('ansible_automatic_inventory') == True
    print('Passed test_ConfigData_update_setting')


# Generated at 2022-06-12 20:56:46.385926
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    config.update_setting(ConfigSetting('ConfigSetting1', 'ConfigValue1'))
    config.update_setting(ConfigSetting('ConfigSetting2', 'ConfigValue2'))
    config.update_setting(ConfigSetting('ConfigSetting3', 'ConfigValue3'), PluginDescriptor('Core', 'ActionModule', None))
    config.update_setting(ConfigSetting('ConfigSetting4', 'ConfigValue4'), PluginDescriptor('Core', 'ActionModule', None))

    assert len(config.get_settings()) == 2
    assert config.get_settings()[0].name == 'ConfigSetting1'
    assert config.get_settings()[0].value == 'ConfigValue1'
    assert config.get_settings()[1].name == 'ConfigSetting2'

# Generated at 2022-06-12 20:56:48.727562
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert settings == []


# Generated at 2022-06-12 20:56:50.281260
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(configparser.ConfigParser(), plugin = None)
    assert True

# Generated at 2022-06-12 20:56:52.956970
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Create test data
    data = ConfigData()

    # Get settings for non-existent system
    settings = data.get_settings()

    # Assert
    assert not settings


# Generated at 2022-06-12 20:56:55.830599
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    # here we test when we pass plugin and name to get_setting()
    setting = config.get_setting('foo')
    assert setting == None

    setting = config.get_setting('foo', 'bar')
    assert setting == None



# Generated at 2022-06-12 20:56:58.011197
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    plugin = (None, 'plugin', 'pluginType')
    setting_plugin = ('test_setting', 'test_value')
    assert configData.update_setting(setting_plugin, plugin)


# Generated at 2022-06-12 20:57:00.632526
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting(Setting('aaa', 'bbb'))
    assert cd.get_setting('aaa')
    assert cd.get_settings()
    #assert cd.get_settings()[0].name == 'aaa'
    #assert cd.get_settings()[0].value == 'bbb'



# Generated at 2022-06-12 20:57:10.204592
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.cli.config.setting import Setting

    config_data = ConfigData()

    setting = Setting()
    setting.name = 'test_global'
    setting.value = 'global'

    config_data.update_setting(setting)

    assert config_data.get_setting(setting.name) == setting

    from ansible.plugins.action import ActionBase

    plugin = ActionBase()
    plugin.name = 'test_plugin'
    plugin.type = 'action'

    setting = Setting()
    setting.name = 'test_plugin'
    setting.value = 'plugin'

    config_data.update_setting(setting, plugin=plugin)

    assert config_data.get_setting(setting.name, plugin=plugin) == setting


# Generated at 2022-06-12 20:57:21.866570
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting1 = Setting(False, 'test_key1', 'test_value1', 'test_section1')
    plugin1 = Plugin('test_type1', 'test_name1')

    cd.update_setting(setting1)
    assert cd.get_setting('test_key1') is not None
    assert cd.get_setting('test_key1').get_value() == 'test_value1'

    cd.update_setting(setting1, plugin1)
    assert cd.get_setting('test_key1') is not None
    assert cd.get_setting('test_key1').get_value() == 'test_value1'
    assert cd.get_setting('test_key1', plugin1) is not None
    assert cd.get_setting('test_key1', plugin1).get_

# Generated at 2022-06-12 20:57:25.328662
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    data.update_setting(Setting('test_setting', 'test_value', 'test_description', 'test_plugin'))
    assert 'test_setting' in data._global_settings


# Generated at 2022-06-12 20:57:38.357834
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """Tests for method get_settings of class ConfigData"""
    # Initializes variables for test
    test_config_data = ConfigData()
    import ansible.plugins.loader as plugin_loader
    test_plugin_loader = plugin_loader.PluginLoader()
    test_plugin = test_plugin_loader.get(class_name='LookupModule', name='ansible.plugins.lookup.password', package='ansible.plugins.lookup')
    import ansible.plugins.loader as plugin_loader
    test_plugin_loader = plugin_loader.PluginLoader()
    test_setting = ConfigDataSetting(name='lookup_password_min_length')
    # Runs method get_settings of class ConfigData with argument None
    test_config_data.update_setting(test_setting)

# Generated at 2022-06-12 20:57:48.687585
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.module_utils.common.collections import ImmutableDict

    config_data = ConfigData()

    plugin = ImmutableDict(type='test_type', name='test_name', package='test_package')

    assert config_data.get_settings() == []

    config_data.update_setting(ImmutableDict(name='test_setting_0', value=0), plugin=plugin)
    config_data.update_setting(ImmutableDict(name='test_setting_1', value=1), plugin=plugin)

    settings = []
    for i in range(2):
        settings.append(ImmutableDict(name='test_setting_' + str(i), value=i, plugin=plugin))

    assert config_data.get_settings() == []

# Generated at 2022-06-12 20:57:56.188276
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # create an instance of ConfigData
    configData = ConfigData()

    # This is a test from ansible/test/units/test_config_data.py
    setting = ConfigSetting(name='vault_password_file',
                            desc='when supplied, the vault password will come from this file on disk.',
                            default='~/.vault_pass.txt',
                            type=str)

    configData.update_setting(setting)

    assert configData.get_setting('vault_password_file') == setting

    return configData


# Generated at 2022-06-12 20:58:06.333022
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    PluginClass = namedtuple('PluginClass', 'type name')

    base_data = ConfigData()


# Generated at 2022-06-12 20:58:11.151922
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert data.get_settings() == []
    data._global_settings = {'a': 'b'}
    assert data.get_settings() == [{'a': 'b'}]
    assert data.get_settings(plugin=None) == [{'a': 'b'}]

    data._plugins = {
        'type1': {
            'name1': {'a': 'b'}
        },
        'type2': {
            'name1': {'c': 'd'},
            'name2': {'e': 'f'},
        }
    }
    assert data.get_settings(plugin=None) == [{'a': 'b'}]

# Generated at 2022-06-12 20:58:14.468330
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    print("test_ConfigData_update_setting")

    config_data = ConfigData()

    setting = Setting('example_setting1')
    setting.value = 'foo'
    config_data.update_setting(setting)
    print(config_data.get_settings())


# Generated at 2022-06-12 20:58:19.151487
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    assert cd._global_settings == {}
    assert cd._plugins == {}

    class P:
        pass
    p = P()
    p.type = 'filter'
    p.name = 'my_filter'
    class S:
        pass
    s = S()
    s.name = 'foo'
    cd.update_setting(s, p)

    assert cd._plugins['filter']['my_filter']['foo'] == s

# Generated at 2022-06-12 20:58:22.723057
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = None
    settings = config_data.get_settings(plugin)
    assert isinstance(settings,list), "Settings is list"


# Generated at 2022-06-12 20:58:33.527542
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()
    config.update_setting(
        Setting(
            'foo',
            'global',
            'boolean',
            True,
            'Does a foo'
        )
    )
    setting = config.get_setting('foo')
    assert setting.name == 'foo'
    assert setting.type == 'boolean'
    assert setting.value is True

    config.update_setting(
        Setting(
            'bar',
            'defaults',
            'string',
            'bar_value',
            'Does a bar'
        ),
        Plugin(
            'bar_plugin',
            'modules'
        )
    )
    setting = config.get_setting('bar', Plugin('bar_plugin', 'modules'))
    assert setting.name == 'bar'

# Generated at 2022-06-12 20:58:42.545659
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible_collections.ansible.netcommon.plugins.modules import net_config

    config_data = ConfigData()

    # Setting
    setting = net_config.Setting('hostname')
    setting.value = 'router-test'

    # Global plugin
    plugin_global = net_config.BaseNetworkConfig()
    plugin_global.name = 'insights'

    # Leaf plugin
    plugin_leaf = net_config.BaseNetworkConfig()
    plugin_leaf.type = 'leaf'
    plugin_leaf.name = 'eos'

    # Spine plugin
    plugin_spine = net_config.BaseNetworkConfig()
    plugin_spine.type = 'spine'
    plugin_spine.name = 'iosxr'

    # Host1 plugin
    plugin_host1 = net_config.BaseNetwork

# Generated at 2022-06-12 20:58:59.487725
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Test for global settings
    cd = ConfigData()
    cd._global_settings = {
        'setting1' : 'value1',
        'setting2' : 'value2',
        'setting3' : 'value3'
    }
    settings = cd.get_settings()
    assert len(settings) == 3
    assert settings[0].name == 'setting1'
    assert settings[1].name == 'setting2'
    assert settings[2].name == 'setting3'

    # Test for plugin settings
    cd = ConfigData()
    cd._global_settings = {}

# Generated at 2022-06-12 20:59:01.854828
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    result = config_data.get_setting("gtest")
    assert result is None


# Generated at 2022-06-12 20:59:04.427812
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    conf = ConfigData()
    settings = conf.get_settings()
    assert len(settings) == 0


# Generated at 2022-06-12 20:59:06.013663
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass


# Generated at 2022-06-12 20:59:07.005024
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    pass


# Generated at 2022-06-12 20:59:12.683137
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    config_data.update_setting(Setting("test_setting", "test_val"))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == "test_setting"

    config_data.update_setting(Setting("test_setting2", "test_val2"), Plugin(PluginType.ACTION_PLUGIN, "action_one"))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == "test_setting"

    settings = config_data.get_settings(Plugin(PluginType.ACTION_PLUGIN, "action_one"))
    assert len(settings) == 1
    assert settings[0].name == "test_setting2"



# Generated at 2022-06-12 20:59:14.408034
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    assert data._global_settings == {}
    assert data._plugins == {}


# Generated at 2022-06-12 20:59:22.449800
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData();
    assert(len(data.get_settings() == 0))
    data.update_setting(Setting('foo', 'bar'))
    assert(len(data.get_settings()) == 1)
    data.update_setting(Setting('foo', 'baz'))
    assert(len(data.get_settings()) == 1)
    assert(data.get_setting('foo') == Setting('foo', 'baz'))
    data.update_setting(Setting('bar', 'baz'))
    assert(len(data.get_settings()) == 2)


# Generated at 2022-06-12 20:59:31.934719
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.doc_fragments.config import Configurable

    class ConfigSetting(Configurable):
        def __init__(self, name, value):
            super(ConfigSetting, self).__init__()
            self.name = name
            self.value = value

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value == other.value
            else:
                return False

    class TestModule(object):
        def __init__(self, **kwargs):
            for kwarg in kwargs:
                setattr(self, kwarg, kwargs[kwarg])



# Generated at 2022-06-12 20:59:39.395857
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    config.update_setting(Setting('ANSIBLE_LOG_PATH'))
    config.update_setting(Setting('ANSIBLE_NOCOWS', 'Bool', 'False'))
    config.update_setting(Setting('ANSIBLE_STDOUT_CALLBACK'))

    settings = config.get_settings()

    print('\n[%d] settings found in config' % len(settings))
    for setting in settings:
        print('- setting %s type %s value %s' % (setting.name, setting.type, setting.value))
    assert len(settings) == 3
    assert settings[0].name == 'ANSIBLE_LOG_PATH'
    assert settings[1].name == 'ANSIBLE_NOCOWS'
    assert settings[2].name == 'ANSIBLE_STDOUT_CALLBACK'

# Generated at 2022-06-12 20:59:52.347768
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()
    assert config.get_setting("foo") is None
    assert config.get_setting("foo", "ansible.foo") is None
    assert config.get_setting("foo", "foo.bar") is None

    setting = Setting("foo", "bar")
    config.update_setting(setting)
    assert config.get_setting("foo") == setting
    assert config.get_setting("foo", "ansible.foo") is None
    assert config.get_setting("foo", "foo.bar") is None

    setting = Setting("foo", "baz", "ansible.foo")
    config.update_setting(setting)
    assert config.get_setting("foo") == setting
    assert config.get_setting("foo", "ansible.foo") == setting

# Generated at 2022-06-12 21:00:02.753285
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    cd = ConfigData()

    assert cd.get_setting('setting_global') is None
    assert cd.get_setting('setting_plugin_type', plugin=PluginStub('plugin_type')) is None

    cd.update_setting(SettingStub('setting_global_1'))
    cd.update_setting(SettingStub('setting_global_2'))
    cd.update_setting(SettingStub('setting_plugin_type_1'), plugin=PluginStub('plugin_type'))
    cd.update_setting(SettingStub('setting_plugin_type_2'), plugin=PluginStub('plugin_type'))
    cd.update_setting(SettingStub('setting_plugin_type_3'), plugin=PluginStub('plugin_type'))

# Generated at 2022-06-12 21:00:06.711602
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configuration=ConfigData()
    setting=dict()
    setting['name']='value'
    setting['plugin']='value'
    configuration.update_setting(setting)
    assert configuration


# Generated at 2022-06-12 21:00:15.870927
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import config_loader
    from ansible.module_utils._text import to_native

    data = ConfigData()
    data.update_setting(config_loader.setting_loader._load_setting('display_skipped_hosts'))
    data.update_setting(config_loader.setting_loader._load_setting('timeout'))
    data.update_setting(config_loader.setting_loader._load_setting('remote_user'), config_loader.Plugin('connection', 'ssh'))
    data.update_setting(config_loader.setting_loader._load_setting('become'), config_loader.Plugin('become', 'sudo'))
    data.update_setting(config_loader.setting_loader._load_setting('become_user'), config_loader.Plugin('become', 'sudo'))
    data

# Generated at 2022-06-12 21:00:23.555383
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting("a", "b", "c", "d"))
    assert config_data.get_setting("a").name == "a"
    assert config_data.get_setting("a").value == "b"
    assert config_data.get_setting("a").plugin_type is None
    assert config_data.get_setting("a").plugin_name is None
    assert config_data.get_setting("z") is None


# Generated at 2022-06-12 21:00:33.632409
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import plugin_loader

    config_data = ConfigData()

    # init plugin settings
    for plugin in plugin_loader.all():
        for key, value in plugin.get_option_class().get_defaults().items():
            setting = Setting(key, None, plugin, value)
            config_data.update_setting(setting, plugin)

    # verify that Integer setting is defined for the shell plugin
    plugin = plugin_loader.get('shell')
    setting = config_data.get_setting('executable', plugin)
    assert setting.name == 'executable'
    assert setting.type == 'path'
    assert setting.default == '/bin/sh'

    # verify that Integer setting is defined for the shell plugin
    setting = config_data.get_setting('not_existing_setting', plugin)

# Generated at 2022-06-12 21:00:39.332545
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    config_data.update_setting(ConfigSetting("debug", "True"))
    config_data.update_setting(ConfigSetting("timeout", "10"))
    assert config_data.get_setting("debug") is not None
    assert config_data.get_setting("timeout") is not None


# Generated at 2022-06-12 21:00:39.899617
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass

# Generated at 2022-06-12 21:00:42.053264
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    PluginSetting = config_data.PluginSetting
    assert config_data.get_settings(PluginSetting) == []


# Generated at 2022-06-12 21:00:44.954028
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cfg_data = ConfigData()
    # With plugin
    assert cfg_data.get_setting(name="setting0", plugin=PluginStub("type1", "name1")) is None

    # Without plugin
    assert cfg_data.get_setting(name="setting0") is None


# Generated at 2022-06-12 21:01:02.880845
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    cd = ConfigData()
    sgt = cd.get_setting(name='stdout_callback')
    assert sgt is None
    sgt = cd.get_setting(name='stdout_callback', plugin=None)
    assert sgt is None
    sgt = cd.get_setting(name='stdout_callback', plugin=Plugin(type='callback', name=None))
    assert sgt is None
    sgt = cd.get_setting(name='stdout_callback', plugin=Plugin(type='callback', name='default'))
    assert sgt is None


# Generated at 2022-06-12 21:01:10.173085
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    test_object = ConfigData()

    assert test_object.get_settings() == []

    test_object._global_settings['foo'] = 'bar'
    assert test_object.get_settings() == ['bar']
    assert test_object.get_settings()[0].name == 'foo'

    test_object._global_settings['bar'] = 'foo'
    assert test_object.get_settings() == ['bar', 'foo']
    assert test_object.get_settings()[0].name == 'foo'
    assert test_object.get_settings()[1].name == 'bar'

# Generated at 2022-06-12 21:01:15.323034
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    module_setting = "user"
    command_setting = "command"
    plugin = Plugin()
    plugin.name = 'ansible'
    plugin.type = PluginType.Module
    setting = Setting()
    setting.name = module_setting
    config_data.update_setting(setting)
    setting.name = command_setting
    config_data.update_setting(setting, plugin)
    settings = config_data.get_settings()
    for setting in settings:
        assert setting.name == module_setting
    settings = config_data.get_settings(plugin)
    for setting in settings:
        assert setting.name == command_setting


# Generated at 2022-06-12 21:01:24.330418
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.config.setting import Setting

    config_data = ConfigData()

    config_data.update_setting(Setting('foo', 'first value'))
    config_data.update_setting(Setting('bar', 'second value'))

    assert len(config_data.get_settings()) == 2
    assert config_data.get_settings()[0].name == 'foo'
    assert config_data.get_settings()[1].name == 'bar'

    assert len(config_data.get_settings(None)) == 2
    assert config_data.get_settings(None)[0].name == 'foo'
    assert config_data.get_settings(None)[1].name == 'bar'

# Generated at 2022-06-12 21:01:35.084948
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from units.mock.loader import DictDataLoader
    from units.plugins.vars import PluginVars
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.cache import CacheModule
    from ansible.template import Templar


    config_data = ConfigData()

    config_data._global_settings.clear()
    config_data._plugins.clear()

    setting = {'key': 'value'}
    data_loader = DictDataLoader({'my_plugin': setting})

    global_settings_src = '\n'.join(["key = value", ])

    cache_dir = ''
    cache_module = CacheModule(cache_dir)

    templar = Templar(loader=data_loader)


# Generated at 2022-06-12 21:01:37.751329
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    # Test default return value
    assert config_data.get_settings() == []


# Generated at 2022-06-12 21:01:44.807900
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    class Plugin:
        def __init__(self, plugin_type, plugin_name):
            self.type = plugin_type
            self.name = plugin_name

    setting_1 = Plugin('1', '1')
    setting_2 = Plugin('2', '2')
    setting_3 = Plugin('3', '3')
    setting_4 = Plugin('4', '4')
    setting_5 = Plugin('5', '5')

    config_data.update_setting(setting_1)
    assert(config_data.get_settings() == [setting_1])

    config_data.update_setting(setting_2)
    assert(config_data.get_settings() == [setting_1, setting_2])

    config_data.update_setting(setting_3)

# Generated at 2022-06-12 21:01:55.869223
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():


    config_data = ConfigData()
    assert config_data.get_setting('foo') is None

    # Test adding a global setting
    setting = ConfigSetting('foo', 'bar')
    config_data.update_setting(setting)
    assert config_data.get_setting('foo') == setting

    # Test adding a setting to a plugin
    setting2 = ConfigSetting('foo2', 'bar2')
    config_data.update_setting(setting2, Plugin('vars', 'foo'))
    assert config_data.get_setting('foo2', Plugin('vars', 'foo')) == setting2
    assert config_data.get_setting('foo2') is None


# Generated at 2022-06-12 21:02:02.303451
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting_name = 'setting_name'
    setting_value = 'setting_value'
    setting = Setting(setting_name, setting_value)
    config_data.update_setting(setting)

    plugins = config_data.get_settings()

    assert plugins[0].get_name() == setting_name
    assert plugins[0].get_value() == setting_value


# Generated at 2022-06-12 21:02:13.532515
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings().__class__ == list
    assert len(cd.get_settings()) == 0

    import configloader
    from configloader import Plugin, Setting

    def test_update_setting(cd, plugin, setting_name, setting_value):
        setting = Setting(setting_name, setting_value)
        cd.update_setting(setting, plugin)
        return cd.get_setting(setting_name, plugin)

    def test_get_settings(cd, plugin):
        return cd.get_settings(plugin).__class__

    plugin = Plugin('test', 'test_type')
    assert test_update_setting(cd, plugin, "test_setting_1", "test_value").value == "test_value"
    assert test_get_settings(cd, plugin) == list

# Generated at 2022-06-12 21:02:42.535800
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    
    from collections import namedtuple
    Plugin = namedtuple('Plugin', 'name type')
    plugin1 = Plugin('A', 'module')
    plugin2 = Plugin('B', 'module')
    plugin3 = Plugin('C', 'module')
    plugin4 = Plugin('D', 'module')
    plugin5 = Plugin('E', 'module')
    plugin6 = Plugin('F', 'module')
    plugin7 = Plugin('G', 'module')
    plugin8 = Plugin('H', 'module')
    plugin9 = Plugin('I', 'module')

    from collections import namedtuple
    Setting = namedtuple('Setting', 'name value')
    setting1 = Setting('debug', '1')
    setting2 = Setting('device', '/dev/null')

# Generated at 2022-06-12 21:02:51.031628
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    config_data.update_setting(ConfigSetting("enabled", "true"))
    config_data.update_setting(ConfigSetting("root", "false"))
    config_data.update_setting(ConfigSetting("force_handlers", "true"))
    assert config_data.get_setting("enabled").value == "true"
    assert config_data.get_setting("root").value == "false"
    assert config_data.get_setting("force_handlers").value == "true"
    assert config_data.get_setting("bananas") is None


# Generated at 2022-06-12 21:02:59.801578
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()
    assert len(config.get_settings()) == 0
    assert len(config.get_settings('type', 'name')) == 0
    assert config.get_setting('name') is None
    assert config.get_setting('type', 'name') is None

    class Setting(object):
        def __init__(self, name=None, value=None, origin=None, plugin_type=None, plugin_name=None):
            self.name = name
            self.value = value
            self.origin = origin
            self.plugin_type = plugin_type
            self.plugin_name = plugin_name

    setting1 = Setting('name1', 'global')
    setting2 = Setting('name2', 'global')
    setting3 = Setting('name3', 'type', 'name')

# Generated at 2022-06-12 21:03:11.997967
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting(None) == None
    assert config_data.get_setting(None, None) == None
    config_data.update_setting(Setting(name= "my_setting", description="my description", value="my_value", ini=True, env=True, cli=True))
    config_data.update_setting(Setting(name= "my_setting2", description="my description", value="my_value", ini=True, env=True, cli=True))
    config_data.update_setting(Setting(name= "my_setting3", description="my description", value="my_value", ini=True, env=True, cli=True, plugin=Plugin(type="my_type", name="my_name")))
    assert config_data.get

# Generated at 2022-06-12 21:03:21.224336
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansiblelint import AnsibleLintRule
    from ansiblelint.rules import RulesCollection

    rulescollection=RulesCollection()
    configuration = ConfigData()

    # Test for get_setting with no setting registered
    # Expected behavior: None is returned
    ruleid = "TEST01"
    rule = AnsibleLintRule(id=ruleid, shortdesc="Test rule", description="Test rule", tags=["test"])
    configuration.update_setting(rule, rule)
    assert configuration.get_setting(ruleid) == rule
    assert configuration.get_setting(ruleid, plugin=rule) == rule
    assert configuration.get_setting('dummyrule') == None
    assert configuration.get_setting('dummyrule', plugin=rule) == None
    assert configuration.get_setting(ruleid, plugin=ruletwo)

# Generated at 2022-06-12 21:03:29.186775
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()
    assert len(cd.get_settings()) == 0

    # Add a global setting
    cd.update_setting(Setting(name="projects_dir", value=":defaults"))

    # Add a plugin setting
    cd.update_setting(Setting(name="some_key", value="some_value"),
                      plugin=Plugin("some_plugin", "some_type"))

    assert len(cd.get_settings()) == 2
    assert len(cd.get_settings(plugin=Plugin("some_plugin", "some_type"))) == 1
