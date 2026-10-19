

# Generated at 2022-06-13 17:28:56.333112
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # First create a vars plugin with only the run method
    class Vars_Plugin(object):
        def run(self):
            return dict(plugin_run=2)

        def get_vars(self, loader, path, entities):
            return dict(plugin_vars=3)

    # Now try to get the vars from the path
    loader, inventory, path, entities = None, None, None, None

    # Add the Vars_Plugin to vars_loader
    vars_loader._all[type(Vars_Plugin())] = Vars_Plugin()

    # Now try to get the vars from the path
    varsdata = get_vars_from_path(loader, path, entities, 'start')

    # Check that the vars are correct
    assert varsdata['plugin_vars'] == 3

# Generated at 2022-06-13 17:29:07.312231
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import from_yaml
    from tests.unit.mock.loader import DictDataLoader
    from tests.unit.vars.test_nested_vars import YamlVarsPlugin

    plugin = YamlVarsPlugin()

# Generated at 2022-06-13 17:29:12.918326
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugin_base
    from .mock.loader import DictDataLoader

    class MockPlugin(vars_plugin_base):
        def __init__(self):
            self._load_name = 'MyMockPlugin'

        def get_vars(self, loader, path, entities):
            return {'a': 1, 'b': 2}

    loader = DictDataLoader({'vars_dir': {}, 'host_vars': {}, 'group_vars': {}})

    results = get_plugin_vars(loader, MockPlugin(), 'vars_dir', [])
    assert results == {'a': 1, 'b': 2}



# Generated at 2022-06-13 17:29:23.286277
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.host_group_vars
    plugin = ansible.plugins.vars.host_group_vars.VarsModule()
    plugin.get_host_vars = lambda x: {'host_var_value': x}
    plugin.get_group_vars = lambda x: {'group_var_value': x}

    plugin._load_name = 'HostGroupVars'
    plugin._original_path = '__main__'
    loader = None
    path = os.path.join(os.path.dirname(__file__), 'data')
    entities = [Host('host1'), 'group1']

    var_dict = get_plugin_vars(loader, plugin, path, entities)
    assert var_dict['host_var_value'] == 'host1'

# Generated at 2022-06-13 17:29:34.704215
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    inventory = '''
all:
  vars:
    var3: "ok"
hosts:
  host1:
    ansible_host: "127.0.0.1"
  host2:
    ansible_host: "127.0.0.1"
hosts1:
  host1:
    ansible_host: "127.0.0.1"
    var1: "ok"
  host2:
    ansible_host: "127.0.0.1"
hosts2:
  host1:
    ansible_host: "127.0.0.1"
  host2:
    ansible_host: "127.0.0.1"
    var2: "ok"
'''

# Generated at 2022-06-13 17:29:45.291851
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin_dir = 'lib/ansible/plugins/vars'
    plugin_name = 'test_plugin.py'
    plugin_path = os.path.join(plugin_dir, plugin_name)
    # Create an empty vars plugin.
    if not os.path.isdir(plugin_dir):
        os.makedirs(plugin_dir)
    with open(plugin_path, 'w'):
        # No content
        pass
    loader = vars_loader._get_plugins()
    plugin = loader.get(plugin_name[:-3])
    assert plugin is not None
    os.remove(plugin_path)
    os.rmdir(plugin_dir)

# Generated at 2022-06-13 17:29:48.909426
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    loader, inventory, sources, entities, stage = 'loader', 'inventory', 'sources', ['entities'], 'stage'

    vars = {'PATH': 'http://www.ansible.com'}

    vars_plugin_list = list(vars_loader.all())
    for plugin in vars_plugin_list:
        if plugin._load_name != 'vars_plugin':
            vars.update(get_plugin_vars(loader, plugin, 'path', entities))

    vars_from_sources = get_vars_from_inventory_sources(loader, sources, entities, stage)

    assert vars == vars_from_sources

# Generated at 2022-06-13 17:29:55.508682
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    entities = None
    stage = 'inventory'
    data = get_vars_from_path(loader, path, entities, stage)
    assert isinstance(data, dict)
    # print("test_get_vars_from_path:", data)


# Generated at 2022-06-13 17:30:03.774051
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    host = Host("")

    # Test with RUN_VARS_PLUGINS = 'all'
    with open("/tmp/test.yml", "w") as f:
        f.write("test: yes\n")
    # add myvars plugin
    from ansible.plugins.vars.myvars import VarsModule as myvars
    vars_loader.add("/tmp/test.yml", myvars)
    sources = ["/tmp/test.yml"]
    entities = [host]
    result = get_vars_from_inventory_sources(None, sources, entities, "inventory")
    assert result == {'test': 'yes'}
    os.remove("/tmp/test.yml")

    # Test with RUN_VARS_PLUGINS = 'demand'

# Generated at 2022-06-13 17:30:07.478155
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Note: Loader is currently not instantiated in any other way in the codebase.
    #       If that changes, this will need to be changed as well.
    loader = vars_loader
    entities = []
    stage = ''
    path = ''

    assert get_vars_from_path(loader, path, entities, stage) == {}

# Generated at 2022-06-13 17:30:15.452669
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = 'ansible.inventory.manager'
    path = 'ansible/inventory'
    entities = Host, Host
    stage = 'inventory'

    assert get_vars_from_path(loader, path, entities, stage) is not None

# Generated at 2022-06-13 17:30:16.436602
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    pass


# Generated at 2022-06-13 17:30:22.179308
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Import this later to avoid circular dependency.
    from units.compat import unittest
    from units.mock.loader import DictDataLoader, DictModuleFinder


# Generated at 2022-06-13 17:30:23.269868
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path([]) == {}

# Generated at 2022-06-13 17:30:34.193581
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class VarsPlugin:
        def __init__(self):
            self.name = 'VarsPlugin'

        def get_vars(self,loader,path,entities):
            return {self.name: 'test'}

    class OldVarsPlugin:
        def __init__(self):
            self.name = 'OldVarsPlugin'

        def get_host_vars(self,host):
            return {self.name: 'test'}

        def get_group_vars(self,host):
            return {self.name: 'test'}

    class InvalidVarsPlugin:
        def __init__(self):
            self.name = 'InvalidVarsPlugin'

        pass

    loader = None
    plugin = VarsPlugin()
    path = None
    entities = []
    out = get_plugin_

# Generated at 2022-06-13 17:30:44.936246
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import test_vars_plugin
    loader = vars_loader

    loader.add_directory(os.path.join(C.DEFAULT_MODULE_PATH, "vars_plugins"), with_subdir=True)

    plugin = vars_loader.get("test_vars_plugin")
    path = '/my/path'
    entities = ['foo', 'bar']

    data = get_plugin_vars(loader, plugin, path, entities)


# Generated at 2022-06-13 17:30:55.006291
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Setup testing environment
    class FakePlugin:
        def __init__(self, name):
            self.info_name = 'info_' + name
            self.name =  name

        def get_vars(self, loader, path, entities):
            return {self.info_name: {'path': path, 'entities': entities, 'name': self.name}}

        def get_host_vars(self, name):
            return {self.info_name: {'host': name}}

        def get_group_vars(self, name):
            return {self.info_name: {'group': name}}

    class FakeLoader:
        pass

    class FakeHost:
        def __init__(self, name):
            self.name = name
        pass


# Generated at 2022-06-13 17:31:02.268273
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.constants import get_config

    config = get_config()
    config.settings['inventory'] = 'tests/units/vars/inventory'
    config.settings['load_callback_plugins'] = []
    config.settings['load_callback_whitelist'] = []
    config.settings['load_filter_plugins'] = []
    config.settings['load_filter_whitelist'] = []
    config.settings['load_lookup_plugins'] = []
    config.settings['load_lookup_whitelist'] = []
    config.settings['load_module_plugins'] = []
    config.settings['load_module_whitelist'] = []
    config.settings['load_plugins'] = False
    config.settings['module_path'] = ['./library', './module_utils']
    config.settings

# Generated at 2022-06-13 17:31:09.427000
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # Let us use atleast one of the plugin - json
    import ansible.plugins.vars.json
    plugin = ansible.plugins.vars.json.VarsModule()
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    plugin.parse(loader, os.path.join(curr_dir, "../../../../test/legacy/inventory/dynamic_inventory/test_json"), [])
    data = get_plugin_vars(loader, plugin, curr_dir, [])
    assert data.get("json") == "data"

# Generated at 2022-06-13 17:31:17.677544
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager

    inventory_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + '..' + os.sep + 'inventory'

    inventory_object = InventoryManager(loader=None, sources=inventory_dir + os.sep + 'test_inventory.yml')
    vars_object = inventory_object.get_vars(host=None, include_hostvars=False)

    display.deprecated('Using the get_vars method on the base inventory is deprecated. '
                       'This functionality will be moved in Ansible 2.15.',
                       version='2.15')

# Generated at 2022-06-13 17:31:26.907286
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Tests that the vars from path will work with a single file
    from ansible.plugins.loader import vars_loader

    path = os.path.join(C.DEFAULT_LOCAL_TMP, "fake_host.yml")
    yaml_data = {
        "vars": {
            "foo": "bar"
        }
    }
    vars_loader.add_directory(path, yaml_data, 'yaml')

    loader = DictDataLoader({'inventory': [path]})
    result = get_vars_from_inventory_sources(loader, loader.get_basedir_list(), ['test1'], 'inventory')
    assert result == {'foo': 'bar'}



# Generated at 2022-06-13 17:31:31.635620
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    import os
    import shutil
    import tempfile
    import unittest

    class TestNoVars(object):
        _load_name = 'no_vars'
        _original_path = '/path/to/collection/no_vars'

    class TestVarsNoEntities(object):
        _load_name = 'vars_no_entities'
        _original_path = '/path/to/collection/vars_no_entities'

        def get_vars(self, loader, path, entities, cache=True):
            return {'value': 'vars_no_entities'}

    class TestVarsEntities(object):
        _load_name = 'vars_entities'
        _original_path = '/path/to/collection/vars_entities'


# Generated at 2022-06-13 17:31:38.783171
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def assert_vars_in_data(path, entities, stage, plugin_name, plugin_data):
        loaded_vars = get_vars_from_path(None, path, entities, stage)
        assert loaded_vars[plugin_name] == plugin_data

    assert_vars_in_data('/foo/bar/baz', [], 'inventory', 'test', {'test': 'data'})

    # Just make sure v1 plugins don't blow up.
    def v1_plugin():
        class VarsModule(object):
            pass
        return VarsModule
    class MockLoader:
        def get_all(self):
            return [v1_plugin()]
    assert_vars_in_data('/foo/bar/baz', [], 'inventory', 'VarsModule', {})

# Generated at 2022-06-13 17:31:49.499609
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class MockVarsPlugin1:
        def get_vars(self, loader, path, entities):
            return {'test': 'mock1'}
    class MockVarsPlugin2:
        def get_host_vars(self, host):
            return {'test': 'mock2'}
        def get_group_vars(self, group):
            return {}
    class MockVarsPlugin3:
        def run(self):
            pass
    class MockVarsPlugin4:
        def get_vars(self, loader, path, entities):
            return {'test': 'mock4'}
        def get_host_vars(self, host):
            return {'test': 'mock4'}

# Generated at 2022-06-13 17:32:00.568908
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    import ansible.inventory.manager
    from ansible.vars.editor import ChildLoader

    class DummyPlugin:
        def get_option(self, key):
            pass

    inventory = ansible.inventory.manager.InventoryManager(loader=None, sources=[])
    loader = ChildLoader(inventory, '/dev/null')

    p1 = DummyPlugin()
    p1._load_name = 'p1'
    p1._original_path = '/path/to/p1'
    p1.get_vars = lambda x, y, z: {'p1': True, 1: True}

    p2 = DummyPlugin()
    p2._load_name = 'p2'
    p2._original_path = '/path/to/p2'

# Generated at 2022-06-13 17:32:01.440469
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: Implement
    pass


# Generated at 2022-06-13 17:32:08.510843
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    test_path = '/path/to/vars/plugin'
    test_plugin_name = 'test.vars.plugin'
    test_entities = ['foo', 'bar']
    test_data = {'var1': 'foo', 'var2': 'bar'}

    class mock_plugin:
        def __init__(self):
            self._load_name = test_plugin_name
        def has_option(self, opt):
            return False
        def get_vars(self, loader, path, entities):
            if path == test_path and entities == test_entities:
                return test_data
            else:
                raise Exception('get_vars called with unexpected parameters')


# Generated at 2022-06-13 17:32:09.052716
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:32:13.730772
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    # Define sources, entities, stage
    sources = ['/etc/ansible/hosts']
    class Host2(Host):
        def __init__(self, name):
            self.name = name
    entities = [Host2('host1')]
    stage = 'task'

    # import required modules for function
    from ansible.plugins.loader import vars_loader

    # Test function
    assert get_vars_from_inventory_sources(vars_loader, sources, entities, stage)



# Generated at 2022-06-13 17:32:18.034994
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = '..'
    entities = None
    stage = 'inventory'
    result = get_vars_from_path(loader, path, entities, stage)
    assert "vars_plugin_list" not in result

# Generated at 2022-06-13 17:32:28.410070
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    hosts = {}

    loader = None
    plugin = vars_loader.get('yaml_file')

    group = Group('rg1')
    hosts['rg1'] = group

    host = Host('h1')
    hosts['h1'] = host
    group.add_host(host)

    host = Host('h2')
    hosts['h2'] = host
    group.add_host(host)

    path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'units', 'plugins', 'vars', 'yaml_file')


# Generated at 2022-06-13 17:32:38.036228
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import sys
    import shutil
    import tempfile
    import ansible.constants as C
    import ansible.utils.collection_loader

    # Setup temp directory
    tmpdir = tempfile.mkdtemp()
    ansible_alias = os.path.join(tmpdir, 'ansible_alias.yml')

    # Setup collections
    collections_paths = C.COLLECTIONS_PATHS + [tmpdir]
    ansible.utils.collection_loader._create_collections_cache(collections_paths)

    # Setup mock vars plugin

# Generated at 2022-06-13 17:32:44.473045
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.vars import TestVarsPlugin

    loader = []
    path = '/tmp/my_path'
    c = [VarsCollection()]

    # Test without error
    test_values = [{'foo': 'bar1'}, {'foo': 'bar2'}]
    v1 = TestVarsPlugin()
    v1.vars = test_values[0]
    v2 = TestVarsPlugin()
    v2.vars = test_values[1]
    C.VARIABLE_PLUGINS_ENABLED = [v1._load_name, v2._load_name]

    data = get_vars_from_path(loader, path, c, 'task')

    assert data == {'foo': 'bar2'}

    # Test with 2.x plugin
   

# Generated at 2022-06-13 17:32:49.115526
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    variable_manager = VariableManager(loader=loader)

    paths = [None]
    entities = [Host('testwebsite')]
    stage='inventory'

    get_vars_from_path(loader, None, entities, stage)

# Generated at 2022-06-13 17:32:49.693589
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    return None

# Generated at 2022-06-13 17:32:55.044731
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    a = {"a": "b"}
    b = {"b": "c"}
    c = {"a": "b", "c": "d"}
    d = {}

    assert a == get_vars_from_path("loader", "path", "entities", "stage")
    assert a == get_vars_from_path("loader", "path", "entities", "stage")
    assert c == get_vars_from_path("loader", "path", "entities", "stage")
    assert d == get_vars_from_path("loader", "path", "entities", "stage")

# Generated at 2022-06-13 17:33:00.154139
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import collection_loader

    fake_loader = collection_loader.all()

    from ansible.plugins.vars import dir_vars

    fake_plugin = dir_vars.VarsModule()


    fake_path = '/home/fake'

    fake_entities = ['fake1', 'fake2', 'fake3']

    fake_data = {'fake1': {'k1': 'v1'}, 'fake2': {'k2': 'v2'}}

    fake_new_data = {'fake3': {'k3': 'v2'}}

    fake_new_data2 = {'fake2': {'k2': 'v2'}}

    assert {} == get_plugin_vars(fake_loader, fake_plugin, fake_path, fake_entities)

    fake

# Generated at 2022-06-13 17:33:00.661905
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:33:04.487086
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert set(get_vars_from_path(None, "", None, "").keys()) == set(['inventory_dir', 'inventory_file'])

# Generated at 2022-06-13 17:33:12.855660
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.config.manager import ConfigManager

    config = ConfigManager()

    # clear plugin directories
    config.setenv('ANSIBLE_VARIABLE_PLUGINS_DIR', '')

    # clear env variables
    config.remove_option('VARIABLE_PLUGINS_ENABLED')
    config.setenv('ANSIBLE_VARIABLE_PLUGINS_ENABLED', '')
    config.remove_option('RUN_VARS_PLUGINS')
    config.setenv('ANSIBLE_RUN_VARS_PLUGINS', '')
    config.remove_option('INVENTORY_ENABLED')
    config.setenv('ANSIBLE_INVENTORY_ENABLED', '')

    # set INI vars

# Generated at 2022-06-13 17:33:32.935403
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    testfile = os.path.join(os.path.dirname(__file__), 'data', 'vars_plugin_data.yml')
    collection_loader = vars_loader.get('collection')
    data = get_vars_from_path(collection_loader, testfile, entities=['all'], stage='task')
    expected_data = {'test_host': 'host1', 'test_group': 'group1', 'test_included': 'included'}
    assert data == expected_data

# Generated at 2022-06-13 17:33:42.769235
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible_collections.ansible.community.tests.unit.plugins.test_vars import VarsModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    plugin = VarsModule()
    plugin.get_vars = lambda x, y, z: {'vars_from_get_vars': '1'}

    loader.set_basedir('/')
    vars = get_plugin_vars(loader, plugin, 'abs_path', [])
    assert vars == {'vars_from_get_vars': '1'}

    loader.set_basedir('/')
    vars = get_plugin_vars(loader, plugin, 'abs_path', ['entity'])
    assert v

# Generated at 2022-06-13 17:33:52.056477
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader)
    inv_manager.add_group('test')
    inv_manager.add_host('test-host', 'test')

    assert get_vars_from_path(loader, '/non-existing-directory', [inv_manager.groups['test']], 'inventory') == {}

    # /etc/ansible/group_vars/test
    assert get_vars_from_path(loader, '/etc/ansible/group_vars', [inv_manager.groups['test']], 'inventory') == {
        'group_name': 'test',
    }

    # /etc/ansible/host_vars/test-host


# Generated at 2022-06-13 17:33:59.344366
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    data = {'key1': 'value1', 'key2': 'value2'}

    class MockVarsPlugin:
        def __init__(self):
            self.vars_dict = data

        def get_vars(self, loader, path, entities, cache=True):
            return self.vars_dict

    mock_plugin = MockVarsPlugin()
    loader = None
    path = 'fake_path'
    entities = []
    stage = 'start'

    assert get_vars_from_path(loader, path, entities, stage) == data



# Generated at 2022-06-13 17:34:02.474698
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: create a fake loader, plugin and path
    loader = None
    path = "/tmp"
    entities = []
    stage = "inventory"
    get_vars_from_path(loader, path, entities, stage)

# Generated at 2022-06-13 17:34:04.751070
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, '/etc', [], 'inventory') == {}

# Generated at 2022-06-13 17:34:15.280716
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # This is mostly a test of the test code, to verify
    # that the plugin loader will work as expected
    # when presented with a list of known vars plugins
    # which include the vars plugins which ship with
    # Ansible itself, as well as any additional vars
    # plugins that may have been found in the
    # 'vars_plugins' directory in the configured
    # Ansible 'plugin' directory
    vars_plugin_list = list(vars_loader.all())
    assert len(vars_plugin_list) > 0

    from ansible.plugins.vars import base
    assert base in vars_plugin_list

    for plugin in vars_plugin_list:
        print(plugin)
        if hasattr(plugin, 'get_vars'):
            assert 1 == 1

# Generated at 2022-06-13 17:34:16.496941
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, None, None, None) is not None

# Generated at 2022-06-13 17:34:17.034955
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    pass

# Generated at 2022-06-13 17:34:18.178089
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, '/', [], 'inventory') == {}

# Generated at 2022-06-13 17:34:31.551404
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader, path, entities = object(), object(), object()
    assert get_vars_from_path(loader, path, entities) is not None
    assert get_vars_from_path(loader, path, entities) == {}

# Generated at 2022-06-13 17:34:43.444172
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import base
    from ansible.plugins.loader import vars_loader

    class Plugin1(object):
        def get_vars(self, loader=None, path=None, entities=None):
            return {'plugin_var1': 'plugin_val1'}

    class Plugin2(object):
        def get_host_vars(self, host):
            return {'plugin_var2': 'plugin_val2'}

    class Plugin3(object):
        def get_group_vars(self, group):
            return {'plugin_var3': 'plugin_val3'}


# Generated at 2022-06-13 17:34:49.429225
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.yaml
    loader = ansible.plugins.vars.yaml.VarsModule()
    path = os.path.dirname(__file__)
    host = Host('test')
    entities = [host]
    data = get_vars_from_path(loader, path, entities, 'inventory')
    assert data is not None

# Generated at 2022-06-13 17:34:50.313706
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert False, 'This function is not yet tested.'

# Generated at 2022-06-13 17:35:01.575044
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.plugin_docs import read_vars_plugin_docs

    loader = vars_loader._create_loader(paths=C.DEFAULT_VARS_PLUGIN_PATH, package=C.DEFAULT_VARS_PLUGIN_PATH)

    plugin_name = 'test_vars'
    source_path = C.DEFAULT_VARS_PLUGIN_PATH[0]
    plugin_path_name = plugin_name + '.yaml'
    plugin_path = os.path.join(source_path, plugin_path_name)

    # Verify plugin exists
    if not os.path.exists(plugin_path):
        raise AnsibleError("{0} does not exist.".format(plugin_path))

    # Verify

# Generated at 2022-06-13 17:35:02.422717
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    d = get_vars_from_path()

# Generated at 2022-06-13 17:35:12.961344
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import os

    current_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(current_dir, './data/var_plugins')

    # load the inventory
    manager = InventoryManager(loader=None, sources=to_bytes(test_dir + '/inventory'), variable_manager=VariableManager())
    # create a variable manager
    vars_manager = VariableManager(loader=None, inventory=manager)
    # run the vars plugins
    vars = get_vars_from_path(vars_manager._loader, to_bytes(test_dir), [manager.groups['ungrouped'], manager.groups['group1']], 'task')


# Generated at 2022-06-13 17:35:14.905147
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = MockLoader()
    path = None
    entities = []
    stage = 'inventory'

    result = get_vars_from_path(loader, path, entities, stage)
    assert result == {}

# Generated at 2022-06-13 17:35:19.743982
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import unittest.mock as mock

    loader = mock.MagicMock()
    vars_loader.add(loader, 'dummy_plugin')
    data = get_vars_from_path(loader, 'path', {}, 'inventory')
    assert data == {'dummy_plugin': 'yes'}

# Generated at 2022-06-13 17:35:20.245571
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:35:48.527317
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    data = {'test': 'test'}
    # vars_loader.is_empty('')

    fake_loader = {'test': 'test'}
    fake_plugin = {'test': 'test'}
    fake_path = {'test': 'test'}
    fake_entities = {'test': 'test'}

    assert data == get_plugin_vars(fake_loader, fake_plugin, fake_path, fake_entities)



# Generated at 2022-06-13 17:35:51.964949
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, None, None, None) == {}
    assert get_vars_from_path(None, None, None, 'inventory') == {}
    assert get_vars_from_path(None, None, None, 'task') == {}


# Generated at 2022-06-13 17:35:55.846096
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    path = '/'
    entities = ['localhost']
    stage = 'task'
    # Test if data
    data = get_vars_from_path(None, path, entities, stage)
    assert isinstance(data, dict)
    # Test if data is not empty
    assert len(data) > 0

# Generated at 2022-06-13 17:36:00.057783
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.filesystem
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    source = os.path.join(os.path.dirname(__file__), 'test_vars_from_path_folder')
    plugin = ansible.plugins.vars.filesystem.VarsModule()
    path = source
    entities = ["localhost", "groupall_group"]
    stage = "task"
    data = get_vars_from_path(loader, path, entities, stage)
    assert(data['var_all'] == 'var_all_value')

# Generated at 2022-06-13 17:36:04.433890
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader, inventory_loader
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    path = './vars_plugins'
    sources = ['./vars_plugins/group_vars/all.yaml']
    all = inventory_loader.get('all')
    stage = 'inventory'
    data = get_vars_from_path(loader, path, sources, all, stage)
    print(data)


# Generated at 2022-06-13 17:36:15.891227
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class Plugin():
        def __init__(self, plugin_name):
            self._load_name = plugin_name

        def get_vars(self, loader, path, entities):
            return {plugin_name: "test_result"}

        def get_group_vars(self, group_name):
            return {group_name: "test_result"}

        def get_host_vars(self, host_name):
            return {host_name: "test_result"}

    class Loader():
        def __init__(self):
            pass

    class Host():
        def __init__(self, name):
            self.name = name

    class Group():
        def __init__(self, name):
            self.name = name

    class VarsPluginLoader():
        def __init__(self):
            pass

# Generated at 2022-06-13 17:36:24.256968
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars.host_group import VarsModule as VarsGroup
    from ansible.plugins.vars.host_variable import VarsModule as VarsHost
    from ansible.utils.collection_loader import gen_vars_cache_file_name
    from ansible.utils.vars import combine_vars
    from ansible.vars import combine_vars

    data = {}
    plugins = []
    plugins.append(VarsGroup())
    plugins.append(VarsHost())
    for plugin in plugins:
        result = get_plugin_vars(None, plugin, '', [])
        # add in group and host vars
        data = combine_vars(data, result)


# Generated at 2022-06-13 17:36:30.051383
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    test_inventory = InventoryManager(loader=loader, sources="/test_inventory")

    test_vars = get_vars_from_path(test_inventory.loader, "/test_inventory", None, 'inventory')

    assert type(test_vars) is dict



# Generated at 2022-06-13 17:36:38.835975
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    host_file = ["./test/integration/inventory_file/hosts/host_file_with_many_hosts"]
    host_list = [host_file, ",".join(["host2", "host3", "host4"])]
    inv = InventoryManager(loader=None, sources=host_list)
    play = Play().load({'name': 'test play', 'hosts': 'all', 'tasks': []}, variable_manager=None, loader=None)
    tqm = TaskQueueManager(inventory=inv, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None)
    loader

# Generated at 2022-06-13 17:36:39.642304
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: add unit tests
    return

# Generated at 2022-06-13 17:37:29.116412
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    # Test for py files
    for file_ in vars_loader.all():
        try:
            data = get_vars_from_path(None, None, None, None)
            assert isinstance(data, dict)
            assert len(data) > 0
        except Exception as e:
            display.display('Could not load/find vars plugin %s' % str(file_), color='red')
    # Test for ansible collection directory

# Generated at 2022-06-13 17:37:29.677852
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:37:36.144181
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin1 = VarsPlugin()
    plugin1._load_name = 'plugin1'
    plugin2 = VarsPlugin()
    plugin2._load_name = 'plugin2'

    allplugins = {}
    allplugins['plugin1'] = plugin1
    allplugins['plugin2'] = plugin2
    loader = FakeVarsLoaders(allplugins)

    entities = (
        Host(name='host1', port=1234),
        Host(name='host2', port=1234),
        Host(name='host3', port=1234),
    )

    expected = {}
    expected['plugin1'] = plugin1
    expected['plugin2'] = plugin2
    for entity in entities:
        expected['plugin1']['id'] = 'host_id'

# Generated at 2022-06-13 17:37:42.703792
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    sources = []
    sources.append("/etc/ansible/hosts")
    sources.append("/root/ansible/hosts")

    entities = []
    # entities can be host or group
    for i in range(15):
        e = Host("host_" + str(i))
        entities.append(e)

    stage = 'inventory' # inventory or task
    print(get_vars_from_inventory_sources(loader, sources, entities, stage))

# Generated at 2022-06-13 17:37:45.751841
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_loader = None
    test_path = os.getcwd()
    test_entities = {}
    test_stage = 'task'
    result = get_vars_from_path(test_loader, test_path, test_entities, test_stage)
    assert result == {}

# Generated at 2022-06-13 17:37:49.000026
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert(get_vars_from_path(None, 'some/path', ['l1', 'l2'], 'inventory') == {})

# Generated at 2022-06-13 17:37:57.951294
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    host = Host('test_get_vars_from_path')

    # Mock the loader and get_all_files plugin
    class Plugin:
        def get_vars(self, loader, path, entities):
            return {'plugin_key': 'plugin_value'}

    class Loader:
        class VarsModule:
            def get_all_files(self, path):
                return ['/tmp/test_get_vars_from_path']

            def add_directory(self, directory, with_subdir=True):
                return ''

        def all(self):
            return [Plugin()]

    class Ansible:
        class Config:
            class RunOnce:
                VARIABLE_PLUGINS_ENABLED = []
                RUN_VARS_PLUGINS = 'start'


# Generated at 2022-06-13 17:38:04.493989
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class plugin:
        _load_name = "test"
        _original_path = "/home/test/"
        def get_vars(self, loader, path, entities):
            return {"test": True}
    class loader:
        pass

    vars_plugin_list = [plugin]
    for plugin in vars_plugin_list:
        assert get_vars_from_path(loader, "/home/test/", "entities", "inventory") == {"test":True}



# Generated at 2022-06-13 17:38:05.066189
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:38:05.638542
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert 1 == 1