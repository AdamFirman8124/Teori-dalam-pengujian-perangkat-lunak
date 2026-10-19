

# Generated at 2022-06-13 22:33:17.879747
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    assert not pm
    pm.load_installed_plugins()
    assert pm



# Generated at 2022-06-13 22:33:20.359918
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.__repr__() != ''


# Generated at 2022-06-13 22:33:22.792258
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert isinstance(pluginManager[0], type)

# Generated at 2022-06-13 22:33:30.275818
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    from httpie.plugins import FormatterPlugin
    class formatter1(FormatterPlugin):
        group_name = 'group1'
        group_title = 'group1_title'
        group_description = 'group1_description'
    class formatter2(FormatterPlugin):
        group_name = 'group1'
        group_title = 'group1_title'
        group_description = 'group1_description'
    class formatter3(FormatterPlugin):
        group_name = 'group1'
        group_title = 'group1_title'
        group_description = 'group1_description'
    class formatter4(FormatterPlugin):
        group_name = 'group2'
        group_title = 'group2_title'
        group_description = 'group2_description'

# Generated at 2022-06-13 22:33:33.525029
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert pluginManager is not None


# Generated at 2022-06-13 22:33:37.564142
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPlugin(BasePlugin):
        pass
    test_plugin_manager = PluginManager()
    test_plugin_manager.register(TestPlugin)
    assert list(test_plugin_manager.filter(TestPlugin)) == [TestPlugin]

# Generated at 2022-06-13 22:33:44.818432
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    #manager.register(FormatterPlugin1,FormatterPlugin2)
    manager.register(FormatterPlugin1)
    manager.register(FormatterPlugin2)
    # print(manager.get_formatters_grouped())
    assert manager.get_formatters_grouped() == {"json": [FormatterPlugin1, FormatterPlugin2], "other": [FormatterPlugin2]}

test_PluginManager_get_formatters_grouped()

manager = PluginManager()
manager.load_installed_plugins()

__all__ = ['manager']

# Generated at 2022-06-13 22:33:49.179313
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    test_PluginManager = PluginManager()
    # assertion
    assert {'auth_type': 'plugin_name'} == test_PluginManager.get_auth_plugin_mapping()

# Generated at 2022-06-13 22:33:53.733646
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    plugin_mapping = manager.get_auth_plugin_mapping()
    assert isinstance(plugin_mapping, dict)
    assert True not in plugin_mapping

# Generated at 2022-06-13 22:34:01.168255
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) >= 1
    assert len(plugin_manager.get_formatters()) >= 1
    assert len(plugin_manager.get_converters()) >= 1
    assert len(plugin_manager.get_transport_plugins()) >= 1


# Generated at 2022-06-13 22:34:06.633055
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager_class = PluginManager()
    assert plugin_manager_class.get_auth_plugin_mapping() == {}

# Generated at 2022-06-13 22:34:18.255911
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    def mock_get_formatters(self):
        return [
            Mock(group_name='group1'),
            Mock(group_name='group2'),
            Mock(group_name='group2'),
            Mock(group_name='group1'),
            Mock(group_name='group1')
        ]

    plugin_manager = PluginManager()
    plugin_manager.get_formatters = mock_get_formatters.__get__(plugin_manager, PluginManager)

    formatters_grouped = plugin_manager.get_formatters_grouped()

    assert len(formatters_grouped) == 2
    assert len(formatters_grouped['group1']) == 3
    assert len(formatters_grouped['group2']) == 2

# Generated at 2022-06-13 22:34:29.246215
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pkg_resources
    from httpie.plugins.base import BasePlugin
    from httpie.plugins.builtin import HTTPBasicAuth
    import os, sys


    class PluginManager(list):
        def register(self, *plugins: Type[BasePlugin]):
            for plugin in plugins:
                self.append(plugin)

        def unregister(self, plugin: Type[BasePlugin]):
            self.remove(plugin)

        def filter(self, by_type=Type[BasePlugin]):
            return [plugin for plugin in self if issubclass(plugin, by_type)]

        def load_installed_plugins(self):
            for entry_point_name in ENTRY_POINT_NAMES:
                for entry_point in iter_entry_points(entry_point_name):
                    plugin = entry_point.load()
                   

# Generated at 2022-06-13 22:34:30.679465
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pass



# Generated at 2022-06-13 22:34:35.689435
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PluginManager_obj = PluginManager()
    PluginManager_obj.load_installed_plugins()
    assert (len(PluginManager_obj.get_formatters_grouped()) > 1)
    assert ("Group 2" in PluginManager_obj.get_formatters_grouped().keys())

# Generated at 2022-06-13 22:34:47.350520
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    from httpie.plugins.builtin import AuthPlugin
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.plugins.builtin import ConverterPlugin
    from httpie.plugins.builtin import TransportPlugin

    pm.register(AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin)
    auth_plugins = pm.filter(AuthPlugin)
    format_plugins = pm.filter(FormatterPlugin)
    convert_plugins = pm.filter(ConverterPlugin)
    transport_plugins = pm.filter(TransportPlugin)

    assert len(auth_plugins) == 1
    assert len(format_plugins) == 1
    assert len(convert_plugins) == 1
    assert len(transport_plugins) == 1

# Generated at 2022-06-13 22:34:52.730173
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert pm.get_auth_plugin_mapping() != {}
    assert pm.get_formatters_grouped() != {}
    assert pm.get_converters() != []
    assert pm.get_transport_plugins() != []

# Generated at 2022-06-13 22:34:55.183875
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(MockFormatter, MockFormatter)
    assert pm.get_formatters_grouped()['MockGroupName'] == MockFormatter


pm = PluginManager()
pm.load_installed_plugins()

# Generated at 2022-06-13 22:35:02.971367
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(BasePlugin)
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(ConverterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(TransportPlugin)
    print(plugin_manager.filter(by_type = FormatterPlugin))
    print(plugin_manager.filter(by_type = AuthPlugin))

test_PluginManager_filter()

# Generated at 2022-06-13 22:35:08.205504
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins.get_auth_plugins() != []
    assert plugins.get_formatters_grouped() != {}
    assert plugins.get_transport_plugins() != []

# Generated at 2022-06-13 22:35:12.969584
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:35:22.474644
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # When
    manager = PluginManager()
    manager.load_installed_plugins()

    # Then

# Generated at 2022-06-13 22:35:24.811723
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == 8

# Generated at 2022-06-13 22:35:27.614287
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert isinstance(pluginManager, PluginManager)


# Generated at 2022-06-13 22:35:29.820110
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm=PluginManager()
    pm.load_installed_plugins()
    assert(len(pm)>0)

# Generated at 2022-06-13 22:35:31.942182
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()


plugins = PluginManager()
plugins.load_installed_plugins()

# Generated at 2022-06-13 22:35:38.029874
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(HTTPlugPlugin, CurlPlugin)
    assert(plugin_manager.get_formatters_grouped()['networking'] == [HTTPlugPlugin, CurlPlugin])
    assert(plugin_manager.get_formatters_grouped()['data'] == [JSONPlugin, URLEncodedPlugin, BackendPlugin])

# Generated at 2022-06-13 22:35:45.840177
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()

# Generated at 2022-06-13 22:35:51.088450
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert len(pluginManager) == 26
    for plugin in pluginManager:
        assert type(plugin) == type
        assert issubclass(plugin, BasePlugin)


# Generated at 2022-06-13 22:35:57.733955
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    manager = PluginManager()
    manager.register(A, B, C)

    assert manager.filter(A) == [A, B, C]
    assert manager.filter(B) == [B]
    assert manager.filter(C) == [C]

# Generated at 2022-06-13 22:36:10.574540
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(AuthPlugin)
    plugins.register(AuthPlugin)
    auth_plugin_mapping = plugins.get_auth_plugin_mapping()
    assert 'basic' in auth_plugin_mapping
    assert issubclass(auth_plugin_mapping['basic'], AuthPlugin), "Plugin is subclass of AuthPlugin"

# Generated at 2022-06-13 22:36:15.356240
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.manager import PluginManager, ENTRY_POINT_NAMES
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:36:21.108467
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins_manager = PluginManager()
    plugins_manager.register(Oauth1AuthPlugin, Oauth2AuthPlugin)
    assert plugins_manager.get_auth_plugin_mapping() == {
        'oauth1': Oauth1AuthPlugin,
        'oauth2': Oauth2AuthPlugin
    }

# Generated at 2022-06-13 22:36:28.502839
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin,FormatterPlugin)
    result = plugin_manager.get_formatters_grouped()
    assert(result is not None)
    assert(result is not {})
    assert(result[None] is not None)
    assert(result[None] is not [])
    assert(len(result[None])==2)

# Generated at 2022-06-13 22:36:32.465117
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print("PluginManager.load_installed_plugins")
    plugin_manager=PluginManager()
    plugin_manager.load_installed_plugins()
    print("plugin_manager",plugin_manager)
    # print("plugin_manager[1]",plugin_manager[1])
    assert isinstance(plugin_manager,list)



# Generated at 2022-06-13 22:36:37.690213
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    assert plugin_manager.get_auth_plugin_mapping() == {}

    plugin_manager.register(A)
    plugin_manager.register(B)
    assert plugin_manager.get_auth_plugin_mapping() == {'A': A, 'B': B}

    plugin_manager.unregister(A)
    assert plugin_manager.get_auth_plugin_mapping() == {'B': B}

    plugin_manager.unregister(B)
    assert plugin_manager.get_auth_plugin_mapping() == {}


# Generated at 2022-06-13 22:36:47.789087
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Foo(BasePlugin):
        pass
    class Bar(Foo):
        pass
    class Baz(Bar):
        pass

    pm = PluginManager()
    pm.register(Foo, Bar, Baz)

    assert len(pm.filter(BasePlugin)) == 3
    assert len(pm.filter(Foo)) == 3
    assert len(pm.filter(Bar)) == 2
    assert len(pm.filter(Baz)) == 1
    assert len(pm.filter()) == 3
    assert Foo in pm.filter(BasePlugin)
    assert Bar in pm.filter(BasePlugin)
    assert Baz in pm.filter(BasePlugin)
    assert Foo in pm.filter(Foo)
    assert Bar in pm.filter(Foo)
    assert Baz in pm.filter(Foo)

# Generated at 2022-06-13 22:36:50.119216
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    assert plugins.get_formatters_grouped() == {}



# Generated at 2022-06-13 22:37:00.788738
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin
    from httpie.plugins.base import BasePlugin, TransportPlugin
    class AuthTest(AuthPlugin):
        auth_type = 'test-auth'
    class ConverterTest(ConverterPlugin):
        name = 'test'
    class FormatterTest(FormatterPlugin):
        name = 'test'
    class TransportTest(TransportPlugin):
        name = 'test'

    plugin_test = PluginManager()
    plugin_test.register(AuthTest,ConverterTest,FormatterTest,TransportTest)

    assert plugin_test.filter(AuthPlugin) == [AuthTest]
    assert plugin_test.filter(BasePlugin) == [AuthTest,ConverterTest,FormatterTest,TransportTest]

# Generated at 2022-06-13 22:37:03.237598
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) == 47, \
        f'PluginManager.load_installed_plugins should have added 47 plugins but added {len(plugins)}.'

# Generated at 2022-06-13 22:37:19.544031
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager.get_auth_plugin_mapping())

if __name__ == '__main__':
    test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:37:24.532478
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.append(AuthPlugin)
    manager.append(ConverterPlugin)
    manager.append(FormatterPlugin)
    assert manager.filter() == [AuthPlugin, ConverterPlugin, FormatterPlugin]
    assert manager.filter(AuthPlugin) == [AuthPlugin]

# Generated at 2022-06-13 22:37:25.611191
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert isinstance(PluginManager().get_formatters_grouped(), dict)

# Generated at 2022-06-13 22:37:31.070777
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    Testcase for testing method get_formatters_grouped of class PluginManager
    """
    assert PluginManager().get_formatters_grouped() == {}, "PluginManager().get_formatters_grouped() should be empty dict {}"
    

# Generated at 2022-06-13 22:37:34.839555
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugins_name = [plugin.name for plugin in plugin_manager]
    assert 'httpbin' in plugins_name

# Generated at 2022-06-13 22:37:42.373344
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Given
    import os
    import tempfile
    from unittest.mock import mock_open, patch

    from httpie.plugins import transport_http
    from httpie.plugins.base import TransportPlugin

    m = mock_open(read_data='{"Name": "httpie-test-plugin", "Version": "0.1"}')

# Generated at 2022-06-13 22:37:50.374625
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Initialize plugins
    plugins = PluginManager()
    
    # Check for plugins
    for name in ENTRY_POINT_NAMES:
        for entry_point in iter_entry_points(name):
            plugin = entry_point.load()
            plugin.package_name = entry_point.dist.key
            plugins.register(plugin)

    assert len(plugins) > 0, 'Plugins were not registered'
    assert len(plugins.filter(AuthPlugin)) > 0, 'Auth plugins were not registered'

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:37:54.660575
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class FooPlugin(FormatterPlugin):
        group_name = 'foo'
    class BarPlugin(FooPlugin):
        group_name = 'bar'
    manager = PluginManager()
    manager.register(FooPlugin, BarPlugin)
    assert manager.get_formatters_grouped() == {'foo': [FooPlugin, BarPlugin]}

# Generated at 2022-06-13 22:37:56.882086
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.append(1)
    pm.append(2)
    pm.append(3)
    assert pm.filter() == [1, 2, 3]

# Generated at 2022-06-13 22:38:10.746696
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from .converters import JsonTestConverter, XmlTestConverter
    from .formatters import HtmlTestFormatter, JsonTestFormatter
    from .transport import TestTransportAdapter
    manager = PluginManager()
    manager.register(HtmlTestFormatter, JsonTestFormatter, JsonTestConverter, XmlTestConverter, TestTransportAdapter)
    assert manager.filter(ConverterPlugin) == [JsonTestConverter, XmlTestConverter]
    assert manager.filter(TransportPlugin) == [TestTransportAdapter]
    assert manager.filter(FormatterPlugin) == [HtmlTestFormatter, JsonTestFormatter]

# Generated at 2022-06-13 22:38:34.771446
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()

# Generated at 2022-06-13 22:38:38.672352
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(PluginA)
    plugins.register(PluginB)
    assert plugins.get_auth_plugin_mapping() == {'a': PluginA, 'b': PluginB}

# Generated at 2022-06-13 22:38:41.354929
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    auth_plugin = PluginManager()
    auth_plugin.load_installed_plugins()
    print(auth_plugin.get_auth_plugin_mapping())


# Generated at 2022-06-13 22:38:44.744358
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    plugins_type = []
    for plugin in plugins:
        plugins_type.append(plugin.__name__)

    assert 'DigestAuthPlugin' in plugins_type

# Generated at 2022-06-13 22:38:48.414975
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter() == []


_plugin_manager = PluginManager()
_plugin_manager.load_installed_plugins()


# Generated at 2022-06-13 22:38:52.292336
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert plugin_manager.get_formatters_grouped() == {}
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_formatters_grouped() != {}

# Generated at 2022-06-13 22:38:56.134366
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0
    assert 'httpie.plugins.transport.http.HTTPTransportPlugin' in str(plugins)


# Generated at 2022-06-13 22:39:02.648980
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm=PluginManager()
    pm.load_installed_plugins()
    print("Method load_installed_plugins of PluginManager:")
    print("\t", pm)
    print("\t", "----------------------------------------------------")
    print("\t", pm.get_auth_plugin('basic'))
    print("\t", pm.get_auth_plugin('digest'))
    print("\t", pm.get_auth_plugin('bearer'))
    print("\t", pm.get_auth_plugin('aws'))
    print("\t", pm.get_auth_plugin('aws-credentials'))
    print("\t", "----------------------------------------------------")
    print("\t", pm.get_formatters())
    print("\t", "----------------------------------------------------")
    print("\t", pm.get_converters())


# Generated at 2022-06-13 22:39:04.407759
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(BasePlugin)
    assert pm.filter(BasePlugin) == [BasePlugin]


# Generated at 2022-06-13 22:39:13.518647
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_list = [{'group_name':'aa', 'name':'aa1'},
                 {'group_name':'aa', 'name':'aa2'},
                 {'group_name':'bb', 'name':'bb1'},
                 {'group_name':'bb', 'name':'bb2'}]
    group_dict = {'aa':[{'group_name':'aa', 'name':'aa1'},
                         {'group_name':'aa', 'name':'aa2'}],
                  'bb':[{'group_name':'bb', 'name':'bb1'},
                        {'group_name':'bb', 'name':'bb2'}]}
    assert group_dict == PluginManager.get_formatters_grouped(PluginManager, test_list)

# Generated at 2022-06-13 22:40:03.276595
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class MyPlugin(BasePlugin):
        pass

    class AnotherPlugin(BasePlugin):
        pass

    pm = PluginManager()
    pm.register(MyPlugin)
    pm.register(AnotherPlugin)
    pm.filter(by_type=MyPlugin) == [MyPlugin]



# Generated at 2022-06-13 22:40:14.972357
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import formatter

    plugin_manager = PluginManager()
    plugin_manager.register(formatter.PrettyJSONFormatter)
    plugin_manager.register(formatter.PrettyURLEncodedFormatter)
    plugin_manager.register(formatter.PrettyMultipartFormatter)
    plugin_manager.register(formatter.RawJSONFormatter)
    plugin_manager.register(formatter.RawURLEncodedFormatter)
    plugin_manager.register(formatter.RawMultipartFormatter)

# Generated at 2022-06-13 22:40:21.117739
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pkg_resources
    from httpie.core import main

    if not pkg_resources.working_set.find(main.__spec__.name):
        raise Exception('The main package cannot be found')

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert hasattr(plugin_manager, "package_name")
    assert plugin_manager.package_name == main.__spec__.name


test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:40:25.819751
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plg = PluginManager()
    assert isinstance(plg, PluginManager)
    plg.register(AuthPlugin)
    assert plg.filter(AuthPlugin) == [AuthPlugin]
    assert plg.filter(ConverterPlugin) == []

# Generated at 2022-06-13 22:40:33.701599
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PM = PluginManager()
    PM.append(FormatterPlugin)
    PM.append(FormatterPlugin)
    PM.append(FormatterPlugin)
    PM.append(FormatterPlugin)
    assert PM.get_formatters_grouped() == {'GroupName': [FormatterPlugin, FormatterPlugin, FormatterPlugin, FormatterPlugin]}



# Generated at 2022-06-13 22:40:43.610528
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    class EmptyPlugin(BasePlugin):
        pass

    class AuthPlugin_v1(AuthPlugin):
        pass

    class FormatterPlugin_v1(FormatterPlugin):
        pass

    class ConverterPlugin_v1(ConverterPlugin):
        pass

    class TransportPlugin_v1(TransportPlugin):
        pass

    plugin_manager = PluginManager()

    plugin_manager.register(AuthPlugin_v1, FormatterPlugin_v1,
                            ConverterPlugin_v1, TransportPlugin_v1,
                            EmptyPlugin)

    assert len(plugin_manager.filter(EmptyPlugin)) == 1
    assert len(plugin_manager.filter(AuthPlugin)) == 1
    assert len(plugin_manager.filter(FormatterPlugin)) == 1
    assert len(plugin_manager.filter(ConverterPlugin)) == 1

# Generated at 2022-06-13 22:40:47.270362
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginmanager = PluginManager()
    pluginmanager.load_installed_plugins()
    from httpie.plugins.builtin import HTTPBasicAuth
    assert HTTPBasicAuth in pluginmanager.get_auth_plugins()
    from httpie.plugins.builtin import JSONFormatterPlugin
    assert JSONFormatterPlugin in pluginmanager.get_formatters()
    from httpie.plugins.builtin import HTTPieHTTPAdapter
    assert HTTPieHTTPAdapter in pluginmanager.get_transport_plugins()

# Generated at 2022-06-13 22:40:56.044152
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()

    plugins.register(ConverterPlugin, AuthPlugin, AuthPlugin, FormatterPlugin, FormatterPlugin, Type[BasePlugin])
    assert plugins.filter() == [ConverterPlugin, AuthPlugin, AuthPlugin, FormatterPlugin, FormatterPlugin, Type[BasePlugin]]
    assert plugins.filter(ConverterPlugin) == [ConverterPlugin]
    assert plugins.filter(AuthPlugin) == [AuthPlugin, AuthPlugin]
    assert plugins.filter(FormatterPlugin) == [FormatterPlugin, FormatterPlugin]


# Unit testing for method unregister of class PluginManager

# Generated at 2022-06-13 22:41:04.529617
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import JSONHeaders, JSONTraceback
    assert PluginManager().filter() == []
    assert PluginManager([JSONHeaders]).filter(JSONHeaders) == [JSONHeaders]
    assert PluginManager().filter(JSONHeaders) == []
    assert PluginManager([JSONHeaders, JSONTraceback]).filter(JSONHeaders) == [JSONHeaders]
    assert PluginManager([JSONHeaders, JSONTraceback]).filter(JSONTraceback) == [JSONTraceback]
    assert PluginManager([JSONHeaders, JSONTraceback]).filter() == [JSONHeaders, JSONTraceback]

# Generated at 2022-06-13 22:41:08.522604
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    a1 = PluginManager()
    a1.register(1, 2, 3)
    assert a1.filter(int) == [1, 2, 3]
    assert a1.filter(str) == []

# Generated at 2022-06-13 22:42:49.596482
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter() == []


# Generated at 2022-06-13 22:42:55.555881
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    def get_attribute(obj, attr):
        return getattr(obj, attr)

    plugins = PluginManager()
    plugins.load_installed_plugins()

    names = set(map(lambda plugin: get_attribute(plugin, "name"), plugins))
    assert "HTTPie" in names

# Generated at 2022-06-13 22:42:58.350915
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()


# Generated at 2022-06-13 22:43:01.487607
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    instance = PluginManager()
    instance.load_installed_plugins()
    assert (len(instance)>0)

# Generated at 2022-06-13 22:43:11.241706
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    from pkg_resources import resource_filename
    from tests.test_plugins.formatters import TestFormatterA
    from tests.test_plugins.group import TestGroupA
    from tests.test_plugins.group import TestGroupB
    from tests.test_plugins.group import TestGroupC

    plugin_manager = PluginManager()
    plugin_manager.register(TestGroupA)
    plugin_manager.register(TestGroupB)
    plugin_manager.register(TestGroupC)
    plugin_manager.register(TestFormatterA)
    assert len(plugin_manager.get_formatters_grouped()) == 3
    assert len(plugin_manager.get_formatters_grouped()[TestGroupA.group_name]) == 1

# Generated at 2022-06-13 22:43:13.994679
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pluginManager = PluginManager()
    pluginManager.register(AuthPlugin)
    assert pluginManager.get_auth_plugin_mapping() == {}