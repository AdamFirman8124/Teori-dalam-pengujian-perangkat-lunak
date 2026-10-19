

# Generated at 2022-06-13 12:55:11.153036
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    This function was auto-generated using Python's unittest module, passing data generated using `inventorygen`
    """
    inventorypath = "/home/ruan/tmp/test.inventory"
    test_inc = InventoryModule(path=inventorypath, runner_callbacks={})
    test_inc.parse(inventorypath)
    assert test_inc.inventory.groups['defaultgroup'].vars['path'] == '/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games'
    assert len(test_inc.inventory.groups['defaultgroup'].vars['ansible_ssh_user']) == 1
    assert test_inc.inventory.groups['defaultgroup'].vars['ansible_ssh_user'][0] == 'ruan'

# Generated at 2022-06-13 12:55:20.592132
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    fixture_name = 'inventory_ini_file.ini'

# Generated at 2022-06-13 12:55:28.806171
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test InventoryModule.parse() fails for invalid argument
    for arg in [0, 3.14, [], {}]:
        with pytest.raises((TypeError, AssertionError)):
            InventoryModule.parse(arg)
    # Test InventoryModule.parse() fails for invalid path
    with pytest.raises(AnsibleError):
        InventoryModule.parse("/invalid/path")
#
# Inventory class tests
#

# Generated at 2022-06-13 12:55:34.321395
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule('.')
    inv._parse('/tmp/foo', ['[group1]',
                            'foo1',
                            'foo2'])
    assert('group1' in inv.inventory.groups)

# Testing this class is currently a bit difficult because there are so many required classes to make it work
# TODO: Refactor this code to make testing easier


# Generated at 2022-06-13 12:55:48.109116
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    with open('/etc/ansible/hosts', 'r') as hosts_file:
        lines = hosts_file.readlines()
        module._parse('', lines)

    assert len(module.inventory.groups) >= 4
    for group in module.inventory.groups:
        if group == 'all' or group == 'ungrouped':
            assert len(module.inventory.groups[group].hosts) >= 1
        elif group == 'test':
            assert len(module.inventory.groups[group].hosts) == 1
        elif group == 'webservers':
            assert len(module.inventory.groups[group].hosts) == 3
        elif group == 'dbservers':
            assert len(module.inventory.groups[group].hosts) == 2

# Generated at 2022-06-13 12:55:57.798366
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class FakeInventory:
        def __init__(self):
            self.groups = {}
        def add_group(self, groupname):
            self.groups[groupname] = gruopname
        def add_child(self, groupname, childname):
            self.groups[groupname].add_child(childname)
        def set_variable(self, groupname, k, v):
            self.groups[groupname][k] = v
        def _expand_hostpattern(self, hostpattern):
            return [[hostpattern], None]
    inventory = FakeInventory()
    inventory_module = InventoryModule(inventory, 'template.cfg')
    with pytest.raises(AnsibleParserError) as excinfo:
        with open('template.cfg', 'r') as f:
            content = f.read()
           

# Generated at 2022-06-13 12:56:09.485511
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test without fail if use_passed_groups is True
    i = InventoryModule()
    i.fail_without_passed_groups = False
    i.parse([], [], [])
    assert i.hosts == {}, "hosts should be empty"
    assert i.groups == {}, "groups should be empty"

    # Test with fail if use_passed_groups is False
    i = InventoryModule()
    assert_raises(AnsibleError, i.parse, [], [], [])


# Generated at 2022-06-13 12:56:20.354478
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_lines = '''
        [ungrouped]
        # comment
        localhost
        [ungrouped:vars]
        # comment
        key1=val1
        key2=val2
        [group1]
        host1
        host2
        [group1:vars]
        key3=val3
        key4=val4
        key5=val5
        [group1:children]
        group1child1
        group1child2
        [group2]
        host3
        host4
        [group2:vars]
        key6=val6
        key7=val7
        key8=val8
        [group2:children]
        group2child1
        group2child2
        '''
    import io
    import os.path
    import tempfile

   

# Generated at 2022-06-13 12:56:30.571299
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None, sources=[])
    im = InventoryModule(inventory=inventory, loader=None)
    im._parse('/dev/null', ['[ungrouped]','127.0.0.1','127.0.0.2','testgroup:','testhost','[testhost:vars]','foo=bar'])
    assert (im.groups['ungrouped'].get_hosts()[0].name == '127.0.0.1')
    assert (im.groups['ungrouped'].get_hosts()[1].name == '127.0.0.2')
    assert (im.groups['testgroup'].get_hosts()[0].name == 'testhost')
    assert (im.groups['testgroup:vars'].get_vars()['foo'] == 'bar')

# Generated at 2022-06-13 12:56:39.808360
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    expected_groupnames = {'ungrouped', 'somegroup', 'naughty'}

    # Create a fake file to parse. We don't bother putting a section in
    # '[ungrouped]' because that's created implicitly by the parser.
    data = StringIO()
    data.write('[somegroup:vars]\n')
    data.write('var=value\n')
    data.write('[naughty:children] # only get coal in their stockings\n')
    data.write('somegroup\n')
    data.write('\n')
    data.seek(0)

    # Create a BlankInventory to host the parsed result.
    inventory = Inventory(host_list=[])

    # Instantiate the parser and parse our fake file.
    parser = InventoryModule()

# Generated at 2022-06-13 12:57:03.032011
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory()
    source = '''
[group1]
foo:bar
bar:baz
'''
    data = to_bytes(source)
    parser = InventoryModule(loader=None, inventory=inventory)
    parser._parse('/dev/null', data.splitlines(True))
    assert len(inventory.groups) == 1
    group1 = inventory.groups.get('group1')
    assert group1

    group1_vars = group1.vars
    assert group1_vars
    assert group1_vars.get('foo') == 'bar'
    assert group1_vars.get('bar') == 'baz'

# Generated at 2022-06-13 12:57:08.877219
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module1 = InventoryModule()
    inventory_module2 = InventoryModule()
    inventory_module1.parse('[mygroup]\nhost1\nhost2')
    expected_result = {'mygroup': {
        'hosts': ['host1', 'host2'],
        'vars': {},
        'children': []
    }}
    assert (inventory_module1.inventory.groups == expected_result)
    inventory_module2.parse('[group1]\nhost1\nhost2\n[group1:vars]\nvar1=value1\n[group1:children]\nchildgroup1')

# Generated at 2022-06-13 12:57:20.348998
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''
    def ansible_module_new(module_name, module_args=None, check_invalid_arguments=True, bypass_checks=False, no_log=False,
                           force_basic_auth=False):
        return AnsibleModule(module_name, module_args, check_invalid_arguments=check_invalid_arguments, bypass_checks=bypass_checks, no_log=no_log,
                             force_basic_auth=force_basic_auth)


# Generated at 2022-06-13 12:57:27.967657
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None, sources=None)
    inventory_module = InventoryModule(inventory=inventory)


# Generated at 2022-06-13 12:57:33.303977
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None, sources=None)
    inv = InventoryModule()
    inv.inventory = inventory

    # Testing with invalid path
    inv.parse("/", [])
    assert inventory.groups == dict()

    # Testing with valid host definition
    inv.parse("/", ["[group1]", "host1", "host2"])
    assert inventory.groups == dict(group1=Group(name='group1', hosts=['host1', 'host2'], vars={}))

    # Testing with valid child definition
    inv.parse("/", ["[group2]", "child1"])

# Generated at 2022-06-13 12:57:45.260798
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Note that this will always fail because the convert_jinja_to_data method will not have been patched during the test
    If you find a better way to patch this method, please let me know.
    '''

    class ImpliedInventory(InventoryModule):

        def __new__(cls, *args, **kwargs):
            obj = super(ImpliedInventory, cls).__new__(cls, *args, **kwargs)
            obj.inventory = ImpliedInventory.ImpliedInventory()
            return obj

        class ImpliedInventory(InventoryModule.ImpliedInventory):
            '''

            '''

            def __init__(self):
                self.groups = {}
                self.hosts = {}
                self.cache = {}

        def get_option(self, k):
            return

# Generated at 2022-06-13 12:57:56.765409
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.read_module('tests/hosts')
    assert inv.inventory.hosts['test1'] is not None
    assert inv.inventory.hosts['test1'].name == 'test1'
    assert set(inv.inventory.hosts['test1'].groups) == set(['ungrouped'])
    assert inv.inventory.groups['ungrouped'].name == 'ungrouped'
    assert inv.inventory.groups['ungrouped'].get_variable('example') == 'one'
    assert inv.inventory.groups['ungrouped'].get_variable('something') == '123'
    assert inv.inventory.groups['ungrouped'].get_variable('somethingelse') == '456'

# Generated at 2022-06-13 12:57:59.063510
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hosts')
    inventory_path = os.path.join(inventory_path, 'vpn.txt')
    InventoryModule._parse(None, inventory_path)
 

# Generated at 2022-06-13 12:58:07.358258
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:58:08.285816
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert True

# Generated at 2022-06-13 12:58:28.391792
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import tempfile
    from ansible.inventory import Inventory, Host, Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Create the inventory and data
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['localhost,'])
    inv_source = tempfile.NamedTemporaryFile(delete=False)
    inv_source.write(b'''
        [groupname]
        alpha
        beta
        gamma

        [groupname:children]
        child

        [groupname:vars]
        a_group_var=1

        [alpha]
        alpha
        beta
        gamma

        [alpha:vars]
        a_host_var=1

        [alpha:children]
        child
    ''')


# Generated at 2022-06-13 12:58:39.845861
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """ test parse method
    """
    iom = InventoryModule()
    # TODO: this needs a better test

# Generated at 2022-06-13 12:58:51.750358
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  p = InventoryModule()

# Generated at 2022-06-13 12:59:01.164077
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = '''
     [groupname]
     # a comment
     alpha
     beta:2345 user=admin      # we'll tell shlex
     gamma sudo=True user=root # to ignore comments
     '''
    inv = InventoryModule()
    inv.parse(data, "test_InventoryModule_parse()")
    # groups added in parse() should be available in inv.groups
    assert inv.groups['groupname'].name == 'groupname'
    # number of hosts in groupname should be 3
    assert len(inv.groups['groupname'].get_hosts()) == 3
    # number of variables in groupname should be 2
    assert len(inv.groups['groupname'].get_vars()) == 2


# Generated at 2022-06-13 12:59:05.279400
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    obj = InventoryModule()
    obj._filename = os.path.join('/root/ansible', 'hosts')
    obj._parse(obj._filename, ['localhost'])



# Generated at 2022-06-13 12:59:16.493565
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    fname = './test/parse'
    # default
    inv.parse(filename=fname)
    assert inv.inventory.get_host('x.y.z').get_variables() == {u'a': u"{{ 'a' }}", u'b': u"{{ 'b' }}"}
    assert inv.inventory.get_host('x.y.z').port == 222
    assert inv.inventory.get_host('x:z').get_variables() == {u'a': u"{{ 'a' }}", u'b': u"{{ 'b' }}"}
    assert inv.inventory.get_host('x:z').port == 666
    assert inv.inventory.groups['g2'].variables['q'] == u'q'

# Generated at 2022-06-13 12:59:23.796065
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    invmod = InventoryModule()
    invmod.parse('''damian.local ansible_host=192.168.1.10
localhost ansible_host=127.0.0.1
#this is a comment
[testgroup]
testhost

testhost2
testhost:23 ansible_port=23
[testgroup:vars]
ansible_port=22
[testgroup:children]
testgroup2

testgroup3
[testgroup2]
testhost2
[testgroup2:vars]
ansible_port=8888
''')
    assert invmod.inventory.get_group("testgroup").get_variables()['ansible_port'] == '22'

# Generated at 2022-06-13 12:59:25.678410
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i=InventoryModule()
    # TODO: write this test



# Generated at 2022-06-13 12:59:27.579392
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventoryModule = InventoryModule()
    inventoryModule.parse("tests/inventory_module/parse.ini")
    assert inventoryModule


# Generated at 2022-06-13 12:59:38.393928
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  # Test args, positive tests
  path = "test.ini"
  lines = ["[testgroup]",
           "testhost1:12345",
           "testhost2",
           "testhost3:12345 user=admin"]
  invmod = InventoryModule()
  invmod.inventory = FakeInventoryModule()
  invmod._filename = "test.ini"

  # method parse
  invmod._parse(path, lines)
  # host testhost1 was added to group testgroup
  testhost1 = invmod.inventory.get_host("testhost1")
  assert testhost1.get_vars()['ansible_ssh_port'] == 12345
  # host testhost2 was added to group testgroup
  testhost2 = invmod.inventory.get_host("testhost2")
  # host testhost3 was

# Generated at 2022-06-13 13:00:11.623674
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # inventory_dir is set by the test framework
    os.environ['ANSIBLE_INVENTORY'] = 'inventory_dir/hosts'

    #Create an instance of the class InventoryModule
    inventory = InventoryModule()
    #Create an instance of the class AnsibleInventory
    ansible_inventory = AnsibleInventory()
    #Set the inventory attribute of the instance of the class InventoryModule
    inventory.inventory = ansible_inventory
    #Parse the inventory file
    inventory.parse(os.environ['ANSIBLE_INVENTORY'])
    #Get the group 'ungrouped'
    group = ansible_inventory.groups['ungrouped']
    #Get the group 'group1'
    group1 = ansible_inventory.groups['group1']
    #Get the group 'group2'
    group2 = ansible

# Generated at 2022-06-13 13:00:20.488369
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    module._parse('/opt/ansible/inventory/hosts', ['[ungrouped]','host1','host2','[group2]','host1','host3'])
    assert module.inventory.groups.has_key('ungrouped')
    assert module.inventory.get_host('host1').get_vars()['group_names'] == ['ungrouped']
    assert module.inventory.get_host('host1').get_vars()['inventory_dir'] == '/opt/ansible/inventory'
    assert module.inventory.get_host('host2').get_vars()['inventory_dir'] == '/opt/ansible/inventory'
    assert module.inventory.get_group('group2').get_vars()['inventory_dir'] == '/opt/ansible/inventory'

# Unit test

# Generated at 2022-06-13 13:00:31.781416
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    mod = InventoryModule()

    class TestInventory(object):
        groups = {}

        def add_group(self, groupname):
            self.groups[groupname] = Group(groupname)

        def set_variable(self, groupname, key, value):
            self.groups[groupname].set_variable(key, value)

        def add_child(self, groupname, child):
            self.groups[groupname].add_child(child)

    # Test parsing a valid inventory. We have no current way to test that
    # the result is correct, but we check to the best of our current ability
    # that the result is at least valid.

# Generated at 2022-06-13 13:00:33.567863
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: https://github.com/ansible/ansible/issues/13522
    # write a unit test here
    pass


# Generated at 2022-06-13 13:00:40.803399
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ungrouped = Group(name='ungrouped')
    hosts = dict()
    groups = dict()
    groups['ungrouped'] = ungrouped
    
    inv = Inventory(hosts=hosts, groups=groups)
    
    inventory_filename = 'inventory_loader.yaml'
    inventory_basename = 'inventory_loader'
    inventory_basedir = '.'
    loader = InventoryModule(None, inventory_filename, 
                             inv,
                             inventory_basename, 
                             inventory_basedir)

    
    
    # Test 1:
    # Build the inventory
    inventory = dict()
    inventory['hosts'] = dict()
    inventory['hosts']['host-01'] = dict()

# Generated at 2022-06-13 13:00:43.480541
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    assert inv.parse('/etc/ansible/hosts', '# this is not a real file') == dict()


# Generated at 2022-06-13 13:00:50.106001
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    assert callable(inventory_module.parse) == True
    with pytest.raises(AnsibleError):
        inventory_module.parse(None, None)
    
    with pytest.raises(AnsibleParserError):
        inventory_module._parse(None, None)
    
    with pytest.raises(AnsibleError):
        inventory_module._raise_error('error')
        
    assert inventory_module.patterns is None
    inventory_module._compile_patterns()
    assert isinstance(inventory_module.patterns['section'], re._pattern_type)
    assert isinstance(inventory_module.patterns['groupname'],re._pattern_type)
    
    assert inventory_module._parse_value('some_value') == 'some_value'


# Generated at 2022-06-13 13:00:52.793340
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # prepare
    # 
    # parse
    #
    # cleanup
    #
    # verify
    assert True


# Generated at 2022-06-13 13:01:00.726722
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:01:15.235710
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=DictDataLoader({}))

    im = InventoryModule(inventory)

    # Basic parsing test - it's probably worthwhile testing the individual subroutines more thoroughly later.

    data = u'''
    [webservers]
    foo.example.org

    [dbservers]
    one.example.org
    two.example.org ansible_port=5555

    [atlanta]
    host1
    host2:2222

    [raleigh]
    host2
    host3

    [southeast:children]
    atlanta
    raleigh

    [southeast:vars]
    some_server=foo.example.org
    halon_system_timeout=30
    self_destruct_countdown=60
    escape_pods=2
    '''

   

# Generated at 2022-06-13 13:02:12.409401
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule(Inventory())

# Generated at 2022-06-13 13:02:18.808627
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module._parse_config(None)
    inventory_module._parse_config('')
    inventory_module._parse_config('simple')
    inventory_module._parse_config('simple_with_port')
    inventory_module._parse_config('simple_with_variables')
    inventory_module._parse_config('simple_with_variables_and_multiple_parents')


# Generated at 2022-06-13 13:02:24.409389
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule(cache={})
    inv._parse(path='test_path', lines=['[testgroup]', 'localhost'])
    assert inv.groups['testgroup'].hosts['localhost'].name == 'localhost'



# Generated at 2022-06-13 13:02:33.654284
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Set up object
    inv = InventoryModule(inventory='test/unit/myhosts')
    inv._compile_patterns() # FIXME: workaround, inventories should be initialized correctly
    inv.parse('test/unit/myhosts')

    # Assert groups
    groups = ['group1', 'group2', 'ungrouped']
    assert inv.inventory.groups.keys() == groups

    # Assert group1 children
    group1_children = ['group2']
    assert inv.inventory.groups['group1'].child_groups.keys() == group1_children
    assert inv.inventory.groups['group1'].parent_groups.keys() == []

    # Assert group2 children
    group2_children = []
    assert inv.inventory.groups['group2'].child_groups.keys() == group2_children


# Generated at 2022-06-13 13:02:44.440091
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inven_mod = InventoryModule()
    data = ["./tests/inventory/test_inventory", "./tests/inventory/test_inventory_blank_lines", "./tests/inventory/test_inventory_duplicate_hosts", "./tests/inventory/test_inventory_empty_groups", "./tests/inventory/test_inventory_duplicate_child_group", "./tests/inventory/test_inventory_host_with_ipv6", "./tests/inventory/test_inventory_group_vars_children", "./tests/inventory/test_inventory_with_vars_and_comments"]
    for test_inventory_path in data:
        inventory_json_filename = test_inventory_path.replace("./tests/inventory", "./output")

# Generated at 2022-06-13 13:02:48.282834
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    parse
    '''
    inventory = InventoryManager(None, None)
    inventory_module = InventoryModule(None, None, None, inventory)
    inventory_module.parse("path")

test_InventoryModule_parse()

# Generated at 2022-06-13 13:03:00.034107
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print("\ntest_InventoryModule_parse")
    inventory_module = InventoryModule()
    from ansible.utils.display import Display

    options = Options()
    display = Display()
    display.verbosity = 1
    inventory_module.set_options(options)
    inventory_module.display = display
    inventory_module.parse("tests/inventory_v2/hosts")

# Generated at 2022-06-13 13:03:15.446993
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # initializing the inventory
    inventory = Inventory("")

    # initialize the module
    module = InventoryModule(inventory=inventory)
    data = [
        '[test]',
        'test.example.com',
        '[test:vars]',
        'test_variable=test_value',
        '[test:children]',
        'child_group',
    ]
    module._parse(path='/BOGUS/', data=data)
    assert len(inventory.groups) == 3
    assert 'test' in inventory.groups
    assert 'child_group' in inventory.groups
    assert 'test:vars' in inventory.groups
    assert len(inventory.groups['test'].get_hosts()) == 1
    assert len(inventory.groups['test'].get_hosts()[0].vars) == 1

# Generated at 2022-06-13 13:03:23.460910
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory()
    path = "/path/to/inventory.file"

# Generated at 2022-06-13 13:03:34.283269
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Testing ungrouped entries
    i = InventoryModule()
    i._parse('/somepath/file1', ['alpha', 'beta', 'gamma'])
    assert len(i.groups['ungrouped'].hosts) == 3
    assert len(i.groups['ungrouped'].vars) == 0
    assert len(i.groups['ungrouped'].children) == 0

    # And now testing their values
    assert i.groups['ungrouped'].hosts['alpha'].port == 22
    assert i.groups['ungrouped'].hosts['alpha'].address == 'alpha'
    assert i.groups['ungrouped'].hosts['alpha'].vars == {}

    assert i.groups['ungrouped'].hosts['beta'].port == 22