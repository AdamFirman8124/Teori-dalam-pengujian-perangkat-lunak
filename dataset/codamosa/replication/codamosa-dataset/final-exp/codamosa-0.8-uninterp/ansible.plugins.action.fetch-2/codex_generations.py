

# Generated at 2022-06-13 09:55:39.984775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    # only for this test, we will pretend we have a valid config
    class _Config:
        def __init__(self):
            self.connection = "smart"
            self.remote_addr = None
            self.remote_user = "user"
            self.private_key_file = "secret"
            self.become = "no"
            self.become_method = "sudo"
            self.become_user = "root"
            self.become_pass = "password"
            self.vault_password = "password"
            self.no_log = False
            self.verbosity = 0
            self.check = False
            self.diff = False
            self.docker_extra_args = None

# Generated at 2022-06-13 09:55:40.567064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:55:50.512823
# Unit test for constructor of class ActionModule
def test_ActionModule():

    obj = None

    # Constructor 1:
    # test_ansible_path = os.path.join(os.path.dirname(__file__), '..', '..', 'plugins', 'action')
    # test_ansible_path = os.path.join(test_ansible_path, 'fetch.py')
    # print(test_ansible_path)
    # module_klass = ActionModule.load_action_plugin(test_ansible_path, action_base=ActionModule)
    # obj = module_klass(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Constructor 2:
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 09:56:01.840378
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test run method of class ActionModule """
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    from ansible import context
    import tempfile
    import json

    class ConnectionMock:
        def __init__(self):
            self._shell = None

        def set_shell(self, shell):
            self._shell = shell

        def set_become(self, become):
            self._become = become

        def set_remote_addr(self, remote_addr):
            self._remote_addr = remote_addr

        def join_path(self, *args):
            return self._shell.join_path(*args)

        def fetch_file(self, source, dest):
            source = source.replace('//', '/')

# Generated at 2022-06-13 09:56:09.894859
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest

    class TestActionModule(unittest.TestCase):
        def test_constructor(self):
            def test_play_context(self, *args, **kwargs):
                return "OK"

            display.verbosity = 99
            action_module = ActionModule(display, None, None, 'shell', 'path', None, (1, 2), None, test_play_context, True)
            self.assertEqual(action_module.run, action_module._execute)

    return unittest.TestLoader().loadTestsFromTestCase(TestActionModule)

# Generated at 2022-06-13 09:56:12.733577
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def _load_name(self):
        return 'ActionModule'

    ActionModule._load_name = _load_name
    ActionModule('test', {}, {}, {})

# Generated at 2022-06-13 09:56:24.716181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = AnsibleModule(argument_spec={'src': dict(required=True), 'dest': dict(required=True), 'flat': dict(required=False, type='bool'), 'fail_on_missing': dict(required=False, type='bool'), 'validate_checksum': dict(required=False, type='bool')})
    # set up proper class attribute to test ActionBase; it makes some assumptions on this
    mod.params = {'src': 'somefile', 'dest': 'somedir'}
    # simulate "connection" attribute and method of ActionBase (see comments for ActionBase)
    mod.connection = mock.Mock()
    mod.connection._shell = mock.Mock()
    mod.connection._shell.tmpdir = '/tmp/foo'

# Generated at 2022-06-13 09:56:26.207107
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:56:27.544877
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    pass

# Generated at 2022-06-13 09:56:35.454563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = "fetch"
    src = "abc.txt"
    module_args = {"src":src}
    connection = FakeFetchConnection()
    task_vars = dict()
    tmp = None
    play_context = FakeFetchPlayContext()
    task = FakeFetchTask(module, module_args, play_context)
    result = dict()
    action_module = ActionModule(task, connection, play_context, tmp, task_vars)
    action_module.run(tmp, task_vars)
    assert "changed" in result


# Generated at 2022-06-13 09:57:02.468782
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Run setup to create variables used in all tests.
    with open("tests/modules/action_plugin/action_plugins/fetch/test_action_module_constructor_success.json", 'r') as file:
        test_constructor_success = json.load(file)

    with open("tests/modules/action_plugin/action_plugins/fetch/test_action_module_constructor_failure_invalid_module_utils.json", 'r') as file:
        test_constructor_failure_invalid_module_utils = json.load(file)

    with open("tests/modules/action_plugin/action_plugins/fetch/test_action_module_constructor_failure_invalid_tasks.json", 'r') as file:
        test_constructor_failure_invalid_tasks = json

# Generated at 2022-06-13 09:57:03.414195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:57:05.573933
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise AnsibleActionSkip("No unit test implemented yet")

# Generated at 2022-06-13 09:57:10.621159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Task
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    play_context = PlayContext()

    an_action_module = ActionModule(task=Task(), connection='ssh', play_context=play_context, loader=loader, templar=None, shared_loader_obj=None)

    an_action_module.connection = 'ssh'
    assert isinstance(an_action_module.connection, string_types)

    an_action_module.play_context = play_context
   

# Generated at 2022-06-13 09:57:11.539983
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 09:57:14.425282
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of the class
    test_am = ActionModule()
    # access the method run
    test_am.run()


# Generated at 2022-06-13 09:57:17.038438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a is not None

# Generated at 2022-06-13 09:57:19.149338
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    print(action_module)



# Generated at 2022-06-13 09:57:27.576671
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible import context
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    options = context.CLIOptions()
    options.module_path = 'path/to/ansible/modules'
    variable_manager = VariableManager()
    loader = DataLoader()

    variable_manager.extra_vars = {'hosts': 'testhost'}
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='hosts')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:57:33.435992
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.text.converters import to_text
    from ansible.playbook.task import Task
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.action import ActionBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.cli.adhoc import Ad

# Generated at 2022-06-13 09:58:13.776376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_vars = dict()
    ansible_options = dict()
    ansible_module_name = 'shell'
    args = dict(args='ls -l')

    action = ActionModule(dict(), ansible_vars, ansible_options, ansible_module_name, args, {})
    action.setup()

    assert action.module_args == dict(args='ls -l')
    assert action._play_context.connection == 'local'


# Unit test to exercise the run() method of ActionModule

# Generated at 2022-06-13 09:58:15.007510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Add testing
    return 42

# Generated at 2022-06-13 09:58:20.844678
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Options(object):
        def __init__(self, verbosity=None, start_at_task=None):
            self.verbosity = verbosity
            self.start_at_task = start_at_task

    class Task(object):
        def __init__(self, action=None, task_type=None, args=None):
            self.action = action
            self.task_type = task_type
            self.args = args

    class TaskResult(object):
        def __init__(self, _result=None):
            self._result = _result

        @property
        def result(self):
            return self._result

    class PlayContext(object):
        def __init__(self, check_mode=None, become_user=None, remote_addr=None):
            self.check_mode = check_

# Generated at 2022-06-13 09:58:21.425017
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:28.781926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.pycompat24 import get_exception
    original_display = Display()
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()

    # Replace display with a version that records the output instead of writing it.
    display = Display()
    display.verbosity = 0


# Generated at 2022-06-13 09:58:39.005310
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN: ActionModule instance with src, dest and flat path
    from mock import MagicMock, Mock
    src = "/tmp/src/file.txt"
    dest = "/tmp/dest/file.txt"
    flat = False
    module = ActionModule(task='dummy', connection=MagicMock(), play_context=MagicMock())
    module._connection = Mock()
    module._connection._shell = Mock()
    module._connection._shell.join_path = Mock(return_value="/tmp/src/file.txt")
    module._connection._shell._unquote = Mock(return_value="/tmp/src/file.txt")
    module._remote_expand_user = Mock(return_value="/tmp/src/file.txt")
    module._loader = Mock()

# Generated at 2022-06-13 09:58:47.288917
# Unit test for constructor of class ActionModule
def test_ActionModule():
    TASK = dict(
        action=dict(
            module='raw',
            args=dict(msg='Hello World')
        )
    )

    TASKVARS = dict(foo='bar')
    action = ActionModule(TASK, TASKVARS)
    assert action.task == TASK
    assert action.connection == None
    assert action.runner == None
    assert action.task_vars == TASKVARS
    assert action.tmp == None
    assert action._play_context == None

    action = ActionModule(TASK, TASKVARS)

    assert action._validate_module_name == None
    assert action._task_vars == TASKVARS
    assert action._fail_json == None

    (res, dummy_is_new_facts) = action._execute_

# Generated at 2022-06-13 09:58:57.874499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action import ActionBase

    # Creating an instance of class ActionModule

# Generated at 2022-06-13 09:59:06.720198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    src = "/path/to/src"
    dest = "/path/to/dest"
    class MyException(Exception):
        pass
    class Mock_ActionBase:
        def __init__(self, module_executed):
            self.module_executed = module_executed
        def run(self, tmp=None, task_vars=None):
            assert tmp is None
            assert task_vars == {"a": "10", "b": "20"}
            return {"changed": True, "a": "10", "b": "20"}
        def _execute_remote_stat(self, path, all_vars, follow):
            assert path == "/path/to/src"
            assert all_vars == {'inventory_hostname': 'host42', "a": "10", "b": "20"}
            assert follow

# Generated at 2022-06-13 09:59:10.900092
# Unit test for constructor of class ActionModule
def test_ActionModule():

    def test_get_checksum():
        action = ActionModule(task=None)
        assert action.get_checksum(None) is None
        assert action.get_checksum({'checksum': 'A0'}) == 'A0'
        assert action.get_checksum({'checksum': None, 'sha1sum': 'B0'}) == 'B0'

# Generated at 2022-06-13 10:00:37.898766
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing for ActionModule constructor')
    assert True

# Generated at 2022-06-13 10:00:41.766997
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # TODO: Complete unit test for method run of class ActionModule in file plugins/action/fetch.py
    assert False

# Generated at 2022-06-13 10:00:49.089926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ minimal test for module run using ActionModule """
    import tempfile
    # create a fake module
    test_dir = tempfile.mkdtemp()
    f = open(test_dir + 'test_file', 'w')
    f.close()
    my_result = {'msg': '', 'rc': 0, 'results': '', 'invocation': {'module_name': 'ansible.legacy.slurp', 'module_args': {}}, 'item': '', 'checksum': '1234567890', 'file': '/file/name', 'stdout': ''}
    my_action = ActionModule()

# Generated at 2022-06-13 10:00:57.604681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.connection.connection_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=[]),
        variable_manager=VariableManager(),
        loader=DataLoader(),
        passwords={},
        stdout_callback='default',
    )
    p = Play().load({}, DataLoader(), tqm)

# Generated at 2022-06-13 10:01:07.527611
# Unit test for method run of class ActionModule
def test_ActionModule_run(): # ActionModule
    from ansible.plugins.action.copy import ActionModule
    from ansible.module_utils.connection.implicit import _set_file_attributes
    from ansible.module_utils.remote_management.slurp import SlurpModule
    from ansible.module_utils.parsing.convert_bool import boolean
    import shutil, tempfile

    # Test with a directory that doesn't exist
    dummydir = tempfile.mkdtemp() + '/testdir'
    try:
        shutil.rmtree(dummydir)
    except OSError:
        pass
    am = ActionModule('test', dict(src=dummydir, dest='/tmp'), False, '/tmp', False, {}, False, None)
    res = am.run(task_vars=dict())

# Generated at 2022-06-13 10:01:08.848864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()


# Generated at 2022-06-13 10:01:10.708637
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    c = ActionModule()
    assert c.run() == 'test'

# Generated at 2022-06-13 10:01:19.764481
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up test members
    mocker = Mocker()
    action_module = ActionModule()

    tmp = mocker.mock()
    task_vars = dict()

    # Set up context manager mocks
    result = mocker.mock()
    run_result = mocker.mock()
    result.update(run_result)
    (ActionBase.run(tmp, task_vars)
        .result(result))
    mocker.replay()

    # Set up context manager mocks
    args = dict()
    args["src"] = "test_src"
    args["dest"] = "test_dest"
    args["flat"] = False
    args["fail_on_missing"] = False
    args["validate_checksum"] = True

