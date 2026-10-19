

# Generated at 2022-06-12 20:32:49.295147
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:32:49.846683
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:51.395133
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Test run method of class PlaybookCLI"""
    # TODO: Mocking
    pass

# Generated at 2022-06-12 20:32:58.711741
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    with open('test_PlaybookCLI_run.json', 'r') as fd_run:
        # NOTE: if you change this test, also change it in test/units/plugins/cli/test_cli.py
        test_data_run = json.load(fd_run)
        test_data_run = test_data_run['test_PlaybookCLI_run']

    for test in test_data_run:

        # set up testing environment
        test_ansible_args = test['argv']
        if test['execution_path']:
            test_execution_path = test['execution_path']
        else:
            test_execution_path = 'test/test_data/test_ansible_cli_data'

# Generated at 2022-06-12 20:33:07.559054
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbcli = PlaybookCLI()

# Generated at 2022-06-12 20:33:13.380067
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.module_utils._text import to_bytes
    from ansible import context
    import os
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()


# Generated at 2022-06-12 20:33:20.936600
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # if we run into keyboard interrupts, just ignore them
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)

    from ansible.cli.adhoc import AdHocCLI
    cli = AdHocCLI([])
    cli.run()

    from ansible.cli.command import CommandCLI
    cli = CommandCLI([])
    cli.run()

    from ansible.cli.galaxy import GalaxyCLI
    cli = GalaxyCLI([])
    cli.run()

    from ansible.cli.pull import PullCLI
    cli = Pull

# Generated at 2022-06-12 20:33:26.891738
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # An example of a playbook path
    playbook_path = '/foo/bar/ansible/test/integration/test_playbook.yml'
    # An example of an ansible.cfg path
    ansible_cfg_path = '/foo/bar/ansible/test/integration/ansible.cfg'

    # Create an instance of the CLI class
    cli = PlaybookCLI([])
    # Create an instance of the PlaybookCLI class
    playbook_cli = PlaybookCLI([])
    # Call the post_process_args method of the CLI class
    cli.post_process_args({'playbooks': playbook_path, 'ansible_config': ansible_cfg_path})
    # Set the verbosity of the display object
    display.verbosity = 0
    # Call the run method of the PlaybookCLI

# Generated at 2022-06-12 20:33:28.280114
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Dummy method to test run method of class PlaybookCLI
    pass

# Generated at 2022-06-12 20:33:32.792682
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO:
    pass

if __name__ == '__main__':

    try:
        cli = PlaybookCLI(None)
        cli._run()
    except Exception as e:
        display.error(to_text(e))
        sys.exit(1)

# Generated at 2022-06-12 20:33:52.748817
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test case for method run of class PlaybookCLI

    """
    import unittest
    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from io import StringIO
    from unittest.mock import patch

    display = Display()

# Generated at 2022-06-12 20:33:53.987614
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: Write a unit test for this method
    pass

# Generated at 2022-06-12 20:33:56.949071
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # used to supress tracebacks for failing tests
    try:
        pb = PlaybookCLI(args=[])

        pb.run()
    except Exception as e:
        raise AssertionError("Unexpected failure: " + str(e))

# Generated at 2022-06-12 20:34:05.975272
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from ansible.playbook.play import Play

    import os
    import sys
    import socket
    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    from ansible.cli.arguments import option_helpers as opt_help
    import ansible.context
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.display import Display

# Generated at 2022-06-12 20:34:11.959000
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    inv = inventory.Inventory()
    variable_manager = variable_manager.VariableManager()
    variable_manager.extra_vars['inventory_hostname'] = 'localhost'
    variable_manager.extra_vars['inventory_hostname_short'] = 'localhost'
    pbex = PlaybookExecutor(playbooks=['/path/to/playbooks'],
                            inventory=inv,
                            variable_manager=variable_manager)

    assert pbex.run() == 0

# Generated at 2022-06-12 20:34:18.516946
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import unittest

    class TestPlaybookCLI(unittest.TestCase):
        def test_result(self):
            import unittest.mock
            from ansible.utils.display import Display
            display = Display()
            args = context.CLIARGS

            args['args'] = []
            args['listhosts'] = True
            args['listtasks'] = True
            args['listtags'] = True
            args['syntax'] = True
            args['flush_cache'] = True
            args['subset'] = False
            args['connection'] = 'smart'
            args['timeout'] = 10
            args['private_key_file'] = None
            args['ssh_common_args'] = None
            args['ssh_extra_args'] = None
            args['sftp_extra_args'] = None

# Generated at 2022-06-12 20:34:30.721844
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from __main__ import get_main_parser
    from ansible.plugins.loader import add_all_plugin_dirs
    import sys

    test_vars = {
        'my_var': 'value',
        'my_host': 'my_hostname',
        'my_fact': 'amazing',
    }

    # Reset CLI options
    CLI.options = None

    # Test PlaybookCLI class
    pb_cli = PlaybookCLI([])
    options, display = pb_cli.parse()
    assert(options.listhosts is False)
    assert(options.syntax is False)
    assert(options.listtasks is False)
    assert(options.listtags is False)
    assert(options.step is False)
    assert(options.start_at_task is None)

    p

# Generated at 2022-06-12 20:34:41.290594
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    return_val=[]
    class PlaybookExecutorStub:
        def __init__(self, *args, **kwargs):
            return_val.append(None)

        def run(self):
            return [{'playbook': 'playbook.yml', 'plays': [{'hosts': 'host1', 'name': 'play1', 'tags': ['tag1']},
                                                           {'hosts': 'host2', 'name': 'play2', 'tags': ['tag2']},
                                                           {'hosts': 'host3', 'name': 'play3', 'tags': ['tag3']}]}]

    class Options:
        def __init__(self):
            self.verbosity = 0
            self.flush_cache = False
            self.listhosts = True
            self.listt

# Generated at 2022-06-12 20:34:41.770321
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:50.573384
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options:
        flush_cache = True
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        subset = False
        diff = False
        start_at_task = False
        step = False
        verbosity = False
        check = False
        inventory = ['localhost,']
        vault_password_file = False
        forks = 5
    playbook_cli = PlaybookCLI()
    playbook_cli.options = Options()
    playbook_cli.run()

# Generated at 2022-06-12 20:35:06.544765
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = {
        'flush_cache': False,
        'listhosts': False,
        'listtags': False,
        'listtasks': False,
        'syntax': False,
        'step': False,
        'start_at_task': None,
        'verbosity': 0,
        'args': ["playbook.yml"],
        }
    ansible_cmd = PlaybookCLI(args)
    ansible_cmd.run()

# Generated at 2022-06-12 20:35:15.248396
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import getpass

# Generated at 2022-06-12 20:35:26.261425
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options(object):
        verbosity = 0

    class CLIArgs(object):
        connection = 'ssh'
        forks = 5
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False
        inventory = None
        subset = None
        module_path = None
        listhosts = None
        listtasks = None
        listtags = False
        syntax = False
        step = None
        start_at_task = None
        args = None
        flush_cache = None
        extra_vars = []

    pbcli = PlaybookCLI()
    pbcli.options = Options()
    pbcli.options.connection = 'ssh'
    pbcli.options.forks = 5
    pbcli.options.check = False
    pbcli

# Generated at 2022-06-12 20:35:27.336597
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbcli = PlaybookCLI()
    pbcli.test()

# Generated at 2022-06-12 20:35:28.323754
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:35:37.341607
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import unittest
    import sys
    from ansible.executor import tasks
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    # Monkey patch unfrackpath to make it noop for allowing test to work on any system
    old_unfrackpath_noop = tasks.unfrackpath
    tasks.unfrackpath = mock_unfrackpath_noop


# Generated at 2022-06-12 20:35:38.645805
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cls = PlaybookCLI(args=[])
    cls.run()

# Generated at 2022-06-12 20:35:39.402940
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:39.952354
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:41.621783
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbc = PlaybookCLI()
    options = pbc.parse()
    pbc.run()

# Generated at 2022-06-12 20:36:17.943451
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import callback_loader

    playbook = Play()
    task = Task()
    task.action = 'setup'
    playbook._tasks = [task]
    pbcli = PlaybookCLI()
    pbcli.parser = CLI.base_parser(
        usage="%prog [options]",
        connect_opts=True,
        meta_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        runtask_opts=True,
        vault_opts=True,
        fork_opts=True,
        module_opts=False,
        desc=pbcli.__doc__)
   

# Generated at 2022-06-12 20:36:28.317005
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # The following are defined as global to assist in the mocking of the CLI class
    global display
    global CLI

    # We will be checking the results of the ansible-playbook --flush-cache command
    # The following is the expected result:
    # PLAY [all] (TASK)
    expected_result = 'PLAY [all]\n'

    # We will grab the output from the display by running the method
    # 'run' from the PlaybookCLI class.  We will test that the defined playbook
    # was properly run.
    # Note: The 'flush_cache' feature was added in Ansible 2.0, where 'run' was
    # referenced as '_run'.  We used '_run' instead of 'run' to make
    # the test flexible between versions of Ansible.

    # Loading the Ansible PlaybookExecutor Class

# Generated at 2022-06-12 20:36:40.832012
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Setup a mock options object
    class Args:
        def __init__(self, args, verbose, list_tasks, list_tags, step,
                     start_at_task, subset, syntax, inventory, module_path,
                     flush_cache, connection, remote_user, timeout,
                     private_key_file, ssh_common_args, ssh_extra_args,
                     sftp_extra_args, scp_extra_args, become, become_method,
                     become_user, become_ask_pass, ask_pass,
                     verbosity, check, diff):
            self.args = args
            self.verbose = verbose
            self.list_tasks = list_tasks
            self.list_tags = list_tags
            self.step = step
            self.start_at_task = start_at_

# Generated at 2022-06-12 20:36:48.956606
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def run_method(a, b, c):
        print("run method called")

    def ask_passwords():
        return (None, None)

    def display_output(a):
        print("display method called")


# Generated at 2022-06-12 20:37:00.345631
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Unit test for method run of class PlaybookCLI"""

    # create a test class object
    testobj = CLI()

    # test with a list of arguments that would be passed to the command line
    testargs = [ 'test_playbook.yml' ]

    # test with a dictionary that would be converted to an argparse object
    # test_playbook.yml is added as the first argument to the Options object
    # a test_connection attribute is added with a value of local
    # a test_verbosity attrbute is added with a value of 0
    # a test_check attribute is added with a value of True
    testkwargs = dict(test_connection= 'local', test_verbosity= 0, test_check= True)

    # run the method and check the results

# Generated at 2022-06-12 20:37:12.773534
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Create a mock object to store options and args
    class Options():
        listtasks = False
        listtags = False
        step = False
        start_at_task = None
        connection = 'ssh'
        module_path = None
        forks = 100
        remote_user = 'username'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = None
        become_user = None
        verbosity = 0
        check = False
        inventory = None
        subset = None
        extra_vars = []
        forking = None
        vault_password_file = None
        tags = []
        skip_tags = []
        one_line

# Generated at 2022-06-12 20:37:22.352699
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # We have to create those objects in test, because the constructor of PlaybookCLI
    # has side effects that we don't want, when testing method run

    loader = DataLoader()
    display.verbosity = 3 # verbose mode

    # A dummy inventory
    inventory = InventoryManager(loader=loader, sources=[])
    inventory.add_host(host='dummy')

    # A dummy variable manager
    variable_manager = VariableManager()

    # A dummy options

# Generated at 2022-06-12 20:37:32.792474
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # setup
    args = ['playbook.yml']

    context.CLIARGS = {}
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['listtasks'] = False
    context.CLIARGS['listtags'] = False
    context.CLIARGS['syntax'] = False
    context.CLIARGS['flush_cache'] = False
    context.CLIARGS['subset'] = None
    context.CLIARGS['args'] = args

    cli = PlaybookCLI()

    # test: no errors raised
    # assert:
    assert cli.run() is not None


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-12 20:37:33.600155
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:34.512520
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: Write this unit test
    pass

# Generated at 2022-06-12 20:38:50.856448
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:38:51.372184
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:38:51.874093
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:38:59.035898
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    FakeArgs = collections.namedtuple('fake_args', ['verbosity', 'syntax', 'check', 'listhosts', 'listtasks',
                                                    'listtags', 'step', 'start_at_task', 'args', 'flush_cache',
                                                    'diff'])

    # no hosts
    with pytest.raises(AnsibleError) as e:
        # -i /dev/null
        fake_args = FakeArgs(verbosity=None, syntax=None, check=None, listhosts=None, listtasks=None,
                             listtags=None, step=None, start_at_task=None, args=[], flush_cache=None, diff=None)
        context.CLIARGS = fake_args
        fake_display = FakeDisplay()
        display.verbosity = 1
        fake

# Generated at 2022-06-12 20:39:00.792920
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pb = PlaybookCLI(['ansible-playbook', '-h'])
    pb.parse()
    pb.run()

# Generated at 2022-06-12 20:39:05.975212
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def test(options, args, expected_return_code, expected_warnings, expected_warnings_list, expected_deprecation_warnings):
        assert expected_return_code
        assert expected_warnings
        assert expected_warnings_list
        assert expected_deprecation_warnings

    results = test(options, args, expected_return_code, expected_warnings, expected_warnings_list, expected_deprecation_warnings)

    assert results is not None


# Generated at 2022-06-12 20:39:06.428501
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:17.508507
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Arrange
    # Create instance of class PlaybookCLI
    playbook_cli = PlaybookCLI()
    playbook_cli.parser = CLI.base_parser(
        usage="%prog [options] playbook.yml [playbook2 ...]",
        connect_opts=True,
        meta_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        inventory_opts=True,
        runtask_opts=True,
        vault_opts=True,
        fork_opts=True,
        module_opts=True,
    )
    # parser.add_option('-v', '--verbose', dest='verbose', default=False, action="store_true")
    # parser.add_option('-f

# Generated at 2022-06-12 20:39:30.532039
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class MockCLI:
        def __init__(self, **kw):
            self.__dict__.update(kw)

    # no errors on empty args list
    context.CLIARGS = MockCLI(verbosity=1, listhosts=False, listtasks=False, listtags=False, syntax=False, subset=[])
    results = PlaybookCLI.run(PlaybookCLI())
    assert results == 0

    # error on not-playbook arg
    context.CLIARGS = MockCLI(verbosity=1, listhosts=False, listtasks=False, listtags=False, syntax=False, subset=[], args=['foobar'])

# Generated at 2022-06-12 20:39:42.291852
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # get an instance of PlaybookCLI
    # set function 'post_process_args' of class PlaybookCLI
    PlaybookCLI.post_process_args = lambda self, x: x
    # set function '_play_prereqs' of class PlaybookCLI
    PlaybookCLI._play_prereqs = lambda self: (None, None, None)

    # set context variable 'CLIARGS'

# Generated at 2022-06-12 20:41:56.124487
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    module = AnsibleModule(argument_spec={})

    p = PlaybookCLI([])
    p.parse()
    assert p.run() is None

# Generated at 2022-06-12 20:41:58.531899
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Check that constructor raises an error if args is not a list
    try:
        PlaybookCLI(args=object())
        assert False
    except AssertionError:
        pass

# Generated at 2022-06-12 20:42:06.930393
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = [
            '--extra-vars', '@/home/ansible/workspace/collection/collection/file.yaml',
            '--private-key', '/home/ansible/workspace/collection/collection/private.pem',
            '--vault-password-file', 'path',
            '--inventory-file', '/home/ansible/workspace/collection/collection/inventory',
            '--no-check-mode',
            '--host-key-checking', 'False',
            '--list-hosts',
            '/home/ansible/workspace/collection/collection/collection_playbook.yml'
    ]

    options = CLI.parse(args)
    context.CLIARGS = options

    c = PlaybookCLI()
    c.run()

# Generated at 2022-06-12 20:42:15.082905
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = []
    passtable = {}
    display_mock = Mock()
    display_mock.verbosity = 0
    loader_mock = Mock()
    inventory_mock = Mock()
    variable_manager_mock = Mock()
    passwords = {}
    # Create a mock pbex object with a list of plays being returned
    pbex_object = Mock()
    pbex_object.run.return_value = [{'playbook': 'test_playbook',
                                     'plays': [Mock(), Mock(), Mock()]}]
    # Create a mock object of class PlaybookExecutor
    pbex_mock = Mock(return_value=pbex_object)
    # Create a mock for the argument 'args'
    playbook_object = Mock()
    playbook_object.__str__.return_value

# Generated at 2022-06-12 20:42:20.419475
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import pytest
    # Required for mocking
    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.utils.display import Display
    from ansible.plugins.loader import add_all_plugin_dirs
    # Stub
    class Stub_AnsibleCollectionConfig:
        original_collection_paths = AnsibleCollectionConfig.collection_paths
        original_playbook_paths = AnsibleCollectionConfig.playbook_paths
        @staticmethod
        def reset():
            AnsibleCollectionConfig.collection_paths = Stub_AnsibleCollectionConfig.original_collection_paths
            AnsibleCollectionConfig.playbook_paths = Stub_AnsibleCollectionConfig.original_playbook_paths

# Generated at 2022-06-12 20:42:24.987028
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import pytest

    sys.argv = ['ansible-playbook', '-i', 'inventory/sample', 'test/test.yml', 'some_tag']
    CLI.setup()

    with pytest.raises(AnsibleError) as exc_info:
        PlaybookCLI().run()
    assert str(exc_info.value) == 'the playbook: test/test.yml could not be found'
