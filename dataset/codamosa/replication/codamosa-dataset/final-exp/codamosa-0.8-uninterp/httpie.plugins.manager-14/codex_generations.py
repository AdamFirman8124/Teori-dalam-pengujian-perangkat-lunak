

# Generated at 2022-06-13 22:33:21.195014
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import core
    plugin_manager = PluginManager()
    plugin_manager.register(core.JSONConverter, core.UrlencodedFormatter, core.HTTPBasicAuth)
    assert plugin_manager.filter() == plugin_manager.filter(by_type=Type[BasePlugin])
    assert plugin_manager.filter(by_type=JSONConverter) == plugin_manager.filter(by_type=ConverterPlugin)

# Generated at 2022-06-13 22:33:29.650631
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Install 2 plugins first
    test_plugin = { 'httpie_plugin_test_1': 'v1',
                    'httpie_plugin_test_2': 'v1'}

# Generated at 2022-06-13 22:33:33.463433
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins_list_before = PluginManager([])
    plugins_list_before.load_installed_plugins()
    assert plugins_list_before != PluginManager([])



# Generated at 2022-06-13 22:33:35.141424
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    m = PluginManager()
    assert m.get_formatters_grouped() == {}

# Generated at 2022-06-13 22:33:43.382979
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(JSONPrettyPrintPlugin, JSONPrettyDumpPlugin)
    assert plugin_manager.get_formatters_grouped() == { 'Pretty Print': [JSONPrettyPrintPlugin, JSONPrettyDumpPlugin]}
    plugin_manager.unregister(JSONPrettyPrintPlugin)
    assert plugin_manager.get_formatters_grouped() == { 'Pretty Print': [JSONPrettyDumpPlugin]}
    plugin_manager.unregister(JSONPrettyDumpPlugin)
    assert plugin_manager.get_formatters_grouped() == {}

# Generated at 2022-06-13 22:33:47.369688
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert(len(pm.filter(AuthPlugin))>0)
    assert(len(pm.filter(FormatterPlugin))>0)
    assert(len(pm.filter(ConverterPlugin))>0)
    assert(len(pm.filter(TransportPlugin))>0)


# Generated at 2022-06-13 22:33:58.699401
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PLUGINS_LIST = [
        """
        class Plugin1(FormatterPlugin):
            group_name = "One"
        """,
        """
        class Plugin2(FormatterPlugin):
            group_name = "Two"
        """,
        """
        class Plugin3(FormatterPlugin):
            group_name = "One"
        """
    ]
    
    
    plugins = PluginManager()
    for plugin in PLUGINS_LIST:
        exec(plugin, globals())
        plugins.register(locals()[plugin.split()[1][:-1]])
    plugins.get_formatters_grouped()
    assert plugins.get_formatters_grouped() == {'One': [Plugin1, Plugin3], 'Two': [Plugin2]}

# Generated at 2022-06-13 22:34:01.273962
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PlugabbleObject = PluginManager()
    loaded_plugins = PlugabbleObject.load_installed_plugins()
    assert loaded_plugins

# Generated at 2022-06-13 22:34:13.403762
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()

    class FakeFormatterPlugin1():
        group_name = "fake_group"
        group_order = 1

    class FakeFormatterPlugin2():
        group_name = "fake_group"
        group_order = 2

    class FakeFormatterPlugin3():
        group_name = "another_group"
        group_order = 1

    manager.register(FakeFormatterPlugin1,
                     FakeFormatterPlugin2,
                     FakeFormatterPlugin3)

    formatters_grouped = manager.get_formatters_grouped()

    assert formatters_grouped["fake_group"][0].group_order < formatters_grouped["fake_group"][1].group_order

