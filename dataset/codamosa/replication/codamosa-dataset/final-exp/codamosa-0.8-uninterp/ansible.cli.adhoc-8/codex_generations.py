

# Generated at 2022-06-12 20:12:07.565179
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad_hoc_cli = AdHocCLI()
    ad_hoc_cli.parser = ad_hoc_cli.init_parser()
    args_dict = {'module_name': 'shell', 'module_args': 'echo hi', 'listhosts': True, 'inventory': 'localhost,'}
    args = ad_hoc_cli.parser.parse_args(['localhost', '--module-name', args_dict['module_name'], '--module-args', args_dict['module_args'], '--list-hosts'], args=args_dict)
    ad_hoc_cli.post_process_args(args)
    ad_hoc_cli.parser.args = args
    result = ad_hoc_cli.run()
    assert result == 0

test_AdHocCLI_run

# Generated at 2022-06-12 20:12:10.110761
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
       Unit test for AdHocCLI class constructor
    '''
    adhoc = AdHocCLI()
    assert adhoc.parser is not None

# Generated at 2022-06-12 20:12:12.521992
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: We need to use a mock class for class AdHocCLI
    #       in order to be able to run this unit test.
    pass

# Generated at 2022-06-12 20:12:19.900994
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    def test_get_host_list(inventory, context_CLIARGS_subset, pattern):
        return ['localhost']

    setattr(AdHocCLI, 'get_host_list', test_get_host_list)

# Generated at 2022-06-12 20:12:21.279625
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli.get_optparser()

# Generated at 2022-06-12 20:12:25.442784
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys

    class TestAdHocCLI(AdHocCLI):
        def __init__(self):
            AdHocCLI.__init__(self)
            sys.argv.extend(['--list-hosts', '-t', 'all'])

        def run(self):
            AdHocCLI.run(self)

    adhoc = TestAdHocCLI()
    adhoc.parse()
    adhoc.post_process_args(adhoc.options)

    try:
        adhoc.run()
    except SystemExit:
        pass

# Generated at 2022-06-12 20:12:33.705727
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # This will fail unless the CLI is constructed with a new
    # ArgumentParser
    cli = AdHocCLI(args=[])
    if not cli.parser:
        raise AssertionError("AdHocCLI failed to create a new ArgumentParser")
    # This will fail unless we have changed the description of the CLI
    # to be a single line under 72 characters long.
    description = to_text(cli.parser.description)
    if '\n' in description or len(description) > 72:
        raise AssertionError("AdHocCLI has a multi-line description")

# Generated at 2022-06-12 20:12:40.283475
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    """
    @assumption: This test assumes that the inventory is having
    a host with name 'localhost' and it is having 'ansible_ssh'
    connection port.
    @status: This test will fail untill `vault_secret_file`
    gets implemented in `ansible.vault.VaultLib`. To make
    the test workable, hence commented out, the unit test
    `test_Passwords_ask_passwords` will have to be updated
    to return a random string as password.
    """

    AdHocCLI().run()

# Generated at 2022-06-12 20:12:46.914934
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import imp
    import os
    from collections import namedtuple

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict

    context._init_global_context(immutable_dict=ImmutableDict)

    loader = DataLoader()

# Generated at 2022-06-12 20:12:48.334061
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:57.588168
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''test_AdHocCLI_run'''


# Generated at 2022-06-12 20:13:06.798022
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI(args=[])
    simple_args = "localhost -m ping -a 'p1=v1 p2=v2'".split()
    context.CLIARGS = obj.parse(args=simple_args)
    # check attributes
    assert obj.usage == '%prog <host-pattern> [options]'
    assert obj.display_min_verbosity == 0
    assert obj.display_max_verbosity == 5
    assert obj.display_verbosity == 0

    # check context
    assert isinstance(context.CLIARGS, dict)
    assert isinstance(context.CLIARGS['module_name'], str)
    assert context.CLIARGS['module_name'] == 'ping'
    assert isinstance(context.CLIARGS['module_args'], str)


# Generated at 2022-06-12 20:13:12.773411
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    AdHocCLI - run
    """
    # Mock data
    c_ask_passwords = "ask_passwords"
    c_vars = []
    c_ifilter = None
    c_subset = False

    # Constructing our own mock object so we can assert if methods have been called
    class MockAdHocCLI(AdHocCLI):
        """
        Mock AdHocCLI
        """
        def __init__(self):
            self.ask_passwords_called = False
            self.play_prereqs_called = False
            self.get_host_list_called = False
            self.play_ds_called = False
            self.play_called = False
            self.playbook_called = False
            self.task_queue_manager_called = False

       

# Generated at 2022-06-12 20:13:23.949111
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    from ansible.cli.adhoc import AdHocCLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    context.CLIARGS._ansible_args = ['ansible', '-i', 'hosts', 'all', '-m', 'ping', '-vvvv']
    adhoc = AdHocCLI(args=context.CLIARGS._ansible_args)
    adhoc.parse()
    context.CLIARGS.pop('module_name')

    loader = DataLoader()
    passwords = dict(vault_pass='secret')
    inventory = InventoryManager(loader=loader, sources=['hosts'])

# Generated at 2022-06-12 20:13:24.948746
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: test_AdHocCLI_run
    pass

# Generated at 2022-06-12 20:13:37.727502
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import ansible.plugins.loader as plugin_loader

    # Create args
    args = ['-m', 'ping', 'localhost', '--listhosts']

    # Create test command
    cmd = AdHocCLI(args=args)

    # Test init_parser
    cmd.init_parser()

    # Test post_process_args
    cmd.post_process_args(cmd.opt)

    # Test get_host_list
    inventory = cmd.get_host_list(cmd.inventory, cmd.opt.subset, cmd.pattern)

    # Test ask_passwords
    sshpass, becomepass = cmd.ask_passwords()

    # Test _play_prereqs
    loader, inventory, variable_manager = cmd._play_prereqs()

    # Test _play_ds
    play = cmd._play_ds

# Generated at 2022-06-12 20:13:38.815905
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO
    assert True

# Generated at 2022-06-12 20:13:46.179223
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class Options(object):
        pass
    class Context(object):
        def __init__(self):
            self.CLIARGS = {
                'ask_vault_pass': False,
                'ask_become_pass': False,
                'ask_pass': False,
                'one_line': True,
                'module_name': 'ping',
                'module_args': '',
                'subset': None,
                'seconds': 10,
                'poll_interval': 15,
                'forks': 100,
                'verbosity': 3,
                'listhosts': False,
            }
        def __getitem__(self, key):
            return self.get(key)

# Generated at 2022-06-12 20:13:56.720878
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    Unit test for method run of class AdHocCLI
    '''
    # Initialize the option parser and grab the CLI options
    cli = AdHocCLI([])
    options = cli.parse()

    # save options to context so they can be read back by adhoc code
    context.CLIARGS = options

    adhoc_runner = AdHocCLI(args=[])

    # Test for invalid CLI options
    try:
        # Run without required option <host-pattern>
        adhoc_runner.run()
        assert False, "test_AdHocCLI_run() failed: Expected exception was not raised"
    except SystemExit as e:
        if e.code != 2:
            raise
    except Exception as e:
        raise

    # Test for valid CLI options
   

# Generated at 2022-06-12 20:14:05.581950
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    import sys

    class MockCLI(object):

        class MockArgs(object):
            listhosts = False
            subset = None
            verbosity = 3
            one_line = False
            module_name = None
            module_args = None
            task_timeout = None
            forks = 100
            ask_pass = False
            ask_su_pass = False
            ask_su_pass = False
            ask_vault_pass = False
            connection = 'smart'
            timeout = 10
            remote_user = None
            remote_port = None
            private_key_file = None
            become_method = None
            become_user = None
            become_ask_pass = False
            become = False
            become_ask_su_pass = False
            check = False
            diff = False
            syntax = False
            start_

# Generated at 2022-06-12 20:14:25.829521
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # We instantiate some options
    context.CLIARGS = {'module_name': 'shell', 'module_args': '-c "ls"', 'subset': None, 'listhosts': None,
                       'verbose': None, 'FORKS': None, 'verbosity': False, 'seconds': None, 'poll_interval': None}

    # Instantiate an object of class AdHocCLI
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:14:28.051416
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI(['-m', 'setup', 'localhost'])
    assert adhoc_cli is not None

# Generated at 2022-06-12 20:14:37.358258
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.base_parser = CLI.base_parser
    cli._play_prereqs = mock.MagicMock()
    cli.get_host_list = mock.MagicMock()
    cli._play_ds = mock.MagicMock()
    cli.ask_passwords = mock.MagicMock()
    cli.post_process_args = mock.MagicMock()
    cli.post_process_args.return_value = dict()
    play = mock.MagicMock()
    playbook = mock.MagicMock()
    play_ds = {'hosts': 'all', 'gather_facts': 'no', 'tasks': ['task']}
    cli._play_ds.return_value = play_ds
    loader = mock.MagicM

# Generated at 2022-06-12 20:14:45.489525
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class Options(object):
        pass

    class ContextCLIARGS(object):
        pass

    context.CLIARGS = ContextCLIARGS()
    context.CLIARGS.module_name = None
    context.CLIARGS.verbosity = False
    context.CLIARGS.module_args = None
    context.CLIARGS.subset = None
    context.CLIARGS.listhosts = False
    context.CLIARGS.seconds = None
    context.CLIARGS.poll_interval = None
    context.CLIARGS.tree = None
    context.CLIARGS.ask_vault_pass = False
    context.CLIARGS.new_vault_password_file = None
    context.CLIARGS.vault_password_file = None


# Generated at 2022-06-12 20:14:48.702315
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    unit test for method run of class AdHocCLI
    '''
    AdHocCLI_obj = AdHocCLI()
    AdHocCLI_obj.run()

# Generated at 2022-06-12 20:14:57.035313
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI(args=['ansible', 'all', '-m', 'shell', '-a', 'ls'])
    adhoc.post_process_args(adhoc.parser.parse_args())
    result = adhoc.run()
    assert result == 0


# this is mostly for testing now, as it makes little sense to write
# bin/ansible when it is not a wrapper for bin/ansible-playbook
if __name__ == '__main__':
    adhoc = AdHocCLI()
    adhoc.parse()
    adhoc.run()

# Generated at 2022-06-12 20:14:59.653837
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=['localhost', '-m', 'debug', '--args', 'msg="Hello world"'])
    result = cli.run()
    assert (result == 0)

# Generated at 2022-06-12 20:15:06.432880
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    group = AdHocCLI()

# Generated at 2022-06-12 20:15:18.700467
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class MockCLI(CLI):
        def get_host_list(self, inventory, subset, pattern):
            return []

    class MockVariableManager():
        def __init__(self):
            self.extra_vars = dict()

        def get_vars(self, loader, play, host, task, include_hostvars=False):
            return dict()

    class MockInventory():
        pass

    class MockOptions():
        def __init__(self):
            self.verbosity = 0
            self.connection = 'ssh'
            self.module_name = 'copy'
            self.module_path = 'module_path'
            self.module_args = None
            self.inventory = ''
            self.listhosts = False
            self.subset = ''
            self.diff = False
            self.ask

# Generated at 2022-06-12 20:15:29.224888
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible import context
    import pytest

    adhoc = AdHocCLI()
    adhoc.run()

    assert context.CLIARGS['module_name'] == 'shell'
    assert context.CLIARGS['module_args'] == 'echo hello'

    with pytest.raises(AnsibleOptionsError) as excinfo:
        # no args
        context.CLIARGS['module_name'] = 'user'
        context.CLIARGS['module_args'] = None
        AdHocCLI.run(adhoc)
    excinfo.match("No argument passed to user module")

    # bad action
    with pytest.raises(AnsibleOptionsError) as excinfo:
        context.CLIARGS['module_name'] = 'include'
        context.CLIAR

# Generated at 2022-06-12 20:16:02.126027
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:02.713782
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:12.628052
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    from ansible.module_utils import basic
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    mock_options = basic.AnsibleOptions(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
                                        become_method=None, become_user=None, check=False, diff=False, verbosity=3)

    mock_loader = DataLoader()
    mock_vault_secrets = VaultLib(password_files=[])
    mock_variable_manager = VariableManager(loader=mock_loader, inventory=None, vault_secrets=mock_vault_secrets)


# Generated at 2022-06-12 20:16:13.124801
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:22.665736
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    #
    # Test 1: Error occurs in post_process_args
    #
    options = opt_help.AdHocCLIOptions()
    options.verbosity = 0
    options.module_name = 'ping'
    options.module_args = 'cmd'
    options.args = 'test-host'
    options.one_line = False
    options.tree = None
    options.listhosts = False
    options.subset = None
    options.ask_vault_pass = False
    options.vault_password_files = []
    options.new_vault_password_file = None
    options.ask_pass = False
    options.ask_su_pass = False
    options.ask_sudo_pass = False
    options.ask_sudo_exe = None
    options.become = False
    options

# Generated at 2022-06-12 20:16:31.801803
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    Returns true when:
    - Trying to run with invalid module, raising AnsibleOptionsError
    - Trying to run with async and poll, raise AnsibleOptionsError
    - Trying to run with missing --module-args and MODULE_REQUIRE_ARGS is True, raise AnsibleOptionsError
    - Trying to run with module in C.MODULE_REQUIRE_ARGS, raise AnsibleOptionsError
    - Trying to run with module in C._ACTION_IMPORT_PLAYBOOK, raise AnsibleOptionsError
    - Trying to run with playbook name as a host pattern, raise AnsibleOptionsError
    - Trying to run with no hosts, return 0
    - Trying to run with valid hosts, return 0
    """
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-12 20:16:42.267589
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''ansible ad-hoc cli run unit test'''

    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import os
    import json
    import copy

    ##############
    # Make testable
    #
    # - Replace stdout_callback with minimal
    # - Make data files
    ##############

    options = copy.deepcopy(C.CLIARGS)
    options['stdout_callback'] = 'minimal'


# Generated at 2022-06-12 20:16:49.878380
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:16:51.199398
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Class is only used in CLI, therefore is not tested
    pass

# Generated at 2022-06-12 20:16:52.052099
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    res = AdHocCLI().run()
    assert isinstance(res, int)

# Generated at 2022-06-12 20:18:19.362703
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.utils.display import Display
    from ansible import constants
    from ansible.module_utils._text import to_text
    from ansible.parsing.splitter import parse_kv
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.cli.arguments import option_helpers as opt_help
    opt_help.add_runas_options(AdHocCLI.parser)
    opt_help.add_inventory_options(AdHocCLI.parser)
    opt_help.add_async_options(AdHocCLI.parser)
    opt_help.add_output_options(AdHocCLI.parser)
    opt_help.add_

# Generated at 2022-06-12 20:18:19.895353
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:18:27.027327
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    context._init_global_context(args=['', '', '-i', 'hosts', '-m', 'ping', 'localhost'])
    options = context.CLIARGS
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=options['inventory_file'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    cli = AdHocCLI()
    r = cli.run()
    print(r)

if __name__ == "__main__":
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:18:27.617375
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:18:30.209487
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """ this is more of an integration test since it uses self._play_prereqs() """
    test_adhoc = AdHocCLI(['-i', 'localhost'])
    test_adhoc.run()

# Generated at 2022-06-12 20:18:31.686876
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cls = AdHocCLI()
    assert cls is not None


# Generated at 2022-06-12 20:18:38.237762
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # config options will be used from test/utils/pytest.ini
    # we need to create a parser object and then put fake args in so we can get them back
    parser = AdHocCLI()
    parser.init_parser()
    parser.options, parser.args = parser.parser.parse_known_args([])

    # create a dictionary with base options
    context.CLIARGS = dict(connection='local',
                           forks=100,
                           become=False,
                           become_method=None,
                           become_user=None,
                           check=False,
                           diff=False,
                           listhosts=False,
                           listtasks=False,
                           listtags=False,
                           verbosity=3)

    # create a dictionary of subsets

# Generated at 2022-06-12 20:18:46.601713
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.vars.manager import VariableManager
    import pytest
    cli = AdHocCLI(args=['-i', 'localhost,'])
    cli.parse()
    assert hostvars is not None
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._extra_vars = {}
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost,']))
    play_ds = cli._play_ds('localhost', None, None)

# Generated at 2022-06-12 20:18:51.281013
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    ansible_options = ["AdHocCLI", "ALL", "-m", "ping"]

    # saving and restoring of command line arguments is necessary
    # since tests may invoke other tests which also use command line
    # arguments and we do not want to interfere with their processing.
    saved_options = sys.argv
    sys.argv = ansible_options

    try:
        adhoc_cli = AdHocCLI()
        adhoc_cli.parse()
        exit_code = adhoc_cli.run()
    finally:
        sys.argv = saved_options

    assert exit_code == 0

# Generated at 2022-06-12 20:18:52.569611
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli