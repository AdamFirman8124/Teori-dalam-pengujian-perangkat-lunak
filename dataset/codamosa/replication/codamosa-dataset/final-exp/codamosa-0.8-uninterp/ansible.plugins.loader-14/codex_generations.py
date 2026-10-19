

# Generated at 2022-06-13 13:17:04.017589
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # Make sure we have the correct values in the cached plugin_load_context
    import types
    import sys

    if sys.version_info < (3,):
        reload(sys)
        sys.setdefaultencoding('utf8')

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = mystdout = StringIO()
    sys.stderr = mystderr = StringIO()

    pl = PluginLoader('action_plugin', 'ActionModule')
    context = pl.find_plugin_with_context('ec2_vpc_subnet')

    mod = pl._module_cache[context.plugin_resolved_path]
    assert isinstance(mod, types.ModuleType)
    obj = getattr(mod, 'ActionModule')

# Generated at 2022-06-13 13:17:14.778358
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    import json

    display_info = {
        'verbosity': 3,
        'verbosity_level': 3
    }

    CONFIG = PATH_TO_CONFIG + '/ansible.cfg'
    cfg_path = os.path.expanduser(CONFIG)
    if os.path.exists(cfg_path):
        # NOTE: We could use AnsibleConfig, but it would only work for 2.4 and higher
        #       If we need 2.4+ for other features, then should switch this to use it.
        #       Also, if we have context from a plugin class, we can just use:
        #           self._config.data
        config = get_config_dict((DataLoader(), cfg_path, 'file', False))

# Generated at 2022-06-13 13:17:30.379635
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    class TestAllPluginLoader(PluginLoader):
        def __init__(self, package, subdir, base_class):
            super(TestAllPluginLoader, self).__init__(package, subdir, base_class)
        def _get_paths(self):
            return self.searchpath
        def _display_plugin_load(self, class_name, name, searched_paths, path, found_in_cache=None, class_only=None):
            # display.debug(msg)
            pass
    import os
    testset_advanced_result = False
    testset_dedupe_result = False
    testset_dedupe_result2 = False
    testset_class_only_result = False
    class TestPluginBase(object):
        def __init__(self, *args, **kwargs):
            self

# Generated at 2022-06-13 13:17:31.246823
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    # FIXME: add a test
    pass



# Generated at 2022-06-13 13:17:38.438386
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():

    paths = ['/path/to/ansible', '/other/path/to/ansible']
    for which_loader in ['connection', 'lookup', 'shell']:
        loader = getattr(sys.modules[__name__], '%s_loader' % which_loader)
        loader.add_directory.reset_mock()
        add_dirs_to_loader(which_loader, paths)
        assert loader.add_directory.call_count == 2
        for loader_args in loader.add_directory.call_args_list:
            args, kwargs = loader_args
            assert args[0] in paths
            assert kwargs.get('with_subdir', False)



# Generated at 2022-06-13 13:17:41.618720
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    p = PluginLoader('', '', '')
    data = ['/tmp', '/tmp/ansible', '/tmp/ansible/plugins']
    p.add_directory(*data)
    assert p._get_paths() == data


# Generated at 2022-06-13 13:17:53.461251
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    try:
        from ansible.errors import AnsibleError
    except ImportError:
        AnsibleError = None
    except SyntaxError:
        AnsibleError = None

    # Test jinja2loader1
    try:
        Jinja2Loader('ansible.plugins.filter.core', 'CoreFilters', 'filter_plugins').find_plugin('uniq')
        Jinja2Loader('ansible.plugins.test.core', 'CoreTests', 'test_plugins').find_plugin('number')
    except AnsibleError:
        pass

    try:
        Jinja2Loader('ansible.plugins.filter.core', 'CoreFilters', 'filter_plugins').find_plugin('nonexisting_plugin')
        raise AssertionError('AnsibleError is not raised for nonexistent plugin')
    except AnsibleError:
        pass

# Generated at 2022-06-13 13:18:00.079471
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    obj = PluginLoader(
        'ansible.plugins.connection',
        'ConnectionModule',
        'ansible.plugins.connection.ConnectionBase',
        required_base_class='ConnectionBase',
        required_base_class_signature='ConnectionBase',
        dest_list=C.DEFAULT_CONNECTION_PLUGIN_PATH,
        package='ansible.plugins.connection')
    for entry in obj.all():
        assert os.path.basename(entry).endswith('py')

# Generated at 2022-06-13 13:18:06.608763
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    get_all_plugin_loaders()
    # Add directory that does not exist.
    add_all_plugin_dirs("/tmp/does_not_exist")
    # Add directory that does exist.
    add_all_plugin_dirs(sys.path[0])
    # Add directory that does exist, but does not contain a subdir for any of the plugin_loaders.
    add_all_plugin_dirs("/etc")

# The path from which a plugin was loaded
PluginPath = namedtuple('PluginPath', ('path', 'subdir'))



# Generated at 2022-06-13 13:18:08.411690
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pass

# vim: set ts=4 sw=4 et:

# Generated at 2022-06-13 13:19:33.703921
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    try:
        assert find_plugin.__module__ == 'ansible.plugins.loader'
    except AssertionError as exc:
        raise AssertionError(exc.message + ' (in module "ansible.plugins.loader" file "ansible/plugins/loader/__init__.py")')
    ok_("find_plugin" in globals())
    assert find_plugin.__class__.__name__ == 'function'
    # TODO: Add tests
    raise NotImplementedError()

# Generated at 2022-06-13 13:19:46.601425
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    import unittest

    class TestPluginLoader(unittest.TestCase):
        def test_get_with_context(self):
            import os

            import ansible.config.base as config_base
            from ansible.config.manager import ConfigManager
            import ansible.errors
            import ansible.plugins


# Generated at 2022-06-13 13:19:48.775268
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    PL = PluginLoader("ansible.plugins.action")
    PL.has_plugin("shell")
    PL.has_plugin("xyz")
    "shell" in PL
    "xyz" not in PL

# Generated at 2022-06-13 13:19:59.995188
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    shell = get_shell_plugin(shell_type='csh')
    assert shell._load_name == 'csh'
    assert shell.SHELL_FAMILY == 'csh'
    assert shell.__module__ == 'ansible.plugins.shell.csh'


# this is used to load plugins from the 'cache' subdir
cache_loader = PluginLoader('cache', 'CacheModule', C.CACHE_PLUGIN_FILENAME, 'cache_plugins', required_base_class='CacheModule')

callback_loader = PluginLoader('callback', 'CallbackModule', 'callback_plugins', 'callback_plugins', required_base_class='CallbackModule')

connection_loader = PluginLoader('connection', 'Connection', C.CONNECTION_PLUGIN_FILENAME, 'connection_plugins', required_base_class='Connection')


# Generated at 2022-06-13 13:20:02.708280
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    '''
    Unit test for method `PluginLoader.__setstate__`
    '''
    obj = PluginLoader(None, None, None, None)
    obj.__setstate__(None)


# Generated at 2022-06-13 13:20:07.259506
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import ansible.utils.plugin_docs as plugin_docs
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.exit_json = exit_json
    p = PluginLoader('module_utils', '_AnsibleModule')
    result = p.all()
    assert isinstance(result, types.GeneratorType)
    assert next(result).__class__.__name__ == '_AnsibleModule'


# Generated at 2022-06-13 13:20:11.133261
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    plugins = Jinja2Loader(
        'ansible.plugins.filter.core',
        'FilterModule',
        'ansible.plugins.filter',
    )
    plugins.all('hostname', 'localhost')
    plugins.get('localhost', 'hostname')


# Generated at 2022-06-13 13:20:15.686271
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    my_loader = PluginLoader('ansible.plugins', 'Base')
    plugin_list = [plugin for plugin in my_loader.all()]

    assert(len(plugin_list) > 0)
    assert(type(plugin_list[0]) == Base)


# Generated at 2022-06-13 13:20:17.409570
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    obj = PluginLoader('ansible.plugins.module_utils', 'ModuleUtils', '_', 'module_utils.py')
    assert obj.all() is not None


# Generated at 2022-06-13 13:20:26.353481
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible import constants as C
    from ansible.inventory.inventory import Inventory
    add_dirs_to_loader('filter', '/root/ansible-new/lib/ansible/plugins/filter')
    add_dirs_to_loader('action', '/root/ansible-new/lib/ansible/plugins/action')
    pass
    # add_dirs_to_loader('filter', '/root/ansible-new/lib/ansible/plugins/filter')
    # add_dirs_to_loader('action', '/root/ansible-new/lib/ansible/plugins/action')
    #

# Generated at 2022-06-13 13:21:33.937708
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # test that method all passes arguments to the plugin
    import os

    p = PluginLoader('test_plugins.test_all', 'TestPlugin', 'tests/test_plugins/test_all')
    plugin1 = list(p.all(arg='arg'))[0]
    assert plugin1.arg == 'arg'

    # test that method all passes arguments to the plugin with multiple plugins in a file
    p = PluginLoader('test_plugins.test_all', 'TestSubclassPlugin', 'tests/test_plugins/test_all')
    plugin2 = list(p.all(arg='arg'))[0]
    assert plugin2.arg == 'arg'

    # test that method all passes arguments to the plugin with multiple plugins in a file with multiple files

# Generated at 2022-06-13 13:21:43.392679
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    import os
    import shutil
    import tempfile
    import yaml
    import time
    import unittest

    # create a temporary directory to store test results
    temp_test_results_directory = tempfile.mkdtemp()

    # create a temporary directory to store test plugins
    plugins_path = os.path.join(temp_test_results_directory, 'plugins')
    os.mkdir(plugins_path)

    # create a fake plugin in the temporary directory
    fake_plugin_filename = 'fake_plugin.py'

# Generated at 2022-06-13 13:21:52.949753
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    global _PLUGIN_PATHS

# Generated at 2022-06-13 13:21:55.102415
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():

    m = MagicMock()
    j2 = Jinja2Loader(m, m, m)
    j2.get('foo')
    assert False, "TODO: Implement me!"



# Generated at 2022-06-13 13:21:55.916168
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    assert False



# Generated at 2022-06-13 13:22:07.485674
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():

    def check_1_item(item,expected_item,expected_paths):
        assert item.__class__.__name__ == expected_item
        assert item._original_path in expected_paths

    plugin_loader = PluginLoader('ansible.plugins.action', 'ActionModule')

    # test that we can get all plugins
    count = 0
    for item in plugin_loader.all():
        count += 1

    assert count >= 300

    # test that we can get all plugins of a specific base class
    count = 0
    for item in plugin_loader.all(base_class='LookupBase'):
        count += 1

    assert count >= 20

    # test that we can get all paths to plugins
    count = 0
    for item in plugin_loader.all(path_only=True):
        count += 1

    assert count

# Generated at 2022-06-13 13:22:12.525353
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    # TODO: test handling of duplicate/conflicting plugins
    # TODO: test class_only and path_only
    # TODO: test handling of missing base class
    # TODO: test find_plugin_with_context

    class StubContext(object):
        def __init__(self):
            self.nope = Mock()
            self.resolved = True
            self.plugin_resolved_name = None
            self.plugin_resolved_path = None
            self.redirect_list = []

    class StubPluginLoader(PluginLoader):
        def __init__(self, package, subdir, class_name, base_class):
            super(StubPluginLoader, self).__init__(package, subdir, class_name, base_class)


# Generated at 2022-06-13 13:22:21.633330
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    import collections
    module_fqcr_token = 'ansible.plugins.test_test_test'
    module_path = b'/home/vagrant/ansible/lib/ansible/plugins/test/test/test.py'
    module_path = to_text(module_path, errors='surrogate_or_strict')
    class_name = 'TestPlugin'
    base_class = 'BaseAnsibleModule'
    package = 'ansible.plugins.test_test'
    collection_name = 'ansible.plugins.test_test'
    collection_root = '/home/vagrant/ansible'
    collection_version = '0.0.1'
    collection_namespace = 'namespace.test'
    collection_requirements_file = None

# Generated at 2022-06-13 13:22:35.582507
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    p = PluginLoadContext()
    p.record_deprecation("daniel", {'warning_text': 'is awesome', 'removal_date': '01/01/01', 'removal_version': '2.9'}, "collection")
    assert p.removal_version == '2.9'
    p.record_deprecation("daniel", {'warning_text': 'is awesome', 'removal_date': '01/01/01', 'removal_version': '3.0'}, "collection")
    assert p.removal_date == '01/01/01'
    p.record_deprecation("daniel", {'warning_text': 'is awesome', 'removal_date': '01/01/02', 'removal_version': '3.0'}, "collection")
    assert p.removal

# Generated at 2022-06-13 13:22:36.530577
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    pass

# Generated at 2022-06-13 13:23:09.373882
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.module_utils import six
    from ansible.plugins.loader import PluginLoader

    class DummyPluginLoader(PluginLoader):
        def __init__(self, subdir, *args):
            self.subdir = subdir
            self.possible_directories = []

            if subdir == 'sub1':
                self.possible_directories = ['/tmp']
            elif subdir == 'sub2':
                self.possible_directories = []
            elif subdir == 'sub3':
                self.possible_directories = ['/tmp']

        @staticmethod
        def add_directory(directory):
            pass

    class Mock_os_path:
        def isdir(self, path):
            if path == '/tmp':
                return True
            return False


# Generated at 2022-06-13 13:23:22.455043
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    # Test with a valid string
    print('Test with a valid string')
    pl = PluginLoader()
    assert 'copy' in pl
    assert 'some_missing_plugin' not in pl
    # Test with a number
    print('Test with a number')
    assert 1 not in pl
    assert '1' not in pl
    # Test with a list
    print('Test with a list')
    assert ['copy', 'some_missing_plugin'] not in pl
    assert ['copy'] in pl
    # Test with a tuple
    print('Test with a tuple')
    assert ('copy', 'some_missing_plugin') not in pl
    assert ('copy', ) in pl

if __name__ == '__main__':
    test_PluginLoader___contains__()

# Generated at 2022-06-13 13:23:27.398273
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    test_shell_type = 'sh'
    test_executable = None
    test_shell = get_shell_plugin(shell_type=test_shell_type, executable=test_executable)
    assert type(test_shell) == type(get_shell_plugin())


# Generated at 2022-06-13 13:23:40.941772
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    def get_deprecation_warnings(collection_name, deprecation_key,
                                 deprecation_value, is_deprecated,
                                 removal_date, removal_version):
        display.verbosity = 3
        context = PluginLoadContext()
        context.record_deprecation('test_plugin',
                                   {deprecation_key: deprecation_value},
                                   collection_name)
        assert context.deprecated == is_deprecated
        assert context.removal_date == removal_date
        assert context.removal_version == removal_version
        assert context.deprecation_warnings == ['test_plugin has been deprecated.']
    # with collection

# Generated at 2022-06-13 13:23:42.763828
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    assert True


# Generated at 2022-06-13 13:23:54.737420
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Test simple load of collection plugin, main branch
    import ansible.plugins.lookup
    import ansible.plugins.action
    import ansible.plugins.cache
    import ansible.plugins.connection
    import ansible.plugins.cliconf
    import ansible.plugins.terminal
    import ansible.plugins.strategy
    import ansible.plugins.shell
    import ansible.plugins.vars
    import ansible.plugins.callback
    import ansible.plugins.survey
    import ansible.plugins.doc_fragments
    import ansible.plugins.test
    import ansible.plugins.filter
    import ansible.plugins.deprecated
    import ansible.plugins.callback.default
    import ansible.plugins.connection.local
    import ansible.plugins.cache.memory

# Generated at 2022-06-13 13:24:03.893514
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
  from ansible.plugins.loader import PluginLoader
  from types import ModuleType
  from ansible.errors import AnsibleError

  path = '/home/runner/work/ansible-base/ansible-base/test/unit/plugins/test_module_loader.py'
  name = 'test_module_loader'
  plugin_loader = PluginLoader('test_module_loader', '', '', 'loader', None, None, True)
  plugin_loader.package = "ansible.plugins.loader"
  results = plugin_loader.find_plugin(name)
  assert type(results) == ModuleType
  assert results.__name__ == 'ansible.plugins.loader.test_module_loader'
  assert results._original_path == path
  assert results._load_name == 'test_module_loader'
  assert results._redirect

# Generated at 2022-06-13 13:24:08.204921
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader(package='ansible.plugins.action',
                          config={},
                          subdir='../../action',
                          )
    # TODO: implement tests for this method
    assert False, "tests for find_plugin not implemented"


# Generated at 2022-06-13 13:24:12.005818
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    data = dict(
        name='test',
        collection_list=None
    )
    assert PluginLoader.has_plugin(data['name'], collection_list=data['collection_list']) == True


# Generated at 2022-06-13 13:24:25.082469
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():

    # Create a new context object.
    from ansible.plugins.loader import PluginLoader
    context_obj = PluginLoader()
    # TODO: Set context_obj.class_name, for example: context_obj.class_name = "class_name"
    # TODO: Set context_obj.package, for example: context_obj.package = "package"

    # Call the class method 'all' with positional arguments, for example:
    # context_obj.all(**kwargs)
    # If the method does not take positional arguments and does not return a value,
    # you can call the method directly without using an assignment statement, for example:
    # context_obj.all()
    # If the method takes positional arguments and does not return a value,
    # you can call the method without using an assignment statement, for example:
    # context_obj

# Generated at 2022-06-13 13:25:06.835775
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_dirs = [os.path.join(os.path.dirname(__file__), "../../plugins")]
    plugin_loader = PluginLoader("action_plugin", package="ansible.plugins.action",
                                 config={}, subdir=os.path.join(plugin_dirs[0], 'action'), class_name='ActionModule')

    momo_context = plugin_loader.find_plugin_with_context('momo')
    assert moment == momo_context.object, "Momo not found"

    momo_context = plugin_loader.find_plugin_with_context('Test.momo')
    assert isinstance(momo_context, FailWithResult)
    assert 'Test doesn\'t exist' in str(momo_context)

    # import collections
    # collections.create_collection('Test')
   

# Generated at 2022-06-13 13:25:22.235622
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    import copy
    plugin_loader = PluginLoader()
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../test/'))
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../test/'))
    assert os.path.join(os.path.dirname(__file__), '../../test/') in plugin_loader._get_paths()
    plugin_loader._get_paths().remove(os.path.join(os.path.dirname(__file__), '../../test/'))
    assert plugin_loader._get_paths() == []

# Generated at 2022-06-13 13:25:33.479920
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    '''
    Unit tests for the class PluginLoader
    '''
    from ansible.plugins.cache import BaseCacheModule
    from ansible.plugins.test.test_module import TestModule
    from ansible.plugins.action import ActionModule
    from ansible.plugins.connection import Connection
    from ansible.plugins.filter import FilterModule
    from ansible.plugins.inventory import BaseInventoryPlugin

    cache_plugin_loader = PluginLoader('ansible.plugins.cache', 'CacheModule', C.DEFAULT_CACHE_PLUGIN_PATH, 'cache.base', 'ansible.cache')
    test_plugin_loader = PluginLoader('ansible.plugins.test', 'TestModule', C.DEFAULT_TEST_PLUGIN_PATH, 'test.base', 'ansible.test')
    action_plugin_loader = PluginLoader

# Generated at 2022-06-13 13:25:43.086501
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    '''
    plugin_load.PluginLoader test stub.
    '''
    # From test/units/lib/ansible_test/_data/ansible/plugins/callback/test.py
    import ansible_test.callback_data.ansible.plugins.callback.test as test
    # From test/units/lib/ansible_test/_data/ansible/plugins/strategy/test.py
    import ansible_test.strategy_data.ansible.plugins.strategy.test as test
    # From test/units/lib/ansible_test/_data/ansible/plugins/action/test.py
    import ansible_test.action_data.ansible.plugins.action.test as test
    # From test/units/lib/ansible_test/_data/ansible/plugins/connection/test.py
    import ans

# Generated at 2022-06-13 13:25:44.341537
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    pass


# Generated at 2022-06-13 13:25:51.991320
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    myloader = PluginLoader('/tmp', 'mypackage','myclass')
    myloader.add_directory('/tmp/foo')
    myplugin = myloader.find_plugin('bar')

    if '/tmp/foo/bar.py' != myplugin:
        raise AssertionError
    if None != myloader.find_plugin('baz'):
        raise AssertionError
    myloader.add_directory('/tmp/bar')
    if None != myloader.find_plugin('baz'):
        raise AssertionError
    myplugin = myloader.find_plugin('bar')
    if '/tmp/foo/bar.py' != myplugin:
        raise AssertionError
    myplugin = myloader.find_plugin('qux')

# Generated at 2022-06-13 13:26:02.109369
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    '''
    Unit test for method get_with_context of class PluginLoader
    '''
    
    import tempfile
    from lib.objects.faker import create_ansible_collections
    from ansible.module_utils.common._collections_compat import CollectionLoader
    from ansible.module_utils.common._collections_compat import my_import

    # TEST: load standard Ansible plugin
    plugin_loader = PluginLoader('ansible.plugins.action', 'ActionModule', '_ansible_action_plugins', C.DEFAULT_INTERNAL_PLUGIN_PATH)
    obj = plugin_loader.get('raw')
    assert obj.__name__ == 'ActionModule'
    assert obj._load_name == 'raw'

    # TEST: load collection plugin in the right order
    role_loader = create_ans