

# Generated at 2022-06-13 13:17:55.922426
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    import ansible.plugins.loader
    plugin_loader = ansible.plugins.loader.PluginLoader(
        'shell_plugin',
        'ansible.plugins.shell_plugin',
        'C.DEFAULT_SHELL_PLUGIN_PATH',
        'shell_plugin')
    plugin_loader.add_directory(os.path.join(ANSIBLETOWER_DATA_PATH, 'shell_plugins'))
    assert plugin_loader._get_paths() == [os.path.join(ANSIBLETOWER_DATA_PATH, 'shell_plugins')]



# Generated at 2022-06-13 13:18:00.721480
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    """
    Test PluginLoader.__contains__()
    """
    pl = PluginLoader(package="ansible.plugins.action", class_name="ActionModule")
    assert 'ping' in pl  # noqa



# Generated at 2022-06-13 13:18:06.073973
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    """Unit test for method all of class Jinja2Loader"""
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.loader import Jinja2Loader
    from ansible.plugins.filter.core import FilterModule
    from ansible.plugins.test.core import TestModule
    import os
    import sys

    # Create and store a mock file name with test jinja2 plugin and add to sys.path
    file_name = 'test_plugin.py'

# Generated at 2022-06-13 13:18:15.955524
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    plugin_loader = PluginLoader('some_class_name', 'some_package', 'some_path', '*.py', 'my_base_class', 'some_collection_list')
    with patch.object(C, 'DEFAULT_MODULE_PATH', DEFAULT_MODULE_PATH):
        with patch.object(C, 'DEFAULT_COLLECTIONS_PATHS', DEFAULT_COLLECTIONS_PATHS):
            with patch.object(display, 'warning', return_value=None) as display_warning:
                with patch.object(PluginLoader, '_get_paths', return_value=DEFAULT_MODULE_PATH):
                    plugin_load_context = plugin_loader.find_plugin_with_context(name='foo', collection_list=['c1', 'c2'])
    assert display_warning.called
   

# Generated at 2022-06-13 13:18:22.065608
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
        assert "c_loader" in globals(), "Test requires that c_loader be created before testing this function"
        add_dirs_to_loader("c", ["test/units/plugins/test_loader/plugins/c"])
        assert len(c_loader.all()) == 3, "Test requires that c_loader have only the test plugin in it for testing"
        assert c_loader.get("plugin_c_one") is not None, "Test failed to identify plugin: plugin_c_one"
        assert c_loader.get("plugin_c_two") is not None, "Test failed to identify plugin: plugin_c_two"
        assert c_loader.get("plugin_c_subdir") is not None, "Test failed to identify plugin: plugin_c_subdir"

# Generated at 2022-06-13 13:18:22.993371
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # FIXME: This is currently untested
    pass


# Generated at 2022-06-13 13:18:30.103377
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    # Create a plugin loader (Mocked for test)
    class MockedJinja2Loader(Jinja2Loader):
        def _get_paths(self):
            return [
                'path1/file1.py',  # file 1
                'path2/file2.py',  # file 2
                'path3/file3.py',  # file 3
                'path4/file4.py',  # file 4
                'path5/file5.py',  # file 5
                'path6/file6.py',  # file 6
            ]

    plugin_loader = MockedJinja2Loader()
    # Use all method to retrieve all plugins (File list)
    plugin_files = plugin_loader.all()

    # Check file list

# Generated at 2022-06-13 13:18:38.738900
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    pl = PluginLoader('action_plugins', package='ansible.plugins')
    # Test_PluginLoader_find_plugin_1
    pl._get_paths = lambda: ['actions']
    pl.plugin_patterns = ['.*']
    pl.package = 'ansible.plugins'
    pl._searched_paths = ['actions']
    pl._display_plugin_load = lambda class_name, name, searched_paths, path, found_in_cache=None, class_only=None:  None
    name = 'foo'
    collection_list = ['test_collections/collection_1']
    assert pl.find_plugin(name, collection_list=collection_list) is not None, "PluginLoader.find_plugin returned wrong value"
    # Test_PluginLoader_find_plugin_2
    pl._get_

# Generated at 2022-06-13 13:18:48.224975
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # param: name: A string, the name of the plugin to load.
    # param: collection_list: Optional list of collections to search for plugins.
    #     If specified, only the specified collections will be searched for plugins. 
    #     This will override the list of collections in the ``ANSIBLE_COLLECTIONS_PATHS`` environment
    #     variable, and the ``collections`` key of the ``ansible.cfg`` configuration file.
    # returns: (PluginLoadContext, PluginLoadContext.plugin_resolved_name)
    results = PluginLoader.find_plugin(name = None, collection_list = None)
    if (results[0] == None
        and results[1] == None):
        # Success
        print('Success:  PluginLoader.find_plugin returned expected results')

# Generated at 2022-06-13 13:18:55.344945
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    import json
    from collections import namedtuple
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock, call
    from ansible_collections.notstdlib.moveitallout.plugins.loader import PluginLoader
    from ansible_collections.notstdlib.moveitallout.plugins.loader import collect_subclasses
    from ansible_collections.notstdlib.moveitallout.plugins.loader import get_with_context_result
    Plugin = namedtuple('Plugin', 'ATTRIBUTES')
    ConfigMeta = namedtuple('ConfigMeta', 'ATTRIBUTES')
    PluginLoadContext = namedtuple('PluginLoadContext', 'ATTRIBUTES')

# Generated at 2022-06-13 13:19:44.418043
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    args = [
        None,
        'test_PluginLoader_find_plugin_with_context',
        None,
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context',
        None,
        None,
        None,
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context',
        'test_PluginLoader_find_plugin_with_context'
    ]


# Generated at 2022-06-13 13:19:48.339244
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    """
    add_dirs_to_loader()
    """
    paths = [ 'test' ]
    which_loader = 'action'
    add_dirs_to_loader('action',paths)


# Generated at 2022-06-13 13:19:50.198463
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    assert False, "Unit tests for Jinja2Loader.find_plugin not written"



# Generated at 2022-06-13 13:20:01.005518
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''
    Test that add_all_plugin_dirs properly adds all plugin directories.
    Improperly, this function also depends on globals().  The test should
    be updated if globals() changes.
    '''
    testdir = '/tmp/ansible_test_plugins'
    os.mkdir(testdir)
    try:
        add_all_plugin_dirs(testdir)

        for loader_name, loader in get_all_plugin_loaders():
            assert testdir in loader.get_directories()
            if loader.subdir:
                assert os.path.join(testdir, loader.subdir) in loader.get_directories()

    finally:
        os.rmdir(testdir)



# Generated at 2022-06-13 13:20:08.368316
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():

    # Test with collections
    def test_find_plugin_with_collections_mock_collection_loader(mocker, fixture_path, monkeypatch):

        # setup
        monkeypatch.setattr(PluginLoader, "_get_package_path", lambda s: fixture_path)

        # test
        def mock_collection_loader(namespace, name, collection_list=[]):
            return PluginLoader(namespace, to_text(os.path.join(os.path.sep, namespace, name)), collection_list=collection_list)

        mock_collections = mocker.Mock()
        mock_collections.get_loader.side_effect = mock_collection_loader

        mock_collections_manager = mocker.Mock()
        mock_collections_manager.get_collections.return_value = mock_collections

       

# Generated at 2022-06-13 13:20:10.472386
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():

    assert getattr(sys.modules[__name__], '%s_loader' % 'action').subdir == 'action_plugins'


# Generated at 2022-06-13 13:20:11.525656
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    p = PluginLoader('', "foo", C.DEFAULT_MODULE_PATH, '', 'bar')


# Generated at 2022-06-13 13:20:21.664596
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    '''
    Unit test for method
    `ansible.utils.plugin_docs.PluginLoader.find_plugin_with_context`
    of class `ansible.utils.plugin_docs.PluginLoader`.
    '''
    # Test with specific arguments for method
    # ansible.utils.plugin_docs.PluginLoader.find_plugin_with_context of
    # class ansible.utils.plugin_docs.PluginLoader.
    result = plugin_docs.PluginLoader('',
                                      '',
                                      'ansible.plugins.action',
                                      'ActionModule',
                                      'ansible.plugins.action.ActionBase').\
                                      find_plugin_with_context(name='debug',
                                                               class_only=False,
                                                               only_first=False,
                                                               collection_list=None)

# Generated at 2022-06-13 13:20:26.251176
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    # Create a plugin loader and add a path /tmp/foo
    pl = PluginLoader('ansible_collections.ansible.builtin', 'FooModule')
    pl.add_directory('/tmp/foo')
    # Verify result
    assert len(pl._plugin_paths) == 1 and pl._plugin_paths[0] == '/tmp/foo'


# Generated at 2022-06-13 13:20:37.973117
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    which_loader = 'shell'
    paths = ['test_add_dirs_to_loader']

    loader = getattr(sys.modules[__name__], '%s_loader' % which_loader)

    if not isinstance(loader, PluginLoader):
        raise AssertionError("loader is not a PluginLoader")

    for path in paths:
        if path in loader._directories:
            raise AssertionError("path should not already be in loader directories: %s" % path)

    add_dirs_to_loader(which_loader, paths)

    for path in paths:
        if path not in loader._directories:
            raise AssertionError("path not found in loader directories: %s" % path)


# Generated at 2022-06-13 13:21:22.668246
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # Test function PluginLoader.all in PluginLoader.py
    # Test the constructor call
    loader = PluginLoader("", "", "", "", "")
    # Test the all method
    for i in loader.all():
        print(i)


# Generated at 2022-06-13 13:21:33.135526
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    # Test the record_deprecation method of class PluginLoadContext when no removal_date exists
    # ---------------------------------------------
    # Test 1
    deprecation = PluginLoadContext()
    deprecation.record_deprecation(name="yum",
                                   deprecation={"warning_text":"deprecated", "removal_versio": "2.0"},
                                   collection_name="")
    deprecation.record_deprecation(name="apt",
                                   deprecation={"warning_text": "deprecated", "removal_date": "2020-01-01"},
                                   collection_name="")
    assert(deprecation.deprecation_warnings[0] == "yum has been deprecated.  deprecation")

# Generated at 2022-06-13 13:21:44.036669
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    sh_executable = "/foo/bar/sh"
    missing_shell_type = "missing_shell_type"
    shell_type = "sh"
    shell_executable = "/bin/sh"
    shell_type_not_required = "python"

    # Missing Shell type and executable
    try:
        shell = get_shell_plugin(shell_type = missing_shell_type, executable = None)
    except AnsibleError:
        pass

    # Shell type and missing executable
    try:
        shell = get_shell_plugin(shell_type = shell_type, executable = None)
    except AnsibleError:
        pass

    # Shell type not required but shell executable

# Generated at 2022-06-13 13:21:53.545340
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    # Prepare test objects
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
    _PLUGIN_PATH_CACHE = {}
    _PLUGIN_PACKAGE_PATH_CACHE = {}
   

# Generated at 2022-06-13 13:21:59.938907
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.modules.shell import ShellModule

    shell_plugin = get_shell_plugin('sh', '/bin/sh')
    assert isinstance(shell_plugin, ShellModule)
    assert shell_plugin.executable == '/bin/sh'

    shell_plugin = get_shell_plugin('sh')
    assert isinstance(shell_plugin, ShellModule)
    assert shell_plugin.executable == '/bin/sh'

    shell_plugin = get_shell_plugin(executable='/usr/bin/zsh')
    assert isinstance(shell_plugin, ShellModule)
    assert shell_plugin.executable == '/usr/bin/zsh'

    try:
        get_shell_plugin()
    except AnsibleError as e:
        assert 'Either a shell type or a shell executable must be provided' in to_native(e)



# Generated at 2022-06-13 13:22:10.076634
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
  # Test with no arguments
  plugin_loader = PluginLoader('foo')
  assert plugin_loader.find_plugin() == None

  assert plugin_loader.find_plugin(name='name') == None

  plugin_load_context = PluginLoadContext()
  plugin_load_context.nope = MagicMock()
  plugin_load_context.resolved = True
  plugin_load_context.resolved_path = None
  plugin_load_context.resolved_plugin_name = None
  plugin_load_context.plugin_object = None
  plugin_load_context.plugin_resolved_path = None
  plugin_load_context.plugin_resolved_name = None
  plugin_load_context.redirect_list = None


# Generated at 2022-06-13 13:22:20.498925
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # make sure we start with a clean slate
    for name, obj in get_all_plugin_loaders():
        obj.directories = []
    # test directory path
    test_dir = "/tmp/ansible_plugin_test"
    # create mock test_dir plugin directories
    # test_dir
    #  |-- lookup_plugins
    #  |-- inventory_plugins
    #  |-- callback_plugins
    #  |-- filter_plugins
    #  |-- connection_plugins
    #  |-- module_utils
    #  |-- modules
    #  |-- module_utils
    #  |-- action_plugins
    #  |-- module_utils
    #  |-- httpapi_plugins

    os.mkdir(test_dir)
    os.chdir(test_dir)


# Generated at 2022-06-13 13:22:34.181159
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    # Test creation and state of empty plugin loader
    pl = PluginLoader('test', '', required_base_class=object, require_init=False)
    assert pl.directories == []

    # Test adding directory to empty plugin loader
    b_path = os.path.expanduser("~/plugins")
    pl.add_directory(b_path)
    assert os.path.abspath(pl.directories[0]) == os.path.abspath(b_path)

    # Test adding non-existent directory to empty plugin loader
    b_path = os.path.expanduser("~/plugins")
    pl.add_directory(b_path)
    assert os.path.abspath(pl.directories[0]) == os.path.abspath(b_path)

    # Test adding directory to non-empty

# Generated at 2022-06-13 13:22:45.033330
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Make some mock objects
    class loader(object):
        def __init__(self):
            self.subdir = 'subdir'
            self.module_path = set()

        def add_directory(self, path):
            self.module_path.add(path)

    class display(object):
        def __init__(self):
            self.warning_messages = set()

        def warning(self, msg):
            self.warning_messages.add(msg)

    old_display = PluginLoader.display
    old_loader = sys.modules[__name__].loader

    sys.modules[__name__].loader = loader()
    PluginLoader.display = display()

    # Test that we don't add a non-directory
    add_all_plugin_dirs("/not/a/real/path")

# Generated at 2022-06-13 13:22:53.477284
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Make sure none of these throw exceptions
    # 1) loads a plugin by name
    plugin_loader = PluginLoader(package='ansible.plugins.action',
                                 class_name='ActionBase',
                                 base_class='ActionBase',
                                 config_base=None,
                                 config_section=None,
                                 subdir=None,
                                 aliases={},
                                 required_base_class=None)
    plugin_load_context = plugin_loader.find_plugin_with_context('debug')
    assert plugin_load_context.plugin_resolved_name == 'debug'

    # 2) loads a plugin by name with a collection prefix
    plugin_load_context = plugin_loader.find_plugin_with_context('ansible_collections.my_ns.my_coll.my_plugins.my_action')
   

# Generated at 2022-06-13 13:23:45.880149
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Imports
    import glob
    import os.path
    import sys

    # Import local modules
    from ansible import constants as C
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.utils import plugin_docs
    from ansible.utils.collection_loader import get_collection_name_from_path, get_collection_to_path_map
    from unit.utils.hacking.helpers import mock_context, mock_scope

    # Setup test data
    TEST_PATH = os.path.join(os.path.dirname(__file__), 'plugin_loader')
    ANSIBLE_PATH = [os.path.join(TEST_PATH, 'ansible'), os.path.join(TEST_PATH, 'ansible/module_utils')]


# Generated at 2022-06-13 13:23:58.036917
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    collection_list = [
        CollectionRequirement.from_str('foo.abc'),
        CollectionRequirement.from_str('foo.xyz'),
    ]
    collection_paths = ['/foo/abc', '/foo/xyz']

    mock_plugin_loader_class = MockPluginLoaderClass('foo', 'bar', 'baz', 'asdf')
    mock_plugin_loader_class._get_paths = Mock(return_value=collection_paths)
    mock_plugin_loader_class._get_package_paths = Mock(return_value=[])

    mock_plugin_loader_class.package_name = 'foo'

    mock_obj_instance = Mock(spec=mock_plugin_loader_class.base_class)
    mock_obj_instance._load_name = 'test_plugin'
    mock_obj

# Generated at 2022-06-13 13:24:07.071720
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    pl = PluginLoader('foo', 'bar', 'baz')
    pl.package = 'ansible.plugins.foo'
    pl.class_name = 'bar'
    pl.base_class = 'baz'
    with pytest.raises(AnsibleError) as exec_info:
        pl.find_plugin_with_context('test1')
    assert "Specify the class_name and base_class" in to_text(exec_info.value)
    with pytest.raises(AnsibleError) as exec_info:
        pl.find_plugin_with_context('test2')
    assert "Specify the package" in to_text(exec_info.value)



# Generated at 2022-06-13 13:24:17.353576
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import ansible

    os.chdir(self.test_dir)
    C.DEFAULT_DEBUG = True
    plugin_loader = PluginLoader(
        'ActionModule',
        'ansible.plugins.action',
        'ansible.plugins',
        C.DEFAULT_ACTION_PLUGIN_PATH.split(os.pathsep),
        'action_plugins')
    plugin_loader.all()
    plugin_loader.all(class_only=True)
    plugin_loader.all(check=True)
    plugin_loader.all(raise_on_error=True)
    ansible.plugins.action.synchronize = MagicMock(return_value='mod_obj')

# Generated at 2022-06-13 13:24:31.318398
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    '''
    Unit test for method find_plugin_with_context in class PluginLoader
    '''
    class_name = 'test_class_name'
    package = 'test_package'
    base_class = 'test_base_class'
    subdir = 'test_subdir'

    data = PluginLoader(
        class_name=class_name,
        package=package,
        base_class=base_class,
        subdir=subdir
    )

    assert data.class_name == 'test_class_name'
    assert data.package == 'test_package'
    assert data.base_class == 'test_base_class'
    assert data.subdir == 'test_subdir'
    assert data.aliases == {}
    assert data.badchars == '-#$+,'


# Generated at 2022-06-13 13:24:39.801125
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Set up mock objects and method calls
    path = '/path/to/plugins'
    suffix = 'suffix'
    name = 'hello'
    full_name = 'ansible.plugins.xxx.%s' % name
    look_for = ['.py', '.ps1', '.bat', '.exe']
    search_path = os.path.join(path, '%s*' % name)

    # Call method
    pl = PluginLoader('ansible.plugins.xxx', 'Plugin', '', '', '', auto_add=False)
    pl._searched_paths.append(path)

# Generated at 2022-06-13 13:24:49.834672
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    import tempfile
    from shutil import rmtree
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.plugins.test.test_strategy import TestStrategy
    # create a test directory for script plugin
    temp_dir = tempfile.mkdtemp(prefix='ansible_test_ansible_strategy_plugins')
    # create a test directory for collection_directory
    collection_directory = tempfile.mkdtemp(prefix='ansible_test_ansible_strategy_plugins')

    strategy_name = 'test_strategy_loader'
    file_name = '%s.py' % strategy_name
    # create the script plugin file
    strategy_file_path = os.path.join(temp_dir, file_name)

    # write the test strategy plugin

# Generated at 2022-06-13 13:24:55.634649
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Set up some mock plugin loaders
    obj_1 = object()
    obj_2 = object()
    obj_1.subdir = 'foo'
    obj_2.subdir = 'bar'
    obj_1.add_directory_called = False
    obj_2.add_directory_called = False

    def mock_add_directory(path):
        obj_1.add_directory_called = path

    obj_1.add_directory = mock_add_directory
    obj_2.add_directory = mock_add_directory

    def get_all_plugin_loaders_1():
        return [('obj_1', obj_1), ('obj_2', obj_2)]

    globals()['get_all_plugin_loaders'] = get_all_plugin_loaders_1
    # Start testing
    #

# Generated at 2022-06-13 13:24:58.075611
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin = PluginLoader(package='ansible.plugins.action')

    assert (plugin == plugin) is False


# Generated at 2022-06-13 13:25:08.473245
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import copy
    import inspect
    import mock
    import os
    import tempfile
    import unittest

    # Find the path to the source file of the current module.
    # We'll need to use it when we create an instance of PluginLoader.
    path_to_source_file = inspect.getsourcefile(test_PluginLoader_all)
    base_path = os.path.split(os.path.abspath(os.path.dirname(path_to_source_file)))[0]

    # Also find the path to the top-level of the Ansible code.
    plugin_loader_module = __import__('ansible.plugins.loader')
    name_of_plugin_loader_module = plugin_loader_module.__name__