# Generated at 2022-06-13 22:34:23.818718
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.pretty import PrettyPlugin, pretty_plugin_manager
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPDigestAuth, JSONData, URLEncodedFormData

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert plugin_manager.load_installed_plugins()

    assert (PrettyPlugin,) == pretty_plugin_manager.filter(PrettyPlugin)
    assert (HTTPBasicAuth, HTTPDigestAuth) == tuple(plugin_manager.filter(AuthPlugin))
    assert (JSONData, URLEncodedFormData) == tuple(plugin_manager.filter(ConverterPlugin))
    assert (HTTPBasicAuth, HTTPDigestAuth) == pretty_plugin_manager.filter(AuthPlugin)

# Generated at 2022-06-13 22:34:30.314863
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    a = PluginManager()
    a.register(AuthPlugin)
    a.register(ConverterPlugin)
    a.register(FormatterPlugin)
    a.register(TransportPlugin)
    print(a.filter())
    print(a.filter(AuthPlugin))
    print(a.filter(ConverterPlugin))


# Generated at 2022-06-13 22:34:32.962326
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()


# Generated at 2022-06-13 22:34:38.313761
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # arrange
    plugin_manager= PluginManager()
    # act
    def get_formatters_grouped(self):
        return {
            group_name: list(group)
            for group_name, group
            in groupby(self.get_formatters(), key=attrgetter('group_name'))
        }
    # assert
    assert get_formatters_grouped == get_formatters_grouped


# Generated at 2022-06-13 22:34:49.029662
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import formatter
    from httpie.plugins.builtin import HTTPHeaderAuth, JSONLinesRenderer

    # Do not include the standard (builtin) plugins.
    plugins: List[Type[FormatterPlugin]] = [
        f for f in formatter.__all__
        if f not in [
            HTTPHeaderAuth.__name__,
            JSONLinesRenderer.__name__,
        ]
    ]
    plugins = formatter.__dict__['__all__']

    from httpie.plugins import manager
    plugins = [manager.__dict__[p] for p in plugins]

    manager = PluginManager()
    manager.register(*plugins)
    assert len(manager.get_formatters_grouped()) == 2 # expected 2 groups


if __name__ == "__main__":
    test

# Generated at 2022-06-13 22:35:02.444842
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    Unit test for method get_formatters_grouped of class PluginManager
    """
    plugin_manager = PluginManager()
    plugin_manager.register(ColoredFormatter)
    plugin_manager.register(JsonColoredFormatter)
    plugin_manager.register(JsonLinesColoredFormatter)
    plugin_manager.register(JsonLinesColoredDictFormatter)

    got = plugin_manager.get_formatters_grouped()
    if (len(got) == 4) \
            and (len(got.get('Colored')) == 3) \
            and (len(got.get('JSONColored')) == 1) \
            and (len(got.get('JSONColoredDict')) == 1):
        assert True
    else:
        assert False

# Generated at 2022-06-13 22:35:10.999348
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugmgr = PluginManager()
    class A(FormatterPlugin):
        group_name = 'a'
    class B(FormatterPlugin):
        group_name = 'b'
    class C(FormatterPlugin):
        group_name = 'a'
    plugmgr.register(A(), B(), C())
    assert plugmgr.get_formatters_grouped() == {'a':[A,C], 'b':[B]}


# Generated at 2022-06-13 22:35:12.041653
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    assert isinstance(plugin_manager.get_auth_plugin_mapping(), dict)

# Generated at 2022-06-13 22:35:22.141525
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, AuthPluginAuto

    class MockAuthPlugin(AuthPlugin):
        auth_type = 'mock'

    class MockAuthPluginAuto(AuthPluginAuto):
        pass

    class MockTransportPlugin(TransportPlugin):
        pass

    class MockFormatPlugin(FormatterPlugin):
        pass


    plugin_types = [MockAuthPlugin, MockAuthPluginAuto, MockTransportPlugin, MockFormatPlugin]

    plugin_manager = PluginManager()
    plugin_manager.register(*plugin_types)

    auth_plugins = plugin_manager.filter(AuthPlugin)
    assert MockAuthPlugin in auth_plugins
    assert MockAuthPluginAuto in auth_plugins
    assert not plugin_manager.filter(AuthPlugin) == plugin_manager
    assert not plugin_manager.filter(MockAuthPlugin) == plugin_manager
   

# Generated at 2022-06-13 22:35:24.632882
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) > 0



# Generated at 2022-06-13 22:35:30.119888
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin_type = plugin_manager.filter(TransportPlugin)
    
    assert plugin_manager
    assert plugin_type


registry = PluginManager()
registry.load_installed_plugins()

# Generated at 2022-06-13 22:35:40.177848
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPBasicAuthPlugin
    from httpie.plugins.builtin import HTTPBearerAuthPlugin, HTTPTokenAuthPlugin

    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    assert plugin_manager.get_auth_plugin(HTTPBasicAuth.auth_type) is HTTPBasicAuthPlugin
    assert plugin_manager.get_auth_plugin(HTTPBearerAuthPlugin.auth_type) is HTTPBearerAuthPlugin
    assert plugin_manager.get_auth_plugin(HTTPTokenAuthPlugin.auth_type) is HTTPTokenAuthPlugin


# Generated at 2022-06-13 22:35:50.990760
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import HTTPieOutputOptions
    from httpie.plugins.builtin import JSONTOption, HTMTOption, PrettyOptions

    plugins = PluginManager()
    plugins.register(HTTPieOutputOptions)
    plugins.register(JSONTOption)
    plugins.register(HTMTOption)
    plugins.register(PrettyOptions)
    assert plugins.get_formatters_grouped() == {
        'colors': [HTTPieOutputOptions],
        'json': [JSONTOption],
        'pretty': [PrettyOptions],
        'table': [HTMTOption]
    }

if __name__ == '__main__':
    test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:35:59.803878
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class DummyClass(object):
        pass
    dummy_class1 = DummyClass()
    dummy_class2 = DummyClass()
    dummy_class3 = DummyClass()

    plugin_manager = PluginManager()
    plugin_manager.register(dummy_class1, dummy_class2, dummy_class3)

    assert plugin_manager.filter(DummyClass) == [dummy_class1, dummy_class2, dummy_class3]
    assert plugin_manager.filter(DummyClass) != [dummy_class1, dummy_class2, dummy_class3, DummyClass]
    assert plugin_manager.filter(DummyClass) != [dummy_class1, dummy_class3]

# Generated at 2022-06-13 22:36:07.848291
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert PluginManager().get_formatters_grouped() == {}
    p = PluginManager()
    p.register(Plugin1)
    p.register(Plugin2)
    p.register(Plugin3)
    p.register(PluginE1)
    r = p.get_formatters_grouped()
    assert list(r['Group1']) == [Plugin1, Plugin3]
    assert list(r['Group2']) == [Plugin2]
    assert list(r['GroupE1']) == [PluginE1]



# Unit testing for PluginManager

# Generated at 2022-06-13 22:36:10.944748
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mgr = PluginManager()
    mgr.load_installed_plugins()
    print(mgr)

# Generated at 2022-06-13 22:36:14.351497
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugins = PluginManager()
    plugins.register(AuthPlugin)
    plugins.get_auth_plugin_mapping()



# Generated at 2022-06-13 22:36:16.083035
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager().load_installed_plugins()

# Generated at 2022-06-13 22:36:24.517409
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.append(FormatterPlugin)
    # print(plugin_manager.get_formatters())
    # print(plugin_manager.get_formatters_grouped())
    plugin_manager.append(FormatterPlugin)
    # print(plugin_manager.get_formatters())
    # print(plugin_manager.get_formatters_grouped())
    plugin_manager.append(FormatterPlugin)
    print(plugin_manager.get_formatters())
    print(plugin_manager.get_formatters_grouped())


# Generated at 2022-06-13 22:36:30.151570
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.load_installed_plugins()

    formatters = plugins.get_formatters_grouped()

    keys = list(formatters.keys())
    for formatter in formatters[keys[0]]:
        assert formatters[keys[0]][0].group_name == formatter.group_name

# Generated at 2022-06-13 22:36:31.629497
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) == 4


# Generated at 2022-06-13 22:36:37.138992
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager)

# Generated at 2022-06-13 22:36:47.442591
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.output.formatters.colors import ColoredFormatter
    from httpie.output.formatters.colors import SupportColorsFormatter
    from httpie.output.formatters.format import FormatFormatter
    from httpie.output.formatters.indent import IndentFormatter
    from httpie.output.formatters.json import JSONFormatter
    from httpie.output.formatters.pretty import PrettyFormatter
    from httpie.output.formatters.table import TableFormatter
    from httpie.output.formatters.terminal import TerminalFormatter
    from httpie.output.formatters.uri import URIFormatter
    from httpie.output.formatters.utils import get_terminal_width
    from httpie.plugins import FormatterPlugin


# Generated at 2022-06-13 22:36:50.120987
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) != 0


# Generated at 2022-06-13 22:36:56.306403
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(ConverterPlugin)
    plugin_manager.register(TransportPlugin)
    print(plugin_manager.get_formatters_grouped())

# Generated at 2022-06-13 22:37:09.894813
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins_list=[FormatterPlugin,FormatterPlugin,FormatterPlugin]
    plugins_list[0].group_name='Group1'
    plugins_list[1].group_name='Group2'
    plugins_list[2].group_name='Group1'
    manager = PluginManager()
    manager.register(*plugins_list)
    # plugins_list[0] and plugins_list[2] are in the same group
    all_formatters_grouped = manager.get_formatters_grouped()
    assert all_formatters_grouped['Group1'][0] == plugins_list[0]
    assert all_formatters_grouped['Group1'][1] == plugins_list[2]
    assert all_formatters_grouped['Group2'][0] == plugins_list[1]


# Generated at 2022-06-13 22:37:17.161452
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    for index in range(3):
        plugin_manager.load_installed_plugins()
        assert len(plugin_manager) > 0
        assert (
            len(plugin_manager) == len(ENTRY_POINT_NAMES)
            or len(plugin_manager) == 3 * len(ENTRY_POINT_NAMES)
        )

# Generated at 2022-06-13 22:37:27.044870
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.register(AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin)
    f_auth = pm.filter(AuthPlugin)
    f_formatter = pm.filter(FormatterPlugin)
    f_converter = pm.filter(ConverterPlugin)
    f_transport = pm.filter(TransportPlugin)
    assert f_auth == [AuthPlugin]
    assert f_formatter == [FormatterPlugin]
    assert f_converter == [ConverterPlugin]
    assert f_transport == [TransportPlugin]


# Generated at 2022-06-13 22:37:29.145182
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert pm is not None

# Generated at 2022-06-13 22:37:32.069510
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert list(pm)


# Generated at 2022-06-13 22:37:41.321421
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:37:49.971543
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class PluginA:
        pass

    class PluginB:
        pass

    PluginC = PluginA

    plugins = PluginManager()
    plugins.register(PluginA, PluginB, PluginC)
    assert plugins.filter() == [PluginA, PluginB, PluginC]
    assert plugins.filter(PluginA) == [PluginA, PluginC]



# Generated at 2022-06-13 22:37:52.051521
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager =  PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager


# Generated at 2022-06-13 22:37:53.213625
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter(by_type=BasePlugin) == []



# Generated at 2022-06-13 22:37:55.563603
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.load_installed_plugins()

    formatters = manager.get_formatters_grouped()

    assert 'Colors' in formatters
    assert len(formatters) == 2

# Generated at 2022-06-13 22:37:58.234074
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # make an instance of PluginManager
    manager = PluginManager()
    manager.append(FormatterPlugin)
    manager.append(FormatterPlugin)
    manager.append(FormatterPlugin)
    manager.append(FormatterPlugin)
    # call the function get_formatters_grouped in manager
    manager.get_formatters_grouped()

# Generated at 2022-06-13 22:38:08.403719
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins import AuthPlugin
    from httpie.plugins.auth.basic import BasicAuthPlugin
    from httpie.plugins.auth.digest import DigestAuthPlugin
    from httpie.plugins.auth.hawk import HawkAuthPlugin
    plugin_manager = PluginManager()
    plugin_manager.register(BasicAuthPlugin, DigestAuthPlugin, HawkAuthPlugin)
    plugin_manager.get_auth_plugin_mapping()
    assert plugin_manager.get_auth_plugin_mapping() == {
        'basic': BasicAuthPlugin,
        'digest': DigestAuthPlugin,
        'hawk': HawkAuthPlugin
    }

# Generated at 2022-06-13 22:38:09.796487
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    a = PluginManager()
    a.load_installed_plugins()
    assert(a)



# Generated at 2022-06-13 22:38:12.766091
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pluginmanager = PluginManager()
    pluginmanager.load_installed_plugins()
    assert len(pluginmanager) > 0
    assert len(pluginmanager.get_auth_plugins()) > 0
    assert len(pluginmanager.get_formatters()) > 0
    assert len(pluginmanager.get_converters()) > 0
    assert len(pluginmanager.get_transport_plugins()) > 0

# Generated at 2022-06-13 22:38:18.239220
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin.formatters.json import JSONFormatter
    from httpie.plugins.builtin.formatters.prettyjson import PrettyJSONFormatter
    from httpie.plugins.builtin.formatters.colors import Formatter
    pluginManager = PluginManager()
    pluginManager.register(JSONFormatter, PrettyJSONFormatter, Formatter)
    assert pluginManager.get_formatters_grouped() == {
        None: [Formatter],
        'json': [JSONFormatter, PrettyJSONFormatter],
        'syntax': [JSONFormatter, PrettyJSONFormatter],
    }

# Generated at 2022-06-13 22:38:26.360953
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class FakeFormatterPlugin(FormatterPlugin):
        group_name = 'fake'
    class RealFormatterPlugin(FormatterPlugin):
        group_name = 'real'
    class RealFormatterPlugin2(FormatterPlugin):
        group_name = 'real'

    plugins = PluginManager()
    plugins.register(FakeFormatterPlugin, RealFormatterPlugin, RealFormatterPlugin2)
    assert plugins.get_formatters_grouped() == {
        'fake': [FakeFormatterPlugin],
        'real': [RealFormatterPlugin, RealFormatterPlugin2],
    }


# Generated at 2022-06-13 22:38:35.645114
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()


# Generated at 2022-06-13 22:38:40.572463
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    This unit test is used to test the method of 'get_formatters_grouped' of class 'PluginManager'
    :return: None
    """
    pm = PluginManager()
    pm.load_installed_plugins()
    print(pm.get_formatters_grouped())



# Generated at 2022-06-13 22:38:42.815986
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert len(plugins) == len(ENTRY_POINT_NAMES)

# Generated at 2022-06-13 22:38:49.835368
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin
    from httpie.plugins import TransportPlugin

    plugins = PluginManager()
    plugins.register(AuthPlugin)
    plugins.register(ConverterPlugin)
    plugins.register(FormatterPlugin)
    plugins.register(TransportPlugin)
    assert len(plugins.filter()) == 4
    assert len(plugins.filter(AuthPlugin)) == 1
    assert len(plugins.filter(ConverterPlugin)) == 1
    assert len(plugins.filter(FormatterPlugin)) == 1
    assert len(plugins.filter(TransportPlugin)) == 1

    assert len([plugin for plugin in plugins.filter(Type[BasePlugin])]) == len(plugins)
    assert len([plugin for plugin in plugins.filter(Type[AuthPlugin])]) == len(plugins.filter(AuthPlugin))


# Generated at 2022-06-13 22:39:02.578168
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    class OneFormatterPlugin(FormatterPlugin):
        group_name = 'one'

    class AnotherFormatterPlugin(FormatterPlugin):
        group_name = 'another'

    class YetAnotherFormatterPlugin(FormatterPlugin):
        group_name = 'yet_another'

    class YetYetAnotherFormatterPlugin(FormatterPlugin):
        group_name = 'yet_another'

    plugin_manager = PluginManager()
    plugin_manager.register(
        OneFormatterPlugin,
        AnotherFormatterPlugin,
        YetAnotherFormatterPlugin,
        YetYetAnotherFormatterPlugin,
    )

# Generated at 2022-06-13 22:39:07.738888
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    class Formatter1(FormatterPlugin):
        group_name = 'formatter1'

    class Formatter2(FormatterPlugin):
        group_name = 'formatter2'

    class Formatter3(FormatterPlugin):
        group_name = 'formatter1'

    plugin_manager = PluginManager()
    plugin_manager.register(Formatter1, Formatter2, Formatter3)
    assert plugin_manager.get_formatters_grouped() == {'formatter1': [Formatter1, Formatter3],
                                                       'formatter2': [Formatter2]}


plugin_manager = PluginManager()
plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:39:12.143903
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) == 4
    assert len(plugin_manager.get_formatters()) == 4
    assert len(plugin_manager.get_converters()) == 1
    assert len(plugin_manager.get_transport_plugins()) == 1

# Generated at 2022-06-13 22:39:18.957085
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PM = PluginManager()
    PM.load_installed_plugins()

# Generated at 2022-06-13 22:39:22.305945
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin
    from httpie.plugins.base import BasePlugin, TransportPlugin
    from httpie.plugins.manager import PluginManager
    from httpie.plugins.tests.helpers import MockAuthPlugin

    class MockFormatterPlugin(FormatterPlugin):
        name = 'MockFormatterPlugin'

    class MockConverterPlugin(ConverterPlugin):
        name = 'MockConverterPlugin'

    class MockTransportPlugin(TransportPlugin):
        name = 'MockTransportPlugin'

    class MockPlugin(BasePlugin):
        name = 'MockPlugin'

    plugins = PluginManager()
    plugins.register(MockAuthPlugin, MockFormatterPlugin, MockConverterPlugin,
                     MockTransportPlugin, MockPlugin)
    print(plugins)

    # Test

# Generated at 2022-06-13 22:39:28.039753
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    class A(BasePlugin):
        pass
    class B(BasePlugin):
        pass
    plugin_manager.register(A, B)
    assert plugin_manager.filter(A) == [A]
    assert plugin_manager.filter(B) == [B]
    assert plugin_manager.filter(BasePlugin) == [A, B]


# Generated at 2022-06-13 22:39:50.100384
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    p = PluginManager()
    p.register(FormatterPlugin)
    print(p.get_formatters_grouped())

if __name__ == '__main__':
    p = PluginManager()
    p.register(FormatterPlugin)
    print(p.get_formatters_grouped())
    #test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:39:56.014855
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()

    assert len(manager.get_auth_plugin_mapping()) > 0
    assert len(manager.get_formatters_grouped()) > 0
    assert len(manager.get_converters()) > 0
    assert len(manager.get_transport_plugins()) > 0



# Generated at 2022-06-13 22:40:01.876385
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    group_1 = [FormatterPlugin]
    group_2 = [FormatterPlugin]
    manager = PluginManager()
    manager.register(*group_1, *group_2)
    result = manager.get_formatters_grouped()
    assert result == {'format': group_1, 'format_group': group_2}



# Generated at 2022-06-13 22:40:09.473205
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import TransportPlugin
    from httpie.compat import is_windows
    from httpie.plugins.base import create_auth_plugin
    pm = PluginManager()
    pm.load_installed_plugins()
    assert isinstance(pm, list)
    epoint = pm[-1]
    assert isinstance(epoint, TransportPlugin)
    assert is_windows() or epoint.__class__.__name__ == 'UnixSocketHTTPAdapter'


# Generated at 2022-06-13 22:40:17.387104
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    # Create mock instance of auth plugin
    class MockAuthPlugin(AuthPlugin):
        auth_type = "test"
        auth_plugin_name = "test"
        description = "test"
        auth_parse = lambda _, r: r

    # Create mock instance of PluginManager
    new_manager = PluginManager()
    new_manager.register(MockAuthPlugin)

    # Test if mock plugin is correctly returned
    plugin_map = new_manager.get_auth_plugin_mapping()
    assert(plugin_map["test"] == MockAuthPlugin)


