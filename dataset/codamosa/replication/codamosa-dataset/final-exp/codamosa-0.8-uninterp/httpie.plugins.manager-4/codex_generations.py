

# Generated at 2022-06-13 22:33:16.833415
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    print(pm.get_formatters())


# Generated at 2022-06-13 22:33:21.141224
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    expected_output = {
        '1': [],
        '2': [],
        '3': [],
    }

    assert plugin_manager.get_formatters_grouped() == expected_output

# Generated at 2022-06-13 22:33:29.430197
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class FormatPlugin1(FormatterPlugin):
        group_name = 'group_name_1'
    class FormatPlugin2(FormatterPlugin):
        group_name = 'group_name_2'
    class FormatPlugin3(FormatterPlugin):
        group_name = 'group_name_1'
    plugins_manager = PluginManager()
    plugins_manager.register(FormatPlugin1, FormatPlugin2, FormatPlugin3)
    group_dict = plugins_manager.get_formatters_grouped()
    assert group_dict['group_name_1'] == [FormatPlugin1, FormatPlugin3]
    assert group_dict['group_name_2'] == [FormatPlugin2]
# ===========================

plugins_manager = PluginManager()
plugins_manager.load_installed_plugins()

# Generated at 2022-06-13 22:33:32.823563
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins(plugins)
    assert plugins.__repr__() == '<PluginManager: []>'

# Generated at 2022-06-13 22:33:35.415800
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins is not None


# Generated at 2022-06-13 22:33:45.072912
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import ConverterPlugin, FormatterPlugin
    from httpie.plugins.builtin import JSONPathFilterPlugin

    class A(FormatterPlugin):
        group_name = 'a'

    class B(FormatterPlugin):
        group_name = 'a'

    class C(FormatterPlugin):
        group_name = 'c'

    class D(ConverterPlugin):
        pass

    class E(JSONPathFilterPlugin):
        pass

    pm = PluginManager()
    pm.register(A, B, C, D, E)

    formatters_grouped = pm.get_formatters_grouped()
    assert formatters_grouped['a'] == [A, B]
    assert formatters_grouped['c'] == [C]


# Generated at 2022-06-13 22:33:51.790220
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager
    pm.register = Mock()
    pm.load_installed_plugins = Mock(wraps=lambda _:
                                       pm.register(Mock(), Mock(), Mock(), Mock()))
    pm.load_installed_plugins()
    assert pm.register.call_count == 4


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:34:02.868960
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    auth_plugins = [
        type('BasicAuthPlugin', (AuthPlugin, object), {'auth_type': 'basic'}),
        type('DigestAuthPlugin', (AuthPlugin, object), {'auth_type': 'digest'})
    ]
    manager = PluginManager(auth_plugins)
    auth_plugin_mapping = manager.get_auth_plugin_mapping()
    assert len(auth_plugin_mapping) == 2
    assert 'basic' in auth_plugin_mapping
    assert 'digest' in auth_plugin_mapping
    assert auth_plugin_mapping['basic'] == auth_plugins[0]
    assert auth_plugin_mapping['digest'] == auth_plugins[1]

# Generated at 2022-06-13 22:34:08.106709
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) == 1
    assert len(plugin_manager.get_formatters_grouped()) == 1
    assert len(plugin_manager.get_transport_plugins()) == 1


# Generated at 2022-06-13 22:34:12.271997
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(FormatterPlugin)
    # result = pm.get_formatters_grouped()
    # assert result == {}
    # assert result is not None


