

# Generated at 2022-06-13 13:18:16.303765
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader(
        'ansible.plugins.action', 'ActionModule',
        C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins', required_base_class='ActionBase')
    plugin_load_context = plugin_loader.find_plugin_with_context('copy', class_only=False)
    assert isinstance(plugin_load_context, PluginLoadContext)
    assert plugin_load_context.resolved and plugin_load_context.plugin_resolved_path and os.path.basename(plugin_load_context.plugin_resolved_path) == 'copy.py'
    assert plugin_load_context.redirect_list == []

# Generated at 2022-06-13 13:18:20.022053
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    path = 'unittest/example_data/plugins'
    add_dirs_to_loader('lookup', [path])
    assert getattr(sys.modules[__name__], 'lookup_loader').get('basic', prevent_duplicates=False)



# Generated at 2022-06-13 13:18:27.271562
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = '/var/lib/ansible/plugins' # fake path
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
            if os.path.isdir(plugin_path):
                obj.add_directory(to_text(plugin_path))



# Generated at 2022-06-13 13:18:36.494912
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    def test_data():
        
        # fmt: off

        # inputs
        name = None
        suffix = None
        path = None
        indirect = False
        collection_list = None
        
        # expected output
        expected_plugin_load_context = None
        
        # fmt: on

# Generated at 2022-06-13 13:18:46.915172
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # fake collection loader
    class FakeCollectionLoader:
        def get_collection_info(self, collection_name, ignore_errors=False):
            if collection_name == 'fake.collection':
                return AnsibleCollectionRef('fake.collection', '1.1.1', path='/fake/path')
            elif collection_name == 'other.collection':
                return AnsibleCollectionRef('other.collection', '0.3.0', path='/other/path')

    # fake collection loader factory
    class FakeCollectionLoaderFactory:
        def __init__(self):
            self.collection_loaders = {}

        def get_loader(self, collection_name, ignore_errors=False):
            if collection_name not in self.collection_loaders:
                self.collection_loaders[collection_name] = FakeCollectionLoader()
            return

# Generated at 2022-06-13 13:18:50.386167
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    foo, bar, foobar = 'foo', 'bar', 'foobar'
    add_all_plugin_dirs(foo)
    add_all_plugin_dirs(bar)
    add_all_plugin_dirs(foobar)
    assert foo in MODULE_CACHE


# Generated at 2022-06-13 13:19:00.270986
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.errors import AnsibleError
    from ansible.errors import AnsibleOptionsError

    for name, obj in get_all_plugin_loaders():
        obj.clear_dirs()

    test_dir = os.path.dirname(__file__)

    if os.path.exists(test_dir):
        # test normal add_all_plugin_dirs
        add_all_plugin_dirs(test_dir)
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                assert os.path.join(test_dir, obj.subdir) in obj._directories, "add_all_plugin_dirs failed to add normal plugin dirs"

        # test add_all_plugin_dirs for invalid path

# Generated at 2022-06-13 13:19:11.722584
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    '''
    Test case for add_dirs_to_loader
    '''
    all_facts_loader = getattr(sys.modules[__name__], 'all_facts_loader')
    assert 'lookup_loader' in get_all_plugin_loaders()

    all_facts_loader.add_directory(os.path.join(C.DEFAULT_LOCAL_TMP, 'test_collection'))
    # Will create a plugin
    add_dirs_to_loader('lookup', [C.DEFAULT_LOCAL_TMP])
    assert all_facts_loader.has_plugin('plugin')

    # Will remove a plugin
    add_dirs_to_loader('lookup', [C.DEFAULT_LOCAL_TMP])
    assert not all_facts_loader.has_plugin('plugin')




# Generated at 2022-06-13 13:19:19.655836
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Note:
    instances = {}
    collections_loader = C.AnsibleLoader(
        C.collection_loader,
        'ansible_collections_path',
        'ansible.plugins.action'
    )

    # Expected:
    #     It returns the path instead of a boolean value like it used to.
    #     It uses the alias_map to find the plugin if a direct match doesn't exist.
    instances[0] = PluginLoader(
        'ansible.plugins.action',
        'ActionModule',
        collections_loader=collections_loader
    )
    instances[0].add_directory(os.path.join('test', 'testdata'))
    plugin_load_context = instances[0].find_plugin_with_context('lolcat')

# Generated at 2022-06-13 13:19:33.702308
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    # Make sure the directories are added to the loader when the loader exists
    test_loader = PluginLoader('test_new_loader', '', '_', '_', '_finder')
    # Save and reset
    saved_loaders = sys.modules[__name__].__dict__.copy()
    sys.modules[__name__].__dict__.clear()

    # Create a new loader and add it to sys.modules
    test_loader = PluginLoader('test_new_loader', '', '_', '_', '_finder')
    sys.modules[__name__].test_new_loader_loader = test_loader

    # Test the function
    add_dirs_to_loader('test_new_loader',
                       paths=['fake_path_1',
                       'fake_path_2'])


# Generated at 2022-06-13 13:19:58.726051
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = None
    try:
        plugin_loader = PluginLoader('', 'some_class', '')
    except Exception as e:
        print('Exception: ' + str(e))


# Generated at 2022-06-13 13:20:05.914695
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.utils.collection_loader import _get_collection_metadata
    import jinja2
    from ansible.utils.collection_loader import _DEFAULT_METADATA_CACHE_TIMEOUT
    import time
    import os
    import random
    import string
    import tempfile
    import shutil
    collection_namespace = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    collection_dir = tempfile.mkdtemp()
    def cleanup():
        shutil.rmtree(collection_dir, ignore_errors=True)
    collection_name = 'nginx'

# Generated at 2022-06-13 13:20:16.778034
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    ''' test add_all_plugin_dirs '''
    path = '/tmp/doesnotexist'
    b_path = os.path.expanduser(to_bytes(path, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                plugin_path = os.path.join(b_path, to_bytes(obj.subdir))
                if os.path.isdir(plugin_path):
                    obj.add_directory(to_text(plugin_path))
    else:
        display.warning("Ignoring invalid path provided to plugin path: '%s' is not a directory" % to_text(path))



# Generated at 2022-06-13 13:20:25.178033
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    pl = PluginLoader(package='test_utils', base_class='test_plugins/test_base.py')

    assert 'test_plugins/test_discovery/good.py' in pl
    assert 'test_plugins/test_discovery/bad.py' not in pl
    assert 'test_plugins/test_discovery/missing_class.py' not in pl
    assert 'test_plugins/test_discovery/bad_base.py' not in pl
    assert 'test_plugins/test_discovery/good_with_config.py' in pl
    assert 'test_plugins/test_discovery/parent.py' not in pl
    assert 'test_plugins/test_discovery/child.py' in pl
    assert 'test_plugins/test_discovery/bad_parent.py' not in pl

# Generated at 2022-06-13 13:20:37.107787
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    module_loader = PluginLoader('ExamModule', 'exam_module', 'tests.integration.test_module_utils.exam_module', 'exam_module', 'exam_module')
    module_loader.add_directory(DATA_PATH)
    result = module_loader.get_with_context('exam_module')
    assert result.plugin_load_context.plugin_search_path == [u'exam_module']
    assert result.object.__name__ == 'ExamModule'
    assert result.object.__doc__ == 'This is an exam module'


# Generated at 2022-06-13 13:20:46.386320
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    loader = PluginLoader('action_plugins')

    # Case 1: File exists in specified path
    result = loader.find_plugin_with_context('ping', './my_ansible_library/action_plugins/ping')
    assert result.resolved
    assert result.plugin_resolved_name == 'ping'
    assert result.plugin_resolved_path == './my_ansible_library/action_plugins/ping'
    assert result.plugin_load_path == './my_ansible_library/action_plugins'

    # Case 2: File exists in collection with no path specified
    result = loader.find_plugin_with_context('mycollection.ping', './my_ansible_library/action_plugins')
    assert result.resolved
    assert result.plugin_resolved_name == 'mycollection.ping'

# Generated at 2022-06-13 13:21:01.026405
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    #
    # get_with_context(name, *args, **kwargs) should return the plugin context and plugin object
    #
    # 1. Connect to the database
    db=database.Database()
    db.connect()
    db.execute('delete from plugin where id>0')
    db.execute('delete from plugin_path where id>0')
    db.execute('delete from plugin_collection where id>0')
    db.execute('delete from plugin_collection_path where id>0')
    db.execute('delete from plugin_class where id>0')

    # 2. Check if database is empty
    result=db.execute('select * from plugin')
    assert(len(result)==0)

    # 3. Insert 2 collection and 5 plugins

# Generated at 2022-06-13 13:21:09.257385
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():

    # Initialize a global plugin loader for Jinja2 filters
    PLUGIN_PATH = os.path.join(os.path.dirname(__file__), 'filter_loader')
    find_plugin = Jinja2Loader(
        package='ansible.plugins.filter',
        config=dict(),
        subdir='filter_plugins',
        path_list=[PLUGIN_PATH],
    ).find_plugin

    # Test the Jinja2 filter plugin loader
    #
    # The function find_plugin() receives the name of a plugin, and searches
    # a list of paths to find a file that contains the given plugin.
    #
    # The test creates a plugin loader with a list of existing paths in which
    # the plugins are located.  The test passes the name of a plugin contained
    # in one of the path items.  The test checks

# Generated at 2022-06-13 13:21:19.343657
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    p = PluginLoadContext()
    p.record_deprecation(name='test_dep', deprecation={'warning_text':'test_text'}, collection_name='test_coll')
    assert p.deprecated == True
    assert p.removal_date == None
    assert p.removal_version == None
    assert p.deprecation_warnings == ['test_dep has been deprecated. test_text']

    p.record_deprecation(name='test_dep_date', deprecation={'warning_text':'test_date', 'removal_date':'1.1'}, collection_name='test_coll')
    assert p.removal_date == '1.1'


# Generated at 2022-06-13 13:21:29.556382
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    pr = PluginLoader("v2_action_plugin", "ActionModule", None, "action_plugins")
    result = pr.get_with_context("system", class_only=False, collection_list=None)
    assert result.object
    assert isinstance(result.object, AnsibleAction)
    assert result.object.__class__.__name__ == "Shell"
    assert result.resolved
    assert result.plugin_resolved_name == "system"
    assert result.plugin_resolved_path == "/home/vagrant/venvs/ansible-automation-sdk-venv/local/lib/python2.7/site-packages/ansible/plugins/action/system.py"
    assert result.collection_resolved
    assert result.collection_resolved_name == "ansible.builtin.system"


# Generated at 2022-06-13 13:21:57.019834
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    try:
        importlib.util.find_spec('test_module_utils.ansible_test')
    except ImportError:
        os.symlink(os.path.join(os.path.dirname(__file__), 'module_utils', 'ansible_test'), 'test_module_utils.ansible_test')
    add_all_plugin_dirs(os.getcwd())
    try:
        from test_module_utils.ansible_test.plugins import callback
        assert True
    except ImportError:
        assert False
    else:
        assert False
    finally:
        for obj in get_all_plugin_loaders():
            obj._directories[:] = []
        os.unlink('test_module_utils.ansible_test')

# TODO: path filtering should be done here.


# Generated at 2022-06-13 13:22:03.074570
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method PluginLoader.__contains__
    '''
    plugin_loader = PluginLoader(
        'ansible.test_plugins',
        'TestPlugins',
        'test_plugin',
        C.CACHE_PLUGIN_FILENAMES
    )
    output = plugin_loader.__contains__('test_plugin')
    assert isinstance(output, bool)
    assert output == True


# Generated at 2022-06-13 13:22:12.371580
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    '''
    Test if find_plugin method of class PluginLoader works as expected
    '''
    # Initialization
    # --------------
    plugin_loader = PluginLoader(
        package='ansible.plugins',
        class_name='ModuleUtil'
    )
    name = 'action_adds'
    candidate_fqcr = 'ansible.module_utils.action_adds'
    suffix = '.py'
    # AnsibleCollectionRef is not mocked here because it is not needed

# Generated at 2022-06-13 13:22:21.463298
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    l_filter = PluginLoader(
        'FilterModule',
        'ansible.plugins.filter',
        C.DEFAULT_FILTER_PLUGIN_PATH,
    )
    l_action = PluginLoader(
        'ActionModule',
        'ansible.plugins.action',
        C.DEFAULT_ACTION_PLUGIN_PATH,
    )
    l_callback = PluginLoader(
        'CallbackModule',
        'ansible.plugins.callback',
        C.DEFAULT_CALLBACK_PLUGIN_PATH,
    )
    l_connection = PluginLoader(
        'ConnectionModule',
        'ansible.plugins.connection',
        C.DEFAULT_CONNECTION_PLUGIN_PATH,
    )

# Generated at 2022-06-13 13:22:31.412623
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    mock_name = 'mock_name'
    pl = PluginLoader(package='mock')
    pl.aliases = {mock_name: 'mock_name'}
    pl.find_plugin = MagicMock()
    pl.find_plugin.return_value.plugin_resolved_path = '/tmp/mock_path'
    pl.has_plugin(mock_name)
    pl.find_plugin.assert_called_with(name=mock_name)

# Generated at 2022-06-13 13:22:39.898290
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    for find_plugin_item in find_plugin_tests:
        loader = PluginLoader(find_plugin_item.get('package'))
        package = find_plugin_item.get('package')
        name = find_plugin_item.get('name')
        suffix = find_plugin_item.get('suffix')
        paths = find_plugin_item.get('paths')
        fqcr = find_plugin_item.get('fqcr', None)
        path = find_plugin_item.get('path', None)
        if fqcr:
            loader.add_collection_paths(paths)
        loader.collection_search_paths = paths
        found_path = loader.find_plugin(name, suffix=suffix, fqcr=fqcr)

# Generated at 2022-06-13 13:22:40.845913
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    pass

# Generated at 2022-06-13 13:22:47.423218
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    name = 'shell'
    suffix = 'action'
    plugin_loader = PluginLoader('action', 'ActionModule')
    plugin_loader.package = 'ansible.plugins.action'
    plugin_loader.subdir = 'actions'
    plugin_loader._search_paths = ['/home/runner/work/ansible/ansible/lib/ansible/plugins/action']
    plugin_loader._display.verbosity = 5

    plugin_load_context = plugin_loader._find_fq_plugin(name, suffix, plugin_load_context=None)

    assert plugin_load_context.current_plugin_path == '/home/runner/work/ansible/ansible/lib/ansible/plugins/action/shell.py'

# Generated at 2022-06-13 13:22:53.721161
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    assert not os.path.isdir('test_add_all_plugin_dirs')
    try:
        add_all_plugin_dirs('test_add_all_plugin_dirs')
    finally:
        assert not os.path.isdir('test_add_all_plugin_dirs')
    os.mkdir('test_add_all_plugin_dirs')
    assert os.path.isdir('test_add_all_plugin_dirs')
    os.rmdir('test_add_all_plugin_dirs')
    assert not os.path.isdir('test_add_all_plugin_dirs')



# Generated at 2022-06-13 13:22:59.002745
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Test to add a part of plugin directory
    plugin_dir = os.path.realpath(__file__)
    plugin_dir = os.path.dirname(plugin_dir)
    plugin_dir = os.path.abspath(os.path.join(plugin_dir, os.pardir))
    plugin_dir = os.path.abspath(os.path.join(plugin_dir, os.pardir))
    add_all_plugin_dirs(plugin_dir)
    for name, obj in get_all_plugin_loaders():
        assert plugin_dir in obj._directories



# Generated at 2022-06-13 13:24:54.209937
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    plugin_loader = PluginLoader(None, 'test', '', None, None)
    assert list(plugin_loader.all()) == []


# Generated at 2022-06-13 13:25:04.000064
# Unit test for function get_shell_plugin
def test_get_shell_plugin():

    shell_type = 'csh'
    shell = get_shell_plugin(shell_type)
    assert shell.SHELL_FAMILY == shell_type

    shell_type = 'sh'
    executable = '/bin/ksh'
    shell = get_shell_plugin(shell_type, executable)
    assert shell.SHELL_FAMILY == shell_type
    assert shell.executable == executable

    shell_type = 'sh'
    executable = '/bin/csh'
    shell = get_shell_plugin(shell_type, executable)
    assert shell.SHELL_FAMILY == 'csh'
    assert shell.executable == executable



# Generated at 2022-06-13 13:25:21.317259
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    plugin_loader = PluginLoader(
        class_name='_test_class',
        package='thepackage',
        config=None,
        subdir='the_subdir',
        aliases={},
        required_base_class='_required_base_class',
        imp=None,
        verbose=True
    )
    def mock_glob_glob(path):
        if path.endswith('/the_subdir/*.py'):
            return [
                'the_subdir/first.py',
                'the_subdir/second.py',
                'the_subdir/third.py',
                'the_subdir/__init__.py',
                'the_subdir/base.py',
            ]
        return []

# Generated at 2022-06-13 13:25:25.116300
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    for _, obj in get_all_plugin_loaders():
        obj.directories = []
    test_path = "./"
    add_all_plugin_dirs(test_path)
    for _, obj in get_all_plugin_loaders():
        assert obj.directories == [test_path + obj.subdir]


# Generated at 2022-06-13 13:25:32.240475
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    from ansible.module_utils._text import to_text
    cls = PluginLoader('ansible.plugins.filter', 'FilterModule', C.DEFAULT_FILTERS_PATH, 'filter_plugins')
    cls.add_directory(C.DEFAULT_FILTERS_PATH, with_subdir=True)

    assert isinstance(cls.all(), types.GeneratorType)
    for i in cls.all():
        assert isinstance(i, FilterModule)

    result = list(cls.all(path_only=True))
    assert isinstance(result[0], str)

    assert isinstance(cls.all(class_only=True), types.GeneratorType)
    for i in cls.all(class_only=True):
        assert isinstance(i, type)

# Generated at 2022-06-13 13:25:41.817577
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    def test(attribute, module_name, path, class_name, base_class, package, module_prefix, has_value=None, result=None, collection_list=None):
        info = mocker.Mock()
        info.attribute = attribute
        info.module_name = module_name
        info.path = path
        info.class_name = class_name
        info.base_class = base_class
        info.package = package
        info.module_prefix = module_prefix
        info.has_value = has_value
        info.result = result
        if collection_list:
            collection = mocker.Mock()
            collection.directories = {'filter_plugins':['collection_filter_plugins_path'], 'test_plugins':['collection_test_plugins_path']}
            collection_list = [ collection ]

# Generated at 2022-06-13 13:25:44.906877
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # get all plugin dirs in old-style paths
    for name, obj in get_all_plugin_loaders():
        assert obj.old_style_loaders.get(path, None)



# Generated at 2022-06-13 13:25:50.558161
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    pl = PluginLoader(None, "ansible.plugins.action")
    pl.add_directory("/tmp")
    assert("/tmp" in pl._get_paths())
    pl.add_directory("/tmp")
    assert(pl._get_paths().count("/tmp") == 1)