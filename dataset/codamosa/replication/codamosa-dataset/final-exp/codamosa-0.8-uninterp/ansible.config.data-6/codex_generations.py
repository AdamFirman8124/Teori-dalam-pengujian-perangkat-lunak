

# Generated at 2022-06-12 20:53:31.135449
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    setting1 = dict(name="setting1", value="value1")

# Generated at 2022-06-12 20:53:32.435076
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    pass


# Generated at 2022-06-12 20:53:33.419463
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()


# Generated at 2022-06-12 20:53:34.099980
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    pass

# Generated at 2022-06-12 20:53:37.531585
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting(None) is None
    assert config_data.get_setting('test') is None

test_ConfigData_get_setting()


# Generated at 2022-06-12 20:53:47.359892
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()
    data.update_setting(Setting('log_level', 'INFO'))
    data.update_setting(Setting('log_path', '/var/log/ansible.log'))
    assert len(data.get_settings())==2

    # Update global setting
    data.update_setting(Setting('log_path', '/var/log/ansible2.log'))
    assert len(data.get_settings())==2
    assert data.get_setting('log_path').value=='/var/log/ansible2.log'

    data.update_setting(Setting('log_level', 'DEBUG', Plugin('test', 'callback')))
    assert len(data.get_settings())==2
    assert len(data.get_settings(Plugin('test', 'callback')))==1

    data.update_setting

# Generated at 2022-06-12 20:53:56.787198
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import os
    import sys
    import unittest

    from ansible.config.plugin import PluginConfig

    # Initialize a ConfigData object
    config_data = ConfigData()

    # Initialize a PluginConfig object and update it to ConfigData object
    plugin_config_1 = PluginConfig('module_name', 'module')
    config_data.update_setting(plugin_config_1)

    # Initialize a PluginConfig object and update it to ConfigData object
    plugin_config_2 = PluginConfig('cli_name', 'cli')
    config_data.update_setting(plugin_config_2)

    # Initialize a PluginConfig object and update it to ConfigData object
    plugin_config_3 = PluginConfig('connection_name', 'connection')
    config_data.update_setting(plugin_config_3)

    # Check whether the

# Generated at 2022-06-12 20:54:08.807786
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.config.setting import SettingDefinition
    from ansible.utils.plugin_docs import get_docstring

    # create a global setting and a plugin setting
    global_setting = SettingDefinition("TEST_GLOBAL_SETTING", get_docstring(SettingDefinition.__init__), "TEST_GLOBAL_SETTING_DEFAULT_VALUE")
    plugin_setting = SettingDefinition("TEST_PLUGIN_SETTING", get_docstring(SettingDefinition.__init__), "TEST_PLUGIN_SETTING_DEFAULT_VALUE")

    data = ConfigData()

    # test empty settings list
    settings = data.get_settings()
    assert settings == []

    # update the global setting and test
    data.update_setting(global_setting)
    settings = data.get_settings()

# Generated at 2022-06-12 20:54:19.429796
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    from collections import namedtuple
    from ansible.compat.tests import unittest

    Setting = namedtuple("Setting", ["name"])
    Plugin = namedtuple("Plugin", ["name", "type"])

    global_setting = Setting("global_setting")
    plugin_setting = Setting("plugin_setting")
    plugin = Plugin("name", "type")

    config_data.update_setting(global_setting)
    config_data.update_setting(plugin_setting, plugin)

    assert global_setting in config_data.get_settings()
    assert plugin_setting in config_data.get_settings(plugin)



# Generated at 2022-06-12 20:54:21.162045
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:54:33.652470
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    setting_1 = type('Setting', (), {})
    setting_1.name = 'foo'

    # Update global setting
    config_data.update_setting(setting_1)
    assert config_data._global_settings['foo'] == setting_1

    setting_2 = type('Setting', (), {})
    setting_2.name = 'bar'
    plugin = type('Plugin', (), {})
    plugin.name = 'myplugin'
    plugin.type = 'mytype'

    # Update non-existing plugin setting
    config_data.update_setting(setting_2, plugin)
    assert config_data._plugins['mytype']['myplugin']['bar'] == setting_2


# Generated at 2022-06-12 20:54:35.217602
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:54:40.578302
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Instantiating class ConfigData
    config_data = ConfigData()
    # Setting up class ConfigData
    config_data.update_setting('test_setting', 'test_plugin')
    # Checking if test_setting was properly updated
    assert config_data.get_setting('test_setting') == 'test_setting', "test_setting was not properly updated"


# Generated at 2022-06-12 20:54:50.678011
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    cd = ConfigData()
    cd.update_setting(GlobalSetting('test1', 'testvalue1', 'testcomment1'))
    cd.update_setting(GlobalSetting('test2', 'testvalue2', 'testcomment2'))
    cd.update_setting(PluginSetting('test3', 'testvalue3', 'testcomment3'),
                      PluginDefinition('connection', 'paramiko', PluginDefinition.PLUGIN_TYPE_CONNECTION))
    cd.update_setting(PluginSetting('test4', 'testvalue4', 'testcomment4'),
                      PluginDefinition('vars', 'include', PluginDefinition.PLUGIN_TYPE_VARS))
    cd.update_setting(PluginSetting('test5', 'testvalue5', 'testcomment5'),
                      PluginDefinition('lookup', 'template', PluginDefinition.PLUGIN_TYPE_LOOKUP))

# Generated at 2022-06-12 20:55:01.669473
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    global_config = ConfigData()

    # Create some attributes for a plugin
    import os

    class Plugin(object):

        def __init__(self, name, type):
            self.name = name
            self.type = type
            self.path = os.path.join('/var/lib', self.type, self.name)

    class Attribute(object):

        def __init__(self, name, value, default=None, prev=None, origin=None, plugin=None):
            self.name = name
            self.value = value
            self.default = default
            self.prev = prev
            self.origin = origin
            self.plugin = plugin

    test_plugin = Plugin('foo', 'bar')


# Generated at 2022-06-12 20:55:12.740184
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_config_data = ConfigData()
    test_setting = 'test_setting'
    test_setting2 = 'test_setting2'
    test_plugin = 'test_plugin'
    test_plugin_type = 'test_plugin_type'
    test_plugin_type2 = 'test_plugin_type2'
    test_setting_object = {'name': test_setting}
    test_setting2_object = {'name': test_setting2}
    test_plugin_object = {'type': test_plugin_type, 'name': test_plugin}

    assert test_config_data.get_settings() == []

    test_config_data.update_setting(test_setting_object)
    test_config_data.update_setting(test_setting2_object)
    test_config_data.update_setting

# Generated at 2022-06-12 20:55:24.271696
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(BoolSetting(name='something', path=['a', 'b']))
    assert config_data.get_setting(name='something').name == 'something'
    assert config_data.get_setting(name='something', plugin=Plugin(type='c', name='d')).name == 'something'

    config_data.update_setting(BoolSetting(name='something', path=['a', 'b']), plugin=Plugin(type='c', name='d'))
    config_data.update_setting(BoolSetting(name='something2', path=['a', 'b']), plugin=Plugin(type='c', name='d'))

# Generated at 2022-06-12 20:55:33.896548
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings() == []
    # Check with plugin
    plugin = PluginConfig('foo', 'bar', 'type')
    cd.update_setting(SettingConfig('bar', 'foobar'))
    cd.update_setting(SettingConfig('foo', 'barfoo'), plugin)
    assert len(cd.get_settings()) == 1
    assert cd.get_settings(plugin)[0].name == 'foo'
    assert len(cd.get_settings(plugin)) == 1
    assert cd.get_settings()[0].name == 'bar'


# Generated at 2022-06-12 20:55:44.518255
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    plugin_type = 'callback'
    plugin_name = 'test'
    setting_name = 'test_setting'

    config = ConfigData()

    assert len(config.get_settings()) == 0
    assert len(config.get_settings(plugin=None)) == 0
    assert len(config.get_settings(plugin=Plugin(plugin_type, plugin_name))) == 0

    config.update_setting(Setting(setting_name, 'test_val'))

    assert len(config.get_settings()) == 1
    assert len(config.get_settings(plugin=None)) == 1
    assert len(config.get_settings(plugin=Plugin(plugin_type, plugin_name))) == 0

    config.update_setting(Setting(setting_name, 'test_val'), Plugin(plugin_type, plugin_name))


# Generated at 2022-06-12 20:55:52.873365
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
  configdata = ConfigData()
  configdata.update_setting(Setting('min_ansible_version', '2.8.0', 'global'))
  configdata.update_setting(Setting('foo', 'bar', 'connection', 'local'))
  configdata.update_setting(Setting('bar', 'baz', 'connection', 'local'))
  configdata.update_setting(Setting('foo', 'baz', 'connection', 'paramiko_ssh'))

  # Get global setting
  global_setting = configdata.get_setting('min_ansible_version')
  assert(global_setting.name == 'min_ansible_version')
  assert(global_setting.value == '2.8.0')
  assert(global_setting.plugin is None)

  # Get multiple settings of the different types
  settings = configdata

# Generated at 2022-06-12 20:56:07.258648
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    new_config = ConfigData()
    new_config._global_settings = {'key': {'name': 'key', 'type': 'dict', 'default': {}} }
    new_config._plugins = {'action': {'ping': {'key': {'name': 'key', 'type': 'dict', 'default': {}} } } }
    assert new_config.get_setting('key', None) == {'name': 'key', 'type': 'dict', 'default': {}}
    assert new_config.get_setting('key', 'action.ping') == {'name': 'key', 'type': 'dict', 'default': {}}
    assert new_config.get_setting('key', None) == {'name': 'key', 'type': 'dict', 'default': {}}


# Generated at 2022-06-12 20:56:18.883527
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    configData = ConfigData()
    from .plugin import Plugin
    from .plugin_setting import PluginSetting
    plugin = Plugin("testPlugin", "testType", "testDescription")
    setting = PluginSetting("mySetting", "myValue")
    configData.update_setting(setting, plugin)
    setting = PluginSetting("mySetting2", "myValue2")
    configData.update_setting(setting, plugin)
    setting = PluginSetting("mySetting2", "myValue3")
    configData.update_setting(setting, plugin)
    setting = PluginSetting("mySetting2", "myValue4")
    configData.update_setting(setting)

    settings = configData.get_setting("mySetting")
    assert(settings.name == "mySetting")
    assert(settings.value == "myValue")
    settings = configData.get

# Generated at 2022-06-12 20:56:30.237353
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    class Setting(object):
        def __init__(self, name, origin):
            self.name = name
            self.origin = origin

    name = "ANSIBLE_STRATEGY"
    origin = "DEFAULT"
    setting = Setting(name, origin)
    config_data.update_setting(setting)
    assert config_data.get_setting(name) is not None

    class Plugin(object):
        def __init__(self, name, type):
            self.name = name
            self.type = type

    type = "strategy"
    name = "free"
    plugin = Plugin(name, type)
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting(name, plugin) is not None

# Generated at 2022-06-12 20:56:41.838847
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # First plugin's setting
    setting1 = parser.Setting(name='foo',
                              value='bar',
                              origin='file',
                              source='test.yml',
                              section='',
                              plugin=parser.Plugin(name='test_plugin', type='test_type'))

    # Second plugin's setting
    setting2 = parser.Setting(name='bar',
                              value='foo',
                              origin='file',
                              source='test.yml',
                              section='',
                              plugin=parser.Plugin(name='test_plugin2', type='test_type2'))

    # Global setting

# Generated at 2022-06-12 20:56:50.154368
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
	config_data = ConfigData()
	setting = ConfigSetting('LOG_PATH', '/var/log/ansible', 'The log path for ansible')
	config_data.update_setting(setting, None)
	assert config_data._global_settings['LOG_PATH'].value == '/var/log/ansible'
	assert config_data._global_settings['LOG_PATH'].description == 'The log path for ansible'
	assert config_data._global_settings['LOG_PATH'].name == 'LOG_PATH'


# Generated at 2022-06-12 20:56:53.806916
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    configData.update_setting(Setting('Value', ['All']))
    configData.update_setting(Setting('K', ['Foo', 'Bar']), Plugin('Foo', 'F'))

# Generated at 2022-06-12 20:56:59.551494
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    obj = ConfigData()
    obj.update_setting('param1')
    assert obj.get_setting('param1') == 'param1'
    assert obj.get_setting('param2') == None
     

# Generated at 2022-06-12 20:57:05.515872
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data.get_settings().__len__() == 0
    plugin = Plugin("ANSIBLE")
    setting = Setting("NAME", "ANSIBLE", "VALUE", "COMMENT")
    config_data.update_setting(setting, plugin)
    assert config_data.get_settings().__len__() == 1
    assert config_data.get_settings()[0].plugin_type == "ANSIBLE"
    assert config_data.get_settings()[0].value == "VALUE"


# Generated at 2022-06-12 20:57:11.293660
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
  config_data = ConfigData()
  config_data.update_setting(Setting('test_setting1', 'test_value1'))
  config_data.update_setting(Setting('test_setting2', 'test_value2'))
  settings = config_data.get_settings()
  assert len(settings) == 2
  assert settings[0].name == 'test_setting1'
  assert settings[0].value == 'test_value1'
  assert settings[1].name == 'test_setting2'
  assert settings[1].value == 'test_value2'


# Generated at 2022-06-12 20:57:22.345892
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """Unit test for method get_settings of class ConfigData"""
    config_data = ConfigData()

    from ansible.plugins import PluginLoader
    plugin_loader = PluginLoader('callback')

    from ansible.plugins.callback import CallbackBase
    plugin_base = CallbackBase()

    from ansible.config.setting import Setting
    setting1 = Setting('setting1', 'value1')
    setting2 = Setting('setting2', 'value2', origin=None, plugin=plugin_base)

    config_data.update_setting(setting1)
    config_data.update_setting(setting2)

    assert 2 == len(config_data.get_settings())
    assert 1 == len(config_data.get_settings(plugin_loader.get('default')))

# Generated at 2022-06-12 20:57:36.119378
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    cd = ConfigData()

    setting = 'test_setting'
    assert cd.get_setting(setting) is None

    cd.update_setting(setting)
    assert cd.get_setting(setting) == setting


# Generated at 2022-06-12 20:57:44.071410
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data_2 = ConfigData()

    class FakeSetting:
        def __init__(self, name_value, value, origin_value, scope_value, show_value, plugin_type_value, plugin_name_value):
            self.name = name_value
            self.value = value
            self.origin = origin_value
            self.scope = scope_value
            self.plugin_type = plugin_type_value
            self.plugin_name = plugin_name_value
            self.show = show_value

        def __repr__(self):
            return str(self.__dict__)

    config_data.update_setting(FakeSetting('test1', 'test1', 'test1', 'test1', True, 'test1', 'test1'), None)
    config_data

# Generated at 2022-06-12 20:57:49.394603
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_setting = Setting(name="test_setting", value="test", origin="test")
    config_data.update_setting(test_setting)
    setting = config_data.get_setting(test_setting.name)
    assert setting.name == test_setting.name
    assert setting.value == test_setting.value
    assert setting.origin == test_setting.origin

# Generated at 2022-06-12 20:57:59.480334
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_setting = GlobalSetting(
        name='ACTION_WARNINGS',
        value='always',
        section='defaults',
        config_file='ansible.cfg',
        line=2,
        source='file'
    )

    plugin = Plugin('callback', 'mail')
    setting = PluginSetting(
        name='to',
        value='someone@somewhere.com',
        section='notification',
        config_file='ansible.cfg',
        line=30,
        source='file',
        plugin=plugin
    )

    config = ConfigData()
    config.update_setting(global_setting)
    config.update_setting(setting)

    assert config.get_setting('ACTION_WARNINGS') == global_setting
    assert config.get_setting('to', plugin) == setting



# Generated at 2022-06-12 20:58:01.526336
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.get_settings()

# Generated at 2022-06-12 20:58:09.040910
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()

    config_data.update_setting(Setting('foo', 'bar'))
    assert config_data.get_setting('foo').value == 'bar'

    config_data.update_setting(Setting('foo', 'baz'))
    assert config_data.get_setting('foo').value == 'baz'

    plugin_1 = Plugin('foo', 'action')
    config_data.update_setting(Setting('foo', 'baz'), plugin_1)
    assert config_data.get_setting('foo').value == 'baz'
    assert config_data.get_setting('foo', plugin_1).value == 'baz'


# Generated at 2022-06-12 20:58:17.256232
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert config_data.get_setting('setting_name') is None
    config_data.update_setting(Setting('setting_name', 'value'))
    assert config_data.get_setting('setting_name').value == 'value'
    config_data.update_setting(Setting('setting_name', 'new_value'))
    assert config_data.get_setting('setting_name').value == 'new_value'
    assert config_data.get_setting('other_setting') is None
    config_data.update_setting(Setting('other_setting', 'value'))
    assert config_data.get_setting('other_setting').value == 'value'


# Generated at 2022-06-12 20:58:29.212492
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    import os
    from ansible.config.setting import Setting

    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    config_data.update_setting(Setting('DEFAULT_MODULE_LANG', 'en_us', 'string', '', path))
    config_data.update_setting(Setting('DEPRECATION_WARNINGS', 'False', 'boolean', '', path))

    config_data.update_setting(Setting('ANSIBLE_ROLES_PATH', '/etc/ansible/roles', 'string', '', path),
                               Setting.Plugin(Setting.Plugin.Type.CORE, 'roles_path'))

# Generated at 2022-06-12 20:58:40.061512
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin=PluginDefinition()

    # Test case: updating a non-existing setting
    config_data.update_setting(setting=create_setting_mock(), plugin=plugin)
    assert len(config_data._global_settings) == 0
    assert len(config_data._plugins) == 0

    # Test case: updating a global setting
    plugin=PluginDefinition()
    config_data.update_setting(setting=create_setting_mock(), plugin=plugin)
    assert len(config_data._global_settings) == 1
    assert len(config_data._plugins) == 0

    # Test case: updating a type-specific setting
    plugin=PluginDefinition(type='lookup')
    config_data.update_setting(setting=create_setting_mock(), plugin=plugin)

# Generated at 2022-06-12 20:58:43.116107
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    settings = config.get_settings()
    for setting in settings:
        assert setting is None


# Generated at 2022-06-12 20:59:07.683082
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting = {'name': 'test', 'value': True}
    cd.update_setting(setting, None)
    cd.update_setting(setting, {'name': 'test', 'type': 'test'})

if __name__ == '__main__':
    test_ConfigData_update_setting()


# Generated at 2022-06-12 20:59:11.140208
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
   q = ConfigData()
   p = q._global_settings
   p['abc'] = 1            
   assert q.get_setting('abc') == 1
   

# Generated at 2022-06-12 20:59:19.031455
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    c = ConfigData()
    c.update_setting({'name': 'test1','value':'testvalue1','default':'testvalue1'})
    c.update_setting({'name': 'test2','value':'testvalue2','default':'testvalue2'})
    c.update_setting({'name': 'test3','value':'testvalue3','default':'testvalue3'})
    c.update_setting({'name': 'test4','value':'testvalue4','default':'testvalue4'})

# Generated at 2022-06-12 20:59:23.664789
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    assert config_data.get_setting('name') == None
    assert config_data.get_setting('name', 'plugin') == None
    assert config_data.get_setting('name', 'plugin') == None
    assert config_data.get_setting(None, None) == None



# Generated at 2022-06-12 20:59:32.997840
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    class Settings(object):
        def __init__(self, name, value, type, units, category, version, env_var, redirected_stderr,
                     deprecated=False, removed=False, sources=None, priority=None,
                     component=None, subcategory=None):
            self.name = name
            self.type = type
            self.units = units
            self.value = value
            self.category = category
            self.version = version
            self.env_var = env_var
            self.redirected_stderr = redirected_stderr
            self.deprecated = deprecated
            self.removed = removed
            self.sources = sources
            self.priority = priority
            self.component = component
            self.subcategory = subcategory
            self.plugin = None

# Generated at 2022-06-12 20:59:34.483600
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []


# Generated at 2022-06-12 20:59:42.369382
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    cd = ConfigData()

    # unit test: no plugin info
    assert len(cd.get_settings()) == 0

    from ansible.plugins import PluginLoader
    from ansible.plugins.loader import find_plugin

    # unit test: non-existent type
    setting = find_plugin(PluginLoader.setting, 'Foo')

    cd.update_setting(setting)
    assert len(cd.get_settings(setting)) == 1
    assert cd.get_settings(setting)[0] == setting

    from ansible.plugins.loader import add_directory

    # unit test: non-existent plugin
    add_directory('./test/support/resources/setting_plugins/')
    setting = find_plugin(PluginLoader.setting, 'Baz', 'Foobar')

    cd.update_setting(setting)

# Generated at 2022-06-12 20:59:47.571981
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    test_setting = Setting("test", "This is only a test", default=True)
    config.update_setting(test_setting)
    setting = config.get_setting("test")
    assert setting.name == "test"
    assert setting.default == True


# Generated at 2022-06-12 20:59:48.413382
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # 'get_settings' is not implemented yet
    pass

# Generated at 2022-06-12 20:59:55.200348
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Given
    d = ConfigData()
    d.update_setting(Setting('test1', 'value1', 'test-plugin'))

    # When
    res = d.get_setting('test1', 'test-plugin')
    # Then
    assert res is not None
    assert res.name == 'test1'
    assert res.value == 'value1'


# Generated at 2022-06-12 21:00:38.764911
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    temp = ConfigData()
    assert temp.get_settings(plugin=None) == []

    import ansible.plugin
    plugin = ansible.plugin.PluginLoader('lookup')
    my_lookup = plugin.get('my_lookup')
    temp.update_setting(ConfigSetting('my_setting', my_lookup, '2', '3', '4', '5', '6'))
    assert temp.get_settings(plugin=None) == [temp.get_setting('my_setting')]


# Generated at 2022-06-12 21:00:42.176231
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    assert cd.get_settings() == []
    assert cd.get_settings() == cd.get_setting(None)
    assert cd.get_settings(None) == cd.get_setting(None)

# Generated at 2022-06-12 21:00:44.065244
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert config_data.get_settings() == []
    assert config_data.get_settings(None) == []


# Generated at 2022-06-12 21:00:52.944890
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import find_plugin_file
    from ansible.plugins import setting as st
    from ansible.plugins.loader import plugin_loader
    from ansible.plugins.settings.core import load_plugin_settings_from_file

    configData = ConfigData()

    # Loads all settings files found in plugins
    plugin_loader.add_directory(find_plugin_file('settings'))
    for p in plugin_loader.all_plugins:
        load_plugin_settings_from_file(p, configData)

    # Assert all settings from plugin core are loaded
    settings = configData.get_settings()
    assert len(settings) > 0
    assert all(isinstance(s, st.Setting) for s in settings)

    # Assert all settings from a specific plugin are loaded
    settings = configData.get

# Generated at 2022-06-12 21:00:57.230685
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()

    # Test get_setting w/o a plugin
    assert config.get_setting('test_setting') is None

    # Test get_setting w/ a plugin
    assert config.get_setting('test_setting', plugin=Plugin('test', 'test_type')) is None


# Generated at 2022-06-12 21:01:02.696660
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    setting = Setting('key', 'value')
    config_data.update_setting(setting)

    setting_1 = config_data.get_setting('key')
    assert setting_1.name == setting.name
    assert setting_1.value == setting.value


# Generated at 2022-06-12 21:01:11.737963
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import os
    import tempfile
    import shutil
    from ansible.config.manager import ConfigManager, ConfigManagerParser
    from ansible.config.data import ConfigData, Setting

    t_dir = tempfile.mkdtemp()

    config_file_path = os.path.join(t_dir, 'ansible.cfg')

    with open(config_file_path, 'w') as cfg:
        cfg.write('[defaults]\n')
        cfg.write('deprecation_warnings=False\n')
        cfg.write('\n[inventory]\n')
        cfg.write('enable_plugins=host_list, script, yaml\n')

    config_data = ConfigData()
    config_manager = ConfigManager(t_dir, config_file_path)
    config_

# Generated at 2022-06-12 21:01:14.127710
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    setting = SettingMock()
    configData.update_setting(setting)
    assert len(configData._global_settings) == 1


# Generated at 2022-06-12 21:01:16.159283
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting("plugin", "name")


# Generated at 2022-06-12 21:01:25.582540
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    setting1 = {"name": "a", "value": 1}
    setting2 = {"name": "b", "value": 2}
    setting3 = {"name": "c", "value": 3}
    setting4 = {"name": "a", "value": 4}
    plugin = {"type": "type1", "name": "name1"}

    # updating the global setting
    config.update_setting(setting1)
    assert config.get_setting("a") == setting1

    # updating a plugin setting
    assert config.get_setting("b") is None
    config.update_setting(setting2, plugin)
    assert config.get_setting("b", plugin) == setting2
    assert config.get_setting("b") is None

    # updating the global setting again

# Generated at 2022-06-12 21:02:44.835432
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from collections import namedtuple
    Plugin = namedtuple('Plugin', ['type', 'name'])
    plugin = Plugin(type='c', name='c')
    config_data.update_setting('a', plugin)
    config_data.update_setting('b', plugin)
    config_data.update_setting('c', plugin)
    config_data.update_setting('d')
    config_data.update_setting('e')
    config_data.update_setting('f')
    assert config_data.get_settings(plugin) == ['a', 'b', 'c']
    assert config_data.get_settings() == ['d', 'e', 'f']



# Generated at 2022-06-12 21:02:55.444190
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting1 = Setting(name='string_value', value='test_value')
    setting2 = Setting(name='int_value', value=1)
    setting3 = Setting(name='bool_value', value=True)
    config_data.update_setting(setting1)
    config_data.update_setting(setting2, plugin=Plugin('connection', 'network_cli'))
    config_data.update_setting(setting3, plugin=Plugin('shell', 'powershell'))
    assert config_data.get_settings() == [setting1]
    assert config_data.get_settings(plugin=Plugin('connection', 'network_cli')) == [setting2]
    assert config_data.get_settings(plugin=Plugin('shell', 'powershell')) == [setting3]

# Unit test

# Generated at 2022-06-12 21:03:06.690098
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    assert config_data.get_setting('force_handlers') == None
    assert config_data.get_setting('force_handlers', plugin = 'foo') == None
    assert config_data.get_setting('force_handlers', plugin = 'bar') == None
    assert config_data.get_setting('force_handlers', plugin = 'baz') == None

    setting = ConfigSetting()
    setting.name = 'force_handlers'
    setting.plugin = None
    setting.value = 'False'

    config_data.update_setting(setting)

    assert config_data.get_setting('force_handlers') == 'False'
    assert config_data.get_setting('force_handlers', plugin = 'foo') == None

# Generated at 2022-06-12 21:03:12.477288
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    # Get global settings
    assert config_data.get_settings() == []

    # Get setting for a specific plugin
    assert config_data.get_settings(plugin='plugin') == []

    # Get settings for specific plugin type
    assert config_data.get_settings(plugin_type='plugin_type') == []


# Generated at 2022-06-12 21:03:19.136950
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()

    class MockPlugin(object):
        pass

    plugin = MockPlugin()
    plugin.type = 'filter'
    plugin.name = 'test'

    class MockSetting(object):
        def __init__(self):
            self.name = 'test'
            self.value = 'test'

    setting = MockSetting()

    data.update_setting(setting, plugin)
    assert data._global_settings == {}
    assert data._plugins['filter']['test']['test'] == setting


# Generated at 2022-06-12 21:03:29.083703
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    test_data = ConfigData()
    plugin = Plugin('system', 'module')
    plugin1 = Plugin('network', 'module')
    setting1 = PluginSetting('action', 'test')
    setting2 = PluginSetting('action', 'test1')
    setting3 = PluginSetting('action', 'test1')

    test_data.update_setting(setting1, plugin)
    test_data.update_setting(setting2)
    test_data.update_setting(setting3, plugin1)

    settings = test_data.get_settings()
    assert len(settings) == 2
    assert settings[0].name == 'action'
    assert settings[1].name == 'action'
    assert settings[0].value == 'test'
    assert settings[1].value == 'test1'
