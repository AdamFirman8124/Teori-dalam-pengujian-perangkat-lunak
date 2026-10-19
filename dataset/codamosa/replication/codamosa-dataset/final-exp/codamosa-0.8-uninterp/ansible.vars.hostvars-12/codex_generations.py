

# Generated at 2022-06-22 12:14:15.020346
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    hv = HostVars({'_loader': lambda: None}, None, None)
    iter(hv)

# Generated at 2022-06-22 12:14:26.345061
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    def test_template(template, expected_result, variables, loader):
        host_vars_vars = HostVarsVars(variables, loader)
        templar = Templar(vars=host_vars_vars)
        assert templar.template(template, convert_bare=False) == expected_result

    class Loader():
        def __init__(self, hostvarsvars):
            self._hostvarsvars = hostvarsvars

        def get_basedir(self, *args, **kwargs):
            return '.'

    # Test that the values of an unaltered dictionary can be used as a template
    class Dict(dict):
        def __str__(self):
            return 'ok'


# Generated at 2022-06-22 12:14:35.319209
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template.vars import VarsModule

    loader = VarsModule()
    variable_manager = VariableManager(loader=loader)

    h = Host('localhost')
    variable_manager.set_host_variable(h, 'one', '{{ two }}')

    play_context = PlayContext()
    play_context.set_variable_manager(variable_manager)

    hostvars = HostVars(loader=loader, inventory=None, variable_manager=variable_manager)

    # If no value for 'two' is defined, 'one' will expand to an empty string
    assert hostvars['localhost']['one'] == ''

    # Template expansion should be successful if the

# Generated at 2022-06-22 12:14:46.673403
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars, HostVars
    loader = DataLoader()
    inv = InventoryManager(loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inv)
    hostvars = HostVars(inv, variable_manager=variable_manager, loader=loader)
    hostvarsvars = HostVarsVars(hostvars, loader=loader)
    hostvars = HostVars(inv, variable_manager=variable_manager, loader=loader)
    assert repr(hostvars) == repr(hostvarsvars)

# Generated at 2022-06-22 12:14:52.282311
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    variables = {
        'foo': 'bar',
        'bar': 'baz',
    }

    iterator = iter(HostVarsVars(variables, None))
    assert next(iterator) == 'foo'
    assert next(iterator) == 'bar'

    try:
        next(iterator)
    except StopIteration:
        pass

# Generated at 2022-06-22 12:14:58.583845
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars import VariableManager, HostVars
    from ansible.inventory import Inventory

    loader = None
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    hostvars = HostVars(inventory, variable_manager, loader)
    variable_manager.set_inventory(inventory)

    i = iter(hostvars)
    assert i == iter(inventory.hosts)



# Generated at 2022-06-22 12:15:09.667379
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.reserved import Reserved

    # Create UnsafeProxy object to test if it would be pickled correctly
    unsafe_proxy = UnsafeProxy(Reserved(dict()))
    # Convert the object into a dict so it can be pickled
    unsafe_proxy_dict = dict(unsafe_proxy.__dict__)

    # Create HostVars objects
    hostvars_1 = HostVars(None, None, None)
    hostvars_1._variable_manager == None
    hostvars_1._loader = None
    hostvars_1._variable_manager._unsafe_proxy = unsafe_proxy
    hostvars_1._variable_manager._loader = None
    hostvars_1._variable_manager._hostvars = None



# Generated at 2022-06-22 12:15:23.042106
# Unit test for method __getitem__ of class HostVars

# Generated at 2022-06-22 12:15:33.865383
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    hosts = [
        "someloader1.example.org",
        "someloader2.example.org",
        "someloader3.example.org",
    ]

    inventory = Inventory(loader=None, variable_manager=None, host_list=hosts)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = dict(
        port=5309,
        somehost="darkstar.example.org",
    )
    variable_manager.set_play_context(play_context)
    play_source =  dict(
        name = "Ansible Play 8",
        hosts = 'loader',
    )

# Generated at 2022-06-22 12:15:42.871409
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible import variables
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager

    h = Host('testhost')
    p = Play()
    v = variables.VariableManager(loader=None, inventory=None)
    v.set_inventory(inventory=None)
    hv = HostVars(inventory=None, variable_manager=v, loader=None)
    hv.set_variable_manager(v)
    hv.set_host_variable(host=h, varname='testvar', value='testvalue')
    hv.set_nonpersistent_facts(host=h, facts={'testfact': 'testvalue'})

# Generated at 2022-06-22 12:15:58.368971
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import inventory_loader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:16:05.968095
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from copy import deepcopy

    original_hv = HostVars({}, {})
    assert original_hv._variable_manager._loader is None
    assert original_hv._variable_manager._hostvars is None

    hv_after_pickle = deepcopy(original_hv)
    assert hv_after_pickle._loader is not None
    assert hv_after_pickle._variable_manager._loader is None
    assert hv_after_pickle._variable_manager._hostvars is None

# Generated at 2022-06-22 12:16:17.376277
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''
    Unit test for method __getitem__ of class HostVars
    '''

    from ansible import constants as C

    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    # Create inventory
    inventory_manager = InventoryManager(None, loader=None, sources=C.DEFAULT_HOST_LIST)
    inventory_manager.hosts['localhost'] = Host('localhost')
    inventory_manager.hosts['localhost'].vars = {'var1': 'value1'}

    # Create variables
    variable_manager = VariableManager()

    # Create HostVars object
    hostvars = HostVars(inventory=inventory_manager, variable_manager=variable_manager, loader=None)

    # Call the method
    result = host

# Generated at 2022-06-22 12:16:19.672515
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # This method cannot be unit tested without Inventory and VariableManager
    # dependencies.
    #
    # Tested in test/integration/targets/hostvars.yml
    pass

# Generated at 2022-06-22 12:16:26.628010
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # Basic object initialization and initialization of _variable_manager
    # with VariableManager class
    inventory = None
    loader = 'loader'
    variable_manager = 'variable_manager'
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_variable_manager(variable_manager)

    # Class initialization for VariableManager
    class VariableManager:
        def get_vars(self, host=None, include_hostvars=True):
            self.get_vars_called = True
            if include_hostvars:
                return 'vars'
            else:
                return 'non-templated variables'

    # Only to test the Method, this should not be called
    def _find_host(self, host_name):
        return host_name


# Generated at 2022-06-22 12:16:37.223575
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    loader = None
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inv)

    hostvars = HostVars(inventory=inv, variable_manager=variable_manager, loader=loader)

    # Simple case: return variables defined in inventory
    hostvars['localhost'] = {'foo': 'localhost foo', 'bar': 'localhost bar'}
    assert hostvars['localhost']['foo'] == 'localhost foo'
    assert hostvars['localhost']['bar'] == 'localhost bar'

    # Variable defined in vars_files
    variable_manager.extra_vars = {'baz': 'baz variable'}
    variable_manager.extra_

# Generated at 2022-06-22 12:16:43.288581
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    '''
    Test scenario:
    Inventory contains a host and a group. A variable that is defined
    in a group is used in a variable of a host. Using method raw_get
    of class HostVar we expect to get data of a variable that is not
    run through the template engine.
    '''
    # inventory contains a host named "localhost"
    inventory = make_inventory(host_vars_hosts)
    # variable manager
    variable_manager = VariableManager(loader=DictDataLoader({}))
    variable_manager.set_inventory(inventory)
    # hostvars
    hostvars = HostVars(inventory, variable_manager, loader=DictDataLoader({}))
    # hostvars['localhost'] should contain a variable, which is not run
    # through the template engine
    localhost_vars = hostv

# Generated at 2022-06-22 12:16:53.338256
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    variable_manager.set_play_context(play_context)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    host = inventory.get_host('localhost')
    variable_manager.set_nonpersistent_facts(host, dict(foo='bar', baz='qux'))

# Generated at 2022-06-22 12:17:05.076183
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    inventory._hosts = hostvars
    host = inventory.add_host('localhost')
    assert repr(hostvars) == "{'localhost': {}}"
    hostvars.set_host_variable(host=host, varname='foo', value='bar')
    assert repr(hostvars) == "{'localhost': {'foo': 'bar'}}"

# Generated at 2022-06-22 12:17:15.939937
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager   import InventoryManager
    from ansible.vars                import VariableManager

    # Find a directory that has the inventory file "hosts"
    inventory_directory = None
    for directory in (".", ".."):
        if os.path.isfile(os.path.join(directory, "hosts")):
            inventory_directory = directory
            break

    assert inventory_directory is not None

    inventory_file      = os.path.join(inventory_directory, "hosts")
    inventory_directory = os.path.abspath(os.path.join(inventory_directory, os.path.pardir))

    inventory = InventoryManager(loader=None, sources=inventory_file)
    variable_manager = VariableManager(loader=None, inventory=inventory)


# Generated at 2022-06-22 12:17:30.332830
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    import copy

    variables = dict(foo = 'abc', bar = 1, baz = [2, 3], qux = {'corge': 'grault'})

    class FakeVarsManager(VariableManager):
        def __init__(self):
            pass

        def get_vars(self, loader, path, play=None, host=None, task=None, include_delegate_to=False):

            if host and host.name:
                foo = copy.deepcopy(variables)
                foo.update(dict(hostvars = host.name))

            return foo

    host

# Generated at 2022-06-22 12:17:40.496286
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.inventory.host_list import Host, Group

    inventory = Group('all')

    allvars = dict(foo=2, bar="baz")

    inventory.set_variable('group_vars', 'all', allvars)

    host = Host('test')
    inventory.add_host(host)

    hostvars = HostVars(inventory, variable_manager=vars_loader, loader=None)

    raw = hostvars.raw_get('test')
    assert 'group_vars/all' in raw
    assert 'hostvars/test' in raw
    assert raw['group_vars/all']['foo'] == 2
    assert raw['group_vars/all']['bar'] == 'baz'

# Generated at 2022-06-22 12:17:45.332186
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    test_hostvars = HostVars(inventory=None, variable_manager=None, loader=None)
    test_hostvars_dict = test_hostvars.__getstate__()
    test_hostvars.__setstate__(test_hostvars_dict)
    assert test_hostvars_dict == test_hostvars.__getstate__()

# Generated at 2022-06-22 12:17:52.931616
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inventory = Inventory(host_list='tests/inventory')
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'foo': 'bar'}

    hv = HostVars(inventory, variable_manager, None)
    r = hv.raw_get('localhost')
    assert(r['foo'] == 'bar')

# Generated at 2022-06-22 12:18:04.849322
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import get_all_plugin_loaders

    # Ansible requires a loader to load plugins when templating is performed.
    # While it is easier to simply specify a plugins path, the following
    # helper finds all plugin loaders, which allows testing without
    # specifying any plugin path.
    plugin_loaders = get_all_plugin_loaders()

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=plugin_loaders, sources='localhost ansible_connection=local'))
    play_context = Play().set_loader(plugin_loaders)

# Generated at 2022-06-22 12:18:14.712080
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.clean import module_response_deepcopy
    import os
    import tempfile
    import json

    inventory_path = os.path.join(tempfile.gettempdir(), 'inventory')
    with open(inventory_path, 'w') as inventory_file:
        inventory_file.write("""
[local]
localhost  ansible_connection=local

[webservers]
foo.example.org
""")

    inventory = InventoryManager(loader=None, sources=inventory_path)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    hostvars.set

# Generated at 2022-06-22 12:18:25.320450
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=["localhost"])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    vc = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    context = PlayContext()
    templar = Templar(loader=DataLoader(), variables=vc, shared_loader_obj=vc)

    def _set(host, var, value):
        vc.set_host_variable(host, var, value)

    host_name = 'localhost'


# Generated at 2022-06-22 12:18:32.615101
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Mock inventory and variable manager
    i = MockInventory()
    v = MockVars()
    loader = MockLoader()
    # HostVars is a Mapping, not a MutableMapping, so we need to use raw_get
    h = HostVars(i, v, loader)
    assert 'a' == h.raw_get('a')['a']
    assert 'b' == h['a']['b']


# Generated at 2022-06-22 12:18:42.603542
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    """
    Unit test for HostVars.__repr__()
    """

    # Create a mock object of class VariableManager
    class VariableManagerMock:
        def __init__(self):
            self.vars_cache = {
                'host1': {
                    'foo1': 'foo',
                    'bar1': 'bar',
                },
            }

    # Create a mock object of class Inventory
    class InventoryMock:
        def __init__(self):
            self.hosts = [
                'host1',
            ]

    # Create a mock object of class AnsibleFileLoader
    class AnsibleFileLoaderMock:
        def __init__(self):
            pass

    # Create a mock object of class Host

# Generated at 2022-06-22 12:18:47.577969
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    hosts = ["foo"]

    inventory = InventoryManager()
    inventory.add_group('all')
    for host in hosts:
        inventory.add_host(host)
    inventory.get_host(hosts[0]).set_variable('db_pass', 'verysecure')

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    # Assert that __repr__ of HostVarsVars contains 'verysecure'
    # if __repr__ of HostVarsVars is to be trusted.
    hvars = HostVars(inventory, variable_manager, None)
    assert 'verysecure' in repr(hvars)

# Generated at 2022-06-22 12:19:03.315169
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    hostvars = HostVars(
        inventory=Inventory(loader=None),
        variable_manager=VariableManager(loader=None, inventory=Inventory(loader=None)),
        loader=None,
    )
    vars_result = hostvars.raw_get('fake_host')
    assert vars_result == AnsibleUndefined(name="hostvars['fake_host']")
    # Check that the cache is empty
    assert hostvars._variable_manager._vars_cache == {}
    # Check that no variables have been added to the cache in the host context
    # because the host does not exist in the inventory
    assert 'fake_host' not in hostvars

# Generated at 2022-06-22 12:19:10.843194
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    # TODO: need to mock this more
    vm = set()
    loader = set()
    inventory = set()
    hostvars = HostVars(inventory, vm, loader)

    # Test for 'does not exist'
    vm_vars = hostvars.raw_get('thisdoesnotexist')
    assert isinstance(vm_vars, AnsibleUndefined)

    # Test for 'localhost'
    vm_vars = hostvars.raw_get('localhost')
    assert isinstance(vm_vars, Mapping)

# Generated at 2022-06-22 12:19:22.126180
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    inventory = InventoryManager(loader=DataLoader(), sources=None)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    play_context = Play().set_variable_manager(variable_manager)
    hostvars = HostVars(inventory, variable_manager, DataLoader())

    # Create two hosts
    inventory.add_host(host='host1')
    hostvars.set_host_variable('host1', 'var1', 'val1')
    inventory.add_host(host='host2')

# Generated at 2022-06-22 12:19:27.953082
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import ansible
    import ansible.vars.unsafe_proxy
    import ansible.vars
    import ansible.inventory
    import ansible.constants

    fake_loader = ansible.parsing.dataloader.DataLoader()

    fake_inventory = ansible.inventory.Inventory(fake_loader, groups={
        'local': [],
        'all': [],
        'ungrouped': [],
    })
    fake_inventory.hosts = ansible.vars.hostvars.HostVars(fake_inventory, ansible.vars.variable_manager.VariableManager(), fake_loader)


# Generated at 2022-06-22 12:19:30.875591
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    hostvars = HostVars(None, None, None)
    assert(hostvars[None] == AnsibleUndefined)

# Generated at 2022-06-22 12:19:37.350591
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    hostvars = HostVars(None, None, None)
    items = list(hostvars)
    assert isinstance(items, list) and len(items) == 0

    try:
        # If the method raises AttributeError, add the call to list()
        # to the assertion, so the exception will be raised
        list(items.__iter__())
        assert False, "items.__iter__() does not raise AttributeError"
    except AttributeError:
        assert True



# Generated at 2022-06-22 12:19:46.972347
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.compat.six import StringIO

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=StringIO(''))
    vars_cache = HostVars(inv, variable_manager=inv.variable_manager, loader=loader)

    assert vars_cache.raw_get('non-exist') == AnsibleUndefined(name="hostvars['non-exist']")
    assert 'non-exist' not in vars_cache
    assert 'non-exist' not in vars_cache.keys()

    host = inv.get_host('localhost')

# Generated at 2022-06-22 12:19:54.702850
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    play = Play().load({'name': 'test', 'hosts': 'all'}, variable_manager=VariableManager(), loader=None)
    task = Task().load({'name': 'test'}, variable_manager=play._variable_manager, loader=play._loader)
    group = Group('all')
    group.add_host(Host('localhost'))

    variable_manager = VariableManager()
    variable_manager._hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=None)
    variable_manager._hostvars._inventory = []
    variable_

# Generated at 2022-06-22 12:20:05.462857
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import vars_loader

    # vars_loader should be registered in __main__, but we want to check it
    # explicitly before running any tests
    vars_loader.add_directory(os.path.join(os.path.dirname(__file__), 'vars_plugins'))

    # Load the inventory
    localhost = dict(host_name='localhost', ansible_host='127.0.0.1')
    groups = dict(local=dict(hosts=[localhost]))

    loader = DataLoader()
    inventory = InventoryManager(loader, groups=groups)

# Generated at 2022-06-22 12:20:09.293657
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader, sources='localhost')
    hostvars = HostVars(inventory, None, loader)
    repr(hostvars)

# Generated at 2022-06-22 12:20:25.042037
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars.hostvars import HostVars

    # Contains 3 hosts
    inventory = Inventory(host_list=["host1", "host2", "host3"])

    # Create an instance of HostVars
    hostvars = HostVars(inventory, None, None)

    # Check if all hosts are iterated over
    assert set(hostvars) == set(["host1", "host2", "host3"])


# Generated at 2022-06-22 12:20:32.721377
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager(loader='tests/test_utils/test_playbooks/hosts')
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)
    variable_manager.set_inventory(inventory_manager)
    initialized_vars = HostVars(inventory=inventory_manager, variable_manager=variable_manager, loader=None)

    result = repr(initialized_vars)
    assert isinstance(result, str)

# Generated at 2022-06-22 12:20:39.561243
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources='localhost,')
    hv = HostVars(inventory=inv, variable_manager=None, loader=loader)

    ii={}
    for i in hv:
        ii[i]=1
    assert localhost in ii


# Generated at 2022-06-22 12:20:43.841602
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/test_hostvars.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)
    foo = hostvars.raw_get('localhost')
    assert foo == {'bar': 'baz'}

# Generated at 2022-06-22 12:20:56.322191
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.inventory
    import ansible.plugins.loader
    import ansible.vars
    import ansible.template

    # Create some fake plugin
    class FakePlugin(object):

        def __init__(self, plugin_name):
            self.plugin_name = plugin_name

    # Create some fake loader
    class FakeLoader(object):
        def __init__(self):
            self.plugins = [FakePlugin("1"), FakePlugin("2")]

        def get_plugin(self, name, *args, **kwargs):
            for plugin in self.plugins:
                if plugin.plugin_name == name:
                    return plugin

    # Create fake inventory and add a host to it
    inventory = ansible.inventory.Inventory()
    host = ansible.inventory.Host("fakehost")
    group = ansible.inventory

# Generated at 2022-06-22 12:21:01.118967
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory

    inventory = MockInventory(loader=DictDataLoader({}))
    variable_manager = DummyVariableManager()

    hostvars = HostVars(inventory, variable_manager, loader=DictDataLoader({}))
    host_name = "foobar"
    hostvars[host_name]
    # operation should not raise exception



# Generated at 2022-06-22 12:21:10.258785
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Tests that HostVars.__getitem__ correctly runs through the templating engine
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    hostvars = HostVars(Inventory(loader=DataLoader()), VariableManager(loader=DataLoader()), loader=DataLoader())
    hostvars._variable_manager.set_host_variable("localhost", "my_fact", "bar")
    assert hostvars.raw_get("localhost").get("my_fact") == "bar"
    assert hostvars["localhost"].get("my_fact") == "bar"



# Generated at 2022-06-22 12:21:13.076017
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pytest
    from collections import Iterable
    h = HostVars(None, None, None)
    assert isinstance(h, Iterable)

# Generated at 2022-06-22 12:21:23.571951
# Unit test for method __getitem__ of class HostVars

# Generated at 2022-06-22 12:21:25.308695
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    pass


# Generated at 2022-06-22 12:21:56.699838
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    # Create a simple inventory
    inventory = Inventory(host_list=[])
    inventory.add_host("localhost")
    inventory.add_host("otherhost")

    # Create a simple variable manager
    variable_manager = VariableManager()
    variable_manager.extend_vars({'foo': 'foo_value'})

    # Create a simple loader, it is not needed for this test but
    # HostVars needs it to be instantiated
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    # Instantiate HostVars
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # localhost must be a Host object

# Generated at 2022-06-22 12:22:05.572674
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    loader = DummyLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    inventory.hosts = [
        Host(name="test1", vars={'a': 1}),
        Host(name="test2", vars={'a': 2})
    ]
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.set_inventory(inventory)
    variable_manager._options = DummyOptions()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hostvars.set_variable_manager(variable_manager)


# Generated at 2022-06-22 12:22:17.235033
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.compat.tests import mock

    inv_data = '''
        [all]
        host01
        host02
        localhost

        [local]
        localhost

        [local:vars]
        my_var="my value"

        [web]
        host02
    '''

    inv_data_file = '/tmp/test'
    with open(inv_data_file, 'w') as f:
        f.write(inv_data)

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=inv_data_file)
    mapper = VariableManager(loader=loader, inventory=inv)

# Generated at 2022-06-22 12:22:28.609229
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    hostvars = HostVars(None, None, None)
    hostvars._variable_manager = FakeVariableManager()

    assert hostvars['test'] == 'test'
    assert hostvars['foo'] == 'foo'
    assert hostvars['bar'] == 'bar'

    assert hostvars.get('test') == 'test'
    assert hostvars.get('foo') == 'foo'
    assert hostvars.get('bar') == 'bar'

    assert 'test' in hostvars
    assert 'foo' in hostvars
    assert 'bar' in hostvars

    assert len(hostvars) == 3
    assert list(hostvars) == ['test', 'foo', 'bar']

# Generated at 2022-06-22 12:22:37.166755
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    inv = Inventory("")
    data = dict(foo="bar")
    h = inv.hosts[0]
    h.set_vars(data)

    variables = VariableManager(loader=None)
    variables.set_inventory(inv)

    hostvars = HostVars(inv, variables, loader=None)
    hostvar = hostvars.raw_get("test")

    for key in data.keys():
        assert key in hostvar
        assert hostvar[key] == data[key]

    for key in hostvar.keys():
        assert key in data
        assert data[key] == hostvar[key]


# Generated at 2022-06-22 12:22:45.061327
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['tests/inventory'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    # check that returned data is not run through the templating engine
    assert '{{' in hostvars['example']['foo']

    # check that templated variable can be used in the returned data
    assert 'fake' in hostvars['example']['bar']

    # check that templated variable cannot be used in the returned data

# Generated at 2022-06-22 12:22:56.816901
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import sys
    import ansible.inventory
    import ansible.vars
    import ansible.utils.shlex
    import ansible.template
    import ansible.utils.unsafe_proxy

    inventory_file = ansible.inventory.Inventory(sys.argv[1])
    group = inventory_file.groups_dict.get(sys.argv[2])
    host = group.get_host(sys.argv[3])
    variable_manager = ansible.vars.VariableManager()
    variable_manager.set_inventory(inventory_file)
    loader = ansible.template.AnsibleLoader(open_func=ansible.utils.shlex.open_if_exists, variables=variable_manager.get_vars(host=host))

# Generated at 2022-06-22 12:23:05.023144
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = Inventory(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    host = inventory.get_host('localhost')
    hostvars.set_host_variable(host, 'foo', 'bar')
    hv = hostvars.raw_get('localhost')
    assert 'foo' in hv



# Generated at 2022-06-22 12:23:16.644074
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import sys
    import io
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVarsVars

    dbg_stream = io.StringIO()
    dbg_handler = logging.StreamHandler(dbg_stream)
    dbg_handler.setLevel(logging.DEBUG)
    logger.addHandler(dbg_handler)

    inventory_manager = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory_manager)

# Generated at 2022-06-22 12:23:25.682352
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    fake_vars_cache = {
        'localhost': {
            'foo': '1',  # non-templated, i.e. "raw"
            'bar': '{{ baz }}',  # templated
        },
        'other_host': {
            'foo': '2',  # non-templated, i.e. "raw"
            'bar': '{{ baz }}',  # templated
        },
        'bad_host': {
            'foo': '{{ foo }}',  # templated but will fail
            'bar': '{{ baz }}',  # templated
        },
    }