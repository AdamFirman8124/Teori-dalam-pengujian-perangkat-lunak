

# Generated at 2022-06-12 20:11:51.150372
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(None)
    assert adhoc

# Generated at 2022-06-12 20:11:59.251340
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class MockOptions:
        pass

    context.CLIARGS = MockOptions()

    context.CLIARGS.subset = None
    context.CLIARGS.listhosts = False
    context.CLIARGS.module_name = 'ping'
    context.CLIARGS.module_args = None
    context.CLIARGS.args = 'all'
    context.CLIARGS.one_line = False
    context.CLIARGS.tree = None
    context.CLIARGS.forks = 5

    cli = AdHocCLI()

    try:
        cli.run()
    except AnsibleOptionsError as e:
        assert True, str(e)
    else:
        assert False, 'Should exit with an AnsibleOptionsError'



# Generated at 2022-06-12 20:12:09.763483
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Test method run of class AdHocCLI"""
    cli = AdHocCLI()

    # Test with no pattern
    cli._play_ds = lambda pattern, async_val, poll: dict(
        name="Ansible Ad-Hoc",
        hosts=pattern,
        gather_facts='no',
        tasks=[{
            'action': {'module': 'debug', 'args': {'msg': 'hello'}},
            'timeout': '30'}])

# Generated at 2022-06-12 20:12:12.010901
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    AdHocCLI class is instantiated with cli options
    '''
    cli = AdHocCLI(['--help'])
    assert cli.parser is not None
    cli = AdHocCLI(['--version'])
    assert cli.parser is not None
    cli = AdHocCLI([])
    assert cli.parser is not None


# Generated at 2022-06-12 20:12:12.851233
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:12:13.507151
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    instance = AdHocCLI()
    instance.run()

# Generated at 2022-06-12 20:12:14.624077
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' adhoc_cli = AdHocCLI(args) '''

# Generated at 2022-06-12 20:12:21.368965
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import unittest

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block

    # construct the command-line argument string
    # arg_string = 'ansible <host-pattern> [options]'
    arg_string = 'testhost -m shell -a "ls -l"'
    # use the same basedir as AdHocCLI.post_process_args()
    basedir = None

    # construct the argparse.Namespace object that would be built by
    # the external command-line parser
    namespace = argparse.Namespace()
    namespace.check = False

# Generated at 2022-06-12 20:12:32.192388
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:12:42.763878
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    from ansible.config.manager import ConfigManager
    from ansible.inventory import Host, Inventory

    # Create an instance of class AdHocCLI
    cli = AdHocCLI()

    # Create an instance of class ConfigManager
    config_manager = ConfigManager()

    # Assert AdHocCLI class constructor for the first arg
    assert cli.options_module == config_manager
    assert cli.options == config_manager.options

    # Assert AdHocCLI class constructor for the second arg
    assert cli.args == []

    # Assert AdHocCLI class constructor for the third arg
    assert cli.callback == config_manager.options['stdout_callback']

    # Create an instance of class Inventory
    inventory = Inventory()

    # Create an instance of class Host

# Generated at 2022-06-12 20:12:52.714777
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(args=[])
    assert adhoc is not None

# Generated at 2022-06-12 20:12:59.654976
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    display.verbosity = 2
    # See issue #19477 for why we need to wrap sys.argv
    class AdHocCLITestClass(AdHocCLI):
        def __init__(self):
            super(AdHocCLITestClass, self).__init__()
            self.args = 'all -i /etc/ansible/hosts -m ping'

    x = AdHocCLITestClass()
    x.parse()
    x.run()


# Generated at 2022-06-12 20:13:04.328759
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Set up arguments mock
    mock_args = [
                '-i', 'inventory',
                '-m', 'ping',
                '-a', 'arguments',
                '--list-hosts',
                'host1,host2'
    ]

    # Initialize AdHocCLI with given arguments
    adhoc_cli = AdHocCLI(args=mock_args)
    adhoc_cli.parse()

    # Run method and check its return
    assert adhoc_cli.run() == 0


# Generated at 2022-06-12 20:13:06.128896
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    display.deprecated("cli.run() is deprecated and will be removed soon. Please use cli.parse() and cli.run()", version='2.14')
    cli.run()

# Generated at 2022-06-12 20:13:11.377967
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    from ansible import context
    context.CLIARGS = {}
    adhoc_cli = AdHocCLI()
    assert isinstance(adhoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:13:11.929193
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:13.659442
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=['-i', 'localhost,'])
    assert cli.run() == 0

if __name__ == '__main__':
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:13:23.139979
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class MockInventory():

        def __init__(self):
            self.hosts = ['127.0.0.1']
            self.pattern = '127.0.0.1'

    class MockDisplay():
        def __init__(self):
            self.display_ok = False

        def display(self, message):
            self.display_ok = True

    inventory = MockInventory()
    display = MockDisplay()

    args = ['-m', 'ping', '127.0.0.1']
    options = opt_help.parse_args(args)
    AdHocCLI(inventory, display).run(args, options)

    assert display.display_ok == True



# Generated at 2022-06-12 20:13:25.691442
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' Unit test for method run of class AdHocCLI '''
    adhoc_obj = AdHocCLI(["-m", "ping", "localhost"])
    adhoc_obj.run()

# Generated at 2022-06-12 20:13:32.315523
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Test if AdHocCLI.run().
    '''
    import ansible.cli.adhoc

    adhoc = ansible.cli.adhoc.AdHocCLI(["localhost", "-m", "ping"])

    result = adhoc.run()

    assert result == 0

# Generated at 2022-06-12 20:13:40.958470
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()

# Generated at 2022-06-12 20:13:41.472373
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:48.028867
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()

    module = 'setup'
    args = ''
    pattern = 'localhost'

    context.CLIARGS = dict(
        async_val=None,
        check=None,
        connection=None,
        forks=None,
        inventory=None,
        listhosts=None,
        module_name=module,
        module_args=args,
        one_line=None,
        output_file=None,
        poll_interval=None,
        subset=None,
        seconds=None,
        ssh_common_args=None,
        ssh_extra_args=None,
        vault_password_files=None,
        verbosity=None,
        start_at_task=None,
        args=pattern
    )

    cli.run()

# Unit

# Generated at 2022-06-12 20:13:57.256408
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Monkey patch CLI to use test function
    CLI.ask_passwords = test_ask_passwords

# Generated at 2022-06-12 20:13:58.988783
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    # Check whether requirement is instance of class AdHocCLI
    assert isinstance(adhoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:13:59.528805
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:00.487447
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()

# Generated at 2022-06-12 20:14:07.560258
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    def _get_AdHocCLI(**kwargs):
        cli = AdHocCLI(**kwargs)
        cli.parse()
        return cli
    def _get_mocked_task_queue_manager(mocker):
        m_stats = mocker.MagicMock()
        m_run_tree = mocker.patch('ansible.cli.adhoc.run_tree')
        def _get_tqm_run(mocker, playbook):
            def _run(p):
                assert p == playbook
                return 123
            mock_run = mocker.patch.object(TaskQueueManager, 'run', side_effect=_run)
            mocker.patch.object(TaskQueueManager, 'send_callback')
            mocker.patch.object(TaskQueueManager, '_stats', m_stats)

# Generated at 2022-06-12 20:14:10.685771
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' constructor should fail without required options '''
    with pytest.raises(AnsibleOptionsError):
        assert AdHocCLI()
    with pytest.raises(AnsibleOptionsError):
        assert AdHocCLI(["-h"])


# Generated at 2022-06-12 20:14:22.765865
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.console.console import ConsoleCLI
    from ansible.utils.display import Display
    Display._verbosity = 1
    Display.verbosity = 1
    # test_AdHocCLI_run.py:27: error: [AdHocCLI] Bad hosts pattern: 'all'
    # with pytest.raises(AnsibleError) as excinfo:
    #     cli = AdHocCLI(['-m','setup','all'])
    # assert 'Bad hosts pattern: \'all\'' in str(excinfo.value)
    cli = AdHocCLI(['-m','setup','dummyhost1'])
    result = cli.run()
    assert result == 0

    console = ConsoleCLI()

# Generated at 2022-06-12 20:14:38.912273
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
      pass

# Generated at 2022-06-12 20:14:45.600067
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' AdHocCLI.run() returns 0 when success '''

    # Initialize context and read config file
    context.CLIARGS = {}
    context.CLIARGS['module_name'] = 'ping'
    context.CLIARGS['module_args'] = 'this=that'
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['tree'] = False
    context.CLIARGS['one_line'] = False
    context.CLIARGS['verbosity'] = 0

    # Test that run() function return 0
    cli = AdHocCLI()
    assert cli.run() == 0

# Generated at 2022-06-12 20:14:49.831042
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Test the function run of class AdHocCLI
    '''

    def get_module_name(module_name):
        '''
        Returns the module_name
        '''
        return module_name

    def is_playbook():
        '''
        Returns True
        '''
        return True

    adhoc_cli = AdHocCLI()
    adhoc_cli.get_module_name = get_module_name
    adhoc_cli.is_playbook = is_playbook

    assert adhoc_cli.run() == 0

# Generated at 2022-06-12 20:14:51.528874
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoccli = AdHocCLI()
    adhoccli.run()

# Generated at 2022-06-12 20:15:01.072264
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli import CLI

    cli = CLI()
    cli.options = dict()
    cli.options['module_name'] = 'shell'
    cli.options['module_args'] = 'whoami'
    cli.options['one_line'] = True
    cli.options['verbosity'] = 0
    cli.options['ask_pass'] = False
    cli.options['ask_become_pass'] = False
    cli.options['host_pattern'] = 'localhost'
    cli.options['listhosts'] = False
    a = AdHocCLI(cli.options)
    assert a.run() == 0

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:15:07.105991
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class FakeModule:
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            return 'bin/ansible'

        def get_parsable_facts(self, *args, **kwargs):
            return {}

    display.verbosity = 3


# Generated at 2022-06-12 20:15:08.963832
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(['-m', 'ping'])

    assert adhoc.parser is not None
    assert adhoc.subparser_loader is not None

# Generated at 2022-06-12 20:15:09.435728
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:15.745596
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import ansible.plugins.loader as plugin_loader
    # instantiate the object to be tested
    ad_hoc_cli = AdHocCLI(['host_pattern'])
    assert isinstance(ad_hoc_cli, AdHocCLI)
    module_name = 'ping'
    module_args = 'args'
    # mock the methods
    ad_hoc_cli.ask_passwords = lambda: ('sshpass', 'becomepass')
    ad_hoc_cli._play_prereqs = lambda: ('loader', 'inventory', 'variable_manager')
    ad_hoc_cli.get_host_list = lambda inventory, subset, pattern: ['host1', 'host2']

# Generated at 2022-06-12 20:15:20.173084
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    runner = AdHocCLI([])
    runner.post_process_args = lambda options, args: options
    result = runner.run()
    assert result == 0, "AdHocCLI_run test failed"
    return 0

if __name__ == "__main__":
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:15:53.771657
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli.parser.prog == 'ansible'


# Generated at 2022-06-12 20:16:01.550951
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    cli = AdHocCLI()
    assert cli.module_name == 'command'
    assert cli.module_args == ''
    assert cli.pattern is None
    assert cli.one_line is False
    assert cli.tree is None
    assert cli.check is False
    assert cli.verbosity == 0
    assert cli.ask_passwords is None
    assert cli.ask_sudo_pass is False
    assert cli.ask_su_pass is False
    assert cli.timeout is None
    assert cli.ssh_common_args is None
    assert cli.sftp_extra_args is None
    assert cli.scp_extra_args is None
    assert cli.ssh_extra_args is None
    assert cli.force_handlers is False

# Generated at 2022-06-12 20:16:04.665138
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad_hoc_obj = AdHocCLI()
    assert isinstance(ad_hoc_obj, AdHocCLI)
    assert isinstance(ad_hoc_obj.parser, CLI.parser_class)


# Generated at 2022-06-12 20:16:09.143255
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    args = ['-i', 'localhost,']
    context.CLIARGS = context.CLI.parse(args)
    context.CLIARGS['module_name'] = 'ping'
    addhoc = AdHocCLI()
    exit_code = addhoc.run()
    assert exit_code == 0

# Generated at 2022-06-12 20:16:16.900080
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class mock_adhoc_cli:
        def __init__(self):
            self.host = 'localhost'
            self.pattern = 'localhost'

# Generated at 2022-06-12 20:16:19.077916
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    #assert adhoc_cli.parser is not None


# Generated at 2022-06-12 20:16:22.227740
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''Unit test for constructor of class AdHocCLI'''
    adhoc_obj = AdHocCLI()
    assert adhoc_obj._display is not None

# Generated at 2022-06-12 20:16:24.301602
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    This method is to handle adhoc ansible cli command execution
    :return: None
    '''
    pass

# Generated at 2022-06-12 20:16:32.131313
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import unittest2 as unittest
    from ansible.parsing.dataloader import DataLoader

    class TestAdHocCLI(unittest.TestCase):
        """ ansible adhoc cli tool """

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_adhoc_cli(self):
            """ ansible adhoc cli tool """
            cli = AdHocCLI(['ping'])
            cli.post_process_args(dict(inventory='/etc/ansible/hosts', listhosts=True))
            result = cli.run()
            self.assertEqual(result, 0)

# Generated at 2022-06-12 20:16:40.202423
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    args = ['/bin/ansible',
            '-m', 'shell',
            '-a', "'ls'",
            'localhost'
            ]

    parser = opt_help.setup_adhoc_parser()
    options = context.CLIARGS = parser.parse_args(args[1:])

    cli = AdHocCLI()
    cli.init_parser()
    cli.post_process_args(options)

    cli.run()

# Generated at 2022-06-12 20:18:03.840247
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    from ansible.cli.adhoc import AdHocCLI

    # test constructor of class AdHocCLI
    ad_hoc = AdHocCLI(args=['-m', 'setup', 'localhost'])

    # test ad_hoc.get_optparser
    parser = ad_hoc.get_optparser()

    # test ad_hoc.post_process_args
    options = ad_hoc.post_process_args(parser.parse_args(['-m', 'setup', 'localhost']))

    # test ad_hoc.run()
    ad_hoc.run()


if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:18:09.636093
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Some pre-requisites required to create objects
    loader, inventory, variable_manager = ansible.cli.adhoc.AdHocCLI()._play_prereqs()
    # We want to mock the host list
    # So, create a fresh class
    class mock_AdHocCLI(AdHocCLI):
        def get_host_list(self, inventory, subset, pattern):
            return ['hostname']
    # Create an object of the above class
    m_obj = mock_AdHocCLI()
    # Variable to hold the return value of run method
    result = m_obj.run()
    # Assert the return value
    assert result == 0

# Generated at 2022-06-12 20:18:10.428910
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
  pass

# Generated at 2022-06-12 20:18:20.951353
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    args = ["localhost", "-m", "ping", "-a", "data=test"]

# Generated at 2022-06-12 20:18:31.222786
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.playbook.play import Play

    args = 'test_args'
    async_val = 10
    poll = 1
    pattern = 'test_pattern'
    sshpass = 'test_sshpass'
    becomepass = 'test_becomepass'
    check_raw = False
    # test branch : context.CLIARGS['module_name'] in C.MODULE_REQUIRE_ARGS = False

# Generated at 2022-06-12 20:18:38.051090
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:18:46.463468
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    context.CLIARGS = {}
    s = AdHocCLI()

# Generated at 2022-06-12 20:18:52.386270
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # Mock
    class myMockTaskQueueManager(TaskQueueManager):
        def __init__(self, inventory, variable_manager, loader, passwords, stdout_callback, run_additional_callbacks=True, run_tree=False, forks=None):
            super(myMockTaskQueueManager,self).__init__(inventory, variable_manager, loader, passwords, stdout_callback, run_additional_callbacks, run_tree, forks)
            self.stdout_callback = stdout_callback
            self.run_additional_callbacks = run_additional_callbacks
            self.run_tree = run_tree
            self.forks = forks
        def cleanup(self):
            pass
        def load_callbacks(self):
            pass
        def send_callback(self, a,b):
            pass
       

# Generated at 2022-06-12 20:19:00.640693
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Create an instance of the AdHocCLI class
    ad_hoc_cli = AdHocCLI(args=[])
    # Create an instance of the parser
    parser = ad_hoc_cli.parser
    # Get the arguments from the user
    options = parser.parse_args(['-m ping', 'dummy1'])
    # Check for conflicts in arguments
    ad_hoc_cli.validate_conflicts(options)
    # Post process and validate the arguments
    options = ad_hoc_cli.post_process_args(options)
    # Execute the run method with the options from the user
    ad_hoc_cli.run()

# Generated at 2022-06-12 20:19:02.185714
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    unit test for AdHocCLI class
    '''

    ad_hoc_cli = AdHocCLI(args=[])