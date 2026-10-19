

# Generated at 2022-06-13 10:52:39.917877
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:46.040371
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import ansible.plugins.action.command

    print(
        'hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahah')
    print(sys.modules['ansible.plugins.action.command'])

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:52:49.551078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell
    mod = ansible.plugins.action.shell.ActionModule(None, None, None, None, None, None)
    result = mod.run(None, {})
    assert('ansible.legacy.command' in result['ansible_facts'])

# Generated at 2022-06-13 10:52:50.143363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:51.216519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Not implemented"


# Generated at 2022-06-13 10:52:59.254227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(loader=None,
                                 shared_loader_obj=None,
                                 connection=None,
                                 play_context=None,
                                 loader_path=None,
                                 templar=None,
                                 task_vars={},
                                 delete_remote_tmp=None)
    result = action_module._execute_module(module_name='test_shell_module',
                                           module_args={})
    assert result['rc'] == 0
    assert result['stdout'] == 'some_test'

# Generated at 2022-06-13 10:53:04.259249
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.template import Templar

    shell = 'touch /tmp/test_shell'
    assert isinstance(shell, str)
    templar = Templar(loader=None, variables={})
    assert isinstance(templar, Templar)
    action = ActionModule(shell, templar, {}, {})
    assert isinstance(action, ActionModule)
    action.run()

# Generated at 2022-06-13 10:53:13.125850
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import doctest
    from collections import namedtuple
    from ansible.module_utils.pycompat24 import get_exception
    from io import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task


# Generated at 2022-06-13 10:53:24.891171
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # execute
  
  # we want to modify result
  class ActionModuleTest(ActionModule):
    pass
  class CommandActionTest:
    def run(self, task_vars=None):
      return dict(stdout='any_string')
  class ActionLoaderTest:
    def get(self, action, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
      return CommandActionTest()
  class SharedLoaderObjTest:
    action_loader = ActionLoaderTest()

  task_vars = dict()

# Generated at 2022-06-13 10:53:31.038506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {}
    result['invocation'] = {}
    result['invocation']['module_name'] = 'shell'
    result['invocation']['module_args'] = {}
    result['invocation']['module_args']['a'] = 'b'
    result['invocation']['module_args']['c'] = 'd'
    result['invocation']['module_args']['e'] = 'f'

    res = ActionModule.run(result)

    return res

# Generated at 2022-06-13 10:53:36.562318
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule()

    try:
        action.run()
    except KeyError:
        pass
    else:
        assert False, "Expect exception"

# Generated at 2022-06-13 10:53:37.549441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ans = ActionModule()
    print(ans.run())

# Generated at 2022-06-13 10:53:38.271867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:48.142170
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import action_loader

    class DummyTask:
        args = {'_uses_shell': False}

    class DummyCommand(object):

        def run(self, *args, **kwargs):
            return {'stdout': 'test_value'}

    class DummyLoader(object):

        def get(self, *args, **kwargs):
            return DummyCommand()

    class DummyVaultLib(VaultLib):
        def decrypt(self, *args, **kwargs):
            return ''

    class DummyActionBase(object):
        values = {}

    

# Generated at 2022-06-13 10:53:49.646451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test for the method 'run' of class 'ActionModule'."""

    # TODO: Implement unit test

    pass

# Generated at 2022-06-13 10:53:50.124784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:56.184771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a object of class ActionModule.
    # Dependency of ActionModule is ActionBase. Hence create a dummy object of ActionBase
    actionBaseObj = ActionBase()
    aModule = ActionModule(actionBaseObj)
    
    #Create a new object of class ansible.plugins.loader._shared_loader_obj
    # This class is used for storeing the variables shared across ansible plugins
    sLoaderObj = ansible.plugins.loader._shared_loader_obj()
    
    #Create a new object of class ansible.plugins.loader.action_loader
    # This class loads action plugins
    actionLoaderObj = ansible.plugins.loader.action_loader(sLoaderObj)
    
    #Create a new object of class ansible.plugins.action.command
    # This class is used to run ansible command.
    # This class is dependent

# Generated at 2022-06-13 10:54:07.500314
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Save the original copy of ActionBase._execute_module
    execute_module = ActionBase._execute_module
    # Mock the _execute_module method
    ActionBase._execute_module = CLASS_execute_module
    # Unit test for method run of class ActionModule
    action_module = CLASS_ActionModule()
    # Load the task
    task_loader = TaskLoader(None)
    # Load the task into the task_loader
    task_loader._make_task_list("Test task")
    # Load the task into the task_loader
    task_loader._make_task_list("Test task")
    # Load the task from the task_loader into the task
    task = Task()
    task._copy_data(task_loader._tasks[0])
    # Make the task into the task of ActionModule
    action_module._task = task

# Generated at 2022-06-13 10:54:16.712812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creation of a fake task and its arguments
    task_args = dict()
    task_args['_uses_shell'] = True
    # Creation of a fake task with the previous arguments
    task = dict()
    task['args'] = task_args
    # Creation of a fake connection
    connection = dict()
    # Creation of a fake play_context
    play_context = dict()
    # Creation of a fake loader
    loader = dict()
    # Creation of a fake templar
    templar = dict()
    # Creation of a fake shared_loader_obj
    shared_obj = dict()
    # Creation of a fake command_action
    command_action = dict()
    # Creation of the fake task_vars
    task_vars = dict()
    # Creation of the ActionModule's object to test

# Generated at 2022-06-13 10:54:21.278998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    config_dict = {'host_list': [{'hostname': 'localhost', 'port': 1234}]}
    command_action = ActionModule(config_dict, 'ansible.legacy.shell')
    task_vars = {}
    result = command_action.run(task_vars=task_vars)
    assert result['invocation']['module_args']['_uses_shell'] == True

# Generated at 2022-06-13 10:54:25.906891
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:26.371936
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:54:34.192214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = __import__("ansible.plugins.action.shell").plugins.action.shell

# Generated at 2022-06-13 10:54:36.064157
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    ActionModule.run(task_vars=task_vars)

# Generated at 2022-06-13 10:54:37.617505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # TODO: Implement real unit tests
  pass

# Generated at 2022-06-13 10:54:45.845746
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Mock the arguments and return values for run()
    tmp, task_vars = {}, {}
    command_action_run_return = dict(
        changed=True,
        _ansible_no_log=False,
        _ansible_verbose_always=True,
        _ansible_ok_name='unused_ok_name',
        _ansible_parsed=True,
        _ansible_item_label='unused_item_label',
        _ansible_diff=None,
        stderr="",
        stderr_lines=[],
        stdout="",
        stdout_lines=[],
        cmd='/bin/false'
    )

    class MockActionLoader:
        def __init__(self, action_loader_get_return):
            self.action_loader_get_return

# Generated at 2022-06-13 10:54:57.081634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    instantiate_ansible = __import__('ansible')
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.shell import ActionModule
    from ansible.template import Templar
    import os

    # Create instance of class ActionBase
    play_context = instantiate_ansible.playbook.PlayContext()
    action_base_instance = ActionBase(play_context, dict(), None, 'hgw_zabbix')

    # Create instance of class ActionModule
    command_action = instantiate_ansible.plugins.action.command.ActionModule(play_context, dict(), None, 'hgw_zabbix')
    play_context.become = 'yes'
    templar = Templar(loader=None, variables={})
    module_name = 'hgw_zabbix'
   

# Generated at 2022-06-13 10:54:57.462819
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:08.208585
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Delete these if you want to see the output of your run
    from ansible import context
    context.CLIARGS = {'ignore_deprecations': True}

    # DECLARE & INITIALIZE VARIABLES
    output = ""
    failed = False

    # Create a mock task so we can create a mock shared_loader_obj
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    task = Task()
    task._role = Role()
    task._block = Block()
    task.block = None
    task.dep_chain = Task()

# Generated at 2022-06-13 10:55:18.769077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance of class with mocked attributes
    mock_task_vars = dict()
    action_module = ActionModule()
    action_module._task = dict()
    action_module._task.args = dict()
    action_module._shared_loader_obj = dict()
    action_module._shared_loader_obj.action_loader = dict()
    action_module._shared_loader_obj.action_loader.get = dict()
    action_module._connection = dict()
    action_module._play_context = dict()
    action_module._loader = dict()
    action_module._templar = dict()

    # Make the tested call
    returned_result = action_module.run(tmp = None, task_vars = mock_task_vars)

    # Assert return value
    assert returned_result == None
   

# Generated at 2022-06-13 10:55:26.701203
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:27.265885
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:55:34.263775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    set_module_args({
        '_ansible_shell_executable': ['/bin/sh', '-c'],
        '_uses_shell': True,
        '_raw_params': 'echo test',
        '_ansible_verbosity': 0,
        '_ansible_no_log': False,
        '_ansible_debug': False
    })
    stub(ActionBase, 'run')

    action_module = ActionModule()
    command_action = ActionBase()
    command_action.run = Mock()
    action_module._shared_loader_obj.action_loader.get = Mock(return_value=command_action)

    result = action_module.run(task_vars=Mock())

    assert result == command_action.run.return_value
    assert result['rc'] == 0
   

# Generated at 2022-06-13 10:55:47.991805
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    import ansible.executor.task_executor
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    import ansible.plugins.action.command

    # Create temporary test file
    tmpdir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmpdir, 'test_file')
    task_vars = {'test_var': 'test_value'}
    res_data = {'test_var': 'test_value', 'test_var2': 'test_value2'}


# Generated at 2022-06-13 10:55:54.678210
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
        Unit test for method run of class ActionModule

        Tests by mocking class objects and matching the output
    """
    from ansible.plugins.action.shell import ActionModule as ShellModule
    from ansible.plugins.action.command import ActionModule as CommandModule
    from test.unit.plugins.action.fixtures import action_fixtures

    actionFixture11 = action_fixtures.ActionFixture11()
    actionFixture12 = action_fixtures.ActionFixture12()

    actionModule = ShellModule(actionFixture11._task, actionFixture11._connection, actionFixture11._play_context, actionFixture11._loader, actionFixture11._templar, actionFixture11._shared_loader_obj)

# Generated at 2022-06-13 10:55:55.232571
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    assert mod

# Generated at 2022-06-13 10:56:06.250125
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks for ActionModule.run method
    task_vars = {}
    action = ActionModule()
    action.__dict__.update({'_task': {}, '_connection': {}, '_play_context': {}, '_loader': {}, '_templar': {}, '_shared_loader_obj': {}})
    action._task.args = {}
    action._task.args['_uses_shell'] = True
    action._shared_loader_obj.action_loader = {}
    command_action = {}
    command_action.run = {}
    action._shared_loader_obj.action_loader.get = lambda *x, **y: command_action
    command_action.run.return_value = {}

    result = action.run(task_vars=task_vars)

    # Check that

# Generated at 2022-06-13 10:56:09.836199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    task_vars = {}
    result = a.run(None, task_vars)
    # this is a weird test, but it should not fail
    assert isinstance(result, dict)
    return True

# Generated at 2022-06-13 10:56:18.891547
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader, connection_loader, action_loader

    mod_obj = action_loader.get('shell',
                                task=None,
                                connection=None,
                                play_context=None,
                                loader=None,
                                templar=None,
                                shared_loader_obj=None)
    mod_obj.run()

# Generated at 2022-06-13 10:56:29.129813
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockTask:
        def __init__(self):
            self.args = {}

    class MockConnection:
        def __init__(self):
            pass

    class MockPlayContext:
        def __init__(self):
            pass

    class MockLoader:
        def __init__(self):
            pass

    class MockTemplar:
        def __init__(self):
            pass

    class MockSharedLoaderObj:
        def __init__(self):
            class MockActionLoader:
                def get(self, action_name, task, connection, play_context, loader, templar, shared_loader_obj):
                    return action_name
            self.action_loader = MockActionLoader()

    actionbase_obj = ActionBase()
    mock_loader = MockLoader()
    mock_templar = MockTem

# Generated at 2022-06-13 10:56:50.894467
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    b_obj = ActionModule(loader=None,
                         connection=None,
                         play_context=None,
                         loader=None,
                         templar=None,
                         shared_loader_obj=None)
    task_vars = {'ansible_facts': {}}
    result = b_obj.run(None, task_vars)

    assert '_uses_shell' in b_obj._task.args
    assert b_obj._task.args['_uses_shell'] == True

# Generated at 2022-06-13 10:57:00.765449
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    loader = DictDataLoader({
        "test_playbook.yaml": """
- name: test_shell
  hosts: all
  tasks:
  - name: echo hello
    shell: echo hello"""
    })
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play.load(loader.get_basedir() + '/test_playbook.yaml', variable_manager=variable_manager, loader=loader)
    play._variable_manager = variable_manager
    play._tqm = TaskQueueManager(inventory=inventory, variable_manager=variable_manager, loader=loader)
    play.post_validate(play._ds, [play._tqm])

    commands = play._tqm._fact_cache[0]

# Generated at 2022-06-13 10:57:13.559257
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:57:20.287261
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # pylint: disable=no-self-use
    class TaskModule:
        def __init__(self, args):
            self.args = args

    dummy_task = TaskModule({'_uses_shell': True})
    action = ActionModule(task=dummy_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    result = action.run(task_vars=task_vars)
    assert result

# Generated at 2022-06-13 10:57:20.889509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:27.962154
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec={
            'test_param': {'type': 'bool'},
        },
        supports_check_mode=True
    )
    action = ActionModule(module, {})

# Generated at 2022-06-13 10:57:34.309774
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(task=None,connection=None,play_context=None,loader=None,templar=None,shared_loader_obj=None)
    '''
    :param task:
    :param connection:
    :param play_context:
    :param loader:
    :param templar:
    :param shared_loader_obj:
    '''
    actionModule.run(tmp=None,task_vars=None)

# Generated at 2022-06-13 10:57:38.437055
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()
    module._task.args = {
        '_raw_params': 'echo "###OK###"',
        '_uses_shell': True,
        'executable': '/bin/sh'
    }

    task_vars = {}

    module.run(task_vars = task_vars)

# Generated at 2022-06-13 10:57:45.837080
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 10:57:56.911494
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  test_task_vars = dict(ansible_user=None, ansible_shell_type=None, ansible_python_interpreter=None, ansible_connection=None, ansible_ssh_common_args=None, ansible_shell_executable=None, ansible_shell_type=None, ansible_user=None, ansible_shell_executable=None, ansible_python_interpreter=None, ansible_connection=None, ansible_ssh_common_args=None)
  test_tmp = None
  test_ActionModule = ActionModule()
  print(test_ActionModule.run("", test_task_vars))

# Generated at 2022-06-13 10:58:49.741205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    FAKE_TASK_VARS = {}
    FAKE_RESULT = {'test': 'result'}
    FAKE_PARAMS = {}
    FAKE_SHELL = 'ansible.legacy.shell'
    FAKE_MODULE_UTILS = 'ansible.module_utils.basic'
    FAKE_COMMAND_ACTION = {'test': 'command_action'}

    class ActionBase:
        def __init__(self):
            self._task = {}
            self._task['args'] = FAKE_PARAMS
        def run(self, task_vars=None):
            return self._task['args']

    class Loader:
        def __init__(self):
            self.action_loader = {'ansible.legacy.command': FAKE_COMMAND_ACTION}

   

# Generated at 2022-06-13 10:58:58.248821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible import context
    from collections import namedtuple
    from ansible.playbook.task import Task

    Options = namedtuple('Options',
                         ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection', 'module_path', 'forks',
                          'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args',
                          'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])

# Generated at 2022-06-13 10:58:58.840533
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:09.130512
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task

    from ansible.playbook.play_context import PlayContext

    from ansible.utils.vars import combine_vars

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create play_context object
    play_context = PlayContext()

    # Create dataloader object
    loader = DataLoader()

    # Create inventory object
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create task object
    task = Task()
    task

# Generated at 2022-06-13 10:59:18.635590
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    temporary_directory = "/tmp/test_ansible_playbook"
    host_vars = {}
    host_vars["ansible_connection"] = "local"
    host_vars["ansible_python_interpreter"] = "/usr/bin/python"
    host_vars["ansible_shell_type"] = "csh"
    host_vars["ansible_shell_executable"] = "/bin/csh"
    host_vars["ansible_user"] = "blah"
    host_vars["ansible_host"] = "localhost"
    host_vars["ansible_hostname"] = "localhost"
    inventory = {}
    inventory["all"] = {}
    inventory["all"]["hosts"] = ["localhost"]
    inventory["all"]["vars"] = host_vars

# Generated at 2022-06-13 10:59:21.951981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule_ = ActionModule(loader=None, action=None, play_context=None, os=None, loader_obj=None)
    ActionModule_.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:59:23.314060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass #TODO: write unit test for method run of class ActionModule


# Generated at 2022-06-13 10:59:24.043582
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:36.360388
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible.plugins.loader as loader_pkg
    loader_for_test=loader_pkg.ActionModuleLoader(None, None)
    from ansible.plugins.action.shell import ActionModule as ActionModule_shell
    module = ActionModule_shell(None, {}, None, None, None, None, loader_for_test)

    # the attribute _task.args['_uses_shell'] is set in the method run
    module.run()
    #print("result: {}".format(module._task.args['_uses_shell']))
    assert module._task.args['_uses_shell'] == True

    # test_ActionModule_run

# Generated at 2022-06-13 10:59:44.784859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    
    action_module = ActionModule()
    # the passed arg is useless for shell.run() method, so just create a stub for it
    task_vars = "SomeString"

    # create a fake play context
    play_context = PlayContext()
    play_context.connection = "local"
    play_context.remote_user = 'stack'
    play_context.become = False
    play_context.become_method = "sudo"
    play_context.become_user = "stack"
    play_context.check_mode = False

    # create a fake task queue manager
    task_queue_manager = TaskQueueManager()
    
    # init the action module
    action

# Generated at 2022-06-13 11:01:15.915597
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:01:17.474305
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:18.036060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:27.458966
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    options = {
        "chdir": "some/path",
        "_": "some other string"
    }
    play_context = MockPlayContext()
    loader = "some loader"
    templar = "some templar"
    display = MockDisplay()
    connection = "some connection"
    task = MockTask()
    # test with no args
    action_module = ActionModule(task, connection, play_context, loader, templar, share_loader=True, display=display)

    with patch.object(action_module._shared_loader_obj.action_loader, 'get') as mock_get:
        action_module.run(task_vars=options)

# Generated at 2022-06-13 11:01:30.000363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {}
    keys = []
    test_obj = ActionModule(keys, result, "")

    # test with empty tmp
    tmp = None
    test_obj.run(tmp)
    # test with tmp
    tmp = {'cmd': 'cmd'}
    keys = ['cmd']
    test_obj.run(tmp)

# Generated at 2022-06-13 11:01:32.510376
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    tmp = None
    task_vars = None
    result = action_module.run(tmp,task_vars)
    print(result)

# Generated at 2022-06-13 11:01:35.155088
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:01:41.974080
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = get_module_class('command')
    command = 'echo "foo"'
    args = dict(creates='/tmp/foo',
                chdir='/tmp',
                executable='/bin/bash',
                removes='/tmp/bar',
                warn=False,
                _uses_shell=True)

    task = dict(action=dict(module=module, args=args),
                async_val=15,
                delegate_to='localhost',
                become_user='bob',
                become=None,
                delegate_facts=None,
                register='shell_out',
                environment=None,
                no_log=False,
                stdin=None,
                stdin_add_newline=True,
                ignore_errors=False)
    task = Task.load(task)

# Generated at 2022-06-13 11:01:42.799257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False



# Generated at 2022-06-13 11:01:52.097198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader

    from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
    from ansible_collections.cisco.iosxr.tests.unit.compat.mock import MagicMock
    from ansible_collections.cisco.iosxr.tests.unit.compat.mock import PropertyMock

    # set up mocks
    mock_loader = MagicMock()
    mock_task = MagicMock()
    mock_loader.action_loader = action_loader
    mock_connection = MagicMock(connection_loader=connection_loader)
    mock_play_context = MagicMock()
    mock_shared_loader