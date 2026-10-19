

# Generated at 2022-06-13 17:28:50.125692
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    from unittest import TestCase

    from ansible.plugins import vars_plugins

    class LoaderMock(object):
        def __init__(self, all_plugins):
            self.all_plugins = all_plugins

        def all(self):
            return self.all_plugins

    path = "/path/to/plugins"
    entities = ["entity"]

    class PluginMock(object):
        def __init__(self, load_name, original_path):
            self._load_name = load_name
            self._original_path = original_path

    class PluginMockV2(object):
        def get_vars(self, loader, path, entities):
            return {"v2": True}

    class PluginMockV1(object):
        def get_host_vars(self, name):
            return

# Generated at 2022-06-13 17:28:53.515745
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    vars2 = {'a': 1, 'c': 3, 'd': 4, 'e': 5}
    plugin = type('Plugin', (object,), {'get_vars': lambda *args, **kwargs: vars1})
    loader = type('Loader', (object,), {'all': lambda: [plugin]})
    result = get_vars_from_path(loader, None, None)
    assert result == vars1

# Generated at 2022-06-13 17:28:58.505569
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Setup a mock loader object
    class MockVarsLoader(object):
        def __init__(self):
            self.all_plugins = []

        def all(self):
            return self.all_plugins

    loader = MockVarsLoader()

    # Setup a mock host object
    class MockHost(object):
        def __init__(self, name):
            self.name = name

    # Setup a mock vars plugin object that supports v2 API

# Generated at 2022-06-13 17:29:08.241490
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    import collections
    import unittest
    import json

    MOCK_VARS_PLUGIN_PATH = 'tests/unit/plugins/vars_plugins'
    MOCK_VARS_PLUGIN_TEST_FILE = 'test_plugin_vars.yaml'

    def _mock_load_plugin(plugin_path, class_prefix):
        """
        Function to mock the 'plugins/vars/__init__.py' file's 'load_plugin' function to return
        the list of plugin classes.
        """
        plugins = []
        for filename in os.listdir(plugin_path):
            if not filename.endswith('.py') or not filename.startswith(class_prefix):
                continue
            plugin_name = os.path.basename(filename)[:-len('.py')]
           

# Generated at 2022-06-13 17:29:16.125975
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # Setup
    from ansible.plugins.vars.host_group_vars import HostVars
    from ansible.plugins.vars.host_group_vars import GroupVars
    import ansible.plugins.loader as pl
    class DummyLoader(object):
        def get(self, name, *args, **kwargs):
            return pl.get_plugin_by_name(vars_loader, 'host_group_vars')
    loader = DummyLoader()
    plugin = pl.get_plugin_by_name(vars_loader, 'host_group_vars')
    path = './tests/units/vars_plugins/vars_plugins'
    entities = [Host('localhost')]
    entities.append(Host('127.0.0.1'))

# Generated at 2022-06-13 17:29:20.457632
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Execute function
    result = get_vars_from_path(loader,
                                path="/some/path",
                                entities=[Host(name="host1"), Host(name="host2")],
                                stage="inventory")
    assert result == {}

# Generated at 2022-06-13 17:29:26.066260
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Create a few test values for the parameters
    to_test_loader = None
    to_test_path = "test_path"
    to_test_entities = None
    to_test_stage = "test_stage"

    # Call the function with the created test values
    return_value = get_vars_from_path(to_test_loader, to_test_path, to_test_entities, to_test_stage)

    # assert the return value
    assert(return_value == {})

# Generated at 2022-06-13 17:29:37.297502
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleError
    import os

    # Set up some parameters to be used in creating an inventory with a single group
    test_inventory_name = 'test_no_whitelist_plugin'
    test_group_name = 'testgroup'
    test_file_path = os.path.join(C.DEFAULT_LOCAL_TMP, test_inventory_name)
    test_plugin_name = 'vars_plugin_test'
    test_whitelist_name = 'vars_whitelist_test'

    # Set up a single plugin

# Generated at 2022-06-13 17:29:48.635766
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # First with a vars directory
    assert get_plugin_vars('a/path', vars_loader.get('vars_dir'), 'a/path', ['host1']) == {'host1': {'var_dir': 'dir'}}

    # Second with a vars_dir plugin that doesn't have get_vars
    assert get_plugin_vars('a/path', vars_loader.get('vars_dir_v1'), 'a/path', ['host1']) == {'host1': {'var_dir': 'dir'}}


# Generated at 2022-06-13 17:29:49.126896
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True

# Generated at 2022-06-13 17:30:07.331766
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class FakeVars(object):
        def __init__(self, has_vars):
            self.has_vars = has_vars
            self.property = None

        def get_vars(self, loader, path, entities):
            return self.has_vars

        def get_group_vars(self, data):
            return self.has_vars

        def get_host_vars(self, data):
            return self.has_vars

    class FakeLoader(object):
        pass

    class FakeHost(object):
        def __init__(self, name):
            self.name = name

    class FakeGroup(object):
        def __init__(self, name):
            self.name = name

    fake_loader = FakeLoader()

    plugin = FakeVars({'one': 1})


# Generated at 2022-06-13 17:30:17.932746
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    loader = vars_loader.find_plugin('auto')
    inv_manager = InventoryManager()

    path = 'test/data/vars/get_vars_from_path/'
    entities = inv_manager.parse_inventory(path)
    assert len(entities['all']['children']) == 1
    assert len(entities['group1']['children']) == 1
    assert entities['host2']
    assert entities['host4']
    hostvars = entities['host4'].get_vars()
    assert hostvars['x'] == 'get_vars_from_path_host2'

    data = {}
    data

# Generated at 2022-06-13 17:30:18.852768
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader = None
    sources = ['origin']
    entities = ['hello']
    stage = "inventory"

# Generated at 2022-06-13 17:30:29.859061
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.cli import CLI
    import os
    import sys

    p = PlayContext()
    l = AnsibleCollectionLoader()
    c = CLI()

# Generated at 2022-06-13 17:30:41.170356
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from collections import namedtuple

    MockLoader = namedtuple('MockLoader', ['vars_plugin_list'])

    class MockVarsPlugin(object):
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self, loader, path, entities):
            return self.vars

    class MockHost(object):
        def __init__(self, name):
            self.name = name

    class MockGroup(object):
        def __init__(self, name):
            self.name = name

    expected_data = {'a': 1, 'group1': {'b': 2}, 'group2': {'b': 3, 'c': 4}, 'host1': {'b': 5, 'c': 6}}

# Generated at 2022-06-13 17:30:43.863863
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader, sources, entities, stage = None, None, None, None
    assert isinstance(get_vars_from_path(loader, sources, entities, stage), dict)


# Generated at 2022-06-13 17:30:53.557408
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    manager = InventoryManager(loader=loader, sources=['tests/vars_plugins/hosts'])
    results = get_vars_from_path(loader, 'tests/vars_plugins/inventory_directory', manager.hosts.values(), 'inventory')
    assert results == {
        'var_from_inventory_group_vars_plugin': {'plugin': 'inventory_group_vars'},
        'var_from_inventory_host_vars_plugin': {'plugin': 'inventory_host_vars'},
        'var_from_inventory_v2_plugin': {'plugin': 'inventory_v2'},
    }

# Generated at 2022-06-13 17:31:01.332765
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.extravars
    import ansible.plugins.vars.inventory_vars

    extra_vars ={"plugin_vars": "plugin_vars_value"}
    loader = ansible.plugins.vars.extravars.VarsModule(extra_vars, True)
    inventory_vars = {"inventory_vars": "inventory_vars_value"}
    path = "/work/ansible/test/file.yaml"
    entities = {"hosts": ['localhost']}

    assert get_vars_from_path(loader, path, entities, 'inventory') == {'plugin_vars': 'plugin_vars_value'}

    loader = ansible.plugins.vars.inventory_vars.VarsModule(inventory_vars, True)
    assert get_vars

# Generated at 2022-06-13 17:31:11.657034
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # mock loader
    class _Loader(object):
        class _DataCache(object):
            def set(self, cache_key, value):
                pass
        _cache = _DataCache()
        _basedir = os.getcwd()
    loader = _Loader()

    # mock plugin
    class _FileVars(object):
        def __init__(self):
            self._load_name = 'file'
        def get_vars(self, loader, path, entities):
            var_file = os.path.join(path, 'var_file.yml')
            var_file2 = os.path.join(path, 'var_file2.yml')
            if os.path.exists(var_file):
                return {
                    'var_file': var_file,
                }

# Generated at 2022-06-13 17:31:20.466415
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    with pytest.raises(AnsibleError, match='Cannot use v1 type vars plugin deprecated_yaml from'):
        vars_loader.all()
        get_vars_from_path(None, None, None, None)
    with pytest.raises(AnsibleError, match='Invalid vars plugin yaml from'):
        vars_loader.clear()
        vars_loader._plugins = { 'yaml': {} }
        get_vars_from_path(None, None, None, None)


# Generated at 2022-06-13 17:31:33.737436
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin = [{'run': lambda: ''}]
    entities = {}
    path = ''
    loader = ''
    data = get_vars_from_path(loader, path, entities, plugin)
    assert data == {'run': ''}



# Generated at 2022-06-13 17:31:35.921315
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    vars_loader._load_plugins()
    data = get_vars_from_path(None, None, None, None)
    assert type(data) == dict

# Generated at 2022-06-13 17:31:40.885439
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    from ansible.plugins.vars import vars_plugin

    class MyVarsPlugin(vars_plugin.VarsBase):

        def get_vars(self, loader, path, entities, cache=True):
            return {'foo': 'bar'}

    loader = None
    my_vars_plugin = MyVarsPlugin(loader, 'my_vars_plugin')
    plugin = my_vars_plugin
    path = '/foo/bar/baz'
    entities = []

    assert get_plugin_vars(loader, plugin, path, entities) == {'foo': 'bar'}

# Generated at 2022-06-13 17:31:48.764624
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    import unittest
    import ansible.utils.collection_loader

    class TestInventory:

        def __init__(self, path):
            self.path = path

        def get_hosts(self, pattern=None):
            return [('testhost', 'testgroup')]

    class TestPlugin(object):

        class VarsModule:

            REQUIRES_WHITELIST = True  # make this plugin whitelisted

            def get_vars(self, loader, path, entities):
                return {'mykey': 'myvalue'}

        def __init__(self, name):
            self._load_name = name
            self.VarsModule = TestPlugin.VarsModule


# Generated at 2022-06-13 17:31:50.639600
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert False

# Generated at 2022-06-13 17:31:51.531470
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    pass

# Generated at 2022-06-13 17:32:01.262383
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader

    from collections import namedtuple
    InventorySource = namedtuple('InventorySource', ['script', 'directory'])

    loader = vars_loader
    vars_plugin_list = list(vars_loader.all())
    # plugin_name= 'yaml'
    plugin_name = 'json'

    path = InventorySource(script=None, directory='/home/wxs/.ansible/source/GitProjects/demo')

    entities = ['localhost']
    stage = 'inventory'

    # vars_plugin_list = ['json', 'win_registry', 'yaml', 'ini', 'template', 'toml']
    vars_plugin_list = ['json']

# Generated at 2022-06-13 17:32:10.311982
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # for this test we use only the vars plugin in tests/units/plugins/vars/test_vars_plugin.py
    # which is not a real vars plugin.

    # vars plugin object
    vars_plugin = vars_loader.get("TestVarsPlugin")

    # create a target object the vars plugin can use
    target_obj = {
        'test_key': 'test_value',
        'test_key2': 'test_value2',
    }

    # create a path the vars plugin can use
    path = "/tmp/test_path"

    # get the vars from the plugin
    plugin_vars = get_plugin_vars(None, vars_plugin, path, [target_obj])

    # ensure the plugin vars are as expected

# Generated at 2022-06-13 17:32:13.160454
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    varsloader = vars_loader()
    data = get_vars_from_path(varsloader,'/home/rhn/ansible/','')
    print (data)


# Generated at 2022-06-13 17:32:24.268624
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class MockLoader:
        class paths:
            class basedir:
                def __str__(self):
                    return 'MockLoader_paths_basedir_str__'

    loader = MockLoader()

    # Test vars_loader Collection
    vars_loader_all = vars_loader.all()
    all_plugins = []
    for plugin in vars_loader_all:
        all_plugins.append(plugin._load_name)
    assert 'host_group' in all_plugins
    assert 'host' in all_plugins

    # Test vars_loader.all() to get all Collection
    assert type(vars_loader.all()) == type(vars_loader_all)

    # Test get_vars_from_path

# Generated at 2022-06-13 17:32:41.040236
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True

# Generated at 2022-06-13 17:32:51.204011
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.parsing.dataloader import DataLoader

    cwd = os.path.dirname(__file__)
    data_loader = DataLoader()
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = os.path.join(cwd, '../collections/')
    collection_loader = AnsibleCollectionLoader()

    path = os.path.join(cwd, '../collections/ansible_namespace/testmolecule/plugins/inventory/vars/test.py')
    entities = [Host(name='testhost')]

    data = get_vars_from_path(collection_loader, path, entities, 'start')

    assert data == {'testvar': 'testvalue'}



# Generated at 2022-06-13 17:33:01.773828
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    Unit test for function get_vars_from_path.
    """
    data = get_vars_from_path(None, './test_data/inventory/vars_plugin_data', ('a_group', 'b_group', 'c_group', 'd_group'), 'inventory')

    assert data['ansible_variable'] == 'ansible_value'
    assert data['ansible_host_one'] == 'host_one'
    assert data['ansible_group_one'] == 'group_one'
    assert data['ansible_group_two'] == 'group_two'

    data = get_vars_from_path(None, './test_data/inventory/vars_plugin_data', ('host1', 'host2', 'host3'), 'inventory')

    assert data['ansible_variable']

# Generated at 2022-06-13 17:33:12.106485
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader

    collection_path = './my_namespace.my_collection-1.2.3/plugins/vars/'
    collection_plugin_path = 'my_namespace.my_collection.my_plugin.yml'

    os.makedirs(collection_path)

    with open(os.path.join(collection_path, collection_plugin_path), 'w') as f:
        f.write('{"test_var": "test_value"}')

    loader = vars_loader.get(collection_plugin_path)

    my_data = get_vars_from_path(loader, collection_path, [], 'inventory')

    assert my_data['test_var'] == 'test_value'


# Generated at 2022-06-13 17:33:19.674928
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    Unit test for function get_vars_from_path
    """
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inventory = Inventory(loader=None, variable_manager=VariableManager(), host_list=['/tmp/myhost'])
    host = inventory.get_host("/tmp/myhost")

    try:
        import sockets
        sockets.AF_UNIX = 6
    except ImportError:
        sockets = None

    class Mock_Vars_Plugin(object):

        def get_vars(self, loader, path, entities):
            return {"test": "vars_two"}

    class Mock_Vars_Plugin_v1(object):
        def run(self):
            return {"test": "vars_three"}


# Generated at 2022-06-13 17:33:31.632697
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Dont actually use inventory
    display.verbosity = 3
    os.environ['ANSIBLE_INVENTORY_UNPARSED_FAILED'] = 'True'

    # Since vars_from_path is called on the playbook path and inventory sources, test both
    path = os.path.join(C.DEFAULT_LOCAL_TMP, 'tests/inventory')
    inventory = open(os.path.join(C.DEFAULT_LOCAL_TMP, 'tests/inventory/inventory'), 'r')
    loader = None
    entities = []

    data = get_vars_from_path(loader, path, entities, 'inventory')
    for line in inventory:
        if 'set_fact' in line:
            break
    assert line == "        set_fact: foo=bar\n"
    inventory.close

# Generated at 2022-06-13 17:33:38.142217
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # expected result
    class TestPlugin:
        def get_vars(self, loader, path, entities):
            return {}
    test_data = {}
    test_vars_plugin_list = [TestPlugin()]
    for plugin in test_vars_plugin_list:
        test_data = combine_vars(test_data, get_plugin_vars(loader=None, plugin=plugin, path=None, entities=None))

    result = get_vars_from_path(loader=None, path=None, entities=None, stage=None)

    assert test_data == result

# Generated at 2022-06-13 17:33:42.037090
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO(robb): create a mock for the vars_plugin_list to test the loading of specific vars plugins
    # TODO(robb): create a mock for the display object to test the messages about invalid vars plugins
    pass

# Generated at 2022-06-13 17:33:43.525388
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    modules = {}

# Generated at 2022-06-13 17:33:45.125388
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.loader import vars_loader

    plugin = vars_loader.get('test')
    assert plugin._load_name == 'test'

# Generated at 2022-06-13 17:34:13.327370
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # test with 1 vars plugin
    test_vars_plugin = lambda self: {'test-plugin-1': 'test-plugin-1-value'}
    test_vars_plugin._load_name = 'test-plugin-1'
    test_vars_plugin.REQUIRES_WHITELIST = True

    vars_loader.add(test_vars_plugin, 'test-plugin-1')
    vars_loader.resolve_all()

    (data, entities, stage) = ({}, [], 'task')

    C.VARIABLE_PLUGINS_ENABLED = ['test-plugin-1']
    C.RUN_VARS_PLUGINS = 'task'

    data = combine_vars(data, get_vars_from_path(None, '', entities, stage))

# Generated at 2022-06-13 17:34:14.029959
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:34:22.397303
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    import os
    import io

    import pytest
    from ansible.inventory.host import Host
    from ansible.utils.vars import combine_vars
    from ansible.plugins.vars import VarsModule
    from ansible.parsing.mod_args import ModuleArgsParser

    for plugin_name in C.VARIABLE_PLUGINS_ENABLED:
        if AnsibleCollectionRef.is_valid_fqcr(plugin_name):
            vars_plugin = vars_loader.get(plugin_name)
            if vars_plugin is None:
                # Error if there's no play directory or the name is wrong?
                continue
            if vars_plugin not in vars_plugin_list:
                vars_plugin_list.append(vars_plugin)


# Generated at 2022-06-13 17:34:29.285451
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_path = os.path.dirname(os.path.abspath(__file__))
    loader = vars_loader.get('yaml')
    entities = []
    data = get_vars_from_path(loader, test_path + '/test_vars_plugins/', entities, 'inventory')
    assert data['example_var'] == 'example'
    assert data['example_var_script'] == 'example_script'
    assert data['example_var_roles'] == 'example_roles'
    data = get_vars_from_path(loader, test_path + '/test_vars_plugins/', entities, 'task')
    assert data['example_var'] == 'example'
    assert data['example_var_script'] == 'example_script'

# Generated at 2022-06-13 17:34:31.266115
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: Make this test do more than just verify the function doesn't blow up
    assert True

# Generated at 2022-06-13 17:34:43.251659
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # This test is only relevant to 2.x because 1.x plugins do not implement
    # get_vars and/or get_[group|host]_vars.

    # A plugin with run but no get_vars/get_[group|host]_vars, which
    # represents a plugin that is not a variable plugin (such as, but not
    # limited to, those in the callback and connection plugin lists).
    class InvalidPlugin:
        def __init__(self, _load_name, _original_path):
            self._load_name = _load_name
            self._original_path = _original_path

        def run(self):
            pass

    class DummyPath:
        def __init__(self, path):
            self.path = path

    class DummyLoader:
        pass


# Generated at 2022-06-13 17:34:51.964693
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager('/etc/ansible/hosts')

    vars1 = get_vars_from_path(inventory, '/etc/ansible', None, None)
    assert isinstance(vars1, dict)

    vars2 = get_vars_from_path(inventory, '/etc/ansible', [inventory.hosts['host1']], None)
    assert isinstance(vars2, dict)

    vars3 = get_vars_from_path(inventory, '/etc/ansible', None, 'inventory')
    assert isinstance(vars3, dict)

    vars4 = get_vars_from_path(inventory, '/etc/ansible', None, 'task')
    assert isinstance(vars4, dict)

# Generated at 2022-06-13 17:35:02.758996
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.vars.vars_plugins.test_vars import TestVars
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.unsafe_proxy import wrap_var

    class TestLoader:
        class inventory_manager:
            pass

        class collection_paths:
            pass

    loader = TestLoader()
    loader.inventory_manager = InventoryManager(loader=loader, sources="localhost,")
    loader.collection_paths = [u'/test/test_collection', u'/test/test_collection/plugins/vars']
    path = '/test/test_collection'
    inventory_hostname = loader.inventory_manager.get_inventory_hostnames()
    group_name = 'group_name'
    group = loader

# Generated at 2022-06-13 17:35:13.241866
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import vars_plugins
    from ansible.plugins.loader import vars_loader
    orig_vars_plugins = vars_plugins[:]
    vars_loader.clear_all_vars_plugins()
    vars_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../test/vars_plugins'))

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['localhost,'])

# Generated at 2022-06-13 17:35:22.328823
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def get_vars(loader, path, entities):
        return {'a' : 1, 'b' : 2}

    import tempfile
    from ansible.plugins.loader import vars_loader
    from ansible.module_utils.basic import AnsibleModule

    old_plugin_list = vars_loader.all()

# Generated at 2022-06-13 17:35:51.672485
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible_collections.notstdlib.moveitallout.plugins.vars.not_the_default import PluginVars as pv
    from ansible.plugins.loader import vars_loader

    class FakeLoader:
        def get_basedir(self, *args, **kwargs):
            basedir = os.path.expanduser('~/ansible-collections/notstdlib/moveitallout/plugins/vars')
            return basedir

    class FakeGroup:
        def __init__(self, name):
            self.name = name

    class FakeHost:
        def __init__(self, name):
            self.name = name

    loader = FakeLoader()
    p = pv('not_the_default', loader)
    groups = [FakeGroup('group1'), FakeGroup('group2')]

# Generated at 2022-06-13 17:35:53.598473
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    test get_vars_from_path
    """
    assert get_vars_from_path(None, 'path', 'entities', 'stage') == {}

# Generated at 2022-06-13 17:36:00.581699
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    my_vars = {'my_var': 'my_value'}
    plugin = type('MyPlugin', (object,), {'get_vars': lambda s, l, x, e: my_vars})
    loader = type('MyLoader', (object,), {'servers': [plugin]})
    path = 'my_path'
    hosts = ['host1', 'host2']
    entities = [type('MyHost', (object,), {'name': host}) for host in hosts]
    stage = 'inventory'

    assert my_vars == get_vars_from_path(loader, path, entities, stage)

# Generated at 2022-06-13 17:36:11.989290
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef

    plugin_name = 'foo.bar'
    plugin = vars_loader.get(plugin_name)
    assert plugin is None

    directory = './lib/ansible/plugins/vars'
    plugin_path = os.path.join(directory, plugin_name + '.py')
    # create the file
    with open(plugin_path, 'w'):
        pass

    plugin = vars_loader.get(plugin_name)
    assert plugin is None

    # remove the file
    os.remove(plugin_path)

    plugin_name = AnsibleCollectionRef.parse('foo.bar.baz')
    loader = vars_loader.VarsModuleLoader()

# Generated at 2022-06-13 17:36:17.709491
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins import vars_loader

    loader = vars_loader
    path = "./lib/ansible/plugins/vars/"

    entities = []
    stage = "inventory"

    data = get_vars_from_path(loader, path, entities, stage)

    assert 'fact_caching_connection' in data
    assert 'fact_caching_prefix' in data
    assert 'vault_password_file' in data

# Generated at 2022-06-13 17:36:18.824504
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO: Add test
    pass

# Generated at 2022-06-13 17:36:25.839836
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def loader_fake(*args, **kwargs):
        return None

    vars_plugin_list = list(vars_loader.all())
    for plugin_name in C.VARIABLE_PLUGINS_ENABLED:
        if AnsibleCollectionRef.is_valid_fqcr(plugin_name):
            vars_plugin = vars_loader.get(plugin_name)
            if vars_plugin is None:
                # Error if there's no play directory or the name is wrong?
                continue
            if vars_plugin not in vars_plugin_list:
                vars_plugin_list.append(vars_plugin)

    for plugin in vars_plugin_list:
        vars_attrs = ('get_vars', 'get_host_vars', 'get_group_vars')
       

# Generated at 2022-06-13 17:36:35.967841
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class Plugin():
        pass

    test_entity = 'somebody'
    test_map = {test_entity: 'something'}
    plugin_instance = Plugin()

    def test_function(loader, path, entities):
        if entities[0] == test_entity:
            return test_map
        else:
            return {}

    def test_function2(entity_name):
        if entity_name == test_entity:
            return test_map
        else:
            return {}

    loader = {}
    plugin_instance.get_vars = test_function
    result = get_plugin_vars(loader, plugin_instance, test_entity, [test_entity])
    assert result == test_map

    plugin_instance.get_vars = test_function2

# Generated at 2022-06-13 17:36:44.680815
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.vars import test_vars_plugin
    from ansible.parsing.plugin_docs import read_vars_docs
    from ansible.utils.vars import combine_vars

    plugin_list = list(vars_loader.all())
    test_plugin = test_vars_plugin.TestVarsPlugin()
    if test_plugin not in plugin_list:
        plugin_list.append(test_plugin)

    test_vars_plugin.TestVarsPlugin.ADDED_DATA = {'test_var': 'yes'}
    data = get_vars_from_path(None, 'plugins/vars/test/', [], 'inventory')
    assert 'test_var' in data
    assert data['test_var']

# Generated at 2022-06-13 17:36:53.434497
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    loader = InventoryManager()
    sources = ['/root/test_get_vars_from_inventory_sources.yml']
    entities = [loader.inventory._inventory.get_group('all')]
    stage = 'task'
    data = get_vars_from_inventory_sources(loader, sources, entities, stage)
    assert data == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Generated at 2022-06-13 17:37:43.885238
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Loader that returns an empty dict for each iterable
    class MockInventoryLoader:
        def __iter__(self):
            return self

        def __next__(self):
            raise StopIteration()

    # Mock class for vars_loader
    class MockVarsLoader:
        def __init__(self):
            self.plugin_list = []
            self.plugin_dict = {}

        def __iter__(self):
            return iter(self.plugin_list)

        def __contains__(self, plugin_name):
            return plugin_name in self.plugin_dict

        def __getitem__(self, plugin_name):
            return self.plugin_dict[plugin_name]

        def add(self, plugin):
            self.plugin_list.append(plugin)

# Generated at 2022-06-13 17:37:51.828853
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import VarsModule

    class TestVarsPlugin(VarsModule):
        """
        Test variables plugin for unit testing
        """
        def get_vars(self, loader, path, entities):
            return {'test': 'test'}

    vars_plugins = [TestVarsPlugin('test')]
    for plugin in vars_plugins:
        data = get_vars_from_path(None, None, None, 'inventory')
        assert data == {'test': 'test'}, 'unexpected vars plugin data'

# Generated at 2022-06-13 17:37:52.727402
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    assert get_vars_from_path is not None

# Generated at 2022-06-13 17:38:00.530602
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = [
        {'hosts': ['host1'], 'vars': {'var1': 'value1'}},
        {'hosts': ['host2'], 'vars': {'var2': 'value2'}}
    ]

    # Set plugin type
    plugin_type = 'vars'
    # Initialize the variable manager
    vars_manager = VariableManager()
    # Load vars plugins
    vars_loader.add_directory(os.path.join(C.DEFAULT_MODULE_PATH, plugin_type))
    # Load inventory

# Generated at 2022-06-13 17:38:07.297301
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class TestPlugin():

        def get_vars(self, loader, path, entities):
            return {'test_plugin': 'get_vars'}

        def get_host_vars(self, hostname):
            return {'test_plugin': 'get_host_vars'}

    class TestPlugin_fail():

        def get_vars(self, loader, path, entities):
            return {'test_plugin_fail': 'get_vars'}

    class TestPlugin_v1():

        def run(self, hostname):
            return {'test_plugin_v1': 'run'}

    class TestPlugin_v1_fail():

        def run(self):
            return {'test_plugin_v1': 'run'}


# Generated at 2022-06-13 17:38:08.246693
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:38:17.159404
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def foo_get_vars(self, loader, path, entities):
        return {"foo_plugin_var": "foo_plugin_value"}

    def bar_get_vars(self, loader, path, entities):
        return {"bar_plugin_var": "bar_plugin_value"}

    class FooPlugin(object):
        get_vars = foo_get_vars

    class BarPlugin(object):
        get_vars = bar_get_vars

    loader = vars_loader
    plugin_list = [FooPlugin(), BarPlugin()]
    for plugin in plugin_list:
        loader.add(plugin._load_name, plugin)

    entities = [Host("test_get_vars_from_path_host")]


# Generated at 2022-06-13 17:38:17.953309
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:38:24.612955
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    import pytest

    inv_data = """
    [group1]
    host1
    host2
    """
    host_data = """
    [group2]
    host3
    """
    inv_file1 = 'inventory1.ini'
    host_file = 'inventory2.ini'
    with pytest.raises(AnsibleError):
        get_vars_from_path(vars_loader, '.', [], 'inventory')
    with open(inv_file1, 'w') as f:
        f.write(inv_data)
    with open(host_file, 'w') as f:
        f.write(host_data)


# Generated at 2022-06-13 17:38:33.754738
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    import ansible.plugins.vars.host_var_files
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    vars_loader.add('mock_vars_plugin', ansible.plugins.vars.host_var_files.LookupModule())
    loader = DictDataLoader({'/etc/ansible/hosts': '''
        [group1]
        localhost
        [group2]
        localhost
        [child:children]
        group1
        group2
    '''})

    inventory = loader.load_inventory(host_list='/etc/ansible/hosts')
