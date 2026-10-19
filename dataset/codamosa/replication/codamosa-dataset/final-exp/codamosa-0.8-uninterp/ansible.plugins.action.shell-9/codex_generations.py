

# Generated at 2022-06-13 10:52:48.019664
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a temporary directory to store the repo
    # This allows us to create files that we need
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)


    result = ActionModule.run(temp_dir)

    # There should exist a file named file_name
    assert(result == 5)

# Generated at 2022-06-13 10:52:48.579892
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:50.291762
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert action_module is not None


# Generated at 2022-06-13 10:52:54.304164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    a = ActionModule(None, None, None, None, None, None)
    assert a.run(tmp=None, task_vars=None) is None

# Generated at 2022-06-13 10:52:55.063236
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 10:53:03.834081
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    _task = dict(action=dict(module_name='shell', module_args=dict()))
    _connection = None
    _play_context = None
    _loader = None
    _templar = None
    _shared_loader_obj = None
    module.run( _task=_task, _connection=_connection, _play_context=_play_context, _loader=_loader,_templar=_templar, _shared_loader_obj=_shared_loader_obj)

# Generated at 2022-06-13 10:53:11.426810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.plugins.action.file import ActionModule
    from ansible.plugins.action.file import ActionModule
    f = ActionModule()
    s = f.run(tmp=None, task_vars=None)
    assert s[0] == 'exists'
    assert s[1] == '/var/lib/jenkins/workspace/ansible/library'
    assert s[2] == 'directory'
    assert s[3] == '0775'
    assert s[4] == 'root'
    assert s[5] == 'tomcat'
    assert s[6] == 'drwxrwsr-x.'

# Generated at 2022-06-13 10:53:24.768419
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:53:26.034992
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # Nothing to test

# Generated at 2022-06-13 10:53:36.209785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Use public functions
    ActionBase.task_vars = task_vars
    ActionBase.load_task_vars = load_task_vars
    ActionBase.set_task_vars = set_task_vars
    ActionBase.noop_task = noop_task
    ActionBase.run = run
    ActionBase._execute_module = _execute_module

    # Use private functions
    ActionBase._execute_module = _execute_module
    ActionBase._add_host_vars = _add_host_vars

    # Use internal functions
    ActionModule.run = run

    # Create an action module object

# Generated at 2022-06-13 10:53:49.185560
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup a mock task object
    task = dict()
    task['args'] = dict()
    task['args']['_uses_shell'] = True

    # Setup a mock connection object
    connection = dict()

    # Setup a mock play_context object
    play_context = dict()

    # Setup a mock loader object
    loader = dict()

    # Setup a mock templar object
    templar = dict()

    # Setup a mock shared_loader_obj object
    shared_loader_obj = dict()

    # Setup a mock command_action object
    command_action = dict()
    command_action['run'] = lambda task_vars: 'ran'

    # Setup a mock shared_loader_obj object
    shared_loader_obj['action_loader'] = dict()

# Generated at 2022-06-13 10:53:54.444840
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockArgs(object):
        _uses_shell = False

    class MockTask(object):
        args = MockArgs()

    class MockPlayContext(object):
        def __init__(self):
            self.become = True
            self.become_user = "root"

    class MockAnsibleModule(object):
        def __init__(self):
            self._task = MockTask()
            self._play_context = MockPlayContext()

    action = ActionModule(MockAnsibleModule())
    result = action.run(None, None)
    assert result == True

# Generated at 2022-06-13 10:53:54.858874
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:06.089490
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Assume the following have been defined as class variables
    ActionBase._task = ActionBase.task
    ActionBase._connection = ActionBase.connection
    ActionBase._play_context = ActionBase.play_context
    ActionBase._loader = ActionBase.loader
    ActionBase._templar = ActionBase.templar
    ActionBase._shared_loader_obj = ActionBase.shared_loader_obj

    #Run method
    ActionModule.run()

    #Asserts 
    assert ActionModule._task == ActionBase.task
    assert ActionModule._connection == ActionBase.connection
    assert ActionModule._play_context == ActionBase.play_context
    assert ActionModule._loader == ActionBase.loader
    assert ActionModule._templar == ActionBase.templar
    assert ActionModule._shared_loader_obj == ActionBase.shared_loader

# Generated at 2022-06-13 10:54:14.353346
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Mock object for ansible.plugins.action.ActionBase.run"""

    from ansible.plugins.action.action_module_test_module import ActionModuleTest

    # Create mock object for class ActionBaseTest
    action_basetest_obj = ActionModuleTest()

    # Start call of method run
    result = action_basetest_obj.run(tmp='test_tmp')

    # Assert result of method run
    assert action_basetest_obj._task.args['_uses_shell'] == True

# Generated at 2022-06-13 10:54:28.319513
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test run method of class ActionModule
    """
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    # Create mock task
    mock_task = namedtuple("MockTask", "args")
    args = {"cmd": "command_name", "shell": "/bin/sh -c", "executable": "/tmp/shell"}
    mock_task.args = args

    # Create mock module
    mock_module_args = {"test": "test"}
    mock_module = AnsibleModule(argument_spec=mock_module_args)

    # Create mock action base
    action_base = ActionBase(mock_task, mock_module_args, mock_module)

# Generated at 2022-06-13 10:54:38.093062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = "localhost"
    ansible_python_interpreter = "/usr/bin/python"
    task_args = {'_uses_shell':True}
    task_action = 'shell'
    ActionBaseClass = ActionBase
    command_action_class = ActionBase
    task_vars = {}
    self = ActionModule(host, ansible_python_interpreter, task_args, task_action, ActionBaseClass, command_action_class)
    tmp = None
    result = self.run(tmp, task_vars)
    print(result)


# call unit test
if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:46.137308
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class ActionModule_run(ActionModule):
        def __init__(self, *args, **kwargs):
            super(ActionModule_run, self).__init__(*args, **kwargs)
            self.arguments_used = ''
            self.returned_value = ''

        def run(self, *args, **kwargs):
            self.arguments_used = args
            self.returned_value = super(ActionModule_run, self).run(*args, **kwargs)
            return self.returned_value

    """
    Required arguments:
        - '_uses_shell' in task.args: True
    """

# Generated at 2022-06-13 10:54:46.718433
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:57.830369
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from ansible.module_utils._text import to_text
    from ansible.plugins.action.shell import ActionModule
    from ansible.playbook.play_context import PlayContext

    a1 = ActionModule(
        task=dict(action='shell', args={'_uses_shell': True}, charset='ascii'),
        connection=None,
        play_context=PlayContext(become_user='test_user', become_method='test_method'),
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )


# Generated at 2022-06-13 10:55:02.798222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:11.159744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins
    import ansible.plugins.action
    import ansible.plugins.action.shell
    import ansible.plugins.connection.local
    from ansible.utils.vars import merge_hash
    from ansible.template import Templar
    from ansible.module_utils.six import StringIO
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.color import stringc

# Generated at 2022-06-13 10:55:11.787604
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:14.689394
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_obj = ActionModule()
    module_obj._shared_loader_obj.action_loader.get('ansible.legacy.command').run()

# Generated at 2022-06-13 10:55:15.279205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:23.664557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None)
    module._task.args['command'] = 'ls'
    module._templar.template.side_effect = lambda command: command.replace('{{', '').replace('}}', '')
    module._shared_loader_obj.action_loader.get.return_value.run.return_value = 'done'
    assert module.run(task_vars=['ansible_check_mode']) == 'done'
    module._shared_loader_obj.action_loader.get.return_value.run.assert_called_with(task_vars={'ansible_check_mode': 'yes'})



# Generated at 2022-06-13 10:55:31.499708
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Scenario 1: action_module is executed with value _uses_shell=True
    # Expected output: action_module will execute command_action with value _uses_shell=True
    _task = {'args': {'_uses_shell': False}}
    x = ActionModule(task=_task)
    result = x.run()
    assert result['_uses_shell']

    # Scenario 2: action_module is executed with value _uses_shell=False
    # Expected output: action_module will execute command_action with value _uses_shell=False
    _task = {'args': {'_uses_shell': False}}
    x = ActionModule(task=_task)
    result = x.run()
    assert not result['_uses_shell']

# Generated at 2022-06-13 10:55:32.697065
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TBD: test code for run
    return 0

# Generated at 2022-06-13 10:55:46.571195
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Read input data
    data = read_data_file(0)

    # Read expected result
    expected_result = read_result_file(0)

    # Load arguments into the task object
    _task = Task(data['args'])

    # Load arguments into the task_vars object
    _task_vars = TaskVars(data['task_vars'])

    # Load arguments into the action module object
    _action_module = ActionModule(_task, _task_vars)

    # Calculate result
    result = _action_module.run(_task_vars)

    # Set expected result type
    expected_result['changed'] = bool(expected_result['changed'])
    expected_result['skipped'] = bool(expected_result['skipped'])

    # Assertion
    assert result == expected_result

# Generated at 2022-06-13 10:55:47.071782
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	pass

# Generated at 2022-06-13 10:55:55.086491
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:56:06.148366
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import shlex
    import unittest
    import unittest.mock as mock
    sys.modules['ansible'] = mock.Mock()
    sys.modules['ansible.plugins'] = mock.Mock()
    sys.modules['ansible.plugins.action'] = mock.Mock()
    sys.modules['ansible.plugins.action.normal'] = mock.Mock()
    from ansible.plugins.action.normal import ActionModule as am
    from ansible.module_utils._text import to_bytes

    # Create a mock for the class Connection and pass the mock to the
    # ActionModule to be utilized during the unit test. The mock will
    # allow us to specify a return value when checking connection
    # type.

# Generated at 2022-06-13 10:56:06.664860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:56:07.497452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:16.634133
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader

    class connection_class:
        def __init__(self):
            self.host = ''
            self.port = 0
            self.user = ''
            self.passwd = ''
            self.private_key_file = ''
            self.connection = ''
            self.remote_usr = ''
            self.remote_pass = ''
            self.transport = ''

    # Connection loader is mocked to return 'connection_class', which
    # is defined locally above
    def connection_loader_function(self):
        return connection_class

    connection_loader.get = connection_loader_function

    # Action loader is mocked to return 'action_class', which is also
   

# Generated at 2022-06-13 10:56:17.157657
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:18.635421
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    pass

# Generated at 2022-06-13 10:56:22.730044
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_file = "../test/unit_test_data/test_ActionModule_run.json"
    test_ActionModule = ActionModule()
    result = test_ActionModule.run(tmp=None, task_vars=None)
    assert result == "echo hello"

# Generated at 2022-06-13 10:56:32.070426
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # replacement of mock.patch is to follow python patch
    # https://www.python.org/dev/peps/pep-0478/
    from unittest.mock import patch
    from ansible.module_utils._text import to_bytes

    # create patch for __init__ of class ActionBase
    with patch.object(ActionBase, '__init__') as mock_init:

        # instantiating action_module
        action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                                     shared_loader_obj=None)

        # testing __init__
        mock_init.assert_called_with(task=None, connection=None, play_context=None, loader=None, templar=None,
                                     shared_loader_obj=None)

# Generated at 2022-06-13 10:56:33.593158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test method run of class ActionModule"""
    
    pass

# Generated at 2022-06-13 10:56:49.014704
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  result = _ActionModule_run()
  print(str(result))


# Generated at 2022-06-13 10:56:49.488653
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:00.149984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define test setup
    # TODO: name of test???
    # Define test setup
    module_name = 'ansible.legacy.shell'
    # TODO: command_string
    command_string = 'command_string'
    # TODO: data
    data = 'data'
    # TODO: _uses_shell
    _uses_shell = '_uses_shell'
    # TODO: action_loader
    action_loader = 'action_loader'
    # TODO: task_vars
    task_vars = 'task_vars'
    # TODO: _task
    _task = '_task'
    # TODO: _connection
    _connection = '_connection'
    # TODO: _play_context
    _play_context = '_play_context'
    # TOD

# Generated at 2022-06-13 10:57:13.301604
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import sys
    import os
    import yaml
    from ansible.module_utils.six import PY3
    if not PY3:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins  # pylint: disable=import-error

    # pylint: disable=unused-variable,too-many-instance-attributes
    class FakeActionModule(object):
        _templar = None
        _shared_loader_obj = None
        _task = None
        _connection = None
        _loader = None
        _play_context = None


# Generated at 2022-06-13 10:57:18.802891
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # None is an invalid arg
    with pytest.raises(TypeError) as ex:
        ActionModule(None)
    assert "argument 1 must be an action plugin" in str(ex.value)

    # "tmp" is an invalid arg
    with pytest.raises(TypeError) as ex:
        ActionModule("tmp")
    assert "argument 1 must be an action plugin" in str(ex.value)

# Generated at 2022-06-13 10:57:26.852778
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import string_types
    from ansible.plugins.action import _low_level_execute_command
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 10:57:36.954038
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task.args['_uses_shell'] = True
    action_module._task.args['_raw_params'] = 'pwd'
    action_module._task.args['_uses_delegate_to'] = False
    action_module._task.args['_ansible_no_log'] = False
    action_module._task.args['_ansible_verbosity'] = 0
    action_module._task.args['_ansible_version'] = '2.8.2'
    action_module._task.args['_ansible_syslog_facility'] = 'LOG_USER'

# Generated at 2022-06-13 10:57:44.496888
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.legacy.action
    import ansible.legacy.command
    import ansible.legacy.task
    import ansible.script.action
    import ansible.utils.vars

    com_action = ansible.legacy.action.ActionModule(
        ansible.legacy.task.Task(
            ansible.script.action.VariableManager(
                loader=ansible.utils.vars.AnsiLoader(),
                host_options=None,
                task_options=None,
                shared_loader_obj=ansible.utils.vars.AnsiLoader()
            ),
            connection=ansible.legacy.command.Connection(None),
            play_context=None
        )
    )

    assert com_action.run() == {'failed': True, 'msg': 'invalid action'}

# Generated at 2022-06-13 10:57:56.039687
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action import ActionBase

    class ActionModule(ActionBase):

        def run(self, tmp=None, task_vars=None):
            del tmp  # tmp no longer has any effect

            # Shell module is implemented via command with a special arg
            self._task.args['_uses_shell'] = True

            command_action = self._shared_loader_obj.action_loader.get('ansible.legacy.command',
                                                                       task=self._task,
                                                                       connection=self._connection,
                                                                       play_context=self._play_context,
                                                                       loader=self._loader,
                                                                       templar=self._templar,
                                                                       shared_loader_obj=self._shared_loader_obj)

# Generated at 2022-06-13 10:58:04.531952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import StringIO
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import become_loader
    from ansible.plugins.loader import terminal_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    import json
    import mock
    import os


# Generated at 2022-06-13 10:58:49.382511
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'localhost'
    task_vars = dict(ansible_forks=5)
    tmp = '/tmp/ansible-tmp-1486963917.63-147729857856000'
    task = dict(action=dict(module_name='shell', module_args='date', _uses_shell=True), name='Test shell unit test')
    play_context = dict(remote_addr=host)

    # Creates a generic ansible templar instance
    templar = Templar()

    # Creates a temporary empty connection plugin
    class ConnectionPlugin():
        def __init__(self, play_context, new_stdin, *args, **kwargs):
            del args, kwargs
            self._play_context = play_context
            self._new_stdin = new_stdin


# Generated at 2022-06-13 10:58:57.149215
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    host = Host('testhost')
    task = Task()
    task.name = 'test'
    task._role = None
    task._block = None
    task._parent = None
    task._action = 'ping'

    shell = ActionModule(host, task, None, None)
    result = shell.run()
    assert result.is_skipped() == False
    assert result._result.get('skipped') == False
    assert result._result.get('changed') == False
    assert isinstance(result, TaskResult)

# Generated at 2022-06-13 10:59:00.909686
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    test_action = ActionModule(None, None, loader=None, templar=None, shared_loader_obj=None)

    assert("result" in test_action.run(tmp=None, task_vars=None).keys())

# Generated at 2022-06-13 10:59:10.180955
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    original_string = 'ansible.legacy.shell'
    expected_result_string = 'ansible.legacy.command'
    # Creating an object for testing
    action_module_obj = ActionModule(original_string, original_string, original_string)
    # Creating an object of the class which is being referenced by the method
    command_action_obj = ansible.plugins.action.ActionBase(expected_result_string, expected_result_string, expected_result_string)
    with mock.patch.object(ActionModule, '_shared_loader_obj') as MockClass:
        instance = MockClass.return_value
        instance.action_loader.get.return_value = command_action_obj
        actual_result_string = action_module_obj.run()

# Generated at 2022-06-13 10:59:19.968414
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.cli import CLI
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block

    # setup test variables
    cli = CLI()
    cli._options = ImmutableDict()
    options = cli.options
    options.connection = 'local'
    options.module_path = None
    options.forks = 1
    options.become = False
    options.become_method = None
    options.become_user = None
    options.private_key_file = None
    options.check = False
    options.syntax = False
    options.diff = False

# Generated at 2022-06-13 10:59:25.406375
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create object instance "am" that provides the run() method
    am = ActionModule()

    # fake object instances required by method "run"
    am._task = {
        'args': {}
    }
    am._shared_loader_obj = {
        'action_loader': {
            'get': ActionModule.run
        }
    }

    # run method with fake values
    result = am.run()

    # check outcome
    assert result == None

# Generated at 2022-06-13 10:59:34.461033
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # unit test for method run of class ActionModule
    # pylint: disable=undefined-variable
    am = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    # pylint: enable=undefined-variable
    task_vars = dict()
    assert am.run(task_vars=task_vars)

# Generated at 2022-06-13 10:59:36.359202
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:59:44.786075
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.task import Task


# Generated at 2022-06-13 10:59:54.578278
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.shell as shell
    import ansible.plugins.action.command as command
    import ansible.playbook.play_context as play_context
    import ansible.executor.task_result as task_result

    # Unused arguments
    tmp = None
    task_vars = {}
    args = {}
    # Same as module_name in meta/main.yml
    module_name = 'shell'


# Generated at 2022-06-13 11:01:32.031991
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    destruct_module = {'args': {'chdir': '/tmp', 'creates': '/root/.ssh/id_rsa', 'executable': None, 'removes':
                                '/root/.ssh/id_rsa', 'warn': True}, 'module': 'shell'}

    from ansible.vars.reserved import DEFAULT_VAULES
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.common.text.formatters import Jinja2TextFormatter
    from ansible.playbook.play import Play
    from ansible.playbook import PlayContext
    from ansible.playbook.task import Task

# Generated at 2022-06-13 11:01:32.594238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:37.726833
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    tmp = None
    task_vars = None

    # Load fixture data
    self = __import__('ansible.plugins.action.shell', fromlist=['ActionModule'])

    action_module = ActionModule()

    # Test executes successfully
    result = action_module.run(tmp, task_vars)
    assert result['failed'] == False
    # Test fails
    result = action_module.run()
    assert result['failed'] == True

# Generated at 2022-06-13 11:01:39.646269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("ActionModule_run")

    # Test for ActionModule class
    action_module_test = ActionModule()
    action_module_test.run()

# Generated at 2022-06-13 11:01:43.654617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule("/test/test_action.py", "ansible.legacy.shell", "test", "test")

    # unit test for return type of method run of class ActionModule
    assert isinstance(a.run("test", "test"), dict)

# Generated at 2022-06-13 11:01:45.246590
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert 1
    # TODO - write a unit test for method run of class ActionModule

# Generated at 2022-06-13 11:01:54.269399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_self = Mock()
    m_self._task.args = {'_uses_shell': False, 'a': 'b'}
    m_self._shared_loader_obj.action_loader.get.return_value.run.return_value = {'a': 'b'}

    assert ActionModule.run(m_self) == {'a': 'b'}

    m_self._shared_loader_obj.action_loader.get.assert_called_once_with(
        'ansible.legacy.command', task=m_self._task, connection=m_self._connection,
        play_context=m_self._play_context, loader=m_self._loader, templar=m_self._templar,
        shared_loader_obj=m_self._shared_loader_obj)
    assert m

# Generated at 2022-06-13 11:02:03.799284
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO

    # Create a fake stdout
    stdout = StringIO()

    # Create a fake ActionModule instance
    class FakeActionModule(ActionModule):
        def run(self, *args, **kwargs):
            self._stdout = stdout
            self.run = None
            return super(FakeActionModule, self).run(*args, **kwargs)

    # Create a fake task

# Generated at 2022-06-13 11:02:12.728324
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:02:14.344655
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ""