# Generated at 2022-06-13 22:40:19.831587
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager)


# Generated at 2022-06-13 22:40:23.898543
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager.get_auth_plugins()) > 0
    assert len(plugin_manager.get_formatters()) > 0
    assert len(plugin_manager.get_transport_plugins()) > 0
    assert len(plugin_manager.get_converters()) > 0

# Generated at 2022-06-13 22:40:25.900975
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.load_installed_plugins()
    actual = pm.get_auth_plugin_mapping()
    assert actual['basic']
    assert actual['digest']

# Generated at 2022-06-13 22:40:41.221706
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    p = PluginManager()
    p.load_installed_plugins()

# Generated at 2022-06-13 22:40:45.939474
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    class A: pass
    class B(A): pass
    class C(A): pass
    class D: pass
    plugin_manager.register(B, C, D)
    assert plugin_manager.filter(A) == [B, C]
    assert plugin_manager.filter(D) == [D]
    assert plugin_manager.filter() == [B, C, D]
    

# Generated at 2022-06-13 22:41:38.721589
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin, TransportPlugin)
    assert plugin_manager.filter(by_type=TransportPlugin) == [TransportPlugin]
    assert plugin_manager.filter(by_type=AuthPlugin) == [AuthPlugin]
    assert plugin_manager.filter(by_type=BasePlugin) == [AuthPlugin, TransportPlugin]


# Generated at 2022-06-13 22:41:42.609282
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    result = True
    for entry_point in iter_entry_points(ENTRY_POINT_NAMES[0]):
         plugin = entry_point.load()
         if not isinstance(plugin, AuthPlugin):
             result = False
    return result

# Generated at 2022-06-13 22:41:57.748423
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # This test would fail if not run from "project root" directory (e.g. from
    # "test" directory).
    pm = PluginManager()

    # Test if plugins are correctly loaded from entry_points
    pm.load_installed_plugins()
    assert len(pm) >= 1

    # Test if only httpie plugins are loaded
    assert all(isinstance(plugin, BasePlugin) for plugin in pm)

    # Test if it is possible to unregister plugins
    plugin = pm[0]
    pm.unregister(plugin)
    assert plugin not in pm

    # Test if it is possible to register plugins
    pm.register(plugin)
    assert plugin in pm

    # Test if it is possible to filter out plugins by type
    formatters = pm.filter(FormatterPlugin)

# Generated at 2022-06-13 22:42:00.617587
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    return pm


# Generated at 2022-06-13 22:42:02.975711
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins


plugin_manager = PluginManager()
plugin_manager.load_installed_plugins()

# Generated at 2022-06-13 22:42:05.348641
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager
    print(plugin_manager)



# Generated at 2022-06-13 22:42:09.411366
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = [
        PluginA,
        PluginAB,
        PluginABC,
        PluginB,
        PluginC
    ]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)
    formatters_grouped = plugin_manager.get_formatters_grouped()
    assert formatters_grouped == expected_formatters_grouped


# Generated at 2022-06-13 22:42:19.864198
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pl = PluginManager()
    pl.load_installed_plugins()
    print('\n', pl, '\n')
    print('\n', pl.get_auth_plugin_mapping(), '\n')
    print('\n', pl.get_converters(), '\n')
    print('\n', pl.get_auth_plugins(), '\n')
    print('\n', pl.get_transport_plugins(), '\n')
    print('\n', pl.get_formatters(), '\n')
    print('\n', pl.get_formatters_grouped(), '\n')

plugins = PluginManager()

# Generated at 2022-06-13 22:42:25.991963
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(a1, a2, a3, a4, a5, a6)
    assert plugins.get_formatters_grouped() == {"group_a": [a1, a4, a5], "group_b": [a2, a3, a6]}


# Test cases

# Generated at 2022-06-13 22:42:26.923702
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    PluginManager.register("A","B")