# Generated at 2022-06-13 10:01:29.393189
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Constructor for class ActionModule
    """

    # test with valid connection and task
    test_connection = 'connection'
    test_task = 'task'
    test_tmp = 'tmp'
    test_play_context = 'play_context'
    test_loader = 'loader'
    test_templar = 'templar'
    test_shared_loader_obj = 'shared_loader_obj'
    test_final_q = 'final_q'

    try:
        action_module = ActionModule(test_connection, test_task, test_tmp, test_play_context, test_loader,
                                     test_templar, test_shared_loader_obj, test_final_q)
    except Exception as e:
        raise Exception('Failed to create ActionModule object') from e

# Generated at 2022-06-13 10:01:32.680645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up parameters
    tmp = None
    task_vars = None
    AM = ActionModule(None, None, None)
    assert not AM.run(tmp, task_vars)

# Generated at 2022-06-13 10:04:47.155077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup test ActionModule object
    m = ActionModule()
    m._connection = FakeTestConnection()
    m._task = FakeTestTask()
    m._play_context = FakeTestPlayContext()
    m._loader = FakeTestDataLoader()
    m._templar = FakeTestTemplar()
    m._shared_loader_obj = None # Not used
    return m

# Generated at 2022-06-13 10:04:47.640903
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:04:48.138766
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:04:54.897786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    loader_mock = {}
    class PlayContext:
        def __init__(self, remote_addr='remote_addr'):
            self.remote_addr = remote_addr
    class Task:
        def __init__(self, module_name='module_name', args={}):
            self.module_name = module_name
            self.args = args
    class Connection:
        def __init__(self, become=False, tmpdir='tmpdir'):
            self.become = become
            self._shell = Shell()
            self._shell.tmpdir = tmpdir
        def _shell_quote(self, data):
            return "shell_quote(%s)" % data
        def _shell_unsafe(self, data):
            return "shell_unsafe(%s)" % data

# Generated at 2022-06-13 10:05:09.328936
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModuleHelper()
    module.set_defaults(**{'src': 'test.src', 'dest': 'test.dest', 'flat': False, 'validate_checksum': True})
    module.mock_shell()
    module.mock_connection()
    module.set_module_args()

    fetch_module = ActionModule(module, 'fetch')

    fetch_module.run(tmp='tmppath', task_vars={})

    module._shell.join_path.assert_called_with('test.src')
    module._remote_expand_user.assert_called_with('test.src')
    module._execute_remote_stat.assert_called_with('test.src', all_vars={}, follow=True)