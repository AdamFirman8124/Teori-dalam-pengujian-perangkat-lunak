

# Generated at 2022-06-13 13:18:00.350371
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
  import unittest
  import os
  class TestAddDirToLoader(unittest.TestCase):
      def setUp(self):
          for loader in get_all_plugin_loaders():
              loader = getattr(sys.modules[__name__], '%s_loader' % loader)
              loader.clear_dirs()

      def test_get_all_plugin_loaders(self):
          '''
          This makes sure that we return the correct list of all the plugin loaders.
          '''
          list_of_all_plugin_loaders = get_all_plugin_loaders()
          list_of_all_plugin_loaders_names = [list_of_all_plugin_loaders[i][0] for i in range(0, len(list_of_all_plugin_loaders)-1)]
         

# Generated at 2022-06-13 13:18:08.827257
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    '''
    Unit test for method find_plugin_with_context of class PluginLoader

    This uses the mock stdlib module: https://docs.python.org/3/library/unittest.mock.html
    to mock methods and attributes of PluginLoader, in order to test the method
    find_plugin_with_context in isolation.
    '''
    import tempfile
    from unittest.mock import patch, MagicMock


# Generated at 2022-06-13 13:18:17.578064
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    args = dict(
        name='action_plugins',
        package='ansible.plugins',
        class_name='ActionBase',
        base_class='ActionBase',
        config_base='action_plugins',
    )
    # test b_path is None
    try:
        # test b_path is None
        pl = PluginLoader(**args)
        # test b_path is ''
        pl = PluginLoader(
            b_path='',
            **args
        )
        # test b_path is '/'
        pl = PluginLoader(
            b_path='/',
            **args
        )
        # test b_path is '/'
        pl = PluginLoader(
            b_path='/',
            suffix='json',
            **args
        )
    except AnsibleError as e:
        raise Assert

# Generated at 2022-06-13 13:18:28.785489
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Check path resolution by plugin loader
    plugin_loader = PluginLoader('ansible.plugins.action', 'ActionModule', 'action_plugins')
    res = plugin_loader.get_with_context('ping')
    assert res.plugin_resolved_name == 'ping'
    assert res.plugin_resolved_path.endswith(os.sep + 'ansible' + os.sep + 'plugins' + os.sep + 'action' + os.sep + 'ping.py')
    assert res.object is not None
    assert res.force_redirect is False
    assert res.redirected_from is None
    assert res.redirect_list == []
    assert res.resolved is True

    # Check path resolution by plugin loader, with a specific path

# Generated at 2022-06-13 13:18:37.276709
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    import shutil
    test_path = tempfile.mkdtemp()
    dirs = {}
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            plugin_path = os.path.join(test_path, to_bytes(obj.subdir))
            os.mkdir(plugin_path)
            obj.add_directory(to_text(plugin_path))
            dirs[name] = plugin_path
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            plugin_paths = obj.get_directories()
            assert plugin_paths == [to_text(dirs[name])]
    shutil.rmtree(test_path)



# Generated at 2022-06-13 13:18:47.513713
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    '''
    Unit test for method all of class PluginLoader
    '''
    from ansible.utils.collection_loader import _get_collection_list
    from .test_module_utils import _mock_module_utils_loader
    # first test we can call the method with no args
    collection_list = _get_collection_list('', None)
    display = Display()
    collection_loader = CollectionLoader('fakes.collection', None, [], _collection_list=collection_list)

    module_loader = PluginLoader('action', 'test_plugins.test_plugin_loader_action',
                                 'TestActionPlugin', collection_loader=collection_loader,
                                 display=display)

    plugins = list(module_loader.all())
    assert len(plugins) == 3, 'Expected 3 action plugins'

# Generated at 2022-06-13 13:18:49.360678
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    assert Jinja2Loader("ansible.plugins.test.test_loader", "ActionModule", "ansible.plugins.test").find_plugin("test_loader.py") == 'test_loader.py'


# Generated at 2022-06-13 13:18:53.363390
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import pdb;  pdb.set_trace()
    manager = PluginLoader('ansible.plugins.lookup', 'LookupModule', C.DEFAULT_LOOKUP_PLUGIN_PATH, 'lookup_plugins')
    lookup_plugin_instance = manager.find_plugin('redis_kv')
    assert lookup_plugin_instance.__class__.__name__ == 'RedisLookupModule'

