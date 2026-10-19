

# Generated at 2022-06-13 22:33:18.419077
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0

# Generated at 2022-06-13 22:33:27.511214
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Create an instance of PluginManager
    plugin_manager = PluginManager()
    # Test if the instance is created correctly
    assert plugin_manager == plugin_manager.filter()
    # Test if the method "load_installed_plugins" can work correctly
    plugin_manager.load_installed_plugins()
    assert isinstance(plugin_manager.filter(), list)
    assert not isinstance(plugin_manager.get_formatters(), list)
    assert not isinstance(plugin_manager.get_converters(), list)
    assert not isinstance(plugin_manager.get_auth_plugins(), list)
    assert not isinstance(plugin_manager.get_transport_plugins(), list)


# Generated at 2022-06-13 22:33:39.537296
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    my_PluginManager = PluginManager()
    my_PluginManager.register(AuthPlugin)
    my_PluginManager.register(AuthPlugin)
    my_PluginManager.register(AuthPlugin)
    my_PluginManager.register(AuthPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    my_PluginManager.register(TransportPlugin)
    assert my_PluginManager.get_formatters_grouped() == {}

# Generated at 2022-06-13 22:33:42.357968
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager[0].package_name == 'httpie'

# Generated at 2022-06-13 22:33:44.819251
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print(PluginManager().load_installed_plugins())

test_PluginManager_load_installed_plugins()


# Generated at 2022-06-13 22:33:54.504207
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin

    from plugins.httpie_sublime_theme import SublimeTheme
    from plugins.httpie_colors import Colors
    from plugins.httpie_fireworks import Fireworks
    from plugins.httpie_statusbar import StatusBarPlugin

    manager = PluginManager()
    manager.register(SublimeTheme, Colors, Fireworks, StatusBarPlugin)

    m = manager.get_formatters_grouped()

    assert issubclass(m['group'][0], FormatterPlugin)

# Generated at 2022-06-13 22:34:03.761841
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    pkg_names = [p.package_name for p in plugin_manager]
    assert 'httpie-cookiejar' in pkg_names
    assert 'httpie-markdown' in pkg_names
    assert 'httpie-jmespath' in pkg_names
    assert 'httpie-aws' in pkg_names
    assert 'httpie-unixsocket' in pkg_names
    assert 'httpie-edgegrid' in pkg_names
    assert 'httpie-jwt-auth' in pkg_names


# Generated at 2022-06-13 22:34:05.811457
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    assert pm.filter(AuthPlugin) == []

# Generated at 2022-06-13 22:34:18.422872
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins import AuthPlugin
    from httpie.plugins.builtin import AuthPluginV1
    from httpie.plugins.builtin import BasicAuthPluginV1
    from httpie.plugins.builtin import DigestAuthPluginV1
    from httpie.plugins.builtin import HawkAuthPluginV1
    # test plugins
    class TestAuthPlugin1(AuthPlugin):
        auth_type = 'test'
        auth_type_aliases = ['t']
    class TestAuthPlugin2(AuthPlugin):
        auth_type = 'test2'
        auth_type_aliases = ['t2']
    class TestAuthPlugin3(AuthPlugin):
        auth_type = 'test3'
        auth_type_aliases = ['t3']

    auth_plugins = PluginManager()

# Generated at 2022-06-13 22:34:21.669770
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pluginManager = PluginManager()
    plugins = [AuthPlugin, ConvertPlugin]
    pluginManager.register(*plugins)

    assert pluginManager.filter(AuthPlugin) == plugins


# Generated at 2022-06-13 22:34:27.498453
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()

    plugin_manager.load_installed_plugins()

    assert isinstance(plugin_manager, PluginManager)
    assert len(plugin_manager) == 4


# Generated at 2022-06-13 22:34:35.037917
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    formatter1 = BasePlugin()
    formatter1.group_name = 'group1'
    formatter2 = BasePlugin()
    formatter2.group_name = 'group2'
    plugins.register(formatter1, formatter2)
    assert plugins.get_formatters_grouped()['group1'] == [formatter1]

# Generated at 2022-06-13 22:34:47.494420
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie import ExitStatus
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPiePlugin, HTTPieJSONPlugin
    from httpie.plugins.builtin import HTTPiePrettyJSONPlugin, HTTPieHTMLPlugin

    plugin_manager = PluginManager()
    plugin_manager.register(HTTPBasicAuth)
    plugin_manager.register(HTTPiePlugin)
    plugin_manager.register(HTTPieJSONPlugin)
    plugin_manager.register(HTTPiePrettyJSONPlugin)
    plugin_manager.register(HTTPieHTMLPlugin)

    assert plugin_manager.get_auth_plugins() == [HTTPBasicAuth]
    assert plugin_manager.get_formatters() == [HTTPiePlugin, HTTPieJSONPlugin, HTTPiePrettyJSONPlugin, HTTPieHTMLPlugin]
    assert plugin_manager.get_formatters_

# Generated at 2022-06-13 22:34:54.297580
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    global test, pass_num, fail_num
    pm = PluginManager()
    pm.load_installed_plugins()
#     print(pm)
    if(len(pm) > 0):
        test=test+1
        pass_num=pass_num+1
    else:
        test=test+1
        fail_num=fail_num+1


# Generated at 2022-06-13 22:35:06.569855
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager1 = PluginManager()
    pluginManager1.load_installed_plugins()
    assert len(pluginManager1) == 3
    assert pluginManager1.get_auth_plugin('jwt') is not None
    assert pluginManager1.get_formatters_grouped()['netrc'] is not None
    assert pluginManager1.get_converters() is not None

    pluginManager2 = PluginManager()
    pluginManager2.register(TestAuthPlugin, TestFormatterPlugin, TestConverterPlugin, TestTransportPlugin)
    pluginManager2.load_installed_plugins()
    assert len(pluginManager2) == 7
    assert pluginManager2.get_auth_plugin('test') is not None
    assert pluginManager2.get_formatters_grouped()['test'] is not None
    assert pluginManager2.get_converters

# Generated at 2022-06-13 22:35:09.969877
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(test_plugin)
    assert plugins.get_auth_plugin_mapping() == {'test_plugin': test_plugin}


# Generated at 2022-06-13 22:35:19.977397
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    x = manager.get_formatters_grouped()
    assert x == {
        'Debug': [httpie.plugins.formatter.debug.DebugFormatter],
        'Human': [httpie.plugins.formatter.colors.ColorsFormatter, httpie.plugins.formatter.format.FormattingFormatter],
        'JSON': [httpie.plugins.formatter.json.JSONFormatter],
        'Machine': [httpie.plugins.formatter.prettyjson.PrettyJSONFormatter],
        'Syntax': [httpie.plugins.formatter.syntax.SyntaxHighlightFormatter]
    }



# Generated at 2022-06-13 22:35:30.598942
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # To run this unit test, you should comment out the below code of class PluginManager:
    # def load_installed_plugins(self):
    #     for entry_point_name in ENTRY_POINT_NAMES:
    #         for entry_point in iter_entry_points(entry_point_name):
    #             plugin = entry_point.load()
    #             plugin.package_name = entry_point.dist.key
    #             self.register(entry_point.load())

    # Unit test:
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0

# Generated at 2022-06-13 22:35:33.141412
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    f1 = FormatterPlugin("f1")
    f2 = FormatterPlugin("f2")
    f3 = FormatterPlugin("f3", "html")

    pm = PluginManager()
    pm.register(f1, f2, f3)
    formatters = pm.get_formatters_grouped()
    assert len(formatters) == 2
    assert len(formatters["text"]) == 2
    assert len(formatters["html"]) == 1

# Generated at 2022-06-13 22:35:38.210332
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    plugins.register(TestingAuthPlugin)
    assert plugins.get_auth_plugin_mapping() == {
        'testing': TestingAuthPlugin
    }
    assert plugins.get_auth_plugin('testing') == TestingAuthPlugin


# Generated at 2022-06-13 22:35:51.987047
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    plugins_manager = PluginManager()
    plugins_manager.load_installed_plugins()

    formatters_grouped = plugins_manager.get_formatters_grouped()
    assert formatters_grouped['json'] == [httpie.plugins.formatter.json.JSONFormatter]
    assert formatters_grouped['xml'] == [httpie.plugins.formatter.pretty_xml.PrettyXMLFormatter]

    auth_plugins_mapping = plugins_manager.get_auth_plugin_mapping()
    assert auth_plugins_mapping['basic'] == httpie.plugins.auth.basic_auth.BasicAuthPlugin
    assert auth_plugins_mapping['digest'] == httpie.plugins.auth.digest_auth.DigestAuthPlugin

    converters = plugins_manager.get_converters()
    assert converters == []

# Generated at 2022-06-13 22:36:04.870336
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin

    p1 = type('p1', (BasePlugin,), {})
    p2 = type('p2', (BasePlugin, AuthPlugin), {})
    p3 = type('p3', (BasePlugin, AuthPlugin, ConverterPlugin), {})
    p4 = type('p4', (BasePlugin, FormatterPlugin), {})
    p5 = type('p5', (BasePlugin, FormatterPlugin, AuthPlugin), {})
    p6 = type('p6', (BasePlugin, AuthPlugin, ConverterPlugin), {})

    plugin_manager = PluginManager()
    plugin_manager.register(p1, p2, p3, p4, p5, p6)


# Generated at 2022-06-13 22:36:10.666063
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0
    assert len(plugins.get_auth_plugins()) > 0
    assert len(plugins.get_formatters()) > 0
    assert len(plugins.get_converters()) > 0
    assert len(plugins.get_transport_plugins()) > 0


# Generated at 2022-06-13 22:36:18.922348
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Formatters are already being sorted in the right order, so I create a PluginManager
    # with 2 formatters, sorted by group_name, and test it
    f1 = FormatterPlugin(group_name='json')
    f2 = FormatterPlugin(group_name='html')
    plugin_manager = PluginManager()
    plugin_manager.register(f1, f2)
    assert plugin_manager.get_formatters_grouped() == {'json': [f1], 'html': [f2]}

# Generated at 2022-06-13 22:36:22.543245
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginManager.register(GoogleAuthPlugin)  # class
    PluginManager.get_auth_plugin_mapping()
    assert PluginManager.get_auth_plugin_mapping() == {'google': GoogleAuthPlugin}

# Google plugin unit test

# Generated at 2022-06-13 22:36:32.914656
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.plugins
    httpie.plugins.__all__ = ['A', 'B', 'C', 'D', 'E', 'F']

    try:
        plugin_manager = PluginManager()
        plugin_manager.register(A, B, C, D, E, F)
        assert plugin_manager.get_formatters_grouped() ==  {'Group 1' : [A, B], 'Group 2' : [D, E], 'Group 3' : [F]}
    finally:
        if 'A' in httpie.plugins.__all__:
            del httpie.plugins.__all__[httpie.plugins.__all__.index('A')]

# Generated at 2022-06-13 22:36:35.646857
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()

    assert len(manager.get_auth_plugins()) > 0
    assert len(manager.get_formatters()) > 0
    assert len(manager.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:36:46.351941
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.manager import PluginManager
    from httpie.plugins.builtin import BuiltinFormatters
    from httpie.plugins.formatter.colors import ColorsFormatterPlugin
    from httpie.plugins.formatter.json import JSONFormatterPlugin
    from httpie.plugins.formatter.pretty import PrettyFormatterPlugin
    from httpie.plugins.formatter.stream import StreamFormatterPlugin
    from httpie.plugins.formatter.utils import get_parser_class

    class Formatter1(BuiltinFormatters):
        name = 'formatter1'
        group_name = 'group1'

    class Formatter2(BuiltinFormatters):
        name = 'formatter2'
        group_name = 'group2'

    class Formatter3(BuiltinFormatters):
        name = 'formatter3'
        group

# Generated at 2022-06-13 22:36:49.085519
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    mapping = plugins.get_auth_plugin_mapping()
    assert isinstance(mapping, dict)



# Generated at 2022-06-13 22:36:50.248794
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    assert plugin_manager.filter(BasePlugin) == []

# Generated at 2022-06-13 22:36:59.650189
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    list1 = pm.get_formatters()
    list2 = pm.get_formatters_grouped()
    list3 = pm.get_converters()
    list4 = pm.get_auth_plugins()
    list5 = pm.get_auth_plugin_mapping()
    list6 = pm.get_transport_plugins()

# Generated at 2022-06-13 22:37:10.097885
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Plugin1(FormatterPlugin):
        group_name = 'group_1'
        name = 'plugin1'
    class Plugin2(FormatterPlugin):
        group_name = 'group_1'
        name = 'plugin2'
    class Plugin3(FormatterPlugin):
        group_name = 'group_2'
        name = 'plugin3'
    class Plugin4(FormatterPlugin):
        group_name = 'group_3'
        name = 'plugin4'

    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3, Plugin4)

    expected = {
        'group_1': [Plugin1, Plugin2],
        'group_2': [Plugin3],
        'group_3': [Plugin4]
    }

    assert expected == plugin_manager.get_

# Generated at 2022-06-13 22:37:14.372669
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    assert plugins.get_auth_plugin_mapping() == {}
    plugins.register(MockAuthPlugin)
    assert plugins.get_auth_plugin_mapping() == {'mock': MockAuthPlugin}

# Generated at 2022-06-13 22:37:21.124182
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    print("\nTesting method get_formatters_grouped of class PluginManager:")
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(ConverterPlugin)
    print(plugin_manager)
    print(plugin_manager.get_formatters_grouped())



# Generated at 2022-06-13 22:37:23.571580
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) >= 4


# Generated at 2022-06-13 22:37:27.540855
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    print('before:', pm)
    assert str(pm) == '<PluginManager: []>'

    pm.load_installed_plugins()
    print('after:', pm)
    assert str(pm) != '<PluginManager: []>'


plugins = PluginManager()

# Generated at 2022-06-13 22:37:36.713614
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(FormatterPlugin)
    formatters = [FormatterPlugin()]
    formatters.group_name = 'Test group_name'
    formatters.plugin_name = 'Test plugin_name'
    formatters.group_name1 = 'Test group_name1'
    formatters.plugin_name1 = 'Test plugin_name1'
    manager.register(formatters)
    assert manager.get_formatters_grouped() == {'group_name': [FormatterPlugin, formatters], 'group_name1': [FormatterPlugin, formatters]}

# Generated at 2022-06-13 22:37:39.194785
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0


# Generated at 2022-06-13 22:37:45.691381
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Setup - create an instance of PluginManager and disable default printing
    # of warnings by warnings module
    plugin_manager = PluginManager()
    warnings.filterwarnings('ignore')
    # Test - print the contents of the instance
    print("Printing contents of the instance of class PluginManager before the "
          "execution of method load_installed_plugins:")
    print(plugin_manager)
    # Expected output - '<PluginManager: []>'
    # Test - execute method load_installed_plugins
    plugin_manager.load_installed_plugins()
    # Test - print the contents of the instance
    print("Printing contents of the instance of class PluginManager after the "
          "execution of method load_installed_plugins:")
    print(plugin_manager)
    # Expected output - the contents should not be empty (as 'httpie'

# Generated at 2022-06-13 22:37:54.223184
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    AuthPlugin = Type[BasePlugin]
    ConverterPlugin = Type[BasePlugin]
    FormatterPlugin = Type[BasePlugin]
    TransportPlugin = Type[BasePlugin]
    class auth(AuthPlugin): pass
    class converter(ConverterPlugin): pass
    class formatter(FormatterPlugin): pass
    class transport(TransportPlugin): pass
    pm.register(auth, formatter, converter, transport)
    assert pm.filter(AuthPlugin) == [auth]
    assert pm.filter(ConverterPlugin) == [converter]
    assert pm.filter(FormatterPlugin) == [formatter]
    assert pm.filter(TransportPlugin) == [transport]


# Generated at 2022-06-13 22:38:11.059366
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin.formatter.colors import AutoColorsFormatter

    plugin_manager = PluginManager()
    plugin_manager.register(AutoColorsFormatter)

# Generated at 2022-06-13 22:38:12.483032
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0
    for plugin in pm:
        assert issubclass(plugin, BasePlugin)

# Generated at 2022-06-13 22:38:18.272988
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    mocked_formatters = [
        Mock(spec=FormatterPlugin, group_name='Group1'),
        Mock(spec=FormatterPlugin, group_name='Group1'),
        Mock(spec=FormatterPlugin, group_name='Group2')
    ]
    mocked_formatter_manager = PluginManager()
    mocked_formatter_manager.get_formatters = Mock(return_value=mocked_formatters)

    result = mocked_formatter_manager.get_formatters_grouped()

    assert len(result) == 2
    assert len(result['Group1']) == 2
    assert len(result['Group2']) == 1

