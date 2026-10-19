

# Generated at 2022-06-22 12:14:24.753722
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import HostVars
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader, sources='localhost,')
    play_context = PlayContext()

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    vars = hostvars.raw_get('localhost')

    assert type(vars) is dict
    assert 'inventory_dir' in vars
    assert vars['inventory_dir'] == '/etc/ansible'

# Generated at 2022-06-22 12:14:27.737637
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    variables = {"foo": "bar"}
    hostvarsvars = HostVarsVars(variables, None)
    assert list(hostvarsvars) == list(variables)

# Generated at 2022-06-22 12:14:36.751071
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create inventory
    inventory = InventoryManager()

    # Create variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}

    # Create instance of HostVars
    host_vars_instance = HostVars(inventory=inventory,
                                  variable_manager=variable_manager,
                                  loader=None)

    # Create host1
    inventory.add_host('host1')

    # Create host2
    inventory.add_host('host2')

    # Check __iter__ returns correct values
    assert list(host_vars_instance.__iter__()) == ['host1', 'host2']



# Generated at 2022-06-22 12:14:48.701759
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({'inventory': 'localhost ansible_connection=local'})

    inventory = InventoryManager(loader=loader, sources=['dynamic_inventory.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # assert hostvars.raw_get('localhost') is not None
    assert hostvars.raw_get('localhost')['ansible_connection'] == 'local'

    data = hostvars.raw_get('localhost')
    assert type(data) == dict
    assert 'ansible_connection' in data

    data = hostvars.raw_get('localhost')
    assert type(data) == dict
    assert 'ansible_connection' in data

# Generated at 2022-06-22 12:14:59.490131
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.errors import AnsibleError

    # Initialize scenario
    loader = DataLoader()
    inventories = InventoryManager(loader=loader,
                                   sources="tests/unit/playbooks/inventory_with_hostvars.ini")
    variable_manager = VariableManager(loader=loader,
                                      inventory=inventories,
                                      use_task_vars=True,
                                      group_vars_as_files=True)

# Generated at 2022-06-22 12:15:10.618155
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import copy
    import json

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    vars_cache = json.load(open('../tests/vars_cache_test.json'))
    # Make sure that the vars_cache contains an immutable object to provide
    # conditions for the method __getitem__ of class HostVars to produce
    # an error when an attempt to deepcopy is made.
    vars_cache['foo'] = {'bar': 'baz'}

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 12:15:24.025896
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    # Dummy class for testing VariableManager
    class DummyVariableManager:
        def __init__(self, hostvars):
            self._hostvars = hostvars
            self._hosts = {}

        def get_vars(self, host=None, include_hostvars=True):
            get_vars_host = host.get_name()
            if include_hostvars and get_vars_host in self._hostvars:
                return self._hostvars[get_vars_host]
            else:
                return {}

        def clear_vars(self):
            self._hostvars = {}

    # Dummy class for testing Host
    class DummyHost:
        def __init__(self, hostname):
            self._name = hostname
        def get_name(self):
            return

# Generated at 2022-06-22 12:15:35.239080
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    class HostVarsVarsMock(HostVarsVars):
        def __init__(self, variables, loader):
            super(HostVarsVarsMock, self).__init__(variables, loader)

    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval, STRING_TYPES


# Generated at 2022-06-22 12:15:44.895495
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    class FakeInventory(object):
        def __init__(self, host_names):
            self._host_names = host_names

        def __iter__(self):
            for host in self._host_names:
                yield host

    class FakeVariableManager(object):
        def __init__(self, host, variables):
            self._host = host
            self._variables = variables

        def get_vars(self, host=None, include_hostvars=True):
            if host == self._host and include_hostvars:
                return self._variables
            return {}

    class FakeLoader(object):
        pass

    host_name = 'fake_host'
    variable = 'fake_var'
    variable_value = 'fake_value'
    host_variables = { variable: variable_value }
   

# Generated at 2022-06-22 12:15:51.699883
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory_manager = InventoryManager(loader=DataLoader(), sources="localhost")
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory_manager)

    hostvars = HostVars(inventory_manager, variable_manager, loader=DataLoader())
    assert repr({'localhost': {}}) == repr(hostvars)

# Generated at 2022-06-22 12:16:05.115639
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    host = Host('localhost')

    variable_manager = VariableManager()
    variable_manager.set_host_variable(host, varname='test_key', value='test_value')
    hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=None)

    assert isinstance(hostvars, HostVars)
    assert isinstance(hostvars.raw_get('localhost'), Mapping)
    assert isinstance(hostvars['localhost'], HostVarsVars)

    assert hostvars['localhost']['test_key'] == 'test_value'

# Generated at 2022-06-22 12:16:12.209796
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    host_names = [
        'a01',
        'b01',
        'a01',
        'devel',
    ]
    inventory = InventoryManager(host_list=[host_names])
    hostvars = HostVars(inventory, VariableManager(), None)
    assert host_names == sorted(list(hostvars))

# Generated at 2022-06-22 12:16:21.508003
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)
    assert repr(hostvars) == '{}'
    assert repr(hostvars) == repr(inventory._hosts_cache)

    inventory.add_host(host='localhost')
    variable_manager.set_nonpersistent_facts(host=inventory.get_host('localhost'), facts={'foo': 'bar'})
    variable_manager.set_host_variable(host=inventory.get_host('localhost'), varname='foo', value='bar')
    assert repr(hostvars)

# Generated at 2022-06-22 12:16:32.726177
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''
    unit test for HostVars.__getitem__()
    '''
    import unittest
    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.parsing.dataloader
    import ansible.playbook.play

    class TestHostVars(unittest.TestCase):

        def setUp(self):
            self.loader = ansible.parsing.dataloader.DataLoader()
            hosts = [
                "server1",
                "server2",
            ]


# Generated at 2022-06-22 12:16:39.241836
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars.set_variable_manager(variable_manager)
    assert variable_manager._hostvars == hostvars

    hostvars.set_inventory(inventory)
    assert inventory._hostvars == hostvars


# Generated at 2022-06-22 12:16:50.136941
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import os

    # VariableManager
    variable_manager = VariableManager()

    # set the inventory
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=os.path.dirname(__file__) + '/inventory_file')

    # test variables
    host_vars = {
        'my_var': 'foo',
        'my_var_templated': "{{ my_var }}",
        'my_var_templated_2': "{{ my_var_templated }}",
    }

# Generated at 2022-06-22 12:17:01.968952
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.plugins.loader import action_loader
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    # set templar 'static_vars'
    HostVarsVars.static_vars = STATIC_VARS

    # prepare facts for templar
    facts = dict(
        ansible_distribution="Debian",
        ansible_distribution_major_version="9",
        ansible_distribution_version="9.10",
        ansible_machine="x86_64",
        ansible_os_family="Debian",
    )

    # prepare roles

# Generated at 2022-06-22 12:17:08.793907
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inventory = Inventory(host_list=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader=None)

    assert list(iter(hostvars)) == []

    inventory.add_host(host=None, group=None, port=None, variables=None)

    assert list(iter(hostvars)) == inventory.hosts



# Generated at 2022-06-22 12:17:17.755845
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Host, Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # Create inventories, loader and variable manager
    inventory = Inventory(loader=DataLoader())
    localhost = Host(name='localhost')
    inventory.add_host(localhost)

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    # Create host vars
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    # Create variable_manager vars and set variable 'foo' with value 'bar'
    variable_manager.set_nonpersistent_facts(localhost, {'foo': 'bar'})

# Generated at 2022-06-22 12:17:29.310431
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DictDataLoader({
        'host.yml': """
res:
  one: "{{ str1 }}"
  two: "{{ str2 }}"
  three: "{{ str3 }}"
""",
    })

    inventory = InventoryManager(loader=loader, sources=['host.yml'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=None))

# Generated at 2022-06-22 12:17:39.838115
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))

    hostvars = HostVars(inventory=inventory, variable_manager=VariableManager(loader=loader), loader=loader)
    host = inventory.get_host("localhost")
    hostvars.set_host_variable(host, "key", "value")

    assert hostvars["localhost"]["key"] == "value"


# Generated at 2022-06-22 12:17:50.770797
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)

    host_vars = HostVars(inventory, variable_manager, loader=None)

    # Raw variable expansion
    host_name = 'test_host'
    variable_manager.set_host_variable(inventory.get_host(host_name), 'test_var', 'test_value')
    data = host_vars.raw_get(host_name)

    assert data['test_var'] == 'test_value'
    assert 'ansible_host' not in data

    # Raw variable expansion with special keyword 'ansible_host'
    host_name = 'test_host_2'
   

# Generated at 2022-06-22 12:18:02.037565
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    """Test that HostVars.raw_get returns the right data

    """

    import unittest

    # Test class that implements only the minimal
    # interface required by HostVars
    class MockInventory(object):
        def get_host(self, host_name):
            if host_name in self._host_data:
                return MockHost(host_name)
            else:
                return None

    class MockHost(object):
        def __init__(self, name):
            self.name = name

    class MockVariableManager(object):
        def __init__(self, hostvars, loader):
            self._hostvars = hostvars
            self._loader = loader

# Generated at 2022-06-22 12:18:13.001095
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.manager import VariableManager

    class MockLoader:
        pass

    class MockInventory:
        pass

    variable_manager = VariableManager()
    variable_manager._loader = MockLoader()

    hostvars = HostVars(MockInventory(), variable_manager, MockLoader())

    # Check if serializing and deserializing the HostVars class works
    # and the attributes _loader and _hostvars of VariableManager get
    # assigned if None.
    assert variable_manager._loader is not None
    assert variable_manager._hostvars is not None
    hostvars.__setstate__(hostvars.__getstate__())
    assert variable_manager._loader is not None
    assert variable_manager._hostvars is not None

# Generated at 2022-06-22 12:18:23.971843
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    inv_data = "{\"all\": {\"hosts\": [\"127.0.0.1\"]}, \"_meta\": {\"hostvars\": {\"127.0.0.1\": {\"ansible_all_ipv4_addresses\": [\"1.1.1.1\"]}}}}"
    inv = InventoryManager(loader=loader, sources=inv_data)
    vars_mgr = VariableManager(loader=loader, inventory=inv)


# Generated at 2022-06-22 12:18:36.413906
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hv = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hv.set_host_variable('localhost', 'new_variable', 'value')
    assert hv.raw_get('localhost')['new_variable'] == 'value'

    variable_manager.set_host_variable('localhost', 'new_variable', 'value2')
    assert hv.raw_get('localhost')['new_variable'] == 'value2'

# Generated at 2022-06-22 12:18:40.838902
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create an inventory that contains at least two hosts
    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'
    hostvars = dict(
        host1=dict(var1=1, var2=2),
        host2=dict(var1=2, var2=1),
    )
    inventory = InventoryManager(loader=DataLoader())
    inventory.hosts = hostvars.keys()
    inventory.set_variable(host1, 'foo', 'bar')
    inventory.set_variable(host2, 'foo', 'baz')

# Generated at 2022-06-22 12:18:46.721836
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    '''
    Ensure the __iter__ method returns iterable of host names.
    '''
    # Setup a mock inventory object
    mock_inventory = type('Inventory', (object,), {
        'hosts': {
            'host1': type('Host1', (object,), {'name': 'host1'}),
            'host2': type('Host2', (object,), {'name': 'host2'}),
            'host3': type('Host3', (object,), {'name': 'host3'}),
        }
    })

    # Setup a mock variable manager object
    mock_variable_manager = type('VariableManager', (object,), {'_hostvars': None})

    # Setup a mock loader object

# Generated at 2022-06-22 12:18:54.315502
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from .inventory import Inventory
    from .inventory import Host
    from .inventory import Group
    from .vars_plugins.yaml import VarsModule as YamlVars
    from .vars_plugins.ini import VarsModule as IniVars

    inventory = Inventory(loader=None)
    # This is a default localhost, it will be created if needed in HostVars.raw_get
    host = Host('localhost')

    # Define variables in different ways
    host.vars = dict(Foo='bar')
    group = Group('group1')
    group.vars = dict(Foo='baz')
    inventory.set_variable(host, 'Host', 'h1')
    inventory.set_variable(group, 'Group', 'g1')
    host.set_variable('Var1', 'value1')

   

# Generated at 2022-06-22 12:19:03.899656
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    def deepcopy(obj):
        return obj

    inventory_manager = InventoryManager(loader=None, sources=u'')
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)

    host_vars = HostVars(inventory=inventory_manager, variable_manager=variable_manager, loader=None)
    host_vars.set_host_variable(host=inventory_manager.get_host('localhost'), varname='foo', value='bar')
    host_vars.set_host_variable(host=inventory_manager.get_host('localhost'), varname='baz', value='qux')

# Generated at 2022-06-22 12:19:24.633788
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-22 12:19:33.768570
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost,"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host_vars = HostVars(inventory, variable_manager, loader)

    data = host_vars.raw_get("localhost")

    assert 'inventory_hostname' in data
    assert data['inventory_hostname'] == "localhost"

# Generated at 2022-06-22 12:19:43.523613
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Add a host without variables
    inv = InventoryManager(loader=DataLoader())
    inv.add_host(host="example.org")

    hvars = HostVars(inventory=inv, variable_manager=None, loader=DataLoader())

    assert "example.org" in hvars
    assert hvars.raw_get("example.org") == dict()
    assert hvars.raw_get("example.org") != dict({"A": "B"})
    assert len(hvars) == 1

    # Add an extra host with variables
    inv.add_host(host="example.net")
    assert "example.net" in hvars

# Generated at 2022-06-22 12:19:55.362048
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager as DummyVars
    from ansible.vars import HostVars as DummyHostVars
    from ansible.template import Templar
    loader = "test_loader"

    dummy_inven = "test_inventory"
    dummy_vars_manager = DummyVars(loader=loader)

    test_host = Host("test_host")

    hostvars = DummyHostVars(dummy_inven, dummy_vars_manager, loader)

    templar = Templar(loader=loader)

    # Test when no host is specified
    result = hostvars._variable_manager.get_vars(host=None, include_hostvars=False)
    assert result == {}
    result = hostvars._variable_

# Generated at 2022-06-22 12:20:05.961153
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import ansible.vars.host_state
    import ansible.vars.vars_cache

    host = ansible.vars.host_state.Host('localhost', '127.0.0.1')
    vc = ansible.vars.vars_cache.VarsCache(loader=None)
    vc.set_host_variable(host, 'x', '1')
    vc.set_host_variable(host, 'y', '2')
    vc.set_host_variable(host, 'z', '{{y}}')
    hv = HostVars(vc, loader=None)

    assert hv.raw_get('localhost') == {'x': '1', 'y': '2', 'z': '{{y}}'}

# Generated at 2022-06-22 12:20:16.662737
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import os
    import tempfile
    import textwrap

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inv_path = tempfile.NamedTemporaryFile(mode='w+')
    inv_path.write(textwrap.dedent("""\
        [group1]
        host1
        host2
        """))
    inv_path.flush()

    inv_manager = InventoryManager(loader=None, sources=[inv_path.name])

    vm = VariableManager(loader=None, inventory=inv_manager)

    hv = HostVars(inventory=inv_manager, variable_manager=vm, loader=None)

    assert sorted(list(hv)) == ['host1', 'host2']



# Generated at 2022-06-22 12:20:24.984398
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    loader = DictDataLoader({
        "host_vars": {
            "hostone": {
                "foobar": "baz"
            }
        }
    })

    inventory = Inventory(loader=loader, variable_manager=VariableManager())

    variable_manager = VariableManager()
    variable_manager._loader = loader

    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars.raw_get("hostone") == {"foobar": "baz"}

    foo = hostvars.raw_get("hosttwo")
    assert foo.__class__.__name__ == 'AnsibleUndefined'

    assert hostvars.raw_get("localhost") == {}

# Generated at 2022-06-22 12:20:36.690525
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager

    loader = DummyLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = DummyVariableManager()

    # inventory.hosts list is empty, __getitem__ should return an
    # undefined value
    hostvars = HostVars(inventory, variable_manager, loader)
    assert repr(hostvars['localhost']) == 'AnsibleUndefined'

    # inventory.hosts list is not empty, __getitem__ should return
    # a HostVarsVars object
    inventory.hosts.append(inventory.get_host('localhost'))
    hostvars = HostVars(inventory, variable_manager, loader)
    assert repr(hostvars['localhost']) == "{'localhost': {'a': 'A'}}"



# Generated at 2022-06-22 12:20:45.474216
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.hostvars import HostVars
    import ansible.vars as vars
    import ansible.inventory as inventory
    import ansible.utils as utils

    # Prepare inventory, variables and loader
    inventory_name = "tests/inventory"
    inventory = inventory.Inventory(inventory_name)
    inventory.parse_inventory(inventory_name)
    inventory.set_variable('host1', 'var1', 'var1_value')
    inventory.set_variable('host2', 'var2', 'var2_value')

    variables = vars.VariableManager(inventory=inventory)
    loader = vars.DataLoader(path_filters=utils.path_dwim(inventory_name))
    hostvars = HostVars(inventory, variables, loader)

    # Validate the raw data got from

# Generated at 2022-06-22 12:20:58.215971
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host

    my_host_1 = Host(name='localhost', port=22)
    my_host_2 = Host(name='webserver', port=22)
    my_host_3 = Host(name='dbserver', port=22)
    my_host_4 = Host(name='testHost', port=22)
    my_host_5 = Host(name='testHost2', port=22)

    my_group = {"test_group": {"hosts": [my_host_1, my_host_2, my_host_3, my_host_4, my_host_5]}}
    my

# Generated at 2022-06-22 12:21:26.938718
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import copy
    import collections
    import sys
    import yaml
    from ansible import constants
    import ansible.constants
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    vars_list = [dict(a=1, b=2, c=3), dict(a=4, b=5, c=6)]

    # Unit tests for methods do __getitem__ and __setitem__ of class HostVars
    class HostVarsUnitTest(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()

# Generated at 2022-06-22 12:21:37.556922
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader.find_plugin(InventoryManager), sources='localhost,')
    variable_manager = VariableManager(loader=loader.find_plugin(VariableManager), inventory=inventory)
    play_context = PlayContext()
    hostvars = HostVars(inventory, variable_manager, loader)

    # Check expected return value if hostname present in inventory
    inventory.hosts.append('localhost')
    hostname = 'localhost'
    assert hostvars[hostname] == HostVarsVars(hostvars.raw_get(hostname), loader)

    # Check expected return value if hostname not present in inventory
   

# Generated at 2022-06-22 12:21:44.841848
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class Inventory:
        def __init__(self, hosts):
            self.hosts = hosts

    class Host:
        def __init__(self, name):
            self.name = name
            self.vars = {}

        def get_vars(self):
            return AnsibleVars(self.vars)

        def set_variable(self, key, value):
            self.vars[key] = value

    class AnsibleVars:
        def __init__(self, hosts):
            self.hosts = hosts

        def get(self, var):
            return self.hosts[var]

    class VariableManager:
        def __init__(self, hosts):
            self.hosts = hosts

        def get_vars(self, host, include_hostvars=False):
            return self.hosts

# Generated at 2022-06-22 12:21:51.596506
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    i = InventoryManager(loader=None, sources='localhost,')
    v = VariableManager(loader=None, inventory=i)
    h = HostVars(inventory=i, variable_manager=v, loader=None)

    assert repr(h) == "{'localhost': {}}"

# Generated at 2022-06-22 12:22:02.979694
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    module = AnsibleModule(
        argument_spec = dict(
            value = dict(type='list', default=list()),
            key = dict(type='str'),
        ),
    )

    class FakeInventory(object):

        def __init__(self, module):
            self.module = module

        def get_host(self, host_name):
            return host_name

        @property
        def hosts(self):
            return self.module.params['value']

    class FakeVariableManager(object):

        def __init__(self):
            self.loader = None
            self.hostvars = None

    inventory = FakeInventory(module)
    variable_manager = FakeVariableManager()
    hostvars = HostVars(inventory, variable_manager, inventory.module)
    assert hostvars.__iter__()

# Generated at 2022-06-22 12:22:14.903516
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    hostvars = HostVars(loader=loader, variable_manager=variable_manager)

    try:
        next(hostvars)
    except StopIteration:
        assert True

    variable_manager._hostvars = hostvars
    variable_manager.hostvars['localhost'] = {}
    variable_manager.hostvars['localhost']['property'] = 'value'
    hostvars.set_variable_manager(variable_manager)

    iterable = iter(hostvars)
    assert next(iterable) == 'localhost'
    try:
        next(iterable)
    except StopIteration:
        assert True

# Generated at 2022-06-22 12:22:26.133045
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()

    play_context = PlayContext()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    inventory.add_host(host='host1')
    inventory.add_host(host='host2')

    variable_manager.set_host_variable(inventory.get_host('host2'), 'foo', 'bar')

# Generated at 2022-06-22 12:22:29.858615
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.inventory.manager import InventoryManager

    hostvars = HostVars(inventory=InventoryManager(loader=None, sources=[], sources_list=[]),
                        variable_manager=None,
                        loader=None)

    assert hostvars.raw_get('localhost') == {}

# Generated at 2022-06-22 12:22:38.116572
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Test for empty Inventory
    inv_manager = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inv_manager)
    hostvars = HostVars(inv_manager, variable_manager, DataLoader())
    assert list(hostvars) == []

    # Test for non empty Inventory
    inv_manager = InventoryManager(loader=DataLoader(), sources='tests/hostvars_hosts')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inv_manager)
    hostvars = HostVars(inv_manager, variable_manager, DataLoader())
    assert list(hostvars)

# Generated at 2022-06-22 12:22:47.618109
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # create inventory
    inventory = Inventory(loader=None, sources=None)
    inventory.get_host("example.org")
    inventory.get_host("example.com")

    # create variable manager
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)
    assert len(hostvars) == 2
    assert "example.org" in hostvars
    assert "example.com" in hostvars
    assert "example.net" not in hostvars

    iter_hostvars = set()
    for host in hostvars:
        iter_hostvars.add(host)

    assert "example.org" in iter_hostvars
    assert "example.com" in iter_hostvars


# Generated at 2022-06-22 12:23:47.702170
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.hostvars import HostVars

    inventory = FakeInventory()
    variable_manager = FakeVariableManager(inventory)
    loader = FakeLoader()

    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars.raw_get('localhost').get('defined_var') == 'defined_in_vars_cache'
    assert hostvars.raw_get('localhost').get('undefined_var') is None
    assert hostvars.raw_get('localhost').get('defined_in_vars') == 'defined_in_vars'
    assert hostvars.raw_get('localhost').get('defined_in_hostvars') == 'defined_in_hostvars'



# Generated at 2022-06-22 12:23:55.874116
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import become_loader
    from ansible.module_utils.common._collections_compat import MutableMapping

    loader = DataLoader()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host = inventory.get_host('localhost')

    # Test case 1:
    # - non existing variable
    # - ordinary variable
    # - hostvars
   

# Generated at 2022-06-22 12:24:03.839999
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    assert len(hostvars) > 0
    hosts = list(hostvars)
    assert len(hosts) > 0
    assert 'localhost' in hosts