

# Generated at 2022-06-12 20:33:21.921813
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    # make a fake 'self'
    self = types.SimpleNamespace()
    self.options = {'list': True}
    self.loader = None
    self.inventory = None
    self.vm = None

    # make a fake 'top'
    top_d = {
        'all': {
            'children': ['ungrouped'],
            'hosts': {},
            'vars': {},
        },
        'ungrouped': {
            'children': [],
            'hosts': {
                'localhost': {},
            },
            'vars': {}
        }
    }
    top = types.SimpleNamespace()
    top.child_group = [types.SimpleNamespace(name=k) for k in top_d]

# Generated at 2022-06-12 20:33:26.092281
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    cli = InventoryCLI(args=['--version'])
    results = cli._remove_internal({'foo': 'bar', 'redis_port': 6379})
    assert results == {'foo': 'bar'}

# Generated at 2022-06-12 20:33:27.424758
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    print(InventoryCLI.json_inventory())


# Generated at 2022-06-12 20:33:37.682172
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
  """
  Group ungrouped host in `[all,ungrouped]`, not `[all]`
  See https://github.com/ansible/ansible-modules-core/issues/6690
  """
  parent_group = Group(name='all')
  ungrouped_group = Group(name='ungrouped')
  host = Host(name='h1')
  ungrouped_group.add_host(host)
  parent_group.add_child_group(ungrouped_group)
  assert InventoryCLI.toml_inventory(InventoryCLI, top=parent_group) == {'all': {'children': ['ungrouped'], 'hosts': {}}}



# Generated at 2022-06-12 20:33:45.422103
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    import StringIO
    import json
    json_str = '{"all" : { "hosts" : ["host1","host2"], "children" : ["host1_children","host2_children"], "vars" : { "var1" : 1, "var2" : "2" } } }'
    expected = json.loads(json_str)
    context.CLIARGS = {'export': True}
    top = Group('all')
    top.set_variable('var1', 1)
    top.set_variable('var2', '2')
    host1 = Host('host1')
    host1_children = Group('host1_children')
    host2 = Host('host2')
    host2_children = Group('host2_children')
    top.add_child_group(host1_children)
   

# Generated at 2022-06-12 20:33:47.545829
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
  inventory_cli = InventoryCLI()
  inventory_cli.post_process_args({'list': True, 'verbosity': 0})


# Generated at 2022-06-12 20:33:48.213035
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    pass

# Generated at 2022-06-12 20:33:53.879183
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    import unittest
    import base64
    import textwrap
    from ansible.cli.inventory import InventoryCLI
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.inventory.yaml import InventoryYaml
    from io import StringIO
    from ansible.plugins.loader import inventory_loader

    testInventory = textwrap.dedent("""
    all:
     hosts:
      test1:
       vars:
        var1: value
    """)
    inv_yaml = InventoryYaml(StringIO(testInventory))
    inv_yaml.parse()
    inv = inv_yaml.inventory

# Generated at 2022-06-12 20:34:02.807475
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    from ansible.cli.inventory import InventoryCLI
    inv_cli = InventoryCLI()
    all_group = mock.MagicMock()
    all_group.name = 'all'
    all_group.child_groups = ['child_of_all']
    all_group.hosts = ['host_of_all']

    def get_vars(group):
        if group == 'all':
            return {'group_vars_from_all': 'yes'}
        elif group == 'child_of_all':
            return {'group_vars_from_child_of_all': 'yes'}

    def get_hosts(host_pattern):
        if host_pattern == 'all':
            return [host_of_all]
        else:
            return [host_of_all2]


# Generated at 2022-06-12 20:34:11.611196
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    # Dummy data
    def get_connection(self):
        connection=namedtuple('connection', ['transport'])
        connection.transport='local'
        return connection
    class Options(object):
        connection=get_connection

    Options.ask_vault_pass=True
    Options.ask_pass=True
    Options.ask_su_pass=True
    Options.ask_sudo_pass=True
    Options.ask_become_pass=True
    Options.ask_become_method=True
    Options.ask_become_flags=True
    Options.ask_pass=True
    Options.private_key_file=True
    Options.become_ask_pass=True
    Options.become_method=True
    Options.become_user=True
    Options.become=True

