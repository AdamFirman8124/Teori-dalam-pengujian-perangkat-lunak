

# Generated at 2022-06-13 22:33:21.052396
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    formatters_grouped = plugin_manager.get_formatters_grouped()
    assert formatters_grouped["Skip"] == [httpie.plugins.formatter.skip.SkipFormatter]



# Generated at 2022-06-13 22:33:22.025297
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert (PluginManager().get_formatters_grouped()
            == {'group': [], 'group-child': []})

# Generated at 2022-06-13 22:33:29.988404
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from data import EntryPoint

    manager = PluginManager()
    manager.register(EntryPoint.group1_1)
    manager.register(EntryPoint.group2_1)
    manager.register(EntryPoint.group2_2)
    manager.register(EntryPoint.group1_2)
    manager.register(EntryPoint.group1_1)

    out = manager.get_formatters_grouped()
    assert len(out) == 2
    assert EntryPoint.group1.group_name in out
    assert EntryPoint.group2.group_name in out

    assert len(out[EntryPoint.group1.group_name]) == 3
    assert len(out[EntryPoint.group2.group_name]) == 2
    assert EntryPoint.group1_1 in out[EntryPoint.group1.group_name]
    assert Entry

# Generated at 2022-06-13 22:33:42.785948
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie import ExitStatus
    from httpie.output.formats import Formatter
    from httpie.constants import DEFAULT_FORMAT
    from httpie import cli

    args = cli.parser.parse_args(args=[])

    # Initialize a PluginManager 
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # print(plugin_manager.get_formatters_grouped())

    HOME = os.path.abspath(gettempdir())
    CONFIG_DIR = os.path.join(HOME, '.httpie')
    CONFIG_PATH = os.path.join(CONFIG_DIR, 'config.json')

# Generated at 2022-06-13 22:33:45.473788
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    manager = PluginManager()
    manager.register(BasePlugin)
    #assert manager.filter(BasePlugin) == [BasePlugin]

# Generated at 2022-06-13 22:33:49.169205
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    assert len(plugins) == 0
    plugins.load_installed_plugins()
    assert len(plugins) > 0



# Generated at 2022-06-13 22:33:53.736539
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # Create a new PluginManager
    manager = PluginManager()

    # Check that the PluginManager contains plug-ins
    assert manager.load_installed_plugins() is None
    assert len(manager) > 0


# Generated at 2022-06-13 22:34:04.992779
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    import httpie.plugins.auth
    """
    1. test func get_auth_plugin_mapping, in this func we create a dict to store all the auth plugin,
    2. create a list to store the auth plugin which are not in the dict
    """
    plugin_mapping_auth = {}
    list_not_in_mapping = []
    list_subclass_auth = []
    list_subclass_auth_plugin = []

# Generated at 2022-06-13 22:34:06.446377
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    print(PluginManager().get_formatters_grouped())

# Generated at 2022-06-13 22:34:17.148750
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()

    assert plugin_manager.filter(Type[BasePlugin]) == []
    plugin_manager.register(AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin)
    assert plugin_manager.filter(Type[BasePlugin]) == [AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin]
    assert plugin_manager.filter(Type[AuthPlugin]) == [AuthPlugin]
    assert plugin_manager.filter(Type[FormatterPlugin]) == [FormatterPlugin]
    assert plugin_manager.filter(Type[ConverterPlugin]) == [ConverterPlugin]
    assert plugin_manager.filter(Type[TransportPlugin]) == [TransportPlugin]


# Generated at 2022-06-13 22:34:23.716835
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mgr = PluginManager()
    mgr.load_installed_plugins()
    return mgr


# Generated at 2022-06-13 22:34:28.895051
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class A():
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B):
        pass
    l = [B, C, D]
    pluginmanager = PluginManager()
    pluginmanager.register(B, C, D)
    assert pluginmanager.filter(A) == l

# Generated at 2022-06-13 22:34:39.871606
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    class FormatterPlugin_1(FormatterPlugin):
        group_name = 'test'
    class FormatterPlugin_2(FormatterPlugin):
        group_name = 'test'
    class FormatterPlugin_3(FormatterPlugin):
        group_name = 'test'
    class FormatterPlugin_4(FormatterPlugin):
        group_name = 'test1'
    class FormatterPlugin_5(FormatterPlugin):
        group_name = 'test1'
    class FormatterPlugin_6(FormatterPlugin):
        group_name = 'test1'
    manager.register(FormatterPlugin_1,FormatterPlugin_2,FormatterPlugin_3,FormatterPlugin_4,FormatterPlugin_5,FormatterPlugin_6)

# Generated at 2022-06-13 22:34:49.676622
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    # arrange 
    pm = PluginManager()
    # act 
    pm.load_installed_plugins()
    # assert
    # The PluginManager is currently working with a
    # hard-coded list of entry points
    assert len(ENTRY_POINT_NAMES) == len(pm)

# Generated at 2022-06-13 22:35:02.858434
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin = PluginManager()
    plugin.load_installed_plugins()
    auth_plugins=plugin.filter(AuthPlugin)
    assert isinstance(auth_plugins, list)

# Generated at 2022-06-13 22:35:10.619566
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.manager import PluginManager
    from httpie.plugins.builtin import JSONFormatter, XMLFormatter
    plugin_manager = PluginManager()
    plugin_manager.register(JSONFormatter, XMLFormatter)
    plugin_group={'HTTP':[JSONFormatter,XMLFormatter]}
    assert plugin_manager.get_formatters_grouped() == plugin_group 


# Generated at 2022-06-13 22:35:18.407033
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    # plugin_manager.register(TestPlugin)
    plugin_manager.load_installed_plugins()
    assert len(plugin_manager) == 4
    assert len(plugin_manager.get_auth_plugins()) == 1
    assert len(plugin_manager.get_formatters()) == 1
    assert len(plugin_manager.get_converters()) == 1
    assert len(plugin_manager.get_transport_plugins()) == 1



# Generated at 2022-06-13 22:35:22.758326
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins.register(BasePlugin)
    assert not plugins.filter(BasePlugin)
    assert plugins.filter()
    assert plugins.filter(BasePlugin, BasePlugin)
    assert isinstance(plugins.filter(BasePlugin)[0], BasePlugin)

# Generated at 2022-06-13 22:35:27.676058
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(MockFormatterPlugin1, MockFormatterPlugin2)
    formatters = manager.get_formatters_grouped()
    assert formatters['mock'] == [MockFormatterPlugin1, MockFormatterPlugin2]


# Generated at 2022-06-13 22:35:31.771174
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin1 = 'plugin1'
    plugin2 = 'plugin2'
    pm = PluginManager()
    pm.register(plugin1, plugin2)
    assert(pm.filter() == [plugin1, plugin2]) 


# Generated at 2022-06-13 22:35:42.064296
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.manager import PluginManager as PluginManager
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager.get_formatters_grouped())

test_PluginManager_get_formatters_grouped()

# Generated at 2022-06-13 22:35:43.796118
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    PluginManager.load_installed_plugins(PluginManager())

# Generated at 2022-06-13 22:35:52.538668
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class fakePlugin1(BasePlugin):
        pass

    class fakePlugin2(BasePlugin):
        pass

    class fakePlugin3(BasePlugin):
        pass

    plugin_list = PluginManager()

    plugin_list.register(fakePlugin1)
    plugin_list.register(fakePlugin2)
    plugin_list.register(fakePlugin3)

    assert plugin_list != []
    assert plugin_list.filter(fakePlugin1) == [fakePlugin1]
    # Expected input: by_type = Type[BasePlugin]
    assert plugin_list.filter(by_type=BasePlugin) == [fakePlugin1, fakePlugin2, fakePlugin3]

# Generated at 2022-06-13 22:35:56.782035
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    print(manager)
    #assert len(manager) == 7
    assert True


manager = PluginManager()
manager.load_installed_plugins()

# Generated at 2022-06-13 22:36:00.072154
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    m = PluginManager()
    m.load_installed_plugins()
    assert isinstance(m, PluginManager)
    #assert m > 0

test_PluginManager_load_installed_plugins()

# Generated at 2022-06-13 22:36:01.861448
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.load_installed_plugins()
    assert len(manager) > 0, "The number of plugins is not greater than 0"


# Generated at 2022-06-13 22:36:05.746304
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    """
    Arrange
    Act
    Assert
    """
    # Arrange
    # Act
    lst = PluginManager()
    lst.load_installed_plugins()
    # Assert
    assert (lst != [])

# Generated at 2022-06-13 22:36:11.009953
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    from httpie.downloads import FileDownloader
    plugins = PluginManager()
    assert plugins.filter() == []
    plugins.register(FileDownloader)
    assert plugins.filter() == [FileDownloader]
    assert plugins.filter(by_type=TransportPlugin) == [FileDownloader]
    assert plugins.filter(by_type=AuthPlugin) == []

# Generated at 2022-06-13 22:36:21.505451
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    # Case 1: plugin A and B have the same group name
    class A(FormatterPlugin):
        group_name = 'A'
    class B(FormatterPlugin):
        group_name = 'A'

    # Case 2: plugin C and D have different group name
    class C(FormatterPlugin):
        group_name = 'C'
    class D(FormatterPlugin):
        group_name = 'D'

    plugins = PluginManager()
    plugins.register(A, B, C, D)

    # test
    assert plugins.get_formatters_grouped() == {'A': [A, B], 'C': [C], 'D': [D]}



# Generated at 2022-06-13 22:36:27.899305
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.builtin import JSONFormatPlugin, HeadersFormatPlugin
    pm = PluginManager()
    pm.register(JSONFormatPlugin, HeadersFormatPlugin)
    plugins = pm.get_formatters_grouped()
    assert plugins['Formats'][0] is JSONFormatPlugin
    assert plugins['Formats'][1] is HeadersFormatPlugin

# Generated at 2022-06-13 22:36:45.314721
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    class X(BasePlugin):
        pass

    class Y(X):
        pass

    class Z(BasePlugin):
        pass

    class Generic:
        pass

    pm = PluginManager()
    pm.register(X, Y, Z)
    assert [Y] == pm.filter(X)
    assert [X, Y] == pm.filter(X) + pm.filter(Y)
    assert [Y] == pm.filter(lambda p: issubclass(p, Y))
    assert [] == pm.filter(Generic)



# Generated at 2022-06-13 22:36:50.311718
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class DummyPlugin(BasePlugin):
        group_name = 'test'
        group_title = 'Test Group'
        group_description = 'Test group description.'

    plugin_manager = PluginManager()
    plugin_manager.register(DummyPlugin)
    assert plugin_manager.get_formatters_grouped() == {'test': [DummyPlugin]}

# Generated at 2022-06-13 22:37:00.244556
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():

    plugins_before = PluginManager()
    plugins_before.register(AuthPlugin)
    mapping_before = plugins_before.get_auth_plugin_mapping()
    print(mapping_before)
    assert mapping_before == {}
    print("test case 1 is passed")

    plugins_after = PluginManager()
    plugins_after.register(AuthPlugin)
    plugins_after.register(AuthPlugin)
    mapping_after = plugins_after.get_auth_plugin_mapping()
    print(mapping_after)
    assert mapping_after == {}
    print("test case 2 is passed")


# 调用方法
test_PluginManager_get_auth_plugin_mapping()

# Generated at 2022-06-13 22:37:05.178572
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins.colors import ColoredFormatter
    from httpie.plugins.default import PrettyFormatter

    plugin_manager = PluginManager()
    plugin_manager.register(PrettyFormatter, ColoredFormatter)

    assert {'Default': [PrettyFormatter]} == plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:37:07.521832
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    assert isinstance(PluginManager().get_formatters_grouped(), dict)



# Generated at 2022-06-13 22:37:09.602834
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    pm = PluginManager()
    pm.append("a")
    pm.append("b")
    assert pm.filter("a") == ["a"]


# Generated at 2022-06-13 22:37:20.452120
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()

    # pkg_resources.iter_entry_points() are returning generator
    # So we have to assign to a list, in order to calculate length with len()
    installed_plugin_classes = list(plugin_manager)

    # We know there are 9 plugins
    assert len(installed_plugin_classes) == 9
    assert installed_plugin_classes[1].__module__ == 'httpie.plugins.httpie.v1'
    assert installed_plugin_classes[1].package_name == 'httpie'



# Generated at 2022-06-13 22:37:29.628598
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import os
    from httpie.plugins.builtin import BuiltinPlugin

    def load_plug_ins(plugin_dir):
        os.environ['HTTPIE_PLUGINS_DIR'] = plugin_dir
        plugin_manager = PluginManager()
        plugin_manager.register(BuiltinPlugin)
        plugin_manager.load_installed_plugins()
        return plugin_manager

    def test_formatters(plugin_dir):
        plugin_manager = load_plug_ins(plugin_dir)
        formatters = plugin_manager.get_formatters_grouped()
        assert "json" in formatters
        assert "html" in formatters
        assert "terminal" in formatters

    def test_formatters_with_filter(plugin_dir):
        plugin_manager = load_plug_ins(plugin_dir)
        plugin_manager

# Generated at 2022-06-13 22:37:36.133209
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    import os
    os.system("echo 'echo test_PluginManager_get_auth_plugin_mapping' >> /tmp/httpie_plugin.log")
    plugins = PluginManager()
    plugins.register(AuthPlugin)
    auth_plugin_mapping = plugins.get_auth_plugin_mapping()
    return auth_plugin_mapping


# Generated at 2022-06-13 22:37:42.336072
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    manager = PluginManager()

# Generated at 2022-06-13 22:38:11.767363
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    '''
    测试加载多个插件
    :return:
    '''
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert 'digest' in auth_plugin_mapping.keys()
    assert 'basic' in auth_plugin_mapping.keys()
    assert 'hawk' in auth_plugin_mapping.keys()



# Generated at 2022-06-13 22:38:14.935462
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    mgr = PluginManager()
    assert mgr == []
    mgr.load_installed_plugins()
    assert len(mgr) >= 2
    assert issubclass(mgr[0], BasePlugin)
    assert issubclass(mgr[1], BasePlugin)


# Generated at 2022-06-13 22:38:18.823028
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugins = PluginManager()
    plugins.register(AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin)
    assert plugins.filter(by_type=AuthPlugin) == [AuthPlugin]

# Generated at 2022-06-13 22:38:22.819334
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register(JSONFormatter, JSONLinesFormatter)
    assert plugin_manager.get_formatters_grouped() == {
        'json': [JSONFormatter, JSONLinesFormatter]
    }

# Generated at 2022-06-13 22:38:26.910277
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():
    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin, FormatterPlugin, ConverterPlugin, TransportPlugin)
    assert isinstance(plugin_manager.filter(AuthPlugin), list)
    assert isinstance(plugin_manager.filter(AuthPlugin)[0], AuthPlugin)


plugin_manager = PluginManager()

# Generated at 2022-06-13 22:38:30.280530
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugins = PluginManager()
    plugins.register(TestFormatterPlugin1, TestFormatterPlugin2, TestFormatterPlugin3)
    assert plugins.get_formatters_grouped() == {'TestFormattersGroup1': [TestFormatterPlugin1], 'TestFormattersGroup2': [TestFormatterPlugin2, TestFormatterPlugin3]}


# Generated at 2022-06-13 22:38:34.660795
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins.builtin import HTTPBasicAuthPlugin
    p = PluginManager()
    p.load_installed_plugins()
    assert HTTPBasicAuthPlugin in p
    assert p.get_auth_plugin_mapping()
    assert p.get_auth_plugin_mapping().get('basic') == HTTPBasicAuthPlugin

manager = PluginManager()

# Generated at 2022-06-13 22:38:41.842207
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    print("Test subject: method 'load_installed_plugins' of class PluginManager")

    # plugin manager just created: no installed plugins yet
    plugin_manager = PluginManager()
    assert len(plugin_manager) == 0

    # load the installed plugins
    plugin_manager.load_installed_plugins()

    # test that list of plugins is not empty
    assert len(plugin_manager) > 0
    print("The list of plugins is not empty: test succeeded!\n")



# Generated at 2022-06-13 22:38:49.368744
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    class FakeEntryPoint():
        def __init__(self, name):
            self.name = name

        def load(self):
            # just return entry point name
            return self.name

        def dist(self):
            # no implementation
            pass

    FakeEntryPointGroup = [FakeEntryPoint('plugin_{}'.format(i)) for i in range(10)]
    FakeEntryPointGroup += [FakeEntryPoint('not_httpie_plugin')]

    class FakeEntryPoints():
        def __init__(self, group):
            self.group = group

        def __iter__(self):
            return iter(self.group)

    class FakePkgResources():
        def iter_entry_points(self, name):
            return FakeEntryPoints(FakeEntryPointGroup)

    def temp_iter_entry_points(name):
        return

# Generated at 2022-06-13 22:39:02.262972
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    class _Formatter(FormatterPlugin):
        group_name = None
        format_name = None

    class JSON(_Formatter):
        group_name = 'JSON'
        format_name = 'JSON'

    class XML(_Formatter):
        group_name = 'XML'
        format_name = 'XML'

    class HTML(_Formatter):
        group_name = 'HTML'
        format_name = 'HTML'

    class CSV(_Formatter):
        group_name = 'CSV'
        format_name = 'CSV'

    class Other(_Formatter):
        group_name = None
        format_name = None

    class TestPluginManager(PluginManager):
        pass

    pm = TestPluginManager()
    pm.register(JSON, XML, HTML, CSV, Other)

    result = pm.get_

# Generated at 2022-06-13 22:39:49.372287
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    # 3 types of plugins
    assert len(plugin_manager) == 3        
    # check whether the plugin is loaded
    assert 'httpie_jwt_auth' in [plugin.package_name for plugin in plugin_manager.get_auth_plugins()]

# Generated at 2022-06-13 22:39:58.955564
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    Check if the formatters are grouped properly
    """
    import httpie.plugins.builtin
    plugin_manager = PluginManager()
    plugin_manager.register(httpie.plugins.builtin.Aes256Formatter)
    plugin_manager.register(httpie.plugins.builtin.JsonppFormatter)
    plugin_manager.register(httpie.plugins.builtin.JsonFormatter)

    output = plugin_manager.get_formatters_grouped()

# Generated at 2022-06-13 22:40:05.387580
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.plugins import builtin

    # Get output formatters from builtin
    builtin_formatters = list(filter(
        lambda p: issubclass(p, FormatterPlugin),
        builtin.__all__
    ))

    # Builtin formatters should exist
    assert builtin_formatters

    # Initialize plugin manager
    pm = PluginManager()
    pm.register(*builtin_formatters)

    # Formatters should be grouped
    assert pm.get_formatters_grouped()

    # There should be at least one group
    assert len(pm.get_formatters_grouped()) > 0

# Generated at 2022-06-13 22:40:17.231035
# Unit test for method filter of class PluginManager
def test_PluginManager_filter():

    from httpie.plugins.auth.basic import BasicAuthPlugin
    from httpie.plugins.auth.digest import DigestAuthPlugin
    from httpie.plugins.formatter import (
        FormatterPlugin,
        EchoFormatter,
        EchoFormatterV1,
        EchoFormatterV2,
        EchoFormatterV3,
    )
    from httpie.plugins.converter import (
        ConverterPlugin,
        EchoConverter,
        EchoConverterV1,
        EchoConverterV2,
        EchoConverterV3,
    )

    class FooTransportPlugin(TransportPlugin):
        name = 'foo'
        description = ''
        auth_type = ''
        auth_require = ()
        auth_config_schema = {}
        auth_class = BasicAuthPlugin
        error_cl

# Generated at 2022-06-13 22:40:17.747089
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
	pass

# Generated at 2022-06-13 22:40:26.586151
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    import httpie.plugins.builtin.formatters as builtin
    from httpie.plugins import formatter
    from httpie.plugins import group_formatter_plugins

    class CustomPlugin(formatter.FormatterPlugin): 
        #group_name = 'builtin'
        group_name = 'custom'

    class CustomPlugin2(formatter.FormatterPlugin): 
        group_name = 'custom'

    manager = PluginManager()
    manager.register(
        CustomPlugin,
        CustomPlugin2
    )
    manager.register(
        *[
            f_plugin
            for f_plugin
            in builtin.__dict__.values()
            if isinstance(f_plugin, type) and issubclass(f_plugin, formatter.FormatterPlugin)
        ]
    )

    formatters_grouped = manager

# Generated at 2022-06-13 22:40:29.409106
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()
    print(plugin_manager)

# Generated at 2022-06-13 22:40:36.078888
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    p = PluginManager()
    p.register(MockAuthPlugin1, MockAuthPlugin2)
    assert p.get_auth_plugin_mapping() == {
        'mock1': MockAuthPlugin1,
        'mock2': MockAuthPlugin2,
    }


# Generated at 2022-06-13 22:40:45.761014
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    plugin_manager = PluginManager()
    plugin_manager.register()


# Generated at 2022-06-13 22:40:54.735835
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    manager = PluginManager()
    manager.register(type('A', (FormatterPlugin,), {'group_name': 'x'}))
    manager.register(type('B', (FormatterPlugin,), {'group_name': 'y'}))
    manager.register(type('C', (FormatterPlugin,), {'group_name': 'y'}))
    assert manager.get_formatters_grouped() == {'x': [manager[0]], 'y': [manager[1], manager[2]]}

# Generated at 2022-06-13 22:41:46.927621
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    manager = PluginManager()
    manager.append(None)
    assert len(manager) == 1
    assert manager.__repr__() == "<PluginManager: [None]>"
    manager.register(dict)
    manager.register(list)
    assert len(manager) == 3
    assert manager.__repr__() == "<PluginManager: [None, <class 'dict'>, <class 'list'>]>"
    manager.unregister(dict)
    assert len(manager) == 2
    assert manager.__repr__() == "<PluginManager: [None, <class 'list'>]>"
    assert manager.filter(Type[BasePlugin]) == [None, list]
    assert manager.filter(Type[TransportPlugin]) == []
    
    
if __name__ == "__main__":
    test_PluginManager_load_installed

# Generated at 2022-06-13 22:41:56.876963
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():

    # Initialize plugin manager
    plugin_manager = PluginManager()
    try:
        plugin_manager.load_installed_plugins()
    except TypeError:
        print('Please make sure that package httpie is installed!')
        exit()

    # Check if plugins were loaded
    assert plugin_manager

    # Check plugin group
    formatter_group = plugin_manager.get_formatters_grouped()
    assert formatter_group

    # Check plugins
    assert plugin_manager.get_auth_plugins()
    assert plugin_manager.get_auth_plugin_mapping()
    assert plugin_manager.get_auth_plugin('basic')
    assert plugin_manager.get_formatters()
    assert plugin_manager.get_converters()
    assert plugin_manager.get_transport_plugins()


# Generated at 2022-06-13 22:42:02.011968
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    def test_PluginManager_load_installed_plugins_test_entrypoint_name_error():
        p = PluginManager()
        with pytest.raises(RuntimeError):
            p.load_installed_plugins('test')

    test_PluginManager_load_installed_plugins_test_entrypoint_name_error()



# Generated at 2022-06-13 22:42:05.920666
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
    from httpie.plugins.auth import BasicAuth

    plugin_manager = PluginManager()
    assert plugin_manager.get_auth_plugin_mapping() == {}

    plugin_manager.register(BasicAuth)
    assert plugin_manager.get_auth_plugin_mapping() == {'basic': BasicAuth}


# Generated at 2022-06-13 22:42:12.548821
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    from httpie.output.formats import get_group_name
    from httpie.output.formats.base import BaseFormat
    from httpie.output.formatters import JsonFormatter, DebugFormatter
    from httpie.output.formatters import (
        IndentFormatter, PlainFormatter, PrettyJsonFormatter,
        PygmentsFormatter, RawFormatter, StreamFormatter,
        TableFormatter
    )

    BaseFormat.get_group_name = get_group_name
    test_class_list = [
        JsonFormatter,
        DebugFormatter,
        IndentFormatter,
        PlainFormatter,
        PrettyJsonFormatter,
        PygmentsFormatter,
        RawFormatter,
        StreamFormatter,
        TableFormatter
    ]
    test_PM = PluginManager()

# Generated at 2022-06-13 22:42:16.490846
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    plugins = PluginManager()
    plugins.load_installed_plugins()

    assert plugins

    # Output processing

    assert plugins.get_formatters()
    assert plugins.get_formatters_grouped()
    assert plugins.get_converters()



# Generated at 2022-06-13 22:42:22.532204
# Unit test for method load_installed_plugins of class PluginManager
def test_PluginManager_load_installed_plugins():
    from httpie.plugins import AuthPlugin, ConverterPlugin, FormatterPlugin, TransportPlugin
    from httpie.plugins.manager import PluginManager
    from httpie.plugins.base import BasePlugin

    plugin_manager = PluginManager()
    plugin_manager.register(AuthPlugin)
    plugin_manager.register(ConverterPlugin)
    plugin_manager.register(FormatterPlugin)
    plugin_manager.register(TransportPlugin)
    plugin_manager.load_installed_plugins()
    assert plugin_manager == PluginManager()


# Generated at 2022-06-13 22:42:30.970898
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """
    The class PluginManager has the method get_formatters_grouped which return
    a dictionary map for data structure of plugins list. This unit test is to
    test this method. The method is modified to return a tuple of the map and
    the list. With these two data structures, it is easy to verify the result 
    is correct.
    """
    # The data structure for the map for data structure of plugins list.
    # The keys are the group name of plugins and the value is the list of 
    # plugins in the group.


# Generated at 2022-06-13 22:42:37.091861
# Unit test for method get_auth_plugin_mapping of class PluginManager
def test_PluginManager_get_auth_plugin_mapping():
	plugins = PluginManager()
	plugins.load_installed_plugins()
	mapping = plugins.get_auth_plugin_mapping()
	s= "AuthPlugin"
	for i in mapping.keys():
		s = s + " " + i
	assert(s == "AuthPlugin basic digest")

# Generated at 2022-06-13 22:42:48.277020
# Unit test for method get_formatters_grouped of class PluginManager
def test_PluginManager_get_formatters_grouped():
    """Formatter plugins should be grouped by group_name"""
    plugin_manager = PluginManager()
    plugin_manager.load_installed_plugins()