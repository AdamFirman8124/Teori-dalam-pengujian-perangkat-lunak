

# Generated at 2022-06-13 13:17:43.013924
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Create a mock collection 'my.collection' with plugins, including a test plugin 'my.collection.tests_plugins.test'
    my_col_dir = tempfile.mkdtemp()
    my_col_path = os.path.join(my_col_dir, 'my', 'collection', 'plugins', 'action')
    os.makedirs(my_col_path)
    with open(os.path.join(my_col_path, 'my_collection_action.py'), 'w') as f:
        f.write('from ansible.plugins.action import ActionBase'
                '\nclass ActionModule(ActionBase):'
                '\n    pass\n')
    my_col_path = os.path.join(my_col_dir, 'my', 'collection', 'plugins', 'filter')
    os.m

# Generated at 2022-06-13 13:17:52.138339
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader(
        'action',
        'ansible.plugins.action',
        'ActionModule',
        C.DEFAULT_ACTION_PLUGIN_PATH,
        'action_plugins',
    )
    assert loader.find_plugin('module_utils.module_common') is not None

    loader = PluginLoader(
        'cache',
        'ansible.plugins.cache',
        'CacheModule',
        C.DEFAULT_CACHE_PLUGIN_PATH,
        'cache_plugins',
    )
    assert loader.find_plugin('base') is None
    assert loader.find_plugin('yaml') is not None

# Generated at 2022-06-13 13:18:01.908599
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    # Unit test for method find_plugin of class Jinja2Loader
    import ansible.errors as errors
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.plugins.loader import Jinja2Loader

    def add_directory_to_class_loader(directory, loader):
        loader.add_directory(directory)

    def add_directory_to_legacy_loader(directory, loader):
        loader.add_directory(directory)

    def test_plugin_loader_Jinja2Loader_find_plugin(collection_name, class_loader, legacy_loader, plugin_name):
        try:
            class_loader.find_plugin(plugin_name, collection_list=[collection_name])
        except errors.AnsibleError:
            legacy_loader.find_plugin(plugin_name)

    # Test 1

# Generated at 2022-06-13 13:18:10.277351
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader(
        class_name='Connection',
        package='ansible.plugins.connection',
        config=dict(),
        subdir='connection_plugins',
        aliases={},
        required_base_class='ConnectionBase')
    name = 'local'
    def test_function(expected_results):
        plugin_load_context = plugin_loader.find_plugin_with_context(name)
        assert plugin_load_context.resolved == expected_results, "Expected '%s' but got '%s'" % (
            expected_results, plugin_load_context.resolved)

    test_function(True)



# Generated at 2022-06-13 13:18:15.188786
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():

    class MockModule(object):
        pass

    class PluginLoader_mock(PluginLoader):
        def __init__(self, package, subdir, base_class):
            pass

        def find_plugin(self, plugin_name, collection_list=None):
            return MockModule()

    loader = PluginLoader_mock('package', 'subdir', 'base_class')
    assert 'plugin_name' in loader



# Generated at 2022-06-13 13:18:25.216259
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.plugins.shell import ShellBase
    from ansible.plugins.shell import C
    from ansible.plugins.shell import ShellModule
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import add_fragments, BUILTIN_DOCSTRING_FIELDS
    import os
    import os.path

    class MyShell(ShellBase):
        ''' This is a test shell plugin '''
        SHELL_FAMILY = 'mytest'
        COMPATIBLE_SHELLS = ('mytest',)

    class DefShellModule(ShellModule):
        _init_failed = False

    class FailingShellModule(ShellModule):
        _init_failed = True

# Generated at 2022-06-13 13:18:34.866554
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    candidates=[]
    for name in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'plugins/'))):
        candidates.append(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'plugins/'+name))))
    add_all_plugin_dirs(candidates[0])
    plugin_loader = get_plugin_loader(os.path.join(candidates[0], 'action_plugins'))
    assert len(plugin_loader.package_paths) == 1
    assert len(plugin_loader.class_paths) == 1

# Generated at 2022-06-13 13:18:46.037315
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    args = dict(
        name='test_plugin',
        collection_list=None,
        class_only=False,
        suffix=None,
        subdir='module_utils',
        package='ansible.module_utils',
        directories=[],
        class_name='TestPlugin'
    )
    pl = PluginLoader(*(), **args)
    pl.add_directory(test_data_path.strpath)
    obj = pl.find_plugin('test_plugin')
    assert obj is not None
    assert obj.__name__ == 'test_plugin'
    assert obj._original_path == '/a/test_plugin.py'

    obj2 = pl.find_plugin('test_plugin2.abs')
    assert obj2 is not None
    assert obj2.__name__ == 'test_plugin2'
    assert obj

# Generated at 2022-06-13 13:18:53.858252
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    def mockfind_plugin(self, name, extension='', class_only=''):
        return {'test': 'test'}
    class mockAnsiblePlugin(object):
        def __init__(self, *args):
            self.args = args
    def mock_get_config(self, user_name):
        return {}
    old_find_plugin = PluginLoader.find_plugin
    PluginLoader.find_plugin = mockfind_plugin
    # Test with dedupe = True
    plugin_loader = PluginLoader('ansible', 'AnsiblePlugin')
    plugin_loader.all()
    plugin_loader.find_plugin = old_find_plugin

# Generated at 2022-06-13 13:18:55.601074
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    plugin_loader = PluginLoader('C', 'B', 'A')
    assert plugin_loader != None


# Generated at 2022-06-13 13:19:57.070642
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # Instantiate the class
    plugin_loader = Jinja2Loader('ansible.plugins.loader.test.data.my_fancy_plugins', 'MyPluginClass')

    # Call the method we are testing
    result = plugin_loader.get('afile.py')

    # Check the result
    assert result == "my_fancy_plugins.my_fancy_plugin.PluginClass"


# Generated at 2022-06-13 13:20:05.916318
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():

    ansible_unit_test.register_plugin_loader_class('foo', PluginLoader)
    plugin_loader = AnsiblePluginLoader(package='test_test_test', subdir='foo_plugins', base_class='FooPlug')
    assert len(list(plugin_loader.all())) == 0

    AnsiblePluginLoader._PLUGIN_PATH_CACHE = {}
    plugin_loader = AnsiblePluginLoader(package='test_test_test', subdir='foo_plugins', base_class='FooPlug')

    base_plugins = (
        'D1.py',
        'D2.py',
        '__init__.py',
        'base.py',
        'D2_2.py',
        'C1.py',
        'C2.py',
    )

# Generated at 2022-06-13 13:20:10.421604
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    plugin_loader = PluginLoader(package='ansible.plugins.inventory', base_class='BaseInventoryPlugin')
    plugin_loader.add_directory('/home/we/my_new_path')
    assert '/home/we/my_new_path' in plugin_loader._paths


# Generated at 2022-06-13 13:20:21.037224
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    test_path = '~/ansible_test_path'

# Generated at 2022-06-13 13:20:28.003319
# Unit test for method find_plugin_with_context of class PluginLoader

# Generated at 2022-06-13 13:20:34.435550
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    assert find_plugin_with_context(plugin_name="absent") == None, "find_plugin_with_context() returned incorrect value."

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 13:20:43.571717
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import ansible.plugins.module_utils
    from collections import namedtuple
    Test = namedtuple('Test', ['base_dir', 'plugin_dir', 'searched_paths', 'expected_paths'])

    # FIXME: Testing for modules directories that are not in the module_utils
    #  directory is out of scope for this unit test.
    #  The PluginLoader should be extended to work with other objects types
    #  in the future.

# Generated at 2022-06-13 13:20:49.262635
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    path = '../ansible/plugins'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    assert (os.path.isdir(b_path))


# Generated at 2022-06-13 13:20:50.129397
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    pass

# Generated at 2022-06-13 13:20:56.434624
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader = PluginLoader('ansible.plugins.action', 'ActionModule', C.DEFAULT_INTERNAL_PLUGINS_PATH, 'action_plugins', required_base_class='ActionBase')
    assert plugin_loader.get_with_context('copy')  # TODO what is this test meant to test?


# Generated at 2022-06-13 13:21:29.119494
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # If all is present in the dict, then it is okay.
    assert 'all' in PluginLoader.__dict__.keys()


# Generated at 2022-06-13 13:21:36.943385
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Create a list of plugin loaders
    assert len(get_all_plugin_loaders()) > 0
    # Make a dir to hold it all
    tmp_dir = tempfile.mkdtemp()
    # Create a dir for each plugin subdir to test for
    for n, o in get_all_plugin_loaders():
        tmp_dir_o = os.path.join(tmp_dir, n)
        os.mkdir(tmp_dir_o)
    # Add it to the path
    add_all_plugin_dirs(tmp_dir)
    # Ensure it worked
    for n, o in get_all_plugin_loaders():
        assert o.plugin_dirs()[0] == os.path.join(tmp_dir, n)
    # Cleanup

# Generated at 2022-06-13 13:21:47.906310
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    import sys
    import pkgutil
    import pytest

    from io import BytesIO, StringIO
    from ansible.plugins import lookup_loader, callback_loader, module_loader, action_loader, connection_loader

    stdout_save = sys.stdout
    stderr_save = sys.stderr

    # stdout capture
    sys.stdout = mystdout = StringIO()
    sys.stderr = mystderr = StringIO()

    context = PluginLoadContext()

    # No deprecation, nothing should change
    deprecation_no_deprecation = {'warning_text': None, 'removal_version': None, 'removal_date': None}
    context.record_deprecation('test', deprecation_no_deprecation, 'ansible.netcommon')
    assert context

# Generated at 2022-06-13 13:21:52.751998
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    p = PluginLoader('test', 'test', C.config.get_config_value('DEFAULT_CACHE_PLUGIN_TIMEOUT') or 240)
    res = p.add_directory('test2')
    assert res is False
    res = p.add_directory('/test3')
    assert res
    res = p.add_directory('/test3')
    assert res is False



# Generated at 2022-06-13 13:21:59.000293
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
    assert add_dirs_to_loader('module', ["fake_path"]) is None
   

# Generated at 2022-06-13 13:22:01.929858
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
  l = PluginLoader( 'action_plugin', 'action_plugins', C.DEFAULT_ACTION_PLUGIN_PATH )
  assert not ( 'notthere' in l )
  assert 'copy' in l

# Generated at 2022-06-13 13:22:07.487098
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method __contains__ of class PluginLoader
    '''
    loader = PluginLoader(package='test_package', class_name='TestClass')
    assert False == loader.has_plugin("foo")
    loader._searched_paths = ['/foo', '/bar']
    assert False == loader.has_plugin("foo")



# Generated at 2022-06-13 13:22:08.001669
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pass



# Generated at 2022-06-13 13:22:13.491399
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    p_path = os.path.join(os.path.dirname(__file__), 'plugins', '*')
    add_dirs_to_loader('action', [p_path])
    assert action_loader.get('copy')
    action_loader.clear()

    add_dirs_to_loader('action', [p_path])
    assert action_loader.get('copy')
    action_loader.clear()

    add_dirs_to_loader('action', [p_path])
    assert action_loader.get('copy')
    action_loader.clear()



# Generated at 2022-06-13 13:22:21.989203
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import ansible.plugins.action
    from ansible.errors import AnsibleError

    plugin_loader = PluginLoader(
        package='ansible.plugins.action',
        class_name='ActionBase',
        base_class='ActionBase',
        config_base_class='ActionModule',
        config_section_name='action',
        create_on_missing=True,
        is_subclass_of=None
    )
    # These tests are to check that the search for plugins works as expected
    # The path of one plugin is manually set in the PluginLoadContext to test the different search paths
    # The tests with three underscores are for plugins that are part of a collection (e.g., community.general.my_plugin)
    assert plugin_loader.find_plugin('ping') == plugin_loader.find_plugin('ansible.builtin.ping')

# Generated at 2022-06-13 13:22:53.375604
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # each test here is a method that decorates a test method

    @pytest.fixture
    def loader_state(self):
        # establish a clean state which will be reset after each test

        self._module_cache = PluginLoader._module_cache
        self._tmp_paths = PluginLoader._tmp_paths
        self._tmp_collection_paths = PluginLoader._collection_paths
        self._searched_paths = PluginLoader._searched_paths
        PluginLoader._module_cache = {}
        PluginLoader._tmp_paths = []
        PluginLoader._collection_paths = {}
        PluginLoader._searched_paths = {}

    @pytest.fixture
    def loader_state_teardown(self):
        # reset the state so that it is clean for the next test

        PluginLoader._

# Generated at 2022-06-13 13:22:57.630110
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method __contains__ of class PluginLoader
    '''
    from ansible.plugins import AnsiblePluginConfig
    default_args = {'class_name': 'Config', 'package': 'ansible.plugins.config', 'config': AnsiblePluginConfig}
    _plugin_loader = PluginLoader(**default_args)

    result = _plugin_loader.has_plugin('invalid_config')
    assert result == False, "The method has_plugin has error"


# Generated at 2022-06-13 13:23:05.202670
# Unit test for function get_shell_plugin
def test_get_shell_plugin():

    test_shell_type = 'sh'
    test_executable = 'bin/sh'
    assert get_shell_plugin(test_shell_type, test_executable).SHELL_NAME == test_shell_type
    assert get_shell_plugin(test_shell_type, test_executable).executable == test_executable

    test_shell_type = None
    test_executable = 'bin/sh'
    assert get_shell_plugin(test_shell_type, test_executable).SHELL_NAME == 'sh'
    assert get_shell_plugin(test_shell_type, test_executable).executable == test_executable

    test_shell_type = 'csh'
    test_executable = 'bin/tcsh'

# Generated at 2022-06-13 13:23:13.678391
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # NOTE: get_with_context is a class method of PluginLoader
    # Create a dummy plugin loader with the class name set to 'DummyPlugin'
    plugin_loader = PluginLoader(package='test.test_utils', class_name='DummyPlugin')
    # Create a dummy plugin that will always return True from has_plugin
    # (so that it will be found by the loader)
    class DummyPlugin(object):
        def __init__(self, plugin_load_context):
            self.plugin_load_context = plugin_load_context
        def has_plugin(self, name, collection_list=None):
            return True
    # Add the dummy plugin to the plugin loader.
    # It will be returned from the loader if the plugin name starts with 'dummy_'

# Generated at 2022-06-13 13:23:26.486208
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    p = PluginLoader('', '', '', '', '')
    # The first two tests are magic-mock'd to avoid having to load plugins.
    # Test 1: Return the first plugin that matches with no aliasing.
    # Unlike the code, this test will show what plugin was matched.
    with patch.object(p, '_get_plugin_paths', return_value=[
            '/foo/bar/plugins/callback/first.py',
            '/foo/bar/plugins/callback/second.py']):
        assert 'plugins/callback/first.py' == p.find_plugin('first')

    # Test 2: If no plugin matches, return None

# Generated at 2022-06-13 13:23:40.641587
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    playbook_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

    assert len(get_unset_plugin_loaders()) == 0

    for plugin_loader in get_all_plugin_loaders():

        plugin_loader_obj = plugin_loader[1]
        plugin_loader_obj.directories = []

    add_all_plugin_dirs(playbook_root)

    assert len(get_set_plugin_loaders()) == len(get_all_plugin_loaders())

    for plugin_loader in get_all_plugin_loaders():

        plugin_loader_obj = plugin_loader[1]

        plugin_loader_name = plugin_loader_obj.name


# Generated at 2022-06-13 13:23:44.232813
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.plugins.shell import ShellBase
    assert issubclass(get_shell_plugin(shell_type = 'sh'), ShellBase)
    assert issubclass(get_shell_plugin(executable = '/bin/sh'), ShellBase)
    assert issubclass(get_shell_plugin(shell_type = 'unknown'), ShellBase)



# Generated at 2022-06-13 13:23:49.456504
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    shell = get_shell_plugin('sh')
    assert shell._load_name == 'sh'
    assert shell.executable == '/bin/sh'
    shell = get_shell_plugin('sh', '/usr/bin/fish')
    assert shell._load_name == 'sh'
    assert shell.executable == '/usr/bin/fish'



# Generated at 2022-06-13 13:23:51.378019
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    assert False, "No test for method record_deprecation"

# Generated at 2022-06-13 13:24:01.586386
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    '''
    Unit tests for the PluginLoader class
    '''
    from ansible.utils.display import Display
    display = Display()

    from ansible.plugins.loader import action_loader, connection_loader, cache_loader, callback_loader, shell_loader
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable, AnsibleFileNotFound, AnsibleParserError

    # Test to check if find_plugin is able to locate the plugin correctly
    action_plugins = action_loader.all()
    assert 'shell' in action_plugins
    # Test to check if find_plugin fails to locate the plugin correctly
    assert 'seashell' not in action_plugins

    # test fallback search for FQCN

# Generated at 2022-06-13 13:25:17.910236
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' test that all PluginLoader's are added to the PATH_CACHE '''
    path = '/path/to/ansible/plugins'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    m = mock.mock_open()
    with mock.patch('ansible.parsing.dataloader.DataLoader.is_directory', return_value=True):
        with mock.patch('os.path.isdir', return_value=True):
            with mock.patch('os.path.join', side_effect=lambda *parts: b"/".join(parts)):
                with mock.patch('__builtin__.open', m, create=True):
                    add_all_plugin_dirs(path)

# Generated at 2022-06-13 13:25:24.659491
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():

    pl = PluginLoader('__test_add_directory__')
    pl.add_directory(os.path.join(os.path.dirname(__file__), 'modules'))
    assert os.path.join(os.path.dirname(__file__), 'modules') in pl._get_paths()
    # cleanup
    pl._searched_paths.remove(os.path.join(os.path.dirname(__file__), 'modules'))


# Generated at 2022-06-13 13:25:31.839330
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():

    #TODO: use tempdirs instead of ./t
    tmpdir = './t/tmp/j2loader_get'
    srcdir = './t/tmp/j2loader_get/src'
    collection_dir = './t/tmp/j2loader_get/collection'
    collection_path = 'ansible_collections.collection_name.collection_namespace'
    collection_plugins = 'ansible_collections.collection_name.collection_namespace.plugins.test'

    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    if not os.path.exists(srcdir):
        os.makedirs(srcdir)
    if not os.path.exists(collection_dir):
        os.makedirs(collection_dir)

    # set

# Generated at 2022-06-13 13:25:41.347097
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' add_all_plugin_dirs unit test'''
    # Module
    assert add_all_plugin_dirs('test_add_all_plugin_dirs') is None
    # Empty
    assert add_all_plugin_dirs('') is None
    # Directory
    os.mkdir('path')
    os.mkdir('path/module_utils')
    os.mkdir('path/lookup_plugins')
    os.mkdir('path/callback_plugins')
    # Call function
    module_loader = get_plugin_loader('module_utils')
    module_loader.add_directory('path/module_utils')
    module_loader.add_directory('path/module_utils')
    module_loader._get_all()
    lookup_loader = get_plugin_loader('lookup')
    lookup_

# Generated at 2022-06-13 13:25:42.317645
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    assert 0


# Generated at 2022-06-13 13:25:43.571346
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    pass


# Generated at 2022-06-13 13:25:46.166333
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # plugin_loader = PluginLoader(...).all(path_only=False|True, class_only=False|True)
    pass

# vim: set ts=4 sw=4 et:

# Generated at 2022-06-13 13:25:50.998672
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.module_utils._text import to_bytes

    obj = Jinja2Loader('ansible.plugins.filter', 'FilterModule', 'filter_plugins')
    obj._get_paths = lambda: ['plugins/filter']

    def _load_module_source(fullname, path):
        from ansible.module_utils._text import to_bytes

        module = imp.new_module(fullname)
        module.MY_VAR = 2