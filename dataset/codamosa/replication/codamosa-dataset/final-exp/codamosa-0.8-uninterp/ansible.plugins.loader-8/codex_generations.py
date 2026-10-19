

# Generated at 2022-06-13 13:17:40.724771
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    args = {}
    kwargs = {}


# Generated at 2022-06-13 13:17:53.049585
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    test_paths = ['a', 'b', 'c']
    loaders = ['module', 'module_utils', 'lookup', 'filter', 'netconf', 'terminal', 'action', 'connection']

    for loader in loaders:
        assert len(getattr(sys.modules[__name__], '%s_loader' % loader)._get_paths()) == 0
    add_dirs_to_loader('module', test_paths)
    assert len(module_loader._get_paths()) == 3
    add_dirs_to_loader('module_utils', test_paths)
    assert len(module_utils_loader._get_paths()) == 3
    add_dirs_to_loader('lookup', test_paths)
    assert len(lookup_loader._get_paths()) == 3


# Generated at 2022-06-13 13:18:02.678670
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    PLUGIN_PATHS_DIR = os.path.dirname(os.path.abspath(__file__))


# Generated at 2022-06-13 13:18:08.487705
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # pylint: disable=redefined-outer-name
    import tempfile
    import shutil
    import sys
    import os

# Generated at 2022-06-13 13:18:17.346026
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
	# Test the happy case
	loader = PluginLoader('ansible.plugins', 'FilterModule', C.DEFAULT_INTERNAL_PLUGIN_PATH, C.DEFAULT_PLUGIN_PATH)
	loader.add_directory(C.DEFAULT_INTERNAL_PLUGIN_PATH)
	assert loader._search_paths == ['/usr/lib/python2.7/site-packages/ansible/plugins/filter_plugins', '/etc/ansible/plugins/filter_plugins', '/etc/ansible/plugins']
	# Test if path is already added
	loader.add_directory(C.DEFAULT_INTERNAL_PLUGIN_PATH)

# Generated at 2022-06-13 13:18:22.603997
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    """
    Test method __contains__ of class PluginLoader
    """
    ######################
    ######## Arrange #####
    ######################

    ######################
    ###### Act/Assert #####
    ######################
    assert True == False # TODO: implement your test cases here



# Generated at 2022-06-13 13:18:32.568875
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    name = 'name'
    plugin_load_result = PluginLoadResult('name')
    plugin_load_result.resolved = True
    plugin_load_result.plugin_resolved_path = 'path'
    plugin_load_context = PluginLoadContext('name', path_only='path')
    plugin_load_context.add_plugin_result(plugin_load_result)

    # Test with default parameters
    with patch.object(PluginLoader, 'find_plugin_with_context', return_value=plugin_load_context):
        pl = PluginLoader('package', 'base_class', 'class_name')
        result = pl.__contains__(name)
        assert result is True

    # Test with collection_list parameter

# Generated at 2022-06-13 13:18:44.424306
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import sys
    import glob
    from ansible.plugins.loader import _PLUGIN_FILTERS
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import string_types
    import os
    import tempfile
    from ansible.collections import ansible_collections_path_cache
    from ansible.module_utils._text import to_native
    from ansible.collections.lookup.basic import BasicLookupPlugin
    from ansible.utils.collection_plugins import AnsibleCollectionRef, is_collection_ref
    from ansible.errors import AnsibleError

    # init function already called by setup_loader, skip it here
    # AnsiblePluginLoader.init()
    # path_only doesn't work in python2.6
    # test class_only =

# Generated at 2022-06-13 13:18:46.748683
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
  plugin_loader = PluginLoader()

# Generated at 2022-06-13 13:18:47.155803
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    pass



# Generated at 2022-06-13 13:19:42.917487
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    pl = PluginLoader(package='ansible.plugins.connection', subdir='', class_name='ConnectionBase')
    for con in pl._get_paths():
        print(con)
    print(pl.package)
    ctx = pl.get_with_context(name='local', class_only=True)
    print(ctx.plugin_resolved_name)
    print(ctx.plugin_resolved_path)
    pobj = pl.get_with_context(name='local')
    print(pobj.__class__.__name__)
    print(pobj.__class__)


# Generated at 2022-06-13 13:19:43.782587
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    return



# Generated at 2022-06-13 13:19:54.913105
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    import types
    from ansible.constants import DEFAULT_CALLBACK_WHITELIST
    # Verify that the callback_loader is not in the global namespace to start
    assert 'callback_loader' not in globals()
    # Verify that adding a directory with the callback_loader produces a loader class
    add_dirs_to_loader('callback', '../test/units/plugins/callback/')
    assert 'callback_loader' in globals()
    assert isinstance(callback_loader, types.ModuleType)
    # Verify that the loader has a list of available plugins
    assert hasattr(callback_loader, '_plugins')
    assert sorted(callback_loader._plugins.keys()) == sorted(['minimal', 'test_callback'])
    # Verify that the loader has a list of plugins by magic tag

# Generated at 2022-06-13 13:20:01.625165
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    # PluginLoader.__setstate__(state)
    # test PluginLoader.__setstate__().
    # Should be an undocumented private method.
    # Raises an exception if the object is in wrong state or if any of the mandatory
    # attributes are missing.
    pl = PluginLoader('')
    class test(object):
        def __setstate__(self, state):
            pass
    pl.all = test
    assert pl.all.__setstate__('state') == None

# Generated at 2022-06-13 13:20:07.266267
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    world = {'was_called': False}

    class MockPathEntry(object):
        def __init__(self, path):
            pass

        def add_directory(self, path):
            world['was_called'] = True

    _get_path_entry_mock = MagicMock(return_value=MockPathEntry('/dir'))

    with patch('os.path.isdir', _get_path_entry_mock):
        pl = PluginLoader('module', 'module_utils', 'module_utils')
        pl.add_directory('/dir')

    assert world['was_called'] is True



# Generated at 2022-06-13 13:20:15.544082
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    module_path = "ansible.plugins.loader.get_all_plugin_loaders"
    set_module_args({})
    module_return_value = dict(
        hello=dict(
            module_utils=dict(
                a=0
            )
        )
    )
    with patch(module_path, return_value=module_return_value):
        with pytest.raises(AnsibleError) as e:
            PluginLoader.__setstate__()
        assert "PluginLoader state is missing 'package'" in to_text(e)


# Generated at 2022-06-13 13:20:24.310092
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    test_display = mock.MagicMock()
    test_package = 'test_package'
    test_paths = 'test_paths'
    test_aliases = 'test_aliases'
    test_class_name = 'test_class_name'
    test_base_class = 'test_base_class'
    test_subdir = 'test_subdir'
    test_cache_size = 'test_cache_size'
    test_searched_paths = 'test_searched_paths'
    test_module_cache = 'test_module_cache'
    test_path_module_cache = 'test_path_module_cache'
    test_plugin_finder_cache = 'test_plugin_finder_cache'
    test_plugin_data = 'test_plugin_data'
    test_

# Generated at 2022-06-13 13:20:28.211809
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    pl = PluginLoader(package='my_package', directories=['my_directory'])
    pl.add_directory('new_directory')
    assert pl.directories == ['my_directory', 'new_directory']


# Generated at 2022-06-13 13:20:38.395002
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    assert get_with_context_result(None, None)
    assert get_with_context_result(None, AnsibleActionLoadingContext())
    assert get_with_context_result(None, 'test')
    assert not get_with_context_result(None, 'test').plugin_loading_context
    assert get_with_context_result('test', 'test').object == 'test'
    assert get_with_context_result('test', None).object == 'test'


# Generated at 2022-06-13 13:20:44.962023
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    '''
    Unit tests for ansible.plugins.loader.PluginLoader.all.
    '''
    _logger = logging.getLogger('unittest')
    _logger.addHandler(logging.NullHandler())
    display = Display(_logger)
    # Test with name that is not in mocked list of filter_plugins names
    plugin_loader = PluginLoader('filter_plugins', '', 'ansible.plugins.filter', 'FilterModule', display)
    assert 'python' not in plugin_loader.all(path_only=True)
    # Test with mocked list of filter_plugins names

# Generated at 2022-06-13 13:21:22.457263
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    class FakePluginLoader(object):
        def __init__(self, subdir):
            self.subdir = subdir
            self.added_paths = []

        def add_directory(self, path):
            self.added_paths.append(path)

    fake_loader_1 = FakePluginLoader('fake_subdir_1')
    fake_loader_2 = FakePluginLoader('fake_subdir_2')

    # Return values for globals().items(), above
    globals_items = [('fake_loader_1', fake_loader_1),
                     ('fake_loader_2', fake_loader_2)]

    with patch('ansible.plugins.loader.globals', return_value=globals_items):
        # Return value for os.path.isdir()
        os_path_isdir = True


# Generated at 2022-06-13 13:21:31.780814
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    from ansible.module_utils._text import to_bytes
    from collections import namedtuple
    from ansible.parsing.utils.module_docs import get_docstring
    from ansible.template import Templar

    TaskResult = namedtuple('TaskResult', ['content', 'result'])

    # Test as_plugin_filter
    loader = ModuleLoader()
    plugin = loader.get_plugin('filter', 'flatten')
    templar = Templar(loader=loader)
    result = [TaskResult(content={'x': {'y': [1, 2, 3]}}, result={'x': {'y': [1, 2, 3]}}),
               TaskResult(content={'z': [9, 8, 7]}, result={'z': [9, 8, 7]})
               ]


# Generated at 2022-06-13 13:21:46.760637
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Make sure we have a clean slate
    PluginLoader.clear_directory_cache()
    # TODO: test adding a path that doesn't exist
    # Create a temporary path containing a few plugin dirs
    import tempfile
    from shutil import rmtree
    from os import mkdir
    from os.path import join
    temp_path = tempfile.mkdtemp()
    for plugin_type in ("action", "callback", "module", "lookup"):
        mkdir(join(temp_path, plugin_type))
    # Test the function
    add_all_plugin_dirs(temp_path)
    # Clean up
    rmtree(temp_path)
    assert len(get_all_plugin_loaders()[0][1]._get_directories()) == 1



# Generated at 2022-06-13 13:21:54.280287
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    PLUGIN_PATH = to_native(data_context().content.plugin_paths[0])
    my_plugin_loader = PluginLoader('actions', 'ActionModule', 'ansible.plugins.action', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_', required_base_class='ActionBase')
    # Test with invalid data
    try:
        my_plugin_loader.__contains__('')
    except Exception as e:
        assert type(e) == AnsibleError
    # Test with valid data
    assert my_plugin_loader.__contains__(os.path.basename(PLUGIN_PATH)) == True

# Generated at 2022-06-13 13:22:00.913482
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    pl = PluginLoader(package='ansible.plugins.action', subdir='foo', class_name='Bar')
    pl.__setstate__({'os_path': 'a', 'class_name': 'b', 'subdir': 'c', '_searched_paths': 'd', 'package': 'e',
                     '_module_cache': 'f', '_cache_max_size': 'g', '_configured_dependency_map': 'h',
                     '_configured_collection_map': 'i', 'base_class': 'j'})
    assert pl.os_path == 'a'
    assert pl.class_name == 'b'
    assert pl.subdir == 'c'
    assert pl._searched_paths == 'd'
    assert pl.package == 'e'
    assert pl._

# Generated at 2022-06-13 13:22:03.696108
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    # Initializing test
    test_loader = PluginLoader()
    test_dict = dict()

    # Testing methods
    test_loader.__setstate__(test_dict)

# Generated at 2022-06-13 13:22:12.764887
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pl = PluginLoader(
        'ansible.plugins.action',
        class_name='ActionBase',
        base_class='ActionBase',
        config_base=None,
        package='ansible',
        config_base_class='ActionModule')
    plugins = pl.all()
    msg = 'number of plugins returned by all is not correct'
    assert len(plugins) == 620, msg

    pl = PluginLoader(
        'ansible.plugins.action',
        class_name='ActionBase',
        base_class='ActionBase',
        config_base=None,
        package='ansible',
        config_base_class='ActionModule')
    plugins = pl.all(path_only=True)
    msg = 'number of plugins returned by all with path_only is not correct'
    assert len(plugins) == 620, msg

# Generated at 2022-06-13 13:22:19.420201
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    test_plugin_class = namedtuple('TestPluginClass', ['subdir'])
    test_plugin_class.subdir = 'test'
    test_plugin_class.add_directory = lambda x: True
    test_plugin_class.get_all = lambda: ['TestPlugin']
    sys.modules['ansible.plugins.test'] = test_plugin_class()
    mock_dir = './test_dir'

    add_all_plugin_dirs(mock_dir)
    sys.modules.pop('ansible.plugins.test')



# Generated at 2022-06-13 13:22:33.093978
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    my_plugin_directory = os.path.join(C.DEFAULT_LOCAL_TMP, "test_plugins")
    if os.path.isdir(my_plugin_directory):
        shutil.rmtree(my_plugin_directory)
    os.makedirs(my_plugin_directory)
    os.environ['ANSIBLE_CALLBACK_PLUGINS'] = my_plugin_directory
    os.environ['ANSIBLE_ACTION_PLUGINS'] = my_plugin_directory
    os.environ['ANSIBLE_LIBRARY'] = my_plugin_directory
    os.environ['ANSIBLE_FILTER_PLUGINS'] = my_plugin_directory
    os.environ['ANSIBLE_TEST_PLUGINS'] = my_plugin_directory

# Generated at 2022-06-13 13:22:43.631053
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    class Foo(object):
        pass

    class TestPluginLoader_all(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_all__is_instance(self):
            loader = PluginLoader('test', '', 'foo', 'bar', required_base_class=Foo)
            loader._get_paths = mock.MagicMock(return_value=['invalid'])
            loader._load_module_source = mock.MagicMock()

            result = loader.all()

            self.assertIsInstance(result, collections.Iterator)

        def test_all__class_only__return_1(self):
            loader = PluginLoader('test', '', 'foo', 'bar', required_base_class=Foo)
            loader._get_paths