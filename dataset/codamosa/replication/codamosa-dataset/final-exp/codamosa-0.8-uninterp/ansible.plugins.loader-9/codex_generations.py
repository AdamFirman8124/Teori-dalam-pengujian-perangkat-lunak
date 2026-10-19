

# Generated at 2022-06-13 13:17:28.024082
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    from ansible.utils.collection_loader import add_dirs_to_loader
    add_dirs_to_loader("collection", ["/home/user/my_collections"])



# Generated at 2022-06-13 13:17:41.203227
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    my_plugin_loader = PluginLoader('/home/username/ansible_test/test', 'module', require_init=False)
    my_plugin_loader.package = 'ansible_collections.test.test_plugins'
    my_plugin_loader.subdir = 'test_plugins'
    my_plugin_loader.class_name = 'Test'
    my_plugin_loader.base_class = 'TestBaseClass'
    my_plugin_loader.add_directory('/home/username/ansible_test/test')
    my_plugin_loader.builtin_collections = set()
    my_plugin_loader.collections = []
    my_plugin_loader.collection_list = None
    my_plugin_loader.config = None

# Generated at 2022-06-13 13:17:50.540014
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Test with an action plugin
    my_plugin_loader = PluginLoader(package='ansible.plugins.action', class_name='ActionBase', base_class='ActionBase')
    assert my_plugin_loader.find_plugin('apt') is not None
    assert my_plugin_loader.find_plugin('systemd') is not None
    # Test with a callback plugin
    my_plugin_loader = PluginLoader(package='ansible.plugins.callback', class_name='CallbackBase', base_class='CallbackBase')
    assert my_plugin_loader.find_plugin('minimal') is not None



# Generated at 2022-06-13 13:17:52.819477
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
  test_obj = PluginLoader()
  assert test_obj.__contains__('asdf') == None



# Generated at 2022-06-13 13:17:53.608976
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    pass

# Generated at 2022-06-13 13:17:56.691910
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = PluginLoader('ansible.plugins.connection', 'Connection', 'connection_plugins')
    assert plugin_loader.__contains__('local')



# Generated at 2022-06-13 13:18:00.349594
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # check a valid path
    b_path = os.path.expanduser(to_bytes(os.path.dirname(__file__)))
    add_all_plugin_dirs(b_path)
    # check an invalid path
    add_all_plugin_dirs('/foo/bar')


# Generated at 2022-06-13 13:18:03.983908
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.plugins import shell_loader
    from ansible.modules.shell import BaseShellModule
    shell = get_shell_plugin('sh', '/bin/sh')
    assert isinstance(shell, BaseShellModule)
    assert shell.executable == '/bin/sh'



# Generated at 2022-06-13 13:18:10.908126
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    global PYTHON_VERSION
    global _PLUGIN_PATH_CACHE
    global _SHARED_OBJECT_LOADERS
    global _PLUGIN_FILTERS
    global _PLUGIN_PATH_CACHE
    global _PLUGIN_CACHE
    global _PLUGIN_FILTER_CACHE
    global _IGNORE_FILES
    global _CACHE_PLUGIN_PATH
    global _CACHE_PLUGIN_PATH_CACHE
    global _FILTER_PLUGIN_PATH
    global _FILTER_PLUGIN_PATH_CACHE
    global _TEST_PLUGIN_PATH
    global _TEST_PLUGIN_PATH_CACHE
    global _PLUGIN_PATH_CACHE_LOCK
    global _PLUG

# Generated at 2022-06-13 13:18:12.340492
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # This method will failed during implementation
    assert(True)


# Generated at 2022-06-13 13:18:52.237564
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader('', '', 'foo')
    loader._paths = [os.path.join(os.sep, 'foo')]

    assert loader._find_plugin('foo') == os.path.join(os.sep, 'foo', 'foo.py')
    assert loader._find_plugin(os.path.join('foo', 'bar')) is None
    assert loader._find_plugin('bar.py') is None


# Generated at 2022-06-13 13:19:02.401487
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    """
    Test PluginLoadContext.record_deprecation()
    """
    class TestPluginLoadContext(PluginLoadContext):
        """
        Test PluginLoadContext class
        """
        def __init__(self):
            self.deprecated = False
            self.removal_date = None
            self.removal_version = None
            self.deprecation_warnings = []

    # test with deprecation warning
    plugin_load_context = TestPluginLoadContext()
    deprecation = {}
    deprecation['warning_text'] = 'Deprecated Text'
    deprecation['removal_date'] = 'yesterday'
    deprecation['removal_version'] = '1.1.1'
    # Call method

# Generated at 2022-06-13 13:19:11.808780
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    for (name, obj) in get_all_plugin_loaders():
        if obj.subdir == 'callback':
            path = 'dummy_dir/callback'
            obj.add_directory(path)
            assert path in obj.directories
            assert len(obj.directories) == 1
            assert path == obj.directories[0]

            path2 = 'dummy_dir2/callback'
            obj.add_directory(path2)
            assert path2 in obj.directories
            assert len(obj.directories) == 2
            assert path2 == obj.directories[1]



# Generated at 2022-06-13 13:19:17.621182
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    shell_loader.directories=[]
    paths=[os.getcwd()+'/test/']
    add_dirs_to_loader('shell',paths)
    assert os.path.abspath(os.getcwd()+'/test/') in shell_loader.directories



# Generated at 2022-06-13 13:19:20.421689
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = PluginLoader('foo', 'bar', 'baz', 'qux')
    assert plugin_loader.__contains__('dex') is False
    assert plugin_loader.__contains__('foo') is True
    assert plugin_loader.__contains__('foo.baz') is True

# Generated at 2022-06-13 13:19:28.563414
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    get_shell_plugin(shell_type='sh')
    get_shell_plugin(shell_type='sh', executable='sh')
    get_shell_plugin(shell_type=None, executable='sh')
    try:
        get_shell_plugin(shell_type=None, executable='cmd')
    except AnsibleError:
        pass
    try:
        get_shell_plugin(shell_type=None, executable=None)
    except AnsibleError:
        pass



# Generated at 2022-06-13 13:19:33.098334
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    PL = PluginLoader('/path/to/nonexistent/directory/modules', 'ModuleDir', 'module_name')
    PL._searched_paths = ['/path/to/nonexistent/directory/modules', '/path/to/nonexistent/directory/modules/*']
    PL._module_cache = {}

    # check if function raises exception when passing invalid types to 'path_only' and 'class_only' parameters
    for val in ([None], [None, None], ['false', 'false'], ['10', '20']):
        assertRaisesRegexp(AnsibleError, "invalid type", PL.all, *val)

    # check succesful case

# Generated at 2022-06-13 13:19:40.009443
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader_obj = PluginLoader(
        'ansible.plugins.lookup',
        'LookupModule',
        config_options=C.config.get_config_value('lookup_plugins'))

    # Test the PluginLoader.get_with_context method
    test_input = {"name": "dummy", "collection_list": None}
    expected_result = get_with_context_result(
        "ansible.plugins.lookup.dummy",
        plugin_load_context=AnsiblePluginLoadContext(
            plugin_resolved_name="dummy", 
            resolved=True, 
            plugin_resolved_path="./ansible/plugins/lookup/dummy.py"))
    assert plugin_loader_obj.get_with_context(**test_input) == expected_result

# Unit

# Generated at 2022-06-13 13:19:52.284089
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # Test with class_only=False (default)
    loader = Jinja2Loader('ansible.legacy')
    name = 'to_datetime'
    test_path = os.path.join(C.DEFAULT_MODULE_PATH, 'converters.py')
    with patch('ansible.utils.plugin_docs.get_docstring', return_value=''), \
        patch('ansible.utils.plugin_docs.get_docstring_examples', return_value=''), \
        patch.object(Jinja2Loader, '_searched_paths', [test_path]), \
        patch.object(Jinja2Loader, '_get_paths', return_value=[test_path]):

        obj = loader.get(name)
        assert obj is not None
        assert obj.__doc

# Generated at 2022-06-13 13:19:56.449700
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    plugin_dirs = ['action', 'cache', 'callback', 'connection', 'lookup', 'shell_plugin', 'strategy', 'vars']
    for name, obj in globals().items():
        if isinstance(obj, PluginLoader):
            assert name in plugin_dirs



# Generated at 2022-06-13 13:20:19.484440
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert getattr(sys.modules[__name__], '%s_loader' % "action")



# Generated at 2022-06-13 13:20:26.950255
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # NOTE: this test does not test the loading of collections, but rather the legacy resolution
    # collection loading is tested in a different test
    class FakeLoadContext(object):
        def __init__(self, path, name, resolved, nope):
            self.plugin_resolved_path = path
            self.plugin_resolved_name = name
            self.resolved = resolved
            self.nope = nope

    class TestPluginLoader(PluginLoader):
        def __init__(self, *args, **kwargs):
            self._aliases = {'thing2': 'thing1'}
            super(TestPluginLoader, self).__init__(*args, **kwargs)

# Generated at 2022-06-13 13:20:41.369083
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    import unittest
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 0

    def test_get(self, name):
        return self.get(name, display)

    class MyJinja2Loader(Jinja2Loader):
        def all(self, *args, **kwargs):
            return list(super(MyJinja2Loader, self).all(*args, **kwargs))

    loader = MyJinja2Loader('ansible.plugins', 'action', 'ActionBase')
    loader.add_directory(os.path.join(os.path.dirname(__file__), '..', 'modules'))


# Generated at 2022-06-13 13:20:53.237784
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # argv = list(sys.argv)
    # sys.argv = argv[0:1]
    # # Bootstrap the jinja2_loader
    # jinja2_loader = Jinja2Loader(module_name='ansible')
    # sys.argv = argv
    # # Initialize the jinja2_loader
    # jinja2_loader.init(load_on_init=False)
    # Assert the call to jinja2_loader.get
    # jinja2_loader.get(name)
    raise NotImplementedError


# Generated at 2022-06-13 13:20:55.609361
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    func = add_all_plugin_dirs
    assert len(get_all_plugin_loaders()) == 4



# Generated at 2022-06-13 13:21:03.779989
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    loader = PluginLoader(config=None, package='ansible.plugins.test', subdir='', base_class=None, namespaces=None)
    loader._add_directory('ansible/plugins/test/youpi')
    assert loader._searched_paths[-1] == 'ansible/plugins/test/youpi'
    assert loader._searched_paths[0] != 'ansible/plugins/test/youpi'


# Generated at 2022-06-13 13:21:14.908142
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader("ansible_collections.my.my_ns.my_coll.plugins.action", 'action', 'AnsibleAction')
    assert loader.find_plugin("local.py") == "/home/users/jf/ansible_collections/my/my_ns/my_coll/plugins/action/local.py"
    assert loader.find_plugin("ansible_collections.my.my_ns.my_coll.plugins.action.local.py") == "/home/users/jf/ansible_collections/my/my_ns/my_coll/plugins/action/local.py"
    assert loader.find_plugin("ansible.builtin.local.py") == "/Users/jf/ansible/lib/ansible/plugins/action/local.py"
    # FIXME: Check why this fails

# Generated at 2022-06-13 13:21:19.207384
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method __contains__ of class PluginLoader
    '''
    plugin_loader = PluginLoader('test')
    assert False == (plugin_loader.has_plugin('test'))
    assert False == (plugin_loader.has_plugin('test2'))

# Generated at 2022-06-13 13:21:28.416812
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    """
    Test that it can add directories to the plugin loaders
    """

    # Test passing multiple directory
    paths = ['/path/to/custom/module',
             '/path/to/custom/module/v2',
             '/path/to/custom/module/v3',
             '/path/to/custom/module/v4',
             '/path/to/custom/module/v5',
             '/path/to/custom/module/v6',
             '/path/to/custom/module/v7']

    # TODO: I'm not sure what the goal of this function is, this test is pretty
    # much useless
    add_dirs_to_loader("module", paths)



# Generated at 2022-06-13 13:21:36.683925
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = 'name'
    mock_pluginloaders = {'pluginloaders': [{'obj': 'add_directory'}]}

    with patch.object(sys.modules[__name__], 'get_all_plugin_loaders', return_value = mock_pluginloaders):
        with patch.object(os.path, 'expanduser', return_value = 'path'):
            # Test non-existing path
            with patch.object(os.path, 'isdir', return_value = False):
                with patch.object(display, 'warning') as mock_display_warning:
                    add_all_plugin_dirs('test_value')
                    mock_display_warning.assert_called_with(u"Ignoring invalid path provided to plugin path: "
                                                            u"'test_value' is not a directory")
            #

# Generated at 2022-06-13 13:21:55.236910
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # Assign
    # Try
    # Assert
    assert True

# Generated at 2022-06-13 13:22:01.332944
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    import ansible.plugins.loader as pl
    base_class = ["BaseClass"]
    package = ["package"]
    class_name = ["ClassName"]

    pl1 = pl.PluginLoader(base_class, package, class_name)
    var1 = "name"
    pl1.find_plugin(var1)



# Generated at 2022-06-13 13:22:11.013364
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    '''
    Deprecation message should not be printed for deprecation.warning_text=None
    '''
    import mock
    import sys

    import ansible.utils.plugin_docs
    from ansible.utils.plugin_docs import get_docstring, get_docfragment, _get_docfragment_from_data

    def _get_docfragment_from_data_test(data, name, fragment):
        def_data = _get_docfragment_from_data(data, name, fragment)
        return def_data

    ctx = PluginLoadContext()
    name = "get_option"
    deprecation = {'warning_text' : None}
    collection_name = ""


# Generated at 2022-06-13 13:22:13.241723
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    l = PluginLoader('ansible.plugins.filter', 'ActionModule')
    assert (('template' in l) == True)
    assert (('foobar' in l) == False)


# Generated at 2022-06-13 13:22:21.855418
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    import sys
    import unittest
    from mock import patch, PropertyMock

    p = patch.object(sys, 'modules', {})
    p.start()
    
    with patch('ansible_collections.ansible.builtin.plugins.module_utils.plugins.loader._get_available_collections_list') as get_available_collections_list:
        with patch('ansible_collections.ansible.builtin.plugins.module_utils.plugins.loader.AnsibleCollectionRef') as AnsibleCollectionRef:
            
            # Constructor test
            ####################
            
            # Ensure that the system is setup correctly for the tests to run
            assert 'ansible_collections.ansible' in sys.modules
            assert 'ansible.builtin' in sys.modules

# Generated at 2022-06-13 13:22:26.682183
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    add_all_plugin_dirs(os.path.join(os.path.dirname(__file__), '..', '..', 'plugins'))
    assert 'Authentication' in MODULE_CACHE


# Generated at 2022-06-13 13:22:38.090963
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    class Loader(PluginLoader):
        plugin_kwargs = dict(key_a=9, key_b=10)
        def __init__(self, class_name, package, config, subdir, aliases, *args, **kwargs):
            super(Loader, self).__init__(class_name, package, config, subdir, aliases, *args, **kwargs)
            self.called = 0
            self.plugin_kwargs = kwargs
            self.plugin_args = args

        def get(self, name, *args, **kwargs):
            self.called += 1
            return super(Loader, self).get(name, *args, **kwargs)


# Generated at 2022-06-13 13:22:48.245270
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    # declare the object of the class
    test_record_deprecation = PluginLoadContext()
    # check the warning text for the first deprecation
    warning_text_first=test_record_deprecation.record_deprecation('test1',{'warning_text':'This plugin is deprecated.'},'test_coll').deprecation_warnings[0]
    # check the warning text for the second deprecation
    warning_text_second=test_record_deprecation.record_deprecation('test2',{'warning_text':'This plugin is deprecated.','removal_version':'1.0'},'test_coll').deprecation_warnings[1]
    # check if the function returns the same object

# Generated at 2022-06-13 13:22:50.835266
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    shell = get_shell_plugin('sh')
    assert shell.SHELL_FAMILY == 'sh'
    assert hasattr(shell, 'executable')
    assert hasattr(shell, 'random_marker')



# Generated at 2022-06-13 13:22:56.098006
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # Setup:
    config.initialize_plugin_configuration_definitions()
    loader = Jinja2Loader('filter_plugins', 'FilterModule')
    loader.set_plugin_paths()

    args = []
    kwargs = {}

    # Test:
    try:
        loader.get('dummy', *args, **kwargs)
    except AnsibleError as exc:
        # Assert: exception from get
        assert exc == 'No code should call "get" for Jinja2Loaders (Not implemented)'

    # Cleanup:
    config.clean_reset_plugins()


# Generated at 2022-06-13 13:23:27.608369
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    from importlib import util
    import sys
    # Make sure that _display_plugin_load is covered by test
    sys.modules['ansible.module_utils.common.logging'] = util.find_spec('ansible.module_utils.common.logging').loader.load_module()

    # mock out the module cache in _load_module_source
    module_cache = {}
    for _module in ('action', 'cache', 'lookup', 'module_common', 'strategy', 'terminal'):
        module_cache['{}.{}'.format(_module, _module)] = util.find_spec('ansible.plugins.{}'.format(_module)).loader.load_module()

# Generated at 2022-06-13 13:23:39.314519
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    from ansible.plugins.loader import PluginLoader

    plugin_list = ['cli', 'inventory', 'callback', 'lookup', 'vars', 'filter']
    for plugin in plugin_list:
        if plugin is not plugin_list:
            continue
        try:
            fail_unless(PluginLoader(plugin, 'ansible.plugins.%s' % plugin, 'ansible.plugins.%s.%s' % (plugin, plugin)))
        except ImportError:
            print('WARNING: no plugin of type "%s" was found on this system' % plugin)


# Generated at 2022-06-13 13:23:42.346601
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    class_ = PluginLoader
    meth = getattr(class_, '__contains__')
    meth()



# Generated at 2022-06-13 13:23:46.633728
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # get method args
    # return_type='instance', args=None, kwargs=None
    pl = PluginLoader(package='ansible.plugins.action', subdir='test_plugins', plugin_base_class=str)
    for obj in pl.all():
        print(obj)
    #print(pl.all())



# Generated at 2022-06-13 13:23:51.833334
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # test 'action' plugin loader from a plugin_dir, a 'ansible_collections.valentinog.test' collection and
    # a 'ansible' collection (not installed)
    plugin_dir = './lib/ansible/plugins'
    collection_dir = './lib/ansible_collections/valentinog/test'
    collection_dir2 = './lib/ansible'

    def _find_plugin(plugin_load_context, plugin_name, plugin_type, plugin_dir, collection_dir=None, collection_dir2=None):
        loader = PluginLoader.get(plugin_type, './lib/ansible/plugins', 'ansible.plugins')
        context = loader.find_plugin_with_context(plugin_name, plugin_load_context, collection_list=(collection_dir, collection_dir2))


# Generated at 2022-06-13 13:23:54.002615
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    jinja2Loader = Jinja2Loader()
    assert jinja2Loader.get('to_json', *(), **{}) is None

# Generated at 2022-06-13 13:24:03.300333
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.plugins.action import ActionModule
    from ansible.plugins.cache import CacheModule
    from ansible.plugins.cliconf import CliConf
    from ansible.plugins.connection import Connection
    from ansible.plugins.filter import FilterModule
    from ansible.plugins.inventory import InventoryModule
    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.netconf import NetConf
    from ansible.plugins.shell import ShellModule
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.test import TestModule
    from ansible.plugins.terminal import Terminal
    from ansible.plugins.vars import VarsModule

# Generated at 2022-06-13 13:24:12.674919
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import ansible.plugins.loader
    loader = ansible.plugins.loader.PluginLoader(package='ansible.plugins.test', config=dict(ANSIBLE_TEST_PLUGINS_ALL={"magic_number_2": {"a": 1, "b": 2, "c": 3}, "magic_number_3": {"a": 2}, "magic_number_4": {"c": 4}}), class_name='MagicNumber', base_class='ansible.plugins.test.magic_number.MagicNumber', )
    # C.DEFAULT_DEBUG = True

# Generated at 2022-06-13 13:24:13.531455
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    return None  # TODO: add unit test for method get of class Jinja2Loader


# Generated at 2022-06-13 13:24:19.935695
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.plugins import get_all_plugin_loaders
    for plugin_type, plugin_loader in get_all_plugin_loaders():
        old_path_length=len(plugin_loader.package_paths)
        plugin_loader.add_directory("/ansible-test")
        assert len(plugin_loader.package_paths)==old_path_length+1
        assert plugin_loader.package_paths[-1]=="/ansible-test"
        plugin_loader.add_directory("/ansible-test2")
        assert len(plugin_loader.package_paths)==old_path_length+2
        assert plugin_loader.package_paths[-1]=="/ansible-test2"



# Generated at 2022-06-13 13:25:05.709836
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    with pytest.raises(AnsibleError) as exc:
        # Arrange
        jinja2loader = Jinja2Loader('ansible.legacy.filter_plugins', 'FilterModule')
        # Act
        jinja2loader.find_plugin('substr')
    # Assert
    assert 'No code should call "find_plugin"' in str(exc)

# Generated at 2022-06-13 13:25:14.457879
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pl = PluginLoader('ansible.plugins.test.test_utils', 'AnsibleTest', 'tests', required_base_class='BaseClass')
    assert len(list(pl.all())) == 1
    assert len(list(pl.all(path_only=True))) == 1
    assert len(list(pl.all(class_only=True))) == 1

# Generated at 2022-06-13 13:25:23.749800
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    pf = PluginLoader('ansible.plugins.action', 'ActionModule',
                      C.DEFAULT_INVENTORY_ENABLED_GROUP_PATTERNS, 'action_plugins')
    rc = pf.find_plugin_with_context('systemd')
    assert rc.resolved
    assert str(rc.plugin_resolved_name) == 'ansible.plugins.action.systemd'
    # FIXME: add tests for other cases

# Generated at 2022-06-13 13:25:27.622543
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
  obj = Cake()
  name = 'name'
  a = obj.find_plugin_with_context(name)
  assert a._plugin_load_context.plugin_resolved_path == "path"
  assert a._plugin_load_context.plugin_resolved_name == "name"
  assert a._plugin_load_context.redirect_list == []


# Generated at 2022-06-13 13:25:28.774440
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    pass # test is noop since function is implemented in Python


# Generated at 2022-06-13 13:25:34.684026
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''Add existing plugin dirs and test that the path is added'''
    # Test with a non existent directory
    path = '/non_existent/'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    for name, obj in get_all_plugin_loaders():
        obj.plugin_paths.clear()  # clear current plugin paths
        if obj.subdir:
            plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
            obj.add_directory(to_text(plugin_path))
            assert len(obj.plugin_paths) == 0
    # Test with an existent directory
    path = './test/integration/filter_plugins/'
    b_path = os.path

# Generated at 2022-06-13 13:25:37.588550
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
  """
  :type plugin_loader: Jinja2Loader
  """
  plugin_loader = Jinja2Loader()
  plugin_loader.get()


# Generated at 2022-06-13 13:25:40.465911
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    class TestLoader(PluginLoader):
        subdir = 'test_type'

    TestLoader.add_directory('/path/to/test_type')

    assert TestLoader.get_directory() == ['/path/to/test_type']


# Generated at 2022-06-13 13:25:42.818308
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    jinja2_loader = Jinja2Loader('./')
    for element in jinja2_loader.get('plugin_name'):
        assert element is None

# Generated at 2022-06-13 13:25:51.158085
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    find_plugin_with_context_result_object_name = 'find_plugin_with_context_result_object_name'
    find_plugin_with_context_result_object_redirect_list = 'find_plugin_with_context_result_object_redirect_list'
    find_plugin_with_context_result_object_resolved = 'find_plugin_with_context_result_object_resolved'
    find_plugin_with_context_result_object_plugin_resolved_fqcr = 'find_plugin_with_context_result_object_plugin_resolved_fqcr'
    find_plugin_with_context_result_object_plugin_resolved_name = 'find_plugin_with_context_result_object_plugin_resolved_name'
    find_plugin_with_context_result_object