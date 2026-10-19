

# Generated at 2022-06-22 12:14:21.090148
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import pprint
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory, Host, Group

    # Construct inventory object
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    # Construct group object
    group_name = 'group_name'
    group = Group(inventory=inventory, name=group_name)
    group.vars = dict(group_var_name='group_var_value')

    # Construct host object
    host_name = 'host_name'
    host = Host(inventory=inventory, name=host_name)
    host.vars = dict(host_var_name='host_var_value')

    # Add host to

# Generated at 2022-06-22 12:14:30.063850
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader, [])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # Non-existent host
    assert hostvars.raw_get("non-existent") == {}

    # Existent host
    assert hostvars.raw_get("localhost") == {}

    # Add host
    inventory.add_host("localhost")

    # Existent host
    assert hostvars.raw_get("localhost") == {}

# Generated at 2022-06-22 12:14:40.848065
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleUndefinedVariable

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    hostvars = HostVars(inventory, variable_manager, loader)

    # HostVars returns AnsibleUndefined if requested host is not found
    assert isinstance(hostvars['nonexistinghostname'], AnsibleUndefined)

    # HostVars returns HostVarsVars if requested host is found
    assert isinstance(hostvars['localhost'], HostVarsVars)

    # Check that HostVarsVars is immutable
    # Call setattr to avoid fail

# Generated at 2022-06-22 12:14:52.904253
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Generate a dummy inventory
    inventory_path = '/tmp/ansible_dummy_inventory'
    with open(inventory_path, 'w') as f:
        f.write('[group1]\nhost1\nhost2\n')
        f.write('[group2]\nhost3\nhost4\n')
        f.write('[group3]\nhost5\nhost6\n')

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=inventory_path)
    variable_manager = inventory.get_variable_manager()
    hostvars = HostVars(inventory, variable_manager, loader)

    # Assert method raw_get returns the same dict as

# Generated at 2022-06-22 12:15:03.179281
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader =  DataLoader()
    hosts = ["foobar"]
    inventory = Inventory(loader=loader, host_list=hosts)
    variable_manager = VariableManager(loader=loader)
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = dict(
        foo=1,
        bar="{{foo}}",
        baz="{{bar}}"
    )

    host_vars = HostVars(inventory, variable_manager, loader)

    # Test with a real host
    vars = host_vars.raw_get("foobar")
    assert vars["foo"] == 1
    assert vars["bar"] == 1
   

# Generated at 2022-06-22 12:15:14.535534
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars import VariableManager

    def _get_item_for_host(hostvars, host):
        for item in hostvars:
            if host == item:
                return item
        return False

    class DummyVariableManager(VariableManager):
        # Mock the original method for testing only the __iter__ method
        def _get_vars(self, host, new_pb_basedir):
            return None

    def _test(hostvars, hosts):
        hostvars.set_variable_manager(DummyVariableManager())
        hosts_iter = list(hostvars)

        assert len(hosts_iter) == len(hosts)
        for host in hosts:
            assert _get_item_for_

# Generated at 2022-06-22 12:15:26.208393
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    vault_secret = 'ansible'
    vault_password_file = tempfile.NamedTemporaryFile(mode='w')
    vault_password_file.write('%s\n' % vault_secret)
    vault_password_file.flush()
    vault_opts = {'vault_password_file': vault_password_file.name}
    vault_loader = DataLoader(vault_secrets=[VaultLib(**vault_opts)])
    inventory = Inventory('localhost', vault_loader=vault_loader)
    variable_manager = VariableManager

# Generated at 2022-06-22 12:15:36.249859
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class Inventory(object):
        def __init__(self, hosts):
            self.hosts = hosts

        def get_host(self, host_name):
            return self.hosts.get(host_name)

    class Host(object):
        def __init__(self, vars):
            self.vars = vars

    class VariableManager(object):
        def __init__(self, loader):
            self._loader = loader

        def get_vars(self, host, include_hostvars=True):
            return host.vars

    class Loader(object):
        def __init__(self, data):
            self.data = data

        def get_basedir(self):
            return ''

        def template(self, data, *args, **kwargs):
            return self.data


