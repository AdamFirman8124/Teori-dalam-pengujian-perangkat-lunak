

# Generated at 2022-06-22 12:14:26.900332
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    vars_cache = {'localhost': {'a': 12, 'b': 'stuff'}}
    variable_manager = VariableManager(loader=DataLoader(), inventory=None, version_info=None, vars_cache=vars_cache)
    inventory = Inventory([Host('localhost')], [Group('sample_group')])
    inventory.set_variable_manager(variable_manager)
    variable_manager.set_inventory(inventory)
    hostvars = HostVars(inventory, variable_manager, DataLoader())
    assert hostvars.raw_get('localhost') == {'a': 12, 'b': 'stuff'}

# Generated at 2022-06-22 12:14:33.158719
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'a': '1', 'b': '2'}

    hostvars = HostVarsVars(variable_manager.get_vars(), loader)

    assert sorted(hostvars) == sorted(variable_manager.get_vars())


# Generated at 2022-06-22 12:14:36.352668
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars_vars = HostVarsVars({'a': 'b', 'c': 'd'}, None)
    assert sorted(hostvars_vars) == ['a', 'c']

# Generated at 2022-06-22 12:14:48.442793
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.plugins.loader import vars_loader

    for name in HostVars.__iter__.func_code.co_names:
        # __iter__ uses the following names from other modules
        if name not in ('HostVars', 'vars_loader', '__name__', 'iterator'):
            assert name in HostVars.__dict__

    # Create a dummy inventory
    inventory_class = vars_loader._inventory_classes['host_list']
    dummy_inventory_instance = inventory_class({'plugin': 'host_list', 'hosts': ['foo']})

    # Create a dummy variable manager
    dummy_variable_manager = vars_loader.get('variable_manager')
    # Make a HostVars instance using this inventory dummy

# Generated at 2022-06-22 12:14:52.803574
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from collections import Iterable
    class LoaderModule(object):
        pass
    loader = LoaderModule()
    hostvars_vars = HostVarsVars({'test': 'test'}, loader)
    assert isinstance(hostvars_vars.__iter__(), Iterable)

# Generated at 2022-06-22 12:14:58.355153
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])

    group = Group(name="test")

    inventory.add_group(group)

    host = Host(name="test")
    group.add_host(host)

    variable_manager = VariableManager(loader=loader, inventory=inventory)

    vars_template = {}
    vars_template["ansible_version"] = "1.9.4"
    vars_template["ansible_play_hosts"] = "test"

    variable_manager._hostvars = Host

# Generated at 2022-06-22 12:15:09.340786
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars = HostVars(None, None, None)

    test_host = dict()
    test_host["name"] = 'testhost'
    test_host["vars"] = dict()
    test_host["vars"]["var1"] = 'value1'
    test_host["vars"]["var2"] = 'value2'
    test_host["vars"]["var3"] = 'value3'

    hostvars._vars = test_host
    hostvars._vars["ansible_sshd_port"] = 22
    hostvars._vars["ansible_ssh_user"] = "user"

    variables = dict()
    variables["inventory_hostname"] = "localhost"
    hostvars._loader = dict(path_info=dict(), variables=variables)


# Generated at 2022-06-22 12:15:22.647323
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import become_loader, module_loader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.persistent_facts import PersistentFact

    loader = module_loader
    loader.add_directory(os.path.join(os.path.dirname(__file__), '../modules'))
    loader.add_directory(os.path.join(os.path.dirname(__file__), '../module_utils'))

    become_loader.add_directory(os.path.join(os.path.dirname(__file__), '../become'))

# Generated at 2022-06-22 12:15:32.767917
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import unittest
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create fake inventory
    inventory = Inventory(loader=DataLoader(), variable_manager=None)
    inventory.set_variable('test_host', 'ansible_user', 'pablo')

    # Create fake variable manager
    variable_manager = VariableManager()

