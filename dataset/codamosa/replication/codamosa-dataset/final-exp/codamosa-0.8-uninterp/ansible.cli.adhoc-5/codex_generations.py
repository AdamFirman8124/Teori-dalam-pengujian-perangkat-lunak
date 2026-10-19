

# Generated at 2022-06-12 20:11:55.781835
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    AdHocCLI class is tested for following Scenarios.
        - verifying the init_parser method for arguments
    '''

    # Case 1: AdHocCLI class is instantiated with required params
    ad_hoc_cli = AdHocCLI()

    # Case 2: AdHocCLI class is instantiated without required params
    with mock.patch('ansible.cli.AdHocCLI.init_parser'):
        ad_hoc_cli_without_params = AdHocCLI(['arg1', 'arg2'])

    # Case 3: Testing the init_parser method for expected args
    assert hasattr(ad_hoc_cli, 'args') is True
    assert hasattr(ad_hoc_cli, 'parser') is True

# Generated at 2022-06-12 20:11:57.029212
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad = AdHocCLI(None, None)
    print(ad)

# Generated at 2022-06-12 20:11:59.403726
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    ad_hoc_cli = AdHocCLI()
    assert ad_hoc_cli is not None


# Generated at 2022-06-12 20:12:00.280172
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    AdHocCLI().run()

# Generated at 2022-06-12 20:12:10.878396
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Preparing mocks
    class MyAdHocCLI(AdHocCLI):
        def _play_ds(self, pattern, async_val, poll):
            self.pattern = pattern
            self.async_val = async_val
            self.poll = poll
            self.ansible_vault_pass = None
            return 'playds'

        def _play_prereqs(self):
            self.prereqs = True
            return ('loader', 'inventory', 'variable_manager')

        def get_host_list(self, inventory, subset, pattern):
            self.inventory = inventory
            self.subset = subset
            self.pattern = pattern
            return 'hosts'

        def ask_passwords(self):
            self.ask_passwords = True
            return ('sshpass', 'becomepass')

# Generated at 2022-06-12 20:12:18.739943
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    obj = AdHocCLI()

    # test method run with module name : ping
    context.CLIARGS = {'args': 'webservers', 'module_name': 'ping', 'subset': 'webservers', 'module_args': ''}
    obj.run()
    display.verbosity = 3

    # test method run with module name : ping
    context.CLIARGS = {'subset': 'webservers', 'module_args': '', 'module_name': 'ping', 'one_line': False, 'args': 'webservers'}
    obj.run()

    # test method run with module name : ping

# Generated at 2022-06-12 20:12:22.187854
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    Unit test class
    '''

    ad_hoc_cli = AdHocCLI()
    assert isinstance(ad_hoc_cli, AdHocCLI)
    assert isinstance(ad_hoc_cli, CLI)

# Generated at 2022-06-12 20:12:22.751183
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:33.795888
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    import sys
    sys.path.append('../')

    from ansible.errors import AnsibleError, AnsibleOptionsError

    adhoc_cli = AdHocCLI()

    # Test case-1: host pattern will be tested in init_parser of class PlayCLI
    adhoc_cli.init_parser()
    host_pattern = adhoc_cli.parser.parse_args(['all'])
    assert host_pattern.args == 'all'

    # Test case-2: module name will be tested in init_parser of class PlayCLI
    adhoc_cli.init_parser()
    module_name = adhoc_cli.parser.parse_args(['-m', 'ping', 'all'])
    assert module_name.module_name == 'ping'

    # Test case-3: module arguments will

# Generated at 2022-06-12 20:12:42.510669
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
   display = AnsibleDisplay()
   context.CLIARGS = {'version': False, 'inventory': ['/var/lib/awx/venv/lib/python2.7/site-packages/ansible/inventory/inventory.py'], 'help': False, 'listtags': False, 'listtasks': False, 'module_path': None, 'tags': [], 'diff': True, 'check': False, 'skip_tags': [], 'one_line': False, 'start_at_task': None, 'vault_password_file': None, 'verbosity': 0, 'connection': 'smart', 'syntax': False, 'extra_vars': [], 'step': None, 'forks': 5, 'module_name': 'ping', 'module_args': "", 'args': ['localhost']}
   cli = AdHocCL

# Generated at 2022-06-12 20:12:54.952756
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    test_args = {
        'args': ['all'],
        'module_name': 'shell',
        'module_args': 'ls -l /var/log/'
    }
    adhoc_cli = AdHocCLI(args=test_args)
    adhoc_cli.parse()
    adhoc_cli.post_process_args(adhoc_cli.options)
    adhoc_cli.run()

# Generated at 2022-06-12 20:12:57.744518
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc_cli = AdHocCLI(args=[])
    assert isinstance(adhoc_cli, AdHocCLI)

# Generated at 2022-06-12 20:12:59.000048
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-12 20:13:07.610214
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.init_parser()

# Generated at 2022-06-12 20:13:10.729262
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Create an instance of AdHocCLI
    args = ['-m', 'command', '-a', 'uptime']
    options = opt_help.get_opt_parser(args=args)
    adhoc_cli = AdHocCLI(options)
    result = adhoc_cli.run()
    assert result == 0

# Generated at 2022-06-12 20:13:16.600058
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI(['ansible', 'test', '-m', 'ping', 'test_host'])
    assert adhoc.parser.prog == 'ansible'
    assert adhoc.parser._positionals.title == 'pattern'
    assert adhoc.parser._positionals.help == 'host pattern'

# Generated at 2022-06-12 20:13:24.336355
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Verifying the basic execution of AdHocCLI
    args = [
        'ansible',
        'all',
        '-i', 'localhost,',
        '-m', 'ping',
    ]
    AdHocCLI(args).run()
    # Verifying the basic execution of AdHocCLI with -a option
    args = [
        'ansible',
        'all',
        '-i', 'localhost,',
        '-m', 'ping',
        '-a', 'data=test',
    ]
    AdHocCLI(args).run()
    # Verifying that an exception is thrown while executing AdHocCLI without -a option

# Generated at 2022-06-12 20:13:24.867493
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:13:37.725817
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import unittest
    import sys
    from ansible.utils.display import Display
    from ansible.cli.adhoc import AdHocCLI
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes

    display = Display()
    display.verbosity = 4

    class TestAdHocCLI(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.inventory = InventoryManager(loader=self.loader, sources=[])
            self.passwords = {}

# Generated at 2022-06-12 20:13:38.817233
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:14:05.549872
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Given
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=["test/test_hosts"])

    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-12 20:14:06.980691
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI("")
    obj.run()

# Generated at 2022-06-12 20:14:09.219294
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert isinstance(adhoc, AdHocCLI)


# Generated at 2022-06-12 20:14:16.269994
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """ Unit test for method run of class AdHocCLI """

    # Create a class instance
    args = [
        '-m', 'copy',
        '-a', 'src=/tmp/hello dest=/tmp/world',
        'localhost',
    ]
    adhoc_cli = AdHocCLI(args)

    # Unit test for method post_process_args of class AdHocCLI
    adhoc_cli.post_process_args(adhoc_cli.options)

# Generated at 2022-06-12 20:14:25.956604
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():

    # setup the args
    args = list()
    parser = AdHocCLI(args).parse()

    # Test the option -h, --help
    assert parser.option_list[0].short_opts == '-h'
    assert parser.option_list[0].long_opts == ['--help']
    assert parser.option_list[0].dest == 'help'
    assert parser.option_list[0].action == 'help'
    assert parser.option_list[0].help == 'Display help message and exit'

    # Test the option -v, --verbose
    assert parser.option_list[1].short_opts == '-v'
    assert parser.option_list[1].long_opts == ['--verbose']
    assert parser.option_list[1].dest == 'verbosity'


# Generated at 2022-06-12 20:14:35.548415
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:14:36.802473
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Load class
    ad_hoc = AdHocCLI()

# Generated at 2022-06-12 20:14:42.697888
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.utils.display import Display
    import os
    import sys

    Display().verbosity = 4
    test_file = os.path.join(os.path.dirname(__file__) + "/../../../", 'test/lib/ansible_test/_data/adhoc/test_AdHocCLI_run.py')
    #sys.argv.append(test_file)
    #AdHocCLI().run()


if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:14:53.290715
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    class Stream:
        def write(self, _):
            pass
    class Options:
        def __init__(self):
            self.module_name = "ping"
            self.module_args = "data=hello world"
            self.subset = None
            self.listhosts = None
            self.verbosity = 0
            self.ask_vault_pass = False
            self.ask_become_pass = False
            self.ask_pass = False
            self.tree = None
            self.timeout = 10
            self.one_line = False
            self.output_file = None
            self.module_path = []
            self.private_key_file = None
            self.remote_user = None
            self.connection = None
            self.timeout = None
            self.ssh_common

# Generated at 2022-06-12 20:15:01.245819
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Configure an AdHocCLI for testing
    class TestAdHocCLI(AdHocCLI):
        def ask_passwords(self):
            return ('conn_pass', 'become_pass')
        def _play_prereqs(self):
            Inventory = __import__('ansible.inventory.inventory').inventory.Inventory
            VariableManager = __import__('ansible.vars.manager').vars.VariableManager
            loader = __import__('ansible.parsing.dataloader').parsing.dataloader.DataLoader()
            return (
                loader,
                Inventory(loader),
                VariableManager(loader=loader)
            )

    adhoc_cli = TestAdHocCLI()

# Generated at 2022-06-12 20:15:45.633762
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''
    ansible ad-hoc -m ping localhost
    '''
    module_name = 'ping'
    module_args = ''
    hosts = 'localhost'
    bin_ansible_callbacks = False
    verbosity = 0
    listhosts = False
    subset = None
    one_line = False
    tree = ''
    forks = None
    seconds = None
    poll_interval = None
    check = False
    inventory = '/etc/ansible/hosts'
    ask_vault_pass = False
    ask_pass = False
    ask_sudo_pass = False
    ask_su_pass = False
    tags = None
    skip_tags = None
    connection = 'smart'
    timeout = None
    ssh_common_args = None
    sftp_extra_args = None

# Generated at 2022-06-12 20:15:47.019468
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert adhoc is not None

# Generated at 2022-06-12 20:15:47.953120
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:15:57.040860
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import mock

    class MockHost:
        def __init__(self, name):
            self.name = name

    class MockHostInfo:
        def __init__(self, hostname, address):
            self.name = hostname
            self.vars = dict(remote_addr=address)

    class FakeInventory:
        def __init__(self, pattern):
            self.pattern = pattern
            self.hosts = dict(_meta=dict(hostvars=dict()))

        def get_hosts(self, pattern, ignore_rest=True):
            return [MockHost(name) for name in self.hosts.keys() if name != '_meta']

        def add_group(self, name):
            self.hosts[name] = dict(vars=dict())


# Generated at 2022-06-12 20:16:08.623446
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    class Options:
        verbosity = 0
        subset = None
        listhosts = False
        module_path = None
        module_name = 'command'
        module_args = 'echo hello'
        inventory = '/etc/ansible/hosts'
        pattern = 'all'
        forks = 0
        remote_user = 'root'
        remote_pass = None
        private_key_file = None
        sudo = False
        sudo_user = None
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False
        seconds = 20
        poll_interval = 15
        extra_vars = []
        playbook_path = None
        tags = []
        start_at_task = None
        skip_tags = []
        one_line = False

# Generated at 2022-06-12 20:16:16.563965
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    """
    This function tests run method of class AdHocCLI
    """
    import pytest
    from ansible.cli.adhoc import AdHocCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common._collections_compat import UserDict
    import os
    import json
    import sys
    import shutil
    cwd = os.getcwd()
    os.chdir("tests/cli/adhoc")
    current_dir = os.getcwd()
    adhoc_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir

# Generated at 2022-06-12 20:16:26.253502
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.config.manager import ConfigManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    localhost = 'localhost'
    hostname = 'hostname'
    module_name = 'hostname'
    module_args = 'hostname'
    pattern = ''
    config_manager = ConfigManager()
    loader = DataLoader(config_manager)
    variable_manager = VariableManager(loader=loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=localhost)
    args = {'module_name': module_name, 'module_args': module_args, 'args': pattern}
    adhoc_cli = AdHocCLI(args)
    result = adhoc_

# Generated at 2022-06-12 20:16:28.635563
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    myAdHocCLI = AdHocCLI()
    res =myAdHocCLI.run()
    assert res==0

# Generated at 2022-06-12 20:16:29.187005
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:16:31.553066
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:18:03.103328
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:18:09.974013
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    import sys
    import inspect
    import argparse
    from collections import namedtuple
    from ansible.cli.adhoc import AdHocCLI

    if sys.version_info[0] > 2:
        from io import StringIO
    else:
        from StringIO import StringIO

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", '--time', default=0, dest='seconds')
    parser.add_argument("-T", '--poll-interval', default=10, dest='poll_interval')
    parser.add_argument("-B", '--seconds', default=0, dest='seconds')   # Seconds
    parser.add_argument("-P", '--poll', default=10, dest='poll_interval')   # Poll

# Generated at 2022-06-12 20:18:10.719959
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    pass

# Generated at 2022-06-12 20:18:21.140223
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # create a file on system to create ad-hoc task
    with open('sample.yml', 'w') as f:
        f.write('''
        - hosts: localhost
          tasks:
            - name: ping test
              ping:
        ''')

    # create object of class AdHocCLI
    adhoc = AdHocCLI(['-m','ping', 'localhost','-a', 'echo hello world'])

    res = adhoc.run()

    # assert to check for ad-hoc task runnning in localhost
    assert res is None

    # create object of class AdHocCLI
    adhoctask = AdHocCLI(['-i','./sample.yml', 'localhost'])

    res = adhoctask.run()

    # assert to check for

# Generated at 2022-06-12 20:18:28.254855
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # define instance of class AdHocCLI
    adhoc_cli = AdHocCLI()

    # add options to AdHocCLI instance
    adhoc_cli.add_cli_opt('module_name', 'shell')
    adhoc_cli.add_cli_opt('module_args', 'uname -a')
    adhoc_cli.add_cli_opt('subset', None)
    adhoc_cli.add_cli_opt('listhosts', None)
    adhoc_cli.add_cli_opt('one_line', 'True')
    adhoc_cli.add_cli_opt('tree', None)

    # call method run of class AdHocCLI
    result = adhoc_cli.run()

# Generated at 2022-06-12 20:18:30.831596
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    assert AdHocCLI(['--list-hosts'])
    assert AdHocCLI(['--module-name'])
    assert AdHocCLI(['--module-args'])

# Generated at 2022-06-12 20:18:33.526929
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ad_hoc_cli = AdHocCLI(args=['-c', 'local', '-m', 'shell', '-a', 'ls /', 'localhost'])
    result = ad_hoc_cli.run()
    assert result == 0

# Generated at 2022-06-12 20:18:36.637087
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    import os
    from ansible.cli.adhoc import AdHocCLI
    p = AdHocCLI(args=['ansible-playbook', '--version'])
    assert os.path.isfile(p.parser._usage_dir_file)


# Generated at 2022-06-12 20:18:38.717308
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(args=[])
    cli.parser.parse_args(args=['localhost', '--list-hosts'])
    cli.post_process_args(cli.options)
    assert cli.run() == 0

# Generated at 2022-06-12 20:18:39.131374
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass