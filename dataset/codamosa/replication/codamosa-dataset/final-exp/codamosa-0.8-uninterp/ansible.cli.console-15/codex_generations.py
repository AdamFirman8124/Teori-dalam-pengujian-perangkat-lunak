

# Generated at 2022-06-12 20:23:11.651133
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    pass


# Generated at 2022-06-12 20:23:17.921323
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    playbook_path = C.name

# Generated at 2022-06-12 20:23:20.464847
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console=ConsoleCLI(args=[])
    console.modules=("setup","debug")
    console.helpdefault("setup")
    console.helpdefault("debug")

# Generated at 2022-06-12 20:23:27.867909
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    # Arrange
    con = ConsoleCLI()
    con.modules = ['ping']
    con.loader = DictDataLoader({'core': DictDataFinder({'doc_fragments': {}})})
    con.module_args = lambda x: ['ping']
    def display(msg):
        print(msg)
    con.display = display

    # Act
    con.helpdefault('ping')

    # Assert
    # FIXME: No asserts here


# Generated at 2022-06-12 20:23:31.032898
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    ccli = ConsoleCLI()
    assert ccli.list_modules() == [x.replace('.py', '') for x in os.listdir(MODULE_PATH)]



# Generated at 2022-06-12 20:23:39.027254
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
  hosts = [
    Host(name='host1'),
    Host(name='host2'),
    Host(name='host3'),
    Host(name='host4'),
    Host(name='host5')
  ]

  groups = [
    Group(name='group1'),
    Group(name='group2'),
    Group(name='group3'),
    Group(name='group4'),
    Group(name='group5')
  ]

  inventory = Inventory(hosts=hosts, groups=groups)
  loader = DictDataLoader({})
  pattern = "host1"
  console_cli = ConsoleCLI(
    None,
    loader,
    inventory,
    VariableManager(),
    pattern
  )


# Generated at 2022-06-12 20:23:40.039815
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    console = ConsoleCLI()
    assert 'ping' in console.list_modules()

# Generated at 2022-06-12 20:23:43.437375
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    console_cli = ConsoleCLI(None, None)
    modules = console_cli.list_modules()
    assert 'shell' in modules
    assert 'ping' in modules

# Generated at 2022-06-12 20:23:47.160628
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    a = ConsoleCLI()
    modules = a.list_modules()
    assert len(modules) > 0
    assert "ping" in modules
    assert "setup" in modules
    a.do_exit("")


# Generated at 2022-06-12 20:23:50.319327
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    """
    Unit test for method complete_cd of class ConsoleCLI
    """
    # Initialize
    cli = ConsoleCLI()
    # Test
    assert True == ""
## Unit test for method completedefault of class ConsoleCLI

# Generated at 2022-06-12 20:24:57.008249
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    # mock
    mock_module_name = 'setup'
    mock_in_path = "/usr/local/lib/python3.5/lib-dynload/_io.cpython-35m-x86_64-linux-gnu.so"
    mock_oc = {
        'description': [
            'Gathers facts about remote hosts'
        ],
        'options': {
            'filter': {
                'description': [
                    'When supplied, the ansible_facts key will contain only the facts matched by the filter.'
                ],
                'required': False
            }
        }
    }

    # prepare
    consoleCLI_instance = ConsoleCLI()

    # execute
    plugin_docs.get_docstring = MagicMock(return_value=(mock_oc, None, None, None))
    module_loader

# Generated at 2022-06-12 20:25:04.116532
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    # FIXME: Do not use hard coded path
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    units = ConsoleCLI('ansible-console', os.path.join(fixture_path, 'inventory'))
    assert units.complete_cd('', 'cd ', 4, 4) == ['all', 'bar', 'foo']



# Generated at 2022-06-12 20:25:07.013267
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
	pyfaux.debug(Shell())
	pyfaux.go()
	pyfaux.debug(ConsoleCLI())
	pyfaux.go()
	test_object = ConsoleCLI()
	test_object.cmdloop()
	pyfaux.assertTrue(test_object)

# Generated at 2022-06-12 20:25:15.123195
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    """
    Test helpdefault method of ConsoleCLI

    It is difficult to test the code from helpdefault method
    because it is difficult to get the task.action.args
    into the method for testing.

    """

    # Reset the module to its initial state
    context.CLIARGS = ansible.utils.context._init_global_context()
    options = context.CLIOptionParser()
    options.parse()

    # Make a ConsoleCLI instance

# Generated at 2022-06-12 20:25:16.468513
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
  # Test when not using a shell module
  # Test when using a shell module
  pass


# Generated at 2022-06-12 20:25:17.972610
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    pass

