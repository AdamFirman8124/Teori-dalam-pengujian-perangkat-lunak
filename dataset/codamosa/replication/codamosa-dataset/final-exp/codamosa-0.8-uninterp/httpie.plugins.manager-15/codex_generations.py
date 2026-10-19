

# Generated at 2022-06-13 22:33:23.322351
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    """
    Unit test for method filter of class PluginManager
    """
    class A:
        pass
    class B:
        pass
    class C:
        pass
    class AA(A):
        pass
    class AB(A):
        pass
    class ABC(AB):
        pass
    plugin_manager = PluginManager()
    plugin_manager.register(A,B,C,AA,AB,ABC)
    assert plugin_manager.filter(A) == [A,AA,AB,ABC]


# Generated at 2022-06-13 22:33:30.822499
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # test grouping formatters with same group_name
    plugins = PluginManager()

    class FormatterPlugin_01(FormatterPlugin):
        group_name = "same_group"
        group_order = 1
        order = 1

    class FormatterPlugin_02(FormatterPlugin):
        group_name = "same_group"
        group_order = 1
        order = 1

    class FormatterPlugin_03(FormatterPlugin):
        group_name = "other_group"
        group_order = 2
        order = 3

    plugins.register(FormatterPlugin_01, FormatterPlugin_02, FormatterPlugin_03)

    # type `plugins` is a list that stores all plugins that have been registered
    # type `plugins.get_formatters_grouped()` is a dict that stores all formatters that have been registered,
   

# Generated at 2022-06-13 22:33:36.819993
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A(object): pass
    class B(A): pass
    class C(A): pass
    class D(object): pass
    plugin_manager = PluginManager()
    plugin_manager.register(A,B,C,D)
    assert plugin_manager.filter(A) == [A,B,C]


# Generated at 2022-06-13 22:33:41.933274
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = []
    plugin_manager = PluginManager(plugins)
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(AuthPlugin)
    assert plugin_manager.get_auth_plugin_mapping() == [(AuthPlugin, AuthPlugin, AuthPlugin)]

# Generated at 2022-06-13 22:33:50.701519
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.register(
        BasicAuth,
        BearerTokenAuth,
        DigestAuth,
        FormAuth,
        HawkAuth,
        OAuth1Auth,
        OAuth2Auth
    )
    assert plugin_manager.get_auth_plugin_mapping() == {
        'basic': BasicAuth,
        'bearer': BearerTokenAuth,
        'digest': DigestAuth,
        'form': FormAuth,
        'hawk': HawkAuth,
        'oauth1': OAuth1Auth,
        'oauth2': OAuth2Auth
    } == {
        plugin.auth_type: plugin
        for plugin in plugin_manager.get_auth_plugins()
    }


# Generated at 2022-06-13 22:33:55.181139
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    assert str(plugin_manager) == '<PluginManager: []>'
    plugin_manager.load_installed_plugins()
    assert str(plugin_manager) != '<PluginManager: []>'

# Generated at 2022-06-13 22:34:00.304504
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    # Make sure we get what we are expecting
    assert len(pm) > 0
    for plugin in pm:
        assert isinstance(plugin, BasePlugin)



# Generated at 2022-06-13 22:34:04.726903
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager.get_transport_plugins()) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0

# Generated at 2022-06-13 22:34:08.195914
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == 1
    assert pm[0].__name__ == "HTTPBasicAuth"

# Generated at 2022-06-13 22:34:20.024592
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(TestFormatter1, TestFormatter2, TestFormatter3)
    assert plugins.get_formatters_grouped() == {'group1': [TestFormatter1, TestFormatter2], 'group2': [TestFormatter3]}
    plugins.unregister(TestFormatter3)
    assert plugins.get_formatters_grouped() == {'group1': [TestFormatter1, TestFormatter2]}
    plugins.unregister(TestFormatter1)
    plugins.register(TestFormatter3)
    assert plugins.get_formatters_grouped() == {'group1': [TestFormatter2], 'group2': [TestFormatter3]}
    plugins.unregister(TestFormatter2)
    plugins.unregister(TestFormatter3)
    assert plugins.get_format

