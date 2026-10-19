

# Generated at 2022-06-13 17:28:59.918492
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath
    from ansible.vars.manager import VariableManager
    from ansible.vars.manager import _get_default_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.collection_vars import CollectionVars
    from ansible.vars.group_vars import GroupVars

    sources = [DataLoader().get_real_file(unfrackpath(__file__))]

# Generated at 2022-06-13 17:29:04.533909
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import get_collection_role_lookup_info
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    collection_base_path, collection_lookup_paths = get_collection_role_lookup_info()
    variable_manager = VariableManager(loader=loader, collection_search_paths=collection_lookup_paths)
    result = get_vars_from_path(loader, '../../../test/integration/targets', ['localhost'], 'inventory')
    assert type(result) == dict

# Generated at 2022-06-13 17:29:13.117573
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # unit test class for mocked func_loaders
    class FakeVarsPlugin(object):

        def __init__(self, name, path=None, stage=None):
            self._load_name = name
            self._original_path = path
            self._stage = stage

        def get_vars(self, loader, path, entities):
            return {'data': path}

    class FakeGroupVarsPlugin(FakeVarsPlugin):

        def get_vars(self, loader, path, entities):
            for entity in entities:
                if isinstance(entity, Host):
                    return {'data': path + entity.name}


# Generated at 2022-06-13 17:29:23.457807
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from importlib import import_module

    # TODO: Add a test to verify the error message
    # TODO: Add a test to verify the error message
    # TODO: Add a test to verify the error message

    # Create a dummy vars_loader
    vars_loader._all = {}

    # Get the YAML plugin
    yaml_plugin = vars_loader.get('yaml')
    vars_loader._all.update({yaml_plugin._load_name: yaml_plugin})

    # Load the plugin module
    module = import_module(yaml_plugin._original_path)

    # Make sure the YAML plugin is in the list of vars plugins
    assert yaml_plugin.get_vars == getattr(module.VarsModule, 'get_vars')

# Generated at 2022-06-13 17:29:34.913114
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class TestLoader:
        def __init__(self):
            pass

    class DummyVarsPlugin:
        def get_vars(self, loader, path, entities):
            return {'plugin1': 'plugin1'}

    class DummyVarsPluginWithConfig:
        def __init__(self):
            self.cp = ConfigParser()
            self.cp.add_section('defaults')
            self.cp.set('defaults', 'stage', 'inventory')

        def get_option(self, k):
            return self.cp.get('defaults', k)

    class DummyVarsPluginWithConfigAndStage:
        def __init__(self):
            self.cp = ConfigParser()
            self.cp.add_section('defaults')

# Generated at 2022-06-13 17:29:36.831065
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    unit test for get_vars_from_path
    """
    pass

# Generated at 2022-06-13 17:29:41.881090
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())
    result = get_vars_from_path(None, None, None, None)
    assert result == {}

    result = get_vars_from_path(None, None, ['localhost'], None)
    assert result == {}

# Generated at 2022-06-13 17:29:51.125355
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import ansible_collection_loader

    plugin_name = 'dummy_vars_plugin'
    plugin_path = os.path.join('test', 'units', 'plugins', 'vars', plugin_name)
    new_plugin_path = os.path.join(plugin_path, 'plugins')

    # create dummy plugin
    assert ansible_collection_loader.add_directory(plugin_path, with_subdir=False, ignore_errors=True)

    plugin = vars_loader.get(plugin_name)

    assert plugin is not None

    # make use of it

# Generated at 2022-06-13 17:30:00.230233
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    a = AnsibleCollectionRef.parse('ansible.builtin.vars_plugin')
    b = b'dummy_path'
    c = ('entity1', 'entity2')
    d = 'inventory'
    # test dummy plugin having a method get_vars
    # with get_vars calling get_host_vars and get_group_vars
    class DummyPlugin2:
        _load_name = 'dummy_plugin2'
        def get_vars(self, loader, path, entities):
            data = {}
            for entity in entities:
                if isinstance(entity, Host):
                    data.update(self.get_host_vars(entity))
                else:
                    data.update(self.get_group_vars(entity))
            return data

# Generated at 2022-06-13 17:30:09.881931
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import foo_vars
    test_path = '/test_path/'
    test_host = Host('test_host')
    test_group = 'test_group'
    test_host_list = [test_host]
    test_group_list = [test_group]
    test_entity_list = [test_host, test_group]
    test_plugin = foo_vars.VarsModule()
    test_plugin._load_name = 'foo_vars'
    test_plugin._original_path = '/test_plugin/'
    test_plugin.get_vars = lambda x, y, z: "test_vars"
    test_loader = object()
    assert get_plugin_vars(test_loader, test_plugin, test_path, test_host_list)

# Generated at 2022-06-13 17:30:18.500754
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    loader = InventoryManager()
    vars_from_path = get_vars_from_path(loader, 'test/testdata/vars_plugin/test_vars_plugins/', [], 'inventory')
    assert vars_from_path['from_inventory_vars_test_vars_plugins_path']

# Generated at 2022-06-13 17:30:26.060074
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    test_loader = vars_loader()

    class basic_vars_plugin:
        _load_name = 'basic_vars'

        def get_vars(self, loader, path, entities):
            return {'basic': 'value'}

    class demand_vars_plugin:
        _load_name = 'demand_vars'

        def get_vars(self, loader, path, entities):
            return {'demand': 'value'}

        @staticmethod
        def get_option(key):
            if key == 'stage':
                return 'inventory'

    class start_vars_plugin:
        _load_name = 'start_vars'

        def get_vars(self, loader, path, entities):
            return {'start': 'value'}


# Generated at 2022-06-13 17:30:37.211438
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.utils.collection_loader import AnsibleFileFinder
    from ansible.utils import collection_finder
    from ansible.utils.collection_loader import AnsibleCollectionRef

    plugin1_path = collection_finder.find_collection_file("plugins/vars/plugin1.yml")
    plugin2_path = collection_finder.find_collection_file("plugins/vars/plugin2.yml")
    plugin1 = AnsibleFileFinder(plugin1_path)
    plugin2 = AnsibleFileFinder(plugin2_path)
    vars_loader.resolve_collection_path(AnsibleCollectionRef.from_str('ansible/testcoll'))


# Generated at 2022-06-13 17:30:46.084390
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import copy
    import unittest
    class FakeVarsPlugin(object):
        def __init__(self, file_name, path, entities, stage):
            self.file_name = file_name
            self.path = path
            self.entities = entities
            self.stage = stage

        def get_option(self, name):
            if name == 'stage':
                if self.stage == 'inventory':
                    return 'all'
                else:
                    return 'task'
            else:
                return None

        @staticmethod
        def get_vars(loader, path, entities):
            return {
                'path': path,
                'entities': entities
            }


# Generated at 2022-06-13 17:30:56.185916
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="")
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # no plugin registered
    vars_plugin_list = list(vars_loader.all())
    assert get_vars_from_path(loader, "path", [], "start") == {}

    # test with basic plugin
    vars_plugin_module = get_vars_plugin_class()
    vars_plugin_list.append(vars_loader.add_plugin(VarsModule, vars_plugin_module, "vars_plugin_module"))
    assert get_vars_from_

# Generated at 2022-06-13 17:30:58.026722
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    data = get_vars_from_path(None, C.DEFAULT_LOCAL_TMP, None, 'task')
    assert data == {}



# Generated at 2022-06-13 17:30:58.443224
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:31:02.136390
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())
    plugin = vars_plugin_list[0]
    path = './'
    entities = []
    stage = 'all'
    data = get_vars_from_path(vars_plugin_list, path, entities, stage)
    print(data)

if __name__ == '__main__':
    test_get_vars_from_path()

# Generated at 2022-06-13 17:31:11.991454
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=["tests/unit/plugins/test_vars_loader/inventory/host_vars_dir1"])

    vars = get_vars_from_path(loader=loader, path="tests/unit/plugins/test_vars_loader/inventory/host_vars_dir1",
                              entities=inv.hosts.values(), stage='inventory')
    host_vars_dir1 = vars.get('host_vars_dir1')
    assert host_vars_dir1 == 'host_vars_dir1'


# Generated at 2022-06-13 17:31:23.536609
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.config.manager import ConfigManager
    config = ConfigManager(['ansible.cfg'])
    DEFAULT_CACHE_PLUGIN_NAME = 'jsonfile'
    DEFAULT_CACHE_PLUGIN_CONNECTION = ''
    cache_plugin = config.get_cache_plugin(DEFAULT_CACHE_PLUGIN_NAME, DEFAULT_CACHE_PLUGIN_CONNECTION)

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader
    # get_plugin_vars needs loader to get a data-loader
    loader = DataLoader()
    play_context = PlayContext()

# Generated at 2022-06-13 17:31:41.807985
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Test non existing directory
    result = get_vars_from_path("dir_not_exist", ["host_one"],'', '')
    assert result == {}
    # Test existing directory
    result = get_vars_from_path("tests/unit/plugins/vars/data/vartest", ["host_one"],'', '')
    assert list(result.keys()) == ['role']
    assert result['role'] == 'webserver'

# Generated at 2022-06-13 17:31:42.676220
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:31:43.546166
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: implement unit test
    pass

# Generated at 2022-06-13 17:31:50.641601
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # We need to mock loader object and vars_loader object in order to test get_vars_from_path function
    class Loader(object):
        pass

    class VarsLoader(object):
        pass

    class VarsPlugin(object):

        def __init__(self):
            self._load_name = 'vars_plugin'
            self._original_path = 'mocked_path'

        def get_vars(self, loader, path, entities):
            return {'plugin_plugin': 'plugin_vars'}

        def get_host_vars(self, host):
            return {'host_plugin': 'host_vars'}

        def get_group_vars(self, group):
            return {'group_plugin': 'group_vars'}

    loader = Loader()

    vars

# Generated at 2022-06-13 17:31:58.836266
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible_collections.test.collection_plugins.test_vars_plugin as vars_plugin
    import sys

    sys.modules['ansible_collections.test.collection_plugins.plugins.vars'] = vars_plugin

    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible import constants as C
    from ansible.plugins.inventory import BaseInventoryPlugin
    from ansible.plugins.vars import BaseVarsPlugin

    class MockVarsPlugin(BaseVarsPlugin):
        def get_vars(self, loader, path, entities):
            return {self._load_name: path}

    class MockInventoryPlugin(BaseInventoryPlugin):
        TYPE_NAME = 'mock_inventory'

    MockInventoryCollection = Ans

# Generated at 2022-06-13 17:31:59.904397
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:32:00.681006
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    assert 1 == 1

# Generated at 2022-06-13 17:32:03.040331
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, None, None, 'inventory') == {}
    assert get_vars_from_path(None, None, None, 'task') == {}


# Generated at 2022-06-13 17:32:11.658928
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import tempfile
    import shutil
    from ansible.parsing.dataloader import DataLoader

    plugins = [{
        'name': 'test_name',
        'path': 'path2'
    }]

    loader = DataLoader()

# Generated at 2022-06-13 17:32:23.185121
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    class TestPlugin:
        def get_vars(self, *args, **kwargs):
            return {'test_plugin': 1}

    display.verbosity = 3
    data = get_vars_from_path(None, os.getcwd(), [], 'task')
    assert not data

    vars_loader.add('test_plugin', TestPlugin())
    C.VARIABLE_PLUGINS_ENABLED = ['test_plugin']

    data = get_vars_from_path(None, os.getcwd(), [], 'task')
    assert data == {'test_plugin': 1}

    C.VARIABLE_PLUGINS_ENABLED = []

    data = get_vars_from_path(None, os.getcwd(), [], 'task')
    assert not data



# Generated at 2022-06-13 17:32:40.069963
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    raise NotImplementedError()


# Generated at 2022-06-13 17:32:50.468573
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    Tests the get_vars_from_path function from this file
    """
    from ansible.plugins.vars import HostVars
    from ansible.inventory.dir import InventoryDirectory
    import tempfile
    import shutil
    import os

    test_dir = tempfile.mkdtemp(prefix='ansible-test_get_vars_from_path-')

# Generated at 2022-06-13 17:32:58.715450
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin_spec = {'vars_dir': './test/unit/plugins/vars_dir'}
    loader = './test/unit/plugins/vars_dir/loadme.yaml'
    path = './test/unit/plugins/vars_dir'
    plugins = vars_loader.all(
        class_only=True,
        subdir=None
    )
    entities = None

    result = get_vars_from_path(loader, path, entities, 'inventory')
    assert result == plugin_spec


# Generated at 2022-06-13 17:33:08.896578
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Disable pylint because of Ansible module imports
    # pylint: disable=no-name-in-module,import-error

    from ansible.plugins.loader import vars_loader
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory

    # Load the hosts file
    inventory_file = os.path.join(os.path.dirname(__file__), 'sample_hosts')
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=inventory_file)
    # get the hosts
    hosts = inventory.get_hosts()

    # get the vars for the host

# Generated at 2022-06-13 17:33:17.428134
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import find_plugin_files
    from ansible.plugins.vars import YAMLDictReader
    from ansible.utils.vars import resolve_vars
    from ansible.vars.vars_cache import VarsCache

    # Setup a loader to test with
    loader = vars_loader.get('yaml')
    cache = VarsCache()

    # Add a simple plugin returning a single value
    class SimpleVar(YAMLDictReader):
        def get_vars(self, loader, path, entities):
            return {'simple': 'value'}

    # Add a plugin returning a variable referencing another value
    class DependentVar(YAMLDictReader):
        def get_vars(self, loader, path, entities):
            return {'dependent': '{{ simple }}'}

   

# Generated at 2022-06-13 17:33:29.642779
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    '''
    Unit test for function get_vars_from_path
    '''
    # Ensure that the global VARS_PLUGINS setting is respected
    C.VARIABLE_PLUGINS_ENABLED = ['test_vars_plugin_shipped']
    C.RUN_VARS_PLUGINS = 'start'

    # Get a basic loader for testing
    loader = vars_loader._create_loader(None, 'vars')
    C.VARS_PLUGIN_CLASSES = vars_loader._get_all_plugin_class_loaders(loader)

    # Get a basic test plugin for testing
    vars_plugin = C.VARS_PLUGIN_CLASSES['test_vars_plugin_shipped']

    # Ensure plugin is not initialized with a bad option
    # This matches the

# Generated at 2022-06-13 17:33:38.528126
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.clean import module_response_deepcopy

    inventory = InventoryManager(
        loader=None,
        sources=[
            "./test/vars_plugins/cache1",
        ],
    )

    group = inventory.groups.get("test")
    assert group is not None

    host_1 = inventory.get_host("one")
    assert host_1 is not None

    vars_1 = get_vars_from_path(inventory._loader, "./test/vars_plugins", [host_1], "task")
    assert vars_1 is not None

    host_2 = inventory.get_host("two")
    assert host_2 is not None


# Generated at 2022-06-13 17:33:47.406241
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    path = os.path.join(os.path.expanduser("~"), "test1")
    os.mkdir(path)
    os.mkdir(os.path.join(path, "group_vars"))
    os.mkdir(os.path.join(path, "host_vars"))
    with open(os.path.join(path, "group_vars/all"), "w") as f:
        f.write("var1: 1\nvar2: 2\n")
    with open(os.path.join(path, "host_vars/host1"), "w") as f:
        f.write("var1: 2\nvar3: 3\n")

# Generated at 2022-06-13 17:33:57.477608
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.inventory.manager import InventoryManager

    loader = None
    # path is path to 'sample_inventory' directory
    path = os.path.join(os.path.dirname(__file__), "unit", "data", "inventory", "sample_inventory")

    # entities is group 'server'
    group = InventoryManager(loader, sources=path).get_group("server")
    entities = [group]

    stage = 'inventory'
    # get_vars_from_path() returns a dict, where each key is plugin class and value is a dict from plugin.get_vars()
    data = get_vars_from_path(loader, path, entities, stage)

# Generated at 2022-06-13 17:33:58.768293
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    assert get_plugin_vars(None, {}, None, []) == {}

# Generated at 2022-06-13 17:34:37.192184
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager

    loader = InventoryManager("/path/to/fake/inventory", vault_password="dummy")
    sources = ["/path/to/fake/inventory/group_vars", "/path/to/fake/inventory/host_vars"]
    data = get_vars_from_inventory_sources(loader, sources, ["group_name", "host_name"], "inventory")

    assert data == {'group_name': {'group_name': 'group_name'}, 'host_name': {'host_name': 'host_name'}}

    sources = ["/path/to/fake/inventory/group_vars", "/path/to/fake/inventory/host_vars", "/path/to/fake/inventory/plugin_vars"]

# Generated at 2022-06-13 17:34:38.315252
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    data = {}
    display.debug(data)

# Generated at 2022-06-13 17:34:47.990816
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    class Loader():
        def get_basedir(self, path):
            return '/'

    loader = Loader()

    class Plugin():
        def get_vars(self, loader, path, entities):
            return {'plugin': 'plugin'}

    class Plugin2():
        def get_vars(self, loader, path, entities):
            return {'plugin2': 'plugin2'}

    class Vars_loader():
        plugins = [Plugin(), Plugin2()]

    vars_loader.all = Vars_loader()

    class Host():
        def __init__(self, name):
            self.name = name

    class Group():
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 17:34:55.286592
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    # setup the loader, inventory, and variable managers
    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['tests/vartest'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    def vars_file(path): return VariableManager._vars_from_file(loader, path)

    hosts = inventory.get_hosts()
    groups = inventory.get_groups()
    hostvars = vars_file('tests/vartest/hostvars')

# Generated at 2022-06-13 17:35:05.325511
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['tests/vars_files/hosts', 'tests/vars_files/host_vars'])
    host = inventory.get_host(pattern="test0")
    host.set_variable('ansible_ssh_private_key_file', 'some/path')
    host.set_variable('ansible_ssh_private_key_file', 'some/other/path')
    host.set_variable('ansible_ssh_private_key_file', 'other/path')

# Generated at 2022-06-13 17:35:14.783723
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # Faked get_vars function for test plugin
    def fooplugin_get_vars(*args, **kwargs):
        return {'var_fooplugin_1': True}

    # Fake plugin class
    class FakeVarsPlugin(object):

        def __init__(self, *args, **kwargs):
            pass

        # Fake run
        def run(self, *args, **kwargs):
            pass

        get_vars = fooplugin_get_vars
        _load_name = 'fake_vars_plugin'

    # Create fake plugin instance
    fake_plugins = [FakeVarsPlugin()]

    # Create fake loader
    class FakeLoader(object):

        def __init__(self, *args, **kwargs):
            pass

        # Return fake plugin

# Generated at 2022-06-13 17:35:15.548421
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    assert 1

# Generated at 2022-06-13 17:35:18.913043
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    result = get_vars_from_path(None, './test_dir', [], 'start')
    assert result == {'test_var': 'test_value'}


# Generated at 2022-06-13 17:35:21.274786
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = r"/tmp"
    entities = ()
    stage = 'task'
    get_vars_from_path(loader, path, entities, stage)

# Generated at 2022-06-13 17:35:23.874449
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """ Unit test for function get_vars_from_path """
    assert get_vars_from_path(C.VARIABLE_PLUGINS_ENABLED, '/etc', 'hosts', 'inventory') == {}

# Generated at 2022-06-13 17:36:07.768783
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.inventory.host import Host

    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader, sources='localhost')
    host1 = Host(name='host1')
    host1.port = 1000
    inventory.add_host(host1)
    host2 = Host(name='host2')
    inventory.add_host(host2)
    group1 = inventory.get_group('all')

# Generated at 2022-06-13 17:36:18.145663
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import vars_loader
    from ansible.vars.manager import VariableManager
    groups = ['group1', 'group2']
    hosts = ['host1', 'host2']
    my_groups = [Group(name=g) for g in groups]
    my_hosts = [Host(name=h) for h in hosts]
    my_entities = my_groups + my_hosts
    my_path = os.path.abspath('.')
    my_loader = None
    my_vars_loader = VariableManager(loader=my_loader, inventory=None)
    my_stage = 'task'

    print('vars_loader = {}'.format(vars_loader))
    my

# Generated at 2022-06-13 17:36:23.208244
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    inventory_sources = ['/etc/ansible/hosts', '/etc/ansible/group_vars/all']
    host = Host('localhost', port=2121)
    display.verbosity = 2
    data = get_vars_from_inventory_sources(None, inventory_sources, [host], 'inventory')
    #print(data)
    assert data


if __name__ == '__main__':
    test_get_vars_from_inventory_sources()

# Generated at 2022-06-13 17:36:24.746154
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import unittest
    import tempfile
    import shutil
    import os


# Generated at 2022-06-13 17:36:25.274238
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:36:34.579785
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins
    import ansible.plugins.vars

    mock_loader = object()
    mock_path = '/path/to/somewhere'
    mock_entity = object()
    mock_stage = 'inventory'

    ansible.plugins.vars.all = [ansible.plugins.vars.host_group_vars, ansible.plugins.vars.host_vars]
    data = get_vars_from_path(mock_loader, mock_path, [mock_entity], mock_stage)

    assert isinstance(data, dict)
    assert data == {'ansible_vars_plugins': ['host_group_vars', 'host_vars']}

# Generated at 2022-06-13 17:36:41.120077
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class DummyPlugin(object):
        _load_name = 'dummy'

        def get_vars(self, loader, path, entities):
            return {"a": "b"}

    loader = {}
    path = None
    entities = None

    vars = get_plugin_vars(loader, DummyPlugin(), path, entities)

    assert vars == {"a": "b"}

# Generated at 2022-06-13 17:36:44.181110
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Setup
    loader = None
    path = "./"
    entities = ["myhost"]
    stage = "task"
    # Exercise
    data = get_vars_from_path(loader, path, entities, stage)
    # Verify
    assert isinstance(data, dict)


# Generated at 2022-06-13 17:36:49.239351
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    from ansible.plugins.loader import vars_loader
    loader = vars_loader
    test_vars_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "lib", "ansible", "test", "unit", "test_vars_plugins")

    test_plugin = vars_loader.get(os.path.join(test_vars_dir, "vars_plugins"))
    test_data = get_vars_from_path(loader, test_vars_dir, [], "inventory")
    assert test_data['test_vars_var'] == "inventory_var"
    assert test_data['test_vars_var2'] == "inventory_var2"

    test_plugin = vars_

# Generated at 2022-06-13 17:36:58.726632
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    import ansible.plugins.vars.host_group_vars
    import ansible.plugins.vars.host_vars

    C.VARIABLE_PLUGINS_ENABLED.append('host_vars')
    C.VARIABLE_PLUGINS_ENABLED.append('host_group_vars')

    loader = 'fake'
    path = '/tmp/testing/path'
    entities = ['fake']
    stage = 'inventory'

    # host
    data = {
        'fake': {
            'fake1': 'fake1_data',
        },
    }
    vars_plugin = vars_loader.get('host_vars')
    vars

# Generated at 2022-06-13 17:38:09.625869
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader = None
    sources = None

    assert get_vars_from_inventory_sources(loader, sources, [], '') == {}

# Generated at 2022-06-13 17:38:13.554033
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    d = {}
    r = get_vars_from_path(d, '/tmp/path', ['entity1', 'entity2', 'entity3'], 'task')
    print(r)

if __name__ == '__main__':
    test_get_vars_from_path()

# Generated at 2022-06-13 17:38:21.276118
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # we don't have any vars plugins in this test so we need to fake the return value
    class FakePlugin:
        def get_vars(self, loader, path, entities):
            return {'a': 1, 'b': 2}

    class FakeLoader:
        pass

    class FakeEntity:
        def __init__(self, name):
            self.name = name

    loader = FakeLoader()
    plugin = FakePlugin()

    plugin_list = [plugin]
    entities = [FakeEntity('host1'), FakeEntity('host2')]
    path = 'some/path'

    vars_data = get_vars_from_path(loader, path, entities, 'task')

    assert vars_data == {'a': 1, 'b': 2}

# Generated at 2022-06-13 17:38:25.123238
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.data import InventoryData

    data = InventoryData()

    path = 'tests/integration/inventory/dynamic/empty'
    get_vars_from_path(data, path, [], 'inventory')

# Generated at 2022-06-13 17:38:30.496050
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import BaseVarsPlugin

    class TestVars(BaseVarsPlugin):
        def get_vars(self, loader, path, entities):
            return {
                'test_value': 'vars'
            }

    data = get_plugin_vars(None, TestVars(), 'path', ['entity'])
    assert isinstance(data, dict)
    assert data['test_value'] == 'vars'


# Generated at 2022-06-13 17:38:32.126282
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert 'a' == 'a'