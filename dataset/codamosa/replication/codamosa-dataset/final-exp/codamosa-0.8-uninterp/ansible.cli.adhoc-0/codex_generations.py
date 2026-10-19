

# Generated at 2022-06-12 20:11:57.072374
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(args=["-m", "module_name"])
    assert isinstance(cli, AdHocCLI)
    assert cli.parser is not None

# Generated at 2022-06-12 20:12:03.888253
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # FIXME - this is not really a unit test and needs to be rewritten
    display.verbosity = 3
    testargs = [
        '-l',
        'target',
        '-m',
        'setup',
        'target',
    ]
    adhoc_cls = AdHocCLI(args=testargs)
    adhoc_cls.parse()
    adhoc_cls.post_process_args()
    adhoc_cls.run()

# Generated at 2022-06-12 20:12:13.324014
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class MockAdHocCLI(AdHocCLI):
        def post_process_args(self, options):
            return options

        def run(self):
            super(MockAdHocCLI, self).run()
            # avoid adding to tasks that don't support it, unless set, then give user an error
            if context.CLIARGS['module_name'] not in C._ACTION_ALL_INCLUDE_ROLE_TASKS and any(frozenset((context.CLIARGS['seconds'], context.CLIARGS['poll_interval']))):
                self.assertEqual(context.CLIARGS['seconds'], context._ansible_async_seconds)

# Generated at 2022-06-12 20:12:21.052412
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # test for run method
    import os
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback.default import CallbackModule
    from ansible.utils.shlex import shlex_split
    from ansible.plugins.callback.tree import CallbackModule as CallbackTree
    from ansible.plugins.callback.default import CallbackModule as CallbackDefault
    from ansible.utils.path import unfrackpath

    # Mock create os module

# Generated at 2022-06-12 20:12:31.831464
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI()
    # test for bad playbook

# Generated at 2022-06-12 20:12:32.556535
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:41.540298
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    conn_pass = None
    become_pass = None
    cli = AdHocCLI([])

# Generated at 2022-06-12 20:12:43.613615
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    adhoccli = AdHocCLI()
    adhoccli._display = Display()
    adhoccli.run()

# Generated at 2022-06-12 20:12:52.423748
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    mock_options = lambda **kwargs: type('Options', (), kwargs)
    cli = AdHocCLI()
    cli.parser = object()
    cli.options = mock_options()
    cli.args = ''
    cli.rbu = object()
    cli.callback = object()
    cli._play_ds = lambda x, y, z: object()
    cli._playbook = Playbook()
    cli._tqm = object()
    cli.inventory = Inventory()
    cli.variable_manager = VariableManager()
    cli.loader = object()
    cli.load()
    cli.run()

# Generated at 2022-06-12 20:13:01.235314
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    import ansible.config.manager
    from ansible.playbook.play import Play

    ADHOC = AdHocCLI(None)
    ADHOC.setup()
    # create an options parser for bin/ansible
    ADHOC.init_parser()
    options = ADHOC.post_process_args(ADHOC.parse())

    # change the value of options
    options.connection = 'local'
    options.forks = 1
    options.tree = '/tmp/adhoc_test'
    options.verbosity = 3
    options.module_name = 'shell'
    options.module_args = 'ls'
    options.args = 'all'
    options.one_line = True
    # create objects required to execute tasks in adhoc
    (loader, inventory, variable_manager)

# Generated at 2022-06-12 20:13:17.356530
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoccli = AdHocCLI()
    cliargs = dict(
        module_name='shell',
        module_args='ls',
        args='all'
    )
    context.CLIARGS = cliargs
    with pytest.raises(AnsibleOptionsError) as err:
        adhoccli.run()
    assert "No argument passed to shell module" in str(err)

# Generated at 2022-06-12 20:13:24.732502
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.adhoc import AdHocCLI

    # define test cases

# Generated at 2022-06-12 20:13:37.725677
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    import sys
    import mock
    import __builtin__
    from ansible.errors import AnsibleError
    from ansible import constants as C
    from ansible.cli import CLI
    from ansible.cli.adhoc import AdHocCLI
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.plugins.callback.default import CallbackModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars

# Generated at 2022-06-12 20:13:38.485890
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:13:42.934832
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test to check that a task queue manager is created
    # and run method is called
    ad = AdHocCLI(None)
    with mock.patch('ansible.executor.task_queue_manager.TaskQueueManager') as m_tqm:
        ad.run()
        assert m_tqm.call_count == 1
        assert m_tqm.run.call_count == 1

# Generated at 2022-06-12 20:13:44.798529
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI(args=['-a', 'test ping', 'test'])
    adhoc.post_process_args()
    adhoc.run()

# Generated at 2022-06-12 20:13:46.932565
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI(args=['-m', 'ping', 'localhost'])
    assert adhoc.run() == 0

# Generated at 2022-06-12 20:13:51.857483
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    with pytest.raises(AnsibleOptionsError):
        adhoc = AdHocCLI()
        playbook = dict(
            name="Ansible Ad-Hoc",
            hosts=pattern,
            gather_facts='no',
            tasks=[mytask])
        assert adhoc.run(pattern, async_val, poll) == playbook

# Generated at 2022-06-12 20:13:56.400969
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # Create a AdHocCLI object
    adhoc_cli_obj = AdHocCLI(command=set())

    # Create a dict and assign any key, value pairs to it

# Generated at 2022-06-12 20:14:00.805324
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Creating a AdHocCLI object with required arguments
    cli = AdHocCLI(args=['all'])
    cli.post_process_args()
    # testing the run method to test if it returns 0
    assert cli.run() == 0

# Generated at 2022-06-12 20:14:21.502613
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    sys.modules['ansible.module_utils.six'].moves.input = lambda x: 'secret'
    c = AdHocCLI(args=['localhost', '-m', 'ping'])
    c.parse()
    c.run()

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:14:31.462873
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test AdHocCLI.run() with error (No argument passed to module)
    module_name = C.DEFAULT_MODULE_NAME
    module_args = C.DEFAULT_MODULE_ARGS
    method = AdHocCLI()
    with pytest.raises(AnsibleOptionsError) as err:
        method.run()
    assert err.value.args[0] == "No argument passed to %s module" %module_name

    # Test AdHocCLI.run() with error (No hosts matched, nothing to do)
    module_args = "test"
    pattern = "subset"
    method = AdHocCLI()
    with pytest.raises(AnsibleOptionsError) as err:
        method.run()

# Generated at 2022-06-12 20:14:32.458336
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:37.940422
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    test_AdHocCLI = AdHocCLI()
    options = test_AdHocCLI.parser.parse_args(args=['all', '-m', 'command', '-a', 'ls', '-vvvvv'])
    context.CLIARGS = vars(options)
    test_AdHocCLI.run()

# Generated at 2022-06-12 20:14:40.877783
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    parser = opt_help.get_base_parser()
    options = parser.parse_args(['host'])
    cli = AdHocCLI(parser)
    cli.options = options
    cli.run()

# Generated at 2022-06-12 20:14:45.753787
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI(args=[])

    assert obj._play_ds(pattern='', async_val=None, poll=None) == dict(
        name="Ansible Ad-Hoc",
        hosts="",
        gather_facts='no',
        tasks=[])



# Generated at 2022-06-12 20:14:56.763031
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.arguments import option_helpers as opt_help
    import ansible.constants as C

    cli = AdHocCLI([])

    # post_process_args() test
    class TestOpt(opt_help.BaseOptions):
        pass

    TestOpt.__dict__.update(C.CLI_OPTIONS)
    options = TestOpt()

    # patch options value
    options.check = True
    options.verbosity = 0
    options.inventory = ["./test/test_ad_hoc_inventory"]
    options.module_name = "ping"
    options.module_args = ""
    options.args = "test_host"
    options.connection = "local"
    options.forks = 10
    options.timeout = 10
    options.listhosts = False


# Generated at 2022-06-12 20:15:05.553786
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    import unittest
    import ansible.utils.display

    from ansible_mock import patch
    from ansible.cli.adhoc import AdHocCLI

    class AnsibleAdHocCLITest(unittest.TestCase):
        def setUp(self):
            self.orig_stdout = ansible.utils.display.Display().nomirror
            self.orig_no_log = ansible.utils.display.Display().no_log
            ansible.utils.display.Display().nomirror = True
            ansible.utils.display.Display().no_log = True

        def tearDown(self):
            ansible.utils.display.Display().nomirror = self.orig_stdout
            ansible.utils.display.Display().no_log = self.orig_no_log


# Generated at 2022-06-12 20:15:17.359700
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import argparse
    from ansible.errors import AnsibleOptionsError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.plugins.callback.default import CallbackModule
    import sys


    # Mock Parser class
    class Parser:
        args = []
        def __init__(self):
            self.args = sys.argv

    # Mock loader class
    class MyLoader:
        pass

    # Mock PlaybookExecutor class
    class MyPlaybookExecutor:
        pass

    # Mock Display class
    class MyDisplay:
        def __init__(self, verbosity):
            self.verbosity = verbosity

    # Mock TaskQueueManager class

# Generated at 2022-06-12 20:15:22.162849
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    module_args = 'ansible_network_os=ios device_type=ios commands="show version"'
    module_name = 'napalm_cli'
    args = 'localhsot'
    cliargs = dict(
        forks=2,
        module_name=module_name,
        module_args=module_args,
    )

    test_Ahd = AdHocCLI(args, **cliargs)

    # Test is not complete, as TaskQueueManager can't be mocked, yet
    assert test_Ahd.run() == 0



# Generated at 2022-06-12 20:16:06.821204
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # run is a method of class AdHocCLI and so we need to create a class object
    test_obj = AdHocCLI()

    # Since run method is returning an integer value, we use assertEqual to unit test it
    assertEqual(test_obj.run(), 0)

# Generated at 2022-06-12 20:16:15.559543
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import unittest
    import ansible.config.manager
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.inventory.manager
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.inventory.host
    import ansible.playbook.playbook
    import ansible.context
    import ansible.errors
    import ansible.executor.task_queue_manager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from io import StringIO
    from ansible.cli import CLI
    from ansible.cli.adhoc import AdHocCLI
    from .test__utils import *

    # pylint: disable=too-few

# Generated at 2022-06-12 20:16:16.807753
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    my = AdHocCLI(args=['-m', 'setup', 'all'])
    my.run()

# Generated at 2022-06-12 20:16:18.303293
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Creating an object of class AdHocCLI
    obj = AdHocCLI()

# Generated at 2022-06-12 20:16:22.934812
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    #setup()
    adhoc_cli = AdHocCLI()
    adhoc_cli.setup()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        adhoc_cli.run()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

# Generated at 2022-06-12 20:16:23.531063
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:26.167866
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    adhoc.parse()
    adhoc.post_process_args(adhoc.options)
    adhoc.run()

# Generated at 2022-06-12 20:16:27.383081
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert False, "Unit test for AdHocCLI method run not implemented"

# Generated at 2022-06-12 20:16:29.539630
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI(['-m', 'file', '-a', 'path=/etc/hosts', 'host'])
    assert obj.parser._actions[2].dest == 'module_args'
    assert obj.parser._actions[3].dest == 'module_name'


# Generated at 2022-06-12 20:16:32.885058
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
  """
  Unit test for constructor of class AdHocCLI
  """
  cli = AdHocCLI()
  assert cli.parser

# Generated at 2022-06-12 20:18:00.331150
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:18:06.984377
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Unit test for method run of class AdHocCLI"""

    # Test 1:
    # Test the function with following values
    # 1. pattern = 'sample'
    # 2. async_val = '0'
    # 3. poll = '0'
    # Test 1 asserts:
    # 1. Run the function with above values.
    # Test 1 should not return any error.

    pattern = 'sample'
    async_val = 0
    poll = 0

    # Call _play_ds function and pass the above values
    play_ds = AdHocCLI()._play_ds(pattern, async_val, poll)

    assert (play_ds != None)



# Generated at 2022-06-12 20:18:13.063621
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play

    loader = DataLoader()
    options = context.CLIARGS
    inventory = InventoryManager(loader=loader, sources=options['inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # get basic objects
    loader, inventory, variable_manager = PlaybookExecutor._load_playbook_from_file("test_data/adhoc_playbook.yml", loader, inventory, variable_manager)

# Generated at 2022-06-12 20:18:19.274464
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.init_parser()
    cli_options = cli.parser.parse_args(['all', '-m', 'setup'])
    cli_extras = cli.post_process_args(cli_options)
    from ansible.cli.adhoc import AdHocCLI
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:18:20.244696
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:18:22.661019
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI(['localhost'],['-m', 'ping'])
    test_run = adhoc_cli.run()
    assert test_run == 0

# Generated at 2022-06-12 20:18:32.808038
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # inputs
    options = opt_help.add_runtask_options(None)
    options = opt_help.add_module_options(options)
    options = opt_help.add_async_options(options)
    options = opt_help.add_check_options(options)
    options = opt_help.add_runas_options(options)
    options = opt_help.add_connect_options(options)
    options = opt_help.add_output_options(options)
    options = opt_help.add_fork_options(options)
    options = opt_help.add_inventory_options(options)
    options = opt_help.add_vault_options(options)
    options = opt_help.add_tasknoplay_options(options)
    options = opt_help.add_basedir

# Generated at 2022-06-12 20:18:33.455157
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.init_parser()

# Generated at 2022-06-12 20:18:34.498973
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    CLI.args = 'localhost -m ping'
    AdHocCLI()

# Generated at 2022-06-12 20:18:39.235167
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    hostpattern = 'localhost'

    # Ad-hoc requires the user's password, the user's become password, the user's vault password and the list of hosts
    # We mock the CLI to behave in the same way as the Command Line Interface
    mock = Mock()
    mock.ask_passwords.return_value = False, False
    mock.get_host_list.return_value = ['localhost']

    # We create an AdHocCLI
    adhoccli = AdHocCLI(mock)

    # We execute the run method
    adhoccli.run()