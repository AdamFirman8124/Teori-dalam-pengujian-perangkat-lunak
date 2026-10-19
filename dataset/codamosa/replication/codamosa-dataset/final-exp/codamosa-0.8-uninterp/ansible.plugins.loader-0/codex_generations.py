

# Generated at 2022-06-13 13:17:40.584475
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    pass

# Generated at 2022-06-13 13:17:49.608456
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    get_shell_plugin(shell_type="sh", executable="/bin/fake_shell")
    module_to_test = None
    fakeshell_path = os.path.join(C.DEFAULT_MODULE_PATH, "shell")
    for path in sys.modules[__name__].shell_loader.get_plugin_paths(subdir=None):
        if "test_shell" in path:
            module_to_test = path

    assert module_to_test == os.path.join(fakeshell_path, 'test_shell')

# ---


# Generated at 2022-06-13 13:17:53.184506
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    '''
    Unit test for plugin Loader method
    '''
    loader = PluginLoader("", "", "")
    loader.add_directory("")
    assert loader.dir_list


# Generated at 2022-06-13 13:17:55.407334
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # This test is for a private method
    assert False, 'Test not implemented'


# Generated at 2022-06-13 13:18:03.994439
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():

    #
    # This tests the all method of PluginLoader.
    #

    # Verify loading with no plugins
    p = PluginLoader('__not_a_real_package__', 'not_a_real_base_class', 'not_a_real_class')
    assert list(p.all()) == []

    # Verify loading with no module.
    p = PluginLoader('__not_a_real_package__', 'not_a_real_base_class', 'not_a_real_class')
    assert list(p.all(os.devnull)) == []

    # Verify loading with a real but empty module.
    p = PluginLoader('ansible.module_utils.logging', 'LoggingBase', 'LoggingBase')
    assert list(p.all(os.devnull)) == []

    # Verify loading.
    p

# Generated at 2022-06-13 13:18:14.477749
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pl = PluginLoader('name', 'path', 'parent', 'subdir')
    os.makedirs(os.path.join('path', 'subdir'))
    f = open(os.path.join('path', 'subdir', 'test_plugin.py'), 'w')
    f.close()
    f = open(os.path.join('path', 'subdir', 'test_plugin.pyc'), 'w')
    f.close()
    f = open(os.path.join('path', 'subdir', 'test_plugin.pyo'), 'w')
    f.close()

    list(pl.all(path_only=True))
    list(pl.all(class_only=True))

    # FIXME: Make this test more complete


# Generated at 2022-06-13 13:18:19.314161
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    PLUGIN_PATH_CACHE.clear()
    # Testing case when path is not a directory
    add_all_plugin_dirs(os.path.join(os.path.dirname(__file__), "not_a_directory"))
    assert len(PLUGIN_PATH_CACHE) == 0
    # Testing case when path is a directory
    add_all_plugin_dirs(os.path.dirname(__file__))
    assert len(PLUGIN_PATH_CACHE) == 4



# Generated at 2022-06-13 13:18:21.607005
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    instance = PluginLoader('', '', '', '', '')
    assert not (instance.__contains__(''))


# Generated at 2022-06-13 13:18:31.798623
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Ensure that add_all_plugin_dirs tries to add all plugin dirs
    # and gives a warning when it can't
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import PATH_CACHE
    from ansible.plugins.loader import PLUGIN_PATH_CACHE
    from ansible.plugins.loader import MODULE_CACHE
    # First, clear cache
    for lst in (PATH_CACHE, PLUGIN_PATH_CACHE, MODULE_CACHE):
        lst.clear()
    # Create an invalid path and a directory
    from tempfile import mkdtemp
    import shutil
    b_fake_plugin_path = to_bytes(mkdtemp())
    b_plugin_path = to_bytes(mkdtemp())


# Generated at 2022-06-13 13:18:38.349864
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():

    plugin_loader = PluginLoader("action_plugin")
    plugin_load_context = plugin_loader.get_with_context("ping").plugin_load_context

    assert("Cannot import the required Python library" in plugin_load_context.error_message)
    assert("ping" in plugin_load_context.error_message)

    plugin_load_context = plugin_loader.get_with_context("copy").plugin_load_context

    assert("Cannot import the required Python library" not in plugin_load_context.error_message)
    assert("ping" not in plugin_load_context.error_message)


# Generated at 2022-06-13 13:19:59.956576
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    # No param, should not change self._directories
    class TestClass1(PluginLoader):
        def __init__(self, package, directories=[]):
            self.package = package
            self._directories = directories
    test_obj1 = TestClass1('ansible.plugins.test_module')
    result = test_obj1.add_directory()
    assert test_obj1._directories == []
    assert result == None

    # Param as a str type, should add to self._directories
    class TestClass2(PluginLoader):
        def __init__(self, package, directories=[]):
            self.package = package
            self._directories = directories
    test_obj2 = TestClass2('ansible.plugins.test_module')
    result = test_obj2.add_directory('test_directory')

# Generated at 2022-06-13 13:20:07.697916
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():

    # Tests covering the 'redirect' feature
    # Pretty much all the tests currently cover the redirect feature.  If that is ever removed,
    # then we should probably write some more tests to cover the non-redirect case.

    # find_plugin is the central method of the plugin loader and the most complex
    # it is tested indirectly by each of the other methods, but it is also tested here
    # directly to ensure thorough coverage.
    #
    # this method tests the find_plugin method for the connection plugin loader
    # (the only loader with a base_class configured)
    #
    # this method should catch any breakage resulting from changes to _match_plugin and _get_plugin_path

    # remove these once we have a better, more generic test harness
    from ansible import constants as C
    from ansible.utils.display import Display

# Generated at 2022-06-13 13:20:18.652002
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    '''
    Unit test for method add_directory of class PluginLoader
    '''

    # First ensure the base class for the PluginLoader can be instantiated
    try:
        pl = PluginLoader('')
    except:
        assert False, 'Unable to instantiate PluginLoader base class'

    # Then create an instance of the class to test
    test_pl = PluginLoader('ansible.plugins.test_plugins')

    # Add a plugin directory to the list to later ensure it is removed
    # Use the same directory for both calls as if we used different directories
    # the call to remove would remove all directories and we would get an
    # error on the remove call.
    test_dir = os.path.join(os.getcwd(), 'unit/results/ansible_plugins/test_plugins')

# Generated at 2022-06-13 13:20:27.609722
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    plugin_load_context = _init_plugin_loader().find_plugin_with_context('one_plugin')
    assert plugin_load_context, 'plugin loader find_plugin_with_context stored a plugin load context'
    assert plugin_load_context.plugin_resolved_name == 'one_plugin', 'plugin load context resolved name %s expected one_plugin' % plugin_load_context.plugin_resolved_name
    assert plugin_load_context.plugin_resolved_path, 'plugin load context resolved path was not set'
    assert plugin_load_context.plugin_resolved_path.endswith('one_plugin.py'), 'plugin load context resolved path %s was not a path ending in one_plugin.py' % plugin_load_context.plugin_resolved_path

# Generated at 2022-06-13 13:20:41.697408
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    #Test with a valid directory path
    loader = PluginLoader(
        'unit_test',
        'unit_test_collection.plugins',
        'unit_test_collection.plugins_package.unit_test'
    )
    loader.add_directory(to_bytes(os.path.join(os.path.dirname(__file__), '..', 'test_collections', 'unit_test_collection', 'plugins_package')))
    #Test with a non existant directory path
    loader = PluginLoader(
        'unit_test',
        'unit_test_collection.plugins',
        'unit_test_collection.plugins_package.unit_test'
    )

# Generated at 2022-06-13 13:20:54.411997
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    all_plugin_loaders = get_all_plugin_loaders()
    for _, obj in all_plugin_loaders:
        obj.directories = []
        obj.plugin_path_cache = {}
        obj.plugin_packages = []
        obj.plugin_pkg_namespace = {}

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'ansible', 'modules'))
    add_all_plugin_dirs(path)
    for _, obj in all_plugin_loaders:
        assert obj.directories == [os.path.abspath(path)]
        assert obj.plugin_path_cache == {}
        assert obj.plugin_packages == []
        assert obj.plugin_pkg_namespace == {}


# Generated at 2022-06-13 13:20:56.575835
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
  plugin_loader = PluginLoader(
      package='ansible.plugins.action',
      config=dict(),
      subdir='actions',
      aliases={},
      class_name='ActionModule'
  )
  plugin_loader.add_directory('/home/k/ansible/lib/ansible/plugins/action')


# Generated at 2022-06-13 13:21:07.471415
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():

    with mock.patch.object(os.path, 'isdir', mock.MagicMock(return_value=False)):
        from ansible.plugins.loader import Jinja2Loader
        mock_config_loader = mock.MagicMock()
        mock_config_loader.get_config_value.return_value = "."
        plugin_loader = Jinja2Loader(config_loader=mock_config_loader, package='unit_tests.unit_tests_files.plugins')
        mock_os_path_sep = mock.patch('os.path.sep', new='/')(plugin_loader)
        mock_path_exists = mock.patch('os.path.exists', new=lambda _path: True)(plugin_loader)

# Generated at 2022-06-13 13:21:17.643815
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    from ansible.parsing.dataloader import DataLoader
    import ansible.playbook.play as play

    paths = [os.path.join(os.path.dirname(play.__file__), 'plugins', 'action')]
    add_dirs_to_loader('action', paths)
    assert ActionModule in action_loader._plugin_classes.values()

    del action_loader._plugin_classes
    action_loader.plugin_manager.plugin_loaders = {}
    loader = DataLoader()
    action_loader = PluginLoader('ActionModule', 'ansible.plugins.action',
                                 C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins',
                                 'action', 'ansible.plugins.action', loader, enable_plugins=True)

# Generated at 2022-06-13 13:21:24.629756
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    test_variable = {
        "path": [
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plugins', 'connection'),
        ]
    }
    add_dirs_to_loader("connection", test_variable["path"])
    assert sys.modules[__name__].connection_loader.paths[0] == test_variable["path"][0]



# Generated at 2022-06-13 13:21:54.349150
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Testcase 1: Fetch module named 'ping'
    p = PluginLoader('Module')
    module_data = p.get_with_context('ping')
    assert (module_data.object.__doc__ == "This is a core module that is always available in Ansible, it's loaded from ANSIBLE_LIBRARY and does not need to be installed.")
    # Testcase 2: Fetch callback named 'redis'
    p = PluginLoader('CallbackModule','callback')
    callback_data = p.get_with_context('redis')
    assert (callback_data.object.__doc__ == "This is an stdout callback that writes events to the redis cache")


# Generated at 2022-06-13 13:21:56.823238
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    from ansible.module_utils.common.collections import PluginLoader
    loader_instance = PluginLoader('module_utils', 'ansible.module_utils', 'AnsibleModule')
    assert loader_instance.get_with_context('test') is None

# Generated at 2022-06-13 13:22:03.871312
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    init_args = dict(package="ansible.template",
                     subdir="filter_plugins",
                     aliases={},
                     required_base_class="FilterModule",
                     )
    # This is a test to ensure that find_plugin() for Jinja2Loaders utilizes the collection_list
    # argument and does not load anything from 'ansible.legacy'.
    #
    # This test is in response to PR ansible/ansible#42031.
    #
    # In that PR, the testing code that loads the filters and tests for a template sees a bug
    # where the pluginloader code finds a jinja2 test named 'defined' which ends up being the
    # 'defined' test from the ansible.legacy collection instead of the one from 'ansible.builtin'.
    # The fix is to use the 'collection_list' argument to pass

# Generated at 2022-06-13 13:22:10.724312
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dirpath = os.path.join(dirname, 'test_utils/test_plugins/test_add_all_plugin_dirs')
    add_all_plugin_dirs(dirpath)
    base = '/'.join(dirpath.split('/')[:-1])
    a_path = os.path.join(base, 'action_plugin')
    filter_plugin_path = os.path.join(base, 'filter_plugin')
    connection_plugin_path = os.path.join(base, 'connection_plugin')
    lookup_plugin_path = os.path.join(base, 'lookup_plugin')

# Generated at 2022-06-13 13:22:17.477654
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
  class Mock_self():
    def __init__(self, package, subdir, base_class, class_name):
      self.package = package
      self.subdir = subdir
      self.base_class = base_class
      self.class_name = class_name

    def _get_paths(self):
      return ('/home/robert/ansible/lib/ansible/plugins/cliconf',
              '/home/robert/ansible/lib/ansible/plugins/module_utils',
              '/home/robert/ansible/lib/ansible/plugins/action')

    def _module_cache(self):
      return dict()

    def _load_module_source(self, name, path):
      return dict(name=name, path=path)


# Generated at 2022-06-13 13:22:24.492287
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    """
    [Unit test for function add_all_plugin_dirs in module ansible.plugins.loader]

    [Description]
    Validates the function add_all_plugin_dirs in module ansible.plugins.loader when providing a valid path.

    [Work Items]
    Make sure to cover the following code paths:
    - Ensure all plugin subdirs are added to the loader path when a valid path is provided.
    - Ensure all plugin subdirs are not added to the loader path when an invalid path is provided.
    """
    # Setup
    path = './lib/ansible/config'
    # Test
    add_all_plugin_dirs(path)

    # Verify

# Generated at 2022-06-13 13:22:32.230636
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # assume class name is Jinja2Loader
    jinja2loader = Jinja2Loader()
    # assume get returns a Jinja2Loader object
    jinja2loader_object = jinja2loader.get("ansible.legacy")
    # assume the return of get is a Jinja2Loader class
    assert isinstance(jinja2loader_object, Jinja2Loader)



# Generated at 2022-06-13 13:22:34.597463
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    plugin_path = './'
    add_all_plugin_dirs(plugin_path)


# Generated at 2022-06-13 13:22:45.311542
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    paths = ('/foo', '/bar')
    which_loader = 'action'
    loader = getattr(sys.modules[__name__], '%s_loader' % which_loader)
    for path in paths:
        loader.add_directory(path, with_subdir=True)
    assert 'foo' in loader._module_paths
    assert 'bar' in loader._module_paths

add_dirs_to_loader('action', C.DEFAULT_ACTION_PLUGIN_PATH)
add_dirs_to_loader('connection', C.DEFAULT_CONNECTION_PLUGIN_PATH)
add_dirs_to_loader('lookup', C.DEFAULT_LOOKUP_PLUGIN_PATH)

# Generated at 2022-06-13 13:22:53.688554
# Unit test for function get_shell_plugin
def test_get_shell_plugin():

    # test for default shell_type = sh
    shell = get_shell_plugin()
    assert 'sh' == shell.SHELL_FAMILY

    # test for valid shell_type
    shell = get_shell_plugin(shell_type='csh')
    assert 'csh' == shell.SHELL_FAMILY

    # test for valid executable
    executable = '/bin/bash'
    shell = get_shell_plugin(executable=executable)
    assert '/bin/bash' == shell.executable
    assert 'sh' == shell.SHELL_FAMILY

    # test for invalid executable
    executable = '/bin/blah'
    shell = get_shell_plugin(executable=executable)
    assert '/bin/blah' == shell.executable
    assert 'sh' == shell.SHELL_FAMILY

# Generated at 2022-06-13 13:23:47.183199
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    '''
    Test PluginLoader.find_plugin
    :return:
    '''
    pass



# Generated at 2022-06-13 13:23:53.299861
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader = PluginLoader('/tmp/ansible_test_plugins/callback', 'CallbackModule')
    result = plugin_loader.get_with_context('success')
    assert isinstance(result, get_with_context_result)
    if result.resolved:
        assert result.object
        assert result.plugin_initializing_path
        assert result.plugin_matched_path
        assert result.plugin_resolved_name
        assert result.plugin_resolved_path
        assert result.plugin_filename



# Generated at 2022-06-13 13:24:00.430463
# Unit test for method get_with_context of class PluginLoader

# Generated at 2022-06-13 13:24:11.230212
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    sh = get_shell_plugin(shell_type='sh')
    assert sh.SHELL_FAMILY == 'sh'

    sh = get_shell_plugin(shell_type='sh', executable='/bin/sh')
    assert sh.SHELL_FAMILY == 'sh'

    sh = get_shell_plugin(executable='/bin/sh')
    assert sh.SHELL_FAMILY == 'sh'

    sh = get_shell_plugin(shell_type='csh', executable='/bin/csh')
    assert sh.SHELL_FAMILY == 'csh'

    sh = get_shell_plugin(shell_type='bash', executable='/bin/sh')
    assert sh.SHELL_FAMILY == 'sh'

    # The following isn't supported yet.  It results in a shell type of None

# Generated at 2022-06-13 13:24:24.041047
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    import tempfile
    from shutil import rmtree

    def create_test_dir(test_subdir):
        test_dir = tempfile.mkdtemp(prefix='ansible_test_%s_' % which_loader)
        test_subdir_path = os.path.join(test_dir, test_subdir)
        os.mkdir(test_subdir_path)
        return test_subdir_path


# Generated at 2022-06-13 13:24:35.123160
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # Test with both valid and invalid values
    valid_values = [(test_class, test_name) for test_name, test_class in _JINJA2_TESTS]
    for test_class, test_name in valid_values:
        test_obj = Jinja2Loader(test_class, 'test', '', 'ansible.plugins.test.test')
        test_obj.get(test_name)
    invalid_values = [(test_class, 'fake_plugin') for test_class, _ in _JINJA2_TESTS]
    for test_class, test_name in invalid_values:
        with pytest.raises(AnsibleError):
            test_obj = Jinja2Loader(test_class, 'test', '', 'ansible.plugins.test.test')
            test_obj.get

# Generated at 2022-06-13 13:24:41.956185
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    """ Unit test for method get of class Jinja2Loader """
    # pylint: disable=redefined-outer-name
    import ansible.plugins.action.builtin_task
    from ansible.plugins.action.builtin_task import ActionModule
    from ansible.plugins.loader import action_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.plugin_docs import get_docstring
    class TestFilterModule(ActionModule):
        """
        A test filter module
        """
        pass

    collection_loader = AnsibleCollectionLoader()

# Generated at 2022-06-13 13:24:44.219535
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    add_dirs_to_loader('action', [C.ACTION_PLUGIN_PATH])



# Generated at 2022-06-13 13:24:45.593741
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert callable(add_dirs_to_loader)



# Generated at 2022-06-13 13:24:49.234079
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    new_plugin_path_list = ['test_add_dirs_to_loader_path']
    add_dirs_to_loader('module', new_plugin_path_list)
    assert(new_plugin_path_list[0] in PATH_CACHE['module'])



# Generated at 2022-06-13 13:25:16.519158
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    loader = PluginLoader('callback_plugins', 'CallbackModule', 'callback', 'callback_')
    result = loader.get_with_context('ping')
    assert result.plugin_load_context.plugin_resolved_name == 'ping'
    # print("%s" % result.plugin_load_context.redirect_list)
    assert 'ansible.plugins.callback.ping' in result.plugin_load_context.redirect_list
    assert result.object.__class__.__name__ == 'CallbackModule'


# Generated at 2022-06-13 13:25:22.079458
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    orig_path = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    try:
        os.chdir(tmpdir)
        add_all_plugin_dirs(tmpdir)
    finally:
        os.chdir(orig_path)



# Generated at 2022-06-13 13:25:33.400311
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    # pylint: disable=protected-access
    # pylint: disable=no-member
    # pylint: disable=redefined-outer-name
    # pylint: disable=import-outside-toplevel
    from ansible import constants as C
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    import os
    import shutil
    import sys
    import tempfile
    import textwrap
    import yaml

    class_name = 'MyPlugin'
    base_class = 'BasePlugin'
    package_root = 'ansible_collections.my_namespace.my_collection.plugins'
    package_name = '%s.%s' % (package_root, class_name)
    module_name = 'my_plugin'
    module_content

# Generated at 2022-06-13 13:25:42.919046
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # load a plugin that is known to exist
    loader = PluginLoader(package='callback', searchpath=[DATA_PATH])
    obj = loader.find_plugin('minimal')
    assert obj.plugin_resolved_path == DATA_PATH + '/callback/minimal.py'

    # load a plugin that is known not to exist
    loader = PluginLoader(package='callback', searchpath=[DATA_PATH])
    obj = loader.find_plugin('no_such_plugin_should_ever_exist_so_this_test_should_always_fail')
    assert obj is None

    # load a plugin that exists in a collection, but only a namespace
    loader = PluginLoader(package='terminal', searchpath=[DATA_PATH])
    obj = loader.find_plugin('minimal', collection_list=[DATA_PATH + '/ns1_collection'])


# Generated at 2022-06-13 13:25:47.906933
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    cwd = os.getcwd()
    executable = os.path.join(cwd, "bin/sh")
    if not os.path.exists(executable):
        executable = "bin/sh"
    shell = get_shell_plugin(shell_type="sh", executable=executable)

    assert shell.SHELL_FAMILY == "sh"
    assert shell.executable == executable

