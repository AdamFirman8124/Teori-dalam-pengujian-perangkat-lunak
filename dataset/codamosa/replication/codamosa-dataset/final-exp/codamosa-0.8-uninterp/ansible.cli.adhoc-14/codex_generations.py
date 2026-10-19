

# Generated at 2022-06-12 20:11:55.995385
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class TestAdHocCLI(AdHocCLI):
        def get_host_list(self, inventory, subset, pattern):
            return ['localhost']

        def validate_conflicts(self, options):
            pass

        def ask_passwords(self):
            return None, None

        def _play_prereqs(self):
            return None, None, None

    cli = TestAdHocCLI()
    assert cli.run() == 0

# Generated at 2022-06-12 20:11:59.739128
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test if run() returns 0
    a = AdHocCLI()
    a.init_parser()
    a.run()

    # Test if run() returns 1
    a = AdHocCLI()
    a.init_parser()
    a.run()

# Generated at 2022-06-12 20:12:08.151410
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Disable this code as it is under construction.
    return None

    # Define parameters
    params = {'module_name': 'ping'}
    options = opt_help.create_options(params,
        {'verbosity': 0, 'module_path': '%s/lib/ansible/modules/network' % os.getcwd(), 'inventory': '%s/tests/inventory' % os.getcwd(), 'args': '-c local -m ping'})

    # Create instance
    cli = AdHocCLI(args=[], options=options)

    # Run method
    cli.run()

# Generated at 2022-06-12 20:12:10.196416
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(None)
    assert adhoc.parser
    assert not adhoc.parser.has_option('-i')

# Generated at 2022-06-12 20:12:17.610255
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ''' Unit test for AdHocCLI class run method '''

    # Check when no args are passed
    context.CLIARGS = {}
    try:
        AdHocCLI().run()
        import pytest
        pytest.fail('Expected error when no args are passed to AdHocCLI')
    except SystemExit as err:
        assert err.code == 2

    # Check when hosts are not specified in inventory
    context.CLIARGS = {'subset': 'bar:baz'}
    try:
        AdHocCLI().run()
        import pytest
        pytest.fail('Expected error when incorrectly pattern is specified')
    except AnsibleError as err:
        assert "boo doesn't exist" in str(err)

    # Check when no module is specified
    context.CLIAR

# Generated at 2022-06-12 20:12:28.035417
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    class Args:
        verbosity = 3
        subset = True
        listhosts = 'all'
        module_name = None
        module_args = 'echo hi'
        seconds = 2
        poll_interval = 2
        inventory = 'localhost,'
        ask_pass = True
        private_key_file = 'blah'
        user = 'ansible'
        become = False
        become_method = 'sudo'
        become_user = 'root'
        become_ask_pass = True
        remote_user = 'ansible'
        connection = 'ssh'
        timeout = 10
        ssh_common_args = None
        sftp_extra_args = None
        scp_extra_args = None
        ssh_extra_args = None
        poll_interval = 15
        seconds = 300

# Generated at 2022-06-12 20:12:35.371545
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(args=['test.example.com', '-m', 'setup'])
    assert adhoc
    assert adhoc.options
    assert 'test.example.com' in adhoc.args
    assert '-m' in adhoc.args
    assert 'setup' in adhoc.args
    assert not adhoc.parser
    assert not adhoc.subparsers
    assert adhoc.display

# Generated at 2022-06-12 20:12:35.937069
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:37.874581
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI('')
    assert isinstance(adhoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:12:43.652259
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.mock import patch

    # Test function first with no arguments
    # and then with all arguments populated
    for count in range(0,2):
        if count == 0:
            opt, args = AdHocCLI.parse(["localhost"])
        else:
            opt, args = AdHocCLI.parse(["localhost",  "--module-name", "shell", "-a", "foo"])

        cli = AdHocCLI(opt, args)

        with patch.object(CLI, 'run'):
            cli.run()

# Generated at 2022-06-12 20:12:59.156110
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test return code
    # Test display output
    # Test handle password prompts
    # Test get basic objects
    # Test get list of hosts to execute against
    # Test just listing hosts
    # Test verify we have arguments if we know we need em
    # Test Avoid modules that don't work with ad-hoc
    # Test construct playbook objects to wrap task
    # Test now create a task queue manager to execute the play
    pass

# Generated at 2022-06-12 20:13:05.680961
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import argparse
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.utils.display import Display
    from ansible.utils.sentinel import Sentinel
    from ansible import context

    # create parser
    parser = argparse.ArgumentParser()
    opt_help.add_runas_options(parser)
    opt_help.add_inventory_options(parser)
    opt_help.add_async_options(parser)
    opt_help.add_output_options(parser)
    opt_help.add_connect_options(parser)
    opt_help.add_check

# Generated at 2022-06-12 20:13:06.447528
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI(args=[])
    assert obj.args == []

# Generated at 2022-06-12 20:13:11.794827
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    This function is used to test run function of class AdHocCLI.
    :return: None
    '''
    ad_hoc_cli = AdHocCLI()
    assert ad_hoc_cli.run() is None

# Generated at 2022-06-12 20:13:13.183123
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(args=[])
    assert cli.parser._prog_name == 'ansible'

# Generated at 2022-06-12 20:13:24.116151
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import os
    import tempfile
    import shutil
    from ansible.module_utils.basic import AnsibleModule

    with tempfile.TemporaryDirectory(prefix='ansible_test_adhoc') as tmpdir:
        os.chdir(tmpdir)
        os.mkdir('library')
        os.mkdir('playbooks')
        os.mkdir('inventory')

        with open('library/test.py', 'w') as f:
            f.write('''\
#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = ''')


# Generated at 2022-06-12 20:13:27.111702
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli.parser._usage.strip().startswith('usage:')
    assert cli.parser._prog.strip() == 'ansible-playbook'
    assert cli.parser._description.strip().startswith('Define and run a single task')

# Generated at 2022-06-12 20:13:38.119545
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI([])
    cli.post_process_args(cli.parser.parse_args(['localhost', '-a', '"value a"', '-m', '"module1"', '-e', '"extravars1"', '-v', '-c', 'local', '--ask-become-pass', '--become-user', 'user1', '--vault-password-file', 'vault_password_file1', '--listhosts']))

    class MockDisplay(object):
        def display(self, msg):
            pass


    # TODO - test with real objects the call of run() method

    display_backup = display
    display = MockDisplay()
    assert cli.run() is None
    display = display_backup

# Generated at 2022-06-12 20:13:38.845466
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()

# Generated at 2022-06-12 20:13:41.425870
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli.name == 'ansible'
    assert cli.description == 'Ad-hoc command executor.'
    assert cli.run


# Generated at 2022-06-12 20:14:06.341897
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ''' constructor AdHocCLI argv
        argv: ansible foo.example.com -m ping --ask-pass
    '''
    adhoc_cli = AdHocCLI(['foo.example.com', '-m', 'ping', '--ask-pass'])
    adhoc_cli.parse()
    adhoc_cli.post_process_args(adhoc_cli.options)

# Generated at 2022-06-12 20:14:14.028646
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    Used to test the run method of the Ansible AdHocCLI class
    """

# Generated at 2022-06-12 20:14:24.519531
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    display = Display()
    display.verbosity = 4

    # Create an AdHocCLI object
    adhoc_cli = AdHocCLI()

    # Set context.CLIARGS

# Generated at 2022-06-12 20:14:27.869912
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # Construct python object for class AdHocCLI
    ad_hoc_cli_obj = AdHocCLI()


# Constructor of class CLI

# Generated at 2022-06-12 20:14:37.182484
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    import os

    # Make sure we can run this class
    here = os.path.dirname(os.path.abspath(__file__))
    adhoc_path = os.path.join(here, '../../../hacking/test-adhoc.py')
    adhoc_command_ansible_playbook = ['ansible-playbook', '-i', 'localhost,', adhoc_path]
    adhoc_command_bin_ansible = ['ansible', 'localhost', '-m', 'ping']

    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

    # Mock args so we can test the run method with random data
    # We'll also use this method to run adhoc

# Generated at 2022-06-12 20:14:39.617595
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """
    This is a test function to test the constructor of class AdHocCLI.
    """
    adhoc_cli = AdHocCLI()
    assert adhoc_cli

# Generated at 2022-06-12 20:14:40.908687
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:14:42.731380
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    """Test constructor of class AdHocCLI"""

    adhoc = AdHocCLI()
    assert adhoc
    assert adhoc.parser

# Generated at 2022-06-12 20:14:44.528549
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad = AdHocCLI()
    assert isinstance(ad, AdHocCLI)

# Generated at 2022-06-12 20:14:45.885408
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:15:35.678972
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # This can be more easily tested if we can mock out the CLI args,
    # but that is a problem with the current method of building the CLI.
    # Test values are based on the "bin/ansible" file.
    # Test for simple validation test on run that covers one code path
    # that runs in ad-hoc CLI.
    cli = AdHocCLI()
    try:
        cli.post_process_args(dict(module_name="import_tasks", module_args=""))
        assert(False)
    except AnsibleOptionsError:
        pass

# Generated at 2022-06-12 20:15:45.043376
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.cli import CLI
    from ansible.cli.adhoc import AdHocCLI

    c = AdHocCLI(args=[])
    c.parse()

    options = c.options


# Generated at 2022-06-12 20:15:53.999804
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class Options(object):
        verbosity = 0
        module_name = 'command'
        module_args = ''
        forks = 10
        listhosts = False
        subset = None
        inventory = ''
        pattern = '127.0.0.1'
        one_line = False
        tree = None
        asksub_pass = False
        ask_sudo_pass = False
        remote_user = 'root'
        connection = 'ssh'
        timeout = 10
        ssh_common_args = ''
        sftp_extra_args = ''
        scp_extra_args = ''
        ssh_extra_args = ''
        become = False
        become_method = 'sudo'
        become_user = None
        check = False
        extra_vars = []
        playbook = ''
        passwords = {}
        private

# Generated at 2022-06-12 20:15:55.388786
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert adhoc_cli is not None

# Generated at 2022-06-12 20:15:59.340457
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    try:
        assert AdHocCLI().get_optparser() == CLI().get_optparser()
    except AssertionError:
        raise AssertionError('assertion error: AdHocCLI()')
    else:
        print('AdHocCLI is working fine')


if __name__ == '__main__':
    test_AdHocCLI()

# Generated at 2022-06-12 20:16:01.886381
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc_cli = AdHocCLI()
    adhoc_cli.run()

# Generated at 2022-06-12 20:16:02.747195
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()


# Generated at 2022-06-12 20:16:03.983250
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    a = AdHocCLI()
    assert a is not None

# Generated at 2022-06-12 20:16:13.756778
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Test for function run of class AdHocCLI
    adhoc_cli = AdHocCLI()

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    adhoc_cli.loader = DataLoader()
    adhoc_cli.options = adhoc_cli.common_parser.parse_args(['localhost', '-m', 'setup', '-a', 'filter=ansible_distribution'])
    adhoc_cli.inventory = InventoryManager(adhoc_cli.loader, adhoc_cli.options.inventory, adhoc_cli.options.host_list)

# Generated at 2022-06-12 20:16:19.888418
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:17:49.518094
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(args=[])
    assert cli.parse() == 0

# Generated at 2022-06-12 20:17:50.596226
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert cli

# Generated at 2022-06-12 20:17:51.843003
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """ Unit test to test AdHocCLI.run() """
    #ToDo

# Generated at 2022-06-12 20:17:52.652784
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()
    pass

# Generated at 2022-06-12 20:18:03.015478
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import io
    import tempfile
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.inventory.manager import InventoryManager

    # Setup Arguments

# Generated at 2022-06-12 20:18:09.695565
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # create the CLI object like bin/ansible-playbook would
    cli = AdHocCLI(args=None)
    # Set the command line options
    cli.options = context.CLIARGS
    # Set the inventory for the adhoc CLI
    context.CLIARGS["inventory"] = "test/inventory"
    # Set the host pattern for the adhoc CLI
    context.CLIARGS["args"] = "test1,"
    # Set the module_name for the adhoc CLI
    context.CLIARGS["module_name"] = "command"
    # Set the module_args for the adhoc CLI
    context.CLIARGS["module_args"] = "ifconfig"
    # Run adhoc run method
    cli.run()

# Generated at 2022-06-12 20:18:14.917205
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    ad_hoc_cli = AdHocCLI(args=['-c', 'local', '-m',
        'setup', '-a', 'filter=ansible_distribution'])
    ad_hoc_cli.run()
    """
    # TODO: Add unit test for AdHocCLI

# Generated at 2022-06-12 20:18:16.589375
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI()
    assert isinstance(adhoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:18:21.139536
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    import argparse
    class MockArgs:
        def __init__(self):
            self.module_name='ping'
            self.one_line=True
            self.verbosity=3
            self.args='localhost'
    with pytest.raises(AnsibleOptionsError):
        AdHocCLI({},ad_hoc_args=MockArgs())

# Generated at 2022-06-12 20:18:22.355341
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    adhoc.run()