

# Generated at 2022-06-22 12:14:25.334813
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    data = {
        'foo': 'bar',
        'nested': {
            'key': 'val',
            'key2': 'val2',
            'foo': 'bar',
            'nested': {
                'a': 'b',
            },
        },
        'list': ['foo', 'bar', 'baz'],
    }

    data2 = {
        'another': 'dict',
    }

    data['self'] = data

    class FakeLoader():
        pass

    loader = FakeLoader()
    templar = Templar(loader=loader)
    host_vars_vars = HostVarsVars(data, loader=loader)

    templar.set_available_variables(data2)

# Generated at 2022-06-22 12:14:27.926473
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    variables = dict(a=1, b=2)
    inventory = None
    loader = None
    variable_manager = None
    hostvars = HostVars(inventory, variable_manager, loader)
    variable_manager = variable_manager or variable_manager
    variable_manager.set_host_variable(host=None, variable='hostvars', value=variables)
    assert hostvars.raw_get(host_name=None) == variables

# Generated at 2022-06-22 12:14:38.975389
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():

    from ansible.module_utils.six import PY2
    from ansible.module_utils.common.collections import is_iterable
    from ansible.parsing.yaml.loader import AnsibleLoader

    a_short_dict = { 'a': 1, 'b': 2, 'c': 3 }

# Generated at 2022-06-22 12:14:51.233378
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = variable_manager._loader

    # Initialize inventory
    inventory = InventoryManager(loader=loader, sources=None)
    # Add group
    group1 = inventory.add_group('group1')
    # Add host
    inventory.add_host(host=group1, name="host1")
    # Set hostvars
    variable_manager.set_host_variable("host1", "var1", "val1")
    variable_manager.set_host_variable("host1", "var2", "val2")

    # Test iterating over hostvars of host1
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars_vars = hostvars

# Generated at 2022-06-22 12:15:00.962799
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Build the data structure needed to construct the HostVars object
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    # Set the value of an host variable, use the hostvars[host_name] notation
    # to trigger the cache update when necessary and then get the host variable
    # in non templated way

# Generated at 2022-06-22 12:15:09.685567
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.utils.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader)
    inventory = InventoryManager(loader, variable_manager, 'fake_hosts.yml')
    hostvars = HostVars(inventory, variable_manager, loader)

    state = hostvars.__getstate__()

    hostvars.__setstate__(state)
    assert hostvars._variable_manager._loader == loader
    assert hostvars._variable_manager._hostvars == hostvars

# Generated at 2022-06-22 12:15:15.184792
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from units.mock.loader import DictDataLoader
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    # Create a mock inventory and add a couple of hosts to it
    mock_host1 = dict(name="host1", vars=dict(foo=1))
    mock_host2 = dict(name="host2", vars=dict(foo=2))

    inventory = Inventory(loader=DictDataLoader({'host1': mock_host1, 'host2': mock_host2}))
    variable_manager = VariableManager(loader=DictDataLoader({}), host_vars=inventory._hosts)

    # Create an instance of HostVars
    hostvars = HostVars(inventory, variable_manager, loader=DictDataLoader({}))

    # Method __repr__

# Generated at 2022-06-22 12:15:26.630701
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # Prepare data
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    vm = VariableManager()
    inv = Inventory(loader=loader, variable_manager=vm)
    hostvars = HostVars(inventory=inv, variable_manager=vm, loader=loader)
    hostvars.set_host_variable(host=inv.get_host("group1"), varname="var1", value="value1")

    # Perform test
    result = hostvars.raw_get("group1")

    # Make sure we have the variable and its value
    assert result["var1"] == "value1"

    # Make sure variable got cached

# Generated at 2022-06-22 12:15:33.945441
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class FakeVariableManager():
        def __init__(self):
            self._loader = None
            self._hostvars = None

    hostvars = HostVars({}, FakeVariableManager(), None)
    hostvars._variable_manager._loader = None
    hostvars._variable_manager._hostvars = None
    hostvars.__setstate__(hostvars.__getstate__())

    assert hostvars._variable_manager._loader is not None
    assert hostvars._variable_manager._hostvars is not None

# Generated at 2022-06-22 12:15:39.632116
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    inventory.add_host(host='h1')
    hostvars = HostVars(inventory, VariableManager(), loader)

    assert [host for host in hostvars] == ['h1']

# Generated at 2022-06-22 12:15:53.912724
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    # Test data that will be used in 'HostVarsVars' object
    test_data = {
        'var1': "{{ lookup('vault', 'unsafe_password') }}",
        'var2': "{{ lookup('vault', 'unsafe_password', 'vault_password=password') }}",
        'var3': "{{ lookup('vault', 'other_password', 'vault_password=password', 'other_password') }}",
        'var4': "{{ lookup('vault', 'other_password', vault_password=password, password_file=password) }}",
    }

    # Create 'HostVarsVars' object and test expected and returned data
    obj = HostVarsVars(test_data, loader=None)
    assert obj['var1'] == test_data['var1']

# Generated at 2022-06-22 12:16:05.784000
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # We use two templar instances.
    templar_1 = Templar(loader=None)
    templar_2 = Templar(loader=None)

    # We create a HostVars instance.
    hostvars = HostVars(inventory=None, variable_manager=None, loader=None)

    # We create a dict to be returned by __getitem__.
    test_hostvars = {
        'key_1': templar_1.template('{{ foo }}'),
        'key_2': templar_2.template('{{ bar }}'),
    }

    # We set the variable manager of the HostVars instance.
    variable_manager = DummyModuleUtilsCommonCollectionsCompatVariableManager()
    variable_manager.add_host_vars(hostvars=test_hostvars)
    hostv

# Generated at 2022-06-22 12:16:17.236575
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    display = Display()
    loader = None
    variable_manager = VariableManager(loader=loader, inventory=None)
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Test lookup of host which is defined in inventory
    ret = hostvars.raw_get('localhost')
    assert ret == {'groups': {'all': ['localhost']}, 'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost'}

    # Test lookup of host which is not defined in inventory

# Generated at 2022-06-22 12:16:27.010022
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create inventory object
    inventory = InventoryManager(loader=None, sources=[])

    # Create host object
    host = Host(name='localhost')
    host.set_variable('foo', 'bar')

    # Add host to inventory object
    inventory.add_host(host)

    # Create VariableManager object
    variable_manager = VariableManager()

    # Create HostVars object
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # Test HostVars object
    for host in hostvars:
        assert host.name == 'localhost'
        assert host.get_variable('foo') == 'bar'



# Generated at 2022-06-22 12:16:37.450567
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import ansible.vars.hostvars
    import ansible.vars.variable_manager
    import ansible.plugins.loader
    import ansible.template.template
    import ansible.template.vars
    import ansible.utils.unsafe_proxy

    _loader = ansible.plugins.loader.PluginLoader(None, None, None)
    _vvars = ansible.template.vars.VariableVars(loader=_loader)
    _tmplr = ansible.template.template.Templar(_vvars, loader=_loader, shared_loader_obj=None)
    _unsafe = ansible.utils.unsafe_proxy.AnsibleUnsafeText('')

    # Save state of HostVars and VariableManager

# Generated at 2022-06-22 12:16:46.095070
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.parsing.dataloader

    loader = ansible.parsing.dataloader.DataLoader()
    inv = ansible.inventory.manager.InventoryManager(loader=loader, sources=['localhost,'])
    var_mgr = ansible.vars.manager.VariableManager(loader=loader, inventory=inv)
    hostvars = HostVars(inv, var_mgr, loader=loader)
    hostvars.raw_get('localhost')

# Generated at 2022-06-22 12:16:55.101328
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    hostvars_instance = HostVars(inventory=None,
                                 loader=DataLoader(),
                                 variable_manager=VariableManager())

    # Test whether an exception is raised when state contains the attributes
    # that are not defined in the class
    try:
        state = {'unknown_attribute': 'some_value'}
        hostvars_instance.__setstate__(state)
    except AttributeError:
        pass
    else:
        raise AssertionError("The __setstate__ method doesn't raise " \
                             "an exception when using an unknown attribute")

    # Test whether an exception is raised when

# Generated at 2022-06-22 12:17:06.912193
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create temporary VariableManager with empty state
    from ansible.vars.manager import VariableManager
    from collections import namedtuple
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader

    FakeOptions = namedtuple('FakeOptions', ['connection_plugins'])
    FakeOptions.all_vars = False
    FakeOptions.roles_path = []

    fake_loader = DataLoader()
    fake_variable_manager = VariableManager(loader=fake_loader, options=FakeOptions())

    # The method raises NoSuchHostException if VariableManager has no loader
    try:
        fake_variable_manager.set_host_variable('example', 'var', 'value')
    except AnsibleError:
        pass

    # The method raises NoSuchHostException if VariableManager has no hostvars

# Generated at 2022-06-22 12:17:16.880790
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.reserved import Reserved
    from collections import defaultdict
    from ansible.template import Templar
    import jinja2
    import sys

    if sys.version_info[0] > 2:
        unicode = str

    # Note: To make test scenarios more compcat, this test method calls
    # all the functions and methods directly rather than using mocked
    # objects. This makes it easier to test other methods of Hostvars.

    # Create variable manager and hostvars.
    variable

# Generated at 2022-06-22 12:17:29.109625
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    # Quickly create a fake inventory with two hosts
    inventory = InventoryManager(loader, sources=['localhost,127.0.0.1,'])
    inventory.hosts.append(inventory.inventory.get_host('localhost'))
    inventory.hosts.extend(inventory.inventory.add_host('127.0.0.1'))
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:17:39.307386
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Inventory

    loader = DictDataLoader({})
    inventory = Inventory(loader)
    inventory.hosts = ['localhost', 'test']

    hostvars = HostVars(inventory, loader)

    assert list(hostvars) == ['localhost', 'test']


# Generated at 2022-06-22 12:17:49.887377
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext


    hosts = '127.0.0.1,'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=hosts)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 12:17:59.110244
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars.unsafe_proxy import wrap_var
    loader = DictDataLoader({
        'templates/hostvarsvars_test.j2': '"{{ foo }},{{ bar }}",'
    })
    templar = Templar(loader=loader)
    variables = {
        'foo': 'Foo',
        'bar': 'Bar',
        'baz': 'Baz',
    }
    wrapped_variables = wrap_var(HostVarsVars(variables, loader=loader))
    for var in wrapped_variables.keys():
        assert(var in variables)



# Generated at 2022-06-22 12:18:06.706719
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from vars_plugins.host_yaml import VarsModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=None, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # Test get dict
    assert(hostvars['localhost'] == {'foo': 'bar', 'baz': 'qux'})

    # Test get undefined variable
    assert(isinstance(hostvars['nonesuch'], AnsibleUndefined))

    # Test get variable with undefined variable in its value
    variable_manager.set_host_variable(inventory.get_host('localhost'), 'undefined_var', 'value')


# Generated at 2022-06-22 12:18:15.368628
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Setup
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager('/dev/null', variable_manager=variable_manager)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Execution
    it = hostvars['localhost']
    keys = list(it.keys())

    # Assertion
    assert len(keys) == len(hostvars['localhost']), 'Both iterators must be of the same length'
    assert 'ansible_all_ipv4_addresses' in keys, 'Failed to iter hosts vars'


# Generated at 2022-06-22 12:18:20.425917
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="")
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    vars = HostVars(inventory, variable_manager, loader)

    assert { host for host in vars } == set()

# Generated at 2022-06-22 12:18:32.176106
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    variable_manager.extra_vars = {'foo': 'bar'}

    hostvars = HostVars(inventory, variable_manager, DataLoader())

    # Raw get should not follow the HostVarsVars templating engine
    assert hostvars.raw_get('localhost') == {'foo': 'bar', 'inventory_hostname': 'localhost'}

    # Raw get should not combine with the inventory host variables

# Generated at 2022-06-22 12:18:42.361511
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class FakeLoader(object):
        pass

    class FakeInventory(object):
        def __init__(self):
            class FakeHost(object):
                name = 'host1'
                vars = {'foo': 'foo', 'bar': 'bar'}
                groups = ['group1']
                def get_vars(self):
                    return self.vars

            self.fake_host = FakeHost()

        def get_host(self, hostname):
            if hostname == 'host1':
                return self.fake_host
            else:
                return None

    class FakeVariableManager(VariableManager):
        def __init__(self):
            self.hostvars = {}


# Generated at 2022-06-22 12:18:44.710717
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    This method is not intended to be used directly.

    See the following link for details:

    https://github.com/ansible/ansible/blob/v2.1.1.0-1/test/test_utils.py#L401
    '''
    pass

# Generated at 2022-06-22 12:18:53.074161
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # We do not need a real environment for this test.
    from ansible.plugins.loader import find_plugin

    loader = find_plugin(None, 'test', None)
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=loader, sources=[])
    inventory.hosts.append('1.1.1.1')
    inventory.hosts.append('2.2.2.2')
    inventory.hosts.append('3.3.3.3')
    context = PlayContext(inventory=inventory, loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory, play_context=context)

# Generated at 2022-06-22 12:19:09.038378
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # raw_get should return the same value as hostvars[hostname]
    variables = {'test': '{{ hostvars[inventory_hostname]["test"] }}'}
    inventory = InventoryManager(loader=None, sources=None)
    hostvars = HostVars(inventory, VariableManager(loader=None), None)
    host = inventory.add_host('localhost')
    hostvars.set_host_variable(host, 'test', 'ok')
    assert hostvars.raw_get('localhost')['test'] == hostvars['localhost']['test']

# Generated at 2022-06-22 12:19:15.533010
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})

    inventory = Inventory(loader, VariableManager(loader=loader), host_list='localhost,')

    hostvars = HostVars(inventory, VariableManager(loader=loader, inventory=inventory), loader)
    templar = Templar(loader=loader, variables=hostvars)

    assert templar.template("{{ hostvars['localhost']['somvar'] | default('notset') }}",
                            fail_on_undefined=False, static_vars=STATIC_VARS) == 'notset'

    hostvars.set_host_variable(inventory.get_host('localhost'), 'somvar', 'set')



# Generated at 2022-06-22 12:19:20.977252
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import collections
    import ansible.inventory
    inventory = ansible.inventory.Inventory("")
    loader = ansible.plugins.loader.PluginLoader("", "", "", None)
    variable_manager = ansible.vars.VariableManager()

    hv = HostVars(inventory, variable_manager, loader)
    assert isinstance(iter(hv), collections.Iterator)


# Generated at 2022-06-22 12:19:33.284720
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible import context

    inventory = InventoryManager(loader=DataLoader(), sources='localhost')
    variables = VariableManager(loader=DataLoader(), inventory=inventory)

    hostvars = HostVars(inventory, variables, DataLoader())

    assert hostvars['localhost'] == {}

    play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        vars = dict(
            foo = "{{ bar }}",
            bar = "baz",
        ))

# Generated at 2022-06-22 12:19:44.238537
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # No error is raised during execution, test passes
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.module_utils._text import to_bytes

    localhost = {'hostname': 'localhost'}

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost")

    group = inventory.groups.create('all')
    host = group.add_host(hostname='localhost')
    host.vars.update(localhost)
    host.set_variable('ansible_connection', 'local')

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_v

# Generated at 2022-06-22 12:19:56.365815
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import pytest
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['devhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # check for undefined host
    foo = hostvars.raw_get('bar')
    assert isinstance(foo, AnsibleUndefined)

    # check for defined host
    foo = hostvars.raw_get('devhost')
    assert isinstance(foo, dict)
    assert 'inventory_hostname' in foo
    assert foo['inventory_hostname'] == 'devhost'


# Generated at 2022-06-22 12:20:04.462044
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    # If new variables are added to self._vars, this unit test should fail
    # with error message:
    # '100 iterations reached. Probably missing self._vars[var] '
    # 'in HostVarsVars.__getitem__'
    variables = {'key': 'value'}
    host_vars_vars = HostVarsVars(variables, loader=None)
    for var in host_vars_vars:
        host_vars_vars[var]
    for var in host_vars_vars:
        host_vars_vars[var]

# Generated at 2022-06-22 12:20:12.394383
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars['localhost'] = {'var1': 'value1'}
    assert hostvars['localhost']['var1'] == 'value1'

    assert len(hostvars) == 1
    assert 'localhost' in hostvars


# Generated at 2022-06-22 12:20:19.596581
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    HostVars_obj = HostVars(None, None, None)
    HostVars_obj._find_host = host_name_mock
    HostVars_obj._variable_manager = AnsibleVars_obj
    HostVars_obj._loader = AnsibleLoader_obj

    assert HostVars_obj['host_name_mock'] == {'key1': 'value1', 'key2': 'value2'}


# Generated at 2022-06-22 12:20:26.875724
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    import ansible.plugins.loader as plugins_loader

    class DummyInventory:
        def __init__(self):
            self.hosts = []

        def get_host(self, name):
            for host in self.hosts:
                if host.name == name:
                    return host
            return None
    class DummyHost:
        def __init__(self, name):
            self.name = name
    class DummyLoader:
        def __init__(self):
            pass

    inventory = DummyInventory()
    inventory.hosts.append(DummyHost('test1'))
    inventory.hosts.append(DummyHost('test2'))


# Generated at 2022-06-22 12:20:45.080812
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars

    class FakeInventory:

        def __init__(self, hosts):
            self.hosts = hosts

    variables = dict(a=1, b=dict(c=3, d=4))
    hostvars = HostVars(FakeInventory(['host1', 'host2']), VariableManager(), None)
    assert repr(hostvars) == "{'host1': {'a': 1, 'b': {'c': 3, 'd': 4}}, 'host2': {'a': 1, 'b': {'c': 3, 'd': 4}}}"

# Generated at 2022-06-22 12:20:51.868847
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=MockLoader(), sources=['localhost'])
    hostvars = HostVars(inventory, VariableManager(loader=MockLoader()), MockLoader())

    assert len(list(hostvars.__iter__())) == 1



# Generated at 2022-06-22 12:21:01.353760
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader, [], [])
    var_manager = VariableManager(loader=loader, inventory=inv_manager)

    hostvars = HostVars(inv_manager, var_manager, loader)

    variables = {'v1': 'test', 'v2': 'test2'}
    hostvars_vars = HostVarsVars(variables, loader)

    test_arr = []
    for k in hostvars_vars:
        test_arr.append(k)

    assert sorted(test_arr) == sorted(variables.keys())

# Generated at 2022-06-22 12:21:11.431490
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import variable_manager_loader
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    def test_data(self, hostname):
        if hostname == 'good':
            return {'foo': 'bar'}
        else:
            return AnsibleUndefined(name='hostvars[%s]' % hostname)

    loader = DataLoader()
    variable_mgr = variable_manager_loader.get('vars', loader=loader)
    inventory = inventory_loader.get('host_list', loader=loader)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_mgr, loader=loader)
    hostvars._find_host

# Generated at 2022-06-22 12:21:22.081621
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    variables = {'foo': 'bar'}

    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    import ansible.vars.hostvars
    import ansible.vars.manager
    import ansible.inventory.host

    loader = DataLoader()
    inventory = Inventory(loader=loader)
    variable_manager = ansible.vars.manager.VariableManager(loader=loader, inventory=inventory)
    play = Playbook.load(loader=loader, variable_manager=variable_manager,
                         inventory=inventory,
                         host_list='localhost',
                         playbooks='tests/test_hostvars_getitem.yml',
                         variable_manager=variable_manager)
    play._tqm._stdout_callback = None

# Generated at 2022-06-22 12:21:29.012072
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=DataLoader(), sources=["tests/inventory/test_hostvars.yaml"])
    variable_manager = VariableManager(loader=DataLoader())

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    assert list(hostvars) == ['localhost', 'fakehost']


# Generated at 2022-06-22 12:21:39.318599
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-22 12:21:45.772927
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import ansible.plugins.loader as plugin_loader
    import ansible.vars.manager as var_manager
    import ansible.inventory.manager as inv_manager

    host = plugin_loader.get_plugin('inventory').get('localhost')()
    host.name = host.get_name()

    variables = var_manager.VariableManager()
    variables.set_host_variable(host, 'foo', 'bar')
    variables.set_host_variable(host, 'baz', 'qux')

    inventory = inv_manager.InventoryManager(loader=plugin_loader.get('loader'),
                                             sources=['localhost,'])
    inventory.add_host(host)

    loader = plugin_loader.get('loader')

    hostvars = HostVars(inventory, variables, loader)
    hostvarsvars = hostv

# Generated at 2022-06-22 12:21:50.449075
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader =  DataLoader()
    variables = {'username': 'admin', 'password': 'secret'}
    variable_manager.set_nonpersistent_facts(variables)

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    hostvars = HostVars(inventory, variable_manager, loader)

    host_name = 'test_host'
    result = hostvars.raw_get(host_name)

    assert 'username' in result
    assert 'password' in result
    assert 'username' not in result['test_host']

# Generated at 2022-06-22 12:21:57.164211
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    """Make sure HostVars.__repr__() works properly

    """
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = dict(all={'hosts': ['host_a', 'host_b']}, host_a={'vars': {'foo': 'bar'}})
    hv = HostVars(inventory, {}, loader)

    assert repr(hv) == "{'host_a': {'foo': 'bar'}, 'host_b': {}}"

# Generated at 2022-06-22 12:22:29.096517
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.plugins.loader as plugin_loader
    from ansible.vars.manager import VariableManager

    inventory = plugin_loader.get('InventoryModule')()
    variable_manager = VariableManager(loader=None, inventory=None)
    variable_manager._fact_cache = {
        'localhost': {'var_a': 'a', 'var_b': 'b'},
        '127.0.0.1': {'var_a': 'a', 'var_b': 'b'},
        '127.0.0.2': {'var_a': 'a', 'var_b': 'b'},
    }
    hostvars = HostVars(inventory, variable_manager, loader=None)

# Generated at 2022-06-22 12:22:33.365419
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import yaml
    yaml_text = '''
    ---
    1: test
    2: test
    3: test
    ...
    '''
    data = yaml.load(yaml_text)
    h = HostVars(data)
    repr(h)

# Generated at 2022-06-22 12:22:45.050365
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    data = dict(
        __ansible_vars=dict(
            ansible_play_hosts=['localhost'],
            ansible_play_role_names=[],
        ),
        __ansible_facts=dict(
            ansible_all_ipv4_addresses=['127.0.0.1'],
        ),
    )

    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.add_nonpersistent_facts(data)
    variable_manager.add_group_vars_file('group_vars', 'group_vars.yml')


# Generated at 2022-06-22 12:22:56.813190
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inv_path = '../../tests/inventory'
    host_vars_file = '../../tests/inventory/host_vars/a.example.org'

    inventory = InventoryManager(loader=None, sources=[inv_path])
    variable_manager = VariableManager()
    variable_manager.add_host_variable(host=inventory.hosts['a.example.org'], varname='foo', value='bar')

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    # The order of items in the list is important.
    assert sorted(hostvars) == sorted(['a.example.org'])


# Generated at 2022-06-22 12:23:07.870103
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os

    dl = DataLoader()
    this_dir, this_filename = os.path.split(__file__)
    localhost_ini = os.path.join(this_dir, '../inventory/test_inventory/hosts.ini')
    inventory = InventoryManager(loader=dl, sources=localhost_ini)
    variable_manager = VariableManager(loader=dl, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=dl)

    assert hostvars.raw_get('localhost') is not None

# Generated at 2022-06-22 12:23:19.700008
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import unittest
    import ansible.vars.manager

    # Prepare some data
    inventory = ansible.inventory.Inventory(host_list=[])
    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.manager.VariableManager(loader=loader, inventory=inventory)
    host = ansible.inventory.host.Host(name='localhost')
    variables = {'ansible_version': '2.0.0'}
    variable_manager.set_host_variable(host, "vars", variables)

    # Test __getitem__
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars_vars = hostvars['localhost']
    assert isinstance(hostvars_vars, HostVarsVars)



# Generated at 2022-06-22 12:23:20.783078
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # FIXME
    pass


# Generated at 2022-06-22 12:23:27.340420
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class DummyLoader:

        def __init__(self):
            self._data = {
                'my_var': 'some value'
            }

        def get_basedir(self, host=None):
            return "/dummy/basedir"

        def get_vars(self, load_from, vault_password=None, host=None, share_loader=False):
            return self._data, 'ansible_vars'

    loader = DummyLoader()
    hostvars = HostVars(inventory=InventoryManager(loader=loader, sources=[]),
                        variable_manager=VariableManager(loader=loader),
                        loader=loader)

    # We want to check that HostVarsVars object iterates variables
   

# Generated at 2022-06-22 12:23:39.459382
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.errors import AnsibleError
    from ansible.template import Templar

    # mock inventory
    inventory = InventoryManager(loader=DataLoader(), sources='')
    host = inventory.get_host(pattern='test_host')

    # mock play
    play = Play()

    # construct variable manager
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    variable_manager.extra_vars = {'first_var': 'first var'}

# Generated at 2022-06-22 12:23:50.478147
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create a fake instance of VariableManager
    vm = type('VariableManager', (object,), {'_loader': None, '_hostvars': None})()

    # Create vars_cache
    vars_cache = {'some_host': {'some_var': 'some_value'}}

    # Create a fake instance of HostVars
    hv = type('HostVars', (HostVars,), {'_inventory': None, '_loader': None, '_variable_manager': vm})
    hv.set_variable_manager(vm)

    # Make sure that _loader and _hostvars are not set after __setstate__
    # call
    hv.__setstate__({'_vars_cache': vars_cache})
    assert vm._loader is None
    assert vm._hostvars is None