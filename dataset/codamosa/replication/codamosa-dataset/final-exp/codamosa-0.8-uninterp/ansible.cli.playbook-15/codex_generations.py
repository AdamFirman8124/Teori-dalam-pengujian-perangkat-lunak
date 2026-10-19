

# Generated at 2022-06-12 20:32:53.958820
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.plugins.loader import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create an instance of PlaybookCLI class
    c = PlaybookCLI(args=[])

    # Construct OptionParser object with the required parameters
    parser = c.base_parser(
        usage='%prog [options] playbook.yml [playbook2 ...]',
        inventory=None,
        subset=None,
        check=False)

    # Initialize Options
    options, args = parser.parse_args([])

    # Initialize context from options
    context.CLIARGS = options

    # Create DataLoader object
    loader = DataLoader()

    # Create VariableManager object

# Generated at 2022-06-12 20:32:55.004086
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:58.134704
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create parser for CLI options
    parser = PlaybookCLI().init_parser()
    # parse CLI options
    options = PlaybookCLI().parse(parser)
    # post process CLI options
    options = PlaybookCLI().post_process_args(options)
    # run
    return PlaybookCLI().run()

# Generated at 2022-06-12 20:33:07.153365
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    class Inventory:
        def __init__(self, hosts, patterns=None):
            self.hosts = hosts
            self.patterns = patterns

        def list_hosts(self, pattern=None):
            return self.hosts

        def get_hosts(self, pattern):
            return self.patterns[pattern]

    class VariableManager:
        def __init__(self, vars_dict=None, play=None):
            if vars_dict:
                self.vars_dict = vars_dict
            else:
                self.vars_dict = {}
            self.play = play

        def clear_facts(self, hostname):
            pass


# Generated at 2022-06-12 20:33:12.959891
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # test for invalid input
    options = context.CLIARGS
    options['become_pass'] = 'test_become_pass'
    options['become'] = True
    options['become_method'] = 'test_become_method'
    options['listhosts'] = True
    options['listtags'] = True
    options['listtasks'] = True
    options['syntax'] = True
    options['flush_cache'] = True
    options['check'] = True
    options['connection'] = 'test_connection'
    options['inventory_file'] = 'test_inventory_file'
    options['extra_vars'] = 'test_extra_vars'
    options['module_path'] = 'test_module_path'
    options['module_name'] = 'test_module_name'

# Generated at 2022-06-12 20:33:13.623106
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:21.562690
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Create a mock object from class PlaybookCLI and call run
    display = Display()
    display.verbosity = 1

# Generated at 2022-06-12 20:33:26.303131
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.module_utils.common._collections_compat import _CollectionFinder
    import ansible.cli.playbook
    import ansible.module_utils
    import ansible.module_utils.common
    import ansible.module_utils.connection
    import ansible.module_utils.facts
    import ansible.module_utils.six
    import ansible.module_utils.system
    import ansible.module_utils.urls
    import ansible.module_utils.weakref
    import ansible.plugins
    import ansible.plugins.action
    import ansible.plugins.callback
    import ansible.plugins.connection
    import ansible.plugins.filter
    import ansible.plugins.inventory
    import ansible.plugins.loader
    import ansible.plugins.lookup
    import ansible.plugins.str

# Generated at 2022-06-12 20:33:27.655329
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI([])
    cli.run()

# Generated at 2022-06-12 20:33:28.573559
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    PlaybookCLI.run()

# Generated at 2022-06-12 20:33:51.245179
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest
    from ansible.executor.task_queue_manager import TaskQueueManager, \
        TaskQueueManagerInvalidConfiguration

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host, Group

    from ansible.playbook.play import Play


# Generated at 2022-06-12 20:33:52.740450
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:55.942204
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    module = PlaybookCLI()
    import io
    import sys
    sys.stdout = buffer = io.StringIO()
    module.run()
    sys.stdout = sys.__stdout__
    assert buffer.getvalue() != ""

