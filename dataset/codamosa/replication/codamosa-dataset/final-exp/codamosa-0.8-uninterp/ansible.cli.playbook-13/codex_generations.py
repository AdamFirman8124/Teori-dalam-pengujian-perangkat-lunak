

# Generated at 2022-06-12 20:32:41.412578
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: implement test_PlaybookCLI_run
    pass

# Generated at 2022-06-12 20:32:45.352342
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Unit tests must use the CLI object
    args = [
        '--list-hosts',
        '-vvv',
        'test/fixtures/playbook/playbook.yml',
    ]
    cli = PlaybookCLI(args)
    cli.parse()
    cli.run()

# Generated at 2022-06-12 20:32:52.474706
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    This function tests the run function of ansible.cli.playbook.PlaybookCLI.
    '''
    mock_cli = CLI(['ansible-playbook', 'playbook.yml'], '0.0.0.0')
    mock_cli.parse()
    context.CLIARGS = mock_cli.options

    mock_class = PlaybookCLI(mock_cli.args, mock_cli.options)
    result = mock_class.run()
    assert result == 0

# Generated at 2022-06-12 20:32:59.847210
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cls = PlaybookCLI(['echo'])
    # set hostlist to initial state
    hostlist = context.CLIARGS['subset']

    # true - hosts in subset
    # false - there are no hosts in subset
    context.CLIARGS['subset'] = ['localhost']
    assert cls._run() == 0
    context.CLIARGS['subset'] = []
    context.CLIARGS['listhosts'] = True
    assert cls._run() == 0
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['listtags'] = True
    assert cls._run() == 0
    context.CLIARGS['listtags'] = False
    context.CLIARGS['syntax'] = True
    assert cls._run() == 0


# Generated at 2022-06-12 20:33:08.125233
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # this is copied from the end of the file where it is not reachable from
    # other modules
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager

    # create test objects

# Generated at 2022-06-12 20:33:13.896432
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Note: slightly wrong, this is written so that implicit localhost manages passwords
    sshpass = None
    becomepass = None
    passwords = {}

    PlaybookCLI.ask_passwords = lambda: (sshpass, becomepass)
    PlaybookCLI._play_prereqs = lambda self: [None, None, None]
    PlaybookCLI.get_host_list = lambda self, inventory, subset: None
    PlaybookCLI._flush_cache = lambda self, inventory, variable_manager: None

    from collections import namedtuple

    mock_result = namedtuple('MockResult', ['playbook', 'plays'])
    mock_play = namedtuple('MockPlay', ['_included_path', 'hosts', 'name', 'tags'])

    mock_play._included_path = None
    mock_play

# Generated at 2022-06-12 20:33:21.730315
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    print("In test_PlaybookCLI_run")
    loader = DataLoader()
    variable_manager = VariableManager()
    list_of_hosts = [Host(name='localhost', port=22)]
    list_of_groups = [{"name": "localhost", "hosts": ["localhost"]}]
    inventory = InventoryManager(loader=loader, sources=list_of_groups)
    inventory.add_group('localhost')
    inventory.add_host(Host(name='localhost', port=22))
    variable_manager._extra_vars = {"ansible_ssh_pass": "password"}
    playbook_

# Generated at 2022-06-12 20:33:31.455425
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # create a mock of the option parser
    class MockOP():
        def __init__(self):
            self.verbosity = True

    p = PlaybookCLI()

    # create a mock of class Host
    class MockH():
        def get_name(self):
            return 'test'
        def get_variables(self):
            return {}

    # create a mock of class Host
    class MockI():
        def __init__(self):
            self.get_hosts = lambda x: [MockH()]

    # create a mock of class VariableManager
    class MockVM():
        def get_host_variables(self, host):
            return {}
        def get_vars(self, play):
            return {}
        def clear_facts(self, hostname):
            return

    # create a mock of

# Generated at 2022-06-12 20:33:38.662770
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def test_PlaybookExecutor_run():
        class PlaybookCLI:
            def _play_prereqs(self):
                return (loader, inventory, variable_manager)
            def ask_passwords(self):
                return (sshpass, becomepass)
            def validate_conflicts(self, options, runas_opts=True, fork_opts=True):
                pass
            def run(self):
                pass
    test_cli = PlaybookCLI()
    test_cli.run()

# Generated at 2022-06-12 20:33:40.957723
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run()

# Generated at 2022-06-12 20:34:00.566192
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    import shutil
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host_list = '''
    localhost ansible_connection=local ansible_python_interpreter="/usr/bin/env python"
    '''

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=host_list)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    test_playbook_dir = tempfile.mkdtemp()

    test_playbook_path = os.path.join(test_playbook_dir, 'test_playbook.yml')

# Generated at 2022-06-12 20:34:01.624857
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI()
    cli.run()

# Generated at 2022-06-12 20:34:11.848751
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Initialization
    import os
    context.CLIARGS['verbosity'] = 2
    context.CLIARGS['syntax'] = False
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['listtasks'] = False
    context.CLIARGS['listtags'] = True
    context.CLIARGS['step'] = False
    context.CLIARGS['start_at_task'] = None
    context.CLIARGS['args'] = [os.path.join(os.path.dirname(__file__), 'data', 'test.yml')]

    # Test with all parameters set to False
    try:
        PlaybookCLI.run()
    except KeyboardInterrupt:
        pass

    # Test with listtasks set to True
    context.CL

# Generated at 2022-06-12 20:34:14.336805
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    sys.argv = ['ansible-playbook', '-i', 'hosts', '--list-hosts', 'playbook.yml']
    cli = PlaybookCLI()

    cli.run()



# Generated at 2022-06-12 20:34:15.212910
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass

# Generated at 2022-06-12 20:34:15.778156
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:27.673062
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import pytest

    class MockCmd():
        pass

    # needed so that the local host is ignored when we search for implicit localhost
    sys.argv = ['/usr/bin/ansible-playbook', 'test']
    ac_obj = MockCmd()
    ac_obj.playbook = 'test'
    ac_obj.listhosts = False
    ac_obj.listtasks = False
    ac_obj.listtags = False
    ac_obj.syntax = False
    ac_obj.connection = 'ssh'
    ac_obj.timeout = 30
    ac_obj.forks = 10
    ac_obj.remote_user = None
    ac_obj.private_key_file = None
    ac_obj.ssh_common_args = None

# Generated at 2022-06-12 20:34:35.825225
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create base objects
    loader, inventory, variable_manager = PlaybookCLI._play_prereqs()
    passwords = {}
    # create the playbook executor, which manages running the plays via a task queue manager
    pbex = PlaybookExecutor(playbooks=context.CLIARGS['args'], inventory=inventory,
                            variable_manager=variable_manager, loader=loader,
                            passwords=passwords)
    # return result of pbex.run() for testing
    return pbex

# Testing method _play_prereqs of class PlaybookCLI without passing in the rest of the arguments

# Generated at 2022-06-12 20:34:36.597517
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:37.996846
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """ Unit test for method run of class PlaybookCLI """
    pass

# Generated at 2022-06-12 20:35:11.664322
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class TestOptions:
        verbosity = 3
        listtasks = False
        listtags = False
        step = False
        start_at_task = None
        subset = None
        connection = 'local'
        forks = 10
        check = False
        diff = False
        # tags = None
        # skip_tags = None
        # extra_vars = None
        listhosts = False
        syntax = False
        flush_cache = False
        # private_key_file = None
        # ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        # become = None
        # become_method = None
        #

# Generated at 2022-06-12 20:35:22.027055
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Unit test for method run of class PlaybookCLI
    """
    def test_args(args):
        """
        Common testcases for the args
        """
        testargs = ['ansible-playbook']
        for arg in args:
            testargs.append(arg)
        return testargs

    # Success testcases
    from ansible.playbook.play import Play

    context.CLIARGS = {}
    context.CLIARGS['check'] = False
    context.CLIARGS['connection'] = 'smart'
    context.CLIARGS['force_handlers'] = False
    context.CLIARGS['flush_cache'] = False
    context.CLIARGS['force_poll'] = False
    context.CLIARGS['listhosts'] = False
    context.CLIARGS

# Generated at 2022-06-12 20:35:30.695098
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(['--list-tasks', '--list-tags', '--start-at-task', '--step', '-k'])
    cli._play_prereqs = lambda : "prereqs"
    cli.ask_passwords = lambda : "ask_passwords"
    cli._flush_cache = lambda inventory, variable_manager: "flush_cache"


# Generated at 2022-06-12 20:35:35.766890
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli import CLI

    fake_command = CLI.base_parser(['ansible-playbook', '--list-hosts'])
    PlaybookCLI.setup_parser(fake_command)
    args = fake_command.parse_args('ansible-playbook --list-hosts'.split())
    cli = PlaybookCLI(args)
    assert cli.run() == 0

# Generated at 2022-06-12 20:35:46.537631
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os.path

    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError

    with pytest.raises(AnsibleError) as err:
        p = PlaybookCLI(['/tmp/doesnotexist'])
        p.parse()
        p.run()
    assert 'could not be found' in str(err.value)

    with pytest.raises(AnsibleError) as err:
        p = PlaybookCLI(['.'])
        p.parse()
        p.run()
    assert 'does not appear to be a file' in str(err.value)

    assert PlaybookCLI([os.path.join(os.path.dirname(__file__), 'test_data/valid.yml')]).run() == 0
    assert Playbook

# Generated at 2022-06-12 20:35:55.549907
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    inventory_path = '~/ansible/ansible/inventory'
    variable_list = [
        'ansible_connection=local',
        'ansible_python_interpreter=/usr/bin/python'
    ]

    # creating PlaybookCLI object
    playbook_cli = PlaybookCLI()

    # initialize parser
    playbook_cli.init_parser()

    # process args
    options, args = playbook_cli.parser.parse_args()

    # post process args
    playbook_cli.post_process_args(options)

    # initialize loader
    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.add_group_vars('local', {'ansible_connection': 'local'})

# Generated at 2022-06-12 20:35:58.400135
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = [ '--list-hosts' ]
    result = PlaybookCLI(args).run()
    assert result == 0

# Generated at 2022-06-12 20:35:58.931370
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:00.358064
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    play = PlaybookCLI()
    play.run()

# Generated at 2022-06-12 20:36:10.844200
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # exit codes
    SUCCESS = 0
    FAILURE = 1
    # set arguments in a dictionary
    test_args = {'listhosts': True,
                 'listtasks': True,
                 'listtags': True,
                 'step': True,
                 'start_at_task': 'do_something',
                 'args': ['playbook.yml', 'playbook2.yml']}
    # test with argv and test arguments,
    # don't use with / as path for windows
    with test_common.patchargv('/', test_args):
        test_playbook_cli = PlaybookCLI()
        ansible_args, remaining_args = test_playbook_cli.parse()
        # test post_process_args

# Generated at 2022-06-12 20:36:37.837167
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:39.315842
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    print("Not implemented!")
    assert False


# Generated at 2022-06-12 20:36:47.969098
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    print("\nTest: PlaybookCLI.run")
    print("Description: Run a simple playbook")

    import os
    import tempfile
    import shutil

    # Create a tempory directory to use as a working directory
    temp_dir = tempfile.mkdtemp()

    # Create a basic playbook in the tempory dir
    playbook_name = 'simple_playbook.yml'
    playbook_path = os.path.join(temp_dir, playbook_name)
    playbook_contents = "---\n- hosts: localhost\n  tasks:\n  - name: ping\n    ping:\n"
    with open(playbook_path, 'w') as f:
        f.write(playbook_contents)

    # Create a tempory inventory
    inventory_name = 'inventory'
    inventory_path = os

# Generated at 2022-06-12 20:36:48.821441
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: implement me
    pass

# Generated at 2022-06-12 20:37:00.038179
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    # Flag to indicate if exception thrown or not
    exception_thrown = False
    # Dict to hold the context.CLIARGS

# Generated at 2022-06-12 20:37:12.592926
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from unittest import mock

    # This test case is a complete mess.
    # 1. Mock calls to CLI.run() and CLI.post_process_args(), as they are tested separately
    # 2. As related mocks depend on each other, we need to use a side effect
    # 3. We can't use a context manager, because this side effect is called
    #    from inside another one which would hang the execution.
    test_instance = PlaybookCLI()

    # Create a mock for the side effect.
    # This object is used for preserving the context for all the side effects we need.
    class side_effect_mock(object):
        def __init__(self):
            self._main_side_effect_called = False


# Generated at 2022-06-12 20:37:13.432338
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PB = PlaybookCLI()

# Generated at 2022-06-12 20:37:23.510473
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI

    # Create playbook CI object
    pb = PlaybookCLI(args=["-i", "tests/unit/mock/inventory_explicit_list"])
    pb.parse()
    context.CLIARGS = pb.options

    try:
        exit_code = pb.run()
        assert exit_code == 0
    except AnsibleError as e:
        assert False, "AnsibleError exception should not occur in this test"

    # Test the dry-run
    context.CLIARGS['check'] = True

    try:
        exit_code = pb.run()
        assert exit_code == 0
    except AnsibleError as e:
        assert False, "AnsibleError exception should not occur in this test"

    # Test the

# Generated at 2022-06-12 20:37:25.535544
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    args = ['args']
    cli = PlaybookCLI(args)
    cli.run()

# Generated at 2022-06-12 20:37:35.536948
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    inventory = BaseInventory()
    variable_manager = BaseVariableManager()
    loader = BaseLoader()
    passwords = {}

    plugin_loader = BasePluginLoader()
    from ansible.plugins.loader import in_playbook_plugins
    plugin_loader.set_plugin_paths(in_playbook_plugins)
    plugin_loader.add_plugin_dir("/test_dir/")
    plugin_loader.add_default_directory("/test_dir2/")
    plugin_loader.find_plugins()

    pbex = PlaybookExecutor(playbooks=['playbook.yml'], inventory=inventory,
                            variable_manager=variable_manager, loader=loader,
                            passwords=passwords)

    results = pbex.run()
    assert results == 0

# Generated at 2022-06-12 20:38:58.558633
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class ModuleX(object):
        def __init__(self):
            self.ansible_connection = "local"
            self.ansible_ssh_pass = "local"

    if sys.version_info[0] < 3:
        sys.modules['ansible.modules.example_module'] = ModuleX()
    else:
        m = ModuleX()
        sys.modules['ansible.modules.example_module'] = m
        sys.modules['ansible.modules.example_module.__main__'] = m

    args

# Generated at 2022-06-12 20:39:04.301760
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:39:05.005449
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass

# Generated at 2022-06-12 20:39:07.160431
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI().run()

# Generated at 2022-06-12 20:39:17.601089
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    display = Display()
    display.verbosity = 2
    # change args, so we don't call the parser

# Generated at 2022-06-12 20:39:30.608538
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import argparse

    module = __import__('ansible.cli.playbook')
    module.constants = __import__('ansible.constants')
    module.constants.HOST_KEY_CHECKING = False
    module.constants.DEFAULT_HOST_LIST = 'test/integration/ansible_hosts'
    module.constants.DEFAULT_MODULE_PATH = 'library'

    # Need to add some ansible default paths for finding plugins
    module.constants.DEFAULT_MODULE_PATH = 'library'
    module.constants.DEFAULT_UNDEFINED_VAR_BEHAVIOR = 'warn'
    module.constants.ANSIBLE_RETRY_FILES_ENABLED = False
    module.constants.ANSIBLE_PASSLIB_BACKEND = 'auto'


# Generated at 2022-06-12 20:39:31.150456
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:42.910672
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    global display
    global context

    class LocalDisplay:
        def __init__(self):
            self.messages = {}

        def display(self, message):
            self.messages[str(message)] = 1

    class LocalContext:
        class LocalCLIARGS:
            verbosity = 0
            connection = "ssh"
            module_path = "/path/to/ansible/modules"
            forks = 10

            def __init__(self):
                self.args = {}

        def __init__(self):
            self.CLIARGS = self.LocalCLIARGS()

    display = LocalDisplay()
    context = LocalContext()

    # call the PlaybookCLI class's run function
    PlaybookCLI.run()

    # check the result

# Generated at 2022-06-12 20:39:46.851061
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_cli = PlaybookCLI()
    test_cli.post_process_args = lambda x: x
    test_cli.parser = test_cli.init_parser()
    test_cli.run()

# Generated at 2022-06-12 20:39:48.748421
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbcli = PlaybookCLI()
    pbcli.post_process_args()
    pbcli.run()

# Generated at 2022-06-12 20:42:09.213608
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    context.CLIARGS = {}
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['module_path'] = None
    context.CLIARGS['flush_cache'] = True
    context.CLIARGS['connection'] = 'local'
    context.CLIARGS['timeout'] = 10
    context.CLIARGS['remote_user'] = None
    context.CLIARGS['ask_become_pass'] = None
    context.CLIARGS['ask_vault_pass'] = None
    context.CLIARGS['vault_password_files'] = None
    context.CLIARGS['new_vault_password_file'] = None
    context.CLIARGS['output_file'] = None
    context.CLIARGS['tags'] = None


# Generated at 2022-06-12 20:42:16.486456
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.playbook import Playbook

    def _play_prereqs(self):
        loader = None
        inventory = None
        variable_manager = None
        return loader, inventory, variable_manager

    PlaybookCLI._play_prereqs = _play_prereqs
    PlaybookCLI.get_host_list = lambda self, inventory, subset: None
    PlaybookCLI.ask_passwords = lambda self: (None, None)


# Generated at 2022-06-12 20:42:17.020687
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:42:25.093643
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Preparing Mock Objects to be passed as Argument to method run of class PlaybookCLI
    class MockCLI:
        def __init__(self):
            self.versioned_formatter = None
            self.display = None

    mock_cli = MockCLI()
    class MockPlaybookCLI(PlaybookCLI):
        def __init__(self):
            self.parser = None
            self.cli = mock_cli
            self.passwords = None

        def ask_passwords(self):
            return (None, None)

        def init_parser(self):
            pass

        def post_process_args(self):
            return context.CLIARGS

        def _play_prereqs(self):
            class MockOptions:
                verbosity = 0
