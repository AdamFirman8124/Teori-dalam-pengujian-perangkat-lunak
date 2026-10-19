

# Generated at 2022-06-12 20:32:42.992633
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:32:52.402804
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import ansible.playbook.play
	
    class FakeOptions:
        listtasks = False
        listtags = False
        step = False
        start_at_task = None
        hosts = '1.1.1.1'
        syntax = None
        subset = None
        become_ask_pass = False
        ask_vault_pass = False
        diff = False
        flush_cache = False
        tags = None
        skip_tags = None
        check = False
        extra_vars = []
        inventory = None
        module_path = None
        only_tags = None
        verbosity = 0
        connection = None
        ask_pass = False
        ask_su_pass = False
        ask_sudo_pass = False
        become = False
        become_method = None
        become_user = None
       

# Generated at 2022-06-12 20:32:56.467070
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:32:56.947219
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:02.828434
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import logging
    from .test_utils import AnsibleExitJson, AnsibleFailJson

    # logging.basicConfig(level=logging.DEBUG)

    class CollectionLibMock(object):
        pass

    class CollectionMock(object):
        def __init__(self):
            self.__collections__ = [
                {
                    "namespace": "namespace1",
                    "name": "collection1",
                    "version": "1.0.0"
                }
            ]

    class LoaderMock(object):
        def __init__(self):
            self.collection_mock = CollectionMock()
            sys.modules['ansible.collections.namespace1.collection1'] = self.collection_mock


# Generated at 2022-06-12 20:33:09.722371
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    #Setup
    import argparse
    import os
    import tempfile

    from ansible.cli.arguments import option_helpers
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.display import Display

    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    test_playbook_dir = os.path.join(test_dir,'playbooks')
    os.makedirs(test_playbook_dir)

    test_tasks = """
    - name: test task
      debug:
        msg: "Hello world!"
    """

    test_playbook_file = os.path.join(test_playbook_dir,'test.yml')


# Generated at 2022-06-12 20:33:19.295308
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # test example
    context.CLIARGS = {'args': ['site.yml'], 'verbosity': 0, 'flush_cache': False}
    cli = PlaybookCLI(['ansible-playbook', 'site.yml'])
    cli.run()

    # with missing playbook
    context.CLIARGS = {'args': ['not-existing.yml'], 'verbosity': 0, 'flush_cache': False}
    cli = PlaybookCLI(['ansible-playbook', 'not-existing.yml'])
    try:
        cli.run()
    except AnsibleError as error:
        assert 'not-existing.yml' in error.message

    # with empty playbook

# Generated at 2022-06-12 20:33:22.396893
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # file does not exists
    try:
        PlaybookCLI().run([__file__, 'not_existed_file'])
        assert False, "PlaybookCLI.run() did not raise an exception"
    except SystemExit:
        pass
    except:
        assert False, "PlaybookCLI.run() raised unexpected exception"


# Generated at 2022-06-12 20:33:23.640870
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:26.677879
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pb_run = PlaybookCLI(['/usr/bin/ansible-playbook', '/home/ansible/test/test.yml'])
    pb_run.run()


# Generated at 2022-06-12 20:33:42.953107
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys, os
    # Create a test PlaybookCLI object
    cli = PlaybookCLI(['-i', './test/testinventory'])
    # Make sure the env var is set KEEP_REMOTE_FILES
    os.environ["ANSIBLE_KEEP_REMOTE_FILES"] = "1"
    rc = cli.run()
    os.environ["ANSIBLE_KEEP_REMOTE_FILES"] = "0"
    sys.exit(rc)

# Generated at 2022-06-12 20:33:52.832226
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VarManager
    from ansible.errors import AnsibleError

    # Create a module for testing
    class FakeTaskQueueManager(TaskQueueManager):
        def __init__(self, *args, **kwargs):
            super(FakeTaskQueueManager, self).__init__(*args, **kwargs)
            self._stats = dict(
                ok=dict(hosts={}),
                failures=dict(hosts={}),
                dark={},
                processed={},
            )
            self._pending_results = []
            self._tqm_reaped = False


# Generated at 2022-06-12 20:33:53.776906
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass

# Generated at 2022-06-12 20:33:55.627142
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: Test that PlaybookCLI.run() works as expected
    assert True == True

# Generated at 2022-06-12 20:33:56.397675
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:33:57.156059
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass

# Generated at 2022-06-12 20:33:58.362199
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:58.877889
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:33:59.391308
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:09.503079
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import sys
    import tempfile
    import yaml
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    pb_data = '''
    ---
    - hosts:
      tasks:
      - name: Test Task Name
      - name: Test Task2 Name
      - name: Test Task3 Name
    '''

    pb_data_res = yaml.safe_load(pb_data)
    pb_res = Play().load(pb_data_res, variable_manager=VariableManager(), loader=None)
    pb_res.post_validate(templar=Templar(loader=None))

    runner_args

# Generated at 2022-06-12 20:34:21.004235
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:34:24.714990
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_cli = PlaybookCLI(['/dev/null', '/dev/null'])
    try:
        assert isinstance(test_cli.run(), int)
    except AnsibleError as e:
        raise AssertionError("AnsibleError:" + str(e))

# Generated at 2022-06-12 20:34:35.823573
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options(object):
        listhosts = False
        listtags = False
        listtasks = False
        syntax = False
        subset = None
        inventory = 'hosts'
        flush_cache = False
        verbosity = 0
        check = False
    class RunnerOptions(object):
        module_path = None
        forks = 5
        timeout = None
        remote_user = 'root'
        remote_pass = None
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = 'sudo'
        become_user = 'root'
        become_pass = None
        become_exe = None
        become_flags = None

# Generated at 2022-06-12 20:34:41.978870
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    b_playbook_dir = os.path.dirname(os.path.abspath(to_bytes('/playbook/playbook.yml', errors='surrogate_or_strict')))
    b_playbook_dirs = [b_playbook_dir]
    AnsibleCollectionConfig.playbook_paths = b_playbook_dirs
    pc = PlaybookCLI([])
    pc.parse(['playbook.yml'])
    pc.run()
    assert True

# Generated at 2022-06-12 20:34:47.813608
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbookcli = PlaybookCLI()
    args = ['playbook.yml','playbook1.yml','playbook2.yml']
    context.CLIARGS = {'args':args}
    results = playbookcli.run()
    assert isinstance(results,list)

# Generated at 2022-06-12 20:34:52.711951
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class PlaybookCLI_runTest(object):
        def __init__(self):
            pass
        def __call__(self):
            return 0
        def _flush_cache(self, inventory, variable_manager):
            pass

    PlaybookCLI_runTest._flush_cache = PlaybookCLI._flush_cache
    context.CLIARGS = {'args': ['ansible-test/test_data/test_playbook.yml'], 'subset': 'all', 'listhosts': True}
    foo = PlaybookCLI_runTest()
    foo.ask_passwords = lambda: (None, None)
    foo.parser = PlaybookCLI(['ansible-playbook', 'good.yml'])
    foo.run()

# Generated at 2022-06-12 20:35:00.511578
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    def test_playbook_executor_run(self):
        self.mock_playbook_executor.run.return_value = (0, 'ok')
        self.mock_display.display.return_value = None

        result = self.cli.run()

        self.mock_playbook_executor.run.assert_called_once_with()
        self.assertEqual(None, result)

    def test_playbook_executor_run_error(self):
        self.mock_playbook_executor.run.return_value = (1, 'error')
        self.mock_display.display.return_value = None

        result = self.cli.run()

        self.mock_playbook_executor.run.assert_called_once_with()

# Generated at 2022-06-12 20:35:10.594332
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # set up
    # create mock class
    class MockDisplay(object):
        def __init__(self):
            pass
        def verbosity(self):
            pass
        def display(self, msg):
            if msg.startswith('\nplaybook'):
                return msg
                pass
            elif msg.startswith('\\n'):
                return msg
            else:
                pass

    class MockCLIARGS(object):
        def __init__(self):
            self.args = ['test.yml']
            self.subset = None
            self.flush_cache = True
            self.listhosts = False
            self.listtasks = True
            self.listtags = False
            self.syntax = False


# Generated at 2022-06-12 20:35:19.324393
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class MockCLI(PlaybookCLI):
        def _play_prereqs(self):
            loader = 'loader'
            inventory = 'inventory'
            variable_manager = 'variable_manager'
            return (loader, inventory, variable_manager)
    playbook_cli = MockCLI()

    class MockOptions:
        connection = 'connection'
        module_path = 'module_path'
        forks = 1
        become = False
        become_method = None
        become_user = None
        become_ask_pass = False
        verbosity = 0
        check = False
        diff = False
        inventory = ['inventory']
        subset = 'subset'
        extra_vars = []
        extra_vars_file = []
        tags = []
        skip_tags = []
        flush_cache = False
        listhost

# Generated at 2022-06-12 20:35:20.789053
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    foo = PlaybookCLI()
    assert foo.run() == None

# Generated at 2022-06-12 20:35:41.504162
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import shutil
    import tempfile

    # Prepare a test environment
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'temp_dummy_playbooks'))
    shutil.copyfile(
        os.path.join(os.path.dirname(__file__), "test_playbookcli.py"),
        os.path.join(temp_dir, 'temp_dummy_playbooks', 'dummy_playbook.yml')
    )
    os.makedirs(os.path.join(temp_dir, 'collections', 'testns', 'testcoll'))

# Generated at 2022-06-12 20:35:51.845812
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # dirname where yamls are located
    yaml_dirname = os.path.join(os.path.dirname(__file__), 'fixtures', 'yaml')
    # files to be used as playbooks
    yamls = ('playbook_syntax_error.yml', 'playbook_syntax_error_ansible_2.5.yaml')
    # iterate over yamls and test them
    for y in yamls:
        print('Testing playbook syntax error on file: ' + y)
        try:
            cli = PlaybookCLI(['ansible-playbook', os.path.join(yaml_dirname, y)])
            result = cli.run()
            assert result == 4
        except Exception as e:
            assert False

# Generated at 2022-06-12 20:35:52.595506
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO: test PlaybookCLI.run()
    pass

# Generated at 2022-06-12 20:35:57.328817
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    cli = PlaybookCLI()

    playbook_path = 'tests/test_playbook_cli.yml'
    with open(playbook_path, 'rb') as pb:
        playbook_string = pb.read()

    #create a fake parser to pass to our mocked CLI
    mock_parser = cli.create_parser()

    #create a fake options object to pass to our mocked CLI
    mock_options = cli.create_optparser().parse_args()

    #create a fake context object to pass to our mocked CLI
    mock_context = context.CLIARGS
    mock_context['args'] = playbook_string
    mock_context['listtasks'] = False
    mock_context['listtags'] = False
    mock_context['step'] = False
    mock_context['start_at_task'] = None

# Generated at 2022-06-12 20:36:00.052687
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # TODO:
    # Add tests
    #
    # 1. List failed and succeeded hosts
    # 2. List tags and tasks
    # 3. Check print error when playbook not found
    # 4. Check print error when playbook is not a file
    # 5. Check --flush-cache option
    # 6. Create base objects
    # 7.
    pass

# Generated at 2022-06-12 20:36:10.541150
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # create a dummy class that has a run method
    class CLI(PlaybookCLI):
        pass

    options = CLI.parser.parse_args([])[0]

    # create a dummy class that has a run method
    class Playbook(object):
        def __init__(self, cnxt, options, playbooks):
            pass

        def run(self):
            pass

    # create a dummy class that has a run method
    class Display(object):
        def __init__(self):
            self.verbosity = 0

        def display(self, msg):
            pass

    # create a dummy class that has a run method
    class AnsibleError(object):
        pass

    # create a dummy class that has a run method
    class AnsibleCollectionConfig(object):
        playbook_paths = []

    cli = CLI

# Generated at 2022-06-12 20:36:11.746926
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Test whether run method works when passed with arguments
    # FIXME: This test has not been implemented yet
    pass

# Generated at 2022-06-12 20:36:12.212623
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:13.056532
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:13.624495
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:36:43.514460
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    PlaybookCLI.run()

# Generated at 2022-06-12 20:36:50.497919
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    with open('/tmp/test_get_host_list_cache', 'w') as f:
        f.write("1\n")
    with open('/tmp/test_get_host_list_cache', 'r') as f:
        get_host_list_cache_contents = f.read()
    if get_host_list_cache_contents == "1":
        os.remove('/tmp/test_get_host_list_cache')

# Generated at 2022-06-12 20:37:01.805103
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """Test method run of class PlaybookCLI."""

    import pytest

    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError

    # Mock class that simulates the CLI object
    class CliMock(object):

        class OptionsMock(object):
            """Mock class that simulates the options of the CLI object
            """


# Generated at 2022-06-12 20:37:13.963222
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class Options(object):
        def __init__(self, args, verbosity):
            self.args = args
            self.verbosity = verbosity
            self.check = False
            self.flush_cache = False
            self.listhosts = False
            self.listtasks = False
            self.listtags = False
            self.syntax = False
            self.step = False
            self.connection = 'ssh'
            self.timeout = 10
            self.forks = 5
            self.remote_user = 'root'
            self.become = False
            self.become_method = 'sudo'
            self.become_user = None
            self.become_ask_pass = False
            self.ask_pass = False
            self.private_key_file = None
            self.ssh_common_args

