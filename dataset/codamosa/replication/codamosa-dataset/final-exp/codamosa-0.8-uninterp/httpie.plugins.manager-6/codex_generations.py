

# Generated at 2022-06-13 22:33:25.905825
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Plugin(FormatterPlugin):
        pass
    def mock_get_formatters(self):
        return [
            Plugin('a', 'b'),
            Plugin('a', 'b'),
            Plugin('a', 'c'),
            Plugin('d', 'e'),
        ]
    plugin_manager = PluginManager()
    plugin_manager.get_formatters = mock_get_formatters
    groups = plugin_manager.get_formatters_grouped()
    assert groups == {'b': [Plugin('a', 'b'), Plugin('a', 'b')],
                      'e': [Plugin('d', 'e')],
                      'c': [Plugin('a', 'c')]}

# Generated at 2022-06-13 22:33:31.970443
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(GroupA, GroupB)
    # test the method
    grouped = manager.get_formatters_grouped()
    # test the result
    assert GroupA.group_name in grouped
    assert GroupB.group_name in grouped
    assert len(grouped) == 2
    assert GroupA.group_name in grouped
    assert GroupA in grouped[GroupA.group_name]
    assert GroupB.group_name in grouped
    assert GroupB in grouped[GroupB.group_name]
    # test the result of method filter
    assert len(manager.filter(FormatterPlugin)) == 2
    assert GroupA in manager.filter(FormatterPlugin)
    assert GroupB in manager.filter(FormatterPlugin)

# Test: get_auth_plugin_mapping

# Generated at 2022-06-13 22:33:44.554779
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    assert manager.get_formatters_grouped() == {}


# Generated at 2022-06-13 22:33:50.193630
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    local_plugin_mapping = {}
    for plugin in plugins:
        if isinstance(plugin, AuthPlugin):
            local_plugin_mapping[plugin.auth_type] = plugin
    assert PluginManager().get_auth_plugin_mapping() == local_plugin_mapping

# Generated at 2022-06-13 22:33:55.433425
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    pm = PluginManager()
    pm.load_installed_plugins()
    assert pm[0].__module__ == 'httpie.plugins.auth.basic'
    assert pm[6].__module__ == 'httpie.plugins.transport.http'



# Generated at 2022-06-13 22:34:05.371184
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin
    class FormatterPlugin1(FormatterPlugin):
        group_name = 'test_group_name'
    class FormatterPlugin2(FormatterPlugin):
        group_name = 'test_group_name'
    class FormatterPlugin3(FormatterPlugin):
        group_name = 'test_group_name'
    class FormatterPlugin4(FormatterPlugin):
        group_name = 'test_group_name'
    class FormatterPlugin5(FormatterPlugin):
        group_name = 'test_group_name'
    class FormatterPlugin6(FormatterPlugin):
        group_name = 'test_group_name1'
    class FormatterPlugin7(FormatterPlugin):
        group_name = 'test_group_name1'

# Generated at 2022-06-13 22:34:11.248814
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pluginmanager = PluginManager()
    pluginmanager.register(TestPlugin1)
    pluginmanager.register(TestPlugin2)
    pluginmanager.register(TestPlugin3)
    dictionary = pluginmanager.get_formatters_grouped()
    assert "first" in dictionary
    assert "third" in dictionary


# Generated at 2022-06-13 22:34:20.570741
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_mgr = PluginManager()
    class Foo(object):
        pass
    def bar():
        pass
    class A(Foo):
        pass
    class B(Foo):
        pass
    plugin_mgr.register(A)
    plugin_mgr.register(B)
    assert A in plugin_mgr.filter(Foo)
    assert B in plugin_mgr.filter(Foo)
    assert A in plugin_mgr.filter(Foo)
    assert A not in plugin_mgr.filter(bar)


# Generated at 2022-06-13 22:34:26.334893
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = [
        FormatterPlugin('foo', group_name='group_a'),
        FormatterPlugin('foo1', group_name='group_a'),
        FormatterPlugin('foo2', group_name='group_b'),
        FormatterPlugin('foo3', group_name='group_a'),
        FormatterPlugin('foo4', group_name='group_b'),
    ]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)
    assert plugin_manager.get_formatters_grouped() == {
        'group_a': plugins[:3],
        'group_b': plugins[2:]
    }


plugins = PluginManager()



# Generated at 2022-06-13 22:34:34.616441
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import FormatterPlugin
    from httpie.plugins.builtin.formatters import (
        _JsonPretty,
        _Json,
        _Colors,
        _Headers,
        _PhpHtml,
        _PhpSerialize,
        _PhpVarExport,
        _Php,
        _Csv,
        _Table,
        _Urlencoded,
        _Websocket,
        _TTY,
    )
    class JsonPretty(FormatterPlugin):
        group_name = "JSON"
        name = "json-pretty"
        output_formatters = [_JsonPretty]
    class Json(FormatterPlugin):
        group_name = "JSON"
        name = "json"
        output_formatters = [_Json]
   

# Generated at 2022-06-13 22:34:42.809627
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(Group1Plugin1, Group1Plugin2, Group2Plugin)
    assert plugin_manager.get_formatters_grouped() == {"group1": [Group1Plugin1, Group1Plugin2], "group2": [Group2Plugin]}

# Generated at 2022-06-13 22:34:43.670160
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager.load_installed_plugins(PluginManager())

# Generated at 2022-06-13 22:34:46.256459
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Instantiation of PluginManager class
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    pluginManager.get_formatters_grouped()

# Generated at 2022-06-13 22:34:59.184519
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_test_1 = type('test1', (AuthPlugin,), {})
    plugin_test_2 = type('test2', (AuthPlugin,), {})
    plugin_test_3 = type('test3', (AuthPlugin,), {})
    plugin_test_4 = type('test4', (AuthPlugin,), {})
    plugin_test_5 = type('test5', (AuthPlugin,), {})
    plugin_test_6 = type('test6', (AuthPlugin,), {})

    plugin_manager = PluginManager()
    plugin_manager.register(plugin_test_1, plugin_test_2, plugin_test_3,
                            plugin_test_4, plugin_test_5, plugin_test_6)
    plugin_list = plugin_manager.filter(AuthPlugin)

# Generated at 2022-06-13 22:35:04.015282
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pass
    # pm = PluginManager()
    # plugins = pm.filter(by_type=Type[AuthPlugin])
    # assert len(plugins) == 1
    # assert isinstance(plugins[0], AuthPlugin)
    # assert isinstance(plugins[0], HTTPBasicAuth)

# Generated at 2022-06-13 22:35:14.634773
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_mgr = PluginManager()
    plugin_mgr.load_installed_plugins()
    auth_plugin_mapping = plugin_mgr.get_auth_plugin_mapping()
    assert type(auth_plugin_mapping) == dict
    assert 'basic' in auth_plugin_mapping
    assert 'digest' in auth_plugin_mapping
    assert 'jwt' in auth_plugin_mapping
    assert 'aws' in auth_plugin_mapping
    assert 'aws4' in auth_plugin_mapping
    assert 'hawk' in auth_plugin_mapping


# Generated at 2022-06-13 22:35:22.059374
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A(BasePlugin):
        pass
    class B(A):
        pass
    class C(BasePlugin):
        pass
    assert PluginManager().register(A,B,C).filter(BasePlugin) == [A,B,C]
    assert PluginManager().register(A,B,C).filter(A) == [A,B]
    assert PluginManager().register(A,B,C).filter(C) == [C]
    assert PluginManager().register(A,B,C).filter(B) == [B]


# Generated at 2022-06-13 22:35:36.689704
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # Case 1: Len of instance before calling PluginManager.get_auth_plugin_mapping()
    # and PluginManager.load_installed_plugins() is 0
    plugin_manager = PluginManager()
    assert len(plugin_manager) == 0

    # Case 2: Len of instance before calling PluginManager.get_auth_plugin_mapping() and
    # PluginManager.load_installed_plugins() is not 0
    plugin_manager.register(AuthPlugin, FormatterPlugin)
    assert len(plugin_manager) != 0

    # Case 3: Len of instance after calling PluginManager.get_auth_plugin_mapping()
    # and PluginManager.load_installed_plugins()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugin_mapping()) != 0



# Generated at 2022-06-13 22:35:49.980212
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PM = PluginManager()

    from httpie.plugins.formatter.v1 import FormatterPlugin
    from httpie.plugins.formatter.json import JSONFormatterPlugin
    from httpie.plugins.formatter.html import HTMLFormatterPlugin

    class FormatterPlugin_1(FormatterPlugin):
        group_name = 'f1'
        name = 'name'

    class FormatterPlugin_2(FormatterPlugin):
        group_name = 'f1'
        name = 'name'

    class FormatterPlugin_3(FormatterPlugin):
        group_name = 'f2'
        name = 'name'

    PM.register(
        FormatterPlugin_1,
        FormatterPlugin_2,
        FormatterPlugin_3,
        JSONFormatterPlugin,
        HTMLFormatterPlugin
    )

    assert PM.get

# Generated at 2022-06-13 22:35:57.698638
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    expected_auth_plugin_mapping = {'basic': httpie.plugins.auth.BasicAuthPlugin, 'digest': httpie.plugins.auth.DigestAuthPlugin}
    assert auth_plugin_mapping == expected_auth_plugin_mapping


# Generated at 2022-06-13 22:36:09.409443
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import ConverterPlugin
    from httpie.plugins import TransportPlugin
    import pytest
    class MockPlugin(BasePlugin):
        pass
    class MockAuthPlugin(AuthPlugin):
        pass
    class MockFormatterPlugin(FormatterPlugin):
        pass
    class MockConverterPlugin(ConverterPlugin):
        pass
    class MockTransportPlugin(TransportPlugin):
        pass
    class MockAuthPlugin2(AuthPlugin):
        pass
    class MockFormatterPlugin2(FormatterPlugin):
        pass
    class MockConverterPlugin2(ConverterPlugin):
        pass
    class MockTransportPlugin2(TransportPlugin):
        pass
    plugin_manager = PluginManager()

# Generated at 2022-06-13 22:36:14.113389
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    auth_plugin_mapping = {}
    auth_plugin_mapping['name'] = TestClassAuthPlugin
    assert TestClassPluginManager.get_auth_plugin_mapping() == auth_plugin_mapping


# Generated at 2022-06-13 22:36:16.659162
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert (PluginManager.filter.__annotations__ ==
            {'by_type': Type[BasePlugin]})


# Generated at 2022-06-13 22:36:19.852060
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_manager.get_formatters_grouped()


# Generated at 2022-06-13 22:36:27.450607
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.core import CoreAuthPlugin
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth
    from httpie.plugins.httpie import HTTPieAuthPlugin

    manager_list = PluginManager()
    manager_list.load_installed_plugins()

    plugin_count = len(manager_list)

    assert issubclass(HTTPBasicAuth, AuthPlugin) is True
    assert issubclass(HTTPDigestAuth, AuthPlugin) is True
    assert issubclass(HTTPieAuthPlugin, AuthPlugin) is True
    assert issubclass(CoreAuthPlugin, AuthPlugin) is True
    assert plugin_count >= 4

# Generated at 2022-06-13 22:36:35.014940
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    f1 = FormatterPlugin()
    f1.group_name = "group1"
    f2 = FormatterPlugin()
    f2.group_name = "group1"
    f3 = FormatterPlugin()
    f3.group_name = "group2"
    f4 = FormatterPlugin()
    f4.group_name = "group2"

    pm = PluginManager()
    pm.register(f1, f2, f3, f4)
    result =  {
            "group1": [f1, f2],
            "group2": [f3, f4]
        }
    assert (pm.get_formatters_grouped() == result)


# Generated at 2022-06-13 22:36:44.106939
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mngr = PluginManager()
    mngr.register(
        type('formatter', (FormatterPlugin,), {}),
        type('converter', (ConverterPlugin,), {}),
        type('auth', (AuthPlugin,), {}),
        type('transport', (TransportPlugin,), {}),
    )
    mngr.load_installed_plugins()
    assert set(
        getattr(mngr, method_name)()
        for method_name
        in ('get_auth_plugins', 'get_formatters', 'get_converters', 'get_transport_plugins')
    )
    assert mngr

# Generated at 2022-06-13 22:36:49.927721
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPTokenAuth
    pm = PluginManager()
    pm.register(HTTPBasicAuth, HTTPTokenAuth)
    assert pm.get_auth_plugin_mapping() == {
        'basic': HTTPBasicAuth,
        'token': HTTPTokenAuth,
    }

# test get_formatters_grouped

# Generated at 2022-06-13 22:36:57.361539
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class ParentClass:
        pass
    class SubClass(ParentClass):
        pass
    class OtherClass:
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(ParentClass, SubClass, OtherClass)

    assert plugin_manager.filter(ParentClass) == [ParentClass, SubClass]
    assert plugin_manager.filter(OtherClass) == [OtherClass]

# Generated at 2022-06-13 22:37:03.826090
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert isinstance(plugins, list) == True
    assert isinstance(plugins[0], type) == True
    assert isinstance(plugins[0].package_name, str) == True


# Generated at 2022-06-13 22:37:15.495161
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Pluginx(FormatterPlugin, FormatterPlugin):
        pass
    Pluginx.group_name = 'group1'
    Pluginx.package_name = 'Not imported'
    manager = PluginManager()
    manager.register(Pluginx)
    assert (manager.get_formatters_grouped()['group1'] ==
            [Pluginx, Pluginx])

# Generated at 2022-06-13 22:37:28.247740
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    mapping = plugins.get_auth_plugin_mapping()
    assert mapping['basic'] == httpie.plugins.auth.basic.BasicAuthPlugin
    assert mapping['digest'] == httpie.plugins.auth.digest.DigestAuthPlugin
    assert mapping['hawk'] == httpie.plugins.auth.hawk.HawkAuthPlugin
    assert mapping['jwt'] == httpie.plugins.auth.jwt.JWTAuthPlugin
    assert mapping['multipart'] == httpie.plugins.auth.multipart.MultipartAuthPlugin
    assert mapping['ntlm'] == httpie.plugins.auth.ntlm.NTLMAuthPlugin
    assert mapping['oauth1'] == httpie.plugins.auth.oauth1.OAuth1AuthPlugin
   

# Generated at 2022-06-13 22:37:31.533902
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 6

# Generated at 2022-06-13 22:37:40.408944
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class P(BasePlugin):
        pass

    class A(P):
        pass

    class B(P):
        pass

    class C(P, AuthPlugin):
        pass

    class A1:
        pass

    class B1:
        pass

    plugins = PluginManager()
    plugins.register(A, B, C, A1, B1)

    assert plugins.filter() == [A, B, C, A1, B1]
    assert plugins.filter(A) == [A]
    assert plugins.filter(FormatterPlugin) == []
    assert plugins.filter(AuthPlugin) == [C]
    assert plugins.filter(P) == [A, B, C]


# Generated at 2022-06-13 22:37:44.876542
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    a = PluginManager()
    a.load_installed_plugins()
    print("\nAll the plugins are:")
    for i in a:
        print(i)

# Generated at 2022-06-13 22:37:50.819456
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    test_PluginManager_get_formatters_grouped：获取格式化插件分组后的列表
    """
    import json
    from httpie.plugins.builtin import JSONFormatter
    PluginManager.register(JSONFormatter)

# Generated at 2022-06-13 22:37:55.012272
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    a_class = Type[BasePlugin]  # BasePlugin.__class__
    plugin_manager.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)
    result = plugin_manager.filter(AuthPlugin)
    if result:
        assert result == [AuthPlugin, AuthPlugin, AuthPlugin, AuthPlugin], "result is not expected"
    else:
        assert False, "result is not expected"



# Generated at 2022-06-13 22:37:58.582435
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert PluginManager.get_formatters_grouped(PluginManager()) == {
        'group1': list(base_formatter),
        'group2': [base_formatter],
        'group3': [base_formatter]
    }
    assert PluginManager.get_formatters_grouped(PluginManager()) == {
        'group1': [base_formatter],
        'group2': [base_formatter],
        'group3': [base_formatter]
    }

# Generated at 2022-06-13 22:38:07.287894
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(FormatterPlugin)

    formatters_grouped = plugin_manager.get_formatters_grouped()
    assert formatters_grouped.keys() == {'group1', 'group2', 'group3'}


# Generated at 2022-06-13 22:38:14.684856
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    assert pm.get_formatters_grouped() == {}

    class FormatHTML(FormatterPlugin):
        group_name = 'html'

    class FormatText(FormatterPlugin):
        group_name = 'text'

    class FormatXML(FormatterPlugin):
        group_name = 'xml'

    pm.register(FormatHTML, FormatText, FormatXML)
    assert pm.get_formatters_grouped() == {
        'html': [FormatHTML],
        'text': [FormatText],
        'xml': [FormatXML],
    }


# Generated at 2022-06-13 22:38:27.438191
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    mgr = PluginManager()
    mgr.register(FormatterPlugin)
    ret = mgr.get_formatters_grouped()
    assert ret['Formatter'] == [FormatterPlugin]

# Generated at 2022-06-13 22:38:30.980123
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginManager = PluginManager()
    pluginManager.load_installed_plugins()
    assert len(pluginManager) > 0


# Generated at 2022-06-13 22:38:33.276405
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager().load_installed_plugins()
    assert plugins[0].package_name == 'httpie-unixsocket'

# Generated at 2022-06-13 22:38:37.445021
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    l = [ FormatterPlugin, FormatterPlugin, FormatterPlugin, PluginManager]
    l[0].group_name = 'json'
    l[1].group_name = 'html'
    l[2].group_name = 'xml'
    dic = {'json': [l[0]], 'html': [l[1]], 'xml': [l[2]]}
    assert PluginManager().get_formatters_grouped() == dic

# Generated at 2022-06-13 22:38:41.744906
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()
    manager.load_installed_plugins()
    auth_plugin_mapping = manager.get_auth_plugin_mapping()
    assert 'basic' in auth_plugin_mapping
    assert 'digest' in auth_plugin_mapping


# Generated at 2022-06-13 22:38:43.561236
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    p = PluginManager()
    p.load_installed_plugins()

    assert len(p)==15



# Generated at 2022-06-13 22:38:51.875632
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import HTMLFormatterPlugin
    from httpie.plugins import BuiltinPlugin
    plugins_manager = PluginManager()
    plugins_manager.register(BuiltinPlugin)
    plugins_grouped = plugins_manager.get_formatters_grouped()
    assert plugins_grouped['HTML View'][0] == HTMLFormatterPlugin

# PluginManager instance.
plugins_manager = PluginManager()
plugins_manager.load_installed_plugins()

# Generated at 2022-06-13 22:38:56.191688
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class CustomPlugin(FormatterPlugin):
        package_name = "package_name"

    PlugMan = PluginManager()
    PlugMan.register(CustomPlugin)
    assert PlugMan.get_formatters_grouped() == {'standard':[CustomPlugin]}

# Generated at 2022-06-13 22:39:07.611270
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin
    from httpie.plugins.base import BasePlugin, TransportPlugin

    class AuthPluginMock(AuthPlugin):
        pass

    class AuthPluginMock1(AuthPlugin):
        pass

    class ConverterPluginMock(ConverterPlugin):
        pass

    class FormatterPluginMock(FormatterPlugin):
        pass

    class TransportPluginMock(TransportPlugin):
        pass

    class PluginMock(BasePlugin):
        pass

    plugin_manager = PluginManager()

    plugin_manager.register(
        AuthPluginMock, AuthPluginMock1,
        ConverterPluginMock, FormatterPluginMock, TransportPluginMock,
        PluginMock
    )

    assert not plugin_manager.filter(PluginMock)

    assert plugin_manager

# Generated at 2022-06-13 22:39:12.574715
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.append(Type[AuthPlugin])
    plugin_manager.append(Type[ConverterPlugin])
    plugin_manager.append(Type[FormatterPlugin])
    plugin_manager.append(Type[TransportPlugin])
    assert [Type[AuthPlugin], Type[FormatterPlugin], Type[TransportPlugin]] == plugin_manager.filter(
        by_type=Type[BasePlugin])

# Generated at 2022-06-13 22:39:35.253894
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    p = PluginManager()
    p.load_installed_plugins()

    assert len(p) != 0



# Generated at 2022-06-13 22:39:36.989785
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0



# Generated at 2022-06-13 22:39:38.499735
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) > 0


# Generated at 2022-06-13 22:39:45.073853
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.builtin import HTTPBasicAuth

    plugin = PluginManager()
    plugin.register(HTTPBasicAuth)
    plugin.register(HTTPBasicAuth)
    assert len(plugin.filter()) == 2
    assert len(plugin.filter(AuthPlugin)) == 1



# Generated at 2022-06-13 22:39:57.266381
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    formatters = PluginManager().get_formatters_grouped()

# Generated at 2022-06-13 22:40:05.993532
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.output
    from httpie.output.formatters.colors import ColorsFormatter
    from httpie.output.formatters.json import JSONFormatter
    from httpie.output.formatters.colors import ColorsFormatter
    # print(httpie.plugins.manager)
    # formatted_output.Formatter
    # print(isinstance(formatted_output.Formatter, httpie.base.BasePlugin))
    manager = PluginManager()
    manager.register(
        httpie.output.table.TableFormatter,
        httpie.output.formatters.json.JSONFormatter,
        httpie.output.formatters.colors.ColorsFormatter
    )
    # print(manager.get_formatters())
    grouped = manager.get_formatters_grouped()
    print(grouped)
    #

# Generated at 2022-06-13 22:40:17.426292
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # test data
    export_plugins = {
        'formatter': {
            'group_name': 'Formatter',
            'package_name': 'formatter',
        },
        'converter': {
            'group_name': 'Converter',
            'package_name': 'converter',
        },
        'auth': {
            'auth_type': 'Auth',
            'package_name': 'auth',
        },
    }

    def mock_load_plugins(entry_point_name):
        plugins = []
        if entry_point_name in export_plugins:
            export_plugin = export_plugins[entry_point_name]
            plugin = base.BasePlugin()
            for key, value in export_plugin.items():
                setattr(plugin, key, value)

# Generated at 2022-06-13 22:40:24.635217
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    def FakeAuthPlugin1(AuthPlugin):
        auth_type = 'fake-auth-1'

    def FakeAuthPlugin2(AuthPlugin):
        auth_type = 'fake-auth-2'

    def FakeTransport(TransportPlugin):
        pass


    manager = PluginManager()
    manager.register(FakeTransport,FakeAuthPlugin1,FakeAuthPlugin2)

    assert manager.filter(AuthPlugin) == [FakeAuthPlugin1, FakeAuthPlugin2]
    assert manager.filter(TransportPlugin) == [FakeTransport]
    assert manager.filter(Type[TransportPlugin]) == [FakeTransport]

# Generated at 2022-06-13 22:40:27.672516
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.register(BasicAuthPlugin, DigestAuthPlugin, BearerTokenAuthPlugin)
    assert (pm.get_auth_plugin_mapping()
            == {'basic': BasicAuthPlugin,
                'digest': DigestAuthPlugin,
                'bearer': BearerTokenAuthPlugin})


# Generated at 2022-06-13 22:40:31.600477
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()

    assert len(pm.get_auth_plugins()) >= 1
    assert len(pm.get_formatters()) >= 1
    assert len(pm.get_converters()) >= 1
    assert len(pm.get_transport_plugins()) >= 1
    assert len(pm) >= 1

# Generated at 2022-06-13 22:41:24.383517
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A(object):
        pass
    
    class B(A):
        pass
    
    class C(B):
        pass
    
    class D(object):
        pass
    
    class E(D):
        pass
    
    class F(E):
        pass

    plugins = [A, B, C, D, E, F]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)

    assert set(plugin_manager.filter(A)) == set([A, B, C])
    assert set(plugin_manager.filter(D)) == set([D, E, F])
    assert set(plugin_manager.filter(E)) == set([E, F])
    assert set(plugin_manager.filter(C)) == set([C])

# Generated at 2022-06-13 22:41:26.072969
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginManager().get_auth_plugin_mapping()


# Generated at 2022-06-13 22:41:35.444796
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPlugin1(BasePlugin):
        pass
    class TestPlugin2(BasePlugin):
        pass
    class TestPlugin3(BasePlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(TestPlugin1, TestPlugin2, TestPlugin3)
    plugin_manager.filter() == [TestPlugin1, TestPlugin2, TestPlugin3]
    plugin_manager.filter(by_type=BasePlugin) == [TestPlugin1, TestPlugin2, TestPlugin3]
    plugin_manager.filter(by_type=TestPlugin) == [TestPlugin1, TestPlugin2, TestPlugin3]
    plugin_manager.filter(by_type=TestPlugin1) == [TestPlugin1]

# Generated at 2022-06-13 22:41:43.624380
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    f1=FormatterPlugin()
    f2=FormatterPlugin()
    f3=FormatterPlugin()
    a1=AuthPlugin()
    a2=AuthPlugin()
    a3=AuthPlugin()
    c1=ConverterPlugin()
    c2=ConverterPlugin()
    c3=ConverterPlugin()
    t1=TransportPlugin()
    t2=TransportPlugin()
    t3=TransportPlugin()
    plugin_manager = PluginManager()
    plugin_manager.register(f1, f2, f3, a1, a2, a3, c1, c2, c3, t1, t2, t3)
    assert plugin_manager.filter(FormatterPlugin)==[f1, f2, f3]

# Generated at 2022-06-13 22:41:53.286410
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class Plugin1(BasePlugin):
        pass

    class Plugin2(BasePlugin):
        pass

    class Plugin3(BasePlugin):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(Plugin1, Plugin2, Plugin3)

    assert plugin_manager == [Plugin1, Plugin2, Plugin3]
    assert plugin_manager.filter(by_type=Plugin1) == [Plugin1]
    assert plugin_manager.filter() == [Plugin1, Plugin2, Plugin3]



# Generated at 2022-06-13 22:41:57.647521
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()

    try:
        plugin_manager.load_installed_plugins()
        print('load_installed_plugins() method of class PluginManager works')
    except:
        raise AssertionError

    assert len(plugin_manager) > 0
    print('Passed test case')

test_PluginManager_load_installed_plugins()


# Generated at 2022-06-13 22:42:02.327886
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.register(BashFormatPlugin, JSONFormatPlugin, ColoredJSONFormatPlugin)
    assert pm.get_formatters_grouped() == {
        'Bash': [BashFormatPlugin],
        'JSON': [JSONFormatPlugin, ColoredJSONFormatPlugin]
    }

# Generated at 2022-06-13 22:42:10.446109
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.output.formatters.base import Formatter
    class Formatter1(Formatter):
        group_name = 'group1'
    class Formatter2(Formatter):
        group_name = 'group1'
    class Formatter3(Formatter):
        group_name = 'group2'
    class Formatter4(Formatter):
        group_name = 'group2'
    # Add all formatters
    plugins = PluginManager()
    plugins.register(Formatter1, Formatter2, Formatter3, Formatter4)
    # Test method get_formatters_grouped
    formatters_grouped = plugins.get_formatters_grouped()
    assert len(formatters_grouped) == 2
    assert 'group1' in formatters_grouped
    assert 'group2' in formatters_grouped

# Generated at 2022-06-13 22:42:18.055858
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    class _A: pass
    class _A2(_A): pass
    class _B: pass
    plugins.register(_A, _A2, _B)
    assert plugins.filter(by_type=_A) == [_A, _A2]
    assert plugins.filter(by_type=_B) == [_B]
    assert plugins.filter() == [_A, _A2, _B]


# Generated at 2022-06-13 22:42:22.512935
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # Note: The length of list plugin_manager will change with the number of plugins
    assert len(plugin_manager) == 28
