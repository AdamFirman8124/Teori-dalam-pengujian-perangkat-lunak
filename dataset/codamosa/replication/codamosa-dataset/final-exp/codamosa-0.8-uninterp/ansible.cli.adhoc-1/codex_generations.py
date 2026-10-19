

# Generated at 2022-06-12 20:11:53.163322
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class Mock_CLI(AdHocCLI):
        def __init__(self):
            self.options = context.CLIARGS
            self.option_parser = 'option_parser'
            self.args = ['192.168.0.1']

        def ask_vault_passwords(self):
            return
        def ask_passwords(self):
            return ('sshpass', 'becomepass')

        def get_host_list(self, inventory, subset, pattern):
            return [inventory]

        def _play_prereqs(self):
            return ('loader', 'inventory', 'variable_manager')

    mock_cli = Mock_CLI()

# Generated at 2022-06-12 20:12:00.729872
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import pytest
    from ansible.cli.adhoc import AdHocCLI

    # ad_hoc = AdHocCLI(args)
    ad_hoc = AdHocCLI()
    with pytest.raises(AnsibleOptionsError) as e:
        ad_hoc.run()

    # ad_hoc = AdHocCLI(args)
    ad_hoc = AdHocCLI(None)
    with pytest.raises(AnsibleOptionsError) as e:
        ad_hoc.run()

# Generated at 2022-06-12 20:12:01.322266
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:03.107408
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Test AdHocCLI class."""
    pass

# Generated at 2022-06-12 20:12:05.420821
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert isinstance(adhoc_cli, AdHocCLI)


# Generated at 2022-06-12 20:12:14.415517
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from mock import patch

    # Retrieve class and object
    from ansible.cli.adhoc import AdHocCLI
    adhoc_cli = AdHocCLI()

    # Monkeypatching
    with patch.multiple(C, DEFAULT_MODULE_ARGS='module_args', DEFAULT_MODULE_NAME='module_name', MODULE_REQUIRE_ARGS='module_name') as mock_values:
        mock_values['TREE_DIR'] = 'tree_dir'
        mock_values['CALLBACKS_ENABLED'] = ['tree']


# Generated at 2022-06-12 20:12:21.238079
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class FakeAdHocCLI(AdHocCLI):
        def get_host_list(self, inventory, subset, pattern):
            return [host.name for host in inventory.hosts]

        def ask_passwords(self):
            return (None, None)

        def _play_prereqs(self):
            return (None, None, None)

    class FakeContext():
        CLIARGS = {}

    context.CLIARGS = FakeContext().CLIARGS
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['one_line'] = False
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['ask_pass'] = False
    context.CLIARGS['ask_become_pass'] = False
    context.CLI

# Generated at 2022-06-12 20:12:32.042546
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test args
    pattern = "localhost"
    async_val = 1
    poll = 1
    sshpass = "sshpass"
    becomepass = "becomepass"
    passwords = {'conn_pass': sshpass, 'become_pass': becomepass}
    display.verbosity = 4
    context.CLIARGS = {'module_name': 'shell',
                        'module_args': 'echo -e "Hello World"',
                        'subset': False,
                        'listhosts': False,
                        'seconds': async_val,
                        'poll_interval': poll,
                        'tree': False,
                        'one_line': True,
                        'forks': 100}


# Generated at 2022-06-12 20:12:41.264574
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    Test if AdHocCLI method run will create, execute and remove task queue manager
    """
    adhoccli = AdHocCLI()

    # Mock objects
    class ModuleArgs:
        module_name = 'test_name'
        module_args = 'test_args'

    class MockCLIARGS:
        """
        Mocked CLIARGS
        """
        def __init__(self):
            self.verbosity = 1
            self.ask_pass = True
            self.module_name = 'test_name'
            self.module_args = module_args = 'test_args'
            self.args = 'test_arg'
            self.subset = 'test_subset'
            self.listhosts = False
            self.seconds = 1
            self.poll_interval = 2

# Generated at 2022-06-12 20:12:43.917284
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' unit test for Ansible-cli AdHocCLI'''
    ad_hoc_cli = AdHocCLI()
    assert isinstance(ad_hoc_cli, CLI)
    assert isinstance(ad_hoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:12:53.864821
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.help import HelpCLI

    context._init_global_context(['ansible-adhoc'])

    args = ['localhost', '-i', '/dev/null', '-m', 'setup']

    runner = AdHocCLI(args)
    assert runner.run() == 2



# Generated at 2022-06-12 20:13:02.611759
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

	# test using both sample modules
	module_name = 'ping'
	module_name_fail = 'sample'

	# test using both ping and sample modules
	# test using both ping and sample modules
	module_args = '"data=Success"'
	module_args_fail = '"data=Fail"'

	# test using both valid and invalid host pattern
	pattern = 'localhost'
	pattern_fail = 'abcd'

	# test using empty connection password and invalid connection password
	conn_pass = ''
	conn_pass_fail = 'abcd'

	# test using empty become password and invalid become password
	become_pass = ''
	become_pass_fail = 'abcd'

	# test using both valid and invalid verbosity
	verbosity = '0'
	verbosity_fail = '3'

	# test using

# Generated at 2022-06-12 20:13:07.193194
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    #
    # Unit test for method run of class AdHocCLI
    #
    # TODO : update to take in a Mock for the full test
    # TODO : create Ansible options to run with a playbook that has a run
    # TODO : test if context.CLIARGS['args']

    #
    # Older test that only tests that method doesn't crash
    #
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:13:09.794065
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # test for invalid host pattern
    context.CLIARGS = {'args': '/path/to/file'}
    cli = AdHocCLI(args=[])
    # AdHocCLI.run() has no return
    assert cli.run() is None


# Generated at 2022-06-12 20:13:10.452258
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()

# Generated at 2022-06-12 20:13:17.387735
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.inventory.manager import InventoryManager

    # Using real data from the 'test' folder
    test_playbook = '''
    - hosts: localhost
      gather_facts: no
      tasks:
        - shell: "echo -n '{{ item }}: ' && echo '1' > /tmp/{{ item }}-test"
          with_items:
            - item1
            - item2
            - item3
    '''
    tmpfile = open('./testfile', 'w')
    tmpfile.write(test_playbook)
    tmpfile.close()

    # creating mock class and objects
    # creating mock class and objects
    mock_display = Display()
    mock_display.debug = True
    mock_display.verbosity = 4

    mock_inventory = InventoryManager()

# Generated at 2022-06-12 20:13:24.763018
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' unit test for constructor of class AdHocCLI '''

    # pylint: disable=redefined-variable-type
    # pylint: disable=too-many-function-args
    # pylint: disable=protected-access

    _ = AdHocCLI(['-c', 'local', '-m', 'setup', 'localhost'])  # execute without failure


if __name__ == '__main__':
    # pylint: disable=invalid-name
    import __main__
    main = getattr(__main__, '__file__', None) or __main__.__doc__
    if main is None or main.startswith(('-', '.')):
        # support "python -m ansible ... or python ansible ..."
        main = sys.argv[0]
    cl

# Generated at 2022-06-12 20:13:27.149723
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:27.784500
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:13:38.318534
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    from ansible.cli.adhoc import AdHocCLI
    from ansible.errors import AnsibleOptionsError
    from io import StringIO
    from ansible.utils.vars import combine_vars

    test_stdout = StringIO()
    display.verbosity = 3
    display.DeprecationWarning = lambda *a, **k: None
    display.display = lambda *a, **k: None
    display.display = test_stdout.write
    display._display = lambda *a, **k: None
    display._display = lambda *a, **k: None
    # Avoid to output log to sys.stdout when test
    logging = module_loader.get_single_instance_class('logging')

# Generated at 2022-06-12 20:13:58.959165
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # Test with no argument
    # AdHocCLI()

    # Test with valid arguments
    AdHocCLI(['-a', 'pip install ansible'])
    AdHocCLI(['-a', 'pip install ansible', '-m', 'apt', '-A', '--ask-vault-pass', '--ask-pass', '--ask-su-pass', '--ask-sudo-pass', '--flush-cache', '--force-handlers', '--list-hosts', '--list-tags'])
    AdHocCLI(['-m', 'apt', '-a', 'pip install ansible', '-C', '-D', '--diff', '--extra-vars'])

# Generated at 2022-06-12 20:13:59.945331
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI([])
    assert cli.parser.description

# Generated at 2022-06-12 20:14:08.279700
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' AdHocCLI.__init__() unittest '''

    # Create a instance of class AdHocCLI
    adhoc_cli = AdHocCLI()
    assert adhoc_cli

if __name__ == "__main__":
    import unittest
    test_cases = (
        test_AdHocCLI,
    )
    suite = unittest.TestSuite(map(unittest.FunctionTestCase, test_cases))
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-12 20:14:15.005568
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from io import StringIO
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.cli.adhoc import AdHocCLI
    import ansible.constants as C

    cli = AdHocCLI([])
    cli.parser = cli.create_parser()
    if not hasattr(cli, '_play_prereqs'):
        cli._play_prereqs = lambda: (None, None, None)
    if not hasattr(cli, 'get_host_list'):
        cli.get_host_list = lambda i, o, p: ['localhost']
    cli.ask_passwords = lambda: (None, None)

    context.CLIARGS = cli.parse()[0]
    context.CL

# Generated at 2022-06-12 20:14:16.823849
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli._tqm is None

# Generated at 2022-06-12 20:14:26.299436
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class MockInventory(object):
        def __init__(self, *args,**kwargs):
            pass

    class MockVariableManager(object):
        def __init__(self, *args,**kwargs):
            pass

    class MockLoader(object):
        def __init__(self, *args,**kwargs):
            pass

    class MockTQM(TaskQueueManager):
        def __init__(self, *args,**kwargs):
            pass
        
        def run(self, play):
            return 0

    class MockPlaybook(Playbook):
        def __init__(self, *args,**kwargs):
            pass

    class MockPlay(Play):
        def __init__(self, *args,**kwargs):
            pass


    import sys

# Generated at 2022-06-12 20:14:28.141439
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli is not None


# Generated at 2022-06-12 20:14:37.447809
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='localhost,')
    variable_manager.set_inventory(inventory)

    pattern = 'localhost'

    cli = AdHocCLI(args=[])
    cli.parser = cli.create_parser()
    cli.options, cli.args = cli.parser.parse_known_args()
    cli.post_process_args(cli.options)

    play_ds = cli._play_ds(pattern, cli.seconds, cli.poll_interval)
    play = Play

# Generated at 2022-06-12 20:14:45.564096
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """ run tests on AdHocCLI() class constructor """

    # instantiate AdHocCLI
    adhoc = AdHocCLI()

    # test run with defaults
    adhoc.run()

    # test run with extra module_name
    context.CLIARGS['module_name'] = 'ping'
    adhoc.run()

    # test run with module_name
    context.CLIARGS['module_name'] = 'ping'
    adhoc.run()

    # test run with module_name and module_args
    context.CLIARGS['module_name'] = 'ping'
    context.CLIARGS['module_args'] = '-c 1'
    adhoc.run()

if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:14:46.915421
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:15:16.046716
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # Provide mock of super class to avoid calling of parent constructor
    # that notifies about invocation of CLI
    class MockCLI(object):
        def __init__(self):
            self.__name = 'MockCLI'

        @property
        def name(self):
            return self.__name

    AdHocCLI(MockCLI())

# Generated at 2022-06-12 20:15:22.731734
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # mock existing objects
    for i in ('os', 'sys'):
        setattr(AdHocCLI, '_'+i, mock.MagicMock())
    AdHocCLI._sys.argv = ['ansible-playbook', 'test.yml']
    with mock.patch.object(PlaybookCLI, '_play_prereqs'):
        setattr(AdHocCLI, '_pattern', 'all')
        setattr(AdHocCLI, '_options', {'one_line': ['True']})
        with mock.patch.object(Display, 'display', return_value=None):
            # mock tqm
            mock_tqm = mock.MagicMock()
            AdHocCLI._tqm = mock_tqm

# Generated at 2022-06-12 20:15:24.498076
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    construct_test = AdHocCLI()
    construct_test.init_parser()
    assert construct_test

# Generated at 2022-06-12 20:15:25.577341
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    command = AdHocCLI()
    command.run()

# Generated at 2022-06-12 20:15:27.550230
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    print('Testing method run of class AdHocCLI')
    print('Not yet implemented')


# Generated at 2022-06-12 20:15:39.572582
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Dummy ansible-playbook execution
    # Check for 'stdout_callback'
    if C.DEFAULT_STDOUT_CALLBACK != 'default':
        stdout_callback_value = C.DEFAULT_STDOUT_CALLBACK
    else:
        stdout_callback_value = 'minimal'

    # Test-1
    # Test for ansible-playbook execution with '-i' and '-m'

# Generated at 2022-06-12 20:15:46.902975
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    import sys
    import os
    import json
    import tempfile

    # Prepare for test
    sys.argv = [sys.argv[0], 'localhost',
                '-c', 'local',
                '-m', 'command',
                '-a', 'id',
                '-v']
    sys.stdout = tempfile.TemporaryFile('w+')

    # Execute test
    AdHocCLI().run()

    # Restore environment
    sys.argv = [sys.argv[0]]
    sys.stdout.seek(0)
    output = sys.stdout.read()
    sys.stdout = sys.__stdout__

    # Test
    assert(len(output) > 0)


# Generated at 2022-06-12 20:15:53.550858
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    options = opt_help.read_cli_vals()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, options.host_list)
    variable_manager.set_inventory(inventory)
    option = opt_help.parse_cli_args()
    adhoc_cli = AdHocCLI(option)
    adhoc_cli.run()

# Generated at 2022-06-12 20:15:54.643309
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad_hoc = AdHocCLI()
    assert ad_hoc.parser



# Generated at 2022-06-12 20:15:56.305215
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert isinstance(adhoc, AdHocCLI)

# Generated at 2022-06-12 20:17:10.290772
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.module_utils.facts import inject_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactModule
    facts = inject_facts(dict(), DistributionFactModule())

    # Script location: lib/ansible/cli/adhoc.py
    # Arguments to the script

# Generated at 2022-06-12 20:17:17.999660
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test values
    command = ['--module-name', 'setup', 'localhost', '-m', 'shell', '-a', 'ls /tmp', '--listhosts']

    # Run test
    print("\nTest command: %s\n" % command)
    a = AdHocCLI(command)
    results = a.run()

    # Verify argument usage -- expected: 0
    if not results == 0:
        raise AssertionError("Argument usage not 0: %s" % results)

    print("\nBasic test passed\n")

# Generated at 2022-06-12 20:17:19.323668
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    raise AnsibleError(msg='not implemented')

# Generated at 2022-06-12 20:17:26.957561
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class FakeInventory(object):
        def __init__(self, hosts):
            self.hosts = hosts

        def get_hosts(self, pattern=None, ignore_rest=False, ignore_errors=False):
            return self.hosts

    class FakeVariableManager(object):
        def __init__(self, loader):
            pass

    class FakeLoader(object):
        def __init__(self):
            pass

    class FakeOptions(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class FakeDisplay(object):
        def __init__(self):
            self.verbosity = 1
            self.display_results = []

        def display(self, result):
            self.display_results.append(result)


# Generated at 2022-06-12 20:17:37.265862
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    def run_module(host, module_name, module_args):
        print(host)
        print(module_name)
        print(module_args)

        return (dict(invocation=dict(module_name=module_name, module_args=module_args),
                     result=dict(rc=0, changed=False, stderr="", stdout="")))


# Generated at 2022-06-12 20:17:38.536981
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:17:46.133218
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    def fake_playbook_on_stats(stats):
        fake_playbook_on_stats.stats = stats


# Generated at 2022-06-12 20:17:56.274428
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Creating an object of class AdHocCLI
    adhoc_cli = AdHocCLI()

    # creating object of class CLIARGOBJ
    cliargs = opt_help.CLIARGOBJ()
    cliargs.forks = 2
    cliargs.module_name = 'ping'
    cliargs.module_args = 'user=ansible'
    cliargs.subset = None
    cliargs.tree = None
    cliargs.listhosts = True
    cliargs.inventory = '/etc/ansible/hosts'

    # calling method post_process_args of class AdHocCLI
    adhoc_cli.post_process_args(cliargs)

    connect_options = opt_help.CLIARGOBJ()
    # calling method get_

# Generated at 2022-06-12 20:18:00.733489
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    pass
#     options = ['-m', 'ping', 'localhost']
#     options.insert(0, 'ansible')
#     adhoc = AdHocCLI(args=options)
#     adhoc.run()

# Generated at 2022-06-12 20:18:01.940299
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:21:35.265195
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    from ansible.module_utils.facts import is_local
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from io import StringIO

    # FIXME: load_callback_plugin is broken
    constants_bin_ansible_callbacks = C.DEFAULT_LOAD_CALLBACK_PLUGINS
    C.DEFAULT_LOAD_CALLBACK_PLUGINS = False

    # FIXME: stdout_callback = oneline is broken
    constants_stdout_callback = C.DEFAULT_STDOUT_CALLBACK
    C.DEFAULT_STDOUT_CALLBACK = 'default'

    cli = AdHocCLI(None)

    cli.option_parser = cli.init_parser()
