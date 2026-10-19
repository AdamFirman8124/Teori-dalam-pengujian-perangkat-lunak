

# Generated at 2022-06-12 20:33:03.739577
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    from datetime import date
    mydate = date.today()

    # Test with yaml format
    context.CLIARGS['yaml'] = True
    result = InventoryCLI.dump(mydate)
    assert result == "!python/object/apply:datetime.date\nargs:\n- %d\n- %d\n- %d\n" % (mydate.year, mydate.month, mydate.day)

    # Test with json format
    context.CLIARGS['yaml'] = False
    result = InventoryCLI.dump(mydate)
    assert result != "!python/object/apply:datetime.date\nargs:\n- %d\n- %d\n- %d\n" % (mydate.year, mydate.month, mydate.day)

# Generated at 2022-06-12 20:33:13.846481
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    data = dict(a=1, b=2)
    assert InventoryCLI.dump(data) == '{"a": 1, "b": 2}'
    data = dict(a=1, b=2)
    assert InventoryCLI.dump(data, yaml=True) == 'a: 1\nb: 2\n'
    data = dict(a=1, b=2)
    assert InventoryCLI.dump(data, toml=True) == 'a = 1\nb = 2\n\n'
    data = dict(a=1, b=2)
    assert InventoryCLI.dump(data, yaml=True) == 'a: 1\nb: 2\n'


# Generated at 2022-06-12 20:33:15.041994
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    t_inventory = InventoryCLI()
    results = t_inventory.toml_inventory()
    assert results == True


# Generated at 2022-06-12 20:33:20.056378
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
 error = 0
 inventory = make_inventory()
 inventory.parse_inventory('./test/unit/ansible_inventory_unittest/json_inventory')
 InventoryCLI.inventory_obj = inventory

 try:
  cli = InventoryCLI(args='')
  # default output
  InventoryCLI.json_inventory(inventory.groups['all'])
 except:
  print("InventoryCLI.json_inventory failed")
  error += 1



# Generated at 2022-06-12 20:33:30.176596
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    import sys
    sys.modules['__main__'].output.__tags__ = []
    sys.modules['__main__'].output.__shown_deprecation_warning = False
    sys.modules['builtins.raw_input']=lambda x: ''
    sys.modules['builtins.input']=lambda x: ''

    print("TESTING post_process_args of class InventoryCLI")

    # Arguments of post_process_args:
    #    self - <ansible.cli.inventory.InventoryCLI object>

    # Testing default value of args
    options = {"list": False, "host": False, "inventory": "./hosts"}
    c = InventoryCLI(args=options)
    c.post_process_args(options)

    # Testing default value of args

# Generated at 2022-06-12 20:33:39.021056
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    inv = InventoryCLI(args=['--list'])
    inv.post_process_args = MagicMock(return_value=inv.options)
    inv.validate_conflicts = MagicMock()
    inv._play_prereqs = MagicMock(return_value=(inv.loader, inv.inventory, inv.vm))
    inv.dump = MagicMock()
    inv.json_inventory = MagicMock(return_value={'one': 1, 'two': 2})
    # case where exit code is 0
    inv.run()
    # case where exit code is 1
    inv.run()

# Generated at 2022-06-12 20:33:51.110191
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():

    class Options:
        pass

    # TODO: finish
    # test_InventoryCLI_run_empty_host()
    # test_InventoryCLI_run_host()
    # test_InventoryCLI_run_graph()
    # test_InventoryCLI_run_list()
    # test_InventoryCLI_run_list_export()
    # test_InventoryCLI_run_list_human_format()
    # test_InventoryCLI_run_list_host()
    # test_InventoryCLI_run_list_host_human_format()
    # test_InventoryCLI_run_list_output()
    # test_InventoryCLI_run_list_output_export()
    # test_InventoryCLI_run_list_output_human_format()
    #

# Generated at 2022-06-12 20:33:58.072107
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    context.CLIARGS = {}
    context.CLIARGS['pattern'] = 'all'
    # initialize class
    inventory_cli = InventoryCLI()
    # mock class inventory
    inventory_cli.inventory = mock.Mock()
    # get_hosts() method return value
    inventory_cli.inventory.get_hosts.return_value = [
        {'name': 'host1'},
        {'name': 'host2'}
    ]
    # get_vars() method return value
    inventory_cli.inventory.groups.get().get_vars.return_value = {'var': 'value'}
    inventory_cli.inventory.groups.get().hosts = ['host1', 'host2']
    # add hosts to group
    top = mock.Mock()

# Generated at 2022-06-12 20:34:06.224312
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    try:
        import pygraphviz
    except ImportError:
        raise SkipTest("pygraphviz is not installed")

    try:
        import ansible.plugins.inventory.yaml
    except ImportError:
        raise SkipTest("ansible.plugins.inventory.yaml is not installed")

    from ansible.cli.arguments import parse_args
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.vault import VaultLib
    from ansible.utils.display import Display


# Generated at 2022-06-12 20:34:15.966111
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():

    d = dict(
        hosts=['host1','host2','host3','host4','host5','host6','host7','host8','host9','host10'],
        vars={'key1': 'value1', 'key2': 'value2'},
        children=['child1','child2','child3','child4','child5','child6','child7','child8','child9','child10']
    )

    # test with json

# Generated at 2022-06-12 20:34:41.450441
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    print("************* Unit test for method post_process_args of class InventoryCLI *************")
    # sample args
    args = ["--list", "all"]
    # create object of class InventoryCLI
    cli = InventoryCLI(args)
    # call method post_process_args of class InventoryCLI
    actual_result = cli.post_process_args(args)
    # assert output
    assert actual_result == ['--list', 'all']



# Generated at 2022-06-12 20:34:53.856275
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    yaml_data = {'192.168.10.11': {'ansible_ssh_host': '127.0.0.1'}, '192.168.10.12': {'ansible_ssh_host': '127.0.0.2'}}
    yaml_output = b'{"192.168.10.11": {"ansible_ssh_host": "127.0.0.1"}, "192.168.10.12": {"ansible_ssh_host": "127.0.0.2"}}\n'
    assert dump(yaml_data) == yaml_output

    json_data = {'a': ['a', 'b'], 'b': 2, 'c': {'d': None}}

# Generated at 2022-06-12 20:35:01.268443
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():

    import sys

    import ansible.constants
    ANSIBLE_HOSTS_FILE_NAME = ansible.constants.DEFAULT_HOST_LIST

    import ansible.plugins.inventory.toml
    HAS_TOML = ansible.plugins.inventory.toml.HAS_TOML


# Generated at 2022-06-12 20:35:09.050354
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    context.CLIARGS = {'pattern': 'all', 'verbosity': 0, 'subset': None, 'refresh_cache': False, 'host': None, 'list': None,
                       'yaml': False, 'graph': True, 'export': False, 'toml': False, 'show_vars': False, 'output_file': None, 'args': []}
    obj = InventoryCLI("ansible-inventory")
    obj.loader, obj.inventory, obj.vm = obj._play_prereqs()
    res = obj.inventory_graph()
    assert type(res) == str


# Generated at 2022-06-12 20:35:18.111053
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    # set up mock objects
    options = tu.setup_inventory_mock(ansible_args=tu.inventory_args)
    options['verbosity'] = 4
    options['graph'] = True
    options['list'] = False
    options['host'] = False
    options['show_vars'] = False
    options['pattern'] = 'all'
    # create object and test method
    inven = InventoryCLI(args=[])
    res = inven.inventory_graph()
    # validate results
    assert res is not None
    assert isinstance(res, str)
    assert res.startswith("@all:")
    assert "--@ungrouped:" in res
    assert "----localhost" in res
    assert "----@test_hosts_group_1:" in res
    assert "------host1" in res


