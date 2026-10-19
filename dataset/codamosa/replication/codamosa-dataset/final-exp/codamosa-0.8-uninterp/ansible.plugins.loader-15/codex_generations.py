

# Generated at 2022-06-13 13:17:16.392084
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    from ansible import constants as C
    import ansible.plugins.action


# Generated at 2022-06-13 13:17:19.613498
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # Test with all valid values of filters
    # Test with all invalid values of filters
    # Test with filters as None
    pass


# Generated at 2022-06-13 13:17:25.353546
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    loader = PluginLoader('/usr/lib/python2.7/dist-packages/ansible/plugins/action', 'ActionModule', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins')
    loader.__setstate__({})



# Generated at 2022-06-13 13:17:29.041379
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    def get_basenames(plugins):
        return [os.path.basename(p.__file__) for p in plugins]

    # We have a test directory we can use to create a jinja2 loader
    loader = Jinja2Loader('test')

    # This test directory has a few files.  Collect them all up here.
    files = loader.all()

    # Here is the list of files in the test directory
    files_basenames = get_basenames(files)
    assert files_basenames == ['collection_file.py', 'lookup_loader.py', 'lookup_plugins.py', 'lookup_symlink.py', 'lookup_unclassified.py']



# Generated at 2022-06-13 13:17:30.614305
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert add_dirs_to_loader('module', ['/etc/ansible/modules'])



# Generated at 2022-06-13 13:17:34.690785
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    test_path = os.path.join(os.path.dirname(__file__), '../test_utils/plugins/sh')
    add_dirs_to_loader('shell', [test_path])
    # we should now be able to load our test shell plugin
    shell_loader.get('test_shell')



# Generated at 2022-06-13 13:17:38.181474
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    assert get_shell_plugin('sh', '/bin/bash')
    assert get_shell_plugin('sh', '/bin/bash').executable == '/bin/bash'
    assert get_shell_plugin('sh').SHELL_FAMILY == 'sh'
    assert not get_shell_plugin('shell', '/bin/bash')



# Generated at 2022-06-13 13:17:39.803381
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    PL = imp.new_module('PluginLoader')

# Generated at 2022-06-13 13:17:52.127727
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Make sure that the direct method is working
    assert PluginLoader.find_plugin('action_plugins', name='setup') is not None
    assert PluginLoader.find_plugin('action_plugins', name='setup', redirect_per_package_overrides={'raw_module': 'raw_module2'}) is not None
    assert PluginLoader.find_plugin('action_plugins', name='setup', redirect_per_package_overrides={'raw_module': ('raw_module2', 'raw_module3')}) is not None
    assert PluginLoader.find_plugin('action_plugins', name='setup', redirect_per_package_overrides={'raw_module': 'raw_module2', 'raw_module3': 'raw_module4'}) is not None

# Generated at 2022-06-13 13:18:01.946155
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    try:
        import __main__ as main
        main.PLUGIN_PATH_CACHE = {}
    except ImportError:
        pass

    test_plugin_loader = PluginLoader(
        'test_package',
        'test_class',
        package_paths,
        'ansible.test_utils.plugins.test_package'
    )
    plugins = test_plugin_loader.all()
    assert len(list(plugins)) == 2

    test_plugin_loader = PluginLoader(
        # TODO: fix the path below so it's not a relative path and so it works with all dists
        '../test_utils/plugins/test_package',
        'test_class',
        package_paths,
        'ansible.test_utils.plugins.test_package'
    )
    plugins = test_plugin

# Generated at 2022-06-13 13:19:14.997396
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    def get_collection_meta(deprecation):
        display = get_plugin_class('display')
        name = 'object_name_1'
        return display.deprecated(name, None, deprecation)

    # Test when the deprecation is None.
    deprecation = None
    p = PluginLoadContext()
    p.record_deprecation(name, deprecation, 'collection_name_1')
    assert True == p.deprecated
    assert None == p.removal_date
    assert None == p.removal_version
    assert deprecation == p.deprecation_warnings[0]

    # Test when the deprecation is a dict and it contains key 'warning_text' but not 'removal_date' or 'removal_version'.

# Generated at 2022-06-13 13:19:16.044251
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    assert(False)


# Generated at 2022-06-13 13:19:30.157433
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    import tempfile
    import shutil
    import collections

    def __add_all_plugin_dirs_check(subdirs, path, expected_dirs):
        # create temporary plugin directories
        plugin_dir = tempfile.mkdtemp()
        os.chdir(plugin_dir)


# Generated at 2022-06-13 13:19:31.276403
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    pass

# Generated at 2022-06-13 13:19:36.036573
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    class_under_test = PluginLoader
    # Input params for method under test
    name = None
    collection_list = None

    # Expected result
    expected_result = None

    # Invoke method under test
    result = class_under_test.has_plugin(name, collection_list)

    # Check result
    assert expected_result == result

# Generated at 2022-06-13 13:19:38.629022
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    '''
    Unit test for method PluginLoader.__setstate__
    '''
    pass

# Generated at 2022-06-13 13:19:45.340585
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    print('In test_PluginLoader_find_plugin')
    import ansible.plugins.action
    d = PluginLoader('action', 'ActionModule', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins')
    d._get_paths_from_collections()
    d.find_plugin('async')


# Generated at 2022-06-13 13:19:55.550819
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    import shutil
    import os
    from ansible.plugins.loader import PluginLoader
    from ansible.plugins.action import ActionModule
    from ansible.plugins.callback import CallbackModule
    from ansible.plugins.connection import Connection
    from ansible.plugins.shell import ShellModule
    from ansible.plugins.strategy import StrategyModule

    orig_plugin_search_path = [i for i in sys.path]

    tmpd = tempfile.mkdtemp()

    action = os.path.join(tmpd, 'action')
    connection = os.path.join(tmpd, 'connection')
    callback = os.path.join(tmpd, 'callback')
    shell = os.path.join(tmpd, 'shell')
    strategy = os.path.join(tmpd, 'strategy')



# Generated at 2022-06-13 13:19:59.596383
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    setattr(PluginLoader, '__setstate__', __setstate__)
    plugin_loader = PluginLoader(package='test.test_plugin_loader', class_name='test_plugin_loader_test_class_name')
    plugin_loader.__setstate__()


# Generated at 2022-06-13 13:20:03.384246
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    pl = PluginLoader('collection_name', 'name', 'base', 'class_name')
    # Using fixture to remove side effects
    pl.add_directory(os.path.join(os.path.dirname(__file__), 'fixtures', 'collections', 'test_ns', 'test_coll', 'plugins', 'test_dir'))
    assert '/test_dir' in pl._get_paths()

# Generated at 2022-06-13 13:21:59.584792
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    pass

# Generated at 2022-06-13 13:22:06.639481
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # verify method returns none when name is not provided
    print("\ntest_Jinja2Loader_get: method returns none when name is not provided")
    jinja2_loader = Jinja2Loader()
    assert jinja2_loader.get() is None
    # verify method returns none when name is not a string
    print("\ntest_Jinja2Loader_get: method returns none when name is not a string")
    assert jinja2_loader.get(123) is None
    # verify method returns none when name is an empty string
    print("\ntest_Jinja2Loader_get: method returns none when name is an empty string")
    assert jinja2_loader.get("") is None
    # verify method returns none when name is a string that is not in the list of plugins

# Generated at 2022-06-13 13:22:10.723421
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''Unit test for add_all_plugin_dirs'''
    file_path = os.path.abspath(os.path.dirname(__file__))
    plugin_path = os.path.abspath(os.path.join(file_path, '../../../plugins'))
    add_all_plugin_dirs(plugin_path)



# Generated at 2022-06-13 13:22:13.668402
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    test_instance = PluginLoader('module_utils', 'Ansiballz')
    # test_instance.get_with_context()


# Generated at 2022-06-13 13:22:19.860524
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    def test_plugin_regex_search_all(plugin_loader, subdir, base_class, class_name, expected_basenames,
                                 expected_loaded_modules, expected_searched_paths):
        class_only = False
        path_only = False
        dedupe = True

# Generated at 2022-06-13 13:22:33.620225
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    PLUGIN_LOADER_SEARCHED_PATHS = [
        'collection1/plugins/',
        'plugins/',
        'plugins/2/'
    ]

    COLLECTION_LIST = [
        {
            'origin': 'ansible.builtin',
            'name': 'ansible_builtin'
        },
        {
            'origin': 'ansible.base',
            'name': 'ansible_base'
        },
        {
            'origin': 'third_party_collection',
            'name': 'third_party_collection'
        }
    ]


# Generated at 2022-06-13 13:22:40.777521
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    deprecation = dict(warning_text='This is a test', removal_date='2020-01-01' )
    ctx = PluginLoadContext().record_deprecation('module name', deprecation, 'collection name')
    assert ctx.removal_date == '2020-01-01'
    assert ctx.removal_version is None
    assert ctx.deprecation_warnings == ['module name has been deprecated. This is a test']



# Generated at 2022-06-13 13:22:46.442984
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    name = get_fixture_path('empty_module.py')
    package = 'ansible_fixtures'
    plugin_type = 'module'
    mock_result = Mock(name=name, package=package, plugin_type=plugin_type)
    type(mock_result).__contains__ = Mock(return_value=name)
    assert isinstance(mock_result.__contains__(), basestring)



# Generated at 2022-06-13 13:22:57.945535
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    '''
    Unit tests for PluginLoader.all method
    '''
    display = Display()
    # Set up test plugin paths
    plugin_path = [
        '/plugin/path2/',
        '/plugin/path/',
        '/path/that/is/not/plugins/',
        '/base/path/',
        '/base/path/',
        '/base/path/'
    ]
    # Set up test plugins
    plugins = [
        'test_plugin.py',
        'filter_plugin.py',
        'test_plugin.py'
    ]
    # Set up plugin loader for testing
    test_plugin_loader = PluginLoader('/plugin/path', plugin_path, '.', C.DEFAULT_DEBUG, display)
    for plugin in plugins:
        assert plugin in test_plugin_loader.all()

# Generated at 2022-06-13 13:23:04.491699
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    from ansible.plugins.action.normal import ActionModule as ActionModule_normal
    from ansible.plugins.action.gathering import ActionModule as ActionModule_gathering
    from ansible.plugins.action.debug import ActionModule as ActionModule_debug

    action_loader = PluginLoader('ActionModule', 'ansible.plugins.action', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins', required_base_class=ActionBase)
    for i in action_loader.all():
        assert isinstance(i, ActionModule_normal) or isinstance(i, ActionModule_gathering) or isinstance(i, ActionModule_debug) or i == 'debug'


# Generated at 2022-06-13 13:24:16.964802
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    action_plugin_loader = ActionModuleLoader()
    secret_plugin_loader = SecretLoader()
    terminal_plugin_loader = TerminalPluginLoader()
    # Testing the function
    plugin_load_context = action_plugin_loader.get_with_context(name='pause', plugin_load_context=None)
    assert plugin_load_context.resolved
    assert plugin_load_context.plugin_resolved_name == 'pause'
    assert plugin_load_context.plugin_resolved_path == '/home/rsoares/.local/lib/python3.6/site-packages/ansible/plugins/action/pause.py'
    assert plugin_load_context.redirect_list == ['ansible.builtin.pause']

# Generated at 2022-06-13 13:24:24.014991
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader("action_plugin")
    plugin_name = 'copy'
    collection_list = []
    plugin = loader.find_plugin(plugin_name, collection_list=collection_list)
    print("plugin:", plugin)

test_PluginLoader_find_plugin()


# Generated at 2022-06-13 13:24:25.263070
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    assert True


# Generated at 2022-06-13 13:24:30.761586
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    for name, obj in get_all_plugin_loaders():
        assert not obj.get_directories()
        # create fake dir structure
        obj.add_directory('/path/to/{0}'.format(obj.subdir))
        assert obj.get_directories() == ['/path/to/{0}'.format(obj.subdir)]


# Generated at 2022-06-13 13:24:35.079735
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader = PluginLoader('test_plugins')
    get_with_context_result = plugin_loader.get_with_context('action')
    assert get_with_context_result.resolved
    assert get_with_context_result.object
    assert get_with_context_result.plugin_resolved_name == 'action'


# Generated at 2022-06-13 13:24:41.935773
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # legacy is either False or True
    legacy = False

    if legacy:
        collection_name = None
        jinja2_loader = Jinja2Loader('ansible.plugins.filter', 'FilterModule', 'ansible.plugins.filter.core')
    else:
        collection_name = 'namespace.collection'
        jinja2_loader = Jinja2Loader('namespace.collection.plugins.filter', 'FilterModule', 'namespace.collection.plugins.filter.core')


# Generated at 2022-06-13 13:24:51.268463
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    """
    Ensures that add_all_plugin_dirs works correctly
    """
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import PluginLoader
    # empty out the PATH_CACHE so we don't have
    # any directories already in it
    PATH_CACHE.clear()
    assert PATH_CACHE == {}

    # create a fake module dir
    test_module_dir = 'test_module_dir'
    os.mkdir(test_module_dir)

    # create a fake action plugin dir
    test_action_dir = 'test_action_dir'
    os.mkdir(test_action_dir)

    # add the fake dirs to PATH_CACHE
    add_all_plugin_dirs(test_module_dir)


# Generated at 2022-06-13 13:24:53.970929
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    l = PluginLoader(
        'ActionModule',
        'ansible.plugins.action',
        C.DEFAULT_ACTION_PLUGIN_PATH,
        'action_plugins',
    )
    assert l.find_plugin('file') == 'ansible.plugins.action.file'


# Generated at 2022-06-13 13:24:57.468724
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    '''
    Test find_plugin of PluginLoader
    '''
    loader = PluginLoader('ansible.plugins.action', 'ActionModule', 'action_plugins', required_base_class='ActionBase')
    assert loader.find_plugin('fail')[:-1] == ("ansible/plugins/action/fail.py", "ansible.plugins.action.fail")
    assert loader.find_plugin('set_fact')[:-1] == ("ansible/plugins/action/set_fact.py", "ansible.plugins.action.set_fact")

test_PluginLoader_find_plugin()



# Generated at 2022-06-13 13:25:07.803562
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    loader = Jinja2Loader()

    import ansible.plugins.filter.core
    import ansible.plugins.test.core

    # Test name is not a qualified collection ref
    assert loader.get('map') is ansible.plugins.filter.core.map
    assert loader.get('map') is ansible.plugins.test.core.map

    # Test name is a qualified collection ref
    # NOTE: this test is not as clean as it could be.  We're passing in a collection name, and this
    # method itself would normally determine the collection name.  It's not easy to figure out what
    # the calling code is passing in at this point.
    assert loader.get('ansible.legacy.filters.map') is ansible.plugins.filter.core.map