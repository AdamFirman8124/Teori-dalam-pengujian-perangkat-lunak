

# Generated at 2022-06-12 20:32:43.335086
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:53.647873
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import pytest
    from ansible.cli.playbook import PlaybookCLI

    # create a fake class to mock argv
    class fake_sys_argv:
        def __init__(self, arg):
            self.argv = arg

        def get(self):
            return self.argv

    # create a fake class for stdout
    class fake_stdout:
        def __init__(self):
            self.out = ""

        def get(self):
            return self.out

        def write(self, stdout_str, stderr_str=None):
            self.out += stdout_str

    # test for PlaybookCLI.run() when context.CLIARGS['listhosts'] is True
    # and context.CLIARGS['subset'] is None
    #

# Generated at 2022-06-12 20:32:56.663981
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    p=PlaybookCLI(['--list-hosts',"playbook.yml"])
    p.run()
if __name__ == '__main__':
    test_PlaybookCLI_run()

# Generated at 2022-06-12 20:33:02.297828
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest

    def mock__flush_cache(inventory, variable_manager):
        pass

    def mock__play_prereqs():
        return 'loader', 'inventory', 'variable_manager'

    @pytest.fixture
    def my_playbook(monkeypatch):
        '''Fixture providing a PlaybookCLI object with some monkeypatched methods.'''
        # Monkey-patching is required since a lot of external dependencies are involved
        monkeypatch.setattr('ansible.cli.playbook.PlaybookCLI._flush_cache', mock__flush_cache)
        monkeypatch.setattr('ansible.cli.playbook.PlaybookCLI._play_prereqs', mock__play_prereqs)
        monkeypatch.setattr('ansible.cli.CLI.post_process_args', lambda self, x: x)

# Generated at 2022-06-12 20:33:02.867135
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:09.743867
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Check that run raises AnsibleError when playbook argument is not a valid file or directory
    #
    # Arrange
    args = {
        'ask_vault_pass': False,
        'ask_pass': False,
        'become_ask_pass': False,
        'check': False,
        'diff': False,
        'vault_password_files': [],
        'forks': 5,
        'remote_user': 'root',
        'private_key_file': None,
        'listhosts': False,
        'subset': None,
        'timeout': 10,
        'listtags': False,
        'listtasks': False,
        'step': False,
        'start_at_task': None,
        'args': ['notapath']
    }
    cli = Playbook

# Generated at 2022-06-12 20:33:17.396177
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class AnsibleOptions(object):
        tags = ['all']
        listtags = True
        listtasks = True
        listhosts = True
        start_at_task = 'setup'
        step = True
        subset = 'webservers'
        inventory = 'hosts'
        one_line = True
        forks = 10
        module_path = None
        extra_vars = ['key=value']

# Generated at 2022-06-12 20:33:24.081178
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins import callbacks
    from ansible.plugins import connection_loader
    from ansible.plugins import filter_loader
    from ansible.plugins import lookup_loader
    from ansible.plugins import module_loader
    from ansible.plugins import shell_loader
    from ansible.plugins import strategy_loader
    from ansible.plugins import test_loader
    from ansible.plugins import vault_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.plugins.loader import plugins
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from six import PY2

    if PY2:
        from StringIO import StringIO
    else:
        from io import StringIO


# Generated at 2022-06-12 20:33:32.052522
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Testing PlaybookCLI.run()
    import tempfile
    import os
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_options_vars
    from ansible.galaxy.collection import CollectionRequirement


# Generated at 2022-06-12 20:33:39.854104
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class MockCLI(PlaybookCLI):

        def __init__(self):
            self.args = 'ad-hoc'

        def post_process_args(self):
            pass

        def ask_passwords(self):
            return 'ssh','become'

        def _play_prereqs(self):
            pass

        def run(self):
            return 'testing'


    try:
        results = MockCLI().run()
        assert results == 'testing'
    except CalledProcessError as e:
        assert False, e.stderr

# Generated at 2022-06-12 20:33:57.340893
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class MockOpts(object):
        verbosity = 0
        subset = None

    class MockCLIARGS(object):
        verbose = False
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        flush_cache = False
        subset = None
        tags = None
        start_at_task = None
        args = ['test.yml']

    context.CLIARGS = MockCLIARGS()

    class MockPlaybookExecutor(object):
        def __init__(self, playbooks, inventory, variable_manager, loader, passwords):
            self.playbooks = playbooks
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.passwords = passwords

        def run(self):
            return 0



# Generated at 2022-06-12 20:34:02.399479
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Instantiate a PlaybookCLI object with the arguments used to call ansible-playbook
    import sys
    cli = PlaybookCLI(["ansible-playbook", 
                      "-i", "/usr/share/ansible/plugins/inventory/test.yml", 
                      "playbook.yml"])
    cli.parse()
    cli.post_process_args(context.CLIARGS)
    # Call the run method of PlaybookCLI
    cli.run()

# Generated at 2022-06-12 20:34:12.446893
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from unittest import TestCase, mock

    from ansible import constants as C
    from ansible.playbook import Playbook

    test_case = TestCase()

    mock_playbookCLI = mock.Mock(spec=PlaybookCLI)
    mock_options = mock.Mock()
    mock_options.listhosts = False
    mock_options.listtags = False
    mock_options.listtasks = False
    mock_options.syntax = False
    mock_options.become_method = None
    mock_options.become_user = None
    mock_options.become_ask_pass = False
    mock_options.connection = None
    mock_options.timeout = C.DEFAULT_TIMEOUT
    mock_options.remote_user = None
    mock_options.ask_pass = False
   

# Generated at 2022-06-12 20:34:23.730918
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:34:24.344995
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:25.048672
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:36.023748
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    argv = []
    context.CLIARGS = {}
    cli = PlaybookCLI(args=argv)
    cli.parse()
    # context.CLIARGS = {'args': 'playbooks/ntp.yml', 'help': False}
    context.CLIARGS = {'args': ['playbooks/ntp.yml'], 'help': False, 'connection': 'ssh'}
    cli.run()
    # assert 0 == cli.run()

    # for no hosts matched error
    context.CLIARGS = {'args': ['playbooks/ntp.yml'], 'help': False, 'connection': 'ssh'}
    context.CLIARGS['subset'] = '!localhost'
    cli.run()
    # assert 4 == cli.run()

# Generated at 2022-06-12 20:34:36.579122
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:44.929837
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test that run() can read data from 'mock.yml'
    playbook_cli = PlaybookCLI()

    # Generate a mock object to replace sys.argv
    mock_args = []
    mock_args.append('__main__')
    mock_args.append('mock.yml')

# Generated at 2022-06-12 20:34:55.709512
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class MockPlaybookCLI(PlaybookCLI):
        def ask_passwords(self):
            return ('sshpass', 'becomepass')

        def _play_prereqs(self):

            class MockLoader():
                def set_basedir(self, basedir):
                    pass

            loader = MockLoader()

            class MockInventory():
                def __init__(self, host_list):
                    self.host_list = host_list

                def _get_hosts_from_pattern(self, pattern):
                    return self.host_list

                def get_hosts(self, pattern):
                    return self._get_hosts_from_pattern(pattern)

                def list_hosts(self):
                    return self.host_list

            inventory = MockInventory([])


# Generated at 2022-06-12 20:35:15.336419
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:35:26.343750
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    context.CLIARGS = {}

    display.verbosity = 5
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 20:35:26.861678
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:27.209148
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:36.443358
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test CLI.run with custom loader and mock.mock_open and some mocks for other objects
    # The mocked class for reading the file is to check that the file is loaded and its content
    # is processed into a list of playbooks.

    # Check for any existing environment variables and remove the ones needed for ansible.
    # This is done so that tests doesn't affect each other.
    cur_envs = dict(os.environ)

# Generated at 2022-06-12 20:35:47.278675
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test for class PlaybookCLI.
    """
    # When no args are passed to the argparse parser during unit testing, the parser complains and
    # exits in the CLI class.  It's a bit finicky, but we can create a dummy parser that does
    # not complain about missing args and just uses defaults for everything.
    def dummy_parser(*args, **kwargs):
        """Creates a dummy parser that uses defaults for everything."""
        parser = CLI.base_parser(*args, **kwargs)

# Generated at 2022-06-12 20:35:47.859565
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert True

# Generated at 2022-06-12 20:35:56.553402
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Initialize required objects
    class Options():
        def __init__(self):
            self.syntax = False
            self.connection = 'ssh'
            self.module_path = None
            self.forks = None
            self.become = True
            self.become_method = 'sudo'
            self.become_user = 'root'
            self.check = False
            self.extra_vars = [u'ansible_ssh_user=centos']
            self.flush_cache = False
            self.listhosts = None
            self.listtags = None
            self.listtasks = None
            self.module_path = None
            self.new_vault_password_file = None
            self.output_file = None
            self.private_key_file = None
            self.skip_

# Generated at 2022-06-12 20:36:06.953298
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    import shutil
    import os
    from ansible.inventory import Inventory
    from ansible.cli.playbook import PlaybookCLI
    from ansible.plugins.loader import add_directory

    # Create test playbook
    fd, fp = tempfile.mkstemp()
    test_playbook = '- hosts: all\n  gather_facts: false\n  tasks:\n  - name: Test\n    ping:\n'
    os.write(fd, to_bytes(test_playbook))
    os.close(fd)

    # Create test inventory
    fd, fp2 = tempfile.mkstemp()
    os.write(fd, to_bytes('localhost ansible_connection=local'))
    os.close(fd)

    # Create test plugins directory
    fake_collection_path

# Generated at 2022-06-12 20:36:16.635908
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class FakeOpts:
        args = ["playbook.yml"]
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        flush_cache = False

    class FakeCollectionsConfig:
        collection_paths = ["collections:/"]
        namespace_collections = []

        def __init__(self):
            self.namespace_collections = []
            self.collection_paths = ["collections:/"]

    class FakeCLIARGS:
        subset = None
        diff = False


# Generated at 2022-06-12 20:36:50.007684
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # remove existing data from project root path
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_playbook.yml')
    try:
        os.remove(file_path)
    except OSError:
        pass

    # create a playbook CLI object
    test_cli = PlaybookCLI(args=[file_path])

    # no playbook in the --args list, so the method should return an exit code of 4
    assert test_cli.run() == 4

    # create a playbook file
    with open(file_path, 'w') as f:
        f.write("""
        - hosts: test_host
          tasks:
            - name: test task
              debug:
                var: hello
        """)

    # run the test playbook

# Generated at 2022-06-12 20:36:51.147045
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    assert False


# Generated at 2022-06-12 20:36:51.718894
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert True

# Generated at 2022-06-12 20:36:53.389683
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:37:05.056185
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI()
    cli.options = lambda: None
    cli.options.sudo_user = None
    cli.options.connection = 'ssh'
    cli.options.remote_user = None
    cli.options.ask_pass = False
    cli.options.verbosity = 0
    cli.options.ask_sudo_pass = False
    cli.options.ask_su_pass = False
    cli.options.become = False
    cli.options.become_method = 'sudo'
    cli.options.become_user = 'root'
    cli.options.listhosts = False
    cli.options.listtasks = False
    cli.options.listtags = False
    cli.options.syntax = False
    cli.options

# Generated at 2022-06-12 20:37:10.869390
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    Test method run of class PlaybookCLI.
    '''

    from ansible.errors import AnsibleError
    from ansible.module_utils.common.removed import RemovedInAnsible28Warning

    # Prepare mocks
    class MockCLI(CLI):
        '''
        A mock CLi class used to test the PlaybookCLI class.
        '''
        def __init__(self):
            pass

        def init_parser(self):
            pass

        def post_process_args(self, options):
            return options

    class MockVariableManager(object):
        '''
        A mock VariableManager class used to test the PlaybookCLI class.
        '''
        def __init__(self, inventory):
            self.inventory = inventory


# Generated at 2022-06-12 20:37:18.677562
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test run()
    # Test when
    # 1. context.CLIARGS['listhosts'] is True
    # 2. context.CLIARGS['listtasks'] is True
    # 3. context.CLIARGS['listtags'] or context.CLIARGS['listtasks'] is True
    # 4. context.CLIARGS['syntax'] is True

    # Create one object that contains the argument and return values
    arguments_returns = {}

    # Create two objects that contains the return values of the methods
    # in the object pbex
    pbex_returns = {}

# Generated at 2022-06-12 20:37:29.790646
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class MockModuleV2CLI(object):
        ''' Mock class for module v2 cli '''

        def __init__(self, module_name, module_args, module_path=None, forks=None, become=None, become_method=None, become_user=None, check=False, diff=False):
            self.module_name = module_name
            self.module_args = module_args
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.bec

# Generated at 2022-06-12 20:37:31.475530
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # TODO: create unit tests for the module.
    pass

# Generated at 2022-06-12 20:37:39.500705
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook.play_context import PlayContext

    class DummyDisplay(object):
        def __init__(self):
            self.verbosity = 4
            self.display_skipped_hosts = True
            self.nonpersistent_connection = False
            self.skipped = []

        def display(self, msg):
            pass

        def display_verbose(self, msg, *args, **kwargs):
            pass

        def verbose(self, msg, *args, **kwargs):
            pass

        def display_debug(self, msg, *args, **kwargs):
            pass

        def debug(self, msg, *args, **kwargs):
            pass


# Generated at 2022-06-12 20:39:08.020101
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    parser = CLI.base_parser(connect_opts=True, meta_opts=True, runas_opts=True, subset_opts=True, check_opts=True,
                             inventory_opts=True, runtask_opts=True, vault_opts=True, fork_opts=True, module_opts=True)
    base_options, args = parser.parse_known_args(args=[])
    ctl = PlaybookCLI(base_options)
    ctl.init_parser()

    options, args = ctl.parser.parse_args(args=[])
    ctl.post_process_args(options)

    assert options.connect_timeout == 10
    assert options.diff
    assert options.host_key_checking
    assert options.host_key_auto_add
    assert options

# Generated at 2022-06-12 20:39:18.287347
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.errors import AnsibleError
    import os
    import stat
    import pytest

    class AnsiblePlaybookMultiCLI_run(PlaybookCLI):
        def __init__(self):
            self.args = ['test1.yml', 'test2.yml']
            self.my_post_process_args(self.args)

        def init_parser(self):
            self.parser = parser

        def my_post_process_args(self, args):
            b_playbook_dirs = []
            for playbook in args:

                resource = _get_collection_playbook_path(playbook)
                if resource is not None:
                    playbook_collection = resource[2]

# Generated at 2022-06-12 20:39:24.550163
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbc = PlaybookCLI()
    data = pbc.run()
    print(data)

if __name__ == "__main__":
    test_PlaybookCLI_run()

# Generated at 2022-06-12 20:39:29.068916
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = ['playbook.yml']
    options = {'list_tasks': True, 'step': True, 'verbosity': 1}
    cli = PlaybookCLI(args, **options)
    cli.run()

if __name__ == '__main__':
    test_PlaybookCLI_run()

# Generated at 2022-06-12 20:39:41.201676
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task.include import TaskInclude
    from ansible.plugins.loader import add_all_plugin_dirs

    # Add core plugin directories to the plugin loader
    add_all_plugin_dirs()

    # We do not want to send this to dbs
    os.environ['ANSIBLE_NOCOWS'] = 'true'

    # create a block and task include

# Generated at 2022-06-12 20:39:42.599384
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    r = PlaybookCLI.run()
    if r > 0:
        raise ValueError()

# Generated at 2022-06-12 20:39:44.307177
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Check if command is available
    cli = PlaybookCLI(args=[])
    assert cli.run is not None

# Generated at 2022-06-12 20:39:47.668804
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    config = PlaybookCLI()
    result = config.run()

    # Assert if the function is called
    assert not result

# Generated at 2022-06-12 20:39:57.036816
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # setup mocks and apply patches
    mock_playbook_ansible_playbook_cli_run1 = MagicMock(return_value=PlaybookCLI())
    mock_add_plugin_directory1 = MagicMock(return_value=None)
    mock_add_plugin_directory2 = MagicMock(return_value=None)

    tmp_file1 = NamedTemporaryFile(suffix="yml")
    tmp_file1.write(b"""
    ---
    - hosts: localhost
      tasks:
        - name: example task
          debug:
            msg: "Test Message"
    """)
    tmp_file1.flush()

    tmp_file2 = NamedTemporaryFile(suffix="yml")

# Generated at 2022-06-12 20:40:07.539530
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: need to mock out all the dependencies of the run method.
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["test/testhosts"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 20:41:31.043929
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    import sys
    sys.argv.append("/home/user/playbook.yml")

    opt = PlaybookCLI().parse()
    opt.show_custom_stats=True
    PlaybookCLI().run()

# Generated at 2022-06-12 20:41:35.631328
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Arrange
    args = []
    args.append("ansible-playbook")
    args.append("--list-hosts")
    args.append("-i")
    args.append("test/test_playbook_cli/inventory")
    args.append("test/test_playbook_cli/playbook.yml")

    # Act
    display.verbosity = 3
    cli = PlaybookCLI(args)
    result = cli.run()

    # Assert
    assert result == 0


# Generated at 2022-06-12 20:41:41.570737
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI

    class Options:
        listtags = False
        listtasks = False
        listhosts = False

        verbosity = 0
        syntax = False
        subset = None
        start_at_task = None
        step = False

        connection = 'smart'
        timeout = C.DEFAULT_TIMEOUT
        ssh_common_args = None
        sftp_extra_args = None
        scp_extra_args = None
        ssh_extra_args = None
        become = False
        become_method = C.DEFAULT_BECOME_METHOD
        become_user = None
        become_ask_pass = False
        check = False
        inventory = None
        diff = False
        vault_password_files = None
        tags = []
        skip_tags = []

# Generated at 2022-06-12 20:41:50.630896
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
     def _get_cmd(*args, **kwargs):
         return [(to_bytes('host.example.com'), to_bytes('/bin/echo test'), to_bytes(''))]
     import ansible.plugins.action.normal
     ansible.plugins.action.normal._get_cmd = _get_cmd
     from ansible.utils import context_objects as co
     from collections import namedtuple
     from ansible.inventory.manager import InventoryManager
     from ansible.parsing.dataloader import DataLoader
     from ansible.vars.manager import VariableManager
     from ansible.executor import playbook_executor
     from ansible.executor.task_queue_manager import TaskQueueManager
     from ansible.plugins.callback import CallbackBase
     from ansible.errors import AnsibleError

# Generated at 2022-06-12 20:41:53.526019
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbcli = PlaybookCLI(args=['test'])
    # test for displays
    display.verbosity = 3
    pbcli.run()
    display.verbosity = 0

# Generated at 2022-06-12 20:41:54.164734
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:42:03.852789
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: consider converting this into a test of functionality in the method
    # rather than just testing to see if the method runs

    def display_mock(value):
        assert value == '\nplaybook: here'

    display.display = display_mock

    class OptionsMock:
        def __init__(self):
            self.listhosts = False
            self.listtasks = False
            self.listtags = False
            self.syntax = False
            self.connection = 'smart'
            self.module_path = None
            self.forks = 5
            self.private_key_file = None
            self.timeout = 10
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra

# Generated at 2022-06-12 20:42:11.645995
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.module_utils.common._collections_compat import MutableSequence
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    import os
    import pytest

    class MockCLIArgs:
        listhosts = False
        listtags = False
        syntax = False
        subset = False
        flush_cache = False
        verbosity = 0
        diff = False
        check = False
        inventory = []
        extra_vars = []
        limits = []
        tags = []
        skip_tags = []
        start_at_task = None
        args = []

    class MockPlaybook:
        def __init__(self, playbook):
            playbook_collection = _get_collection_name_from_path(playbook)
           

# Generated at 2022-06-12 20:42:18.870662
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # init
    mocker.patch('ansible.cli.PlaybookCLI.ask_passwords')

    # use fixture
    pbex_run_mock = mocker.patch('ansible.executor.playbook_executor.PlaybookExecutor.run')

    # patch
    mocker.patch('ansible.cli.PlaybookCLI._play_prereqs')
    mocker.patch('ansible.cli.CLI.get_host_list', return_value=['host1', 'host2'])

    # init class
    cli = PlaybookCLI(['playbook.yml', 'playbook2.yml'])

    # run
    cli.run()

    # test
    assert pbex_run_mock.called
    assert pbex_run_mock.call_

# Generated at 2022-06-12 20:42:26.749935
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """ Test for `ansible-playbook -i inventory playbook.yml` """

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    mocker = Mocker()
    mock_get_host_list = mocker.replace(CLI.get_host_list)
    mock_get_host_list(ANY, ANY)
    mocker.count(0, None)

    # mock the play object with empty tasks
    m_play = mocker.mock()
    mocker.count(0, None)
    mocker.replay()

    # mock the playbook executor
    m_playbook_executor = mocker.mock()
    mocker.count(2, None)
    mocker.replay()

    # mock the play