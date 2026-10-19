

# Generated at 2022-06-12 20:32:49.093127
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # We use a simple playbook that reads a variable from a file and prints it out
    playbook_path = os.path.join(os.path.dirname(__file__), '../../../test/integration/playbooks/module_include_vars.yml')
    inventory_path = os.path.join(os.path.dirname(__file__), '../../../test/integration/inventory')

    # Execute the playbook
    cli = PlaybookCLI(['-i', inventory_path, playbook_path])
    exit_code = cli.run()
    assert exit_code == 0



# Generated at 2022-06-12 20:32:49.680389
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:50.227632
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:57.892323
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # test_PlaybookCLI_run : Test whether playbook is executed successfully.

    from ansible import constants as C
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager

    # set inventory
    inventory = InventoryManager(loader=None, sources=C.DEFAULT_HOST_LIST)

    # set variable manager
    variable_manager = variable_manager = combine_vars(loader=None, variables={}, include_cache=False)

    # set options
    options = context.CLIARGS
    options['connection'] = 'local'
    options['module_path'] = C.DEFAULT_MODULE_PATH
    options['forks'] = 1
    options['become'] = None
    options['become_method'] = None
    options['become_user'] = None

# Generated at 2022-06-12 20:33:06.921675
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Mock the CLIARGS
    class Struct:
        def __init__(self):
            self.listhosts = True

    context.CLIARGS = Struct()

    #Mock the Display class
    class DisplayMock:
        def __init__(self):
            self.verbosity=0
            self.display("")

    display = DisplayMock

    # Mock the loader and inventory classes
    class LoaderMock:
        def __init__(self):
            self.set_basedir("basedir")

    class InventoryMock:
        def __init__(self):
            self.list_hosts = ["192.168.56.103"]

    # Mock the variable_manager class
    class VariableManagerMock:
        def __init__(self):
            self.get_hosts = ["host-abc"]

# Generated at 2022-06-12 20:33:07.346468
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:13.820155
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # create mock objects for module dependencies
    class MockCLI(object):
        @staticmethod
        def get_host_list(inventory, subset):
            return None

    class MockAnsibleError(object):
        pass

    class MockAnsibleOptions(object):
        def __init__(self, **kwargs):
            self.connection = kwargs.get('connection')
            self.module_path = kwargs.get('module_path')
            self.forks = kwargs.get('forks')
            self.become = kwargs.get('become')
            self.become_method = kwargs.get('become_method')
            self.become_user = kwargs.get('become_user')
            self.check = kwargs.get('check')

# Generated at 2022-06-12 20:33:21.675564
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible import context
    from ansible.cli import CLI
    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.plugins.loader import add_all_plugin_dirs, plugin_loader
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    plugin_loader.cleanup_all_tmp_files()
    context._init_global_context(load_plugins=False)

    get_option = option_helpers._get_option_factories(CLI, PlaybookCLI)

    options = get_option('vault_password_file')(['/tmp/ansible_vault_passwd_file'])
    options = get_option('vault_password')(['/tmp/ansible_vault_passwd'])

# Generated at 2022-06-12 20:33:22.381491
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    raise NotImplementedError

# Generated at 2022-06-12 20:33:23.642224
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():  # noqa
    pass

# Generated at 2022-06-12 20:33:42.483822
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    display = Display()
    parser = CLI.base_parser(constants=C)
    pb = PlaybookCLI(parser)

    pb.get_opt({'--flush-cache': True, '--inventory-file': 'hosts',
                '--module-path': 'ansible_module',
                '--verbosity': 0,
                '--list-hosts': True,
                'args': ['playbook.yml']})
    pb.parser = parser
    assert pb.run() is None

# Generated at 2022-06-12 20:33:48.430664
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    v_callbacks = ['action_show', 'action_skip']

# Generated at 2022-06-12 20:33:49.032426
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:56.879211
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Create a mock display object
    display = Display()

    # Create a mock playbook object
    playbook = PlaybookCLI()

    # Create a mock parser object
    parser = CLI.base_parser('test_playbook_cli', '2.12')

    # Create a mock command line argument
    context.CLIARGS = {'listtags': True, 'subset': [], 'flush_cache': False,
                       'listhosts': False, 'listtasks': False, 'syntax': False, 'step': False,
                       'start_at_task': None, 'args': ['test.yml']}

    # Create a mock inventory object
    inventory = CLI.setup_inventory(parser, context.CLIARGS)

    loader = CLI.setup_loader()

    # Create a mock variable manager object
    variable_manager = CLI

# Generated at 2022-06-12 20:33:57.374955
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:57.843716
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:07.810512
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Define test data

    # New PlaybookCLI object with fake args
    playbook_path = os.path.join(os.path.dirname(__file__), 'playbooks')
    args = ['--inventory-file', os.path.join(playbook_path, 'hosts'),
            os.path.join(playbook_path, 'ping.yml')]
    PLAYBOOK_CLI = PlaybookCLI(args)

    # Define mock data
    host_list = ['localhost']

    # Define mock objects
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=args[1])
    variable_manager

# Generated at 2022-06-12 20:34:11.242990
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Test whether asking for passwords returns the password"""
    cli = PlaybookCLI()
    cli.base_parser = CLI.base_parser
    pass_a = cli.ask_passwords()
    assert pass_a
    assert pass_a[0] == None
    assert pass_a[1] == None

# Generated at 2022-06-12 20:34:18.058195
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''playbook_cli.py:PlaybookCLI.run()'''

    import os
    import tempfile
    import shutil
    import pytest

    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    loader = DataLoader()

    # create base objects
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create temporary directory as base for all files
    tmpdir = tempfile.mkdtemp()

    # create 'hosts' file

# Generated at 2022-06-12 20:34:19.091825
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:53.055708
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Arrange
    pbc = PlaybookCLI(['-i', 'localhost,'])
    pbc.post_process_args = lambda opts: opts
    pbc.run = lambda: None
    pbc.parser = pbc.create_parser()
    pbc.options, pbc.args = pbc.parser.parse_args('')
    pbc.validate_conflicts = lambda opts, runas_opts, vault_opts: None
    pbc.ask_passwords = lambda: "pass"

    # Act
    pbc.run()

    # Assert

# Generated at 2022-06-12 20:34:53.635807
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:55.344176
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = ['--version']
    cli = PlaybookCLI(args)
    cli.parse()

# Generated at 2022-06-12 20:35:06.072992
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins.loader import module_loader, callback_loader
    from ansible.module_utils import connection_loader
    from ansible.module_utils.facts.virt_facts import VirtFactCollector
    from ansible.parsing.dataloader import DataLoader

    loader_module_dummy = module_loader
    loader_module_dummy.add_directory("./")
    loader_callback_dummy = callback_loader
    connection_loader_dummy = connection_loader
    virt_fact_collector = VirtFactCollector()

    data_loader_dummy = DataLoader()

    assert(PlaybookCLI.run(None) == 1)

# Generated at 2022-06-12 20:35:15.035087
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    import unittest
    from unittest.mock import MagicMock, patch, call
    import gc
    import os
    import stat
    import sys
    from datetime import date
    from ansible.cli.args import optparse_helpers as opt_help
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path

# Generated at 2022-06-12 20:35:25.956986
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    env_dict={}
    playbook_cli = PlaybookCLI(env_dict)
    playbook_cli.options = { "listhosts": True, "listtasks": True, "listtags": True, "syntax": True }

    p = {
        "plays": [
            Play("some_play1", r"fqdn1:fqdn2"),
            Play("some_play2", r"fqdn1:fqdn2")
        ]
    }
    display.output = [
        {
            "action": "display",
            "arguments": {
                "msg": "** demo: {{ output_variable }} **\n"
            }
        }
    ]


# Generated at 2022-06-12 20:35:35.058638
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import json
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Generation of inventory
    host_1 = dict()
    host_1['hostname'] = 'host_1'
    host_1['port'] = '22'
    host_1['ansible_ssh_host'] = '127.0.0.1'
    host_1['ansible_ssh_pass'] = 'password'
    host_1['ansible_ssh_port'] = '22'

    host_2 = dict()
    host_2['hostname'] = 'host_2'
    host_2['port'] = '22'
    host_2['ansible_ssh_host'] = '127.0.0.1'
    host

# Generated at 2022-06-12 20:35:37.248331
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    # Without args the CLI exits
    with pytest.raises(SystemExit):
        PlaybookCLI().run()

# Generated at 2022-06-12 20:35:38.133898
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert False, "No test implemented"

# Generated at 2022-06-12 20:35:48.953071
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Initialize class PlaybookCLI
    playbook_cli = PlaybookCLI()

    # Create a new argument parser
    parser = CLI.base_parser(
        constants=C,
        usage='%prog [options] playbook.yml [playbook2 ...]',
        connect_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        inventory_opts=True,
        runtask_opts=True,
        vault_opts=True,
        fork_opts=True,
        module_opts=True,
        desc='runs Ansible playbooks, executing the defined tasks on the targeted hosts.',
        base_parser=parser,
    )


# Generated at 2022-06-12 20:36:46.980893
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #Test passing run
    playbookCLI = PlaybookCLI()
    pass


# Generated at 2022-06-12 20:36:54.731213
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import collections

    # Setup the context
    context._init_global_context(['ansible-playbook'])

    # Setup the args

# Generated at 2022-06-12 20:37:06.579841
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Configure test
    from io import StringIO
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader, sources=None, vault_password=None)
    host_list = []
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 20:37:16.459544
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI._flush_cache = lambda x, y: None

    class args:
        listtasks = False
        listtags = False
        step = False
        start_at_task = None
        verbosity = 0
        subset = None
        flush_cache = None
        diff = False
        check = None
        skip_tags = None
        start_at = None
        syntax = None
        force_handlers = False
        step_tags = None
        connection = 'ssh'
        module_path = None
        inventory = None
        become = False
        become_method = 'sudo'
        become_user = None
        become_ask_pass = False
        tags = None
        skip_tags = None
        private_key_file = None
        remote_user = None
        extra_vars = []
        extra_

# Generated at 2022-06-12 20:37:21.624659
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    import mock

    pm = PlaybookCLI(['test.yml'])
    # Return the object which have been instantiated in PlaybookCLI.__init__
    pm._play_prereqs = mock.MagicMock()
    pm.post_process_args = mock.MagicMock()
    pm.ask_passwords = mock.MagicMock()

    pm.run()

# Generated at 2022-06-12 20:37:32.657685
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:37:40.234170
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class PlaybookCLI_UnitTest(PlaybookCLI):

        def __init__(self, **kwargs):
            super(PlaybookCLI_UnitTest, self).__init__(**kwargs)
            self.parser = CLI.base_parser(**kwargs)
            self.init_parser()
            self.args = self.parser.parse_args()
            self.post_process_args(self.args)
            self.parser.version = '{0} unittest'.format(self.parser.version)

    with open('./test/units/files/config_units.cfg', 'w') as conf_file:
        conf_file.write('[defaults]\nhost_key_checking=false\n')

    pb = PlaybookCLI_UnitTest()
    pb.run()

   

# Generated at 2022-06-12 20:37:44.090761
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # create base objects
    loader, inventory, variable_manager = PlaybookCLI._play_prereqs()

    # create the playbook executor, which manages running the plays via a task queue manager
    pbex = PlaybookExecutor(playbooks=['/Users/michael/dev/ansible/test/units/modules/utilities/test_module.py'],
                            inventory=inventory,
                            variable_manager=variable_manager, loader=loader)

    results = pbex.run()

    assert 0

# Generated at 2022-06-12 20:37:45.569660
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-12 20:37:49.100479
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Arrange
    import sys

    # Act
    PlaybookCLI(sys.argv).run()

    # Assert

# Generated at 2022-06-12 20:39:15.088925
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def mock_PlaybookExecutor_run(self):
        return [{'plays': [{'name': 'Got it from the environment', 'hosts': ['localhost'], 'tags': []}]}]

    def mock_PlaybookExecutor___init__(self, *args, **kwargs):
        return

    PlaybookExecutor.run = mock_PlaybookExecutor_run
    PlaybookExecutor.__init__ = mock_PlaybookExecutor___init__

    # Pass the required and optional arguments
    context.CLIARGS = {}
    context.CLIARGS['args'] = ['test.yml']
    context.CLIARGS['listtags'] = True
    context.CLIARGS['listtasks'] = True
    context.CLIARGS['check'] = False
    context.CLIARGS

# Generated at 2022-06-12 20:39:22.799485
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    Unit test for method run of class PlaybookCLI
    '''
    # Set up mock environment
    class MockDisplay(object):
        def __init__(self):
            self.verbosity = 0

        def display(self, msg):
            return msg
    mock_display = MockDisplay()
    display.__class__ = mock_display.__class__

    class MockCLI(object):
        def __init__(self):
            self.parser = None
            self.args = None
            self.passwords = None

        def ask_passwords(self):
            return self.passwords

        def _play_prereqs(self):
            return self.args

        def get_host_list(inventory, subset):
            return True


# Generated at 2022-06-12 20:39:32.443468
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import copy
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook import Play
    import ansible.playbook.play
    import ansible.utils.vars
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_path_exists

    args = [
        'ansible-playbook',
        'playbook.yml',
        'playbook2.yml'
    ]

    # create the default objects
    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager()

    # Add hosts to inventory

# Generated at 2022-06-12 20:39:37.370660
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def test_playbook_cli_run(args):
        cli = PlaybookCLI(args)


    assert test_playbook_cli_run(["playbook.yml", "playbook2.yml"]) == None

# Generated at 2022-06-12 20:39:45.035723
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Arrange
    playbook_path = "fake/playbook.yml"

# Generated at 2022-06-12 20:39:49.924405
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(args=["tests/fixtures/playbooks/ansible.cfg", "tests/fixtures/playbooks/simple-playbook.yml"])
    cli.parse()
    assert PlaybookCLI.run(cli) == 0

# Generated at 2022-06-12 20:39:58.150684
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:40:08.297059
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook.play import Play
    from io import StringIO
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    import tempfile
    import pytest

    # Create the object
    pb = PlaybookCLI()
    # Create CLI arguments
    args = pb.parser.parse_args([])
    # Create the context
    context.CLIARGS = args

    # Create a test inventory
    output = StringIO()
    config_data = {
        'plugin': 'memory',
        'host_list': [None],
    }
    # Create the inventory

# Generated at 2022-06-12 20:40:19.054266
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader

    mock_args = [
        'ansible-playbook',
        '--connection', 'local',
        '--inventory', 'localhost,',
        '--module-path', './lib/ansible/modules',
        '--extra-vars', '@test.yml',
        'mock.yml'
    ]

    display = Display()
    cli = CLI(args=mock_args)

# Generated at 2022-06-12 20:40:23.681242
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # From https://github.com/ansible/ansible/blob/devel/test/units/cli/test_cli_playbook_run.py
    import json
    import os
    import shutil
    import tempfile
    import yaml
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.cli.playbook import PlaybookCLI
    from ansible.utils.display import Display
    loader = DataLoader()
    display = Display()
    display.verbosity = 2
    display.display("CWD: " + os.getcwd())

# Generated at 2022-06-12 20:41:46.753258
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options(object):
        pass

    context.CLIARGS = Options()
    context.CLIARGS.flush_cache = True
    context.CLIARGS.listtasks = True
    context.CLIARGS.listtags = True
    context.CLIARGS.verbosity = 3
    context.CLIARGS.args = ['local/sample-playbook.yml']

    instance = PlaybookCLI(context.CLIARGS, 'local')
    instance.run()

# Generated at 2022-06-12 20:41:47.342395
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass # TODO

# Generated at 2022-06-12 20:41:48.575590
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # FIXME: add another test case?
    pass


# Generated at 2022-06-12 20:41:58.841207
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Setup test variables
    options = context.CLIARGS
    options['verbosity'] = 5
    options['listhosts'] = False
    options['listtasks'] = False
    options['listtags'] = False
    options['syntax'] = False
    options['connection'] = 'ssh'
    options['module_path'] = '/path/to/module'
    options['forks'] = 9999
    options['become'] = True
    options['become_method'] = 'sudo'
    options['become_user'] = None
    options['remote_user'] = 'some_user'
    options['private_key_file'] = 'some_key'
    options['ssh_common_args'] = 'some_args'
    options['ssh_extra_args'] = 'some_extra_args'

# Generated at 2022-06-12 20:42:07.124556
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Examples of tests that can be run
    p = PlaybookCLI()

    # # PlaybookExecutor.run() is called
    # p._flush_cache("inventory", "variable_manager")
    # p._play_prereqs()
    # p.ask_passwords()

    # TODO: put more tests here.
    #
    # More examples of tests
    # ---------------------------------------------------------------
    #
    # # we can mock out any method we want, and WindowsError is not defined in
    # # some places
    # class WindowsError(Exception):
    #     pass
    #
    # # we can mock out any method we want, and not cause an exception
    # # monkeypatch is the tool to do this
    # @mock.patch.object(PlaybookCLI, '_flush_cache')
    # def test_

# Generated at 2022-06-12 20:42:10.506508
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    with pytest.raises(RuntimeError) as excinfo:
        class MyPlaybookCLI(PlaybookCLI):
            def run(self):
                raise RuntimeError("oops")
        MyPlaybookCLI().run()

    assert str(excinfo.value) == 'oops'

# Generated at 2022-06-12 20:42:16.652466
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Create local objects for PlaybookCLI.run()
    class PlaybookCLI_run():
        def __init__(self, loader, inventory, variable_manager, passwords, results=[]):
            self.loader = loader
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.passwords = passwords
            self.results = results

        def run(self):
            return self.results

    loader_obj = PlaybookCLI_run('loader', 'inventory', 'variable_manager', 'passwords')
    loader = PlaybookCLI_run()
    loader.loader = loader_obj

    # Call function using local objects
    results = loader.run()
    assert results == loader_obj.results

# Generated at 2022-06-12 20:42:24.772307
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass
#    from ansible.executor.task_queue_manager import TaskQueueManager
#
#    ##################################################################
#
#    # this is the standard playbook execution pathway
#
#    playbook = 'playbook.yml'
#
#    variable_manager.extra_vars = load_extra_vars(loader=None, options=context.CLIARGS)
#    passwords = {}
#
#    pbex = PlaybookExecutor(playbooks=[playbook], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords=passwords)
#    results = pbex.run()
#
#    ##################################################################
#
#    # this is the standard playbook execution pathway
#    from ansible.executor.playbook_executor import PlaybookExecutor
#
#    playbook_path