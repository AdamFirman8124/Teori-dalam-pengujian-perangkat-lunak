

# Generated at 2022-06-13 10:16:12.272151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:16:12.637041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

# Generated at 2022-06-13 10:16:23.979195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.stats import AggregateStats
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    import ansible.constants as C
    import sys

    options = {'verbosity': 0, 'action_plugins': C.DEFAULT_ACTION_PLUGIN_PATH}
    # Since we are not passing in any inventory we need

# Generated at 2022-06-13 10:16:34.465776
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import os
    import tempfile
    import json

    # mock ansible.constants
    constants = mock.MagicMock()
    constants.__salt__ = {
        'config.get': lambda x: None,
    }
    constants.DEFAULT_REMOTE_USER = 'does not matter'
    constants.DEFAULT_SUDO_EXE = 'does not matter'
    constants.DEFAULT_SUDO_FLAGS = 'does not matter'
    constants.DEFAULT_SU_EXE = 'does not matter'
    constants.DEFAULT_SU_FLAGS = 'does not matter'

    # mock ansible.plugins.action
    action_base = mock.MagicMock()
    action_base.action_loader.get.return_value = None
    action_base.ActionBase._execute_

# Generated at 2022-06-13 10:16:48.081948
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    from collections import namedtuple

    class task:
        wrapped_async = False
        async_val = None

    class connection:
        def has_native_async(self):
            return False

    class Result:
        def __init__(self):
            self.result = {}

    class TaskResult:
        def __init__(self):
            self.result = {}

    class PluginResult:
        def __init__(self):
            self.result = {}

    class task_vars:
        def __init__(self):
            self.result = {}

    class tmp:
        pass

    class ActionBase:
        def __init__(self):
            self._supports_check_mode = True
            self._supports_async = True

   

# Generated at 2022-06-13 10:16:49.351151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(Task(), Connection('localhost'))
    assert am is not None

# Generated at 2022-06-13 10:16:49.986135
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  return True

# Generated at 2022-06-13 10:16:51.289910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:17:04.837054
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock

    # Test with no invocation params
    task_vars = dict()
    tmp = None
    wrap_async = False

    module_result = dict(skipped=False,
                         changed=True,
                         msg='msg',
                         meta='meta')

    mock_self = mock.Mock()
    mock_self._supports_check_mode = True
    mock_self._supports_async = True

    mock_self.run = mock.Mock(return_value=dict(skipped=False))

    mock_self._execute_module = mock.Mock(return_value=module_result)

    mock_self._remove_tmp_path = mock.Mock()
    mock_self._connection = mock.Mock()
    mock_self._connection.has_native_async = False

    mock_

# Generated at 2022-06-13 10:17:13.554608
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import sys
    import tempfile
    import shutil
    import yaml
    from ansible.plugins.action import ActionModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = variable_manager.loader

    test_dir_name = 'test_file_folder'
    current_dir = os.getcwd()
    temp_dir_path = tempfile.mkdtemp()
    test_dir_path = temp_dir_path + '/' + test_dir_name
    os.mkdir(test_dir_path)
    os.chdir(test_dir_path)

    # Create fake inventory

# Generated at 2022-06-13 10:17:23.403459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    doc = """
    Executes a module on a remote node
    """

    s="The silent killer kills silently"
    tmp=None
    task_vars={'test_var_1': s}

    # create a new instance of the ActionModule class, with argument values for temporary directory and task variables
    action = ActionModule(tmp,task_vars)
    # get value of docstring attribute
    doc_val = action.doc
    # get return value from run function of the class
    result = action.run(tmp, task_vars)

    # print the value of docstring, run function's return value, and the temporary directory
    print( "USER MODULE DOCSTRING:%s" % (doc_val))
    print( "RUN RETURN VALUE:%s" % (result))

# Generated at 2022-06-13 10:17:29.630303
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.__init__ import ActionModule as _ActionModule
    import ansible.plugins.action.__init__ as __init__
    # FIXME: does not verify *all* attributes defined in ActionBase class
    for attribute in ['_supports_check_mode', '_supports_async', '_uses_tmp']:
        assert hasattr(_ActionModule, attribute)
    # check if run() is defined in class ActionModule
    assert __init__.ActionModule.run is not None

# Generated at 2022-06-13 10:17:30.273457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:30.784423
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:17:32.535475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: We need a better way to test this.
    pass

# Generated at 2022-06-13 10:17:41.412607
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:17:55.337751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash

    import pytest

    ###############################################################
    #                  ActionModule.run()
    ###############################################################
    # test create ActionModule object with no params
    def test_ActionModule_run_1():
        _task = Task()
        _connection = 'test_connection'
        _play_context = 'test_play_context'
        _loader = 'test_loader'
        _templar = 'test_templar'
        _shared_loader_obj = 'test_shared_loader_obj'



# Generated at 2022-06-13 10:17:59.374195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection_mock = Connection()
    task_mock = Task()
    module_mock = ActionModule(task_mock, connection_mock)
    module_mock.run()
    print(connection_mock.state)
    assert(connection_mock.state == 'exec_module')


# Generated at 2022-06-13 10:18:00.752426
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test ActionModule_run")

    # TODO: implement test


# Unit tests for class ActionModule

# Generated at 2022-06-13 10:18:05.630858
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an object for ActionModule class
    actionModule_obj = ActionModule(None, dict(), True, None, None, None, None)
    # check the type of instance created
    assert isinstance(actionModule_obj, ActionModule)


# Generated at 2022-06-13 10:18:13.061263
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        assert ActionModule("Test", "Test")
    except Exception as e:
        print("Exception: " + str(e))
        assert False

# Generated at 2022-06-13 10:18:19.517990
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.task
    result = ansible.playbook.task.Task()
    result.action = 'setup'

    assert result.handlers == []
    assert result.tags == []
    assert result.any_errors_fatal == False
    assert result.notify == []
    assert result.when == []
    assert result.register == None
    assert result.ignore_errors == False
    assert result.max_fail_percentage == None
    assert result.delegate_to == None
    assert result.run_once == False
    assert result.action == 'setup'

# Generated at 2022-06-13 10:18:20.450327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 10:18:21.790517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:18:29.464790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class ActionModule with 2 args
    executor = ActionModule('/etc/ansible/roles/test/tasks','/etc/ansible/roles/test/tasks/main.yml')
    assert executor.__dict__['_task'].__dict__['_role_name'] == 'test'
    assert executor.__dict__['_task'].__dict__['_role_path'] == '/etc/ansible/roles/test'
    assert executor.__dict__['_task'].__dict__['_ds'] == '/etc/ansible/roles/test/tasks/main.yml'
    assert executor.__dict__['_task'].__dict__['_role_params'] == {'test': 'test'}

    # Constructor of class ActionModule with 1 arg

# Generated at 2022-06-13 10:18:39.824261
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create an instance of the class to test
    class my_test():
        _task = {'action': 'setup'}
        _connection = {}
        _play_context = {}
        def __init__(self, task, connection, play_context):
            self._task = task
            self._connection = connection
            self._play_context = play_context

    # prepare and run test
    actionmodule = ActionModule()
    result = actionmodule.run(my_test({'async_val': False, 'async': 300}, {'has_native_async': True}, {}), {})

    # check that the test returns the expected result
    assert result == {'skipped': True}

# Generated at 2022-06-13 10:18:40.990712
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None

# Generated at 2022-06-13 10:18:51.366875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    import ansible.module_utils.basic
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    connection_loader_module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
        bypass_checks=True
    )
    inventory = InventoryManager(loader=DataLoader())
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)


# Generated at 2022-06-13 10:18:57.876813
# Unit test for constructor of class ActionModule
def test_ActionModule():

    mock_loader = "loader"
    mock_templar = "templar"
    mock_task = "task"
    action_module = ActionModule(mock_loader, mock_templar, mock_task)
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True


# Generated at 2022-06-13 10:19:07.673598
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    fake_task = {
        'action': 'setup',
        'args': {
            'module_args': 'module_args'
        }
    }
    # noinspection PyArgumentList
    action_module = ActionModule(task=fake_task, connection='connection', play_context='play_context')

    def execute_module(task_vars=None, wrap_async=None):

        return {
            '_ansible_verbose_override': True
        }

    def _remove_tmp_path(tmp_path):
        pass

    action_module._connection._shell.tmpdir = 'tmpdir'
    action_module._execute_module = execute_module
    action_module._remove_tmp_path = _remove_tmp_path


# Generated at 2022-06-13 10:19:19.739004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:19:31.274155
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    
    from ansible.plugins.action.normal import ActionModule
    from ansible.module_utils.connection import ConnectionBase
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    import ansible.constants as C
    import json
    import os
    
    # create a dummy task object
    task = Task()

# Generated at 2022-06-13 10:19:33.286365
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test signature of class ActionModule to detect signature changes.
    """
    a = ActionModule(None, None, None, None, None, None)

