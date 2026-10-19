

# Generated at 2022-06-12 20:53:32.318883
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    setting1 = {"name": "setting1", "value": "value1"}
    setting2 = {"name": "setting2", "value": "value2"}

    # Put short-cut names for the setting types in local variables
    SETTING_TYPES = configdata.SETTING_TYPES
    GENERAL_SETTING = configdata.GENERAL_SETTING
    PLUGIN_SETTING = configdata.PLUGIN_SETTING
    MODULE_SETTING = configdata.MODULE_SETTING
    CLICONF_SETTING = configdata.CLICONF_SETTING
    CORE_CLI_SETTING = configdata.CORE_CLI_SETTING
    CORE_PLUGIN_SETTING = configdata.CORE_PLUGIN_SETTING
    NETWORK_CLI

# Generated at 2022-06-12 20:53:42.868960
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    # Setting global
    global_setting = Setting('global_setting', 'global_test')
    config_data.update_setting(global_setting)
    assert(config_data._global_settings == {'global_setting': global_setting})
    # Setting plugin
    plugin_setting = Setting('plugin_setting', 'plugin_test')
    config_data.update_setting(plugin_setting, PluginName('test', 'connection'))
    assert('test' in config_data._plugins['connection'])
    assert(config_data._plugins['connection']['test'] == {'plugin_setting': plugin_setting})
    # Setting existing global
    existing_global_setting = Setting('global_setting', 'existing_global_test')
    config_data.update_setting(existing_global_setting)
   

# Generated at 2022-06-12 20:53:51.246159
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config = ConfigData()

    setting_1 = ConfigSetting(name='test_setting')
    config.update_setting(setting_1, plugin=None)

    test_plugin = Plugin(type='test_plugin', name='test_name', path='test_path')
    setting_2 = ConfigSetting(name='test_setting')
    config.update_setting(setting_2, plugin=test_plugin)

    assert config.get_setting('test_setting') == setting_1
    assert config.get_setting('test_setting', plugin=test_plugin) == setting_2

    assert config.get_setting('test_setting_does_not_exist') is None
    assert config.get_setting('test_setting_does_not_exist', plugin=test_plugin) is None



# Generated at 2022-06-12 20:53:58.764526
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """Unit testing for ConfigData.get_settings().
    """
    from ansible.plugins.vars import VariableManager
    from ansible.config.setting import Setting

    config_data = ConfigData()
    vm = VariableManager()
    config_data.update_setting(Setting('connection', 'local', vm, display='Connection', help='execution connection type', type="str", choices=['smart', 'ssh', 'paramiko', 'local'], default='smart', env_var=None))

    # assert without plugin
    assert config_data.get_settings()[0].name == 'connection'
    assert config_data.get_settings()[0].value == 'local'
    assert config_data.get_settings()[0].filename == ''
    assert config_data.get_settings()[0].origin == 'default'

    # assert

# Generated at 2022-06-12 20:54:03.740124
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    test_obj = ConfigData()
    setting = Setting('I\'m a setting')
    test_obj.update_setting(setting)
    assert setting.name in test_obj._global_settings
    assert test_obj._global_settings[setting.name] == setting


# Generated at 2022-06-12 20:54:10.194784
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    from ansible.module_utils.common.collections import ImmutableDict

    from ansible.plugins.test.test_collection_loader import TestModule
    from ansible.plugins.test.test_action_plugin import ActionModule as TestActionModule

    test_module = TestModule(
        type='module',
        name='plugin_name',
        path='{0}/ansible/plugins/test/test_module_plugin.py'.format(os.path.dirname(__file__)),
    )
    test_action_module = TestActionModule(
        type='action',
        name='plugin_name',
        path='{0}/ansible/plugins/test/test_action_plugin.py'.format(os.path.dirname(__file__)),
    )

    test_global

# Generated at 2022-06-12 20:54:14.851240
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    setting = Setting('test', 'value')
    cd.update_setting(setting)
    assert cd._global_settings['test'] == setting


# Generated at 2022-06-12 20:54:16.559384
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    test_cd = ConfigData()
    assert(test_cd.get_settings() == [])


# Generated at 2022-06-12 20:54:21.296937
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    assert config_data.get_setting('unknown') is None
    assert config_data.get_setting('unknown', None) is None


# Generated at 2022-06-12 20:54:25.444437
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_dat = ConfigData()
    assert config_dat.get_settings() == []

    plugin = Plugin('v2', 'shell')
    assert config_dat.get_settings(plugin) == []


# Generated at 2022-06-12 20:54:40.238892
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    assert not config_data.get_settings()
    setting = Setting('location', 'default', 'description')
    assert not config_data.get_settings()
    config_data.update_setting(setting)
    assert config_data.get_settings()
    setting = Setting('location', 'new default', 'new description')
    config_data.update_setting(setting)
    assert config_data.get_setting('location').default == 'new default'
    assert config_data.get_setting('location').description == 'new description'
    setting = Setting('new setting', 'new setting default', 'new setting description')
    config_data.update_setting(setting)
    config_data_settings = config_data.get_settings()
    assert len(config_data_settings) == 2
    assert any

# Generated at 2022-06-12 20:54:50.432903
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    import units.compat.mock as mock
    import ansible.plugins.config.base as base

    cm = ConfigData()

    mock_setting = base.Setting('name1', base.Setting.STRING, base.Setting.CONFIG)
    cm_get_setting = ConfigData.get_setting
    with mock.patch.object(ConfigData, 'get_setting', wraps=cm_get_setting) as m:
        cm.update_setting(mock_setting)

        # test global setting
        m.assert_called_once_with(ConfigData, 'name1')
        assert cm.get_setting('name1') == mock_setting

        # test plugin setting
        m.reset_mock()
        from collections import namedtuple
        Plugin = namedtuple('Plugin', ['name', 'type'])
        mock_plugin

# Generated at 2022-06-12 20:55:01.623632
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    from ansible.plugins.loader import AnsiblePlugin
    from ansible.plugins.base_configuration import BaseConfiguration

    with open("/home/honggildong/ansible/hacking/test/units/lib/ansible/plugins/lookup/test_template.py","r") as f:
        code = f.read()
    print(code)
    exec(code, globals())


# Generated at 2022-06-12 20:55:12.695909
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    config_data = ConfigData()
    plugin = PluginSpec(type='connection', name='local')
    setting = ConfigEntry(plugin.type, plugin.name, 'accelerate', 'True', 'bool', 'No description.')
    config_data.update_setting(setting)
    setting = ConfigEntry(plugin.type, plugin.name, 'accelerate_timeout', '30', 'int', 'No description.')
    config_data.update_setting(setting)
    settings = config_data.get_settings(plugin)
    assert len(settings) == 2

    global_setting = ConfigEntry(None, None, 'action_plugins', 'Dir1,Dir2', 'list', 'No description.')
    config_data.update_setting(global_setting)

# Generated at 2022-06-12 20:55:14.921441
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    cd = ConfigData()


# Generated at 2022-06-12 20:55:22.947769
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    # create instance of ConfigData
    config_data = ConfigData()

    # create Mock object for plugin.Plugin
    plugin = MockPlugin()

    # create Mock object for config_data.Setting
    setting = MockSetting()

    # update setting inside the config_data
    config_data.update_setting(setting, plugin)

    # get settings from config_data for the plugin
    settings = config_data.get_settings(plugin)

    # verify settings is list of one setting
    assert(len(settings) == 1)

    # verify the one setting is the setting we added
    assert(settings[0] is setting)

# Generated at 2022-06-12 20:55:26.356811
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(1)
    config_data.update_setting(2)
    assert config_data.get_settings() == [1, 2]


# Generated at 2022-06-12 20:55:36.735133
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    print('')
    print('####################Expected results of method update_setting of class ConfigData##############')
    print('For update global setting:')
    update_setting = config_data.update_setting(Setting('debug','True'))
    print(update_setting)
    print('For update setting for plugin process:')
    update_setting = config_data.update_setting(Setting('enabled','0'),Plugin('process','psutil'))
    print(update_setting)
    print('For update setting for plugin cloud, this is wrong input:')
    update_setting = config_data.update_setting(Setting('enabled','0'),Plugin('cloud','cloud'))
    print(update_setting)
    print('################################################################################')


# Generated at 2022-06-12 20:55:45.723990
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    test_host_1 = Host('host_1')
    test_host_2 = Host('host_2')
    test_host_1.set_variable('ansible_net_hostname', 'test1')
    test_host_2.set_variable('ansible_net_hostname', 'test2')
    test_host_1.set_variable('a_setting', 'my_value')
    test_host_2.set_variable('a_setting', 'my_other_value')
    test_host_1.set_variable('another_setting', 'my_value')
    test_host_2.set_variable('another_setting', 'my_other_value')
    test_group_1 = Group('group_1')
    test_group_1.add_host(test_host_1)
    test_

# Generated at 2022-06-12 20:55:53.193052
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    data = ConfigData()
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader

    data._global_settings = {
        'ansible_host_key_checking': True,
        'retry_files_enabled': True,
        'host_key_auto_add': True
    }

    data._plugins = {
        'cli': {
            'default': {
                'ansible_host_key_checking': False
            }
        }
    }

    plugin = CLI('default', "/dev/null", DataLoader(), None)

    settings = data.get_settings()
    assert len(settings) == 3

    settings = data.get_settings(plugin)
    assert len(settings) == 1

    settings = data.get_settings()

# Generated at 2022-06-12 20:56:09.021736
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    configdata = ConfigData()

    # check initial value
    assert len(configdata._global_settings) == 0
    assert len(configdata._plugins) == 0

    # create a setting with plugin name
    fake_plugin = ConfigDataPlugin("v2_runner", "s3")
    fake_setting = ConfigDataSetting("aws_access_key", "value")
    configdata.update_setting(fake_setting, fake_plugin)

    assert len(configdata._global_settings) == 0
    assert len(configdata._plugins) == 1
    assert len(configdata._plugins["v2_runner"]) == 1

    # create a setting without plugin name
    fake_setting = ConfigDataSetting("abc", "xyz")
    configdata.update_setting(fake_setting)

    assert len(configdata._global_settings) == 1

# Generated at 2022-06-12 20:56:17.186033
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from ansible.plugins.loader import PluginLoader
    config_data = ConfigData()
    plugin = PluginLoader('action', 'mymodule', 'mymodule_class', 'mymodule_module', 'mymodule_base_class')
    config_data.update_setting('module', plugin)
    plugin_path = config_data.get_setting('module', plugin)
    assert plugin_path.name == 'module'
    assert plugin_path.plugin.name == 'mymodule'

# Generated at 2022-06-12 20:56:28.709533
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansible.plugins.loader import PluginLoader

    config_data = ConfigData()

    strategy = PluginClass(type='strategy', name='free', path='/tmp/ansible/ansible/plugins/strategy')
    connection = PluginClass(type='connection', name='local', path='/tmp/ansible/ansible/plugins/connection')
    lookup = PluginClass(type='lookup', name='file', path='/tmp/ansible/ansible/plugins/lookup')

    # Test with plugin = None
    config_data.update_setting(Setting(name='help'))
    result = config_data.get_settings()
    assert len(result) == 1
    assert result[0].name == 'help'

    # Test with strategy plugin
    config_data.update_setting(Setting(name='help'), strategy)
   

# Generated at 2022-06-12 20:56:39.722646
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    import sys
    import os
    import runpy
    sys.path.append("..")
    from bin.plugins import PluginLoader
    from data.base import Setting

    conf = ConfigData()

    plugin_loader = PluginLoader()
    plugin_loader.load_plugins()

    plugin_type = plugin_loader.get_type("action")
    plugin = plugin_type.get_plugin("setup")

    conf.update_setting(Setting("gather_facts", True, plugin))
    conf.update_setting(Setting("remote_user", "ansible", plugin))
    conf.update_setting(Setting("transport", "paramiko", plugin))

    settings = conf.get_settings(plugin)
    assert len(settings) == 3

# Generated at 2022-06-12 20:56:42.761012
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()
    config_data.update_setting(ConfigSetting(name='setting_a'))

    assert config_data.get_settings()[0].name == 'setting_a'
    assert config_data.get_settings()[0].value == None


# Generated at 2022-06-12 20:56:53.328803
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()

    import ansible.constants as C
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.connection.local as connection_local

    local_connection = plugin_loader.get(plugin_loader.C.C_CONNECTION, 'local', connection_local.Connection)

    config.update_setting(Setting(local_connection, C.DEFAULT_LOCAL_TMP, '$HOME/tmp'))
    config.update_setting(Setting(local_connection, C.DEFAULT_REMOTE_TMP, '/tmp'))

    import ansible.plugins.lookup.environ as lookup_environ
    environ = plugin_loader.get(plugin_loader.C.C_LOOKUP, 'environ', lookup_environ.LookupModule)

    config.update_setting

# Generated at 2022-06-12 20:57:05.479134
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    global_setting_str = 'str'
    global_setting_bool = False
    plugin_type = 'plugin_type'
    plugin_name = 'plugin_name'
    plugin_setting_str = 'plugin_str'

    config_data = ConfigData()

    # This should get global setting (if it exists)
    assert config_data.get_setting(global_setting_str) is None

    # This should get global setting (if it exists)
    assert config_data.get_setting(global_setting_bool) is None

    # This should get nothing
    assert config_data.get_setting('foo', plugin_type) is None

    # This should get nothing
    assert config_data.get_setting('foo', plugin_name) is None

    # This should get nothing

# Generated at 2022-06-12 20:57:09.730108
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting(name='a'))
    config_data.update_setting(Setting(name='b'), Plugin('c', 'd'))
    print(config_data._global_settings['a'].name)
    print(config_data._plugins['c']['d']['b'].name)
    assert False


# Generated at 2022-06-12 20:57:14.968833
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()

    setting1 = Setting(name="general", plugin=None)

    setting2 = Setting(name="timeout", plugin=Plugin(type="INVENTORY", name="static"))

    setting3 = Setting(name="port", plugin=Plugin(type="INVENTORY", name="static"))

    config_data.update_setting(setting1)
    config_data.update_setting(setting2)
    config_data.update_setting(setting3)

    settings = config_data.get_settings()
    assert settings[0] == setting1

    settings = config_data.get_settings(plugin=Plugin(type="INVENTORY", name="static"))
    assert settings[0] == setting2 and settings[1] == setting3


# Generated at 2022-06-12 20:57:17.193207
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()

    setting = config_data.get_setting('any name','any plugin')
    assert setting is None


# Generated at 2022-06-12 20:57:39.886257
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    import os
    from collections import namedtuple
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common._collections_compat import Mapping, Sequence

    Plugin = namedtuple('Plugin', ('name', 'type'))

    os.environ['ANSIBLE_CONFIG'] = 'test/resources/test_ansible.cfg'

    from ansible.plugins.loader import config_loader
    config_loader.load_config_file()

    config_data.update_setting(config_loader.config_file._global_settings['accelerate'])

    # Verifiy that the global setting is available
    assert config_data.get_setting('accelerate') is not None


# Generated at 2022-06-12 20:57:49.661067
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configdata = ConfigData()
    plugin1 = PluginDescriptor('foo', 'bar')
    plugin2 = PluginDescriptor('foo', 'baz')
    setting = PluginSetting('boolean', name='foo', value=True)
    plugin_setting = PluginSetting('foo', group='bar')
    configdata.update_setting(setting)
    configdata.update_setting(plugin_setting, plugin=plugin1)
    configdata.update_setting(plugin_setting, plugin=plugin2)
    assert 2 == len(configdata.get_settings())
    assert 1 == len(configdata.get_settings(plugin=plugin1))
    assert 1 == len(configdata.get_settings(plugin=plugin2))


# Generated at 2022-06-12 20:57:56.383578
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    conf = ConfigData()
    s = Setting('name', 'value')
    conf.update_setting(s, None)
    assert 'name' in conf._global_settings
    plugin = Plugin('type', 'name')
    s = Setting('name', 'value')
    conf.update_setting(s, plugin)
    assert 'type' in conf._plugins
    assert 'name' in conf._plugins['type']
    assert 'name' in conf._plugins['type']['name']


# Generated at 2022-06-12 20:57:58.659830
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    setting = list(config.get_settings())
    assert setting == [], 'The list of settings should be empty'


# Generated at 2022-06-12 20:58:01.556309
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    configData = ConfigData()
    configData._global_settings['global_setting'] = 'global_setting value'
    assert configData.get_settings()[0].name == 'global_setting'
    assert configData.get_settings()[0].value == 'global_setting value'


# Generated at 2022-06-12 20:58:03.330712
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    #TODO: create the unit test
    pass

# Generated at 2022-06-12 20:58:08.747903
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = Plugin("some-plugin", "action")
    setting = Setting("some-setting")

    assert config_data.get_setting("some-setting") is None
    config_data.update_setting(setting)
    assert config_data.get_setting("some-setting") == setting
    assert config_data.get_setting("some-setting", plugin) is None
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting("some-setting", plugin) == setting



# Generated at 2022-06-12 20:58:12.287123
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    setting = Setting(name='test_setting', value='test_value')
    config_data.update_setting(setting)
    assert config_data.get_setting('test_setting') == setting


# Generated at 2022-06-12 20:58:19.903335
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    test_config_data = ConfigData()

    # Invalid settings
    assert test_config_data.get_settings() == []

    # Add global settings
    test_config_data.update_setting(Setting('bool_setting', 'true', 'boolean', 'Default setting'))
    test_config_data.update_setting(Setting('int_setting', '42', 'integer', 'Default setting'))
    test_config_data.update_setting(Setting('str_setting', 'default value', 'string', 'Default value'))
    test_config_data.update_setting(Setting('list_setting', 'first, second, third', 'list', 'Default value'))
    test_config_data.update_setting(Setting('dict_setting', 'key1: value1, key2: value2', 'dict', 'Default value'))

   

# Generated at 2022-06-12 20:58:30.258184
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config = ConfigData()
    setting = Setting('bar_setting')
    assert config.get_setting(setting.name) is None
    config.update_setting(setting)
    assert config.get_setting(setting.name) is not None
    assert config.get_setting(setting.name).name == 'bar_setting'

    plugin = Plugin('bar_plugin', 'bar')
    setting = Setting('bar_plugin_setting', 'bar_plugin')
    assert config.get_setting(setting.name, plugin) is None
    config.update_setting(setting, plugin)
    assert config.get_setting(setting.name, plugin) is not None
    assert config.get_setting(setting.name, plugin).name == 'bar_plugin_setting'


# Generated at 2022-06-12 20:58:55.577520
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    # Test with no plugin
    data = ConfigData()
    s = Setting('A', 'V')
    data.update_setting(s)
    assert(data.get_settings() == [s])
    assert(data.get_settings(Plugin('C', 'P')) == [])
    # Test with plugin
    p = Plugin('C', 'P')
    data.update_setting(s, p)
    assert(data.get_settings() == [s])
    assert(data.get_settings(p) == [s])
    assert(data.get_settings(Plugin('C', 'P2')) == [])


# Generated at 2022-06-12 20:59:01.210727
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    plugin_type = ''
    plugin_name = ''
    plugin_version = ''
    plugin_path = ''
    plugin = Plugin(plugin_type, plugin_name, plugin_version, plugin_path);

    setting = Setting('', '')
    config_data.update_setting(setting, plugin)


# Generated at 2022-06-12 20:59:12.880392
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    data = ConfigData()
    setting1 = Setting(name='plugin_debug', value="False", origin='vars_file')
    data.update_setting(setting1)
    assert data._global_settings['plugin_debug'].name == 'plugin_debug'
    assert data._global_settings['plugin_debug'].value == "False"
    assert data._global_settings['plugin_debug'].origin == 'vars_file'
    # Adding a plugin setting
    plugin1_1 = Plugin(name='net_ping', type='network')
    setting2 = Setting(name='use_persistent_connection', value='False', origin='vars_file')
    data.update_setting(setting2, plugin1_1)

# Generated at 2022-06-12 20:59:16.757919
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    plugin = Plugin(name='plugin', type='dummy')
    setting = Setting(name='setting', value='value')
    config_data.update_setting(setting, plugin=plugin)

    assert config_data.get_setting('setting', plugin=plugin).value == 'value'


# Generated at 2022-06-12 20:59:21.040955
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    config_data = ConfigData()
    config_data.update_setting(Setting('foo', 'bar'))

    assert config_data.get_setting('foo') == Setting('foo', 'bar')


# Generated at 2022-06-12 20:59:29.824054
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    test_setting = ConfigSetting()
    test_setting.name = "TestSetting"
    test_setting.plugin = Plugin("TestPlugin", Plugin.TYPE_CALLBACK)
    cd.update_setting(test_setting)
    assert cd.get_setting("TestSetting", Plugin("TestPlugin", Plugin.TYPE_CALLBACK)) == test_setting
    assert cd.get_setting("TestSetting") == None
    test_setting = ConfigSetting()
    test_setting.name = "TestSetting"
    cd.update_setting(test_setting)
    assert cd.get_setting("TestSetting") == test_setting
    assert cd.get_setting("TestSetting", Plugin("TestPlugin", Plugin.TYPE_CALLBACK)) == None


# Generated at 2022-06-12 20:59:38.027469
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    """
    This method tests the get_settings method of the class ConfigData
    :return:
    """
    global_setting1 = GlobalSetting('a', 'b', 's', 'd')
    global_setting2 = GlobalSetting('e', 'f', 'g', 'h')
    global_setting3 = GlobalSetting('i', 'j', 'k', 'l')

    data = ConfigData()

    data.update_setting(global_setting1)
    data.update_setting(global_setting2)
    data.update_setting(global_setting3)

    test_settings1 = data.get_settings()

    assert len(test_settings1) == len(data._global_settings)
    assert test_settings1[0].name == 'a' and test_settings1[1].name == 'e' and test_settings1

# Generated at 2022-06-12 20:59:45.663629
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    # Update some settings to ConfigData
    config_data.update_setting(Setting('foo', 'global', 'global'))
    config_data.update_setting(Setting('bar', 'baz', 'global'))

    # Update some settings to ConfigData with plugin foo
    config_data.update_setting(Setting('foo', 'bar', 'foo', 'test'))
    config_data.update_setting(Setting('bar', 'foo', 'foo', 'test'))

    # Update some settings to ConfigData with plugin bar
    config_data.update_setting(Setting('foo', 'baz', 'bar', 'test'))
    config_data.update_setting(Setting('bar', 'baz', 'bar', 'test'))

    assert len(config_data.get_settings()) == 2
   

# Generated at 2022-06-12 20:59:46.624175
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    assert 1 == 1


# Generated at 2022-06-12 20:59:53.346057
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from units.compat.mock import patch, Mock
    from ansible.plugins.loader import PluginLoader

    loader = PluginLoader('connection', 'localhost')

    plugin = Mock()
    plugin.type = 'connection'
    plugin.name = loader.all()[0]

    config_data = ConfigData()
    config_data.update_setting(Setting('timeout', 30, loader.all()[0]))
    config_data.update_setting(Setting('network_os', 'ios', loader.all()[0]))
    config_data.update_setting(Setting('network_os', 'ios', 'localhost'))

    with patch.object(loader, 'all', return_value=[plugin.name]):
        assert config_data.get_setting('timeout') == 30

# Generated at 2022-06-12 21:00:33.790390
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    from units.mock.loader import DictDataLoader
    from units.plugins.test.loader import load_plugin_custom_configuration

    # Create data loader

# Generated at 2022-06-12 21:00:39.551417
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config = ConfigData()

    from ansible.config.setting import Setting
    setting = Setting('setting_name', 'value')

    config.update_setting(setting)
    assert config._global_settings['setting_name'].value == 'value'
    assert config.get_setting('setting_name').value == 'value'


# Generated at 2022-06-12 21:00:46.554007
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    c = ConfigData()
    from datetime import datetime
    s1 = Setting(name='s1', value='value1', value_type='bool',
                 origin='file', section='file', key='s1',
                 category='default')
    s2 = Setting(name='s2', value='value2', value_type='str',
                 origin='file', section='file', key='s2',
                 category='default')
    s3 = Setting(name='s3', value='value3', value_type='str',
                 origin='file', section='file', key='s3',
                 category='default')
    c.update_setting(s1)
    c.update_setting(s2)
    c.update_setting(s3)

    settings = c.get_settings()
    assert len(settings) == 3


# Generated at 2022-06-12 21:00:50.955100
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config_data = ConfigData()

    # Get settings for a plugin
    plugin = Plugin('lookup', 'passwd')
    settings = config_data.get_settings(plugin)
    assert 0 == len(settings)

    # Get settings for no plugin
    settings = config_data.get_settings()
    assert 0 == len(settings)



# Generated at 2022-06-12 21:00:53.248350
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    config_data.update_setting("general")
    assert config_data._global_settings == "general"


# Generated at 2022-06-12 21:01:04.633396
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    config_data = ConfigData()
    from collections import namedtuple
    Plugin = namedtuple('Plugin', ['name', 'type'])
    Setting = namedtuple('Setting', ['name', 'value'])
    plugin = Plugin('test', 'valid')
    setting = Setting('test', 'test-value')
    config_data.update_setting(setting, plugin)
    assert config_data.get_setting('test') is None
    assert config_data.get_setting('test', plugin) == setting
    new_setting = Setting('test', 'new-value')
    config_data.update_setting(new_setting)
    assert config_data.get_setting('test') == new_setting
    assert config_data.get_setting('test', plugin) == setting


# Generated at 2022-06-12 21:01:12.865677
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():

    from ansibullbot.config import config
    from ansibullbot.wrappers.plugin import Plugin

    cfg = ConfigData()

    p = Plugin('/path/to/ansible/ansible')
    assert p.type == 'module'
    assert p.name == 'ansible'

    assert cfg.get_settings() == []
    assert cfg.get_settings(p) == []

    cfg.update_setting(config.ConfigSetting('default_skip_labels', ['skip-ansible', 'skip-bot']), p)
    cfg.update_setting(config.ConfigSetting('default_skip_labels', ['skip-ansible', 'skip-bot']))

    assert len(cfg.get_settings()) == 2
    assert len(cfg.get_settings(p)) == 1

    assert cfg.get

# Generated at 2022-06-12 21:01:14.950472
# Unit test for method get_settings of class ConfigData
def test_ConfigData_get_settings():
    config = ConfigData()
    assert config.get_settings() == []
    assert config.get_settings(plugin) == []



# Generated at 2022-06-12 21:01:24.917864
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    from ansible.config.setting import Setting

    config_data = ConfigData()

    setting1 = Setting(name='ANSIBLE_NOCOLOR', value='True')

    # update global setting
    config_data.update_setting(setting1, None)
    assert config_data._global_settings.get('ANSIBLE_NOCOLOR') == setting1

    # update setting from test_callback plugin
    from ansible.plugins.callback import CallbackBase
    test_callback = CallbackBase()
    test_callback.type = 'callback'
    test_callback.name = 'test_callback'
    setting2 = Setting(name='test_setting', value='test')
    config_data.update_setting(setting2, test_callback)

# Generated at 2022-06-12 21:01:29.706328
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    conf = ConfigData()
    conf.update_setting('first plugin')
    conf.update_setting('second plugin')
    conf.update_setting('third plugin')

# Generated at 2022-06-12 21:02:42.042352
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():
    cd = ConfigData()
    cd.update_setting(Setting(name="test1", value="testvalue1"))
    assert(cd.get_setting("test1").name == "test1")
    assert(cd.get_setting("test1").value == "testvalue1")

    cd.update_setting(Setting(name="test2", value="testvalue2"), Plugin(name="test"))
    assert(cd.get_setting("test2").name == "test2")
    assert(cd.get_setting("test2").value == "testvalue2")
    assert(cd.get_setting("test2", Plugin(name="test")).name == "test2")
    assert(cd.get_setting("test2", Plugin(name="test")).value == "testvalue2")


# Generated at 2022-06-12 21:02:52.253463
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    config_data = ConfigData()
    assert config_data.get_settings() == []
    assert config_data.get_setting('PLUGIN_PATH') is None

    setting = Setting(name='PLUGIN_PATH', value='/usr/share/ansible/plugins')
    config_data.update_setting(setting)
    assert config_data.get_settings() == [setting]
    assert config_data.get_setting('PLUGIN_PATH') == setting

    setting = Setting(name='PLUGIN_PATH', value='/usr/local/share/ansible/plugins')
    config_data.update_setting(setting)
    assert config_data.get_setting('PLUGIN_PATH') == setting


# Generated at 2022-06-12 21:03:00.513075
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # Test: Get non-existent global setting
    assert config_data.get_setting('some setting') is None

    # Test: Get non-existent local setting
    assert config_data.get_setting('some setting', 'some/plugin') is None

    # Test: Update a global setting
    global_setting = {'name': 'some setting', 'value': 'some value'}
    config_data.update_setting(global_setting)
    assert config_data.get_setting('some setting') == global_setting

    # Test: Update a local setting
    local_setting = {'name': 'some setting', 'value': 'some other value'}
    config_data.update_setting(local_setting, 'some/plugin')

# Generated at 2022-06-12 21:03:10.852772
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():
    setting_name = 'foo'
    config_data = ConfigData()

    setting1 = Setting(name=setting_name)
    config_data.update_setting(setting1)

    setting2 = Setting(name='bar')
    config_data.update_setting(setting2)

    setting3 = Setting(name=setting_name)
    plugin = Plugin(type='bar', name='foo')
    config_data.update_setting(setting3, plugin)

    setting_expected = setting1
    setting_actual = config_data.get_setting(setting_name)
    assert setting_expected == setting_actual
    assert setting_actual == setting1
    assert setting_actual == setting2


# Generated at 2022-06-12 21:03:20.531857
# Unit test for method update_setting of class ConfigData
def test_ConfigData_update_setting():

    # Creating ConfigData. Currently no data is stored.
    config_data = ConfigData()

    # Updating ConfigData with setting.
    setting = { 'name' : 'setting_1', 'origin' : 'origin_1' }
    config_data.update_setting(setting)

    # Updating ConfigData with another setting.
    setting = { 'name' : 'setting_2', 'origin' : 'origin_1' }
    config_data.update_setting(setting)

    # Global_setting dictionary will be:
    # global_setting = { 'setting_1' : { 'name' : 'setting_1', 'origin' : 'origin_1', 'plugin': None },
    #                    'setting_2' : { 'name' : 'setting_2', 'origin' : 'origin_1', 'plugin': None } }
   

# Generated at 2022-06-12 21:03:30.377895
# Unit test for method get_setting of class ConfigData
def test_ConfigData_get_setting():

    config_data = ConfigData()

    # initialize global_settings with a key
    global_settings = {}
    global_settings['key'] = 'value'
    config_data._global_settings = global_settings

    # get value for key 'key' with plugin being None
    assert config_data.get_setting('key') == 'value'

    # initialize plugins
    plugins = {}
    plugins['type'] = {}
    plugins['type']['name'] = {}
    plugins['type']['name']['key'] = 'value'
    config_data._plugins = plugins

    # get value for key 'key' with plugin being defined
    assert config_data.get_setting('key', {'type': 'type', 'name': 'name'}) == 'value'
