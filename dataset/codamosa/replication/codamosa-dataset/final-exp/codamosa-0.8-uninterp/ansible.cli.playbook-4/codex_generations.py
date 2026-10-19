

# Generated at 2022-06-12 20:32:49.755890
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:32:57.551511
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import ansible.module_utils.basic
    import ansible.playbook.play_context

    parser = CLI.base_parser(constants=ansible.constants)
    options = parser.parse_args(['playbook.yml'])[0]
    my_display = ansible.utils.display.Display()
    options.verbosity = my_display.verbosity
    play_context = ansible.playbook.play_context.PlayContext(options=options)
    loader = ansible.parsing.dataloader.DataLoader()
    my_inventory = ansible.inventory.manager.InventoryManager(loader=loader, sources='')
    my_variable_manager = ansible.vars.manager.VariableManager(loader=loader, inventory=my_inventory)

    ansible_playbook_cli = PlaybookCL

# Generated at 2022-06-12 20:33:06.707185
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Create a fake inventory
    class TestInventory(object):
        def __init__(self):
            self.hosts = ['localhost']
        def get_hosts(self, args):
            return []

    class TestOptions(object):
        verbosity = 1
        flush_cache = True
        listhosts = False
        listtags = False
        listtasks = False
        subset = ''
        syntax = False
        become_method = 'sudo'
        become_user = 'root'

    class TestVars(object):
        def get_vars(self, play):
            return {'foo':'bar'}

    class MyCLI(PlaybookCLI):
        def _play_prereqs(self):
            return MockLoader(), TestInventory(), TestVars()


# Generated at 2022-06-12 20:33:07.102234
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:12.906103
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.cli.arguments import option_helpers as opt_help

    # Create a minimal set of arguments needed to instantiate a PlaybookCLI object
    mocker.patch.object(opt_help, "add_runas_options")
    mocker.patch.object(opt_help, "add_subset_options")
    mocker.patch.object(opt_help, "add_check_options")

# Generated at 2022-06-12 20:33:17.039735
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    s = 'The generated credential is: %(password)s'
    display.display(s)

    display.display("The module is %("
                    "password)s"
                    ".")

    display.display("The module is %("
                    "password)s"
                    "."
                    "%("
                    "password"
                    ")s")

# Generated at 2022-06-12 20:33:23.807533
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    
    context.CLIARGS = {'listhosts': False, 'listtasks': False, 'listtags': False, 'syntax': False, 'flush_cache': False, 
                       'tags': [], 'skip_tags': [], 'start_at_task': None, 'step': False, 'subset': None,
                       'args': ['test.yaml'], 'verbosity': 1}
    p = PlaybookCLI()
    p.post_process_args(context.CLIARGS)
    
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = 'tests/inventory'

# Generated at 2022-06-12 20:33:32.004877
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.cli.playbook import PlaybookCLI
    from ansible.constants import CONFIG_DEFAULTS
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible import context
    import os.path
    import sys
    import argparse


# Generated at 2022-06-12 20:33:33.579544
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert True


# Generated at 2022-06-12 20:33:42.846549
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display
    from ansible.cli.playbook.cli import PlaybookCLI
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.vars.manager import VariableManager
    display = Display()
    display.verbosity = 2
    variable_manager = VariableManager()

# Generated at 2022-06-12 20:34:00.807413
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    test_PlaybookCLI_run:
    Tests a parallel playbook run:
        - Create PlaybookCLI object
        - Set all required parameters and flags
        - Call method run
    """
    playbook = "/var/lib/awx/projects/_6__examples/playbooks/pbex.yml"

    playbook_cli = PlaybookCLI()
    playbook_cli.options.listhosts = True
    playbook_cli.options.diff = True
    playbook_cli.options.check = True
    playbook_cli.options.force_handlers = True
    playbook_cli.options.start_at_task = 'goodbye world'
    playbook_cli.options.step = True
    playbook_cli.options.syntax = False
    playbook_cli.options.forks = 10
    playbook_cli.options.bec

# Generated at 2022-06-12 20:34:01.875016
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pb = PlaybookCLI([])
    pb.run()

# Generated at 2022-06-12 20:34:04.643044
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    print("Nothing to test")
    return


if __name__ == "__main__":
    PlaybookCLI()
    test_PlaybookCLI_run()

# Generated at 2022-06-12 20:34:14.064157
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class ModuleDeprecationWarning(UserWarning):
        pass


# Generated at 2022-06-12 20:34:19.752872
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
  # Needed for test
  os.environ["ANSIBLE_CONFIG"] = "test_ansible_config.cfg"
  from collections import namedtuple
  from ansible.parsing.dataloader import DataLoader

  # Mock objects
  # args mock
  args = namedtuple("args", ['host_key_checking', 'private_key_file', 'syntax', 'connection', 'module_path',
                             'forks', 'remote_user', 'ask_pass', 'verbosity', 'check', 'extra_vars',
                             'ask_sudo_pass', 'ask_su_pass', 'diff', 'listhosts', 'listtasks',
                             'listtags', 'step', 'start_at_task', 'args'])

  # config mock
  class FakeConfig(object):
    pass


# Generated at 2022-06-12 20:34:30.903257
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible import context
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from ansible.cli import CLI
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    cli = PlaybookCLI(['-l', 'localhost', 'playbook.yml'])
    cli.parse()
    context.CLIARGS = cli.options
    context.CLIARGS['listtags'] = True
    context.CLIARGS['listtasks'] = True
    context.CLIARGS['listhosts'] = True
    context.CLIARGS['syntax'] = True
    context.CLIARGS['connection'] = 'local'
    context.CLIARGS['module_path'] = None

# Generated at 2022-06-12 20:34:41.291002
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.errors import AnsibleError

    PlaybookCLI._flush_cache = lambda inventory, variable_manager: None
    PlaybookCLI._play_prereqs = lambda self: ({'test': 1}, {'test': 2}, {'test': 3})
    PlaybookCLI.ask_passwords = lambda self: ({'conn_pass': 'test1'}, {'become_pass': 'test2'})
    CLI.get_host_list = lambda inventory, subset: None
    loader = {'test': 1}
    inventory = {'test': 2}
    variable_manager = {'test': 3}

    # Could not create PlaybookExecutor

# Generated at 2022-06-12 20:34:53.397186
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create a dummy inventory
    inventory = Inventory(loader=None, variable_manager=None, host_list=['localhost'])
    # create a dummy variable manager
    variable_manager = VariableManager(loader=None, inventory=inventory)
    # create a playbook CLI
    playbook_cli = PlaybookCLI()
    # create a fake context for passing to the playbook CLI

# Generated at 2022-06-12 20:34:54.002090
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:59.671671
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import unittest
    import mock

    # create a mock version of PlaybookCLI
    mock_cli = mock.MagicMock(spec=PlaybookCLI)
    mock_cli.run = PlaybookCLI.run

    mock_options = mock.MagicMock(spec=dict)
    mock_args = mock.MagicMock(spec=list)
    mock_args.args = ['mock_playbook.yml']

    with mock.patch.object(PlaybookCLI, 'get_optparser') as mock_get_optparser:
        mock_parser = mock.MagicMock(spec=CLI.optparser)
        mock_parser.parse_args.return_value = (mock_options, mock_args)

        mock_get_optparser.return_value = mock_parser

        # run PlaybookCL

# Generated at 2022-06-12 20:35:28.646989
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from unit.fixtures import fake_options
    from unit.fixtures import fake_loader
    from unit.fixtures import fake_inventory
    from unit.fixtures import fake_variable_manager
    from unit.fixtures import fake_PlaybookExecutor
    from unit.fixtures import fake_display

    pbcli = PlaybookCLI(args=fake_options())
    context.CLIARGS = pbcli.parser.parse_args(args=fake_options())
    pbcli_run = pbcli.run()
    assert pbcli_run == fake_PlaybookExecutor().run()

# Generated at 2022-06-12 20:35:37.640779
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Create mock argument parser
    class MockParser(object):
        def __init__(self, args):
            self.args = args

        def parse_args(self):
            return self.args

    # Create mock options
    class MockOptions:
        host_key_checking = False
        module_path = None
        remote_user = None
        connection = 'local'
        private_key_file = None
        syntax = False
        check = False
        start_at_task = None
        diff = False
        v = 0
        listhosts = False
        listtags = False
        listtasks = False
        step = False
        subset = None

    # Create mock password
    class MockPassword:
        passwd = None

    # Create mock object for sending message

# Generated at 2022-06-12 20:35:41.319501
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    module = AnsibleModule()
    module.exit_json = Mock(return_value='x')

    playbook_cli = PlaybookCLI(['--list-hosts'])
    playbook_cli.run()
    assert module.exit_json.call_count == 1


# Generated at 2022-06-12 20:35:43.742038
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    instance = PlaybookCLI()
    try:
        instance.run()
    except AnsibleError:
        assert False

# Generated at 2022-06-12 20:35:45.403479
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run()

# Generated at 2022-06-12 20:35:47.020782
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    This method tests the run() in class PlaybookCLI
    """
    # TODO implement this test
    pass

# Generated at 2022-06-12 20:35:47.587707
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:56.355392
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:36:06.868528
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os
    import mock

    from ansible.cli.playbook import PlaybookCLI, CLI
    from ansible.module_utils._text import to_bytes
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-12 20:36:16.565708
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    import ansible.cli.playbook
    import ansible.constants as C
    import ansible.playbook.play_context
    import ansible.playbook.playbook
    import ansible.utils.vars

    class MockOptions:
        def __init__(self, **args):
            self.__dict__.update(args)

    mock_args = [ '--help' ]

    # False tests
    for required_attribute in ['syntax', 'check', 'listtasks', 'listtags', 'step']:
        # Instantiate class, then remove the required attribute
        setattr(ansible.cli.playbook.PlaybookCLI, required_attribute, False)
        pb = ansible.cli.playbook.PlaybookCLI(mock_args)
        assert required_attribute in dir(pb)

# Generated at 2022-06-12 20:36:50.656944
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    display_mock = Display()
    cli = PlaybookCLI()
    cli.base_parser.return_value.parse_args.return_value = context.CLIARGS
    # Display.verbosity = options.verbosity
    display.verbosity = 0
    context.CLIARGS['listhosts'] = True
    # noinspection PyUnusedLocal
    # CLI.get_host_list(inventory, context.CLIARGS['subset'])
    context.CLIARGS['subset'] = 'all'
    # (sshpass, becomepass) = self.ask_passwords()
    # loader, inventory, variable_manager = self._play_prereqs()
    # PlaybookExecutor(self, playbooks, inventory, variable_manager, loader, passwords)
    # tracker = pbex._

# Generated at 2022-06-12 20:37:01.859588
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    import json
    import os
    import shutil
    import tempfile
    import unittest

    class TestPlaybookCLI(unittest.TestCase):

        TEST_PLAYBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'test_data', 'playbooks')

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_run(self):

            cli = PlaybookCLI(['playbook.yml'])
           

# Generated at 2022-06-12 20:37:02.922960
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:14.492808
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """PlaybookCLI - run"""

    playbook = 'tests/fixtures/commandline/ansible-playbook.yaml'

    mock_cli = PlaybookCLI()

    # setup args
    mock_cli.options = mock_cli.parser.parse_args()
    mock_cli.options.connection = 'local'
    mock_cli.options.module_path = './lib/ansible/modules/'
    mock_cli.options.forks = 10
    mock_cli.options.become = False
    mock_cli.options.become_method = 'sudo'

    # setup run function
    mock_inventory = 'tests/fixtures/hosts'
    mock_variable_manager = 'mock variable manager'
    mock_loader = 'mock loader'

# Generated at 2022-06-12 20:37:25.225848
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_args = ['-c', 'local', '-m', 'debug', '-e', 'var=value', '-e', 'var2="value with spaces"']
    cli = PlaybookCLI(args=test_args, executable='/usr/bin/ansible-playbook')
    cli.parse()

    assert context.CLIARGS['module_path']  == None
    assert context.CLIARGS['syntax']       == False
    assert context.CLIARGS['ask_vault_pass'] == False
    assert context.CLIARGS['ask_pass']     == False
    assert context.CLIARGS['vault_password_file'] == None
    assert context.CLIARGS['remote_user']  == 'root'

# Generated at 2022-06-12 20:37:35.696789
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible.executor.playbook_executor import PlaybookExecutor

    pbex_mock = PlaybookExecutor
    pbex_mock.run = lambda self: ['test_result']
    pbex_mock.__new__ = lambda cls, *args: pbex_mock
    pbex_mock.__init__ = lambda self, *args, **kwargs: None
    CLI.ask_passwords = lambda self: ('passw0rd', 'passw0rd')
    cli = PlaybookCLI(['/usr/bin/ansible-playbook', '-i', './test.inventory', 'test_playbook.yml'])
    assert cli.run() == 0


# Generated at 2022-06-12 20:37:44.317602
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options:
        verbosity = 0
        subset = None
        listhosts = False
        listtasks = False
        listtags = False
        syntax = None
        step = False
        start_at_task = None
        inventory = "/etc/ansible/hosts"
        flush_cache = False
        connection = "smart"
        module_path = None
        forks = 100
        remote_user = "root"
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = "sudo"
        become_user = None
        become_ask_pass = False
        check = None
        diff = False
        list_tasks = False


# Generated at 2022-06-12 20:37:45.114471
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    raise NotImplementedError

# Generated at 2022-06-12 20:37:56.420811
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class opts:
        tags = ['all']
        listhosts = False
        subset = None
        inventory = None
        listtasks = False
        listtags = False
        syntax = False
        start_at_task = None
        step = False
        verbosity = 0
        one_line = False
        connection = None
        remote_user = None
        ask_pass = False
        private_key_file = None
        sudo = False
        sudo_user = None
        become = False
        become_method = None
        become_user = None
        become_ask_pass = False
        ask_vault_pass = False
        vault_password_files = []
        vault_ids = []
        forks = None
        diff = False
        check = False
        extra_vars = None
        extra_vars_files

# Generated at 2022-06-12 20:38:02.744727
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Setup playbooks
    playbook_file1 = 'playbook1.yml'
    playbook_file2 = 'playbook2.yml'
    open(playbook_file1, 'a').close()
    open(playbook_file2, 'a').close()

    # Setup args
    args = ['ansible-playbook', playbook_file1, playbook_file2]

    # Setup CLIARGS
    context.CLIARGS = {'args': args[2:]}

    # Initialize PlaybookCLI
    playbook = PlaybookCLI(args)

    # Setup inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')

    # Run play


# Generated at 2022-06-12 20:38:56.768672
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def mock_ask_passwords():
        return (None, None)

    def mock_play_prereqs():
        return (None, None, None)

    context.CLIARGS = {'listhosts': False, 'listtasks': False,
                       'listtags': False, 'syntax': False,
                       'flush_cache': False, 'subset': None,
                       'step': False, 'start_at_task': None,
                       'args': ['/tmp/my_playbook.yml',
                                '/tmp/my_playbook2.yml']}

    cli = PlaybookCLI()
    cli._ask_passwords = mock_ask_passwords
    cli._play_prereqs = mock_play_prereqs
    cli.run()

# Generated at 2022-06-12 20:38:57.332429
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:05.455902
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    class Loader:
        pass

    class Inventory:
        pass

    class VariableManager:
        pass

    parser = object()
    args = object()

    cli = PlaybookCLI(parser, args)
    cli.ask_passwords = lambda: (None, None)
    cli._play_prereqs = lambda: (Loader(), Inventory(), VariableManager())


# Generated at 2022-06-12 20:39:08.030423
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Test run for PlaybookCLI"""
    pass

# Generated at 2022-06-12 20:39:18.293932
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Remove ansible.cfg from the environment
    abspath = os.path.abspath(__file__)
    cur_dir = os.path.dirname(abspath)
    if 'ANSIBLE_CONFIG' in os.environ:
        del os.environ['ANSIBLE_CONFIG']

    # Setup ansible.cfg pointing to the test directory
    os.environ['ANSIBLE_CONFIG'] = cur_dir + '/ansible.cfg'

    # Setup playbook
    playbook = cur_dir + '/test_playbook.yml'


    # Test Run with -h flag
    options = ['-h']

    pb = PlaybookCLI(args=options)
    assert pb.run() == 0

    # Test Run with --version flag
    options = ['--version']

    pb = Playbook

# Generated at 2022-06-12 20:39:20.168517
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:31.533492
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class playbook_executor:
        """ Class for mocking PlaybookExecutor """
        def __init__(self):
            self.plays = [{'playbook': None, 'plays': [None]}]


    class display:
        """ Class for mocking display """
        def __init__(self):
            self.verbosity = 0

        @staticmethod
        def display(msg):
            """ Mock method for display """
            pass

    class cli_arguments:
        """ Class for mocking cli arguments """
        def __init__(self):
            self.args = None

        def __getitem__(self, key):
            if key in self.__dict__:
                return self.__dict__[key]
            return None

    class loader:
        """ Class for mocking loader """

# Generated at 2022-06-12 20:39:43.186220
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-12 20:39:44.171121
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:39:45.503977
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:13.986258
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    raise NotImplementedError

# Generated at 2022-06-12 20:40:15.252501
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI()
    cli.run()

# Generated at 2022-06-12 20:40:15.799300
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:16.438071
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:40:23.412127
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    def ask_passwords_side_effect(obj):
        #TODO: Mocking private method is not good practice, need to look at other solutions.
        return ('sshpass', 'becomepass')

    PlaybookCLI_obj = PlaybookCLI()
    PlaybookCLI_obj.ask_passwords = ask_passwords_side_effect

    def _play_prereqs_side_effect():
        return ('loader', 'inventory', 'variable_manager')

    PlaybookCLI_obj._play_prereqs = _play_prereqs_side_effect

    def post_process_args_side_effect(options):
        return options

    PlaybookCLI_obj.post_process_args = post_process_args_side_effect


# Generated at 2022-06-12 20:40:25.536636
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import mock
    p = mock.patch.object(PlaybookCLI, 'run')
    p.start()
    p.stop()

# Generated at 2022-06-12 20:40:26.097451
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert 0

# Generated at 2022-06-12 20:40:33.194062
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Tests for the PlaybookCLI.run() method.
    """

    class TmpOptions(object):
        def __init__(self):
            self.check = False
            self.flush_cache = False
            self.listhosts = False
            self.listtags = False
            self.listtasks = False
            self.syntax = False
            self.verbosity = 0

    class TmpArgs(object):
        def __init__(self):
            self.args = None

    class TmpDisplay(object):
        def __init__(self):
            self.verbosity = 0

    class TmpInventory(object):
        def __init__(self):
            self.host_list = None
            self.groups = dict()


# Generated at 2022-06-12 20:40:38.136440
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from vcr_unittest import VCRTestCase

    class TestPlaybookCLI_run(VCRTestCase):
        def test_run(self):
            with open("test/ansible/test_playbook_cli.yml", "rb") as data:
                results = PlaybookCLI.run(data)
                self.assertIsInstance(results, int)
                self.assertEqual(results, 0)
    my_class = TestPlaybookCLI_run()
    my_class.test_run()

# Generated at 2022-06-12 20:40:46.298636
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #from ansible.module_utils.six import StringIO
    import ansible.module_utils.connection
    #ansible.module_utils.connection = mock.Mock()
    #test_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = 'C:\\Users\\akumars7\\PycharmProjects\\ansible-python\\test'
    #test_dir = r'C:\Users\akumars7\PycharmProjects\ansible-python\test'
    #playbook = os.path.join(test_dir, 'playbooks', 'playbook.yaml')
    playbook = os.path.join(test_dir, 'playbooks', 'playbook.yaml')
    #print('>>>', playbook)
    #cmd = PlaybookCLI

# Generated at 2022-06-12 20:41:38.007996
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test run method

    options = context.CLIARGS
    options['listtags'] = True
    options['listtasks'] = True
    options['listhosts'] = True

    options['connection'] = 'local'
    options['module_path'] = None
    options['forks'] = 5
    options['remote_user'] = 'root'
    options['private_key_file'] = None
    options['ssh_common_args'] = None
    options['ssh_extra_args'] = None
    options['sftp_extra_args'] = None
    options['scp_extra_args'] = None
    options['become'] = False
    options['become_method'] = 'sudo'
    options['verbosity'] = 0
    options['check'] = False
    options['syntax'] = False
    options

# Generated at 2022-06-12 20:41:38.546174
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:41:49.235518
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os
    import shutil
    import sys
    import tempfile
    import unittest

    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import plugin_loader

    # FIXME: This is a hack to prevent the _load_plugins function to
    # hang forever on an unknown plugin
    old_known_plugin_type_classes = plugin_loader.known_plugin_type_classes
    plugin_loader.known_plugin_type_classes = tuple()

    class TestPlaybookCLI(unittest.TestCase):

        def setUp(self):
            self._tmp_cwd = tempfile.mkdtemp()
            self._tmp_playbook_dir = tempfile.mk

# Generated at 2022-06-12 20:41:52.581744
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    with open('test_playbook_cli.yml', 'w') as f:
        f.write(
            """
            - hosts: all
              tasks:
                - name: run command
                  command: echo "Hello world!"
            """
        )
    cli = PlaybookCLI()
    cli.parse(['test_playbook_cli.yml'])
    cli.run()

# Generated at 2022-06-12 20:41:54.277512
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Dummy unit test for testing function run of class PlaybookCLI
    """
    assert True

# Generated at 2022-06-12 20:41:54.833630
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    pass

# Generated at 2022-06-12 20:41:55.522375
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:41:56.941391
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert False, "TODO: write your module tests here"

# Generated at 2022-06-12 20:42:05.805484
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class FakeInventory(object):

        def __init__(self, hosts):
            self._hosts = hosts

        def list_hosts(self):
            return self._hosts

    class FakeVariableManager(object):
        def __init__(self):
            return

        def clear_facts(self, hostname):
            return

    class FakeCLIARGS(dict):

        def __init__(self):
            super(FakeCLIARGS, self).__init__(flush_cache=True,
                                              listhosts=True,
                                              listtags=True,
                                              listtasks=True,
                                              subset=False,
                                              syntax=False,
                                              verbosity=0,
                                              args=['/path/to/playbook']
                                              )


# Generated at 2022-06-12 20:42:06.626467
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass