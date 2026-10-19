

# Generated at 2022-06-12 20:53:39.041736
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import PluginLoader
    from ansible.errors import AnsibleError
    from os.path import dirname, join, realpath

    plugin_dir = join(dirname(dirname(dirname(dirname(realpath(__file__))))), 'lib/ansible/plugins/action')

    try:
        plugin_loader = PluginLoader(
            'ActionModule',
            '',
            enabled=lambda x: True,
            terms=['action', 'actions'],
            class_only=True,
            package_errors=True,
            directories=[plugin_dir],
        )
    except AnsibleError as e:
        print('Failed to load action plugins: %s' % to_text(e))


# Generated at 2022-06-12 20:53:48.628789
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    import collections
    import ansible.module_utils.common.collections as collections_utils
    config_data = ConfigData()
    
    def setting_factory(name, plugin_type, plugin_name=None, value=None, origin=None):
        p = collections.namedtuple('Plugin', 'type,name')
        s = collections.namedtuple('Setting', 'name,plugin,value,origin')
        return s(name, p(plugin_type, plugin_name), value, origin)

    # Create some settings
    setting1 = setting_factory('default_key', 'shell', None, 'value1', 'path1')
    setting2 = setting_factory('default_key', 'shell', 'sh', 'value2', 'path2')

# Generated at 2022-06-12 20:53:57.558448
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_context = {}
    test_context['config_data'] = ConfigData()
    test_context['test_data'] = []
    test_context['test_data'].append({'SB_PLUGIN_TYPE': 'B', 'SB_PLUGIN_NAME': 'C', 'SB_SETTING_NAME': 'D', 'SB_SETTING_VALUE': 'E', 'REF_ID': 'F'})
    test_context['test_data'].append({'SB_PLUGIN_TYPE': 'B', 'SB_PLUGIN_NAME': 'C', 'SB_SETTING_NAME': 'D', 'SB_SETTING_VALUE': 'E', 'REF_ID': 'F'})

# Generated at 2022-06-12 20:54:08.996462
# Unit test for method update_setting of class ConfigData

# Generated at 2022-06-12 20:54:16.138202
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # Case 1 - plugin is None
    setting = config_data.get_setting('foo', None)
    assert setting is None

    # Case 2 - plugin is not None
    setting = config_data.get_setting('foo', 'bar')
    assert setting is None


# Generated at 2022-06-12 20:54:24.270716
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data_obj = ConfigData()
    assert config_data_obj._global_settings == {}
    assert config_data_obj._plugins == {}

    # Testing update_setting method with plugin as None
    config_data_obj.update_setting("Ansible")
    assert config_data_obj._global_settings == {"Ansible": "Ansible"}
    assert config_data_obj._plugins == {}

    # Testing update_setting method with plugin parameter
    config_data_obj._global_settings["Ansible"] = None
    config_data_obj.update_setting("Ansible", "Plugin")
    assert config_data_obj._global_settings == {"Ansible": None}
    assert config_data_obj._plugins == {"Plugin": {"Ansible": {"Ansible": "Ansible"}}}




# Generated at 2022-06-12 20:54:28.647828
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    cd = ConfigData()
    cd.update_setting(PluginSetting())
    cd.update_setting(PluginSetting(), Plugin())
    assert len(cd.get_settings()) == 1
    assert len(cd.get_settings(Plugin())) == 1


# Generated at 2022-06-12 20:54:35.673572
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    assert data.get_setting('settings1') is None
    data.update_setting('setting1')
    assert data.get_setting('settings1') == 'setting1'
    assert data.get_settings().count('settings1') == 1
    assert data.get_setting('settings1', 'plugin1') is None
    assert data.get_settings('plugin1').count('settings1') == 0
    data.update_setting('setting1', 'plugin1')
    assert data.get_setting('settings1', 'plugin1') == 'setting1'
    assert data.get_settings('plugin1').count('settings1') == 1
    assert data.get_settings().count('settings1') == 2

# Generated at 2022-06-12 20:54:46.725183
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # create some settings as testcases
    global_setting = ConfigSetting(name='global_setting', value='global_value')
    plugin_setting = ConfigSetting(name='plugin_setting', value='plugin_value')

    # create the plugin
    plugin = Plugin('type', 'name')

    # create the config data that is beeing tested
    config_data = ConfigData()

    # update the settings
    config_data.update_setting(global_setting)
    config_data.update_setting(plugin_setting, plugin)

    # test for global setting
    settings = config_data.get_settings()

    assert len(settings) == 1

    assert settings[0].name == 'global_setting'
    assert settings[0].value == 'global_value'

    # test for plugin setting

# Generated at 2022-06-12 20:54:54.339467
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    data = ConfigData()

    # Add a global setting
    data.update_setting(PluginSetting('a', '', '', '', '', '', '', '', '', ''))

    # Add a plugin specific setting
    data.update_setting(PluginSetting('b', '', '', '', '', '', '', '', '', ''),
                        PluginDescriptor('type', 'name', 'path'))

    assert len(data.get_settings()) == 1
    assert len(data.get_settings(PluginDescriptor('type', 'name', 'path'))) == 1

    assert data.get_settings()[0].name == 'a'
    assert data.get_settings(PluginDescriptor('type', 'name', 'path'))[0].name == 'b'



# Generated at 2022-06-12 20:54:59.933968
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting('settings1')
    assert config_data.get_setting('settings1') == 'settings1'
    assert 'settings1' in config_data.get_settings()

# Generated at 2022-06-12 20:55:06.884734
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting1 = ConfigSetting('setting1', 'value1')
    setting2 = ConfigSetting('setting2', 'value2')
    setting3 = ConfigSetting('setting3', 'value3')
    plugin1 = Plugin('plugin1', 'type1')
    config_data.update_setting(setting2, plugin1)
    config_data.update_setting(setting3, plugin1)
    config_data.update_setting(setting1)
    settings = config_data.get_settings()
    assert len(settings) == 3
    assert settings[0].name == 'setting1'
    assert settings[1].name == 'setting2'
    assert settings[2].name == 'setting3'


# Generated at 2022-06-12 20:55:16.335744
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(ConfigSetting(name='display_skipped_hosts',
                                             value='on_unreachable',
                                             plugin=ConfigPlugin(type='core', name='display')))
    config_data.update_setting(ConfigSetting(name='display_ok_hosts',
                                             value='always',
                                             plugin=ConfigPlugin(type='core', name='display')))
    config_data.update_setting(ConfigSetting(name='display_custom_stats',
                                             value='always',
                                             plugin=ConfigPlugin(type='core', name='display')))

# Generated at 2022-06-12 20:55:20.256012
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting("ansible_host") is None
    assert config_data.get_setting("ansible_host", "localhost") is None


# Generated at 2022-06-12 20:55:21.500467
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    c = ConfigData()
    s = c.get_settings()
    assert s == []

# Generated at 2022-06-12 20:55:25.662557
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = MockSetting('test_setting', 'test_value', 'test_description')
    config_data.update_setting(setting, MockPlugin('test_plugin'))
    assert config_data.get_settings(MockPlugin('test_plugin')) == [setting]


# Generated at 2022-06-12 20:55:36.119194
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    settings = config_data.get_settings()
    assert not settings
    global_setting = Setting(name='foo', value='bar')
    connection_setting = Setting(name='foo', value='baz')
    connection_plugin = Plugin('connection', 'netconf')
    config_data.update_setting(global_setting)
    config_data.update_setting(connection_setting, connection_plugin)
    settings = config_data.get_settings()
    assert len(settings) == 1
    assert settings[0] == global_setting
    settings = config_data.get_settings(connection_plugin)
    assert len(settings) == 1
    assert settings[0] == connection_setting


# Generated at 2022-06-12 20:55:45.300911
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    setting = Setting("bar")
    config_data.update_setting(setting)
    settings = config_data.get_settings()
    ##print(settings)
    #assert settings[0] == virtualbox
    settings = config_data.get_settings()
    settings = config_data.get_settings()
    assert settings[0].name == "bar"
    assert settings[0].type == "foo"
    setting = Setting("host")
    config_data.update_setting(setting)
    settings = config_data.get_settings()
    assert settings[0].name == "host"
    assert settings[0].type == "foo"
    assert settings[1].name == "bar"
    assert settings[1].type == "foo"
    settings = config_data.get_settings()


# Generated at 2022-06-12 20:55:53.249651
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    
    setting = Setting('ansible_python_interpreter', '/usr/bin/python', {'env': {'PATH': '/usr/bin'}, 'ini': {'configure': '/etc/ansible/ansible.cfg'}, 'yaml': {'configure': '/etc/ansible/ansible.yml'}})
    plugin = Plugin('core', 'action_plugin', '/etc/ansible/plugins/action_plugins')
    setting1 = Setting('ansible_python_interpreter', '/usr/bin/python', {'env': {'PATH': '/usr/bin'}, 'ini': {'configure': '/etc/ansible/ansible.cfg'}, 'yaml': {'configure': '/etc/ansible/ansible.yml'}})

# Generated at 2022-06-12 20:56:04.039474
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    global_setting_1 = {
        'name': 'DEFAULT_ANSIBLE_LIBRARY',
        'value': './library',
        'source': '',
        'source_type': '',
        'source_version': '',
        'source_file': ''
    }

    global_setting_2 = {
        'name': 'max_vars',
        'value': '1000',
        'source': '',
        'source_type': '',
        'source_version': '',
        'source_file': ''
    }


# Generated at 2022-06-12 20:56:08.920593
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    data = ConfigData()
    assert data.get_setting("fact_caching") is None
    data.update_setting("setting")
    assert data.get_setting("setting") is not None


# Generated at 2022-06-12 20:56:16.803450
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import ConfigData, PluginConfig
    configData = ConfigData()
    data = configData.get_settings()
    assert data is not None
    configData.update_setting(PluginConfig('foo', 'string', 'bar', 'get', 'Display a string value', True, 'global', '', '', ''))
    data = configData.get_settings()
    assert data[0].name == "foo"


# Generated at 2022-06-12 20:56:28.362508
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    config_data.update_setting(Setting("1", "1"))
    setting = Setting("2", "2")
    config_data.update_setting(setting)
    setting = Setting("3", "3", plugin_type="C")
    config_data.update_setting(setting)

    assert len(config_data.get_settings()) == 2
    assert config_data.get_setting("1") == Setting("1", "1")
    assert config_data.get_setting("2") == Setting("2", "2")
    assert config_data.get_setting("3") == None

    assert config_data.get_settings(Plugin("3", "3", plugin_type="C")) == [Setting("3", "3", plugin_type="C")]
    assert config_data.get_setting

# Generated at 2022-06-12 20:56:30.474041
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    c = ConfigData()
    assert c.get_settings() == []


# Generated at 2022-06-12 20:56:41.993025
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo','bar','global-setting','','','','',''))
    config_data.update_setting(Setting('one','two','global-setting','','','','',''))
    config_data.update_setting(Setting('one','two','global-setting','','','','',''))
    assert config_data.get_setting('foo').value == 'bar'
    assert config_data.get_setting('foo').origin == 'global-setting'
    assert config_data.get_setting('foo').plugin is None
    assert config_data.get_setting('foo').origin_type is None
    assert config_data.get_setting('foo').priority == 100
    assert config_data.get_setting('foo').original_value == 'bar'
    assert config_

# Generated at 2022-06-12 20:56:47.499871
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    c = ConfigData()

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import CollectionLoader

# Generated at 2022-06-12 20:56:56.059181
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    print('Testul pentru metoda get_settings din clasa ConfigData')

# Generated at 2022-06-12 20:57:02.853465
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
	configdata=ConfigData()
	setting = Setting('fact_caching_connection', '/home/ansible/factcachesqlite.db')
	configdata.update_setting(setting)
	set1=configdata.get_setting('fact_caching_connection')
	assert(set1.name=='fact_caching_connection')
	assert(set1.value=='/home/ansible/factcachesqlite.db')

# Generated at 2022-06-12 20:57:09.848620
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()
    plugin_type = 'myplugin_type'
    plugin_name = 'myplugin_name'
    setting_name = 'myplugin_setting'
    setting_desc = 'myplugin_setting_desc'
    setting_value = 'myplugin_setting_value'
    plugin = Plugin(plugin_type, plugin_name)
    setting = Setting(setting_name, setting_desc)
    setting.value = setting_value
    config.update_setting(setting, plugin)
    config.update_setting(setting)
    assert config.get_setting(setting_name, plugin) == setting
    assert config.get_setting(setting_name) == setting


# Generated at 2022-06-12 20:57:16.382106
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    
    # Initialize configdata
    configdata = ConfigData()

    # Assert that the global settings are empty
    assert len(configdata.get_settings()) == 0

    # Assert that the global settings are empty
    assert len(configdata.get_settings('acme.plugins.test')) == 0

    # Add setting to global settings
    configdata.update_setting('test.test')

    # Assert that the global settings are not empty
    assert len(configdata.get_settings()) == 1

# Generated at 2022-06-12 20:57:25.287611
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = Setting('setting1', 'value1')
    config_data.update_setting(setting1)
    setting2 = Setting('setting2', 'value2')
    config_data.update_setting(setting2)
    assert config_data._global_settings['setting1'].name == 'setting1'
    assert config_data._global_settings['setting2'].name == 'setting2'


# Generated at 2022-06-12 20:57:27.045635
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    assert config_data.get_settings() == []



# Generated at 2022-06-12 20:57:29.930981
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    obj = ConfigData()
    plugin = {}
    setting = {}
    obj.update_setting(setting, plugin)


# Generated at 2022-06-12 20:57:35.743328
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting1 = Setting(name='setting1', value='value1')
    config_data.update_setting(setting1)
    assert config_data.get_setting('setting1') == setting1
    setting2 = Setting(name='setting2', value='value2')
    plugin = Plugin(name='plugin', type='plugin_type')
    config_data.update_setting(setting2, plugin)
    assert config_data.get_setting('setting2', plugin) == setting2

# Generated at 2022-06-12 20:57:38.504979
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from ansible.module_utils.common.config import Setting
    setting = Setting(name='test', plugin=None)
    config_data.update_setting(setting)
    assert config_data.get_setting('test') == setting


# Generated at 2022-06-12 20:57:45.336610
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin =  Plugin("fancy_test_plugin", "action")
    setting_01 = Setting("setting_01", "string")
    setting_02 = Setting("setting_02", "string")

    config_data.update_setting(setting_01, plugin)
    config_data.update_setting(setting_02, plugin)

    settings = config_data.get_settings(plugin)
    assert setting_01 in settings and setting_02 in settings


# Generated at 2022-06-12 20:57:52.769193
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ..setting_base import SettingBase

    config_data = ConfigData()

    setting = SettingBase('xyz', 'abc')
    config_data.update_setting(setting)

    # Test that the setting exists in global settings
    assert config_data.get_setting('xyz') is not None
    assert config_data.get_setting('xyz').name == 'xyz'
    assert config_data.get_setting('xyz').value == 'abc'

    # Test that the setting does not exist in local settings
    assert config_data.get_setting('xyz', 'local') is None

# Generated at 2022-06-12 20:57:58.817843
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_setting = Setting("PLUGINS", "/usr/share/ansible/plugins")
    test_plugin = Plugin("ActionModule", "debug")

    config_data.update_setting(test_setting)
    config_data.update_setting(test_setting, test_plugin)

    assert config_data.get_setting("PLUGINS") == test_setting
    assert config_data.get_setting("PLUGINS", test_plugin) == test_setting

# Generated at 2022-06-12 20:58:04.728521
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    import unittest
    module_names = ('common', 'module_utils', 'callback', 'cliconf', 'netconf', 'inventory', 'vars', 'action', 'cache', 'connection', 'documentation_fragments', 'lookup', 'shell', 'strategy', 'terminal', 'test', 'units')
    class FakeSetting():

        def __init__(self, name, value):
            self._name = name
            self._value = value

    class FakePlugin():

        def __init__(self, type, name):
            self._type = type
            self._name = name


# Generated at 2022-06-12 20:58:07.192642
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()
    setting = Setting('test_setting', 'test_value')
    config.update_setting(setting)

    assert config.get_setting('test_setting') == setting


# Generated at 2022-06-12 20:58:12.521148
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    data = ConfigData()
    setting = NamedSetting("key", "value", "global")
    data.update_setting(setting)
    assert data.get_setting("key") == setting


# Generated at 2022-06-12 20:58:16.168213
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()
    assert not config_data.get_setting('lookup')
    assert not config_data.get_setting('lookup', 'lookup_plugin')
    assert not config_data.get_setting('')
    assert not config_data.get_setting('')



# Generated at 2022-06-12 20:58:22.042260
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    class mock_setting:
        def __init__(self, name):
            self.name = name
            self.value = name

    class mock_plugin:
        def __init__(self, type, name):
            self.type = type
            self.name = name

    cd = ConfigData()

    s1 = mock_setting('s1')
    s2 = mock_setting('s2')
    cd.update_setting(s1)
    cd.update_setting(s2)
    output_settings = cd.get_settings()
    assert len(output_settings) == 2

    cd = ConfigData()

    s1 = mock_setting('s1')
    s2 = mock_setting('s2')
    p1 = mock_plugin('p1', 'p1')

# Generated at 2022-06-12 20:58:32.815217
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.module_utils.config_data import ConfigSetting, Plugin
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_unicode

    plugin_type = 'connection'
    plugin_name = 'netconf'
    plugin = Plugin(plugin_type, plugin_name)

    cd = ConfigData()
    for setting_name in ('timeout', 'persistent_connect_timeout', 'persistent_command_timeout'):
        setting = ConfigSetting(setting_name, to_unicode('10'))
        cd.update_setting(setting)
        setting = ConfigSetting(setting_name, to_unicode('20'))
        cd.update_setting(setting, plugin)

    # make sure we get the correct data when plugin is None

# Generated at 2022-06-12 20:58:39.759022
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = Plugin('cloud', 'openstack')
    setting1 = Setting('foo', plugin=plugin)
    setting2 = Setting('bar', plugin=plugin)
    # configure setting 1
    setting1.update(value='value1')
    config_data.update_setting(setting1)
    # configure setting 2
    setting2.update(value='value2')
    config_data.update_setting(setting2)
    assert len(config_data.get_settings()) == 2


# Generated at 2022-06-12 20:58:42.660174
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    data = ConfigData()

    assert(data.get_setting('abc') is None)

    pass


# Generated at 2022-06-12 20:58:49.454955
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import config_loader
    from ansible.plugins.loader import plugin_loader
    from units.mock.loader import DictDataLoader
    from units.mock.plugins.loader import plugin_config_loader

    config_data = ConfigData()
    config_loader.add(plugin_config_loader, 'ini')

    config_data.update_setting(plugin_config_loader.get_setting('default_module_name'))
    config_data.update_setting(plugin_config_loader.get_setting('default_module_name', 'action'))


# Generated at 2022-06-12 20:58:52.829376
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    setting = Setting("foo", "bar", 42)
    configData.update_setting(setting)
    assert(configData.get_setting("foo") == setting)



# Generated at 2022-06-12 20:59:00.113360
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configData = ConfigData()
    try:
        from ansible.plugins.loader import PluginLoader
    except ImportError:
        from ansible.plugins import PluginLoader
    try:
        from ansible.parsing.utils.yaml.objects import AnsibleVaultEncryptedUnicode
    except ImportError:
        from ansible.parsing.vault import VaultSecret

    inventory_loader = PluginLoader('InventoryModule', 'inventory/', 'ansible.plugins.inventory')
    inventory_plugins = inventory_loader.all(class_only=True)
    inventory_plugin = inventory_plugins['host_list']()
    inventory_plugin.name = "host_list"

    plugin_loader = PluginLoader('ModuleUtils', 'module_utils/', 'ansible.plugins.module_utils')
    plugin_plugins = plugin_loader

# Generated at 2022-06-12 20:59:06.924625
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    
    config_data = ConfigData()
    config_data.update_setting(Setting('test', 'test', 'test'))
    plugin = Plugin('test', 'test', 'test')
    config_data.update_setting(Setting('test', 'test', 'test'), plugin)
    assert len(config_data.get_settings()) == 1
    assert len(config_data.get_settings(plugin)) == 1    


# Generated at 2022-06-12 20:59:19.270059
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import io
    import sys
    import tempfile

    # Class used to capture stdout and stderr
    class Stream(object):
        def __init__(self):
            self.data = io.StringIO()

        def write(self, s):
            self.data.write(s)

        def __str__(self):
            return self.data.getvalue()

    # Capture stdout and stderr to demonstrate
    # interaction with typical terminal and IDE
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = out = Stream()
    sys.stderr = err = Stream()

    config_data = ConfigData()
    plugin = Plugin('name', 'type')
    setting = Setting('name', 'value', 'description')


# Generated at 2022-06-12 20:59:24.719979
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    import pytest

    config_data = ConfigData()
    plugin = PluginDescriptor('test_plugin', 'test_type')
    config_data.update_setting(PluginSetting('test_setting', 'test_value'), plugin)

    settings = config_data.get_settings()
    assert len(settings) == 0
    settings = config_data.get_settings(plugin)
    assert len(settings) == 1


# Generated at 2022-06-12 20:59:30.698186
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()

    plugin_type = 'callback'
    plugin_name = 'debug'
    name = 'verbosity'

    configdata.update_setting(Setting(name=name, value=0))
    configdata.update_setting(Setting(name=name, value=1), plugin=Plugin(type=plugin_type, name=plugin_name))

    assert configdata.get_settings()[0].value == 0
    assert configdata.get_settings(plugin=Plugin(type=plugin_type, name=plugin_name))[0].value == 1


# Generated at 2022-06-12 20:59:40.978484
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from collections import namedtuple
    Setting = namedtuple('Setting', ['name', 'value', 'origin'])
    setting = Setting(name='foo', value='bar', origin='baz')
    config_data.update_setting(setting, plugin=None)
    assert config_data._global_settings[setting.name].value == setting.value
    assert config_data._global_settings[setting.name].origin == setting.origin

    module = namedtuple('Module', ['type', 'name'])
    module = module(type='module', name='module_1')
    config_data.update_setting(setting, plugin=module)
    assert config_data._plugins[module.type][module.name][setting.name].value == setting.value

# Generated at 2022-06-12 20:59:43.054107
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()

    plugin = None
    settings = config_data.get_settings(plugin)

    assert len(settings) == 0



# Generated at 2022-06-12 20:59:49.344005
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    plugin = Plugin('modules')
    config_data = ConfigData()
    assert config_data.get_settings(plugin) == []
    assert config_data.get_settings() == []

    setting1 = Setting('module_utils', 'lib/ansible/module_utils/', 'module_utils path')
    config_data.update_setting(setting1)
    assert config_data.get_settings(plugin) == []
    assert config_data.get_settings() == [setting1]

    setting2 = Setting('action_plugins', 'lib/ansible/plugins/action/', 'action plugin path')
    config_data.update_setting(setting2, plugin)
    assert config_data.get_settings(plugin) == [setting2]
    assert config_data.get_settings() == [setting1]


# Generated at 2022-06-12 20:59:58.568778
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    from ansible.plugins.loader import generate_raw_config

    plugin_type = 'lookup'
    plugin_name = 'vault'
    attributes = dict(
        name='vault_password_file',
        section='lookup_plugins/vault',
        env_var='ANSIBLE_VAULT_PASSWORD_FILE',
    )
    config = generate_raw_config(plugin_type, plugin_name, attributes)
    config_data = ConfigData()
    config_data.update_setting(config)
    assert config_data.get_settings(config.plugin)[0].value == '/path/to/my/file'



# Generated at 2022-06-12 21:00:01.335732
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    plugin = Plugin('python', 'dummy_module')
    setting = Setting()
    config_data.update_setting(setting, plugin)
    assert [setting] == config_data.get_settings(plugin)



# Generated at 2022-06-12 21:00:09.682593
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    c = ConfigData()
    # test case1: get_setting(self, name, plugin=None)
    assert(c.get_setting("bar")==None)
    # test case2: get_setting(self, name, plugin=None)
    from PluginSpec import PluginSpec
    from PluginSpec import PluginSetting
    s = PluginSetting("bar")
    p = PluginSpec("foo", "bar", "baz")
    c.update_setting(s,p)
    assert(c.get_setting("bar")==None)
    # test case3: get_setting(self, name, plugin=None)
    assert(c.get_setting("bar", p)==s)
    assert(c.get_setting("foo", p)==None)
    assert(c.get_setting("foo")==None)

# Unit

# Generated at 2022-06-12 21:00:17.101870
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    class FakePlugin(object):
        def __init__(self, name='fake_plugin', type='fake_type'):
            self.name = name
            self.type = type

    global_setting = {'name': 'foo', 'value': 'bar'}
    config_data = ConfigData()
    config_data.update_setting(global_setting)
    global_setting_from_data = config_data.get_setting(global_setting['name'])
    assert global_setting_from_data == global_setting

    plugin_setting = {'name': 'foo', 'value': 'bar'}
    plugin = FakePlugin()
    config_data.update_setting(plugin_setting, plugin)
    plugin_setting_from_data = config_data.get_setting(plugin_setting['name'], plugin)
    assert plugin

# Generated at 2022-06-12 21:00:31.346481
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    """
    :return:
    """
    config = ConfigData()
    setting = {
        "name": "a",
        "default": 2
    }
    config.update_setting(setting)
    assert(config.get_setting("a")["name"] == "a")


# Generated at 2022-06-12 21:00:41.878392
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import PluginLoader
    from ansible.config.manager import ConfigManager
    from ansible.config.setting import Setting, ValueOrigin

    # create Setting objects for testing
    setting_a = Setting('a', 'Value A', CONSTANT, ValueOrigin(CONSTANT, 'config file', 'section', 'option'))
    setting_b = Setting('b', 'Value B', CONSTANT, ValueOrigin(CONSTANT, 'env var', 'ENV_VAR2', 'value'))
    setting_c = Setting('c', 'Value C', CONSTANT, ValueOrigin(CONSTANT, 'env var', 'ENV_VAR3', 'value'))

    # create ConfigData object to test
    config_data = ConfigData()

    # test getting non-existant setting
    assert config_data.get

# Generated at 2022-06-12 21:00:52.031322
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    # Instantiate ConfigData object
    config_data = ConfigData()
    
    # Verify that _global_settings is an empty dict
    assert config_data._global_settings == {}
    
    # Verify that _plugins is an empty dict
    assert config_data._plugins == {}
    
    # Configure a setting for global domain
    setting1 = ConfigDataSetting('setting1', 'value1', source='file', section='ansible.cfg')
    config_data.update_setting(setting1)
    
    # Verify that _global_settings is not empty
    assert config_data._global_settings != {}
    
    # Verify that _global_settings contains 1 element
    assert len(config_data._global_settings) == 1
    
    # Verify that _global_settings contains the expected key

# Generated at 2022-06-12 21:01:03.591567
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    config_data.update_setting(ConfigSetting('name1', 'value1'))

    # global setting
    assert config_data.get_setting('name1', None) == ConfigSetting('name1', 'value1')
    # unset global setting
    assert config_data.get_setting('name2', None) is None

    # unset plug-in type/name
    assert config_data.get_setting('name3', ConfigPlugin('type1', 'name1')) is None

    config_data.update_setting(ConfigSetting('name2', 'value2'), ConfigPlugin('type1', 'name1'))

    # plug-in type/name

# Generated at 2022-06-12 21:01:04.977754
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    d = ConfigData()
    d.get_settings()


# Generated at 2022-06-12 21:01:11.872034
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    configdata.update_setting(Setting("fact-cache", "/home/ansible/plugins/facts"))
    configdata.update_setting(Setting("CACHE_PLUGIN", "jsonfile"))
    configdata.update_setting(Setting("CACHE_PLUGIN_CONNECTION", None))
    configdata.update_setting(Setting("CACHE_PLUGIN_TIMEOUT", 3600))
    assert len(configdata.get_settings()) == 4
    configdata.update_setting(Setting("gathering", "explicit"))
    assert len(configdata.get_settings()) == 5


# Generated at 2022-06-12 21:01:16.040932
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    assert config.get_setting('foo') == None
    assert config.get_setting('foo', plugin=None) == None
    assert config.get_setting('foo', plugin=[]) == None
    assert config.get_setting('foo', plugin=[]) == None


# Generated at 2022-06-12 21:01:25.518201
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    import os
    import yaml
    from ansible.plugins.action import ActionModule
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.connection import ConnectionBase
    from ansible.plugins.inventory import InventoryBase
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.module_utils import ModuleUtilsBase
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.vars import VarsBase

    class TestPlugin(object):

        type = None
        name = None

        def __init__(self, type, name):
            self.type = type
            self.name = name

    config_data = ConfigData()

# Generated at 2022-06-12 21:01:31.395211
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='foo', value='bar'))
    assert config_data.get_setting('foo') == Setting(name='foo', value='bar')

    assert config_data.get_setting('aabb') is None
    assert config_data.get_setting('aabb', Plugin()) is None


# Generated at 2022-06-12 21:01:40.574622
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_data =[('x', 'y', 'z', 'a', 'example', 'example', 'example', 'example'),
                ('p', 'q', 'r', 'b', 'example2', 'example2', 'example2', 'example2')]
    test_data.append(('p', 'q', 'r', 'b', 'example2', 'example2', 'example2', 'example2'))
    for data in test_data:
        setting = ConfigSetting()
        setting.name = data[0]
        setting.category = data[1]
        setting.getting_started = data[2]
        setting.description = data[3]
        setting.aliases = [test_data[x] for x in range(4, 8)]

# Generated at 2022-06-12 21:02:00.136156
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    A = ConfigData()
    assert A.get_settings() == []


# Generated at 2022-06-12 21:02:03.391776
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # unit test: config_data.get_setting
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0
    assert len(config_data.get_settings('non-existing plugin')) == 0

# Generated at 2022-06-12 21:02:07.033761
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    from ansible.config.setting import Setting

    # Create test instances
    config_data = ConfigData()
    setting = Setting('foo', description='bar')

    # Test the method does not raise exceptions
    config_data.update_setting(setting)


# Generated at 2022-06-12 21:02:17.866083
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible import constants as C
    from ansible.plugins.loader import plugin_loader

    # Update config module search path
    C.config.config_module_paths = ['./unit/plugins/test_config_data']

    # Load config plugins
    plugin_loader.load_config_plugins()
    config_plugins = plugin_loader.get_config_plugins()

    # Create config data
    config_data = ConfigData()
    config_data.update_setting(config_plugins[0].get_settings()[0])
    config_data.update_setting(config_plugins[1].get_settings()[0])
    config_data.update_setting(config_plugins[1].get_settings()[1])

# Generated at 2022-06-12 21:02:21.793838
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansiblelint.rules.lineinfile import LineInFileRule

    configdata = ConfigData()
    configdata.update_setting(LineInFileRule())


# Generated at 2022-06-12 21:02:30.685196
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    # Arrange
    config_data = ConfigData()
    plugin = Plugin('test', 'debug')
    config_data.update_setting(Setting('name', 'description', 'time'), plugin)
    config_data.update_setting(Setting('value', 'description', 'time'), plugin)
    config_data.update_setting(Setting('name2', 'description', 'time'), plugin)
    config_data.update_setting(Setting('name6', 'description', 'time'), plugin)
    plugin1 = Plugin('test1', 'debug')
    config_data.update_setting(Setting('name3', 'description', 'time'), plugin1)

    # Act
    actual = config_data.get_setting('name')

    # Assert
    assert actual.name == 'name'


# Generated at 2022-06-12 21:02:37.415036
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    test_setting = Setting('setting1')
    test_setting._plugin = Plugin('plugin1', 'plugin type')
    config_data.update_setting(test_setting, test_setting._plugin)
    assert config_data._plugins['plugin type']['plugin1']['setting1'] == test_setting


# Generated at 2022-06-12 21:02:44.460496
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    plugin = Plugin("test", "test")

    assert setting_1.get_plugin_type() == 'test'
    assert setting_1.get_plugin_name() == 'test'
    assert setting_1.get_name() == 'test_setting_1'
    assert setting_1.get_value() == 'test_setting_1 value'
    assert setting_1.get_description() == 'test_setting_1 description'

    config.update_setting(setting_1)
    assert config.get_setting("test_setting_1", plugin) == setting_1

    assert setting_2.get_plugin_type() == 'test'
    assert setting_2.get_plugin_name() == 'test'
    assert setting_2.get_name() == 'test_setting_2'

# Generated at 2022-06-12 21:02:52.117030
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting(name='test', value='test_value')
    plugin = Plugin(type='module', name='test')
    # test global update_setting
    config_data.update_setting(setting)
    assert config_data._global_settings['test'].value == 'test_value'
    # test plugin update_setting
    config_data.update_setting(setting, plugin)
    assert config_data._plugins[plugin.type][plugin.name]['test'].value == 'test_value'


# Generated at 2022-06-12 21:02:56.530294
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    assert len(config_data.get_settings()) == 0
    config_data.update_setting(Setting(name="key1", value="value1"))
    assert len(config_data.get_settings()) == 1
    assert config_data.get_settings()[0].name == "key1"
    assert config_data.get_settings()[0].value == "value1"
    config_data.update_setting(Setting(name="key2", value="value2"))
    assert len(config_data.get_settings()) == 2
    assert config_data.get_settings()[1].name == "key2"
    assert config_data.get_settings()[1].value == "value2"
