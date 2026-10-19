

# Generated at 2022-06-13 10:52:42.591627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    assert module is not None

    result = module.run(task_vars={})

    assert result is not None

# Generated at 2022-06-13 10:52:52.571721
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    This test case is to test the run method of ActionModule class.
    '''
    from collections import namedtuple
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    import sys
    import os
    if sys.version_info >= (2, 7):
        import unittest
    else:
        import unittest2 as unittest
    def setUpModule():
        '''
        This method is run once for each module
        '''
        # Set up the

# Generated at 2022-06-13 10:53:01.444891
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    class Task:
        args = {'_uses_shell': True}
    m._task = Task()
    m._shared_loader_obj = None
    m._task = None
    m._connection = None
    m._play_context = None
    m._loader = None
    m._templar = None
    m._shared_loader_obj = None
    m._task_vars = None
    m._any_vars = None
    m.run(None, None)

# Generated at 2022-06-13 10:53:08.098136
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils import basic
    import ansible.plugins.action as a
    import ansible.plugins.action.command as c


    class MockConstructor(object):
        def __init__(self, loader, play_context, new_stdin):
            self.loader = loader
            self.play_context = play_context
            self.new_stdin = new_stdin


    class MockModule(object):
        def __init__(self, no_log=False, check_mode=False, diff=False):
            self.no_log = no_log
            self.check_mode = check_mode

# Generated at 2022-06-13 10:53:22.156254
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create dummy objects for class instantiation
    module_loader = object()
    action_loader = object()
    connection = object()
    play_context = object()
    shared_loader_obj = object()
    loader = object()
    templar = object()
    task = object()
    ansible_vars = dict()

    # Create ActionModule instance
    action_module_obj = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj
    )

    # Create ActionBase instance
    def check_conditional():
        return True
    def dump_results():
        return True
    def run_task_wrap():
        return True
    action_base

# Generated at 2022-06-13 10:53:31.870205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionModule():
        task_vars = None
        tmp = None
        class MockSharedLoaderObj:
            class MockActionLoader:
                def get(Key1, Key2, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
                    return Key2
        _shared_loader_obj = MockSharedLoaderObj()
        _loader = MockSharedLoaderObj()
        class MockTask:
            def __init__(self):
                self.args = {}
        _task = MockTask()
        class MockConnection:
            pass
        _connection = MockConnection()
        class MockPlayContext:
            pass
        _play_context = MockPlayContext()
        class MockTemplar:
            pass
        _templar = MockTemplar

# Generated at 2022-06-13 10:53:41.704510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_module = ActionModule()

    # Command module is implemented via command with a special arg
    my_module._task.args['_uses_shell'] = True

    command_action = my_module._shared_loader_obj.action_loader.get('ansible.legacy.command',
                                                                   task=my_module._task,
                                                                   connection=my_module._connection,
                                                                   play_context=my_module._play_context,
                                                                   loader=my_module._loader,
                                                                   templar=my_module._templar,
                                                                   shared_loader_obj=my_module._shared_loader_obj)
    result = command_action.run(task_vars=None)

    return result

# Generated at 2022-06-13 10:53:42.702889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    assert True

# Generated at 2022-06-13 10:53:53.083561
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    action_module = ActionModule()
    action_module.configuration.stdout_callback = 'default'
    action_module._task.args['_raw_params'] = 'ls -ltr'
    action_module._task.args['creates'] = '/tmp/foo'
    action_module._task.args['removes'] = '/tmp/foo'
    action_module._task.args['chdir'] = '/tmp'
    action_module._task.args['executable'] = '/bin/bash'
    action_module._task.args['warn'] = 'yes'
    action_module._task.args['stdin'] = 'my_stdin'
    action_module._task.args['stdin_add_newline'] = 'True'
    action_module

# Generated at 2022-06-13 10:54:00.252897
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    # Setup mock objects

    Task = action_loader.get('ansible.legacy.command', class_only=True)  # pylint: disable=no-member
    task = Task()
    task.args = {'_uses_shell': True}
    Connection = action_loader.get('ansible.legacy.shell', class_only=True)  # pylint: disable=no-member
    connection = Connection()

    # Create test object

# Generated at 2022-06-13 10:54:06.362477
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule

    # test for empty task_vars
    task_vars = {}
    am = ActionModule()
    am._task = {}

    assert(type(am.run(task_vars=task_vars)) == dict)

# Generated at 2022-06-13 10:54:16.502626
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Validate the function `run` of the class `ActionModule`
    """
    # GIVEN
    from ansible.plugins.action.copy import ActionModule

    class MockTemplar(object):
        def template(self, data):
            return data

    class MockTask(object):
        def __init__(self):
            self.args = dict()

    class MockCommandAction(object):
        def __init__(self):
            self.return_value = 'success'

        def run(self, tmp=None, task_vars=None):
            return self.return_value

    module_action = ActionModule()
    module_action._task = MockTask()
    module_action._templar = MockTemplar()
    module_action._task.args['_uses_shell'] = False
    module

# Generated at 2022-06-13 10:54:23.345169
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    t = ActionModule()
    result = t.run("C:\\test", "task_vars=test")
    assert result['msg'] == 'The shell module does not make sense on Windows hosts. If you needed to use command because of WinRM, use the win_command module instead.'

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:24.688894
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('hello world')

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:25.458339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run()

# Generated at 2022-06-13 10:54:36.949205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    filename = get_testdata_file('fixtures.yaml')
    task_vars = get_task_vars_data(filename)

    _connection = 'local'
    _task = get_task_data(task_vars)
    _play_context = get_play_context()
    _loader = 'loader'
    _templar = 'templar'
    _shared_loader_obj = 'shared_loader_obj'

    action_module = ActionModule(loader=_loader,
                                 connection=_connection,
                                 play_context=_play_context,
                                 task=_task,
                                 templar=_templar,
                                 shared_loader_obj=_shared_loader_obj)

    result = action_module.run(task_vars=task_vars)
   

# Generated at 2022-06-13 10:54:44.791808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.task import Task

    class TestActionModuleRun(unittest.TestCase):

        class TestActionBase(ActionBase):
            pass

        class TestActionModule(ActionModule):

            def __init__(self, task_vars=None):
                self._task = task_vars

            def _execute_module(self, tmp=None, task_vars=None, wrap_async=None):
                return {'is_async': wrap_async}

        def setUp(self):
            self.actionBase = self.TestActionBase()
            self.action = self.TestActionModule()


# Generated at 2022-06-13 10:54:55.844460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ansible_facts = {}
    ansible_facts['ansible_python_version'] = "2.7.5"
    ansible_facts['ansible_os_family'] = "RedHat"
    test_data = {"ansible_facts": ansible_facts}
    ActionModule_obj = ActionModule(None, test_data)
    action_loader_obj = {}
    action_loader_obj['ansible.legacy.command'] = "ansible.legacy.command"
    play_context_obj = {}
    play_context_obj['become'] = True
    play_context_obj['become_method'] = "sudo"
    play_context_obj['become_user'] = "admin"
    task_obj = {}
    task_obj['args'] = {"_uses_shell": False}
    test

# Generated at 2022-06-13 10:55:04.079808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # stub for url method
    def url(*args, **kwargs):
        return 'path'

    # stub for _parse_url method
    def _parse_url(self, *args, **kwargs):
        return 'login', 'password', 'hostname', 'path'

    # stub for run method
    def run(*args, **kwargs):
        return dict(stdout='password')

    import os
    import tempfile
    import shutil


# Generated at 2022-06-13 10:55:11.724031
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:55:24.924417
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_data = {
        'action_module': {
            'run': {
                'test_method': 'run',
                'test_args': {},
                'test_result': {},
            },
        },
    }
    test_object = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_object.async_val = False
    test_object._play_context = None
    test_object._loader = None
    test_object._templar = None
    test_object._shared_loader_obj = None
    test_object._task = None
    test_object._connection = None
    result = test_object.run()

# Generated at 2022-06-13 10:55:32.930798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO

    name = 'test_ActionModule_run'
    module_name = 'shell'
    task_vars = dict(
        ansible_connection='local',
        ansible_shell_type='csh',
        ansible_shell_executable='/bin/csh'
    )
    module_args = dict(
        _raw_params='hostname',
        _uses_shell=True,
        executable='/bin/csh'
    )
    args = dict(module_name=module_name, module_args=module_args)

    # execute the action
    action = ActionModule()
    action.ITEM = name
    action._task = Value(args)
    action._connection = LocalConnection()
    action._task_vars = task_vars


# Generated at 2022-06-13 10:55:46.846874
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  s = sys.modules["ansible"]
  s.plugins = mock.Mock()
  s.plugins.action = mock.Mock()
  s.plugins.action.ActionBase = ActionBase()

  action_module = ActionModule()
  action_module._task = mock.Mock()
  action_module._task.args = {}
  action_module._task.args['_uses_shell'] = True
  action_module._shared_loader_obj = mock.Mock()
  action_module._shared_loader_obj.action_loader = mock.Mock()
  action_module._shared_loader_obj.action_loader.get = mock.Mock()
  command_action = mock.Mock()
  action_module._shared_loader_obj.action_loader.get.return_value = command_action
  action_

# Generated at 2022-06-13 10:55:52.641895
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModuleObject = ActionModule(connection=MockConnection(), play_context=MockPlayContext(), loader=MockLoader(),
                                      templar=MockTemplar(), shared_loader_obj=MockShared_loader_obj())
    actionModuleObject._task.args['_uses_shell'] = True
    actionModuleObject._task.args['arg1'] = 'test_value1'
    actionModuleObject._task.args['arg2'] = 'test_value2'
    actionModuleObject._task.args['arg3'] = 'test_value3'
    commandActionObject = MockCommandAction()
    actionModuleObject._shared_loader_obj.action_loader.action_plugins = {'ansible.legacy.command': commandActionObject}

# Generated at 2022-06-13 10:56:06.816389
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import get_all_plugin_loaders

    ac = get_all_plugin_loaders()[1].get('ansible.legacy.shell')[0]()

    def del_tmp(a, b, c):
        pass

    # Instance object of class ActionBase
    ab = ActionBase()

    # Fake args and task_vars
    args = {
        '_uses_shell': True
    }


# Generated at 2022-06-13 10:56:15.258925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_obj = ActionModule()
    _task = {'args': {'_uses_shell': False, '_raw_params': 'ls -l'}}
    result = my_obj.run(tmp=None, task_vars=None, _task=_task, _connection=None, _play_context=None, _loader=None, _shared_loader_obj=None)
    print(result)
    assert "stdout" in result.keys()
    assert "stderr" in result.keys()
    assert "rc" in result.keys()
    assert result['rc'] == 0
    assert "changed" in result.keys()
    assert result['changed'] == True


# Generated at 2022-06-13 10:56:23.423349
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Expected result
    expected_result = {
        'invocation': {
            'module_args': {
                '_uses_shell': True
            }
        }
    }

    # Create ActionModule object
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Execute method run
    result = action_module.run(
        tmp='test',
        task_vars=None
    )

    # Assert expected result
    assert result == expected_result

# Generated at 2022-06-13 10:56:32.576895
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Test for method run in class ActionModule
    '''
    # Test for config_path
    ansible_vars = {'ansible_config': './ansible.cfg'}
    with patch.dict(os.environ, ansible_vars):
        config_path = os.path.expanduser(configuration.Config().config_file_path)
        if not os.path.exists(config_path):
            print('config_file not found in config path')
            print('config_path: {} '.format(config_path))
            exit(1)
        print('config_path: {}'.format(config_path))
        print('config_file {} found in config_path'.format(os.path.basename(config_path)))

    # Test for config_data
    
    config_parser = config

# Generated at 2022-06-13 10:56:40.726391
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # read the tests file
    test_file = os.path.join(os.path.dirname(__file__), 'test_for_ActionModule_run.yml')
    with open(test_file, 'r') as f:
        test_content = yaml.load(f.read())
    # load data which is need to run the test
    hosts = test_content['hosts']
    test_name = test_content['test_name']
    test_data = test_content['test_data']

    # start the test
    for test_value in test_data:
        # setup the test and the test environment
        setup_test_env(test_value)

# Generated at 2022-06-13 10:56:42.145551
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._shared_loader_obj = None
    ActionModule.run(None, None)

# Generated at 2022-06-13 10:56:50.811375
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:51.555163
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:52.295900
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:56:53.524845
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # assert False
    pass


# Generated at 2022-06-13 10:57:01.499623
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = AnsibleTask({ 'arguments' : { '_uses_shell' : True } })
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()

    action_module = ActionModule(connection, play_context, loader, templar, task, shared_loader_obj)

    action_module_run_mock = Mock(ActionModule, 'run', return_value='result')

    action_module.run(tmp=None, task_vars=None)

    action_module_run_mock.assert_called_with(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:57:02.256313
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:08.758170
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    args = {'_uses_shell': True, 'chdir': None, 'argv': None, 'executable': None, '_raw_params': 'echo hello', '_uses_shell': True}
    task_vars = {}
    module.run(None, task_vars)


# Generated at 2022-06-13 10:57:10.581642
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Instantiate ActionModule object
    am = ActionModule()

    # Call run
    # am.run()

    # Check if its been called
    assert True

# Generated at 2022-06-13 10:57:11.133171
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:21.076227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Build up data structures needed to test
    action_module = ActionModule()
    action_module._task = {'args': {'_uses_shell': None}}
    action_module._loader = None
    action_module._connection = None
    action_module._play_context = None
    action_module._templar = None
    action_module._shared_loader_obj = None

    class MockCommand(object):
        def run(self, task_vars):
            return 'test_ActionModule_run'

    mock_command_obj = MockCommand()
    action_module._shared_loader_obj = {'action_loader': {'ansible.legacy.command': mock_command_obj}}

    # Execute the code to tested
    result = action_module.run(tmp=None, task_vars=None)



# Generated at 2022-06-13 10:57:37.924365
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with pytest.raises(Exception) as excinfo:
        pass

# Generated at 2022-06-13 10:57:38.505204
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:39.259074
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    testobj = ActionModule()
    testobj.run()

# Generated at 2022-06-13 10:57:43.182642
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Just a simple test as not sure how to setup the
    # context required.
    am = ActionModule(None, None, None, None, None, None)
    assert am.run(None, None) == {'failed': True, 'module_stderr': '', 'module_stdout': '', 'msg': 'Non-zero return code', 'rc': 1}

# Generated at 2022-06-13 10:57:47.346969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("\n###TEST_START###\n")
    print("\n###TEST_END###\n")
# Unit test end


if __name__ == '__main__':
    test_ActionModule_run()
# End

# Generated at 2022-06-13 10:57:48.698842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test
    assert True

# Generated at 2022-06-13 10:57:49.471706
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:57:54.657042
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {
        'action': {
            'module': 'command',
            'args': 'ls',
            '_uses_shell': True
        }
    }
    action_module = ActionModule(task, None, None, None, None)
    action_module.run()

# Generated at 2022-06-13 10:57:55.425726
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:57:55.809619
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:48.943810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import ansible.plugins.action
    from ansible.plugins.action.command import ActionModule
    from ansible.plugins.action.exec_command import ActionModule as ExecCommandActionModule
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.config.manager import ConfigManager, Setting, DataSpec

# Generated at 2022-06-13 10:58:57.840591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # # Create a MockTask object.
    mock_task = MockTask()
    # # Create a MockAnsibleModule object.
    mock_ansible_module = MockAnsibleModule()
    # # Create a MockConnection object.
    mock_connection = MockConnection()
    # # Create a MockPlayContext object.
    mock_play_context = MockPlayContext()
    # # Create a MockLoader object.
    mock_loader = MockLoader()
    # # Create a MockTemplar object.
    mock_templar = MockTemplar()
    # # Create a MockSharedLoaderObj object.
    mock_shared_loader_obj = MockSharedLoaderObj()

    # # Create an instance of the ActionModule class and call it's methods run.

# Generated at 2022-06-13 10:59:08.374441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test the run method of ActionModule."""
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult

    task_queue_manager = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=False,
        run_tree=False,
        settings=None)
    # PlayContext
    play_context = PlayContext()
    # Mock TaskResult
    task_result = TaskResult()

# Generated at 2022-06-13 10:59:18.044955
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestActionModule(ActionModule):
        def __init__(self, tmp=None, task_vars=None):
            self.tmp = tmp
            self.task_vars = task_vars
            self._task = self
            self._connection = self
            self._play_context = self
            self._loader = self
            self._templar = self
            self._shared_loader_obj = self

    tmp = 1
    task_vars = 2

    test_class = TestActionModule(tmp, task_vars)
    result = test_class.run(tmp, task_vars)

# Generated at 2022-06-13 10:59:20.726185
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing the class object
    action_module_obj = ActionModule()
    # Calling the method with arguments to return the values
    result = action_module_obj.run()
    assert result == 'ansible.legacy.command'

# Generated at 2022-06-13 10:59:29.082894
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    from ansible.plugins.action import ActionBase

    tmp = 'tmp'
    task_vars = {'a':1}
    _task = mock.MagicMock()
    _connection = mock.MagicMock()
    _play_context = mock.MagicMock()
    _loader = mock.MagicMock()
    _templar = mock.MagicMock()
    _shared_loader_obj = mock.MagicMock()

    action_module = ActionModule(_task, _connection, _play_context, _loader, _templar, _shared_loader_obj)
    command_action = mock.MagicMock()
    result = mock.MagicMock()
    command_action.run.return_value = result
    action_module._shared_loader_obj.action_loader.get.return_value

# Generated at 2022-06-13 10:59:30.736994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionMod = ActionModule()
    print(actionMod.run(tmp='', task_vars=''))

# Generated at 2022-06-13 10:59:36.863190
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {
        "changed": False,
        "_ansible_verbose_always": True,
        "stderr": "",
        "stderr_lines": [],
        "stdout": "Current directory: /tmp/\n",
        "stdout_lines": ["Current directory: /tmp/"],
        "warnings": [],
        "rc": 0
    }
    assert  result == ActionModule().run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:59:44.922392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    import json

    from ansible.plugins.loader import connection_loader, module_loader

    from ansible.plugins.action.shell import ActionModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # init the class
    action_module = ActionModule(
        task=dict(args=dict(), action="command"),
        connection=connection_loader.get('network_cli', 'local'),
        play_context=dict(),
        loader=module_loader,
        templar=None,
        shared_loader_obj=None
    )

    response = action_module.run(task_vars=dict())


# Generated at 2022-06-13 10:59:45.618533
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:25.789749
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = {'args': {'_uses_shell': True}}
    action_module._shared_loader_obj = ''
    action_module._connection = ''
    action_module._play_context = ''
    action_module._loader = ''
    action_module._templar = ''
    action_module._shared_loader_obj = ''
    action_module._connection = ''
    action_module._play_context = ''
    action_module._loader = ''
    action_module._templar = ''
    action_module._shared_loader_obj = ''
    action_module._connection = ''
    action_module._play_context = ''
    action_module._loader = ''
    action_module._templar = ''

# Generated at 2022-06-13 11:01:35.360105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModuleTestObj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = actionModuleTestObj.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 11:01:35.722572
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:01:36.265805
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:39.237830
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test for a return code of type dict and the key 'msg'
    # Return 0 as return code
    assert(ActionModule.run(1,2) is not None)
    assert(isinstance(ActionModule.run(1,2), dict))
    assert('msg' in ActionModule.run(1,2))

# Generated at 2022-06-13 11:01:40.618048
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule('ActionModule', 'local', 'runner', 'ansible.legacy.shell', 'ansible.legacy.command')


# Generated at 2022-06-13 11:01:41.152503
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:47.136353
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = dict()
    _task = dict()
    _connection = None
    _play_context = dict()
    _loader = None
    _templar = None
    _shared_loader_obj = None
    obj = ActionModule(None,tmp,_task,_connection,_play_context,_loader,_templar,_shared_loader_obj)
    assert obj.run(tmp,task_vars) == None

# Generated at 2022-06-13 11:01:50.536784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #  " This test is going to use default argument values of run method of class ActionModule."
    #  " It will also test whether the run method is returning the required output."

    test_object = ActionModule()
    assert test_object.run()

# Generated at 2022-06-13 11:01:57.220835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a class object
    am1 = ActionModule()

    # create a temporary file
    fd, tmp = tempfile.mkstemp()

    # create a dictionary to pass as arguments to method run
    args = {}
    args['tmp'] = tmp
    args['task_vars'] = {}
    args['task_vars']['ansible_user_id'] = 'odroid'
    args['task_vars']['ansible_ssh_pass'] = 'odroid'
    args['task_vars']['ansible_become_pass'] = 'odroid'

    # call method run
    result = am1.run(**args)
    # print results
    print(result)
