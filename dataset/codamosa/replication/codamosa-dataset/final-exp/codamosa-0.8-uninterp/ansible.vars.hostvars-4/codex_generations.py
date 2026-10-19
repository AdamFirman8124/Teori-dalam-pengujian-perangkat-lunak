

# Generated at 2022-06-22 12:14:26.343062
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.six import PY3

    inventory = InventoryManager(loader=DataLoader(), sources=['while True:'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    ## test with no hosts in inventory
    expected = '{}'
    observed = repr(hostvars)
    assert observed == expected, '%s: expected: %s, observed: %s' % (inspect.stack()[0][3], expected, observed)

    ## test with hosts in inventory

# Generated at 2022-06-22 12:14:35.729220
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import sys, os
    # Needed to import class HostVars
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    inventory = Inventory(loader=None, variable_manager=VariableManager(loader=None, inventory=None))
    vars_obj = HostVars(inventory=inventory, variable_manager=VariableManager(loader=None, inventory=inventory), loader=None)
    # Set variable 'foo' to 'hello world'
    vars_obj._variable_manager.set_host_variable(inventory.get_host('localhost'), 'foo', 'hello world')
    # Set variable 'h' to 'localhost'
   

# Generated at 2022-06-22 12:14:44.285445
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = Host(name="foo", variables={'foo': 'bar'})
    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars["foo"] == {'foo': 'bar'}
    assert hostvars["bar"] == AnsibleUndefined(name="hostvars['bar']")

# Generated at 2022-06-22 12:14:55.768952
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    inv_data = """
    all:
      children:
        webservers:
          hosts:
            web01.example.com:
        dbservers:
          hosts:
            db01.example.com:
    """
    # Create the groups and the host objects
    inventory = InventoryManager(loader=None, sources=inv_data)
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # Create object of class HostVars
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # Add a new variable group
    group = inventory.groups['webservers']
    group.set_variable('variable_on_group', 'value_of_variable_on_group')

# Generated at 2022-06-22 12:15:05.206559
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../lib/ansible'))
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    cli = CLI(None)
    cli._options = cli.base_parser(None).parse_args(['/dev/null'])
    cli._variables = VariableManager(loader=DataLoader(), inventory=Inventory(None))
    cli._variables.extra_vars = {'var1': 'value1', 'var2': 'value2'}

# Generated at 2022-06-22 12:15:13.358987
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Test setup
    import os
    import tempfile
    import yaml

    tmpdir = tempfile.mkdtemp()
    inv_path = os.path.join(tmpdir, 'hosts')
    vars_path = os.path.join(tmpdir, 'host_vars')
    os.mkdir(vars_path)

    # Given: Inventory with a group and a host
    hosts = {'test_group': ['test_host']}
    with open(inv_path, 'w') as f:
        yaml.dump(hosts, f)

    # and: Fake Ansible configuration
    from ansible.config.manager import ConfigManager
    from ansible.utils.display import Display
    display = Display()
    c = ConfigManager(display)
    c.parse()

    # and: Fake inventory


# Generated at 2022-06-22 12:15:15.399708
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    assert isinstance(HostVars(None, None, None).__iter__, type(iter([])))

# Generated at 2022-06-22 12:15:26.758782
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.six import PY3

    class TestPlugin(object):

        def __init__(self):
            self.inventory = None

        def verify_file(self, path):
            return path.endswith(('test_hostvars_repr', '.yaml', '.yml'))

        def parse(self, inventory, loader, path, cache=True):
            self.inventory = InventoryManager(loader=loader, sources=path)

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-22 12:15:36.618775
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager())
    variables = VariableManager(loader=DataLoader()).get_vars(play=dict(hosts=['localhost']))
    hostvars = HostVars(inventory, variable_manager=VariableManager(loader=DataLoader(), variables=variables))

    hostvars.set_host_variable(host='localhost', varname='ansible_connection', value='local')

    vars_localhost = hostvars.raw_get('localhost')
    vars_localhost['ansible_connection'] = 'remote'

    assert hostvars.raw_get('localhost')['ansible_connection'] == 'local'

    #

# Generated at 2022-06-22 12:15:45.958603
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    class FakeVars(object):
        def keys(self):
            return ['var1', 'var2']

    FakeVarsInstance = FakeVars()

    class LazyFakeVars(object):
        def __init__(self, instance):
            self.instance = instance

        def __getitem__(self, key):
            return self.instance[key]

    class MockLoader(object):
        def __init__(self):
            self.failed = False

        def get_real_file(self, path):
            return path

        def template(self, *args, **kwargs):
            if self.failed:
                raise Exception('Dummy error')
            return '{' + args[0] + '}'

    class MockHost(object):
        def __init__(self):
            self.vars = Lazy

# Generated at 2022-06-22 12:15:57.412945
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template import Templar

    inventory = Inventory(host_list=["localhost"])
    inventory.set_variable("localhost", "var1", "value1")
    inventory.set_variable("localhost", "var2", "value2")

    vars_manager = VariableManager(loader=DataLoader())
    vars_manager.add_group_vars("all", dict(var3="value3"))
    vars_manager.add_host_vars("localhost", dict(var4="value4"))
    vars_manager.add_host_vars

# Generated at 2022-06-22 12:16:08.916493
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    # from ansible.utils.vars import combine_vars
    from ansible.plugins import filter_loader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')
    variable_manager.set_inventory(inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hosts = hostvars.__iter__()

    assert isinstance(hostvars, HostVars)
    assert isinstance(hosts, Iterable)



# Generated at 2022-06-22 12:16:15.243887
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    hostvars = HostVars(inventory=InventoryManager(loader=DataLoader(), sources=['localhost']),
                        variable_manager=VariableManager(), loader=DataLoader())
    assert 'localhost' in hostvars.raw_get('localhost')

# Generated at 2022-06-22 12:16:24.691278
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import pickle
    from ansible.playbook.role import RoleRequirement

    # Create VariableManager and HostVars
    from ansible.inventory.manager import InventoryManager
    im = InventoryManager('localhost')
    from ansible.vars.manager import VariableManager
    vm = VariableManager(loader=None, inventory=im)
    hv = HostVars(inventory=im, variable_manager=vm, loader=None)

    # Pickle and unpickle HostVars to create a new instance of VariableManager
    # and make sure the new instance is properly configured
    vm2 = pickle.loads(pickle.dumps(hv))
    assert vm2._loader is None
    assert vm2._hostvars == hv

    # Make sure variable_manager is properly configured in RoleRequirement

# Generated at 2022-06-22 12:16:35.127303
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import copy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv)

    variables = {'test_hostvars': 'ok'}
    hostvars = HostVars(inv, variable_manager, loader)
    hostvars.set_host_variable(host=inv.hosts["localhost"], varname='foo', value=variables)

    assert repr(hostvars) == "{'localhost': {'foo': {'test_hostvars': 'ok'}}}"



# Generated at 2022-06-22 12:16:46.387982
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import wrap_var
    import json

    # Create inventory
    inventory = Inventory('/etc/ansible/hosts', [HOST_1, HOST_2])

    # Create variable manager
    variable_manager = VariableManager()

    # Create loader for variable_manager
    loader = DataLoader()

    # Create hostvars
    hostvars = HostVars(inventory, variable_manager, loader)

    # Check that hostvars_1 is empty
    hostvars_1 = hostvars.raw_get(HOST_1)
    assert hostvars_1 == {}

    # Check that hostvars_2 is empty

# Generated at 2022-06-22 12:16:55.217081
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    context = PlayContext()
    hostvars = HostVars({}, context)
    assert repr({}) == repr(hostvars)
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    hostvars.set_variable_manager(variable_manager)
    hostvars.set_inventory({'hosts': ['a', 'b']})
    assert {'a': AnsibleUndefined(name="hostvars['a']"), 'b': AnsibleUndefined(name="hostvars['b']")} == hostvars
    hostvars.set_host_variable('a', 'a_var', 123)


# Generated at 2022-06-22 12:17:03.471357
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import collections
    import warnings

    # Suppress AnsibleDeprecationWarning
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    # Test data
    vars = {'foo': 'bar', 'bar': {'foo': 'bar'}, 'baz': [1, 2, 3]}

    # Test __iter__
    iterator = HostVarsVars(vars, loader=None).__iter__()
    assert isinstance(iterator, collections.Iterator)
    assert list(iterator) == list(vars.keys())



# Generated at 2022-06-22 12:17:14.481748
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # case 1
    vars_dict = dict(a=1, b='2', c=3)
    vars_dict_template = dict(a=1, b=2, c=3)
    my_host_vars = HostVars(vars_dict)
    assert repr(my_host_vars) == repr(vars_dict_template)

    # case 2
    vars_dict = dict(a=1, b='2', c=3)
    vars_dict_template = dict(a=1, b='2', c=3)
    my_host_vars = HostVars(vars_dict, fail_on_undefined=True)
    assert repr(my_host_vars) == repr(vars_dict_template)


# Generated at 2022-06-22 12:17:21.337106
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    # Test assumptions about the way Templar renders data in Ansible
    from ansible.template import Templar

    templar = Templar(loader=None)

    string_with_vars = '{{ a }}'
    data = {'a': 'b'}
    result = templar.template(string_with_vars, variables=data, fail_on_undefined=False, static_vars=STATIC_VARS)
    assert result == 'b'

    string_with_vars_list = ['a', 'b', 'c', 'd']
    data = {'a': 'x', 'b': '2', 'c': '3', 'd': '4'}

# Generated at 2022-06-22 12:17:36.299282
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager

    import ansible.inventory.manager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inv = ansible.inventory.manager.InventoryManager(loader=loader, sources=['localhost,'])
    var_manager = VariableManager(loader=loader,inventory=inv)
    hostvars = HostVars(inventory=inv, variable_manager=var_manager, loader=loader)

    data = hostvars.raw_get('localhost')
    assert isinstance(data, dict)
    assert 'inventory_hostname' in data
    assert data['inventory_hostname'] == 'localhost'

    data = hostvars.raw_get('not_there')
    assert isinstance(data, AnsibleUndefined)

# Generated at 2022-06-22 12:17:44.241740
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.template import Templar
    from ansible.vars import combine_vars
    from ansible.playbook.play import Play

    '''
    Unit test to verify correctness of method raw_get of class HostVars.
    '''

    # This test simulates the situation when method raw_get of class HostVars
    # was called with 'group1' as a host name.

    # Create the inventory, with one group called 'group1' and a host called
    # 'localhost

# Generated at 2022-06-22 12:17:56.350803
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()
    group = Group('test')
    group.vars = {'foo': 'bar'}
    host = Host('localhost')
    host.vars = {'bar': 'baz'}
    group.add_host(host)
    inventory = InventoryManager(loader=None, sources=[])
    inventory.add_group(group)
    variable_manager = VariableManager()
    variable_manager._loader = None
    variable_manager._inventory = inventory

# Generated at 2022-06-22 12:18:08.694847
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    class FakeVariableManager:

        def get_vars(self, *args, **kwargs):
            return {
                'foo': 'bar',
                'baz': [1, 2, 3],
                'dic': {'key': 'value'}
            }

    class FakeInventory:
        def __init__(self):
            self.hosts = ['localhost']

        def get_host(self, hostname):
            return self.hosts[0]

    class FakeLoader:
        def __init__(self):
            pass

        def path_dwim(self, filename):
            return filename

    loader = FakeLoader()
    manager = FakeVariableManager()
    inventory = FakeInventory()

    hostvars = HostVars(inventory, manager, loader)


# Generated at 2022-06-22 12:18:16.672100
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Define variables and objects that will be used in this unit test.
    inventory = '{"all": {"children": ["local"]}, "local": {"hosts": ["localhost"]}}'
    loader = '''{"localhost": {"var1": "value1", "var2": "{{var1}}}", "var3": "{{var4}}"}}'''
    variable_manager = {'vars_cache': {'localhost': {'var4': 'value4'}}}

    # Init HostVars instance with variables and objects that will be used in this unit test.
    hostvars = HostVars(inventory, variable_manager, loader)

    # Try to get a variable from _vars_cache.
    assert(hostvars.get("localhost")["var3"] == 'value4')

# Generated at 2022-06-22 12:18:27.235893
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader)
    hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=loader)

    # Make sure that method __setstate__ works correctly when object's
    # attributes _variable_manager._loader and _variable_manager._hostvars
    # are not set
    obj_copy = pickle.loads(pickle.dumps(hostvars))

    assert obj_copy._variable_manager._loader is not None
    assert obj_copy._variable_manager._hostvars is not None
    assert obj_copy._variable_manager._hostvars == obj_copy

    # Make sure that method __setstate__ works correctly when object's
    # attributes _variable_manager._loader and _variable_manager._hostvars
    # are

# Generated at 2022-06-22 12:18:39.209508
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    hostvars = HostVars(None, None, None)

    # Test 1: Make sure to return an AnsibleUndefined when the key does not exist
    result = hostvars.__getitem__('test_host_none')
    expected = AnsibleUndefined(name="hostvars['test_host_none']")
    assert result == expected

    # Test 2: Make sure to return AnsibleSafeText value when the key exists
    hostvars._vars_cache = {'test_host': {'test_var': 'value'}}
    result = hostvars.__getitem__('test_host')['test_var']
    expected = 'value'
    assert isinstance(result, AnsibleUnsafeText)
    assert result == expected

# Generated at 2022-06-22 12:18:43.137550
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # Test data
    inventory_mock = {'hosts': ['a', 'b', 'c']}
    hosts = HostVars(inventory=inventory_mock, variable_manager={}, loader={})

    # Test execution
    hosts_iterator = iter(hosts)

    # Test assertion
    assert hosts_iterator == iter(inventory_mock['hosts'])

# Generated at 2022-06-22 12:18:50.733342
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    host_list = ['localhost', '127.0.0.1']

    _loader = DictDataLoader({})
    _variable_manager = VariableManager(loader=_loader)
    _inventory = InventoryManager(loader=_loader, sources='')

    hostvars = HostVars(_inventory, _variable_manager, _loader)

    iter_hostvars = [ host.name for host in hostvars ]

    assert iter_hostvars == host_list

# Generated at 2022-06-22 12:19:02.545685
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    my_vars = dict(
        foo='bar',
        bam=1,
    )
    my_hosts = [
        'host1',
        'host2',
    ]
    my_hostvars = dict((h, my_vars) for h in my_hosts)

    loader = DataLoader()
    vault_secrets_filename = '/path/to/vault_secrets.yml'
    vault_secrets = VaultLib([])
    vault

# Generated at 2022-06-22 12:19:13.122249
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Create test object
    obj = HostVars(None, None, None)

    # Test __setstate__ with valid data
    obj.__dict__.update({'_inventory': 'test'})
    obj.__dict__.update({'_loader': 'test'})
    obj.__dict__.update({'_variable_manager': 'test'})
    obj.__setstate__({})

    # Test __setstate__ with invalid data
    obj.__setstate__(None)
    obj.__setstate__(1)
    obj.__setstate__('')
    obj.__setstate__({'invalid': 'invalid'})
    obj.__setstate__({'loader': 'invalid'})
    obj.__setstate__({'inventory': 'invalid'})
    obj.__setstate

# Generated at 2022-06-22 12:19:22.126193
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    inventory_path = 'test/units/inventory/test_inventory.yml'
    inventory = InventoryManager(loader=DataLoader(), sources=[inventory_path])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    repr_data = repr(HostVars(inventory, variable_manager, DataLoader()))
    foo = "hostvars['_meta']"
    if foo in repr_data:
        return True
    else:
        return False

# Generated at 2022-06-22 12:19:34.441940
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    hostvars = HostVars(None, variable_manager, loader)

    variables = dict(
            foo="{{ bar }}",
            bar="baz",
        )

    # template variables assigned to a host
    hostvars.set_host_variable("some_host", "bar", "some_value")

    hostvars_vars = HostVarsVars(variables, loader)
    assert hostvars_vars["foo"] == "baz"

    # template variables assigned to a host override variables stored in
    # a variable file

# Generated at 2022-06-22 12:19:36.023702
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    hostvars = HostVars({})
    assert repr(hostvars).startswith("{}")


# Generated at 2022-06-22 12:19:46.109592
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    def get_host(name):
        if not inventory.hosts:
            inventory.add_host(Host(name='localhost', port=22))
        return inventory.get_host(name)

    hostvars = HostVars(inventory, variable_manager, DataLoader())
    hostvars.set_host_variable(get_host('localhost'), 'var1', 'value1')


# Generated at 2022-06-22 12:19:58.214771
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import sys
    sys.path.append('/home/user/myplaybooks')
    from ansible.config.manager import ConfigManager

    config_manager = ConfigManager('/home/user/myplaybooks/ansible.cfg')
    variable_manager = VariableManager(
        config_manager=config_manager,
        loader=Loader(),
    )

    inventory = InventoryManager(
        loader=Loader(),
        sources=[],
        variable_manager=variable_manager,
        config_manager=config_manager,
    )

    # We must set
    #   loader.possible_pid_files = ['/home/user/myplaybooks/ansible.pid']
    # because of method _get_pids_to_cleanup in class PidFile,
    # and we must set
    #   loader.possible_project_files

# Generated at 2022-06-22 12:20:08.185922
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        "fixtures/inventory-with-incorrect-group-vars": "",
        "playbooks/play.yml": "",
        "playbooks/fixtures/play.yml": "",
    })
    inventory = InventoryManager.load_inventory_from_loader(loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    host = Host("localhost")

    # Simple values
    variable_manager.set_host_variable(host, "foo", "bar")
    assert hostvars.get("localhost") == {"foo": "bar"}

# Generated at 2022-06-22 12:20:13.504508
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    play_context = PlayContext()
    variable_manager = VariableManager(loader=None, inventory=InventoryManager(loader=None, sources=[]))

# Generated at 2022-06-22 12:20:24.398474
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.vars.hostvars import HostVars
    from ansible.vars.variable_manager import VariableManager

    # Mock variables to be used by HostVars and VariableManager
    class FakeInventory:
        def __init__(self):
            self.hosts = []

        def get_host(self, name):
            if not self.hosts:
                return None

            return self.hosts[0]

    class FakeHost:
        def __init__(self, vars):
            self.vars = vars

    class FakeLoader:
        @staticmethod
        def load_from_file(path, cache=False, unsafe=False, show_content=True):
            return {'test': 'value'}

    # Create fake objects and init HostVars
    inventory = FakeInventory()
    loader

# Generated at 2022-06-22 12:20:29.060231
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from collections import namedtuple

    Host = namedtuple('Host', ['name'])

    hv = HostVars({Host('host1'): {'a': 'b'}})

    assert repr(hv) == "{Host(name='host1'): {'a': 'b'}}"

# Generated at 2022-06-22 12:20:42.341863
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(loader=DataLoader())
    inventory.add_group('the_group')
    inventory.add_host(host=inventory.localhost)
    inventory.add_host(host='other_host', group='the_group')

    variable_manager = VariableManager()
    hostvars = HostVars(inventory, variable_manager, loader=DataLoader())

    assert set(hostvars) == set([inventory.localhost, 'other_host'])

# Generated at 2022-06-22 12:20:53.818250
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    '''
    Ensures that HostVars.__setstate__() assigns _loader and _hostvars
    attributes to VariableManager instance if they are set to None.
    '''

    class Inventory(object):
        def __init__(self, loader):
            self._loader = loader

        def get_host(self, host_name):
            return None

    class Loader(object):
        def __init__(self): pass

    class VariableManager(object):
        def __init__(self, loader):
            self._loader = loader
            self._hostvars = None

        def __getstate__(self):
            return {'_loader': None, '_hostvars': None}

        def __setstate__(self, state):
            self.__dict__.update(state)

    loader = Loader()
   

# Generated at 2022-06-22 12:21:00.167182
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    test_hostvars = HostVars({}, VariableManager(), None)
    test_hostvars.set_inventory(InventoryManager(loader=None, sources=['localhost,']))
    assert test_hostvars.raw_get('localhost') == {
        'inventory_hostname': 'localhost',
        'inventory_hostname_short': 'localhost',
        'hostvars': {}
    }


# Generated at 2022-06-22 12:21:10.594663
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class Inventory(InventoryManager):
        def __init__(self, loader, sources='.'):
            self._loader = loader
            super(Inventory, self).__init__(loader, sources)

        def get_host(self, host_name):
            if host_name in self.hosts:
                return self.hosts[host_name]
            else:
                return None

    inventory = Inventory(DataLoader())
    inventory.hosts = {"localhost": MockHost('localhost')}
    hostvars = HostVars(inventory=inventory, variable_manager=VariableManager(), loader=DataLoader())


# Generated at 2022-06-22 12:21:17.772177
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    mock_hosts = ['hostA', 'hostB', 'hostC']
    mock_groups = [{
        'name': 'groupA',
        'hosts': ['hostA', 'hostB'],
    }, {
        'name': 'groupB',
        'hosts': ['hostC'],
    }]
    mock_loader = {
        'path/to/inventory': [{
            'hosts': mock_hosts,
            'groups': mock_groups,
        }]
    }
    mock_variable_manager = VariableManager()

# Generated at 2022-06-22 12:21:26.453041
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(
        loader=DataLoader(),
        variable_manager=VariableManager()
    )

    # pylint: disable=unused-variable
    host1 = inventory.add_host('host1')
    host2 = inventory.add_host('host2')
    # pylint: enable=unused-variable

    hvars = HostVars(inventory=inventory, variable_manager=VariableManager(), loader=DataLoader())

    assert len(hvars) == 2
    assert list(hvars) == ['host1', 'host2']



# Generated at 2022-06-22 12:21:37.184609
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(loader=DataLoader())
    inventory.add_host('foo')
    inventory.add_host('bar')
    inventory.add_host('baz')
    inventory.set_variable('foo', 'foo', 'foo')
    inventory.set_variable('foo', 'bar', 'bar')
    inventory.set_variable('bar', 'foo', 'foo')
    inventory.set_variable('baz', 'foo', 'bar')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, DataLoader())


# Generated at 2022-06-22 12:21:47.603512
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_data = {
        "_meta": {
            "hostvars": {
                "localhost": {
                    "foo": "bar"
                }
            }
        },

        "first": {
            "hosts": [
                "localhost"
            ],
            "vars": {
                "example": "original"
            }
        },

        "second": {
            "hosts": [
                "localhost"
            ],
            "vars": {
                "example": "override"
            }
        },
    }

    inv_obj = InventoryManager(loader, sources=inv_data)
   

# Generated at 2022-06-22 12:21:58.748787
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import os

    add_all_plugin_dirs()
    inventory_filename = os.getcwd() + '/tests/lib/ansible/inventory/test_inventory_1'
    loader = DataLoader()
    inventory = InventoryManager(loader, sources=inventory_filename)
    variable_manager = VariableManager()
    variable_manager._inventory = inventory

    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:22:05.327260
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    hostvars = HostVars(None, variable_manager, loader=DataLoader())

    assert variable_manager._hostvars is None

    state = dict(hostvars.__dict__)

    assert '_variable_manager' in state
    assert '_inventory' in state
    assert '_loader' in state

    hostvars.__setstate__(state)

    assert variable_manager._hostvars is hostvars



# Generated at 2022-06-22 12:22:22.665630
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    class MockInventory:

        def get_host(self, host_name):
            return 'a'

    class MockHost:

        def get_variables(self):
            return {'a': 'b'}

    class MockVariableManager:

        def get_vars(self, host='localhost', include_hostvars=True):
            return {'a': 'b'}

    class MockLoader:
        pass

    hostvars = HostVars(MockInventory(), MockVariableManager(), MockLoader())
    assert hostvars['a'] == {'a': 'b'}


# Generated at 2022-06-22 12:22:32.203313
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.errors import AnsibleParserError

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/test_hostvars.yml'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=variable_manager)
    assert hostvars.get('test_host_1') == {u'host_specific_var': u'some-value'}

    # If a host is not found, returns AnsibleUndefined
    assert isinstance(hostvars.get('not_present_host'), AnsibleUndefined)

# Generated at 2022-06-22 12:22:39.209414
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory_file = "/dev/null"
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    host = Host()
    host.name = "localhost"
    hostvars.set_variable_manager(variable_manager)

    variables = {
        "a": 1,
        "b": "{{a}}",
        "c": {
            "d": "{{b}}",
        }
    }
    hostvars

# Generated at 2022-06-22 12:22:48.435906
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager()
    inventory._hosts_cache = inventory._inventory.hosts
    host = inventory.get_host('localhost')
    assert host is not None

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager._hostvars = HostVars(inventory, variable_manager, loader)

    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_variable_manager(variable_manager)
    hostvars['localhost'].set_variable_manager(variable_manager)
    hostvars['localhost'].set_inventory(inventory)

    hostvars.set_host_variable

# Generated at 2022-06-22 12:22:58.648487
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    loader = DictDataLoader({'hostvars/hostname.yml': '''
---
hostvars_var_one: true
hostvars_var_two: 1
hostvars_var_three: 0.1
hostvars_var_four: [ 1, 2, 3]
hostvars_var_five: {'key': 'val'}
'''})
    variable_manager = VariableManager(loader=loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    host = inventory.get_host('hostname')

    hostvars = HostVars(inventory, variable_manager, loader)

# Generated at 2022-06-22 12:23:10.065156
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    vm_mock = MockVariableManager()
    vm_mock._loader = MockLoader()

    statetest = HostVars(MockInventory(), vm_mock, MockLoader())
    state = statetest.__getstate__()

    assert state.pop('_loader', None) is None
    assert state.pop('_variable_manager', None) is None
    assert state == {'_inventory': MockInventory()}

    # Loader and VariableManager are not restored by __setstate__.
    # They are expected to be available in the environment.
    vm_mock._loader = None
    vm_mock._hostvars = None
    statetest.__setstate__(state)

    assert vm_mock._loader is statetest._loader
    assert vm_mock._hostvars is statetest


# Generated at 2022-06-22 12:23:21.582948
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    loader = DictDataLoader({'inventory': 'localhost ansible_connection=local'})

    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars._find_host = lambda name: None
    assert isinstance(hostvars.raw_get('unknown_host'), AnsibleUndefined)

    inventory.add_host(name='localhost')
    host = inventory.get_host(name='localhost')
    variable_manager.set_host_variable(host, 'foo', 'bar')
    assert hostvars.raw_get('localhost')['foo'] == 'bar'


# Generated at 2022-06-22 12:23:29.850379
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    dataloader = DataLoader()

    inventory = InventoryManager(dataloader)
    hostvars = HostVars(inventory, VariableManager(), dataloader)
    test_hostname = 'test_host'
    hostvars.set_host_variable(Host(test_hostname), 'test_var', 2)
    assert hostvars[test_hostname]['test_var'] == 2

    hostvars.set_host_variable(Host(test_hostname), 'test_var', '{{ test_var }}')
    assert hostvars[test_hostname]['test_var']

# Generated at 2022-06-22 12:23:41.908369
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class ExampleVariableManager():
        def __init__(self):
            self._loader = None
            self._hostvars = None

        # Methods __getstate__ and __setstate__ of VariableManager do not
        # preserve _loader and _hostvars attributes to improve pickle
        # performance and memory utilization.
        def __getstate__(self):
            state = self.__dict__.copy()
            for key in list(state.keys()):
                if key == "_loader" or key == "_hostvars":
                    del state[key]
            return state

        def __setstate__(self, state):
            self.__dict__.update(state)

    variable_manager = ExampleVariableManager()

    class ExampleLoader():
       def __init__(self):
           self._basedir = None

    loader = ExampleLoader()



# Generated at 2022-06-22 12:23:50.954023
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    inv = InventoryManager(loader=DataLoader())
    vars_manager = VariableManager(loader=DataLoader(), inventory=inv)
    inv.add_host('foohost', 'foohost')
    inv.add_host('barhost', 'barhost')
    hostvars = HostVars(inv, vars_manager, DataLoader())
    mylist = [x for x in hostvars]
    assert len(mylist) == 2
    assert 'foohost' in mylist
    assert 'barhost' in mylist

# Generated at 2022-06-22 12:24:06.817085
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager

    inventory = mock.MagicMock()
    inventory.get_host.return_value = None
    inventory.hosts = [
        'no_hostname',
        'localhost',
        'localhost_other_name'
    ]

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    loader = mock.MagicMock()
    hv = HostVars(inventory, variable_manager, loader)

    # Hosts mentioned in inventory are always available
    for host in inventory.hosts:
        assert host in hv

    # Hosts not mentioned in inventory are never available
    assert 'bogus' not in hv

    # Hosts not mentioned in inventory are not even in vars_cache
    assert 'bogus' not in hv._variable