# Generated at 2022-06-13 22:38:19.830690
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    print(pm.get_formatters_grouped())

# Generated at 2022-06-13 22:38:24.481008
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # auth_type: plugin
    plugin_manage_get_auth_plugin_mapping = {
        plugin.auth_type: plugin for plugin in self.get_auth_plugins()
    }
    assert len(plugin_manage_get_auth_plugin_mapping) == 0



# Generated at 2022-06-13 22:38:26.124661
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0


# Generated at 2022-06-13 22:38:30.882263
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    assert not pm

    pm.load_installed_plugins()
    assert pm


plugins = PluginManager()

plugins.load_installed_plugins()

# Generated at 2022-06-13 22:38:38.442158
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import FormatterPlugin, ConverterPlugin
    from httpie.plugins import AuthPlugin, TransportPlugin
    class AuthFormatterPlugin(FormatterPlugin, AuthPlugin): pass
    class AuthConverterPlugin(ConverterPlugin, AuthPlugin): pass
    class TransportFormatterPlugin(FormatterPlugin, TransportPlugin): pass
    class TransportConverterPlugin(ConverterPlugin, TransportPlugin): pass
    class FormatterTransportPlugin(TransportPlugin, FormatterPlugin): pass
    class ConverterTransportPlugin(TransportPlugin, ConverterPlugin): pass
    class AuthTransportPlugin(TransportPlugin, AuthPlugin): pass
    plugins_list = [AuthFormatterPlugin, AuthConverterPlugin, TransportFormatterPlugin, TransportConverterPlugin, FormatterTransportPlugin, ConverterTransportPlugin, AuthTransportPlugin]
    plugins = PluginManager

# Generated at 2022-06-13 22:38:47.712698
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import collections
    import types
    import unittest
    class TestPluginManager (PluginManager):
        def __init__(self):
            super().__init__()
            self.register(*self.get_formatters())
    test_PluginManager = TestPluginManager()

    # Test cases
    test_PluginManager.register(TestFormatterPlugin1(), TestFormatterPlugin2())
    #print(test_PluginManager)
    test_group = test_PluginManager.get_formatters_grouped()
    #print(test_group)
    assert isinstance(test_group, collections.Mapping), 'should be a mapping object'
    assert isinstance(test_group['TestGroup'], (collections.Sequence, types.GeneratorType)), 'should be a sequence object'
    assert len(test_group['TestGroup']) == 2

# Generated at 2022-06-13 22:38:50.067715
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins_manager = PluginManager()
    assert plugins_manager.load_installed_plugins() == None



# Generated at 2022-06-13 22:39:11.937964
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)

    expected_output = {
        'http': [AuthPlugin],
        'general': [ConverterPlugin],
        'assist': [FormatterPlugin],
        'adapter': [TransportPlugin]
    }
    assert pm.get_formatters_grouped() == expected_output

# Generated at 2022-06-13 22:39:17.772054
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0
    for plugin in plugins:
        assert issubclass(plugin, BasePlugin)
        assert plugin.package_name

    # Test plugins are sorted by package name.
    assert list(sorted(plugins, key=attrgetter('package_name'))) == plugins


if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:39:22.670414
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.append(FormatterPlugin)
    plugins.append(FormatterPlugin)
    assert len(plugins.get_formatters_grouped()) == 1

# Generated at 2022-06-13 22:39:29.539555
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins.register(type('AuthPlugin', (), {'type': 'auth'}))
    plugins.register(type('TransportPlugin', (), {'type': 'auth'}))
    plugins.register(type('TransportPlugin2', (), {'type': 'auth'}))
    plugins.register(type('FormatterPlugin', (), {'type': 'format'}))

    assert len(plugins.filter(TransportPlugin)) == 2
    assert len(plugins.filter(AuthPlugin)) == 1
    assert len(plugins.filter(FormatterPlugin)) == 1

# Generated at 2022-06-13 22:39:39.623543
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Set up
    from httpie.plugins.manager import PluginManager
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.builtin import HTMLFormatterPlugin
    from httpie.plugins.builtin import PrettyFormatterPlugin
    from httpie.plugins.builtin import StreamFormatterPlugin

    # Arrange
    plugins = PluginManager()
    plugins.register(JSONFormatterPlugin)
    plugins.register(HTMLFormatterPlugin)
    plugins.register(PrettyFormatterPlugin)
    plugins.register(StreamFormatterPlugin)

    # Act
    result = plugins.get_formatters_grouped()

    # Assert
    assert result == {"json": [JSONFormatterPlugin, PrettyFormatterPlugin], 
                      "html": [HTMLFormatterPlugin], 
                      "text": [StreamFormatterPlugin]}

# Generated at 2022-06-13 22:39:50.457777
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager)
    # print(manager.get_auth_plugin_mapping())
    # print(manager.get_auth_plugin('jwt'))
    print(manager.get_formatters_grouped())
    print(manager.get_converters())
    print(manager.get_transport_plugins())

if __name__ == "__main__":
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:39:59.562062
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # 1
    plugins = PluginManager()
    plugin1 = type('Plugin1', (list,), {})
    plugin2 = type('Plugin2', (list,), {})
    plugin3 = type('Plugin3', (list,), {})
    plugin4 = type('Plugin4', (list,), {})
    plugin1.auth_type = 'basic'
    plugin2.auth_type = 'basic'
    plugin3.auth_type = 'bearer'
    plugin4.auth_type = 'bearer'
    plugins.register(plugin1)
    plugins.register(plugin2)
    plugins.register(plugin3)
    plugins.register(plugin4)
    auth_plugin_dict = plugins.get_auth_plugin_mapping()
    assert auth_plugin_dict['basic'] == list
    assert auth_plugin_

# Generated at 2022-06-13 22:40:07.010741
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin
    from httpie.plugins.base import BasePlugin

    class Plugin1(FormatterPlugin, BasePlugin):
        group_name = 'group1'

    class Plugin2(AuthPlugin, BasePlugin):
        group_name = 'group2'

    class Plugin3(ConverterPlugin, BasePlugin):
        group_name = 'group3'

    class Plugin4(TransportPlugin, BasePlugin):
        pass

    class Plugin5(FormatterPlugin, BasePlugin):
        group_name = 'group1'

    plugins = [Plugin1, Plugin2, Plugin3, Plugin4, Plugin5]

    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)


# Generated at 2022-06-13 22:40:14.318629
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginsManager = PluginManager()
    assert PluginsManager.get_auth_plugin_mapping() == {}

    from httpie.plugins.auth.basic import BasicAuthPlugin
    from httpie.plugins.auth.digest import DigestAuthPlugin

    PluginsManager.register(BasicAuthPlugin, DigestAuthPlugin)
    assert PluginsManager.get_auth_plugin_mapping() == {
        "basic": BasicAuthPlugin,
        "digest": DigestAuthPlugin,
    }


# Generated at 2022-06-13 22:40:21.261045
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()

# Generated at 2022-06-13 22:41:04.715022
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # GIVEN
    import httpie.plugins.formatter.json as json_formatter
    import httpie.plugins.formatter.pretty as pretty_formatter
    plugin_manager = PluginManager()
    plugin_manager.register(json_formatter.Formatter, pretty_formatter.Formatter)
    # WHEN
    result = plugin_manager.get_formatters_grouped()
    # THEN
    expected = {"JSON": [json_formatter.Formatter], "Pretty": [pretty_formatter.Formatter]}
    assert result == expected

# Generated at 2022-06-13 22:41:08.777846
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print("PluginManager.load_installed_plugins() unit testing...")
    plugin = PluginManager()
    assert plugin == []
    plugin.load_installed_plugins()
    assert len(plugin) > 0

# Generated at 2022-06-13 22:41:16.749349
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    m = PluginManager()
    m.register(type('TestPlugin', (BasePlugin,), {
        'name': 'TestPlugin',
        'entry_point_name': 'httpie.plugins.auth.v1'}))

    m.load_installed_plugins()

    assert len(m) == 1

    found = None
    for plugin in m:
        if plugin.name == 'TestPlugin':
            found = plugin
    assert found is not None

# Generated at 2022-06-13 22:41:19.930720
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert 'httpie_httpie_jwt_auth' in str(manager)


# Generated at 2022-06-13 22:41:21.887268
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager != None
    

# Generated at 2022-06-13 22:41:27.513743
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    for entry_point_name in ENTRY_POINT_NAMES:
        for entry_point in iter_entry_points(entry_point_name):
            plugin = entry_point.load()
            assert plugin in pm

# Generated at 2022-06-13 22:41:29.503482
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:41:33.102141
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(FormatterPluginMock)
    assert len(pm.get_formatters_grouped()) == 1
    assert pm.get_formatters_grouped().get('formatter') is not None


# Generated at 2022-06-13 22:41:38.202153
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(HtmlFormatter, JsonFormatter,CsvFormatter)
    assert plugin_manager.get_formatters_grouped() == {'Html': [HtmlFormatter], 'Json': [JsonFormatter], 'Csv': [CsvFormatter]}


plugins = PluginManager()
plugins.load_installed_plugins()

# Generated at 2022-06-13 22:41:43.918827
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = [
        FormatterPlugin,
        FormatterPlugin
    ]

    plugin_manager = PluginManager()
    plugin_manager.register(*formatters)

    grouped_formatters = plugin_manager.get_formatters_grouped()
    assert len(grouped_formatters) == 1

    assert len(grouped_formatters['Formatters']) == 2

# Generated at 2022-06-13 22:43:11.627502
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    ep1 = Mock()
    ep1.load.return_value = plugin1 = Mock()
    ep2 = Mock()
    ep2.load.return_value = plugin2 = Mock()
    ep3 = Mock()
    ep3.load.return_value = plugin3 = Mock()

    plugin1.group_name = 0
    plugin2.group_name = 0
    plugin3.group_name = 1

    iter_entry_points_func = Mock()
    iter_entry_points_func.return_value = [ep1, ep2, ep3]
    plugin_manager = PluginManager()