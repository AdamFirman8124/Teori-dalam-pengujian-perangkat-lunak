

# Generated at 2022-06-13 12:55:12.375599
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  from ansible.inventory.manager import InventoryManager
  import os
  import os.path
  inventory_path = os.path.join(os.path.dirname(__file__), "../../ansible_inventory")
  test_file = os.path.join(inventory_path, "hosts")
  inventory = InventoryManager(inventory_src=test_file)
  test_file = os.path.join(inventory_path, "hosts_include")
  inventory.add_host(host=test_file)
  file_path = os.path.join(os.path.dirname(__file__), "../../../docs/examples/script_module/inventory.py")
  inv = InventoryModule(inventory=inventory, filename=file_path)
  inv.parse()


# Generated at 2022-06-13 12:55:21.361621
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    
    # Create test object with default TEST_HOST_LIST
    module = InventoryModule(inventory=Inventory(loader=DictDataLoader({"host_list":TEST_HOST_LIST,"my_groups":TEST_MY_GROUPS_1})))
    module.filename = 'my_groups'
    
    # Parse the group file
    module.parse()
    
    # Check inventory hosts
    hosts = module.inventory.get_hosts()

# Generated at 2022-06-13 12:55:32.487638
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    correct contents of groups from the given array of lines. No exception on
    any parse success.
    '''
    vars = {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j'}
    test_module = InventoryModule(None)
    test_module.vars_loader = MagicMock()
    test_module.vars_loader.get_basedir.return_value = '/tmp'
    test_module.vars_loader.get_vars.return_value = vars
    test_module.vars_loader.get_inventory_basedir.return_value = '/tmp'
    test_module.inventory.add_group = MagicMock()
    test_module.inventory.set_variable = MagicMock()
    test_module

# Generated at 2022-06-13 12:55:47.493416
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # empty input
    test = InventoryModule()
    try:
        test._parse('path','')
    except AnsibleParserError as e:
        assert isinstance(e,AnsibleParserError)
    else:
        assert False
    # No comment or empty line
    test = InventoryModule()
    data = """
        [test:vars]
        [test:children]
        [test]
    """
    try:
        test._parse('path', data)
    except Exception as e:
        assert False
    else:
        assert True
    # With comment
    test = InventoryModule()
    data = """
        #comment
        [test:vars]
        [test:children]
        [test]
    """

# Generated at 2022-06-13 12:55:57.208457
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory_parser = InventoryModule()
    inventory.inventory = Inventory()
    for pattern in [u'localhost', u'example.org']:
        inv_info = inventory_parser.inventory._expand_hostpattern(pattern)
        inventory.inventory._expand_cache[pattern] = ([inv_info[0]], inv_info[1])
        inventory.inventory.hosts[pattern] = [Host(pattern)]

    hostvars = {u'localhost': {u'ansible_connection': u'local'}, u'example.org': {}}
    for pattern, hv in hostvars.items():
        for host in inventory.inventory._expand_cache[pattern][0]:
            for k, v in hv.items():
                inventory.inventory.set_variable(host, k, v)

   

# Generated at 2022-06-13 12:56:05.456773
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import json
    inv = dict()
    inv['path'] = 'ansible/test/'
    inv['name'] = 'test_inventory'
    inv['playbook'] = 'test_playbook.yml'
    InventoryModule(inventory=inv, host_list='localhost,').parse()
    assert inv['vars']['localhost'] == dict(ansible_host='127.0.0.1')
    inv = dict()
    inv['path'] = 'ansible/test/'
    inv['name'] = 'test_inventory'
    inv['playbook'] = 'test_playbook.yml'
    InventoryModule(inventory=inv, host_list='127.0.0.1,').parse()

# Generated at 2022-06-13 12:56:16.404391
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:56:26.274672
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test successful parsing
    dummy_path = 'dummy_path'

# Generated at 2022-06-13 12:56:35.469704
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class MyInventoryModule(InventoryModule):
        pass

    my_inv_mod = MyInventoryModule()
    my_inv_mod._compile_patterns()
    assert my_inv_mod.patterns['section'].match('[groupname]')
    assert my_inv_mod.patterns['section'].match('[groupname:children] #abc')

    assert my_inv_mod.patterns['groupname'].match('groupname')
    assert not my_inv_mod.patterns['groupname'].match('[groupname]')
    assert not my_inv_mod.patterns['groupname'].match('[groupname:vars]')

    assert my_inv_mod._parse_variable_definition('foo=bar') == ('foo', 'bar')
    assert my_inv_mod._parse_variable

# Generated at 2022-06-13 12:56:44.107660
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for InventoryModule.parse
    '''
    # stub out variables
    _filename = 'test_filename'
    _options = 'test_options'
    _loader = 'test_loader'
    _inventory = 'test_inventory'
    _cache = 'test_cache'
    test_object = InventoryModule(_filename, _options, _loader, _inventory, _cache)
    path = 'test_path'
    data = 'test_data'

    # invoke the method
    result = test_object._parse(path, data)

    # assert the results
    assert(result == None)

# Generated at 2022-06-13 12:56:58.312330
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager('')
    m = InventoryModule(loader=None, inventory=inventory, variable_manager=None)
    m.parse('')


# Generated at 2022-06-13 12:57:01.433537
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    args = ['/etc/ansible/hosts']
    mi = InventoryModule(**{})
    mi.parse(args)
    assert mi.inventory.groups['all']
    assert mi.inventory.groups['all'].hosts['localhost']

# Generated at 2022-06-13 12:57:11.951969
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from collections import OrderedDict
    dataloader = DataLoader()
    inventory = InventoryManager(loader = dataloader, sources = ['examples/inventory/inventory_file'])
    inventory_module_parser = InventoryModule(inventory, 'examples/inventory/inventory_file')
    inventory_module_parser.parse()
    # TODO: fix this test
    #assert inventory.get_hosts('group1') == ['host1','host2','host3','host4','host5']
    #assert len(inventory.get_hosts('group2')) == 0
    #assert len(inventory.get_hosts('all')) == 0
    #assert len(inventory.get_hosts('group3

# Generated at 2022-06-13 12:57:19.651465
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create an instance of Inventory
    inventory = InventoryManager(loader=DictDataLoader({}))
    # Create an instance of InventoryModule
    inventory_module = InventoryModule(inventory=inventory)
    # test the method parse of class InventoryModule
    try:
        inventory_module.parse("/my/ansible/inventory", [to_bytes("localhost ansible_connection=local")])
    except Exception as e:
        assert False, ('test_InventoryModule_parse() failed with: %s' % to_text(e))


# Generated at 2022-06-13 12:57:22.295130
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # FIXME:
    # 1. Write unit tests for parse(self, inventory, loader, hosts=None, variable_manager=None, cache=False)
    # 2. Fix the unit test
    return


# Generated at 2022-06-13 12:57:25.821051
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    module.parse("[unittest]", "127.0.0.1")
    assert module.host_vars['127.0.0.1'] == {}


# Generated at 2022-06-13 12:57:32.185243
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    cls=InventoryModule
    parser = cls('hosts')
    
    # [groupname]
    # hostname
    path = 'test_parse_hosts'
    lines = ['[groupname]', 'hostname']
    parser.parse(path, lines)

    # [groupname:children]
    # childgroup
    path = 'test_parse_children'
    lines = ['[groupname:children]', 'childgroup']
    parser.parse(path, lines)

    # [groupname:vars]
    # key=value
    path = 'test_parse_vars'
    lines = ['[groupname:vars]', 'key=value']
    parser.parse(path, lines)

    # [groupname]
    # hostname
    # [groupname:children]
    # child

# Generated at 2022-06-13 12:57:39.967965
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible import constants as C
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    def get_host(hostname):
        for h in i.get_hosts():
            if h.name == hostname:
                return h
        return None

    def get_group(groupname):
        for g in i.groups.values():
            if g.name == groupname:
                return g
        return None

    i = InventoryModule(loader=None)
    try:
        i.parse(path=get_test_data_path(os.path.join('testinventory', 'test1')), cache=False)
    except AnsibleError as e:
        assert False, e.message

    assert i.inventory.groups['ungrouped'] == Group('ungrouped')

    assert get

# Generated at 2022-06-13 12:57:46.749371
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryManager(loader=DictDataLoader({'hosts': '''
local ansible_connection=local
foo1
[group1]
foo2
[group2:vars]
foo3
[group3]
foo4
[group4:children]
group5
'''}))
    assert 'local' == inv.get_host('local').get_name()
    assert 'foo1' == inv.get_host('foo1').get_name()
    assert 'foo2' == inv.get_host('foo2').get_name()
    assert 'foo3' == inv.get_host('foo3').get_name()
    assert 'foo4' == inv.get_host('foo4').get_name()
    assert 'group1' == inv.get_group('group1').get_name()

# Generated at 2022-06-13 12:57:49.837205
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = IniInventory()
    InventoryModule.parse(inventory, "unit-test")
    groups = inventory.list_groups()
    assert groups == ['all']

# Generated at 2022-06-13 12:58:02.627363
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print(InventoryModule.parse('/foo/bar'))

# Generated at 2022-06-13 12:58:17.696770
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_data = """
[all:vars]
ansible_ssh_user=vnc
ansible_ssh_pass=secret
ansible_become_pass=secret

[rancher:vars]
#rancher_image_version=latest
rancher_image_version=v1.1.1
rancher_network_name=vnc_net
rancher_version=v1.1.1

[hosts]
#host1
#host2

[rancher]
host1
host2

[rancher:children]
hosts
"""
    # Test parsing a blank file
    inventory = InventoryModule(loader=DataLoader())
    inventory.parse_inventory(inventory_data.encode('utf-8'))
    assert "all" in inventory.inventory.groups
   

# Generated at 2022-06-13 12:58:19.202902
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Placeholder for method tests
    pass


# Generated at 2022-06-13 12:58:23.844964
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    try:
        module.parse("/etc/ansible/", "", "")
        pytest.fail("No exception raise")
    except AnsibleError as error:
        assert error.args[0] == "No inventory was parsed, check your syntax and make sure there is a group called:[ungrouped]"
    

# Generated at 2022-06-13 12:58:31.836466
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=DataLoader())
    inventory.add_group('group')
    inventory.add_group('parent')
    inventory.add_group('child')
    inventory.add_group('ungrouped')
    inventory.add_host(Host('one.example.org'))
    inventory.add_host(Host('two.example.org'))

    module = InventoryModule(loader=None, inventory=inventory)

# Generated at 2022-06-13 12:58:40.166093
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """ Parses the inventory file and returns a dict describing it """
    inventory_path = 'inventory'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    test_module = InventoryModule(inventory=inventory, loader=loader, path=inventory_path)

    with open(inventory_path, 'r') as f:
        data = [to_text(line, errors='surrogate_or_strict') for line in f.readlines()]
    assert test_module._parse('inventory', data) is None
    #assert test_module.parse(inventory_path) == inventory


# Generated at 2022-06-13 12:58:51.653629
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # FIXME: Calling parse like this is not convenient if we have a class...
    if sys.version_info[0] > 2:
        class FakeFile(io.StringIO):
            pass
    else:
        class FakeFile(StringIO.StringIO):
            pass
    examples_dir = os.path.dirname(__file__)
    d = os.path.join(examples_dir, 'inventory_example.ini')
    inv = InventoryModule()
    inv.parse(FakeFile(u'[test]\nhost1'), d, 'test')  # FIXME: fake filename
    assert inv.inventory.groups['test']['hosts'] == ['host1']
    assert inv.inventory.groups['test']['vars'] == {}



# Generated at 2022-06-13 12:58:58.658205
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    im = InventoryModule()
    im._parse(path='a', lines=['[a:vars]','a=1','[a]','b','[a:children]','b'])
    assert im.inventory.groups['a'].vars['a'] == 1
    assert im.inventory.groups['a'].hosts['b'].vars == {}
    assert im.inventory.groups['b'].vars == {}
    assert im.inventory.groups['b'].hosts == {}
    assert im.inventory.groups['a'].child_groups['b']
    assert im.inventory.groups['a'].hosts.keys() == ['b']


# Generated at 2022-06-13 12:59:06.911370
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print("===== test_InventoryModule_parse =====")
    inv = InventoryModule()
    inv.parse('tst/ansible/inventory/tst.inventory', {})
    print("inv.inventory = %s" % inv.inventory)
    print("inv.inventory.groups = %s" % inv.inventory.groups)
    print("inv.inventory.groups['all'] = %s" % inv.inventory.groups['all'])
    print("inv.inventory.groups['all'].hosts = %s" % inv.inventory.groups['all'].hosts)
    print("inv.inventory.groups['all'].hosts[0].name = %s" % inv.inventory.groups['all'].hosts[0].name)

# Generated at 2022-06-13 12:59:18.011703
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    file = '/Users/myself/dev/github/ansible/ansible/inventory/test/inventory'
    #file = '/Users/myself/dev/github/ansible/ansible/inventory/test/inventory_yaml'
    module = InventoryModule()
    module.parse(file)

# Generated at 2022-06-13 12:59:38.793542
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()
    inv_mod.parse(None, '')


# Generated at 2022-06-13 12:59:47.249277
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory(host_list=[])
    inventory_file = InventoryModule(loader=None, inventory=inventory)
    inventory_file._parse(path='/etc/ansible/hosts', lines=['localhost ansible_connection=local'])
    assert inventory.list_hosts() == ['localhost']
    assert inventory.get_groups_dict() == {'all': {'hosts': ['localhost'], 'children': []}, 'ungrouped': {'hosts': ['localhost'], 'vars': {}}}

# Generated at 2022-06-13 12:59:58.994552
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.host import Host

    # all examples are from comments in the code
    # pattern 1
    # [groupname]
    # [somegroup:vars]
    # [naughty:children] # only get coal in their stockings
    data = '''\
[groupname]
[somegroup:vars]
[naughty:children] # only get coal in their stockings
'''
    im = InventoryModule(None)
    im._parse('/etc/hosts', data.split('\n'))

    groups = im.inventory.groups
    inv_groups = dict((g.name, g) for g in groups)
    assert 'groupname' in inv_groups
    assert inv_groups['groupname'].name == 'groupname'
    assert not inv_groups['groupname'].get_vars

# Generated at 2022-06-13 13:00:05.648550
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    # FIXME: need to mock a real result here.
    inv_source = 'hosts'
    cache = False
    # FIXME: need to mock a real result here.
    inv_dest = '/tmp/'
    vault_password = None
    loader = DataLoader()
    inventoryM = InventoryManager(loader=loader, sources=inv_source)
    im = InventoryModule(inventory=inventoryM)


# Generated at 2022-06-13 13:00:17.436444
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    raw = ("\n"
    "  # [groupname]\n"
    "  # host1\n"
    "  # host2\n"
    "\n"
    "  # [groupname:vars]\n"
    "  # var1 = value\n"
    "  # var2 = value2\n"
    "\n"
    "  # [groupname:children]\n"
    "  # subgroup\n"
    "\n"
    "  # [ungrouped]\n"
    "  # host3.example.com\n\n")
    path = 'test/hosts'
    m = InventoryModule()
    m.parse(path, raw)
    print(m.inventory.get_groups())


# Class InventoryScript

# Generated at 2022-06-13 13:00:28.775588
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #
    # inventory_parse is used by Ansible in order to parse the inventory file and
    # build the inventory structure used later
    #
    inv = InventoryModule()
    inv.parse('/dev/null', '''
[host_group_1]
host_1a
host_1b
[host_group_2:children]
host_group_1
[host_group_2:vars]
ansible_ssh_user=foo
ansible_ssh_port=22
[host_3:vars]
ansible_connection=local
''')
    assert len(inv.inventory.groups) == 3
    hg1 = inv.inventory.groups['host_group_1']
    hg2 = inv.inventory.groups['host_group_2']
    assert len(hg1.hosts) == 2


# Generated at 2022-06-13 13:00:39.820463
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory([])
    inventory_module = InventoryModule()
    inventory_module.inventory = inventory

# Generated at 2022-06-13 13:00:48.385208
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ini = '''
[test]
a:1234
b:2345

[test:children]
othergroup
othergroup:1234

[othergroup]
a:1234
b:2345
b:3456

[othergroup:vars]
a:5678
d:2345

[othergroup:children]
test2
test2:1234

[test:vars]
test:test345

[test2]
a:1234
b:2345

[test2:children]
test

[test2:vars]
test:test
'''
    with open(my_path, 'w') as f:
        f.write(ini)

    inventory = DataLoader().load_from_file(my_path)

# Generated at 2022-06-13 13:00:59.385462
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module._parse(path = 'some/mock/path/to/inventory',
                            content = ['[test]', 'test_host', 'test_host2 ansible_host=test_host2', 
                                       '[test:vars]', 'a=2', 'b="3"', 'c={a: 2, b: 3}', 'd="""string"""',
                                       '[test:children]', 'test_child'])
    
    print(inventory_module.inventory.hosts)
    print(inventory_module.inventory.groups)


# Generated at 2022-06-13 13:01:14.362016
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:02:00.938072
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print('Test _parse of class InventoryModule')
    # Returns a populated inventory obj.
    inventory = ansible.parsing.dataloader.DataLoader()
    inv = InventoryModule(loader=inventory)
    inv.parse('test.ini', ['[test]', 'test1', 'test2', '[test:vars]', 'var1=test'])
    print(inv.groups)



# Generated at 2022-06-13 13:02:09.116921
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager()
    inv_source = InventoryModule(inventory, 'test/unit/ansible_test/inventory1.yml')
    inv_source.parse()
    assert len(inventory.groups) == 3
    assert len(inventory.hosts) == 3
    assert len(inventory.groups['ungrouped'].hosts) == 1
    assert len(inventory.groups['group1'].hosts) == 2
    assert len(inventory.groups['group2'].hosts) == 0
    assert len(inventory.groups['group2'].subgroups) == 2
    assert len(inventory.groups['group1'].subgroups) == 0


# Generated at 2022-06-13 13:02:11.102198
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    ret = inv.parse("", "")
    assert ret is None


# Generated at 2022-06-13 13:02:13.548826
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv=InventoryModule()
    inv.read_file('tests/test_inventory.ini')


# Generated at 2022-06-13 13:02:22.401957
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Tests for parsing
    # All tests are actually parsing the same file, so we use the same data
    # object
    data = """
# comment1
[group1]
hostname1 ansible_port=4000 some_variable=1
hostname2
[group2:children]
group1
[group3:vars]
some_other_var=3
ansible_connection=ssh
ansible_ssh_user=root
[group4:vars]
some_other_var=4
[group5]
ipv6_host ansible_connection=ssh ansible_user=admin
# comment2
[token_expansion_group]
host[01:50].example.com
"""

    # Create a new instance of the InventoryModule class
    inv = InventoryModule()

    # Fake a filename for the inventory file

# Generated at 2022-06-13 13:02:32.570388
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import unittest

    class InventoryModuleTest(unittest.TestCase):
        def setUp(self):
            self.inven = InventoryModule()

        def test_parse_section_1(self):
            # test case: valid key="value"
            self.assertEqual(
                self.inven._parse_variable_definition('key="value"'), ('key', 'value')
            )

        def test_parse_section_2(self):
            # test case: valid key=value
            self.assertEqual(
                self.inven._parse_variable_definition('key=value'), ('key', 'value')
            )


# Generated at 2022-06-13 13:02:36.132263
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Parse an inventory file and return the corresponding inventory.
    """
    invert = InventoryModule()
    invert.do_parse('/tmp/test_ansible/ansible.cfg','/tmp/test_ansible/test_inventory')


# Generated at 2022-06-13 13:02:44.229630
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    module.parse("test")
    assert module.inventory.groups == {}
    assert module.inventory.vars == {}

    module = InventoryModule()
    module.parse("test")
    assert module.inventory.groups == {}
    assert module.inventory.vars == {}

    module = InventoryModule()
    module.parse("[defaults]")
    assert module.inventory.groups == {}
    assert module.inventory.vars == {}

    module = InventoryModule()
    module.parse("[defaults]\n\n")
    assert module.inventory.groups == {}
    assert module.inventory.vars == {}



# Generated at 2022-06-13 13:02:55.947623
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule()
    class Inventory:
        def __init__(self):
            self.groups = {}

        def add_group(self, groupname):
            self.groups[groupname] = Group(groupname)

        def add_child(self, groupname, childgroup):
            self.groups[groupname].add_child_group(self.groups[childgroup])

        def set_variable(self, groupname, varname, value):
            self.groups[groupname].set_variable(varname, value)

        def get_variables(self, groupname):
            return self.groups[groupname].get_variables()

        def groups_for_host(self, hostname):
            return self.groups['ungrouped'].get_host_groups(hostname)


# Generated at 2022-06-13 13:03:05.963074
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from unittest import TestCase, main

    import os

    import ansible.constants as C

    class TestInventoryModuleParse(TestCase):
        ''' Unit test class to test the parse method of class InventoryModule '''

        def setUp(self):
            self.test_subdir = os.path.join('test', 'parser_inventory_unit_tests')
            self.test_dir = os.path.join(C.DEFAULT_LOCAL_TMP, self.test_subdir)
            self.test_file = os.path.join(self.test_dir, 'inventory')

        @staticmethod
        def _make_test_dir_structure(*dir_path):
            ''' make a test directory structure '''