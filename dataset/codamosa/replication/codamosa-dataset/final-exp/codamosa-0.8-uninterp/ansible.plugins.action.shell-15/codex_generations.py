

# Generated at 2022-06-13 10:52:52.254576
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# Mock framework objects
	mock_task = type('', (), {})()

	mock_task.args = {'_uses_shell': True}

	mock_connection = type('', (), {})()

	mock_play_context = type('', (), {})()

	mock_loader = type('', (), {})()

	mock_templar = type('', (), {})()

	mock_shared_loader_obj = type('', (), {})()

	mock_action_loader = type('', (), {'get': lambda x, task=mock_task, connection=mock_connection, play_context=mock_play_context, loader=mock_loader, templar=mock_templar, shared_loader_obj=mock_shared_loader_obj: 'command'})
	

# Generated at 2022-06-13 10:52:54.865500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.modules.shell import ActionModule as am
    assert isinstance(am(), am)

# Generated at 2022-06-13 10:52:55.640072
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:08.276860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(connection=None,
                                 task=dict(
                                     args=dict(
                                         _uses_shell=True,
                                         chdir='/home/foo',
                                         executable='/bin/bash',
                                         free_form='/bin/sh -c "ls /home/foo"',
                                         creates='/home/foo/bar.txt'),
                                     get_attributes=dict(
                                         become=True,
                                         become_method='sudo',
                                         become_user='foo')),
                                 play_context=None,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)
    result = action_module.run(task_vars=dict(ansible_tmpdir='/tmp'))

# Generated at 2022-06-13 10:53:22.178400
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import PY3
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play import Play
    import ansible.playbook.play
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_result import TaskResultCallback
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

# Generated at 2022-06-13 10:53:27.361972
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule

    task = None
    loader = None
    templar = None
    shared_loader_obj = None
    play_context = None
    connection = None
    action_module = ActionModule(task, loader, templar, shared_loader_obj, connection, play_context)  

    tmp = None
    task_vars = {}
    result = action_module.run(tmp, task_vars)
    assert result is not None

# Generated at 2022-06-13 10:53:28.059860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:28.652790
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:38.652703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    from ansible.playbook.play_context import PlayContext

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.cli import CLI
    
    module_name = 'ansible.legacy.shell'
    action_class = ActionBase.load_action_plugin(module_name, module_name)
    action = action_class(task=Task(), connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    result = action.run(task_vars={})

    assert result["rc"] == 1

# Generated at 2022-06-13 10:53:39.399796
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.run()

# Generated at 2022-06-13 10:53:51.710245
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.template import Templar

    t = Templar()
    task = Task()

# Generated at 2022-06-13 10:53:52.515251
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	pass

# Generated at 2022-06-13 10:53:53.680822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # The run method of the Ansible Script ActionModule should call the run
    # method of the Ansible Script command action
    pass

# Generated at 2022-06-13 10:53:59.280755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None

# Generated at 2022-06-13 10:54:01.163122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # TODO: write tests for method run of class ActionModule
    #
    assert False

# Generated at 2022-06-13 10:54:11.007677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule('ansible.legacy.shell', 'task', 'connection', 'play_context', 'loader', 'templar', 'shared_loader_obj')
    command_action = action._shared_loader_obj.action_loader.get('ansible.legacy.command',
                                                                   task=action._task,
                                                                   connection=action._connection,
                                                                   play_context=action._play_context,
                                                                   loader=action._loader,
                                                                   templar=action._templar,
                                                                   shared_loader_obj=action._shared_loader_obj)
    command_action._debug = "Debug"
    command_action._diff = "Diff"
    command_action._remote_tmp = "/tmp"
    command_action._connection = "connection"
    command

# Generated at 2022-06-13 10:54:17.803408
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    place_holder_obj = None

    command_action = place_holder_obj
    _loader = place_holder_obj
    _templar = place_holder_obj
    _task = place_holder_obj
    _connection = place_holder_obj
    _play_context = place_holder_obj
    _shared_loader_obj = place_holder_obj

    a = ActionModule(command_action,
                        _loader,
                        _templar,
                        _task,
                        _connection,
                        _play_context,
                        _shared_loader_obj)

    assert a.run() != None

# Generated at 2022-06-13 10:54:25.280821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    module = ActionModule()
    path_to_main = os.path.dirname(os.path.realpath(__file__))
    module._shared_loader_obj = DictDataLoader({path_to_main: DictDataFinder({'path_to_main': path_to_main}, [])})
    
    class ActionBase_module:
        def get(self, name, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            self.name = name
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj

    module._shared_

# Generated at 2022-06-13 10:54:36.647490
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Init class
  modules = ['ansible.legacy.command']
  self._shared_loader_obj = SharedPluginLoaderObj(modules=modules)
  self._task = task
  self._connection = connection
  self._play_context = play_context
  self._loader = loader
  self._templar = templar
  self._task.args['_uses_shell'] = True

  # Init command_action object

# Generated at 2022-06-13 10:54:45.028235
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit test this method
    task = klass("")
    task.action = "shell"
    task.args = {'_uses_shell': True}
    task._task = task
    shared_loader_obj = klass("")
    task._shared_loader_obj = shared_loader_obj
    task_vars = {}

    shell_action = ActionModule(task, klass(""), klass(""), klass(""), klass(""), klass(""), klass(""))
    command_action = klass("")
    shell_action._task.args['_uses_shell'] = True
    task = shell_action._task
    task.action = "ansible.legacy.command"
    shell_action.run(task_vars=task_vars)

# Generated at 2022-06-13 10:54:59.229042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    
    # Testing with default/empty parameters
    a.run(tmp=None,task_vars=None)
    
    # Testing with empty tmp and default task_vars
    a.run(tmp=None,task_vars=None)
    
    # Testing with empty tmp and custom task_vars
    a.run(tmp=None,task_vars={'a':'b'})
    
    # Testing with tmp as None and custom task_vars
    a.run(tmp=None,task_vars={'a':'b'})
    
    # Testing with tmp as path and custom task_vars
    a.run(tmp='/',task_vars={'a':'b'})
    
    # Testing with tmp as path and default task_vars

# Generated at 2022-06-13 10:55:09.448244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup variables for test
    task_vars = dict()
    tmp = dict()

    # Test for module with no args passed
    # Setup variables for test
    action = AnsibleAction(task_vars, tmp)
    result = action.run(task_vars)
    # Module name is command
    assert result.keys()[0] == 'ansible.legacy.command'

    # Test for module with args passed
    # Setup variables for test
    task_vars = {'args': {'_raw_params': '/bin/echo "Hello"'}}
    action = AnsibleAction(task_vars, tmp)
    result = action.run(task_vars)
    # Module name is command
    assert result.keys()[0] == 'ansible.legacy.command'
    # Check if args is passed correctly

# Generated at 2022-06-13 10:55:10.000862
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:55:11.879247
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	print('Test 1: method run of class ActionModule')
	assert 1 == 1


# Generated at 2022-06-13 10:55:21.800429
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'localhost'
    play_context = PlayContext()
    play_context.check_mode = False
    play_context.verbosity = 4
    play_context.connection = 'local'
    play_context.network_os = 'any'
    play_context.remote_addr = host
    play_context.remote_user = 'root'
    play_context.port = 22
    loader = DataLoader()
    templar = Templar(loader=loader)

# Generated at 2022-06-13 10:55:30.696164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = '''{
        "action": "shell", 
        "name": "shell", 
        "args": {
          "_raw_params": "echo 'HELLO WORLD'", 
          "chdir": null, 
          "_uses_shell": true
        }, 
        "env": {}, 
        "always_run": false, 
        "register": null
      }'''
    mock_task = json.loads(mock_task)
    expected_result = {
            "pid": 15803, 
            "stderr": "", 
            "stdout": "HELLO WORLD\n", 
            "stdout_lines": [
                "HELLO WORLD"
            ], 
            "warnings": []
    }

# Generated at 2022-06-13 10:55:31.704228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: implement test case
    assert False

# Generated at 2022-06-13 10:55:40.936665
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import unittest
    import unittest.mock as mock
    from ansible.module_utils._text import to_bytes

    # import ansible.plugins.action.shell as shell
    # Reload module to clear mocks
    import importlib
    importlib.reload(sys.modules[__name__])
    from ansible.plugins.action.shell import ActionModule as shell

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple

    class TestCommandAction(unittest.TestCase):

        class TestOptions(object):
            _connection = None
            become = False
           

# Generated at 2022-06-13 10:55:41.391491
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()

# Generated at 2022-06-13 10:55:50.398401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.playbook.play
    import ansible.playbook.task
    class Task(object):
        def __init__(self, args):
            self.args = args
    class Args(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    task = Task(Args(**{'_uses_shell': True}))
    my_task = ansible.playbook.task.Task()
    my_task._task = task
    my_task._connection = None
    my_task._play_context = None
    my_task._loader = None
    my_task._templar = None
    my_task._shared_loader_obj = None

# Generated at 2022-06-13 10:56:08.432150
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:56:17.635696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    arg = {}
    arg['_ansible_verbosity'] = 5
    arg['_uses_shell'] = False
    arg['chdir'] = None
    arg['creates'] = None
    arg['executable'] = None
    arg['removes'] = None
    arg['warn'] = True
    arg['_raw_params'] = 'echo "Hello World"'
    r_arg = {'_raw_params': 'echo "Hello World"'}
    from ansible.plugins.action.command import ActionModule as command_action_module
    class Mock_command_action(command_action_module):
        def run(self, task_vars=None):
            self.assertEqual(self._task.args, r_arg)
            return "Hello World"
    class Mock_command_connection:
        pass

# Generated at 2022-06-13 10:56:23.614816
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create the object under test here, stubbing out necessary arguments
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Call method under test
    result = am.run(tmp=None, task_vars=None)

    # Assert the test results here
    assert result == {'foo': 'bar'}

# Generated at 2022-06-13 10:56:24.310998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:24.907911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:30.126183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock of ActionBase class
    actionbase_instance = ActionBase()

    # Create a mock of ActionModule class
    actionmodule_instance = ActionModule()

    # Create a dictionary of arguments required for method
    # ActionModule.run
    args = {
        'tmp': None,
        'task_vars': None,
    }

    # Test method ActionModule.run with arguments
    actionmodule_instance.run(**args)

# Generated at 2022-06-13 10:56:30.953950
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:39.861966
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import io
    import sys
    import traceback
    from collections import namedtuple

    from ansible.plugins.action import ActionBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.utils.vars import load_extra_vars
    from ansible.playbook.block import Block



# Generated at 2022-06-13 10:56:46.443698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = 'tmp'
    task_vars = {'some': 'thing'}
    class ActionModule_mock():
        def __init__(self, tmp, task_vars):
            self.tmp = tmp
            self.task_vars = task_vars
        def run(self, tmp, task_vars):
            assert self.tmp == tmp
            assert self.task_vars == task_vars
    action_module_obj = ActionModule_mock(tmp, task_vars)
    result = action_module_obj.run('tmp', {'some': 'thing'})

# Generated at 2022-06-13 10:56:48.892024
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    p = ActionModule()
    # TODO: write unit test
    # p.run(tmp=None, task_vars=None)


# Generated at 2022-06-13 10:57:06.039046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    TODO: Implement unit test for method run of class ActionModule
    """
    pass

# Generated at 2022-06-13 10:57:10.925812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run()")
    data = {
        ('shell', ('ansible.legacy.command', 'unit_test'))
    }
    s = ActionModule()
    s.run(data)
# Unit test of class ActionModule

# Generated at 2022-06-13 10:57:20.796890
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action import ActionModule

    from ansible.module_utils._text import to_text, to_bytes
    from ansible.compat.tests.mock import patch

    # Create an instance of class ActionModule to use in test
    action = ActionModule(
        task={'args': {'name': 'test'}},
        connection={},
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Create a mock class for ActionBase's load_module_utils()
    class MockLoadModuleUtils:
        return_value = 'fake_utils'  # Use a fake string as return value

        # This method will be patched in to replace the original method
        def load_module_utils(self):
            return self.return_

# Generated at 2022-06-13 10:57:22.931962
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell as shell

    actionmodule = shell.ActionModule()

    actionmodule.run()


# Generated at 2022-06-13 10:57:34.054150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell_local import ActionModule
    from ansible.error import AnsibleAction, AnsibleError
    import os
    import tempfile

    if os.environ.get('TEST_UNIT_TEST'):
        test_unit_test = os.environ.get('TEST_UNIT_TEST')
    else:
        test_unit_test = False

    module_name = 'shell_local'

    # Unclutter the module path
    if '_' in module_name:
        module_split = module_name.split('_')
    else:
        module_split = module_name.split('.')

    from ansible.plugins import action_loader
    action_class = action_loader._load_action_plugin(module_split[0], module_split[1])


# Generated at 2022-06-13 10:57:35.026876
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.run()

# Generated at 2022-06-13 10:57:41.084385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a mock module
    module = MockModule()

    # create a mock PlayContext
    pc = MockPlayContext()

    # create a mock TaskExecutor
    te = MockTaskExecutor(pc)

    # create a mock task
    task = MockTask()

    # create a new ActionModule and execute the run method
    am = ActionModule(task, connection=None, play_context=pc, loader=None,
                      templar=None, shared_loader_obj=None)

    am.run()

    assert(am._task.args['_uses_shell'] == True)

# Generated at 2022-06-13 10:57:46.010479
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test_play_context is a fake object imported in module
    # ansible.playbook.play_context.PlayContext
    # In this test, it's only used to call the constructor of class ActionBase
    test_task = Task()
    test_task.args = {'_uses_shell': 'False'}
    test_module = ActionModule(None, test_task, None, None, None, None, None)
    assert test_module.run()['cmd'] == '/bin/sh -c '

###############################################################################


# Generated at 2022-06-13 10:57:46.891485
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    print()

# Generated at 2022-06-13 10:58:00.067094
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    play_context = dict()
    connection = dict()
    loader = dict()
    templar = dict()
    shared_loader_obj = dict()

    task = dict()
    task["args"] = dict()
    task["args"]["_uses_shell"] = True

    action_module = dict()
    action_module["action"] = dict()
    action_module["action"]["ActionModule"] = dict()
    action_module["action"]["ActionModule"]["name"] = "ActionModule"
    action_module["action"]["ActionModule"]["version"] = "1.0.0"
    action_module["action"]["ActionModule"]["action"] = ActionModule
    action_module["action"]["ActionModule"]["_task"] = task



# Generated at 2022-06-13 10:58:47.548316
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib

    action_module = ActionModule()

    setattr(action_module._task.args, 'command', 'echo hello')
    setattr(action_module._task.args, 'creates', '/tmp/test')
    setattr(action_module._task.args, 'removes', '/tmp/test')
    setattr(action_module._task.args, 'executable', '/bin/bash')

    action_module._shared_loader_obj = None
    action_module._task = None
    action_module

# Generated at 2022-06-13 10:58:54.826869
# Unit test for method run of class ActionModule
def test_ActionModule_run():

        # Arrange
        # Create an object of ActionModule class
        action_module_obj=ActionModule()

        # mock a task
        task = MagicMock()
        # mock a loader
        loader=MagicMock()
        # set the loader attribute of ActionModule object
        action_module_obj._loader = loader

        # Set attributes of a task
        task.args = dict()
        task.args['_uses_shell'] = True
        task.action = 'shell'

        # Set attributes of ActionModule object
        action_module_obj._task = task
        action_module_obj._shared_loader_obj = 1
        action_module_obj._play_context = 1
        action_module_obj._templar = 1
        task_vars = dict()
        task_vars['ansible_check_mode'] = False

# Generated at 2022-06-13 10:59:05.751370
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule({'name': 'test for method run of class ActionModule',
         'tags': ['t1'],
         'when': [{'variable': 'ansible_version'}],
         'args': {'_uses_shell': 1}},
         '',
         '',
         '',
         None)
    result = m.run(None, {'ansible_version': '2.6.0'})
    print(result)
    assert 'ansible_facts' in result and \
           'ansible_version' in result['ansible_facts'] and \
           'revision' in result['ansible_facts']['ansible_version'] and \
           result['ansible_facts']['ansible_version']['revision'] == '39ba8b550c'



# Generated at 2022-06-13 10:59:07.184100
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    assert a.run() is not None

# Generated at 2022-06-13 10:59:07.758084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:09.234941
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    _ActionModule = ActionModule()
    _ActionModule.run()

# Generated at 2022-06-13 10:59:09.917151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:19.609655
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.command import ActionModule
    from ansible import constants as C
    from ansible.utils.color import stringc

    class FakeAction(ActionBase):

        # Method run of class ActionBase
        def run(self, tmp=None, task_vars=None):
            del tmp  # tmp no longer has any effect
            print('Hello there!')
            return 'result'

    class FakeLoader(object):
        def get(self, name, *args, **kwargs):
            if name == 'ansible.legacy.command':
                return FakeAction()


# Generated at 2022-06-13 10:59:28.266042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  out = {}
  out['system_tmpdir'] = '/var/tmp'
  out['system_tempdir'] = '/var/folders/xi/j9n7sljd1zs6xnly5vw0m7cm0000gn/T'
  var = {}
  var['ansible_connection'] = 'ssh'
  var['ansible_ssh_common_args'] = '-o StrictHostKeyChecking=no'
  var['ansible_ssh_host'] = '192.168.0.1'
  var['ansible_ssh_port'] = '22'
  var['ansible_ssh_private_key_file'] = '~/.ssh/id_rsa'
  var['ansible_ssh_user'] = 'suzen'

# Generated at 2022-06-13 10:59:33.333548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action_module_spec/test_action_module.py:31:in `test_run_uses_shell': "command" action has no method named "_run_uses_shell"
    print("test_ActionModule_run")
    assert False

# Generated at 2022-06-13 11:01:00.090755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule()

# Generated at 2022-06-13 11:01:04.294616
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = {'hostvars': {}}
    hostvars = data.get('hostvars')
    module_name = 'ansible_collections.ansible.builtin.shell'

    module = ActionModule(
        data,
        hostvars,
        module_name,
    )

    module.run()

# Generated at 2022-06-13 11:01:08.916644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    spec = {"test_attr": "_uses_shell"}
    module = ActionModule(None, task={"args": {"test_attr": 1}},
                          task_vars={"test_attr": 2},
                          loader=None,
                          templar=None,
                          shared_loader_obj=spec)
    module._shared_loader_obj = {"test_attr": 3}
    module._task = {"args": {"test_attr": 4}}
    module._connection = {"test_attr": 5}
    module._play_context = {"test_attr": 6}
    module._loader = {"test_attr": 7}
    module._templar = {"test_attr": 8}
    ActionBase._remove_tmp_path = lambda x: None


# Generated at 2022-06-13 11:01:20.544000
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test of the method ActionModule.run()
    """
    from ansible.errors import AnsibleActionFail
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    class Task:
        def __init__(self):
            self.args = {}
    class Connection:
        def __init__(self):
            pass
    class PlayContext:
        def __init__(self):
            pass
    class Loader:
        def __init__(self):
            pass
    class Templar:
        def __init__(self):
            pass
        def template(self, src, **kwargs):
            return src
    class ActionLoader:
        def __init__(self):
            pass

# Generated at 2022-06-13 11:01:21.605633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_fail_action_module = ActionModule()

# Generated at 2022-06-13 11:01:31.290422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    import ansible.plugins.action.command as command
    setattr(command, 'ActionModule', ActionModule)
    import ansible.plugins.loader as loader
    setattr(loader, 'ActionLoader', loader.ActionLoader)
    import ansible.plugins.loader.action_loader as action_loader
    setattr(action_loader, 'ActionModuleLoader', action_loader.ActionModuleLoader)
    import ansible.playbook.play_context as play_context
    setattr(play_context, 'PlayContext', play_context.PlayContext)
    import ansible.template as template
    setattr(template, 'AnsibleTemplar', template.AnsibleTemplar)
    import ansible.parsing.vault as vault
    setattr(vault, 'VaultLib', vault.VaultLib)


# Generated at 2022-06-13 11:01:39.358567
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test that in case of win_shell, that the shell module is used
    """
    action_base = ActionBase()
    action_base._connection = None
    action_base._task = None
    action_base._loader = None
    action_base._find_needle = None
    action_base._shared_loader_obj = None
    action_base._play_context = None
    action_base._templar = None

    action_module = ActionModule(action_base)
    action_module._task = {
        "action": {
            "__ansible_module__": "win_shell"
        },
        "args": {
            "_raw_params": "echo test",
            "_uses_shell": False
        }
    }

# Generated at 2022-06-13 11:01:43.734620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule(
        task = {
            'version': 2,
            'args': {
                'path': 'foo.bar',
                '_uses_shell' : True
            },
            'action': 'shell',
            'delegate_to': 'localhost',
        },
        connection = {},
        play_context = {},
        loader = {},
        templar = '',
        shared_loader_obj = {}
    )
    # test_module._task.args['_uses_shell'] = True
    result = test_module.run(tmp='foo.bar', task_vars=dict())
    print(result)
    assert 'invocation' in result
    assert 'module_args' in result['invocation']
    assert 'shell' in result['invocation']['module_args']

# Generated at 2022-06-13 11:01:44.227577
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:46.468648
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)