

# Generated at 2022-06-22 12:14:28.301731
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    hosts = [ 'host1', 'host2', 'host3' ]
    variable_manager = DummyVariableManager(hosts)
    hostvars = HostVars(DummyInventory(hosts), variable_manager, DummyLoader())

    for host in hosts:
        variable_manager.set_host_variable(host, 'foo', 'bar')
        assert hostvars.raw_get(host)['foo'] == 'bar'

    assert hostvars.raw_get('host4') == AnsibleUndefined(name="hostvars['host4']")


# Generated at 2022-06-22 12:14:39.455014
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Hide the real implementation of VariableManager because we do not have
    # an inventory and loader to claim them.
    class VariableManager:
        def __init__(self):
            self._loader = None
            self._hostvars = None

        def __getstate__(self):
            return dict(vars=dict(name='Ansible', version=(2, 0, 0)))

        def __setstate__(self, state):
            self.vars = state['vars']

    inventory = None
    loader = None
    variable_manager = VariableManager()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hostvars_state = dict(
        _variable_manager=variable_manager,
        _loader=loader,
        _inventory=inventory,
    )
   

# Generated at 2022-06-22 12:14:46.726750
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    variables = {'x': 1, 'y': 2}
    loader = None

    try:
        hvv = HostVarsVars(variables, loader)
        for i, var in enumerate(hvv):
            assert(var == list(variables.keys())[i])
    except AssertionError as e:
        raise AssertionError('HostVarsVars.__iter__() test failed: %s' % e.args)


# Generated at 2022-06-22 12:14:49.454949
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    test_inventory = FakeInventory()
    test_variable_manager = FakeVariableManager()
    test_loader = FakeLoader()
    test_hostvars = HostVars(test_inventory, test_variable_manager, test_loader)
    assert repr(test_hostvars) == "{}"

    test_inventory.hosts.append('localhost')
    test_hostvars.set_host_facts('localhost', {'somefact': 'somevalue'})
    assert repr(test_hostvars) == "{'localhost': {'somefact': 'somevalue'}}"


# Generated at 2022-06-22 12:14:56.056536
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create inventory
    inventory = InventoryManager(loader=None, sources=('127.0.0.2,'))
    inventory.add_host('127.0.0.1')
    inventory.add_child('child', inventory.get_host('127.0.0.1'))
    inventory.get_host('127.0.0.2').set_variable('magic', 42)

    # Create variable manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    variable_manager.set_host_variable('127.0.0.2', 'magic', 'not42')

    # Create hostvars
    hostvars = HostVars(inventory, variable_manager, loader=None)



# Generated at 2022-06-22 12:15:04.915892
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    # Create a temporary file for testing
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Set some variables
    inventory = InventoryManager(loader=loader, sources=path)
    inventory.add_host('host1')
    inventory.add_host('host2')
    inventory.add_host('host3')
    inventory.set_variable('host1', 'var1', 'value1')
    inventory.set_variable('host1', 'var2', 'value2')
    inventory.set_variable('host2', 'var1', 'value1')
    inventory.set_variable('host2', 'var2', 'value2')
    inventory.set_variable('host3', 'var1', 'value1')
    inventory.set_variable('host3', 'var2', 'value2')


# Generated at 2022-06-22 12:15:13.218682
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import sys
    import os
    import pytest

    # We need to create an inventory to test module,
    # so create a fake one and the required directories
    class FakeInventory():
        def __init__(self, hosts_data):
            self.hosts = [hosts_data]

    class FakeLoader():
        pass

    # Create fake inventory
    FAKE_INVENTORY_HOST = "fake_inventory_host"
    fake_hosts_data = {
        "hostname": FAKE_INVENTORY_HOST,
        "vars": {
            "greeting": "Hello",
            "name": "World",
            "missing_name": "{{ missing_name }}",
        }
    }
    fake_inventory = FakeInventory(fake_hosts_data)

    # Create fake

# Generated at 2022-06-22 12:15:25.101611
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager

    yaml_data = """
---
- hosts:
    test:
        ansible_port: 2222
    test2:
        ansible_port: 2222
    localhost:
        ansible_port: 2222
    fake:
        ansible_port: 2222
    fail:
        ansible_port: 2222
    ungrouped:
        ansible_port: 2222
"""

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=yaml_data)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # check whether HostVars can be iterated

# Generated at 2022-06-22 12:15:35.553666
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._loader = loader
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=[])
    host1 = Host('host1')
    host2 = Host('host2')
    group = Group('all')
    group.add_host(host1)
    group.add_host(host2)
    inventory.add_group(group)
    inventory.add_host(host1)
    inventory.add_host(host2)

    hostvars = Host

# Generated at 2022-06-22 12:15:46.527184
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    play_context = PlayContext(inventory=inventory)

    hostvars_obj = HostVars(inventory=inventory, variable_manager=play_context.variable_manager, loader=DataLoader())


# Generated at 2022-06-22 12:15:58.240891
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    hostvars = HostVars(inventory, variable_manager, loader)

    # test existence of ansible host
    assert 'localhost' in hostvars

    # test non-existence host
    assert 'somehost' not in hostvars

    # test undefined
    assert hostvars.raw_get('somehost')._name == "hostvars['somehost']"
    assert hostvars['somehost']._name == "hostvars['somehost']"

    # test existence of

# Generated at 2022-06-22 12:16:05.397988
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host

    # Create an empty inventory
    inventory = Inventory(loader=None)
    host = Host(name='fake_host')

    # Create a HostVars instance with the non-empty inventory
    hv = HostVars(inventory, variable_manager=None, loader=None)
    inventory.add_host(host)

    # Test if the __repr__ method runs as expected
    assert repr(hv) == "{'fake_host': {}}"

# Generated at 2022-06-22 12:16:14.898219
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory_manager = InventoryManager()

    # Test with empty inventory
    hostvars = HostVars(inventory_manager, VariableManager(), None)
    assert repr(hostvars) == '{}'

    # Test with populated inventory
    inventory_manager.inventory = dict(
        all=dict(
            children=dict(
                group1=dict(),
                group2=dict(),
            )
        )
    )
    hostvars = HostVars(inventory_manager, VariableManager(), None)
    assert repr(hostvars) == '{}'

# Generated at 2022-06-22 12:16:21.983865
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.hostvars import HostVars
    class DummyVariableManager:
        _loader = None
        _hostvars = None
    class DummyInventory:
        hosts = []
    class DummyLoader:
        pass
    vm = DummyVariableManager()
    loader = DummyLoader()
    hv = HostVars(DummyInventory(), vm, loader)
    vm._hostvars = None
    vm._loader = None
    hv.__setstate__({})

# Generated at 2022-06-22 12:16:30.257083
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hvars = HostVars(inventory, variable_manager, loader)
    assert hvars._find_host("localhost") is not None

    for host in hvars:
        assert hvars._find_host(host) is not None

# Generated at 2022-06-22 12:16:35.688401
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars

    v = VariableManager()
    hvv = HostVarsVars(v.get_vars(), Templar(vars=v.get_vars()))

    assert len(list(hvv.__iter__())) == 19


# Generated at 2022-06-22 12:16:47.143534
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import sys

    class MyVars(dict):

        def __delitem__(self, key):
            raise NotImplementedError()

        def __setitem__(self, key, value):
            raise NotImplementedError()

        def clear(self):
            raise NotImplementedError()

        def pop(self, key):
            raise NotImplementedError()

        def popitem(self):
            raise NotImplementedError()

        def setdefault(self, key, default):
            raise NotImplementedError()

        def update(self, other):
            raise NotImplementedError()

    myvars = MyVars({'foo': 'bar'})

    hostvars = HostVarsVars(myvars, None)
    hostvars[0]

    iter = hostvars.__iter

# Generated at 2022-06-22 12:16:53.693223
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader,['tests/inventory'])
    variable_manager = VariableManager()

    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars.raw_get('localhost') == variable_manager.get_vars(host=inventory.get_host('localhost'), include_hostvars=False)



# Generated at 2022-06-22 12:17:01.562610
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    """
    A unit test for the `HostVarsVars.__iter__` method.

    This unit test covers the case where the `iter(obj)` call
    returns a generator.  This is a requirement for the method
    to be a correct implementation of the `__iter__` method.
    """
    obj = HostVarsVars({"foo": "bar"}, None)
    result = iter(obj)
    assert hasattr(result, "__next__")

# Generated at 2022-06-22 12:17:10.175883
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.constants import DEFAULT_HOST_LIST
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    inventory = Inventory(DEFAULT_HOST_LIST)
    variable_manager = VariableManager()
    loader = variable_manager._loader
    hostvars = HostVars(inventory, variable_manager, loader)
    host, raw_hostvars = 'localhost', hostvars.raw_get('localhost')
    assert raw_hostvars
    assert 'ansible_ssh_host' in raw_hostvars
    assert 'ssh_host' not in raw_hostvars



# Generated at 2022-06-22 12:17:20.996244
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=["tests/units/module_utils/test_hostvars.inv"])

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    host = hostvars['darkstar']
    assert host['var_a'] == 1
    assert host['var_c'] == 3
    assert host['var_d'] == 4
    assert host['var_f'] == 6
    assert host['var_g'] == 7

    host = hostvars['localhost']
    assert host['var_a']

# Generated at 2022-06-22 12:17:30.070447
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager(), host_list=['localhost'])
    vars_manager = VariableManager(loader=loader, inventory=inv)
    hostvars = HostVars(inventory=inv, variable_manager=vars_manager, loader=loader)

    # test with undefined host
    assert hostvars.raw_get('undefined') == AnsibleUndefined(name="hostvars['undefined']")

# Generated at 2022-06-22 12:17:40.191858
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Generated at 2022-06-22 12:17:47.390943
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(inventory=ImmutableDict(hosts=[ 'localhost', '127.0.0.1' ]))
    variable_manager = VariableManager(inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)
    assert sorted(hostvars) == [ '127.0.0.1', 'localhost' ]

# Generated at 2022-06-22 12:17:48.635179
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert False, "Not implemented"

# Generated at 2022-06-22 12:18:00.167781
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    inv_source = ""
    inv_source += "[servers]\n"
    inv_source += "localhost ansible_connection=local\n"
    inv_source += "server.example.com\n"

    loader = DictDataLoader({'host_vars': {'localhost': {'foo': 'bar'}}, 'group_vars': {'servers': {'baz': 'qux'}}})
    inventory = InventoryManager(loader=loader, sources=inv_source)

    variable_manager = VariableManager()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    hosts = ['localhost', 'server.example.com']
    count = 0

# Generated at 2022-06-22 12:18:12.116907
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class FakeInventory:
        def __init__(self):
            self._hosts = {}

        def get_host(self, name):
            try:
                return self._hosts[name]
            except KeyError:
                host = Host(name)
                self._hosts[name] = host
                return host

    class FakeVariableManager:
        def __init__(self):
            self.vars_cache = {}

        def get_vars(self, host, include_hostvars):
            try:
                return self.vars_cache[host]
            except KeyError:
                self.vars_cache[host] = {}
                return self.vars_cache[host]

    class FakeHost:
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-22 12:18:23.065046
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.galaxy_cli.main import GalaxyCLI
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders, get_all_plugins


# Generated at 2022-06-22 12:18:28.518346
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    class LoaderStub(object):
        def get_basedir(self):
            return 'ansible/loader'
    loader_stub = LoaderStub()
    values = { 'foo': 1, 'bar': 2 }
    host_vars_vars = HostVarsVars(values, loader=loader_stub)
    result = list(iter(host_vars_vars))
    assert(len(result) == 2)


# Generated at 2022-06-22 12:18:34.905481
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVarsVars

    class DummyInventory(dict):
        def __init__(self):
            super(DummyInventory, self).__init__()
        def get_host(self, host_name):
            return self.get(host_name)
        def add_host(self, host):
            self[host.name] = host

    class DummyHost(dict):
        def __init__(self, host_name):
            self.name = host_name

    class DummyVariableManager(VariableManager):
        def __init__(self):
            super(DummyVariableManager, self).__init__()
            self._vars_cache = {'host_name': 'host_var'}

    inventory = DummyIn

# Generated at 2022-06-22 12:18:45.176103
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class DummyModule(object):
        def __init__(self):
            self.params = {'test1': 'test2'}

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager())
    loader = DataLoader()
    variable_manager = VariableManager()
    play_source = dict(
        name="Ad-hoc",
        hosts='host1',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='ping'), register='ping_result')
        ]
    )
    play = Play

# Generated at 2022-06-22 12:18:53.374383
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=C.DEFAULT_LOADER_NAME, sources=[]))

    hostvars = HostVars(inventory=variable_manager.inventory, variable_manager=variable_manager, loader=C.DEFAULT_LOADER_NAME)
    hostvars._vars_cache["foo"] = dict(a=1, b=2)
    assert hostvars["foo"] == dict(a=1, b=2)
    hostvars._vars_cache["foo"] = dict(a=1, b=2, c=dict(x=5, y=6))

# Generated at 2022-06-22 12:19:00.088216
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    loader = None
    variable_manager = None
    hv = HostVars(None, variable_manager, loader)

    hv_dict = {
        '_inventory': None,
        '_loader': loader,
        '_variable_manager': variable_manager,
    }

    hv.__setstate__(hv_dict)

# Generated at 2022-06-22 12:19:10.773889
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create inventory, variable manager and hostvars
    context.CLIARGS = {'inventory': [os.path.join(os.path.dirname(__file__), '../../test/unit/ansible_test_inventory')]}
    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # Check data obtained from HostVars
    test_host = inventory.get_host('test_host')
    assert (hostvars['test_host'] == variable_manager.get_vars(host=test_host))

# Generated at 2022-06-22 12:19:22.126191
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import pickle
    from ansible.vars.manager import VariableManager

    # Create HostVars object to pickle
    host = MockHost("test")
    loader = MockDataLoader("")
    inventory = MockInventory([host])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Pickle the object and then unpickle it
    pickled_hostvars = pickle.dumps(hostvars)
    unpickled_hostvars = pickle.loads(pickled_hostvars)

    # Check if all required attributes are set after unpickling
    assert hasattr(unpickled_hostvars, '_inventory')
    assert hasattr(unpickled_hostvars, '_variable_manager')

# Generated at 2022-06-22 12:19:34.441745
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.plugins.loader import inventory_loader, vars_loader
    from ansible.playbook.play import Play

    class DummyVars:
        def __init__(self, vars_dict):
            self.vars_dict = vars_dict

        def get_vars(self, host=None, include_hostvars=False):
            return self.vars_dict

    class DummyPlay:
        def __init__(self):
            self._variable_manager = DummyVars({})

        def _load_vars(self, host=None):
            pass

        def get_variable_manager(self):
            return self._variable_manager

    class DummyInventory:
        def __init__(self):
            self._hosts = []
            self._hosts_cache = {}

       

# Generated at 2022-06-22 12:19:41.139631
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({
        "host_vars/hostname": """
some_variable: foo
"""})

    inventory = InventoryManager(loader)
    inventory.parse_inventory(host_list="hostname")
    variable_manager = VariableManager(loader, inventory)

    hostvars = HostVars(inventory, variable_manager, loader)
    assert repr(hostvars) == "{'hostname': {'some_variable': 'foo'}}"



