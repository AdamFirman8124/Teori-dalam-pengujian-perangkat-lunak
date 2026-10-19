

# Generated at 2022-06-22 12:14:23.305258
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import sys
    import types

    if sys.version_info[0] == 2:
        # only python2 needs to test if the class has the correct method types
        test_dict = {'key1': 'value1', 'key2': 'value2'}
        hvv = HostVarsVars(test_dict, loader=None)

        assert isinstance(hvv.__iter__, types.MethodType)

        var_list = []
        for var in hvv:
            var_list.append(var)

        # var order is not guaranteed
        var_list.sort()

        assert var_list == ['key1', 'key2']

# Generated at 2022-06-22 12:14:30.426141
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.parsing.dataloader import DataLoader

    vars = {
        'a': '{{b}}',
        'b': '{{c}}',
        'c': '{{d}}',
        'd': '{{e}}',
        'e': 'f'
    }

    loader = DataLoader()

    hostvars_vars = HostVarsVars(vars, loader)

    if hostvars_vars['a'] != 'f':
        raise AssertionError('test_HostVarsVars___getitem__() error')

# Generated at 2022-06-22 12:14:40.870503
# Unit test for method __getitem__ of class HostVarsVars
def test_HostVarsVars___getitem__():
    from ansible.vars.hostvars import HostVarsVars

    def is_template_failed(variables, var):
        try:
            foo = variables[var]
            return False
        except KeyError as e:
            return True

    # test valid foo = { 'bar': '{{ not_defined }}' }
    variables = HostVarsVars({ 'bar': '{{ not_defined }}' }, None)
    assert (not variables['bar'])
    assert (variables.get('bar'))
    assert (is_template_failed(variables, 'not_defined'))

    # test invalid foo = { 'bar': '{{ not_defined }}' }
    variables = HostVarsVars({ 'bar': '{{ not_defined }}' }, None)

# Generated at 2022-06-22 12:14:46.672331
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    vars = {'foo': 'bar', 'bar': 'baz'}
    v = HostVarsVars(vars, loader=loader)

    assert len(vars) == len(v)
    for var in v:
        assert var in vars



# Generated at 2022-06-22 12:14:56.817068
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inv_path = '../tests/inventory/host_vars_expansion_test.yml'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inv_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    variables = inventory.get_host('host1').get_vars()
    hosts = HostVars(inventory, variable_manager, loader)
    hostvars = hosts.get('host1')
    assert hostvars['v1'] == variables['v1']

# Generated at 2022-06-22 12:15:02.565601
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    import pytest

    a = HostVarsVars({'a': 1, 'b': 2, 'c': 3}, None)
    foo = []
    for x in a:
        foo.append(x)
    assert foo == ['a', 'b', 'c']

    a = HostVarsVars({}, None)
    foo = []
    for x in a:
        foo.append(x)
    assert foo == []


# Generated at 2022-06-22 12:15:13.853734
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    loader = DictDataLoader({
        "inventory": """
[group1]
host1 ansible_foo=42
""",
        "group_vars/group1.yml": """
bar: 1
""",
        "host_vars/host1.yml": """
bar: 2
foo: 3
""",
        "host_vars/host2.yml": """
bar: 4
"""
    })
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))
    variable_manager = inventory.get_variable_manager()
    hostvars = HostVars(inventory, variable_manager, loader)


# Generated at 2022-06-22 12:15:24.956672
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from collections import Mapping
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader, os.path.join(os.path.dirname(__file__), '../../tests/inventory'))
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    hostvars = HostVars(inventory, variable_manager, loader)

    assert isinstance(hostvars, Mapping)

    hostnames = []
    for hostname in hostvars:
        hostnames.append(hostname)

    assert len(hostnames) > 0

# Generated at 2022-06-22 12:15:35.414182
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import pytest

    # create the objects to test
    loader = DataLoader()
    inventory = Inventory(loader, [], [])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory, variable_manager, loader)

    # add hosts to the inventory
    host1 = inventory.add_host('host1', port=22, groups=['group1'], variables=dict(var1='host1'))
    host2 = inventory.add_host('host2', port=22, groups=['group2'], variables=dict(var1='host2'))

# Generated at 2022-06-22 12:15:41.832223
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inv_obj)

    hostvars = HostVars(inventory=inv_obj, variable_manager=variable_manager, loader=loader)
    hostvars['localhost']

# Generated at 2022-06-22 12:15:55.065190
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Create a test inventory with a single localhost host
    inventory = InventoryManager([])
    inventory.add_host("localhost")

    # Create a VariableManager, and test that it is present in the inventory
    variable_manager = VariableManager()
    inventory.set_variable_manager(variable_manager)

    # Create a hostvars object and run the test
    hostvars = HostVars(inventory, variable_manager, inventory.get_loader())
    assert(hostvars.raw_get("localhost") == {})

    # Verify that hostvars contain variables, even if not present in inventory
    hostvars.set_host_variable("localhost", "fact", "value")

# Generated at 2022-06-22 12:16:06.967161
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    Tests method __repr__ of class HostVars
    :return:
    '''
    # Create a simple inventory
    inv_source = "[test_hostvars]\nlocalhost\n"
    inventory = Inventory(loader=DataLoader(), host_list=inv_source)
    # Create a set of variables
    variables = VariableManager(loader=DataLoader())
    variables.set_host_variable(inventory.get_host('localhost'), 'x', 5)
    # Create a HostVars object for the inventory
    hostvars = HostVars(inventory, variables, loader=DataLoader())
    # Generate __repr__ for hostvars. In Python 2 it is:
    #  {'localhost': {'x': 5, 'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost'}}

# Generated at 2022-06-22 12:16:16.684949
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    from ansible.inventory.host import Host
    from ansible.vars.unsafe_proxy import wrap_var
    h = Host('example1')

    d = {'ansible_foo1': wrap_var('example2')}
    d2 = {'ansible_foo2': wrap_var('example3')}

    hvars = HostVarsVars(d, None)
    hvars.set_host_variable(h, 'ansible_foo2', wrap_var('example3'))

    matched_keys = set(hvars)
    expected_keys = set(d.keys() + d2.keys())
    assert matched_keys == expected_keys

# Generated at 2022-06-22 12:16:25.370492
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,'])

    g = Group('valid_group')
    inventory.add_group(g)

    h1 = Host('h1')
    h2 = Host('h2')
    h3 = Host('h3')
    inventory.add_host(h1, 'valid_group')
    inventory.add_host(h2, 'valid_group')
    inventory.add_host(h3)

    hostvars = HostVars(inventory, VariableManager())

    keys = [x for x in hostvars]
    assert len(keys) == 3

# Generated at 2022-06-22 12:16:36.114488
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    hv = HostVars(None, None, None)
    # the object is iterable
    assert isinstance(hv, Iterable)

    # the object is not an iterator
    assert not isinstance(hv, Iterator)

    # the object is iterable only once
    it = iter(hv)
    assert isinstance(it, Iterator)

    # an iterator can be looped only once
    try:
        assert not isinstance(it, Iterable)
        # can not get the iterator twice
        next(it)
        assert False
    except StopIteration:
        pass
    assert isinstance(it, Iterator)

    # the object becomes iterable
    assert isinstance(hv, Iterable)

    # the object can be iterated again
    it = iter(hv)

# Generated at 2022-06-22 12:16:44.252327
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    inventory = None
    loader = None
    variable_manager = None
    hostvars = HostVars(inventory=inventory, loader=loader, variable_manager=variable_manager)
    # Emulate pickling by calling method __getstate__
    state = hostvars.__getstate__()
    # Simulate unpickling by calling method __setstate__
    hostvars.__setstate__(state)
    assert hostvars._inventory is None
    assert hostvars._loader is None
    assert hostvars._variable_manager is None


# Generated at 2022-06-22 12:16:51.822886
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    hostvars = HostVars(None, variable_manager, loader)

    templar = Templar(loader=loader)

    host = '_test_host'
    inventory = {
        host: {
            'a': 1,
            'b': 2,
        },
    }

    hostvars.set_variable_manager(
        VariableManager(
            loader=loader,
            inventory=inventory
        )
    )

    # The host is defined
    data = hostvars[host]
    assert isinstance(data, HostVarsVars)
    assert len(data) == 2

# Generated at 2022-06-22 12:16:55.139095
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    hv = HostVars({1:2})
    hv[1] = {'foo': 'bar'}
    assert eval(repr(hv)) == {1: {'foo': 'bar'}}

# Generated at 2022-06-22 12:17:06.912417
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import sys
    import pickle
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    if PY3:
        assert sys.version_info[0] == 3
    assert sys.version_info[1] >= 4

    assert DataLoader
    assert VariableManager
    assert InventoryManager
    assert Host

    loader = DataLoader()
    group = Host(name='group', port='2222')
    group.set_variable('inventory_hostname', 'group')
    group.set_variable('inventory_hostname_short', 'group')

# Generated at 2022-06-22 12:17:09.542715
# Unit test for method __iter__ of class HostVarsVars
def test_HostVarsVars___iter__():
    class Dummy(object):
        pass

    loader = Dummy()
    hvv = HostVarsVars({'foo': 1, 'bar': 2}, loader)
    assert set(iter(hvv)) == set(hvv.keys())

# Generated at 2022-06-22 12:17:29.632200
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import datetime
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=loader)

    a = {'item1': 'value1', 'item2': 'value2', 'item3': datetime.datetime(2017, 11, 21, 0, 0)}
    hostname = 'test_host'
    hostvars.set_host_variable(host=hostname, varname='a', value=a)

    assert hostvars.get(hostname) == HostVarsVars(variables=a, loader=loader)

    # HostVarsVars method __getitem__ uses Templar to expand variables

# Generated at 2022-06-22 12:17:39.869038
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import pytest

    # input data
    host_name = 'foo'

# Generated at 2022-06-22 12:17:50.827466
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)

    host = inventory.add_host(host=u'localhost', groups=[u'group1'], port=22)

    variable_manager.set_host_variable(host, u'var1', u'localhost')
    variable_manager.set_host_variable(host, u'var2', u'group1')

    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars[u'localhost'][u'var1'] == u'localhost'

# Generated at 2022-06-22 12:17:58.589751
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.vars.reserved import Reserved
    from ansible.inventory.manager import InventoryManager

    dct = { 'k1': 'v1', 'k2': 'v2' }
    res = Reserved(loader=None)
    inv = InventoryManager(loader=None)

    vars = HostVars(inventory=inv, variable_manager=res, loader=None)
    vars.host_vars = { 'k1': 'v1', 'k2': 'v2' }
    assert repr(dct) == repr(vars)

# Generated at 2022-06-22 12:18:09.439301
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import pytest

    v = {}
    hv = HostVars(v, None, None)

    # should return an AnsibleUndefined if host not found
    assert isinstance(hv.raw_get('host_not_found'), AnsibleUndefined)

    # should return the cached variable data if found
    v.update({
        'host_found': {'foo': 'bar'},
        'localhost': {'ansible_connection': 'local'},
    })
    assert hv.raw_get('host_found') == {'foo': 'bar'}

    # should return the cached variable data for localhost on demand
    assert hv.raw_get('localhost') == {'ansible_connection': 'local'}

# Generated at 2022-06-22 12:18:15.344732
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory_manager = InventoryManager(loader=loader, sources=['localhost,'])
    hostvars = HostVars(inventory_manager, variable_manager, loader)
    assert hostvars.raw_get('localhost') == {'groups': {'ungrouped': ['localhost']}}

# Generated at 2022-06-22 12:18:20.457751
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    hostvars = HostVars(inventory=None, variable_manager=None, loader=None)

    assert hostvars.raw_get("localhost") == {"ansible_local": {"some_var": "some_value"}, "host_specific_var": "bar"}
    assert hostvars.raw_get("foobar") == AnsibleUndefined("hostvars['foobar']")

# Generated at 2022-06-22 12:18:32.214267
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)

    host_name = 'test1'
    host = inventory.get_host(host_name)
    host_variable_name = 'test_variable'
    host_variable_value_template = 'my{{ ansible_os_family }}'
    host_variable_value = 'myDebian'
    variable_manager.set_host_variable

# Generated at 2022-06-22 12:18:39.358374
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    host_vars = HostVars(inventory=inventory,
                         variable_manager=None,
                         loader=loader)
    inventory.add_host('myhost')
    inventory.add_host('otherhost')
    assert sorted(list(host_vars)) == ['myhost', 'otherhost']


# Generated at 2022-06-22 12:18:44.711533
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    hosts = [Host(name='localhost')]
    variables = {'var': 'var'}
    vars_manager = VariableManager(loader=None)
    vars_manager._hostvars_cache['localhost'] = variables
    hostvars = HostVars(inventory=None, variable_manager=vars_manager, loader=None)

    assert hostvars.raw_get('localhost') == variables
    assert hostvars.raw_get('127.0.0.1') == variables

# Generated at 2022-06-22 12:19:02.196470
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    inventory = dict(
        hostvars=dict(
            foo=dict(foo='{{ bar }}', baz='baz'),
            bar=dict(bar='{{ ok }}', baz='baz'),
            baz=dict(baz='baz'),
        )
    )


# Generated at 2022-06-22 12:19:12.060132
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    import ansible.playbook
    import ansible.inventory
    class FakeHost:
        def __init__(self, name):
            self.name = name
            self.vars = {'a': 1}
    vars_manager = ansible.vars.VariableManager()
    inventory = ansible.inventory.Inventory(vars_manager=vars_manager)
    inventory.hosts = [
        FakeHost('a'),
        FakeHost('b')]
    loader = ansible.parsing.dataloader.DataLoader()
    hostvars = ansible.vars.HostVars(inventory, vars_manager, loader)
    assert sorted(list(hostvars), key=lambda host: host.name) == sorted(inventory.hosts, key=lambda host: host.name)


# Generated at 2022-06-22 12:19:23.771879
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host

    escaped = "\\N{INVERTED EXCLAMATION MARK}"
    unescaped = u"\N{INVERTED EXCLAMATION MARK}"

    # hostvars
    host = Host('host1')
    hostvars = {host: {'var1': unescaped, u'var2': escaped}}
    assert repr(HostVars(hostvars=hostvars)) == "{'host1': {u'var2': %r, 'var1': %r}}" % (unescaped, escaped)

    # inventory
    hostvars = {u'host1': {'var1': unescaped, u'var2': escaped}}
    inventory = {'_meta': {'hostvars': hostvars}}
    assert repr(HostVars(inventory=inventory))

# Generated at 2022-06-22 12:19:35.760720
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Test 1.1
    host = "foobar"
    loader = DataLoader()
    loader.set_basedir(os.getcwd())
    inventory = VariableManager(loader=loader)
    inventory._hosts = {"foobar": True}
    inventory._vars_per_host.setdefault("foobar", {})["myvar"] = "myval"
    test_subject = HostVars(inventory, VariableManager(), loader)

    try:
        result = test_subject[host]
    except:
        raise AssertionError("HostVars.__getitem__ failed")

    # Test 1.2
    host = "localhost"

# Generated at 2022-06-22 12:19:45.401194
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.variable_manager import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    inventory = Inventory(loader=None, variable_manager=None, host_list=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)
    inventory.add_host('bar')
    variable_manager.set_host_variable(host=inventory.get_host('bar'), varname='foo', value='bar')
    v = hostvars.raw_get('bar')
    assert v['foo'] == 'bar'

# Generated at 2022-06-22 12:19:57.094372
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Invoke constructor of class HostVars
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    hostvars = HostVars(inventory=inventory,
                        variable_manager=variable_manager,
                        loader=loader)

    # Set some variables
    hostvars.set_variable_manager(variable_manager)
    hostvars.set_host_variable('localhost', 'foobar1', 'foobar1')

# Generated at 2022-06-22 12:20:07.032079
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    from ansible_collections.community.general.tests.unit.compat.mock import Mock
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    inventory._hosts_cache = {
        'localhost': Mock(),
        'otherhost': Mock(),
    }
    inventory.set_variable('localhost', 'var1', 'foo')
    inventory.set_variable('localhost', 'var2', '{{ var3 }}')
    inventory.set_variable('localhost', 'var3', 'bar')

# Generated at 2022-06-22 12:20:18.362266
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create hosts
    host1 = Host(name="host1")
    host2 = Host(name="host2")

    # Create Inventory and add hosts to it
    inventory = InventoryManager(loader=DataLoader())
    inventory.add_host(host1)
    inventory.add_host(host2)

    # Create Variable Manager
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    # Set facts to hosts
    variable_manager.set_host_variable(host1, "ansible_ssh_host", "1.1.1.1")
    variable_manager.set_host_variable

# Generated at 2022-06-22 12:20:24.670429
# Unit test for method __iter__ of class HostVars
def test_HostVars___iter__():
    from ansible.vars.hostvars import HostVars
    class Inventory(object):
        def __init__(self):
            self.hosts = ['foo', 'bar']
    class VariableManager(object):
        def __init__(self):
            self.hostvars = None
    inventory = Inventory()
    variable_manager = VariableManager()
    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=None)
    assert list(hostvars) == ['foo', 'bar']

# Generated at 2022-06-22 12:20:33.378657
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    hv = HostVars(
        inventory = None,
        variable_manager = None,
        loader = None
    )

    assert hv.raw_get("ansible") is AnsibleUndefined(name="hostvars['ansible']")
    assert hv.raw_get("ansible") is not AnsibleUndefined(name="hostvars['ansible']")
    assert hv.raw_get("ansible") is not AnsibleUndefined(name="hostvars['ansible2']")
    assert hv.raw_get("ansible") != hv.raw_get("ansible2")



# Generated at 2022-06-22 12:20:46.849192
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    def inventory_host(hostname, vars):
        from ansible.inventory.host import Host

        host = Host(hostname)
        host.vars = vars
        return host

    # Empty hostvars
    hostvars = HostVars(inventory=None, variable_manager=None, loader=None)
    assert hostvars['localhost'] == {}
    assert hostvars.get('localhost', 'var') == AnsibleUndefined(name="hostvars[\'localhost\']['var']")

    # Hostvars with variables
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    inventory.host

# Generated at 2022-06-22 12:20:59.588727
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    # Test to ensure that HostVars is immutable.
    # It has been observed that some code checks if HostVars can be modified
    # by trying a pop() or __del__. In those cases an exception is raised,
    # which is exactly what is expected.
    def test_immutability(name, hostvars):
        old_vars = hostvars[name]
        try:
            hostvars[name]['foo'] = 'bar'
        except Exception:
            pass
        return hostvars[name] == old_vars

    # Test to ensure that HostVars.__getitem__ is __deepcopy__-friendly.
    # This has been observed to fail in cases where, for example, the HostVars
    # object is loaded in a playbook that uses include_vars.

# Generated at 2022-06-22 12:21:05.348102
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    import os
    import tempfile
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    tfd, tfp = tempfile.mkstemp()
    os.close(tfd)

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=tfp)
    inventory.add_host(host="test")
    inventory.set_variable("test", "foo", "bar")

    hostvars = HostVars(inventory=inventory, variable_manager=inventory.get_variable_manager(), loader=DataLoader())

    assert hostvars["test"]["foo"] == "bar"
    assert hostvars["test"].get("foo") == "bar"


# Generated at 2022-06-22 12:21:13.349851
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.domain import GlobalVars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost")
    host_vars = inventory._host_vars
    vm = VariableManager(loader=loader, inventory=inventory)
    results = host_vars.raw_get('localhost')
    assert(isinstance(results, Mapping))
    assert(isinstance(results, GlobalVars))
    assert('omit' in results)
    assert('playbook_dir' in results)
    assert('inventory_hostname' in results)

# Generated at 2022-06-22 12:21:23.797852
# Unit test for method __repr__ of class HostVars

# Generated at 2022-06-22 12:21:32.928326
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    '''
    This test tries to be sure that repr(HostVars(...)) will not fail,
    without any assertion on the repr result.
    '''
    # Parameters to call HostVars.__init__
    inventory_file = None
    variable_manager = None
    loader = None

    # Creating a Mock object to represent a class 'Inventory', having
    # method 'get_host' which returns a Mock object, having method 'get_vars'
    # which itself returns a dict.
    class MockInventory:
        class MockHost():
            def get_vars(self):
                return {'my_var': 'my_value'}

        def get_host(self, host_name):
            return MockInventory.MockHost()

    mock_inventory = MockInventory()

    # Creating an instance of HostV

# Generated at 2022-06-22 12:21:42.080605
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.unicode import to_unicode

    loader = DataLoader()

    variable_manager = VariableManager()
    inventory = Inventory("localhost", variable_manager=variable_manager, loader=loader)
    variable_manager.set_inventory(inventory)
    variable_manager.set_variable("foo", "bar")

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    assert hostvars.raw_get("localhost") == dict(foo=to_unicode("bar", errors='surrogate_or_strict'))

# Generated at 2022-06-22 12:21:54.699429
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():

    from ansible.vars import VariableManager
    from ansible import inventory

    variables_1 = dict(foo='bar', baz='boo')
    variables_2 = dict(foo='baz')

    h1 = inventory.Host(name='h1')
    h2 = inventory.Host(name='h2')

    i = inventory.Inventory()

    i.add_group(inventory.Group('g1'))
    i.add_host(h1, 'g1')
    i.add_host(h2, 'g1')

    l = None
    vm = VariableManager(loader=l)
    vm.set_host_variable(host=h1, varname='vars', value=variables_1)

# Generated at 2022-06-22 12:22:04.414195
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    hostvars = HostVars(inventory=InventoryManager(loader=DataLoader(), sources=[]),
                        variable_manager=VariableManager(),
                        loader=DataLoader())

    assert repr(hostvars) == "{}"

    hostvars._inventory.hosts = [
        {'name': 'example_1', 'vars': {'foo': 'bar'}},
        {'name': 'example_2', 'vars': {'baz': 'qux'}},
        {'name': 'example_3', 'vars': {'foo': 'bar', 'baz': 'qux'}}
    ]


# Generated at 2022-06-22 12:22:16.337807
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    # Test cases
    class PickleMethodsTest1(object):
        def __getstate__(self):
            return 'dummy1'

    class PickleMethodsTest2(object):
        def __getstate__(self):
            return 'dummy2'

        def __setstate__(self, state):
            self.state = state

    class PickleMethodsTest3(object):
        def __setstate__(self, state):
            self.state = state

    test_cases = [
        PickleMethodsTest1(),
        PickleMethodsTest2(),
        PickleMethodsTest3()
    ]

    # Tested class
    class TestedClass(object):
        def __init__(self, var):
            self.var = var

        def __getstate__(self):
            return self.var


# Generated at 2022-06-22 12:22:27.419240
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    from ansible.vars import VariableManager

    v = VariableManager()
    hv = HostVars(inventory=None, variable_manager=v, loader=None)
    hv.__setstate__({'_variable_manager': {}, '_inventory': None, '_loader': None})

    assert hv._variable_manager._loader == None
    assert hv._variable_manager._hostvars == hv

# Generated at 2022-06-22 12:22:37.503832
# Unit test for method __setstate__ of class HostVars
def test_HostVars___setstate__():
    import pickle
    from ansible.vars import VariableManager, HostVars
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    inventory.host_vars={}
    inventory.host_vars["127.0.0.1"] = [{"foo":"bar"}]
    vm = VariableManager(loader=loader)
    vm.set_inventory(inventory)
    vm.set_host_variable("127.0.0.1","baz","fu")
    hv = HostVars(inventory, vm, loader)

    assert hv.raw_get("127.0.0.1")["foo"]=="bar"

# Generated at 2022-06-22 12:22:47.195439
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():

    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    hostvars = HostVars(inventory=None, variable_manager=variable_manager, loader=None)

    assert hostvars.raw_get('foo') == AnsibleUndefined(name="hostvars['foo']")
    hostvars.set_host_variable(host=None, varname='foo', value='bar')
    assert hostvars.raw_get('foo') == 'bar'
    hostvars.set_host_variable(host=None, varname='foo', value='baz')
    assert hostvars.raw_get('foo') == 'baz'
    hostvars.set_host_variable(host=None, varname='foo', value=1)
    assert hostvars.raw_get('foo') == 1

# Generated at 2022-06-22 12:22:57.877586
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.inventory import Inventory
    from ansible.plugins import vars_loader
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    vars_plugin = vars_loader.all(C)
    inventory = Inventory(loader=None)
    variable_manager = VariableManager(loader=None, inventories=[inventory])
    hostvars = HostVars(inventory, variable_manager, loader=None)

    # create a dummy host and set a variable
    host = inventory.get_host("localhost")
    varname = "foobar"
    varvalue = "spam"
    variable_manager.set_host_variable(host, varname, varvalue)

    # check that variable is set
    vars_plugin.get_host_vars(host=host)
    assert variable_

# Generated at 2022-06-22 12:23:09.227080
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    ''' Verify that we can read hostvars[host], run the resultant
    dictionary through the templating engine, and get values back. '''

    class MockInventory:
        class Host:
            name = 'testhost'
            vars = dict(
                one="{{ host.name }}",
                two="{{ hostvars[host.name]['one'] }}",
                three="{{ hostvars[host.name]['four'] }}",
                four="foo"
            )

        hosts = [Host()]

    class MockVariableManager:
        def __init__(self):
            self._hostvars = None

    class MockLoader:
        def get_basedir(self):
            return os.getcwd()

    from ansible.parsing import DataLoader
    loader = DataLoader()

    inventory = MockIn

# Generated at 2022-06-22 12:23:20.007956
# Unit test for method raw_get of class HostVars
def test_HostVars_raw_get():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    # Create empty inventory
    inventory = Inventory("/dev/null")

    # Create variable manager
    variable_manager = VariableManager()
    variable_manager._inventory = inventory
    variable_manager._vars_cache = {}

    # Create HostVars
    loader = DataLoader()
    hostvars = HostVars(inventory, variable_manager, loader)
    hostvars.set_variable_manager(variable_manager)

    # Assert that localhost does not contain default variables such as ansible_ssh_port
    assert "ansible_ssh_port" not in hostvars.raw_get("localhost")

# Generated at 2022-06-22 12:23:26.018921
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    hostvars = HostVars(None, None, None)

    class FakeInventory:
        def __init__(self, hosts):
            self.hosts = hosts

    class Host:
        def __init__(self, name):
            self.name = name

    hostvars._inventory = FakeInventory([Host('host1'), Host('host2')])

    hostvars.raw_get = lambda host_name: dict(foo=1)

    assert eval(repr(hostvars)) == {
        'host1': { 'foo': 1 },
        'host2': { 'foo': 1 },
    }

# Generated at 2022-06-22 12:23:37.982843
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    # The method __repr__ of HostVars returns a dictionary where values are
    # python primitives (strings, ints, booleans, etc).
    if getattr(HostVars, '__repr__') is None:
        raise Exception('The method __repr__ of HostVars was not implemented')

    # The values of the dictionary returned by __repr__ are python primitives
    if not isinstance(Agenda.__repr__(), dict):
        raise Exception('The method __repr__ of HostVars does not return a dictionary')

    for value in Agenda.__repr__().values():
        if not isinstance(value, (str, int, bool, float, long)):
            raise Exception('The method __repr__ of HostVars does not return a dictionary of python primitives')

# Generated at 2022-06-22 12:23:42.286466
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    hostvars = HostVars(inventory=inventory, variable_manager=variable_manager, loader=DataLoader())

    assert repr(hostvars) == "{'localhost': {}}"


# Generated at 2022-06-22 12:23:52.163660
# Unit test for method __repr__ of class HostVars
def test_HostVars___repr__():
    class FakeInventory(object):
        def __init__(self, hosts):
            self.hosts = hosts
        def get_host(self, host_name):
            return self.hosts.get(host_name)

    class FakeHost(object):
        def __init__(self, name):
            self.name = name
        def get_name(self):
            return self.name

    class FakeVariableManager(object):
        def __init__(self):
            self._hostvars = None
        def get_vars(self, host=None, include_hostvars=False):
            if isinstance(host, FakeHost):
                return {'foo': 'bar'}
            return AnsibleUndefined()

    hosts = {}
    for h in ['host1', 'host2']:
        hosts[h]

# Generated at 2022-06-22 12:24:01.963700
# Unit test for method __getitem__ of class HostVars
def test_HostVars___getitem__():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inventory = Inventory(loader=None, variable_manager=VariableManager())
    hostvars = HostVars(inventory, VariableManager(), None)
    hostvars['example.com']
    assert hostvars['example.com'] == {}