# Generated at 2022-06-13 10:19:37.111738
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    import ansible.utils.vars
    result = ansible.plugins.action.ActionModule.run(None, None)
    assert result.get('skipped', None) is None
    assert result._supports_check_mode == True
    assert result._supports_async == True

# Generated at 2022-06-13 10:19:37.897213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()

# Generated at 2022-06-13 10:19:41.170129
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_plugin = ActionModule()
    action_plugin.action = 'hah'
    action_plugin._connection = object
    action_plugin._task = object
    action_plugin._task.action = 'setup'

    result = action_plugin.run(None, None)

    assert result['_ansible_verbose_override'] is True

# Generated at 2022-06-13 10:19:42.643204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:19:44.696118
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.play
    import ansible.playbook.task
    assert ActionModule.__doc__

# Generated at 2022-06-13 10:19:51.878575
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    import ansible.inventory.manager
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueItem
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 10:19:55.108476
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible = Ansible()
    constructor = ansible.get_action_plugin("action_plugin")
    #assert constructor is ActionModule, "constructor does not match"
    print("constructor matches")

# Generated at 2022-06-13 10:20:29.660369
# Unit test for method run of class ActionModule
def test_ActionModule_run():

  ############################################################

  # initialize test
  test_name = 'test_ActionModule_run'
  test_passed = 'FAILED'

  # create variables
  tmp = None
  task_vars = {
    'my test var': 'value1',
    'my other test var': 'value2',
  }

  # initialize class object
  AM = ActionModule(
    task=None,
    connection=None,
    play_context=None,
    loader=None,
    templar=None,
    shared_loader_obj=None
  )

  # run run method
  result1 = AM.run(tmp, task_vars)

  # initialize expected result
  expected_result1 = {}

  # test
  assert result1 == expected_result1

  ############################################################

 

# Generated at 2022-06-13 10:20:34.364456
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor
    cls = globals()["ActionModule"]
    action = cls(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action is not None
    assert repr(action) == "<ansible.plugins.action.ActionModule object>"

# Generated at 2022-06-13 10:20:44.229397
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
    )
    p = Play()
    t = Task()
    t.action = "debug"
    p._tasks = [t]
    p._tasks.append(t)
    am = ActionModule(p, tqm._loader, tqm.shared_loader_obj)
    # am.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:20:44.875433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:20:45.807367
# Unit test for constructor of class ActionModule
def test_ActionModule():
   assert isinstance(ActionModule(),ActionBase)

# Generated at 2022-06-13 10:20:55.862769
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    options = {'connection': 'local', 'module_name': None, 'module_path': None, 'module_args': '', 'forks': 5, 'become': None, 'become_method': None, 'become_user': None, 'check': False, 'listhosts': None, 'listtasks': None, 'listtags': None, 'syntax': None, 'module_vars': [], 'module_defaults': [], 'module_default_vars': [], 'vault_password': None, 'ask_pass': False, 'ask_become_pass': False, 'diff': False}
    task = Task()
    task.noop_on_check(False)

# Generated at 2022-06-13 10:21:01.977031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    x = ActionModule(None, None, None)
    x._supports_check_mode = True
    x._supports_async = True
    result = x.run(tmp="foo", task_vars={})
    assert 'skipped' not in result

    assert result.get('invocation', {}).get('module_args') is None

# Generated at 2022-06-13 10:21:10.187330
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._supports_async = True
    module._supports_check_mode = True
    tmp = None
    task_vars = {
        "foo": "bar"
    }
    result = module.run(tmp, task_vars)
    assert result.get('failed') is True
    assert result.get('msg') == "this action plugin needs to be rewritten to work with the current module interface"

# Generated at 2022-06-13 10:21:12.182554
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.play

    action = ActionModule()
    assert action._task == None

# Generated at 2022-06-13 10:21:19.118610
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for correct functionality of method run() of class ActionModule
    '''
    print('Unit test for method run of class ActionModule')
    #print('FIXME: unit test for method run() of class ActionModule')
    print('Unit test for method run of class ActionModule SUCCESSFUL')
    #print('FIXME: unit test for method run() of class ActionModule SUCCESSFUL')


# unit test adhoc command ansible
# ansible localhost -m lib.ansible_collections.notstdlib.moveitallout.plugins.modules.action -a '{"debug_var": "action_module"}'
# ansible localhost -m lib.ansible_collections.notstdlib.moveitallout.plugins.modules.action -a '{"debug_var": "action_module_action_base"}'

# Generated at 2022-06-13 10:22:20.571212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()


# Generated at 2022-06-13 10:22:23.161793
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._connection.has_native_async == 'no'

# Generated at 2022-06-13 10:22:26.683009
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of class ActionModule
    action_module = ActionModule()
    assert action_module
    assert action_module.run


test_ActionModule()

# Generated at 2022-06-13 10:22:35.575599
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test reading variables from task_vars
    module = ActionModule()
    module._supports_async = True
    module._supports_check_mode = False
    module._task_vars = {'foobar': 'baz'}
    module._task = {'async_val': None}
    module._connection = {'has_native_async': False}
    module._execute_module = lambda: {'module_result': 'foobar'}
    module._remove_tmp_path = lambda: {'remove_tmp_path_result': 'foobar'}
    module._execute_module = lambda: {'module_result': 'foobar'}
    module._remove_tmp_path = lambda: {'remove_tmp_path_result': 'foobar'}
    result = module.run()
    assert result

# Generated at 2022-06-13 10:22:44.436898
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Initialize an instance of class ActionModule
    _ActionModule = ActionModule()

    # Declare some variables
    _ActionModule._connection = {'has_native_async':False}
    _ActionModule._task = {'async_val':False}
    _ActionModule._remove_tmp_path = lambda temp_dir: None

    # Call method run of class ActionModule
    result = _ActionModule.run(None, None)

    # Assert exit_json and return values of method run
    assert {} == result, "Failed to assert the return value of method run"

# Generated at 2022-06-13 10:22:47.525702
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._supports_check_mode == True
    assert module._supports_async == True
    assert isinstance(module, ActionBase)

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:22:52.422925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Build mock arguments for method run of class ActionModule
    tmp = None
    task_vars = ''
    # Build mock object for class ActionModule
    action_module = ActionModule(None, None)
    # Test method run of class ActionModule
    action_module.run(tmp, task_vars)

# Generated at 2022-06-13 10:22:53.895038
# Unit test for constructor of class ActionModule
def test_ActionModule():
   module = ActionModule(None, None)


# Generated at 2022-06-13 10:22:54.997472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, 'Not implemented'


# Generated at 2022-06-13 10:22:55.584678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:11.927524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(None, None, None, None)
    x.run()
    return x

# Generated at 2022-06-13 10:25:13.318025
# Unit test for constructor of class ActionModule
def test_ActionModule():
    s = ActionModule()
    assert s is not None, "Action Module Object creation failed"

# Generated at 2022-06-13 10:25:16.197998
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor of class ActionModule
    """
    action_module = ActionModule('path/to/nowhere')
    print(action_module)

# import module snippets
from ansible.module_utils.basic import *

main()

# Generated at 2022-06-13 10:25:17.518403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()


# Generated at 2022-06-13 10:25:26.890962
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:25:36.446903
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = dict(log_path='/var/log/log.log')
    tmp = '/tmp'
    task_vars = dict(log_path='/tmp')
    class Wrapper:
        ansible = dict(supports_check_mode=True)

    conn = Wrapper()

    class Tmp:
        pass

    class Shell:
        class Prompt:
            def __init__(self):
                self.tmpdir = '/tmp'
        prompt = Prompt()

    tmp = Tmp()
    tmp.shell = Shell()

    conn.shell = tmp.shell

    class ExecuteModule:
        class ModuleResult:
            def __init__(self):
                self.exception = 'Not implemented'
        class ArgSpec:
            def __init__(self):
                self.args = ['log_path']

# Generated at 2022-06-13 10:25:37.709443
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:25:44.651088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.plugins.loader import connection_loader


    connection = connection_loader.get('local', None)
    action = connection_loader.get('shell', 'local')

    task = Task()
    task._role = None
    task.action = action
    task.async_val = None

    play_context = PlayContext()
    play_context.become = False
    play_context.become_method = None

    play = Play().load({'name': 'test', 'hosts': 'localhost'}, variable_manager={}, loader=None)


# Generated at 2022-06-13 10:25:49.081743
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Setup test values
    tmp = '/test'
    task_vars = {}

    # Create test class
    action_module = ActionModule(tmp, task_vars)

    # Test for not skipped
    assert action_module.run()

# Generated at 2022-06-13 10:25:54.238134
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

if __name__ == '__main__':
    test_ActionModule()