# Generated at 2022-06-22 12:15:34.419861
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # TODO: implement
    pass

# Generated at 2022-06-22 12:15:55.102856
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    inventory = Inventory("local.host")
    inventory.set_variable("local.host", "x", "a")
    inventory.set_variable("local.host", "y", "$x {{x}}")
    inventory.set_variable("local.host", "z.a.b", 10)
    inventory.set_variable("local.host", "z.c", "a")
    inventory.set_variable("local.host", "z.d", "$z")
    inventory.set_variable("local.host", "z.e", "$z.f.g")
    inventory.set_variable("local.host", "z.a.g", 20)
    inventory.set_variable("local.host", "z.a.g.h", 30)

# Generated at 2022-06-22 12:16:03.442701
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()
    inventory = Inventory("")
    variable_manager = VariableManager(loader=None, inventory=inventory)
    variable_manager._vars = {'hello': 'world'}
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)
    assert hostvars['localhost'] == {'hello': 'world'}



# Generated at 2022-06-22 12:16:15.394192
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible import context
    from ansible.parsing.dataloader import DataLoader

    # Setup the environment
    context.CLIARGS = Namespace(module_path=None)

    # Create the inventory, variable_manager, loader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    inventory._hosts_cache['localhost'] = dict(variable_manager.get_vars(host=inventory.get_host('localhost'), include_hostvars=True))

    hostvars = HostVars(inventory, variable_manager, loader)

# Generated at 2022-06-22 12:16:20.314600
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    import ansible.vars.manager
    vm = ansible.vars.manager.VariableManager()
    inventory = InventoryManager(vm, '/some/fake/path')
    hostvars = HostVars(inventory, vm, None)
    assert hostvars.__iter__() == inventory.hosts

# Generated at 2022-06-22 12:16:26.863632
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    play_source =  dict(
        name = "Ansible Play 0",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Hello World!'))),
        ]
    )

    loader = None
    options = None
    passwords = None
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-22 12:16:35.451800
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    hosts = ['localhost', 'dummy']
    inventory = InventoryManager(loader=DataLoader(), sources=','.join(hosts))
    variables = VariableManager()
    hv = HostVars(inventory, variables, get_all_plugin_loaders())
    hvv = hv.raw_get('dummy')
    assert(hvv.get('inventory_hostname') == 'dummy')


# Generated at 2022-06-22 12:16:45.537108
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from io import StringIO
    names = []
    inv = """
    [group]
    localhost
    """
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=StringIO(inv))
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    v = HostVars(inventory, variable_manager, loader)
    for i in v:
        names.append(i.name)
    assert names == ['localhost']


# Generated at 2022-06-22 12:16:52.946925
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager()
    vars = HostVars(inv, variable_manager, loader=loader)

    variable_manager.set_nonpersistent_facts(inv.get_host('localhost'), {'testing': 1})

    assert vars.raw_get('localhost') == {'testing': 1}

# Generated at 2022-06-22 12:17:05.076074
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inv_data = {
        'hostvars': {
            'foo': {
                'bar': 'baz',
                'bam': {
                    'buzz': 'buzzy',
                    'bad': 'not good'
                }
            }
        }
    }

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    inventory.load_data(inv_data)

    play_context = PlayContext()

    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-22 12:17:15.758994
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    # create group 'all'
    group1 = Group('all')
    group1.vars = {'g1_value': 'g1_value'}

    # create group 'group1'
    group2 = Group('group1')
    group2.vars = {'g2_value': 'g2_value'}

    # create group 'group2'
    group3 = Group('group2')

    # create host1
    host1 = Host('host1')

# Generated at 2022-06-22 12:17:32.277424
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))
    inventory.add_host(host='testhost')
    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=VariableManager(loader=loader))
    assert(hostvars.raw_get('testhost') == {})

    hostvars.raw_get('testhost')['test_variable'] = 'test_value'
    assert(hostvars.raw_get('testhost') == {'test_variable': 'test_value'})

