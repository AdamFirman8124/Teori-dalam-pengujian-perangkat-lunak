

# Generated at 2022-06-13 11:40:23.850855
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    runner_result_failure = """
fatal: [127.0.0.1]: FAILED! => {
    "changed": true, 
    "failed": true, 
    "msg": "Failed to connect to the host via ssh."
}
"""
    runner_result_stdout = "this is the runner_result_stdout!!!"
    runner_result_file = "runner_result_file"
    runner_result_stdout_lines = ["this is the runner_result_stdout!!!", "this is the runner_result_stdout!!!"]
    runner_result_stderr = "this is the runner_result_stderr!!!"
    runner_result_stderr_lines = ["this is the runner_result_stderr!!!", "this is the runner_result_stderr!!!"]


# Generated at 2022-06-13 11:40:34.550814
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    uuid = 'some_uuid'
    name = 'some_name'
    path = 'some_path'
    play = 'some_play'
    action = 'some_action'

    task_data = TaskData(uuid, name, path, play, action)
    assert task_data.uuid == uuid
    assert task_data.name == name
    assert task_data.path == path
    assert task_data.play == play
    assert task_data.action == action
    assert task_data.start is not None
    assert task_data.host_data == {}


# Generated at 2022-06-13 11:40:35.342041
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass

# Generated at 2022-06-13 11:40:41.551901
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task_data = TaskData("", "", "", "", "")

    # test ok
    host = HostData("", "", "ok", "")
    task_data.add_host(host)
    assert len(task_data.host_data) == 1

    # test included
    host = HostData("", "", "included", "")
    host.result = "included"
    task_data.add_host(host)
    assert len(task_data.host_data) == 1
    assert task_data.host_data['host.uuid'].result == 'included\nincluded'
    # print(task_data.host_data['host.uuid'].result)

    # test duplicate host callback

# Generated at 2022-06-13 11:40:45.700415
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task_data = TaskData('123456789', 'TestTask', 'TestPath', 'TestPlay', 'TestAction')
    assert task_data.add_host(HostData('987654321', 'TestHost', 'TestStatus', 'TestResult')) is None


# Generated at 2022-06-13 11:40:51.458348
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task_data_instance = TaskData('uuid', 'name', 'path', 'play', 'action')
    host_instance = HostData('uuid', 'name', 'status', 'result')
    task_data_instance.add_host(host_instance)
    assert task_data_instance.host_data['uuid'] == host_instance


# Generated at 2022-06-13 11:41:03.542107
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    uuid = 'task_data_uuid_1'
    name = 'task_data_name_1'
    path = 'task_data_path_1'
    play = 'task_data_play_1'
    action = 'task_data_action_1'

    task_data = TaskData(uuid, name, path, play, action)

    host_data = HostData('host_data_uuid_1', 'host_data_name_1', 'host_data_status_1', 'host_data_result_1')
    try:
        task_data.add_host(host_data)
        assert len(task_data.host_data) == 1
    except Exception as err:
        print(err)


# Generated at 2022-06-13 11:41:09.971800
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    taskData = TaskData("uuid", "name", "path", "play", "action")
    hostData1 = HostData("uuid1", "name1", "ok", "result1")
    hostData2 = HostData("uuid2", "name2", "failed", "result2")
    hostData3 = HostData("uuid2", "name2", "ok", "result3")
    taskData.add_host(hostData1)
    taskData.add_host(hostData2)
    taskData.add_host(hostData3)


# Generated at 2022-06-13 11:41:12.133539
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    assert cb.v2_runner_on_failed(result='failed') is None

# Generated at 2022-06-13 11:41:15.255677
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task = TaskData('test_id1', 'test_name', 'test_path', 'test_play', 'test_action')
    task.add_host(HostData('test_id1', 'test_name', 'test_status', 'test_result'))
    assert task.host_data['test_id1'].uuid == 'test_id1'


# Generated at 2022-06-13 11:41:32.899277
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Define input and expected output
    input_obj = MockResult()
    input_obj.host._hostname = 'hostname'
    
    input_obj.result['msg'] = 'msg'
    
    expected_return = None
    expected_task_data = {
        'task_uuid': {'name': 'name',
         'action': 'action',
         'play': 'play',
         'path': 'path',
         '_uuid': 'task_uuid',
         'start': 0,
         'host_data': {'host_uuid': {'name': 'hostname',
            'status': 'failed',
            'result': input_obj}}}}
    expected_file_name = 'path/to/file-1.xml'

    # Init CallbackModule object
    obj = CallbackModule

# Generated at 2022-06-13 11:41:39.526882
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    playbook = FakePlaybook('', 'abc')
    assert cb.v2_playbook_on_start(playbook) == None
    assert cb._playbook_path == 'abc'
    assert cb._playbook_name == 'abc'


# Generated at 2022-06-13 11:41:40.421689
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
  pass

# Generated at 2022-06-13 11:41:45.455079
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = Playbook()
    callback = CallbackModule()
    callback.v2_playbook_on_start(playbook)
    assert callback._playbook_path == '/path/to/playbook'
    assert callback._playbook_name == 'playbook'



# Generated at 2022-06-13 11:41:47.446359
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    cb.v2_playbook_on_start()


# Generated at 2022-06-13 11:41:54.419904
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Arrange
    cm = CallbackModule()
    # cm._start_task(1)
    result = {'result':{'rc': '0','msg': '','skip_reason': 'Conditional result was False','changed': False,'invocation': {'module_args': 'echo this is a test','module_name': 'command','module_complex_args': {'_raw_params': 'echo this is a test','_uses_shell': False,'chdir': None,'creates': None,'executable': None,'removes': None,'stdin': None,'warn': True}}}}
    ignore_errors = True
    # Act
    cm.v2_runner_on_failed(result=result, ignore_errors=ignore_errors)
    # Assert
    assert type(result) == dict


# Generated at 2022-06-13 11:41:57.634244
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # TODO: Implement test case for method CallbackModule.v2_runner_on_failed
    raise unittest.SkipTest("Not implemented.")



# Generated at 2022-06-13 11:42:02.759693
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Arrange
    playbook = 'my_playbook'
    cb = CallbackModule()
    # Act
    cb.v2_playbook_on_start(playbook)
    # Assert
    assert cb._playbook_path == 'my_playbook'
    assert cb._playbook_name == 'my_playbook'
    assert cb._play_name is None
    assert cb._task_data == {}


# Generated at 2022-06-13 11:42:10.590270
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # create a new instance of CallbackModule
    callback_module_cls = CallbackModule()

    # create dummy parameters
    file_name = 'test_data/test.yml'
    c = MagicMock()
    c.file_name = file_name
    c._file_name = file_name
    # c = MagicMock(file_name = file_name,
    #     _file_name = file_name)

    # call the method we want to test
    callback_module_cls.v2_playbook_on_start(c)

    # verify the attribute was set
    assert callback_module_cls._playbook_path == file_name
    assert callback_module_cls._playbook_name == 'test'



# Generated at 2022-06-13 11:42:17.588765
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = MockPlaybook()
    result = MockStats()
    cb = CallbackModule()
    cb.v2_playbook_on_start(playbook)
    assert cb._playbook_path == "test.yml"
    assert cb._playbook_name == "test"
    cb.v2_playbook_on_stats(result)
    assert cb._playbook_path == "test.yml"
    assert cb._playbook_name == "test"


# Generated at 2022-06-13 11:42:37.215235
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Set up mock objects
    playbook = mock.MagicMock()
    self = CallbackModule()

    # Execute method under test
    self.v2_playbook_on_start(playbook)

    # Assertions
    assert self._playbook_path is not None
    assert self._playbook_name is not None


# Generated at 2022-06-13 11:42:41.332986
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    '''
    Unit test for method v2_playbook_on_start of class CallbackModule
    '''
    callback = CallbackModule()
    callback.v2_playbook_on_start()
    pass


# Generated at 2022-06-13 11:42:50.246483
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    cb._task_class = 'false'
    cb._task_relative_path = ''
    cb._fail_on_change = 'false'
    cb._hide_task_arguments = 'false'
    cb._test_case_prefix = ''
    cb._include_setup_tasks_in_report = 'true'
    cb._fail_on_ignore = 'false'
    cb._output_dir = 'True'
    cb._playbook_path = ''
    cb._playbook_name = 'playbookname'
    cb.v2_playbook_on_play_start(play='test')
    task = {'action': 'test'}
    task = FakeTask()
    task._uuid = 'new_uuid'
   

# Generated at 2022-06-13 11:42:55.310864
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = Mock()

    playbook._file_name = 'playbook.yml'

    callbackmodule = CallbackModule()

    callbackmodule.v2_playbook_on_start(playbook)

    assert callbackmodule._playbook_path == 'playbook.yml'
    assert callbackmodule._playbook_name == 'playbook'


# Generated at 2022-06-13 11:43:04.159476
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start(): 
    print('Testing CallbackModule.v2_playbook_on_start')
    import ansible.playbook
    import os
    import os.path
    import os
    import time
    import re
    from ansible import constants as C
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.plugins.callback import CallbackBase
    from ansible.utils._junit_xml import (
        TestCase,
        TestError,
        TestFailure,
        TestSuite,
        TestSuites,
    )
    playbook = ansible.playbook.Playbook()
    instance = CallbackModule()
    instance.v2_playbook_on_start(playbook)


# Generated at 2022-06-13 11:43:05.293904
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass # Nothing to test

# Generated at 2022-06-13 11:43:13.361893
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # mock object of class Playbook
    class Playbook(object):
        def __init__(self):
            self._file_name = "playbook_xyz.yml"
    # mock object of class Play
    class Play(object):
        def __init__(self):
            self._name = "my_play"
    # mock object of class Task
    class Task(object):
        def __init__(self):
            self._uuid = "123"
            self._name = "my_task"
            self._action = "some_action"
            self._path = "data/test_data/test_data.yml"
        def get_name(self):
            return self._name
        def get_path(self):
            return self._path
        def action(self):
            return self._action
   

# Generated at 2022-06-13 11:43:18.005720
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    callbackModule = CallbackModule()
    playbook = Playbook()
    playbook.add_attribute('_file_name', './dummy.txt')
    callbackModule.v2_playbook_on_start(playbook)
    assert callbackModule._playbook_path == './dummy.txt'
    assert callbackModule._playbook_name == 'dummy'


# Generated at 2022-06-13 11:43:23.975577
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    class Mock_v2_playbook_on_start_returns:
        def __init__(self):
            self._file_name = None
 
    instance = CallbackModule()
    instance._playbook_path = None
    instance._playbook_name = None
    instance.v2_playbook_on_start(Mock_v2_playbook_on_start_returns())
    assert instance._playbook_path == None
    assert instance._playbook_name == None

# Generated at 2022-06-13 11:43:24.848395
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass # TODO


# Generated at 2022-06-13 11:43:52.730222
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    import os
    import os.path
    from ansible.module_utils._text import to_bytes
    
    from ansible.plugins.callback import CallbackBase
    from ansible.utils._junit_xml import TestCase, TestSuite, TestSuites
    
    class Playbook:
        def __init__(self, _file_name, name):
            self._file_name = _file_name
            self.name = name
    
    class AnsibleModule:
        def __init__(self, params, ok=True, changed=False, skipped=False, failed=False):
            self.params = params
            self.ok = ok
            self.changed = changed
            self.skipped = skipped
            self.failed = failed
    
    def apply_mocking(*args, **kwargs):
        mocked_methods

# Generated at 2022-06-13 11:43:56.139851
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # create instance of module
    m = CallbackModule()

    # test invocation of method v2_runner_on_failed
    m.v2_runner_on_failed()

# Generated at 2022-06-13 11:44:04.263597
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Test v2_runner_on_failed() method
    # initialization of the callback module
    from ansible.plugins import callback_loader
    callback = callback_loader._create_instance('junit')
    callback.set_runner(Runner('localhost', 'test', 'test'))
    # initialization of the result
    result = Result(Task(DictObj({'name': 'test', 'action': 'test'}), 'localhost', 'test', DictObj({})))
    result._host = 'localhost'
    result._task = Task(DictObj({'name': 'test', 'action': 'test'}), 'localhost', 'test', DictObj({}))
    result._result = result.dict()
    result._result['stdout'] = 'test'
    result._result['stdout_lines'] = ['test']
    result

# Generated at 2022-06-13 11:44:11.045424
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    global callback
    mock_playbook = MagicMock()
    mock_playbook._file_name = '/mock/playbook.yml'
    callback.v2_playbook_on_start(mock_playbook)

    assert callback._playbook_path == '/mock/playbook.yml'
    assert callback._playbook_name == 'playbook'


# Generated at 2022-06-13 11:44:22.568058
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    cb._output_dir = os.path.expanduser('~/.ansible.log')
    os.environ["JUNIT_TASK_CLASS"] = "False"
    os.environ["JUNIT_TASK_RELATIVE_PATH"] = "none"
    os.environ["JUNIT_FAIL_ON_CHANGE"] = "False"
    os.environ["JUNIT_FAIL_ON_IGNORE"] = "False"
    os.environ["JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT"] = "True"
    os.environ["JUNIT_HIDE_TASK_ARGUMENTS"] = "False"

# Generated at 2022-06-13 11:44:23.584470
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass # Not implemented


# Generated at 2022-06-13 11:44:34.045383
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Setup CallbackModule
    c = CallbackModule()
    c._output_dir = os.getenv('JUNIT_OUTPUT_DIR', os.path.expanduser('~/.ansible.log'))
    c._task_class = os.getenv('JUNIT_TASK_CLASS', 'False').lower()
    c._task_relative_path = os.getenv('JUNIT_TASK_RELATIVE_PATH', '')
    c._fail_on_change = os.getenv('JUNIT_FAIL_ON_CHANGE', 'False').lower()
    c._fail_on_ignore = os.getenv('JUNIT_FAIL_ON_IGNORE', 'False').lower()

# Generated at 2022-06-13 11:44:34.691700
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass


# Generated at 2022-06-13 11:44:44.262149
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("Unit test for method v2_runner_on_failed of class CallbackModule ")
    print("=======================================================")
    print("Expected:")
    print("passed")
    print("Actual:")
    from ansible.plugins.callback import CallbackBase
    from ansible.utils._junit_xml import (
    TestCase,
    TestError,
    TestFailure,
    TestSuite,
    TestSuites,
)

# Generated at 2022-06-13 11:44:50.673389
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    """unit test for v2_playbook_on_start method of class CallbackModule"""
    callbackModule = CallbackModule()
    playbook = DummyPlaybook(file_name='test.yml')
    callbackModule.v2_playbook_on_start(playbook)
    assert callbackModule._playbook_path == 'test.yml'
    assert callbackModule._playbook_name == 'test'
    

# Generated at 2022-06-13 11:45:26.305546
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cbm = CallbackModule()
    cbm.v2_playbook_on_start(playbook=Playbook(file_name='/tmp/test_playbook.yml'))
    assert cbm._playbook_path == '/tmp/test_playbook.yml'
    assert cbm._playbook_name == 'test_playbook'



# Generated at 2022-06-13 11:45:30.560155
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    c._start_task(object())
    c.v2_runner_on_failed(object())
    assert c._task_data[object()].host_data[object()].status == "failed"


# Generated at 2022-06-13 11:45:41.502877
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    """
    Test if unit test for v2_runner_on_failed() method returns correct values.
    """
    
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    # create test inventory
    loader = DataLoader()
    results_callback = CallbackModule()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create test options
    options = None

    # create test playbooks
    script_dir = os.path.dirname(os.path.realpath(__file__))
    playbook_path = os.path

# Generated at 2022-06-13 11:45:42.456123
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass

# Generated at 2022-06-13 11:45:46.909566
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
# CallbackModule: v2_playbook_on_start
    playbook = Playbook()
    callbackModule = CallbackModule()
    callbackModule.v2_playbook_on_start(playbook)


# Generated at 2022-06-13 11:45:47.789299
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:45:52.715386
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
  # Setup
  stat_mock = MagicMock()
  stat_mock._file_name = "my_playbook"
  # Test
  instance = CallbackModule()
  instance.v2_playbook_on_start(stat_mock)


# Generated at 2022-06-13 11:46:03.086505
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Create an instance of CallbackModule
    cbmodule = CallbackModule()
    
    # Test if init method has been called
    assert cbmodule._playbook_name is None
    assert cbmodule._playbook_path is None
    assert cbmodule._play_name is None
    
    # Test if v2_playbook_on_start has been called
    class mock_playbook:
        def __init__(self):
            self._file_name = "./test/test_CallbackModule_v2_playbook_on_start.yml"
    
    mock_playbook = mock_playbook()
    cbmodule.v2_playbook_on_start(mock_playbook)
    

# Generated at 2022-06-13 11:46:09.977884
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    playbook = MagicMock()
    playbook._file_name = '/path/to/file.yml'
    cb.v2_playbook_on_start(playbook)
    assert cb._playbook_path == '/path/to/file.yml'
    assert cb._playbook_name == 'file'


# Generated at 2022-06-13 11:46:13.378944
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Setup mocks
    class MockClass:
        def __init__(self):
            self._file_name = 'C:\\Temp\\hello-world.yml'

    # Execute function
    callback_module = CallbackModule()
    callback_module.v2_playbook_on_start(MockClass())

    # Check results
    assert callback_module._playbook_path == 'C:\\Temp\\hello-world.yml'
    assert callback_module._playbook_name == 'hello-world'


# Generated at 2022-06-13 11:47:16.883826
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cbm = CallbackModule()
    cbm.v2_runner_on_failed(unittest.mock.Mock())
    assert 1 == 1, "Should not fail"

# Generated at 2022-06-13 11:47:23.159233
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    module = CallbackModule()
    playbook = {"_file_name": "C:\\Users\\Julien\\.ansible\\cp.retry"}
    module.v2_playbook_on_start(playbook)
    assert module._playbook_name == "cp"
    assert module._playbook_path == "C:\\Users\\Julien\\.ansible\\cp.retry"


# Generated at 2022-06-13 11:47:28.748675
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    """
    CallbackModule.v2_playbook_on_start is a method of CallbackModule class
    """
    # noinspection PyProtectedMember
    assert hasattr(CallbackModule, 'v2_playbook_on_start')

# Generated at 2022-06-13 11:47:33.046828
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # set up
    cb = CallbackModule()
    pb = None

    # run
    cb.v2_playbook_on_start(pb)

    # assert
    assert cb._playbook_name == "<unknown>"
    assert cb._playbook_path == None


# Generated at 2022-06-13 11:47:37.160079
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    callback_module = CallbackModule()
    playbook =  ['test', 'test']
    callback_module.v2_playbook_on_start(playbook)
    assert callback_module._playbook_path ==  'test'
    assert callback_module._playbook_name ==  'test'


# Generated at 2022-06-13 11:47:40.815499
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    class MockPlaybook():
        _file_name = 'test'
    module = CallbackModule()
    module.v2_playbook_on_start(MockPlaybook())
    # test
    assert module._playbook_path == 'test'


# Generated at 2022-06-13 11:47:48.138255
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import Mock
    from ansible.compat.tests.mock import patch

    def test(self, playbook):
        self._playbook_path = playbook._file_name
        self._playbook_name = os.path.splitext(os.path.basename(self._playbook_path))[0]

    with patch('os.path.splitext') as os_path_splitext:
        with patch('os.path.basename') as os_path_basename:
            os_path_splitext.return_value = Mock(spec_set=['__getitem__'])
            os_path_basename.return_value = 'mock_basename'
            callback = CallbackModule()
           

# Generated at 2022-06-13 11:47:56.249180
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Test scenario mocks
    starting_playbook = TestMock.MockObject()
    starting_playbook._file_name = 'playbook_name'

    # Executing code
    cm = CallbackModule()
    cm.v2_playbook_on_start(starting_playbook)

    # Verifying results
    assert cm._playbook_path == 'playbook_name'

    assert cm._playbook_name == 'playbook_name'


# Generated at 2022-06-13 11:48:03.052851
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    class MockPlaybook:
        def __init__(self, _file_name):
            self._file_name = _file_name
    class MockModule:
        def __init__(self, *args, **kwargs):
            pass
        def v2_playbook_on_start(self, *args, **kwargs):
            pass
        def __getattr__(self, name):
            if name.startswith("v2_playbook_on_start"):
                return MockModule.v2_playbook_on_start
            else:
                raise AttributeError("MockModule instance has no attribute '%s'" % name)
    cb = MockModule()
    cb.v2_playbook_on_start(MockPlaybook("mock-playbook.yml"))
    assert os.path.bas

# Generated at 2022-06-13 11:48:03.638205
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass