

# Generated at 2022-06-12 20:53:29.948623
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # ConfigData is instantiated
    config_data = ConfigData()
    # config_data has no plugins loaded
    assert len(config_data.get_settings()) == 0



# Generated at 2022-06-12 20:53:33.024634
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = config_data.update_setting({'name': 'ansible_password', 'plugin':'connection', 'value': 'abc'})
    assert setting['name'] == 'ansible_password'

# Generated at 2022-06-12 20:53:34.628263
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings() == []

# Generated at 2022-06-12 20:53:45.353931
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # create a configData object
    configdata = ConfigData()

    # create a setting object and update configData
    setting1 = Setting(name='setting1')
    configdata.update_setting(setting1)

    # create two plugin objects and two setting objects for those plugins
    plugin1 = Plugin(type='type1', name='name1')
    plugin2 = Plugin(type='type2', name='name2')
    setting2 = Setting(name='setting2')
    setting3 = Setting(name='setting3')

    # update configData with the two setting objects for plugins
    configdata.update_setting(setting2, plugin1)
    configdata.update_setting(setting3, plugin2)

    # test if get_settings returns all the settings in the configData
    assert len(configdata.get_settings()) == 3

    # test

# Generated at 2022-06-12 20:53:51.477392
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()

    # Test global settings
    data._global_settings = {'key': 'value'}
    assert data.get_settings().get('key') == 'value'

    # Test plugin settings
    data._plugins = {'type': {'name': {'key': 'value'}}}
    assert data.get_settings(plugin={'name': 'name', 'type': 'type'}).get('key') == 'value'


# Generated at 2022-06-12 20:54:02.027368
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configdata = ConfigData()
    assert (configdata.get_setting("ANSIBLE_CONFIG") is None)

    from ansible.plugins.loader import config_loader

# Generated at 2022-06-12 20:54:07.142683
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()

    plugin = Plugin(type='facts', name='foo')
    setting = Setting(name='bar', plugin=plugin, value='baz')

    config.update_setting(setting)

    assert len(config.get_settings(plugin)) == 1
    assert config.get_setting(setting.name, plugin) == setting
    assert config.get_settings()[0] == setting


# Generated at 2022-06-12 20:54:12.041352
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    from ansible import constants as C
    from ansible.cli.arguments import AnsibleCLIArguments
    from ansible.plugins.loader import PluginLoader
    from ansible.utils.display import Display
    display = Display()
    cli = AnsibleCLIArguments(usage='')
    
    plugin = PluginLoader.get("callback", cli, "Null", C, display)
    assert 'Null' == plugin.name
    assert 'callback' == plugin.type
    assert plugin == config_data.get_setting("callback", plugin)

# Generated at 2022-06-12 20:54:15.397755
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    plugin = PluginDefinition('action', 'awx')
    setting = PluginSettingDefinition('user_name')
    cd.update_setting(setting, plugin=plugin)


# Generated at 2022-06-12 20:54:23.763670
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import get_docstring

    plugin_loaders = get_all_plugin_loaders()
    display = Display()

    # unit tests
    config_data = ConfigData()

    # no plugin
    setting = config_data.get_setting('bin_ansible_callbacks')
    assert setting is None

    # unknown plugin type
    plugin = 'test1'
    setting = config_data.get_setting(name='bin_ansible_callbacks', plugin=plugin)
    assert setting is None

    # unknown plugin name
    plugin = plugin_loaders['shell'].get_plugin(name='test2', display=display)
    setting = config_data.get_setting

# Generated at 2022-06-12 20:54:34.459971
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from collections import namedtuple
    from ansiblelint.rules import RuleMatch
    from ansiblelint.config import Setting

    plugin = namedtuple('Plugin', ['type', 'name'])
    setting1 = Setting('a_setting', 'a description', [], None, True, False, RuleMatch)
    setting2 = Setting('another_setting', 'a description', [], None, False, True, RuleMatch)
    config = ConfigData()
    config.update_setting(setting1)
    config.update_setting(setting2)

    settings = config.get_settings()
    assert(len(settings) == 2)
    assert(settings[0].name == 'a_setting')
    assert(settings[1].name == 'another_setting')



# Generated at 2022-06-12 20:54:38.981967
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data._global_settings = {'hello': {'value': 'world'}, 'default_value': {'value': 'foo'}}
    assert config_data.get_settings() == [{'value': 'world'}, {'value': 'foo'}]


# Generated at 2022-06-12 20:54:43.686197
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configData = ConfigData()
    plugin = PluginDefinition('connection', 'local')
    configData.update_setting(SettingDefinition('host_key_checking', 'True'), plugin)
    assert(configData.get_setting('host_key_checking', plugin).value == 'True')



# Generated at 2022-06-12 20:54:52.133938
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.config.setting import Setting

    config_data = ConfigData()

    # Test for global setting
    config_data.update_setting(Setting('role_path', '/user/me/ansible/roles'))
    assert config_data.get_setting('role_path').value == '/user/me/ansible/roles'

    # Test for plugin settings
    from ansible.plugins.loader import PluginLoader
    test_plugin_loader = PluginLoader('INVENTORY')
    test_plugin = test_plugin_loader.get('simple_file')
    config_data.update_setting(Setting('hostfile', '/etc/hosts'), plugin=test_plugin)
    assert config_data.get_setting('hostfile', plugin=test_plugin).value == '/etc/hosts'


# Generated at 2022-06-12 20:54:59.913063
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    plugin_type = 'module'
    plugin_name = 'ping'
    setting_name = 'timeout'
    setting_value = '2'
    setting_plugin = Plugin(plugin_name, plugin_type)
    setting = Setting(setting_name, setting_value, plugin=None)
    config_data.update_setting(setting)
    setting = Setting(setting_name, setting_value, plugin=setting_plugin)
    config_data.update_setting(setting)

    with pytest.raises(Exception):
        config_data.get_settings('no plugin')

    settings = config_data.get_settings()
    assert settings[0].plugin is None
    assert settings[0].name == setting_name
    assert settings[0].value == setting_value

    settings = config_data

# Generated at 2022-06-12 20:55:08.020338
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    import MockPlugin as mock_plugin

    plugin = mock_plugin.Plugin("TestPlugin")
    setting = mock_plugin.Setting("test", "TestSetting", mock_plugin.TYPE_STRING, "test value", None, plugin)

    data = ConfigData()
    data.update_setting(setting, plugin)

    assert data.get_setting(setting.name) is None
    assert data.get_setting(setting.name, plugin) is setting


# Generated at 2022-06-12 20:55:15.752307
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    setting1 = Setting(name='setting_name_1', type='Boolean', value=True)
    setting2 = Setting(name='setting_name_2', type='String', value='string_2')
    setting3 = Setting(name='setting_name_3', type='Integer', value=3)
    setting4 = Setting(name='setting_name_4', type='Boolean', value=False)
    setting5 = Setting(name='setting_name_5', type='String', value='string_5')
    setting6 = Setting(name='setting_name_6', type='Integer', value=6)

    plugin1 = Plugin(type='Connection', name='connection_1')
    plugin2 = Plugin(type='Module', name='module_2')

# Generated at 2022-06-12 20:55:22.033606
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()

    # first test with global settings
    setting = cd.get_setting('name')
    assert setting is None

    # now test with real settings
    from ansibledocgen.data.setting import Setting
    cd.update_setting(Setting('name', 'value'))

    setting = cd.get_setting('name')
    assert setting.name == 'name'
    assert setting.value == 'value'


# Generated at 2022-06-12 20:55:33.941501
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configdata = ConfigData()

    # TEST1: get setting
    setting = configdata.get_setting('my_setting')
    assert setting == None

    # TEST2: set setting
    setting = Setting('my_setting', 'my_value')
    configdata.update_setting(setting)
    setting = configdata.get_setting('my_setting')
    assert setting != None
    assert setting.name == 'my_setting'
    assert setting.value == 'my_value'

    # TEST3: set setting for plugin
    plugin = Plugin(Plugin.CORE, 'module_util')
    setting = Setting('my_setting', 'my_value2')
    configdata.update_setting(setting, plugin)
    setting = configdata.get_setting('my_setting', plugin)
    assert setting != None
    assert setting.name

# Generated at 2022-06-12 20:55:44.525720
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint.rules.Credentials import CredentialsRule
    from ansiblelint.runner import Runner

    host_settings = {'host_key_checking': 'yes'}
    settings = ConfigData()
    settings.update_setting(Setting('host_key_checking', 'yes', host_settings))
    settings.update_setting(Setting('host_key_checking', 'no', host_settings), plugin=Runner(['playbook']))

    assert len(settings.get_settings()) == 1
    assert settings.get_settings('/tmp/playbook')[0].value == 'no'
    assert settings.get_settings('/tmp/tasks.yaml')[0].value == 'yes'
    assert len(settings.get_settings('/tmp/playbook', plugin=CredentialsRule)) == 0

#

# Generated at 2022-06-12 20:55:55.127500
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    plugin1 = Base(type='type1', name='name1')
    plugin2 = Base(type='type1', name='name2')
    plugin3 = Base(type='type2', name='name1')
    plugin4 = Base(type='type2', name='name2')
    setting1 = Setting(name='setting1', value='value1')
    setting2 = Setting(name='setting2', value='value2')
    setting3 = Setting(name='setting3', value='value3')
    setting4 = Setting(name='setting4', value='value4')
    setting5 = Setting(name='setting5', value='value5')
    setting6 = Setting(name='setting6', value='value6')
    configData.update_setting(setting1)

# Generated at 2022-06-12 20:56:05.806423
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    configdata = ConfigData()

    import ansible.plugins.loader
    # all
    settings = configdata.get_settings()
    assert settings == [] 
    # by plugin
    test_plugin = ansible.plugins.loader.plugin_loader.get('lookup', 'ph')
    settings = configdata.get_settings(test_plugin)
    assert settings == []

    # all
    from ansible.config.manager import Setting
    test_set = Setting('foo', 1)
    configdata.update_setting(test_set)
    settings = configdata.get_settings()
    assert settings[0].name == 'foo' and settings[0].value == 1
    settings = configdata.get_settings(test_plugin)
    assert settings == []
    # by plugin
    test_set = Setting('foo', 1)


# Generated at 2022-06-12 20:56:16.948224
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    
    config_data = ConfigData()

    config_data = ConfigData()
    config_data._global_settings = {
        "foo1": 'bar1',
        "foo2": 'bar2'
    }
    config_data._plugins = {
        "action": {
            "foobar": {
                "foo3": 'bar3',
                "foo4": 'bar4'
            }
        }
    }

    assert config_data.get_settings() == ['bar1', 'bar2']
    assert config_data.get_settings('action', 'foobar') == ['bar3', 'bar4']
    assert config_data.get_settings('invalid', 'foobar') == []



# Generated at 2022-06-12 20:56:18.266672
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    assert ConfigData.get_settings == ConfigData.get_settings

# Generated at 2022-06-12 20:56:28.028560
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = GlobalSetting("1", "", "", "", "", "")
    config_data.update_setting(setting)
    assert config_data.get_setting("1") == setting

    plugin_path = "a/b/c"
    plugin_name = "some_name"
    plugin_type = PluginType.CACHE
    plugin = Plugin(plugin_name, plugin_path, plugin_type)
    setting = PluginSetting("2", "", plugin, "", "", "")
    config_data.update_setting(setting)
    assert config_data.get_setting("2", plugin) == setting

# Generated at 2022-06-12 20:56:32.377001
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible.plugins.test.test_data import TestGlobalSettings, TestPluginSettings
    c = ConfigData()
    setting = TestGlobalSettings()
    c.update_setting(setting)
    setting = TestPluginSettings()
    c.update_setting(setting, setting.plugin)
    assert c.get_settings(setting.plugin) == [setting]
    assert c.get_settings() == []

# Generated at 2022-06-12 20:56:43.082005
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    setting = Setting('fruit', 'apple')
    config_data.update_setting(setting)
    assert config_data.get_setting('fruit') == setting

    setting = Setting('color', 'red')
    config_data.update_setting(setting)
    assert config_data.get_setting('color') == setting

    plugin = Plugin(PluginType.MODULE, 'debug')
    setting = Setting('verbosity', 'high', plugin)
    config_data.update_setting(setting)
    assert config_data.get_setting('verbosity', plugin) == setting

    assert config_data.get_setting('verbosity') is None
    assert config_data.get_setting('color') == setting

    assert config_data.get_setting('verbose', plugin) is None

# Generated at 2022-06-12 20:56:53.534759
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    class FakePlugin():
        def __init__(self, name, type):
            self.name = name
            self.type = type

    global_setting = {'name': 'global_setting', 'description': 'Global setting', 'type': 'bool', 'value': 'True'}
    plugin1_setting = {'name': 'plugin1_setting', 'description': 'Plugin 1 setting', 'type': 'bool', 'value': 'True'}
    plugin2_setting = {'name': 'plugin2_setting', 'description': 'Plugin 2 setting', 'type': 'bool', 'value': 'True'}

    plugin1 = FakePlugin('plugin1', 'inventory')
    plugin2 = FakePlugin('plugin2', 'inventory')

    config = ConfigData()
    config.update_setting(global_setting)

# Generated at 2022-06-12 20:56:57.833421
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting(Setting('foo', 'bar', False, False, False, False, 'string', 'Comment for foo', 'section'), Plugin('fizz', 'buzz'))
    cd.update_setting(Setting('bar', 'baz', False, False, False, False, 'string', 'Comment for bar', 'section'))
    assert cd.get_setting('foo', Plugin('fizz', 'buzz')).value == 'bar'
    assert cd.get_setting('bar').value == 'baz'


# Generated at 2022-06-12 20:57:05.174443
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansiblelint.rules.LineTooLongRule import LineTooLongRule
    from ansiblelint.setting import Setting

    config_data = ConfigData()
    plugin = LineTooLongRule(None)
    setting = Setting("max_line_length", "80")
    config_data.update_setting(setting, plugin)

    assert config_data.get_setting("max_line_length") is None
    assert config_data.get_setting("max_line_length", plugin) is not None
    assert config_data.get_setting("max_line_length", plugin).name == "max_line_length"


# Generated at 2022-06-12 20:57:16.490920
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_setting = Setting(name='key1', value_type='int', default=10)
    cd = ConfigData()
    cd.update_setting(global_setting)
    assert(cd.get_setting(global_setting.name) == global_setting)
    assert(cd.get_setting('key2') == None)

    plugin_setting_1 = Setting(name='key1', value_type='int', default=10)
    plugin_setting_2 = Setting(name='key2', value_type='int', default=10)
    plugin_1 = Plugin(name='plugin_1', type='action')
    plugin_2 = Plugin(name='plugin_2', type='action')
    cd.update_setting(plugin_setting_1, plugin=plugin_1)

# Generated at 2022-06-12 20:57:25.328726
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = ConfigSetting('n', 'v')
    config_data.update_setting(setting)
    if config_data._global_settings['n'] != setting:
        raise Exception("ConfigData did not save global setting")

    setting = ConfigSetting('n', 'v')
    plugin = Plugin('p', 't')
    config_data.update_setting(setting, plugin)
    if config_data._plugins['t']['p']['n'] != setting:
        raise Exception("ConfigData did not save plugin setting")


# Generated at 2022-06-12 20:57:35.412126
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config = ConfigData()

    # Test with 'plugin' = None
    assert config.get_settings() == []

    # Test with 'plugin' containing a non-existent plugin name
    plugin = PluginDefinition('myplugin')
    assert config.get_settings(plugin) == []

    # Test with 'plugin' containing a name that matches with a plugin definition
    # that does not have defaults
    plugin.set_name('myplugin')
    plugin.set_type('type')
    plugin.add_setting('setting1', 'default1')
    plugin.add_setting('setting2', 'default2')
    config.update_setting(plugin.get_setting('setting1'))
    config.update_setting(plugin.get_setting('setting2'))

# Generated at 2022-06-12 20:57:40.704645
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    # test get_settings without plugin
    assert len(config_data.get_settings()) == 0

    # test get_settings with plugin with no settings
    fake_plugin = Plugin('fake_plugin')
    assert len(config_data.get_settings(fake_plugin)) == 0

    # test get_settings with plugin with settings
    fake_plugin = Plugin('fake_plugin')
    fake_config = Setting('fake_config', fake_plugin)

    config_data.update_setting(fake_config)

    assert len(config_data.get_settings(fake_plugin)) == 1
    assert fake_config in config_data.get_settings(fake_plugin)


# Generated at 2022-06-12 20:57:44.472125
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    data.update_setting(ConfigLine('a'))
    data.update_setting(ConfigLine('b'))

    assert data.get_setting('a')
    assert data.get_setting('b')


# Generated at 2022-06-12 20:57:49.742959
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting("SOME_SETTING"))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == "SOME_SETTING"
    settings = config_data.get_settings(Plugin("api", "doc"))
    assert len(settings) == 0


# Generated at 2022-06-12 20:57:59.742164
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import iteritems
    from ansible.utils.plugin_docs import DOCUMENTABLE_PLUGIN_TYPES, get_doc_section

    config_data = ConfigData()

    for plugin_type, plugin_data in iteritems(DOCUMENTABLE_PLUGIN_TYPES):
        plugin_type = plugin_type.strip()
        plugin_data = dict([(k.strip(), v.strip()) for k, v in iteritems(plugin_data)])

        if not isinstance(plugin_data, Mapping):
            # Only iterate over dicts, ignore all other iterable types
            continue

        # Test the global settings
        plugin = None

# Generated at 2022-06-12 20:58:07.566374
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = Plugin('', '', '', '')

    assert (len(config_data.get_settings()) == 0)
    assert (len(config_data.get_settings(plugin)) == 0)

    config_data.update_setting(Setting('valid_setting_1', ''), plugin)
    config_data.update_setting(Setting('valid_setting_2', ''))

    assert (len(config_data.get_settings()) == 2)
    assert (len(config_data.get_settings(plugin)) == 1)


# Generated at 2022-06-12 20:58:17.295182
# Unit test for method update_setting of class ConfigData

# Generated at 2022-06-12 20:58:29.212717
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from copy import deepcopy

    from ansible_collections.ansible.community.tests.unit.modules.plugins.loader.test_module_utils.test_read_config import (
        Option,
        Plugin,
    )

    # test plugin 1
    plugin1 = Plugin('cache', 'jsonfile')
    option1 = Option('CACHE_PLUGIN', 'jsonfile')
    option1.origin = 'cache.cfg'
    option2 = Option('CACHE_PLUGIN_CONNECTION', None)
    option2.origin = 'cache.cfg'
    option3 = Option('CACHE_PLUGIN_TIMEOUT', '3600')
    option3.origin = 'cache.cfg'

    # test plugin 2
    plugin2 = Plugin('cache', 'redis')

# Generated at 2022-06-12 20:58:45.174974
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Instanciate
    config = ConfigData()
    result = config.get_settings()
    assert isinstance(result, list) and len(result) == 0

    plugin = PluginDescriptor()
    plugin.name = 'test'
    result = config.get_settings(plugin)
    assert isinstance(result, list) and len(result) == 0

    plugin.type = 'foo'
    result = config.get_settings(plugin)
    assert isinstance(result, list) and len(result) == 0

    # Set a few settings
    setting = SettingDescriptor()
    setting.name = 'foo'
    setting.value = 'bar'
    setting.default = 'bar'
    setting.description = 'foo is used to test'
    setting.category = 'Testing'

# Generated at 2022-06-12 20:58:49.127672
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = config_data.get_setting('plugin_name')
    assert plugin is None


# Generated at 2022-06-12 20:58:58.130944
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    configData = ConfigData()

    # init
    configData._global_settings = {
        'ansible_cache_plugins': 'jsonfile',
        'ansible_directory_layout': 'default',
        'ansible_host_key_checking': 'False',
        'ansible_callback_whitelist': 'timer'
    }

    settings = configData.get_settings()
    assert len(settings) == 4

    settings_names = [s.name for s in settings]
    assert 'ansible_cache_plugins' in settings_names
    assert 'ansible_directory_layout' in settings_names
    assert 'ansible_host_key_checking' in settings_names
    assert 'ansible_callback_whitelist' in settings_names



# Generated at 2022-06-12 20:59:04.599408
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class Plugin(object):
        def __init__(self, name):
            self.name = name
            self.type = 'module'

    config_data = ConfigData()

    # test 1 - get_settings(plugin=None)
    assert len(config_data.get_settings()) == 0

    # test 2 - get_settings(plugin=Plugin1)
    assert len(config_data.get_settings(Plugin('Plugin1'))) == 0

# Generated at 2022-06-12 20:59:15.284612
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    assert config.get_setting("fake") is None

    global_setting = PluginSetting("a", "b", "c")
    config.update_setting(global_setting)
    assert config.get_setting("a") is not None
    assert config.get_setting("a").value == "b"
    assert config.get_setting("a", PluginDescriptor("d", "e")).value == "b"

    plugin_setting = PluginSetting("a", "f", "g")
    config.update_setting(plugin_setting, PluginDescriptor("d", "e"))
    assert config.get_setting("a", PluginDescriptor("d", "e")).value == "f"
    assert config.get_setting("a").value == "b"



# Generated at 2022-06-12 20:59:20.993066
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('') is None
    assert config_data.get_setting('', plugin='a') is None
    assert config_data.get_setting('a') is None
    assert config_data.get_setting('a', plugin='a') is None

config_data = ConfigData()

# Generated at 2022-06-12 20:59:23.809452
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='verbose', value=False))
    assert config_data.get_setting(name='verbose').value is False

# Generated at 2022-06-12 20:59:26.871887
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('ansible_host_pattern', 'all'))
    assert config_data.get_setting('ansible_host_pattern') == Setting('ansible_host_pattern', 'all')

# Generated at 2022-06-12 20:59:35.929499
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    import os
    import sys
    import json


    source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    if os.path.isdir(os.path.join(source_dir, 'lib')):
        sys.path.insert(0, os.path.join(source_dir, 'lib'))
    else:
        sys.path.insert(0, os.path.join(source_dir, 'lib', 'ansible'))

    from ansible.plugins.loader import fragment_loader
    from ansible.plugins.loader import config_loader

    global_settings = []

# Generated at 2022-06-12 20:59:41.493689
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.plugins.loader import find_plugin
    from ansible.plugins.loader import plugin_loader
    from ansible.plugins.loader import lookup_loader

    config_data = ConfigData()

    for plugin_type in ['action', 'cache', 'callback', 'connection', 'filter',
                        'inventory', 'lookup', 'module_utils', 'strategy',
                        'shell']:
        plugins = plugin_loader.all(plugin_type)
        for plugin in plugins:
            instance = find_plugin(plugin_type, plugin)
            plugin_info = instance.get_option_info()
            for setting in plugin_info:
                config_data.update_setting(setting, instance)

    assert config_data._global_settings
    assert config_data._plugins



# Generated at 2022-06-12 20:59:56.350590
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    print("Testing ConfigData")
    config_data = ConfigData()
    setting = Setting("test_setting", "test_value", "test_plugin", "test_plugin_type")
    config_data.update_setting(setting)
    assert config_data._global_settings["test_setting"] == setting
    assert config_data._plugins == {}
    
    

# Generated at 2022-06-12 21:00:02.933187
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible_collections.ansible.community.plugins.module_utils.config import Setting

    config_data = ConfigData()
    setting = Setting(name="force_handlers", plugin="ansible.cfg", scope="DEFAULT")
    config_data.update_setting(setting)

    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == "force_handlers"

    settings = config_data.get_settings(plugin=setting.plugin)
    assert len(settings) == 1
    assert settings[0].name == "force_handlers"

# Generated at 2022-06-12 21:00:13.158832
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()

    # Global setting
    setting_1 = ConfigSetting('test_setting_1', 'test value 1', 'test description 1')
    data.update_setting(setting_1)
    setting = data.get_setting('test_setting_1')
    assert setting == setting_1

    # Plugin setting
    plugin_1 = ConfigPlugin('test_type_1', 'test_name_1')
    setting_2 = ConfigSetting('test_setting_2', 'test value 2', 'test description 2')
    data.update_setting(setting_2, plugin_1)
    setting = data.get_setting('test_setting_2', plugin_1)
    assert setting == setting_2



# Generated at 2022-06-12 21:00:17.505562
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Trying to update a global setting
    s1 = Setting('test', 'yes')
    d1 = ConfigData()
    d1.update_setting(s1)
    assert d1.get_setting('test') == s1

    # Trying to update a plugin setting
    s2 = Setting('test2', 'no')
    p = Plugin('test', 'test_type')
    d1.update_setting(s2, p)
    assert d1.get_setting('test2', p) is not None


# Generated at 2022-06-12 21:00:29.407775
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
	from ansible.plugins.loader import PluginLoader
	from ansible.plugins.test.test_action import DummyActionModule
	from ansible.plugins.test.test_action import DummyActionModuleSubclass
	
	config_data = ConfigData()
	
	action_loader = PluginLoader('ActionModule', 'ansible.plugins.action', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins', required_base_class=ActionBase)
	
	DummyActionModule.update_setting(Setting('dummymodule1_setting', 'dummymodule1_value'))
	DummyActionModule.update_setting(Setting('dummymodule2_setting', True))
	DummyActionModuleSubclass.update_setting(Setting('dummymodulesubclass_setting', 'dummymodulesubclass_value'))
	
	

# Generated at 2022-06-12 21:00:34.799060
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    cd = ConfigData()

    # test with empty config data
    setting = cd.get_setting('name')
    assert(setting is None)
    setting = cd.get_setting('name', 'plugin')
    assert(setting is None)

    # test with partial data
    cd.update_setting(Setting('name', 'value'))
    setting = cd.get_setting('name')
    assert(setting.name == 'name')
    assert(setting.value == 'value')
    setting = cd.get_setting('name', 'plugin')
    assert(setting is None)



# Generated at 2022-06-12 21:00:43.137713
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from os import path
    from ansible.parsing.plugin_docs import read_docstring

    config_data = ConfigData()

    lib_path = path.join(path.dirname(__file__), '..', '..', '..', '..', 'lib')
    ansible_module_utils_path = path.join(lib_path, 'ansible', 'module_utils')
    framework = path.join(ansible_module_utils_path, 'basic.py')
    basic = read_docstring(framework)

    config_data.update_setting(basic.settings[0])

# Generated at 2022-06-12 21:00:45.979617
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    assert data.get_setting(None) is None
    assert data.get_setting(None, "None") is None


# Generated at 2022-06-12 21:00:52.891265
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    config_data.update_setting(Setting(name='ANSIBLE_DEBUG',
        value='False',
        origin='command line',
        priority=5))

    assert config_data.get_setting('ANSIBLE_DEBUG') is not None
    assert config_data.get_setting('ANSIBLE_DEBUG').name == 'ANSIBLE_DEBUG'
    assert config_data.get_setting('ANSIBLE_DEBUG').value == 'False'
    assert config_data.get_setting('ANSIBLE_DEBUG').origin == 'command line'
    assert config_data.get_setting('ANSIBLE_DEBUG').priority == 5



# Generated at 2022-06-12 21:01:04.590625
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin1 = Plugin('type1','name')
    plugin2 = Plugin('type2','name')
    setting1 = Setting('core','type1','name','setting1','value1')
    setting2 = Setting('core', 'type2', 'name', 'setting2', 'value2')

    try:
        config_data.update_setting(setting1,plugin1)
    except:
        assert True
    
    try:
        config_data.update_setting(setting2, plugin2)
    except:
        assert True
    
    config_data.update_setting(setting1)
    config_data.update_setting(setting2)
    setting1_from_config = config_data.get_setting('setting1')

# Generated at 2022-06-12 21:01:34.139447
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()

    assert len(cd.get_settings()) == 0

    settings = {
        'setting1': {
            'setting1_key1': 'setting1_value1',
            'setting1_key2': 'setting1_value2'
        },
        'setting2': {
            'setting2_key1': 'setting2_value1',
            'setting2_key2': 'setting2_value2'
        },
        'setting3': {
            'setting3_key1': 'setting3_value1',
            'setting3_key2': 'setting3_value2'
        }
    }

    for s in settings:
        cd.update_setting(s)

    assert len(cd.get_settings()) == len(settings)


# Generated at 2022-06-12 21:01:41.152353
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    c = ConfigData()
    s = {'name':'test_conf_data'}
    s_type = 'test'
    plugin_name = 'test_plugin'
    plugin = {
        'type': s_type,
        'name': plugin_name
    }
    c.update_setting(s, plugin=plugin)
    assert c._plugins[s_type][plugin_name][s['name']] == s
    assert c._plugins[s_type][plugin_name][s['name']] != None
    assert c._global_settings[s['name']] == None


# Generated at 2022-06-12 21:01:44.646522
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    class Plugin():
        name = 'shell'

    plugin = Plugin()
    plugin.type = 'connection'

    class Setting():
        name = 'executable'
        value = '/bin/sh'

    setting = Setting()

    config_data.update_setting(setting, plugin)

    assert (config_data.get_settings(plugin) == [setting])


# Generated at 2022-06-12 21:01:54.754789
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data._global_settings = {'global_setting1': 'global_setting1_value'}
    config_data._plugins={'action': {'action_plugin1': {'action_setting1': 'action_setting1_value'}}}
    assert config_data.get_setting('global_setting1') == 'global_setting1_value'
    assert config_data.get_setting('action_setting1', plugin=PluginMock('action', 'action_plugin1')) == 'action_setting1_value'


# Generated at 2022-06-12 21:01:58.621574
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    data.update_setting({'name': 'foo', 'value': 'bar'})
    assert data.get_setting('foo') == {'name': 'foo', 'value': 'bar'}


# Generated at 2022-06-12 21:02:05.098471
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    assert not configData._global_settings
    assert not configData._plugins
    configData.update_setting(None)
    assert configData.get_setting(None)
    configData.update_setting("", "")
    assert configData.get_setting("")
    configData.update_setting("", "", "")
    assert configData.get_setting("", "")
    configData.update_setting("", Plugin("", ""))
    assert configData.get_setting("", Plugin("",""))


# Generated at 2022-06-12 21:02:12.262286
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansiblelint.rules import RulesCollection, RuleMatch

    rulesdir = 'lib/ansiblelint/rules'

    rules = RulesCollection.create_from_directory(rulesdir)

    config_data = ConfigData()
    config_data.update_setting(rules.rules[0].setting_name, plugin=rules.rules[0].plugin)

    assert config_data.get_setting(rules.rules[0].setting_name, plugin=rules.rules[0].plugin)

# Generated at 2022-06-12 21:02:20.260338
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import PluginLoader
    from ansible.config.setting import Setting

    config_data = ConfigData()

    # test returning setting from global settings
    global_setting1 = Setting('test_setting', 'test_value')
    config_data.update_setting(global_setting1)
    setting = config_data.get_setting(name='test_setting')
    assert setting.name == 'test_setting'
    assert setting.value == 'test_value'
    assert setting.plugin == None

    # test returning setting from plugin settings
    setting_plugin = PluginLoader('filter', 'test_filter', '', desc='A test filter plugin')
    plugin_setting1 = Setting('test_setting', 'test_value')
    config_data.update_setting(plugin_setting1, setting_plugin)
    setting = config

# Generated at 2022-06-12 21:02:30.569799
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """get settings"""

    settings = {
        'C.DEFAULT_MODULE_PATH': '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/ansible/modules',
        'C.DEFAULT_MODULE_NAME': 'command',
        'C.DEFAULT_PATHS': ['/Users/me/Workspace/ansible3/plugins/modules', '/usr/share/ansible/plugins/modules']
    }

    config_data = ConfigData()

    for setting_name, value in settings.items():
        setting = Setting(setting_name, value)
        config_data.update_setting(setting)


# Generated at 2022-06-12 21:02:38.930007
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.utils.plugin_docs import ConfigSetting

    config_data = ConfigData()

    config_setting = ConfigSetting(
        name='foo',
        description='Foo setting',
        required=True,
        default='bar',
        choices=['foo', 'bar'],
        env_var='FOO_ENV_VAR'
    )

    config_data.update_setting(config_setting)

    assert config_data.get_setting('foo') == config_setting



# Generated at 2022-06-12 21:03:16.339483
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    d = ConfigData()
    assert d.get_setting('foo') == None



# Generated at 2022-06-12 21:03:24.051870
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansiblelint.rules import RuleMatch, PluginConfiguration
    from ansiblelint.config.yaml_loader import ConfigLoader

    config_data = ConfigData()

    # default mode
    config = ConfigLoader()
    config.defaults = {'rulesdir': "/ansible/test/rules"}
    config_data.update_setting(config.defaults)
    assert config_data.get_setting('rulesdir') is not None

    # global mode
    config = ConfigLoader()
    config.defaults = {'rulesdir': "/ansible/test/rules"}
    config_data.update_setting(config.defaults)
    assert config_data.get_setting('rulesdir') is not None

    # plugin mode
    plugin = PluginConfiguration("test", "action", "test")
    config = ConfigLoader()

# Generated at 2022-06-12 21:03:25.557468
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    assert not config_data.get_settings
