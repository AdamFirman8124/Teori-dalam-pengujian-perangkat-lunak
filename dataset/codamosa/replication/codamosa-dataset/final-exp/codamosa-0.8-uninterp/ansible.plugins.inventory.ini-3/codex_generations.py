

# Generated at 2022-06-13 12:55:12.573213
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    
    # initialize a InventoryModule object
    im = InventoryModule()

    # valid host name
    hostname = 'web01.example.com'
    
    # valid group
    group = 'example_group'

    # invalid group
    invalid_group = 'example:group'

    # invalid hostname
    invalid_hostname = 'web01#example.com'

    # valid host definition
    host_definition = hostname + '=' + 'test'

    # invalid host definition
    invalid_host_definition = hostname + 'test'

    # valid host definition with comment
    host_definition_with_comment = host_definition + ' # comment'

    # valid section
    section = '[' + group + ']'

    # invalid section
    invalid_section = '[' + group + ':vars]'

    # valid section header


# Generated at 2022-06-13 12:55:21.516377
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    hostvars = {}
    inventory = InventoryManager(loader=DataLoader(), sources='')
    inv = InventoryModule()

    # single host
    inventory._options = Options(vars={}, listtags=False, listtasks=False, subset=None, tags=[], verbosity=0)
    inv.parse('host1', inventory)
    assert 'host1' in inventory.get_hosts() and len(inventory.get_hosts()) == 1
    assert inventory.get_host('host1').name == 'host1'
    
    # single host with port
    inventory._options = Options(vars={}, listtags=False, listtasks=False, subset=None, tags=[], verbosity=0)
    inv.parse('host1:1234', inventory)

# Generated at 2022-06-13 12:55:32.526030
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:55:40.515324
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create the module instance to test
    im = InventoryModule()
    im._parse('/dummy/path', ['', '# this is a comment', 'alpha',
                              '[group1:vars]', 'foo=bar', '',
                              '[group2]', 'host1', 'host2:1234', 'host3', 'host4:1234'])

    # Check that the groups are correct
    assert 'ungrouped' in im.inventory.groups
    assert 'group1' in im.inventory.groups
    assert 'group2' in im.inventory.groups
    assert 'alpha' in im.inventory.groups
    assert 'alpha' in im.inventory.get_groups_dict()
    assert 'group1' in im.inventory.get_groups_dict()
    assert 'group2' in im.inventory.get_groups

# Generated at 2022-06-13 12:55:50.928735
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    inv_object = InventoryModule()

    # test the inventory supplied is not empty
    content = """
    [testgroup]
    localhost
    """
    if len(content) == 0:
        assert False

    # test if the inventory supplied is not accessible to the user
    try:
        with open('./test/inv_file/test_inv', 'w') as test_inv:
            test_inv.write(content)
        os.chmod('./test/inv_file/test_inv', 400)
        inv_object.parse('./test/inv_file/test_inv')
        os.chmod('./test/inv_file/test_inv', 600)

        assert False
    except OSError as e:
        assert e.errno == os.errno.EACCES

# Generated at 2022-06-13 12:56:01.862150
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Create an ANSInventory object
    ansinv = ANSInventory(filename='/tmp/testInventory.yml')
    # Create a host inside the ansinv inventory object
    host = ansinv.get_host("test_host")

    # Create a InventoryModule object
    inv_mod = InventoryModule()
    # Create the inventory file
    f = open("/tmp/testInventory.yml", "w+")
    f.write("""[test_group]\n""")
    f.write("""test_host_1 ansible_host=127.0.0.1 ansible_port=22\n""")
    f.close()
    # Populate the inventory object with the content of the inventory file
    inv_mod.parse(ansinv, "/tmp/testInventory.yml")

    # Check if

# Generated at 2022-06-13 12:56:14.663678
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test with path = "./test/test_inventory_module/test_read_inventory_from_file"
    inventory_module = InventoryModule()
    fake_inventory = FakeInventory()
    inventory_module.set_inventory(fake_inventory)
    inventory_module.parse('./test/test_inventory_module/test_read_inventory_from_file')
    assert inventory_module.groups["tomcat"].vars == {'ansible_user': 'tomcat_user'}
    assert inventory_module.groups["tomcat"].hosts["tomcat1"].vars == {'ansible_port': '12314', 'ansible_host': '192.168.10.1'}

# Generated at 2022-06-13 12:56:17.984550
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()
    inv_mod.parse('/dev/null', '[group1]\nfoo\nbar:2345\n')
    assert isinstance(inv_mod.inventory, Inventory)

# Generated at 2022-06-13 12:56:26.084215
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.utils.unicode import to_bytes, to_unicode
    data = """
[ungrouped]
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python

[group1]
alpha:2222
beta
gamma
delta:2222

[group2:children]
group1

[group2:vars]
foo = bar

[ungrouped:vars]
group_var = 1
"""
    inventory = Inventory()
    InventoryModule('/etc/ansible/hosts')._parse('/etc/ansible/hosts', data.split('\n'))

# Generated at 2022-06-13 12:56:35.312535
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()


# Generated at 2022-06-13 12:57:00.259496
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    InventoryModule_parse = InventoryModule({'__file__':'/var/lib/awx/projects/_3__16_08_2017_19_27__3_/project.yml'}).parse()

# Generated at 2022-06-13 12:57:04.507366
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
	inv = InventoryModule()
	inv._parse('/home/ansible/inventory/hosts', ['[groupname]', 'alpha:2345 user=admin # we\'ll tell shlex', 'gamma sudo=True user=root # to ignore comments'])
	for group in inv.groups:
		print(group)
		for host in inv.groups[group].hosts:
			print(host)
			print(inv.groups[group].hosts[host].vars)

if __name__ == '__main__':
	test_InventoryModule_parse()

# Generated at 2022-06-13 12:57:14.667820
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.parsing.dataloader import DataLoader
    data = """
    seattle:
        hosts:
            host1.a.com:
                hostname: "{{ host1.a.com }}"
                port: 1234
                user: admin
                password: "admin"
            host2.a.com:
                hostname: "{{ host2.a.com }}"
                port: 1234
                user: admin
                password: "admin"
    """
    obj = from_yaml(data)

    loader = DataLoader()
    groups = InventoryModule().parse(loader, obj, '/etc/ansible/hosts')

# Generated at 2022-06-13 12:57:24.002785
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print("InventoryModule test: inventory parse")

    # Load inventory from disk
    module = InventoryModule()
    module.parse('test/inventory/hosts')

    # We expect to have 4 groups
    groups = module.get_groups()
    assert len(groups) == 4

    # Group 'ungrouped' should have one host (we know it's a dict object)
    assert isinstance(groups['ungrouped'], dict)
    assert len(groups['ungrouped']) == 1
    assert 'alpha' in groups['ungrouped']

    # Group 'alpha' should have one host (we know it's a dict object)
    assert isinstance(groups['alpha'], dict)
    assert len(groups['alpha']) == 1
    assert 'alpha' in groups['alpha']

    # Group 'beta' should have two hosts (we

# Generated at 2022-06-13 12:57:35.253965
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    filename = 'test_file'

# Generated at 2022-06-13 12:57:46.614194
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create entry for testing inventory plugin
    plugin = InventoryModule('test', os.path.dirname(os.path.abspath(__file__)), 'test')
    # Create the inventory object with plugin instance attached
    i = Inventory(plugin)
    # Run the method to be unit tesed
    plugin._parse('test_path', [u'[all]\n', u'localhost\n', u'[all:vars]\n', u'ansible_connection=local\n'])
    # Check that the inventory was populated with a group and host as expected
    assert i.groups == {'all': Group('all')}
    assert i.hosts == {'localhost': Host('localhost')}
    assert i.hosts['localhost'].groups == [i.groups['all']]
    assert i.groups['all'].host

# Generated at 2022-06-13 12:57:57.102996
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()
    inv_mod._parse('', [
        '[ungrouped]',
        'localhost ansible_connection=local',
        '',
        '[group1]',
        'localhost ansible_ssh_port=15000',
        '',
        '[group2:children]',
        'group1',
        '',
        '[group2:vars]',
        'foo=bar',
        '',
        '[127.0.0.1]',
        '',
        '[group3]',
        '127.0.0.1=127.0.0.1 somevar=someval',
        'localhost'
    ])

    # check the total number of groups
    assert 5 == len(inv_mod.inventory.groups)

    # check the total number of hosts in each group
   

# Generated at 2022-06-13 12:58:01.309413
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory.parse(src="""
    [group1]
    host1 foo=bar baz=faz
    [group1:children]
    group2
    [group2]
    host2
    [group2:vars]
    foo=override
    """, inventory=inventory)
    assert inventory.inventory._groups['group1']._vars == {u'baz': 'faz', u'foo': 'bar'}
    assert inventory.inventory._groups['group2']._vars == {u'foo': 'override'}

# Test method _parse_value of class InventoryModule

# Generated at 2022-06-13 12:58:08.050013
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_mgr = InventoryManager(loader, sources='')

    inv_mgr.parse_sources()


# Generated at 2022-06-13 12:58:14.562262
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Return True if unit test passes, False if fails
    """

# Generated at 2022-06-13 12:58:41.060967
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Setup some fake objects so we can execute parse.
    class FakeFilename(object):
        def __init__(self, filename):
            self._filename = filename

        def __str__(self):
            return self._filename

    class FakeInventory(object):
        def __init__(self):
            self.groups = {}
            self._hosts = {}
            self.vars = {}

        def add_group(self, group):
            if group not in self.groups:
                self.groups[group] = {}

        def add_child(self, parent, child):
            self.groups[child]['parents'] = self.groups[child].get('parents', []) + [parent]

        def add_host(self, host, group):
            if host not in self._hosts:
                self._hosts[host]

# Generated at 2022-06-13 12:58:53.043614
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    if not os.path.exists(INVENTORY_FILE_PATH):
        print('Did not find inventory file at {0}, skipping integration test'.format(INVENTORY_FILE_PATH))
        return

    # inventory file to load
    inventory_file = INVENTORY_FILE_PATH

    # resource to test
    test_resource = InventoryModule()

    # load inventory file
    test_resource.parse(inventory_file, None)
    assert len(test_resource._hosts_cache) == 2
    assert len(test_resource._groups_list) == 1

    # test getting hosts from inventory
    hosts = test_resource.get_hosts()
    assert len(hosts) == 2

    # test getting host variables from inventory

# Generated at 2022-06-13 12:59:06.429763
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class MockModule(object):
        def __init__(self, lines):
            self.lines = lines

        def get_file_contents(self, path):
            return self.lines

    counted = {'groups': 0, 'hosts': 0, 'vars': 0, 'child': 0}

# Generated at 2022-06-13 12:59:09.003584
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # FIXME: This should be converted to use test ansible modules
    return None


# Generated at 2022-06-13 12:59:17.618910
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

# instantiate a InventoryModule object 
    x = ansible.inventory.InventoryModule()

    # default inventory path
    inventory = '/etc/ansible/hosts'

    # parse the inventory file
    x.parse(inventory)

# print total number of hosts from the inventory file
    print('\nTotal number of hosts in the inventory file are: %d \n' % len(x.inventory.list_hosts()))

# print a list of hosts from the inventory file
    print('The following is a list of hosts from the inventory file:')
    for host in x.inventory.list_hosts():
        print(host)


# Generated at 2022-06-13 12:59:18.836514
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  # FIXME
  raise NotImplementedError

# Generated at 2022-06-13 12:59:30.769429
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule.InventoryModule()
    assert inventory._parse_value('"False"') == "False"
    assert inventory._parse_value('"True"') == "True"
    assert inventory._parse_value('"foo"') == "foo"
    assert inventory._parse_value('False') is False
    assert inventory._parse_value('True') is True
    assert inventory._parse_value('"False"') == "False"
    assert inventory._parse_value('"True"') == "True"
    assert inventory._parse_value('"foo"') == "foo"
    assert inventory._parse_value('"foo') == "\"foo"
    assert inventory._parse_value('""') == ""
    assert inventory._parse_value('True ') == "True "

# Generated at 2022-06-13 12:59:41.884965
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = AnsibleInventory()
    parser = InventoryModule(inv)

    parser._parse(b'hosts',
                  [b'#ignore comment',
                   b'\n',
                   b'[group1]',
                   b'default ansible_ssh_host=127.0.0.1 ansible_ssh_user=vagrant ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key',
                   b'\n',
                   b'[group2:children]',
                   b'group1'])

    assert set(inv.groups.keys()) == set(['group1', 'group2'])
    assert inv._vars.get('group1') is None
    assert inv._vars.get('group2') is None

# Generated at 2022-06-13 12:59:55.395411
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:59:57.597770
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    InventoryModule.parse("test")


# Generated at 2022-06-13 13:00:31.857398
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create the inventory object and call its method parse
    inventory = InventoryModule()
    inventory.parse()


if __name__ == '__main__':
    import traceback
    import sys
    import os

    # If no input was given, and assuming the script name is ansible_search_inventory.py,
    # then we will get the input from the current directory,
    # otherwise, we will get the input from the arguments given
    if len(sys.argv) == 1:
        inventory = InventoryModule(os.path.dirname(__file__))
    else:
        inventory = InventoryModule(sys.argv[1])

    # Parse the file or directory given in argument
    # or if no argument was given, the current directory

# Generated at 2022-06-13 13:00:39.411461
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Unit test for method parse of class InventoryModule
    """
    module = InventoryModule()


# Generated at 2022-06-13 13:00:42.655440
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    path = "./"
    data = []

    module.parse(path, data, cache=None)
    assert module.inventory.groups == dict()


# Generated at 2022-06-13 13:00:49.865090
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    parser = InventoryModule()
    parser.parse("/path/to/inventory",
        to_bytes("""
# a comment
[all:vars]
a_var=1
another_var=foo
[webservers]
host1
host2
host3 ansible_ssh_port=2222
[dbservers]
host4
host5:5678
""", errors="surrogate_escape"))

    assert parser._inventory.groups["all"].vars == {'a_var': 1, 'another_var': 'foo'}
    assert parser._inventory.groups["webservers"].hosts == {
        "host1": {},
        "host2": {},
        "host3": {"ansible_ssh_port": 2222, "port": 22},  # port 22 is inherited
    }

# Generated at 2022-06-13 13:00:58.978869
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = '''
    [all]
    a1
    a2
    [test]
    [test:vars]
    [test:children]
    subtest
    [subtest]
    b1
    b2
    '''
    import io
    filename = 'test.ini'
    #with open(filename, 'w') as f:
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(to_bytes(data, errors='surrogate_or_strict'))
    inventory = InventoryManager(loader=MockLoader(path=filename))
    #inventory._subscriptions = set(['all', 'test'])
    inventory.parse_sources([filename])
    #print(inventory.hosts.keys())

# Generated at 2022-06-13 13:01:14.059683
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    This test will test the method parse of the class InventoryModule with correct and incorrect input.
    It will also catch Exceptions that might have been thrown.

    Expected results:
    parse() returns a dict, then it will pass.
    Else, it will fail.

    We expect the following Exceptions to be raised:
    AnsibleParserError: When the content is incorrect, then this will be raised.

    '''
    import yaml

#    FIXME: On windows, there is no way to create a file and read it at the same time.
#    This results in windows not being able to run this test.
#    if not platform.system() == "Windows":

    # Create a tempfile to be used in the test

# Generated at 2022-06-13 13:01:24.092536
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:01:26.176512
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: write unit test
    print("TODO")


# Generated at 2022-06-13 13:01:39.107454
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    text = u"""
    [group1]
    test01 ansible_ssh_host=1.1.1.1 ansible_ssh_user=root ansible_ssh_private_key_file=/home/kevin/keys/id_rsa
    test01 ansible_ssh_host=2.2.2.2 ansible_ssh_user=root ansible_ssh_private_key_file=/home/kevin/keys/id_rsa
    """
    inventory_module.parse(text)

# Generated at 2022-06-13 13:01:51.295848
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os

    # inventory module
    im = InventoryModule()
    im._filename = './test/test_inventory.ini'
    im._basedir = 'test'
    im._initialize()
    im._load()

    # inventory directory
    path = './test/test_inventory.ini'
    assert os.path.exists(path)

    # inventory attributes

# Generated at 2022-06-13 13:02:22.103140
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=None, sources=[])
    inventory.set_playbook_basedir(r'D:\PycharmProjects\ansible\tests')
    inventory_file = InventoryFile(r'D:\PycharmProjects\ansible\tests\inventory', inventory=None, cache=None)
    inventory_mod = InventoryModule(inventory_file, cache=None)
    inventory_mod.parse(r'D:\PycharmProjects\ansible\tests\inventory', lines=None, filename=None)
    print('success')

if __name__ == '__main__':
    test_InventoryFile_load_file_onlyif_missing()

# Generated at 2022-06-13 13:02:32.395729
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    data = prepare_data("data_inventory.yaml")
    inventory.parse("test_inventory.yaml", data)
    assert len(inventory.inventory.groups) == 52
    assert len(inventory.inventory.groups['group1'].hosts) == 0
    assert 'group2' in inventory.inventory.groups
    assert 'group3' in inventory.inventory.groups
    assert 'group4' in inventory.inventory.groups
    assert 'group5' in inventory.inventory.groups
    assert 'group6' in inventory.inventory.groups
    assert len(inventory.inventory.groups['group6'].hosts) == 0
    assert 'group7' in inventory.inventory.groups
    assert 'group8' in inventory.inventory.groups
    assert 'group9' in inventory.inventory.groups

# Generated at 2022-06-13 13:02:40.990142
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

# Generated at 2022-06-13 13:02:47.166930
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Unit tests for method parse of class InventoryModule with YAML formatted files
    """
    filename = 'test_inventory_module.yaml'
    # Create a temporary file
    temp_fd, temp_name = tempfile.mkstemp()
    f = os.fdopen(temp_fd, 'wb')

# Generated at 2022-06-13 13:02:58.604978
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:03:05.876396
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    # basic parsing
    module._parse(None, [
        '[groupname]',
        '[othergroup:vars]',
        'foo',
        'bar'
    ])
    assert module.inventory.groups['groupname'].name == 'groupname'
    assert module.inventory.groups['groupname'].vars == {}
    assert 'foo' in module.inventory.groups['groupname'].hosts
    assert 'bar' in module.inventory.groups['groupname'].hosts
    assert module.inventory.groups['othergroup'].name == 'othergroup'
    assert module.inventory.groups['othergroup'].vars == {}
    assert len(module.inventory.groups['othergroup'].hosts) == 0
    # parsing of hostnames

# Generated at 2022-06-13 13:03:12.674900
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

# Generated at 2022-06-13 13:03:13.847482
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert(InventoryModule._parse('', ['']) == None)


# Generated at 2022-06-13 13:03:20.481718
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method /ansible/inventory/manager.py:InventoryModule.parse
    '''
    path = os.path.join(os.path.dirname(__file__), '../../../examples/hosts')
    #print("--- test_InventoryModule_parse::path= [{}]".format(path)) # DEBUG TEST
    inv = InventoryModule(config_manager=ConfigManager())
    inv.parse(path, [b'localhost ansible_connection=local'])
    assert inv.groups["all"]["vars"]["ansible_connection"] == "local"


# Generated at 2022-06-13 13:03:25.479701
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''
    # path = os.path.join(os.path.dirname(__file__), "..", "..", "ansible", "plugins", "inventory",
    #                     "test_inventory_manager.inventory")
    path = os.path.join(os.path.dirname(__file__), "data", "test_inventory_manager.inventory")
    inventory = InventoryModule.parse(path)

    assert_equal(len(inventory.groups), 6)

    assert_equal(len(inventory.groups['ungrouped']), 4)
    assert_equal(inventory.groups['ungrouped'][0].name, 'alpha')
    assert_equal(inventory.groups['ungrouped'][1].name, 'beta')

# Generated at 2022-06-13 13:04:19.339917
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    invmod = InventoryModule()
    invmod.parse('/tmp/hosts', ['[group0]', 'host1', '[group1:vars]', 'a=1', '[group2:children]', 'group0'])
    assert(invmod.groups == {u'group0': {u'hosts': [u'host1'], u'vars': {}}, u'group1': {u'vars': {u'a': 1}}, u'group2': {u'children': [u'group0']}})
    invmod.parse('/tmp/hosts', ['[group:]', 'host1'])
    assert(invmod.groups == {u'group:': {u'hosts': [u'host1'], u'vars': {}}})


# Generated at 2022-06-13 13:04:32.283156
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    def assert_parse(p, expected, expected_hosts, expected_groups):
        """
        Runs the given parser, checking that the result is as expected.
        """
        p.parse()
        actual = p.inventory.get_hosts()
        assert expected_hosts == actual, "expected hosts don't match actual hosts: %s != %s" % (expected_hosts, actual)
        actual = p.inventory.get_groups()
        assert expected_groups == actual, "expected groups don't match actual groups: %s != %s" % (expected_groups, actual)

    # Test base_dir.
    p = InventoryModule()
    p.basedir = os.path.join(os.getcwd(), 'test/inventory/base_dir')
    assert_parse(p, 1, {}, {})
    p.parse

# Generated at 2022-06-13 13:04:35.899690
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    testInventoryModule = InventoryModule()
    testInventoryModule._parse('/path/to/inventory', ['[foo:bar]', '[baz:vars]', 'alpha'])
    assert testInventoryModule.inventory.groups == {u'foo': {'vars': {}, 'children': u'bar'}, u'baz': {'vars': {}, 'children': {}}}
    assert testInventoryModule.inventory.hosts == {u'alpha': {}}


# Generated at 2022-06-13 13:04:43.724262
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_path = 'test/integration/inventory/hosts' 
    inventory_module = InventoryModule(ansible_inventory=None, loader=None, inventory_filename=inventory_path)
    inventory_module.parse()
    assert inventory_module.inventory.groups['all'].hosts
    assert inventory_module.inventory.groups['all'].vars
    assert inventory_module.inventory.groups['all'].children



# Generated at 2022-06-13 13:04:51.611236
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = '''
    [all]
    192.168.0.1
    test.example.org:2222
    192.168.0.3:2222

    [all:vars]
    ansible_ssh_user=root
    ansible_ssh_pass=rootPassword
    '''

    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(InventoryModule)
    inventory.parse_source('[InventoryModule]', data)
    assert inventory.hosts == ['192.168.0.1', 'test.example.org', '192.168.0.3'], inventory.hosts
    assert inventory.groups == ['all'], inventory.groups