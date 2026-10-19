

# Generated at 2022-06-12 20:11:46.124141
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.run()


# Generated at 2022-06-12 20:11:48.787741
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ansible_adhoc = AdHocCLI(['-m', 'ping'])
    ansible_adhoc.post_process_args(ansible_adhoc.parser.parse_args(['localhost']))
    ansible_adhoc.run()

# Generated at 2022-06-12 20:11:53.596289
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.adhoc import AdHocCLI
    x = AdHocCLI('/bin/ansible', ['localhost', '-m', 'setup'])
    x.parse()
    print(x.run())


if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:11:55.247034
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    from ansible.cli.adhoc import AdHocCLI
    assert AdHocCLI

# Generated at 2022-06-12 20:12:05.828484
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    import sys
    import pytest
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    from modules.lib.test_base import AnsibleExitJson
    from modules.lib.test_base import AnsibleFailJson
    from units.compat.mock import patch
    from units.modules.utils import set_module_args
    from units.compat import mock
    from units.compat.mock import MagicMock

    ###########################################################################
    # this is the test for AdHocCLI.run() method.
    ###########################################################################
    # inventory file path
    inventory_file_path = os.path.join(os.path.dirname(__file__))
    # Prepare args for AdHocCLI.run() method
    #

# Generated at 2022-06-12 20:12:14.744865
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from click.testing import CliRunner
    import os
    import sys
    import tempfile
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueManagerCLI
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    # save original AdHocCLI.run method
    original_run = AdHocCLI.run

    original_environ = os.environ.copy()

    # create folder for fake ansible.cfg and a fake inventory file
    temp_ansible_home = tempfile.TemporaryDirectory(prefix="ansible_")

    # create a fake

# Generated at 2022-06-12 20:12:16.220818
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    result = AdHocCLI.run(AdHocCLI())
    assert result == 0


# Generated at 2022-06-12 20:12:22.489262
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from unittest import mock
    from io import StringIO
    from ansible.playbook.play_context import PlayContext

    test_class = AdHocCLI()
    test_class.post_process_args = mock.MagicMock(return_value = None)
    test_class.ask_passwords = mock.MagicMock(return_value = (None, None))
    test_class.get_host_list = mock.MagicMock(return_value = ['localhost'])
    play_ds = test_class._play_ds('localhost', None, None)
    play = Play().load(play_ds, variable_manager = None, loader = None)
    play._prereqs = mock.MagicMock(return_value = None)

# Generated at 2022-06-12 20:12:32.509739
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class mock_TaskQueueManager():

        def __init__(self, *args, **kwargs):
            pass

        def load_callbacks(self):
            pass

        def send_callback(self, arg1, arg2):
            pass

        def run(self, arg1):
            pass

        def cleanup(self):
            pass

    class mock_Loader():

        def __init__(self, *args, **kwargs):
            pass

        def cleanup_all_tmp_files(self):
            pass

    class mock_AdHocCLI(AdHocCLI):

        def __init__(self, *args, **kwargs):
            pass

        def init_parser(self):
            pass

        def _play_ds(self, *args, **kwargs):
            pass


# Generated at 2022-06-12 20:12:41.541835
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    module_name = 'ping'
    module_args = 'test=test'
    pattern = 'all'
    seconds = 0
    poll_interval = 0

    # Create instance of class AdHocCLI
    cli = AdHocCLI(['-a', module_args, '-m', module_name, pattern])

    mocked = Mock(
        _play_prereqs=Mock(
            return_value=(Mock(), Mock(), Mock())
        ),
        get_host_list=Mock(return_value=Mock())
    )
    mocked._play_prereqs.configure_mock(return_value=(Mock(), Mock(), Mock()))
    mocked.get_host_list.configure_mock(return_value=Mock())

# Generated at 2022-06-12 20:12:54.518017
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    adhoc_cli = AdHocCLI()

    # Test 1:success
    try:
        adhoc_cli.run()
    except AnsibleOptionsError:
        pass

    #Test 2:failure
    try:
        adhoc_cli.run()
    except AnsibleOptionsError:
        pass

    #Test 3:failure
    try:
        adhoc_cli.run()
    except AnsibleOptionsError:
        pass

# Generated at 2022-06-12 20:12:56.031227
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    obj = AdHocCLI()
    obj.run()

# Generated at 2022-06-12 20:13:03.920948
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    args = [
        'cli_adhoc.py',
        '-i', 'inventory_file',
        '-m', 'my_module',
        '-a', 'my_module_args',
        'pattern'
    ]

    play_ds = {
        'name': 'Ansible Ad-Hoc',
        'hosts': 'pattern',
        'gather_facts': 'no',
        'tasks': [
            {
                'action': {
                    'module': 'my_module',
                    'args': 'my_module_args'
                },
                'timeout': C.DEFAULT_TASK_TIMEOUT
            }
        ]
    }

    with patch.object(Play, 'load', autospec=True) as mock_play_load:
        mock_play_load.return_value

# Generated at 2022-06-12 20:13:05.148612
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:13:15.578312
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """Unit test for method run of class AdHocCLI.

    This test is not a functional test. It mocks the actual functionality of the method `run`.
    It just ensures that the right methods are called with the right parameters.

    :return: Nothing
    """
    import sys
    import mock

    ad_hoc_cli = AdHocCLI(args=sys.argv[1:])
    ad_hoc_cli.init_parser()
    with mock.patch.object(ad_hoc_cli, 'post_process_args') as m_post_process_args:
        with mock.patch.object(ad_hoc_cli.parser, 'parse_args') as m_parse_args:
            m_parse_args.return_value = mock.Mock()

# Generated at 2022-06-12 20:13:16.709994
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli is not None

# Generated at 2022-06-12 20:13:24.370442
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    parser = cli.parser
    assert parser.prog == 'ansible'
    assert parser.usage == '%prog <host-pattern> [options]'
    assert parser.description == '''Define and run a single task 'playbook' against a set of hosts'''
    assert parser.epilog == '''Some actions do not make sense in Ad-Hoc (include, meta, etc)'''
    assert len(parser._positionals.title) == 1
    assert parser._positionals.title == 'positional arguments'
    assert len(parser._positionals.actions) == 1
    assert parser._positionals.actions[0].dest == 'args'
    assert parser._positionals.actions[0].metavar == 'pattern'
    assert parser._positionals.actions[0].help

# Generated at 2022-06-12 20:13:31.201134
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    test_cli = AdHocCLI()
    test_cli.init_parser()
    context.CLIARGS = test_cli.parser.parse_args('')
    assert isinstance(test_cli.run(), int)

# Generated at 2022-06-12 20:13:31.812031
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert True

# Generated at 2022-06-12 20:13:40.220560
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    sys.modules['__main__'].display = Display()
    sys.modules['__main__'].inventory = Inventory()

# Generated at 2022-06-12 20:14:00.115045
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert isinstance(cli, AdHocCLI)
    assert isinstance(cli, CLI)

# Unit tests for method init_parser of class AdHocCLI

# Generated at 2022-06-12 20:14:02.727586
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(["127.0.0.1"])

# Generated at 2022-06-12 20:14:09.002487
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import tempfile
    tmp_path = tempfile.mkdtemp()
    if os.path.exists(tmp_path):
        sys.path.insert(0, tmp_path)

# Generated at 2022-06-12 20:14:09.446434
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:21.275839
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create a dummy class to avoid AnsibleOptionsError
    class Mock_CLI(object):
        def __init__(self, args):
            self.args = args
            self.parser = Mock_Parser()

    # Create a dummy class to avoid the b_url and callback options
    class Mock_Parser(object):
        def __init__(self):
            self.add_argument = Mock()

    # Create a dummy class to avoid AnsibleOptionsError caused by args
    class Mock_AdHocCLI(AdHocCLI):
        def __init__(self, args):
            self.args = args
            self.options = Mock_Options()
            self.display = Mock()

    # Create a dummy class to avoid AnsibleOptionsError
    class Mock_Options(object):
        def __init__(self):
            self.sub

# Generated at 2022-06-12 20:14:21.878488
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:24.479735
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' ad_hoc_cli = AdHocCLI(args=None)  '''
    ad_hoc_cli = AdHocCLI(args=None)
    assert ad_hoc_cli.parser

# Generated at 2022-06-12 20:14:34.862810
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    mocker = Mocker()
    my_module_name='setup'
    my_module_args='size=10M state=present'
    my_host_pattern='myhost'
    my_forks=5
    my_connection='ssh'
    my_ssh_user='root'
    my_ssh_pass='mypass'
    my_sudo='yes'
    my_sudo_user='root'
    my_sudo_pass='mypass'


# Generated at 2022-06-12 20:14:36.847200
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    adhoc.post_process_args({})
    adhoc.run()

# Generated at 2022-06-12 20:14:45.036462
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Write a small mock playbook to use in the test
    write_playbook = open("adhoc.yml", "w")
    write_playbook.write("---\n"
                         "- hosts: all\n"
                         "  tasks:\n"
                         "    - name: Define hostname\n"
                         "      hostname: name={{ inventory_hostname }}\n"
                         "      register: result\n"
                         "...\n")
    write_playbook.close()

    # Create a mock host file
    write_host = open("hosts", "w")
    write_host.write("[all]\n"
                     "localhost\n")
    write_host.close()

    test_adhoc = AdHocCLI(["adhoc.yml", "--listhosts"])
    test_

# Generated at 2022-06-12 20:15:21.205052
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create a temporary context
    context_obj = context.CLIARGS
    context_obj['module_name'] = 'setup'
    context_obj['module_args'] = ''
    context_obj['one_line'] = False
    context_obj['listhosts'] = False
    context_obj['forks'] = 5
    context_obj['ask_pass'] = False
    context_obj['verbosity'] = 0
    context_obj['become'] = False
    context_obj['become_method'] = None
    context_obj['become_user'] = None
    context_obj['ask_become_pass'] = False
    context_obj['check'] = False
    context_obj['inventory'] = None
    context_obj['syntax'] = False
    context_obj['extra_vars'] = dict()

