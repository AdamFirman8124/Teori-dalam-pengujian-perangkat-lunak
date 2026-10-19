

# Generated at 2022-06-22 12:14:23.152213
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    i = InventoryManager(loader=None, sources="")
    i.add_host('127.0.0.1')
    v = VariableManager(loader=None, inventory=i, version_info=dict(major=2, minor=0, micro=0))

    myhvars = HostVars(i, v, lambda x: x)
    assert repr({'127.0.0.1': myhvars.get('127.0.0.1')}) == repr(myhvars)

# Generated at 2022-06-22 12:14:28.514437
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars = dict(hostVar1='hostValue1', hostVar2='hostValue2')
    hostvarsVars = HostVarsVars(hostvars, loader=None)
    assert len(hostvars) == len(hostvarsVars)
    assert sorted(hostvars) == sorted(hostvarsVars)
    assert sorted(hostvars.keys()) == sorted(hostvarsVars)

# Generated at 2022-06-22 12:14:39.620796
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible import inventory
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    # We have to create an inventory and a play for HostVars to work
    # correctly.
    inventory_manager = inventory.Manager(loader=None, sources=[])
    play_context = Play().load(dict(name="test", hosts=None, gather_facts="no"))

    # Create a host in the inventory
    host = Host(name='localhost')
    inventory_manager.add_host(host)

    # Create a variable manager on the basis of an inventory and a play
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)

    # Create HostVars object

# Generated at 2022-06-22 12:14:51.811219
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    class InventoryDummy:

        def __init__(self):
            self.vars = {'foo': 'bar'}

    class VariableManagerDummy:

        def __init__(self):
            self.vars_cache = {
                'group_1': {'group_var_1': 'group_var_1 value'},
                'group_2': {'group_var_2': 'group_var_2 value'},
                'localhost': {'localhost_var': 'localhost_var value'},
            }

    class LoaderDummy:
        pass

    inventory = InventoryDummy()
    variable_manager = VariableManagerDummy()
    loader = LoaderDummy()

# Generated at 2022-06-22 12:14:57.342931
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import sys
    import types

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class MockInventory(object):
        def __init__(self, hosts=[]):
            self.hosts = hosts

        def get_host(self, host_name):
            for host in self.hosts:
                if host.name == host_name:
                    return host
            return None

    class MockHost(object):
        def __init__(self, name):
            self.name = name

    class MockVariableManager(object):
        def __init__(self, variables=None, loader=None):
            self._vars = variables or {}
            self._loader = loader
            self._hostvars = None


# Generated at 2022-06-22 12:15:05.853586
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager())
    hostvars = HostVars(inv, VariableManager(loader, inv), loader)

    assert hostvars.raw_get('nohost-exists') is None
    assert hostvars.raw_get('nohost-exists') == hostvars.raw_get('nohost-exists')

# Generated at 2022-06-22 12:15:18.321312
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    inventory = InventoryManager(['localhost'], [C.DEFAULT_HOST_LIST])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = PlayContext(variable_manager=variable_manager)

    hostvars = HostVars(inventory, variable_manager, play_context._loader)

    def test(hostname):
        if hostname is None:
            assert hostvars._find_host(hostname) is None
            assert hostvars.raw_get(hostname) is None
            return

        host = hostvars._find_host(hostname)

# Generated at 2022-06-22 12:15:21.910942
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template.safe_eval import safe_eval

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext(variable_manager=variable_manager)

# Generated at 2022-06-22 12:15:29.534374
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Simulate object HostVars
    class HostVarMock(HostVarsVars):
        def __repr__(self):
            return repr(self._vars)

        def __setstate__(self, state):
            self.__dict__.update(state)

    class HostVarsMock(HostVars):
        def __init__(self, inventory, variable_manager, loader):
            self._inventory = inventory
            self._loader = loader
            self._variable_manager = variable_manager
            self._variable_manager._hostvars = self

        def raw_get(self, host_name):
            return {'foo': 'bar', 'baz': AnsibleUndefined()}

    inventory = None
    loader = None
    variable_manager = None

# Generated at 2022-06-22 12:15:41.023233
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    inventory = FakeInventory()
    variable_manager = FakeVariableManager(inventory)
    loader = FakeLoader()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    assert hostvars['host1'] == {'z': {'a': 'a', 'b': 'b', 'c': 'c'}}
    assert hostvars['host2'] == {'z': {'a': 'aa', 'b': 'bb', 'c': 'cc'}}
    assert hostvars['host3'] == {'z': {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}}
    assert hostvars['host4'] == {'z': {'a': 'aaaa', 'b': 'bbbb', 'c': 'cccc'}}

# Generated at 2022-06-22 12:15:51.990548
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    assert set(hostvars) == set(inventory.get_hosts())

# Generated at 2022-06-22 12:15:59.441799
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create InventoryManager and HostVars
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='/dev/null')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    variable_manager.extra_vars = {'foo': 'bar'}
    host_vars = HostVars(inv_manager, variable_manager, loader)

    # Get variables of host localhost
    raw_host_vars = host_vars.raw_get('localhost')

    # Make sure it contains the variable foo
    assert host_vars.raw_get('localhost')['foo'] == 'bar'

# Generated at 2022-06-22 12:16:06.241150
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import ansible.inventory

    # Create an empty inventory object
    i = ansible.inventory.Inventory()

    # Create instances of HostVars and Host objects
    hv = HostVars(i, None, None)
    h = ansible.inventory.Host("foo")

    # Populate the inventory
    i.add_host(h)

    # Check method __iter__ of class HostVars
    assert list(hv) == [h]

# Generated at 2022-06-22 12:16:17.561914
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible import context
    dl = DataLoader()
    host_vars = HostVars(InventoryManager(loader=dl, sources=["/dev/null"]), VariableManager(loader=dl, inventory=InventoryManager(loader=dl, sources=["/dev/null"])), dl)

    assert repr(host_vars) == "{}"

    foo = {'localhost': {'a': 1}}

# Generated at 2022-06-22 12:16:25.867504
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Setup
    import mock
    import sys
    import os
    import time
    import types
    import ansible.plugins
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    the_time = time.time()
    class new_metadata:
        def __init__(self):
            return

        @property
        def refresh_time(self):
            return the_time

    class new_host:
        def __init__(self, *args):
            return

        @property
        def vars(self):
            return { 'testvar': 42 }

        @property
        def name(self):
            return 'testhost'

    class new_group:
        def __init__(self, *args):
            return


# Generated at 2022-06-22 12:16:36.543432
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pickle
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources='localhost,'))

    inventory = variable_manager.inventory
    host = Host(name='localhost')
    inventory.add_host(host)
    group = Group(name='foo')
    inventory.add_group(group)
    inventory.add_child('foo', host)

    play_context = PlayContext()

    hostvars = HostVars

# Generated at 2022-06-22 12:16:40.412953
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():

    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    h = HostVars(Inventory(), VariableManager(), None)
    state = {
        "_loader": None,
        "_variable_manager": None,
        "_inventory": None
    }
    new_state = h.__setstate__(state)
    assert "_loader" not in new_state
    assert "_hostvars" not in new_state["_variable_manager"].__dict__

# Generated at 2022-06-22 12:16:50.750520
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible import constants as C

    hv = HostVars(loader=None, inventory=None, variable_manager=VariableManager(loader=None, inventory=None))
    hv._variable_manager._loader = C.DEFAULT_LOADER_NAME
    hv._variable_manager._hostvars = True

    hv_state = hv.__getstate__()
    hv_new = HostVars(loader=None, inventory=None, variable_manager=VariableManager(loader=None, inventory=None))
    hv_new.__setstate__(hv_state)

    assert hv_new._variable_manager._loader == C.DEFAULT_LOADER_NAME
    assert hv_new

# Generated at 2022-06-22 12:17:02.527979
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class Fake_VariableManager(object):
        def __init__(self, inventory):
            self._inventory = inventory

        def __setstate__(self, state):
            self.__dict__.update(state)

    class Fake_Inventory(object):
        def __init__(self, loader):
            self._loader = loader

        def get_host(self, host_name):
            if host_name in self._loader.get_basedir().listdir():
                return host_name
            return None

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = Fake_Inventory(loader)
    variable_manager = Fake_VariableManager(inventory)


# Generated at 2022-06-22 12:17:13.406584
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Generating sample inventory
    hosts = ["host1", "host2", "host3", "host4", "host5"]
    groups = [
        {"name": "test_group_01", "hosts": ["host1", "host2", "host3"]},
        {"name": "test_group_02", "hosts": ["host3", "host4", "host5"]},
        {"name": "test_group_03", "hosts": ["host1", "host2", "host5"]},
        {"name": "test_group_04", "hosts": []}
    ]

    loader = DataLoader()

# Generated at 2022-06-22 12:17:32.495842
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    host1 = 'host1'
    host2 = 'host2'

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,{0},'.format(host2)])

    # prepare hostvars
    extra_vars = {'ansible_version': {'major': 2, 'minor': 0, 'revision': 0, 'string': '2.0.0'}}
    variables = VariableManager(loader=loader, inventory=inventory)
    variables.extra_vars = extra_vars

    hostvars = HostV

# Generated at 2022-06-22 12:17:42.181500
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from io import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    inventory = Inventory(loader, StringIO(u'localhost'))
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 12:17:54.451123
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager

    inventory = DummyInventory()
    variable_manager = create_variable_manager(inventory)

    hostvars = HostVars(inventory, variable_manager, None)

    # Create localhost
    hostvars.raw_get('localhost')
    host = inventory.get_host('localhost')
    assert host is not None

    # Add two files for localhost:
    # * group_vars/all.yml
    # * group_vars/group_1/all.yml
    add_file_to_inventory(host, 'group_vars/all.yml',
                          content='var_all_raw: var_all_raw_value')

# Generated at 2022-06-22 12:18:02.603402
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None
    variable_manager = VariableManager()

    inventory = InventoryManager(loader=loader, sources=[])
    host = inventory.add_host('localhost')

    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=variable_manager)

    hostvars.set_host_variable(host, 'a', 1)
    hostvars.set_host_variable(host, 'b', 2)

    repr(hostvars)

# Generated at 2022-06-22 12:18:09.439099
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    hostvars = HostVars(Host(), InventoryManager(None, {}), VariableManager())
    assert hasattr(hostvars, '__iter__')
    assert hasattr(hostvars, '__getitem__')
    assert hasattr(hostvars, '__contains__')

# Generated at 2022-06-22 12:18:16.183568
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars['localhost']['inventory_hostname'] == 'localhost'
    assert len(hostvars) == 1
    assert 'localhost' in hostvars

# Generated at 2022-06-22 12:18:26.497591
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Initialize inventory
    inventory = FakeInventory(hosts=['host01', 'host02'])

    # Initialize variable manager and set variable to ensure
    # variable manager has the variable.
    variable_manager = FakeVariableManager()
    variable_manager.set_host_variable(inventory.get_host('host01'), 'foo', 'bar')

    host_vars = HostVars(inventory, variable_manager, FakeLoader())
    assert repr(host_vars) == "{'host01': {'foo': 'bar'}, 'host02': {}}"

    # Initialize variable manager and set variable to ensure
    # variable manager has the variable.
    variable_manager = FakeVariableManager()

# Generated at 2022-06-22 12:18:33.956762
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, "localhost")

    hostvars = HostVars(inventory, variable_manager, loader)
    assert repr(hostvars) == "HostVars({'localhost': None})"

# Generated at 2022-06-22 12:18:43.338802
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    import os.path
    import tempfile
    import textwrap

    test_host = "testhost.example.com"
    test_path = tempfile.mkdtemp()

    host_vars_file = os.path.join(test_path, "host_vars")
    host_vars_data = textwrap.dedent('''\
    ---
    foo: host_var_foo
    bar: host_var_bar
    ''')
    with open(host_vars_file, "w") as f:
        f.write(host_vars_data)


# Generated at 2022-06-22 12:18:48.391568
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    inventory = InventoryManager(host_list=[])


    hosts = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    assert len(hosts) == 0
    assert list(hosts) == []

    inventory.hosts.append("host")
    assert len(hosts) == 1
    assert list(hosts) == ["host"]

    inventory.hosts.append("host2")
    assert len(hosts) == 2
    assert list(hosts) == ["host", "host2"]

    inventory.clear_pattern_cache()
    assert len(hosts) == 2
    assert list(hosts) == ["host", "host2"]


# Generated at 2022-06-22 12:19:04.762863
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager

    class MockInventory():
        def __init__(self):
            self.hosts = []

        def get_host(self, host_name):
            for host in self.hosts:
                if host.name == host_name:
                    return host
            return None

    # HostVars class is immutable so it is necessary to have
    # some class that will be used as a holder of set_host_variable
    # method.
    class MockHost():
        def __init__(self, name):
            self.name = name

    class MockInventoryPlugin():
        def get_variables(self, host, include_hostvars=False):
            return {}

    inventory = MockInventory()
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-22 12:19:13.074937
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    class MockLoader:
        def get_basedir(self):
            return '/'

    class MockVariableManager:
        def get_vars(self, host, include_hostvars):
            return {u'a': u'b', u'c': u'd'}

    inv = Inventory(loader=MockLoader())
    var_mgr = VariableManager(loader=MockLoader())
    hostvars = HostVars(inventory=inv, variable_manager=var_mgr, loader=MockLoader())

    hostvars_var = hostvars[u'non_existent_host']
    assert isinstance(hostvars_var, HostVarsVars)

# Generated at 2022-06-22 12:19:24.351779
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import copy
    import json
    import unittest
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    class TestInventory(InventoryManager):
        host = None

        def __init__(self):
            self.host = InventoryManager.Host(name='localhost')

        def hosts(self):
            return [self.host]

    class TestVars(dict):
        pass

    class TestHostVars(HostVars):
        def __getitem__(self, key):
            return dict()

    class TestPlay(Play):
        hosts = None

        def __init__(self, hosts):
            self.hosts = hosts


# Generated at 2022-06-22 12:19:36.236760
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import ansible.inventory.manager

    class VariableManager(object):
        def __init__(self):
            self._vars_cache = {}
            self._nonpersistent_facts_cache = {}

        def add_host_vars(self, host, hostvars):
            self._vars_cache[host.name] = hostvars

    class Inventory(object):
        def __init__(self):
            self._hosts_cache = {}

        def get_host(self, host_name):
            if host_name not in self._hosts_cache:
                host = ansible.inventory.host.Host(host_name)
                host.vars = {}
                host.groups = []
                self._hosts_cache[host_name] = host
            return self._hosts_cache[host_name]



# Generated at 2022-06-22 12:19:39.615019
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    h = HostVars({'a':1, 'b':2, 'c':3})
    assert list(dict(h)) == list(h)


# Generated at 2022-06-22 12:19:47.951871
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import ansible.playbook.play_context
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    data = {
        'inventory': '''
            localhost ansible_connection=local
        ''',
        'group_vars/all': '''
            ---
            ungrouped:
              - 42
              - 43
        '''
    }
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=data['inventory'])
    inventory.subset(None)
    variable_manager = VariableManager()

# Generated at 2022-06-22 12:19:59.937069
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost'])

    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    host_name = 'test_host'
    ansible_var = 'test_var'

    host = inventory.get_host(host_name)
    host_vars._variable_manager.set_host_variable(host, ansible_var, 'test_value')

    raw_vars = host_vars.raw_get('test_host')

# Generated at 2022-06-22 12:20:09.662533
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    host = inventory.add_host('example.org')
    host.set_variable('foo', 'bar')
    hostvars.set_host_variable(host, 'spam', 'eggs')

    assert hostvars.raw_get('example.org')['foo'] == 'bar'
    assert hostvars.raw_get('example.org')['spam'] == 'eggs'

    assert hostvars['example.org']['foo'] == 'bar'

# Generated at 2022-06-22 12:20:21.737638
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class MockVariableManager:
        def __init__(self):
            self._hostvars = None
            self._loader = None

        def set_host_variable(self, host, varname, value):
            pass

        def set_nonpersistent_facts(self, host, facts):
            pass

        def set_host_facts(self, host, facts):
            pass

    class MockLoader():
        pass

    hostvars = HostVars(None, None, None)
    hostvars._loader = MockLoader()
    hostvars._variable_manager = MockVariableManager()

    # The following values are the defaults at the end of method __setstate__
    pickled_dict = dict(
        _inventory = None,
        _loader = hostvars._loader,
        _variable_manager = MockVariableManager(),
    )

# Generated at 2022-06-22 12:20:27.515513
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    """
    _check_vars() function is being used to verify the fact that variable
    expansion is being skipped in the HostVars' raw_get() method.
    """
    class MockInventoryUnicode:
        def __init__(self):
            self.unicode_var = u'\u2014'

        def get_host(self, name):
            if name == 'jumper':
                return self
            elif name == 'localhost':
                return MockInventoryHost()

    def _check_vars(hostvars, host, name):
        host_vars_dict = hostvars.raw_get(host)
        if name in host_vars_dict:
            assert host_vars_dict[name] is not None
            assert host_vars_dict[name] != ''

# Generated at 2022-06-22 12:20:59.708596
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    mock_inventory = InventoryManager(loader=loader, sources='')
    mock_inventory.hosts = ['1', '2', '3']
    mock_inventory.groups = ['a']
    mock_inventory._hosts_cache = {
        '1': {'vars': {'foo': 'bar'}, 'groups': ['a']},
        '2': {'vars': {'foo': 'bar'}, 'groups': []},
        '3': {'vars': {'foo': 'bar'}, 'groups': []},
    }

# Generated at 2022-06-22 12:21:08.990567
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Use example of HostVars.__setstate__
    mock_dict = {
        '_vars': {},
        '_inventory': None,
        '_loader': None,
        '_variable_manager': object(),
    }

    hostvars = HostVars(None, None, None)
    hostvars.__setstate__(mock_dict)
    assert hostvars._loader is None
    assert hostvars._variable_manager._loader is None
    assert hostvars._variable_manager._hostvars is None
    assert hostvars._variable_manager._loader is None
    assert hostvars._variable_manager._hostvars is None

# Generated at 2022-06-22 12:21:12.532699
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.hostvars import HostVars
    hv = HostVars(None, None)
    assert hv.raw_get('localhost') is None

# Generated at 2022-06-22 12:21:21.072144
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # create test inventory
    from ansible.inventory import Inventory
    inventory = Inventory()
    inventory.add_host(host='localhost', port=2222)

    # create test variable manager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager._loader = loader
    variable_manager.set_inventory(inventory)

    # create test HostVars object
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-22 12:21:31.499163
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import unittest
    import sys

    class HostVarsTestCase(unittest.TestCase):
        def setUp(self):
            self.vars_data = {
                'name1': {
                    'var1': '{{name1_var1}}',
                    'var2': '{{name1_var2}}',
                },
                'name2': {
                    'var1': '{{name2_var1}}',
                    'var2': '{{name2_var2}}',
                },
            }
            self.vars = HostVars(inventory=None, variable_manager=None, loader=None)
            _inventory_hosts = {}
            for host_name in self.vars_data.keys():
                _host = type('host', (object,), {})()

# Generated at 2022-06-22 12:21:41.022642
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    import os

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, host_vars={'localhost': {'local_var': 'ok'}})
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager,
                                 host_list=['localhost'])
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    templar = Templar(loader=loader, variables=hostvars['localhost'])
    assert templar.template("{{ local_var }}", convert_bare=True) == 'ok'

# Generated at 2022-06-22 12:21:53.530674
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible import constants as C

    class FakeInventory():
        def __init__(self):
            self.hosts = ['testhost']

        def get_host(self, hostname):
            host = FakeHost()
            host.name = hostname
            return host


# Generated at 2022-06-22 12:22:03.162256
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import pytest

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.plugins.loader import vars_loader

    def _create_variable_manager_and_host(hostname, variables):
        from ansible.vars.manager import VariableManager
        from ansible.vars.hostvars import HostVars
        from ansible.vars.hostvars import HostVarsVars

        inventory = DummyInventory(hostname)
        variable_manager = VariableManager(loader=vars_loader, inventory=inventory)
        hostvars = HostVars(inventory, variable_manager, vars_loader)

        host = inventory.get_host(hostname)
        hostvars.set_host_variable(host, 'myvar', variables)

        return hostvars


# Generated at 2022-06-22 12:22:15.107578
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import copy
    import pickle
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    class FakeHost(object):
        def __init__(self, name):
            self.name = name

    class FakeInventory(Inventory):
        def __init__(self, *args, **kwargs):
            super(FakeInventory, self).__init__(*args, **kwargs)
            self.hosts = [FakeHost('localhost'), FakeHost('remotehost')]

    class FakeVariableManager(VariableManager):
        def __init__(self, *args, **kwargs):
            super(FakeVariableManager, self).__init__(*args, **kwargs)

# Generated at 2022-06-22 12:22:17.234277
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    assert(u"""{'all': {'children': ['ungrouped']}}""" == HostVars(None, None, None).__repr__())

# Generated at 2022-06-22 12:23:08.761002
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    inv_data = '''
    [test_host]
    localhost

    [test_host:vars]
    ansible_host=127.0.0.1
    '''
    inv_manager = InventoryManager()
    inv_manager.load_inventory_from_data(inv_data)

    vars_manager = VariableManager()

    vars = HostVars(inv_manager, vars_manager, loader=None)
    vars.set_variable_manager(vars_manager)

    # Raw_get is returning a dict with hostvars and vars
    assert vars.raw_get('localhost')['ansible_host'] == '127.0.0.1'

# Generated at 2022-06-22 12:23:20.472683
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # A set of hosts that can be used to test hostvars
    hosts = ["host1", "host2", "host3"]
    # A set of hostvars that can be used to test setting hostvars in
    # VariableManager._hostvars
    hostvars = {
        "host1": {"foo": "bar"},
        "host2": {"bar": "foo"},
        "host3": {"baz": "faz"}
    }

    # First, create an inventory with a set of hosts.
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)

# Generated at 2022-06-22 12:23:26.241457
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import ansible.inventory
    inventory = ansible.inventory.Inventory("")
    inventory.set_variable("host01", "var01", "val01")

    import ansible.vars
    variable_manager = ansible.vars.VariableManager()
    variable_manager.set_inventory(inventory)

    import ansible.template
    loader = ansible.template.AnsibleTemplate()

    hostvars = HostVars(inventory, variable_manager, loader)
    assert set(hostvars) == set(inventory.hosts)
    assert set(hostvars.keys()) == set(inventory.hosts)

# Generated at 2022-06-22 12:23:37.741843
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import copy

    from units.mock.loader import DictDataLoader

    test_inv = dict(hostvars=dict(host1=dict(var1=1, var2=2)))
    loader = DictDataLoader(test_inv)
    variable_manager = VariableManager(loader=loader)
    hostvars = HostVars(inventory=variable_manager.inventory,
                        variable_manager=variable_manager,
                        loader=loader)

    assert set(hostvars) == set(['host1'])

    # make sure it works with a deepcopy
    deep_hostvars = copy.deepcopy(hostvars)
    assert set(deep_hostvars) == set(['host1'])


# Generated at 2022-06-22 12:23:48.961625
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(loader=DataLoader()), host_list=[])
    from ansible.vars import HostVars
    hostvars = HostVars(inventory=inventory, variable_manager=inventory.get_variable_manager(), loader=DataLoader())

    assert hostvars.__repr__() == "{}"

    inventory.set_variable('group', 'a', 'b')
    inventory.set_variable('group', 'c', {'a': 'b'})
    inventory.set_variable('group', 'd', '{{ lookup("template", "test.tpl") }}')

# Generated at 2022-06-22 12:23:57.992259
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    hosts = [
        Host(name='default', port=22),
        Host(name='other', port=222)
    ]
    variables = {
        'foo': 'bar',
        'baz': ['a', 'b', 'c'],
        'unsafe': AnsibleUnsafeText('<script>alert("I am unsafe")</script>')
    }
    manager = VariableManager()
    manager.set_inventory(inventory=None)
    manager.set_loader(load=DataLoader())
    manager

# Generated at 2022-06-22 12:24:04.987414
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.utils.vars import combine_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager._vars = {'foo': 'bar'}

    hostvars = HostVars(None, variable_manager, None)
    assert hostvars._loader is None
    assert variable_manager._loader is None
    assert variable_manager._hostvars is hostvars
    assert variable_manager._vars == {'foo': 'bar'}

    state = {'_inventory': None, '_loader': 'loader', '_variable_manager': variable_manager}
    hostvars.__setstate__(state)

    assert hostvars._loader == 'loader'
    assert variable_manager._