# Generated at 2022-06-22 12:17:41.987593
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager


# Generated at 2022-06-22 12:17:53.676886
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(loader=None, sources='')
    variable_manager = DummyVariableManager()
    loader = DummyLoader()
    hostvars = HostVars(inventory, variable_manager, loader)
    expected_result = []
    assert list(hostvars.__iter__()) == expected_result

    inventory.hosts = [1, 2, 3]
    expected_result = [1, 2, 3]
    assert list(hostvars.__iter__()) == expected_result

    inventory.hosts = [1, 2, 3]
    inventory.hosts.reverse()
    expected_result = [1, 2, 3]
    assert list(hostvars.__iter__()) == expected_result


# Generated at 2022-06-22 12:17:58.967835
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # setup_mock_objects cannot be used here because the test suite is not designed
    # to be called with the arguments `setup_mock_objects(playbooks=['playbook1.yml'])`
    loader = DictDataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    loader.set_basedir('/etc/ansible')
    inventory.set_variable_manager(variable_manager)
    inventory._hosts_cache = {'host1': FakeHost(), 'host2': FakeHost()}
    inventory._patterns_cache = {}

# Generated at 2022-06-22 12:18:11.078950
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(None)

    HOST_VARS = {'red': {'a': 1, 'b': 2}, 'green': {'c': 3, 'd': 4}, 'blue': {'e': 5, 'f': 6}}
    hosts = {'red': Host('red', variable_manager=variable_manager, loader=loader),
             'green': Host('green', variable_manager=variable_manager, loader=loader),
             'blue': Host('blue', variable_manager=variable_manager, loader=loader)}


# Generated at 2022-06-22 12:18:18.155072
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    inventory = InventoryManager(loader=DataLoader())
    host = Host(name="testhost")
    host.set_variable("a", "some value")
    inventory.add_host(host)

    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    templar = Templar(loader=DataLoader(), variables=hostvars)

# Generated at 2022-06-22 12:18:29.421920
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create an inventory containing a host with a variable
    inventory = Inventory(loader=DataLoader())
    inventory.add_host(host='example')
    inventory.set_variable(host='example', var='name', value='example')

    # Create a variable_manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    # Create a HostVars object
    hostvars = HostVars(inventory, variable_manager, DataLoader())

    # Make a test:
    # Check if raw_get returns a value from inventory (the variable).
    # The value should not be expanded through the Templating engine

# Generated at 2022-06-22 12:18:36.675203
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    vars_cache = {
        'host-1': {},
        'host-2': {},
    }
    inventory = MockInventory(hosts=[
        'host-1',
        'host-2',
    ])

    vm = MockVariableManager(vars_cache)
    loader = MockLoader(vars={})

    hostvars = HostVars(inventory, vm, loader)
    assert set(hostvars) == {'host-1', 'host-2'}

# Generated at 2022-06-22 12:18:41.226139
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    inv = Inventory(host_list=[])
    vm = VariableManager(loader=None, inventory=inv)
    hv = HostVars(inventory=inv, variable_manager=vm, loader=None)

    for host in hv:
        pass



# Generated at 2022-06-22 12:18:46.202571
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    data = {
        'test': {
            'foo': '{{bar}}',
            'bar': '{{baz_dict.key}}',
            'baz_dict': {'key': 'value'},
            'baz_list': ['a', 'b', '{{c}}'],
            'c': 'd',
            'd': AnsibleUnsafeText('c'),
        },
    }

    class FakeLoader:
        def get_basedir(self, path):
            return None

        def path_dwim(self, path):
            return path

    class FakeInventory(dict):
        def get_host(self, host):
            from ansible.inventory.host import Host
            return Host(host)


# Generated at 2022-06-22 12:18:59.055182
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert HostVars.__getitem__.__doc__ == HostVars.__getitem__.__func__.__doc__

# Generated at 2022-06-22 12:19:10.170952
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.template import Templar
    class VariableManager:
        def __init__(self):
            self._vars_cache = {'template_result': 'test'}
        def get_vars(self, include_hostvars=True):
            return self._vars_cache
    class Play:
        def __init__(self):
            self._variable_manager = VariableManager()
    class Inventory:
        def __init__(self):
            self._loader = None
            self._variable_manager = VariableManager()
        def get_host(self, hostname='localhost'):
            if hostname == 'localhost':
                return Play()
            else:
                return None

# Generated at 2022-06-22 12:19:18.448679
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory_manager = InventoryManager(loader=None, sources='localhost')
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)
    hostvars = HostVars(inventory_manager, variable_manager, None)
    hostvars.set_nonpersistent_facts('localhost', { 'test_key': 'value1' })
    assert hostvars.raw_get('localhost')['test_key'] == 'value1'

# Generated at 2022-06-22 12:19:30.579147
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    vars_cache = {}
    inventory = None
    variable_manager = None
    loader = None
    hostvars = HostVars(inventory, variable_manager, loader)

    # test "return data" branch

    # setup
    loader = FakeLoader()
    hostvars._loader = loader
    hostvars._inventory = FakeInventory()
    hostvars._variable_manager = FakeVariableManager()
    hostvars._variable_manager._hostvars = hostvars
    hostvars._variable_manager._loader = loader
    hostvars._vars_cache = vars_cache
    hostvars._vars_cache[hostvars._find_host('foo')] = {'a': 'A'}

    # test
    assert hostvars['foo'] == {'a': 'A'}

    # test

# Generated at 2022-06-22 12:19:39.966028
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    play = Play().load({}, loader=loader, variable_manager=VariableManager(loader=loader, inventory=inventory))

    hostvars = HostVars(inventory, None, loader)
    assert repr(hostvars) == "{'localhost': 'localhost'}"

    play._variable_manager.set_host_variable('localhost', 'test_var', 'test_value')

    hostvars.set_variable_manager(play._variable_manager)

# Generated at 2022-06-22 12:19:51.542735
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        'inventory': """
        [local]
        localhost ansible_connection=local
        """,
    })
    inv = InventoryManager(loader=loader, sources='inventory')
    vars_manager = VariableManager(host_list=inv.hosts)

    hostvars = HostVars(inv, vars_manager, loader)

    hostvars_vars = hostvars['localhost']
    assert isinstance(hostvars_vars, Mapping)

    assert hostvars_vars['inventory_hostname'] == 'localhost'
    hostvars_vars['inventory_hostname'] = 'otherhost'

# Generated at 2022-06-22 12:20:03.324794
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host

    #
    # Data
    #
    ds = {
        'hosts': ['host.example.com', 'host2.example.com'],
        'vars': {
            'foo': {
                'a': 'b',
                'c': 1,
            }
        },
        '_meta': {
            'hostvars': {
                'host.example.com': {
                    'var1': '{{ foo.a }}',
                },
            }
        }
    }

    #
    # Test
   

# Generated at 2022-06-22 12:20:06.043296
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    hv = HostVars({'a': 'b'})
    assert hv.get('a') == 'b'
    assert hv.get('b') == AnsibleUndefined

# Generated at 2022-06-22 12:20:17.160338
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    from copy import deepcopy

    from ansible.plugins.loader import vars_loader
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    templar = Templar(loader=dataloader)
    inventory = InventoryManager(dataloader=dataloader, sources='localhost,')
    hostvars = HostVars(inventory=inventory, variable_manager=VariableManager(loader=dataloader), loader=dataloader)

    host = inventory.get_host('localhost')
    hostvars.set_host_facts(host=host, facts=dict(foo="bar"))

    # Check that __getitem__ returns

# Generated at 2022-06-22 12:20:24.603943
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    path = './test/units/vars/hostvars/hosts'
    inventory = InventoryManager(loader=loader, sources=path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars_iter = iter(hostvars)
    assert(next(hostvars_iter) == 'redis')

# Generated at 2022-06-22 12:20:56.273637
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pytest

    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import add_all_plugin_dirs

    loaders = get_all_plugin_loaders()
    if not loaders:
        add_all_plugin_dirs()

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    # check on hosts
    assert 'localhost' in host_vars

# Generated at 2022-06-22 12:21:03.651894
# Unit test for method __setstate__ of class HostVars

# Generated at 2022-06-22 12:21:12.134606
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible import constants as C
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # Setup
    inventory = ['localhost']
    host_name = 'localhost'
    host = Host(name=host_name)
    play_context = PlayContext()
    fake_loader = lambda *args: dict()
    variable_manager = VariableManager(loader=fake_loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, fake_loader)

    # Test: ansible_play_hosts is not returned because it is defined as static_var
    expected_hostvars = dict()

# Generated at 2022-06-22 12:21:20.592437
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import pytest
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

    localhost = inventory.get_host('localhost')
    variable_manager.set_host_variable(localhost, 'foo', '1')

    hostvars = HostVars(inventory, variable_manager, loader)
    assert repr(hostvars) == "{'localhost': {'foo': '1'}}"

    variable_manager.set_host_variable(localhost, 'foo', None)


# Generated at 2022-06-22 12:21:21.120059
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert True

# Generated at 2022-06-22 12:21:30.510993
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._loader = loader
    variable_manager._inventory = Inventory(loader, variable_manager, 'localhost,')

    variable_manager.set_host_variable('localhost', 'foo', 'bar')
    hostvars = HostVars(inventory=variable_manager._inventory, variable_manager=variable_manager, loader=loader)

    assert 'foo' in hostvars.raw_get('localhost')
    assert 'bar' == hostvars.raw_get('localhost')['foo']


# Generated at 2022-06-22 12:21:32.508229
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    variables = dict(a='a', b='b', c='c')
    x = HostVarsVars(variables, None)
    assert list(x) == list(variables)


# Generated at 2022-06-22 12:21:42.327028
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.playbook.vars
    import ansible.playbook.inventory
    import ansible.constants as C
    import ansible.template
    import ansible.utils.template

    class Inventory_hostname_short(object):
        def __init__(self, hostname):
            self.hostname = hostname

    class Groups(object):
        def __init__(self, name):
            self.name = name

    class Inventory_host(object):
        def __init__(self, hostname):
            self.name = hostname
            self.groups = [Groups(name=hostname)]
            self.hostname_short = Inventory_hostname_short(hostname=hostname)

    inventory = ansible.playbook.inventory.Inventory(host_list=[])

# Generated at 2022-06-22 12:21:54.854548
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    varmanager = VariableManager(loader=loader, inventory=inventory)
    inventory.clear_pattern_cache()

    hostvars = HostVars(inventory=inventory, variable_manager=varmanager, loader=loader)
    host = hostvars._find_host("localhost")
    assert(host is not None)

    # set a simple variable "foo" in the variables of host
    varmanager.set_host_variable(host=host, varname='foo', value='bar')

    # get the variables of the host


# Generated at 2022-06-22 12:22:04.275325
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    vars_manager = VariableManager()

    inventory_path = 'tests/inventory/hostvars_inventory.ini'
    loader = AnsibleLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_path)

    hostvars = HostVars(inventory=inventory, variable_manager=vars_manager, loader=loader)

    assert hostvars.raw_get('group1_host1') == {'var1': 123, 'var2': 'value2'}
    assert hostvars.raw_get('group2_host2') == {'var1': 123, 'var2': 'value2'}

# Generated at 2022-06-22 12:22:51.084324
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    #
    # Shared setup for tests
    #
    from ansible.parsing.splitter import parse_kv
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import inventory_loader

    inventory = InventoryManager(loader=inventory_loader, sources=None)
    vars = VariableManager()
    vars._hostvars = HostVars(inventory, vars, None)
    vars._extra_vars = {}

    vars.add_host_vars("localhost", {"name": "localhost"})

    #
    # Test for HostVars.raw_get
    #

    # Missing 'localhost' should return value of missing()
   

# Generated at 2022-06-22 12:23:00.138256
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.plugins import runner
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variables = {"version": "1.0", "server": "localhost"}
    hosts = []
    host = Host(name='localhost')
    host.set_variable('version', '2.0')
    host.set_variable('server', '127.0.0.1')
    hosts.append(host)
    groups = {}
    group = Group('all')
    group.add_host(host)
    groups['all'] = group
    inventory = runner.Inventory(host_list=hosts, group_list=groups)
    variable_manager = runner.VariableManager()
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = variables


# Generated at 2022-06-22 12:23:06.877737
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from collections import Mapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    mock_inventory_manager = InventoryManager(loader=DataLoader(), sources='')
    mock_variable_manager = VariableManager(loader=DataLoader(), inventory=mock_inventory_manager)
    mock_template_loader = DataLoader()

    hostvars = HostVars(inventory=mock_inventory_manager, variable_manager=mock_variable_manager, loader=mock_template_loader)
    assert isinstance(hostvars, Mapping)

# Generated at 2022-06-22 12:23:18.650420
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    inventory = Inventory(host_list=[])
    variable_manager = VariableManager()
    loader = DataLoader()

    hv = HostVars(inventory, variable_manager, loader)

    inventory.add_host(host="host1")
    inventory.add_host(host="host2")


# Generated at 2022-06-22 12:23:26.536092
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    inventory = InventoryManager(loader=DataLoader(), sources=["127.0.0.1"])
    variable_manager = VariableManager()
    variable_manager._loader = inventory._loader
    play_context = PlayContext()

    # Empty vars
    hostvars = HostVars(inventory, variable_manager, inventory._loader)
    assert repr(hostvars) == "{'127.0.0.1': {}}"

    # Non-empty vars
    variable_manager._vars_per_host = {'127.0.0.1': {'foo': 'bar'}}
   

# Generated at 2022-06-22 12:23:38.795542
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import pytest
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-22 12:23:44.078832
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager, DataLoader

    ds = {}  # Dummy State

    vm = VariableManager()
    ds['_variable_manager'] = vm

    hv = HostVars(Inventory(loader=DataLoader(), variable_manager=vm), vm, DataLoader())
    ds['_hostvars'] = hv
    
    hv.__setstate__(ds)
    assert(vm._loader is not None)
    assert(vm._hostvars is not None)
    assert(vm._hostvars is hv)

# Generated at 2022-06-22 12:23:54.292065
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    class Inventory(object):
        def __init__(self, loader):
            self._loader = loader

        def get_host(self, host_name):
            return self.HOST(host_name, loader=self._loader)

    class HostVarsVariableManager(object):
        def __init__(self, loader):
            self._loader = loader

        def get_vars(self, host, include_hostvars=True):
            return dict(foo=1)

    class HOST(object):
        def __init__(self, name, loader):
            self.name = name
            self._loader = loader

    hv = HostVars(Inventory(None), HostVarsVariableManager(None), None)
    assert hv.raw_get('whatever') == dict(foo=1)

# Generated at 2022-06-22 12:24:05.171281
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Use monkeypatch to hide import error
    import sys
    import os
    sys.modules['_yaml'] = None

    # Test vars_cache
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    inventory.set_playbook_basedir(os.getcwd())
    inventory.add_group('mygroup')
    inventory.add_host(host='myhost1')
    inventory.add_host(host='myhost2')
    host1 = inventory.get_host('myhost1')
    host1.set_variable('foo', 'bar')