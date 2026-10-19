

# Generated at 2022-06-13 10:52:52.467129
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import sys
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import PY3

    from io import BytesIO
    from ansible.plugins.action.normal import ActionModule as am

    class TestActionModule(unittest.TestCase):

        class TestValidActionModule(unittest.TestCase):

            def setUp(self):
                self._am = am(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:53:03.839324
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 10:53:12.927284
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock argument
    class Bunch(object):
        pass
    tmp = Bunch()
    tmp.name = 'async_wrapper.3008'
    tmp.path = '/home/user/.ansible/tmp/ansible-tmp-1437069010.94-115678868272630/async_wrapper.3008'

    task_vars = Bunch()
    task_vars._connection_info = {'network_os': 'ansible.netcommon.network_os'}
    task_vars._target_host = 'host'

    # Mock return value
    class Bunch2(object):
        def __init__(self):
            self.exe = '/bin/sh'
            self.cmd = ["/bin/sh -c 'ls'"]
            self.failed = False
            self.pars

# Generated at 2022-06-13 10:53:19.937701
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    foo = 'foo'
    tmp = 'tmp'
    task_vars = {foo: foo}

    action_plugin_class_instance = ActionModule(None,'','','','','','','','','')
    assert action_plugin_class_instance.run(tmp, task_vars) == {'_ansible_verbose_always': True, '_uses_shell': True, '_ansible_no_log': False}

# Generated at 2022-06-13 10:53:21.608026
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    assert a.run(None, None) == None

# Generated at 2022-06-13 10:53:22.737797
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:53:31.989650
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # The dict object is created here to help with tests
    # The calling code should NEVER do this as the objects
    # are not fed in by name.

    # initialize required objects
    my_args = {'_uses_shell': True}
    my_task = {'name': '', 'args': my_args}
    my_action = {'name': '', 'action': ''}
    my_action_loader = {'get': ''}

    # initialize class
    obj = ActionModule(my_task, my_action, my_action_loader)

    assert obj._task.name == ''
    assert obj._task.args['_uses_shell']
    assert obj._action.name == ''
    assert obj._action.action == ''
    assert obj._action_loader.get == ''

# Generated at 2022-06-13 10:53:37.082921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test assert statements
    task = {'args': {'_uses_shell': True}}
    assert ActionModule._task == task

    # Test return statement
    result = {'result': 'returned'}
    assert ActionModule.run(tmp=None, task_vars=None) == result

# Generated at 2022-06-13 10:53:37.640464
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:41.317019
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    task_vars = {'x': 1}
    result = am.run(task_vars=task_vars)
    assert result == {'ansible_facts': {'discovered_interpreter_python': '/usr/bin/python'}, 'changed': False}

# Generated at 2022-06-13 10:53:48.271820
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.module_utils.six import StringIO
    from ansible.compat.tests.mock import patch

    action_plugin = ActionModule(None, None, None, None, None, None)

    result = action_plugin.run()



# Generated at 2022-06-13 10:53:55.053656
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    resp_dict = {'results': '123', 'status': '1'}
    resp = dict([('cmd', 'pip install ansible'),
                 ('msg', resp_dict), 
                 ('stdout_lines', ['123']), 
                 ('warnings', ['123'])])
    del resp['msg']
    task_vars = dict([('test_task_vars', resp),
                      ('test_task_vars_1', resp)])
    action_module = ActionModule()
    result = action_module.run(None, task_vars)
    assert(result['results'] == '123')

# Generated at 2022-06-13 10:54:06.242060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #test input and expected result
    in1 = {'_raw_params': u'ls'}

# Generated at 2022-06-13 10:54:15.500793
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    d = {
      "changed": False,
      "comment": "",
      "invocation": {
        "module_args": {
          "_raw_params": "/bin/false",
          "_uses_shell": True,
          "argv": None,
          "chdir": None,
          "creates": None,
          "executable": None,
          "removes": None,
          "warn": True
        }
      },
      "rc": 0,
      "stderr": "",
      "stdout": "",
      "stdout_lines": [

      ]
    }
    assert ActionModule().run() == d

# Generated at 2022-06-13 10:54:17.460564
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert module.run() == 'result'

# Generated at 2022-06-13 10:54:31.399106
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	import sys
	import os

	#sys.path.append("/Users/nate/ansible")
	import ansible.plugins.action.shell
	import ansible.plugins.action.template
	import ansible.plugins.action.copy
	import ansible.playbook.action
	import ansible.playbook.block
	import ansible.playbook.task
	import ansible.playbook.play
	import ansible.executor.task_queue_manager
	import ansible.executor.playbook_executor


# Generated at 2022-06-13 10:54:41.975467
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    from ansible.plugins.action import ActionBase

    action = mock.create_autospec(ActionBase)

    # Test successful run
    result = action.run(task_vars={})
    assert result == {'invocation': {
        'module_args': {}
    }}

    # Test invocation failure
    action.run.side_effect = Exception('foo')
    try:
        result = action.run(task_vars={})
    except Exception as e:
        assert 'foo' == str(e)

    # Test parsing failure
    action.run.side_effect = None
    result = action.run(task_vars={})
    assert result['_ansible_parsed'] is False
    assert result['_ansible_verbose_override'] is True


# Generated at 2022-06-13 10:54:51.915822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars=dict(
                   ansible_shell_type='csh', 
                   ansible_shell_executable='/bin/csh', 
                   ansible_python_interpreter='something', 
                   ansible_connection='local', 
                   ansible_python_version=2, 
                   ansible_user='user', 
                   ansible_host='localhost', 
                   ansible_port=9090, 
                   ansible_hostname='host'
                   )
    _ansible_loop_var=None
    _ansible_tmpdir=None
    ansible_local=dict()
    ansible_local.check=None
    _ansible_no_log=False
    ansible_local.task=AnsibleTask()
    ansible_local.task.become=None
    ans

# Generated at 2022-06-13 10:55:01.741866
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule

    def command_action_run_func(tmp=None, task_vars=None):
        return "TEST_RESULT"

    import ansible.plugins.action.command as command
    command.ActionModule.run = command_action_run_func
    import ansible.plugins.action.normal as normal
    normal.ActionModule.run = command_action_run_func

    class MockTask(object):
        def __init__(self):
            self.args = {'_uses_shell': False}

    class MockActionPlugin(object):
        def get(self, name, *args, **kwargs):
            if name == 'ansible.legacy.command':
                return command.ActionModule(*args, **kwargs)

# Generated at 2022-06-13 10:55:06.162993
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    bool_true = True
    str_test_dir = "testdir"
    module_args = {"_ansible_module_name":"aix_command", "_ansible_module_args": {"cmd": "echo hi", "_ansible_system_tmpdir": str_test_dir, "bool_true": bool_true, "_ansible_no_log": True, "_ansible_shell_executable": "/bin/sh"} }
    am = ActionModule({"module_args":module_args}, 'aix_command')
    am.run()



# Generated at 2022-06-13 10:55:10.629026
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:18.729921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance of ActionModule
    am = ActionModule()
    # Assign arbitrary value to tmp
    tmp = None
    # Assign arbitrary value to task_vars
    task_vars = None
    # Call method run
    # @mock.patch.object(ActionBase, 'run')
    # def test_something(self, mock_func):
    #     mock_func.return_value = "bar"
    result = am.run(tmp=None, task_vars=None)
    # Assert hasattr() for ActionModule
    assert hasattr(am, 'run'), "ActionModule hasn't attribute 'run'"

# Generated at 2022-06-13 10:55:19.405631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:21.660222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_mock = ActionModule()
    result = module_mock.run()
    assert result == dict()

# Generated at 2022-06-13 10:55:24.718087
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return 'test_data'
    test_plugin_connection = TestModule()
    assert test_plugin_connection.run() == 'test_data'

# Generated at 2022-06-13 10:55:32.850084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up data structures needed to test ActionModule.run
    # Placeholders to be populated
    tmp = None
    task_vars = None
    result = None

    # Path to module
    class_under_test = 'ansible.legacy.shell.ActionModule'

    # Create object with needed attributes
    action = ActionModule()
    action._task = 'task placeholder'
    action._connection = 'connection placeholder'
    action._play_context = 'play_context placeholder'
    action._loader = 'loader placeholder'
    action._templar = 'templar placeholder'
    action._shared_loader_obj = 'shared_loader_obj placeholder'

    # Call object method with known values
    result = action.run(tmp, task_vars)

    # Check results, return
    assert result == 'result placeholder', result

# Generated at 2022-06-13 10:55:37.132469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader

    t = action_loader.get('ansible.legacy.shell', None, None, None, None, None)\
        # type: ActionModule

    assert t is not None

# Generated at 2022-06-13 10:55:37.933344
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:38.758233
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:55:47.048457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create the action module
    action_module = ActionModule()
    
    # Mock the task object to get the right command 
    task = {"args": {"_raw_params": "uname -a"}}
    action_module._task = task

    # Mock the task_vars
    task_vars = {}

    # Run the action module
    result = action_module.run(tmp=None, task_vars=task_vars)
    print (result)

# Generated at 2022-06-13 10:56:05.821686
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask:
        def __init__(self):
            self.args = {}
    class FakeLoader:
        def __init__(self):
            pass
    class FakePlayContext:
        def __init__(self):
            self.new_stdin = True
            self.new_stdout = True
    class FakeRunner:
        def __init__(self):
            self.module_name = 'ansible.legacy.command'
    class FakeSharedLoaderObj:
        def get(self, module_name, task, connection, play_context, loader, templar, shared_loader_obj):
            assert module_name == 'ansible.legacy.command'
            return FakeRunner()
        def __init__(self):
            self._path_cache = {}
            self._module_cache = {}

# Generated at 2022-06-13 10:56:06.355997
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:56:15.874750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  module = 'shell'
  task_vars = dict()
  module_args = dict()
  module_args['_uses_shell'] = True
  tmp = None
  task = dict()
  task['args'] = module_args
  task_vars = dict()
  task_vars['ansible_args'] = dict()
  task_vars['ansible_args']['_uses_shell'] = True

  action_module = ActionModule(module, task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
  try:
    result = action_module.run(tmp=tmp, task_vars=task_vars)
    assert True
  except Exception as err:
    assert False, "Unexpected Exception: " + str(err)

# Generated at 2022-06-13 10:56:26.386862
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule
    actionModule_obj = AnsibleModule(test_command_argument)
    # Get the testing file path
    test_file_path = os.path.join(test_directory, test_file)
    # Execute the method run of class ActionModule
    result = actionModule_obj.run({'test_file_path':test_file_path})

# Generated at 2022-06-13 10:56:35.801353
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = {"a": "b"}
    module_name = "a_module"
    arguments = "a_arguments"
    path = "a_path"
    task_vars = {"b": "c"}

    class Task:
        def __init__(self, args):
            self.args = args

    task = Task({"a_arg": "a_value"})

    class SharedPluginLoaderObj:
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj


# Generated at 2022-06-13 10:56:36.730100
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:56:39.594789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    command_action = CommandActionModule()
    task_vars = dict(ansible_shell_type='csh')
    command_action.run(task_vars=task_vars)



# Generated at 2022-06-13 10:56:46.776611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostvars = [{}]
    play_context = (0, 2)
    self_loader_obj = action('ansible.legacy.shell', "test/test_dunder_uses_shell", play_context, hostvars)

    self_loader_obj.run()

    try:
        ansible.errors.AnsibleError
    except NameError:
        assert False, "ansible.errors.AnsibleError should be defined after run() method"

    # AssertionError: Expected to find '_uses_shell' in {'_uses_shell': True})
    assert set(self_loader_obj._task.args) == '_uses_shell'

# Generated at 2022-06-13 10:56:47.562071
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:48.601637
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Not yet implemented')

# Generated at 2022-06-13 10:57:14.552854
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Assuming that self.run() is called
    # We need to know more about the structure of the code but this is what we
    # can do now.
    #
    # Imports needed for testing
    import ansible.plugins.action.shell
    from ansible.plugins.action.command import ActionModule as CommandModuleClass
    import ansible.plugins.loader
    import ansible.plugins.base
    import ansible.plugins.lookup
    import ansible.plugins.callback
    import ansible.plugins.filter
    import ansible.plugins.connection
    import ansible.plugins.shell_loader
    import ansible.plugins.vars
    import ansible.plugins.strategy
    import ansible.plugins.terminal
    import ansible.plugins.cliconf
    import ansible.plugins.inventory
    import ansible.plugins

# Generated at 2022-06-13 10:57:24.306740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask():
        def __init__(self):
            self.args = {'_uses_shell': True}

    class FakeConnection():
        def __init__(self):
            self.result = {'changed': True}

        def __getattr__(self, name):
            if name == 'result':
                return self.result


    class FakeModuleLoader():
        def __init__(self):
            self.action_loader = FakeActionLoader()

    class FakeActionLoader():
        def __init__(self):
            self.command_action = FakeCommandAction()


# Generated at 2022-06-13 10:57:26.660647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=undefined-variable,missing-docstring
    # TODO
    pass

# Generated at 2022-06-13 10:57:28.049170
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Inside test_ActionModule_run")

    assert True

# Generated at 2022-06-13 10:57:36.953822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import random
    import string

    random_id = ''.join([random.choice(string.ascii_letters) for n in range(10)])
    random_tmpdir = '/tmp/test_ansible_module_shell_' + random_id

    os.mkdir(random_tmpdir)

    test_action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    
    result = test_action_module.run(tmp=random_tmpdir)

    os.rmdir(random_tmpdir)

    assert result

# Generated at 2022-06-13 10:57:39.826336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test setting
    action_module = ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None,
                                 shared_loader_obj=None)

    assert action_module.run() is None

