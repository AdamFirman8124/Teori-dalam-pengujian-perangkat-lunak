

# Generated at 2022-06-22 12:14:21.029038
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():

    variables = dict(a=0, b=1)

    instance = HostVarsVars(variables, object())
    assert(isinstance(instance, Mapping))

    assert(len(variables) == len(instance))
    assert(set(variables.keys()) == set(instance))
    assert(variables == dict((key, instance[key]) for key in instance.keys()))

# Generated at 2022-06-22 12:14:30.972414
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import vault_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class Options(object):
        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = 5
            self.remote_user = 'root'
            self.private_key_file = None
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra_args = None
            self.become = False

# Generated at 2022-06-22 12:14:36.671868
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    hostvars = HostVars({}, variable_manager, loader)

    assert hostvars["foo"] is AnsibleUndefined



# Generated at 2022-06-22 12:14:48.642223
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    class Loader:
        def __init__(self, vars):
            self._vars = vars

        def get_basedir(self):
            return '.'

    class Inventory:
        def __init__(self, vars):
            self._vars = vars

        def get_host(self, hostname):
            return Host(self._vars[hostname])

    class Host:
        def __init__(self, vars):
            self._vars = vars

        def get_vars(self):
            return self._vars


# Generated at 2022-06-22 12:14:59.055053
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._loader = loader
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager))
    variable_manager.set_vault_password('password')

    hostvars = HostVars(variable_manager.get_inventory(), variable_manager, loader)

    assert "testhost1" in hostvars
    assert hostvars.raw_get("testhost1").get("ansible_host") == "foo"
    assert hostvars.get("testhost1").get("ansible_host") == "foo"

# Generated at 2022-06-22 12:15:06.256946
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    loader = None
    variables = {'var': 1}
    var_vars = HostVarsVars(variables, loader)
    assert next(iter(var_vars)) == 'var'
    variables = {'var1': 1, 'var2': 2}
    var_vars = HostVarsVars(variables, loader)
    assert sorted(iter(var_vars)) == ['var1', 'var2']

# Generated at 2022-06-22 12:15:18.910933
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    inventory = MockInventory()

    hv = HostVars(inventory, None, None)
    hv.set_variable_manager(MockVariableManager())
    hv.set_host_facts(MockHost(), {'facts': {'facts': 'facts'}})

    hv1 = pickle.loads(pickle.dumps(hv))

    assert hv._loader is not None
    assert hv._variable_manager._loader is not None
    assert hv._variable_manager._hostvars is not None
    assert hv1._loader is None
    assert hv1._variable_manager._loader is None
    assert hv1._variable_manager._hostvars is not None

    assert hv._variable_manager._host_facts == hv1._variable_manager._host_facts



# Generated at 2022-06-22 12:15:26.956598
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars_iter = list(hostvars.__iter__())
    assert len(hostvars_iter) == 1
    assert hostvars_iter[0].name == 'localhost'

# Generated at 2022-06-22 12:15:36.777917
# Unit test for method __getitem__ of class HostVars

# Generated at 2022-06-22 12:15:47.814520
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    vars1 = {'a': 'b'}
    vars2 = {'c': 'd'}

    loader = DummyLoader()
    inv = Inventory(loader=loader)
    hostvars = HostVars(inv, VariableManager(loader=loader), loader)
    inv.add_host(host='host1')
    inv.add_host(host='host2')
    hostvars.set_host_variable(inv.get_host('host1'), 'a', 'b')
    hostvars.set_host_variable(inv.get_host('host2'), 'c', 'd')

    # Get initial state of instance and create another instance to test __setstate__
    state = hostvars.__getstate__()
   

# Generated at 2022-06-22 12:15:58.983077
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    class MockInventory:

        def __init__(self):
            self.hosts = []
            self.included_file_names = []

        def __call__(self, *args, **kwargs):
            return self

        def add_group(self, *args, **kwargs):
            pass

        def get_host(self, *args, **kwargs):
            return self.hosts[0]

    class MockLoader:

        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            return self

        def path_dwim(self, *args, **kwargs):
            return "path_dwim_result"

# Generated at 2022-06-22 12:16:07.579182
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    i = Inventory(host_list=[])
    i.add_host(host='one')
    i.add_host(host='two')
    i.add_host(host='three')

    v = VariableManager()
    hv = HostVars(i, v, None)

    res = list(hv)
    assert len(res) == 3
    assert 'one' in res
    assert 'two' in res
    assert 'three' in res


# Generated at 2022-06-22 12:16:18.622997
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class FakeHost: pass
    class FakeVariableMgr:
        def __init__(self):
            self._vars_cache = {
                'host1': {'testvar': 'testval'}
            }

        def get_vars(self, host, include_hostvars=True):
            return self._vars_cache.get(host.name, AnsibleUndefined)

    class FakeInventory:
        def __init__(self):
            self._hosts_cache = { 'host1': FakeHost }

        def get_host(self, host_name):
            return self._hosts_cache.get(host_name)

    hvars = HostVars(FakeInventory(), FakeVariableMgr(), loader=None)
    assert hvars['host1']['testvar'] == 'testval'


# Generated at 2022-06-22 12:16:26.199355
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.playbook.play
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.template import Templar

    hostvars = HostVars(None, None, None)
    assert repr({}) == repr(hostvars)

    hostvars._inventory = Group(name='all')
    hostvars._inventory.hosts = {'localhost': Host(name='localhost')}
    assert repr({'localhost': {}}) == repr(hostvars)

    hostvars._variable_manager = DummyVariableManager(None)
    hostvars._variable_manager._fact_cache = {'localhost': {'ansible_lsb': {'codename': 'jessie'}}}

# Generated at 2022-06-22 12:16:33.131159
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    vars_cache = dict(a=1, b=2)

    inventory = dict(hosts=dict(host1=dict(vars=vars_cache)))

    variable_manager = dict(get_vars=lambda h, i: vars_cache)
    loader = dict()

    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars['host1'] == dict(a=1, b=2)

# Generated at 2022-06-22 12:16:44.201192
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import os
    import yaml
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/unit/inventory')
    variable_manager.set_inventory(inventory)
    host = inventory.get_host(host_name='jumper')
    variable_manager.set_host_variable(host, 'foo', 'bar')
    variable_manager.set_host_variable(host, 'nested', dict(a='b', c='d'))
    variable

# Generated at 2022-06-22 12:16:53.964250
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    inventory = Inventory(loader=DictDataLoader({'all': {'hosts': {'foo': {}, 'bar': {}}}}))
    variable_manager = VariableManager(loader=DictDataLoader({'hostvars': {'foo': {}, 'bar': {}}}))
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader=DictDataLoader())
    # Verify number of returned hosts.

# Generated at 2022-06-22 12:17:03.075220
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=[])
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars.set_host_variable('localhost', 'a', set([1]))
    print(hostvars.raw_get('localhost'))

# Generated at 2022-06-22 12:17:08.319364
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    variable_manager = VariableManager()
    variable_manager._vars_cache = {'foo': 'bar'}
    loader = DataLoader()
    inventory = AnsibleInventory(loader, variable_manager)
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars.raw_get('foo') == {'foo': 'bar'}

# Generated at 2022-06-22 12:17:16.587844
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class FakeLoader:
        def __init__(self):
            pass

    class FakeHost:
        def __init__(self):
            pass

    class FakeInventory:
        def __init__(self):
            pass

        def get_host(self, host_name):
            return FakeHost()

    hv = HostVars(FakeInventory(), None, FakeLoader())
    assert hv._loader is None
    assert hv._variable_manager._hostvars is None

    hv.__setstate__({})
    assert hv._loader == FakeLoader()
    assert hv._variable_manager._hostvars == hv

# Generated at 2022-06-22 12:17:34.026237
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory

    vars_manager = VariableManager()
    loader = DictDataLoader({})
    inventory = MockInventory(loader=loader, variable_manager=vars_manager, host_list=[])

    hostvars = HostVars(inventory, vars_manager, loader)

    fake_host = object()
    vars_manager.set_host_variable(fake_host, 'a', '1')
    vars_manager.set_host_variable(fake_host, 'b', '2')

    assert hostvars[fake_host]['a'] == '1'
    assert hostvars[fake_host]['b'] == '2'

    # Test dict-like

# Generated at 2022-06-22 12:17:42.337302
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inv_obj)
    hostvars = HostVars(inv_obj, variable_manager, loader)
    hostvars.set_host_variable("localhost", "test", 1)
    hostvars.set_host_variable("localhost", "test2", 2)
    assert hostvars.raw_get("localhost") == {"test": 1, "test2": 2}

# Generated at 2022-06-22 12:17:53.677407
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(host_list=[])
    variable_manager = VariableManager(loader=DataLoader())
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager,
                        loader=variable_manager._loader)
    localhost = inventory.get_host('localhost')
    variable_manager.set_host_variable(localhost, 'test_var', 'test_value')

    assert hostvars.raw_get('localhost')['test_var'] == 'test_value'
    assert hostvars.raw_get('some_other_host') == AnsibleUndefined()

# Generated at 2022-06-22 12:17:58.967315
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Pretend that we have a host
    class FakeHost:
        def __init__(self, my_name, my_vars):
            self.name = my_name
            self.vars = my_vars

    # Pretend that we have an inventory
    class FakeInventory:
        def __init__(self, my_hosts):
            self.hosts = my_hosts

        def get_host(self, name):
            return self.hosts.get(name, None)

    hosts = {
        'foo': FakeHost('foo', {'bar': 'baz'}),
        'bar': FakeHost('bar', {'foo': 'baz'}),
    }

    inventory = FakeInventory(hosts)

    hostvars = HostVars(inventory, None)


# Generated at 2022-06-22 12:18:11.092506
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    '''
    This test is not unit test for class HostVars, method __setstate__ but for class VariableManager,
    methods __getstate__ and __setstate__. The reason is that class HostVars holds references
    to objects that are not pickled, so they have to be restored during de-serialization process.
    '''

    import pickle
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=DataLoader())
    variable_manager = VariableManager(loader=DataLoader())
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    hostvars._variable_manager._hostvars = None

# Generated at 2022-06-22 12:18:21.851227
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    loader = DictDataLoader({'vars': {'foo': 'bar'}})
    variable_manager = VariableManager(loader=loader, inventory=None)

    hostvars1 = HostVars(inventory=None, variable_manager=variable_manager, loader=loader)
    d = {'f': 1}
    hostvars1.__setstate__(d)
    assert hostvars1.__dict__['f'] == 1

    # VariableManager of hostvars should be updated if needed
    hostvars2 = HostVars(inventory=None, variable_manager=variable_manager, loader=loader)
    hostvars2.__setstate__(d)
    assert hostvars2._variable_manager._hostvars == hostvars2
    assert hostvars2._variable_manager._loader == loader

# Unit

# Generated at 2022-06-22 12:18:29.932802
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import copy
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager._loader = None
    variable_manager._hostvars = None

    inventory = FakeInventory()
    hostvars = HostVars(inventory, variable_manager, None)

    # Save state of hostvars object to pickle
    hostvars_pickle = copy.dumps(hostvars)

    # Create new HostVars instance from pickle
    hostvars2 = HostVars(None, None, None)
    hostvars2.__setstate__(copy.loads(hostvars_pickle))

    # Assert that attributes _loader and _hostvars are set
    assert hostvars2._variable_manager._loader is None
    assert hostvars2._variable_manager._hostv

# Generated at 2022-06-22 12:18:40.993793
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')
    variable_manager.set_inventory(inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # Test with host that exists
    assert hostvars.raw_get('test_host') == {'ansible_ssh_host': '192.168.56.101', 'test_variable': 'this is a test'}
    # Test with host that does not exist
    assert hostvars

# Generated at 2022-06-22 12:18:45.326959
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Set up a mock Inventory, VariableManager and Loader
    mock_inventory = Mock()
    mock_variables = Mock()
    mock_loader = Mock()

    # When get_vars is called, return a dict of variables
    mock_variables.get_vars.return_value = {'foo': 'bar'}

    # Instantiate HostVars
    hostvars = HostVars(mock_inventory, mock_variables, mock_loader)

    # Expect that __getitem__ does not return the dict of variables directly
    # but instead a wrapper
    assert isinstance(hostvars['somehost'], HostVarsVars)



# Generated at 2022-06-22 12:18:50.400301
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    hostvars = HostVars(inventory=inventory, variable_manager=None, loader=loader)
    for host_name in hostvars:
        assert host_name in inventory.hosts


# Generated at 2022-06-22 12:19:15.206802
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    """
    HostVars should initialize properly
    """
    import datetime

    # This should be changed if the Ansible version is updated.
    ANSIBLE_VERSION = "2.7.0"


# Generated at 2022-06-22 12:19:26.177553
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import ansible.constants as C
    import ansible.vars.hostvars as HV
    import ansible.vars.manager as VM


# Generated at 2022-06-22 12:19:37.474436
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.vars import HostVarsVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    inventory = InventoryManager(loader=DataLoader(), sources=['test/ansible/inventory/hosts.yml'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, DataLoader())

    # Test hostvars.raw_get for an existing host
    assert hostvars.raw_get('server1')['inventory_hostname'] == 'server1'

    # Test hostvars.raw_get for an existing group
    assert hostvars.raw_

# Generated at 2022-06-22 12:19:46.568335
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():

    # define mock inventory
    class MockInventory:
        def __init__(self):
            self.hosts = ['foo', 'bar', 'baz']

    # define mock variable manager
    class MockVariableManager:
        def __init__(self):
            self.vars_cache = {
                'foo': {'a': 1},
                'bar': {'b': 2},
                'baz': {'c': 3},
            }

    # define mock loader
    class MockLoader:
        pass

    hostvars = HostVars(inventory=MockInventory(), variable_manager=MockVariableManager(), loader=MockLoader())
    assert set(hostvars) == set(['foo', 'bar', 'baz'])

# Generated at 2022-06-22 12:19:58.627150
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import os
    import shutil
    import tempfile
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # Create a temporary file in the temporary directory
    tmp_file = os.path.join(tmp_dir, 'hosts')
    with open(tmp_file, 'w') as tmp:
        tmp.write("""
            [test]
            localhost
            """)

    # Create an inventory manager
    inv_mgr = InventoryManager(loader=None, sources=[tmp_file])

    # Create a variable manager
    var_mgr = VariableManager(loader=None, inventory=inv_mgr)

    # Create a HostVars object

# Generated at 2022-06-22 12:20:07.786654
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import pickle

    loader = DataLoader()
    inventories = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventories)

    hostvars = HostVars(inventory=inventories, variable_manager=variable_manager, loader=loader)

    # It should be true when setstate is implemented
    hostvars_pickled = pickle.dumps(hostvars)
    hostvars_reloaded = pickle.loads(hostvars_pickled)

    assert hostvars_reloaded._loader == loader
    assert hostvars_reloaded._variable_manager._loader == loader
   

# Generated at 2022-06-22 12:20:19.145759
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Prepare mocks
    test_vars_data = { 'a': 'b' }
    test_vars_host = 'test_host'
    test_vars_host_obj = 'test_host_obj'
    test_vars_manager = 'test_vars_manager'
    test_vars_loader = 'test_vars_loader'
    variable_manager = VariableManager()
    variable_manager._vars_cache[test_vars_host] = test_vars_data
    variable_manager._hostvars = HostVars
    inventory = InventoryManager()

# Generated at 2022-06-22 12:20:26.322951
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager('./test_inventory')
    variable_manager = inventory_manager.get_variable_manager()
    hostvars = HostVars(inventory_manager.get_inventory(), variable_manager, variable_manager._loader)
    hostname = 'somehost'

    # Test that method raw_get returns correct data
    data = hostvars.raw_get(hostname)
    assert len(data) > 0
    assert 'foo' in data
    assert data['foo'] == 'bar'

    # Test that method raw_get doesn't resolve variables in returned data
    data = hostvars.raw_get(hostname)
    assert 'bar' == data['foobar']

# Generated at 2022-06-22 12:20:38.400667
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class InventoryMock(object):
        def __init__(self, **kwargs):
            self.hosts = kwargs.get('hosts', {'a': {'vars': dict(var1='val1', var2='val2')}})

        def get_host(self, hostname):
            return self.hosts.get(hostname, None)

    class VarManagerMock(object):
        def __init__(self, **kwargs):
            self.vars_cache = kwargs.get('vars_cache', dict(var2='val2'))

        def get_vars(self, host=None, include_hostvars=False):
            if host is None:
                return self.vars_cache

# Generated at 2022-06-22 12:20:46.769756
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class FakeInventory():
        def __init__(self):
            self.hosts = ['host_1', 'host_2']
    class FakeLoader():
        def __init__(self):
            pass
        def get_real_file(self, file):
            pass
        def path_dwim(self, path):
            pass
        def path_exists(self, path):
            pass
        def is_file(self, path):
            pass

    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variables = {'key_1': 'value_1', 'key_2': 'value_2'}
    variable_manager.set_nonpersistent_facts(FakeInventory.hosts[0], variables)
    variables

# Generated at 2022-06-22 12:21:08.986508
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    assert set(HostVars(
        inventory=None,
        variable_manager=None,
        loader=None
    )) == set([])


# Generated at 2022-06-22 12:21:20.542725
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    host = inventory.get_host('localhost')
    variable_manager.set_host_variable(host, 'key1', 'value1')
    variable_manager.set_host_variable(host, 'key2', 'value2')

    assert hostvars.raw_get('localhost') == {
        'key1': 'value1',
        'key2': 'value2',
    }


# Generated at 2022-06-22 12:21:30.311683
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    class Inventory:
        def __init__(self):
            self.hosts = [Host(name="localhost")]
            self.groups = []

        def get_host(self, host_name):
            if host_name == "localhost":
                return self.hosts[0]
            else:
                return None

    class Loader:
        pass

    inventory = Inventory()
    variable_manager = VariableManager()
    loader = Loader()

    hostvars = HostVars(inventory, variable_manager, loader)

    variable_manager.set_nonpersistent_facts(inventory.hosts[0], variables="test")

# Generated at 2022-06-22 12:21:36.511060
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.giveaway import Giveaway

    # Create inventory without connection
    inventory = Giveaway.get_inventory()

    # Create variable manager
    variable_manager = Giveaway.get_variable_manager(inventory)

    # Create loader
    loader = Giveaway.get_loader()

    # Create host vars view
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test method __iter__ with empty inventory
    assert list(hostvars.__iter__()) == []

# Generated at 2022-06-22 12:21:44.185439
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    class TestInventory(object):

        def __init__(self):
            self.hosts = []

        def get_host(self, host):
            return None

    class TestVariableManager(object):

        def __init__(self):
            self._vars_cache = {}

        def get_vars(self, host=None, include_hostvars=True):
            if host and host in self._vars_cache:
                return self._vars_cache[host]
            return {}

        def set_host_variable(self, host, varname, value):
            if host not in self._vars_cache:
                self._vars_cache[host] = {}
            self._vars_cache[host][varname] = value


# Generated at 2022-06-22 12:21:56.296413
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.module_utils.six import PY2

    inventory = InventoryManager(loader=None, sources=None)

    # In Ansible 2.8, inventory vars are stored in a dict, while
    # in Ansible 2.7, inventory vars are stored in a list.
    # Make the code compatible with both versions by converting
    # a dict to a list.
    if PY2:
        ivars = u"all: {'a': 'A'}"
    else:
        ivars = "all: {'a': 'A'}"
    group = inventory.add_group(u'all')

# Generated at 2022-06-22 12:22:05.984333
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import ansible.vars.hostvars
    FakeHostVars = ansible.vars.hostvars.HostVars

    class FakeTemplate(object):
        def __init__(self, data, static_vars, fail_on_undefined):
            self.data = data
            self.static_vars = static_vars
            self.fail_on_undefined = fail_on_undefined

        def __call__(self, data, fail_on_undefined=None, static_vars=None):
            if fail_on_undefined is not None:
                self.fail_on_undefined = fail_on_undefined

            if static_vars is not None:
                self.static_vars = static_vars


# Generated at 2022-06-22 12:22:17.593530
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from six import itervalues
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.inventory.manager import InventoryManager

    hosts = [
        {'name': 'host_1', 'vars': dict(foo='bar')},
        {'name': 'host_2', 'vars': dict(foo='baz')},
    ]
    inventory = InventoryManager(
        loader=None,
        sources=hosts,
    )
    variable_manager = VariableManager()

    hostvars = HostVars(inventory, variable_manager, None)

    assert "host_1" in hostvars
    assert "host_2" in hostvars

    assert "host_3" not in hostvars

# Generated at 2022-06-22 12:22:18.200562
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    assert True

# Generated at 2022-06-22 12:22:29.597527
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    vars = HostVars({'localhost': ['hello']}, None, None)
    assert dict == type(vars.raw_get('localhost'))
    assert vars.raw_get('localhost') == {'inventory_hostname': 'localhost', 'groups': {'ungrouped': ['localhost']},
                                         'omit': '__omit_place_holder__'}
    assert dict == type(vars.raw_get('localhost')['inventory_hostname'])
    assert str == type(vars.raw_get('localhost')['inventory_hostname']['value'])

# Generated at 2022-06-22 12:23:14.489401
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    hostvars = HostVars(None, variable_manager, None)

    variable_manager.set_nonpersistent_facts(None, dict(foo='bar'))
    variable_manager.set_host_variable(None, 'xyz', 'abc')
    assert hostvars.raw_get(None) == dict(ansible_facts=dict(foo='bar'), xyz='abc')

# Generated at 2022-06-22 12:23:24.588623
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # HostVars is not tested in unit tests because
    # 1. it is too complicated to be mocked
    # 2. it is immutable and therefore thoroughly tested in integration tests.
    #
    # This function aims to test __getitem__ method
    # (which is related with #2 above) in isolation
    # in order to make sure this function is not changed.

    class FakeVariables(object):
        def __getitem__(self, var):
            if var == "var1":
                return "1"
            else:
                return "2"

        def __contains__(self, var):
            return True

    loader = None
    vars_dict = {
        "var1": "{{ var1 }}",
        "var2": "{{ var2 }}",
    }
    # Expected_result:
    #   original

# Generated at 2022-06-22 12:23:36.329080
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # Create inventory
    inventory = Inventory(loader=None, variable_manager=VariableManager())
    group = inventory.add_group('test_group')
    group.add_host(inventory.get_host('test_host1'))
    group.add_host(inventory.get_host('test_host2'))

    # Create hostvars instance
    play_context = PlayContext()
    block = Block(loader=None, role=None, task_include=None, play=None, variable_manager=VariableManager())
    variable_manager = VariableManager()
   

# Generated at 2022-06-22 12:23:47.891571
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import inventory_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Init
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost")
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # Get host
    host = inventory.get_host("localhost")
    assert host is not None

    # Assign variable
    variable_manager.set_host_variable(host=host, varname="foo", value="bar")

    # Assign facts
    variable_manager.set_nonpersistent

# Generated at 2022-06-22 12:23:58.393266
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class TestInventory:
        def __init__(self):
            pass

        def get_host(self, host_name):
            return TestHost(host_name)

        @property
        def hosts(self):
            return ['foo']

    class TestHost:
        def __init__(self, name):
            self.name = name
            self.vars = {'bar': name}

        def get_name(self):
            return self.name

    loader = DataLoader()
    inventory = TestInventory()
    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:24:09.204896
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from units.compat.mock import MagicMock, patch

    # Mock objects
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    host = MagicMock()
    hostvars = MagicMock()

    # Return values for mock objects
    variable_manager.get_vars.return_value = hostvars
    inventory.get_host.return_value = host

    # Test HostVars object
    host_vars = HostVars(inventory, variable_manager, loader)

    # Compare results of method raw_get
    assert host_vars.raw_get("host_name") == hostvars
    inventory.get_host.assert_called_once_with("host_name")