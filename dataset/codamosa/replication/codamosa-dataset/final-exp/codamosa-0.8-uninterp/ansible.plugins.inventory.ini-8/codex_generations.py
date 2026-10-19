

# Generated at 2022-06-13 12:55:13.275616
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory(loader=DictDataLoader({}))
    inventory_file = '''
[group1]
web1
web3:2223

[group1:vars]
some_server_variable=foo

[group2:vars]
invalid_variable={{foo
another_invalid_variable={{bar}}

[group2]
web2 ansible_ssh_host=web1 ansible_ssh_user=root

[group3]
localhost ansible_connection=local
web[0:2:2]

[group4]
web[0:2:2]
'''
    inventory.loader.set_basedir(os.path.join('playbooks', 'inventory', 'test_inventory'))
    inventory.parse_inventory(inventory_file)


# Generated at 2022-06-13 12:55:22.108234
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory.parse(BASE_DIR + '/test_data/hosts')
    # print( inventory.groups)
    assert inventory.groups['all'].hosts['host2.example.org'].vars['ansible_ssh_host'] == '192.168.1.3'
    assert inventory.groups['all'].hosts['host2.example.org'].vars['ansible_ssh_port'] == 2200
    assert inventory.groups['all'].hosts['host3.example.org'].vars['ansible_ssh_host'] == '192.168.1.4'
    assert inventory.groups['all'].hosts['host3.example.org'].vars['ansible_ssh_port'] == 22

# Generated at 2022-06-13 12:55:32.837044
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:55:46.085576
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(["general", "all"])
    inventory._inventory_plugins = dict(module=dict(class_name="InventoryModule"))
    inventory.set_playbook_basedir(os.path.join(os.path.dirname(__file__), '..'))
    inventory._load_inventory_sources()
    assert len(inventory.get_groups_dict()) == 2
    assert 'all' in inventory.get_groups_dict()
    assert 'general' in inventory.get_groups_dict()
    assert 'foo' in inventory.get_groups_dict()['general']['hosts']
    assert 'bar' in inventory.get_groups_dict()['all']['hosts']

# Generated at 2022-06-13 12:55:51.154654
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  from ansible.inventory.host import Host
  from ansible.inventory.group import Group
  from ansible.parsing.yaml.loader import AnsibleLoader
  from ansible.parsing.yaml.objects import AnsibleUnicode

  # Test 1: Valid inventory file with no comment lines and no host vars (integer and string variables)
  InventoryModule_parse_hostnames = ['host1', 'host2', 'host3', 'host4', 'host5', 'host6', 'host7', 'host8', 'host9', 'host10']
  InventoryModule_parse_groupname = 'ungrouped'
  InventoryModule_parse_filename = 'InventoryModule_parse_test1.txt'

# Generated at 2022-06-13 12:55:59.765607
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventorymodule = InventoryModule("hosts.yml", "/path/to/default/")
    # Test 1
    group_name = "test_hosts"
    group_vars = {}
    host_pattern = "test1"
    host_vars = {"ansible_user": "ubuntu"}
    port = 22
    try:
        inventorymodule.parse(group_name, group_vars, host_pattern, host_vars, port)
    except Exception as e:
        if "Error parsing host definition 'test1' : No closing quotation" in e.message:
            pass
        else:
            raise e
    # Test 2
    group_name = "test_hosts"
    group_vars = {}
    host_pattern = "test1"
    host_vars = {"ansible_user": "root"}

# Generated at 2022-06-13 12:56:14.034268
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    load_plugin("inventory/static_inventory")
    inv_module = InventoryModule()
    inv_module.groups = {"ungrouped": {}}
    inv_module.hosts = {}
    inv_module.patterns = {}
    inv_module.enable_plugins()
    # Test 1
    with pytest.raises(AnsibleParserError):
        inv_module._parse("/root", [])
    # Test 2
    with pytest.raises(AnsibleError) as execinfo:
        inv_module._parse("/etc/ansible/hosts", ["[group1:children", "group2", "group3]", "[group2]", "127.0.0.1"])

# Generated at 2022-06-13 12:56:22.258354
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_data = '''host1.example ansible_ssh_host=host1.example ansible_ssh_port=2222
host2.example
host3.example
'''
    inventory = Inventory(loader=DataLoader())
    inventory_source = InventoryModule()
    inventory_source._populate_host_vars = MagicMock()
    inventory_source._parse(inventory_data)
    for host in ['host1.example', 'host2.example', 'host3.example']:
        inventory_source._populate_host_vars.assert_any_call([host], {}, None, None)


# Generated at 2022-06-13 12:56:30.691255
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    inv = InventoryModule([])
    data = [
        "[test]",
        "test1",
        "test2:2222",
        "test3 user=root",
        "test4 user=foo sudo=True",
        "[test:vars]",
        "a=b",
        "c=d",
        "e=f g",
        "[test:children]",
        "c1",
        "c2"
    ]

    inv.parse(data)

    # check hosts
    assert(str(inv.inventory.groups['test'].hosts) == "set(['test1', 'test2', 'test3', 'test4'])")

    # check port
    assert(inv.inventory.groups['test'].hosts['test2'].port == 2222)

# Generated at 2022-06-13 12:56:39.939637
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    mock_loader = DataLoader()
    with mock.patch("os.path.exists") as _mock_os_path_exists:
        inventory_dir = "dir"
        path = os.path.join(inventory_dir, "somefile")
        _mock_os_path_exists.return_value = True
        mock_data = [
            "[servers:children]\n",
            "east   \n"  # No trailing comment
        ]
        with mock.patch("ansible.inventory.InventoryFile._read_data_from_file") as _mock_read_data_from_file:
            _mock_read_data_from_file.return_value = mock_data

# Generated at 2022-06-13 12:57:11.866930
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    
    # FIXME: Replace with proper unit test
    
    # FIXME:
    import sys
    
    inventory_file = './tests/' + sys.argv[1]
    
    with open(inventory_file) as f:
        inventory_text = f.read()

    inventory = InventoryModule()

    inventory.parse(inventory_text)
    # print( inventory.groups )
    
    # XXX: This test needs the following file ./tests/inventory.ini
    f = open('./tests/inventory.ini')
    full_inventory = f.read()
    f.close()
    inventory.parse(full_inventory)
    
    

# FIXME: Move this to model.py

# Generated at 2022-06-13 12:57:22.294042
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print ("test method parse of class InventoryModule")

    inv = InventoryModule()

    # [default]
    # testhost
    # [group1]
    # testhost:9090
    # [group1:vars]
    # testkey1="testvalue1"
    # testkey2=123
    # [group2]
    # testhost
    # [group2:vars]
    # testkey2=321
    # [group2:children]
    # group1

    # testhost
    assert len(inv.hosts)==0
    assert inv not in inv.hosts
    assert 'testhost' not in inv.hosts

    testhost = Host('testhost')
    assert testhost not in inv.hosts

    # [group1]
    # testhost:9090
    # [group1

# Generated at 2022-06-13 12:57:30.626558
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_data = """
[group_name]
host_name ansible_host=192.0.2.1 ansible_user=user ansible_port=2222
"""

    p = InventoryParser(None)
    p.parse(inv_data.split('\n'))
    assert p.inventory.groups['group_name'].vars['ansible_user'] == 'user'
    assert p.inventory.groups['ungrouped'].vars['ansible_port'] == '2222'
 

# Generated at 2022-06-13 12:57:39.091614
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:57:49.622100
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # init InventoryModule
    inventory_module = InventoryModule()
    # init pattern
    pattern = re.compile(to_text(r'''^\[
                    ([^:\]\s]+)             # a group name (see groupname below)
                    (?::(\w+))?             # optional : and tag name
                \]
                \s*                         # ignore trailing whitespace
                (?:\#.*)?                   # and/or a comment till the
                $                           # end of the line
            ''', errors='surrogate_or_strict'), re.X)
    m = pattern.match(to_text('[mygroup]', errors='surrogate_or_strict'))
    assert m.groups() == ('mygroup', None)


# Generated at 2022-06-13 12:57:58.978820
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """Check that the parses of the method InventoryModule are working.
    """
    inventory = InventoryManager(loader=DictDataLoader({}))
    # Create a file with a single host
    hosts_file = """
[postgresql]
somehost
"""
    temp_file = NamedTemporaryFile(suffix='.yml', mode='w+b', prefix='ansible_test_')
    temp_file.write(to_bytes(hosts_file))
    temp_file.seek(0)
    temp_file_name = to_text(temp_file.name)
    inv_mod = InventoryModule()
    inv_mod.parse(temp_file_name, inventory)
    # Check the parsing
    assert inventory.list_hosts('postgresql') == ['somehost']

# Generated at 2022-06-13 12:57:59.660045
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 12:58:07.635437
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Constructor
    test_module = InventoryModule('test_module')

    test_module.parse('./test/test_inventory_module.cfg')
    # Get groups
    groups = list(test_module.inventory.groups.keys())
    assert len(groups) == 4
    assert 'all' in groups
    assert 'ungrouped' in groups
    assert 'group1' in groups
    assert 'group2' in groups

    # Get hosts
    hosts = list(test_module.inventory.hosts.keys())
    assert len(hosts) == 5
    assert 'host1' in hosts
    assert 'host2' in hosts
    assert 'host3' in hosts
    assert 'hostname1' in hosts
    assert 'hostname2' in hosts
    assert 'host1' in test_module.inventory.get_host

# Generated at 2022-06-13 12:58:14.428485
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule(loader=None, groups={}, basedir='', _vault_password=None)
    inv_path = u"/home/fj/ansible/ansible/lib/ansible/plugins/inventory/"
    inv_path_list = u"/home/fj/ansible/ansible/lib/ansible/plugins/inventory/test_multiple_sources"
    list_inv_path = [u"inventory_test_dir/test_children", u"inventory_test_dir/test_vars"]
    # Test case with not a file path
    try:
        inventory.parse("fj", "hosts")
    except AnsibleParserError as e:
        assert "Path not a file or directory: fj" in str(e)
    # Test case with a file path and not yaml or ini file

# Generated at 2022-06-13 12:58:21.028501
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''
    inventory = InventoryManager(Inventory(), loader=DataLoader())
    inventory_mod = InventoryModule(inventory)
    try:
        path = 'test_path'
        data = ['[group1]', 'localhost ansible_connection=local']
        inventory_mod._parse(path, data)
    except Exception as exception:
        assert False, 'Test failed because: %s' %  exception


# Generated at 2022-06-13 12:58:55.937421
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None, sources=None, hosts=None, groups=None,
                                 parser=None, variation=None, host_list=None)

# Generated at 2022-06-13 12:59:05.239504
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule(loader=None, inventory=None)
    inventory_module._filename = './test_resources/ini_inventory/test_inventory.ini'
    with open('./test_resources/ini_inventory/test_inventory.ini','r') as f:
        inventory_module._parse('./test_resources/ini_inventory/test_inventory.ini', f.readlines())
    assert inventory_module.inventory.groups['group1']['vars'] == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Generated at 2022-06-13 12:59:16.494069
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create an instance of InventoryModule and call method parse
    i = InventoryModule()
    i.parse('test.ini', '''
[all:vars]
ansible_ssh_user=user

[redfish]
172.17.0.11 ansible_ssh_user=redfish
172.17.0.12 ansible_ssh_user=redfish

[dm]
# Remote hosts will be accessed by user `redfish`
172.17.0.21 ansible_ssh_user=redfish
172.17.0.22 ansible_ssh_user=redfish

[mock]

[mock:children]
dm redfish
''')
    # Compare result to reference

# Generated at 2022-06-13 12:59:21.638092
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_inventory = '''
    Localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
    [group1]
    host1 ansible_host=10.2.2.2 ansible_ssh_user=root ansible_ssh_pass=rootsecret
    host2
    host3
    [group2]
    host4
    host5
    [group3:children]
    ungrouped
    group2
    '''
    inven = InventoryModule(None, None)

    inven._parse('inventory', test_inventory.splitlines())
    assert inven.inventory.groups['ungrouped'].hosts['localhost'].vars['ansible_python_interpreter'] == '/usr/bin/python3'
    assert inven.inventory.groups['group1'].host

# Generated at 2022-06-13 12:59:22.665792
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    assert True

# Generated at 2022-06-13 12:59:33.846087
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Testing 'parse' method of class InventoryModule
    #
    # Args:
    #    - data (str): String with inventory contents
    #
    # Returns:
    #    - None
    data = '''[testgroup1]
    node1
    node2
        # line        
    [testgroup2:children]
    testgroup1
    [testgroup2:vars]
    var1=value1
    var2=value2
    '''

    inv_obj = InventoryModule(None, None)
    inv_obj.parse(data)

    assert ('testgroup1' in inv_obj.inventory.groups.keys())
    assert ('testgroup2' in inv_obj.inventory.groups.keys())


# Generated at 2022-06-13 12:59:44.198170
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ##############################################################################################
    # This is the test file
    yaml_file = '''
    all:
    hosts:
        all_hosts:
            ansible_ssh_host: 192.168.1.1
    children:
        ungrouped:
            hosts:
                all_hosts:
            children:
                windows:
    '''
    ##############################################################################################
    # This is the expected inventory data

# Generated at 2022-06-13 12:59:57.431229
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import json
    import os
    import io
    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.inventory.host import Host

    inventory = InventoryModule(loader=None, variable_manager=None, host_list='')
    plugin = InventoryModule(loader=None, variable_manager=None, host_list='')

    global test_pass
    global test_fail
    test_pass = 0
    test_fail = 0

    def _load_file(filename):
        dirpath = os.path.abspath(os.path.dirname(__file__))
        data = None

        p = os.path.join(dirpath, 'files/%s' % filename)
        with io.open(p, 'rb') as f:
            data = f.read()

        return data



# Generated at 2022-06-13 13:00:03.286892
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ansible_path = os.path.dirname(__file__) + "/../../"
    #ansible_path = os.path.dirname(__file__) + "/../../"
    #ansible_path = os.path.dirname(__file__) + "/../../../"
    inv = InventoryModule(filename=ansible_path+'contrib/inventory/test_inventory.ini', groups=True)
    print(inv.groups)
    print(inv.inventory.get_groups_dict())
    for key, value in inv.get_groups_dict().items():
        print("{}: {}".format(key, value))
    print("my_group: ", inv.groups['my_group'])
    print("my_group: ", inv.inventory.groups['my_group'])
    #print("my_

# Generated at 2022-06-13 13:00:12.869107
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

    inventory_data = '''
[group1]
foo  bar=baz
    baz
ansible_ssh_host=quux
[group:children]
group1
group2
[group1:vars]
group_var=value
[group2:vars]
group2_var=value
    '''

    inventory = InventoryManager(loader=None, sources='')
    # we do not have a filename, so we pass in None
    inventory_module.parse(None, inventory_data, inventory)

    assert 'group1' in inventory.groups
    assert 'foo' in inventory.groups['group1'].hosts
    assert 'group1' in inventory.hosts['foo'].vars

# Generated at 2022-06-13 13:01:13.781222
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
	
    class Inventory(object):

         def __init__(self):
             self.groups = dict()
             self.hosts = dict()

         def add_group(self, group):
             self.groups[group] = Group(group)

         def add_host(self, host, port=None):
             self.hosts[host] = Host(host)

         def add_child(self, group, child):
             if group in self.groups:
                 group = self.groups[group]
             self.groups[child] = self.groups[child].copy()
             if child in self.groups:
                 child = self.groups[child]
             group.add_child_group(child)

         def set_variable(self, group, key, value):
             self.groups[group].set_variable(key, value)



# Generated at 2022-06-13 13:01:23.841282
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    result = inv.parse('test/test_inventory.ini', cache=False)
    assert_equals(result, True)
    hosts1 = inv.inventory.get_hosts('all')
    assert_true(hosts1[0].name == 'alpha')
    assert_true(hosts1[0].get_vars()['user'] == 'test')
    assert_true(hosts1[0].get_vars()['port'] == '22')
    assert_true(hosts1[3].name == 'epsilon')
    assert_true(hosts1[3].get_vars()['user'] == 'admin')
    assert_true(hosts1[3].get_vars()['port'] == '24')

# Generated at 2022-06-13 13:01:24.935386
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  parser=InventoryModule()
  parser.parse('/home/a/ansible/inventory','')


# Generated at 2022-06-13 13:01:25.497552
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:01:26.057247
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:01:33.486796
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:01:44.826223
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule(None)
    i.parse("""
    # a comment
    [one]
    a
    [two:vars]
    a = b
    b:c
    c = something here
    [three:children]
    three_one
    three_two
    [three_one:vars]
    d = something else
    """, '/dev/null')
    print(i.host_vars['a'])
    assert 'a' in i.host_vars
    assert 'c' in i.host_vars
    assert 'b:c' in i.host_vars
    assert i.host_vars['a'] == {}
    assert i.host_vars['c'] == {'var': 'something here'}
    assert i.host_vars['b:c']

# Generated at 2022-06-13 13:01:55.680901
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryScript.from_file('get_inventory.py')
    src = 'inventory'
    ic = InventoryModule(i, src)

# Generated at 2022-06-13 13:02:02.445166
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Unit test for method parse of class InventoryModule
    :return:
    """
    module = InventoryModule()
    path = None
    source = "test.ini"
    try:
        module.parse(path, source)
    except AnsibleParserError as e:
        print("Error in test_parser: {}".format(e))


if __name__ == "__main__":
    test_InventoryModule_parse()

# Generated at 2022-06-13 13:02:10.929694
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

    # No inventory file
    inventory_module.parse('/path/not/yet/existing')
    
    # Invalid inventory file
    with open('/tmp/invalid_inventory.yml', 'w+') as f:
        f.write('---')
    try:
        inventory_module.parse('/tmp/invalid_inventory.yml')
    except AnsibleParserError:
        pass
    finally:
        os.remove('/tmp/invalid_inventory.yml')

    # Valid inventory file
    with open('/tmp/valid_inventory.yml', 'w+') as f:
        f.write('all:\n')
        f.write('  hosts:\n')
        f.write('    localhost\n')

# Generated at 2022-06-13 13:03:51.733822
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Unit test for method parse of class InventoryModule
    # given an inventory module of type ini
    uut = InventoryModule(loader=None, inventory=None, pattern=None, vault_password=None)
    # when it is parsed
    uut.parse("/path/to/inventory", "{}")
    # then the contents of the inventory should be parsed
    pass


# Generated at 2022-06-13 13:04:01.575974
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ansible_module = AnsibleModule(argument_spec=dict())
    ansible_module.fail_json = Mock(side_effect=AnsibleFailJson)
    inventory = InventoryManager()
    imp = InventoryModule(ansible_module, inventory, {}, [])
    imp._raise_error = Mock()
    imp._compile_patterns = Mock()
    imp._parse_host_definition = Mock(side_effect=[('host_name', 23, {'key': 'value'}), ('host_name', 23, {'key': 'value'}), ('host_name', 23, {'key': 'value'})])
    imp._expand_hostpattern = Mock(side_effect=[(['host_name'], 23), (['host_name'], 23), (['host_name'], 23)])
    imp._

# Generated at 2022-06-13 13:04:11.211967
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Build class
    inventory_module = InventoryModule()
    # Build test file
    import tempfile
    fd, tf = tempfile.mkstemp()
    os.close(fd)
    with open(tf, 'w') as f:
        f.write("""
            [testgroup]
            host1
        """)
    # execute parse
    inventory_module.parse(tf)
    # destroy test file
    os.remove(tf)
    # check results
    assert inventory_module.get_host("host1")
    assert len(inventory_module.get_host("host1").get_vars()) == 0
    assert inventory_module.get_host("host1").groups[0].name == 'testgroup'
    assert len(inventory_module.get_host("host1").get_groups()) == 1



# Generated at 2022-06-13 13:04:18.590041
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
        Tests whether the Inventory in the InventoryModule is filled with the information
        found in a given hosts file.
    '''
    # Setup the test.
    hostFile = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    hostFile.write(bytes('''
    [servers]
    server1 ansible_ssh_port=22
    server2 ansible_ssh_port=33
    server3 ansible_ssh_port=44
    server4 ansible_ssh_port=55
    server5

    [webserver:vars]
    ansible_ssh_port=22
    python_version=3.4
    '''))
    hostFile.close()
    hostFile = hostFile.name

    inv = InventoryModule()
    # Test the parse function

# Generated at 2022-06-13 13:04:31.920384
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:04:45.443100
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #
    # Parsing a single host in the ungrouped group
    #
    path = '/tmp/hosts'
    data = [
        'localhost',
    ]
    inv_mod = InventoryModule()
    inv_mod._parse(path, data)

    assert inv_mod.inventory.groups[u'ungrouped'].get_host('localhost') is not None

    #
    # Parsing a single host in the ungrouped group with port
    #
    path = '/tmp/hosts'
    data = [
        'localhost:10000',
    ]
    inv_mod = InventoryModule()
    inv_mod._parse(path, data)

    assert inv_mod.inventory.groups[u'ungrouped'].get_host('localhost') is not None

# Generated at 2022-06-13 13:04:54.787001
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule('tests/inventory/unittest_hosts_ascii.ini')
    inv.parse_inventory(inv.file_path)
    assert inv.inventory.groups['ungrouped'].hosts['example.com'].port == 6379
    inv = InventoryModule('tests/inventory/unittest_hosts_ascii.ini')
    inv.parse_inventory(inv.file_path)
    assert inv.inventory.groups['ungrouped'].hosts['example.com'].name