# Generated at 2022-06-22 12:15:45.693352
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader=None)

    # hosts are not registered in inventory
    assert hostvars.raw_get('foo') == AnsibleUndefined(name="hostvars['foo']")

    # hosts are registered in inventory but variables are not set
    host = inventory.add_host(name='foo')
    assert hostvars.raw_get('foo') == {}

    # hosts are registered in inventory and variables are set
    variable_manager.set_nonpersistent_facts(host, dict(foo='bar'))
    assert hostvars.raw_

# Generated at 2022-06-22 12:15:49.438111
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variables = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variables, loader)
    d = hostvars.__repr__()
    assert d == "{'localhost': {}}"

# Generated at 2022-06-22 12:16:00.616755
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import os
    import sys
    import tempfile
    import copy
    import pprint
    from ansible.utils import pycompat
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-22 12:16:11.629788
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Template

    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    orig_variable_manager = variable_manager

    state = {
        '_variable_manager': variable_manager,
        '_inventory': inventory,
        '_loader': loader
    }

    hostvars.__setstate__(state)

    assert hostvars._variable_manager == orig_variable_manager



# Generated at 2022-06-22 12:16:20.042201
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.plugins.loader import vars_loader

    class DummyInventory(object):
        def __init__(self):
            self.hosts = {'testhost': {'vars': {'testvar': 'testvalue'}}}
            self.hosts = [self.hosts['testhost']]

        def get_host(self, host_name):
            if host_name == 'testhost':
                return {'vars': {'testvar': 'testvalue'}}
            else:
                return None

    class DummyVariableManager(object):
        def __init__(self):
            self._vars_cache = dict()

        def get_vars(self, host=None, include_hostvars=True):
            return self._vars_cache


# Generated at 2022-06-22 12:16:26.777404
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    inv_manager.hosts.add_host(host='host1')
    inv_manager.hosts.add_host(host='host2')
    inv_manager.hosts.add_host(host='unreachable')
    inv_manager.hosts.set_variable('host2', 'ansible_connection', 'smart')
    inv_manager.groups.add_group(group='group1')
    inv_manager.groups.add_child(group='group1', host='host1')

# Generated at 2022-06-22 12:16:37.269681
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import variable_manager as variable_manager_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    variable_manager_loader.add_directory(variable_manager, '.')

    hostvars = HostVars(inventory=inv_manager, variable_manager=variable_manager, loader=loader)

    host = Host("localhost")
    host.set_variable("foo", "bar")

# Generated at 2022-06-22 12:16:48.821117
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars._variable_manager.set_nonpersistent_facts(inventory.get_host('fake_host'), dict(foo='bar'))
    hostvars._variable_manager.set_nonpersistent_facts(inventory.get_host('fake_host2'), dict(foo='bar2'))

# Generated at 2022-06-22 12:16:59.025331
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # The original code of __setstate__ in VariableManager does not
    # preserve _loader and _hostvars attributes, because of that
    # HostVars.__setstate__ has to re-assign them from HostVars class
    # attribute to VariableManager instance attribute.

    from ansible.vars.manager import VariableManager

    vm = VariableManager()
    hv = HostVars(None, vm, None)

    assert vm._loader is None
    assert vm._hostvars is None

    vm.__setstate__({"something": 123})
    hv.__setstate__({"_loader": 123, "_hostvars": vm, "_variable_manager": vm})

    assert vm._loader is None
    assert vm._hostvars is vm

# Generated at 2022-06-22 12:17:10.270276
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Mocking
    class Inventory(object):
        def __init__(self):
            self.hosts = {'foo': None}

        def get_host(self, host_name):
            return self.hosts.get(host_name)

    class VariableManager(object):
        def __init__(self):
            self._loader = None
            self._hostvars = None

    class Loader(object):
        pass

    class Data(object):
        def __init__(self):
            # Fake hostvars that can be used to test pickling
            self.hostvars = {'foo': {'var1': 'val1', 'var2': 'val2'}}
            self._loader = Loader()
            self._inventory = Inventory()
            self._variable_manager = VariableManager()

    # Check if host

# Generated at 2022-06-22 12:17:13.578425
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hvv = HostVarsVars({'a':1, 'b':2, 'c':3}, None)

    assert sorted(list(iter(hvv))) == sorted(['a', 'b', 'c'])

# Generated at 2022-06-22 12:17:19.852936
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.hostvars import HostVars

    vars_cache = {'localhost': {'x': 1}}

    inventory = None
    variable_manager = None
    loader = None

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars.set_variable_manager(variable_manager)
    hostvars.set_inventory(inventory)

    hostvars._vars_cache = vars_cache

    state = { '_inventory': inventory, '_loader': loader,
              '_variable_manager': variable_manager, '_vars_cache': vars_cache }

    hostvars.__setstate__(state)

    assert hostvars._vars_cache['localhost']['x'] == 1
    assert hostvars._variable_manager._loader == loader


# Generated at 2022-06-22 12:17:30.071727
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    host_vars = HostVars({}, DataLoader())
    host_vars.set_variable_manager(VariableManager(loader=DataLoader()))
    host_vars.set_inventory(Inventory(loader=DataLoader(), host_list=['test']))
    assert host_vars['test'] is not None

# Generated at 2022-06-22 12:17:34.717791
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader, [])
    variable_manager = VariableManager(loader, inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    host = inventory.get_host('localhost')
    variable_manager.set_host_variable(host, 'ansible_version', '1.2.3')

    assert hostvars['localhost']['ansible_version'] == '1.2.3'

# Generated at 2022-06-22 12:17:43.618236
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar

    loader = DataLoader()

    host = Inventory(loader=loader, variable_manager=VariableManager())

    host.add_host(host='localhost', port=22)

    temp_host = host.get_host("localhost")
    temp_host.vars['foo'] = 'bar'
    temp_host.vars['baz'] = 'qux'


# Generated at 2022-06-22 12:17:54.682217
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    data = { 'var1': 'val1', 'var2': 'val2' }
    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    hvvars = HostVarsVars(data, loader=DataLoader())

    assert(hvvars['var1'] == 'val1')
    assert(hvvars['var2'] == 'val2')

# Generated at 2022-06-22 12:18:00.195418
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader)

    hostvars = HostVars(inventory, variable_manager, loader)

    h1 = inventory.add_host("h1")
    h1.set_variable("var1", "value1")
    h1.set_variable("var2", "value2")

    variables = hostvars.raw_get("h1")
    variables_expected = {
        'var1': 'value1',
        'var2': 'value2',
    }
    assert variables == variables_expected

# Generated at 2022-06-22 12:18:12.163525
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import variable_manager, cache_loader
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars import Inventory

    vars_dict = dict(
        ansible_version='2.0.0.2', inventory_hostname='localhost', groups=dict(
            group1=dict(
                hosts=dict(
                    localhost='localhost',),
                vars=dict(
                    groupvar1='value1'),
                children=dict(
                    group2=dict(
                        hosts=dict(
                            localhost='localhost',),
                        vars=dict(
                            group2var1='value3'),
                        children=dict()))))
    )


# Generated at 2022-06-22 12:18:23.159876
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.vars.hostvars
    import collections

    # Create a collection of variables.
    vars = collections.OrderedDict()
    vars['var1'] = '{{ foo }}'
    vars['var2'] = '{{ bar }}'
    vars['var3'] = '{{ lookup("pipe", "echo baz") }}'

    # Create a HostVarsVars instance
    hostvars_vars = ansible.vars.hostvars.HostVarsVars(vars, None)

    # The instance should be equal to the expected value
    assert repr(hostvars_vars) == "{'var1': '{{ foo }}', 'var2': '{{ bar }}', 'var3': '{{ lookup(\"pipe\", \"echo baz\") }}'}"

# Generated at 2022-06-22 12:18:31.521527
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.constants import DEFAULT_HOST_LIST
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=DataLoader(), variable_manager=variable_manager, host_list=DEFAULT_HOST_LIST)

    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    assert hostvars.raw_get('localhost') is not None
    assert hostvars.raw_get('testhost') is AnsibleUndefined

    # Add a new host that does not have hostvars
    new_host = inventory.get_host('testhost')
    new_host.vars.clear()


# Generated at 2022-06-22 12:18:41.975526
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.inventory.host import Host

    import ansible.playbook.play_context
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class Inventory(object):
        def get_host(self, host_name):
            if host_name == 'localhost':
                return Host(name='localhost')
            return None

    class PlayContext(ansible.playbook.play_context.PlayContext):
        def __init__(self):
            self.special_vars = {'inventory_dir': '.'}

    def test():
        inventory = Inventory()
        variable_manager = VariableManager()
        loader = DataLoader()

        # Put some data in vars_cache
        host = inventory.get_host('localhost')
        play_context = PlayContext()


# Generated at 2022-06-22 12:18:47.312749
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''Test look up host vars

    Ensure that `HostVars.__getitem__()` returns the correct variables when
    the host has registered variables and when it does not have any.
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=[])

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    host_variables = dict(foo='bar', bar='baz')

# Generated at 2022-06-22 12:19:03.559251
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.inventory import Inventory

    inventory = Inventory(loader=None, variable_manager=None, host_list=[])
    hostvars = HostVars(inventory, variable_manager=None, loader=None)

    assert hostvars.__repr__() == '{}'

    inventory.add_host(host='host')

    data = {'foo': 'bar', 'ansible_facts': ['a', 'b', 'c']}
    hostvars.set_host_variable('host', 'vars', data)
    hostvars.set_host_variable('host', 'groups', ['group1', 'group2'])
    hostvars.set_host_variable('host', 'name', 'host')

    assert hostvars.__re

# Generated at 2022-06-22 12:19:12.921524
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    from ansible.compat.tests import unittest

    class TestHostVars(unittest.TestCase):

        def setUp(self):
            vault_password = 'secret'
            loader = DataLoader()
            vault_secrets = [('default', VaultLib([vault_password]))]

            inventory_file = 'test/unit/ansible/inventory/test_inventory.yaml'
            inventory = InventoryManager(loader=loader, sources=inventory_file)

# Generated at 2022-06-22 12:19:24.312898
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # For localhost
    assert isinstance(host_vars.raw_get('localhost'), dict)
    assert host_vars.raw_get('localhost')

# Generated at 2022-06-22 12:19:36.192948
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DummyLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    variables = {'hostvars': {'host_1': {'a': 1}, 'host_2': {'b': 2}}}
    templar = Templar(variables=variables, loader=loader)

    # Method __repr__ of HostVars calls method templar.template recursively.
    # For example, suppose that the variables contain something like
    # hostvars['host_1'], then templar.template is called with
    # fail_on_undefined=False and static_vars=STATIC_VARS, where
    # hostv

# Generated at 2022-06-22 12:19:46.161206
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Mocks
    class InventoryMock:
        def __init__(self, iterable):
            self.hosts = iterable

    class VariableManagerMock:
        def get_vars(self, host, include_hostvars):
            return self._vars[host]

    class HostMock:
        def __init__(self, hostname):
            self.name = hostname

    # Variables
    loader = None
    inventory = InventoryMock([ HostMock('host1') ])
    variable_manager = VariableManagerMock()
    variable_manager._vars = {
        'host1': { 'foo': 'bar', 'baz': 'spam' }
    }

    # Test
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars.__repr

# Generated at 2022-06-22 12:19:46.920666
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # TODO
    pass

# Generated at 2022-06-22 12:19:58.978977
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import lookup_loader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = lookup_loader.get('vars_plugins', 'variable_manager')(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars.set_host_variable('localhost', 'foo', 'bar')
    assert repr(hostvars) == "{'localhost': {'foo': 'bar'}}"

    hostvars.set_host_variable('localhost', 'hello', 'world')

# Generated at 2022-06-22 12:20:08.623058
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create the objects to be mocked for test
    inventory = Inventory(loader=None, variable_manager=None, host_list=['host1', 'host2'])
    inventory.hosts['host1'].vars = {'var1': 'a', 'var2': 'b'}
    inventory.hosts['host2'].vars = {'var1': 'c', 'var2': 'd'}
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # Test HostVars.raw_get
    hostvars = HostVars(inventory, variable_manager, loader=None)

# Generated at 2022-06-22 12:20:16.017634
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager

    state = {
        '_inventory': None,
        '_loader': None,
        '_variable_manager': VariableManager(),
    }

    hostvars = HostVars({}, {}, {})
    hostvars.__setstate__(state)
    assert hostvars._loader is None
    assert hostvars._variable_manager._loader is None
    assert hostvars._variable_manager._hostvars is hostvars

# Generated at 2022-06-22 12:20:24.603329
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager

    var_manager = VariableManager()
    var_manager.set_host_variable("localhost", "foo", "bar")
    host_vars = {'localhost': var_manager.get_vars(host=var_manager.get_host("localhost"))}
    host_vars = HostVars(None, var_manager, None)
    assert repr(host_vars) == repr(host_vars)

    host_vars = HostVars(None, var_manager, None)
    host_vars2 = HostVars(None, var_manager, None)
    assert repr(host_vars) == repr(host_vars2)

# Generated at 2022-06-22 12:21:02.773474
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import add_all_plugin_dirs

    def create_inventory():
        inventory_manager = InventoryManager(loader=None, sources=['127.0.0.1'])
        group = inventory_manager.groups['all']
        group.set_variable('gvar', dict(a='x', b=2, c=[1, 2, 3]))
        host = inventory_manager.get_host('127.0.0.1')
        host.set_variable('hvar', dict(a='x', b=2, c=[1, 2, 3]))
        return inventory_manager


# Generated at 2022-06-22 12:21:11.985978
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.vars import VariableManager

    # Prepare the mock objects
    class MockVars(MutableMapping):
        def __init__(self):
            self._data = {}

        def __getitem__(self, host):
            if not host in self._data:
                self._data[host] = AnsibleUndefined(name="vars_cache['%s']" % host)
            return self._data[host]

        def __setitem__(self, host, vars):
            self._data[host] = vars

        def __delitem__(self, host):
            del self._data[host]

        def __iter__(self):
            for host in self._data.keys():
                yield host

       

# Generated at 2022-06-22 12:21:22.577699
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    # create a loader to parse yaml
    loader = DataLoader()

    # create an inventory
    inventory = InventoryManager(loader=loader, sources='localhost,')

    # create a variable manager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create a templar for templates
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    # generate a raw hostvars
    raw_hostvars = {
        'foo': 'bar',
        'baz': 'qux',
    }

    # create a HostVarsVars
    hostv

# Generated at 2022-06-22 12:21:32.169239
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from . import mock
    from . import unittest

    from ansible import constants as C
    from ansible.errors import AnsibleUndefinedVariable

    from ansible.vars.hostvars import HostVars

    # Create a bare-bones inventory
    inventory = mock.Mock()
    host_vars = {'localvariable': 'localvalue'}
    inventory.get_host = mock.MagicMock(return_value=mock.Mock(name='localhost', vars=host_vars))

    # Create a bare-bones variable manager
    variable_manager = mock.MagicMock()

    # Create a bare-bones loader
    loader = mock.Mock()

    # Create the object being tested
    host_vars_obj = HostVars(inventory, variable_manager, loader)
    host_vars_obj

# Generated at 2022-06-22 12:21:41.792934
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    import os

    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader, sources=['test/unit/ansible/test_inventories/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)
    hostvars = HostVars(inventory_manager, variable_manager, loader)

    # test HostVars and HostVars.__iter__
    assert len(hostvars) == 5
    assert set(hostvars) == set(('host1', 'host2', 'host3', 'host4', 'host5'))

   

# Generated at 2022-06-22 12:21:54.316969
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create a mock variables manager
    class MockVariableManager(object):
        def __init__(self):
            self._loader = None
            self._hostvars = None
            self._vars_cache = {}

        def set_host_variable(self, host, varname, value):
            self._vars_cache.setdefault(host, {})[varname] = value

        def get_vars(self, host, include_hostvars=False):
            return self._vars_cache.setdefault(host, {})

    class MockAnsibleLoader(object):
        def __init__(self):
            self.path_finder = None

    class MockAnsibleInventory(object):
        def __init__(self):
            self.hosts = []


# Generated at 2022-06-22 12:22:03.815250
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

    inventory = InventoryManager(loader=None, sources=None)
    host_one = Host(name="one")
    host_two = Host(name="two")
    group_one = Group(name="one")
    group_one.add_host(host_one)
    group_two = Group(name="two")
    group_two.add_host(host_two)

    inventory.add_group(group_one)
    inventory.add_group(group_two)
    hostvars = HostVars(inventory, VariableManager(loader=None, sources=None), None)


# Generated at 2022-06-22 12:22:14.605363
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import ansible.vars.manager
    variable_manager = ansible.vars.manager.VariableManager()
    variable_manager._fact_cache
    hv = HostVars({}, variable_manager, {}, {})
    hostname = 'this_host_name'
    hv[hostname]
    # Add the host with all defaults
    hv._var_cache.setdefault(hostname, {})

    hostvars = hv[hostname]
    assert isinstance(hostvars, dict), 'Returned value is not a dict. Got %s' % type(hostvars)
    assert isinstance(hostvars, HostVarsVars), 'Expected HostVarsVars'

# Generated at 2022-06-22 12:22:23.719541
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory/hostvars'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    assert sorted(list(hostvars)) == [
            u'192.168.50.1',
            u'192.168.50.2',
            u'localhost'
    ]


# Generated at 2022-06-22 12:22:32.974645
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Test 1

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    expected = "{'localhost': {'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost'}}"
    assert repr(hostvars) == expected

    # Test 2

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory)

    host = inventory.get_host('localhost')

# Generated at 2022-06-22 12:22:59.910449
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    """HostVars: __setstate__() method

    AnsibleUnsafeLoader is not a FennecLoader descendant which is
    required for several modules and methods, but it still can be picked
    and unpicked. Since it does not have _loader nor _hostvars attributes,
    we need to check that __setstate__ assigns them properly.
    """

    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import AnsibleUnsafeLoader
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=AnsibleUnsafeLoader())
    inventory.add_group('test_group')
    inventory.add_host(host='test_host', group='test_group')

# Generated at 2022-06-22 12:23:11.740597
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    import ansible.constants as C

    class FakeLoader(object):
        pass

    inventory = InventoryManager(loader=FakeLoader())
    variable_manager = VariableManager(loader=FakeLoader(), inventory=inventory)

    localhost = Host()
    localhost.name = "localhost"
    localhost.set_variable("ansible_var_1", "foo")
    inventory.add_host(localhost)

    hostvars = HostVars(inventory, variable_manager, FakeLoader())
    localhostvars = hostvars["localhost"]
    assert localhostv

# Generated at 2022-06-22 12:23:20.821090
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory.manager import InventoryManager

    class VarManager:
        def __init__(self):
            self._vars_cache = {}
            self._loader = None
            self._hostvars = None

    inventory = InventoryManager('localhost')
    loader = None
    hostvars = HostVars(inventory, VarManager(), loader)

    # Simulate pickle
    state = hostvars.__dict__
    if '_variable_manager' in state:
        del state['_variable_manager']

    hostvars.set_variable_manager(VarManager())
    hostvars.__setstate__(state)

# Generated at 2022-06-22 12:23:29.787545
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class DummyHost:
        def __init__(self, name='host'):
            self.name = name

    class DummyInventory:
        def __init__(self):
            self.hosts = []
            self.vars = {}

        def get_host(self, host_name):
            for host in self.hosts:
                if host.name == host_name:
                    return host
            return None

    class DummyVariableManager:
        def __init__(self, variables):
            self._vars_cache = variables

        def get_vars(self, host=None, include_hostvars=True):
            return self._vars_cache

    def test_HostVars___repr__(variables, expected_repr):
        inventory = DummyInventory()

# Generated at 2022-06-22 12:23:41.858453
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    host_list = [
        'localhost',
        'foohost'
    ]
    inventory = InventoryManager(loader=loader, sources=host_list)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # Try to access raw hostvars for non-existent host
    assert hostvars.raw_get('does-not-exist') is None

    # Try to access raw hostvars for localhost
    assert hostvars.raw_get('localhost') is not None

    # Try to access raw hostvars for dummy host

# Generated at 2022-06-22 12:23:50.274340
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hostvars.set_host_variable(host='localhost', varname='foo', value='bar')
    assert hostvars.raw_get('localhost')['foo'] == 'bar'

# Generated at 2022-06-22 12:23:58.960898
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test for invalid host
    result = hostvars.raw_get("invalid_host")
    assert(isinstance(result, AnsibleUndefined))

    # Test for variable of localhost
    variable_manager.set_nonpersistent_facts(inventory.localhost, dict(test_variable=dict(test_item="test_value")))
    result = hostvars.raw_get

# Generated at 2022-06-22 12:23:59.681923
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    assert 1 == 1