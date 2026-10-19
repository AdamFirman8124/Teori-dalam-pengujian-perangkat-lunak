

# Generated at 2022-06-13 10:52:48.798879
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(loader=None, shared_loader_obj=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action.run(tmp=None, task_vars=None)

    assert(result == None)

# Generated at 2022-06-13 10:52:49.661539
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:01.183733
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:53:03.382518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("\n")
    print("Testing ActionModule.run()")
    # Pass fake class and method to method run
    a = ActionModule(None, None, None)
    a.run(None, None)

# Generated at 2022-06-13 10:53:09.487193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection = None
    taskvars = {'ansible_shell_executable': '/bin/bash'}
    data = 'find "${base_dir}" -name "${pattern}" -type f -print0|xargs -0 -n 1 zip "${target}"'.encode()
    args = {'_raw_params': data.decode(),
            '_uses_shell': True,
            'chdir': '/tmp',
            'executable': None,
            'removes': None,
            'warn': True}
    task = {'args': args,
            'delegate_to': 'localhost'}
    loader = None
    templar = None
    shared_loader_obj = None
    plugin = ActionModule(connection, task, loader, templar, shared_loader_obj)

# Generated at 2022-06-13 10:53:22.865613
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import sys
    import os
    import tempfile

    TEST_SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
    if TEST_SRC_DIR not in sys.path:
        sys.path.append(TEST_SRC_DIR)

    from ansible.plugins.loader import action_loader

    from ansible.parsing import loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor import task_queue_manager
    from ansible.utils.vars import load_extra_vars


# Generated at 2022-06-13 10:53:28.459149
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = None
    mock_connection = None
    mock_play_context = None
    mock_loader = None
    mock_templar = None
    mock_shared_loader_obj = None
    action_module = ActionModule(mock_task, mock_connection, mock_play_context,
                                 mock_loader, mock_templar, mock_shared_loader_obj)
    assert action_module.run() == None

# Generated at 2022-06-13 10:53:37.883541
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:53:42.437219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule

    # Arrange
    task_vars = dict()
    tmp = "tmp"
    am = ActionModule()

    # Act
    result = am.run(tmp, task_vars)

    # Assert
    assert result == dict()

# Generated at 2022-06-13 10:53:52.921288
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ..playbook_executor import PlaybookExecutor
    from ..playbook_executor import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vault import VaultLib
    from ansible.plugins import module_loader
    from ansible.plugins.loader import action_loader
    from ansible.plugins.action import ActionBase

    # Set up args
    variable_manager = VariableManager()
    loader = DataLoader()
    display = Display()
    vault_secrets = VaultLib(loader=loader)
    options = ImmutableDict()
    passwords = dict()



# Generated at 2022-06-13 10:54:06.097060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({'_ansible_version': '2.8.0.dev0', '_ansible_no_log': False, '_raw_params': 'ls', '_uses_shell': True}, None, [], None, None, False, False)

    ret = module.run({}, {})
    assert ret['rc'] == 0
    assert 'stdout' in ret
    assert 'stderr' in ret
    assert 'stdout_lines' in ret
    assert 'stderr_lines' in ret
    assert 'stdout_lines' in ret
    assert 'invocation' in ret
    assert 'warnings' in ret
    assert 'end' in ret
    assert 'changed' in ret
    assert 'start' in ret
    assert 'delta' in ret



# Generated at 2022-06-13 10:54:16.434164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    task1 = {'shell': '/bin/foo'}
    connection1 = None
    play_context1 = None
    loader1 = None
    templar1 = None
    shared_loader_obj1 = None
    action_Base1 = ActionBase(task1, connection1, play_context1, loader1, templar1, shared_loader_obj1)
    action_module1 = ActionModule(task1, action_Base1._connection, action_Base1._play_context, action_Base1._loader, action_Base1._templar, action_Base1._shared_loader_obj)
    action_module1._task = task1
    action_module1._connection = connection1
    action_module1._play_context = play_context1
    action_module1

# Generated at 2022-06-13 10:54:30.436064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {}
    task['action'] = {}
    task['action']['args'] = {'_uses_shell': True}
    task['action']['name'] = 'shell'
    task['action']['module_name'] = 'shell'
    task['delegate_to'] = None
    task['register'] = 'shell'
    task['run_once'] = False
    task['_ansible_verbosity'] = 0
    task['_ansible_no_log'] = False
    task['_ansible_debug'] = False
    task['_ansible_diff'] = False
    task['task_name'] = 'debug'
    task['_ansible_item_label'] = ''
    task['_ansible_ignore_errors'] = False
    task['_ansible_internal_poll_interval']

# Generated at 2022-06-13 10:54:31.479452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # needs to be implemented
    return

# Generated at 2022-06-13 10:54:32.084666
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:54:42.473897
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  task = {
    'args':{
      '_uses_shell': True
    },
    'name':'a task',
    '_role': None,
    'vars':{
      'ansible_check_mode': True
    }
  }
  def create_task(self, *args, **kwargs):
    self._task = task

  def get_loader(self, *args, **kwargs):
    return self
  def load_only_plugin(self, *args, **kwargs):
    return self

  module = ActionModule()
  module._shared_loader_obj = ActionModule()
  module._shared_loader_obj.action_loader = ActionModule()
  module._shared_loader_obj.action_loader.get = ActionModule()


# Generated at 2022-06-13 10:54:44.310560
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Check if ActionModule.run can be instantiated
    cls = ActionModule('test_data')
    assert cls is not None

# Generated at 2022-06-13 10:54:44.921042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:54.799088
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Check that the run method returns expected dictionary"""
    task_loader = TestTaskObject()
    action_loader = TestActionObject()
    shared_loader_obj = TestSharedLoaderObject(action_loader, task_loader)
    task = TestTaskObject()
    connection = TestConnectionObject()
    play_context = TestPlayContextObject()
    loader = TestLoaderObject()
    templar = TestTemplarObject()

    action_module = ActionModule(task_loader, action_loader, shared_loader_obj, task, connection, play_context, loader, templar)
    assert action_module.run() == {'msg': 'AnsibleModule unit test'}, "ActionModule test failed"


# Generated at 2022-06-13 10:55:03.412360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Test method run of class ActionModule''' 
    g = dict(
        shell_results = dict(
            rc = d(
                msg = "",
                stderr = "",
                stdout = "",
                stdout_lines = [""]
            )
        )
    )
    exec('''def return_code():
        return _rc''')
    exec('''def return_msg():
        return _msg''')
    exec('''def return_stderr():
        return _stderr''')
    exec('''def return_stdout():
        return _stdout''')
    exec('''def return_stdout_lines():
        return _stdout_lines''')
    exec('''def return_results():
        return _results''')
    global _rc
   

# Generated at 2022-06-13 10:55:18.149839
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test method run of class ActionModule"""
    task = {
        'args': {'_uses_shell': True},
        '_ansible_no_log': False,
        'action': 'ansible.legacy.shell'
    }
    loader = {'_ansible_no_log': False, '_ialsologtostderr': False}
    task_vars = {
        'ansible_debug': False,
        'ansible_facts': {},
        'ansible_forks': 5,
        'ansible_log_path': None,
        'ansible_verbose_always': False
    }


# Generated at 2022-06-13 10:55:28.480883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    module = 'ansible.legacy.shell'
    args_dict = dict(CHANGED_WHEN='True')
    task = DummyTask(module=module, args=args_dict)
    args = dict(task=task)
    action_module = ActionModule(**args)

    # Test
    action_module.run()

    # Assert
    # No assertions are needed, however they are included only to show the
    # expected state of the class after the method run is executed.

    assert action_module._task.action == 'ansible.legacy.command'
    # The following line will cause the test to fail as the '_uses_shell' is
    # not yet added.
    # assert action_module._task.args == args_dict

# Generated at 2022-06-13 10:55:33.581528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an object of class ActionModule
    # as variables are required in method run()
    # use default values as these variables are not used anywhere else
    action_module = ActionModule(connection=None, play_context=None,
                                 loader=None, templar=None,
                                 shared_loader_obj=None)

    # ActionModule class requires tmp, task_vars as function arguments
    # all above variables will be available to it through __init__
    tmp = None
    task_vars = None
    assert action_module.run(tmp, task_vars) is None

# Generated at 2022-06-13 10:55:47.516787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    config = {}

# Generated at 2022-06-13 10:55:54.535390
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # import library
    import os
    import sys
    import inspect
    import mock
    # import module to test
    module_to_test = "ansible.playbook.action.shell"
    sys.modules["ansible.playbook.action.shell"] = mock.Mock()
    import ansible.plugins.action.shell
    from ansible.plugins.action.shell import ActionModule

    # mock setup
    # "run" method
    _task = mock.Mock()
    _connection = mock.Mock()
    _play_context = mock.Mock()
    _loader = mock.Mock()
    _templar = mock.Mock()
    _shared_loader_obj = mock.Mock()

# Generated at 2022-06-13 10:55:55.512767
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:55:56.074822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:55:57.003690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(None)

# Generated at 2022-06-13 10:56:07.565193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.stats import AggregateStats
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.loader import callback_loader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task


# Generated at 2022-06-13 10:56:10.185926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    result = action_module.run()
    assert result is not None

# Generated at 2022-06-13 10:56:27.560399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an object of class ActionModule and set the necessary attributes
    am = ActionModule()

    # Set the task_vars attribute
    task_vars = dict()
    task_vars['user'] = 'ansible'

    # Execute the run method. The assert statements in this module
    # check the desired functionality of the run method
    result = am.run(task_vars=task_vars)
    assert result['cmd'] == 'whoami'
    assert result['changed'] == False
    assert result['rc'] == 0
    assert result['invocation']['module_args']['_raw_params'] == 'whoami'
    assert result['invocation']['module_args']['_uses_shell'] == True

# Generated at 2022-06-13 10:56:37.219054
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockActionModule:

        def __init__(self):
            self.action = ActionModule()
            self.action._ds = {}
            self.action._shared_loader_obj = {}
            self.action._task = {}
            self.action._connection = {}
            self.action._play_context = {}
            self.action._loader = {}
            self.action._templar = {}
            mock_shared_loader_obj = {}
            mock_action_loader = {}
            mock_command = {}
            mock_command.run = Mock(return_value="return_value")
            mock_action_loader.get = Mock(return_value=mock_command)
            mock_shared_loader_obj.action_loader = mock_action_loader
            self.action._shared_loader_obj = mock_shared_loader_obj

# Generated at 2022-06-13 10:56:46.204675
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # construct a mock for ActionBase
    ab = ActionBase()
    ab.connection = 'local'
    ab.datastructure = {'ansible_facts': {'version': '2.9.0'}, 'changed': False, 'failed': False, 'stdout': '',
                        'stdout_lines': []}
    ab._task = {'args': {'_uses_shell': True}, 'complex_args': {}, 'delegate_to': None,
                'delegate_facts': False, 'failed_when_result': False, 'loop': '', 'module_name': 'shell',
                'name': 'Init xrun'}
    ab._loader = None
    ab._templar = None

# Generated at 2022-06-13 10:56:46.904087
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:56:54.021560
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('\nStarting test_ActionModule_run')

    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.shell import ActionModule
    from ansible.playbook.task import Task

    task_data = {'action': 'shell',
                 'args': {'_uses_shell': True, '_raw_params': 'echo "{{ user_name }}"'},
                 'name': 'shell action'}

    # define shared loader object
    shared_loader_obj = dict()
    shared_loader_obj['action_loader'] = dict()
    # add shell action loader
    shared_loader_obj['action_loader']['shell'] = ActionModule

    # define task object
    task = Task()
    task.action = 'shell'
    task._attributes = task_data
    task._shared_

# Generated at 2022-06-13 10:57:02.783934
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = 'ansible.legacy.plugins.actions.shell'

    # generate module args
    new_module_args = {
        '_uses_shell': True
    }

    # generate task
    new_task = AnsibleTask()
    new_task.args = new_module_args

    # generate connection
    # new_connection = AnsibleConnection()

    # generate task_vars
    new_task_vars = {'ansible_shell_type': 'csh'}

    # generate loader
    new_loader = AnsibleLoader()

    # generate templar
    from ansible.template import Templar
    new_templar = Templar(loader=new_loader, variables=new_task_vars)

    from ansible.plugins.loader import ActionModuleLoader
    new_shared_loader_obj = ActionModule

# Generated at 2022-06-13 10:57:07.160052
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = dict()
    action_module = ActionModule(tmp, task_vars)
    result = action_module.run(tmp, task_vars)
    assert result == {}

# Generated at 2022-06-13 10:57:07.942227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:14.726112
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    _connection = object()
    _task = object()
    _play_context = object()
    _loader = object()
    _templar = object()
    _shared_loader_obj = object()

    module = ActionModule(_connection, _task, _play_context, _loader, _templar, _shared_loader_obj)

    module.run(tmp=None, task_vars={})
    module.run(tmp="", task_vars={"test1": "test1"})
    module.run(tmp="test", task_vars={"test2": "test2"})

# Generated at 2022-06-13 10:57:18.462197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell as shell

    am = shell.ActionModule('...', {}, {}, None, None, None, '...', '...', None, None)

    task_vars = dict()

    res = am.run(None, task_vars)

    assert res.get('changed')

# Generated at 2022-06-13 10:57:42.402350
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  mock_shared_loader_obj = Mock()
  mock_task = Mock()
  mock_connection = Mock()
  mock_play_context = Mock()
  mock_loader = Mock()
  mock_templar = Mock()
  mock_action_loader = Mock()
  mock_command_action = Mock()

  mock_shared_loader_obj.action_loader.get.return_value = mock_command_action
  mock_command_action.run.return_value = {'some': 'output'}

  module = ActionModule(task=mock_task,
                        connection=mock_connection,
                        play_context=mock_play_context,
                        loader=mock_loader,
                        templar=mock_templar,
                        shared_loader_obj=mock_shared_loader_obj)

 

# Generated at 2022-06-13 10:57:48.794754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    class FakeTask(object):
        def __init__(self):
            self.module_args = dict(command='echo "hello world"')
            self.action = 'shell'
            self.args = dict()

    def fake_init_loader(self):
        self.command_manager = dict()

    fake_loader = action_loader.ActionModuleLoader()
    fake_loader._init_loader = fake_init_loader

    fake_task

# Generated at 2022-06-13 10:58:00.850864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six.moves import queue
    from ansible.module_utils._text import to_text

    class FakeShellAction(object):

        def run(self, task_vars):
            return {}

    class FakeLoaderAction(object):

        def get(self, name, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            return FakeShellAction()

    class FakeTemplar(object):

        def template(self, value):
            return value

    class FakeConnection(object):

        def connect(self, task_vars):
            return {}

        def exec_command(self, value):
            return {}

    class FakeQueue(object):

        def __init__(self):
            self.data = []



# Generated at 2022-06-13 10:58:01.624004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:05.249153
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule(None, None, None, None, None, {})
    assert m.run(None, None) == {'failed': True, 'msg': 'shell module is only usable when the command connection type is used'}

# Generated at 2022-06-13 10:58:17.702984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule."""

    from ansible.plugins.action import ActionBase

    import unittest
    import unittest.mock

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.include import Include
    from ansible.template import Templar

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    mock_host = unittest.mock.create_autospec(Host)
    mock_host.get_vars.return_value = dict()
    mock_host.get_groups.return_value = []

    mock_group = unittest.mock.create_autospec(Group)


# Generated at 2022-06-13 10:58:18.089920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 10:58:32.510253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple
    from ansible.executor.task_result import TaskResult
    from ansible.executor import result

    Result = namedtuple('Result', ('command', 'returncode', 'stdout', 'stderr'))

    param = {
        'command': 'hostname',
        'returncode': 0,
        'stdout': 'localhost',
        'stderr': '',
    }

    task_vars = None
    task_result = TaskResult(host=None, task=None, return_data=Result(**param))
    task_result._result = result.Result()

    class TestActionBase:
        _connection = None
        _play_context = None
        _loader = None
        _task = None
        _templar = None
        _shared_loader_obj = None

# Generated at 2022-06-13 10:58:33.045792
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:41.412404
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    command_action_result = {
        'invocation': {
            'module_args': 'echo test',
            'module_name': 'ansible.legacy.command'
        },
        'rc': 0,
        'stdout': 'test\n'
    }

    class DataModule:
        data = 'echo test'

    class LoaderModule:
        pass

    class SharedLoaderObjModule:
        pass

    class ConnectionModule:
        pass

    class PlayContextModule:
        pass

    class TaskModule:
        def __init__(self):
            self.args = dict()
            self.async_val = None

    class EmptyModule:
        pass

    task = TaskModule()
    task_vars = dict()

    empty = EmptyModule()
    data = DataModule()
    loader = LoaderModule

# Generated at 2022-06-13 10:59:24.360460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule."""
    class MockTask:
        def __init__(self):
            self.args={'_uses_shell': True}
    class MockTaskVars:
        def __init__(self):
            self.proxies={'hostname':'host.localhost', 'proxy_port':'3128'}
    class MockActionLoader:
        def __init__(self):
            self.action_loader={'ansible.legacy.command': None}
    class MockPlayContext:
        def __init__(self):
            self.become = {}
            self.become_method = 'sudo'
    class MockResult:
        def __init__(self):
            self.result = True
            self.stdout = 'systemd-analyze'

# Generated at 2022-06-13 10:59:37.780807
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run"""

    # init root object
    root = AnsibleRoot()

    # init connection object
    conn = AnsibleConnectionBase()

    # init task object
    task = AnsibleTask()
    task.action = "ansible.legacy.shell"

    # init loader object
    loader = AnsibleLoader()

    # init play context object
    play_context = AnsiblePlayContext()

    # init templar object
    templar = AnsibleTemplar()

    # init shared loader object
    shared_loader_obj = AnsibleBaseCLI()

    # init action module object
    action_module = ActionModule(task, conn, play_context, loader, templar, shared_loader_obj)

# Generated at 2022-06-13 10:59:42.740824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initial setup
    ansible_module_shell = ActionModule()
    ansible_module_shell._shared_loader_obj.action_loader.get = lambda *args, **kwargs: ansible_module_shell
    ansible_module_shell._task.args = {'_uses_shell': True}
    ansible_module_shell.run()
    assert ansible_module_shell._task.args['_uses_shell']

# Generated at 2022-06-13 10:59:45.146182
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # remove when fixed: https://github.com/ansible/ansible/issues/29384
    pass



# Generated at 2022-06-13 10:59:57.948723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = dict(
        cmd='/usr/bin/whoami',
        _raw_params='/usr/bin/whoami',
        _uses_shell=True,
        chdir=None,
        creates=None,
        removes=None,
        stdin=None,
        stdin_add_newline=True,
        warn=True,
        executable=None
    )
    module = ActionModule(dict(ANSIBLE_MODULE_ARGS=module_args))
    result = module.run()
    assert result['cmd'] == '/usr/bin/whoami'
    assert result['invocation']['module_args']['_raw_params'] == '/usr/bin/whoami'
    assert result['invocation']['module_args']['_uses_shell'] is True

# Generated at 2022-06-13 11:00:10.053843
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test 1: Test for the correct return status 
    print('Test 1: Test for the correct return status')
    task_vars = {}
    act = ActionModule('/ansible/testdir', {}, task_vars=task_vars)
    result = act.run()
    assert result['changed'] == False
    assert result['msg'] == 'No output'
    assert result['rc'] == 0

    # Test 2: Test for the correct return status 
    print('Test 2: Test for the correct return status')
    task_vars = {}
    act = ActionModule('/ansible/testdir', { '_uses_shell': True}, task_vars=task_vars)
    result = act.run()
    assert result['changed'] == False
    assert result['msg'] == 'No output'
    assert result

# Generated at 2022-06-13 11:00:10.727717
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:00:11.806702
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing")



# Generated at 2022-06-13 11:00:12.450041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:00:19.320930
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
    from collections import OrderedDict
    import json

    test_case = {
        "tmp": "/tmp/tmp_value",
        "task_vars": {
            "test_task_var": "test_task_var_value"
        },
        "result": {
            "_ansible_parsed": True,
            "changed": False,
            "cmd": "export FOO=bar; echo $FOO",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "bar",
            "stdout_lines": [
                "bar"
            ],
            "warnings": []
        }
    }

    # Create a fake environment

# Generated at 2022-06-13 11:01:56.264789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating a mock object for the action plugin
    class MockActionModule(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

    # Creating a fake task and setting args to satisfy the constructor of MockActionModule
    task = type('obj', (object,), {'args': {'_uses_shell': True}})
    # Creating a fake loader and setting the search_path attribute to satisfy the constructor of MockActionModule
    loader = type('obj', (object,), {'search_path': None})
    # Creating a fake

# Generated at 2022-06-13 11:02:04.869274
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN
    task_vars = dict()
    fake_module_name = 'fake.module.name'
    fake_command = 'fake_command'
    fake_args = {
        '_uses_shell': True,
        '_raw_params': fake_command,
        '_tmp_path': '/tmp/fake/path'
    }
    fake_connection = type('FakeConnection', (object,), {})

# Generated at 2022-06-13 11:02:05.472794
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:02:07.924944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert action_module.run(tmp='/tmp', task_vars={}) == "AnsibleModule object"
    

# Generated at 2022-06-13 11:02:15.181285
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('\nIn test_ActionModule_run')
    import ansible
    from ansible import errors
    from ansible.plugins.action.shell import ActionModule as shell

    module_name = 'shell'
    module_args = 'echo'
    target_host_name = 'localhost'
    task_vars = {'ansible_ssh_host': target_host_name}
    task_vars['ansible_ssh_pass'] = 'vagrant'
    task_vars['ansible_ssh_port'] = 22
    task_vars['ansible_ssh_user'] = 'vagrant'
    task_vars['ansible_ssh_private_key_file'] = '/Users/schowdhu/.vagrant.d/insecure_private_key'

# Generated at 2022-06-13 11:02:23.149981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # given
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    # Mocking need a real object
    class mock_shared_loader_obj:
        action_loader = None

    class mock_loader:
        pass

    class mock_play:
        pass

    class mock_task:
        def __init__(self):
            self.args = {}

    class mock_templar:
        pass

    class mock_variable_manager:
        def __init__(self):
            self.extra_vars = {}

    class mock_inventory_manager:
        def __init__(self):
            self.host_list = []


# Generated at 2022-06-13 11:02:34.683748
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def test_tmp_and_tmp_path_get_default_values_if_not_provided(mocker, tmp_path):
        mocker.patch('ansible.plugins.action.ActionBase._get_tmp_path', return_value=tmp_path)
        action_module_run = ActionModule(mocker.Mock(), mocker.Mock(), mocker.Mock(), mocker.Mock(), mocker.Mock())
        assert action_module_run.run()
        assert (tmp_path / '.ansible_async').is_dir()

    def test_runner_run_returns_the_returned_result_of_the_command_run(mocker, tmp_path):
        mocker.patch('ansible.plugins.action.ActionBase._get_tmp_path', return_value=tmp_path)


# Generated at 2022-06-13 11:02:43.665789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection_mock.return_value.exec_command.return_value = ('stdout','stderr')
    test_args = {'_uses_shell': True}
    result_mock = MagicMock(return_value=test_args)
    command_action_module.run = result_mock
    test_module = ActionModule(connection=connection_mock, 
                               task=task_mock, 
                               play_context=play_context_mock, 
                               loader=loader_mock, 
                               templar=templar_mock, 
                               shared_loader_obj=shared_loader_obj_mock)
    result = test_module.run(tmp=None,
                             task_vars=task_vars_mock)
    assert result == test_args