

# Generated at 2022-06-13 22:33:18.419274
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # Assuming that there are 24 plugins installed in the system
    assert len(plugin_manager) == 24


# Generated at 2022-06-13 22:33:21.902070
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 5
    for plugin in plugin_manager:
        assert plugin.package_name.startswith('httpie-')

# Generated at 2022-06-13 22:33:24.685928
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PM = PluginManager()
    dict_AuthPlugin = PM.get_auth_plugin_mapping()
    print(dict_AuthPlugin)
    return



# Generated at 2022-06-13 22:33:30.934252
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    for plugin in pm.filter(Type[BasePlugin]):
        print(plugin)

if __name__ == '__main__':
    pm = PluginManager()
    pm.load_installed_plugins()
    for entry_point_name in ENTRY_POINT_NAMES:
        for entry_point in iter_entry_points(entry_point_name):
            plugin = entry_point.load()
            plugin.package_name = entry_point.dist.key
            pm.register(entry_point.load())

    print('print plugins')
    print(pm)
    print('print plugins filter BasePlugin')
    print(pm.filter(Type[BasePlugin]))

    print('print plugins filter AuthPlugin')
    print(pm.get_auth_plugins())


# Generated at 2022-06-13 22:33:39.591371
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie import plugins
    from httpie.plugins.auth import basic_auth, digest_auth
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth
    manager = PluginManager()
    manager.register(basic_auth.BasicAuthPlugin, HTTPBasicAuth)
    manager.register(digest_auth.DigestAuthPlugin, HTTPDigestAuth)
    assert manager.get_auth_plugin_mapping() == {
        'basic': HTTPBasicAuth,
        'digest': HTTPDigestAuth
    }

# Generated at 2022-06-13 22:33:43.878572
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(FooFormatter, BarFormatter)
    assert pm.get_formatters_grouped() == {
        'Foo': [FooFormatter],
        'Bar': [BarFormatter],
    }



# Generated at 2022-06-13 22:33:49.173642
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # list of installed plugins
    print(plugin_manager)


if __name__ == "__main__":
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:34:00.204145
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.builtin import RawJSONFormatterPlugin
    from httpie.plugins.builtin import PrettyJSONFormatterPlugin

    plugins = [JSONFormatterPlugin, RawJSONFormatterPlugin, PrettyJSONFormatterPlugin]

    manager = PluginManager()
    manager.extend(plugins)

    actual = manager.get_formatters_grouped()
    expected = {
        'JSON': [JSONFormatterPlugin, RawJSONFormatterPlugin, PrettyJSONFormatterPlugin],
        'Web Browser': [],
        'Syntax Highlighting': [],
    }

    assert actual == expected


# Generated at 2022-06-13 22:34:11.698697
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(type('default', (FormatterPlugin,), {}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': None}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': ''}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': 'A'}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': 'A'}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': 'B'}))
    plugin_manager.register(type('default', (FormatterPlugin,), {'group_name': 'C'}))


# Generated at 2022-06-13 22:34:16.224942
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Given
    class Plugin(BasePlugin):
        pass

    manager = PluginManager()
    manager.register(Plugin)

    # When
    result = manager.filter(by_type=Plugin)

    # Then
    assert list(result) == [Plugin]

# Generated at 2022-06-13 22:34:22.935390
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    auths = pm.filter(AuthPlugin)
    if not auths:
        print("\nUnit test for method filter of class PluginManager has failed\n")
    else:
        print("\nUnit test for method filter of class PluginManager has succeeded\n")


# Generated at 2022-06-13 22:34:31.174808
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class BasePlugin:
        pass
    class PluginX(BasePlugin):
        pass
    class PluginY(BasePlugin):
        pass
    class PluginZ:
        pass
    plugin_manager = PluginManager()
    plugin_manager.register(PluginX, PluginY, PluginZ)
    assert plugin_manager.filter(PluginX) == [PluginX]
    assert plugin_manager.filter(PluginY) == [PluginY]
    assert plugin_manager.filter(PluginZ) == [PluginZ]
    assert plugin_manager.filter(BasePlugin) == [PluginX, PluginY]


# Generated at 2022-06-13 22:34:34.621681
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    # check whether plugins have been properly loaded
    assert len(plugin_manager) > 0


# Generated at 2022-06-13 22:34:47.388069
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Setup
    from httpie import ExitStatus
    class JSONFormatterPlugin(FormatterPlugin):
        group_name = 'json'
        output_format = 'json'
    class ColoredJSONFormatterPlugin(FormatterPlugin):
        group_name = 'json'
        output_format = 'json'
    class JSONFormatterPlugin2(FormatterPlugin):
        group_name = 'json'
        output_format = 'json'
    plugins = PluginManager()
    plugins.register(JSONFormatterPlugin, ColoredJSONFormatterPlugin, JSONFormatterPlugin2)
    # Test
    x = plugins.get_formatters_grouped()

# Generated at 2022-06-13 22:34:50.237621
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == len(ENTRY_POINT_NAMES)

# Generated at 2022-06-13 22:34:57.758282
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager_test = PluginManager()
    plugin_manager_test.register(
        Plugin_Test_1,
        Plugin_Test_2
    )
    auth_plugin_mapping_test = plugin_manager_test.get_auth_plugin_mapping()
    assert isinstance(auth_plugin_mapping_test, dict)
    assert auth_plugin_mapping_test['plugin_test'] == Plugin_Test_1


# Generated at 2022-06-13 22:35:08.608844
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    auth_plugin_mapping = PluginManager().get_auth_plugin_mapping()

# Generated at 2022-06-13 22:35:10.435563
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    assert PluginManager().get_auth_plugin_mapping() == {}

# Generated at 2022-06-13 22:35:21.529698
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    assert isinstance(pm, list)
    assert '<PluginManager: []>' == str(pm)
    class pl1(BasePlugin):
        auth_type = 'pl1'
    class pl2(BasePlugin):
        auth_type = 'pl2'
    pm.register(pl1, pl2)
    assert '<PluginManager: [__main__.pl1, __main__.pl2]>' == str(pm)
    assert {'pl1': pl1, 'pl2': pl2} == pm.get_auth_plugin_mapping()
    assert pm.get_auth_plugin('pl1') == pl1
    assert pm.get_auth_plugin('pl2') == pl2

# Generated at 2022-06-13 22:35:36.174962
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.base import BasePlugin
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.plugins import AuthPlugin, FormatterPlugin
    from httpie.plugins.builtin import (
        HTTPBasicAuth,
        HTTPTokenAuth,
        KeyValueFormatter,
    )

    plugin_manager = PluginManager()

    plugin_manager.register(HTTPiePlugin, HTTPBasicAuth, HTTPTokenAuth, KeyValueFormatter)
    plugin_manager.load_installed_plugins()
    auth_plugins = plugin_manager.filter(AuthPlugin)
    assert len(auth_plugins) == 2
    formatter_plugins = plugin_manager.filter(FormatterPlugin)
    assert len(formatter_plugins) == 2
    all_plugins = plugin_manager.filter(BasePlugin)

# Generated at 2022-06-13 22:35:52.107398
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    plugins = [i.__name__ for i in plugins]
    assert "AutomaticAuthPlugin" in plugins
    assert "AliasPlugin" in plugins
    assert "AuthPlugin" in plugins
    assert "ConverterPlugin" in plugins
    assert "DownloaderPlugin" in plugins
    assert "DownloadPlugin" in plugins
    assert "FormatterPlugin" in plugins
    assert "H2cPlugin" in plugins
    assert "H2Plugin" in plugins
    assert "JSONFormatPlugin" in plugins
    assert "JSONPlugin" in plugins
    assert "PrettyPlugin" in plugins
    assert "SessionPlugin" in plugins
    assert "TransportPlugin" in plugins
    assert "UnixSocketPlugin" in plugins


if __name__ == "__main__":
    test_PluginManager_load_

# Generated at 2022-06-13 22:36:01.671348
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.get_formatters_grouped().get('BlaBlaBla') is None
    assert 'cli' in manager.get_formatters_grouped().keys()
    assert 'json' in manager.get_formatters_grouped().keys()
    assert 'pretty' in manager.get_formatters_grouped().keys()
    assert 'table' in manager.get_formatters_grouped().keys()
    assert 'colors' in manager.get_formatters_grouped().keys()

# Generated at 2022-06-13 22:36:13.116151
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import AUTH_PLUGIN_MAP, FORMATTERS

    pm = PluginManager()

    # Load installed plugins
    pm.load_installed_plugins()

    # Verify the objects AUTH_PLUGIN_MAP and FORMATTERS
    assert {plugin.auth_type: plugin for plugin in pm.get_auth_plugins()} == AUTH_PLUGIN_MAP
    assert {
        group_name: list(group)
        for group_name, group
        in groupby(pm.get_formatters(), key=attrgetter('group_name'))
    } == FORMATTERS

# Generated at 2022-06-13 22:36:18.817135
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    class a():pass
    class b():pass
    class c(a):pass
    class d():pass
    class e(a):pass
    class f():pass
    plugin_manager.register(a,b,c,d,e,f)
    assert plugin_manager.filter(a) == [a,c,e]

# Generated at 2022-06-13 22:36:24.014596
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    color = Color()
    pm = PluginManager()
    pm.register(colors.Bash, colors.Color, colors.Windows)
    expected = {'Colors': [colors.Color], 'Compat': [colors.Windows, colors.Bash]}
    actual = pm.get_formatters_grouped()
    assert expected == actual

# Generated at 2022-06-13 22:36:32.499635
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    class Plugin1(BasePlugin):
        pass

    class Plugin2(BasePlugin):
        pass

    class Plugin3(BasePlugin):
        pass

    class Plugin4(BasePlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3, Plugin4)

    assert plugin_manager.filter() == [Plugin1, Plugin2, Plugin3, Plugin4]
    assert plugin_manager.filter(AuthPlugin) == []
    assert plugin_manager.filter(FormatterPlugin) == []
    assert plugin_manager.filter(ConverterPlugin) == []
    assert plugin_manager.filter(TransportPlugin) == []



# Generated at 2022-06-13 22:36:36.323057
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Setup
    plugins_manager = PluginManager()
    # Exercise
    formatters_grouped = plugins_manager.get_formatters_grouped()
    # Verify
    assert isinstance(formatters_grouped, dict)
    assert formatters_grouped.pop('common')
    assert not formatters_grouped.pop('unfinished')


# Generated at 2022-06-13 22:36:38.706501
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:36:46.108447
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(
        AuthPlugin,
        FormatterPlugin,
        ConverterPlugin,
        TransportPlugin,
    )
    plugin_manager.load_installed_plugins()
    formatters = plugin_manager.get_formatters_grouped()
    default_formatters = formatters['Default']
    assert default_formatters == [DefaultFormatter]
    json_formatters = formatters['JSON']

# Generated at 2022-06-13 22:36:49.208957
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    print(plugin_manager)

# Generated at 2022-06-13 22:37:12.465903
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert "main" in plugin_manager.get_formatters_grouped().keys()
    assert "main" in plugin_manager.get_formatters_grouped().keys()
    assert "dev" in plugin_manager.get_formatters_grouped().keys()
    assert "util" in plugin_manager.get_formatters_grouped().keys()
    assert "old" in plugin_manager.get_formatters_grouped().keys()
    assert "default" in plugin_manager.get_formatters_grouped().keys()
    assert "pygments" in plugin_manager.get_formatters_grouped().keys()

# test code for method register and unregister of class PluginManager

# Generated at 2022-06-13 22:37:18.740680
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plg = PluginManager()
    plg.register(AuthPlugin)
    plg.register(AuthPlugin)
    plg.register(AuthPlugin)
    assert len(plg) == 3
    auth_plugin_mapping = plg.get_auth_plugin_mapping()
    assert len(auth_plugin_mapping) == 3

# Generated at 2022-06-13 22:37:22.638023
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == len(ENTRY_POINT_NAMES)

# Generated at 2022-06-13 22:37:27.612894
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    assert repr(manager) == '<PluginManager: []>'
    manager.register(Type[BasePlugin])
    manager.load_installed_plugins()
    assert repr(manager) != '<PluginManager: []>'
    assert manager.get_formatters_grouped() == {
        '_core': [Type[BasePlugin]],
    }

# Generated at 2022-06-13 22:37:34.218881
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert len(pluginManager.get_auth_plugins()) >= 2
    assert len(pluginManager.get_formatters()) >= 1
    assert len(pluginManager.get_converters()) >= 1
    assert len(pluginManager.get_transport_plugins()) >= 1
# End of unit test



# Generated at 2022-06-13 22:37:38.477971
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    mapping = plugin_manager.get_auth_plugin_mapping()
    result = True
    for plugin in mapping.values():
        if not issubclass(plugin, AuthPlugin):
            result = False
    return result


# Generated at 2022-06-13 22:37:40.263416
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert type(plugin_manager.get_formatters_grouped()) == dict

# Generated at 2022-06-13 22:37:46.474630
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_name = 'ConverterPlugin'
    plugin_type = BasePlugin
    plugins = PluginManager()
    plugins.register(BasePlugin)
    plugins.register(ConverterPlugin)
    assert plugins.filter(plugin_type)[0].__name__ == plugin_name


# Generated at 2022-06-13 22:37:55.695043
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    print(pm)
    assert len(pm) > 0
    # print(pm.get_auth_plugins())
    # print(pm.get_auth_plugin_mapping())
    # print(pm.get_auth_plugin('basic'))
    # print(pm.get_formatters())
    # print(pm.get_formatters_grouped())
    # print(pm.get_converters())
    # print(pm.get_transport_plugins())
    # print(pm.filter(TransportPlugin))
    # print(pm.filter(AuthPlugin))
    # print(pm.filter(FormatterPlugin))
    # print(pm.filter(ConverterPlugin))
    # print(pm.filter())
    # print(type(pm

# Generated at 2022-06-13 22:37:59.108584
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:38:19.309403
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert len(PluginManager().load_installed_plugins()) > 0

# Generated at 2022-06-13 22:38:28.757301
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    #Testing for httpie.plugins.auth.v1
    plugin = plugin_manager[0]
    plugin.package_name = None
    plugin_manager.load_installed_plugins()
    assert plugin.package_name == 'httpie'
    #Testing for httpie.plugins.formatter.v1
    plugin = plugin_manager[1]
    plugin.package_name = None
    plugin_manager.load_installed_plugins()
    assert plugin.package_name == 'httpie'
    #Testing for httpie.plugins.converter.v1
    plugin = plugin_manager[2]
    plugin.package_name = None
    plugin_manager.load_installed_plugins()
    assert plugin.package_name == 'httpie'
    #Testing for httpie.plugins.transport.v

# Generated at 2022-06-13 22:38:30.291421
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    _pm = PluginManager()
    _pm.load_installed_plugins()


manager = PluginManager()
manager.load_installed_plugins()

# Generated at 2022-06-13 22:38:32.284816
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginsManager = PluginManager()
    PluginsManager.load_installed_plugins() ==  True

# Generated at 2022-06-13 22:38:37.545237
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm=PluginManager()
    pm.register(HttpiePluginsAuthBasicPlugin)
    assert len(pm.get_auth_plugin_mapping())==1
    assert pm.get_auth_plugin_mapping()["basic"]==HttpiePluginsAuthBasicPlugin

# Generated at 2022-06-13 22:38:46.800474
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import sys
    import pkg_resources
    import httpie.plugins.builtin

    plugin_manager = PluginManager()
    if not plugin_manager:
        if sys.version_info.major >= 3:
            old = pkg_resources.iter_entry_points
            pkg_resources.iter_entry_points = lambda name: []
        else:
            old = pkg_resources.iter_entry_points
            pkg_resources.iter_entry_points = lambda name: iter([])
        plugin_manager.load_installed_plugins()
        pkg_resources.iter_entry_points = old
    assert plugin_manager
    # test this method only create the plugin, not load the plugin
    for plugin in plugin_manager:
        assert not plugin.load()

# Generated at 2022-06-13 22:38:50.301169
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.register(AuthPlugin)
    assert pm.get_auth_plugin_mapping() == {AuthPlugin.auth_type: AuthPlugin}

# Generated at 2022-06-13 22:38:53.645941
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # check if basic Auth is installed
    if 'Basic' in PluginManager().get_auth_plugin_mapping().keys():
        return True
    else:
        return False


# Generated at 2022-06-13 22:38:56.380145
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager=PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 0

# Generated at 2022-06-13 22:38:57.144978
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pass

# Generated at 2022-06-13 22:39:30.404387
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import auth, formatter, converter, transport
    from httpie.plugins.base import create_auth_plugin, create_formatter_plugin, create_converter_plugin, create_transport_plugin

    # test case 1
    class MyTestPlugin(BasePlugin):
        pass

    m = PluginManager()
    t1 = create_auth_plugin(auth.OAuth1, 'test', {'a': 'b'})
    t2 = create_auth_plugin(auth.OAuth2, 'test', {'a': 'b'})
    t3 = create_formatter_plugin(formatter.JSONFormatter, 'test', {'a': 'b'})
    t4 = create_formatter_plugin(formatter.PrettyJsonFormatter, 'test', {'a': 'b'})
    t

# Generated at 2022-06-13 22:39:38.460701
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_auth_plugin_mapping().keys() == {'basic', 'digest', 'jwt'}
    assert plugin_manager.get_formatters_grouped().keys() == {'json', 'csv', 'table', }
    assert plugin_manager.get_converters().__len__() == 0
    assert plugin_manager.get_transport_plugins().__len__() == 0
    # Here, it's mean we have 3 auth plugins and 3 formatter plugins and 3 transport plugins,
    # so class PluginManager can load it and we can use it

# Generated at 2022-06-13 22:39:41.104154
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()




# Generated at 2022-06-13 22:39:51.425551
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    assert plugins.get_formatters_grouped()=={}

    plugins.register(FormatterPlugin)
    assert plugins.get_formatters_grouped() == {
        'None': [FormatterPlugin]
    }

    plugins.register(ConverterPlugin)
    assert plugins.get_formatters_grouped() == {
        'None': [FormatterPlugin]
    }

    plugins.register(ConverterPlugin)
    assert plugins.get_formatters_grouped() == {
        'None': [FormatterPlugin]
    }

# Generated at 2022-06-13 22:39:53.833289
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.unregister(plugin_manager.get_auth_plugin("basic"))
    assert plugin_manager.get_auth_plugin_mapping()['basic'] != None

# Generated at 2022-06-13 22:39:56.608131
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager) == 0, "PluginManager should not have any plugin registered after loading all installed plugins"

# Generated at 2022-06-13 22:39:59.855296
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager.get_auth_plugin_mapping())


# Generated at 2022-06-13 22:40:07.114993
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPTokenAuth, HTTPiePlugin, LocalhostAuthPlugin
    from httpie.plugins.builtin import PythonHTTPiePlugin, JSONStreamPlugin, JSONPlugin, HTTPiePlugin
    from httpie.plugins.builtin import XMLExtendedPlugin, XMLPlugin, PrettyHTTPiePlugin, XMLStreamPlugin
    from httpie.plugins.builtin import PygmentsHTTPiePlugin, KeyValueHTTPiePlugin, HTMLStreamPlugin, HTMLPlugin
    from httpie.plugins.builtin import HTTPGzipPlugin, HTTPieCurlHTTPPlugin, HTTPieRequestsPlugin
    from httpie.plugins.builtin import HTTPieUrllib3Plugin, HTTPieASyncHTTPClientPlugin, HTTPieTCPPlugin
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:40:09.997212
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    a = PluginManager()
    a.register(class__)
    assert  a.get_formatters_grouped() == 3

# Generated at 2022-06-13 22:40:20.564570
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Xxx:
        def __init__(self, group_name):
            self.group_name = group_name
            
    x = PluginManager()
    x.register(Xxx('a'))
    x.register(Xxx('b'))
    x.register(Xxx('b'))
    x.register(Xxx('c'))
    x.register(Xxx('a'))
    x.register(Xxx('a'))
    x.register(Xxx('c'))

# Generated at 2022-06-13 22:41:11.016196
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert True


# Generated at 2022-06-13 22:41:21.181485
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    assert plugins.get_auth_plugin_mapping() == {}

    class DummyPlugin(AuthPlugin):
        auth_type = 'dummy'

    plugins.register(DummyPlugin)
    assert plugins.get_auth_plugin_mapping() == {'dummy': DummyPlugin}

    class DummyPlugin2(AuthPlugin):
        auth_type = 'dummy2'

    plugins.register(DummyPlugin2)
    assert plugins.get_auth_plugin_mapping() == {
        'dummy': DummyPlugin,
        'dummy2': DummyPlugin2,
    }


# Generated at 2022-06-13 22:41:25.706603
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(BasePlugin)
    assert plugin_manager.get_formatters_grouped() == {'Group 1': []}

# Generated at 2022-06-13 22:41:27.505674
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) == 42


# Generated at 2022-06-13 22:41:37.025396
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    
    class FormatterPlugin_1(FormatterPlugin):
        group_name = 'group_name_1'
    class FormatterPlugin_2(FormatterPlugin):
        group_name = 'group_name_1'
    class FormatterPlugin_3(FormatterPlugin):
        group_name = 'group_name_2'
    
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin_1, FormatterPlugin_2, FormatterPlugin_3)
    expected = {
        'group_name_1': [FormatterPlugin_1, FormatterPlugin_2],
        'group_name_2': [FormatterPlugin_3],
    }
    assert plugin_manager.get_formatters_grouped() == expected

# Generated at 2022-06-13 22:41:42.659291
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = [
        'httpie.plugins.formatter',
        'httpie.plugins.converter',
        'httpie.plugins.transport',
        'httpie.plugins.auth',
    ]
    for plugin in plugins:
        assert plugin in str(PluginManager().load_installed_plugins())

# Generated at 2022-06-13 22:41:52.596119
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    class Formatter(FormatterPlugin):
        group_name = 'TestGroup'

    class Formatter2(FormatterPlugin):
        group_name = 'TestGroup2'

    class MyFormatter(FormatterPlugin):
        group_name = 'TestGroup'

    pluginManager = PluginManager()
    pluginManager.register(Formatter, Formatter2, MyFormatter)

    assert len(pluginManager.get_formatters_grouped()['TestGroup']) == 2
    assert len(pluginManager.get_formatters_grouped()['TestGroup2']) == 1



# Generated at 2022-06-13 22:41:56.001593
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.append(AuthPlugin())
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert auth_plugin_mapping == {'basic': AuthPlugin}, print(auth_plugin_mapping)

# Generated at 2022-06-13 22:41:57.884763
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert isinstance(plugins, PluginManager)
    

# Generated at 2022-06-13 22:42:03.976693
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.plugins.builtin import JSONPlugin
    from httpie.plugins.builtin import TerminalPlugin
    from httpie.plugins.builtin import HTMLPlugin

    plm = PluginManager()
    plm.register(HTTPiePlugin, JSONPlugin, TerminalPlugin, HTMLPlugin)
    formatters_grouped = plm.get_formatters_grouped()
    # All builtin formatters should be grouped into 'builtin' group
    assert formatters_grouped['builtin'] == [HTTPiePlugin, JSONPlugin,
                                             TerminalPlugin, HTMLPlugin]