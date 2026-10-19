

# Generated at 2022-06-13 13:17:33.190102
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    obj = PluginLoader('')
    assert False == (None in obj)


# Generated at 2022-06-13 13:17:43.145523
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    from ansible.plugins.loader import PluginLoader
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import b
    from ansible.module_utils import basic

    path_tmpdir = basic._create_tmp_dir()
    path_module = os.path.join(path_tmpdir, 'foo.py')

    with open(path_module, 'wb') as f:
        f.write(to_bytes('''#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import basic

try:
    import json
except ImportError:
    import simplejson as json

DOCUMENTATION = '''))


# Generated at 2022-06-13 13:17:44.372786
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    pass


# Generated at 2022-06-13 13:17:52.577866
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    '''
    Unit test for method __setstate__ of class PluginLoader
    '''
    loader = PluginLoader('ansible.plugins.test', 'TestPlugins', 'test_plugins', 'Test', 'test')
    loader.__setstate__(serialized_data=dict(aliases={"test":"test"}))
    # If this assertion fails, there is a bug in ansible/plugins/loader/__init__.py
    assert loader.aliases == {'test': 'test'},"Attribute aliases has unexpected value: %s" % loader.aliases

# Generated at 2022-06-13 13:17:57.490418
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():

    data=dict(
        name="name",
        _PLUGIN_PATH_CACHE = {},
        package="package",
        class_name="class_name",
        base_class="base_class",
        _searched_paths=[],
        subdir="subdir",
        aliases={},
        _module_cache={},
        _plugin_config_cache={},
        _plugin_count_cache={},
        config_class="config_class",
        config_envvar="config_envvar",
        )

    # Instantiate PluginLoader
    pl = PluginLoader(**data)

    # test find_plugin method:
    # We need to remove the '_' from the attribute name
    # to get the actual method name

# Generated at 2022-06-13 13:18:03.254334
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = "PLAYBOOK_DIR/tests/plugins/module_utils"
    add_all_plugin_dirs(path)
    if os.path.isdir(path):
        for name, obj in get_all_plugin_loaders():
            if obj.subdir:
                plugin_path = os.path.join(path, obj.subdir)
                assert os.path.isdir(plugin_path)

# Generated at 2022-06-13 13:18:14.197050
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    from ansible.plugins.loader import add_all_plugin_dirs

    class FakePluginLoader:
        subdir = 'fake'
        def add_directory(self, path):
            assert path == os.path.join(os.path.expanduser('~/fakepath'), 'fake')

    fl = FakePluginLoader()
    pls = dict(pluginloader=fl)
    add_all_plugin_dirs.__globals__.update(pls)

    # Make sure that we don't crash and burn if no subdir exists in the path given
    add_all_plugin_dirs('~/fakepath')

    # Create a subdir for the FakePluginLoader and make sure it's added
    os.mkdir(os.path.join(os.path.expanduser('~/fakepath'), 'fake'))
   

# Generated at 2022-06-13 13:18:20.935338
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    PL = PluginLoader(package='test',
                      directories=['/test/test_collections', '/test/test_collections2'])
    result = PL.find_plugin_with_context(name='test.plugin1', collection_list=None)
    assert result.plugin_resolved_path == '/test/test_collections/test/plugins/test/plugin1.py'
    assert result.plugin_resolved_name == 'test.plugin1'
    result = PL.find_plugin_with_context(name='test.plugin2', collection_list=None)
    assert result.plugin_resolved_path == '/test/test_collections/test/plugins/test/plugin2.py'
    assert result.plugin_resolved_name == 'test.plugin2'

# Generated at 2022-06-13 13:18:23.678220
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    shell = get_shell_plugin(shell_type='sh')
    assert shell.SHELL_FAMILY == 'sh'
    assert shell.executable == '/bin/sh'



# Generated at 2022-06-13 13:18:32.523179
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    # This is an example plugin loader for the test cases. It is not
    # well written and it's functionality is very limited.
    class TestPluginLoader(PluginLoader):
        def __init__(self, package, directories):
            super(TestPluginLoader, self).__init__(package, directories, '', 'Plugin')

    # Set up working directories
    d1 = tempfile.mkdtemp(dir='/tmp')
    d2 = tempfile.mkdtemp(dir='/tmp')

    # Put a plugin in a plugin directory

# Generated at 2022-06-13 13:19:11.370879
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader(
        package='ansible.module_utils.foo',
        searchpath=['test/unit/module_utils/test_foo',
                    'test/unit/module_utils/other_foo',
                    'test/unit/module_utils/bar'],
        keep_patterns=['*.py'])
    plugin_load_context = loader.find_plugin_with_context(
        name='my_plugin',
        mod_type_name='plugin',
        collection_list=None,
    )
    assert plugin_load_context.resolved
    assert plugin_load_context.plugin_resolved_name == 'my_plugin'
    assert plugin_load_context.plugin_resolved_path == 'test/unit/module_utils/test_foo/my_plugin/__init__.py'


# Generated at 2022-06-13 13:19:19.389287
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import os
    C.DEFAULT_DEBUG = True
    C.DEFAULT_COLLECTIONS_PATHS = []
    # testing dummy, using file fixture
    test_file_fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'PluginLoader.find_plugin.yml')
    # expected result is the content of the last file fixture
    expected_yml = yaml.safe_load(open(test_file_fixture_path).read())

    p = PluginLoader('action_plugin', 'ActionModule', '_')

    # normalize and validate test fixtures
    for index, element in enumerate(expected_yml['tasks']):
        if '_expected' in element:
            expected_yml['tasks'][index]['_expected']['exception']

# Generated at 2022-06-13 13:19:32.920901
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader(
        package='ansible.plugins.testpkg', class_name='MyPluginClass',
        config_key='ANSIBLE_TESTPKG_PLUGINS', aliases={},
    )

    def test_find_plugin(import_name, expected_fqcr, expected_path):
        assert plugin_loader.find_plugin(name=import_name) == expected_fqcr
        assert plugin_loader.find_plugin_with_context(name=import_name).plugin_resolved_path == expected_path

    test_find_plugin('aliased', 'ansible_collections.testcoll.other.module1', '/path/to/ansible_collections/testcoll/other/plugins/modules/module1.py')

# Generated at 2022-06-13 13:19:36.252483
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    loader = PluginLoader(os.path.basename(__file__).replace('.py', ''), 'ansible.plugins')
    loader.__setstate__((set(), list(), dict(), None, None, None, list(), list()))
    assert loader.class_name == 'ansible.plugins'

# Generated at 2022-06-13 13:19:50.005568
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import Jinja2Loader

    def _get_loader():
        loader = DataLoader()
        loader.set_basedir('/tmp')

        host_inventory = InventoryManager(loader, 'localhost')
        variable_manager = VariableManager(loader=loader, inventory=host_inventory)

        return Jinja2Loader(variable_manager)

    # Test that a module plugin by name returns the requested plugin
    p = _get_loader().get('lookup')
    assert isinstance(p, Jinja2Extensions)

    # Test that a module plugin by path returns the

# Generated at 2022-06-13 13:20:01.272827
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    module_name = 'module'

    # constructor: return None
    loader = Jinja2Loader(module_name, 'path', 'class', 'base-class')
    assert loader.find_plugin('pluginname') is None

    # function find_plugin not implemented
    try:
        # create internal objects of class, which is not exposed for normal code
        loader._searched_paths = ['path1', 'path2']
        loader._module_cache = {'path': module_name}
        loader.find_plugin('pluginname')
        # NOTE: we won't get here, expected exception
        assert False
    except AnsibleError as e:
        assert e.message == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'


# Generated at 2022-06-13 13:20:08.511310
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    test_obj = PluginLoader("", "", "", "")

    # Test with no args
    test_obj.add_directory(path="/Users/anirudh/workspace/Collection")
    # Test with no args
    test_obj.add_directory(path="/Users/anirudh/workspace/Collection/random")
    # Test with no args
    test_obj.add_directory(path="/Users/anirudh/workspace/Collection/random")
    # Test with no args
    test_obj.add_directory(path="/Users/anirudh/workspace/Collection/random")
    # Test with no args
    test_obj.add_directory(path="/Users/anirudh/workspace/Collection/random")
    # Test with no args

# Generated at 2022-06-13 13:20:19.411286
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    PLUGIN_PATH_CACHE.clear()
    sys.path.pop()
    sys.path.pop()
    plugin_path_list = ["/tmp/foo/plugins/action", "/tmp/foo/plugins/module", "/tmp/foo/plugins/filter"]
    sys.path.extend(plugin_path_list)
    add_all_plugin_dirs("/tmp/foo")
    assert PLUGIN_PATH_CACHE[os.path.basename(plugin_path_list[0])] == os.path.join(plugin_path_list[0], "*")
    assert PLUGIN_PATH_CACHE[os.path.basename(plugin_path_list[1])] == os.path.join(plugin_path_list[1], "*")
    assert PLUGIN_PATH_

# Generated at 2022-06-13 13:20:27.638285
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():

    # Test 1 - path is a directory
    class TestPluginLoader(PluginLoader):
        pass
    test_plugin_loader = TestPluginLoader()
    test_plugin_loader.set_directory(os.path.join(C.DEFAULT_LOCAL_TMP, 'ansible_module_utils'))
    test_plugin_loader.socket_path = None

    b_path = os.path.expanduser(to_bytes(C.DEFAULT_LOCAL_TMP, errors='surrogate_or_strict'))
    if os.path.isdir(b_path):
        if test_plugin_loader.subdir:
            plugin_path = os.path.join(b_path, to_bytes(test_plugin_loader.subdir))
            if os.path.isdir(plugin_path):
                test_

# Generated at 2022-06-13 13:20:35.108170
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    obj = Jinja2Loader('filter_loader', 'filter_plugins', C.DEFAULT_FILTER_PLUGIN_PATH)
    name = 'terraform'
    plugin = obj.get(name)
    assert plugin.name == name
    assert plugin.filter_loader == obj


# Generated at 2022-06-13 13:21:19.514809
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():

    # This test is to cover the functionality of the function find_plugin in class PluginLoader
    # Test case 1: If a plugin file is not found, the function find_plugin throws the exception
    #              AnsibleError
    with pytest.raises(AnsibleError) as excinfo:
        find_plugin(plugin_name='TestPlugin', plugin_type='TestPluginType')
    assert "TestPlugin could not be found for the TestPluginType TestPluginType" in str(excinfo.value)

    # Test case 2: If a plugin file is found, the function find_plugin returns the path to the
    #              plugin file
    # Test Plugin name: test.py
    # Test Plugin type: TestPluginType

    # Adding the TestPlugin as global to the test module
    # TestPlugin is used to be searched in the directories
    global TestPlugin

    #

# Generated at 2022-06-13 13:21:26.522210
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    # Test PluginLoader.__setstate__
    # This method is called after __getstate__ to restore the object state.
    # It assumes that the object has been initialized properly.
    # This method might be called after the object has been created using
    # the class constructor or after it has been unpickled.
    # It's not required to deal with the extra state that might
    # be returned by __getstate__.
    #
    # We use it to check if the object was pickled correctly.
    pass

# Generated at 2022-06-13 13:21:34.216953
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    '''
    Unit test for method __setstate__()
    :return:
    '''
    pl = PluginLoader(package='ansible.modules.', class_name='ModuleUtil')
    #
    # PluginLoader.__setstate__() works but not in this way.  PluginLoader is set to pickleable
    # but its not a namedtuple.
    #
    # pl.__setstate__((1,2,3,4,5))
    # assert pl.package == 1
    # assert pl.class_name == 2
    # assert pl.paths == 3
    # assert pl.package_path == 4
    # assert pl.aliases == 5
    #
    # pl.__setstate__((1,2))
    # assert pl.package == 1
    # assert pl.class_name == 2


# Generated at 2022-06-13 13:21:41.481741
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():

    # Test when self.package
    plugin_loader = PluginLoader('foo', 'bar')
    plugin_loader.__setstate__({})
    assert not hasattr(plugin_loader, 'package')
    assert not hasattr(plugin_loader, 'class_name')

    # Test when not self.package
    plugin_loader = PluginLoader(class_name='bar')
    plugin_loader.__setstate__({})
    assert not hasattr(plugin_loader, 'package')
    assert not hasattr(plugin_loader, 'class_name')


# Generated at 2022-06-13 13:21:51.329208
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # Create an instance of PluginLoader
    AP = PluginLoader('ansible.plugins', 'Connection')
    # Create a (fake) plugin path
    from collections import namedtuple
    ANSIBLE_TEST_DATA = namedtuple('ANSIBLE_TEST_DATA', ('ansible_test_data'))
    plugin_path = AnsiblePlugin(
        name=None,
        path=ANSIBLE_TEST_DATA('ansible/test/unit/collection/plugins/test_ansible_collections.py'),
        collection_name=None,
        version=None
    )
    # Test find_plugin with a valid plugin name
    AP.find_plugin_with_context('connection_test', collection_list=[plugin_path])


# Generated at 2022-06-13 13:21:57.919287
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    from os.path import realpath, abspath
    from shutil import rmtree
    from ansible.utils import context_objects as co

    current_test_directory = realpath(tempfile.mkdtemp())
    base_test_directory = realpath(os.path.join(current_test_directory, 'base_test_directory'))
    for path_id in ('valid_path', 'invalid_path'):
        os.mkdir(os.path.join(current_test_directory, path_id))

# Generated at 2022-06-13 13:22:03.498981
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():

    class_loader = Jinja2Loader(package='ansible.plugins.filter', config={}, directories=[])

    try:
        class_loader.get('camel_to_snake_case')
    except AnsibleError as e:
        assert e.message == 'No code should call "get" for Jinja2Loaders (Not implemented)'

    try:
        class_loader.get('ansible.builtin.camel_to_snake_case')
    except AnsibleError as e:
        assert e.message == 'No code should call "get" for Jinja2Loaders (Not implemented)'



# Generated at 2022-06-13 13:22:12.601218
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    finder = PluginLoader()
    # Test case: when name is 'Copy'
    # Expected Result: find_plugin method returns [PluginLoader.NOPE_CONTEXT, 'ansible.plugins.action.copy.ActionModule']
    # Actual Result:
    assert finder.find_plugin('Copy') == [PluginLoader.NOPE_CONTEXT, 'ansible.plugins.action.copy.ActionModule']

    # Test case: when name is 'AnsibleModule'
    # Expected Result: find_plugin method returns [PluginLoader.NOPE_CONTEXT, 'ansible.module_utils.basic.AnsibleModule']
    # Actual Result:
    assert finder.find_plugin('AnsibleModule') == [PluginLoader.NOPE_CONTEXT, 'ansible.module_utils.basic.AnsibleModule']

    # Test

# Generated at 2022-06-13 13:22:16.638571
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    d = os.path.dirname(__file__)
    d = os.path.join(d, 'config_definitions')
    LOADER.add_directory(d, with_subdir=False)
    LOADER.add_directory(d, with_subdir=True)


# Generated at 2022-06-13 13:22:18.901917
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    assert isinstance(PluginLoader.all, types.MethodType)


# Get the class of an object (python, not ansible)

# Generated at 2022-06-13 13:23:28.616064
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():
    p = PluginLoader('test_plugin', 'test_plugin', 'test')
    p.add_directory('./test/test_plugins')
    assert len(p.plugin_paths) == 1
    assert 'test/test_plugins' in p.plugin_paths
    p.add_directory('./test/test_plugins')
    assert len(p.plugin_paths) == 1
    assert 'test/test_plugins' in p.plugin_paths
    p.add_directory('./test/test_plugins/')
    assert len(p.plugin_paths) == 1
    assert 'test/test_plugins' in p.plugin_paths
    p.add_directory('test/test_plugins')
    assert len(p.plugin_paths) == 1

# Generated at 2022-06-13 13:23:43.927402
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    '''
    Unit test for method __setstate__ of class PluginLoader.

    Test to ensure that pickling/unpickling still works after the
    addition of the __setstate__ method in Python 2.6.
    '''
    import pickle
    import six

    if six.PY2:
        plugin_loader = PluginLoader('ansible.plugins.lookup')
        plugin_loader2 = pickle.loads(pickle.dumps(plugin_loader))
        assert plugin_loader.paths == plugin_loader2.paths
        assert plugin_loader.package == plugin_loader2.package
        assert plugin_loader.base_class == plugin_loader2.base_class

PLUGIN_PATH_CACHE = {}
PLUGIN_LOADER_CACHE = {}
PLUGIN_CACHE = {}



# Generated at 2022-06-13 13:23:56.320337
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    # We want to test the functionality of the __setstate__ method.
    # From what I can tell, PluginLoader is not used as a class in library code.
    # It's used as a base class, but it's hard to instantiate a PluginLoader directly
    # because its internal API is not presented in a way that's usable on its own.
    # So, the best way I can think of to test this method is to have some simple
    # plugin code, and then to call the method from a unit test.
    import os
    import imp
    import sys
    here = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.join(here, 'library/plugins/lookup'))
    from test_plugin_loader import TestLookupModule as test_lookup_plugin


# Generated at 2022-06-13 13:23:58.287607
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    add_dirs_to_loader('filter', ['/path/to/filters'])
    assert '/path/to/filters' in filter_loader.package_paths



# Generated at 2022-06-13 13:24:03.803156
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'action_plugins')
    assert os.path.isdir(fixture_path)
    assert os.listdir(fixture_path)

    # instantiate object
    PluginLoader('action', 'ActionModule', 'ansible.plugins.action', C.DEFAULT_ACTION_PLUGIN_PATH, 'action_plugins', 'action')
    # method under test
    # Module.__setstate__()
    raise SkipTest

# Generated at 2022-06-13 13:24:15.249502
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    # load test data
    which_loader = 'shell'
    paths = ['./tests/unit/plugins/loader']

    # call actual function to retrieve the shell plugin
    shell_plugin = add_dirs_to_loader(which_loader, paths)

    # test assertion
    assert shell_plugin is not None
    assert 'ExecutorModule' in shell_plugin.name
    assert shell_plugin.name == 'shell'
    assert shell_plugin.__doc__ == 'Shell execute a command and return the results'
    assert shell_plugin.SHELL_FAMILY == 'sh'
    assert 'module_utils/shell.py' in shell_plugin.get_filename()
    assert shell_plugin.__module__ == 'tests.unit.plugins.loader.module_utils.shell'
    assert shell_plugin.get_option('shell')

# Generated at 2022-06-13 13:24:29.396833
# Unit test for method __setstate__ of class PluginLoader

# Generated at 2022-06-13 13:24:32.148490
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    loader = PluginLoader('a')
    # plugin_load_context must be a obj of PluginLoadContext
    assert loader.get_with_context('b')[1].__class__.__name__ == 'PluginLoadContext'

# Generated at 2022-06-13 13:24:40.392886
# Unit test for method __setstate__ of class PluginLoader
def test_PluginLoader___setstate__():
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 13:24:50.244555
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    from ansible.plugins.shell import ShellModule
    from ansible.plugins.action.normal import ActionModule as normalActionModule
    import pytest
    cmd = '/bin/ls'
    executable = '/bin/bash'
    shell = get_shell_plugin('sh', executable)
    assert isinstance(shell, ShellModule)
    assert shell.executable == executable
    shell = get_shell_plugin(executable=executable)
    assert isinstance(shell, ShellModule)
    assert shell.executable == executable
    shell = get_shell_plugin('sh')
    assert isinstance(shell, ShellModule)
    assert shell.executable == 'sh'
    shell = get_shell_plugin(executable=cmd)
    assert isinstance(shell, normalActionModule)
    assert shell.executable == cmd

# Generated at 2022-06-13 13:25:45.215729
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    # Init args
    package = 'ansible.plugins.action'
    subdir = 'actions'
    class_name = 'ActionModule'
    base_class = 'ActionBase'
    plugins_path = None
    collection_list = ['namespace.collection1', 'namespace.collection2']
    config = None
    aliases = {}

    # Init return value for 'find_plugin_with_context'
    plugin_load_context = PluginLoader.PluginLoadContext(
        resolved=True,
        plugin_resolved_name='test',
        plugin_resolved_path='/path/to/test',
        searched_paths=[],
    )

    # Init return value for '_find_fq_plugin_with_context (line 111)'

# Generated at 2022-06-13 13:25:49.793007
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    loader = PluginLoader('callback', 'CallbackModule')
    callback = loader.get_with_context('default')
    assert callback.object.__class__.__name__ == 'Default'


# Generated at 2022-06-13 13:25:59.933873
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    orig_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    # First, we'll create a new plugin loader and make sure it's
    # empty.
    test_plugin_loader = PluginLoader('test_plugin', 'test_path')
    assert test_plugin_loader.all() == []
    assert test_plugin_loader._package_cache == {}

    # We'll create a temporary directory and add two plugin files to
    # it, one for each of the two plugins we'll be testing.

    # Import the tempfile module, and use it to create a temporary
    # directory, which we'll use for testing.
    import tempfile
    tmp_dir = tempfile.mkdtemp()

    # Create plugin 1