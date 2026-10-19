

# Generated at 2022-06-13 10:52:42.651287
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(tmp='foo', task_vars='bar')

# Generated at 2022-06-13 10:52:43.320542
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:44.061690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:52:51.842303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    result = {'invocation': {'module_args': 'echo hi'}, 'stdout': 'hi', 'stdout_lines': ['hi'], '_ansible_verbose_always': True, 'stderr': '', '_ansible_no_log': False, 'rc': 0, 'stdout_json': '["hi"]', 'changed': False, 'cmd': ['echo', 'hi'], 'stderr_lines': []}
    assert result == ActionModule().run()

# Generated at 2022-06-13 10:52:53.089078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:06.326153
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def mock__task_variable(key,var_default):
        if key == 'ansible_env':
            return {}
        return key + ':' + var_default

    mock_self = MagicMock()
    mock_self._task = MagicMock()
    mock_self._task.args = {'_uses_shell': True}
    mock_self._connection = '_connection'
    mock_self._play_context = '_play_context'
    mock_self._loader = '_loader'
    mock_self._templar = '_templar'
    mock_self._shared_loader_obj = MagicMock()
    mock_self._shared_loader_obj.action_loader = MagicMock()

    mock_command_action = MagicMock()

# Generated at 2022-06-13 10:53:07.732486
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  print ("In test_ActionModule_run")
  assert True

# Generated at 2022-06-13 10:53:15.231931
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    class ActionModuleMock(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj

    class TaskMock:
        def __init__(self, args):
            self.args = args
    
    class LoaderMock:
        def __init__(self, action_loader):
            self.action_loader = action_loader
    

# Generated at 2022-06-13 10:53:15.982991
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:53:27.252002
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mocker, action_module = mocker_action_module(action_class=ActionModule)
    mocker.patch('ansible.plugins.action.ActionBase._find_needle', return_value=dict())
    mocker.patch('ansible.plugins.action.ActionBase._compare_needle_in_haystack', return_value=None)
    action_module.run(task_vars=dict())
    assert action_module._shared_loader_obj.action_loader.get.call_count == 1
    assert action_module._shared_loader_obj.action_loader.get.call_args[0] == ('ansible.legacy.command',)
    assert action_module._task.args['_uses_shell'] == True

# Generated at 2022-06-13 10:53:31.482946
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    module_test = tempfile.mkdtemp()
    print(module_test)
    # FIXME: Implement test


# Generated at 2022-06-13 10:53:41.682586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.shell import ActionModule
    from ansible.plugins.loader import shared_loader_obj

    # class ActionModule(ActionBase):
    a = ActionModule(
        task=shared_loader_obj._task,
        connection=shared_loader_obj._connection,
        play_context=shared_loader_obj._play_context,
        loader=shared_loader_obj._loader,
        templar=shared_loader_obj._templar,
        shared_loader_obj=shared_loader_obj
    )

    # def run(self, tmp=None, task_vars=None):

# Generated at 2022-06-13 10:53:48.645065
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    b_options = {'a': 1, 'b': 2}
    b_task_vars = {'a': 3, 'c': 4}
    basi = ActionBase(None, None, None, None, b_options, None, None, None, None)
    am = ActionModule(basi, None, None, None, b_options, None, None, None, None)
    r = am.run(task_vars=b_task_vars)
    print(r)

# Generated at 2022-06-13 10:53:49.406563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = ActionModule()
    result.run()

# Generated at 2022-06-13 10:53:55.675836
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Here is how to implement a unit test.
    #
    ##
    ## Here is how to set up some task vars so you can
    ## test the implementation of ActionModule.run()
    ##
    
    # Setup test task vars and sources ...
    #
    ## Get this file's path
    import sys, os
    Path = os.path.dirname(os.path.abspath(__file__))
    
    # ... which modules will be run ...
    #
    ## Load the task_vars for this module
    from yaml import load
    task_vars = load(open(Path + '/../test/test_' + 'zetar_action_module' + '/task_vars.yml'))
    
    ##
    ## Here is how to set up some task vars so you

# Generated at 2022-06-13 10:54:06.822928
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.errors import AnsibleError
    from ansible import constants as C
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars
    import os

    # Mocking _execute_module and run_command of CommandAction
    class FakeCommandAction(object):
        def __init__(self, *args, **kwargs):
            self._task = args[1]
            self._connection = args[2]
            self._loader = args[4]

        def _execute_module(self, *args, **kwargs):
            ''' _execute_module is used to mock _execute_module of CommandAction '''
            self.executed_module = args, kwargs
            return "shell_result", "shell_command"


# Generated at 2022-06-13 10:54:10.415552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod._task.args['_raw_params'] = 'echo "abcd"'
    res = mod.run()
    assert res['stdout'] == "abcd\n"
    assert res['rc'] == 0


# Generated at 2022-06-13 10:54:18.774621
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup test objects
    task = AnsibleActionModuleTest.create_task_object()
    connection = AnsibleActionModuleTest.create_connection_object()
    play_context = AnsibleActionModuleTest.create_play_context_object()
    loader = AnsibleActionModuleTest.create_loader_object()
    templar = AnsibleActionModuleTest.create_templar_object()
    shared_loader_obj = AnsibleActionModuleTest.create_shared_loader_object()
    
    # Create the object that we are testing
    test_object = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    #TODO: Fill in the test
    """
    assert False
    """

# Generated at 2022-06-13 10:54:26.113812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(loader=None,
                                 connection=None,
                                 play_context=None,
                                 templar=None,
                                 task=None,
                                 shared_loader_obj=None)

    action_module.run()
    # verify that attribute _task.args has key '_uses_shell'
    assert '_uses_shell' in action_module._task.args

# Generated at 2022-06-13 10:54:26.614529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:54:39.655477
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection

    module_mock = AnsibleModule(argument_spec={})
    connection_mock = Connection(None)

    am = ActionModule(module_mock, None, connection_mock, None, None, None, None)
    am._task.args = {'_uses_shell': True}
    module_mock.fail_json = lambda msg: msg

    result = am.run(tmp=None, task_vars=None)

    assert result['ansible_facts']['command_invocation'] == {'module_args': {'_uses_shell': True}}

# Generated at 2022-06-13 10:54:49.145670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.module_utils.six import string_types
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor import task_executor
    from ansible.playbook.play import Play
    from ansible.playbook import ds
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    module_name = "shell"

    action_plugin = action_loader.get(module_name, task=None)
    assert isinstance(action_plugin, ActionModule)


# Generated at 2022-06-13 10:54:53.164502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_args = dict(
        chdir="/tmp",
        executable="/bin/bash"
    )
    action_module = ActionModule()
    result = action_module.run(task_vars=None, task_args=task_args)
    print(result)

# Generated at 2022-06-13 10:55:02.446728
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Init a ActionModule instance
    actmod = ActionModule()

    # Init a task
    actmod._task = {}

    # Init task args
    actmod._task["args"] = {"cmd": "ls"}

    # Init ansible_check_mode
    actmod._task["ansible_check_mode"] = True

    # Init _loader
    actmod._loader = None

    # Init _templar
    actmod._templar = None

    # Init _connection
    actmod._connection = None

    # Init _play_context
    actmod._play_context = None

    # Init _shared_loader_obj
    actmod._shared_loader_obj = None

    # Init task_vars
    task_vars = {}

    # Call run method of ActionModule

# Generated at 2022-06-13 10:55:13.632515
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = "test_host"
    task_vars = {"test_var": "test_var_value"}
    task = {"test_task": "test_task_value"}
    self = ActionModule(task, host, file_utils, connection, play_context, loader, templar, shared_loader_obj)
    self._templar.template.return_value = "test_command_value"

    result = self.run(task_vars)

    self._shared_loader_obj.action_loader.get.assert_called_once_with('ansible.legacy.command')
    command_action = self._shared_loader_obj.action_loader.get.return_value
    command_action.run.assert_called_once_with(task_vars=task_vars)

# Generated at 2022-06-13 10:55:21.395962
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(tmp=None, task_vars={"some_var": "some_value"})
    actionModule._task = "ansible.legacy.shell"
    actionModule._connection = "connection_obj"
    actionModule._play_context = "play_context"
    actionModule._loader = "loader"
    actionModule._templar = "templar"
    actionModule._shared_loader_obj = "shared_loader_obj"

    assert actionModule.run(tmp=None, task_vars={"some_var": "some_value"}) == {"some_var": "some_value"}

# Generated at 2022-06-13 10:55:27.438758
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize data for test

    # Create instance of class ActionModule with dummy data
    test_instance = ActionModule(index=0, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Init data for run
    tmp = None
    task_vars = None

    # Call method run of class ActionModule and test result
    assert test_instance.run(tmp=tmp, task_vars=task_vars) != None

# Generated at 2022-06-13 10:55:27.885219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 0 == 0

# Generated at 2022-06-13 10:55:34.409885
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # To create a mock class first
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class AnsibleModule(object):
        def __init__(self, argument_spec, supports_check_mode=False, bypass_checks=False, no_log=False, check_invalid_arguments=True, add_file_common_args=False, mutually_exclusive=None, required_together=None,
                           required_one_of=None, required_by=None):
            self.params = None
            self.check_mode = check_mode
            self.argument_spec = argument_spec

# Generated at 2022-06-13 10:55:39.026147
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = dict(arg1='arg 1',arg2='arg 2')
    action = ActionModule(task=dict(args=args))
    action.run()
    assert action._task.args['_uses_shell'] == True

# Generated at 2022-06-13 10:55:52.205654
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # access protected variables
    # ActionModule._task = None
    # ActionModule._connection = None
    # ActionModule._play_context = None
    # ActionModule._loader = None
    # ActionModule._templar = None
    # ActionModule._shared_loader_obj = None
    # ActionModule.run = None

    # setup

    # action module
    from ansible.plugins.action.shell import ActionModule

    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Invoke method
    result = action_module.run(tmp=None, task_vars=None)

    # Verify the result
    assert(result == None)

# Generated at 2022-06-13 10:55:57.951483
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing the module class
    action_module = ActionModule()
    # Initializing the local vars
    tmp = ''
    task_vars = {}
    # Call the run method
    result = action_module.run(tmp, task_vars)
    assert result is not None

# Generated at 2022-06-13 10:55:59.000739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 10:56:10.392846
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.shell import ActionModule as Shell
    from ansible.plugins.action import ActionBase as Action
    from ansible.executor.task_queue_manager import TaskQueueManager as Task
    import ansible.playbook.play_context as Play
    import ansible.playbook.play as Playbook
    import ansible.plugins.loader as Plugins
    import ansible.vars.manager as Vars

    # instantiate the class

    class MockTask(object):
        args = {'_uses_shell':True}
        def __init__(self):
            self.args
        def get_args(self):
            return self.args

    class MockPlay(object):
        pass

    class MockTaskQueueManager(object):
        pass

    class MockVars(object):
        pass


# Generated at 2022-06-13 10:56:19.787241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #def run(self, tmp=None, task_vars=None):
    print("Method: Run")
    # tmp no longer has any effect
    # Shell module is implemented via command with a special arg
    self._task.args['_uses_shell'] = True
    command_action = self._shared_loader_obj.action_loader.get('ansible.legacy.command',
                                                                   task=self._task,
                                                                   connection=self._connection,
                                                                   play_context=self._play_context,
                                                                   loader=self._loader,
                                                                   templar=self._templar,
                                                                   shared_loader_obj=self._shared_loader_obj)
    result = command_action.run(task_vars=task_vars)
    return result

# Generated at 2022-06-13 10:56:27.687061
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''test_ActionModule_run
    Test run method of class ActionModule.
    '''
    action_module = ActionModule()
    action_module._task.args = {'_uses_shell': True}
    action_module._task.args['command'] = 'echo hello'
    action_module._task.args['warn'] = True

    assert action_module.run() == {'changed': True, 'warnings': ['Consider using the ansible.builtin.shell module instead. This feature will be removed in a future release. '], 'rc': 0, 'stdout': 'hello', 'stdout_lines': ['hello']}

# Generated at 2022-06-13 10:56:28.514788
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False


# Generated at 2022-06-13 10:56:31.274859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create object
    action_module = ActionModule(None, None, None)

    # Invoke method run
    result = action_module.run(None, None)

    print(result)

# Generated at 2022-06-13 10:56:40.112699
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ...mock.loader import DictDataLoader
    from ...mock.connection import Connection
    from .mock.task import Task
    from .mock.settings import Settings

    # Create a data loader for test module
    data_loader = DictDataLoader({
        "my_shell_module.yml": '''
- name: Test shell module Ansible
  hosts: localhost
  tasks:
    - name: Create a new file
      shell: touch file_one.txt

      args:
        executable: /bin/bash
        chdir: /tmp
'''})

    # Create a connection to localhost
    localhost_connection = Connection('localhost')

    # Create a play context
    play_context = PlayContext()

    # Create a new task
    task = Task()

    # Create a new settings
    setting = Settings

# Generated at 2022-06-13 10:56:48.160342
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    #  =================== ACTION
    class ActionBase_mock:
        #  =================== BUILD
        def __init__(self):
            self.args = {'_uses_shell': True}

    #  =================== CONNECTION
    class Connection_mock:
        pass

    #  =================== LOADER
    class Loader_mock:
        def get_basedir(self):
            return 'ansible_directory'

    #  =================== PLAY_CONTEXT
    class PlayContext_mock:
        pass

    #  =================== TASK
    class Task_mock:
        def __init__(self):
            self.args = {}

    #  =================== TEMPLAR
    class Templar_mock:
        pass


    #  =================== INSTANCES MOCK
    action_base_m

# Generated at 2022-06-13 10:57:13.944614
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.utils.context_objects import AnsibleContext
    from ansible.utils.context_objects import AnsibleConnection
    from ansible.utils.context_objects import AnsibleTask
    from ansible.utils.context_objects import AnsibleTaskVars
    from ansible.utils.context_objects import AnsiblePlayContext
    from ansible.utils.context_objects import AnsibleLoader
    from ansible.utils.context_objects import AnsibleTemplar
    from ansible.utils.context_objects import AnsibleSharedLoaderObj

    am = ActionModule()

    am._task = AnsibleTask()
    am._task.args['_uses_shell'] = True
    am._connection = AnsibleConnection()
    am._play_context = AnsiblePlayContext()
    am._loader

# Generated at 2022-06-13 10:57:17.126894
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing ActionModule_run')
    action_module = ActionModule()
    action_module.run()
    print('ActionModule_run finished')

# Call test_ActionModule_run()
test_ActionModule_run()

# Generated at 2022-06-13 10:57:19.337894
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    abc = ActionModule()
    abc.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:57:19.916568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:20.888526
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Run method of class ActionModule
    pass

# Generated at 2022-06-13 10:57:27.961817
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    class MockActionBase():
        def __init__(self, action_base):
            pass
        def run(self, tmp=None, task_vars=None):
            pass

    class MockActionModule(ActionBase):
        def run(self, tmp=None, task_vars=None):
            del tmp  # tmp no longer has any effect

            # Shell module is implemented via command with a special arg
            self._task.args['_uses_shell'] = True


# Generated at 2022-06-13 10:57:34.310203
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Construct arguments with default values
    arguments = dict()

    # Construct parameters with default values
    parameters = dict()

    # Construct module with default arguments
    module = ActionModule(arguments, parameters)

    task_vars = {"ansible_facts": {"ansible_hostname": "vm-3003", "ansible_os_family": "RedHat"}, "var": "var1"}
    tmp = "/tmp/test-shell"
    module.run(tmp, task_vars)

# Generated at 2022-06-13 10:57:42.583658
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = dict()

    # Mock objects
    class MockActionBase(object):
        def __init__(self):
            self.called_methods = list()
            self._task = dict()
            self._task['args'] = dict()
            self._shared_loader_obj = dict()
            self._shared_loader_obj['action_loader'] = dict()
            self._shared_loader_obj['action_loader']['ansible.legacy.command'] = 'mock_command_action'
            self._connection = 'mock_connection'
            self._play_context = 'mock_play_context'
            self._loader = 'mock_loader'
            self._templar = 'mock_templar'


# Generated at 2022-06-13 10:57:54.442152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a ActionModule object
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.plugins.loader import action_loader
    from ansible.plugins.connection.netconf import Connection
    from ansible.plugins.action.command import ActionModule

    # Create a task_queue_manager object
    loader = DataLoader()

# Generated at 2022-06-13 10:57:54.913406
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:39.196528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.shell import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManag

# Generated at 2022-06-13 10:58:40.934284
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:58:48.494634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    inp_task_vars = {'var_1': 'var-1'}

    # Test with satisfied condition
    inp_task = {'args': {'_raw_params': 'echo'}}
    result = ActionModule(inp_task).run(task_vars=inp_task_vars)

# Generated at 2022-06-13 10:58:57.587661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.plugins.strategy import StrategyBase
  from ansible.playbook.block import Block
  from ansible.playbook.task import Task
  from ansible.playbook.handler import Handler
  from ansible.playbook.play import Play
  from ansible.playbook.play_context import PlayContext

  from ansible.template import Templar
  from ansible.vars.manager import VariableManager
  from ansible.context import CLIContext
  from ansible.executor.task_queue_manager import TaskQueueManager
  from ansible.parsing.dataloader import DataLoader
  from ansible.utils.display import Display

  from unittest import mock
  from docutils.utils import SystemMessage

  from ansible.plugins.action import ActionBase
  from ansible.plugins.action.shell import ActionModule

# Generated at 2022-06-13 10:58:58.186680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:58.794152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:59:09.095376
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    action_module = ActionModule()
    # Call method run of class ActionModule
    result = action_module.run()
    # Check if the result is a dict
    if not isinstance(result, dict):
        raise AssertionError("The action base class __init__ method should return a dict")
    # Check if the result has the keys _ansible_parsed, invoice, stdout_lines and _ansible_verbose_always
    keys = result.keys()
    for key in ['_ansible_parsed', 'invoice', 'stdout_lines', '_ansible_verbose_always']:
        if key not in keys:
            raise AssertionError("The action base class __init__ method should return a dict with key {}".format(key))

# Generated at 2022-06-13 10:59:18.634365
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mocking dependencies of method run of ActionModule - START
    import ansible.plugins.action
    mock_task_vars = {'ansible_version': {'full': '2.4.0'}}
    # Importing module under test
    from ansible.plugins.action.shell import ActionModule
    # Mocking dependencies of method run of ActionModule - END
    ansible_shell_instance = ActionModule(
            {'name': 'shell', 'action': 'shell', 'extras': {'_uses_shell': True}}
            , connection='ssh', play_context={}, loader={}, templar={}, shared_loader_obj={})
    ansible_shell_instance._task.args = {'_uses_shell': True}

# Generated at 2022-06-13 10:59:27.818321
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Fake_task():
        def __init__(self):
            self.args = {}

    class Fake_connection():
        def __init__(self):
            self.__class__.name = 'local'
            self.__class__.transport = 'local'
            self.__class__.nocows = 1

    class Fake_play_context():
        def __init__(self):
            self.check_mode = False

    class Fake_shared_loader_obj():
        def __init__(self):
            pass

        def action_loader(self):
            class Fake_action_loader():
                def __init__(self):
                    pass


# Generated at 2022-06-13 10:59:34.243167
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Creating mock object for ActionModule class """
    mock_ActionModule_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    """ Creating a mock objec for command_action class loaded as ansible.legacy.command """
    command_action = mock.Mock()
    mock_ActionModule_obj._shared_loader_obj.action_loader.get.return_value = command_action

    """ creating an instance of result class """
    result_obj = result.Result(None)

    """ Calling the function run of class ActionModule """
    mock_ActionModule_obj.run(tmp=None, task_vars=None)

    """ Asserting the return value of run function """
    assert command_action.run.return_value == result

# Generated at 2022-06-13 11:00:59.530557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:09.781741
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    from ansible.plugins.action import ActionModule
    from ansible.module_utils.six import iteritems

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars

    from ansible.template import Templar
    
    #from ansible.plugins.loader import module_loader
    #from ansible.parsing.dataloader import DataLoader
    #from ansible.vars.manager import VariableManager
    #from ansible

# Generated at 2022-06-13 11:01:18.055500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    @param tmp: Path to the temporary directory.
    @type tmp: str
    @param task_vars: Dictionary of variables.
    @type task_vars: dict

    @return: Key-value pair from action plugin.
    @rtype: dict
    """
    # This is the default mock of _shared_loader_obj.action_loader.get
    # The code in run should override this method, so it is not defined here.
    return None


# Generated at 2022-06-13 11:01:27.503242
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create action module and mock action module
    actionModule = ActionModule()
    actionModule._loader = None
    actionModule._templar = None
    actionModule._task = None
    actionModule._connection = None
    actionModule._play_context = None
    actionModule._shared_loader_obj = None

    # Get method command from action module
    actionCommand = actionModule._shared_loader_obj.action_loader.get('ansible.legacy.command')
    actionCommand._loader = None
    actionCommand._templar = None
    actionCommand._task = None
    actionCommand._connection = None
    actionCommand._play_context = None
    actionCommand._shared_loader_obj = None

    # Create mocks to run method
    tmp = None
    task_vars = {}

    # Run method
    result_actionModule

# Generated at 2022-06-13 11:01:34.521697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(
        task=None, 
        connection=None,
        play_context=None,
        loader=None, 
        templar=None,
        shared_loader_obj=None
    )
    result = action_module.run(tmp=None, task_vars=None)
    assert result['rc'] == 0
    assert result['stdout'] == 'echo 123'
    assert result['stderr'] == ''
    assert result['stdout_lines'] == ['echo 123']
    assert result['stderr_lines'] == []

# Generated at 2022-06-13 11:01:36.907690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing some dummy data
    tmp = None
    task_vars = None

    # Creating the instance of class ActionModule
    test_instance = ActionModule(loader=None, connection=None, play_context=None, task=None, action_loader=None)

    # Passing the dummy data to the run method
    test_instance.run(tmp, task_vars)

# Generated at 2022-06-13 11:01:37.294317
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:01:47.657282
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C

    # Create a Task object
    task = Task()

# Generated at 2022-06-13 11:01:49.401553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    assert True

# Generated at 2022-06-13 11:01:49.919249
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass