

# Generated at 2022-06-13 22:33:27.373404
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin
    from httpie.plugins import converge
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import TransportPlugin
    pm = PluginManager()
    pm.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)
    pm.register(converge.Converge)
    
    # test plugin
    class AuthPlugin(BasePlugin):
        name = 'unit test plugin'
        auth_type = 'test'
        

    test_plugin = AuthPlugin()
    pm.register(test_plugin)
    assert(pm.filter(AuthPlugin) == [test_plugin])
    assert(pm.filter(ConverterPlugin) == [converge.Converge])

# Generated at 2022-06-13 22:33:30.935757
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager)

    assert plugin_manager.get_formatters()
    assert plugin_manager.get_converters()


if __name__ == "__main__":
    test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:33:33.022387
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    a = PluginManager()
    print(a)



# Generated at 2022-06-13 22:33:44.319489
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    class Base():
        def __init__(self, *response):
            self.response = response

        def foo(self):
            pass

    class A1(Base):
        pass

    class A2(Base):
        pass

    class A3(Base):
        pass

    class A4(Base):
        pass

    class A5(A1):
        pass

    class A6(A2):
        pass

    class A7(A3):
        pass

    class A8(A4):
        pass

    a = PluginManager()

    a.register(A1, A2, A3, A4, A5, A6, A7, A8)

    assert len(a.filter(Base))            == 8
    assert len(a.filter(A1))              == 4

# Generated at 2022-06-13 22:33:53.562993
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    l1 = [Plugin1(), Plugin2(), Plugin3()]
    l2 = [Plugin4(), Plugin5(), Plugin6()]
    l3 = [Plugin7(), Plugin8(), Plugin9()]
    pm.register(*l1)
    pm.register(*l2)
    pm.register(*l3)
    d = {'group1': l1, 'group2': l2, 'group3': l3}
    assert pm.get_formatters_grouped() == d


# Generated at 2022-06-13 22:34:01.168359
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager=PluginManager()
    plugin_manager.register(JSONV1Plugin)
    plugin_manager.register(JSONV2Plugin)
    res=plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:34:12.760278
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():

    plugin_manager = PluginManager()

    # Register auth plugins with different auth_type values
    class AuthTestPlugin_1(AuthPlugin):
        auth_type = 't1'

    class AuthTestPlugin_2(AuthPlugin):
        auth_type = 't2'

    plugin_manager.register(AuthTestPlugin_1, AuthTestPlugin_2)

    # Check that plugin by auth_type is found
    assert plugin_manager.get_auth_plugin('t1') == AuthTestPlugin_1
    assert plugin_manager.get_auth_plugin('t2') == AuthTestPlugin_2

    # Check that exception is thrown when plugin is not found
    with pytest.raises(KeyError):
        plugin_manager.get_auth_plugin('t3')

# Generated at 2022-06-13 22:34:22.293226
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    '''
    Unit test for method get_formatters_grouped of class PluginManager
    :return:
    '''
    pm = PluginManager()
    pm.load_installed_plugins()
    # group by group_name, ex: httpie.plugins.formatter.v1.JsonFormatter: 'html;json'
    # filter httpie.plugins.formatter.v1.JsonFormatter
    print(pm.get_formatters_grouped())
    for k, v in pm.get_formatters_grouped().items():
        print(f'{k}:\n{v}')

# Generated at 2022-06-13 22:34:27.548157
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins.get_formatters()) == 41
    assert len(plugins.get_auth_plugins()) == 5
    assert len(plugins.get_transport_plugins()) == 3
    assert len(plugins.get_converters()) == 1

# Generated at 2022-06-13 22:34:39.247469
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # given
    pluginManager = PluginManager()

    # when
    auth_plugin_mapping = pluginManager.get_auth_plugin_mapping()

    # then
    assert len(auth_plugin_mapping) == 0

    # given
    class AuthPlugin(BasePlugin):
        auth_type = 'test'

        def get_auth(self, auth_username=None, auth_password=None,
                     auth_token=None, auth_api_key=None, auth_jwt=None,
                     auth_0_token=None, auth_1_token=None, auth_2_token=None):
            return auth_username, auth_password, auth_token

    # when
    pluginManager.register(AuthPlugin)
    auth_plugin_mapping = pluginManager.get_auth_plugin_mapping()

    # then

# Generated at 2022-06-13 22:34:45.369467
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    p = PluginManager()
    p.register(A, B, C)
    assert p.get_formatters_grouped() == {'a': [A], 'b': [B,C]}


# Generated at 2022-06-13 22:34:58.767658
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.builtin import BasicAuthPlugin
    from httpie.plugins.builtin import DigestAuthPlugin
    from httpie.plugins.builtin import HawkAuthPlugin
    from httpie.plugins.builtin import OAuth1Plugin

    plugins_list = [BasicAuthPlugin, DigestAuthPlugin, HawkAuthPlugin, OAuth1Plugin]
    pm = PluginManager()
    for plugin in plugins_list:
        pm.register(plugin)
    plugin_mapping = pm.get_auth_plugin_mapping()

    # Verify the mapping is correct
    assert plugin_mapping['basic'] == BasicAuthPlugin
    assert plugin_mapping['digest'] == DigestAuthPlugin
    assert plugin_mapping['hawk'] == HawkAuthPlugin
    assert plugin_mapping['oauth1'] == OAuth1Plugin

    # Verify the mapping only contains valid

# Generated at 2022-06-13 22:35:09.270144
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import builtin
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.plugins.builtin_plugins import HumanReadableJSONFormatterPlugin, JSONFormatterPlugin,\
         SerializedJSONFormatterPlugin, PrettyJsonFormatterPlugin, FormatPlugin
    import json, jsbeautifier

    assert list(builtin.get_formatters_grouped().keys()) == ['json', 'binary']
    json_formatters: List[FormatterPlugin] = builtin.get_formatters_grouped()['json']
    assert len(json_formatters) == 4
    assert [type(f) for f in json_formatters] == [HumanReadableJSONFormatterPlugin, JSONFormatterPlugin,
                                                  SerializedJSONFormatterPlugin, PrettyJsonFormatterPlugin]

# Generated at 2022-06-13 22:35:14.256442
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.register(PluginAuth, PluginAuth2)
    assert pm.get_auth_plugin_mapping()['auth'] == PluginAuth
    assert pm.get_auth_plugin_mapping()['auth2'] == PluginAuth2



# Generated at 2022-06-13 22:35:21.399521
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(HttpbinAuthPlugin, AuthPlugin, ConverterPlugin, BasePlugin)
    pm.register(FormatterPlugin)
    assert pm.filter(BasePlugin) == [BasePlugin]
    assert pm.filter(ConverterPlugin) == [ConverterPlugin, FormatterPlugin]
    assert pm.filter(AuthPlugin) == [HttpbinAuthPlugin, AuthPlugin]
    assert pm.filter(TransportPlugin) == []
    assert pm.filter(FormatterPlugin) == [FormatterPlugin]



# Generated at 2022-06-13 22:35:25.539952
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Arrange
    manager = PluginManager()
    # Act
    manager.load_installed_plugins()
    # Assert
    assert len(manager) > 0
    print(manager)


# Generated at 2022-06-13 22:35:36.324616
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPluginA(BasePlugin):
        pass

    class TestPluginB(BasePlugin):
        pass

    class TestPluginC(TestPluginA):
        pass

    class TestPluginD(TestPluginB):
        pass

    m = PluginManager()
    m.register(TestPluginA, TestPluginB, TestPluginC, TestPluginD)
    assert TestPluginA in m.filter()
    assert TestPluginB in m.filter()
    assert TestPluginC in m.filter()
    assert TestPluginD in m.filter()
    assert TestPluginA in m.filter(TestPluginA)
    assert TestPluginB in m.filter(TestPluginB)
    assert TestPluginC in m.filter(TestPluginC)
    assert TestPluginD in m.filter(TestPluginD)

# Generated at 2022-06-13 22:35:49.630390
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import pkg_resources



# Generated at 2022-06-13 22:35:56.312474
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    from httpie.plugins.builtin import JSONFormatterPlugin, FormFormatterPlugin
    pm.register(JSONFormatterPlugin,FormFormatterPlugin)
    expected = {
        'JSON': [JSONFormatterPlugin],
        'Forms': [FormFormatterPlugin]
    }
    assert pm.get_formatters_grouped() == expected

# Generated at 2022-06-13 22:36:04.936417
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    list_plugin = [plugin for plugin in PluginManager]
    assert len(list_plugin) == 0
    PluginManager.append(AuthPlugin)
    PluginManager.append(ConverterPlugin)
    PluginManager.append(FormatterPlugin)
    PluginManager.append(TransportPlugin)
    assert len(PluginManager) == 4
    list_plugin_AuthPlugin = [type(plugin) for plugin in PluginManager.filter(AuthPlugin)]
    assert len(list_plugin_AuthPlugin) == 1
    assert list_plugin_AuthPlugin[0] == AuthPlugin

# Generated at 2022-06-13 22:36:10.233121
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    assert pm == []
    pm.load_installed_plugins()
    assert pm != []

# Generated at 2022-06-13 22:36:15.736349
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pluginManager = PluginManager()
    pluginManager.register(TestPlugin1)
    pluginManager.register(TestPlugin2)
    assert pluginManager.get_auth_plugin_mapping() == {
        'test1': TestPlugin1,
        'test2': TestPlugin2
    }

# Generated at 2022-06-13 22:36:24.449829
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    p = PluginManager()
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(C):
        pass
    p.register(A)
    p.register(B)
    p.register(C)
    p.register(D)
    res = p.filter(A)
    assert res == [A, B, C, D]
    res = p.filter(C)
    assert res == [C, D]
    assert p == [A, B, C, D]


# Generated at 2022-06-13 22:36:28.602758
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert 'basic' in auth_plugin_mapping, "Auth plugin mapping must contain 'basic' key."


# Generated at 2022-06-13 22:36:32.400963
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(ConverterPlugin, FormatterPlugin)
    assert plugin_manager.filter() == plugin_manager.filter(by_type=Type[ConverterPlugin]) == [ConverterPlugin, FormatterPlugin]

# Generated at 2022-06-13 22:36:39.020022
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class PluginManagerFake(PluginManager):
        def __init__(self):
            self.data = [
                {'group_name': 'adj', 'name': 'a'},
                {'group_name': 'adj', 'name': 'b'},
                {'group_name': 'noun', 'name': 'c'}
            ]
            self.index = 0
            self.count = 3
            self.reset()
        def __iter__(self):
            return self
        def __next__(self):
            if self.index == self.count:
                raise StopIteration
            self.index += 1
            return self.get_formatters()[self.index-1]
        def get_formatters(self):
            return self.data
        def reset(self):
            self.index = 0

# Generated at 2022-06-13 22:36:48.456603
# Unit test for method load_installed_plugins of class PluginManager

# Generated at 2022-06-13 22:36:52.595739
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.load_installed_plugins()

# Generated at 2022-06-13 22:37:05.396437
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class TestFormatterPlugin(FormatterPlugin):
        group_name = 'test_name'

    class TestFormatterPlugin2(FormatterPlugin):
        group_name = 'test_name'
    
    class TestFormatterPlugin3(FormatterPlugin):
        group_name = 'test_name2'


    manager = PluginManager()
    manager.register(TestFormatterPlugin, TestFormatterPlugin2, TestFormatterPlugin3)

    assert manager.get_formatters_grouped() == {'test_name': [TestFormatterPlugin, TestFormatterPlugin2], 'test_name2': [TestFormatterPlugin3]}

# Generated at 2022-06-13 22:37:07.687893
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    assert plugin_manager.load_installed_plugins() != None


# Generated at 2022-06-13 22:37:24.857664
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import clint
    from httpie.plugins import FormatterPlugin

    class MyPlugin(FormatterPlugin):
        group_name = 'Fake group'
        group_name2 = 'Fake group2'
        group_name3 = 'Fake group3'
        group_name4 = 'Fake group4'
        group_name5 = 'Fake group5'

        def format_headers(self, headers: HeadersDict) -> str:
            pass

        def format_body(self, body: bytes, mime: str, headers: HeadersDict) -> str:
            pass

        def format(self, args, parser, httpbin_url):
            pass

    manager = PluginManager()
    manager.register(MyPlugin)
    result = manager.get_formatters_grouped()
    assert result == {'Fake group': [MyPlugin]}

# Generated at 2022-06-13 22:37:27.919147
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(TestPlugin_1, TestPlugin_2)
    expected = {
        'test': [TestPlugin_1, TestPlugin_2]
    }
    assert pm.get_formatters_grouped() == expected


# Generated at 2022-06-13 22:37:32.569468
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    for entry_point_name in ENTRY_POINT_NAMES:
        assert entry_point_name in plugin_manager



# Generated at 2022-06-13 22:37:37.134420
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins.register(JsonPlugin)
    plugins.register(JsonLinesPlugin)
    plugins.register(png_encoder)
    assert len(plugins.filter(FormatterPlugin)) == 2
    assert len(plugins.filter(ConverterPlugin)) == 1



# Generated at 2022-06-13 22:37:44.797788
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins import AuthPlugin

    # test
    pm = PluginManager()
    # mock
    pm.register(AuthPlugin)
    # check
    assert pm.get_auth_plugin_mapping() == {AuthPlugin.auth_type: AuthPlugin}
    pm.unregister(AuthPlugin)

    # test
    pm = PluginManager()
    # mock
    pm.register(AuthPlugin)
    # check
    assert pm.get_auth_plugin_mapping() == {AuthPlugin.auth_type: AuthPlugin}
    pm.unregister(AuthPlugin)

    # test
    pm = PluginManager()
    # mock
    # check
    assert pm.get_auth_plugin_mapping() == {}

    # test
    pm = PluginManager()
    # mock
    # check
    assert pm.get_auth

# Generated at 2022-06-13 22:37:53.719691
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    plugins = manager.get_formatters()

    # test group_name of plugins' group
    group_names = manager.get_formatters_grouped().keys()
    assert len(list(group_names)) == len(set(group_names))

    # test number of plugins in each group
    for group_name, group in manager.get_formatters_grouped().items():
        assert group_name == group[0].group_name
        for plugin in group:
            assert plugin.group_name == group_name

    # test sum of number of plugins in each group equals total number of plugins
    assert sum([len(group) for group in manager.get_formatters_grouped().values()]) == len(plugins)



# Generated at 2022-06-13 22:37:57.648301
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.plugins
    pluginManager = PluginManager()
    pluginManager.register(httpie.plugins.html.HTMLTableRenderer,
        httpie.plugins.json.JSONTableRenderer)
    assert pluginManager.get_formatters_grouped() == {
        'Visual': [httpie.plugins.html.HTMLTableRenderer],
        'Visual (JSON)': [httpie.plugins.json.JSONTableRenderer]
    }

# Generated at 2022-06-13 22:38:06.545240
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Foo(BasePlugin):
        pass

    class Bar(BasePlugin):
        pass

    class Baz(Foo):
        pass

    manager = PluginManager()
    manager.append(Foo)
    manager.append(Bar)
    manager.append(Baz)

    assert manager.filter(Bar) == [Bar]
    assert manager.filter(Foo) == [Foo, Baz]
    assert manager.filter(BasePlugin) == [Foo, Bar, Baz]

# Metaclass

# Generated at 2022-06-13 22:38:10.623906
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(FormatterPluginA)
    plugins.register(FormatterPluginB)
    plugins.register(FormatterPluginC)
    plugins.register(FormatterPluginD)
    assert plugins.get_formatters_grouped() == {
        'group1': [FormatterPluginA, FormatterPluginB],
        'group2': [FormatterPluginC],
        'group3': [FormatterPluginD]
    }


# Generated at 2022-06-13 22:38:17.581442
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A:
        pass
    class B(A):
        pass
    class C:
        pass
    class D:
        pass
    plugin_manager = PluginManager()
    plugin_manager.register(B)
    assert(plugin_manager[0].__bases__ == (A,))
    assert(plugin_manager.filter(A) == [B])
    assert(plugin_manager.filter(C) == [])
    plugin_manager.register(C)
    assert(plugin_manager.filter(A) == [B])
    assert(plugin_manager.filter(C) == [C])
    assert(plugin_manager.filter(D) == [])



# Generated at 2022-06-13 22:38:37.329664
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.input import ParseError
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.unicode import UnicodeOutputDecoderPlugin
    from httpie.plugins.unicode.detector import EncodingDetector
    from httpie.plugins.unicode.detector import chardet
    pm = PluginManager()
    pm.load_installed_plugins()
    assert AuthPlugin in [type(plugin) for plugin in pm]
    assert FormatterPlugin in [type(plugin) for plugin in pm]
    assert ConverterPlugin in [type(plugin) for plugin in pm]
    assert TransportPlugin in [type(plugin) for plugin in pm]
    assert HTTPBasicAuth in [type(plugin) for plugin in pm]
    assert ParseError in [type(plugin) for plugin in pm]
    assert UnicodeOutputDecoder

# Generated at 2022-06-13 22:38:47.193322
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(B): pass
    class E(D): pass
    class F(D): pass
    class G(D): pass
    class H: pass

    plugin_manager = PluginManager()
    plugin_manager.register(A, B, C, D, E, F, G, H)

    assert plugin_manager.filter(A) == [A, B, C, D, E, F, G]
    assert plugin_manager.filter(B) == [B, C, D, E, F, G]
    assert plugin_manager.filter(C) == [C]
    assert plugin_manager.filter(D) == [D, E, F, G]
    assert plugin_manager.filter(E) == [E]
    assert plugin

# Generated at 2022-06-13 22:38:57.738839
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class MyPlugin(BasePlugin):
        pass

    class MyPlugin2(MyPlugin):
        pass

    class MyPlugin3(MyPlugin):
        pass

    class MyPlugin4(BasePlugin):
        pass

    plugins = PluginManager()
    plugins.register(MyPlugin2, MyPlugin3, MyPlugin4)
    assert plugins.filter(by_type=MyPlugin) == [MyPlugin2, MyPlugin3]
    assert plugins.filter(by_type=BasePlugin) == [MyPlugin2, MyPlugin3, MyPlugin4]
    assert plugins.filter(by_type=MyPlugin4) == [MyPlugin4]


# Generated at 2022-06-13 22:39:04.515742
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    def _test_plugin(plugin_manager, by_type):
        pass
    from httpie.output.formatters import JSONFormatter
    from httpie.plugins import AuthPlugin
    pm = PluginManager()
    pm.register(JSONFormatter, AuthPlugin)
    pm.filter(by_type=AuthPlugin)
    pm.filter(by_type=JSONFormatter)
    # If a wrong type is given, there will be no plugin
    assert [] == pm.filter(by_type=int)

# Generated at 2022-06-13 22:39:07.127063
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_mgr = PluginManager()
    plugin_mgr.load_installed_plugins()
    assert len(plugin_mgr) > 0

# Generated at 2022-06-13 22:39:09.429538
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:39:14.151084
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins_dict = {
        'cbor': [1, 2, 3],
        'json': [4, 5, 6]
    }
    plugins_list = []
    for plugin in plugins_dict:
        plugin_items = plugins_dict[plugin]
        for item in plugin_items:
            plugins_list.append((item, plugin))
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins_list)
    assert plugin_manager.get_formatters_grouped() == plugins_dict

# Generated at 2022-06-13 22:39:15.858115
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth

    test = PluginManager()
    test.register(HTTPBasicAuth)
    assert test.filter()[0] == HTTPBasicAuth
    assert test.filter(by_type=TransportPlugin) == []



# Generated at 2022-06-13 22:39:19.806054
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin_1, FormatterPlugin_2, FormatterPlugin_3)
    plugin_manager.get_formatters_grouped()


# Generated at 2022-06-13 22:39:24.172310
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager_obj = PluginManager()
    plugin_manager_obj.load_installed_plugins()
    assert plugin_manager_obj.get_auth_plugin_mapping() != {}
    

# Generated at 2022-06-13 22:39:50.552577
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0

# Generated at 2022-06-13 22:39:54.680672
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert manager.get_auth_plugins()
    assert manager.get_formatters()
    assert manager.get_transport_plugins()


# Generated at 2022-06-13 22:39:58.698651
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) != 0
    assert len(plugin_manager.get_auth_plugins()) != 0
    assert len(plugin_manager.get_converters()) != 0
    assert len(plugin_manager.get_formatters()) != 0
    assert len(plugin_manager.get_transport_plugins()) != 0

# Generated at 2022-06-13 22:40:03.838807
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    p = PluginManager()
    assert(p.filter()==[])
    assert(p.filter(1)==[])
    assert(p.filter(AuthPlugin)==[])
    assert(p.filter(ConverterPlugin)==[])
    assert(p.filter(TransportPlugin)==[])
    assert(p.filter(FormatterPlugin)==[])


# Generated at 2022-06-13 22:40:06.463511
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert isinstance(plugin_manager, list)

# Generated at 2022-06-13 22:40:08.882912
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins is not None

# Generated at 2022-06-13 22:40:11.378232
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) == 5
    print(manager)



# Generated at 2022-06-13 22:40:21.593634
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin1 = FormatterPlugin()
    plugin1.group_name = "c"
    plugin2 = FormatterPlugin()
    plugin2.group_name = "b"
    plugin3 = FormatterPlugin()
    plugin3.group_name = "c"
    plugin4 = FormatterPlugin()
    plugin4.group_name = "a"

    plugins = PluginManager()
    plugins.register(plugin1)
    plugins.register(plugin2)
    plugins.register(plugin3)
    plugins.register(plugin4)

    grouped = plugins.get_formatters_grouped()

    assert len(grouped) == 3

    assert "b" in grouped
    assert len(grouped["b"]) == 1
    assert grouped["b"][0] == plugin2

    assert "a" in grouped

# Generated at 2022-06-13 22:40:24.268667
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    expected_output = {
        'group_name': [plugin]
    }
    assert plugin_manager.get_formatters_grouped() == expected_output

# Generated at 2022-06-13 22:40:28.762529
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plgMgr = PluginManager()
    plgMgr.load_installed_plugins()

    assert len(plgMgr) > 0

    for plugin in plgMgr:
        assert hasattr(plugin, 'package_name')


# Generated at 2022-06-13 22:41:14.761552
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.load_installed_plugins()
    auth_plugin_mapping = pm.get_auth_plugin_mapping()
    assert 'basic' in auth_plugin_mapping.keys()
    assert 'digest' in auth_plugin_mapping.keys()


# Generated at 2022-06-13 22:41:19.520187
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    #input
    plugins = PluginManager()
    plugins.register(
        FormatterPlugin, FormatterPlugin, FormatterPlugin,
        FormatterPlugin, FormatterPlugin,
    )
    #output
    plugins.get_formatters_grouped()



# Generated at 2022-06-13 22:41:26.958910
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.plugins.auth.builtin import BasicAuthPlugin
    from httpie.plugins.auth.v1 import AuthPlugin
    from httpie.plugins.formatter.v1 import FormatterPlugin
    from httpie.plugins.converter.v1 import ConverterPlugin
    from httpie.plugins.transport.v1 import TransportPlugin
    import pytest

    plugin_mgr = PluginManager()
    plugin_mgr.register(HTTPiePlugin, BasicAuthPlugin)

    assert plugin_mgr.filter(AuthPlugin) == [HTTPiePlugin, BasicAuthPlugin]

    assert plugin_mgr.filter(FormatterPlugin) == [HTTPiePlugin]

    assert plugin_mgr.filter(ConverterPlugin) == []


# Generated at 2022-06-13 22:41:27.961259
# Unit test for method get_formatters_grouped of class PluginManager

# Generated at 2022-06-13 22:41:30.256506
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()


# Global plugin manager
plugin_manager = PluginManager()

# Generated at 2022-06-13 22:41:40.637404
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import FormatterPlugin as BaseFormatter
    from httpie.plugins.builtin import JSONStreamFormatter as JSONStream
    from httpie.plugins.builtin import PrettyJSONStreamFormatter as PrettyJSON
    from httpie.plugins.builtin import JSONFormatter as JSON
    from httpie.plugins.builtin import TableFormatter as Table

    assert PluginManager().get_formatters_grouped() == {}

    plugin_manager = PluginManager([JSONStream, PrettyJSON, JSON, Table])
    r = plugin_manager.get_formatters_grouped()

    assert type(r) == dict
    assert len(r.keys()) == 2
    assert BaseFormatter.group_name in r.keys()
    assert JSONStream.group_name in r.keys()

# Generated at 2022-06-13 22:41:48.170266
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    def get_entry_point_name(plugin_class):
        if issubclass(plugin_class, AuthPlugin):
            return 'httpie.plugins.auth.v1'
        elif issubclass(plugin_class, FormatterPlugin):
            return 'httpie.plugins.formatter.v1'
        elif issubclass(plugin_class, ConverterPlugin):
            return 'httpie.plugins.converter.v1'
        elif issubclass(plugin_class, TransportPlugin):
            return 'httpie.plugins.transport.v1'
        else:
            raise TypeError(
                f'{plugin_class.__name__} is not a subclass of BasePlugin'
            )


# Generated at 2022-06-13 22:41:53.113983
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A: pass
    class B(A): pass
    class C(A): pass

    manager = PluginManager()
    manager.register(A, B, C)

    plugins = manager.filter(by_type=A)
    assert plugins == [A, B, C]

    plugins = manager.filter(by_type=B)
    assert plugins == [B]

# Generated at 2022-06-13 22:41:57.846419
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:42:02.819912
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_converters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0