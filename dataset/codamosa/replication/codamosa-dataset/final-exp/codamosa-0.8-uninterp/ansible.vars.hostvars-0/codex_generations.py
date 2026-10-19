

# Generated at 2022-06-22 12:14:24.158318
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.inventory import Inventory
    from ansible.template import Templar

    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    add_all_plugin_dirs()

    inventory = Inventory()
    inventory.parse_inventory_file('hosts')

    templar = Templar(loader=None)

    variable_manager = VariableManager(loader=None, inventory=None, variables=None)
    variable_manager._hostvars = HostVars(inventory, variable_manager, templar)

    host_vars = variable_manager._hostvars

    host_vars._vars = {'a': 'b'}
    host_vars._variable_manager._loader = templar

# Generated at 2022-06-22 12:14:26.811704
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars_vars = HostVarsVars({'foo': 'bar'}, None)
    for var in hostvars_vars:
        assert var == 'foo'

# Generated at 2022-06-22 12:14:36.114534
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import mock
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import MutableMapping

    # Create mock objects
    inventory_mock = mock.MagicMock()
    variable_manager_mock = mock.MagicMock()
    variable_manager_mock.get_vars.return_value = {'foo': 1}
    loader_mock = mock.MagicMock()

    # Create object
    hostvars = HostVars(inventory_mock, variable_manager_mock, loader_mock)

    # assert methods exist
    assert (hasattr(hostvars, 'raw_get') and callable(hostvars.raw_get))

    # assert Mapping

# Generated at 2022-06-22 12:14:36.904713
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    pass

# Generated at 2022-06-22 12:14:48.797776
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():

    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager(loader=None, sources=["/dev/null/hosts"])

    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager(loader=None, inventory=inventory_manager)

    from ansible.template import Templar

    templar = Templar(loader=None)

    hostvars = HostVars(inventory=inventory_manager,variable_manager=variable_manager,loader=templar)

    assert hostvars._inventory.hosts is not None

    assert hostvars._variable_manager.hostvars is not None

    assert hostvars._loader.available_variables is not None

    assert hostvars._loader.get_basedir is not None

    assert hostvars._loader.path_dwim is not None

# Generated at 2022-06-22 12:14:58.819994
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    class FakeParser:
        def get_host_vars(self, inventory, host, new_vars):
            return {'foo': 'bar'}
    loader = DataLoader()
    parser = FakeParser()
    inventory = Inventory(loader, parser, host_list='/dev/null')
    variable_manager = VariableManager(loader, inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_variable_manager(variable_manager)
    assert hostvars.__repr__() == "{'all': {'foo': 'bar'}}"

# Generated at 2022-06-22 12:15:09.667884
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    host = Host('localhost')
    data = {'test_value': 'foo'}
    host.vars = data
    vars_manager = VariableManager()
    vars_manager.set_nonpersistent_facts(host=host, facts=data)
    host_vars_data = HostVars(inventory=None,
                              variable_manager=vars_manager,
                              loader=None)

    host_vars = host_vars_data['localhost']
    host_vars_data.set_host_variable(host=host,
                                     varname='test_value',
                                     value=host_vars_data['localhost']['test_value'])

# Generated at 2022-06-22 12:15:23.041534
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager

    loader = None

    hosts = [Host('11.11.11.11'), Host('22.22.22.22'), Host('33.33.33.33')]
    hostnames = ['11.11.11.11', '22.22.22.22', '33.33.33.33']
    groups = [Group('all'), Group('ungrouped'), Group('test')]

    varman = VariableManager(loader=loader)
    varman._add_group_vars_files(loader, groups)
    varman._add_host_vars_files(loader, hosts)
    varman._set_inventory(hosts)


# Generated at 2022-06-22 12:15:33.865886
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    '''Unit test for method __iter__ of class HostVars.'''
    import ansible.vars.hostvars
    inventory = ansible.inventory.Inventory(host_list=[])
    variable_manager = ansible.vars.manager.VariableManager(loader=None, inventory=inventory)
    hostvars = ansible.vars.hostvars.HostVars(inventory, variable_manager, loader=None)

    inventory_hostname1 = ansible.inventory.host.Host(name='inventory_hostname1')
    inventory_hostname2 = ansible.inventory.host.Host(name='inventory_hostname2')
    inventory.add_group('group')
    inventory.add_host(inventory_hostname1, 'group')
    inventory.add_host(inventory_hostname2, 'group')


# Generated at 2022-06-22 12:15:37.188910
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager

    inv = InventoryManager('localhost,')
    hostvars = HostVars(inv, None, None)

    lst = sorted(hostvars)
    assert lst == ['localhost']

# Generated at 2022-06-22 12:15:51.690774
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Prepare play context and inventory
    inventory = InventoryManager()
    inventory.add_host(host='some_host')
    play_context = PlayContext()
    play_context.inventory = inventory

    # Prepare variable manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'some_var': 'some_value'}

    # Create a HostVarsVars
    some_host = inventory.get_host('some_host')
    raw_hostvars = variable_manager.get_vars(host=some_host, include_hostvars=False)
    hostvars_vars

# Generated at 2022-06-22 12:16:02.780147
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    '''
    This method tests raw_get of HostVars class. It checks
    whether raw_get returns the original data.
    '''
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host_vars = HostVars(inventory, variable_manager, loader)

    inventory.add_host("test_host")

    host_vars.set_variable_manager(variable_manager)
    host_vars.set_inventory(inventory)

# Generated at 2022-06-22 12:16:10.287132
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    v = VariableManager()
    hv = HostVars(dict(), v, DataLoader())
    hv['foo'] = 'bar'
    assert hv['foo'] == 'bar'
    assert hv['{{ foo }}'] == 'bar'
    assert hv.raw_get('foo') == 'bar'

# Generated at 2022-06-22 12:16:10.622539
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    assert True

# Generated at 2022-06-22 12:16:14.178062
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible import context
    from ansible.parsing.dataloader import DataLoader

    hv = HostVars(inventory=context.CLIARGS['inventory'], variable_manager=VariableManager(), loader=DataLoader())
    v = HostVarsVars(variables={'var1':'value1','var2':'value2'}, loader=DataLoader())
    assert (len([x for x in v]) == 2)
    assert (next(iter(v)) == 'var1')
    assert (next(iter(v)) == 'var1')
    assert (next(iter(v)) == 'var1')
    assert (v['var1'] == 'value1')

# Generated at 2022-06-22 12:16:24.074626
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # Pylint complains about missing signatures.
    # pylint: disable=no-value-for-parameter
    from ansible.inventory import Host, Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inv = Inventory(loader=DataLoader())
    inv.add_host(Host("example.com"))
    inv.add_host(Host("localhost"))
    inv.get_host("localhost").set_variable("key", "value")

    variable_manager = VariableManager()
    variable_manager.set_inventory(inv)

    variables = {"key": "value"}
    variable_manager.set_host_variable("localhost", "key", "value")
    variable_manager.set_host_variable("example.com", "key", "value")

    hostv

# Generated at 2022-06-22 12:16:34.888897
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import random

    random.seed(42)
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='/dev/null')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    hosts = ['host{0}'.format(x) for x in range(10)]
    dummy = {'foo': 'bar', 'a': 'b'}
    for h in hosts:
        host = inventory.get_host(h)
        hostvars.set_host_variable(host, 'ansible_host', host.name)
        hostv

# Generated at 2022-06-22 12:16:42.385570
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class MockerVarManager(object):
        def __init__(self):
            self._hostvars = None

    x = MockerVarManager()
    state = dict(a=1, _variable_manager=x)

    hv = HostVars(inventory=None, variable_manager=None, loader=None)
    hv.__setstate__(state)
    assert hv._variable_manager._hostvars == hv
    assert hv.a == 1
    assert hv._variable_manager is x

# Generated at 2022-06-22 12:16:50.818702
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''
    Verify method __getitem__ of class HostVars
    '''

    #
    # TEST: hostvars['host_name'] returns host variables
    #
    hv1 = HostVars({'test_host': { 'test_var': 'test_value' } }, None, None)
    assert hv1['test_host']['test_var'] == 'test_value'

    #
    # TEST: hostvars['nonexistent_host'] returns AnsibleUndefined
    #
    hv2 = HostVars({}, None, None)
    assert isinstance(hv2['nonexistent_host'], AnsibleUndefined)



# Generated at 2022-06-22 12:17:02.628831
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    import os
    #from ansible.inventory.host import Host
    #from ansible.inventory.group import Group
    #from ansible.inventory.ini import InventoryParser
    #from ansible.inventory.yaml import InventoryYAMLParser

    inventory_path = os.path.join(os.path.dirname(__file__), '../../playbooks/inventory/')
    inventory = InventoryManager(loader=DataLoader(), sources=['%s/hosts' % inventory_path])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)


# Generated at 2022-06-22 12:17:15.392581
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    expected = ['localhost',]
    actual = sorted(hostvars.__iter__())

    assert expected == actual

# Generated at 2022-06-22 12:17:22.398720
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    import collections
    import copy
    import sys

    from io import StringIO

    from ansible.compat.tests import unittest
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.compat import ipaddress
    from ansible.vars.manager import VariableManager

    # The class HostVars inherits some methods from base classes
    # collections.Mapping and ansible.module_utils.common._collections_compat.Mapping.
    # However, the method __repr__ is not inherited and implemented in class HostVars.
    # Therefore, we have to reimplement the tested method in classes
    # collections.Mapping and ansible.module_utils.common._collections_compat.Mapping
    # and mock the inherited attributes to test the method __

# Generated at 2022-06-22 12:17:33.638406
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    data = (
        ('localhost', {'foo': 'bar'}),
        ('127.0.0.1', {'foo': 'bar'}),
    )

    from ansible.playbook.hosts import Host, Inventory
    inventory = Inventory('/foo/bar')
    for (hostname, vars) in data:
        host = Host(hostname=hostname)
        inventory.add_host(host)
        hostvars = HostVars(inventory, None)
        hostvars._variable_manager = DummyVarManager(vars)

        def test_one():
            assert hostvars.raw_get(hostname) == vars

        def test_two():
            assert hostvars.raw_get(host.name) == vars

        test_one()
        test_two()

# Unit

# Generated at 2022-06-22 12:17:42.987196
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class FakeInventory(object):
        ''' A simple inventory object with localhost and one remote host in it '''

        def __init__(self):
            self.hosts = ['localhost', 'remote-host']

        def get_host(self, host):
            if host not in self.hosts:
                return None
            return FakeHost(host)

    class FakeHost(object):
        ''' A simple host object representing one host '''

        def __init__(self, host):
            self.name = host

        def get_vars(self):
            if self.name == 'localhost':
                return {'ansible_connection': 'local', 'ansible_ssh_host': '127.0.0.1'}

# Generated at 2022-06-22 12:17:55.302167
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    hostname = 'localhost'
    # no variables are defined
    assert 'test_variable' not in hostvars[hostname]
    assert 'test_variable' not in hostvars.raw_get(hostname)

    # define variables

# Generated at 2022-06-22 12:18:05.598532
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Prepare environment
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test
    hostvars_iter = iter(hostvars)
    assert next(hostvars_iter) == 'localhost'
    # StopIteration exception indicates that we have iterated whole hosts list
    next(hostvars_iter)

# Generated at 2022-06-22 12:18:14.856378
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager, HostVars
    from ansible.parsing.dataloader import DataLoader

    inventory = {
        'all': {
            'hosts': {
                'localhost': {
                    'a': 1,
                    'b': 2,
                },
                'other': {
                    'a': 2,
                    'b': 1,
                }
            }
        }
    }
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    assert repr(hostvars) == "{'localhost': {'a': 1, 'b': 2}, 'other': {'a': 2, 'b': 1}}"

# Generated at 2022-06-22 12:18:18.823515
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,'])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # test hostvars.__iter__
    d = dict.fromkeys(hostvars, None)
    assert d == {'localhost': None}

# Generated at 2022-06-22 12:18:24.808944
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager()
    inventory.add_host(Host('test_host_0'))

    variable_manager = VariableManager(loader=None)
    hostvars = HostVars(inventory, variable_manager, loader=None)
    assert repr(hostvars) == '{Host(name=test_host_0): {}}'

# Generated at 2022-06-22 12:18:27.183013
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    assert 'localhost' in HostVars(None, None, None)
    assert 'omit' in HostVars(None, None, None)['localhost']

# Generated at 2022-06-22 12:18:46.099055
# Unit test for method __getitem__ of class HostVars

# Generated at 2022-06-22 12:18:51.870207
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    expected = ['localhost']
    result = list(iter(hostvars))
    assert result == expected

# Generated at 2022-06-22 12:19:01.779181
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,') # comma is a hack for single host
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    assert(len(hostvars) == 1)
    assert(list(hostvars) == ['localhost'])
    assert(set(hostvars) == {'localhost'})


# Generated at 2022-06-22 12:19:02.629745
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    HostVars({})


# Generated at 2022-06-22 12:19:12.337028
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import get_all_plugin_loaders

    class TestMapping(Mapping):
        def __getitem__(self, key):
            raise NotImplementedError()

        def __contains__(self, key):
            raise NotImplementedError()

        def __iter__(self):
            raise NotImplementedError()

        def __len__(self):
            return 2

    class TestInventory:
        def get_host(self, hname):
            raise NotImplementedError()


# Generated at 2022-06-22 12:19:23.969025
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # inventory that does not load any vars from disk
    inv_path = ':memory:'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inv_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    host1 = "localhost"
    host2 = "localhost2"
    host_vars.set_nonpersistent_facts(host1, {})

# Generated at 2022-06-22 12:19:34.393855
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=None)
    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    host = inventory.get_host('localhost')
    variable_manager.set_host_variable(host, 'foo', 'bar')

    hostvars.set_variable_manager(variable_manager)
    hostvars.set_inventory(inventory)

    assert hostvars.raw_get('localhost')['foo'] == 'bar'

# Generated at 2022-06-22 12:19:44.693000
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import sys
    import os
    import tempfile

    old_argv = sys.argv
    sys.argv = [old_argv[0]]

    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager

    from ansible.vars import VariableManager

    from collections import namedtuple

    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import vars_loader

    sys.path.insert(0, os.path.dirname(__file__))

    cli = CLI()

    mydir = os.path.dirname(__file__)
    mydir = os.path.dirname(mydir)


# Generated at 2022-06-22 12:19:56.672731
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class Inventory(object):
        def __init__(self, hosts=None):
            if hosts is None:
                hosts = []
            self.hosts = hosts

        def __iter__(self):
            return self.hosts.__iter__()

    class Host(object):
        def __init__(self, hostname):
            self.name = hostname

        def __repr__(self):
            return '<host {}>'.format(self.name)

    class VariableManager(object):
        def __init__(self, loader=None, inventory=None, variables=None, extra_vars=None):
            self._loader = loader
            self._inventory = inventory
            self._variables = variables
            self._vars_cache = {}
            self._extra_vars = extra_vars


# Generated at 2022-06-22 12:20:03.230348
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    vars = dict(a="a", b="b", complex=dict(v="v", w="w"))
    inventory = dict(hosts=["host1", "host2"])
    vm = dict(vars_cache=dict(host1=vars, host2=vars), all_hosts=["host1", "host2"])
    loader = dict()
    hostvars = HostVars(inventory, vm, loader)
    repr(hostvars)

# Generated at 2022-06-22 12:20:31.984636
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    # Test various cases
    # AnsibleUndefined() is called in this case
    inventory = None
    variable_manager = None
    loader = None
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars['test'] is None
    assert isinstance(hostvars['test'], AnsibleUndefined)

    # If a host is found, __getitem__ returns a new HostVarsVars object
    inventory = dict()
    inventory['hosts'] = dict()
    inventory['hosts']['test'] = dict()
    variable_manager = dict()
    loader = dict()
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars['test'] == dict()
    assert isinstance(hostvars['test'], HostVarsVars)



# Generated at 2022-06-22 12:20:42.533843
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager

    # Make a mock inventory
    inventory = InventoryManager(
        loader=None, sources=[]
    )

    # Make a mock loader
    loader = None

    ## Make a mock variable manager
    #class MockVariableManager:
    #    def __init__(self):
    #        self._vars_per_host = {}
    #        self._vars_per_group = {}
    #        self._vars_per_hostgroup = {}
    #
    #    def add_group_vars(self, host=None, group=None, hostgroup=None, new_vars=None):
    #        pass
    #    def add_host_vars(self, host=None, hostvars=None, new_vars=None):
    #        pass
   

# Generated at 2022-06-22 12:20:47.481627
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory/host_vars'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # The output contains unicode characters when Jinja2 is used but no
    # unicode characters when AnsibleUndefined is used.

# Generated at 2022-06-22 12:20:59.708058
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.plugins.loader import fact_loader

    HostVars.set_inventory(Inventory(loader=None, variable_manager=VariableManager()))
    variable_manager = VariableManager()
    variable_manager.set_loader(fact_loader)
    variable_manager.set_inventory(Inventory(loader=None, variable_manager=VariableManager()))
    variable_manager.extra_vars = {}
    variable_manager.options_vars = {}
    variable_manager.options_vars['ssh_pass'] = None
    variable_manager.options_vars['become_pass'] = None
    variable_manager._fact_cache = {}
    variable_manager._host_fact_cache = {}
    HostVars.set_variable_manager

# Generated at 2022-06-22 12:21:05.409822
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    Ensure that method __repr__ of HostVars returns a dictionary
    with hostvars that are templated.
    '''

    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    inventory = Inventory(host_list=[])
    loader = False
    variable_manager = VariableManager(loader=False, inventory=inventory)
    hostvars = HostVars(loader=loader, inventory=inventory, variable_manager=variable_manager)
    assert hostvars.__repr__() == '{}'

    inventory = Inventory(host_list=['test_host1'])
    hostvars = HostVars(loader=loader, inventory=inventory, variable_manager=variable_manager)
    hostvars.set_host_variable('test_host1', 'foo', 'bar')

# Generated at 2022-06-22 12:21:12.389116
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # TODO: convert this to an actual unit test
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=["localhost,"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    variable_manager.extra_vars = {
        'foo': 'bar'
    }
    print(hostvars.raw_get('localhost'))
    assert 'foo' not in hostvars.raw_get('localhost')

# Generated at 2022-06-22 12:21:20.927666
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.utils import plugin_docs

    inventory = plugin_docs.get_example_inventory()
    variable_manager = plugin_docs.get_example_variable_manager(inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader=None)

    # check that hostvars is instantiated
    assert hostvars is not None

    # check that hostvars has three hosts
    assert len(hostvars) == 3
    # check that hostvars has the first host in its iterable
    assert next(iter(hostvars)) == 'foohost.example.org'

    # check that hostvars has the second host in its iterable
    assert next(iter(hostvars)) == 'barhost.example.org'

    # check that hostvars has the third host in its iterable
   

# Generated at 2022-06-22 12:21:30.710702
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import collections
    import datetime
    import os
    import shutil
    import sys
    import tempfile
    import unittest
    import yaml

    from ansible import constants as C
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common._collections_compat import MutableSequence, MutableMapping
    from ansible.module_utils.six import string_types
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Make sure that we can create a HostVars instance in case if
    # the constants.DEFAULT_HOST_LIST is not

# Generated at 2022-06-22 12:21:40.536873
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    hostvars = HostVars({}, variable_manager, loader)

    inventory = [
        {
            "hostname": "test1",
            "hostvars": {
                "test1_var1": "test1_value1",
                "test1_var2": "test1_value2",
            }
        },
        {
            "hostname": "test2",
            "hostvars": {
                "test2_var1": "test2_value1",
                "test2_var2": "test2_value2",
            }
        },
    ]

    for host in inventory:
        hv

# Generated at 2022-06-22 12:21:49.837920
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_host_variable('localhost', 'var', 'value')
    assert hostvars['localhost']['var'] == 'value'


# Generated at 2022-06-22 12:22:36.069323
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import collections
    import sys
    import unittest
    import yaml

    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager  # contains HostVars
    from ansible.vars.manager import VariableManager

    class MockLoader(object):
        data = {
            "host_vars/some_host.yml": "some_var: some_value",
            "group_vars/some_group.yml": "some_other_var: some_other_value",
        }

        def get_basedir(self, *args, **kwargs):
            return "."

        def path_exists(self, path):
            return path in self.data


# Generated at 2022-06-22 12:22:46.566231
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    source_data = {
        "groups": {
            "foo": { "hosts": ["host1", "host2"] },
            "bar": { "hosts": ["host3"] },
            "baz": { "hosts": [] },
            "ungrouped": { "hosts": ["host4"] }
        },
        "_meta": {
            "hostvars": {
                "host1": { "var1": "val1", "var2": "val2" },
                "host2": { "var3": "val3" },
                "host3": { "var1": "val3", "var2": "val4" },
                "host4": { "var1": "val5" }
            }
        }
    }

# Generated at 2022-06-22 12:22:55.530515
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.parsing.dataloader

    ds = ansible.parsing.dataloader.DataLoader()
    fake_variable_manager = FakeVariableManager(ds, {})
    fake_host = FakeHost('host1')
    hostvars = fake_variable_manager._hostvars
    hostvars.set_host_variable(fake_host, 'var1', 'var1_value')
    hostvars_repr = repr(hostvars)
    assert hostvars_repr == "{'host1': {'var1': 'var1_value'}}"


# Generated at 2022-06-22 12:23:07.081761
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager(["localhost,", "localhost,"], None)

    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()

    from ansible.plugins.loader import vars_loader
    loader = vars_loader.VarsModule()

    import ansible.constants
    loader.set_basedir(ansible.constants.DEFAULT_MODULE_PATH)

    hostvars = HostVars(inventory_manager, variable_manager, loader)

# Generated at 2022-06-22 12:23:18.907836
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    ''' Tests to ensure that HostVars.raw_get() works as expected '''

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-22 12:23:26.071571
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inv_manager = InventoryManager(loader=DataLoader())
    inv_manager.add_host('bogus')
    hostvars = HostVars(inventory=inv_manager,
                        variable_manager=None,
                        loader=DataLoader())
    assert hostvars.raw_get('bogus') == AnsibleUndefined(name="hostvars['bogus']")


# Test for __getitem__, __contains__, __iter__, __len__, __repr__
# This is a unit test for method HostVarsVars.__getitem__

# Generated at 2022-06-22 12:23:38.358224
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import json
    import os

    # Create a fake ansible.cfg
    cwd = os.getcwd()
    with open('ansible.cfg', 'w') as f:
        f.write('''\
[defaults]
inventory = %s/hosts
''' % cwd)

    import ansible
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_mgr = InventoryManager(loader, sources=['hosts'])
    hostvars = HostVars(inv_mgr, None, loader)

    # Extract the host names from the inventory
    inv = json.loads(ansible.inventory.host_list(inventory=inv_mgr))

# Generated at 2022-06-22 12:23:41.588468
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    new_hostvars = HostVars({'host1': 'value'})
    assert repr(new_hostvars) == "{'host1': 'value'}"



# Generated at 2022-06-22 12:23:51.593435
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    host_vars = {}
    host_vars['host1'] = { 'foo': 'bar', 'baz': { 'qaz': 'qaz' } }
    host_vars['host2'] = { 'foo': 'bar', 'baz': { 'qaz': 'qux' } }

    host_vars['host1']['var1'] = '{{ baz.qaz }}'
    host_vars['host2']['var1'] = '{{ baz.qaz }}'

    host_vars['host1']['var2'] = '{{ var1 }}'
    host_vars['host2']['var2'] = '{{ var1 }}'

   

# Generated at 2022-06-22 12:24:00.482089
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import jinja2
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_nonpersistent_facts(inventory.get_host('localhost'), {'fact': 'value'})
    hostvars.set_host_facts(inventory.get_host('localhost'), {'fact2': 'value2'})