# Generated at 2022-06-12 20:33:57.292929
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    def run(self):
        assert False, "Test not implemented."
    '''
    pass

# Generated at 2022-06-12 20:34:06.179520
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import tempfile
    from ansible.playbook.play import Play
    from ansible.inventory.host import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.display import Display

    display = Display()

    pb = PlaybookCLI(['/dev/null', '-i', 'localhost,'])

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources=['localhost,'])
    fake_variable_manager = VariableManager()

# Generated at 2022-06-12 20:34:14.815150
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:34:15.385903
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:23.825787
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def get_display_output(*args):
        return '\n'.join(args)

    display.display = get_display_output

    context_mock = {
        'bin_ansible_callbacks': True,
        'bin_ansible_inventory': True,
        'bin_ansible_runner': True,
        'bin_ansible_vars': True,
        'CLIARGS': {},
    }
    context.CLIARGS = context_mock['CLIARGS']

    cli = PlaybookCLI()
    cli.run()

# Generated at 2022-06-12 20:34:35.181708
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    This test is called from the unit test file
    test/sanity/code-smell/unittests/test_playbook_cli.py
    with python-m unittest test_playbook_cli.TestPlaybookCli.test_PlaybookCli_run
    """
    # pylint: disable=protected-access
    import ansible.playbook.play_context as play_context
    import ansible.playbook.play as play
    import ansible.playbook.block as block
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import DictInventory
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-12 20:34:43.955610
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import os
    import shutil
    import tempfile

    from ansible.module_utils.six.moves import configparser

    # make temp directory to test in
    tmp_directory = tempfile.mkdtemp()

    # make a temp directory to use as a cache
    cachedir = tempfile.mkdtemp()

    # prep a fake inventory
    inventory = os.path.join(tmp_directory, "hosts")
    with open(inventory, 'w') as f:
        f.write("""
localhost ansible_connection=local

[all:vars]
ansible_python_interpreter=/usr/bin/python

[testhost]
testhost.example.org
""")

    # prep fake ansible.cfg
    ansiblecfg = os.path.join(tmp_directory, "ansible.cfg")

# Generated at 2022-06-12 20:35:00.314749
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import sys

    sys.argv = ['ansible-playbook', 'playbook.yml']
    opt = PlaybookCLI(args=sys.argv[1:]).parse()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-12 20:35:01.323222
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:02.014900
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:10.554500
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test dict of args to generate test case data
    args = {
        'listhosts': True,
        'listtags': True,
        'listtasks': True,
        'syntax': True,
        'args': [
            './tests/playbook/sample.yml',
            './tests/playbook/sample_with_include.yml',
            './tests/playbook/sample_with_imports.yml',
            './tests/playbook/sample_with_roles.yml',
        ]
    }
    # Create PlaybookCLI instance
    playbook_cli = PlaybookCLI(args)
    # Test PlaybookCLI's method run
    playbook_cli.run()

# Generated at 2022-06-12 20:35:17.493916
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Create mock objects
    loader = create_autospec(Loader)
    inventory = create_autospec(Inventory)
    variable_manager = create_autospec(VariableManager)
    options = create_autospec(Options)
    passwords = {'conn_pass': None, 'become_pass': None}

    # Run test
    cli = PlaybookCLI(args=[])
    pbex_mock = cli.run(loader, inventory, variable_manager, options, passwords)

    # Check results
    assert(isinstance(pbex_mock, PlaybookExecutor))

# Generated at 2022-06-12 20:35:18.062148
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:23.621659
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    ''' Verify that if no arguments are passed, an error is raised '''
    args = []
    try:
        context._init_global_context(args)
    except AnsibleOptionsError as e:
        assert e.options.args == []
    else:
        assert False, 'Should have raised AnsibleOptionsError'


# Generated at 2022-06-12 20:35:24.639510
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:35:27.894821
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
        display.verbosity = 0
        pbcli = PlaybookCLI(['-i','testinventory','testplaybook.yml'])
        pbcli.post_process_args()
        pbcli.ensure_not_privileged()
        pbcli.get_opt_parser()
        pbcli.run()

# Generated at 2022-06-12 20:35:36.957431
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''Unit test for method run of class PlaybookCLI'''
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.basic import AnsibleModule
    from ansible.template import Templar
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import add_all_plugin_dirs, module_finder
    from ansible.plugins.loader import callback_loader

    class Inventory(Inventory):
        def __init__(self, loader, variable_manager, host_list):
            self._loader

# Generated at 2022-06-12 20:35:50.560079
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:51.112441
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:35:52.353210
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run(inventory=None, variable_manager=None)

# Generated at 2022-06-12 20:35:58.839827
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    mock_self = PlaybookCLI()

    hosts = [
        {'ipv4': '10.80.80.3', 'name': 'test1', 'port': 22, 'ssh_key': '/tmp/test', 'user': 'test'},
        {'ipv4': '10.80.80.4', 'name': 'test2', 'port': 22, 'ssh_key': '/tmp/test', 'user': 'test'},
        {'ipv4': '10.80.80.5', 'name': 'test3', 'port': 22, 'ssh_key': '/tmp/test', 'user': 'test'}
    ]

    assert mock_self._flush_cache(hosts) == 0

# Generated at 2022-06-12 20:36:05.555218
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test for case of successful run
    cli = PlaybookCLI(['ping.yml'])
    cli.run()

    # Test for case of PlaybookCLI with args and forks arguments
    cli = PlaybookCLI(['ping.yml'], forks=10)
    cli.run()

    # Test for case of PlaybookCLI with args and become argument
    cli = PlaybookCLI(['ping.yml'], become=True)
    cli.run()

# Generated at 2022-06-12 20:36:15.397289
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Run with --list-hosts
    cli = PlaybookCLI(['ansible-playbook', '-i', './test/integration/inventory', '--list-hosts', './test/integration/ansible_playbook_listhosts.yml'])
    cli.parse()
    result = cli.run()
    assert result == 0

    # Run with --list-tasks
    cli = PlaybookCLI(['ansible-playbook', '-i', './test/integration/inventory', '--list-tasks', './test/integration/ansible_playbook_listtasks.yml'])
    cli.parse()
    result = cli.run()
    assert result == 0

    # Run with --step

# Generated at 2022-06-12 20:36:19.090303
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI(args=[])
    cli.post_process_args(cli.options)
    cli.run()

# Generated at 2022-06-12 20:36:28.563657
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError
    import os

    # Test error handling when playbook not found
    pb = PlaybookCLI(['/tmp/non_existent_playbook'])
    try:
        pb.run()
    except SystemExit:
        assert True
    except AnsibleError:
        assert False
    except Exception:
        assert False
    else:
        assert False

    # Test error handling when playbook is a directory
    dir_path = os.path.join(os.path.dirname(__file__), 'test_playbooks')
    pb = PlaybookCLI([dir_path])
    try:
        pb.run()
    except SystemExit:
        assert True
    except AnsibleError:
        assert False

# Generated at 2022-06-12 20:36:29.940107
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: implement unit test
    pass


# Generated at 2022-06-12 20:36:30.983951
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:58.817644
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:59.519531
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI()

# Generated at 2022-06-12 20:37:12.126633
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:37:12.561022
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:13.168755
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:22.112338
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Test error case when no playbooks are specified

    with pytest.raises(SystemExit) as ex:
        pb_executor = PlaybookCLI([])
        assert ex.value.code == 1

    # Test successful case when playbook path is valid

    tmp_playbook_file_name = 'tmp_playbook'
    tmp_playbook_file = open(tmp_playbook_file_name, 'w')
    tmp_playbook_file.write('---')
    tmp_playbook_file.close()

    pb_executor = PlaybookCLI([str(tmp_playbook_file_name)])
    assert pb_executor.run() == 0
    os.remove(tmp_playbook_file_name)

# Generated at 2022-06-12 20:37:33.082738
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Patch to avoid running real ansible-playbook runs
    old_PlaybookCLI_run = PlaybookCLI.run

    result_run = None

    def mocked_run(*args, **kwargs):
        nonlocal result_run
        result_run = True
        return 0

    PlaybookCLI.run = mocked_run

    result_args = None

    def mocked_parse(*args):
        nonlocal result_args
        result_args = args

    # Patch to avoid running real argument parsing
    old_parser_parse = CLI.parse
    CLI.parse = mocked_parse

    test = PlaybookCLI(args=['foo'])
    try:
        test.parse()
        assert result_args is not None
        assert result_run is not None
    finally:
        PlaybookCLI.run = old_Play

# Generated at 2022-06-12 20:37:33.423198
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:34.105830
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run()
    assert PlaybookCLI

# Generated at 2022-06-12 20:37:39.863963
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # set up args
    args = ['ansible', 'playbook.yaml']

    # set up context
    context._init_global_context(args)
    p = PlaybookCLI(args)
    # test with empty arguments
    p.run()
    # test with random argument
    context.CLIARGS['foo'] = 'bar'
    with pytest.raises(AnsibleError):
        p.run()
    # test with empty context
    del context.CLIARGS['foo']
    context.CLIARGS = {}
    with pytest.raises(AnsibleError):
        p.run()

# Generated at 2022-06-12 20:38:59.614396
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # the fixture is a fake command line argument parser
    # which returns the arguments which are used in the
    # class PlaybookCLI
    # args = fixure.get_args()
    # class_obj = PlaybookCLI(args=args)
    # assert class_obj.run() != 0

    pass

# Generated at 2022-06-12 20:39:00.101110
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:07.728422
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    PlaybookCLI.get_host_list = lambda a,b: None
    PlaybookCLI.ask_passwords = lambda a: (None, None)

    class opts:
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        subset = None
        flush_cache = False
        verbosity = 1
        extra_vars = None
        connection = 'ssh'
        timeout = 10
        private_key_file = None
        remote_user = 'root'
        remote_pass = None
        become = False
        become_method = None
        become_user = None
        become_pass = None
        check = False
        forks = 5
        inventory = None
        subset = None
        module_path = None
        start_at_task = None
        step = None

# Generated at 2022-06-12 20:39:08.354492
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:09.306696
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:09.679508
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:10.237726
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:11.217989
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cmd = PlaybookCLI()
    cmd.run()

# Generated at 2022-06-12 20:39:20.421312
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.errors import AnsibleError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    pbcli = PlaybookCLI()


# Generated at 2022-06-12 20:39:31.648032
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible import context
    from ansible.cli import CLI
    from ansible.cli.argparser import CLIArgParser
    import os
    import shutil
    import tempfile

    context.CLIARGS = CLIArgParser(['echo']).parse_args()
    context.CLIARGS['help'] = False
    context.CLIARGS['version'] = False
    context.CLIARGS['galaxy_info'] = False
    context.CLIARGS['listhosts'] = False
    context.CLIARGS['listtasks'] = False
    context.CLIARGS['listtags'] = False
    context.CLIARGS['syntax'] = False
    context.CLIARGS['flush_cache'] = False
    context.CLIARGS['tags'] = 'all'
    context.CL

# Generated at 2022-06-12 20:40:37.490167
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Example inventory file
    inventory_file = 'tests/units/cli/inventory'
    inventory = 'localhost,' + inventory_file
    # Example test playbook
    playbook_file = 'tests/units/cli/playbook.yml'

    # Initialize the PlaybookCLI object
    cli = PlaybookCLI(['-i', inventory, playbook_file])

    # Create an AnsibleOptions object
    ansible_options = cli.parse()
    # Create an AnsibleContext object
    ansible_context = cli.context(ansible_options)
    # Configure the cli context
    cli.configure_context(ansible_context)
    # Run the cli and get the result
    result = cli.run()

    # Assertions
    assert result == 0
    # Checks that the default verbosity

# Generated at 2022-06-12 20:40:44.267211
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.cli.cli import CLI
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader

    def create_file(filename, content):
        f = open(filename, 'w')
        f.write(content)
        f.close()

    playbook_path = tempfile.mkdtemp()
    filename = os.path.join(playbook_path, 'playbook.yml')

    content = """\
- hosts: localhost
  tasks:
  - name: ping
    ping:
"""
    create_file(filename, content)

    def test_implicit_localhost_no_limit(monkeypatch):
        monkeypatch.setattr(CLI, 'parse', lambda x: None)

# Generated at 2022-06-12 20:40:50.674804
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # Setup
    import sys
    import tempfile

    module_name = 'test_module_name'
    module_args = 'test_module_args'
    include_role = 'test_include_role'
    include_tasks = 'test_include_tasks'
    include_variables = 'test_include_variables'
    limit = 'test_limit'
    listtags = True
    listtasks = True
    playbook = 'test_playbook_path'
    subset = 'test_subset'

    # Create temporary files
    # 'playbook'
    (playbook_fd, playbook_path) = tempfile.mkstemp(text=True)


# Generated at 2022-06-12 20:41:00.774916
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import ansible.config
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    class MockPlaybookExecutor(PlaybookExecutor):
        def __init__(self, play, variable_manager, loader, options):
            self.play = play
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.inventory = None
            self.passwords = {}
            self.callback = None
            self.__play_ptr = 0
            self.__

# Generated at 2022-06-12 20:41:01.292657
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    assert 1 == 2

# Generated at 2022-06-12 20:41:02.599539
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
    Unit test for method run of class PlaybookCLI
    '''
    pass

# Generated at 2022-06-12 20:41:05.798510
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # FIXME: This test cannot be run without core of Ansible (main.py)
    pass

# Generated at 2022-06-12 20:41:06.324304
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:41:07.351160
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pbc = PlaybookCLI()
    pbc.run()

# Generated at 2022-06-12 20:41:07.805408
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass