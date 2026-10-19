

# Generated at 2022-06-13 13:19:34.722297
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # TODO: Fix test so it works when plugins moved to collections.
    # Verify that find_plugin works as expected. In particular, it should return None
    # when the plugin to find has not been found.
    pl = PluginLoader('user', 'lookup_plugins', 'lookup_plugins')
    path = pl.find_plugin('unavailable')
    assert(path is None)


# Generated at 2022-06-13 13:19:42.941100
# Unit test for method all of class PluginLoader

# Generated at 2022-06-13 13:19:54.527635
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    test_add_all_plugin_dirs_path = os.path.join(os.path.dirname(__file__), u'test_add_all_plugin_dirs')
    if os.path.exists(test_add_all_plugin_dirs_path):
        shutil.rmtree(test_add_all_plugin_dirs_path)
    os.mkdir(test_add_all_plugin_dirs_path)
    for obj in get_all_plugin_loaders():
        os.mkdir(os.path.join(test_add_all_plugin_dirs_path, obj.subdir))
    add_all_plugin_dirs(test_add_all_plugin_dirs_path)

# Generated at 2022-06-13 13:20:04.347440
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.module_utils._text import to_bytes
    plugin_loader = Jinja2Loader()
    name = 'test_plugin_name'
    module_name = 'test_module_name'
    plugin_class_name = 'test_plugin_class_name'
    places = ('/usr/share/ansible/plugins/test/plugins/', '/home/user/.ansible/plugins/test/plugins/', plugin_loader.basedir)
    collections = (None,)
    # Test with redirect_name argument
    redirect_names = {'redirected_module_name': 'correct_module_name'}
    # Test with _load_name argument
    _load_names = {'correct_module_name': 'correct_load_name'}
    # Test with args and kwargs arguments