# Generated at 2022-06-13 13:18:54.340161
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    assert callable(PluginLoader)



# Generated at 2022-06-13 13:19:03.694723
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():

    # expected list of collections for the tested loader
    collections = ['ansible.builtin', 'shared.dummy', 'ansible.netcommon']
    # expected list of plugins (without a collection prefix)
    plugins = ['fileformat', 'meta', 'urls', 'filter_plugins.Dummy', 'filter_plugins.Dummy2', 'filter_plugins.Dummy3']

    # generate the expected list of collections.plugins
    fqcr_list = ['.'.join([c, p]) for c in collections for p in plugins]

    # create an instance of the tested loader
    loader = Jinja2Loader()
    # configure the loader's base path
    loader._basedir = os.path.join(sys.path[0], 'test', 'lib', 'ansible', 'plugins')
    # generate new collection search paths for the loader
    loader

# Generated at 2022-06-13 13:19:39.383192
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    pl = PluginLoader("a.b.c")
    # path and collection_list are not used
    pl.add_directory(path="/", collection_list=None)

    # name is a module, not plugin
    assert pl.find_plugin("foo") is None

    # name is not valid
    with pytest.raises(AnsibleError):
        pl.find_plugin("foo$bar")

    # conflicting names which resolve to different plugins

# Generated at 2022-06-13 13:19:53.152930
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    test_path = '/path/to/plugins'
    ansible_module_loader = PluginLoader('module', '', C.DEFAULT_MODULE_PATH, 'ansible.builtin', C.DEFAULT_MODULE_PATH)
    ansible_module_loader.subdir = 'module_utils'
    ansible_module_loader.package = 'ansible'
    init = '__init__.py'
    class PluginLoaderTestClass:
        def add_directory(self, path):
            self.path = path
    plugin_loader = PluginLoaderTestClass()
    plugin_loader.subdir = 'test/subdir'
    plugin_loader.package = 'test'

# Generated at 2022-06-13 13:20:03.269369
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    class_name = 'ModuleUtil'
    package = 'ansible.utils'
    base_class = None
    aliases = dict()
    collection_list = None
    class_only = False
    local_search_path = None
    name = 'template'
    use_configuration_define = None
    pl = PluginLoader(class_name, package, base_class, aliases, collection_list=collection_list, local_search_path=local_search_path,
                      use_configuration_define=use_configuration_define)
    pl.get_with_context(name, class_only=class_only)
    # It is not possible to check the result, since it is a random attribute of the class

## define constants

# a mapping of plugin types to the relative/absolute paths caches for that type
_PLUGIN_PATH

# Generated at 2022-06-13 13:20:05.173243
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = PluginLoader(package='ansible.plugins.action')
    assert plugin_loader.__contains__(name='copy')



# Generated at 2022-06-13 13:20:16.059970
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pl = PluginLoader('')
    rv = pl.all()
    assert(rv.__class__.__name__ == 'generator')
    # test the actual plugin loading logic
    plclass = PluginLoader('ansible.plugins.connection', 'ConnectionBase', C.DEFAULT_CONNECTION_PLUGIN_PATH)
    rv = plclass.all()
    assert(rv.__class__.__name__ == 'generator')
    # test the actual plugin loading logic
    plclass = PluginLoader('ansible.plugins.lookup', 'LookupBase', C.DEFAULT_LOOKUP_PLUGIN_PATH)
    rv = plclass.all()
    assert(rv.__class__.__name__ == 'generator')
    # test the actual plugin loading logic

# Generated at 2022-06-13 13:20:19.600727
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    '''
    Code for unit testing add_dirs_to_loader
    '''
    from ansible.utils.collection_loader import add_dirs_to_loader

    add_dirs_to_loader(which_loader='module', path=["/path/to/file"])



# Generated at 2022-06-13 13:20:26.545485
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    assert get_shell_plugin('sh').executable == '/bin/sh'
    assert get_shell_plugin(executable='/bin/sh').executable == '/bin/sh'
    assert get_shell_plugin('sh', executable='/bin/bash').executable == '/bin/bash'
    assert get_shell_plugin(executable='/bin/bash').executable == '/bin/bash'
    assert get_shell_plugin('sh', executable='/bin/sh').executable == '/bin/sh'
    assert get_shell_plugin('sh', executable='/bin/csh').executable == '/bin/csh'



# Generated at 2022-06-13 13:20:31.104021
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    class_object = PluginLoadContext()
    assert class_object.record_deprecation('name', 'deprecation', 'collection_name')


# Generated at 2022-06-13 13:20:38.395021
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import ansible.plugins.action.normal
    loader = PluginLoader('action', 'ActionModule',
                          'ansible.plugins.action', C.DEFAULT_INVENTORY_ENABLED_GROUP_PATTERNS)
    module_list = [m for m in loader.all()]
    assert(len(module_list) > 0)

# Generated at 2022-06-13 13:20:47.390601
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # mock the plugin loaders
    global _old_plugin_loaders
    _old_plugin_loaders = list(get_all_plugin_loaders())
    try:
        mock_plugin_loader = PluginLoader("MOCK_PLUGIN_LOADER", "mock_subdir", '', '')
    except:
        raise AssertionError("Could not instantiate PluginLoader")
    # test directory with only expected subdir
    assert len(get_all_plugin_loaders()) == 1
    path = "../test/fixtures/mock_plugin_dir/contains_mock_subdir"
    add_all_plugin_dirs(path)
    assert len(get_all_plugin_loaders()) == 1
    mock_plugin_loader = get_all_plugin_loaders()[0][1]
   

# Generated at 2022-06-13 13:21:24.004939
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():

    class MyJ2(Jinja2Loader):
        def __init__(self, package, class_name, base_class, search_path=None, collection_list=None, collection_list_order=None, j2_env_options=None):
            super(MyJ2, self).__init__(package, class_name, base_class, search_path=search_path, collection_list=collection_list,
                        collection_list_order=collection_list_order, j2_env_options=j2_env_options)

    # Test scenario 1:
    #   Test proper handling of plugin name without '.', which means it is
    #   a legacy plugin (i.e. not a collection plugin).
    #
    #   NOTE: This does not yet account for the fact that base_class == None
    #         because an

# Generated at 2022-06-13 13:21:32.719506
# Unit test for method find_plugin of class PluginLoader

# Generated at 2022-06-13 13:21:43.652941
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    sys.modules.pop('ansible.plugins.action', None)
    sys.modules.pop('ansible.plugins.connection', None)

    # Setup
    action_loader = C.ACTION_PLUGIN_PATH
    connection_loader = C.CONNECTION_PLUGIN_PATH
    loader_config = [action_loader, connection_loader]

    for loader in loader_config:
        loader_instance = globals()[loader]
        loader_instance.directories = []
        for directory in C.DEFAULT_MODULE_PATH:
            loader_instance.add_directory(directory)

    # Execute
    all_plugin_loaders = get_all_plugin_loaders()
    assert all_plugin_loaders
    assert len(all_plugin_loaders) == 1

# Generated at 2022-06-13 13:21:52.100468
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' verify that we can add multiple plugin types in bulk '''
    import tempfile

    # make a temporary directory to place dirs under.
    top_path = tempfile.mkdtemp()
    dirs = defaultdict(tempfile.mkdtemp)

    def cleanup():
        pass
        # Our tempdirs are magically cleaned up by the fact that we're
        # creating them in a with block
        #for dir in dirs.values():
        #    os.rmdir(dir)
        #os.rmdir(top_path)

    # make some mock plugin dirs of different types:

# Generated at 2022-06-13 13:21:57.414794
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader(package='ansible.plugins.connection', class_name='ConnectionBase')
    # test normal use case
    plugin_load_context = plugin_loader.find_plugin_with_context('local')
    assert plugin_load_context.resolved


# Generated at 2022-06-13 13:21:59.370085
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    j = Jinja2Loader("ansible.plugins.action", "ActionModule")
    with pytest.raises(AnsibleError):
        j.find_plugin("fooo")


# Generated at 2022-06-13 13:22:09.601554
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    # This is a destructive test and requires a new instance of the class,
    # and should be called with a unique temp directory
    # Also, it modifies ansible.constants.
    # Test id: 2020102404315833-50186-423784
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp(prefix="ansible_test_PluginLoader_")
    C.DEFAULT_MODULE_PATH.append(tmpdir)
    pl = PluginLoader('test', package='test.test')
    pl.add_directory(tmpdir)

# Generated at 2022-06-13 13:22:20.427892
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    """ Unit test for method get_with_context of class PluginLoader """
    class DummyPluginLoader(PluginLoader):
        pass
    try:
        from ansible.vars.hostvars import HostVars
        from ansible.vars import DefaultVars
        from ansible.vars.manager import create_vars_files
    except Exception:
        pytest.skip("unable to import ansible modules")
    if not os.path.exists(HOST_VARS_PATH):
        os.makedirs(HOST_VARS_PATH)
    create_vars_files(HOST_VARS_PATH)
    # create test file
    with open(os.path.join(HOST_VARS_PATH, 'localhost'), 'wb') as f:
        f.write(b'localhost:')
    host

# Generated at 2022-06-13 13:22:34.121123
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'test_utils'))
    import base_plugin_loader_test

    # Test adding good path to get_plugin_loaders()
    plugin_loader_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_utils', 'collection_loader_plugins')
    add_all_plugin_dirs(plugin_loader_path)
    # Both namespaces are searchable

# Generated at 2022-06-13 13:22:44.977564
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    p = PluginLoadContext()
    print(p.deprecation_warnings)
    p.record_deprecation('name', {'warning_text': 'text'}, 'collection')
    print(p.deprecation_warnings)
    p.record_deprecation('name', {'warning_text': 'text', 'removal_version': '2.0'}, 'collection')
    print(p.deprecation_warnings)
    p.record_deprecation('name', {'warning_text': 'text', 'removal_version': '2.0', 'removal_date': '2020-02-02'}, 'collection')
    print(p.deprecation_warnings)

# Generated at 2022-06-13 13:23:16.593412
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    assert False, "Write a unit test for this function"



# Generated at 2022-06-13 13:23:25.926038
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' Ensure add_all_plugin_dirs works correctly. '''
    fn = '/tmp/plugins'
    add_all_plugin_dirs(fn)
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            assert(fn not in obj.plugin_dirs)
    # Add the directory to a plugin
    obj.add_directory(fn)
    add_all_plugin_dirs(fn)
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            assert(fn in obj.plugin_dirs)



# Generated at 2022-06-13 13:23:32.986254
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    jinja_loader = PluginLoader(
        'ansible.legacy.plugins.filter.tests',
        'FilterModule',
        'filter_plugins',
        required_base_class='FilterModule',
    )
    # access after ctor to load plugins
    _ = jinja_loader._get_paths()

    with pytest.raises(AnsibleError) as exception_info:
        jinja_loader.find_plugin('Ansible.legacy.plugins.filter.tests.test')

    assert 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)' in str(exception_info)



# Generated at 2022-06-13 13:23:46.048763
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader(
        package='package',
        class_name='class_name',
        config=None,
        subdir='subdir',
        aliases={},
        required_base_class=None
    )

    # Path: /home/bobby/src/ansible/lib/ansible/plugins/subdir/__init__.py
    # Note: Will not find the plugin in this file
    __init___py_path = '/home/bobby/src/ansible/lib/ansible/plugins/subdir/__init__.py'

    # Path: /home/bobby/src/ansible/lib/ansible/plugins/subdir/action/baz.py

# Generated at 2022-06-13 13:23:54.888145
# Unit test for method all of class PluginLoader

# Generated at 2022-06-13 13:24:03.925904
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    # Test when loader is 'action'
    which_loader = 'action'
    paths = ['/path/to/action/1','/path/to/action/2']
    add_dirs_to_loader(which_loader, paths)
    assert sys.modules[__name__].action_loader.module_paths == paths
    # Test when loader is 'cache'
    which_loader = 'cache'
    paths = ['/path/to/cache/1','/path/to/cache/2']
    add_dirs_to_loader(which_loader, paths)
    assert sys.modules[__name__].cache_loader.module_paths == paths
    # Test when loader is 'callback'
    which_loader = 'callback'

# Generated at 2022-06-13 13:24:15.514448
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    def assert_fqcr_is_same(original, actual):
        assert original.namespace == actual.namespace
        assert original.collection == actual.collection
        assert original.plugin_type == actual.plugin_type
        assert original.name == actual.name

    plugin_loader = PluginLoader("my_type", "my_package.my_class", C.config, 'my_module')
    # monkey patch for the purpose of testing
    plugin_loader._find_plugin_in_dir = MagicMock(name="_find_plugin_in_dir")
    plugin_loader._find_fq_plugin = MagicMock(name="_find_fq_plugin")

    # test basic functionality
    plugin_loader._find_plugin_in_dir.return_value = 'my_path'
    load_context = plugin_loader.find

