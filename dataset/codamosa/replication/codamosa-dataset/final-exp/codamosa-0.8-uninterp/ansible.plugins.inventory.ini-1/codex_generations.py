

# Generated at 2022-06-13 12:55:05.038200
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory(loader=None, variable_manager=None, host_list='/dev/null')
    inventory.parse_inventory('test/units/data/inventory.ini')


# Generated at 2022-06-13 12:55:14.275112
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # inventory_module_obj = None
    # # print(inventory_module_obj)

    # inventory_module_obj = InventoryModule('test_hosts')
    # # print(inventory_module_obj)

    inventory_module_obj = InventoryModule()

    inventory_module_obj.inventory = Inventory([])
    # print(inventory_module_obj)


    data = [
        'a',
        'b',
        'c'
    ]
    path = 'test_hosts'
    inventory_module_obj._parse(path, data)

    # for module in inventory_module_obj.inventory.groups:
    #     print(module)
    #     print(inventory_module_obj.inventory.groups[module])

    # inventory_module_obj.inventory.clear_pattern_cache()
    # print(inventory_

# Generated at 2022-06-13 12:55:22.981447
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    TEST_DIR = 'test_data'
    TEST_SRC_DIR = 'test_data/test_src'
    TEST_DST_DIR = 'test_data/test_dst'
    TEST_DIFF_DIR = 'diff_data'
    TEST_FAIL_DIR = 'fail_data'

    if not os.path.exists(TEST_SRC_DIR):
        os.makedirs(TEST_SRC_DIR)

    if not os.path.exists(TEST_DST_DIR):
        os.makedirs(TEST_DST_DIR)

    if not os.path.exists(TEST_FAIL_DIR):
        os.makedirs(TEST_FAIL_DIR)

    src_files = os.listdir(TEST_SRC_DIR)

# Generated at 2022-06-13 12:55:33.058378
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    filename = 'ansible/inventory/hosts'
    inventory = dict(
        plugin="ansible.inventory.hosts",
        _options=dict(host_list=[filename]),
        host_list=[filename],
        groups={},
        host_patterns={filename: [ '*' ] },
        basedir=get_basedir(),
        variable_manager=dict(
            hostvars={},
            groupvars={},
            options=dict(
                _rfile_attrs=dict(),
            ),
        ),
    )
    inv = InventoryModule(filename)
    inv._load(loader=DataLoader(), path=filename)


# Generated at 2022-06-13 12:55:40.168202
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
	
	#inventory_module.py source code line: 213
	#prepare input
	path = "hosts"
	

# Generated at 2022-06-13 12:55:44.975518
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #inventory = AnsibleInventory()
    path = os.path.join(os.path.dirname(__file__), 'data', 'inventory')
    script = InventoryModule(path, inventory=None)
    # TODO: complete test
    script.parse()


# Generated at 2022-06-13 12:55:48.154653
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  inventory_path = "./flask/Ansible/inventory/hosts"
  inventory_obj = InventoryModule()
  inventory_obj.parse(inventory_path)
  return(inventory_obj)


# Generated at 2022-06-13 12:55:57.841745
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule(loader=None, variable_manager=None, host_list='hosts')

    # Scenario 1
    #
    # No groups, no hosts, but several variable assignments.

    data = '''
[all:vars]

ansible_ssh_user=root
ansible_connection=ssh
'''
    inventory._parse(path=None, lines=data.splitlines())

    assert sorted(inventory.inventory.groups) == ['all']
    assert len(inventory.inventory.groups['all'].hosts) == 0
    assert sorted(inventory.inventory.groups['all'].vars.keys()) == ['ansible_connection', 'ansible_ssh_user']
    assert inventory.inventory.groups['all'].vars['ansible_ssh_user'] == 'root'

# Generated at 2022-06-13 12:56:13.185337
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # create an instance of the class
    test_inventory = InventoryModule()
    # ensure that the inventory is empty before the parse
    assert len(test_inventory.hosts) == 0
    test_inventory.parse("test/test_inventory_ini.txt", None, None, None)  # run the parse method
    # ensure that the inventory was created
    assert len(test_inventory.hosts) == 5
    assert test_inventory.groups["testgroup"]['vars']['testvar'] == "this is a test variable"

# create unparsed inventory
test_inventory = InventoryModule.unparsed_inventory()
# add a host to the inventory
test_inventory.add_host("host1")
# create a group
test_inventory.add_group("testgroup")
# add variables to the group
test_inventory.set

# Generated at 2022-06-13 12:56:23.415582
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    print('Testing InventoryModule.parse()')

    # Create an instance of our class
    inventory = InventoryModule()

    # Create a fake inventory file with some data

# Generated at 2022-06-13 12:56:44.248869
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    import tempfile
    from yaml import safe_load

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    #import logging
    #logging.basicConfig()

    #yaml_inventory = """
    #  all:
    #    children:
    #      servers:
    #        hosts:
    #          localhost:
    #      workstations:
    #        hosts:
    #          localhost:
    #          www.example.com:
    #      datacenters:
    #        children:
    #          rack1:
    #            hosts:
    #              www.somewhere.com:
    #              www.somewhereelse.com:
    #

# Generated at 2022-06-13 12:56:51.968111
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    filename = 'inventory.ini'
    data = [
        '[group1]',
        'host1',
        '[group1:vars]',
        'key1=value1',
        '[group2]',
        'host2',
        '[group2:vars]',
        'key2=value2',
        '[group3:children]',
        'group1',
        'group2',
        '[group3:vars]',
        'key3=value3'
    ]
    i = InventoryModule()
    i.parse(filename, data)
    assert i.inventory.groups['group1'].name == 'group1'
    assert i.inventory.groups['group1'].get_hosts()[0].name == 'host1'
    assert i.inventory.groups['group1'].get_v

# Generated at 2022-06-13 12:56:53.957146
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module.parse("/path/to/inventory","[ungrouped]\nhost1")


# Generated at 2022-06-13 12:57:05.204851
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule(None)
    inv = Inventory()
    i.inventory = inv
    i._parse('1', ["[group1]", "host1"])
    assert inv.get_hosts('group1')
    assert inv.get_host('host1')
    assert inv.get_host('host1').get_vars() == {}
    i.inventory = inv
    i._parse('1', ["[groupname]", "host2:123"])
    assert len(inv.get_hosts('groupname')) == 1
    assert inv.get_host('host2').get_vars() == {'ansible_port': '123'}
    assert inv.get_host('host2').get_variable('ansible_port') == '123'
    i.inventory = inv

# Generated at 2022-06-13 12:57:15.329534
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    """ test the parsing function of class InventoryModule """

    import ansible.inventory.host
    import ansible.inventory.group

    # we create a temporary file
    tmpfile = tempfile.mkstemp(prefix='InventoryModule_parse')[1]

# Generated at 2022-06-13 12:57:18.642924
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule('mock_inventory.cfg')
    parsed_inventory = inventory_module.parse(dict(groups=dict()))
    assert parsed_inventory.groups == dict()


# Generated at 2022-06-13 12:57:25.440423
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()


from ansible.inventory.host import Host
from ansible.inventory.group import Group

from ansible.utils.vars import combine_vars
# a simple inventory for use in tests


# Generated at 2022-06-13 12:57:36.198401
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test input
    lines = [
    '[groupname]',
    'alpha:2345 user=admin      # we\'ll tell shlex',
    'gamma sudo=True user=root # to ignore comments'
    ]

    # Test setup
    path = 'test_path'

    # Test call
    test_inventory = InventoryModule()

# Generated at 2022-06-13 12:57:41.351454
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    # At the moment there is no parse unit test.
    # TODO: we need something to feed in and return as an object
    #inventory_module._parse(self)
    print("test_InventoryModule_parse has no unit tests at the moment")


# Generated at 2022-06-13 12:57:45.492916
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # prepare inputs
    path = 'some path'
    lines = ['some line']
    # create instance
    # pass inputs as *args
    instance = InventoryModule(path, lines)
    result = instance.parse()
    assert result is None # TODO: implementation of test


# Generated at 2022-06-13 12:58:02.780390
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    lines = [
        '[group1]',
        'host1',
        'host2 ansible_port=22 ansible_host=server.example.org',
        'host3',
        '',
        '# A comment should be ignored.',
        '',
        '[group2]',
        'host4',
        '[group3:children]',
        'group1',
        'group2',
        '''[group4:vars]
foo=baz
bar={{ myvar }}
herp=derp
''',
        '''[group5:vars]
foo={{ myvar }}
bar=baz
''',
    ]

    inventory_filename = 'inventory'
    inventory = Inventory(loader=DictDataLoader({inventory_filename: '\n'.join(lines)}))
    inventory_module

# Generated at 2022-06-13 12:58:17.923714
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module._populate_host_vars = MagicMock()
    inventory_module._parse_group_name = MagicMock()
    inventory_module._parse_variable_definition = MagicMock()
    inventory_module._parse_host_definition = MagicMock()
    inventory_module._expand_hostpattern = MagicMock()
    inventory_module._compile_patterns = MagicMock()
    lines = ["[groupname]", "[groupname:children]", "[groupname:vars]"]
    inventory_module._parse(MagicMock(), lines)
    assert inventory_module.patterns["groupname"].match.call_count == 3
    assert inventory_module.patterns["section"].match.call_count == 3


# Generated at 2022-06-13 12:58:28.089454
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager('/dev/null')
    inventory.set_variable('all', 'foo', 'bar')
    inventory.add_group('ungrouped')
    inventory.add_group('all')
    inventory.add_group('somegroup')
    inventory.add_child('all', 'somegroup')
    inventory.add_child('somegroup', 'all')
    inventory.add_host(InventoryHost('alpha'))
    inventory.add_host(InventoryHost('beta'))
    inventory.set_variable('beta', 'ansible_ssh_port', 1234)
    inventory.add_group('naughty')
    inventory.add_child('naughty', 'coal')
    inventory.add_host(InventoryHost('gamma'))
    inventory.add_host(InventoryHost('omega'))
    inventory

# Generated at 2022-06-13 12:58:31.780603
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    _in = InventoryModule("hosts")
    _in.parse("./unit/inventories/hosts")
    assert "host_all" in _in.inventory.groups

# Generated at 2022-06-13 12:58:40.445757
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None)
    inventory_parser = InventoryModule(inventory)
    inventory_parser.parse("./test/test_inventory_data.txt")
    assert inventory.groups['all'].hosts == ['testserver1', 'testserver2', 'testserver3']
    assert inventory.hosts['testserver2'].vars['test_var'] == 8888
    assert inventory.groups['test_group1'].vars['test_group_var1'] == 'some_value'
    assert inventory.groups['test_group2'].vars['test_group_var2'] == 'some_other_value'



# Generated at 2022-06-13 12:58:52.341621
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(None, loader=None)
    inventory._loader = DictDataLoader({"/path/to/ini": """
[group_name]
host
host:1234
host ansible_ssh_user=user
[group_name:children]
group_name
[group_name:vars]
foo=bar
"""})
    myinv = InventoryModule(None, "/path/to/ini", loader=None)
    myinv.inventory = inventory
    myinv._parse("/path/to/ini", ["[group_name]", "host1", "host2:1234", "host3 ansible_ssh_user=user", "[group_name:children]", "child1", "[group_name:vars]", "foo=bar"])
    assert len(inventory.groups) == 3
    assert len

# Generated at 2022-06-13 12:58:59.927078
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventoryModule = InventoryModule()
    src = load_data_file(path.join(path.dirname(__file__), '../data/inventory/dynamic_inventory.yml'))
    inventoryModule.parse(Inventory(loader=DictDataLoader({'src': src})), 'src', cache=False)

    assert len(inventoryModule.inventory.get_groups()) == 8
    assert len(inventoryModule.inventory.get_groups_dict()) == 8
    assert 'ungrouped' in inventoryModule.inventory.get_groups()
    assert 'all' in inventoryModule.inventory.get_groups()
    assert 'a' in inventoryModule.inventory.get_groups()
    assert 'b' in inventoryModule.inventory.get_groups()
    assert 'c' in inventoryModule.inventory.get_groups()
    assert 'd' in inventory

# Generated at 2022-06-13 12:59:01.378972
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: write unit test!
    pass

# Generated at 2022-06-13 12:59:02.599102
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

    # FIXME: tests


# Generated at 2022-06-13 12:59:04.130567
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    a = InventoryModule()
    a.parse('tests/inventory', 'bad-definitions.ini')


# Generated at 2022-06-13 12:59:45.983506
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    source = '''[nginx:vars]
nginx_conf_path = /etc/nginx/nginx.conf
nginx_log_path = /var/log/nginx/

[elasticsearch]
server_1
'''
    inventory = InventoryModule.parse(source, cache=False)
    assert len(inventory.groups) == 2
    assert len(inventory.groups['elasticsearch']['hosts']) == 1
    assert len(inventory.groups['nginx']['vars']) == 2
    assert [host.name for host in inventory.groups['elasticsearch']['hosts']] == ['server_1']
    assert inventory.groups['nginx']['vars']['nginx_conf_path'] == '/etc/nginx/nginx.conf'


# Generated at 2022-06-13 12:59:58.374289
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    InventoryModule.parse
    '''

    # parse
    # Test parsing failure on missing file
    inv_module = InventoryModule(
        pattern=None)
    inv_module.clear_pattern_cache()
    inv_module.vars_loader = DataLoader()

    # parse
    # Test parsing failure on missing file
    inv_module = InventoryModule(
        pattern=None)
    inv_module.clear_pattern_cache()
    inv_module.vars_loader = DataLoader()
    inv_module.parse({})
    with pytest.raises(AnsibleParserError):
        inv_module.parse({'path': 'not-existing-file'})

    # parse
    # Test parsing failure with wrong yaml
    inv_module = InventoryModule(
        pattern=None)

# Generated at 2022-06-13 13:00:05.912359
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test 'parse' method:

    inv = InventoryModule(loader=None, variable_manager=None, host_list='/dev/null')


# Generated at 2022-06-13 13:00:09.173466
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = '''
[local]
localhost
'''
    inventory = InventoryModule(data.encode())
    assert inventory.groups['local']



# Generated at 2022-06-13 13:00:09.950017
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: test this!
    pass

# Class FileInventoryModule

# Generated at 2022-06-13 13:00:19.833211
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    class InventoryModule():
        def __init__(self):
        def parse(self, inventory, loader, path, cache=True):
    '''
    # Note: This test is somewhat questionable.  A class is being tested with
    # a static object as its only argument, no actual class instance is being
    # created.  The consequence is that the code is being tested in isolation,
    # untested.  The static object has a method named _raise_error.

    m = InventoryModule()

# Generated at 2022-06-13 13:00:31.200994
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    _loader = DataLoader()

    groups = (
        '[webservers]\n'
        'foo ansible_ssh_host=1.1.1.1\n'
        'bar\n'
        '[dbservers]\n'
    )

    inv = InventoryManager(loader=_loader, sources=groups)

    module = InventoryModule()
    module._inventory = inv
    module._filename = 'test_InventoryModule_parse'
    module.parse('/dev/null', groups)

    assert len(inv.get_groups()) == 2

# Generated at 2022-06-13 13:00:36.706860
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    inventory_module.parse('''
# this is a comment
foo
bar:23
local ansible_connection=local ansible_python_interpreter="/usr/bin/env python"
# comment
baz ansible_ssh_host=192.0.2.1

[ungrouped]
h1 h2 # comment

[group1]
a:b:c:d:e:f
a=b=c=d

[group2:children]
subgroup1 subgroup2

[subgroup1]

[subgroup1:vars]
x=y=z
''')
    assert inventory_module.inventory.get_group('ungrouped').get_host('h1') == Host(name='h1')
    assert inventory_module.inventory.get_group

# Generated at 2022-06-13 13:00:43.935408
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Test for method parse of class InventoryModule
    :return: None
    """
    lines = ['[test_group]', 'test_host ansible_port=9000']
    inv_module = InventoryModule()
    inv_module.parse('/tmp', lines)

    assert 'test_host' in inv_module.inventory.hosts
    assert 'test_group' in inv_module.inventory.groups
    assert 'test_group' in inv_module.inventory.groups['test_group'].child_groups


# Generated at 2022-06-13 13:00:55.758176
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # The inventory module will parse a passed in inventory and return the parsed results.

    # Create an instance of the InventoryModule class, read in the inventory file
    module = InventoryModule()
    with open(os.path.join(TEST_DATA_ROOT_DIR, 'test_inventory_module.ini'), 'r') as f:
        lines = [line.rstrip() for line in f]

    # Call the parse method to populate the groups.
    module._parse('test_inventory_module.ini', lines)

    # See that we have added groups as expected.

# Generated at 2022-06-13 13:01:57.377971
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_args = dict(path='ansible/inventory/my_hosts', cache=False)

    test_inventory = dict(
        host_list=['127.0.0.1'],
        group_list=['group_name'],
        hosts=dict(
            _meta=dict(hostvars=dict()),
            all=dict(
                hosts=dict(
                    host1=dict(ansible_host='127.0.0.1')
                )
            ),
            group_name=dict(
                hosts=dict(
                    host1=dict(ansible_host='127.0.0.1')
                )
            )
        )
    )

    test_ansible_module = TestAnsibleModule()

    # TestException happens
    test_args['path'] = 'wrong_path'


# Generated at 2022-06-13 13:02:07.806109
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    def get_parser(path, data):
        inv_mod = InventoryModule()
        inv_mod._filename = path
        inv_mod._read_data(data)
        return inv_mod
    def check_parse(path, data, expected):
        parser = get_parser(path, data)
        inventory = Inventory(None, None)

        # no defined groups
        parser._populate(inventory)
        assert inventory.groups == expected, "Problem with %s" % path
    # test multiple hosts on the same line, separated by commas; should all go into 'ungrouped' group

# Generated at 2022-06-13 13:02:19.380169
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    module._parse(None, [])
    assert module.groups == dict()

    module = InventoryModule()
    module._parse(None, [
        '[group1]',
        'group1-1.mydomain.tld',
        'group1-2.mydomain.tld user=alice',
        '',
        '[group2]',
        'group2-1.mydomain.tld',
        'group2-2.mydomain.tld user=bob',
        '',
        '[group1:vars]',
        'foo=bar',
        '',
        '[group2:vars]',
        'bar=baz',
    ])

# Generated at 2022-06-13 13:02:31.335114
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create an instance of InventoryModule to call the method
    instance = InventoryModule()

    # Create the path to a file for InventoryModule to open
    path = "path/to/dummy/file"

    # Create the data to be used to initialise the parser
    data = ['[groupname]', 'host1', 'host2']

    # Create an instance of AnsibleInventory to store the groups
    inventory = AnsibleInventory('path/to/config/file')

    # Create a dummy value for the _options member of the InventoryModule instance
    instance._options = data

    # Assign the local variables to the member variables of the InventoryModule instance
    instance._filename = path
    instance.inventory = inventory

    # Call the method under test
    instance._parse(path, data)

    # Assert that the inventory now has the group

# Generated at 2022-06-13 13:02:40.289199
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(Loader())
    module = InventoryModule(inventory=inventory)


# Generated at 2022-06-13 13:02:51.084360
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    im = InventoryModule('any_inventory', 'any_groups')
    im._compile_patterns()

# Generated at 2022-06-13 13:03:01.663422
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # see testcases/inventory/hosts/hosts_file_ignore
    # https://github.com/ansible/ansible/issues/13750
    #if not os.path.exists(filename):
    #    raise AnsibleError("file not found: %s" % filename)
    #InventoryParser = get_plugin_parser(filename)
    #if InventoryParser is None:
    #    raise AnsibleError("unknown inventory type for: %s" % filename)
    #inventory = Inventory(loader=loader)
    #InventoryParser(filename, inventory).parse(filename)
    #print(inventory)
    print('')


# define the class InventoryLoader
# used to load inventory

# Generated at 2022-06-13 13:03:05.516766
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: fix the tests

    #m = InventoryModule()
    #m.parse(None, 'test')
    pass

# Generated at 2022-06-13 13:03:15.376452
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=DictDataLoader({"foo": """
[groupname]
localhost ansible_connection=local
localhost
[badsection]
[badsection:children]
children
[badsection:vars]
vars=1
[goodsection]
[goodsection:vars]
[goodsection:children]
"""}))

    im = InventoryModule(inventory=inventory)
    im.parse_inventory_sources()
    assert im.parse(path='foo') is None


# Generated at 2022-06-13 13:03:22.823182
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  inventory_module = InventoryModule()
  inventory_module.parse(path='../inventory',
                         cache=False,
                         vault_password=None,
                         loader=None,
                         sources=None,
                         vault_ids=None)
  print(inventory_module.inventory)
  groups = inventory_module.inventory.groups
  hosts = inventory_module.inventory.hosts
  print('groups: %s' % groups)
  print('hosts: %s' % hosts)
  for host in hosts:
    print('host %s' % host)
    print('vars %s' % hosts[host].vars)
    for group in hosts[host].get_groups():
      print('group %s' % group)