# Generated at 2022-06-12 20:37:14.446292
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:25.174879
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    import pytest

    class FakeInventory(object):

        def __init__(self):
            self.hosts_all = {
                "123":
                    {
                        'hostname': '123',
                        'variables': {'ansible_host': '1.2.3.4'},
                        'groups': ['group1', 'group2'],
                    },
                "456":
                    {
                        'hostname': '456',
                        'variables': {'ansible_host': '5.6.7.8'},
                        'groups': ['group1', 'group2'],
                    },
            }

        def get_hosts(self, pattern):
            return self.hosts_all

        def get_host(self, hostname):
            return self.hosts_all[hostname]


# Generated at 2022-06-12 20:37:35.659536
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:36.465762
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:37:36.973834
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:37:46.954118
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    import contextlib
    from io import StringIO

    from ansible.cli.arguments import option_helpers as opt_help
    from ansible.errors import AnsibleOptionsError
    from ansible.utils.path import unfrackpath

    from units.mock.procenv import swap_stdin_and_argv

    mock_args = opt_help.create_parser().parse_args('')

    with swap_stdin_and_argv():
      # Test if there is a playbook in the arguments
      with contextlib.redirect_stdout(StringIO()) as stdout:
        mock_args.args = []
        with pytest.raises(AnsibleOptionsError) as exc:
          PlaybookCLI(mock_args).run()

      # Test if the playbook(s) is/are readable

# Generated at 2022-06-12 20:38:38.773555
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    """
    Test method run of class PlaybookCLI
    """
    # Change working directory to project root
    os.chdir(os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
    ))

    cli = PlaybookCLI(['ansible-playbook', 'playbooks/executor_flow.yml'])
    cli.parse()
    cli.post_process_args(cli.options)

    assert cli.run() is 0

# Generated at 2022-06-12 20:38:45.473960
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # used to display the request to the user
    import argparse
    import sys
    # to modify the arguments
    import collections

    parser = argparse.ArgumentParser()
    # we use add_argument_group because it does not change the argument name
    # used in the help
    # added for method run without arguments
    parser.add_argument('--list-hosts', dest='listhosts', action='store_true')
    parser.add_argument('--list-tasks', dest='listtasks', action='store_true')
    parser.add_argument('--list-tags', dest='listtags', action='store_true')
    parser.add_argument('--step', dest='step', action='store_true')
    parser.add_argument('--start-at-task', dest='start_at_task')

# Generated at 2022-06-12 20:38:54.538530
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    display = Display()
    # create the cli object
    cli = PlaybookCLI(None)
    cli.display = display
    args = ['-i', '/path/to/inventory', '--list-tasks', 'playbook.yml']
    cli.run(args)
    # test if parse method was called
    assert cli.parser.parse_args.called
    # test if process_args method was called
    assert cli.post_process_args.called
    # test if _run_playbook method was called
    assert cli._run_playbook.called
    # test if _flush_cache method was called
    assert cli._flush_cache.called
    # test if _run_playbook method was called with correct arguments

# Generated at 2022-06-12 20:39:04.107402
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.display import Display
    from ansible.errors import AnsibleError

    display = Display()
    display.verbosity = 5

    os.environ['ANSIBLE_STDOUT_CALLBACK'] = 'debug'
    os.environ['ANSIBLE_TRANSPORT'] = 'smart'


# Generated at 2022-06-12 20:39:08.618573
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        test_PlaybookCLI_run()
    else:
        print("USAGE: %s <test_method>" % __name__)

# Generated at 2022-06-12 20:39:18.854974
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Code exists to support pathname manipulation
    # therefore using unittest.mock.patch() method to dynamically mock the os module.
    # This module is used twice to mock 2 different function calls:
    #   - os.path.abspath
    #   - os.path.dirname
    with mock.patch('os.path') as os_path:

        # mock os.path.abspath.return_value = '/home/user/playbook-one.yml'
        os_path.abspath.return_value = '/home/user/playbook-one.yml'

        # mock os.path.dirname.return_value = '/home/user'
        os_path.dirname.return_value = '/home/user'

        # instantiate PlaybookCLI object
        # its run() method is tested below

# Generated at 2022-06-12 20:39:31.223260
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # initialize cli args stub

# Generated at 2022-06-12 20:39:32.755841
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass

# Generated at 2022-06-12 20:39:39.929608
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    playbooks = ['./test/integration/targets/test_playbook/playbook.yml']
    opts = {'listtasks': True}
    cli = PlaybookCLI()
    cli.post_process_args(opts)
    cli.parser.parse_args(playbooks, namespace=context.CLIARGS)
    cli.run()
    assert context.CLIARGS == {}

# Generated at 2022-06-12 20:39:41.581157
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    # Arrange

    # Act
    PlaybookCLI.run()

    # Assert

# Generated at 2022-06-12 20:40:54.598769
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    c = {'flush_cache': True, 'listhosts': True, 'listtags': True, 'listtasks': True,
         'verbosity': 3, 'syntax': False, 'tags': [], 'skip_tags': [], 'start_at_task': None,
         'step': False,
         'args': ['all_hello.yml']}

# Generated at 2022-06-12 20:40:55.677191
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    pass


# Generated at 2022-06-12 20:41:02.609736
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class TestPlaybookCLI(PlaybookCLI):

        def ask_passwords(self):
            return 'sshpass', 'becomepass'

        def _play_prereqs(self):
            class TestInventory():

                def __init__(self, list_hosts):
                    self.list_hosts = list_hosts

                def list_hosts(self, subset):
                    return self.list_hosts

            class TestVariableManager():

                def clear_facts(self, hostname):
                    pass

                def get_vars(self, play):
                    return {}

            class TestLoader():

                def __init__(self):
                    self.basedir = ''

                def set_basedir(self, basedir):
                    self.basedir = basedir

            loader = TestLoader()
            inventory = TestInventory

# Generated at 2022-06-12 20:41:11.141850
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():

    sys.argv = [sys.argv[0], 'playbook.yml']
    # sys.argv = [sys.argv[0], '--check', 'playbook.yml']
    # sys.argv = [sys.argv[0], '--help']
    # sys.argv = [sys.argv[0], '--list-tasks', 'playbook.yml']
    # sys.argv = [sys.argv[0], '--list-tags', 'playbook.yml']
    # sys.argv = [sys.argv[0], '--step', 'playbook.yml']
    # sys.argv = [sys.argv[0], '--start-at-task', 'restart_zk', 'playbook.yml']
    # sys.argv

# Generated at 2022-06-12 20:41:17.800391
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    test_instance = PlaybookCLI()
    test_instance.init_parser()
    test_instance.post_process_args(context.CLIARGS)
    with pytest.raises(AnsibleError) as excinfo:
        test_instance.run()
    assert "the playbook: test_PlaybookCLI_run could not be found" in str(excinfo.value)

# Generated at 2022-06-12 20:41:18.712324
# Unit test for method run of class PlaybookCLI

# Generated at 2022-06-12 20:41:26.401245
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    '''
        This is a unit test for run method of Playbook class
    '''
    from ansible.cli.arguments import options as cli_opts

    # Create a PlaybookCLI object
    playbook_cli = PlaybookCLI(['--list-hosts'], options=cli_opts, args_files=[])

    playbook_cli.post_process_args(cli_opts)

    assert playbook_cli.parser.VERSION == C.__version__
    assert playbook_cli.parser.description == "Runs Ansible playbooks, executing the defined tasks on the targeted hosts."
    assert playbook_cli.parser.prog == "ansible-playbook"
    assert playbook_cli.parser.usage == "%prog [options] playbook.yml [playbook2 ...]"

# Generated at 2022-06-12 20:41:35.639429
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    class myoptions:
        args = ["test.yml", "test2.yml"]
        connection = "smart"
        verbosity = 0
        listhosts = False
        listtasks = False
        listtags = False
        syntax = False
        subset = None
        check = False
        diff = False
        inventory = ""
        flush_cache = False
        extra_vars = []
        ask_vault_pass = None
        vault_password_files = []
        start_at_task = None
        step = None
        private_key_file = None
        become = None
        become_method = None
        become_user = None
        become_ask_pass = False
        forks = 5
        module_path = None
        remote_user = None
        remote_port = 22

# Generated at 2022-06-12 20:41:45.427223
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # create a test ansible configuration

    # set test values
    inventory = '../../../ansible/inventory'
    module_path = '../plugins/modules'
    connection = 'ssh'
    remote_user = 'remote_user'
    test_args = ['-i', inventory, '--connection', connection, '--remote-user', remote_user, '-m', module_path, '--help']

    # could not find a way to mock sys.argv, so just patch CLIARGS to test
    original_args = context.CLIARGS
    context.CLIARGS = {}
    cli = PlaybookCLI(args=test_args)
    post_processed_args = cli.post_process_args(context.CLIARGS)
    context.CLIARGS = original_args
    assert post

# Generated at 2022-06-12 20:41:46.333762
# Unit test for method run of class PlaybookCLI
def test_PlaybookCLI_run():
    # TODO
    pass