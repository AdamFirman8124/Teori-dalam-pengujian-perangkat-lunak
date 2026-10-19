

# Generated at 2022-06-13 22:33:14.104587
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    assert len(plugin_manager) == 0
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0


# Generated at 2022-06-13 22:33:17.420977
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
	manager = PluginManager()
	manager.register(BasePlugin)
	manager.filter()[0].__name__ == 'BasePlugin'


# Generated at 2022-06-13 22:33:18.590993
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert 'PluginManager' != None

# Generated at 2022-06-13 22:33:23.219132
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager, mock_iter_entry_points = \
        _load_installed_plugins_mock(return_value=[])
    plugin_manager.register(AuthPlugin)  # Prevent an empty list

    plugin_manager.load_installed_plugins()

    assert mock_iter_entry_points.called



# Generated at 2022-06-13 22:33:29.168842
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin, HTTPFormatterPlugin, StreamFormatterPlugin
    class DummyFormatterPlugin(BasePlugin):
        group_name = 'Dummy Formatters'
    plugins = PluginManager()
    plugins.register(JSONFormatterPlugin, HTTPFormatterPlugin, DummyFormatterPlugin, StreamFormatterPlugin)
    assert plugins.get_formatters_grouped() == {'Dummy Formatters': [DummyFormatterPlugin], 'Formatters': [JSONFormatterPlugin, HTTPFormatterPlugin], 'Streaming Formatters': [StreamFormatterPlugin]}

# Generated at 2022-06-13 22:33:33.712919
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm) > 0
    assert all(
        issubclass(plugin, BasePlugin)
        for plugin in pm
    )

# Generated at 2022-06-13 22:33:43.964878
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plg_mngr = PluginManager()
    #load all plugins
    plg_mngr.load_installed_plugins()

    #create a dict with group_name and number of items
    dict_grouped_num = {}
    for group in plg_mngr.get_formatters_grouped():
        dict_grouped_num[group] = len(plg_mngr.get_formatters_grouped()[group])

    assert dict_grouped_num['JS, HTML, XML, Markdown'] == 1
    assert dict_grouped_num['Single-line'] == 2
    assert dict_grouped_num['Table'] == 2
    assert dict_grouped_num['TTY'] == 1

# Generated at 2022-06-13 22:33:50.194333
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert plugin_manager.get_auth_plugins()
    assert plugin_manager.get_formatters()
    assert plugin_manager.get_converters()
    assert plugin_manager.get_transport_plugins()

# Generated at 2022-06-13 22:33:58.469034
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.register(TestAuthPlugin1, TestAuthPlugin2)
    plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert "authtype1" in plugin_mapping
    assert "authtype2" in plugin_mapping
    assert isinstance(plugin_mapping["authtype1"], TestAuthPlugin1)
    assert isinstance(plugin_mapping["authtype2"], TestAuthPlugin2)

# Generated at 2022-06-13 22:34:09.794849
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from pluginmanager.list_installed_packages import list_installed_packages
    from pluginmanager.load_installed_plugins import load_installed_plugins
    from pluginmanager.unzip_package import unzip_package
    from pluginmanager.download_package import download_package
    def check(p_name,p_version):
        download_package(p_name,p_version)
        unzip_package(p_name)
        assert p_name in list_installed_packages()
        load_installed_plugins()
        assert 'httpie.plugins.transport' in list_installed_packages()
    
    p_name_list=['httpie-edgegrid']
    p_version_list=['0.2.1']

# Generated at 2022-06-13 22:34:23.573358
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    import httpie.plugins.auth.aws
    import httpie.plugins.auth.basic
    import httpie.plugins.auth.digest
    import httpie.plugins.auth.hawk
    import httpie.plugins.auth.jwt
    import httpie.plugins.auth.oauth1
    import httpie.plugins.auth.oauth2
    import httpie.plugins.auth.ntlm
    # Create a PluginManager Object
    pm = PluginManager()

# Generated at 2022-06-13 22:34:28.831551
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPlugin(BasePlugin):
        name = 'test'
        description = ''
        auth_required = False

    plugin_manager = PluginManager()
    test_plugin = TestPlugin()
    plugin_manager.register(test_plugin)

    assert plugin_manager.filter(by_type=TestPlugin)[0] == TestPlugin



# Generated at 2022-06-13 22:34:34.575289
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_mgr = PluginManager()
    plugin_mgr.load_installed_plugins()
    print(plugin_mgr)
    assert len(plugin_mgr) == 2

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:34:37.385132
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager.get_formatters_grouped())

test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:34:48.353479
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class TestPlugin1(BasePlugin):
        pass

    class TestPlugin2(TestPlugin1):
        pass

    class TestPlugin3(TestPlugin1):
        pass

    class TestPlugin4(TestPlugin2):
        pass

    manager = PluginManager()
    manager.register(TestPlugin1, TestPlugin2, TestPlugin3, TestPlugin4)

    assert manager.filter(by_type=TestPlugin1) == [TestPlugin1, TestPlugin2, TestPlugin3, TestPlugin4]
    assert manager.filter(by_type=TestPlugin2) == [TestPlugin2, TestPlugin4]
    assert manager.filter(by_type=TestPlugin3) == [TestPlugin3]
    assert manager.filter(by_type=TestPlugin4) == [TestPlugin4]

# Generated at 2022-06-13 22:34:56.449501
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import json_formatter as json
    from httpie.plugins import pretty_formatter as pretty
    p = PluginManager()
    p.register(json.JSONFormatter)
    p.register(pretty.PrettyFormatter)
    assert p.get_formatters_grouped() == {'JSON': [json.JSONFormatter]}
    assert p.get_formatters_grouped() != {'JSON': [json.JSONFormatter]}


# Generated at 2022-06-13 22:35:07.794149
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.plugins.basic_auth import BasicAuthPlugin
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.builtin import HTTPiePlugin
    from httpie.plugins.keyboard import KeyboardAuthPlugin
    from httpie.plugins.json import JSONBodyPlugin

    # Create a mock plugin manager
    plugin_manager = PluginManager()
    plugin_manager.register(HTTPBasicAuth, HTTPiePlugin, KeyboardAuthPlugin,  BasicAuthPlugin, JSONBodyPlugin)

    # Test 
    auth_plugins = plugin_manager.filter(AuthPlugin)
    assert len(auth_plugins) == 3
    assert auth_plugins == [HTTPBasicAuth, KeyboardAuthPlugin, BasicAuthPlugin]
    auth_plugins = plugin_manager.filter(AuthPlugin)

    formatter_plugins = plugin_manager.filter(FormatterPlugin)


# Generated at 2022-06-13 22:35:20.253826
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin, PrettyFormatterPlugin
    plugin_manager = PluginManager()
    plugin_manager.register(JSONFormatterPlugin)
    plugin_manager.register(PrettyFormatterPlugin)
    group_dict = plugin_manager.get_formatters_grouped()
    assert "builtin" in group_dict.keys()
    assert "Output formatters" in group_dict.keys()
    assert "JSON" in group_dict.keys()
    assert "Builtin" in group_dict.keys()
    assert "Input formatters" in group_dict.keys()
    assert "Pretty" in group_dict.keys()
    assert "HTML" in group_dict.keys()


plugins = PluginManager()

# Load the built-in plugins.

# Generated at 2022-06-13 22:35:27.904353
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # fixture
    plugin_manager = PluginManager()
    # test
    plugin_manager.load_installed_plugins()
    # check
    assert len(plugin_manager) == 2
    assert len(plugin_manager.get_auth_plugins()) == 1
    assert len(plugin_manager.get_formatters()) == 1
    assert plugin_manager[0]
    assert plugin_manager[1]


# Generated at 2022-06-13 22:35:36.218981
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    plugin = plugin_manager.get_auth_plugin_mapping()
    assert plugin == {'basic': httpie.plugins.BasicAuthPlugin,
                      'bearer': httpie.plugins.BearerAuthPlugin,
                      'digest': httpie.plugins.DigestAuthPlugin,
                      'hmac': httpie.plugins.HmacAuthPlugin,
                      'hawk': httpie.plugins.HawkAuthPlugin,
                      'oauth1': httpie.plugins.OAuth1Plugin,
                      'oauth2': httpie.plugins.OAuth2Plugin}

# Generated at 2022-06-13 22:35:47.353148
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():

    class test_json:
        group_name = 'json'

    class test_form:
        group_name = 'form'

    test_mgr = PluginManager()
    test_mgr.register(test_json, test_form)

    test_result = test_mgr.get_formatters_grouped()
    assert test_result['json'] == [test_json]
    assert test_result['form'] == [test_form]

# Generated at 2022-06-13 22:35:51.424821
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.register(MyAuthPlugin)
    assert pm.get_auth_plugin_mapping() == {
        'myauth': MyAuthPlugin
    }



# Generated at 2022-06-13 22:35:54.872870
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    a = PluginManager()
    a.register(list)
    a.register(str)
    a.register(int)
    assert len(a.filter(BasePlugin)) == 3

# Generated at 2022-06-13 22:35:59.282320
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    instance = PluginManager()
    instance.register(BASICAuthPlugin)
    instance.register(DigestAuthPlugin)
    assert instance.get_auth_plugin_mapping() == {
        'basic': BASICAuthPlugin,
        'digest': DigestAuthPlugin
    }

# Generated at 2022-06-13 22:36:07.942084
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class Plugin1(FormatterPlugin):
        group_name = 'group1'
    class Plugin2(FormatterPlugin):
        group_name = 'group2'
    class Plugin3(FormatterPlugin):
        group_name = 'group1'
    plugins = PluginManager([Plugin1, Plugin2, Plugin3])
    assert plugins.get_formatters_grouped() == {'group1': [Plugin1, Plugin3], 'group2': [Plugin2]}

# Generated at 2022-06-13 22:36:11.756710
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie import plugins
    plugins.manager = PluginManager()
    plugins.manager.load_installed_plugins()
    print(plugins.manager)

# Generated at 2022-06-13 22:36:23.358428
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():  # noqa
    from httpie import __version__
    from httpie.plugins import AuthPlugin, TransportPlugin

    from httpie.plugins.builtin import AuthBasicPlugin, DigestAuthPlugin
    from httpie.plugins.builtin import LocalhostAuthPlugin
    from httpie.plugins.builtin import HTTPGzipAuthPlugin, HTTPJsonPlugin
    from httpie.plugins.builtin \
            import HTTPAWSAuthPlugin, HTTPAuthPlugin, HTTPBearerAuthPlugin
    from httpie.plugins.builtin \
            import HTTPBearerTokenAuthPlugin, HTTPBasicAuthPlugin
    from httpie.plugins.builtin import HTTPDigestAuthPlugin
    from httpie.plugins.builtin import HTTPDefaultTransportPlugin
    from httpie.plugins.builtin import HTTPFallbackTransportPlugin

# Generated at 2022-06-13 22:36:30.268427
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.register(AuthPlugin, FormatterPlugin)
    print(manager.filter(Type[BasePlugin]))  # [<class '__main__.AuthPlugin'>, <class '__main__.FormatterPlugin'>]
    # print(manager.filter(Type[AuthPlugin]))  # [<class '__main__.AuthPlugin'>]
    # print(manager.filter(Type[FormatterPlugin]))  # [<class '__main__.FormatterPlugin'>]


# test_PluginManager_filter()



# Generated at 2022-06-13 22:36:32.048594
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) > 0

# Generated at 2022-06-13 22:36:32.917290
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert issubclass(PluginManager.filter, list)

# Generated at 2022-06-13 22:36:42.297464
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    PluginManager_instance = PluginManager()
    print(PluginManager_instance.get_formatters_grouped())



# Generated at 2022-06-13 22:36:47.511356
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.load_installed_plugins()

# Generated at 2022-06-13 22:36:53.664714
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PluginManager1 = PluginManager()
    PluginManager1.register(AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin)
    PluginManager1.load_installed_plugins()
    assert PluginManager1.filter(AuthPlugin) == PluginManager1.get_auth_plugins()
    assert PluginManager1.filter(AuthPlugin) == [plugin for plugin in PluginManager1 if issubclass(plugin, AuthPlugin)]
    assert PluginManager1.filter(BasePlugin) == [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]



# Generated at 2022-06-13 22:36:55.254636
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    assert PluginManager().filter() == []


# Generated at 2022-06-13 22:37:09.532914
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from datetime import datetime, timezone
    from httpie.core import std_headers
    from httpie.plugins import builtin
    from httpie.plugins.builtin import HTTPHeaders, JSON, RawJSON
    from httpie.plugins.internal import base_v1
    from httpie.plugins.json import JSONFlow
    from httpie.plugins.json.pretty import PrettyJSON
    from httpie.plugins.json.stream import StreamJSON
    from httpie.plugins.json.stream_pretty import StreamPrettyJSON
    from httpie.plugins.text import HTML, JavaScript
    from httpie.plugins.text.flow import FlowFormatter
    from httpie.plugins.text.stream import StreamFormatter
    plugins = PluginManager()

# Generated at 2022-06-13 22:37:16.828080
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    # The first time when running this test, there are 19 authentication plugins,
    # 71 converters, 3 formatters and 2 transports,
    # so we assert the length of plugins to be 95.
    # The second time, the length of plugins should be 95 still.
    assert len(plugins) == 95


# Generated at 2022-06-13 22:37:20.292607
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert PluginManager().get_formatters_grouped() == {}

PluginManager = PluginManager()

# Generated at 2022-06-13 22:37:24.404575
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    obj = PluginManager()
    obj.load_installed_plugins()
    assert issubclass(obj[0], BasePlugin)
    assert issubclass(obj[0], AuthPlugin)


# Generated at 2022-06-13 22:37:30.620098
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Mock plugin manager
    plugin_manager = PluginManager()

    # Mock plugin_manager.register()
    def mock_register(*plugins):
        for plugin in plugins:
            plugin_manager.append(plugin)

    plugin_manager.register = mock_register

    # Mock iter_entry_points()
    class MockEntryPoint:
        # Mock entry_point.load()
        def load(self):
            class MockPlugin:
                package_name = 'mocked package'

            return MockPlugin

        # Mock entry_point.dist.key
        dist = MockEntryPoint()

    def mock_iter_entry_points(entry_point_name):
        return [MockEntryPoint()]

    iter_entry_points = mock_iter_entry_points

    # Test load_installed_plugins()
    plugin_manager.load_installed_plugins

# Generated at 2022-06-13 22:37:39.401364
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # Arrange
    plugin_manager = PluginManager()
    class BasePluginB(BasePlugin):
        pass

    class ChildPluginA(BasePluginB):
        pass

    class ChildPluginB(BasePluginB):
        pass

    class ChildPluginC(BasePlugin):
        pass

    plugin_manager.register(ChildPluginA, ChildPluginB, ChildPluginC)
    # Act
    filter_result = plugin_manager.filter(by_type=BasePluginB)
    # Assert
    assert len(filter_result) == 2
    assert [type(plugin) for plugin in filter_result] == [ChildPluginA, ChildPluginB]

# Generated at 2022-06-13 22:37:57.319830
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class foo(BasePlugin):
        pass
    class bar(BasePlugin):
        pass
    class blah(foo):
        pass
    plugins = PluginManager()
    plugins.register(foo, foo, bar, blah)
    assert plugins.filter(foo) == [foo, foo, blah]
    assert plugins.filter(bar) == [bar]
    assert plugins.filter() == []

# Generated at 2022-06-13 22:38:02.303475
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(FormatterPlugin, FormatterPlugin)
    assert plugin_manager.get_formatters_grouped() == \
           {'formatter': [FormatterPlugin, FormatterPlugin]}


# Generated at 2022-06-13 22:38:09.936610
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()

    # Test for empty list
    plugin_manager.load_installed_plugins()

    assert plugin_manager.get_auth_plugins()
    assert not plugin_manager.get_auth_plugin_mapping()

    assert plugin_manager.get_formatters()
    assert plugin_manager.get_formatters_grouped()
    assert plugin_manager.get_converters()

    assert plugin_manager.get_transport_plugins()

# Generated at 2022-06-13 22:38:13.575994
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
  plugin_manager = PluginManager()
  plugin_manager.load_installed_plugins()
  assert plugin_manager.get_formatters_grouped() == {
    'group1': [HttpiePlugin],
    'group2': [
      HttpiePlugin,
      HttpiePlugin,
      HttpiePlugin,
      HttpiePlugin,
      HttpiePlugin,
    ],
    'group3': [HttpiePlugin],
    'group4': [HttpiePlugin],
  }

# Generated at 2022-06-13 22:38:18.498810
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(Plugin1, Plugin2)
    assert plugins.get_formatters_grouped() == {'Group 1': [Plugin1], 'Group 2': [Plugin2]}

# Generated at 2022-06-13 22:38:21.961553
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    pm = PluginManager()
    pm.load_installed_plugins()
    p = pm.get_auth_plugin_mapping()
    assert type(p) is dict and p != {}


# Generated at 2022-06-13 22:38:24.283807
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) != 0



# Generated at 2022-06-13 22:38:25.219068
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager.load_installed_plugins()

# Generated at 2022-06-13 22:38:31.372202
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.register(1)
    manager.register(2)
    manager.register(3)
    manager.register(4)
    manager.register(5)
    assert manager.filter(0) == [0]


# Generated at 2022-06-13 22:38:35.373588
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    pm = PluginManager()
    pm.load_installed_plugins()
    assert len(pm.filter(TransportPlugin)) == 0
    assert len(pm.filter(ConverterPlugin)) == 0
    assert len(pm.filter(FormatterPlugin)) == 0
    assert len(pm.filter(AuthPlugin)) == 0


# Generated at 2022-06-13 22:39:09.904566
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.builtin import PrettyFormatterPlugin
    pm = PluginManager([JSONFormatterPlugin, PrettyFormatterPlugin])
    formatters = pm.get_formatters_grouped()
    assert formatters['Built-in'][0] == JSONFormatterPlugin
    assert formatters['Built-in'][1] == PrettyFormatterPlugin



# Generated at 2022-06-13 22:39:18.956453
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class AuthPlugin:
        id = 'auth'
    class ConverterPlugin:
        id = 'converter'
    class FormatterPlugin:
        id = 'formatter'
    class TransportPlugin:
        id = 'transport'
    class Plugin:
        pass
    plugins = [Plugin, Plugin, AuthPlugin, AuthPlugin, ConverterPlugin, TransportPlugin]
    plugin_manager = PluginManager()
    plugin_manager.register(*plugins)
    auth_plugins = plugin_manager.filter(AuthPlugin)
    converter_plugins = plugin_manager.filter(ConverterPlugin)
    formatter_plugins = plugin_manager.filter(FormatterPlugin)
    transport_plugins = plugin_manager.filter(TransportPlugin)
    all_plugins = plugin_manager.filter()
    assert len(auth_plugins) == 2

# Generated at 2022-06-13 22:39:29.763399
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatterPlugin
    from httpie.plugins.base import Group, FormatterPlugin
    result = PluginManager().get_formatters_grouped()
    # Unit test for keys of get_formatters_grouped
    assert result.keys() == {'Default', 'Syntax', 'Other'}
    # Unit test for value of 'Default' key of get_formatters_grouped
    assert result['Default'] == []
    # Unit test for value of 'Syntax' key of get_formatters_grouped
    assert result['Syntax'] == []
    # Unit test for value of 'Other' key of get_formatters_grouped
    assert result['Other'] == [JSONFormatterPlugin]
    # Unit test for method get_formatters_grouped of class PluginManager

# Generated at 2022-06-13 22:39:35.159719
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(
        Type[FormatterPlugin],
        Type[FormatterPlugin],
        Type[FormatterPlugin],
        Type[FormatterPlugin],
        Type[FormatterPlugin],
    )

    assert len(plugin_manager.get_formatters_grouped()) == 0



# Generated at 2022-06-13 22:39:36.904466
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager_object = PluginManager()
    plugin_manager_object.test_plugin2()


# Generated at 2022-06-13 22:39:40.362970
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import FormatterPlugin, CLIFormatter
    plugins = PluginManager()
    plugins.register(CLIFormatter)
    assert plugins.get_formatters_grouped() == {'cli': [CLIFormatter]}
    plugins.unregister(CLIFormatter)
    assert plugins.get_formatters_grouped() == {}


# Generated at 2022-06-13 22:39:43.376485
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    assert plugins

# Generated at 2022-06-13 22:39:47.312354
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    result = plugin_manager.get_auth_plugin_mapping()
    assert result is not None, "the get_auth_plugin_mapping is not None"



# Generated at 2022-06-13 22:39:51.645186
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    import httpie
    pm = PluginManager()
    pm.load_installed_plugins()
    print(pm)
    assert len(pm) == 1
    # print(pm.__dir__)


