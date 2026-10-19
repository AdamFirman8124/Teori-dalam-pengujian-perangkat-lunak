

# Generated at 2022-06-22 12:14:24.956971
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    host_vars = HostVars(InventoryManager(loader=None, sources=[u'']), None, None)

    assert host_vars._inventory.get_host(u'localhost') is None
    assert u'localhost' in host_vars
    assert host_vars._inventory.get_host(u'localhost') is not None

    assert u'localhost' in host_vars
    assert u'server1' not in host_vars

    host_vars._inventory.add_host(host=u'server1', group=u'group1')
    assert u'server1' in host_vars
    assert u'group1' in host_vars[u'server1']

# Generated at 2022-06-22 12:14:29.699954
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.hostvars import HostVars

    loader = None
    variable_manager = None
    inventory = None

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars.set_variable_manager(variable_manager)
    hostvars.set_inventory(inventory)
    hostvars.__setstate__(dict())

    return

# Generated at 2022-06-22 12:14:40.677185
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible import context
    from ansible.vars import VariableManager

    # Test that an exception is not raised if _loader and _hostvars are None
    # because they are assigned to _variable_manager attributes.
    loader = context.CLIARGS._get_loader(variable_manager=VariableManager())
    inventory = loader.inventory
    variable_manager = VariableManager(loader=loader)

    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.__setstate__(hostvars.__getstate__())

    # Test that no exception is raised if _loader and _hostvars are not None
    # because their values are the same with ones that are assigned.
    variable_manager = VariableManager(loader=loader)
    variable_manager._hostvars = hostvars
    variable_manager._loader

# Generated at 2022-06-22 12:14:46.084523
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    loader = DictDataLoader({})
    variables = dict(foo='bar', bar='baz')
    hostvars_vars = HostVarsVars(variables, loader)
    assert hostvars_vars['foo'] == 'bar'
    assert hostvars_vars['bar'] == 'baz'


# Generated at 2022-06-22 12:14:49.305664
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    assert repr({'localhost': {'foo': 'bar'}}) == repr(HostVars({'foo': 'bar'},
                                                               'localhost'))

# Generated at 2022-06-22 12:14:58.818631
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    hostvars = HostVars(None, None, None)

    # We need to get rid of _loader and _hostvars attributes to simulate state
    # of VariableManager as returned by method __getstate__
    del hostvars._variable_manager._loader
    del hostvars._variable_manager._hostvars

    try:
        hostvars._variable_manager.get_vars()
    except AttributeError:
        pass
    else:
        raise AssertionError('Expected failure.')

    hostvars.__setstate__({})

    try:
        hostvars._variable_manager.get_vars()
    except AttributeError:
        raise AssertionError('Unexpected failure.')

# Generated at 2022-06-22 12:15:09.668685
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultSecret
    vault_secret = VaultSecret('secret')

    hostvars = HostVars(inventory=Inventory(loader=DataLoader(), variable_manager=VariableManager(loader=DataLoader(), inventory=Inventory(loader=DataLoader()))),
                        variable_manager=VariableManager(loader=DataLoader(), inventory=Inventory(loader=DataLoader())),
                        loader=DataLoader())

    assert isinstance(hostvars, Mapping)
    for k in hostvars:
        assert isinstance(k, str)
        assert '.' not in k
        assert '_' not in k

# Generated at 2022-06-22 12:15:23.040644
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    class TestHost(object):
        def __init__(self, name):
            self.name = name
    class TestInventory(object):
        def __init__(self):
            pass
        def get_host(self, name):
            return TestHost(name)
    class TestVariableManager(object):
        def __init__(self):
            pass
        def get_vars(self, host, include_hostvars=True):
            return {'foo':'bar'}
    class TestLoader(object):
        def __init__(self):
            pass
    hv = HostVars(inventory=TestInventory(), variable_manager=TestVariableManager(), loader=TestLoader())
    assert hv.raw_get('localhost') == {'foo':'bar'}
    assert hv.raw_get('anotherhost')

# Generated at 2022-06-22 12:15:33.865167
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager, HostVarsVars, HostVars
    import ansible.parsing.dataloader
    import io

    loader = ansible.parsing.dataloader.DataLoader()

    # The following unit test is based on the assumption that all
    # serialization/deserialization of data is to/from string.
    # To make the test more stable, we pick the shortest possible string
    # to represent None in the pickle module.
    pickled_none = 'c__builtin__\nNone\np0\n.'
    assert pickle.loads(pickled_none) is None

    # We expect __setstate__ will set all attributes required for HostVars
    # to be initialized and working. To achieve that, we pass None to the
    # method, which will cause an Att

# Generated at 2022-06-22 12:15:43.718832
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    class MockVariableManager:
        def get_vars(self, host=None, include_hostvars=False):
            return self._variables

        def set_host_variable(self, host, varname, value):
            self._variables[varname] = value

    class MockInventory:
        def __init__(self):
            self.hosts = ['localhost']

        def get_host(self, host_name):
            if host_name in self.hosts:
                return host_name
            return None

    class MockLoader:
        pass

    vm = MockVariableManager()
    vm._variables = {'foo': 'bar'}
    inventory = MockInventory()
    loader = MockLoader()

    hv = HostVars(inventory, vm, loader)

# Generated at 2022-06-22 12:15:56.669917
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''
    Calling HostVars.__getitem__ should:
    - call HostVars.raw_get(host_name)
    - use the returned value to create a HostVarsVars instance
    '''
    hostvars = HostVars()

    def callee_raw_get(host_name):
        return 'the vars of %s' % host_name

    def callee_HostVarsVars(vars):
        return '[templated -- %s]' % vars

    hostvars.raw_get = callee_raw_get
    hostvars.HostVarsVars = callee_HostVarsVars

    result = hostvars['somehost']

    assert result == '[templated -- the vars of somehost]'

# Generated at 2022-06-22 12:16:08.454094
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # Ensure that the "magic" method __iter__ works...
    hostvars_variables = hostvars.get('localhost')

# Generated at 2022-06-22 12:16:17.982390
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # Use simple dictionary as an inventory with hosts 'a', 'b' and 'c'
    inventory = {'a':1, 'b':2, 'c':3}
    # The return value of __iter__ will be iterated over, so make it
    # equivalent to the set of hosts.
    class TestVariableManager:
        def get_vars(self, host, include_hostvars):
            return {}

    # Create HostVars object with the created inventory
    hostvars = HostVars(inventory, TestVariableManager(), None)
    # The set of keys in a dictionary is equal to the set of its hosts
    assert set(key for key in hostvars) == set(inventory.keys())

# Generated at 2022-06-22 12:16:25.935448
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible import constants
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    vars_1 = dict(
        a=dict(b=1),
        c=dict(d=list([dict(e=2), dict(e=3)])),
        x=1,
        y=list([2, 3]),
        z=list([dict(a=1), dict(a=2)])
    )

    # Test GetItem after it was exposed to the environment
    def test_getitem_expose(variables, var):
        variables.update(vars_1)
        loader = DataLoader()

        # Test if we can retrieve the variable from the variable store
        variables['_ansible_vars'].get(var=var)
        # Test

# Generated at 2022-06-22 12:16:36.575639
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    import ansible.playbook
    import ansible.inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host_vars = {}
    # Set hostvars for hosta and hostb
    for host in ('hosta', 'hostb'):
        variables = {'ansible_version': {'full': '2.0.0.0'},
                     'group_names': ['all'],
                     'groups': {'all': ['hostb', 'hosta']}}
        variable_manager = VariableManager()
        variable_manager.extra_vars = {'hostvars': host_vars}

# Generated at 2022-06-22 12:16:41.347844
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    inventory = "localhost ansible_ssh_host=127.0.0.1 ansible_connection=local"
    loader = DictDataLoader({None: inventory})
    variable_manager = VariableManager(loader=loader)
    variable_manager._vars_cache = {"localhost": {"a": "old"}}
    variable_manager.set_host_variable("localhost", "a", "new")

    hostvars = HostVars(loader.get_inventory("localhost"), variable_manager, loader)

    assert hostvars["localhost"]['a'] == "new"
    assert hostvars.raw_get("localhost")['a'] == "old"

# Generated at 2022-06-22 12:16:51.629425
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')
    hostvars = HostVars(inventory, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-22 12:17:03.432166
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    import copy
    import sys
    import types

    from ansible import constants as C

    from ansible.errors import AnsibleError
    from ansible.plugins.loader import vars_loader
    from ansible.utils.vars import combine_vars

    from units.mock.loader import DictDataLoader
    from units.mock.vault import vault_secrets

    def _cycle_deepcopy(obj):
        return copy.deepcopy(copy.deepcopy(obj))

    variable_manager = vars_loader.VariableManager()


# Generated at 2022-06-22 12:17:11.287687
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play_context import PlayContext

    class MockInventory:

        def __init__(self):
            self.hosts = ['foo', 'bar']

        def get_host(self, host_name):
            return host_name

    mock_inventory = MockInventory()
    mock_context = PlayContext()
    mock_loader = 'mock_loader'
    hv = HostVars(mock_inventory, mock_context, mock_loader)
    assert hv.__repr__() == "{'foo': {}, 'bar': {}}"

# Generated at 2022-06-22 12:17:17.007321
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager('localhost,')
    variable_manager = VariableManager(loader=None)
    loader = None
    hostvars = HostVars(inventory, variable_manager, loader)
    output = hostvars.__repr__()
    assert output == "{'localhost': {}}"



# Generated at 2022-06-22 12:17:30.190702
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    class TestLoader(object):
        def get_basedir(self):
            return '.'
    test_hostvar_vars = HostVarsVars({'var1': '{{basevar}}', 'basevar':'basevar'}, TestLoader())
    assert 'var1' in test_hostvar_vars
    assert 'basevar' in test_hostvar_vars


# Generated at 2022-06-22 12:17:40.329305
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    variables = dict(var1='value1', var2=dict(var21='value21', var22='value22'))

    loader_mock = mock.Mock()
    templar_mock = mock.Mock()
    loader_mock.get_basedir.return_value = ''
    templar_mock.template.side_effect = lambda x, fail_on_undefined=None, static_vars=None, **kwargs: x
    loader_mock.load_plugin_filters = lambda x: x

    hostvarsvars = HostVarsVars(variables, loader=loader_mock)

    # Test with just plain value
    assert hostvarsvars['var1'] == 'value1'

    # Test with nested dict
    assert hostvarsvars['var2'] == dict

# Generated at 2022-06-22 12:17:51.523701
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    class TestLoader:
        def __init__(self):
            self._basedir = '.'

        def get_basedir(self):
            return self._basedir

    loader = TestLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])

    hostvars = HostVars(inventory, variable_manager, loader)

# Generated at 2022-06-22 12:17:55.647593
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    # Create a new HostVarsVars instance
    hvv_instance = HostVarsVars({'a': '[1, 2, 3]', 'b': '2'}, None)
    assert hvv_instance.__iter__() == ['a', 'b']

# Generated at 2022-06-22 12:18:07.858833
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager

    _inventory = "inventory"
    _loader = "loader"
    _variable_manager = VariableManager()
    _variable_manager._loader = None
    _variable_manager._hostvars = None

    host_vars = HostVars(_inventory, _variable_manager, _loader)
    assert host_vars._loader == _loader
    assert host_vars._variable_manager._hostvars == host_vars

    new_state = {"_inventory": "new_inventory",
                 "_loader": "new_loader",
                 "_variable_manager": {"_loader": None, "_hostvars": None}}

    host_vars.__setstate__(new_state)

    assert host_vars._loader == "new_loader"
    assert host_vars._variable_manager._

# Generated at 2022-06-22 12:18:16.120917
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible import inventory
    from ansible import utils
    from ansible.utils import plugin_docs

    class Variable(dict):
        ''' Variable class that implements getter and setter. '''
        def __getitem__(self, k):
            return dict.get(self, k)

        def __setitem__(self, k, v):
            dict.__setitem__(self, k, v)

    class FakeVariableManager(object):
        ''' Fake manager that handles variables. '''
        def __init__(self):
            self._variables = Variable()

        def get_vars(self, host=None, include_hostvars=True):
            return self._variables

        def set_host_facts(self, host, facts):
            pass


# Generated at 2022-06-22 12:18:25.271531
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_loader(loader)

    hostvars = HostVars({}, variable_manager, loader)

    hostvars.set_host_variable('some_host', 'key1', 'value1')

    assert hostvars.raw_get('some_host')['key1'] == 'value1'
    assert hostvars['some_host']['key1'] == 'value1'
    assert hostvars['some_host']['key1'] == 'value1'


# Generated at 2022-06-22 12:18:37.518474
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible import inventory
    from ansible import variables
    from ansible.errors import AnsibleUndefinedVariable
    from ansible import constants as C
    C.HOST_KEY_CHECKING = False

    i = inventory.Inventory("/dev/null")
    i.set_variable('foo', 'foo')
    i.set_variable('bar', 'bar')

    h = i.get_host("localhost")

    # set some facts
    h.set_variable('ansible_ssh_host', '127.0.0.1')
    h.set_variable('ansible_ssh_port', 22)
    h.set_variable('ansible_ssh_user', 'root')
    h.set_variable('ansible_ssh_pass', 'password')


# Generated at 2022-06-22 12:18:40.893562
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager()

    hostvars = HostVars(inventory, variable_manager, loader)

    # get hostvars
    hostvars_vars = hostvars['localhost']

    # create test object
    hostvars_vars_test = HostVarsVars(hostvars_vars, loader)

    # test __iter__ method
    assert len(list(iter(hostvars_vars_test))) == len(hostvars_vars)

# Generated at 2022-06-22 12:18:43.304526
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # no host in inventory, __getitem__() should return undefined
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.variable_manager import VariableManager
    inventory = InventoryManager('')
    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader=None)
    hostvars.raw_get('foobar')

# Generated at 2022-06-22 12:18:54.488250
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class _Inventory:
        def __init__(self):
            self.hosts = ['host1', 'host2']

        def get_host(self, host_name):
            if host_name in self.hosts:
                return _Host(host_name)
            else:
                return None

        def pop_host(self, host_name):
            if host_name in self.hosts:
                self.hosts.remove(host_name)

        def add_host(self, host_name):
            self.hosts.append(host_name)


    class _Host:
        def __init__(self, host_name):
            self.name = host_name
            self.groups = []

    class _VariableManager:
        def __init__(self, loader):
            self._loader = loader



# Generated at 2022-06-22 12:19:01.981341
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from .inventory import Inventory
    from .variable_manager import VariableManager

    hostvars = HostVars(Inventory(), VariableManager())
    state = hostvars.__getstate__()
    state['_loader'] = 'test'
    state['_variable_manager']['_hostvars'] = 'test'
    hostvars.__setstate__(state)

    assert hostvars._loader == 'test'
    assert hostvars._variable_manager._hostvars == 'test'

# Generated at 2022-06-22 12:19:11.914798
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,'])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory=inventory, loader=None, variable_manager=variable_manager)

    assert 'localhost' in hostvars
    assert 'localhost' in hostvars
    assert hostvars['localhost'] == HostVarsVars(hostvars['localhost'], loader=None)
    assert hostvars['localhost']['inventory_file'] == u'(u\'\', u\'\')'
    assert hostvars['localhost']['inventory_dir'] == u'(u\'\', u\'\')'



# Generated at 2022-06-22 12:19:23.471542
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()

    # Fix issue when some variables are in Jinja2 format but not in JSON
    # For example:
    # 'ansible_all_ipv4_addresses': [u'10.0.2.15'] -> 'ansible_all_ipv4_addresses': ["10.0.2.15"]
    hostvars = loader.load_from_file('tests/unit/vars/hostvars.json')
    templar = Templar(loader=loader)

# Generated at 2022-06-22 12:19:31.428461
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.raw_get('localhost')

# Generated at 2022-06-22 12:19:40.464859
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,', 'somehost,'])
    host1, host2 = inventory.get_hosts()
    context = PlayContext()
    context.inventory = inventory
    context.vars_cache = {}

    variable_manager = VariableManager(loader=loader, inventory=inventory, playcontext=context)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hostvars_iter = hostvars.__iter__()

# Generated at 2022-06-22 12:19:52.307597
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    import yaml

    data = yaml.load("""
test1: [
  { item: some_value }
]
test2:
- item: some_value
- item:
- item:       some_value3
test3:
- { item: some_value }
- { item: some_value2 }
test4:
- { item: some_value, nested: { x: some_value } }
test5:
- item: some_value
- item:
- nested: [
  { x: some_value }
]
    """)

    loader = None

    def fail_on_undefined(v):
        return '{{%s}}' % v

    hostvars = HostVarsVars(data, loader)
    templar = Templar(loader=loader)

# Generated at 2022-06-22 12:20:03.956001
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    test_inventory = "localhost ansible_connection=local"
    loader = DictDataLoader({"/etc/ansible/hosts": test_inventory}, variable_manager=VariableManager())
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=loader.get_hosts())
    inventory._hosts_cache = {
        "localhost": Host('localhost', variable_manager=None),
    }
    inventory._vars_per_host = {
        "localhost": {
            "ansible_connection": "local",
            "foo": "bar",
        }
    }
    variable_manager = inventory.get_variable_manager()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # There should be initial values in _loader and _hostvars

# Generated at 2022-06-22 12:20:13.847555
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from collections import namedtuple
    from ansible.inventory import Inventory

    FakeGroup = namedtuple('FakeGroup', ['name', 'vars'])
    FakeHost = namedtuple('FakeHost', ['name', 'vars'])

    # Create base HostVars
    inv = Inventory()
    inv.groups.add_group(FakeGroup('group1', {'g1': 'group1var', 'g2': 'group2var'}))
    inv.hosts.add_host(FakeHost('host1', {'h1': 'host1var', 'h2': 'host2var'}))
    variable_manager = FakeVariableManager()
    variable_manager.set_inventory(inv)
    hostvars = HostVars(inventory=inv, variable_manager=variable_manager, loader=None)

    # Add fake host

# Generated at 2022-06-22 12:20:24.605456
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible import constants as C
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars

    # Create the objects we use
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 12:20:41.555434
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['localhost,'])
    hv = HostVars(inventory, None, loader)
    assert repr(hv) == "{'localhost': {}}"

# Generated at 2022-06-22 12:20:52.354631
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))
    hostvars = HostVars(inventory, VariableManager(loader=loader), loader=loader)

    # Test 1: checking if hostvars['localhost'] returns a HostVarsVars instance
    test1 = hostvars['localhost']
    assert isinstance(test1, HostVarsVars)
    assert test1 == {}
    assert test1.__getstate__() == {}

    # Test 2: checking if hostvars[foo] returns a HostVarsVars instance
    #         when no host named foo exists in the inventory

# Generated at 2022-06-22 12:21:01.943372
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    class Inventory:
        def __init__(self):
            self.hosts = ['host1', 'host2']

        def get_host(self, host_name):
            return self.hosts.index(host_name) + 1

    class VariableManager:
        def __init__(self, variables):
            self._vars = variables
            self._hostvars = None

        def get_vars(self, host, include_hostvars=False):
            if isinstance(host, int) and host > 0:
                return {'host': host}
            return AnsibleUndefined()

        def __contains__(self, host_name):
            return (str(host_name) in self._vars)


# Generated at 2022-06-22 12:21:11.838977
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # inventory is required to make HostVars not to raise an error
    inv_data = """
inventory_hostname=foo
all_host_vars_=foo
all_host_vars_2=bar
local_host_vars_=foo
"""
    inventory = InventoryManager(loader=None, sources=inv_data)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # __getitem__ does not raise an error for host existing in inventory
    assert hostvars['foo'] == hostvars['foo']

    # __getitem__ does not raise an error for host not existing in inventory
    assert hostvars['bar']

# Generated at 2022-06-22 12:21:15.315721
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Test hostvars[hostname] value of type Undefined
    hostvars = HostVars({'localhost':{}, '192.168.1.1':{}}, {}, {})
    assert hostvars['192.168.2.2'] == AnsibleUndefined(name="hostvars['192.168.2.2']")

# Generated at 2022-06-22 12:21:24.897501
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    my_loader = DataLoader()
    my_inv = InventoryManager(loader=my_loader, sources=['localhost,'])
    my_variables = {
        'one': {
            'two': {
                'three': 'value'
            }
        }
    }
    my_host = my_loader.load_from_data(my_variables)
    my_inv.hosts = [my_host]

    # Note: hostvars[hostname] should be equal to hostvars.get(hostname)
    #       however hostvars.get(hostname) is not directly accessible
    #       in template (Jinja2) because it is available via
    #       variables._hostvars

# Generated at 2022-06-22 12:21:33.355204
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    This function has been added to allow full test coverage of the HostVars class
    because the __repr__ method cannot be tested by unit tests for the module
    module_utils.common._collections_compat.

    HostVars is a class that inherits from the collections.Mapping abstract base class.
    The __repr__ method is part of the Mapping class.

    In order to properly test __repr__, a class that inherits from HostVars must be created.
    This new class will have the __repr__ method overridden to return a list of
    data values for the class' members.

    Here is the list that is returned by this function:
    [('foo', 'bar'), ('bar', 'baz')]

    '''

# Generated at 2022-06-22 12:21:41.243076
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    inventory = 'localhost ansible_connection=local ansible_python_interpreter="python"'
    inventory = loader.load(inventory, 'test')
    variable_manager = VariableManager(loader=loader)
    hostvars = HostVars(inventory, variable_manager, loader)

    iter_hostvars = iter(hostvars)
    assert next(iter_hostvars) == 'localhost'
    assert next(iter_hostvars) == 'localhost'

# Generated at 2022-06-22 12:21:53.772136
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class DummyInventory(object):
        def __init__(self, host_names):
            self.hosts = host_names

    class DummyVariableManager(object):
        def __init__(self):
            self._vars_cache = {
                'alpha': dict(
                    foo = 'ansible',
                    bar = dict(
                        baz = 'qux',
                    ),
                ),
                'beta': dict(
                    foo = 'ansible',
                    bar = dict(
                        baz = 'qux',
                    ),
                ),
            }

        def get_vars(self, host=None, include_hostvars=False):
            return self._vars_cache.get(host)

    class DummyLoader(object):
        def __init__(self, searchpath):
            self.searchpath

# Generated at 2022-06-22 12:21:56.840800
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pytest
    from ansible.inventory.manager import InventoryManager
    ivm = InventoryManager()
    assert list(ivm.get_hosts().__iter__()) == list(ivm.hosts)

# Generated at 2022-06-22 12:22:17.873618
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class ResultCallback(object):
        def __init__(self):
            self.test_result = False

        def v2_runner_on_unreachable(self, result):
            self.test_result = True

    class Host(object):
        def __init__(self, name):
            self.name = name

    class Inventory(object):
        def __init__(self, loader, variable_manager):
            self._hosts = []
            self._loader = loader
            self._variable_manager = variable_manager

        def add_host(self, host):
            self._hosts.append(host)

        def get_host(self, host_name):
            return host if host.name == host_name else None

    class HostVarsVars(dict):
        def __missing__(self, key):
            return

# Generated at 2022-06-22 12:22:29.289437
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager('tests/inventory', None)
    inventory = inventory_manager.get_inventory()
    hostvars = HostVars(inventory, None, None)
    assert len(list(hostvars.keys())) == 0
    assert len(list(hostvars.values())) == 0
    assert len(list(iter(hostvars))) == 0
    assert len(hostvars) == 0
    assert len(hostvars.get('foo', [])) == 0

    inventory_manager = InventoryManager('tests/inventory_hostvars', None)
    inventory = inventory_manager.get_inventory()
    hostvars = HostVars(inventory, None, None)
    assert len(list(hostvars.keys())) == 1

# Generated at 2022-06-22 12:22:37.770696
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import sys
    import os
    source_dir = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, source_dir)

    # Imports of objects necessary for HostVars initialization
    from ansible.inventory import Inventory
    import ansible.constants as C
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    hosts = ['host1', 'host2', 'host3']
    host_vars = dict(host1={'var1': 'val1', 'var2': 'val2'},
                    host3={'var3': 'val3', 'var4': 'val4'})

# Generated at 2022-06-22 12:22:46.351789
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from collections import Mapping
    from .inventory import Inventory
    from .loader import DataLoader
    from .vars.manager import VariableManager

    loader = DataLoader()
    inventory = Inventory(loader=loader, host_list="localhost")
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    assert isinstance(hostvars, Mapping)
    assert hostvars.__repr__() == "{'localhost': {'ansible_inventory': {'hosts': {'localhost': {'ansible_play_hosts': ['localhost']}}}}}", \
        "Invalid output of method __repr__ of class HostVars"

# Generated at 2022-06-22 12:22:57.468069
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class MockInventory():
        def __init__(self, variable_manager):
            self._variable_manager = variable_manager

        def get_host(self, hostname):
            class MockHost():
                def __init__(self):
                    self._variable_manager = self._inventory._variable_manager
                    self._vars = {"var": "{{ var }}"}

                def get_vars(self):
                    return self._vars

            return MockHost()

    class MockVariableManager():
        def set_host_variable(self, host, varname, value):
            host._vars[varname] = value

    inventory = MockInventory(MockVariableManager())
    hostvars = HostVars(inventory=inventory, variable_manager=MockVariableManager(), loader=None)
    hostvars.set_host_variable

# Generated at 2022-06-22 12:23:00.523097
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    foo = HostVars({
        'a': 'foo',
        'b': 'bar',
    })
    assert(repr(foo) == "{'a': 'foo', 'b': 'bar'}")

# Generated at 2022-06-22 12:23:07.579915
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    cleartext_hostvars = {'foo': 'bar'}
    hostname = 'localhost'

    loader = DataLoader()
    vault_secrets = VaultLib([])
    vars_manager = VariableManager()
    inventory = InventoryManager(loader=loader,
                                 sources=None,
                                 vault_secrets=vault_secrets,
                                 host_list=[hostname])

# Generated at 2022-06-22 12:23:19.444957
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    """
    Provides an unit test for method __repr__ of class HostVars
    """
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    if not isinstance(STATIC_VARS, list):
        raise AssertionError("STATIC_VARS is not a list, the test is not applicable")


# Generated at 2022-06-22 12:23:26.825244
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, source='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host_vars = HostVars(inventory, variable_manager, loader)

    # Inject hostvars into variable_manager to support variable templating
    variable_manager.set_nonpersistent_facts(inventory.get_host('localhost'), host_vars.raw_get('localhost'))

    variable_manager.set_host_variable(inventory.get_host('localhost'), 'foo', 'bar')

# Generated at 2022-06-22 12:23:39.089157
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    data = """
    foo: localhost
    bar:
      - a
      - {a:b}
    """

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost")
    inventory.add_host(host='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load(data, variable_manager=variable_manager, loader=loader)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    assert len(hostvars) == 1
    assert 'localhost'

# Generated at 2022-06-22 12:24:08.974320
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import sys
    if sys.version_info[:2] == (2, 6):
        from unittest2 import TestCase, main
    else:
        from unittest import TestCase, main
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    simple_inventory = """
    localhost ansible_connection=local
    """
    simple_vars_file = """
    localhost
    """

    # first set of tests, with inventory variables
    class TestHostVars(TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.inventory = InventoryManager(loader=self.loader, sources=simple_inventory)