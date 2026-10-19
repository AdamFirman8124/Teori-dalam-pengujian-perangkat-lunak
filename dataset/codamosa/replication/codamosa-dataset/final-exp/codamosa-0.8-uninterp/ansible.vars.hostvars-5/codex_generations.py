

# Generated at 2022-06-22 12:14:17.694222
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # TODO: write unit test
    pass


# Generated at 2022-06-22 12:14:23.182742
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    var_manager = VariableManager(loader=loader)

    hostvars = HostVars(inventory, var_manager, loader)
    assert hostvars['localhost'] == dict(inventory_hostname='localhost', inventory_hostname_short='localhost')

# Generated at 2022-06-22 12:14:30.683503
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    hostvars = {}
    hostvars['localhost'] = {'inventory_dir': '.', 'inventory_file': './hosts'}

    hvv = HostVarsVars(hostvars['localhost'], None)
    hvv_iter = iter(hvv)
    assert hostvars['localhost'].keys() == [x for x in hvv_iter]

    hvv = HostVarsVars(hostvars, None)
    hvv_iter = iter(hvv['localhost'])
    assert hostvars['localhost'].keys() == [x for x in hvv_iter]

# Generated at 2022-06-22 12:14:40.937927
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,'])
    variable_manager = VariableManager(loader=None, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, None)

# Generated at 2022-06-22 12:14:51.710621
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    inv = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inv)
    context = PlayContext()
    variable_manager.set_play_context(context)

    hostvars = HostVars(inv, variable_manager, None)

    assert hostvars.raw_get('localhost') == {'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost', 'groups': [], 'group_names': [], 'omit': '__omit_place_holder__'}

# Generated at 2022-06-22 12:15:01.198255
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    inventory_path = '/path/to/inventory'
    mock_inventory = create_autospec(InventoryManager(inventory=inventory_path))
    mock_variable_manager = create_autospec(VariableManager())
    mock_loader = create_autospec(DataLoader())
    hostvars = HostVars(mock_inventory, mock_variable_manager, mock_loader)

    mock_host_1 = create_autospec(Host('host1'))
    mock_host_2 = create_autospec(Host('host2'))
    mock_inventory.hosts = [mock_host_1, mock_host_2]
    output = list(hostvars)
    expected_output = [mock_host_1, mock_host_2]

    assert output == expected_output

# Generated at 2022-06-22 12:15:02.878426
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    pass

# Generated at 2022-06-22 12:15:11.704760
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import sys
    import os
    import unittest
    import tempfile
    import shutil
    import json

    from ansible.parsing import DataLoader
    from ansible.plugins.inventory import InventoryModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    class TestInventoryModule(InventoryModule):
        ''' Return a static inventory '''
        def verify_file(self, path):
            ''' always valid '''
            return True

        def parse(self, inventory, loader, path, cache=True):
            super(TestInventoryModule, self).parse(inventory, loader, path)
            host1 = inventory.add_host('host1')
            host2 = inventory.add_host('host2')
            group1 = inventory.add_group('group1')

# Generated at 2022-06-22 12:15:24.375146
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    # HostVarsVars is a proxy for variables.
    # Templating of variables using Standard variables must not be a part of HostVarsVars.
    # The test verifies that HostVarsVars can handle templating errors and iterate over all
    # variables, even if some of them are incorrectly templated.

    # ansible_connection is templated using ansible_ssh_private_key_file as Standard variables.
    host = Host(vars={'ansible_connection': '{{ ansible_ssh_private_key_file }}'})

    # ansible_ssh_private_key_

# Generated at 2022-06-22 12:15:34.974853
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.vars.hostvars import HostVars
    from ansible.plugins.loader import add_all_plugin_dirs

    loader = DataLoader()
    all_plugin_dirs = add_all_plugin_dirs('')
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list='localhost')
    hostvars = HostVars(inventory, VariableManager(loader=loader), loader)

    assert hostvars.__class__.__name__ == 'HostVars'
    assert hostvars.__iter__() == iter(inventory.hosts)

# Generated at 2022-06-22 12:15:48.276786
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    vars_cache = {
        'test_host': {
            'test_var_1': 'ansible {{ inventory_hostname }}',
            'test_var_2': 'ansible {{ groups[0] }}',
            'test_var_3': 'ansible',
            'test_var_4': 'ansible {{ test.test_var_3 }}',
        }
    }

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'test': {
            'test_var_3': 'localhost',
        }
    }
    variable_manager._vars_cache = vars_cache

    inventory = Inventory

# Generated at 2022-06-22 12:15:57.442863
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():

    from ansible.playbook import Playbook
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inv = Inventory(host_list='tests/inventory')
    vm = VariableManager([])
    hv = HostVars(inv, vm, loader=None)
    hv_dict = dict(inv.hosts)
    hv_data = hv.__getstate__()
    hv.__setstate__(hv_data)
    hv_dict2 = dict(inv.hosts)

    # Verify that localhost was created and added to all hosts
    assert 'localhost' in hv_dict
    assert 'localhost' in hv_dict2
    assert hv_dict.keys() == hv_dict2.keys()

    # Pickle and unpickle object
    import pickle


# Generated at 2022-06-22 12:16:02.832282
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    vars = dict(a=1, b=dict(c=1))
    variables = HostVarsVars(vars, loader=None)
    assert variables['a'] == 1
    assert variables['b']['c'] == 1
    try:
        variables['c']
    except KeyError:
        assert True


# Generated at 2022-06-22 12:16:12.091317
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    inventory = _create_inventory()
    variable_manager = _create_variable_manager(inventory)
    loader = _create_loader(variable_manager)

    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars_vars = hostvars['localhost']

    hostvars_vars_iter = iter(hostvars_vars)
    hostvars_vars_keys = set(hostvars_vars_iter)

    assert hostvars_vars_keys == set(hostvars_vars)



# Generated at 2022-06-22 12:16:21.347327
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Load fixtures
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost,')
    variable_manager.set_inventory(inventory)

    # Create HostVars
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # Create variable mocks

# Generated at 2022-06-22 12:16:32.573693
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inventory = Inventory(
        loader=DataLoader(),
        variable_manager=VariableManager(),
        host_list=[
            'localhost',
            '127.0.0.1',
            'myhost',
        ],
    )

    hostvars = HostVars(
        inventory=inventory,
        variable_manager=inventory.variable_manager,
        loader=inventory._loader,
    )

    assert set(hostvars) == set(['localhost', '127.0.0.1', 'myhost'])
    assert set(hostvars.keys()) == set(['localhost', '127.0.0.1', 'myhost'])

# Generated at 2022-06-22 12:16:43.615406
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    # Test inventory
    class TestInventory():
        def __init__(self, groups=None, hosts=None):
            self.groups = groups if groups else {}
            self.hosts = hosts if hosts else {}

        def get_host(self, host_name):
            if host_name in self.hosts:
                return self.hosts[host_name]
            else:
                return None

    # Test host
    class TestHost():
        def __init__(self, name):
            self.name = name

    # Create inventory
    inventory = TestInventory()
    inventory.hosts = {
        'foo': TestHost('foo'),
        'bar': TestHost('bar'),
        'baz': TestHost('baz'),
    }

    # Create variable manager

# Generated at 2022-06-22 12:16:53.553713
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(omit=['127.0.0.1'])
    variable_manager._loader = loader
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    inventory.subset('all')
    variable_manager.set_inventory(inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # Test if setstate restored _loader and _hostvars to VariableManager
    assert hostvars._variable_manager._loader is loader

# Generated at 2022-06-22 12:17:05.761261
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    from ansible.module_utils.common.collections import ImmutableDict
    import os

    hostvars_dir = os.path.dirname(os.path.abspath(__file__))
    inventory_dir = os.path.dirname(hostvars_dir)
    data_loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=data_loader, sources=[os.path.join(inventory_dir, "test_inventory")])
    variable_manager.set_inventory(inventory_manager)
    variable_manager.extra_v

# Generated at 2022-06-22 12:17:15.251212
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        "hostvars.yaml": """
---
host1:
  var: testhost1
host2:
  var: testhost2
        """,
    })

    inventory = InventoryManager(loader=loader, sources=["hostvars.yaml"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # HostVars should have two hosts
    assert len(hostvars) == 2
    assert list(hostvars) == ["host1", "host2"]

# Generated at 2022-06-22 12:17:32.015148
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import sys

    if not sys.stdin.isatty():
        raise Exception('Raw get is only meant to be tested from the CLI')

    options = {'listhosts': False, 'listtasks': False, 'listtags': False, 'syntax': False, 'connection': 'local', 'module_path': '', 'forks': 10, 'become': False, 'become_method': None, 'become_user': None, 'check': False, 'diff': False}

# Generated at 2022-06-22 12:17:41.841007
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["localhost,"])
    variable_manager.set_inventory(inventory)
    context = PlayContext()
    context.CLIARGS = {}
    context.set_options({'inventory': inventory})
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

# Generated at 2022-06-22 12:17:53.951068
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Define a fake InventoryManager
    class FakeInventoryManager(InventoryManager):
        def __init__(self):
            self.hosts = ['host1', 'host2']

# Generated at 2022-06-22 12:18:05.858377
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Setup fixture
    import os
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    inventory_dir = os.path.join(current_dir, 'inventory')
    inventory = InventoryManager(loader=loader, sources=[inventory_dir])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # Test that HostVars returns AnsibleUndefined if host is not found

# Generated at 2022-06-22 12:18:15.188393
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()
    dl = DataLoader()
    im = InventoryManager(loader=dl)

    # Make sure that localhost is present
    im.add_host('localhost')

    vm = VariableManager(loader=dl, inventory=im)
    hv = HostVars(im, vm, dl)

    # Clean slate test - nothing has been done
    assert hv['localhost'] == {}

    # Set some vars on localhost

# Generated at 2022-06-22 12:18:17.756219
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    hv = HostVars()
    r = hv.__repr__()
    assert isinstance(r, str)
    assert len(r) > 0

# Generated at 2022-06-22 12:18:28.380492
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    # Expected
    expected = (
        'ansible_version',
        'ansible_play_hosts',
        'ansible_dependent_role_names',
        'ansible_play_role_names',
        'ansible_role_names',
        'inventory_hostname',
        'inventory_hostname_short',
        'inventory_file',
        'inventory_dir',
        'groups',
        'group_names',
        'omit',
        'playbook_dir',
        'play_hosts',
        'role_names',
        'ungrouped',
        'test_var',
        'test_var2'
    )

    # Setup vars

# Generated at 2022-06-22 12:18:40.198402
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    inv_manager = InventoryManager(loader=DataLoader(), sources=['test_iter', 'test_iter_dir'])
    inv_var_manager = VariableManager(loader=DataLoader(), inventory=inv_manager)

    host_vars = HostVars(inventory=inv_manager, variable_manager=inv_var_manager, loader=inv_var_manager._loader)
    host_vars.set_variable_manager(inv_var_manager)

    hosts_in_inventory = [Host(name=name) for name in ['host1', 'host2', 'host3']]

# Generated at 2022-06-22 12:18:45.108519
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class MockInventory():
        def __init__(self, host_name):
            self.host_name = host_name

        def get_host(self, host_name):
            if host_name == self.host_name:
                class MockHost():
                    def __init__(self, host_name):
                        self.host_name = host_name
                        self.vars = { "a" : "b" }
                return MockHost(host_name)
            else:
                return None

    class MockVariableManager():
        # Do not perform any initialization in constructor
        # so we can set _hostvars in test.
        def __init__(self):
            pass

        def get_vars(self, host=None, include_hostvars=False):
            if include_hostvars:
                return None


# Generated at 2022-06-22 12:18:53.320977
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import ansible.utils
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    class Null(object):
        def __init__(self, *args, **kwargs):
            self.vars = dict()

        def get_vars(self, loader, play, host, task):
            return self.vars

    class Inventory(Inventory):
        def __init__(self, loader, variable_manager):
            super(Inventory, self).__init__(loader=loader, variable_manager=variable_manager)
            self.hosts = dict()

        def get_host(self, name):
            if name in self.hosts:
                return self.hosts[name]

            return None

    class LoaderModule(object):
        def __init__(self):
            pass

    variable

# Generated at 2022-06-22 12:19:12.683507
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = Mock()
    loader.get_basedir.return_value = '/path/to/basedir/'

    inventory = InventoryManager(loader=loader, sources=['/path/to/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    hostvars._variable_manager._vars_cache = {'all': {'my_var': 'my_value'}}
    assert hostvars['localhost']['my_var'] == 'my_value'
    assert hostvars.raw_get('localhost') != 'my_value'

# Generated at 2022-06-22 12:19:24.102192
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import mock
    import os
    import sys

    # We need to force AnsibleUndefined to inherit from object under Python 3
    # otherwise this test will fail.
    if sys.version_info[0] == 3:
        super_new = AnsibleUndefined.__new__

        def __new__(cls, *args, **kwargs):
            return super_new(cls, object)

        AnsibleUndefined.__new__ = __new__

    class FakeVariableManager(object):
        def __init__(self, vars_cache):
            self._vars_cache = vars_cache

        def get_vars(self, host=None, include_hostvars=True):
            if host is None:
                return {'test_get_vars_None': 'test_get_vars_None'}

# Generated at 2022-06-22 12:19:36.048845
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from collections import namedtuple
    from ansible.parsing.yaml.loader import AnsibleLoader

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.invocation.play_context import PlayContext

    vars_manager = VariableManager()
    inventory = Inventory(loader=AnsibleLoader(''), variable_manager=vars_manager)
    play_context = PlayContext()
    play_context.vars_prompt = {}
    play_context.prompt = lambda x,y,z: "foo"
    play_context.remote_addr = ''
    play_context.connection = namedtuple("conn", ["host"])()
    play_context.network_os = 'linux'
    play_context.become = False

# Generated at 2022-06-22 12:19:46.109440
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import json
    import ansible
    import ansible.cli.adhoc
    import ansible.inventory
    import ansible.plugins.loader
    import ansible.vars
    import sys
    import tempfile
    import yaml

    # Create an inventory and add a host.
    inventory = ansible.inventory.Inventory(ansible.cli.adhoc.parse_cli_args([]).inventory)
    inventory.add_host(ansible.inventory.Host(name="localhost"))

    # Create a dummy callback plugin.
    class DummyCallback(object):
        def v2_runner_on_ok(self, result):
            print(json.dumps(result._result, indent=4, default=ansible._json_encoder))

    # Create a variable manager and load dummy data.
    variable_manager = ansible.v

# Generated at 2022-06-22 12:19:58.163592
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # test Ansible variable substitution with the `hostvars` variable
    assert_equals(HostVars({'k1': 'v1'}, 'localhost')['localhost']['k1'], 'v1')

    # test Ansible variable substitutions with more complex `hostvars` variable
    assert_equals(HostVars({'k1': 'v1', 'v2': {'k2': 'v2'}}, 'localhost')['localhost']['k1'], 'v1')
    assert_equals(HostVars({'k1': 'v1', 'v2': {'k2': 'v2'}}, 'localhost')['localhost']['v2']['k2'], 'v2')


# Generated at 2022-06-22 12:20:07.529311
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():

    from ansible import constants as C

    vars = dict(a=1, b=2, c=3)

    # Generate an empty new Ansible configuration
    config = C.Config(C.load_config_file())

    # Generate a new empty Ansible Inventory
    inventory = C.Inventory(loader=C.DataLoader(), variable_manager=C.VariableManager(config=config), host_list=[])

    # Generate a new empty Ansible VariableManager
    variable_manager = C.VariableManager(config=config, inventory=inventory)

    # Generate a new empty Ansible loader
    loader = C.DataLoader()

    # Generate a new HostVarsVars
    host_objects = HostVarsVars(vars, loader=loader)

    # Initialize an iter

# Generated at 2022-06-22 12:20:18.891068
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    class Inventory(object):
        def __init__(self):
            self.host_list = ["foo1", "foo2"]
            self.hosts = {
                "foo1": "bar1",
                "foo2": "bar2",
            }
            self.vars = {
                "foo1": "bar1",
                "foo2": "bar2",
            }

        def get_host(self, name):
            return self.hosts.get(name)

        def get_variables(self, name):
            return self.vars.get(name)

    class Loader(object):
        def __init__(self):
            self.files = None

        def set_basedir(self, basedir):
            pass

        def path_exists(self, path):
            pass


# Generated at 2022-06-22 12:20:22.437439
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    variables = { 'foo': 'foo', 'bar': 'bar' }
    loader = object()
    hvv = HostVarsVars(variables, loader)

    assert sorted(list(hvv)) == ['bar', 'foo']

# Generated at 2022-06-22 12:20:32.762196
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # The class HostVars is abstract, so we use a subclass, HostVarsVars,
    # to test __repr__ implementation. That implementation uses
    # Templar to get the representation of some variables, but Templar
    # can only be constructed with a loader. As we are only testing the
    # string representation, the loader will not be actually used, so we
    # just create a mock.
    class StringMock:
        def __init__(self, value): self.value = value
        def __str__(self): return self.value
    variables = {
        'foo': StringMock('{{ bar }}'),
        'bar': StringMock('{{ baz }}'),
        'baz': StringMock('baz'),
    }
    loader = StringMock('')

# Generated at 2022-06-22 12:20:43.153095
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class MockInventory(object):
        def __init__(self):
            self.hosts = ['host1', 'host2']
    class MockVariableManager(object):
        def __init__(self):
            self.__getitem__ = lambda self, key: {}
        def get_vars(self, *args):
            return {}
    import sys
    import copy_reg as copyreg
    from types import MethodType
    copyreg.pickle(MethodType, lambda f: (lambda self: self, f.__name__), 1)
    h = HostVars(MockInventory(), MockVariableManager(), loader=None)
    hostvars_iter = iter(h)
    # unfortunately, we can't do unittest.assertRaisesRegex since we want to
    # support Python 2.6

# Generated at 2022-06-22 12:21:01.552042
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Not ansible 2.8 compatible
    #import ansible.plugins.loader as plugin_loader
    #plugin_loader.add_directory('./plugins/inventory')

    loader = DataLoader()
    inventory_file = './inventory/hosts.static'
    inventory = InventoryManager(loader=loader, sources=inventory_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=variable_manager)

    assert hostvars.raw_get('test01')['ansible_ssh_host'] == '127.0.0.1'

    #

# Generated at 2022-06-22 12:21:11.636629
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import ansible.inventory
    import ansible.variable_manager
    import ansible.vars.hostvars
    import ansible.vars.vars_cache
    import ansible.parsing.dataloader

    loader = ansible.parsing.dataloader.DataLoader()
    inventory = ansible.inventory.Inventory(loader=loader)
    variable_manager = ansible.variable_manager.VariableManager(loader=loader, inventory=inventory)
    hostvars = ansible.vars.hostvars.HostVars(inventory, variable_manager, loader)

    inventory.get_host('foohost')

    raw_get = hostvars.raw_get('foohost')
    assert raw_get == ansible.vars.vars_cache.dump_cache_data('foohost')

# Generated at 2022-06-22 12:21:18.606348
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    playbook = Play()
    loader = DataLoader()
    variable_manager = VariableManager(loader)

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    hostvars_repr = repr(hostvars)
    assert isinstance(hostvars_repr, str)
    assert hostvars_repr == '{}'

# Generated at 2022-06-22 12:21:25.354794
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.manager import VariableManager

    inventory = lambda: None
    inventory.hosts = []
    inventory.hosts.append('host1')
    inventory.hosts.append('host2')

    hv = HostVars(inventory, VariableManager(), loader=None)
    hosts = list(hv)

    assert hosts == ['host1', 'host2']

# Generated at 2022-06-22 12:21:33.726612
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    loader = DictDataLoader({})

    # Test rendering of jinja2 variable when variable
    # is a string, an integer and a complex combination
    # of variables and strings

# Generated at 2022-06-22 12:21:37.395043
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    hostvars = HostVars({}, None, None)
    result = hostvars.raw_get("arbitrary_host")
    assert isinstance(result, AnsibleUndefined)

# Generated at 2022-06-22 12:21:44.746526
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    fake_loader = DictDataLoader({
        "vars/foo.yml": """
---
bar: bar
""",
        "vars/self.yml": """
---
self: "{{ ansible_play_hosts }}"
""",
        "hosts.yml": """
---
all:
  hosts:
    localhost:
    remotehost:
      ansible_host: 127.0.0.1
""",
    })
    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager())
    fake_inventory.parse_inventory(host_list=['localhost', 'remotehost'])
    fake_variable_manager = VariableManager(loader=fake_loader)

# Generated at 2022-06-22 12:21:56.746703
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    class TestInventory(dict):
        def __getitem__(self, host):
            return self.get(host, {})
        def iter(self):
            return self.__iter__()

    class TestVariableManager():
        def __init__(self):
            self._vars_cache = {
                'inventory1': {
                },
                'inventory2': {
                },
                'inventory3': {
                },
                'inventory4': {
                },
                'localhost': {
                },
            }

    loader = DictDataLoader({})
    test_inventory = TestInventory()
    test_variable_manager = TestVariableManager()
    test_object = HostVars(test_inventory, test_variable_manager, loader)
    assert test_object._variable_manager == test_variable_manager
    assert test

# Generated at 2022-06-22 12:22:05.597213
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inv_dir = os.path.dirname(__file__) + os.path.sep + 'dummy_inv'
    host_file = os.path.join(inv_dir, 'hosts')

    # Create inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[host_file])

    # Create variable manager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create HostVars
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager,
                        loader=loader)

    # Tests for method __getitem__
    host = variable_manager.get_host('host1')
    fp = BytesIO

# Generated at 2022-06-22 12:22:12.017227
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    INVENTORY = """
        localhost ansible_connection=local
    """

    def filter_bash_history(data):
        ''' filter-out bash history from ansible facts '''
        if isinstance(data, dict):
            for k in data.keys():
                if k.endswith('_history'):
                    del data[k]
        return data

    # Create the inventory, with host localhost
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=INVENTORY)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Fake localhost

