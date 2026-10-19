

# Generated at 2022-06-13 11:40:12.437731
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    # Arrange
    task_uuid = 'uuid'
    name = 'name'
    path = 'path'
    play = 'play'
    start = 'start'
    action = 'action'
    host_data = {}
    task_data = TaskData(task_uuid, name, path, play, action)
    host = HostData('uuid', 'hostname', 'status', 'result')
    # Act
    task_data.add_host(host)
    # Assert
    assert task_data.host_data['uuid'].uuid == 'uuid'
    # Cleanup



# Generated at 2022-06-13 11:40:21.522822
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    td = TaskData('uuid', 'name', 'path', 'play', 'action')

    hd = HostData('uuid', 'name', 'status', None)
    hd.result = 'result'
    td.add_host(hd)

    assert td.host_data['uuid'].result == hd.result

    hdn = HostData('uuid', 'name', 'status', None)
    hdn.result = 'another result'
    td.add_host(hdn)

    assert td.host_data['uuid'].result == 'result\nanother result'


# Generated at 2022-06-13 11:40:36.170285
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.modules.system import ping
    import os
    import shutil
    import textwrap
    import xml.etree.ElementTree as ET

    def _read_xml(path):
        with open(path, 'rb') as file:
            return ET.fromstringlist(file.readlines())


# Generated at 2022-06-13 11:40:41.918084
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    a = TaskData('uuid', 'name', 'path', 'play', 'action')
    b = HostData('uuid', 'name', 'status', 'result')
    c = HostData('uuid', 'name', 'status', 'result')
    a.add_host(b)
    a.add_host(c)



# Generated at 2022-06-13 11:40:47.589016
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task_data = TaskData(uuid='uuid', name='name', path='path', play='play', action='action')
    host_data = HostData(uuid='uuid', name='name', status='ok', result=None)
    task_data.add_host(host_data)
    assert (len(task_data.host_data)==1)



# Generated at 2022-06-13 11:40:57.267367
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task = TaskData('uuid', '[play] task: a task', 'path', 'play', 'action')
    host1 = HostData('uuid1', 'host1', 'included', 'result a')
    host2 = HostData('uuid1', 'host1', 'included', 'result b')
    host3 = HostData('uuid1', 'host1', 'failed', 'result c')

    task.add_host(host1)

    assert task.host_data['uuid1'].status == 'included'
    assert task.host_data['uuid1'].result == 'result a'

    task.add_host(host2)

    assert task.host_data['uuid1'].status == 'included'

# Generated at 2022-06-13 11:41:04.947410
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    test_taskdata = TaskData('1', 'task1', 'file1', 'play1', 'action')
    test_host = HostData('1', 'host1', 'ok', {'_task': 'task1', '_host': 'host1'})
    expected_output = {'1': 'host1'}
    test_taskdata.add_host(test_host)
    output = test_taskdata.host_data
    assert output == expected_output


# Generated at 2022-06-13 11:41:12.564608
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    import pytest
    from collections import defaultdict
    from junit_logging.junit_callback import TaskData
    from junit_logging.junit_callback import HostData

    test_name = 'test_name'
    test_path = 'test_path'
    test_play = 'test_play'

    task_data = TaskData(test_name,test_path,test_play)
    assert(task_data.name == test_name)
    assert(task_data.path == test_path)
    assert(task_data.play == test_play)

    task_data.add_host('test_key','test_value')

    assert(task_data.host_data['test_key'] == 'test_value')


# Generated at 2022-06-13 11:41:18.618846
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    task = TaskData(uuid = '123', name = 'a task', path = 'foo', play = 'bar')
    host_included = HostData(uuid = 'included', name = 'included host', status = 'included', result = 'included')
    host_included2 = HostData(uuid = 'included', name = 'included host', status = 'included', result = 'included2')
    host_ok = HostData(uuid = 'ok', name = 'ok host', status = 'ok', result = 'ok')
    host_failed = HostData(uuid = 'failed', name = 'failed host', status = 'failed', result = 'failed')

    host_ok.start = 0
    host_ok.finish = 1

    task.add_host(host_ok)

# Generated at 2022-06-13 11:41:24.331427
# Unit test for method add_host of class TaskData
def test_TaskData_add_host():
    '''
    Test for method add_host of class TaskData
    '''
    test_task = TaskData(uuid = 123, name = 'test_name', path = 'test_path', play = 'test_play', action = 'test_action')
    test_host = HostData(uuid = 123, name = 'test_name', status = 'test_status', result = 'test_result')

    test_task.add_host(test_host)

    assert(test_host.name == test_task.host_data[123].name)



# Generated at 2022-06-13 11:41:33.663934
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 11:41:34.582510
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
  pass


# Generated at 2022-06-13 11:41:39.183373
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
	path = "~/ansible-junit.log"
	playbook_filename = "~/playbook.yml"
	playbook = CallbackModule()
	playbook.v2_playbook_on_start(playbook_filename)
	assert(playbook_filename == playbook._playbook_path)
	assert(playbook_filename == playbook._playbook_name)


# Generated at 2022-06-13 11:41:42.671794
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    from ansible.playbook import Playbook

    playbook = Playbook()

    callback_module = CallbackModule()
    callback_module.v2_playbook_on_start(playbook)

    assert callback_module._playbook_path == ""
    assert callback_module._playbook_name == ""


# Generated at 2022-06-13 11:41:43.354770
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass

# Generated at 2022-06-13 11:41:48.775025
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Initialization
    cb = CallbackModule()
    pb = Playbook(playbook='Ansible')

    # Execution
    cb.v2_playbook_on_start(pb)

    # Verification
    assert cb._playbook_path == 'Ansible'
    assert cb._playbook_name == 'Ansible'



# Generated at 2022-06-13 11:41:58.730946
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    cb.disabled = True
    cb._output_dir = os.getenv('JUNIT_OUTPUT_DIR', os.path.expanduser('~/.ansible.log'))
    cb._task_class = os.getenv('JUNIT_TASK_CLASS', 'False').lower()
    cb._task_relative_path = os.getenv('JUNIT_TASK_RELATIVE_PATH', '')
    cb._fail_on_change = os.getenv('JUNIT_FAIL_ON_CHANGE', 'False').lower()
    cb._fail_on_ignore = os.getenv('JUNIT_FAIL_ON_IGNORE', 'False').lower()
    cb._include_setup_tasks_in_report = os

# Generated at 2022-06-13 11:42:00.978507
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    test_obj = CallbackModule()
    playbook = DummyPlaybook()
    test_obj.v2_playbook_on_start(playbook)


# Generated at 2022-06-13 11:42:07.485789
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    try:
        # Arrange
        callback_module = CallbackModule()
        playbook = unittest.mock.Mock()
        playbook._file_name = "test_playbook.yml"

        # Act
        callback_module.v2_playbook_on_start(playbook)

        # Assert
        assert callback_module._playbook_path == "test_playbook.yml"
        assert callback_module._playbook_name == "test_playbook"
    except:
        pytest.fail("No exception raised in test_CallbackModule_v2_playbook_on_start")



# Generated at 2022-06-13 11:42:08.334838
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass



# Generated at 2022-06-13 11:42:18.983673
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    with open('./junit.log', 'w') as f:
        f.write('')
    module = CallbackModule()
    module.v2_playbook_on_start(playbook=AnsiblePlaybook())

# Generated at 2022-06-13 11:42:27.909679
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.callback import CallbackBase
    from ansible.executor import task_result
    
    
    class CallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'junit'
        CALLBACK_NEEDS_ENABLED = True
        def __init__(self):
            
            self._output_dir = os.getenv('JUNIT_OUTPUT_DIR', os.path.expanduser('~/.ansible.log'))
            self._task_class = os.getenv('JUNIT_TASK_CLASS', 'False').lower()
            self._task_relative_path = os.get

# Generated at 2022-06-13 11:42:38.786106
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    ''' test method CallbackModule.v2_runner_on_failed '''
    class task():
        def get_name(self):
            return self.name
        def __init__(self, name):
            self.name = name
    class result():
        class _task():
            def __init__(self, name):
                self._uuid = name
        def __init__(self, uuid):
            self._uuid = uuid
            self._host = self._task(uuid)
            self._task = self._task(uuid)
        def _get_task_name(self):
            return self._uuid

    class HostData():
        def __init__(self, host_uuid, host_name, status, result):
            self.name = host_name
            self.status = status
   

# Generated at 2022-06-13 11:42:43.069654
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = True
    data_calback = CallbackModule(playbook)
    data_calback.v2_playbook_on_start(playbook)
    assert data_calback._playbook_name == 'True'
    assert data_calback._playbook_path == 'True'

# Generated at 2022-06-13 11:42:46.052322
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cbm = CallbackModule()

    result = "test"
    cbm.v2_runner_on_failed(result, ignore_errors=False)
    assert cbm._finish_task('failed', result)



# Generated at 2022-06-13 11:42:57.432187
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cbm = CallbackModule()
    cbm.v2_playbook_on_start(playbook = "<playbook>")
    cbm.v2_playbook_on_play_start(play = "<play>")
    cbm.v2_runner_on_no_hosts(task = "<task>")
    cbm.v2_playbook_on_task_start(task = "<task>", is_conditional = False)
    cbm.v2_playbook_on_cleanup_task_start(task = "<task>")
    cbm.v2_runner_on_failed(result = "<result>", ignore_errors = False)
    cbm.v2_runner_on_ok(result = "<result>")

# Generated at 2022-06-13 11:43:05.993185
# Unit test for method v2_playbook_on_start of class CallbackModule

# Generated at 2022-06-13 11:43:10.631062
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # initialize callback
    my_callback = CallbackModule()

    # define test data
    my_task = 'dummy task'
    my_result = 'dummy result'
    my_ignore_errors = False

    # call v2_runner_on_failed
    my_callback.v2_runner_on_failed(my_result, my_ignore_errors)

    # TODO: Check results


# Generated at 2022-06-13 11:43:14.844398
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    cb.v2_playbook_on_start()
    cb.v2_playbook_on_start('playbook')


# Generated at 2022-06-13 11:43:29.104236
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    import os
    import time
    import re

    from callback_module import CallbackModule
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
    
    c = CallbackModule()
    c.v2_playbook_on_start('/home/fake/ansible/site.yml')
    assert c._playbook_path == '/home/fake/ansible/site.yml'
    assert c._playbook_name == 'site'


# Generated at 2022-06-13 11:43:46.568818
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    failed = False
    junit_plugin = CallbackModule()
    #put in your own test case here
    assert failed == False


# Generated at 2022-06-13 11:43:55.757924
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Return value of the tested method
    # (instance of class CallbackModule)
    obj = CallbackModule()
    # Arguments provided to the tested method
    # (instance of class PlayBook)
    playbook = PlayBook()
    # Call the tested method
    obj.v2_playbook_on_start(playbook)
    # Assertion for correctness of the tested method
    assert obj._playbook_path == playbook._file_name
    assert obj._playbook_name == os.path.splitext(os.path.basename(obj._playbook_path))[0]


# Generated at 2022-06-13 11:43:58.403316
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    """
    Test that the playbook name is set correctly.
    """
    pass



# Generated at 2022-06-13 11:44:02.321378
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

  # Test instance creation
  x=CallbackModule()

  # Test method call
  x.v2_runner_on_failed(result, ignore_errors=False)

  # Test method call
  x.v2_runner_on_failed(result, ignore_errors=True)


# Generated at 2022-06-13 11:44:07.528439
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # set the file name for the playbook
    test_callback = CallbackModule()
    test_callback.v2_playbook_on_start("test_playbook")

    assert "test_playbook" == test_callback._playbook_path
    assert "test_playbook" == test_callback._playbook_name


# Generated at 2022-06-13 11:44:12.204822
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    b = CallbackModule()
    b.v2_playbook_on_start('playbook')
    assert b._playbook_path == 'playbook'
    assert b._playbook_name == 'playbook'


# Generated at 2022-06-13 11:44:23.550398
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    output_dir = os.path.expanduser('~/.ansible.log')
    playbook_name = os.path.splitext(os.path.basename(__file__))[0]

    obj = CallbackModule()
    obj.v2_playbook_on_start(__file__)

    assert obj._playbook_name == playbook_name
    assert obj._playbook_path == __file__
    assert obj._output_dir == output_dir
    assert obj._task_class == 'false'
    assert obj._task_relative_path == ''
    assert obj._fail_on_change == 'false'
    assert obj._fail_on_ignore == 'false'
    assert obj._include_setup_tasks_in_report == 'true'
    assert obj._hide_task_arguments == 'false'


# Generated at 2022-06-13 11:44:28.335603
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()
    playbook = mock.Mock()
    playbook.get_filename.return_value = "./playbook.yml"
    cb.v2_playbook_on_start(playbook)
    assert cb._playbook_path == "./playbook.yml"
    assert cb._playbook_name == "playbook"

# Generated at 2022-06-13 11:44:32.163085
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    c = CallbackModule()
    assert c.v2_playbook_on_start(c._playbook_path) == os.path.splitext(os.path.basename(c._playbook_path))[0]



# Generated at 2022-06-13 11:44:32.918400
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    assert True

# Generated at 2022-06-13 11:45:06.957366
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    sample_callback = CallbackModule()
    assert sample_callback.v2_playbook_on_start('playbook') is None
    assert sample_callback._playbook_path == 'playbook'
    assert sample_callback._playbook_name == 'playbook'


# Generated at 2022-06-13 11:45:12.574414
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    import os, os.path
    # Method CallbackModule.v2_playbook_on_start
    # Test 1
    callback = CallbackModule()
    callback.v2_playbook_on_start("playbook")
    assert callback._playbook_path == "playbook._file_name"
    assert callback._playbook_name == "os.path.splitext(os.path.basename(callback._playbook_path))[0]"



# Generated at 2022-06-13 11:45:13.618449
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass


# Generated at 2022-06-13 11:45:17.354396
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
	# initialize target class
	cb = CallbackModule()
	# initialize params
	playbook = None
	# perform operation
	cb.v2_playbook_on_start(playbook)
	# verify results
	assert True # TODO: implement your test here


# Generated at 2022-06-13 11:45:23.360888
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    global task_data
    global play_name
    cb = CallbackModule()
    cb.v2_playbook_on_stats('stats')
    assert len(task_data) == 1
    assert task_data[0]['msg'] == 'Failure'
    assert play_name == 'my_play'

# Generated at 2022-06-13 11:45:24.879236
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass


# Generated at 2022-06-13 11:45:25.730603
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass


# Generated at 2022-06-13 11:45:33.935098
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = mock_object()
    playbook._file_name = '/Users/polachok/Documents/GitRepo/ansible/test.yml'
    callback = CallbackModule()

    callback.v2_playbook_on_start(playbook)

    # Check for correct output dir
    assert(callback._output_dir == os.path.expanduser('~/.ansible.log'))
    # Check for correct playbook name
    assert(callback._playbook_name == 'test')


# Generated at 2022-06-13 11:45:43.704279
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback.junit import CallbackModule
    import ansible.task
    import ansible.inventory
    import ansible.vars

    args = {'msg': 'TEST_FAIL'}
    result = ansible.task.TaskResult(ansible.inventory.Host(name='testhost'), args)
    result._result = {'failed': True, 'msg': 'TEST_FAIL'}
    callback = CallbackModule()
    callback.v2_runner_on_failed(result)
    assert(callback._task_data['a734225fcb6e41f9b8aa6c86ec6b0c6b'].host_data.get('d48a9f1c8db14cc6abf5f7bd74a0d2f1').status == 'failed')


# Generated at 2022-06-13 11:45:56.588200
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # test that all attributes are initialized
    cb0 = CallbackModule()
    assert cb0._playbook_path == None
    assert cb0._playbook_name == None
    assert cb0._play_name == None
    assert cb0._task_data == {}
    assert cb0.disabled == False
    
    # test that playbook path, name and play name are correctly set
    playbook = None
    cb1 = CallbackModule()
    cb1.v2_playbook_on_start(playbook)
    assert cb1._playbook_path == playbook._file_name
    assert cb1._playbook_name == os.path.splitext(os.path.basename(cb1._playbook_path))[0]
    assert cb1._play_name == None

# Generated at 2022-06-13 11:46:59.438643
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    clb = CallbackModule()
    clb.v2_runner_on_failed(None)


# Generated at 2022-06-13 11:47:08.742372
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    """
    Testing CallbackModule::v2_playbook_on_start
    """
    imp = get_import_mock('import os')
    imp.set_attr('os.path.splitext', lambda path: ('', '.yml'))
    imp.set_attr('os.path.basename', lambda path: 'playbook.yml')
    imp.set_attr('os.path.expanduser', lambda path: path)

    m = get_instance_mock(CallbackModule())
    m.set_attr('_playbook_path', None)
    m.set_attr('_playbook_name', None)

    # run

# Generated at 2022-06-13 11:47:10.256574
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # GIVEN
    # WHEN
    # THEN

    pass


# Generated at 2022-06-13 11:47:14.393863
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = 'playbook_path'
    callbackModule = CallbackModule()
    callbackModule.v2_playbook_on_start(playbook)
    assert callbackModule._playbook_path == 'playbook_path'
    assert callbackModule._playbook_name == 'playbook_path'


# Generated at 2022-06-13 11:47:19.147010
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Initialize
    playbook = {"tasks": []}
    # Run function
    callback = CallbackModule()
    try:
        callback.v2_playbook_on_start(playbook)
    except Exception as err:
        assert False, err
    assert True


# Generated at 2022-06-13 11:47:24.490543
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    callbackModule = CallbackModule()
    callbackModule._playbook_path = None
    callbackModule._playbook_name = None

    playbook = DummyPlaybook()
    callbackModule.v2_playbook_on_start(playbook)
    assert callbackModule._playbook_path == 'ansible.log'
    assert callbackModule._playbook_name == 'ansible'



# Generated at 2022-06-13 11:47:39.799777
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    import os
    p = os.path.dirname
    parent = p(p(os.path.realpath(__file__)))
    import sys
    sys.path.append(parent)
    import test_utils
    test_utils.remove_dir_contents(".ansible.log")
    from collections import namedtuple

    # Arrange
    playbook = namedtuple('playbook', '_file_name')(
      parent + "/test_callback.yml")

    # Act
    callback = CallbackModule()
    callback.v2_playbook_on_start(playbook)

    # Assert
    assert callback._playbook_name == 'test_callback'
    test_utils.remove_dir_contents(".ansible.log")


# Generated at 2022-06-13 11:47:41.056139
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    assert(True)



# Generated at 2022-06-13 11:47:49.996715
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

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


# Generated at 2022-06-13 11:47:53.159911
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    self = CallbackModule()
    playbook = None
    self.v2_playbook_on_start(playbook)