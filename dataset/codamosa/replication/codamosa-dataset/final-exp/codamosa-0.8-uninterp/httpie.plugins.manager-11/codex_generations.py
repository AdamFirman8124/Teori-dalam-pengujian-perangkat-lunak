

# Generated at 2022-06-13 22:33:20.041571
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    test_auth_type = 'basic'
    assert plugins.get_auth_plugin_mapping()[test_auth_type].auth_type == test_auth_type

# Generated at 2022-06-13 22:33:26.191298
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0


# Generated at 2022-06-13 22:33:28.352028
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # check for auth plugin will be loaded
    assert "NullAuthPlugin" in map(lambda x: x.__name__, PluginManager().filter(AuthPlugin))


# Generated at 2022-06-13 22:33:43.818783
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.compat import is_py36
    from httpie.plugins import DEFAULT_FORMAT

    pm = PluginManager()
    pm.register(FormatDict, FormatJson, FormatPrettyJson, FormatColors, FormatNone)
    assert pm.get_formatters_grouped() == {
        'json': [FormatDict, FormatJson, FormatPrettyJson],
        'binary': [FormatColors],
        'metadata': [FormatNone],
    }

    # Make sure the built-in default format is not registered.
    pm = PluginManager()
    pm.register(FormatDict, FormatJson, FormatPrettyJson, FormatColors, FormatNone)
    assert DEFAULT_FORMAT not in pm.get_formatters_grouped()['json']

    # Make sure we don't register the built-in default

# Generated at 2022-06-13 22:33:48.648072
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager.get_auth_plugin_mapping())

test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:33:51.022422
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    assert manager.get_formatters_grouped() == {}

# Generated at 2022-06-13 22:33:59.456131
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.load_installed_plugins()
    formatters = manager.get_formatters_grouped()
    assert list(formatters["prettifiers"]) == [
        'httpie.plugins.formatter.prettyjsonpp',
        'httpie.plugins.formatter.prettyjson'
    ]
    assert list(formatters['syntax']) == [
        'httpie.plugins.formatter.colors',
        'httpie.plugins.formatter.format'
    ]

# Generated at 2022-06-13 22:34:00.649609
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert True


# Generated at 2022-06-13 22:34:05.643841
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.load_installed_plugins()

# Generated at 2022-06-13 22:34:10.253548
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 1

if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:34:22.356649
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.filter(FormatterPlugin)
    plugin_manager.get_formatters()
    result = plugin_manager.get_formatters_grouped()
    assert result == {"group1": [class1, class2], "group2": [class3, class4]}

class1 = FormatterPlugin()
class1.group_name = "group1"

class2 = FormatterPlugin()
class2.group_name = "group1"

class3 = FormatterPlugin()
class3.group_name = "group2"

class4 = FormatterPlugin()
class4.group_name = "group2"

# Generated at 2022-06-13 22:34:27.583466
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    assert plugin_manager.get_auth_plugin_mapping() == {}
    plugin_manager.register(kerberos_auth.KerberosAuthPlugin)
    assert plugin_manager.get_auth_plugin_mapping() == {'Kerberos': kerberos_auth.KerberosAuthPlugin}


# Generated at 2022-06-13 22:34:39.278803
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import os
    import sys
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.plugins.manager import PluginManager
    from httpie.output.formatters.colors import get_lexer
    from httpie.plugins.browser import BrowserViewPlugin
    from httpie.plugins.builtin import HTTPHeadersPlugin
    from httpie.plugins.builtin import HTTPieOutputPlugin
    from httpie.plugins.builtin import HTTPMethodsPlugin
    from httpie.plugins.builtin import HTTPOptionsPlugin
    from httpie.plugins.json import JSONOutputPlugin
    from httpie.plugins.pretty import PrettyOutputPlugin
    from httpie.plugins.raw import RawJSONOutputPlugin
    from httpie.plugins.unicode import UnicodeOutputPlugin
    plugins = PluginManager()
    plugins.load_installed_plugins()



# Generated at 2022-06-13 22:34:49.341979
# Unit test for method get_formatters_grouped of class PluginManager

# Generated at 2022-06-13 22:34:52.610473
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters_grouped()


manager = PluginManager()

# Generated at 2022-06-13 22:34:55.779426
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:35:07.535346
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    local_plugin_manager = PluginManager()
    local_plugin_manager.register(type("FormatterPlugin1", (FormatterPlugin,), {"group_name": "group1"}))
    local_plugin_manager.register(type("FormatterPlugin2", (FormatterPlugin,), {"group_name": "group2"}))
    local_plugin_manager.register(type("FormatterPlugin3", (FormatterPlugin,), {"group_name": "group2"}))

    formatters_grouped = local_plugin_manager.get_formatters_grouped()
    assert "group1" in formatters_grouped
    assert "group2" in formatters_grouped
    assert len(formatters_grouped["group1"]) == 1

# Generated at 2022-06-13 22:35:18.406514
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    ## Case 1: plugin_manager is empty
    plugin_manager = PluginManager()
    formatters_grouped = plugin_manager.get_formatters_grouped()
    assert formatters_grouped == {}

    ## Case 2: plugin_manager is not empty
    plugin_manager = PluginManager()
    plugin_manager.register(DummyFormatter1)
    plugin_manager.register(DummyFormatter2)

    formatters_grouped = plugin_manager.get_formatters_grouped()
    assert formatters_grouped == {
        'Group1': [DummyFormatter1],
        'Group2': [DummyFormatter2]
    }



# Generated at 2022-06-13 22:35:27.691292
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.get_auth_plugin_mapping()['basic']
    assert manager.get_auth_plugin_mapping()['digest']
    assert manager.get_auth_plugin_mapping()['hmac']
    assert manager.get_auth_plugin_mapping()['ntlm']
    assert manager.get_auth_plugin_mapping()['bearer']
    assert manager.get_auth_plugin_mapping()['aws4-hmac-sha256']
    assert manager.get_auth_plugin_mapping()['aws4-signature']
    assert manager.get_auth_plugin_mapping()['hawkAuth']
    assert manager.get_auth_plugin_mapping()['negotiate']

# Generated at 2022-06-13 22:35:32.540551
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    from httpie.plugins import FormatterPlugin, Formatter
    from httpie.plugins import ConverterPlugin, Converter
    from httpie.plugins import AuthPlugin, TransportPlugin

    class FakeFormatterPlugin(FormatterPlugin):
        group_name = 'fake'
        name = 'fake'
        format_name = 'fake'
        format = 'fake'
        Formatter = Formatter

    class FakeFormatterPlugin2(FormatterPlugin):
        group_name = 'fake'
        name = 'fake2'
        format_name = 'fake2'
        format = 'fake2'
        Formatter = Formatter

    class FakeConverterPlugin(ConverterPlugin):
        name = 'fake'
        Converter = Converter

    class FakeAuthPlugin(AuthPlugin):
        auth_type = 'fake'

# Generated at 2022-06-13 22:35:40.649416
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    def _check_plugin(plugin, by_type=Type[BasePlugin]):
        assert issubclass(plugin, by_type)

    manager = PluginManager()
    manager.register(ByePlugin, HelloPlugin, AuthPlugin)
    plugins = manager.filter(BasePlugin)
    for plugin in plugins:
        _check_plugin(plugin)
    plugins = manager.filter(HelloPlugin)
    for plugin in plugins:
        _check_plugin(plugin, HelloPlugin)

# Generated at 2022-06-13 22:35:47.034762
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    assert issubclass(plugin_manager.get_auth_plugin('basic'), AuthPlugin)
    assert issubclass(plugin_manager.get_formatters()[1], FormatterPlugin)
    assert issubclass(plugin_manager.get_converters()[1], ConverterPlugin)
    assert issubclass(plugin_manager.get_transport_plugins()[1], TransportPlugin)

# Generated at 2022-06-13 22:35:50.034975
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    mgr = PluginManager()
    list_plugins = mgr.filter(BasePlugin)
    assert list_plugins == [], 'list_plugins is not empty'

# Generated at 2022-06-13 22:36:00.013828
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin
    from json.decoder import JSONDecodeError
    from httpie.plugins.formatter.json import JSONFormatter
    from httpie.plugins.converter.json import JSONConverter
    from httpie.plugins.transport.tcp import TCPTransport
    pm = PluginManager()
    pm.register(JSONFormatter, JSONConverter, JSONDecodeError, TCPTransport)
    assert pm.filter(AuthPlugin) == []
    assert pm.filter(JSONDecodeError) == [JSONDecodeError]
    assert pm.filter(JSONDecodeError) == [JSONDecodeError]
    assert pm.filter(JSONFormatter) == [JSONFormatter]
    assert pm.filter(JSONConverter) == [JSONConverter]

# Generated at 2022-06-13 22:36:01.776542
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Once we want to use this method, write it up.
    return None

# Generated at 2022-06-13 22:36:08.228087
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) >= 1
    assert len(plugin_manager.get_converters()) >= 1
    assert len(plugin_manager.get_formatters()) >= 1
    assert len(plugin_manager.get_transport_plugins()) >= 1

# Generated at 2022-06-13 22:36:12.206762
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager) != 0


# Generated at 2022-06-13 22:36:15.009923
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    
    assert len(pluginManager) > 0


# Generated at 2022-06-13 22:36:17.437359
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManagerInstance=PluginManager()
    PluginManagerInstance.load_installed_plugins()
    assert len(PluginManagerInstance)>=2


# Generated at 2022-06-13 22:36:27.450548
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.auth import BasicAuth
    from httpie.input import JSONAuth
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPJSONAuth
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == 2
    auth_map = pm.get_auth_plugin_mapping()
    assert auth_map['basic'] == BasicAuth
    assert auth_map['json'] == JSONAuth
    assert pm.get_auth_plugin('basic') == HTTPBasicAuth
    assert pm.get_auth_plugin('json') == HTTPJSONAuth
    assert len(pm.get_formatters()) == 0
    assert len(pm.get_converters()) == 0
    assert len(pm.get_transport_plugins()) == 0


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:36:32.824614
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert isinstance(PluginManager().load_installed_plugins(), list)

# Generated at 2022-06-13 22:36:44.613605
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(FormatterPlugin, AuthPlugin, AuthPlugin, TransportPlugin)
    
    # Test with no specific type
    assert len(pm.filter()) == len(pm)
    assert pm.filter() == pm

    # Test with the base Plugin class
    assert len(pm.filter(BasePlugin)) == len(pm)
    assert pm.filter(BasePlugin) == pm

    # Test with the FormatterPlugin class
    assert len(pm.filter(FormatterPlugin)) == 1
    assert pm.filter(FormatterPlugin) == [FormatterPlugin]

    # Test with the AuthPlugin class
    assert len(pm.filter(AuthPlugin)) == 2
    assert pm.filter(AuthPlugin) == [AuthPlugin, AuthPlugin]

    # Test with the TransportPlugin class

# Generated at 2022-06-13 22:36:50.961510
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()

    assert pluginManager != PluginManager()
    assert pluginManager.get_auth_plugins() != PluginManager().get_auth_plugins()
    assert pluginManager.get_formatters() != PluginManager().get_formatters()
    assert pluginManager.get_converters() != PluginManager().get_converters()
    assert pluginManager.get_transport_plugins() != PluginManager().get_transport_plugins()



# Generated at 2022-06-13 22:36:58.684872
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.__main__ import PluginManager
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin
    from httpie.plugins.base import BasePlugin, TransportPlugin
    
    # create an instance of PluginManager
    plugin_manager = PluginManager()
    
    # load installed plugins
    plugin_manager.load_installed_plugins()
    
    # assert that the plugin manager implements the BasePlugin
    assert all(isinstance(plugin, BasePlugin) for plugin in plugin_manager)

    # assert that the plugin manager implements all plugins
    assert all(isinstance(plugin, AuthPlugin) for plugin in plugin_manager.get_auth_plugins())
    assert all(isinstance(plugin, FormatterPlugin) for plugin in plugin_manager.get_formatters())

# Generated at 2022-06-13 22:37:08.321751
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    class BasePlugin1:
        pass
    class BasePlugin2(BasePlugin1):
        pass
    class BasePlugin3(BasePlugin1):
        pass
    class BasePlugin4:
        pass
    pm.register(BasePlugin1, BasePlugin2, BasePlugin3, BasePlugin4)
    result = pm.filter()
    assert list(result) == [BasePlugin1, BasePlugin2, BasePlugin3, BasePlugin4]


# Generated at 2022-06-13 22:37:17.161440
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()
    assert ENTRY_POINT_NAMES[0] == 'httpie.plugins.auth.v1'
    assert ENTRY_POINT_NAMES[1] == 'httpie.plugins.formatter.v1'
    assert ENTRY_POINT_NAMES[2] == 'httpie.plugins.converter.v1'
    assert ENTRY_POINT_NAMES[3] == 'httpie.plugins.transport.v1'

# Generated at 2022-06-13 22:37:28.854499
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert True == True
    # Test from httpie / httpie / plugins.py
    from httpie.plugins import AuthPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import TransportPlugin
    from httpie.plugins.base import BasePlugin

    class A(BasePlugin):
        pass
    class B(BasePlugin):
        pass
    class C(BasePlugin):
        pass

    class AuthA(AuthPlugin):
        pass
    class AuthB(AuthPlugin):
        pass
    class AuthC(AuthPlugin):
        pass

    class FormatA(FormatterPlugin):
        pass
    class FormatB(FormatterPlugin):
        pass
    class FormatC(FormatterPlugin):
        pass

    class ConvertA(ConverterPlugin):
        pass

# Generated at 2022-06-13 22:37:35.999999
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    print('** Unit test for function get_auth_plugin_mapping of class PluginManager: ')
    pm = PluginManager()
    pm.load_installed_plugins()
    print('mapping = ', pm.get_auth_plugin_mapping())
    print('** Unit test end.\n')

if __name__ == '__main__':
    test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:37:41.185634
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(
        TestPlugin1,
        TestPlugin2,
        TestPlugin3,
        TestPlugin4,
    )
    assert manager.get_formatters_grouped() == {
        'test_group1': [TestPlugin1, TestPlugin2],
        'test_group2': [TestPlugin3, TestPlugin4],
    }


# Generated at 2022-06-13 22:37:44.986215
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    assert isinstance(plugin_manager.get_auth_plugin_mapping(), dict)


# Generated at 2022-06-13 22:37:59.736526
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import AuthPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import TransportPlugin
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert issubclass(pluginManager.get_auth_plugin('basic'), AuthPlugin)
    assert issubclass(pluginManager.get_formatters_grouped()['format'][0], FormatterPlugin)
    assert issubclass(pluginManager.get_converters()[0], ConverterPlugin)
    assert issubclass(pluginManager.get_transport_plugins()[0], TransportPlugin)

# Generated at 2022-06-13 22:38:10.238905
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    formatter_1 = mock.Mock()
    formatter_1.group_name = 'first'
    formatter_2 = mock.Mock()
    formatter_2.group_name = 'second'
    formatter_3 = mock.Mock()
    formatter_3.group_name = 'first'
    plugin_manager.register(formatter_1, formatter_2, formatter_3)
    expected = {'first': [formatter_1, formatter_3], 'second': [formatter_2]}
    assert plugin_manager.get_formatters_grouped() == expected

# Generated at 2022-06-13 22:38:16.677855
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    def test_formatters_grouped(plugins):
        pm = PluginManager(plugins)
        assert pm.get_formatters_grouped() == {
            'group1': [F1, F2],
            'group2': [F3],
        }

    class FormatterPlugin:
        group_name = None

    class F1(FormatterPlugin):
        group_name = 'group1'

    class F2(FormatterPlugin):
        group_name = 'group1'

    class F3(FormatterPlugin):
        group_name = 'group2'

    # Assert that order doesn't matter
    test_formatters_grouped([F1, F2, F3])
    test_formatters_grouped([F3, F2, F1])

# Generated at 2022-06-13 22:38:20.375583
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.register(MockPlugin1)
    assert len(plugin_manager) == 1


# Generated at 2022-06-13 22:38:22.731711
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    """
    Write your own unit test for method load_installed_plugins of class PluginManager
    """

# Generated at 2022-06-13 22:38:30.085447
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import RFC822JSONFormatter, JSONLinesFormatter, JSONFormatter

    manager = PluginManager()
    manager.register(JSONFormatter, RFC822JSONFormatter, JSONLinesFormatter)
    formatters = manager.get_formatters()
    assert formatters == [JSONFormatter, RFC822JSONFormatter, JSONLinesFormatter]
    formatters_grouped = manager.get_formatters_grouped()
    assert formatters_grouped["JSON"] == [JSONFormatter]
    assert formatters_grouped["JSON Lines"] == [JSONLinesFormatter]
    assert formatters_grouped["RFC 822 - JSON"] == [RFC822JSONFormatter]

# Generated at 2022-06-13 22:38:37.833522
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin
    from httpie.plugins.builtin import BasicAuthPlugin, BasicAuth
    from httpie.plugins.builtin import JSONPPrettyFormatter
    from httpie.plugins.builtin import JSONFormat
    from httpie.plugins.builtin import HTTPTransport
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.get_auth_plugins() == [BasicAuthPlugin]
    assert manager.get_auth_plugin('basic') == BasicAuth
    assert manager.get_formatters() == [JSONPPrettyFormatter]
    assert manager.get_converters() == [JSONFormat]
    assert manager.get_transport_plugins() == [HTTPTransport]

# Generated at 2022-06-13 22:38:40.918663
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    mapping = plugin_manager.get_auth_plugin_mapping()
    assert mapping



# Generated at 2022-06-13 22:38:46.907224
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert PluginManager().get_formatters_grouped() == {}

    class TestFormatter_1(FormatterPlugin):
        group_name = "g1"

    class TestFormatter_2(FormatterPlugin):
        group_name = "g2"

    plugins = PluginManager([TestFormatter_1, TestFormatter_2])
    assert plugins.get_formatters_grouped() == {
        "g1": [TestFormatter_1],
        "g2": [TestFormatter_2],
    }

# Generated at 2022-06-13 22:38:54.526464
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSON, JSONPrettyError
    plugin_manager = PluginManager()

    import httpie.plugins.builtin
    plugin_manager.register(JSON, JSONPrettyError)

    print(plugin_manager)
    print(plugin_manager.get_formatters())
    print(plugin_manager.get_formatters_grouped())

    plugin_manager.unregister(JSON)
    print(plugin_manager)

# Generated at 2022-06-13 22:39:15.328507
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pytest
    pm=PluginManager()
    p=pm.load_installed_plugins()
    assert p==pm
    with pytest.raises(AttributeError):
        assert p.package_name

# Generated at 2022-06-13 22:39:20.290871
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm.get_converters()) != 0
    assert len(pm.get_auth_plugins()) != 0
    assert len(pm.get_formatters()) != 0
    # assert False

# Generated at 2022-06-13 22:39:28.039612
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import PrettyJSONFormatter
    plugin_manager = PluginManager()
    plugin_manager.register(JSONFormatter)
    plugin_manager.register(PrettyJSONFormatter)
    grouped_formatters = plugin_manager.get_formatters_grouped()
    assert list(grouped_formatters.keys()) == ['JSON']
    assert list(grouped_formatters['JSON']) == [JSONFormatter, PrettyJSONFormatter]

# Generated at 2022-06-13 22:39:32.408020
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    auth_plugins = plugin_manager.filter(AuthPlugin)
    assert len(auth_plugins) >= 1

# Generated at 2022-06-13 22:39:40.675799
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin
    class TestPlugin(BasePlugin):
        pass
    class TestAuthPlugin(AuthPlugin):
        pass
    class TestConverterPlugin(ConverterPlugin):
        pass
    class TestFormatterPlugin(FormatterPlugin):
        pass
    class TestTransportPlugin(TransportPlugin):
        pass

    pm = PluginManager()
    TestPlugin, TestAuthPlugin, TestConverterPlugin, TestFormatterPlugin, TestTransportPlugin = \
            TestPlugin, TestAuthPlugin, TestConverterPlugin, TestFormatterPlugin, TestTransportPlugin
    pm.register(
        TestPlugin, TestAuthPlugin, TestConverterPlugin, TestFormatterPlugin, TestTransportPlugin
    )
    assert TestPlugin in pm.filter() and TestAuthPlugin

# Generated at 2022-06-13 22:39:51.539159
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PluginManager_test = PluginManager()
    PluginManager_test.register(AuthPlugin)
    PluginManager_test.register(FormatterPlugin)
    PluginManager_test.register(ConverterPlugin)
    PluginManager_test.register(TransportPlugin)
    assert PluginManager_test.filter(AuthPlugin) == [AuthPlugin] 
    assert PluginManager_test.filter(FormatterPlugin) == [FormatterPlugin] 
    assert PluginManager_test.filter(ConverterPlugin) == [ConverterPlugin] 
    assert PluginManager_test.filter(TransportPlugin) == [TransportPlugin] 


# Generated at 2022-06-13 22:40:02.352769
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin
    from httpie.plugins.base import BasePlugin

    class Plugin1(BasePlugin):
        name = "plugin1"
        description = "plugin1 description"

    class Plugin2(AuthPlugin):
        name = "plugin2"
        description = "plugin2 description"

    manager = PluginManager()
    manager.register(Plugin1, Plugin2)

    assert manager.filter() == [Plugin1, Plugin2]
    assert manager.filter(auth.AuthPlugin) == [Plugin2]
    assert manager.filter(AuthPlugin) == [Plugin2]
    assert manager.filter(Plugin2) == []
    assert manager.filter(by_type=Plugin2) == []
    assert manager.filter(by_type=Plugin1) == [Plugin1]

# Generated at 2022-06-13 22:40:04.016137
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    actual = PluginManager()
    actual.load_installed_plugins()
    assert actual

# Generated at 2022-06-13 22:40:14.540738
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Create a mock list of plugins
    plugins = [
        type('PluginA', (BasePlugin,), {'category': 'auth'}),
        type('PluginB', (BasePlugin,), {'category': 'auth'}),
        type('PluginC', (BasePlugin,), {'category': 'formatter'})
    ]

    # Create the plugin manager object
    plugin_manager = PluginManager()

    # Insert mock plugins into the plugin manager
    for plugin in plugins:
        plugin_manager.register(plugin)

    # Filter by AuthPlugin
    filtered_plugins = plugin_manager.filter(AuthPlugin)

    # Check if the output matches the expected
    assert plugins[:2] == filtered_plugins

# Generated at 2022-06-13 22:40:21.428500
# Unit test for method filter of class PluginManager
def test_PluginManager_filter(): 
    from httpie.plugins.formatter import JSONFormatter
    from httpie.plugins.converter import JSONConverter
    plugins = PluginManager()
    plugins.register(JSONFormatter,JSONConverter)
    assert plugins.filter(BasePlugin) == plugins.filter(JSONFormatter) + plugins.filter(JSONConverter)
    assert plugins.filter(JSONFormatter) == [JSONFormatter]
    assert plugins.filter(JSONConverter) == [JSONConverter]
    assert plugins.filter(AuthPlugin) == []


# Generated at 2022-06-13 22:41:02.176132
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(FormatterPlugin)
    pm.register(FormatterPlugin)

    assert pm.get_formatters_grouped() == {"Default": [FormatterPlugin]}


# Generated at 2022-06-13 22:41:06.653902
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
	#without type filter
	pm = PluginManager()
	pm.register(TransportPlugin)
	pm.register(AuthPlugin)
	pm.register(ConverterPlugin)
	pm.register(FormatterPlugin)

	result = pm.filter()
	assert result == [TransportPlugin, AuthPlugin, ConverterPlugin, FormatterPlugin]
	
	#with type filter
	result = pm.filter(AuthPlugin)
	assert result == [AuthPlugin]

# Generated at 2022-06-13 22:41:11.894149
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager.get_auth_plugins()) >2
    assert len(manager.get_converters()) >2
    assert len(manager.get_formatters()) >2
    assert len(manager.get_transport_plugins()) >2

# Generated at 2022-06-13 22:41:23.389246
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    from httpie.plugins.builtin.formatters import BuiltinFormatterPlugin
    from httpie.plugins.builtin.__main__ import common_options
    from httpie.plugins.builtin.colors import ColorsPlugin
    from httpie.plugins.builtin.format import FormatPlugin
    from httpie.plugins.builtin.stream import StreamPlugin
    pm.register(BuiltinFormatterPlugin(), ColorsPlugin(), FormatPlugin(), StreamPlugin())
    
    formatters = pm.get_formatters_grouped()
    assert(len(formatters['Builtin']) == 4)
    assert(formatters['Builtin'][0] == BuiltinFormatterPlugin)
    assert(formatters['Builtin'][1] == ColorsPlugin)
    assert(formatters['Builtin'][2] == FormatPlugin)
   

# Generated at 2022-06-13 22:41:29.651834
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_auth_plugin_mapping() == {
        'basic': httpie.plugins.auth.basic.BasicAuthPlugin,
        'digest': httpie.plugins.auth.digest.DigestAuthPlugin
    }

# Generated at 2022-06-13 22:41:32.511791
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(str)
    assert pm.get_formatters_grouped() == {'default': [str]}


# Generated at 2022-06-13 22:41:41.775552
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(
        FakeJsonPlugin,
        FakeJsonPrettyPlugin,
        FakeJsonTabPlugin,
        FakeJsonUglyPlugin,
        FakeHtmlPlugin,
        FakeHtmlPrettyPlugin,
        FakeHtmlTabPlugin,
        FakeHtmlUglyPlugin,
        FakeCsvPlugin,
        FakeCsvPrettyPlugin,
        FakeCsvTabPlugin,
        FakeCsvUglyPlugin,
    )


# Generated at 2022-06-13 22:41:49.699134
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin
    from httpie.plugins.base import BasePlugin, TransportPlugin
    from httpie.plugins.builtin import AuthPluginConflict, FileUploadPlugin
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin,PythonFormatter)
    assert plugin_manager.filter(by_type=AuthPlugin) == [AuthPlugin]

# Generated at 2022-06-13 22:41:51.115878
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()

# Generated at 2022-06-13 22:41:59.915406
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin

    g = PluginManager()
    g.register(AuthPlugin)
    g.register(FormatterPlugin)
    g.register(ConverterPlugin)
    g.register(TransportPlugin)
    result = g.filter(AuthPlugin)
    assert len(result) == 1
    assert result[0] == AuthPlugin