# Generated at 2022-06-13 22:39:52.684533
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    assert PluginManager


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:40:56.612683
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    PluginManager.register(AuthPlugin)
    assert PluginManager.filter(AuthPlugin) is not 0
    assert PluginManager.filter(ConverterPlugin) is 0
    assert PluginManager.filter(FormatterPlugin) is 0
    assert PluginManager.filter(TransportPlugin) is 0
    assert PluginManager.filter(BasePlugin) is not 0
    assert PluginManager.filter(BasePlugin) is not 0

test_PluginManager_filter()

# Generated at 2022-06-13 22:41:05.421481
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()

    class Formatter1(FormatterPlugin):
        group_name = 'type1'

    class Formatter2(FormatterPlugin):
        group_name = 'type2'

    class Formatter3(FormatterPlugin):
        group_name = 'type2'

    manager.register(Formatter1, Formatter2, Formatter3)

    formatters_grouped = manager.get_formatters_grouped()

    assert formatters_grouped == {
        'type1': [Formatter1],
        'type2': [Formatter2, Formatter3],
    }


plugins = PluginManager()
plugins.load_installed_plugins()

# Generated at 2022-06-13 22:41:14.219991
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    import mock
    import pytest
    from httpie.plugins import AuthPlugin, TransportPlugin

    # Arrange
    entry_point_name = 'httpie.plugins.auth.v1'
    auth_plugin_1 = mock.MagicMock(spec=AuthPlugin)
    auth_plugin_1.auth_type = 'foo'
    auth_plugin_2 = mock.MagicMock(spec=AuthPlugin)
    auth_plugin_2.auth_type = 'bar'
    transport_plugin = mock.MagicMock(spec=TransportPlugin)
    entry_point_1 = mock.MagicMock()
    entry_point_1.load.return_value = auth_plugin_1
    entry_point_2 = mock.MagicMock()
    entry_point_2.load.return_value = auth_plugin_2
   

# Generated at 2022-06-13 22:41:24.155106
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    # assert PluginManager().filter(FormatterPlugin)==[]
    #
    # assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]
    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]
    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]
    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]
    assert PluginManager().filter(FormatterPlugin)==[]

    assert PluginManager().filter(FormatterPlugin)==[]

# Generated at 2022-06-13 22:41:34.490181
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class PluginA(BasePlugin):
        pass

    class PluginB(BasePlugin):
        pass

    class PluginC(BasePlugin):
        pass

    class PluginD(PluginB):
        pass

    class PluginE(PluginB):
        pass

    plugin_manager = PluginManager()
    plugin_manager.register(PluginA, PluginB, PluginC, PluginD, PluginE)

    assert plugin_manager.filter(PluginA) == [PluginA]
    assert plugin_manager.filter(PluginB) == [PluginB, PluginD, PluginE]
    assert plugin_manager.filter(PluginC) == [PluginC]
    assert plugin_manager.filter(BasePlugin) == [PluginA, PluginB, PluginC, PluginD, PluginE]

# Generated at 2022-06-13 22:41:43.092467
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    assert plugin_manager.get_formatters_grouped() == {}
    plugin_manager.register(json.JsonFormatter, json.JsonPrettyFormatter)
    assert plugin_manager.get_formatters_grouped() == {'JSON': [json.JsonFormatter, json.JsonPrettyFormatter]}
    plugin_manager.register(json.JsonPrettyFormatter)
    assert plugin_manager.get_formatters_grouped() == {'JSON': [json.JsonFormatter, json.JsonPrettyFormatter]}
    plugin_manager.register(JsonQueryFormatter)

# Generated at 2022-06-13 22:41:47.791939
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    actual = PluginManager()
    actual.load_installed_plugins()
    assert len(actual.get_formatters_grouped()) == 3

# Generated at 2022-06-13 22:42:01.690984
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    pm = PluginManager()
    pm.load_installed_plugins()

    formatters = pm.get_formatters_grouped()
    assert formatters.keys() == {'Formatting', 'Syntax highlighting'}

# Generated at 2022-06-13 22:42:04.523012
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(FormatterPlugin)
    plugins.register(FormatterPlugin)
    plugins.register(FormatterPlugin)
    assert len(plugins.get_formatters_grouped()) == 0

# Generated at 2022-06-13 22:42:07.804289
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()
    
    assert plugins.get_auth_plugins()
    assert plugins.get_formatters()
    assert plugins.get_converters()
    assert plugins.get_transport_plugins()