# Generated at 2022-06-13 22:34:29.340567
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(
        FormatterPluginGroup_A,
        FormatterPluginGroup_B,
        FormatterPluginGroup_B,
        FormatterPluginGroup_A,
        FormatterPluginGroup_B
    )
    assert pm.get_formatters_grouped()['Group_A'] == [FormatterPluginGroup_A, FormatterPluginGroup_A]
    assert pm.get_formatters_grouped()['Group_B'] == [FormatterPluginGroup_B, FormatterPluginGroup_B, FormatterPluginGroup_B]


# Generated at 2022-06-13 22:34:31.770193
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.register(AuthPlugin)
    assert len(manager.get_auth_plugin_mapping()) == 0



# Generated at 2022-06-13 22:34:40.614770
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class PluginA(BasePlugin):
        pass
    class PluginB(BasePlugin):
        pass
    class PluginC(BasePlugin):
        pass

    class MockEntryPoint:
        def __init__(self, load):
            self.load = load
            self.dist = MockEntryPoint(load.__module__)
    def mocked_iter_entry_points(entry_point_name):
        if entry_point_name == 'httpie.plugins.transport.v1':
            yield MockEntryPoint(PluginA)
            yield MockEntryPoint(PluginC)
        else:
            yield MockEntryPoint(PluginB)

    # Monkey patch iter_entry_points
    import sys
    import pkg_resources
    import builtins
    real_iter_entry_points = pkg_resources.iter_entry_points
    real_import

# Generated at 2022-06-13 22:34:48.285242
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Base1:
        pass
    class Base2:
        pass
    class Derived1(Base1):
        pass
    class Derived2(Base2):
        pass
    plugin_manager = PluginManager()
    plugin_manager.register(Derived1, Derived2, Base1)
    assert plugin_manager.filter(Base1) == [Derived1, Base1]
    assert plugin_manager.filter(Base2) == [Derived2]
    # Test with a class that doesn't inherit from BasePlugin
    assert plugin_manager.filter(str) == []

# Generated at 2022-06-13 22:34:50.958115
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager)>0


# Generated at 2022-06-13 22:35:03.471423
# Unit test for method filter of class PluginManager

# Generated at 2022-06-13 22:35:17.328068
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    auth_plugin = type("AuthPlugin", (AuthPlugin,), {})
    formatter_plugin = type("FormatterPlugin", (FormatterPlugin,), {})
    converter_plugin = type("ConverterPlugin", (ConverterPlugin,), {})
    transport_plugin = type("TransportPlugin", (TransportPlugin,), {})
    plugin_manager = PluginManager()
    # register auth plugin, formatter plugin, converter plugin, transport plugin
    plugin_manager.register(auth_plugin, formatter_plugin, converter_plugin, transport_plugin)
    # load installed plugins
    plugin_manager.load_installed_plugins()
    # verify if load_installed_plugins loads plugins
    assert list(iter_entry_points('httpie.plugins.auth.v1')) == [auth_plugin]

# Generated at 2022-06-13 22:35:20.273555
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert pm

# Generated at 2022-06-13 22:35:23.188905
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    assert isinstance(pm.get_formatters_grouped(), dict)

# Generated at 2022-06-13 22:35:29.592471
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    AuthPlugin_mapping_length = len(plugin_manager.get_auth_plugin_mapping())
    assert AuthPlugin_mapping_length == 1
    assert plugin_manager.get_auth_plugin_mapping()['basic'] == httpie.plugins.auth.basic.BasicAuthPlugin



# Generated at 2022-06-13 22:35:32.343003
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:35:35.966086
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) > 0
    for plugin in manager:
        assert hasattr(plugin, 'package_name')

# Generated at 2022-06-13 22:35:43.371735
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.filter(AuthPlugin)) != 0
    assert len(plugin_manager.filter(FormatterPlugin)) != 0
    assert len(plugin_manager.filter(ConverterPlugin)) != 0
    assert len(plugin_manager.filter(TransportPlugin)) != 0



# Generated at 2022-06-13 22:35:57.593220
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PluginManager.load_installed_plugins()
    print("===== Test PluginManager: get_formatters_grouped =====")

# Generated at 2022-06-13 22:36:01.992797
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import DEFAULT_FORMAT, FORMATTERS
    pm = PluginManager()
    pm.register(*FORMATTERS)
    d = pm.get_formatters_grouped()
    assert d['Builtin'][0] == DEFAULT_FORMAT

# Generated at 2022-06-13 22:36:07.336468
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    for entry_point_name in ENTRY_POINT_NAMES:
        for entry_point in iter_entry_points(entry_point_name):
            plugin_type = entry_point.load()
            assert issubclass(plugin_type, BasePlugin)

# Generated at 2022-06-13 22:36:17.875713
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(AesFormatter, GraphQLFormatter)
    plugin_manager.register(JsonFormatter, PrettyJsonFormatter)
    plugin_manager.register(GxmlFormatter, TxtFormatter, XmlFormatter)
    groups = plugin_manager.get_formatters_grouped()
    assert groups['json'] == [JsonFormatter, PrettyJsonFormatter]
    assert groups['xml'] == [GxmlFormatter, XmlFormatter]
    assert groups['other'] == [AesFormatter, GraphQLFormatter, TxtFormatter]


# Generated at 2022-06-13 22:36:21.153510
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    assert pm.get_auth_plugin_mapping() == {}
    pm.register(AuthPlugin)
    assert pm.get_auth_plugin_mapping() == {}


# Generated at 2022-06-13 22:36:32.650067
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # This unit test is written to verify the filter method of class PluginManager
    # The method returns only the subclass of the specified class
    # Unit test class definition
    class A:
        pass

    class B1(A):
        pass

    class B2(A):
        pass

    class C1(B1):
        pass

    class C2(B2):
        pass

    # the above classes are used to test the filter method
    # the definition is defined according to the tree structure of the class
    # test the effect of calling without parameters
    pm = PluginManager()
    pm.register(C1, C2)
    assert pm.filter() == [C1, C2]
    # test the effect of calling with class B1
    assert pm.filter(by_type=B1) == [C1]
    # test the effect

# Generated at 2022-06-13 22:36:39.164526
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert PluginManager().get_formatters_grouped()['Custom'] == [httpie.plugins.formatter.custom.CustomFormatter]
    assert PluginManager().get_formatters_grouped()['Colored'] == [httpie.plugins.formatter.colors.ColoredFormatter]
    assert PluginManager().get_formatters_grouped()['Browser'] == [httpie.plugins.formatter.browser.BrowserFormatter]
    assert PluginManager().get_formatters_grouped()['Json'] == [httpie.plugins.formatter.json.JSONFormatter]
    assert PluginManager().get_formatters_grouped()['Curl'] == [httpie.plugins.formatter.curl.CurlFormatter, httpie.plugins.formatter.curl_print.CurlPrintFormatter]
    assert PluginManager().get_format

# Generated at 2022-06-13 22:36:45.810975
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPBasicAuth
    p = PluginManager()
    p.load_installed_plugins()
    assert HTTPBasicAuth in p

# Generated at 2022-06-13 22:36:48.053851
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    m = PluginManager()
    m.register(1, 2, 3, 4, 5)
    assert m.filter(int) == [1, 2, 3, 4, 5]
    assert m.filter(str) == []

# Generated at 2022-06-13 22:36:52.735449
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.converter import Json, KeyValue
    pm = PluginManager()
    pm.register(Json, KeyValue)
    assert pm.filter(ConverterPlugin) == [Json, KeyValue]

# Generated at 2022-06-13 22:36:59.988313
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import DEFAULT_TRANSPORT_PLUGINS
    pm = PluginManager()
    pm.load_installed_plugins()
    loaded_transport_plugins = pm.get_transport_plugins()
    assert loaded_transport_plugins == DEFAULT_TRANSPORT_PLUGINS


# Generated at 2022-06-13 22:37:08.568258
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.formatter.pretty import PrettyFormatter
    from httpie.plugins.formatter.json import JSONFormatter

    manager = PluginManager()
    assert manager.get_formatters_grouped() == {}

    manager.register(PrettyFormatter)
    manager.register(JSONFormatter)
    result = manager.get_formatters_grouped()['Output processing']
    assert PrettyFormatter in result
    assert JSONFormatter in result

# Generated at 2022-06-13 22:37:17.970123
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    from httpie.plugins import AUTH, FORMATTERS, CONVERTERS, TRANSPORT
    from httpie.plugins.builtin import (
            HTTPBasicAuthPlugin, DigestAuthPlugin, OAuth1Plugin, OAuth2Plugin
    )

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert plugin_manager.get_auth_plugins() == [
        HTTPBasicAuthPlugin, DigestAuthPlugin, OAuth1Plugin, OAuth2Plugin
    ]

    assert plugin_manager.get_forma

# Generated at 2022-06-13 22:37:22.494437
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(*ENTRY_POINT_NAMES)
    assert pm.filter() == ENTRY_POINT_NAMES


# Generated at 2022-06-13 22:37:25.417866
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) >= 10

# Generated at 2022-06-13 22:37:31.940815
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()

    assert len(manager.get_auth_plugins()) > 0
    assert len(manager.get_formatters()) > 0
    assert len(manager.get_converters()) > 0
    assert len(manager.get_transport_plugins()) > 0



# Generated at 2022-06-13 22:37:37.346229
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_mgr = PluginManager()
    plugin_mgr.load_installed_plugins()
    assert len(plugin_mgr.get_auth_plugins()) > 0
    assert len(plugin_mgr.get_formatters()) > 0
    assert len(plugin_mgr.get_converters()) > 0
    assert len(plugin_mgr.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:37:46.752516
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager.register()
    try:
        PluginManager.load_installed_plugins()
    finally:
        PluginManager.unregister()



# Generated at 2022-06-13 22:37:55.885994
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()

    class Formatter1(FormatterPlugin):
        group_name = 'group1'
        group_title = 'Group 1'
        group_order = 1
        group_index = 0

    class Formatter2(FormatterPlugin):
        group_name = 'group1'
        group_title = 'Group 1'
        group_order = 1
        group_index = 1

    class Formatter3(FormatterPlugin):
        group_name = 'group2'
        group_title = 'Group 2'
        group_order = 2
        group_index = 0

    manager.register(Formatter1, Formatter2)

    # test case 1
    assert manager.get_formatters_grouped() == {
        'group1': [Formatter1, Formatter2]
    }

    manager.register

# Generated at 2022-06-13 22:38:01.791779
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class TestPluginManager(PluginManager):
        def __init__(self):
            self.load_installed_plugins()
    test_PluginManager = TestPluginManager()
    assert len(test_PluginManager) > 0

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:38:07.645321
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
   plugin_manager = PluginManager()
   plugin_manager.register(HtmlFormatter, JsonFormatter, PrettyJsonFormatter)
   grouped_formatters = plugin_manager.get_formatters_grouped()
   assert len(grouped_formatters['json']) == 2


plugins = PluginManager()

# Generated at 2022-06-13 22:38:13.602805
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from io import StringIO
    from .tests.httpie.plugins.test_auth import DummyAuthPlugin, DummyAuthPlugin2
    from .tests.httpie.plugins.test_formatter import DummyFormatterPlugin
    from .tests.httpie.plugins.test_converter import DummyConverterPlugin
    from .tests.httpie.plugins.test_transport import DummyTransportPlugin
    plugin_manager = PluginManager()
    plugin_manager.register(DummyAuthPlugin, DummyFormatterPlugin, DummyConverterPlugin, DummyAuthPlugin2, DummyTransportPlugin)

    assert plugin_manager.get_auth_plugin_mapping() == {'dummy': DummyAuthPlugin, 'dummy2': DummyAuthPlugin2}



# Generated at 2022-06-13 22:38:26.085771
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.output.formatter import FormatterPlugin
    from httpie.plugins.output.converter import ConverterPlugin
    from httpie.plugins.auth.basic import BasicAuthPlugin
    from httpie.plugins.transport.http import HTTPTransport

    formatter_plugin: FormatterPlugin = FormatterPlugin()
    converter_plugin: ConverterPlugin = ConverterPlugin()
    basic_auth_plugin: BasicAuthPlugin = BasicAuthPlugin()
    http_transport: HTTPTransport = HTTPTransport()

    plugin_manager = PluginManager()
    plugin_manager.register(
        formatter_plugin,
        converter_plugin,
        basic_auth_plugin,
        http_transport,
    )

    assert plugin_manager.filter(FormatterPlugin) == [formatter_plugin]
    assert plugin_manager.filter

# Generated at 2022-06-13 22:38:37.098522
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # create a PluginManager object
    plugin_mgr = PluginManager()

    # create objects of BasePlugin class with plugin name
    class BasePlugin1(BasePlugin):
        pass

    class BasePlugin2(BasePlugin):
        pass

    class BasePlugin3(BasePlugin):
        pass

    class BasePlugin4(BasePlugin):
        pass

    class BasePlugin5(BasePlugin):
        pass

    plugin_mgr.register(BasePlugin1, BasePlugin2, BasePlugin3, BasePlugin4, BasePlugin5)

    class BasePlugin6(BasePlugin):
        pass

    pluginType = BasePlugin

    plugins = plugin_mgr.filter(pluginType)
    assert BasePlugin1 in plugins
    assert BasePlugin2 in plugins
    assert BasePlugin3 in plugins
    assert BasePlugin4 in plugins
    assert BasePlugin5 in plugins
   

# Generated at 2022-06-13 22:38:44.943220
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import AuthPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import TransportPlugin

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager.get_converters()) > 1
    assert len(plugin_manager.get_formatters()) > 1
    assert len(plugin_manager.get_transport_plugins()) > 1
    assert len(plugin_manager.get_auth_plugins()) > 1


# Generated at 2022-06-13 22:38:49.076716
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager.register(AuthPlugin)
    PluginManager.register(ConverterPlugin)
    PluginManager.register(FormatterPlugin)
    PluginManager.register(TransportPlugin)


# Generated at 2022-06-13 22:38:56.070758
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import TerminalPlugin
    from httpie.plugins import TerminalFormatter
    pm = PluginManager()
    pm.register(TerminalFormatter)
    group = pm.get_formatters_grouped()
    assert group == {'terminal': [TerminalFormatter]}

if __name__ == '__main__':
    test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:39:11.984470
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert True

# Generated at 2022-06-13 22:39:15.862936
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print('Unit test for method load_installed_plugins of class PluginManager')

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    print(plugin_manager)
    print('Test passed')


# Generated at 2022-06-13 22:39:28.228720
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    fake_plugin = type('FakePlugin', (BasePlugin,), {})
    fake_entry_point = type('FakeEntryPoint', (), {
        'load': lambda: fake_plugin,
        'name': '',
        'dist': type('FakeDistribution', (), {
            'key': ''
        })
    })
    fake_entry_point_group = type('FakeEntryPointGroup', (), {
        'name':'',
        'iter_entry_points': lambda : [fake_entry_point]
    })
    plugin_manager = PluginManager()
    plugin_manager.register = lambda x: None
    plugin_manager.append = lambda x: None
    plugin_manager.load_installed_plugins(
        entry_point_groups=[fake_entry_point_group]
    )
    assert plugin_manager.get_auth_plugin

# Generated at 2022-06-13 22:39:37.257795
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():

    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.httpie.auth import HTTPieHTTPBasicAuth
    from httpie.plugins.test.test_auth import TestAuthPlugin
    from httpie.plugins.auth import AuthPlugin
    from httpie.plugins import builtin

    p = PluginManager()

    p.register(TestAuthPlugin, HTTPieHTTPBasicAuth, builtin.HTTPBasicAuth)
    assert p.get_auth_plugin_mapping() == {
        'test': TestAuthPlugin,
        'basic': HTTPBasicAuth
    }

# Generated at 2022-06-13 22:39:39.806150
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.append(Type[FormatterPlugin])
    manager.get_formatters_grouped() == {'group_name': [Type[FormatterPlugin]]}

# Generated at 2022-06-13 22:39:52.505594
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # fake plugins
    class AuthPlugin1(AuthPlugin):
        auth_type = "AuthPlugin1"
    class AuthPlugin2(AuthPlugin):
        auth_type = "AuthPlugin2"
    class FormatterPlugin1(FormatterPlugin):
        group_name = "FormatterPlugin1"
    class FormatterPlugin2(FormatterPlugin):
        group_name = "FormatterPlugin2"
    class ConverterPlugin1(ConverterPlugin):
        content_type = "ConverterPlugin1"
    class ConverterPlugin2(ConverterPlugin):
        content_type = "ConverterPlugin2"
    class TransportPlugin1(TransportPlugin):
        name = "TransportPlugin1"
    class TransportPlugin2(TransportPlugin):
        name = "TransportPlugin2"

    manager = PluginManager()

# Generated at 2022-06-13 22:40:00.293158
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Create a PluginManager object
    plugin_manager = PluginManager()

    # Add a formatter to the plugin manager and determine the formatters in that group
    plugin_manager.register(JSONPrettyPlugin)

    assert plugin_manager.get_formatters_grouped() == {'json': [JSONPrettyPlugin]}

    # Add another formatter with the same group and get the formatters in that group
    plugin_manager.register(JSONStreamPlugin)

    assert plugin_manager.get_formatters_grouped() == {'json': [JSONPrettyPlugin, JSONStreamPlugin]}

    # Remove a formatter from the plugin manager and get the formatters in that group
    plugin_manager.unregister(JSONPrettyPlugin)

    assert plugin_manager.get_formatters_grouped() == {'json': [JSONStreamPlugin]}

    # Remove remaining formatter from the plugin

# Generated at 2022-06-13 22:40:06.781317
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins import builtin
    from . import builtin as client_builtin
    from . import server_auth as server_auth
    from . import server_auth_v2 as server_auth_v2
    from . import session as session
    plugin_manager=PluginManager()
    plugin_manager.register(*client_builtin.plugins)
    plugin_manager.register(*builtin.plugins)
    plugin_manager.register(*server_auth.plugins)
    plugin_manager.register(*server_auth_v2.plugins)
    plugin_manager.register(*session.plugins)
    plugin_manager.load_installed_plugins()
    print(plugin_manager.get_auth_plugin_mapping())


# Generated at 2022-06-13 22:40:17.976936
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    import os
    import sys
    import glob
    import httpie.plugins.auth.v1 as ha
    import httpie.plugins.formatter.v1 as hf
    import httpie.plugins.converter.v1 as hc
    import httpie.plugins.transport.v1 as htt

    # Remove old *.pyc files to be able to load modification plugins
    for pyc in glob.glob('*/**/*.pyc', recursive=True):
        os.remove(pyc)

    p = PluginManager()
    p.unregister(ha.BasicAuthPlugin)
    p.unregister(ha.DigestAuthPlugin)
    p.unregister(hf.JSONFormatterPlugin)
    p.unregister(hf.PrettyJSONFormatterPlugin)

# Generated at 2022-06-13 22:40:21.875678
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    auth_plugins = PluginManager().get_auth_plugin_mapping()
    print(auth_plugins)
    assert 1 == 1

if __name__ == "__main__":
    test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:40:39.792757
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    print(plugins)


# Generated at 2022-06-13 22:40:41.973262
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert(isinstance(plugins, PluginManager))


# Generated at 2022-06-13 22:40:45.408887
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(type(plugin_manager))
    print(plugin_manager)
    print(plugin_manager.get_auth_plugins())


if __name__ == "__main__":
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:40:56.415040
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = [
        class_('httpie.format.formatters.json.JSONFormatter', 'JSONFormatter'),
        class_('httpie.format.formatters.terminal.TerminalFormatter', 'TerminalFormatter'),
        class_('httpie.format.formatters.terminal.TerminalFormatter', 'TerminalFormatter')
    ]

    plugin_manager = PluginManager()
    plugin_manager.register(*formatters)

    assert plugin_manager.get_formatters_grouped() == {
        'json': [formatters[0]],
        'terminal': [formatters[1], formatters[2]]
    }


class_ = namedtuple('class', 'module_name,name')

# Generated at 2022-06-13 22:41:05.006992
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin

    class CustomFormatter(FormatterPlugin):
        group_name = 'group1'

    class CustomFormatter2(FormatterPlugin):
        group_name = 'group2'

    class CustomFormatter3(FormatterPlugin):
        group_name = 'group2'

    pm = PluginManager()
    pm.register(CustomFormatter)
    pm.register(CustomFormatter2)
    pm.register(CustomFormatter3)
    assert pm.get_formatters_grouped() == {'group1': [CustomFormatter], 'group2': [CustomFormatter2, CustomFormatter3]}



# Generated at 2022-06-13 22:41:09.351023
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()

    print(pluginManager.get_formatters_grouped())

if __name__ == '__main__':
    test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:41:13.867212
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager
    print('Unit test for method load_installed_plugins of class PluginManager:')
    print('Test successful!\n')


# Generated at 2022-06-13 22:41:23.989199
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    global_manager = PluginManager()
    
    global_manager.register(second_auth, second_formatter, second_converter, second_transport)
    global_manager.register(first_auth, first_formatter, first_converter, first_transport)

    assert type(global_manager.filter()) == list
    assert global_manager.filter() == [second_auth, second_formatter, second_converter, second_transport, first_auth, first_formatter, first_converter, first_transport]
    assert global_manager.filter(Type) == []
    assert global_manager.filter(ConverterPlugin) == [second_converter, first_converter]
    assert global_manager.filter(TransportPlugin) == [second_transport, first_transport]

# Generated at 2022-06-13 22:41:29.698005
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class TestPluginManager(PluginManager):
        def load_installed_plugins(self):
            super().load_installed_plugins()
            assert sorted(self.get_auth_plugin_mapping().keys()) == ['aws-sigv4']

    test_PluginManager = TestPluginManager()
    test_PluginManager.load_installed_plugins()

# Generated at 2022-06-13 22:41:32.510934
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    res = pluginmanager.get_auth_plugin_mapping()
    assert res['oauth1'] == httpie.plugins.auth.oauth1.OAuth1AuthPlugin


# Generated at 2022-06-13 22:42:06.047334
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert len(PluginManager().filter()) == 0
    assert len(PluginManager().register(object).filter(object)) == 1
    assert len(PluginManager().register(object).filter(str)) == 0

manager = PluginManager()
manager.load_installed_plugins()

# Generated at 2022-06-13 22:42:10.974970
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    l=PluginManager()
    l.register(JsonPlugin)
    l.register(ColorsPlugin)
    l.register(PrettyPlugin)
    l.register(RcPlugin)
    l.register(JsonLinesPlugin)
    d=l.get_formatters_grouped()
    assert d['Group1'] == [JsonPlugin, JsonLinesPlugin]
    assert d['Group2'] == [ PrettyPlugin]
    assert d['Group3'] == [ColorsPlugin]
    assert d['Group4'] == [RcPlugin]


# Generated at 2022-06-13 22:42:13.643460
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert isinstance(PluginManager().load_installed_plugins(),
                      PluginManager)


# Generated at 2022-06-13 22:42:17.469772
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginManager = PluginManager()
    assert PluginManager.get_auth_plugin_mapping() == {}
    PluginManager.register(auth_type)
    assert PluginManager.get_auth_plugin_mapping() == {'test': auth_type}


# Generated at 2022-06-13 22:42:19.987832
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pg = PluginManager()
    pg.load_installed_plugins()
    assert len(pg) > 0

# Generated at 2022-06-13 22:42:31.279790
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """Unit test for method get_formatters_grouped of class PluginManager
    """
    from httpie.plugins import formatter

    # Remove plugins
    for plugin in formatter.__all__:
        if isinstance(plugin, list):
            for p in plugin:
                formatter.__all__.remove(p)
        else:
            formatter.__all__.remove(plugin)

    # Append plugins to test
    formatter.__all__.append('NewLineFormatterPlugin')
    formatter.__all__.append('TextApartFormatterPlugin')

    class NewLineFormatterPlugin(FormatterPlugin):
        name = 'new'
        group_name = 'new'
        description = 'new'

    class TextApartFormatterPlugin(FormatterPlugin):
        name = 'text'

# Generated at 2022-06-13 22:42:44.760340
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = []
    class FormatA(FormatterPlugin):
        group_name = 'A'
    class FormatA1(FormatterPlugin):
        group_name = 'A'
    class FormatA2(FormatterPlugin):
        group_name = 'A'
    class FormatB(FormatterPlugin):
        group_name = 'B'
    class FormatB1(FormatterPlugin):
        group_name = 'B'
    class FormatB2(FormatterPlugin):
        group_name = 'B'
    plugins.append(FormatA())
    plugins.append(FormatA1())
    plugins.append(FormatA2())
    plugins.append(FormatB())
    plugins.append(FormatB1())
    plugins.append(FormatB2())
    plugins_manager = PluginManager(plugins)
    assert plugins_manager.get

# Generated at 2022-06-13 22:42:49.947539
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_formatters()) == 8
    assert len(plugin_manager.get_formatters_grouped()) == 2
    assert len(plugin_manager.get_converters()) == 9
    assert len(plugin_manager.get_auth_plugins()) == 6
    assert len(plugin_manager.get_auth_plugin_mapping()) == 6
    assert len(plugin_manager.get_transport_plugins()) == 2

# Generated at 2022-06-13 22:42:55.203244
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Plugin1(BasePlugin): pass
    class Plugin2(Plugin1): pass
    class Plugin3(Plugin2): pass

    plugins = PluginManager()
    plugins.register(Plugin1, Plugin2, Plugin3)



# Generated at 2022-06-13 22:42:58.025908
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    print(PluginManager().filter(base_plugin.BasePlugin))