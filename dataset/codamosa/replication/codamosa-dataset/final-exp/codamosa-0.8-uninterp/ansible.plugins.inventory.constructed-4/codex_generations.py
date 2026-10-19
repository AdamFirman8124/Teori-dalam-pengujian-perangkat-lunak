

# Generated at 2022-06-13 12:44:23.871293
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    pass

# Generated at 2022-06-13 12:44:34.041642
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    import os
    import unittest
    import ansible.plugins.inventory as inv

    class TestInventoryModule(unittest.TestCase):
        def setUp(self):
            self.loader = None
            self.sources = None
            self.host = None
            self.im = inv.get_inventory_plugin(["constructed"])

        def test_host_vars(self):
            import ansible.inventory.host as host

            # setup variables required to call host_vars from InventoryModule
            self.loader = None
            self.sources = None
            self.host = host.Host("test_host")
            self.host.set_variable('test_var', 'test_value')
            results = self.im.host_vars(self.host, self.loader, self.sources)

            self

# Generated at 2022-06-13 12:44:46.294781
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from collections import namedtuple
    from ansible.vars.manager import VariableManager

    # preparation
    loader = namedtuple('loader', ('get_basedir'))(lambda: '/some/path')
    source = namedtuple('source', ('name'))('some source')
    sources = [source]
    variables = VariableManager()
    inventory = namedtuple('inventory', ('loader', 'sources', '_vars_plugins_cache', '_vars_per_host'))
    inventory.loader = loader
    inventory.sources = sources
    inventory._vars_plugins_cache = {}
    inventory._vars_per_host = {'some_host': {'my_var': 'my_value'}}
    im = InventoryModule()

    # run & check

# Generated at 2022-06-13 12:44:50.485080
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_path = 'inventory.config'
    path = os.path.join(os.path.dirname(__file__), inventory_path)
    inventory = InventoryModule()
    inventory.verify_file(path)
    assert inventory.verify_file(path) == True

# Generated at 2022-06-13 12:44:57.952561
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class DummyInventoryPlugin(BaseInventoryPlugin):
        NAME = 'test'
        def get_host_vars(self, host):
            base_vars = {'x': 2, 'y': 5}
            return combine_vars(base_vars, self.get_option('my_var'))
    loader = DataLoader()
    host = Host(name='host')
    group = Group(name='group')
    group.add_host(host)
    group.set_variable('group_var', 1)

# Generated at 2022-06-13 12:44:59.674186
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = MockInventory
    loader = MockLoader
    path = "test_InventoryModule_parse"

    # Call parse method
    assert(InventoryModule.parse(inventory, loader, path, cache=False))

# Generated at 2022-06-13 12:45:10.496690
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    # Test method host_groupvars of Class InventoryModule
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import inventory_loader, vars_loader

    options = {'plugin': 'constructed', 'use_vars_plugins': True}
    inventory = InventoryManager(loader=DataLoader(), sources=['test'])
    host = Host(name='test')
    inventory.add_host(host)
    group = inventory.add_group('test_group')
    group.add_host(host)


# Generated at 2022-06-13 12:45:20.885281
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    import os
    import tempfile


# Generated at 2022-06-13 12:45:22.840593
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # TODO: Add tests for this method when used from CLI
    pass

# Generated at 2022-06-13 12:45:32.865954
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Making a mock class to fake InventoryModule
    class MockInventoryModule(InventoryModule):

        def __init__(self):
            self.groups = []
            self.compose = []
            self.keyed_groups = []

        # Mock object for this method
        def _add_host_to_keyed_groups(self, keyed_groups, hostvars, host, strict=True, fetch_hostvars=True):
            self.keyed_groups.append(getattr(host, keyed_groups['prefix']))

    # Making a mock class to fake InventoryPlugin
    class MockInventoryPlugin2(BaseInventoryPlugin):
        def __init__(self):
            self.hosts = []
            self.groups = []
            self.sources = []

        # Mock object for this method

# Generated at 2022-06-13 12:45:47.356659
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inv = InventoryModule()
    loader = DataLoader()
    host = Host(name='foobar', port=22)
    host.set_variable('group_names', ['alpha','foo','bar','baz'])
    inventory = VariableManager(loader, host_list=[])
    variables = inv.host_groupvars(host, loader, [])

# Generated at 2022-06-13 12:45:56.675631
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    # create a host object for testing, vars are a dictionary of variables
    host = MockHost(vars = {
        'var1': '1',
        'var2': '2'
    })

    # create a new instance of InventoryModule
    inv = InventoryModule()

    # invoke host_vars function with host as its parameter
    hvars = inv.host_vars(host, None, None)

    # assert that the host_vars function returns the expected variables
    assert hvars['var1'] == '1'
    assert hvars['var2'] == '2'


# Generated at 2022-06-13 12:46:03.709643
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():

    from ansible.plugins.loader import InventoryPluginLoader
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    host = Host('test')
    host.vars = dict(a=1, b=2)
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])

    module = InventoryModule()

    # simulate valid inventory
    module.parse(inventory, loader, '/tmp/test.yml', cache=False)

    # verify that host variables are returned
    vars = module.host_vars(host, loader, [])
    assert isinstance(vars, dict)

# Generated at 2022-06-13 12:46:12.039400
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    inventory = Inventory(VariableManager(), loader=DataLoader(), host_list=['127.0.0.1:2222'])

# Generated at 2022-06-13 12:46:13.535562
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''Unit test for method parse of class InventoryModule'''

    # TODO: Not yet implemented.
    pass

# Generated at 2022-06-13 12:46:20.051717
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import inventory_loader

    loader = DataLoader()
    v = VariableManager()
    e = InventoryManager(loader=loader, sources=["temp/hosts-test"])
    e.add_host(Host("example.org", "testhost"))
    host = e.get_host("testhost")
    hostvars = {"foo": "bar", "baz": "qux"}
    host.set_variable_manager(v)
    host.add_group("all")
    host.add_group("foogroup")
    host.add_group("bar")
    host

# Generated at 2022-06-13 12:46:25.567259
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory._read_config_data = lambda x: None
    inventory.parse = lambda x, loader, path, cache: None
    setattr(inventory, 'hostvars', None)
    assert inventory.parse(None, None, None) is None

# Generated at 2022-06-13 12:46:32.836537
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    inventory = InventoryModule()
    inventory.options = dict(use_vars_plugins=True, strict=False)
    sources = [[{'inventory_path': './test/inventory/host_vars'}]]
    hostvars = inventory.host_groupvars(inventory.hosts.get('host1'), None, sources)
    assert(hostvars['host_group_var'] == 'host1')
    assert(hostvars['group_var'] == 'group1')
    assert(hostvars['all_group_var'] == 'group1')
    assert(hostvars['ungrouped_var'] == 'ungrouped')
    assert(hostvars['other_var'] is None)


# Generated at 2022-06-13 12:46:33.380977
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert True

# Generated at 2022-06-13 12:46:44.380170
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import os
    import sys
    import inspect

    from ansible.errors import AnsibleOptionsError
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import inventory_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath

    sys.modules['ansible.parsing.yaml.loader'] = DictDataLoader
    # Disable unfrackpath for this unit test harness, as we don't need it, and it
    # will break when attempting to load a VCR.yaml file
    sys.modules['ansible.module_utils.connection'] = DataLoader()


# Generated at 2022-06-13 12:46:59.634725
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import inventory_loader

    def get_inventory_manager(path):
        loader = DataLoader()
        inventory = InventoryManager(loader=loader, sources=path)
        return inventory

    inventory_dir = os.path.dirname(os.path.abspath(__file__))
    inventory_manager = get_inventory_manager(path=os.path.join(inventory_dir, "inventory_1"))
    variable_manager = VariableManager(loader=inventory_manager.loader, inventory=inventory_manager)
    inventory = InventoryModule()
    inventory._set

# Generated at 2022-06-13 12:47:02.208613
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    assert module.parse({}, {}, {}) == None

# Generated at 2022-06-13 12:47:10.197318
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Test for correct file extension
    assert(InventoryModule().verify_file('file.config'))
    assert(InventoryModule().verify_file('file.yaml'))
    assert(InventoryModule().verify_file('file.yml'))
    # Test for incorrect file extension
    assert(not InventoryModule().verify_file('file.txt'))

# Generated at 2022-06-13 12:47:20.993007
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    import unittest
    import ansible.plugins.loader as plugin_loader
    test_host_vars = None
    class TestInventoryModuleHostVars(InventoryModule):
        def host_vars(self, host, loader, sources):
            return super(TestInventoryModuleHostVars, self).host_vars(host, loader, sources)
    class TestInventoryHost:
        def __init__(self, name):
            self.name = name
            self.vars = {'var1': 'value1', 'var2': 'value2'}
        def get_name(self):
            return self.name
        def get_vars(self):
            return self.vars
        def get_groups(self):
            return []

# Generated at 2022-06-13 12:47:29.780096
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import pytest
    from ansible.inventory.manager import InventoryManager

    template_dir = 'tests/unit/resources/constructed/inventory_template'
    inventory_dir = 'tests/unit/resources/constructed/inventory_dir/hosts'
    inventory_path = 'tests/unit/resources/constructed/inventory_dir'
    inventory_data = """
    plugin: constructed
    # strict: False
    compose:
        var_sum: var1 + var2
    groups:
        webservers: inventory_hostname.startswith('web')
    keyed_groups:
        - prefix: distro
          key: ansible_distribution
    """

# Generated at 2022-06-13 12:47:32.502277
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()
    assert inventory.verify_file('inventory.config') == True
    assert inventory.verify_file('inventory.yaml') == False
    assert inventory.verify_file('inventory') == False

# Generated at 2022-06-13 12:47:43.095171
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.inventory.host import Host

    p = InventoryModule()

    loader = FakeVarsPluginLoader()
    # group_vars/all exists
    loader.extra_vars = {
        'group_vars_all': { 'a': 'b' },
        # group_vars/group exists
        'group_vars_group': { 'c': 'd' },
        # host_vars/exists
        'host_vars_exists': { 'e': 'f' },
    }

    host = Host('exists')
    host.add_group('group')
    assert loader.extra_vars['group_vars_all'] == p.host_groupvars(host, loader, None)

    loader = FakeVarsPluginLoader()
    # group_vars/all exists
    loader

# Generated at 2022-06-13 12:47:53.678220
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Test to verify inventory plugin constructed.
    """
    module = InventoryModule()
    class_inventory = '''
    plugin: constructed
    strict: False
    compose:
        var_sum: var1 + var2
        server_type: "ansible_hostname | regex_replace ('(.{6})(.{2}).*', '\\2')"
    groups:
        webservers: inventory_hostname.startswith('web')
        development: "'devel' in (ec2_tags|list)"
        private_only: not (public_dns_name is defined or ip_address is defined)
        multi_group: (group_names | intersect(['alpha', 'beta', 'omega'])) | length >= 2
    keyed_groups:
    '''
    inventory = class_inventory
    loader

# Generated at 2022-06-13 12:48:03.241664
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()

    valid_files = (
        'inventory.config',
        'inventory.yml',
        'inventory.yaml',
        'inventory.json',
        'inventory.toml'
    )

    for path in valid_files:
        assert module.verify_file(path) is True

    invalid_files = (
        '.config',
        '.yml',
        'inventory.txt',
        'inventory.yaml.txt',
    )

    for path in invalid_files:
        assert module.verify_file(path) is False



# Generated at 2022-06-13 12:48:05.331111
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    module = InventoryModule()
    assert module.host_groupvars('host', 'loader', 'sources') == None


# Generated at 2022-06-13 12:48:24.428255
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.host import Host
    from ansible.plugins.loader import InventoryLoader
    from ansible.vars.manager import VariableManager

    inventory_module = InventoryModule()

    # Create a Host and a VariableManager. Also, add a host variable to the Host
    host = Host(name='example.com')
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'foo': 'bar'}
    host.set_variable_manager(variable_manager)

    # Execute host_vars() and do an assertion.
    # Since we have not added any inventory sources, the returned variable
    # should only contain the variable 'foo'
    assert inventory_module.host_vars(host, InventoryLoader(), []) == {'foo': 'bar'}

# Generated at 2022-06-13 12:48:32.792655
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.inventory import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["hosts"])
    inventory.add_group("all")
    host = Host(name="foo", groups=["all"])
    inventory.add_host(host, "all")
    inventory.add_group("group")
    inventory.add_host(host, "group")
    inventory.add_group("one")
    inventory.add_host(host, "one")
    inventory.add_group("two")
    inventory.add_host(host, "two")
    inventory.add_group("three")

# Generated at 2022-06-13 12:48:44.440403
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from collections import namedtuple
    from ansible import constants as C
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import find_plugin_filepaths
    config = """
    plugin: constructed
    strict: False
    compose:
        var_sum: var1 + var2
    groups:
        webservers: inventory_hostname.startswith('web')
    keyed_groups:
        - prefix: distro
          key: ansible_distribution
        - key: placement.availability_zone
          parent_group: all_ec2_zones
    """
    loader = Ans

# Generated at 2022-06-13 12:48:45.823055
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: validate method parse of class InventoryModule
    pass


# Generated at 2022-06-13 12:48:54.496205
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = [
        {
            "hosts": ['host1', 'host2', 'host3'],
            # '_meta' isn't required for hostvars, but the inventory expects it to be present and populated
            "_meta": {'hostvars': ['host1', 'host2', 'host3']}
        }
    ]
    # create an instance of InventoryModule clas
    constructed = InventoryModule()

    # create an instance of AnsibleInventory class and assign inventory to it
    ansible_inventory = AnsibleInventoryClass()
    ansible_inventory.groups = inventory

    # create an instance of AnsibleInventory class and assign _meta to it
    ansible_inventory._meta = AnsibleInventoryClass()

    # create an instance of AnsibleInventory class and assign hostvars to it
    ansible_inventory._meta

# Generated at 2022-06-13 12:49:01.936502
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import os
    import sys
    import collections

    current_dir = os.path.realpath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
    sys.path.append(parent_dir)

    from ansible.plugins.inventory.constructed import InventoryModule

    if not os.path.split(__file__)[0]:  # if __file__ has no parent
        current_dir = os.path.realpath(os.getcwd())

    # for the following tests we use the 'inventory.config'
    # file located in the same directory as this test file
    test_files = ['inventory.config']


    ###########################################################################
    # Tests for the method parse of class InventoryModule
    #

# Generated at 2022-06-13 12:49:11.727179
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host = Host(name='server1')
    group = inventory.add_group('group1')
    group.vars = {'group1var1': 'group1var1value'}
    group.hosts = [host]
    host.groups = [group]
    im = InventoryModule()
    im.set_options({'use_vars_plugins': False})

# Generated at 2022-06-13 12:49:24.544315
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    inventory = {'testhost_1': {'vars': {'testvar': 'testval'}},
                 'testhost_2': {'vars': {'testvar': 'testval', 'testvar2': 'testval2'}}}

    loader = dict()
    sources = dict()

    inventory_module = InventoryModule()
    # with host object
    host_obj = BaseInventoryPlugin()
    host_obj.name = 'testhost_1'
    host_obj.vars = inventory['testhost_1']
    host_vars = inventory_module.host_vars(host_obj, loader, sources)
    assert host_vars == {'testvar': 'testval'}

    # with name
    host_vars = inventory_module.host_vars('testhost_2', loader, sources)

# Generated at 2022-06-13 12:49:39.269134
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()

    # Test 1: verify_file is called without any extension
    path = '../sample_inv/inventory.config'
    result = module.verify_file(path)
    assert result == True, "Result should be: True"

    # Test 2: verify_file is called with a '.config' extension
    path = '../sample_inv/inventory.config.config'
    result = module.verify_file(path)
    assert result == True, "Result should be: True"

    # Test 3: verify_file is called with a '.txt' extension
    path = '../sample_inv/inventory.config.txt'
    result = module.verify_file(path)
    assert result == False, "Result should be: False"

    # Test 4: verify_file is called with a non-existent file


# Generated at 2022-06-13 12:49:45.839434
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    def _get_base_inventory():
        loader = DataLoader()
        host = Host(name='test.example.com')
        host.vars["a"] = "A"
        inventory = InventoryManager(loader)
        inventory.add_host(host)
        return inventory, loader

    inventory, loader = _get_base_inventory()
    inventory._options['use_vars_plugins'] = False

    plugin = InventoryModule()
    plugin.parse(inventory, loader, 'unit test', cache=True)
    expected = {'a': 'A'}
    actual = plugin.host_vars(host, loader, None)

    assert(expected == actual)


# Generated at 2022-06-13 12:50:18.238968
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from tests.unit.plugins.inventory.test_dynamic_inventory import TestDynamicInventory

    group = TestDynamicInventory.impl_group()
    group.vars = {'group_var_h': 'group_var_val_h'}

    host = TestDynamicInventory.impl_host()
    host.name = 'test_host_name'
    host.vars = {'host_var_h': 'host_var_val_h'}
    host.groups = [group]

    inventory = TestDynamicInventory.impl_inventory(hosts=[host], groups=[group])
    loader = DataLoader()
    constructed_plugin = InventoryModule()

# Generated at 2022-06-13 12:50:28.330405
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    i = inventory_loader.get('constructed', loader=loader, path='./test_1.config', cache=True)
    i.parse_inventory(loader)

    assert(i.hosts['host_44444444444444444444444444444444444444444444444444444444444444444444444444444444'].vars['var_sum'] == '444')

# Generated at 2022-06-13 12:50:37.674256
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Integrated unit test for InventoryModule.parse method.
    Tests multiple features of this plugin in combination.
    """
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import inventory_loader

    # First setup a working directory and fill it with a sample inventory, config and test files
    workingdir_path = '/tmp/ansible_constructed_test'
    os.system('rm -rf %s' % workingdir_path)
    os.makedirs(workingdir_path)
    # Test inventory with 2 hosts (having 2 groups each)
    test_inventory_path = os.path.join(workingdir_path, "inventory.ini")
    test_inventory_file = open(test_inventory_path, 'w')

# Generated at 2022-06-13 12:50:41.601012
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    plugin = InventoryModule()
    vars = plugin.host_groupvars(inv.hosts['localhost'], loader, [])
    assert 'group_name' in vars
    assert vars['group_name'] == 'all'

# Generated at 2022-06-13 12:50:42.375019
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 12:50:50.516366
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    from ansible.inventory import Inventory, Group

    host = Inventory()
    host.add_group(Group('all'))
    host.add_group(Group('ungrouped'))
    host.add_host(host='host1', groups=['group1', 'group2'])

    host_obj = host.hosts['host1']

    inv_host = InventoryModule()
    host_groupvars = inv_host.host_groupvars(host_obj, None, None)
    assert host_groupvars == {'group_names': ['all', 'group1', 'group2', 'ungrouped'], 'groups': ['all', 'group1', 'group2', 'ungrouped']}


# Generated at 2022-06-13 12:51:02.915586
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    # Set up mock inventory plugin class
    import ansible.plugins.loader as plugin_loader

    class Host(object):
        def __init__(self, hostvars):
            self.vars = hostvars

    # Set up test input data
    data = {
        'hostvars': {'foo': 'foo-value'},
        'sources': [{'foo': 'bar'}]
    }

    # Set up test expectations
    result = {'foo': 'foo-value'}

    # Call the tested method
    method = InventoryModule()
    res = method.host_vars(Host(data['hostvars']), plugin_loader, data['sources'])

    assert result == res

# Generated at 2022-06-13 12:51:04.223214
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 12:51:10.749144
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    inventory = PluginLoader('/plugin_dir', 'hosts', 'inventory', 'script').inventory_sources_for("/no/file/here")
    if not inventory:
        raise Exception("Failed to find inventory source plugins")
    sources = inventory[0]
    loader = PluginLoader("/not/a/real/path", "lookup", 'lookup_plugins', 'lookup')
    loader.set_cwd("/no/file/here")
    gvars = InventoryModule().host_groupvars(sources[0].get_host("group1-1"), loader, sources)
    print(gvars)

# Generated at 2022-06-13 12:51:20.296604
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.plugins.loader import inventory_loader
    import os

    # Negative test
    # test that non-existent file returns False
    plugin = inventory_loader.get("constructed")
    path = 'non-existent-inventory-file.txt'
    assert not plugin.verify_file(path)

    # Positive test
    # test that valid constructed inventory source file returns True
    path = './inventory.config'
    assert plugin.verify_file(path)

    # Positive test
    # test that valid YAML file returns True
    path = 'test_inventory.yaml'
    assert plugin.verify_file(path)
    os.remove(path)

# Generated at 2022-06-13 12:51:56.644191
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.color import stringc
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import ansible.plugins.loader

    plugins = ansible.plugins.loader.all(class_only=True)
    plugins.pop('InventoryModule')  # to exclude inventory plugins
    ansible_plugins_list = ansible.plugins.loader.find_plugins()


# Generated at 2022-06-13 12:52:10.043006
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    # test host_vars method of class InventoryModule
    import sys
    import ansible.utils.vars
    from ansible.inventory.host import Host
    from ansible.vars import SafeDict
    from ansible.module_utils._text import to_text
    from ansible.utils.display import Display
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    display = Display()
    source_path = ["./tests/inventory_sources/host_vars" ]
    hostvars = dict()
    hostvars["ansible_hostname"] = "host1"
    hostvars["ansible_connection"] = "ssh"
    hostvars["ansible_ssh_host"] = "host1"
    hostvars["ansible_ssh_port"] = 22
    hostvars

# Generated at 2022-06-13 12:52:19.107515
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.plugins.loader import inventory_loader
    inventory = inventory_loader._get_inventory_plugins(C.DEFAULT_HOST_LIST)[0].inventory
    plugins = inventory._inventory.__class__.__bases__[0]._plugins

    class MockLoader(object):
        def load_from_file(*args):
            return {'host': {'var': 'val'}}

        def get_basedir(*args):
            return '.'

    loader = MockLoader()
    inventory.build_inventory(loader=loader)

    host = inventory.hosts['host']
    hostvars = plugins.host_vars(host, loader)
    assert hostvars['var'] == 'val'

# Generated at 2022-06-13 12:52:20.236636
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert True


# Generated at 2022-06-13 12:52:30.901877
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''Unit test for `parse` method of class InventoryModule'''
    # import only the class you are testing
    InventoryModule = __import__('lib.ansible.plugins.inventory.constructed').InventoryModule

    # instantiate a class to be tested
    inventory_module = InventoryModule()

    # instantiate arguments for a method to be tested
    import os
    import lib.ansible.plugins.inventory.source_config as source_config
    import lib.ansible.plugins.inventory.manager as manager
    import lib.ansible.plugins.loader as loader

    # create inventory object
    inventory = manager.InventoryManager(loader, sources=[])

    # create loader object
    loader = loader.PluginLoader()

    # get path to the localhost file

# Generated at 2022-06-13 12:52:34.456134
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # create mock data/object
    inventory = None
    loader = None
    path = None
    # call the method
    result = InventoryModule().verify_file(path)

    assert result is not None

# Generated at 2022-06-13 12:52:41.077791
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    from ansible import context
    import os

    instance = InventoryModule()

    inventory_filename = 'inventory.config'
    inventory_path = os.path.join(context.ANSIBLE_TEST_DATA_ROOT, inventory_filename)
    with open(inventory_path, 'w'):
        pass

    assert instance.verify_file(inventory_path)

    os.remove(inventory_path)
    assert not instance.verify_file(inventory_path)

# Generated at 2022-06-13 12:52:49.643859
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader)
    vars_manager = VariableManager()
    inv = inv_manager.parse_sources(['localhost,'], None, cache=False)
    assert inv is not None

    print("Example of use of constructed plugin. Example from docs with demo of hostvars")
    constructed_plugin = InventoryModule()
    constructed_plugin.parse(inventory=inv, loader=loader, path='constructed_example.yaml', cache=False)
    assert constructed_plugin is not None

    hostvars = vars_manager.get_host_variables(host=inv.hosts['localhost'])


# Generated at 2022-06-13 12:52:54.596509
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    with pytest.raises(AnsibleOptionsError):
        InventoryModule.parse(ansible.inventory.hosts.Group(), ansible.parsing.dataloader.DataLoader(), '/path/to/file', cache=False)

# Generated at 2022-06-13 12:52:55.972202
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass


# Generated at 2022-06-13 12:54:01.955207
# Unit test for method host_vars of class InventoryModule
def test_InventoryModule_host_vars():
    from ansible.inventory.host import Host
    host = Host("hostname")
    loader = ""
    sources = []
    inm = InventoryModule()
    inm.parse(host, loader, sources, cache=False)

    assert host.get_vars() == inm.host_vars(host, loader, sources)

# Generated at 2022-06-13 12:54:12.717280
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():
    import json

    loader = None

    # create fake inventory with a host that has 3 groups
    inv = {'_meta': {'hostvars': {'alpha': {'a': 1},
                                  'beta': {'b': 2}}},
           'all': {'hosts': ['alpha', 'beta']},
           'alpha': {'hosts': ['alpha']},
           'beta': {'hosts': ['beta']},
           'omega': {'hosts': []}}
    inventory = json.dumps(inv)

    # create fake loader with contents of ansible.cfg, vars plugin directories, and custom vars plugin directory
    # - ansible.cfg [vars_plugins] directory
    # - ansible/plugins/vars directory
    # - vars plugin directory

# Generated at 2022-06-13 12:54:20.188157
# Unit test for method host_groupvars of class InventoryModule
def test_InventoryModule_host_groupvars():

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    my_inventory = InventoryManager(loader=None, sources="foobar")

    constructed = InventoryModule()
    constructed.parse(my_inventory, loader, "foobar", cache=None)

    hostvars = constructed.host_groupvars(None, loader, None)
    assert hostvars == {}

