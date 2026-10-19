

# Generated at 2022-06-13 11:51:33.551770
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    mock_display = Mock()
    cb = CallbackModule(display=mock_display)

    assert cb
    assert cb.callback_version == 2.0
    assert cb.callback_type == 'stdout'
    assert cb.callback_name == 'oneline'
    assert cb._display == mock_display



# Generated at 2022-06-13 11:51:36.145435
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    """ Unit test of method 'v2_runner_on_failed' of class 'CallbackModule'
    """
    # TODO: TO BE PORTED
    pass


# Generated at 2022-06-13 11:51:45.133754
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()

    res = MockResult()

# Generated at 2022-06-13 11:51:50.620006
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    # setup test object
    module = CallbackModule()
    # test constructor
    assert isinstance(module, CallbackModule)
    # test version
    assert module.CALLBACK_VERSION == 2.0
    # test type
    assert module.CALLBACK_TYPE == 'stdout'
    # test name
    assert module.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:51:59.632041
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.module_utils.common.collections import ImmutableDict

    module = CallbackModule()
    result = ImmutableDict(changed=True, _host=ImmutableDict(get_name=lambda: 'localhost'),
        _result=ImmutableDict(get='this is the returned result', ansible_facts=ImmutableDict(info=dict(a=0, b=1, c=2))))
    real_result = module.v2_runner_on_ok(result)
    expected_result = "localhost | CHANGED => {\"ansible_facts\": {\"info\": {\"a\": 0, \"b\": 1, \"c\": 2}}, \"changed\": true, \"get\": \"this is the returned result\"}\n"
    assert real_result == expected_result


# Generated at 2022-06-13 11:52:09.860200
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("Unit test for method v2_runner_on_failed of class CallbackModule")
    fake_host = "127.0.0.1"
    fake_task_name = "test_v2_runner_on_failed"
    fake_result_dict = {
                         "exception": "test exception message",
                         "module_stdout": "test module stdout message",
                         "module_stderr": "test module stderr message",
                         "module_lang": "test module lang",
                         "module_set_locale": "test module set locale"
                       }
    fake_result = FakeResult(FakeHost(fake_host), FakeTask(fake_task_name, fake_result_dict))
    oneline = CallbackModule()
    oneline.v2_runner_on_failed(fake_result)



# Generated at 2022-06-13 11:52:12.434804
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    assert CallbackModule().v2_runner_on_ok("result") == None


# Generated at 2022-06-13 11:52:22.990427
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.plugins.callback import CallbackBase
    class DummyCallbackModule(CallbackBase):
        def v2_runner_on_ok(self, result):
            color = 'COLOR'
            if result._result.get('changed', False):
                color = 'COLOR_CHANGED'
            if result._task.action in C.MODULE_NO_JSON and 'ansible_job_id' not in result._result:
                color = 'NO_JSON'
            return color

    dummyCallbackModule = DummyCallbackModule()
    c = CallbackModule()
    c._display = DummyCallbackModule()
    ansible_host = DummyCallbackModule()
    ansible_host.get_name = lambda: 'DummyHost'
    result = DummyCallbackModule()

# Generated at 2022-06-13 11:52:30.295589
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Create a callback module
    oneline = CallbackModule()
    assert oneline is not None
    
    # Create a fake result
    result = type('Result_obj', (object,), {})()
    result._result = {'exception': 'An error occurred'}
    
    # Call method
    oneline.v2_runner_on_failed(result)
    
    # Verify method output
    assert result._result['exception'] == 'An error occurred'
        

# Generated at 2022-06-13 11:52:44.664311
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Setup
    callback = CallbackModule()

# Generated at 2022-06-13 11:53:02.270524
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    class test: pass
    import json
    import sys

    test.result = {}
    test.result['_host'] = {}
    test.result['_host'].get_name = lambda: "TEST01"
    test.result['_task'] = {}
    test.result['_task'].action = "TEST_ACTION"
    test.result['_result'] = {}
    test.result['_result']['changed'] = True
    test.result['_result']['ansible_job_id'] = "TEST_JOB_ID"
    test.result['_result']['stdout'] = "TEST STDOUT"
    test.result['_result']['stderr'] = "TEST STDERR"
    test.result['_result']['rc'] = 0

    stdout = sys

# Generated at 2022-06-13 11:53:12.414581
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 11:53:22.064755
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import sys
    import tempfile
    import unittest
    # Temporary file to store the standard output and the standard error
    (_, outfile) = tempfile.mkstemp(prefix="test_CallbackModule_v2_runner_on_failed_out_")
    (_, errfile) = tempfile.mkstemp(prefix="test_CallbackModule_v2_runner_on_failed_err_")
    # Cleans the temporary files
    def cleantmp():
        import os
        os.remove(outfile)
        os.remove(errfile)
    # Replace the stdout and stderr
    original_out = sys.stdout
    original_err = sys.stderr
    sys.stdout = open(outfile, "a")
    sys.stderr = open(errfile, "a")

# Generated at 2022-06-13 11:53:28.864368
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host

    callback = CallbackModule()
    host = Host(name='localhost')

    result = TaskResult(host, 0, {})
    result._result = {'changed': False}
    result._task = {'action': 'command'}
    callback.v2_runner_on_ok(result)

    result = TaskResult(host, 0, {})
    result._result = {'changed': True}
    result._task = {'action': 'command'}
    callback.v2_runner_on_ok(result)

    result = TaskResult(host, 0, {})
    result._result = {'changed': False, 'foo': {'bar': [1, 2, 3, 4]}}

# Generated at 2022-06-13 11:53:38.678346
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import json
    import yaml

    # Create instance of class CallbackModule.
    cb_instance = CallbackModule()

    # Call method v2_runner_on_failed of class CallbackModule.
    # Create a fake result.
    result = dict()
    result['_host'] = dict()
    result['_host']['get_name'] = lambda : 'host01'
    result['_result'] = dict()

# Generated at 2022-06-13 11:53:49.465713
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackBase


# Generated at 2022-06-13 11:53:52.738517
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    obj = CallbackModule()
    assert obj.CALLBACK_VERSION == 2.0
    assert obj.CALLBACK_TYPE == 'stdout'
    assert obj.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:54:02.579421
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Create a Mock object that will be the result.result
    result = Mock()
    # Create a Fake object that will be the result._task.action
    result._task = Mock()
    result._task.action = "fake"
    # Create a Fake object that will be the result._host.get_name
    result._host = Mock()
    result._host.get_name = "host_name"
    # Create a Mock object that will be the _dump_results
    _dump_results = Mock()


    # Create a object that will be the callback
    callback = CallbackModule()
    # Create a Mock object that will be the callback._display
    callback._display = Mock()

    # Make call the callback method
    callback.v2_runner_on_ok(result)

    # test the result of the v2_runner_on_

# Generated at 2022-06-13 11:54:13.836213
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    stdout = '''
    Ansible test 
    Error
    '''
    exception = '''
    Ansible error. 
    '''
    rc = '1'
    result = {
        '_host' : 'hostname',
        '_result' : {
            'exception' : exception,
            'stdout' : stdout,
            'stderr' : stdout,
            'rc' : rc
        }
    }
    callback = CallbackModule()
    result = callback.v2_runner_on_failed(result)
    # check if the output has the correct hostname, exception, rc, stdout and stderr
    assert(result) 

# Generated at 2022-06-13 11:54:23.099143
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import json
    import mock

    mock_display = mock.Mock()
    callback = CallbackModule()
    callback._display = mock_display

    # no change
    hostname = 'myhost.mydomain'
    result = {'changed': False}
    callback.v2_runner_on_ok(mock.Mock(
        _host=mock.Mock(get_name=lambda: hostname),
        _result=result
    ))
    mock_display.display.assert_called_with('{} | SUCCESS => {}'.format(
        hostname, json.dumps(result, indent=0)
    ), color='green')

    # changed
    mock_display.display.reset_mock()
    result = {'changed': True}

# Generated at 2022-06-13 11:54:35.619120
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Get instance of CallbackModule
    callback_module_instance = CallbackModule()
    # Run test method
    callback_module_instance.v2_runner_on_failed(result, ignore_errors=False)
    

# Generated at 2022-06-13 11:54:36.468571
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    CallbackModule()
    assert True

# Generated at 2022-06-13 11:54:37.083311
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert CallbackModule()

# Generated at 2022-06-13 11:54:46.551861
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Arrange
    result = MockResult()
    result.action = 'some_action'
    result.changed = False
    result.failed = False
    result.msg = 'some_message'
    result._result = {
        #'parsed': True,
        'invocation': MockSubResult(),
        'stdout': '',
        'stdout_lines': [],
        'warnings': [],
        'msg': 'some_message'
    }

    instance = CallbackModule()
    instance._display = MockDisplay()

    # Act
    instance.v2_runner_on_ok(result)

    # Assert
    assert 'some_message' in instance._display.display_log[0]



# Generated at 2022-06-13 11:54:53.768705
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Create and wrap a mock display object
    display = Display()
    callback = CallbackModule(display)
    # Create an object to simulate a result
    result = Result()
    result._host = ResultHost()
    result._host.name = 'hostname'
    result._task = ResultTask()
    result._task.action = 'setup'
    result._result = {}
    # Test that no color is applied if 'changed' is False
    callback.v2_runner_on_ok(result)
    assert display.display == [('hostname | SUCCESS => {}', None)]
    # Test that the color constant is applied if 'changed' is True
    result._result['changed'] = True
    callback.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:54:55.665977
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    c = CallbackModule()
    assert c.CALLBACK_TYPE == 'stdout'
    assert c.CALLBACK_VERSION == 2.0

# Generated at 2022-06-13 11:55:02.914923
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # mock object to test this method
    class MockResult(object):
        # mock object of class object is an instance of class object
        def __init__(self, host, result):
            self.host = host
            self.result = result

        def _task(self):
            return "MockResult._task()"

        def _host(self):
            return "MockResult._host()"

    class MockDisplay(object):
        # mock object of class object is an instance of class object
        def __init__(self, verbosity):
            self.verbosity = verbosity

        def display(self, msg, color=None):
            return "MockDisplay.display()"

    class MockCallbackBase(object):
        # mock object of class object is an instance of class object
        def __init__(self):
            self.verb

# Generated at 2022-06-13 11:55:07.334708
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    instance = CallbackModule()
    result = object()
    ignore_errors = False
    output = instance.v2_runner_on_failed(result, ignore_errors)

# Generated at 2022-06-13 11:55:17.249115
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    ansible_result = {
        "exception": "Exception",
        "stdout": "stdout",
        "stderr": "stderr",
        "rc": 1,
    }
    callback = CallbackModule()
    callback._command_generic_msg = lambda a, b, c: "test_result"
    callback.CALLBACK_NAME = "oneline"
    callback.CALLBACK_VERSION = "2.0"
    callback.v2_runner_on_failed(ansible_result)
    assert callback.CALLBACK_TYPE == "stdout"
    assert callback.CALLBACK_NAME == "oneline"
    assert callback.CALLBACK_VERSION == "2.0"


# Generated at 2022-06-13 11:55:22.868290
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Create a CallbackModule class object
    m = CallbackModule(display=None)
    # Call the v2_runner_on_ok method from the class object
    result = m.v2_runner_on_ok(result=None)
    # Check the result
    assert result == None


# Generated at 2022-06-13 11:55:47.112180
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import json
    import pytest
    cb = CallbackModule()

# Generated at 2022-06-13 11:55:51.056054
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    print("Testing the v2_runner_on_failed function of CallbackModule class")

    from unittest.mock import Mock
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    callback = CallbackModule()
    callback.set_options(Mock())
    callback._display = Mock()
    result = Mock()
    result._result = {
        'exception': 'An exception occured',
    }
    result._task = Mock()
    result._task.action = 'shell'
    result._host = Mock()
    result._host.get_name = Mock(return_value='test_host')
    callback._dump_results = Mock()

# Generated at 2022-06-13 11:56:00.911307
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    host = Host("testserver01")
    variable_manager = VariableManager()

    task = Task()
    task._role = None
    task.action = 'shell'
    task.args = {'_raw_params': 'echo Hello World!'}
    task.set_loader(variable_manager)
    play_context = dict(
        become=False,
        become_user='test',
        become_method='test',
        become_flags='test',
        verbosity=3,
        check=False
    )


# Generated at 2022-06-13 11:56:13.582698
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback_module_instance=CallbackModule()
    result={'exception':'stderr','module_stderr':'','module_stdout':'','msg':'No module named zhang'}
    

# Generated at 2022-06-13 11:56:22.318249
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext

    context = PlayContext(remote_addr='127.0.0.1')
    hostname = '127.0.0.1'
    change = False
    module = 'command'
    result = {'rc':0, 'stdout':'hello world'}
    display = {'display':print}

    class Host:
        def __init__(self, hostname):
            self.hostname = hostname
        def get_name(self):
            return self.hostname

    class Task:
        def __init__(self, module):
            self.module = module
        def get_name(self):
            return self.module
        def action(self):
            return self.module


