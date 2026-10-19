

# Generated at 2022-06-13 17:28:54.547274
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.plugins.loader import vars_loader
    from ansible.vars.vars_plugins.host_list import VarsModule
    from ansible.vars.vars_plugins.group_list import VarsModule as VarsGroupModule
    vars_loader.add('ansible.vars.vars_plugins.host_list', VarsModule())
    vars_loader.add('ansible.vars.vars_plugins.group_list', VarsGroupModule())
    # test vars plugin

# Generated at 2022-06-13 17:29:05.798816
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # monkey patch vars_loader.all to inject fake vars plugins
    vars_loader.all = lambda: (FakeVarsPlugin(a=1), FakeVarsPlugin(b=2), FakeVarsPlugin(c=3))
    loader, _ = vars_loader.get("vars_loader")

    # fake inventory sources
    # inventory source is a list of directories (like inventory source files) and hosts (they can be in a comma-separated list)
    sources = [
        './inventory_dir1',
        './inventory_dir2',
        './inventory_dir3',
        './inventory_dir4,localhost'
    ]

    # fake stage
    stage = 'inventory'

    # build list of Host and Group entities

# Generated at 2022-06-13 17:29:13.751957
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp()
    tmp_name = os.path.basename(tmp_dir)
    shutil.rmtree(tmp_dir, ignore_errors=True)
    # Fake the inventory directory setup

# Generated at 2022-06-13 17:29:23.980493
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    import ansible.plugins.loader
    from ansible.inventory.host import Host

    path = './test/vars_plugin'
    hosts = Host(name='localhost')
    data = get_vars_from_path(PathData(ansible.plugins.loader), path, [hosts], 'task')
    assert data.get('test_get_vars_from_path_host') is not None
    assert data.get('test_get_vars_from_path_host') == 'localhost'
    assert len(data) == 1

    data = get_vars_from_path(PathData(ansible.plugins.loader), path, ['localhost'], 'task')
    assert data.get('test_get_vars_from_path_host') is not None

# Generated at 2022-06-13 17:29:26.674497
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = '/home/user/test'
    entities = ['test']
    stage = 'inventory'
    data = get_vars_from_path(loader, path, entities, stage)
    print(data)

# Generated at 2022-06-13 17:29:37.367360
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager

    cli = CLI()
    display.verbosity = 0
    inv_manager = InventoryManager(inventory=cli.options.inventory.name, loader=cli.loader)
    inv_manager.parse_sources()
    inv_manager.add_group('test_group')
    inv_manager.groups[0].set_variable('test_group_var', 'test_group_value')
    inv_manager.add_host('test_host1')
    inv_manager.hosts[0].set_variable('test_host_var', 'test_host_value')
    inv_manager.hosts[0].set_variable('test_overriden_var', 'test_host_value')
    inv_manager.hosts[0].set_variable

# Generated at 2022-06-13 17:29:38.831475
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass



# Generated at 2022-06-13 17:29:49.486893
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    for path in [
        'test/test_vars_plugins/valid_dir/subdir',
        '/test/test_vars_plugins/valid_dir/subdir',
        '/test/test_vars_plugins/valid_dir/subdir/',
    ]:

        data = get_vars_from_path(loader, path, ['host1'], 'inventory')
        assert 'inventory_hostname' in data
        assert data['inventory_hostname'] == 'host1'
        assert 'inventory_dir' in data
        assert data['inventory_dir'] == path

        data = get_vars_from_path(loader, path, ['group1'], 'inventory')

# Generated at 2022-06-13 17:29:50.651221
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:29:51.283105
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:30:04.442786
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    loader = lambda x, y: None
    plugin = lambda: None
    plugin.get_vars = lambda l, p, e: {'x': 1}
    plugin._load_name = 'y'
    plugin._original_path = 'z'

    assert get_vars_from_path(loader, 'a', 'b', 'c') == {}

    class PluginClass:
        def __init__(self):
            self._load_name = 'y'
            self._original_path = 'z'

        def get_vars(self, loader, path, entities):
            return {'x': 2}

    assert get_vars_from_path(loader, 'a', 'b', 'c') == {}


# Generated at 2022-06-13 17:30:11.857225
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Test empty vars_plugin_list
    loader = None
    path = None
    entities = None
    stage = None
    assert {} == get_vars_from_path(loader, path, entities, stage)

    # Test vars_plugin_list with vars_plugin(get_vars(), get_host_vars() and get_group_vars())
    def get_vars_dict():
        return {'test_key': 'test_value'}
    vars_plugin_list = []
    vars_plugin_list.append(get_vars_dict)
    loader = None
    path = None
    entities = None
    stage = None
    assert {'test_key': 'test_value'} == get_vars_from_path(loader, path, entities, stage)

    # Test v

# Generated at 2022-06-13 17:30:12.780085
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:30:19.045759
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    C.RUN_VARS_PLUGINS = 'start'
    C.VARIABLE_PLUGINS_ENABLED = ['yaml_vars']
    display = Display()

    inventory = InventoryManager('tests/support/inventory/host_vars', loader=vars_loader)
    loader = vars_loader.get('yaml_vars')
    path = 'tests/support/inventory/host_vars'

    assert loader is not None
    assert path is not None

    # get_vars_from_path with host entities
    host = inventory.get_

# Generated at 2022-06-13 17:30:24.900300
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())
    stage = 'inventory'
    data = {}
    plugin = vars_plugin_list[8]
    path = os.path.dirname(__file__)
    entities = []
    data = combine_vars(data, get_plugin_vars(None, plugin, path, entities))
    assert len(data) == 1


# Generated at 2022-06-13 17:30:36.173467
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugins as vars_loader
    from ansible_collections.ansible.community.plugins.vars import caldera_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import fedora_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import freebsd_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import gentoo_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import openbsd_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import redhat_vars_plugin
    from ansible_collections.ansible.community.plugins.vars import rhel

# Generated at 2022-06-13 17:30:43.804462
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    args = dict(
        sources=["sources"],
        stage="task",
        entities=[],
    )

    from ansible.plugins.loader import vars_loader
    from ansible.inventory import Inventory
    loader = Inventory(args["sources"])
    vars_loader.add(VarsPlugin())

    data = get_vars_from_inventory_sources(loader, args["sources"], args["entities"], args["stage"])

    assert data["foo"] == "bar"

# Fake vars plugin

# Generated at 2022-06-13 17:30:53.910319
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Setup a fake vars plugin
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.vars.unsafe_proxy import UnsafeProxy

    class FakeVarsPlugin(object):

        def get_vars(self, loader, path, entities, cache=True):
            return {'test_var': 'test_value'}

    fvp = FakeVarsPlugin()
    vars_loader.add(fvp, 'fakevars')

    # Setup a fake loader
    class FakeLoader(object):
        def __init__(self):
            self._inventory_sources = ['all']

    loader = FakeLoader()

    # Setup a fake host
    class FakeHost(object):
        def __init__(self, host_name):
            self.name = host_name

    host = FakeHost

# Generated at 2022-06-13 17:31:00.827573
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.utils.addresses import parse_address
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    loader = AnsibleCollectionLoader()
    plugin = vars_loader.get(b'demo_vars')
    path = b"/tmp"
    host1 = Host.create(data=None, name=parse_address(b"localhost"))
    host2 = Host.create(data=None, name=parse_address(b"my_host"))
    inventory = InventoryManager(loader=loader, sources=u"/tmp/hosts")
    inventory.add_host(host=host1, group="all")
    inventory.add_host

# Generated at 2022-06-13 17:31:01.504907
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass


# Generated at 2022-06-13 17:31:15.630812
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.loader import InventoryLoader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    loader = InventoryLoader()
    inv = loader.load_from_file("./test/test_vars_from_path.yaml")

    # Initialize variable manager
    vars_manager = VariableManager(loader=loader, inventory=inv)

    # Get vars from a group
    group = inv.get_group("group_1")
    vars_from_group = get_vars_from_path(loader, "./", [group], "task")
    assert(vars_from_group['group_1_a'] == 'value_1_a')

    # Get vars from a host
    host = inv.get

# Generated at 2022-06-13 17:31:24.375564
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VarManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/inventory'])
    var_manager = VarManager()

    vars_from_inventory = get_vars_from_inventory_sources(loader, sources=inventory.get_sources(), entities=inventory.get_hosts(), stage='inventory')
    var_manager._vars_from_inventory = vars_from_inventory

    assert var_manager.set_host_variable('host_one', 'var1', value="a") == "a"
    assert var_manager.set_host_variable('host_one', 'var1', value="b") == "b"



# Generated at 2022-06-13 17:31:33.340156
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    ''' Test get_plugin_vars '''

    loader, inv_loader, play_ctx = setup_class()

    # test get_plugin_vars for a simple case
    test_plugin = vars_loader.get('_test_vars_plugin')
    assert test_plugin is not None

    test_host = Host('testhost')
    test_group = inv_loader._inventory.get_group('group1')
    test_entities = [test_host, test_group]

    test_data = get_plugin_vars(loader, test_plugin, '.', test_entities)
    assert test_data == {
        'testhost': {'host_var': 'host'},
        'group1': {'group1_var': 'group'},
    }

    # test get_plugin_vars

# Generated at 2022-06-13 17:31:35.222740
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO: test get_vars_from_path
    pass

# Generated at 2022-06-13 17:31:37.911124
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    loader = None
    plugin = vars_loader.get("fake")
    path = "/path/to/directory"
    entities = [Host("hostname")]
    data = get_plugin_vars(loader, plugin, path, entities)
    assert data == {}

# Generated at 2022-06-13 17:31:48.711050
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import vars_loader
    import collections

    # Create an inventory
    group1_dict = collections.defaultdict(dict)
    group1_dict['hosts']['host1.example.org'] = {'ansible_connection': 'local'}
    group1_dict['vars'] = {'g1v1': 'g1v1 value'}
    group1 = Group(name='group1', inventory=InventoryManager(loader=None))
    group1.vars = VariableManager()
    group1.vars.data = group1_dict['vars']

# Generated at 2022-06-13 17:31:59.086205
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # We need a testclass that implements the vars loader plugin interface
    class MockPlugin(object):
        def get_vars(self, *args, **kwargs):
            return {"foo": "bar"}

    # Create a mock loader
    loader = object()

    # Create a mock path
    path = "mock_path"

    # Create a mock entity
    entity = "mock_entity"

    # Create a mock plugin
    plugin = MockPlugin()

    # Call the function to test
    actual = get_plugin_vars(loader, plugin, path, entity)

    # Assert:
    assert actual["foo"] == "bar"


# Generated at 2022-06-13 17:32:05.249749
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    display.verbosity = 3

    inventory = InventoryManager(loader=DataLoader(), sources=['tests/inventory/vars_plugins/host_vars'])
    assert get_vars_from_inventory_sources(
        loader=inventory.loader,
        sources=['tests/inventory/vars_plugins/host_vars'],
        entities=inventory.hosts.values(),
        stage='inventory'
    ) == {'test_host': {'connection': 'smart'}}

# Generated at 2022-06-13 17:32:12.245286
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    path = "bar"

    mock_plugin = type('mock_plugin', (object,), {
        'get_vars': lambda self, loader, path, entities: {
            'bar': ['bar'],
        },
    })
    mock_plugin.__name__ = "mock_plugin"
    mock_plugin._load_name = "mock_plugin"
    mock_plugin._original_path = "/mypath"

    mock_loader = type('mock_loader', (object,), {
        'get': lambda self, key: None,
    })

    assert get_plugin_vars(mock_loader, mock_plugin, path, []) == {'bar': ['bar']}


# Generated at 2022-06-13 17:32:19.954445
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef

    plugin_name = 'testing_vars_plugin'
    collection_name = 'test'
    plugin_path = '/tmp/collection_ns/collection_name/plugins/vars/'
    plugin_file = '%s/%s.py' % (plugin_path, plugin_name)

# Generated at 2022-06-13 17:32:53.267812
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader

    class InventoryPlugin:
        def __init__(self, name):
            self._load_name = name

    class VarsPlugin:
        def __init__(self, name):
            self._load_name = name

        def get_vars(self, loader, path, entities):
            return {self._load_name: 1}

        def get_group_vars(self, group):
            return {self._load_name: 2}

        def get_host_vars(self, host):
            return {self._load_name: 2}

    class DeprecatedVarsPlugin:
        def __init__(self, name):
            self._load_name = name
            self.run = True

    # Load up inventory and vars plugins

# Generated at 2022-06-13 17:33:02.425373
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    Test the get_vars_from_path function for each of the vars plugins

    The test contains the following steps:
      1) create a mock vars plugin that declares the get_vars function
      2) create a loader with the test plugin and any other plugins that reference
         the same module path(s)
      3) call get_vars_from_path with the loader and the module path
      4) assert that the expected variables are present in the returned variables

    The get_vars_from_path function was refactored to account for v2 and v3 plugins
    and provide a common interface to all vars plugins. The function will raise an
    exception if an incompatible plugin is encountered.
    """

    # create an instance of the test class and add a function that will be mocked

# Generated at 2022-06-13 17:33:12.874243
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    host_vars = {
        'foo': 'bar',
        'baz': 'qux'
    }
    group_vars = {
        'group': 'bar',
        'qux': 'qux'
    }

    class MockInventoryPlugin():
        def get_vars(self, loader, path, entities):
            return {
                'foo': 'bar',
                'baz': 'qux',
                'group': 'bar',
                'qux': 'qux'
            }

        def get_host_vars(self, host):
            return host_vars

        def get_group_vars(self, group):
            return group_vars

        def get_option(self):
            return 'start'

    class MockVarsPlugin():
        has_option = False
        _

# Generated at 2022-06-13 17:33:18.621773
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.vars import combine_vars

    dirs = [get_vars_from_path, get_vars_from_inventory_sources]

    for func in dirs:
        result = func(None, [os.path.join(os.path.dirname(__file__), '../../test/units/vars/old_vars_plugin')], [], 'inventory')

# Generated at 2022-06-13 17:33:30.857350
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.plugins.vars import VarsModule

    class VarsModuleTest(VarsModule):
        ''' get_vars test plugin '''

        def get_vars(self, loader, path, entities):
            ''' this version of the plugin supports v2 of the callback interface '''
            return {'test_vars': 'vars_from_path'}

        def get_host_vars(self, host):
            ''' this version of the plugin supports v1 of the callback interface '''
            return {'test_vars': 'host_vars'}

    test_plugin = VarsModuleTest()


# Generated at 2022-06-13 17:33:39.746812
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    inv = InventoryManager()
    inv.loader = None
    inv.construct_portable_inventory = None
    inv.get_hosts = None
    inv.get_host = None
    inv.get_group = None
    inv.list_hosts = None
    inv.list_groups = None
    inv.groups = None

    # test for non-existing path
    inv.sources = [None]
    stage = 'task'
    entities = [inv]
    obtained = get_vars_from_inventory_sources(inv.loader, inv.sources, entities, stage)
    assert obtained == {}
    # test for valid path
    inv.sources = ["/etc", "/home"]
    stage = 'task'
    entities = [inv]
    obtained = get

# Generated at 2022-06-13 17:33:42.010936
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class MockPlugin:
        def get_vars(self, loader, path, entities):
            return {'test': 'vars'}

    loader = None
    plugin = MockPlugin()
    path = None
    entities = [object]
    assert get_plugin_vars(loader, plugin, path, entities) == {'test': 'vars'}



# Generated at 2022-06-13 17:33:44.790013
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # init data
    sources = ['foo.yml']
    entities = [Host('foo')]
    stage = 'inventory'

    # start test
    assert get_vars_from_path(None, sources[0], entities, stage) == None

# Generated at 2022-06-13 17:33:48.638206
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    plugin = vars_loader.get("yaml")
    entities = ['yaml_host']
    path = '/tmp'

    data = get_vars_from_path(None, path, entities, 'start')

    print(data)



# Generated at 2022-06-13 17:33:58.767771
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    import ansible.plugins.vars
    import ansible.plugins.vars.host_group_vars
    import ansible.plugins.vars.group_vars
    import ansible.plugins.vars.yaml
    import ansible.plugins.vars.ini
    import ansible.plugins.vars.json
    import ansible.plugins.vars.toml

    class TestLoader(object):
        def load_from_file(self, *a, **kw):
            return {}

    group_name = 'test'
    host_name = '127.0.0.1'
    path = __file__
    entities = [Group(group_name), Host(host_name)]
    loader = TestLoader()

   

# Generated at 2022-06-13 17:34:27.811369
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import collections
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Create an inventory manager
    loader = DataLoader()
    i_mgr = InventoryManager(loader, './test/')

    # load the inventory file
    test_inventory_data = i_mgr.get_inventory_sources('./test/unit/inventory/test_inventory_source_vars_plugin')

    class Host1(collections.namedtuple('Host1', ['name'])):
        def __getitem__(self, item):
            return getattr(self, item)

    class Host2(collections.namedtuple('Host2', ['name'])):
        def __getitem__(self, item):
            return getattr(self, item)


# Generated at 2022-06-13 17:34:36.280023
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import unittest
    class TestGetVarsFromPath(unittest.TestCase):
        def setUp(self):
            self.plugin = mock.Mock()
            self.plugin.get_vars = mock.Mock(return_value={'a': 'foo'})
            self.plugin.get_host_vars = mock.Mock(return_value={'b': 'foo'})
            self.plugin.get_group_vars = mock.Mock(return_value={'c': 'foo'})
            self.display = mock.Mock()

        def test_get_vars(self):
            data = {}
            data = get_plugin_vars(self.plugin, None, 'host', 'host')
            self.assertIsInstance(data, dict)


# Generated at 2022-06-13 17:34:42.794941
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    ''' Test function to return plugin vars '''

    from ansible.inventory.host import Host
    from ansible.plugins.loader import vars_loader

    file_loader = vars_loader.get('file')
    assert file_loader

    host = Host('test')
    entities = [host]

    loader = None
    path = 'test.yml'
    assert get_plugin_vars(loader, file_loader, path, entities) == {}

# Generated at 2022-06-13 17:34:47.465833
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import DictVars

    class DictVarsDummy(DictVars):
        def get_vars(self, loader, path, entities, cache=True):
            return {'foo': 'bar'}

    class DictVarsDummy2(DictVars):
        def get_host_vars(self, host):
            return {'baz': 'bam'}

        def get_group_vars(self, group):
            return {'bleep': 'bloop'}

    class DictVarsDummy3(DictVars):
        def run(self, host):
            pass


# Generated at 2022-06-13 17:34:54.911663
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # pylint: disable=redefined-outer-name
    def plugin_factory(name):
        class Plugin(object):
            def get_vars(self, loader, path, entities):
                return {name: {'var1': 'val1', 'var2': 'val2'}}

            def get_option(self, option):
                return {'stage': 'all'}[option]
        return Plugin()

    loader = object()
    path = object()
    entity = object()

    loader, entity = object(), object()
    path = object()
    assert get_vars_from_path(loader, path, [entity], 'inventory') == {}

    loader, entity, plugin = object(), object(), plugin_factory('plugin1')
    path = object()

# Generated at 2022-06-13 17:34:55.826834
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path() == {}

# Generated at 2022-06-13 17:35:03.383592
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_plugin = vars_loader.get('vars')
    data = get_vars_from_path(vars_loader, os.path.dirname(os.path.realpath(__file__)), {'test_inventory': {}}, 'inventory')
    assert data['test_variable']['test_key'] == 'test_value', "could not retrieve vars from test_vars.yaml"
    assert test_plugin.get_option('stage') == None, "test_vars.yaml is not populated with plugin specific stage: None"



# Generated at 2022-06-13 17:35:10.833314
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugins
    loader = vars_loader

    plugin_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'plugins', 'vars', '__init__.py')
    plugin = vars_plugins['vars'](loader=loader, path=plugin_path)
    entities = []

    data = get_plugin_vars(loader, plugin, None, entities)

    assert 'ansible_facts' in data

# Generated at 2022-06-13 17:35:19.274519
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader_mock = MagicMock()
    path = '/path/to/playbook'
    entities = [MagicMock()]
    stage = 'inventory'
    var_plugin_mock = Mock()
    var_plugin_mock.get_vars = MagicMock(return_value={})
    var_plugin_mock.get_host_vars = MagicMock(return_value={})
    var_plugin_mock.get_group_vars = MagicMock(return_value={})
    var_plugin_mock._load_name = 'var_plugin_mock'
    var_plugin_mock._original_path = 'var_plugin_mock_path'


# Generated at 2022-06-13 17:35:22.539094
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    loader = vars_loader
    path = './tests/'
    entities = {}
    stage = 'inventory'
    result = get_vars_from_path(loader, path, entities, stage)


if __name__ == "__main__":
    test_get_vars_from_path()

# Generated at 2022-06-13 17:36:04.377070
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    from ansible.plugins import vars_plugins

    class MyTestPlugin(object):
        '''
        A plugin to test host and group vars
        '''

        def get_vars(self, loader, path, entities):
            return {'x': 1}

        def get_group_vars(self, host):
            return {'g': 'group'}

        def get_host_vars(self, host):
            return {'h': 'host'}

    class MyTestPlugin2(object):

        def get_vars(self, loader, path, entities):
            return {'x': 2}

    class MyTestPlugin3(object):
        '''
        A plugin to test error handling
        '''

        def run(self, host):
            return {'x': 100}


# Generated at 2022-06-13 17:36:15.838882
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    loader = None
    path = '../../../test/units/vars/'
    host = Host(name='localhost')
    group = Host()
    group.name = 'group'
    group.vars = {'group_var': 'group_var_value'}
    group.hosts = [host]

    data = get_vars_from_path(loader, path, [host, group], 'inventory')
    assert 'a' == data['a']
    assert 'b' == data['b']
    assert 'c' == data['c']
    assert 'd' == data['d']
    assert 'e' == data['e']
    assert 'f' == data['f']
    assert 'g' == data['g']
    assert 'h' == data['h']

# Generated at 2022-06-13 17:36:24.192865
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert os.path.isdir(to_bytes('test/data/vars_plugin_dir'))
    assert os.path.isdir(to_bytes('test/data/vars_plugin_dir/inventory_vars'))
    assert os.path.isfile(to_bytes('test/data/vars_plugin_dir/inventory_vars/vars.yml'))
    assert os.path.isdir(to_bytes('test/data/vars_plugin_dir/group_vars'))
    assert os.path.isfile(to_bytes('test/data/vars_plugin_dir/group_vars/all.yml'))
    assert os.path.isdir(to_bytes('test/data/vars_plugin_dir/host_vars'))
    assert os.path.isf

# Generated at 2022-06-13 17:36:25.027974
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:36:35.260194
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    test_cases = {
        'test_case_1': {
            'path': '/home/ansible/test_test/',
            'entities': {},
            'stage': 'inventory',
            'expected_result': {}
        }
    }

    def get_plugin_vars(loader, plugin, path, entities):
        ansible_vars = []
        ansible_vars.append({'name': 'ansible_version', 'value': '2.9.12'})
        ansible_vars.append({'name': 'inventory_file', 'value': '/etc/ansible/hosts'})
        ansible_vars.append({'name': 'inventory_dir', 'value': '/etc/ansible'})

# Generated at 2022-06-13 17:36:42.103322
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = Inventory(loader, 'localhost,')
    inv.parse_inventory(path=dict(hosts=['localhost']))
    inv_sources = ['test/integration/inventory_base.yml']
    data = get_vars_from_path(loader, inv_sources[0], inv.groups.values(), 'inventory')
    assert data


# Generated at 2022-06-13 17:36:42.940793
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:36:46.127450
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_loader = vars_loader()
    assert isinstance(test_loader, vars_loader)
    test_path = '/tmp/test'
    test_entities = ['test']
    test_stage = 'inventory'
    assert 'data' == get_vars_from_path(test_loader, test_path, test_entities, test_stage)

# Generated at 2022-06-13 17:36:55.556119
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins import vars as vars_plugins

    # given
    vars_plugin_list = list(vars_loader.all())
    plugin_name = 'vars_plugins.my_var_plugin'
    vars_plugin_name = vars_loader.get(plugin_name)
    vars_plugin_list.append(vars_plugin_name)

    entities = ['localhost']
    path = '.'

    # when
    data = get_plugin_vars(vars_loader, vars_plugin_name, path, entities)

    # then
    assert data['my_var'] == 'my_value'



# Generated at 2022-06-13 17:37:04.332267
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """ Exercising function get_vars_from_path with various plugins """

    import ansible.plugins.vars
    import ansible.plugins.vars.system

    from ansible_collections.ansible.example.plugins.vars import test

    loader = None
    entities = None
    stage = None

    # Good plugin, no stage
    path = '/path/to/something'
    data = get_vars_from_path(loader, path, entities, stage)
    assert type(data) == dict
    assert data == {}

    # Old format plugin, should not run
    path = '/path/to/something'
    data = get_vars_from_path(loader, path, entities, stage)
    assert type(data) == dict
    assert data == {}

    # Good plugin, all

# Generated at 2022-06-13 17:38:26.264858
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import test_vars_plugin

    loader = vars_loader
    plugin = test_vars_plugin.TestVarsModule()
    path = "/"
    entities = ['localhost']

    data = get_plugin_vars(loader, plugin, path, entities)
    assert data == {'var_name': 'var_value'}


# Generated at 2022-06-13 17:38:35.094391
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.vars import auto
    from ansible.plugins.vars.hashivault import HashivaultVars
    from ansible.utils.display import Display
    test_display = Display()
    test_vars_loader = vars_loader.VarsModuleLoader()
    test_vars_loader.add_directory(os.path.join(os.path.dirname(auto.__file__), '..', 'vars'))
    test_vars_loader.add_directory(os.path.join(os.path.dirname(HashivaultVars.__file__), '..', 'vars'))
    test_vars_loader.rescan_paths()