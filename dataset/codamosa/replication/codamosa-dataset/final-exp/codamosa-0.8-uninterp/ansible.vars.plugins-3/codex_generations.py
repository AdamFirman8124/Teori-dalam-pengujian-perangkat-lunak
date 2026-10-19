

# Generated at 2022-06-13 17:28:39.658370
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: add test
    pass

# Generated at 2022-06-13 17:28:47.476790
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader, hosts, groups, sources = init_inventory_loader()

    # Mock data
    sources.append(None)
    sources.append(',')
    sources.append('/non/existing/dir')
    sources.append('/etc/ansible/hosts')

    # Call get_vars_from_inventory_sources and check if list of sources is not modified
    assert 'None' not in get_vars_from_inventory_sources(loader, sources, hosts, 'inventory')
    assert 'None' not in get_vars_from_inventory_sources(loader, sources, hosts, 'task')
    assert ',' not in get_vars_from_inventory_sources(loader, sources, hosts, 'inventory')

# Generated at 2022-06-13 17:28:57.442614
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.loader import module_loader

    assert len(vars_loader._modules) == 0
    assert len(vars_loader._module_cache) == 0
    assert len(vars_loader._aliases) == 0
    assert len(vars_loader._plugin_path_cache) == 0

    # make sure we start with nothing in the loader, and that
    # the cache contains expected values
    v2_loader = module_loader.ModuleLoader(vars_loader._plugin_path_cache)
    vars_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/plugins/vars'))

    # make sure module_utils is present (needed for the test plugins to load)


# Generated at 2022-06-13 17:29:07.508148
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import tempfile


# Generated at 2022-06-13 17:29:15.625661
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    class FakeVarsPlugin():
        def get_vars(self, loader, path, entities):
            return {'fake_vars_plugin': 'Hello'}

    class FakeVarsHostPlugin():
        def get_host_vars(self, host):
            return {'fake_host_vars_plugin': 'World'}

    class FakeVarsGroupPlugin():
        def get_group_vars(self, group):
            return {'fake_group_vars_plugin': '!'}

    class FakeClass():
        def __init__(self):
            pass

    class FakeHost():
        def __init__(self, name):
            self.name = name

    class FakeGroup():
        def __init__(self, name):
            self.name = name

    # Test a 2.0-style vars plugin

# Generated at 2022-06-13 17:29:18.180979
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    # TODO: Add test for function get_vars_from_inventory_sources
    pass

# Generated at 2022-06-13 17:29:26.905932
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    def fake_get_plugin_vars(loader, plugin, path, entities):
        return dict(my_var="my_value")

    fake_entity_1, fake_entity_2 = "fake_entity_1", "fake_entity_2"
    fake_entities = (fake_entity_1, fake_entity_2)

    fake_path_1, fake_path_2 = "/fake/path1", "/fake/path2"
    fake_paths = (fake_path_1, fake_path_2)

    from ansible.plugins.loader import vars_loader
    from ansible.plugins.loader import vars_plugins
    from ansible.utils.vars import combine_vars

    saved_get_plugin_vars = get_plugin_vars

# Generated at 2022-06-13 17:29:28.843291
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: write test code
    pass



# Generated at 2022-06-13 17:29:36.976220
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    path = os.path.join(C.TEST_DIR, 'test_vars_plugin.py')
    plugin = vars_loader.get('test_vars_plugin', path=path)
    loader = 'test_loader'
    entities = [
        Host(name='host1'),
        Host(name='host2'),
        Host(name='host3'),
    ]

    expected_result = {
        '_host1': 'host1',
        '_host2': 'host2',
        'host3': 'host3',
    }

    result = get_plugin_vars(loader, plugin, path, entities)
    assert expected_result == result

# Generated at 2022-06-13 17:29:37.580756
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:29:51.342154
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class test_vars_plugin():
        class __init__(self):
            self._load_name = 'test_vars_plugin'
            self.path = 'test_path'
            self.entities = 'test_entities'

        def get_vars(self, loader, path, entities):
            return {'get_vars': ''}

        def get_host_vars(self, name):
            return {'get_host_vars': ''}

        def get_group_vars(self, name):
            return {'get_group_vars': ''}
    data = get_plugin_vars('', test_vars_plugin(), '', '')
    assert data == {'get_vars': ''}



# Generated at 2022-06-13 17:29:53.791219
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # TODO: Write a unit test for get_vars_from_path()
    pass


# Generated at 2022-06-13 17:29:58.610111
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    from ansible.plugins.vars import vars_plugin

    assert get_plugin_vars(None, None, None, None) == {}
    assert get_plugin_vars(None, None, "", "") == {}
    assert get_plugin_vars(None, vars_plugin.VarsModule, "", "") == {}
    assert get_plugin_vars(None, vars_plugin.VarsModule, "", "host") == {}

# Generated at 2022-06-13 17:30:07.145291
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.loader.vars_plugins
    import ansible.plugins.vars.base_vars
    import ansible.plugins.vars.group_vars_files
    from ansible.plugins.loader import vars_loader
    test_path = '/tmp/test_vars_from_path'
    plugin_list = [ansible.plugins.vars.base_vars.BaseVars(vars_loader)]
    plugin_list.append(ansible.plugins.vars.group_vars_files.GroupVarsFiles(vars_loader, test_path))
    ansible.plugins.loader.vars_plugins._vars_plugins = plugin_list
    print("**Test plugin list: " + str(plugin_list))


# Generated at 2022-06-13 17:30:17.932686
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.inventory import Inventory

    plugin_class = type('TestVarsPlugin', (object,), {'get_vars': lambda self, loader, path, entities: {'bar': 'foo'}})

    plugin_obj = plugin_class()
    plugin_obj._load_name = 'TestVarsPlugin'
    plugin_obj._original_path = '/some/path'
    plugin_obj.set_options = lambda *args, **kwargs: None

    inventory = Inventory('hosts')
    inventory.add_host(Host(name="foo"))

    assert {'bar': 'foo'} == get_plugin_vars(inventory.loader, plugin_obj, '/some/path', inventory.entries.keys())


# Generated at 2022-06-13 17:30:27.749492
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # create a mock for plugin.get_vars()
    class my_plugin():
        def get_vars(self, *args, **kwargs):
            return {'key1': 'value1'}

    mock_vars_loader = [my_plugin()]

    # mock for path
    path = '/tmp/'

    # mock for entities
    class my_entity():
        def __init__(self, name):
            self.name = name

    entities = [ my_entity('entity_1'), my_entity('entity_2') ]

    # mock for stage
    stage = 'inventory'

    expected_data = {'key1': 'value1'}

    actual_data = get_vars_from_path(mock_vars_loader, path, entities, stage)

    assert expected_data == actual_

# Generated at 2022-06-13 17:30:39.084009
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    display.verbosity = 2
    def get_plugin_vars(loader, plugin, path, entities):
        data = {}
        try:
            data = plugin.get_vars(loader, path, entities)
        except AttributeError:
            try:
                for entity in entities:
                    if isinstance(entity, Host):
                        data.update(plugin.get_host_vars(entity.name))
                    else:
                        data.update(plugin.get_group_vars(entity.name))
            except AttributeError:
                if hasattr(plugin, 'run'):
                    raise AnsibleError("Cannot use v1 type vars plugin %s from %s" % (plugin._load_name, plugin._original_path))

# Generated at 2022-06-13 17:30:48.440688
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager

    # Add some fake paths to search for
    sources = [
        '/etc/ansible/hosts',
        '/etc/myhosts'
    ]

    # Create some fake plugins
    class FakeVarsPlugin1(object):
        def get_vars(self, loader, path, entities):
            vars = {}
            vars['test_key_1'] = 'test_val_1'
            return vars

    class FakeVarsPlugin2(object):
        def get_vars(self, loader, path, entities):
            vars = {}
            vars['test_key_2'] = 'test_val_2'
            return vars

    # Load fake plugins.

# Generated at 2022-06-13 17:30:57.549705
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import sys
    import ansible.plugins.loader
    from ansible.constants import DEFAULT_MODULE_PATH

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from test_utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    class TestGetVarsFromPath(ModuleTestCase):

        def setUp(self):
            super(TestGetVarsFromPath, self).setUp()
            self.mock_module = False
            self.mock_get_vars = False
            self.mock_get_group_vars = False
            self.mock_get_host_vars = False


# Generated at 2022-06-13 17:31:02.211784
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    loader = vars_loader
    assert get_plugin_vars(loader,loader.get('host_group_add'),'/tmp',['all']) == {
        'group': 'all',
        'host_group_add_fake_var': 'fake_value'}
    assert get_vars_from_path(loader,'/tmp',['all'],'inventory') == {
        'group': 'all',
        'host_group_add_fake_var': 'fake_value'}

# Generated at 2022-06-13 17:31:16.505065
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host

    host = Host('hostname1')
    host.vars = {'k0': 'v0_host', 'k1': 'v1'}

    path = 'path'
    loader = None
    data = get_vars_from_path(loader, path, [host], 'inventory')
    assert data == {'k0': 'v0_host', 'k1': 'v1'}



# Generated at 2022-06-13 17:31:17.875910
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO: Test me
    pass

# Generated at 2022-06-13 17:31:25.812884
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/mock_inventory/host_vars_ordering_play'])
    variable_manager = VariableManager(loader=loader, sources=inventory)
    assert loader.get_basedir() == os.path.abspath(os.path.curdir)
    assert loader.path_exists("test_vars_ordering_inventory_plugin.yml")

    # Test all plugins
    plugin_names = [plugin._load_name for plugin in plugin_loader.all(class_only='VarsModule')]
    plugin

# Generated at 2022-06-13 17:31:30.370665
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Make a fake variables plugin
    class FakeVariablesModule(VarsBase):
        def __init__(self):
            self._original_path = 'fake_path'
            self._load_name = 'fake'

        def get_vars(self, loader, path, entities):
            return {'foo': 'bar'}

    fake_loader = PluginLoader(None)
    fake_loader.loaders = lambda **kwargs: [FakeVariablesModule()]
    fake_loader.file_match = lambda **kwargs: [FakeVariablesModule()]

    assert get_vars_from_path(fake_loader, 'fake_path', [], 'inventory') == {'foo': 'bar'}

# Generated at 2022-06-13 17:31:33.664551
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible_collections.testns.testcoll import plugins

    data = {}
    data = get_plugin_vars(None, plugins.my_vars_plugin(), None, None)
    assert data == {'foo': 'bar'}

# Generated at 2022-06-13 17:31:34.819737
# Unit test for function get_vars_from_inventory_sources

# Generated at 2022-06-13 17:31:43.120218
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # vars_loader is mocked
    test_loader = {
        'get_single_plugin': lambda a, b, c, d: b
    }
    # Entities are also mocked
    test_entities = [
        {
            'name': 'inventory_hostname'
        }
    ]
    # test_plugins is a dict of plugin name and return value
    test_plugins = {
        'plugin 1': 'plugin 1 return val',
        'plugin 2': 'plugin 2 return val'
    }

    # Given
    vars_loader.clear_all()
    for plugin_name, return_val in test_plugins.items():
        vars_loader.add(plugin_name, None, return_val)

    # When

# Generated at 2022-06-13 17:31:50.365721
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.plugins.loader import vars_loader

    class TestVarsPlugin:
        def __init__(self):
            self.vars_data = None

        def get_vars(self, loader, path, entities):
            if self.vars_data is None:
                self.vars_data = {}
            self.vars_data['path'] = path
            self.vars_data['entities'] = entities
            return self.vars_data

    test_plugin = TestVarsPlugin()
    vars_loader.add(test_plugin, 'test_vars_plugin')


# Generated at 2022-06-13 17:31:57.831941
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """test_get_vars_from_path: get_vars_from_path() should return a dictionary of vars"""
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    cli = CLI(['-i', 'localhost,'], '/dev/null', '/dev/null', loader=loader)
    inv = cli.inventory.get_host_vars('localhost')
    assert type(inv) is dict

# Generated at 2022-06-13 17:32:07.135017
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader, module_loader

    fake_loader = DictDataLoader({})
    fake_inventory = DictInventory(host_list=[DictHost(name='fakehost')])

    class FakeModuleLoader(object):

        def get(self, path, name, *args, **kwargs):
            class FakeVarsModule(object):
                def run(self, path, entities, names=None, options=None):
                    return {'a': 1, 'b': entity.name}

            return FakeVarsModule()

    class FakeVarsLoader(object):
        class FakeVarsPlugin(object):
            def __init__(self, path, entities):
                self.path = path
                self.entities = entities


# Generated at 2022-06-13 17:32:23.170493
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager

    host_path = os.path.dirname(os.path.dirname(__file__)) + "/../../lib/ansible/plugins/inventory/host_list.py"
    group_path = os.path.dirname(os.path.dirname(__file__)) + "/../../lib/ansible/plugins/inventory/group_vars.py"
    mock_loader = lambda: None
    mock_loader.all = lambda: [host_path, group_path]

    entities = InventoryManager(["localhost"]).get_hosts()

    data = get_vars_from_path(mock_loader, ".", entities, "inventory")
    assert data["inventory_file"] == "localhost"
    assert data["inventory_dir"] == "."

# Generated at 2022-06-13 17:32:29.754995
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    loader = InventoryManager('localhost,')

    display = Display()
    display.verbosity = 2

    # source is a folder with some vars files
    # source/group_vars/group1
    # source/group_vars/group2
    # source/host_vars/localhost
    # source/vars1.yml

    # host_list is a file contains some hosts
    # host_list
    # localhost
    # 127.0.0.1

    # Test the function: get_vars_from_path
    source = './test/integration/vars_plugins/test_var_plugins'
    host_list = './test/integration/vars_plugins/host_list'


# Generated at 2022-06-13 17:32:38.183199
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible

    ansible_path = ansible.__path__[0]
    plugin_path = os.path.join(ansible_path, 'plugins', 'vars')
    loader = None
    path = plugin_path
    entities = ['example']
    stage = 'task'
    vars_data = get_vars_from_path(loader, path, entities, stage)
    assert isinstance(vars_data, dict)
    assert len(vars_data) > 0
    assert vars_data['example1'] is not None
    assert vars_data['example2'] is not None
    assert vars_data['example3'] is not None
    assert vars_data['example4'] is not None

# Generated at 2022-06-13 17:32:44.561536
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import vars_loader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    path = 'test/test_get_vars_from_path'
    entities = ['groupname']
    stage = 'inventory'

    all_plugin_dict = vars_loader.all()
    data = {}
    for plugin in all_plugin_dict:
        data = combine_vars(data, get_plugin_vars(loader, plugin, path, entities))

    vars_man = VariableManager()
    vars_man.extra_vars = {
        "name": "value",
        "name2": "value2",
        "nam3": "value3"
    }
    vars_

# Generated at 2022-06-13 17:32:53.504912
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars import combine_vars

    test_dir = os.path.join(os.path.dirname(__file__), 'vars_loader_test_data')

    inventory = InventoryManager(loader=None, sources=[test_dir])
    host = inventory.get_host('test_host')

    # Get vars from path.
    assert host.vars == combine_vars(get_vars_from_path(loader=None, path=test_dir, entities=[host], stage='task'),
                                     get_vars_from_path(loader=None, path=test_dir, entities=[host], stage='inventory'))

    # Get vars from inventory sources.

# Generated at 2022-06-13 17:33:02.458930
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import ansible.plugins.vars.host_group_vars

    inventory = InventoryManager(loader=None, sources=["localhost"])
    inventory.add_host("localhost")
    inventory.add_group("local")
    inventory.add_host("another", groups=["local"])

    variable_manager = VariableManager(loader=None, inventory=inventory)
    variable_manager._vars_plugins = { 'host_group_vars': ansible.plugins.vars.host_group_vars.VarsModule() }

    path = "my/path"


# Generated at 2022-06-13 17:33:11.894089
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    VARS_PLUGINS_ENABLED_OLD = C.VARIABLE_PLUGINS_ENABLED
    C.VARIABLE_PLUGINS_ENABLED = ('v1_config', 'v2_config')

    # Test loading old vars plugins
    vars_plugin_list = list(vars_loader.all())
    assert len(vars_plugin_list) == 2

    # Test loading new vars plugins
    vars_plugin_list = list(vars_loader.all())
    assert len(vars_plugin_list) == 2

    C.VARIABLE_PLUGINS_ENABLED = VARS_PLUGINS_ENABLED_OLD

# Generated at 2022-06-13 17:33:19.558686
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.config.loader as configuration
    class TestLoader(object):
        def get_basedir(self):
            return 'test/'
    class TestEntity(object):
        def __init__(self, name):
            self.name = name
        def get_vars(self):
            return {'foo': 'bar'}
    config = configuration.Config()
    loader = TestLoader()
    ent = TestEntity('lalala')
    config.runtime_path = 'test'
    display.verbosity = 2
    # test yaml vars plugin
    print(get_vars_from_path(loader, 'test', [ent], 'inventory'))
    # test ini vars plugin
    print(get_vars_from_path(loader, 'test', [ent], 'inventory'))

# Generated at 2022-06-13 17:33:31.535550
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from units.mock.loader import DictDataLoader
    from units.compat import Mock

    test_vars_plugin = Mock()
    test_vars_plugin.vars = {"var1": "value1", "var2": "value2"}
    test_vars_plugin.get_vars.return_value = test_vars_plugin.vars
    test_vars_plugin.get_host_vars.return_value = test_vars_plugin.vars
    test_vars_plugin.get_group_vars.return_value = test_vars_plugin.vars
    test_vars_plugin._load_name = "test_vars_plugin"
    test_vars_plugin._original_path = "test_vars_plugin.py"

# Generated at 2022-06-13 17:33:32.434471
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    #TODO:
    pass

# Generated at 2022-06-13 17:33:43.437820
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import mock, sys
    import os.path

    current_path = os.path.dirname(os.path.realpath(__file__))
    mocks_path = os.path.join(current_path, 'mocks')
    sys.path.append(mocks_path)

    print("Running Inventory Vars Plugins tests")
    print("====================================")

    # Import test plugin
    import test_vars_plugin
    test_vars_plugin.setup()

    # Prepare mocked vars plugin loading
    vars_loader_inst = mock.MagicMock()
    vars_loader_inst.all.return_value = [test_vars_plugin]

    # Import mocked loader
    from ansible.plugins.loader import vars_loader as vars_loader_real
    vars_loader_real.__init

# Generated at 2022-06-13 17:33:43.952804
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True

# Generated at 2022-06-13 17:33:50.496212
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/vars_plugins/hosts'])
    play = Play().load(dict(
        hosts=inventory,
        gather_facts='no',
        tasks=[],
    ), loader=loader, variable_manager=inventory.get_variable_manager())
    variable_manager = play.get_variable_manager()

    stage = 'inventory'
    entities = [inventory.groups['all'], inventory.groups['all'].hosts['host1'], inventory.groups['all'].hosts['host2']]
    path1 = 'test/vars_plugins/group_vars'

# Generated at 2022-06-13 17:33:51.397208
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Not implemented yet.
    return


# Generated at 2022-06-13 17:33:52.430938
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path()

# Generated at 2022-06-13 17:34:02.356615
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    os.environ['ANSIBLE_PYTHON_INTERPRETER'] = 'python2.7'
    os.environ['ANSIBLE_VARIABLE_PLUGINS'] = 'vars_plugins'

    config = {}

    loader = vars_loader
    loader.set_basedir(os.path.join(os.path.dirname(__file__), 'vars_plugins'))
    loader.set_config(config)
    loader.set_command_line_options(config)
    loader.load_all()

    plugin = loader.get('test_v1')

    class FakeEntity():
        name = 'foo'

    entities = [FakeEntity()]

    data = get_plugin_vars(loader, plugin, '', entities)
    assert data

    # no longer raises error
    data = get

# Generated at 2022-06-13 17:34:09.577706
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_data = {'test_var': 'test_value'}
    test_path = '.'

    # Return data for get_vars_from_path
    def port_vars(loader, path, entities):
        return test_data

    assert test_data == get_vars_from_path({}, test_path, None, None)
    assert test_data == get_vars_from_path({'port_vars': port_vars}, test_path, None, None)


# Generated at 2022-06-13 17:34:19.078758
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    test_path = os.path.join(C.DEFAULT_LOCAL_TMP, "test_get_vars_from_path")
    os.mkdir(test_path)

    # create inventory directory
    path = os.path.join(test_path, "inventory")
    os.mkdir(path)
    # create empty file
    f = open(os.path.join(test_path, "vars_test.py"), "w+")
    f.close()
    open(os.path.join(test_path, "vars_test"), "w+").close()

    loader = vars_loader.get("vars_test")
    host_vars_dir = os.path.join(path, "host_vars")
    os.mk

# Generated at 2022-06-13 17:34:27.589518
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """Test that vars are returned from a path"""
    from ansible_collections.ansible.misc.plugins.vars import yaml_data
    from ansible.plugins.loader import vars_loader

    # Call the get_vars func
    expected_result = {'yaml_file_name': 'file', 'yaml_file_path': '/path/to/folder',
                       'yaml_file_content': [1, 2, 3, 4]}
    data = get_vars_from_path(None, '.', None, None)
    assert expected_result == data

    # Check that the vars plugin is added to the list of vars plugins
    plugin_list = list(vars_loader.all())
    assert yaml_data in plugin_list



# Generated at 2022-06-13 17:34:32.442499
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import pytest
    from ansible.plugins.vars.vars_plugin import VarsBase

    class TestVarsPlugin(VarsBase):
        pass

    with pytest.raises(AnsibleError):
        TestVarsPlugin()

    with pytest.raises(AnsibleError):
        get_vars_from_path(None, None, None, None)

# Generated at 2022-06-13 17:34:40.989449
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:34:42.321615
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    #TODO
    pass


# Generated at 2022-06-13 17:34:44.485075
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    plugin = vars_loader.get("yaml")
    data = get_vars_from_path(None, "test/test", None, None)

    assert(data == {'test': {'name': 'test1'}})


# Generated at 2022-06-13 17:34:45.846205
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:34:47.467679
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, '.', [], 'inventory') == {}

# Generated at 2022-06-13 17:34:53.700302
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # test that an empty AnsibleCollectionRef returns an empty dict
    col_ref = AnsibleCollectionRef()
    assert get_vars_from_path(None, None, None, None) == {}

    # test that an AnsibleCollectionRef with an invalid name returns an empty dict
    col_ref = AnsibleCollectionRef(name='foo.bar.baz')
    assert get_vars_from_path(None, None, None, None) == {}

    # test that an AnsibleCollectionRef with an valid name returns a proper dict
    col_ref = AnsibleCollectionRef(name='ansible.builtin')
    assert get_vars_from_path(None, None, None, None) == {}

# Generated at 2022-06-13 17:35:01.182794
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = 'plugins/vars/test_getvars.py'
    path = 'tests/vars_plugins/test_getvars/getvars'
    hosts = []
    assert_result = {'test_plugin': {},'plugin_no_run': {'plugin': 'plugin_no_run'},'plugin_no_get_vars': {'plugin': 'plugin_no_get_vars'}}
    data = get_vars_from_path(loader, path, hosts, 'inventory')
    assert data == assert_result

# Generated at 2022-06-13 17:35:08.748024
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())

    def test_plugin(loader, path, entities):
        return {'test_key': 'test_value'}

    plugin = vars_loader.get('test_plugin')
    plugin.get_vars = test_plugin
    vars_plugin_list.append(plugin)
    path = './test_path'
    entities = []
    data = get_vars_from_path(loader, path, entities, 'inventory')

    assert data['test_key'] == 'test_value'

# Generated at 2022-06-13 17:35:17.356904
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class Plugin():
        def __init__(self, load_name, has_option, get_option, stage_value, has_var_methods):
            self._load_name = load_name
            self.has_option = has_option
            self.get_option = get_option
            self.stage_value = stage_value
            self.has_var_methods = has_var_methods

        def get_vars(self, loader, path, entities):
            # Only run if this function exists
            if not self.has_var_methods:
                return {}

            if 'single-method' in self._load_name:
                # Test that this is a v2 plugin
                assert(loader is not None)
                assert(path is not None)
                assert(entities is not None)


# Generated at 2022-06-13 17:35:18.489878
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:35:46.767989
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO: Test all other branches in this function
    from ansible.plugins.vars import vars_base

    class TestPlugin(vars_base.AnsibleVarsBase):

        def get_vars(self, *args, **kwargs):
            return {'test_vars': True}
    plugin = TestPlugin()

    vars_loader.add(plugin, 'test', 'test_var_loader.py')
    assert get_vars_from_path(None, '/', [], 'inventory')['test_vars']



# Generated at 2022-06-13 17:35:54.612861
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Initalize a data loader and an inventory manager with a fake inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    get_vars_from_path(loader, 'path', inventory.get_hosts('localhost'), 'inventory')
    get_vars_from_path(loader, 'path', inventory.get_groups(), 'inventory')
    get_vars_from_path(loader, 'path', inventory.get_hosts('localhost') + inventory.get_groups(), 'inventory')
    get_vars_from_path(loader, 'path', inventory.get_hosts('localhost'), 'task')

# Generated at 2022-06-13 17:36:02.493615
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import plugin_loader

    _plugin_list = [
        'vars_plugin.py',
        'vars_plugin2.py',
    ]

    _plugin_context = {}
    _loader = plugin_loader.PluginLoader(
        'vars',
        'vars',
        C.VARS_PLUGINS_PATH,
        '_',
        'vars_plugins',
        _plugin_list,
        _plugin_context,
    )

    _plugin_list = list(_loader.all())

    _plugin_name = 'vars_plugin.py'
    _plugin = _plugin_list[0]
    path = ''
    entities = ['host_name', 'group_name']

    data = get_plugin_vars(_loader, _plugin, path, entities)


# Generated at 2022-06-13 17:36:13.731598
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.plugin_docs import get_docstring
    from ansible_collections.ansible.collection_loader.vars_plugins.test_vars_plugin import TestVarsPlugin

    inventory = InventoryManager(loader=DataLoader(), sources='localhost')
    host = inventory.get_host(hostname='localhost')
    plugin_vars = get_vars_from_path(loader=None, path=None, entities=[host, ], stage='all')

    # testing to see if the plugin added the variable we thought it would
    assert plugin_vars['plugin_variable'] == 'plugin_value'

    # testing to see if the docs got generated for the test plugin

# Generated at 2022-06-13 17:36:22.851083
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # This is necessary to get rid of all the defult plugins that may be enabled
    # by default.
    C.VARIABLE_PLUGINS_ENABLED = []
    for plugin in vars_loader.all():
        if plugin._load_name not in C.VARIABLE_PLUGINS_ENABLED and getattr(plugin, 'REQUIRES_WHITELIST', False):
            # 2.x plugins shipped with ansible should require whitelisting, older or non shipped should load automatically
            continue
        C.VARIABLE_PLUGINS_ENABLED.append(plugin._load_name)
    # Unit test get_vars_from_path
    loader = None
    test_path = "unit_test_path"
    test_entities = ['all']

# Generated at 2022-06-13 17:36:27.807132
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Case 1: Test with invalid path
    path = 'invalid_path'
    entities = None
    stage = 'task'
    # Expect to receive an empty dictionary
    expected_result = {}
    returned_data = get_vars_from_path(None, path, entities, stage)
    assert returned_data == expected_result



# Generated at 2022-06-13 17:36:37.285751
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # utils part
    # CollectionRef is a subclass of str
    CollectionRef = type(
        'CollectionRef',
        (str,),
        {
            'is_valid_fqcr': staticmethod(lambda _s: False),
        }
    )
    # FakeCollectionRef is a subclass of CollectionRef
    FakeCollectionRef = type(
        'FakeCollectionRef',
        (CollectionRef,),
        {}
    )

    # vars_loader part
    class FakeVarsPlugin(object):
        def __init__(self, load_name):
            self._load_name = load_name


# Generated at 2022-06-13 17:36:45.466158
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Setup
    loader, path, entities, stage = 'a', 'b', 'c', 'task'
    plugin_name_1 = 'a.plugins.vars.a'
    plugin_name_2 = 'a.plugins.vars.b'
    collection_1 = 'a.plugins.vars'
    plugin_1_vars = {'a': '1'}
    plugin_2_vars = {'a': '2'}
    C.VARIABLE_PLUGINS_ENABLED.append(plugin_name_1)
    C.VARIABLE_PLUGINS_ENABLED.append(collection_1)
    C.RUN_VARS_PLUGINS = 'all'
    plugin_1 = vars_loader.get(plugin_name_1)

# Generated at 2022-06-13 17:36:52.326943
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager
    loader = InventoryManager("/etc/ansible/hosts")
    sources = ["/etc/ansible/hosts"]
    entities = loader.get_hosts("test_host")
    stage = "inventory"
    data = get_vars_from_inventory_sources(loader, sources, entities, stage)
    assert (data is not None)

# Generated at 2022-06-13 17:37:00.991259
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    vars_plugin_list = list(vars_loader.all())
    for plugin_name in C.VARIABLE_PLUGINS_ENABLED:
        vars_plugin = vars_loader.get(plugin_name)
        if vars_plugin is None:
            raise Exception("Invalid vars plugin %s" % plugin_name)
        if vars_plugin not in vars_plugin_list:
            vars_plugin_list.append(vars_plugin)

    path = "test"
    entities = {}
    stage = "inventory"
    data = get_vars_from_path(path, entities, stage)


# Generated at 2022-06-13 17:37:33.059261
# Unit test for function get_plugin_vars

# Generated at 2022-06-13 17:37:36.792878
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, None, None, None) == {}
    assert get_vars_from_path(None, None, None, None) == {}
    assert get_vars_from_path(None, '', None, None) == {}

# Generated at 2022-06-13 17:37:45.323930
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    import ansible.plugins.vars.test_vars_plugin
    from ansible.module_utils._text import to_bytes

    loader = vars_loader
    path = os.path.dirname(ansible.plugins.vars.test_vars_plugin.__file__)
    # Ensure all plugins are valid to catch/test any functionality that does not work for all plugin types
    plugin_names = {p._load_name for p in loader.all()}
    if plugin_names != set(['test_vars_plugin']):
        raise AssertionError("the unit test requires the only vars plugin to be test_vars_plugin")

    source_hosts = {'host1': 'host1', 'host2': 'host2'}

    # set stage

# Generated at 2022-06-13 17:37:56.072625
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    loader = DictDataLoader({
        b'vars_plugins/a.yml': b'',
        b'vars_plugins/b.yml': b''})
    plugin_a = DictVars(loader, b'vars_plugins/a.yml', 'a', {'host_vars': {'foo': 'bar'}})
    plugin_b = DictVars(loader, b'vars_plugins/b.yml', 'b', {'group_vars': {'a': 'b'}})
    plugin_list = [plugin_a, plugin_b]
    host = Host('foo')
    host.name = 'foo'
    data = {}

# Generated at 2022-06-13 17:38:02.838206
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Create the loader
    loader = get_loader()
    vars_plugin_list = list(vars_loader.all())

    # Add a path
    path = 'test_var_path'
    # Create a dummy plugin
    test_plugin = DummyPlugin()
    test_plugin._load_name = 'test_plugin_name'
    test_plugin._original_path = 'test_plugin_path'
    # Add dummy plugin to the list of plugins
    vars_plugin_list.append(test_plugin)
    # Call the function
    data = get_vars_from_path(loader, path, [], 'task')

    # Check if the function returns a dictionary with required items
    assert type(data) == dict
    assert data['var_name'] == 'var_value'

# A generic base class for unit

# Generated at 2022-06-13 17:38:11.542137
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    C.RUN_VARS_PLUGINS = 'start'
    context.CLIARGS['inventory'] = ['/ansible/test/unit/inventory/inventory_sources_vars/start']

    inventory = InventoryManager(loader=DataLoader())
    hosts = inventory.get_hosts()
    loader = DataLoader()

    data = get_vars_from_path(loader, context.CLIARGS['inventory'][0], hosts, 'task')
    assert data['test_var'] == 'test_var_value'
    assert data['test_var2'] == 'test_var2_value'

# Generated at 2022-06-13 17:38:20.171190
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    plugin = vars_loader.get("yaml_file")
    src = "./tests/integration/inventory_vars/plugins/"
    path = "./tests/integration/inventory_vars/group_vars/all/"
    host = Host("localhost")
    group = Group("test")

    entities = [host]

    data = get_vars_from_path(vars_loader, path, entities, "start")
    assert data['yaml_file_all'] == 'test_yaml_file_all'
    assert data['yaml_file_host'] == 'test_yaml_file_host'



# Generated at 2022-06-13 17:38:21.486204
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, '', None, None) == {}



# Generated at 2022-06-13 17:38:31.041271
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    class TestVars1(object):
        REQUIRES_WHITELIST = True
        def get_vars(self, loader, path, entities):
            return {
                "test": "test1"
            }

    class TestVars2(object):
        def get_vars(self, loader, path, entities):
            return {
                "test": "test2"
            }

    class TestVars3(object):
        def get_host_vars(self, host):
            return None

    class TestVars4(object):
        def get_group_vars(self, group):
            return None

    class TestVars5(object):
        def run(self):
            return None

    loader = object()
    path = object()
    entities = object()
    test_vars = Test

# Generated at 2022-06-13 17:38:36.339839
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    fake_loader = None
    fake_path = "/path/to/fake/file"
    fake_entities = ['fake_entity1', 'fake_entity2']
    fake_stage = 'fake_stage'

    # Fake variable plugins class
    class FakePlugin:
        def get_vars(self, loader, path, entities):
            return {
                "variable1": "var1",
                "variable2": "var2",
            }
    # Fake variable plugins loader
    class FakePluginLoader:
        def __init__(self):
            self.fake_plugin = FakePlugin()
        def all(self):
            return [self.fake_plugin]

    # Assert the expected results are returned when running get_vars_from_path
    vars_loader = FakePluginLoader()
    variables = get_vars_from