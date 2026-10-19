

# Generated at 2022-06-13 13:18:06.127786
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    c_instance = PluginLoader('c_package', package='a_package',
                              config=ConfigParser(),
                              subdir='subdir',
                              aliases=dict(),
                              class_name='class_name',
                              base_class='a_package.a_class',
                              )
    c_instance.__setstate__('test')
    assert c_instance == 'test'

# Generated at 2022-06-13 13:18:15.991538
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    pl = PluginLoader(b'TestPluginLoader', 'ansible.plugins.test_loader', C.DEFAULT_MODULE_PATH, 'ansible.plugins.test_loader.TestPluginLoader', 'ansible.plugins.test_loader.BaseTestPluginLoader', 'test_plugin_loader')
    # unserialize to demonstrate method

# Generated at 2022-06-13 13:18:18.436260
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    # test passing parameters to the method
    try:
        plugin_loader = PluginLoader('a', 'b', 'c')
        plugin_loader.add_directory('/tmp')
    except Exception as e:
        assert False, e



# Generated at 2022-06-13 13:18:28.962010
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    add_dirs_to_loader(
        which_loader="module",
        paths=[
            # This path is on Travis CI
            "/home/travis/build/ansible/ansible/plugins/action"
        ]
    )
    add_dirs_to_loader(
        which_loader="cache",
        paths=[
            # This path is on Travis CI
            "/home/travis/build/ansible/ansible/plugins/cache"
        ]
    )
    add_dirs_to_loader(
        which_loader="callback",
        paths=[
            # This path is on Travis CI
            "/home/travis/build/ansible/ansible/plugins/callback"
        ]
    )

# Generated at 2022-06-13 13:18:37.768494
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    #Tests to ensure find_plugin_with_context gives the expected results
    #Adding the results in a dictionary
    expected_results = {}
    expected_results['cache'] = {'action_name': None, 'plugin_search_path': None, 'plugin_load_context': "<ansible_collections.ansible.builtin.plugins.loader.get_with_context_result object at 0x7faecc49a908>"}
    expected_results['cache_loader'] = {'action_name': None, 'plugin_search_path': None, 'plugin_load_context': "<ansible_collections.ansible.builtin.plugins.loader.get_with_context_result object at 0x7faecc49a908>"}

# Generated at 2022-06-13 13:18:38.665749
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert 1 == 1


# Generated at 2022-06-13 13:18:42.674173
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    '''
    Test if list of the plugins will be returned
    '''
    # Test if it returns a Generator
    assert isinstance(PluginLoader('LookupModule', config=None, package='ansible.plugins.lookup').all(), types.GeneratorType) == True, "PluginLoader not returning a generator"



# Generated at 2022-06-13 13:18:51.479763
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    all_plugin_loaders = get_all_plugin_loaders()

    path = '/usr/share/ansible'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        for name, obj in all_plugin_loaders:
            if obj.subdir:
                obj.directories = []
                plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
                if os.path.isdir(plugin_path):
                    obj.add_directory(to_text(plugin_path))
                    path_obj = obj.directories[0]

# Generated at 2022-06-13 13:18:57.482888
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():

    # Execute unit under test
    data = dict()
    pl = PluginLoader(package='', class_name='', base_class='', config_base_class='')
    pl.__setstate__(data)

    test = pl._searched_paths != []

    # Ensure that exception is raised
    assert test, 'AnsibleAssertionError: plugin loader should not have searched paths'


# Generated at 2022-06-13 13:18:58.093771
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pass



# Generated at 2022-06-13 13:20:01.477310
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    shell = get_shell_plugin('sh')
    assert shell.SHELL_FAMILY == 'sh'



# Generated at 2022-06-13 13:20:02.986297
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    add_all_plugin_dirs('this_is_not_a_dir')


# Generated at 2022-06-13 13:20:08.988456
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = '~/ansible/plugins/module'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
                if os.path.isdir(plugin_path):
                    obj.add_directory(to_text(plugin_path))
    else:
        display.warning("Ignoring invalid path provided to plugin path: '%s' is not a directory" % to_text(path))    
    

# Generated at 2022-06-13 13:20:10.471514
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # FIXME: Add unit tests for PluginLoader.all
    pass