# Generated at 2022-06-13 13:24:23.957021
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    all_plugin_loader_instances = PluginLoader.all(return_type='instance', args=None, kwargs=None)
    all_plugin_loader_classes = PluginLoader.all(return_type='class', args=None, kwargs=None)
    all_plugin_loader_paths = PluginLoader.all(return_type='path', args=None, kwargs=None)

# Generated at 2022-06-13 13:24:34.429832
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    closure = {
        'actual': None
    }

    def call_function():
        # create an instance of PluginLoader
        plugin_loader = PluginLoader(
            package='ansible.plugins.cache',
            class_name='CacheModule',
            config_base=dict(),
            subdir=None,
            aliases=None,
            class_only=False,
            required_base_class='CacheModule',
            base_class='CacheModule')

        # call the method
        return plugin_loader.find_plugin(name='memory')

    # check if the returned value is correct type
    assert isinstance(call_function(), type(closure))
    # check if the returned value is correct
    assert call_function() == closure


# Generated at 2022-06-13 13:24:36.867405
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method __contains__ of class PluginLoader
    '''
    # The function is not implemented yet
    assert not __contains__()


# Generated at 2022-06-13 13:25:16.940868
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    fake_dir = os.path.join(os.path.dirname(__file__), '__fakedir__')
    os.mkdir(fake_dir)
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            os.mkdir(os.path.join(fake_dir, obj.subdir))
    try:
        add_all_plugin_dirs(fake_dir)
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                assert obj.directories == [os.path.join(fake_dir, obj.subdir)]
    finally:
        os.rmdir(fake_dir)



# Generated at 2022-06-13 13:25:26.254829
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # Setup test data
    nope_msg = 'nope'
    path_to_redirect = 'path/to/redirect'
    plugin_load_context = PluginLoaderContext()
    plugin_load_context_nope = PluginLoaderContext()
    plugin_load_context_nope.nope(nope_msg)

    # Mock methods that return plugin_load_context
    mock1 = MagicMock()
    mock1.return_value = plugin_load_context_nope
    mock2 = MagicMock()
    mock2.return_value = plugin_load_context
    mock3 = MagicMock()
    mock3.return_value = plugin_load_context_nope
    mock4 = MagicMock()
    mock4.return_value = plugin_load_context

    # Mock find_plugin_with_

# Generated at 2022-06-13 13:25:37.112817
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    obj = PluginLoader(package=None, search_paths=None, class_name=None, config_base=None, subdir=None)
    path = None
    setup_loader_mock = MagicMock()
    obj.setup_loader = setup_loader_mock
    setup_loader_mock.return_value = path
    suffix = None
    plugin_load_context_mock = MagicMock()
    obj.find_plugin_with_context = MagicMock()
    obj.find_plugin_with_context.return_value = plugin_load_context_mock
    module_cache = dict()
    obj._module_cache = module_cache
    load_module_source_mock = MagicMock()
    obj._load_module_source = load_module_source_mock
    load_module_source

# Generated at 2022-06-13 13:25:46.309888
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    # Create a temporary directory
    # We cannot use @mock_open because the call to add_all_plugin_dirs uses os.path.isdir()
    # which cannot be mocked
    temp_dir = tempfile.mkdtemp()
    plugin_dir = os.path.join(temp_dir, 'plugins')
    os.mkdir(plugin_dir)


# Generated at 2022-06-13 13:25:53.185231
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader('foo', 'bar', 'baz', 'qux')
    ansible_collections = ['ansible.collections.dummy']

    # Test 1 : tell plugin loader to find plugin called 'test' without any collection
    # and without any plugin_path
    # expected : plugin loader returns nope saying candidate path is not eligible for resolution
    assert plugin_loader.find_plugin("test") == plugin_loader.nope("candidate path is not eligible for resolution")

    # Test 2 : tell plugin loader to find plugin called 'test' with collection list set to
    # ansible_collections and without any plugin_path
    # expected : plugin loader returns nope saying candidate path is not eligible for resolution