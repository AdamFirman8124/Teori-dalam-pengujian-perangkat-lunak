

# Generated at 2022-06-12 20:33:06.625324
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    import os
    test_directory = os.path.dirname(os.path.realpath(__file__))
    inv_file = os.path.join(test_directory,".inventory")

    loader = DataLoader()

    extra_args = ['--inventory', inv_file,'--list']
    cli_args = parse_args(extra_args, None)
    inventoryCLI = InventoryCLI(loader, cli_args)
    top = inventoryCLI._get_group('all')
    results1=inventoryCLI.json_inventory(top)

# Generated at 2022-06-12 20:33:13.567405
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    # ansible-inventory -h
    cli = InventoryCLI([])
    cli.parser.parse_args = mock.MagicMock(return_value=mock.DEFAULT)
    display = mock.MagicMock()
    cli.run()
    display.verbosity = None
    display.display.assert_called_once_with('usage: ansible-inventory [-h]')


# Generated at 2022-06-12 20:33:19.022675
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    cli = InventoryCLI()
    top = cli._get_group('all')
    top.child_groups = []
    top.hosts = []
    result = cli.toml_inventory(top)
    assert result == {}

    top.child_groups = [Mock(name="subgroup1"), Mock(name="subgroup2")]
    top.hosts = [Mock(name="host1"), Mock(name="host2")]
    result = cli.toml_inventory(top)
    assert result == {
        'all': {
            'children': ['subgroup1', 'subgroup2'],
            'hosts': {
                'host1': {},
                'host2': {}
            }
        },
        'subgroup1': {},
        'subgroup2': {}
    }

# Generated at 2022-06-12 20:33:24.316063
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    # Initialize needed inputs
    top = object()
    # Run method under test
    actual = InventoryCLI.toml_inventory(top)
    # Verify
    assert actual is not None
###############################################################################

# Generated at 2022-06-12 20:33:26.135336
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    x = InventoryCLI()
    y = x.toml_inventory()
    assert y == {}



# Generated at 2022-06-12 20:33:37.451895
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    my_InventoryCLI=InventoryCLI()
    with pytest.raises(AnsibleOptionsError) as excinfo: # option --host can not be used with option --list
        my_InventoryCLI.post_process_args(dict(host='myhost.domain.com', list=True))
        assert excinfo.value.message == "Conflicting options used, only one of --host, --graph or --list can be used at the same time."
    with pytest.raises(AnsibleOptionsError) as excinfo: # option --graph can not be used with option --list
        my_InventoryCLI.post_process_args(dict(graph=True, list=True))

# Generated at 2022-06-12 20:33:40.582944
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    inventory = InventoryCLI()
    inventory.parser = "Called method post_process_args of class InventoryCLI"
    assert inventory.post_process_args("options") == "Called method post_process_args of class InventoryCLI"

# Generated at 2022-06-12 20:33:42.180554
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    # TODO
    pass


# Generated at 2022-06-12 20:33:48.367590
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    inv = Inventory('tests/integration/inventory/inv_included_group_vars_d')
    inv_cli = InventoryCLI()
    result = inv_cli.json_inventory(inv.groups['all'])
    assert type(result) == dict
    assert '_meta' in result
    assert 'hostvars' in result['_meta']
    assert type(result['_meta']['hostvars']) == dict



# Generated at 2022-06-12 20:33:55.524285
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    args = {'list': True, 'yaml': True, 'pattern': 'all'}
    inventory_args = {'host_list': '/etc/ansible/hosts', 'loader': None, 'sources': None, 'groups': None, 'parser': None}
    CLIARGS = DotDict()
    CLIARGS.update(args)
    context.CLIARGS = CLIARGS
    inventory_cli = InventoryCLI({})
    inventory_cli.loader = DataLoader()
    inventory_cli.inventory = InventoryManager(**inventory_args)
    print(inventory_cli.yaml_inventory(inventory_cli.inventory.groups['all']))


# Generated at 2022-06-12 20:34:10.204024
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    main = InventoryCLI()
    main.run()

# Generated at 2022-06-12 20:34:21.007724
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.display import Display
    from io import StringIO

    context._init_global_context(cli_args=['-i', 'tests/unit/inventory/test_hosts', 'all'], ignore_plugin_load_errors=True)
    context.CLIARGS = {'list':True, 'yaml':True, 'verbosity':0}

    loader = DataLoader()

    inventory = InventoryManager(loader, sources=context.CLIARGS['inventory'])
    display = Display()
    display.verbosity = context.CLIARGS['verbosity']


# Generated at 2022-06-12 20:34:32.033734
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    """Test method inventory_graph of class InventoryCLI"""

    class obj(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    class obj2(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)


# Generated at 2022-06-12 20:34:32.959454
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    pass

# Generated at 2022-06-12 20:34:33.558791
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
  pass

# Generated at 2022-06-12 20:34:42.629801
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.utils import context_objects as co
    from ansible.plugins.loader import vars_loader

    my_loader = AnsibleLoader(None, True, None)

    # Initialize inventory
    my_inventory = Inventory(my_loader)
    my_inventory.subset('all')
    # Create a fake host
    my_host = Host('foobar')
    # Create a fake group
    my_group = Group('ungrouped')
    # Add host to group
    my_group.add_host(my_host)
    # Add group to inventory
    my_inventory.add_group(my_group)

# Generated at 2022-06-12 20:34:46.041356
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    args = ""
    c = InventoryCLI(args)
    assert c.run() is None


# Generated at 2022-06-12 20:34:47.713372
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    # TODO: Implement this test
    pass


# Generated at 2022-06-12 20:34:57.493519
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():

  class test_params(object):
    host = None
    list = False
    graph = True
    pattern = None
    output_file = None
    yaml = None
    toml = False
    show_vars = None
    export = False
    args = None

  context.CLIARGS = test_params()

  test_inventory = '''
  [all]
  test_host0

  [test_group0]
  test_host0
  test_host1

  [test_group1]
  test_host2
  '''

  test_inventory_path = os.path.join(os.path.dirname(__file__), 'data/test_inventory')
  with open(test_inventory_path, 'w') as f:
    f.write(test_inventory)

  test_args

# Generated at 2022-06-12 20:35:08.770433
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    from ansible.cli.inventory import InventoryCLI
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    # Create mock objects
    loader = DataLoader()
    inventory = inventory_loader.get('auto')
    inventory.add_host('test1')
    c = InventoryCLI(args=['test1'])
    c.loader = loader
    c.inventory = inventory
    c.vm = VariableManager()

    # Assert dump method
    results = c._get_host_variables(host=inventory.hosts['test1'])
    assert results == {}

    results = c.dump(results)
    assert results == '{}'

# Generated at 2022-06-12 20:35:46.016162
# Unit test for method toml_inventory of class InventoryCLI

# Generated at 2022-06-12 20:35:55.120657
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    from ansible import constants as C
    from ansible.cli import CLI
    cliargs = CLI.base_parser(const_kwargs={'version': C.__version__}, usage='%(prog)s inventory [--list] [-y]', desc="Displays Ansible inventory data for host(s)", ignore_unknown_options=True)
    cliargs.add_argument('-y', '--yaml', action='store_true', default=False, dest='yaml',
                         help='Use YAML format instead of default JSON')
    cliargs.add_argument('-t', '--toml', action='store_true', default=False, dest='toml',
                         help='Use TOML format instead of default JSON')

# Generated at 2022-06-12 20:35:59.907163
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.host import Host
    class TestGroup(AnsibleBaseYAMLObject):
        yaml_tag = u'!group'
        def __init__(self, host_manager, data=None, **kargs):
            self.hosts = host_manager
            self._data = data or dict()

            self._update_data(**kargs)

    class TestHost(Host):
        def get_vars(self):
            return {'list_var': ['a','b','c'], 'dictionary': {'a': 'b'}, 'string_var': 'string', 'integer_var': 3}


# Generated at 2022-06-12 20:36:10.479787
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    inv = InventoryCLI()
    options = C()
    # Try all three options. Only one should be accepted at a time
    options.host = True
    options.graph = True
    options.list = True
    # Case 1: host, graph and list are all set to True: Error
    try:
        inv.post_process_args(options)
        assert False, "Should raise an AnsibleOptionsError exception"
    except AnsibleOptionsError:
        pass
    # Case 2: host is set to True
    options.graph = False
    options.list = False
    try:
        res0 = inv.post_process_args(options)
        assert res0 == options
    except AnsibleOptionsError:
        assert False, "Should NOT raise an AnsibleOptionsError exception"
    # Case 3: graph is set to True
    options

# Generated at 2022-06-12 20:36:14.823529
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    ctx = {}
    args = DummyOpts()
    args.list = True
    args.graph = None
    args.host = None
    args.yaml = None
    args.toml = None
    args.show_vars = False
    args.export = False
    args.output_file = None
    args.verbosity = 3
    args.args = []
    args.pattern = []
    args.private_key_file = None
    args.check = False
    args.syntax = None
    args.connection = None
    args.module_path = None
    args.forks = 0
    args.become = None
    args.become_method = None
    args.become_user = ''
    args.ask_become_pass = ''
    args.ask_pass = ''


# Generated at 2022-06-12 20:36:21.610887
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    my_inv = InventoryCLI()

    class MockGroup(object):
        def __init__(self, name):
            self.name = name

        def get_hosts(self):
            if self.name == 'all':
                return [Host('host1'), Host('host2')]
            elif self.name == 'group1':
                return [Host('host1')]
            elif self.name == 'group2':
                return [Host('host2')]
            elif self.name == 'group3':
                return [Host('host3')]
            else:
                return [Host('host_not_exist')]

        def get_vars(self):
            if self.name == 'group1':
                return {'var1': 'val1'}
            else:
                return {}


# Generated at 2022-06-12 20:36:25.023289
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    temp_instance=InventoryCLI()
    assert temp_instance.dump({'a':'apple', 'b':'banana', 'c':'cat', 'd':'dog'})=="{'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog'}"


# Generated at 2022-06-12 20:36:30.969777
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    # Create test class object
    T = InventoryCLI()

    # Create test host objects
    host1 = MockHost()
    host1.name = 'host1'
    host2 = MockHost()
    host2.name = 'host2'
    host3 = MockHost()
    host3.name = 'host3'
    host4 = MockHost()
    host4.name = 'host4'
    host5 = MockHost()
    host5.name = 'host5'

    # Create mock groups
    all = MockGroup()
    all.name = 'all'
    all.parent_groups = []
    all.child_groups = [a1, b1, c1, d1, e1]
    all.hosts = [host1, host2, host3, host4, host5]


# Generated at 2022-06-12 20:36:43.078924
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    test_group = MagicMock()
    test_group.name = 'all'
    test_group.child_groups = [MagicMock(), MagicMock(), MagicMock()]
    test_group.child_groups[0].name = 'test1'
    test_group.child_groups[0].child_groups = [MagicMock(), MagicMock()]
    test_group.child_groups[0].child_groups[0].name = 'test1-1'
    test_group.child_groups[0].child_groups[1].name = 'test1-2'
    test_group.child_groups[1].name = 'test2'
    test_group.child_groups[2].name = 'test3'

# Generated at 2022-06-12 20:36:50.294120
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():

    from ansible.inventory.manager import InventoryManager
    from ansible.config.manager import ConfigManager

    config_mgr = ConfigManager()
    config_mgr._parsed_sections = {"DEFAULTS": { "ansible_inventory": "./tests/data/inventory/host_vars" },
                                   "inventory": { "enable_plugins": ["yaml", "vars_plugins"]}}
    # defaults to all
    inventory = InventoryManager(config_mgr, sources="./tests/data/inventory/host_vars")
    inventory.subset("all")

    print(InventoryCLI.dump(inventory.get_host("a").get_vars()))

# Generated at 2022-06-12 20:37:43.580795
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    # passing
    assert InventoryCLI(parser=None).post_process_args(options=None) == None


# Generated at 2022-06-12 20:37:55.110567
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    from ansible.cli import CLI
    from ansible.plugins.inventory.script import InventoryScript
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible import constants as C
    import ansible.plugins.loader as ploader
    import ansible.plugins.inventory as pinventory
    import os

    args = CLI.base_parser(
        usage='test plugin',
        connect_opts=True,
        meta_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        diff_opts=True
    ).parse_args('')

    # Add directories to plugin path
    plugin_path = add_all_plugin_dirs(args.ansible_config_file)
    C.class_loader = pl

# Generated at 2022-06-12 20:37:59.773256
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    class TestInventoryCLI(InventoryCLI):
        def __init__(self):
            super(InventoryCLI, self).__init__()
            self.parser = CLI.base_parser(
                usage='usage: %prog [options]',
                connect_opts=True,
                meta_opts=True,
                runas_opts=True,
                subset_opts=True,
                check_opts=True,
                runtask_opts=True,
                vault_opts=True,
                fork_opts=True,
                module_opts=True,
                sqlite_opts=True,
                output_opts=True,
                defs_opts=True,
            )
            self.post_process_args = lambda x: x

    a = InventoryCLI()

# Generated at 2022-06-12 20:38:05.819610
# Unit test for method post_process_args of class InventoryCLI
def test_InventoryCLI_post_process_args():
    # TODO: test all the different combinations in argparse.
    # This will be hard to do given that argparse always calls super, so
    # the first call always happens in InventoryCLI.
    # TODO: maybe change argparse so it doesn't call super, but instead
    # calls an explicit function in the superclass?
    # Note that this function is difficult to test, because it calls exit()
    # if there is an error.
    # Also note that some of the tests here repeat tests in InventoryCLI.
    # That is wrong, but I don't care about that, I'm going to change it
    # to just have the InventoryCLI tests.
    pass

# Generated at 2022-06-12 20:38:10.060670
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    inventory_cli = InventoryCLI(
        args=['--graph', '--host', 'all', '-i', 'inventory.ini', '--verbose'])
    inventory_cli.setup()
    inventory_cli.post_process_args(inventory_cli.options)
    results = inventory_cli.run()
    assert isinstance(results, dict)

# Generated at 2022-06-12 20:38:15.448371
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    # Create an instance of InventoryCLI
    inventory = InventoryCLI()
    # Create an instance of Inventory
    inventory_instance = Inventory()
    inventory.inventory = inventory_instance
    # Create an instance of Group
    group = Group('Test Group')
    # Add the Group to the Inventory
    inventory_instance.add_group(group)
    # Create an instance of Host
    host = Host('Test Host')
    # Add the Host to the Group
    group.add_host(host)
    # Call the method json_inventory on the InventoryCLI instance
    assert {'Test Group':{'hosts':['Test Host']}} == inventory.json_inventory(group)


# Unit test of method _remove_empty of class InventoryCLI

# Generated at 2022-06-12 20:38:19.810997
# Unit test for method dump of class InventoryCLI

# Generated at 2022-06-12 20:38:30.197272
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inventory = Inventory(loader, groups={"group": Group("group"), "ungrouped": Group("ungrouped"), "all": Group("all")},
                          host_list=[Host('127.0.0.2', port=22), Host('127.0.0.1', port=22)])

    cmd = InventoryCLI(args=[])
    inventory.subset('all').add_host(inventory.get_host(loader.get_basedir()))
    
    cmd.vm = inventory.get_host('all')
    cmd.inventory = inventory
    result = cmd.toml_inventory

# Generated at 2022-06-12 20:38:39.979698
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    def df1(group, depth=0):
        results = {}
        results[group.name] = {}
        if group.name != 'all':
            results[group.name]['hosts'] = [h.name for h in sorted(group.hosts, key=attrgetter('name'))]
        results[group.name]['children'] = []
        for subgroup in sorted(group.child_groups, key=attrgetter('name')):
            results[group.name]['children'].append(subgroup.name)
            if subgroup.name not in seen:
                results.update(df1(subgroup))
                seen.add(subgroup.name)
        if context.CLIARGS['export']:
            results[group.name]['vars'] = self._get_group_variables(group)

# Generated at 2022-06-12 20:38:46.664439
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    module = 'ansible.cli.inventory'
    cls = 'InventoryCLI'

# Generated at 2022-06-12 20:40:48.495190
# Unit test for method inventory_graph of class InventoryCLI

# Generated at 2022-06-12 20:40:54.077053
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    import sys
    import os
    import tempfile

    tmp_file = tempfile.NamedTemporaryFile()
    test_file = tmp_file.name

    f = open(test_file,"w")
    f.write("""
[testgroup]
testhost ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222 # this is a comment
    """)
    f.close()

    cli = InventoryCLI(args=['-i', test_file])
    cli.post_process_args(cli.parser.parse_args([]))
    output = cli.inventory_graph()

    assert output == "@testgroup:\n  |-- testhost"

    os.remove(test_file)

# Generated at 2022-06-12 20:41:01.808062
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():

    ansible_vars = {
        'inventory_dir': '/var/lib/ansible',
        'inventory_file': '/var/lib/ansible/hosts.yaml'
    }

    ansible_vars['inventory_dir'] = bytes(ansible_vars['inventory_dir'], 'utf-8')
    ansible_vars['inventory_file'] = bytes(ansible_vars['inventory_file'], 'utf-8')

    invcli = InventoryCLI()
    invcli.options.json = True
    invcli.options.yaml = False
    assert invcli.dump(ansible_vars) == '{\n    "inventory_dir": "/var/lib/ansible", \n    "inventory_file": "/var/lib/ansible/hosts.yaml"\n}\n'

# Generated at 2022-06-12 20:41:10.625168
# Unit test for method dump of class InventoryCLI
def test_InventoryCLI_dump():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.utils.color import stringc

    loader = DataLoader()

    # inventory_manager
    inventory_manager = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)
    
    # play_source
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='Hello World!'))),
        ]
    )


# Generated at 2022-06-12 20:41:11.375760
# Unit test for method json_inventory of class InventoryCLI
def test_InventoryCLI_json_inventory():
    pass

# Generated at 2022-06-12 20:41:23.238580
# Unit test for method yaml_inventory of class InventoryCLI
def test_InventoryCLI_yaml_inventory():
    from io import StringIO
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    context._init_global_context(load_default_config=False)

    # create the inventory and loader objects
    loader = DataLoader()
    var_manager = VariableManager()
    inventory = InventoryManager(loader, sources='')

    # Create a dummy source plugin to generate the groups
    inventory.add_group('ungrouped')
    host1 = Host(name='host_one')

# Generated at 2022-06-12 20:41:23.835792
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    pass

# Generated at 2022-06-12 20:41:34.344047
# Unit test for method toml_inventory of class InventoryCLI
def test_InventoryCLI_toml_inventory():
    def flatten(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def test_group(name, hosts, children=None, vars={}):
        group = collections.namedtuple('group', ['name', 'hosts', 'child_groups'])
        hosts = [collections.namedtuple('host', ['name'])(name=n) for n in hosts]

# Generated at 2022-06-12 20:41:40.889461
# Unit test for method inventory_graph of class InventoryCLI
def test_InventoryCLI_inventory_graph():
    test_args = ['--graph', 'all']
    parser = InventoryCLI.base_parser(constants.DEFAULT_VERBOSITY,
                                      constants.DEFAULT_INVENTORY)
    cli = InventoryCLI(parser)
    context.CLIARGS = parser.parse_args(test_args)
    context.CLIARGS = parser.parse_args(test_args)
    context.CLIARGS['verbosity'] = constants.DEFAULT_VERBOSITY
    cli.post_process_args(context.CLIARGS)

    # Initialize needed objects
    cli.loader, cli.inventory, cli.vm = cli._play_prereqs()

    # Execute
    start_at = cli._get_group('all')
    result = cli._graph_

# Generated at 2022-06-12 20:41:50.558258
# Unit test for method run of class InventoryCLI
def test_InventoryCLI_run():
    context.CLIARGS = AttrDict()
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['host'] = False
    context.CLIARGS['graph'] = True
    context.CLIARGS['list'] = False
    context.CLIARGS['yaml'] = False
    context.CLIARGS['toml'] = False
    context.CLIARGS['show_vars'] = True
    context.CLIARGS['export'] = False
    context.CLIARGS['output_file'] = None
    context.CLIARGS['args'] = []
    context.CLIARGS['pattern'] = 'all'
    assert InventoryCLI().run()

    context.CLIARGS = AttrDict()