# Generated at 2022-06-12 20:25:26.008680
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    @mock.patch('ansible.cli.console.Display', autospec=True)
    @mock.patch('ansible.cli.console.read_vault_password', autospec=True)
    @mock.patch('ansible.cli.console.SubCommand', autospec=True)
    @mock.patch('ansible.cli.console.CLI', autospec=True)
    def _test_console_cli(CLI, SubCommand, read_vault_password, Display, capsys):
        cli = CLI()
        subcmd = SubCommand(cli)
        subcmd.parse()

        console_cli = ConsoleCLI(subcmd)
        console_cli.inventory = mock.Mock()

        # Case 1: host_filter matches multiple hosts
        console_cli.inventory.list_hosts.return_

# Generated at 2022-06-12 20:25:29.485514
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    cli = ConsoleCLI()
    cli.default = Mock(return_value=True)
    cli.modules = ["ansible", "command"]
    cli.helpdefault("command")
    assert cli.default.call_args[0][0] == "command"

# Generated at 2022-06-12 20:25:33.477820
# Unit test for method default of class ConsoleCLI
def test_ConsoleCLI_default():
    host = '''
         localhost
           | SUCCESS => {
           "ansible_facts": {
               "discovered_interpreter_python": "/usr/bin/python"
           },
           "changed": false
       }
    '''
    test = ConsoleCLI()
    test.default(host)



# Generated at 2022-06-12 20:25:34.784913
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    console = ConsoleCLI()
    with pytest.raises(Exception):
        console.completedefault(text, line, begidx, endidx)


# Generated at 2022-06-12 20:26:04.652495
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
  obj = ConsoleCLI()

# Generated at 2022-06-12 20:26:12.254008
# Unit test for method complete_cd of class ConsoleCLI
def test_ConsoleCLI_complete_cd():
    """
    Test if a completion is returned for the host 'ubuntu-xenial'.
    :return:
    """
    hostname = 'ubuntu-xenial'
    cli = ConsoleCLI()
    cli.inventory = ansible.inventory.Inventory(loader=ansible.cli.CLI.CLI.loader,
                                                variable_manager=ansible.cli.CLI.CLI.variable_manager)
    cli.inventory.get_host(hostname)
    cli.cwd = 'all'
    completion = cli.complete_cd(hostname, 'cd {0}'.format(hostname), 4, len(hostname))
    assert(hostname == completion[0])


# TODO: add unit test

# Generated at 2022-06-12 20:26:16.985628
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    class MockShellModule:
        def run(self, module_name):
            return None

    with patch.object(MockShellModule, 'run') as shell:
        console = ConsoleCLI(MockShellModule())
        console.helpdefault('shell')
        assert shell.called


# Generated at 2022-06-12 20:26:24.329487
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():

    print("Testing ConsoleCLI.do_list")

    # Test 1:

    print("  Test 1: unsupported argument")

    consoleCLI = ConsoleCLI()
    consoleCLI.inventory = ["group1", "group2"]
    consoleCLI.selected = ["host1", "host2"]

    consoleCLI.do_list("UNSUPPORTED_ARG")

    # Test 2:

    print("  Test 2: supported argument")

    consoleCLI = ConsoleCLI()
    consoleCLI.inventory = ["group1", "group2"]
    consoleCLI.selected = ["host1", "host2"]

    consoleCLI.do_list("groups")



# Generated at 2022-06-12 20:26:27.197349
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console = ConsoleCLI()
    assert console.helpdefault('debug')
    assert not console.helpdefault('debugging')


# Generated at 2022-06-12 20:26:37.310391
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    pb = PlaybookExecutor(playbooks=['./test/test.yaml'],
                          inventory=inventory,
                          variable_manager=variable_manager,
                          loader=loader,
                          options=Options(),
                          passwords={})
    pb._tqm._stdout_callback = Mock()

    def do_cd(arg):
        if arg:
            self.cwd = arg

# Generated at 2022-06-12 20:26:38.010333
# Unit test for method set_prompt of class ConsoleCLI
def test_ConsoleCLI_set_prompt():
    pass

# Generated at 2022-06-12 20:26:39.489281
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-12 20:26:45.942152
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    from units.compat.mock import patch
    from units.compat.unittest import TestCase
    from ansible.cli.console import ConsoleCLI
    import ansible.constants as C
    test = TestCase()
    argspec = {
        '_meta': {
            'hostvars': {},
        },
        'all': {
            'hosts': [],
            'vars': {},
        },
    }
    (cwd, _) = os.path.split(os.path.realpath(__file__))
    test.assertEqual(cwd.rsplit(os.sep, 1)[-1], 'test')
    os.chdir(cwd)

# Generated at 2022-06-12 20:26:54.550672
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():
    def mocked_complete(self, *args):
        pass
    orig_complete = ConsoleCLI.completedefault
    ConsoleCLI.completedefault = mocked_complete
    cli = ConsoleCLI()
    cli.list_modules = lambda: ['setup', 'group_by', 'add_host']
    cli.module_args('setup') == ['filter', 'gather_subset', 'gather_timeout',
                                 'gather_facts', 'no_log', '_uses_shell']
    ConsoleCLI.completedefault = orig_complete



# Generated at 2022-06-12 20:27:24.994079
# Unit test for method list_modules of class ConsoleCLI
def test_ConsoleCLI_list_modules():
    test_input_list_modules = ['']
    test_output_list_modules = []
    test_input_list_modules[0] = os.path.join(os.environ['ANSIBLE_LIBRARY'], 'modules')
    cli = ConsoleCLI()
    cli._find_modules_in_path(test_input_list_modules[0])
    test_output_list_modules = cli.modules
    assert test_output_list_modules != []


# Generated at 2022-06-12 20:27:31.628001
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    """
    Test Name: test_ConsoleCLI_helpdefault
    """
    print("Test start")
    plugin = ConsoleCLI()
    plugin.init_parser()
    plugin.parse()

    plugin.module_loader = module_loader
    plugin.plugin_loader = plugin_loader
    plugin.fragment_loader = fragment_loader
    plugin.terminal_width = 80

    plugin.init_parser()
    plugin.parse()

    plugin.parse()
    plugin.load_plugins()
    plugin.run()
    print("Test End")

if __name__ == '__main__':
    test_ConsoleCLI_helpdefault()

# Generated at 2022-06-12 20:27:40.474306
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    expected = {
        # for method completedefault of class ConsoleCLI
        (['command'], '', 0, 0, ['all']): {'completions': [], 'return': None},
        (['command', 'a'], '', 0, 0, ['all']): {'completions': [], 'return': None},
        (['command', 'a'], '', 1, 0, ['host1', 'host2', 'host3']): {'completions': ['', '2', '3'], 'return': None},
    }

    for args, kwargs, result in iteritems(expected):
        yield check_complete, ConsoleCLI, 'completedefault', args, kwargs, result



# Generated at 2022-06-12 20:27:45.868548
# Unit test for method run of class ConsoleCLI
def test_ConsoleCLI_run():
    """Test run() method"""
    cli = ConsoleCLI(args=['ansible-console', '--inventory', '../../inventory', '--pattern', 'localhost', '-vvvv'])
    cli.pattern = 'localhost'
    cli.cwd = 'localhost'
    cli.check_mode = False
    cli.diff = False
    cli.become = False
    cli.forks = 5
    cli.task_timeout = 0
    cli.run()
    cli.cmdloop()

# Generated at 2022-06-12 20:27:58.674827
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    from __main__ import display, C

    inventory_manager = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)
    loader = DataLoader()
    passwords = {}

    context._init_global_context(loader=loader, inventory=inventory_manager, variable_manager=variable_manager, version_info=__version__)
    consolecli = ConsoleCLI(
        inventory=inventory_manager,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        config=C,
    )
    mock_input = MagicMock(return_value='exit')
    mock_input.side_effect = ['exit']

# Generated at 2022-06-12 20:27:59.974970
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    console = ConsoleCLI()
    console.run()

# Generated at 2022-06-12 20:28:01.553024
# Unit test for method do_cd of class ConsoleCLI
def test_ConsoleCLI_do_cd():
	pass


# Generated at 2022-06-12 20:28:04.838029
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    #Tests the helpdefault method
    c=ConsoleCLI()
    c.helpdefault('123')

if __name__ == '__main__':
    test_ConsoleCLI_helpdefault()

# Generated at 2022-06-12 20:28:09.941202
# Unit test for method do_timeout of class ConsoleCLI
def test_ConsoleCLI_do_timeout():
    def mock_do_timeout(self, arg):
        return self.do_timeout(arg)
    mock_c = MagicMock()
    mock_args = MagicMock()
    ConsoleCLI.do_timeout = mock_do_timeout
    ConsoleCLI.do_timeout(mock_c, mock_args)


# Generated at 2022-06-12 20:28:10.764409
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    ConsoleCLI.cmdloop()

# Generated at 2022-06-12 20:29:09.389476
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():

    class TestConsoleCLI(ConsoleCLI):

        def _ask_passwords(self):
            return ('', '')

        def _play_prereqs(self):
            class TestInventory(Inventory):
                def __init__(self, *args, **kwargs):
                    super(TestInventory, self).__init__(*args, **kwargs)

                def get_hosts(self, pattern):
                    if pattern == 'all':
                        return ['127.0.0.1', '10.20.30.40']
                    elif pattern == '127.0.0.1':
                        return ['127.0.0.1']
                    elif pattern == '10.20.30.40':
                        return ['10.20.30.40']
                    else:
                        return []


# Generated at 2022-06-12 20:29:12.032351
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    c = ConsoleCLI()
    c.modules = ['command']
    c.module_args('command')
    c.completedefault('test', 'command ', 0, 4)

# Generated at 2022-06-12 20:29:15.133235
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    console = ConsoleCLI()

# Generated at 2022-06-12 20:29:21.363703
# Unit test for method module_args of class ConsoleCLI
def test_ConsoleCLI_module_args():

    class TestConsoleCLI(ConsoleCLI):

        def __init__(self):
            super(TestConsoleCLI, self).__init__()
            self.modules = ['docker_image']

    console = TestConsoleCLI()
    
    expected_result = ['name', 'build', 'rm', 'force', 'path', 'dockerfile', 'nocache', 'pull', 'port', 'tags', 'timeout',
                       'use_tls', 'tls_verify', 'tls_cert', 'tls_key', 'tls_cacert', 'tls_cert_path', 'tls_key_path',
                       'tls_cacert_path']
    result = console.module_args('docker_image')

    assert len(result) == len(expected_result)

# Generated at 2022-06-12 20:29:32.207592
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    arguments = dict(
        become=None,
        become_method=None,
        become_user=None,
        check=None,
        connection=None,
        diff=None,
        extra_vars=None,
        forks=100,
        help=False,
        inventory=None,
        limit=None,
        listhosts=None,
        module_path=None,
        pattern=None,
        private_key_file=None,
        remote_user=None,
        subset=None,
        syntax=None,
        tags=None,
        timeout=None,
        tree=None,
        vault_password_file=None,
        verbosity=0,
    )

    # Testing method helpdefault of class ConsoleCLI.
    # [Errno 2] No such file or directory:
    #

# Generated at 2022-06-12 20:29:39.921925
# Unit test for method do_list of class ConsoleCLI
def test_ConsoleCLI_do_list():
    # Setup the class
    ansible_console = ConsoleCLI()

    # Create groups
    groups = [
        'group1',
        'group2',
        'group3'
    ]
    ansible_console.groups = groups

    # Create hosts
    hosts = [
        'host1',
        'host2',
        'host3',
        'host4',
        'host5'
    ]
    ansible_console.hosts = hosts

    # Test do_list for group
    for group in groups:
        # Test group match
        result = ansible_console.do_list(group)
        assert result is None

    # Test do_list for host
    for host in hosts:
        # Test host match
        result = ansible_console.do_list(host)
        assert result is None

   

# Generated at 2022-06-12 20:29:48.398253
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():

    class FakeConsoleCLI(ConsoleCLI):

        def __init__(self):
            ConsoleCLI.__init__(self)

        def module_args(self, module_name):
            return ['name', 'state', 'owner']

        def list_modules(self):
            return ['lineinfile']

    cli = FakeConsoleCLI()
    line = "lineinfile owner="
    text = cli.completedefault(text=line.split()[-1], line=line, begidx=len(line.split()[-1]), endidx=len(line.split()[-1]))
    assert text == ['name="', 'state="']

    line = "lineinfile name=state="

# Generated at 2022-06-12 20:29:50.143903
# Unit test for method helpdefault of class ConsoleCLI
def test_ConsoleCLI_helpdefault():
    content = ConsoleCLI.helpdefault("yum")
    assert_equal(content,'Manages packages with the ``yum`` package manager')

# Generated at 2022-06-12 20:29:50.676511
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    pass



# Generated at 2022-06-12 20:29:52.114337
# Unit test for method cmdloop of class ConsoleCLI
def test_ConsoleCLI_cmdloop():
    with pytest.raises(TypeError):
        ConsoleCLI.cmdloop()


# Generated at 2022-06-12 20:31:55.224293
# Unit test for method completedefault of class ConsoleCLI
def test_ConsoleCLI_completedefault():
    from ansible.cli import CLI
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase, default
    class TestCLI(CLI):
        def get_optparser(self):
            return CLI.get_optparser(self, version=__version__, start=False)
    class MyInventory(Inventory):
        pass
    class TestConsoleCLI(ConsoleCLI):
        def display(self, msg, *args, **kwargs):
            pass
        def prompt(self, prompt, opts=None, private=False):
            pass
       