# Generated at 2022-06-22 12:19:50.475029
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # Create empty inventory and hosts list
    inventory = type('Inventory', (), {})()
    inventory.hosts = []

    # Create empty variable manager
    variable_manager = type('VariableManager', (), {})()
    variable_manager._hostvars = {}

    # Create empty loader
    loader = type('Loader', (), {})()

    # Create instance of HostVars
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test if method __iter__ returns generator
    assert isinstance(hostvars.__iter__(), type(hostvars._find_host("localhost")))

# Generated at 2022-06-22 12:20:02.342835
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():  # noqa
    # kwargs is a "dict" which is a "Mapping" with no '_loader' attribute
    kwargs = {}
    # instantiate a HostVars with a "dict"
    instance = HostVars(kwargs)
    # set instance._loader to a "Mock" object
    instance._loader = Mock()
    # kwargs is a "dict" which has no 'hostvars' attribute
    instance._kwargs = kwargs
    # call method __getitem__ of class HostVars
    ret = instance.__getitem__('hostvars')
    # assert the type of ret is HostVars
    assert isinstance(ret, HostVars)
# Add an attribute '__setstate__' to class HostVars
HostVars.__setstate__ = test_HostVars___getitem

# Generated at 2022-06-22 12:20:09.139203
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({
        'some_playbook.yml': "",
        'group_vars/something.yml': "somevar: foo",
        'host_vars/somehost.yml': "somevar: bar",
    })

    inventory = InventoryManager(loader=loader, sources='some_inventory_source')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # The variable 'somevar' is set to string 'bar' in host_vars/somehost.yml
    # but should be string 'foo' in the end, because it's set to string 'foo'
    # in the lower priority group_

# Generated at 2022-06-22 12:20:24.637573
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from .inventory import Inventory
    from .loader import DataLoader
    from .vars_manager import VariableManager
    loader = DataLoader()

# Generated at 2022-06-22 12:20:36.730830
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inv_map = """
    localhost ansible_connection=local
    """.strip()

    inv = InventoryManager(loader=loader, sources=inv_map)

    var_manager = VariableManager()
    var_manager.set_inventory(inv)

    host = inv.get_host("localhost")

    hostvars = HostVars(inventory=inv, loader=loader, variable_manager=var_manager)

    hostvars.set_host_variable(host, "var", "val")

    assert hostvars.get(host.name)["var"] == "val"

# Generated at 2022-06-22 12:20:45.506174
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    class DummyVariableManager:
        def __init__(self):
            self.vars_cache = {
                'foo': {'bar': 'baz'},
                'nested': {'foo': 'bar', 'bar': 'baz'},
            }

        def get_vars(self, *args, **kwargs):
            return self.vars_cache

    class DummyInventory:
        def __init__(self):
            self.hosts = ['foo', 'nested']

        def get_host(self, host_name):
            if host_name in self.hosts:
                return host_name
            else:
                return None

    vm = DummyVariableManager()
    inv = DummyInventory()

    hostvars = HostVars(inv, vm, None)
    assert hostv

# Generated at 2022-06-22 12:20:58.215128
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,' + ','.join(STATIC_VARS)])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, None)
    assert 'localhost' in hostvars

    # Returned value should be __dict__ of a hostvars object
    hostvars_dict = hostvars.raw_get('localhost')
    assert isinstance(hostvars_dict, dict)
    assert len(hostvars_dict) == len(STATIC_VARS)
    for var in STATIC_VARS:
        assert var in hostvars_dict



# Generated at 2022-06-22 12:21:00.646359
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(["localhost"])
    assert repr(HostVars(inventory, None, None)) == "{'localhost': {}}"



# Generated at 2022-06-22 12:21:10.921156
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import ansible.vars.unsafe_proxy

    unsafe_vars = ansible.vars.unsafe_proxy.unsafe_proxy

    class MyUndefined(object):
        def __contains__(self, _):
            return False
        def __getitem__(self, _):
            return None
        def get(self, _, default=None):
            return default
        def __iter__(self):
            for v in ('1', '2'):
                yield v

    class MyVariables(object):
        def __init__(self):
            self.undefined = MyUndefined()

    class MyHostVarsVars(HostVarsVars):
        def __init__(self):
            HostVarsVars.__init__(self, {}, loader=None)
            self._vars = My

# Generated at 2022-06-22 12:21:18.161591
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager))

    hostvars = HostVars(variable_manager=variable_manager, loader=loader)

    hostvars.set_host_variable(variable_manager._inventory.get_host('127.0.0.1'), 'foo', 'bar')

# Generated at 2022-06-22 12:21:23.016371
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars_vars = HostVarsVars({'a':'a', 'b':'b', 'c':'c'}, None)
    assert set(hostvars_vars.__iter__()) == set(['a', 'b', 'c'])

# Generated at 2022-06-22 12:21:32.508223
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    var_mgr = VariableManager(loader=loader, inventory=inv)
    hostvars = HostVars(inv, var_mgr, loader)

    assert hostvars.raw_get('foo') is None
    assert hostvars.raw_get('localhost') == {}
    assert hostvars.raw_get('127.0.0.1') == {}
    assert hostvars.raw_get('::1') == {}
    assert hostvars.raw_get('127.0.0.1') == {}


# Generated at 2022-06-22 12:21:37.858285
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    h = HostVars(None, None, None)

    try:
        h.raw_get('localhost')
        assert False
    except KeyError:
        pass

    h.set_inventory(FakeInventory(['localhost']))
    assert h.raw_get('localhost') == {}
    assert h.raw_get('localhost') is not h.raw_get('localhost')



# Generated at 2022-06-22 12:21:55.298102
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader, sources=['inventory'])
    host_vars = HostVars(inventory, variable_manager, loader)

    host_one = ('fake_host_one', {'name': 'fake_host_one'})
    host_two = ('fake_host_two', {'name': 'fake_host_two'})

# Generated at 2022-06-22 12:22:04.772032
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({'host_vars/host.yml':
                                'variables_1: True\n'
                                'variables_2: True\n'
                            })
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    host = Host('dummy_host')
    variable_manager.add_host_variable(host, 'variables_1', False)
    variable_manager.add_host_variable(host, 'variables_2', False)

    hostvars_vars = hostvars['dummy_host']
   

# Generated at 2022-06-22 12:22:16.666817
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources='')
    # Populate inventory with hosts
    inventory.hosts = dict((host, None) for host in ['host1', 'host2'])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    inventory.set_variable_manager(variable_manager)
    inventory.set_host_variable('host1', 'foo', 'bar')
    inventory.set_host_variable('host2', 'foo', 'baz')

# Generated at 2022-06-22 12:22:28.017051
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    This test method is a regression test for issue #25263.

    The issue raised a TypeError exception when a host with
    vars_files was included in the inventory.

    The test is a modified version of the code in method
    _repr_ of class HostVars.
    '''
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=[])

    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    h = HostVars(inventory, variable_manager, loader)

    out = {}

# Generated at 2022-06-22 12:22:37.140334
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    im = InventoryManager(loader, None, sources={"localhost": """localhost ansible_connection=local"""})
    vm = VariableManager(loader=loader, inventory=im)

    hv = HostVars(im, vm, loader)

    # Test a simple case
    vm.extra_vars = {'foo': 'rope', 'baz': 'ropl'}
    assert hv['localhost']['foo'] == 'rope'

    # Test a case where the variable needs to be updated
    # with a default value before it can be accessed.
    assert hv['localhost']['ansible_host'] is not None

# Generated at 2022-06-22 12:22:46.962134
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    class MockLoader:
        pass

    loader = MockLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, os.path.expanduser("~/.ansible_hosts"), vault_password_file=os.path.expanduser("~/.vault_pass"))
    hostvars = HostVars(inventory, variable_manager, loader)
    play = Play.load(dict(name="Ansible Play", hosts="all"), variable_manager=variable_manager, loader=DataLoader())
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-22 12:22:50.554923
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    hostvars = HostVars({1: {'a': '{{ b }}', 'b': '{{ c }}', 'c': 'd'}}, None, None)
    assert hostvars[1]['a'] == 'd'


# Generated at 2022-06-22 12:23:00.075620
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class FakeInventory(object):
        def __init__(self):
            self._hosts_cache = {
                'host1': FakeHost('host1', 'all', 'fake-inventory'),
                'host2': FakeHost('host2', 'all', 'fake-inventory'),
            }

        def clear(self):
            raise Exception("clear not implemented")

        def get_host(self, hostname):
            if hostname not in self._hosts_cache:
                return None
            return self._hosts_cache[hostname]

        @property
        def hosts(self):
            return self._hosts_cache.values()

    class FakeHost(object):
        def __init__(self, name, group, inventory):
            self.name = name
            self.groups = [group]
            self.inventory = inventory



# Generated at 2022-06-22 12:23:06.224399
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    variables = {'a':'b', 'c':'d'}
    hh = HostVars(None, None, None)
    hh._variable_manager = object()
    hh._variable_manager.get_vars = lambda: variables
    assert hh.__repr__() == "{'localhost': {'a': 'b', 'c': 'd'}}"


# Generated at 2022-06-22 12:23:18.080093
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # pylint: disable=unused-variable,unused-argument,protected-access
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches

    import collections
    import json

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    loader = DataLoader()
    vault_secrets_file = None
    vault = VaultLib(vault_secrets_file)


# Generated at 2022-06-22 12:23:40.480365
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    data = {}
    with open('test/inventory/test_inventory.yml') as f:
        data['test_inventory.yml'] = f.read()
    inventory.load_inventory(data)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
   

# Generated at 2022-06-22 12:23:49.085070
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    hostvars = __import__('ansible.inventory').hostvars

    class Memo:
        pass

    # test HostVarsVars._vars
    vars = {'foo': '{{ bar }}', 'bar': 'baz', 'onetwo': '1{{ two }}'}
    vars_vars = hostvars.HostVarsVars(vars=vars, loader=None)
    assert vars_vars['foo'] == 'baz'
    assert vars_vars['onetwo'] == '12'

    # test HostVarsVars.__deepcopy__
    vars_vars_copy = copy.deepcopy(vars_vars, memo=Memo())
    assert vars_vars_copy is vars_vars

    # test HostVars._variable_manager.get

# Generated at 2022-06-22 12:23:58.073922
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Setup inventory with a host.
    hosts_path = '../../test/units/inventory/sample_hosts'
    my_inventory = InventoryManager(loader='', sources=hosts_path)
    host = my_inventory.get_host('foobar')

    # Setup fake loader.
    class FakeLoader:
        pass
    loader = FakeLoader()
    loader.get_basedir = lambda: '..'

    # Setup variable_manager.
    variable_manager = VariableManager(loader=loader, inventory=my_inventory)
    variable_manager._host_vars_plugins = None

    # Setup HostVars

# Generated at 2022-06-22 12:24:05.047389
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(host_list=[])
    variable_manager = VariableManager()
    loader = DataLoader()
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars._find_host = lambda x: None
    assert isinstance(hostvars.raw_get('foo'), AnsibleUndefined)

    hostvars._find_host = lambda x: x
    assert hostvars.raw_get('foo') == {}

    hostvars._variable_manager.set_host_variable('foo', 'bar', 'baz')
    assert hostvars.raw_get('foo') == {'bar': 'baz'}