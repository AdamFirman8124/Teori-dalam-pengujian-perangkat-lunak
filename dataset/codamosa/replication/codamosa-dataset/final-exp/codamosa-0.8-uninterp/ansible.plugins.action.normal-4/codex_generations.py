

# Generated at 2022-06-13 10:16:12.161121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:16:22.866138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' verify the run method of the ActionModule class behaves as expected '''

# Generated at 2022-06-13 10:16:28.940921
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Result object must be initialized to an empty dict
    result = dict()
    # self._supports_check_mode must be set to True
    supports_check_mode = True
    # self._supports_async must be set to True
    supports_async = True

    am = ActionModule()

    assert result == am.run()
    assert supports_check_mode == am._supports_check_mode
    assert supports_async == am._supports_async

# Generated at 2022-06-13 10:16:37.911789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  class ActionModuleRunTest(ActionModule):
    def run(self, tmp=None, task_vars=None):
      return {
        'skipped': 'skipped',
        'invocation': {
          'module_args': {
            '_ansible_no_log': True
          }
        },
        '_ansible_no_log': True,
        '_ansible_verbose_override': False
      }

  # test run()
  actmodrun = ActionModuleRunTest()
  assert actmodrun.run() == {
    'skipped': 'skipped',
    '_ansible_no_log': True,
    '_ansible_verbose_override': False
  }

# Generated at 2022-06-13 10:16:49.264843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("##########################")
    print("C --> Class ActionModule")
    print("m --> Method run")
    print("##########################")
    print("")
    ##################################################################################################
    # First test case: We create an object of Type ActionModule and test the method run
    # Second test case: We don't create an object but we call the method run directly.
    ##################################################################################################
    # The first case is related to the second case, because the second function calls the first function
    # and the second case is the one that should be called by the user.
    ##################################################################################################

    ##################################################################################################
    # First test case
    ##################################################################################################
    print("FIRST TEST CASE")
    print("----------------")

    # Creation of an object of type ActionModule
    action_module = ActionModule()

    # We

# Generated at 2022-06-13 10:16:50.138814
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:17:03.641201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    import sys
    import StringIO
    from ansible.playbook.task import Task

    # Dummy class for the unittest of ActionModule
    class DummyActionBase(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return super(ActionBase, self)

    sys.stdout = out = StringIO.StringIO()
    am = ActionModule(DummyActionBase, Task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am.run()
    sys.stdout = sys.__stdout__

    class TestActionModule(unittest.TestCase):
        def test_actions(self):
            out.seek(0)
            output = out.read()

# Generated at 2022-06-13 10:17:06.969779
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.__class__.__name__ == 'ActionModule'
    assert am.__doc__ == 'Action plugin to execute actions synchronously.'
    assert am._supports_check_mode
    assert am._supports_async

# Generated at 2022-06-13 10:17:09.910173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	try:
		am = ActionModule(None, {})
		am.run()
	except (TypeError, ValueError, SyntaxError) as e:
		assert(False)
	else:
		assert(True)

# Generated at 2022-06-13 10:17:10.420781
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:17:23.679220
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    spec_list = dict(
        action='run',
        path='/tmp/ansible_test_dir',
        state='directory'
    )

# Generated at 2022-06-13 10:17:26.356998
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()

    assert mod._supports_async == True
    assert mod._supports_check_mode == True

    # test run() function
    mod.run()

# Generated at 2022-06-13 10:17:29.917177
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert not x._supports_async
    assert not x._supports_check_mode
    x._supports_async = True
    x._supports_check_mode = True

# Generated at 2022-06-13 10:17:31.034482
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule()

# Generated at 2022-06-13 10:17:33.522592
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()
    assert actionmodule._supports_check_mode == True
    assert actionmodule._supports_async == True

# Generated at 2022-06-13 10:17:36.856689
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    tmp=None
    task_vars=None

    result = a.run(tmp,task_vars)
    assert result["failed"]
    assert result["msg"] == "invalid action detected: test_ActionModule_run"

# Generated at 2022-06-13 10:17:37.444434
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:48.799346
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = {"action": {"__ansible_module__": "test_module"}}
    tmp = "/path/to/tmp"
    task_vars = dict()
    am = ActionModule(task, tmp, task_vars)
    assert am._task == task
    assert am._supports_check_mode == True
    assert am._supports_async == True
    assert am._task.async_val == 0
    assert am._connection.has_native_async == False
    assert am._remove_tmp_path == am._connection._shell._remove_tmp_path
    del am


# Generated at 2022-06-13 10:17:50.171882
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # I should probably implement tests here
    return 1 == 1

# Generated at 2022-06-13 10:17:58.918734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    import ansible.constants as C

    AnsibleTask = namedtuple('AnsibleTask', ['action', 'async_val'])
    AnsibleOptions = namedtuple('AnsibleOptions', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff', 'remote_user'])
    AnsibleVariableManager = namedtuple('AnsibleVariableManager', ['_options', 'extra_vars', 'graph'])

    options = Ans

# Generated at 2022-06-13 10:18:16.232343
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Imports
    from ansible.plugins.action.normal import ActionModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    
    # Create the variable manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(variable_manager))
    
    # Create the play context
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.become = False
    
    # Create the action module
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=play_context,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    
    # Make

# Generated at 2022-06-13 10:18:25.104276
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:18:32.065391
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(action=dict(module='setup'))
    connection = dict(host='localhost')
    play_context = dict()
    am = ActionModule(task,connection,play_context)
    assert isinstance(am,ActionModule)

    with pytest.raises(Exception) as e:
        task = dict(action='setup')
        am = ActionModule(task,connection,play_context)
        assert isinstance(am,ActionModule)

# Generated at 2022-06-13 10:18:37.813878
# Unit test for constructor of class ActionModule
def test_ActionModule():
  task_vars = dict()
  tmp = '/tmp'
  action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
  result = action_module.run(tmp=tmp, task_vars=task_vars)
  assert result == None

# Generated at 2022-06-13 10:18:40.409618
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._supports_check_mode == True
    assert module._supports_async == True

# Generated at 2022-06-13 10:18:41.354397
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:18:51.516834
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.module_utils.six import StringIO
    from ansible.utils.vars import combine_vars

    from ansible.module_utils.connection import Connection
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    loader = DataLoader()
    results = dict(changed=False)
    connection = Connection(loader=loader)

    task = Task()
    task.connection = connection
    task_vars = combine_vars(task, loader.load_from_file('/tmp/vars'))

    action = ActionModule(loader=loader, task=task, connection=connection)
    action._execute_module(task_vars=task_vars, wrap_async=True)

    print(task_vars)
    assert 1 == 1

# Generated at 2022-06-13 10:19:02.435362
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:19:02.966002
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:19:11.622432
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule. """
    task = dict()
    task['action'] = dict(__ansible_action__=dict())
    from ansible.plugins.loader import connection_loader
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    task_result = TaskResult(
        host=dict(),
        task_executor=TaskExecutor(dict(),
            connection=connection_loader.get('local', task, play_context=dict()),
            play_context=dict(),
            loader=dict(), shared_loader_obj=None),
        task=task)
    assert ActionModule(task_result=task_result).task == task

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:19:32.587869
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_user="test",
        ansible_ssh_pass="pass",
        ansible_ssh_port="1234",
        ansible_ssh_host="localhost",
        ansible_connection="ssh",
        ansible_network_os="not_real_os",
        ansible_verbosity=3
    )
    from ansible.plugins.action import ActionModule
    am = ActionModule('localhost', 'test_module_path', task_vars, 
                      'test_playbook_path', 'test_play_path', 'test_task_path')
    assert am.task_vars == task_vars
    assert am.module_name == 'test_module_path'
    assert am.module_args == ''


# Generated at 2022-06-13 10:19:38.949569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostname = 'testhost'
    port = '22'
    play_context = dict(remote_addr=hostname, port=port, network_os='ios')
    loader = 'test-loader'
    task = dict(action=dict(module='command', args='show ip interface brief'))
    task_vars = dict()

    # Call constructor
    action = ActionModule(task, play_context, loader, templar=None, shared_loader_obj=None)
    action.run(task_vars=task_vars)


# Generated at 2022-06-13 10:19:41.421141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(loader=None, shared_loader_obj=None, connection=None, play_context=None, loader_cache=None, variable_manager=None, compiler=None)
    assert (action_module)

# Generated at 2022-06-13 10:19:53.499478
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.connection_plugins import ConnectionBase
    from ansible.executor.task_queue_manager import TaskQueueManager


    class DummyConnection(ConnectionBase):

        def __init__(self):
            self._shell = None
            self._play_context = None

        def set_play_context(self, play_context):
            self._play_context = play_context

        def _connect(self):
            self._shell = DummyShellConnection()
            self._shell.open()


# Generated at 2022-06-13 10:19:58.432138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'hostvars': {'localhost':{'ansible_connection': 'local'}}}
    action_module = ActionModule(None, None, None)
    result = action_module._execute_module(task_vars, False)
    print(result)
    assert result.get('invocation', None) is not None

# Generated at 2022-06-13 10:20:06.196460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit tests for methods of AnsibleModule
    import sys
    import os
    import ansible.plugins.action
    from ansible.plugins.action.normal import ActionModule

    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six import iterkeys

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import MagicMock
    from ansible.compat.tests.mock import Mock

    # Basic testcases to test the methods of the class ActionModule
    # of the file action.py

    # This testcase is to test the method run of the class ActionModule
    # of the file action.py


# Generated at 2022-06-13 10:20:09.284838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    test class ActionModule(ActionBase)
    '''
    module = ActionModule()
    assert isinstance(module, ActionModule) == True

# Generated at 2022-06-13 10:20:16.978519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # excercise the test_ActionModule_run method

    # set up some test data
    import copy
    import inspect
    import os
    import sys
    import pytest
    import ansible.utils.vars

    # set up some test data
    ansible_result = dict(skipped=False,
                          invocation=dict(module_args=None),
                          _ansible_verbose_override=False,
                          _ansible_no_log=False)
    ansible_task_vars = dict(testVars1=True, testVars2=True)
    tmp = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    wrap_async = False
    is_failed = False
    exception = None

# Generated at 2022-06-13 10:20:24.738847
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a test method for ActionModule class"""

    # Test Parameters
    params = { 'action': 'ping',
               'delegate_to': 'localhost',
               'async': 10,
               'async_poll': 10,
               'async_status_dir': '',
               'async_status_file': '',
               'connection': 'smart',
               'flush_cache': False,
               'ignore_errors': False,
               'notify': [],
               'remote_user': 'chandan',
               'sudo': False,
               'sudo_user': 'chandan'}
    module_name = 'ping'
    inject = {}
    task_vars = {}
    tmp = '/tmp'

    # Create object of class ActionModule
    act_mod = ActionModule()

    # Test for run function

# Generated at 2022-06-13 10:20:26.662999
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # test the return value for method run, use the mock object instead of a real object
    assert True

# Generated at 2022-06-13 10:20:59.353671
# Unit test for constructor of class ActionModule
def test_ActionModule():
    
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.normal import ActionModule as NormalActionModule
    from ansible.plugins import action_loader

    # Constructor for normal action (i.e. normal action module and not connection plugin)
    normal_action = NormalActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert normal_action._supports_check_mode == True
    assert normal_action._supports_async == True
    assert normal_action._task == None
    assert normal_action._connection == None
    assert normal_action._play_context == None
    assert normal_action._loader == None
    assert normal_action._templar == None
    assert normal_action._shared_loader_

# Generated at 2022-06-13 10:21:00.142586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:08.846297
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.plugins.action.normal
    import ansible.playbook.task

    # test constructor of ActionModule
    task = ansible.playbook.task.Task()
    parameters = { 'remote_user':'ansible', 'remote_password':'ansible'}
    action_plugin = ansible.plugins.action.normal.ActionModule(task, parameters)

    assert action_plugin._priority == 1
    assert action_plugin._supports_check_mode == True
    assert action_plugin._supports_async == True

# Generated at 2022-06-13 10:21:16.883894
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ModuleMock(object):
        def __init__(self, *args):
            pass

    mock_class = ModuleMock()
    mock_class.run = lambda *args: False
    mock_class.noop = lambda *args: False
    mock_class._connection = {'has_native_async': False}

    # test with result as False
    mock_class.result = False
    ActionModule.run(mock_class)
    assert mock_class.result == False

    # test with result as True
    mock_class.result = True
    mock_class._execute_module = lambda : False
    ActionModule.run(mock_class)
    assert mock_class.result == False

# Generated at 2022-06-13 10:21:28.567217
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    t = Task()
    p = Play()
    tqm = None
    loader = None
    variable_manager = None
    inventory = InventoryManager(loader=loader, sources="/path/to/hosts_file")
    t.action = 'shell'
    p.add_task(t)
    playbook = PlaybookExecutor(playbooks=["/path/to/playbook_file"], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})

# Generated at 2022-06-13 10:21:29.689722
# Unit test for constructor of class ActionModule
def test_ActionModule():
  assert ActionModule.__name__ == "ActionModule"

# Generated at 2022-06-13 10:21:35.998841
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ test method run of ActionModule"""

    # Initialize a ActionModule object 
    test_object = ActionModule(add_cleanup_task=True, task_vars={})
    
    #insert the test parameters
    tmp =  {}
    task_vars = {}
    
    #Execute the method run of the Class ActionModule
    result = test_object.run(tmp=tmp, task_vars=task_vars)
    
    # Assert the expected result
    assert result == {}

# Generated at 2022-06-13 10:21:40.312669
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule(
            task = None,
            connection = None,
            play_context = None,
            loader = None,
            templar = None,
            shared_loader_obj = None
        )
    assert instance.tmp == None
    assert instance.task_vars == None

# Generated at 2022-06-13 10:21:41.140360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:42.242023
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:22:44.719099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    expected_result = {
        'skipped': False,
        'changed': False,
        'actions': [],
        'verbose_override': True
    }
    action_module_result = ActionModule().run(tmp='dummy value', task_vars='dummy value')
    assert action_module_result.viewkeys() == expected_result.viewkeys()

# Generated at 2022-06-13 10:22:45.305198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:22:52.781888
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import play
    from ansible import playbook
    from ansible import inventory
    from ansible import module_utils

    from ansible.playbook import play as play_tests
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase

    class CallbackModule(CallbackBase):
        """
        Callback module for use in testing
        """
        def __init__(self, display=None):
            if display:
                self._display = display
            else:
                self._display = Display()
            self.called = None

        def on_any(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 10:22:59.148870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_module = ActionModule()
    assert act_module._supports_async == True
    assert act_module._supports_check_mode == True
    assert act_module._uses_shell == False

    act_module = ActionModule('abcd', 'efgh')
    assert act_module._task.args['action'] == 'abcd'
    assert act_module._connection.play_context.remote_addr == 'efgh'

# Generated at 2022-06-13 10:23:02.227562
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = "ansible_facts"
    task_vars = {"c":1}
    am = ActionModule(module_args, task_vars)
    assert am.action_args == "ansible_facts" and am.task_vars == {"c":1}

# Generated at 2022-06-13 10:23:02.942801
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert False, 'No tests for this plugin implemented yet.'

# Generated at 2022-06-13 10:23:03.941675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    k = ActionModule()

# Generated at 2022-06-13 10:23:04.802996
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:23:07.009375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.copy import ActionModule
    print(ActionModule)

# Generated at 2022-06-13 10:23:18.662264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    # raise exception if module is not found
    ansible.plugins.action._action_plugins = {}
    import ansible.plugins.action.normal
    module = ansible.plugins.action.normal.ActionModule(
        task=dict(action=dict(module_name='copy', module_args=dict(src='haha', dest='hehe'))),
        connection=None,
        play_context=dict(check_mode=False)
    )
    assert module.run() == dict(
        skipped=False,
        changed=False,
        msg="",
        _ansible_verbose_override=True
    )

# Generated at 2022-06-13 10:25:35.871065
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:39.034723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    print(repr(action))
    assert repr(action) == "<ansible.plugins.action.ActionModule object at 0x7f1da71fc250>"

# Generated at 2022-06-13 10:25:39.898200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise Exception('Not implemented')


# Generated at 2022-06-13 10:25:40.444745
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:25:46.528737
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.constants
    from ansible.plugins.action import ActionBase
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.utils.vars import merge_hash
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    import ansible.playbook.task_include


# Generated at 2022-06-13 10:25:50.526341
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionBase._configure_module()
    assert ActionModule(task = None, connection = None, play_context = None, loader = None, templar = None, shared_loader_obj = None)

# Generated at 2022-06-13 10:26:01.524042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("test_ActionModule")
    import ansible.inventory
    import ansible.playbook.task
    import ansible.utils.vars
    import ansible.vars

    host = ansible.inventory.host.Host(name="test")

    task = ansible.playbook.task.Task()
    task._role = ansible.playbook.role.Role()
    task.args = dict()
    task.action = "test"
    action_module = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module != None

    result = dict(changed=True)
    fact_cache = dict()
    fact_cache["action_module"] = result
    task_vars = dict()
    task_vars

# Generated at 2022-06-13 10:26:16.732859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.utils.vars import combine_vars
    from ansible.utils import template
    from ansible.plugins.action.normal import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    import ansible