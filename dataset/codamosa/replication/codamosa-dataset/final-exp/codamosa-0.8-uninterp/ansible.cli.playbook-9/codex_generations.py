

# Generated at 2022-06-12 20:32:46.341110
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test 1
    test_PlaybookCLI = PlaybookCLI()
    assert test_PlaybookCLI.display is not None


# Generated at 2022-06-12 20:32:55.851734
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from ansible import constants as C

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars

    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.playbook.play import Play
    from ansible.playbook._data import PlaybookData
    from ansible.playbook._includer import IncludeLoader
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task

   

# Generated at 2022-06-12 20:33:05.132865
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.parsing.dataloader import DataLoader

    # This is a basic "unit test" for method PlaybookCLI.run() that does not
    # require a full-blown integration test.

    class FakeOpts(object):
        def __init__(self):
            self.ask_pass = False
            self.ask_vault_pass = False
            self.connect_timeout = 10
            self.verbosity = 0
            self.check = False
            self.diff = False
            self.extra_vars = None
            self.flush_cache = False
            self.force_handlers = False
            self.force_poll = False
            self.inventory = "/path/to/inventory"
            self.listhosts = False
            self.listtags = False
            self.listtasks = False
           

# Generated at 2022-06-12 20:33:06.698839
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    sys.argv = ['ansible-playbook', '--list-hosts', 'playbook.yml']
    cli = PlaybookCLI({})
    assert cli.run() == 0

# Generated at 2022-06-12 20:33:12.931106
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Setup test.
    from ansible.errors import AnsibleError


# Generated at 2022-06-12 20:33:21.133139
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class MockPlaybookCLI(PlaybookCLI):
        pass

    results = []

    class MockPlaybookExecutor:
        def __init__(self, playbooks, inventory, variable_manager, loader, passwords):
            pass

        def run(self):
            results.append('Playbook Executor Run')
            return results

    class MockInventory:
        @staticmethod
        def list_hosts():
            return 'hosts'

        @staticmethod
        def get_hosts():
            return 'playhosts'

    class MockLoader:
        @staticmethod
        def set_basedir():
            pass

    class MockVariableManager:
        @staticmethod
        def get_hosts():
            return 'hosts'

        @staticmethod
        def get_vars():
            return 'all_vars'

       

# Generated at 2022-06-12 20:33:27.026788
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # PlaybookCLI.run() exits when the module is run so we test it via a method in a separate class
    # The unit test code is in the test_module_utils directory
    class TestPlaybookCLI(PlaybookCLI):

        def run(self):
            return super(TestPlaybookCLI, self).run()

    # Mock options

# Generated at 2022-06-12 20:33:38.345329
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Prepare a fake context
    context.CLIARGS = dict()
    context.CLIARGS['args'] = ['test_data/test_playbook_cli.yml']
    context.CLIARGS['listhosts'] = True
    context.CLIARGS['listtasks'] = True
    context.CLIARGS['listtags'] = True
    context.CLIARGS['step'] = True
    context.CLIARGS['start_at_task'] = 'test task'

    # Run
    PlaybookCLI().run()

    # Prepare a fake context
    context.CLIARGS = dict()
    context.CLIARGS['args'] = ['test_data/test_playbook_cli.yml']
    context.CLIARGS['listhosts'] = True
    context.CL

# Generated at 2022-06-12 20:33:45.794598
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    The class PlaybookCLI has method run, which is tested here
    """

    #instantiate
    pbcli = PlaybookCLI(['/usr/local/bin/ansible-playbook'])

    #create test args
    options = pbcli.parser.parse_args(['-i', 'test_inv', '-b', '-c', 'local',
                                       '--vault-id', 'test@prompt',
                                       '-v', '--become-user', 'testuser',
                                       '--become-method', 'su',
                                       '-k', '--flush-cache', 'test_playbook.yml'])

    #add test args

# Generated at 2022-06-12 20:33:50.606092
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Instantiate test class
    pbcli = PlaybookCLI('ansible-playbook')

    # Example playbook in test/integration/playbooks
    playbook_path = 'playbooks/play.yml'

    # Set command line arguments for playbook run
    pbcli.args = ['-v', playbook_path]

    # Run method to execute playbook run
    pbcli.run()

# Generated at 2022-06-12 20:34:02.081018
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:09.133698
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test that the method exit with 0 if
    - a playbook is given
    - the playbook exists
    - the playbook is a file
    """
    context.CLIARGS = {}
    context.CLIARGS['args'] = [ "dummy" ]
    context.CLIARGS['help'] = False

    play = PlaybookCLI()
    play.post_process_args = lambda x: x
    play.parse()
    play.run()

# Generated at 2022-06-12 20:34:09.667429
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:11.126932
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    p = PlaybookCLI()
    res = p.run()
    assert res == 0



# Generated at 2022-06-12 20:34:17.943782
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_Playerbook_CLI = PlaybookCLI()

    # Case 1: not run success
    options = {}
    options['listhosts'] = True
    options['listtasks'] = True
    options['listtags'] = True
    options['syntax'] = True
    options['ask_vault_pass'] = True
    options['new_vault_password_file'] = True
    options['output_file'] = False
    options['flush_cache'] = False
    options['verbosity'] = 0
    options['connection'] = False
    options['module_path'] = True
    options['forks'] = True
    options['become'] = True
    options['become_method'] = True
    options['become_user'] = True
    options['check'] = True
    options['listhosts'] = True

# Generated at 2022-06-12 20:34:29.485621
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(args=['--list-hosts', 'playbook.yml'])
    cli.post_process_args(context.CLIARGS)

    loader, inventory, variable_manager = cli._play_prereqs()
    pbex = PlaybookExecutor(playbooks=context.CLIARGS['args'], inventory=inventory,
                            variable_manager=variable_manager, loader=loader,
                            passwords={})

    # Mocking method run from PlaybookExecutor class
    class MockPlaybookExecutor(PlaybookExecutor):
        def run(self):
            return 0

    pbex.run = MockPlaybookExecutor.run
    assert cli.run() == 0


# Generated at 2022-06-12 20:34:30.448916
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    
    PlaybookCLI.run()

# Generated at 2022-06-12 20:34:33.666731
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Unit test for the method 'playbook_executor' of class PlaybookCLI
    """
    pass

# Generated at 2022-06-12 20:34:34.460559
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    raise RuntimeError('Test not implemented!')

# Generated at 2022-06-12 20:34:37.617520
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    print("Testing command line: --help")
    cli = PlaybookCLI([])
    cli.parse()
    assert cli.run() == 0

if __name__ == '__main__':
    plugin = PlaybookCLI()
    plugin.execute()

# Generated at 2022-06-12 20:34:59.739529
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:04.816075
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class Options(object):
        verbosity = 0
        connection = 'ssh'
        module_path = None
        forks = 10
        remote_user = 'root'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        playbook_path = '/path/to/ansible/playbooks'
        syntax = False
        start_at_task = None
        step = None
        subset = None
        inventory = 'playbook.inventory'
        listhosts = False
        listtasks = False
        listtags

# Generated at 2022-06-12 20:35:15.028770
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os
    import sys
    import tempfile

    save_cwd = os.getcwd()
    save_argv = sys.argv


# Generated at 2022-06-12 20:35:22.204773
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible.cli.arguments import DISPLAY_ARGS
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager

    with pytest.raises(AnsibleError) as err:
        context.CLIARGS = {'args': ['/tmp/playbook.yml'], 'connection': 'local', 'verbosity': 3}
        cli = PlaybookCLI(args=[])
        cli.run()
    assert "playbook: /tmp/playbook.yml" == str(err.value)
    assert "could not be found" in str(err.value)

    context

# Generated at 2022-06-12 20:35:25.955920
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    Returns the number of failed tests
    '''
    fail_count = 0
    # run() has a CLI interface and doesn't take arguments, so nothing to unit test
    pass

    return fail_count


# Generated at 2022-06-12 20:35:28.091961
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.cli import CLI
    cli = CLI(['-i', 'localhost,', '-m', 'ping', 'all'])
    cli.parse()
    pass

# Generated at 2022-06-12 20:35:28.605013
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:37.608223
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import mock

    context.CLIARGS = mock.MagicMock()
    context.CLIARGS.verbosity = 0
    context.CLIARGS.flush_cache = False
    context.CLIARGS.args = ['test_PlaybookCLI_run']
    context.CLIARGS.listhosts = False
    context.CLIARGS.listtags = False
    context.CLIARGS.syntax = False
    context.CLIARGS.check = False
    context.CLIARGS.check_mode = False
    context.CLIARGS.step = False
    context.CLIARGS.start_at_task = None
    context.CLIARGS.force_handlers = False

    pbcli = PlaybookCLI()

    inventory = mock.MagicMock()
    variable

# Generated at 2022-06-12 20:35:38.185685
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:48.994274
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # these are called with a method because we can't set the function
    # signature of the __call__ method, and so we can't really mock the
    # function using a decorator
    #
    # TODO: implement a decorator which can set the function signature
    #       of the __call__ method

    # create a mock of class PlaybookCLI
    class MockPlaybookCLI:

        # mock method CLIbase.get_host_list
        def mock_get_host_list(self, inventory, subset):
            return True

        # mock method PlaybookCLI._play_prereqs
        def mock_play_prereqs(self):
            return True

        # mock method PlaybookExecutor.run

# Generated at 2022-06-12 20:36:54.239829
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class MockException(Exception):
        pass

    def ask_passwords(self):
        raise MockException

    def get_host_list(inventory, subset):
        raise MockException

    def _play_prereqs(self):
        raise MockException

    class MockPlaybookExecutor(object):
        def run(self):
            return None

    class MockAnsibleCLI(object):
        def run(self):
            return None

    class MockPlaybookCLI(PlaybookCLI):
        def ask_passwords(self):
            return ask_passwords(self)

        def get_host_list(inventory, subset):
            return get_host_list(inventory, subset)

        def _play_prereqs(self):
            return _play_prereqs(self)


# Generated at 2022-06-12 20:37:00.792939
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # FIXME: Jenkins build fails if this is written in traditional form.
    #
    # pb = PlaybookCLI()
    # inv = pb._play_prereqs()[1]
    #
    # Add localhost to inventory.
    # inv.add_host('localhost')
    #
    # Run a playbook
    # res = pb.run()
    #
    # Assert that the playbook run was successful
    # assert res == 0
    pass

# Generated at 2022-06-12 20:37:01.441012
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:13.663218
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:37:23.920379
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbook_cli = PlaybookCLI()

    # playbook is the 1st positional arg
    playbook = "/my/test/test_filename.yml"
    args = [ playbook, "a", "b"]

# Generated at 2022-06-12 20:37:34.681870
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible_collections.misc.not_a_real_collection.plugins.modules import test_ping
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vars import combine_vars

    test_args = {
        'verbosity': 3,
        'inventory': 'inventory',
        'listtasks': True,
        'listtags': True,
        'step': False,
        'start_at_task': None,
        'args': ['playbook'],
    }
    test_playbook_cli = PlaybookCLI(args=test_args)
    with pytest.raises(AnsibleError) as excinfo:
        test_playbook_cli.run()

# Generated at 2022-06-12 20:37:35.577761
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:37:40.840686
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.cli.arguments import OPTION_FLAGS
    from ansible.cli import CLI
    """
    Unit test for method run of class PlaybookCLI

    """
    pb = PlaybookCLI()
    pb.run()

    #assertEqual(first, second, msg)
    pb.post_process_args(context.CLIARGS)
    pb.init_parser()

# Generated at 2022-06-12 20:37:44.651007
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test successful run
    #inventory = Inventory(loader=CLI._create_loader(['all'], None, variable_manager))

    # Test with None input
    assert PlaybookCLI.run(None) == 0

    # Test with the inventory is empty
    assert PlaybookCLI.run([]) == 0

    # Test with the inventory containing a wrong file
    assert PlaybookCLI.run(['foobar.yml']) == 0

    # test with a good inventory
    assert PlaybookCLI.run() == 0

# Generated at 2022-06-12 20:37:45.255091
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run(True)

# Generated at 2022-06-12 20:40:11.020906
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.config.manager import ConfigManager
    from ansible.errors import AnsibleError
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class TestPlaybookCLI(PlaybookCLI):
        def _play_prereqs(self):
            class TestLoader:
                def get_basedir(self):
                    return '/test/ansible/path/'
                def set_basedir(self, path):
                    pass
            class TestInventory:
                def list_hosts(self, pattern):
                    return [pattern]
            class TestVariableManager:
                pass
            return (TestLoader(), TestInventory(), TestVariableManager())

# Generated at 2022-06-12 20:40:21.016099
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Unit test run method of class PlaybookCLI"""
    # This code sure is a mess
    # pylint: disable=too-many-return-statements,too-many-locals
    # pylint: disable=too-many-branches,too-many-statements
    # pylint: disable=protected-access

    def check(cmd, **kwargs):
        """Add another loop around the normal check function to do additional verification"""
        if cmd[0] == 'ssh':
            if cmd[1] in ('-C', '-o', 'ControlMaster=auto', '-o', 'ControlPersist=60s', '-o', 'ControlPath=/home/myuser/.ansible/cp/ansible-ssh-%h-%p-%r'):
                raise ValueError("Bad command")
        check_orig

# Generated at 2022-06-12 20:40:21.663760
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:40:30.241116
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class MyException(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    class MyPlaybookCLI(PlaybookCLI):
        def ask_passwords(self):
            return ('sshpass', 'becomepass')

        def _play_prereqs(self):
            class MyOptions(object):
                pass
            opts = MyOptions()
            opts.connection = 'ssh'
            opts.module_path = 'module_path'
            opts.forks = 5
            opts.become = False
            opts.become_method = 'sudo'
            opts.become_user = 'root'
            opts.check = False
            opts.diff = False

            inventory = Base

# Generated at 2022-06-12 20:40:39.914156
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:40:43.928166
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create some sample fake args.
    args = ['ansible-playbook', '--version']

    # create an instance of PlaybookCLI and call run
    cli = PlaybookCLI(args)
    res = cli.run()

    # check that res is not a list
    assert not isinstance(res, list)

# Generated at 2022-06-12 20:40:44.359137
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:45.937114
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(['test.yml'])
    inventory = cli.inventory_manager.get_inventory()
    for host in inventory.get_hosts():
        host.vars['ansible_connection'] = 'local'

# Generated at 2022-06-12 20:40:51.943680
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    class TestCLIargs(object):
        version = False
        verbosity = 0
        inventory = None
        subset = None
        module_paths = None
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        connection = 'smart'
        timeout = C.DEFAULT_TIMEOUT
        forks = context.CLIARGS['forks']
        remote_user = C.DEFAULT_REMOTE_USER
        private_key_file = C.DEFAULT_PRIVATE_KEY_FILE
        diff = False
        check = False
        syntax_check = False
        start_at_task = None
        step = False
        become = False
        become_method = 'sudo'
        become_user = C.DEFAULT_BECOME_USER
        become_

# Generated at 2022-06-12 20:40:55.973814
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    try:
        pb = PlaybookCLI(['plays/playbook.yml'])
        assert pb.run() == 0
    except AnsibleError:
        assert False