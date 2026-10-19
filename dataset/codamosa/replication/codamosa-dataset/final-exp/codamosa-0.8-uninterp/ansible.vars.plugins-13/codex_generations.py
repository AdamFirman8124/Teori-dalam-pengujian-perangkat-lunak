

# Generated at 2022-06-13 17:28:48.126547
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import sys
    from ansible.utils.vars import combine_vars
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.vars_plugins.test.data import vars_data

    # Change working directory to test directory
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)

    # Setup modules path
    test_module_path = os.path.join(test_dir, 'ansible_collections/notstdlib/moveitallout/plugins/modules/')
    sys.path.insert(0, test_module_path)

    # Get vars from path

# Generated at 2022-06-13 17:28:54.336969
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = MockVarsModule()
    plugin = MockVarsPlugin()
    assert not get_vars_from_path(loader, 'foo', ['a','b','c'], 'inventory')
    plugin._load_name = 'plugin'
    plugin.get_vars = MockGetVars()
    assert get_vars_from_path(loader, 'foo', ['a','b','c'], 'inventory')

# Generated at 2022-06-13 17:29:05.748107
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class FakePlugin:
        def __init__(self, load_name):
            self._load_name = load_name

        def get_vars(self, loader, path, entities):
            if self._load_name == "undefined":
                raise NotImplementedError("not implemented")
            elif self._load_name == "error":
                raise Exception("error")
            else:
                return {self._load_name: self._load_name}

    loader = {}
    plugin_list = []
    plugin_list.append(FakePlugin("plugin1"))
    plugin_list.append(FakePlugin("undefined"))
    plugin_list.append(FakePlugin("error"))
    plugin_list.append(FakePlugin("plugin2"))
    loader["_vars_plugins"] = plugin_list

# Generated at 2022-06-13 17:29:06.329621
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:29:10.879689
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = 'test/test_plugins/test_vars_plugin'
    entities = None
    stage = 'inventory'
    data = get_vars_from_path(loader, path, entities, stage)

    assert data is not None
    assert data == {'test_var': 'test_value'}

# Generated at 2022-06-13 17:29:15.475819
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    ''' ansible.inventory.vars_plugins.get_vars_from_path '''
    # TODO: add tests

    from ansible.plugins import vars_loader
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader

    assert True  # for debug

# Generated at 2022-06-13 17:29:25.511526
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.merge import merge_hash

    inv = InventoryManager(loader=None, sources=['tests/unit/utils/vars_loader/inventory'])

    vars_data = get_vars_from_path(inv._loader, 'tests/unit/utils/vars_loader/inventory', inv.hosts.values(), 'inventory')
    assert merge_hash(vars_data)['test_inventory_plugin'] == 'inventory'

    vars_data = get_vars_from_path(inv._loader, 'tests/unit/utils/vars_loader/inventory', [inv.groups['foo']], 'inventory')
    assert merge_hash(vars_data)['test_inventory_plugin'] == 'inventory'

    vars_data = get_v

# Generated at 2022-06-13 17:29:31.210265
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import load_plugins
    from ansible.utils.collection_loader import _init_collections

    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp(prefix='ansible_test_vars_plugin_')
    print(tmpdir)
    # init vars_loader
    load_plugins()
    # init collection loader
    _init_collections()

    # patch env variable to use temporary directory as collection_path
    os.environ[C.COLLECTIONS_PATHS_ENVAR] = tmpdir
    # create dummy collection and plugin
    collection_dir = os.path.join(tmpdir, 'test_collection')

# Generated at 2022-06-13 17:29:39.154418
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.vars.host_list as var_host_list
    import ansible.plugins.vars.hostvars as var_hostvars
    import ansible.plugins.vars.yaml as var_yaml

    vars_plugin_list = [var_yaml.VarsModule(), var_hostvars.VarsModule(), var_host_list.VarsModule()]

    for plugin in vars_plugin_list:
        plugin_loader.add_directory(os.path.dirname(os.path.abspath(__file__)))
        plugin._load_name = plugin.__class__.__name__
        plugin._original_path = os.path.dirname(os.path.abspath(__file__))


# Generated at 2022-06-13 17:29:49.674580
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    path = "tests/vars_plugins/"
    os.makedirs(path)
    test_data = {
        'a': {'b': 1},
        'b': {'b': 2},
        'c': {'a': {'a': 1, 'b': 2}},
    }

    class FakeVars(object):
        def __init__(self, data):
            self.data = data
        def get_vars(self, *args, **kwargs):
            return self.data

        def get_group_vars(self, *args, **kwargs):
            return self.data

        def get_host_vars(self, *args, **kwargs):
            return self.data

    def fake_get_vars_from_path(loader, path, entities, stage):
        return

# Generated at 2022-06-13 17:29:59.593909
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: Implement this test
    pass


# Generated at 2022-06-13 17:30:06.037170
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    loader, inventory, variable_manager = _init_vars_dir_loader_variable_manager()
    group = inventory.get_group('ungrouped')
    expected_result = {'var1': 'value1', 'var2': 'value2', 'var3': 'value3'}
    assert get_plugin_vars(loader,
                           vars_loader.get(path=os.path.join(DATA_PATH, 'plugins', 'group_vars')),
                           os.path.join(DATA_PATH, 'host_vars'),
                           [group]) == expected_result



# Generated at 2022-06-13 17:30:09.429193
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    This test is meant to make sure that the vars_plugin_list is getting
    populated correctly.
    """
    print(vars_loader.all())
    assert len(vars_loader.all()) > 1

# Generated at 2022-06-13 17:30:19.758230
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class TestVarsPlugin(object):
        def run(self):
            return {'foo': 'bar'}

    class TestVarsPluginV2(object):
        def get_vars(self, loader, path, entities):
            return {'foo': 'bar'}

    loader = vars_loader
    loader.add("test_vars_plugin", TestVarsPlugin())
    loader.add("test_vars_plugin_v2", TestVarsPluginV2())

    data = {'plugin_vars': {}}

    data['plugin_vars'] = combine_vars(data['plugin_vars'], get_vars_from_path(loader, "/tmp/path_1", ["test_vars_plugin"], "task"))
    assert len(data['plugin_vars']) == 0

# Generated at 2022-06-13 17:30:30.600721
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    from ansible.plugins.loader import vars_loader

    plugin_list = vars_loader.get_all()


# Generated at 2022-06-13 17:30:42.145415
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_list import get_collection_list
    from ansible.utils.path import unfrackpath

    data = {}

    #import the module 'test_vars_plugin' in collections
    collections_name = 'ansible_collections.test_namespace.test_collection'
    coll_ref = AnsibleCollectionRef.from_string(collections_name)
    coll_mgr = get_collection_list(coll_ref, use_cache=False)
    coll_mgr_obj = coll_mgr.get(coll_ref, use_cache=False)
    coll_mgr_obj.init_collection_plugins(None)

    # add the plugin to vars_loader

# Generated at 2022-06-13 17:30:50.147193
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # simple test - use bare module
    test_plugin = os.path.join(C.DEFAULT_MODULE_PATH[0], 'test/test_plugin.py')
    plugin_vars = get_vars_from_path(None, test_plugin, [], 'task')
    assert plugin_vars['var1'] == '1', 'failed to load plugin contents'

    # test for multiple entities
    plugin_vars = get_vars_from_path(None, test_plugin, [Host('1.1.1.1'), Host('2.2.2.2')], 'inventory')
    assert plugin_vars['var1'] == '1', 'failed to load plugin contents'
    assert plugin_vars['var2'] == '2', 'failed to load plugin contents'

# Generated at 2022-06-13 17:30:53.099207
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = None
    entities = []
    stage = "inventory"
    data = get_vars_from_path(loader, path, entities, stage)
    assert data == {}



# Generated at 2022-06-13 17:30:57.394040
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # test file plugin
    path = os.path.join(os.path.split(os.path.split(__file__)[0])[0], 'lib/ansible/plugins/vars')
    data = get_vars_from_path(dict(), path, ['test_host'], 'inventory')
    assert data == {'file_data': 'I am file data'}

# Generated at 2022-06-13 17:31:01.420241
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.dummy_vars
    plugin = ansible.plugins.vars.dummy_vars.VarsModule()
    loader = "FakeLoader"
    path = "FakePath"
    entities = ["FakeEntity1", "FakeEntity2"]
    data = get_vars_from_path(loader, path, entities, 'task')
    assert data == {"dummy_var" : 1}

# Generated at 2022-06-13 17:31:11.187635
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass



# Generated at 2022-06-13 17:31:15.256001
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import anymarkup
    import pytest

    # test_plugin.yaml is a small, simple vars plugin
    test_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_plugin.yaml')
    assert os.path.exists(test_path)

    # Parse the plugin and get the plugin objects from it
    with open(test_path, 'rb') as fp:
        data = anymarkup.parse(fp)
    plugins = vars_loader.get_all_plugin_loaders_from_metadata(data, test_path)
    assert len(plugins) == 1
    loader = vars_loader.ModuleLoader()
    plugin = plugins[0]
    entities = [Host("localhost")]

# Generated at 2022-06-13 17:31:22.997416
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # host_vars plugin, single folder with hosts and groups
    print(get_vars_from_path(None, "/home/vagrant/test_host_vars/vars_folders", ["test1", "test2", "web"], "inventory"))

    # group_vars plugin, single folder with host and groups
    print(get_vars_from_path(None, "/home/vagrant/test_group_vars/vars_folders", ["test1", "test2", "web"], "inventory"))



# Generated at 2022-06-13 17:31:26.361732
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader, _, _, _ = setup_loader()
    data = {}
    path = "~/.ansible/plugins/vars/"
    from ansible.plugins.vars import vars_loader
    plugin_list = list(vars_loader.all())
    entities = [Host()]
    for plugin in plugin_list:
        data = combine_vars(data, get_plugin_vars(loader, plugin, path, entities))

# Generated at 2022-06-13 17:31:36.698081
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # for testing
    class FakePlugin:

        def __init__(self, name):
            self._load_name = name

        def get_vars(self, loader, path, entities):
            return {'plugin_get_vars': True}

        def get_group_vars(self, name):
            return {'plugin_get_group_vars': True}

    class FakeLoader:

        def __init__(self, name):
            self.name = name

        def path_exists(self, name):
            return name == self.name

    path = '/path'

    class FakeHost:

        def __init__(self, name):
            self.name = name

    class FakeGroup:

        def __init__(self, name):
            self.name = name

    # setup

# Generated at 2022-06-13 17:31:38.122384
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    assert 'a' == get_vars_from_inventory_sources('', '', '', '')

# Generated at 2022-06-13 17:31:44.985092
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    if C.RUN_VARS_PLUGINS:
        C.RUN_VARS_PLUGINS = 'all'
    if C.VARIABLE_PLUGINS:
        C.VARIABLE_PLUGINS = 'all'

    loader = "loader"
    path = "/tmp"
    entities = ['host1', 'host2']
    stage = 'inventory'
    if get_vars_from_path(loader, path, entities, stage):
        print("Vars from path is True")
    else:
        print("Vars from path is False")

if __name__ == '__main__':
    test_get_vars_from_path()

# Generated at 2022-06-13 17:31:52.416208
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars.datadiff.datadiff import VarsModule as datadiff
    from ansible.plugins.vars.extravars.extravars import VarsModule as extravars
    import ansible.plugins.vars
    import vars_loader
    from vars_loader import _get_collection_vars_plugins
    from ansible.module_utils.six import iteritems
    if os.path.isfile('test_plugin_vars.py'):
        os.remove('test_plugin_vars.py')
    test_playbook_dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "test/integration/targets/")
    test_

# Generated at 2022-06-13 17:31:54.525754
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    #data = get_vars_from_path(loader, path, entities, stage)
    assert False

# Generated at 2022-06-13 17:31:57.089176
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    print("test_get_vars_from_path")
    print(get_vars_from_path(None,'/etc/ansible/hosts',['test'], 'inventory'))

# Generated at 2022-06-13 17:32:33.600948
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class Plugin(object):
        def get_vars(self, loader, path, entities):
            pass

    class Host(object):
        def __init__(self, name):
            self.name = name

    class Group(object):
        def __init__(self, name):
            self.name = name

    loader = Mock()

    data = get_plugin_vars(loader, Plugin(), 'path', [Host('host_name'), Group('group_name')])

    assert data == {}



# Generated at 2022-06-13 17:32:41.464094
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager

    loader = 'test_loader'
    path = 'test_path'
    stage = 'test_stage'
    data = {}
    plugin = 'test_plugin'
    plugin_list = [plugin]

    class VarsLoaderMock:
        all = lambda: plugin_list

    class PluginMock:
        def get_vars(self, loader, path, entities):
            return {'key': 'value'}

    def combine_vars(data, additional_data):
        data.update(additional_data)
        return data

    class InventoryManagerMock:
        def __init__(self, loader):
            self.loader = loader


# Generated at 2022-06-13 17:32:43.531261
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path('loader', 'path', 'entities', 'inventory') is not None

# Generated at 2022-06-13 17:32:52.792702
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import get_all_plugin_loaders
    import ansible.plugins.inventory.auto

    display._output = False

    loader = get_all_plugin_loaders()['vars']

    # test with vars plugin
    plugin = vars_loader.get(u'facter')
    host = Host(u'127.0.0.1')

    assert get_plugin_vars(loader, plugin, u'.', [host])
    assert get_plugin_vars(loader, plugin, u'./facter', None)
    assert get_plugin_vars(loader, plugin, u'', [host])
    assert get_plugin_vars(loader, plugin, None, None)

    # test with host vars plugin

# Generated at 2022-06-13 17:33:02.388512
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class TestPlugin1:
        def get_vars(self, loader, path, entities, cache=True):
            return {'data1': 1}

    class TestPlugin2:
        def get_host_vars(self, host):
            return {'data2': 2}

    class TestPlugin3:
        def get_group_vars(self, group):
            return {'data3': 3}

    class TestPlugin4:
        def run(self):
            pass

    for plugin in [TestPlugin1(), TestPlugin2(), TestPlugin3(), TestPlugin4()]:
        res = get_plugin_vars(None, plugin, None, None)
        if plugin.__class__ == TestPlugin1:
            assert res['data1'] == 1

# Generated at 2022-06-13 17:33:11.282764
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader

    vault_password_file = os.path.join(os.path.dirname(__file__), "vault_password.txt")

    vault = VaultLib([vault_password_file])

    loader = AnsibleLoader(vault.decrypt, vault.is_encrypted)

    fake_loader = {}
    fake_loader.file_finder = [to_bytes(os.path.join(os.path.dirname(__file__),'targets', 'main'))]

    data = get_vars_from_path(fake_loader, fake_loader.file_finder[0], ['fakehost'], 'task')

    assert(len(data) == 2)

# Generated at 2022-06-13 17:33:19.193403
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.vars.collection_plugins.ansible.vars_plugins.foo import VarsModule as FooVarsModule
    from ansible.vars.collection_plugins.bar.plugins.vars.baz import VarsModule as BazVarsModule
    loader = vars_loader._create_loader(paths=[], class_name='VariableFileLoader')
    loader.add_directory(None, 'foo')
    loader.add_directory(None, 'bar/plugins/vars')
    loader._package_cache['foo'] = (1, FooVarsModule)
    loader._package_cache['bar.plugins.vars.baz'] = (1, BazVarsModule)
    vars_plugin

# Generated at 2022-06-13 17:33:31.308256
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.loader import InventoryLoader
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({})
    inv_loader = InventoryLoader(loader=loader)
    inv = inv_loader.load_from_file('/dev/null')

    vars_manager = VariableManager()
    vars_manager.set_inventory(inv)

    test_host = Host(name="testhost")
    test_host.set_variable("var", "var")

    result = get_vars_from_path(loader, "/dev/null", [test_host], stage="inventory")
    assert result == {
        "var": "var",
    }

    test_group = inv.groups['all']

# Generated at 2022-06-13 17:33:34.837305
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = C.CACHE_PLUGIN_FILENAME.get('vars')
    path = os.getcwd()
    entities = []
    stage = None
    result = get_vars_from_path(loader, path, entities, stage)
    assert result != None
    assert result == {}

# Generated at 2022-06-13 17:33:44.561933
# Unit test for function get_vars_from_path

# Generated at 2022-06-13 17:34:29.518777
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    os.environ["ANSIBLE_VARIABLE_PLUGINS"] = "vars_plugins.test_plugin, vars_plugins.yaml_test_plugin"
    var_test_plugin = vars_loader.get("vars_plugins.test_plugin")
    var_test_yaml_plugin = vars_loader.get("vars_plugins.yaml_test_plugin")
    assert var_test_plugin is not None
    assert var_test_yaml_plugin is not None
    path = os.path.join(os.getcwd(), "test", "unit", "_data", "vars_plugin")
    display.vv

# Generated at 2022-06-13 17:34:37.332688
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_vars_loader = vars_loader.VarsModuleLoader()
    test_vars_loader.set_cwd(__file__)
    test_collection_loader = vars_loader.VarsModuleLoader(pdn='ansible_collections.testns.testing')
    test_collection_loader.set_cwd(__file__)
    test_collection_loader.load_all()

    from ansible.plugins.vars.host_list import HostList

    test_plugin_list = vars_loader.all()
    host_1 = Host('test_host_1')
    host_2 = Host('test_host_2')
    # test for plugin list
    plugin = test_plugin_list.get('host_list')

    # test for host_list plugin
    # host_list plugin is only used

# Generated at 2022-06-13 17:34:44.999386
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Setup a fake vars loader plugin
    from ansible.plugins.loader import vars_loader
    plugin_class = type('FakeVarsPlugin', (object,), dict(get_vars=lambda x,y,z: dict(foo='bar'), __file__="fake_file"))
    plugin = plugin_class()
    plugin._load_name = 'dummy'
    plugin._original_path = plugin.__file__
    vars_loader.add(plugin)
    # Test function
    assert get_vars_from_path(None, '', '', '') == dict(foo='bar')

# Generated at 2022-06-13 17:34:56.145198
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from .test_utils import capture_output

    class MockVarsPlugin(object):
        def __init__(self, name, vars):
            self._load_name = name
            self._vars = vars

        def get_vars(self, loader, path, entities):
            return self._vars

        def get_group_vars(self, group_name):
            return self._vars

        def get_host_vars(self, host_name):
            return self._vars


    class MockCollectionLoader(object):
        def __init__(self, collection_vars):
            self.collection_vars = collection_vars
            self.plugin = None

        def add(self, plugin):
            self

# Generated at 2022-06-13 17:34:57.817929
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path('/path/to/vars', [], 'inventory') == {}

# Generated at 2022-06-13 17:34:58.477372
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:34:59.086396
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:35:02.471966
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader = None
    sources = ['/tmp/']
    entities = []
    stage = 'inventory'
    assert get_vars_from_inventory_sources(loader, sources, entities, stage) == {}

# Generated at 2022-06-13 17:35:03.806133
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True



# Generated at 2022-06-13 17:35:08.094177
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_data = get_vars_from_path(None, './test_dir', None, None)
    assert len(vars_data) == 1
    assert vars_data.get("test_var") == "test_var_value"

# Generated at 2022-06-13 17:35:55.388114
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class VarPlugin(object):
        def __init__(self, *args, **kwargs):
            super(VarPlugin, self).__init__(*args, **kwargs)
            self.name = "testvars"

        def get_vars(self, loader, path, entities, cache=True):
            return {'testvars': {'testkey': 'testvalue'}}

    test_plugin = VarPlugin()

    data = get_plugin_vars(None, test_plugin, "", [])

    assert data['testvars']['testkey'] == 'testvalue'

# Generated at 2022-06-13 17:36:02.997193
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    pluginManager = vars_loader.all(class_only=True)
    display.display(pluginManager)

    options = {'syntax': 'yaml', 'extensions': ['vars']}

    # vamping for a test
    data_vars = {'foo': 'bar'}
    data_hostvars = {'fakehost': {'ansible_host': '127.0.0.1'}}
    pluginManager.append(vars_loader._VarsModule({'path': None}, data=data_vars))

# Generated at 2022-06-13 17:36:08.062876
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.vars.vars_plugins.vault import get_vars as vvars
    test_data = vvars(None, os.path.dirname(os.path.abspath(__file__)), ['dummy'])
    assert test_data == {'vault_test': 'foo'}

# Generated at 2022-06-13 17:36:11.288230
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    # loads vars from inventory source
    data = get_vars_from_inventory_sources(
        loader=None,
        sources="/some/path",
        entities=None,
        stage="task")
    assert data

# Generated at 2022-06-13 17:36:11.997276
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:36:21.575415
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import vars_loader

    loader = vars_loader
    path = './tests/vars_plugins'
    host = Host('test_host')
    group = Group('test_group')
    entities = [host, group]
    stage = 'task'

    data = get_vars_from_path(loader, path, entities, stage)

    assert data == {
        'group_data': {'test_group': {'var_name': 'group_value'}},
        'host_data': {'test_host': {'var_name': 'host_value'}},
        'all_data': {'var_name': 'all_value'}
    }

# Generated at 2022-06-13 17:36:26.704491
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Tests valid and invalid plugin
    loader = None
    entities = []
    path = "/foo/bar"
    for klass in vars_loader.all():
        vars_plugin = get_vars_from_path(loader, path, entities, klass)
        assert vars_plugin

    vars_plugin = get_vars_from_path(loader, path, entities, None)
    assert not vars_plugin

# Generated at 2022-06-13 17:36:27.978917
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True

# Generated at 2022-06-13 17:36:37.427759
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    dataloader = DataLoader()
    pb_inventory = InventoryManager(loader=dataloader, sources=['localhost'])
    variable_manager = VariableManager(loader=dataloader, inventory=pb_inventory)
    playcontext = PlayContext()

# Generated at 2022-06-13 17:36:45.578132
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.parsing.vault import VaultLib
    from ansible.inventory.manager import InventoryManager

    vault_secret = 'test'
    vault_password_file = str(__file__) + 'test_get_vars_from_path.vault_pass'
    with open(vault_password_file, 'w') as f:
        f.write(vault_secret)
    vault_password_file = os.path.realpath(vault_password_file)

    # Test host_vars parsing
    host_vars_dir = str(__file__) + 'test_get_vars_from_path.host_vars_dir'
    os.makedirs(host_vars_dir)

    host_vars_file = host_vars_dir + '/localhost.yml'

# Generated at 2022-06-13 17:38:17.461452
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = None
    entities = None
    stage = None
    get_vars_from_path(loader, path, entities, stage)


# Generated at 2022-06-13 17:38:26.710755
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class VarsPlugin:
        def get_vars(self, loader, path, entities):
            return {'test_vars': {'var1': 'val1', 'var2': 'val2'}}

    class VarsPlugin1:
        def get_vars(self, loader, path, entities):
            return {'test_vars': {'var1': 'val2', 'var3': 'val3'}}

    class VarsPlugin2:
        def get_vars(self, loader, path, entities):
            return {'test_vars': {'var3': 'val3'}}

    class VarsPlugin3:
        def get_vars(self, loader, path, entities):
            return {'test_vars': {'var4': 'val4'}}


# Generated at 2022-06-13 17:38:28.955828
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader, path, entities, stage = None, None, None, None
    assert get_vars_from_path(loader, path, entities, stage) == {}

# Generated at 2022-06-13 17:38:33.589354
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible_collections.test.test_utils.test_module_utils.test_plugins.test_loader.test_vars_loader import TestVarsPlugin
    v = vars_loader.get('test_vars_plugin')
    assert get_plugin_vars(None, v, None, ['abc', 'def']) == {u'abc': 3, u'def': 4}