

# Generated at 2022-06-13 10:52:40.882007
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	module = ActionModule()
	module.run()

# Generated at 2022-06-13 10:52:51.920091
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up required mocks
    fake_task = FakeTask()
    fake_connection = FakeConnection()
    fake_play_context = FakePlayContext()
    fake_loader = FakeLoader()
    fake_templar = FakeTemplar()
    fake_shared_loader_obj = FakeSharedLoaderObj(fake_loader)

    # Create instance of class under test
    action_module_instance = ActionModule(fake_task, fake_connection, fake_play_context, fake_loader, fake_templar, fake_shared_loader_obj)

    # Create mocks to be returned by mocks used by class under test
    # and mock out those mocks
    fake_command_action = FakeCommandAction()
    fake_command_module = FakeCommandModule(fake_command_action)
    fake_shared_loader_obj.action_

# Generated at 2022-06-13 10:53:05.737978
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    task_name = 'name'
    task_vars = {'a': 'A'}
    action_module = ActionModule(task=task_name, connection=None,
                                 play_context=None, loader=None, templar=None, shared_loader_obj=None)
    mock_task = Mock()
    action_module._task = mock_task
    
    action_module._task.args = {}
    mock_loader = Mock()
    action_module._loader = mock_loader
    mock_loader.action_loader = Mock()
    mock_ansible_legacy_command = Mock()
    mock_ansible_legacy_command.run = Mock(return_value='ok')

# Generated at 2022-06-13 10:53:13.845771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._shared_loader_obj = type("a", (object,), {})
    a = ActionModule()

    CommandModule = type("CommandModule", (object,), {})
    a._shared_loader_obj.action_loader = type("b", (object,), {
        'get': lambda self, action: CommandModule(),
    })
    a._task = type("c", (object,), {
        'args': {},
    })
    a._connection = "d"
    a._play_context = "e"
    a._templar = "f"
    a._loader = "g"

    CommandModule.run = lambda self, task_vars: True

    assert a.run(tmp="h", task_vars="i") is True


# Generated at 2022-06-13 10:53:26.262821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.context import Connection
    from ansible.context import CLIArgs
    from ansible.plugins.action.shell import ActionModule
    import json
    import pytest
    
    class DummyConnection:
        def connect(self, host, port, username, password,
                    host_key, host_key_auto_add, timeout, look_for_keys):
            pass

    class DummyCLIArgs:
        def __init__(self):
            self.verbosity = 1
            self.inventory = "tests/unit/data/inventory"
            self.connection = "local"

# Generated at 2022-06-13 10:53:36.298951
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.network.common.config import NetworkConfig
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play

# Generated at 2022-06-13 10:53:47.151354
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionModule.run()")

    fake_loader = "fake_loader"
    fake_templar = "fake_templar"
    fake_shared_loader_obj = "fake_shared_loader_obj"
    fake_play_context = "fake_play_context"
    fake_task = "fake_task"
    fake_connection = "fake_connection"
    fake_task_vars = "fake_task_vars"

    action_module = ActionModule(fake_loader, fake_templar, fake_shared_loader_obj, fake_play_context, fake_task, fake_connection)
    result = action_module.run(fake_task_vars)
    assert result["invocation"]["module_args"]["_uses_shell"] == True

# Generated at 2022-06-13 10:53:56.017346
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class VarsModule:

        class Vars:

            def __init__(self):
                self.ansible_check_mode = False


    class TaskModule:

        def __init__(self):
            self.args = {'_raw_params': 'echo "success"'}
            self.set_loader(None)
            self.set_task_vars(None)

        def set_loader(self, loader):
            self.loader = loader

        def set_task_vars(self, task_vars):
            self.vars = task_vars


    class SharedLoaderObjModule:

        class ActionLoaderModule:

            def get(self, command, task, connection, play_context, loader, templar, shared_loader_obj):
                pass


# Generated at 2022-06-13 10:54:07.339703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import shutil
    import tempfile
    import ansible.plugins.loader
    import ansible.plugins.action
    import ansible.module_utils

    class ShellModule(object):
        def __init__(self, ansible_module):
            self.ansible_module = ansible_module

    class TempDir(object):
        def __init__(self, prefix=None):
            self.prefix = prefix
            self.path = tempfile.mkdtemp(self.prefix)

        def __enter__(self):
            return self.path

        def __exit__(self, exc_type, exc_val, exc_tb):
            shutil.rmtree(self.path)


# Generated at 2022-06-13 10:54:12.446230
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # empty task
    task = {'args': {}}
    task_vars = {}

    # empty task
    action_module = ActionModule(task, {}, {'task_vars': task_vars}, {}, {}, {})
    result = action_module.run(task_vars=task_vars)
    assert result == {'msg': '', 'stdout': ''}

# Generated at 2022-06-13 10:54:28.186053
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.module_utils import basic
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import connection_loader
    import tempfile
    #import test.support.os_helper as helper

    results = dict()
    results['failed'] = False
    class mock_loader_obj(object):
        def __init__(self):
            self.action_loader = ActionBase
        #def load_from_file(self, file):
        #    return ActionBase
        #def get_action(self, action_name, task, connection, play_context, loader, templar, shared_loader_obj

# Generated at 2022-06-13 10:54:34.652832
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(loader=None, play_context=None, new_stdin=None, connection=None, shell=None,
                                 templar=None, shared_loader_obj=None)
    with pytest.raises(AttributeError, match=r".* object has no attribute '_task'$"):
        # test __init__ method of class ActionModule
        action_module.run()

# Generated at 2022-06-13 10:54:35.018670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:35.642907
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO

# Generated at 2022-06-13 10:54:36.296919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:36.898391
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:37.617203
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:45.845744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {'_ansible_version': '2.8.0', '_ansible_no_log': False, '_raw_params': '', '_ansible_parsed': True, 'ansible_loop_var': 'item', '_ansible_module_name': 'shell', '_ansible_module_set': True, '_ansible_mods_cache': {'ansible.legacy.shell': {'args': {'chdir': None, 'creates': None, 'executable': None, 'free_form': 'echo "Hello World!"', 'removes': None, 'warn': True}, 'action': 'ansible.legacy.shell', 'name': 'shell', 'type': 'action', 'was_loaded': True}}}

# Generated at 2022-06-13 10:54:55.494900
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  print("call test_ActionModule_run")
  tmp_path = '/tmp/test/path'
  task_vars = dict(tmp='/tmp/test/path')

  am = ActionModule()

  def_tmp = '/test/path'
  def_task_vars = dict(tmp='/test/path')
  amm = am.run(def_tmp, def_task_vars)

  # def_tmp should be overwritten by tmp_path
  assert(amm == dict(
          tmp='/tmp/test/path',
          msg="Hello World!"
  ))


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:55:03.860627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test1_sample_taskvars contains the variable 'msg1'
    task_vars = {'msg1': 'Test message 1'}
    test1_sample_taskvars = task_vars
    action = ActionModule(None, None, None)
    # Now call the run method of this class with the test_loader object of Ansible
    # (Note: We cannot create an object of this class directly, as there are a lot of dependencies)
    result = action.run(tmp=None, task_vars=test1_sample_taskvars)
    # assert that the run method returns a dictionary of variables
    assert isinstance(result, dict), "The result should be a dictionary"
    # assert that the run method returns the correct value of msg1
    assert result.get('msg1') == 'Test message 1'

# Generated at 2022-06-13 10:55:11.498765
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a class instance
    action_module = ActionModule()

    # Create a empty task
    task = {"name": "example_task"}

    # Configure the task
    action_module._task = task

    # Call the run method with a example payload
    action_module.run()

# Generated at 2022-06-13 10:55:12.105239
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:20.970113
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Start test
    import pytest
    F = pytest.mark.parametrize('method',['_execute_module', '_execute_module_repl'])

    @F
    def test_execute_module(self,mocker,transport,connection,method):
        runner = mocker.patch(connection + '.run')
        runner.return_value = 5,b'{"failed": "True"}', b''
        a = ActionModule(transport,'/tmp',connection,1,'ansible.legacy.ping')
        a._task.args['_raw_params'] = b"echo hello"
        a._task.args['_uses_shell'] = True
        a._task.args['chdir'] = '/tmp'
        a._task.args['creates'] = None


# Generated at 2022-06-13 10:55:21.579884
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	pass

# Generated at 2022-06-13 10:55:22.633678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:55:31.229452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """

    # Paths to the source code of the respective class

# Generated at 2022-06-13 10:55:38.606788
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    shell_command = "echo test"
    play_context = None
    task = None

    command_action_run = None
    command_action = None
    action_module = ActionModule()
    action_module._task = task
    action_module._play_context = play_context
    action_module._shared_loader_obj.action_loader.get = Mock(return_value=command_action)
    command_action.run = Mock(return_value=command_action_run)
    action_module.run(None, None)
    command_action.run.assert_called_with(task_vars=None)

# Generated at 2022-06-13 10:55:39.448351
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run called")

# Generated at 2022-06-13 10:55:47.184094
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action as action
    class FakeActionBase(action.ActionBase):
        def __init__(self):
            self.result = dict(changed=True)
    class FakeActionModule(ActionModule):
        def __init__(self):
            self.action = FakeActionBase()
    module = FakeActionModule()
    result = module.run(task_vars=None)
    assert result == {'changed': True}

# Generated at 2022-06-13 10:55:49.554643
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    modinstance = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    modinstance.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:56:09.814207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Dummy case where module_name does not exist
    from ansible.plugins.action.shell import ActionModule

    print("Test Start:")
    # dummy var to hold module args
    module_args = {}
    module_args["_ansible_verbosity"] = 4
    module_args["_ansible_no_log"] = False
    module_args["_ansible_debug"] = False
    module_args["_ansible_diff"] = False
    module_args["_uses_shell"] = False
    module_args["chdir"] = None
    module_args["executable"] = None
    module_args["_raw_params"] = "ls -A"
    module_args["_uses_delegate"] = False
    module_args["_ansible_check_mode"] = False

# Generated at 2022-06-13 10:56:23.133200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    from unittest import TestCase
    from mock import patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.python import qaz

    class TestActionModule(TestCase):
        ''' test class for TestActionModule '''

        class TestReferenceModule(object):
            ''' class for storing module references '''

            def __init__(self):
                self.action_loader = None
                self.legacy_command = None


# Generated at 2022-06-13 10:56:23.714531
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:32.790419
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")

    class MockModule(object):
        def __init__(self, action="", args=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            self.action = action
            self.args = args
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj

    class MockTask(object):
        def __init__(self, args=None):
            self.args = args

    class MockActionBase(object):
        def __init__(self, task_vars=None):
            self.task_vars

# Generated at 2022-06-13 10:56:40.814132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host_vars = dict(test_value_th=30, test_value_ru=20)
    task_vars = dict(hostvars=dict(host1=host_vars))

    parameters = dict(
        _raw_params="ansible_facts.test_results[inventory_hostname].test_value",
        _uses_shell=True)
    module_args = dict(
        _ansible_shell_executable="/usr/bin/ansible-test",
        _ansible_shell_type="sh")
    task_vars = dict(hostvars=dict(host1=host_vars))


# Generated at 2022-06-13 10:56:45.459488
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append('/tmp/ansible/test/units/plugins/actions')
    from ansible.plugins.action.shell import ActionModule
    obj = ActionModule()
    tmp = None
    task_vars = None
    result = obj.run(tmp, task_vars)
    assert result['_ansible_verbose_always'] is False
    assert result['changed'] == True

# Generated at 2022-06-13 10:56:50.002461
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for unit test for method run of class ActionModule
    class TestActionModule(ActionBase):
        def run(self, tmp=None, task_vars=None):
            print('hello')
            return 'passed'

    x = TestActionModule()
    assert x.run() == 'passed'

# Generated at 2022-06-13 10:57:00.486432
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    obj = ActionModule(DummyConnection, DummyTask)
    tmp = None
    task_vars = {'var': 'value'}
    result = obj.run(tmp, task_vars)

# Generated at 2022-06-13 10:57:13.459245
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # ModuleFinder only searches the directory it was initialized with
    import sys
    import os
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.shell import ActionModule

    sys.path.insert(0, os.path.abspath('https://github.com/ansible/ansible/test/test_plugins/action_plugins/test_ActionModule'))


# Generated at 2022-06-13 10:57:17.389514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(load_file_common_arguments, connection='aaa', templar='bbb', play_context='ccc', loader='ddd', task_vars='eee')
    result = a.run(tmp=None, task_vars='fff')
    assert result == '0' or result == 0

# Generated at 2022-06-13 10:57:41.196152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import shared_loader_obj
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext

    # Create a task
    task_args = dict(command='ls -l')
    task = Task().load({'action': 'shell', 'args': task_args})

    tqm = None

# Generated at 2022-06-13 10:57:43.769587
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module.run(tmp=None, task_vars=None) is None

# Generated at 2022-06-13 10:57:55.390690
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Testing a task with shell module with an example command
    dictionary = {'action': {'module': 'shell', 'args': 'echo hello world'}, 'name': 'shell'}
    task = TaskVars(dictionary, 'test_ActionModule_run')
    loader = DataLoader()
    templar = Templar(loader=loader)
    connection = Connection(mock=MockConnection())
    play_context = PlayContext()
    play_context.become = False
    action_module = ActionModule(task, connection, play_context, loader=loader, templar=templar, shared_loader_obj=None)
    task_vars = dict()
    result = action_module.run(task_vars=task_vars)

# Generated at 2022-06-13 10:57:56.470149
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

# Generated at 2022-06-13 10:58:02.043161
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from lib.action_module.shell import ActionModule

    tmp = None
    task_vars = {}

    action_module = ActionModule(tmp, task_vars)
    action_module.run(tmp, task_vars)

# Generated at 2022-06-13 10:58:11.995428
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    # 1. Fake tmp
    # 2. Fake connection
    # 3. Fake task
    # 4. Fake task_vars
    tmp = None
    connection = None
    task = None
    task_vars = None

    # Act
    # Create an instance and call method run of class ActionModule
    am = ActionModule(task, connection, _loader=None, _shared_loader_obj=None, _play_context=None, _task_vars=None, _templar=None)
    result = am.run(tmp=tmp, task_vars=task_vars)

    # Assert
    # ...

# Generated at 2022-06-13 10:58:21.054644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = MagicMock()
    mock_connection = MagicMock()
    mock_play_context = MagicMock()
    mock_loader = MagicMock()
    mock_templar = MagicMock()
    mock_shared_loader_obj = MagicMock()
    mock_task_vars = MagicMock()
    mock_command_action = MagicMock()
    mock_result = MagicMock()

    ansible_module_shell = ActionModule(mock_task, mock_connection, mock_play_context, mock_loader, mock_templar,
                                        mock_shared_loader_obj)

    # Arrange

    mock_task.args = {'_uses_shell': True}
    mock_shared_loader_obj.action_loader.get.return_value = mock_command_action
   

# Generated at 2022-06-13 10:58:22.941359
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Since this method is full of Ansible internals like self._loader, etc. there's not much point in testing it
    pass

# Generated at 2022-06-13 10:58:31.691257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import merge_hash
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import json

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source

# Generated at 2022-06-13 10:58:33.407268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert not ActionModule(None, None, None, None, None, None).run(None, None)

# Generated at 2022-06-13 10:59:15.196994
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockTask:
        def __init__(self):
            self.args = {'_uses_shell': False}
            self.rulename = 'Some-rule-name'

    class MockLoader:
        class MockFlags:
            action_loglevel = None
            action_log_path = None
            action_warnings = None
            action_deprecation_warnings = None

        def get_plugin_loader(self, module):
            pass

    class MockCallbacks:
        def v2_runner_on_failed(self, result, ignore_errors=False):
            pass

        def v2_runner_on_ok(self, result):
            pass

        def v2_runner_on_skipped(self, result):
            pass


# Generated at 2022-06-13 10:59:24.825743
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock
    import unittest.mock as mock

    # mock non-particular methods
    (mock_task_vars, mock_tmp, mock_task_args, mock_connection, mock_play_context, mock_loader, 
    mock_templar, mock_shared_loader_obj) = \
    (mock.MagicMock(), mock.MagicMock(), mock.MagicMock(), mock.MagicMock(), mock.MagicMock(), mock.MagicMock(), 
    mock.MagicMock(), mock.MagicMock())

    # mock particular methods and attributes
    mock_command_action = mock.MagicMock()
    mock_shared_loader_obj.action_loader.get.return_value = mock_command_action

    # instantiate

# Generated at 2022-06-13 10:59:39.371456
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C
    import os
    import sys
    import json

    class Model:

        def __init__(self, w_c):
            self.w_c = w_c


# Generated at 2022-06-13 10:59:39.964283
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:59:40.498650
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 10:59:48.554707
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Prepare mocks necessary for execution of the method and assertions
    from ansible.plugins.action import ActionBase
    ActionBase.run = lambda self, tmp=None, task_vars=None: {'rc': 2}
    action_module = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task = {'args': {'_uses_shell': False}}

    # Execution of the method and assertions
    assert action_module.run(tmp=None, task_vars={}) == {'rc': 2}

# Generated at 2022-06-13 10:59:59.098717
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def do_test(mock_task, mock_task_vars,
                expected_stdout, expected_stderr, expected_rc, expected_stdout_lines,
                expected_stderr_lines):
        def check_result(actual_result):
            # Check the contents of result returned by the run method of class ActionModule.
            assert 'ansible_facts' not in actual_result
            result_failed = actual_result['failed']
            result_changed = actual_result['changed']
            result_rc = actual_result['rc']
            result_stdout = actual_result['stdout']
            result_stdout_lines = actual_result['stdout_lines']
            result_stderr = actual_result['stderr']
            result_stderr_lines = actual_result['stderr_lines']

# Generated at 2022-06-13 11:00:11.040132
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Declare mock objects to be used to construct ActionModule
    task = Mock()
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()

    # Declare mock objects to be used to make assertions/expectations after
    # creation of action module
    command_action = Mock()
    command_action.run = Mock()

    ActionModule.run(task, connection, play_context, loader, templar, shared_loader_obj)

    # Assertions/Expectations
    task.args.__setitem__.assert_called_with('_uses_shell', True)

# Generated at 2022-06-13 11:00:13.118268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_module = ActionModule()
    output = fake_module.run()
    print(output)

# Generated at 2022-06-13 11:00:19.517502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mocks
    mock_task = Mock()
    mock_connection = Mock()
    mock_play_context = Mock()
    mock_loader = Mock()
    mock_templar = Mock()
    mock_shared_loader_obj = Mock()
    mock_action_loader = Mock()
    mock_command_action = Mock()

    # run action
    action_module = ActionModule(task=mock_task,
                                 connection=mock_connection,
                                 play_context=mock_play_context,
                                 loader=mock_loader,
                                 templar=mock_templar,
                                 shared_loader_obj=mock_shared_loader_obj)
    action_module._shared_loader_obj.action_loader = mock_action_loader
    action_module._shared_loader_obj

# Generated at 2022-06-13 11:01:53.485423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class MockTask(object):
        def __init__(self, args={}):
            self.args = args
            self.name = 'mock_action'
            self.async_val = 0
            self.async_seconds = 0


# Generated at 2022-06-13 11:02:03.408024
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_action_base = MockActionBase()
    m_task_vars = dict()
    m_command_action = MockCommandAction()
    m_command_action.return_value = dict()
    m_loader = MockLoader()
    m_loader.action_loader.get.return_value = m_command_action

    action_module = ActionModule(m_action_base, m_loader)
    result = action_module.run(task_vars=m_task_vars)

    # check if correct action is called
    m_command_action.assert_called_once()
    # check if task arg of command action is correct
    assert m_command_action.call_args[1]['_uses_shell']

    # check if return value is correct
    assert result == dict()


# Mock classes for unit tests

# Generated at 2022-06-13 11:02:05.811320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = action_module.run()
    print(result)

# Generated at 2022-06-13 11:02:09.458353
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    (connection, module_name, module_args, task_vars, tmp, task_path) = (None, None, None, None, None, None)
    ad = ActionModule(connection=connection, module_name=module_name, module_args=module_args, task_vars=task_vars, tmp=tmp, task_path=task_path)
    result = ad.run(tmp=None, task_vars=None)
    assert(result == None)

# Generated at 2022-06-13 11:02:10.290398
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "No test written"

# Generated at 2022-06-13 11:02:16.870543
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.plugins.action.shell as shell

    # Create a mock class in order to be able to call protected method
    class Shell(shell.ActionModule):

        def _create_tmp_path(self, cmd):
            del cmd
            return '/home/tmp/'

        def _make_tmp_path(self, cmd):
            del cmd
            return '/home/tmp/'

        def _write_tmp_file(self, cmd):
            del cmd
            return '/home/tmp/'

        def _get_working_path(self, cmd):
            del cmd
            return '/home/'

        def _remove_tmp_path(self, cmd):
            del cmd
            return '/home/'

        def _connection_info(self):
            return {'name': 'local'}


# Generated at 2022-06-13 11:02:19.127985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
#     host = FakeModule()
#     host.params = {'_ansible_loop_var': 'A'}
#     host.add_complex_task()
#     assert host.complex_task() == 'A'

# Generated at 2022-06-13 11:02:25.662989
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    tmp = '/tmp'
    task_vars = {}
    task_vars['module_name'] = 'shell'
    task_vars['module_args'] = {'echo':'something'}

    ansible_module_shell = ActionModule()
    ansible_module_shell._task = {'args':{'_uses_shell': True}}
    ansible_module_shell._connection = 'ssh'
    ansible_module_shell._play_context = 'play_context'
    ansible_module_shell._loader = 'loader'
    ansible_module_shell._templar = 'templar'
    ansible_module_shell._shared_loader_obj = 'shared_loader_obj'

    # Calling run method for ActionModule

# Generated at 2022-06-13 11:02:30.412955
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(loader=None, play_context=None, new_stdin=None)

    command_action = action.loader.action_loader.get('ansible.legacy.command',
                                                     task=action.task,
                                                     connection=action.connection,
                                                     play_context=action.play_context,
                                                     loader=action.loader,
                                                     templar=action.templar,
                                                     shared_loader_obj=action._shared_loader_obj)
    command_action.run = MagicMock()
    action.run(task_vars={})
    command_action.run.assert_called_once()

# Generated at 2022-06-13 11:02:37.182980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  class task:
    args = {}
  class ansible_module:
    task=task
  class connection:
    pass
  class loader:
    pass
  class shared_loader_obj:
    action_loader=ansible_module
  class play_context:
    remote_addr = "remote_addr"
    port = 1040
    remote_user = "remote_user"
    password = "password"

  action_module = ActionModule()
  action_module.run(task_vars={})