# Generated at 2022-06-22 12:22:45.061801
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost:1')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-22 12:22:56.812990
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    hostvars = HostVars(inventory, variable_manager, loader)

    variable_manager.set_inventory(inventory)

    inventory.add_group('group1')
    inventory.add_group('group2')
    inventory.add_group('group3')

    inventory.add_host(Host('localhost'))
    inventory.add_host(Host('host1'))
    inventory.add_host(Host('host2'))
    inventory.add_host(Host('host3'))

    variable_manager.set_host_variable

# Generated at 2022-06-22 12:23:02.891272
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Host
    hvars = HostVars({}, {}, {})
    hvars._inventory = {
        'hosts': [
            Host(name='foobar'),
            Host(name='abc'),
            Host(name='xyz'),
        ]
    }
    assert sorted(list(hvars.__iter__())) == ['abc', 'foobar', 'xyz']



# Generated at 2022-06-22 12:23:14.699340
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import sys
    import imp
    import os
    from ansible.constants import DEFAULT_HOST_LIST

    lib_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lib'))
    if lib_path not in sys.path:
        sys.path.append(lib_path)

    variable_manager = imp.load_source('ansible.vars.variable_manager', os.path.join(lib_path, 'ansible', 'vars', 'variable_manager.py'))

# Generated at 2022-06-22 12:23:24.707856
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.manager import VariableManager

    class Host:
        def __init__(self, name):
            self._name = name
            self._vars = dict()

        def get_name(self):
            return self._name

        def set_variable(self, k, v):
            self._vars[k] = v

        def get_vars(self):
            return self._vars

    class Inventory:
        _hosts = None

        def __init__(self, hosts):
            self._hosts = hosts

        def get_host(self, hostname):
            for host in self._hosts:
                if hostname == host.get_name():
                    return host
            return None

    class DummyLoader:
        def __init__(self):
            pass


