

# Generated at 2022-06-13 22:33:24.548727
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    """Test if the load_installed_plugins method of class PluginManager
    works properly.
    """
    # Create a PluginManager instance
    plugin_manager = PluginManager()
    # Make sure that all of the plugins are loaded
    plugin_manager.load_installed_plugins()
    # Make sure that the plugin manager is not empty
    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0


# Generated at 2022-06-13 22:33:27.728532
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import Http2Plugin

    plugin_manager = PluginManager()
    plugin_manager.register(Http2Plugin)
    assert len(plugin_manager.filter()) == 1
    assert len(plugin_manager) == 1

# Generated at 2022-06-13 22:33:29.593805
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins != None

# Generated at 2022-06-13 22:33:36.241672
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PlugMan = PluginManager()
    PlugMan.load_installed_plugins()

    assert len(PlugMan) != 0
    assert len(PlugMan.get_auth_plugins()) != 0
    assert len(PlugMan.get_converters()) != 0
    assert len(PlugMan.get_formatters()) != 0
    assert len(PlugMan.get_transport_plugins()) != 0

# Generated at 2022-06-13 22:33:37.848587
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    assert plugin_manager.filter(AuthPlugin) == []

# Generated at 2022-06-13 22:33:43.670533
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    p = PluginManager()
    assert p.get_auth_plugins() == []
    assert p.get_formatters() == []
    assert p.get_converters() == []
    p.load_installed_plugins()
    assert p.get_auth_plugins() != []
    assert p.get_formatters() != []
    assert p.get_converters() != []

# Generated at 2022-06-13 22:33:47.641274
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuthPlugin, JSONFormatterPlugin, HTTPXAuthPlugin, KeyValueFormatterPlugin

    plugin_manager = PluginManager()
    plugin_manager.register(HTTPBasicAuthPlugin, HTTPXAuthPlugin, JSONFormatterPlugin, KeyValueFormatterPlugin)

    auth_plugin = plugin_manager.get_auth_plugins()
    assert HTTPBasicAuthPlugin in auth_plugin
 

# Generated at 2022-06-13 22:33:54.264126
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # Create a PluginManager
    plugin_manager = PluginManager()
    # Create a Mapping
    mapping = {
        plugin.auth_type: plugin for plugin in plugin_manager.get_auth_plugins()
    }
    # Get the method's result
    res = plugin_manager.get_auth_plugin_mapping()
    # Check equality between mapping and result
    assert mapping == res


# Generated at 2022-06-13 22:34:03.293166
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A:
        pass
    
    class B:
        pass

    class C(A):
        pass

    class D(A, B):
        pass

    class E(D, C):
        pass

    pm = PluginManager()
    pm.register(A, B, C, D, E)

    assert pm.filter(A) == [A, C, D, E]
    assert pm.filter(B) == [B, D, E]
    assert pm.filter(D) == [D, E]

# Generated at 2022-06-13 22:34:17.272393
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    '''
    Tests that get_formatters_grouped method of PluginManager class 
    will return a dictionary where keys are the group names and values are lists
    of formatters in these groups
    '''
    manager = PluginManager()
    manager.load_installed_plugins()
    formatters = manager.get_formatters()
    groups = manager.get_formatters_grouped()

    # expected formatters grouped by group name
    expected_grouped_formatters = {
        'Group 1': [formatters[0], formatters[1]],
        'Group 2': [formatters[2], formatters[3]],
        'Without group': [formatters[4]]
    }

    # check dictionary keys, values
    assert all(isinstance(key, str) for key in groups.keys())    # check all keys are strings
   

# Generated at 2022-06-13 22:34:22.564682
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie import ExitStatus
    pm = PluginManager()
    assert ExitStatus.PLUGIN_ERROR not in ([1,2,3,4])

# Generated at 2022-06-13 22:34:29.957219
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from unittest.mock import Mock
    a = Mock()
    a.group_name = "group1"
    b = Mock()
    b.group_name = "group2"
    c = Mock()
    c.group_name = "group1"
    d = Mock()
    d.group_name = "group3"
    l = PluginManager()
    l.register(a,b,c,d)
    assert l.get_formatters_grouped() == {"group1": [a,c], "group2":[b], "group3":[d]}

# Generated at 2022-06-13 22:34:37.385057
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(AuthPlugin)
    pm.register(AuthPlugin)
    pm.register(ConverterPlugin)
    pm.register(ConverterPlugin)
    assert len(pm.filter()) == 4
    assert len(pm.filter(AuthPlugin)) == 2
    assert len(pm.filter(ConverterPlugin)) == 2
    assert len(pm.filter(BasePlugin)) == 4
    assert len(pm.filter(TransportPlugin)) == 0

# Generated at 2022-06-13 22:34:41.916979
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()


# Unit tests for methods get_auth_plugins, get_auth_plugin_mapping and get_auth_plugin of class PluginManager

# Generated at 2022-06-13 22:34:48.472436
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(
        'plugins.httpie.plugins.formatter.v1.XmlFormatterPlugin',
        'plugins.httpie.plugins.formatter.v1.JsonFormatterPlugin',
        'plugins.httpie.plugins.formatter.v1.PrettyJsonFormatterPlugin'
    )
    assert pm.get_formatters_grouped() == {
        'json': ['plugins.httpie.plugins.formatter.v1.JsonFormatterPlugin',
                 'plugins.httpie.plugins.formatter.v1.PrettyJsonFormatterPlugin'],
        'xml': ['plugins.httpie.plugins.formatter.v1.XmlFormatterPlugin']
    }



# Generated at 2022-06-13 22:34:50.177918
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mgr = PluginManager()
    mgr.load_installed_plugins()

# Generated at 2022-06-13 22:35:03.121853
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = [
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin()
    ]
    formatters[0].group_name = "A"
    formatters[1].group_name = "A"
    formatters[2].group_name = "B"
    formatters[3].group_name = "B"
    formatters[4].group_name = "B"
    formatters[5].group_name = "C"
    formatters[6].group_name = "C"
    manager = PluginManager()
    for formatter in formatters:
        manager.register(formatter)
    grouped_formatters = manager.get_formatters_grouped()

# Generated at 2022-06-13 22:35:13.626417
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    font_file_path = '/Library/Fonts/Arial.ttf'
    manager.load_installed_plugins()
    
    assert 'httpie.plugins.auth.v1' in ENTRY_POINT_NAMES
    assert 'httpie.plugins.formatter.v1' in ENTRY_POINT_NAMES
    assert 'httpie.plugins.converter.v1' in ENTRY_POINT_NAMES
    assert 'httpie.plugins.transport.v1' in ENTRY_POINT_NAMES



# Generated at 2022-06-13 22:35:18.667724
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert list(iter_entry_points('httpie.plugins.auth.v1'))
    assert list(iter_entry_points('httpie.plugins.formatter.v1'))
    assert list(iter_entry_points('httpie.plugins.converter.v1'))
    assert list(iter_entry_points('httpie.plugins.transport.v1'))
    plugins_manager = PluginManager()
    plugins_manager.load_installed_plugins()
    assert plugins_manager.get_auth_plugin_mapping()
    assert plugins_manager.get_formatters()
    assert plugins_manager.get_converters()
    assert plugins_manager.get_transport_plugins()

# Generated at 2022-06-13 22:35:21.627831
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:35:35.786915
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONPrettyFormatterPlugin
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.builtin import FormURLEncodedFormatterPlugin
    from httpie.plugins.builtin import HTMLFormatterPlugin
    from httpie.plugins.builtin import RawJSONFormatterPlugin
    from httpie.plugins.builtin import PrettyJsonFormatterPlugin
    from httpie.plugins.builtin import LineFormatterPlugin
    from httpie.plugins.builtin import LinePrettyFormatterPlugin
    from httpie.plugins.builtin import TableFormatterPlugin
    from httpie.plugins.builtin import TablePrettyFormatterPlugin
    
    plugin_manager = PluginManager()

# Generated at 2022-06-13 22:35:38.927369
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth
    p = PluginManager()
    print(p)
    p.load_installed_plugins()
    auth_plugins = p.get_auth_plugins()
    assert HTTPBasicAuth in auth_plugins

# Generated at 2022-06-13 22:35:42.126434
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_mgr = PluginManager()
    plugin_mgr.load_installed_plugins()

    assert any(plugin_mgr)

# Generated at 2022-06-13 22:35:44.955360
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    p = PluginManager()
    assert p.filter(by_type=Type[AuthPlugin]) == []



# Generated at 2022-06-13 22:35:58.309572
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import BuiltinPlugin, BuiltinConfigurePlugin
    from httpie.plugins.colors import ColorsPlugin
    import httpie.plugins
    # Instantiating plugin_manager
    plugin_manager = PluginManager()
    # Registering plugins
    plugin_manager.register(httpie.plugins.builtin.BuiltinPlugin)
    plugin_manager.register(httpie.plugins.builtin.BuiltinConfigurePlugin)
    plugin_manager.register(httpie.plugins.colors.ColorsPlugin)
    # Calling method
    res = plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:36:01.890950
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class P(object): pass
    manager = PluginManager()
    manager.register(P)
    result = manager.filter()
    assert result == [P]


# Generated at 2022-06-13 22:36:06.545323
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Foo:
        pass

    class Bar:
        pass

    class Baz(Foo):
        pass

    manager = PluginManager()
    manager.register(Foo, Bar, Baz, Foo, Bar)

    assert set(manager.filter(Foo)) == {Foo, Baz}



# Generated at 2022-06-13 22:36:14.898868
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    from pkg_resources import iter_entry_points

    class Colorful(FormatterPlugin):
        group_name = 'colorful'

    class Pretty(FormatterPlugin):
        group_name = 'pretty'

    class Ugly(FormatterPlugin):
        group_name = 'ugly'

    class Foo(FormatterPlugin):
        group_name = 'foo'

    class Bar(FormatterPlugin):
        group_name = 'bar'

    # mock each entry point of group httpie.plugins.formatter.v1
    entry_points = []
    entry_points.append(EntryPoint('httpie.plugins.formatter.v1', 'colorful',
                                   Colorful))

# Generated at 2022-06-13 22:36:18.159112
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    m = PluginManager()
    m.load_installed_plugins()
    assert m


pm = PluginManager()
pm.load_installed_plugins()

# Generated at 2022-06-13 22:36:22.699457
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert pm.get_auth_plugins() != []
    assert pm.get_formatters_grouped() != {}
    assert pm.get_converters() != []
    assert pm.get_transport_plugins() != []

# Generated at 2022-06-13 22:36:33.349838
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    #print(pm)
    print(pm.get_auth_plugins())
    print(pm.get_formatters())
    print(pm.get_formatters_grouped())
    print(pm.get_converters())
    print(pm.get_transport_plugins())
    print(pm.get_auth_plugin_mapping())
    print(pm.get_auth_plugin('basic'))



# Generated at 2022-06-13 22:36:37.255741
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    from httpie.plugins.builtin import BuiltinFormatterPlugin, BuiltinConverterPlugin

    manager = PluginManager()
    manager.register(BuiltinFormatterPlugin, BuiltinConverterPlugin)
    print(manager)

    print(manager.get_formatters_grouped())

if __name__ == '__main__':
    test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:36:41.324437
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    expected = {
        None: [],
        'groupA': [],
        'groupB': [],
        'groupC': []
    }
    assert manager.get_formatters_grouped() == expected

# Generated at 2022-06-13 22:36:49.298577
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import pytest
    from httpie.output.formatters.json import JsonFormatter
    from httpie.output.formatters.json import JsonLinesFormatter
    from httpie.output.formatters.json import JsonLinesStreamFormatter
    from httpie.output.formatters.json import JsonStreamFormatter

    manager = PluginManager()
    manager.register(JsonFormatter, JsonLinesFormatter,
                     JsonStreamFormatter, JsonLinesStreamFormatter)
    assert list(manager.get_formatters_grouped().keys()) == ['json']
    assert all(isinstance(plugin, JsonFormatter)
               for plugin in manager.get_formatters_grouped()['json'])

# Generated at 2022-06-13 22:36:56.435409
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.append(TransportPlugin)
    manager.append(FormatterPlugin)
    current_manager = manager.filter(TransportPlugin)
    assert current_manager == [TransportPlugin],\
        'Unit test for method filter of class PluginManager failed'


plugin_manager = PluginManager()



# Generated at 2022-06-13 22:37:09.947612
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(type('none', (Plugin,), {'group_name': 'g1'}))
    plugin_manager.register(type('none', (Plugin,), {'group_name': 'g2'}))
    plugin_manager.register(type('none', (Plugin,), {'group_name': 'g1'}))
    plugin_manager.register(type('none', (Plugin,), {'group_name': 'g2'}))

# Generated at 2022-06-13 22:37:14.881614
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    a_list = [1, 2, 3]
    print(a_list)
    print(list(groupby(a_list)))
    print({key: list(group) for key, group in groupby(a_list)})

# Generated at 2022-06-13 22:37:17.102528
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    _plugin_manager = PluginManager()
    _plugin_manager.register()

# Generated at 2022-06-13 22:37:28.835701
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    '''
    Test method filter of class PluginManager
    '''
    pluginManager = PluginManager()

    class PluginOne(BasePlugin):
        '''
        Test class PluginOne. This class inherits from BasePlugin
        '''
        pass

    class PluginTwo(BasePlugin):
        '''
        Test class PluginTwo. This class inherits from BasePlugin
        '''
        pass

    class PluginThree(BasePlugin):
        '''
        Test class PluginThree. This class inherits from BasePlugin
        '''
        pass

    pluginManager.register(PluginOne, PluginTwo, PluginThree)
    assert pluginManager.filter() == [PluginOne, PluginTwo, PluginThree]
    assert pluginManager.filter(by_type=PluginOne) == [PluginOne]

# Generated at 2022-06-13 22:37:35.176097
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Foo:
        pass

    class Bar(Foo):
        pass

    class Qux(Foo):
        pass

    manager = PluginManager()
    manager.register(Foo, Bar, Qux)
    manager.filter(Foo) == [Foo, Bar, Qux]
    manager.filter(Bar) == [Bar]

# Generated at 2022-06-13 22:37:52.185822
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager)
    print('auth', plugin_manager.get_auth_plugin_mapping())
    print(plugin_manager.get_auth_plugin('basic'))
    print(plugin_manager.get_converters())
    print(plugin_manager.get_formatters())
    print(plugin_manager.get_formatters_grouped())
    print(plugin_manager.get_transport_plugins())



# Generated at 2022-06-13 22:37:57.459149
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    def create_plugin_class():
        class Plugin(BasePlugin):
            ...

        return Plugin

    class A(create_plugin_class()):
        ...

    class B(create_plugin_class()):
        ...

    class C(create_plugin_class()):
        ...

    class D(A):
        ...

    manager = PluginManager()
    manager.register(A, B, C, D)
    assert manager.filter(create_plugin_class()) == [A, B, C, D]
    assert manager.filter(A) == [A, D]

# Generated at 2022-06-13 22:38:04.884784
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    formatters = pm.get_formatters_grouped()
    assert isinstance(formatters, dict)
    assert formatters["Default"] == []
    assert formatters["Debug"] == []
    assert formatters["Input"] == []
    assert formatters["JSON"] == []
    assert formatters["Output"] == []
    assert formatters["Visual"] == []
    assert formatters["Progress"] == []

# Generated at 2022-06-13 22:38:15.601323
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    ''' Test function for method get_formatters_grouped of class PluginManager.
    '''
    pm = PluginManager()
    pm.load_installed_plugins()
    print(pm.get_formatters_grouped())

# Generated at 2022-06-13 22:38:22.819344
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
  # Create an PluginManager object
  plugin_manager = PluginManager()
  
  # Call method load_installed_plugins of class PluginManager
  plugin_manager.load_installed_plugins()
  
  # Check the result
  assert plugin_manager.get_auth_plugins() != []
  assert plugin_manager.get_formatters() != []
  assert plugin_manager.get_converters() != []

# Generated at 2022-06-13 22:38:33.895418
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_list: List[Type[FormatterPlugin]] = plugin_manager.get_formatters()
    assert len(plugin_list) == 5
    formatters_grouped: Dict[str, List[Type[FormatterPlugin]]] = plugin_manager.get_formatters_grouped()
    assert len(formatters_grouped) == 3
    assert 'basic' in formatters_grouped.keys()
    assert len(formatters_grouped['basic']) == 2
    assert 'others' in formatters_grouped.keys()
    assert len(formatters_grouped['others']) == 2
    assert 'related' in formatters_grouped.keys()
    assert len(formatters_grouped['related']) == 1

plugin_manager = PluginManager()

# Generated at 2022-06-13 22:38:36.465133
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(Type[BasePlugin])
    assert plugin_manager.filter() == plugin_manager

# Generated at 2022-06-13 22:38:44.206779
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()

# Generated at 2022-06-13 22:38:58.101760
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.auth.basic import BasicAuthPlugin
    from httpie.plugins.auth.digest import DigestAuthPlugin
    from httpie.plugins.auth.oauth2 import OAuth2Plugin, OAuth2ImplicitPlugin, OAuth2PasswordPlugin
    # Instances are created because they are required in the get_auth_plugin_mapping method
    plugin_instance = PluginManager()
    plugin_instance.register(BasicAuthPlugin)
    plugin_instance.register(DigestAuthPlugin)
    plugin_instance.register(OAuth2Plugin)
    plugin_instance.register(OAuth2ImplicitPlugin)
    plugin_instance.register(OAuth2PasswordPlugin)
    # Obtained value from the get_auth_plugin_mapping method
    auth_plugin_mapping = plugin_instance.get_auth_plugin_mapping()


# Generated at 2022-06-13 22:39:04.788139
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A():
        pass
    class B(A):
        pass
    class C(A):
        pass
    class X():
        pass

    pm = PluginManager()
    pm.register(A, B, C, X)
    pm_filter = pm.filter(A)
    assert set(pm_filter) == {A, B, C}
    assert not set(pm_filter).issubset(set(pm))


plugins = PluginManager()

plugins.load_installed_plugins()

# Generated at 2022-06-13 22:39:39.249608
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    import json
    import os
    from httpie.plugins import AuthPlugin, TransportPlugin
    from httpie.plugins.base import BasePlugin
    from httpie.utils import URL
    from httpie.client import HTTPieClient
    from httpie.context import Environment, EnvironmentAware
    class MyAuthPlugin(AuthPlugin):
        auth_type = 'my-auth-type'
        def get_auth(self, username, password):
            return self.auth_type, (username, password)
        def get_auth_from_url(self, url, auth_parts):
            type, parts = self.get_auth(auth_parts[0], auth_parts[1])
            return type, parts
    class MyTransportPlugin(TransportPlugin):
        name = 'my-transport-plugin'

# Generated at 2022-06-13 22:39:43.545278
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin)
    assert plugin_manager.get_auth_plugin_mapping() == {'auth-type': AuthPlugin}

# Generated at 2022-06-13 22:39:52.437751
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    p = PluginManager()
    p.register(FormatterPlugin)
    d = p.get_formatters_grouped()

    assert isinstance(d, dict)
    assert not d
    assert len(d) == 0

    test_formatter_plugin_group_name = 'g'

    class TestFormatterPlugin(FormatterPlugin):
        group_name = test_formatter_plugin_group_name

    p.register(TestFormatterPlugin)
    d1 = p.get_formatters_grouped()
    assert d1[test_formatter_plugin_group_name] == [TestFormatterPlugin]

# Generated at 2022-06-13 22:40:00.271517
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class DummyPlugin(BasePlugin):
        pass

    class TestUserAgentDummyPlugin(BasePlugin):
        user_agent = 'Test/1.0 (httpie/1.0)'

    plugin_manager = PluginManager()
    plugin_manager.register(DummyPlugin)

    def iter_entry_points(entry_point_name, *args, **kwargs):
        return iter([
            lambda: TestUserAgentDummyPlugin()
        ])

    plugin_manager.load_installed_plugins = types.MethodType(
        PluginManager.load_installed_plugins,
        plugin_manager
    )
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 2
    assert len(plugin_manager.get_formatters()) == 1

# Generated at 2022-06-13 22:40:02.729426
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    plugin_list = pluginManager.get_auth_plugins()
    assert len(plugin_list) >= 1

# Generated at 2022-06-13 22:40:06.214599
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(FormatterPlugin)
    assert plugins.get_formatters_grouped() == {}

manager = PluginManager()
manager.load_installed_plugins()

# Generated at 2022-06-13 22:40:08.102946
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) != 0



# Generated at 2022-06-13 22:40:09.907839
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert len(plugin_manager) != 0

# Generated at 2022-06-13 22:40:12.681182
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(BasePlugin)
    assert plugin_manager.filter(BasePlugin) == [BasePlugin]


# Generated at 2022-06-13 22:40:22.019523
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPluginManager(PluginManager):
        pass

    manager = TestPluginManager()
    class a1:
        pass
    class a2:
        pass
    class b1(BasePlugin):
        pass
    class b2(BasePlugin):
        pass
    class c1(b1):
        pass
    class c2(b2):
        pass
    manager.register(a1,a2,b1,b2,c1,c2)
    assert all([issubclass(plugin,b1) for plugin in manager.filter(b1)])
    assert all([issubclass(plugin,b2) for plugin in manager.filter(b2)])
    assert all([not issubclass(plugin,b2) for plugin in manager.filter(b1)])

# Generated at 2022-06-13 22:40:55.301667
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin

    manager = PluginManager()
    manager.register(JSONFormatterPlugin)

    assert manager.get_formatters_grouped() == {'JSON': [JSONFormatterPlugin]}

# Generated at 2022-06-13 22:40:59.076204
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_auth_plugin_mapping()


# Generated at 2022-06-13 22:41:01.823130
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_PluginManager = PluginManager()
    test_PluginManager.load_installed_plugins()
    assert isinstance(test_PluginManager.get_formatters_grouped(), dict)

# Generated at 2022-06-13 22:41:07.801711
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plg.register(DummyAuthPlugin)
    plg.register(DummyTransportPlugin)
    plg.register(DummyConverterPlugin)
    plg.register(DummyFormatterPlugin)
    plg.register(DummyBasePlugin)
    assert len(plg.filter()) == 6
    assert len(plg.filter(AuthPlugin)) == 1
    assert len(plg.filter(TransportPlugin)) == 1
    assert len(plg.filter(ConverterPlugin)) == 1
    assert len(plg.filter(FormatterPlugin)) == 1
    assert len(plg.filter(BasePlugin)) == 5


# Generated at 2022-06-13 22:41:14.875435
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Plugin_1(BasePlugin):
        pass
    class Plugin_2(Plugin_1):
        pass
    class Plugin_3(Plugin_1):
        pass
    pm = PluginManager()
    pm.register(Plugin_1, Plugin_2, Plugin_3)
    assert pm.filter() == [Plugin_1, Plugin_2, Plugin_3]
    assert pm.filter(by_type=Plugin_1) == [Plugin_1, Plugin_2, Plugin_3]
    assert pm.filter(by_type=Plugin_2) == [Plugin_2]
    assert pm.filter(by_type=Plugin_3) == [Plugin_3]
    assert pm.filter(by_type=BasePlugin) == [Plugin_1, Plugin_2, Plugin_3]

#  Unit test for method get_auth_plugin_

# Generated at 2022-06-13 22:41:22.375416
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.auth import BasicAuth
    from httpie.plugins.formatter import JsonPointer
    from httpie.plugins.converter import Urlencoded
    from httpie.plugins.transport import Requests

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager[0] is BasicAuth 
    assert plugin_manager[1] is JsonPointer
    assert plugin_manager[2] is Urlencoded
    assert plugin_manager[3] is Requests

# Generated at 2022-06-13 22:41:27.302336
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(DummyFormatterPlugin)
    info = pm.get_formatters_grouped()
    assert isinstance(info, dict)
    assert 'DummyGroup' in info



# Generated at 2022-06-13 22:41:37.120512
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    test_formatters = PluginManager()
    test_formatters.register(Plugin1_test, Plugin2_test, Plugin3_test,
                              Plugin4_test, Plugin5_test, Plugin6_test,
                              Plugin7_test, Plugin8_test, Plugin9_test,
                              Plugin10_test, Plugin11_test, Plugin12_test)
    assert test_formatters.get_formatters_grouped() == {
        'Test Group 1': [Plugin1_test, Plugin2_test, Plugin3_test],
        'Test Group 2': [Plugin5_test, Plugin6_test, Plugin7_test, Plugin8_test],
        'Test Group 3': [Plugin9_test, Plugin10_test, Plugin11_test, Plugin12_test],
    }


# Generated at 2022-06-13 22:41:43.809150
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class BasePlugin:
        pass
    class Plugin1(BasePlugin):
        pass
    class Plugin2(BasePlugin):
        pass
    class Plugin3(BasePlugin):
        pass
    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3)
    assert plugin_manager.filter(by_type = BasePlugin) == [Plugin1, Plugin2, Plugin3]

# Generated at 2022-06-13 22:41:50.862833
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) >= 2
    urllib3 = manager[0]
    assert isinstance(urllib3, TransportPlugin)
    assert urllib3.package_name == 'urllib3'
    assert urllib3.name == 'urllib3'

# Generated at 2022-06-13 22:43:04.899014
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.register() #Because we are using the function register, we need to add this
    pluginManager.load_installed_plugins()
    assert len(pluginManager) >= 1
    for plugin in pluginManager:
        assert True


# Generated at 2022-06-13 22:43:09.102552
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(FormatterPlugin, FormatterPlugin)
    assert len(pm.get_formatters_grouped()) == 1
    assert type(pm.get_formatters_grouped().keys()) == dict_keys
    for i in pm.get_formatters_grouped().keys():
        assert i == 'form'


# Generated at 2022-06-13 22:43:16.796585
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    installed_plugins_manager = PluginManager()
    installed_plugins_manager.load_installed_plugins()
    installed_plugins_manager.register(installed_plugins_manager.get_auth_plugin('Basic'))
    installed_plugins_manager.register(installed_plugins_manager.get_auth_plugin('Digest'))

    list_formatters_grouped = installed_plugins_manager.get_formatters_grouped()

    assert isinstance(list_formatters_grouped, dict)
    assert list_formatters_grouped