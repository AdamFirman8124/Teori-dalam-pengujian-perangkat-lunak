

# Generated at 2022-06-12 20:11:56.451832
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # TODO: write me :)
    pass

# Generated at 2022-06-12 20:12:07.024014
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import callback_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import sys
    import json
    import os
    from ansible.module_utils._text import to_text

    inventory = Inventory('localhost', VariableManager(), DataLoader())
    mock_options = {}
    mock_options['module_name'] = 'command'
    mock_options['module_args'] = 'ls'
    mock_options['subset'] = None
    mock_options['listhosts'] = False

# Generated at 2022-06-12 20:12:15.726186
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    cb = 'oneline'

    hosts_filename = '/var/tmp/ansible_hosts'
    with open(hosts_filename, 'w+') as f:
        f.write(""" [myservers]
                node1.example.com
                node2.example.com

                [mywebservers:children]
                myservers
                """)

    inventory = InventoryManager(loader=loader, sources=[hosts_filename])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # construct playbook objects to wrap task

# Generated at 2022-06-12 20:12:26.485772
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    def setup_args(self):
        pass

    def do_cli_setup(self, args):
        pass

    def get_optparser(self):
        pass

    def post_process_args(self, options):
        pass

    def run_subset(self, pattern):
        pass

    adhoc_cli = AdHocCLI()
    adhoc_cli.setup_args = setup_args
    adhoc_cli.do_cli_setup = do_cli_setup
    adhoc_cli.get_optparser = get_optparser
    adhoc_cli.post_process_args = post_process_args
    adhoc_cli.run_subset = run_subset
    adhoc_cli.run()


# Generated at 2022-06-12 20:12:27.779040
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cls = AdHocCLI()
    cls.run()
    pass

# Generated at 2022-06-12 20:12:30.567480
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    adhoc.parse()
    assert adhoc.run() == 0

# Generated at 2022-06-12 20:12:33.750803
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    AdHocCLI class - constructor test
    '''
    adhoc_obj = AdHocCLI(args=[])
    assert adhoc_obj



# Generated at 2022-06-12 20:12:35.092660
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    assert adhoc.run() == 1

# Generated at 2022-06-12 20:12:41.500210
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    Unit test for constructor of class AdHocCLI.
    '''

    adhoc = AdHocCLI()
    assert isinstance(adhoc, AdHocCLI) is True
    assert isinstance(adhoc, CLI) is True


if __name__ == '__main__':
    from ansible.module_utils import basic
    basic._ANSIBLE_ARGS = ['ansible-2.9.4', '-m', 'setup', 'localhost']
    adhoc = AdHocCLI()
    adhoc.run()

# Generated at 2022-06-12 20:12:41.995136
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass

# Generated at 2022-06-12 20:12:52.499215
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:12:55.190111
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI()
    assert isinstance(cli, AdHocCLI)
    assert isinstance(cli.parser, CLI.parser)


if __name__ == '__main__':
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:12:56.244830
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    pass


# Generated at 2022-06-12 20:13:04.074707
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic

    def _get_parser():
        class Bunch(object):
            pass

        parser = Bunch()
        parser.parse_args = lambda: Bunch()
        parser.parse_args.return_value = Bunch()
        parser.parse_args.return_value.action = 'run'
        parser.parse_args.return_value.module_name = 'ping'
        parser.parse_args.return_value.module_path = None
        parser.parse_args.return_value

# Generated at 2022-06-12 20:13:10.826857
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible import constants as C
    from ansible.cli import CLI
    from ansible.cli.adhoc import AdHocCLI
    from ansible.errors import AnsibleError, AnsibleOptionsError
    import pytest

    def side_effect_get_host_list(inventory, subset, pattern):
        if pattern == 'foo':
            return []
        else:
            return ['ok']

    def side_effect_ask_passwords():
        return ('foo', 'bar')

    class MockCLI(CLI):
        def get_host_list(self, inventory, subset, pattern):
            return side_effect_get_host_list(inventory, subset, pattern)

        def ask_passwords(self):
            return side_effect_ask_passwords()


# Generated at 2022-06-12 20:13:12.383999
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoccli = AdHocCLI()
    adhoccli.init_parser()



# Generated at 2022-06-12 20:13:13.838887
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    main()


# Generated at 2022-06-12 20:13:15.858988
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    adhoc = AdHocCLI()
    # TODO: Improve this test case
    adhoc.run()

# Generated at 2022-06-12 20:13:23.635332
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    '''Unit test for method run of class AdHocCLI'''
    logfile = tempfile.mktemp()
    class Args:
        pass
    args = Args()
    args.verbosity = 0
    args.inventory = os.path.join('test', 'test_inventory')
    args.listhosts = True
    args.subset = None
    args.module_name = 'command'
    args.module_args = 'ls'
    args.tree = logfile
    args.args = ''

    # If we run this unit test, ansible will try to use a ssh connection
    # to localhost. Because of this, set C.HOST_KEY_CHECKING = False
    C.HOST_KEY_CHECKING = False

    ad_hoc_cli = AdHocCLI(args)
   

# Generated at 2022-06-12 20:13:25.642267
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI([])
    cli.post_process_args(dict(module_name='test', module_args='test'))
    assert cli.run() == 0

# Generated at 2022-06-12 20:13:43.859766
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()

# Generated at 2022-06-12 20:13:49.514494
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # Test when TaskQueueManager returns a value
    from ansible.errors import AnsibleError, AnsibleOptionsError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils._text import to_text
    from ansible.parsing.splitter import parse_kv
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.utils.display import Display
    from collections import namedtuple

    display = Display()

    #default options passed to TaskQueueManager

# Generated at 2022-06-12 20:13:58.261503
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys, os
    import pytest
    from io import StringIO
    from unittest.mock import patch
    from ansible.module_utils.six import PY2, b
    from ansible.module_utils._text import to_bytes, to_text

    with patch('ansible.cli.AdHocCLI.run') as my_run:
        cli = AdHocCLI(['arg1', 'arg2'])
        args = cli.parse()
        cli.post_process_args(args)
        cli.run()

    calling_module = sys.modules[__name__]

# Generated at 2022-06-12 20:14:09.020502
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    display = Display()

# Generated at 2022-06-12 20:14:20.616530
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.plugins.callback.default import CallbackModule
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    import shutil
    import tempfile
    import json

    display = Display()

    # create temp dir
    tmp_path = tempfile.mkdtemp()

    # make sure we clean up temp files on ctrl+c
    import atexit
   

# Generated at 2022-06-12 20:14:23.945118
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoccl = AdHocCLI(args=['ansible', '-i', 'localhost,'])
    assert adhoccl._play_prereqs()


if __name__ == '__main__':
    cli = AdHocCLI()
    cli.run()

# Generated at 2022-06-12 20:14:34.455787
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    mock_subset = ''
    mock_module_name = 'ping'
    mock_module_args = ''
    mock_listhosts = True
    mock_subset = ''
    mock_verbose = 0
    mock_inventory = None
    mock_module_paths = None
    mock_forks = 1
    mock_ask_vault_pass = False
    mock_vault_password_files = None
    mock_new_vault_password_file = None
    mock_output_file = None
    mock_become_ask_pass = False
    mock_ask_

# Generated at 2022-06-12 20:14:43.044012
# Unit test for method run of class AdHocCLI

# Generated at 2022-06-12 20:14:45.576157
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # construct the class object
    adhoc_obj = AdHocCLI(sys.argv)
    # call the run method
    adhoc_obj.run()

# Generated at 2022-06-12 20:14:49.893160
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    ahc = AdHocCLI()
    # Select basic options for ad-hoc
    options = ['ansible-adhoc','localhost','--module-name','shell','--args','whoami']
    # Call method run
    result = ahc.run()
    # Assert method run
    assert result == 0

# Generated at 2022-06-12 20:15:37.593648
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import mock
    from ansible.cli.adhoc import AdHocCLI
    mock_play_prereqs = mock.Mock()
    args = mock.Mock(subset=None, one_line=False, tree=None, listhosts=False, module_name='ping', module_args='', verbosity=2, forks=None, seconds=None, poll_interval=None)
    ans_ad = mock.Mock()
    ans_ad.display = mock.Mock()
    ans_ad.display.verbosity = 2
    mock_inst = mock.Mock()
    type(mock_inst).ask_passwords = mock.PropertyMock(return_value=(None, None))

# Generated at 2022-06-12 20:15:46.516254
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import inventory_loader, module_loader
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-12 20:15:55.416914
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():

    # create mock for class TaskQueueManager
    class MockTaskQueueManager(object):
        def __init__(self):
            self.cleanup = set()

        def __getitem__(self, key):
            return self.__dict__[key]

        def __setitem__(self, key, value):
            self.__dict__[key] = value

        def __delitem__(self, key):
            del self.__dict__[key]

        def cleanup(self):
            for cleanup_function in self.cleanup:
                cleanup_function()

        def load_callbacks(self):
            pass

        def send_callback(self, callback_name, *args, **kwargs):
            pass

        def run(self, play):
            pass


    # create mock for class Play

# Generated at 2022-06-12 20:15:58.124036
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI()
    cli.init_parser()
    options = cli.post_process_args(cli.parser.parse_args(['192.168.100.201', '-m', 'ping']))
    assert options.module_name == 'ping'

if __name__ == '__main__':
    test_AdHocCLI_run()

# Generated at 2022-06-12 20:16:00.310206
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    Test AdHocCLI() constructor
    '''
    adhoc_cli = AdHocCLI()
    assert isinstance(adhoc_cli, AdHocCLI)


# Generated at 2022-06-12 20:16:10.931404
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.manager import VariableManager

    args = [
        'ansible',
        'all',
        '-i', 'hosts',
        '-m', 'setup',
        '-a', 'var="v"'
    ]

    context._init_global_context(args)

# Generated at 2022-06-12 20:16:13.926880
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    context._init_global_context(load_plugins=False)
    ip = AdHocCLI()
    ip.post_process_args(dict(module_name='ping', args='localhost', one_line=True, verbosity=4))
    ip.run()

# Generated at 2022-06-12 20:16:14.942312
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    cli = AdHocCLI(args=[])
    assert cli is not None

# Generated at 2022-06-12 20:16:15.955713
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    adhoc = AdHocCLI()
    assert adhoc

# Generated at 2022-06-12 20:16:21.409956
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    # Testing AdHocCLI._play_ds
    # No arguments
    cli = AdHocCLI()
    cli.context = context
    cli.options = opt_help.create_empty_options()
    cli.options.module_args = None
    cli.options.module_name = 'ping'
    cli.post_process_args(cli.options)
    cli.parser = cli.init_parser()
    cli.parser.prog = 'ansible'
    cli.parser.parse_args(['localhost', '-m', 'ping'])
    cli.args = cli.parser.parse_args(['localhost', '-m', 'ping'])

    # Check the proper exception is raised if there are no args to a module that requires them

# Generated at 2022-06-12 20:17:50.468730
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    obj = AdHocCLI()
    assert obj.run() == None

# Generated at 2022-06-12 20:18:01.272755
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    mocker.patch.object(Display, 'verbosity')
    mocker.patch.object(Display, 'warning')
    mocker.patch.object(CLI, 'ask_passwords')
    mocker.patch.object(CLI, 'get_host_list')
    mocker.patch.object(CLI, '_play_prereqs')
    mocker.patch.object(Play, 'load')
    mocker.patch.object(Playbook, '__init__')
    mocker.patch.object(Playbook, '_entries')
    mocker.patch.object(Playbook, '_file_name')
    mocker.patch.object(TaskQueueManager, '__init__')
    mocker.patch.object(TaskQueueManager, 'load_callbacks')

# Generated at 2022-06-12 20:18:02.136867
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()



# Generated at 2022-06-12 20:18:06.865267
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    AdHocCLI class is a subclass of CLI class
    '''

    # Initialize AdHocCLI
    adhoc_obj = AdHocCLI()

    # Testing parser for AdHocCLI class
    adhoc_obj.init_parser()

    # Testing post_process_args function of AdHocCLI class
    adhoc_obj.post_process_args()

    # Testing run function of AdHocCLI class
    adhoc_obj.run()

# Generated at 2022-06-12 20:18:08.660466
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    cli = AdHocCLI(['localhost', '-m', 'copy', '-a', 'src=/etc/hosts dest=/tmp/z'])
    cli.run()

# Generated at 2022-06-12 20:18:13.138962
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    '''
    return the CLI object for ad-hoc commands
    '''

    adhoc_cli = AdHocCLI(None, None, None)
    assert adhoc_cli is not None
    assert adhoc_cli.__doc__ is not None

# Generated at 2022-06-12 20:18:15.918365
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    test_cli = AdHocCLI()
    test_cli.post_process_args(context.CLIARGS)
    test_cli.run()

# Generated at 2022-06-12 20:18:24.240614
# Unit test for method run of class AdHocCLI
def test_AdHocCLI_run():
    import sys
    import tempfile
    from StringIO import StringIO

    class MockTqm(object):
        def __init__(self, bad_value=False):
            self.options = None
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.passwords = None
            self.stdout_callback = None
            self.run_additional_callbacks = None
            self.run_tree = None
            self.forks = None
            self.stats = None
            self.bad_value = bad_value

        def load_callbacks(self):
            pass

        def send_callback(self, event, data):
            if self.bad_value and event == 'v2_playbook_on_start':
                pass
            else:
                self.stats = data

# Generated at 2022-06-12 20:18:25.329893
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    pass

# Generated at 2022-06-12 20:18:26.701369
# Unit test for constructor of class AdHocCLI
def test_AdHocCLI():
    AdHocCLI()