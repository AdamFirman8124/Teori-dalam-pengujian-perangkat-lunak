

# Generated at 2022-06-13 13:17:53.553821
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    for return_val in [False, True]:
        for is_plugin in [False, True]:
            for is_contained in [False, True]:
                if is_contained == return_val:
                    continue
                loader = PluginLoader(os.path.normpath('collection/ns/plugins/module_utils'), '', '', '', '', subdir='plugins')
                check_none = False
                if is_plugin:
                    if is_contained:
                        obj = object()
                        loader.get_with_context = MagicMock()
                        loader.get_with_context.return_value.object = obj
                        check_none = True
                    else:
                        loader.find_plugin_with_context = MagicMock()
                        loader.find_plugin_with_context.return_value.nope.return_value = return_val
               

# Generated at 2022-06-13 13:18:01.013820
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    dsp = Display()
    which_loader = "module"
    loader = getattr(sys.modules[__name__], '%s_loader' % which_loader)
    paths = []
    paths.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_plugin_testplugin.py"))
    loader.add_directory(paths[0], with_subdir=True)
    obj = loader.all()
    dsp.display(obj)

    for path in paths:
        os.remove(path)

    assert True == True




# Generated at 2022-06-13 13:18:03.234066
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    test_class = Jinja2Loader('filter_plugins', 'ansible.plugins.filter_plugins.filter_loader')
    assert [] == list(test_class.all())


# Generated at 2022-06-13 13:18:10.412989
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    display = Display()
    class PluginLoader:
        plugin_path = []
        subdir = ''
    plugin_loader = PluginLoader()
    def add_directory(path):
        plugin_loader.plugin_path.append(to_text(path))
    plugin_loader.add_directory = add_directory
    for name, obj in globals().items():
        if name == 'plugin_loader':
            globals()[name] = obj
    # Case 1: Add plugin dir with invalid path
    plugin_loader.plugin_path = []
    path = 'home/user/invalid_path'
    add_all_plugin_dirs(path)
    assert plugin_loader.plugin_path == []
    # Case 2: Add plugin dir with valid path
    plugin_loader.plugin_path = []
    path = ''
    add_

# Generated at 2022-06-13 13:18:16.702188
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    try:
        test_shell = get_shell_plugin()
        raise AssertionError("get_shell_plugin() should raise an exception when not provided arguments")
    except AnsibleError as e:
        assert "either a shell type or a shell executable must be provided" in to_native(e)

    test_shell = get_shell_plugin(shell_type="sh")

    assert test_shell.SHELL_FAMILY == "sh"
    assert test_shell.IGOR_DONE == "done"
    assert test_shell.BATCHFILE_ENV == "set"



# Generated at 2022-06-13 13:18:26.037522
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    module_argv = json.loads(MODULE_ARGV)
    with patch.object(sys, 'argv', module_argv):
        # initialize
        global_symbols = globals()
        global_symbols['get_distribution'] = MagicMock()
        global_symbols['get_distribution'].return_value = None
        global_symbols['importlib_metadata'] = MagicMock()
        global_symbols['importlib_metadata'].version = MagicMock()
        global_symbols['importlib_metadata'].version.return_value = "2.0.0"

        version_info = global_symbols['version_info']
        version_info_mock = MagicMock(return_value=version_info)

# Generated at 2022-06-13 13:18:31.777107
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    j2loader = Jinja2Loader('ansible.plugins.test_plugin', 'Test_plugin', 'plugins/test_plugin', 'plugins/test_plugin', 'test_plugin.py')
    # No files currently in test directory
    #with pytest.raises(AnsibleError) as error:
    #    j2loader.find_plugin("a_file")
    #assert 'file or collection could not be loaded' in str(error.value)
    #assert 'does not exist' in str(error.value)
    #with pytest.raises(AnsibleError) as error:
    #    j2loader.find_plugin("no_collection")
    #assert 'file or collection could not be loaded' in str(error.value)
    #assert 'no such collection' in str(error.value)
    #with py

# Generated at 2022-06-13 13:18:34.231267
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():

    # Test for method __contains__(self, parameter_list)
    # of class PluginLoader
    # This method is not being tested

    pass


# Generated at 2022-06-13 13:18:39.348869
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    def test_add_dirs_to_loader_add_directory(self, d):
        for dir in d:
            self._paths.append(dir)

    from ansible.plugins import module_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.action import ActionModule
    from ansible.plugins.lookup import LookupModule
    from ansible.plugins.become import BecomeModule
    from ansible.plugins.connection import ConnectionModule
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.shell import ShellModule

    p = [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plugins')]
    test_dirs = ['shell_plugins']
    module_loader.add_directory = test_add_dir

# Generated at 2022-06-13 13:18:44.885311
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    from ansible.compat.tests.mock import Mock, call, patch
    from ansible.utils.collection_loader import add_dirs_to_loader
    mock_loader = Mock()
    with patch.dict("sys.modules", {'ansible.utils.collection_loader': mock_loader}):
        with patch('glob.glob') as mock_glob:
            with patch('os.path.isdir') as mock_isdir:
                mock_glob.return_value = ['a', 'b']
                mock_isdir.side_effect = [True, False]
                add_dirs_to_loader('action', ['a', 'b'])
                mock_loader.assert_has_calls([call.action_loader.add_directory('a', with_subdir=True)])



# Generated at 2022-06-13 13:19:26.005728
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    dummy_loader = Jinja2Loader(package="ansible.legacy",
                                subdir="test_plugins",
                                base_class="TestPlugin",
                                )
    assert isinstance(dummy_loader.get("plugin_name"), TestPlugin)
    assert isinstance(dummy_loader.get("my_col.my_ns.my_plugin"), TestPlugin)



# Generated at 2022-06-13 13:19:30.351286
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    p = PluginLoader('ansible.plugins.action', 'ActionModule', 'action_plugins')
    plugin_load_context = p.find_plugin_with_context('copy')
    print(plugin_load_context.to_json())


# Generated at 2022-06-13 13:19:37.687954
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    unit_test_name = 'test_Jinja2Loader'

    loader = Jinja2Loader(paths=['/path/to/dir'])
    with patch.object(loader, 'get') as mock_get:
        loader.find_plugin(unit_test_name)
        mock_get.assert_called_with(unit_test_name)

    loader = Jinja2Loader(paths=['/path/to/dir:collection'])
    with patch.object(loader, 'get') as mock_get:
        loader.find_plugin(unit_test_name)
        mock_get.assert_called_with('collection.%s' % unit_test_name)



# Generated at 2022-06-13 13:19:51.680078
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    def test_plugin(obj, *args, **kwargs):
        if obj is None:
            raise Exception("obj is None")
        if not isinstance(obj, MyPlugin):
            raise Exception("obj is not a MyPlugin")

    class MyPlugin(object):
        def __init__(self):
            pass

    class PluginLoaderNoredirect(PluginLoader):
        _redirect_map = {}

    class PluginLoaderNoAlias(PluginLoader):
        _redirect_map = {}

        def __init__(self):
            super(PluginLoaderNoAlias, self).__init__('ansible.plugins.action', 'ActionModule', C.DEFAULT_INTERNAL_PLUGINS)


# Generated at 2022-06-13 13:19:55.645007
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    """
    Check if the method adds a directory to the _directories list
    """
    loader = PluginLoader('/fake/package', 'fake.class')
    assert len(loader._directories) == 0
    loader.add_directory('/fake/directory')
    assert len(loader._directories) == 1
    assert loader._directories[0] == '/fake/directory'


# Generated at 2022-06-13 13:20:05.018768
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    import pytest
    from ansible.errors import AnsibleError

    # Basic return valid plugin
    loader = PluginLoader('test_plugins')
    obj = loader.get_with_context('test_plugins/test')
    assert isinstance(obj, get_with_context_result)
    assert obj.object is not None
    assert obj.plugin_load_context is not None
    assert obj.plugin_load_context.resolved is True
    assert obj.plugin_load_context.plugin_resolved_name == 'test_plugins/test'
    assert os.path.splitext(obj.plugin_load_context.plugin_resolved_path)[0].endswith('test_plugins/test')

    # Basic return invalid plugin
    obj = loader.get_with_context('test_plugins/invalid')

# Generated at 2022-06-13 13:20:15.357203
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # Dummy classes for the plugin base class and for testing
    class C(object):
        pass
    class D(C):
        pass
    # Dummy plugin path
    plugin_path = tempfile.mkdtemp()
    # Add the plugin path to our module search paths
    sys.path.append(plugin_path)
    # Fake plugin, it's just a loader for a test class
    plugin_name = 'ansible_test_plugin'
    plugin_dir = os.path.join(plugin_path, plugin_name)
    plugin_file = os.path.join(plugin_dir, '__init__.py')
    os.makedirs(plugin_dir)

# Generated at 2022-06-13 13:20:24.130141
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    import imp
    import platform
    imp.load_source('platform', '/Users/myself/venv/ansible/lib/python2.7/site-packages/ansible/module_utils/basic.py')
    from ansible.module_utils.basic import AnsibleModule  # noqa: F401

    from ansible.plugins.test.test_filter.test_dict import TestDictFilter  # noqa: F401

    # Sample Loader to test
    loader = Jinja2Loader(package='ansible.plugins.filter', base_class='FilterModule')

    # Test result
    r = loader.get('ansible.plugins.filter.test_dict',
        collection_list=['ansible_collections.ansible.test']
    )

    # Verify we got expected object back

# Generated at 2022-06-13 13:20:38.275270
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    import ansible.plugins.loader as loader

    # test first call
    loader.get_plugin_loader.im_func.cache_clear()
    loader_get = loader.get_plugin_loader.im_func
    from ansible.plugins.action import ActionModule
    assert loader_get('action') == loader.PluginLoader('action', 'ActionModule')

    # test call with different name
    assert loader_get('lookup') == loader.PluginLoader('lookup', 'LookupModule')

    # test cache is used
    jinja2_loader = loader.PluginLoader('lookup', 'LookupModule')
    loader.get_plugin_loader.im_func.cache_clear()
    assert loader_get('lookup') == jinja2_loader



# Generated at 2022-06-13 13:20:40.379193
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    PluginLoader(package='ansible.plugins.cache', directories=[])



# Generated at 2022-06-13 13:23:54.263879
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    """
    Ensure we get back a shell plugin when searched for shell plugin
    """
    shell_plugin = get_shell_plugin()
    assert shell_plugin.SHELL_FAMILY == 'sh'


# Generated at 2022-06-13 13:24:01.546880
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # in-context test, need a non-empty plugin_dir
    tmp_plugin_dir = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
    os.mkdir(tmp_plugin_dir)

    # create a dummy module to load
    dummy_mod_name = 'dummy.py'

# Generated at 2022-06-13 13:24:07.152952
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
  global _PLUGIN_FILTERS

  _PLUGIN_FILTERS = {
    'ansible.plugins.filter.core': ['__init__.py'],
    'ansible.plugins.filter': ['__init__.py', 'core.py']
  }

  # This is wrong for few reasons.
  # 1. get method has 'name' argument, not 'dir'
  # 2. It sets 'searched_paths', which is readonly property.
  # 3. It gets a tuple of paths.
  # 4. It retrieves a plugin by name, but the name is path.
  loader = Jinja2Loader('ansible.plugins.filter', 'FilterModule', 'filter_plugins', collection_list=None)
  loader.searched_paths=('/foo/bar',)

# Generated at 2022-06-13 13:24:17.384696
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Get a test fixture
    PLUGIN_LOADER_FIXTURE = PluginLoaderFixture()
    PLUGIN_LOADER_FIXTURE.setup()

    # Example for path_only=True
    # Create a plugin loader for action plugins
    loader = PluginLoader(
        "ActionModule",
        "ansible.plugins.action",
        C.DEFAULT_ACTION_PLUGIN_PATH,
        "action_plugins",
        required_base_class="ActionBase"
    )

    # Call the method under test
    path_only = True
    for plugin in loader.all(path_only=path_only):
        # The plugin should be a string
        assert(type(plugin) is str)
        assert(plugin == PLUGIN_LOADER_FIXTURE.action_plugin_path)

    # Example for class

# Generated at 2022-06-13 13:24:31.318545
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    loader = PluginLoader('foo')
    plugin_load_context = loader.find_plugin_with_context('bar')
    assert(plugin_load_context.resolved == False)
    plugin_resolved_name = 'ansible.plugins.action.synchronize'
    plugin_resolved_path = '/some/path'
    plugin_resolved_fqcr = 'ansible_collections.org.some.collection.foo.bar'
    plugin_redirected_name = 'ansible.plugins.connection.ssh'
    plugin_redirected_path = '/some/other/path'
    plugin_redirected_fqcr = 'ansible_collections.org.some.other.collection.foo.bar'
    redirect_list = [plugin_redirected_path]
    plugin_load_context = PluginLoad

# Generated at 2022-06-13 13:24:38.280767
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    try:
        from __main__ import display
    except ImportError:
        display = None
    loader = PluginLoader(
        'callback',
        'ansible.plugins.callback',
        'CallbackModule',
        'announce'
    )
    plugins = loader.all()
    plugin_list = list(plugins)
    assert plugin_list
    for plugin in plugin_list:
        assert plugin.__class__.__name__.endswith('Plugin')
        assert hasattr(plugin, 'run')


# Unit tests for get_with_context and find_plugin_with_context of PluginLoader

# Generated at 2022-06-13 13:24:48.275259
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_text
    import ansible_collections.foo.bar
    import ansible_collections.foo.baz


# Generated at 2022-06-13 13:24:55.315604
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    class PluginLoaderTest(object):
        subdir = 'plugins'
        def __init__(self):
            self.paths = []
        def add_directory(self, path):
            self.paths.append(path)
    p = PluginLoaderTest()
    globals()['PluginLoaderTest'] = PluginLoaderTest
    add_all_plugin_dirs('/TestPath')
    assert p.paths == []
    os.mkdir('/TestPath')
    add_all_plugin_dirs('/TestPath')
    assert p.paths == []
    os.mkdir('/TestPath/plugins')
    add_all_plugin_dirs('/TestPath')
    assert p.paths == ['/TestPath/plugins']
    p.paths = []

# Generated at 2022-06-13 13:25:06.766150
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():

    # deprecation dict with all of the keys
    d = {
        "warning_text": "This module is going to be removed in a future release, use xyz instead.",
        "removal_date": "2020-01-01",
        "removal_version": "2.1.0",
    }

    # Test with all of the keys in the dict
    load_context = PluginLoadContext()
    assert load_context.record_deprecation('foo', d, collection_name='bar') == load_context
    assert load_context.resolved is False
    assert load_context.deprecated is True
    assert load_context.removal_date == "2020-01-01"
    assert load_context.removal_version == "2.1.0"

# Generated at 2022-06-13 13:25:09.489474
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    class_instance = Jinja2Loader(None, None)
    assert class_instance.find_plugin('my_plugin') == None
