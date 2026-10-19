

# Generated at 2022-06-13 22:33:20.521933
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONPBFormatter, JSONFormatter, URLEncodedFormatter
    plugin_manager = PluginManager()
    plugin_manager.register(JSONPBFormatter, JSONFormatter, URLEncodedFormatter)
    formatters_grouped = plugin_manager.get_formatters_grouped()
    print(formatters_grouped)

# Generated at 2022-06-13 22:33:23.407534
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugin = plugins.get_formatters()[0]
    plugins.unregister(plugin)
    assert plugin not in plugins

# Generated at 2022-06-13 22:33:30.490292
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()

    plugin = plugins.get_auth_plugin('basic')
    assert plugin.name == 'Basic Auth'
    assert plugin.auth_type == 'basic'
    assert plugin.description == 'Basic HTTP authentication'
    assert plugin.help == 'Basic HTTP authentication'
    assert plugin.package_name == 'httpie'

    plugin = plugins.get_auth_plugin('digest')
    assert plugin.name == 'Digest Auth'
    assert plugin.auth_type == 'digest'
    assert plugin.description == 'Digest HTTP authentication'
    assert plugin.help == 'Digest HTTP authentication'
    assert plugin.package_name == 'httpie'

    plugin = plugins.get_auth_plugin('hawk')
    assert plugin.name == 'Hawk Auth'
    assert plugin

# Generated at 2022-06-13 22:33:40.327639
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Instantiate an object of the class PluginManager
    mgr = PluginManager()
    # Register some plugins
    from httpie.plugins import builtin
    mgr.register(builtin.HTTPBasicAuthPlugin)
    mgr.register(builtin.FormatterPlugin)
    # Assert that the method filter returns the expected result
    assert mgr.filter() == [builtin.HTTPBasicAuthPlugin, builtin.FormatterPlugin]
    assert mgr.filter(AuthPlugin) == [builtin.HTTPBasicAuthPlugin]
    assert mgr.filter(FormatterPlugin) == [builtin.FormatterPlugin]

# Generated at 2022-06-13 22:33:44.318641
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import sys, os
    sys.path.insert(0, os.path.abspath('..'))
    from httpie.plugins.formatter.v1 import FormatterPlugin
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_formatters() == [FormatterPlugin]


# Generated at 2022-06-13 22:33:46.961202
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    assert type(plugins.filter()) == list

# Generated at 2022-06-13 22:33:54.163960
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.register(Auth1, Auth2)
    expected_mapping = {'AuthType1': Auth1, 'AuthType2': Auth2}
    actual_mapping = plugin_manager.get_auth_plugin_mapping()
    assert expected_mapping[0] == actual_mapping[0] and \
           expected_mapping[1] == actual_mapping[1]

# Generated at 2022-06-13 22:33:55.864219
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pass


plugins = PluginManager()

# Generated at 2022-06-13 22:33:58.119888
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    return manager

# Generated at 2022-06-13 22:34:02.067840
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter(AuthPlugin) == []
    assert PluginManager().filter(FormatterPlugin) == []
    assert PluginManager().filter(ConverterPlugin) == []
    assert PluginManager().filter(TransportPlugin) == []

    return True


# Generated at 2022-06-13 22:34:11.274339
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) != 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:34:16.838696
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    from httpie.plugins.builtin import AuthPlugin
    from httpie.plugins.argtypes import auth_type
    from httpie.plugins.builtin import auth_basic
    manager.register(AuthPlugin)
    assert manager.filter(AuthPlugin) == [AuthPlugin]



# Generated at 2022-06-13 22:34:24.453486
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import RadioFormatter, HeadersFormatter
    print(JSONFormatter.group_name)
    print(RadioFormatter.group_name)
    print(HeadersFormatter.group_name)
    plugin_manager = PluginManager()
    plugins = plugin_manager.get_formatters_grouped()
    # plugins = plugin_manager.get_formatters()
    print(plugins)



# Generated at 2022-06-13 22:34:25.503959
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    print(PluginManager.filter)

# Generated at 2022-06-13 22:34:31.349276
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    formatter_grouped = plugin_manager.get_formatters_grouped()
    assert type(formatter_grouped) is dict
    assert formatter_grouped.get('json') is not None
    assert formatter_grouped.get('table') is not None
    assert formatter_grouped.get('html') is not None
    assert formatter_grouped.get('colors') is not None

# Generated at 2022-06-13 22:34:38.001205
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class A(FormatterPlugin):
        group_name = 'B'
    class B(FormatterPlugin):
        group_name = 'B'
    class C(FormatterPlugin):
        group_name = 'C'
    
    plugins = PluginManager()
    plugins.register(A, B, C)
    
    assert plugins.get_formatters_grouped() == {
        'B': [A, B],
        'C': [C],
    }

# Generated at 2022-06-13 22:34:41.023727
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0


# Generated at 2022-06-13 22:34:43.820256
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters_grouped = plugin_manager.get_formatters_grouped()


# Generated at 2022-06-13 22:34:47.277960
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth, BasicAuth
    pm = PluginManager()
    pm.register(HTTPBasicAuth, BasicAuth)
    assert len(pm.filter(AuthPlugin)) == 2
    assert len(pm.filter(TransportPlugin)) == 0


# Generated at 2022-06-13 22:34:58.294766
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Plugin1(FormatterPlugin):
        group_name = 'test_group'
        name = '1'
    class Plugin2(FormatterPlugin):
        group_name = 'test_group'
        name = '2'
    class Plugin3(FormatterPlugin):
        group_name = 'another_test_group'
        name = '3'

    manager = PluginManager()
    manager.register(Plugin1, Plugin2, Plugin3)
    expected_result = {
        'test_group': [Plugin1, Plugin2],
        'another_test_group': [Plugin3]
    }
    assert manager.get_formatters_grouped() == expected_result

# Generated at 2022-06-13 22:35:06.193030
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm1 = PluginManager()
    list1 = [('a', 'A'), ('b', 'B'), ('a', 'C')]
    pm1.register(list1)
    assert pm1.get_auth_plugin_mapping() == {'a': 'C', 'b': 'B'}

# Generated at 2022-06-13 22:35:17.329770
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    auth_plugins = plugin_manager.get_auth_plugins()
    assert auth_plugins[0].auth_type == 'basic'
    assert auth_plugins[0].package_name == 'httpie-ntlm'
    assert auth_plugins[1].auth_type == 'digest'
    assert auth_plugins[1].package_name == 'httpie-digest-auth'
    formatters = plugin_manager.get_formatters()
    assert formatters[0].package_name == 'httpie-json-ascii'

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:35:27.284577
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    Test if the method self.get_formatters_grouped() of the class PluginManager
    works correctly. 
    """
    from httpie.plugins import httpie_plugins
    formatter_list = []
    
    # Get the formatters, and sort them by their group_name
    result = httpie_plugins.get_formatters_grouped()
    assert list(result.keys()) == ['group1', 'group2']
    
    # Test the formatters in group1
    formatter_list.append(result['group1'][0])
    formatter_list.append(result['group1'][1])
    assert formatter_list[0].name == 'FormatterOne'
    assert formatter_list[1].name == 'FormatterTwo'
    
    # Test the formatters in group2
   

# Generated at 2022-06-13 22:35:30.045264
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.register(TransportPlugin)
    plugin_manager.register(AuthPlugin)
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 2, \
        'The number of plugins should be greater than 2, but it is {}'\
        .format(str(len(plugin_manager)))


# Generated at 2022-06-13 22:35:37.636236
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import ConverterPlugin, FormatterPlugin, BasePlugin, TransportPlugin
    from httpie.plugins import AuthPlugin
    from httpie.plugins.base import BasePlugin
    pluginManager = PluginManager()

    list_test = [BasePlugin, FormatterPlugin, AuthPlugin, \
        ConverterPlugin, BasePlugin, TransportPlugin]
    pluginManager.register(*list_test)
    assert pluginManager.filter(AuthPlugin) == [AuthPlugin]
    assert pluginManager.filter(FormatterPlugin) == [FormatterPlugin]
    assert pluginManager.filter(ConverterPlugin) == [ConverterPlugin]
    assert pluginManager.filter(TransportPlugin) == [TransportPlugin]
    assert pluginManager.filter() == list_test[1:]



# Generated at 2022-06-13 22:35:50.531787
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:35:56.564144
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    
    formatter_groups = pluginManager.get_formatters_grouped()
    for group in formatter_groups:
        for plugin in formatter_groups[group]:
            print("{} {}".format(group, plugin.name))


# Generated at 2022-06-13 22:36:00.953937
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Create instance of class PluginManager
    plugin_manager = PluginManager()
    
    # Check to see that plugin_manager is an instance of PluginManager
    assert isinstance(plugin_manager, PluginManager)
    
    # Load installed plugins 
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:36:05.345765
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(AuthPlugin)
    pm.register(FormatterPlugin)
    assert list(pm.filter(AuthPlugin)) == [AuthPlugin]
    assert list(pm.filter(FormatterPlugin)) == [FormatterPlugin]



# Generated at 2022-06-13 22:36:13.656952
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert isinstance(pm, PluginManager)
    pm.get_auth_plugin('basic')
    pm.get_auth_plugin('digest')
    pm.get_auth_plugin('hawk')
    pm.get_auth_plugin('gssnegotiate')
    pm.get_auth_plugin('oauth1')
    pm.get_auth_plugin('ntlm')
    pm.get_auth_plugin('aws4-hmac-sha256')
    pm.get_converters()
    pm.get_formatters()
    pm.get_formatters_grouped()
    pm.get_transport_plugins()

# Generated at 2022-06-13 22:36:27.856393
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Given
    pm = PluginManager()
    pm.append(PluginManager)
    pm.append(Type)
    pm.append(List)
    # When
    TypeList = pm.filter(Type)
    # Then
    assert len(TypeList) == 2
    assert TypeList[0] == Type
    assert TypeList[1] == List


# Generated at 2022-06-13 22:36:34.947735
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    # Initialization of plugin manager
    plugin_manager = PluginManager()

    # Get the installed plugins
    plugin_manager.load_installed_plugins()

    # Get the list of plugins
    plugins = plugin_manager.get_auth_plugins()

    # Check whether the loading of plugins is right or not
    if not plugins:
        raise Exception('[+] Plugins not found!')
    else:
        print('[+] Plugins successfully loaded!')

# TODO: Test and comment methods below

# if __name__ == "__main__":
#     test_PluginManager_load_installed_plugins()

# Method which returns the plugin according to a given format

# Generated at 2022-06-13 22:36:37.469126
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert not len(plugin_manager) == 0


# Generated at 2022-06-13 22:36:42.655773
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    l = plugin_manager.filter(by_type=Type[BasePlugin])
    assert len(l) == 0
    plugin_manager.load_installed_plugins()
    l = plugin_manager.filter(by_type=Type[BasePlugin])
    assert len(l) > 0

# Generated at 2022-06-13 22:36:46.387730
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()

    assert plugins

    for entry_point_name in ENTRY_POINT_NAMES:
        assert any(entry_point.load() in plugins for entry_point in iter_entry_points(entry_point_name))

# Generated at 2022-06-13 22:36:48.236225
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.register(AuthPlugin)
    assert False


plugins = PluginManager()

# Generated at 2022-06-13 22:36:52.944253
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mgr = PluginManager()
    mgr.load_installed_plugins()

    assert len(mgr) > 0
    assert len(mgr.get_auth_plugins()) > 0
    assert len(mgr.get_formatters()) > 0

# Generated at 2022-06-13 22:37:08.666392
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class FormatterBase(FormatterPlugin):
        group_name = 'BASE'

    class Plugin1(FormatterBase):
        group_name = 'B'

    class Plugin2(FormatterBase):
        group_name = 'A'

    class Plugin3(FormatterBase):
        group_name = 'B'

    class Plugin4(FormatterBase):
        group_name = 'A'

    class Plugin5(FormatterBase):
        group_name = 'C'

    class Plugin_extra(FormatterPlugin):
        group_name = 'BASE'

    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3, Plugin4, Plugin5, Plugin_extra)


# Generated at 2022-06-13 22:37:22.445961
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # load_installed_plugins(self)

    manager = PluginManager()
    manager.load_installed_plugins() # Installed plugins

    # Add own plugins
    manager.register(type('MyFormatter', (FormatterPlugin, ), {'name': 'myformat'}))

    assert type(manager) == PluginManager
    # assert len(manager) > 0 # No assert here because it will not work with PyPI packages
    assert type(manager.get_auth_plugins()) == list
    assert type(manager.get_auth_plugin_mapping()) == dict
    assert type(manager.get_auth_plugin('basic')) == type
    assert type(manager.get_formatters()) == list
    assert type(manager.get_formatters_grouped()) == dict
    assert type(manager.get_converters()) == list
    assert type

# Generated at 2022-06-13 22:37:30.157857
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    assert pm.get_formatters_grouped() == {}
    pm = PluginManager()
    pm.register(FormatterPlugin)
    assert pm.get_formatters_grouped() == {'default': [FormatterPlugin]}
    pm = PluginManager()
    pm.register(FormatterPlugin, FormatterPlugin)
    assert pm.get_formatters_grouped() == \
        {'default': [FormatterPlugin, FormatterPlugin]}
    pm = PluginManager()
    pm.register(FormatterPlugin, FormatterPlugin2, FormatterPlugin)
    assert pm.get_formatters_grouped() == \
        {'default': [FormatterPlugin, FormatterPlugin], 'default2': [FormatterPlugin2]}
    pm = PluginManager()

# Generated at 2022-06-13 22:37:49.536445
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert(pluginManager)


# Generated at 2022-06-13 22:37:51.694559
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    #test
    plugins = PluginManager()
    #assert
    assert plugins.get_auth_plugin_mapping() == {}


# Generated at 2022-06-13 22:37:53.481238
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PlugMan = PluginManager()
    PlugMan.load_installed_plugins()
    print(PlugMan.get_auth_plugin_mapping())


# Generated at 2022-06-13 22:37:55.606767
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    p = PluginManager()
    assert(isinstance(p.get_auth_plugin_mapping(), dict))


# Generated at 2022-06-13 22:37:59.185563
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0
    assert len(pm.get_auth_plugins()) > 0
    assert len(pm.get_formatters()) > 0
    assert len(pm.get_converters()) > 0
    assert len(pm.get_transport_plugins()) > 0



# Generated at 2022-06-13 22:38:03.804944
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin, FormatterPlugin)
    assert isinstance(plugin_manager, PluginManager)
    assert isinstance(plugin_manager.get_formatters_grouped(), dict)



# Generated at 2022-06-13 22:38:06.491877
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert (len(plugins)) == 15


# Generated at 2022-06-13 22:38:11.830430
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm.filter(AuthPlugin)) != 0
    assert len(pm.filter(ConverterPlugin)) != 0
    assert len(pm.filter(FormatterPlugin)) != 0
    assert len(pm.filter(TransportPlugin)) != 0

# Generated at 2022-06-13 22:38:15.251407
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    m = PluginManager()
    m.load_installed_plugins()
    formatters = m.get_formatters_grouped()
    assert 'Basic formatters' in formatters
    assert 'Composite formatters' in formatters
    assert 'Syntax highlighting' in formatters
    assert 'Options' in formatters

# Generated at 2022-06-13 22:38:24.480848
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Plugins
    class Plugin1(FormatterPlugin):
        group_name = 'foo'

    class Plugin2(FormatterPlugin):
        group_name = 'foo'

    class Plugin3(FormatterPlugin):
        group_name = 'bar'

    # Create PluginManager object
    p = PluginManager()

    # Register plugins
    p.register(Plugin1, Plugin2, Plugin3)

    # Get formatters grouped
    assert p.get_formatters_grouped() == {
        'foo': [Plugin1, Plugin2],
        'bar': [Plugin3],
    }

# Generated at 2022-06-13 22:38:59.176872
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import converter, formatter, script

    manager = PluginManager()
    manager.load_installed_plugins()
    manager.load_installed_plugins()  # Run twice

    # These are loaded by default.
    assert converter.JSONConverter in manager
    assert formatter.JSONFormatter in manager
    assert script.ScriptPlugin in manager

    # Ensure that the same plugin is not registered twice.
    assert manager.count(script.ScriptPlugin) == 1

# Generated at 2022-06-13 22:39:09.714270
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(
        type('ConverterPluginA', (BasePlugin,), {}),
        type('ConverterPluginB', (BasePlugin,), {}),
        type('TransportPluginA', (BasePlugin,), {}),
        type('TransportPluginB', (BasePlugin,), {}),
    )

    converter_plugins = plugin_manager.filter(ConverterPlugin)
    assert len(converter_plugins) == 2
    assert all(isinstance(plugin, ConverterPlugin) for plugin in converter_plugins)

    transport_plugins = plugin_manager.filter(TransportPlugin)
    assert len(transport_plugins) == 2
    assert all(isinstance(plugin, ConverterPlugin) for plugin in converter_plugins)

# Generated at 2022-06-13 22:39:11.477835
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:39:16.371436
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager.get_formatters_grouped()) == 1
    assert len(manager.get_formatters_grouped()['output.formatters.cli']) == 1
    assert len(manager.get_converters()) == 1

manager = PluginManager()

# Generated at 2022-06-13 22:39:26.427050
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_PluginManager = PluginManager()
    test_PluginManager.load_installed_plugins()
    assert isinstance(test_PluginManager.get_formatters_grouped(), dict)
    assert 'default' in test_PluginManager.get_formatters_grouped().keys()
    assert 'json' in test_PluginManager.get_formatters_grouped().keys()
    assert 'html' in test_PluginManager.get_formatters_grouped().keys()
    assert 'templated' in test_PluginManager.get_formatters_grouped().keys()


# Generated at 2022-06-13 22:39:32.653342
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    for group_name in ['Form', 'Pretty', 'Syntax']:
        assert group_name in plugins.get_formatters_grouped().keys()
        assert len(plugins.get_formatters_grouped()[group_name]) > 0

# Generated at 2022-06-13 22:39:38.310950
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    from httpie.plugins.manager import ENTRY_POINT_NAMES
    for entry_point_name in ENTRY_POINT_NAMES:
        for entry_point in iter_entry_points(entry_point_name):
            plugin = entry_point.load()
            plugin.package_name = entry_point.dist.key
            manager.register(entry_point.load())

# Generated at 2022-06-13 22:39:42.880281
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager)

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:39:53.231143
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    cls1 = type('Plugin1', (), {})
    cls2 = type('Plugin2', (), {})
    cls3 = type('Plugin3', (), {})
    cls4 = type('Plugin4', (), {})
    cls5 = type('Plugin5', (), {})

    cls1.group_name = 'group1'
    cls2.group_name = 'group1'
    cls3.group_name = 'group2'
    cls4.group_name = 'group2'
    cls5.group_name = 'group3'

    manager = PluginManager()
    manager.register(cls1, cls2, cls3, cls4, cls5)
    # Test for all

# Generated at 2022-06-13 22:40:00.440216
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # generate some test data
    class FormatterPlugin_test0(FormatterPlugin):
        pass
    FormatterPlugin_test0.group_name = 'group1'

    class FormatterPlugin_test1(FormatterPlugin):
        group_name = 'group1'

    class FormatterPlugin_test2(FormatterPlugin):
        group_name = 'group2'

    class FormatterPlugin_test3(FormatterPlugin):
        group_name = 'group1'

    class FormatterPlugin_test4(FormatterPlugin):
        group_name = 'group1'

    class FormatterPlugin_test5(FormatterPlugin):
        group_name = 'group2'

    # create a plugin manager and register with the test data
    pm = PluginManager()

# Generated at 2022-06-13 22:41:07.165689
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = [
        type('Group1_Plugin1', (FormatterPlugin,), {'group_name': 'group1'}),
        type('Group2_Plugin1', (FormatterPlugin,), {'group_name': 'group2'}),
        type('Group2_Plugin2', (FormatterPlugin,), {'group_name': 'group2'}),
        type('Group1_Plugin2', (FormatterPlugin,), {'group_name': 'group1'}),
    ]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)
    actual = plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:41:09.522182
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plg_mng = PluginManager()
    plg_mng.load_installed_plugins()

# Generated at 2022-06-13 22:41:22.116730
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    groupedFormatter = pluginManager.get_formatters_grouped()
    # print(groupedFormatter)
    assert len(groupedFormatter) > 0
    assert "Debug" in groupedFormatter.keys()
    assert "Color" in groupedFormatter.keys()
    assert "Syntax" in groupedFormatter.keys()
    assert "Format" in groupedFormatter.keys()
    assert "Beautify" in groupedFormatter.keys()
    assert "Compact" in groupedFormatter.keys()
    assert "Formatters" in groupedFormatter.keys()
    assert "HTTPie" in groupedFormatter.keys()
    assert "Extra" in groupedFormatter.keys()
    assert "Summary" in groupedFormatter.keys()

# Generated at 2022-06-13 22:41:29.302930
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # given
    manager=PluginManager()

    test_mapping={
        'basic': BasicAuthPlugin(),
        'digest': DigestAuthPlugin()
    }

    # when
    manager.register(DigestAuthPlugin())
    manager.register(BasicAuthPlugin())

    assert test_mapping == manager.get_auth_plugin_mapping()



# Generated at 2022-06-13 22:41:37.976702
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    pm_class_list = [
        plugin.__module__ + ':' + plugin.__name__
        for plugin in pm
    ]
    assert  'httpie_http2:HTTP2Plugin' in pm_class_list
    assert  'httpie_aws_authv4:AWSv4AuthPlugin' in pm_class_list
    assert  'httpie_digest_auth:DigestAuthPlugin' in pm_class_list
    assert  'httpie_json:JSONFormatPlugin' in pm_class_list
    assert  'jsonpatch:JSONPatchPlugin' in pm_class_list
    assert  'httpie_mock_adapter:MockAdapter' in pm_class_list

# Generated at 2022-06-13 22:41:47.372651
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """Unit test for method get_formatters_grouped of class PluginManager"""
    plugin_manager = PluginManager()

# Generated at 2022-06-13 22:41:52.426020
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugins = plugin_manager.get_auth_plugin_mapping()
    assert len(plugins) == 0

    plugin_manager.register(MyPlugin)
    plugins = plugin_manager.get_auth_plugin_mapping()
    assert "my-plugin" in plugins
    assert plugins.get("my-plugin") is MyPlugin


# Generated at 2022-06-13 22:41:54.447002
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins_ = PluginManager()
    plugins_.load_installed_plugins()
    print(plugins_.get_formatters_grouped())

# Generated at 2022-06-13 22:42:03.876270
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import mock
    import httpie.plugins

    PluginManager().load_installed_plugins()

    assert httpie.plugins.__all__ == []

    import httpie.plugins

    PluginManager().load_installed_plugins()

    assert httpie.plugins.__all__ == []

    import os
    from unittest import TestCase

    with mock.patch('pkg_resources.iter_entry_points') as mocked:
        mocked.return_value = [
            mock.Mock(dist=mock.Mock(key='test.auth'),
                      load=mock.Mock(return_value=AuthPlugin))
        ]
        PluginManager().load_installed_plugins()

        assert httpie.plugins.__all__ == ['test.auth']
        assert httpie.plugins.test.auth.__all__ == ['AuthPlugin']

    #

# Generated at 2022-06-13 22:42:06.800086
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.register(mock.Mock)
    pm.load_installed_plugins()
    assert len(pm) == len(ENTRY_POINT_NAMES) + 1