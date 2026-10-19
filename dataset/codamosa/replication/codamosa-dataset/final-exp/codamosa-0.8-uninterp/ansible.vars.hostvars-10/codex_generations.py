

# Generated at 2022-06-22 12:14:22.182871
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    class MockVars:
        def get(self, name, default=None):
            return "hello from %s" % name

    vars = MockVars()

    class MockLoader:
        def get_basedir(self, *args, **kwargs):
            return '/'

    loader = MockLoader()

    hvv = HostVarsVars(vars, loader)
    assert hvv['foo'] == "hello from foo"
    assert hvv['bar'] == "hello from bar"
    assert hvv['baz'] == "hello from baz"


# Generated at 2022-06-22 12:14:29.165612
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    loader = None
    variables = {
        'a': 1,
        'b': '{{ a }}',
        'c': 3,
    }
    hostvars_vars = HostVarsVars(variables, loader)
    assert len(hostvars_vars) == 3
    assert hostvars_vars['a'] == 1
    assert hostvars_vars['b'] == 1
    assert hostvars_vars['c'] == 3
    assert len(hostvars_vars) == 3


# Generated at 2022-06-22 12:14:31.457008
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars = HostVarsVars(dict(a='b'), None)
    assert list(iter(hostvars)) == list(iter(dict(a='b')))

# Generated at 2022-06-22 12:14:40.958272
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    test_loader = type('TestLoader', (object,), {})()

    mock_variable_manager = type('VariableManager', (object,), {
        '_hostvars': None,
        '_loader': None,
    })()

    test_hostvars = HostVars(
        variable_manager=mock_variable_manager,
        loader=test_loader,
        inventory=None,
    )

    assert test_hostvars._variable_manager._hostvars is None
    assert test_hostvars._variable_manager._loader is None

    test_hostvars.__setstate__({
        '_inventory': None,
        '_loader': test_loader,
        '_variable_manager': mock_variable_manager,
    })

    assert test_hostvars._variable_manager._hostvars is test

# Generated at 2022-06-22 12:14:53.057243
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    '''Checks whether method `__setstate__` of `HostVars` updates
    `_loader` and `_hostvars` attributes of a VariableManager instance
    when it is called.
    '''

    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    hostvars = HostVars(None, None, None)
    vm = hostvars._variable_manager = VariableManager()

    # Change the state of the hostvars to make checks
    state = {'_loader': 'loader', '_inventory': 'inventory'}
    hostvars.__setstate__(state)

    # Verify changes of the hostvars state
    assert hostvars._loader == 'loader'
    assert hostvars._inventory == 'inventory'

    # Verify changes of the

# Generated at 2022-06-22 12:15:02.733201
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # pylint: disable=import-error,unused-variable,no-name-in-module, too-few-public-methods
    from ansible.inventory import Inventory
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory()

    vm = VariableManager()
    vm.set_inventory(inventory)

    inventory.set_variable('foo', 'bar')
    vm.set_loader(loader)


    hv = HostVars(inventory, vm, loader)
    assert hv.raw_get('foo') == {'foo': wrap_var('bar')}

# Generated at 2022-06-22 12:15:14.060082
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    def Host(name):
        return type(name, (), dict(name=name))

    # test_hosts = [Host('host1'), Host('host2')]
    test_hosts = [host1, host2]  # TODO: fix this, so we will not use global variables
    test_mapping = dict(
        host1=dict(
            var1="value1",
            var2=dict(
                var3="value3"
            )
        ),
        host2=dict(
            var1="value1",
            var2=dict(
                var3="value3"
            )
        )
    )

    test_inventory = type('test_inventory', (object, ), dict(hosts=test_hosts))

# Generated at 2022-06-22 12:15:18.969090
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    var_mgr = dict(a=1, b=2)
    hostvars_vars = HostVarsVars(var_mgr, {})
    assert set(hostvars_vars) == set(var_mgr)


# Generated at 2022-06-22 12:15:25.644725
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    hosts = HostVars(inventory, variable_manager, loader)

    assert len(list(hosts)) == 1
    assert 'localhost' in list(hosts)

# Generated at 2022-06-22 12:15:36.014815
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_nonpersistent_facts('localhost', {'foo': 'bar'})
    hostvars.set_host_variable('localhost', 'baz', 'qux')
    hostvars.set_host_facts('localhost', {'fizz': 'buzz'})