# Generated at 2022-06-13 22:34:20.260290
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.base import BasePlugin, AuthPlugin, FormatterPlugin, ConverterPlugin

    class PluginFoo(BasePlugin):
        pass

    class PluginFooAuth(AuthPlugin):
        pass

    class PluginFooConverter(ConverterPlugin):
        pass

    class PluginFooFormatter(FormatterPlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(PluginFooAuth, PluginFooConverter, PluginFooFormatter)



# Generated at 2022-06-13 22:34:23.671848
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginManager.get_auth_plugin_mapping = object()
    PluginManager.get_auth_plugin_mapping = object()
    PluginManager.get_auth_plugin_mapping = object()


# Generated at 2022-06-13 22:34:27.549876
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()

    print (plugins)


if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:34:38.981799
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    #Create a list of plugins
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(ConverterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(TransportPlugin)
    
    # Unit test AuthPlugin
    assert plugin_manager.filter(AuthPlugin) == [AuthPlugin]
    
    # Unit test ConverterPlugin
    assert plugin_manager.filter(ConverterPlugin) == [ConverterPlugin]
    
    # Unit test FormatterPlugin
    assert plugin_manager.filter(FormatterPlugin) == [FormatterPlugin]
    
    # Unit test TransportPlugin
    assert plugin_manager.filter(TransportPlugin) == [TransportPlugin]


# Generated at 2022-06-13 22:34:40.405994
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()

# Generated at 2022-06-13 22:34:46.448812
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginmanager = PluginManager()
    pluginmanager.load_installed_plugins()
    assert len(pluginmanager.get_auth_plugins()) > 0
    assert len(pluginmanager.get_formatters_grouped()) > 0
    assert len(pluginmanager.get_converters()) > 0
    assert len(pluginmanager.get_transport_plugins()) > 0


# Generated at 2022-06-13 22:34:52.291146
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager.filter(AuthPlugin))
    print(plugin_manager.filter(FormatterPlugin))
    print(plugin_manager.filter(ConverterPlugin))
    print(plugin_manager.filter(TransportPlugin))


# Generated at 2022-06-13 22:35:04.017589
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()

# Generated at 2022-06-13 22:35:06.777373
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugins = plugin_manager.filter()
    assert len(plugins) > 0

# Generated at 2022-06-13 22:35:19.431207
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    def get_formatters_grouped():
        from httpie.plugins.builtin import BuiltinFormatterPlugin
        from httpie.plugins.json import JSONFormatterPlugin
        from httpie.plugins.pretty import PrettyFormatterPlugin
        from httpie.plugins.raw import RawFormatterPlugin

        return {
            'Visual': [PrettyFormatterPlugin],
            'Raw': [RawFormatterPlugin],
            'Data Serialization': [JSONFormatterPlugin],
            'Builtin': [BuiltinFormatterPlugin]
        }

    plugin_manager = PluginManager()
    plugin_manager.register(BuiltinFormatterPlugin, JSONFormatterPlugin, PrettyFormatterPlugin, RawFormatterPlugin)

    assert plugin_manager.get_formatters_grouped() == get_formatters_grouped()


# Generated at 2022-06-13 22:35:33.882186
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # initialize an empty list, which will be filled
    # as load_installed_plugins of class PluginManager
    # is run
    httpie_plugins_list = []

    # create an instance of PluginManager and 
    # invoke load_installed_plugins
    pm = PluginManager()
    pm.load_installed_plugins()

    # fill httpie_plugins_list with the plugins
    # loaded by PluginManager
    httpie_plugins_list = pm.filter()

    # can only be executed after the httpie_plugins_list
    # is declared
    def count_plugins(httpie_plugins_list):
        # count the number of plugins
        num_httpie_plugins = 0
        for plugin in httpie_plugins_list:
            num_httpie_plugins += 1
        return num_httpie_plugins

    # check if plugins were

# Generated at 2022-06-13 22:35:36.562582
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:35:43.556678
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.register(A)
    manager.register(B)
    manager.register(C)
    
    assert len(manager.filter(by_type=X)) == 3
    assert len(manager.filter(by_type=Y)) == 2
    assert len(manager.filter(by_type=Z)) == 1

# Generated at 2022-06-13 22:35:53.736782
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pkg_resources
    from httpie import __package__ as pkg
    from httpie._compat import is_windows
    import os
    import sys
    import unittest

    class TestPluginManager(unittest.TestCase):
        def test_load_plugins(self):
            base_path = pkg_resources.resource_filename(pkg, 'plugins')
            if is_windows:
                plugins_path = os.path.join(base_path, 'windows')
            else:
                plugins_path = os.path.join(base_path, 'unix')
            sys.path.insert(0, plugins_path)

# Generated at 2022-06-13 22:36:00.895106
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # arrange
    plugin_manager = PluginManager()
    plugin1 = MagicMock()
    plugin2 = MagicMock()
    plugin_manager.register(plugin1, plugin2)
    assert len(plugin_manager) == 2
    # act
    plugin_manager.load_installed_plugins()
    # assert
    assert len(plugin_manager) > 2
    assert plugin1 in plugin_manager
    assert plugin2 in plugin_manager



# Generated at 2022-06-13 22:36:04.450712
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert plugin_manager.get_formatters_grouped() == {
        'web browser': [], 'generic': [], 'web service': []
    }



# Generated at 2022-06-13 22:36:12.338995
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    import pdb; pdb.set_trace()
    assert all([plugin in plugin_manager for plugin in plugin_manager])
    for plugins in [plugin_manager.get_auth_plugins(),
                    plugin_manager.get_formatters(),
                    plugin_manager.get_converters(),
                    plugin_manager.get_transport_plugins()]:
        assert len(plugins) >= 1
        for plugin in plugins:
            assert isinstance(plugin, BasePlugin)


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:36:23.525871
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.plugins

    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()

    plugin_mapping = pluginManager.get_formatters_grouped()

    # Group 0:
    assert list(map(
        lambda x: x.__module__ + '.' + x.__name__,
        plugin_mapping['HTTP']
    )) == [
        'httpie.plugins.format.httpie.HTTPieJSONFormatter',
        'httpie.plugins.format.httpie.HTTPieFormFormatter'
    ]

    assert list(map(
        lambda x: x.__module__ + '.' + x.__name__,
        plugin_mapping['Browser']
    )) == [
        'httpie.plugins.format.browser.BrowserFormatter'
    ]


# Generated at 2022-06-13 22:36:33.560938
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Plugin1(BasePlugin):
        pass

    class Plugin2(Plugin1):
        pass

    class Plugin3(Plugin1):
        pass

    class Plugin4(BasePlugin):
        pass

    class Plugin5(Plugin4):
        pass

    manager = PluginManager()
    manager.register(Plugin1, Plugin2, Plugin3, Plugin4, Plugin5)
    assert len(manager) == 5

    plugins = manager.filter(by_type=BasePlugin)
    assert len(plugins) == 5
    assert all(isinstance(plugin, BasePlugin) for plugin in plugins)

    plugins = manager.filter(by_type=Plugin1)
    assert len(plugins) == 3
    assert all(issubclass(plugin, Plugin1) for plugin in plugins)

    plugins = manager.filter(by_type=Plugin4)

# Generated at 2022-06-13 22:36:36.769860
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # print(plugin_manager.get_formatters_grouped())
    assert plugin_manager.get_formatters_grouped()['JSON']
    assert len(plugin_manager.get_formatters_grouped()) > 5

# Generated at 2022-06-13 22:36:41.152119
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager)
    assert len(manager) > 0