# Generated at 2022-06-12 20:35:28.434784
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    from ansible.plugins.loader import inventory_loader
    from ansible.plugins.inventory.host_list import InventoryModule as host_list
    from ansible.plugins.inventory.simple_group import InventoryModule as simple_group
    from ansible.plugins.inventory.script import InventoryModule as script
    from ansible.plugins.inventory.ini import InventoryModule as ini
    from ansible.plugins.inventory.auto import InventoryModule as auto
    from ansible.plugins.inventory.yaml import InventoryModule as yaml
    from ansible.plugins.inventory.toml import InventoryModule as toml
    loader = DataLoader()
    inventory_loader._get_inventory_plugins().extend([
        host_list,
        simple_group,
        script,
        ini,
        auto,
        yaml,
        toml
    ])
    inventory

# Generated at 2022-06-12 20:35:37.510420
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    # TODO: how to mock ansible options and setup env without breaking existing tests?
    cli = InventoryCLI(args=['--list'])

    # test regular yaml output
    data = {'a': 1, 'b': 'foo', 'c': [1, 2, 3, 4]}
    assert cli.dump(data) == '{a: 1, b: foo, c: [1, 2, 3, 4]}\n'

    # TODO: how to test toml output?
    # test toml output
    cli.parser.set_defaults(toml=True)
    data = {'a': 1, 'b': 'foo', 'c': [1, 2, 3, 4]}

# Generated at 2022-06-12 20:35:48.459424
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    host_vars = {
        'all': {
            'ansible_group_priority': 1
        },
        'ungrouped': {
            'children': ['all'],
            'hosts': {
                'foo': {
                    'var1': 'val1',
                    'var2': 'val2',
                },
                'bar': {
                    'var1': 'val1',
                    'var2': 'val2',
                },
            },
        },
    }

# Generated at 2022-06-12 20:35:56.487523
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    top = DummyGroup()
    top.name = 'all'
    g1 = DummyGroup()
    g1.name = 'g1'
    g2 = DummyGroup()
    g2.name = 'g2'
    h1 = DummyHost()
    h1.name = 'h1'
    h2 = DummyHost()
    h2.name = 'h2'
    top.child_groups.append(g1)
    top.child_groups.append(g2)
    g1.child_groups.append(g2)
    g1.child_groups.append(h1)
    g2.child_groups.append(h2)

# Generated at 2022-06-12 20:35:58.602137
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    assert True


# Unit test runner
if __name__ == '__main__':
    print(__doc__)

# Generated at 2022-06-12 20:36:44.866544
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    dummy_inventory = DummyInventory()
    dummy_inventory.set_variable('group1', 'var1', 1)
    dummy_inventory.set_variable('group2', 'var2', 2)
    dummy_inventory.set_variable('host1', 'var1', 1)
    dummy_inventory.set_variable('host2', 'var2', 2)
    dummy_inventory.add_host('host1')
    dummy_inventory.add_host('host2')
    dummy_inventory.add_group('group1')
    dummy_inventory.add_child('group1', 'group2')
    dummy_inventory.add_parent('group2', 'group1')
    inv = InventoryCLI(dummy_inventory)

# Generated at 2022-06-12 20:36:46.845939
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    pass


# Generated at 2022-06-12 20:36:47.575953
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    pass

# Generated at 2022-06-12 20:36:55.068738
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    my_inv = Inventory()
    h = Host("localhost")
    my_inv.add_host(h)
    h = Host("localhost")
    h.set_variable("foo", "bar")
    my_inv.add_host(h)
    h = Host("localhost")
    h.set_variable("baz", (1, 2, 3))
    my_inv.add_host(h)
    h = Host("localhost")
    h.set_variable("lol", 3)
    my_inv.add_host(h)
    h = Host("localhost")
    h.set_variable("mdr", True)
    my_inv.add_host(h)
    h = Host("localhost")
    h.set_variable("", None)
    my_inv.add_host(h)
    h = Host

# Generated at 2022-06-12 20:36:55.793523
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    pass

# Generated at 2022-06-12 20:37:03.665871
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    inventory = InventoryCLI(parser=Parser(), args=[])
    fake_stuff = {
        'fake_key1': 'fake_value1',
        'fake_key2': 'fake_value2'
    }
    output = inventory.dump(fake_stuff)
    assert output is not None
    parsed_output = json.loads(output)
    assert parsed_output['fake_key1'] == 'fake_value1'
    assert parsed_output['fake_key2'] == 'fake_value2'


# Generated at 2022-06-12 20:37:14.851826
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    example_var = dict()
    example_var['a'] = '1'
    example_var['b'] = '2'

    example_hostinfo = dict()
    example_hostinfo['ansible_group_priority'] = 1
    example_hostinfo['ansible_vars'] = example_var

    example_hostvariables = dict()
    example_hostvariables['host1'] = example_hostinfo

    example_hosts = dict()
    example_hosts['examplehost1'] = example_hostvariables
    example_hosts['examplehost2'] = example_hostvariables

    example_group1 = dict()
    example_group1['children'] = dict()
    example_group1['hosts'] = dict()
    example_group1['vars'] = example_var

    example_group2 = dict()

# Generated at 2022-06-12 20:37:19.632815
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    import pytest
    import sys
    sys.path.insert(0, '/Users/sshedden/Documents/P4/p4ansible/playbooks')
    assert(InventoryCLI.json_inventory(InventoryCLI()) is not None)
    assert(InventoryCLI.json_inventory(InventoryCLI()) is None)

# Generated at 2022-06-12 20:37:21.623852
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    # TODO: write unit test for method inventory_graph of class InventoryCLI
    pass

# Generated at 2022-06-12 20:37:32.702311
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    # set up command line arguments
    args = ['ansible', '-m', 'ping', '-i', 'local', 'server', '-vvvv']
    context.CLIARGS = AnsibleCLI.parse(args)
    context.CLI.base_parser = context.CLI.base_parser()

    # initialize needed objects
    cli = InventoryCLI(args)
    cli.parser = cli.base_parser
    cli.options, cli.args = cli.parser.parse_args(args)
    cli.options = cli.post_process_args(cli.options)

    # initialize needed attributes
    inventory_file = 'local'
    cli.inventory = InventoryManager(inventory_file)
    cli.inventory._subset = None
    cli.vm = VariableManager()



# Generated at 2022-06-12 20:39:32.098754
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    ansible_options_args = dict(connection='local', module_path=None, forks=10, private_key_file=None,
                                ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                                become=True, become_method=None, become_user=None, verbosity=None, check=False,
                                start_at_task=None)
    ansible_options = AnsibleOptions(ansible_options_args)

    parser_args = dict(desc='Ansible inventory script', usage='%(prog)s [options] [host pattern]',
                       epilog='See %(prog)s --version for more details', prog='ansible-inventory')
    parser = CLI.base_parser(parser_args)

# Generated at 2022-06-12 20:39:43.019906
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    import inspect
    class Input:
        pattern = ['all']
        args = None
        list = True
        host = False
        graph = False
        verbosity = 0
        yaml = False
        toml = False
        show_vars = False
        export = True
        output_file = None
    input = Input()
    inventory_cli = InventoryCLI(None, None, None)
    options = inspect.getargspec(inventory_cli.post_process_args)[0]
    data = {}
    for item in options:
        data[item] = getattr(input, item)
    inventory_cli.post_process_args(data)

if __name__ == '__main__':
    test_InventoryCLI_post_process_args()

# Generated at 2022-06-12 20:39:54.375899
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    fake_top = FakeGroup()
    fake_top.name = 'fake_top'
    fake_group_a = FakeGroup()
    fake_group_a.name = 'group_a'
    fake_group_b = FakeGroup()
    fake_group_b.name = 'group_b'
    fake_group_c = FakeGroup()
    fake_group_c.name = 'group_c'
    fake_group_z = FakeGroup()
    fake_group_z.name = 'group_z'
    fake_group_a.child_groups.append(fake_group_b)
    fake_group_a.child_groups.append(fake_group_c)
    fake_top.child_groups.append(fake_group_a)

# Generated at 2022-06-12 20:40:06.865879
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    from ansible.parsing.dataloader import DataLoader
    from ansible.cli.inventory import InventoryCLI
    from ansible.errors import AnsibleError
    from ansible.inventory import Inventory
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    file = "/Users/ksundaram/ansible-inventory/tests/toml_1.toml"

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[file])
    inventory.subset("all")
    hosts = inventory.get_hosts()
    # Instantiate the class, pass in hosts
    inventory_cli = InventoryCLI(hosts=hosts)
    # Set the required value
    inventory_cli.context.CLIARGS['toml'] = True
    inventory_cli.context

# Generated at 2022-06-12 20:40:18.170319
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    print("Test method run of class InventoryCLI")

# Generated at 2022-06-12 20:40:28.619688
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    test_inventory = InventoryCLI()

    class TestGroup:
        name = 'test'

        def __init__(self):
            self.hosts = []
            self.child_groups = []

        def get_hosts(self):
            return self.hosts

        def get_vars(self):
            return {}

    class TestHost(InventoryCLI):
        name = 'test'

        def get_vars(self):
            return {}

    context.CLIARGS = {'export': True}

    test_group = TestGroup()
    test_host = TestHost()
    test_group.hosts.append(test_host)
    test_group.name = 'test'


# Generated at 2022-06-12 20:40:34.947310
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():

    context.CLIARGS = AttributeDict()
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['inventory'] = 'hosts'
    context.CLIARGS['listtasks'] = False
    context.CLIARGS['listtags'] = False
    context.CLIARGS['syntax'] = False
    context.CLIARGS['connection'] = 'local'
    context.CLIARGS['module_path'] = None
    context.CLIARGS['forks'] = 5
    context.CLIARGS['remote_user'] = None
    context.CLIARGS['private_key_file'] = None
    context.CLIARGS['ssh_common_args'] = None
    context.CLIARGS['ssh_extra_args'] = None
    context

# Generated at 2022-06-12 20:40:42.446137
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    o = InventoryCLI()
    o._inventory = InventoryManager()
    o.inventory.clear_pattern_cache()
    o.inventory._vars_plugins = 'set_facts'
    o.inventory._vars_per_group = {
        'all': {
            'ansible_connection': 'network_cli',
            'foo': 'bar'
        },
        'centos': {
            'ansible_connection': 'local'
        }
    }

# Generated at 2022-06-12 20:40:49.209414
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    class args(object):
        basedir = None
        graph = False
        host = None
        list = False
        pattern = 'all'
        output_file = None
        show_vars = False
        toml = True
        verbosity = None
        yaml = False

    class inv_object(object):
        def __init__(self, name):
            self.name = name
            self.hosts = None
            self.child_groups = []

    group_all = inv_object('all')
    group_all.hosts = []
    group_a = inv_object('a')
    group_a.child_groups = [group_all]
    group_b = inv_object('b')
    group_b.child_groups = [group_a]

    # Test output when the inventory is empty
   

# Generated at 2022-06-12 20:40:59.417388
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
  from ansible.plugins.inventory.group import Group
  from ansible.plugins.inventory.host import Host
  from ansible.parsing.yaml.objects import AnsibleUnicode
  host = Host(name="host", port=22, variables={"ansible_ssh_user": AnsibleUnicode("root")})
  group = Group(name="group", variables={"ansible_connection": AnsibleUnicode("ssh")})
  group.hosts.add(host)
  top = Group(name="all")
  top.child_groups.add(group)
  inventory = InventoryCLI()
  inventory.inventory = top