# Generated at 2022-06-22 12:15:51.608796
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils._text import to_text
    from ansible.utils.vars import combine_vars

    loader = DataLoader()

    inv = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=[])

    host1 = inv.get_host(to_text('host1'))
    host2 = inv.get_host(to_text('host2'))

    inv.add_host(host=host1, group='all')
    inv.add_host(host=host2, group='all')

    host1.set_variable('test', 0)
    host2.set_variable('test', 1)

# Generated at 2022-06-22 12:15:59.312128
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.plugins import module_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    import collections
    import yaml

    # create necessary objects
    mock_loader = module_loader.ModuleLoader()
    mock_inventory = InventoryManager(loader=mock_loader)
    mock_

# Generated at 2022-06-22 12:16:05.624686
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory

    class FakeHost:
        def __init__(self, name):
            self.name = name

    hosts = [FakeHost('h1'), FakeHost('h2')]

    class FakeInventory:
        hosts = hosts

    h = HostVars(FakeInventory, None, None)

    assert set(h.keys()) == set([h.name for h in hosts])

# Generated at 2022-06-22 12:16:12.676013
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import os

    hostvars = HostVars({'a': 'A', 'b': 'B'}, inventory='inventory.file')

    assert sorted(list(hostvars.__iter__())) == sorted(['a', 'b'])



# Generated at 2022-06-22 12:16:21.988372
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # This test requires a functional inventory and variable manager
    # to be created.
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    group_name = 'test_group1'

    loader = DataLoader()

    # Create a variable manager and inventory, add group and a host to group
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    group = inventory.add_group(group_name)

    test_host = inventory.add_host(host='testHost1', group=group)

    # Create hostvars
    hostvars = HostVars(inventory, variable_manager, loader)

    #

# Generated at 2022-06-22 12:16:27.709489
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    hostvars = HostVars(Inventory(DataLoader()), VariableManager(), DataLoader())
    assert hostvars.raw_get("localhost") == {"ansible_python_interpreter": "/usr/bin/python"}

# Generated at 2022-06-22 12:16:37.913436
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.utils import context_objects as co

    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    inventory.add_host(Host('test', groups=['group']))
    inventory.add_group(Group('group'))
    inventory.add_child('group', 'all')

    play_context = PlayContext()

    vars_manager = VariableManager()

# Generated at 2022-06-22 12:16:49.440948
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ..plugins.inventory import InventoryPlugin
    from ..plugins import module_loader
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.constants as C

    loader = ansible.parsing.dataloader.DataLoader()
    group_vars = ansible.parsing.dataloader.DataLoader()
    host_vars = ansible.parsing.dataloader.DataLoader()
    inventory = InventoryPlugin(loader=loader)
    inventory.add_host('localhost')
    inventory.set_variable('localhost','ansible_connection','local')
    inventory.set_variable('localhost','test_var','test_val')

# Generated at 2022-06-22 12:17:00.627549
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.module_utils.six.moves import builtins
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'a': 'variable_manager',
        'b': 'extra_vars'
    }
    loader = DataLoader()

    hostvars = HostVars(inventory=None,
                        variable_manager=variable_manager,
                        loader=loader)

    hostvars.set_host_variable(host='localhost', varname='c', value='set_host_variable')
    hostvars.set_host_variable(host='localhost', varname='d', value='set_host_variable')

# Generated at 2022-06-22 12:17:11.895417
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import itertools
    import os
    import sys
    import unittest

    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    class HostVarsVars__getitem__TestCase(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.inventory = InventoryManager(loader=self.loader, sources='')
            self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
            self.hostvars = HostVars(self.inventory, self.variable_manager, self.loader)


# Generated at 2022-06-22 12:17:18.217575
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    inventory = AnsibleInventory(loader=C.DEFAULT_LOADER, variable_manager=variable_manager)
    result = HostVars(inventory=inventory, variable_manager=variable_manager, loader=C.DEFAULT_LOADER)
    assert result.raw_get('localhost') == {'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost'}


# Generated at 2022-06-22 12:17:30.120713
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host_name = "localhost"
    host = Host(name=host_name)
    variable_manager._inventory._hosts_cache[host_name] = host
    variable_manager.set_nonpersistent_facts(host=host, facts=dict(host_name=host_name))


# Generated at 2022-06-22 12:17:31.709683
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    ''' Test `HostVars` objects iteration '''
    pass # TODO

# Generated at 2022-06-22 12:17:41.506419
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import pickle
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = pickle.dumps(PlaybookLoader(None))
    inventory = pickle.dumps(InventoryManager(loader))
    variable_manager = pickle.dumps(VariableManager(loader))
    play_context = pickle.dumps(PlayContext())

    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    play._variable_manager = variable_manager
    play._context = play_context

    current = pickle.dumps(HostVars(inventory, variable_manager, loader))
    test = pickle.loads(current)

    assert test._

# Generated at 2022-06-22 12:17:53.677512
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import json
    host = 'localhost'
    vars = dict(a=1, b=2, c=3, d=4)
    h = HostVars(inventory=None, variable_manager=None, loader=None)
    assert h.raw_get(host) == vars
    assert json.loads(repr(h.raw_get(host))) == vars
    assert str(h.raw_get(host)) == str(vars)
    assert h.raw_get(host)["a"] == vars["a"]
    assert h.raw_get(host).get("a") == vars.get("a")
    assert h.raw_get(host)["b"] == vars["b"]
    assert h.raw_get(host)["c"] == vars["c"]
    assert h.raw_

# Generated at 2022-06-22 12:18:05.543188
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Use a fixed seed so results are deterministic
    import random
    random.seed(42)

    # Create a hostvars object that can be passed to template
    # rendering engine.
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Create hostvars for two hosts and add to inventory
    for hostname in ["host1", "host2"]:
        host = inventory.add_host(hostname)

# Generated at 2022-06-22 12:18:15.053020
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    loader = None

    inventory = Inventory(loader=loader)
    inventory.add_host(Host("localhost"))

    variable_manager = VariableManager()
    variable_manager.add_group_vars(inventory, "ungrouped", {
        "test": 'hello',
    })
    variable_manager.add_host_vars(inventory, "localhost", {
        "test": 'world',
    })

    hostvars = HostVars(inventory, variable_manager, loader)

    iterator = iter(hostvars)

    hostname = next(iterator)
    assert hostname == 'localhost'


# Generated at 2022-06-22 12:18:23.253953
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import unittest, mock

    vars_cache = dict(foo='bar')
    mock_get_host = mock.Mock()
    mock_get_host.return_value = 'host_object'
    inventory_object = mock.Mock()
    inventory_object.hosts = []

    for host in vars_cache.keys():
        inventory_object.hosts.append(mock.Mock(name=host))

    hostvars = HostVars(inventory_object, mock.Mock(), mock.Mock())

    for host in hostvars:
        assert(host == hostvars._find_host(host))



# Generated at 2022-06-22 12:18:31.612970
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import collections
    import sys

    class TestVarsCache(collections.Mapping):
        def __init__(self):
            self._data = {'a': 2, 'b': 3}
        def __getitem__(self, key):
            return self._data[key]
        def __contains__(self, key):
            return key in self._data
        def __iter__(self):
            return iter(self._data)
        def __len__(self):
            return len(self._data)

    class TestInventory(object):
        def __init__(self):
            self.hosts = ['a', 'b']
            self.vars_cache = TestVarsCache()


# Generated at 2022-06-22 12:18:33.046604
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    assert HostVars(None, None, None)

# Generated at 2022-06-22 12:18:46.373365
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inv_file = os.path.join(os.path.dirname(__file__), 'test_hostvars_inventory.yml')
    inv = InventoryManager(loader=DataLoader(), sources=inv_file)
    vars_manager = VariableManager(loader=DataLoader(), inventory=inv)

    # Test host vars
    hvars = HostVars(inv, vars_manager, DataLoader())
    assert hvars.raw_get('faire') == {'ansible_ssh_host': '192.168.1.54'}

# Generated at 2022-06-22 12:18:49.522140
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert HostVars(inventory=None, variable_manager=None, loader=None).__getitem__('test_name') == AnsibleUndefined(name="hostvars['test_name']")



# Generated at 2022-06-22 12:19:02.186307
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Prepare data
    inventory_path = os.path.join(os.path.dirname(__file__), '../../../data/inventory')
    inventory = Inventory(loader=DataLoader(), sources=inventory_path, vault_password='ASDASD')
    variables = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variables, loader=DataLoader())

    # Execute method
    repr_value = repr(hostvars)

    # Perform test and assertions
    expected_value = repr(dict([('host1', {'hostvars': {'hostvars': {'hostvars': {'hostvars': {'foo': 'bar'}}}}})]))
    assert repr_value == expected_value


# Generated at 2022-06-22 12:19:12.060967
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)

    hosts = ['localhost', '127.0.0.1']
    for host in hosts:
        group = inventory.get_group('all')
        new_host = inventory.add_host(host=host, group=group)
        variable_manager.set_host_variable(new_host, 'host_var', 'host_var_value')

    hostvars = HostVars(inventory, variable_manager, loader)
    count = 0
    for host in hostvars:
        count += 1

        hostvars

# Generated at 2022-06-22 12:19:23.770740
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    inventory = InventoryManager(host_list=['localhost'])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = Play()
    task_vars = {}
    host_vars = HostVars(inventory, variable_manager, loader=None)

    # Test with undefined host
    assert isinstance(host_vars.raw_get('undef_host'), AnsibleUndefined)

    # Test when variables are not set in host cache
    inventory.add_host(host='host1')
    assert host_vars.raw_get('host1') == {}

    # Test with

# Generated at 2022-06-22 12:19:35.760736
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    '''
    Because method __setstate__ of class HostVars uses
    attribute _loader, it needs to be verified during
    serialization/deserialization.

    This unit test includes serialization and deserialization
    of object to ensure that serialized object is the same
    as the original one, along with verifying that
    attributes _loader and _hostvars of VariableManager
    objects were assigned correctly.
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # setup simple inventory, play and task
    host1 = MockHost("host1")
    host2 = MockHost("host2")
    inventory = MockInventory

# Generated at 2022-06-22 12:19:45.885976
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=None, sources='')
    hostvars = HostVars(inventory, variable_manager=None, loader=None)

    import ansible.vars.hostvars
    ansible.vars.hostvars.HostVars = HostVars

    # Method __repr__ of class HostVars should raise exception
    # if inventory is not set (inventory is None).

# Generated at 2022-06-22 12:19:55.560837
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    inventory = Inventory("")
    loader = None
    variable_manager = VariableManager(loader=loader)

    host_vars_instance = HostVars(inventory=inventory, loader=loader, variable_manager=variable_manager)

    assert list(host_vars_instance) == []

    inventory.hosts = {
        "localhost": "",
        "slave": "",
        "master": ""
    }

    assert list(host_vars_instance) == ["localhost", "slave", "master"]

    inventory.hosts = {}

    assert list(host_vars_instance) == []

# Generated at 2022-06-22 12:20:06.043145
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.playbook import Playbook
    from ansible.vars import VariableManager

    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='ping', args=''), register='ping_result'),
        ]
    )
    play = Playbook().load(play_source, variable_manager=VariableManager(), loader=False)
    inventory = play.inventory
    hostvars = HostVars(inventory, play.variable_manager, loader=False)

    # empty inventory
    assert [] == list(hostvars)

    # inventory with many hosts
    inventory.add_host(host="host1")
    inventory.add_host(host="host2")

# Generated at 2022-06-22 12:20:17.119487
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.variables import VariableManager

    # Create objects to be passed to __setstate__
    variable_manager = VariableManager()
    variable_manager._loader = 'loader'
    variable_manager._hostvars = 'hostvars'

    class _Inventory(object):
        pass

    inventory = _Inventory()

    hostvars = HostVars(inventory, variable_manager, loader='loader')

    # Use __setstate__ to set state of variable_manager and hostvars
    # objects to None
    hostvars.__setstate__({
        '_inventory': inventory,
        '_loader': 'loader',
        '_variable_manager': variable_manager,
    })

    # Assert that _loader and _hostvars attributes of variable_manager
    # object have been recovered and are equal to originally created
   

# Generated at 2022-06-22 12:20:44.740121
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    source = dict(
        _inventory=Inventory(),
        _loader='_loader',
        _variable_manager=VariableManager(),
    )
    hostvars = HostVars(None, None, None)

    hostvars.__setstate__(source)

    assert hostvars._inventory == source['_inventory']
    assert hostvars._loader == source['_loader']
    assert hostvars._variable_manager._loader == source['_loader']
    assert hostvars._variable_manager._hostvars is hostvars

    assert hostvars._variable_manager is source['_variable_manager']

    source['_variable_manager']._loader = None
    source['_variable_manager']._hostvars = None
    hostv

# Generated at 2022-06-22 12:20:54.127901
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR
    variable_manager = VariableManager()
    variable_manager.extra_vars = {"var1": "foo", "var2": "bar"}
    variable_manager.options = Options({'hash_behaviour': DEFAULT_HASH_BEHAVIOUR})
    host_vars = HostVars(None, variable_manager, None)
    assert repr(host_vars) == "{'localhost': {'var1': 'foo', 'var2': 'bar'}}"


# Generated at 2022-06-22 12:21:02.695912
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory_manager = InventoryManager(loader=loader, sources=['localhost,'])
    hostvars = HostVars(inventory_manager, variable_manager, loader)

    assert isinstance(hostvars, Mapping)
    assert isinstance(hostvars, HostVars)
    assert isinstance(hostvars, HostVarsVars)

    assert next(iter(hostvars)) == 'localhost'

# Generated at 2022-06-22 12:21:11.951220
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.vault import VaultLib
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars import TokenData
    from ansible.utils.vars import combine_vars
    from ansible.errors import AnsibleError
    import tempfile
    import shutil
    import os
    import pytest
    import yaml

    datadir = os.path.join(os.path.dirname(__file__), 'data')
    host_vars_path = os.path.join(datadir, 'host_vars')
    project_vars_path = os.path.join(datadir, 'group_vars/all')
    inventory_path = os.path.join(datadir, 'hosts')



# Generated at 2022-06-22 12:21:20.393724
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    class TestInventory(Inventory):
        def get_host(self, hostname):
            if hostname == 'localhost':
                return 'localhost'
            else:
                return None

    foo = {}
    foo['foo'] = '{{ 1+2 }}'
    foo['bar'] = 'no template'
    hostvars = HostVarsVars(foo, DataLoader())
    assert hostvars['foo'] == '3'
    assert hostvars['bar'] == 'no template'

    # To cover the situation when play_vars is None, we need to create a
    # VariableManager.  So, the simplest VariableManager will be created here.

# Generated at 2022-06-22 12:21:30.136339
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import pickle
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create a sample object of class HostVars to test
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext(variable_manager=variable_manager)
    fake_hostvars = HostVars(inventory, variable_manager, loader)

    # Save it first to be able to load it
    with open('/tmp/testpickle', 'wb') as f:
        pickle.dump(fake_hostvars, f, protocol=0)

# Generated at 2022-06-22 12:21:39.305602
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():

    class TestHostVarsVars(HostVarsVars):
        def __init__(self, variables, loader):
            super(TestHostVarsVars, self).__init__(variables, loader)
            self.template_res = {}

        def template(self, data, fail_on_undefined=False, override_vars=None, static_vars=None):
            self.template_res['data'] = data
            self.template_res['fail_on_undefined'] = fail_on_undefined
            self.template_res['override_vars'] = override_vars
            self.template_res['static_vars'] = static_vars
            return 'template_result'

    variables = {'foo': 'bar'}
    loader = None


# Generated at 2022-06-22 12:21:45.772960
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Dictionary to store class instances
    instances = {}

    # Class VariableManager
    instances['variable_manager'] = VariableManager()

    # Class Host
    instances['host'] = Host(name='test')

    # Class HostVars
    instances['hostvars'] = HostVars(
        inventory=None,
        variable_manager=instances['variable_manager'],
        loader=BaseLoader()
    )

    # Get the state
    state = instances['hostvars'].__getstate__()

    # Remove _hostvars attribute from the instance of VariableManager
    instances['variable_manager'].__dict__.pop('_hostvars', None)

    # Set the state again
    instances['hostvars'].__setstate__(state)

    # Assert

# Generated at 2022-06-22 12:21:53.868024
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources='')
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)

    assert isinstance(hostvars, HostVars)
    assert isinstance(hostvars.__iter__(), type(iter([])))

# Generated at 2022-06-22 12:22:00.789600
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    hostvars = {'a': {'b': '{{ c }}', 'd': '{{ c }}'}}
    hostvars_vars = HostVarsVars(hostvars, loader=None)
    hostvars_vars['a']['b'] = 1
    hostvars_vars['c'] = 2
    assert hostvars_vars['a']['b'] == 2
    assert hostvars_vars['a']['d'] == 2
    assert hostvars_vars['c'] == 2

# Generated at 2022-06-22 12:22:48.326017
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import random
    import string
    import tempfile

    class MockVariableManager(object):

        def __init__(self, inventory, loader):
            self.inventory = inventory
            self.loader = loader
            self.vars_cache = {}

        def get_vars(self, host=None, include_hostvars=True):
            if host is None:
                return dict()

            if host.name not in self.vars_cache:
                self.vars_cache[host.name] = dict()

            return self.vars_cache[host.name]

        def set_host_variable(self, host, varname, value):
            assert isinstance(host, MockHost)
            assert isinstance(varname, basestring)

# Generated at 2022-06-22 12:22:58.577102
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class FakeLoader:
        def __init__(self):
            self._templar = Templar(loader=self)

        def get_basedir(self):
            return '.'

    class FakeVariableManager:
        def __init__(self):
            self._variables = dict(ansible_version="2.0")
            self._vault_secrets = {}

        def get_vars(self, play=None, host=None, task=None, include_hostvars=True):
            return self._variables

        def get_vault_secrets(self, play=None, host=None, task=None, vault_ids=None):
            return self._vault_secrets

    class FakeHost:
        def __init__(self, name):
            self.name = name
            self.vars = dict()

# Generated at 2022-06-22 12:23:09.958771
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import copy
    from ansible.inventory.host import Host

    # TODO: make this test less dependent on internal implementation details
    # of ansible.playbook.play.Play and ansible.playbook.play.PlayContext

    # create a HostVars instance
    inventory = [Host(name='localhost')]
    variable_manager = FakeVariableManager()
    loader = FakeLoader()
    hostvars = HostVars(inventory, variable_manager, loader)

    # verify that a initial state of HostVars is iterable
    assert(len(list(hostvars)) == 1)

    # make a copy of the HostVars instance
    hostvars_copy = copy.deepcopy(hostvars)

    # change 'hosts' attribute of hostvars._inventory
    hostvars._inventory.hosts = []

    # verify

# Generated at 2022-06-22 12:23:21.495356
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import sys
    import pickle
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.objects import AnsibleUnicode

    loader = DummyLoader()
    inventory = Inventory(loader=loader)
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    host = inventory.get_host('testhost')

# Generated at 2022-06-22 12:23:29.828387
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.path import unfrackpath

    dummy_loader = DataLoader()
    dummy_variable_manager = VariableManager()

    # HostVars is immutable and has no set_host_variable method,
    # create a new instance of VariableManager so we can set host variables.
    variable_manager = VariableManager()
    hostvars = HostVars(loader=dummy_loader)
    hostvars.set_variable_manager(variable_manager)

    inventory_manager = InventoryManager(loader=dummy_loader,
                                         sources=unfrackpath("examples/hosts"))
    hostvars.set_inventory

# Generated at 2022-06-22 12:23:41.907831
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    inventory = InventoryManager(loader=DataLoader(), sources=["localhost"])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, DataLoader())
    assert repr(hostvars) == "{'localhost': {}}"
    hostvars.set_host_variable(host=hostvars._find_host('localhost'), varname='foo', value='bar')
    print(hostvars)
    assert repr(hostvars) == "{'localhost': {'foo': 'bar'}}"

# Generated at 2022-06-22 12:23:50.954921
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    def make_hostvars(variables):
        from ansible.inventory.manager import InventoryManager
        from ansible.parsing.dataloader import DataLoader

        # Make an inventory with single host myhost and variables
        inventory = InventoryManager(loader=DataLoader())
        host = Host("myhost")
        group = Group("all")
        group.add_host(host)
        inventory.add_group(group)
        inventory.add_host(host)
        inventory.set_variable_manager(VariableManager(inventory=inventory))
        inventory.set_variable_manager(VariableManager(inventory=inventory, loader=DataLoader()))

        # Create HostVars object
        return Host

# Generated at 2022-06-22 12:23:58.960489
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    v1 = {'s1': 'v1', 's2': '{{v2}}'}
    v2 = {'k1': 'v1', 'k2': 'v2'}
    v3 = {'s1': 'v1', 's2': 'v2'}

    assert HostVarsVars(v1, None) == {'s1': 'v1', 's2': '{{v2}}'}

    templar = Templar(variables=v1, loader=None)
    assert HostVarsVars(v1, templar) == {'s1': 'v1', 's2': 'v2'}
    assert HostVarsVars(v1, templar) == v3