

# Generated at 2022-06-12 20:53:29.163635
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    cd._global_settings['test1'] = 'test2'
    assert cd.get_setting('test1') == 'test2'


# Generated at 2022-06-12 20:53:34.532590
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()
    plugin2 = Plugin(name="dummy_plugin")
    setting2 = Setting(name="new_setting", value="new_value", plugin=plugin2)
    configdata.update_setting(setting2, plugin2)
    print(configdata.get_setting("new_setting", plugin2))

    plugin1 = Plugin(name="dummy_plugin")
    setting1 = Setting(name="new_setting", value="new_value", plugin=plugin1)
    configdata.update_setting(setting1, plugin1)
    print(configdata.get_setting("new_setting", plugin1))

    plugin = Plugin(name="dummy_plugin")
    setting = Setting(name="new_setting", value="new_value", plugin=plugin)
    configdata.update_setting(setting)

# Generated at 2022-06-12 20:53:35.910531
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    assert (callable(ConfigData.update_setting))



# Generated at 2022-06-12 20:53:46.468669
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = {'name': u'cacert', 'metadata': {'host': u'inventory_hostname'}}
    config_data.update_setting(setting1)
    setting2 = {'name': u'cacert', 'metadata': {'host': u'inventory_hostname', 'plugin_type': u'action_plugin', 'plugin_name': u'CommandModule'}}
    config_data.update_setting(setting2)
    setting3 = {'name': u'cacert', 'metadata': {'host': u'inventory_hostname', 'plugin_type': u'cache_plugin', 'plugin_name': u'Redis'}}
    config_data.update_setting(setting3)

# Generated at 2022-06-12 20:53:53.797045
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    # Initialise plugin and setting names
    plugin_name = "sample_plugin"
    setting_name = "sample_setting"

    # Initialise plugin and setting values
    plugin_value = "sample_value"
    setting_value = "test_value"

    # Initialise Plugin and Setting objects
    plugin = Plugin(plugin_name, plugin_value)
    setting = Setting(setting_name, setting_value)

    # Initialise ConfigData object
    config_data = ConfigData()

    # Assign ``setting`` to ``config_data``
    config_data.update_setting(setting, plugin)

    # Call method get_setting on ``config_data``
    actual_setting = config_data.get_setting(setting_name, plugin)

    # Assert result with expected output
    assert actual_setting == setting


# Unit test

# Generated at 2022-06-12 20:53:58.226927
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configuration = ConfigData()
    setting_test_1 = Setting.from_dict(dict(name='test', value='config_value_1'))
    plugin = Plugin(type='action', name='action1')
    global_setting_test_2 = Setting.from_dict(dict(name='test2', value='config_value_2'))
    plugin_setting_test_3 = Setting.from_dict(dict(name='test3', value='config_value_3'))

    assert 'test' not in configuration._global_settings
    assert 'action' not in configuration._plugins
    assert 'action1' not in configuration._plugins['action']
    assert 'test' not in configuration._plugins['action']['action1']

    configuration.update_setting(setting_test_1)
    assert 'test' in configuration._global_settings



# Generated at 2022-06-12 20:54:09.034443
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    setting = Setting('default')
    cd.update_setting(setting)
    assert cd.get_setting('default') == setting
    assert cd.get_setting('default', None) == setting

    plugin = Plugin(None, 'test1')
    setting = Setting('default')
    cd.update_setting(setting, plugin)
    assert cd.get_setting('default', plugin) == setting
    assert cd.get_setting('default') == setting
    assert cd.get_setting('default', None) == setting

    plugin = Plugin(None, 'test2')
    setting = Setting('default')
    cd.update_setting(setting, plugin)
    assert cd.get_setting('default') == setting
    assert cd.get_setting('default', None) == setting

# Generated at 2022-06-12 20:54:18.704086
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    from ansible.plugins.loader import shared_loader
    plugin = shared_loader.find_plugin('connection', 'SSH')

    setting = Setting('foo', 'bar', None, None, None, None)
    config_data.update_setting(setting)

    setting = Setting('foo', 'bar', None, None, None, None)
    config_data.update_setting(setting, plugin)

    assert setting in config_data.get_settings(plugin)
    assert setting in config_data.get_settings()


# Generated at 2022-06-12 20:54:28.997276
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    # Set up global setting
    setting = ConfigSetting(name="strict")
    config_data.update_setting(setting)

    # Set up a collection setting
    setting = ConfigSetting(name="collections_paths", plugin=ConfigPlugin(name="foo", type="collection"))
    config_data.update_setting(setting)

    # Set up another collection setting
    setting = ConfigSetting(name="default_collection", plugin=ConfigPlugin(name="bar", type="collection"))
    config_data.update_setting(setting)

    assert config_data.get_setting("strict")
    assert config_data.get_setting("collections_paths", plugin=ConfigPlugin(name="foo", type="collection"))

# Generated at 2022-06-12 20:54:36.579779
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from __main__ import ConfigData

    cd = ConfigData()

    assert len(cd.get_settings()) == 0, 'test_ConfigData_update_setting: unexpected number of settings on empty'

    cd.update_setting(ConfigSetting(name='module_setup', description='mod_set', value=True))
    cd.update_setting(ConfigSetting(name='internal_testing', description='int_test', value=False, plugin=PluginDefinition('callback', 'skiptest')))

    assert len(cd.get_settings()) == 1, 'test_ConfigData_update_setting: unexpected number of settings on global'

    assert cd.get_setting('module_setup') is not None, 'test_ConfigData_update_setting: global setting not found'

# Generated at 2022-06-12 20:54:44.324140
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.cli.arguments import PluginOptions
    from ansible.config.setting import Setting

    config_data = ConfigData()

    p = PluginOptions('connection', 'ssh')

    setting = Setting('ansible_user', 'root')

    config_data.update_setting(setting)

    assert config_data.get_setting('ansible_user') == setting
    assert config_data.get_setting('ansible_user', p) is None

    config_data.update_setting(setting, p)

    assert config_data.get_setting('ansible_user') == setting
    assert config_data.get_setting('ansible_user', p) == setting


# Generated at 2022-06-12 20:54:52.439752
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.module_utils.ansible_release import __version__ as release_version
    from ansible.module_utils.basic import AnsibleModule

    from ansible_collections.ansible.community.plugins.module_utils.config import Setting

    # Create an Ansible module for testing
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # Create a new config data
    config_data = ConfigData()

    # Add three settings: one global, two local
    assert config_data.get_setting('length') is None
    length_setting = Setting('length', 'abc=def', 'abc=def', release_version)
    config_data.update_setting(length_setting)
    assert config_data.get_setting(length_setting.name) == length_

# Generated at 2022-06-12 20:55:00.228848
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import pytest
    from ansible.plugins.loader import config as config_loader
    from ansible.module_utils.common.collections import ImmutableDict

    config_data = ConfigData()
    config_data.update_setting(
        config_loader.Setting(
            "ANSIBLE_KEEP_REMOTE_FILES", "False", "default", "bool",
            "keep remote files on the server after the execution of a playbook or module",
            "env", "True", "False", [], ["ANSIBLE_REMOTE_FILES"]
        )
    )

# Generated at 2022-06-12 20:55:07.666906
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = ConfigSetting('setting_foo', 'bar')
    plugin = ConfigPlugin('module', 'net_ping')
    config_data.update_setting(setting)
    assert config_data.get_setting('setting_foo') == setting
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('setting_foo', plugin) == setting



# Generated at 2022-06-12 20:55:16.480012
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting("string") == None
    assert config.get_setting("string", "some_plugin") == None
    assert config.get_setting("string", "some_plugin_type.some_plugin_name") == None

    config.update_setting("string")
    assert config.get_setting("string") == "string"
    assert config.get_setting("string", "some_plugin") == None
    assert config.get_setting("string", "some_plugin_type.some_plugin_name") == None

    assert config.get_setting("string", "some_plugin_type.some_plugin_name") == None
    assert config.get_setting("string", "some_plugin_type.some_plugin_name") == None


# Generated at 2022-06-12 20:55:17.757073
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass

# Generated at 2022-06-12 20:55:22.109756
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    def function(self, a, b):
        return a + b

    data = ConfigData()

    assert data.get_setting("nonexisting") is None
    assert data.get_setting("nonexisting", "plugin") is None

    data.update_setting(PluginSetting("existing", "value", "type", "name", None, "description"))
    assert data.get_setting("existing").value == "value"
    data.update_setting(PluginSetting("existing", "value2", "type", "name", None, "description"))
    assert data.get_setting("existing").value == "value2"

    data.update_setting(PluginSetting("existing_plugin", "value", "type", "name", None, "description"))
    assert data.get_setting("existing_plugin", "plugin").value == "value"

    data.update

# Generated at 2022-06-12 20:55:27.477732
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config = ConfigData()

    # Test with no plugin
    settings = config.get_settings()
    assert len(settings) == 0

    # Test with plugin
    from ansibledocgen.objects.plugin import Plugin
    plugin = Plugin("test", "action")
    settings = config.get_settings(plugin)
    assert len(settings) == 0


# Generated at 2022-06-12 20:55:31.195440
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('module_setup', 'sample') == None


# Generated at 2022-06-12 20:55:33.679694
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings()==[]
    assert config_data.get_settings().__class__ is list

# Generated at 2022-06-12 20:55:41.096339
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    test_data = ConfigData()
    test_data.update_setting(Setting('setting1', 'value1'))
    test_data.update_setting(Setting('setting1', 'value2'), Plugin('plugin1', 'plugin_type'))
    test_data.update_setting(Setting('setting2', 'value3'), Plugin('plugin2', 'plugin_type'))

    # Test for global setting
    assert(test_data.get_setting('setting1') == Setting('setting1', 'value1'))

    # Test for plugin setting
    assert(test_data.get_setting('setting1', Plugin('plugin1', 'plugin_type')) == Setting('setting1', 'value2'))

# Generated at 2022-06-12 20:55:50.210774
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    setting_a = Setting('name', 'value')
    config_data.update_setting(setting_a)
    assert config_data.get_setting('name') == setting_a

    setting_b = Setting('name', 'value')
    plugin = Plugin('type1', 'name1')
    config_data.update_setting(setting_b, plugin)
    assert config_data.get_setting('name', plugin) == setting_b

    assert config_data.get_setting('name', Plugin('type1', 'name2')) is None
    assert config_data.get_setting('unknown') is None
    assert config_data.get_setting('unknown', plugin) is None



# Generated at 2022-06-12 20:55:50.821038
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
        config = ConfigData()
        print(config.get_settings())

# Generated at 2022-06-12 20:55:56.800574
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    data = ConfigData()
    assert data.get_setting('any', Plugin('any')) == None
    assert data.get_setting('any', None) == None
    data.update_setting(DataSetting('any'), None)
    assert data.get_setting('any', Plugin('any')) == None
    assert data.get_setting('any', None) != None
    assert data.get_setting('any', Plugin('any2')) == None


# Generated at 2022-06-12 20:56:06.611717
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from collections import namedtuple
    from types import ModuleType

    from ansible.executor.module_common import load_module_util

    plugin = namedtuple('plugin', 'name, type')('module_name', 'module')

    config_data = ConfigData()
    config_data.update_setting(Setting(name='setting_name_1'))
    config_data.update_setting(Setting(name='setting_name_2'))
    config_data.update_setting(Setting(name='setting_name_1'), plugin=plugin)
    config_data.update_setting(Setting(name='setting_name_2'), plugin=plugin)

    assert len(config_data.get_settings()) == 2

# Generated at 2022-06-12 20:56:18.667943
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Set up the objects to be used as parameters
    class TestPlugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    test_config_data = ConfigData()
    test_config_data.update_setting(ConfigSetting('one', 'foo'))
    test_config_data.update_setting(ConfigSetting('two', 'bar'), TestPlugin('plugin_type', 'plugin_name'))

    # Test case for when "plugin" parameter is None
    test_settings = test_config_data.get_settings()
    assert test_settings[0].name == 'one'

    # Test case for when "plugin" parameter is not None
    test_settings = test_config_data.get_settings(TestPlugin('plugin_type', 'plugin_name'))
   

# Generated at 2022-06-12 20:56:30.033870
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
  from ansible.module_utils.plugin import Plugin

  plugin_name = "test_plugin"
  plugin_type = "test_type"
  test_plugin = Plugin(plugin_name, plugin_type)

  config_data = ConfigData()
  test_setting = Setting("test_setting", "mytest_setting", priority=1)

  config_data.update_setting(test_setting, None)
  config_data.update_setting(test_setting, test_plugin)

  assert config_data.get_setting("test_setting", None) == test_setting
  assert config_data.get_setting("test_setting", test_plugin) == test_setting
  assert len(config_data.get_settings(None)) == 1
  assert len(config_data.get_settings(test_plugin)) == 1

# Generated at 2022-06-12 20:56:39.800917
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Arrange
    config_data = ConfigData()
    plugin = Plugin(type='module_utils', name='win_partition')
    setting = Setting(name='blah', value='blah')

    # Act
    config_data.update_setting(setting, plugin)

    # Assert
    assert config_data._global_settings.get(setting.name) is None
    assert config_data._plugins['module_utils'].get('win_partition').get(setting.name) is not None
    assert isinstance(config_data._plugins['module_utils'].get('win_partition').get(setting.name), Setting)



# Generated at 2022-06-12 20:56:43.644190
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    configdata = ConfigData() 
    configdata.update_setting(Setting('host_key_checking', 'yes'))
    configdata.update_setting(Setting('ansible_ask_pass', 'True'))

    assert configdata.get_setting('host_key_checking').value == 'yes'
    assert configdata.get_setting('ansible_ask_pass').value == 'True'


# Generated at 2022-06-12 20:56:53.966053
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansiblelint.rules.lineinfile import LineExistsSpecifyFullPath
    from ansiblelint.rules.lineinfile import LineExists
    from ansiblelint.rules.lineinfile import LineShouldMatch
    from ansiblelint.rules.lineinfile import LineShouldContain
    from ansiblelint.rules.lineinfile import LineShouldNotMatch
    from ansiblelint.rules.lineinfile import LineShouldNotContain
    from ansiblelint.rules.lineinfile import LineDeleted
    from ansiblelint.rules.lineinfile import LineAdded
    from ansiblelint.rules.lineinfile import LineHasVars
    from ansiblelint.rules.lineinfile import LineHasNoVars
    from ansiblelint.rules.lineinfile import LineHasNestedVars

# Generated at 2022-06-12 20:57:01.845724
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansiblelint.rules import RulesCollection

    config_data = ConfigData()
    plugins = RulesCollection()
    config_data.update_setting(setting=Setting(setting_name="test_setting_global", value=True), plugin=None)
    config_data.update_setting(setting=Setting(setting_name="test_setting_plugin", value=True), plugin=plugins.get_plugin(type="test_plugin1"))
    config_data.update_setting(setting=Setting(setting_name="test_setting_2_global", value=True), plugin=None)
    config_data.update_setting(setting=Setting(setting_name="test_setting_2_plugin", value=True), plugin=plugins.get_plugin(type="test_plugin1"))

    assert(len(config_data.get_settings()) == 2)


# Generated at 2022-06-12 20:57:09.235144
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Create object of class ConfigData and update a setting
    config_data = ConfigData()
    setting = dict(name="test_setting_name", plugin_type="test_setting_plugin_type", plugin_name="test_setting_plugin_name", value="test_setting_value")
    config_data.update_setting(setting)

    # Assert method update_setting updates data correctly
    assert config_data._global_settings.get("test_setting_name") is None
    assert config_data._plugins["test_setting_plugin_type"]["test_setting_plugin_name"]["test_setting_name"] == setting


# Generated at 2022-06-12 20:57:11.988958
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()
    plugin = 'Collection'
    name = 'foo'

    configdata.update_setting(ConfigSetting(name=name, plugin=plugin))
    assert configdata._plugins[plugin][plugin][name].name == name

# Generated at 2022-06-12 20:57:15.395783
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # setup
    configData = ConfigData()
    setting = Setting("a", "b", plugin="c")
    assert len(configData.get_settings()) == 0

    # execute
    configData.update_setting(setting)
    assert len(configData.get_settings()) == 1

    # teardown
    assert True


# Generated at 2022-06-12 20:57:17.758815
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    setting = {'name': 'setting_name', 'group':'setting_group', 'value': 'setting_value'}
    config_data.update_setting(setting)
    settings = config_data.get_settings()
    assert (len(settings) == 1)


# Generated at 2022-06-12 20:57:29.934129
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    class PluginType(object):
        def __init__(self, type):
            self.type = type

    class Plugin(object):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    class Setting(object):
        def __init__(self, name, value, private, plugin=None):
            self.name = name
            self.plugin_type = plugin.type if plugin else None
            self.plugin_name = plugin.name if plugin else None
            self.value = value
            self.private = private

        def __str__(self):
            return '%s(%s)' % (self.name, self.value)

    # Create a type for the config setting
    config_setting_type = PluginType('setting')

    # Create the config data
    config_

# Generated at 2022-06-12 20:57:33.356425
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    assert config_data.get_setting('setting1') is None
    assert config_data.get_setting('setting1', plugin=object) is None
    assert config_data.get_setting('setting2', plugin=object) is None


# Generated at 2022-06-12 20:57:34.929135
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting('test') is None


# Generated at 2022-06-12 20:57:39.934480
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()

    assert config.get_setting('foo', 'bar') is None

    from ansible.utils.plugin_docs import get_docstring
    from ansible.plugins import AnsiblePlugin, action_loader
    method = get_docstring(action_loader.get('ping'))
    plugin = AnsiblePlugin(method)

    setting = Setting(name='foo', plugin=plugin)
    config.update_setting(setting)

    assert config.get_setting('foo') == setting
    assert config.get_setting('foo', plugin) == setting


# Generated at 2022-06-12 20:57:44.955009
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting('1', '1')
    assert config_data._global_settings == '1'
    config_data.update_setting('1', '2')
    assert config_data._plugins == {'1': {'1': '1', '2': '1'}}


# Generated at 2022-06-12 20:57:58.818809
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin = Plugin(name='plugin', type='type1')
    setting1 = Setting(name='name1', desc='desc1', value='val1')
    config_data.update_setting(setting1, None)

    assert config_data.get_setting('name1') == setting1
    assert config_data.get_setting('name1', plugin) == None

    setting2 = Setting(name='name2', desc='desc2', value='val2')
    config_data.update_setting(setting2, plugin)

    assert config_data.get_setting('name1') == setting1
    assert config_data.get_setting('name1', plugin) == None
    assert config_data.get_setting('name2', plugin) == setting2



# Generated at 2022-06-12 20:58:00.976630
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:58:08.694715
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()
    config.update_setting()

# Generated at 2022-06-12 20:58:14.987459
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    config_data.update_setting(Setting(name=u'a', value=1, origin=u'foo', filename=u'bar'))
    assert config_data.get_setting(name=u'a').value == 1

    config_data.update_setting(Setting(name=u'b', value=2, origin=u'bar', filename=u'foo'))
    assert config_data.get_setting(name=u'b').value == 2



# Generated at 2022-06-12 20:58:18.821286
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    setting = ConfigData.ConfigurationSetting()
    setting.name = 'foo'
    setting.value = 'bar'
    config_data.update_setting(setting)

    assert len(config_data.get_settings()) == 1
    assert config_data.get_settings()[0].value == 'bar'


# Generated at 2022-06-12 20:58:27.714010
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_setting = ConfigSetting('value.1')
    config_data.update_setting(test_setting)
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0] == test_setting

    test_plugin = Plugin('test_plugin', PluginType.MODULE)
    test_setting = ConfigSetting('value.2')
    config_data.update_setting(test_setting, test_plugin)
    settings = config_data.get_settings(test_plugin)
    assert len(settings) == 1
    assert settings[0] == test_setting


# Generated at 2022-06-12 20:58:32.894123
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()
    assert not configData.get_settings()
    #
    configData.update_setting(Setting('a', 'b', 'c', 'd'))
    assert len(configData.get_settings()) == 1
    assert configData.get_settings()[0].name == 'a'


# Generated at 2022-06-12 20:58:37.045509
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting = Setting('test_setting', 'int', 3, 'test_setting', '', 'This is test setting for unit test')
    cd.update_setting(setting)
    assert cd._global_settings['test_setting'].value == 3


# Generated at 2022-06-12 20:58:44.586434
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    print("Unit test for method get_setting of class ConfigData")

    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.loader import find_plugin
    from ansible.config.base import BaseConfig
    from ansible.config.settings import Setting

    plugin = find_plugin(PluginLoader(), 'connection', 'local')
    plugin_config_settings = filter(lambda x: x.__class__.__name__ == 'Setting',
                                    plugin.__class__.__init__.__func__.__annotations__.values())

    host_config_setting = Setting('host', 'localhost', 'string')
    config_data.update_setting(host_config_setting)

    print("\nTesting when plugin is None")
    setting = config_data.get_setting('host')

# Generated at 2022-06-12 20:58:50.393735
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    configData = ConfigData()
    setting1 = ConfigSetting(name='setting1', value='value1')

    configData.update_setting(setting1)
    configData.update_setting(setting1, plugin=ConfigPlugin('type5', 'name1'))
    configData.update_setting(setting1, plugin=ConfigPlugin('type5', 'name2'))

    assert len(configData._global_settings) == 1
    assert len(configData._plugins) == 1
    assert setting1.name in configData._global_settings
    assert setting1.name in configData._plugins['type5']['name1']
    assert setting1.name in configData._plugins['type5']['name2']
    assert configData.get_setting('setting1') == setting1

# Generated at 2022-06-12 20:59:10.146320
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin_type = 'aws'
    plugin_name = 'test'
    setting_name = 'name'
    setting_value = 'value'
    setting_new_value = 'value_new'
    plugin = Plugin(plugin_type, plugin_name)
    setting = Setting(setting_name, setting_value)
    setting_new = Setting(setting_name, setting_new_value)

    # get_setting return None when the setting is not in global settings and plugins
    assert config_data.get_setting(setting_name) is None
    # get_setting return None when plugin is not in plugins
    assert config_data.get_setting(setting_name, plugin) is None

    # get_setting return None when the setting is in global settings but not in plugins
    config_data.update_setting

# Generated at 2022-06-12 20:59:18.580788
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from UnitTests.test_ansible_collections_mocking.plugins.module_utils.ansible_test_collection import AnsibleTestCollection

    ansible_test_collection = AnsibleTestCollection()
    config_data = ConfigData()

    # Test update_setting with a global setting
    setting = ansible_test_collection.get_setting_by_name('test_setting_0')
    config_data.update_setting(setting)
    setting = config_data.get_setting('test_setting_0')
    assert setting.name == 'test_setting_0'
    assert setting.value == 'setting_0'

    # Test update_setting with a plugin setting
    setting = ansible_test_collection.get_setting_by_name('test_setting_1')
    plugin = ansible_test_collection.get_plugin

# Generated at 2022-06-12 20:59:28.694945
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    print('Testing ConfigData method get_setting\n')

    import sys
    sys.path.append('./test/units')

    from ansible.plugins import module_loader, PluginLoader

    loader = PluginLoader('module_utils', 'ansible.module_utils', C.DEFAULT_MODULE_UTILS_PATH, 'module_utils')
    for i in loader.all(class_only=True):
        module_loader.add_directory(i._original_path)

    from TestSetting import TestSetting

    config_data_obj = ConfigData()

    test_setting = TestSetting('ansible', 'doc_fragments', 'test_key', 'test_value', '/etc/ansible/ansible.cfg')
    config_data_obj.update_setting(test_setting)


# Generated at 2022-06-12 20:59:37.392121
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(Setting('setting', 'value'))
    # Test with plugin argument None
    assert config_data.get_settings()[0].name == 'setting'
    assert config_data.get_settings()[0].value == 'value'
    # Test with a valid plugin argument
    plugin = Plugin(Plugin.CORE, 'test')
    config_data.update_setting(Setting('test_setting', 'test_value'), plugin)
    assert config_data.get_settings(plugin)[0].name == 'test_setting'
    assert config_data.get_settings(plugin)[0].value == 'test_value'
    # Test with a invalid plugin argument
    plugin = Plugin(Plugin.CORE, 'invalid')
    assert config_data.get_settings(plugin)

# Generated at 2022-06-12 20:59:48.495391
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    import os
    import sys
    here = os.path.abspath(os.path.dirname(__file__))
    module_path = os.path.join(here, '../../plugins/')
    sys.path.append(module_path)

    path = os.path.join(here, '../../plugins/module_utils/')
    sys.path.append(path)

    import module_utils.urls as urls

    from ansible_collections.notmintest.not_a_real_collection.plugins.cliconf.iosxr import Cliconf

    from ansible.module_utils.connection import Connection

    from ansible.module_utils.network.common.utils import load_provider

    from ansible.module_utils.network.iosxr.providers.cliconf import Clic

# Generated at 2022-06-12 20:59:59.884433
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible_collections.ansible.community.plugins.module_utils.common.config_data import Setting, Plugin

    config_data = ConfigData()

    s1 = Setting('global1', 'global1')
    config_data.update_setting(s1)
    assert config_data.get_setting('global1') == s1

    p1_1 = Plugin('core', 'lookup', 'file')
    s1_1 = Setting('global1', 'p1_1')
    config_data.update_setting(s1_1, p1_1)
    assert config_data.get_setting('global1') == s1
    assert config_data.get_setting('global1', p1_1) == s1_1

    p1_2 = Plugin('core', 'lookup', 'file')
    s

# Generated at 2022-06-12 21:00:07.719997
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_config = ConfigData()
    plugin_type = 'lookup'
    plugin_name = 'file'
    setting_1 = Setting('var_name', 'var_value')
    test_config.update_setting(setting_1)
    test_config.update_setting(setting_1, Plugin(plugin_type, plugin_name))

    assert len(test_config.get_settings()) == 1
    assert len(test_config.get_settings(Plugin(plugin_type, plugin_name))) == 1

# Generated at 2022-06-12 21:00:10.496532
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    plugin = ConfigPlugin("filter", "test", None, None)

    assert len(config.get_settings(plugin)) == 0

    setting = ConfigSetting("test", None, "test", None, None, None, plugin)
    config.update_setting(setting, plugin)
    assert len(config.get_settings(plugin)) == 1
    assert config.get_setting("test", plugin) == setting

# Generated at 2022-06-12 21:00:13.657305
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting('setting', 'plugin')
    config_data.update_setting('setting', 'plugin')
    config_data.update_setting('setting', 'plugin')

if __name__ == '__main__':
    test_ConfigData_update_setting()

# Generated at 2022-06-12 21:00:19.108256
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data._global_settings = {'setting1':'setting1', 'setting2':'setting2'}
    assert len(config_data.get_settings()) == 2
    config_data._plugins = {'type1':{
                                'name1':{'setting3':'setting3'},
                                'name2':{'setting4':'setting4'}
                                },
                            'type2':{
                                'name1':{'setting5':'setting5', 'setting6':'setting6'}
                                }
                            }
    assert len(config_data.get_settings(None)) == 2
    assert len(config_data.get_settings('type1','name1')) == 1

# Generated at 2022-06-12 21:00:43.962238
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = PluginConfig('Dummy', 'dummy', 'core')
    setting = SettingConfig('ansible', False, False, 'core')
    config_data.update_setting(setting, plugin)
    setting = SettingConfig('ansible', False, False)
    config_data.update_setting(setting)
    assert config_data.get_setting('ansible', plugin) is not None
    assert config_data.get_setting('ansible') is not None
    assert config_data.get_setting('ansible', PluginConfig('NotDummy', 'not_dummy', 'core')) is None
    assert config_data.get_setting('unknown') is None


# Generated at 2022-06-12 21:00:51.891440
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    # test with global setting
    setting = Setting("http_port", 9981, "http port to listen on")
    config_data.update_setting(setting)

    assert config_data.get_setting("http_port") == setting

    # test with plugin setting
    setting = Setting("http_port", 9981, "http port to listen on")
    plugin = Plugin("my_plugin", "my_type")
    config_data.update_setting(setting, plugin)

    assert config_data.get_setting("http_port", plugin) == setting


if __name__ == '__main__':
    test_ConfigData_update_setting()

# Generated at 2022-06-12 21:01:03.421778
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    test_data1 = ConfigData()

    plugin = Plugin(type='filter', name='inject')
    setting = Setting('role_name')
    setting.value = 'foo'
    test_data1.update_setting(setting, plugin)

    plugin = Plugin(type='filter', name='subset')
    test_data1.update_setting(setting, plugin)

    plugin = Plugin(type='filter', name='subset')
    setting = Setting('role_name')
    setting.value = 'bar'
    test_data1.update_setting(setting, plugin)

    assert(len(test_data1.get_settings()) == 0)

    assert(len(test_data1.get_settings(plugin)) == 1)
    plugin.name = 'subset'

# Generated at 2022-06-12 21:01:13.549318
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(value="INI", name="INI_NAME"))
    config_data.update_setting(
        Setting(value="YAML", name="YAML_NAME"),
        Plugin("MODULE", "MODULE")
    )
    config_data.update_setting(
        Setting(value="JSON", name="JSON_NAME"),
        Plugin("MODULE", "MODULE")
    )

    # Test for global config setting
    ini_setting = config_data.get_setting(name="INI_NAME")
    assert ini_setting.type == "INI"
    assert ini_setting.name == "INI_NAME"
    assert ini_setting.value == "INI"
    assert ini_setting.plugin is None

   

# Generated at 2022-06-12 21:01:16.408291
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_object = ConfigData()
    # get_settings with an empty configuration
    settings = test_object.get_settings()
    assert len(settings) == 0


# Generated at 2022-06-12 21:01:23.464310
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    from ansible.plugins.loader import Plugin
    from ansible.config.manager import Setting
    plugin = Plugin('test', '', ['test1'])
    setting = Setting('test1', '', plugin)
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('test1', plugin).name == 'test1'
    assert not config_data.get_setting('test2', plugin)
    assert not config_data.get_setting('test1')


# Generated at 2022-06-12 21:01:28.395639
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = config_data.get_setting(name = 'force_color')
    settings = config_data.get_settings()
    # It is expected that the settings is an empty list
    assert settings is []


# Generated at 2022-06-12 21:01:34.501892
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    configData = ConfigData()
    if configData.get_setting("callback_whitelist") == None:
        assert 1 == 0
    if configData.get_settings() == None:
        assert 1 == 0
    if configData.get_setting("lookup", Plugin("lookup","lookup_plugins")) == None:
        assert 1 == 0
    if configData.get_settings(Plugin("lookup","lookup_plugins")) == None:
        assert 1 == 0

# Test object for ConfigData

# Generated at 2022-06-12 21:01:41.622599
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    config_setting = ConfigSetting('setting_name', 'setting_value')
    config_data.update_setting(config_setting)

    config_setting = ConfigSetting('setting_name', 'setting_value')
    config_data.update_setting(config_setting)

    retrieved_config_setting = config_data.get_setting('setting_name')
    assert retrieved_config_setting.value == 'setting_value'

    retrieved_config_setting = config_data.get_setting('setting_name', 'plugin_module')
    assert retrieved_config_setting is None

# Generated at 2022-06-12 21:01:42.913690
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting(Setting())


# Generated at 2022-06-12 21:02:02.531527
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    confdata = ConfigData()
    confdata.update_setting(Setting(name="a", value="b"))

    assert confdata.get_setting("a") != None
    assert confdata.get_setting("b") == None


# Generated at 2022-06-12 21:02:13.641743
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_settings = {'display_skipped_hosts': 'no', 'force_handlers': 'no', 'display_ok_hosts': 'yes'}
    plugins = {'callback': {'json':{'json_indent': '5'}}, 'cache': {'jsonfile': {'max_cache_size': '100'}}}
    data = ConfigData()
    for k in global_settings:
        setting = {'name': k, 'value': global_settings[k]}
        data.update_setting(setting)
    for t in plugins:
        for p in plugins[t]:
            for k in plugins[t][p]:
                setting = {'name': k, 'value': plugins[t][p][k]}
                plugin = {'type': t, 'name': p}

# Generated at 2022-06-12 21:02:16.318592
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert len(settings) == 0


# Generated at 2022-06-12 21:02:23.240400
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    import os
    file_path = os.path.abspath('test')
    setting1 = Setting(name='setting', plugin=Plugin(name='testing', type='callback', path=file_path))
    config_data.update_setting(setting1)
    setting2 = Setting(name='setting', plugin=Plugin(name='testing', type='callback', path=file_path))
    config_data.update_setting(setting2)
    assert setting1 == setting2
    
    

# Generated at 2022-06-12 21:02:27.481828
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []
    config_data._global_settings['test'] = 'test'
    config_data._global_settings['test2'] = 'test2'
    assert len(config_data.get_settings()) == 2


# Generated at 2022-06-12 21:02:30.287794
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    assert data.get_setting("FOO").value is None
    data.update_setting(ConfigSetting("FOO", "bar"))
    assert data.get_setting("FOO").value == "bar"

# Generated at 2022-06-12 21:02:41.385647
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting = Setting('setting1', 'value1', 'comment1')
    cd.update_setting(setting)
    if cd.get_setting('setting1') != setting:
        raise AssertionError('Object returned by ConfigData.get_setting is not equal to the' +
                             'object added using ConfigData.update_setting')
    plugin = Plugin('plugin1', 'plugin_type1')
    setting = Setting('setting1', 'value1', 'comment1')
    cd.update_setting(setting, plugin)
    if cd.get_setting('setting1', plugin) != setting:
        raise AssertionError('Object returned by ConfigData.get_setting is not equal to the' +
                             'object added using ConfigData.update_setting')


# Generated at 2022-06-12 21:02:42.677589
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting("") is None


# Generated at 2022-06-12 21:02:53.645065
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.module_utils.ansible_release import __version__
    from collections import namedtuple

    Plugin = namedtuple('Plugin', ['name', 'type'])
    Setting = namedtuple('Setting', ['name', 'value'])

    config = ConfigData()

    setting = Setting(name='lookup_plugin', value='foo')
    config.update_setting(setting)

    assert config.get_setting('lookup_plugin') == setting

    plugin = Plugin(name='foo', type='lookup')
    setting = Setting(name='cwd', value=__version__)
    config.update_setting(setting, plugin)

    assert config.get_setting('cwd', plugin) == setting

    setting = Setting(name='cwd', value='somethingelse')
    config.update_setting(setting)

    assert config

# Generated at 2022-06-12 21:03:02.644112
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    plugin = Plugin('type', 'name')
    setting = Setting('parameter1')

    assert None is config_data.get_setting(setting.name)
    assert None is config_data.get_setting(setting.name, plugin)

    config_data.update_setting(setting)
    config_data.update_setting(setting, plugin)

    setting = config_data.get_setting(setting.name)
    assert setting.name == 'parameter1'
    setting = config_data.get_setting(setting.name, plugin)
    assert setting.name == 'parameter1'