# Generated at 2022-06-12 20:34:41.291827
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    results = InventoryCLI.dump({u"ansible_all_ipv4_addresses": [u"172.16.241.129", u"192.168.95.128"]})
    assert u"{\n    \"ansible_all_ipv4_addresses\": [\n        \"172.16.241.129\", \n        \"192.168.95.128\"\n    ]\n}" in results, "returned string:\n{}".format(results)

    results = InventoryCLI.dump({u"ansible_all_ipv4_addresses": [u"192.168.95.128"]})

# Generated at 2022-06-12 20:34:42.818569
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    cli = InventoryCLI([])
    cli.parse()
    assert cli.json_inventory is not None

# Generated at 2022-06-12 20:34:54.989193
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    cli = InventoryCLI()
    class inventory_object:

        # used after creating the object
        def __init__(self):
            self.name = 'group_name'
            self.child_groups = []
            self.hosts = []

    import copy
    test_top = inventory_object()
    test_top.name = 'all'
    test_top.child_groups = [copy.copy(inventory_object()) for x in range(10)]
    test_top.hosts = [copy.copy(inventory_object()) for x in range(20)]
    assert cli.yaml_inventory(test_top)
    test_top = inventory_object()
    test_top.name = 'all'
    test_top.child_groups = []
    test_top.hosts = []

# Generated at 2022-06-12 20:35:00.734517
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    base_dir = os.path.dirname(__file__)
    inventory_file = os.path.join(base_dir, 'data/hosts/hosts/insecure_hosts')
    inventory = InventoryCLI._inventory_loader(inventory_file)
    # Initialize needed objects
    loader, inventory, vm = InventoryCLI._play_prereqs(inventory=inventory)
    results = InventoryCLI.json_inventory(inventory.groups.get('all'))

# Generated at 2022-06-12 20:35:10.632453
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    """ Test the method InventoryCLI.inventory_graph of the class InventoryCLI """
    pattern = context.CLIARGS['pattern']
    context.CLIARGS['pattern'] = "group1"
    context.CLIARGS['graph'] = True
    src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    config_path = os.path.join(src_dir, 'ansible.cfg')
    context.CLIARGS['config'] = config_path
    inventory = InventoryCLI(args=[])
    loader, inventory, vm = inventory._play_prereqs()
    group = inventory.groups.get("group1")
    start_at = group

# Generated at 2022-06-12 20:35:19.420466
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    class Group(object):
        def __init__(self, name, hostnames):
            self.child_groups = []
            self.name = name
            self.hosts = [Host(hostname) for hostname in hostnames]
            self.vars = {name: name}

    class Host(object):
        def __init__(self, name):
            self.name = name

    top = Group("all", ["localhost"])
    hosts = ["localhost", "example"]

    g1 = Group('g1', hosts)
    g2 = Group('g2', hosts)
    g11 = Group('g1-1', hosts)
    g12 = Group('g1-2', hosts)
    g111 = Group('g1-1-1', hosts)
    g112 = Group('g1-1-2', hosts)

# Generated at 2022-06-12 20:35:26.958958
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    # Initialize ansible.cli.inventory.InventoryCLI
    inventory_cli = InventoryCLI()
    inventory_cli._graph_name('test_graph_name', depth=0)
    # Initialize ansible.cli.inventory.InventoryCLI
    inventory_cli = InventoryCLI()
    inventory_cli._graph_group(group=None, depth=0)
    # Initialize ansible.cli.inventory.InventoryCLI
    inventory_cli = InventoryCLI()
    inventory_cli.inventory_graph()


# Generated at 2022-06-12 20:35:36.210319
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    # Initialize test
    current_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_path = os.path.join(current_dir, '../data/inventory/toml')
    test_data_path = os.path.abspath(test_data_path)

    parser = CLI.base_parser(
        constants.DEFAULT_MODULE_PATH,
        constants.DEFAULT_MODULE_NAME,
        constants.DEFAULT_MODULE_ARGS,
        'inventory_plugins'
    )

    inventory_cli = InventoryCLI(parser)

    inventory_cli.subparser = parser.subcommands.choices['inventory']

# Generated at 2022-06-12 20:35:46.362621
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    # FIXME: argparse '--extra-vars' support is broken on Windows
    is_windows = (platform.system() in ('Windows', 'Microsoft', 'microsoft'))
    if is_windows:
        pytest.skip("argparse '--extra-vars' support is broken on Windows")
    # TODO: options for this test
    # TODO: need to expand test with more options
    # TODO: test output as well
    icli = InventoryCLI()
    icli.setup()
    icli.parser.parse_args(['--list', '--host', 'test_host.example.com'])
    icli.post_process_args(context.CLIARGS)
    icli.run()


# Generated at 2022-06-12 20:35:55.439945
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    """Test the InventoryCLI.json_inventory() method."""

# Generated at 2022-06-12 20:36:18.139922
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    inventory_file = os.path.join(inventory_dir, 'hosts')
    inventory = Inventory(loader=loader, host_list=inventory_file)
    inventory.subset('all')
    group = inventory.groups.get('all')
    top = group
    cli = InventoryCLI()
    cli.json_inventory(top)

# Generated at 2022-06-12 20:36:24.692207
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    class MockInventory(object):
        def __init__(self):
            self.groups = [
                MockGroup(
                    'group1',
                    [
                        MockHost('web1'),
                        MockHost('web2')
                    ],
                    [
                        MockGroup('group1_sub1'),
                        MockGroup('group1_sub2')
                    ]),
                MockGroup(
                    'group2',
                    [
                        MockHost('web3')
                    ],
                    [
                        MockGroup('group2_sub1'),
                        MockGroup('group2_sub2')
                    ]
                ),
                MockGroup(
                    'group3',
                    [],
                    [
                        MockGroup('group3_sub1'),
                        MockGroup('group3_sub2')
                    ]
                )
            ]


# Generated at 2022-06-12 20:36:35.566974
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    test_cli = InventoryCLI(args=[])
    test_cli.options.pattern = 'all'
    test_cli.options.verbosity = 0
    test_cli.options.yaml = False
    test_cli.options.toml = False
    test_loader = DataLoader()
    test_inventory = InventoryManager(loader=test_loader, sources='localhost,')
    test_inventory._options = test_cli.options
    test_inventory.groups = {}
    test_group1 = test_inventory.groups.get('all')

# Generated at 2022-06-12 20:36:43.378421
# Unit test for method toml_inventory of class InventoryCLI

# Generated at 2022-06-12 20:36:50.445956
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    inventory_cli = InventoryCLI()
    group_dic = {
        "hosts": ['host1', 'host2', 'host3'],
        "children": [],
        "vars": {
            "group_var": "group var value"
        },
        "name": "all",
    }
    group = HostGroup(**group_dic)
    print(group)
    print(group.get_vars())
    toml_inventory_result = inventory_cli.toml_inventory(group)
    print(json.dumps(toml_inventory_result, sort_keys=True, indent=4))

# Generated at 2022-06-12 20:37:01.805429
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    # Test a simple situation where the host has a single non-string value for a var
    test_vars = {}
    test_vars['my_var'] = 123
    # Test a simple situation where the host has a single string value for a var
    test_vars['my_var2'] = '123'
    # Test a simple situation where the host has a dictionary value for a var
    test_vars['my_var3'] = {'key': 'value'}
    test_vars2 = {'my_var': 123}
    test_vars3 = {'my_var': '123'}
    test_vars4 = {'my_var': {'key': 'value'}}
    # Test a complex situation

# Generated at 2022-06-12 20:37:14.046077
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    json_data = {'key1': 'value1', 'key2': 'value2'}
    yaml_data = 'key1: value1\nkey2: value2\n'
    toml_data = toml_dumps(json_data)

    try:
        import yaml
    except ImportError:
        mark_skip('python-yaml library not found, skipping test_InventoryCLI_dump')

    if not HAS_TOML:
        mark_skip('The python "toml" library is required, skipping test_InventoryCLI_dump')

    icli = InventoryCLI()

    for test_data, test_format in ((json_data, 'json'), (yaml_data, 'yml'), (toml_data, 'toml')):
        display.verbosity = 3

# Generated at 2022-06-12 20:37:24.715287
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    # Test toml_inventory with normal data
    inventory_data = dict(hosts=['host1', 'host2'], vars={'var1': 'val1', 'var2': 'val2'}, children=['child'])
    expected_result = dict(all=dict(hosts=dict(host1={}, host2={}), vars=dict(var1='val1', var2='val2'), children=['child']))
    top = call_mock(name='all', child_groups=[call_mock(name='child')], hosts=[call_mock(name='host1'), call_mock(name='host2')], vars=inventory_data.get('vars'))
    cli = InventoryCLI([])
    cli.toml_inventory = Mock(return_value=inventory_data)


# Generated at 2022-06-12 20:37:35.414907
# Unit test for method dump of class InventoryCLI

# Generated at 2022-06-12 20:37:41.914685
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    # Test for dump(stuff)
    yaml_stuff = ['first_line', 'second_line', {'key1': 'val1', 'key2': 'val2'}]
    assert InventoryCLI.dump(yaml_stuff) == '- first_line\n- second_line\n- key1: val1\n  key2: val2\n'

    json_stuff = {'key1': 'val1', 'key2': 'val2'}
    assert InventoryCLI.dump(json_stuff) == '{\n    "key1": "val1",\n    "key2": "val2"\n}'

    toml_stuff = {'key1': 'val1', 'key2': 'val2'}

# Generated at 2022-06-12 20:38:43.613470
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    obj = InventoryCLI(module)
    obj.run()

# Generated at 2022-06-12 20:38:54.171001
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    # Copy of class InventoryCLI from inventory/cli.py
    class InventoryCLI(object):
        pass
    
    # Create instance of class InventoryCLI
    inventory_cli = InventoryCLI()
    # Create a mock object for the class Display
    display_mock = mock.Mock()
    # Add the mock object to the instance of InventoryCLI
    inventory_cli.display = display_mock
    # Create a mock object for the method _play_prereqs of InventoryCLI
    inventory_cli._play_prereqs_mock = mock.Mock()
    # Add the mock object to the instance of InventoryCLI
    inventory_cli._play_prereqs = inventory_cli._play_prereqs_mock
    # Create a mock object for the method dump of InventoryCLI
    inventory_cli.dump = mock

# Generated at 2022-06-12 20:39:03.793524
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    import os
    import sys
    import test.utils as utils

    inventory_file = os.path.join(utils.get_data_path(), 'inventory', 'inventory_file')
    inventory_directory = os.path.join(utils.get_data_path(), 'inventory', 'inventory_directory')
    plugin_directory = os.path.join(utils.get_data_path(), 'inventory', 'empty_directory')

    # create the cli parser object
    c = InventoryCLI([inventory_file, inventory_directory])
    c.parser.add_argument('--list', action='store_true', default=True, dest='list', help='List active servers')
    c.parser.add_argument('--host', action='store', default=None, dest='host', help='Get all the variables about a specific host')
    c.parser

# Generated at 2022-06-12 20:39:09.545518
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    '''
    Unit test for method json_inventory of class InventoryCLI
    '''

    # Setup test object
    inventory_src = '''
    [all]
    fiosrvr2
    fiosrvr1
    nas-1

    [group1]
    fiosrvr2
    fiosrvr1

    [group2]
    fiosrvr1

    [group3]
    fiosrvr2
    '''
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[inventory_src])
    class_ = InventoryCLI(loader=loader, inventory=inventory)

    # Setup args
    top = inventory.groups.get('all')
    args = dict()

    # Exercise the method
    result = class_.json_inventory(top)

    # Assert results
   

# Generated at 2022-06-12 20:39:13.349205
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    """
    Create a  instance of class InventoryCLI
    Testing method dump
    """
    inventory = InventoryCLI()
    display = Display()
    data = {"num": 1, "str": "a"}
    results = inventory.dump(data)
    eq_(results, '{"num": 1, "str": "a"}\n', "Test failed")


# Generated at 2022-06-12 20:39:18.490952
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    inventory_cli = InventoryCLI(args=['ansible-inventory','--graph'])
    assert inventory_cli.inventory_graph() == 'all:\n  |--@all:\n  |  |--@ungrouped:\n  |  |--@ungrouped:\n  |  |--@ungrouped:\n  |  |--@ungrouped:\n  |  |--@ungrouped:\n  |--@all:'


# Generated at 2022-06-12 20:39:25.438939
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    gr = Groups()
    gr.add_group('test_group')
    cli = InventoryCLI([], None)
    assert cli.yaml_inventory(gr) == {'test_group': {'hosts': {}, 'children': {}}}


# Generated at 2022-06-12 20:39:33.118294
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    temp_args = {
        "host": False,
        "pattern": "all",
        "list": False
    }
    temp_cliargs = {
        "host": "host",
        "pattern": "pattern",
        "list": "list"
    }
    temp_context = {
        "CLIARGS": temp_cliargs
    }

    with patch.object(InventoryCLI, "_get_group") as mock_get_group:
        mock_get_group.return_value.name = "all"
        mock_get_group.return_value.child_groups = []
        ICI = InventoryCLI(temp_args, context=temp_context)
        result = ICI.json_inventory(mock_get_group.return_value)

    assert result == {'all': {}}



# Generated at 2022-06-12 20:39:42.606303
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    collection = MagicMock()
    cli = InventoryCLI(
        args=['--list', '--toml'],
        collection=collection)
    collection.get_command.return_value = cli
    collection.create.return_value = cli

    cli.run()

    collection.get_command.assert_called_once_with('inventory', 'list')
    collection.create.assert_called_once_with()
    cli.parser.parse_args.assert_called_once_with(['--list', '--toml'])
    cli.post_process_args.assert_called_once_with(cli.parser.parse_args.return_value)

# Generated at 2022-06-12 20:39:53.986530
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    run_setup(None)
    # test performing the method
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    inv_data = """
        [all:vars]
        foo=bar
        [group1]
        host1
        [group2]
        host2 ansible_host=host2.example.com
        [group2:vars]
        baz=quux
        """
    inv_source = InventoryManager(loader=loader, sources=inv_data).get_inventory()
    var_manager = VariableManager(loader=loader, inventory=inv_source)
    all_group = inv_source.get_group('all')
    results = InventoryCLI.yaml

# Generated at 2022-06-12 20:42:04.164125
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    # FIXME (after release)
    # this test is fragile, since it doesn't mock external components
    # but at least it runs and fails when there is a regression
    from ansible.plugins.loader import become_loader

    become_loader.get('auto').become = mock.Mock(autospec=True, return_value=None)

    inventory = {
        'hosts': {'myhost': {'ansible_host': 'ip.ip.ip.ip'}},
        'groups': {'mygroup': {'hosts': ['myhost']}},
    }
    # FIXME (after release)
    # this method is fragile because it depends on an external plugin
    path = 'ansible.plugins.inventory.yaml'
    target = 'YamlInventory'
    source = path + '.' + target
   

# Generated at 2022-06-12 20:42:05.873975
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    inventory_cli = InventoryCLI()
    inventory_cli.run()

# Generated at 2022-06-12 20:42:14.461078
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    print('In test_InventoryCLI_post_process_args')
    post_process_args_params = {'list': False, 'host': 'host', 'graph': False, 'pattern': 'all', 'verbosity': 0, 'version': False}
    #data = {'output_file': None, 'subset': None, 'playbook': '', 'syntax': False, 'vault_password_files': '', 'sudo': None, 'sudo_user': 'root', 'ask_pass': False, 'private_key_file': '', 'remote_user': '', 'remote_port': None, 'ssh_common_args': '', 'ssh_extra_args': '', 'sftp_extra_args': '', 'scp_extra_args': '', 'become': None, 'become_method': '', '

# Generated at 2022-06-12 20:42:20.054223
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():

    inventory_path = "test/unit/ansible_test/_data/inventory/multi_group_toml/inventory.toml"

    cli_inven = InventoryCLI.init_parser()
    cli_inven.options = cli_inven.parser.parse_args([])
    cli_inven.options.toml = True
    try:
        cli_inven.parse([inventory_path])
    except SystemExit:
        pass

    inv = cli_inven.inventory
    test_result = cli_inven.toml_inventory(inv.groups["all"])
    correct_toml = toml.load("test/unit/ansible_test/_data/inventory/multi_group_toml/inventory.toml")

    assert test_result == correct_toml