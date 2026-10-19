

# Generated at 2022-06-13 22:33:27.276813
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import HTTPieJSONEncoderPlugin
    from httpie.plugins.builtin import JSONPlugin
    from httpie.plugins.builtin import PrettyJsonPlugin
    from httpie.plugins.builtin import StreamFormatterPlugin
    from httpie.plugins.builtin import TracebackFormatterPlugin
    from httpie.plugins.builtin import UnicodeJSONEncoderPlugin
    plugins = PluginManager()
    plugins.register(HTTPieJSONEncoderPlugin)
    plugins.register(JSONPlugin)
    plugins.register(PrettyJsonPlugin)
    plugins.register(StreamFormatterPlugin)
    plugins.register(TracebackFormatterPlugin)
    plugins.register(UnicodeJSONEncoderPlugin)

# Generated at 2022-06-13 22:33:37.235241
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    p = PluginManager()
    p.register('httpie.plugins.formatter.colors.ColorsPlugin',
               'httpie.plugins.formatter.json.JSONPlugin',
               'httpie.plugins.formatter.json.JSONStreamPlugin',
               'httpie.plugins.formatter.jsonlines.JSONLinesPlugin',
               'httpie.plugins.formatter.jsonlines.JSONLinesStreamPlugin',
               'httpie.plugins.formatter.table.TablePlugin',
               'httpie.plugins.formatter.template.TemplatePlugin',
               'httpie.plugins.formatter.template.TemplateStreamPlugin')
    f = p.get_formatters_grouped()

# Generated at 2022-06-13 22:33:44.691772
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    import httpie
    plugins = (
        httpie.plugins.TransportPlugin,
        httpie.plugins.FormatterPlugin,
        httpie.plugins.FormatPlugin,
        httpie.plugins.AuthPlugin,
        httpie.plugins.ConverterPlugin,
        httpie.plugins.ConverterPlugin,
        httpie.plugins.ConverterPlugin,
    )
    pm = PluginManager()
    pm.register(*plugins)
    print(pm.filter(ConverterPlugin))
    print(pm.filter(TransportPlugin))


# Generated at 2022-06-13 22:33:49.525348
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 1


if __name__ == "__main__":
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:33:54.988743
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(FormatterPlugin)
    assert plugin_manager.get_formatters_grouped() == {'group_name': [FormatterPlugin, FormatterPlugin]}


# Generated at 2022-06-13 22:34:03.781587
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class PluginA(BasePlugin):
        pass
    class PluginB(BasePlugin):
        pass
    class PluginC(PluginA):
        pass

    class PluginD(PluginA):
        pass

    pm = PluginManager()
    pm.register(
        PluginA, PluginB, PluginC
    )

    assert [p.__name__ for p in pm.filter(by_type=PluginA)] == ['PluginA', 'PluginC']
    assert [p.__name__ for p in pm.filter(by_type=PluginB)] == ['PluginB']

# Generated at 2022-06-13 22:34:17.616540
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.register(AwsAuthPlugin)
    manager.register(GssApiAuthPlugin)
    manager.register(HawkAuthPlugin)
    manager.register(HttpAuthPlugin)
    manager.register(NetrcAuthPlugin)
    manager.register(OAuth1AuthPlugin)
    manager.register(OAuth2AuthPlugin)

    mapping = manager.get_auth_plugin_mapping()
    assert mapping['aws'] == AwsAuthPlugin
    assert mapping['gssapi'] == GssApiAuthPlugin
    assert mapping['hawk'] == HawkAuthPlugin
    assert mapping['http'] == HttpAuthPlugin
    assert mapping['netrc'] == NetrcAuthPlugin
    assert mapping['oauth1'] == OAuth1AuthPlugin
    assert mapping['oauth2'] == OAuth2AuthPlugin



# Generated at 2022-06-13 22:34:22.671018
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = get_formatters()
    for group_key, group in formatters.items():
        for formatter in group:
            assert formatter.group_name == group_key
            with pytest.raises(AttributeError):
                formatter.group_name == None


# Generated at 2022-06-13 22:34:33.195974
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import httpie
    from httpie import plugins
    from httpie.plugins import auth, converter, formatter, transport

    pm = PluginManager()
    pm.load_installed_plugins()

    # The load_installed_plugins() method is essentially a wrapper around `iter_entry_points()`.
    # We check here if the loaded plugins are actually in the entry-points.
    # However the entry-points discovery is really tied to pkg_resources,
    # so we can only check the plugin name here.
    names = [
        plugin.__name__
        for plugin in pm
    ]

    assert 'HTTPBasicAuth' in names
    assert 'HTTPDigestAuth' in names
    assert 'Converter' in names
    assert 'JSONConverter' in names
    assert 'JSONPointer' in names

# Generated at 2022-06-13 22:34:40.849081
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins import auth
    from httpie.plugins import formatter
    from httpie.plugins import converter
    from httpie.plugins import transport
    plugin_manager = PluginManager()

# Generated at 2022-06-13 22:34:49.355476
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    import string
    import random
    import tempfile
    import pkg_resources
    dist = pkg_resources.Distribution(tempfile.mkdtemp())
    prefix = 'httpie_plugin_'
    for i in range(0, 3):
        class_name = prefix + ''.join(random.choices(string.ascii_uppercase, k = random.randint(3,10)))
        def __init__(self):
            pass
        locals()[class_name] = type(class_name, (object,),{ "__init__" : __init__})
        pkg_resources.EntryPoint.parse(f'dummy.plugin={class_name}:__init__', dist=dist).load(require=False)
    pm = PluginManager()
    pm.load_installed_plugins()

# Generated at 2022-06-13 22:34:54.030665
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import BuiltinFormatter
    plugin_manager = PluginManager()
    plugin_manager.register(BuiltinFormatter)
    assert plugin_manager.get_formatters_grouped() == {'builtin': [BuiltinFormatter]}

# Generated at 2022-06-13 22:35:03.865722
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Plugin1(BasePlugin): pass
    class Plugin2(BasePlugin): pass
    class Plugin3(BasePlugin): pass
    class Plugin4(BasePlugin): pass
    class Plugin5(BasePlugin): pass
    class Plugin6(Plugin2): pass

    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3, Plugin4, Plugin5, Plugin6)

    assert len(plugin_manager.filter(Plugin1)) == 1
    assert len(plugin_manager.filter(Plugin2)) == 2
    assert len(plugin_manager.filter(BasePlugin)) == 6



# Generated at 2022-06-13 22:35:08.353358
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()


if __name__ == '__main__':
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:35:20.583377
# Unit test for method get_formatters_grouped of class PluginManager

# Generated at 2022-06-13 22:35:24.632881
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    pm.filter(type)
    assert len(pm.filter(type)) > 0


# Generated at 2022-06-13 22:35:28.028333
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    adict = pm.get_formatters_grouped()
    assert isinstance(adict, dict)
    
    

# Generated at 2022-06-13 22:35:36.478537
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    """
    Verify that the method PluginManager.get_auth_plugin_mapping() returns a dictionary in which each item contains
    a plugin's auth_type as the key and the plugin object as the value.
    """
    string = "Test Plugin"
    pluginType = type(string, (AuthPlugin, object), {"auth_type": "test", "get_auth": lambda *args, **kwargs: "basic"})
    manager = PluginManager()
    manager.register(pluginType)
    auth_plugin_mapping = manager.get_auth_plugin_mapping()
    assert len(auth_plugin_mapping) == 1
    assert "test" in auth_plugin_mapping

# Generated at 2022-06-13 22:35:46.114794
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.base import BasePlugin

    class A(BasePlugin): pass
    class B(A): pass
    class C(B): pass
    class D(A): pass

    pm = PluginManager()
    pm.register(A, B, C, D)

    assert pm.filter() == [A, B, C, D]
    assert pm.filter(A) == [A, B, C, D]
    assert pm.filter(B) == [B, C]
    assert pm.filter(C) == [C]


# Generated at 2022-06-13 22:35:58.765698
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # Input to the method
    p = PluginManager()
    print('test_PluginManager_get_auth_plugin_mapping')
    # Expected output of the method

# Generated at 2022-06-13 22:36:09.430736
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    class Class1(BasePlugin):
        pass
    class Class2(BasePlugin):
        pass
    class Class3(BasePlugin):
        pass
    plugins.register(Class1, Class2, Class3)
    assert plugins.filter() == [Class1, Class2, Class3]
    assert plugins.filter(BasePlugin) == [Class1, Class2, Class3]
    assert plugins.filter(Class1) == [Class1]
    assert plugins.filter(Class2) == [Class2]
    assert plugins.filter(Class3) == [Class3]
    plugins.unregister(Class3)
    assert plugins.filter() == [Class1, Class2]
    assert plugins.filter(Class3) == []



# Generated at 2022-06-13 22:36:16.468273
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register()

    assert len(plugins) > 0
    for plugin in plugins:
        print(plugin.auth_type)
        print(plugin.auth_type in plugins.get_auth_plugin_mapping().keys())
        assert plugin.auth_type in plugins.get_auth_plugin_mapping().keys()


# Generated at 2022-06-13 22:36:23.101074
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert pluginManager.get_auth_plugin("basic")
    assert pluginManager.get_auth_plugin("digest")
    assert pluginManager.get_auth_plugin("jwt")
    assert pluginManager.get_formatters()
    assert pluginManager.get_formatters_grouped()
    assert pluginManager.get_converters()
    assert pluginManager.get_transport_plugins()

# Generated at 2022-06-13 22:36:30.465262
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import JSONFormatterPlugin, PrettyFormatterPlugin, CSVFormatterPlugin
    plugin_manager = PluginManager()
    plugin_manager.register(JSONFormatterPlugin)
    plugin_manager.register(PrettyFormatterPlugin)
    plugin_manager.register(CSVFormatterPlugin)
    print(plugin_manager.get_formatters_grouped())
    assert isinstance(plugin_manager.get_formatters_grouped(), dict)



# Generated at 2022-06-13 22:36:31.629407
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter(by_type=FormatterPlugin) == []



# Generated at 2022-06-13 22:36:38.466969
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    class P1(BasePlugin): ...
    class P2(BasePlugin): ...
    class P3(BasePlugin): ...
    class P4(BasePlugin): ...

    class C(ConverterPlugin): ...
    class F(FormatterPlugin): ...
    class A(AuthPlugin): ...
    class T(TransportPlugin): ...

    class H(AuthPlugin): ...
    class I(AuthPlugin): ...
    class J(AuthPlugin): ...

    class X(FormatterPlugin): ...
    class Y(FormatterPlugin): ...
    class Z(FormatterPlugin): ...

    class E(ConverterPlugin): ...
    class R(ConverterPlugin): ...
    class W(ConverterPlugin): ...

    class K(TransportPlugin): ...
    class L(TransportPlugin): ...
    class M(TransportPlugin): ...

# Generated at 2022-06-13 22:36:47.648957
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager() # use a empty PluginManager
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.builtin import PrettyJSONFormatterPlugin
    from httpie.plugins.builtin import XMLFormatterPlugin
    plugins.register(JSONFormatterPlugin, PrettyJSONFormatterPlugin, XMLFormatterPlugin)

# Generated at 2022-06-13 22:36:52.933013
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin, ConverterPlugin, FormatterPlugin)
    assert plugin_manager.filter(AuthPlugin) == [AuthPlugin]
    assert plugin_manager.filter(ConverterPlugin) == [ConverterPlugin]
    assert plugin_manager.filter(FormatterPlugin) == [FormatterPlugin]


if __name__ == '__main__':
    test_PluginManager_filter()

# Generated at 2022-06-13 22:37:08.569439
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    assert pm.filter(by_type=Type[AuthPlugin]) == []
    assert pm.filter(by_type=Type[BasePlugin]) == []

    class A(BasePlugin):
        pass
    class B(BasePlugin):
        pass
    class C(A):
        pass
    class D(B):
        pass
    class E(C):
        pass
    class F(D):
        pass

    pm.register(A, B, C, D, E, F)
    assert pm.filter(by_type=Type[AuthPlugin]) == []
    assert pm.filter(by_type=Type[BasePlugin]) == [A, B, C, D, E, F]
    assert pm.filter(by_type=Type[A]) == [A, C, E]



# Generated at 2022-06-13 22:37:15.153980
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_auth_plugin('basic')
    assert plugin_manager.get_formatters()
    assert plugin_manager.get_converters()
    assert plugin_manager.get_transport_plugins()


# Generated at 2022-06-13 22:37:21.009683
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class testplugin(BasePlugin):
        pass
    
    plugins = PluginManager()
    plugins.load_installed_plugins()
    plugins.register(testplugin)
    assert testplugin in plugins



# Generated at 2022-06-13 22:37:22.893371
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    s = pm.register()
    assert s == pm

# Generated at 2022-06-13 22:37:28.962086
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.append(FormatterPlugin)
    plugin_manager.append(FormatterPlugin)
    plugin_manager.append(FormatterPlugin)
    result = plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:37:32.296216
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0



# Generated at 2022-06-13 22:37:34.029647
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins

# Generated at 2022-06-13 22:37:37.173059
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pManager = PluginManager()
    pManager.register(1, 2, 3, 4, 5)
    assert pManager.get_formatters_grouped() == {'html': [3, 4, 5], 'json': [1, 2]}

# Generated at 2022-06-13 22:37:41.744851
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.load_installed_plugins()
    auth_plugin_mapping = manager.get_auth_plugin_mapping()
    expected_key = 'basic'
    expected_value = 'httpie_jwt_auth.JWTAuthPlugin'
    assert auth_plugin_mapping[expected_key] == expected_value

# Generated at 2022-06-13 22:37:47.580273
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pining = PluginManager()
    pining.register(PiningPlugin)
    pining.load_installed_plugins()
    grouped_formatters = pining.get_formatters_grouped()
    assert 'Pining' in grouped_formatters.keys()
    assert len(grouped_formatters['Pining']) == 1

# Generated at 2022-06-13 22:37:50.447238
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.register(FakeAuthPlugin)
    mapping = manager.get_auth_plugin_mapping()
    assert mapping['fake'] == FakeAuthPlugin


# Generated at 2022-06-13 22:37:52.130346
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins, "plugins is not empty"

# Generated at 2022-06-13 22:37:59.479040
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm=PluginManager()
    pm.load_installed_plugins()
    assert len(pm)>0

# Generated at 2022-06-13 22:38:09.007771
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    testing_pluginmanager = PluginManager()
    testing_pluginmanager.register(MockFormatterPlugin_1)
    testing_pluginmanager.register(MockFormatterPlugin_2)
    testing_pluginmanager.register(MockFormatterPlugin_3)
    testing_pluginmanager.register(MockFormatterPlugin_4)
    assert testing_pluginmanager.get_formatters_grouped() == {"group_1" : [MockFormatterPlugin_1, MockFormatterPlugin_2], "group_2" : [MockFormatterPlugin_3, MockFormatterPlugin_4]}

# Generated at 2022-06-13 22:38:12.838748
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(
        FakeFormatterPlugin0,
        FakeFormatterPlugin0,
        FakeFormatterPlugin1,
        FakeFormatterPlugin2
    )

    assert plugin_manager.get_formatters_grouped() == {
        'group0': [FakeFormatterPlugin0, FakeFormatterPlugin0],
        'group1': [FakeFormatterPlugin1],
        'group2': [FakeFormatterPlugin2],
    }



# Generated at 2022-06-13 22:38:14.534383
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 4


# Generated at 2022-06-13 22:38:26.324439
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.formatter import FormatterPlugin
    from httpie.plugins.builtin import (
        JSONFormatterPlugin,
        PrettyJSONFormatterPlugin,
        PrettyURLEncodedFormatterPlugin,
        RawJSONFormatterPlugin,
        URLEncodedFormatterPlugin,
    )

    def create_plugin_mock(group_name: str) -> Type[FormatterPlugin]:
        plugin = Mock(FormatterPlugin)
        plugin.group_name = group_name
        return plugin

    manager = PluginManager()
    manager.load_installed_plugins()

# Generated at 2022-06-13 22:38:37.229396
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from plugins.gssapi_auth import GssapiAuthPlugin
    from plugins.jwt_auth import JWTAuthPlugin
    from plugins.hawk_auth import HawkAuthPlugin
    from plugins.ocid_auth import OCIDAuthPlugin
    # create PluginManager instance
    pm = PluginManager()
    # register plugins
    pm.register(GssapiAuthPlugin, JWTAuthPlugin, HawkAuthPlugin, OCIDAuthPlugin)
    # test method get_auth_plugin_mapping
    assert pm.get_auth_plugin_mapping() == {'gssapi_auth': GssapiAuthPlugin, 'jwt_auth': JWTAuthPlugin,
                                            'hawk_auth': HawkAuthPlugin, 'ocid_auth': OCIDAuthPlugin}
test_PluginManager_get_auth_plugin_mapping()

plugin_

# Generated at 2022-06-13 22:38:42.769184
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugins = [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]
    plugin_manager.register(*plugins)
    assert plugin_manager.filter(AuthPlugin) == [AuthPlugin]
    assert plugin_manager.filter(FormatterPlugin) == [FormatterPlugin]
    assert plugin_manager.filter(TransportPlugin) == [TransportPlugin]

# Generated at 2022-06-13 22:38:49.813118
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import json
    import pytest
    from httpie.compat import is_windows
    from httpie.plugins import AttributedDict
    from httpie.output.formatters.colors import ColorScheme
    from httpie.output.formatters.colors import Linux, NoColor, Windows

    class JsonTestCase(AttributedDict):
        expected_output = None

        def __init__(self, data, **kwargs):
            super().__init__(data, **kwargs)
            self.expected_output = self.expected_output.replace('\n', '')

    class TestColorScheme(ColorScheme):
        NAME = 'test'
        TEST = '42'


# Generated at 2022-06-13 22:38:54.870546
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(FormatterPlugin)
    pm.register(ConverterPlugin)
    assert isinstance(pm.filter(FormatterPlugin), list)
    assert isinstance(pm.filter(ConverterPlugin), list)


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:39:00.502790
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    """
    This test case confirms the working of the filter method of the class PluginManager
    """
    from httpie.plugins import AuthPlugin, FormatterPlugin, ConverterPlugin
    test = PluginManager()
    test.register(AuthPlugin)
    test.register(FormatterPlugin)
    test.register(ConverterPlugin)
    ret = test.filter(AuthPlugin)
    assert isinstance(ret, list)

# Generated at 2022-06-13 22:39:15.832333
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class FormatterPlugin1(FormatterPlugin):
        group_name = "Group1"
    class FormatterPlugin2(FormatterPlugin):
        group_name = "Group2"
    class FormatterPlugin3(FormatterPlugin):
        group_name = "Group2"
    class FormatterPlugin4(FormatterPlugin):
        group_name = "Group1"
    pm = PluginManager()
    pm.register(FormatterPlugin1, FormatterPlugin2, FormatterPlugin3, FormatterPlugin4)
    assert pm.get_formatters_grouped() == {'Group1': [FormatterPlugin1, FormatterPlugin4], 'Group2': [FormatterPlugin2, FormatterPlugin3]}

pm = PluginManager()
pm.load_installed_plugins()

# Generated at 2022-06-13 22:39:25.713190
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    def test(by_type=Type[BasePlugin]):
        return [plugin for plugin in pm if issubclass(plugin, by_type)]

    pm.register(AuthPlugin, FormatterPlugin, ConverterPlugin)
    assert pm.filter() == [AuthPlugin, FormatterPlugin, ConverterPlugin]
    assert pm.filter(AuthPlugin) == [AuthPlugin]
    assert pm.filter(FormatterPlugin) == [FormatterPlugin]
    assert pm.filter(ConverterPlugin) == [ConverterPlugin]
    assert pm.filter(list) == []

# Generated at 2022-06-13 22:39:28.682925
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
	pluginmanager = PluginManager()
	pluginmanager.load_installed_plugins()
	print(pluginmanager.get_auth_plugin_mapping())


if __name__ == '__main__':
	test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:39:33.634809
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pluginManager = PluginManager()
    pluginManager.register(Plugin1)
    pluginManager.register(Plugin2)
    assert pluginManager.get_auth_plugin_mapping() == {'plugin1': Plugin1, 'plugin2': Plugin2}


# Generated at 2022-06-13 22:39:35.975037
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
	plugin_manager = PluginManager()
	plugin_manager.load_installed_plugins()
	print(plugin_manager)
	assert plugin_manager != []

# Generated at 2022-06-13 22:39:51.226784
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class MockEntryPoint:
        def __init__(self, plugin):
            self.plugin = plugin
            class MockDist:
                key = 'pkg-name'
            self.dist = MockDist()
        def load(self):
            return self.plugin
    class MockPluginManager:
        def __init__(self, plugin):
            self.plugin = plugin
        def append(self, plugin):
            assert self.plugin == plugin
        def iter_entry_points(self, entry_point_name):
            assert entry_point_name == 'httpie.plugins.auth.v1'
            yield MockEntryPoint(self.plugin)
    class MockPlugin:
        auth_type = 'test'
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins = MockPluginManager(MockPlugin).load_installed_

# Generated at 2022-06-13 22:39:59.909187
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    class FakeEntryPoint:
        def __init__(self, name: str, load: Type[BasePlugin]):
            self.name = name
            self.load = load
        def load(self):
            return self.load()
        def dist(self):
            return type('', (object,), {'key': 'httpie-' + self.name})
    class FakeEntryPointGroup:
        def __init__(self, entry_points):
            self.entry_points = entry_points
        def __iter__(self):
            return iter(self.entry_points)
    def fake_iter_entry_points(name: str):
        return FakeEntryPointGroup([
            FakeEntryPoint(name.split('.')[-1], plugin)
            for plugin in PluginManager().filter(eval(name))
        ])

    original_

# Generated at 2022-06-13 22:40:07.133131
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from .plugins import FormatterPlugin

    grab_group_name = lambda f: f.group_name
    formatter_plugins = [
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin(),
        FormatterPlugin()
    ]
    # set the group_names
    formatter_plugins[0].group_name = 'test'
    formatter_plugins[1].group_name = 'test'
    formatter_plugins[2].group_name = 'abc'
    formatter_plugins[3].group_name = 'abc'
    formatter_plugins[4].group_name = 'abc'
    formatter_plugins[5].group_name = 'def'
    formatter_plugins[6].group_name = 'def'

   

# Generated at 2022-06-13 22:40:14.453828
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(AuthPlugin, AuthPlugin)
    assert isinstance(pm.filter(AuthPlugin), list)  # should be list
    assert len(pm.filter(AuthPlugin)) == 2
    assert isinstance(pm.filter(AuthPlugin)[0], type)  # should be class type
    assert issubclass(pm.filter(AuthPlugin)[0], AuthPlugin)


if __name__ == '__main__':
    test_PluginManager_filter()

# Generated at 2022-06-13 22:40:20.605655
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Formatter1(FormatterPlugin):
        name = 'formatter1'
    class Formatter2(FormatterPlugin):
        name = 'formatter2'

    pluginManager = PluginManager()
    pluginManager.register(Formatter1, Formatter2)
    assert len(pluginManager.filter(FormatterPlugin)) == 2
    assert len(pluginManager.filter(FormatterPlugin)) == 2
    assert len(pluginManager.filter(FormatterPlugin)) == 2



# Generated at 2022-06-13 22:40:40.638594
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mypluginmanager = PluginManager()
    assert mypluginmanager.load_installed_plugins() == True


# Generated at 2022-06-13 22:40:44.965554
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from pkg_resources import iter_entry_points
    from httpie.plugins.formatter import FormatterPlugin

    pm = PluginManager()
    pm.register(iter_entry_points('httpie.plugins.formatter.v1').__next__().load())
    assert isinstance(pm.get_formatters_grouped()['All'][0], FormatterPlugin)

# Generated at 2022-06-13 22:40:50.319771
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.input import KeyValue
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPTokenAuth
    from httpie.plugins.builtin import HTTPBearerAuth
    from httpie.plugins.builtin.colors import ColoredFormatter
    from httpie.plugins.builtin.format import JSONFormatter
    from httpie.plugins.builtin.format import JSONPrettyFormatter
    from httpie.plugins.builtin.format import RawJSONFormatter
    from httpie.plugins.builtin.format import JSONLinesFormatter
    from httpie.plugins.builtin.format import UrlFormatter
    from httpie.plugins.builtin.format import FormFormatter
    from httpie.plugins.builtin.format import PrettyJsonFormatter

# Generated at 2022-06-13 22:40:52.512513
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()



# Generated at 2022-06-13 22:40:55.222786
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.get_auth_plugins()
    assert manager.get_formatters()
    assert manager.get_converters()



# Generated at 2022-06-13 22:40:58.450520
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    expected = {
        'group_name': list
    }
    assert expected == PluginManager.get_formatters_grouped()

# Generated at 2022-06-13 22:41:04.515514
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    p = PluginManager()
    p.register(FormatterPlugin)
    formatters_grouped = p.get_formatters_grouped()
    assert isinstance(formatters_grouped, dict)
    assert list(formatters_grouped.keys()) == [FormatterPlugin.group_name]
    actual = next(iter(formatters_grouped.values()))
    expected = [FormatterPlugin]
    assert actual == expected

# Generated at 2022-06-13 22:41:09.067016
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    assert len(plugins.get_auth_plugin_mapping()) == 0

    plugins.load_installed_plugins()
    assert len(plugins.get_auth_plugin_mapping()) > 0


# Generated at 2022-06-13 22:41:20.811923
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager_adapter = PluginManager()
    plugin_manager_adapter.register(TransportPlugin)
    plugin_manager_adapter.register(FormatterPlugin)
    plugin_manager_adapter.register(ConverterPlugin)
    plugin_manager_adapter.register(AuthPlugin)
    assert len(plugin_manager_adapter.filter()) == 4
    assert len(plugin_manager_adapter.filter(ConverterPlugin)) == 1
    assert len(plugin_manager_adapter.filter(FormatterPlugin)) == 1
    assert len(plugin_manager_adapter.filter(TransportPlugin)) == 1
    assert len(plugin_manager_adapter.filter(AuthPlugin)) == 1


# Generated at 2022-06-13 22:41:27.209689
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(AuthPlugin)
    print(pm.filter(AuthPlugin))
    assert pm.filter(AuthPlugin) == [AuthPlugin]
    pm_filter_bool = pm.filter(by_type=Type[AuthPlugin])
    assert pm_filter_bool == [AuthPlugin]

# Generated at 2022-06-13 22:42:02.866095
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    #plugins = plugin_manager.load_installed_plugins()
    plugins = plugin_manager.get_formatters()

    print(plugin_manager.get_formatters_grouped())

# Generated at 2022-06-13 22:42:05.714158
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.register(CustomAuthPlugin)
    assert plugin_manager.get_auth_plugin_mapping().keys() == {'custom'}



# Generated at 2022-06-13 22:42:08.750656
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    """Method load_installed_plugins of class PluginManager.

    :return: None
    """
    # Load the plugins
    PluginManager().load_installed_plugins()
    assert isinstance(PluginManager(), PluginManager)
    assert len(PluginManager()) > 2



# Generated at 2022-06-13 22:42:21.368769
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:42:32.029324
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    from httpie.plugins.base import BasePlugin
    from httpie.plugins.auth.httpie_auth import BasicAuth

    class AuthPlugin:
        pass

    class FmtPlugin:
        pass

    class CvtPlugin:
        pass

    class TransportPlugin:
        pass

    class Others:
        pass

    class NewAuthPlugin(AuthPlugin, BasePlugin):
        pass

    class NewFormatPlugin(FmtPlugin):
        pass

    class NewConvertPlugin(CvtPlugin):
        pass

    manager.register(Others,
                     NewAuthPlugin, NewFormatPlugin, NewConvertPlugin,
                     TransportPlugin,
                     BasicAuth)

    assert manager.filter(by_type=AuthPlugin) == [NewAuthPlugin]

# Generated at 2022-06-13 22:42:45.657225
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class PluginA(BasePlugin):
        pass

    class PluginB(BasePlugin):
        pass

    class PluginC1(PluginA):
        pass

    class PluginC2(PluginA):
        pass

    class PluginD1(PluginB):
        pass

    class PluginD2(PluginB):
        pass

    class PluginE1(PluginC1):
        pass

    class PluginE2(PluginC2):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(PluginA, PluginB, PluginC1, PluginC2, PluginD1, PluginD2, PluginE1, PluginE2)
    assert len(plugin_manager.filter(BasePlugin)) == 8
    assert len(plugin_manager.filter(PluginA)) == 5
    assert len(plugin_manager.filter(PluginB)) == 3


# Generated at 2022-06-13 22:42:51.572575
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class MyPlugin(BasePlugin):
        pass

    class OtherPlugin(BasePlugin):
        pass

    class SubPlugin(MyPlugin):
        pass

    class TSubPlugin(TransportPlugin):
        pass

    class OtherTSubPlugin(TransportPlugin):
        pass

    class STransportPlugin(TransportPlugin):
        pass

    pm = PluginManager()
    pm.register(MyPlugin, OtherPlugin, SubPlugin, TSubPlugin, OtherTSubPlugin, STransportPlugin)
    assert isinstance(pm.filter(), list)
    assert len(pm.filter()) == 6
    assert isinstance(pm.filter(Type[BasePlugin]), list)
    assert len(pm.filter(Type[BasePlugin])) == 6
    assert isinstance(pm.filter(BasePlugin), list)
    assert len(pm.filter(BasePlugin))

# Generated at 2022-06-13 22:42:54.705860
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register()
    assert plugin_manager.filter()


# Generated at 2022-06-13 22:43:05.486712
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    # Registering the plugins
    plugin_manager.register(AppendAuthPlugin, EchoAuthPlugin)
    plugin_manager.register(JSONFormatterPlugin, LinkFormatterPlugin)
    # Check filter
    assert plugin_manager.filter(AuthPlugin) == [AppendAuthPlugin, EchoAuthPlugin]
    assert plugin_manager.filter(FormatterPlugin) == [JSONFormatterPlugin, LinkFormatterPlugin]


# Generated at 2022-06-13 22:43:07.331513
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins = plugins.filter(ConverterPlugin)
    print(plugins)

# test_PluginManager_filter()