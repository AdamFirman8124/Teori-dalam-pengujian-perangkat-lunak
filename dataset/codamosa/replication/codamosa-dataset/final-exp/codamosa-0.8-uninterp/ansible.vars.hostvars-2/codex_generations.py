

# Generated at 2022-06-22 12:14:24.381908
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(loader=None, sources='')
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager(loader=None, inventory=inventory)

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    hostvars = HostVars(inventory, variable_manager, loader)
    state = hostvars.__getstate__()
    assert state['_inventory'] == inventory
    assert state['_loader'] == loader
    assert state['_variable_manager'] == variable_manager
    hostvars.__setstate__(state)
    assert hostvars._inventory == inventory
    assert hostvars._loader == loader
    assert hostvars._variable_manager == variable_manager
    assert hostvars._

# Generated at 2022-06-22 12:14:33.443490
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    # VariableManager contains empty dicts
    assert 'localhost' not in hostvars

    # Set value to dict of 'localhost' in VariableManager
    hostvars.set_host_variable(host=inventory.get_host('localhost'), varname='foo', value='bar')

    # Test that value was set
    assert 'localhost' in hostvars

# Generated at 2022-06-22 12:14:45.105629
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import os
    import tempfile
    import shutil

    class inventory_dump(object):
        def __init__(self, hosts):
            self.hosts = hosts

        def get_host(self, host_name):
            if host_name in self.hosts:
                return {'name': host_name}
            else:
                return None

        def __setstate__(self, state):
            self.__dict__.update(state)


# Generated at 2022-06-22 12:14:56.567269
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # Setup
    inventory = make_fake_inventory()
    variable_manager = VariableManager()
    loader = DictDataLoader({})

    mock_host = inventory.hosts.get('host1')
    mock_host.name = 'host1'
    mock_host.vars.update({'one': '1', 'two': '2'})
    mock_host.get_groups.return_value = [inventory.groups.get('group1'), inventory.groups.get('all')]
    mock_host.get_group_vars.return_value = {'three': '3', 'four': '4'}

    # Action
    hostvars = HostVars(inventory, variable_manager, loader)
    host_vars = hostvars.raw_get(mock_host.name)

    # Assertions


# Generated at 2022-06-22 12:15:06.128664
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # This unit test covers a corner case of method __setstate__ of class HostVars.
    # It is not included in any test suite. To run it locally, execute:
    #   $ ansible-test units --python 2.7 -t lib/ansible/vars/hostvars.py
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.loader.manager import SafeVariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    def instantiate_private_class(private_class, *args, **kwargs):
        return private_class.__new__(private_class, *args, **kwargs)

    # Create hostvars from scratch
    hostvars = instantiate

# Generated at 2022-06-22 12:15:18.745182
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    mgr = VariableManager(loader=None)
    templar = Templar(loader=None)

    # Try to raise error with incorrect variables' value
    class FakeInventory():
        def __init__(self):
            self.hosts = ['fakehost']
            self.host_vars = {'fakehost': {'foo': 'bar'}}
            self.groups = {'group1': {'hosts': ['fakehost'], 'vars': {'foo': 'bar'}}}
            self.groups_vars = {}
            self.group_vars = {}

        def get_host(self, host_name):
            return self.host_vars.get(host_name, None)


# Generated at 2022-06-22 12:15:26.839513
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.hostvars import HostVars

    hv = HostVars(None, None, None)
    assert repr(hv) == "{}"

    hv._inventory = MockInventory()
    hv._variable_manager = MockVariableManager()
    assert repr(hv) == "{'testhost1': {}, 'testhost2': {}}"

    class TestHost(object):
        name = 'testhost1'

    hv._inventory.hosts = [TestHost()]
    assert repr(hv) == "{'testhost1': {}}"


# Generated at 2022-06-22 12:15:36.739093
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])

    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # set the ansible_variable for the host localhost
    variable_manager.set_host_variable(host=hostvars._find_host('localhost'), varname='test', value="test")

    # get the ansible_variable test from hostvars

# Generated at 2022-06-22 12:15:47.027294
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    inventory = Inventory(host_list=[])
    variable_manager = VariableManager()

    hostvars = HostVars(inventory, variable_manager, None)

    assert hostvars._inventory is inventory
    assert hostvars._variable_manager is variable_manager
    assert variable_manager._hostvars is hostvars

    state = hostvars.__getstate__()

    hostvars = HostVars(None, None, None)
    hostvars.__setstate__(state)

    assert hostvars._inventory is inventory
    assert hostvars._variable_manager is variable_manager
    assert variable_manager._hostvars is hostvars

# Generated at 2022-06-22 12:15:56.499978
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import sys
    import copy
    import pickle
    import collections

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Method __iter__ of class HostVars provides the same functionality as method __iter__ of class dict.
    # Method __iter__ of class dict returns a view object which is an iterator over the dictionary's keys.
    # Method __iter__ of class HostVars returns a view object which is an iterator over the HostNames of the Hosts
    # in the inventory.

    # Create an inventory object from the default inventory file
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])

    # Create a variable manager object
    # The variable manager object is responsible for gathering and merging

# Generated at 2022-06-22 12:16:11.202007
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class Host():
        pass

    # Create host to be used in VariableManager
    host = Host()

    # Create HostVars object with some state
    loader = object()
    hostvars = HostVars(object(), object(), loader)
    hostvars._variable_manager = object()
    hostvars._variable_manager.set_host_variable(host, 'a', 1)  # assign some host variable

    # Use __setstate__ to restore HostVars object state
    hostvars.__setstate__(hostvars.__dict__)

    # Check that host variables are still available
    assert hostvars._variable_manager.get_vars(host=host)['a'] == 1

# Generated at 2022-06-22 12:16:13.089872
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # TODO: Implement the unit test
    raise NotImplementedError()


# Generated at 2022-06-22 12:16:22.301125
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host1 = Host(name='host1', groups=['group1','group2'], port=22)
    host2 = Host(name='host2', groups=['group2','group3'], port=22)
    host3 = Host(name='host3', groups=['group3','group4'], port=22)
    host4 = Host(name='host4', groups=['group4','group5'], port=22)

# Generated at 2022-06-22 12:16:32.829662
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class TestVariableManager:
        def __getstate__(self):
            return {'_data': None}
        def __setstate__(self, state):
            self.__dict__.update(state)
    class TestInventory:
        def get_host(self, name):
            pass
    class TestAnsibleLoader:
        pass
    hv = HostVars(TestInventory(), TestVariableManager(), TestAnsibleLoader())
    hv.set_variable_manager(TestVariableManager())
    if hv._variable_manager._loader is None:
        raise AssertionError("Loader is None")
    if hv._variable_manager._hostvars is None:
        raise AssertionError("Hostvars is None")

# Generated at 2022-06-22 12:16:37.306745
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    h = Host('test')
    l = DataLoader()
    v = VariableManager(loader=l)
    hv = HostVars(None, v, l)
    assert isinstance(hv[h.get_name()], dict)
    assert isinstance(hv[h.get_name()]['inventory_file'], AnsibleUndefined)


# Generated at 2022-06-22 12:16:48.006182
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    vars_cache = {
        'foo': 'bar',
        'ec2_id': {'foo': 'bar'}
    }

    inventory = MockInventory(vars_cache.keys())
    variable_manager = VariableManager(loader=None, inventory=inventory)
    variable_manager.set_vars(vars_cache)

    hostvars = HostVars(inventory, variable_manager, loader=None)
    host_name = 'localhost'

    assert hostvars.raw_get(host_name) is vars_cache

test_HostVars_raw_get()



# Generated at 2022-06-22 12:16:56.869746
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test dict_merge with 'tag_Name_mytag'
    hostvars.set_host_variable(inventory.get_host('badger'), 'tag_Name_mytag', 'this is mytag')
    assert hostvars.raw_get('badger')['tag_Name_mytag'] == 'this is mytag'

    # Test dict_merge with 'tag_mytag'

# Generated at 2022-06-22 12:17:08.368327
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    context = PlayContext()
    inventory = Inventory(loader, host_list=[])
    variable_manager = VariableManager(loader, inventory, context)
    hostvars = HostVars(inventory, variable_manager, loader)

    state = {'_inventory': inventory, '_loader': loader,
             '_variable_manager': variable_manager}
    hostvars.__setstate__(state)
    assert inventory == hostvars._inventory
    assert loader == hostvars._loader
    assert variable_manager == hostvars._variable_manager
    assert loader == hostvars._variable_manager

# Generated at 2022-06-22 12:17:15.527333
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    hostvars = HostVars({})
    assert hostvars['localhost'] == UnsafeProxy({})

    hostvars = HostVars({'localhost': {}})
    assert hostvars['localhost'] == {}

    hostvars = HostVars({'localhost': {'foo': 'bar'}})
    assert hostvars['localhost'] == {'foo': 'bar'}

# Generated at 2022-06-22 12:17:20.815514
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import copy

    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory import Inventory

    loader = Object()

    inventory = Inventory(loader=loader)
    inventory.hosts.append(Host(name='host1'))
    inventory.hosts.append(Host(name='host2'))

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.set_host_variable(inventory.get_host('host1'), 'foo', 'bar')
    variable_manager.set_host_variable(inventory.get_host('host1'), 'baz', '{{ foo }}')

    var = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-22 12:17:38.665541
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager

    # Create HostVars instance
    hostvars = HostVars(None, None, None)

    # Check that _variable_manager attribute is present (it should be)
    assert hasattr(hostvars, '_variable_manager')

    # Assign it to a local variable
    variable_manager = hostvars._variable_manager

    # Check that attribute _loader is not present (it shouldn't be)
    assert not hasattr(variable_manager, '_loader')

    # Check that attribute _hostvars is not present (it shouldn't be)
    assert not hasattr(variable_manager, '_hostvars')

    # Call method __setstate__ of HostVars

# Generated at 2022-06-22 12:17:45.089977
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.persistent_fact_manager import PersistentFactManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources="")
    variable_manager._loader = loader
    variable_manager._fact_cache = PersistentFactManager(loader=loader)

    hv = HostVars(inventory, variable_manager, loader)

    variable_manager.set_nonpersistent_facts(inventory.get_host('localhost'), dict(ansible_facts=dict(localvar='localval')))
    inventory.add_host("localhost")
    inventory

# Generated at 2022-06-22 12:17:57.085489
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.six import PY3

    # define the question to be asked
    inputs = dict(
        host_name = 'myhost1',
        hostvars = dict(
            myhost1 = dict(
                foo = 'foo',
                bar = 'bar',
            ),
            myhost2 = dict(
                foo = 'not used',
            ),
        ),
    )

    # define the expected output
    if PY3:
        # In Python 3 we'll get back a HostVarsVars object
        expected_output = dict(
            foo = 'foo',
            bar = 'bar',
        )

# Generated at 2022-06-22 12:18:09.324097
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible import errors
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    test_inventory = InventoryManager(loader=None, sources="")
    test_inventory.add_group('test_group')
    test_inventory.add_host(host=Host('test_host'), group='test_group')
    test_vars_manager = VariableManager(loader=None, inventory=test_inventory)
    test_hostvars = HostVars(test_inventory, test_vars_manager, loader=None)
    host_name = 'test_host'
    test_vars_manager.set_host_variable(host=test_hostvars._find_host(host_name), varname='test_key', value='test_value')

# Generated at 2022-06-22 12:18:18.769648
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import os
    import sys
    import ansible.plugins.loader
    import ansible.plugins.vars.hostvars
    import ansible.plugins.vars.fact_cache
    import ansible.plugins.inventory.simple_wrapper

    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible_collections.ansible.collection_mazer.plugins.vars.fact_cache import FactCache
    from ansible_collections.ansible.collection_mazer.plugins.vars.hostvars import HostVars

    base_dir = os.path.dirname(ansible.plugins.loader.__file__)

# Generated at 2022-06-22 12:18:30.229760
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    loader_mock = Mock()
    inventory_mock = Mock()
    inventory_mock.get_host.side_effect = [Mock(), Mock()]
    inventory_mock.hosts = [Mock(), Mock()]
    inventory_mock.get_host.return_value = Mock()
    inventory_mock.get_host.return_value.name = 'dummy_host'
    variable_manager_mock = Mock()
    variable_manager_mock.get_vars.return_value = {'foo': 'bar'}
    v = HostVars(inventory_mock, variable_manager_mock, loader_mock)
    assert v.__repr__() == "{'dummy_host': {'foo': 'bar'}, 'dummy_host': {'foo': 'bar'}}"

# Generated at 2022-06-22 12:18:41.135011
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play_context import PlayContext

    variables = dict(
        a = 1,
        b = dict(c = 2, d = 3)
    )

    hostvars = HostVars(object(), dict(), PlayContext())
    # VariableManager.set_host_variable() is called with argument `host`
    # which must be an instance of Host and without `host` as a keyword
    # argument, it is set to None. So, we call the method with the same
    # parameter.
    hostvars.set_host_variable(None, 'a', variables['a'])
    hostvars.set_host_variable(None, 'b', variables['b'])

    assert repr(hostvars) == repr(dict(variables))

    # When AnsibleUndefined is returned a dict

# Generated at 2022-06-22 12:18:46.136810
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible import errors

    class TestInventory(object):
        def __init__(self, vars):
            self._hosts = vars.keys()
            self._vars = vars

        def get_host(self, host_name):
            return TestHost(host_name)

    class TestHost(object):
        def __init__(self, hostname):
            self.name = hostname
            self._vars = TestInventory._vars[hostname]

    class TestVariableManager(object):
        def __init__(self):
            self._vars_caches = {}

        def get_vars(self, host=None, include_hostvars=True):
            if host is None:
                return {}
            if include_hostvars:
                return host._vars

# Generated at 2022-06-22 12:18:53.954187
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader, sources=['localhost,'])

    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader)

    # Store instance of HostVars in object
    hostvars_object = hostvars

    # Pickle and restore state of hostvars
    state = hostvars_object.__getstate__()
    hostvars.__setstate__(state)

    # Assert that pickling process did not change the state
    assert hostvars._inventory == hostvars_object._inventory
    assert hostvars._loader == hostvars_object._loader
    assert hostvars._variable_manager == hostvars_

# Generated at 2022-06-22 12:19:03.819367
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    initial_data = {
        'first_value': '{{ second_value }}',
        'second_value': '{{ third_value }}',
        'third_value': 'raw_data'
    }

    try:
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock

    from ansible.template import Templar
    from ansible.vars import VariableManager

    loader = Mock()
    inventory = Mock()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager._vars_cache['localhost'] = initial_data
    hostvars = HostVars(inventory, variable_manager, loader)

    with patch.object(Templar, 'template', return_value=initial_data):
        assert hostvars.raw_get('localhost')

# Generated at 2022-06-22 12:19:26.684531
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create a VariableManager, HostVars and a host
    v = VariableManager()
    v._loader = DictDataLoader({})
    h = HostVars(inventory=None, variable_manager=v, loader=None)
    host = Host('host', _variable_manager=v)

    # Get state of a VariableManager
    state = v.__getstate__()
    # Modify a hostvars to use a fresh VariableManager
    state['_hostvars'] = h
    # Restore the state of a VariableManager
    v.__setstate__(state)

    # Check that hostvars is set to the hostvars object and loader is set
    # to the loader from the hostvars object.
    assert v._hostvars == h
    assert v._loader == h._loader

    # Check that hostvars are set

# Generated at 2022-06-22 12:19:33.284853
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    variable_manager = VariableManager()
    variable_manager._loader = MockLoader()
    variable_manager._hostvars = None

    state = dict(variable_manager=variable_manager, inventory=None, loader=None)
    hostvars = HostVars(None, variable_manager, None)
    hostvars.__setstate__(state)

    assert hostvars._loader is None


# Generated at 2022-06-22 12:19:44.239014
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inventory = InventoryManager(loader, [])
    variable_manager = VariableManager(loader, inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars._inventory.hosts = {}
    assert repr(hostvars) == '{}'

    class SomeHost:
        pass

    host = SomeHost()
    host.name = 'testhost'
    host.vars = {'testvar': 'testval'}
    class SomeGroup:
        pass

    group = SomeGroup()
    group.hosts = [host]

# Generated at 2022-06-22 12:19:56.365118
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create temporary objects for the test
    class FakeVariableManager:
        _loader = None
        _hostvars = None

        def __setstate__(self, state):
            pass

    class FakeInventory:

        def __init__(self):
            self.hosts = dict()

        def get_host(self, name):
            return self.hosts[name] if name in self.hosts else None

    class FakeHost:
        def __init__(self, name):
            self.name = name

    class FakeLoader:
        def __init__(self, vars):
            self.vars = vars

    class FakeVarsCache:
        def __init__(self, vars):
            self.vars = vars


# Generated at 2022-06-22 12:20:06.483956
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Prepare data for test, including:
    # - Add localhost to inventory
    inventory = InventoryManager(["localhost"], None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    variable_manager.set_host_variable(inventory.hosts[0], 'ansible_hostname', 'localhost')
    variable_manager.set_host_variable(inventory.hosts[0], 'var1', 'value1')
    variable_manager.set_host_variable(inventory.hosts[0], 'var2', 'value2')

    # - Add dependent role to inventory
    deps_role = inventory.add_group('deps_role')

# Generated at 2022-06-22 12:20:13.450281
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

    hostvars = HostVars(inv_manager, variable_manager, loader)

    assert hostvars[hostvars.__getitem__.__code__.co_varnames[0]] is not None



# Generated at 2022-06-22 12:20:21.702546
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class Fake_inventory:
        def __init__(self, hostlist):
            self.hosts = hostlist

    fake_hostlist = [
        'foo.example.org',
        'bar.example.org',
        'localhost',
    ]

    fake_hv = HostVars(Fake_inventory(fake_hostlist), None, None)

    hosts = set()
    for host in fake_hv:
        hosts.add(host)

    assert hosts == set(fake_hostlist)


# Generated at 2022-06-22 12:20:27.499669
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    loader = DictDataLoader({'defaults/main.yml': '''
        dict_variable:
          - 'dict value 1'
          - 'dict value 2'
        list_variable:
          - 'list value 1'
          - 'list value 2'
        second_level_variable:
          second_level_value: 'second level'
        '''})

# Generated at 2022-06-22 12:20:38.797340
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    import ansible.constants as C

    dummy_inventory = """
[test_host]
localhost ansible_port=1234
"""

    host = 'localhost'

    test_host = Inventory(host_list=C.DEFAULT_HOST_LIST)
    test_host.add_host(host, port=1234)
    test_vm = VariableManager(loader=C.DEFAULT_LOADER, inventory=test_host)

    hostvars = HostVars(inventory=test_host, variable_manager=test_vm, loader=C.DEFAULT_LOADER)
    assert hostvars.raw_get(host) == {'ansible_port': 1234}

# Generated at 2022-06-22 12:20:43.918351
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    assert "localhost" in hostvars

# Generated at 2022-06-22 12:21:38.114509
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hosts_special_vars = HostVars(inventory, variable_manager, loader=None)

    host = "test"
    group = "group1"

    group1_vars = {'1': 1, '2': 2, '3': 3}
    host_vars = {'4': 4, '5': 5, '6': 6}

    inventory.get_group(group).set_variable("group_vars", group1_vars)
    inventory.get_host(host).set_variable("host_vars", host_vars)

    #get host vars,

# Generated at 2022-06-22 12:21:43.980917
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=loader)

    hostvars.set_host_variable(host=None, varname='test_hostvars_var', value='test_hostvars_value')

    assert repr(hostvars) == "{'localhost': {u'test_hostvars_var': u'test_hostvars_value'}}"

# Generated at 2022-06-22 12:21:56.096898
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:22:05.751826
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.vars
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars
    from ansible.template import Templar

    inventory = Inventory(DataLoader())
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = ansible.vars.HostVars(inventory, variable_manager, DataLoader())

    host = inventory.add_host('localhost')
    foo = HostVarsVars({'foo': '{{ ansible_play_hosts }}'}, DataLoader())
    templar = Templar(loader=DataLoader())

    hostvars.set_host_variable(host, 'hostvars', foo)

# Generated at 2022-06-22 12:22:17.414417
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # Setup
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    inventory.add_host(host='foo')
    inventory.set_variable(host='foo', varname='foo', value='foo')
    inventory.set_variable(host='foo', varname='bar_before', value='bar_before')
    inventory.set_variable(host='foo', varname='bar_after', value='bar_after')
    inventory.set_variable(host='foo', varname='bar_missing', value='bar_missing')

# Generated at 2022-06-22 12:22:28.803780
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    inventory = InventoryManager(loader=loader, sources=['tests/inventory/host_vars_inventory'])
    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars.raw_get('localhost') == dict()

    variable_manager.set_host_variable(inventory.get_host('test1'), 'testvar1', 'testval1')
    variable_manager.set_host_variable(inventory.get_host('test2'), 'testvar2', 'testval2')


# Generated at 2022-06-22 12:22:37.601010
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    inventory = '''
    localhost ansible_connection=local ansible_python_interpreter=python
    test1
    test2
    '''
    from ansible.inventory.script import InventoryScript
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    inventory = InventoryScript(inventory=inventory)
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    expected_repr = """{'test1': {}, 'test2': {}, 'localhost': {'ansible_connection': 'local', 'ansible_python_interpreter': 'python'}}"""
    actual_repr = repr

# Generated at 2022-06-22 12:22:46.481298
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class _FakeInventory():
        hosts = []

    class _FakeVariableManager():
        _loader = None
        _hostvars = None
        def get_vars(self, host=None, include_hostvars=False):
            return {}

        def get_vars_by_path(self, search_path, include_hostvars=False):
            return {}

        def set_host_variable(self, host, varname, value):
            pass

        def set_nonpersistent_facts(self, host, facts):
            pass

        def set_host_facts(self, host, facts):
            pass


# Generated at 2022-06-22 12:22:55.784664
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    mock_loader = object()
    mock_variable_manager = object()

    hostvars = HostVars(
        inventory=None,
        variable_manager=mock_variable_manager,
        loader=mock_loader,
    )
    hostvars.__dict__.update({
        '_inventory': None,
        '_loader': None,
        '_variable_manager': None,
    })

    hostvars.__setstate__(hostvars.__getstate__())

    assert hostvars._inventory is None
    assert hostvars._loader is mock_loader
    assert hostvars._variable_manager is mock_variable_manager

# Generated at 2022-06-22 12:23:07.178634
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,127.0.0.1'])
    variable_manager = VariableManager()

    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())


# Generated at 2022-06-22 12:24:02.146368
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import RESERVED_VARS
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    host_vars = HostVars({'some_var': 'some_value'}, loader)
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(variable_manager.get_vars(play=Play.load(dict(_hosts='localhost'), variable_manager=variable_manager, loader=loader)))
    variable_manager.add_nonpersistent_facts({'some_var': 'some_value'})
