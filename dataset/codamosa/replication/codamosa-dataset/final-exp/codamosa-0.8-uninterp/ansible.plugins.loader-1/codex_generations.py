

# Generated at 2022-06-13 13:17:56.848067
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    """
    Test function to add all plugin directories to class object.
    """
    def test_loader(path, *args, **kwargs):
        """
        Test Class object
        """
        return

    test_loader.add_directory = lambda path: setattr(test_loader, 'path', path)
    test_loader.subdir = 'testpath'

    # Test for correct behavior if path is a directory
    path = '/usr/lib/ansible/plugins'
    globals()['test_loader'] = test_loader
    add_all_plugin_dirs(path)
    assert test_loader.path == '/usr/lib/ansible/plugins/testpath'
    del globals()['test_loader']

    # Test for warning behavior if path is not a directory

# Generated at 2022-06-13 13:18:06.788166
# Unit test for method format_paths of class PluginLoader
def test_PluginLoader_format_paths():
    import os
    import ansible.utils

    loader = PluginLoader(
        package='ansible.plugins.loader',
        subdir='test_plugins',
    )

    paths_list = ['/workspace/ansible/ansible/lib/ansible/plugins/test_plugins',
                  '/workspace/ansible/ansible/lib/ansible/plugins/test_plugins/bar',
                  '/workspace/ansible/ansible/lib/ansible/plugins/test_plugins',
                  '/workspace/ansible/ansible/lib/ansible/plugins/test_plugins/foo',
                  '/workspace/ansible/ansible/lib/ansible/plugins/test_plugins',
                  '/workspace/ansible/ansible/lib/ansible/plugins/test_plugins/tar']

    returned_paths = loader.format

# Generated at 2022-06-13 13:18:16.401270
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    def setup_mocks(mock_plugin_loader):
        # Setting up mock values
        mock_plugin_load_context = MagicMock()
        mock_plugin_load_context.plugin_resolved_name = 'ansible.plugins.test_plugin_loader.test_plugin_loader_test_case_2'
        mock_plugin_load_context.plugin_resolved_path = path
        mock_plugin_load_context.resolved = False
        mock_plugin_load_context.nope.return_value = mock_plugin_load_context

        mock_plugin_loader.get_plugin_with_context = MagicMock()
        mock_plugin_loader.get_plugin_with_context.return_value = mock_plugin_load_context

# Generated at 2022-06-13 13:18:20.746483
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    with patch('ansible.utils.plugin_docs.find_plugin') as find_plugin:
        find_plugin.return_value = None
        loader = Jinja2Loader()

        ret = loader.find_plugin('test')
        assert ret is None

        find_plugin.assert_called_once_with(loader, 'test')


# Generated at 2022-06-13 13:18:28.066161
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    PluginLoader.clear_cache()
    plugin_load_result = PluginLoader('shell_loader', 'ShellModule').get_with_context('shell')
    assert plugin_load_result.resolved
    assert hasattr(plugin_load_result.object, '_load_name')
    assert hasattr(plugin_load_result.object, '_original_path')
    assert hasattr(plugin_load_result.object, '_redirected_names')
    assert plugin_load_result.plugin_resolved_name == 'shell'


# Generated at 2022-06-13 13:18:37.037311
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    import tempfile
    import shutil
    from ansible.plugins.loader import module_loader, add_dirs_to_loader

    testname = 'test_add_dirs_to_loader'
    tmpdir = '%s/lib/ansible/test/test_plugins/' % tempfile.gettempdir()
    module_path = '%s/%s/%s' % (tmpdir, testname, 'module_utils')
    os.makedirs(module_path)
    example_path = '%s/%s' % (module_path, 'example.py')
    with open(example_path, 'w') as f:
        f.write("print '__example__'")

    # test module_loader
    add_dirs_to_loader('module_utils', [module_path])
   

# Generated at 2022-06-13 13:18:47.280794
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Testing that find_plugin returns a PluginLoadContext
    plugin_load_context = PluginLoader.find_plugin(name='ping')
    assert isinstance(plugin_load_context, PluginLoadContext)
    assert isinstance(plugin_load_context.plugin_resolved_name, str)
    assert isinstance(plugin_load_context.resolved, bool)
    assert isinstance(plugin_load_context.redirect_list, list)
    assert isinstance(plugin_load_context.plugin_resolved_path, str)
    assert isinstance(plugin_load_context.plugin_search_hints, list)
    assert isinstance(plugin_load_context.plugin_load_contexts_attempted, list)

    # Testing that a PluginLoadContext with the attribute 'resolved' set to False
    # indicates that the plugin could not

# Generated at 2022-06-13 13:18:52.741549
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # arrange
    import sys
    import unittest
    import tempfile
    import types
    import ansible.module_utils.six as six
    import ansible.errors
    import ansible.module_utils.ansible_release
    import ansible.constants as constants
    # import ansible.constants as C
    import ansible.config.manager as configmgr
    configmgr.set_defaults(constants.DEFAULTS)
    import ansible.plugins.loader as pl

    class Test_Jinja2Loader(unittest.TestCase):
        def setUp(self):
            self.settings = configmgr.ConfigData('plugin', 'plugin_dirs')
            # TODO: create a plugin dir and override this with a path in there vs hardcoding tmp
            # plugin_dir = os.path

# Generated at 2022-06-13 13:19:02.583351
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    try:
        get_shell_plugin()
    except AnsibleError as e:
        if "Either a shell type or a shell executable must be provided " in str(e):
            pass
        else:
            raise AssertionError("Error didn't contain correct message (%s)" % str(e))
    else:
        raise AssertionError("Expected AnsibleError to occur")

    try:
        get_shell_plugin("zsh")
    except AnsibleError as e:
        if "Could not find the shell plugin required (zsh)." in str(e):
            pass
        else:
            raise AssertionError("Error didn't contain correct message (%s)" % str(e))
    else:
        raise AssertionError("Expected AnsibleError to occur")

# *****************************************************



# Generated at 2022-06-13 13:19:13.980532
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    def get_jinja2_loader_instance(config):
        paths = [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures/loader/jinja2')]
        return Jinja2Loader(config, paths)

    jinja2_plugin_loader = get_jinja2_loader_instance(None)
    path = jinja2_plugin_loader.get('my_plugin.py')
    module_cache = jinja2_plugin_loader._module_cache
    class_name = jinja2_plugin_loader.class_name
    base_class = jinja2_plugin_loader.base_class
    plugin_class = getattr(module_cache[path], class_name)

# Generated at 2022-06-13 13:20:25.066044
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    """ Add a directory to a plugin loader and search for a specific plugin
    """
    import os
    import shutil
    import tempfile
    import ansible
    import ansible.plugins

    directory = ''
    init_file, load_file = None, None


# Generated at 2022-06-13 13:20:34.178832
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # Setup test
    test_loader = PluginLoader(
        'collection_name',
        'package_name',
        'base_class_name',
        'class_name',
        'subdir'
    )
    # Test the method
    test_loader.all(
        path_only='path_only',
        class_only='class_only',
        _dedupe='_dedupe'
    )
    # Verify the results


# Generated at 2022-06-13 13:20:37.669997
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert add_dirs_to_loader(which_loader='connection', paths=['/var/cache/ansible/plugin_loader/connection']) == None


# Generated at 2022-06-13 13:20:43.214585
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    loader = PluginLoader('ansible.plugins.test')
    plugins = list(loader.all())
    assert len(plugins) == 1, plugins
    plugin = plugins[0]
    assert isinstance(plugin, TestPlugins)
    assert plugin.__file__.rstrip('c') == os.path.join(os.path.dirname(__file__), 'plugins', 'test', 'test.py')



# Generated at 2022-06-13 13:20:58.468442
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    o = PluginLoader('module_utils', '_AnsibullbotPlugin')
    expected = 'Invalid collection name {0}: {1}'
    actual = None
    try:
        actual = o.get_with_context('fqcn_without_colon')
    except AnsibleError as e:
        actual = str(e)
    assert actual == expected

    expected = 'Invalid collection name {0}: {1}'
    actual = None
    try:
        actual = o.get_with_context('colon_without_fqcn')
    except AnsibleError as e:
        actual = str(e)
    assert actual == expected

    expected = 'Invalid collection name collection.found_ansible: {0}'
    actual = None

# Generated at 2022-06-13 13:21:08.176776
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    import json
    import sys
    import imp
    import os
    import pytest
    import pkgutil
    import yaml

    def get_imp_orig(name):
        if imp is not None:
            return imp.find_module(name)
        loader = importlib.util.find_spec(name)
        file_handle = loader.loader.get_filename(name)
        return loader.loader, file_handle, None

    # Simply returns the first component of the second argument
    def get_imp_patch(name):
        return ('patch',)

    def get_sys_modules_patch():
        return {'ansible_unit_test_collection_name': 'ansible.test_collection'}

    def get_AnsibleCollectionConfig_orig():
        config = AnsibleCollectionConfig()

# Generated at 2022-06-13 13:21:13.637597
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    from ansible.compat import HASH_MODULE
    from ansible.utils.hashsums import sha256, sha256_t_digest
    checksum = os.path.join('/path/to/directory', 'CHKSUMS')

    def mock_is_file(path):
        if path == checksum:
            return True
        raise OSError()

    def mock_is_dir(path):
        if path == '/path/to/directory/module_utils':
            return True
        raise OSError()

    def mock_exists(path):
        if path == '/path/to/directory':
            return True
        raise OSError()

    def mock_open(path, mode):
        if path == checksum:
            fh = mock.MagicMock()
            fh

# Generated at 2022-06-13 13:21:14.654451
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    pass


# Generated at 2022-06-13 13:21:16.656474
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    _ = None  # Cause pyflakes to ignore this line
    # No tests for method get_with_context for class PluginLoader
    pass



# Generated at 2022-06-13 13:21:21.614473
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.dataloader import DataLoader
    class Connection: pass
    class PlayContext:
        def get_connection(self, _):
            connection = Connection()
            connection.env = dict()
            return connection
    class Play:
        class PlayContext: pass
    class Options:
        class _Plugins(Mapping):
            def __init__(self, _): pass
            def __iter__(self):
                items = []
                for i in range(0, 1):
                    items.append(i)
                return iter(items)
            def __getitem__(self, key):
                return key

# Generated at 2022-06-13 13:21:42.175768
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    loader = PluginLoader('foo', 'bar', C.DEFAULT_MODULE_PATH, 'foo.bar', 'bar',  required_base_class='bar')
    assert loader.has_plugin('baz') is True

# Generated at 2022-06-13 13:21:52.003329
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    self_ = PluginLoader()
    self_.subdir = None
    self_.base_class = None
    self_.class_name = None
    self_.package = None
    self_._searched_paths = []
    self_._module_cache = {}
    args = []
    kwargs = {'_dedupe': True, 'path_only': False, 'class_only': False}
    source = '''
    all_matches = []
    for i in self._get_paths():
        all_matches.extend(glob.glob(to_native(os.path.join(i, "*.py"))))
    '''
    exec(source)
    loaded_modules = set()
    path = None

# Generated at 2022-06-13 13:21:58.475993
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Test against non directory path
    class TestClass(PluginLoader):
        pass
    TestClass.subdir = 'test_sub_dir'
    TestClass.add_directory = get_add_directory_function(TestClass)
    path = 'non_directory_string'
    assert not os.path.isdir(path)
    add_all_plugin_dirs(path)
    # Check if warning is shown
    assert len(display.warnings) == 1
    assert display.warnings[0] == ("Ignoring invalid path provided to plugin path: 'non_directory_string' is not a directory")
    # Test against directory path
    path = 'test_fixtures/test_plugin_loader_add_all_plugin_dirs'
    dir_path = os.path.join(path, 'test_sub_dir')
   

# Generated at 2022-06-13 13:22:05.770344
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    plugin_loader = get_all_plugin_loaders()[0][1]
    plugin_loader.directories = []

    # test path does not exist
    assert len(plugin_loader.directories) == 0
    add_all_plugin_dirs("/does/not/exist")
    assert len(plugin_loader.directories) == 0

    # test path is not a directory
    assert len(plugin_loader.directories) == 0
    add_all_plugin_dirs("/dev/null")
    assert len(plugin_loader.directories) == 0

    # test path is a directory and subdir does not exist
    assert len(plugin_loader.directories) == 0
    add_all_plugin_dirs("/etc")
    assert len(plugin_loader.directories) == 0

    # test path is a

# Generated at 2022-06-13 13:22:11.256766
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    # test when shell_type is passed as a parameter
    shell = get_shell_plugin('sh')
    assert shell is not None, 'Failed when shell type is passed as a parameter'

    # test when executable is passed as a parameter
    shell = get_shell_plugin(executable='sh')
    assert shell is not None, 'Failed when executable is passed as a parameter'

    # test when both are passed as parameters (shell_type will be used)
    shell = get_shell_plugin('sh', executable='sh')
    assert shell is not None, 'Failed when both parameters are passed (shell_type will be used)'

    # test when no parameter is passed (AnsibleError will be raised)

# Generated at 2022-06-13 13:22:17.786852
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    """ Unit test for method get_with_context of class PluginLoader """
    # data for test cases

# Generated at 2022-06-13 13:22:19.673711
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    """Test find_plugin_with_context of PluginLoader."""
    raise NotImplementedError


# Generated at 2022-06-13 13:22:28.560392
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.plugins.shell.sh import ShellModule as ShellSh
    from ansible.plugins.shell.powershell import ShellModule as ShellPowerShell

    shell = get_shell_plugin(shell_type='sh')
    assert isinstance(shell, ShellSh)
    assert shell.executable is None

    shell = get_shell_plugin(shell_type='powershell', executable='powershell.exe')
    assert isinstance(shell, ShellPowerShell)
    assert shell.executable == 'powershell.exe'



# Generated at 2022-06-13 13:22:38.731251
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    test_shell_types = ['sh', 'csh', 'powershell', 'fish', 'bash']
    valid_shells = ['ash', 'dash', 'bash']

    for shell in test_shell_types:
        shell_plugin = get_shell_plugin(shell_type=shell)
        assert shell_plugin.SHELL_FAMILY == shell

    shell_to_test = get_shell_plugin(shell_type='test')
    assert shell_to_test is None

    for shell in valid_shells:
        shell_plugin_exe = get_shell_plugin(executable=shell)
        assert shell_plugin_exe.SHELL_FAMILY == 'sh'

    invalid_shell_plugin = get_shell_plugin(executable='invalid')
    assert invalid_shell_plugin is None



# Generated at 2022-06-13 13:22:44.538767
# Unit test for function get_shell_plugin
def test_get_shell_plugin():

    # test by shell_type
    shell_sh = get_shell_plugin(shell_type='sh')
    assert isinstance(shell_sh, ShellModule) == True
    assert shell_sh.SHELL_FAMILY == 'sh'
    # test by executable
    shell_bash = get_shell_plugin(executable='/bin/bash')
    assert shell_bash.SHELL_FAMILY == 'sh'



# Generated at 2022-06-13 13:23:48.075967
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # NOTE: currently this is not supported, so we just include a simple test to ensure
    #       it exists and is tested in case this changes
    try:
        plugin_loader = Jinja2Loader('ansible.plugins.lookup.tests','ansible.plugins.filter_loader', config=None)
        returned_value = plugin_loader.get('test_plugin')
        assert returned_value.__class__.__name__ == 'LookupModule'
        assert returned_value._load_name == 'test_plugin'
    except ImportError:
        # don't fail if the test lookup plugin is not installed
        pass


# Generated at 2022-06-13 13:23:57.239777
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    l = PluginLoader('')
    assert 'f' in l
    assert 'fo' in l
    assert 'foo' in l
    assert 'bar' in l
    assert 'foobar' in l
    assert 'fobar' in l
    assert 'fbar' in l
    assert not 'F' in l
    assert not 'fo' in l
    assert not 'foo' in l
    assert not 'bar' in l
    assert not 'foobar' in l
    assert not 'fobar' in l
    assert not 'fbar' in l

# Testcases for class PluginLoader

# Generated at 2022-06-13 13:24:04.653114
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    loader = PluginLoader(
        'ActionModule',
        'ansible.plugins.action',
        C.config.get_config_value('action_plugins'),
        'action_plugins',
        required_base_class='ActionBase'
    )
    context = loader.get_with_context('copy')
    assert context is not None
    assert context.object is not None
    assert context.resolved is True
    assert context.plugin_resolved_name == 'copy'
    assert context.plugin_resolved_path.endswith(os.path.join('action_plugins', 'copy.py'))
    # NOTE: invalid plugin name; this should not throw
    assert loader.get_with_context('invalid_action_plugin_name') is None


# Generated at 2022-06-13 13:24:15.747194
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    call_args = {}
    call_args['name'] = None
    call_args['ignore_deprecated'] = False
    call_args['collection_list'] = None
    call_args['suffix'] = None

    # Setup mocks
    config = MagicMock(spec_set=Configuration)
    config.get_plugin_load_priority = MagicMock(return_value=None)
    config.get_plugin_load_with_priority_path = MagicMock(return_value=None)
    config.get_plugin_paths = MagicMock(return_value=['/path/to/plugins'])
    plugin_loader = PluginLoader(config, collection_list=None)

    # Run method

# Generated at 2022-06-13 13:24:24.600623
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    plc = PluginLoadContext()
    assert plc.record_deprecation(name='test.test_collection.test_action', deprecation=None, collection_name='test_collection').deprecated is False
    assert plc.record_deprecation(name='test.test_collection.test_action', deprecation={'warning_text': 'Test warning'}, collection_name='test_collection').deprecated is True



# Generated at 2022-06-13 13:24:31.383579
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    temp_dir = tempfile.mkdtemp()
    pl = PluginLoader(
        'action_plugin',
        'ansible.plugins.action',
        C.DEFAULT_ACTION_PLUGIN_PATH,
        'action_plugins',
        required_base_class='ActionBase'
    )
    pl.add_directory(temp_dir)
    assert os.path.abspath(temp_dir) in pl._get_paths()

# Generated at 2022-06-13 13:24:36.321759
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''Plugin Loader tests'''
    test_path = 'test_path'
    mock_obj = MockPluginLoader()
    globals()['MockPluginLoader'] = mock_obj
    add_all_plugin_dirs(test_path)
    assert mock_obj.add_directory_calls[0] == test_path
    del globals()['MockPluginLoader']



# Generated at 2022-06-13 13:24:44.168896
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    """
    Test function `find_plugin` of class `PluginLoader`.

    :returns: If the test case passes, will return True.
    :rtype: bool
    """
    try:
        # GIVEN: instantiate object `PluginLoader`
        plugin_loader = PluginLoader()
        result = plugin_loader.find_plugin('copy')
        assert 'ansible/plugins/action/' in result
    except Exception:
        # WHEN exception occurs, return False
        return False
    # WHEN no exception occurs, return True
    return True


# Generated at 2022-06-13 13:24:45.343133
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    assert False, "No test available"

# Generated at 2022-06-13 13:24:52.249615
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.plugins import module_loader
    from ansible.plugins import lookup_loader

    path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'fixtures', 'test_plugins')
    add_all_plugin_dirs(path)

    play = PlaybookCLI()
    module_loader_obj = module_loader.find_plugin('test_module')
    assert module_loader_obj is not None

    lookup_plugin_obj = lookup_loader.find_plugin('test_lookup')
    assert lookup_plugin_obj is not None


# Generated at 2022-06-13 13:25:26.926548
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Check C._ANSIBLE_LOOKUP_PLUGINS is set by adding plugin path
    for name, obj in get_all_plugin_loaders():
        obj._directories = set()
    current_plugins = C._ANSIBLE_LOOKUP_PLUGINS
    C._ANSIBLE_LOOKUP_PLUGINS = set()
    assert len(C._ANSIBLE_LOOKUP_PLUGINS) == 0
    add_all_plugin_dirs("test_plugins")
    assert len(C._ANSIBLE_LOOKUP_PLUGINS) == 0
    add_all_plugin_dirs("test/test_plugins")
    assert len(C._ANSIBLE_LOOKUP_PLUGINS) > 0
    C._ANSIBLE_LOOKUP_PLUGINS = current_plugins

    # Check invalid path provided and

# Generated at 2022-06-13 13:25:33.520262
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    print('Testing: class PluginLoader (method: all)')
    loader = PluginLoader(package='ansible.utils.plugin_docs', class_name='FilterModule')
    lst = []
    for plugin in loader.all():
        plugin_doc = getattr(plugin, 'DOCUMENTATION')
        if plugin_doc:
            lst.append(plugin_doc)
    print('Count of plugins:', len(lst))
    assert len(lst) >= 3
    print('Test passed')



# Generated at 2022-06-13 13:25:42.965271
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # A plugin path which doesn't exist
    add_all_plugin_dirs(os.path.join(C.DEFAULT_LOCAL_TMP, 'non-existent'))
    # A directory which exists but has no plugins subdirs
    add_all_plugin_dirs(C.DEFAULT_LOCAL_TMP)
    # A directory with one plugin subdir
    os.makedirs(os.path.join(C.DEFAULT_LOCAL_TMP, 'test-plugin-dir', 'module_utils'))
    os.makedirs(os.path.join(C.DEFAULT_LOCAL_TMP, 'test-plugin-dir', 'modules'))
    add_all_plugin_dirs(os.path.join(C.DEFAULT_LOCAL_TMP, 'test-plugin-dir'))

# Generated at 2022-06-13 13:25:51.280284
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    class_name, name, package, subdir, base_class = ("ModuleExecutor","shell","ansible.plugins.action","action",None)
    #Case 1: The implementation of success case
    #Possible implementation:
    #  - The plugin, in this case shell, is not in the collection, but it is in the Ansible core
    #  - Look for the plugin in the cache, it will be succes, because the cache will be empty (the plugin has not been loaded)
    #  - Look for the plugin in Ansible core, it will be succes, because the shell plugin is in Ansible core
    #  - Look for the plugin in the collection, it will be fails, because the plugin is not in the collection
    #  - Look for the plugin in the "ansible.builtin" directory, it will be fails, because the plugin is not there



# Generated at 2022-06-13 13:25:57.259783
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' Test add_all_plugin_dirs function. '''

    # Test invalid path
    invalid_path = "/invalid/path"
    add_all_plugin_dirs(invalid_path)
    assert not os.path.isdir(invalid_path)

    # Test valid path
    valid_path = "."
    add_all_plugin_dirs(valid_path)
    assert os.path.isdir(valid_path)

