

# Generated at 2022-06-22 12:14:17.590625
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert False, "not implemented"


# Generated at 2022-06-22 12:14:22.678636
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import mock

    hv = HostVars(None, None, None)
    assert hasattr(hv, '_inventory')
    assert hasattr(hv, '_loader')
    assert hasattr(hv, '_variable_manager')

    inventory_mock = mock.Mock()
    hv._inventory = inventory_mock
    assert iter(hv) == iter(inventory_mock.hosts)


# Generated at 2022-06-22 12:14:32.099109
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # Do not allow use of HostVars without passing inventory and variable_manager
    HostVars(None, None, None)
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['all'])
    playbook = Play().load({}, variable_manager=variable_manager, loader=loader)
    variable_manager.set_inventory(inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    # Create two hosts (one already exists in inventory)
    host = inventory.get_host('all')
    host

# Generated at 2022-06-22 12:14:36.352449
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # Importing the module is needed because the module is not imported
    # by the main program, the main program imports only the classes defined
    # in this module.
    from ansible.vars.hostvars import HostVars

    hostvars = HostVars({})
    repr(hostvars)

# Generated at 2022-06-22 12:14:45.908332
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # Mocking inventory and variable manager
    inventory = MockInventory()
    variable_manager = MockVariableManager()

    # Mocking hostvars
    hv = HostVars(inventory, variable_manager, loader=None)

    # Asserting the returned "hostvars" value is the expected
    assert hv.raw_get("host1") == {'var1': '1', 'var2': '2'}
    assert hv.raw_get("host2") == {'var1': '10'}
    assert hv.raw_get("host3") == AnsibleUndefined(name="hostvars['host3']")



# Generated at 2022-06-22 12:14:57.302407
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    hosts = """
    [group]
    host1
    host2
    """

    loader = DictDataLoader({
        "hosts": hosts
    })

    inventory = InventoryManager(loader=loader, variable_manager=VariableManager())

    play = Play().load(dict(
        hosts='group',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='Hello World')))
        ]
    ), variable_manager=inventory.get_variable_manager(), loader=loader)


# Generated at 2022-06-22 12:15:04.306631
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager([], loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host_vars_object = HostVars(inventory, variable_manager, loader)

    undefined_result = host_vars_object.raw_get('localhost')

    assert undefined_result == AnsibleUndefined(name="hostvars['localhost']")

# Generated at 2022-06-22 12:15:08.341829
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    h = HostVarsVars({'1': 1, '2': 2}, None)
    assert hasattr(h, '__iter__')
    # The next line will fail if HostVarsVars.__iter__ does not
    # return an iterator.
    list(h)

# Generated at 2022-06-22 12:15:08.925762
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    assert True

# Generated at 2022-06-22 12:15:22.156207
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    play = Play.load(dict(
        name="Ansible Play",
        hosts=['localhost'],
        gather_facts='no',
        roles=[],
        tasks=[
            dict(action=dict(module='debug', args=dict(msg="{{ hostvars['localhost']['foo'] }}"))),
        ]
    ), loader=loader)

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(play.hosts[0], dict(foo='bar'))

    hostvars = HostVars(play.get_variable_manager()._inventory, variable_manager, loader)


# Generated at 2022-06-22 12:15:35.272794
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    inventory = AnsibleInventory(loader=None)
    host = AnsibleHost(name='test-host', port=1234, variables=dict(var='value'))
    inventory.add_host(host)
    host_vars = HostVars(inventory, VariableManager(), loader=None)

    # In python2, repr() works differently for objects of new-style and
    # old-style classes. This makes unit tests fail. The following code
    # converts HostVars to new-style class.
    host_vars.__class__ = type('HostVarsNewStyle',
                               (host_vars.__class__, object),
                               {})

    host_vars_repr = repr(host_vars)
    assert isinstance(host_vars_repr, str)
    # When 'test-host'

# Generated at 2022-06-22 12:15:44.855585
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    class Host:
        def __init__(self, id):
            self.id = id

        def get_name(self):
            return self.id

    class Inventory:
        def __init__(self):
            self._hosts = dict()

        def _add_host(self, host):
            self._hosts[host.get_name()] = host

        def get_host(self, host_name):
            return self._hosts.get(host_name)

        def __contains__(self, host_name):
            return (host_name in self._hosts)

        def __iter__(self):
            for host in self._hosts:
                yield host

        def __len__(self):
            return len(self._hosts.keys())


# Generated at 2022-06-22 12:15:55.140472
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    hostvars = HostVars(None, variable_manager, loader)
    variables = {
        'foo': '{{bar}}',
        'bar': '{{baz}}',
        'baz': 'foobar',
    }
    variable_manager.update_vars(variables)
    assert hostvars['localhost'] == variables
    variables['bar'] = '{{bazbar}}'
    variable_manager.update_vars(variables)
    assert hostvars.raw_get('localhost') == variables

# Generated at 2022-06-22 12:16:01.125249
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = inventory.get_variable_manager()

    hostvars = HostVars(inventory, variable_manager, loader)

    hostname = 'localhost'
    assert repr(hostvars[hostname]) == repr(hostvars.raw_get(hostname))
    assert repr(hostvars.raw_get(hostname)) == repr({})
    assert repr(hostvars) == repr({hostname: {}})


# Generated at 2022-06-22 12:16:04.582326
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible import constants as C
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[C.DEFAULT_HOST_LIST])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)
    variables = hostvars.raw_get(inventory_hostname)
    assert variables is not None

# Generated at 2022-06-22 12:16:16.256798
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    # Just a dummy object to satisfy the constructor
    class DummyObject:
        pass

    # Just a dummy method to satisfy the constructor
    def dummy_method(*args, **kwargs):
        return None

    def test_raw_get_when_hostvars_is_defined():
        # Prepare the mock
        inventory = DummyObject()
        inventory.data = {'_meta': {'hostvars': {'localhost': {}}}}
        inventory.get_host = dummy_method

        # Execute the code to test
        hostvars = HostVars(loaders=[], inventory=inventory, variable_manager=None)
        result = hostvars.raw_get('localhost')

        # Check the result
        assert isinstance(result, dict)


# Generated at 2022-06-22 12:16:25.736776
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # pylint: disable=too-few-public-methods
    class FakeLoader:
        def __init__(self, **kwargs):
            pass

        def set_basedir(self, path):
            pass
    # pylint: enable=too-few-public-methods

    class FakeInventory:
        def __init__(self, **kwargs):
            pass

        def get_host(self, host_name):
            return host_name

        def get_host(self, host_name):
            if host_name == 'test_host':
                return 'test_host'
            return None

        def __repr__(self):
            return "FakeInventory"

    # pylint: disable=too-few-public-methods

# Generated at 2022-06-22 12:16:36.439238
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    inventory = 'localhost ansible_connection=local'
    vm = '''
    [all:vars]
    a = 1
    b =
      - 1
      - 2
    c =
      hello: world
      number: 42
    d =
      - hello: world
        number: 42
    '''
    vars_files = '''
    ---
    a: 42
    shallow_copy:
      list:
        - name: foo
          value: bar
    deep_copy:
      list:
        - name: foo
          value: bar
    '''
    # Expected data

# Generated at 2022-06-22 12:16:42.806420
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # tasks/main.yml
    # - hosts: localhost
    #   vars:
    #     myvar: abc
    #   tasks:
    #     - debug: msg="{{ hostvars[inventory_hostname] }}"
    #
    # => this test checks if method __getitem__ of class HostVars returns a
    #    HostVarsVars instance with the value of task hostvars[inventory_hostname]
    #

    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-22 12:16:45.140841
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    hv = HostVars({'foo': 'bar'}, None, None)
    assert list(hv) == ['foo']

# Generated at 2022-06-22 12:17:00.678698
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    '''
    Test __getitem__ of HostVars() when:

    1) Inventory is empty
    2) Inventory contains one host with empty vars and complex structure of static vars.
    '''

    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.variables import VariableManager

    loader = DictDataLoader({})

    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    # test with empty inventory
    assert hostvars[''].get('ansible_play_hosts', None) is None

# Generated at 2022-06-22 12:17:11.942128
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVarsVars
    import types
    import sys

    # Initialize a HostVars object
    vars_cache = {'foo': 'bar'}
    loader = lambda : None
    inventory = None
    variable_manager = UnsafeProxy({}, {}, {}, loader)
    hostvars = HostVars(inventory, variable_manager, loader)

    # Execute __repr__
    result = repr(hostvars)

    # Check the result

# Generated at 2022-06-22 12:17:20.609104
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vv = HostVarsVars({'foo': 'bar'}, loader=None)
    assert vv['foo'] == 'bar'
    assert vv._loader is None

    vv = HostVarsVars({'foo': AnsibleVaultEncryptedUnicode('bar')}, loader=None)
    assert vv['foo'] == 'bar'
    assert vv._loader is None
    assert isinstance(vv['foo'], AnsibleVaultEncryptedUnicode)

    vv = HostVarsVars({'foo': 'bar'}, loader=None)
    templar = Templar(loader=None)


# Generated at 2022-06-22 12:17:26.558936
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(["tests/inventory"])
    variable_manager = InventoryVariableManager(inventory)
    hostvars = HostVars(inventory, variable_manager, None)
    hostvars.__getitem__ = lambda host: {}
    assert len(list(hostvars)) == 6


# Generated at 2022-06-22 12:17:37.366774
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    class Inventory:
        def __init__(self):
            self.pattern_cache = {}
            self.hosts = ['localhost']
            self.cache = {}

        def get_host(self, host_name):
            if host_name in self.cache:
                return self.cache[host_name]

            h = Host(host_name)
            self.cache[host_name] = h
            return h

    class Host:
        def __init__(self, name):
            self.name = name
            self.vars = {}

    class Loader:
        pass

    class VariableManager:
        def __init__(self):
            self._hostvars = None
            self.loader = Loader()


# Generated at 2022-06-22 12:17:45.828826
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Checking HostVars.__getitem__ returns a HostVarsVars instance
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory
    from ansible.vars import VariableManager
    from ansible.inventory import Host
    from collections import MutableMapping

    hosts = {'host1': {'hostname': 'host1', 'vars': {'foo': 'bar'}},
             'host2': {'hostname': 'host2', 'vars': {'foo': 'bar'}},
             'host3': {'hostname': 'host3', 'vars': {'foo': 'bar'}}}

    # Creating an inventory
    inventory = MockInventory()
    loader = DictDataLoader({})

    for host_name in hosts.keys():
        host

# Generated at 2022-06-22 12:17:57.587976
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    inventory = InventoryManager(loader=DataLoader(), sources=[])
    inventory._hosts_cache['host1'] = Host('host1')
    inventory._hosts_cache['host2'] = Host('host2')

    ho = HostVars(inventory=inventory, variable_manager=VariableManager(), loader=DataLoader())
    assert set(ho) == {'host1', 'host2'}

    # Check that method __iter__ is not implemented in parent class Mapping
    #

# Generated at 2022-06-22 12:18:09.953770
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])

    hostvars = HostVars(inventory, variable_manager, loader)

    host = Host(name="test")
    variable_manager.set_host_variable(host, "foo", "bar")
    variable_manager.set_host_variable(host, "baz", "quux")
    variable_manager.set_host_variable(host, "list", ["a", "b", "c"])

# Generated at 2022-06-22 12:18:20.027225
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    groups = dict(
        group1=dict(
            hosts=dict(test1=dict()),
            vars=dict(ansible_user='root'),
            children=dict(
                group3=dict(
                    hosts=dict(test3=dict()),
                    vars=dict(ansible_user='john'),
                    children=dict(
                        group4=dict(
                            hosts=dict(test4=dict()),
                            vars=dict(ansible_user='jane'),
                        )
                    )
                )
            )
        ),
        group2=dict(
            hosts=dict(test2=dict()),
            vars=dict(ansible_user='user'),
        )
    )


# Generated at 2022-06-22 12:18:31.761077
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import unittest
    import json

    import ansible.playbook

    from ansible.constants import DEFAULT_HOST_LIST

    class TestHostVars(unittest.TestCase):

        def test___repr__(self):
            # Setup
            inventory = ansible.inventory.Inventory(DEFAULT_HOST_LIST)
            variable_manager = ansible.vars.VariableManager()
            datasource = ansible.playbook.play_source.TaskDatasource()
            loader = ansible.parsing.dataloader.DataLoader()
            for host in inventory.hosts:
                variable_manager.set_host_variable(host, 'foo', 'bar')
                variable_manager.set_host_variable(host, 'test_a', 'a')
                variable_manager.set_host_

# Generated at 2022-06-22 12:18:44.480054
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import os
    import sys
    import json
    import copy
    import unittest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six import iteritems
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Group
    from ansible.template import Templar
    from ansible.template import Jinja2TemplateModule
    from six import string_types

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common._collections_compat.abc import MutableMapping

    loader = DataLoader()

# Generated at 2022-06-22 12:18:52.960659
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars[('hostvars', 'localhost')]['foo'] = 'bar'
    variable_manager.extra_vars[('hostvars', 'localhost')]['wiz'] = 'bang'
    variable_manager.extra_vars[('hostvars', 'localhost')]['ansible_all_ipv4_addresses'] = 'foo'
    variable_manager.extra_vars[('hostvars', 'localhost')]['ansible_all_ipv6_addresses'] = 'foo'
    variable_manager.extra_vars[('hostvars', 'localhost')]['ansible_default_ipv4'] = 'foo'

# Generated at 2022-06-22 12:18:59.443487
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # AnsibleUndefined should not be templated in __repr__
    data = {'foo': 'bar', 'baz': AnsibleUndefined('dummy')}
    hostvars = HostVarsVars(data, loader=None)
    assert repr(data) == repr(hostvars)

# Generated at 2022-06-22 12:19:10.375172
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Play().load(loader=loader, variable_manager=variable_manager, use_handlers=False)
    hostvars = HostVars(inventory, variable_manager, loader)
    assert hostvars._variable_manager._hostvars is hostvars
    assert hostvars._loader is loader

    state = hostvars.__getstate__()
    del state['_variable_manager']
    hostvars.__setstate__(state)
    assert hostvars._variable_manager._hostvars is hostv

# Generated at 2022-06-22 12:19:21.931989
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory_path = 'tests/inventory/host_vars_iter'

    # Create inventory instance
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_path)
    assert len(inventory.hosts) == 6

    variables = {'var1': 1, 'inventory_hostname': 'localhost'}
    hostvars = HostVars(inventory, variables=variables, loader=loader)

    hostnames = []
    for host in hostvars:
        hostnames.append(host.name)
    assert len(hostnames) == 6

    # Create hostvars and fill some variables
    hostvars_1 = hostvars['group1_host1']
    hostv

# Generated at 2022-06-22 12:19:32.160719
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # hostvars.raw_get('localhost') is Equivalent to hostvars.raw_get(u'localhost')
    assert hostvars.raw_get('localhost') == hostvars.raw_get(u'localhost')

# Generated at 2022-06-22 12:19:35.620866
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    res = HostVars(None, None, None).__repr__()
    import re
    assert re.match('^{}$', res)


__all__.extend(['test_HostVars___repr__'])

# Generated at 2022-06-22 12:19:45.798453
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    class FakeInventory():
        def get_host(self, host_name):
            return None

    class FakeVariableManager():
        def get_vars(self, host, include_hostvars):
            return {'k1': 'v1'}

    inventory = FakeInventory()
    loader = None
    variable_manager = FakeVariableManager()

    hostvars = HostVars(inventory, variable_manager, loader)
    # Since host 'h1' does not exist in inventory, HostVars should return
    # AnsibleUndefined
    assert hostvars['h1'] == AnsibleUndefined(name="hostvars['h1']")

    class FakeHost():
        def __init__(self, host_name):
            self.name = host_name


# Generated at 2022-06-22 12:19:57.455427
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    # Fakes
    class FakeInventory(object):
        def __init__(self):
            self.hosts = ['localhost', 'otherhost']

        def get_host(self, host_name):
            if host_name in self.hosts:
                return type('Host', (), dict(name=host_name))
            else:
                return None

    class FakeVariableManager(object):
        def __init__(self):
            self.host_vars_files = {}
            self.host_vars_files['localhost'] = 'fake_hostvars_file'

        def get_vars(self, host, include_hostvars):
            if include_hostvars:
                return {'ansible_hostvars_file': self.host_vars_files[host.name]}
            else:
                return

# Generated at 2022-06-22 12:20:02.297112
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    inventory = FakeInventory()
    variable_manager = FakeVariableManager()
    loader = FakeLoader()

    hostvars = HostVars(inventory, variable_manager, loader)
    hosts = []
    for host in hostvars:
        hosts.append(host)
    assert hosts == list(set(hostvars._inventory.hosts)), hosts

# Generated at 2022-06-22 12:20:25.070467
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Host
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    # populate variables
    vars_manager = VariableManager()
    hostvars = HostVars(inventory=None, variable_manager=vars_manager, loader=None)
    host = Host('localhost')
    vars_manager.add_host_vars(host, {'foo': 'bar', 'spam': 'eggs'})

    # check data is not templated
    data = hostvars.raw_get('localhost')
    assert data['foo'] == 'bar'
    assert isinstance(data['spam'], AnsibleUndefined)

# Generated at 2022-06-22 12:20:36.732336
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(
        loader=DataLoader(),
        sources=['tests/inventory/test_hostvars.ini'])

    variable_manager = VariableManager(loader=DataLoader())

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())
    assert hostvars._inventory == inventory
    assert hostvars._loader == DataLoader()
    assert hostvars._variable_manager == variable_manager

    hostvars.set_inventory(inventory=inventory)
    hostvars.set_variable_manager(variable_manager=variable_manager)

    index = 0

# Generated at 2022-06-22 12:20:39.086495
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    """
    Anchor callback function for unit test of _HostVars.__getitem__()
    """
    return None


# Generated at 2022-06-22 12:20:49.076249
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager

    loader = 'dummy_loader'
    variable_manager = VariableManager(loader=loader)
    variable_manager._hostvars = HostVars(None, variable_manager, loader)
    unsafe_proxy = UnsafeProxy(variable_manager)
    unsafe_proxy_dump = unsafe_proxy.__getstate__()

    # Check that variable manager inside UnsafeProxy has None for
    # _loader and _hostvars attributes
    variable_manager = unsafe_proxy_dump['_obj']
    if variable_manager._loader is not None:
        raise AssertionError('Expected variable_manager._loader is None')


# Generated at 2022-06-22 12:20:57.685125
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.manager import VariableManager

    host_vars = HostVars({}, VariableManager())
    assert repr(host_vars) == repr({})

    import copy
    import pickle

    host_vars_copy = copy.deepcopy(host_vars)
    host_vars_pickle = pickle.loads(pickle.dumps(host_vars))

    assert repr(host_vars) == repr(host_vars_copy)
    assert repr(host_vars) == repr(host_vars_pickle)

# Generated at 2022-06-22 12:21:06.949822
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    import ansible.plugins.cache.memory
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.playbook.play
    import ansible.template
    assert HostVars(
        inventory=ansible.inventory.manager.InventoryManager(
            loader=ansible.plugins.loader.Loader(),
            sources=[],
        ),
        variable_manager=ansible.vars.manager.VariableManager(
            loader=ansible.plugins.loader.Loader(),
            inventory=None,
            version_info=ansible.__version__,
        ),
        loader=ansible.plugins.loader.Loader(),
    ).__repr__() == "{}"

# Generated at 2022-06-22 12:21:14.603639
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/test_invextra_vars.ini'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    assert hostvars['all']['login_user'] == 'root'
    assert hostvars['test.example.com']['remote_user'] == 'root'
    assert hostvars['test.example.com']['group_members'] == ['test.example.com']

# Generated at 2022-06-22 12:21:24.534022
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    def get_inventory(content, loader):
        inventory = InventoryManager(loader=loader, sources=content)
        variable_manager = VariableManager(loader=loader, inventory=inventory)
        return inventory, variable_manager

    loader = DataLoader()

    inventory, variable_manager = get_inventory('localhost ansible_connection=local', loader)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    assert repr(hostvars) == "{'localhost': {}}"


# Generated at 2022-06-22 12:21:32.987394
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create inventory, DataLoader and VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create hostvars
    hostvars = HostVars(inventory, variable_manager, loader)

    # update variables of host localhost
    host = inventory.get_host(name='localhost')
    for key, value in (('foo', '1'), ('bar', '2'), ('baz', '3')):
        variable_manager.set_host_variable(host, key, value)

    # get variables of host localhost
    hostv

# Generated at 2022-06-22 12:21:38.934181
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.vars.hostvars import HostVars
    host_vars = HostVars({}, {'test_key': 'test_value'}, None)
    assert host_vars['test_key'] == 'test_value'
    try:
        host_vars['invalid_key']
    except KeyError:
        assert True
    else:
        assert False


# Generated at 2022-06-22 12:22:04.414046
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    # Test is skipped if pytest-ansible_vars_provider is not installed
    try:
        import pytest_ansible_vars_provider
    except:
        import pytest
        pytest.skip("Test requires pytest-ansible-vars-provider")

    # Test is skipped if environment variable PYTEST_ANSIBLE_VARS_DIR is not set
    import os
    if 'PYTEST_ANSIBLE_VARS_DIR' not in os.environ:
        import pytest
        pytest.skip("Environment variable PYTEST_ANSIBLE_VARS_DIR is not set")

    import glob
    import json
    import yaml

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()



# Generated at 2022-06-22 12:22:16.336758
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    '''
    Make sure that raw_get works as expected
    '''

    # Create fake loader and inventory
    fake_loader = FakeLoader()
    fake_inventory = FakeInventory()

    # Create variables manager with fake loader
    variable_manager = FakeVariablesManager(loader=fake_loader)

    # Create hostvars
    hostvars = HostVars(inventory=fake_inventory,
                        variable_manager=variable_manager,
                        loader=fake_loader)

    # Set some host_vars
    hostvars.set_host_variable(fake_inventory.get_host('host1'),
                               varname='foo', value='bar')
    hostvars.set_host_variable(fake_inventory.get_host('host2'),
                               varname='bar', value='baz')

    # Test variables
   

# Generated at 2022-06-22 12:22:27.655858
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    class FakeVariableManager(object):
        def __init__(self):
            self._vars_cache = {}
            self._host_vars_from_group = {}
            self._loader = None
            self._hostvars = None

    class FakeInventory(object):
        def __init__(self):
            self._hosts_cache = {}

        def get_host(self, host_name):
            return self._hosts_cache.get(host_name)

    class FakeHost(object):
        def __init__(self, name):
            self.name = name

    class FakeLoader(object):
        def __init__(self):
            self.defer_facts = False

    variable_manager = FakeVariableManager()
    inventory = FakeInventory()
    loader = FakeLoader()

    # The HostVars

# Generated at 2022-06-22 12:22:36.218548
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        "hostvars": {
            "cached": {
                "hello": "world",
                "foo": "bar"
            }
        }
    })

    host_vars = HostVars(InventoryManager(loader=loader), VariableManager(loader=loader), loader=loader)

    assert host_vars.raw_get("cached") == {"hello": "world", "foo": "bar"}
    assert host_vars.raw_get("foo") == {"foo": "bar"}


from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-22 12:22:46.604472
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    # Initializing objects
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_variable_manager(variable_manager)

    # Store hostvars to pickle file
    import pickle

# Generated at 2022-06-22 12:22:56.195625
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory import Inventory
    # Creating an empty inventory
    inventory = Inventory(host_list=[])
    # Creating a variable_manager without a hostvars attribute
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    # Creating a HostVars for testing the method __iter__
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars(inventory, variable_manager, loader=None)
    # Assert that the result of the method __iter__ is the same as
    # the result of the method keys() of the inventory
    assert list(hostvars) == inventory.hosts.keys()



# Generated at 2022-06-22 12:23:07.522929
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.unsafe_proxy import UnsafeVariableManager
    from ansible.vars.manager import VariableManager
    class TestHost:
        pass
    class TestHosts:
        def __iter__(self):
            yield TestHost()
    class TestInventory:
        hosts = TestHosts()
    class TestVariableManager(VariableManager):
        def get_vars(self, host, include_hostvars=False):
            return {}
    class TestUnsafeVariableManager(UnsafeVariableManager):
        def get_vars(self, host, include_hostvars=False):
            return {}
    def test(variable_manager):
        loader = None
        inventory = TestInventory()
        hostvars = HostVars(inventory, variable_manager, loader)
        repr(hostvars)

# Generated at 2022-06-22 12:23:19.343122
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    # it seems this method is not used by current Ansible code
    # however, it is used in unit tests, so if you change it,
    # update unit tests as well
    from ansible.vars.inventory_manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common._collections_compat import MutableMapping

    inventory = InventoryManager(Loader=None, sources='tests/inventory')
    # by default, VariableManager uses HostVars, we do not want it
    variable_manager = VariableManager(loader=None, inventory=inventory, host_vars=None)
    host_vars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)

    host_name = 'testhost'

# Generated at 2022-06-22 12:23:26.265918
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])
    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=VariableManager(loader=loader, inventory=inventory))

    all_hosts = list(hostvars)
    assert len(all_hosts) == 1
    assert all_hosts[0].name == '127.0.0.1'


# Generated at 2022-06-22 12:23:38.523596
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible import constants as C
    from ansible.errors import AnsibleParserError
    from ansible.utils.vars import combine_vars

    hostname1 = "foohost"
    hostname2 = "barhost"

    data1 = {'var1': 'value1'}
    data2 = {'var2': 'value2'}
    vvars = combine_vars(data1, data2)

    loader = DataLoader()

    try:
        inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    except AnsibleParserError as e:
        raise AnsibleError(e)