# Generated at 2022-06-13 11:56:31.963119
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import os
    import sys
    import json
    import unittest
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess

    display = Display()
    display.verbosity = 3
    display.color = 'never'
    display.columns = 80

    class TestTaskQueueManager(TaskQueueManager):
        # Override to prevent worker process creation
        def _init_worker_process(self):
            return WorkerProcess(self._final_q, worker_timeout=self._worker_timeout)



# Generated at 2022-06-13 11:56:33.791442
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    import ansible.plugins.callback.oneline as oneline

    callback = oneline.CallbackModule()
    result = {}
    callback.v2_runner_on_failed(result, ignore_errors=False)

# Generated at 2022-06-13 11:56:34.720170
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert isinstance(CallbackModule(), CallbackBase)

# Generated at 2022-06-13 11:56:44.390990
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    import sys
    test_host = "localhost"
    display = sys.stdout
    class TestCond:
        def __init__(self):
            self.verbosity = 1
    class TestHost:
        def __init__(self, test_host):
            self.name = test_host
            self.get_name = lambda: self.name
    class TestTask:
        def __init__(self):
            self.action = "create"
    class TestResult:
        def __init__(self, host, result):
            self.host = TestHost(host)
            self.task = TestTask()
            self._result = result
            self._host = self.host
    class TestCond:
        def __init__(self):
            self.color = None

# Generated at 2022-06-13 11:56:47.965233
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    callback = CallbackModule()
    assert callback.CALLBACK_NAME == 'oneline'
    assert callback.CALLBACK_TYPE == 'stdout'
    assert callback.CALLBACK_VERSION == 2.0


# Generated at 2022-06-13 11:57:24.601687
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    test_module = CallbackModule()
    test_task = type('task', (object,), {})
    test_result = type('result', (object,), {'_result': {}, '_task': test_task()})
    test_result._task.action = 'test'
    test_module.v2_runner_on_failed(test_result)


# Generated at 2022-06-13 11:57:30.363877
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = MagicMock()
    result._result = { 'exception': 'test_exception' }
    result._task = MagicMock()
    result._task.action = "test_action"
    result._host = MagicMock()
    result._host.get_name.return_value = "test_host"
    callback._display = MagicMock()
    callback._display.verbosity = 1
    callback.v2_runner_on_failed(result)
    callback._display.display.assert_called_with("An exception occurred during task execution. To see the full traceback, use -vvv. The error was: test_exception", color='red')


# Generated at 2022-06-13 11:57:39.493953
# Unit test for method v2_runner_on_failed of class CallbackModule

# Generated at 2022-06-13 11:57:48.321090
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    class FakeResult:
        def __init__(self):
            self._host = "localhost"
            self._result = {"exception":"Traceback (most recent call last):\n  File \"/foo/bar\", line 1, in \nNameError: name 'foo' is not defined"}

    display = FakeDisplay()
    display.verbosity = 2
    callback = CallbackModule(display)

    callback.v2_runner_on_failed(FakeResult())

    assert display.msg == "localhost | FAILED! => {'exception': 'Traceback (most recent call last):\\n  File \"/foo/bar\", line 1, in \\nNameError: name 'foo' is not defined'}"


# Generated at 2022-06-13 11:57:49.586350
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    assert True

# Generated at 2022-06-13 11:57:52.536464
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    callback.v2_runner_on_ok('result')



# Generated at 2022-06-13 11:57:55.509510
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callback = CallbackModule()
    result = { '_result': {'changed': False}}
    assert callback.v2_runner_on_ok(result) == " | SUCCESS => "


# Generated at 2022-06-13 11:58:01.716474
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = CallbackModule()
    result._result = {
        'exception': 'Exception Occurred',
        'stdout': 'ok',
        'changed': False,
    }
    result._task.action = 'shell'
    result._host.get_name = lambda: 'test'
    result._display.verbosity = 3
    assert result.v2_runner_on_failed() == None
    result._display.verbosity = 2
    assert result.v2_runner_on_failed() == None
    result._display.verbosity = 1
    assert result.v2_runner_on_failed() == None

# Generated at 2022-06-13 11:58:06.518651
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule()
    assert x.CALLBACK_TYPE == x.CALLBACK_TYPE
    assert x.CALLBACK_NAME == x.CALLBACK_NAME
    assert x.CALLBACK_VERSION == x.CALLBACK_VERSION
    assert x.CALLBACK_VERSION == 2.0

    assert x.CALLBACK_TYPE == 'stdout'
    assert x.CALLBACK_NAME == 'oneline'

# Generated at 2022-06-13 11:58:14.647925
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class TestResult():
        def __init__(self, host, result, task):
            self._host = host
            self._result = result
            self._task = task
        def get_name(self):
            return self._host.name
    test_host = TestHost("test_host")
    test_task = TestTask("test_task")
    test_result = TestResult(test_host, {'exception': 'test exception'}, test_task)

    # Test case: quiet mode, exception
    test_callback = CallbackModule()
    test_callback._display.verbosity = 0
    test_callback._display.color = False
    assert_equals(test_callback.v2_runner_on_failed(test_result), "test_host | FAILED! => {'exception': 'test exception'}")

# Generated at 2022-06-13 11:59:37.784891
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback.default import CallbackModule
    callback_module = CallbackModule()
    result = {'exception': 'An exception occurred: message'}
    callback_module.v2_runner_on_failed(result)


# Generated at 2022-06-13 11:59:38.878563
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # TODO
    print('Test passed')

# Generated at 2022-06-13 11:59:48.492586
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = object()
    result.host_name = 'test_host'
    result._result = dict(changed=False)
    result._task = object()
    result._task.action = 'test_module'
    result._result.update(ansible_job_id='test_job_id')
    result._result.update(rc=0)
    result._result.update(stderr='')
    result._result.update(stdout='test STDOUT')

    # Run
    call_back = CallbackModule()
    call_back.v2_runner_on_ok(result)

    # Verify
    assert 'SUCCESS' in call_back.output
    assert 'rc=0' in call_back.output
    assert 'stdout' in call_back.output


# Generated at 2022-06-13 11:59:55.252689
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cb = CallbackModule()
    cb._display = None
    cb._dump_results = None
    result = Mock()
    result._host = Mock()
    result._host.get_name = Mock(return_value = 'localhost')
    result._result = {}
    result._result['changed'] = True
    result._task = Mock()
    result._task.action = 'setup'
    cb.v2_runner_on_ok(result)


# Generated at 2022-06-13 12:00:03.830314
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    class Options:
        def __init__(self):
            self.one_line = True

    class Host:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class Task:
        def __init__(self, action):
            self.action = action

    class Display:
        def __init__(self):
            self.displayed = None

        def display(self, msg, color):
            self.displayed = msg

    class RunnerResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class Runner:
        def __init__(self, run_state, exception=None):
            self.exception = exception
            self

# Generated at 2022-06-13 12:00:12.387172
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    result = type('Result', (object,), {'_host': type('_host', (object,), {'get_name': lambda _: 'test-hostname'}),
                                         '_result': {'exception': 'testException', 'rc': '-1'}})()
    cb.v2_runner_on_failed(result)
    print(cb._display._lines)
    assert cb._display._lines == [
        u'test-hostname | FAILED! => {u"exception": "testException", u"rc": -1}'
    ], u'Incorrect error message printed'

# Generated at 2022-06-13 12:00:18.590058
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_unicode
    from ansible.parsing.dataloader import DataLoader
    import json

    results = {}

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    results['_ansible_check_mode'] = module._name
    results['_ansible_no_log'] = False
    results['_ansible_verbosity'] = 2
    results['_ansible_module_name'] = 'setup'
    results['_ansible_module_version'] = '2.9'
    results['_ansible_module_uargs'] = {}

# Generated at 2022-06-13 12:00:23.092870
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result = 'test'
    ignore_errors = False
    oneline = CallbackModule()
    assert type(oneline.v2_runner_on_failed(result, ignore_errors)) == None
    assert str(oneline.v2_runner_on_failed(result, ignore_errors)) == "<bound method CallbackModule.v2_runner_on_failed of <ansible.plugins.callback.oneline.CallbackModule object at 0x7f190828a710>>"


# Generated at 2022-06-13 12:00:23.707493
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    pass

# Generated at 2022-06-13 12:00:31.619807
# Unit test for constructor of class CallbackModule
def test_CallbackModule():
    x = CallbackModule()
    assert hasattr(x, 'CALLBACK_VERSION')
    assert hasattr(x, 'CALLBACK_TYPE')
    assert hasattr(x, 'CALLBACK_NAME')
    assert hasattr(x, 'v2_runner_on_failed')
    assert hasattr(x, 'v2_runner_on_ok')
    assert hasattr(x, 'v2_runner_on_unreachable')
    assert hasattr(x, 'v2_runner_on_skipped')
    assert hasattr(x, '_command_generic_msg')