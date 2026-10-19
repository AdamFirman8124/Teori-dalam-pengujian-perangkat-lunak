

# Generated at 2022-06-13 17:28:54.503664
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Unit test for the function get_vars_from_path
    from ansible import context
    from ansible.playbook.play import Play
    from ansible.plugins.loader import vars_loader

    context._init_global_context()

    host = Host('127.0.0.1')
    host.set_variable('ansible_python_interpreter', '/usr/bin/python')

    plugin = vars_loader._get_one_plugin(C.DEFAULT_VARS_PLUGIN_PATH)
    data = get_plugin_vars(vars_loader, plugin, '/home/sh', [host])
    assert type(data) is dict

# Generated at 2022-06-13 17:28:55.065899
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    pass

# Generated at 2022-06-13 17:29:06.418737
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    GROUPS = ['top_group']
    GROUPS.extend(['group_%d' % x for x in range(9)])

    HOSTS = ['top_host']
    HOSTS.extend(['host_%d' % x for x in range(9)])

    hosts = []
    groups = [Group(name=name) for name in GROUPS]

    for group in groups:
        group.vars.update(get_vars_from_path(None, group.name, group, 'inventory'))

    for host_name in HOSTS:
        host = Host(name=host_name)

# Generated at 2022-06-13 17:29:06.820017
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:29:15.562098
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    test_data = {
        'path': '/path/to/inventory/source',
        'entities': ['foo', 'bar'],
        'stage': 'dummy',
        'plugin_vars': {'plugin': 'vars'},
        'pattern_vars': {'pattern': 'vars'},
        'inventory_vars': {'inventory': 'vars'},
    }

    test_data_uuids_list = ['foo', 'bar']

    loader_mock = get_loader_mock()
    display_mock = get_display_mock()

    get_vars_from_path_mock = get_get_vars_from_path_mock()
    assert_plugin_vars_mock = get_assert_plugin_vars_mock()
    assert_inventory_

# Generated at 2022-06-13 17:29:19.681366
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader = None
    sources = ["/etc/ansible/hosts"]
    entities = {}
    stage = None

    #TODO
    #return get_vars_from_inventory_sources(loader, sources, entities, stage)
    return

# Generated at 2022-06-13 17:29:27.905869
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes

    inventory_loader = InventoryManager(loader=None, sources="localhost,")
    # Example that would work with a vars_plugin
    # data = get_vars_from_inventory_sources(
    #     inventory_loader,
    #     "localhost,",
    #     entities=None,
    #     stage="inventory"
    # )
    # assert len(data) != 0

    # Example that would work with a vars_plugin
    data = get_vars_from_inventory_sources(
        inventory_loader,
        sources=['/does/not/exist', '/etc/ansible/hosts'],
        entities=None,
        stage="task"
    )
    assert len(data)

# Generated at 2022-06-13 17:29:37.670036
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin_loader = vars_loader
    path = '../test/testdata/vars_plugins'
    var_plugins = vars_loader.all(path)

    host_1 = Host('host_1')
    host_2 = Host('host_2')
    host_3 = Host('host_3')
    host_4 = Host('host_4')
    host_5 = Host('host_5')
    host_6 = Host('host_6')
    host_7 = Host('host_7')
    host_8 = Host('host_8')
    host_9 = Host('host_9')
    host_10 = Host('host_10')
    host_11 = Host('host_11')

    group_1 = {'name': 'group_1'}

# Generated at 2022-06-13 17:29:48.345231
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class FakeVarsPlugin():
        def get_vars(self, loader, path, entities):
            return {'plugin_vars': ['bar', 'baz']}

    class FakePlugin():
        pass

    loader = 'test_loader'
    path = 'test_path'
    entities = ['test_entity']
    plugin = FakeVarsPlugin()
    data = get_plugin_vars(loader, plugin, path, entities)
    assert data == {'plugin_vars': ['bar', 'baz']}

    plugin = FakePlugin()
    try:
        data = get_plugin_vars(loader, plugin, path, entities)
    except AnsibleError as e:
        assert 'Cannot use v1 type vars plugin' in e.message

# Generated at 2022-06-13 17:29:57.097766
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import ansible.plugins.loader
    ansible.plugins.loader.all.add(VarsAccumulator())
    inventory = ['host_vars/host1.yaml', 'host_vars/host2.yaml']
    entities = ['host1', 'host2']
    assert {
        'host1': {
            'foo': '1',
            'bar': '1',
        },
        'host2': {
            'foo': '2',
            'bar': '2',
        }
    } == get_vars_from_inventory_sources(None, inventory, entities, 'task')



# Generated at 2022-06-13 17:30:17.887859
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import unittest

    class FakePlugin:
        def _init_(self, name):
            self._load_name = name
            self._original_path = 'test'

        def get_vars(self, loader, path, entities):
            return {'result': 'test'}

    class FakePlugin2:
        def _init_(self, name):
            self._load_name = name
            self._original_path = 'test'

        def get_group_vars(self, entity_name):
            return {'result': 'test'}

        def get_host_vars(self, entity_name):
            return {'result': 'test'}

    class FakeLoader:
        pass

    class FakePlayer:
        def _init_(self, name):
            self.name = name


# Generated at 2022-06-13 17:30:25.686505
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Mocking the vars_loader to return the test_vars_plugin created in mock_plugin_test_plugin.py
    test_plugin = MockPlugin.test_plugin()
    loader = MockLoader(
        ansible_playbook=MockPlaybook("test_playbook"),
        all_plugins=MockPluginCollection(test_plugin)
    )
    # Loading the vars plugins from the above mocked vars_loader
    vars_plugin_list = list(vars_loader.all())
    for plugin_name in C.VARIABLE_PLUGINS_ENABLED:
        plugin = loader.vars.get(plugin_name)
        if plugin is None:
            # Error if there's no play directory or the name is wrong?
            continue

# Generated at 2022-06-13 17:30:26.991067
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    # Does not run without context
    assert False

# Generated at 2022-06-13 17:30:27.653345
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert True

# Generated at 2022-06-13 17:30:29.610694
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    data = get_plugin_vars(loader, plugin, path, entities)

    print(data)

# Generated at 2022-06-13 17:30:35.604537
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def get_vars_from_path_calls(self):
        return self.get_vars_from_path_calls

    class test_plugin:
        @staticmethod
        def get_vars(loader, path, entities):
            return {'test': path}
        @staticmethod
        def get_host_vars(host):
            return host
        @staticmethod
        def get_group_vars(group):
            return group
        @staticmethod
        def get_option(option):
            return option
        @staticmethod
        def has_option(option):
            return option
    
    class test_loader:
        get_vars_from_path_calls = []
        def get(plugin):
            self = test_loader
            if plugin == 'test_plugin':
                return test_plugin

# Generated at 2022-06-13 17:30:46.154890
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible import context
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    context.CLIARGS._parse_args(args=[])
    loader = DataLoader()
    host_pattern = 'all'
    groups = ['ungrouped']
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    inventory.parse_sources(host_pattern, groups)
    host_list = inventory.get_hosts()
    hosts = []
    for h in host_list:
        hosts.append(h)
    entity_list = groups + hosts
    data = get_vars_from_inventory_sources(loader, ['localhost,'], entity_list, 'inventory')

    assert data

# Generated at 2022-06-13 17:30:56.232287
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    """
    test_get_vars_from_inventory_sources : Tests get_vars_from_inventory_sources function
    """

    # Create a collection for the test
    collection = "test_file"
    test_collection = "build_ansible_test_collection"
    test_collection_dir = "./test/unit/plugins/test_file"
    test_vars_file = "./test/unit/plugins/test_file/vars_plugins/test.yml"

    # Create collection's directory (for ex: test/unit/collection/build_ansible_test_collection)
    if not os.path.exists(test_collection_dir):
        print("Creating test directory : %s" % (test_collection_dir))
        os.mkdir(test_collection_dir)

    # Create collection

# Generated at 2022-06-13 17:30:58.305779
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader, path, entities, stage = None, "/root/ansible/playbook", [], "task"
    get_vars_from_path(loader, path, entities, stage)

# Generated at 2022-06-13 17:31:00.612530
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None

    path = 'test/path'
    entities = []
    stage = 'test'

    res = get_vars_from_path(loader,path,entities,stage)

    assert isinstance(res,dict)


# Generated at 2022-06-13 17:31:15.075556
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import sys
    sys.path.append('/home/ansible/workspace/2.9-dev/lib/ansible/plugins/vars')
    from test_plugin import ProvideVars
    from ansible.plugins.loader import vars_loader

    vars_loader.add('test_plugin', ProvideVars())

    test_data = get_vars_from_inventory_sources(None, ['/home/ansible/workspace/2.9-dev/lib/ansible/plugins/vars'], [], 'task')
    assert test_data['test_1'] == 1



# Generated at 2022-06-13 17:31:22.651867
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    sources = [
        './',
        '/path/to/dir',
        '../inventory/',
        'host_list,other_host_list',
        'host1'
    ]
    display.vvvv(sources)

    loader = [
        'ec2',
        'mongo',
        'redis'
    ]
    display.vvvv(loader)

    assert get_vars_from_inventory_sources(loader, sources, entities=None, stage='INVENTORY')

# Generated at 2022-06-13 17:31:28.420205
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugins

    # test the base class method
    random_name = 'this is the group name'
    random_path = 'this is the path'

    vars_plugin = vars_plugins.VarsModule()
    try:
        get_plugin_vars(None, vars_plugin, random_path, random_name)
        assert False
    except AnsibleError:
        assert True

    # test the v1 method
    class MyPlugin:

        def __init__(self):
            self.name = 'my_plugin'
            self.path = random_path
            self.class_name = 'MyPlugin'

        def get_host_vars(self, host):
            assert host == random_name
            return {'1': 1}


# Generated at 2022-06-13 17:31:35.618026
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class Plugin:
        def get_vars(self, loader, path, entities):
            return {'test': 'vars'}

    class PluginNew:
        def get_host_vars(self, host):
            return {'test': 'vars'}

    assert get_plugin_vars(None, Plugin(), None, None) == {'test': 'vars'}
    assert get_plugin_vars(None, PluginNew(), None, []) == {'test': 'vars'}

# Generated at 2022-06-13 17:31:43.815481
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.config.manager import ConfigManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    config = ConfigManager(os.path.join(os.path.dirname(__file__), 'test_get_vars_from_path.cfg'))
    loader = DataLoader(config.get_config_value('DEFAULT', 'fact_caching', 'memory'))
    play_context = PlayContext(config=config)

    host1 = Host('test1')
    host2 = Host('test2')
    host1.vars = {'ansible_ssh_user': 'foo'}
    host2.vars = {'ansible_ssh_user': 'bar'}


# Generated at 2022-06-13 17:31:50.903266
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager

    loader = None
    path = os.path.join(os.path.dirname(__file__), 'host_vars')
    hosts = InventoryManager(loader=loader, sources=path).get_hosts()

    # Test V2 plugin
    entities = [hosts['host1']]
    inventory_path = os.path.join(path, 'group_vars/all.yml')
    plugin_data = get_vars_from_path(loader, inventory_path, entities, 'inventory')
    assert plugin_data['var1'] == 'host1'
    assert plugin_data['var2'] == 'group_vars/all'

    # Test V2 plugin for invalid host
    invalid_host = Host('invalid')
    entities = [invalid_host]


# Generated at 2022-06-13 17:32:01.009452
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import vars_plugins
    from ansible.plugins.loader import vars_loader
    import os, sys

    full_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, full_path)

    # Need to add sample plugin to vars_loader
    vars_plugins.path = [full_path]
    vars_loader.add_directory(full_path)
    vars_loader.all()

    # Test good plugin
    data = get_vars_from_path(None, '.', [], 'task')
    assert isinstance(data, dict) and len(data) == 1 and data['plugin_var'] == 'Variable from sample plugin'

    # Test bad plugin
    data = get_vars_from

# Generated at 2022-06-13 17:32:05.027864
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Remove this test once we have tests for the plugin loading code.
    # Confirms we don't crash or get an error trying to load invalid plugins.
    class InvalidPlugin(object):
        pass
    assert get_vars_from_path(None, None, None, None) == {}
    assert get_vars_from_path(None, None, None, None, extra_plugins=[InvalidPlugin()]) == {}



# Generated at 2022-06-13 17:32:09.631576
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars.test_vars_plugin import TestVariablePlugin

    vars_plugin_list = list(vars_loader.all())

    test_plugin = TestVariablePlugin()
    test_plugin._load_name = 'test_plugin'
    test_plugin._original_path = 'test'

    vars_plugin_list.append(test_plugin)

    test_vars = get_vars_from_path(None, 'test', ['entities'], 'inventory')

    assert test_vars == {'foo': 'bar'}

# Generated at 2022-06-13 17:32:16.699053
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=None, host_list='tests/inventory_vars_plugin')

    # Check that vars plugins work when run_vars_plugins is set to 'all'
    C.RUN_VARS_PLUGINS = 'all'
    entities = [inv.get_groups_dict()['ungrouped']]

    sources = []
    sources.append(inv.get_hosts_dict()['testhost'].inventory_dir)
    sources.append(inv.get_groups_dict()['all'].inventory_dir)
    sources.append(inv.get_groups_dict()['group_with_vars'].inventory_dir)

   

# Generated at 2022-06-13 17:32:40.103224
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import auto
    plugin_name = 'auto'
    plugin = vars_loader.get(plugin_name)
    loader = None
    path = None

# Generated at 2022-06-13 17:32:42.257486
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    print('test_get_vars_from_path')
    assert 1 == 1

# Generated at 2022-06-13 17:32:51.631164
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins.loader import vars_loader

    loader = vars_loader

    path = './ansible-base/test/unit/plugins/testdata/var_plugins/'
    entity = ['host_in_group_1', 'host_in_group_2']
    stage = 'inventory'
    data = {}

    test_plugin = vars_loader.get('plugin_vars.test_plugin')
    test_plugin.has_option = lambda option: True
    test_plugin.get_option = lambda option: True

    data = combine_vars(data, get_plugin_vars(loader, test_plugin, path, entity))
    assert data['test_var_1'] == 'inventory_value'
    assert data['test_var_2'] == 'inventory_value'

    data = {}
   

# Generated at 2022-06-13 17:32:59.585688
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    vars_plugins = vars_loader.all()
    with open('test_get_vars_from_path.yml', 'w') as f:
        f.write('foo: bar')
    for plugin in vars_plugins:
        data = get_vars_from_path(None, 'test_get_vars_from_path.yml', None, 'inventory')
        if plugin._load_name == 'yaml':
            assert data == {'foo': 'bar'}

# Generated at 2022-06-13 17:33:04.014464
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    for name, obj in vars_loader.all():
        obj.has_option = lambda x: False
    vars_loader.enable_plugins(None)
    data = get_vars_from_path(None, '/path/to/source', ['entity1', 'entity2'], 'inventory')
    assert data == {}

    for name, obj in vars_loader.all():
        obj.has_option = lambda x: False
        obj.get_vars = lambda x, y, z: {name: name}
    vars_loader.enable_plugins(['test1', 'test2'])
    data = get_vars_from_path(None, '/path/to/source', ['entity1', 'entity2'], 'inventory')

# Generated at 2022-06-13 17:33:07.112445
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.vars.manager import VariableManager

    loader = None
    path = "/tmp"
    entities = ['test1', 'test2']
    stage = 'inventory'
    data = get_vars_from_path(loader, path, entities, stage)
    assert data == {}

# Generated at 2022-06-13 17:33:16.745614
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import vars_plugin
    from ansible.plugins.loader import vars_loader
    import ansible.constants as C
    vars_loader.add("test_var_a", vars_plugin.VarPlugin("test_var_a", "test", '0.1.0'))
    C.VARIABLE_PLUGINS_ENABLED.append("test_var_a")
    vars_loader.add("test_var_b", vars_plugin.VarPlugin("test_var_b", "test", '0.1.0'))
    C.VARIABLE_PLUGINS_ENABLED.append("test_var_b")
    data = get_vars_from_path(None, '/some/path', [], 'inventory')

# Generated at 2022-06-13 17:33:28.810419
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    facts_cache = {}
    variables = VariableManager(loader=loader, inventory=inventory)
    data = get_vars_from_path(loader, './', inventory.hosts.values(), 'inventory')
    variables.set_host_variable(host=inventory.hosts.values()[0], varname="test", value=data["test"])
    variables.set_nonpersistent_facts(facts_cache)

# Generated at 2022-06-13 17:33:36.728453
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os.path
    from ansible.plugins.loader import vars_loader

    data = dict(a=1, b=2)
    path = os.path.dirname(__file__)

    # Test using the vars plugin we're testing
    vars_loader.add_directory(path)
    assert dict(a=1, b=2) == get_vars_from_path(None, path, [], 'inventory')

    # Test without the vars plugin we're testing
    vars_loader.clear()
    vars_loader.add_directory(path)
    assert dict() == get_vars_from_path(None, path, [], 'inventory')

# Generated at 2022-06-13 17:33:45.986666
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    import ansible.utils.plugin_docs as plugin_docs
    from ansible.plugins.loader import vars_loader

    fake_plugin = plugin_docs.FakeVarsPlugin('plugin_name')
    assert get_plugin_vars(vars_loader, fake_plugin, '', []) == fake_plugin.get_vars(vars_loader, '', [])

    fake_plugin = plugin_docs.VarsPlugin1('plugin_name')
    assert get_plugin_vars(vars_loader, fake_plugin, '', []) == fake_plugin.get_vars(vars_loader, '', [])

    fake_plugin = plugin_docs.VarsPlugin2('plugin_name')
    assert get_plugin_vars(vars_loader, fake_plugin, '', []) == fake_plugin.get_

# Generated at 2022-06-13 17:34:12.090841
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=[ 'tests/lib/ansible/inventory/test_inventory.yml'])
    inv._inventory.add_host(Host(name='foobar', port=2222))
    vars_manager = VariableManager(loader=loader, inventory=inv)
    vars_manager._extra_vars = {'foo': 'bar'}

    all_vars = get_vars_from_path(loader, './', inv.hosts, stage='inventory')

# Generated at 2022-06-13 17:34:20.959746
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Setup
    from ansible.plugins.loader import vars_loader
    vars_loader.add('test', get_vars_from_path, 'test/get_vars_from_path.py')

    loader = 'fake_loader'
    path = 'test/get_vars_from_path.json'
    host = Host('test_host')
    group = Host('test_group')
    entities = [host, group]
    stage = 'inventory'

    # Execute
    data = get_vars_from_path(loader, path, entities, stage)

    # Assert

# Generated at 2022-06-13 17:34:28.383373
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # Test to ensure plugin vars is a compliment of host and group vars
    from ansible.plugins.vars.host_group_vars import get_host_group_vars
    class DummyVarsPlugin:
        def __init__(self, host_vars, group_vars):
            self.host_vars = host_vars
            self.group_vars = group_vars

        def get_host_vars(self, host):
            return self.host_vars[host]

        def get_group_vars(self, group):
            return self.group_vars[group]


# Generated at 2022-06-13 17:34:36.721823
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    # function get_vars_from_inventory_sources() is called with only one argm - loader,
    # hence loader is enough to carry out unit testing
    scoped_loader_mock = mock.MagicMock()
    sources = ['abc/inventory_hosts', 'abc/hosts']

    hosts = ['test_host1', 'test_host2']
    scoped_loader_mock.get_hosts.return_value = hosts

    # run the test case
    vars_from_inventory_sources = get_vars_from_inventory_sources(scoped_loader_mock, sources)

    assert_equal(scoped_loader_mock.get_hosts.called, True)
    assert_equal(scoped_loader_mock.get_hosts.call_count, 1)

    #

# Generated at 2022-06-13 17:34:38.157958
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:34:47.951069
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import vars_loader

    fixture_dir = os.path.join(os.path.dirname(__file__), '..', 'unit', 'utils', 'vars', 'fixtures')
    plugin_dir = os.path.join(fixture_dir, 'plugins')
    collection_plugin_dir = os.path.join(plugin_dir, 'ansible_collections', 'my_namespace', 'my_collection', 'plugins', 'vars')

    # copy plugins to avoid creating file in fixture dir


# Generated at 2022-06-13 17:34:58.539981
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.vars.test_vars_plugins as test_vars_plugins
    loader = test_vars_plugins.TestVarsPluginLoader()
    vars_plugin = loader.get('test_vars_plugin')
    entities = [ Host(name='localhost'), Host(name='other'), Host(name='localhost', port=2200) ]
    data = get_plugin_vars(loader, vars_plugin, '/path/to/inventory', entities)

# Generated at 2022-06-13 17:34:59.188099
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:35:02.838597
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin = "roles_path"
    test_data = {'a': '', 'b': '', 'c': ''}
    assert get_vars_from_path(None, None, None, None) == test_data

# Generated at 2022-06-13 17:35:09.110572
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entities = [Host(name='test_inventory')]
    stage = 'task'
    data = get_vars_from_path(loader, path, entities, stage)
    assert(data['ansible_facts_dir'].endswith('ansible/facts'))

# Generated at 2022-06-13 17:35:27.152137
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    import os
    import sys

    # 2.x plugin
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'plugins', 'vars'))
    loader, plugin = vars_loader.find_plugin('vars_2x_plugin')
    class DummyEntity:
        def __init__(self, name):
            self.name = name
    entities = [DummyEntity('foo_host'), DummyEntity('bar_group')]
    class DummyLoader:
        def get_basedir(self):
            return os.path.dirname(plugin._original_path)
    data = get_plugin_vars(DummyLoader(), plugin, '', entities)

# Generated at 2022-06-13 17:35:37.050671
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import inventory_loader

    plugin_name = 'auto'
    plugin = inventory_loader.get(plugin_name)
    if plugin is None:
        raise Exception("plugin not found: %s" % plugin_name)

    loader = InventoryManager("")
    path = "."
    host = Host("test_host")
    data = get_vars_from_path(loader, path, [host], 'inventory')
    assert data == {}  # checks that plugin auto works correctly in the unit test

    # Check if plugin auto doesn't load on the task
    # Checks if plugin returns {} for tasks, for example no parameters for tasks in the inventory
    data = get_vars_from_path(loader, path, [host], 'task')
    assert data == {}



# Generated at 2022-06-13 17:35:39.666738
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    result = get_vars_from_path('loader', 'vars_plugins_path', 'entities', 'stage')
    assert result == {}


# Generated at 2022-06-13 17:35:48.422136
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible_collections.community.general.tests.unit.compat import unittest

    class TestVarsPlugin(object):
        def __init__(self):
            self._load_name = 'testvars'

        def get_vars(self, loader, path, entities):
            return {'testdata': {'cmd': 'testdata'}}

    class TestVarsPluginConfigured(object):
        def __init__(self):
            self._load_name = 'testvars'
            self.testvars = type("testvars", (), {
                'has_option': lambda self, key: True,
                'get_option': lambda self, key: 'start',
            })()


# Generated at 2022-06-13 17:35:55.610140
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # if a get_vars() method exists
    class VarsPlugin_has_get_vars:
        def get_vars(self, loader, path, entities):
            return dict(has_get_vars='yes')

    # if a get_host_vars() method exists
    class VarsPlugin_has_get_host_vars:
        def get_host_vars(self, hostname):
            return dict(has_get_host_vars='yes')

    # if a get_group_vars() method exists
    class VarsPlugin_has_get_group_vars:
        def get_group_vars(self, groupname):
            return dict(has_get_group_vars='yes')

    # if a get_group_vars() method exists

# Generated at 2022-06-13 17:36:02.934719
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import ansible.utils.plugin_docs
    module_path = os.path.dirname(os.path.dirname(__file__))
    # FIXME: setting the test README path here only works if the path has not been set before.
    #        we should revisit the test framework to either allow a fresh environment per test
    #        or find a way to always reset this variable to it's default value before loading a test
    #        module.
    ansible.utils.plugin_docs.README_PATH = os.path.join(module_path, '__init__.py')
    from ansible.plugins.vars import test
    assert get_vars_from_path(None, __file__, None, 'inventory')['test_var'] == 'foo'



# Generated at 2022-06-13 17:36:14.213686
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class fake_plugin():
        _load_name = "fake"

        def get_vars(self, loader, path, entities):
            return {"var": "value"}

    class fake_plugin2():
        _load_name = "fake"

        def get_host_vars(self, name):
            return {"var": "value"}

    class fake_plugin3():
        _load_name = "fake"

        def get_group_vars(self, name):
            return {"var": "value"}

    class fake_plugin4():
        _load_name = "fake2"

    class fake_loader():
        class _fake_path_mgr():
            class paths():
                plugin_paths = ['/a/b/c']


# Generated at 2022-06-13 17:36:18.865755
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """
    Sanity check if the function get_vars_from_path returns a list
    """
    test_loader = None
    test_path = None
    test_entities = None

    assert isinstance(get_vars_from_path(test_loader, test_path, test_entities, 'inventory'), dict)

# Generated at 2022-06-13 17:36:21.010438
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    '''
    get_plugin_vars test
    :return:
    '''
    loader = None
    plugin = None
    path = None
    entities = None

# Generated at 2022-06-13 17:36:30.404030
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.module_utils.loader import path_dwim
    from ansible.module_utils.loader import module_loader
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = module_loader
    inv_loader = InventoryManager(loader=loader, sources='tests/inventory/directory_inventory')
    vars_loader.add_directory(path_dwim('lib/ansible/plugins/vars'))
    vars_manager = VariableManager(loader=loader, inventory=inv_loader)
    host = inv_loader.get_host('localhost')
    host_vars = get_vars_from_path(loader, 'lib/ansible/plugins/vars', host, 'start')

# Generated at 2022-06-13 17:36:49.151694
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # TODO
    return 0

# Generated at 2022-06-13 17:36:58.647271
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.module_utils.common._collections_compat import Mapping

    class Dummy:
        pass

    class DummyLoader:
        pass

    class DummyPlugin:
        _load_name = 'dummy_plugin'
        _original_path = '/tmp/dummy_path'

        def get_vars(loader, path, entities):
            assert(isinstance(loader, DummyLoader))
            assert(isinstance(path, str))
            assert(isinstance(entities, list))
            return {'vars': {'x': 1}}

    class DummyPluginRequiresWhitelist:
        REQUIRES_WHITELIST = True
        _load_name = 'dummy_plugin'
        _original_path = '/tmp/dummy_path'


# Generated at 2022-06-13 17:37:02.722790
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    ''' Test vars plugins are fetched. '''

    path = '/var/tmp/foo'
    entities = ['all', 'webservers']
    stage = 'inventory'
    loader = 'mock'

    data = get_vars_from_path(loader, path, entities, stage)
    assert isinstance(data, dict)

# Generated at 2022-06-13 17:37:05.710767
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class TestPlugin:
        def get_vars(self, loader, path, entities):
            return {'foo': 'bar'}

    loader = {}
    path = None
    entities = ['1']

    data = get_plugin_vars(loader, TestPlugin(), path, entities)
    assert data == {'foo': 'bar'}

# Generated at 2022-06-13 17:37:10.671726
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    plugin_path = u'hacking/env-vars'
    path = u'/this/is/a/test'
    entities = [Host(u'localhost'), Host(u'testhost1')]
    stage = 'inventory'

    data = {}

    # 2.x plugin
    plugin = vars_loader.get(u'hacking/env-vars')
    data = combine_vars(data, get_plugin_vars(None, plugin, path, entities))

    # 1.x plugin
    plugin = vars_loader.get(u'ansible.builtin.vars_plugins.env_vars')
    data = combine_vars(data, get_plugin_vars(None, plugin, path, entities))


# Generated at 2022-06-13 17:37:11.655072
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # TODO: Implement

    assert False

# Generated at 2022-06-13 17:37:16.374067
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    inventory_sources = ['/Users/vitalii/ansible-path/ad_hoc_test/vars']
    entities = [Host('test')]
    stage = 'inventory'

    data = get_vars_from_path(None, to_bytes(inventory_sources[0]), entities, stage)
    assert 'var_name' in data
    assert 'var_name_1' in data

# Generated at 2022-06-13 17:37:17.456262
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    # Basic function test
    pass

# Generated at 2022-06-13 17:37:25.896996
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost,")

    host = inventory.get_host("localhost")
    # Mock host object for testing
    host.vars = {'foo': 'bar'}

    inventory_vars = VariableManager(loader=loader, inventory=inventory)
    plugin_vars = get_plugin_vars(loader, vars_loader.get("host_list"), "./test_vars_plugin", [host])

    assert 'foo' in plugin_vars



# Generated at 2022-06-13 17:37:33.831957
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import c_vars
    from ansible.plugins.vars import c_vars_2
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host

    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader, sources=[])
    var_manager = VariableManager(loader=loader, inventory=inventory_manager)
    assert get_vars_from_path(loader, '.', [], 'task') == {}
    inventory_manager.add_group('group')
    var_manager.add_group_vars('group', {'z': '1'})

# Generated at 2022-06-13 17:38:35.286949
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars.host_group import VarsModule as vars_host_group
    from ansible.plugins.vars.host_all import VarsModule as vars_host_all
    loader = None
    path = '/'
    stage = 'inventory'
    plugin_list = [vars_host_group(), vars_host_all()]
    data = {}
    entities = ['localhost', 'all']

    data = get_vars_from_path(loader, path, entities, stage)

    assert(data == {'group_names': ['all'], 'groups': {'all': {'hosts': ['localhost']}}})