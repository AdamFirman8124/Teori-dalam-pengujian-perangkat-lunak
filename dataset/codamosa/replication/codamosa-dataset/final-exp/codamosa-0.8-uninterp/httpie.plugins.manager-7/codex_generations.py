

# Generated at 2022-06-13 22:33:21.084996
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.auth import BasicAuthPlugin
    from httpie.plugins.auth.kerberos_auth import KerberosAuthPlugin

    pm = PluginManager()
    pm.register(BasicAuthPlugin, KerberosAuthPlugin)
    assert pm.get_auth_plugin_mapping() == {
        'basic': BasicAuthPlugin,
        'kerberos': KerberosAuthPlugin
    }

# Generated at 2022-06-13 22:33:29.603559
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import HTTPieColorsFormatter
    from httpie.plugins.builtin import JSONFormatter
    from httpie.plugins.builtin import RawJSONFormatter
    from httpie.plugins.builtin import JSONLinesFormatter
    from httpie.plugins.builtin import HtmlFormatter
    plugin_manager = PluginManager()
    plugin_manager.register(HTTPieColorsFormatter,
                            JSONFormatter,
                            RawJSONFormatter,
                            JSONLinesFormatter,
                            HtmlFormatter)
    expected = {
        'Group A': [HTTPieColorsFormatter],
        'Group B': [JSONFormatter, RawJSONFormatter, JSONLinesFormatter],
        'Group C': [HtmlFormatter]
    }
    assert plugin_manager.get_formatters

# Generated at 2022-06-13 22:33:33.401917
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) > 0
    assert '<PluginManager: []>' != repr(manager)


# Generated at 2022-06-13 22:33:38.362792
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    print(manager)
    manager.load_installed_plugins()
    print(manager)
    print('formatters: ')
    print(manager.get_formatters_grouped())

if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:33:46.313394
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    @author: Wang Ziyue
    @date: 2020/3/30
    """
    # arrange
    class MockFormatterPlugin(FormatterPlugin):
        group_name = 'Test1'

    class MockFormatterPlugin1(FormatterPlugin):
        group_name = 'Test1'

    class MockFormatterPlugin2(FormatterPlugin):
        group_name = 'Test2'

    mockFormatterPlugin, mockFormatterPlugin1, mockFormatterPlugin2 = MockFormatterPlugin(), MockFormatterPlugin1(), MockFormatterPlugin2()
    pluginManager = PluginManager()
    pluginManager.register(mockFormatterPlugin, mockFormatterPlugin1, mockFormatterPlugin2)

    # act
    result = pluginManager.get_formatters_grouped()

    # assert

# Generated at 2022-06-13 22:33:53.286946
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins_manager = PluginManager()
    plugins_manager.register(TestPlugin1, TestPlugin2, TestPlugin3)

    assert plugins_manager.get_formatters_grouped() == {
        'group1': [TestPlugin1, TestPlugin2],
        'group2': [TestPlugin3]
    }



# Generated at 2022-06-13 22:34:00.600050
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.auth import BasicAuth, DigestAuth
    from httpie.plugins.builtin import HTTPBasicAuth

    plugin_manager = PluginManager()
    plugin_manager.register(BasicAuth, DigestAuth, HTTPBasicAuth)
    mapping = plugin_manager.get_auth_plugin_mapping()
    assert mapping['basic'] == BasicAuth
    assert mapping['digest'] == DigestAuth
    assert mapping['http-auth'] == HTTPBasicAuth



# Generated at 2022-06-13 22:34:06.452948
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.auth import AuthPlugin
    class MyAuthPlugin(AuthPlugin):
        auth_type = 'my'
    plugin_manager = PluginManager()
    plugin_manager.register(MyAuthPlugin)
    assert plugin_manager.get_auth_plugin_mapping() == {
        'my': MyAuthPlugin
    }

# Generated at 2022-06-13 22:34:07.217076
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PluginManager().filter()

# Generated at 2022-06-13 22:34:14.676302
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.load_installed_plugins()
    formatters = manager.get_formatters_grouped()
    assert type(formatters) == dict
    assert len(formatters) > 0
    assert len(formatters['generic']) > 0
    assert len(formatters['json']) > 0
    assert 'html' in formatters.keys()
    assert 'csv' not in formatters.keys()


# Generated at 2022-06-13 22:34:19.207561
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin = plugin_manager.load_installed_plugins()
    assert len(plugin)==4



# Generated at 2022-06-13 22:34:28.061290
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A:
        pass

    class B:
        pass

    class C(A):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(A, B, C)
    plugin_filter_a = plugin_manager.filter(A)
    plugin_filter_b = plugin_manager.filter(B)
    assert len(plugin_filter_a) ==  2
    assert len(plugin_filter_b) ==  1
    assert plugin_filter_a[0] == A
    assert plugin_filter_a[1] == C
    assert plugin_filter_b[0] == B


# Generated at 2022-06-13 22:34:34.059242
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    assert manager.filter() == []
    assert manager.filter(by_type=str) == []
    manager.register(str)
    assert manager.filter(by_type=str) == [str]



# Generated at 2022-06-13 22:34:44.478575
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    FormatterPlugin1 = type('FormatterPlugin1', (FormatterPlugin,), {})
    FormatterPlugin2 = type('FormatterPlugin2', (FormatterPlugin,), {})
    FormatterPlugin1.group_name = 'group1'
    FormatterPlugin2.group_name = 'group2'
    manager.register(FormatterPlugin1, FormatterPlugin2)
    assert manager.get_formatters_grouped() == {
        'group1': [FormatterPlugin1],
        'group2': [FormatterPlugin2],
    }

# Generated at 2022-06-13 22:34:49.174902
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPluginWithGroupA)
    plugin_manager.register(FormatterPluginWithGroupB)
    plugin_manager.register(FormatterPluginWithoutGroup)
    assert plugin_manager.get_formatters_grouped() == {
        'Group A': [FormatterPluginWithGroupA],
        'Group B': [FormatterPluginWithGroupB],
        None: [FormatterPluginWithoutGroup],
    }


# Generated at 2022-06-13 22:34:59.382732
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert plugin_manager.get_formatters_grouped() == {}
    plugin_manager.register(CustomJsonFormatter, CustomJsonFormatter)
    assert (plugin_manager.get_formatters_grouped() == {
        'json': [CustomJsonFormatter, CustomJsonFormatter]
    })
    plugin_manager.append(CustomJsonFormatter)
    assert (plugin_manager.get_formatters_grouped() == {
        'json': [CustomJsonFormatter, CustomJsonFormatter, CustomJsonFormatter]
    })

plugin_manager = PluginManager()

# Generated at 2022-06-13 22:35:09.532659
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import formatter

    class FormatGroup0(FormatterPlugin):
        group_name = 'group0'

    class FormatGroup1(FormatterPlugin):
        group_name = 'group1'

    class FormatGroup1a(FormatterPlugin):
        group_name = 'group1'

    class FormatGroup2(FormatterPlugin):
        group_name = 'group2'

    plugins_formatters = [FormatGroup0, FormatGroup1, FormatGroup1a, FormatGroup2]
    manager = PluginManager()
    manager.register(*plugins_formatters)

# Generated at 2022-06-13 22:35:15.966785
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.plugins as all_plugins
    pm = PluginManager()
    pm.register(all_plugins.FormattedTextFormatter, all_plugins.HTMLFormatter)
    assert pm.get_formatters_grouped() == {'group_name_1': [all_plugins.FormattedTextFormatter], 'group_name_2': [all_plugins.HTMLFormatter]}

# Generated at 2022-06-13 22:35:23.432679
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import core
    # test environment:
    # current available plugins list is empty
    plugin_manager = PluginManager()
    assert len(plugin_manager) == 0
    # test under condition:
    # load all installed plugins
    plugin_manager.load_installed_plugins()
    length_of_plugin_manager = len(plugin_manager)
    assert length_of_plugin_manager > 0
    # test under condition:
    # available plugins list are not empty
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0
    # test environment:
    # current available plugins list is not empty
   

# Generated at 2022-06-13 22:35:27.968173
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    p1 = PluginManager([1, 2, 3, 4, 5])
    assert p1.filter(by_type=int) == [1, 2, 3, 4, 5]
    assert p1.filter(by_type=str) == []

# Generated at 2022-06-13 22:35:34.798147
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    _plugin_manager = PluginManager()
    _plugin_manager.load_installed_plugins()
    assert len(ENTRY_POINT_NAMES) == len(_plugin_manager)


# Generated at 2022-06-13 22:35:37.165454
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert 1 == len(plugins)

# Generated at 2022-06-13 22:35:43.432369
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_pluginManager = PluginManager()
    test_pluginManager.register(TestFormatterPlugin)
    test_pluginManager.register(TestFormatterPlugin)

    assert test_pluginManager.get_formatters_grouped() == { 'test': [TestFormatterPlugin, TestFormatterPlugin] }


# Generated at 2022-06-13 22:35:45.469532
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    instances = PluginManager()
    instances.load_installed_plugins()

    assert instances is not None



# Generated at 2022-06-13 22:35:57.805204
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    plugins = PluginManager()
    plugins.register(
        JsonFormatterPlugin,
        SyntaxHighlightJsonFormatterPlugin,
        SyntaxHighlightXmlFormatterPlugin,
        XmlFormatterPlugin,
        HtmlFormatterPlugin,
        UrlFormatterPlugin)

    f_grouped = plugins.get_formatters_grouped()
    assert f_grouped == {
        'JSON': [JsonFormatterPlugin, SyntaxHighlightJsonFormatterPlugin],
        'XML': [XmlFormatterPlugin, SyntaxHighlightXmlFormatterPlugin],
        'HTML': [HtmlFormatterPlugin],
        'URL': [UrlFormatterPlugin],
    }

# Generated at 2022-06-13 22:36:00.835492
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.load_installed_plugins()
    plugins = manager.filter(AuthPlugin)
    assert len(plugins) > 0


# Generated at 2022-06-13 22:36:05.643563
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    formatters_grouped = plugin_manager.get_formatters_grouped()
    print(formatters_grouped)

if __name__ == '__main__':
    test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:36:14.245144
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.base import BasePlugin

    class TestPlugin(BasePlugin):
        pass

    class Formatter(FormatterPlugin):
        pass

    class Converter(ConverterPlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(Converter, Formatter, TestPlugin)

    assert list(plugin_manager.filter()) == [Converter, Formatter, TestPlugin]
    assert list(plugin_manager.filter(ConverterPlugin)) == [Converter]
    assert list(plugin_manager.filter(FormatterPlugin)) == [Formatter]
    assert list(plugin_manager.filter(TestPlugin)) == [TestPlugin]


# Generated at 2022-06-13 22:36:25.727886
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PluginManager.register(self, [
        argparse.Namespace(group_name="1"),
        argparse.Namespace(group_name="2"),
        argparse.Namespace(group_name="1"),
        argparse.Namespace(group_name="3"),
        argparse.Namespace(group_name="1")
        ])
    assert PluginManager.get_formatters_grouped() == {
        "1" : [argparse.Namespace(group_name="1"), 
               argparse.Namespace(group_name="1"), 
               argparse.Namespace(group_name="1")],
        "2" : [argparse.Namespace(group_name="2")],
        "3" : [argparse.Namespace(group_name="3")]
        }

# Generated at 2022-06-13 22:36:30.617780
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import TestAuthPlugin, TestFormatterPlugin
    plugins = PluginManager()
    plugins.register(TestAuthPlugin, TestFormatterPlugin)

    assert plugins.filter(AuthPlugin) == [TestAuthPlugin]
    assert plugins.filter(FormatterPlugin) == [TestFormatterPlugin]



# Generated at 2022-06-13 22:36:45.769853
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    class FooPlugin(object):
        pass

    class BarPlugin(FooPlugin):
        pass

    class BazPlugin(object):
        pass

    manager = PluginManager()
    manager.register(FooPlugin)
    manager.register(BazPlugin)
    manager.register(BarPlugin)

    assert manager.filter() == [FooPlugin, BazPlugin, BarPlugin]
    assert manager.filter(FooPlugin) == [FooPlugin, BarPlugin]
    assert manager.filter(BarPlugin) == [BarPlugin]

# Generated at 2022-06-13 22:36:52.381762
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    lst = [
        {
            'group_name': 'image',
            'name': 'json',
            'is_binary': True
        },
        {
            'group_name': 'image',
            'name': 'xml',
            'is_binary': True
        },
        {
            'group_name': 'image',
            'name': 'html',
            'is_binary': False
        },
        {
            'group_name': 'image',
            'name': 'test',
            'is_binary': True
        },
    ]

# Generated at 2022-06-13 22:36:57.515481
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(AuthPlugin1, AuthPlugin2)
    assert {
        'mock-auth-type': AuthPlugin2,
        'mock-auth-type2': AuthPlugin1,
    } == plugins.get_auth_plugin_mapping()



# Generated at 2022-06-13 22:37:03.999232
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from ..plugins.builtin import JSONFormatterPlugin

    plugin = PluginManager()
    plugin.register(JSONFormatterPlugin)
    formatters_grouped = plugin.get_formatters_grouped()
    assert formatters_grouped == {'group_name': [JSONFormatterPlugin]}

# Generated at 2022-06-13 22:37:10.032174
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from my_formatter import Colorized

    pm = PluginManager()
    pm.register(Colorized)
    groups = pm.get_formatters_grouped()
    assert groups['Other'] == [Colorized]

pm = PluginManager()
pm.load_installed_plugins()
#print(pm)
#print(pm.get_auth_plugin_mapping())

print(pm.get_formatters_grouped())

# Generated at 2022-06-13 22:37:13.788337
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print('This is a test for method load_installed_plugins of class PluginManager')
    p = PluginManager()
    p.load_installed_plugins()
    assert p


# Generated at 2022-06-13 22:37:25.593897
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.register(AuthPlugin)
    manager.register(FormatterPlugin)
    manager.register(ConverterPlugin)
    manager.register(TransportPlugin)
    assert manager.filter() == [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]
    assert manager.filter(AuthPlugin) == [AuthPlugin]
    assert manager.filter(FormatterPlugin) == [FormatterPlugin]
    assert manager.filter(ConverterPlugin) == [ConverterPlugin]
    assert manager.filter(TransportPlugin) == [TransportPlugin]

# Generated at 2022-06-13 22:37:27.592533
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PluginManager.register(*ENTRY_POINT_NAMES)

# Generated at 2022-06-13 22:37:39.350308
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    id_to_plugin = {
        'json': MockFormatterPlugin(group_name='json'),
        'json-pp': MockFormatterPlugin(group_name='json'),
        'json-pretty': MockFormatterPlugin(group_name='json'),
        'text': MockFormatterPlugin(group_name='text'),
        'html': MockFormatterPlugin(group_name='html'),
    }
    pm = PluginManager([id_to_plugin[e] for e in ['json', 'html', 'text', 'json-pretty', 'json-pp']])

# Generated at 2022-06-13 22:37:51.002425
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print()
    print("Unit test for method load_installed_plugins of class PluginManager")
    lst = PluginManager()
    lst.load_installed_plugins()
    # print(lst)
    # print(lst.get_auth_plugins())
    # print(lst.get_auth_plugin_mapping())
    # print(lst.get_auth_plugin('basic'))
    print(lst.get_formatters())
    print(lst.get_formatters_grouped())
    print(lst.get_converters())
    print(lst.get_transport_plugins())
    print(repr(lst))


if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:38:14.046473
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    all_status = True
    for item in ENTRY_POINT_NAMES:
        all_status = False if not all_status else pm.filter(3, item)
    if not all_status:
        raise Exception(f'Error: Some of the plugins are not found {pm}')
    else:
        print('Unit test for PluginManager class has passed')

import time


# Generated at 2022-06-13 22:38:18.165962
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    mgr = PluginManager()
    grp = mgr.get_formatters_grouped()
    assert isinstance(grp, dict)
    assert 1 in grp

# Generated at 2022-06-13 22:38:24.572808
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from .JSONPlugin import JSONPlugin
    from .PrettyHTTPPlugin import PrettyHTTPPlugin
    from .RawPlugin import RawPlugin

    manager = PluginManager()
    manager.register(JSONPlugin, PrettyHTTPPlugin, RawPlugin)
    assert manager.get_formatters_grouped() == {
        'json': [JSONPlugin],
        'http': [PrettyHTTPPlugin],
        'debug': [RawPlugin],
        'default': [PrettyHTTPPlugin],
    }

# Generated at 2022-06-13 22:38:26.797905
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():    
    manager = PluginManager()
    manager.register(HttpiePlugin)
    assert manager.get_formatters_grouped() == {'httpie': [HttpiePlugin]}



# Generated at 2022-06-13 22:38:30.813474
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth
    assert PluginManager().filter(AuthPlugin).count(HTTPBasicAuth) == 1

# Generated at 2022-06-13 22:38:38.421058
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import (
        BuiltinJSONFormatter,
        BuiltinPrettyJSONFormatter,
        BuiltinTableFormatter,
    )
    manager = PluginManager()
    manager.register(BuiltinJSONFormatter, BuiltinPrettyJSONFormatter, BuiltinTableFormatter)

    formatters_grouped = manager.get_formatters_grouped()
    assert formatters_grouped.keys() == {'pretty', 'ugly'}

    assert len(formatters_grouped['pretty']) == 2
    assert len(formatters_grouped['ugly']) == 1

    example_pretty_formatter = formatters_grouped['pretty'][0]
    assert example_pretty_formatter.group_name == 'pretty'
    assert example_pretty_formatter.display_name == 'Pretty'
   

# Generated at 2022-06-13 22:38:47.713373
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class AuthPlugin1(AuthPlugin): pass
    class AuthPlugin2(AuthPlugin): pass
    class ConverterPlugin1(ConverterPlugin): pass
    class ConverterPlugin2(ConverterPlugin): pass
    class FormatterPlugin1(FormatterPlugin): pass
    class FormatterPlugin2(FormatterPlugin): pass
    class TransportPlugin1(ConverterPlugin): pass
    class TransportPlugin2(ConverterPlugin): pass

    plugins = [
        AuthPlugin1,
        AuthPlugin2,
        ConverterPlugin1,
        ConverterPlugin2,
        FormatterPlugin1,
        FormatterPlugin2,
        TransportPlugin1,
        TransportPlugin2
    ]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)

# Generated at 2022-06-13 22:39:00.583357
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class AuthPlugin1(AuthPlugin):
        auth_type = 'hi'

    class AuthPlugin2(AuthPlugin):
        auth_type = 'hi'

    class FormatterPlugin1(FormatterPlugin):
        group_name = 'hi'

    class FormatterPlugin2(FormatterPlugin):
        group_name = 'hi'

    class ConverterPlugin1(ConverterPlugin):
        group_name = 'hi'

    class ConverterPlugin2(ConverterPlugin):
        group_name = 'hi'

    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin1, AuthPlugin2, FormatterPlugin1, FormatterPlugin2, ConverterPlugin1, ConverterPlugin2)

    print(plugin_manager)

    assert len(plugin_manager.filter(AuthPlugin)) == 2

# Generated at 2022-06-13 22:39:06.969368
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pluginManager = PluginManager()
    pluginManager.register(
        TableFormatter,
        CSVFormatter,
        JSONFormatter,
        JSONLinesFormatter,
        HTMLFormatter
    )

    result = {
        'Table': [TableFormatter],
        'CSV': [CSVFormatter],
        'JSON': [JSONFormatter],
        'JSON Lines': [JSONLinesFormatter],
        'HTML': [HTMLFormatter],
        'Custom': [],
        'Others': []
    }
    assert isinstance(pluginManager.get_formatters_grouped(), type(result))
    assert pluginManager.get_formatters_grouped() == result



# Generated at 2022-06-13 22:39:08.826499
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0


# Generated at 2022-06-13 22:39:49.532048
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert isinstance(plugin_manager,list)
    assert isinstance(plugin_manager.get_formatters(),list)
    assert isinstance(plugin_manager.get_converters(),list)
    assert isinstance(plugin_manager.get_auth_plugins(),list)

# Generated at 2022-06-13 22:39:53.572122
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    # Create instance of PluginManager
    pm = PluginManager()

    # Assert that load_installed_plugins method is working as expected
    assert pm.load_installed_plugins() is None


# Generated at 2022-06-13 22:40:00.531350
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class FakePlugin(BasePlugin):
        pass
    class FakeTransportPlugin(TransportPlugin):
        pass

    mocked_plugins = {
        ('httpie.plugins.auth.v1', 'FakePlugin'): FakePlugin,
        ('httpie.plugins.auth.v1', 'FakeTransportPlugin'): FakeTransportPlugin,
    }
    mocked_entry_point_dist = type('FakeEntryPointDist', (), {
        'key': 'FakePackageName'
    })

    def mocked_iter_entry_points(name: str) -> List[object]:
        plugin_type, plugin_name = name.split('.')[-2:]
        plugin = mocked_plugins[plugin_type, plugin_name]

# Generated at 2022-06-13 22:40:04.580681
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    msg = 'PluginManager() did not load all installed plugins'
    assert len(plugins) == len(ENTRY_POINT_NAMES), msg

# Generated at 2022-06-13 22:40:06.514934
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    result = PluginManager()
    result.load_installed_plugins()
    assert result

# Generated at 2022-06-13 22:40:13.107225
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    active_plugins = PluginManager()
    active_plugins.load_installed_plugins()
    assert active_plugins.get_auth_plugin('basic') == BasicAuthPlugin
    assert active_plugins.get_auth_plugin('digest') == DigestAuthPlugin
    assert active_plugins.get_auth_plugin('hawk') == HawkAuthPlugin
    assert active_plugins.get_auth_plugin('ntlm') == NTLMAuthPlugin



# Generated at 2022-06-13 22:40:24.310624
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Create an instance of PluginManager Object.
    plugin_manager = PluginManager()

    # Create an instance of FormatterPlugin Object.
    class TestFormatterPlugin(FormatterPlugin):
        group_name = 'testFormatterPlugin_group'

    # Add the created object to the plugin_manager list.
    plugin_manager.register(TestFormatterPlugin)

    # Create another instance of FormatterPlugin Object.
    class TestFormatterPlugin2(FormatterPlugin):
        group_name = 'testFormatterPlugin_group'

    # Add the created object to the plugin_manager list.
    plugin_manager.register(TestFormatterPlugin2)

    # Store the expected result in a variable.
    expected_result = {'testFormatterPlugin_group': [TestFormatterPlugin, TestFormatterPlugin2]}

    # Call the function get_formatters

# Generated at 2022-06-13 22:40:27.201203
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    a = PluginManager()
    a.register(TransportPlugin)
    assert a.filter(TransportPlugin) == [TransportPlugin]
    a.register(AuthPlugin)
    assert a.filter(TransportPlugin) == [TransportPlugin]
    assert a.filter(AuthPlugin) == [AuthPlugin]

# Generated at 2022-06-13 22:40:31.839743
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager)
    assert len(manager) > 0
    assert len(manager.filter(AuthPlugin)) == 2


# Generated at 2022-06-13 22:40:42.696189
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D: pass

    class A2: pass
    class B2(A2): pass
    class C2(B2): pass
    class D2: pass

    class A3: pass
    class B3(A3): pass
    class C3(B3): pass
    class D3: pass

    plugin_manager = PluginManager()
    plugin_manager.register(A, B, C, D, A2, B2, C2, D2, A3, B3, C3, D3)
    assert(plugin_manager.filter(A) == [A, B, C, A2, B2, C2, A3, B3, C3])

# Generated at 2022-06-13 22:41:54.476422
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_instance = PluginManager()
    plugin_instance.register(AuthPlugin, FormatterPlugin, ConverterPlugin)
    assert len(plugin_instance.filter()) == 3
    assert len(plugin_instance.filter(AuthPlugin)) == 1
    assert len(plugin_instance.filter(FormatterPlugin)) == 1
    assert len(plugin_instance.filter(ConverterPlugin)) == 1



# Generated at 2022-06-13 22:41:55.787183
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()

# Generated at 2022-06-13 22:41:59.103178
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.load_installed_plugins()

    plugins = pm.filter(AuthPlugin)
    assert len(plugins) != 0
    assert all(issubclass(plugin, AuthPlugin) for plugin in plugins)


PLUGIN_MANAGER = PluginManager()
PLUGIN_MANAGER.load_installed_plugins()

# Generated at 2022-06-13 22:42:03.467022
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class PluginA(BasePlugin):
        pass
    class PluginB(BasePlugin):
        pass
    class PluginC(PluginA):
        pass
    
    test = PluginManager()
    test.register(PluginA, PluginB, PluginC)
    target = test.filter(BasePlugin)
    assert len(target) == 3
    assert PluginA in target
    assert PluginB in target
    assert PluginC in target


# Generated at 2022-06-13 22:42:09.411718
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PM = PluginManager()
    PM.register(AuthPlugin)
    PM.register(FormatterPlugin)
    PM.register(ConverterPlugin)
    PM.register(TransportPlugin)
    assert PM.filter(AuthPlugin) == [AuthPlugin]
    assert PM.filter(FormatterPlugin) == [FormatterPlugin]
    assert PM.filter(ConverterPlugin) == [ConverterPlugin]
    assert PM.filter(TransportPlugin) == [TransportPlugin]
    print('PluginManager.filter() unit testing passed!')


# Generated at 2022-06-13 22:42:15.569665
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    '''
    # Get a list of all the auth plugins available
    '''
    mgr = PluginManager()
    mgr.load_installed_plugins()
    print("\nGet a list of all the auth plugins available")
    print(mgr.get_auth_plugin_mapping())


# Generated at 2022-06-13 22:42:24.327300
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_formatters = [
        {'group_name': 'test', 'plugin': 'test_plugin'},
        {'group_name': 'test1', 'plugin': 'test_plugin1'},
        {'group_name': 'test1', 'plugin': 'test_plugin2'},
        {'group_name': 'test2', 'plugin': 'test_plugin3'},
        {'group_name': 'test2', 'plugin': 'test_plugin4'}
    ]
    test_obj = PluginManager()
    for fmt in test_formatters:
        class TestPlugin(FormatterPlugin):
            group_name = fmt['group_name']
        test_obj.register(TestPlugin)


# Generated at 2022-06-13 22:42:26.012919
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    if __name__ == '__main__':
        pm = PluginManager()
        pm.register(PluginManager)
        assert (pm.get_formatters_grouped() == {'others': [PluginManager]})



# Generated at 2022-06-13 22:42:29.677521
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    '''
    Unit test for method get_formatters_grouped of class PluginManager
    :return:
    '''
    pm = PluginManager()
    pm.load_installed_plugins()

# Generated at 2022-06-13 22:42:35.584647
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from importlib.resources import path
    from os import path as os_path
    from pathlib import Path
    from shutil import rmtree
    from unittest import mock
    from httpie.compat import is_windows

    class DummyPlugin(BasePlugin):
        pass

    class DummyPlugin2(BasePlugin):
        pass

    manager = PluginManager()