# Generated at 2022-06-13 13:20:15.544111
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # Set up fixture
    loader = PluginLoader("foo", "bar", "/path/to/plugins")

    # Test success cases
    assert loader.find_plugin_with_context("baz") is None
    assert loader.find_plugin_with_context("foo.bar.baz") is None

# Generated at 2022-06-13 13:20:18.018862
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    from ansible.plugins.action import ActionModule
    from ansible.cli import CLI

# Generated at 2022-06-13 13:20:20.150758
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    b_path = '/tmp'
    for name, obj in get_all_plugin_loaders():
        assert isinstance(obj, PluginLoader)



# Generated at 2022-06-13 13:20:22.949066
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    t = PluginLoader(package='ansible.plugins.test', base_class='BaseTest', class_name='Test')
    count = 0
    for obj in t.all():
        count += 1

    assert count == 1



# Generated at 2022-06-13 13:20:23.830226
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    pass


# Generated at 2022-06-13 13:20:37.178331
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    # Fake a plugin
    class FakePluginLoader(PluginLoader):
        subdir = 'fake_plugin_type'

        def __init__(self):
            super(FakePluginLoader, self).__init__()
            self._plugins = []

        @property
        def plugins(self):
            return self._plugins

        def add_directory(self, path):
            self._plugins.append(path)
    FakePluginLoader()

    # Create a temporary directory structure to test
    # -a path/to/dir
    #   -dir
    #     -action_plugin
    #       -module1.py
    #       -module2.py
    #     -callback_plugin
    #     -connection_plugin
    #     -shell_plugin
    #     -inventory_plugin
    #     -other_plugin
    #     -filter

# Generated at 2022-06-13 13:21:07.860079
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' test function add_all_plugin_dirs '''
    from ansible.plugins.action import ActionModule
    from ansible.plugins.callback import CallbackModule
    from ansible.plugins.connection import Connection
    from ansible.plugins.filter import FilterModule
    from ansible.plugins.inventory import InventoryPlugin
    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.module_utils import ModuleUtils
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.test import TestModule
    from ansible.plugins.vars import VariableModule
    if C.COLLECTIONS_PATHS:
        for path in C.COLLECTIONS_PATHS:
            add_all_plugin_dirs(path)

# Generated at 2022-06-13 13:21:09.261486
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    assert True



# Generated at 2022-06-13 13:21:19.366892
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Tests find_plugin method of class PluginLoader,
    # in case of plugin with not provided handler, should throw requested plugin not found, otherwize should return the plugin path
    handler_path = '/tmp/ansible_test/playbook'
    if not os.path.exists(handler_path):
        os.makedirs(handler_path)

    with open(handler_path + '/not_provided.py', 'w') as fs:
        fs.write('#!/usr/bin/python')

    loader = PluginLoader('action', 'ActionModule', 'action_plugins', 'my')
    with pytest.raises(AnsibleError):
        loader.find_plugin(name='not_provided')


# Generated at 2022-06-13 13:21:20.358697
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' add_all_plugin_dirs(path) '''


# Generated at 2022-06-13 13:21:30.359283
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    cls = 'PluginLoader'

    class AnsibleModuleMock(object):
        def __init__(self, spec, **kwargs):
            self.params = kwargs
            self.spec = spec

        def fail_json(self, *args, **kwargs):
            pass

    m_module = AnsibleModuleMock(spec='ansible.module_utils.basic')

    def __mock_load_module_source(name, path):
        return sys.modules[name]

    m = mock.mock_open(read_data='#!/usr/bin/python')
    m.side_effect = [m]


# Generated at 2022-06-13 13:21:39.478075
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    context = PluginLoadContext()
    assert context.record_deprecation("name1",{"warning_text":"warning text","removal_date":"never"},None)
    assert context.record_deprecation("name2",{"warning_text":"","removal_date":None},None)
    assert context.record_deprecation("name3",{"warning_text":None,"removal_version":None},None)

test_PluginLoadContext_record_deprecation()



# Generated at 2022-06-13 13:21:50.150092
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader_01 = PluginLoader('action_plugin', 'ActionModule', 'ansible.plugins.action')
    plugin_loader_02 = PluginLoader('cache_plugin', 'CacheModule', 'ansible.plugins.cache')
    plugin_loader_03 = PluginLoader('cache_plugin', 'CacheModule', 'ansible.plugins.cache')
    plugin_loader_04 = PluginLoader('collection_finder', 'CollectionsFinder', 'ansible.plugins.collection_finder')
    plugin_loader_05 = PluginLoader('connection_plugin', 'Connection', 'ansible.plugins.connection')
    plugin_loader_06 = PluginLoader('filter_plugin', 'FilterModule', 'ansible.plugins.filter')
    plugin_loader_07 = PluginLoader('inventory_plugin', 'InventoryModule', 'ansible.plugins.inventory')
    plugin_loader_08

# Generated at 2022-06-13 13:21:57.386804
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    #mock C.config
    C.config = ConfigParser.ConfigParser()
    #mock plugin_loader
    plugin_loader = PluginLoader('', '', '', '', [])
    #mock plugin_candidate
    plugin_candidate = object()
    #mock plugin_load_context
    class plugin_load_context:
        def __init__(self, plugin_candidate):
            self.plugin_candidate = plugin_candidate
    #set C.IGNORE_FILES
    C.IGNORE_FILES = ['.bcd', '.efg']
    #set ini_files
    ini_files = [plugin_candidate]
    #set plugin_candidate.name
    plugin_candidate.name = 'abc.py'
    #call plugin_loader.find_plugin_with_context

# Generated at 2022-06-13 13:22:08.104017
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # Initialize the class
    # Use of real basedir from ansible instead of a dummy
    p = PluginLoader(
        package='ansible.plugins.action',
        config=dict(),
        directories=['/etc/ansible', '/usr/share/ansible'],
        basedir='ansible/plugins'
    )
    result = p.find_plugin_with_context('shell')

    # Verify correct path
    assert result.plugin_resolved_path.endswith('shell.py')
    # Verify that we found something
    assert result.resolved

    # Verify that non-existing plugin yields a useful error message
    result = p.find_plugin_with_context('foobar')
    assert result.error.startswith('foobar not found')

    # Verify that all the entries in the path are there

# Generated at 2022-06-13 13:22:11.726494
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    PLUGIN_PATH_CACHE.clear()
    PATH_CACHE.clear()

    plugin_loader = get_plugin_loader('cache')
    plugin_loader.add_directory('/tmp/fake/dir/')
    assert '/tmp/fake/dir/cache' in PLUGIN_PATH_CACHE



# Generated at 2022-06-13 13:22:38.559206
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader = PluginLoader('action_plugin', 'Controller', 'ansible.plugins.action')

    # Non-existent plugin name
    with pytest.raises(AnsibleError):
        plugin_loader.get_with_context(name='non-existent-plugin')

    # Plugin name that matches a collection name
    with pytest.raises(AnsibleError):
        plugin_loader.get_with_context(name='ansible_collections')

    # Plugin name that matches a collection name with suffix
    with pytest.raises(AnsibleError):
        plugin_loader.get_with_context(name='ansible_collections.test')

# Generated at 2022-06-13 13:22:45.776746
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    # verify that the plugin loader returns various expected values for various kinds of plugins
    plugin_loader = PluginLoader(class_name='Foo', package='ansible.plugins.action', base_class='ActionBase',
                                 config_base='bar', config_env_var=None)
    plugin_loader.add_directory(DATA_PATH, with_subdir=True)
    assert 'shell' in plugin_loader
    assert 'unavailable' not in plugin_loader
    assert 'module' in plugin_loader
    assert 'unavailable_module' not in plugin_loader
    assert 'action' in plugin_loader  # intentionally not "foo" - we want to test the default search paths
    assert 'foo' in plugin_loader  # this one has a redirect



# Generated at 2022-06-13 13:22:51.212465
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # FIXME: This will not work until we modify the source code to not need the basedir
    # I think we can load it from the module, but I haven't tried yet
    #
    # plugins = Jinja2Loader('ansible/plugins/filter_plugins', 'FilterModule')
    #
    # for i in plugins.get('fileglob.basename'):
    #     # i.compile()
    #     print(i)
    #
    pass



# Generated at 2022-06-13 13:22:53.883735
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pl = PluginLoader('ansible.plugins', 'Module', C.DEFAULT_INVENTORY_ENABLED)
    pl_all = pl.all()
    for p in pl_all:
        print(p.__class__)


# Generated at 2022-06-13 13:23:03.884746
# Unit test for method find_plugin of class PluginLoader

# Generated at 2022-06-13 13:23:09.145711
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    """
    Tests for method get for class Jinja2Loader.
    """

    # Make sure that class exists
    assert isinstance(Jinja2Loader, object)

    # Not implemented and not used
    # SKIP
    # with pytest.raises(NotImplementedError):
    #    Jinja2Loader().get(name='string')

# Generated at 2022-06-13 13:23:12.809400
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = os.environ['PWD']
    add_all_plugin_dirs(path)
    assert sys.path.count(path) == 1



# Generated at 2022-06-13 13:23:21.179604
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    import types
    loader = Jinja2Loader()
    test_name = 'ansible.legacy.plugins.filter.jinja2.Add'
    loader.add_directory(os.path.join('lib/ansible/plugins/filter'))
    result = loader.get(test_name)
    assert isinstance(result, types.FunctionType)
    assert result.__name__ == 'Add'

# Generated at 2022-06-13 13:23:28.381146
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    assert get_shell_plugin(shell_type='sh') is not None
    assert get_shell_plugin(shell_type='pwsh') is not None
    assert get_shell_plugin(executable='/usr/bin/sh') is not None
    assert get_shell_plugin(executable='/usr/bin/pwsh') is not None
    try:
        get_shell_plugin()
    except AnsibleError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 13:23:32.899087
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    loader = PluginLoader("test_path", "test_name")
    try:
        loader.__contains__("test_key")
    except Exception as exception:
        assert(type(exception) == AnsibleError)


# Generated at 2022-06-13 13:25:24.089749
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    """Test get_with_context of class PluginLoader
    """
    uut = PluginLoader()
    # TODO: Write test
    assert False



# Generated at 2022-06-13 13:25:31.377129
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Run these tests in a separate subprocess to not interfere with other tests
    from ansible import context
    from ansible.cli.playbook import PlaybookCLI
    from ansible.plugins.loader import connection_loader, module_loader, filter_loader
    from ansible.utils.context_objects import AnsibleContext
    from ansible.utils.display import Display
    context._init_global_context(cli=PlaybookCLI(args=[]))
    c = context.global_context
    c.set_playcontext(PlayContext())
    c.defaults = defaults.DefaultLoader()
    c.display = Display()
    c.connection_loader = connection_loader
    c.module_loader = module_loader
    c.filter_loader = filter_loader
    c.ansible_vars = dict()
    c.ansible_

# Generated at 2022-06-13 13:25:41.127557
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    import tempfile

    tmppath = to_bytes(tempfile.mkdtemp())
    with open(os.path.join(tmppath, '__init__.py'), 'wb') as f:
        f.write(b'')

    for filename in os.listdir(pkg_resources.resource_filename(__name__, '../plugins/filter_plugins')):
        with open(os.path.join(tmppath, filename), 'wb') as f:
            f.write(pkg_resources.resource_stream(__name__, '../plugins/filter_plugins/' + filename).read())

    loader = Jinja2Loader()
    loader.add_directory(tmppath)

    # Validate that method get of class Jinja2Loader
    # handles an unknown file

# Generated at 2022-06-13 13:25:49.885201
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # FIXME: temp mock to run this test without need to import modules
    class MockPluginLoader:
        def __call__(self, *args, **kwargs):
            return 'mock_plugin_loader'
    __import__('ansible.plugins.loader').mock_plugin_loader = MockPluginLoader()

    jinja2_loader = Jinja2Loader()

    assert jinja2_loader.get('unknown') is None
    assert jinja2_loader.get('nonexistent.plugin') is None

    assert jinja2_loader.get('mock_plugin_loader') == 'mock_plugin_loader'

    old_sys_path = sys.path
    sys.path = ['./lib']

# Generated at 2022-06-13 13:25:57.964981
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    path = tempfile.mkdtemp()
    for loader in get_all_plugin_loaders():
        obj = loader[1]
        if obj.subdir:
            plugin_path = os.path.join(path, obj.subdir)
            os.makedirs(plugin_path)
            add_fragments(plugin_path, obj.module_utils_path, obj.module_utils_glob)
    add_all_plugin_dirs(path)
    for loader in get_all_plugin_loaders():
        obj = loader[1]
        assert os.path.join(path, obj.subdir) in obj.plugin_dirs