# Generated at 2022-06-22 12:23:35.725476
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    variables = dict(a=1, b=2, c=3)
    play = Play().load({'hosts': 'local', 'vars': variables}, variable_manager=None, loader=None)
    inventory = InventoryManager(loader=None, sources='localhost,')
    hostvars = HostVars(inventory=inventory, variable_manager=None, loader=None)

    def test():
        play._variable_manager = play.set_variable_manager(play.get_variable_manager())
        play._variable_manager._hostvars = hostvars
        assert repr(hostvars) == repr(variables)

    test()

# Generated at 2022-06-22 12:23:46.786582
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    def _load_fixture(fixture_name):
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager

        loader = DataLoader()
        variable_manager = VariableManager()

        path = os.path.join(os.path.dirname(__file__), 'fixtures', fixture_name)
        return load_fixture(path, loader=loader, variable_manager=variable_manager)

    def _set_host_variable(hostvars, host, varname, value):
        hostvars.set_host_variable(host, varname, value)

    def _set_nonpersistent_facts(hostvars, host, facts):
        hostvars.set_nonpersistent_facts(host, facts)

    hostvars = _load_fixture

# Generated at 2022-06-22 12:23:55.341950
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='127.0.0.1,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:23:58.524756
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    assert tuple(HostVars({}, None, None)) == tuple()
    assert tuple(HostVars({'x': {}, 'y': {}}, None, None)) == ('x', 'y')

# Generated at 2022-06-22 12:24:09.335796
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display

    display = Display()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(
        inventory=inventory,
        loader=loader,
        variable_manager=variable_manager
    )

    print("\n# Unit test for method __repr__ of class HostVars")

    print("\nExpected output:\n{\"localhost\": {\"foo\": \"bar\", \"baz\": \"boo\"}}")