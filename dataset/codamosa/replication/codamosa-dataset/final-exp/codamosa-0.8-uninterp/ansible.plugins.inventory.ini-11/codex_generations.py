

# Generated at 2022-06-13 12:55:09.177653
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    path = 'path'
    lines = ['host1', 'host2', 'host3']
    data = GlobalInventory()
    target = InventoryModule(data)
    target.parse(path, '', lines)
    assert data.get_host('host1') is not None


# Generated at 2022-06-13 12:55:18.014420
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    This test use the real InventoryModule class and check if the `parse` method
    of the class is working fine for different use case.
    """
    inventory = MagicMock()
    inventory_dict = {
        '_groups': {
            'all': {},
        },
    }
    inventory.configure_mock(**inventory_dict)

    inventory_module = InventoryModule()
    inventory_module.inventory = inventory

    # Case 1
    lines = """
            [group1]
            host1.example.com
        """
    inventory_module.lineno = 0
    inventory_module.parse(path='', lines=lines)

    # Case 2
    lines = """
            [group1]
            host1.example.com:12
        """
    inventory_module.lineno = 0
    inventory_

# Generated at 2022-06-13 12:55:24.435618
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule([], {})
    inventory._parse(None, [
        '# A simple test\n',
        '[group1]\n',
        'localhost\n',
        '\n',
        '# A group with variables\n',
        '[group2:vars]\n',
        'foo=bar\n',
        '\n',
        '# A group with children\n',
        '[group3:children]\n',
        'group1\n'
    ])

    assert sorted(inventory.inventory.get_groups()) == ['group1', 'group2', 'group3']

    assert inventory.inventory.list_hosts() == ['localhost']
    assert inventory.inventory.get_variables('localhost') == {}

    assert inventory.inventory.list_hosts('group1') == ['localhost']


# Generated at 2022-06-13 12:55:33.678196
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = mock_inventory()
    inventory_file_path = os.path.join(os.path.dirname(__file__), "./test_inventories/test_inventory_for_InventoryModule_parse")
    #######################
    # Test parse function #
    #######################
    print("Testing parse:")
    # Make sure that we do not get any errors while parsing a correct inventory file
    try:
        InventoryModule(inventory=inventory).parse(inventory_file_path)
        print("Able to parse inventory file.")
    except Exception as e:
        assert False, "Got error \"{}\"".format(e.message)

    # Test parsing an invalid inventory file

# Generated at 2022-06-13 12:55:41.226279
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    generator = make_inventory_generator()
    generator.gen_hosts()

# Generated at 2022-06-13 12:55:51.640507
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    path = '/tmp/test_InventoryModule'
    data = [
        u'localhost ansible_connection=local ansible_python_interpreter="/usr/bin/env python"',
        u'bogus:: localhost',
        u'bogus : 23 localhost',
        u'[ungrouped]\n',
        u'[webservers]\n',
        u'foo\n',
        u'bar\n',
        u'# comment\n',
        u''
    ]

    with open(path, 'w') as f:
        for line in data:
            f.write(line + '\n')
    inv = InventoryModule(path)
    inv.parse()
    assert(inv.inventory.groups['webservers'] is not None)
    #assert(len(inv

# Generated at 2022-06-13 12:56:02.307299
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:56:07.875669
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    obj = InventoryModule("test", "data")
    # FIXME: This should be more robust
    with pytest.raises(AnsibleError) as excinfo:
        obj._parse("test", "data")


# Generated at 2022-06-13 12:56:18.917678
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_source = '''
[webservers]
localhost

[dbservers]
localhost

[dbservers:vars]
db_host=10.0.0.1
db_port=3306

[webservers:vars]
http_port=80

[ungrouped]
localhost

[somegroup:children]
webservers
dbservers
        '''

    # Create a template file object that Ansible can open and read.
    def open_fixture(filename, encoding='utf-8'):
        with open(filename, encoding=encoding) as f:
            return f

    inv_source_filename = './InventoryModule_parse_unittest_inv_source.txt'

# Generated at 2022-06-13 12:56:29.263131
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Ensure that all supported formats are parsed correctly.
    """

    def test_inventory(inv):
        """
        Return the parsed inventory, or fail with a helpful message.
        """

        try:
            return InventoryModule(inv, loader=DictDataLoader()).parse()
        except AnsibleError as e:
            print("Error parsing inventory %s" % inv)
            print("----------------------------------------------")
            print(e.message)
            print("----------------------------------------------")

            raise

    # Generate a simple inventory with a variety of hosts and variables for
    # testing.

# Generated at 2022-06-13 12:56:57.448766
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    For a given an inventory.ini and a 'host', this is our expected
    output.
    """
    host = 'test1'

    groups = ['all:children', 'ungrouped', 'group1', 'group2', 'group2:children', 'group2:vars', 'group3', 'group3:children', 'group3:vars', 'group4', 'group4:children', 'group4:vars']

# Generated at 2022-06-13 12:57:06.937754
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Unit test for method parse of class InventoryModule
    # complex test
    input_filename = 'test/test_complex_inventory.yml'
    input_inventory = InventoryModule(loader=DataLoader(), groups={} )
    input_inventory.parse_inventory(input_filename)
    assert input_inventory.groups['ungrouped'].get_hosts() == [u'foobar.example.com'], 'inventory parse test failed'
    assert input_inventory.groups['foobar'].get_hosts() == [u'foobar.example.com'], 'inventory parse test failed'
    assert input_inventory.groups['foobar'].vars['ntp_server'] == u'ntp.nasa.org', 'inventory parse test failed'

# Generated at 2022-06-13 12:57:16.330734
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # create an instance of the class
    inventoryModule = InventoryModule(None, None, None)
    # try a line variable definition
    result = inventoryModule._parse_variable_definition("var=2")
    assert (result == ('var', 2))
    # try a line invalid variable definition
    raised = False
    try:
        inventoryModule._parse_variable_definition("var 2")
    except AnsibleParserError:
        raised = True
    assert (raised == True)
    # try a line group definition
    result = inventoryModule._parse_group_name("name")
    assert (result == "name")
    # try a line invalid group definition
    raised = False
    try:
        inventoryModule._parse_group_name("nam e")
    except AnsibleParserError:
        raised = True
    assert (raised == True)
    #

# Generated at 2022-06-13 12:57:24.891939
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_data = '''
# This is a comment
[group1]
hosta
hostb:1234
hostc:1234 user=root
hostd:1234 user=admin
[group1:vars]
ansible_ssh_user=test
ansible_ssh_port=1234
[group2]
hoste


# This is a comment
[group2:vars]
name2=value2
name3: value3
[group3]
hosta
hostf
[group3:children]
group2
'''
    lines = inventory_data.split('\n')
    invmod = InventoryModule(None, None)
    invmod._parse('mypath', lines)

# Generated at 2022-06-13 12:57:35.788956
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = Inventory('hosts')
    inventory.parse_inventory(None, os.path.join(os.path.dirname(__file__), 'hosts'))
    assert inventory.groups['web'].vars['variable1'] == 'value1'
    assert inventory.groups['web'].vars['variable2'] == 'value2'
    assert inventory.groups['web'].vars['variable3'] == 'value3'
    assert inventory.groups['web'].vars['variable4'] == 'value4'
    assert inventory.groups['web'].vars['variable5'] == 'value5'
    assert inventory.groups['web'].vars['variable6'] == 'value6'
    # check that a host from a group is also in the group

# Generated at 2022-06-13 12:57:47.023888
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule(None)
    print("Running tests for class InventoryModule")
    # Test with a correct ini file
    inv.parse('tests/ini/correct.ini')
    if inv._filename != "tests/ini/correct.ini":
        print("ERROR: did not correctly parse filename")
    if inv.inventory.groups["children"].name != "children":
        print("ERROR: did not correctly parse group")
    if inv.inventory.groups["children"].vars != {'foo': 'bar'}:
        print("ERROR: did not correctly parse group vars")
    if inv.inventory.groups["parent"].name != "parent":
        print("ERROR: did not correctly parse group")

# Generated at 2022-06-13 12:57:57.335094
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class mock_inventory:
        def __init__(self):
            self.hosts = dict()
            self.groups = dict()

        def add_host(self, hostname):
            if hostname in self.hosts:
                pass
            h = mock_host(hostname)
            self.hosts[hostname] = h
            return h

        def add_group(self, groupname):
            if groupname in self.groups:
                pass
            g = mock_group(groupname)
            self.groups[groupname] = g
            return g

        def set_variable(self, groupname, k, v):
            if groupname in self.groups:
                self.groups[groupname].add_variable(k, v)
            else:
                raise Exception()


# Generated at 2022-06-13 12:58:05.042867
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(loader=DataLoader())
    path_to_yaml_file = os.path.join(os.path.dirname(__file__), '../test/test_hosts.yaml')
    path_to_ini_file = os.path.join(os.path.dirname(__file__), '../test/test_hosts.ini')
    mod = InventoryModule(inventory, path_to_yaml_file)
    mod.parse()
    mod1 = InventoryModule(inventory, path_to_ini_file)
    mod1.parse()


# Generated at 2022-06-13 12:58:20.336544
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager([])
    module = InventoryModule(inventory, [])
    path = './test/files/inventory.ini'
    with open(path) as f:
        # m = hashlib.md5()
        # m.update(bytes(f.read(), encoding="utf-8"))
        # inventory_data = bytes(m.hexdigest(), encoding="utf-8")
        lines = f.readlines()
        lines[1] = lines[1].strip() + " #last\n"
        module._parse(path, lines)

        # assert inventory.hosts.__repr__() == inventory_data

        # test complete inventory

# Generated at 2022-06-13 12:58:29.290100
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.template import Templar

    from units.mock.loader import DictDataLoader

    # TODO: use testinfra's fixture here
    filename = '../../../lib/ansible/inventory/host_list'
    with open(filename, 'r') as f:
        inventory=InventoryModule()
        inventory._filename=filename
        inventory._read_data(f)

# Generated at 2022-06-13 12:58:55.705409
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    path = ''
    filename = ''
    data = []
    obj = Inventory()
    InventoryModule.parse(path, filename, data, obj) # If this is not called in the global scope the command line argument -m is not found


# class of our inventory script

# Generated at 2022-06-13 12:59:04.980596
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    InventoryModule - Parse
    """
    # Import
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    # Init
    filepath = '/etc/ansible/hosts'
    # Init
    cli = CLI(args=[])
    dataloader = DataLoader()
    inventory = InventoryManager(
        loader=dataloader,
        sources=[filepath]
    )
    variable_manager = VariableManager(loader=dataloader, inventory=inventory)
    # Parse
    inm = InventoryModule(cli, filepath, inventory)
    print(inm._parse(filepath, ['127.0.1.1 localhost']))

# Generated at 2022-06-13 12:59:16.209014
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:59:23.614854
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_path = os.path.expanduser("/home/brian/dev/ansible/inventory/hosts")
    inventory = Inventory("localhost")
    inventory.parse(inventory_path, None)
    #inventory.parse_inventory(inventory_path, True)

    print("HOSTS")
    print("-----")
    for hostname in inventory.get_hosts():
        print("HOST: %s" % hostname)
        print("VARS: %s" % inventory.hosts[hostname].vars)
        #for var in inventory.hosts[hostname].get_vars():
        #    print("VAR: %s" % var)

        print("GROUPS")
        print("------")

# Generated at 2022-06-13 12:59:34.307605
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    hostnames = ('alpha', 'beta', 'gamma')
    lines = [
        '[groupA]',
        '; this is a comment',
        'alpha=1234',
        'beta',
        'gamma:2345 sudo=True user=root',
        ''
    ]
    groupname = 'groupA'
    path = '/tmp/test.yml'

    inventory = Inventory('/dev/null')

    inventory.add_group(groupname)
    inventory.set_variable(groupname, 'alpha', 1234)
    inventory.add_host(hostname='alpha', group=groupname, port=None)
    inventory.add_host(hostname='beta', group=groupname, port=None)
    inventory.add_host(hostname='gamma', group=groupname, port=2345)
   

# Generated at 2022-06-13 12:59:44.681024
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #
    # The following are valid lines in an inventory file
    #
    ## Section headers
    i = InventoryModule(filename="")
    #
    # [groupname]
    i._parse(path='', lines=['[groupname]'])
    i._parse(path='', lines=['[groupname:children]'])
    i._parse(path='', lines=['[groupname:vars]'])
    ##
    ## Valid Host definitions
    ##
    ## hostname
    i._parse(path='', lines=['hostname'])
    ## hostname:port
    i._parse(path='', lines=['hostname:1234'])
    ## hostnames separated by commas
    i._parse(path='', lines=['hostname1,hostname2'])

# Generated at 2022-06-13 12:59:57.709632
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Create object
    inventory = InventoryModule()

    # Create some fake variables
    inventory._hosts = dict()
    inventory._patterns = dict()
    inventory._extras = dict()
    inventory._groups = dict()
    inventory._vars = dict()

    # Set some fake variables
    inventory.inventory = dict()
    inventory.inventory['_hosts'] = dict()
    inventory.inventory['_patterns'] = dict()
    inventory.inventory['_extras'] = dict()
    inventory.inventory['_groups'] = dict()
    inventory.inventory['_vars'] = dict()

    # Set some more fake variables
    inventory.groups = dict()
    inventory.groups['a'] = dict()
    inventory.groups['a']['_hosts'] = ['b', 'c']
    inventory.groups['b'] = dict

# Generated at 2022-06-13 13:00:02.476509
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule("foo.ini")
    inv.parse("""
    [groupname]
    [anothergroup:children]
    """, None)
    assert inv.inventory.groups[0].name == "groupname"
    assert inv.inventory.groups[1].name == "anothergroup"


# Generated at 2022-06-13 13:00:09.053052
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule()


# Generated at 2022-06-13 13:00:19.612273
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #Test the InventoryModule with a valid file

    #Create a test file
    fd, filepath = tempfile.mkstemp()
    testfile = open(filepath,'w')
    testfile.write("[testgroup]\n")
    testfile.write("localhost\n")
    testfile.write("127.0.0.1\n")
    testfile.write("[testgroup:vars]\n")
    testfile.write("ansible_connection=local\n")
    testfile.write("ansible_python_interpreter=/usr/bin/python\n")
    testfile.close()

    # parse the test file
    myInventory = InventoryModule()
    myInventory.parse(filepath)

    #check if the 2 hosts were added to the testgroup

# Generated at 2022-06-13 13:01:17.477793
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    f = open(os.path.join(os.path.dirname(__file__), '../test/test_inventory.ini'), 'r')
    test_str = f.read()
    f.close()

    test_str = to_bytes(test_str)
    parser = InventoryModule()
    parser._parse(os.path.join(os.path.dirname(__file__), '../test/test_inventory.ini'),test_str.split(b"\n"))

    print(parser.inventory.hosts.items())
    print(parser.inventory.groups.items())
    print(parser.inventory.get_host('jupiter').get_vars())
    print(parser.inventory.groups.get('ungrouped').get_vars())

# Generated at 2022-06-13 13:01:26.992478
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:01:33.000324
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    mod = InventoryModule()
    content = """

[meh]
# Test comment
meh:9000
[foobar]
seven=8 nine=10
one = 1 # other comment
two = 2

[junk:children]
# child comment
foo
bar
[toread:vars]
# I do nothing
"""
    content = to_text(content)
    mod._parse("/etc/ansible/hosts", content.split("\n"))

    inv = mod.get_inventory()
    # Test group parsing
    assert "meh" in inv.groups
    assert len(inv.groups) == 4

    # Test host parsing
    assert "meh" in inv.hosts
    assert len(inv.hosts) == 1

    # Test variable setting
    assert "foo" in inv.groups


# Generated at 2022-06-13 13:01:37.736195
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_mod = InventoryModule(Inventory())
    inv_mod.parse('/etc/ansible/hosts', '''
[ungrouped]
localhost
    '''.strip())

    assert 'ungrouped' in inv_mod.inventory.groups
    assert 'localhost' in inv_mod.inventory.hosts
    assert 'localhost' in inv_mod.inventory.groups['ungrouped'].hosts


# Generated at 2022-06-13 13:01:51.838617
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    global ansible_parser_config
    global yaml_inventory_conf
    global yaml_example_1
    global yaml_example_2
    global yaml_example_3
    global yaml_example_4
    global yaml_example_5
    global yaml_example_6
    global yaml_example_7
    global yaml_example_8
    global yaml_example_9
    global yaml_example_10
    global yaml_example_11
    global yaml_example_12
    global yaml_example_13
    global yaml_example_14
    global yaml_example_15

    ansible_parser_config = AnsibleParserConfig()
    ansible_parser_config.set_default_data(dict())


# Generated at 2022-06-13 13:02:03.351328
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # a group definition
    group_txt = "[group1]\n"
    # a variable definition
    group_txt += "[group1:vars]\n"
    group_txt += "test_var=test_value\n"
    # a group definition
    group_txt += "[group2]\n"
    # a variable definition
    group_txt += "[group2:vars]\n"
    group_txt += "test_var=test_value\n"
    # a host definition
    group_txt += "localhost ansible_connection=local test_var=test_value\n"
    for path in ['/dev/null', '/tmp/ansible_test_file', '/tmp/ansible/test_file']:
        # create an empty file for testing
        open(path, 'w').close()
       

# Generated at 2022-06-13 13:02:11.475930
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = MagicMock()
    inventory.groups = {}
    inventory.add_group = MagicMock()
    inventory.set_variable = MagicMock()
    inventory.add_child = MagicMock()

    module = InventoryModule(inventory)
    module._parse_host_definition = MagicMock()
    module._parse_value = MagicMock()
    module._expand_hostpattern = MagicMock(return_value=(['line1'], '2345'))
    module._parse_group_name = MagicMock()
    module._add_pending_children = MagicMock()
    module._parse_variable_definition = MagicMock(return_value=('groupname', 'vars'))

    module._groups = {}
    module._COMMENT_MARKERS = ''


# Generated at 2022-06-13 13:02:16.271978
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    path = '~/ansible/inventory/hosts'
    try:
        module.parse(path)
    except Exception as e:
        if type(e) == AnsibleParserError:
            assert 1 == 0
        else:
            raise e

# Generated at 2022-06-13 13:02:27.752315
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager(Loader())
    i = InventoryModule()
    i.inventory = inventory
    i._parse("",
        [
            "[blah]",
            "blah",
        ])
    assert inventory.get_host("blah").vars == dict()
    assert inventory.get_host("blah").get_variables() == dict()
    assert inventory.get_host("blah").get_group_vars() == dict()
    assert inventory.get_host("blah").get_group_variables() == dict()

    i = InventoryModule()
    i.inventory = inventory
    i._parse("",
        [
            "[UnitTestGroupName]",
            "UnitTestHostName",
        ])
    assert inventory.get_host("UnitTestHostName") is not None

# Generated at 2022-06-13 13:02:29.338099
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = InventoryModule().parse('test')
    assert data


# Generated at 2022-06-13 13:04:06.273765
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_path = "../../../../../ansible/inventory/lineinfile.py"
    inventory_filename = "lineinfile.py"
    inventory_module = InventoryModule(inventory_filename, inventory_module_cache)

    inventory_module.parse(inventory_path)

    # Uncomment to see results
    # print(inventory_module.inventory.get_groups_dict())
    # print(inventory_module.inventory.get_groups_dict()['ungrouped']['vars'])
    # print(inventory_module.inventory.get_groups_dict()['ungrouped']['hosts'])
    # print(inventory_module.inventory.get_hosts_dict())
    # print(inventory_module.inventory.get_hosts_dict()['localhost']['vars'])


# Generated at 2022-06-13 13:04:16.594860
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryManager('localhost,')
    inventory.parse_inventory(path=os.path.join(os.path.dirname(__file__), 'data', 'inventory', 'complex_hosts'))

    # test parsing the file
    assert len(inventory.get_hosts('all')) == 4

    # test parsing the file and a subset
    assert len(inventory.get_hosts('nested')) == 4

    # test parsing the file and a subset
    assert len(inventory.get_hosts('nested:nested1')) == 2

    # test parsing the file and a subset
    assert len(inventory.get_hosts('nested:nested1:nested2:nested3')) == 1

    # test parsing the file and a subset

# Generated at 2022-06-13 13:04:30.152411
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    os.environ['ANSIBLE_INVENTORY_UNPARSED_FAILED'] = '0'
    inv = InventoryModule('')
    inv.inventory = Inventory()
    inv.directory = './testdata'
    inv.parse()

    assert inv.inventory.get_groups() == ['ungrouped', 'group1', 'group2']
    assert inv.inventory.groups['group1'].name == 'group1'
    assert inv.inventory.groups['group1'].hosts[0].name == 'host1'
    assert inv.inventory.groups['group1'].hosts[0].port == 1234
    assert inv.inventory.groups['group1'].hosts[0].variables == {'var1': '1', 'var2': '2'}

# Generated at 2022-06-13 13:04:35.954784
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # create a temp file for testing
    test_file = tempfile.mktemp()
    with open(test_file, mode="w") as f:
       f.write('[test]\n')
       f.write('localhost [1.1.1.1]\n')
       f.write('localhost [1.1.1.2]\n')
       f.write('localhost:22 ansible_port=22\n')
       f.write('localhost:2222 ansible_port=2222\n')
       f.write('localhost ansible_port=22 [1.1.1.3]\n')
       f.write('localhost ansible_port=2222 [1.1.1.4]\n')

# Generated at 2022-06-13 13:04:50.757834
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()

# Generated at 2022-06-13 13:05:00.911772
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule()
    i._parse(os.path.dirname(__file__) + '/test.inventory', i._read_file(os.path.dirname(__file__) + '/test.inventory'))
    assert i.inventory.groups['all'] == ansible.inventory.Group('all')
    assert len(i.inventory.groups['all'].hosts) == 4
    assert i.inventory.groups['webservers'] == ansible.inventory.Group('webservers')
    assert len(i.inventory.groups['webservers'].hosts) == 1
    assert i.inventory.groups['webservers'].hosts['alpha'] == ansible.inventory.Host('alpha')
    assert i.inventory.groups['webservers'].hosts['alpha'].port == 22