# Generated at 2022-06-13 22:36:46.387881
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    global entry_point
    entry_point_name = 'httpie.plugins.auth.v1'
    entry_point = iter_entry_points(entry_point_name)
    plugin = entry_point.load()
    plugin.package_name = entry_point.dist.key
    self.register(entry_point.load())
    return self.filter(AuthPlugin)

test_PluginManager_filter()

# Generated at 2022-06-13 22:36:53.574494
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.load_installed_plugins()
    f_groups = pm.get_formatters_grouped()
    for group_name, group in f_groups.items():
        for f in group:
            assert isinstance(f, FormatterPlugin)
    assert len(f_groups['pretty']) == 4
    assert f_groups['pretty'][1].__name__ == 'ColoredFormatter'
    assert f_groups['ugly'][0].__name__ == 'DisabledFormatter'
    assert f_groups['ugly'][1].__name__ == 'JSONFormatter'



# Generated at 2022-06-13 22:36:56.472936
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0

# Generated at 2022-06-13 22:37:03.572323
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    """
    unit test for method get_auth_plugin_mapping of class PluginManager
    """
    plugins = PluginManager()
    # It should work normally as long as it has been loaded
    plugins.load_installed_plugins()
    assert plugins.get_auth_plugin_mapping() != {}


# Generated at 2022-06-13 22:37:10.624209
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth, KeyValuesArgType

    assert issubclass(HTTPBasicAuth, AuthPlugin)
    assert issubclass(HTTPDigestAuth, AuthPlugin)

    assert issubclass(KeyValuesArgType, ConverterPlugin)


    pm = PluginManager()
    pm.register(HTTPBasicAuth, HTTPDigestAuth, KeyValuesArgType)

    assert pm.get_auth_plugins() == [HTTPBasicAuth, HTTPDigestAuth]
    assert pm.get_converters() == [KeyValuesArgType]



# Generated at 2022-06-13 22:37:23.748877
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm=PluginManager()
    class AuthPluginA(AuthPlugin):
        pass
    class AuthPluginB(AuthPlugin):
        pass
    class AuthPluginC(AuthPlugin):
        pass
    class FormatterPluginA(FormatterPlugin):
        pass
    class FormatterPluginB(FormatterPlugin):
        pass
    class FormatterPluginC(FormatterPlugin):
        pass
    class ConverterPluginA(ConverterPlugin):
        pass
    class ConverterPluginB(ConverterPlugin):
        pass
    class ConverterPluginC(ConverterPlugin):
        pass

# Generated at 2022-06-13 22:37:28.119335
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.register(object)
    pm.register(AuthPlugin)
    
    mapping = pm.get_auth_plugin_mapping()
    assert mapping == {}
    
    pm.register(AuthPlugin)
    mapping = pm.get_auth_plugin_mapping()
    assert mapping == {'AuthPlugin': AuthPlugin}

# Generated at 2022-06-13 22:37:36.098838
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # sut
    manager = PluginManager()
    manager.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)

    # test
    assert len(manager.filter(AuthPlugin)) == 1
    assert len(manager.filter(ConverterPlugin)) == 1
    assert len(manager.filter(FormatterPlugin)) == 1
    assert len(manager.filter(TransportPlugin)) == 1

    assert len(manager.filter()) == 0


# Generated at 2022-06-13 22:37:41.221475
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert issubclass(AuthPlugin, BasePlugin)
    assert issubclass(FormatterPlugin, BasePlugin)
    assert issubclass(ConverterPlugin, BasePlugin)
    assert issubclass(TransportPlugin, BasePlugin)
    assert issubclass(BasePlugin, object)
    assert issubclass(object, object)

plugin_manager = PluginManager()

# Generated at 2022-06-13 22:37:53.854987
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pkg_resources
    from mock import patch

    global ENTRY_POINT_NAMES
    mock_iter_entry_points = pkg_resources.iter_entry_points

    # Mock entry_points
    def mock_iter_entry_points(entry_point_name):
        class EntryPoint():
            class dist():
                key = "key"
            load = lambda self: 'Test'
        if entry_point_name == 'httpie.plugins.auth.v1':
            return [EntryPoint()]
        elif entry_point_name == 'httpie.plugins.formatter.v1':
            return [EntryPoint()]
        elif entry_point_name == 'httpie.plugins.converter.v1':
            return [EntryPoint()]

# Generated at 2022-06-13 22:37:57.456086
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    print("Testing method load_installed_plugins of class PluginManager")
    plugins = PluginManager()
    plugins.load_installed_plugins()
    
    if len(plugins) < 1:
        raise ValueError(f"PluginManager.load_installed_plugins is error, because len of plugins < 1")


# Generated at 2022-06-13 22:38:02.963635
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth

    plugin_manager = PluginManager()
    plugin_manager.register(HTTPBasicAuth)

    assert plugin_manager.filter(AuthPlugin) == [HTTPBasicAuth]
    assert plugin_manager.filter(FormatterPlugin) == []


# Generated at 2022-06-13 22:38:14.098441
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # mock a PluginManager
    class TextFormatterPlugin(FormatterPlugin):
        group_name='Text'
    class XMLFormatterPlugin(FormatterPlugin):
        group_name='XML'
    class JSONFormatterPlugin(FormatterPlugin):
        group_name='JSON'
    class HTMLFormatterPlugin(FormatterPlugin):
        group_name='HTML'
    class NewFormatterPlugin(FormatterPlugin):
        group_name='New'
    plugin_manager = PluginManager()
    plugin_manager.register(TextFormatterPlugin,XMLFormatterPlugin,JSONFormatterPlugin,HTMLFormatterPlugin)
    result = plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:38:19.518374
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    p = PluginManager()
    p.load_installed_plugins()
    assert len(p) > 0
    assert all(isinstance(plugin, AuthPlugin) for plugin in p)
    assert all([plugin.package_name != 'httpie' for plugin in p])


# Generated at 2022-06-13 22:38:24.951430
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins.register(AuthPlugin, FormatterPlugin, ConverterPlugin)
    assert plugins.filter(by_type=AuthPlugin) == [AuthPlugin]
    assert plugins.filter(by_type=FormatterPlugin) == [FormatterPlugin]
    assert plugins.filter(by_type=ConverterPlugin) == [ConverterPlugin]


# Generated at 2022-06-13 22:38:27.060878
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters()
    str(repr(plugin_manager))

# Generated at 2022-06-13 22:38:35.636667
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    list_of_plugins = [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]
    pluginManager = PluginManager()
    pluginManager.register(*list_of_plugins)
    assert pluginManager.filter() == list_of_plugins, 'Filter is not working'
    assert pluginManager.filter(by_type=AuthPlugin) == [AuthPlugin], 'Filter is not working'
    assert pluginManager.filter(by_type=ConverterPlugin) == [ConverterPlugin], 'Filter is not working'
    assert pluginManager.filter(by_type=TransportPlugin) == [TransportPlugin], 'Filter is not working'
    assert pluginManager.filter(by_type=FormatterPlugin) == [FormatterPlugin], 'Filter is not working'

# Generated at 2022-06-13 22:38:39.795172
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class B(BasePlugin): pass
    class A(BasePlugin): pass

    pm = PluginManager()
    pm.append(A)
    pm.append(B)

    pm.load_installed_plugins()
    assert pm == [B, A]

# Generated at 2022-06-13 22:38:44.063500
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_formatters_grouped() == {
        'group_name': ['plugin_class_name'],
        'group_name2': ['plugin_class_name2']
    }


# Generated at 2022-06-13 22:38:53.399577
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager_installed = PluginManager()
    PluginManager_installed.load_installed_plugins()
    assert 'httpie_jwt_auth' in [i.package_name for i in PluginManager_installed]

# Generated at 2022-06-13 22:39:01.666020
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    # Create a PluginManager instance
    plugin_manager = PluginManager()

    # Register some plugins to this instance
    plugin_manager.register(
        HTTPBasicAuth,
        HTTPTokenAuth,
        AuthPlugin,
        FormatterPlugin,
        ConverterPlugin,
        TransportPlugin,
        GzipTransport,
        HTTPDeflateTransport
    )

    # Test if the result will be what we expected
    assert plugin_manager.filter(AuthPlugin) == [HTTPBasicAuth, HTTPTokenAuth]
    assert plugin_manager.filter(FormatterPlugin) == []
    assert plugin_manager.filter(ConverterPlugin) == []
    assert plugin_manager.filter(TransportPlugin) == [GzipTransport, HTTPDeflateTransport]

# Generated at 2022-06-13 22:39:07.980148
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class P(BasePlugin): pass
    class P1(P): pass
    class P2(P): pass
    class P3(P): pass
    class P1_1(P1): pass
    class P2_1(P2): pass
    class P2_2(P2): pass
    class P2_3(P2): pass
    # P1, P2, P3, P1_1, P2_1, P2_2, P2_3
    plugins = PluginManager([P1, P2, P3, P1_1, P2_1, P2_2, P2_3])
    # total plugins
    assert len(plugins.filter()) == 7
    # total BasePlugin
    assert len(plugins.filter(BasePlugin)) == 7
    # total P

# Generated at 2022-06-13 22:39:15.655062
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A:
        pass

    class B:
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    class F(D, B):
        pass

    class G(E, F, C):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(A, B, C, D, E, F, G)
    assert len(plugin_manager.filter(A)) == 4
    assert len(plugin_manager.filter(B)) == 4
    assert len(plugin_manager.filter(C)) == 3
    assert len(plugin_manager.filter(D)) == 2
    assert len(plugin_manager.filter(E)) == 1
    assert len(plugin_manager.filter(F)) == 1

# Generated at 2022-06-13 22:39:20.669241
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(A, B, C)
    assert manager.get_formatters_grouped() == {
        'A': [A],
        'B': [B],
        'C': [C]
    }



# Generated at 2022-06-13 22:39:24.918007
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    return plugins.__repr__()

print(test_PluginManager_load_installed_plugins())




# Generated at 2022-06-13 22:39:32.077142
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    #      Subclass     ,    Superclass
    #   Subclass    ,  Superclass
    #  Subclass      , Superclass
    # Subclass       ,Superclass
    assert PluginManager().filter(AuthPlugin) == []
    assert PluginManager().filter(ConverterPlugin) == []
    assert PluginManager().filter(FormatterPlugin) == []
    assert PluginManager().filter(TransportPlugin) == []
    assert PluginManager([AuthPlugin]).filter(AuthPlugin) == [AuthPlugin]
    assert PluginManager([ConverterPlugin]).filter(ConverterPlugin) == [ConverterPlugin]
    assert PluginManager([FormatterPlugin]).filter(FormatterPlugin) == [FormatterPlugin]
    assert PluginManager([TransportPlugin]).filter(TransportPlugin) == [TransportPlugin]
    # Edge Cases

# Generated at 2022-06-13 22:39:37.508570
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert len(plugin_manager.get_formatters_grouped()) == 1
    assert 'HTML' in plugin_manager.get_formatters_grouped()
    assert len(plugin_manager.get_formatters_grouped()['HTML']) == 1
    assert plugin_manager.get_formatters_grouped()['HTML'][0].name == 'html'

# Generated at 2022-06-13 22:39:41.345360
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0


# Generated at 2022-06-13 22:39:52.861451
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert (
        PluginManager.filter(
            [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin],
            AuthPlugin
        )
        == [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]
    )
    assert (
        PluginManager.filter(
            [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin],
            FormatterPlugin
        )
        == [FormatterPlugin, ConverterPlugin]
    )
    assert (
        PluginManager.filter(
            [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin],
            ConverterPlugin
        )
        == [ConverterPlugin]
    )
    assert (
        PluginManager.filter(
            [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin],
            TransportPlugin
        )
        == []
    )

# Generated at 2022-06-13 22:40:06.616462
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    import httpie.plugins.builtin
    pm = PluginManager()
    assert [[httpie.plugins.builtin.HTTPBasicAuth]] == pm.filter(AuthPlugin)

# Generated at 2022-06-13 22:40:07.685524
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()

# Generated at 2022-06-13 22:40:12.680876
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin = PluginManager()
    plugin.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)
    plugin.filter(AuthPlugin)
    plugin.filter(ConverterPlugin)
    plugin.filter(FormatterPlugin)
    plugin.filter(TransportPlugin)


# Generated at 2022-06-13 22:40:20.335483
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(DummyAuthPlugin1, DummyAuthPlugin2)
    (plugin_name1, plugin_instance1), (plugin_name2, plugin_instance2) = \
        plugins.get_auth_plugin_mapping().items()
    assert plugin_name1 == 'test-auth-1' and \
        plugin_name2 == 'test-auth-2' and \
        issubclass(plugin_instance1, DummyAuthPlugin1) and \
        issubclass(plugin_instance2, DummyAuthPlugin2)


# Generated at 2022-06-13 22:40:22.884896
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = PluginManager().get_formatters()
    formatters_grouped = PluginManager().get_formatters_grouped()
    assert len(formatters) > 0
    assert len(formatters_grouped) > 0

# Generated at 2022-06-13 22:40:27.998616
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager[0] == BasicAuthPlugin
    assert plugin_manager[1] == DigestAuthPlugin
    assert plugin_manager[2] == JsonPlugin
    assert plugin_manager[3] == PrettyJsonPlugin
    assert plugin_manager[4] == FormPlugin
    assert plugin_manager[5] == UrlencodedPlugin
    assert plugin_manager[6] == ResponseContentPlugin
    assert plugin_manager[7] == UrlPlugin
    assert plugin_manager[8] == CurlTransportPlugin

# Generated at 2022-06-13 22:40:32.793330
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """Test for method get_formatters_grouped of class PluginManager."""
    class PluginA(FormatterPlugin):
        group_name = 'Group A'
        __test__ = False
    class PluginB(FormatterPlugin):
        group_name = 'Group B'
        __test__ = False
    class PluginC(FormatterPlugin):
        group_name = 'Group A'
        __test__ = False
    class PluginD(FormatterPlugin):
        group_name = 'Group B'
        __test__ = False
    manager = PluginManager()
    manager.register(PluginA, PluginB, PluginC, PluginD)
    assert manager.get_formatters_grouped() == {
        'Group A': [PluginA, PluginC],
        'Group B': [PluginB, PluginD],
    }

# Generated at 2022-06-13 22:40:40.801576
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins_manager = PluginManager()

    class FormatterPlugin1(FormatterPlugin):
        group_name = '1'
    class FormatterPlugin2(FormatterPlugin):
        group_name = '2'

    plugins_manager.register(FormatterPlugin1, FormatterPlugin2)

    expected_value = {'1': [FormatterPlugin1], '2': [FormatterPlugin2]}
    actual_value = plugins_manager.get_formatters_grouped()

    assert expected_value == actual_value

# Generated at 2022-06-13 22:40:43.997208
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    p = PluginManager()
    assert list(p.filter(AuthPlugin)) == []
    assert list(p.filter(FormatterPlugin)) == []
    assert list(p.filter(ConverterPlugin)) == []
    assert list(p.filter(TransportPlugin)) == []



# Generated at 2022-06-13 22:40:49.382644
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    
    # check the type of returned value 
    def check_type(x):
        return isinstance(x, dict)
    assert check_type(plugin_manager.get_formatters_grouped())
    
    # check the length of the dictionary
    def check_length(x):
        return len(x) == 4
    assert check_length(plugin_manager.get_formatters_grouped())
    
    # check the existence of the key
    def check_key(x,y):
        return x in y.keys()
    assert check_key('Grouped', plugin_manager.get_formatters_grouped())
    assert check_key('Single', plugin_manager.get_formatters_grouped())

# Generated at 2022-06-13 22:41:20.427567
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters_grouped()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:41:24.102111
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class MyTransportPlugin(TransportPlugin):
        pass

    class MyAuthPlugin(AuthPlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(MyTransportPlugin, MyAuthPlugin)

    assert plugin_manager.filter(TransportPlugin) == [MyTransportPlugin]
    assert plugin_manager.filter(AuthPlugin) == [MyAuthPlugin]

# Generated at 2022-06-13 22:41:30.042345
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import JSONFormatterPlugin, HeadersFormatterPlugin

    def dummy_plugin(plugin, *args, **kwargs):
        plugin.group_name = 'group'
        return plugin(*args, **kwargs)
    dummy_plugin = dummy_plugin(FormatterPlugin)
    manager = PluginManager([dummy_plugin, JSONFormatterPlugin, HeadersFormatterPlugin])

    # return two groups: the one the dummy plugin belongs to, and the special group
    assert len(manager.get_formatters_grouped()) == 2
    # the dummy plugin and the JSON formatter plugin should belong to the same group
    assert len(manager.get_formatters_grouped()['group']) == 2
    # the headers formatter plugin is the only one which belongs to the special group

# Generated at 2022-06-13 22:41:36.770798
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin
    from httpie.plugins.base import BasePlugin
    from httpie.plugins.formatter.v1 import FormatterPlugin
    from httpie.plugins.auth.v1 import AuthPlugin
    from httpie.plugins.converter.v1 import ConverterPlugin

    plugin_manager = PluginManager()
    plugin_manager.register(
        AuthPlugin,
        FormatterPlugin,
        ConverterPlugin,
        BasePlugin
    )

    result = plugin_manager.filter(AuthPlugin)
    assert list(result) == [AuthPlugin]

# Generated at 2022-06-13 22:41:43.242145
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    class TestPlugin(BasePlugin):
        pass
    pm.register(TestPlugin)
    assert pm.filter() == [TestPlugin]
    assert str(pm) == '<PluginManager: [<class \'httpie.plugins.test.test_core.test_PluginManager_filter.<locals>.TestPlugin\'>]>'


# Generated at 2022-06-13 22:41:50.771459
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONPrettyFormatPlugin

    manager = PluginManager()

    assert len(manager.get_formatters_grouped()["Pretty, human-readable output"]) == 1

    manager = PluginManager()
    manager.register(JSONPrettyFormatPlugin)

    assert len(manager.get_formatters_grouped()["Pretty, human-readable output"]) == 2

# Generated at 2022-06-13 22:42:00.314727
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
	plugins = PluginManager()
	class TestPlugin1(BasePlugin):
				pass
	class TestPlugin2(BasePlugin):
				pass
	class TestPlugin3(BasePlugin):
				pass
	class TestPlugin4(BasePlugin):
				pass
	class TestPlugin5(BasePlugin):
				pass
	class TestPlugin6(BasePlugin):
				pass
	class TestPlugin7(BasePlugin):
				pass
	class TestPlugin8(BasePlugin):
				pass
	class TestPlugin9(BasePlugin):
				pass
	class TestPlugin10(BasePlugin):
				pass
	class TestPlugin11(BasePlugin):
				pass
	class TestPlugin12(AuthPlugin):
				pass


# Generated at 2022-06-13 22:42:09.179791
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    """
    Test case:
    Load the installed plugins using the entry points of the HTTPie
    """
    from sys import version_info
    from pkg_resources import iter_entry_points, _namespace_packages

    def _get_entry_point_names():
        """
        Get entry point names from HTTPie
        """
        ep_names = []
        for ep_name in ENTRY_POINT_NAMES:
            ep_names.append(ep_name)

        return ep_names

    def _get_entry_points():
        """
        Get entry points from HTTPie
        """
        ep_names = _get_entry_point_names()
        ep = []

# Generated at 2022-06-13 22:42:15.187905
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    p = PluginManager()
    p.register(HTTPBasicAuth) # class HTTPBasicAuth: auth_type = 'basic'
    m = p.get_auth_plugin_mapping()
    assert 'basic' in m
    assert m['basic'] == HTTPBasicAuth


# Generated at 2022-06-13 22:42:23.763376
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import builtin
    from httpie.plugins import formatter
    from httpie.plugins import jmespath

    def formatters_grouped_test(formatters: Dict[str, List[Type[FormatterPlugin]]]):
        print('\n')
        for group_name, formatters_grouped in formatters.items():
            print(f"{group_name}: {formatters_grouped}")

    # Test 1
    print(f"\nTest 1: only builtin")
    pm = PluginManager()
    pm.register(builtin.BuiltinPlugin)
    formatters_grouped_test(pm.get_formatters_grouped())

    # Test 2
    print(f"\nTest 2: builtin and formatter")
    pm = PluginManager()