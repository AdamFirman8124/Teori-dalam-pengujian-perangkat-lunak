

# Generated at 2022-06-12 20:32:40.597020
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cls = PlaybookCLI(args=[])
    cls.run()


# Generated at 2022-06-12 20:32:50.984341
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #
    # Testing for cases where no playbook is provided.
    # Should fail as there is no playbook provided.
    #
    CLIARGS = dict(flush_cache=False, syntax=False, start_at_task=None, step=False,
                   listtags=False, listtasks=False, module_path=None, connection=None,
                   remote_user=None, private_key_file=None, sudo_user=None, timeout=None,
                   subset=[], listhosts=False, forks=None, sudo=None, become=None,
                   become_method=None, become_user=None, check=False, diff=False,
                   syntax_check=False, start_at_task=None, verbosity=None, args=[])

    display = Display()
    pb_cli = PlaybookCLI(None, display)

# Generated at 2022-06-12 20:32:51.527837
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:52.085279
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:59.476441
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible import constants as C
    from ansible.cli import CLI
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import all_plugin_groups
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.loader import all
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    from ansible.vars.manager import VariableManager
    from ansible_collections.sgreen.ansible_cli_playbook.tests.unit.mock import mock_open
    from ansible_collections.sgreen.ansible_cli_playbook.tests.unit.mock import patch

# Generated at 2022-06-12 20:33:07.982153
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class FakePlaybookExecutor:

        def __init__(self, playbooks=None, inventory=None, variable_manager=None, loader=None, passwords=None):
            self.playbooks = playbooks
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.passwords = passwords

        def run(self):
            return [{'playbook': self.playbooks[0],
                     'plays': [FakePlay(hosts='localhost', name='play1', tags=['tag1', 'tag2']),
                               FakePlay(hosts='localhost', name='play2', tags='tag3')]}]


    def _process_block(b):
        taskmsg = ''

# Generated at 2022-06-12 20:33:08.425819
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:10.221435
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:17.159489
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test function for run function of PlaybookCLI.

    """
    from .test_utils import MockCLI
    with MockCLI() as cli:
        cli.playbookcli = PlaybookCLI(['playbookcli', 'ansible.cfg', '/tmp/playbook.yml'])
        cli.mock_options = {'listtags': True, 'listtasks': True}
        cli.mock_args = cli.playbookcli.parse()
        cli.playbookcli.run()

# Generated at 2022-06-12 20:33:23.870752
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from io import StringIO
    PlaybookCLI.parser = opt_help.create_parser()

# Generated at 2022-06-12 20:33:32.782624
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    result = PlaybookCLI().run()
    assert result == 1

# Generated at 2022-06-12 20:33:33.896716
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:43.059364
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from units.mock.loader import DictDataLoader

    cli = PlaybookCLI([])
    cli.options = opt_help.get_base_opts({})
    sshpass = None
    becomepass = None
    passwords = {}

    loader = DictDataLoader({
        'playbook.yml': """
        - hosts: all
          tasks:
            - name: foo
              debug: msg="hello world"
        """,
        'inventory.yml': """
        all:
            hosts:
                localhost:
        """,
        'ansible.cfg': """
        [defaults]
        host_key_checking = False
        """
    })

    inventory = Inventory(loader=loader, variable_manager=VariableManager, host_list='inventory.yml')

    pbex = PlaybookExec

# Generated at 2022-06-12 20:33:48.055397
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test the correct execution of PlaybookCLI.
    """

    # Test --version
    # with pytest.raises(SystemExit) as cm:
    #     PlaybookCLI(['PlaybookCLI.py', '--version'])
    # assert cm.value.code == 0

    # Test --help
    # with pytest.raises(SystemExit) as cm:
    #     PlaybookCLI(['PlaybookCLI.py', '--help'])
    # assert cm.value.code == 0

    # Test playbooks
    plb_cli = PlaybookCLI(['PlaybookCLI.py'])
    plb_cli.run()

# Generated at 2022-06-12 20:33:54.829122
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Unit testing for the method run() of PlaybookCLI class. """


# Generated at 2022-06-12 20:33:55.662524
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # hush pylint
    assert True

# Generated at 2022-06-12 20:33:59.892339
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Initialize a dummy class
    class Obj(object):
        description = ''
        epilog = ''

    # Initialize a dummy parent class
    class Dummy_playbook_cli(PlaybookCLI):
        pass

    # Create an instance
    cli = Dummy_playbook_cli(Obj())

    # Initialize argument
    args = ''

    # Call the method
    cli.parse(args.split())
    cli.run()

# Generated at 2022-06-12 20:34:00.427704
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:02.061603
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Unit test for method run of class PlaybookCLI"""
    # TODO: write a unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:34:09.462059
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os, sys, shlex

    test_args_file = sys.modules[__name__].__file__.rstrip('c') + 'args'
    args_file = open(test_args_file, 'r')
    args = shlex.split(args_file.read())
    args_file.close()
    args.append('playbooks/test_playbook.yml')
    p = PlaybookCLI(args)

    result = p.run()
    assert result == 0

# Generated at 2022-06-12 20:34:34.617561
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
    from ansible.utils.display import Display
    import shutil
    # test fixture
    # create a playbook working directory
    playbook_dir = '/tmp/test_playbook_cli'
    os.mkdir(playbook_dir)

# Generated at 2022-06-12 20:34:35.768810
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    raise NotImplementedError


# Generated at 2022-06-12 20:34:44.383122
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Mocking mock_tqm_instance
    from ansible.executor.task_queue_manager import TaskQueueManager
    mock_tqm = TaskQueueManager(None, None, None, None, None, None, None)
    mock_tqm.send_callback = ''
    mock_tqm.stats = {'dark': {}, 'failures': {}, 'skipped': {}, 'ok': {}, 'processed': {}, 'changed': {}}
    # Mocking playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    mock_variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-12 20:34:47.612430
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test case: no playbook supplied
    result = PlaybookCLI.run(None, [])
    assert result == 2

    # Test case: non-existent path supplied
    result = PlaybookCLI.run(None, ['--help'])
    assert result == 0

    # Test case: missing file
    result = PlaybookCLI.run(None, ['playbook_play.yml'])
    assert result == 2

# Generated at 2022-06-12 20:34:57.337953
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    args = ['/path/to/playbook.yml']

# Generated at 2022-06-12 20:34:59.639442
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:10.354140
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    class MockOptions(object):
        listhosts = False
        subset = None
        listtasks = True
        listtags = False
        start_at_task = None
        step = False
        syntax = True
        connection = 'local'
        module_path = None
        forks = context.CLIARGS['forks']
        remote_user = context.CLIARGS['remote_user']
        private_key_file = context.CLIARGS['private_key_file']
        ssh_common_args = context.CLIARGS['ssh_common_args']
        ssh_

# Generated at 2022-06-12 20:35:19.122416
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #Initializing test variables
    context.CLIARGS = {'listhosts': True, 'listtags': True, 'listtasks': True, 'syntax': False,
                       'subset': None, 'flush_cache': False,
                       'args': ['/Users/patel/ansible/ansible/test/static/test_collections/ansible_collections/ansible_test/test_fixtures/plugins/inventory/test_collection_inventory.yaml']}

    #Creating display object for mocking
    display = Display()
    #Mocking display class
    display.display = lambda x: ""

    #Creating object of class PlaybookCLI
    pb = PlaybookCLI()
    #Running run method which will return status of 0 (success)
    status = pb.run()

    assert status == 0

# Generated at 2022-06-12 20:35:22.453048
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(['foo'])
    setattr(cli, '_play_prereqs', lambda: (None, None, None))
    cli.run()



# Generated at 2022-06-12 20:35:24.016041
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #TODO
    return True

# Generated at 2022-06-12 20:36:08.708567
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:17.678680
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    context._init_global_context(override_sys_args=['ansible-playbook'])

# Generated at 2022-06-12 20:36:27.725463
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """This tests the method run of class PlaybookCLI on a list of playbooks"""

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=data_loader, inventory=inventory)
    cli = PlaybookCLI(['-i', 'localhost,', 'hacking/test-vars-included.yml'])
    cli._play_prereqs = lambda: (data_loader, inventory, variable_manager)
    cli.run()

# Generated at 2022-06-12 20:36:29.451496
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(['test', '-vvs'])
    cli.run()

# Generated at 2022-06-12 20:36:42.060447
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Create a mock object to represent the options
    class Options(object):
        def __init__(self):
            self.version = False
            self.inventory = None
            self.listhosts = False
            self.subset = None
            self.module_paths = []
            self.extra_vars = []
            self.playbook_paths = []
            self.ask_vault_pass = False
            self.vault_password_files = []
            self.new_vault_password_file = None
            self.output_file = None
            self.flush_cache = False
            self.tags = []
            self.skip_tags = []
            self.one_line = None
            self.tree = None
            self.ask_sudo_pass = False
            self.ask_su_pass = False


# Generated at 2022-06-12 20:36:42.651496
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:44.402046
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Skipped in Ansible 2.0 as the test is not applicable
    # This test should no longer be applicable
    pass

# Generated at 2022-06-12 20:36:48.076139
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.setup()
    res = PlaybookCLI.run()

# Unit test of @staticmethod _flush_cache of class PlaybookCLI

# Generated at 2022-06-12 20:36:55.306054
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create a PlaybookCLI instance for testing
    cli = PlaybookCLI(args=[])
    cli.setup()
    cli.parser = cli.create_parser()

    # test 'listtasks'
    args = ['-i', 'localhost,', '-c', 'local', '-k', '-T', 's',
            '--list-tasks', '--list-tags', '-vvv', '--check', '-e', 'free_form_some_confs=some_value', 'fake_playbook.yml']
    context.CLIARGS = cli.parse(args)
    cli.post_process_args(context.CLIARGS)
    result = cli.run()
    assert result == 0

    # test 'listhosts'

# Generated at 2022-06-12 20:37:07.092643
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.module_utils._text import to_bytes

    # Initialize a class
    cli = PlaybookCLI()

    # We want to check the functionality of the class PlaybookCLI,
    # so we use the run method of the class

    # We initialize the parser of the class
    cli.init_parser()

    # We are testing the method run of the class PlaybookCLI,
    # so we need to define the values of the options of the parser

    # We define the name of the playbook
    # We use a test file
    options = ['ansible-test-playbook.yml']

    # We introduce the option --list-tasks as True
    # If we want to list all tasks that would be executed
    options.append('--list-tasks')

    # We introduce the option --list-tags as True

# Generated at 2022-06-12 20:39:19.872069
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    context.CLIARGS = {'args': 'ansible/test/unit/ansible/test_playbook_cli.yml'}
    cli = PlaybookCLI(args=[])
    cli.run()
    print('')
    print('************* Flushing Cache *************')
    print('')
    cli.run()

# Generated at 2022-06-12 20:39:31.413866
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class TestPlaybookCLI(PlaybookCLI):
        def _flush_cache(self, inventory, variable_manager):
            pass

    class TestOptions(object):
        def __init__(self):
            self.syntax = False
            self.listhosts = False
            self.listtasks = False
            self.listtags = False
            self.verbosity = 0
            self.connection = None
            self.module_path = None
            self.forks = 5
            self.remote_user = C.DEFAULT_REMOTE_USER
            self.private_key_file = C.DEFAULT_PRIVATE_KEY_FILE
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra_args

# Generated at 2022-06-12 20:39:33.390264
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: Not implemented
    pass

# Generated at 2022-06-12 20:39:43.741684
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test fixture
    def mock_ask_passwords():
        return "foo", "bar"

    def mock_post_process_args(self, options):
        return options

    def mock_get_host_list(inventory, subset):
        return

    def mock_run(self):
        return

    PlaybookCLI._ask_passwords = mock_ask_passwords
    PlaybookCLI.post_process_args = mock_post_process_args
    PlaybookCLI.get_host_list = mock_get_host_list
    PlaybookCLI.run = mock_run

    # Test code
    args = [
        '-e', '@playbook.yml',
        '-i', 'inventory',
        'playbook.yml',
    ]

# Generated at 2022-06-12 20:39:44.317340
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:55.548476
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''Unit test for method run of class PlaybookCLI'''

    # import statements
    import sys
    import os
    import pathlib
    import tempfile
    import shutil
    import io

    import pytest

    # instantiate class
    cli = PlaybookCLI(args=[])

    # create temp dir
    temp_dir = tempfile.mkdtemp()

    # create temp files
    temp_file1 = os.path.join(temp_dir, 'testfile1.yml')
    pathlib.Path(temp_file1).write_text('hosts: all\n')

    # create temp files
    temp_file2 = os.path.join(temp_dir, 'testfile2.yml')
    pathlib.Path(temp_file2).write_text('hosts: all\n')

# Generated at 2022-06-12 20:39:56.165321
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:04.165433
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    playbook_path = os.path.join(test_dir, u'playbook.yml')

    with open(playbook_path, 'w') as f:
        f.write("- hosts: all\n"
                "  gather_facts: no\n"
                "  tasks:\n"
                "  - debug: msg=\"Hello from Ansible.\"\n")

    pbcli = PlaybookCLI()
    pbcli.run()

# Generated at 2022-06-12 20:40:04.959778
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:10.121750
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = [
        'ansible-playbook',
        '-i', 'hosts',
        'playbooks/ping.yml',
    ]
    pbcli = PlaybookCLI(args)
    pbcli.parse()
    pbcli.run()


# Command line tool entry point is here
if __name__ == '__main__':
    pbcli = PlaybookCLI('')
    pbcli.parse()
    pbcli.run()