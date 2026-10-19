

# Generated at 2022-06-13 13:22:55.031146
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    path = '/ansible/test'
    target = 'target'
    instance = PluginLoader(path, 'ansible.test', 'TestPlugin', require_fqcr=True)
    target_resolution_info = ResolutionInfo(target, path, True)
    expected_resolution_info = ResolutionInfo(target, path, True)
    expected_resolution_info.candidates = [target_resolution_info]
    actual_resolution_info = instance.find_plugin_with_context(target)
    assert actual_resolution_info.plugin_resolved_name == expected_resolution_info.plugin_resolved_name
    assert actual_resolution_info.candidates == expected_resolution_info.candidates
    assert actual_resolution_info.resolved == expected_resolution_info.resolved
    assert actual_resolution_info.reason == expected_resolution_info

# Generated at 2022-06-13 13:23:04.664761
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    PLUGIN_PATH = ['/Users/patrickdebois/projects/ansible/lib/ansible/plugins/cache']
    # test plugin is of class PluginLoader
    # plugin name is defined in class PluginLoader at initialization
    name = 'memcache'
    plugin_name = 'memcache'
    collection_list = None
    plugin_load_context = None
    path = '/Users/patrickdebois/projects/ansible/lib/ansible/plugins/cache/memcache.py'

    # test plugin is of class PluginLoader
    plugin = PluginLoader(name, subdir='cache')

    # test plugin is of class PluginLoader
    # test plugin is of class PluginLoader
    # test plugin is of class PluginLoader
    # test plugin is of class PluginLoader
    # test plugin is of class PluginLoader
    # test plugin is of class Plugin

# Generated at 2022-06-13 13:23:12.474788
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    old_path = sys.path
    try:
        sys.path.append('/tmp/foo')
        old_dirs = set()
        for name, obj in get_all_plugin_loaders():
            old_dirs.update(set(obj.directories))
            obj.directories = []
        add_all_plugin_dirs(os.path.join('/tmp', 'foo'))
        for name, obj in get_all_plugin_loaders():
            new_dirs = set(obj.directories)
            assert new_dirs.difference(old_dirs) == new_dirs
            obj.directories = []
    finally:
        sys.path = old_path



# Generated at 2022-06-13 13:23:25.923203
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    loader = get_all_plugin_loaders()
    assert len(loader) >= 2
    assert ('callback_loader', callback_loader) in loader
    assert ('connection_loader', connection_loader) in loader
    assert ('lookup_loader', lookup_loader) in loader
    assert ('shell_loader', shell_loader) in loader
    assert ('module_loader', module_loader) in loader
    assert ('filter_loader', filter_loader) in loader
    assert ('test_loader', test_loader) in loader
    assert ('vars_loader', vars_loader) in loader
    assert ('action_loader', action_loader) in loader
    assert ('strategy_loader', strategy_loader) in loader
    assert ('cache_loader', cache_loader) in loader
    assert ('doc_fragment_loader', doc_fragment_loader)

# Generated at 2022-06-13 13:23:33.688227
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():

    from types import ModuleType
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars

    # TODO: move to plugin_loader test module
    class TestHost(Host):
        def __init__(self, *args, **kwargs):
            super(TestHost, self).__init__(*args, **kwargs)
            self._variable_manager = HostVars()

    # TODO: move to plugin_loader test module
    class TestModule(ModuleType):
        def __init__(self):
            self.FILTERS = {}

    # TODO: move to plugin_loader test module

# Generated at 2022-06-13 13:23:46.342148
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    global _LOCAL_PATH_CACHE

    directories = [['ansible', 'plugins', 'action', 'test'], ['ansible', 'plugins', 'action', 'test']]
    directories.append(['lib', 'ansible', 'plugins', 'action', 'test'])
    for d in directories:
        directory = os.path.join(*d)
        if not os.path.exists(directory):
            os.makedirs(directory)
            tempdir = True
        else:
            tempdir = False

        with open(os.path.join(directory, '__init__.py'), 'wb') as f:
            f.write(b'#')


# Generated at 2022-06-13 13:23:51.378015
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    class_name = 'test_class_name'
    package = 'test_package'
    config_manager = object()
    plugin_loader = PluginLoader(class_name, package, config_manager)
    plugin_loader.all(path_only=False, class_only=False)

# Generated at 2022-06-13 13:23:52.010186
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    assert(True)



# Generated at 2022-06-13 13:24:01.847301
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    # reload the module to ensure a clean env
    importlib.reload(sys.modules[__name__])
    from ansible.utils.path import unfrackpath

    ############################################################################
    # setup
    ############################################################################
    # set up test directories
    test_dir = os.path.join(os.path.dirname(__file__), 'test_PluginLoader_directory_lists')
    # test files
    test_files = ['a.py', 'b.py', 'c.txt', 'd.py']
    # create local test directories

    for file in test_files:
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, file), 'w'):
            # touch the files
            pass

    # test plugin loader config

# Generated at 2022-06-13 13:24:13.139085
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert isinstance(add_dirs_to_loader(which_loader='action',
                                         paths=C.DEFAULT_ACTION_PLUGIN_PATH.split(os.pathsep)), object)
    assert isinstance(add_dirs_to_loader(which_loader='become',
                                         paths=C.DEFAULT_BECOME_PLUGIN_PATH.split(os.pathsep)), object)
    assert isinstance(add_dirs_to_loader(which_loader='cache',
                                         paths=C.DEFAULT_CACHE_PLUGIN_PATH.split(os.pathsep)), object)