# Generated at 2022-06-12 20:15:21.801082
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:15:23.514634
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    ad_hoc = AdHocCLI()
    ad_hoc.run()
    '''
    assert True

# Generated at 2022-06-12 20:15:28.716606
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class TestAdHocCLI(AdHocCLI):
        def __init__(self):
            super(TestAdHocCLI, self).__init__()
            self.parser = None

        def init_parser(self):
            pass

        def ask_passwords(self):
            return (None, None)

        def post_process_args(self, options):
            return options

        def _play_prereqs(self):
            return (None, None, None)

    cli = TestAdHocCLI()
    try:
        cli.run()
    except AnsibleOptionsError:
        pass

# Generated at 2022-06-12 20:15:37.126791
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # Create instance of class AdHocCLI
    ahc = AdHocCLI(['-m', 'setup', 'localhost', 'myhost'], None)

    # Assert type of parameter self.args
    assert(type(ahc.args) == list)

    # Assert value of parameter self.args
    assert(ahc.args == ['-m', 'setup', 'localhost', 'myhost'])

    # Assert type of parameter self.parser
    assert(type(ahc.parser) == ArgumentParser)



# Generated at 2022-06-12 20:15:46.221114
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Valid values
    args = ['-i', 'hosts', '-m', 'setup', 'localhost']

# Generated at 2022-06-12 20:15:47.818086
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    unit test for method run of class AdHocCLI
    :return:
    '''
    pass

# Generated at 2022-06-12 20:15:49.498654
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=[])
    cli.run()
    return cli

# Generated at 2022-06-12 20:15:53.411964
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert adhoc
    assert adhoc.run() == 0

# Generated at 2022-06-12 20:15:58.919532
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.adhoc import AdHocCLI
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_native
    from ansible.parsing.dataloader import DataLoader

    cmd = AdHocCLI([])
    config = {'verbosity': 3, 'module_name': 'command', 'module_args': 'uptime', 'one_line': True, 'listhosts': True}
    cmd.options = config

    # AdHocCLI._tqm can't be set, otherwise it won't be tested
    if hasattr(cmd, '_tqm'):
        del cmd._tqm

    # need to override display so there is something to check in the results
    display = Display()
    display.verbosity = 3


# Generated at 2022-06-12 20:17:12.743326
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    my_adhoc_command_line = AdHocCLI(['ping'])
    res = my_adhoc_command_line.run()
    assert res == 0

# Generated at 2022-06-12 20:17:14.520337
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI(args='')
    assert adhoc_cli

# Generated at 2022-06-12 20:17:24.522686
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys

    class MockCLIArgs(object):
        def __init__(self):
            self.pattern = "all"
            self.forks = 5
            self.verbosity = 0
            self.ask_vault_pass = False
            self.vault_password_files = None
            self.new_vault_password_file = None
            self.ask_pass = False
            self.private_key_file = None
            self.remote_user = None
            self.connection = "ssh"
            self.timeout = 10
            self.ssh_common_args = None
            self.sftp_extra_args = None
            self.scp_extra_args = None
            self.ssh_extra_args = None
            self.poll_interval = 15
            self.seconds = 10
            self.check

# Generated at 2022-06-12 20:17:34.162922
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    def _ask_passwords_mock_func(*args, **kwargs):
        return '', None

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    test = AdHocCLI()
    inventory = InventoryManager(None, None)
    variables = VariableManager(loader=None)
    test._play_ds = lambda x, y, z: 'DummyPlayDSValue'
    test.ask_passwords = _ask_passwords_mock_func

    test.run(pattern='pattern', inventory=inventory, variables=variables, async_val=None,
             poll=None, subset=None, listhosts=None, verbosity=0, sshpass='sshpass',
             becomepass='becomepass', one_line=None, tree=False)

    test.run

# Generated at 2022-06-12 20:17:34.701550
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:17:43.056188
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.adhoc import AdHocCLI

    yaml_data = """
    ---
    - hosts: localhost
      gather_facts: no
      connection: local
      tasks:
       - test: echo "hello world"
    """
    yaml_file = '/path/to/all.yml'
    with open(yaml_file, 'w') as f:
        f.write(yaml_data)

    ansible_cli = AdHocCLI()

    # test run()
    result = ansible_cli.run()
    assert result == 0

    # test run() again
    result = ansible_cli.run(['-a', yaml_file])
    assert result == 0

# Generated at 2022-06-12 20:17:45.644520
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()


test_AdHocCLI_run()

# Generated at 2022-06-12 20:17:46.526786
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:17:55.545567
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    # test instance is created successfully
    adhoc_cli = AdHocCLI(['/usr/bin/ansible', 'localhost', '-m', 'command', '-a', 'uptime', '--listhosts'])
    assert adhoc_cli._play_context.module_name == 'command'
    assert adhoc_cli._play_context.module_args == 'uptime'
    assert adhoc_cli._display.verbosity == 3
    assert adhoc_cli._display.verbosity_options == {}
    assert adhoc_cli._display.display('test') == None
    assert adhoc_cli._display.warning('test') == None


# Generated at 2022-06-12 20:17:56.509841
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()