

# Generated at 2022-06-12 20:32:44.123207
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = ['ansible-playbook', '--help']
    instance = CLI(args)
    out = instance.parse()
    assert isinstance(out, dict)

# Generated at 2022-06-12 20:32:54.321642
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options(object):
        verbosity = 0
        listhosts = False
        listtasks = False
        listtags = False
        subset = None
        syntax = False
        connection = None
        module_path = None
        forks = 5
        remote_user = None
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = None
        become_user = None
        become_ask_pass = False
        check = False
        inventory = None
        flush_cache = False
        sudo = False
        sudo_user = None
        sudo_pass = False
        extra_vars = None
        extra_vars_file = None
        vault

# Generated at 2022-06-12 20:32:55.069173
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:04.405729
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    data_loader = DataLoader()
    display = Display()
    options = CLI.base_parser(
        usage="%prog [options] playbook.yml [playbook2 ...]",
        desc="Runs Ansible playbooks, executing the defined tasks on the targeted hosts.")

    cli_options = options.parse_args('')
    context.CLIARGS = cli_options
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory

# Generated at 2022-06-12 20:33:08.934201
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    def run_method(*args):
        pass

    def ask_passwords(*args):
        pass

    def _play_prereqs(*args):
        pass

    class CommandLine:
        options = None

    class Context:
        CLIARGS = CommandLine()

    PlaybookCLI.run = run_method
    PlaybookCLI.ask_passwords = ask_passwords
    PlaybookCLI._play_prereqs = _play_prereqs
    context.CLIARGS = CommandLine()

# Generated at 2022-06-12 20:33:10.686406
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass

# Generated at 2022-06-12 20:33:18.544282
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    yaml_data = ""

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=yaml_data)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    context.CLIARGS._store(['--list-hosts'])
    context.CLIARGS['listhosts'] = True

    pbc = PlaybookCLI(args=['ansible/test/utils/ansible_playbook_listhosts.yml'])
    inventory.list_hosts()
    pbc.post_process_args(context.CLIARGS)
    pbc._play_prereqs()
   

# Generated at 2022-06-12 20:33:25.013938
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager

    class TestPlaybookCLI(PlaybookCLI):
        def __init__(self, args):
            self.args = args
            super(TestPlaybookCLI, self).__init__()

        def _play_prereqs(self):
            loader = self._loader()
            if self.args['force_hosts']:
                inventory = InventoryManager(loader=loader, sources=self.args['hosts'])
            else:
                inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)

            variable_manager = self._variable_manager(loader=loader, inventory=inventory)

            return (loader, inventory, variable_manager)


# Generated at 2022-06-12 20:33:36.324828
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test with correct arguments
    class TestPlaybookCLI(PlaybookCLI):
        def get_host_list(self, *args, **kwargs):
            return ['hostname']

        def validate_conflicts(self, options, *args, **kwargs):
            return True

        def _play_prereqs(self):
            class TestLoader:
                def set_basedir(self, *args, **kwargs):
                    return True
            class TestVariableManager:
                def get_vars(self, *args, **kwargs):
                    return True
            class TestInventory:
                def get_hosts(self, *args, **kwargs):
                    return ['hostname']

                def list_hosts(self, *args, **kwargs):
                    return ['hostname']
            return TestLoader(), TestInventory

# Generated at 2022-06-12 20:33:36.951485
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:51.599158
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

	# Initialize the test objects
	cli=PlaybookCLI(['playbook.yml'])
	options = cli.parse()
	options = cli.post_process_args(options)

	# Run the test
	res = cli.run()

	# Assert the results
	assert res == 0

# Generated at 2022-06-12 20:33:58.329544
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.inventory import Inventory
    import os
    import sys
    import shutil
    import tempfile
    import ansible.constants as C

    ansible_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    sys.path.append(ansible_path)

    # create a temp directory local to the current working directory
    pwd = os.getcwd()
    tmp = tempfile.mkdtemp()

    cwd = os.path.join(pwd, tmp)
    os.chdir(cwd)


# Generated at 2022-06-12 20:34:08.304157
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:34:10.414697
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    assert(1 == 1)
    #assert(1 == 0)


if __name__ == "__main__":

    test_PlaybookCLI_run()

# Generated at 2022-06-12 20:34:10.959063
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert False

# Generated at 2022-06-12 20:34:11.479783
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:12.007053
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:12.501085
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:15.567388
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbc = PlaybookCLI([])
    pbc.run()
    # TODO: Need test case that actually provide arguments
    #pbc.run(['-i', 'test_inventory'])

# Generated at 2022-06-12 20:34:27.449191
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # FIXME: Remove this test once we can mock
    import sys
    from unittest.mock import Mock
    from unittest.mock import patch

    # create base objects
    mock_loader = Mock()
    mock_inventory = Mock()
    mock_variable_manager = Mock()

    # create the playbook executor, which manages running the plays via a task queue manager
    mock_pbex = Mock()
    mock_pbex.run.return_value = True

    patch('ansible.cli.playbook.PlaybookCLI._play_prereqs', lambda *args, **kwargs: (mock_loader, mock_inventory, mock_variable_manager)).start()
    patch('ansible.playbook.playbook_executor.PlaybookExecutor', lambda *args, **kwargs: mock_pbex).start()

   

# Generated at 2022-06-12 20:34:57.745789
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:34:59.648402
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:01.595731
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: implement test
    pass

# Generated at 2022-06-12 20:35:11.140756
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    import sys
    import textwrap
    from ansible.parsing.dataloader import DataLoader

    from ansible.cli import CLI
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # create the CLI object & parse the argv

# Generated at 2022-06-12 20:35:12.492224
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbcli = PlaybookCLI()
    pbcli.run()

# Generated at 2022-06-12 20:35:20.616396
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    module_args = {
        '_raw_params': '',
        '_uses_shell': False,
        '_uses_delegate': False,
        '_env': {'no_log': False, 'ansible_check_mode': False, 'ansible_managed': 'Ansible managed: {file}\n'},
        '_diff': True,
        '_ansible_check_mode': False,
    }
    def _display(self, msg):
        pass
    import __builtin__
    __builtin__.display = _display

# Generated at 2022-06-12 20:35:21.562165
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:30.417054
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # prepare mocks
    class Options():
        # set some defaults
        verbosity = 5
        subset = None
        inventory = None
        syntax = None
        listtasks = None
        listtags = None
        step = None
        start_at_task = None
        args = ['playbook.yml']
    options = Options()
    ansible_playbook = PlaybookCLI(args=[])
    ansible_playbook.ask_passwords = lambda: (None, None)
    (loader, inventory, variable_manager) = ansible_playbook._play_prereqs()
    pbex = PlaybookExecutor(playbooks=options.args, inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    pbex.run = lambda: []
    ansible_playbook.post_

# Generated at 2022-06-12 20:35:31.078978
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:38.994289
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import RESERVED_TASK_VARS

    b_TEST_PLAYBOOK_DIR = os.path.join(os.path.dirname(__file__), 'test_playbooks')


# Generated at 2022-06-12 20:36:43.915858
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # AssertionError raised if context.CLIARGS['flush_cache'] is not set to True
    C.CONFIG = {'flush_cache': True}
    context.CLIARGS = {'flush_cache': True}

    # AssertionError raised if context.CLIARGS['listtasks'] is not set to False
    context.CLIARGS = {'listtasks': False}

    # AssertionError raised if context.CLIARGS['listtags'] is not set to False
    context.CLIARGS = {'listtags': False}

    # AssertionError raised if context.CLIARGS['syntax'] is not set to False
    context.CLIARGS = {'syntax': False}

    # test_dir is a directory that does not exist

# Generated at 2022-06-12 20:36:53.666780
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # test case 1
    # args[0] = 'playbook.yaml'
    cli = PlaybookCLI()
    cli.run()

    # test case 2
    # args[0] = 'playbook.yaml'
    # args[1] = 'playbook.yaml'
    cli = PlaybookCLI()
    cli.run()

    # test case 3
    # args[0] = 'playbook.yaml'
    # cliargs = {"listhosts": True}
    # cliargs = {"listtags": True}
    cliargs = {"listtasks": True}
    cli = PlaybookCLI()
    cli.run()

    # test case 4
    # args[0] = 'playbook.yaml'
    # args[1] = 'play

# Generated at 2022-06-12 20:36:55.008250
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_instance = PlaybookCLI()
    test_instance.run()

# Generated at 2022-06-12 20:37:06.831752
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class TestCLI():
        def __init__(self):
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.passwords = None
            self.args = None

    cli = TestCLI()
    pb = PlaybookCLI(cli)
    cli.args = ['test_playbook.yml']

    # Case 1: when the playbook is not found
    pb.run()
    cli.args = ['test_playbook_not_found.yml']
    try:
        pb.run()
    except AnsibleError as e:
        assert "the playbook: test_playbook_not_found.yml could not be found" in str(e)

    # Case 2: when the playbook is not a file

# Generated at 2022-06-12 20:37:10.152614
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # basic test
    pbc = PlaybookCLI(["-i", "tests/inventory", "tests/playbooks/test_playbook.yml"])
    pbc.run()

# Generated at 2022-06-12 20:37:11.511534
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:11.948091
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:20.978748
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Runs the method run of class PlaybookCLI for testing. With this we can
    check if the methods run in CLI.setup_implicit_local_fact_cache and
    run_playbook are called and with the proper arguments"""
    from ansible.tests.unit.mock.loader import DictDataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class PlaybookCLITest(PlaybookCLI):

        def __init__(self):
            self.ask_passwords_called = False
            self.setup_implicit_local_fact_cache_called = False
            self.run_playbook_called = False

        def ask_passwords(self):
            self.ask_passwords

# Generated at 2022-06-12 20:37:32.035817
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    import os
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # create a simple playbook with two hosts
    test_playbook = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
    test_playbook.write("""---
- hosts: all
  tasks:
""")
    test_playbook.close()
    test_playbook = test_playbook.name

    # create an inventory file with two hosts
    test_inventory = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
    test_inventory.write("""
all:
  hosts:
    localhost:
    example.org:
""")
    test_inventory.close()

# Generated at 2022-06-12 20:37:39.835073
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import unittest
    from unittest.mock import patch
    from unittest.mock import Mock
    from ansible.cli import CLI
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionConfig
    from ansible.vars import VariableManager

    class TestCLI(CLI):
        def exe(self):
            pass

        def post_process_args(self, options):
            pass

        def run(self):
            pass

        @staticmethod
        def _flush_cache(inventory, variable_manager):
            pass

        @staticmethod
        def get_host_list(inventory, subset):
            pass

        def init_parser(self):
            pass


# Generated at 2022-06-12 20:39:56.779018
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(to_bytes("""
            ---
            - hosts: all
              tasks:
                - name: test_playbook
                  command: echo hello""", errors='surrogate_or_strict'))

    args = [f.name]

# Generated at 2022-06-12 20:39:59.283174
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbook_cli = PlaybookCLI([])
    playbook_cli.post_process_args({"listtags": True})
    assert playbook_cli.run() == 0

# Generated at 2022-06-12 20:40:09.061190
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    inventory = dict()
    variable_manager = dict()
    loader = dict()
    passwords = dict()
    runner_callbacks = {"on_start": "v1", "on_unreachable": "v2", "on_async_poll": "v3", "on_async_ok": "v4", "on_async_failed": "v5", "on_file_diff": "v6", "on_setup": "v7", "on_import_for_host": "v8", "on_not_import_for_host": "v9", "on_play_start": "v10", "on_stats": "v11"}


# Generated at 2022-06-12 20:40:19.646113
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # No arguments returns 1
    pbcli = PlaybookCLI(args=[])
    assert pbcli.run() == 1
    # Invalid host list returns 1
    pbcli = PlaybookCLI(args=['host1','host2','host3'])
    assert pbcli.run() == 1
    # No playbooks returns 1
    pbcli = PlaybookCLI(args=[])
    assert pbcli.run() == 1
    # Invalid playbook returns 1
    pbcli = PlaybookCLI(args=["./not_a_playbook.yml"])
    assert pbcli.run() == 1
    # Valid playbooks returns 0
    pbcli = PlaybookCLI(args=["./test/playbooks/playbook1.yml"])
    assert pbcli.run() == 0


# Generated at 2022-06-12 20:40:29.006038
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os
    import tempfile
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes
    import shutil
    import sys

    def _create_playbook(tmpdir, playbook_content):
        playbook_path = os.path.join(tmpdir, 'playbook.yml')

        with open(playbook_path, "w") as playbook_file:
            playbook_file.write(playbook_content)
        return playbook_path

    class DictModule(object):
        def __init__(self, module_name, module_args):
            self.module_name = module_name
            self.module_args = module_args

       

# Generated at 2022-06-12 20:40:30.611587
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:40.012554
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.mock.plugins.loader import DictModule, DictInventory
    from ansible.mock.plugins import MockModule
    from io import StringIO

    class FakePluginLoader:
        '''
        temporary plugin loader for use with the test, mocking out
        an actual plugin loader and just returning a few objects
        '''

        def __init__(self):
            self.inventories = DictInventory()
            self.modules = DictModule()
            self.callbacks = {}
            self.lookup_plugins = {}
            self.filter_plugins = {}
            self.connection_plugins = {}
            self.fragment_loader = None

    class FakeOption(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


# Generated at 2022-06-12 20:40:44.626554
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    cls = PlaybookCLI(args=['valid_playbook.yml', '--verbose'])

    def my_askpass(prompt):
        return 'test'

    def my_ask_becomepass(prompt):
        return 'test'

    cls.ask_passwords = my_askpass
    cls.ask_become_pass = my_ask_becomepass

    assert cls.run() == 0

# Generated at 2022-06-12 20:40:46.735010
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # we should be able to execute the run method on a instance
    cli = PlaybookCLI(args=[])
    assert(cli is not None)
    cli.run()
    assert(True)

# Generated at 2022-06-12 20:40:48.591271
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = ['ansible-playbook', 'test/test_playbook.yml']
    cli = PlaybookCLI(args)
    cli.parse()
    assert cli.run() == 0