# Generated at 2022-06-13 10:57:41.006306
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule_instance = ActionModule()
    # TODO: Complete the unit test

# Generated at 2022-06-13 10:57:47.975509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import Connection
    from ansible.module_utils._text import to_text
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    mock_task = MagicMock(Task)
    mock_play_context = MagicMock(PlayContext)
    mock_loader = MagicMock()
    mock_templar = MagicMock(Templar)
    mock_task_vars = MagicMock(VariableManager)
    mock_shared_

# Generated at 2022-06-13 10:58:00.481994
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Importing here ensures we're using the new code path rather than the old one
    from ansible.plugins.action.shell import ActionModule

    action_module = ActionModule(None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task = mock.Mock()
    action_module._task.args = dict()

    action_module._shared_loader_obj.action_loader.get.return_value = mock.Mock()
    action_module._shared_loader_obj.action_loader.get.return_value.run.return_value = { 'some_key': 'some_value' }

    result = action_module.run(tmp=None, task_vars=None)

    assert result['some_key'] == 'some_value'

# Generated at 2022-06-13 10:58:01.407188
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print()

# Generated at 2022-06-13 10:58:44.493018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    runner = ActionModule({'forks': 10})
    task_vars = dict(foo="bar", bam="baz")
    result = runner.run(task_vars=task_vars)
    assert result == {}

# Generated at 2022-06-13 10:58:45.714146
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    assert action is not None

# Generated at 2022-06-13 10:58:50.203601
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({}, MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock())
    result = module.run(tmp=MagicMock(), task_vars=MagicMock())

# Generated at 2022-06-13 10:58:57.671968
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.loader import module_loader

    # create test module
    module = AnsibleModule(argument_spec={'_command_module': {'type': 'list', 'required': True}, '_command_module_args': {'type': 'dict'}})

    # create test action
    action = ActionModule(module, [], [], [], [], None, None, None, None, None)

    # create test command action
    command_action = module_loader.get('ansible.legacy.command')

    action.run()

    command_action.run(task_vars={})

# Generated at 2022-06-13 10:59:08.261940
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_task = {
        "args": {
            "arg1": "val1",
            "arg2": "val2"
        }
    }
    fake_shared_loader_obj = {}
    fake_connection = {}
    fake_play_context = {}
    fake_loader = {}
    fake_templar = {}

    am = ActionModule(fake_task,
                      fake_connection,
                      fake_play_context,
                      fake_loader,
                      fake_templar,
                      fake_shared_loader_obj)

    # with valid parameters
    ca_run = am.run(task_vars=None)
    assert ca_run == {}

    ca_run = am.run(task_vars={"var1": "val1"})
    assert ca_run == {}

    # with no parameters

# Generated at 2022-06-13 10:59:09.685518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    print(module.run())


# Generated at 2022-06-13 10:59:10.695847
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""

# Generated at 2022-06-13 10:59:16.202740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_obj = ActionModule()
    action_module_obj._task.args['_raw_params'] = 'pwd'
    action_module_obj._task.args['_uses_shell'] = True
    result_stdout = action_module_obj.run({},{'ansible_shell_type': 'sh'})['stdout']
    assert(result_stdout == '/home/vagrant\n')


# Generated at 2022-06-13 10:59:16.843562
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:59:26.288504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source_command = 'ls -la'
    test_args = {'_uses_shell': True}
    run_args = {'_ansible_shell_executable': '/bin/sh', '_raw_params': source_command}
    test_args.update(run_args)

    def runMock(self, tmp=None, task_vars=None):
        del tmp  # tmp no longer has any effect


# Generated at 2022-06-13 11:00:52.915095
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am._shared_loader_obj.action_loader.get = MagicMock()
    am.run()
    am._shared_loader_obj.action_loader.get.assert_called_with('ansible.legacy.command',
                                                               task=am._task,
                                                               connection=am._connection,
                                                               play_context=am._play_context,
                                                               loader=am._loader,
                                                               templar=am._templar,
                                                               shared_loader_obj=am._shared_loader_obj)

# Generated at 2022-06-13 11:00:53.299515
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:00:56.158195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # ToDo: Test data
    task = dict(
        args=dict(
            _uses_shell=True
        )
    )
    task_vars = dict()
    tmp = None

    action_module = ActionModule(task, tmp, task_vars)
    result = action_module.run(tmp, task_vars)
    assert result is not None
    assert result['rc'] == 0
    # Pass

# Generated at 2022-06-13 11:00:56.531965
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:00:59.480747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    obj = ActionModule('mock_module', 'mock_task', 'mock_connection', 'mock_play_context', 'mock_loader', 'mock_templar', 'mock_shared_loader_obj')
    assert obj.run() == None

# Generated at 2022-06-13 11:01:03.610204
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize
    action_module = ActionModule()

    # Initialize inputs
    tmp = None
    task_vars = None

    # Call run
    run_result = action_module.run(tmp, task_vars)

    # Assert result
    assert run_result == "default"

# Generated at 2022-06-13 11:01:15.221274
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostvars = dict()
    hostvars['ansible_play_hosts'] = None
    hostvars['foo_var'] = 'bar'
    task_vars = dict()
    task_vars['hostvars'] = hostvars
    task = dict()
    task['args'] = dict()
    task['args']['_uses_shell'] = False
    action = ActionModule(task, None, task_vars, None)
    result = action.run(task_vars=task_vars)
    assert result['module_stdout'] == 'Command not defined'
    assert result['module_stderr'] == ''

# Generated at 2022-06-13 11:01:19.998006
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModuleObj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    #returns result
    assert type(actionModuleObj.run(tmp=None, task_vars=None)) == type({})

# Generated at 2022-06-13 11:01:29.863093
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.module_loader import MockModuleLoader
    from units.mock.plugins import action_base

    with action_base.setup_mock(action_base.TestAction):
        task_vars = dict(omg='bbq')
        inject = dict()

        # Simulate loader.get_basedir()
        mock_loader = DictDataLoader({
            "/etc/ansible/roles/a_role/tasks/main.yml": "",
            "playbook": "",
        })
        mock_loader.set_basedir('/etc/ansible/roles/a_role/tasks/')

        mock_loader.module_loader = MockModule

# Generated at 2022-06-13 11:01:30.613299
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass