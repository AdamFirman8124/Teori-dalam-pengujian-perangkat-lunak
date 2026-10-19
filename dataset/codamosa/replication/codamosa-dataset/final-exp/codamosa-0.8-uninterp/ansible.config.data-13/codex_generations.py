

# Generated at 2022-06-12 20:53:30.926170
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configData.update_setting('one')
    configData.update_setting('two', 'plugin')
    configData.update_setting('three', ('type', 'name'))
    assert configData.get_setting('one') == 'one'
    assert configData.get_setting('two', 'plugin') == 'two'
    assert configData.get_setting('three', ('type', 'name')) == 'three'


# Generated at 2022-06-12 20:53:38.667339
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    config_data.update_setting(ConfigSetting('setting1', 'setting1_value'))
    assert config_data.get_setting('setting1') == ConfigSetting('setting1', 'setting1_value')

    plugin = Plugin('my_plugin', 'action')
    config_data.update_setting(ConfigSetting('setting2', 'setting2_value'), plugin)
    assert config_data.get_setting('setting2') == ConfigSetting('setting2', 'setting2_value')



# Generated at 2022-06-12 20:53:48.345794
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    # Unknown setting
    setting = config.get_setting(name='unknown_setting')
    assert setting is None

    # Global setting
    setting = config.get_setting(name='global_setting')
    assert setting is None

    # Plugin setting
    plugin = Plugin('plugins_type', 'plugin_name')
    setting = config.get_setting(name='plugin_setting', plugin=plugin)
    assert setting is None

    # Add global setting and then check its value
    config.update_setting(Setting('global_setting', 'global_value'))
    setting = config.get_setting(name='global_setting')
    assert setting is not None
    assert setting.value == 'global_value'

    # Add plugin setting and then check its value

# Generated at 2022-06-12 20:53:54.979902
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()

    print("TEST: test_ConfigData_get_settings")
    print("TEST: test_ConfigData_get_settings global")
    setting = {'name': 'foo'}
    configData.update_setting(setting)
    assert configData.get_settings()[0].name == 'foo'

    print("TEST: test_ConfigData_get_settings plugin")
    plugin = {'name': 'baz', 'type': 'fizz'}
    setting = {'name': 'foo'}
    configData.update_setting(setting, plugin)
    assert configData.get_settings(plugin)[0].name == 'foo'

    print("PASS: test_ConfigData_get_settings")

# Generated at 2022-06-12 20:54:03.312320
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Instantiates ConfigData()
    config_data = ConfigData()

    # Add a new Global Setting to config_data
    config_data.update_setting(Setting('name_global_setting', 'global_value'))

    # Assert if the global setting was added
    assert config_data.get_settings()[0].name == 'name_global_setting'
    assert config_data.get_settings()[0].value == 'global_value'


# Generated at 2022-06-12 20:54:09.883166
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting_dict({'a': [1, 2, 3]})
    config_data.update_setting_dict({'b': [2, 3, 4]})
    config_data.update_setting_dict({'c': [3, 4, 5]})
    assert config_data._global_settings == {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}

    assert config_data.get_setting('b') == [2, 3, 4]



# Generated at 2022-06-12 20:54:20.815112
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    plugin_type = 'type'
    plugin_name = 'name'
    config_data = ConfigData()
    assert config_data._plugins == {}

    #Test UPDATE
    setting = {}
    setting['name'] = 'name'
    setting['plugin'] = Plugin(plugin_type, plugin_name)
    setting['value'] = 'value'
    setting['origin'] = 'origin'
    setting['priority'] = 1200
    config_data.update_setting(setting)
    assert config_data._plugins[plugin_type][plugin_name][setting['name']] == setting

    #Test UPDATE again
    setting['priority'] = 1300
    config_data.update_setting(setting)
    assert config_data._plugins[plugin_type][plugin_name][setting['name']] == setting

    #Test different origin
    setting['origin']

# Generated at 2022-06-12 20:54:31.025258
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from __main__ import Config
    from __main__ import Plugin

    # Not testing the parsing methods here, just the get_settings method of ConfigData

    config_data = ConfigData()

    cfg = Config(["-t", "plugins/lookup/ansible/gce.py", "-t", "plugins/cache/redis.py"])

    config_data.update_setting(cfg.get_setting(
        "gcp_service_account_contents"), Plugin(None, "lookup", "ansible", "gce"))
    config_data.update_setting(cfg.get_setting(
        "service_account_contents"), Plugin(None, "cache", "", "redis"))

    lookups = config_data.get_settings()
    assert len(lookups) == 2
    assert lookups[0].plugin_

# Generated at 2022-06-12 20:54:38.343113
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    config_data.update_setting(Setting('test_global'))

    plugin = Plugin('test_plugin')
    config_data.update_setting(Setting('test_plugin'), plugin)

    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'test_global'

    settings = config_data.get_settings(plugin)
    assert len(settings) == 1
    assert settings[0].name == 'test_plugin'


# Generated at 2022-06-12 20:54:48.847845
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    from ansible.config.setting import Setting
    from ansible.plugins.loader import PluginLoader
    plugin_loader = PluginLoader()
    plugin = plugin_loader.get('callback', 'default')
    setting = Setting('callback_whitelist', ['debug', 'profile_tasks'], plugin)
    setting2 = Setting('callback_whitelist', ['debug', 'profile_tasks'], plugin)
    setting3 = Setting('callback_whitelist', ['debug', 'profile_tasks'], None)
    config_data.update_setting(setting)
    config_data.update_setting(setting2, plugin)
    config_data.update_setting(setting3)
    settings = config_data.get_settings()
    assert len(settings) == 2

# Generated at 2022-06-12 20:55:01.623667
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    global_setting = Setting(name='timeout', value=123, origin='defaults')
    config_data.update_setting(global_setting)
    plugin = Plugin('cache', 'redis', 'fact_cache')
    plugin_setting = Setting(name='host', value='127.0.0.1', origin='ansible.cfg')
    config_data.update_setting(plugin_setting, plugin)
    print(config_data.get_setting('timeout', None))
    print(config_data.get_setting('host', plugin))

if __name__ == "__main__":
    test_ConfigData_get_setting()

# Generated at 2022-06-12 20:55:12.695716
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    config_data.update_setting(ConfigSetting('foo', 'bar'))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'foo'
    assert settings[0].value == 'bar'

    config_data.update_setting(ConfigSetting('foo', 'baz'))
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'foo'
    assert settings[0].value == 'baz'

    config_data.update_setting(ConfigSetting('bar', 'baz'))
    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'foo'
    assert settings[0].value

# Generated at 2022-06-12 20:55:15.958453
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configData.update_setting("hello")
    assert configData._global_settings["hello"] == "hello"

# Generated at 2022-06-12 20:55:26.976555
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    d = ConfigData()

    assert d.get_setting("bla") == None

    from ansible.plugins.loader import PluginLoader

    p = PluginLoader()
    assert d.get_setting("bla", p.get("action")) == None
    assert d.get_setting("bla", p.get("cache")) == None
    assert d.get_setting("bla", p.get("callback")) == None
    assert d.get_setting("bla", p.get("cliconf")) == None
    assert d.get_setting("bla", p.get("connection")) == None
    assert d.get_setting("bla", p.get("doc_fragment")) == None
    assert d.get_setting("bla", p.get("filter")) == None

# Generated at 2022-06-12 20:55:34.437156
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
   c = ConfigData()
   c.update_plugin_setting(Setting("foo", "foo"), "bar", "bar")
   s = c.get_settings("bar", "bar")
   assert s == [Setting("foo", "foo")]

   c.update_plugin_setting(Setting("foo", "bar"), "bar", "bar")
   s = c.get_setting("foo", "bar", "bar")
   assert s == Setting("foo", "bar")

# Generated at 2022-06-12 20:55:44.792713
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    # Create instance of class ConfigData
    configData = ConfigData()

    # Update global setting
    configData.update_setting(Setting('test_global_setting', 'test_value', 'test_section'))
    assert configData._global_settings.get('test_global_setting').value == 'test_value'

    # Update global setting
    configData.update_setting(Setting('test_global_setting', 'test_2_value', 'test_section'))
    assert configData._global_settings.get('test_global_setting').value == 'test_2_value'

    # Create instance of class Plugin
    plugin = Plugin('test_plugin', 'test_type')

    # Update plugin setting

# Generated at 2022-06-12 20:55:52.903942
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    class TestPlugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name
    cd = ConfigData()
    cd.update_setting('t1', TestPlugin(type='t2', name='t3'))
    cd.update_setting('t4', TestPlugin(type='t5', name='t6'))
    cd.update_setting('t7', TestPlugin(type='t8', name='t9'))
    cd.update_setting('t10', TestPlugin(type='t11', name='t12'))
    cd.update_setting('t13', TestPlugin(type='t14', name='t15'))
    assert len(cd.get_settings()) == 0

# Generated at 2022-06-12 20:56:03.678429
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    from collections import namedtuple
    Plugin = namedtuple('Plugin', ['type', 'name'])

    # Test for global config with full list of attributes
    from ansiblelint import RuleMatch
    setting = RuleMatch('test_id', 'test_message', 'test_path', 'test_linenb', 'test_column')
    config_data.update_setting(setting)

    # Test for global config with empty plugin
    setting = config_data.get_setting('test_id', Plugin('test_type', 'test_name'))
    assert setting is not None
    assert setting == RuleMatch('test_id', 'test_message', 'test_path', 'test_linenb', 'test_column')

    # Test for non-existing config
    setting = config_data.get_setting

# Generated at 2022-06-12 20:56:10.468320
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configdata = ConfigData()

    # Test 1: Get a plugin setting
    (plugin_type, plugin_name) = ('lookup', 'password')
    configdata.update_setting(ConfigSetting('password', 'abc123'), PluginInfo(plugin_type, plugin_name))
    setting = configdata.get_setting('password', PluginInfo(plugin_type, plugin_name))
    assert setting.value == 'abc123'

    # Test 2: Get a non existent setting
    setting = configdata.get_setting('does_not_exist')
    assert setting is None

    # Test 3: Get a global setting (not plugin specific)
    configdata.update_setting(ConfigSetting('debug', False))
    setting = configdata.get_setting('debug')
    assert setting.value == False


# Generated at 2022-06-12 20:56:18.013077
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data1 = ConfigData()
    data1.update_setting(ConfigSetting(name='greeting', value='hello'))
    assert data1._global_settings.get('greeting').value == 'hello'
    data1.update_setting(ConfigSetting(name='greeting', value='hello'), plugin=Plugin(name='helloplug', type='lookup'))
    assert data1._plugins['lookup']['helloplug']['greeting'].value == 'hello'



# Generated at 2022-06-12 20:56:29.418877
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    my_config = ConfigData()
    setting_name = "name"
    setting_value = "value"
    my_config.update_setting(Setting(setting_name, setting_value, None, 'ini'))
    assert my_config.get_setting(setting_name, None).name == setting_name
    assert my_config.get_setting(setting_name, None).value == setting_value


# Generated at 2022-06-12 20:56:34.683203
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    _config_data = ConfigData()
    _config_data.update_setting(Setting(name='test', value='test'))
    assert 'test' == _config_data.get_setting(name='test')



# Generated at 2022-06-12 20:56:41.977344
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint import RunnerConfig, RunnerConfigSetting

    # test global settings
    config_data = ConfigData()
    setting = RunnerConfigSetting('foo', 'bar')
    config_data.update_setting(setting)
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0] == setting

    # test plugin settings
    plugin = RunnerConfig.get_plugin_config('AnsibleLint')
    setting = RunnerConfigSetting('foo', 'bar')
    config_data.update_setting(setting, plugin)
    settings = config_data.get_settings(plugin)
    assert len(settings) == 1
    assert settings[0] == setting


# Generated at 2022-06-12 20:56:51.025383
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    global_setting=Setting("key1","value1")
    global_setting2=Setting("key2","value2")
    plugin_setting=Setting("key3","value3")
    plugin = PluginDefinition("plugin_type1", "plugin_name1")
    config=ConfigData()
    config.update_setting(global_setting)
    config.update_setting(global_setting2)
    config.update_setting(plugin_setting,plugin)
    assert config.get_setting("key2") == global_setting2
    assert config.get_setting("key3",plugin) == plugin_setting


# Generated at 2022-06-12 20:56:57.986914
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    new_setting = Setting('abc', 'abc', 456)
    config_data.update_setting(new_setting)
    assert config_data.get_setting('abc') == new_setting
    assert config_data.get_settings()[0] == new_setting

    new_setting1 = Setting('def', 'def', 789)
    new_plugin1 = Plugin('type1', 'plugin1')
    config_data.update_setting(new_setting1, new_plugin1)
    assert config_data.get_setting('def', new_plugin1) == new_setting1
    assert config_data.get_settings(new_plugin1)[0] == new_setting1

    new_setting2 = Setting('ghi', 'ghi', 123)

# Generated at 2022-06-12 20:56:59.901494
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []



# Generated at 2022-06-12 20:57:09.033258
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import os
    import tempfile
    from ansible.config.setting import Setting
    # create temporary config file and setting file
    tmpdir = tempfile.mkdtemp()
    tmpini = os.path.join(tmpdir, 'ansible.cfg')
    tmpini2 = os.path.join(tmpdir, 'ansible.cfg2')
    test_config_data = ConfigData()
    config_parser = configparser.ConfigParser()
    # create a setting and add it to the config data
    some_setting = Setting('foo', 'bar')
    test_config_data.update_setting(some_setting)
    # create another setting and add it to the config data
    another_setting = Setting('baz', 'bat')
    test_config_data.update_setting(another_setting)
    # write out config file


# Generated at 2022-06-12 20:57:17.193387
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting1 = ConfigSetting('foo', 'bar')
    config.update_setting(setting1)
    setting2 = ConfigSetting('bar', 'baz')
    assert setting1 == config.get_setting('foo')
    assert setting2 != config.get_setting('bar')
    assert config.get_setting('bar') is None

    plugin1 = ConfigPlugin('foo', 'bar')
    setting3 = ConfigSetting('foo', 'bar')
    config.update_setting(setting3, plugin1)
    assert setting3 == config.get_setting('foo', plugin1)
    assert config.get_setting('foo') == setting1


# Generated at 2022-06-12 20:57:23.249170
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from collections import namedtuple
    config = ConfigData()
    Plugin = namedtuple('Plugin', ['type', 'name'])
    plugin = Plugin('test_type', 'test_name')
    settings = config.get_settings()
    assert settings == []
    settings = config.get_settings(plugin)
    assert settings == []


# Generated at 2022-06-12 20:57:33.604553
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # setting_name is present in global settings
    setting = mock_setting_get("setting_name", "setting_value")
    config_data.update_setting(setting)
    expected_setting = config_data.get_setting("setting_name")
    assert setting == expected_setting

    # setting_name is present in plugin settings
    plugin = mock_plugin_get("plugin_name", "plugin_type")
    expected_setting = mock_setting_get("setting_name", "setting_value")
    config_data.update_setting(expected_setting, plugin)
    actual_setting = config_data.get_setting("setting_name", plugin)
    assert expected_setting == actual_setting
    assert actual_setting is not None

    # setting_name is not present in global nor plugin settings
    actual

# Generated at 2022-06-12 20:57:48.910933
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()
    plugin_type = 'test_type'
    plugin_name = 'test_name'

    plugin1 = Plugin(plugin_type, plugin_name)
    setting1 = Setting('test_name1', type='string', default='test_default_value1')
    setting2 = Setting('test_name2', type='string', default='test_default_value2')

    plugin2 = Plugin(plugin_type, 'test_name2')
    setti

# Generated at 2022-06-12 20:57:59.055053
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    from ansible.config.setting import Setting

    setting_1 = Setting('name', 'value', 'http://foo.bar')
    setting_2 = Setting('name2', 'value2', 'http://bar.baz', 'user')
    setting_3 = Setting('name3', 'value3', 'http://foo.bar', 'baz')

    config_data.update_setting(setting_1)
    config_data.update_setting(setting_2)
    config_data.update_setting(setting_3)

    assert config_data.get_setting('name').value == 'value'
    assert config_data.get_setting('name2', 'user').value == 'value2'
    assert config_data.get_setting('name3', 'baz').value == 'value3'


# Generated at 2022-06-12 20:58:05.059686
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting('set1', 'value1')
    plugin = Plugin('type1', 'name1')
    config_data.update_setting(setting)
    config_data.update_setting(setting, plugin)
    assert setting == config_data.get_setting('set1')
    assert setting == config_data.get_setting('set1', plugin)

# Generated at 2022-06-12 20:58:08.984081
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = dict({"name":"name1","value":{"a":"1"}})
    plugin = dict({"type":"type1","name":"name1"})
    config_data.update_setting(setting,plugin)
    print(config_data._global_settings)
    print(config_data._plugins)
    assert "name1" == config_data._global_settings["name1"]["name"]
    assert "name1" == config_data._plugins["type1"]["name1"]["name1"]["name"]

# Test for methods of class ConfigData

# Generated at 2022-06-12 20:58:11.854325
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []
    assert config_data.get_settings(None) == []


# Generated at 2022-06-12 20:58:18.257932
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert len(cd.get_settings()) == 0

    config = {'foo': {'type': 'file', 'name': 'foo', 'foo': 'bar'}}
    cd.update_setting(Setting(config['foo']))
    assert len(cd.get_settings()) == 1

    settings = cd.get_settings()
    assert settings[0].type == config['foo']['type']
    assert settings[0].name == config['foo']['name']
    assert settings[0].get('foo') == config['foo']['foo']



# Generated at 2022-06-12 20:58:27.670069
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    details = {'details': {'msg': 'Setting definitions for plugin: Type: action, Name: my_action'}}
    plugin_type = 'action'
    plugin_name = 'my_action'
    setting_name = 'setting_name'
    setting_value = 'setting_value'
    setting = Setting(setting_name, setting_value, plugin_type, plugin_name, details)
    plugin = Plugin(plugin_type, plugin_name)
    config = ConfigData()
    config.update_setting(setting, plugin)
    assert config.get_settings() == []
    assert config.get_settings(plugin) == [setting]


# Generated at 2022-06-12 20:58:38.646143
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config = ConfigData()
    config.update_setting(Setting('action_plugins', 'action_plugins', '/home/ubuntu/ansible/action_plugins'))
    config.update_setting(Setting('library', 'library', '/home/ubuntu/ansible/library'))
    config.update_setting(Setting('vault_password_file', 'vault_password_file', '/home/ubuntu/.ansible/vault'))
    config.update_setting(Setting('roles_path', 'roles_path', '/home/ubuntu/ansible/roles'))
    config.update_setting(Setting('deprecation_warnings', 'deprecation_warnings', 'false'))
    config.update_setting(Setting('host_key_checking', 'host_key_checking', 'false'))

# Generated at 2022-06-12 20:58:45.474010
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cfg = ConfigData()
    assert [] == cfg.get_settings()
    cfg.update_setting({'name': 'a', 'value': 'b'})
    assert [{'name': 'a', 'value': 'b'}] == cfg.get_settings()
    assert [{'name': 'a', 'value': 'b'}] == cfg.get_settings(None)
    from ansible.module_utils.common.collections import ImmutableDict
    class Plugin(ImmutableDict):
        def __init__(self, x):
            self.name = x
            self.type = 'x'
            super(Plugin, self).__init__()
    cfg.update_setting({'name': 'a', 'value': 'x'}, Plugin('cfg'))

# Generated at 2022-06-12 20:58:52.119639
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_config = ConfigData()
    assert test_config._global_settings == {}
    assert test_config._plugins == {}

    assert len(test_config.get_settings()) == 0
    assert test_config.get_setting('foo') is None
    assert test_config.get_setting('foo', plugin=object()) is None


# Generated at 2022-06-12 20:59:12.917429
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert len(settings) == 0

    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.common.plugin_config import PluginConfig
    plugin_config = PluginConfig(name='fake_plugin', type='fake_type')
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.common.config.setting import Setting
    setting = Setting(name='fake_setting', value='fake_value')
    config_data.update_setting(setting, plugin=plugin_config)
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'fake_setting'

# Generated at 2022-06-12 20:59:20.011617
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    def test_ConfigData_get_settings_test01():

        config_data = ConfigData()

        config_data.update_setting(Setting('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'))
        config_data.update_setting(Setting('b','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'))
        config_data.update_setting(Setting('c','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'))

# Generated at 2022-06-12 20:59:29.643530
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # Test case-1: Check global exists
    config_setting = {"name": "foo_setting_1", "value": "bar_setting_1", "origin": "unit test"}

    from module_utils.config import Setting
    setting = Setting(config_setting)
    config_data.update_setting(setting)

    from module_utils.common.collections import ImmutableDict
    from module_utils.connection import Connection
    connection = Connection(ImmutableDict(config_data.get_setting("foo_setting_1").config))
    assert connection.value == config_setting["value"]

    # Test case-2: Check plugin exists
    plugin_type = "connection"
    plugin_name = "local"

# Generated at 2022-06-12 20:59:37.851859
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    assert len(config.get_settings()) == 0

    config = ConfigData()
    config_data = {'ANSIBLE_COMMAND_WARNINGS': 'False'}
    for key, value in config_data.items():
        config.update_setting(Setting(key, value))

    settings = config.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'ANSIBLE_COMMAND_WARNINGS'
    assert settings[0].value == 'False'


# Generated at 2022-06-12 20:59:42.089335
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = AnsiblePlugin(type=C.CORE, name=C.DEFAULT)
    setting = ConfigSetting(name='TASKS', plugin=plugin)
    config_data.update_setting(setting)
    settings = config_data.get_settings()
    assert len(settings) == 1

# Generated at 2022-06-12 20:59:44.569341
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    
    # Create a ConfigData and a Setting objects
    conf_data = ConfigData()
    setting = Setting()
    setting.name = "ssh_args"
    setting.plugin = "Connection"

    # Update the setting in the ConfigData
    conf_data.update_setting(setting, setting.plugin)

    # Check the setting was updated
    assert conf_data._plugins["Plugin"][setting.name] == [setting]


# Generated at 2022-06-12 20:59:52.735956
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting("test_setting", "test_value")
    plugin = Plugin("test_plugin", "test_type")
    config_data.update_setting(setting)
    assert(config_data.get_setting("test_setting").name=="test_setting")
    assert (config_data.get_setting("test_setting").value == "test_value")
    config_data.update_setting(setting, plugin)
    assert (config_data.get_setting("test_setting", plugin).name == "test_setting")
    assert (config_data.get_setting("test_setting", plugin).value == "test_value")
    assert(config_data.get_setting("test_setting").name == "test_setting")

# Generated at 2022-06-12 20:59:58.199782
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    print(config_data.update_setting('test', 'plugin'))
    config_data.update_setting('test', 'plugin')
    config_data.update_setting('test', 'plugin')
    return config_data.get_setting('test', 'plugin')

# Generated at 2022-06-12 21:00:09.063969
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from _fixtures import test_data
    from _fixtures import test_config
    from _fixtures import test_plugin
    from ansible.parsing.plugin_docs import get_docstring

    plugin = test_plugin(test_data.DOCSTRING_DOCUMENTATION_PLUGIN_DATA)
    module_docstring = get_docstring(object, lines=test_data.DOCSTRING_DOCUMENTATION_BLANK_LINES_MULTI)
    config_data = ConfigData()

    # Test updating setting for plugin
    config_data.update_setting(test_config.ConfigSetting(plugin, module_docstring, 'LOG_PATH', 'path to log file',
                                                         test_config._get_validator('path'), test_config.ConfigValue()))

# Generated at 2022-06-12 21:00:12.841038
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    # Verify that when no plugin is passed in, the global_settings are returned
    assert config.get_settings() == config._global_settings
    # Verify that when an unknown plugin is passed in an empty array is returned.
    assert config.get_settings(plugin=None) == []

# Generated at 2022-06-12 21:00:31.964857
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_config = ConfigData()
    test_config.update_setting("test")
    assert("test" in test_config._global_settings)
    assert("test" not in test_config._plugins)

# Generated at 2022-06-12 21:00:36.114074
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import PluginLoader

    config_data = ConfigData()

    connection_plugins = PluginLoader('Connection', 'ansible.plugins.connection', config_data)
    assert len(config_data.get_settings(connection_plugins.get('local'))) == 1
    assert config_data.get_settings(connection_plugins.get('local'))[0].name == 'executable'

    lookup_plugins = PluginLoader('Lookup', 'ansible.plugins.lookup', config_data)
    assert len(config_data.get_settings(lookup_plugins.get('file'))) == 1
    assert config_data.get_settings(lookup_plugins.get('file'))[0].name == 'base_dir'

# Generated at 2022-06-12 21:00:42.778717
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    c = ConfigData()

    assert c.get_settings() == []

    sg = ConfigSetting('host_key_checking')
    c.update_setting(sg)

    assert c.get_settings() == [sg]

    s = ConfigSetting('host_key_checking')
    c.update_setting(s, MockPlugin())

    assert c.get_settings() == [sg]

    sp = c.get_settings(MockPlugin())

    assert sp == [s]




# Generated at 2022-06-12 21:00:52.507825
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()

    setting_0 = Setting(
            name='setting_0',
            value='setting_value_0',
            description='setting description 0',
            plugin=Plugin(
                    type='test',
                    name='test_plugin_0'))
    configData.update_setting(setting_0)

    setting_1 = Setting(
            name='setting_1',
            value='setting_value_1',
            description='setting description 1',
            plugin=Plugin(
                    type='test',
                    name='test_plugin_1'))
    configData.update_setting(setting_1)


# Generated at 2022-06-12 21:00:53.011891
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass

# Generated at 2022-06-12 21:01:04.723183
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # Create value of ConfigData class
    config_data = ConfigData()

    # Global settings
    global_setting = ConfigSetting(name='global_setting', path='/global/setting', value='global_setting_value')
    config_data.update_setting(global_setting)

    # Plugin settings
    plugin_1_setting_1 = ConfigSetting(name='plugin_1_setting_1', path='/plugin/1/setting/1', value='plugin_1_setting_1_value')
    plugin_1_setting_2 = ConfigSetting(name='plugin_1_setting_2', path='/plugin/1/setting/2', value='plugin_1_setting_2_value')
    plugin_1 = ConfigPlugin(type='type_1', name='plugin_1', version='1.0.0')
    config_data.update

# Generated at 2022-06-12 21:01:12.921934
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    """
    Tests the methods update_setting of class ConfigData
    :return:
    """

    from ansible.module_utils.common._collections_compat import MutableMapping

    config_data = ConfigData()

    # Test that plugin settings are stored separately from global settings
    global_setting = Setting('')
    config_data.update_setting(global_setting)
    assert isinstance(config_data._global_settings, MutableMapping)
    assert config_data._global_settings.get(global_setting.name) is global_setting
    assert not isinstance(config_data._plugins, MutableMapping)
    assert config_data._plugins == {}

    plugin_setting = Setting('')
    plugin_type = 'test_type'
    plugin_name = 'test_name'

# Generated at 2022-06-12 21:01:17.664017
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # most simple test:
    # update a setting and get it again

    # prepare test data
    data = ConfigData()
    test_setting = ConfigSetting('key', 'value')

    # prepare test object
    data.update_setting(test_setting)

    # test
    assert data.get_setting('key') == test_setting.value

# Generated at 2022-06-12 21:01:20.961351
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings(plugin=None) == []
    assert config_data.get_settings(plugin=FLAGS) == []


# Generated at 2022-06-12 21:01:30.724625
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data._global_settings['some_setting'] = 1
    config_data._global_settings['some_other_setting'] = 2
    config_data._plugins['some_type'] = {}
    config_data._plugins['some_type']['some_plugin'] = {}
    config_data._plugins['some_type']['some_plugin']['some_setting'] = 3
    config_data._plugins['some_type']['some_plugin']['some_other_setting'] = 5

    # check for default
    assert(len(config_data.get_settings()) == 2)
    assert(len(config_data.get_settings(None)) == 2)

    # check for module specific settings

# Generated at 2022-06-12 21:01:52.113913
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible import constants as C
    from ansible.plugins.loader import find_plugin_file

    config_data = ConfigData()

    plugin, path = find_plugin_file('connection', 'local')
    plugin.type = 'connection'
    plugin.name = 'local'
    setting = C.ConfigLine('local')
    setting.value = '/path/to/ansible'
    config_data.update_setting(setting, plugin)

    assert config_data.get_setting('local', plugin).value == '/path/to/ansible'


# Generated at 2022-06-12 21:02:03.051241
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()

    class setting:
        def __init__(self, n, v, d):
            self.name = n
            self.value = v
            self.default = d

    s1 = setting('a', 'value_of_a', 'default_of_a')
    s2 = setting('b', 'value_of_b', 'default_of_b')

    configdata.update_setting(s1, plugin=None)
    configdata.update_setting(s2, plugin=None)

    assert configdata.get_setting('a') == s1
    assert configdata.get_setting('b') == s2

    class plugin:
        def __init__(self, t, n):
            self.type = t
            self.name = n


# Generated at 2022-06-12 21:02:11.767077
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    test_setting_1 = Setting()
    test_setting_1.name = 'setting_1'
    test_setting_1.value = 'test_value_1'
    test_setting_2 = Setting()
    test_setting_2.name = 'setting_2'
    test_setting_2.value = 'test_value_2'
    config_data.update_setting(test_setting_1)
    config_data.update_setting(test_setting_2)
    settings = config_data.get_settings()
    assert len(settings) == 2

# Generated at 2022-06-12 21:02:19.974335
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    setting_1 = {}
    setting_1["name"] = "setting_1"
    setting_1["type"] = "bool"
    setting_1["default"] = False
    setting_1["env"] = "ANSIBLE_CORE_SETTING_1"
    setting_1["ini"] = "core_setting_1"
    setting_1["const"] = "CORE_SETTING_1"
    setting_1["cli"] = ["-S", "--core-setting-1"]
    setting_1["version_added"] = "2.5"
    setting_1["category"] = ("core",)
    setting_1["description"] = "Core setting 1"
    setting_1["subset"] = "connection,inventory,vars"

    setting_2 = {}
    setting_

# Generated at 2022-06-12 21:02:30.390341
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting("name1") is None
    config.update_setting(Setting("name1", "value1", is_secret=False))
    assert config.get_setting("name1") == Setting("name1", "value1", is_secret=False)

    # plugin is None
    assert config.get_setting("name1", Plugin("type", "name")) is None
    config.update_setting(Setting("name1", "value1", is_secret=False), Plugin("type", "name"))
    assert config.get_setting("name1") == Setting("name1", "value1", is_secret=False)

    config.update_setting(Setting("name2", "value2", is_secret=False), Plugin("type", "name"))

# Generated at 2022-06-12 21:02:38.838386
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    # Create a fake SettingInstance
    class FakeSettingInstance():
        def __init__(self):
            self.name = 'test'

    # Create fake SettingInstance and update config_data
    fake_setting_instance = FakeSettingInstance()
    config_data.update_setting(fake_setting_instance, None)

    # Check of returned value is correct
    assert config_data.get_setting('test', None).name == fake_setting_instance.name

# Generated at 2022-06-12 21:02:41.009637
# Unit test for method update_setting of class ConfigData

# Generated at 2022-06-12 21:02:46.740056
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    config.update_setting(Setting('base_path', '/path/to/base'))
    settings = config.get_settings()
    assert len(settings) == 1
    assert settings[0].name == 'base_path'
    assert settings[0].value == '/path/to/base'
    assert settings[0].scope == 'global'
    config.update_setting(Setting('cache_path', '/path/to/cache'))
    settings = config.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'base_path'
    assert settings[0].value == '/path/to/base'
    assert settings[0].scope == 'global'
    assert settings[1].name == 'cache_path'

# Generated at 2022-06-12 21:02:53.646391
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from collections import namedtuple

    plugin = namedtuple('plugin', ['type', 'name'])
    configData = ConfigData()
    setting = None

    configData.update_setting(setting)
    global_settings = configData.get_settings()
    assert setting in global_settings

    configData.update_setting(setting, plugin='filter')
    plugins = configData.get_settings(plugin)
    assert global_settings + [setting] == plugins


# Generated at 2022-06-12 21:03:04.764492
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='foo', value='bar', origin='test-file'))
    config_data.update_setting(Setting(name='baz', value='qux', origin='test-file'))
    settings = config_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'foo'
    assert settings[0].value == 'bar'
    assert settings[0].origin == 'test-file'
    assert settings[1].name == 'baz'
    assert settings[1].value == 'qux'
    assert settings[1].origin == 'test-file'

    # test invalid plugin
    settings = config_data.get_settings(Plugin(type='foo', name='bar'))
    assert settings == []