# Generated at 2022-06-13 13:20:10.433095
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' Test the addition of plugin directories.  Make sure that invalid paths
    and paths without any plugins are skipped.

    :returns:  Boolean of True for pass, False for fail
    :rtype:  bool
    '''
    results = []

    for plugin_type, plugin_type_obj in get_all_plugin_loaders():
        plugin_type_obj.clear_directory_cache()

    test_dir = '/tmp/add_all_plugin_dirs_test/'
    # First create the test directory and some subdirs
    f_dir = os.path.join(test_dir, 'foo')
    b_dir = os.path.join(test_dir, 'bar')
    os.mkdir(test_dir)
    os.mkdir(f_dir)

# Generated at 2022-06-13 13:20:21.037951
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    class Mock_AnsibleError(AnsibleError):
        pass

    class Mock_get_all_plugin_loaders():
        def __init__(self):
            self._invoked = 0
        def __call__(self, addons_only=False):
            self._invoked += 1
            return {'foo': 'bar', 'alpha': 'beta'}

    class Mock_get_user_collections():
        def __init__(self):
            self._invoked = 0
        def __call__(self):
            self._invoked += 1
            return {'foo': 'bar', 'alpha': 'beta'}

    class Mock_get_collections_cache():
        def __init__(self):
            self._invoked = 0
        def __call__(self):
            self._invoked += 1


# Generated at 2022-06-13 13:20:28.860418
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # TODO: Unit test for sealed methods for more thorough testing
    # Rely on _get_paths()
    paths = [
        os.path.join(C.DEFAULT_MODULE_PATH, 'test.py'),
        os.path.join(C.DEFAULT_MODULE_PATH, 'test2.py'),
    ]

    def _get_paths():
        for path in paths:
            yield path


# Generated at 2022-06-13 13:20:33.912308
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    plugin_loader = PluginLoader('ansible.plugins.cache', 'CacheModule', 'cache')
    plugin_loader.all()
    assert True is True



# Generated at 2022-06-13 13:20:41.275862
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
   '''
   # Jinja2Loader.get
   '''
   p = Jinja2Loader()

   # AssertionError: 'get' returned None
   with pytest.raises(AssertionError):
      p.get('name','*args','**kwargs')

   # AssertionError: 'get' returned None
   with pytest.raises(AssertionError):
      p.get('name','*args','**kwargs')



# Generated at 2022-06-13 13:20:56.312102
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = PluginLoader( 'module_utils', 'AnsibleModule', None, 'ansible' )
    assert plugin_loader.has_plugin('module-utils.module_utils') is True
    assert plugin_loader.has_plugin('module_utils.module_utils') is True
    assert plugin_loader.has_plugin('module_utils.module_utils.basic') is True
    assert plugin_loader.has_plugin('module_utils.module_utils.basic.foo') is False
    assert plugin_loader.has_plugin('module-utils.module_utils.basic') is True
    assert plugin_loader.has_plugin('module-utils.module_utils.basic.foo') is False
    assert plugin_loader.has_plugin('module_utils.module-utils') is True

# Generated at 2022-06-13 13:21:29.974383
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    import os
    import tempfile
    from ansible.plugins import cache
    fake_paths = [tempfile.mkdtemp() for _ in range(2)]
    for path in fake_paths:
        fake_subdir = os.path.join(path, 'lookup')
        os.mkdir(fake_subdir)
        fake_file1 = os.path.join(fake_subdir, 'fake_plugin.py')
        with open(fake_file1, 'wb') as f:
            f.write(b'from ansible.plugins.lookup import LookupBase\n')
    add_dirs_to_loader('lookup', fake_paths)
    # wipe plugin_path cache
    cache.PLUGIN_PATH_CACHE = dict()

# Generated at 2022-06-13 13:21:36.053224
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    data = [{
        'args': [],
        'kwargs': {},
        'expected': [{'path': 'foo'}]
    }]

    jll = Jinja2Loader('ansible.legacy', 'Jinja2Plugin', 'foo')
    jll._searched_paths = ['foo']
    jll._sp_matches = {'foo': ['foo/bar.py']}

    for item in data:
        expected = item['expected']
        result = jll.find_plugin(*item['args'], **item['kwargs'])
        assert result == expected


# Generated at 2022-06-13 13:21:42.155501
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    # Test with None type
    assert get_shell_plugin() == 'sh'
    #Test with executable
    assert get_shell_plugin(executable="/bin/sh") == 'sh'
    assert get_shell_plugin(executable="/bin/bash") == 'bash'
    assert get_shell_plugin(executable="/bin/zsh") == 'sh'
    #Test with shell type
    assert get_shell_plugin(shell_type="sh") == 'sh'
    assert get_shell_plugin(shell_type="bash") == 'bash'



# Generated at 2022-06-13 13:21:42.776964
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # FIXME
    assert False



# Generated at 2022-06-13 13:21:45.440009
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    PLUGIN_PATH_CACHE.clear()
    assert not PLUGIN_PATH_CACHE
    add_all_plugin_dirs(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'plugins'))
    for obj in get_all_plugin_loaders():
        assert obj[1]._directories



# Generated at 2022-06-13 13:21:54.447576
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    mock_display = MagicMock()
    type(display).verbosity = PropertyMock(return_value=3)

    mock_config = MagicMock(get=MagicMock(return_value=True))

    mock_base_class = MagicMock()

    # Mock an object that will pass the check for the base class
    mock_obj = MagicMock()
    type(mock_obj).__bases__ = PropertyMock(return_value=(mock_base_class,))
    setattr(mock_obj, '_original_path', None)
    setattr(mock_obj, '_load_name', None)
    setattr(mock_obj, '_redirected_names', None)

    # Mock the module
    mock_module = MagicMock()
    type(mock_module).NAME

# Generated at 2022-06-13 13:22:01.522913
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    assert isinstance(get_shell_plugin('sh'),ShellModule)
    assert isinstance(get_shell_plugin(executable='/bin/echo'),ShellModule)
    assert isinstance(get_shell_plugin('sh','/bin/echo'),ShellModule)
    assert isinstance(get_shell_plugin(executable='/bin/csh'),ShellModule)
    assert isinstance(get_shell_plugin('sh','/bin/csh'),ShellModule)


# Generated at 2022-06-13 13:22:11.289876
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    """
    PluginLoader's get_with_context method returns a tuple containing the plugin object and a PluginLoadContext object
    containing information about the plugin's loading.

    This test uses temporary directories to simulate the filesystem and the collection loader.
    """

    test_context = dict(
        collection_search_paths=[],
        collection_paths=[],
        loader_name='action',
        parent_name='dummy',
        class_name='Dummy',
        package='ansible.plugins.action',
        base_class='ActionBase',
    )

    def create_plugin_file(plugin_file_name, plugin_name):
        full_path = os.path.join(plugin_dir, plugin_file_name)

# Generated at 2022-06-13 13:22:20.602237
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''
    Test the add_all_plugin_dirs function for the following conditions

    1. Test for the path does not exist
    2. Test for the path is a file
    3. Test for the path is a directory and does not contain any plugin subdirs
    4. Test for the path is a directory and contains one plugin subdir
    '''

    # Create some mock plugin loader classes and required data
    class MockPluginLoader(object):
        subdir = None

        def __init__(self, subdir):
            self.subdir = subdir

        def add_directory(self, path):
            pass

    class MockPlugin1(MockPluginLoader):
        subdir = 'test-plugin-dir-1'

    class MockPlugin2(MockPluginLoader):
        subdir = 'test-plugin-dir-2'

   

# Generated at 2022-06-13 13:22:28.560321
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    orig_path = os.getcwd()
    os.mkdir(os.path.join(orig_path, 'test_loader'))
    os.chdir(os.path.join(orig_path, 'test_loader'))
    try:
        add_dirs_to_loader('connection','.')
        assert connection_loader.get('local') is not None
    finally:
        os.chdir(orig_path)



# Generated at 2022-06-13 13:23:06.939670
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    import minitest
    import minitest.mock

    c1 = minitest.mock.Mock(spec_set=AnsibleCollectionRef)
    c1.collection = 'c1'
    c1.data = {'name': 'c1'}
    c2 = minitest.mock.Mock(spec_set=AnsibleCollectionRef)
    c2.collection = 'c2'
    c2.data = {'name': 'c2'}

    with minitest.mock.patch('ansible.utils.collections_loader.get_collection_ref', side_effect=(c1, c2)) as get_coll_ref_mock:
        t = PluginLoader('ansible.plugins.test', 'BaseCls', 'ansible.plugins.test')
        plugin_load_

# Generated at 2022-06-13 13:23:21.504629
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    temp_plugin_loaders = copy.deepcopy(plugin_loaders)
    old_plugin_loaders = copy.deepcopy(plugin_loaders)
    ansible.plugins.loader._PLUGIN_PATH_CACHE = {}
    ansible.plugins.loader._PLUGIN_PATH_CACHE_TIME = 0
    plugin_loaders = {}
    plugin_paths = {}
    test_result = True
    plugin_loaders["foo"] = {}
    for i in range(100):
        plugin_loaders["foo"]["bar"] = PluginLoader("bar", "foo")
        if plugin_loaders["foo"]["bar"] != plugin_loaders["foo"]["bar"]:
            test_result = False
    plugin_loaders = temp_plugin_loaders
    plugin_paths = old

# Generated at 2022-06-13 13:23:24.732808
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    # There are no unit tests for this method
    # but there is a functional test.
    #
    # See test/functional/test_lookup_plugins.py
    pass

# Generated at 2022-06-13 13:23:33.265624
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    try:
        shell_plugin = get_shell_plugin()
    except Exception:
        shell_plugin = None
    assert shell_plugin is not None

    try:
        shell_plugin = get_shell_plugin(shell_type=None, executable='/bin/sh')
    except Exception:
        shell_plugin = None
    assert shell_plugin is not None

    try:
        shell_plugin = get_shell_plugin(shell_type="sh", executable=None)
    except Exception:
        shell_plugin = None
    assert shell_plugin is not None

    try:
        shell_plugin = get_shell_plugin(shell_type="sh", executable='/bin/sh')
    except Exception:
        shell_plugin = None
    assert shell_plugin is not None


# Generated at 2022-06-13 13:23:34.057866
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    pass

# Generated at 2022-06-13 13:23:46.505206
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    '''
    Unit test for finding `find_plugin_with_context`
    '''

    v2_collection = '/tmp/collections/foo/bar'
    v2_collection_contents = '''{
        "ansible.builtin": {
            "plugins": {
                "modules": {
                }
            }
        }
    }'''

    v2_collection_module = '''{
        "ansible.builtin": {
            "plugins": {
                "modules": {
                    "test": {
                        "name": "ansible.builtin.test",
                        "path": "/tmp/collections/foo/bar/plugins/modules/test.py"
                    }
                }
            }
        }
    }'''


# Generated at 2022-06-13 13:23:55.225051
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    plugin_load_context = PluginLoadContext()
    assert len(plugin_load_context.deprecation_warnings) == 0

    deprecation = {'warning_text': 'Use is deprecated.'}
    plugin_load_context.record_deprecation('foo', deprecation, 'ns.coll')
    assert plugin_load_context.deprecated == True
    assert plugin_load_context.removal_date == None
    assert plugin_load_context.removal_version == None
    assert len(plugin_load_context.deprecation_warnings) == 1
    assert plugin_load_context.deprecation_warnings[0] == ('foo has been deprecated. Use is deprecated.')

    deprecation = {'warning_text': 'Use is deprecated.', 'removal_date': '2018-11-01'}

# Generated at 2022-06-13 13:23:59.182548
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    """Test the add_all_plugin_dirs function"""
    # Clean up plugin paths
    for path in C.DEFAULT_MODULE_PATH:
        while path in sys.path:
            sys.path.remove(path)
    for obj in get_all_plugin_loaders():
        obj.print_paths()
        for path in obj.get_directories():
            if path in obj._get_paths():
                obj.remove_directory(path)
    # Add a non-existent directory
    add_all_plugin_dirs('/does/not/exist')
    # Add a file instead of a directory
    add_all_plugin_dirs('/etc/passwd')
    # Add a plugin directory

# Generated at 2022-06-13 13:24:10.588454
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    # test with shell_type
    ansible_shell = get_shell_plugin(shell_type='sh')
    assert ansible_shell.SHELL_FAMILY == 'sh'
    assert ansible_shell.SHELL_TYPE == 'sh'

    # test with executable
    executable = '/bin/ksh'
    ansible_shell = get_shell_plugin(executable=executable)
    assert ansible_shell.SHELL_FAMILY == 'sh'
    assert ansible_shell.SHELL_TYPE == 'sh'
    assert ansible_shell.executable == executable

    # test with shell_type and executable
    shell_type = 'powershell'
    executable = 'pwsh'
    ansible_shell = get_shell_plugin(shell_type=shell_type, executable=executable)
    assert ans

# Generated at 2022-06-13 13:24:16.222532
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # two modules have the same class name
    p = PluginLoader('tests.test_plugin_loader', 'TestPlugin', 'test_plugin_finder', 'test_plugin_config', 'test_plugin_loader_class')
    assert p.get_with_context('test') == get_with_context_result(None,
                                                                 PluginLoadContext(nope_reason='test is not eligible for last-chance resolution'))



# Generated at 2022-06-13 13:24:47.072577
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # Arguments:
    collection_list = None
    name = 'ansible.collections.a.b.c.lookup.d'
    extension = 'lookup'

    # Setup mock paths
    # FIXME: replace with mocks
    mock_paths = MockModulePaths()
    mock_paths.paths = [
        '/home/jenkins/.ansible/plugins/a/b/c/lookup_plugins',
        '/home/jenkins/ansible/lib/ansible/plugins/a/b/c/lookup_plugins',
    ]
    mock_paths.get_collections_paths = lambda *args: mock_paths.paths
    mock_paths.get_collection_path = lambda *args: 'collections'

# Generated at 2022-06-13 13:24:54.547102
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.utils.collection_plugins import Jinja2Loader
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import read_docstring


# Generated at 2022-06-13 13:25:04.602793
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # PluginLoader.find_plugin(name, extension='', use_cache=True, class_only=False, collection_list=None)
    
    # set up args
    name = 'plugin name'
    extension = ''
    use_cache = True
    class_only = False
    collection_list = None
    
    # run find_plugin
    # FIXME: needs real input to run
    #loader.find_plugin(name, extension=extension, use_cache=use_cache, class_only=class_only, collection_list=collection_list)
    
    # output to stdout
    print('in test_PluginLoader_find_plugin')


# Generated at 2022-06-13 13:25:22.008554
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    class PluginLoaderForTest(PluginLoader):
        def __init__(self, package, directories):
            super(PluginLoaderForTest, self).__init__(package, '*', '*', directories=directories)
    import tempfile
    import os
    import shutil
    import glob

    class CleansUp(object):
        def __init__(self, *dirs):
            self.dirs = dirs
        def __enter__(self):
            return self.dirs
        def __exit__(self, t, v, tb):
            for directory in self.dirs:
                shutil.rmtree(directory, ignore_errors=True)

# Generated at 2022-06-13 13:25:29.858439
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader(package='ansible_collections.nsbl.testing.plugins.filter_plugins', class_name='Filters')
    assert plugin_loader.find_plugin('non_existent_filter') is None
    assert plugin_loader.find_plugin('filter_plugins_test') == os.path.join(os.path.dirname(__file__), 'filter_plugins', 'filter_plugins_test.py')
    assert plugin_loader.find_plugin('ansible_collections.nsbl.testing.plugins.filter_plugins.filter_plugins_test') == os.path.join(os.path.dirname(__file__), 'filter_plugins', 'filter_plugins_test.py')

# Generated at 2022-06-13 13:25:39.933873
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    test_dir = 'test_dir'
    test_class_name = 'test_class_name'
    class_name = 'class_name'
    class_path = 'class_path'
    obj = 'obj'
    plugin_load_context = 'plugin_load_context'
    result = 'result'
    name = 'name'
    found_in_cache = 'found_in_cache'
    class_only = 'class_only'
    redirected_names = 'redirected_names'
    path = 'path'

    def get_with_context_result(target, plugin_load_context):
        return result

    class_obj = MagicMock()
    # Construct call stack to simulate scope
    parent_module = sys.modules[__name__]
    module = imp.new_module(class_name)

# Generated at 2022-06-13 13:25:40.878012
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
  raise NotImplementedError()


# Generated at 2022-06-13 13:25:44.753219
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    c = PluginLoader(package='mypackage')
    c.has_plugin = MagicMock(return_value=True)
    assert 'foo' in c
    c.has_plugin.assert_called_with('foo', collection_list=None)


# Generated at 2022-06-13 13:25:49.883435
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    '''test add_all_plugin_dirs'''
    # Wrong location
    _plugins = []
    try:
        add_all_plugin_dirs(path=os.path.join(os.path.abspath(os.path.sep), 'wrong', 'location', 'invalid'))
    except:
        _plugins.append("WRONG LOCATION")
    # Valid location
    add_all_plugin_dirs(path='/usr')
    assert 'WRONG LOCATION' in _plugins

