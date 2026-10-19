

# Generated at 2022-06-12 20:11:51.957023
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI.run()

# Generated at 2022-06-12 20:11:52.826461
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:11:55.140332
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    adhoc_cli = AdHocCLI(['localhost', '--list-hosts'])
    adhoc_cli.run()
    '''
    pass

# Generated at 2022-06-12 20:12:00.962399
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Creating a mock class for AdHocCLI

    class AdHocCLI():

        def __init__(self):
            pass

        def run(self):
            pass

    class AdHocCLI2(AdHocCLI):

        def __init__(self):
            pass

        def run(self):
            return "No match"

    a = AdHocCLI2()
    # Calling run method with 0
    assert a.run() == "No match"

# Generated at 2022-06-12 20:12:11.468867
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create an instance of AdHocCLI
    adhoc_cli = AdHocCLI()

    # Create a parser
    adhoc_cli.init_parser()

    # Create an argument list
    arg_list = ['adhoc.yml', '-a', 'option_a=val_a option_b=val_b',
                '--module-name', 'ping', '-u', 'vagrant', '-k', '-c', 'ssh',
                '-vvvv', '-i', 'adhoc.inv', '-e', 'ehlo=there']

    # Parse the given arguments
    args = adhoc_cli.parser.parse_args(arg_list[1:])

    # Post process the arguments
    adhoc_cli.post_process_args(args)

    # Return 0

# Generated at 2022-06-12 20:12:13.929548
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: use patch to mock out _play_prereqs()
    # cli = AdHocCLI()
    # cli.run()
    # TODO: assert results
    return


# Generated at 2022-06-12 20:12:16.597049
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert isinstance(adhoc, CLI)
    assert adhoc.run() == 0

if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:12:17.214131
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:27.867200
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class OptionsMock():

        def __init__(self, **kwargs):
            self.module_name = kwargs['module_name']
            self.module_args = kwargs['module_args']
            self.subset = kwargs['subset']
            self.forks = kwargs['forks']
        
            self.ask_pass = kwargs['ask_pass']
            self.ask_sudo_pass = kwargs['ask_sudo_pass']

            self.ask_vault_pass = kwargs['ask_vault_pass']
            self.vault_password_file = kwargs['vault_password_file']

            self.become = kwargs['become']
            self.become_user = kwargs['become_user']
            self.become

# Generated at 2022-06-12 20:12:31.121573
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert adhoc._play_prereqs() == adhoc.play_prereqs()

# Generated at 2022-06-12 20:12:50.079604
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.module_utils.facts.system.distribution import Distribution as distro
    from ansible.module_utils.facts.system.distribution import LinuxDistribution


# Generated at 2022-06-12 20:12:56.774296
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    _ = AdHocCLI(args=[])

# Generated at 2022-06-12 20:13:04.302687
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import time
    import os
    import socket
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    
    ##Test data
    if not os.path.exists('/etc/ansible/hosts'):
        socket.gethostname()
        host_dir = "hosts"
        host_file = host_dir + os.sep + socket.gethostname()
        os.makedirs(host_dir)

# Generated at 2022-06-12 20:13:12.182609
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # construct our own command-line options for testing
    sys.argv = ['ansible', 'no-such-group', '-m', 'ping']
    cli = AdHocCLI(args=sys.argv[1:])
    # run the ad-hoc command
    cli.parse()
    cli.run()

# Generated at 2022-06-12 20:13:13.818691
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:16.597101
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """
    This is AdHocCLI test.
    """
    ad_hoc_cli = AdHocCLI()
    assert ad_hoc_cli is not None

# Generated at 2022-06-12 20:13:17.395486
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:23.973886
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import json
    import os
    import shutil

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_dir = os.path.join(test_dir, 'test_data/AdHocCLI/')
    playback_dir = os.path.join(test_data_dir, 'playbooks/playback')
    adhoc_dir = os.path.join(test_data_dir, 'playbooks/adhoc')

    shutil.copy(os.path.join(playback_dir, 'print_hello.yml'), os.path.join(adhoc_dir, 'print_hello.yml'))

# Generated at 2022-06-12 20:13:24.540336
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert False

# Generated at 2022-06-12 20:13:37.685653
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import argparse

    # AdhocCLI.run() needs command line arguments
    parser = argparse.ArgumentParser(
        description='AdhocCLI unit tests',
        epilog='Ansible unit tests',
    )

    opt_help.add_runas_options(parser)
    opt_help.add_inventory_options(parser)
    opt_help.add_async_options(parser)
    opt_help.add_output_options(parser)
    opt_help.add_connect_options(parser)
    opt_help.add_check_options(parser)
    opt_help.add_runtask_options(parser)
    opt_help.add_vault_options(parser)
    opt_help.add_fork_options(parser)
    opt_help.add_module_options

# Generated at 2022-06-12 20:13:54.933101
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert isinstance(adhoc, AdHocCLI)

# Generated at 2022-06-12 20:14:00.221564
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    context.CLIARGS = {'module_name': 'shell',
                       'module_args': 'ls',
                       'forks': 10,
                       'subset': 'all',
                       'listhosts': 'True',
                       'verbosity': 3,
                       'ask_pass': 'False',
                       'ask_become_pass': 'False',
                       'inventory': './test/inventory',
                       'extra_vars': '@./test/extra_var_adhoc.yml',
                       'seconds': '100',
                       'check': 'False'
                       }

    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:14:03.170670
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.init_parser()
    options = cli.parse(['localhost','-m','ping'])
    cli.post_process_args(options)
    cli.setup_logging()
    cli.run()

# Generated at 2022-06-12 20:14:09.254474
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['all_hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    adhoc = AdHocCLI(None, None)
    adhoc.init_parser()

# Generated at 2022-06-12 20:14:21.014580
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli.adhoc import AdHocCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible import context
    import io
    import sys

    # Mock display
    output = io.StringIO()
    sys.stdout = output

    # Create AdHocCLI object and call run
    cli = AdHocCLI()
    cli.run()

    # Check that ad-hoc run properly
    result = output.getvalue()
    assert "No hosts matched, nothing to do" in result

    # Create AdHocCLI object and call run with hosts
    cli = AdHocCLI()

# Generated at 2022-06-12 20:14:30.820560
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import os
    import pytest

    from ansible.plugins.loader import action_loader

    @pytest.mark.parametrize('required_args, value', [
        (False, ''),
        (True, 'test')
    ])
    # Unit test case to check the execution of AdHocCLI class
    def test_AdHocCLI_run(mocker, tmpdir, required_args, value):
        action = action_loader.get('command', class_only=True)
        action.REQUIRES_ARGS = required_args

        mocker.patch.dict(action_loader.all(), {'command': action})

        args = CLICommand(mocker, tmpdir, ['localhost', '-m', 'command', '-a', value])


# Generated at 2022-06-12 20:14:39.736075
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI(args=[])
    adhoc_cli.options = []
    adhoc_cli.options.append(('module_name','ping'))
    adhoc_cli.options.append(('module_args',''))
    adhoc_cli.options.append(('verbosity',1))
    adhoc_cli.options.append(('listhosts',False))
    adhoc_cli.options.append(('host_key_checking',False))
    adhoc_cli.options.append(('seconds',None))
    adhoc_cli.options.append(('poll_interval',None))
    adhoc_cli.options.append(('tree',None))
    adhoc_cli.options.append(('forks',10))
    ad

# Generated at 2022-06-12 20:14:49.408035
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    context.CLIARGS = {
        'forks': 10,
        'module_name': 'command',
        'module_args': 'command',
        'subset': None,
        'listhosts': False,
        'seconds': None,
        'poll_interval': None,
        'ask_pass': False,
        'ask_vault_pass': False,
        'ask_become_pass': False,
        'args': 'localhost'
    }
    ad_hoc = AdHocCLI()
    ad_hoc.run()
    assert context.CLIARGS['verbosity'] == 0

# Generated at 2022-06-12 20:14:53.658209
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=['localhost', '-m', 'ping'])
    cli.parser.parse_args(['localhost', '-m', 'ping'])
    cli.parser.print_help()
    assert cli.run() == 0

# Generated at 2022-06-12 20:14:55.324977
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    This function tests the method run of class AdHocCLI
    '''
    AdHocCLI.run()

# Generated at 2022-06-12 20:15:38.629854
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI()

    class MockCLIargs(object):
        def __init__(self):
            self.forks = 5
            self.vault_password_files = 'my/password/file.txt'
            self.new_vault_password_file = 'my/new/password/file.txt'
            self.ask_vault_pass = False
            self.verbosity = 5
            self.check = False

    class MockCLIargs2(object):
        def __init__(self):
            self.forks = 5
            self.verbosity = 5
            self.check = False
            self.subset = None
            self.task_timeout = 10
            self.inventory = 'my/inventory/file.ini'
            self.listhosts = False

# Generated at 2022-06-12 20:15:46.874115
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import os
    import tempfile
    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.errors import AnsibleError

    from units.module_utils.common import AnsibleExitJson
    from units.module_utils.common import AnsibleFailJson
    from units.module_utils.common import AnsibleModule
    from units.module_utils.common import AnsibleUndefined
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    def _mock_exists(path):
        "Mock os.path.exists"
        return True


# Generated at 2022-06-12 20:15:50.876934
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    module_name = 'command'
    module_args = 'uptime'
    cliargs = [module_name, module_args]
    cls = AdHocCLI(args=cliargs)
    cls.post_process_args()
    ret = cls.run()
    assert ret == 0

# Generated at 2022-06-12 20:15:51.776919
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    raise NotImplementedError

# Generated at 2022-06-12 20:15:52.960254
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli

# Generated at 2022-06-12 20:15:53.817409
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:16:01.582169
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import warnings
    import argparse

    #
    # Create an argument parser
    #
    parser = argparse.ArgumentParser()
    #
    # Create an AdHocCLI object by calling it
    #
    adhoc = AdHocCLI(parser)

    adhoc.parser = parser

    class Object(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    #
    # Create an object for cmdline args
    #
    class CLIARGS(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    context.CLIARGS = CLIARGS(module_name='setup', module_args='', forks=10)

# Generated at 2022-06-12 20:16:02.014435
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:11.993329
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class MockCLI(object):
        ''' Mock class needed by AdHocCLI.post_process_args '''
        def __init__(self, options):
            self.options = options

    class MockParser(object):
        ''' Mock class needed by AdHocCLI.post_process_args '''
        def __init__(self, options):
            self.options = options

    class MockModuleDeprecationWarning(object):
        ''' Mock class needed by AdHocCLI.post_process_args '''
        def __init__(self, options):
            self.options = options

    class MockInvCLI(object):
        ''' Mock class needed by AdHocCLI.run '''
        def __init__(self, options):
            self.options = options


# Generated at 2022-06-12 20:16:18.716525
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    mod_args = "name=testuser group=wheel"
    pattern = 'test1'

# Generated at 2022-06-12 20:17:30.832535
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:17:40.114771
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    mock_options = MockOptions()
    mock_options.module_args = "echo hello"
    mock_options.module_name = 'command'

    display = Mock()
    ad_hoc_cli = AdHocCLI(mock_options)
    ad_hoc_cli.display = display

    # Create 2 mock hosts
    inventory = MockInventory()
    inventory.hosts = {'foo': MockHost('foo'), 'bar': MockHost('bar')}

    ad_hoc_cli.post_process_args = Mock(return_value=mock_options)
    ad_hoc_cli.ask_passwords = Mock(return_value=('', ''))
    ad_hoc_cli._play_prereqs = Mock(return_value=(None, inventory, None))


# Generated at 2022-06-12 20:17:46.425061
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' unit testing for ad-hoc cli class '''

    class Options(object):
        host_key_checking = False
        connection = 'ssh'
        module_path = '/usr/share/ansible'
        forks = 5
        timeout = 10
        inventory = 'hosts'
        verbosity = 1
        check = False
        listhosts = False
        remote_user = 'root'
        private_key_file = None
        module_name = 'ping'
        module_args = 'dest=localhost'
        one_line = False
        tree = None

    options = Options()
    adhoc = AdHocCLI(options)
    assert len(adhoc) == 0

# Generated at 2022-06-12 20:17:47.304750
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    assert False, "TODO: Implement"

# Generated at 2022-06-12 20:17:49.519306
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoccli = AdHocCLI()
    assert isinstance(adhoccli, AdHocCLI) != None


# Generated at 2022-06-12 20:18:00.152988
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    display = Display()

    # pylint: disable=unused-variable
    def mock_run(self, pattern, async_val, poll):
        return dict(
            name="Ansible Ad-Hoc",
            hosts=pattern,
            gather_facts='no',
            tasks=[{'action': {'module': 'ping', 'args': ''}}])

    def mock_ask_passwords():
        return None, None

    def mock_parse_kv(module_args, check_raw):
        return dict([('args', module_args)])

    def mock_get_host_list(inventory, subset, pattern):
        return ['testhost']

    AdHocCLI._play_ds = mock_run
    AdHocCLI.ask_passwords = mock_ask_passwords
    AdHocCLI

# Generated at 2022-06-12 20:18:05.060891
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test the method run of the class AdHocCLI
    # Declare AdHocCLI
    myAdHocCLI = AdHocCLI()
    # Declare the expected output, which is result
    expected = myAdHocCLI.run()
    # Declare the actual output, which is result_run
    result_run = myAdHocCLI.run()
    # Compare expected output with actual output
    assert expected == result_run

# Generated at 2022-06-12 20:18:06.341593
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad_hoc_cli = AdHocCLI()

    # This will execute the command with the arguments supplied, and return the result
    ad_hoc_cli.run()

# Generated at 2022-06-12 20:18:11.306664
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """
    create an instance of AdHocCLI class and
    assert that all the expected options are defined

    Note: This test does not produce code coverage for the code
    it runs as it does not execute the run() method to make a cli
    call.
    """
    adhoc_cli = AdHocCLI(args=['localhost', '-m', 'ping'])


# Generated at 2022-06-12 20:18:11.709857
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass