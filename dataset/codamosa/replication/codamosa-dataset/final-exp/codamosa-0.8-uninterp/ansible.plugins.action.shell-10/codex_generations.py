

# Generated at 2022-06-13 10:52:40.939842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:41.656768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 0

# Generated at 2022-06-13 10:52:52.226227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_name = __name__
    module_path = __file__

    class Task:
        def __init__(self):
            self.args = dict()

    class MyActionBase(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

        def _execute_module(self, tmp=None, task_vars=None, wrap_async=None):
            return dict()

    class MyLegacyModule:
        def __init__(self):
            self.connection = None

# Generated at 2022-06-13 10:52:53.335707
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert(True)

# Generated at 2022-06-13 10:53:04.632142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell
    task = None
    connection = None
    play_context = None
    loader = None
    templar = None
    shared_loader_obj = None
    action_module = ansible.plugins.action.shell.ActionModule(
        task,
        connection,
        play_context,
        loader,
        templar,
        shared_loader_obj
    )

    # The following code snippet is run to test the run method of class ActionModule
    tmp = None
    task_vars = None
    ret = action_module.run(tmp, task_vars)
    print(ret)


# Generated at 2022-06-13 10:53:05.353602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:13.782775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    class TestActionModule(unittest.TestCase):
        """
        Custom class for testing the ActionModule.
        """
        def setUp(self):
            self.tmp = None
            self.task_vars = None
            self.module = ActionModule()
            self.module._task = 'task'
            self.module._task.args = {}
            self.module._shared_loader_obj = 'shared_loader_obj'
            self.module._connection = 'connection'
            self.module._play_context = 'play_context'
            self.module._loader = 'loader'
            self.module._templar = 'templar'

        def testing_run(self):
            """
            Perform a test of the ActionModule class.
            """

# Generated at 2022-06-13 10:53:20.771259
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a._task = Dict()
    a._shared_loader_obj = Dict()
    a._connection = Dict()
    a._play_context = Dict()
    a._loader = Dict()
    a._templar = Dict()
    assert a.run(task_vars=Dict()) == Dict(**{'_uses_shell': True})

# Generated at 2022-06-13 10:53:30.699665
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This function creates a mock task and plays it using the action plugin
    """
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    import ansible.constants as C

    class CallbackModule(CallbackBase):
        """
        Callback module for this unit test
        """

# Generated at 2022-06-13 10:53:31.309945
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:37.743589
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModule_class:
        def __init__(self, actionbase):
            pass

        def run(self, tmp=None, task_vars=None):
            return None

    class ActionBase_class:
        def __init__(self):
            pass
    action_module = ActionModule_class(ActionBase_class())
    assert action_module.run() is None

# Generated at 2022-06-13 10:53:38.414436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:38.956820
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:53:40.503938
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:53:50.764969
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    print(" ".rjust(80, "="))
    print("Unit Test: Method: run of Class: ActionModule")
    print(" ".ljust(80, "="))

    # print("\nUnimplemented\n")
    # assert False

    # Declare variables
    test_ActionModule_run_task_args_dict = {}
    test_ActionModule_run_task_args_dict['_uses_shell'] = False
    test_ActionModule_run_task_vars_dict = {}

    # Create an instance of the class
    test_ActionModule_instance = ActionModule()

    # Set the _task.args['_uses_shell'] to False
    test_ActionModule_instance._task.args = test_ActionModule_run_task_args_dict
    # Set the _task.action to shell
    test_

# Generated at 2022-06-13 10:53:51.380940
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 10:53:57.540574
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up module parameters
    tmp = None
    task_vars = {'ansible_check_mode': True, 'shell_executable': '/bin/sh'}

    # Set up expected results
    expected_result = {'changed': False, 'cmd': '/bin/sh', 'delta': '0:00:00.002364', 'end': '2018-07-04 08:18:30.541748', 'rc': 0, 'start': '2018-07-04 08:18:30.539384', 'stderr': '', 'stderr_lines': [], 'stdout': '', 'stdout_lines': []}


    # Execute method and test results
    action_module = ActionModule()
    result = action_module.run(tmp, task_vars)
    assert result == expected_

# Generated at 2022-06-13 10:53:59.957828
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # test run with arguments
    module.run(tmp=None,task_vars=None)

# Generated at 2022-06-13 10:54:02.385774
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test: test_ActionModule_run """
    action = ActionModule()
    assert True

# Generated at 2022-06-13 10:54:03.134291
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:15.971741
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #1. setup
        #1.1 setup variables
    class tmp:
        pass
    class task_vars:
        pass
    class obj:
        pass
    obj.test = 'test'

    #1.2 setup mocks
    m = ActionModule(obj, obj, obj, obj)
    m._task.args = {'_uses_shell': True}
    m._shared_loader_obj.action_loader.get = Mock(return_value=Mock(return_value='result'))
    
    #2. exercise
    result = m.run(tmp=None, task_vars=None)

    #3. verify
    assert result == 'result'

# Generated at 2022-06-13 10:54:20.073466
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test ActionModule.run() takes positional arguments (tmp, task_vars)
    act_mod = ActionModule()
    assert act_mod.run(tmp=None, task_vars=None) is None

# Generated at 2022-06-13 10:54:23.689667
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action._task = "task"
    action._connection = "connection"
    action._play_context = "play_context"
    action._loader = "loader"
    action._templar = "templar"
    action._shared_loader_obj = "shared_loader_obj"
    action.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:54:29.408340
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    params = {'command': 'ls -l'}
    tmp = None
    task_vars = {'inventory_hostname': 'test1', 'test': 'test'}
    result = module.run(tmp, task_vars)
    print(result)

# Generated at 2022-06-13 10:54:40.531524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # assertEqual will be helpful for some testing
    from ansible.module_utils.six import assertRegex
    from ansible.module_utils.six.moves import builtins
    # Need to initialize module to run
    from ansible.plugins.action import ActionBase
    tmp = 'test_tmp'
    task_vars = 'test_task_vars'
    m = ActionModule(None, None, tmp, task_vars, None, None, None, None, None)

    # Test method with default return value
    assertRegex(m.run(tmp, task_vars), '\w+')
    # Test method with return value
    assertRegex(m.run(tmp, task_vars), '\w+\s+\w+')



# Generated at 2022-06-13 10:54:50.371904
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeOptionsModule:
        pass
    class FakeConnectionModule:
        pass
    class FakeSystemInfoModule:
        pass
    class FakeTaskModule:
        def __init__(self):
            self.args = {}
    class FakePlayContextModule:
        def __init__(self):
            self.become = None
            self.become_method = None
            self.become_user = None
            self.no_log = False
    class FakeTemplarModule:
        def __init__(self):
            self.environment = {}
        def template(self, string):
            return string
    class FakeLoaderModule:
        pass
    class FakeSharedLoaderObjModule:
        def __init__(self):
            self.action_loader = FakeActionLoaderModule()

# Generated at 2022-06-13 10:55:00.431180
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = dict(
        _uses_shell=True,
        _raw_params='/bin/false',
        _uses_shell=False,
        _uses_executable=None,
        _executable=None,
        chdir=None,
        creates=None,
        removes=None,
        warn=True,
        executable=None,
        _at_through_errors=False,
        # test_set_exception=None,
        # test_try_dont_have_become=False,
        # test_try_become=False,
        # test_try_no_become=False,
        # test_no_log=False,
        # test_stdout=None,
        # test_stderr=None,
        # test_rc=None,
    )

    # create a

# Generated at 2022-06-13 10:55:05.736285
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  print('In test_ActionModule_run')
  action_module = ActionModule(1,2,3)
  result = action_module.run(tmp=None, task_vars=None)
  print('result=%s' % str(result))
  assert result['invocation']['module_args']['chdir'] is None

# Generated at 2022-06-13 10:55:06.277216
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:11.879297
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Check method run of class ActionModule works."""
    # Create stub with desired method return values
    tmp = None

    task_vars = {}

    # Create action object
    action = ActionModule(None, None, None, None, None, None, None)

    # Test method run with desired return values
    ret = action.run(tmp, task_vars)
    assert isinstance(ret, dict)

# Generated at 2022-06-13 10:55:29.118602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.plugins.loader import action_loader
    from ansible.module_utils._text import to_bytes

    # from ansible.module_utils._text import to_bytes

    # arguments for __init__ method of class ActionModule
    task = {
        'action': 'shell',
        'args': {
            'arg1': 'value1'
        }
    }
    connection = None
    play_context = None
    loader = basic._AnsiballzLoader()
    templar = None
    shared_loader_obj = action_loader

    # create instance of class ActionModule

# Generated at 2022-06-13 10:55:35.243083
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModule_test:
        def __init__(self, _task):
            self._loader = "loader"
            self._templar = "templar"
            self._share_loader_obj = "loader_obj"
    class ActionBase_test:
        def __init__(self, _task):
            pass
        def run(self, task_vars = None):
            return {'stdout': 'stdout'}
    class Task_test:
        def __init__(self):
            self.args = {'_uses_shell': True}
    class Connection_test:
        def __init__(self, _task):
            pass
    class PlayContext_test:
        def __init__(self):
            self.become = "become"

# Generated at 2022-06-13 10:55:45.415687
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockTemplar(object):
        def __init__(self):
            self.template = 'redhat-release'

    class MockTask(object):
        def __init__(self):
            self.args = { 'a':1, '_uses_shell' : False }

    class MockActionLoader(object):
        def __init__(self):
            pass

        def get(self, name, task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            return render_command

    class MockCommandAction(object):
        def __init__(self):
            pass

        def run(self, task_vars=None):
            return { 'stdout': 'stdout', 'stderr': 'stderr' }

    render_command = Mock

# Generated at 2022-06-13 10:55:45.893039
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:47.286710
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	action_module = ActionModule()
	result = action_module.run()
	assert result['failed'] == True

# Generated at 2022-06-13 10:55:47.784340
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:51.351753
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Imports
    import ansible.plugins.action.shell

    class A():
        pass

    args = {}
    c = A()
    class_name = ansible.plugins.action.shell.ActionModule
    c.run(args)

# Generated at 2022-06-13 10:56:05.802546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest
    from unittest.mock import call, patch, mock_open, Mock

    from ansible import context
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    from ansible.plugins.action.shell import ActionModule as ShellActionModule
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var

    pytestmark = pytest.mark.connection('local')


# Generated at 2022-06-13 10:56:15.216072
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock ansible_module needed for class to instantiate
    ansible_module = ['echo', 'Hello World']

    # setting up the module mock
    module_mock = {}
    module_mock['ANSIBLE_MODULE_ARGS'] = {}
    module_mock['ANSIBLE_MODULE_ARGS']['_raw_params'] = ansible_module[0]

    # setting up the arguments to instantiate the class
    task_vars = {}
    tmp = '/tmp/ansible-tmp-dummy'

    # mock the command action plugin
    class CommandActionPlugin:
        def run(self, task_vars):
            return None

    # setting up the arguments to instantiate the class
    task_args = {}
    task_args['_raw_params'] = ansible_module[0]
    task

# Generated at 2022-06-13 10:56:17.116481
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	tmp = "tmp"
	task_vars = dict()
	action_module = ActionModule(tmp,task_vars)


# Generated at 2022-06-13 10:56:34.493043
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task.args = {'_raw_params': 'ls'}
    print(module._task.args)
    res = module.run()
    assert res['rc'] == 0

# Generated at 2022-06-13 10:56:35.341267
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass

# Generated at 2022-06-13 10:56:42.672959
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import module_loader
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    class ActionBase_SubClass(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return 'the_run_result'

    test_results = [
        'the_run_result',
    ]

    task0 = Task()
    task0.name = 'test_result_0'

    task_list = [
        task0,
    ]


# Generated at 2022-06-13 10:56:49.795523
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# Setup
	from ansible.plugins.action.shell import ActionModule
	from ansible.module_utils.basic import AnsibleModule
	from ansible.module_utils.common.collections import ImmutableDict
	import json
	#from ansible.utils import string_types
	from ansible.errors import AnsibleAction, AnsibleUndefinedVariable
	from tempfile import NamedTemporaryFile
	from ansible.compat.six.moves import configparser
	from ansible.parsing.utils.addresses import parse_address
	import os
	#from ansible.parsing.splitter import parse
	from ansible.playbook.play_context import PlayContext
	from ansible.playbook.task import Task
	from ansible.playbook.block import Block
	from ansible.playbook.role import Role


# Generated at 2022-06-13 10:56:51.345298
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:57:01.030342
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping

    # Mock of AnsibleModule
    class MockAnsibleModule(object):
        def __init__(self, args, **kwargs):
            MockAnsibleModule.args = args
            MockAnsibleModule.kwargs = kwargs

    # Mocks of ActionBase
    class MockActionBase(object):
        def __call__(self, *args, **kwargs):
            return self

        def get_connection(self):
            pass

        def get_loader(self):
            pass

        def get_variable_manager(self):
            pass

        def get_loader(self):
            pass

       

# Generated at 2022-06-13 10:57:13.661579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ is function `run` of class `ActionModule` working correctly? """
    from ansible.plugins.action import ActionBase
    from mock import MagicMock
    from ansible.module_utils.six import PY3
    from ansible.plugins.action.shell import ActionModule
    from ansible.plugins.action.command import ActionModule as CommandActionModule

    # Mock class `Connection` which is a dependency of class `ActionBase`
    mock_connection = MagicMock()

    # Mock class `ShellModule` which is a dependency of class `ActionBase`
    mock_shell_module = MagicMock()

    # Mock class `CommandActionModule` which is a dependency of class `ActionModule`

# Generated at 2022-06-13 10:57:14.273863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:57:24.189999
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    class TestTask:
        def __init__(self, args=None, action=None):
            self.args = args
            self.action = action

    class TestActionBase:
        def __init__(self, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

    class TestActionLoader:
        def __init__(self):
            self._actions = {'ansible.legacy.command': TestActionBase}


# Generated at 2022-06-13 10:57:35.076925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import yaml
    import json


    # We do all the work in our own tmp dir, though this should be the default
    # anyway.
    # This also means we don't need to mock unfrackpath

# Generated at 2022-06-13 10:58:11.675363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create an instance of the class under test
    x = ActionModule()
    # exercise the method under test
    #  x.run()
    return True

# run unit tests

# Generated at 2022-06-13 10:58:20.973452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create and setup a mock object class ActionModule
    test = "test"
    # task_vars=None
    # chdir=None
    # executable=None
    # creates=None
    # removes=None
    # warn=False
    # stdin=None
    # stdin_add_newline=True
    # strip_empty_ends=True
    # shell=None
    # remote_user=None
    # remote_pass=None
    # remote_port=None
    # executable=None
    # environment=None
    # removes=None
    # creates=None
    # chdir=None
    # warn=False

    # ansible/lib/ansible/plugins/action/shell.py
    # L.25 class ActionModule(ActionBase):

# Generated at 2022-06-13 10:58:21.542148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO

# Generated at 2022-06-13 10:58:31.062536
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp=None
    task_vars={}
    self=ActionModule()
    self._task.args={}
    self._task.args['_uses_shell'] = True
    self._task.args['_raw_params'] = 'ls'
    command_action = self._shared_loader_obj.action_loader.get('ansible.legacy.command',
                                                                   task=self._task,
                                                                   connection=self._connection,
                                                                   play_context=self._play_context,
                                                                   loader=self._loader,
                                                                   templar=self._templar,
                                                                   shared_loader_obj=self._shared_loader_obj)
    command_action.run(task_vars=task_vars)

# Generated at 2022-06-13 10:58:32.076566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:34.545477
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule
    action_module = ActionModule(None, None, None, None, None)
    response = action_module.run(None, None)
    assert response['rc'] == 0

# Generated at 2022-06-13 10:58:35.469816
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:49.005110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task = action_module._task
    task.action = 'the-action'
    task.args = {'the-arg': 'the_value'}
    task.run_once = 'the-run-once'

    command_action = MagicMock()
    action_module._shared_loader_obj = Mock()
    action_module._shared_loader_obj.action_loader = Mock()
    action_module._shared_loader_obj.action_loader.get = Mock(return_value=command_action)

    task_vars = dict()

    command_action.run.return_value = dict(changed=True)

    result = action_module.run

# Generated at 2022-06-13 10:58:57.896253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    class fake_ansible_legacy_command():
        class fake_module():
            class FakeSelf:
                def __init__(self):
                    self.args = []

                def run(self, task_vars=None):
                    return 1, 2, 3

        def fake_loader(self, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            return self.fake_module().FakeSelf()


# Generated at 2022-06-13 10:58:58.460302
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:00:12.501972
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    "Unit test for method run of class ActionModule"

    # Initializing ActionModule class object
    # a = ActionModule()

    # cmd = "echo 'Hello World'"
    # a._task.args['_uses_shell'] = True
    # result = a.run(command_action=cmd, task_vars='')
    # assert result == (-1, '', '', 'Hello World')
    return

# Generated at 2022-06-13 11:00:18.680663
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ansible.plugins.action.ActionBase.__bases__ = (object,)
    # task object:
    task = ansible.utils.unsafe_proxy.AnsibleUnsafeText(u'task')
    ansible.plugins.action.ActionBase.task = task
    # shared_loader_obj object:
    shared_loader_obj = ansible.parsing.dataloader.DataLoader()
    ansible.plugins.action.ActionBase.shared_loader_obj = shared_loader_obj
    # Execute run method of class ActionModule
    action_module = ansible.plugins.action.ActionModule(task, shared_loader_obj)
    action_module.run()

# Generated at 2022-06-13 11:00:31.827755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Testing the run method of class ActionModule. """
    import tempfile
    tf1 = ''.join(tempfile.mkstemp()).replace('/', '\\')
    tf2 = ''.join(tempfile.mkstemp()).replace('/', '\\')

# Generated at 2022-06-13 11:00:41.839708
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.legacy_shell
    script_module = ansible.plugins.action.legacy_shell.ActionModule(None, None, None, None)
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    class MockConnection:
        def __init__(self, runner, host=None):
            self.runner = runner

# Generated at 2022-06-13 11:00:47.373225
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append('../')
    #sys.path.append('../../')
    from ansible.plugins import module_loader
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    from ansible.plugins.action.shell import ActionModule
    import pytest


# Generated at 2022-06-13 11:00:55.350240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes

    module_utils_text_to_bytes_mock = Mock()
    module_utils_text_to_bytes_mock.return_value = 'test-command'
    setattr(module_utils_text_to_bytes_mock, '__name__', 'to_bytes')


# Generated at 2022-06-13 11:00:55.848599
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:00:56.681910
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert False

# Generated at 2022-06-13 11:00:57.793747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()

    assert actionModule.run() == None

# Generated at 2022-06-13 11:01:03.353783
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockActionModule(ActionModule):

        def _execute_module(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
            del conn
            del tmp
            del module_name
            del module_args
            del inject
            del complex_args
            del kwargs

            return {'rc': 0, 'stdout': 'stdout'}

    class MockActionBase:
        def __init__(self):
            self.task = Mock()
            self.task.args = {'_ansible_verbosity': 3, '_uses_shell': False}
            self.task.action = 'shell'
            self.task.env = {'PATH': '/usr/bin'}
            self.task.no_log = False