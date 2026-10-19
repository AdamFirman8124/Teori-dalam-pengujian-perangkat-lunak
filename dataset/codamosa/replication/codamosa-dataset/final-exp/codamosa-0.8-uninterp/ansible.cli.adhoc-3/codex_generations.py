

# Generated at 2022-06-12 20:11:51.151684
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # test: new AdHocCLI().run()
    pass


# Generated at 2022-06-12 20:11:54.392516
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:11:56.048308
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    instance=AdHocCLI()
    return instance.run()

# Generated at 2022-06-12 20:11:57.268413
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    args = ['-h']
    cli = AdHocCLI(args)

# Generated at 2022-06-12 20:12:08.197795
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class Dummy(AdHocCLI):
        def __init__(self, *args, **kwargs):
            self.options = {
                'module_name': 'ping',
                'module_args': '',
                'forks': 10,
                'seconds': 0,
                'poll_interval': 5,
                'listhosts': False,
                'subset': False,
                'tree': None,
                'verbose': 0,
                'ask_pass': False,
                'ask_become_pass': False
            }
            self.ask_passwords = lambda: None

        def run(self):
            super(Dummy, self).run()

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Set up host inventory

# Generated at 2022-06-12 20:12:11.400045
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli is not None

# Generated at 2022-06-12 20:12:20.322317
# Unit test for method post_process_args of class AdHocCLI
def test_AdHocCLI_post_process_args():
    def mock_verbose(self, msg, *args, **kwargs):
        print(msg)

    # Mock object attributes
    setattr(Display, 'verbosity', 0)
    # Mock method
    setattr(Display, 'verbose', mock_verbose)

    # Create a new AdHocCLI object
    my_adhoc = AdHocCLI()
    my_adhoc.init_parser()

    # Construct options object
    options = my_adhoc.parser.parse_args()

    # Call method post_process_args of class AdHocCLI
    my_adhoc.post_process_args(options)

    # Expected result
    result = AdHocCLI.post_process_args(my_adhoc, options)

    print("Expected result:")

# Generated at 2022-06-12 20:12:30.214594
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # Testing with existing parser object
    parser = CLI.base_parser(
        usage='%prog [options]',
        epilog="""This is the CLI for Ansible ad hoc""",
    )
    ad_hoc_cli = AdHocCLI(parser)

    # Testing with default parser object
    ad_hoc_cli = AdHocCLI()

    # Testing with default parser object
    ad_hoc_cli = AdHocCLI()

    # Testing with list of options
    ad_hoc_cli = AdHocCLI(['-m', ''])

    # Testing with list of options
    ad_hoc_cli = AdHocCLI(['-m', '', '-a', 'foo=bar'])

# Generated at 2022-06-12 20:12:35.671027
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI(args=[])
    module_name = C.DEFAULT_MODULE_NAME
    module_args = C.DEFAULT_MODULE_ARGS
    pattern = "test_pattern"
    obj.post_process_args({'module_name': module_name, 'module_args': module_args, 'args': pattern})
    assert obj.args == [pattern]


# Generated at 2022-06-12 20:12:43.823329
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    cli = AdHocCLI([])
    cli.options = cli.parse()

    loader, inventory, variable_manager = cli._play_prereqs()

    # define the tasks
    play_ds = dict(
        name="Ansible Ad-Hoc",
        hosts=['163.172.181.146'],
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='uname -a'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )

    # create play with tasks
    play = Play().load(play_ds, variable_manager=variable_manager, loader=loader)

    # Run it - instantiate task queue manager, which takes care

# Generated at 2022-06-12 20:13:07.515213
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create AdHocCLI object
    cli = AdHocCLI()

    # Create fake object for args
    class obj:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                self.__dict__[k] = v

    args = obj(module_name='test', module_args='test')
    context.CLIARGS = args

    # Create fake objects for self._play_prereqs()
    loader = 'test'
    inventory = 'test'
    variable_manager = 'test'
    cli._play_prereqs = lambda: (loader, inventory, variable_manager)

    # Set empty list for get_host_list
    cli.get_host_list = lambda: []

    # Assert test condition
    assert cli.run

# Generated at 2022-06-12 20:13:13.485735
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import pytest

    # Test: Under normal conditions
    def run_normal():
        ''' Test AdHocCLI.run() under normal operation '''
        # Setup:
        def mock_ask_passwords(self):
            return None, None

        AdHocCLI._ask_passwords = mock_ask_passwords


# Generated at 2022-06-12 20:13:24.157770
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    #  Helper method to mock class TaskQueueManager
    def mock_tqm_run(self, play):
        pass

    # Helper method to mock class TaskQueueManager
    def mock_post_process_args(self, options):
        return options

    AdHocCLI._play_ds = mock_play_ds
    AdHocCLI.run = mock_tqm_run
    AdHocCLI.post_process_args = mock_post_process_args

    # Context dict for test
    ctx_dict = dict(module_name='module', module_args='module_args', forks=10, verbosity=3)

# Generated at 2022-06-12 20:13:25.618088
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Does not take any arguments
    cli = AdHocCLI()
    assert cli is not None

# Generated at 2022-06-12 20:13:30.382617
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    Test the method run of class AdHocCLI.
    """

    # Initialize a AdHocCLI object
    adHocCLI = AdHocCLI()

    # Initialize an options object
    class Options(object):
        """
        Declare an options object.
        """
        def __init__(self):
            self.module_name = 'setup'
            self.module_args = 'ansible_ssh_pass=test'
            self.verbosity = 0
            self.check = False
            self.inventory = './tests/unit/mock/ansible/inventory/hosts'

    # Run the method
    adHocCLI.run(Options(), 'localhost')

# Generated at 2022-06-12 20:13:33.654596
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test that invokes the run method of AdHocCLI.
    '''

    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

# Generated at 2022-06-12 20:13:41.052622
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(["255.255.255.0", "-m", "command", "-a", "uptime", "-i", "/path/to/my/hosts", "-e", "key=value", "-T", "60", "--list-hosts"])
    assert adhoc.parser.version == C.ANSIBLE_VERSION
    assert adhoc.options.host_pattern == '255.255.255.0'
    assert adhoc.options.module_name == 'command'
    assert adhoc.options.module_args == 'uptime'
    assert adhoc.options.inventory == '/path/to/my/hosts'
    assert adhoc.options.extra_vars == [['key', 'value']]
    assert adhoc.options.task_timeout == 60
   

# Generated at 2022-06-12 20:13:47.778039
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Construct required objects.
    cli = AdHocCLI()
    cli.options = opt_help.get_empty_options_mock()
    cli.options.connection = 'local'
    cli.options.module_name = 'file'
    cli.options.module_args = 'path=/etc/hosts state=touch'
    cli.options.subset = None
    cli.options.listhosts = None
    cli.options.one_line = False
    cli.options.tree = None
    cli.options.verbosity = 0
    cli.parser = opt_help.get_parser_mock()
    inventory = opt_help.get_inventory_mock()
    loader = opt_help.get_loader_mock()

# Generated at 2022-06-12 20:13:50.662635
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI()
    obj.init_parser()
    opt = obj.post_process_args(context.CLIARGS)
    obj.run()


# Generated at 2022-06-12 20:13:52.517221
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI()
    result = adhoc_cli.run()
    assert result == 0

# Generated at 2022-06-12 20:14:21.572181
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Import mock to test setting-up of the TaskQueueManager
    try:
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock
    from tempfile import mkdtemp
    import shutil
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.cli.adhoc import AdHocCLI
    from ansible.errors import AnsibleOptionsError

    mock_tqm = Mock(name='TaskQueueManager')
    mock_tqm.send_callback.return_value = None

    # Create a context for the test
    # - ansible options set to just include the host pattern
    # - include the module name
    # - include the

# Generated at 2022-06-12 20:14:23.147366
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

# Generated at 2022-06-12 20:14:29.528573
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create CLI object
    a = AdHocCLI([])

    # Create Mock TaskQueueManager
    a._tqm = TaskQueueManager()
    # Create Mock TaskQueueManager._stats
    a._tqm._stats = MockObject()
    # Create loader
    loader = MockObject()
    a._tqm.loader = loader
    # Mock inventory
    inventory = MockObject()
    a._tqm.inventory = inventory
    # Mock Passwords
    passwords = MockObject()
    a._tqm.passwords = passwords
    # Mock callbacks
    a._tqm.callbacks = MockObject()
    # Mock display object
    a._display = display

    # Create ad hoc object
    p = AdHocCLI([])
    # Mock play
    p._play_ds = MockObject()
   

# Generated at 2022-06-12 20:14:38.769957
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    opt = context.CLIARGS

    # Test the method with subset option
    opt['subset'] = True
    opt['listhosts'] = True
    opt['action'] = 'list'
    opt['tree'] = 'tree'
    opt['run_once'] = True
    opt['listtasks'] = True
    opt['listtags'] = True
    opt['syntax'] = True
    opt['ask_vault_pass'] = True
    opt['extra_vars'] = 'extra_vars'
    opt['encrypt'] = 'encrypt'
    opt['vault_password_file'] = './ansible/vault_pass'
    opt['ask_pass'] = True

# Generated at 2022-06-12 20:14:39.318210
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:43.590806
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert isinstance(adhoc_cli, CLI)
    assert adhoc_cli.base_parser is not None
    assert adhoc_cli.parser is not None

# Generated at 2022-06-12 20:14:54.234824
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    # Create the actual AdHocCLI instance
    cli = AdHocCLI(args=['all', '-m', 'debug', '-a', 'msg=hello world'])
    # Create the parser based on the available arguments
    cli.parse()
    # Create the InventoryManager instance
    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,', 'otherserver,'])
    # Create the VariableManager instance
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    # Run the AdHocCLI._play_ds method

# Generated at 2022-06-12 20:14:54.784899
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert True

# Generated at 2022-06-12 20:14:58.924735
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()

    cli.args = ['localhost', '--module-name', 'shell', '--module-args', 'ls']
    cli.parser = cli.create_parser()
    cli.options = cli.post_process_args(cli.parse())
    result = cli.run()
    assert result == 0

# Generated at 2022-06-12 20:15:00.243077
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(['localhost'])
    assert adhoc


# Generated at 2022-06-12 20:15:35.215226
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:37.353040
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    try:
        result = AdHocCLI().run()
        assert result == 0
    except:
        pass

# Generated at 2022-06-12 20:15:40.067315
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad_hoc_cli = AdHocCLI(args=['-h'])
    ad_hoc_cli.run()

# Generated at 2022-06-12 20:15:42.138326
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    #
    # Note: Tests are not currently implemented
    #       This is a stub that will be implemented in a future PR
    #
    pass

# Generated at 2022-06-12 20:15:52.237051
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:15:53.392319
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoccl = AdHocCLI()
    adhoccl.run()

# Generated at 2022-06-12 20:15:53.902021
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:54.772057
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run(AdHocCLI())

# Generated at 2022-06-12 20:15:56.152622
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # AdHocCLI() raises no exception
    AdHocCLI()

# Generated at 2022-06-12 20:16:04.084320
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    c = AdHocCLI()
    c.options = c.options_context()
    c.options.vvv = False
    c.options.connection = 'local'
    c.options.timeout = 10
    c.options.remote_user = 'root'
    c.options.ask_pass = False
    c.options.module_path = None
    c.options.become = False
    c.options.become_method = 'sudo'
    c.options.become_user = 'root'
    c.options.ask_value_pass = False
    c.options.verbosity = 0
    c.options.check = False
    c.options.inventory = './tests/ansible_test/hosts'
    c.options.listhosts = False
    c.options.subset = None
   

# Generated at 2022-06-12 20:17:23.682587
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display
    display = Display()

    # Unit test for constructor of class AdHocCLI
    try:
        AdHocCLI(args=['all', '--listhosts'])
    except AnsibleError as e:
        display.display("AdHocCLI.__init__() Exception '%s' caught" % e.message)

# Generated at 2022-06-12 20:17:25.438762
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    This is an unit test for method 'run' of class AdHocCLI.

    Tests:
        *Pattern is valid,
        *Pattern is empty.
    """
    pass

# Generated at 2022-06-12 20:17:34.847479
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    options = context.CLIARGS
    options['subset'] = 'host-a'
    options['module_name'] = C.DEFAULT_MODULE_NAME
    options['module_args'] = '-a'
    options['listhosts'] = False
    options['pattern'] = 'host-a'
    options['seconds'] = context.CLIARGS['seconds']
    options['poll_interval'] = context.CLIARGS['poll_interval']
    options['module_name'] = C.DEFAULT_MODULE_NAME
    options['one_line'] = False
    options['tree'] = None
    options['forks'] = context.CLIARGS['forks']
    # options['remote_user'] = 'root'
    # options['ask_pass'] = True

    # Create a instance of class

# Generated at 2022-06-12 20:17:43.766217
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    display = Display()
    display.verbosity = 0

    class MockCLI(object):
        # Avoid using the real play_prereqs, which would make a lot of calls
        # to other methods.
        #
        # Here we just need an inventory and a variable manager, so that's all
        # we set up.
        def _play_prereqs(self):
            inventory = FakeInventory()
            variable_manager = FakeVariableManager()
            return None, inventory, variable_manager

        def ask_passwords(self):
            return (None, None)

        # get_host_list is hard to fake, since it calls other methods.  Just
        # have it pretend there are no hosts.
        def get_host_list(self, inventory, subset=None, pattern=None):
            return []


# Generated at 2022-06-12 20:17:54.867779
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Testing run method by passing list of hosts and list of tasks
    # Create an instance of AdHocCLI class
    a = AdHocCLI()
    # Create context object
    context.CLIARGS = {'listhosts': False}
    # Create AnsibleOptionsError instance
    ansible_options_error_instance1 = AnsibleOptionsError('No argument passed to setup module')
    ansible_options_error_instance2 = AnsibleOptionsError("'setup' is not a valid action for ad-hoc commands")
    # Test run by passing list of hosts and list of tasks
    assert a.run() == 0
    # Test run method by passing list of hosts and no tasks
    context.CLIARGS = {'listhosts': False, 'module_name': 'setup'}
    # Test run method by passing list of hosts

# Generated at 2022-06-12 20:18:04.648844
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''Unit test for AdHocCLI.run()'''

    # Stub display.verbosity
    display.verbosity = 0

    # Stub context.CLIARGS

# Generated at 2022-06-12 20:18:05.162142
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:18:05.543183
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
	pass

# Generated at 2022-06-12 20:18:09.073324
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    module_name = 'setup'
    module_args = 'filter=ansible_distribution'
    pattern = 'localhost,'

    cli_args = dict(
        module_name=module_name,
        module_args=module_args,
        args=pattern
    )

    class DummyArgs(object):
        def __init__(self, cli_args):
            for key, value in cli_args.items():
                setattr(self, key, value)

    context.CLIARGS = DummyArgs(cli_args)

    result = AdHocCLI().run()

    assert result == 0

# Generated at 2022-06-12 20:18:10.876936
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()